"""Synthetic JSON-stat fixtures: these are NOT economic observations."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import hbs_probe


def fixture():
    # Flat order: unit x geo x coicop x time; arbitrary numbers used only in tests.
    return {"class": "dataset", "id": ["unit", "geo", "coicop", "time"], "size": [1, 2, 1, 1],
            "dimension": {"unit": {"category": {"index": {"PPS_HH": 0}}},
                          "geo": {"category": {"index": {"PL": 0, "NL": 1}}},
                          "coicop": {"category": {"index": {"CP01": 0}}},
                          "time": {"category": {"index": {"2020": 0}}}},
            "value": {"0": 12.0, "1": 15.0}, "status": {"1": "p"}}


class ProbeTests(unittest.TestCase):
    def test_query_is_fixed_and_small(self):
        url = hbs_probe.query_url()
        self.assertIn("geo=PL&geo=NL", url)
        self.assertIn("unit=PPS_HH", url)

    def test_sparse_values_and_flags(self):
        result = hbs_probe.analyze(fixture())
        self.assertEqual(result["observations"][0]["value"], 12)
        self.assertEqual(result["observations"][1]["source_flag"], "p")
        self.assertEqual(result["result"], "OBSERVATIONS_RETRIEVED_REVIEW_REQUIRED")

    def test_dense_values_reverse_dimensions(self):
        f = fixture()
        f["id"] = ["geo", "time", "unit", "coicop"]
        f["size"] = [2, 1, 1, 1]
        f["value"] = [23, 24]
        self.assertEqual(hbs_probe.observation(f, "NL")["value"], 24)

    def test_category_index_array(self):
        f = fixture()
        f["dimension"]["geo"]["category"]["index"] = ["NL", "PL"]
        f["value"] = [33, 44]
        self.assertEqual(hbs_probe.observation(f, "PL")["value"], 44)

    def test_missing_value_does_not_become_zero(self):
        f = fixture()
        f["value"] = {"0": 12}
        with self.assertRaisesRegex(ValueError, "NL"):
            hbs_probe.analyze(f)

    def test_unfiltered_dimensions_are_rejected(self):
        f = fixture()
        f["id"].append("household")
        f["size"].append(2)
        f["dimension"]["household"] = {"category": {"index": {"A": 0, "B": 1}}}
        with self.assertRaisesRegex(ValueError, "Unfiltered"):
            hbs_probe.analyze(f)

    def test_invalid_class_rejected(self):
        with self.assertRaisesRegex(ValueError, "JSON-stat"):
            hbs_probe.analyze({"class": "error"})

    def test_no_bool_as_numeric(self):
        f = fixture()
        f["value"]["1"] = True
        with self.assertRaisesRegex(ValueError, "invalid numeric"):
            hbs_probe.analyze(f)


if __name__ == "__main__":
    unittest.main()
