# Goal4 Full-Thesis 6-Question Final Audit - 2026-07-05

작성 시점: 2026-07-07 KST

이 문서는 사용자가 요청한 6개 질문을 기준으로, 예전 `C05 10개` 산출물과 최신 `main` 산출물을 분리해서 정리한다.

핵심 결론:

```text
예전 문제:
production FULL_THESIS 10개가 전부 C05로 몰렸다.

현재 main:
C05-only는 해소됐다.
하지만 meaningful full thesis pass는 아직 아니다.
```

쉬운 예:

```text
예전에는 답안지 10장이 전부 "계약형 C05" 시험지였다.
지금은 7개 과목 답안지가 생겼다.
그런데 7개 모두 필수 첨부서류가 빠져 있어서 졸업 합격은 아니다.
```

## 기준 파일

예전 C05-only 질문의 원인 추적:

```text
docs/0705/census_v4_full_thesis_production_c05_audit_2026-07-05.md
```

최신 canonical 판정:

```text
docs/operational/research_to_runtime_parity_matrix_2026-07-05.json
docs/operational/census_mode_v4_full_thesis_production_audit.json
docs/operational/census_mode_v4_full_thesis_production_runner_audit.json
docs/operational/census_mode_v4_full_thesis_seed_materialization_audit.json
output/census_v4/2026-07-06-goal4-next-runtime-full-attempt-batch1-budget14400/census_stage_map.jsonl
output/census_v4/2026-07-06-goal4-next-runtime-full-attempt-batch1-budget14400/score_contributions.jsonl
configs/e2r_archetype_weight_profile_v2_2.json
```

최신 summary:

```text
final_status = MEANINGFUL_RUNTIME_PARITY_NOT_READY
production_full_e2r_score_path_pass = true
meaningful_full_thesis_evidence_pass = false
archetype_balanced_full_thesis_pass = true

full_thesis_row_count = 7
distinct_full_thesis_archetype_count = 7
c05_full_thesis_row_count = 1
c05_full_thesis_share = 0.142857

required_positive_missing_full_thesis_row_count = 7
green_gap_full_thesis_row_count = 7
mandatory_archetype_full_thesis_missing = C15, C24
```

즉:

```text
score path는 닫힌 row가 있다.
하지만 Green/required-positive 증거가 모두 닫힌 meaningful row는 아직 0개다.
```

## 1. 왜 production FULL_THESIS 10개가 전부 C05였나?

예전 v177 산출물에서는 seed 단계의 `target_archetype`이 전부 `UNKNOWN/null`이었다.

그런데 seed row 안에는 event-board에서 넘어온 참고 문맥이 있었다.

```text
source_primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
source_missing_primitives = repeat_evidence_family, cash_or_revision_conversion
source_failed_stage_gates = missing_green_bridge
```

그 뒤 planner가 `top_k_archetype_hypotheses[0]`를 C05로 내보냈고, production row도 C05로 닫혔다.

경로:

```text
seed target_archetype UNKNOWN
-> source_primary_archetype C05 참고 문맥
-> planner top1 C05
-> final assigned archetype C05
-> C05 Evidence Contract로 full-thesis score path 생성
```

예전 10개 symbol:

| symbol | company | seed target_archetype | source_primary context | planner top1 | final archetype |
|---|---|---|---|---|---|
| 001360 | 삼성제약 | UNKNOWN/null | C05 | C05 | C05 |
| 001470 | 삼부토건 | UNKNOWN/null | C05 | C05 | C05 |
| 002990 | 금호건설 | UNKNOWN/null | C05 | C05 | C05 |
| 010960 | 삼호개발 | UNKNOWN/null | C05 | C05 | C05 |
| 034020 | 두산에너빌리티 | UNKNOWN/null | C05 | C05 | C05 |
| 034730 | SK | UNKNOWN/null | C05 | C05 | C05 |
| 043260 | 성호전자 | UNKNOWN/null | C05 | C05 | C05 |
| 047040 | 대우건설 | UNKNOWN/null | C05 | C05 | C05 |
| 060900 | 에이전트AI | UNKNOWN/null | C05 | C05 | C05 |
| 097230 | HJ중공업 | UNKNOWN/null | C05 | C05 | C05 |

최신 main에서는 이 상태가 아니다.

```text
현재 full_thesis row:
C01 = 1
C03 = 1
C05 = 1
C06 = 1
C08 = 1
C17 = 1
C28 = 1
```

따라서 현재 답은:

```text
C05-only 문제는 해소됐다.
하지만 C05-only가 해소됐다고 Goal4가 완료된 것은 아니다.
```

## 2. target_archetype_counts가 UNKNOWN인데 최종 production row가 C05로 나온 경로

예전 `target_archetype_counts = UNKNOWN`은 "아키타입이 없다"가 아니라 "planner가 다시 판단해야 한다"는 뜻이었다.

문제는 planner가 C05 참고 문맥에 강하게 끌렸다는 점이다.

쉬운 예:

```text
시험지 표지에는 과목명이 비어 있었다.
그런데 봉투 안 참고 메모가 전부 "계약형 문제"라고 되어 있었다.
채점자가 그 메모를 보고 전부 계약형 C05 시험지로 처리했다.
```

최신 seed materialization audit는 달라졌다.

```text
seed_event_count = 111
planner_run_seed_count = 111
real_provider_success_seed_count = 110
source_task_execution_seed_count = 110
stagecourt_trace_seed_count = 23
full_thesis_promoted_seed_count = 7
```

최신 `target_archetype_counts`는 C01~C32/R13에 분산되어 있다. 각 canonical 아키타입은 대체로 3개 seed를 받았고, C29는 6개다.

하지만 audit verdict는 아직 `FAIL`이다.

```text
operator_materialization_status = PENDING_FULL_THESIS_MATERIALIZATION
actual_materialization_pass_allowed = false
full_thesis_seed_promotion_pass = false
critical_count = 48
```

핵심 critical:

```text
event_or_partial_score_operator_use_allowed_count = 12
event_or_partial_stage_operator_use_allowed_count = 12
final_operator_score_use_missing_count = 12
final_operator_stage_use_missing_count = 12
```

의미:

```text
111개 seed를 돌렸지만, 일부 row는 여전히 full thesis가 아니라 partial/event 상태다.
partial row를 운영 full thesis처럼 말하면 안 된다.
```

## 3. 27.9998 / 77.9998 점수는 어디서 나왔나?

예전 C05-only 10개 산출물의 `27.9998`과 `77.9998`은 `FULL_E2R_100` 공식에서 나온 값이다.

공식:

```text
weighted_component =
  clamp(raw_component, 0, canonical_component_max)
  / canonical_component_max
  * archetype_weight

final_score =
  clamp(sum(weighted_components) + calibration_bonus - risk_penalty, 0, 100)
```

예전 C05 weight:

```text
EPS/Visibility/Bottleneck/Mispricing/Rerating/Capital/Info
= 18/22/10/12/10/8/20
```

예전 27.9998:

```text
earnings_visibility = 13.3333 / 20 * 22 = 14.6666
information_confidence = 3.3333 / 5 * 20 = 13.3332
sum = 27.9998
```

예전 77.9998:

```text
eps_fcf_explosion = 20 / 20 * 18 = 18
earnings_visibility = 13.3333 / 20 * 22 = 14.6666
bottleneck_pricing = 20 / 20 * 10 = 10
market_mispricing = 15 / 15 * 12 = 12
valuation_rerating = 15 / 15 * 10 = 10
information_confidence = 3.3333 / 5 * 20 = 13.3332
sum = 77.9998
```

`0.0002` 차이는 별도 epsilon이 아니라 `13.3333` 같은 소수점 raw component의 반올림 부산물이다.

Stage threshold:

```text
Stage1 threshold = 40
Stage2 threshold = 65
Yellow threshold = 80
Green threshold = 90
```

최신 7개 full-thesis score-path row trace:

| symbol | company | archetype | score | stage | component formula |
|---|---|---|---:|---|---|
| 003380 | 하림지주 | C05 | 27.9998 | 0 | earnings_visibility 13.3333/20\*22=14.6666; information_confidence 3.3333/5\*20=13.3332 |
| 005930 | 삼성전자 | C06 | 44.1667 | 1 | eps_fcf 20/20\*24=24.0000; visibility 6.6667/20\*21=7.0000; bottleneck 5/20\*19=4.7500; mispricing 3.75/15\*15=3.7500; rerating 3.75/15\*12=3.0000; info 1.6667/5\*5=1.6667 |
| 011170 | 롯데케미칼 | C17 | 18.7500 | 0 | visibility 5/20\*12=3.0000; bottleneck 5/20\*18=4.5000; mispricing 3.75/15\*10=2.5000; rerating 3.75/15\*10=2.5000; info 1.25/5\*25=6.2500 |
| 012510 | 더존비즈온 | C28 | 13.2666 | 0 | visibility 3.3333/20\*24=4.0000; bottleneck 4/20\*8=1.6000; mispricing 3/15\*16=3.2000; rerating 3/15\*14=2.8000; info 0.8333/5\*10=1.6666 |
| 047810 | 한국항공우주 | C03 | 37.0000 | 0 | visibility 10/20\*24=12.0000; bottleneck 10/20\*17=8.5000; mispricing 7.5/15\*14=7.0000; rerating 7.5/15\*14=7.0000; info 2.5/5\*5=2.5000 |
| 052400 | 코나아이 | C01 | 11.9999 | 0 | visibility 3.3333/20\*25=4.1666; bottleneck 3.3333/20\*18=3.0000; mispricing 2.5/15\*12=2.0000; rerating 2.5/15\*12=2.0000; info 0.8333/5\*5=0.8333 |
| 058470 | 리노공업 | C08 | 65.2000 | 2 | eps_fcf 20/20\*22=22.0000; visibility 12/20\*21=12.6000; bottleneck 12/20\*16=9.6000; mispricing 9/15\*14=8.4000; rerating 9/15\*12=7.2000; info 3/5\*9=5.4000 |

주의:

```text
위 7개는 score path trace다.
required-positive/Green gap이 남아 있으므로 meaningful full thesis pass가 아니다.
```

## 4. C05가 아닌 아키타입 후보가 full-thesis production에서 왜 0개였나?

예전 C05-only 산출물 기준으로는 맞는 질문이다. 당시에는 C05 외 후보가 production full-thesis로 승급하지 못했다.

최신 main에서는 더 이상 0개가 아니다.

```text
non-C05 full-thesis score-path row:
C01, C03, C06, C08, C17, C28
```

다만 mandatory canary 상태는 아직 실패다.

| archetype | latest status | symbol | why not meaningful pass |
|---|---|---|---|
| C06 | score path closed only | 005930 삼성전자 | customer_preorder_or_allocation, hbm_capacity_constraint, hbm_capacity_pre_sold, memory_price_increase_mentioned 누락 |
| C08 | score path closed only | 058470 리노공업 | qualification_confirmed, repeat_order_confirmed 누락 |
| C15 | no production full-thesis row | 001390 KG케미칼 blocked | spread_expansion/utilization_rate 등 source pending, mandatory full-thesis row 없음 |
| C17 | score path closed only | 011170 롯데케미칼 | inventory_cycle, opm_expansion_pctp, spread_expansion 누락 |
| C24 | source attempted, no accepted claim | 000100 planner top1 sample | accepted full-thesis claim 0개, mandatory full-thesis row 없음 |
| C28 | score path closed only | 012510 더존비즈온 | arr_growth_visible, nrr, recurring_margin_leverage, rpo_to_sales 누락 |

쉬운 예:

```text
C06 삼성전자는 시험장에는 들어갔다.
하지만 HBM 고객 배정, capacity sold-out 같은 필수 서류가 없어 합격은 아니다.

C24는 시험장 입장권은 만들었지만, 채점 가능한 답안 claim 자체가 아직 없다.
```

## 5. required_positive_missing_primitives가 있는데 FULL_THESIS_PRODUCTION_PASS를 허용한 이유

이게 가장 중요한 문제였다.

예전 라벨:

```text
FULL_THESIS_PRODUCTION_PASS
```

문제:

```text
score path closed
meaningful full thesis passed
```

이 둘을 분리하지 않았다.

현재는 이렇게 분리되어야 한다.

```text
PRODUCTION_FULL_E2R_SCORE_PATH_PASS = true
MEANINGFUL_FULL_THESIS_EVIDENCE_PASS = false
```

쉬운 예:

```text
답안지를 제출했다 = true
정답 근거와 필수 첨부서류가 모두 있다 = false
```

최신 production audit도 pass를 막고 있다.

```text
status = PENDING_FULL_THESIS_PRODUCTION
production_pass_allowed = false
production_full_thesis_row_count = 7
production_full_thesis_row_with_required_positive_missing_primitives_count = 7
production_full_thesis_row_with_green_gap_primitives_count = 7
```

따라서 최종 답:

```text
이 pass는 "meaningful full thesis passed"가 아니다.
"claim-backed FULL_E2R_100 score path가 일부 row에서 닫혔다"까지만 허용해야 한다.
```

## 6. 삼성전자/하이닉스는 왜 production full-thesis row로 안 올라왔나?

예전 답과 최신 답을 구분해야 한다.

예전 C05-only 산출물:

```text
삼성전자/하이닉스는 controlled smoke 쪽에 있었고,
production full-thesis row로 세면 안 됐다.
```

최신 main:

```text
삼성전자 005930은 production full-thesis score-path row로 올라왔다.
하지만 meaningful pass가 아니다.
```

삼성전자 최신 row:

```text
symbol = 005930
company = 삼성전자
archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
score = 44.1667
stage = 1
score_scale = FULL_E2R_100
score_source = BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT
accepted_claim_ids = CLM-9d0e270b5c0ab656cdf4, CLM-91107f3d28ed2ad75cf9
missing required-positive = customer_preorder_or_allocation, hbm_capacity_constraint, hbm_capacity_pre_sold, memory_price_increase_mentioned
missing Green = customer_preorder_or_allocation, hbm_capacity_constraint, hbm_capacity_pre_sold
```

SK하이닉스는 최신 promoted full-thesis production row에 없다.

```text
하이닉스 controlled smoke/event-board 기록과 production full-thesis row를 섞으면 안 된다.
production full-thesis row는 실제 production source task -> accepted claim -> score contribution -> StageCourt trace가 닫힌 row만 센다.
```

쉬운 예:

```text
삼성전자는 실제 시험 답안지가 생겼다.
하지만 필수 HBM 첨부서류가 부족해서 합격은 아니다.

하이닉스는 모의고사 기록이나 event-board 기록을 실제 시험 합격자 명단에 넣으면 안 된다.
```

## 최종 판정

현재 상태:

```text
C05-only 쏠림: 해소됨
전 아키타입 시도: 36개 모두 runtime parity matrix에 있음
score path closed: 7개
meaningful full thesis passed: 0개
Goal4 완료: 아님
```

남은 blocker:

```text
GREEN_GAP_ON_PROMOTED_ROWS
MANDATORY_ARCHETYPE_FULL_THESIS_ROW_MISSING
PRODUCTION_SCORE_PATH_IS_NOT_MEANINGFUL_FULL_THESIS_PASS
REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS
```

다음 패치 방향:

```text
1. C01/C03/C05/C06/C08/C17/C28의 required-positive/Green gap을 source-backed claim으로 닫는다.
2. C15는 blocked candidate에서 spread/utilization/margin bridge를 닫아 production row를 만든다.
3. C24는 source route를 재수리해서 accepted full-thesis claim부터 만들어야 한다.
4. SK하이닉스는 smoke/event-board가 아니라 production full-thesis trace로 따로 승급해야 한다.
5. `FINAL` score row라도 required-positive/Green gap이 있으면 meaningful pass로 집계하지 않는다.
```

한 줄 결론:

```text
지금은 "채점기 경로가 일부 아키타입에서 돌아간다"까지 증명됐다.
"모든 아키타입에서 연구자료 수준의 의미 있는 운영 thesis가 나온다"는 아직 증명되지 않았다.
```
