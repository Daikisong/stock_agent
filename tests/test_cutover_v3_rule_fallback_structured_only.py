import unittest

from e2r.production.cutover_v3 import _claim_extractor_provider_audit_v3
from tests.cutover_v3_test_helpers import fake_v3_base


class CutoverV3RuleFallbackStructuredOnlyTests(unittest.TestCase):
    def test_rule_fallback_score_claims_are_limited_to_structured_official_records(self):
        report = _claim_extractor_provider_audit_v3(
            base_bundles=[fake_v3_base(count=2)],
            claim_extraction={
                "report": {
                    "rows": [],
                    "summary": {
                        "llm_raw_assertion_extractor_used_count": 0,
                        "forced_target_subject_count": 0,
                        "forced_positive_polarity_count": 0,
                        "forced_current_temporal_count": 0,
                        "contract_visible_to_raw_extractor_count": 0,
                        "primitive_gap_direct_mapping_count": 0,
                    },
                }
            },
        )

        self.assertEqual(report["summary"]["production_extraction_mode"], "STRUCTURED_OFFICIAL_ONLY")
        self.assertEqual(report["summary"]["rule_fallback_score_eligible_claim_count"], 2)
        self.assertEqual(report["summary"]["unstructured_text_rule_score_count"], 0)
        self.assertEqual(report["summary"]["status"], "CLAIM_EXTRACTOR_AUDIT_PASS")


if __name__ == "__main__":
    unittest.main()
