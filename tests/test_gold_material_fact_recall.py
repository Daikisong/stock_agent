from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.research_quality import BlindResearchQualityBenchmark


class GoldMaterialFactRecallTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_controlled_blind_fixture_replays_with_zero_critical(self) -> None:
        fixture = (
            self.ROOT
            / "tests/fixtures/semantic_scoring_v2/blind_benchmark"
        )
        actual = BlindResearchQualityBenchmark().compare(
            gold_root=fixture / "gold",
            production_root=fixture / "production",
        ).audit
        self.assertEqual(actual["benchmark_mode"], "CONTROLLED_BLIND_LANE_CONTRACT")
        self.assertEqual(actual["critical_count_sum"], 0)
        self.assertGreaterEqual(actual["noncritical_fact_recall"], 0.9)

    def test_operational_audit_is_live_samsung_hynix_not_fixture(self) -> None:
        operational = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_v5_gold_research_recall.json"
            ).read_text(encoding="utf-8")
        )
        fixture = self.ROOT / "tests/fixtures/semantic_scoring_v2/blind_benchmark"
        controlled = BlindResearchQualityBenchmark().compare(
            gold_root=fixture / "gold",
            production_root=fixture / "production",
        ).audit

        self.assertEqual(operational["benchmark_mode"], "PRIVATE_POST_RUN_FULL_THESIS_GOLD")
        self.assertEqual(operational["critical_count_sum"], 0)
        self.assertGreater(operational["gold_fact_count"], 9)
        self.assertEqual(operational["gold_component_memo_count"], 14)
        self.assertEqual(set(operational["per_target"]), {"005930", "000660"})
        self.assertEqual(
            operational["post_run_comparison"]["status"],
            "PENDING_PHASE94_CLEAN_PRODUCTION_RERUN",
        )
        self.assertFalse(
            operational["phase93_scope_truth"]["post_run_recall_attested"]
        )
        self.assertNotEqual(operational, controlled)

    def test_benchmark_writes_target_specific_dossier_leaves(self) -> None:
        fixture = self.ROOT / "tests/fixtures/semantic_scoring_v2/blind_benchmark"
        benchmark = BlindResearchQualityBenchmark()
        result = benchmark.compare(
            gold_root=fixture / "gold",
            production_root=fixture / "production",
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = benchmark.write_dossier_leaves(
                result=result,
                gold_root=fixture / "gold",
                production_root=fixture / "production",
                dossier_roots={
                    "TARGET-A": root / "a",
                    "TARGET-B": root / "b",
                },
            )
            for target_id, key in (("TARGET-A", "a"), ("TARGET-B", "b")):
                self.assertEqual(set(paths[target_id]), {"gold", "production", "comparison"})
                for name in (
                    "gold_material_facts.jsonl",
                    "production_material_facts.jsonl",
                    "material_fact_comparison.jsonl",
                ):
                    rows = [
                        json.loads(line)
                        for line in (root / key / name).read_text().splitlines()
                        if line.strip()
                    ]
                    self.assertTrue(rows)
                    self.assertEqual({row["target_id"] for row in rows}, {target_id})


if __name__ == "__main__":
    unittest.main()
