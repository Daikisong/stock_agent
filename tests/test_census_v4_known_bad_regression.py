import unittest

from e2r.census.known_bad_regression import run_known_bad_regression
from e2r.production.claim_extraction.contract_blind_extractor import (
    ContractBlindRawAssertionExtractor,
    ExtractionInput,
)
from tests.census_v4_test_helpers import census_v4_artifacts


class CensusV4KnownBadRegressionTests(unittest.TestCase):
    def test_wrong_subject_normal_audit_opinion_is_not_assigned_to_target(self):
        extractor = ContractBlindRawAssertionExtractor()
        records = extractor.extract(
            ExtractionInput(
                target_entity_id="CORP_SAMSUNG_ELECTRONICS",
                target_aliases=("삼성전자",),
                as_of_date="2026-07-01",
                document_id="DOC-WORLDEX-AUDIT",
                anchor_id="ANC-WORLDEX-AUDIT",
                source_text="월덱스는 삼성전자와 거래 관계가 있으며 감사의견은 적정이다.",
            )
        )
        audit_records = [record for record in records if record.predicate == "audit_or_accounting_claim"]
        self.assertEqual(len(audit_records), 1)
        self.assertEqual(audit_records[0].subject, "월덱스")
        self.assertNotEqual(audit_records[0].subject, "삼성전자")

    def test_old_risk_resolved_case_is_required_known_bad(self):
        report = run_known_bad_regression(
            output_root=census_v4_artifacts()["output_root"],
            target_gate="anti_fake",
        )
        by_id = {case["case_id"]: case for case in report["cases"]}

        self.assertIn("old_risk_resolved_not_current_hard_break", by_id)
        case = by_id["old_risk_resolved_not_current_hard_break"]
        self.assertEqual(case["status"], "PASS")
        self.assertFalse(case["observed"]["score_eligible"])
        self.assertIn("temporal_not_allowed:RESOLVED", case["observed"]["eligibility_reasons"])
        self.assertEqual(case["observed"]["primitive_status"], "RESOLVED")
        self.assertEqual(case["observed"]["support_claim_ids"], [])
        self.assertEqual(case["observed"]["transition_overlay"], "NONE")


if __name__ == "__main__":
    unittest.main()
