순서상 이번은 **R5 Loop 11 — 소비재·유통·브랜드 가격경로 검증 라운드**다.

이번 R5 Loop 11은 **K-food export, K-beauty structural winner, K-beauty ODM/distribution, legacy China-exposure beauty, e-commerce JV, e-commerce trust break, tourism retail policy event, K-food packaging/input shock**을 같이 본다.

```text
round = R5 Loop 11
round_id = round_176
large_sector = CONSUMER_RETAIL_BRAND
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true_for_retail_platform_trust_reference_non_krx
hard_4c_krx_confirmed = false
```

이번에도 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC 전체 구간은 안정적으로 확보하지 못했다. 대신 Reuters / FT / MarketWatch / Vogue Business / Business Insider / WSJ가 제공한 **가격 anchor, 이벤트 수익률, 매출·수출·시장규모·사용자·소비금액·규제 지표**로 계산 가능한 값만 계산했다. 30D/90D/180D full OHLC가 없는 항목은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R5 = 소비재·유통·브랜드
```

R5의 Stage 3는 “핫하다”, “K-food다”, “K-beauty다”, “중국 관광객이 온다”, “이커머스 제휴가 있다”가 아니다. **반복구매·해외 sell-through·ASP·OPM·재고/채권 품질·channel retention·trust**가 실제 돈으로 닫히는 순간이다.

---

# 2. 대상 canonical archetype

```text
K_FOOD_EXPORT_RECURRING
K_FOOD_GLOBAL_STAPLE_BRAND
K_FOOD_INPUT_PACKAGING_4C
K_BEAUTY_DEVICE_GLOBAL_BRAND
K_BEAUTY_INDIE_BRAND_US_CHANNEL
K_BEAUTY_ODM_DISTRIBUTOR_LEVERAGE
LEGACY_BEAUTY_CHINA_EXPOSURE_4C
ECOMMERCE_JV_SCALE_AND_DATA_GATE
ECOMMERCE_TRUST_BREACH_HARD_4C
TOURISM_RETAIL_DUTYFREE_EVENT
PRICE_ONLY_RALLY
EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
K-food:
- Samyang Buldak export
- Nongshim Shin Ramyun / Toomba expansion
- U.S. / Europe sell-through
- ASP / capacity expansion
- packaging shortage / naphtha shock / input-cost RedTeam

K-beauty:
- APR / Medicube device + skincare
- d’Alba / Tirtir / Torriden / Beauty of Joseon
- Silicon2 distribution leverage
- Cosmax / Kolmar ODM leverage
- Olive Young U.S. store
- tariff margin squeeze
- physical-store sell-through gate

Legacy beauty:
- AmorePacific / LG H&H
- China demand weakness
- duty-free / travel retail weakness
- COSRX plateau risk
- Chinese local brand competition

E-commerce / retail:
- E-Mart / Shinsegae / Gmarket
- Alibaba / AliExpress Korea JV
- customer data gate
- cross-border market share
- Coupang breach as non-KRX hard trust-break reference
- Naver / E-Mart / CJ Logistics opportunity

Tourism retail:
- Hotel Shilla
- Hyundai Department Store
- Paradise
- Hankook Cosmetics
- China visa-free policy
- tourist arrivals vs tourist spend / OPM
```

---

# 4. 국장 신규 후보 case

## Case A — Samyang Foods `structural_success_candidate + input/packaging 4C-watch`

```text
symbol = 003230
case_type = structural_success_candidate + 4C-watch
archetype = K_FOOD_EXPORT_RECURRING / K_FOOD_INPUT_PACKAGING_4C
```

### stage date

```text
Stage 1:
2023~2024
- Buldak global viral demand
- U.S. / Europe export growth
- spicy ramen challenge / global social-media demand

Stage 2:
2024-06-14
- 2Q OP estimate +84% YoY
- U.S. / Europe shipment growth
- ASP uplift
- capacity expansion
- shares +5.7%, close 647,000원

Stage 3:
2024-06-14 후보
- export growth + ASP + OP revision이 함께 나온 구간

Stage 4B:
Buldak single-SKU premium이 valuation을 먼저 끌면 후보

Stage 4C-watch:
2026-03-26
- Iran/Hormuz energy crisis로 naphtha / packaging shortage
- Samyang / Nongshim / Yonwoo 등 packaging shortage 압박
- 일부 공장 20~30% capacity operation context
```

Samyang Foods는 R5에서 여전히 K-food export 성공 benchmark다. 2024년 6월 Kiwoom은 Buldak 수출 호조, U.S./Europe shipment 증가, ASP 상승, capacity expansion을 근거로 2Q 영업이익을 812억 원, 전년 대비 +84%로 추정했고, 주가는 5.7% 오른 647,000원에 마감했다. 하지만 2026년에는 Hormuz/energy shock이 naphtha와 packaging shortage로 번지며 Samyang, Nongshim, Yonwoo 같은 소비재·화장품 포장재 사용 기업에 압박을 주는 4C-watch가 생겼다. 즉 R5에서는 수요뿐 아니라 **packaging/input availability**도 gate에 넣어야 한다. ([마켓워치][1])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch / Reuters reported anchors

entry_date:
2024-06-14

stage3_price:
647,000원

event_MFE_1D:
+5.7%

implied_prior_close:
647,000 / 1.057
= 약 611,921원

target_price:
830,000원

target_upside_from_stage3_price:
830,000 / 647,000 - 1
= +28.3%

OP_estimate_Q2:
81.2B won

OP_growth_estimate:
+84% YoY

2026_packaging_shock:
Samyang / Nongshim / Yonwoo packaging shortage context

MFE_30D / 90D / 180D / 1Y / 2Y:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = aligned_partial
rerating_result = K_food_export_rerating_candidate
stage_failure_type = green_success_candidate_with_input_packaging_watch
```

---

## Case B — Nongshim `success_candidate / global staple brand`

```text
symbol = 004370
case_type = success_candidate
archetype = K_FOOD_GLOBAL_STAPLE_BRAND
```

### stage date

```text
Stage 1:
2023~2024
- Shin Ramyun global staple
- K-food instant noodle export boom
- K-culture driven food demand

Stage 2:
2024-05-27
- Shin Ramyun 2023 sales 1.2T won / $883M
- nearly 60% overseas
- North America sales $538M, +10%
- U.S. annual sales target $1.5B by 2030

Stage 3:
보류
- global staple 구조는 좋지만
- OPM/EPS revision, channel sell-through, ASP, inventory 확인 필요

Stage 4B:
global staple narrative가 가격에 먼저 반영되면 후보

Stage 4C:
China slowdown, packaging/input shock, commodity cost, channel stuffing
```

Nongshim은 Samyang처럼 single viral SKU가 아니라 **global staple brand**에 가깝다. FT는 Shin Ramyun의 2023년 매출이 1.2조 원, 약 8.83억 달러였고, 매출의 거의 60%가 해외에서 나왔다고 보도했다. 북미 매출은 5.38억 달러로 10% 성장했고, Nongshim은 2030년 미국 연매출 15억 달러를 목표로 한다. 다만 global staple 구조가 좋아도 Stage 3는 OPM/EPS revision과 channel sell-through로 확인해야 한다. ([Financial Times][2])

### 실제 가격경로 검증

```text
price_data_source:
FT business evidence

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search

Shin_Ramyun_2023_sales:
1.2T won / $883M

overseas_sales_share:
nearly 60%

North_America_sales_2023:
$538M

North_America_sales_growth:
+10%

U.S._sales_target_2030:
$1.5B

target_growth_from_2023_North_America_sales:
1.5B / 538M - 1
= +178.8%

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = global_staple_brand_watch
stage_failure_type = stage2_watch_success_not_green
```

---

## Case C — APR / Medicube `structural_success + 4B-watch`

```text
symbol = 278470
case_type = structural_success + 4B-watch
archetype = K_BEAUTY_DEVICE_GLOBAL_BRAND
```

### stage date

```text
Stage 1:
2024 IPO / 2025 K-beauty device virality
- Medicube beauty device
- TikTok / Amazon / Ulta / creator-affiliate distribution

Stage 2:
2025-07~10
- APR stock up over 75% since IPO
- stage2 price anchor 158,300원
- market cap about $4.2B
- CEO stake 31%, billionaire narrative

Stage 3:
2025 Q4 후보
- Q4 revenue about $440M, +124% YoY
- overseas revenue about $362M, +203% YoY
- overseas share 87%
- FY 2025 revenue about $1.2B
- Medicube revenue about $1.1B
- TikTok Shop revenue $102.9M+
- Ulta 1,400+ store expansion

Stage 4B:
2025~2026
- stock up sharply after IPO
- Medicube revenue concentration 91.7%
- beauty device / single-brand concentration
```

APR/Medicube는 이번 R5 Loop 11에서도 structural success benchmark로 남긴다. Business Insider는 APR 주가가 IPO 이후 75% 이상 올라 158,300원에 거래됐고, 시총이 약 42억 달러라고 보도했다. Vogue Business는 2025년 4분기 APR 매출이 약 4.4억 달러로 +124%, 해외 매출이 약 3.62억 달러로 +203% 증가했고, Medicube가 FY 2025 매출 약 11억 달러로 전체의 대부분을 차지한다고 보도했다. 구조적 성공이지만 단일 브랜드·device concentration 때문에 4B-watch가 필요하다. ([Business Insider][3])

### 실제 가격경로 검증

```text
price_data_source:
Business Insider / Vogue Business anchors

stage2_price:
158,300원

IPO_to_stage2_MFE_minimum:
> +75%

implied_IPO_reference_price_from_75pct_gain:
158,300 / 1.75
= 약 90,457원 이하

market_cap_July_2025:
$4.2B

Q4_2025_revenue:
$440M

Q4_2025_revenue_growth:
+124% YoY

Q4_2025_overseas_revenue:
$362M

Q4_2025_overseas_growth:
+203% YoY

overseas_revenue_share_Q4:
87%

FY_2025_revenue:
$1.2B

Medicube_FY_2025_revenue:
$1.1B

Medicube_share_of_APR_revenue:
1.1 / 1.2
= 91.7%

TikTok_Shop_revenue:
$102.9M+

Amazon_Prime_Day_sales:
$22M

Ulta_store_expansion:
1,400+ stores

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = aligned
rerating_result = K_beauty_device_true_rerating_plus_4B_watch
stage_failure_type = green_success_candidate
```

---

## Case D — d’Alba / Silicon2 / Cosmax / Kolmar `success_candidate + overheat`

```text
symbols = 483650 / 257720 / 192820 / 161890
case_type = success_candidate + overheat
archetype = K_BEAUTY_INDIE_BRAND_US_CHANNEL / K_BEAUTY_ODM_DISTRIBUTOR_LEVERAGE
```

### stage date

```text
Stage 1:
2024~2025
- K-beauty U.S. e-commerce boom
- indie brand viral demand
- Amazon / TikTok / Sephora / Ulta / Target / Costco expansion

Stage 2:
2025-06-05
- Tirtir, d’Alba, Torriden, Beauty of Joseon retail talks
- Korea became biggest cosmetics exporter to U.S. in 2024
- top five K-beauty brands in U.S. e-commerce +71% over two years
- overall U.S. market +21%
- Cosmax / Kolmar ODM leverage
- Silicon2 distribution leverage

Stage 3:
없음
- retail talks / e-commerce virality만으로 Green 금지
- physical-store sell-through, repeat order, OPM, inventory/receivables 확인 필요

Stage 4B:
2025-06-05
- d’Alba shares more than doubled since debut last month
```

K-beauty indie/ODM basket은 Stage 2 후보지만 아직 Green은 아니다. Reuters는 Tirtir, d’Alba, Torriden, Beauty of Joseon 등이 Ulta, Sephora, Target, Costco 등 미국 오프라인 리테일러와 입점 논의를 진행 중이라고 보도했다. 한국은 2024년 미국 최대 화장품 수출국이 됐고, U.S. e-commerce 상위 5개 K-beauty 브랜드는 2년간 평균 71% 성장해 전체 미국 시장 21%를 크게 웃돌았다. 그러나 Silicon2 CEO는 장기 성공에는 physical-store sales가 필요하다고 말했다. 즉 e-commerce virality와 retail talks는 Stage 2이고, physical sell-through 전 Green은 아니다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters business and reported return anchors

stage3_price:
N/A

dAlba_reported_MFE_since_debut:
> +100%

top5_Korean_cosmetics_US_ecommerce_growth:
+71% over two years

overall_US_market_growth:
+21%

relative_growth_vs_US_market:
71 / 21
= 3.38x

retail_talks:
Ulta / Sephora / Target / Costco

ODM_model:
Cosmax / Kolmar used by indie K-beauty brands

Silicon2_price:
price_data_unavailable_after_deep_search

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = price_moved_without_evidence_for_dAlba / success_candidate_for_ODM_distribution
rerating_result = K_beauty_indie_retail_watch
stage_failure_type = stage2_evidence_not_green
```

---

## Case E — AmorePacific / LG H&H legacy beauty `failed_rerating / China exposure 4C-watch`

```text
symbols = 090430 / 051900
case_type = failed_rerating / 4C-watch
archetype = LEGACY_BEAUTY_CHINA_EXPOSURE_4C
```

### stage date

```text
Stage 1:
2024~2025
- K-beauty global revival
- COSRX / Laneige / Sulwhasoo U.S. transition 기대
- Western market pivot

Stage 2:
보류
- U.S. / Europe growth와 China decline offset 확인 필요

Stage 3:
없음
- K-beauty macro tailwind만으로 Green 금지

Stage 4C-watch:
2024~2026
- China beauty demand weakness
- C-Beauty local brands rising
- duty-free / travel retail weakness
- premium beauty slowdown
```

AmorePacific과 LG H&H 같은 legacy beauty는 “K-beauty가 좋다”와 “회사가 좋다”를 분리해야 한다. FT와 Vogue는 APR 같은 신흥 K-beauty brand가 AmorePacific·LG H&H 같은 기존 대형사를 앞지르는 흐름을 설명했고, Reuters는 중국의 C-Beauty 브랜드가 빠르게 점유율을 가져가면서 글로벌 beauty player에게 압박을 주고 있다고 보도했다. 중국은 여전히 750억 달러 규모의 beauty market이지만, 현지 브랜드 경쟁과 느린 성장 때문에 legacy premium exposure에는 4C-watch를 붙여야 한다. ([Financial Times][5])

### 실제 가격경로 검증

```text
price_data_source:
FT / Vogue / Reuters legacy-China beauty context

stage3_price:
N/A

AmorePacific_stock_OHLC:
price_data_unavailable_after_deep_search

LG_H&H_stock_OHLC:
price_data_unavailable_after_deep_search

China_beauty_market_size:
about $75B

legacy_risk_factors:
China demand weakness
C-Beauty local competition
duty-free / travel retail weakness
premium beauty slowdown

new_K_beauty_outperformance_context:
APR became most valuable Korean beauty group in FT framing
APR valuation about $6B, fourfold stock rise since January in FT source

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch / insufficient_price_data
rerating_result = legacy_K_beauty_China_exposure_break
stage_failure_type = should_have_been_yellow_or_red
```

---

## Case F — E-Mart / Shinsegae / Alibaba JV `success_candidate + data gate watch`

```text
symbols = 139480 / 004170
case_type = success_candidate + data/privacy watch
archetype = ECOMMERCE_JV_SCALE_AND_DATA_GATE
```

### stage date

```text
Stage 1:
2024-12-26
- Shinsegae / E-Mart and Alibaba International JV
- Gmarket + AliExpress Korea
- cross-border e-commerce scale-up

Stage 2:
2024-12-26
- 50:50 online-shopping JV announcement
- E-Mart shares +5.5%
- Gmarket / AliExpress Korea run independently

Stage 2 강화:
2025-09-18
- KFTC conditional approval
- JV expected cross-border e-commerce market share 41%
- Gmarket 50M customer data
- Korean spending on Chinese online imports 4.7T won, +32%
- Alibaba share 62% by value

Stage 3:
없음
- JV와 data scale만으로 Green 금지
- Gmarket GMV, take-rate, margin, customer retention, data-compliance 확인 필요

Stage 4B:
JV / Alibaba headline로 valuation이 먼저 움직이면 후보

Stage 4C:
KFTC data restrictions, customer-data misuse, cross-border margin pressure, Temu/AliExpress price competition
```

E-Mart/Shinsegae-Alibaba JV는 R5 retail/e-commerce의 좋은 Stage 2다. WSJ는 E-Mart가 Alibaba와 AliExpress Korea·Gmarket을 묶는 50:50 JV를 추진한다고 보도했고, 발표 후 E-Mart 주가는 5.5% 상승했다. 이후 KFTC는 조건부 승인을 내렸지만, Gmarket의 5,000만 고객 데이터와 Alibaba의 data analytics 결합에 대한 우려 때문에 3년간 한국 고객 해외쇼핑 데이터 공유를 제한했다. JV는 해외직구 시장 점유율 41%가 예상되고, 2024년 중국발 온라인 쇼핑은 4.7조 원으로 전년 대비 +32%, Alibaba는 금액 기준 62%를 차지했다. ([월스트리트저널][6])

### 실제 가격경로 검증

```text
price_data_source:
WSJ / Reuters JV and regulatory anchors

stage3_price:
N/A

E_Mart_event_MFE:
+5.5%

JV_structure:
50:50 joint venture

assets:
AliExpress Korea + Gmarket

KFTC_approval:
conditional

expected_cross_border_market_share:
41%

Gmarket_customer_database:
50M customers

data_sharing_restriction:
3 years

Korean_spending_on_Chinese_online_imports_2024:
4.7T won / $3.4B

growth:
+32% YoY

Alibaba_share_by_value:
62%

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + regulatory_data_watch
rerating_result = e_commerce_JV_scale_watch
stage_failure_type = stage2_watch_success_not_green
```

---

## Case G — Coupang breach / Korean e-commerce trust break `hard 4C reference + KRX competitor opportunity`

```text
symbols = CPNG / 035420 / 139480 / 000120 / Kurly unlisted
case_type = hard_4C_reference + competitor_success_candidate
archetype = ECOMMERCE_TRUST_BREACH_HARD_4C
```

### stage date

```text
Stage 1:
2025-11
- Coupang data breach disclosed
- Korean e-commerce trust shock

Stage 2:
KRX competitor opportunity
- Naver / E-Mart / Kurly / CJ Logistics fast-delivery opportunity

Stage 3:
없음
- competitor opportunity만으로 Green 금지
- actual user retention, GMV, margin, logistics utilization 확인 필요

Stage 4C:
2025-11~2026-02
- 34M users affected
- mobile MAU -3.5%
- average daily consumer spending -6.3%
- Coupang stock -34% since breach
- Naver mobile users +23%
- CJ Logistics overnight/one-day shipment volume +120% YoY
```

Coupang은 US-listed라 국장 직접 종목은 아니지만, 한국 e-commerce trust hard 4C reference로 반드시 넣어야 한다. Reuters는 Coupang data leak이 3,400만 users에 영향을 줬고, names, phone numbers, shipping addresses가 노출됐으며, 과학기술정보통신부가 정교한 cyberattack보다 management failure 쪽으로 판단했다고 보도했다. 이후 Coupang mobile users는 11월 대비 1월에 -3.5%, average daily spending은 -6.3% 감소했고, 주가는 breach 이후 약 -34%였다. 반면 Naver mobile users는 +23%, CJ Logistics overnight/one-day delivery volume은 4Q에 +120% 증가했다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters e-commerce breach / competitor anchor

stage3_price:
N/A

Coupang_users_affected:
34M

Coupang_mobile_user_activity_change:
-3.5% from November to January

Coupang_average_daily_spending_change:
-6.3%

Coupang_average_daily_spending_January:
139.2B won / $97M

Coupang_stock_drawdown_since_breach:
about -34%

Naver_mobile_users:
+23% over same period

CJ_Logistics_overnight_or_one_day_volume_growth:
+120% YoY in Q4

Coupang_Q4_revenue_estimate_trim:
-2.2%

Coupang_core_earnings_estimate_trim:
-6.7%

hard_4C_krx_direct:
false

hard_4C_reference:
true
```

### alignment

```text
score_price_alignment = thesis_break_for_Coupang / success_candidate_for_competitors
rerating_result = e_commerce_trust_break_and_share_shift_watch
stage_failure_type = hard_4C_reference_non_krx
```

---

## Case H — Hotel Shilla / Hyundai Department / Paradise / Hankook Cosmetics `tourism retail event premium`

```text
symbols = 008770 / 069960 / 034230 / 123690
case_type = event_premium / success_candidate
archetype = TOURISM_RETAIL_DUTYFREE_EVENT
```

### stage date

```text
Stage 1:
2025-08-06
- China group-tourist visa-free entry policy
- department store / hotel / casino / cosmetics basket expectation

Stage 2:
2025-08-06
- Hyundai Department Store +7.1%
- Hotel Shilla +4.8%
- Paradise +2.9%
- Hankook Cosmetics +9.9%

Stage 2 추가:
2025-09-29
- visa-free programme starts
- Chinese groups of 3+ can stay 15 days
- programme runs through June 2026

Stage 3:
없음
- 관광객 수 증가만으로 Green 금지
- tourist spend, duty-free sales, casino drop/hold, OPM 확인 필요

Stage 4B:
정책 발표일 동반 급등

Stage 4C:
anti-Chinese rallies, low-spend tour mix, duty-free margin weakness, tourism-policy fade
```

관광·면세·백화점 basket은 R5의 전형적인 Stage 2/event premium이다. Reuters는 중국 단체관광객 무비자 정책 발표 후 Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%가 올랐다고 보도했다. 이후 2025년 9월 29일부터 3명 이상 중국 단체관광객은 15일간 무비자로 체류할 수 있게 됐고, 정책은 2026년 6월까지 이어진다. 그러나 President Lee가 anti-Chinese/anti-foreigner rallies 단속을 지시할 정도로 관광 회복에는 social trust risk도 붙는다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters event return and tourism policy anchors

stage3_price:
N/A

Hyundai_Department_event_MFE_1D:
+7.1%

Hotel_Shilla_event_MFE_1D:
+4.8%

Paradise_event_MFE_1D:
+2.9%

Hankook_Cosmetics_event_MFE_1D:
+9.9%

visa_free_period:
2025-09-29 to 2026-06

visa_free_stay:
15 days

group_condition:
3+ Chinese tourists

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium / success_candidate
rerating_result = tourism_retail_recovery_watch
stage_failure_type = stage2_watch_success_not_green
```

---

# 5. 이번 R5 case별 요약표

| case                          | 분류                             |                                                                       실제 가격검증 | alignment             |
| ----------------------------- | ------------------------------ | ----------------------------------------------------------------------------: | --------------------- |
| Samyang Foods                 | structural_success + 4C-watch  |                  647,000원, +5.7%, target upside +28.3%; packaging shock watch | aligned_partial       |
| Nongshim                      | success_candidate              |                   Shin Ramyun $883M, overseas nearly 60%, U.S. target +178.8% | global staple Stage 2 |
| APR / Medicube                | structural_success + 4B        |                       158,300원, IPO 이후 >75%, Q4 revenue +124%, overseas +203% | aligned + 4B          |
| d’Alba / Silicon2 / ODM       | overheat + Stage 2             |                         d’Alba >2x, top5 K-beauty ecom +71%, U.S. market +21% | event premium         |
| Amore / LG H&H                | failed_rerating / 4C-watch     |                       China / C-Beauty / travel retail risk, OHLC unavailable | thesis watch          |
| E-Mart / Shinsegae-Alibaba    | success_candidate + data watch |                                  E-Mart +5.5%, JV share 41%, Gmarket 50M data | Stage 2               |
| Coupang breach / competitors  | hard 4C reference              | CPNG -34%, users -3.5%, spending -6.3%, Naver +23%, CJ Logistics +120% volume | trust break           |
| Hotel Shilla / tourism basket | event premium                  |                               Shilla +4.8%, Hyundai Dept +7.1%, Hankook +9.9% | event premium         |

---

# 6. score-price alignment 판정

```text
aligned / structural_success_candidate:
- Samyang Foods
- APR / Medicube

success_candidate:
- Nongshim
- E-Mart / Shinsegae-Alibaba JV
- Silicon2 / Cosmax / Kolmar ODM-distribution basket
- tourism retail basket, 단 Stage 2

event_premium:
- d’Alba post-debut rally
- Hotel Shilla / Hyundai Department / Hankook Cosmetics tourism policy event
- E-Mart Alibaba JV announcement, if price outruns GMV/margin
- competitor rally after Coupang breach

price_moved_without_evidence:
- d’Alba >2x before physical sell-through
- tourism-policy rally before tourist spend / OPM
- K-beauty retail talks before store sell-through
- e-commerce JV headline before GMV/take-rate/margin

thesis_break_watch:
- Amore / LG H&H legacy China exposure
- K-food packaging/input shortage
- K-beauty tariff / saturation / China decline
- E-Mart JV data gate
- Coupang trust break as reference hard 4C

4B-watch:
- APR valuation / single-brand concentration
- d’Alba post-debut >2x
- tourism policy basket
- E-Mart +5.5% JV event
- Samyang Buldak single-SKU premium

hard_4C:
- Coupang retail-platform trust break as non-KRX reference case
```

---

# 7. 점수비중 교정

## 올릴 축

```text
repeat_demand +5
export_growth +5
overseas_sales_mix +5
ASP_uplift +4
channel_sellthrough +5
physical_store_sellthrough +5
OPM_improvement +5
inventory_quality +4
receivables_quality +4
platform_trust +5
customer_data_compliance +5
```

### 왜 올리나

Samyang은 export·ASP·OP revision이 같이 확인됐고, APR은 해외 매출·TikTok Shop·Amazon·Ulta 같은 채널 conversion이 실제 매출로 내려왔다. E-Mart/Alibaba JV는 customer data scale과 cross-border scale이 있지만, R5 Green은 GMV와 take-rate, margin, data compliance가 확인될 때다. Coupang breach는 플랫폼 신뢰가 무너지면 사용자와 소비액이 실제로 빠지는 것을 보여준다.

## 내릴 축

```text
viral_product_only -5
brand_heat_only -5
retail_talks_without_sell_through -5
IPO_or_debut_rally -5
China_exposure_without_offset -5
tourism_policy_only -5
ecommerce_JV_without_GMV_margin -4
customer_data_risk -5
packaging_input_shortage -4
tariff_margin_uncertainty -4
```

### 왜 내리나

d’Alba처럼 debut 후 2배 이상 오른 경우는 sell-through 전이면 4B다. tourism basket은 정책 발표일 급등했지만 spend/OPM 전에는 event premium이다. E-Mart JV는 scale이 있지만 customer data gate가 있다. Amore/LG H&H는 K-beauty macro가 좋아도 China exposure를 통과해야 한다.

## Green gate 강화 조건

```text
R5 Stage 3-Green 필수:
1. 반복구매 / 반복수요 확인
2. 해외 매출 비중 증가
3. channel sell-through 확인
4. physical-store sell-through 확인
5. ASP 또는 product mix 개선
6. OPM / FCF 개선
7. 재고·매출채권 안정
8. tariff / packaging / input shock 통과
9. customer data / platform trust 통과
10. 가격경로가 evidence 이후 따라옴

금지:
viral TikTok만 있음
입점 논의만 있음
IPO/debut rally만 있음
관광정책만 있음
이커머스 JV headline만 있음
China decline offset 없음
single product story만 있음
data breach / trust break 존재
```

## 4B 조기감지 조건

```text
4B-watch:
Stage 3 이후 2~4배 이상 상승
IPO/debut 후 1개월 내 2배 이상 상승
single SKU / single device 의존도 높음
미국 입점 기대가 sell-through보다 먼저 가격에 반영
관광정책 발표일 retail/beauty basket 동반 급등
JV / M&A / data-scale headline으로 retail주 급등
좋은 뉴스에도 원가·포장재·관세 리스크 증가

4B-elevated:
브랜드 성장률 normalize
U.S. tariff 비용 전가 실패
physical-store sell-through 확인 안 됨
채널 확장 후 재고 증가
customer data / privacy gate 발생
tourism arrivals는 늘지만 spend 약함
```

## 4C hard gate 조건

```text
food safety recall
packaging/input shortage causing production disruption
tariff margin squeeze
channel stuffing
inventory build
receivables spike
single product fad collapse
retail channel sell-through failure
China sales collapse not offset by U.S./Europe
customer data breach
platform trust break
GMV/user/spending deterioration
tourism spend failure
```

이번 R5 Loop 11에서 KRX 직접 hard 4C는 확정하지 않는다. 다만 **Coupang breach는 Korean retail-platform hard 4C reference**로 둔다. 국장 관점에서는 Naver, E-Mart, CJ Logistics 같은 competitor opportunity가 생겼지만, 그 자체도 user retention·GMV·margin으로 확인되어야 Green이다.

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

---

# 9. patch-ready 출력

## docs/round/round_176.md 요약

```md
# R5 Loop 11. Consumer / Retail / Brand Price Validation

이번 라운드는 R5 Loop 11 price-validation 라운드다.

핵심 결론:
- Samyang Foods remains a K-food export structural-success candidate. Stage anchor was 647,000 won, +5.7%, with target 830,000 won and Q2 OP estimate +84%. But 2026 energy/naphtha packaging shortage adds 4C-watch for K-food packaging/input risk.
- Nongshim is global staple brand Stage 2. Shin Ramyun 2023 sales 1.2T won / $883M, overseas share nearly 60%, North America sales $538M, U.S. target $1.5B by 2030. OPM/EPS/channel sell-through required.
- APR/Medicube is structural success plus 4B-watch. Stage2 price 158,300 won, IPO-to-stage2 MFE >75%, Q4 2025 revenue +124%, overseas +203%, FY revenue $1.2B, Medicube $1.1B, but Medicube share 91.7% requires concentration watch.
- d’Alba/Silicon2/Cosmax/Kolmar basket is Stage 2 plus overheat. Top-five K-beauty U.S. ecommerce brands +71% over two years vs U.S. market +21%, but d’Alba >2x since debut and physical sell-through still required.
- AmorePacific/LG H&H are legacy China-exposure 4C-watch. New K-beauty winners are outperforming while C-Beauty and China/travel retail weakness pressure legacy premium beauty.
- E-Mart/Shinsegae-Alibaba JV is Stage 2 plus data gate. E-Mart +5.5%; JV expected cross-border share 41%; Gmarket 50M customer data; KFTC restricted data sharing for three years.
- Coupang breach is non-KRX hard 4C reference. 34M users affected, mobile activity -3.5%, daily spending -6.3%, stock -34%; competitors Naver, E-Mart, Kurly and CJ Logistics saw opportunity, but Green requires GMV/margin confirmation.
- Hotel Shilla / Hyundai Department / Paradise / Hankook Cosmetics tourism basket is event premium. Policy-day returns were +4.8% / +7.1% / +2.9% / +9.9%, but tourist spend and OPM required.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 176 R5 Loop 11 Consumer Retail Brand Price Validation

## 반영 내용
- R5 Loop 11 price-validation 라운드를 추가했다.
- K-food export, global ramen staple, K-beauty device, K-beauty indie/ODM, legacy China-exposure beauty, e-commerce JV/data gate, e-commerce trust break, tourism retail event를 비교했다.
- Reuters/FT/MarketWatch/Vogue Business/Business Insider/WSJ anchors로 가능한 MFE/MAE 및 business/event/trust metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- repeat demand, export growth, overseas mix, channel sell-through, physical-store sell-through, OPM/FCF, platform trust, customer-data compliance 가중치 강화
- viral product-only, retail talks without sell-through, debut rally, tourism policy-only, e-commerce JV without GMV/margin, China exposure without offset, data risk 감점 강화
- R5 4B-watch와 platform-trust 4C-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r5_loop11_samyang_buldak_export_packaging_watch","symbol":"003230","company_name":"Samyang Foods","case_type":"structural_success_candidate","primary_archetype":"K_FOOD_EXPORT_RECURRING","stage2_date":"2024-06-14","stage3_date":"2024-06-14_candidate","stage4c_date":"2026-03-26_watch","price_validation":{"price_data_source":"MarketWatch/Reuters reported anchors","stage3_price":647000,"event_mfe_1d_pct":5.7,"implied_prior_close":611921,"target_price":830000,"target_upside_pct":28.3,"op_estimate_q2_krw_bn":81.2,"op_growth_estimate_pct":84,"packaging_shock_context":"Samyang/Nongshim/Yonwoo packaging shortage under naphtha/energy crisis","price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned_partial","rerating_result":"K_food_export_rerating_candidate","notes":"Export/ASP/OP revision supports Stage 3 candidate; packaging/input risk requires 4C-watch."}
{"case_id":"r5_loop11_nongshim_shin_global_staple","symbol":"004370","company_name":"Nongshim","case_type":"success_candidate","primary_archetype":"K_FOOD_GLOBAL_STAPLE_BRAND","stage2_date":"2024-05-27","price_validation":{"price_data_source":"FT business evidence","stage3_price":null,"shin_2023_sales_krw_trn":1.2,"shin_2023_sales_usd_mn":883,"overseas_sales_share_pct":60,"north_america_sales_2023_usd_mn":538,"north_america_growth_pct":10,"us_sales_target_2030_usd_bn":1.5,"target_growth_from_2023_na_sales_pct":178.8,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"global_staple_brand_watch","notes":"Global staple and overseas expansion are Stage 2; OPM/EPS and channel sell-through required for Green."}
{"case_id":"r5_loop11_apr_medicube_structural_4b","symbol":"278470","company_name":"APR / Medicube","case_type":"structural_success","primary_archetype":"K_BEAUTY_DEVICE_GLOBAL_BRAND","stage2_date":"2025-07-08","stage3_date":"2025-Q4_candidate","stage4b_date":"2025-2026","price_validation":{"price_data_source":"Business Insider/Vogue Business anchors","stage2_price":158300,"ipo_to_stage2_mfe_min_pct":75,"implied_ipo_reference_price_max":90457,"market_cap_july_2025_usd_bn":4.2,"q4_2025_revenue_usd_mn":440,"q4_2025_revenue_growth_pct":124,"q4_2025_overseas_revenue_usd_mn":362,"q4_2025_overseas_growth_pct":203,"q4_overseas_revenue_share_pct":87,"fy_2025_revenue_usd_bn":1.2,"medicube_fy_2025_revenue_usd_bn":1.1,"medicube_revenue_share_pct":91.7,"tiktok_shop_revenue_usd_mn":102.9,"amazon_prime_day_sales_usd_mn":22,"ulta_store_expansion_count":1400,"price_validation_status":"reported_price_and_revenue_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"K_beauty_device_true_rerating_plus_4B_watch","notes":"Revenue conversion supports structural success, but Medicube concentration and valuation require 4B-watch."}
{"case_id":"r5_loop11_indie_kbeauty_odm_distribution_watch","symbol":"483650/257720/192820/161890","company_name":"d'Alba / Silicon2 / Cosmax / Kolmar basket","case_type":"overheat","primary_archetype":"K_BEAUTY_INDIE_BRAND_US_CHANNEL","stage2_date":"2025-06-05","stage4b_date":"2025-06-05","price_validation":{"price_data_source":"Reuters business and reported return anchors","stage3_price":null,"dalba_reported_mfe_since_debut_pct":100,"top5_korean_cosmetics_us_ecommerce_growth_pct":71,"overall_us_market_growth_pct":21,"relative_growth_vs_us_market_multiple":3.38,"retail_talks":["Ulta","Sephora","Target","Costco"],"odm_model":["Cosmax","Kolmar"],"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence_for_dalba_success_candidate_for_odm_distribution","rerating_result":"K_beauty_indie_retail_watch","notes":"Retail talks and ecommerce growth are Stage 2; physical sell-through, repeat orders, OPM and working-capital quality required before Green."}
{"case_id":"r5_loop11_amore_lghh_legacy_china_exposure","symbol":"090430/051900","company_name":"AmorePacific / LG Household & Health Care","case_type":"failed_rerating","primary_archetype":"LEGACY_BEAUTY_CHINA_EXPOSURE_4C","stage4c_date":"2024-2026_watch","price_validation":{"price_data_source":"FT/Vogue/Reuters legacy China beauty context","stage3_price":null,"china_beauty_market_size_usd_bn":75,"legacy_risk_factors":["China demand weakness","C-Beauty local competition","duty-free/travel retail weakness","premium beauty slowdown"],"new_kbeauty_outperformance_context":"APR became most valuable Korean beauty group in FT framing","apr_valuation_context_usd_bn":6,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch_insufficient_price_data","rerating_result":"legacy_K_beauty_China_exposure_break","notes":"K-beauty macro is not enough; China and travel-retail weakness block Green until U.S./Europe offset is proven."}
{"case_id":"r5_loop11_emart_shinsegae_alibaba_jv_data_gate","symbol":"139480/004170","company_name":"E-Mart / Shinsegae / Alibaba JV","case_type":"success_candidate","primary_archetype":"ECOMMERCE_JV_SCALE_AND_DATA_GATE","stage2_date":"2024-12-26/2025-09-18","price_validation":{"price_data_source":"WSJ/Reuters JV and regulatory anchors","stage3_price":null,"emart_event_mfe_pct":5.5,"jv_structure":"50:50 joint venture","assets":["AliExpress Korea","Gmarket"],"kftc_approval":"conditional","expected_cross_border_market_share_pct":41,"gmarket_customer_database_mn":50,"data_sharing_restriction_years":3,"korean_spending_chinese_online_imports_2024_krw_trn":4.7,"growth_pct":32,"alibaba_share_by_value_pct":62,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_regulatory_data_watch","rerating_result":"e_commerce_JV_scale_watch","notes":"JV scale is Stage 2; GMV, take-rate, margin, retention and data compliance required before Green."}
{"case_id":"r5_loop11_coupang_breach_ecommerce_trust_reference","symbol":"CPNG/035420/139480/000120","company_name":"Coupang breach / Naver-E-Mart-CJ Logistics competitor basket","case_type":"4c_reference","primary_archetype":"ECOMMERCE_TRUST_BREACH_HARD_4C","stage4c_date":"2025-11_to_2026-02","price_validation":{"price_data_source":"Reuters e-commerce breach / competitor anchor","stage3_price":null,"coupang_users_affected_mn":34,"mobile_activity_change_pct":-3.5,"average_daily_spending_change_pct":-6.3,"average_daily_spending_january_krw_bn":139.2,"coupang_stock_drawdown_since_breach_pct":-34,"naver_mobile_users_change_pct":23,"cj_logistics_overnight_one_day_volume_growth_pct":120,"q4_revenue_estimate_trim_pct":-2.2,"q4_core_earnings_estimate_trim_pct":-6.7,"hard_4c_krx_direct":false,"hard_4c_reference":true,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_for_Coupang_success_candidate_for_competitors","rerating_result":"e_commerce_trust_break_and_share_shift_watch","notes":"Coupang is non-KRX but is the clean R5 platform-trust hard 4C reference; competitors need GMV/margin confirmation before Green."}
{"case_id":"r5_loop11_tourism_retail_china_visa_event","symbol":"008770/069960/034230/123690","company_name":"Hotel Shilla / Hyundai Department Store / Paradise / Hankook Cosmetics","case_type":"event_premium","primary_archetype":"TOURISM_RETAIL_DUTYFREE_EVENT","stage2_date":"2025-08-06/2025-09-29","stage4b_date":"2025-08-06","price_validation":{"price_data_source":"Reuters event return and tourism policy anchors","stage3_price":null,"hyundai_department_event_mfe_1d_pct":7.1,"hotel_shilla_event_mfe_1d_pct":4.8,"paradise_event_mfe_1d_pct":2.9,"hankook_cosmetics_event_mfe_1d_pct":9.9,"visa_free_period":"2025-09-29_to_2026-06","visa_free_stay_days":15,"group_condition":"3+ Chinese tourists","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"tourism_retail_recovery_watch","notes":"Visa-free tourist policy is Stage 2/event; tourist spend, sell-through, duty-free sales and OPM required before Green."}
```

## shadow weight row 초안

```csv
archetype,repeat_demand,export_growth,overseas_mix,asp,channel_sellthrough,physical_store_sellthrough,opm_fcf,inventory_quality,platform_trust,data_compliance,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
K_FOOD_EXPORT_RECURRING,+5,+5,+5,+4,+5,+3,+5,+4,+2,+1,-2,+4,+3,Samyang export/ASP/OP revision supports Stage 3 candidate but packaging/input watch remains.
K_FOOD_GLOBAL_STAPLE_BRAND,+5,+5,+5,+3,+5,+4,+4,+4,+2,+1,-1,+3,+3,Nongshim global staple is Stage 2 until OPM/EPS/sell-through confirm.
K_FOOD_INPUT_PACKAGING_4C,+0,+0,+0,+0,+0,+0,+4,+5,+2,+1,-3,+3,+5,Packaging/naphtha shortage can become R5 input-cost 4C.
K_BEAUTY_DEVICE_GLOBAL_BRAND,+5,+5,+5,+3,+5,+5,+5,+3,+2,+1,-2,+5,+3,APR is structural success but valuation/concentration require 4B-watch.
K_BEAUTY_INDIE_BRAND_US_CHANNEL,+3,+5,+5,+2,+5,+5,+4,+4,+2,+1,-5,+5,+4,d'Alba/indie K-beauty requires physical sell-through before Green.
K_BEAUTY_ODM_DISTRIBUTOR_LEVERAGE,+3,+5,+5,+2,+5,+5,+4,+5,+2,+1,-3,+4,+4,Cosmax/Kolmar/Silicon2 benefit only if brand sell-through and working capital hold.
LEGACY_BEAUTY_CHINA_EXPOSURE_4C,+2,+3,+3,+2,+3,+3,+4,+5,+2,+1,-2,+4,+5,Amore/LG H&H legacy China exposure blocks macro K-beauty Green until offset is proven.
ECOMMERCE_JV_SCALE_AND_DATA_GATE,+4,+3,+2,+2,+5,+4,+5,+4,+5,+5,-4,+5,+5,E-Mart/Alibaba JV needs GMV/take-rate/margin and data compliance.
ECOMMERCE_TRUST_BREACH_HARD_4C,+0,+0,+0,+0,+0,+0,+0,+0,+5,+5,0,+3,+5,Coupang breach is R5 platform-trust hard 4C reference.
TOURISM_RETAIL_DUTYFREE_EVENT,+2,+3,+3,+2,+5,+5,+4,+3,+3,+1,-5,+5,+4,Tourism retail needs spend/sell-through/OPM, not just visitor policy.
```

---

# 이번 R5 Loop 11 결론

R5는 **진짜 winner와 event premium이 가장 비슷하게 보이는 섹터**다. 그래서 좋은 브랜드라도 sell-through와 OPM을 보기 전에는 Green을 늦게 줘야 한다.

```text
1. Samyang Foods는 export + ASP + OP revision이 함께 나온 Stage 3 후보다.
   다만 packaging/input shock을 4C-watch로 붙여야 한다.

2. Nongshim은 global staple brand Stage 2다.
   해외 매출과 U.S. target은 좋지만 OPM/EPS/sell-through 전 Stage 3는 아니다.

3. APR/Medicube는 R5 structural success다.
   그러나 Medicube revenue concentration 91.7%와 valuation 상승 때문에 4B-watch가 필요하다.

4. d’Alba / Silicon2 / Cosmax / Kolmar basket은 K-beauty Stage 2다.
   retail talks와 e-commerce growth는 좋지만 physical-store sell-through 전 Green 금지다.

5. Amore / LG H&H는 K-beauty macro와 회사 실적을 분리해야 한다.
   China/C-Beauty/travel-retail weakness는 4C-watch다.

6. E-Mart / Shinsegae-Alibaba JV는 e-commerce scale Stage 2다.
   하지만 GMV/take-rate/margin/data compliance 전 Green은 아니다.

7. Coupang breach는 non-KRX지만 R5 platform trust hard 4C reference다.
   국장 competitor opportunity도 실제 GMV와 margin으로 확인해야 한다.

8. Hotel Shilla / Hyundai Department / Paradise / Hankook Cosmetics는 tourism policy event premium이다.
   tourist arrivals보다 tourist spend와 OPM이 Stage 3 조건이다.
```

한 문장으로 압축하면:

> **R5에서 진짜 Stage 3는 “K-food·K-beauty·관광·이커머스가 핫하다”가 아니라, 반복구매·해외 sell-through·ASP·OPM·재고/채권 품질·platform trust가 실제 이익 체급으로 내려오는 순간이다.**

[1]: https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045?utm_source=chatgpt.com "Samyang Foods Set to Post Strong 2Q Earnings -- Market Talk"
[2]: https://www.ft.com/content/4218f2b8-5498-411b-81fe-e3c836868d64?utm_source=chatgpt.com "Maker of Shin instant ramen expands overseas as Korean noodles become hit"
[3]: https://www.businessinsider.com/south-korea-kim-byung-hoon-beauty-billionaire-kylie-jenner-fan-2025-7?utm_source=chatgpt.com "Meet South Korea's new millennial beauty billionaire, who counts Kylie Jenner as a fan of his skincare gadgets"
[4]: https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/?utm_source=chatgpt.com "Korean beauty startups bet booming US demand outlasts tariff pain"
[5]: https://www.ft.com/content/6a0f7e2c-f3b9-4eb6-961c-d69af28f7183?utm_source=chatgpt.com "Kardashian endorsement of skincare gadget creates K-beauty champion"
[6]: https://www.wsj.com/business/e-mart-alibaba-plan-online-shopping-joint-venture-e5cfdc37?utm_source=chatgpt.com "E-mart, Alibaba Plan Online-Shopping Joint Venture"
[7]: https://www.reuters.com/business/retail-consumer/coupang-braces-increased-competition-amid-fallout-south-korea-data-breach-2026-02-25/?utm_source=chatgpt.com "Coupang braces for increased competition amid fallout from South Korea data breach"
[8]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/?utm_source=chatgpt.com "South Korea to offer visa-free entry to Chinese tourists from late September"
