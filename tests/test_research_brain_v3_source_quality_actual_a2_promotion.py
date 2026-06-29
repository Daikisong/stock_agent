import unittest

from research_brain_v2_test_helpers import load_json


class ResearchBrainV3SourceQualityActualA2PromotionTests(unittest.TestCase):
    def test_a2_promotions_have_url_anchor_claim_and_no_source_proxy(self):
        report = load_json("docs/operational/research_brain_v3_source_quality_promotion_report.json")
        sample = load_json("docs/operational/research_brain_v3_a2_promoted_claims_sample.json")
        self.assertEqual(report["summary"]["source_proxy_to_A2_count"], 0)
        self.assertTrue(report["summary"]["source_proxy_only_rows_remain_non_A2"])
        self.assertGreater(report["summary"]["a2_actual_promoted_count"], 0)
        self.assertTrue(sample["summary"]["all_rows_have_source_url_document_anchor_claim"])


if __name__ == "__main__":
    unittest.main()
