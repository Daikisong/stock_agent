import json
import tempfile
import unittest
from pathlib import Path

from e2r.census.census_runner_v4 import CensusV4RunConfig, _self_repair_log_v4, run_census_mode_v4
from e2r.census.test_result_evidence import TEST_RESULT_ARTIFACT_SCHEMA
from tests.census_v4_test_helpers import census_v4_artifacts, read_json


class CensusV4GoalRequiredAuditsTests(unittest.TestCase):
    def test_self_repair_treats_live_source_pass_verdict_as_resolved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "brain_web_readiness_gate_audit.json").write_text(
                json.dumps({"brain_web_evidence_pass_allowed": True}, ensure_ascii=False),
                encoding="utf-8",
            )
            log = _self_repair_log_v4(
                config=CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(root),
                    target_gate="meaningful",
                ),
                audits={
                    "known_bad_regression_report": {"completion_eligible": True, "status": "PASS", "failed_case_count": 0},
                    "test_result_evidence": {"completion_eligible": True},
                    "claim_to_stage_forensic": {"verdict": "PASS", "critical_count": 0},
                    "source_task_realness": {"verdict": "LIVE_SOURCE_PASS", "live_source_pass_allowed": True},
                    "runtime_plausibility": {"verdict": "PASS_LIVE_RUNTIME_PLAUSIBILITY", "runtime_mode": "HYBRID_CENSUS"},
                    "samsung_hynix_full_thesis_smoke": {
                        "verdict": "PENDING_FULL_THESIS_REFRESH",
                        "full_thesis_smoke_honesty_pass_allowed": True,
                    },
                },
            )

        self.assertEqual(log["unresolved_failures"], [])
        self.assertTrue(log["completion_eligible"])
        self.assertIn("SOURCE_TASK_REALNESS_AUDIT_FAILED", log["resolved_failures"])
        self.assertIn("full_thesis_smoke_pending", log["deferred_goal_blockers"])
        self.assertIn("full_thesis_smoke_execution_pending", log["deferred_goal_blockers"])
        self.assertIn("full_thesis_smoke_honesty_false", log["deferred_goal_blockers"])
        self.assertIn("full_thesis_production_pass_false", log["deferred_goal_blockers"])
        self.assertIn("source_connector_capability_pending", log["deferred_goal_blockers"])
        self.assertIn("source_backed_replay_parity_all_archetypes_pending", log["deferred_goal_blockers"])
        self.assertIn("controlled_semantic_replay_pending", log["deferred_goal_blockers"])

    def test_goal_required_runtime_audit_files_exist_and_pass_honesty_gates(self):
        root = census_v4_artifacts()["output_root"]
        expected = {
            "claim_to_stage_forensic_audit.json",
            "source_task_realness_audit.json",
            "source_connector_capability_audit.json",
            "existing_ledger_reuse_audit.json",
            "last_effective_thesis_audit.json",
            "source_coverage_audit.json",
            "runtime_plausibility_audit.json",
            "brain_web_readiness_gate_audit.json",
            "brain_claim_mapping_trace.jsonl",
            "non_representative_claim_audit.json",
            "source_task_satisfaction_audit.json",
            "primitive_state_chain_audit.json",
            "primitive_mappings.jsonl",
            "official_event_counter_audit.json",
            "samsung_hynix_full_thesis_smoke.json",
            "full_thesis_production_runner_audit.json",
            "full_thesis_production_audit.json",
            "full_thesis_seed_materialization_audit.json",
            "full_thesis_refresh_queue.jsonl",
            "full_thesis_refresh_queue_audit.json",
            "c06_guard_replay_audit.json",
            "c06_source_backed_semantic_replay.json",
            "c08_source_backed_semantic_replay.json",
            "c15_source_backed_semantic_replay.json",
            "c17_source_backed_semantic_replay.json",
            "c24_source_backed_semantic_replay.json",
            "c28_source_backed_semantic_replay.json",
            "controlled_semantic_replay_audit.json",
            "web_naver_acquisition_audit.json",
            "llm_claim_extraction_audit.json",
            "known_bad_regression_report.json",
            "self_repair_log.json",
            "test_result_evidence_audit.json",
            "goal_requirement_matrix_audit.json",
            "goal_completion_audit.json",
            "report_generation_audit.json",
        }
        for name in expected:
            self.assertTrue((root / name).exists(), name)

        forensic = read_json(root / "claim_to_stage_forensic_audit.json")
        realness = read_json(root / "source_task_realness_audit.json")
        connector_capability = read_json(root / "source_connector_capability_audit.json")
        reuse = read_json(root / "existing_ledger_reuse_audit.json")
        thesis = read_json(root / "last_effective_thesis_audit.json")
        coverage = read_json(root / "source_coverage_audit.json")
        runtime = read_json(root / "runtime_plausibility_audit.json")
        brain_gate = read_json(root / "brain_web_readiness_gate_audit.json")
        non_representative = read_json(root / "non_representative_claim_audit.json")
        source_satisfaction = read_json(root / "source_task_satisfaction_audit.json")
        primitive_chain = read_json(root / "primitive_state_chain_audit.json")
        known_bad = read_json(root / "known_bad_regression_report.json")
        full_thesis_production = read_json(root / "full_thesis_production_audit.json")
        full_thesis_seed_materialization = read_json(root / "full_thesis_seed_materialization_audit.json")
        full_thesis_refresh_queue_audit = read_json(root / "full_thesis_refresh_queue_audit.json")
        c06_guard = read_json(root / "c06_guard_replay_audit.json")
        c06_source_replay = read_json(root / "c06_source_backed_semantic_replay.json")
        c08_source_replay = read_json(root / "c08_source_backed_semantic_replay.json")
        c15_source_replay = read_json(root / "c15_source_backed_semantic_replay.json")
        c17_source_replay = read_json(root / "c17_source_backed_semantic_replay.json")
        c24_source_replay = read_json(root / "c24_source_backed_semantic_replay.json")
        c28_source_replay = read_json(root / "c28_source_backed_semantic_replay.json")
        controlled_semantic_replay = read_json(root / "controlled_semantic_replay_audit.json")
        self_repair = read_json(root / "self_repair_log.json")
        test_evidence = read_json(root / "test_result_evidence_audit.json")
        goal_matrix = read_json(root / "goal_requirement_matrix_audit.json")
        goal_completion = read_json(root / "goal_completion_audit.json")
        report_generation = read_json(root / "report_generation_audit.json")

        self.assertEqual(forensic["verdict"], "PASS")
        self.assertEqual(forensic["critical_count"], 0)
        self.assertEqual(realness["verdict"], "PASS_LEDGER_REFRESH_REALNESS")
        self.assertEqual(realness["verdict_scope"], "LEDGER_REFRESH_REALNESS_PASS")
        self.assertFalse(realness["live_source_pass_allowed"])
        self.assertGreater(realness["source_task_claim_producing_count"], 0)
        self.assertEqual(realness["source_task_real_fetch_count"], 0)
        self.assertGreater(realness["source_task_fresh_provider_cache_count"], 0)
        self.assertEqual(connector_capability["verdict"], "SOURCE_CONNECTOR_CAPABILITY_PASS")
        self.assertTrue(connector_capability["source_connector_capability_pass_allowed"])
        self.assertGreater(connector_capability["full_thesis_required_source_class_count"], 0)
        self.assertEqual(connector_capability["blocking_full_thesis_source_class_count"], 0)
        self.assertEqual(connector_capability["blocking_full_thesis_task_count"], 0)
        self.assertTrue(connector_capability["full_thesis_task_executable_source_path_pass_allowed"])
        self.assertGreater(connector_capability["full_thesis_task_with_blocking_source_class_count"], 0)
        self.assertIn("IssuerIR", connector_capability["placeholder_source_classes"])
        self.assertNotIn("TrustedNews", connector_capability["placeholder_source_classes"])
        self.assertIn("IssuerIR", connector_capability["non_executable_full_thesis_source_classes"])
        self.assertNotIn("TrustedNews", connector_capability["non_executable_full_thesis_source_classes"])
        self.assertIn("TrustedNews", connector_capability["bounded_web_acquisition_source_classes"])
        self.assertIn("IssuerOfficial", connector_capability["missing_connector_source_classes"])
        self.assertIn("ReportPDF", connector_capability["registry_missing_but_acquisition_covered_source_classes"])
        self.assertIn("BrokerReportPublicPDF", connector_capability["registry_missing_but_acquisition_covered_source_classes"])
        self.assertIn("CompanyNewsroom", connector_capability["registry_missing_but_acquisition_covered_source_classes"])
        self.assertIn("NaverSearch", connector_capability["bounded_web_acquisition_source_classes"])
        self.assertIn("GeneralWebSearch", connector_capability["bounded_web_acquisition_source_classes"])
        self.assertNotIn("ReportPDF", connector_capability["missing_connector_source_classes"])
        self.assertNotIn("CompanyNewsroom", connector_capability["missing_connector_source_classes"])
        self.assertEqual(
            {
                row["canonical_source_class"]: row["capability_status"]
                for row in connector_capability["source_classes"]
                if row["canonical_source_class"] in {"CompanyNewsroom", "ReportPDF", "NaverSearch"}
            },
            {
                "CompanyNewsroom": "BOUNDED_WEB_VERIFIED_ISSUER_ORIGINAL_IMPLEMENTED",
                "ReportPDF": "BOUNDED_WEB_VERIFIED_REPORT_ORIGINAL_IMPLEMENTED",
                "NaverSearch": "BOUNDED_WEB_SEARCH_FETCH_IMPLEMENTED",
            },
        )
        self.assertEqual(reuse["verdict"], "PASS")
        self.assertEqual(reuse["reused_claim_count"], reuse["lifecycle_refreshed_reused_claim_count"])
        self.assertEqual(thesis["verdict"], "PASS")
        self.assertEqual(thesis["last_effective_thesis_count"], thesis["source_timeline_count"])
        self.assertEqual(coverage["verdict"], "PASS_LEDGER_REFRESH_COVERAGE")
        self.assertFalse(coverage["operational_live_source_coverage_pass"])
        self.assertGreater(coverage["cutover_replay_only_symbol_count"], 0)
        self.assertEqual(runtime["verdict"], "PASS_LEDGER_REFRESH_RUNTIME_HONESTY")
        self.assertEqual(runtime["runtime_mode"], "LEDGER_REFRESH")
        self.assertEqual(runtime["llm_call_count"], 0)
        self.assertEqual(brain_gate["verdict"], "NOT_REQUESTED")
        self.assertFalse(brain_gate["minimum_gate_applies"])
        self.assertFalse(brain_gate["operational_minimum_count_gate_applies"])
        self.assertEqual(brain_gate["minimum_required_counts"]["llm_planner_call_count"], 30)
        self.assertEqual(brain_gate["minimum_required_counts"]["web_search_task_count"], 20)
        self.assertEqual(brain_gate["minimum_required_counts"]["web_search_call_count"], 20)
        self.assertEqual(brain_gate["minimum_required_counts"]["web_fetched_document_count"], 10)
        self.assertEqual(brain_gate["minimum_required_counts"]["llm_claim_extractor_attempt_count"], 10)
        self.assertEqual(brain_gate["minimum_required_counts"]["web_or_llm_accepted_claim_count"], 3)
        self.assertFalse(brain_gate["brain_web_evidence_pass_allowed"])
        self.assertEqual(brain_gate["blockers"], [])
        self.assertEqual(non_representative["verdict"], "PASS")
        self.assertEqual(non_representative["critical_count"], 0)
        self.assertGreater(non_representative["accepted_claim_count"], 0)
        self.assertGreater(non_representative["representative_stage_claim_count"], 0)
        self.assertEqual(
            non_representative["accepted_claim_count"],
            non_representative["representative_stage_claim_count"] + non_representative["non_representative_claim_count"],
        )
        self.assertEqual(non_representative["critical_counts"]["non_representative_claim_score_leak_count"], 0)
        self.assertEqual(source_satisfaction["verdict"], "PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION")
        self.assertEqual(source_satisfaction["verdict_scope"], "LEDGER_REFRESH_SOURCE_TASK_SATISFACTION_PASS")
        self.assertFalse(source_satisfaction["live_source_task_satisfaction_pass_allowed"])
        self.assertGreater(source_satisfaction["baseline_only_score_claim_count"], 0)
        self.assertGreater(source_satisfaction["representative_score_claim_count"], 0)
        self.assertEqual(
            source_satisfaction["source_task_chain_closed_to_representative_stage_count"],
            source_satisfaction["representative_score_claim_count"],
        )
        self.assertEqual(primitive_chain["verdict"], "PASS")
        self.assertEqual(primitive_chain["critical_count"], 0)
        self.assertGreater(primitive_chain["primitive_mapping_count"], 0)
        self.assertEqual(
            primitive_chain["representative_score_claim_with_primitive_state_count"],
            primitive_chain["representative_score_claim_count"],
        )
        self.assertTrue(primitive_chain["mapping_leaf_resolution_supported"])
        self.assertEqual(known_bad["status"], "PASS")
        self.assertTrue(known_bad["completion_eligible"])
        self.assertGreaterEqual(known_bad["case_count"], 8)
        self.assertEqual(known_bad["failed_case_count"], 0)
        self.assertEqual(full_thesis_production["verdict"], "PENDING_FULL_THESIS_PRODUCTION")
        self.assertFalse(full_thesis_production["production_pass_allowed"])
        self.assertEqual(full_thesis_production["production_full_thesis_row_count"], 0)
        self.assertTrue(full_thesis_production["production_runner_implemented"])
        self.assertIn("production_full_thesis_not_requested_or_no_rows", full_thesis_production["blockers"])
        self.assertEqual(full_thesis_refresh_queue_audit["verdict"], "PASS")
        self.assertEqual(
            full_thesis_refresh_queue_audit["queue_candidate_count"],
            full_thesis_refresh_queue_audit["event_board_non_stage0_count"],
        )
        self.assertGreater(full_thesis_refresh_queue_audit["queue_candidate_count"], 0)
        self.assertEqual(full_thesis_refresh_queue_audit["critical_counts"]["score_allowed_before_execution_count"], 0)
        self.assertEqual(full_thesis_refresh_queue_audit["critical_counts"]["stage_promotion_allowed_before_execution_count"], 0)
        self.assertEqual(full_thesis_production["full_thesis_refresh_queue_candidate_count"], full_thesis_refresh_queue_audit["queue_candidate_count"])
        self.assertEqual(full_thesis_seed_materialization["verdict"], "PASS")
        self.assertEqual(full_thesis_seed_materialization["verdict_scope"], "LEDGER_INTEGRITY_ONLY")
        self.assertTrue(full_thesis_seed_materialization["ledger_integrity_pass_allowed"])
        self.assertFalse(full_thesis_seed_materialization["actual_materialization_pass_allowed"])
        self.assertFalse(full_thesis_seed_materialization["full_thesis_seed_promotion_pass"])
        self.assertEqual(
            full_thesis_seed_materialization["operator_materialization_status"],
            "PENDING_FULL_THESIS_MATERIALIZATION",
        )
        self.assertEqual(
            full_thesis_seed_materialization["seed_event_count"],
            full_thesis_refresh_queue_audit["queue_candidate_count"]
            + full_thesis_seed_materialization["controlled_smoke_full_thesis_final_scope_count"],
        )
        self.assertEqual(full_thesis_seed_materialization["trace_row_count"], full_thesis_seed_materialization["seed_event_count"])
        self.assertEqual(full_thesis_seed_materialization["status_counts"], {"PLANNER_NOT_RUN": full_thesis_seed_materialization["seed_event_count"]})
        self.assertEqual(full_thesis_seed_materialization["critical_count"], 0)
        self.assertEqual(full_thesis_seed_materialization["full_thesis_promoted_seed_count"], 0)
        self.assertTrue(c06_guard["guard_replay_pass"])
        self.assertTrue(c06_guard["positive_wiring_smoke_ready"])
        self.assertTrue(c06_guard["source_backed_positive_replay_ready"])
        self.assertTrue(c06_guard["positive_semantic_replay_ready"])
        self.assertEqual(c06_guard["guard_case_count"], 3)
        self.assertEqual(c06_guard["guard_case_pass_count"], 3)
        self.assertTrue(c06_guard["guard_cases_pass"])
        self.assertEqual(c06_guard["score_contribution_leak_count"], 0)
        self.assertEqual(c06_guard["hard_break_false_positive_count"], 0)
        self.assertTrue(c06_source_replay["positive_replay_pass"])
        self.assertEqual(c06_source_replay["accepted_primitive_ids"], ["customer_preorder_or_allocation"])
        self.assertEqual(c06_source_replay["accepted_claim_count"], 1)
        self.assertEqual(c06_source_replay["blockers"], [])
        self.assertTrue(c08_source_replay["positive_replay_pass"])
        self.assertTrue(c08_source_replay["guard_replay_pass"])
        self.assertEqual(set(c08_source_replay["positive_accepted_primitive_ids"]), {"socket_or_test_demand_visible", "named_customer_quality"})
        self.assertEqual(c08_source_replay["guard_accepted_primitive_ids"], ["socket_or_test_demand_visible"])
        self.assertEqual(c08_source_replay["profile_only_guard_leaked_primitives"], [])
        self.assertEqual(c08_source_replay["accepted_claim_count"], 4)
        self.assertEqual(c08_source_replay["blockers"], [])
        self.assertTrue(c15_source_replay["positive_replay_pass"])
        self.assertTrue(c15_source_replay["guard_replay_pass"])
        self.assertEqual(
            set(c15_source_replay["positive_accepted_primitive_ids"]),
            {"spread_expansion", "pricing_power_confirmed", "fcf_quality_score"},
        )
        self.assertEqual(c15_source_replay["guard_accepted_primitive_ids"], [])
        self.assertEqual(c15_source_replay["raw_commodity_guard_leaked_primitives"], [])
        self.assertEqual(c15_source_replay["accepted_claim_count"], 6)
        self.assertEqual(c15_source_replay["blockers"], [])
        self.assertTrue(c17_source_replay["positive_replay_pass"])
        self.assertTrue(c17_source_replay["guard_replay_pass"])
        self.assertEqual(
            set(c17_source_replay["positive_support_primitive_ids"]),
            {"spread_expansion", "opm_expansion_pctp", "utilization_rate"},
        )
        self.assertEqual(c17_source_replay["guard_support_primitive_ids"], ["spread_expansion"])
        self.assertEqual(c17_source_replay["spread_only_guard_leaked_support_primitives"], [])
        self.assertEqual(c17_source_replay["accepted_claim_count"], 10)
        self.assertEqual(c17_source_replay["blockers"], [])
        self.assertFalse(c17_source_replay["production_score_evidence_allowed"])
        self.assertTrue(c24_source_replay["positive_replay_pass"])
        self.assertTrue(c24_source_replay["guard_replay_pass"])
        self.assertEqual(c24_source_replay["positive_support_primitive_ids"], ["trial_quality_visible"])
        self.assertEqual(c24_source_replay["guard_counter_primitive_ids"], ["binary_event_unresolved"])
        self.assertEqual(c24_source_replay["binary_event_guard_leaked_support_primitives"], [])
        self.assertEqual(c24_source_replay["accepted_claim_count"], 5)
        self.assertEqual(c24_source_replay["blockers"], [])
        self.assertFalse(c24_source_replay["production_score_evidence_allowed"])
        self.assertTrue(c28_source_replay["positive_replay_pass"])
        self.assertTrue(c28_source_replay["guard_replay_pass"])
        self.assertEqual(
            set(c28_source_replay["positive_support_primitive_ids"]),
            {"arr_growth_visible", "nrr", "retention_or_renewal", "rpo_to_sales", "recurring_margin_leverage"},
        )
        self.assertEqual(c28_source_replay["guard_support_primitive_ids"], [])
        self.assertEqual(c28_source_replay["guard_accepted_claim_ids"], [])
        self.assertEqual(c28_source_replay["keyword_only_guard_leaked_support_primitives"], [])
        self.assertEqual(c28_source_replay["accepted_claim_count"], 7)
        self.assertEqual(c28_source_replay["blockers"], [])
        self.assertFalse(c28_source_replay["production_score_evidence_allowed"])
        self.assertTrue(controlled_semantic_replay["controlled_semantic_replay_pass"])
        self.assertEqual(controlled_semantic_replay["case_count"], 10)
        self.assertEqual(controlled_semantic_replay["pass_count"], 10)
        self.assertEqual(controlled_semantic_replay["pending_count"], 0)
        self.assertEqual(controlled_semantic_replay["fail_count"], 0)
        self.assertEqual(controlled_semantic_replay["blockers"], [])
        case_ids = {case["case_id"] for case in controlled_semantic_replay["cases"]}
        self.assertIn("OLD_RISK_RESOLVED_FIXTURE", case_ids)
        self.assertIn("C08_TEST_SOCKET_CUSTOMER_ORDER_PROFILE_ONLY_GUARD", case_ids)
        self.assertIn("C15_MATERIAL_SPREAD_PASS_THROUGH_RAW_COMMODITY_GUARD", case_ids)
        self.assertIn("C17_CHEMICAL_SPREAD_REALIZED_MARGIN_BRIDGE_GUARD", case_ids)
        self.assertIn("C24_CLINICAL_BINARY_EVENT_GUARD", case_ids)
        self.assertIn("C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD", case_ids)
        self.assertEqual(self_repair["schema_version"], "e2r_census_v4_self_repair_log_v1")
        self.assertEqual(self_repair["status"], "RUN_COMPLETE")
        self.assertTrue(self_repair["loop_executed"])
        self.assertTrue(self_repair["completion_eligible"])
        self.assertEqual(self_repair["unresolved_failures"], [])
        self.assertIn("brain_web_evidence_pass_false", self_repair["deferred_goal_blockers"])
        self.assertNotIn("full_thesis_smoke_pending", self_repair["deferred_goal_blockers"])
        self.assertNotIn("full_thesis_smoke_execution_pending", self_repair["deferred_goal_blockers"])
        self.assertNotIn("full_thesis_smoke_honesty_false", self_repair["deferred_goal_blockers"])
        self.assertIn("full_thesis_production_pass_false", self_repair["deferred_goal_blockers"])
        self.assertNotIn("source_connector_capability_pending", self_repair["deferred_goal_blockers"])
        self.assertIn("full_thesis_seed_materialization_not_promoted", self_repair["deferred_goal_blockers"])
        self.assertNotIn("source_backed_replay_parity_all_archetypes_pending", self_repair["deferred_goal_blockers"])
        self.assertNotIn("controlled_semantic_replay_pending", self_repair["deferred_goal_blockers"])
        self.assertEqual(test_evidence["verdict"], "STRING_SUMMARY_ONLY")
        self.assertFalse(test_evidence["completion_eligible"])
        self.assertFalse(goal_matrix["goal_completion_minimum_pass"])
        self.assertFalse(goal_matrix["meaningful_operational_stage_requirement_pass"])
        self.assertFalse(goal_matrix["brain_web_requirement_pass"])
        self.assertFalse(goal_matrix["production_full_thesis_requirement_pass"])
        self.assertIn("full_thesis_goal4_semantic_split", goal_matrix)
        self.assertEqual(
            goal_matrix["production_full_e2r_score_path_pass"],
            goal_matrix["full_thesis_goal4_semantic_split"]["production_full_e2r_score_path_pass"],
        )
        self.assertEqual(
            goal_matrix["meaningful_full_thesis_evidence_pass"],
            goal_matrix["full_thesis_goal4_semantic_split"]["meaningful_full_thesis_evidence_pass"],
        )
        self.assertGreater(goal_matrix["required_goal_completion_pass_count"], 0)
        self.assertIn("BRAIN_WEB_EVIDENCE_PASS", goal_matrix["pending_gate_ids"])
        self.assertNotIn("SOURCE_CONNECTOR_CAPABILITY_PASS", goal_matrix["pending_gate_ids"])
        self.assertNotIn("FULL_THESIS_SMOKE_HONESTY_PASS", goal_matrix["pending_gate_ids"])
        self.assertNotIn("FULL_THESIS_SMOKE_PASS", goal_matrix["pending_gate_ids"])
        self.assertIn("FULL_THESIS_PRODUCTION_PASS", goal_matrix["pending_gate_ids"])
        self.assertNotIn("FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS", goal_matrix["pending_gate_ids"])
        self.assertIn("FULL_THESIS_SEED_PROMOTION_PASS", goal_matrix["pending_gate_ids"])
        self.assertNotIn("ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS", goal_matrix["pending_gate_ids"])
        self.assertNotIn("CONTROLLED_SEMANTIC_REPLAY_PASS", goal_matrix["pending_gate_ids"])
        self.assertIn("FULL_TEST_ARTIFACT_PASS", goal_matrix["pending_gate_ids"])
        self.assertEqual(report_generation["verdict"], "PASS")
        self.assertEqual(report_generation["critical_count"], 0)
        self.assertTrue(report_generation["report_generated_from_leaf_audit"])
        self.assertEqual(report_generation["in_memory_summary_used_for_acceptance_count"], 0)
        self.assertEqual(report_generation["leaf_report_metric_mismatch_count"], 0)
        self.assertFalse(report_generation["report_only_status_change_allowed"])
        self.assertFalse(goal_completion["goal_completion_ready"])
        self.assertNotIn("self_repair_not_run", goal_completion["blockers"])
        self.assertNotIn("self_repair_unresolved_failures", goal_completion["blockers"])
        self.assertNotIn("known_bad_regression_not_run", goal_completion["blockers"])
        self.assertNotIn("full_thesis_smoke_pending", goal_completion["blockers"])
        self.assertNotIn("full_thesis_smoke_execution_pending", goal_completion["blockers"])
        self.assertNotIn("full_thesis_smoke_honesty_false", goal_completion["blockers"])
        self.assertTrue(goal_completion["full_thesis_smoke_honesty_pass_allowed"])
        self.assertTrue(goal_completion["full_thesis_smoke_execution_pass_allowed"])
        self.assertIn("full_thesis_production_pass_false", goal_completion["blockers"])
        self.assertNotIn("source_connector_capability_pending", goal_completion["blockers"])
        self.assertFalse(goal_completion["full_thesis_production_pass_allowed"])
        self.assertIn("full_thesis_goal4_semantic_split", goal_completion)
        self.assertEqual(
            goal_completion["production_full_e2r_score_path_pass_allowed"],
            goal_completion["full_thesis_goal4_semantic_split"]["production_full_e2r_score_path_pass"],
        )
        self.assertEqual(
            goal_completion["meaningful_full_thesis_evidence_pass_allowed"],
            goal_completion["full_thesis_goal4_semantic_split"]["meaningful_full_thesis_evidence_pass"],
        )
        self.assertTrue(goal_completion["source_connector_capability_pass_allowed"])
        self.assertEqual(goal_completion["source_connector_capability_summary"]["blocking_full_thesis_source_class_count"], 0)
        self.assertEqual(goal_completion["source_connector_capability_summary"]["blocking_full_thesis_task_count"], 0)
        self.assertTrue(goal_completion["source_connector_capability_summary"]["full_thesis_task_executable_source_path_pass_allowed"])
        self.assertGreater(goal_completion["source_connector_capability_summary"]["full_thesis_task_with_blocking_source_class_count"], 0)
        self.assertIn("IssuerIR", goal_completion["source_connector_capability_summary"]["placeholder_source_classes"])
        self.assertNotIn("ReportPDF", goal_completion["source_connector_capability_summary"]["missing_connector_source_classes"])
        self.assertNotIn("CompanyNewsroom", goal_completion["source_connector_capability_summary"]["missing_connector_source_classes"])
        self.assertTrue(goal_completion["full_thesis_seed_materialization_audit_pass_allowed"])
        self.assertTrue(goal_completion["full_thesis_seed_ledger_integrity_pass_allowed"])
        self.assertFalse(goal_completion["full_thesis_seed_actual_materialization_pass_allowed"])
        self.assertFalse(goal_completion["full_thesis_seed_promotion_pass_allowed"])
        self.assertEqual(
            goal_completion["full_thesis_seed_materialization_summary"]["status_counts"],
            {"PLANNER_NOT_RUN": full_thesis_seed_materialization["seed_event_count"]},
        )
        self.assertEqual(goal_completion["full_thesis_seed_materialization_summary"]["verdict_scope"], "LEDGER_INTEGRITY_ONLY")
        self.assertFalse(goal_completion["full_thesis_seed_materialization_summary"]["actual_materialization_pass_allowed"])
        self.assertEqual(goal_completion["full_thesis_seed_materialization_summary"]["full_thesis_promoted_seed_count"], 0)
        self.assertEqual(goal_completion["full_thesis_production_status"], "PENDING_FULL_THESIS_PRODUCTION")
        self.assertTrue(goal_completion["c06_guard_replay_pass_allowed"])
        self.assertEqual(goal_completion["c06_guard_replay_status"], "C06_GUARD_REPLAY_PASS")
        self.assertNotIn("source_backed_replay_parity_all_archetypes_pending", goal_completion["blockers"])
        self.assertIn("full_thesis_seed_promotion_pass_false", goal_completion["blockers"])
        self.assertNotIn("controlled_semantic_replay_pending", goal_completion["blockers"])
        self.assertTrue(goal_completion["controlled_semantic_replay_pass_allowed"])
        self.assertEqual(goal_completion["controlled_semantic_replay_summary"]["case_count"], 10)
        self.assertEqual(goal_completion["controlled_semantic_replay_summary"]["pass_count"], 10)
        self.assertEqual(goal_completion["controlled_semantic_replay_summary"]["pending_count"], 0)
        self.assertIn("machine_readable_test_result_artifact_missing", goal_completion["blockers"])
        self.assertIn("goal_requirement_matrix_pass_false", goal_completion["blockers"])
        self.assertFalse(goal_completion["goal_requirement_matrix_summary"]["goal_completion_minimum_pass"])
        self.assertEqual(goal_completion["goal_requirement_matrix_summary"]["required_goal_completion_count"], goal_matrix["required_goal_completion_count"])

    def test_machine_readable_test_result_artifact_can_clear_test_evidence_blocker(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            artifact = root / "test_result.json"
            artifact.write_text(
                json.dumps(
                    {
                        "schema_version": TEST_RESULT_ARTIFACT_SCHEMA,
                        "command": ["python", "-m", "unittest", "discover", "-s", "tests"],
                        "started_at": "2026-07-01T00:00:00+00:00",
                        "finished_at": "2026-07-01T00:01:53+00:00",
                        "duration_seconds": 113.112,
                        "exit_code": 0,
                        "status": "OK",
                        "test_count": 4887,
                        "failed_count": 0,
                        "error_count": 0,
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            output_root = root / "out"
            run_census_mode_v4(
                CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(output_root),
                    v3_output_root="output/census_v3/2026-07-01",
                    write_operational_docs=False,
                    test_result_summary="string summary is not enough",
                    test_result_artifact=str(artifact),
                )
            )
            evidence = read_json(output_root / "test_result_evidence_audit.json")
            goal_completion = read_json(output_root / "goal_completion_audit.json")
            goal_matrix = read_json(output_root / "goal_requirement_matrix_audit.json")

            self.assertEqual(evidence["verdict"], "MACHINE_READABLE_TEST_ARTIFACT_PASS")
            self.assertTrue(evidence["completion_eligible"])
            self.assertTrue(evidence["artifact_valid"])
            self.assertEqual(evidence["artifact_test_count"], 4887)
            self.assertNotIn("machine_readable_test_result_artifact_missing", goal_completion["blockers"])
            self.assertFalse(goal_completion["goal_completion_ready"])
            self.assertFalse(goal_matrix["goal_completion_minimum_pass"])
            self.assertNotIn("FULL_TEST_ARTIFACT_PASS", goal_matrix["pending_gate_ids"])
            self.assertNotIn("known_bad_regression_not_run", goal_completion["blockers"])
            self.assertNotIn("self_repair_not_run", goal_completion["blockers"])
            self.assertIn("brain_web_evidence_pass_false", goal_completion["blockers"])
            self.assertIn("full_thesis_smoke_pending", goal_completion["blockers"])
            self.assertIn("full_thesis_smoke_execution_pending", goal_completion["blockers"])
            self.assertNotIn("full_thesis_smoke_honesty_false", goal_completion["blockers"])
            self.assertIn("full_thesis_production_pass_false", goal_completion["blockers"])
            self.assertNotIn("source_connector_capability_pending", goal_completion["blockers"])
            self.assertNotIn("source_backed_replay_parity_all_archetypes_pending", goal_completion["blockers"])
            self.assertNotIn("controlled_semantic_replay_pending", goal_completion["blockers"])
            self.assertIn("goal_requirement_matrix_pass_false", goal_completion["blockers"])

    def test_invalid_test_result_artifact_does_not_clear_test_evidence_blocker(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            artifact = root / "test_result.json"
            artifact.write_text("{}", encoding="utf-8")
            output_root = root / "out"
            run_census_mode_v4(
                CensusV4RunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(output_root),
                    v3_output_root="output/census_v3/2026-07-01",
                    write_operational_docs=False,
                    test_result_artifact=str(artifact),
                )
            )
            evidence = read_json(output_root / "test_result_evidence_audit.json")
            goal_completion = read_json(output_root / "goal_completion_audit.json")

            self.assertEqual(evidence["verdict"], "INVALID_TEST_ARTIFACT")
            self.assertFalse(evidence["completion_eligible"])
            self.assertFalse(evidence["artifact_valid"])
            self.assertIn("schema_version must be e2r_test_result_artifact_v1", evidence["artifact_validation_errors"])
            self.assertIn("machine_readable_test_result_artifact_missing", goal_completion["blockers"])

if __name__ == "__main__":
    unittest.main()
