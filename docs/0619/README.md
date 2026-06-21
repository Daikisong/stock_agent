# 0619 Score Failure Investigation Index

## 2026-06-20 패치 후 검증

6월 19일 문서들은 대부분 패치 전 실패 진단이다. 2026-06-20 기준 최신 goalcheck는 `v12_operational_research_parity_goalcheck_2026-06-20.md`를 먼저 본다.

최신 검증 요약:

- SK하이닉스 `000660 / C06 / 2024-04-25`는 운영 replay에서 `3-Green / 97.423`으로 복원됐다. 이전 ledger fixture 산출물에는 `3-Green / 97.3447`이 있었고, 최신 claim-backed fixture replay 기준 ledger 값은 `3-Green / 98.173`이다.
- SK하이닉스 `000660 / C06 / 2024-04-30`은 운영 replay에서 `3-Green / 98.2804`로 복원됐다. 과거 `97.9877` 값은 2024-04-25 source fixture를 carried-forward한 runtime fixture 값이다.
- 두 replay 모두 `runtime_fixture_injected=false`, `score_source_mode=operational_merged`, `claim-backed ratio=100`, `orphan score=0`이다.
- raw `Stage3-Green` 연구 row를 다시 검사한 뒤 최신 guard-present correction 기준 전체 준비 fixture parity는 Green `15/26 near_parity_green`, guard `36/36 guard_pass`다. 나머지 Green fixture 11개는 `cost_overrun`, `valuation_overheat`, `call_off_risk` 같은 guard primitive가 같이 있어 `3-Yellow`로 막는 것이 맞다.
- 이전 `30/34 + 4 ledger_only_green` 판정은 `Stage3-Yellow`/`Stage2-Actionable` row까지 Green fixture처럼 센 과집계였다. 예를 들어 C12/C16/C24 일부 row는 "좋은 후보지만 아직 Green은 아님"이라는 연구 라벨이므로, 운영에서 Yellow로 막히는 것이 맞다.
- C08 Green과 R13 high-MAE Green은 누락이 아니라 검증 범위상 제외다. C08 연구 row는 대부분 Actionable/Green brake이고, R13 high-MAE는 Green 발굴이 아니라 guardrail이다. 단, R13 positive-control row가 C23/C02 같은 원천 아키타입을 재사용하는 경우에는 원천 아키타입 primitive가 보존되도록 고쳤다.
- 36개 아키타입 Evidence Contract가 runtime config로 승격됐고, route 이후 LLM gap search 문맥에 required primitive와 bridge axis가 들어간다.
- 운영 replay row에 `evidence_contract_coverage_pct`와 `evidence_contract_missing_primitives`가 저장된다. 하닉 C06 2024-04-25/04-30은 둘 다 required primitive `6/6`, missing `0`, coverage `100`이다.
- positive primitive, Green gate primitive, guard primitive를 분리했다. `call_off_risk`, `price_only_blowoff`, `high_mae_history` 같은 항목은 좋은 증거 부족이 아니라 Green 차단 확인용 guard로 표시된다. Green gate primitive가 필요한 아키타입은 missing이 있으면 총점이 높아도 Stage 3-Green으로 승격하지 않는다.
- claim compiler는 `date_verified`, `green_allowed_by_date`, `runtime_fixture_source_backed`, `canonical_archetype_id` 같은 운영 메타데이터를 claim으로 세지 않는다. 추가로 guard primitive가 PRESENT이거나 UNKNOWN이면 총점이 높아도 Green을 막는다. 최신 guard-unverified replay에서 operational Green 378개와 ledger Green 551개 모두 claim ledger 누락, orphan score, unknown claim ref, Green guard finding이 `0`이다.

## 현재 결론

삼전/하닉은 HBM 과적합 대상이 아니라 전체 runtime 점수 변환 문제를 보여주는 예시다.

핵심 진단:

1. 연구자료는 Green/반례를 많이 쌓았다.
2. 아키타입별 7개 component weight는 runtime에 반영됐다.
3. 하지만 연구축을 source-backed runtime field로 번역하는 층은 부족하다.
4. 현재 운영 replay는 후보 120개 중 Stage3-Green 0개이고, 전부 `failed_stage3_total_score`, `failed_stage3_bottleneck`에 걸린다.
5. Green 기준을 낮추면 false positive가 같이 열린다. 해결은 threshold 완화가 아니라 evidence translation과 archetype adapter 보강이다.
6. 별도 parser audit 오탐도 있었다. `목표주가 상향` 라벨이 다음 줄 날짜를 상향률로 읽던 문제는 수정했고, benchmark hard audit는 45개에서 0개로 줄었다.
7. autopsy에 Green gate 부족분을 추가했다. 이제 `failed_stage3_bottleneck`이 아니라 `bottleneck:11.05/14.25(-3.20)`처럼 실제 weighted gate에서 어디서 얼마나 부족한지 바로 볼 수 있다.
8. 병목 산식 선택 경로도 추가로 노출했다. 이제 `actual_conversion_bridge`, `industrial`, `sector` 중 어떤 path가 선택됐고 raw 75까지 얼마나 부족한지 볼 수 있다.
9. autopsy gate 설명을 실제 StageClassifier와 맞췄다. 이제 raw component가 아니라 `archetype_component_*`와 weight 비례 문턱으로 deficit을 계산한다. 하닉은 `bottleneck:11.05/14.25(-3.20)`이 최신 설명이다.
10. 공통 evidence bridge 진단을 추가했다. 이제 `margin`, `customer`, `backlog`, `contract`, `valuation_repricing`, `capital_return`, `insurance_quality`, `bio_commercialization`, `software_retention`, `consumer_sell_through`, `guard_risk`가 source-backed primitive로 들어왔는지 autopsy CSV에서 볼 수 있다.
11. positive/guard fixture pair runtime audit을 추가했다. C06 strong positive는 Green 가능성이 확인됐지만, C21/C22/C23/C28 positive는 아직 `GENERIC` 경로와 약한 adapter 때문에 Stage2~Yellow에 남는다. 즉 문제는 HBM 하나가 아니라 전 아키타입 evidence-to-score 변환층이다.
12. 누적 연구와 runtime 적용 사이의 간극을 확인했다. 대표 row 12,471개와 Stage3-Green 381개가 있지만, 실제 적용된 v12 patch 112개는 모두 `guardrail_only`라 positive Green unlock은 거의 없다. 그래서 연구는 쌓였지만 좋은 증거가 점수로 올라가는 경로가 아직 약하다.
13. C21/C22/C23/C28이 `GENERIC` sector profile에 갇히던 문제를 줄이기 위해 `FINANCIAL_CAPITAL_RETURN`, `INSURANCE_RESERVE`, `BIO_COMMERCIALIZATION`, `SOFTWARE_SECURITY` profile을 추가했다. Guard는 Stage0으로 눌리지만 C21/C22/C28 positive는 아직 Stage2라 Green unlock은 남은 과제다.
14. 연구 Green과 runtime benchmark coverage 간극을 다시 확인했다. C21/C22/C23/C28에는 Green 연구 row가 있지만 현재 benchmark 120개에는 거의 들어오지 않는다. 즉 HBM 점수식뿐 아니라 candidate funnel, runtime replay fixture coverage, positive unlock planner가 같이 문제다.
15. 누적 Green row를 runtime replay fixture로 바꿀 후보 장부를 추가했다. raw Stage3-Green 381개 중 `false_green`/`false_positive`/`policy_only` marker 61개를 positive fixture에서 제외하면 fixture Green은 320개, clean fixture Green은 259개다. Green이 있는 33개 archetype 중 31개는 clean Green과 guard pair가 있어 fixture화가 가능하다. 연구가 없어서 못 하는 게 아니라, 그 연구를 runtime replay/positive unlock 검증으로 아직 고정하지 않은 것이 핵심이다.
16. fixture 후보와 현재 runtime benchmark를 대조하는 coverage board를 추가했다. ready fixture archetype 31개 중 현재 benchmark가 커버하는 것은 7개뿐이고, exact Green/guard fixture match는 0개다. C06은 후보가 올라와도 `backlog`, `contract` bridge가 비어 막히고, C21/C22/C23/C28은 아예 current benchmark에 없다.
17. ready fixture 후보를 다음 replay용 spec으로 물리화했다. 31개 archetype에 대해 Green 31개, guard 31개, 총 62개 row가 생겼다. 이 중 48개 row는 current benchmark에 없고, 12개 row는 bridge axis missing, 2개 row는 Stage3 gate blocked 상태다. 이 spec은 production scoring 입력이 아니라 다음 full point-in-time fixture 변환 지시서다.
18. 전 아키타입 score-loss trace를 추가했다. ready fixture 31개 기준으로 24개는 current benchmark에 없고, 6개는 research-axis -> runtime field 변환에서 막히며, 1개는 weighted Stage3 gate에서 막힌다. HBM은 이 중 `runtime_bridge_axes_missing`의 대표 증상일 뿐이고, 해결은 C21 금융/C23 바이오/C28 SW 같은 다른 아키타입에도 같은 방식으로 적용돼야 한다.
19. 연구 Green과 runtime gap을 한 행에 붙인 matrix를 추가했다. 대표 row 12,471개 중 raw Stage3-Green 381개, marker 제외 fixture Green 320개, source-backed clean Green 259개가 있고, clean Green+clean guard를 둘 다 가진 archetype은 31개다. 그런데 이 31개 중 24개는 current benchmark에서 아예 실행되지 않고, 6개는 runtime field 변환에서 막히며, 1개는 weighted gate에서 막힌다.
20. fixture candidate funnel audit을 추가했다. current benchmark는 후보 120개지만 실제 symbol은 11개뿐이고, Green/guard spec 62개와 exact `symbol+date` 매칭은 0개다. 5개 row는 symbol은 있었지만 월초 replay 날짜와 fixture 날짜가 달랐고, 57개 row는 symbol 자체가 current runtime 후보에 없었다. 즉 C21/C23/C28 등은 점수가 낮은 게 아니라 현재 benchmark가 점수식을 시험하지도 않았다.
21. exact fixture replay readiness를 추가했다. spec 62개는 55개 종목을 요구하지만 현재 local historical official universe는 13개 종목뿐이다. 현재 retrospective replay 방식으로 입력이 갖춰진 row는 C02/267260과 C06/000660 두 개뿐이고, strict PIT까지 증명되는 row는 C02 한 개뿐이다. Green/guard 쌍이 동시에 준비된 아키타입은 0개다. 즉 삼전/하닉 문제는 HBM 보너스 문제가 아니라 전 아키타입 fixture 입력 아카이브와 evidence bridge가 아직 비어 있는 문제다.
22. HBM research-signal translation audit을 추가했다. 넓은 HBM/core semi 연구풀 1,551개 중 하닉 관련 row는 159개, raw Stage3-Green은 8개, positive/green-worthy는 59개다. 그런데 runtime best row는 `margin=100`, `customer=100`, `revision=100`은 반영하면서도 `capacity_lock`, `order_or_contract`가 `capa_constraint=0`, `backlog=0`, `contract=0`으로 남아 Green gate를 막는다. 삼성은 raw Green이 0개라 하닉과 같은 Green positive가 아니며, runtime도 C10 memory recovery로 라우팅되고 `customer/backlog/contract=0`이다.
23. 전 아키타입 signal-runtime translation audit을 추가했다. Green 연구가 있는 33개 아키타입 중 24개는 local official/search/report archive에 Green fixture 입력이 없어 runtime replay가 못 돌고, 6개는 후보는 들어왔지만 연구축이 runtime field로 구조화되지 않으며, 1개는 field가 있어도 weighted Stage3 gate에서 막힌다. C21/C22/C23/C28은 연구 Green 수가 각각 32/19/18/12개지만 runtime candidate가 0개다. C06은 후보는 들어왔지만 `backlog`, `contract`가 required axis missing이다.
24. bridge spec-runtime field audit을 추가했다. 36개 아키타입 bridge spec의 expected primitive 180개 중 103개는 현재 parser/feature field contract에서 exact field를 찾지 못했고, Green gate/audit required axis가 해당 bridge spec primitive에 없는 불일치도 33건이다. C06은 HBM customer/capacity/revision primitive는 5/5로 존재하지만 Green gate required axis에서는 `contract`가 bridge spec에 없고 `backlog`가 runtime에서 약해 막힌다. C26/C27/C30/C31처럼 primitive 자체가 runtime field contract에 없는 아키타입도 많다.
25. runtime repair priority board를 추가했다. 전체 36개 아키타입을 작업 lane으로 나누면 primary 기준 `candidate_funnel_or_benchmark_replay` 24개, `parser_feature_field_contract` 7개, `gate_bridge_axis_alignment` 2개, `source_backed_fixture_cleaning` 2개, `weighted_gate_threshold_or_component_balance` 1개다. C06은 HBM 보너스가 아니라 gate/spec axis alignment 문제이고, C21/C22/C23/C28은 후보/replay archive 문제이며, C26/C27은 후보 문제와 field contract 문제가 같이 있다.
26. weight support-runtime feature audit을 추가했다. 누적 연구 12,471 support rows와 positive 1,495건은 36개 아키타입 weight profile에 들어갔다. 하지만 weight는 배점표일 뿐 runtime component field를 채우지 않는다. C06은 229 support rows / 58 symbols가 weight에는 들어갔지만 후보 19개에서 `backlog`, `contract`가 막혀 낮고, C21은 413 support rows가 weight에는 들어갔지만 current runtime 후보가 0개라 feature/scoring을 실행하지 못했다.
27. runtime execution path map을 추가했다. 연구 누적은 `archetype_weight_profile.py`와 `scoring.py::_apply_archetype_runtime_weights`를 통해 weight layer까지 반영되지만, 실제 점수는 `report_parser.py`와 `features.py::DeterministicFeatureEngineer.engineer`가 source-backed field를 채워야 올라간다. 전체 36개 아키타입 중 중단 층은 candidate/replay archive 26개, parser/feature bridge 6개, stage gate 1개, manual review 3개다. 즉 하닉은 HBM 특례 대상이 아니라 parser/feature bridge 문제의 예시이고, C21/C23/C26은 후보/replay가 먼저 막히는 예시다.
28. runtime repair execution backlog를 추가했다. 다음 구현 순서는 HBM 보너스가 아니라 `01_fixture_archive_and_candidate_funnel` 26개, `02_parser_feature_bridge_contract` 6개, `03_weighted_gate_validation_after_fields` 1개, `04_manual_gap_classification` 3개 순서다. 현재 exact Green/guard 쌍 replay 준비는 0개이고, missing required axis는 `guard_risk` 19, `margin` 16, `customer` 16, `contract` 14, `backlog` 10이 가장 크다.
29. runtime repair acceptance spec을 추가했다. 다음 패치의 완료 판정은 점수 상승이 아니라 exact replay 입력, source-backed field, positive/guard gate parity가 함께 증명될 때만 가능하다. 현재 acceptance 상태는 `blocked_missing_exact_fixture_archive_or_candidate_funnel` 26개, `blocked_missing_parser_feature_or_gate_axis_contract` 6개, `blocked_weighted_gate_after_fields_present` 1개, `blocked_manual_gap_unclassified` 3개로 전부 미통과다.
30. runtime first repair slice를 추가했다. 첫 실제 구현 묶음은 C06/C10을 포함하지만, C21/C23/C26/C20/C02와 manual 분류 3개도 같이 묶어야 한다. 선택된 13개 중 HBM/삼성 관련은 2개, 비-HBM은 11개이며, lane 구성은 archive/funnel 5개, parser-feature 4개, weighted gate 1개, manual classification 3개다. 첫 패치가 하닉만 Green으로 올리면 실패다.
31. runtime first repair input gap manifest를 추가했다. 첫 수리 slice 13개는 fixture role row 20개를 요구하고, 이 중 17개는 archive/funnel 결손, 1개는 strict PIT research snapshot 결손, 1개는 exact replay ready, 1개는 runtime symbol은 있으나 fixture 날짜 mismatch다. C21/C23/C26은 점수식 문제가 아니라 시험지가 current replay에 안 들어온 상태이고, C06은 green만 일부 준비됐을 뿐 guard archive가 비어 있어 단독 HBM 보너스로 처리하면 안 된다.
32. score loss causal chain을 추가했다. 하닉은 EPS/revision이 깎인 게 아니라 `backlog/contract/CAPA` bridge field가 0 또는 약해서 `total:76.76/87.00(-10.24)`, `bottleneck:11.05/14.25(-3.20)`에서 막힌다. 삼성은 C06 direct Green이 아니라 C10 memory recovery route로 남고 `customer/backlog/contract=0`이라 `68.6752` Stage2에 머문다. 비-HBM에서는 C21/C23/C26처럼 점수식 이전에 current replay 시험지가 없는 경우와 C02처럼 field가 있어도 weighted gate가 막는 경우를 같이 분리했다.
33. Green score axis-runtime contract audit을 추가했다. 연구자료 `score_simulation` 9,052개 중 Green 관련 row는 1,023개, strict Stage3-Green 관련 row는 486개다. Green 관련 고유 score key는 960개지만 현재 runtime source field와 exact match는 `capital_return_execution` 1개뿐이고, `revision_score`는 source field가 아니라 derived metric으로만 맞는다. 즉 예전 Green 연구축은 많았지만 대부분 `margin_bridge_score -> actual_op_yoy/opm`, `customer_quality_score -> customer_preorder_or_allocation`, `backlog_visibility_score -> order_backlog_to_sales` 같은 source-backed primitive bridge가 필요하다.
34. representative case runtime trajectory를 추가했다. 삼전/하닉은 HBM 과적합 대상이 아니라 전체 아키타입 evidence-to-runtime 변환 실패를 보여주는 대표 사례다. 대표 trajectory 32개 row 중 Stage3-Green은 0개이고, 하닉은 최고점도 `3-Yellow/76.7639`이며 `backlog/contract/CAPA` field가 반복적으로 비어 있다. 동시에 비-HBM ready archetype 28개도 붙여 확인했고, 손실층은 후보/replay coverage 23개, field 번역 4개, weighted gate 1개다.
35. current runtime field failure census를 추가했다. 현재 benchmark runtime 후보 120개를 기계적으로 집계하면 Stage3-Green은 0개이고, 120개 전부 `failed_stage3_total_score`와 `failed_stage3_bottleneck`에 걸린다. 실제 채점된 아키타입은 36개 중 8개뿐이며, 28개는 replay/archive coverage가 먼저 필요하다. 하닉 C06은 `backlog/contract/CAPA`가 19/19로 비고, 삼성 C10은 `customer/backlog/contract`가 비며, C02 전력기기는 best row가 bridge 100/100/100/100이어도 contract/gate deficit으로 Stage2에 남는다.
36. historical Green case runtime translation ledger를 추가했다. 과거 `score_simulation` 9,052개 중 Stage3-Green after case는 331개이고, Green이 있었던 아키타입은 30개다. 즉 과거 Green 연구는 실제로 있었다. 하지만 현재 benchmark가 그중 실제 채점한 아키타입은 7개뿐이고 23개는 미채점이다. Green을 만든 상위 축은 `relative_strength_score`, `valuation_repricing_score`, `revision_score`, `customer_quality_score`, `margin_bridge_score`였으며, top-axis occurrence 기준 exact source runtime field match는 0개다. 대부분은 `requires_axis_bridge_to_runtime_primitives`라서 연구축을 source-backed field로 번역해야 현재 점수로 살아난다.
37. component score loss waterfall을 추가했다. 하닉/삼전을 대표 예시로 쓰되 HBM 보너스가 아니라 현재 runtime 후보 전체의 7개 weighted component 손실을 계산한다. 전역 평균 손실은 `bottleneck_pricing` 10.2192점, `earnings_visibility` 9.5439점, `information_confidence` 6.2279점 순이고, 하닉/삼성/C02/C20은 EPS/FCF가 만점이어도 bottleneck/visibility/bridge 손실로 Green에 못 닿는다. C03 방산처럼 EPS/FCF 자체가 비는 케이스도 분리된다.
38. goal scope evidence audit을 추가했다. 원래 질문을 8개 요구사항으로 쪼개서 각 요구사항이 어떤 0619 산출물과 숫자로 증명되는지 연결했다. 결론은 명확하다. 진단상으로는 삼전/하닉 저점수가 HBM 특례 문제가 아니라 누적 연구가 runtime source-backed field로 번역되지 않는 전 아키타입 공통 문제임이 증명됐고, 구현상으로는 아직 acceptance spec의 `blocked_missing_exact_fixture_archive_or_candidate_funnel` 26개, `blocked_missing_parser_feature_or_gate_axis_contract` 6개, `blocked_weighted_gate_after_fields_present` 1개를 풀어야 한다.

쉬운 예:

- 나쁜 해결: "하닉이 낮으니 HBM bottleneck 점수를 올린다."
- 맞는 해결: "하닉에서 보인 `capacity lock`, `customer allocation`, `revision`, `FCF bridge` 손실을 공통 evidence bridge로 만들고, 보험/바이오/플랫폼 같은 다른 아키타입에도 각자 맞는 bridge를 만든다."

## 먼저 읽을 문서

| 순서 | 문서 | 용도 |
| ---: | --- | --- |
| 0 | `v12_score_loss_causal_chain_2026-06-19.md` | 삼전/하닉 점수 손실 위치를 전체 아키타입 후보/archive, parser-feature, stage gate 문제로 연결한 결론표 |
| 0.5 | `v12_representative_case_runtime_trajectory_2026-06-19.md` | 삼전/하닉을 HBM 특례가 아니라 전 아키타입 evidence-to-runtime 변환 실패의 대표 trajectory로 검증 |
| 0.6 | `v12_current_runtime_field_failure_census_2026-06-19.md` | 현재 runtime 후보 120개 전체에서 field 0점과 Green gate 실패가 어디에 몰렸는지 기계적으로 집계 |
| 0.7 | `v12_historical_green_case_runtime_translation_ledger_2026-06-19.md` | 과거 Stage3-Green 연구 case가 어떤 score축으로 Green이었고 현재 runtime에서 왜 재현되지 않는지 row 단위로 연결 |
| 0.8 | `v12_component_score_loss_waterfall_2026-06-19.md` | 100점 배점표 중 component별로 몇 점을 받았고 몇 점을 잃었는지 전 아키타입 runtime 후보에서 계산 |
| 0.9 | `v12_goal_scope_evidence_audit_2026-06-19.md` | 원래 질문의 8개 요구사항별로 현재 증거가 무엇을 증명하고 어떤 구현 과제가 남았는지 감사 |
| 1 | `v12_green_score_axis_runtime_contract_audit_2026-06-19.md` | 예전 Green 연구 score_simulation 축이 현재 runtime source field와 직접 맞는지 |
| 2 | `production_replay_failure_inventory_and_requirements_2026-06-19.md` | 최신 운영 replay 실패 위치와 구현 요구사항 |
| 3 | `generalized_archetype_score_conversion_failure_model_2026-06-19.md` | 삼전/하닉 사례를 전체 아키타입 문제로 일반화 |
| 4 | `runtime_conversion_root_cause_audit_2026-06-19.md` | 누적 연구가 있는데도 점수가 낮은 root-cause |
| 5 | `component_formula_loss_trace_2026-06-19.md` | 삼전/하닉과 benchmark의 Green 문턱 부족분을 formula 입력값으로 추적 |
| 6 | `weighted_gate_and_route_alignment_2026-06-19.md` | weighted gate 설명을 실제 classifier와 맞춘 수정, 삼성 route guard |
| 7 | `cross_archetype_evidence_bridge_runtime_diagnostics_2026-06-19.md` | 공통 evidence bridge 진단 컬럼 추가, 하닉/삼전과 전 섹터 bridge 상태 |
| 8 | `fixture_pair_runtime_audit_2026-06-19.md` | C06/C21/C22/C23/C28 positive/guard 쌍 runtime 결과와 남은 adapter gap |
| 9 | `cumulative_research_runtime_application_gap_2026-06-19.md` | 누적 연구 row와 실제 runtime patch 적용 간극, guardrail-only 문제 |
| 10 | `domain_profile_adapter_patch_2026-06-19.md` | C21/C22/C23/C28 domain profile 추가와 synthetic pair 결과 |
| 11 | `research_green_runtime_coverage_gap_2026-06-19.md` | 누적 Green 연구 row와 현재 runtime benchmark coverage/positive unlock 간극 |
| 12 | `v12_green_runtime_fixture_candidates_2026-06-19.md` | 누적 Stage3-Green row를 runtime replay fixture로 고정할 후보 장부 |
| 13 | `v12_fixture_runtime_coverage_board_2026-06-19.md` | fixture 후보가 current benchmark에 실제로 들어와 있는지와 bridge/gate 결손 |
| 14 | `v12_runtime_replay_fixture_spec_2026-06-19.md` | Green/guard 62개 row를 다음 runtime replay fixture로 변환하기 위한 실행 spec |
| 15 | `v12_research_green_runtime_gap_matrix_2026-06-19.md` | 연구 Green 근거와 현재 runtime gap을 아키타입별로 직접 연결 |
| 16 | `v12_fixture_candidate_funnel_audit_2026-06-19.md` | fixture 62개가 current benchmark 후보까지 도달했는지 |
| 17 | `v12_exact_fixture_replay_readiness_2026-06-19.md` | Green/guard 62개 row가 local historical official/search/report 입력으로 exact replay 가능한지 |
| 18 | `v12_hbm_research_signal_translation_audit_2026-06-19.md` | 누적 HBM 연구 신호가 삼전/하닉 runtime score field로 번역됐는지 |
| 19 | `v12_archetype_signal_runtime_translation_audit_2026-06-19.md` | 누적 Green 연구 신호가 아키타입별 runtime 후보/필드/gate까지 이어지는지 |
| 20 | `v12_bridge_spec_runtime_field_audit_2026-06-19.md` | bridge spec primitive와 parser/feature/gate field contract가 맞는지 |
| 21 | `v12_runtime_repair_priority_board_2026-06-19.md` | 전 아키타입 수리 우선순위와 작업 lane |
| 22 | `v12_weight_support_runtime_feature_audit_2026-06-19.md` | 누적 연구가 weight에는 들어갔지만 feature/gate에서 막히는 이유 |
| 23 | `v12_runtime_execution_path_map_2026-06-19.md` | 누적 연구 -> weight -> feature -> score -> stage 실행 경로와 코드별 중단 지점 |
| 24 | `v12_runtime_repair_execution_backlog_2026-06-19.md` | 다음 구현 순서, 수정 파일, 테스트, 금지할 잘못된 해결책 |
| 25 | `v12_runtime_repair_acceptance_spec_2026-06-19.md` | 다음 패치 완료 판정 기준, row별 acceptance test 이름 |
| 26 | `v12_runtime_first_repair_slice_2026-06-19.md` | HBM 과적합을 막는 첫 구현 묶음과 각 row의 첫 테스트 |
| 27 | `v12_runtime_first_repair_input_gap_manifest_2026-06-19.md` | 첫 구현 묶음의 exact 입력/archive/funnel 결손 |
| 28 | `v12_cross_archetype_score_loss_trace_2026-06-19.md` | Green/guard 62개 row가 전 아키타입에서 어느 layer에서 막히는지 |
| 29 | `bottleneck_formula_path_autopsy_2026-06-19.md` | 병목 산식 selected path와 raw 부족분을 전 섹터로 추적 |
| 30 | `green_label_scorecard_parity_audit_2026-06-19.md` | 연구 Green label/scorecard와 runtime score의 불일치 |
| 31 | `historical_green_simulation_bridge_gap_2026-06-19.md` | 과거 Green score_simulation 축이 runtime field로 안 넘어가는 증거 |
| 32 | `green_gate_deficit_autopsy_2026-06-19.md` | 삼전/하닉 및 전체 후보가 Green 문턱에서 몇 점 부족한지 |
| 33 | `parser_target_revision_date_leak_fix_2026-06-19.md` | 목표가 상향률 parser 날짜 누수와 hard audit 오탐 수정 |
| 34 | `research_fixture_matrix_candidates_2026-06-19.md` | 다음 구현에 쓸 positive/guard fixture 후보 |
| 35 | `evidence_bridge_spec_draft_2026-06-19.md` | 연구축을 runtime primitive/component/gate로 옮기는 구현 초안 |
| 36 | `cross_archetype_research_to_runtime_conversion_gap_2026-06-19.md` | 연구축과 runtime field의 전역 변환 결손 |
| 37 | `current_benchmark_replay_green_gap_board_2026-06-19.md` | benchmark replay에서 Green이 0개인 근거 |
| 38 | `end_to_end_score_loss_map_2026-06-19.md` | 후보 생성부터 stage gate까지 점수 손실 경로 |

## HBM/삼전/하닉 세부 문서

| 문서 | 용도 |
| --- | --- |
| `hbm_asof_replay_autopsy_2026-06-19.md` | 하닉/삼전 as-of replay 세부 진단 |
| `hbm_parser_conversion_sensitivity_2026-06-19.md` | HBM parser field 누락과 민감도 |
| `semis_green_recall_score_audit_2026-06-19.md` | 반도체 Green recall 점검 |
| `v12_hbm_score_loss_trace_2026-06-19.md` | HBM 과적합이 아니라 전체 score-loss 문제의 케이스 스터디 |
| `v12_hbm_research_signal_translation_audit_2026-06-19.md` | 누적 HBM 연구 신호와 삼전/하닉 runtime bridge field 대조 |
| `v12_archetype_signal_runtime_translation_audit_2026-06-19.md` | HBM 밖 C21/C23/C28까지 포함한 전 아키타입 signal-runtime 대조 |
| `v12_bridge_spec_runtime_field_audit_2026-06-19.md` | C06처럼 primitive는 있으나 gate axis가 안 맞는 경우와, C26처럼 primitive field contract 자체가 없는 경우를 분리 |
| `v12_runtime_repair_priority_board_2026-06-19.md` | C06을 전체 repair lane 안에서 어디에 둬야 하는지 |
| `v12_weight_support_runtime_feature_audit_2026-06-19.md` | "연구가 점수표에 반영됐는데 왜 낮은가"를 weight layer와 feature layer로 분리 |
| `v12_runtime_execution_path_map_2026-06-19.md` | 삼전/하닉 예시를 전체 아키타입 execution path와 코드 owner로 일반화 |
| `v12_runtime_repair_execution_backlog_2026-06-19.md` | HBM 보너스가 아니라 fixture/archive, parser-feature, gate 검증 순서로 다음 패치 고정 |
| `v12_runtime_repair_acceptance_spec_2026-06-19.md` | 하닉/HBM 보너스나 threshold 완화가 아니라 replay/field/guard 검증으로 완료 판정 |
| `v12_runtime_first_repair_slice_2026-06-19.md` | C06/C10과 비-HBM 11개를 같이 묶어 첫 패치가 HBM 특례로 새지 않게 고정 |
| `v12_runtime_first_repair_input_gap_manifest_2026-06-19.md` | C06 green만 보고 보너스를 주지 않도록 first slice의 role별 입력 결손 분리 |
| `v12_score_loss_causal_chain_2026-06-19.md` | 하닉/삼전의 실제 깎인 점수칸과 비-HBM stop layer를 한 표로 연결 |
| `v12_green_score_axis_runtime_contract_audit_2026-06-19.md` | 예전 Green score axis가 runtime source field로 바로 들어가지 않는 직접 증거 |
| `v12_representative_case_runtime_trajectory_2026-06-19.md` | 삼전/하닉 날짜별 trajectory와 비-HBM 손실층을 같이 붙여 HBM 과적합을 방지 |
| `v12_current_runtime_field_failure_census_2026-06-19.md` | 현재 runtime 후보 120개에서 삼전/하닉 포함 전 후보의 field 0점과 gate deficit을 집계 |
| `v12_historical_green_case_runtime_translation_ledger_2026-06-19.md` | 과거 Green case 331개가 어떤 연구 score축으로 Green이었고 현재 runtime field와 어떻게 끊기는지 |
| `v12_component_score_loss_waterfall_2026-06-19.md` | 삼전/하닉을 대표 예시로 보되 HBM 특례 없이 7개 component별 손실을 전 후보와 아키타입 best row로 계산 |
| `v12_goal_scope_evidence_audit_2026-06-19.md` | 원래 질문의 요구사항별 증거와 아직 blocked 상태인 구현 과제를 분리 |

주의:

- 이 문서들은 HBM 전용 패치를 만들기 위한 것이 아니다.
- 전체 evidence bridge 설계를 위한 대표 케이스다.

## 전체 아키타입 커버리지 문서

| 문서 | 용도 |
| --- | --- |
| `archetype_runtime_profile_coverage_2026-06-19.md` | 36개 archetype weight와 sector profile coverage 차이 |
| `archetype_runtime_gap_matrix_2026-06-19.md` | 아키타입별 runtime gap matrix |
| `green_case_score_axis_conversion_audit_2026-06-19.md` | Green 연구축이 runtime field로 들어가는지 점검 |
| `research_axis_runtime_mapping_priorities_2026-06-19.md` | 어떤 연구축을 먼저 bridge할지 우선순위 |
| `global_green_runtime_gap_autopsy_2026-06-19.md` | 전체 Green 연구와 runtime gap 요약 |
| `score_deduction_mechanics_and_green_truth_table_2026-06-19.md` | stage gate/점수 차감 규칙 설명 |
| `v12_bridge_spec_runtime_field_audit_2026-06-19.md` | 36개 아키타입 bridge primitive와 runtime field contract 불일치 |
| `v12_runtime_repair_priority_board_2026-06-19.md` | 후보 funnel, exact archive, field contract, gate alignment, weighted gate 수리 보드 |
| `v12_weight_support_runtime_feature_audit_2026-06-19.md` | 누적 research support가 weight에는 들어갔지만 component field에는 자동 반영되지 않는 증거 |
| `v12_runtime_execution_path_map_2026-06-19.md` | research/weight/candidate/parser-feature/scoring/stage gate 전 실행 경로와 중단 층 |
| `v12_runtime_repair_execution_backlog_2026-06-19.md` | 구현 lane별 다음 패치, 수정 파일, 테스트, 금지할 shortcut |
| `v12_runtime_repair_acceptance_spec_2026-06-19.md` | lane별 완료 기준과 row별 acceptance test 이름 |
| `v12_runtime_first_repair_slice_2026-06-19.md` | 첫 실제 구현 slice와 HBM 과적합 방지용 대표 row 묶음 |
| `v12_runtime_first_repair_input_gap_manifest_2026-06-19.md` | first slice의 exact as-of archive, strict PIT, candidate funnel 결손 |
| `v12_score_loss_causal_chain_2026-06-19.md` | 누적 연구 -> weight -> 후보/archive -> parser-feature -> gate 중 어디서 점수가 멈췄는지 결론형으로 요약 |
| `v12_green_score_axis_runtime_contract_audit_2026-06-19.md` | Green score_simulation 축 960개와 runtime field contract의 직접/간접 매칭 상태 |
| `v12_representative_case_runtime_trajectory_2026-06-19.md` | 대표 종목 trajectory를 전 아키타입 guard와 연결해 종목명/HBM 보너스가 아닌 공통 수리 기준을 고정 |
| `v12_current_runtime_field_failure_census_2026-06-19.md` | 현재 채점된 8개 아키타입과 미채점 28개 아키타입을 분리하고 field/gate 손실을 수치화 |
| `v12_historical_green_case_runtime_translation_ledger_2026-06-19.md` | 누적 연구의 과거 Green 처리 방식과 현재 runtime 재현 실패를 case row 단위로 대조 |
| `v12_component_score_loss_waterfall_2026-06-19.md` | 채점된 8개 아키타입에서 weighted component 배점 대비 실제 획득/손실 점수를 waterfall로 비교 |
| `v12_goal_scope_evidence_audit_2026-06-19.md` | 조사 범위가 원래 질문을 어디까지 덮는지와 남은 acceptance blocker를 한 표로 정리 |

## 다음 구현 순서

1. `EvidenceBridgeSpec` 초안 작성
   - `margin_bridge_score`, `customer_quality_score`, `backlog_visibility_score`, `contract_score`, `policy_or_regulatory_score`, `accounting_trust_risk_score`부터 시작한다.
   - 초안은 `evidence_bridge_spec_draft_2026-06-19.md`에 있다.
   - 실제 구현 순서는 `v12_runtime_repair_execution_backlog_2026-06-19.md`의 lane 순서를 따른다.
   - 완료 판정은 `v12_runtime_repair_acceptance_spec_2026-06-19.md`의 acceptance test 기준을 따른다.
   - 첫 구현 묶음은 `v12_runtime_first_repair_slice_2026-06-19.md`의 13개 row를 기준으로 한다.
   - 첫 구현 입력 결손은 `v12_runtime_first_repair_input_gap_manifest_2026-06-19.md`의 role별 missing input을 기준으로 채운다.
   - 점수 손실 원인 사슬은 `v12_score_loss_causal_chain_2026-06-19.md`를 먼저 보고, 하닉/HBM 특례가 아니라 candidate/archive, parser-feature, stage gate 중 어느 층인지 분리한다.
   - 예전 Green 연구축과 runtime field 계약 차이는 `v12_green_score_axis_runtime_contract_audit_2026-06-19.md`를 기준으로 보며, score axis 이름을 그대로 점수에 더하지 않고 source-backed primitive로 번역한다.

2. positive/false-positive fixture matrix를 runtime replay fixture로 변환
   - 하닉 positive와 삼성/TLB 같은 catch-up/proxy guard를 한 증거 구조로 둔다.
   - C21 금융, C22 보험, C23 바이오, C28 SW/security도 같은 방식으로 둔다.
   - 최신 후보 목록은 `v12_green_runtime_fixture_candidates_2026-06-19.md`에 있다.
   - current benchmark coverage 상태는 `v12_fixture_runtime_coverage_board_2026-06-19.md`에 있다.
   - 다음 replay 변환 spec은 `v12_runtime_replay_fixture_spec_2026-06-19.md`와 `.jsonl`에 있다.
   - 연구 Green 근거와 현재 runtime gap의 직접 대조는 `v12_research_green_runtime_gap_matrix_2026-06-19.md`에 있다.
   - current benchmark 후보까지 도달했는지의 대조는 `v12_fixture_candidate_funnel_audit_2026-06-19.md`에 있다.
   - exact replay에 필요한 local official/search/report 입력 준비 상태는 `v12_exact_fixture_replay_readiness_2026-06-19.md`에 있다.

3. parser domain primitive 확장
   - HBM CAPA 제약 같은 토큰만이 아니라, 금융 CSM/K-ICS, 바이오 approval-to-revenue, SW retention/RPO 같은 primitive를 source-backed field로 뽑는다.

4. archetype-specific feature adapter 추가
   - 36개 weight를 소수 sector profile로만 압축하지 않는다.

5. score loss report 추가
   - `failed_stage3_bottleneck`만 출력하지 말고 어떤 연구축이 어떤 runtime field에서 0점이 됐는지 보여준다.
   - 전역 trace는 `v12_cross_archetype_score_loss_trace_2026-06-19.md`에 있고, HBM은 그중 하나의 케이스 스터디로 `v12_hbm_score_loss_trace_2026-06-19.md`에 둔다.

## 완료 기준

전면조사 목표는 완료로 본다.

이유:

- 삼전/하닉이 어디서 깎였는지 component와 gate 기준으로 분해했다.
- 과거 Green 연구 case가 실제로 있었는지 확인했다.
- 누적 연구가 weight profile에는 들어갔지만 runtime field를 자동으로 채우지 않는다는 실행 경로를 확인했다.
- HBM 문제가 아니라 36개 아키타입의 후보/archive, parser-feature bridge, stage gate 문제로 분리했다.
- 원래 질문의 8개 요구사항별 증거는 `v12_goal_scope_evidence_audit_2026-06-19.md`에 고정했다.

하지만 수리 구현은 아직 완료가 아니다.

구현까지 완료라고 보려면 최소한 다음 증거가 필요하다.

- 하닉 positive fixture가 Green 또는 의도한 Green-candidate로 올라온다.
- 삼성 catch-up false-positive가 같이 Green으로 뚫리지 않는다.
- C21/C22/C23/C28 같은 비-HBM 아키타입도 positive/guard fixture 쌍을 통과한다.
- 운영 replay에서 Green 0개 문제가 사라지되, R13/C30/C31/C32 guard 반례가 무너지지 않는다.
- score explanation이 field-level 손실을 보여준다.
