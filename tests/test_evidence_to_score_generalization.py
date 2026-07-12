from __future__ import annotations

import unittest

from e2r.research_brain.scoring.generalization_canaries import compile_evidence_to_score_generalization_audit


class EvidenceToScoreGeneralizationTests(unittest.TestCase):
    def test_historical_c06_and_c08_c15_canaries_share_calibrated_bridge(self) -> None:
        audit = compile_evidence_to_score_generalization_audit()
        self.assertEqual(audit["status"], "EVIDENCE_TO_SCORE_GENERALIZATION_PASS")
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertEqual(len(audit["cases"]), 13)
        sold_out = audit["cases"]["c06_hynix_sold_out_capacity_positive"]
        revenue_mix = audit["cases"]["c06_hynix_revenue_mix_positive"]
        qualification = audit["cases"]["c06_samsung_qualification_lag_guard"]
        reopen = audit["cases"]["c06_samsung_reopen_customer_dependency_guard"]
        package = audit["cases"]["c06_package_substrate_profile_guard"]
        self.assertGreater(sold_out["component_score_vector"]["earnings_visibility"], 0)
        self.assertGreater(sold_out["component_score_vector"]["bottleneck_pricing"], 0)
        self.assertGreater(revenue_mix["component_score_vector"]["earnings_visibility"], 0)
        self.assertGreater(revenue_mix["component_score_vector"]["eps_fcf_explosion"], 0)
        self.assertFalse(qualification["hard_break_emitted"])
        self.assertGreater(qualification["counter_effect_fraction"], 0)
        self.assertEqual(
            qualification["component_statuses"]["earnings_visibility"],
            "VERIFIED_COUNTER",
        )
        self.assertEqual(reopen["component_score_vector"]["earnings_visibility"], 0)
        self.assertEqual(reopen["component_score_vector"]["bottleneck_pricing"], 0)
        self.assertGreater(reopen["component_score_vector"]["eps_fcf_explosion"], 0)
        self.assertEqual(
            {key for key, value in package["component_score_vector"].items() if value},
            {"information_confidence"},
        )
        self.assertGreater(audit["cases"]["c08_direct_customer_order_positive"]["verified_supported_score"], 0)
        self.assertGreater(audit["cases"]["c15_issuer_pass_through_positive"]["verified_supported_score"], 0)
        self.assertGreater(audit["cases"]["c08_product_profile_only_guard"]["verified_supported_score"], 0)
        self.assertEqual(
            {
                key
                for key, value in audit["cases"]["c08_product_profile_only_guard"]["component_score_vector"].items()
                if value
            },
            {"information_confidence"},
        )
        self.assertEqual(audit["cases"]["c15_raw_commodity_headline_guard"]["verified_supported_score"], 0)
        self.assertEqual(audit["cases"]["wrong_subject_accounting_guard"]["rejection_reason"], "TARGET_MISMATCH")
        self.assertEqual(
            audit["cases"]["same_issuer_wrong_segment_guard"]["rejection_reason"],
            "REROUTED_TO_OTHER_MECHANISM",
        )
        self.assertEqual(audit["cases"]["old_risk_resolved_guard"]["open_counter_impact_count"], 0)
        support_counter = audit["cases"]["support_counter_same_component"]
        self.assertGreater(support_counter["support_effect_fraction"], 0)
        self.assertGreater(support_counter["counter_effect_fraction"], 0)
        self.assertEqual(
            support_counter["component_statuses"]["bottleneck_pricing"],
            "CONTRADICTED_OPEN",
        )


if __name__ == "__main__":
    unittest.main()
