# Cumulative Research vs Runtime Application Gap - 2026-06-19

## 결론

누적 연구자료는 실제로 많이 쌓였고, 일부는 runtime에 반영됐다.

하지만 반영 방향이 두 갈래로 갈라져 있다.

```text
1. 아키타입별 점수 비중
   -> runtime에 반영됨
   -> 36개 canonical archetype weight 적용

2. positive Green unlock / 점수 보너스
   -> 거의 반영되지 않음
   -> 적용된 v12 patch 112개가 전부 guardrail_only
```

그래서 사용자가 느낀 문제가 생긴다.

쉬운 예:

- 연구자료에는 "하닉은 HBM Green이었다"는 누적 row가 있다.
- runtime weight도 C06에 맞게 들어간다.
- 그런데 "HBM capacity sold-out, customer allocation, backlog/contract"를 component 점수로 바꾸는 positive adapter가 약하면 점수는 안 올라간다.
- 반대로 "price-only, high-MAE, false-positive"를 막는 guardrail은 많이 들어갔다.

즉 지금 엔진은 연구를 안 본 것이 아니다.

문제는 누적 연구가 주로 "막는 쪽"으로 안전 반영됐고, "좋은 증거를 점수로 올리는 쪽"은 아직 source-backed field와 adapter가 부족하다는 점이다.

## 현재 누적 연구 장부 상태

`reports/e2r_calibration/v12/ingest_summary.md` 기준:

| item | value |
| --- | ---: |
| discovered v12 MD | 2,263 |
| raw trigger rows | 18,760 |
| validated trigger rows | 13,738 |
| representative trigger rows | 12,471 |
| rejected rows | 8,186 |
| covered large sectors | 10 |
| covered canonical archetypes | 36 |
| archetype runtime weight count | 36 |
| production default scoring changed | True |

`data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl` 기준:

| item | count |
| --- | ---: |
| representative rows | 12,471 |
| Stage2-Actionable | 4,704 |
| Stage3-Green | 381 |
| Stage3-Yellow | 886 |
| Stage4B | 2,472 |
| Stage4C | 699 |
| usable for weight calibration | 6,442 |
| source proxy only | 3,723 |
| evidence URL pending | 3,906 |

이 숫자는 "연구가 거의 없다"가 아니다.

오히려 자료는 많다.

## 그런데 적용된 patch가 전부 guardrail이다

`data/e2r/calibration/v12/v12_promotion_decisions.jsonl`와 `v12_patch_specs.jsonl` 기준:

| item | count |
| --- | ---: |
| promotion decisions | 133 |
| apply_next_patch | 112 |
| blocked_by_data_quality | 21 |
| actual patch specs | 112 |
| guardrail_only patch | 112 |
| positive stage2 bonus patch | 0 |
| full 4B overlay positive patch | 0 |

적용된 axis:

| axis | count | 방향 |
| --- | ---: | --- |
| `stage2_required_bridge` | 46 | 얕은 Stage2를 막음 |
| `earlier_thesis_break_watch` | 40 | 4C thesis break를 더 빨리 감시 |
| `local_4b_watch_guard` | 25 | price-only 4B를 full 4B로 올리지 않음 |
| `hard_4c_confirmation` | 1 | hard 4C 확인 |

막힌 positive성 후보:

| axis | blocked count | blocker |
| --- | ---: | --- |
| `full_4b_overlay_candidate` | 21 | `full_4b_overlay_needs_verified_non_proxy_evidence` |

핵심:

```text
누적 연구 -> default runtime에 반영됨
하지만 그 반영이 대부분 "방어/차단" 방향이다.
```

예:

- 좋은 연구 row가 "이 종목은 Green이었다"라고 해도, evidence URL pending/source proxy가 많으면 positive unlock으로 승격되지 않는다.
- 반례 row가 "이런 건 false positive였다"라고 하면 guardrail-only patch로는 비교적 안전하게 들어간다.

## 아키타입별 연구 row와 현재 runtime 점수의 차이

대표 비교:

| archetype | rep rows | positive-ish | guard-ish | weight usable | current profile error | runtime n | runtime stage | avg score | avg total deficit | avg bottleneck deficit | avg visibility deficit | backlog bridge rate | contract bridge rate | customer bridge rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 229 | 89 | 153 | 145 | 150 | 19 | 3-Yellow:12, 1:7 | 75.23 | 11.77 | 3.93 | 0.19 | 0.00 | 0.00 | 1.00 |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 366 | 149 | 251 | 240 | 243 | 1 | 2:1 | 68.68 | 18.32 | 3.56 | 2.30 | 0.00 | 0.00 | 0.00 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 358 | 203 | 226 | 184 | 192 | 22 | 1:22 | 57.10 | 29.90 | 4.79 | 3.00 | 0.00 | 0.00 | 0.00 |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 413 | 248 | 169 | 241 | 169 | 0 | not_in_120 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 327 | 179 | 184 | 173 | 141 | 0 | not_in_120 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 269 | 134 | 152 | 170 | 147 | 0 | not_in_120 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 285 | 111 | 180 | 142 | 161 | 0 | not_in_120 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| C02_POWER_GRID_DATACENTER_CAPEX | 277 | 136 | 186 | 158 | 151 | 44 | 2:33, 1:11 | 66.10 | 20.90 | 6.49 | 3.17 | 0.75 | 0.50 | 0.50 |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 267 | 124 | 150 | 171 | 71 | 12 | 1:12 | 35.65 | 51.35 | 10.37 | 3.47 | 1.00 | 1.00 | 1.00 |

해석:

- C06은 연구 row가 충분하고 customer bridge도 runtime에 들어온다.
- 그런데 backlog/contract bridge가 0이라 Green 병목이 열린 적이 없다.
- C21/C22/C23/C28은 연구 row가 많지만 이번 benchmark 120에는 아예 runtime 후보로 안 잡혔다.
- 즉 "아키타입 연구가 쌓였다"와 "현재 replay 후보/field에 들어왔다"는 별개다.

## 삼전/하닉은 정확히 어디서 깎였나

### SK하이닉스 2024-05-01

| component | weighted score | max |
| --- | ---: | ---: |
| EPS/FCF | 24.0000 | 24 |
| earnings visibility | 15.9077 | 21 |
| bottleneck pricing | 11.0522 | 19 |
| market mispricing | 12.8520 | 15 |
| valuation rerating | 9.8712 | 12 |
| capital allocation | 0.0808 | 4 |
| information confidence | 3.0000 | 5 |
| risk penalty | 0.0000 | - |
| total | 76.7639 | 100 |

Green gate:

| gate | actual | required | deficit |
| --- | ---: | ---: | ---: |
| total | 76.7639 | 87.0000 | 10.2361 |
| bottleneck | 11.0522 | 14.2500 | 3.1978 |

Bridge:

| bridge | value |
| --- | ---: |
| margin | 100 |
| customer | 100 |
| valuation repricing | 100 |
| backlog | 0 |
| contract | 0 |
| capital return | 0 |

세부 field:

| field | value |
| --- | ---: |
| revision_score | 100 |
| actual_profit_conversion_score | 80.0333 |
| structural_shortage | 68.4 |
| asp_pricing_power | 20 |
| backlog_rpo_visibility | 15 |
| contract_quality | 0 |
| capa_constraint | 0 |
| bottleneck_selected_raw | 58.1697 |
| bottleneck_raw_required_for_green | 75 |
| bottleneck_raw_deficit_to_green | 16.8303 |

쉬운 해석:

```text
"실적 전망"은 만점으로 들어갔다.
하지만 "HBM CAPA가 실제로 잠겼다"와 "backlog/contract로 매출 가시성이 잠겼다"는 점수가 거의 안 들어갔다.
그래서 병목 점수가 Green 문턱에서 3.20점 부족하다.
```

즉 하닉은 전망이 낮게 평가된 게 아니다.

전망은 높게 평가됐다.

깎인 곳은 HBM structural bottleneck을 증명하는 field다.

### 삼성전자 2024-04-01

| component | weighted score | max |
| --- | ---: | ---: |
| EPS/FCF | 22.0000 | 22 |
| earnings visibility | 11.1963 | 18 |
| bottleneck pricing | 6.9400 | 14 |
| market mispricing | 9.2784 | 12 |
| valuation rerating | 7.7990 | 10 |
| capital allocation | 0.0615 | 5 |
| information confidence | 11.4000 | 19 |
| risk penalty | 0.0000 | - |
| total | 68.6752 | 100 |

Green/Yellow gate:

| gate | actual | required | deficit |
| --- | ---: | ---: | ---: |
| total | 68.6752 | 87.0000 | 18.3248 |
| yellow total | 68.6752 | 75.0000 | 6.3248 |
| bottleneck | 6.9400 | 10.5000 | 3.5600 |
| visibility | 11.1963 | 13.5000 | 2.3037 |

Bridge:

| bridge | value |
| --- | ---: |
| margin | 100 |
| valuation repricing | 100 |
| customer | 0 |
| backlog | 0 |
| contract | 0 |

쉬운 해석:

```text
삼성은 "메모리 회복 + 실적 개선 + valuation"은 들어갔다.
하지만 "HBM 고객 qualification + 대량공급 allocation + capacity lock"이 없어서 C06이 아니라 C10 memory recovery로 남는다.
```

이건 삼성에 보수적인 것이 맞다.

다만 사용자 지적처럼, 하닉 positive조차 Green이 안 되는 것은 별개의 문제다.

## 왜 "예전 Green 연구"가 현재 Green 점수로 바로 안 바뀌나

원인은 4개다.

### 1. 연구 label은 runtime input이 아니다

`Stage3-Green` 연구 row는 calibration evidence다.

runtime score는 그 label을 직접 읽지 않는다.

쉬운 예:

```text
연구 row: "유한양행 2024-08-20은 structural success"
runtime score: FDA 승인, 로열티, 매출 전환, revision 같은 source-backed field만 사용
```

이 원칙은 맞다.

미래 수익률이나 과거 성공 label을 실시간 판단에 직접 쓰면 후견지명이 되기 때문이다.

### 2. positive unlock은 data-quality blocker에 막혔다

`full_4b_overlay_candidate` 21개가 모두 `blocked_by_data_quality`다.

blocker는:

```text
full_4b_overlay_needs_verified_non_proxy_evidence
```

즉 좋은 positive 연구가 있어도 source proxy나 evidence URL pending이 많으면 "점수 올리는 patch"로는 못 들어간다.

### 3. 적용된 patch는 전부 guardrail-only다

112개 patch가 적용됐지만 전부:

```text
max_delta = guardrail_only
```

이건 Stage2/4B/4C의 false positive를 막는 데는 효과가 있다.

하지만 하닉 같은 strong positive를 Green으로 올리지는 않는다.

### 4. weight는 바뀌었지만 component 원재료가 비어 있다

C06 weight는 이미 HBM에 맞다.

```text
C06 bottleneck max = 19
C06 visibility max = 21
C06 EPS/FCF max = 24
```

하지만 하닉 replay에서는:

```text
capa_constraint = 0
contract_quality = 0
backlog bridge = 0
contract bridge = 0
```

weight가 아무리 맞아도 원재료가 0이면 점수가 안 오른다.

예:

```text
수학 시험 배점을 10점에서 30점으로 올렸다.
그런데 답안지에 풀이가 비어 있으면 여전히 0점이다.
```

## 지금 전체 문제 정의

현재 문제는 "HBM 점수 하나가 낮다"가 아니다.

전체 문제는 다음이다.

```text
누적 연구자료는 archetype별로 positive/guard를 많이 알고 있다.
runtime weight도 archetype별로 바뀌었다.
하지만 positive evidence를 source-backed runtime primitive로 바꾸는 adapter가 부족하다.
그래서 좋은 케이스도 component 점수가 비거나 낮고,
적용된 rolling patch는 대부분 guardrail이라 점수를 올리지 않는다.
```

## 다음에 실제로 고쳐야 하는 것

우선순위는 threshold 완화가 아니다.

다음 네 가지다.

1. positive bridge field를 더 안정적으로 뽑기
   - C06: `hbm_capacity_pre_sold`, `customer_allocation`, `qualification_confirmed`, `backlog/contract visibility`
   - C21: `roe`, `pbr`, `treasury_share_cancellation`, `dividend_execution`, `credit_cost_quality`
   - C22: `csm_growth`, `k_ics`, `reserve_quality`, `loss_ratio_quality`, `payout_execution`
   - C23: `approval_to_revenue`, `royalty_route`, `partner_economics`, `reimbursement`
   - C28: `arr`, `nrr`, `renewal`, `retention`, `recurring_margin`

2. feature adapter가 primitive를 component로 바꾸게 하기
   - parser가 field를 뽑아도 component 공식이 안 쓰면 점수는 안 오른다.

3. positive/guard fixture pair를 정식 regression으로 고정하기
   - 하닉 positive vs 삼성 HBM catch-up guard
   - JB금융 positive vs value-up beta guard
   - 삼성화재 positive vs rate-cycle beta guard
   - 유한양행 approval positive vs HLB pre-PDUFA guard
   - 이엠로 SaaS/contract positive vs 안랩 political theme guard

4. promotion planner가 positive unlock을 언제 허용할지 별도 조건 만들기
   - 지금은 guardrail-only가 너무 압도적이다.
   - source-backed positive pair가 충분하면 bounded positive adapter patch를 허용해야 한다.

## 현재 작업 상태

이번 조사에서 확인된 것:

- `goal.md`의 표준 v12 ingest/apply는 실행되어 있었다.
- active profile은 `e2r_2_2`다.
- runtime archetype weight profile은 36개 canonical archetype을 갖는다.
- rolling calibration apply summary는 `production_default_scoring_changed=true`다.
- 하지만 실제 patch 112개는 모두 `guardrail_only`다.
- 하닉의 Green 실패는 EPS/FCF/revision 부족이 아니라 HBM bottleneck bridge field 부족이다.
- 삼성은 C10 memory recovery로 남는 것이 현재 evidence 기준으로는 맞다.
- 비-HBM C21/C22/C23/C28도 연구 row는 많지만 positive adapter가 약하거나 benchmark 후보에 안 올라온다.

아직 완료가 아닌 것:

- source-backed positive bridge를 실제 runtime field로 더 안정화해야 한다.
- positive adapter patch를 guardrail-only와 분리해서 설계해야 한다.
- 전체 archetype fixture pair가 정식 테스트로 고정되어야 한다.

