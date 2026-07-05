import json
import unittest
from pathlib import Path


class ResearchReverseNoProxyToScoreTests(unittest.TestCase):
    def test_source_proxy_rows_are_planning_only(self) -> None:
        inventory = json.loads(
            Path("docs/operational/research_reverse_case_inventory.json").read_text(encoding="utf-8")
        )
        proxy_rows = [row for row in inventory["records"] if row["source_proxy_only"]]
        self.assertGreater(len(proxy_rows), 0)
        for row in proxy_rows[:1000]:
            self.assertEqual(row["source_quality"], "SOURCE_PROXY_ONLY")
            self.assertFalse(row["runtime_score_eligible"])
            self.assertFalse(row["production_scoring_changed"])
            self.assertEqual(row["do_not_promote_reason"], "source_proxy_only_planning_only")


if __name__ == "__main__":
    unittest.main()
