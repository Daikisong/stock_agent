순서상 이번은 **R5 Loop 10 — 소비재·유통·브랜드 가격경로 검증 라운드**다.

이번 R5는 **K-food, K-beauty, ODM/유통 플랫폼, legacy China exposure, 관광·면세·백화점, 의류·브랜드 M&A optionality**를 같이 본다. R5의 핵심은 “핫하다”가 아니라 **반복구매·해외 채널 sell-through·ASP·OPM·재고/채권 품질·현금전환**이다.

```text
round = R5 Loop 10
round_id = round_163
large_sector = CONSUMER_RETAIL_BRAND
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
```

이번 환경에서는 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC를 안정적으로 직접 확보하지 못했다. 대신 Reuters / FT / MarketWatch / Business Insider / Vogue Business / AP가 제공한 **가격 anchor, 이벤트 수익률, 매출·수출·시장규모·거래금액 지표**로 계산 가능한 값만 계산했다.

---

# 1. 이번 라운드 대섹터

```text
R5 = 소비재·유통·브랜드
```

R5의 Stage 3는 브랜드가 유명해지는 순간이 아니다. **유명세가 반복구매와 해외 채널 sell-through로 바뀌고, 그게 ASP·OPM·FCF로 내려오는 순간**이다.

---

# 2. 대상 canonical archetype

```text
K_FOOD_EXPORT_RECURRING
K_FOOD_GLOBAL_STAPLE_BRAND
K_FOOD_SINGLE_SKU_REGULATORY_WATCH
K_BEAUTY_DEVICE_GLOBAL_BRAND
K_BEAUTY_INDIE_BRAND_US_CHANNEL
K_BEAUTY_ODM_DISTRIBUTOR_LEVERAGE
K_BEAUTY_RETAIL_PLATFORM
LEGACY_BEAUTY_CHINA_EXPOSURE_4C
TOURISM_RETAIL_DUTYFREE_EVENT
APPAREL_M_AND_A_OPTIONALITY
PRICE_ONLY_RALLY
EVENT_PREMIUM
CHANNEL_SELLTHROUGH_GATE
```

---

# 3. deep sub-archetype

```text
K-food:
- Samyang Buldak export
- Denmark recall / partial reversal
- Nongshim Shin Ramyun global staple
- U.S. / Europe expansion
- single-SKU dependence
- local regulation / food-safety watch

K-beauty:
- APR / Medicube device + skincare
- d’Alba / Tirtir / Torriden / Beauty of Joseon
- Silicon2 distributor leverage
- Cosmax / Kolmar ODM leverage
- Olive Young U.S. store
- U.S. e-commerce → physical retail sell-through
- tariff margin squeeze
- China decline / saturation watch

Legacy beauty:
- AmorePacific / LG H&H
- China demand weakness
- duty-free weakness
- COSRX plateau
- local Chinese brand competition

Retail / tourism:
- Hotel Shilla
- Hyundai Department Store
- Paradise
- Hankook Cosmetics
- China visa-free policy
- China-Japan diplomatic reroute
- tourist arrivals vs tourist spend / OPM

Apparel / M&A:
- F&F / TaylorMade
- ROFR / legal dispute
- M&A optionality vs confirmed EPS accretion
```

---

# 4. 국장 신규 후보 case

## Case A — 삼양식품 `structural_success_candidate + regulatory 4C-watch`

```text
symbol = 003230
case_type = structural_success_candidate + 4C-watch
archetype = K_FOOD_EXPORT_RECURRING / K_FOOD_SINGLE_SKU_REGULATORY_WATCH
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
- single-SKU risk와 regulatory risk는 별도 RedTeam

Stage 4B:
Buldak valuation이 단일 제품 프리미엄으로 과도하게 확장된 구간이면 후보

Stage 4C-watch:
2024-06-12
- Denmark recalls three spicy Buldak variants
- acute-poisoning concern / capsaicin level
- 품질 문제라기보다 local regulation / consumer-safety issue

4C relief:
2024-08-08
- Denmark partly reverses ban for two variants
```

삼양식품은 R5에서 “바이럴이 실적으로 내려온” 좋은 후보 중 하나다. Kiwoom은 Buldak 수출 호조, U.S./Europe 출하 증가, ASP 상승, 생산능력 확장을 근거로 2024년 2분기 영업이익을 전년 대비 84% 증가한 812억 원으로 추정했고, 주가는 5.7% 오른 647,000원에 마감했다. 다만 Denmark recall은 hard 4C가 아니라 local-regulatory 4C-watch다. 덴마크는 capsaicin 위험을 이유로 3종을 리콜했으나, 이후 2종에 대해서는 금지를 해제했다. ([마켓워치][1])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch price/target anchor + AP/Reuters regulatory evidence

entry_date:
2024-06-14

stage3_price:
647,000원

stage2_event_MFE_1D:
+5.7%

implied_prior_close:
647,000 / 1.057
= 약 611,921원

target_price:
830,000원

target_upside_from_stage3_price:
(830,000 / 647,000) - 1
= +28.3%

OP_estimate_Q2:
81.2B won

OP_growth_estimate:
+84% YoY

Denmark_recall_status:
2024-06 recall, 2024-08 partial reversal

MFE_30D / 90D / 180D / 1Y / 2Y:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
price_data_unavailable_after_deep_search

peak_price:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = aligned_partial
rerating_result = K_food_export_rerating_candidate
stage_failure_type = green_success_candidate_with_regulatory_watch
```

---

## Case B — 농심 `success_candidate / global staple brand`

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
- Shin Ramyun 2023 sales 1.2조 원 / $883M
- nearly 60% overseas
- North America sales +10%, $538M
- U.S. annual sales target $1.5B by 2030

Stage 3:
보류
- global staple 구조는 강함
- OPM/EPS revision, channel sell-through, ASP, inventory 확인 필요

Stage 4B:
global staple narrative가 가격에 먼저 반영되면 후보

Stage 4C:
China slowdown, U.S. competition, commodity cost, channel stuffing, local regulation 시 후보
```

농심은 viral one-product가 아니라 **global staple brand** 후보에 가깝다. FT는 Shin Ramyun의 2023년 매출이 1.2조 원, 약 8.83억 달러였고, 매출의 거의 60%가 해외에서 나왔다고 보도했다. 북미 매출은 2023년 5.38억 달러로 10% 성장했고, 농심은 2030년 미국 연매출 15억 달러를 목표로 제시했다. ([Financial Times][2])

### 실제 가격경로 검증

```text
price_data_source:
FT business evidence

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- FT는 농심 주가 anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

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

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = global_staple_brand_watch
stage_failure_type = stage2_watch_success
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
- U.S. beauty-tech demand

Stage 2:
2025-07~10
- APR stock surged after IPO
- market value around $4B~$6B
- device + skincare hybrid brand validation

Stage 3:
2025 Q4 후보
- Q4 revenue 약 $440M, +124% YoY
- overseas revenue 약 $362M, +203% YoY
- FY 2025 revenue 약 $1.2B
- Medicube revenue 약 $1.1B
- Ulta 1,400+ store expansion
- TikTok Shop / Amazon sales conversion

Stage 4B:
2025~2026
- stock up more than fourfold since January per FT
- market value around $6B
- single-brand/device concentration
```

APR/Medicube는 R5에서 가장 강한 structural_success 후보 중 하나다. Vogue Business는 APR의 2025년 4분기 매출이 약 4.4억 달러로 전년 대비 124% 증가했고, 해외 매출은 203% 증가한 약 3.62억 달러라고 보도했다. FY 2025 매출은 약 12억 달러, Medicube 매출은 약 11억 달러로 전체의 대부분을 차지한다. FT는 APR 주가가 2025년 1월 이후 4배 이상 올랐고 시가총액이 약 60억 달러에 도달했다고 보도했다. 따라서 Stage 3 후보이면서 동시에 4B-watch다. ([Vogue][3])

### 실제 가격경로 검증

```text
price_data_source:
Vogue Business / FT reported revenue and market-value anchors

stage3_price:
price_data_unavailable_after_deep_search

Q4_2025_revenue:
$440M

Q4_2025_revenue_growth:
+124% YoY

Q4_2025_overseas_revenue:
$362M

Q4_2025_overseas_growth:
+203% YoY

FY_2025_revenue:
$1.2B

Medicube_FY_2025_revenue:
$1.1B

Medicube_share_of_APR_revenue:
1.1 / 1.2
= 91.7%

Ulta_store_expansion:
1,400+ stores

TikTok_Shop_revenue:
$102.9M+

reported_MFE_since_January:
> +300%

market_value_context:
about $6B

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- 4배 이상 상승과 $6B valuation은 4B-watch 필요.
```

### alignment

```text
score_price_alignment = aligned
rerating_result = K_beauty_device_true_rerating_plus_4B_watch
stage_failure_type = green_success_candidate
```

---

## Case D — d’Alba / Silicon2 / Cosmax / Kolmar `success_candidate + event premium`

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
- ODMs Cosmax / Kolmar support high-margin outsource model
- Silicon2 CEO says physical-store sales needed for long-term success

Stage 3:
없음
- retail talks / e-commerce virality만으로 Green 금지
- sell-through, repeat order, OPM, inventory/receivables 확인 필요

Stage 4B:
2025-06-05
- d’Alba shares more than doubled since debut last month

Stage 4C:
retail sell-through failure, U.S. tariff squeeze, inventory build, brand plateau, China decline 시 후보
```

K-beauty indie basket은 Stage 2 후보지만 Green은 아니다. Reuters는 Tirtir, d’Alba, Torriden, Beauty of Joseon 등이 Ulta, Sephora, Target, Costco 등과 미국 오프라인 입점을 논의하고 있다고 보도했다. 한국은 2024년 미국 최대 화장품 수출국이 됐고, U.S. e-commerce 상위 5개 K-beauty 브랜드는 2년간 평균 71% 성장해 전체 미국 시장 성장률 21%를 크게 웃돌았다. 다만 Reuters는 많은 브랜드가 Cosmax·Kolmar 같은 ODM에 의존한다고 설명했고, Silicon2 CEO는 장기 성공에는 physical-store sell-through가 필요하다고 말했다. d’Alba는 상장 후 한 달 만에 2배 이상 상승해 4B/event premium도 같이 붙는다. ([Reuters][4])

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
- Reuters는 Silicon2 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = price_moved_without_evidence_for_dAlba / success_candidate_for_ODM_distribution
rerating_result = K_beauty_indie_retail_watch
stage_failure_type = stage2_evidence_not_green
```

---

## Case E — CJ / Olive Young `success_candidate / K-beauty retail platform`

```text
symbols = CJ Corp / CJ Olive Young exposure
case_type = success_candidate
archetype = K_BEAUTY_RETAIL_PLATFORM
```

### stage date

```text
Stage 1:
2024~2025
- Olive Young as K-beauty curation platform
- U.S. K-beauty expansion
- inbound tourist beauty retail

Stage 2:
2025~2026
- Olive Young first U.S. store plan
- U.S. K-beauty market reaches $2B by July 2025
- K-beauty category +37% YoY
- Olive Young operates 1,300+ stores in Korea

Stage 3:
없음
- CJ listed vehicle로 연결되는 이익, store economics, OPM, IPO/valuation monetization 확인 전 Green 금지

Stage 4B:
Olive Young IPO/미국진출 기대만으로 CJ 계열주가 먼저 rerating되면 후보

Stage 4C:
U.S. retail sell-through failure, tariff squeeze, inventory build, brand saturation, IPO delay 시 후보
```

Olive Young은 K-beauty retail platform 후보지만, 상장된 CJ vehicle의 Stage 3로 바로 이어지지는 않는다. Business Insider는 미국 K-beauty 시장이 2025년 7월까지 1년간 20억 달러 규모로 37% 성장했고, Olive Young이 2026년 미국 첫 매장을 준비하고 있다고 보도했다. Olive Young은 한국 내 1,300개 이상 매장을 보유한 K-beauty specialist retailer로 정리된다. ([Business Insider][5])

### 실제 가격경로 검증

```text
price_data_source:
Business Insider / Reuters platform evidence

stage3_price:
N/A

CJ_or_CJ_OliveYoung_price:
price_data_unavailable_after_deep_search
- Reuters/BI는 CJ Corp 주가 reaction anchor를 제공하지 않음.
- CJ Olive Young은 직접 상장사가 아님.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

U.S._K_beauty_market_size_to_July_2025:
$2B

U.S._K_beauty_market_growth:
+37% YoY

Olive_Young_Korea_stores:
1,300+

U.S._store_timing:
2026 planned

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = K_beauty_retail_platform_watch
stage_failure_type = stage2_watch_success
```

---

## Case F — 아모레퍼시픽 / legacy K-beauty `failed_rerating / China exposure watch`

```text
symbol = 090430
case_type = failed_rerating / 4C-watch
archetype = LEGACY_BEAUTY_CHINA_EXPOSURE_4C
```

### stage date

```text
Stage 1:
2023~2025
- K-beauty global revival
- COSRX / Laneige / Sulwhasoo U.S. transition 기대
- North America / EMEA growth attempt

Stage 2:
보류
- U.S. growth와 China decline offset 확인 필요

Stage 3:
없음
- K-beauty macro tailwind만으로 Green 금지

Stage 4C-watch:
2024~2025
- China beauty demand weakness
- luxury/premium beauty slowdown
- local Chinese brand competition
- duty-free weakness / daigou pressure
```

아모레퍼시픽은 R5에서 “K-beauty macro”와 “legacy company execution”을 분리해야 하는 케이스다. Vogue는 아모레퍼시픽이 China decline과 duty-free weakness를 겪으면서 North America와 EMEA로 방향을 돌리고 있다고 정리했다. Reuters도 L’Oréal의 2024년 3분기 North Asia 매출이 6.5% 감소했고, 중국 소비 약화가 global beauty sector 전반에 압력을 줬다고 보도했다. 즉 K-beauty가 강해도 legacy China exposure가 크면 Green을 막아야 한다. ([Vogue][6])

### 실제 가격경로 검증

```text
price_data_source:
Vogue AmorePacific strategic context + Reuters global beauty China-demand evidence

stage3_price:
N/A

AmorePacific_stock_OHLC:
price_data_unavailable_after_deep_search
- 이번 pass에서 AmorePacific event-day price anchor를 직접 확인하지 못함.
- Reuters/FT/MarketWatch에서 회사별 OHLC anchor 확보 실패.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

legacy_risk_factors:
China demand weakness
duty-free weakness
local Chinese brand competition
premium beauty slowdown

L'Oreal_Q3_2024_like_for_like_growth:
+3.4%, below expected +6%

L'Oreal_North_Asia_sales:
-6.5%

L'Oreal_share_decline_since_June:
about -20%

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = thesis_break_watch / insufficient_price_data
rerating_result = legacy_K_beauty_China_exposure_break
stage_failure_type = should_have_been_yellow_or_red
```

---

## Case G — 호텔신라 / 현대백화점 / 파라다이스 / 한국화장품 `tourism retail event premium`

```text
symbols = 008770 / 069960 / 034230 / 123690
case_type = event_premium / success_candidate
archetype = TOURISM_RETAIL_DUTYFREE_EVENT
```

### stage date

```text
Stage 1:
2025-03~08
- 중국 단체관광객 무비자 정책 발표
- tourist retail / beauty / duty-free recovery 기대

Stage 2:
2025-08-06
- visa-free entry from 2025-09-29 to June 2026
- Hyundai Department Store +7.1%
- Hotel Shilla +4.8%
- Paradise +2.9%
- Hankook Cosmetics +9.9%

추가 Stage 2:
2025-09-29
- visa-free programme starts
- Chinese groups of 3+ can stay 15 days
- Shilla Duty Free organizes Chinese cruise tour
- Baedal Minjok introduces Alipay / WeChat Pay options

Stage 3:
없음
- 관광객 수 증가만으로 Green 금지
- 객단가, 면세 매출, beauty sell-through, casino drop/hold, OPM 확인 필요

Stage 4B:
정책 발표일 동반 급등

Stage 4C:
tourist spend 부진, anti-Chinese rallies, low-price tour mix, duty-free margin weakness 시 후보
```

관광·면세·백화점 basket은 Stage 2 event candidate다. Reuters는 중국 단체관광객 무비자 정책 발표 후 현대백화점 +7.1%, 호텔신라 +4.8%, 파라다이스 +2.9%, 한국화장품 +9.9%가 상승했다고 보도했다. 이후 실제 시행 시점에는 3명 이상 중국 단체관광객이 15일간 무비자로 체류할 수 있게 됐고, Shilla Duty Free가 중국 cruise tour를 조직하는 등 수요 capture 시도가 나왔다. 하지만 Green은 tourist arrivals가 아니라 **tourist spend, duty-free sales, casino drop/hold, OPM**이다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters event return and tourism metric anchors

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

2024_visitors:
16.4M

visitor_growth_2024:
+48%

Chinese_share:
28%

2025_visitor_target:
18.5M

target_growth_vs_2024:
18.5 / 16.4 - 1
= +12.8%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = event_premium / success_candidate
rerating_result = tourism_retail_recovery_watch
stage_failure_type = stage2_watch_success_not_green
```

---

## Case H — F&F / TaylorMade `event_premium / M&A optionality`

```text
symbol = 383220
case_type = event_premium / M&A_watch
archetype = APPAREL_M_AND_A_OPTIONALITY
```

### stage date

```text
Stage 1:
2025-07-21
- TaylorMade acquisition optionality
- ROFR / consent-right dispute
- golf equipment brand exposure

Stage 2:
약한 Stage 2
- Goldman Sachs advisor
- possible TaylorMade value around $3.5B
- F&F invested 358B won in 2021 subordinated equity
- confirmed acquisition 없음

Stage 3:
없음
- M&A optionality만으로 Green 금지
- confirmed transaction, financing, EPS accretion, integration plan 필요

Stage 4B:
거래 기대만으로 주가가 급등하면 event premium

Stage 4C:
거래 무산, 법적 분쟁, 투자손상, 본업 브랜드 부진 시 후보
```

F&F는 TaylorMade optionality 때문에 R5 브랜드/M&A 후보로 볼 수 있지만, 아직 Green은 아니다. Reuters는 F&F가 TaylorMade 인수를 위해 Goldman Sachs를 자문사로 선임했고, TaylorMade 매각가가 약 35억 달러에 이를 수 있다고 보도했다. F&F는 2021년 TaylorMade 인수 당시 후순위 지분 3,580억 원을 투자했고, ROFR·consent rights를 주장하고 있다. 하지만 확정 거래, financing, EPS accretion, integration plan이 확인되기 전에는 M&A optionality event다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters deal evidence anchor

stage3_price:
N/A

F&F_stock_price:
price_data_unavailable_after_deep_search
- Reuters는 F&F 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

reported_TaylorMade_possible_value:
$3.5B

F&F_2021_subordinated_equity_investment:
358B won

FX_rate_reported:
1,387.39 won per USD

KRW_equivalent_of_$3.5B:
3.5B * 1,387.39
= 약 4.856T won

F&F_investment_vs_possible_TaylorMade_value:
358B / 4.856T
= 약 7.4%

total_subordinated_equity_investment:
619.2B won

F&F_share_of_subordinated_equity:
358 / 619.2
= 57.8%

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = M&A_optionality_watch
stage_failure_type = should_have_been_stage1_or_stage2_only
```

---

# 5. 이번 R5 case별 요약표

| case                          | 분류                            |                                                         실제 가격검증 | alignment          |
| ----------------------------- | ----------------------------- | --------------------------------------------------------------: | ------------------ |
| 삼양식품                          | structural_success + 4C-watch |  647,000원, +5.7%; target upside +28.3%; Denmark recall/reversal | aligned_partial    |
| 농심                            | success_candidate             |           Shin Ramyun $883M, 해외 nearly 60%, U.S. target +178.8% | success_candidate  |
| APR / Medicube                | structural_success + 4B       |                      Q4 revenue +124%, overseas +203%, 주가 4배 이상 | aligned + 4B       |
| d’Alba / Silicon2 / ODM       | overheat + Stage 2            |           d’Alba debut 후 >2배; top5 K-beauty U.S. ecommerce +71% | event_premium      |
| CJ / Olive Young              | success_candidate             |              U.S. K-beauty $2B, +37%; Olive Young 1,300+ stores | stage2_watch       |
| AmorePacific                  | failed_rerating / China watch | China/duty-free weakness; L’Oréal North Asia -6.5% read-through | thesis_break_watch |
| Hotel Shilla / tourism basket | event_premium                 |                 Shilla +4.8%, Hyundai Dept +7.1%, Hankook +9.9% | event_premium      |
| F&F / TaylorMade              | event_premium                 |              possible $3.5B deal, F&F 358B won prior investment | M&A optionality    |

---

# 6. score-price alignment 판정

```text
aligned / structural_success_candidate:
- 삼양식품
- APR / Medicube

success_candidate:
- 농심
- CJ / Olive Young
- Silicon2 / Cosmax / Kolmar ODM-distribution basket

event_premium:
- d’Alba IPO/post-debut rally
- Hotel Shilla / Hyundai Department Store / Hankook Cosmetics tourism retail event
- F&F TaylorMade M&A optionality

price_moved_without_evidence:
- d’Alba retail-talks + post-debut rally
- 관광정책 발표일 retail/beauty basket
- F&F M&A optionality if price moved before signed deal

thesis_break_watch:
- AmorePacific legacy China exposure
- Samyang local-regulatory recall watch

4B-watch:
- APR 4배 이상 상승
- d’Alba debut 후 2배 이상
- tourism retail policy-day rally
- Samyang single-SKU Buldak valuation expansion
- F&F M&A optionality without confirmed transaction

hard_4C_confirmed:
- false
```

---

# 7. 점수비중 교정

## 올릴 축

```text
repeat_demand +5
export_growth +5
ASP_uplift +4
channel_sell_through +5
overseas_sales_mix +5
U.S._sales_mix +4
OPM_improvement +5
inventory_quality +4
receivables_quality +4
physical_store_sellthrough +5
brand_extension_success +3
```

### 왜 올리나

삼양식품은 수출·ASP·OP revision이 한 번에 확인됐고, APR은 해외 매출과 미국 채널이 실제 매출로 이어지며 대형 price path가 확인됐다. 농심은 Shin Ramyun이 global staple 구조를 갖고 있어, 일회성 viral보다 더 안정적인 R5 Stage 2 후보가 된다.

## 내릴 축

```text
viral_product_only -5
brand_heat_only -5
retail_talks_without_sell_through -5
IPO_or_debut_rally -5
influencer_endorsement_only -4
single_SKU_dependence -4
China_exposure_without_offset -5
M&A_optionality_without_EPS -5
tariff_margin_uncertainty -3
local_regulatory_recall -4
inventory_or_receivables_build -5
```

### 왜 내리나

d’Alba는 입점 논의와 상장 후 급등이 있었지만 sell-through evidence가 부족하다. AmorePacific은 K-beauty macro가 좋아도 China exposure와 legacy premium beauty weakness가 있으면 Green이 막혀야 한다. F&F는 TaylorMade optionality가 있어도 확정 거래와 EPS accretion 전에는 Stage 3가 아니다.

## Green gate 강화 조건

```text
R5 Stage 3-Green 필수:
1. 반복구매 / 반복수요 확인
2. 해외 매출 비중 증가
3. channel sell-through 확인
4. ASP 또는 product mix 개선
5. OPM 개선
6. 재고·매출채권 안정
7. tariff / recall / regulation 통과
8. single-SKU / single-device risk 관리
9. 가격경로가 evidence 이후 따라옴

금지:
viral TikTok만 있음
입점 논의만 있음
IPO/debut rally만 있음
인플루언서 endorsement만 있음
M&A optionality만 있음
China decline offset 없음
single product story만 있음
```

## 4B 조기감지 조건

```text
4B-watch:
Stage 3 이후 2~4배 이상 상승
IPO/debut 후 1개월 내 2배 이상 상승
single SKU / single device 의존도 높음
미국 입점 기대가 sell-through보다 먼저 가격에 반영
관광정책 발표일 retail/beauty basket 동반 급등
해외 매출은 좋지만 OPM 개선이 둔화
M&A optionality가 signed transaction보다 먼저 가격화

4B-elevated:
경쟁 제품 대거 출시
U.S. tariff 비용을 가격에 전가하지 못함
채널 확장 후 재고 증가
매출채권 증가
브랜드 성장률 normalize
regulatory recall 확대
```

## 4C hard gate 조건

```text
food safety recall 확산
regulatory ban
channel stuffing
inventory build
receivables spike
single product fad collapse
U.S. tariff margin squeeze
retail channel sell-through failure
China sales collapse not offset by U.S./Europe
M&A event failure / impairment
brand acquisition impairment
```

이번 R5 Loop 10에서 hard 4C는 확정하지 않는다. Samyang Denmark recall은 부분 해제됐으므로 `regulatory_4C_watch`, AmorePacific China exposure는 `thesis_break_watch`, d’Alba/F&F/tourism retail은 `event_premium`으로 둔다.

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

## docs/round/round_163.md 요약

```md
# R5 Loop 10. Consumer / Retail / Brand Price Validation

이번 라운드는 R5 Loop 10 price-validation 라운드다.

핵심 결론:
- Samyang Foods는 Buldak export, ASP uplift, OP revision이 같이 확인되어 Stage 3 후보가 된다. 647,000원 close, +5.7%, target upside +28.3% anchor가 있다. Denmark recall/reversal은 local-regulatory 4C-watch로 기록한다.
- Nongshim은 Shin Ramyun global staple 구조가 강하다. Shin 2023 sales $883M, overseas share nearly 60%, U.S. target $1.5B by 2030이다. OPM/EPS/channel sell-through 전 Green 보류다.
- APR/Medicube는 R5 structural success benchmark다. Q4 2025 revenue +124%, overseas revenue +203%, FY revenue about $1.2B, Medicube about $1.1B. 주가 4배 이상 상승과 single-brand/device concentration 때문에 4B-watch가 필요하다.
- d’Alba/Silicon2/Cosmax/Kolmar K-beauty basket은 U.S. retail talks와 e-commerce growth가 강하지만, sell-through 전 Stage 3 금지다. d’Alba debut 후 >2배는 event premium이다.
- CJ/Olive Young은 K-beauty retail platform Stage 2 후보지만, direct listed earnings bridge와 store economics 전 Green 금지다.
- AmorePacific은 K-beauty macro와 company-level performance를 분리해야 한다. China exposure와 duty-free weakness는 4C-watch다.
- Hotel Shilla / Hyundai Department Store / Paradise / Hankook Cosmetics are China-tourism event candidates. Policy-day returns were +4.8% / +7.1% / +2.9% / +9.9%, but tourist spend and OPM are required before Green.
- F&F TaylorMade optionality is M&A event premium. Possible $3.5B valuation and F&F’s 358B won investment are meaningful, but signed transaction, financing and EPS accretion are required before Green.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 163 R5 Loop 10 Consumer Retail Brand Price Validation

## 반영 내용
- R5 Loop 10 price-validation 라운드를 추가했다.
- K-food export, global staple ramen, K-beauty device, indie K-beauty ODM/distribution, K-beauty retail platform, legacy China exposure, tourism retail event, apparel M&A optionality를 비교했다.
- Reuters/FT/MarketWatch/Business Insider/Vogue/AP reported anchors로 가능한 MFE/MAE 및 business metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- repeat demand, export growth, ASP, channel sell-through, overseas mix, OPM, physical-store sell-through 가중치 강화
- viral product, IPO/debut rally, retail talks without sell-through, China exposure without offset, M&A optionality 감점 강화
- R5 4B-watch와 regulatory/channel 4C-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r5_loop10_samyang_buldak_export_regulatory_watch","symbol":"003230","company_name":"Samyang Foods","case_type":"structural_success_candidate","primary_archetype":"K_FOOD_EXPORT_RECURRING","stage2_date":"2024-06-14","stage3_date":"2024-06-14_candidate","stage4c_date":"2024-06-12","price_validation":{"price_data_source":"MarketWatch/AP/Reuters reported anchors","stage3_price":647000,"event_mfe_1d_pct":5.7,"implied_prior_close":611921,"target_price":830000,"target_upside_pct":28.3,"op_estimate_q2_krw_bn":81.2,"op_growth_estimate_pct":84,"denmark_recall_status":"2024-06 recall; 2024-08 partial reversal","price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned_partial","rerating_result":"K_food_export_rerating_candidate","notes":"Export/ASP/OP revision supports Stage 3 candidate; Denmark recall is regulatory 4C-watch, not hard 4C after partial reversal."}
{"case_id":"r5_loop10_nongshim_shin_global_staple","symbol":"004370","company_name":"Nongshim","case_type":"success_candidate","primary_archetype":"K_FOOD_GLOBAL_STAPLE_BRAND","stage2_date":"2024-05-27","price_validation":{"price_data_source":"FT business evidence","stage3_price":null,"shin_2023_sales_krw_trn":1.2,"shin_2023_sales_usd_mn":883,"overseas_sales_share_pct":60,"north_america_sales_2023_usd_mn":538,"north_america_growth_pct":10,"us_sales_target_2030_usd_bn":1.5,"target_growth_from_2023_na_sales_pct":178.8,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"global_staple_brand_watch","notes":"Global staple and overseas expansion are Stage 2; OPM/EPS and channel sell-through required for Green."}
{"case_id":"r5_loop10_apr_medicube_structural_4b","symbol":"278470","company_name":"APR / Medicube","case_type":"structural_success","primary_archetype":"K_BEAUTY_DEVICE_GLOBAL_BRAND","stage2_date":"2025-2026","stage3_date":"2025-Q4_candidate","stage4b_date":"2025-2026","price_validation":{"price_data_source":"Vogue Business/FT revenue and market-value anchors","stage3_price":null,"q4_2025_revenue_usd_mn":440,"q4_2025_revenue_growth_pct":124,"q4_2025_overseas_revenue_usd_mn":362,"q4_2025_overseas_growth_pct":203,"fy_2025_revenue_usd_bn":1.2,"medicube_fy_2025_revenue_usd_bn":1.1,"medicube_revenue_share_pct":91.7,"ulta_store_expansion_count":1400,"tiktok_shop_revenue_usd_mn":102.9,"reported_mfe_since_january_pct":300,"market_value_context_usd_bn":6,"price_validation_status":"reported_revenue_marketcap_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"K_beauty_device_true_rerating_plus_4B_watch","notes":"Revenue conversion supports structural success, but single-brand/device concentration and fourfold rally require 4B-watch."}
{"case_id":"r5_loop10_indie_kbeauty_odm_distribution_watch","symbol":"483650/257720/192820/161890","company_name":"d'Alba / Silicon2 / Cosmax / Kolmar basket","case_type":"overheat","primary_archetype":"K_BEAUTY_INDIE_BRAND_US_CHANNEL","stage2_date":"2025-06-05","stage4b_date":"2025-06-05","price_validation":{"price_data_source":"Reuters business and reported return anchors","stage3_price":null,"dalba_reported_mfe_since_debut_pct":100,"top5_korean_cosmetics_us_ecommerce_growth_pct":71,"overall_us_market_growth_pct":21,"relative_growth_vs_us_market_multiple":3.38,"retail_talks":["Ulta","Sephora","Target","Costco"],"odm_model":["Cosmax","Kolmar"],"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence_for_dalba_success_candidate_for_odm_distribution","rerating_result":"K_beauty_indie_retail_watch","notes":"Retail talks and ecommerce growth are Stage 2; sell-through, repeat orders, OPM and working-capital quality required before Green."}
{"case_id":"r5_loop10_cj_olive_young_retail_platform","symbol":"001040/CJ_OliveYoung_exposure","company_name":"CJ / Olive Young","case_type":"success_candidate","primary_archetype":"K_BEAUTY_RETAIL_PLATFORM","stage2_date":"2025-2026","price_validation":{"price_data_source":"Business Insider platform evidence","stage3_price":null,"us_kbeauty_market_size_usd_bn":2.0,"us_kbeauty_market_growth_pct":37,"olive_young_korea_stores":1300,"us_store_timing":"2026 planned","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"K_beauty_retail_platform_watch","notes":"Olive Young is Stage 2 platform exposure; direct listed earnings bridge, store economics and OPM required for Green."}
{"case_id":"r5_loop10_amorepacific_legacy_china_exposure","symbol":"090430","company_name":"AmorePacific","case_type":"failed_rerating","primary_archetype":"LEGACY_BEAUTY_CHINA_EXPOSURE_4C","stage4c_date":"2024-2025_watch","price_validation":{"price_data_source":"Vogue AmorePacific context + Reuters global beauty China-demand evidence","stage3_price":null,"legacy_risk_factors":["China demand weakness","duty-free weakness","local Chinese brand competition","premium beauty slowdown"],"loreal_q3_2024_like_for_like_growth_pct":3.4,"loreal_expected_growth_pct":6.0,"loreal_north_asia_sales_pct":-6.5,"loreal_share_decline_since_june_pct":-20,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch_insufficient_price_data","rerating_result":"legacy_K_beauty_China_exposure_break","notes":"K-beauty macro is not enough; China/duty-free weakness and premium beauty slowdown block Green until U.S./Europe offset is proven."}
{"case_id":"r5_loop10_tourism_retail_china_visa_event","symbol":"008770/069960/034230/123690","company_name":"Hotel Shilla / Hyundai Department Store / Paradise / Hankook Cosmetics","case_type":"event_premium","primary_archetype":"TOURISM_RETAIL_DUTYFREE_EVENT","stage2_date":"2025-08-06/2025-09-29","stage4b_date":"2025-08-06","price_validation":{"price_data_source":"Reuters event return and tourism metrics","stage3_price":null,"hyundai_department_event_mfe_1d_pct":7.1,"hotel_shilla_event_mfe_1d_pct":4.8,"paradise_event_mfe_1d_pct":2.9,"hankook_cosmetics_event_mfe_1d_pct":9.9,"visa_free_period":"2025-09-29_to_2026-06","visa_free_stay_days":15,"group_condition":"3+ Chinese tourists","visitors_2024_mn":16.4,"visitor_growth_2024_pct":48,"chinese_share_pct":28,"target_visitors_2025_mn":18.5,"target_growth_vs_2024_pct":12.8,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"tourism_retail_recovery_watch","notes":"Visa-free tourist policy is Stage 2/event; tourist spend, sell-through, duty-free sales and OPM required before Green."}
{"case_id":"r5_loop10_fnf_taylormade_mna_optionality","symbol":"383220","company_name":"F&F","case_type":"event_premium","primary_archetype":"APPAREL_M_AND_A_OPTIONALITY","stage1_date":"2025-07-21","price_validation":{"price_data_source":"Reuters deal evidence anchor","stage3_price":null,"reported_taylormade_value_usd_bn":3.5,"ff_2021_subordinated_equity_investment_krw_bn":358,"fx_rate_reported":1387.39,"krw_equiv_value_krw_trn":4.856,"ff_investment_vs_possible_value_pct":7.4,"total_subordinated_equity_investment_krw_bn":619.2,"ff_share_of_subordinated_equity_pct":57.8,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium","rerating_result":"M&A_optionality_watch","notes":"TaylorMade optionality is Stage 1/2 event; confirmed transaction, financing and EPS accretion required for Green."}
```

## shadow weight row 초안

```csv
archetype,repeat_demand,export_growth,asp,channel_sellthrough,overseas_mix,opm,inventory_quality,receivables_quality,event_penalty,regulatory_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
K_FOOD_EXPORT_RECURRING,+5,+5,+4,+4,+5,+5,+4,+4,-2,+4,+4,+3,Samyang export/ASP/OP revision supports Stage 3 candidate but recall/regulatory watch remains.
K_FOOD_GLOBAL_STAPLE_BRAND,+5,+5,+3,+5,+5,+4,+4,+4,-1,+2,+3,+3,Nongshim global staple is Stage 2 until OPM/EPS/sell-through confirm.
K_BEAUTY_DEVICE_GLOBAL_BRAND,+5,+5,+3,+5,+5,+5,+3,+3,-2,+2,+5,+3,APR is structural success but fourfold rally and concentration require 4B-watch.
K_BEAUTY_INDIE_BRAND_US_CHANNEL,+3,+5,+2,+5,+5,+4,+4,+4,-5,+3,+5,+4,d'Alba/indie K-beauty retail talks require sell-through before Green.
K_BEAUTY_ODM_DISTRIBUTOR_LEVERAGE,+3,+5,+2,+5,+5,+4,+5,+5,-3,+2,+4,+4,Cosmax/Kolmar/Silicon2 benefit only if brand sell-through and working capital hold.
K_BEAUTY_RETAIL_PLATFORM,+5,+4,+2,+5,+4,+5,+4,+4,-3,+3,+4,+3,Olive Young platform needs listed earnings bridge and U.S. store economics.
LEGACY_BEAUTY_CHINA_EXPOSURE_4C,+2,+3,+2,+3,+3,+4,+5,+5,-2,+4,+4,+5,Amore legacy China exposure blocks macro K-beauty Green until offset is proven.
TOURISM_RETAIL_DUTYFREE_EVENT,+2,+3,+2,+5,+3,+4,+4,+3,-5,+2,+5,+4,Tourism retail event needs spend/sell-through/OPM, not just visitor policy.
APPAREL_M_AND_A_OPTIONALITY,+1,+1,+1,+1,+1,+3,+2,+2,-5,+2,+5,+3,F&F TaylorMade optionality is not Green until confirmed deal and EPS accretion.
```

---

# 이번 R5 Loop 10 결론

R5는 Stage 3 후보가 분명 있지만, **viral·입점 논의·관광정책·M&A optionality를 너무 쉽게 Green으로 올리면 false positive가 빠르게 쌓이는 섹터**다.

```text
1. Samyang Foods는 수출 + ASP + OP revision이 같이 확인되어 Stage 3 후보가 될 수 있다.
   하지만 Denmark recall 같은 local-regulatory watch를 같이 붙여야 한다.

2. Nongshim은 Shin Ramyun global staple 구조가 좋다.
   그러나 OPM/EPS revision과 sell-through 확인 전 Stage 3는 보류다.

3. APR/Medicube는 R5의 가장 강한 structural success 후보 중 하나다.
   하지만 4배 이상 상승, single-brand/device concentration 때문에 4B-watch를 요구한다.

4. d’Alba / Silicon2 / Cosmax / Kolmar K-beauty basket은 U.S. e-commerce와 retail talks가 강하지만,
   physical store sell-through 전 Stage 3 금지다.

5. CJ / Olive Young은 좋은 K-beauty retail platform 후보지만,
   direct listed earnings bridge와 U.S. store economics 전 Green 금지다.

6. AmorePacific은 K-beauty macro tailwind와 회사 실적을 분리해야 한다.
   China exposure와 legacy premium beauty weakness는 4C-watch다.

7. Hotel Shilla / Hyundai Department / Paradise / Hankook Cosmetics는 중국 무비자 정책 이벤트로 올랐지만,
   tourist spend와 OPM 전에는 event premium이다.

8. F&F TaylorMade는 M&A optionality이지 브랜드 Stage 3가 아니다.
```

한 문장으로 압축하면:

> **R5에서 진짜 Stage 3는 “K-food·K-beauty·브랜드가 핫하다”가 아니라, 반복구매·해외 채널 sell-through·ASP·OPM·재고/채권 품질이 실제 이익 체급 변화로 내려오는 순간이다.**
> **R5는 viral·IPO/debut rally·입점 논의·관광정책·M&A optionality를 먼저 4B/Event Premium으로 분리해야 점수표가 산다.**

[1]: https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045?utm_source=chatgpt.com "Samyang Foods Set to Post Strong 2Q Earnings -- Market Talk"
[2]: https://www.ft.com/content/4218f2b8-5498-411b-81fe-e3c836868d64?utm_source=chatgpt.com "Maker of Shin instant ramen expands overseas as Korean noodles become hit"
[3]: https://www.vogue.com/article/how-k-beauty-brand-medicube-pulled-off-its-global-breakout?utm_source=chatgpt.com "How K-Beauty Brand Medicube Pulled Off Its Global Breakout"
[4]: https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/?utm_source=chatgpt.com "Korean beauty startups bet booming US demand outlasts tariff pain"
[5]: https://www.businessinsider.com/korean-beauty-brands-exclusive-sephora-ulta-olive-young-2025-10?utm_source=chatgpt.com "A K-beauty turf war is brewing in the US"
[6]: https://www.vogue.com/article/beyond-k-beauty-inside-amorepacifics-fight-for-global-dominance?utm_source=chatgpt.com "Beyond K-beauty: Inside Amorepacific's fight for global dominance"
[7]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/?utm_source=chatgpt.com "South Korea to offer visa-free entry to Chinese tourists from late September"
[8]: https://www.reuters.com/world/asia-pacific/s-korean-fashion-retailer-ff-hires-goldman-taylormade-acquisition-2025-07-21/?utm_source=chatgpt.com "S. Korean fashion retailer F&F hires Goldman for TaylorMade acquisition"
