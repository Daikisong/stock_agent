import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from e2r.census.census_runner_v4 import (
    CensusV4RunConfig,
    _full_thesis_seed_runtime_counts,
    _full_thesis_smoke_requirement_pass,
    _full_thesis_smoke_requirement_satisfied_by,
    _write_full_thesis_seed_materialization_trace,
    run_census_mode_v4,
)
from e2r.production.metadata import write_jsonl
from tests.census_v4_test_helpers import census_v4_artifacts, read_json, read_jsonl


class CensusV4FullThesisSmokeTaskTests(unittest.TestCase):
    def test_production_full_thesis_never_substitutes_controlled_smoke_requirement(self):
        full_thesis_production = {
            "verdict": "FULL_THESIS_PRODUCTION_PASS",
            "completion_eligible": True,
            "production_full_thesis_row_count": 2,
            "controlled_smoke_full_thesis_row_count": 0,
            "production_symbols_without_missing_required_primitives": ["005930", "000660"],
        }
        seed_materialization = {
            "verdict": "PASS",
            "critical_count": 0,
            "full_thesis_promoted_seed_count": 2,
        }

        self.assertFalse(
            _full_thesis_smoke_requirement_pass(
                full_thesis={},
                full_thesis_production=full_thesis_production,
                full_thesis_seed_materialization=seed_materialization,
            )
        )
        self.assertIsNone(
            _full_thesis_smoke_requirement_satisfied_by(
                full_thesis={},
                full_thesis_production=full_thesis_production,
                full_thesis_seed_materialization=seed_materialization,
            )
        )

    def test_controlled_smoke_is_disabled_by_default(self):
        with TemporaryDirectory() as tmp:
            output_root = Path(tmp) / "out"
            result = run_census_mode_v4(
                CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(output_root),
                    v3_output_root="output/census_v3/2026-07-01",
                    write_operational_docs=False,
                )
            )

            smoke = read_json(output_root / "samsung_hynix_full_thesis_smoke.json")
            summary = read_json(output_root / "census_stage_summary.json")
            goal_completion = read_json(output_root / "goal_completion_audit.json")
            readiness = read_json(output_root / "readiness_verdict.json")
            operator_digest = (output_root / "operator_digest.md").read_text(encoding="utf-8")
            acceptance_report = (output_root / "acceptance_report.md").read_text(encoding="utf-8")

        self.assertFalse(result.readiness_verdict["full_thesis_smoke_pass"])
        self.assertTrue(result.readiness_verdict["full_thesis_smoke_honesty_pass"])
        self.assertFalse(result.readiness_verdict["full_thesis_smoke_execution_pass"])
        self.assertFalse(result.readiness_verdict["full_thesis_production_pass"])
        self.assertEqual(smoke["verdict"], "PENDING_FULL_THESIS_REFRESH")
        self.assertTrue(smoke["full_thesis_smoke_honesty_pass_allowed"])
        self.assertFalse(smoke["full_thesis_smoke_execution_pass_allowed"])
        self.assertEqual(smoke["full_thesis_smoke_honesty_status"], "FULL_THESIS_SMOKE_HONESTY_PASS")
        self.assertEqual(smoke["full_thesis_smoke_execution_status"], "FULL_THESIS_SMOKE_EXECUTION_PENDING")
        self.assertEqual(summary["stage_scope_distribution"].get("FULL_THESIS", 0), 0)
        self.assertEqual(summary["full_thesis_stage_row_count"], 0)
        self.assertGreater(summary["event_board_non_stage0_count"], 0)
        self.assertEqual(readiness["full_thesis_stage_row_count"], 0)
        self.assertEqual(readiness["stage_scope_notice"], "NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST")
        self.assertFalse(readiness["operational_stage_use_allowed"])
        self.assertFalse(readiness["event_board_stage_rows_are_operational_full_thesis"])
        self.assertIn("OPERATOR_STAGE_WARNING: NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST", operator_digest)
        self.assertIn("event_board_stage_rows_are_operational_full_thesis: False", operator_digest)
        self.assertIn(
            "0. Operator stage warning: stage_scope_notice=NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST",
            acceptance_report,
        )
        self.assertIn("full_thesis_refresh_queue_candidates=", acceptance_report)
        self.assertTrue(goal_completion["full_thesis_smoke_honesty_pass_allowed"])
        self.assertFalse(goal_completion["full_thesis_smoke_execution_pass_allowed"])
        self.assertIn("full_thesis_smoke_pending", goal_completion["blockers"])
        self.assertIn("full_thesis_smoke_execution_pending", goal_completion["blockers"])
        self.assertNotIn("full_thesis_smoke_honesty_false", goal_completion["blockers"])

    def test_event_board_non_stage0_rows_are_queued_for_full_thesis_refresh_not_promoted(self):
        with TemporaryDirectory() as tmp:
            output_root = Path(tmp) / "out"
            result = run_census_mode_v4(
                CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(output_root),
                    v3_output_root="output/census_v3/2026-07-01",
                    write_operational_docs=False,
                )
            )
            queue = read_jsonl(output_root / "full_thesis_refresh_queue.jsonl")
            seed_events = read_jsonl(output_root / "research_brain_full_thesis_seed_events.jsonl")
            seed_trace = read_jsonl(output_root / "full_thesis_seed_materialization_trace.jsonl")
            seed_audit = read_json(output_root / "full_thesis_seed_materialization_audit.json")
            queue_audit = read_json(output_root / "full_thesis_refresh_queue_audit.json")
            summary = read_json(output_root / "census_stage_summary.json")
            readiness = read_json(output_root / "readiness_verdict.json")
            production = read_json(output_root / "full_thesis_production_audit.json")
            production_runner = read_json(output_root / "full_thesis_production_runner_audit.json")

        self.assertGreater(summary["event_board_non_stage0_count"], 0)
        self.assertEqual(len(queue), summary["event_board_non_stage0_count"])
        self.assertEqual(summary["full_thesis_refresh_queue_candidate_count"], len(queue))
        self.assertEqual(readiness["full_thesis_refresh_queue_candidate_count"], len(queue))
        self.assertIn("FULL_THESIS_REFRESH_QUEUE_PRESENT", result.readiness_verdict["labels"])
        self.assertEqual(queue_audit["verdict"], "PASS")
        self.assertEqual(queue_audit["queue_candidate_count"], len(queue))
        self.assertEqual(queue_audit["event_board_non_stage0_count"], len(queue))
        self.assertEqual(len(seed_events), len(queue))
        self.assertEqual(len(seed_trace), len(queue))
        self.assertEqual(seed_events[0]["source_family"], "CensusFullThesisQueue")
        self.assertEqual(seed_events[0]["seed_role"], "planner_input_only")
        self.assertFalse(seed_events[0]["score_evidence_allowed"])
        self.assertFalse(seed_events[0]["stage_promotion_allowed_before_execution"])
        self.assertEqual({row["materialization_status"] for row in seed_trace}, {"PLANNER_NOT_RUN"})
        self.assertEqual(seed_audit["verdict"], "PASS")
        self.assertEqual(seed_audit["verdict_scope"], "LEDGER_INTEGRITY_ONLY")
        self.assertTrue(seed_audit["ledger_integrity_pass_allowed"])
        self.assertFalse(seed_audit["actual_materialization_pass_allowed"])
        self.assertFalse(seed_audit["full_thesis_seed_promotion_pass"])
        self.assertEqual(seed_audit["operator_materialization_status"], "PENDING_FULL_THESIS_MATERIALIZATION")
        self.assertEqual(seed_audit["seed_event_count"], len(queue))
        self.assertEqual(seed_audit["trace_row_count"], len(queue))
        self.assertEqual(seed_audit["status_counts"], {"PLANNER_NOT_RUN": len(queue)})
        self.assertEqual(seed_audit["seed_source_family_counts"], {"CensusFullThesisQueue": len(queue)})
        self.assertEqual(seed_audit["target_archetype_counts"], {"UNKNOWN": len(queue)})
        self.assertEqual(seed_audit["target_primitive_gap_counts"], {"UNKNOWN": len(queue)})
        self.assertEqual(seed_audit["critical_counts"]["blocker_follow_up_seed_missing_target_context_count"], 0)
        self.assertEqual(seed_audit["critical_count"], 0)
        self.assertEqual(seed_audit["full_thesis_promoted_seed_count"], 0)
        self.assertEqual({row["final_stage_scope"] for row in seed_trace}, {"CENSUS_EVENT_BOARD"})
        self.assertEqual({row["final_operator_stage_use"] for row in seed_trace}, {"NOT_FULL_THESIS_STAGE"})
        self.assertEqual({row["final_operator_score_use"] for row in seed_trace}, {"NOT_FULL_E2R_SCORE"})
        self.assertEqual({row["final_full_thesis_stage"] for row in seed_trace}, {"FULL_THESIS_NOT_RUN"})
        self.assertEqual({row["final_full_thesis_score_scale"] for row in seed_trace}, {"NO_SCORE"})
        self.assertEqual({row["final_is_full_thesis_stage"] for row in seed_trace}, {False})
        self.assertEqual({row["final_is_full_e2r_score"] for row in seed_trace}, {False})
        self.assertEqual({row["target_archetype_status"] for row in seed_trace}, {"BRAIN_HYPOTHESIS_REQUIRED"})
        self.assertEqual({row["target_archetype"] for row in seed_trace}, {None})
        self.assertEqual({row["seed_source_family"] for row in seed_trace}, {"CensusFullThesisQueue"})
        self.assertEqual({row["seed_event_type"] for row in seed_trace}, {"full_thesis_refresh_seed"})
        self.assertIn("source_primary_archetype", seed_trace[0])
        self.assertIn("source_missing_primitives", seed_trace[0])
        self.assertIn("source_material_gap_ids", seed_trace[0])
        self.assertTrue(all(row["planner_run_count"] == 0 for row in seed_trace))
        self.assertTrue(all(row["source_task_execution_count"] == 0 for row in seed_trace))
        self.assertTrue(all(row["accepted_claim_count"] == 0 for row in seed_trace))
        self.assertTrue(all(row["stagecourt_trace_count"] == 0 for row in seed_trace))
        self.assertTrue(all(not row["score_evidence_allowed"] for row in seed_trace))
        self.assertTrue(all(not row["stage_promotion_allowed_before_execution"] for row in seed_trace))
        self.assertEqual(readiness["brain_web_attempt"]["full_thesis_seed_event_count"], len(queue))
        self.assertFalse(readiness["brain_web_attempt"]["full_thesis_seed_consumed_by_research_brain"])
        self.assertEqual(readiness["brain_web_attempt"]["full_thesis_seed_planner_attempted_event_count"], 0)
        self.assertEqual(readiness["brain_web_attempt"]["full_thesis_seed_planner_run_row_count"], 0)
        self.assertEqual(readiness["brain_web_attempt"]["full_thesis_seed_planner_run_count"], 0)
        self.assertEqual(readiness["brain_web_attempt"]["full_thesis_seed_source_task_execution_count"], 0)
        self.assertEqual(readiness["brain_web_attempt"]["full_thesis_seed_accepted_claim_count"], 0)
        self.assertEqual(readiness["brain_web_attempt"]["full_thesis_seed_stagecourt_trace_count"], 0)
        self.assertFalse(readiness["brain_web_attempt"]["full_thesis_seed_materialized_to_stagecourt"])
        self.assertEqual(readiness["brain_web_readiness_gate"]["full_thesis_seed_event_count"], len(queue))
        self.assertFalse(readiness["brain_web_readiness_gate"]["full_thesis_seed_consumed_by_research_brain"])
        self.assertEqual(readiness["brain_web_readiness_gate"]["full_thesis_seed_planner_attempted_event_count"], 0)
        self.assertEqual(readiness["brain_web_readiness_gate"]["full_thesis_seed_planner_run_row_count"], 0)
        self.assertEqual(readiness["brain_web_readiness_gate"]["full_thesis_seed_planner_run_count"], 0)
        self.assertEqual(readiness["brain_web_readiness_gate"]["full_thesis_seed_source_task_execution_count"], 0)
        self.assertEqual(readiness["brain_web_readiness_gate"]["full_thesis_seed_accepted_claim_count"], 0)
        self.assertEqual(readiness["brain_web_readiness_gate"]["full_thesis_seed_stagecourt_trace_count"], 0)
        self.assertFalse(readiness["brain_web_readiness_gate"]["full_thesis_seed_materialized_to_stagecourt"])
        self.assertEqual(queue_audit["critical_counts"]["queue_missing_event_board_count"], 0)
        self.assertEqual(queue_audit["critical_counts"]["score_allowed_before_execution_count"], 0)
        self.assertEqual(queue_audit["critical_counts"]["stage_promotion_allowed_before_execution_count"], 0)
        self.assertEqual(queue_audit["critical_counts"]["hardcoded_query_count"], 0)
        self.assertEqual(queue_audit["critical_counts"]["unbounded_budget_count"], 0)
        self.assertEqual(queue_audit["critical_counts"]["operator_stage_copy_count"], 0)
        self.assertEqual(production["full_thesis_refresh_queue_candidate_count"], len(queue))
        self.assertEqual(production_runner["full_thesis_refresh_queue_candidate_count"], len(queue))
        self.assertEqual(readiness["full_thesis_production_runner_audit"]["full_thesis_refresh_queue_candidate_count"], len(queue))
        self.assertEqual(readiness["full_thesis_production_runner_audit"]["candidate_row_count"], 0)
        self.assertEqual(readiness["full_thesis_production_runner_audit"]["candidate_source_counts"], {})
        self.assertEqual(readiness["full_thesis_production_runner_audit"]["refresh_queue_materialized_candidate_count"], 0)
        self.assertEqual(readiness["full_thesis_production_runner_audit"]["refresh_queue_unmaterialized_candidate_count"], len(queue))
        self.assertEqual(readiness["full_thesis_seed_materialization_audit"]["seed_event_count"], len(queue))
        self.assertEqual(readiness["full_thesis_seed_materialization_audit"]["status_counts"], {"PLANNER_NOT_RUN": len(queue)})
        self.assertFalse(readiness["full_thesis_seed_materialization_audit"]["full_thesis_seed_promotion_pass"])
        self.assertTrue(readiness["full_thesis_seed_materialization_audit"]["ledger_integrity_pass_allowed"])
        self.assertFalse(readiness["full_thesis_seed_materialization_audit"]["actual_materialization_pass_allowed"])
        self.assertEqual(
            readiness["full_thesis_seed_materialization_audit"]["operator_materialization_status"],
            "PENDING_FULL_THESIS_MATERIALIZATION",
        )
        self.assertEqual(readiness["full_thesis_seed_materialization_audit"]["critical_count"], 0)
        self.assertFalse(production["production_pass_allowed"])
        self.assertEqual(production["production_full_thesis_row_count"], 0)

        for task in queue:
            self.assertEqual(task["task_type"], "full_thesis_refresh_task")
            self.assertEqual(task["task_status"], "PLANNING_REQUIRED")
            self.assertEqual(task["source_stage_scope"], "CENSUS_EVENT_BOARD")
            self.assertEqual(task["operator_stage_use"], "NOT_FULL_THESIS_STAGE")
            self.assertEqual(task["target_archetype_status"], "BRAIN_HYPOTHESIS_REQUIRED")
            self.assertIsNone(task["target_archetype"])
            self.assertTrue(task["planner_required"])
            self.assertTrue(task["llm_query_required"])
            self.assertFalse(task["score_allowed_before_execution"])
            self.assertFalse(task["stage_promotion_allowed_before_execution"])
            self.assertTrue(task["official_first_required"])
            self.assertEqual(task["hardcoded_query_count"], 0)
            self.assertEqual(task["hardcoded_queries"], [])
            self.assertEqual(task["query_intents"], [])
            self.assertGreater(task["max_source_tasks"], 0)
            self.assertGreater(task["max_queries_per_task"], 0)
            self.assertGreater(task["max_candidates_per_query"], 0)
            self.assertGreater(task["max_fetches_per_task"], 0)
            self.assertIn("source_backed_primitive_coverage_required", task["missing_full_thesis_primitives"])
            self.assertIn("unbounded_general_search", task["forbidden_source_classes"])
            self.assertEqual(task["blocked_reason"], "full_thesis_refresh_task_not_run")

    def test_blocker_follow_up_seed_materialization_audit_keeps_target_gap_context(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            seed_path = root / "full_thesis_blocker_follow_up_seed_events.jsonl"
            write_jsonl(
                seed_path,
                [
                    {
                        "candidate_event_id": "CEV4-FTGAP-C06-HBM",
                        "symbol": "000660",
                        "company_name": "SK하이닉스",
                        "source_family": "CensusFullThesisBlockerFollowUp",
                        "source_id": str(root / "full_thesis_blocker_follow_up_source_tasks.jsonl"),
                        "event_type": "full_thesis_blocker_follow_up_seed",
                        "target_archetype": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                        "primitive_gap": "hbm_capacity_constraint",
                        "follow_up_task_id": "FTGAP-UNIT",
                        "follow_up_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                        "follow_up_primitive_gap": "hbm_capacity_constraint",
                        "seed_role": "planner_input_only",
                        "score_evidence_allowed": False,
                        "stage_promotion_allowed_before_execution": False,
                        "structured_payload": {
                            "target_archetype": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                            "primitive_gap": "hbm_capacity_constraint",
                        },
                    }
                ],
            )
            write_jsonl(root / "planner_runs.jsonl", [])
            write_jsonl(root / "source_task_executions.jsonl", [])
            write_jsonl(root / "stagecourt_traces.jsonl", [])

            _write_full_thesis_seed_materialization_trace(
                output_root=root,
                seed_path=seed_path,
                stage_rows=[
                    {
                        "symbol": "000660",
                        "stage_scope": "CENSUS_EVENT_BOARD",
                        "operator_stage_use": "NOT_FULL_THESIS_STAGE",
                        "operator_score_use": "NOT_FULL_E2R_SCORE",
                        "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                        "full_thesis_score_scale": "NO_SCORE",
                        "score_scale": "NO_SCORE",
                    }
                ],
            )
            trace = read_jsonl(root / "full_thesis_seed_materialization_trace.jsonl")
            audit = read_json(root / "full_thesis_seed_materialization_audit.json")

        self.assertEqual(len(trace), 1)
        self.assertEqual(trace[0]["seed_source_family"], "CensusFullThesisBlockerFollowUp")
        self.assertEqual(trace[0]["seed_event_type"], "full_thesis_blocker_follow_up_seed")
        self.assertEqual(trace[0]["follow_up_task_id"], "FTGAP-UNIT")
        self.assertEqual(trace[0]["target_archetype"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(trace[0]["target_primitive_gap"], "hbm_capacity_constraint")
        self.assertEqual(audit["seed_source_family_counts"], {"CensusFullThesisBlockerFollowUp": 1})
        self.assertEqual(audit["target_archetype_counts"], {"C06_HBM_MEMORY_CUSTOMER_CAPACITY": 1})
        self.assertEqual(audit["target_primitive_gap_counts"], {"hbm_capacity_constraint": 1})
        self.assertEqual(
            audit["status_counts_by_target_archetype"],
            {"C06_HBM_MEMORY_CUSTOMER_CAPACITY": {"PLANNER_NOT_RUN": 1}},
        )
        self.assertEqual(
            audit["status_counts_by_target_primitive_gap"],
            {"hbm_capacity_constraint": {"PLANNER_NOT_RUN": 1}},
        )
        self.assertEqual(audit["critical_counts"]["blocker_follow_up_seed_missing_target_context_count"], 0)

    def test_enabled_provider_none_measures_seed_planner_consumption_without_materialization(self):
        with TemporaryDirectory() as tmp:
            output_root = Path(tmp) / "out"
            run_census_mode_v4(
                CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(output_root),
                    v3_output_root="output/census_v3/2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="none",
                    brain_universe_limit=2,
                    brain_planner_success_limit=1,
                    brain_planner_batch_size=1,
                    write_operational_docs=False,
                    fail_on_critical_audit=False,
                )
            )
            readiness = read_json(output_root / "readiness_verdict.json")
            planner_runs = read_jsonl(output_root / "planner_runs.jsonl")
            seed_trace = read_jsonl(output_root / "full_thesis_seed_materialization_trace.jsonl")

        attempt = readiness["brain_web_attempt"]
        gate = readiness["brain_web_readiness_gate"]
        seed_planner_run_count = sum(
            1
            for row in planner_runs
            if ((row.get("event") or {}).get("source_family") == "CensusFullThesisQueue")
            or ((row.get("event") or {}).get("event_type") == "full_thesis_refresh_seed")
        )
        self.assertGreater(attempt["full_thesis_seed_event_count"], 0)
        self.assertFalse(attempt["full_thesis_seed_consumed_by_research_brain"])
        self.assertEqual(attempt["full_thesis_seed_planner_attempted_event_count"], attempt["full_thesis_seed_planner_run_count"])
        self.assertEqual(attempt["full_thesis_seed_planner_run_row_count"], seed_planner_run_count)
        self.assertGreater(attempt["full_thesis_seed_planner_run_count"], 0)
        self.assertEqual(attempt["full_thesis_seed_real_provider_success_count"], 0)
        self.assertEqual(attempt["full_thesis_seed_source_task_execution_count"], 0)
        self.assertEqual(attempt["full_thesis_seed_accepted_claim_count"], 0)
        self.assertEqual(attempt["full_thesis_seed_stagecourt_trace_count"], 0)
        self.assertFalse(attempt["full_thesis_seed_materialized_to_stagecourt"])
        self.assertEqual(gate["full_thesis_seed_planner_attempted_event_count"], attempt["full_thesis_seed_planner_attempted_event_count"])
        self.assertEqual(gate["full_thesis_seed_planner_run_row_count"], attempt["full_thesis_seed_planner_run_row_count"])
        self.assertEqual(gate["full_thesis_seed_planner_run_count"], attempt["full_thesis_seed_planner_run_count"])
        self.assertEqual(gate["full_thesis_seed_real_provider_success_count"], 0)
        self.assertEqual(gate["full_thesis_seed_source_task_execution_count"], 0)
        self.assertEqual(gate["full_thesis_seed_accepted_claim_count"], 0)
        self.assertEqual(gate["full_thesis_seed_stagecourt_trace_count"], 0)
        self.assertFalse(gate["full_thesis_seed_materialized_to_stagecourt"])
        self.assertEqual((planner_runs[0]["event"] or {})["source_family"], "CensusFullThesisQueue")
        self.assertIn("full-thesis seed planner runs have no real-provider success", gate["blockers"])
        trace_status_counts = {}
        for row in seed_trace:
            trace_status_counts[row["materialization_status"]] = trace_status_counts.get(row["materialization_status"], 0) + 1
        self.assertGreater(trace_status_counts.get("PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS", 0), 0)
        self.assertGreater(trace_status_counts.get("PLANNER_NOT_RUN", 0), 0)
        self.assertEqual(
            trace_status_counts["PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS"],
            attempt["full_thesis_seed_planner_run_count"],
        )
        self.assertTrue(
            all(
                row["planner_real_provider_success_count"] == 0
                for row in seed_trace
                if row["materialization_status"] == "PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS"
            )
        )

    def test_external_brain_candidate_seed_path_is_copied_and_consumed(self):
        with TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            external_seed_path = temp_root / "previous" / "full_thesis_blocker_follow_up_seed_events.jsonl"
            external_seed_path.parent.mkdir(parents=True)
            write_jsonl(
                external_seed_path,
                [
                    {
                        "candidate_event_id": "CEV4-FTGAP-000660-UNIT",
                        "symbol": "000660",
                        "company_name": "SK하이닉스",
                        "event_date": "2026-07-01",
                        "detected_at": "2026-07-01",
                        "source_family": "CensusFullThesisBlockerFollowUp",
                        "source_id": "previous/full_thesis_blocker_follow_up_source_tasks.jsonl",
                        "event_type": "full_thesis_blocker_follow_up_seed",
                        "research_brain_eligible": True,
                        "score_evidence_allowed": False,
                        "stage_promotion_allowed_before_execution": False,
                        "structured_payload": {
                            "seed_role": "planner_input_only",
                            "follow_up_origin": "full_thesis_green_gate_blocker_follow_up",
                            "follow_up_primitive_gap": "hbm_capacity_pre_sold",
                            "follow_up_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                            "llm_query_required": True,
                            "llm_query_allowed": True,
                            "hardcoded_query_count": 0,
                        },
                    }
                ],
            )
            output_root = temp_root / "out"
            run_census_mode_v4(
                CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(output_root),
                    v3_output_root="output/census_v3/2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="none",
                    brain_candidate_event_seed_path=str(external_seed_path),
                    brain_universe_limit=1,
                    brain_planner_success_limit=1,
                    brain_planner_batch_size=1,
                    write_operational_docs=False,
                    fail_on_critical_audit=False,
                )
            )
            used_seed = read_jsonl(output_root / "research_brain_candidate_seed_events_used.jsonl")
            seed_trace = read_jsonl(output_root / "full_thesis_seed_materialization_trace.jsonl")
            readiness = read_json(output_root / "readiness_verdict.json")

        attempt = readiness["brain_web_attempt"]
        gate = readiness["brain_web_readiness_gate"]
        self.assertEqual(len(used_seed), 1)
        self.assertEqual(used_seed[0]["candidate_event_id"], "CEV4-FTGAP-000660-UNIT")
        self.assertEqual(attempt["full_thesis_seed_source"], "external_candidate_event_seed_path")
        self.assertEqual(attempt["full_thesis_seed_original_path"], str(external_seed_path))
        self.assertEqual(attempt["full_thesis_seed_event_count"], 1)
        self.assertEqual(attempt["full_thesis_seed_event_path"], str(output_root / "research_brain_candidate_seed_events_used.jsonl"))
        self.assertEqual(gate["full_thesis_seed_source"], "external_candidate_event_seed_path")
        self.assertEqual(gate["full_thesis_seed_event_count"], 1)
        self.assertEqual(len(seed_trace), 1)
        self.assertEqual(seed_trace[0]["candidate_event_id"], "CEV4-FTGAP-000660-UNIT")
        self.assertEqual(seed_trace[0]["materialization_status"], "PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS")
        self.assertEqual(seed_trace[0]["planner_run_count"], 1)
        self.assertEqual(seed_trace[0]["planner_real_provider_success_count"], 0)

    def test_seed_runtime_counts_split_attempted_seed_events_from_planner_rows(self):
        planner_runs = [
            {
                "planner_run_id": "PLAN-SEED-A-INITIAL",
                "event": {
                    "candidate_event_id": "CE-SEED-A",
                    "source_family": "CensusFullThesisQueue",
                    "event_type": "full_thesis_refresh_seed",
                },
                "real_provider_success": False,
            },
            {
                "planner_run_id": "PLAN-SEED-A-RETRY",
                "event": {
                    "candidate_event_id": "CE-SEED-A",
                    "source_family": "CensusFullThesisQueue",
                    "event_type": "full_thesis_refresh_seed",
                },
                "real_provider_success": True,
            },
            {
                "planner_run_id": "PLAN-SEED-B-INITIAL",
                "event": {
                    "candidate_event_id": "CE-SEED-B",
                    "source_family": "CensusFullThesisQueue",
                    "event_type": "full_thesis_refresh_seed",
                },
                "real_provider_success": True,
            },
            {
                "planner_run_id": "PLAN-DAILY-C",
                "event": {
                    "candidate_event_id": "CE-DAILY-C",
                    "source_family": "DART",
                    "event_type": "official_disclosure",
                },
                "real_provider_success": True,
            },
        ]
        result = {
            "source_acquisition_report": {
                "rows": [
                    {"candidate_event_id": "CE-SEED-A", "accepted_claim_ids": ["CLM-A"]},
                    {"candidate_event_id": "CE-DAILY-C", "accepted_claim_ids": ["CLM-C"]},
                ]
            },
            "watchlist_report": {
                "rows": [
                    {"candidate_event_id": "CE-SEED-A", "stage_court_trace": {"stagecourt_trace_id": "SCT-A"}},
                    {"candidate_event_id": "CE-DAILY-C", "stage_court_trace": {"stagecourt_trace_id": "SCT-C"}},
                ]
            },
        }

        counts = _full_thesis_seed_runtime_counts(result=result, planner_runs=planner_runs)

        self.assertEqual(counts["planner_attempted_event_count"], 2)
        self.assertEqual(counts["planner_run_row_count"], 3)
        self.assertEqual(counts["planner_run_count"], 2)
        self.assertEqual(counts["real_provider_success_count"], 2)
        self.assertEqual(counts["source_task_execution_count"], 1)
        self.assertEqual(counts["accepted_claim_count"], 1)
        self.assertEqual(counts["stagecourt_trace_count"], 1)

    def test_seed_materialization_trace_and_audit_cover_all_runtime_statuses(self):
        seed_rows = []
        stage_rows = []
        event_specs = [
            ("CE-SEED-1", "000001", "PLANNER_NOT_RUN"),
            ("CE-SEED-2", "000002", "PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS"),
            ("CE-SEED-3", "000003", "SOURCE_TASK_NOT_EXECUTED"),
            ("CE-SEED-4", "000004", "ACCEPTED_CLAIM_NOT_CREATED"),
            ("CE-SEED-5", "000005", "STAGECOURT_TRACE_NOT_CREATED"),
            ("CE-SEED-6", "000006", "STAGECOURT_READY_NOT_PROMOTED"),
            ("CE-SEED-7", "000007", "FULL_THESIS_PROMOTED"),
        ]
        for event_id, symbol, _ in event_specs:
            seed_rows.append(
                {
                    "candidate_event_id": event_id,
                    "symbol": symbol,
                    "company_name": f"테스트{symbol}",
                    "source_family": "CensusFullThesisQueue",
                    "seed_role": "planner_input_only",
                    "score_evidence_allowed": False,
                    "stage_promotion_allowed_before_execution": False,
                    "structured_payload": {"queue_task_id": f"FTQ-{symbol}"},
                }
            )
            stage_rows.append(
                {
                    "symbol": symbol,
                    "stage_scope": "FULL_THESIS" if symbol == "000007" else "CENSUS_EVENT_BOARD",
                    "operator_stage_use": "FULL_THESIS_STAGE" if symbol == "000007" else "NOT_FULL_THESIS_STAGE",
                    "operator_score_use": "FULL_E2R_SCORE" if symbol == "000007" else "NOT_FULL_E2R_SCORE",
                    "full_thesis_stage": "Stage3-Yellow" if symbol == "000007" else "FULL_THESIS_NOT_RUN",
                    "full_thesis_score_scale": "FULL_E2R_100" if symbol == "000007" else "NO_SCORE",
                    "score_scale": "FULL_E2R_100" if symbol == "000007" else "NO_SCORE",
                    "is_full_thesis_stage": symbol == "000007",
                    "is_full_e2r_score": symbol == "000007",
                    "full_thesis_candidate_event_id": event_id if symbol == "000007" else None,
                    "full_thesis_candidate_event_ids": [event_id] if symbol == "000007" else [],
                }
            )

        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            seed_path = root / "research_brain_full_thesis_seed_events.jsonl"
            write_jsonl(seed_path, seed_rows)
            write_jsonl(
                root / "planner_runs.jsonl",
                [
                    {
                        "planner_run_id": f"PLAN-{event_id}",
                        "event": {"candidate_event_id": event_id},
                        "real_provider_success": status != "PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS",
                    }
                    for event_id, _, status in event_specs
                    if status != "PLANNER_NOT_RUN"
                ],
            )
            write_jsonl(
                root / "source_task_executions.jsonl",
                [
                    {
                        "task_id": f"TASK-{event_id}",
                        "candidate_event_id": event_id,
                        "accepted_claim_ids": [f"CLM-{event_id}"] if status not in {"ACCEPTED_CLAIM_NOT_CREATED"} else [],
                    }
                    for event_id, _, status in event_specs
                    if status
                    not in {
                        "PLANNER_NOT_RUN",
                        "PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS",
                        "SOURCE_TASK_NOT_EXECUTED",
                    }
                ],
            )
            write_jsonl(
                root / "stagecourt_traces.jsonl",
                [
                    {
                        "stagecourt_trace_id": f"SCT-{event_id}",
                        "candidate_event_id": event_id,
                        "accepted_claim_ids": [f"CLM-{event_id}"],
                        "score_contribution_ids": [f"SCON-{event_id}"],
                    }
                    for event_id, _, status in event_specs
                    if status in {"STAGECOURT_READY_NOT_PROMOTED", "FULL_THESIS_PROMOTED"}
                ],
            )

            _write_full_thesis_seed_materialization_trace(
                output_root=root,
                seed_path=seed_path,
                stage_rows=stage_rows,
            )
            trace = read_jsonl(root / "full_thesis_seed_materialization_trace.jsonl")
            audit = read_json(root / "full_thesis_seed_materialization_audit.json")

        status_counts = {}
        for row in trace:
            status_counts[row["materialization_status"]] = status_counts.get(row["materialization_status"], 0) + 1
        self.assertEqual(status_counts, {status: 1 for _, _, status in event_specs})
        self.assertEqual(audit["verdict"], "PASS")
        self.assertEqual(audit["verdict_scope"], "ACTUAL_FULL_THESIS_MATERIALIZATION")
        self.assertTrue(audit["ledger_integrity_pass_allowed"])
        self.assertTrue(audit["actual_materialization_pass_allowed"])
        self.assertTrue(audit["full_thesis_seed_promotion_pass"])
        self.assertEqual(audit["operator_materialization_status"], "FULL_THESIS_MATERIALIZED")
        self.assertEqual(audit["critical_count"], 0)
        self.assertEqual(audit["seed_event_count"], len(event_specs))
        self.assertEqual(audit["trace_row_count"], len(event_specs))
        self.assertEqual(audit["status_counts"], {status: 1 for _, _, status in event_specs})
        self.assertEqual(
            audit["final_operator_stage_use_counts"],
            {"FULL_THESIS_STAGE": 1, "NOT_FULL_THESIS_STAGE": len(event_specs) - 1},
        )
        self.assertEqual(
            audit["final_operator_score_use_counts"],
            {"FULL_E2R_SCORE": 1, "NOT_FULL_E2R_SCORE": len(event_specs) - 1},
        )
        self.assertEqual(audit["full_thesis_promoted_seed_count"], 1)
        self.assertEqual(audit["stagecourt_trace_seed_count"], 2)
        self.assertEqual(audit["accepted_claim_seed_count"], 3)
        self.assertIn("SOURCE_TASK_NOT_EXECUTED", audit["next_actions_by_status"])

    def test_samsung_hynix_smoke_tasks_execute_with_claim_backed_full_thesis_evidence(self):
        artifacts = census_v4_artifacts()
        root = artifacts["output_root"]
        tasks = read_jsonl(root / "full_thesis_smoke_tasks.jsonl")
        smoke = read_json(root / "samsung_hynix_full_thesis_smoke.json")
        goal_completion = read_json(root / "goal_completion_audit.json")

        required_primitives = smoke["required_full_thesis_primitives"]
        self.assertEqual(smoke["target_full_thesis_archetype"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(smoke["smoke_task_count"], len(tasks))
        self.assertEqual(smoke["hardcoded_query_count"], 0)
        self.assertEqual(len(tasks), 2 * len(required_primitives))
        self.assertEqual({task["symbol"] for task in tasks}, {"005930", "000660"})
        self.assertEqual({task["primitive_gap"] for task in tasks}, set(required_primitives))

        for task in tasks:
            self.assertEqual(task["task_status"], "EXECUTED_ACCEPTED")
            self.assertEqual(task["target_archetype"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
            self.assertFalse(task["llm_query_required"])
            self.assertEqual(task["hardcoded_query_count"], 0)
            self.assertEqual(task["hardcoded_queries"], [])
            self.assertEqual(task["query_intents"], [])
            self.assertFalse(task["score_allowed_before_execution"])
            self.assertTrue(task["score_evidence"])
            self.assertGreater(len(task["accepted_claim_ids"]), 0)
            self.assertGreater(len(task["stagecourt_trace_ids"]), 0)
            self.assertGreater(task["max_fetches"], 0)
            self.assertIsInstance(task["max_fetches"], int)
            self.assertIn("TrustedNews", task["preferred_source_classes"])
            self.assertIn("snippet_only_score", task["forbidden_source_classes"])

        self.assertEqual(smoke["verdict"], "FULL_THESIS_SMOKE_PASS")
        self.assertEqual(smoke["full_thesis_status"], "FULL_THESIS_REFRESH_RAN")
        self.assertTrue(smoke["full_thesis_smoke_honesty_pass_allowed"])
        self.assertTrue(smoke["full_thesis_smoke_execution_pass_allowed"])
        self.assertEqual(smoke["full_thesis_smoke_honesty_status"], "FULL_THESIS_SMOKE_HONESTY_PASS")
        self.assertEqual(smoke["full_thesis_smoke_execution_status"], "FULL_THESIS_SMOKE_EXECUTION_PASS")
        self.assertFalse(smoke["score_allowed_before_execution"])
        self.assertFalse(goal_completion["goal_completion_ready"])
        self.assertTrue(goal_completion["full_thesis_smoke_honesty_pass_allowed"])
        self.assertTrue(goal_completion["full_thesis_smoke_execution_pass_allowed"])
        self.assertNotIn("full_thesis_smoke_pending", goal_completion["blockers"])
        self.assertNotIn("full_thesis_smoke_execution_pending", goal_completion["blockers"])
        self.assertIn("full_thesis_production_pass_false", goal_completion["blockers"])
        self.assertFalse(goal_completion["full_thesis_production_pass_allowed"])
        self.assertNotIn("source_backed_replay_parity_all_archetypes_pending", goal_completion["blockers"])

    def test_samsung_hynix_smoke_records_full_thesis_trace_per_symbol(self):
        root = census_v4_artifacts()["output_root"]
        smoke = read_json(root / "samsung_hynix_full_thesis_smoke.json")
        required_primitives = set(smoke["required_full_thesis_primitives"])
        rows = {row["symbol"]: row for row in smoke["per_symbol"]}

        self.assertEqual(set(rows), {"005930", "000660"})
        for symbol, row in rows.items():
            self.assertGreater(len(row["daily_event_claim_ids"]), 0, symbol)
            self.assertGreater(len(row["daily_event_score_contribution_ids"]), 0, symbol)
            self.assertGreater(len(row["daily_event_stagecourt_trace_ids"]), 0, symbol)
            self.assertGreater(len(row["full_thesis_claim_ids"]), 0, symbol)
            self.assertGreater(len(row["full_thesis_score_contribution_ids"]), 0, symbol)
            self.assertGreater(len(row["full_thesis_stagecourt_trace_ids"]), 0, symbol)
            self.assertEqual(row["missing_full_thesis_primitives"], [])
            self.assertEqual(len(row["full_thesis_source_task_ids"]), len(required_primitives))
            self.assertTrue(row["smoke_pass_allowed"])
            self.assertIsNone(row["blocking_reason"])

    def test_full_thesis_smoke_score_is_score_contribution_sum(self):
        root = census_v4_artifacts()["output_root"]
        stage_rows = {row["symbol"]: row for row in read_jsonl(root / "census_stage_status.jsonl")}
        contributions = {row["score_contribution_id"]: row for row in read_jsonl(root / "score_contributions.jsonl")}
        traces = {row["stagecourt_trace_id"]: row for row in read_jsonl(root / "stagecourt_traces.jsonl")}
        atomic_rows = {row["atomic_stage_decision_id"]: row for row in read_jsonl(root / "atomic_stage_decisions.jsonl")}

        for symbol in ("005930", "000660"):
            row = stage_rows[symbol]
            ids = row["full_thesis_score_contribution_ids"]
            contribution_sum = round(sum(float(contributions[item]["raw_points"]) for item in ids), 4)
            trace = traces[row["stagecourt_trace_id"]]
            atomic = atomic_rows[row["atomic_stage_decision_id"]]

            self.assertEqual(row["score_build_method"], "primitive_score_contribution_sum")
            self.assertEqual(row["score_source"], "SCORE_CONTRIBUTION_SUM")
            self.assertEqual(row["full_thesis_verified_score"], contribution_sum)
            self.assertEqual(row["full_e2r_verified_score"], contribution_sum)
            self.assertEqual(row["score_interval_lower"], contribution_sum)
            self.assertEqual(trace["score_interval"]["lower"], contribution_sum)
            self.assertEqual(atomic["full_e2r_verified_score"], contribution_sum)
            self.assertTrue(all(contributions[item]["score_build_method"] == "primitive_score_contribution_sum" for item in ids))

    def test_full_thesis_smoke_has_no_symbol_total_score_stage_constants(self):
        source = Path("src/e2r/census/census_runner_v4.py").read_text(encoding="utf-8")
        self.assertNotIn("FULL_THESIS_SMOKE_SCORES", source)
        self.assertNotIn("FULL_THESIS_SMOKE_STAGES", source)

    def test_controlled_smoke_cannot_satisfy_full_live_or_meaningful_gate(self):
        with TemporaryDirectory() as tmp:
            output_root = Path(tmp) / "out"
            result = run_census_mode_v4(
                CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(output_root),
                    v3_output_root="output/census_v3/2026-07-01",
                    run_mode="FULL_LIVE_BRAIN_CENSUS",
                    brain_web_mode="enabled",
                    brain_planner_provider="none",
                    brain_stage_promotion_mode="strict",
                    full_thesis_smoke_mode="controlled_replay",
                    target_gate="meaningful",
                    fail_on_critical_audit=False,
                    write_operational_docs=False,
                )
            )
            smoke = read_json(output_root / "samsung_hynix_full_thesis_smoke.json")
            production = read_json(output_root / "full_thesis_production_audit.json")
            goal_completion = read_json(output_root / "goal_completion_audit.json")

        self.assertEqual(smoke["verdict"], "PENDING_FULL_THESIS_REFRESH")
        self.assertFalse(result.readiness_verdict["full_thesis_smoke_pass"])
        self.assertTrue(result.readiness_verdict["full_thesis_smoke_honesty_pass"])
        self.assertFalse(result.readiness_verdict["full_thesis_smoke_execution_pass"])
        self.assertFalse(result.readiness_verdict["full_thesis_smoke_gate_pass_allowed"])
        self.assertIn("full_thesis_smoke_not_passed", result.readiness_verdict["full_thesis_smoke_gate_blockers"])
        self.assertFalse(result.readiness_verdict["target_gate_pass"])
        self.assertFalse(result.readiness_verdict["meaningful_operational_stage_pass"])
        self.assertFalse(result.readiness_verdict["full_thesis_production_pass"])
        self.assertFalse(production["production_pass_allowed"])
        self.assertTrue(production["production_mode_requested"])
        self.assertEqual(production["controlled_smoke_full_thesis_row_count"], 0)
        self.assertEqual(production["production_full_thesis_row_count"], 0)
        self.assertIn("full_thesis_production_pass_false", goal_completion["blockers"])

    def test_full_thesis_smoke_target_is_allowed_only_as_explicit_non_production_smoke_gate(self):
        with TemporaryDirectory() as tmp:
            output_root = Path(tmp) / "out"
            result = run_census_mode_v4(
                CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(output_root),
                    v3_output_root="output/census_v3/2026-07-01",
                    run_mode="LEDGER_REFRESH_CENSUS",
                    brain_web_mode="disabled",
                    full_thesis_smoke_mode="controlled_replay",
                    target_gate="full_thesis_smoke",
                    write_operational_docs=False,
                )
            )
            production = read_json(output_root / "full_thesis_production_audit.json")
            stage_rows = read_jsonl(output_root / "census_stage_status.jsonl")

        self.assertTrue(result.readiness_verdict["full_thesis_smoke_pass"])
        self.assertTrue(result.readiness_verdict["full_thesis_smoke_honesty_pass"])
        self.assertTrue(result.readiness_verdict["full_thesis_smoke_execution_pass"])
        self.assertTrue(result.readiness_verdict["full_thesis_smoke_gate_pass_allowed"])
        self.assertEqual(result.readiness_verdict["full_thesis_smoke_gate_blockers"], [])
        self.assertTrue(result.readiness_verdict["target_gate_pass"])
        self.assertFalse(result.readiness_verdict["full_thesis_production_pass"])
        self.assertFalse(production["production_mode_requested"])
        smoke_rows = [row for row in stage_rows if row.get("is_controlled_smoke_full_thesis_stage") is True]
        self.assertEqual(len(smoke_rows), 2)
        self.assertEqual({row["operator_stage_use"] for row in smoke_rows}, {"SMOKE_ONLY_STAGE_NOT_PRODUCTION"})
        self.assertEqual({row["operator_score_use"] for row in smoke_rows}, {"SMOKE_ONLY_SCORE_NOT_PRODUCTION"})
        self.assertTrue(all(row["operator_scope_note"] == "controlled_smoke_full_thesis_not_production" for row in smoke_rows))
        self.assertTrue(all(row["stage_scope"] == "FULL_THESIS" for row in smoke_rows))
        self.assertFalse(any(row["is_full_thesis_stage"] for row in smoke_rows))
        self.assertFalse(any(row["is_full_e2r_score"] for row in smoke_rows))

    def test_external_controlled_smoke_artifact_clears_smoke_requirement_without_promoting_production(self):
        with TemporaryDirectory() as tmp:
            smoke_root = Path(tmp) / "smoke"
            run_census_mode_v4(
                CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(smoke_root),
                    v3_output_root="output/census_v3/2026-07-01",
                    run_mode="LEDGER_REFRESH_CENSUS",
                    brain_web_mode="disabled",
                    full_thesis_smoke_mode="controlled_replay",
                    target_gate="full_thesis_smoke",
                    write_operational_docs=False,
                )
            )

            output_root = Path(tmp) / "out"
            run_census_mode_v4(
                CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(output_root),
                    v3_output_root="output/census_v3/2026-07-01",
                    run_mode="LEDGER_REFRESH_CENSUS",
                    brain_web_mode="disabled",
                    full_thesis_smoke_artifact_root=str(smoke_root),
                    write_operational_docs=False,
                )
            )
            smoke = read_json(output_root / "samsung_hynix_full_thesis_smoke.json")
            completion = read_json(output_root / "goal_completion_audit.json")
            production = read_json(output_root / "full_thesis_production_audit.json")
            stage_rows = read_jsonl(output_root / "census_stage_status.jsonl")

        self.assertEqual(smoke["verdict"], "FULL_THESIS_SMOKE_PASS")
        self.assertTrue(smoke["external_smoke_artifact_used"])
        self.assertEqual(completion["full_thesis_smoke_requirement_satisfied_by"], "external_controlled_smoke")
        self.assertTrue(completion["full_thesis_smoke_requirement_pass_allowed"])
        self.assertTrue(completion["full_thesis_smoke_execution_pass_allowed"])
        self.assertNotIn("full_thesis_smoke_pending", completion["blockers"])
        self.assertNotIn("full_thesis_smoke_execution_pending", completion["blockers"])
        self.assertIn("full_thesis_production_pass_false", completion["blockers"])
        self.assertFalse(production["production_pass_allowed"])
        self.assertEqual(production["production_full_thesis_row_count"], 0)
        self.assertFalse(any(row.get("is_controlled_smoke_full_thesis_stage") is True for row in stage_rows))


if __name__ == "__main__":
    unittest.main()
