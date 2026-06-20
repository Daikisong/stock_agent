# V12 Goal Scope Evidence Audit

이 문서는 원래 질문을 요구사항으로 쪼개서, 0619 산출물이 무엇을 증명했고 무엇이 아직 구현 과제인지 정리한다.
점수나 stage를 바꾸는 문서가 아니라 진단 범위 감사표다.

## Summary

- investigation_plain_conclusion: 삼전/하닉 저점수는 HBM 특례로 풀 문제가 아니라 누적 연구가 candidate/archive, runtime input evidence, parser-feature bridge, weighted gate 중 어디서 멈추는지 전 아키타입에서 분리해야 하는 공통 문제다.
- implementation_plain_conclusion: 조사 목표는 요구사항별 증거로 완료됐지만, 수리 구현은 아직 완료가 아니다. acceptance spec의 blocked 항목을 exact replay, parser/feature bridge, positive/guard parity로 풀어야 한다.
- investigation_completion_status: `complete_for_root_cause_investigation`
- implementation_repair_status: `not_complete_and_tracked_as_acceptance_blockers`
- requirement_count: `8`
- requirement_status_counts: `{'proved': 1, 'proved_but_weight_layer_only': 1, 'proved_current_artifacts': 1, 'proved_failure_taxonomy': 1, 'proved_for_current_benchmark': 2, 'proved_no': 1, 'proved_root_cause': 1}`
- current_stage3_green_count: `0`
- historical_stage3_green_after_case_count: `331`
- research_support_rows: `12471`
- runtime_exercised/unexercised_archetypes: `7` / `29`
- hynix/samsung_green_shortfall_to_87: `6.9869` / `14.8819`
- stop_layer_counts: `{'candidate_replay_archive': 29, 'manual_review': 3, 'stage_gate': 4}`
- acceptance_status_counts: `{'blocked_missing_exact_fixture_archive_or_candidate_funnel': 32, 'blocked_weighted_gate_after_fields_present': 4}`

## Requirement Coverage

| id | status | question | plain answer | remaining work | evidence |
| --- | --- | --- | --- | --- | --- |
| R1_samsung_hynix_score_cut_location | proved_for_current_benchmark | 삼전/하닉 점수가 어디서 깎였나? | 하닉은 EPS/FCF가 만점인데 bottleneck/visibility/bridge 손실로 Green까지 6.9869점 부족하다. 삼성도 EPS/FCF는 만점이지만 confidence/bottleneck/visibility 손실로 Green까지 14.8819점 부족하다. | 점수 기준을 낮추는 것이 아니라 source-backed bridge field를 채워 positive/guard replay로 검증해야 한다. | docs/0619/v12_component_score_loss_waterfall_2026-06-19.md<br>docs/0619/v12_current_runtime_field_failure_census_2026-06-19.md<br>docs/0619/v12_score_loss_causal_chain_2026-06-19.md |
| R2_historical_green_cases_existed | proved | 지금까지 연구자료에 Green까지 간 애들이 실제로 있었나? | 있었다. score_simulation row 9052개 중 historical Stage3-Green after case가 331개이고, Green이 있었던 아키타입은 30개다. | historical Green label을 그대로 production Green으로 쓰지 말고 source-backed fixture로 재현해야 한다. | docs/0619/v12_historical_green_case_runtime_translation_ledger_2026-06-19.md<br>docs/0619/v12_green_score_axis_runtime_contract_audit_2026-06-19.md |
| R3_research_accumulated_into_weights | proved_but_weight_layer_only | 연구자료가 합쳐져서 점수표가 만들어진 게 맞나? | 맞다. 누적 support row 12471개, positive 1495개, counterexample 2628개가 36개 아키타입 weight profile에 들어갔다. | weight는 배점표라서 답안지 field를 자동으로 채우지 않는다. parser/feature bridge가 별도로 필요하다. | docs/0619/v12_weight_support_runtime_feature_audit_2026-06-19.md<br>docs/0619/v12_runtime_execution_path_map_2026-06-19.md |
| R4_why_low_despite_accumulation | proved_root_cause | 누적됐는데 왜 지금 pipeline 점수는 낮나? | 누적 연구는 weight layer까지는 들어갔지만, 현재 scorer는 research score축 이름을 직접 읽지 않는다. Green score key top40 중 {'exact_derived_metric_only': 1, 'exact_source_runtime_field': 2, 'missing_axis_bridge_contract': 9, 'requires_axis_bridge_to_runtime_primitives': 28} 상태라서 대부분 source-backed primitive bridge가 필요하다. | margin/customer/backlog/contract/capital_return 같은 score축을 실제 parser field와 component 입력으로 연결해야 한다. | docs/0619/v12_runtime_execution_path_map_2026-06-19.md<br>docs/0619/v12_green_score_axis_runtime_contract_audit_2026-06-19.md<br>docs/0619/v12_component_score_loss_waterfall_2026-06-19.md |
| R5_not_hbm_only | proved_no | HBM 문제만 고치면 끝나는가? | 아니다. 현재 benchmark가 실제 채점한 아키타입은 7개뿐이고 29개는 미채점이다. ready fixture 31개 기준 손실층도 {'candidate_funnel_or_replay_coverage': 24, 'runtime_input_evidence_coverage': 2, 'weighted_component_or_stage3_gate': 4}로 나뉜다. | C21/C22/C23/C28/C26 같은 비-HBM도 exact replay와 bridge adapter를 같이 보강해야 한다. | docs/0619/v12_cross_archetype_score_loss_trace_2026-06-19.md<br>docs/0619/v12_current_runtime_field_failure_census_2026-06-19.md<br>docs/0619/v12_component_score_loss_waterfall_2026-06-19.md |
| R6_systemic_failure_layers | proved_failure_taxonomy | 전체적으로 우리 문제가 무엇인가? | 중단 층은 {'candidate_replay_archive': 29, 'manual_review': 3, 'stage_gate': 4}다. 수리 완료 판정 상태도 {'blocked_missing_exact_fixture_archive_or_candidate_funnel': 32, 'blocked_weighted_gate_after_fields_present': 4}라서, 후보/archive, parser-feature bridge, gate alignment를 분리해서 고쳐야 한다. | 수리 자체는 아직 완료가 아니다. acceptance spec의 blocked 상태를 실제 fixture/replay/test로 풀어야 한다. | docs/0619/v12_runtime_execution_path_map_2026-06-19.md<br>docs/0619/v12_runtime_repair_acceptance_spec_2026-06-19.md<br>docs/0619/v12_runtime_repair_execution_backlog_2026-06-19.md |
| R7_current_runtime_component_distribution | proved_for_current_benchmark | 지금 점수 손실은 어떤 과목에 몰려 있나? | 전역 평균 손실 상위는 bottleneck_pricing 10.4771점, earnings_visibility 9.113점, eps_fcf_explosion 6.0517점이다. | 이 분포는 current benchmark 후보 120개 기준이다. 미채점 28개 아키타입은 replay 후 별도 재계산해야 한다. | docs/0619/v12_component_score_loss_waterfall_2026-06-19.md |
| R8_documentation_under_0619 | proved_current_artifacts | 0619 폴더에 계속 문서화했나? | 0619 README가 현재 결론과 읽을 순서를 갖고 있고, v12 진단 문서들이 JSON/MD 쌍으로 남아 있다. | 새 수리 패치가 생기면 같은 방식으로 acceptance evidence와 README를 갱신해야 한다. | docs/0619/README.md<br>docs/0619/v12_component_score_loss_waterfall_2026-06-19.md<br>docs/0619/v12_runtime_execution_path_map_2026-06-19.md |

## Easy Reading

- 지금까지 연구가 사라진 것은 아니다. 배점표에는 들어갔다.
- 그런데 배점표는 시험 문제의 배점일 뿐이다. 답안지의 source-backed field가 비면 점수는 낮게 나온다.
- 하닉은 EPS/FCF와 bridge field가 강하게 잡혀도 total/bottleneck gate를 통과해야 Green이 된다.
- 삼성은 같은 HBM 테마라도 C06 direct Green이 아니라 C10 memory recovery route로 따로 검증해야 한다.
- C01/C19/R13처럼 후보 row의 입력 가족이 약한 케이스는 parser 실패로 단정하지 말고 replay 입력부터 보강해야 한다.
- C21 금융, C23 바이오, C26 플랫폼 같은 비-HBM은 아예 current benchmark 시험지에 안 들어온 케이스가 많다.
- 따라서 원인 조사는 완료됐고, 다음 작업은 HBM 보너스가 아니라 exact replay archive, parser/feature bridge, positive/guard parity를 구현하는 것이다.
