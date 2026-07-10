import unittest
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch

from e2r.census.census_runner_v4 import (
    CensusV4RunConfig,
    _brain_audit,
    _brain_web_attempt_blockers,
    _command_string,
    _extractor_audit,
    _export_brain_web_bundle_leafs,
    _readiness_verdict,
    _web_audit,
    run_census_mode_v4,
)
from e2r.production.metadata import write_jsonl
from e2r.cli.run_e2r_census_v4_until_pass import _resolve_write_operational_docs, main as census_v4_cli_main
from e2r.research_brain.v4_schemas import SourceTaskExecutionV4
from tests.census_v4_test_helpers import census_v4_artifacts, census_v4_test_support_kwargs


def _read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


class CensusV4RunModeHonestyTests(unittest.TestCase):
    def test_reproduction_command_includes_runtime_budget_when_configured(self):
        command = _command_string(
            CensusV4RunConfig(
                as_of_date="2026-07-01",
                output_root="output/census_v4/unit",
                **census_v4_test_support_kwargs(),
                run_mode="BRAIN_AND_WEB_ACQUISITION_ENABLED",
                brain_web_mode="enabled",
                brain_runtime_budget_seconds=900.0,
            )
        )

        self.assertIn("--brain-runtime-budget-seconds 900.0", command)

    def test_brain_web_attempt_blocks_source_task_success_without_accepted_claims(self):
        blockers = _brain_web_attempt_blockers(
            real_provider_success_count=1,
            source_task_execution_count=9,
            accepted_claim_count=0,
            unique_accepted_claim_count=0,
            accepted_claim_exported_count=0,
            brain_to_claim_trace_count=0,
            stagecourt_trace_exported_count=0,
            promoted_stage_row_count=0,
        )
        self.assertIn("Research Brain source tasks produced no accepted claims", blockers)
        self.assertNotIn("Research Brain did not execute source tasks", blockers)

    def test_web_audit_task_only_is_not_real_acquisition_pass(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_jsonl(
                root / "web_search_tasks.jsonl",
                [
                    {
                        "web_task_id": "WEBTASK-A",
                        "provider_name": "NaverSearch",
                        "search_call_executed": False,
                        "status": "REJECTED_BY_POLICY",
                    }
                ],
            )
            write_jsonl(root / "web_search_results.jsonl", [])
            write_jsonl(root / "web_fetched_documents.jsonl", [])
            audit = _web_audit(
                CensusV4RunConfig(as_of_date="2026-07-01", brain_web_mode="enabled"),
                output_root=root,
            )

        self.assertEqual(audit["verdict"], "WEB_TASKS_ONLY_NOT_FETCHED")
        self.assertEqual(audit["pass_scope"], "task_only_no_search_result_or_fetch")
        self.assertFalse(audit["task_only_real_acquisition_pass_allowed"])

    def test_run_mode_request_prevents_disabled_brain_web_audit_pass(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = CensusV4RunConfig(
                as_of_date="2026-07-01",
                run_mode="BRAIN_AND_WEB_ACQUISITION_ENABLED",
                brain_web_mode="disabled",
            )
            brain = _brain_audit(config, output_root=root)
            web = _web_audit(config, output_root=root)
            extractor = _extractor_audit(config, output_root=root)

        self.assertTrue(brain["requested_by_run_mode"])
        self.assertFalse(brain["requested_by_brain_web_mode"])
        self.assertEqual(brain["verdict"], "FAIL")
        self.assertEqual(brain["llm_claimed_but_zero_calls_count"], 1)
        self.assertTrue(web["requested_by_run_mode"])
        self.assertFalse(web["requested_by_brain_web_mode"])
        self.assertEqual(web["verdict"], "FAIL")
        self.assertEqual(web["web_claimed_but_zero_search_count"], 1)
        self.assertTrue(extractor["requested_by_run_mode"])
        self.assertFalse(extractor["requested_by_brain_web_mode"])
        self.assertEqual(extractor["verdict"], "FAIL")
        self.assertEqual(extractor["llm_claim_extractor_claimed_but_zero_count"], 1)

    def test_brain_audit_counts_real_planner_attempts_separately_from_successes(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_jsonl(
                root / "planner_runs.jsonl",
                [
                    {"provider_mode": "real", "real_provider_success": True},
                    {"provider_mode": "real", "real_provider_success": True},
                    {"provider_mode": "real", "real_provider_success": False, "provider_error": "codex_cli_timeout"},
                    {
                        "provider_mode": "none",
                        "real_provider_success": False,
                        "provider_error": "planner_not_attempted_after_real_planner_limit",
                    },
                ],
            )
            brain = _brain_audit(
                CensusV4RunConfig(as_of_date="2026-07-01", brain_web_mode="enabled"),
                output_root=root,
            )

        self.assertEqual(brain["planner_run_row_count"], 4)
        self.assertEqual(brain["llm_planner_call_count"], 3)
        self.assertEqual(brain["llm_planner_attempt_count"], 3)
        self.assertEqual(brain["llm_real_provider_success_count"], 2)
        self.assertEqual(brain["llm_real_provider_failure_count"], 1)
        self.assertEqual(brain["llm_planner_not_attempted_count"], 1)
        self.assertEqual(brain["verdict"], "PASS")

    def test_brain_triage_run_mode_requires_planner_but_not_web_fetch(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = CensusV4RunConfig(
                as_of_date="2026-07-01",
                run_mode="BRAIN_TRIAGE_ENABLED",
                brain_web_mode="disabled",
            )
            brain = _brain_audit(config, output_root=root)
            web = _web_audit(config, output_root=root)
            extractor = _extractor_audit(config, output_root=root)

        self.assertTrue(brain["requested_by_run_mode"])
        self.assertEqual(brain["verdict"], "FAIL")
        self.assertFalse(web["requested_by_run_mode"])
        self.assertEqual(web["verdict"], "DISABLED_HONESTY_PASS")
        self.assertFalse(extractor["requested_by_run_mode"])
        self.assertEqual(extractor["verdict"], "DISABLED_HONESTY_PASS")

    def test_web_audit_requires_fetched_document_for_real_acquisition_pass(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_jsonl(
                root / "web_search_tasks.jsonl",
                [
                    {
                        "web_task_id": "WEBTASK-A",
                        "provider_name": "NaverSearch",
                        "search_call_executed": True,
                        "status": "SEARCH_EXECUTED",
                    }
                ],
            )
            write_jsonl(
                root / "web_search_results.jsonl",
                [{"web_result_id": "WEBRESULT-A", "web_task_id": "WEBTASK-A", "provider_name": "NaverSearch"}],
            )
            write_jsonl(root / "web_fetched_documents.jsonl", [])
            audit = _web_audit(
                CensusV4RunConfig(as_of_date="2026-07-01", brain_web_mode="enabled"),
                output_root=root,
            )

        self.assertEqual(audit["verdict"], "WEB_RESULTS_ONLY_NOT_FETCHED")
        self.assertEqual(audit["naver_search_call_count"], 1)
        self.assertNotEqual(audit["pass_scope"], "real_full_source_acquisition")

    def test_brain_web_exported_source_task_execution_has_top_level_trace_fields(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            execution = SourceTaskExecutionV4(
                task_id="TASK-A",
                source_task={
                    "task_id": "TASK-A",
                    "symbol": "003090",
                    "company_name": "대웅",
                    "candidate_event_id": "CE-LIVE-DART-003090-20260630801612",
                    "primitive_gap": "implementation_timeline",
                },
                status="NO_EVIDENCE_FOUND",
                fetched_document_ids=("DOC-A",),
            )
            _export_brain_web_bundle_leafs(
                result={
                    "bundles": {
                        "CE-LIVE-DART-003090-20260630801612": SimpleNamespace(
                            executions=(execution,),
                            documents={},
                            anchors={},
                            raw_assertions={},
                            ledger=SimpleNamespace(claims={}, mappings={}),
                        )
                    },
                    "planner_runs": (),
                },
                output_root=root,
            )
            rows = _read_jsonl(root / "source_task_executions.jsonl")

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["symbol"], "003090")
        self.assertEqual(rows[0]["company_name"], "대웅")
        self.assertEqual(rows[0]["candidate_event_id"], "CE-LIVE-DART-003090-20260630801612")
        self.assertEqual(rows[0]["source_origin"], "research_brain_v4_attempt")
        self.assertEqual(rows[0]["source_task_execution_origin"], "research_brain_v4_attempt")

    def test_brain_web_attempt_blocks_claims_that_have_no_stagecourt_trace(self):
        blockers = _brain_web_attempt_blockers(
            real_provider_success_count=1,
            source_task_execution_count=9,
            accepted_claim_count=3,
            unique_accepted_claim_count=3,
            accepted_claim_exported_count=3,
            brain_to_claim_trace_count=3,
            stagecourt_trace_exported_count=0,
            promoted_stage_row_count=0,
        )
        self.assertEqual(
            blockers,
            [
                "Research Brain accepted claims have no StageCourt trace export",
                "Research Brain StageCourt traces are not promoted into census_stage_status rows",
            ],
        )

    def test_brain_web_attempt_blocks_summary_counts_without_exported_leaf_rows(self):
        blockers = _brain_web_attempt_blockers(
            real_provider_success_count=1,
            source_task_execution_count=9,
            accepted_claim_count=3,
            unique_accepted_claim_count=3,
            accepted_claim_exported_count=3,
            source_task_exported_count=0,
            source_task_execution_exported_count=0,
            evidence_document_exported_count=0,
            evidence_anchor_exported_count=0,
            score_contribution_exported_count=0,
            brain_to_claim_trace_count=3,
            stagecourt_trace_exported_count=3,
            promoted_stage_row_count=0,
        )
        self.assertEqual(
            blockers,
            [
                "Research Brain source task attempts have no exported source_task_executions rows",
                "Research Brain source task attempts have no exported source_tasks rows",
                "Research Brain accepted claims have no exported evidence_documents rows",
                "Research Brain accepted claims have no exported evidence_anchors rows",
                "Research Brain accepted claims have no exported score_contributions rows",
                "Research Brain StageCourt traces are not promoted into census_stage_status rows",
            ],
        )

    def test_brain_web_attempt_blocks_stagecourt_trace_that_is_not_promoted(self):
        blockers = _brain_web_attempt_blockers(
            real_provider_success_count=1,
            source_task_execution_count=9,
            accepted_claim_count=3,
            unique_accepted_claim_count=3,
            accepted_claim_exported_count=3,
            brain_to_claim_trace_count=3,
            stagecourt_trace_exported_count=3,
            promoted_stage_row_count=0,
        )
        self.assertEqual(blockers, ["Research Brain StageCourt traces are not promoted into census_stage_status rows"])

    def test_brain_web_attempt_accepts_only_real_provider_claim_export_stagecourt_and_promoted_row(self):
        blockers = _brain_web_attempt_blockers(
            real_provider_success_count=1,
            source_task_execution_count=9,
            accepted_claim_count=3,
            unique_accepted_claim_count=3,
            accepted_claim_exported_count=3,
            brain_to_claim_trace_count=3,
            stagecourt_trace_exported_count=3,
            promoted_stage_row_count=3,
        )
        self.assertEqual(blockers, [])

    def test_no_brain_or_web_pass_when_artifacts_are_empty(self):
        readiness = census_v4_artifacts()["readiness"]
        labels = set(readiness["labels"])
        self.assertIn("OFFICIAL_BASELINE_OR_LEDGER_REFRESH_ONLY", labels)
        self.assertNotIn("BRAIN_WEB_EVIDENCE_PASS", labels)
        self.assertFalse(readiness["meaningful_operational_stage_pass"])
        self.assertFalse(readiness["brain_web_evidence_pass"])
        self.assertTrue(readiness["full_thesis_smoke_pass"])
        self.assertFalse(readiness["full_thesis_production_pass"])
        self.assertTrue(readiness["all_archetype_replay_pass"])
        self.assertEqual(readiness["target_gate"], "anti_fake")
        self.assertTrue(readiness["target_gate_pass"])
        self.assertEqual(readiness["anti_fake_blockers"], [])
        self.assertGreater(len(readiness["remaining_operational_gaps"]), 0)
        self.assertNotIn("all archetype", " ".join(readiness["remaining_operational_gaps"]).lower().replace("-", " "))

    def test_readiness_does_not_use_ambiguous_full_universe_label(self):
        readiness = census_v4_artifacts()["readiness"]
        self.assertNotEqual(readiness["verdict"], "FULL_UNIVERSE_STAGE_MAP_PASS")
        self.assertNotIn("FULL_UNIVERSE_STAGE_MAP_PASS", readiness["labels"])

    def test_brain_web_gate_ready_can_set_brain_web_target_pass(self):
        readiness = _readiness_verdict(
            config=CensusV4RunConfig(
                as_of_date="2026-07-01",
                brain_web_mode="enabled",
                brain_planner_provider="real",
                brain_stage_promotion_mode="strict",
                target_gate="brain_web",
            ),
            leaf_audit={"verdict": "PASS", "metrics": {"evidence_claim_payload_count": 1}},
            stage_rows=[
                {
                    "symbol": "005930",
                    "full_thesis_stage": "FULL_THESIS_NOT_RUN",
                    "census_assessment_event_id": "CAE-005930",
                    "candidate_event_count": 1,
                }
            ],
            research_brain_bridge={"bridge_mode": "missing_report_bundle", "verdict": "NOT_IMPORTED"},
            brain_web_attempt={
                "attempt_mode": "research_brain_v4_production_shadow_attempt",
                "verdict": "ATTEMPTED_WITH_SOURCE_TASKS",
                "real_provider_success_count": 1,
                "source_task_execution_count": 1,
                "accepted_claim_count": 1,
                "unique_accepted_claim_count": 1,
                "brain_to_census_claim_exported_count": 1,
                "brain_to_census_stage_exported_count": 1,
                "claim_acceptance_ready": True,
                "stagecourt_trace_ready": True,
                "cutover_export_ready": True,
                "blockers": [],
            },
            brain_stage_promotion={
                "verdict": "PROMOTION_APPLIED",
                "brain_stage_promotion_mode": "strict",
                "brain_stage_trace_count": 1,
                "brain_promoted_stage_row_count": 1,
                "unsafe_promoted_stage_row_count": 0,
                "brain_snapshot_document_count": 0,
                "blockers": [],
            },
            brain_web_readiness_gate={
                "verdict": "READY_FOR_BRAIN_WEB_EVIDENCE_PASS",
                "minimum_gate_applies": True,
                "brain_web_evidence_pass_allowed": True,
                "blockers": [],
            },
            goal_audits={},
        )

        self.assertTrue(readiness["brain_web_evidence_pass"])
        self.assertTrue(readiness["target_gate_pass"])
        self.assertEqual(readiness["target_gate"], "brain_web")
        self.assertIn("BRAIN_WEB_EVIDENCE_PASS", readiness["labels"])
        self.assertFalse(readiness["meaningful_operational_stage_pass"])

    def test_meaningful_pass_does_not_leave_unresolved_operational_gap_labels(self):
        with TemporaryDirectory() as tmp:
            output_root = Path(tmp) / "out"
            output_root.mkdir(parents=True)
            (output_root / "all_archetype_replay_matrix.json").write_text(
                json.dumps({"all_archetype_replay_pass": True}),
                encoding="utf-8",
            )
            readiness = _readiness_verdict(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(output_root),
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                    target_gate="meaningful",
                ),
                leaf_audit={
                    "verdict": "PASS",
                    "metrics": {
                        "evidence_claim_payload_count": 1,
                        "full_thesis_stage_row_count": 1,
                        "full_e2r_verified_score_present_count": 1,
                        "event_board_non_stage0_count": 0,
                        "full_thesis_refresh_queue_candidate_count": 1,
                    },
                },
                stage_rows=[
                    {
                        "symbol": "005930",
                        "stage_scope": "FULL_THESIS",
                        "base_stage": "Stage2-Watch",
                        "score_scale": "FULL_E2R_100",
                    }
                ],
                research_brain_bridge={
                    "bridge_mode": "imported_operational_report_bundle",
                    "usable_for_census_cutover": False,
                },
                brain_web_attempt={
                    "attempt_mode": "research_brain_v4_production_shadow_attempt",
                    "verdict": "ATTEMPTED_WITH_SOURCE_TASKS",
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": 1,
                    "unique_accepted_claim_count": 1,
                    "brain_to_census_claim_exported_count": 1,
                    "brain_to_census_stage_exported_count": 1,
                    "claim_acceptance_ready": True,
                    "stagecourt_trace_ready": True,
                    "cutover_export_ready": True,
                    "blockers": [],
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_stage_promotion_mode": "strict",
                    "brain_stage_trace_count": 1,
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "blockers": [],
                },
                brain_web_readiness_gate={
                    "verdict": "READY_FOR_BRAIN_WEB_EVIDENCE_PASS",
                    "minimum_gate_applies": True,
                    "brain_web_evidence_pass_allowed": True,
                    "blockers": [],
                },
                goal_audits={
                    "full_thesis_production": {
                        "verdict": "FULL_THESIS_PRODUCTION_PASS",
                        "completion_eligible": True,
                        "production_pass_allowed": True,
                        "production_full_thesis_row_count": 1,
                    },
                    "samsung_hynix_full_thesis_smoke": {
                        "verdict": "FULL_THESIS_SMOKE_PASS",
                        "full_thesis_status": "FULL_THESIS_REFRESH_RAN",
                        "score_allowed_before_execution": False,
                        "hardcoded_query_count": 0,
                        "daily_event_and_full_thesis_separated": True,
                        "per_symbol": [{"smoke_pass_allowed": True}],
                    },
                    "source_connector_capability": {"source_connector_capability_pass_allowed": True},
                    "full_thesis_seed_materialization": {
                        "verdict": "PASS",
                        "full_thesis_promoted_seed_count": 1,
                    },
                    "controlled_semantic_replay": {"controlled_semantic_replay_pass": True},
                },
            )

        self.assertTrue(readiness["meaningful_operational_stage_pass"])
        self.assertTrue(readiness["brain_web_evidence_pass_allowed"])
        self.assertTrue(readiness["full_thesis_production_pass_allowed"])
        self.assertTrue(readiness["full_thesis_smoke_requirement_pass_allowed"])
        self.assertTrue(readiness["brain_web_promoted_stagecourt_path"])
        self.assertEqual(readiness["remaining_operational_gaps"], [])

    def test_brain_web_requested_records_attempt_but_stays_not_ready_without_real_success(self):
        with TemporaryDirectory() as tmp:
            result = run_census_mode_v4(
                CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(Path(tmp) / "out"),
                    **census_v4_test_support_kwargs(),
                    run_mode="BRAIN_AND_WEB_ACQUISITION_ENABLED",
                    brain_web_mode="enabled",
                    brain_planner_provider="none",
                    fail_on_critical_audit=False,
                    write_operational_docs=False,
                )
            )
        self.assertEqual(result.readiness_verdict["verdict"], "NOT_READY")
        self.assertEqual(result.leaf_audit["critical_counts"]["llm_claimed_but_zero_calls_count"], 0)
        self.assertGreater(result.leaf_audit["metrics"]["planner_run_count"], 0)
        self.assertGreater(result.leaf_audit["critical_counts"]["llm_claimed_but_zero_real_success_count"], 0)
        self.assertGreater(result.leaf_audit["critical_counts"]["web_claimed_but_zero_search_count"], 0)
        self.assertEqual(result.leaf_audit["critical_counts"]["llm_claim_extractor_claimed_but_zero_count"], 0)
        self.assertEqual(result.readiness_verdict["brain_web_attempt"]["real_provider_success_count"], 0)
        self.assertEqual(result.readiness_verdict["brain_web_attempt"]["verdict"], "ATTEMPTED_NOT_CUTOVER_READY")
        self.assertFalse(result.readiness_verdict["brain_web_attempt"]["claim_acceptance_ready"])
        self.assertIn(
            "Research Brain source tasks produced no accepted claims",
            result.readiness_verdict["brain_web_attempt"]["blockers"],
        )
        self.assertEqual(result.readiness_verdict["brain_stage_promotion"]["verdict"], "PROMOTION_DISABLED_BY_POLICY")
        self.assertEqual(result.readiness_verdict["brain_stage_promotion"]["brain_promoted_stage_row_count"], 0)
        self.assertEqual(result.readiness_verdict["brain_web_readiness_gate"]["verdict"], "BLOCKED")
        self.assertFalse(result.readiness_verdict["brain_web_readiness_gate"]["brain_web_evidence_pass_allowed"])
        self.assertIn("LLM planner real-provider success count is zero", " ".join(result.readiness_verdict["anti_fake_blockers"]))

    def test_runtime_budget_exhausted_full_thesis_seed_is_audited_distinctly(self):
        with TemporaryDirectory() as tmp:
            output_root = Path(tmp) / "out"
            result = run_census_mode_v4(
                CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(output_root),
                    **census_v4_test_support_kwargs(),
                    max_symbols=20,
                    run_mode="BRAIN_AND_WEB_ACQUISITION_ENABLED",
                    brain_web_mode="enabled",
                    brain_planner_provider="none",
                    brain_source_acquisition="live_official_first",
                    brain_universe_limit=2,
                    brain_planner_success_limit=2,
                    brain_planner_batch_size=1,
                    brain_max_source_tasks_per_plan=1,
                    brain_max_fetches_per_task=1,
                    brain_accepted_claim_target=0,
                    brain_max_distinct_candidate_attempts=2,
                    brain_retry_max=1,
                    brain_claim_extractor_provider="rule_fallback",
                    brain_runtime_budget_seconds=0.0,
                    brain_stage_promotion_mode="disabled",
                    full_thesis_smoke_mode="disabled",
                    fail_on_critical_audit=False,
                    write_operational_docs=False,
                )
            )
            gate = result.readiness_verdict["brain_web_readiness_gate"]
            attempt = result.readiness_verdict["brain_web_attempt"]
            seed_audit = json.loads((output_root / "full_thesis_seed_materialization_audit.json").read_text(encoding="utf-8"))
            seed_trace = _read_jsonl(output_root / "full_thesis_seed_materialization_trace.jsonl")

        self.assertEqual(result.readiness_verdict["verdict"], "NOT_READY")
        self.assertGreater(attempt["full_thesis_seed_runtime_budget_exhausted_count"], 0)
        self.assertEqual(
            gate["full_thesis_seed_runtime_budget_exhausted_count"],
            attempt["full_thesis_seed_runtime_budget_exhausted_count"],
        )
        self.assertIn("full-thesis seed planner stopped after runtime budget exhaustion", gate["blockers"])
        self.assertNotIn("full-thesis seed planner runs have no real-provider success", gate["blockers"])
        self.assertGreater(seed_audit["status_counts"].get("PLANNER_PENDING_RUNTIME_BUDGET_EXHAUSTED", 0), 0)
        self.assertNotIn("PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS", seed_audit["status_counts"])
        self.assertTrue(
            all(
                "full_thesis_seed_planner_stopped_after_runtime_budget_exhausted" in row["materialization_blockers"]
                for row in seed_trace
                if row["materialization_status"] == "PLANNER_PENDING_RUNTIME_BUDGET_EXHAUSTED"
            )
        )

    def test_cli_returns_nonzero_when_readiness_is_not_ready(self):
        with TemporaryDirectory() as tmp:
            code = census_v4_cli_main(
                [
                    "--as-of-date",
                    "2026-07-01",
                    "--universe",
                    "krx",
                    "--output-root",
                    str(Path(tmp) / "out"),
                    "--v3-output-root",
                    "output/census_v3/2026-07-01",
                    "--run-mode",
                    "BRAIN_AND_WEB_ACQUISITION_ENABLED",
                    "--brain-web-mode",
                    "enabled",
                    "--fail-on-critical-audit",
                    "false",
                ]
            )
        self.assertEqual(code, 1)

    def test_cli_keyboard_interrupt_marks_partial_output_invalid(self):
        with TemporaryDirectory() as tmp:
            output_root = Path(tmp) / "interrupted"
            output_root.mkdir(parents=True, exist_ok=True)
            (output_root / "planner_runs.jsonl").write_text('{"planner_run_id":"P1"}\n{"planner_run_id":"P2"}\n', encoding="utf-8")
            (output_root / "accepted_claims.jsonl").write_text("", encoding="utf-8")
            with patch(
                "e2r.cli.run_e2r_census_v4_until_pass.run_census_mode_v4",
                side_effect=KeyboardInterrupt("unit interrupt"),
            ):
                code = census_v4_cli_main(
                    [
                        "--as-of-date",
                        "2026-07-01",
                        "--universe",
                        "krx",
                        "--output-root",
                        str(output_root),
                        "--v3-output-root",
                        "output/census_v3/2026-07-01",
                        "--run-mode",
                        "FULL_LIVE_BRAIN_CENSUS",
                        "--brain-web-mode",
                        "enabled",
                        "--brain-claim-extractor-timeout-seconds",
                        "12",
                        "--brain-runtime-budget-seconds",
                        "9",
                        "--write-operational-docs",
                        "false",
                    ]
                )
            marker = json.loads((output_root / "partial_run_invalid.json").read_text(encoding="utf-8"))

        self.assertEqual(code, 130)
        self.assertEqual(marker["verdict"], "INVALID_PARTIAL_OUTPUT")
        self.assertEqual(marker["status"], "INTERRUPTED")
        self.assertEqual(marker["reason"], "keyboard_interrupt")
        self.assertFalse(marker["readiness_evidence_allowed"])
        self.assertFalse(marker["score_or_stage_evidence_allowed"])
        self.assertFalse(marker["full_thesis_promotion_allowed"])
        self.assertEqual(marker["config"]["brain_claim_extractor_timeout_seconds"], 12.0)
        self.assertEqual(marker["config"]["brain_runtime_budget_seconds"], 9.0)
        summary = marker["partial_output_summary"]
        self.assertEqual(summary["files"]["planner_runs.jsonl"]["row_count"], 2)
        self.assertEqual(summary["files"]["accepted_claims.jsonl"]["row_count"], 0)
        self.assertGreaterEqual(summary["existing_file_count"], 2)
        self.assertGreaterEqual(summary["nonempty_file_count"], 1)

    def test_cli_runner_exception_marks_partial_output_invalid(self):
        with TemporaryDirectory() as tmp:
            output_root = Path(tmp) / "failed"
            with patch(
                "e2r.cli.run_e2r_census_v4_until_pass.run_census_mode_v4",
                side_effect=RuntimeError("unit provider failed"),
            ):
                code = census_v4_cli_main(
                    [
                        "--as-of-date",
                        "2026-07-01",
                        "--universe",
                        "krx",
                        "--output-root",
                        str(output_root),
                        "--v3-output-root",
                        "output/census_v3/2026-07-01",
                        "--run-mode",
                        "BRAIN_AND_WEB_ACQUISITION_ENABLED",
                        "--brain-web-mode",
                        "enabled",
                        "--write-operational-docs",
                        "false",
                    ]
                )
            marker = json.loads((output_root / "partial_run_invalid.json").read_text(encoding="utf-8"))

        self.assertEqual(code, 1)
        self.assertEqual(marker["verdict"], "INVALID_PARTIAL_OUTPUT")
        self.assertEqual(marker["status"], "FAILED")
        self.assertEqual(marker["reason"], "runner_exception")
        self.assertEqual(marker["exception_type"], "RuntimeError")
        self.assertIn("unit provider failed", marker["exception_message"])
        self.assertFalse(marker["readiness_evidence_allowed"])

    def test_cli_target_gate_keeps_anti_fake_exit_separate_from_meaningful_completion(self):
        with TemporaryDirectory() as tmp:
            anti_fake_code = census_v4_cli_main(
                [
                    "--as-of-date",
                    "2026-07-01",
                    "--universe",
                    "krx",
                    "--output-root",
                    str(Path(tmp) / "anti_fake"),
                    "--v3-output-root",
                    "output/census_v3/2026-07-01",
                    "--run-mode",
                    "LEDGER_REFRESH_CENSUS",
                    "--target-gate",
                    "anti_fake",
                    "--write-operational-docs",
                    "false",
                ]
            )
            meaningful_code = census_v4_cli_main(
                [
                    "--as-of-date",
                    "2026-07-01",
                    "--universe",
                    "krx",
                    "--output-root",
                    str(Path(tmp) / "meaningful"),
                    "--v3-output-root",
                    "output/census_v3/2026-07-01",
                    "--mode",
                    "HYBRID_CENSUS",
                    "--brain-web-mode",
                    "enabled",
                    "--max-iterations",
                    "10",
                    "--fail-on-run-mode-overclaim",
                    "true",
                    "--fail-on-atomic-mismatch",
                    "true",
                    "--fail-on-semantic-guard",
                    "true",
                    "--target-gate",
                    "meaningful",
                    "--fail-on-critical-audit",
                    "false",
                    "--write-operational-docs",
                    "false",
                ]
            )
        self.assertEqual(anti_fake_code, 0)
        self.assertEqual(meaningful_code, 1)

    def test_cli_target_gate_rejects_brain_web_and_production_full_thesis_until_their_leafs_exist(self):
        with TemporaryDirectory() as tmp:
            brain_web_code = census_v4_cli_main(
                [
                    "--as-of-date",
                    "2026-07-01",
                    "--universe",
                    "krx",
                    "--output-root",
                    str(Path(tmp) / "brain_web"),
                    "--v3-output-root",
                    "output/census_v3/2026-07-01",
                    "--run-mode",
                    "LEDGER_REFRESH_CENSUS",
                    "--brain-web-mode",
                    "disabled",
                    "--target-gate",
                    "brain_web",
                    "--fail-on-critical-audit",
                    "false",
                    "--write-operational-docs",
                    "false",
                ]
            )
            production_full_thesis_code = census_v4_cli_main(
                [
                    "--as-of-date",
                    "2026-07-01",
                    "--universe",
                    "krx",
                    "--output-root",
                    str(Path(tmp) / "full_thesis"),
                    "--v3-output-root",
                    "output/census_v3/2026-07-01",
                    "--run-mode",
                    "LEDGER_REFRESH_CENSUS",
                    "--brain-web-mode",
                    "disabled",
                    "--target-gate",
                    "full_thesis",
                    "--fail-on-critical-audit",
                    "false",
                    "--write-operational-docs",
                    "false",
                ]
            )
            controlled_smoke_code = census_v4_cli_main(
                [
                    "--as-of-date",
                    "2026-07-01",
                    "--universe",
                    "krx",
                    "--output-root",
                    str(Path(tmp) / "full_thesis_smoke"),
                    "--v3-output-root",
                    "output/census_v3/2026-07-01",
                    "--run-mode",
                    "LEDGER_REFRESH_CENSUS",
                    "--brain-web-mode",
                    "disabled",
                    "--full-thesis-smoke-mode",
                    "controlled_replay",
                    "--target-gate",
                    "full_thesis_smoke",
                    "--fail-on-critical-audit",
                    "false",
                    "--write-operational-docs",
                    "false",
                ]
            )
        self.assertEqual(brain_web_code, 1)
        self.assertEqual(production_full_thesis_code, 1)
        self.assertEqual(controlled_smoke_code, 0)

    def test_cli_operational_docs_auto_only_for_canonical_output_root(self):
        self.assertTrue(
            _resolve_write_operational_docs(
                as_of_date="2026-07-01",
                output_root="output/census_v4/2026-07-01",
                value="auto",
            )
        )
        self.assertFalse(
            _resolve_write_operational_docs(
                as_of_date="2026-07-01",
                output_root="/tmp/census_v4_smoke/out",
                value="auto",
            )
        )
        self.assertTrue(
            _resolve_write_operational_docs(
                as_of_date="2026-07-01",
                output_root="/tmp/census_v4_smoke/out",
                value="true",
            )
        )
        self.assertFalse(
            _resolve_write_operational_docs(
                as_of_date="2026-07-01",
                output_root="output/census_v4/2026-07-01",
                value="false",
            )
        )


if __name__ == "__main__":
    unittest.main()
