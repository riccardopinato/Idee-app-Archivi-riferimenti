import copy
import json
import unittest

from scripts.factory_10x_metrics import LEDGER, validate

class MetricsContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(LEDGER.read_text(encoding="utf-8"))

    def test_eight_unmeasured_baselines(self):
        self.assertEqual(validate(self.data), {"metrics":8,"verified_samples":0,"unmeasured":8})

    def test_false_baseline_rejected(self):
        x = copy.deepcopy(self.data)
        x["metrics"][0]["baseline"]["value"] = 10
        with self.assertRaises(ValueError):
            validate(x)

    def test_false_verification_rejected(self):
        x = copy.deepcopy(self.data)
        x["metrics"][0]["assurance"] = "VERIFIED"
        with self.assertRaises(ValueError):
            validate(x)

    def test_unreviewed_sample_rejected(self):
        x = copy.deepcopy(self.data)
        x["metrics"][0]["observations"].append({
            "source_sha":"a"*40,"source_url":"https://github.com/a/b/commit/"+"a"*40,
            "gate_reviewed":False,"cohort":"sample","period":"2026-W46",
            "value":3,"checked_at":"2026-11-12T01:00:00Z"
        })
        with self.assertRaises(ValueError):
            validate(x)

    def test_private_revenue_forbidden(self):
        x = copy.deepcopy(self.data)
        revenue = next(m for m in x["metrics"] if m["id"]=="net_revenue_per_product")
        revenue["observations"]=[{"value":12}]
        with self.assertRaises(ValueError):
            validate(x)

    def test_reviewed_ratio_validated_and_duplicate_rejected(self):
        x=copy.deepcopy(self.data)
        m=next(y for y in x["metrics"] if y["id"]=="reuse_ratio")
        row={"source_sha":"a"*40,"source_url":"https://github.com/a/b/commit/"+"a"*40,
             "gate_reviewed":True,"cohort":"pilot","period":"2026-W46",
             "value":0.25,"checked_at":"2026-11-12T01:00:00Z"}
        m["observations"].append(row)
        self.assertEqual(validate(x)["verified_samples"],1)
        m["observations"].append(row)
        with self.assertRaises(ValueError):
            validate(x)

if __name__=="__main__":
    unittest.main()
