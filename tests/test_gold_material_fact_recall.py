from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.research_quality import BlindResearchQualityBenchmark


class GoldMaterialFactRecallTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_operational_audit_replays_from_blind_fixture(self) -> None:
        fixture = (
            self.ROOT
            / "tests/fixtures/semantic_scoring_v2/blind_benchmark"
        )
        actual = BlindResearchQualityBenchmark().compare(
            gold_root=fixture / "gold",
            production_root=fixture / "production",
        ).audit
        expected = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_research_quality_gold_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(actual, expected)
        self.assertEqual(actual["critical_count_sum"], 0)
        self.assertGreaterEqual(actual["noncritical_fact_recall"], 0.9)


if __name__ == "__main__":
    unittest.main()
