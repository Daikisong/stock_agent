순서상 이번은 **R5 Loop 13 — 소비재·유통·브랜드 가격경로 검증 라운드**다.

```text
round = R5 Loop 13
round_id = round_202
large_sector = CONSUMER_RETAIL_BRAND
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true_for_retail_credit_reference
direct_listed_hard_4c_confirmed = false
next_round = R6 Loop 13
```

이번 R5 Loop 13은 Samyang/Nongshim 같은 기존 K-food 대표 성공사례만 반복하지 않고, **K-beauty device, indie K-beauty, H&B platform, 중국 관광·면세·백화점, cross-border e-commerce JV, grocery restructuring, celebrity food-service overheat**까지 같이 봤다.

이번에도 KRX/Naver/Yahoo/Stooq 기준 **수정주가 일봉 전체 구간**은 안정적으로 확보하지 못했다. 그래서 30D/90D/180D full OHLC는 만들지 않고, Reuters / FT / MarketWatch / Business Insider / Tom’s Hardware가 보도한 **event price, event return, IPO/상장 후 수익률, 매출·영업이익 anchor, 정책·거래금액**만 계산했다. full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R5 = 소비재·유통·브랜드
```

R5에서 진짜 Stage 3는 “K-beauty”, “K-food”, “중국 관광객”, “면세점”, “브랜드 글로벌화”, “인플루언서”, “IPO”, “유명인이 먹었다”가 아니다.

진짜 Stage 3는 **반복구매, sell-through, 물리채널 재주문, same-store sales, gross margin, tariff pass-through, inventory discipline, customer data trust, franchise margin, cash conversion**이 같이 닫히는 순간이다.

---

# 2. 대상 canonical archetype

```text
K_BEAUTY_DEVICE_GLOBAL_BRAND_4B
INDIE_K_BEAUTY_US_RETAIL_CHANNEL
H_AND_B_PLATFORM_GLOBALIZATION
K_FOOD_EXPORT_ASP_CAPACITY
CHINA_TOURISM_DUTYFREE_RETAIL_EVENT
CROSS_BORDER_ECOMMERCE_DATA_GATE
GROCERY_RETAIL_CREDIT_4C_REFERENCE
CELEBRITY_FOOD_SERVICE_EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
K-beauty device:
- APR / Medicube
- beauty device + celebrity TikTok + U.S. sales
- overseas revenue share, U.S. device concentration, tariff risk

Indie K-beauty:
- d'Alba Global / Tirtir / Beauty of Joseon / Torriden / Anua / Medicube
- Sephora / Ulta / Costco / Target / Amazon channel expansion
- online virality vs physical-store sell-through

H&B platform:
- CJ Olive Young
- U.S. store launch / Sephora-competition
- curation platform vs single-brand risk
- unlisted subsidiary / parent CJ read-through gap

K-food:
- Samyang Buldak
- ASP, U.S./Europe shipment, production capacity
- Denmark recall / capsaicin, packaging cost shock, single-SKU risk

Tourism retail:
- Hyundai Department Store / Hotel Shilla / Shinsegae / Hankook Cosmetics
- Chinese group visa-free entry
- China-Japan travel redirect
- duty-free / department store / cosmetics basket

Cross-border e-commerce:
- Shinsegae Gmarket / AliExpress Korea JV
- 50M customer database
- data-sharing restriction / Alibaba cross-border share

Retail credit:
- Homeplus / MBK
- court-led restructuring
- liquidation value > going-concern value
- equity write-off / sale process

Food-service event:
- Kyochon / Cherrybro / Neuromeka
- Jensen Huang fried-chicken viral event
- no same-store sales evidence
```

---

# 4. 국장 신규 후보 case

## Case A — APR / Medicube `structural_success_candidate + 4B-watch`

```text
symbol = 278470
case_type = structural_success_candidate + 4B-watch
archetype = K_BEAUTY_DEVICE_GLOBAL_BRAND_4B
```

### stage date

```text
Stage 1:
2025-01~2025-10
- K-beauty device demand
- Medicube skincare device promoted by global celebrities
- U.S. social-commerce and TikTok-driven demand

Stage 2:
2025-10-20
- stock price more than four-fold since January
- market value about $6B
- $180 facial skincare device
- device forms about one-third of U.S. sales
- overseas revenue nearly 80% of Q2 revenue
- U.S. contributes almost 30% of revenue
- revenue increased sevenfold since 2018

Stage 3:
보류
- revenue conversion is strong
- but R5 Green requires repeat purchase, device replacement cycle, gross margin, channel durability, tariff pass-through

Stage 4B:
2025-10-20
- more than four-fold stock rise before long-term repeat purchase proof
```

APR은 R5에서 강한 structural success 후보지만, 동시에 4B-watch다. FT는 APR 주가가 2025년 1월 이후 4배 이상 올랐고, 시가총액이 약 $6B까지 커졌으며, $180 facial skincare device가 U.S. sales의 약 3분의 1을 차지한다고 보도했다. Q2 해외 매출 비중은 거의 80%, U.S. 비중은 거의 30%였고, 매출은 2018년 이후 7배 늘었다. 다만 이 정도로 가격이 먼저 간 경우에는 “좋다”보다 “반복구매가 진짜냐”를 먼저 봐야 한다. ([Financial Times][1])

### 실제 가격경로 검증

```json
{
  "price_data_source": "FT APR / Medicube reported return and business anchors",
  "entry_date": "N/A",
  "stage3_price": null,
  "reported_stock_return_since_jan_2025_pct": 300,
  "market_value_usd_bn": 6,
  "device_price_usd": 180,
  "device_share_of_us_sales": "about_one_third",
  "q2_overseas_revenue_share_pct": 80,
  "us_revenue_share_pct": 30,
  "revenue_growth_since_2018_multiple": 7,
  "us_tariff_on_korean_cosmetics_pct": 15,
  "price_increase_plan": "not_planning_to_raise_prices_at_source_date",
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = aligned_partial_but_4B_watch
rerating_result = K_beauty_device_structural_candidate
stage_failure_type = fourfold_rerating_requires_repeat_purchase_margin_check
```

---

## Case B — d’Alba / indie K-beauty basket `success_candidate + overheat`

```text
symbols = 483650 / 257720 / 090430 / 192820 / K-beauty basket
case_type = success_candidate + overheat
archetype = INDIE_K_BEAUTY_US_RETAIL_CHANNEL
```

### stage date

```text
Stage 1:
2024~2025
- South Korea becomes major U.S. cosmetics exporter
- K-beauty expands from Amazon/e-commerce to Ulta, Sephora, Costco, Target

Stage 2:
2025-06-05
- d'Alba Global shares more than doubled since debut last month
- d'Alba in talks with Costco, Ulta Beauty and Target
- Tirtir aims to double U.S. sales
- Beauty of Joseon and Torriden launch via Sephora
- South Korea overtook Germany as world's third-largest beauty product exporter in 2024
- $13B cosmetics output, four fifths exports
- top five Korean cosmetics brands in U.S. e-commerce grew 71% on average over two years vs total U.S. market 21%

Stage 4B:
2025-06
- d'Alba >2x since debut before physical-store sell-through proof

Stage 3:
없음
- U.S. retail shelf access is Stage 2
- actual reorder rate, sell-through, gross margin after tariffs, inventory discipline required
```

d’Alba와 indie K-beauty basket은 R5에서 매우 좋은 Stage 2다. Reuters는 d’Alba Global 주가가 상장 후 한 달 만에 2배 이상 올랐고, d’Alba가 Costco·Ulta·Target과 retail distribution을 논의 중이라고 보도했다. 또 top five Korean cosmetics brands의 U.S. e-commerce sales는 2년 평균 +71%로 전체 U.S. market +21%를 크게 앞섰다. 하지만 physical store에 들어가는 것과 실제 reorder/sell-through가 나오는 것은 다르다. 그래서 Green은 아직 아니다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters K-beauty U.S. expansion / d'Alba anchor",
  "stage3_price": null,
  "d_alba_post_debut_return_min_pct": 100,
  "korea_cosmetics_output_2024_usd_bn": 13,
  "export_share_of_output_pct": 80,
  "implied_export_output_usd_bn": 10.4,
  "top5_korean_us_ecommerce_growth_2y_pct": 71,
  "overall_us_market_growth_2y_pct": 21,
  "korean_vs_overall_growth_spread_pp": 50,
  "top5_french_us_ecommerce_growth_2y_pct": 15,
  "korean_vs_french_growth_spread_pp": 56,
  "tariff_baseline_pct": 10,
  "planned_tariff_pct": 25,
  "actual_physical_store_sellthrough_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_overheat
rerating_result = indie_K_beauty_US_channel_stage2
stage_failure_type = IPO_debut_rally_and_channel_talks_not_sellthrough_green
```

---

## Case C — CJ Olive Young / CJ Corp read-through `success_candidate, unlisted platform gap`

```text
symbols = CJ Corp read-through / CJ Olive Young unlisted
case_type = success_candidate + insufficient_price_data
archetype = H_AND_B_PLATFORM_GLOBALIZATION
```

### stage date

```text
Stage 1:
2025-06~2025-10
- Olive Young global online platform and U.S. expansion
- K-beauty curation platform
- Sephora / Ulta competition ahead of U.S. store launch

Stage 2:
2025-06-05 / 2025-10-15
- Olive Young plans first U.S. store in Los Angeles / U.S. debut expected in 2026
- U.S. K-beauty market reaches $2B in year to July 2025
- +37% YoY
- Olive Young has more than 1,300 stores in Korea
- U.S. retailers are locking up exclusive K-beauty brands before Olive Young arrival

Stage 3:
없음
- unlisted Olive Young platform is not CJ Corp Green
- U.S. store sales, online GMV, take-rate, margin, parent value bridge required

Stage 4B:
CJ read-through or K-beauty platform premium moves before U.S. unit economics
```

CJ Olive Young은 R5에서 매우 좋은 H&B platform 후보지만, 상장주 기준으로는 조심해야 한다. Reuters는 Olive Young이 U.S. 진출을 추진한다고 보도했고, Business Insider는 U.S. K-beauty market이 2025년 7월 기준 1년간 $2B, 전년 대비 +37%였으며, Olive Young이 한국에 1,300개 이상의 매장을 가진 retailer라고 설명했다. 하지만 Olive Young은 직접 상장사가 아니므로 CJ Corp에 Stage 3를 주려면 parent value bridge가 필요하다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters K-beauty / Business Insider U.S. K-beauty and Olive Young anchors",
  "stage3_price": null,
  "direct_listed_ticker": "N/A",
  "parent_readthrough": "CJ Corp",
  "olive_young_korea_store_count": 1300,
  "us_kbeauty_market_size_2025_usd_bn": 2.0,
  "us_kbeauty_market_growth_pct": 37,
  "us_store_launch_timing": "2026 expected in BI; Reuters reported LA plan as early as 2025",
  "parent_value_bridge_confirmed": false,
  "store_unit_economics_confirmed": false,
  "mfe_mae": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_insufficient_price_data
rerating_result = H_and_B_platform_globalization_watch
stage_failure_type = unlisted_subsidiary_not_parent_green
```

---

## Case D — Samyang Foods / Buldak `structural_success_candidate + safety/input-cost watch`

```text
symbol = 003230
case_type = structural_success_candidate + 4C-watch
archetype = K_FOOD_EXPORT_ASP_CAPACITY
```

### stage date

```text
Stage 1:
2024-06-14
- Buldak exports
- ASP rise
- U.S. / Europe shipment growth
- production capacity expansion

Stage 2:
2024-06-14
- Kiwoom raises Q2 OP estimate to 81.2B won
- +84% YoY OP estimate
- target price 660,000 → 830,000 won
- shares close +5.7% at 647,000 won

Stage 3:
2024-06-14 candidate
- export + ASP + capacity + OP revision align

Stage 4C-watch:
2024-06-12
- Denmark recalls three spicy Buldak products over high capsaicin / acute poisoning concern

Stage 4C-watch 추가:
2026-03-26
- Reuters reports Samyang Foods warns prolonged Middle East conflict could cause packaging material shortages and higher costs
```

Samyang은 R5 K-food의 좋은 structural success 후보로 유지한다. MarketWatch는 Kiwoom이 Buldak exports, ASP 상승, U.S./Europe shipment 증가, production capacity 확대를 근거로 Q2 OP estimate를 812억 원, +84% YoY로 올렸고, 주가는 647,000원에 마감했다고 보도했다. 다만 Denmark recall과 packaging material shortage risk는 `food safety / input cost` 4C-watch로 붙인다. ([마켓워치][3])

### 실제 가격경로 검증

```json
{
  "price_data_source": "MarketWatch earnings anchor + AP recall + Reuters packaging-cost risk",
  "entry_date": "2024-06-14",
  "stage3_price_krw": 647000,
  "event_mfe_1d_pct": 5.7,
  "implied_prior_close_krw": 611921,
  "target_price_krw": 830000,
  "target_upside_from_stage3_pct": 28.3,
  "q2_op_estimate_krw_bn": 81.2,
  "op_growth_estimate_pct": 84,
  "denmark_recalled_products": 3,
  "recall_reason": "high capsaicin / acute poisoning concern",
  "input_cost_watch": "PET / packaging material shortage risk under Middle East energy shock",
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = aligned_partial
rerating_result = K_food_export_ASP_capacity_stage3_candidate
stage_failure_type = single_brand_safety_input_cost_4C_watch
```

---

## Case E — Hyundai Dept / Hotel Shilla / Shinsegae / Hankook Cosmetics `event_premium`

```text
symbols = 069960 / 008770 / 004170 / 123690 / 034230
case_type = event_premium + 4B-watch
archetype = CHINA_TOURISM_DUTYFREE_RETAIL_EVENT
```

### stage date

```text
Stage 1:
2025-03-20 / 2025-08-06
- South Korea announces Chinese group tourist visa-free programme
- consumer retail / duty-free / hotel / casino / cosmetics demand expectation

Stage 2:
2025-08-06
- Chinese group tourists allowed visa-free entry from 2025-09-29 to 2026-06
- Hyundai Department Store +7.1%
- Hotel Shilla +4.8%
- Paradise +2.9%
- Hankook Cosmetics +9.9%

Stage 4B:
2025-11-21
- China-Japan diplomatic dispute redirects cruise/tourism interest to Korea
- Lotte Tour >+20%
- Yellow Balloon +24%
- Shinsegae +6%
- Adora Magic City Jeju stay extends 31~57h vs usual 9h

Stage 3:
없음
- tourist policy and redirect are not Green
- duty-free spend, hotel occupancy, SSS, cosmetics sell-through, margin required
```

중국 단체관광 비자면제와 China-Japan 갈등은 R5 retail/duty-free에 좋은 Stage 2지만, event premium이다. Reuters는 2025년 8월 6일 현대백화점 +7.1%, 호텔신라 +4.8%, Paradise +2.9%, 한국화장품 +9.9%가 올랐다고 보도했다. 11월에는 cruise rerouting 기대에 Lotte Tour >20%, Yellow Balloon +24%, Shinsegae +6%도 나왔다. 그러나 소비재 Stage 3는 관광객 headline이 아니라 실제 객단가와 same-store sales다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters China visa-free / cruise rerouting event anchors",
  "stage3_price": null,
  "visa_free_start": "2025-09-29",
  "programme_end": "2026-06",
  "group_condition": "3_or_more_mainland_Chinese_tourists",
  "visa_free_stay_days": 15,
  "hyundai_department_store_mfe_pct": 7.1,
  "hotel_shilla_mfe_pct": 4.8,
  "paradise_mfe_pct": 2.9,
  "hankook_cosmetics_mfe_pct": 9.9,
  "lotte_tour_redirect_mfe_pct": 20,
  "yellow_balloon_redirect_mfe_pct": 24,
  "shinsegae_redirect_mfe_pct": 6,
  "adora_usual_jeju_stay_hours": 9,
  "adora_new_jeju_stay_hours": "31-57",
  "jeju_stay_extension_low_pct": 244.4,
  "jeju_stay_extension_high_pct": 533.3,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_4B_watch
rerating_result = China_tourism_retail_dutyfree_watch
stage_failure_type = tourist_flow_headline_not_spend_margin_green
```

---

## Case F — Shinsegae / AliExpress-Gmarket JV `success_candidate + data gate`

```text
symbols = 004170 / 139480 read-through
case_type = success_candidate + 4C-watch
archetype = CROSS_BORDER_ECOMMERCE_DATA_GATE
```

### stage date

```text
Stage 1:
2025-09-18
- AliExpress Korea / Shinsegae unit JV
- Gmarket and AliExpress Korea combined cross-border e-commerce platform
- Chinese direct-import growth

Stage 2:
2025-09-18
- KFTC conditionally approves JV
- combined overseas online-shopping market share 41%
- Korean online purchases of Chinese imports +32% to 4.7T won in 2024
- Alibaba accounts for 62% by value
- Gmarket customer database about 50M customers

Stage 4C-watch:
2025-09-18
- KFTC cites significant worry over customer information sharing
- companies barred from sharing Korean overseas-shopping customer data for three years
- independent operations required

Stage 3:
없음
- JV approval is Stage 2
- take-rate, GMV, logistics margin, data-compliance, customer retention needed
```

Shinsegae / AliExpress-Gmarket JV는 R5 digital retail success_candidate지만, data gate가 붙는다. Reuters에 따르면 JV의 overseas online shopping market share는 41%까지 올라가고, 2024년 한국인의 중국 직구 지출은 4.7조 원으로 +32% 증가했으며 Alibaba가 value 기준 62%를 차지했다. 그러나 KFTC는 Gmarket의 5,000만 고객 데이터와 Alibaba data analytics 결합을 우려해 3년간 data sharing을 제한했다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters KFTC conditional approval anchor",
  "stage3_price": null,
  "combined_market_share_overseas_online_shopping_pct": 41,
  "gmarket_customer_database_mn": 50,
  "korean_china_import_online_spending_2024_krw_trn": 4.7,
  "spending_growth_2024_pct": 32,
  "alibaba_share_by_value_pct": 62,
  "data_sharing_ban_years": 3,
  "independent_operation_required": true,
  "take_rate_confirmed": false,
  "gmv_profitability_confirmed": false,
  "mfe_mae": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_data_4C_watch
rerating_result = cross_border_ecommerce_platform_stage2
stage_failure_type = JV_approval_not_GMV_margin_data_green
```

---

## Case G — Homeplus / MBK `retail credit hard reference`

```text
direct_company = Homeplus unlisted
readthrough = grocery / offline retail / PE-owned consumer retail
case_type = 4C-reference
archetype = GROCERY_RETAIL_CREDIT_4C_REFERENCE
```

### stage date

```text
Stage 1:
2025-03
- Homeplus enters court-led restructuring
- grocery retail under pressure from e-commerce and post-COVID demand shift
- No.2 grocery retailer in Korea

Stage 4C-reference:
2025-06-13
- MBK plans sale of Homeplus to avoid liquidation
- liquidation value higher than going-concern value
- MBK to cancel 2.5T won worth of shares
- Homeplus liquidation value 3.7T won
- total assets 6.8T won

Stage 4C-reference validation:
2025-06-20
- court approves sale plan
- Samil PwC appointed to manage sale
- sale intended to repay creditors and preserve jobs
- MBK's earlier $6.1B deal marked as setback

Stage 3:
N/A
```

Homeplus는 상장사가 아니지만, R5 retail hard reference다. Reuters는 Homeplus의 liquidation value가 going-concern value보다 높았고, MBK가 2.5조 원어치 보통주를 write-off할 계획이라고 보도했다. Homeplus liquidation value는 3.7조 원, total assets는 6.8조 원으로 제시됐다. 이 case는 오프라인 grocery retail에서 “점포망이 크다”가 Stage 3가 아니라는 기준이다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Homeplus restructuring / court-sale anchors",
  "stage3_price": null,
  "direct_listed_ticker": "N/A",
  "company_status": "court-led restructuring",
  "liquidation_value_krw_trn": 3.7,
  "total_assets_krw_trn": 6.8,
  "mbk_share_writeoff_krw_trn": 2.5,
  "mbk_share_writeoff_usd_bn": 1.83,
  "prior_deal_context_usd_bn": 6.1,
  "sale_manager": "Samil PwC",
  "sale_timeline_months": "2-3",
  "hard_4c_reference": true,
  "mfe_mae": "N/A_unlisted"
}
```

### alignment

```text
score_price_alignment = thesis_break_reference
rerating_result = grocery_retail_credit_failure_reference
stage_failure_type = unlisted_retail_credit_hard_reference
```

---

## Case H — Kyochon / Cherrybro / Neuromeka `price_moved_without_evidence`

```text
symbols = 339770 / 066360 / 348340
case_type = overheat + price_moved_without_evidence
archetype = CELEBRITY_FOOD_SERVICE_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-10-31
- Nvidia CEO Jensen Huang visits Korean fried chicken restaurant with Samsung and Hyundai executives
- viral social-media event
- AI-chip deal atmosphere spills into unrelated food-service stocks

Stage 4B:
2025-10-31
- Kyochon F&B up to +20%
- Cherrybro up to daily limit +30%
- Neuromeka surged
- Kkanbu Chicken, actual restaurant visited, not listed
- MarketWatch: only Neuromeka retained gains by close

Stage 3:
없음
- no same-store sales evidence
- no franchise margin evidence
- no repeat demand evidence
```

Kyochon / Cherrybro / Neuromeka는 R5에서 가장 깨끗한 `price_moved_without_evidence`다. Jensen Huang이 Samsung·Hyundai 경영진과 비상장 Kkanbu Chicken에서 식사하자 관련 food-service/poultry/robot stocks가 급등했다. Tom’s Hardware는 Kyochon이 최대 +20%, Cherrybro가 daily limit +30%까지 올랐다고 보도했고, MarketWatch는 실제 식당이 비상장인데도 Kyochon·Cherrybro·Neuromeka가 모두 급등했으며, 종가까지 상승분을 유지한 것은 Neuromeka뿐이라고 전했다. ([Tom's Hardware][7])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Tom's Hardware / MarketWatch event-return anchors",
  "stage3_price": null,
  "kyochon_event_mfe_pct": 20,
  "cherrybro_event_mfe_pct": 30,
  "neuromeka_event": "surged; only one of the three retained gains by close according to MarketWatch",
  "actual_restaurant": "Kkanbu Chicken",
  "actual_restaurant_listed": false,
  "same_store_sales_confirmed": false,
  "franchise_margin_confirmed": false,
  "repeat_demand_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = celebrity_food_service_event_premium
stage_failure_type = should_be_4B_not_stage3
```

---

# 5. 이번 R5 case별 stage date 요약

| case                    | Stage 1    | Stage 2    | Stage 3              | Stage 4B                  | Stage 4C                            |
| ----------------------- | ---------- | ---------- | -------------------- | ------------------------- | ----------------------------------- |
| APR / Medicube          | 2025-01~10 | 2025-10-20 | 보류                   | 2025-10-20                | tariff/channel watch                |
| d’Alba / indie K-beauty | 2024~2025  | 2025-06-05 | N/A                  | 2025-06                   | tariff/channel watch                |
| CJ Olive Young          | 2025~2026  | 2025~2026  | N/A                  | parent read-through watch | N/A                                 |
| Samyang Foods           | 2024-06-14 | 2024-06-14 | 2024-06-14 candidate | single-brand watch        | recall/input-cost watch             |
| tourism retail basket   | 2025-03/08 | 2025-08-06 | N/A                  | 2025-11-21                | geopolitical/tourism reversal watch |
| Shinsegae-AliExpress JV | 2025-09-18 | 2025-09-18 | N/A                  | JV premium watch          | data gate watch                     |
| Homeplus                | 2025-03    | N/A        | N/A                  | N/A                       | 2025-06 hard reference              |
| Kyochon/Cherrybro       | 2025-10-31 | N/A        | N/A                  | 2025-10-31                | meme fade                           |

---

# 6. 실제 가격경로 검증 총괄

| case                    |                                                                     anchor | MFE / MAE 해석                         | 판정                           |
| ----------------------- | -------------------------------------------------------------------------: | ------------------------------------ | ---------------------------- |
| APR                     |                                                stock >4x, market value $6B | structural success but already 4B    | success_candidate_4B         |
| d’Alba / indie K-beauty |                                                     d’Alba >2x since debut | channel Stage 2, overheat            | success_candidate_overheat   |
| Olive Young             |                              U.S. K-beauty market $2B, +37%; 1,300+ stores | unlisted platform gap                | insufficient                 |
| Samyang                 |                                             647,000원, +5.7%, target +28.3% | export/ASP/capacity aligned          | aligned_partial              |
| tourism retail          | Hyundai Dept +7.1%, Hotel Shilla +4.8%, Hankook +9.9%; Shinsegae +6% later | tourist-flow event premium           | event_premium                |
| Shinsegae-Ali JV        |                     41% market share, 50M customer DB, data sharing ban 3y | platform Stage 2 + data gate         | 4C-watch                     |
| Homeplus                |                                 liquidation value 3.7T, MBK write-off 2.5T | offline retail credit hard reference | thesis_break_reference       |
| Kyochon/Cherrybro       |                                                                +20% / +30% | celebrity event, no sales evidence   | price_moved_without_evidence |

---

# 7. score-price alignment 판정

```text
aligned:
- Samyang Foods, partial; export / ASP / capacity / OP revision aligned

structural_success_candidate:
- APR / Medicube
- Samyang Foods

success_candidate:
- d’Alba / indie K-beauty
- CJ Olive Young / CJ Corp read-through
- Shinsegae-AliExpress Gmarket JV

event_premium:
- China tourism / duty-free / department store basket
- Kyochon / Cherrybro / Neuromeka Jensen event

overheat:
- APR >4x
- d’Alba >2x since debut
- Kyochon / Cherrybro meme move

price_moved_without_evidence:
- Kyochon / Cherrybro / Neuromeka
- tourism retail basket before spend / SSS / margin confirmation
- CJ Olive Young parent read-through before U.S. unit economics
- d’Alba if physical-store sell-through is not proven

thesis_break_watch:
- Samyang recall / packaging input-cost risk
- Shinsegae-AliExpress data gate
- Homeplus retail credit reference
- China tourism reversal risk

hard_4C_confirmed:
- direct listed hard 4C: false
- sector hard reference: Homeplus retail credit restructuring
```

---

# 8. 점수비중 교정

## 올릴 축

```text
repeat_purchase +5
physical_store_sellthrough +5
same_store_sales +5
gross_margin_after_tariff +5
inventory_discipline +5
channel_reorder_rate +5
parent_value_bridge +4
data_governance +5
franchise_margin +4
cash_conversion +5
```

### 왜 올리나

APR과 d’Alba는 가격과 channel narrative가 강하지만, 반복구매와 physical-store sell-through가 없으면 4B다. Olive Young은 platform value가 좋지만 parent CJ로의 value bridge가 필요하다. Tourism retail은 관광객이 오는 것과 duty-free spend / department-store SSS가 다르다. Shinsegae-Ali JV는 data governance가 핵심 gate다.

## 내릴 축

```text
viral_social_media_only -5
celebrity_event_only -5
tourist_arrival_headline_only -5
IPO_or_debut_pop_only -5
channel_talks_without_sellthrough -5
unlisted_subsidiary_readthrough_only -4
gross_margin_before_tariff_pass -4
data_sharing_regulatory_risk -5
offline_retail_credit_stress -5
```

### 왜 내리나

Kyochon/Jensen event는 sales evidence 없이 주가만 뛰었다. d’Alba >2x는 physical-store sell-through 전이면 4B다. China visa-free retail rally는 spending conversion 전 event premium이다. Homeplus는 점포망이 있어도 credit stress가 오면 retail thesis가 깨진다.

## Green gate 강화 조건

```text
R5 Stage 3-Green 필수:
1. repeat purchase 확인
2. physical-store sell-through / reorder 확인
3. same-store sales 확인
4. gross margin after tariffs 확인
5. inventory / channel stuffing risk 없음
6. parent-subsidiary value bridge 확인
7. platform은 data-governance 통과
8. food-service는 franchise margin / repeat demand 확인
9. tourism retail은 duty-free spend / hotel occupancy / department-store SSS 확인
10. price path가 evidence 이후 따라옴

금지:
viral TikTok only
celebrity event only
tourist-arrival headline only
IPO/debut pop only
channel talks only
unlisted subsidiary read-through only
```

## 4B 조기감지 조건

```text
4B-watch:
beauty stock >2x~4x before repeat purchase / margin proof
IPO/debut pop >100%
tourism/duty-free basket +5~10% on policy headline
celebrity food-service event +20~30%
U.S. retail-channel talks before sell-through
parent company rally on unlisted Olive Young value
cross-border JV premium before data-compliance proof

4B-elevated:
tariff pass-through untested
China exports falling / China demand weak
channel inventory risk
single-device / single-SKU concentration
data-sharing restrictions
offline retail credit stress
```

## 4C hard gate 조건

```text
food-safety recall
input-cost shock without pass-through
retail credit restructuring
data-governance violation
tourism policy reversal
China/Korea diplomatic shock
inventory build / channel stuffing
franchise margin collapse
celebrity event fade
```

이번 R5 Loop 13에서는 direct listed hard 4C를 확정하지 않는다. 다만 **Homeplus retail-credit restructuring**은 sector hard reference이고, **Shinsegae-AliExpress data gate**, **Samyang recall/input-cost risk**, **tourism retail event premium**, **Kyochon/Cherrybro meme move**는 모두 shadow gate로 둔다.

---

# 9. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 10. 레포 반영용 patch-ready 출력

## docs/round/round_202.md 요약

```md
# R5 Loop 13. Consumer / Retail / Brand Price Validation

이번 라운드는 R5 Loop 13 price-validation 라운드다.

핵심 결론:
- APR / Medicube is structural_success_candidate plus 4B-watch. Stock rose more than four-fold since January 2025, market value about $6B, device price $180, device about one-third of U.S. sales, overseas revenue nearly 80% of Q2 revenue, U.S. nearly 30%.
- d'Alba / indie K-beauty is success_candidate plus overheat. d'Alba shares more than doubled since debut; U.S. physical retail talks with Costco, Ulta, Target; top five Korean U.S. ecommerce beauty brands grew 71% over two years vs overall market 21%. Sell-through required.
- CJ Olive Young is H&B platform globalization candidate, but unlisted subsidiary gap remains. U.S. K-beauty market reached $2B by July 2025, +37%; Olive Young has 1,300+ Korean stores and U.S. debut expected in 2026. Parent CJ value bridge required.
- Samyang Foods is aligned_partial K-food Stage 3 candidate. Stage3 anchor 647,000 won, +5.7%, target 830,000 won, Q2 OP estimate 81.2B won, +84% YoY. Denmark recall and packaging cost risk are 4C-watch.
- China tourism retail basket is event premium. Hyundai Department +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9% on visa-free news; later Shinsegae +6% on cruise rerouting. Spending/margin required.
- Shinsegae-AliExpress Gmarket JV is success_candidate plus data 4C-watch. Combined overseas online-shopping share 41%, Gmarket database 50M customers, Chinese direct-import spending 4.7T won +32%, Alibaba share 62%. Data sharing banned for 3 years.
- Homeplus is retail credit hard reference. Court-led restructuring, liquidation value 3.7T won, total assets 6.8T won, MBK to write off 2.5T won shares.
- Kyochon / Cherrybro / Neuromeka Jensen event is price_moved_without_evidence. Kyochon up to +20%, Cherrybro +30%, actual restaurant Kkanbu Chicken not listed, no same-store-sales proof.
```

## docs/checkpoints/checkpoint_28a_round202_r5_loop13.md 요약

```md
# Checkpoint 28A Round 202 R5 Loop 13 Consumer Retail Brand Price Validation

## 반영 내용
- R5 Loop 13 price-validation 라운드를 추가했다.
- K-beauty device, indie K-beauty channel, Olive Young platform, Samyang K-food export, China tourism retail, Shinsegae-AliExpress JV, Homeplus retail credit, Jensen fried-chicken event를 비교했다.
- Reuters / FT / MarketWatch / Business Insider / Tom’s Hardware anchors로 가능한 event MFE/MAE 및 business metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- repeat purchase, physical-store sell-through, same-store sales, gross margin after tariff, inventory discipline, channel reorder rate, data governance, parent value bridge, franchise margin 가중치 강화
- viral social media-only, celebrity event-only, tourist-arrival headline-only, IPO/debut pop-only, channel talks without sell-through, unlisted subsidiary read-through-only, offline retail credit stress 감점 강화
```

## data/e2r_case_library/cases_r5_loop13_round202.jsonl 초안

```jsonl
{"case_id":"r5_loop13_apr_medicube_kbeauty_device_4b","symbol":"278470","company_name":"APR / Medicube","case_type":"structural_success_candidate","primary_archetype":"K_BEAUTY_DEVICE_GLOBAL_BRAND_4B","stage2_date":"2025-10-20","stage4b_date":"2025-10-20","price_validation":{"price_data_source":"FT APR / Medicube reported return and business anchors","stage3_price":null,"reported_stock_return_since_jan_2025_pct":300,"market_value_usd_bn":6,"device_price_usd":180,"device_share_of_us_sales":"about_one_third","q2_overseas_revenue_share_pct":80,"us_revenue_share_pct":30,"revenue_growth_since_2018_multiple":7,"us_tariff_on_korean_cosmetics_pct":15,"price_increase_plan":"not_planning_to_raise_prices_at_source_date","price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"aligned_partial_but_4B_watch","rerating_result":"K_beauty_device_structural_candidate","notes":"Device brand economics look strong, but >4x rerating requires repeat purchase, channel durability and margin proof."}
{"case_id":"r5_loop13_dalba_indie_kbeauty_us_channel","symbol":"483650/257720/090430/192820","company_name":"d'Alba Global / Silicon2 / Amorepacific / Cosmax-Kolmar read-through","case_type":"success_candidate_overheat","primary_archetype":"INDIE_K_BEAUTY_US_RETAIL_CHANNEL","stage2_date":"2025-06-05","stage4b_date":"2025-06","price_validation":{"price_data_source":"Reuters K-beauty U.S. expansion / d'Alba anchor","stage3_price":null,"d_alba_post_debut_return_min_pct":100,"korea_cosmetics_output_2024_usd_bn":13,"export_share_of_output_pct":80,"implied_export_output_usd_bn":10.4,"top5_korean_us_ecommerce_growth_2y_pct":71,"overall_us_market_growth_2y_pct":21,"korean_vs_overall_growth_spread_pp":50,"top5_french_us_ecommerce_growth_2y_pct":15,"korean_vs_french_growth_spread_pp":56,"tariff_baseline_pct":10,"planned_tariff_pct":25,"actual_physical_store_sellthrough_confirmed":false,"price_validation_status":"reported_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_but_overheat","rerating_result":"indie_K_beauty_US_channel_stage2","notes":"U.S. channel talks and ecommerce growth are Stage 2; sell-through, reorder and gross margin after tariffs required."}
{"case_id":"r5_loop13_cj_olive_young_global_hb_platform","symbol":"CJ_Corp_readthrough/unlisted_OliveYoung","company_name":"CJ Olive Young / CJ Corp read-through","case_type":"success_candidate","primary_archetype":"H_AND_B_PLATFORM_GLOBALIZATION","stage2_date":"2025-2026","price_validation":{"price_data_source":"Reuters K-beauty / Business Insider U.S. K-beauty and Olive Young anchors","stage3_price":null,"direct_listed_ticker":"N/A","parent_readthrough":"CJ Corp","olive_young_korea_store_count":1300,"us_kbeauty_market_size_2025_usd_bn":2.0,"us_kbeauty_market_growth_pct":37,"us_store_launch_timing":"2026 expected in BI; Reuters reported LA plan as early as 2025","parent_value_bridge_confirmed":false,"store_unit_economics_confirmed":false,"price_validation_status":"unlisted_subsidiary_price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_insufficient_price_data","rerating_result":"H_and_B_platform_globalization_watch","notes":"Olive Young platform value is Stage 2; parent CJ Green requires store economics, GMV/take-rate and value bridge."}
{"case_id":"r5_loop13_samyang_buldak_export_asp_capacity","symbol":"003230","company_name":"Samyang Foods","case_type":"structural_success_candidate","primary_archetype":"K_FOOD_EXPORT_ASP_CAPACITY","stage3_date":"2024-06-14_candidate","stage4c_date":"2024-06-12/2026-03-26_watch","price_validation":{"price_data_source":"MarketWatch earnings anchor + AP recall + Reuters packaging-cost risk","stage3_price_krw":647000,"event_mfe_1d_pct":5.7,"implied_prior_close_krw":611921,"target_price_krw":830000,"target_upside_from_stage3_pct":28.3,"q2_op_estimate_krw_bn":81.2,"op_growth_estimate_pct":84,"denmark_recalled_products":3,"recall_reason":"high capsaicin / acute poisoning concern","input_cost_watch":"PET / packaging material shortage risk under Middle East energy shock","price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned_partial","rerating_result":"K_food_export_ASP_capacity_stage3_candidate","notes":"Export/ASP/capacity evidence aligned, but single-brand concentration, recall and input-cost risk remain."}
{"case_id":"r5_loop13_china_tourism_dutyfree_retail_event","symbol":"069960/008770/004170/123690/034230","company_name":"Hyundai Department Store / Hotel Shilla / Shinsegae / Hankook Cosmetics / Paradise","case_type":"event_premium","primary_archetype":"CHINA_TOURISM_DUTYFREE_RETAIL_EVENT","stage2_date":"2025-08-06","stage4b_date":"2025-11-21","price_validation":{"price_data_source":"Reuters China visa-free / cruise rerouting event anchors","stage3_price":null,"visa_free_start":"2025-09-29","programme_end":"2026-06","group_condition":"3_or_more_mainland_Chinese_tourists","visa_free_stay_days":15,"hyundai_department_store_mfe_pct":7.1,"hotel_shilla_mfe_pct":4.8,"paradise_mfe_pct":2.9,"hankook_cosmetics_mfe_pct":9.9,"lotte_tour_redirect_mfe_pct":20,"yellow_balloon_redirect_mfe_pct":24,"shinsegae_redirect_mfe_pct":6,"adora_usual_jeju_stay_hours":9,"adora_new_jeju_stay_hours":"31-57","jeju_stay_extension_low_pct":244.4,"jeju_stay_extension_high_pct":533.3,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_4B_watch","rerating_result":"China_tourism_retail_dutyfree_watch","notes":"Tourist-flow policy is Stage 2; duty-free spend, hotel occupancy, SSS and margin required before Green."}
{"case_id":"r5_loop13_shinsegae_aliexpress_gmarket_data_gate","symbol":"004170/139480_readthrough","company_name":"Shinsegae / AliExpress Korea / Gmarket JV","case_type":"success_candidate_4c_watch","primary_archetype":"CROSS_BORDER_ECOMMERCE_DATA_GATE","stage2_date":"2025-09-18","stage4c_date":"2025-09-18_watch","price_validation":{"price_data_source":"Reuters KFTC conditional approval anchor","stage3_price":null,"combined_market_share_overseas_online_shopping_pct":41,"gmarket_customer_database_mn":50,"korean_china_import_online_spending_2024_krw_trn":4.7,"spending_growth_2024_pct":32,"alibaba_share_by_value_pct":62,"data_sharing_ban_years":3,"independent_operation_required":true,"take_rate_confirmed":false,"gmv_profitability_confirmed":false,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_data_4C_watch","rerating_result":"cross_border_ecommerce_platform_stage2","notes":"JV approval is Stage 2; data governance, take-rate, GMV profitability and logistics margin required."}
{"case_id":"r5_loop13_homeplus_retail_credit_hard_reference","symbol":"unlisted_Homeplus/grocery_retail_reference","company_name":"Homeplus / MBK Partners","case_type":"4c_reference","primary_archetype":"GROCERY_RETAIL_CREDIT_4C_REFERENCE","stage4c_date":"2025-06-13/2025-06-20","price_validation":{"price_data_source":"Reuters Homeplus restructuring / court-sale anchors","stage3_price":null,"direct_listed_ticker":"N/A","company_status":"court-led restructuring","liquidation_value_krw_trn":3.7,"total_assets_krw_trn":6.8,"mbk_share_writeoff_krw_trn":2.5,"mbk_share_writeoff_usd_bn":1.83,"prior_deal_context_usd_bn":6.1,"sale_manager":"Samil PwC","sale_timeline_months":"2-3","hard_4c_reference":true,"price_validation_status":"unlisted_retail_credit_reference"},"score_price_alignment":"thesis_break_reference","rerating_result":"grocery_retail_credit_failure_reference","notes":"Offline retail scale cannot override credit stress; used as R5 hard reference, not direct listed row."}
{"case_id":"r5_loop13_kyochon_cherrybro_neuromeka_jensen_event","symbol":"339770/066360/348340","company_name":"Kyochon F&B / Cherrybro / Neuromeka","case_type":"overheat","primary_archetype":"CELEBRITY_FOOD_SERVICE_EVENT_PREMIUM","stage4b_date":"2025-10-31","price_validation":{"price_data_source":"Tom's Hardware / MarketWatch event-return anchors","stage3_price":null,"kyochon_event_mfe_pct":20,"cherrybro_event_mfe_pct":30,"neuromeka_event":"surged; only one of the three retained gains by close according to MarketWatch","actual_restaurant":"Kkanbu Chicken","actual_restaurant_listed":false,"same_store_sales_confirmed":false,"franchise_margin_confirmed":false,"repeat_demand_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"celebrity_food_service_event_premium","notes":"Celebrity viral event is 4B/event premium, not Stage 3 without SSS, franchise margin and repeat demand."}
```

## data/sector_taxonomy/score_weight_profiles_round202_r5_loop13_v1.csv 초안

```csv
archetype,repeat_purchase,physical_store_sellthrough,same_store_sales,gross_margin_after_tariff,inventory_discipline,channel_reorder_rate,parent_value_bridge,data_governance,franchise_margin,cash_conversion,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
K_BEAUTY_DEVICE_GLOBAL_BRAND_4B,+5,+4,+3,+5,+5,+5,+2,+2,+0,+5,-4,+5,+3,APR shows strong device brand economics but >4x rally requires 4B-watch.
INDIE_K_BEAUTY_US_RETAIL_CHANNEL,+5,+5,+3,+5,+5,+5,+2,+2,+0,+5,-5,+5,+3,d'Alba/K-beauty channel talks need sell-through and reorder proof.
H_AND_B_PLATFORM_GLOBALIZATION,+5,+5,+5,+5,+5,+5,+5,+4,+0,+5,-4,+5,+3,Olive Young platform value needs parent bridge and U.S. unit economics.
K_FOOD_EXPORT_ASP_CAPACITY,+5,+5,+4,+5,+5,+5,+1,+1,+2,+5,-2,+4,+4,Samyang export/ASP/capacity aligned; recall/input-cost risks remain.
CHINA_TOURISM_DUTYFREE_RETAIL_EVENT,+4,+5,+5,+4,+5,+4,+2,+2,+0,+5,-5,+5,+4,Tourist-flow event requires spend, SSS, hotel occupancy and margin.
CROSS_BORDER_ECOMMERCE_DATA_GATE,+5,+4,+4,+4,+5,+5,+3,+5,+0,+5,-4,+4,+5,Shinsegae-Ali JV needs data compliance and GMV/take-rate proof.
GROCERY_RETAIL_CREDIT_4C_REFERENCE,+3,+3,+5,+4,+5,+3,+0,+3,+0,+5,0,+3,+5,Homeplus shows offline retail credit stress is hard reference.
CELEBRITY_FOOD_SERVICE_EVENT_PREMIUM,+1,+0,+5,+3,+3,+1,+0,+1,+5,+3,-5,+5,+3,Kyochon/Cherrybro Jensen event is price_moved_without_evidence.
```

---

# 이번 R5 Loop 13 결론

```text
1. APR / Medicube는 R5의 강한 structural_success_candidate다.
   하지만 주가가 이미 4배 이상 뛰었으므로 지금은 4B-watch가 맞다.

2. d’Alba / indie K-beauty basket은 U.S. channel Stage 2다.
   physical-store sell-through와 gross margin after tariff가 확인되어야 Green이다.

3. CJ Olive Young은 H&B platform 후보지만, unlisted subsidiary gap이 크다.
   CJ Corp Green을 주려면 parent value bridge와 U.S. unit economics가 필요하다.

4. Samyang Foods는 aligned_partial Stage 3 후보로 인정할 수 있다.
   export, ASP, capacity, OP revision이 같이 붙었다. 단 recall/input-cost risk는 4C-watch다.

5. China tourism retail basket은 event premium이다.
   관광객 headline이 아니라 duty-free spend, hotel occupancy, SSS, margin이 Stage 3 조건이다.

6. Shinsegae-AliExpress/Gmarket JV는 cross-border e-commerce Stage 2다.
   data governance gate를 통과해야 한다.

7. Homeplus는 R5 retail credit hard reference다.
   오프라인 점포망이 커도 liquidation value가 going-concern value보다 높으면 thesis가 끊긴다.

8. Kyochon / Cherrybro / Neuromeka Jensen event는 price_moved_without_evidence다.
   유명인이 먹은 장면은 매출이 아니다.
```

한 문장으로 압축하면:

> **R5에서 진짜 Stage 3는 “K-beauty·K-food·관광객·유명인·채널입점 이야기가 뜬다”가 아니라, 반복구매·sell-through·SSS·gross margin·data trust·cash conversion이 실제 숫자로 닫히는 순간이다.**

* [Reuters](https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/?utm_source=chatgpt.com)
* [Financial Times](https://www.ft.com/content/6a0f7e2c-f3b9-4eb6-961c-d69af28f7183?utm_source=chatgpt.com)
* [마켓워치](https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/chinese-cruise-ships-look-steer-clear-japan-amid-diplomatic-dispute-2025-11-21/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-conditionally-approves-aliexpress-shinsegae-unit-joint-venture-2025-09-18/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/en/mbk-plans-sell-its-troubled-korean-supermarket-chain-homeplus-2025-06-13/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/struggling-retailer-homeplus-gets-approval-sale-plan-south-korean-court-2025-06-20/?utm_source=chatgpt.com)
* [Tom's Hardware](https://www.tomshardware.com/tech-industry/korean-fried-chicken-stocks-surge-30-percent-as-nvidia-ceo-jensen-huang-dines-out-on-local-delicacy-entire-industry-buoyed-by-secret-ingredient-jensanity?utm_source=chatgpt.com)
* [마켓워치](https://www.marketwatch.com/story/jensen-huang-spreads-nvidia-magic-to-fried-chicken-stocks-06b49648?utm_source=chatgpt.com)

[1]: https://www.ft.com/content/6a0f7e2c-f3b9-4eb6-961c-d69af28f7183?utm_source=chatgpt.com "Kardashian endorsement of skincare gadget creates K-beauty champion"
[2]: https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/?utm_source=chatgpt.com "Korean beauty startups bet booming US demand outlasts tariff pain"
[3]: https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045?utm_source=chatgpt.com "Samyang Foods Set to Post Strong 2Q Earnings -- Market Talk"
[4]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/?utm_source=chatgpt.com "South Korea to offer visa-free entry to Chinese tourists from late September"
[5]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-conditionally-approves-aliexpress-shinsegae-unit-joint-venture-2025-09-18/?utm_source=chatgpt.com "South Korea conditionally approves AliExpress, Shinsegae unit joint venture"
[6]: https://www.reuters.com/en/mbk-plans-sell-its-troubled-korean-supermarket-chain-homeplus-2025-06-13/?utm_source=chatgpt.com "MBK plans to sell its troubled Korean supermarket chain Homeplus"
[7]: https://www.tomshardware.com/tech-industry/korean-fried-chicken-stocks-surge-30-percent-as-nvidia-ceo-jensen-huang-dines-out-on-local-delicacy-entire-industry-buoyed-by-secret-ingredient-jensanity?utm_source=chatgpt.com "Korean fried chicken stocks surge 30% as Nvidia CEO Jensen Huang dines out on local delicacy - entire industry buoyed by secret ingredient, Jensanity"
