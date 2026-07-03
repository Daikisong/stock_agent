import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from e2r.census.census_runner_v4 import CensusV4RunConfig, _brain_web_readiness_gate_audit, run_census_mode_v4
from e2r.production.metadata import write_jsonl
from tests.census_v4_test_helpers import census_v4_artifacts, read_json


class CensusV4BrainWebReadinessGateTests(unittest.TestCase):
    def test_canonical_disabled_run_records_not_requested_not_pass(self):
        root = census_v4_artifacts()["output_root"]
        gate = read_json(root / "brain_web_readiness_gate_audit.json")
        readiness = read_json(root / "readiness_verdict.json")

        self.assertEqual(gate["verdict"], "NOT_REQUESTED")
        self.assertFalse(gate["minimum_gate_applies"])
        self.assertFalse(gate["operational_minimum_count_gate_applies"])
        self.assertEqual(gate["minimum_required_counts"]["llm_planner_call_count"], 30)
        self.assertEqual(gate["minimum_required_counts"]["web_search_task_count"], 20)
        self.assertEqual(gate["minimum_required_counts"]["web_search_call_count"], 20)
        self.assertEqual(gate["minimum_required_counts"]["web_fetched_document_count"], 10)
        self.assertEqual(gate["minimum_required_counts"]["llm_claim_extractor_attempt_count"], 10)
        self.assertEqual(gate["minimum_required_counts"]["web_or_llm_accepted_claim_count"], 3)
        self.assertFalse(gate["brain_web_evidence_pass_allowed"])
        self.assertEqual(gate["source_task_execution_count"], 0)
        self.assertEqual(gate["web_or_llm_accepted_claim_count"], 0)
        self.assertEqual(gate["blockers"], [])
        self.assertFalse(readiness["brain_web_evidence_pass"])
        self.assertEqual(readiness["brain_web_readiness_gate"]["verdict"], "NOT_REQUESTED")
        self.assertFalse(readiness["brain_web_readiness_gate"]["operational_minimum_count_gate_applies"])
        self.assertEqual(readiness["brain_web_readiness_gate"]["minimum_required_counts"], gate["minimum_required_counts"])
        self.assertEqual(readiness["full_thesis_seed_materialization_audit"]["verdict"], "PASS")
        self.assertEqual(readiness["full_thesis_seed_materialization_audit"]["verdict_scope"], "LEDGER_INTEGRITY_ONLY")
        self.assertEqual(readiness["full_thesis_seed_materialization_audit"]["status_counts"], {"PLANNER_NOT_RUN": 85})
        self.assertEqual(readiness["full_thesis_seed_materialization_audit"]["full_thesis_promoted_seed_count"], 0)
        self.assertFalse(readiness["full_thesis_seed_materialization_audit"]["full_thesis_seed_promotion_pass"])
        self.assertTrue(readiness["full_thesis_seed_materialization_audit"]["ledger_integrity_pass_allowed"])
        self.assertFalse(readiness["full_thesis_seed_materialization_audit"]["actual_materialization_pass_allowed"])
        self.assertEqual(readiness["full_thesis_seed_materialization_audit"]["critical_count"], 0)
        self.assertIn("FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS", readiness["labels"])
        self.assertIn("FULL_THESIS_SEED_LEDGER_INTEGRITY_PASS", readiness["labels"])
        self.assertIn("FULL_THESIS_SEED_ACTUAL_MATERIALIZATION_PENDING", readiness["labels"])
        self.assertIn("FULL_THESIS_SEED_PROMOTION_PENDING", readiness["labels"])
        self.assertNotIn("FULL_THESIS_SEED_PROMOTION_PASS", readiness["labels"])
        self.assertIn(
            "full-thesis seed materialization audit shows no promoted FULL_THESIS seed",
            readiness["remaining_operational_gaps"],
        )

    def test_enabled_without_real_provider_source_or_extractor_is_blocked(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp) / "out"
            result = run_census_mode_v4(
                CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(root),
                    v3_output_root="output/census_v3/2026-07-01",
                    run_mode="BRAIN_AND_WEB_ACQUISITION_ENABLED",
                    brain_web_mode="enabled",
                    brain_planner_provider="none",
                    fail_on_critical_audit=False,
                    write_operational_docs=False,
                )
            )
            gate = read_json(root / "brain_web_readiness_gate_audit.json")

        self.assertEqual(gate["verdict"], "BLOCKED")
        self.assertTrue(gate["minimum_gate_applies"])
        self.assertFalse(gate["brain_web_evidence_pass_allowed"])
        blockers = " ".join(gate["blockers"])
        self.assertIn("LLM planner real-provider success count is zero", blockers)
        self.assertIn("Brain/Web source task execution count is zero", blockers)
        self.assertIn("web/LLM accepted claim count is zero", blockers)
        self.assertIn("brain stage promotion verdict is not PROMOTION_APPLIED", blockers)
        self.assertEqual(result.readiness_verdict["brain_web_readiness_gate"]["verdict"], "BLOCKED")
        self.assertTrue(result.readiness_verdict["brain_web_readiness_gate"]["operational_minimum_count_gate_applies"])
        self.assertEqual(result.readiness_verdict["brain_web_readiness_gate"]["minimum_required_counts"]["llm_planner_call_count"], 30)
        self.assertFalse(result.readiness_verdict["brain_web_readiness_gate"]["brain_web_evidence_pass_allowed"])
        self.assertEqual(result.readiness_verdict["brain_web_readiness_gate"]["source_lineage_feedback_retry_execution_count"], 0)
        self.assertEqual(result.readiness_verdict["brain_web_readiness_gate"]["source_lineage_feedback_retry_accepted_execution_count"], 0)
        self.assertEqual(result.readiness_verdict["brain_web_readiness_gate"]["source_lineage_feedback_retry_no_evidence_execution_count"], 0)
        self.assertEqual(result.readiness_verdict["verdict"], "NOT_READY")

    def test_connected_brain_claim_trace_contribution_and_stage_can_pass_gate(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_brain_gate_fixture(root, claim_id="CLM-A", contribution_claim_id="CLM-A", stage_claim_id="CLM-A")
            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": 1,
                    "real_document_fetched_count": 1,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[{"stagecourt_trace_id": "SCT-BRAIN-A", "accepted_claim_ids": ["CLM-A"], "score_scale": "EVENT_WEIGHTED_PARTIAL"}],
            )

        self.assertEqual(gate["verdict"], "READY_FOR_BRAIN_WEB_EVIDENCE_PASS")
        self.assertTrue(gate["brain_web_evidence_pass_allowed"])
        self.assertEqual(gate["brain_trace_missing_accepted_claim_count"], 0)
        self.assertEqual(gate["brain_contribution_without_accepted_support_count"], 0)
        self.assertEqual(gate["brain_stage_trace_without_accepted_claim_count"], 0)
        self.assertEqual(gate["promoted_stage_without_brain_trace_count"], 0)
        self.assertEqual(gate["brain_claim_unresolved_document_ref_count"], 0)
        self.assertEqual(gate["brain_claim_unresolved_anchor_ref_count"], 0)
        self.assertEqual(gate["direct_accepted_claim_count"], 1)
        self.assertEqual(gate["rerouted_accepted_claim_count"], 0)
        self.assertEqual(gate["direct_source_task_satisfied_count"], 1)
        self.assertEqual(gate["rerouted_source_task_claim_count"], 0)
        self.assertEqual(gate["brain_accepted_claim_count"], 1)
        self.assertEqual(gate["web_or_llm_accepted_claim_count"], 1)
        self.assertEqual(gate["llm_extracted_accepted_claim_count"], 1)
        self.assertEqual(gate["official_accepted_claim_count"], 0)

    def test_source_family_deduped_brain_trace_without_score_contribution_is_not_blocker(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_brain_gate_fixture(root, claim_id="CLM-A", contribution_claim_id="CLM-A", stage_claim_id="CLM-A")
            accepted = _read_jsonl(root / "accepted_claims.jsonl")
            accepted.append(
                {
                    **accepted[0],
                    "claim_id": "CLM-B",
                }
            )
            write_jsonl(root / "accepted_claims.jsonl", accepted)
            traces = _read_jsonl(root / "brain_to_claim_trace.jsonl")
            traces.append(
                {
                    **traces[0],
                    "accepted_claim_id": "CLM-B",
                    "score_contribution_id": None,
                    "score_contribution_ids": [],
                    "score_support_status": "SOURCE_FAMILY_DEDUPED",
                    "score_deduped_by_source_family": True,
                    "trace_status": "SOURCE_FAMILY_DEDUPED",
                }
            )
            write_jsonl(root / "brain_to_claim_trace.jsonl", traces)
            stage_traces = _read_jsonl(root / "stagecourt_traces.jsonl")
            stage_traces[0]["accepted_claim_ids"] = ["CLM-A", "CLM-B"]
            write_jsonl(root / "stagecourt_traces.jsonl", stage_traces)

            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": 2,
                    "real_document_fetched_count": 1,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[{"stagecourt_trace_id": "SCT-BRAIN-A", "accepted_claim_ids": ["CLM-A", "CLM-B"], "score_scale": "EVENT_WEIGHTED_PARTIAL"}],
            )

        self.assertEqual(gate["brain_trace_missing_score_contribution_ref_count"], 0)
        self.assertNotIn("Brain/Web trace rows missing score_contribution_id", " ".join(gate["blockers"]))
        self.assertEqual(gate["verdict"], "READY_FOR_BRAIN_WEB_EVIDENCE_PASS")

    def test_non_representative_accepted_brain_trace_without_score_contribution_is_not_blocker(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_brain_gate_fixture(root, claim_id="CLM-A", contribution_claim_id="CLM-A", stage_claim_id="CLM-A")
            accepted = _read_jsonl(root / "accepted_claims.jsonl")
            accepted.append({**accepted[0], "claim_id": "CLM-B"})
            write_jsonl(root / "accepted_claims.jsonl", accepted)
            traces = _read_jsonl(root / "brain_to_claim_trace.jsonl")
            traces.append(
                {
                    **traces[0],
                    "accepted_claim_id": "CLM-B",
                    "score_contribution_id": None,
                    "score_contribution_ids": [],
                    "stagecourt_trace_id": None,
                    "score_support_status": "ACCEPTED_NON_REPRESENTATIVE_NOT_SCORE_CONTRIBUTING",
                    "representative_score_claim": False,
                    "trace_status": "ACCEPTED_NON_REPRESENTATIVE_NOT_SCORE_CONTRIBUTING",
                }
            )
            write_jsonl(root / "brain_to_claim_trace.jsonl", traces)

            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": 2,
                    "real_document_fetched_count": 1,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[{"stagecourt_trace_id": "SCT-BRAIN-A", "accepted_claim_ids": ["CLM-A"], "score_scale": "EVENT_WEIGHTED_PARTIAL"}],
            )

        self.assertEqual(gate["brain_trace_missing_score_contribution_ref_count"], 0)
        self.assertEqual(gate["brain_trace_missing_stagecourt_ref_count"], 0)
        self.assertEqual(gate["brain_trace_nonrepresentative_missing_stagecourt_ref_count"], 1)
        self.assertIn(
            "non-representative Brain/Web accepted claim traces without StageCourt refs: 1",
            gate["nonblocking_gaps"],
        )
        self.assertNotIn("Brain/Web trace rows missing score_contribution_id", " ".join(gate["blockers"]))
        self.assertNotIn("Brain/Web trace rows missing stagecourt_trace_id", " ".join(gate["blockers"]))
        self.assertEqual(gate["verdict"], "READY_FOR_BRAIN_WEB_EVIDENCE_PASS")

    def test_representative_brain_trace_without_stagecourt_is_blocker(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_brain_gate_fixture(root, claim_id="CLM-A", contribution_claim_id="CLM-A", stage_claim_id="CLM-A")
            traces = _read_jsonl(root / "brain_to_claim_trace.jsonl")
            traces[0]["stagecourt_trace_id"] = None
            write_jsonl(root / "brain_to_claim_trace.jsonl", traces)

            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": 1,
                    "real_document_fetched_count": 1,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[{"stagecourt_trace_id": "SCT-BRAIN-A", "accepted_claim_ids": ["CLM-A"], "score_scale": "EVENT_WEIGHTED_PARTIAL"}],
            )

        self.assertEqual(gate["brain_trace_missing_stagecourt_ref_count"], 1)
        self.assertIn("Brain/Web trace rows missing stagecourt_trace_id: 1", gate["blockers"])
        self.assertEqual(gate["verdict"], "BLOCKED")

    def test_score_supported_claim_marked_nonrepresentative_still_requires_stagecourt(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_brain_gate_fixture(root, claim_id="CLM-A", contribution_claim_id="CLM-A", stage_claim_id="CLM-A")
            traces = _read_jsonl(root / "brain_to_claim_trace.jsonl")
            traces[0]["score_contribution_id"] = None
            traces[0]["score_contribution_ids"] = []
            traces[0]["stagecourt_trace_id"] = None
            traces[0]["score_support_status"] = "ACCEPTED_NON_REPRESENTATIVE_NOT_SCORE_CONTRIBUTING"
            traces[0]["representative_score_claim"] = False
            traces[0]["trace_status"] = "ACCEPTED_NON_REPRESENTATIVE_NOT_SCORE_CONTRIBUTING"
            write_jsonl(root / "brain_to_claim_trace.jsonl", traces)

            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": 1,
                    "real_document_fetched_count": 1,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[{"stagecourt_trace_id": "SCT-BRAIN-A", "accepted_claim_ids": ["CLM-A"], "score_scale": "EVENT_WEIGHTED_PARTIAL"}],
            )

        self.assertEqual(gate["brain_trace_missing_score_contribution_ref_count"], 1)
        self.assertEqual(gate["brain_trace_missing_stagecourt_ref_count"], 1)
        self.assertEqual(gate["brain_trace_nonrepresentative_missing_stagecourt_ref_count"], 0)
        self.assertIn("Brain/Web trace rows missing score_contribution_id: 1", gate["blockers"])
        self.assertIn("Brain/Web trace rows missing stagecourt_trace_id: 1", gate["blockers"])
        self.assertEqual(gate["verdict"], "BLOCKED")

    def test_rule_fallback_extractor_claim_cannot_pass_as_llm_brain_web(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_brain_gate_fixture(
                root,
                claim_id="CLM-A",
                contribution_claim_id="CLM-A",
                stage_claim_id="CLM-A",
                extractor_provider_mode="rule_fallback",
            )
            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": 1,
                    "real_document_fetched_count": 1,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[{"stagecourt_trace_id": "SCT-BRAIN-A", "accepted_claim_ids": ["CLM-A"], "score_scale": "EVENT_WEIGHTED_PARTIAL"}],
            )

        self.assertEqual(gate["verdict"], "BLOCKED")
        self.assertFalse(gate["brain_web_evidence_pass_allowed"])
        self.assertEqual(gate["llm_claim_extractor_real_provider_count"], 0)
        self.assertEqual(gate["claim_extractor_non_llm_provider_count"], 1)
        self.assertIn("LLM claim extractor has no real LLM provider runs", " ".join(gate["blockers"]))

    def test_llm_claim_extractor_provider_error_blocks_brain_web_readiness(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_brain_gate_fixture(root, claim_id="CLM-A", contribution_claim_id="CLM-A", stage_claim_id="CLM-A")
            runs = _read_jsonl(root / "claim_extractor_runs.jsonl")
            runs[0]["status"] = "PROVIDER_FAILED"
            runs[0]["provider_error"] = "codex_cli_timeout:12s"
            runs[0]["timeout_seconds"] = 12.0
            write_jsonl(root / "claim_extractor_runs.jsonl", runs)
            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": 1,
                    "real_document_fetched_count": 1,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[{"stagecourt_trace_id": "SCT-BRAIN-A", "accepted_claim_ids": ["CLM-A"], "score_scale": "EVENT_WEIGHTED_PARTIAL"}],
            )

        self.assertEqual(gate["verdict"], "BLOCKED")
        self.assertFalse(gate["brain_web_evidence_pass_allowed"])
        self.assertEqual(gate["llm_claim_extractor_provider_error_count"], 1)
        self.assertEqual(gate["llm_claim_extractor_timeout_count"], 1)
        blockers = " ".join(gate["blockers"])
        self.assertIn("LLM claim extractor provider errors are unresolved: 1", blockers)
        self.assertIn("LLM claim extractor timeouts are unresolved: 1", blockers)

    def test_attempt_counts_without_exported_source_rows_are_blocked(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_jsonl(root / "planner_runs.jsonl", [{"planner_run_id": "PLAN-A", "provider_mode": "real", "real_provider_success": True}])
            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": 1,
                    "real_document_fetched_count": 1,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[{"stagecourt_trace_id": "SCT-BRAIN-A", "accepted_claim_ids": ["CLM-A"], "score_scale": "EVENT_WEIGHTED_PARTIAL"}],
            )

        self.assertEqual(gate["verdict"], "BLOCKED")
        self.assertFalse(gate["brain_web_evidence_pass_allowed"])
        self.assertEqual(gate["attempt_source_task_execution_count"], 1)
        self.assertEqual(gate["source_task_execution_count"], 0)
        self.assertEqual(gate["attempt_real_document_fetched_count"], 1)
        self.assertEqual(gate["real_document_fetched_count"], 0)
        self.assertEqual(gate["attempt_accepted_claim_count"], 1)
        self.assertEqual(gate["web_or_llm_accepted_claim_count"], 0)
        blockers = " ".join(gate["blockers"])
        self.assertIn("attempt count has no exported source_task_executions rows", blockers)
        self.assertIn("attempt count has no exported evidence_documents rows", blockers)
        self.assertIn("attempt count has no exported accepted_claims rows", blockers)

    def test_source_lineage_retry_drop_is_counted_in_readiness_gate(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_jsonl(root / "planner_runs.jsonl", [{"planner_run_id": "PLAN-A", "provider_mode": "real", "real_provider_success": True}])
            write_jsonl(
                root / "source_task_executions.jsonl",
                [
                    {
                        "task_id": "TASK-DROP-A",
                        "source_origin": "research_brain_v4_attempt",
                        "source_task_execution_origin": "research_brain_v4_attempt",
                        "status": "REJECTED_BY_POLICY",
                        "source_task": {
                            "task_id": "TASK-DROP-A",
                            "source_origin": "research_brain_v4_attempt",
                            "reason_from_memory": (
                                "feedback_retry:source_lineage_unverified_original;"
                                "dropped:source_lineage_retry_discovery_only_after_unverified_original"
                            ),
                        },
                        "not_eligible_reasons": ["source_lineage_retry_discovery_only_after_unverified_original"],
                        "provider_errors": ["source_lineage_retry_discovery_only_after_unverified_original"],
                        "budget_used": {"queries": 0, "candidates": 0, "fetches": 0},
                        "stop_reason": "source_lineage_retry_discovery_only_after_unverified_original",
                    }
                ],
            )
            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": 0,
                    "real_document_fetched_count": 0,
                },
                brain_stage_promotion={
                    "verdict": "BLOCKED",
                    "brain_promoted_stage_row_count": 0,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[],
            )

        self.assertEqual(gate["verdict"], "BLOCKED")
        self.assertEqual(gate["source_task_execution_count"], 1)
        self.assertEqual(gate["policy_rejected_source_task_execution_count"], 1)
        self.assertEqual(gate["zero_budget_policy_rejected_source_task_execution_count"], 1)
        self.assertEqual(gate["source_lineage_feedback_retry_execution_count"], 1)
        self.assertEqual(gate["source_lineage_feedback_retry_accepted_execution_count"], 0)
        self.assertEqual(gate["source_lineage_feedback_retry_no_evidence_execution_count"], 0)
        self.assertEqual(gate["source_lineage_feedback_retry_dropped_count"], 1)
        self.assertEqual(gate["discovery_only_retry_after_unverified_original_count"], 1)
        self.assertNotIn("attempt count has no exported source_task_executions rows", " ".join(gate["blockers"]))

    def test_source_lineage_good_retry_outcomes_are_counted_in_readiness_gate(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_brain_gate_fixture(root, claim_id="CLM-A", contribution_claim_id="CLM-A", stage_claim_id="CLM-A")
            executions = _read_jsonl(root / "source_task_executions.jsonl")
            executions[0]["reason_from_memory"] = "unit;feedback_retry:source_lineage_unverified_original"
            executions[0]["source_task"] = {
                "task_id": "TASK-A",
                "reason_from_memory": "unit;feedback_retry:source_lineage_unverified_original",
            }
            executions.append(
                {
                    "task_id": "TASK-LINEAGE-NO-EVIDENCE",
                    "source_origin": "research_brain_v4_attempt",
                    "status": "NO_EVIDENCE_FOUND",
                    "source_task": {
                        "task_id": "TASK-LINEAGE-NO-EVIDENCE",
                        "reason_from_memory": "unit;feedback_retry:source_lineage_unverified_original",
                    },
                    "accepted_claim_ids": [],
                    "fetched_document_ids": [],
                    "budget_used": {"queries": 1, "candidates": 1, "fetches": 0},
                    "stop_reason": "unit_retry_no_evidence",
                }
            )
            write_jsonl(root / "source_task_executions.jsonl", executions)

            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 2,
                    "accepted_claim_count": 1,
                    "real_document_fetched_count": 1,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[{"stagecourt_trace_id": "SCT-BRAIN-A", "accepted_claim_ids": ["CLM-A"], "score_scale": "EVENT_WEIGHTED_PARTIAL"}],
            )

        self.assertEqual(gate["verdict"], "READY_FOR_BRAIN_WEB_EVIDENCE_PASS")
        self.assertEqual(gate["source_lineage_feedback_retry_execution_count"], 2)
        self.assertEqual(gate["source_lineage_feedback_retry_accepted_execution_count"], 1)
        self.assertEqual(gate["source_lineage_feedback_retry_no_evidence_execution_count"], 1)
        self.assertEqual(gate["source_lineage_feedback_retry_dropped_count"], 0)

    def test_brain_claim_missing_document_or_anchor_row_is_blocked(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_brain_gate_fixture(root, claim_id="CLM-A", contribution_claim_id="CLM-A", stage_claim_id="CLM-A", write_anchor=False)
            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": 1,
                    "real_document_fetched_count": 1,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[{"stagecourt_trace_id": "SCT-BRAIN-A", "accepted_claim_ids": ["CLM-A"], "score_scale": "EVENT_WEIGHTED_PARTIAL"}],
            )

        self.assertEqual(gate["verdict"], "BLOCKED")
        self.assertFalse(gate["brain_web_evidence_pass_allowed"])
        self.assertEqual(gate["brain_claim_unresolved_anchor_ref_count"], 1)
        self.assertIn("accepted Brain/Web claims reference missing evidence_anchors rows", " ".join(gate["blockers"]))

    def test_brain_claim_score_ineligible_is_blocked(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_brain_gate_fixture(
                root,
                claim_id="CLM-A",
                contribution_claim_id="CLM-A",
                stage_claim_id="CLM-A",
                score_eligible=False,
            )
            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": 1,
                    "real_document_fetched_count": 1,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[{"stagecourt_trace_id": "SCT-BRAIN-A", "accepted_claim_ids": ["CLM-A"], "score_scale": "EVENT_WEIGHTED_PARTIAL"}],
            )

        self.assertEqual(gate["verdict"], "BLOCKED")
        self.assertFalse(gate["brain_web_evidence_pass_allowed"])
        self.assertEqual(gate["brain_claim_score_ineligible_count"], 1)
        self.assertIn("accepted Brain/Web claims are not score eligible by deterministic guard", " ".join(gate["blockers"]))

    def test_brain_and_web_acquisition_mode_requires_web_task_and_fetched_document(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_brain_gate_fixture(root, claim_id="CLM-A", contribution_claim_id="CLM-A", stage_claim_id="CLM-A")
            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    run_mode="BRAIN_AND_WEB_ACQUISITION_ENABLED",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": 1,
                    "real_document_fetched_count": 1,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[{"stagecourt_trace_id": "SCT-BRAIN-A", "accepted_claim_ids": ["CLM-A"], "score_scale": "EVENT_WEIGHTED_PARTIAL"}],
            )

        self.assertEqual(gate["verdict"], "BLOCKED")
        self.assertFalse(gate["brain_web_evidence_pass_allowed"])
        blockers = " ".join(gate["blockers"])
        self.assertIn("requires web/news search task rows", blockers)
        self.assertIn("requires fetched full-source web/news documents", blockers)

    def test_production_brain_web_mode_blocks_below_operational_minimum_counts(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_brain_gate_fixture(root, claim_id="CLM-A", contribution_claim_id="CLM-A", stage_claim_id="CLM-A")
            write_jsonl(
                root / "web_search_tasks.jsonl",
                [{"web_task_id": "WEBTASK-A", "provider_name": "NaverSearch", "search_call_executed": True, "status": "SEARCH_EXECUTED"}],
            )
            write_jsonl(
                root / "web_search_results.jsonl",
                [{"web_result_id": "WEBRESULT-A", "web_task_id": "WEBTASK-A", "provider_name": "NaverSearch"}],
            )
            write_jsonl(root / "web_fetched_documents.jsonl", [{"web_document_id": "WEBDOC-A", "web_task_id": "WEBTASK-A"}])
            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    run_mode="BRAIN_AND_WEB_ACQUISITION_ENABLED",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": 1,
                    "real_document_fetched_count": 1,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[{"stagecourt_trace_id": "SCT-BRAIN-A", "accepted_claim_ids": ["CLM-A"], "score_scale": "EVENT_WEIGHTED_PARTIAL"}],
            )

        self.assertEqual(gate["verdict"], "BLOCKED")
        self.assertTrue(gate["operational_minimum_count_gate_applies"])
        self.assertFalse(gate["brain_web_evidence_pass_allowed"])
        blockers = " ".join(gate["blockers"])
        self.assertIn("operational minimum planner runs not met: 1/30", blockers)
        self.assertIn("operational minimum web search tasks not met: 1/20", blockers)
        self.assertIn("operational minimum web/news search calls not met: 1/20", blockers)
        self.assertIn("operational minimum fetched documents not met: 1/10", blockers)
        self.assertIn("operational minimum claim extractor attempts not met: 1/10", blockers)
        self.assertIn("operational minimum web/LLM accepted claims not met: 1/3", blockers)

    def test_production_brain_web_mode_can_pass_when_operational_minimum_counts_are_met(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_brain_gate_operational_minimum_fixture(root)
            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    run_mode="BRAIN_AND_WEB_ACQUISITION_ENABLED",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 30,
                    "source_task_execution_count": 3,
                    "accepted_claim_count": 3,
                    "real_document_fetched_count": 3,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[
                    {
                        "stagecourt_trace_id": "SCT-BRAIN-A",
                        "accepted_claim_ids": ["CLM-1", "CLM-2", "CLM-3"],
                        "score_scale": "EVENT_WEIGHTED_PARTIAL",
                    }
                ],
            )

        self.assertEqual(gate["verdict"], "READY_FOR_BRAIN_WEB_EVIDENCE_PASS")
        self.assertTrue(gate["operational_minimum_count_gate_applies"])
        self.assertTrue(gate["brain_web_evidence_pass_allowed"])
        self.assertEqual(gate["minimum_required_counts"]["llm_planner_call_count"], 30)
        self.assertEqual(gate["web_search_task_count"], 20)
        self.assertEqual(gate["web_search_call_count"], 20)
        self.assertEqual(gate["web_fetched_document_count"], 10)
        self.assertEqual(gate["llm_claim_extractor_attempt_count"], 10)
        self.assertEqual(gate["web_or_llm_accepted_claim_count"], 3)
        self.assertEqual(gate["brain_accepted_claim_count"], 3)
        self.assertEqual(gate["llm_extracted_accepted_claim_count"], 3)
        self.assertEqual(gate["web_news_accepted_claim_count"], 3)
        self.assertEqual(gate["official_accepted_claim_count"], 0)

    def test_official_only_brain_claim_does_not_count_as_web_or_llm_accepted_claim(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_brain_gate_fixture(
                root,
                claim_id="CLM-DART",
                contribution_claim_id="CLM-DART",
                stage_claim_id="CLM-DART",
                source_provider="OpenDART",
                raw_assertion_id="RAWPROD-DART",
            )
            write_jsonl(
                root / "web_search_tasks.jsonl",
                [{"web_task_id": "WEBTASK-A", "provider_name": "NaverSearch", "search_call_executed": True, "status": "SEARCH_EXECUTED"}],
            )
            write_jsonl(root / "web_search_results.jsonl", [{"web_result_id": "WEBRESULT-A", "web_task_id": "WEBTASK-A"}])
            write_jsonl(root / "web_fetched_documents.jsonl", [{"document_id": "DOC-WEB", "web_task_id": "WEBTASK-A"}])
            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    run_mode="BRAIN_AND_WEB_ACQUISITION_ENABLED",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": 1,
                    "real_document_fetched_count": 1,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[{"stagecourt_trace_id": "SCT-BRAIN-A", "accepted_claim_ids": ["CLM-DART"], "score_scale": "EVENT_WEIGHTED_PARTIAL"}],
            )

        self.assertEqual(gate["brain_accepted_claim_count"], 1)
        self.assertEqual(gate["official_accepted_claim_count"], 1)
        self.assertEqual(gate["web_or_llm_accepted_claim_count"], 0)
        self.assertEqual(gate["web_news_accepted_claim_count"], 0)
        self.assertEqual(gate["llm_extracted_accepted_claim_count"], 0)
        self.assertEqual(gate["verdict"], "BLOCKED")
        self.assertIn("web/LLM accepted claim count is zero", " ".join(gate["blockers"]))

    def test_count_only_brain_artifacts_with_mismatched_ids_are_blocked(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_brain_gate_fixture(root, claim_id="CLM-A", trace_claim_id="CLM-B", contribution_claim_id="CLM-C", stage_claim_id="CLM-D")
            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 1,
                    "accepted_claim_count": 1,
                    "real_document_fetched_count": 1,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[{"stagecourt_trace_id": "SCT-BRAIN-A", "accepted_claim_ids": ["CLM-E"], "score_scale": "EVENT_WEIGHTED_PARTIAL"}],
            )

        self.assertEqual(gate["verdict"], "BLOCKED")
        self.assertFalse(gate["brain_web_evidence_pass_allowed"])
        blockers = " ".join(gate["blockers"])
        self.assertIn("accepted Brain/Web claims missing from brain_to_claim_trace", blockers)
        self.assertIn("Brain/Web score contributions do not support accepted Brain/Web claims", blockers)
        self.assertIn("Brain/Web StageCourt traces do not carry accepted Brain/Web claims", blockers)
        self.assertIn("promoted Brain/Web stage rows are not connected", blockers)

    def test_provider_failed_non_claim_task_does_not_block_brain_web_readiness(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_brain_gate_fixture(root, claim_id="CLM-A", contribution_claim_id="CLM-A", stage_claim_id="CLM-A")
            executions = _read_jsonl(root / "source_task_executions.jsonl")
            executions.append(
                {
                    "task_id": "TASK-IR-PENDING",
                    "source_origin": "research_brain_v4_attempt",
                    "status": "PROVIDER_FAILED",
                    "accepted_claim_ids": [],
                    "fetched_document_ids": [],
                    "stop_reason": "live_official_no_fetchable_document",
                }
            )
            write_jsonl(root / "source_task_executions.jsonl", executions)

            gate = _brain_web_readiness_gate_audit(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    brain_web_mode="enabled",
                    brain_planner_provider="real",
                    brain_stage_promotion_mode="strict",
                ),
                output_root=root,
                brain_web_attempt={
                    "real_provider_success_count": 1,
                    "source_task_execution_count": 2,
                    "accepted_claim_count": 1,
                    "real_document_fetched_count": 1,
                },
                brain_stage_promotion={
                    "verdict": "PROMOTION_APPLIED",
                    "brain_promoted_stage_row_count": 1,
                    "unsafe_promoted_stage_row_count": 0,
                    "brain_snapshot_document_count": 0,
                    "fake_provider_used_count": 0,
                },
                stage_rows=[{"stagecourt_trace_id": "SCT-BRAIN-A", "accepted_claim_ids": ["CLM-A"], "score_scale": "EVENT_WEIGHTED_PARTIAL"}],
            )

        self.assertEqual(gate["verdict"], "READY_FOR_BRAIN_WEB_EVIDENCE_PASS")
        self.assertTrue(gate["brain_web_evidence_pass_allowed"])
        self.assertEqual(gate["brain_source_task_without_document_ref_count"], 0)
        self.assertNotIn("Brain/Web source task rows missing fetched document refs: 1", gate["blockers"])


def _write_brain_gate_fixture(
    root: Path,
    *,
    claim_id: str,
    trace_claim_id: str | None = None,
    contribution_claim_id: str,
    stage_claim_id: str,
    write_anchor: bool = True,
    score_eligible: bool = True,
    extractor_provider_mode: str = "llm",
    source_provider: str = "NaverSearch",
    raw_assertion_id: str | None = None,
) -> None:
    trace_claim_id = trace_claim_id or claim_id
    raw_assertion_id = raw_assertion_id or ("RAWLLM-A" if extractor_provider_mode == "llm" else "RAWRULE-A")
    extractor_raw_ids = [raw_assertion_id] if extractor_provider_mode == "llm" and raw_assertion_id.startswith("RAWLLM-") else []
    write_jsonl(root / "planner_runs.jsonl", [{"planner_run_id": "PLAN-A", "provider_mode": "real", "real_provider_success": True}])
    write_jsonl(
        root / "claim_extractor_runs.jsonl",
        [
            {
                "claim_extractor_run_id": "EXT-A",
                "source_origin": "research_brain_v4_attempt",
                "provider_mode": extractor_provider_mode,
                "provider_name": "unit_llm_extractor",
                "forbidden_context_seen": [],
                "raw_assertion_ids": extractor_raw_ids,
            }
        ],
    )
    write_jsonl(
        root / "source_task_executions.jsonl",
        [
            {
                "task_id": "TASK-A",
                "source_origin": "research_brain_v4_attempt",
                "status": "EVIDENCE_OS_ACCEPTED",
                "accepted_claim_ids": [claim_id],
                "fetched_document_ids": ["DOC-A"],
                "satisfies_source_task": True,
                "satisfaction_type": "DIRECT_ACCEPTED_CLAIM",
                "direct_accepted_claim_ids": [claim_id],
                "rerouted_accepted_claim_ids": [],
            }
        ],
    )
    write_jsonl(root / "evidence_documents.jsonl", [{"document_id": "DOC-A", "source_origin": "research_brain_v4_attempt", "canonical_url": "https://example.com/doc"}])
    write_jsonl(
        root / "evidence_anchors.jsonl",
        [{"anchor_id": "ANCH-A", "document_id": "DOC-A", "source_origin": "research_brain_v4_attempt", "anchor_type": "TEXT_SPAN"}]
        if write_anchor
        else [],
    )
    write_jsonl(
        root / "accepted_claims.jsonl",
        [
            {
                "claim_id": claim_id,
                "brain_web_claim": True,
                "source_origin": "research_brain_v4_attempt",
                "document_id": "DOC-A",
                "anchor_id": "ANCH-A",
                "raw_assertion_id": raw_assertion_id,
                "source_provider": source_provider,
                "event_date": "2026-06-30",
                "target_scope_status": "DIRECT",
                "temporal_status": "CURRENT",
                "score_eligible": score_eligible,
            }
        ],
    )
    write_jsonl(root / "score_contributions.jsonl", [{"score_contribution_id": "SCON-A", "source_origin": "research_brain_v4_attempt", "support_claim_ids": [contribution_claim_id]}])
    write_jsonl(
        root / "stagecourt_traces.jsonl",
        [
            {
                "stagecourt_trace_id": "SCT-BRAIN-A",
                "trace_id": "SCT-BRAIN-A",
                "source_origin": "research_brain_v4_attempt",
                "accepted_claim_ids": [stage_claim_id],
                "score_contribution_ids": ["SCON-A"],
            }
        ],
    )
    write_jsonl(
        root / "brain_to_claim_trace.jsonl",
        [
            {
                "schema_version": "e2r_census_v4_brain_to_claim_trace_v1",
                "accepted_claim_id": trace_claim_id,
                "score_contribution_id": "SCON-A",
                "score_contribution_ids": ["SCON-A"],
                "stagecourt_trace_id": "SCT-BRAIN-A",
                "source_origin": "research_brain_v4_attempt",
                "satisfies_source_task": True,
                "satisfaction_type": "DIRECT_ACCEPTED_CLAIM",
            }
        ],
    )
    write_jsonl(root / "web_search_tasks.jsonl", [])
    write_jsonl(root / "web_search_results.jsonl", [])
    write_jsonl(root / "web_fetched_documents.jsonl", [])


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _write_brain_gate_operational_minimum_fixture(root: Path) -> None:
    claim_ids = ["CLM-1", "CLM-2", "CLM-3"]
    write_jsonl(
        root / "planner_runs.jsonl",
        [{"planner_run_id": f"PLAN-{idx}", "provider_mode": "real", "real_provider_success": True} for idx in range(1, 31)],
    )
    write_jsonl(
        root / "claim_extractor_runs.jsonl",
        [
            {
                "claim_extractor_run_id": f"EXT-{idx}",
                "source_origin": "research_brain_v4_attempt",
                "provider_mode": "llm",
                "provider_name": "unit_llm_extractor",
                "forbidden_context_seen": [],
                "raw_assertion_ids": [f"RAWLLM-{idx}"] if idx <= 3 else [],
            }
            for idx in range(1, 11)
        ],
    )
    write_jsonl(
        root / "web_search_tasks.jsonl",
        [
            {
                "web_task_id": f"WEBTASK-{idx}",
                "provider_name": "NaverSearch",
                "search_call_executed": True,
                "status": "SEARCH_EXECUTED",
            }
            for idx in range(1, 21)
        ],
    )
    write_jsonl(
        root / "web_search_results.jsonl",
        [
            {
                "web_result_id": f"WEBRESULT-{idx}",
                "web_task_id": f"WEBTASK-{idx}",
                "provider_name": "NaverSearch",
            }
            for idx in range(1, 21)
        ],
    )
    write_jsonl(
        root / "web_fetched_documents.jsonl",
        [{"web_document_id": f"WEBDOC-{idx}", "document_id": f"DOC-{idx}", "web_task_id": f"WEBTASK-{idx}"} for idx in range(1, 11)],
    )
    write_jsonl(
        root / "source_task_executions.jsonl",
        [
            {
                "task_id": f"TASK-{idx}",
                "source_origin": "research_brain_v4_attempt",
                "status": "EVIDENCE_OS_ACCEPTED",
                "accepted_claim_ids": [claim_id],
                "fetched_document_ids": [f"DOC-{idx}"],
                "satisfies_source_task": True,
                "satisfaction_type": "DIRECT_ACCEPTED_CLAIM",
                "direct_accepted_claim_ids": [claim_id],
                "rerouted_accepted_claim_ids": [],
            }
            for idx, claim_id in enumerate(claim_ids, 1)
        ],
    )
    write_jsonl(
        root / "evidence_documents.jsonl",
        [
            {
                "document_id": f"DOC-{idx}",
                "source_origin": "research_brain_v4_attempt",
                "canonical_url": f"https://example.com/doc-{idx}",
            }
            for idx in range(1, 4)
        ],
    )
    write_jsonl(
        root / "evidence_anchors.jsonl",
        [
            {
                "anchor_id": f"ANCH-{idx}",
                "document_id": f"DOC-{idx}",
                "source_origin": "research_brain_v4_attempt",
                "anchor_type": "TEXT_SPAN",
            }
            for idx in range(1, 4)
        ],
    )
    write_jsonl(
        root / "accepted_claims.jsonl",
        [
            {
                "claim_id": claim_id,
                "brain_web_claim": True,
                "source_origin": "research_brain_v4_attempt",
                "document_id": f"DOC-{idx}",
                "anchor_id": f"ANCH-{idx}",
                "raw_assertion_id": f"RAWLLM-{idx}",
                "source_provider": "NaverSearch",
                "event_date": "2026-06-30",
                "target_scope_status": "DIRECT",
                "temporal_status": "CURRENT",
                "score_eligible": True,
            }
            for idx, claim_id in enumerate(claim_ids, 1)
        ],
    )
    write_jsonl(
        root / "score_contributions.jsonl",
        [
            {
                "score_contribution_id": f"SCON-{idx}",
                "source_origin": "research_brain_v4_attempt",
                "support_claim_ids": [claim_id],
            }
            for idx, claim_id in enumerate(claim_ids, 1)
        ],
    )
    write_jsonl(
        root / "stagecourt_traces.jsonl",
        [
            {
                "stagecourt_trace_id": "SCT-BRAIN-A",
                "trace_id": "SCT-BRAIN-A",
                "source_origin": "research_brain_v4_attempt",
                "accepted_claim_ids": claim_ids,
                "score_contribution_ids": ["SCON-1", "SCON-2", "SCON-3"],
            }
        ],
    )
    write_jsonl(
        root / "brain_to_claim_trace.jsonl",
        [
            {
                "schema_version": "e2r_census_v4_brain_to_claim_trace_v1",
                "accepted_claim_id": claim_id,
                "score_contribution_id": f"SCON-{idx}",
                "score_contribution_ids": [f"SCON-{idx}"],
                "stagecourt_trace_id": "SCT-BRAIN-A",
                "source_origin": "research_brain_v4_attempt",
                "satisfies_source_task": True,
                "satisfaction_type": "DIRECT_ACCEPTED_CLAIM",
            }
            for idx, claim_id in enumerate(claim_ids, 1)
        ],
    )


if __name__ == "__main__":
    unittest.main()
