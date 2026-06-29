import unittest

from e2r.research_brain.v2_source_quality import reclassify_v1_source_quality
from research_brain_v2_test_helpers import load_json


class ResearchBrainV2SourceQualityTests(unittest.TestCase):
    def test_reclassification_splits_old_a_into_a2_a1_a0(self):
        report = load_json("docs/operational/research_brain_v2_source_quality_reclassification.json")
        counts = report["summary"]["source_quality_v2_counts"]
        self.assertEqual(
            counts["A2_EVIDENCE_OS_REPLAY_VERIFIED"]
            + counts["A1_URL_BACKED_ANCHOR_PENDING"]
            + counts["A0_URL_STRING_ONLY"],
            report["summary"]["v1_A_URL_BACKED_REPLAY_READY_count"],
        )
        self.assertEqual(report["summary"]["A2_replay_sample_pass_count"], 200)

    def test_source_proxy_never_becomes_replay_or_score(self):
        report = load_json("docs/operational/research_brain_v2_source_quality_reclassification.json")
        self.assertEqual(report["summary"]["source_proxy_to_replay_fixture_count"], 0)
        self.assertEqual(report["summary"]["source_proxy_to_score_count"], 0)

    def test_url_string_only_is_not_a2_without_evidence_os_ready_gate(self):
        v1_summary = {"source_quality_class_counts": {"A_URL_BACKED_REPLAY_READY": 5}}
        report = reclassify_v1_source_quality(v1_summary=v1_summary, a2_sample_size=5, evidence_os_ready=False)
        counts = report["summary"]["source_quality_v2_counts"]
        self.assertEqual(counts["A2_EVIDENCE_OS_REPLAY_VERIFIED"], 0)
        self.assertEqual(counts["A1_URL_BACKED_ANCHOR_PENDING"], 5)


if __name__ == "__main__":
    unittest.main()
