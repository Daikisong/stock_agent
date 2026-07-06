import json
import unittest
from pathlib import Path

from e2r.census.all_archetype_runtime_execution_manifest import (
    GOAL4_NEXT_RUNTIME_BUDGET_SECONDS,
    GOAL4_NEXT_RUNTIME_PLANNER_BATCH_SIZE,
    build_all_archetype_runtime_execution_manifest,
)
from e2r.census.census_runner_v4 import CensusV4RunConfig, _planner_run_event_is_full_thesis_seed


class AllArchetypeRuntimeExecutionManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.docs = Path("docs/operational")
        cls.plan = json.loads(
            (cls.docs / "all_archetype_next_runtime_attempt_plan_2026-07-05.json").read_text(encoding="utf-8")
        )
        cls.manifest = build_all_archetype_runtime_execution_manifest(
            next_attempt_plan=cls.plan,
            seed_event_path=cls.docs / "all_archetype_next_runtime_seed_events_2026-07-05.jsonl",
            source_task_path=cls.docs / "all_archetype_next_runtime_source_tasks_2026-07-05.jsonl",
            repo_root=Path("."),
        )

    def test_manifest_points_census_v4_at_next_runtime_seed_events(self) -> None:
        config = self.manifest["census_v4_config_kwargs"]
        self.assertEqual(self.manifest["schema_version"], "e2r_all_archetype_runtime_execution_manifest_v1")
        self.assertEqual(self.manifest["seed_event_count"], 111)
        self.assertEqual(self.manifest["source_task_shell_count"], 111)
        self.assertEqual(
            config["brain_candidate_event_seed_path"],
            "docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl",
        )
        self.assertEqual(config["brain_web_mode"], "enabled")
        self.assertEqual(config["run_mode"], "BRAIN_AND_WEB_ACQUISITION_ENABLED")
        self.assertEqual(config["brain_source_acquisition"], "live_full_bounded")
        self.assertEqual(config["target_gate"], "full_thesis")
        self.assertEqual(config["brain_stage_promotion_mode"], "strict")
        self.assertEqual(config["brain_planner_batch_size"], GOAL4_NEXT_RUNTIME_PLANNER_BATCH_SIZE)
        self.assertEqual(config["brain_planner_batch_size"], 1)
        self.assertEqual(config["brain_runtime_budget_seconds"], GOAL4_NEXT_RUNTIME_BUDGET_SECONDS)
        self.assertEqual(config["brain_runtime_budget_seconds"], 14400.0)

    def test_manifest_config_kwargs_can_construct_census_v4_config(self) -> None:
        config = CensusV4RunConfig(**self.manifest["census_v4_config_kwargs"])
        self.assertEqual(config.brain_candidate_event_seed_path, self.manifest["seed_event_path"])
        self.assertEqual(config.brain_web_mode, "enabled")
        self.assertEqual(config.brain_planner_provider, "real")
        self.assertEqual(config.brain_planner_batch_size, 1)
        self.assertEqual(config.brain_runtime_budget_seconds, 14400.0)

    def test_manifest_command_contains_seed_path_and_safety_flags(self) -> None:
        command = self.manifest["run_command"]
        self.assertIn("PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass", command)
        self.assertIn("--brain-candidate-event-seed-path", self.manifest["run_command_argv"])
        self.assertIn("docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl", command)
        self.assertIn("--brain-web-mode enabled", command)
        self.assertIn("--target-gate full_thesis", command)
        self.assertIn("--brain-stage-promotion-mode strict", command)
        self.assertFalse(self.manifest["safety_assertions"]["score_allowed_before_execution"])
        self.assertFalse(self.manifest["safety_assertions"]["stage_promotion_allowed_before_execution"])
        self.assertTrue(self.manifest["safety_assertions"]["llm_query_generation_required"])
        self.assertTrue(self.manifest["safety_assertions"]["planner_batch_isolation_required"])
        self.assertEqual(self.manifest["safety_assertions"]["planner_batch_size"], 1)
        self.assertEqual(self.manifest["safety_assertions"]["runtime_budget_seconds"], 14400.0)
        self.assertIn("--brain-planner-batch-size 1", command)
        self.assertIn("--brain-runtime-budget-seconds 14400.0", command)

    def test_census_v4_seed_runtime_counter_recognizes_goal4_seed_event(self) -> None:
        event = self.plan["seed_events"][0]
        run = {"event": event}
        self.assertTrue(_planner_run_event_is_full_thesis_seed(run))


if __name__ == "__main__":
    unittest.main()
