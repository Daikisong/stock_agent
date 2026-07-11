# E2R Semantic Scoring v2 Forensic Baseline

- status: SEMANTIC_SCORING_V2_FORENSIC_BASELINE_CAPTURED
- frozen input: 52f09f3 Samsung/Hynix dossier leaves
- baseline hash: d2ae9eae2aca95ffd99350855e3e7ff72835b0f605172aceb66df5f921243e50
- production ready: false

## Measured defects

- declared_support_type_count: 7
- cap_table_support_type_count: 4
- missing_support_type_count: 3
- source_cap_missing_count: 0
- temporal_cap_missing_count: 0
- positive_proposal_zeroed_by_missing_cap_count: 9
- counter_proposal_zeroed_by_missing_cap_count: 1
- supported_question_absent_component_count: 6
- partially_supported_question_absent_component_count: 2
- cross_business_question_closure_count: 22
- same_document_duplicate_credit_group_count: 6
- same_document_duplicate_credit_count: 22
- same_fact_duplicate_credit_group_count: 0
- same_fact_duplicate_credit_count: 0
- support_counter_component_counter_effect_zero_count: 1
- accepted_claim_event_score_injection_count: 2
- eligibility_field_contradiction_count: 39

## 쉬운 예

`PARTIAL_BRIDGE` impact는 proposal과 ledger에 존재하지만 cap table에 key가 없어 0점이 됐다. 이는 근거가 약해서 0점인 것이 아니라 lookup 계약이 빠진 내부 오류다.

삼성 Tesla Foundry 위탁생산 계약은 삼성전자 claim 장부에는 남길 수 있지만, HBM 고객 배정 질문을 닫아서는 안 된다.

## Exact baseline rows

- positive impacts silently zeroed: 9
- counter impacts silently zeroed: 1
- question/component contradictions: 8
- mechanism-scope failures: 22
- same-document duplicate-credit groups: 6
- accepted-claim event injections: 2
- eligibility contradictions: 39

이 문서는 결함이 해결됐다는 PASS가 아니라, Phase 59+ 수리 전 결함을 같은 frozen corpus에서 재현한 기준선이다.
