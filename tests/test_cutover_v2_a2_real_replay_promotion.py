import unittest

from e2r.production import cutover_v2


class CutoverV2A2ReplayPromotionTests(unittest.TestCase):
    def test_a2_promotion_requires_anchor_claim_and_source_date(self):
        original = cutover_v2._fetch_a2_url

        def fake_fetch(url, *, cache_dir):
            return {
                "status": "FETCHED",
                "mode": "fresh_provider_cache",
                "provider_request_id": "REQ",
                "content_hash": cutover_v2._stable_id("HASH", url),
                "published_at": "2024-01-01",
                "anchor_type": "TEXT_SPAN",
                "anchor_locator": f"url:{url}",
            }

        try:
            cutover_v2._fetch_a2_url = fake_fetch
            result = cutover_v2.build_a2_replay_promotion_report(
                repo_root=".",
                output_dir="/tmp/e2r_test_a2",
                fetch_live=True,
                fetch_limit_per_arch=80,
            )
        finally:
            cutover_v2._fetch_a2_url = original
        summary = result["report"]["summary"]
        self.assertEqual(summary["status"], "A2_REPLAY_PASS")
        self.assertGreaterEqual(summary["A2_REAL_REPLAY_VERIFIED_count"], 30)
        self.assertEqual(summary["source_proxy_to_A2_count"], 0)
        self.assertEqual(summary["evidence_url_pending_to_A2_count"], 0)
        self.assertEqual(summary["A2_without_anchor_count"], 0)
        self.assertEqual(summary["A2_without_source_date_count"], 0)
        self.assertEqual(summary["A2_without_accepted_claim_id_count"], 0)


if __name__ == "__main__":
    unittest.main()
