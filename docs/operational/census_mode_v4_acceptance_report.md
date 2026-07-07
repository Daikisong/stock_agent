# Census Mode v4 Acceptance Report

0. Operator stage warning: stage_scope_notice=FULL_THESIS_STAGE_ROWS_PRESENT_SCOPE_GUARD_REQUIRED; operational_stage_use_allowed=False; full_thesis_rows=6; full_thesis_refresh_queue_candidates=81; full_e2r_verified_score_rows=6; event_board_non_stage0_rows=81; event_board_stage_rows_are_operational_full_thesis=False
1. Final status: IMPLEMENTATION_MERGED, V3_FORENSIC_REVIEW_COMPLETE, ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS, ATOMIC_STAGE_DECISION_PASS, SCORE_SCALE_PASS, STAGE_SEMANTICS_PASS, SEMANTIC_PRIMITIVE_GUARD_PASS, DAILY_EVENT_FULL_THESIS_SEPARATION_PASS, CENSUS_ASSESSMENT_CANDIDATE_EVENT_SEPARATION_PASS, FULL_THESIS_SMOKE_HONESTY_PASS, FULL_THESIS_SMOKE_EXECUTION_PENDING, FULL_THESIS_SMOKE_PENDING, FULL_THESIS_SMOKE_REQUIREMENT_PENDING, FULL_THESIS_PRODUCTION_CANNOT_SUBSTITUTE_SMOKE, FULL_THESIS_REFRESH_QUEUE_PRESENT, BRAIN_WEB_ATTEMPT_RECORDED, BRAIN_STAGE_PROMOTION_AUDITED, BRAIN_WEB_READINESS_GATE_AUDITED, OFFICIAL_BASELINE_EVIDENCE_CLAIM_PAYLOAD_PRESENT, KNOWN_BAD_REGRESSION_PASS, SELF_REPAIR_LOOP_PASS, RESEARCH_BRAIN_V4_REPORT_BRIDGE_IMPORTED, BRAIN_WEB_EVIDENCE_PASS
2. Commit SHA / message / push status / working tree: report_generation_sha=4eec331e4a1c2ebeac8ec2f528b4991c6fd154f6; push_status=not_pushed_by_runner
3. Test artifact command: missing
   Test log summary: not_run_by_census_v4_runner
   Test artifact duration_seconds: None
   Test evidence audit: STRING_SUMMARY_ONLY; artifact_exists=False; artifact_test_count=None
4. Target gate: full_thesis; target_gate_pass=False; target_gate_verdict=TARGET_GATE_BLOCKED
5. Goal completion audit: goal_completion_ready=False; blockers=['full_thesis_smoke_pending', 'full_thesis_smoke_execution_pending', 'full_thesis_production_pass_false', 'full_thesis_seed_materialization_audit_not_pass', 'machine_readable_test_result_artifact_missing', 'goal_requirement_matrix_pass_false']
5a. Full thesis production audit: PENDING_FULL_THESIS_PRODUCTION; production_pass_allowed=False; production_mode_requested=True; refresh_queue_candidates=81; production_rows=6; controlled_smoke_rows=0; controlled_smoke_rejected=0; blockers=['production_full_thesis_rows_with_required_positive_missing_primitives']
5b. C06 guard replay audit: guard_replay_pass=True; guard_cases=3/3; blockers=['controlled_smoke_claims_are_fixture_mapped_not_contract_blind_extracted']
5c. Controlled semantic replay audit: pass=True; cases=10/10; pending=0; blockers=[]
5d. Full thesis smoke gate: honesty_pass=True; execution_pass=False; legacy_smoke_pass=False; gate_pass_allowed=False; gate_blockers=['full_thesis_smoke_not_passed', 'full_thesis_smoke_gate_not_requested', 'controlled_smoke_not_allowed_for_production_run_mode', 'controlled_smoke_requires_brain_web_disabled']
5e. Goal requirement matrix: minimum_pass=False; pass=18/22; pending=3; fail=1; blockers=['full_thesis_smoke_pending', 'full_thesis_production_pass_false', 'full_thesis_seed_materialization_audit_not_pass', 'machine_readable_test_result_artifact_missing']
6. Run mode: BRAIN_AND_WEB_ACQUISITION_ENABLED
7. Leaf artifact audit: PASS
8. Eligible / Stage rows: 3391 / 3391
9. Base/display stage distribution: {'Stage0': 3301, '3-Green': 1, 'Stage1': 51, '1': 1, 'Stage2-Watch': 29, '0': 6, '2': 1, 'Red': 1}
10. Stage signal distribution: {'NO_CURRENT_CATALYST': 3301, 'FULL_THESIS_PRODUCTION_STAGE': 6, 'OFFICIAL_EVENT_WATCH': 33, 'BRAIN_WEB_CLAIM_BACKED_STAGE': 2, 'EVIDENCE_INSUFFICIENT': 10, 'MATERIAL_CLAIM_WATCH': 29, 'SOURCE_PENDING': 8, 'RISK_REVIEW': 1, 'BRAIN_OFFICIAL_CLAIM_BACKED_STAGE': 1}
11. Score scale distribution: {'NO_SCORE': 3319, 'FULL_E2R_100': 6, 'EVENT_WEIGHTED_PARTIAL': 66}
12. Stage scope distribution: {'CENSUS_EVENT_BOARD': 3382, 'FULL_THESIS': 6, 'BRAIN_WEB_PARTIAL': 2, 'BRAIN_OFFICIAL_PARTIAL': 1}
13. Score scope distribution: {'NO_SCORE': 3319, 'FULL_E2R_100': 6, 'EVENT_WEIGHTED_PARTIAL': 63, 'BRAIN_WEB_CLAIM_BACKED_PARTIAL': 2, 'BRAIN_OFFICIAL_CLAIM_BACKED_PARTIAL': 1}
14. Operator stage use distribution: {'NOT_FULL_THESIS_STAGE': 3385, 'FULL_THESIS_STAGE': 6}
15. Operator score use distribution: {'NOT_FULL_E2R_SCORE': 3385, 'FULL_E2R_SCORE': 6}
16. Event evidence score rows: 66
17. Full E2R verified score rows: 6
17a. Full thesis stage rows: 6; refresh queue candidates: 81; event-board non-Stage0 rows: 81; operator_stage_scope_notice=FULL_THESIS_STAGE_ROWS_PRESENT_SCOPE_GUARD_REQUIRED
18. Candidate event scope distribution: {'ASSESSMENT_ONLY': 3301, 'CANDIDATE_EVENTS_PRESENT': 90}
19. Candidate event count: 248
20. Score eligible candidate event count: 98
21. Planner rows: 455; real LLM planner calls=108; real_success=108; not_attempted=347
22. LLM planner real-provider success: 108
23. Brain/Web attempt verdict: ATTEMPTED_WITH_SOURCE_TASKS; source_tasks=735; accepted_claims=111
24. Brain Stage promotion verdict: PROMOTION_APPLIED; promoted=9; unsafe_promoted=0; snapshot_docs=1
25. Brain/Web readiness gate: READY_FOR_BRAIN_WEB_EVIDENCE_PASS; pass_allowed=True; minimum_gate_applies=True; operational_minimum_count_gate_applies=True; minimum_required_counts={'llm_claim_extractor_attempt_count': 10, 'llm_planner_call_count': 30, 'official_first_violation_count': 0, 'web_fetched_document_count': 10, 'web_or_llm_accepted_claim_count': 3, 'web_search_call_count': 20, 'web_search_task_count': 20}; blockers=0; connectivity_missing=0
26. Web search tasks: 128
27. Claim extractor runs: 112
28. Evidence claim payload rows: 158
29. Non-representative claim audit: PASS; critical_count=0; warning_count=58; representative_claims=79; non_representative_claims=79; reason_distribution={'accepted_claim_without_atomic_decision': 58, 'non_representative_atomic_decision': 21}
30. Research Brain bridge verdict: SHADOW_OR_IMPORT_ONLY; usable_for_census_cutover=False; snapshot_url_count=255
31. Claim-to-stage forensic audit: PASS; critical_count=0; scored_rows=72
32. Source task realness audit: LIVE_SOURCE_PASS; scope=LEDGER_REFRESH_REALNESS_PASS; live_source_pass_allowed=True; claim_producing=84; real_fetch=24; fresh_cache=60; lifecycle_refresh=32
33. Source task satisfaction audit: PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION; scope=LEDGER_REFRESH_SOURCE_TASK_SATISFACTION_PASS; live_source_task_satisfaction_pass_allowed=False; critical_count=0; warning_count=79; representative_score_claims=79; chain_closed_to_representative_stage=114; non_representative_source_task_claims=79; baseline_only_score_claims=32
34. Primitive state chain audit: PASS; critical_count=0; representative_score_claims=79; representative_score_claims_with_primitive=79; primitive_states=254; primitive_mappings=119; mapping_leaf_resolution_supported=True
35. Existing ledger reuse audit: PASS; reused_claims=92; new_brain_web_claims=66
36. Last effective thesis audit: PASS; status_distribution={'ACTIVE_THESIS': 74, 'NEEDS_REFRESH': 3, 'NO_KNOWN_THESIS': 3306, 'SOURCE_PENDING': 8}
37. Source coverage audit: PASS_LEDGER_REFRESH_COVERAGE; live_source_coverage_pass=False; cutover_replay_only_symbols=67
38. Runtime plausibility audit: PASS_LIVE_RUNTIME_PLAUSIBILITY; runtime_mode=BRAIN_AND_WEB_ACQUISITION_ENABLED; provider_calls=24; llm_calls=108
39. Sample leaf bundle rows: 72
40. Report generation source: leaf_artifact_audit.json + readiness_verdict.json; report_generated_from_leaf_audit=true
41. Static production path audit:
    legacy_runner_production_reachable_count=0
    legacy_v3_runner_production_reachable_count=0
    empty_claims_stage_builder_production_count=0
    old_cli_can_claim_pass_count=0
    official_cli_not_v4_runner_count=0
    sample_bundle_missing_scored_row_count=0
42. Final verdict: NOT_READY
43. Output root: output/census_v4/2026-07-05-research-to-runtime-parity-self-repair-01-20260707T130702Z
44. runtime_seconds: 11291.10

Note: v4 does not claim Meaningful Operational Stage or Brain/Web evidence pass unless the required leaf artifacts exist.
