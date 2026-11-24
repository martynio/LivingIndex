#!/usr/bin/env python3
"""Read-only HBS 2020 PL/NL division coverage probe; no production data."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/hbs_exp_t121"
COUNTRIES = ("PL", "NL")
DIVISIONS = tuple(f"CP{i:02d}" for i in range(1, 13))
MAX_BYTES = 5_000_000


def query_url():
    pairs = [("lang", "EN"), ("freq", "A"), ("time", "2020"), ("unit", "PPS_HH")]
    pairs += [("geo", code) for code in COUNTRIES]
    pairs += [("coicop", code) for code in DIVISIONS]
    return BASE + "?" + urlencode(pairs)


def category_index(data, name, size):
    dim = data["dimension"][name]["category"]["index"]
    if isinstance(dim, list):
        if len(set(dim)) != len(dim):
            raise ValueError(f"Duplicate category in {name}")
        dim = {code: i for i, code in enumerate(dim)}
    if not isinstance(dim, dict) or len(dim) != size:
        raise ValueError(f"Invalid category count for {name}")
    if any(not isinstance(k, str) or type(v) is not int for k, v in dim.items()):
        raise ValueError(f"Invalid index in {name}")
    if set(dim.values()) != set(range(size)):
        raise ValueError(f"Non-contiguous or duplicate positions in {name}")
    return dim


def flat_value(values, offset, length):
    if isinstance(values, list) and len(values) == length:
        return values[offset]
    if isinstance(values, dict):
        return values.get(str(offset))
    raise ValueError("Invalid JSON-stat value/status shape")


def analyze(data):
    if not isinstance(data, dict) or data.get("class") != "dataset" or data.get("version") != "2.0":
        raise ValueError("Expected JSON-stat 2.0 dataset")
    dims, sizes = data["id"], data["size"]
    if not isinstance(dims, list) or not isinstance(sizes, list) or len(dims) != 5 or len(sizes) != 5:
        raise ValueError("Expected five dimensions")
    time = "time" if "time" in dims else "time_period"
    if set(dims) != {"freq", "coicop", "unit", "geo", time}:
        raise ValueError("Unexpected dimensions")
    if any(type(size) is not int or not 1 <= size <= 12 for size in sizes):
        raise ValueError("Invalid dimension size")
    axes = {name: category_index(data, name, size) for name, size in zip(dims, sizes)}
    for name, code in (("freq", "A"), ("unit", "PPS_HH"), (time, "2020")):
        if set(axes[name]) != {code}:
            raise ValueError(f"Unexpected {name} category")
    if not set(axes["geo"]).issubset(COUNTRIES) or not set(axes["coicop"]).issubset(DIVISIONS):
        raise ValueError("Unexpected country or consumption category")
    length = math.prod(sizes)
    observations = []
    for geo in COUNTRIES:
        for coicop in DIVISIONS:
            coords = {"freq": "A", "unit": "PPS_HH", time: "2020", "geo": geo, "coicop": coicop}
            value = flag = offset = None
            if all(code in axes[name] for name, code in coords.items()):
                offset = 0
                for name, size in zip(dims, sizes):
                    offset = offset * size + axes[name][coords[name]]
                value = flat_value(data["value"], offset, length)
                if data.get("status") is not None:
                    flag = flat_value(data["status"], offset, length)
                if value is not None and (type(value) not in (int, float) or not math.isfinite(value)):
                    raise ValueError(f"Invalid numeric value: {geo}/{coicop}")
                if flag is not None and not isinstance(flag, str):
                    raise ValueError(f"Invalid source flag: {geo}/{coicop}")
            observations.append({"country": geo, "coicop": coicop, "value": value,
                                 "source_flag": flag, "flat_index": offset})
    missing = sum(row["value"] is None for row in observations)
    return {"result": "INCOMPLETE_REVIEW_REQUIRED" if missing else "OBSERVATIONS_RETRIEVED_REVIEW_REQUIRED",
            "expected_cells": 24, "missing_cells": missing, "observations": observations,
            "dimensions": dims, "sizes": sizes, "category_indices": axes,
            "dataset_updated": data.get("updated")}


def fetch(url):
    request = Request(url, headers={"Accept": "application/json", "User-Agent": "LivingIndex-Research-Matrix/0.1"})
    with urlopen(request, timeout=35) as response:
        raw = response.read(MAX_BYTES + 1)
        status = response.status
        content_type = response.headers.get("Content-Type", "")
    if len(raw) > MAX_BYTES or status != 200 or "json" not in content_type.lower():
        raise ValueError("Unexpected HTTP status, content type or response size")
    return raw, status


def run_probe(fetcher=fetch):
    report = {"created_at_utc": datetime.now(timezone.utc).isoformat(), "source": "Eurostat",
              "dataset": "hbs_exp_t121", "url": query_url(), "result": "BLOCKED",
              "disclaimer": "Research-only PPS per household; no currency conversion, aggregation or production approval."}
    try:
        raw, status = fetcher(report["url"])
        report.update(http_status=status, sha256_response=hashlib.sha256(raw).hexdigest(),
                      retrieved_at_utc=datetime.now(timezone.utc).isoformat())
        if status != 200:
            raise ValueError(f"Unexpected HTTP status: {status}")
        report.update(analyze(json.loads(raw)))
    except (ValueError, OSError, KeyError, TypeError, OverflowError) as exc:
        report["error"] = f"{type(exc).__name__}: {exc}"
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    report = run_probe()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{report['result']}: {args.output}")
    return 0 if report["result"] == "OBSERVATIONS_RETRIEVED_REVIEW_REQUIRED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
