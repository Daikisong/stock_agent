# Round 287 R5 Green Gate Review

Do not apply these weights to production scoring yet.

R5 Stage 3-Green is not `K-food`, `K-beauty`, `tourism`, `JV`, or `brand` as a label. It requires sell-through, ASP, capacity-to-revenue conversion, tariff/regulatory fit, take-rate, data trust, fulfilment unit economics and price-path evidence.

## Required Fields

- export_sellthrough_confirmed
- brand_ASP_power_confirmed
- capacity_to_revenue_conversion_confirmed
- offline_channel_sellthrough_confirmed
- tariff_absorption_confirmed
- tourist_spend_per_head_confirmed
- ecommerce_take_rate_confirmed
- data_trust_internal_control_confirmed
- fulfillment_unit_economics_confirmed
- domestic_consumption_sensitivity_measured
- price_path_after_evidence

## Forbidden Patterns

- viral_brand_headline_only
- visitor_count_only
- online_ecommerce_growth_without_offline_sellthrough
- JV_scale_without_take_rate
- revenue_uplift_without_unit_economics
- IPO_or_stock_pop_without_repeat_purchase
- consumer_export_story_without_local_regulatory_fit
- domestic_retail_ignored
- data_breach_or_customer_trust_failure

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| export_sellthrough | raise | 5 | K-food/K-beauty 수출은 sell-in보다 sell-through가 먼저다. |
| brand_ASP_power | raise | 5 | 브랜드가 실제 판가와 마진으로 닫혀야 한다. |
| capacity_to_revenue_conversion | raise | 4 | CAPA 증설은 매출과 OP로 전환될 때만 강하다. |
| offline_channel_sellthrough | raise | 5 | 미국 리테일 입점은 매장 회전과 리오더가 필요하다. |
| tariff_absorption | raise | 5 | 관세 이후에도 gross margin이 유지되어야 한다. |
| tourist_spend_per_head | raise | 5 | 관광객 수보다 객단가와 구매전환율이 중요하다. |
| ecommerce_take_rate | raise | 5 | 플랫폼 규모는 take-rate과 margin으로 닫혀야 한다. |
| data_trust_internal_control | raise | 5 | 이커머스는 데이터 신뢰와 내부통제가 Green gate다. |
| fulfillment_unit_economics | raise | 5 | 물류 매출 증가는 건당 마진과 FCF 전환이 필요하다. |
| domestic_consumption_sensitivity | raise | 4 | 내수 유통은 소비둔화 민감도를 RedTeam에 넣는다. |
| viral_brand_headline_only | lower | -5 | 바이럴 브랜드 headline만으로 Stage 3-Green을 만들지 않는다. |
| visitor_count_only | lower | -5 | 방문객 수만 있고 지출/마진이 없으면 event premium이다. |
| online_ecommerce_growth_without_offline_sellthrough | lower | -5 | 온라인 성장만으로 오프라인 sell-through를 대체하지 않는다. |
| JV_scale_without_take_rate | lower | -5 | JV 규모와 고객 DB는 take-rate 전에는 Stage 2다. |
| revenue_uplift_without_unit_economics | lower | -5 | 물류 매출 uplift는 unit economics 전에는 Green 금지다. |
| IPO_or_stock_pop_without_repeat_purchase | lower | -5 | IPO/주가 급등은 반복구매 전에는 4B-watch다. |
| consumer_export_story_without_local_regulatory_fit | lower | -4 | 수출 브랜드는 현지 규제 적합성 게이트가 필요하다. |
| domestic_retail_ignored | lower | -4 | 내수 소비 충격을 무시하면 유통 Green이 왜곡된다. |
| data_breach_or_customer_trust_failure | lower | -5 | 데이터 유출과 고객 신뢰 훼손은 hard 4C 참고점이다. |

## Easy Examples
- `Buldak export` can be Stage 3-like only when ASP, shipments, capacity and OP revision all close; a local recall stays as a 4C-watch.
- `K-beauty U.S. growth` is Stage 2 until physical-store sell-through and tariff absorption are visible.
- `tourist visa-free policy` can move stocks, but without spend per head and margin it remains event premium.
- `Gmarket/AliExpress JV` is Stage 2 until take-rate, compliance and fulfillment margin are proven.
