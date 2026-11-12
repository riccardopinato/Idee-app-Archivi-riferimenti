"""X10-023 contract QA: synthetic dossiers are never device certification."""
from copy import deepcopy
import unittest

from scripts.factory_10x_notification_evidence import (
    SCENARIOS, EvidenceContractError, classify,
)

SRC = "a" * 40
HASH = "b" * 64


def dossier():
    return {
        "schema_version": 1,
        "record_type": "X10_023_ANDROID_NOTIFICATION_QA_DOSSIER",
        "identity": {
            "repository": "riccardopinato/Agenda-per-Anna",
            "source_sha": SRC,
            "artifact_sha256": HASH,
            "package_id": "com.example.testapp",
            "version_code": 112,
        },
        "device": {
            "platform": "Android",
            "manufacturer": "Example", "model": "ExampleDevice",
            "os_build": "release-build", "sdk_int": 36,
        },
        "scenarios": [
            {
                "id": scenario,
                "result": "PASS",
                "acquisition": "PHYSICAL_DEVICE_OBSERVATION",
                "proofs": [{
                    "kind": "trace", "sha256": HASH,
                    "ref": "local/evidence/trace-" + scenario,
                }],
            } for scenario in SCENARIOS
        ],
    }


def check(value, sha=SRC):
    return classify(value, expected_source_sha=sha)


class AndroidEvidenceContractTest(unittest.TestCase):
    def test_complete_claim_cannot_certify_physical_delivery(self):
        result = check(dossier())
        self.assertTrue(result["claimed_scenarios_pass"])
        self.assertEqual(result["disposition"],
                         "UNTRUSTED_COMPLETE_CLAIM_REQUIRES_INDEPENDENT_VERIFICATION")
        for key in ("external_artifact_bytes_rehashed", "trusted_os_execution_observed",
                    "device_verified", "golden_promoted",
                    "x10_023_eligible_for_verification", "platform_release_verified"):
            self.assertIs(result[key], False)

    def test_missing_scenarios_not_pass(self):
        item = dossier()
        item["scenarios"] = item["scenarios"][:-1]
        out = check(item)
        self.assertFalse(out["claimed_scenarios_pass"])
        self.assertIn("SIGNED_RELEASE_IDENTITY", out["missing_scenarios"])

    def test_blocked_and_failed_preserve_no_pass(self):
        item = dossier()
        item["scenarios"][0]["result"] = "BLOCKED"
        item["scenarios"][1]["result"] = "FAIL"
        out = check(item)
        self.assertEqual(out["disposition"], "CLAIMS_INCOMPLETE_OR_FAILED")
        self.assertIn("PERMISSION_DENIED", out["blocked_or_not_verified_scenarios"])
        self.assertIn("PERMISSION_GRANTED", out["failed_scenarios"])

    def test_sha_mismatch_rejected(self):
        with self.assertRaisesRegex(EvidenceContractError, "UNPINNED_OR_MISMATCHED_SOURCE"):
            check(dossier(), "c" * 40)

    def test_invalid_identity_never_accepted(self):
        for field, value in (
            ("artifact_sha256", "invalid"),
            ("package_id", "NOT_A_PACKAGE"),
            ("version_code", 0),
            ("version_code", True),
            ("source_sha", "badsha"),
        ):
            item = dossier()
            item["identity"][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(EvidenceContractError):
                check(item)

    def test_absent_or_fake_device_metadata_denied(self):
        for field, value in (
            ("sdk_int", "36"),
            ("sdk_int", True),
            ("os_build", ""),
            ("platform", "Web"),
            ("manufacturer", None),
        ):
            item = dossier()
            item["device"][field] = value
            with self.subTest(field=field), self.assertRaisesRegex(
                EvidenceContractError, "INVALID_DEVICE_IDENTITY"
            ):
                check(item)

    def test_pass_without_evidence_rejected(self):
        item = dossier()
        item["scenarios"][2]["proofs"] = []
        with self.assertRaisesRegex(EvidenceContractError, "PASS_WITHOUT_PROOF"):
            check(item)

    def test_duplicate_and_unknown_scenarios_rejected(self):
        item = dossier()
        item["scenarios"].append(deepcopy(item["scenarios"][0]))
        with self.assertRaisesRegex(EvidenceContractError, "INVALID_OR_DUPLICATE_SCENARIO"):
            check(item)
        item = dossier()
        item["scenarios"][0]["id"] = "USER_REPORTED_IT_WORKS"
        with self.assertRaisesRegex(EvidenceContractError, "INVALID_OR_DUPLICATE_SCENARIO"):
            check(item)

    def test_unsafe_proof_identity_and_urls_rejected(self):
        for ref in ("../secret", "https://example.com/fake-proof", "",
                    "http://localhost/private"):
            item = dossier()
            item["scenarios"][0]["proofs"][0]["ref"] = ref
            with self.subTest(ref=ref), self.assertRaisesRegex(
                EvidenceContractError, "UNSAFE_OR_UNBOUND_PROOF_REF"
            ):
                check(item)
        item = dossier()
        item["scenarios"][0]["proofs"][0]["sha256"] = "not_hash"
        with self.assertRaisesRegex(EvidenceContractError, "UNSAFE_OR_UNBOUND_PROOF_REF"):
            check(item)

    def test_cannot_masquerade_a_test_fixture_as_physical_observation(self):
        item = dossier()
        scenario = next(x for x in item["scenarios"]
                        if x["id"] == "SCHEDULED_NOTIFICATION_DELIVERED")
        scenario["acquisition"] = "DART_UNIT_TEST"
        with self.assertRaisesRegex(EvidenceContractError,
                                    "PHYSICAL_SCENARIO_NOT_OBSERVED"):
            check(item)

    def test_evidence_ref_hash_is_not_independently_rehashed(self):
        item = dossier()
        item["scenarios"][0]["proofs"][0]["sha256"] = "f" * 64
        out = check(item)
        self.assertFalse(out["external_artifact_bytes_rehashed"])
        self.assertFalse(out["device_verified"])

    def test_partial_record_is_never_promoted(self):
        item = dossier()
        item["scenarios"] = [{
            "id": "PERMISSION_DENIED", "result": "NOT_VERIFIED",
            "proofs": [],
        }]
        out = check(item)
        self.assertFalse(out["claimed_scenarios_pass"])
        self.assertEqual(out["scenario_count"], 1)
        self.assertEqual(out["total_required_scenarios"], len(SCENARIOS))


if __name__ == "__main__":
    unittest.main()
