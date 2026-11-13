#!/usr/bin/env python3
"""Read-only, evidence-only Eurostat HBS 2020 PL/NL probe. No data publication."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/hbs_exp_t121"
MAX_BYTES = 5_000_000


def query_url():
    params = [("lang", "EN"), ("geo", "PL"), ("geo", "NL"),
              ("time", "2020"), ("unit", "PPS_HH"), ("coicop", "CP01")]
    return BASE + "?" + urllib.parse.urlencode(params)


def position(data, dim, code):
    part = data.get("dimension", {}).get(dim)
    if not isinstance(part, dict):
        raise ValueError(f"Missing dimension: {dim}")
    index = part.get("category", {}).get("index")
    if isinstance(index, dict):
        if code not in index:
            raise ValueError(f"Missing {dim}={code}")
        pos = index[code]
    elif isinstance(index, list):
        if code not in index:
            raise ValueError(f"Missing {dim}={code}")
        pos = index.index(code)
    else:
        raise ValueError(f"Missing category index for {dim}")
    if not isinstance(pos, int) or isinstance(pos, bool) or pos < 0:
        raise ValueError(f"Invalid category position for {dim}={code}")
    return pos


def at_flat(values, offset):
    if isinstance(values, list):
        return values[offset] if offset < len(values) else None
    if isinstance(values, dict):
        return values.get(str(offset))
    raise ValueError("Expected JSON-stat value/status array or object")


def observation(data, geo):
    if not isinstance(data, dict) or data.get("class") != "dataset":
        raise ValueError("Not a JSON-stat dataset")
    dims, sizes = data.get("id"), data.get("size")
    if not isinstance(dims, list) or not isinstance(sizes, list) or len(dims) != len(sizes):
        raise ValueError("Malformed dimensions and sizes")
    if len(set(dims)) != len(dims) or any(not isinstance(s, int) or isinstance(s, bool) or s < 1 for s in sizes):
        raise ValueError("Invalid dimension sizes")
    time_dim = "time" if "time" in dims else "time_period"
    wanted = {"geo": geo, time_dim: "2020", "unit": "PPS_HH", "coicop": "CP01"}
    if not all(d in dims for d in wanted):
        raise ValueError("Missing required geo/time/unit/coicop dimension")
    offset = 0
    for dim, size in zip(dims, sizes):
        if dim in wanted:
            pos = position(data, dim, wanted[dim])
        elif size == 1:
            pos = 0
        else:
            raise ValueError(f"Unfiltered dimension {dim} has {size} categories")
        if pos >= size:
            raise ValueError(f"Invalid position for {dim}")
        offset = offset * size + pos
    value = at_flat(data.get("value"), offset)
    if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value):
        raise ValueError(f"Missing/invalid numeric observation for {geo}")
    status = data.get("status")
    flag = at_flat(status, offset) if status is not None else None
    return {"country": geo, "value": value, "source_flag": flag, "flat_index": offset}


def analyze(data):
    observations = [observation(data, geo) for geo in ("PL", "NL")]
    return {"result": "OBSERVATIONS_RETRIEVED_REVIEW_REQUIRED", "observations": observations,
            "dimensions": data["id"], "sizes": data["size"], "dataset_updated": data.get("updated"),
            "disclaimer": "Exploratory PPS per household. Not PLN/EUR monthly spending, not methodologically approved."}


def retrieve(url):
    req = urllib.request.Request(url, headers={"User-Agent": "LivingIndex-Research-Probe/0.1", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=35) as response:
        raw = response.read(MAX_BYTES + 1)
        content_type = response.headers.get("Content-Type", "")
        http_status = response.status
    if len(raw) > MAX_BYTES:
        raise ValueError("Response exceeds 5 MB research limit")
    if "json" not in content_type.lower():
        raise ValueError(f"Unexpected Content-Type: {content_type}")
    parsed = json.loads(raw.decode("utf-8"))
    return parsed, hashlib.sha256(raw).hexdigest(), http_status


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    url = query_url()
    report = {"created_at_utc": datetime.now(timezone.utc).isoformat(), "source": "Eurostat",
              "dataset": "hbs_exp_t121", "url": url, "purpose": "Research-only 2020 PL/NL CP01 PPS_HH probe",
              "source_rights": "Review before publishing raw observations", "result": "BLOCKED"}
    try:
        data, digest, http_status = retrieve(url)
        report["sha256_response"] = digest
        report["http_status"] = http_status
        report.update(analyze(data))
    except (ValueError, OSError, urllib.error.URLError, json.JSONDecodeError) as exc:
        report["error"] = f"{type(exc).__name__}: {exc}"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{report['result']}: {args.output}")
    if report["result"] == "BLOCKED":
        print(report.get("error", "No valid observations"))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
