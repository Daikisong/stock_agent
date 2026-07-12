from __future__ import annotations

import json
from pathlib import Path
import shutil
import tempfile
import unittest

from e2r.research_brain.researcher_mode import (
    PHASE93_POST_RUN_FAIL,
    PHASE93_POST_RUN_PASS,
    PHASE93_POST_RUN_PENDING,
    PHASE93_READY,
    PHASE93_RECALL_THRESHOLDS,
    PHASE93_SOURCE_FAMILIES,
    compare_phase93_gold_post_run,
    compile_phase93_gold_research_recall_audit,
    gold_authority_leakage_paths,
    load_phase93_gold_corpus,
)


class E2RV5FullThesisGoldBenchmarkTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]
    GOLD = (
        ROOT
        / "data/benchmark_labels/e2r_v5_full_thesis_gold_2026-07-12"
    )

    @classmethod
    def setUpClass(cls) -> None:
        cls.corpus = load_phase93_gold_corpus(cls.ROOT)
        cls.audit = compile_phase93_gold_research_recall_audit(cls.ROOT)

    def test_committed_phase93_audit_is_reproducible_and_honest(self) -> None:
        committed = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_v5_gold_research_recall.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(self.audit, committed)
        self.assertEqual(self.audit["status"], PHASE93_READY)
        self.assertEqual(self.audit["critical_count_sum"], 0)
        self.assertEqual(
            self.audit["post_run_comparison"]["status"],
            PHASE93_POST_RUN_PENDING,
        )
        self.assertFalse(
            self.audit["phase93_scope_truth"]["post_run_recall_attested"]
        )
        self.assertFalse(
            self.audit["phase93_scope_truth"]["production_readiness_claimed"]
        )

    def test_audit_rebuilds_without_ignored_production_output(self) -> None:
        committed = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_v5_gold_research_recall.json"
            ).read_text(encoding="utf-8")
        )
        with tempfile.TemporaryDirectory() as tmp:
            rebuilt = compile_phase93_gold_research_recall_audit(
                self.ROOT,
                production_root=Path(tmp) / "absent-output",
            )
        self.assertEqual(rebuilt, committed)
        self.assertEqual(
            rebuilt["lane_isolation"]["leakage_audit"]["proof_source"],
            "TRACKED_PRE_GOLD_FINGERPRINT_SNAPSHOT",
        )

    def test_nine_fact_baseline_is_replaced_by_full_thesis_corpus(self) -> None:
        self.assertEqual(len(self.corpus["queries"]), 32)
        self.assertEqual(len(self.corpus["sources"]), 21)
        self.assertEqual(len(self.corpus["facts"]), 28)
        self.assertEqual(len(self.corpus["counterfacts"]), 14)
        self.assertEqual(len(self.corpus["memos"]), 14)
        self.assertGreater(len(self.corpus["facts"]), 9)
        self.assertFalse(self.audit["legacy_nine_fact_audit_is_authoritative"])

    def test_every_target_component_has_balanced_gold_queries(self) -> None:
        manifest = self.corpus["manifest"]
        topics = (*manifest["component_ids"], manifest["red_team_topic_id"])
        for target_id in manifest["target_ids"]:
            for topic_id in topics:
                intents = {
                    row["intent"]
                    for row in self.corpus["queries"]
                    if row["target_id"] == target_id
                    and row["topic_id"] == topic_id
                }
                self.assertEqual(
                    intents,
                    {
                        "SUPPORT_DISCOVERY",
                        "COUNTER_OR_SUPERSESSION_DISCOVERY",
                    },
                )
        self.assertTrue(
            all(
                row["generator_kind"] == "INDEPENDENT_GOLD_RESEARCHER"
                and row["production_execution_allowed"] is False
                for row in self.corpus["queries"]
            )
        )

    def test_all_ten_public_source_families_exist_for_each_target(self) -> None:
        required = set(PHASE93_SOURCE_FAMILIES)
        for target_id in self.corpus["manifest"]["target_ids"]:
            observed = {
                row["source_family"]
                for row in self.corpus["sources"]
                if row["target_id"] == target_id
            }
            self.assertEqual(observed, required)
        self.assertTrue(
            all(
                row["evidence_eligible"] is False
                for row in self.corpus["sources"]
                if row["source_family"] == "NAVER_WEB_DISCOVERY"
            )
        )

    def test_every_component_has_source_backed_support_and_counter(self) -> None:
        source_by_id = {
            row["source_id"]: row for row in self.corpus["sources"]
        }
        for target_id in self.corpus["manifest"]["target_ids"]:
            for component_id in self.corpus["manifest"]["component_ids"]:
                facts = [
                    row
                    for row in self.corpus["facts"]
                    if row["target_id"] == target_id
                    and row["component_id"] == component_id
                ]
                self.assertTrue(any(row["fact_role"] == "SUPPORT" for row in facts))
                self.assertTrue(any(row["fact_role"] == "COUNTER" for row in facts))
                for fact in facts:
                    source = source_by_id[fact["source_id"]]
                    self.assertTrue(source["full_source_verified"])
                    self.assertTrue(source["evidence_eligible"])
                    self.assertEqual(source["target_id"], fact["target_id"])
                    self.assertLessEqual(source["published_date"], "2026-07-12")

    def test_component_memos_are_two_sided_and_score_free(self) -> None:
        self.assertEqual(gold_authority_leakage_paths(self.corpus), ())
        for memo in self.corpus["memos"]:
            self.assertEqual(memo["research_status"], "GOLD_RESEARCH_COMPLETE")
            self.assertTrue(memo["support_fact_ids"])
            self.assertTrue(memo["counterfact_ids"])
            self.assertTrue(memo["why_higher"])
            self.assertTrue(memo["why_lower"])
            self.assertTrue(memo["red_team_question"])
            self.assertTrue(memo["red_team_resolution"])

    def test_production_baseline_has_no_gold_input_injection(self) -> None:
        leakage = self.audit["lane_isolation"]["leakage_audit"]
        self.assertEqual(leakage["gold_source_injected_into_production_count"], 0)
        self.assertEqual(leakage["gold_query_leaked_into_production_count"], 0)
        self.assertEqual(leakage["gold_fact_leaked_into_production_prompt_count"], 0)
        self.assertEqual(leakage["production_lane_gold_visibility_count"], 0)

    def test_generic_validator_contains_no_canary_target_branch(self) -> None:
        source = (
            self.ROOT
            / "src/e2r/research_brain/researcher_mode/full_thesis_gold_benchmark.py"
        ).read_text(encoding="utf-8")
        for literal in ("005930", "000660", "삼성전자", "SK하이닉스"):
            self.assertNotIn(literal, source)

    def test_controlled_independent_post_run_meets_all_recall_gates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            production = Path(tmp) / "production"
            self._write_controlled_production(production)
            result = compare_phase93_gold_post_run(
                self.ROOT,
                production_root=production,
            )
        self.assertEqual(result.status, PHASE93_POST_RUN_PASS)
        self.assertEqual(result.audit["critical_count_sum"], 0)
        for metric, threshold in PHASE93_RECALL_THRESHOLDS.items():
            self.assertGreaterEqual(
                result.audit["metrics"][metric.removesuffix("_min")],
                threshold,
            )

    def test_critical_fact_miss_fails_post_run_gate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            production = Path(tmp) / "production"
            self._write_controlled_production(production, omit_fact_id="G-005930-EPS-S")
            result = compare_phase93_gold_post_run(
                self.ROOT,
                production_root=production,
            )
        self.assertEqual(result.status, PHASE93_POST_RUN_FAIL)
        self.assertLess(result.audit["metrics"]["critical_material_fact_recall"], 1.0)

    def test_counterfact_miss_fails_counter_and_topic_gates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            production = Path(tmp) / "production"
            self._write_controlled_production(production, omit_fact_id="G-000660-CAP-C")
            result = compare_phase93_gold_post_run(
                self.ROOT,
                production_root=production,
            )
        self.assertEqual(result.status, PHASE93_POST_RUN_FAIL)
        self.assertLess(result.audit["metrics"]["counter_supersession_recall"], 1.0)
        self.assertLess(result.audit["metrics"]["component_research_topic_coverage"], 1.0)

    def test_gold_seed_url_injection_fails_post_run_gate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            production = Path(tmp) / "production"
            self._write_controlled_production(production)
            source_url = self.corpus["sources"][0]["source_url"]
            self._write_jsonl(
                production / "production_input_manifest.jsonl",
                [
                    {
                        "input_id": "P-SEED-LEAK",
                        "input_type": "SEED_URL",
                        "origin": "CANONICAL_CONFIG",
                        "value": source_url,
                    }
                ],
            )
            result = compare_phase93_gold_post_run(
                self.ROOT,
                production_root=production,
            )
        self.assertEqual(result.status, PHASE93_POST_RUN_FAIL)
        self.assertEqual(
            result.audit["critical_counts"]["gold_leakage_count"],
            1,
        )

    def test_gold_query_injection_fails_post_run_gate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            production = Path(tmp) / "production"
            self._write_controlled_production(production)
            self._write_jsonl(
                production / "production_input_manifest.jsonl",
                [
                    {
                        "input_id": "P-QUERY-LEAK",
                        "input_type": "QUERY",
                        "origin": "LLM_PLANNER",
                        "value": self.corpus["queries"][0]["literal_query"],
                    }
                ],
            )
            result = compare_phase93_gold_post_run(
                self.ROOT,
                production_root=production,
            )
        self.assertEqual(result.status, PHASE93_POST_RUN_FAIL)
        self.assertEqual(
            result.audit["blind_leakage_audit"]["gold_query_leaked_into_production_count"],
            1,
        )

    def test_known_bad_missing_component_is_rejected(self) -> None:
        with self._mutated_gold() as gold:
            path = gold / "gold_component_memos.jsonl"
            rows = self._read_jsonl(path)[:-1]
            self._write_jsonl(path, rows)
            with self.assertRaisesRegex(ValueError, "cover every target/component"):
                load_phase93_gold_corpus(self.ROOT, gold_root=gold)

    def test_known_bad_future_source_is_rejected(self) -> None:
        with self._mutated_gold() as gold:
            path = gold / "gold_source_map.jsonl"
            rows = self._read_jsonl(path)
            rows[0]["published_date"] = "2026-07-13"
            self._write_jsonl(path, rows)
            with self.assertRaisesRegex(ValueError, "future Gold data"):
                load_phase93_gold_corpus(self.ROOT, gold_root=gold)

    def test_known_bad_discovery_snippet_fact_is_rejected(self) -> None:
        with self._mutated_gold() as gold:
            source_id = next(
                row["source_id"]
                for row in self._read_jsonl(gold / "gold_source_map.jsonl")
                if row["source_family"] == "NAVER_WEB_DISCOVERY"
                and row["target_id"] == "005930"
            )
            path = gold / "gold_material_facts.jsonl"
            rows = self._read_jsonl(path)
            rows[0]["source_id"] = source_id
            rows[0]["source_tier"] = "DISCOVERY_ONLY"
            self._write_jsonl(path, rows)
            with self.assertRaisesRegex(ValueError, "discovery-only"):
                load_phase93_gold_corpus(self.ROOT, gold_root=gold)

    def test_known_bad_missing_source_family_is_rejected(self) -> None:
        with self._mutated_gold() as gold:
            path = gold / "gold_source_map.jsonl"
            rows = self._read_jsonl(path)
            source = next(
                row
                for row in rows
                if row["target_id"] == "005930"
                and row["source_family"] == "PUBLIC_REPORT"
            )
            source["source_family"] = "TRUSTED_MEDIA"
            self._write_jsonl(path, rows)
            with self.assertRaisesRegex(ValueError, "source family coverage mismatch"):
                load_phase93_gold_corpus(self.ROOT, gold_root=gold)

    def test_known_bad_orphan_fact_source_is_rejected(self) -> None:
        with self._mutated_gold() as gold:
            path = gold / "gold_material_facts.jsonl"
            rows = self._read_jsonl(path)
            rows[0]["source_id"] = "GS-ORPHAN"
            self._write_jsonl(path, rows)
            with self.assertRaisesRegex(ValueError, "source lineage is missing"):
                load_phase93_gold_corpus(self.ROOT, gold_root=gold)

    def test_known_bad_gold_score_or_stage_is_rejected(self) -> None:
        with self._mutated_gold() as gold:
            path = gold / "gold_component_memos.jsonl"
            rows = self._read_jsonl(path)
            rows[0]["score"] = 99
            self._write_jsonl(path, rows)
            with self.assertRaisesRegex(ValueError, "forbidden score/Stage"):
                load_phase93_gold_corpus(self.ROOT, gold_root=gold)

    def test_known_bad_nine_fact_corpus_is_rejected(self) -> None:
        with self._mutated_gold() as gold:
            path = gold / "gold_material_facts.jsonl"
            self._write_jsonl(path, self._read_jsonl(path)[:9])
            with self.assertRaisesRegex(ValueError, "nine-fact"):
                load_phase93_gold_corpus(self.ROOT, gold_root=gold)

    def _write_controlled_production(
        self,
        root: Path,
        *,
        omit_fact_id: str | None = None,
    ) -> None:
        facts = []
        for index, gold in enumerate(self.corpus["facts"]):
            if gold["fact_id"] == omit_fact_id:
                continue
            row = dict(gold)
            row["fact_id"] = f"P-INDEPENDENT-{index:03d}"
            row["discovery_origin"] = "CANONICAL_SOURCE_TASK"
            facts.append(row)
        self._write_jsonl(root / "production_material_facts.jsonl", facts)
        self._write_jsonl(
            root / "production_input_manifest.jsonl",
            [
                {
                    "input_id": "P-CONTROLLED-CONFIG",
                    "input_type": "CONFIG",
                    "origin": "CANONICAL_CONFIG",
                    "value": "canonical question and source contracts only",
                }
            ],
        )
        self._write_json(
            root / "production_lane_manifest.json",
            {
                "schema_version": "controlled_full_thesis_production_v1",
                "lane_role": "PRODUCTION",
                "gold_visibility": False,
                "as_of_date": "2026-07-12",
            },
        )
        self._write_jsonl(
            root / "production_component_memos.jsonl",
            [
                {
                    "target_id": target_id,
                    "component_id": component_id,
                    "research_status": "RESEARCH_COMPLETE",
                }
                for target_id in self.corpus["manifest"]["target_ids"]
                for component_id in self.corpus["manifest"]["component_ids"]
            ],
        )

    def _mutated_gold(self):
        class _GoldCopy:
            def __init__(inner_self, outer: "E2RV5FullThesisGoldBenchmarkTests") -> None:
                inner_self.outer = outer
                inner_self.tmp = tempfile.TemporaryDirectory()

            def __enter__(inner_self) -> Path:
                target = Path(inner_self.tmp.name) / "gold"
                shutil.copytree(inner_self.outer.GOLD, target)
                return target

            def __exit__(inner_self, *_args) -> None:
                inner_self.tmp.cleanup()

        return _GoldCopy(self)

    @staticmethod
    def _read_jsonl(path: Path) -> list[dict]:
        return [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    @staticmethod
    def _write_jsonl(path: Path, rows: list[dict]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "".join(
                json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
                for row in rows
            ),
            encoding="utf-8",
        )

    @staticmethod
    def _write_json(path: Path, payload: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    unittest.main()
