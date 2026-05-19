# Round-194 R3 Loop-7 Green Gate Review

## Green Required Evidence

- `binding_contract`
- `gwh_or_tonnage_volume`
- `customer_calloff_or_shipment`
- `utilization_rate`
- `opm_or_gross_margin_improvement`
- `fcf_after_capex`
- `eps_fcf_revision`
- `ev_or_ess_demand_durability`
- `tax_credit_quality_separated_from_underlying_profit`

## Green Forbidden Patterns

- `ev_theme`
- `ess_theme`
- `capa_announcement`
- `customer_name_only`
- `unconfirmed_media_report`
- `lithium_price_spike`
- `ipo_premium`
- `contract_value_without_actual_order`
- `operating_loss_ex_tax_credit`

## Shadow Score Adjustments

| axis | direction | points | reason |
| --- | --- | ---: | --- |
| `contract_binding_quality` | raise | 4 | 계약 headline보다 실제 구속력과 take-or-pay를 본다. |
| `gwh_volume_visibility` | raise | 4 | GWh/톤수 물량이 있어야 매출 경로를 계산할 수 있다. |
| `customer_order_calloff` | raise | 4 | 고객 주문 call-off와 출하 증거가 없으면 Stage 3를 막는다. |
| `opm_margin_visibility` | raise | 4 | ESS/EV 전환이 OPM 또는 gross margin으로 내려오는지 본다. |
| `fcf_after_capex` | raise | 4 | CAPEX 뒤 FCF가 남는지 확인한다. |
| `ess_revenue_conversion` | raise | 3 | ESS 전환은 매출 인식이 확인될 때 강해진다. |
| `utilization_rate` | raise | 3 | 공장 가동률은 CAPA announcement의 반대편 검증축이다. |
| `customer_quality` | raise | 3 | 고객의 모델/전략/신용도가 계약 지속성을 좌우한다. |
| `tax_credit_quality` | raise | 2 | AMPC/세액공제는 본업 이익과 분리해서 본다. |
| `ev_theme` | lower | -5 | EV 성장 테마만으로 Stage 3를 만들지 않는다. |
| `capa_announcement` | lower | -4 | CAPA는 비용이 먼저 나갈 수 있으므로 매출/마진/FCF 전에는 감점한다. |
| `customer_name_only` | lower | -4 | Tesla/Ford 같은 고객명만으로는 충분하지 않다. |
| `non_binding_supply_mou` | lower | -4 | 비구속 MOU는 Stage 1 라우팅에 가깝다. |
| `policy_subsidy_expectation` | lower | -3 | 정책/보조금 기대는 본업 수익성과 분리한다. |
| `lithium_price_event` | lower | -3 | 리튬 가격 이벤트는 구조적 Green이 아니라 cycle/event일 수 있다. |
| `ipo_theme_premium` | lower | -4 | IPO 수급과 그룹 스토리는 price-only 위험이다. |
| `group_vertical_integration_story` | lower | -3 | 내재화 스토리는 외부 고객/OPM/FCF 전에는 제한한다. |
| `ess_media_report_unconfirmed` | lower | -3 | 미확정 ESS 보도는 disclosure confidence cap을 건다. |
| `tax_credit_without_operating_profit` | lower | -3 | AMPC 제외 적자는 Green block에 가깝다. |

## What Not To Change

- Do not apply these weights to production scoring yet.
- Do not use Round194 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds to force promotion.
- Do not invent GWh, shipments, utilization, OPM, FCF, stage prices, or MFE/MAE.
