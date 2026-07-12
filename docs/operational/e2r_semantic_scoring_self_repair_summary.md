# E2R Semantic Scoring Self-Repair Summary

- status: SELF_REPAIR_RESOLVED
- as_of_date: 2026-07-11
- iterations: 12/12
- critical_count_sum: 0
- unresolved internal failure classes: []
- external provider blockers: []
- threshold 완화 / synthetic claim / expected score hardcode / gold injection / fixture-as-live / report-only repair: 0

쉬운 예: `SUPPORTED` 질문이 있는데 실제 component credit이 0이면 문구만 PASS로 바꾸지 않는다. 관련 코드 커밋, 방어 테스트, 같은 frozen corpus, live production, blind gold 비교가 모두 맞아야 수리 완료다.

## Final frozen · live · gold snapshot

- snapshot_id: `1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7`
- frozen: FROZEN_52F09F3_REPAIR_PASS; critical=0; new_document=0
- live: LIVE_SEMANTIC_SCORING_PASS; valid targets=2/2
- gold: BLIND_RESEARCH_QUALITY_PASS; critical recall=1.0; leakage=0
- search adequacy: questions=26; critical=0
- known-bad: SEMANTIC_SCORING_KNOWN_BAD_PASS; 35/35
- generalization: EVIDENCE_TO_SCORE_GENERALIZATION_PASS; critical=0
- 005930: claims=18, impacts=37, subcriteria=26, score=18.159977, score_type=FULL_E2R_100, Stage=0, decision=FINAL
- 000660: claims=33, impacts=115, subcriteria=26, score=19.120509, score_type=FULL_E2R_100, Stage=0, decision=FINAL

## Code-repair iterations

### Iteration 1

- iteration: 1
- target: all archetypes
- failure class: SILENT_ZERO_CAP
- related failure classes: ['SCORING_SCHEMA_INCOMPLETE']
- root cause file/function/config: `configs/e2r_scoring_policy_v2.json:support_type_policies`
- before metrics: `{"counter_missing_cap_zero_count":1,"missing_support_type_count":3,"positive_missing_cap_zero_count":9}`
- patch commit: `ad568c7af2ccf0c35554b1fec15f79ba03a001bf` Phase 59 scoring cap 전수성과 silent-zero 금지 구현
- focused tests: `["tests.test_scoring_schema_totality.ScoringSchemaTotalityTests.test_operational_totality_audit_has_no_critical_count","tests.test_partial_bridge_nonzero_policy.PartialBridgeNonzeroPolicyTests.test_partial_bridge_has_research_backed_nonzero_cap"]` → PASS
- frozen corpus rerun: `{"critical_count_sum":0,"new_document_count":0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"FROZEN_52F09F3_REPAIR_PASS"}`
- live production rerun: `{"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"LIVE_SEMANTIC_SCORING_PASS","target_count":2,"valid_target_count":2}`
- gold comparison: `{"critical_count_sum":0,"critical_fact_recall":1.0,"noncritical_fact_recall":1.0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"BLIND_RESEARCH_QUALITY_PASS"}`
- after metrics: `{"all_archetype_schema_total":36,"missing_scoring_policy_count":0,"silent_zero_default_count":0}`
- metric source: `docs/operational/e2r_semantic_scoring_v2_forensic_baseline.md`
- repair: 누락 cap을 0점 기본값으로 처리하지 않고 total policy 또는 hard error로 바꿨다.
- resolved/unresolved: RESOLVED

### Iteration 2

- iteration: 2
- target: 005930 and all archetypes
- failure class: WRONG_MECHANISM_SCOPE
- related failure classes: []
- root cause file/function/config: `src/e2r/research_brain/scoring/business_mechanism_scope.py:MechanismScopeValidator`
- before metrics: `{"cross_business_question_closure_count":22}`
- patch commit: `ad55168e02edb2aec0adf9309d70fe472801b6fb` Phase 60 동일 회사 내 사업부·제품 메커니즘 scope 검증 구현
- focused tests: `["tests.test_business_mechanism_scope.BusinessMechanismScopeTests.test_same_issuer_wrong_segment_is_rejected_and_rerouted","tests.test_foundry_not_hbm_allocation.FoundryNotHBMAllocationTests.test_tesla_foundry_claim_stays_global_but_c06_impact_is_rerouted"]` → PASS
- frozen corpus rerun: `{"critical_count_sum":0,"new_document_count":0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"FROZEN_52F09F3_REPAIR_PASS"}`
- live production rerun: `{"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"LIVE_SEMANTIC_SCORING_PASS","target_count":2,"valid_target_count":2}`
- gold comparison: `{"critical_count_sum":0,"critical_fact_recall":1.0,"noncritical_fact_recall":1.0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"BLIND_RESEARCH_QUALITY_PASS"}`
- after metrics: `{"cross_business_question_closure_count":0,"foundry_hbm_scope_violation_count":0}`
- metric source: `docs/operational/e2r_semantic_scoring_v2_forensic_baseline.md`
- repair: issuer가 같아도 Foundry·기판·메모리 메커니즘을 분리하고 잘못된 impact를 reroute했다.
- resolved/unresolved: RESOLVED

### Iteration 3

- iteration: 3
- target: claim scoring planes
- failure class: ELIGIBILITY_CONTRADICTION
- related failure classes: []
- root cause file/function/config: `src/e2r/research_brain/scoring/claim_eligibility.py:compile_claim_eligibility_decisions`
- before metrics: `{"legacy_boolean_contradiction_count":39}`
- patch commit: `9ad5938c8df8863d052362b3d820727cbd21c09e` Phase 61 claim 장부·질문·점수·Stage eligibility 분리
- focused tests: `["tests.test_claim_eligibility_decision.ClaimEligibilityDecisionTests.test_accepted_claim_does_not_automatically_enter_every_plane"]` → PASS
- frozen corpus rerun: `{"critical_count_sum":0,"new_document_count":0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"FROZEN_52F09F3_REPAIR_PASS"}`
- live production rerun: `{"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"LIVE_SEMANTIC_SCORING_PASS","target_count":2,"valid_target_count":2}`
- gold comparison: `{"critical_count_sum":0,"critical_fact_recall":1.0,"noncritical_fact_recall":1.0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"BLIND_RESEARCH_QUALITY_PASS"}`
- after metrics: `{"component_score_without_eligibility_decision_count":0,"implicit_stage_event_eligibility_count":0}`
- metric source: `docs/operational/e2r_claim_eligibility_audit.json`
- repair: accepted 하나로 모든 plane을 열던 boolean을 목적별 deterministic decision으로 분리했다.
- resolved/unresolved: RESOLVED

### Iteration 4

- iteration: 4
- target: 005930 and 000660 gold lane
- failure class: GOLD_MATERIAL_FACT_MISSED
- related failure classes: []
- root cause file/function/config: `src/e2r/research_brain/research_quality/blind_benchmark.py:compile_blind_benchmark`
- before metrics: `{"post_run_blind_gold_lane_count":0}`
- patch commit: `b2cb36d2c10ec5f6c755e5a3c86585af4f73cfbc` Phase 63 독립 deep-research 기준과 운영 조사 recall 검증 구현
- focused tests: `["tests.test_gold_research_blindness.GoldResearchBlindnessTests.test_isolated_lanes_pass_without_gold_input_leakage"]` → PASS
- frozen corpus rerun: `{"critical_count_sum":0,"new_document_count":0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"FROZEN_52F09F3_REPAIR_PASS"}`
- live production rerun: `{"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"LIVE_SEMANTIC_SCORING_PASS","target_count":2,"valid_target_count":2}`
- gold comparison: `{"critical_count_sum":0,"critical_fact_recall":1.0,"noncritical_fact_recall":1.0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"BLIND_RESEARCH_QUALITY_PASS"}`
- after metrics: `{"gold_leakage_count":0,"post_run_blind_gold_lane_count":1}`
- metric source: `docs/operational/e2r_research_quality_gold_audit.json`
- repair: production이 보지 못하는 사후 gold lane과 material-fact 비교를 추가했다.
- resolved/unresolved: RESOLVED

### Iteration 5

- iteration: 5
- target: question-family acquisition
- failure class: EVIDENCE_SEARCH_INADEQUATE
- related failure classes: []
- root cause file/function/config: `src/e2r/research_brain/research_quality/search_adequacy.py:compile_search_adequacy`
- before metrics: `{"question_level_adequacy_leaf_count":0}`
- patch commit: `116650aae74134033e992f446bd6a5436e29763b` Phase 64 question별 source saturation과 research-grade 문서선택 구현
- focused tests: `["tests.test_absence_requires_adequate_search.AbsenceRequiresAdequateSearchTests.test_budget_exhaustion_is_pending_never_absence"]` → PASS
- frozen corpus rerun: `{"critical_count_sum":0,"new_document_count":0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"FROZEN_52F09F3_REPAIR_PASS"}`
- live production rerun: `{"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"LIVE_SEMANTIC_SCORING_PASS","target_count":2,"valid_target_count":2}`
- gold comparison: `{"critical_count_sum":0,"critical_fact_recall":1.0,"noncritical_fact_recall":1.0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"BLIND_RESEARCH_QUALITY_PASS"}`
- after metrics: `{"inadequate_absence_count":0,"question_level_adequacy_leaf_count":26}`
- metric source: `docs/operational/e2r_evidence_search_adequacy_audit.json`
- repair: provider 실패·budget 소진·미조사를 absence와 분리하고 route별 search proof를 남겼다.
- resolved/unresolved: RESOLVED

### Iteration 6

- iteration: 6
- target: frozen Samsung/Hynix impact ledger
- failure class: POSITIVE_IMPACT_ERASED
- related failure classes: ['FACT_DUPLICATE_CREDIT', 'DOCUMENT_DUPLICATE_CREDIT']
- root cause file/function/config: `src/e2r/research_brain/scoring/impact_validator.py:ImpactValidator.validate`
- before metrics: `{"positive_impact_zeroed_by_missing_cap_count":9,"same_document_duplicate_credit_count":22}`
- patch commit: `9dbe92b395ab8274e505bb1ac491908b0277828c` Phase 67 silent-zero 제거와 fact·document 중복점수 차단
- focused tests: `["tests.test_fact_cluster_dedupe.FactClusterDedupeTests.test_same_economic_fact_across_claims_and_documents_gets_one_credit","tests.test_document_cluster_credit_cap.DocumentClusterCreditCapTests.test_same_document_claim_fragments_do_not_stack_information_confidence"]` → PASS
- frozen corpus rerun: `{"critical_count_sum":0,"new_document_count":0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"FROZEN_52F09F3_REPAIR_PASS"}`
- live production rerun: `{"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"LIVE_SEMANTIC_SCORING_PASS","target_count":2,"valid_target_count":2}`
- gold comparison: `{"critical_count_sum":0,"critical_fact_recall":1.0,"noncritical_fact_recall":1.0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"BLIND_RESEARCH_QUALITY_PASS"}`
- after metrics: `{"positive_impact_zeroed_by_missing_cap_count":0,"same_document_duplicate_credit_count":0,"same_fact_duplicate_credit_count":0}`
- metric source: `docs/operational/e2r_semantic_scoring_v2_forensic_baseline.md`
- repair: 유효 impact를 cap 누락으로 지우지 않고 fact/document cluster 단위로 중복 credit만 억제했다.
- resolved/unresolved: RESOLVED

### Iteration 7

- iteration: 7
- target: component support/counter plane
- failure class: COUNTER_EFFECT_IGNORED
- related failure classes: []
- root cause file/function/config: `src/e2r/research_brain/scoring/counter_component_math.py:compile_counter_component_math`
- before metrics: `{"support_counter_component_counter_effect_zero_count":1}`
- patch commit: `5045fd98878ba485193fd042c7c2f67adf29c570` Phase 69 support·counter·resolution을 component 점수에 동시 반영
- focused tests: `["tests.test_counter_component_math.CounterComponentMathTests.test_capacity_counter_in_another_subcriterion_caps_same_component"]` → PASS
- frozen corpus rerun: `{"critical_count_sum":0,"new_document_count":0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"FROZEN_52F09F3_REPAIR_PASS"}`
- live production rerun: `{"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"LIVE_SEMANTIC_SCORING_PASS","target_count":2,"valid_target_count":2}`
- gold comparison: `{"critical_count_sum":0,"critical_fact_recall":1.0,"noncritical_fact_recall":1.0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"BLIND_RESEARCH_QUALITY_PASS"}`
- after metrics: `{"counter_impact_ignored_count":0,"resolution_penalty_retained_count":0}`
- metric source: `docs/operational/e2r_counter_component_audit.json`
- repair: support와 counter를 동시에 보존하고 연결된 resolution만 이전 감점을 해제하게 했다.
- resolved/unresolved: RESOLVED

### Iteration 8

- iteration: 8
- target: question/claim/impact/component chain
- failure class: QUESTION_COMPONENT_INCONSISTENCY
- related failure classes: []
- root cause file/function/config: `src/e2r/research_brain/scoring/semantic_closure_reconciler.py:SemanticClosureReconciler.reconcile`
- before metrics: `{"question_component_contradiction_count":8}`
- patch commit: `2966a47051868919b9881c0a2fc6b95425557659` Phase 70 질문·claim·impact·component semantic closure 원자검증
- focused tests: `["tests.test_semantic_closure_reconciler.SemanticClosureReconcilerTests.test_supported_scoring_without_credit_is_pipeline_error"]` → PASS
- frozen corpus rerun: `{"critical_count_sum":0,"new_document_count":0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"FROZEN_52F09F3_REPAIR_PASS"}`
- live production rerun: `{"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"LIVE_SEMANTIC_SCORING_PASS","target_count":2,"valid_target_count":2}`
- gold comparison: `{"critical_count_sum":0,"critical_fact_recall":1.0,"noncritical_fact_recall":1.0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"BLIND_RESEARCH_QUALITY_PASS"}`
- after metrics: `{"positive_claim_absent_component_count":0,"supported_question_zero_credit_count":0}`
- metric source: `docs/operational/e2r_question_component_reconciliation_audit.json`
- repair: SUPPORTED 문구와 실제 nonzero bounded credit를 같은 lineage에서 원자 대조했다.
- resolved/unresolved: RESOLVED

### Iteration 9

- iteration: 9
- target: deterministic StageCourt
- failure class: EVENT_STAGE_INJECTION
- related failure classes: []
- root cause file/function/config: `src/e2r/research_brain/scoring/stagecourt_event_separation.py:audit_stagecourt_event_separation`
- before metrics: `{"accepted_claim_event_score_injection_count":2}`
- patch commit: `77a866c7ec18a10c9bd20fe829b0ce5f2b3ddd08` Phase 71 full-thesis Stage와 daily event overlay 완전 분리
- focused tests: `["tests.test_stagecourt_event_separation.StageCourtEventSeparationTests.test_claim_count_and_event_overlay_never_change_full_thesis_stage"]` → PASS
- frozen corpus rerun: `{"critical_count_sum":0,"new_document_count":0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"FROZEN_52F09F3_REPAIR_PASS"}`
- live production rerun: `{"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"LIVE_SEMANTIC_SCORING_PASS","target_count":2,"valid_target_count":2}`
- gold comparison: `{"critical_count_sum":0,"critical_fact_recall":1.0,"noncritical_fact_recall":1.0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"BLIND_RESEARCH_QUALITY_PASS"}`
- after metrics: `{"claim_count_event_boost_count":0,"event_overlay_stage_injection_count":0}`
- metric source: `docs/operational/e2r_stagecourt_event_separation_audit.json`
- repair: daily event overlay는 모니터링 plane에만 남기고 full-thesis Stage 입력에서 제거했다.
- resolved/unresolved: RESOLVED

### Iteration 10

- iteration: 10
- target: full score and Stage trace
- failure class: FULL_SCORE_INVALID
- related failure classes: ['STAGE_TRACE_MISMATCH']
- root cause file/function/config: `src/e2r/research_brain/scoring/full_score_validity.py:compile_full_score_validity_evidence_v2`
- before metrics: `{"semantic_full_score_gate_count":0}`
- patch commit: `d120dd1ed460a0193f780cf5d78183e176726757` Phase 72 semantic 일관성을 포함한 full score validity v2 구현
- focused tests: `["tests.test_full_score_validity_v2.FullScoreValidityV2Tests.test_invalid_semantics_preserve_verified_score_and_interval","tests.test_atomic_stagecourt_component_trace.AtomicStageCourtComponentTraceTests.test_score_impact_lineage_mismatch_is_rejected"]` → PASS
- frozen corpus rerun: `{"critical_count_sum":0,"new_document_count":0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"FROZEN_52F09F3_REPAIR_PASS"}`
- live production rerun: `{"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"LIVE_SEMANTIC_SCORING_PASS","target_count":2,"valid_target_count":2}`
- gold comparison: `{"critical_count_sum":0,"critical_fact_recall":1.0,"noncritical_fact_recall":1.0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"BLIND_RESEARCH_QUALITY_PASS"}`
- after metrics: `{"full_score_valid_with_semantic_failure_count":0,"semantic_full_score_gate_count":13,"stage_trace_mismatch_count":0}`
- metric source: `docs/operational/e2r_full_score_validity_v2_audit.json`
- repair: semantic gate가 하나라도 실패하면 raw 참고점수는 보존하되 full score와 Stage 확정을 막았다.
- resolved/unresolved: RESOLVED

### Iteration 11

- iteration: 11
- target: frozen 52f09f3 Samsung/Hynix corpus
- failure class: POSITIVE_IMPACT_ERASED
- related failure classes: ['WRONG_MECHANISM_SCOPE', 'COUNTER_EFFECT_IGNORED']
- root cause file/function/config: `configs/e2r_frozen_52f09f3_repair_v1.json:target repair contracts`
- before metrics: `{"foundry_hbm_cross_wire_present":1,"partial_bridge_missing_cap_zero_present":1}`
- patch commit: `126975022add8aa075c88007385ac83e64230333` Phase 74 동일 corpus에서 하이닉스 0점 소거와 삼성 사업부 오매핑 수리 증명
- focused tests: `["tests.test_frozen_52f09f3_repair.Frozen52f09f3RepairTests.test_no_silent_zero_or_semantic_internal_error_remains"]` → PASS
- frozen corpus rerun: `{"critical_count_sum":0,"new_document_count":0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"FROZEN_52F09F3_REPAIR_PASS"}`
- live production rerun: `{"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"LIVE_SEMANTIC_SCORING_PASS","target_count":2,"valid_target_count":2}`
- gold comparison: `{"critical_count_sum":0,"critical_fact_recall":1.0,"noncritical_fact_recall":1.0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"BLIND_RESEARCH_QUALITY_PASS"}`
- after metrics: `{"foundry_hbm_scope_violation_count":0,"new_document_count":0,"partial_bridge_missing_cap_zero_count":0}`
- metric source: `docs/operational/e2r_frozen_52f09f3_repair_audit.json`
- repair: 문서를 추가하지 않고 같은 corpus에서 Hynix nonzero effect와 Samsung Foundry 제외를 재컴파일했다.
- resolved/unresolved: RESOLVED

### Iteration 12

- iteration: 12
- target: live 005930 and 000660
- failure class: GOLD_MATERIAL_FACT_MISSED
- related failure classes: ['EVIDENCE_SEARCH_INADEQUATE']
- root cause file/function/config: `configs/e2r_agentic_evidence_contracts_v2.json:C06 semantic evidence aliases`
- before metrics: `{"live_full_score_valid_target_count":0}`
- patch commit: `37ff52e3b5627e513f6e1d6e155e1dae476d569d` Phase 75 삼성전자·하이닉스 blind deep-research와 semantic scoring 재검증
- focused tests: `["tests.test_samsung_hynix_semantic_scoring_v2.SamsungHynixSemanticScoringV2Tests.test_both_live_dossiers_are_full_deterministic_terminal_scores","tests.test_gold_material_fact_recall.GoldMaterialFactRecallTests.test_operational_audit_is_live_samsung_hynix_not_fixture"]` → PASS
- frozen corpus rerun: `{"critical_count_sum":0,"new_document_count":0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"FROZEN_52F09F3_REPAIR_PASS"}`
- live production rerun: `{"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"LIVE_SEMANTIC_SCORING_PASS","target_count":2,"valid_target_count":2}`
- gold comparison: `{"critical_count_sum":0,"critical_fact_recall":1.0,"noncritical_fact_recall":1.0,"snapshot_id":"1ccb2b66c3c3e2ebebe75b16003dd6c20adcfd56d375c1d1107474d8b83ee7c7","status":"BLIND_RESEARCH_QUALITY_PASS"}`
- after metrics: `{"critical_gold_material_fact_miss_count":0,"live_full_score_valid_target_count":2,"search_adequacy_critical_count_sum":0}`
- metric source: `output/evidence_to_score_v2/live_2026-07-11`
- repair: blind production을 다시 실행해 두 종목 모두 terminal FULL_E2R_100과 gold recall 1.0을 확인했다.
- resolved/unresolved: RESOLVED

## Failure-class closure

- SCORING_SCHEMA_INCOMPLETE: RESOLVED
- SILENT_ZERO_CAP: RESOLVED
- WRONG_MECHANISM_SCOPE: RESOLVED
- ELIGIBILITY_CONTRADICTION: RESOLVED
- QUESTION_COMPONENT_INCONSISTENCY: RESOLVED
- POSITIVE_IMPACT_ERASED: RESOLVED
- COUNTER_EFFECT_IGNORED: RESOLVED
- FACT_DUPLICATE_CREDIT: RESOLVED
- DOCUMENT_DUPLICATE_CREDIT: RESOLVED
- EVENT_STAGE_INJECTION: RESOLVED
- EVIDENCE_SEARCH_INADEQUATE: RESOLVED
- GOLD_MATERIAL_FACT_MISSED: RESOLVED
- FULL_SCORE_INVALID: RESOLVED
- STAGE_TRACE_MISMATCH: RESOLVED
- EXTERNAL_PROVIDER_BLOCKER: NOT_OBSERVED

## Exact verdict

SELF_REPAIR_RESOLVED
