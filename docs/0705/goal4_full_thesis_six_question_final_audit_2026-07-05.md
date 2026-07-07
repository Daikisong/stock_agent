# Goal4 Full-Thesis 6-Question Final Audit - 2026-07-05

작성 시점: 2026-07-08 KST

이 문서는 사용자가 요청한 6개 질문에 답한다. 핵심은 두 상태를 섞지 않는 것이다.

```text
과거 C05-only 산출물:
  production FULL_THESIS 10개가 전부 C05로 몰렸던 문제.

현재 main / 0708 self-repair 이후:
  C05-only는 해소됐지만 Goal4는 아직 완료가 아니다.
```

쉬운 예:

```text
예전 문제:
  답안지 10장이 전부 "C05 계약형" 시험지로 채점됐다.

현재 문제:
  여러 과목 답안지가 생겼지만 필수 증빙 서류가 빠져서 합격은 아니다.
```

## 최신 결론

최신 canonical 파일:

```text
docs/operational/research_to_runtime_parity_matrix_2026-07-05.json
docs/operational/census_mode_v4_full_thesis_production_audit.json
docs/operational/census_mode_v4_full_thesis_production_runner_audit.json
docs/operational/census_mode_v4_full_thesis_seed_materialization_audit.json
```

최신 상태:

```text
final_status = MEANINGFUL_RUNTIME_PARITY_NOT_READY
production_full_e2r_score_path_pass = true
meaningful_full_thesis_evidence_pass = false
archetype_balanced_full_thesis_pass = false

full_thesis_row_count = 6
distinct_full_thesis_archetype_count = 6
c05_full_thesis_share = 0.166667

full_thesis_by_archetype:
  C01_ORDER_BACKLOG_MARGIN_BRIDGE = 1
  C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG = 1
  C05_EPC_MEGA_CONTRACT_MARGIN_GAP = 1
  C06_HBM_MEMORY_CUSTOMER_CAPACITY = 1
  C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY = 1
  C15_MATERIAL_SPREAD_SUPERCYCLE = 1

required_positive_missing_full_thesis_row_rate = 1.0
green_gap_full_thesis_row_rate = 1.0

mandatory_archetype_full_thesis_missing:
  C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  C24_BIO_TRIAL_DATA_EVENT_RISK
  C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

따라서 현재 판정은:

```text
C05-only 쏠림: 해소됨
score path closed row: 6개
meaningful full thesis pass: 0개
Goal4 완료: 아님
```

## 1. 왜 production FULL_THESIS 10개가 전부 C05였나?

이 질문은 과거 C05-only 산출물에 대한 질문이다.

당시 seed 단계의 `target_archetype`은 `UNKNOWN/null`이었다. 그런데 seed 안에는 event-board에서 넘어온 C05 참고 문맥이 있었다.

```text
source_primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
source_missing_primitives = repeat_evidence_family, cash_or_revision_conversion
source_failed_stage_gates = missing_green_bridge
```

그 뒤 planner가 `top_k_archetype_hypotheses[0]`를 C05로 냈고, 최종 production row도 C05 Evidence Contract로 닫혔다.

경로:

```text
seed target_archetype UNKNOWN
-> source_primary_archetype C05 참고 문맥
-> planner top1 C05
-> final assigned archetype C05
-> C05 Evidence Contract score path 생성
```

과거 10개 symbol:

| symbol | company | seed target_archetype | planner top1 | final archetype |
|---|---|---|---|---|
| 001360 | 삼성제약 | UNKNOWN/null | C05 | C05 |
| 001470 | 삼부토건 | UNKNOWN/null | C05 | C05 |
| 002990 | 금호건설 | UNKNOWN/null | C05 | C05 |
| 010960 | 삼호개발 | UNKNOWN/null | C05 | C05 |
| 034020 | 두산에너빌리티 | UNKNOWN/null | C05 | C05 |
| 034730 | SK | UNKNOWN/null | C05 | C05 |
| 043260 | 성호전자 | UNKNOWN/null | C05 | C05 |
| 047040 | 대우건설 | UNKNOWN/null | C05 | C05 |
| 060900 | 에이전트AI | UNKNOWN/null | C05 | C05 |
| 097230 | HJ중공업 | UNKNOWN/null | C05 | C05 |

현재는 이 상태가 아니다.

```text
현재 production full-thesis score-path row:
  C01, C03, C05, C06, C08, C15
```

## 2. target_archetype_counts가 UNKNOWN인데 어떻게 C05로 나왔나?

과거 `UNKNOWN`은 "아키타입이 없다"가 아니라 "planner가 다시 정해야 한다"는 뜻이었다.

문제는 planner에게 전달된 참고 문맥이 C05 쪽으로 치우쳐 있었다는 점이다.

쉬운 예:

```text
시험지 표지의 과목명은 비어 있었다.
그런데 봉투 안 메모가 전부 "계약형 문제"라고 적혀 있었다.
채점자가 그 메모를 보고 전부 C05 계약형으로 처리했다.
```

현재 `census_mode_v4_full_thesis_seed_materialization_audit.json`은 다르다.

```text
target_archetype_counts:
  C01~C32/R13에 분산
  대부분 canonical archetype은 3개 seed 보유
  UNKNOWN count는 최신 target_archetype_counts의 핵심 경로가 아님
```

즉:

```text
과거 문제:
  UNKNOWN seed가 C05 문맥을 타고 C05로 쏠림.

현재 문제:
  seed는 분산됐지만, full-thesis meaningful evidence closure가 아직 안 됨.
```

## 3. 27.9998 / 77.9998 점수는 어디서 나왔나?

점수는 LLM이 직접 부른 숫자가 아니다. `FULL_E2R_100` 가중 합산이다.

공식:

```text
weighted_component =
  clamp(raw_component, 0, component_max)
  / component_max
  * archetype_weight

final_score =
  clamp(sum(weighted_components) + calibration_bonus - risk_penalty, 0, 100)
```

Stage threshold:

```text
Stage1 threshold = 40
Stage2 threshold = 65
Yellow threshold = 80
Green threshold = 90
```

### 과거 27.9998

C05 weight:

```text
earnings_visibility = 22
information_confidence = 20
```

계산:

```text
earnings_visibility: 13.3333 / 20 * 22 = 14.6666
information_confidence: 3.3333 / 5 * 20 = 13.3332
sum = 27.9998
```

`0.0002` 차이는 별도 epsilon이 아니라 `13.3333` 반올림 부산물이다.

### 과거 77.9998

계산:

```text
eps_fcf_explosion: 20 / 20 * 18 = 18.0000
earnings_visibility: 13.3333 / 20 * 22 = 14.6666
bottleneck_pricing: 20 / 20 * 10 = 10.0000
market_mispricing: 15 / 15 * 12 = 12.0000
valuation_rerating: 15 / 15 * 10 = 10.0000
information_confidence: 3.3333 / 5 * 20 = 13.3332
sum = 77.9998
```

### 현재 6개 score-path row formula trace

출처:

```text
output/census_v4/2026-07-05-research-to-runtime-parity-self-repair-01-20260707T173522Z/census_stage_map.jsonl
output/census_v4/2026-07-05-research-to-runtime-parity-self-repair-01-20260707T173522Z/score_contributions.jsonl
configs/e2r_archetype_weight_profile_v2_2.json
```

| symbol | company | archetype | score | stage | component formula |
|---|---|---|---:|---|---|
| 001390 | KG케미칼 | C15 | 14.4000 | 0 | visibility 4/20\*12=2.4000; bottleneck 4/20\*20=4.0000; mispricing 3/15\*10=2.0000; rerating 3/15\*10=2.0000; info 1/5\*20=4.0000 |
| 003380 | 하림지주 | C05 | 27.9998 | 0 | visibility 13.3333/20\*22=14.6666; info 3.3333/5\*20=13.3332 |
| 005930 | 삼성전자 | C06 | 39.8333 | 0 | eps/fcf 20/20\*24=24.0000; visibility 3.3333/20\*21=3.5000; bottleneck 5/20\*19=4.7500; mispricing 3.75/15\*15=3.7500; rerating 3.75/15\*12=3.0000; info 0.8333/5\*5=0.8333 |
| 047810 | 한국항공우주 | C03 | 37.0000 | 0 | visibility 10/20\*24=12.0000; bottleneck 10/20\*17=8.5000; mispricing 7.5/15\*14=7.0000; rerating 7.5/15\*14=7.0000; info 2.5/5\*5=2.5000 |
| 052400 | 코나아이 | C01 | 24.0001 | 0 | visibility 6.6667/20\*25=8.3334; bottleneck 6.6667/20\*18=6.0000; mispricing 5/15\*12=4.0000; rerating 5/15\*12=4.0000; info 1.6667/5\*5=1.6667 |
| 058470 | 리노공업 | C08 | 65.2000 | 2 | eps/fcf 20/20\*22=22.0000; visibility 12/20\*21=12.6000; bottleneck 12/20\*16=9.6000; mispricing 9/15\*14=8.4000; rerating 9/15\*12=7.2000; info 3/5\*9=5.4000 |

주의:

```text
이 6개는 score path row다.
required-positive/Green gap이 모두 남아 있으므로 meaningful full thesis pass가 아니다.
```

## 4. C05가 아닌 아키타입 후보가 왜 0개였나?

과거 C05-only 산출물에서는 C05 외 후보가 production full-thesis로 승급하지 못했다. 원인은 C05 문맥이 UNKNOWN seed를 장악했고, C05 Evidence Contract로 score path가 먼저 닫혔기 때문이다.

현재는 C05 외 full-thesis score-path row가 있다.

```text
non-C05 score-path row:
  C01, C03, C06, C08, C15
```

하지만 주요 canary는 아직 의미 있는 합격이 아니다.

| archetype | 현재 상태 | 왜 meaningful pass가 아닌가 |
|---|---|---|
| C06 | production score path only | 삼성전자 row는 있으나 customer_preorder_or_allocation, hbm_capacity_constraint, hbm_capacity_pre_sold가 Green gap |
| C08 | production score path only | 리노공업 row는 있으나 qualification_confirmed, repeat_order_confirmed 등 Green/required gap |
| C15 | production score path only | KG케미칼 row는 있으나 spread/utilization/margin bridge가 required/Green gap |
| C17 | full thesis blocked | accepted claim 3개는 있으나 production full-thesis row 0개, required/Green primitive gap |
| C24 | planner-only | 000100 target candidate는 있으나 source_task_execution_count 0 |
| C28 | source route attempted | source task 48개 실행, accepted claim 0개, primitive mapping rejected |

쉬운 예:

```text
C08/C15는 시험지를 냈다.
하지만 필수 첨부서류가 빠져서 합격이 아니다.

C24는 시험지를 낸 것이 아니라 시험 접수 후보만 만들어진 상태다.

C28은 서류를 많이 가져왔지만 채점 가능한 문장으로 인정된 claim이 0개다.
```

## 5. required_positive_missing_primitives가 있는데 왜 FULL_THESIS_PRODUCTION_PASS가 허용됐나?

이것이 가장 위험했던 라벨 혼동이다.

나쁜 해석:

```text
FULL_THESIS_PRODUCTION_PASS
= 의미 있는 full thesis 합격
```

올바른 분리:

```text
PRODUCTION_FULL_E2R_SCORE_PATH_PASS
= accepted claim -> score contribution -> FULL_E2R_100 계산 경로가 닫힘

MEANINGFUL_FULL_THESIS_EVIDENCE_PASS
= required-positive와 Green primitive까지 닫힌 운영 thesis
```

현재 최신 production audit는 pass를 막고 있다.

```text
status = PENDING_FULL_THESIS_PRODUCTION
production_pass_allowed = false
production_full_thesis_row_count = 6
production_full_thesis_row_with_required_positive_missing_primitives_count = 6
production_full_thesis_row_with_green_gap_primitives_count = 6
```

쉬운 예:

```text
답안지를 냈다 = score path closed
정답 근거와 필수 첨부서류가 다 있다 = meaningful pass

현재는 앞의 것만 일부 됐고, 뒤의 것은 0개다.
```

## 6. 삼성전자/하이닉스는 왜 production full-thesis row로 안 올라왔나?

예전 C05-only 산출물 기준:

```text
삼성전자/하이닉스는 controlled smoke나 event-board 기록 쪽에 있었고,
production full-thesis row로 세면 안 됐다.
```

현재 main 기준:

```text
삼성전자 005930은 C06 production score-path row로 올라왔다.
하지만 meaningful pass가 아니다.

SK하이닉스 000660은 production full-thesis row에 없다.
refresh queue / smoke / event-board 기록과 production row를 섞으면 안 된다.
```

삼성전자 최신 row:

```text
symbol = 005930
company = 삼성전자
archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
score = 39.8333
stage = 0
score_scale = FULL_E2R_100
score_source = BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT
accepted_claim_count = 1
score_contribution_count = 6
required_positive_missing = true
green_gap = true
```

하이닉스 최신 상태:

```text
production full-thesis promoted_symbols에 000660 없음
refresh_queue_unmaterialized_sample에는 SK하이닉스가 남아 있음
materialization_blocker = full_thesis_refresh_task_has_no_research_brain_stagecourt_trace
```

쉬운 예:

```text
삼성전자는 실제 시험 답안지가 생겼다.
하지만 HBM 필수 증빙이 부족해서 합격은 아니다.

하이닉스는 모의고사/대기열 기록이 있을 뿐,
아직 production full-thesis 합격자 명단에는 없다.
```

## 최종 판정

현재 blockers:

```text
GREEN_GAP_ON_PROMOTED_ROWS
MANDATORY_ARCHETYPE_FULL_THESIS_ROW_MISSING
PRODUCTION_SCORE_PATH_IS_NOT_MEANINGFUL_FULL_THESIS_PASS
REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS
```

다음 패치 방향:

```text
1. C17:
   accepted claim 3개가 왜 full-thesis promotion으로 못 갔는지 required/Green primitive 단위로 분해한다.

2. C24:
   RESEARCH_MEMORY_TARGET_CANDIDATE 000100을 bounded source task execution으로 전환한다.

3. C28:
   shinyoung.com / BrokerReport route에서 왜 accepted claim 0개인지
   no_allowed_primitive_for_predicate와 source lineage rejection을 분해한다.

4. C01/C03/C05/C06/C08/C15:
   score path row를 meaningful pass로 착각하지 않고
   required-positive/Green gap을 source-backed claim으로 닫는다.
```

한 줄 결론:

```text
지금은 "채점기 경로가 C05 밖으로 확장됐다"까지 증명됐다.
"모든 아키타입에서 연구자료 수준의 의미 있는 운영 thesis가 나온다"는 아직 증명되지 않았다.
```
