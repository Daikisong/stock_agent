import unittest

from e2r.production.cutover_v3 import _claim_extractor_provider_audit_v3
from tests.cutover_v3_test_helpers import fake_v3_base


class CutoverV3ClaimExtractorProviderAuditTests(unittest.TestCase):
    def test_claim_extractor_audit_passes_with_llm_and_structured_rule_accounting(self):
        report = _claim_extractor_provider_audit_v3(
            base_bundles=[fake_v3_base()],
            claim_extraction={
                "report": {
                    "rows": [{"raw_assertion_count": 1}],
                    "summary": {
                        "llm_raw_assertion_extractor_used_count": 1,
                        "forced_target_subject_count": 0,
                        "forced_positive_polarity_count": 0,
                        "forced_current_temporal_count": 0,
                        "contract_visible_to_raw_extractor_count": 0,
                        "primitive_gap_direct_mapping_count": 0,
                    },
                }
            },
        )
        self.assertEqual(report["summary"]["status"], "CLAIM_EXTRACTOR_AUDIT_PASS")
        self.assertEqual(report["summary"]["unstructured_text_rule_score_count"], 0)


if __name__ == "__main__":
    unittest.main()
