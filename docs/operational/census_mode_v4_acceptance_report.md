# Census Mode v4 Acceptance Report

0. Operator stage warning: stage_scope_notice=FULL_THESIS_STAGE_ROWS_PRESENT_SCOPE_GUARD_REQUIRED; operational_stage_use_allowed=True; full_thesis_rows=32; full_thesis_refresh_queue_candidates=53; full_e2r_verified_score_rows=32; event_board_non_stage0_rows=53; event_board_stage_rows_are_operational_full_thesis=False
1. Final status: IMPLEMENTATION_MERGED, V3_FORENSIC_REVIEW_COMPLETE, ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS, ATOMIC_STAGE_DECISION_PASS, SCORE_SCALE_PASS, STAGE_SEMANTICS_PASS, SEMANTIC_PRIMITIVE_GUARD_PASS, DAILY_EVENT_FULL_THESIS_SEPARATION_PASS, CENSUS_ASSESSMENT_CANDIDATE_EVENT_SEPARATION_PASS, FULL_THESIS_SMOKE_HONESTY_PASS, FULL_THESIS_SMOKE_EXECUTION_PENDING, FULL_THESIS_SMOKE_PENDING, FULL_THESIS_SMOKE_REQUIREMENT_PASS_BY_PRODUCTION_FULL_THESIS, FULL_THESIS_REFRESH_QUEUE_PRESENT, FULL_THESIS_SEED_LEDGER_INTEGRITY_PASS, FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS, FULL_THESIS_SEED_PROMOTION_PASS, FULL_THESIS_SEED_ACTUAL_MATERIALIZATION_PASS, BRAIN_WEB_ATTEMPT_RECORDED, BRAIN_STAGE_PROMOTION_AUDITED, BRAIN_WEB_READINESS_GATE_AUDITED, OFFICIAL_BASELINE_EVIDENCE_CLAIM_PAYLOAD_PRESENT, KNOWN_BAD_REGRESSION_PASS, SELF_REPAIR_LOOP_PASS, RESEARCH_BRAIN_V4_REPORT_BRIDGE_IMPORTED, BRAIN_WEB_EVIDENCE_PASS
2. Commit SHA / message / push status / working tree: report_generation_sha=16795f44dd993c4895a7a0e2701371ced37eeb7d; push_status=not_pushed_by_runner
3. Test artifact command: PYTHONPATH=src python -m unittest discover -s tests -v
   Test log summary: not_run_by_census_v4_runner
   Test artifact duration_seconds: 251.5772
   Test evidence audit: MACHINE_READABLE_TEST_ARTIFACT_PASS; artifact_exists=True; artifact_test_count=5154
4. Target gate: full_thesis; target_gate_pass=True; target_gate_verdict=TARGET_GATE_PASS
5. Goal completion audit: goal_completion_ready=True; blockers=[]
5a. Full thesis production audit: FULL_THESIS_PRODUCTION_PASS; production_pass_allowed=True; production_mode_requested=True; refresh_queue_candidates=53; production_rows=32; controlled_smoke_rows=0; controlled_smoke_rejected=0; blockers=[]
5b. C06 guard replay audit: guard_replay_pass=True; guard_cases=3/3; blockers=['controlled_smoke_claims_are_fixture_mapped_not_contract_blind_extracted']
5c. Controlled semantic replay audit: pass=True; cases=10/10; pending=0; blockers=[]
5d. Full thesis smoke gate: honesty_pass=True; execution_pass=False; legacy_smoke_pass=False; gate_pass_allowed=False; gate_blockers=['full_thesis_smoke_not_passed', 'full_thesis_smoke_gate_not_requested', 'controlled_smoke_not_allowed_for_production_run_mode', 'controlled_smoke_requires_brain_web_disabled']
5e. Goal requirement matrix: minimum_pass=True; pass=21/21; pending=0; fail=0; blockers=[]
6. Run mode: BRAIN_AND_WEB_ACQUISITION_ENABLED
7. Leaf artifact audit: PASS
8. Eligible / Stage rows: 3391 / 3391
9. Base/display stage distribution: {'0': 25, '1': 5, '2': 2, 'Red': 1, 'Stage0': 3306, 'Stage1': 38, 'Stage2-Watch': 14}
10. Stage signal distribution: {'EVIDENCE_INSUFFICIENT': 4, 'FULL_THESIS_PRODUCTION_STAGE': 32, 'MATERIAL_CLAIM_WATCH': 14, 'NO_CURRENT_CATALYST': 3306, 'OFFICIAL_EVENT_WATCH': 26, 'RISK_REVIEW': 1, 'SOURCE_PENDING': 8}
11. Score scale distribution: {'EVENT_WEIGHTED_PARTIAL': 41, 'FULL_E2R_100': 32, 'NO_SCORE': 3318}
12. Stage scope distribution: {'CENSUS_EVENT_BOARD': 3359, 'FULL_THESIS': 32}
13. Score scope distribution: {'EVENT_WEIGHTED_PARTIAL': 41, 'FULL_E2R_100': 32, 'NO_SCORE': 3318}
14. Operator stage use distribution: {'FULL_THESIS_STAGE': 32, 'NOT_FULL_THESIS_STAGE': 3359}
15. Operator score use distribution: {'FULL_E2R_SCORE': 32, 'NOT_FULL_E2R_SCORE': 3359}
16. Event evidence score rows: 41
17. Full E2R verified score rows: 32
17a. Full thesis stage rows: 32; refresh queue candidates: 53; event-board non-Stage0 rows: 53; operator_stage_scope_notice=FULL_THESIS_STAGE_ROWS_PRESENT_SCOPE_GUARD_REQUIRED
18. Candidate event scope distribution: {'ASSESSMENT_ONLY': 3306, 'CANDIDATE_EVENTS_PRESENT': 85}
19. Candidate event count: 258
20. Score eligible candidate event count: 124
21. LLM planner calls: 432
22. LLM planner real-provider success: 50
23. Brain/Web attempt verdict: ATTEMPTED_WITH_SOURCE_TASKS; source_tasks=389; accepted_claims=307
24. Brain Stage promotion verdict: PROMOTION_APPLIED; promoted=32; unsafe_promoted=0; snapshot_docs=0
25. Brain/Web readiness gate: READY_FOR_BRAIN_WEB_EVIDENCE_PASS; pass_allowed=True; minimum_gate_applies=True; operational_minimum_count_gate_applies=True; minimum_required_counts={'llm_claim_extractor_attempt_count': 10, 'llm_planner_call_count': 30, 'web_fetched_document_count': 10, 'web_or_llm_accepted_claim_count': 3, 'web_search_call_count': 20, 'web_search_task_count': 20}; blockers=0; connectivity_missing=0
26. Web search tasks: 102
27. Claim extractor runs: 64
28. Evidence claim payload rows: 264
29. Non-representative claim audit: PASS; critical_count=0; warning_count=125; representative_claims=95; non_representative_claims=169; reason_distribution={'accepted_claim_without_atomic_decision': 125, 'non_representative_atomic_decision': 44}
30. Research Brain bridge verdict: SHADOW_OR_IMPORT_ONLY; usable_for_census_cutover=False; snapshot_url_count=255
31. Claim-to-stage forensic audit: PASS; critical_count=0; scored_rows=73
32. Source task realness audit: LIVE_SOURCE_PASS; scope=LEDGER_REFRESH_REALNESS_PASS; live_source_pass_allowed=True; claim_producing=138; real_fetch=78; fresh_cache=60; lifecycle_refresh=32
33. Source task satisfaction audit: PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION; scope=LEDGER_REFRESH_SOURCE_TASK_SATISFACTION_PASS; live_source_task_satisfaction_pass_allowed=False; critical_count=0; warning_count=499; representative_score_claims=95; chain_closed_to_representative_stage=183; non_representative_source_task_claims=169; baseline_only_score_claims=32
34. Primitive state chain audit: PASS; critical_count=0; representative_score_claims=95; representative_score_claims_with_primitive=95; primitive_states=341; primitive_mappings=146; mapping_leaf_resolution_supported=True
35. Existing ledger reuse audit: PASS; reused_claims=92; new_brain_web_claims=172
36. Last effective thesis audit: PASS; status_distribution={'ACTIVE_THESIS': 74, 'NEEDS_REFRESH': 3, 'NO_KNOWN_THESIS': 3306, 'SOURCE_PENDING': 8}
37. Source coverage audit: PASS_LEDGER_REFRESH_COVERAGE; live_source_coverage_pass=False; cutover_replay_only_symbols=73
38. Runtime plausibility audit: PASS_LIVE_RUNTIME_PLAUSIBILITY; runtime_mode=BRAIN_AND_WEB_ACQUISITION_ENABLED; provider_calls=78; llm_calls=50
39. Sample leaf bundle rows: 73
40. Report generation source: leaf_artifact_audit.json + readiness_verdict.json; report_generated_from_leaf_audit=true
41. Static production path audit:
    legacy_runner_production_reachable_count=0
    legacy_v3_runner_production_reachable_count=0
    empty_claims_stage_builder_production_count=0
    old_cli_can_claim_pass_count=0
    official_cli_not_v4_runner_count=0
    sample_bundle_missing_scored_row_count=0
42. Final verdict: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
43. Output root: output/census_v4/2026-07-01-v136-goal-gates-audit-refresh
44. runtime_seconds: 0.00

Note: v4 does not claim Meaningful Operational Stage or Brain/Web evidence pass unless the required leaf artifacts exist.
