# E2R Meaningful Scoring Readiness Verdict

- final status: MEANINGFUL_E2R_SCORING_NOT_READY
- pass-only final label: MEANINGFUL_E2R_SCORING_READY_V2
- as_of_date: 2026-07-11
- mandatory targets: 2
- organic accepted claims: 0
- organic validated impacts: 0
- organic verified component points: 0.0
- full score valid canaries: 0
- critical_count_sum: 151
- blockers: ['005930:required_dossier_leaf_missing_count', '005930:organic_accepted_claim_missing', '005930:organic_validated_impact_missing', '005930:organic_verified_component_points_missing', '005930:calibrated_profile_missing', '005930:calibrated_profile_mismatch', '005930:no_score_only_decision', '005930:component_coverage_mismatch', '005930:component_vector_coverage_mismatch', '005930:full_score_invalid', '005930:score_type_not_full_e2r_100', '005930:component_sum_total_mismatch', '005930:stagecourt_trace_missing', '005930:decision_target_mismatch', '005930:decision_as_of_date_mismatch', '005930:score_archetype_mismatch', '005930:missing_scoring_policy_count', '005930:silent_zero_default_count', '005930:positive_impact_zeroed_by_missing_cap_count', '005930:counter_impact_zeroed_by_missing_cap_count', '005930:cross_business_question_closure_count', '005930:supported_question_absent_component_count', '005930:positive_claim_absent_component_count', '005930:absence_with_inadequate_search_count', '005930:counter_impact_ignored_count', '005930:same_fact_duplicate_credit_count', '005930:same_document_duplicate_credit_count', '005930:claim_count_event_boost_count', '005930:eligibility_contradiction_count', '005930:critical_material_fact_miss_count', '005930:v3_semantic_leaf_missing_count', '005930:full_score_validity_v2_failure_count', '000660:required_dossier_leaf_missing_count', '000660:organic_accepted_claim_missing', '000660:organic_validated_impact_missing', '000660:organic_verified_component_points_missing', '000660:calibrated_profile_missing', '000660:calibrated_profile_mismatch', '000660:no_score_only_decision', '000660:component_coverage_mismatch', '000660:component_vector_coverage_mismatch', '000660:full_score_invalid', '000660:score_type_not_full_e2r_100', '000660:component_sum_total_mismatch', '000660:stagecourt_trace_missing', '000660:decision_target_mismatch', '000660:decision_as_of_date_mismatch', '000660:score_archetype_mismatch', '000660:missing_scoring_policy_count', '000660:silent_zero_default_count', '000660:positive_impact_zeroed_by_missing_cap_count', '000660:counter_impact_zeroed_by_missing_cap_count', '000660:cross_business_question_closure_count', '000660:supported_question_absent_component_count', '000660:positive_claim_absent_component_count', '000660:absence_with_inadequate_search_count', '000660:counter_impact_ignored_count', '000660:same_fact_duplicate_credit_count', '000660:same_document_duplicate_credit_count', '000660:claim_count_event_boost_count', '000660:eligibility_contradiction_count', '000660:critical_material_fact_miss_count', '000660:v3_semantic_leaf_missing_count', '000660:full_score_validity_v2_failure_count', 'global:frozen_52f09f3_repair:audit_leaf_missing', 'global:semantic_scoring_known_bad:audit_leaf_missing', 'global:semantic_scoring_reviewer_gate:audit_leaf_missing']
- research-grade acquisition: RESEARCH_GRADE_EVIDENCE_ACQUISITION_PASS
- legacy READY alias active: false
- readiness v3 required: false
- v2 deprecated: true
- investment recommendation emitted: false

## Mandatory Target Gates

- 005930 (삼성전자): CANONICAL_FULL_THESIS_NOT_READY; claims=0, impacts=0, points=0.0, score_type=None
- 000660 (SK하이닉스): CANONICAL_FULL_THESIS_NOT_READY; claims=0, impacts=0, points=0.0, score_type=None

## Required Global Audits

- live_materialization: FULL_LIVE_ACCEPTANCE_PASS; critical=0
- scoring_schema_totality: SCORING_SCHEMA_TOTALITY_PASS; critical=0
- impact_validator_v2: STRICT_IMPACT_VALIDATOR_V2_PASS; critical=0
- business_mechanism_scope: BUSINESS_MECHANISM_SCOPE_PASS; critical=0
- question_component_reconciliation: QUESTION_COMPONENT_RECONCILIATION_PASS; critical=0
- counter_component: COUNTER_COMPONENT_MATH_PASS; critical=0
- fact_document_dedupe: FACT_DOCUMENT_DEDUPE_PASS; critical=0
- full_thesis_event_separation: STAGECOURT_EVENT_SEPARATION_PASS; critical=0
- claim_eligibility: CLAIM_ELIGIBILITY_PLANES_PASS; critical=0
- research_quality_gold: BLIND_RESEARCH_QUALITY_PASS; critical=0
- evidence_search_adequacy: EVIDENCE_SEARCH_ADEQUACY_PASS; critical=0
- question_impact_contract: QUESTION_IMPACT_CONTRACT_PASS; critical=0
- full_score_validity_v2: FULL_SCORE_VALIDITY_V2_AUDIT_PASS; critical=0
- frozen_52f09f3_repair: None; critical=1
- c06_historical_component_replay: C06_HISTORICAL_COMPONENT_REPLAY_PASS; critical=0
- evidence_to_score_generalization: EVIDENCE_TO_SCORE_GENERALIZATION_PASS; critical=0
- semantic_scoring_known_bad: None; critical=1
- semantic_scoring_reviewer_gate: None; critical=1

## Semantic Critical Counts

- missing_scoring_policy_count: 2
- silent_zero_default_count: 2
- positive_impact_zeroed_by_missing_cap_count: 2
- counter_impact_zeroed_by_missing_cap_count: 2
- cross_business_question_closure_count: 2
- supported_question_absent_component_count: 2
- positive_claim_absent_component_count: 2
- absence_with_inadequate_search_count: 2
- counter_impact_ignored_count: 2
- same_fact_duplicate_credit_count: 2
- same_document_duplicate_credit_count: 2
- claim_count_event_boost_count: 2
- eligibility_contradiction_count: 2
- critical_material_fact_miss_count: 2

## Repository Verification

- status: NOT_VERIFIED_IN_THIS_RUN
- repo_dirty: None
- head_origin_same_commit: None

## Exact Final Verdict

MEANINGFUL_E2R_SCORING_NOT_READY
