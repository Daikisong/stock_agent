import unittest

from e2r.production.cutover_v3 import _claim_extractor_provider_audit_v3
from tests.cutover_v3_test_helpers import fake_v3_base


class CutoverV3UnstructuredTextRequiresLLMOrPendingTests(unittest.TestCase):
    def test_unstructured_text_rule_claim_blocks_audit_without_llm_success(self):
        base = dict(fake_v3_base(count=1))
        artifacts = dict(base["output_artifacts"])
        artifacts["evidence_documents"] = [{"document_id": "DOC-NEWS", "source_type": "TEXT_SPAN"}]
        artifacts["evidence_claim_ledger"] = [{"claim_id": "CLM-NEWS", "document_id": "DOC-NEWS", "accepted": True}]
        base["output_artifacts"] = artifacts

        report = _claim_extractor_provider_audit_v3(
            base_bundles=[base],
            claim_extraction={
                "report": {
                    "rows": [{"raw_assertion_count": 0}],
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

        self.assertEqual(report["summary"]["unstructured_text_rule_score_count"], 1)
        self.assertEqual(report["summary"]["status"], "CLAIM_EXTRACTOR_AUDIT_NOT_READY")


if __name__ == "__main__":
    unittest.main()
