순서상 이번은 **R5 Loop 14 — 소비재·유통·브랜드 가격경로 검증 라운드**다.

```text
round = R5 Loop 14
round_id = round_215
large_sector = CONSUMER_RETAIL_BRAND
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true_for_service_trust_reference
next_round = R6 Loop 14
```

이번 R5는 **Samyang Foods/Buldak, Nongshim/Shin Ramyun, APR/Medicube, d’Alba·Silicon2·K-beauty export basket, Hyundai Department Store·Hotel Shilla·Hankook Cosmetics 관광소비 basket, Shinsegae/E-Mart·Alibaba/Gmarket JV, Coupang data breach retail-trust reference, CJ Logistics·Shinsegae fulfilment read-through, 국내 소비둔화 reference**를 본다.

이번에도 KRX/Naver/Yahoo/Stooq 기준의 **수정주가 일봉 OHLC 전체 구간**은 안정적으로 확보하지 못했다. 그래서 30D/90D/180D/1Y full MFE·MAE는 임의 생성하지 않고, Reuters / FT / MarketWatch / AP가 제공한 **event return, event price, target price, 매출·영업이익 추정, IPO/valuation, 이용자·소비액 변화, 정책 기간, tariff risk**를 가격 anchor로 사용한다. full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R5 = 소비재·유통·브랜드
```

R5에서 진짜 Stage 3는 “K-food”, “K-beauty”, “중국 관광객”, “미국 진출”, “이커머스 JV”, “브랜드가 뜬다”, “SNS에서 바이럴이다”가 아니다.

진짜 Stage 3는 아래가 같이 닫히는 순간이다.

```text
K-food:
수출 물량 → ASP → 생산능력 → 채널 확장 → 재고/리콜 리스크 → OP margin

K-beauty:
온라인 바이럴 → 실제 반복구매 → 오프라인 sell-through → tariff 흡수 → 유통마진 → 브랜드 지속성

면세/백화점/호텔:
관광객 수 → 객단가 → 구매전환율 → 면세 수수료율 → 재고/임대료 → 영업이익

이커머스:
MAU → GMV → take-rate → fulfilment cost → 데이터/신뢰 → 규제조건 → FCF

생활소비:
소비심리 → 실제 retail sales → 가전/차/엔터테인먼트 지출 → discretionary margin
```

---

# 2. 대상 canonical archetype

```text
K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE
K_FOOD_EXPORT_REGULATORY_4C_WATCH
K_BEAUTY_DEVICE_BRAND_4B
K_BEAUTY_US_EXPANSION_STAGE2
CHINA_TOURISM_RETAIL_EVENT_PREMIUM
ECOMMERCE_CROSS_BORDER_JV_STAGE2_DATA_GATE
ECOMMERCE_TRUST_BREAK_HARD_REFERENCE
RETAIL_FULFILLMENT_UNIT_ECONOMICS_STAGE2
DOMESTIC_CONSUMPTION_SHOCK_4C_WATCH
```

---

# 3. deep sub-archetype

```text
K-food export:
- Samyang Foods / Buldak
- Nongshim / Shin Ramyun
- U.S. / Europe shipments
- ASP uplift, capacity expansion, export channel depth
- recall/regulatory/spiciness gate

K-beauty:
- APR / Medicube beauty device
- d'Alba / Beauty of Joseon / Tirtir / Torriden / COSRX
- Silicon2 distribution
- U.S. e-commerce and physical retail transition
- tariff and store sell-through gate

Retail / duty-free / tourism:
- Hyundai Department Store
- Hotel Shilla
- Hankook Cosmetics
- Paradise / tourist spend read-through
- Chinese group tourist visa-free policy
- visitor count vs spend-per-head

E-commerce / cross-border:
- Shinsegae / E-Mart / Gmarket
- Alibaba / AliExpress Korea JV
- KFTC conditional approval
- customer data-sharing restriction
- cross-border market share and China import growth

Retail trust:
- Coupang data breach
- Naver / E-Mart / Kurly / CJ Logistics read-through
- user migration, daily spending, logistics volume

Retail fulfilment:
- CJ Logistics / Shinsegae
- SSG.com and e-commerce logistics
- contract revenue uplift vs slower local growth

Domestic consumption:
- martial-law political shock
- December retail sales decline
- cars/home appliances and entertainment spending weakness
```

---

# 4. 국장 신규 후보 case

## Case A — Samyang Foods / Buldak export `structural_success_candidate + regulatory 4C-watch`

```text
symbol = 003230
case_type = structural_success_candidate + 4C-watch
archetype = K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE
```

### stage date

```text
Stage 1:
2024-06-14
- Buldak export demand becomes visible through U.S. and Europe shipments.
- ASP and capacity expansion become earnings drivers.

Stage 2 / Stage 3 candidate:
2024-06-14
- Kiwoom raised Samyang Foods 2Q OP estimate to 81.2B won.
- estimated OP growth: +84% YoY.
- higher Buldak ASP and increased shipments to U.S./Europe cited.
- production capacity expansion supports revenue and earnings.
- target price raised 26% to 830,000 won.
- shares closed +5.7% at 647,000 won.

Stage 4C-watch:
2024-06-12~14
- Denmark recalled three spicy Buldak products due capsaicin/spiciness concern.
- AP source says issue was not product-quality defect but acute poisoning concern due extreme spiciness.
- local regulation / spice tolerance / youth challenge risk remains watch.
```

Samyang Foods는 R5에서 가장 Stage 3에 가까운 소비재 case다. 단순 “K-food 인기”가 아니라 ASP 상승, 미국·유럽 shipment 증가, 생산능력 확장, OP estimate 상향, target price 상향, 주가 +5.7%가 같이 붙었다. 다만 Buldak은 강한 브랜드일수록 local regulation risk도 있다. Denmark recall은 품질 결함보다 spiciness/capsaicin risk였지만, export brand scoring에는 regulatory fit gate를 붙여야 한다. ([마켓워치][1])

### 실제 가격경로 검증

```json
{
  "case_id": "r5_loop14_samyang_buldak_export_stage3_candidate",
  "symbol": "003230",
  "stage3_date_candidate": "2024-06-14",
  "entry_date": "2024-06-14 reported close",
  "stage3_price_krw": 647000,
  "price_data_source": "MarketWatch/Dow Jones event anchor + AP Denmark recall anchor",
  "event_mfe_pct": 5.7,
  "q2_op_estimate_krw_bn": 81.2,
  "q2_op_estimate_yoy_growth_pct": 84,
  "target_price_krw": 830000,
  "target_price_raise_pct": 26,
  "target_upside_from_stage3_price_pct": 28.3,
  "drivers": ["Buldak ASP increase", "U.S./Europe shipment growth", "capacity expansion"],
  "denmark_recall_products_count": 3,
  "recall_cause": "capsaicin/spiciness acute poisoning concern, not product-quality defect",
  "regulatory_fit_watch": true,
  "mfe_30d_90d_180d_1y_2y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = aligned_partial
rerating_result = K_food_export_brand_stage3_candidate
stage_failure_type = export_brand_success_but_local_regulatory_fit_gate
```

---

## Case B — Nongshim / Shin Ramyun global expansion `success_candidate, price unavailable`

```text
symbol = 004370
case_type = success_candidate + insufficient_price_data
archetype = K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE
```

### stage date

```text
Stage 1:
2024-05-27
- Korean ramen exports hit record scale.
- Nongshim accelerates overseas expansion.
- Shin Ramyun becomes global K-food flagship.

Stage 2:
2024-05-27
- instant noodle industry around $50B globally.
- Korean instant noodle exports hit $1B in the prior year.
- Shin Ramyun 2023 sales: 1.2T won / $883M.
- nearly 60% of Shin Ramyun sales from overseas.
- Nongshim target: triple annual U.S. sales to $1.5B by 2030.

Stage 3:
없음
- direct listed price anchor unavailable.
- Green requires U.S. sell-through, Europe channel buildout, factory utilization, gross margin, China slowdown offset.
```

Nongshim은 Samyang보다 가격 anchor가 약하지만, global brand evidence는 강하다. FT는 Shin Ramyun 2023 매출이 1.2T won, 약 $883M이고 거의 60%가 해외에서 나왔다고 보도했다. 또 Nongshim은 2030년까지 U.S. annual sales를 $1.5B로 세 배 키우겠다는 목표를 제시했다. 하지만 이번 라운드에서는 event-day KRX price anchor를 찾지 못해 Stage 3를 주지 않는다. ([Financial Times][2])

### 실제 가격경로 검증

```json
{
  "case_id": "r5_loop14_nongshim_shin_ramyun_global_expansion",
  "symbol": "004370",
  "stage2_date": "2024-05-27",
  "stage3_price": null,
  "price_data_source": "FT brand/export anchor",
  "global_instant_noodle_market_usd_bn": 50,
  "korean_instant_noodle_exports_prior_year_usd_bn": 1,
  "shin_ramyun_2023_sales_krw_trn": 1.2,
  "shin_ramyun_2023_sales_usd_mn": 883,
  "overseas_sales_share_pct": 60,
  "us_sales_target_2030_usd_bn": 1.5,
  "direct_stock_event_price": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["U.S. sell-through", "Europe channel buildout", "factory utilization", "gross margin", "China slowdown offset"]
}
```

### alignment

```text
score_price_alignment = success_candidate_but_price_data_unavailable
rerating_result = K_food_global_brand_stage2
stage_failure_type = global_brand_sales_not_event_price_green
```

---

## Case C — APR / Medicube beauty device `structural_success_candidate + 4B-overheat`

```text
symbol = 278470
case_type = structural_success_candidate + overheat
archetype = K_BEAUTY_DEVICE_BRAND_4B
```

### stage date

```text
Stage 1:
2025-01~2025-07
- Medicube beauty-device virality accelerates.
- U.S. consumer demand shifts from cosmetics-only to skincare devices.

Stage 2:
2025-07~2025-10
- APR market cap around $4.2B in July context; later $6B in FT context.
- stock up more than 75% since IPO in July context.
- FT later reports stock up more than four-fold since January.
- device promoted by Kylie Jenner / TikTok.
- device price around $180 in FT article.
- nearly 80% of Q2 2025 revenue from overseas.
- facial skincare device forms about one-third of U.S. sales.

Stage 4B:
2025-10
- +4x YTD-type price path and $6B market value create overheat watch.
- Green requires repeat purchase, device attach-rate, return rate, regulatory compliance, tariff absorption, offline channel durability.
```

APR은 R5에서 매우 강한 brand-device success candidate다. 기존 K-beauty가 화장품 bottle이었다면, APR은 device/beauty-tech로 ASP와 narrative를 바꾼 case다. FT는 APR 주가가 2025년 1월 이후 4배 이상 올라 $6B market value에 도달했고, Q2 2025 매출의 거의 80%가 해외에서 나왔으며, facial skincare device가 U.S. sales의 약 1/3을 차지한다고 보도했다. 하지만 +4x rerating은 4B-watch다. ([Financial Times][3])

### 실제 가격경로 검증

```json
{
  "case_id": "r5_loop14_apr_medicube_beauty_device_4b",
  "symbol": "278470",
  "stage2_date": "2025-07_to_2025-10",
  "stage4b_date": "2025-10",
  "stage3_price": null,
  "price_data_source": "FT and Business Insider APR valuation/stock-return anchors",
  "market_cap_july_context_usd_bn": 4.2,
  "market_cap_october_context_usd_bn": 6.0,
  "stock_gain_since_ipo_july_context_pct": 75,
  "stock_gain_since_january_ft_context": "more_than_four_fold",
  "device_price_ft_context_usd": 180,
  "overseas_revenue_share_q2_2025_pct": 80,
  "device_share_of_us_sales_pct": 33,
  "repeat_purchase_confirmed": false,
  "device_return_rate_confirmed": false,
  "tariff_absorption_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = structural_success_candidate_but_overheat
rerating_result = K_beauty_device_brand_stage2
stage_failure_type = viral_device_rerating_needs_repeat_purchase_and_channel_margin
```

---

## Case D — K-beauty U.S. expansion basket / d’Alba·Silicon2·Amorepacific `success_candidate + tariff/brick-and-mortar gate`

```text
symbols = 483650 / 257720 / 090430 / 192820 / 161890
case_type = success_candidate + 4C-watch
archetype = K_BEAUTY_US_EXPANSION_STAGE2
```

### stage date

```text
Stage 1:
2024~2025
- South Korea becomes major U.S. cosmetics supplier.
- TikTok/Amazon/e-commerce drive K-beauty growth.

Stage 2:
2025-06-05
- South Korea replaced France as biggest cosmetics exporter to U.S. in 2024.
- Korea overtook Germany to become world’s third-largest beauty product exporter after France and U.S.
- four fifths of Korea’s $13B cosmetics output are exports.
- top five Korean cosmetics brands in U.S. e-commerce grew 71% on average over two years.
- overall U.S. market grew 21%; top five French brands grew 15%.
- d’Alba Global shares more than doubled since debut one month earlier.
- d’Alba in talks with Costco, Ulta, Target.
- Sephora to launch Torriden and Beauty of Joseon.
- COSRX, now under Amorepacific, shows signs of growth plateauing as competition rises.

Stage 4C-watch:
2025
- baseline 10% U.S. tariff already imposed.
- planned 25% tariff may require price increases.
- longer-term success requires physical-store sell-through, not online virality alone.
```

K-beauty는 R5의 구조 후보지만, 이제부터는 “바이럴”보다 **오프라인 sell-through와 tariff absorption**이 더 중요하다. Reuters는 한국이 2024년 U.S. cosmetics exporter 1위가 됐고, 한국 top 5 cosmetics brands의 U.S. e-commerce sales가 2년간 평균 71% 성장했다고 보도했다. 반면 K-beauty는 경쟁심화, 중국 둔화, 10~25% tariff, 오프라인 유통 검증이라는 gate가 붙는다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "case_id": "r5_loop14_kbeauty_us_expansion_tariff_gate",
  "symbols": "483650/257720/090430/192820/161890",
  "stage2_date": "2025-06-05",
  "stage3_price": null,
  "price_data_source": "Reuters/AP K-beauty expansion and tariff anchors",
  "korea_us_cosmetics_export_rank_2024": 1,
  "korea_global_beauty_export_rank_context": 3,
  "korea_cosmetics_output_2024_usd_bn": 13,
  "export_share_of_output_pct": 80,
  "top5_korean_us_ecommerce_sales_growth_2y_pct": 71,
  "overall_us_market_growth_2y_pct": 21,
  "top5_french_us_ecommerce_sales_growth_2y_pct": 15,
  "d_alba_stock_since_debut": "more_than_double",
  "us_imports_of_korean_cosmetics_2024_usd_bn_ap": 1.7,
  "us_imports_growth_2024_pct_ap": 54,
  "baseline_tariff_pct": 10,
  "planned_tariff_risk_pct": 25,
  "physical_store_sellthrough_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_4C_watch
rerating_result = K_beauty_US_expansion_stage2
stage_failure_type = viral_ecommerce_growth_not_physical_channel_margin_green
```

---

## Case E — China tourism retail / department store·duty-free·beauty basket `event_premium`

```text
symbols = 069960 / 008770 / 123690 / 034230 / 004170
case_type = event_premium + 4B-watch
archetype = CHINA_TOURISM_RETAIL_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-03-20
- South Korea announces plan for visa-free Chinese group tourists.
- tourism, duty-free, department stores and beauty retail become consumer catalyst.

Stage 2:
2025-08-06
- visa-free entry for Chinese group tourists from 2025-09-29 to 2026-06.
- 2024 Korea foreign visitors: 16.4M, +48% YoY.
- Chinese nationals were largest share at 28%.
- Korea targets 18.5M visitors in 2025.
- Hyundai Department Store +7.1%.
- Hotel Shilla +4.8%.
- Paradise +2.9%.
- Hankook Cosmetics +9.9%.

Stage 4B:
2025-08-06
- tourism-stock rally occurs before actual tourist spend, duty-free basket size, conversion rate and margin.
```

이 case는 R5 retail/event premium의 정석이다. 중국 관광객 visa-free 정책은 명확한 catalyst이고, 현대백화점 +7.1%, 호텔신라 +4.8%, 한국화장품 +9.9%가 바로 반응했다. 하지만 Stage 3는 입국자 수가 아니라 객단가, 면세 전환율, 구매 품목 mix, 수수료율, 재고와 인건비를 통과해야 한다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "case_id": "r5_loop14_china_tourism_retail_dutyfree_beauty_event",
  "symbols": "069960/008770/123690/034230/004170",
  "stage2_date": "2025-08-06",
  "stage4b_date": "2025-08-06",
  "stage3_price": null,
  "price_data_source": "Reuters China tourist visa-free and retail-stock reaction anchors",
  "visa_free_start": "2025-09-29",
  "visa_free_end": "2026-06",
  "visitors_2024_mn": 16.4,
  "visitors_2024_yoy_growth_pct": 48,
  "chinese_visitor_share_2024_pct": 28,
  "visitor_target_2025_mn": 18.5,
  "hyundai_department_store_event_mfe_pct": 7.1,
  "hotel_shilla_event_mfe_pct": 4.8,
  "paradise_event_mfe_pct": 2.9,
  "hankook_cosmetics_event_mfe_pct": 9.9,
  "spend_per_head_confirmed": false,
  "dutyfree_conversion_confirmed": false,
  "gross_margin_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_4B_watch
rerating_result = China_tourism_retail_event_stage2
stage_failure_type = tourist_count_not_spend_margin_green
```

---

## Case F — Shinsegae / E-Mart / Alibaba-Gmarket JV `success_candidate + data/competition gate`

```text
symbols = 004170 / 139480
case_type = success_candidate + 4C-watch
archetype = ECOMMERCE_CROSS_BORDER_JV_STAGE2_DATA_GATE
```

### stage date

```text
Stage 1:
2024-12-26
- Shinsegae affiliate E-Mart plans JV with Alibaba International.
- Gmarket and AliExpress Korea to be combined under new JV.
- Gmarket had been struggling against Coupang, Naver, AliExpress, Temu.

Stage 2:
2024-12-26
- Bloomberg/Reuters context: JV valued around $4B.
- Shinsegae contributes 100% Gmarket stake.
- AliExpress Korea and Gmarket remain operated independently.

Stage 2 validation:
2025-09-18
- KFTC conditionally approves JV.
- JV controls Gmarket and AliExpress Korea.
- concern: Gmarket’s 50M Korean customer data plus Alibaba analytics.
- data sharing on Korean overseas-shopping customers prohibited for three years.
- combined cross-border e-commerce market share expected at 41%.
- Koreans’ online spending on products shipped from China rose 32% to 4.7T won in 2024.
- Alibaba accounted for 62% of this market by value.
```

Shinsegae/E-Mart의 Alibaba JV는 R5 e-commerce Stage 2다. 좋은 점은 cross-border commerce scale이다. 위험은 데이터와 규제다. KFTC는 Gmarket 50M customer data와 Alibaba analytics 결합을 우려해 3년간 고객 해외쇼핑 데이터 공유를 금지했다. 즉 이 JV는 Green이 되려면 market share가 아니라 take-rate, logistics, customer retention, regulatory compliance가 확인되어야 한다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "case_id": "r5_loop14_shinsegae_emart_alibaba_gmarket_jv",
  "symbols": "004170/139480",
  "stage2_date": "2024-12-26/2025-09-18",
  "stage3_price": null,
  "price_data_source": "Reuters JV announcement and KFTC approval anchors",
  "reported_jv_valuation_usd_bn": 4,
  "emart_contribution": "100% stake in Gmarket",
  "platforms": ["Gmarket", "AliExpress Korea"],
  "korean_customer_database_count_mn": 50,
  "data_sharing_restriction_years": 3,
  "expected_cross_border_market_share_pct": 41,
  "korean_online_china_import_spending_2024_krw_trn": 4.7,
  "spending_growth_2024_pct": 32,
  "alibaba_share_by_value_pct": 62,
  "take_rate_confirmed": false,
  "regulatory_clearance_full": "conditional",
  "direct_event_price": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_4C_watch
rerating_result = cross_border_ecommerce_JV_stage2
stage_failure_type = JV_scale_not_data_compliance_take_rate_green
```

---

## Case G — Coupang data breach / Korean retail trust read-through `hard reference`

```text
symbols = CPNG / 035420 / 139480 / 000120 / retail-logistics basket
case_type = hard_4C_reference + competitor_event_premium
archetype = ECOMMERCE_TRUST_BREAK_HARD_REFERENCE
```

### stage date

```text
Stage 1:
2025-11
- Coupang discloses massive data breach.
- consumer names, phone numbers and shipping addresses exposed.

Stage 4C-reference:
2026-02-25
- breach affected about 34M users.
- Science Ministry blamed management failure rather than sophisticated cyberattack.
- Coupang shares fell around 34% since disclosure.
- mobile user activity -3.5% from November to January.
- daily consumer spending -6.3% to about 139.2B won in January.
- revenue estimate cut 2.2%; core earnings estimate cut 6.7%.

Stage 2 competitor read-through:
2026-02-25
- Naver mobile users +23% from November to January.
- CJ Logistics overnight/one-day shipment volume +120% YoY in Q4.
- E-Mart, Kurly, Naver expand fast delivery.
```

Coupang은 미국상장이라 “국장 case”는 아니지만, R5 retail trust hard reference로는 반드시 필요하다. 생활소비 platform은 가격·배송속도만으로 moat가 유지되지 않고, 데이터 신뢰가 깨지면 이용자와 소비액이 바로 움직인다. 다만 Naver/E-Mart/CJ Logistics 수혜는 competitor event premium이지 자동 Green은 아니다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "case_id": "r5_loop14_coupang_retail_trust_break_readthrough",
  "symbols": "CPNG/035420/139480/000120_readthrough",
  "stage4c_date": "2026-02-25_reference",
  "stage3_price": null,
  "price_data_source": "Reuters Coupang breach and competitor read-through anchor",
  "affected_users_mn": 34,
  "exposed_data": ["names", "phone_numbers", "shipping_addresses"],
  "payment_or_login_data_exposed": false,
  "government_cause_assessment": "management_failure_rather_than_sophisticated_cyberattack",
  "coupang_share_decline_since_disclosure_pct": -34,
  "mobile_user_activity_change_pct": -3.5,
  "daily_consumer_spending_change_pct": -6.3,
  "daily_consumer_spending_jan_krw_bn": 139.2,
  "revenue_estimate_cut_pct": -2.2,
  "core_earnings_estimate_cut_pct": -6.7,
  "naver_mobile_users_change_pct": 23,
  "cj_logistics_overnight_one_day_volume_growth_q4_pct": 120,
  "direct_korean_competitor_stage3_confirmed": false
}
```

### alignment

```text
score_price_alignment = thesis_break_reference
rerating_result = ecommerce_retail_trust_hard_gate
stage_failure_type = data_breach_trust_break
```

---

## Case H — CJ Logistics / Shinsegae fulfilment `evidence_good_but_price_failed`

```text
symbol = 000120
case_type = evidence_good_but_price_failed
archetype = RETAIL_FULFILLMENT_UNIT_ECONOMICS_STAGE2
```

### stage date

```text
Stage 1:
2024-06-17
- Shinsegae Group and CJ Logistics strengthen fulfilment/logistics alliance.
- SSG.com and e-commerce logistics become retail-service catalyst.

Stage 2:
2024-06-17
- Daiwa estimates CJ Logistics can gain around 300B won annual revenue uplift.
- alliance duration: three years.
- target price cut 17% to 116,000 won.
- outperform maintained.
- shares -0.2% at 99,100 won.
- slower local growth and overseas recovery delay cited.

Stage 3:
없음
- revenue uplift estimate was not enough for price confirmation.
- Green requires volume, unit economics, wage/fuel cost, automation, customer concentration.
```

CJ Logistics는 R5 retail fulfilment의 좋은 counterexample이다. Shinsegae와의 3년 deal은 연 300B won revenue uplift가 기대됐지만, 주가는 -0.2%였고 target price는 17% 하향됐다. 물류·유통에서 계약 매출은 Stage 2이고, Stage 3는 단가와 비용 구조가 닫혀야 한다. ([마켓워치][8])

### 실제 가격경로 검증

```json
{
  "case_id": "r5_loop14_cj_logistics_shinsegae_fulfillment_price_failed",
  "symbol": "000120",
  "stage2_date": "2024-06-17",
  "stage3_price": null,
  "price_data_source": "MarketWatch/Dow Jones CJ Logistics event anchor",
  "annual_revenue_uplift_estimate_krw_bn": 300,
  "partnership_duration_years": 3,
  "partners": ["Shinsegae Group", "SSG.com"],
  "target_price_krw": 116000,
  "target_price_cut_pct": -17,
  "event_price_krw": 99100,
  "event_mae_pct": -0.2,
  "target_upside_from_event_price_pct": 17.1,
  "issues": ["slower local business growth", "delay in overseas-business recovery"],
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = retail_fulfillment_contract_stage2
stage_failure_type = revenue_uplift_not_unit_economics_green
```

---

## Case I — Domestic retail sales shock `macro 4C-watch`

```text
symbols = 023530 / 139480 / 004170 / 069960 / 066570 / discretionary basket
case_type = failed_rerating_reference
archetype = DOMESTIC_CONSUMPTION_SHOCK_4C_WATCH
```

### stage date

```text
Stage 1:
2024-12-03
- martial-law shock hits consumer sentiment and year-end shopping.

Stage 4C-watch:
2025-02-03
- December retail sales -0.6% MoM.
- retail sales failed to grow for fourth month.
- car and home-appliance sales -4.1% MoM.
- entertainment spending -0.6%.
- Korea economy grew only 0.1% in Q4.
- won hit 15-year low in political shock context.

Stage 3:
N/A
```

R5에서 소비재·유통주는 수출 브랜드만 보면 안 된다. 국내 discretionary retail은 정치 shock와 소비심리에 직접 맞는다. Reuters는 2024년 12월 retail sales가 -0.6% MoM였고, 자동차·가전 판매가 -4.1%, entertainment spending이 -0.6%였다고 보도했다. 즉 백화점·마트·가전·레저소비 basket은 “금리/관광/정책”보다 소비심리와 가처분소득을 먼저 봐야 한다. ([Reuters][9])

### 실제 가격경로 검증

```json
{
  "case_id": "r5_loop14_domestic_retail_sales_consumption_shock",
  "symbols": "023530/139480/004170/069960/066570_discretionary_basket",
  "stage4c_watch_date": "2025-02-03",
  "stage3_price": null,
  "price_data_source": "Reuters Korea December retail-sales macro anchor",
  "december_retail_sales_mom_pct": -0.6,
  "months_without_retail_sales_growth": 4,
  "cars_home_appliances_sales_mom_pct": -4.1,
  "entertainment_spending_mom_pct": -0.6,
  "q4_gdp_growth_pct": 0.1,
  "won_context": "15-year low after political shock",
  "company_level_ohlc": "price_data_unavailable_after_deep_search",
  "stage3_mfe_mae": "N/A_macro_reference"
}
```

### alignment

```text
score_price_alignment = failed_rerating_reference
rerating_result = domestic_consumption_shock_gate
stage_failure_type = discretionary_retail_not_export_brand_green
```

---

# 5. 이번 R5 case별 stage date 요약

| case                     | Stage 1    | Stage 2                      | Stage 3           | Stage 4B                        | Stage 4C                            |
| ------------------------ | ---------- | ---------------------------- | ----------------- | ------------------------------- | ----------------------------------- |
| Samyang / Buldak         | 2024-06    | 2024-06                      | 2024-06 candidate | export-brand valuation watch    | Denmark recall/regulatory watch     |
| Nongshim / Shin Ramyun   | 2024-05    | 2024-05                      | N/A               | K-food global brand watch       | China slowdown / Europe execution   |
| APR / Medicube           | 2025-01~07 | 2025-07~10                   | N/A               | +4x / $6B overheat              | tariff/regulatory/return-rate watch |
| K-beauty basket          | 2025-06    | 2025-06                      | N/A               | IPO/brand viral premium         | tariff / offline sell-through       |
| China tourism retail     | 2025-03    | 2025-08                      | N/A               | retail/tourism event rally      | spend-per-head gap                  |
| Shinsegae/E-Mart/Alibaba | 2024-12    | 2025-09 conditional approval | N/A               | cross-border e-commerce premium | data-sharing / KFTC gate            |
| Coupang trust            | 2025-11    | competitor read-through      | N/A               | competitor premium              | hard trust reference                |
| CJ Logistics             | 2024-06    | 2024-06                      | N/A               | fulfilment contract watch       | price failed                        |
| Domestic retail shock    | 2024-12    | N/A                          | N/A               | N/A                             | macro consumption watch             |

---

# 6. 실제 가격경로 검증 총괄

| case                  |                                                    가격·사업 anchor | 해석                              | 판정                             |
| --------------------- | --------------------------------------------------------------: | ------------------------------- | ------------------------------ |
| Samyang Foods         |            +5.7%, 647,000 won, OP estimate +84%, target 830,000 | export brand near Stage 3       | aligned_partial                |
| Nongshim              |                        Shin Ramyun 1.2T won sales, 60% overseas | brand Stage 2, no price anchor  | success_candidate              |
| APR                   |      stock >4x since Jan, market cap $6B, overseas revenue ~80% | structural but overheat         | 4B-watch                       |
| K-beauty basket       |      d’Alba >2x since debut, Korean U.S. e-commerce brands +71% | success_candidate + tariff gate | 4C-watch                       |
| Tourism retail        | Hyundai Dept +7.1%, Hotel Shilla +4.8%, Hankook Cosmetics +9.9% | tourism event premium           | 4B-watch                       |
| Shinsegae/E-Mart JV   |                   $4B JV, 50M customers, 41% cross-border share | scale but data gate             | success_candidate              |
| Coupang trust         |                        shares -34%, users -3.5%, spending -6.3% | retail trust hard reference     | thesis_break_reference         |
| CJ Logistics          |                            revenue uplift 300B won, stock -0.2% | evidence good but price failed  | evidence_good_but_price_failed |
| Domestic retail shock |                       retail sales -0.6%, appliances/cars -4.1% | macro 4C-watch                  | failed reference               |

---

# 7. score-price alignment 판정

```text
aligned:
- Samyang Foods / Buldak export, partial.

structural_success_candidate:
- Samyang Foods.
- APR / Medicube, but overheat.
- K-beauty U.S. expansion basket.
- Nongshim, but event price unavailable.

success_candidate:
- Shinsegae/E-Mart Alibaba JV.
- CJ Logistics/Shinsegae fulfilment.
- China tourism retail basket, but only Stage 2 event.

evidence_good_but_price_failed:
- CJ Logistics.
- LG Innotek-like pattern repeated in consumer: estimates/contract revenue uplift not enough without unit economics.

event_premium:
- China tourism retail basket.
- APR / K-beauty viral device and d’Alba IPO-type rerating.
- Shinsegae/E-Mart Alibaba JV if traded before take-rate.

price_moved_without_evidence:
- Tourism retail if visitor-count headline is treated as spend/margin Green.
- K-beauty if online viral growth is treated as physical-channel profitability.
- APR if device virality is treated as repeat-purchase durability.
- Shinsegae/E-Mart JV if scale is treated as take-rate/FCF.

thesis_break_watch:
- Samyang regulatory/local-spiciness fit.
- K-beauty tariff and brick-and-mortar sell-through.
- Shinsegae/E-Mart data-sharing/KFTC restrictions.
- Domestic consumption shock.

thesis_break_reference:
- Coupang data breach / e-commerce trust break.

hard_4C_confirmed:
- direct KRX listed hard 4C: false.
- sector hard reference: Coupang retail/service trust break.
```

---

# 8. 점수비중 교정

## 올릴 축

```text
export_sellthrough +5
brand_ASP_power +5
capacity_to_revenue_conversion +4
offline_channel_sellthrough +5
tariff_absorption +5
tourist_spend_per_head +5
ecommerce_take_rate +5
data_trust_internal_control +5
fulfillment_unit_economics +5
domestic_consumption_sensitivity +4
```

### 왜 올리나

Samyang은 수출 물량, ASP, capacity, OP estimate가 함께 맞았기 때문에 R5 Stage 3 candidate다. APR과 K-beauty basket은 글로벌 브랜드 momentum이 강하지만, 오프라인 sell-through와 tariff 흡수가 없으면 4B다. 관광 retail은 방문객 수가 아니라 객단가가 중요하다. Shinsegae/E-Mart JV는 scale보다 data compliance와 take-rate이 중요하다. Coupang은 trust가 깨지면 이용자·소비액·주가가 동시에 움직일 수 있음을 보여준다.

## 내릴 축

```text
viral_brand_headline_only -5
visitor_count_only -5
online_ecommerce_growth_without_offline_sellthrough -5
JV_scale_without_take_rate -5
revenue_uplift_without_unit_economics -5
IPO_or_stock_pop_without_repeat_purchase -5
consumer_export_story_without_local_regulatory_fit -4
domestic_retail_ignored -4
data_breach_or_customer_trust_failure -5
```

### 왜 내리나

R5의 가장 큰 함정은 “브랜드가 떴다”를 바로 Stage 3로 주는 것이다. Samyang처럼 OP·ASP·수출·capacity가 같이 맞으면 가능하다. 하지만 APR처럼 4배 급등, d’Alba처럼 상장 후 두 배, 관광주처럼 정책 발표 직후 급등한 case는 4B-watch를 먼저 띄워야 한다. 소비재는 한 번 팔리는 것보다 반복구매, 채널마진, 규제·신뢰 유지가 더 중요하다.

---

# 9. Green gate 강화 조건

```text
R5 Stage 3-Green 필수:
1. export sell-through가 실제 매출/OP로 반영.
2. ASP 상승과 물량 증가가 동시에 확인.
3. 생산능력 확장이 revenue로 전환.
4. K-beauty는 온라인뿐 아니라 physical retail sell-through 확인.
5. tariff와 물류비를 가격/마진으로 흡수.
6. 관광 retail은 visitor count가 아니라 spend-per-head, duty-free conversion, gross margin 확인.
7. e-commerce JV는 take-rate, fulfilment cost, data compliance 확인.
8. 물류/fulfilment는 계약 매출보다 unit economics 확인.
9. 생활서비스는 data trust와 customer retention 확인.
10. price path가 evidence 이후 따라옴.
```

---

# 10. 4B 조기감지 조건

```text
4B-watch:
- K-food / K-beauty 브랜드가 단기 +50~100% 이상 rerating.
- IPO 후 한 달 만에 2배 이상 상승.
- viral TikTok / celebrity endorsement만으로 valuation 확대.
- 관광객 visa-free headline으로 retail/duty-free/cosmetics basket 급등.
- cross-border JV scale headline으로 take-rate 전 가격화.
- logistics revenue uplift estimate만으로 물류주 선반영.
- competitor read-through가 trust event 뒤 과도하게 붙음.
```

---

# 11. 4C hard gate 조건

```text
Hard 4C / strong watch:
- data breach / customer trust break.
- regulatory recall / local health regulation issue.
- tariff shock not absorbed by price.
- channel inventory buildup / sell-through failure.
- tourist arrivals without spending conversion.
- JV blocked or constrained by data regulation.
- fulfilment cost inflation crushing unit economics.
- domestic consumption shock / discretionary spending decline.
```

이번 R5 Loop 14에서 직접 국장 hard 4C는 확정하지 않는다. 다만 **Coupang data breach**를 retail/service trust hard reference로 두고, **Samyang regulatory fit**, **K-beauty tariff/offline sell-through**, **tourist spend conversion**, **Shinsegae/E-Mart data gate**, **domestic retail weakness**를 strong watch로 둔다.

---

# 12. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 13. 레포 반영용 patch-ready 출력

## docs/round/round_215.md 요약

```md
# R5 Loop 14. Consumer / Retail / Brand Price Validation

이번 라운드는 R5 Loop 14 price-validation 라운드다.

핵심 결론:
- Samyang Foods / Buldak is aligned_partial Stage 3 candidate. Kiwoom raised 2Q OP estimate to 81.2B won, +84% YoY, citing U.S./Europe shipments, Buldak ASP and capacity expansion. Target price raised 26% to 830,000 won; shares closed +5.7% at 647,000 won. Denmark recall remains regulatory-fit 4C-watch.
- Nongshim / Shin Ramyun is K-food global brand Stage 2. Shin Ramyun 2023 sales were 1.2T won / $883M, nearly 60% overseas; Nongshim targets U.S. annual sales of $1.5B by 2030. Direct event price unavailable.
- APR / Medicube is K-beauty device structural candidate plus 4B overheat. APR stock rose more than four-fold since January, market value reached $6B, nearly 80% of Q2 2025 revenue came from overseas, and beauty device formed about one-third of U.S. sales.
- K-beauty U.S. expansion basket is Stage 2 plus tariff/offline gate. South Korea replaced France as the biggest cosmetics exporter to the U.S. in 2024; top five Korean cosmetics brands in U.S. e-commerce grew 71% over two years; d’Alba shares more than doubled since debut. Physical-store sell-through and tariff absorption required.
- China tourism retail basket is event premium. Visa-free Chinese group tourists from Sept. 29 2025 to June 2026 drove Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%. Spend-per-head and margin required.
- Shinsegae/E-Mart Alibaba-Gmarket JV is e-commerce Stage 2 plus data gate. JV valued around $4B; KFTC conditionally approved but restricted data sharing for three years; JV expected cross-border share 41%. Take-rate, logistics and compliance required.
- Coupang data breach is retail trust hard reference. 34M users affected, shares -34% since disclosure, mobile activity -3.5%, daily spending -6.3%; Naver users +23% and CJ Logistics overnight/one-day volume +120% are read-through, not automatic Green.
- CJ Logistics / Shinsegae fulfilment is evidence_good_but_price_failed. 300B won annual revenue uplift expected, but shares -0.2% at 99,100 won and target cut 17%.
- Domestic retail sales shock is macro 4C-watch. December retail sales -0.6% MoM, cars/home appliances -4.1%, entertainment spending -0.6% amid political shock.
```

## docs/checkpoints/checkpoint_28a_round215_r5_loop14.md 요약

```md
# Checkpoint 28A Round 215 R5 Loop 14 Consumer Retail Brand Price Validation

## 반영 내용
- R5 Loop 14 price-validation 라운드를 추가했다.
- Samyang Foods, Nongshim, APR, K-beauty U.S. expansion basket, China tourism retail basket, Shinsegae/E-Mart Alibaba JV, Coupang trust reference, CJ Logistics/Shinsegae fulfilment, domestic retail-sales shock을 비교했다.
- Reuters / FT / MarketWatch / AP anchors로 가능한 event MFE/MAE, stage price, target price, OP estimate, user/spend change, JV/data metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- export sell-through, brand ASP power, capacity-to-revenue conversion, offline channel sell-through, tariff absorption, tourist spend per head, e-commerce take-rate, data trust/internal control, fulfilment unit economics, domestic consumption sensitivity 가중치 강화.
- viral brand headline-only, visitor count-only, online growth without offline sell-through, JV scale without take-rate, revenue uplift without unit economics, IPO/stock pop without repeat purchase, data breach/customer trust failure 감점 강화.
```

## data/e2r_case_library/cases_r5_loop14_round215.jsonl 초안

```jsonl
{"case_id":"r5_loop14_samyang_buldak_export_stage3_candidate","symbol":"003230","company_name":"Samyang Foods","case_type":"structural_success_candidate_4c_watch","primary_archetype":"K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE","stage3_date":"2024-06-14_candidate","stage4c_date":"2024-06_denmark_recall_watch","price_validation":{"price_data_source":"MarketWatch/Dow Jones event anchor + AP Denmark recall anchor","stage3_price_krw":647000,"event_mfe_pct":5.7,"q2_op_estimate_krw_bn":81.2,"q2_op_estimate_yoy_growth_pct":84,"target_price_krw":830000,"target_price_raise_pct":26,"target_upside_from_stage3_price_pct":28.3,"drivers":["Buldak ASP increase","U.S./Europe shipment growth","capacity expansion"],"denmark_recall_products_count":3,"recall_cause":"capsaicin/spiciness acute poisoning concern, not product-quality defect","regulatory_fit_watch":true,"mfe_30d_90d_180d_1y_2y":"price_data_unavailable_after_deep_search","mae_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"aligned_partial","rerating_result":"K_food_export_brand_stage3_candidate","notes":"Export ASP, shipment, capacity and OP estimate align; regulatory/local-spiciness gate remains."}
{"case_id":"r5_loop14_nongshim_shin_ramyun_global_expansion","symbol":"004370","company_name":"Nongshim","case_type":"success_candidate_price_unavailable","primary_archetype":"K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE","stage2_date":"2024-05-27","price_validation":{"price_data_source":"FT brand/export anchor","stage3_price":null,"global_instant_noodle_market_usd_bn":50,"korean_instant_noodle_exports_prior_year_usd_bn":1,"shin_ramyun_2023_sales_krw_trn":1.2,"shin_ramyun_2023_sales_usd_mn":883,"overseas_sales_share_pct":60,"us_sales_target_2030_usd_bn":1.5,"direct_stock_event_price":"price_data_unavailable_after_deep_search","stage3_conditions":["U.S. sell-through","Europe channel buildout","factory utilization","gross margin","China slowdown offset"]},"score_price_alignment":"success_candidate_but_price_data_unavailable","rerating_result":"K_food_global_brand_stage2","notes":"Global brand evidence strong, but no direct event price and margin/sell-through bridge yet."}
{"case_id":"r5_loop14_apr_medicube_beauty_device_4b","symbol":"278470","company_name":"APR / Medicube","case_type":"structural_success_candidate_overheat","primary_archetype":"K_BEAUTY_DEVICE_BRAND_4B","stage2_date":"2025-07_to_2025-10","stage4b_date":"2025-10","price_validation":{"price_data_source":"FT and Business Insider APR valuation/stock-return anchors","stage3_price":null,"market_cap_july_context_usd_bn":4.2,"market_cap_october_context_usd_bn":6.0,"stock_gain_since_ipo_july_context_pct":75,"stock_gain_since_january_ft_context":"more_than_four_fold","device_price_ft_context_usd":180,"overseas_revenue_share_q2_2025_pct":80,"device_share_of_us_sales_pct":33,"repeat_purchase_confirmed":false,"device_return_rate_confirmed":false,"tariff_absorption_confirmed":false,"mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"structural_success_candidate_but_overheat","rerating_result":"K_beauty_device_brand_stage2","notes":"Beauty-device virality and overseas growth are strong, but +4x rerating needs repeat-purchase/channel-margin proof."}
{"case_id":"r5_loop14_kbeauty_us_expansion_tariff_gate","symbol":"483650/257720/090430/192820/161890","company_name":"d'Alba / Silicon2 / Amorepacific / Cosmax / Kolmar basket","case_type":"success_candidate_4c_watch","primary_archetype":"K_BEAUTY_US_EXPANSION_STAGE2","stage2_date":"2025-06-05","price_validation":{"price_data_source":"Reuters/AP K-beauty expansion and tariff anchors","stage3_price":null,"korea_us_cosmetics_export_rank_2024":1,"korea_global_beauty_export_rank_context":3,"korea_cosmetics_output_2024_usd_bn":13,"export_share_of_output_pct":80,"top5_korean_us_ecommerce_sales_growth_2y_pct":71,"overall_us_market_growth_2y_pct":21,"top5_french_us_ecommerce_sales_growth_2y_pct":15,"d_alba_stock_since_debut":"more_than_double","us_imports_of_korean_cosmetics_2024_usd_bn_ap":1.7,"us_imports_growth_2024_pct_ap":54,"baseline_tariff_pct":10,"planned_tariff_risk_pct":25,"physical_store_sellthrough_confirmed":false,"mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_4C_watch","rerating_result":"K_beauty_US_expansion_stage2","notes":"Online viral growth and exports need physical retail sell-through and tariff absorption."}
{"case_id":"r5_loop14_china_tourism_retail_dutyfree_beauty_event","symbol":"069960/008770/123690/034230/004170","company_name":"Hyundai Department Store / Hotel Shilla / Hankook Cosmetics / Paradise / Shinsegae","case_type":"event_premium_4b_watch","primary_archetype":"CHINA_TOURISM_RETAIL_EVENT_PREMIUM","stage2_date":"2025-08-06","stage4b_date":"2025-08-06","price_validation":{"price_data_source":"Reuters China tourist visa-free and retail-stock reaction anchors","stage3_price":null,"visa_free_start":"2025-09-29","visa_free_end":"2026-06","visitors_2024_mn":16.4,"visitors_2024_yoy_growth_pct":48,"chinese_visitor_share_2024_pct":28,"visitor_target_2025_mn":18.5,"hyundai_department_store_event_mfe_pct":7.1,"hotel_shilla_event_mfe_pct":4.8,"paradise_event_mfe_pct":2.9,"hankook_cosmetics_event_mfe_pct":9.9,"spend_per_head_confirmed":false,"dutyfree_conversion_confirmed":false,"gross_margin_confirmed":false,"mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_4B_watch","rerating_result":"China_tourism_retail_event_stage2","notes":"Visitor-policy rally needs spend-per-head, duty-free conversion and margin proof."}
{"case_id":"r5_loop14_shinsegae_emart_alibaba_gmarket_jv","symbol":"004170/139480","company_name":"Shinsegae / E-Mart / Alibaba / Gmarket","case_type":"success_candidate_4c_watch","primary_archetype":"ECOMMERCE_CROSS_BORDER_JV_STAGE2_DATA_GATE","stage2_date":"2024-12-26/2025-09-18","price_validation":{"price_data_source":"Reuters JV announcement and KFTC approval anchors","stage3_price":null,"reported_jv_valuation_usd_bn":4,"emart_contribution":"100% stake in Gmarket","platforms":["Gmarket","AliExpress Korea"],"korean_customer_database_count_mn":50,"data_sharing_restriction_years":3,"expected_cross_border_market_share_pct":41,"korean_online_china_import_spending_2024_krw_trn":4.7,"spending_growth_2024_pct":32,"alibaba_share_by_value_pct":62,"take_rate_confirmed":false,"regulatory_clearance_full":"conditional","direct_event_price":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_4C_watch","rerating_result":"cross_border_ecommerce_JV_stage2","notes":"Scale and cross-border share are Stage 2; data compliance, take-rate and logistics economics required."}
{"case_id":"r5_loop14_coupang_retail_trust_break_readthrough","symbol":"CPNG/035420/139480/000120_readthrough","company_name":"Coupang / Naver / E-Mart / CJ Logistics read-through","case_type":"hard_4c_reference","primary_archetype":"ECOMMERCE_TRUST_BREAK_HARD_REFERENCE","stage4c_date":"2026-02-25_reference","price_validation":{"price_data_source":"Reuters Coupang breach and competitor read-through anchor","stage3_price":null,"affected_users_mn":34,"exposed_data":["names","phone_numbers","shipping_addresses"],"payment_or_login_data_exposed":false,"government_cause_assessment":"management_failure_rather_than_sophisticated_cyberattack","coupang_share_decline_since_disclosure_pct":-34,"mobile_user_activity_change_pct":-3.5,"daily_consumer_spending_change_pct":-6.3,"daily_consumer_spending_jan_krw_bn":139.2,"revenue_estimate_cut_pct":-2.2,"core_earnings_estimate_cut_pct":-6.7,"naver_mobile_users_change_pct":23,"cj_logistics_overnight_one_day_volume_growth_q4_pct":120,"direct_korean_competitor_stage3_confirmed":false},"score_price_alignment":"thesis_break_reference","rerating_result":"ecommerce_retail_trust_hard_gate","notes":"Retail-service trust break can move users, spending and competitor read-through; competitors are not automatic Green."}
{"case_id":"r5_loop14_cj_logistics_shinsegae_fulfillment_price_failed","symbol":"000120","company_name":"CJ Logistics","case_type":"evidence_good_but_price_failed","primary_archetype":"RETAIL_FULFILLMENT_UNIT_ECONOMICS_STAGE2","stage2_date":"2024-06-17","price_validation":{"price_data_source":"MarketWatch/Dow Jones CJ Logistics event anchor","stage3_price":null,"annual_revenue_uplift_estimate_krw_bn":300,"partnership_duration_years":3,"partners":["Shinsegae Group","SSG.com"],"target_price_krw":116000,"target_price_cut_pct":-17,"event_price_krw":99100,"event_mae_pct":-0.2,"target_upside_from_event_price_pct":17.1,"issues":["slower local business growth","delay in overseas-business recovery"],"mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"retail_fulfillment_contract_stage2","notes":"Revenue uplift estimate is not Green without unit economics, automation and cost control."}
{"case_id":"r5_loop14_domestic_retail_sales_consumption_shock","symbol":"023530/139480/004170/069960/066570_discretionary_basket","company_name":"Domestic discretionary retail basket","case_type":"failed_rerating_reference","primary_archetype":"DOMESTIC_CONSUMPTION_SHOCK_4C_WATCH","stage4c_date":"2025-02-03_watch","price_validation":{"price_data_source":"Reuters Korea December retail-sales macro anchor","stage3_price":null,"december_retail_sales_mom_pct":-0.6,"months_without_retail_sales_growth":4,"cars_home_appliances_sales_mom_pct":-4.1,"entertainment_spending_mom_pct":-0.6,"q4_gdp_growth_pct":0.1,"won_context":"15-year low after political shock","company_level_ohlc":"price_data_unavailable_after_deep_search","stage3_mfe_mae":"N/A_macro_reference"},"score_price_alignment":"failed_rerating_reference","rerating_result":"domestic_consumption_shock_gate","notes":"Domestic discretionary retail must be scored separately from export-brand and tourism-event narratives."}
```

## data/sector_taxonomy/score_weight_profiles_round215_r5_loop14_v1.csv 초안

```csv
archetype,export_sellthrough,brand_asp_power,capacity_to_revenue_conversion,offline_channel_sellthrough,tariff_absorption,tourist_spend_per_head,ecommerce_take_rate,data_trust_internal_control,fulfillment_unit_economics,domestic_consumption_sensitivity,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE,+5,+5,+4,+3,+4,+0,+0,+2,+1,+2,-3,+4,+3,Samyang shows export ASP/shipment/capacity can support Stage 3 candidate.
K_FOOD_EXPORT_REGULATORY_4C_WATCH,+5,+5,+4,+3,+4,+0,+0,+3,+1,+2,0,+4,+4,Denmark Buldak recall shows local regulatory-fit gate for export brands.
K_BEAUTY_DEVICE_BRAND_4B,+4,+5,+4,+5,+5,+0,+0,+2,+1,+2,-5,+5,+4,APR device virality needs repeat purchase, channel margin and tariff absorption.
K_BEAUTY_US_EXPANSION_STAGE2,+5,+5,+4,+5,+5,+0,+0,+2,+1,+2,-5,+5,+4,K-beauty U.S. expansion needs physical retail sell-through and tariff absorption.
CHINA_TOURISM_RETAIL_EVENT_PREMIUM,+1,+3,+1,+3,+2,+5,+0,+1,+2,+4,-5,+5,+3,Tourism retail rally needs spend-per-head, conversion and margin.
ECOMMERCE_CROSS_BORDER_JV_STAGE2_DATA_GATE,+2,+2,+1,+2,+3,+0,+5,+5,+4,+3,-5,+5,+4,Shinsegae/E-Mart Alibaba JV needs take-rate, logistics and data compliance.
ECOMMERCE_TRUST_BREAK_HARD_REFERENCE,+0,+0,+0,+0,+0,+0,+4,+5,+4,+3,0,+4,+5,Coupang breach confirms retail data-trust hard reference.
RETAIL_FULFILLMENT_UNIT_ECONOMICS_STAGE2,+1,+1,+2,+2,+2,+0,+3,+3,+5,+3,-5,+5,+3,CJ Logistics needs volume/unit economics, not only revenue uplift.
DOMESTIC_CONSUMPTION_SHOCK_4C_WATCH,+0,+0,+0,+0,+0,+0,+0,+1,+1,+5,0,+3,+4,Domestic retail shock separates export-brand stories from local discretionary demand.
```

---

# 이번 R5 Loop 14 결론

```text
1. Samyang Foods는 R5에서 aligned_partial Stage 3 candidate다.
   Buldak ASP, 미국/유럽 shipment, capacity, OP estimate, 주가반응이 같이 맞았다.

2. Nongshim은 K-food global brand Stage 2다.
   Shin Ramyun 해외매출 비중은 강하지만 event price와 margin bridge가 필요하다.

3. APR은 구조적 K-beauty device success_candidate지만 4B overheat다.
   +4x 주가, $6B valuation은 repeat purchase와 channel margin 확인 전에는 과열 watch가 떠야 한다.

4. K-beauty U.S. expansion은 Stage 2다.
   온라인 성장률은 강하지만 physical retail sell-through와 tariff absorption이 Green 조건이다.

5. 중국 관광 retail basket은 event premium이다.
   Hyundai Department +7.1%, Hotel Shilla +4.8%, Hankook Cosmetics +9.9%는 visitor headline이지 spend/margin Green이 아니다.

6. Shinsegae/E-Mart Alibaba JV는 cross-border e-commerce Stage 2다.
   $4B JV와 41% share는 좋지만 data-sharing restriction과 take-rate gate가 있다.

7. Coupang breach는 R5 retail trust hard reference다.
   이용자, 소비액, 주가가 동시에 빠졌고, 경쟁사 수혜는 자동 Green이 아니다.

8. CJ Logistics는 evidence_good_but_price_failed다.
   300B won revenue uplift estimate에도 주가는 -0.2%였고 target은 하향됐다.

9. 국내 retail sales shock은 R5 macro 4C-watch다.
   수출 브랜드와 국내 discretionary retail을 같은 점수로 보면 안 된다.
```

한 문장으로 압축하면:

> **R5에서 진짜 Stage 3는 “K-food·K-beauty·관광객·이커머스 JV·브랜드가 좋다”가 아니라, 수출 sell-through·ASP·반복구매·오프라인 전환·tariff 흡수·객단가·take-rate·data trust·unit economics가 실제 숫자로 닫히는 순간이다.**

* [마켓워치](https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045?utm_source=chatgpt.com)
* [AP News](https://apnews.com/article/f622b2d901990a08d180eee3ce2260f2?utm_source=chatgpt.com)
* [Financial Times](https://www.ft.com/content/4218f2b8-5498-411b-81fe-e3c836868d64?utm_source=chatgpt.com)
* [Financial Times](https://www.ft.com/content/6a0f7e2c-f3b9-4eb6-961c-d69af28f7183?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-conditionally-approves-aliexpress-shinsegae-unit-joint-venture-2025-09-18/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/retail-consumer/coupang-braces-increased-competition-amid-fallout-south-korea-data-breach-2026-02-25/?utm_source=chatgpt.com)
* [마켓워치](https://www.marketwatch.com/story/cj-logistics-set-to-gain-from-stronger-ties-with-retailer-shinsegae-market-talk-5d3e0c7a?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/asia/south-korea-dec-retail-sales-decline-amid-political-upheaval-2025-02-03/?utm_source=chatgpt.com)

[1]: https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045?utm_source=chatgpt.com "Samyang Foods Set to Post Strong 2Q Earnings -- Market Talk"
[2]: https://www.ft.com/content/4218f2b8-5498-411b-81fe-e3c836868d64?utm_source=chatgpt.com "Maker of Shin instant ramen expands overseas as Korean noodles become hit"
[3]: https://www.ft.com/content/6a0f7e2c-f3b9-4eb6-961c-d69af28f7183?utm_source=chatgpt.com "Kardashian endorsement of skincare gadget creates K-beauty champion"
[4]: https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/?utm_source=chatgpt.com "Korean beauty startups bet booming US demand outlasts tariff pain"
[5]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/?utm_source=chatgpt.com "South Korea to offer visa-free entry to Chinese tourists from late September"
[6]: https://www.reuters.com/markets/deals/south-koreas-shinsegae-set-up-joint-venture-with-alibaba-international-2024-12-26/?utm_source=chatgpt.com "South Korea's Shinsegae to set up joint venture with Alibaba International"
[7]: https://www.reuters.com/business/retail-consumer/coupang-braces-increased-competition-amid-fallout-south-korea-data-breach-2026-02-25/?utm_source=chatgpt.com "Coupang braces for increased competition amid fallout from South Korea data breach"
[8]: https://www.marketwatch.com/story/cj-logistics-set-to-gain-from-stronger-ties-with-retailer-shinsegae-market-talk-5d3e0c7a?utm_source=chatgpt.com "CJ Logistics Set to Gain From Stronger Ties With Retailer Shinsegae -- Market Talk"
[9]: https://www.reuters.com/markets/asia/south-korea-dec-retail-sales-decline-amid-political-upheaval-2025-02-03/?utm_source=chatgpt.com "South Korea December retail sales decline amid political upheaval"
