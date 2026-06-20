# Green Label Scorecard Parity Audit - 2026-06-19

## 결론

예전 연구자료에는 Stage3-Green이 실제로 많이 있다.

하지만 그 Green label이 현재 production `Stage3-Green`과 같은 뜻은 아니다.

연구자료의 `Stage3-Green`에는 세 종류가 섞여 있다.

1. 실제 대표 trigger로 쓸 수 있는 Green
2. Stage2 대비 늦었는지 비교하는 `label_comparison_only` Green
3. 결과적으로 false-positive였던 Green

따라서 "예전 Green이 많으니 그대로 점수표에 반영하면 된다"가 아니다. 먼저 Green label을 정제하고, 그 안의 evidence axis를 runtime primitive로 바꿔야 한다.

쉬운 예:

- 연구 row: "Stage3-Green, 2024-09-20"
- 실제 의미: "이 시점이면 Green 확인은 됐지만 이미 많이 올라서 늦었다"일 수 있다.
- runtime에 필요한 것: "2024-08-20에 이미 `approval_to_revenue_bridge`, `royalty_route`, `partner_economics_visible`이 있었는가?"

즉 Green 날짜 자체가 답이 아니라, 그 날짜 이전에 어떤 증거가 있었는지가 답이다.

## 1. Green row는 있지만 역할이 섞여 있다

파일:

- `data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl`
- `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`

대표 장부 기준:

| 항목 | 값 |
| --- | ---: |
| total representative rows | 12,471 |
| Stage3-Green rows | 381 |
| aggregate representative Green | 144 |
| `label_comparison_only` Green | 183 |
| current_profile_too_late Green | 130 |
| current_profile_false_positive Green | 85 |

중요한 점:

- Stage3-Green 381개 중 aggregate representative로 바로 쓸 수 있는 것은 144개다.
- 183개는 lateness 비교용이다.
- 85개는 현재 profile verdict 기준 false-positive다.

프롬프트에도 이 구분이 있다.

```text
aggregate_metric_inclusion =
  calibration_usable == true
  AND dedupe_for_aggregate == true
  AND aggregate_group_role == representative
  AND do_not_count_as_new_case != true
```

그리고 Green lateness audit은 별도 목적이다.

```text
green_lateness_ratio =
(Stage3_Green_entry_price - Stage2_Actionable_entry_price)
/
(peak_price_after_Stage2_Actionable - Stage2_Actionable_entry_price)
```

따라서 `Stage3-Green` 문자열만 보고 "이 row를 production Green 정답으로 써라"라고 하면 안 된다.

## 2. Green row의 component score도 production score와 1:1이 아니다

파일:

- `data/e2r/calibration/v12/v12_extracted_triggers_raw.jsonl`
- `data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl`

대표 Green 381개 중:

| field coverage | count |
| --- | ---: |
| `stage3_evidence_fields` 있음 | 257 |
| `raw_component_score_breakdown` 있음 | 27 |
| `raw_total_score` 있음 | 1 |

즉 Green label 대부분은 evidence field는 어느 정도 있지만, production 7개 component로 된 기계적 점수표는 없다.

`v12_extracted_triggers_raw.jsonl`에서 component 이름을 현재 7개 component로 정규화해 보면:

| 항목 | count |
| --- | ---: |
| raw component breakdown rows | 1,777 |
| 현재 component alias로 정규화 가능 | 1,295 |
| canonical-like scale | 1,142 |
| percent-axis/unbounded scale | 134 |
| partial/mixed scale | 19 |

문제는 scale이 섞여 있다는 것이다.

예:

- 어떤 row는 `eps_fcf_explosion=14`, `earnings_visibility=22`, `total=87`처럼 production point와 비슷하다.
- 어떤 row는 `eps_fcf_explosion=78`, `earnings_visibility=83`, `total=526`처럼 0~100 축 점수를 합친다.
- 어떤 row는 C06 Green인데 `eps_fcf_explosion`, `bottleneck_pricing`, `capital_allocation` 일부만 있어 total이 46이다.

따라서 raw component를 그대로 production score로 합산할 수도 없다.

## 3. 연구 Green scorecard와 현재 runtime scorecard의 차이

### 연구 raw component row

정규화 가능한 raw row 기준:

| trigger type | n | avg total | avg EPS | avg visibility | avg bottleneck | avg mispricing | avg valuation | avg capital | avg info |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Stage3-Green | 16 | 103.62 | 14.88 | 19.86 | 15.13 | 19.00 | 16.73 | 13.31 | 11.07 |
| Stage2-Actionable | 430 | 80.95 | 16.64 | 17.56 | 13.21 | 14.00 | 13.16 | 8.27 | 14.38 |
| Stage3-Yellow | 236 | 51.01 | 11.85 | 14.46 | 10.51 | 9.72 | 6.98 | 6.26 | 7.22 |

단, 위 표는 scale-mixed row까지 포함된 값이라 production threshold와 직접 비교하면 안 된다.

canonical-like row만 보면:

| trigger type | n | avg total | avg EPS | avg visibility | avg bottleneck | avg mispricing | avg valuation | avg capital | avg info |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Stage3-Green | 15 | 73.93 | 12.87 | 16.62 | 10.64 | 14.21 | 11.36 | 7.87 | 5.36 |
| Stage2-Actionable | 373 | 58.17 | 11.16 | 14.54 | 9.11 | 11.27 | 9.00 | 4.60 | 6.90 |
| Stage3-Yellow | 226 | 37.65 | 8.38 | 11.55 | 7.53 | 7.70 | 5.04 | 4.60 | 4.93 |

이 숫자가 의미하는 것은 "예전 Green이 약했다"가 아니다.

의미는 이렇다.

- 연구 Green label은 production 87점 gate 통과를 뜻하지 않는 경우가 많다.
- 연구 Green은 price path, lateness, stage3 evidence field, analyst 판단을 섞은 label이다.
- production runtime은 deterministic 7개 component와 AND gate만 본다.

그래서 연구 Green label을 production Green score로 쓰려면 변환 규칙이 필요하다.

## 4. 현재 runtime benchmark의 scorecard

파일:

- `output/0619_asof_stage_promotion_benchmark_current_2023_2026/score_components_by_candidate.csv`

현재 120개 benchmark replay:

| runtime stage | n | avg score | avg EPS | avg visibility | avg bottleneck | avg mispricing | avg valuation | avg capital | avg info |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 3-Yellow | 12 | 76.71 | 20.00 | 15.11 | 11.61 | 12.85 | 12.34 | 0.10 | 3.00 |
| 2 | 34 | 67.86 | 20.00 | 14.43 | 8.71 | 10.56 | 10.51 | 0.91 | 3.00 |
| 1 | 67 | 40.37 | 9.81 | 8.13 | 5.42 | 7.16 | 6.83 | 0.02 | 2.00 |
| 0 | 7 | 4.74 | 0.00 | 4.00 | 1.32 | 0.60 | 0.45 | 0.42 | 0.75 |

현재 runtime Stage3-Yellow는 EPS/FCF와 valuation은 강하다. 하지만 bottleneck과 capital allocation이 낮다.

하닉이 딱 이 모습이다.

```text
SK hynix 2024-04-25
EPS/FCF          20.00
visibility       14.7057
bottleneck       11.3960
mispricing       12.8520
valuation        12.3390
capital           0.0865
info              3.0
total            76.0596
```

Green gate에서 필요한 것은:

```text
total >= 87
visibility >= 15
bottleneck >= 15
```

하닉은 visibility가 거의 닿았지만 bottleneck이 멀다.

이유는 `HBM CAPA 제약`, `advanced packaging bottleneck`, `customer lock`, `capacity pre-sold`가 component로 충분히 번역되지 않기 때문이다.

## 5. 왜 "누적 연구가 있는데도" 이렇게 낮아졌나

### 원인 A: Green label의 용도가 섞여 있다

Stage3-Green 381개 중 183개는 `label_comparison_only`다.

예:

- Stage2-Actionable은 2024-08-20
- Stage3-Green은 2024-09-20
- Green은 맞지만 이미 많이 오른 뒤라 `current_profile_too_late`

이 경우 production이 배워야 하는 것은 "2024-09-20 Green을 맞춰라"가 아니다.

배워야 하는 것은 "2024-08-20에 어떤 evidence bridge가 있었길래 Stage2-Actionable이 빨랐는가"다.

### 원인 B: raw component score가 production component가 아니다

연구자료에는 `contract_score`, `backlog_visibility_score`, `customer_quality_score`, `policy_or_regulatory_score`, `relative_strength_score` 같은 축이 많다.

현재 production component는 7개뿐이다.

```text
eps_fcf_explosion
earnings_visibility
bottleneck_pricing
market_mispricing
valuation_rerating
capital_allocation
information_confidence
```

그래서 `customer_quality_score=9`가 있어도, 이것이 `customer_preorder_or_allocation`, `named_customer_confirmed`, `retention_or_renewal` 같은 runtime field로 바뀌지 않으면 점수에는 안 들어간다.

### 원인 C: scale normalization이 빠져 있다

동일한 `raw_component_score_breakdown` 이름 아래에 다음이 섞여 있다.

```text
production-like point score: total 87
axis-percent score: total 526
partial score: total 46
```

따라서 이 row들을 그대로 평균내거나 production score로 합산하면 오판한다.

### 원인 D: score_simulation은 runtime에서 직접 쓰이지 않는다

`src` 코드 검색 결과:

- `score_simulation` row는 calibration parser/CLI에서 수집된다.
- `raw_component_score_breakdown`은 runtime `DeterministicFeatureEngineer`나 `DeterministicScorer`가 직접 읽지 않는다.
- production score는 source-backed `ResearchReport`, `DisclosureEvent`, `NewsItem`, `FinancialActual`, `Consensus`에서 다시 계산된다.

즉 연구 scorecard는 "훈련 장부"이고, runtime score는 "원천 증거 재계산"이다.

훈련 장부의 축을 원천 증거 field로 바꾸는 bridge가 없으면 둘은 계속 어긋난다.

## 6. 아키타입별로 배워야 하는 것

### C06 HBM

연구가 말한 Green 조건:

```text
HBM demand
+ customer lock/allocation
+ CAPA or advanced packaging bottleneck
+ ASP/revision bridge
+ FCF or margin conversion
- catch-up / qualification lag / no supply deal guard
```

runtime에 필요한 field:

```text
hbm_capacity_constraint
advanced_packaging_bottleneck
capacity_precommitted
hbm_capacity_pre_sold
customer_preorder_or_allocation
customer_qualification_confirmed
no_supply_deal_signed
qualification_lag_risk
```

### C21 financial

연구 Green은 저PBR만이 아니다.

```text
ROE quality
+ executed buyback/cancellation
+ dividend visibility
+ credit-cost control
- policy beta only
```

runtime에 필요한 field:

```text
roe_pbr_gap_score
buyback_executed
treasury_share_cancellation
dividend_growth_visible
credit_cost_quality
npl_ratio_stable
capital_return_unconfirmed
```

### C22 insurance

연구 Green은 보험주 저PBR만이 아니다.

```text
CSM/reserve quality
+ K-ICS/solvency
+ payout execution
- reserve quality unconfirmed
```

runtime에 필요한 field:

```text
csm_growth
csm_margin_quality
k_ics_ratio
solvency_capital_buffer
reserve_quality_score
loss_ratio_quality
payout_execution
```

### C23/C25 bio/medical

연구 Green은 승인 뉴스만이 아니다.

```text
approval confirmed
+ revenue/royalty/reimbursement bridge
+ partner economics
- unresolved binary event
```

runtime에 필요한 field:

```text
regulatory_approval_confirmed
approval_to_revenue_bridge
royalty_route
partner_economics_visible
reimbursement_confirmed
binary_event_unresolved
```

### C28 software/security

연구 Green은 "보안/AI/SW 테마"가 아니다.

```text
ARR/RPO
+ retention/renewal
+ margin leverage
- theme-only/political/security headline risk
```

runtime에 필요한 field:

```text
arr_growth
rpo_to_sales
retention_or_renewal
nrr
churn_low
recurring_margin_leverage
contract_retention_unconfirmed
```

## 7. 다음 구현 기준

Green 연구자료를 production에 반영하려면 다음 순서가 맞다.

1. Green row를 필터링한다.
   - include: `calibration_usable=true`, `dedupe_for_aggregate=true`, `aggregate_group_role=representative`
   - exclude: `label_comparison_only`, obvious false-positive, source proxy only unless 별도 보정

2. `stage3_evidence_fields`를 runtime primitive로 매핑한다.
   - 예: `durable_customer_confirmation` -> `customer_qualification_confirmed`
   - 예: `financial_visibility` -> `approval_to_revenue_bridge` 또는 `medium_term_revision_visibility`

3. `score_simulation` axis를 7개 component로 바로 합산하지 않는다.
   - 먼저 scale을 정규화한다.
   - 그 다음 source-backed primitive로 연결한다.

4. positive/guard fixture를 한 쌍으로 만든다.
   - 하닉 positive vs 삼성 catch-up guard
   - C21 executed capital return vs low-PBR policy beta only
   - C22 CSM/K-ICS/payout vs reserve quality unconfirmed
   - C23 approval-to-revenue vs pre-PDUFA binary event
   - C28 ARR/retention vs security theme-only

5. runtime replay에서 확인한다.
   - Green 0개 문제는 완화되어야 한다.
   - R13/C30/C31/C32 guard는 무너지면 안 된다.

## 한 줄 진단

지금까지 연구가 쌓인 것은 맞다.

하지만 연구 Green label과 연구 scorecard는 production deterministic score가 아니다. Green label을 representative/label-comparison/false-positive로 먼저 나누고, 연구축을 source-backed runtime primitive로 바꾼 뒤에야 현재 pipeline 점수에 반영된다. 이 bridge가 없어서 하닉도 Yellow에 남고, 다른 아키타입도 같은 방식으로 막힌다.
