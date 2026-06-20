# EvidenceBridgeSpec Draft - 2026-06-19

## 결론

현재 runtime은 연구축을 바로 점수로 쓰지 않는다.

흐름은 이렇다.

```text
research text
-> report_parser.py parsed_fields
-> features.py sub_scores / sector_metrics
-> 7 canonical components
-> scoring.py archetype weight
-> staging.py Green gate
```

따라서 연구자료에 `customer_quality_score=9`, `margin_bridge_score=9`, `reserve_quality_score=8`이 있어도, 그것이 runtime primitive field로 바뀌지 않으면 Green 점수에 제대로 들어가지 않는다.

쉬운 예:

- 연구: "하닉 HBM 2024 물량은 sold-out이고 Nvidia shipment가 있다."
- 필요한 runtime field: `hbm_capacity_pre_sold`, `hbm_capacity_constraint`, `customer_preorder_or_allocation`, `medium_term_revision_visibility`
- 현재 문제: 일부 문장은 `hbm_demand_mentioned`나 `pricing_power_mentioned`까지만 가고, CAPA/customer lock field로 충분히 안 간다.

## 현재 코드에서 점수가 들어가는 문

기준 코드:

- `src/e2r/research/report_parser.py`
- `src/e2r/features.py`
- `src/e2r/sector_profiles.py`
- `src/e2r/scoring.py`
- `src/e2r/staging.py`

### 7개 canonical component

`src/e2r/scoring.py`의 runtime score input은 7개뿐이다.

| component | max | 의미 |
| --- | ---: | --- |
| `eps_fcf_explosion` | 20 | EPS/FCF/OP 성장 |
| `earnings_visibility` | 20 | 계약, backlog, structural visibility, revision, FCF quality |
| `bottleneck_pricing` | 20 | CAPA, ASP, structural shortage, sector bottleneck |
| `market_mispricing` | 15 | revision, valuation, structural shortage, price underreaction |
| `valuation_rerating` | 15 | valuation runway, revision, structural shortage |
| `capital_allocation` | 5 | capital return/dilution/capex quality |
| `information_confidence` | 5 | source coverage/confidence |

즉 C21의 `capital_return_execution`, C22의 `CSM`, C23의 `approval_to_revenue`, C28의 `retention`은 별도 component가 아니다. 반드시 위 7개 중 하나 또는 diagnostic gate로 번역되어야 한다.

### Green gate

`src/e2r/staging.py`의 Green gate는 AND 구조다.

| gate | current threshold |
| --- | ---: |
| total | 87 |
| EPS/FCF | 17 |
| visibility | 15 |
| bottleneck | 15 |
| mispricing | 10 |
| valuation | 10 |
| revision | 55 |
| structural visibility | 45 |

쉬운 예:

- 하닉은 EPS/FCF와 revision은 좋다.
- 하지만 bottleneck이 15 미만이면 Green은 닫힌다.
- 그래서 "좋은 전망"만으로는 안 되고, 그 전망이 `capa/backlog/customer/FCF` primitive로 번역되어야 한다.

## 현재 runtime primitive

### 이미 강하게 쓰는 field

| score area | current primitive fields |
| --- | --- |
| contract quality | `contract_duration_months`, `lta_duration_months`, `contract_amount_to_prior_sales`, `contract_to_sales`, `prepayment_exists`, `customer_prepayment`, `non_cancellable`, `take_or_pay`, `multi_year_contract`, `government_customer` |
| backlog/RPO visibility | `order_backlog_to_sales`, `backlog_to_sales`, `rpo_to_sales`, `backlog_yoy_pct`, `rpo_yoy_pct`, `new_orders_yoy_pct`, `record_backlog`, `customer_preorder_or_allocation`, `capacity_precommitted`, `hbm_capacity_pre_sold` |
| CAPA constraint | `capa_utilization_pct`, `capacity_utilization_pct`, `lead_time_months`, `capa_expansion_pct`, `capacity_expansion_pct`, `capa_locked_years`, `capacity_locked_years`, `capacity_constraint`, `capa_shortage`, `hbm_capacity_constraint`, `advanced_packaging_bottleneck` |
| ASP/pricing | `asp_yoy_pct`, `price_increase_pct`, `pricing_yoy_pct`, `high_margin_mix_pct`, `export_mix_pct`, `premium_mix_pct`, `pricing_power_confirmed`, `pricing_power_mentioned`, `asp_increase_mentioned` |
| revision | `eps_revision_pct`, `op_revision_pct`, `fcf_revision_pct`, `target_price_revision_pct`, `estimate_upgrade_mentioned`, `earnings_beat_mentioned` |
| actual conversion | `actual_op_yoy_pct`, `actual_eps_yoy_pct`, `actual_fcf_yoy_pct`, `actual_sales_yoy_pct`, `opm_expansion_pctp` |
| export/channel | `export_ratio`, `us_revenue_ratio`, `export_growth_pct`, `export_channel_expansion`, `overseas_channel_expansion`, `brand_channel_expansion`, `platform_distribution_scale` |
| HBM domain | `hbm_demand_mentioned`, `memory_price_increase_mentioned`, `supply_discipline_mentioned`, `customer_preorder_or_allocation`, `minimum_revenue_guarantee`, `hbm_capacity_constraint`, `advanced_packaging_bottleneck` |

### 현재 parser가 어느 정도 뽑는 field

`report_parser.py`는 다음 종류를 이미 뽑는다.

- `hbm_demand_mentioned`
- `memory_price_increase_mentioned`
- `supply_discipline_mentioned`
- `customer_preorder_or_allocation`
- `hbm_capacity_pre_sold`
- `hbm_capacity_constraint`
- `pricing_power_mentioned`
- `export_channel_expansion`
- `recurring_consumer_demand`
- `high_margin_mix_improvement`
- `government_customer`
- `multi_year_contract`

하지만 토큰이 좁다.

예:

- `공급 부족`, `tight supply`, `capacity constraint`는 잡는다.
- `HBM CAPA 제약`, `advanced packaging bottleneck`, `CoWoS bottleneck`, `packaging capacity allocated` 같은 표현은 누락될 수 있다.

## 연구축 -> runtime primitive mapping

### 공통축

| research axis | runtime primitive | target component/gate |
| --- | --- | --- |
| `margin_bridge_score` | `opm_expansion_pctp`, `actual_op_yoy_pct`, `actual_fcf_yoy_pct`, `high_margin_mix_improvement`, `cash_conversion_quality` | EPS/FCF, visibility, valuation |
| `customer_quality_score` | `named_customer_confirmed`, `hyperscaler_customer`, `government_customer`, `customer_preorder_or_allocation`, `repeat_order_confirmed`, `customer_qualification_confirmed` | visibility, domain evidence, bottleneck |
| `backlog_visibility_score` | `order_backlog_to_sales`, `rpo_to_sales`, `record_backlog`, `delivery_schedule`, `capacity_precommitted` | visibility, structural visibility |
| `contract_score` | `contract_duration_months`, `contract_amount_to_prior_sales`, `prepayment_exists`, `non_cancellable`, `take_or_pay`, `minimum_revenue_guarantee` | contract gate, visibility |
| `valuation_repricing_score` | `target_multiple_delta`, `est_per`, `est_pbr`, `roe`, `market_frame_shift`, `price_stage_score` | valuation, mispricing |
| `execution_risk_score` | `delivery_delay`, `legal_or_contract_risk`, `customer_delay`, `quality_failure`, `supply_chain_disruption` | risk penalty, 4B/4C guard |
| `accounting_trust_risk_score` | `accounting_or_trust_issue`, `auditor_issue`, `restatement_risk`, `share_count_drift`, `source_conflict` | red-team, information confidence |

### C06/C07/C08/C10 semis/HBM

| research phrase | required primitive | current status |
| --- | --- | --- |
| HBM capacity sold out/booked | `hbm_capacity_pre_sold`, `capacity_precommitted`, `customer_preorder_or_allocation` | 일부 있음, token 보강 필요 |
| HBM CAPA 제약 | `hbm_capacity_constraint`, `capa_shortage`, `capacity_constraint` | `CAPA 부족`은 잡지만 `CAPA 제약`류 보강 필요 |
| advanced packaging bottleneck | `advanced_packaging_bottleneck`, `hbm_capacity_constraint` | runtime은 읽지만 parser 직접 추출 약함 |
| Nvidia/customer qualification | `customer_qualification_confirmed`, `named_customer_confirmed`, `hyperscaler_customer` | 전용 primitive 부족 |
| partial pass/no supply deal | `partial_qualification_only`, `no_supply_deal_signed`, `customer_qualification_unresolved` | guard primitive 부족 |
| HBM catch-up without volume | `hbm_catchup_without_volume`, `qualification_lag_risk` | guard primitive 부족 |

필요한 Green 조건:

```text
hbm_customer_capacity_green =
  hbm_capacity_lock
  + named customer qualification
  + revision/estimate bridge
  + ASP/margin/FCF bridge
  - qualification lag / no supply deal guard
```

### C20 consumer export

| research phrase | required primitive | target |
| --- | --- | --- |
| sell-through/reorder | `sell_through_confirmed`, `channel_reorder_confirmed`, `repeat_order_confirmed` | recurring demand, visibility |
| global distribution platform | `platform_distribution_scale`, `overseas_channel_expansion`, `export_channel_expansion` | domain evidence |
| margin bridge | `opm_expansion_pctp`, `high_margin_mix_improvement`, `actual_fcf_yoy_pct` | EPS/FCF, visibility |
| roadshop/channel rebound only | `legacy_channel_rebound_only`, `inventory_overhang`, `discount_rate_pressure` | guard |

### C21 financial

현재 runtime은 `roe`, `est_pbr`, `capital_allocation` 일부만 간접적으로 본다. 금융 전용 profile은 없다.

| research phrase | required primitive | target |
| --- | --- | --- |
| low PBR + high ROE | `roe`, `est_pbr`, `roe_pbr_gap_score` | valuation/mispricing |
| executed buyback/cancellation | `buyback_announced`, `buyback_executed`, `treasury_share_cancellation` | capital allocation, confidence |
| dividend visibility | `dividend_payout_target`, `dividend_growth_visible` | capital allocation |
| credit-cost control | `credit_cost_quality`, `npl_ratio_stable` | visibility/risk |
| value-up beta only | `valueup_policy_beta_only`, `capital_return_unconfirmed` | guard |

필요한 Green 조건:

```text
financial_green =
  low valuation
  + ROE quality
  + executed capital return
  + no credit-cost/trust break
```

### C22 insurance

현재 runtime에는 CSM/K-ICS/reserve 전용 primitive가 없다.

| research phrase | required primitive | target |
| --- | --- | --- |
| CSM visibility | `csm_growth`, `csm_margin_quality`, `new_business_csm_quality` | earnings visibility |
| K-ICS/solvency | `k_ics_ratio`, `solvency_capital_buffer` | visibility/confidence |
| reserve quality | `reserve_quality_score`, `loss_ratio_quality`, `claim_ratio_stable` | risk/visibility |
| shareholder return | `payout_execution`, `buyback_cancellation`, `dividend_visibility` | capital allocation |
| rate-cycle beta only | `insurance_rate_cycle_beta_only`, `reserve_quality_unconfirmed` | guard |

필요한 Green 조건:

```text
insurance_green =
  CSM/reserve quality
  + solvency capital
  + payout execution
  + low accounting/trust risk
```

### C23/C24/C25 bio/medical

현재 runtime은 approval/commercialization/reimbursement profile이 없다.

| research phrase | required primitive | target |
| --- | --- | --- |
| FDA approval confirmed | `regulatory_approval_confirmed`, `approval_scope_clear` | information confidence/domain |
| approval to revenue | `approval_to_revenue_bridge`, `launch_timing_visible`, `sales_milestone_visible` | earnings visibility |
| royalty/partner economics | `partner_economics_visible`, `royalty_route`, `milestone_payment_visible` | visibility/valuation |
| reimbursement/device adoption | `reimbursement_confirmed`, `hospital_adoption_visible`, `billing_volume_visible` | visibility |
| pre-PDUFA expectation | `binary_event_unresolved`, `approval_not_confirmed`, `trial_endpoint_unresolved` | guard/red-team |

필요한 Green 조건:

```text
bio_green =
  confirmed approval or endpoint
  + direct economic owner route
  + revenue/royalty/reimbursement bridge
  - unresolved binary event risk
```

### C27/C28 software/security

현재 runtime은 AI infra 일부만 있고 SaaS/security/content 전용 profile은 약하다.

| research phrase | required primitive | target |
| --- | --- | --- |
| recurring contract | `arr_growth`, `rpo_to_sales`, `contract_renewal_visible`, `retention_or_renewal` | visibility |
| retention quality | `nrr`, `churn_low`, `seat_expansion_visible` | visibility/domain |
| partner economics | `partner_contract_quality`, `platform_partner_confirmed` | contract/domain |
| margin leverage | `opm_expansion_pctp`, `cloud_margin_visible`, `recurring_margin_leverage` | EPS/FCF |
| political/theme security | `political_theme_risk`, `price_only_security_brand`, `contract_retention_unconfirmed` | guard |

필요한 Green 조건:

```text
software_green =
  recurring revenue bridge
  + retention/renewal
  + margin leverage
  + no theme-only/political risk
```

### C30/C31/C32 guard-heavy archetypes

이 그룹은 Green unlock보다 false-positive 방어가 먼저다.

| group | required primitive | guard purpose |
| --- | --- | --- |
| C30 PF/construction | `pf_exposure_repair`, `liquidity_bridge`, `legal_quality_risk`, `defect_liability_risk`, `balance_sheet_cash_bridge` | PF/법적 리스크 무시한 Stage2/Green 차단 |
| C31 policy | `policy_to_company_cash_route`, `subsidy_capture_visible`, `policy_legal_enforceability`, `beneficiary_specificity` | 정책 headline-only 차단 |
| C32 governance | `tender_floor`, `control_premium_finite`, `minority_cash_path`, `ongoing_rerating_route` | tender/event premium을 영구 Green으로 착각 차단 |

## 구현 hook point

### 1. Parser

파일:

- `src/e2r/research/report_parser.py`

해야 할 일:

- `_add_qualitative_e2r_fields()`에 domain primitive 추출을 추가한다.
- 단, 검색어 생성 하드코딩이 아니라 이미 가져온 문서에서 evidence field를 뽑는 것이다.

예:

```text
HBM CAPA 제약 -> hbm_capacity_constraint
CSM 증가/K-ICS -> csm_growth, k_ics_ratio
FDA approval + royalty -> regulatory_approval_confirmed, royalty_route
ARR/RPO/retention -> arr_growth, rpo_to_sales, retention_or_renewal
```

### 2. Feature adapter

파일:

- `src/e2r/features.py`
- `src/e2r/sector_profiles.py`

해야 할 일:

- 9개 sector profile만으로 부족한 Green-heavy archetype을 보강한다.
- 최소 우선순위:
  - C21 finance
  - C22 insurance
  - C23/C25 bio/medical
  - C27/C28 content/software/security
  - C30/C31/C32 guard profiles

### 3. Score loss report

파일 후보:

- `src/e2r/backtest/asof_stage_promotion_autopsy.py`
- `src/e2r/cli/analyze_asof_stage_promotion.py`

해야 할 일:

- Green 실패 시 `failed_stage3_bottleneck`만 보여주지 않는다.
- expected runtime field와 observed runtime field를 같이 출력한다.

예:

```text
research_axis=HBM_capacity_lock
expected=hbm_capacity_pre_sold,hbm_capacity_constraint,customer_preorder_or_allocation
observed=customer_preorder_or_allocation
lost=capa_constraint=0,backlog_rpo_visibility=15,bottleneck_pricing=11.63/20
```

## 검증 기준

패치가 맞으려면 다음을 동시에 통과해야 한다.

1. C06 하닉 positive가 Green 또는 의도한 Green-candidate로 올라온다.
2. C06 삼성 catch-up/qualification-fail guard가 Green으로 같이 뚫리지 않는다.
3. C21/C22/C23/C28 같은 비-HBM fixture도 positive/guard 쌍을 통과한다.
4. 운영 replay에서 Green 0개 문제가 완화된다.
5. R13/C30/C31/C32 guard-heavy 반례가 무너지지 않는다.

## 한 줄 진단

지금 필요한 것은 점수 기준 완화가 아니라 evidence bridge다.

연구축을 runtime primitive로 번역하고, 그 primitive가 7개 component와 Green gate까지 도달해야 한다. 이 번역층이 없으면 연구자료가 아무리 누적되어도 하닉 같은 Green 후보는 Yellow에 남고, 다른 아키타입도 같은 방식으로 막힌다.
