import copy
import json
import unittest

from scripts.factory_10x_package_contract import EXAMPLE, SCHEMA, verify

class GoldenPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example=json.loads(EXAMPLE.read_text(encoding="utf-8"))

    def test_design_only_is_not_a_package(self):
        self.assertEqual(verify(self.example),"DESIGN_ONLY")
        self.assertFalse(self.example["release"]["publish_authorized"])
        self.assertEqual(self.example["license"],"NOT_REVIEWED")
        self.assertFalse(self.example["compatibility"]["tested_pairs"])

    def test_schema_json_valid(self):
        s=json.loads(SCHEMA.read_text(encoding="utf-8"))
        self.assertEqual(s["properties"]["schema_version"]["const"],1)

    def test_unsigned_license_cannot_claim_tested(self):
        p=copy.deepcopy(self.example)
        p["package_state"]="PACKAGE_TESTED"
        with self.assertRaises(ValueError):
            verify(p)

    def test_cannot_certify_from_one_consumer(self):
        p=copy.deepcopy(self.example)
        p.update(package_state="CERTIFIED_MULTI_CONSUMER",version="1.0.0",license="INTERNAL_APPROVED")
        p["provenance"]["source_files"]=["lib/src/profile.dart"]
        p["compatibility"].update(dart_sdk="3.5.0",flutter_sdk="3.29.0",tested_pairs=[{
            "dart":"3.5.0","flutter":"3.29.0","test_url":"https://github.com/a/b/actions/runs/1"}])
        p["tests"].update(donor_ci_urls=["https://github.com/a/b/actions/runs/1"],consumer_ci_urls=["https://github.com/a/b/actions/runs/2"])
        p["consumers"]=[{"repo":"riccardopinato/World-Days","source_sha":"a"*40,"approved":True,"test_url":"https://github.com/a/b/actions/runs/2"}]
        with self.assertRaises(ValueError):
            verify(p)

    def test_floating_dependency_rejected(self):
        p=copy.deepcopy(self.example)
        p["dependencies"]={"supabase_flutter":"^2.17.2"}
        with self.assertRaises(ValueError):
            verify(p)

    def test_publication_needs_verified_state_and_artifact(self):
        p=copy.deepcopy(self.example)
        p["release"]["publish_authorized"]=True
        with self.assertRaises(ValueError):
            verify(p)

    def test_bad_donor_and_factory_sha_rejected(self):
        p=copy.deepcopy(self.example)
        p["golden"]["registry_sha"]="f"*40
        with self.assertRaises(ValueError):
            verify(p)
        p=copy.deepcopy(self.example)
        p["provenance"]["donor_sha"]="not-40-hex"
        with self.assertRaises(ValueError):
            verify(p)

if __name__=="__main__":
    unittest.main()
