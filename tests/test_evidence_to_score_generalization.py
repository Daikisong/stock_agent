from __future__ import annotations

import unittest

from e2r.research_brain.scoring.generalization_canaries import compile_evidence_to_score_generalization_audit


class EvidenceToScoreGeneralizationTests(unittest.TestCase):
    def test_c08_c15_positive_and_guard_canaries_share_calibrated_bridge(self) -> None:
        audit = compile_evidence_to_score_generalization_audit()
        self.assertEqual(audit["status"], "EVIDENCE_TO_SCORE_GENERALIZATION_PASS")
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertGreater(audit["cases"]["c08_direct_customer_order_positive"]["verified_supported_score"], 0)
        self.assertGreater(audit["cases"]["c15_issuer_pass_through_positive"]["verified_supported_score"], 0)
        self.assertEqual(audit["cases"]["c08_product_profile_only_guard"]["verified_supported_score"], 0)
        self.assertEqual(audit["cases"]["c15_raw_commodity_headline_guard"]["verified_supported_score"], 0)
        self.assertEqual(audit["cases"]["wrong_subject_accounting_guard"]["rejection_reason"], "TARGET_MISMATCH")
        self.assertEqual(audit["cases"]["old_risk_resolved_guard"]["open_counter_impact_count"], 0)


if __name__ == "__main__": unittest.main()
