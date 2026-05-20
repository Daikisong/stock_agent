# Round 294 R12 Green Gate Review

Do not apply these weights to production scoring yet.

R12 Stage 3-Green is not `headline is good`. It requires concrete operating numbers. For example, a birthrate rebound becomes useful only when childcare customer count, ARPU and margin appear.

## Required Fields

- farm_income_order_visibility_confirmed
- dealer_inventory_normalization_confirmed
- export_order_and_ASP_margin_confirmed
- food_input_cost_pass_through_confirmed
- volume_retention_after_price_increase_confirmed
- same_store_sales_franchise_fee_confirmed
- delivery_take_rate_unit_economics_confirmed
- labor_service_continuity_confirmed
- recycling_yield_gate_fee_utilization_confirmed
- cleanup_liability_control_confirmed
- childcare_customer_count_ARPU_margin_confirmed
- education_enrolment_retention_regulatory_durability_confirmed
- price_path_after_evidence

## Forbidden Patterns

- farm_equipment_recovery_headline_only
- food_input_inflation_as_pricing_power
- celebrity_AI_visit_without_restaurant_economics
- M&A_scale_without_take_rate_margin
- fast_delivery_without_labor_continuity
- waste_platform_EV_without_recycling_yield
- birthrate_headline_without_customer_count
- hagwon_demand_without_policy_and_demographic_check

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| farm_income_order_visibility | raise | 5 | 농기계는 회복 기대보다 농가소득, dealer inventory, order와 ASP/margin이 먼저다. |
| dealer_inventory_normalization | raise | 5 | 수출 농기계는 dealer inventory overhang이 풀려야 Stage 3 후보가 된다. |
| food_input_cost_pass_through | raise | 5 | 식품 원가 상승은 판가 전가와 volume retention 전에는 margin 악재다. |
| same_store_sales_franchise_fee | raise | 5 | 프랜차이즈 밈은 동일점 매출과 가맹 수수료로 닫혀야 한다. |
| delivery_take_rate_unit_economics | raise | 5 | 배달앱 M&A는 GMV보다 take-rate, rider cost, merchant churn이 핵심이다. |
| labor_service_continuity | raise | 5 | 생활물류 moat는 빠른 배송뿐 아니라 노동·규제·운영 연속성이다. |
| recycling_yield_gate_fee_margin | raise | 5 | 폐기물 인프라는 EV보다 recycling yield, gate fee, utilization, cleanup liability가 중요하다. |
| childcare_actual_customer_growth | raise | 5 | 출산율 headline은 실제 고객수, ARPU, 보조금 capture와 margin으로 내려와야 한다. |
| education_enrolment_retention | raise | 5 | 사교육 수요는 등록률, retention, 교사 비용, 규제 내구성으로 검증한다. |
| headline_only_event | lower | -5 | 유명인 방문, 출산율 headline, M&A headline만으로 Green을 만들지 않는다. |

## Easy Examples
- `Jensen chicken photo` is not restaurant Green without same-store sales.
- `rice price +18.6%` is not food-company Green before pass-through and margin.
- `Baemin 8T won bid` is Stage 2 until approval and unit economics close.
