# Round-195 R4 Loop-7 Green Gate Review

## Green Required Evidence

- `actual_product_spread`
- `cost_curve_advantage`
- `supply_discipline_or_capacity_shutdown_confirmed`
- `inventory_not_building`
- `fcf_conversion_or_cashflow_improvement`
- `price_floor_or_offtake_or_long_term_contract`
- `medium_term_eps_revision`
- `capex_and_dilution_risk_passed`

## Green Forbidden Patterns

- `commodity_price_spike`
- `tender_offer_premium`
- `governance_battle`
- `policy_support_expectation`
- `unconfirmed_media_report`
- `restructuring_plan_only`
- `lithium_or_polysilicon_price_event`
- `geopolitical_refining_margin_spike`

## Shadow Score Adjustments

| axis | direction | points | reason |
| --- | --- | ---: | --- |
| `actual_product_spread` | raise | 4 | 가격 이벤트가 아니라 실제 제품 spread를 확인한다. |
| `fcf_after_working_capital` | raise | 4 | 재고와 운전자본 뒤에 남는 FCF가 중요하다. |
| `supply_discipline_confirmed` | raise | 4 | 공급규율이 확인될 때만 commodity cycle을 구조화한다. |
| `capacity_shutdown_confirmed` | raise | 3 | 구조조정은 실제 shut-down/가동중단이 확인되어야 강해진다. |
| `price_floor_or_offtake` | raise | 4 | 가격 floor와 offtake가 있으면 전략자원 visibility가 올라간다. |
| `cost_curve_advantage` | raise | 3 | 원가곡선 우위가 없으면 가격 하락 때 이익이 무너진다. |
| `strategic_customer_or_government_offtake` | raise | 3 | 전략광물은 정부/고객 offtake가 있어야 Stage 2 이상이다. |
| `inventory_normalization` | raise | 3 | 재고 정상화는 spread 지속성의 핵심이다. |
| `capital_return_from_cashflow` | raise | 2 | 현금흐름 기반 환원은 cycle과 구조 변화를 구분한다. |
| `commodity_price_up_only` | lower | -5 | 원자재 가격 상승만으로 Stage 3를 만들지 않는다. |
| `restructuring_plan_without_margin` | lower | -3 | 구조조정 계획만 있고 spread/OPM이 없으면 Stage 2 watch다. |
| `policy_support_without_fcf` | lower | -3 | 정책 지원은 FCF 전까지 event premium이다. |
| `tender_offer_or_governance_premium` | lower | -4 | 공개매수/경영권 분쟁 프리미엄은 구조적 EPS/FCF와 분리한다. |
| `unconfirmed_media_report` | lower | -4 | 미확인 SpaceX/매각 보도는 Green 근거가 아니다. |
| `capacity_cut_expectation_only` | lower | -3 | 기대만 있고 실제 capacity shutdown이 없으면 제한한다. |
| `lithium_price_event` | lower | -4 | 리튬 가격 이벤트는 cycle/event premium으로 본다. |
| `refining_margin_geopolitical_shock` | lower | -3 | 전쟁성 정제마진 spike는 구조적 Green이 아니다. |
| `customer_or_contract_unconfirmed` | lower | -3 | 고객/계약 미확인은 disclosure confidence cap이다. |
| `capex_heavy_project_pre_revenue` | lower | -3 | 대규모 CAPEX 프로젝트는 매출/FCF 전에는 부담이다. |

## What Not To Change

- Do not apply these weights to production scoring yet.
- Do not use Round195 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds to force promotion.
- Do not invent spreads, offtake, capacity shutdown, margins, stage prices, or MFE/MAE.
