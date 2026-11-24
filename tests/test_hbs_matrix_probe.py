"""Synthetic fixtures only: no real economic observations."""
import hashlib
import json
from pathlib import Path
import sys
import unittest
from urllib.parse import parse_qs, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import hbs_matrix_probe as probe


def fixture():
    codes = {"freq": ["A"], "coicop": list(probe.DIVISIONS), "unit": ["PPS_HH"],
             "geo": ["NL", "PL"], "time": ["2020"]}
    dims = ["coicop", "geo", "unit", "time", "freq"]
    return {"class": "dataset", "version": "2.0", "id": dims,
            "size": [len(codes[d]) for d in dims],
            "dimension": {d: {"category": {"index": codes[d]}} for d in dims},
            "value": list(range(24)), "status": {"1": "p"}}


class MatrixTests(unittest.TestCase):
    def test_query_exact_scope(self):
        q = parse_qs(urlsplit(probe.query_url()).query)
        self.assertEqual(q["coicop"], list(probe.DIVISIONS))
        self.assertEqual(q["geo"], ["PL", "NL"])
        self.assertEqual((q["time"], q["freq"], q["unit"]), (["2020"], ["A"], ["PPS_HH"]))

    def test_named_axes_and_true_zero(self):
        result = probe.analyze(fixture())
        self.assertEqual(result["missing_cells"], 0)
        self.assertEqual(len(result["observations"]), 24)
        self.assertEqual(result["observations"][0]["value"], 1)
        self.assertEqual(result["observations"][0]["source_flag"], "p")
        self.assertEqual(result["observations"][12]["value"], 0)
        self.assertEqual(result["observations"][-1]["value"], 22)

    def test_sparse_missing_cell_preserves_flag(self):
        f = fixture()
        f["value"] = {str(i): i for i in range(24) if i != 1}
        r = probe.analyze(f)
        self.assertEqual(r["missing_cells"], 1)
        self.assertEqual(r["result"], "INCOMPLETE_REVIEW_REQUIRED")
        self.assertIsNone(r["observations"][0]["value"])
        self.assertEqual(r["observations"][0]["source_flag"], "p")

    def test_absent_division_is_missing_not_zero(self):
        f = fixture()
        f["dimension"]["coicop"]["category"]["index"] = list(probe.DIVISIONS[:-1])
        f["size"][0] = 11
        f["value"] = list(range(22))
        r = probe.analyze(f)
        self.assertEqual(r["missing_cells"], 2)
        self.assertIsNone(r["observations"][11]["flat_index"])
        self.assertIsNone(r["observations"][23]["value"])

    def test_wrong_frequency_rejected(self):
        f = fixture()
        f["dimension"]["freq"]["category"]["index"] = ["Q"]
        with self.assertRaisesRegex(ValueError, "freq"):
            probe.analyze(f)

    def test_bad_index_rejected(self):
        f = fixture()
        f["dimension"]["geo"]["category"]["index"] = {"PL": 0, "NL": 0}
        with self.assertRaisesRegex(ValueError, "positions"):
            probe.analyze(f)

    def test_invalid_numeric_rejected(self):
        f = fixture()
        f["value"][1] = True
        with self.assertRaisesRegex(ValueError, "numeric"):
            probe.analyze(f)

    def test_report_records_response_hash(self):
        raw = json.dumps(fixture()).encode()
        r = probe.run_probe(lambda url: (raw, 200))
        self.assertEqual(r["sha256_response"], hashlib.sha256(raw).hexdigest())
        self.assertEqual(r["result"], "OBSERVATIONS_RETRIEVED_REVIEW_REQUIRED")

    def test_transport_and_schema_errors_block(self):
        def fail(url):
            raise OSError("synthetic failure")
        self.assertEqual(probe.run_probe(fail)["result"], "BLOCKED")
        self.assertEqual(probe.run_probe(lambda url: (b"{}", 200))["result"], "BLOCKED")


if __name__ == "__main__":
    unittest.main()
