# Round 281 R12 Green Gate Review

Do not apply these weights to production scoring yet.

R12 Stage 3-Green is not `food inflation`, `birthrate rebound`, `waste policy`, `logistics alliance`, `agri automation theme`, or `IPO size`. It requires pass-through, volume, utilization, trust, enrolment, order backlog, margin, FCF, and price-after-evidence.

## Required Fields

- input_cost_pass_through_confirmed
- inventory_waste_control_confirmed
- gross_margin_stability_confirmed
- feed_cost_hedging_confirmed
- disease_supply_chain_resilience_confirmed
- actual_order_backlog_confirmed
- dealer_sellthrough_confirmed
- logistics_unit_economics_confirmed
- data_trust_service_continuity_confirmed
- waste_tipping_fee_utilization_confirmed
- enrolment_arpu_retention_confirmed
- post_listing_order_book_and_export_margin_confirmed
- cash_conversion_confirmed
- price_path_after_evidence

## Forbidden Patterns

- food_inflation_headline_only
- grain_price_event_only
- disease_supply_shock_as_benefit_only
- aging_farm_theme_only
- logistics_revenue_uplift_without_margin
- birthrate_headline_without_enrolment
- recycling_policy_without_tipping_fee
- IPO_size_without_aftermarket_demand
- data_breach_or_trust_failure

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| input_cost_pass_through | raise | 5 | 농식품 원가 shock 이후 판가 전가가 확인되어야 한다. |
| inventory_waste_control | raise | 5 | 배추·식품·폐기물은 재고와 폐기 관리가 gross margin을 좌우한다. |
| feed_cost_hedging | raise | 5 | 사료·축산은 곡물가격 hedge와 재고 buffer가 핵심이다. |
| disease_supply_chain_resilience | raise | 5 | bird flu 같은 질병 shock는 수입규제와 공급망 회복을 같이 봐야 한다. |
| actual_order_backlog | raise | 5 | 농기계와 IPO 제조업은 theme보다 실제 order book이 중요하다. |
| dealer_sellthrough | raise | 5 | 농기계는 dealer inventory와 North America sell-through가 Stage 3 조건이다. |
| logistics_unit_economics | raise | 5 | 물류 계약은 물동량, 단가, 자동화, 인건비가 닫혀야 한다. |
| data_trust_service_continuity | raise | 5 | 생활서비스는 편의성보다 데이터 trust와 서비스 연속성이 먼저다. |
| waste_tipping_fee_utilization | raise | 5 | 폐기물 인프라는 처리량, tipping fee, utilization, capex 회수를 봐야 한다. |
| enrolment_ARPU_conversion | raise | 5 | 출산율 headline은 enrolment, ARPU, retention으로 내려와야 한다. |
| food_inflation_headline_only | lower | -5 | 식품가격 상승 headline만으로 식품주 Green을 만들지 않는다. |
| grain_price_event_only | lower | -5 | 곡물가격 이벤트는 사료·축산 margin gate다. |
| disease_supply_shock_as_benefit_only | lower | -5 | 질병 shock를 가격상승 수혜로만 보면 4C risk를 놓친다. |
| aging_farm_theme_only | lower | -5 | 농촌 고령화 theme만으로 농기계 주문을 만들지 않는다. |
| logistics_revenue_uplift_without_margin | lower | -5 | 물류 매출 증가 추정은 unit margin 없이는 Stage 2에 그친다. |
| birthrate_headline_without_enrolment | lower | -5 | 출생률 반등만으로 교육·돌봄 매출을 만들지 않는다. |
| recycling_policy_without_tipping_fee | lower | -5 | 폐기물 정책 headline은 fee/utilization/FCF 전까지 제한한다. |
| IPO_size_without_aftermarket_demand | lower | -5 | IPO 규모는 상장 후 수요와 order book 전까지 품질 증거가 아니다. |
| data_breach_or_trust_failure | lower | -5 | 데이터 breach는 생활서비스 hard gate다. |

## Easy Examples
- `cabbage price spike` is a cost gate until pass-through and margin hold.
- `CJ Logistics revenue uplift` is Stage 2 until unit economics and automation productivity are visible.
- `birthrate rebound` is not education/childcare Green until enrolment, ARPU and retention appear.
