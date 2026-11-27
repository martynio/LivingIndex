"""Synthetic report fixtures only, never production observations."""
import hashlib
import json
from pathlib import Path
import sys
import unittest
from urllib.parse import urlencode

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import economic_research as model


def fixture(matrix=False):
    cats = model.DIVISIONS if matrix else ('CP01',)
    q = [('lang','EN'),('geo','PL'),('geo','NL'),('time','2020'),('unit','PPS_HH')]
    q += [('coicop',c) for c in cats]
    if matrix:
        q.append(('freq','A'))
    rows = []
    for i,g in enumerate(model.COUNTRIES):
        for j,c in enumerate(cats):
            row = {'country':g,'value':i+j,'source_flag':None,'flat_index':i*len(cats)+j}
            if matrix:
                row['coicop'] = c
            rows.append(row)
    d = {'source':'Eurostat','dataset':'hbs_exp_t121','url':model.BASE+'?'+urlencode(q),
         'http_status':200,'result':'OBSERVATIONS_RETRIEVED_REVIEW_REQUIRED',
         'created_at_utc':'2020-01-01T00:00:00+00:00','sha256_response':'a'*64,
         'dimensions':['freq','geo','coicop','unit','time'],'sizes':[1,2,len(cats),1,1],
         'observations':rows}
    if matrix:
        d.update(retrieved_at_utc=d['created_at_utc'],expected_cells=24,missing_cells=0,
                 category_indices={'freq':{'A':0},'geo':{'PL':0,'NL':1},'coicop':{c:i for i,c in enumerate(cats)},'unit':{'PPS_HH':0},'time':{'2020':0}})
    return d


def load(d):
    raw = json.dumps(d).encode()
    return model.normalize(raw, hashlib.sha256(raw).hexdigest())


class ResearchTests(unittest.TestCase):
    def test_legacy_zero_and_provenance(self):
        r = load(fixture())
        self.assertFalse(r['production_eligible'])
        self.assertEqual(r['observations'][1]['value'], 0)
        self.assertEqual(r['observations'][1]['availability'], 'observed')
        self.assertEqual(r['unit'], 'PPS_HH')
        self.assertEqual(r['provenance']['coordinate_evidence'], 'legacy_query_and_shape_only')

    def test_matrix(self):
        r = load(fixture(True))
        self.assertEqual(len(r['observations']), 24)
        self.assertEqual(r['provenance']['coordinate_evidence'], 'report_axes')
        self.assertFalse(r['production_eligible'])

    def test_missing_is_not_zero(self):
        d = fixture(True)
        d['observations'][0].update(value=None,source_flag='u')
        d.update(missing_cells=1,result='INCOMPLETE_REVIEW_REQUIRED')
        r = load(d)['observations'][12]
        self.assertIsNone(r['value'])
        self.assertEqual(r['availability'], 'missing')
        self.assertEqual(r['source_flag'], 'u')

    def test_wrong_digest(self):
        with self.assertRaisesRegex(ValueError, 'digest mismatch'):
            model.normalize(b'{}','0'*64)

    def test_duplicate_json(self):
        raw = b'{"source":1,"source":2}'
        with self.assertRaisesRegex(ValueError, 'Duplicate JSON'):
            model.normalize(raw,hashlib.sha256(raw).hexdigest())

    def test_wrong_unit(self):
        d = fixture(); d['url'] = d['url'].replace('PPS_HH','EUR')
        with self.assertRaises(ValueError): load(d)

    def test_wrong_axis(self):
        d = fixture(True); d['category_indices']['freq'] = {'Q':0}
        with self.assertRaises(ValueError): load(d)

    def test_duplicate_coordinate(self):
        d = fixture(); d['observations'][1]['country'] = 'PL'
        with self.assertRaises(ValueError): load(d)

    def test_missing_coordinate(self):
        d = fixture(); d['observations'].pop()
        with self.assertRaises(ValueError): load(d)

    def test_bad_offset(self):
        d = fixture(True); d['observations'][0]['flat_index'] = 4
        with self.assertRaises(ValueError): load(d)

    def test_bad_numbers(self):
        for v in (True,-1,float('nan'),float('inf'),'1'):
            with self.subTest(v=v):
                d = fixture(); d['observations'][0]['value'] = v
                with self.assertRaises(ValueError): load(d)

    def test_mismatched_result(self):
        d = fixture(True); d['observations'][0]['value'] = None
        with self.assertRaises(ValueError): load(d)

    def test_no_promotion_by_input(self):
        d = fixture(); d['production_eligible'] = True; d['review'] = {'rights':'approved'}
        r = load(d)
        self.assertFalse(r['production_eligible'])
        self.assertEqual(r['review']['rights'],'pending')


if __name__ == '__main__':
    unittest.main()
