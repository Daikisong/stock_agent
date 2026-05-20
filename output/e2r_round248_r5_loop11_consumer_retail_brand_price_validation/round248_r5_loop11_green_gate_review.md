# Round 248 R5 Green Gate Review

Do not apply these weights to production scoring yet.

R5 Stage 3-Green is not `K-food`, `K-beauty`, `tourism policy`, or `e-commerce JV`. It requires repeat demand, overseas sell-through, ASP/OPM, inventory/receivables quality, and platform trust.

## Required Fields

- repeat_demand_confirmed
- overseas_sales_mix_increasing
- channel_sellthrough_confirmed
- physical_store_sellthrough_confirmed
- asp_or_product_mix_improvement
- opm_or_fcf_improvement
- inventory_and_receivables_stable
- tariff_packaging_input_shock_passed
- customer_data_or_platform_trust_passed
- price_path_after_evidence

## Forbidden Patterns

- viral_tiktok_only
- retail_talks_only
- ipo_or_debut_rally_only
- tourism_policy_only
- ecommerce_jv_headline_only
- china_decline_without_offset
- single_product_story_only
- data_breach_or_trust_break

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| repeat_demand | raise | 5 | R5는 viral보다 반복구매가 중요하다. |
| export_growth | raise | 5 | K-food/K-beauty export가 OP/EPS로 내려오면 Stage 2 품질이 올라간다. |
| overseas_sales_mix | raise | 5 | 해외 매출 비중 증가는 내수 프레임 해소의 핵심이다. |
| ASP_uplift | raise | 4 | ASP와 product mix 개선은 매출 성장의 질을 높인다. |
| channel_sellthrough | raise | 5 | 입점이 아니라 실제 sell-through가 Green gate다. |
| physical_store_sellthrough | raise | 5 | 오프라인 진열 후 재구매가 확인되어야 e-commerce viral과 분리된다. |
| OPM_improvement | raise | 5 | 수출과 채널 확장은 OPM/FCF로 닫혀야 한다. |
| inventory_quality | raise | 4 | 재고 안정은 shipment와 sell-through를 구분한다. |
| receivables_quality | raise | 4 | 매출채권 품질은 유통/ODM의 현금전환 검증축이다. |
| platform_trust | raise | 5 | 이커머스는 신뢰가 깨지면 사용자와 소비액이 실제로 빠진다. |
| customer_data_compliance | raise | 5 | JV/data scale은 data compliance를 통과해야 한다. |
| viral_product_only | lower | -5 | TikTok viral만으로는 반복구매를 증명하지 못한다. |
| brand_heat_only | lower | -5 | 브랜드 열기만으로 OPM/FCF 체급 변화를 만들 수 없다. |
| retail_talks_without_sell_through | lower | -5 | 입점 논의는 sell-through 전 Stage 2 watch다. |
| IPO_or_debut_rally | lower | -5 | 상장/데뷔 후 급등은 4B-watch 입력이다. |
| China_exposure_without_offset | lower | -5 | 중국 premium/travel retail 약세가 상쇄되지 않으면 Green 금지다. |
| tourism_policy_only | lower | -5 | 관광정책은 spend/OPM 전 event premium이다. |
| ecommerce_JV_without_GMV_margin | lower | -4 | JV scale은 GMV/take-rate/margin 전 Green이 아니다. |
| customer_data_risk | lower | -5 | data breach와 privacy gate는 hard 4C/RedTeam 입력이다. |
| packaging_input_shortage | lower | -4 | 포장재/input shortage는 K-food/K-beauty 생산과 margin을 깬다. |
| tariff_margin_uncertainty | lower | -4 | tariff 비용 전가가 안 되면 수출 growth의 질이 낮아진다. |

## Easy Examples
- `retail talks` are Stage 2 until physical-store sell-through and reorder appear.
- `tourism visa-free policy` is event premium until tourist spend and OPM appear.
- `data breach` is platform-trust 4C; competitor opportunity still needs GMV and margin.
