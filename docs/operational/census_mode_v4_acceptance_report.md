# Census Mode v4 Acceptance Report

0. Operator stage warning: stage_scope_notice=NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST; operational_stage_use_allowed=False; full_thesis_rows=0; full_thesis_refresh_queue_candidates=85; full_e2r_verified_score_rows=0; event_board_non_stage0_rows=85; event_board_stage_rows_are_operational_full_thesis=False
1. Final status: IMPLEMENTATION_MERGED, V3_FORENSIC_REVIEW_COMPLETE, ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS, ATOMIC_STAGE_DECISION_PASS, SCORE_SCALE_PASS, STAGE_SEMANTICS_PASS, SEMANTIC_PRIMITIVE_GUARD_PASS, DAILY_EVENT_FULL_THESIS_SEPARATION_PASS, CENSUS_ASSESSMENT_CANDIDATE_EVENT_SEPARATION_PASS, FULL_THESIS_SMOKE_HONESTY_PASS, FULL_THESIS_SMOKE_EXECUTION_PENDING, FULL_THESIS_SMOKE_PENDING, FULL_THESIS_SMOKE_REQUIREMENT_PENDING, FULL_THESIS_PRODUCTION_CANNOT_SUBSTITUTE_SMOKE, FULL_THESIS_REFRESH_QUEUE_PRESENT, BRAIN_WEB_ATTEMPT_RECORDED, BRAIN_STAGE_PROMOTION_AUDITED, BRAIN_WEB_READINESS_GATE_AUDITED, OFFICIAL_BASELINE_EVIDENCE_CLAIM_PAYLOAD_PRESENT, KNOWN_BAD_REGRESSION_PASS, SELF_REPAIR_LOOP_PASS, RESEARCH_BRAIN_V4_REPORT_BRIDGE_IMPORTED
2. Commit SHA / message / push status / working tree: report_generation_sha=e22fb2b11c8cfbc62ba99385d6f648377b675b6f; push_status=not_pushed_by_runner
3. Test artifact command: missing
   Test log summary: not_run_by_census_v4_runner
   Test artifact duration_seconds: None
   Test evidence audit: STRING_SUMMARY_ONLY; artifact_exists=False; artifact_test_count=None
4. Target gate: full_thesis; target_gate_pass=False; target_gate_verdict=TARGET_GATE_BLOCKED
5. Goal completion audit: goal_completion_ready=False; blockers=['brain_web_evidence_pass_false', 'full_thesis_smoke_pending', 'full_thesis_smoke_execution_pending', 'full_thesis_production_pass_false', 'full_thesis_seed_materialization_audit_not_pass', 'full_thesis_seed_promotion_pass_false', 'machine_readable_test_result_artifact_missing', 'goal_requirement_matrix_pass_false']
5a. Full thesis production audit: PENDING_FULL_THESIS_PRODUCTION; production_pass_allowed=False; production_mode_requested=True; refresh_queue_candidates=85; production_rows=0; controlled_smoke_rows=0; controlled_smoke_rejected=0; blockers=['production_full_thesis_runner_no_eligible_rows']
5b. C06 guard replay audit: guard_replay_pass=True; guard_cases=3/3; blockers=[]
5c. Controlled semantic replay audit: pass=True; cases=10/10; pending=0; blockers=[]
5d. Full thesis smoke gate: honesty_pass=True; execution_pass=False; legacy_smoke_pass=False; gate_pass_allowed=False; gate_blockers=['full_thesis_smoke_not_passed', 'full_thesis_smoke_gate_not_requested', 'controlled_smoke_not_allowed_for_production_run_mode', 'controlled_smoke_requires_brain_web_disabled']
5e. Goal requirement matrix: minimum_pass=False; pass=16/22; pending=5; fail=1; blockers=['full_thesis_smoke_pending', 'full_thesis_production_pass_false', 'full_thesis_seed_materialization_audit_not_pass', 'full_thesis_seed_promotion_pass_false', 'brain_web_evidence_pass_false', 'machine_readable_test_result_artifact_missing']
6. Run mode: BRAIN_AND_WEB_ACQUISITION_ENABLED
7. Leaf artifact audit: PASS
8. Eligible / Stage rows: 3391 / 3391
9. Base/display stage distribution: {'Stage0': 3306, 'Stage1': 55, 'Stage2-Watch': 29, 'Red': 1}
10. Stage signal distribution: {'NO_CURRENT_CATALYST': 3306, 'OFFICIAL_EVENT_WATCH': 36, 'EVIDENCE_INSUFFICIENT': 11, 'MATERIAL_CLAIM_WATCH': 29, 'SOURCE_PENDING': 8, 'RISK_REVIEW': 1}
11. Score scale distribution: {'NO_SCORE': 3325, 'EVENT_WEIGHTED_PARTIAL': 66}
12. Stage scope distribution: {'CENSUS_EVENT_BOARD': 3391}
13. Score scope distribution: {'NO_SCORE': 3325, 'EVENT_WEIGHTED_PARTIAL': 66}
14. Operator stage use distribution: {'NOT_FULL_THESIS_STAGE': 3391}
15. Operator score use distribution: {'NOT_FULL_E2R_SCORE': 3391}
16. Event evidence score rows: 66
17. Full E2R verified score rows: 0
17a. Full thesis stage rows: 0; refresh queue candidates: 85; event-board non-Stage0 rows: 85; operator_stage_scope_notice=NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST
18. Candidate event scope distribution: {'ASSESSMENT_ONLY': 3306, 'CANDIDATE_EVENTS_PRESENT': 85}
19. Candidate event count: 226
20. Score eligible candidate event count: 92
21. Planner rows: 458; real LLM planner calls=111; real_success=110; not_attempted=347
22. LLM planner real-provider success: 110
23. Brain/Web attempt verdict: ATTEMPTED_NOT_CUTOVER_READY; source_tasks=809; accepted_claims=118
24. Brain Stage promotion verdict: ELIGIBLE_NOT_PROMOTED; promoted=0; unsafe_promoted=0; snapshot_docs=0
25. Brain/Web readiness gate: BLOCKED; pass_allowed=False; minimum_gate_applies=True; operational_minimum_count_gate_applies=True; minimum_required_counts={'llm_claim_extractor_attempt_count': 10, 'llm_planner_call_count': 30, 'official_first_violation_count': 0, 'web_fetched_document_count': 10, 'web_or_llm_accepted_claim_count': 3, 'web_search_call_count': 20, 'web_search_task_count': 20}; blockers=4; connectivity_missing=12
26. Web search tasks: 153
27. Claim extractor runs: 123
28. Evidence claim payload rows: 161
29. Non-representative claim audit: PASS; critical_count=0; warning_count=77; representative_claims=66; non_representative_claims=95; reason_distribution={'accepted_claim_without_atomic_decision': 77, 'non_representative_atomic_decision': 18}
30. Research Brain bridge verdict: SHADOW_OR_IMPORT_ONLY; usable_for_census_cutover=False; snapshot_url_count=255
31. Claim-to-stage forensic audit: PASS; critical_count=0; scored_rows=66
32. Source task realness audit: LIVE_SOURCE_PASS; scope=LEDGER_REFRESH_REALNESS_PASS; live_source_pass_allowed=True; claim_producing=87; real_fetch=27; fresh_cache=60; lifecycle_refresh=32
33. Source task satisfaction audit: PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION; scope=LEDGER_REFRESH_SOURCE_TASK_SATISFACTION_PASS; live_source_task_satisfaction_pass_allowed=False; critical_count=0; warning_count=95; representative_score_claims=66; chain_closed_to_representative_stage=66; non_representative_source_task_claims=95; baseline_only_score_claims=32
34. Primitive state chain audit: PASS; critical_count=0; representative_score_claims=66; representative_score_claims_with_primitive=66; primitive_states=114; primitive_mappings=96; mapping_leaf_resolution_supported=True
35. Existing ledger reuse audit: PASS; reused_claims=92; new_brain_web_claims=69
36. Last effective thesis audit: PASS; status_distribution={'ACTIVE_THESIS': 74, 'NEEDS_REFRESH': 3, 'NO_KNOWN_THESIS': 3306, 'SOURCE_PENDING': 8}
37. Source coverage audit: PASS_LEDGER_REFRESH_COVERAGE; live_source_coverage_pass=False; cutover_replay_only_symbols=66
38. Runtime plausibility audit: PASS_LIVE_RUNTIME_PLAUSIBILITY; runtime_mode=BRAIN_AND_WEB_ACQUISITION_ENABLED; provider_calls=27; llm_calls=110
39. Sample leaf bundle rows: 66
40. Report generation source: leaf_artifact_audit.json + readiness_verdict.json; report_generated_from_leaf_audit=true
41. Static production path audit:
    legacy_runner_production_reachable_count=0
    legacy_v3_runner_production_reachable_count=0
    empty_claims_stage_builder_production_count=0
    old_cli_can_claim_pass_count=0
    official_cli_not_v4_runner_count=0
    sample_bundle_missing_scored_row_count=0
42. Final verdict: NOT_READY
43. Output root: output/census_v4/2026-07-05-research-to-runtime-parity-self-repair-01-20260708T131257Z
44. runtime_seconds: 12540.40

Note: v4 does not claim Meaningful Operational Stage or Brain/Web evidence pass unless the required leaf artifacts exist.
