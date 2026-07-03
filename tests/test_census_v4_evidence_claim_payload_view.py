import unittest

from tests.census_v4_test_helpers import census_v4_artifacts, read_jsonl


class CensusV4EvidenceClaimPayloadViewTests(unittest.TestCase):
    def test_evidence_claim_view_matches_accepted_claim_ids(self):
        artifacts = census_v4_artifacts()
        output_root = artifacts["output_root"]
        accepted = read_jsonl(output_root / "accepted_claims.jsonl")
        evidence_claims = read_jsonl(output_root / "evidence_claims.jsonl")
        self.assertGreater(len(evidence_claims), 0)
        self.assertEqual({row["claim_id"] for row in evidence_claims}, {row["claim_id"] for row in accepted})
        self.assertTrue(all(row["payload_source"] == "accepted_claims.jsonl" for row in evidence_claims))
        self.assertTrue(all(row["claim_payload_class"] == "source_backed_accepted_claim" for row in evidence_claims))
        self.assertTrue(all(row["brain_web_claim"] is False for row in evidence_claims))
        full_thesis_claims = [row for row in evidence_claims if row["full_thesis_claim"] is True]
        self.assertEqual(len(full_thesis_claims), 14)
        self.assertTrue(all(row["document_id"] and row["anchor_id"] for row in full_thesis_claims))

    def test_leaf_audit_rejects_claim_payload_mismatch(self):
        artifacts = census_v4_artifacts()
        critical = artifacts["leaf_audit"]["critical_counts"]
        self.assertEqual(critical["accepted_claim_without_evidence_claim_payload_count"], 0)
        self.assertEqual(critical["evidence_claim_payload_without_accepted_claim_count"], 0)
        self.assertEqual(critical["evidence_claim_missing_verifiable_anchor_count"], 0)
        self.assertEqual(artifacts["leaf_audit"]["metrics"]["evidence_claim_payload_count"], len(read_jsonl(artifacts["output_root"] / "evidence_claims.jsonl")))


if __name__ == "__main__":
    unittest.main()
