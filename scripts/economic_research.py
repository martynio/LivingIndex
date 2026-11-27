#!/usr/bin/env python3
"""Normalize reviewed HBS probe reports into research-only JSON. No promotion API."""
import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
import re
from urllib.parse import parse_qs, urlsplit

BASE = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/hbs_exp_t121'
COUNTRIES = ('PL', 'NL')
DIVISIONS = tuple(f'CP{i:02d}' for i in range(1, 13))
HASH = re.compile(r'[0-9a-f]{64}')
MAX_BYTES = 5_000_000


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'Duplicate JSON key')
        result[key] = value
    return result


def timestamp(value):
    require(isinstance(value, str), 'Missing timestamp')
    dt = datetime.fromisoformat(value)
    require(dt.utcoffset() is not None, 'Timestamp needs offset')
    return value


def normalize(raw, expected_sha256):
    """The caller supplies the independently recorded report digest, not an API digest."""
    require(len(raw) <= MAX_BYTES, 'Report too large')
    digest = hashlib.sha256(raw).hexdigest()
    require(digest == expected_sha256, 'Report digest mismatch')
    d = json.loads(raw, object_pairs_hook=unique_object)
    require(isinstance(d, dict), 'Expected report object')
    require(d.get('source') == 'Eurostat' and d.get('dataset') == 'hbs_exp_t121', 'Wrong source')
    require(d.get('http_status') == 200, 'Unsuccessful retrieval')
    require(d.get('result') in ('OBSERVATIONS_RETRIEVED_REVIEW_REQUIRED', 'INCOMPLETE_REVIEW_REQUIRED'), 'Unsupported result')
    require(isinstance(d.get('sha256_response'), str) and HASH.fullmatch(d['sha256_response']), 'Missing response digest')
    url = urlsplit(d['url'])
    require(url.geturl().split('?')[0] == BASE and not url.fragment, 'Wrong endpoint')
    q = parse_qs(url.query, strict_parsing=True)
    matrix = 'category_indices' in d
    categories = DIVISIONS if matrix else ('CP01',)
    expected = {'lang':['EN'], 'geo':list(COUNTRIES), 'time':['2020'], 'unit':['PPS_HH'], 'coicop':list(categories)}
    if matrix:
        expected['freq'] = ['A']
    require(q == expected, 'Query outside approved scope')
    dims, sizes = d['dimensions'], d['sizes']
    time = 'time_period' if 'time_period' in dims else 'time'
    require(len(dims) == 5 and set(dims) == {'freq','geo','coicop','unit',time}, 'Wrong dimensions')
    require(len(sizes) == 5 and all(type(s) is int and 1 <= s <= 12 for s in sizes), 'Wrong dimensions sizes')
    axes = d.get('category_indices')
    if matrix:
        require(isinstance(axes, dict) and set(axes) == set(dims), 'Missing category axes')
        allowed = {'freq':{'A'}, 'unit':{'PPS_HH'}, time:{'2020'}, 'geo':set(COUNTRIES), 'coicop':set(categories)}
        for dim, size in zip(dims, sizes):
            a = axes[dim]
            require(isinstance(a, dict) and len(a) == size and set(a) <= allowed[dim], 'Invalid axis')
            require(all(type(v) is int for v in a.values()) and set(a.values()) == set(range(size)), 'Invalid axis positions')
            if dim not in ('geo', 'coicop'):
                require(set(a) == allowed[dim], 'Missing singleton coordinate')
    else:
        require(sizes == [2 if dim == 'geo' else 1 for dim in dims], 'Invalid legacy shape')
    records = []
    seen = set()
    offsets = set()
    for row in d['observations']:
        geo = row['country']
        cp = row['coicop'] if matrix else 'CP01'
        key = (geo, cp)
        require(geo in COUNTRIES and cp in categories and key not in seen, 'Invalid/duplicate observation')
        seen.add(key)
        value, flag, offset = row['value'], row['source_flag'], row['flat_index']
        require(value is None or (type(value) in (int, float) and math.isfinite(value) and value >= 0), 'Invalid expenditure')
        require(flag is None or isinstance(flag, str), 'Invalid flag')
        if matrix:
            coords = {'freq':'A','geo':geo,'coicop':cp,'unit':'PPS_HH',time:'2020'}
            calculated = None
            if all(coords[dim] in axes[dim] for dim in dims):
                calculated = 0
                for dim, size in zip(dims, sizes):
                    calculated = calculated * size + axes[dim][coords[dim]]
            require(offset == calculated and (offset is None or type(offset) is int), 'Offset mismatch')
        if offset is None:
            require(matrix and value is None and flag is None, 'Invalid absent coordinate')
        else:
            require(type(offset) is int and 0 <= offset < math.prod(sizes) and offset not in offsets, 'Invalid/duplicate offset')
            offsets.add(offset)
        records.append({'country':geo, 'year':2020, 'category':cp, 'value':value, 'source_flag':flag,
                        'source_flat_index':offset, 'availability':'missing' if value is None else 'observed'})
    require(seen == {(g,c) for g in COUNTRIES for c in categories}, 'Incomplete observation keys')
    missing = sum(r['value'] is None for r in records)
    if matrix:
        require(type(d.get('expected_cells')) is int and d['expected_cells'] == 24 and type(d.get('missing_cells')) is int and d['missing_cells'] == missing, 'Invalid coverage count')
    require((missing > 0) == (d['result'] == 'INCOMPLETE_REVIEW_REQUIRED'), 'Result/coverage mismatch')
    return {'schema_version':'1.0.0', 'kind':'research_observations', 'production_eligible':False,
            'source_id':'LI-SRC-009', 'dataset':'hbs_exp_t121', 'measure':'mean_consumption_expenditure',
            'unit':'PPS_HH', 'population':'survey_households', 'frequency':'annual', 'statistic':'mean',
            'provenance':{'query':d['url'], 'report_created_at':timestamp(d['created_at_utc']),
                          'retrieved_at':timestamp(d['retrieved_at_utc']) if matrix else None,
                          'dataset_updated':d.get('dataset_updated'), 'report_sha256':digest,
                          'api_sha256_reported':d['sha256_response'], 'api_bytes_independently_checked':False,
                          'coordinate_evidence':'report_axes' if matrix else 'legacy_query_and_shape_only'},
            'review':{'rights':'pending', 'methodology':'pending', 'independent_cell_check':'pending',
                      'operator_approval':'pending'}, 'observations':sorted(records,key=lambda r:(r['country'],r['category']))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    parser.add_argument('--sha256', required=True)
    parser.add_argument('--output', type=Path, help='New private/local file outside repository; optional')
    args = parser.parse_args()
    try:
        with args.report.open('rb') as stream:
            data = normalize(stream.read(MAX_BYTES + 1), args.sha256)
        if args.output:
            out = args.output.resolve()
            require(not out.is_relative_to(Path(__file__).resolve().parents[1]), 'Output must be outside repository')
            with out.open('x', encoding='utf-8') as stream:
                json.dump(data, stream, indent=2, allow_nan=False)
                stream.write('\n')
        print(f"RESEARCH ONLY: {len(data['observations'])} records; production_eligible=false")
        return 0
    except (ValueError, KeyError, TypeError, OSError, OverflowError) as exc:
        print(f'REJECTED: {type(exc).__name__}', flush=True)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
