# Round-207 R3 Loop-8 Green Gate Review

## Green Required Evidence

- `binding_contract`
- `actual_calloff`
- `gwh_or_tonnage_volume`
- `utilization_improvement`
- `opm_or_gross_margin_improvement`
- `fcf_after_capex`
- `subsidy_excluded_profit_quality`
- `customer_ev_strategy_risk_passed`
- `price_path_after_evidence`

## Green Forbidden Patterns

- `customer_name_only`
- `contract_value_headline_only`
- `ess_or_lfp_theme_only`
- `capa_conversion_only`
- `ampc_excluded_profit_missing_or_negative`
- `ev_demand_slowdown_ignored`
- `ipo_or_vertical_integration_story_only`
- `lithium_price_event_only`

## Shadow Score Adjustments

| axis | direction | points | reason |
| --- | --- | ---: | --- |
| `binding_contract_quality` | raise | 5 | 계약이 있어도 binding/call-off 구조가 보일 때만 R3 visibility가 오른다. |
| `actual_calloff` | raise | 5 | L&F 사례처럼 고객명과 계약금액 headline은 call-off가 없으면 무너질 수 있다. |
| `gwh_or_tonnage_volume` | raise | 5 | 배터리 계약은 GWh/tonnage와 배송 시점이 확인되어야 매출 경로가 보인다. |
| `utilization_rate` | raise | 5 | EV 라인 전환이나 ESS 증설은 가동률 개선 전까지 Stage 3가 아니다. |
| `opm_visibility` | raise | 5 | OPM 또는 gross margin 개선이 없으면 EPS/FCF 체급 변화가 약하다. |
| `fcf_after_capex` | raise | 5 | CAPEX 이후 FCF가 확인되어야 배터리 Green 후보가 된다. |
| `ess_revenue_conversion` | raise | 4 | ESS 계약은 delivery/revenue conversion이 보일 때 Stage 2를 넘어선다. |
| `customer_quality` | raise | 4 | 고객의 EV 전략 지속성과 주문 품질을 따로 확인한다. |
| `subsidy_quality_adjustment` | raise | 4 | AMPC/보조금을 제외한 이익 품질을 분리한다. |
| `ev_theme_only` | lower | -5 | EV 테마만으로는 OPM/FCF 개선을 증명하지 못한다. |
| `ess_theme_only` | lower | -4 | ESS/LFP 전환 기대만 있고 배송·마진이 없으면 Green 금지다. |
| `customer_name_only` | lower | -5 | Tesla/Ford 같은 고객명만으로는 actual call-off를 대체할 수 없다. |
| `contract_value_headline_without_calloff` | lower | -5 | 계약금액 headline은 call-off와 매출 인식 전까지 confidence cap이다. |
| `capa_announcement` | lower | -4 | CAPA 발표는 가동률과 FCF 전까지 부담일 수 있다. |
| `subsidy_dependent_profit` | lower | -5 | AMPC 포함 이익만 좋고 제외 이익이 약하면 Green을 막는다. |
| `negative_fcf_or_debt_burden` | lower | -5 | SK온 사례처럼 손실과 부채는 구조적 rerating을 차단한다. |
| `ipo_or_vertical_integration_story` | lower | -4 | 전구체/수직계열화/IPO narrative는 외부 고객·가동률·OPM 전까지 부족하다. |
| `lithium_price_event` | lower | -4 | 리튬 가격 이벤트는 event premium 또는 cycle로 분리한다. |

## What Not To Change

- Do not apply these weights to production scoring yet.
- Do not use Round207 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds to force promotion.
- Do not invent full OHLC, stage prices, or MFE/MAE when only reported anchors exist.
- Do not treat EV/ESS theme, customer name, contract headline, CAPA conversion, lithium event, or IPO story as Green evidence alone.
