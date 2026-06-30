import unittest

from e2r.production import cutover_v2


class CutoverV2UrlStringOnlyNotA2Tests(unittest.TestCase):
    def test_url_string_without_fetch_is_not_promoted(self):
        original = cutover_v2._fetch_a2_url

        def fake_fetch(url, *, cache_dir):
            return {"status": "PROVIDER_FAILED", "provider_error": "url_string_only", "provider_request_id": "REQ"}

        try:
            cutover_v2._fetch_a2_url = fake_fetch
            result = cutover_v2.build_a2_replay_promotion_report(
                repo_root=".",
                output_dir="/tmp/e2r_test_a2_url_only",
                fetch_live=True,
                fetch_limit_per_arch=3,
            )
        finally:
            cutover_v2._fetch_a2_url = original
        self.assertEqual(result["report"]["summary"]["A2_REAL_REPLAY_VERIFIED_count"], 0)


if __name__ == "__main__":
    unittest.main()
