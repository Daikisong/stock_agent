순서상 이번은 **R5 Loop 9 — 소비재·유통·브랜드 가격경로 검증 라운드**다.

이번 라운드는 지난 R5의 삼양·APR만 반복하지 않고, **K-food 대형 브랜드, K-beauty 디바이스/인디/유통 플랫폼, legacy K-beauty China risk, 관광·면세·백화점 event premium, 의류 M&A optionality**를 같이 본다.

```text
round = R5 Loop 9
round_id = round_150
large_sector = CONSUMER_RETAIL_BRAND
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
```

원시 수정주가 일봉 OHLC는 이번 환경에서 안정적으로 직접 확보하지 못했다. 대신 Reuters / FT / MarketWatch / Business Insider / Vogue / AP에 남은 **가격 anchor, 이벤트 수익률, 매출·수출·시장규모·거래금액 지표**로 계산 가능한 값만 계산했다.

---

# 1. 이번 라운드 대섹터

```text
R5 = 소비재·유통·브랜드
```

R5의 핵심은 “K-food/K-beauty가 핫하다”가 아니라, **반복구매·해외 채널 sell-through·ASP·OPM·재고/채권 품질·FCF가 확인되는가**다.

---

# 2. 대상 canonical archetype

```text
K_FOOD_EXPORT_RECURRING
K_FOOD_GLOBAL_STAPLE_BRAND
K_FOOD_SINGLE_SKU_REGULATORY_WATCH
K_BEAUTY_DEVICE_GLOBAL_BRAND
K_BEAUTY_INDIE_BRAND_US_CHANNEL
K_BEAUTY_RETAIL_PLATFORM
K_BEAUTY_DISTRIBUTOR_ODM_LEVERAGE
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
- Toomba Shin Ramyun product extension
- CJ Bibigo global capacity
- single-SKU risk
- food safety / local regulation

K-beauty:
- APR / Medicube beauty device
- d’Alba / Tirtir / Torriden / Beauty of Joseon U.S. retailer talks
- Silicon2 distribution
- Olive Young U.S. store
- Cosmax / Kolmar ODM leverage
- China decline vs U.S. sell-through
- tariff margin squeeze

Legacy beauty:
- AmorePacific / LG H&H / Shiseido read-through
- China consumer weakness
- local Chinese brand competition
- COSRX plateau
- duty-free weakness

Retail / tourism:
- Hyundai Department Store
- Hotel Shilla
- Hankook Cosmetics
- Chinese group visa-free event
- tourist arrivals vs tourist spend

Apparel / brand M&A:
- F&F / TaylorMade
- ROFR / legal dispute
- M&A optionality vs EPS accretion
```

---

# 4. 국장 신규 후보 case

## Case A — 삼양식품 `structural_success 후보 + regulatory 4C-watch`

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
- single SKU risk와 regulatory risk는 별도 RedTeam

Stage 4B:
Buldak valuation이 단일 제품 프리미엄으로 과도하게 확장된 구간

Stage 4C-watch:
2024-06-12
- Denmark recalls three spicy Buldak variants
- local regulation / child-safety concern

4C relief:
2024-08-08
- Denmark partly reverses ban for two variants
```

MarketWatch는 2024년 6월 14일 삼양식품이 불닭 수출 호조로 2분기 영업이익이 전년 대비 84% 증가한 812억 원을 기록할 수 있다고 보도했고, 미국·유럽 출하 증가와 ASP 상승, 생산능력 확대를 근거로 목표주가가 660,000원에서 830,000원으로 올라갔다. 당시 주가는 5.7% 오른 647,000원에 마감했다. ([마켓워치][1])

하지만 2024년 6월 덴마크는 고캡사이신 함량이 어린이·청소년·취약 성인에게 급성 중독 위험을 줄 수 있다며 Buldak 3종을 리콜했고, 8월에는 재검토 후 2개 품목의 금지를 해제했다. 이건 품질 문제라기보다 현지 규제·소비자 안전 이슈지만, R5에서는 `food_safety_regulatory_watch`로 붙여야 한다. ([AP News][2])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch stage2 price anchor + AP/Reuters regulatory event evidence

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

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = aligned_partial
rerating_result = K_food_export_rerating_candidate
stage_failure_type = green_success_candidate_with_regulatory_watch
```

---

## Case B — 농심 `success_candidate / global staple + product extension`

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

Stage 2:
2024-05-27
- Shin Ramyun 2023 sales 1.2조 원 / $883M
- nearly 60% overseas
- North America sales +10%, $538M
- U.S. annual sales target $1.5B by 2030

추가 Stage 2:
2025년
- Toomba Shin Ramyun launch extension
- 출시 3개월 1,700만 개 판매
- U.S. / China local production
- 60개국 이상 판매

Stage 3:
보류
- global staple 구조는 강하지만, OPM/EPS revision, channel sell-through, ASP 확인 필요

Stage 4B:
new flavor / K-food staple narrative가 가격에 먼저 반영되면 후보

Stage 4C:
China slowdown, U.S. competition, commodity cost, channel stuffing, local regulation 시 후보
```

FT는 농심 신라면이 2023년 1.2조 원, 약 8.83억 달러의 record sales를 기록했고, 그중 거의 60%가 해외에서 나왔다고 보도했다. 북미 매출은 2023년에 5.38억 달러로 10% 증가했고, 농심은 2030년 미국 연매출 15억 달러를 목표로 제시했다. ([Financial Times][3])

Toomba Shin Ramyun은 2024년 9월 출시 후 3개월 만에 1,700만 개가 팔렸고, 2024년 11월 미국 공장, 2025년 3월 중국 공장에서 생산이 시작됐다. 2025년에는 일본 초도 100만 개가 2주 만에 매진됐고, 미국 Walmart·Costco 등으로 확장되며 60개국 이상 판매로 정리된다. 다만 이 출처는 공개 요약 기반이라 `source_confidence = medium_low`로 둔다. ([위키백과][4])

### 실제 가격경로 검증

```text
price_data_source:
FT business evidence + public product-extension summary

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

Toomba_first_3_month_sales:
17M units

Nongshim_US_subsidiary_sales_forecast_2025:
669B won

U.S._subsidiary_growth_forecast:
+7.4%

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
- Kylie Jenner / Hailey Bieber / TikTok
- U.S. beauty-tech demand

Stage 2:
2025-07-08
- APR stock 158,300원
- IPO 이후 +75% 이상
- market cap 약 $4.2B

Stage 3:
2025-10~2026 후보
- 해외 매출비중, 미국 채널, Ulta distribution, TikTok Shop revenue 확인
- 2025 Q4 revenue +124%, overseas revenue +203%

Stage 4B:
2025-10-20 이후
- FT 기준 2025년 1월 이후 주가 4배 이상
- market value 약 $6B
- valuation crowding

Stage 4C:
tariff margin squeeze, device fad fade, competition, sell-through failure, influencer dependence 시 후보
```

Business Insider는 2025년 7월 APR이 158,300원에 거래됐고, 이는 IPO 이후 75% 이상 오른 수준이며 시가총액이 약 42억 달러라고 보도했다. FT는 2025년 10월 APR의 주가가 1월 이후 4배 이상 올랐고 시가총액이 약 60억 달러에 달했다고 정리했다. ([Business Insider][5])

Vogue Business는 APR의 2025년 4분기 매출이 약 4.4억 달러로 전년 대비 124% 증가했고, 해외 매출은 약 3.62억 달러로 203% 늘어 전체 매출의 87%를 차지했다고 보도했다. 2025년 전체 매출은 약 12억 달러, Medicube 매출은 약 11억 달러로 정리된다. ([Vogue][6])

### 실제 가격경로 검증

```text
price_data_source:
Business Insider / FT / Vogue Business reported anchors

stage2_price:
158,300원

implied_IPO_reference_price_from_75pct_gain:
158,300 / 1.75
= 약 90,457원 이하

IPO_to_stage2_MFE_minimum:
> +75%

market_cap_July:
$4.2B

market_cap_Oct:
$6.0B

market_cap_MFE_July_to_Oct:
6.0 / 4.2 - 1
= +42.9%

reported_MFE_since_January:
> +300%

Q4_2025_revenue:
$440M

Q4_2025_revenue_growth:
+124% YoY

Q4_2025_overseas_revenue:
$362M

Q4_2025_overseas_growth:
+203% YoY

Q4_2025_overseas_share:
362 / 440
= 82.3%
(기사상 약 87%로도 표현)

FY_2025_revenue:
$1.2B

Medicube_FY_2025_revenue:
$1.1B

Medicube_share_of_APR_revenue:
1.1 / 1.2
= 91.7%

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
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

## Case D — d’Alba / Silicon2 / indie K-beauty `overheat + distributor Stage 2`

```text
symbols = 483650 / 257720 / K-beauty indie basket
case_type = overheat + success_candidate
archetype = K_BEAUTY_INDIE_BRAND_US_CHANNEL / K_BEAUTY_DISTRIBUTOR_ODM_LEVERAGE
```

### stage date

```text
Stage 1:
2024~2025
- K-beauty U.S. e-commerce boom
- Tirtir / d’Alba / Torriden / Beauty of Joseon retail talks
- Silicon2 distributor leverage

Stage 2:
2025-06-05
- U.S. retailer talks with Ulta / Sephora / Target / Costco
- Korea becomes biggest cosmetics exporter to U.S. in 2024
- top 5 Korean cosmetics brands in U.S. e-commerce +71% over two years
- Silicon2 CEO says physical store sales needed for longer-term success

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

Reuters는 2025년 6월 K-beauty 스타트업들이 U.S. brick-and-mortar 진출을 추진하고 있으며 Tirtir, d’Alba, Torriden, Beauty of Joseon 등이 Ulta, Sephora, Target, Costco 등과 입점 협상을 하고 있다고 보도했다. 2024년 한국은 미국 내 최대 화장품 수출국이 됐고, 미국 e-commerce 상위 5개 한국 화장품 브랜드 매출은 2년 동안 평균 71% 성장했다. 하지만 Silicon2 CEO는 장기 성공에는 physical-store sell-through가 필요하다고 말했다. ([Reuters][7])

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

Stage 4B peak-before 여부:
success
- IPO 후 한 달 2배 이상은 4B/event premium.
```

### alignment

```text
score_price_alignment = price_moved_without_evidence_for_dAlba / success_candidate_for_distributor
rerating_result = K_beauty_indie_retail_watch
stage_failure_type = stage2_evidence_not_green
```

---

## Case E — CJ / Olive Young / K-beauty retail platform `success_candidate / not direct Green`

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

Business Insider는 2025년 10월 미국 K-beauty 시장이 2025년 7월까지 1년간 20억 달러 규모로 37% 성장했다고 보도했고, Olive Young이 2026년 미국 첫 매장을 준비하며 Sephora·Ulta가 K-beauty brand exclusivity를 선점하려는 경쟁이 벌어지고 있다고 정리했다. Olive Young은 한국 내 1,300개 이상 매장을 보유한 K-beauty specialist retailer로 묘사된다. ([Business Insider][8])

### 실제 가격경로 검증

```text
price_data_source:
Business Insider / Reuters / public company summary

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

## Case F — 아모레퍼시픽 / legacy K-beauty `failed_rerating / China exposure`

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

Stage 2:
보류
- U.S. 성장과 China decline offset 확인 필요

Stage 3:
없음
- K-beauty macro tailwind만으로 Green 금지

Stage 4B:
K-beauty macro만으로 legacy beauty주가 rerating되면 후보

Stage 4C-watch:
2024-08
- AmorePacific shares fell by about a quarter after Q2 miss
- worst market day since listing 14 years ago
- China demand / patriotic local-brand shift pressure
```

FT는 2024년 8월 중국 소비 둔화와 현지 브랜드 선호가 아시아 대형 beauty group을 압박하고 있으며, AmorePacific은 2분기 실적 미스로 상장 후 14년 만의 최악의 하루를 겪고 주가가 약 25% 하락했다고 보도했다. 같은 보도에서 Shiseido도 중국 수요 약화와 구조조정 비용으로 큰 폭 하락했고, 중국 소비자들의 local-brand preference가 구조적 압력으로 작용한다고 설명했다. ([Financial Times][9])

### 실제 가격경로 검증

```text
price_data_source:
FT reported event return anchor

stage3_price:
N/A

AmorePacific_event_MAE_1D:
about -25%

event_context:
Q2 earnings miss
China demand weakness
local Chinese brand competition
premium beauty pressure

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- China exposure / premium beauty slowdown은 RedTeam으로 사전 감지 가능.
```

### alignment

```text
score_price_alignment = thesis_break_watch / evidence_good_but_price_failed
rerating_result = legacy_K_beauty_China_exposure_break
stage_failure_type = should_have_been_yellow_or_red
```

---

## Case G — 현대백화점 / 호텔신라 / 한국화장품 `tourism retail event premium`

```text
symbols = 069960 / 008770 / 123690
case_type = event_premium / success_candidate
archetype = TOURISM_RETAIL_DUTYFREE_EVENT
```

### stage date

```text
Stage 1:
2025-03-20
- 중국 단체관광객 무비자 정책 발표
- tourist retail / beauty / duty-free recovery 기대

Stage 2:
2025-08-06
- visa-free entry from 2025-09-29 to June 2026
- Hyundai Department Store +7.1%
- Hotel Shilla +4.8%
- Hankook Cosmetics +9.9%

Stage 3:
없음
- 관광객 수 증가만으로 Green 금지
- 객단가, 면세 매출, beauty sell-through, OPM 확인 필요

Stage 4B:
2025-08-06
- 정책 발표일 동반 급등

Stage 4C:
tourist spend 부진, anti-Chinese rallies, low-price tour mix, duty-free margin weakness 시 후보
```

Reuters는 한국이 2025년 9월 29일부터 2026년 6월까지 중국 단체관광객에게 무비자 입국을 허용하기로 하자, 현대백화점이 7.1%, 호텔신라가 4.8%, 한국화장품이 9.9% 상승했다고 보도했다. 2024년 방한객은 1,640만 명으로 전년 대비 48% 증가했고, 중국인은 28%로 최대 비중을 차지했다. 2025년 정부 목표는 1,850만 명이다. ([Reuters][10])

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

Hankook_Cosmetics_event_MFE_1D:
+9.9%

Paradise_event_MFE_1D:
+2.9%

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

Stage 4B peak-before 여부:
success
- tourist spend / OPM 전 정책 발표일 급등은 4B/event premium.
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
case_type = event_premium / insufficient_evidence
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
없음 또는 약한 Stage 2
- confirmed acquisition 없음
- 본업 의류 실적 evidence 아님

Stage 3:
없음
- M&A optionality만으로 Green 금지
- confirmed transaction, financing, EPS accretion, integration plan 필요

Stage 4B:
거래 기대만으로 주가가 급등하면 event premium

Stage 4C:
거래 무산, 법적 분쟁, 투자손상, 본업 브랜드 부진 시 후보
```

Reuters는 F&F가 TaylorMade 인수를 위해 Goldman Sachs를 자문사로 선임했고, 기존 소유자인 Centroid가 별도 매각 절차를 진행할 경우 법적 조치를 취하겠다고 밝혔다고 보도했다. F&F는 2021년 TaylorMade 인수 때 3,580억 원을 후순위 지분으로 투자했고, 거래가 성사될 경우 TaylorMade의 가치는 약 35억 달러가 될 수 있다고 보도됐다. ([Reuters][11])

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
stage_failure_type = should_have_been_stage1_only
```

---

# 5. 이번 R5 case별 요약표

| case                                      | 분류                            |                                                        실제 가격검증 | alignment          |
| ----------------------------------------- | ----------------------------- | -------------------------------------------------------------: | ------------------ |
| 삼양식품                                      | structural_success + 4C-watch | 647,000원, +5.7%; target upside +28.3%; Denmark recall/reversal | aligned_partial    |
| 농심                                        | success_candidate             |      Shin $883M, 해외 60%, U.S. target +178.8%; Toomba 17M units | success_candidate  |
| APR                                       | structural_success + 4B       |                   158,300원, IPO 이후 >75%; $4.2B→$6B; Jan 이후 >4배 | aligned + 4B       |
| d’Alba / Silicon2                         | overheat + Stage2             |          d’Alba debut 후 >2배; U.S. e-commerce top5 K-brand +71% | event_premium      |
| CJ / Olive Young                          | success_candidate             |  U.S. K-beauty $2B, +37%; Olive Young 1,300+ stores, U.S. 2026 | stage2_watch       |
| AmorePacific                              | failed_rerating               |                        Q2 miss 후 약 -25%, worst day in 14 years | thesis_break_watch |
| Hyundai Dept / Shilla / Hankook Cosmetics | event_premium                 |                   +7.1% / +4.8% / +9.9%; visitor target +12.8% | event_premium      |
| F&F                                       | event_premium                 |       TaylorMade possible value $3.5B, F&F stake exposure 7.4% | M&A optionality    |

---

# 6. score-price alignment 판정

```text
aligned / structural_success_candidate:
- 삼양식품
- APR

success_candidate:
- 농심
- CJ / Olive Young
- Silicon2 / K-beauty distribution platform

event_premium:
- d’Alba IPO/post-debut rally
- Hyundai Department Store / Hotel Shilla / Hankook Cosmetics tourism retail event
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

삼양식품은 수출·ASP·OP revision이 한 번에 확인됐고, APR은 해외 매출과 미국 채널이 실제 매출로 이어지며 대형 price path가 확인됐다. 농심은 Shin Ramyun이 global staple 구조를 갖고 있으며, Toomba는 product extension 가능성을 보여준다.

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

이번 R5에서 hard 4C는 확정하지 않는다. Samyang Denmark recall은 부분 해제됐으므로 `regulatory_4C_watch`, AmorePacific China exposure는 `thesis_break_watch`, d’Alba/F&F/tourism retail은 `event_premium`으로 둔다.

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

## docs/round/round_150.md 요약

```md
# R5 Loop 9. Consumer / Retail / Brand Price Validation

이번 라운드는 R5 Loop 9 price-validation 라운드다.

핵심 결론:
- Samyang Foods는 Buldak export, ASP uplift, OP revision이 같이 확인되어 Stage 3 후보가 된다. 647,000원 close, +5.7%, target upside +28.3% anchor가 있다. 다만 Denmark recall/reversal은 local-regulatory 4C-watch로 기록한다.
- Nongshim은 Shin Ramyun global staple 구조가 강하다. Shin 2023 sales $883M, 해외비중 nearly 60%, U.S. target $1.5B by 2030이다. Toomba extension은 17M units in 3 months로 Stage 2 product-extension 후보지만 OPM/EPS 전 Green 보류다.
- APR은 R5 structural success benchmark다. 158,300원, IPO 이후 >75%, market cap $4.2B → $6B, January 이후 >4배 상승으로 4B-watch가 필요하다.
- d’Alba/Silicon2/K-beauty indie basket은 U.S. retail talks와 e-commerce growth가 강하지만, sell-through 전 Stage 3 금지다. d’Alba debut 후 >2배는 event premium이다.
- CJ/Olive Young은 K-beauty retail platform Stage 2 후보지만, direct listed earnings bridge와 store economics 전 Green 금지다.
- AmorePacific은 K-beauty macro와 company-level performance를 분리해야 한다. China exposure와 Q2 miss로 약 -25% 하락한 legacy K-beauty 4C-watch다.
- Hyundai Department Store / Hotel Shilla / Hankook Cosmetics는 중국 단체관광 무비자 정책 발표일 +7.1% / +4.8% / +9.9% 반응했다. 관광객 수보다 tourist spend/OPM이 Green 조건이다.
- F&F TaylorMade optionality는 M&A event다. $3.5B possible value와 F&F 358B won prior investment가 있지만 confirmed transaction / EPS accretion 전 Stage 3 금지다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 150 R5 Loop 9 Consumer Retail Brand Price Validation

## 반영 내용
- R5 Loop 9 price-validation 라운드를 추가했다.
- K-food export, global staple ramen, K-beauty device, indie K-beauty retail talks, K-beauty retail platform, legacy China exposure, tourism retail event, apparel M&A optionality를 비교했다.
- Reuters/FT/MarketWatch/Business Insider/Vogue/AP reported anchors로 가능한 MFE/MAE 및 business metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- repeat demand, export growth, ASP, channel sell-through, OPM, physical-store sell-through 가중치 강화
- viral product, IPO/debut rally, retail talks without sell-through, China exposure without offset, M&A optionality 감점 강화
- R5 4B-watch와 regulatory/channel 4C-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r5_loop9_samyang_buldak_export_regulatory_watch","symbol":"003230","company_name":"삼양식품","case_type":"structural_success_candidate","primary_archetype":"K_FOOD_EXPORT_RECURRING","stage2_date":"2024-06-14","stage3_date":"2024-06-14","stage4c_date":"2024-06-12","price_validation":{"price_data_source":"MarketWatch/AP/Reuters reported anchors","stage3_price":647000,"stage2_event_mfe_1d_pct":5.7,"implied_prior_close":611921,"target_price":830000,"target_upside_pct":28.3,"op_estimate_q2_krw_bn":81.2,"op_growth_estimate_pct":84,"denmark_recall_status":"2024-06 recall; 2024-08 partial reversal","price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned_partial","rerating_result":"K_food_export_rerating_candidate","notes":"Export/ASP/OP revision supports Stage 3 candidate; Denmark recall is regulatory 4C-watch, not hard 4C after partial reversal."}
{"case_id":"r5_loop9_nongshim_global_staple_toomba","symbol":"004370","company_name":"농심","case_type":"success_candidate","primary_archetype":"K_FOOD_GLOBAL_STAPLE_BRAND","stage2_date":"2024-05-27","price_validation":{"price_data_source":"FT/public product-extension summary","stage3_price":null,"shin_2023_sales_krw_trn":1.2,"shin_2023_sales_usd_mn":883,"overseas_sales_share_pct":60,"north_america_sales_2023_usd_mn":538,"north_america_growth_pct":10,"us_sales_target_2030_usd_bn":1.5,"target_growth_from_2023_na_sales_pct":178.8,"toomba_first_3_month_sales_mn_units":17,"nongshim_us_subsidiary_sales_forecast_2025_krw_bn":669,"us_subsidiary_growth_forecast_pct":7.4,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"global_staple_brand_watch","notes":"Global staple and product extension are Stage 2; OPM/EPS and channel sell-through required for Green."}
{"case_id":"r5_loop9_apr_medicube_structural_4b","symbol":"278470","company_name":"APR / Medicube","case_type":"structural_success","primary_archetype":"K_BEAUTY_DEVICE_GLOBAL_BRAND","stage2_date":"2025-07-08","stage3_date":"2025-10-20","stage4b_date":"2025-10-20","price_validation":{"price_data_source":"Business Insider/FT/Vogue Business anchors","stage2_price":158300,"implied_ipo_reference_price_max":90457,"ipo_to_stage2_mfe_min_pct":75,"market_cap_july_usd_bn":4.2,"market_cap_oct_usd_bn":6.0,"market_cap_mfe_july_to_oct_pct":42.9,"reported_mfe_since_january_pct":300,"q4_2025_revenue_usd_mn":440,"q4_2025_revenue_growth_pct":124,"q4_2025_overseas_revenue_usd_mn":362,"q4_2025_overseas_growth_pct":203,"fy_2025_revenue_usd_bn":1.2,"medicube_fy_2025_revenue_usd_bn":1.1,"medicube_revenue_share_pct":91.7,"price_validation_status":"reported_price_and_marketcap_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"K_beauty_device_true_rerating_plus_4B_watch","notes":"APR is structural success candidate; fourfold rally and $6B valuation require 4B-watch."}
{"case_id":"r5_loop9_dalba_silicon2_indie_kbeauty_watch","symbol":"483650/257720","company_name":"d'Alba / Silicon2 / K-beauty indie basket","case_type":"overheat","primary_archetype":"K_BEAUTY_INDIE_BRAND_US_CHANNEL","stage2_date":"2025-06-05","stage4b_date":"2025-06-05","price_validation":{"price_data_source":"Reuters business and reported return anchors","stage3_price":null,"dalba_reported_mfe_since_debut_pct":100,"top5_korean_cosmetics_us_ecommerce_growth_pct":71,"overall_us_market_growth_pct":21,"relative_growth_vs_us_market_multiple":3.38,"retail_talks":["Ulta","Sephora","Target","Costco"],"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence_for_dalba_success_candidate_for_distributor","rerating_result":"K_beauty_indie_retail_watch","notes":"Retail talks and e-commerce growth are Stage 2; sell-through, repeat orders, OPM and working-capital quality required before Green."}
{"case_id":"r5_loop9_cj_olive_young_retail_platform","symbol":"001040/CJ_OliveYoung_exposure","company_name":"CJ / Olive Young","case_type":"success_candidate","primary_archetype":"K_BEAUTY_RETAIL_PLATFORM","stage2_date":"2025-2026","price_validation":{"price_data_source":"Business Insider/Reuters/public company summary","stage3_price":null,"us_kbeauty_market_size_usd_bn":2.0,"us_kbeauty_market_growth_pct":37,"olive_young_korea_stores":1300,"us_store_timing":"2026 planned","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"K_beauty_retail_platform_watch","notes":"Olive Young is Stage 2 platform exposure; direct listed earnings bridge, store economics and OPM required for Green."}
{"case_id":"r5_loop9_amorepacific_legacy_china_exposure","symbol":"090430","company_name":"아모레퍼시픽","case_type":"failed_rerating","primary_archetype":"LEGACY_BEAUTY_CHINA_EXPOSURE_4C","stage4c_date":"2024-08","price_validation":{"price_data_source":"FT reported event return anchor","stage3_price":null,"event_mae_1d_pct":-25,"event_context":["Q2 earnings miss","China demand weakness","local Chinese brand competition","premium beauty pressure"],"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"legacy_K_beauty_China_exposure_break","notes":"K-beauty macro is not enough; China decline and premium beauty weakness block Green."}
{"case_id":"r5_loop9_tourism_retail_china_visa_event","symbol":"069960/008770/123690","company_name":"현대백화점/호텔신라/한국화장품","case_type":"event_premium","primary_archetype":"TOURISM_RETAIL_DUTYFREE_EVENT","stage2_date":"2025-08-06","stage4b_date":"2025-08-06","price_validation":{"price_data_source":"Reuters event return and tourism metrics","stage3_price":null,"hyundai_department_event_mfe_1d_pct":7.1,"hotel_shilla_event_mfe_1d_pct":4.8,"hankook_cosmetics_event_mfe_1d_pct":9.9,"paradise_event_mfe_1d_pct":2.9,"visitors_2024_mn":16.4,"visitor_growth_2024_pct":48,"chinese_share_pct":28,"target_visitors_2025_mn":18.5,"target_growth_vs_2024_pct":12.8,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"tourism_retail_recovery_watch","notes":"Visa-free tourist policy is Stage 2/event; tourist spend, sell-through, duty-free sales and OPM required before Green."}
{"case_id":"r5_loop9_fnf_taylormade_mna_optionality","symbol":"383220","company_name":"F&F","case_type":"event_premium","primary_archetype":"APPAREL_M_AND_A_OPTIONALITY","stage1_date":"2025-07-21","price_validation":{"price_data_source":"Reuters deal evidence anchor","stage3_price":null,"reported_taylormade_value_usd_bn":3.5,"ff_2021_subordinated_equity_investment_krw_bn":358,"fx_rate_reported":1387.39,"krw_equiv_value_krw_trn":4.856,"ff_investment_vs_possible_value_pct":7.4,"total_subordinated_equity_investment_krw_bn":619.2,"ff_share_of_subordinated_equity_pct":57.8,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium","rerating_result":"M&A_optionality_watch","notes":"TaylorMade optionality is Stage 1/2 event; confirmed transaction, financing and EPS accretion required for Green."}
```

## shadow weight row 초안

```csv
archetype,repeat_demand,export_growth,asp,channel_sellthrough,overseas_mix,opm,inventory_quality,receivables_quality,event_penalty,regulatory_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
K_FOOD_EXPORT_RECURRING,+5,+5,+4,+4,+5,+5,+4,+4,-2,+4,+4,+3,Samyang export/ASP/OP revision supports Stage 3 candidate but recall/regulatory watch remains.
K_FOOD_GLOBAL_STAPLE_BRAND,+5,+5,+3,+5,+5,+4,+4,+4,-1,+2,+3,+3,Nongshim global staple/product extension is Stage 2 until OPM/EPS/sell-through confirm.
K_BEAUTY_DEVICE_GLOBAL_BRAND,+5,+5,+3,+5,+5,+5,+3,+3,-2,+2,+5,+3,APR is structural success but fourfold rally requires 4B-watch.
K_BEAUTY_INDIE_BRAND_US_CHANNEL,+3,+5,+2,+5,+5,+4,+4,+4,-5,+3,+5,+4,d'Alba/indie K-beauty retail talks require sell-through before Green.
K_BEAUTY_RETAIL_PLATFORM,+5,+4,+2,+5,+4,+5,+4,+4,-3,+3,+4,+3,Olive Young platform needs listed earnings bridge and U.S. store economics.
LEGACY_BEAUTY_CHINA_EXPOSURE_4C,+2,+3,+2,+3,+3,+4,+5,+5,-2,+4,+4,+5,Amore legacy China exposure blocks macro K-beauty Green.
TOURISM_RETAIL_DUTYFREE_EVENT,+2,+3,+2,+5,+3,+4,+4,+3,-5,+2,+5,+4,Tourism retail event needs spend/sell-through/OPM, not just visitor policy.
APPAREL_M_AND_A_OPTIONALITY,+1,+1,+1,+1,+1,+3,+2,+2,-5,+2,+5,+3,F&F TaylorMade optionality is not Green until confirmed deal and EPS accretion.
```

---

# 이번 R5 Loop 9 결론

R5는 Stage 3 후보가 분명 있지만, **viral·입점 논의·관광정책·M&A optionality를 너무 쉽게 Green으로 올리면 false positive가 빠르게 쌓이는 섹터**다.

```text
1. 삼양식품은 수출 + ASP + OP revision이 같이 확인되어 Stage 3 후보가 될 수 있다.
   하지만 Denmark recall 같은 local-regulatory watch를 같이 붙여야 한다.

2. 농심은 Shin Ramyun global staple과 Toomba product extension이 좋다.
   그러나 OPM/EPS revision과 sell-through 확인 전 Stage 3는 보류다.

3. APR은 R5의 가장 강한 structural success 후보 중 하나다.
   하지만 4배 이상 상승과 $6B valuation은 4B-watch를 요구한다.

4. d’Alba / Silicon2 / indie K-beauty는 U.S. e-commerce와 retail talks가 강하지만,
   physical store sell-through 전 Stage 3 금지다.

5. CJ / Olive Young은 좋은 K-beauty retail platform 후보지만,
   direct listed earnings bridge와 U.S. store economics 전 Green 금지다.

6. AmorePacific은 K-beauty macro tailwind와 회사 실적을 분리해야 한다.
   China exposure와 legacy premium beauty weakness는 4C-watch다.

7. 현대백화점·호텔신라·한국화장품은 중국 무비자 정책 이벤트로 올랐지만,
   tourist spend와 OPM 전에는 event premium이다.

8. F&F TaylorMade는 M&A optionality이지 브랜드 Stage 3가 아니다.
```

한 문장으로 압축하면:

> **R5에서 진짜 Stage 3는 “K-food·K-beauty·브랜드가 핫하다”가 아니라, 반복구매·해외 채널 sell-through·ASP·OPM·재고/채권 품질이 실제 이익 체급 변화로 내려오는 순간이다.**
> **R5는 viral·IPO/debut rally·입점 논의·관광정책·M&A optionality를 먼저 4B/Event Premium으로 분리해야 점수표가 산다.**

[1]: https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045?utm_source=chatgpt.com "Samyang Foods Set to Post Strong 2Q Earnings -- Market Talk"
[2]: https://apnews.com/article/f622b2d901990a08d180eee3ce2260f2?utm_source=chatgpt.com "Denmark recalls spicy South Korean noodles over health concerns"
[3]: https://www.ft.com/content/4218f2b8-5498-411b-81fe-e3c836868d64?utm_source=chatgpt.com "Maker of Shin instant ramen expands overseas as Korean noodles become hit"
[4]: https://en.wikipedia.org/wiki/Toomba_Shin_Ramyun?utm_source=chatgpt.com "Toomba Shin Ramyun"
[5]: https://www.businessinsider.com/south-korea-kim-byung-hoon-beauty-billionaire-kylie-jenner-fan-2025-7?utm_source=chatgpt.com "Meet South Korea's new millennial beauty billionaire, who counts Kylie Jenner as a fan of his skincare gadgets"
[6]: https://www.vogue.com/article/how-k-beauty-brand-medicube-pulled-off-its-global-breakout?utm_source=chatgpt.com "How K-Beauty Brand Medicube Pulled Off Its Global Breakout"
[7]: https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/?utm_source=chatgpt.com "Korean beauty startups bet booming US demand outlasts tariff pain"
[8]: https://www.businessinsider.com/korean-beauty-brands-exclusive-sephora-ulta-olive-young-2025-10?utm_source=chatgpt.com "A K-beauty turf war is brewing in the US"
[9]: https://www.ft.com/content/6b101349-55b1-4a72-bb21-0b77bf3c5f03?utm_source=chatgpt.com "Product patriotism isn't pretty for Asia's beauty groups"
[10]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/?utm_source=chatgpt.com "South Korea to offer visa-free entry to Chinese tourists from late September"
[11]: https://www.reuters.com/world/asia-pacific/s-korean-fashion-retailer-ff-hires-goldman-taylormade-acquisition-2025-07-21/?utm_source=chatgpt.com "S. Korean fashion retailer F&F hires Goldman for TaylorMade acquisition"
