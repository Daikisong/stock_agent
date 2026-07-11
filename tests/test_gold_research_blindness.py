from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.research_quality import BlindResearchQualityBenchmark


class GoldResearchBlindnessTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]
    FIXTURE = (
        ROOT / "tests/fixtures/semantic_scoring_v2/blind_benchmark"
    )

    def test_isolated_lanes_pass_without_gold_input_leakage(self) -> None:
        result = BlindResearchQualityBenchmark().compare(
            gold_root=self.FIXTURE / "gold",
            production_root=self.FIXTURE / "production",
        )
        self.assertEqual(result.status, "BLIND_RESEARCH_QUALITY_PASS")
        self.assertEqual(result.audit["critical_count_sum"], 0)
        self.assertEqual(result.audit["noncritical_fact_recall"], 1.0)
        self.assertEqual(
            result.audit["critical_counts"][
                "gold_source_injected_into_production_count"
            ],
            0,
        )
        self.assertTrue(
            all(row.semantic_match for row in result.comparisons)
        )

    def test_same_source_may_be_rediscovered_but_cannot_be_a_seed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp) / "benchmark"
            shutil.copytree(self.FIXTURE, fixture)
            source = json.loads(
                (fixture / "gold/gold_source_map.jsonl")
                .read_text()
                .splitlines()[0]
            )
            with (fixture / "production/production_input_manifest.jsonl").open(
                "a", encoding="utf-8"
            ) as handle:
                handle.write(
                    json.dumps(
                        {
                            "input_id": "LEAKED-SEED",
                            "input_type": "SEED_URL",
                            "value": source["source_url"],
                            "origin": "CANONICAL_CONFIG",
                        }
                    )
                    + "\n"
                )
            result = BlindResearchQualityBenchmark().compare(
                gold_root=fixture / "gold",
                production_root=fixture / "production",
            )
        self.assertEqual(result.status, "BLIND_RESEARCH_QUALITY_FAIL")
        self.assertEqual(
            result.audit["critical_counts"][
                "gold_source_injected_into_production_count"
            ],
            1,
        )

    def test_critical_gold_miss_cannot_pass_on_raw_source_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp) / "benchmark"
            shutil.copytree(self.FIXTURE, fixture)
            path = fixture / "production/production_material_facts.jsonl"
            rows = [
                json.loads(line) for line in path.read_text().splitlines()
            ]
            rows = [row for row in rows if row["fact_id"] != "P-203"]
            path.write_text(
                "".join(json.dumps(row) + "\n" for row in rows),
                encoding="utf-8",
            )
            result = BlindResearchQualityBenchmark().compare(
                gold_root=fixture / "gold",
                production_root=fixture / "production",
            )
        self.assertEqual(result.status, "BLIND_RESEARCH_QUALITY_FAIL")
        self.assertEqual(
            result.audit["critical_counts"][
                "material_counter_fact_miss_count"
            ],
            1,
        )

    def test_gold_and_production_directories_cannot_nest(self) -> None:
        with self.assertRaisesRegex(ValueError, "disjoint"):
            BlindResearchQualityBenchmark().compare(
                gold_root=self.FIXTURE,
                production_root=self.FIXTURE / "production",
            )


if __name__ == "__main__":
    unittest.main()
