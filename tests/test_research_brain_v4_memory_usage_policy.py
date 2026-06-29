import unittest

from e2r.research_brain.v4_source_quality_promotion import build_research_memory_usage_audit_v4


class ResearchBrainV4MemoryUsagePolicyTests(unittest.TestCase):
    def test_source_proxy_and_price_path_never_enter_score_or_extraction_prompt(self):
        audit = build_research_memory_usage_audit_v4()
        summary = audit["summary"]
        self.assertEqual(summary["source_proxy_memory_to_score_count"], 0)
        self.assertEqual(summary["price_outcome_to_extraction_prompt_count"], 0)
        self.assertEqual(summary["C24_C28_C17_source_proxy_promoted_to_A2_count"], 0)


if __name__ == "__main__":
    unittest.main()
