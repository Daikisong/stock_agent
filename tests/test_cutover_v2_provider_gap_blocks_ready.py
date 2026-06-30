import unittest

from e2r.production.cutover_v2 import _completion_labels


class CutoverV2ProviderGapBlocksReadyTests(unittest.TestCase):
    def test_provider_gap_blocks_cutover_ready_label(self):
        labels = _completion_labels(
            source_report={"summary": {"status": "LIVE_CONNECTOR_PASS"}},
            provider_matrix={"summary": {"provider_blocker_count": 1}},
            a2={"report": {"summary": {"status": "A2_REPLAY_PASS", "A2_REAL_REPLAY_VERIFIED_count": 30}}},
            claim_extraction={"report": {"summary": {"status": "LLM_EXTRACTION_PASS"}}},
            stage_distribution={"summary": {"status": "MEANINGFUL_STAGE_SPLIT_PASS"}},
            trigger_policy={"summary": {"status": "TRIGGER_POLICY_PASS"}},
            multiday={"summary": {"status": "MULTIDAY_SHADOW_PASS"}},
            static={"summary": {"critical_count_sum": 0}},
        )
        self.assertNotIn("CUTOVER_READY", labels)


if __name__ == "__main__":
    unittest.main()
