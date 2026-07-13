from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.research_brain.researcher_mode import (
    ALL_ARCHETYPE_GENERALIZATION_FAIL,
    ALL_ARCHETYPE_GENERALIZATION_PASS,
    CANONICAL_COMPONENT_ORDER,
    MANDATORY_GENERALIZATION_CANARIES,
    compile_all_archetype_generalization,
)


class E2RV5AllArchetypeGeneralizationTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    @classmethod
    def setUpClass(cls) -> None:
        cls.output_path = (
            cls.ROOT
            / "docs/operational/e2r_v5_all_archetype_generalization.json"
        )
        cls.anchor_path = (
            cls.ROOT / "docs/operational/e2r_v5_component_anchor_atlas.json"
        )
        cls.blind_path = (
            cls.ROOT / "docs/operational/e2r_v5_historical_blind_replay.json"
        )
        cls.committed = json.loads(cls.output_path.read_text(encoding="utf-8"))
        cls.compiled = compile_all_archetype_generalization(repo_root=cls.ROOT)

    def test_committed_artifact_is_reproducible_and_passes(self) -> None:
        self.assertEqual(self.committed, self.compiled)
        self.assertEqual(
            self.committed["status"], ALL_ARCHETYPE_GENERALIZATION_PASS
        )
        self.assertEqual(self.committed["critical_count_sum"], 0)

    def test_complete_registry_enters_the_same_seven_component_path(self) -> None:
        rows = self.committed["archetypes"]
        self.assertEqual(len(rows), len(CANONICAL_ARCHETYPE_IDS))
        self.assertEqual(
            [row["archetype_id"] for row in rows],
            list(CANONICAL_ARCHETYPE_IDS),
        )
        for row in rows:
            strategies = row["component_research_strategies"]
            self.assertEqual(len(strategies), len(CANONICAL_COMPONENT_ORDER))
            self.assertEqual(
                [strategy["component_id"] for strategy in strategies],
                list(CANONICAL_COMPONENT_ORDER),
            )
            self.assertTrue(
                all(
                    strategy["status"] == "COMPONENT_GENERALIZATION_PASS"
                    for strategy in strategies
                )
            )

    def test_source_graph_is_broad_but_literal_queries_remain_llm_owned(self) -> None:
        for row in self.committed["archetypes"]:
            graph = row["source_graph"]
            self.assertEqual(graph["objective_count"], 7)
            self.assertEqual(graph["literal_query_count"], 0)
            self.assertTrue(graph["llm_query_generation_required"])
            for strategy in row["component_research_strategies"]:
                self.assertGreater(len(strategy["preferred_source_families"]), 0)
                self.assertIsNone(strategy["literal_query"])
                self.assertEqual(strategy["query_generation_authority"], "LLM")
                self.assertFalse(strategy["score_authority"])
                self.assertFalse(strategy["stage_authority"])

    def test_every_archetype_has_positive_counter_and_safe_leave_one_out(self) -> None:
        coverage_counts = {"SOURCE_BACKED_HOLDOUT": 0, "EXACT_SOURCE_GAP": 0}
        for row in self.committed["archetypes"]:
            self.assertFalse(row["positive_example"]["explicit_gap"])
            self.assertFalse(row["counter_example"]["explicit_gap"])
            replay = row["leave_one_out_replay"]
            coverage_counts[replay["coverage_status"]] += 1
            self.assertEqual(replay["status"], "LEAVE_ONE_OUT_REPLAY_PASS")
            self.assertEqual(replay["target_reference_count_after_filter"], 0)
            self.assertTrue(
                all(
                    component["memory_ready"]
                    for component in replay["retained_component_memory"]
                )
            )
            self.assertFalse(replay["current_score_replay_authority"])
            self.assertFalse(replay["current_stage_replay_authority"])
        self.assertEqual(coverage_counts["SOURCE_BACKED_HOLDOUT"], 34)
        self.assertEqual(coverage_counts["EXACT_SOURCE_GAP"], 2)

    def test_mandatory_canaries_all_pass_without_special_runtime_branch(self) -> None:
        rows = self.committed["mandatory_canaries"]
        self.assertEqual(
            [row["archetype_id"] for row in rows],
            list(MANDATORY_GENERALIZATION_CANARIES),
        )
        self.assertTrue(
            all(row["status"] == "ALL_ARCHETYPE_GENERALIZATION_PASS" for row in rows)
        )
        scan = self.committed["production_conditioned_branch_scan"]
        self.assertEqual(scan["finding_count"], 0)
        self.assertEqual(scan["findings"], [])

    def test_source_proxy_is_never_an_exact_current_score_anchor(self) -> None:
        policy = self.committed["source_proxy_policy"]
        self.assertEqual(
            policy["allowed_uses"], ["ORDINAL_GUARD", "QUERY_STRATEGY_CONTEXT"]
        )
        self.assertFalse(policy["exact_current_score_anchor_allowed"])
        self.assertEqual(
            self.committed["critical_counts"]
            ["source_proxy_exact_current_score_anchor_count"],
            0,
        )

    def test_tampered_source_proxy_exact_anchor_fails_closed(self) -> None:
        anchor_payload = json.loads(self.anchor_path.read_text(encoding="utf-8"))
        proxy = next(
            row
            for row in anchor_payload["component_anchors"]
            if row["source_proxy_guard_case_ids"]
        )
        proxy["usable_as_exact_anchor"] = True
        tampered = compile_all_archetype_generalization(
            repo_root=self.ROOT,
            anchor_atlas_payload=anchor_payload,
        )
        self.assertEqual(tampered["status"], ALL_ARCHETYPE_GENERALIZATION_FAIL)
        self.assertGreater(
            tampered["critical_counts"]
            ["source_proxy_exact_current_score_anchor_count"],
            0,
        )

    def test_missing_component_coverage_fails_closed(self) -> None:
        anchor_payload = json.loads(self.anchor_path.read_text(encoding="utf-8"))
        anchor_payload["component_coverage"] = anchor_payload[
            "component_coverage"
        ][1:]
        tampered = compile_all_archetype_generalization(
            repo_root=self.ROOT,
            anchor_atlas_payload=anchor_payload,
        )
        self.assertEqual(tampered["status"], ALL_ARCHETYPE_GENERALIZATION_FAIL)
        self.assertGreater(
            tampered["critical_counts"]["archetype_component_roster_mismatch_count"],
            0,
        )

    def test_artifact_never_claims_current_score_or_stage_authority(self) -> None:
        for row in self.committed["archetypes"]:
            self.assertFalse(row["current_score_authority"])
            self.assertFalse(row["current_stage_authority"])
            self.assertFalse(row["source_graph"]["score_authority"])


if __name__ == "__main__":
    unittest.main()
