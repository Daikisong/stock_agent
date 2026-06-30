import unittest

from e2r.production.cutover_v2 import build_a2_replay_promotion_report


class CutoverV2SourceProxyNeverA2Tests(unittest.TestCase):
    def test_fetch_disabled_promotes_no_source_proxy_rows(self):
        result = build_a2_replay_promotion_report(
            repo_root=".",
            output_dir="/tmp/e2r_test_a2_disabled",
            fetch_live=False,
            fetch_limit_per_arch=5,
        )
        self.assertEqual(result["report"]["summary"]["A2_REAL_REPLAY_VERIFIED_count"], 0)
        self.assertTrue(result["failed_queue"])


if __name__ == "__main__":
    unittest.main()
