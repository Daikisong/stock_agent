# Census Mode v4 Acceptance Report

0. Operator stage warning: stage_scope_notice=FULL_THESIS_STAGE_ROWS_PRESENT_SCOPE_GUARD_REQUIRED; operational_stage_use_allowed=True; full_thesis_rows=10; full_thesis_refresh_queue_candidates=62; full_e2r_verified_score_rows=10; event_board_non_stage0_rows=62; event_board_stage_rows_are_operational_full_thesis=False
1. Final status: IMPLEMENTATION_MERGED, V3_FORENSIC_REVIEW_COMPLETE, ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS, ATOMIC_STAGE_DECISION_PASS, SCORE_SCALE_PASS, STAGE_SEMANTICS_PASS, SEMANTIC_PRIMITIVE_GUARD_PASS, DAILY_EVENT_FULL_THESIS_SEPARATION_PASS, CENSUS_ASSESSMENT_CANDIDATE_EVENT_SEPARATION_PASS, FULL_THESIS_SMOKE_HONESTY_PASS, FULL_THESIS_SMOKE_EXECUTION_PASS, FULL_THESIS_SMOKE_PASS, FULL_THESIS_SMOKE_REQUIREMENT_PASS_BY_EXTERNAL_CONTROLLED_SMOKE, FULL_THESIS_PRODUCTION_CANNOT_SUBSTITUTE_SMOKE, FULL_THESIS_REFRESH_QUEUE_PRESENT, FULL_THESIS_SEED_LEDGER_INTEGRITY_PASS, FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS, FULL_THESIS_SEED_PROMOTION_PASS, FULL_THESIS_SEED_ACTUAL_MATERIALIZATION_PASS, BRAIN_WEB_ATTEMPT_RECORDED, BRAIN_STAGE_PROMOTION_AUDITED, BRAIN_WEB_READINESS_GATE_AUDITED, OFFICIAL_BASELINE_EVIDENCE_CLAIM_PAYLOAD_PRESENT, KNOWN_BAD_REGRESSION_PASS, SELF_REPAIR_LOOP_PASS, RESEARCH_BRAIN_V4_REPORT_BRIDGE_IMPORTED, BRAIN_WEB_EVIDENCE_PASS
2. Commit SHA / message / push status / working tree: report_generation_sha=804ded83c1ce0e17145d2fcacce915cf02bae804; push_status=not_pushed_by_runner
3. Test artifact command: python -m unittest discover -s tests -v
   Test log summary: not_run_by_census_v4_runner
   Test artifact duration_seconds: 380.5103
   Test evidence audit: MACHINE_READABLE_TEST_ARTIFACT_PASS; artifact_exists=True; artifact_test_count=5190
4. Target gate: full_thesis; target_gate_pass=True; target_gate_verdict=TARGET_GATE_PASS
5. Goal completion audit: goal_completion_ready=True; blockers=[]
5a. Full thesis production audit: FULL_THESIS_PRODUCTION_PASS; production_pass_allowed=True; production_mode_requested=True; refresh_queue_candidates=62; production_rows=10; controlled_smoke_rows=0; controlled_smoke_rejected=0; blockers=[]
5b. C06 guard replay audit: guard_replay_pass=True; guard_cases=3/3; blockers=[]
5c. Controlled semantic replay audit: pass=True; cases=10/10; pending=0; blockers=[]
5d. Full thesis smoke gate: honesty_pass=True; execution_pass=True; legacy_smoke_pass=True; gate_pass_allowed=False; gate_blockers=['full_thesis_smoke_gate_not_requested', 'controlled_smoke_not_allowed_for_production_run_mode', 'controlled_smoke_requires_brain_web_disabled']
5e. Goal requirement matrix: minimum_pass=True; pass=22/22; pending=0; fail=0; blockers=[]
6. Run mode: BRAIN_AND_WEB_ACQUISITION_ENABLED
7. Leaf artifact audit: PASS
8. Eligible / Stage rows: 3391 / 3391
9. Base/display stage distribution: {'0': 18, '1': 4, '2': 1, 'Red': 1, 'Stage0': 3306, 'Stage1': 44, 'Stage2-Watch': 17}
10. Stage signal distribution: {'BRAIN_OFFICIAL_CLAIM_BACKED_STAGE': 10, 'BRAIN_WEB_CLAIM_BACKED_STAGE': 3, 'EVIDENCE_INSUFFICIENT': 9, 'FULL_THESIS_PRODUCTION_STAGE': 10, 'MATERIAL_CLAIM_WATCH': 17, 'NO_CURRENT_CATALYST': 3306, 'OFFICIAL_EVENT_WATCH': 27, 'RISK_REVIEW': 1, 'SOURCE_PENDING': 8}
11. Score scale distribution: {'EVENT_WEIGHTED_PARTIAL': 58, 'FULL_E2R_100': 10, 'NO_SCORE': 3323}
12. Stage scope distribution: {'BRAIN_OFFICIAL_PARTIAL': 10, 'BRAIN_WEB_PARTIAL': 3, 'CENSUS_EVENT_BOARD': 3368, 'FULL_THESIS': 10}
13. Score scope distribution: {'BRAIN_OFFICIAL_CLAIM_BACKED_PARTIAL': 10, 'BRAIN_WEB_CLAIM_BACKED_PARTIAL': 3, 'EVENT_WEIGHTED_PARTIAL': 45, 'FULL_E2R_100': 10, 'NO_SCORE': 3323}
14. Operator stage use distribution: {'FULL_THESIS_STAGE': 10, 'NOT_FULL_THESIS_STAGE': 3381}
15. Operator score use distribution: {'FULL_E2R_SCORE': 10, 'NOT_FULL_E2R_SCORE': 3381}
16. Event evidence score rows: 58
17. Full E2R verified score rows: 10
17a. Full thesis stage rows: 10; refresh queue candidates: 62; event-board non-Stage0 rows: 62; operator_stage_scope_notice=FULL_THESIS_STAGE_ROWS_PRESENT_SCOPE_GUARD_REQUIRED
18. Candidate event scope distribution: {'ASSESSMENT_ONLY': 3306, 'CANDIDATE_EVENTS_PRESENT': 85}
19. Candidate event count: 236
20. Score eligible candidate event count: 102
21. Planner rows: 350; real LLM planner calls=45; real_success=35; not_attempted=305
22. LLM planner real-provider success: 35
23. Brain/Web attempt verdict: ATTEMPTED_WITH_SOURCE_TASKS; source_tasks=278; accepted_claims=216
24. Brain Stage promotion verdict: PROMOTION_APPLIED; promoted=23; unsafe_promoted=0; snapshot_docs=0
25. Brain/Web readiness gate: READY_FOR_BRAIN_WEB_EVIDENCE_PASS; pass_allowed=True; minimum_gate_applies=True; operational_minimum_count_gate_applies=True; minimum_required_counts={'llm_claim_extractor_attempt_count': 10, 'llm_planner_call_count': 30, 'official_first_violation_count': 0, 'web_fetched_document_count': 10, 'web_or_llm_accepted_claim_count': 3, 'web_search_call_count': 20, 'web_search_task_count': 20}; blockers=0; connectivity_missing=0
26. Web search tasks: 31
27. Claim extractor runs: 45
28. Evidence claim payload rows: 213
29. Non-representative claim audit: PASS; critical_count=0; warning_count=85; representative_claims=89; non_representative_claims=124; reason_distribution={'accepted_claim_without_atomic_decision': 85, 'non_representative_atomic_decision': 39}
30. Research Brain bridge verdict: SHADOW_OR_IMPORT_ONLY; usable_for_census_cutover=False; snapshot_url_count=255
31. Claim-to-stage forensic audit: PASS; critical_count=0; scored_rows=68
32. Source task realness audit: LIVE_SOURCE_PASS; scope=LEDGER_REFRESH_REALNESS_PASS; live_source_pass_allowed=True; claim_producing=81; real_fetch=21; fresh_cache=60; lifecycle_refresh=32
33. Source task satisfaction audit: PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION; scope=LEDGER_REFRESH_SOURCE_TASK_SATISFACTION_PASS; live_source_task_satisfaction_pass_allowed=False; critical_count=0; warning_count=124; representative_score_claims=89; chain_closed_to_representative_stage=153; non_representative_source_task_claims=124; baseline_only_score_claims=32
34. Primitive state chain audit: PASS; critical_count=0; representative_score_claims=89; representative_score_claims_with_primitive=89; primitive_states=269; primitive_mappings=137; mapping_leaf_resolution_supported=True
35. Existing ledger reuse audit: PASS; reused_claims=92; new_brain_web_claims=121
36. Last effective thesis audit: PASS; status_distribution={'ACTIVE_THESIS': 74, 'NEEDS_REFRESH': 3, 'NO_KNOWN_THESIS': 3306, 'SOURCE_PENDING': 8}
37. Source coverage audit: PASS_LEDGER_REFRESH_COVERAGE; live_source_coverage_pass=False; cutover_replay_only_symbols=68
38. Runtime plausibility audit: PASS_LIVE_RUNTIME_PLAUSIBILITY; runtime_mode=BRAIN_AND_WEB_ACQUISITION_ENABLED; provider_calls=21; llm_calls=35
39. Sample leaf bundle rows: 68
40. Report generation source: leaf_artifact_audit.json + readiness_verdict.json; report_generated_from_leaf_audit=true
41. Static production path audit:
    legacy_runner_production_reachable_count=0
    legacy_v3_runner_production_reachable_count=0
    empty_claims_stage_builder_production_count=0
    old_cli_can_claim_pass_count=0
    official_cli_not_v4_runner_count=0
    sample_bundle_missing_scored_row_count=0
42. Final verdict: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
43. Output root: output/census_v4/2026-07-01-v177-goal-followup-production-after-expanded-brain-web-width
44. runtime_seconds: 3939.15

Note: v4 does not claim Meaningful Operational Stage or Brain/Web evidence pass unless the required leaf artifacts exist.
