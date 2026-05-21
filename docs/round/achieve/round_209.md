순서상 이번은 **R5 Loop 8 — 소비재·유통·브랜드 가격경로 검증 라운드**다.

이번 라운드도 원시 수정주가 일봉 OHLC를 안정적으로 직접 추출하지 못한 종목에 대해 숫자를 지어내지 않았다. 대신 Reuters / FT / MarketWatch / Business Insider에 남은 **가격 anchor, 이벤트 수익률, 시가총액, 매출·이익 추정치**로 계산 가능한 값은 직접 계산했다.

```text
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

---

# 1. 이번 라운드 대섹터

```text
R5 = 소비재·유통·브랜드
large_sector = CONSUMER_RETAIL_BRAND
round = R5 Loop 8 / price-path validation
```

R5의 기본 검증축은 `export_growth`, `channel_expansion`, `repeat_demand`, `opm`, `inventory`, `receivables`, `recall_regulation`이다. R5는 K푸드, K뷰티, 유통, 이커머스, ODM, 의류, 렌탈, 규제 소비재를 다루지만, 핵심은 “브랜드가 핫하다”가 아니라 **반복수요·채널 sell-through·OPM·재고/채권 품질·FCF가 확인되는가**다. 

Round 119 기준으로 R5에서 부족한 증거는 `viral_product`, `brand_heat`이고, 필요한 증거는 `repeat_demand`, `asp`, `channel_sell_through`, `opm`, `inventory_quality`다. Green blocker는 `fad_normalization`, `channel_stuffing`, `recall_or_regulation`이다. 

---

# 2. 대상 canonical archetype

```text
EXPORT_RECURRING_CONSUMER
K_FOOD_GLOBAL_STAPLE_BRAND
K_FOOD_SINGLE_SKU_RISK
K_BEAUTY_BRAND_US_CHANNEL
K_BEAUTY_EXPORT_DISTRIBUTION
K_BEAUTY_OEM_ODM_SUPPLYCHAIN_KOREA
K_BEAUTY_RETAIL_PLATFORM
BEAUTY_DEVICE_EXPORT
APPAREL_FAST_FASHION_BRAND_OEM
CHANNEL_STUFFING_INVENTORY_OVERLAY
TARIFF_IMPORT_MARGIN_OVERLAY
EVENT_PREMIUM_GOVERNANCE_OVERLAY
PRICE_ONLY_RALLY
```

이번 R5의 핵심 질문은 이거다.

```text
K푸드·K뷰티·브랜드 테마인가?
아니면 반복소비, 해외 채널, sell-through, OPM, 재고/채권 품질이
실제 EPS/FCF 체급 변화로 내려오는가?
```

---

# 3. deep sub-archetype

```text
K푸드:
- Buldak export
- Shin Ramyun global staple
- U.S. / Europe shipment growth
- ASP uplift
- overseas capacity
- single SKU risk
- recall / regulation risk

K뷰티 디바이스:
- APR / Medicube
- beauty device
- U.S. sales mix
- overseas revenue mix
- TikTok / influencer virality
- Ulta distribution
- tariff margin squeeze
- competition / product-cycle fade

K뷰티 indie brand:
- d’Alba Global
- retail talks with Costco / Ulta / Target
- IPO overheat
- U.S. physical store sell-through
- viral product vs repeat purchase

K뷰티 ODM:
- Cosmax / Kolmar
- Foxconn of fast beauty
- customer diversification
- outsourced production
- margin pass-through
- receivables / inventory quality

Legacy K뷰티:
- Amorepacific
- COSRX plateau
- China exposure
- U.S. transition
- brand mix recovery

의류 / M&A event:
- F&F
- TaylorMade acquisition
- ROFR / legal dispute
- M&A optionality vs brand rerating
```

---

# 4. 국장 신규 후보 case

## Case A — 삼양식품 `structural_success 후보 / K-food export`

```text
symbol = 003230
case_type = structural_success 후보
archetype = EXPORT_RECURRING_CONSUMER / K_FOOD_GLOBAL_STAPLE_BRAND
```

### evidence

2024년 6월 14일 MarketWatch는 삼양식품이 불닭볶음면 수출 호조로 2분기 강한 실적을 낼 것으로 예상된다고 보도했다. Kiwoom은 2분기 영업이익 추정치를 전년 대비 84% 증가한 812억 원으로 올렸고, 미국·유럽 출하 증가와 ASP 상승, 생산능력 확대를 근거로 목표주가를 660,000원에서 830,000원으로 상향했다. 당시 삼양식품 주가는 5.7% 상승해 647,000원에 마감했다. ([마켓워치][1])

### stage date

```text
Stage 1:
2023~2024
- Buldak viral export
- 미국·유럽 K-food demand

Stage 2:
2024-06-14
- 2Q OP estimate +84% YoY
- ASP 상승
- 미국·유럽 출하 증가
- 생산능력 확대

Stage 3:
2024-06-14 후보
- 수출 성장 + ASP + OP revision이 함께 나온 구간
- 다만 full OHLC 기준 MFE/MAE는 직접 확보 실패

Stage 4B:
Buldak 단일 제품과 K-food premium이 valuation에 과도하게 반영된 구간이면 후보

Stage 4C:
recall / regulation / single SKU fade / copycat risk 발생 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch reported close and target-price anchor

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
(830,000 / 647,000) - 1
= +28.3%

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
stage_failure_type = green_success_candidate
```

### 교정

삼양식품은 R5에서 `export_growth`, `ASP`, `OP revision`, `capacity_support`를 올려준다. 다만 `single_SKU_dependence`, `viral_product_only`, `recall_regulation`은 동시에 4B/4C watch로 둔다.

---

## Case B — 농심 `success_candidate / global staple K-food`

```text
symbol = 004370
case_type = success_candidate
archetype = K_FOOD_GLOBAL_STAPLE_BRAND / EXPORT_RECURRING_CONSUMER
```

### evidence

FT는 2024년 5월 농심 신라면의 2023년 매출이 1.2조 원, 약 8.83억 달러로 사상 최대였고, 이 중 거의 60%가 해외에서 나왔다고 보도했다. 북미 매출은 2023년에 5.38억 달러로 10% 증가했고, 농심은 미국 매출을 2030년까지 15억 달러로 키우겠다는 목표를 제시했다. ([Financial Times][2])

### stage date

```text
Stage 1:
2023~2024
- Shin Ramyun global staple
- K-food export growth

Stage 2:
2024-05-27
- Shin Ramyun record sales
- overseas sales nearly 60%
- North America sales +10%

Stage 3:
보류
- 안정적 글로벌 staple 구조는 강하지만
- OPM, ASP, channel sell-through, EPS revision 확인 필요

Stage 4B:
K-food staple valuation이 이미 크게 확장된 경우 후보

Stage 4C:
중국 둔화, 원가 상승, 미국 sell-through 둔화, food safety issue 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
FT business evidence source only

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- FT는 주가 anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

North_America_sales_2023:
$538M

U.S._sales_target_2030:
$1.5B

implied_US_target_growth_from_2023_North_America_sales:
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

### 교정

농심은 삼양식품과 달리 viral 단일제품보다 `global_staple`, `repeat_demand`, `localized_distribution` 쪽을 올려준다. Stage 3는 OPM/EPS revision이 확인된 뒤 줘야 한다.

---

## Case C — APR `structural_success + 4B-watch`

```text
symbol = 278470
case_type = structural_success + 4B-watch
archetype = BEAUTY_DEVICE_EXPORT / K_BEAUTY_BRAND_US_CHANNEL
```

### evidence

Business Insider는 2025년 7월 8일 APR 주가가 158,300원에 거래됐고, 이는 IPO 이후 75% 이상 상승한 수준이며 시가총액이 약 42억 달러라고 보도했다. ([Business Insider][3])

FT는 2025년 10월 20일 APR 주가가 2025년 1월 이후 4배 이상 올랐고, 시가총액이 약 60억 달러까지 커졌다고 보도했다. 같은 기사에서 2025년 2분기 매출의 거의 80%가 해외에서 나왔고, 미국 매출이 거의 30%를 차지했다고 정리했다. ([Financial Times][4])

Vogue Business는 2026년 2월 Medicube가 2025년 4분기 약 4.4억 달러 매출을 기록해 전년 대비 124% 증가했고, 해외 매출은 약 3.62억 달러로 203% 증가했다고 보도했다. 또한 2025년 전체 매출은 약 12억 달러, Medicube 매출은 약 11억 달러였다고 설명했다. ([Vogue][5])

### stage date

```text
Stage 1:
2024 IPO / 2025 K-beauty device virality
- Medicube beauty device
- Kylie Jenner / TikTok / U.S. expansion

Stage 2:
2025-07-08
- stock 158,300원
- IPO 이후 +75% 이상
- market cap about $4.2B

Stage 3:
2025-10-20 후보
- overseas revenue nearly 80% in Q2
- U.S. revenue nearly 30%
- stock more than fourfold since January
- market cap about $6B

Stage 4B:
2025-10-20
- 4배 이상 상승
- valuation crowding
- U.S. tariff / competition risk

Stage 4C:
없음
- 단, tariff margin squeeze, device fad fade, competition, sell-through failure 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Business Insider / FT / Vogue Business reported anchors

stage2_price:
158,300원

implied_IPO_reference_price_from_75pct_gain:
158,300 / 1.75
= 약 90,457원 이하
=> IPO 이후 MFE > +75%

FT_market_cap_Jul_anchor:
$4.2B

FT_market_cap_Oct_anchor:
$6.0B

market_cap_MFE_July_to_Oct:
6.0 / 4.2 - 1
= +42.9%

reported_MFE_since_January:
> +300%

stage3_price:
price_data_unavailable_after_deep_search
- FT는 2025-10-20 주가 절대값을 제공하지 않고 market cap / return만 제공.
- share count 기반 implied price는 가능하지만 raw OHLC가 아니므로 stage3_price는 unavailable 처리.

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MFE_1Y:
reported since-January MFE > +300%

MAE:
price_data_unavailable_after_deep_search

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- 2025-10-20 시점에서 4배 이상 상승과 valuation crowding이 이미 확인됨.
```

### alignment

```text
score_price_alignment = aligned
rerating_result = K_beauty_device_true_rerating_plus_4B_watch
stage_failure_type = green_success_candidate
```

### 교정

APR은 R5에서 `overseas_sales_mix`, `U.S._sales_mix`, `category_creation`, `OPM`, `sell-through`를 올린다. 동시에 `viral_influencer_dependence`, `tariff_margin_squeeze`, `competition`, `valuation_4B`를 강하게 붙여야 한다.

---

## Case D — d’Alba Global `overheat / price_moved_without_evidence`

```text
symbol = 483650
case_type = overheat / 4B-watch
archetype = K_BEAUTY_BRAND_US_CHANNEL / PRICE_ONLY_RALLY
```

### evidence

Reuters는 2025년 6월 d’Alba Global이 Costco, Ulta Beauty, Target과 미국 오프라인 유통 입점을 논의 중이라고 보도했다. 같은 기사에서 d’Alba Global 주가는 상장 후 한 달 만에 두 배 이상 올랐다고 설명했다. 다만 이것은 실제 매장 sell-through가 아니라 **입점 논의 + IPO 직후 가격 선반영**이다. ([Reuters][6])

### stage date

```text
Stage 1:
2025년 IPO / K-beauty U.S. channel story

Stage 2:
2025-06-05
- Costco / Ulta / Target 입점 논의
- U.S. K-beauty physical channel 기대

Stage 3:
없음
- 입점 논의만으로 Green 금지
- sell-through, repeat order, OPM, inventory quality 확인 필요

Stage 4B:
2025-06-05
- 상장 후 한 달 만에 주가 2배 이상

Stage 4C:
입점 실패, sell-through 부진, tariff 부담, 재고 증가 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported return anchor

stage3_price:
N/A

reported_MFE_since_debut:
> +100%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- 상장 후 한 달 만에 2배 이상 상승은 4B-watch.
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = IPO_K_beauty_event_premium
stage_failure_type = should_have_been_4B_watch_not_green
```

### 교정

d’Alba는 `retail_talks_without_sell_through`, `IPO_first_month_rally`, `brand_heat_only`를 감점한다.

---

## Case E — 코스맥스 / 한국콜마 `success_candidate / ODM leverage`

```text
symbols = 192820 / 161890
case_type = success_candidate
archetype = K_BEAUTY_OEM_ODM_SUPPLYCHAIN_KOREA
```

### evidence

Reuters는 한국 indie K-beauty 브랜드들이 미국 시장에 진출하면서 생산을 Cosmax와 Kolmar 같은 contract manufacturers에 맡기고 있으며, 이들이 “fast beauty의 Foxconn”으로 불린다고 보도했다. 같은 기사에서 한국은 2024년 독일을 넘어 세계 3위 화장품 수출국이 됐고, 화장품 생산액 130억 달러 중 5분의 4가 수출용이라고 설명했다. ([Reuters][6])

### stage date

```text
Stage 1:
2024~2025
- K-beauty indie brand boom
- U.S. e-commerce / physical channel expansion

Stage 2:
2025-06-05
- Cosmax / Kolmar as contract manufacturing backbone
- high-margin / scalable outsourcing model

Stage 3:
보류
- 회사별 order visibility, customer diversification, OPM, inventory/receivables 확인 필요

Stage 4B:
K-beauty ODM주가 브랜드 성공을 뒤따라 일괄 rerating되면 후보

Stage 4C:
고객 브랜드 성장 둔화, receivables 증가, inventory build, tariff pass-through failure 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters business evidence only

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- Reuters는 Cosmax/Kolmar 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

K-beauty_export_structure:
$13B cosmetics output, about 80% export-driven

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = ODM_supply_chain_watch
stage_failure_type = stage2_watch_success
```

### 교정

ODM은 좋은 구조지만, Stage 3는 `고객 다변화 + 수주 + OPM + 재고/채권 안정`이 있어야 한다.

---

## Case F — 아모레퍼시픽 `failed_rerating / transition watch`

```text
symbol = 090430
case_type = failed_rerating / transition_watch
archetype = K_BEAUTY_BRAND_US_CHANNEL / CHINA_CONSUMER_EXPOSURE_4C
```

### evidence

Reuters는 2025년 6월 K-beauty가 미국에서 강하게 성장하고 있지만, 기존 최대 시장이던 중국 수출은 지정학과 경쟁 때문에 약해졌고, 아모레퍼시픽이 편입한 COSRX 같은 브랜드도 경쟁 심화와 저가 대체재 때문에 성장 plateau 조짐이 있다고 보도했다. 이건 “K-beauty macro”와 “legacy company-level rerating”을 분리해야 한다는 근거다. ([Reuters][6])

### stage date

```text
Stage 1:
2024~2025
- K-beauty U.S. expansion
- COSRX / Laneige / Sulwhasoo global mix 기대

Stage 2:
2025-06-05
- K-beauty U.S. push 확인
- 동시에 China decline / COSRX plateau risk 확인

Stage 3:
없음
- China decline offset, U.S./Europe sell-through, OPM recovery 확인 전 Green 금지

Stage 4B:
legacy K-beauty가 macro tailwind만으로 rerating되면 후보

Stage 4C:
China sales collapse, brand growth plateau, inventory/receivable deterioration 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters business evidence only

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- Reuters는 Amorepacific 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed_candidate
rerating_result = legacy_K_beauty_transition_watch
stage_failure_type = should_have_been_yellow_or_watch
```

### 교정

아모레퍼시픽은 `K-beauty macro tailwind ≠ company-level Green` 기준점이다. 미국 채널 성장과 중국 둔화 상쇄, 브랜드 mix, OPM 회복이 필요하다.

---

## Case G — F&F `event_premium / M&A optionality`

```text
symbol = 383220
case_type = event_premium / insufficient_evidence
archetype = APPAREL_FAST_FASHION_BRAND_OEM / EVENT_PREMIUM_GOVERNANCE_OVERLAY
```

### evidence

2025년 7월 F&F는 TaylorMade 인수를 위해 Goldman Sachs를 자문사로 선임했고, 기존 보유자인 Centroid가 별도 매각 절차를 진행할 경우 법적 조치를 취하겠다고 밝혔다. F&F는 2021년 TaylorMade 인수 때 3,580억 원 후순위 지분투자를 했고, 핵심 경영사안에 대한 동의권과 우선매수권을 주장했다. Reuters는 TaylorMade 거래가 약 35억 달러 valuation을 받을 수 있다고 보도했다. ([Reuters][7])

### stage date

```text
Stage 1:
2025-07-21
- TaylorMade acquisition / ROFR / legal event

Stage 2:
없음 또는 약한 Stage 2
- 실제 인수 확정 전
- 본업 의류 실적 evidence 아님

Stage 3:
없음
- M&A optionality만으로 Green 금지

Stage 4B:
거래 기대만으로 주가가 급등하면 event premium 4B-watch

Stage 4C:
거래 무산, 법적 분쟁, 투자손상, 본업 브랜드 부진 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters deal evidence only

stage3_price:
N/A

stage1_price:
price_data_unavailable_after_deep_search
- Reuters는 F&F 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

reported_TaylorMade_possible_valuation:
$3.5B

F&F_2021_subordinated_equity_investment:
358.0 billion won

KRW_equivalent_of_$3.5B_at_reported_fx_1387.39:
3.5B * 1,387.39 = 약 4.856 trillion won

F&F_subordinated_equity_vs_possible_TaylorMade_value:
358B / 4.856T
= 약 7.4%

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

### 교정

F&F는 R5에서 `M&A optionality`와 `brand rerating`을 분리해야 한다. TaylorMade 이벤트는 Stage 1~2 event이고, Stage 3는 본업 매출·OPM·FCF 또는 인수 후 EPS accretion이 확인되어야 한다.

---

# 5. 이번 R5 case별 요약표

| case          | 분류                        |                                                       실제 가격검증 | alignment                                |
| ------------- | ------------------------- | ------------------------------------------------------------: | ---------------------------------------- |
| 삼양식품          | structural_success 후보     | 647,000원 close, +5.7%; target 830,000원, implied upside +28.3% | aligned_partial                          |
| 농심            | success_candidate         |                Shin Ramyun $883M, 해외 60%; U.S. target +178.8% | success_candidate                        |
| APR           | structural_success + 4B   |        158,300원, IPO 이후 >75%; 시총 $4.2B→$6B +42.9%; Jan 이후 >4배 | aligned + 4B                             |
| d’Alba Global | overheat / 4B             |                                              IPO 후 한 달 만에 >2배 | price_moved_without_evidence             |
| 코스맥스/한국콜마     | success_candidate         |                           K-beauty ODM backbone, 가격 anchor 없음 | success_candidate                        |
| 아모레퍼시픽        | failed / transition watch |                   COSRX plateau / China decline, 가격 anchor 없음 | evidence_good_but_price_failed_candidate |
| F&F           | event_premium             |      TaylorMade possible value $3.5B, F&F investment 3,580억 원 | event_premium                            |

---

# 6. score-price alignment 판정

```text
aligned / structural_success_candidate:
- 삼양식품
- APR

success_candidate:
- 농심
- 코스맥스 / 한국콜마

price_moved_without_evidence:
- d’Alba Global IPO 후 한 달 2배 이상

evidence_good_but_price_failed_candidate:
- 아모레퍼시픽

event_premium:
- F&F TaylorMade M&A optionality

4B-watch:
- APR 2025년 1월 이후 4배 이상
- d’Alba IPO 후 한 달 2배 이상
- 삼양식품 단일 Buldak 제품 프리미엄이 valuation에 과도하게 반영되는 구간
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
ODM_customer_diversification +4
```

### 이유

삼양식품은 수출, ASP, OP revision이 동시에 확인됐고, APR은 해외 매출 거의 80%, 미국 매출 거의 30%, 주가 4배 이상이라는 price path가 확인됐다. 이 둘은 R5에서 진짜 Stage 3 후보가 될 수 있는 기준점이다. ([마켓워치][1])

## 내릴 축

```text
viral_product_only -5
brand_heat_only -5
retail_talks_without_sell_through -4
IPO_first_month_rally -5
influencer_endorsement_only -4
single_SKU_dependence -4
China_exposure_without_offset -4
M&A_optionality_without_EPS -4
tariff_margin_uncertainty -3
inventory_or_receivables_build -5
```

### 이유

d’Alba는 Costco/Ulta/Target 입점 “논의”와 상장 후 2배 상승이 확인됐지만, sell-through와 반복발주는 아직 확인되지 않았다. F&F의 TaylorMade 이벤트도 M&A optionality일 뿐 본업 EPS/FCF 증거가 아니다. ([Reuters][6])

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
8. 가격경로가 evidence 이후 따라옴

금지:
viral TikTok만 있음
입점 논의만 있음
IPO 직후 급등
인플루언서 endorsement만 있음
M&A optionality만 있음
비상장 자회사 가치만 있음
중국 둔화 상쇄 증거 없음
```

## 4B 조기감지 조건

```text
4B-watch:
Stage 3 이후 2~4배 이상 상승
IPO 후 한 달 2배 이상 상승
single SKU / single device 의존도가 높음
보고서가 K-food / K-beauty macro만 반복
미국 입점 기대가 sell-through보다 먼저 가격에 반영
해외 매출은 좋지만 OPM 개선이 둔화

4B-elevated:
경쟁 제품 대거 출시
tariff 비용을 가격에 전가하지 못함
채널 확장 후 재고 증가
매출채권 증가
브랜드 성장률 normalize
```

## 4C hard gate 조건

```text
food safety recall
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

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

이번 세션에서 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉을 안정적으로 직접 확보하지 못했다. 대신 Reuters / FT / MarketWatch / Business Insider의 가격 anchor와 이벤트 수익률을 사용해 계산 가능한 부분은 직접 계산했다.

---

# 9. patch-ready 출력

## docs/round/round_137.md 요약

```md
# R5 Loop 8. Consumer / Retail / Brand Price Validation

이번 라운드는 R5 price-validation 라운드다.

핵심 결론:
- 삼양식품은 Buldak 수출, ASP 상승, OP revision이 같이 확인되어 Stage 3 후보가 될 수 있다. 2024-06-14 주가는 647,000원, 당일 +5.7%, 목표가 830,000원으로 implied upside +28.3%다.
- 농심은 Shin Ramyun global staple 구조가 강하지만, OPM/EPS revision 전 Stage 3는 보류한다.
- APR은 K-beauty device 구조적 성공 후보이며, 2025년 1월 이후 4배 이상 상승해 4B-watch가 필요하다.
- d’Alba Global은 U.S. retail talks와 IPO 후 2배 상승이 확인됐지만 sell-through 전 Stage 3가 아니다.
- Cosmax/Kolmar는 K-beauty ODM backbone으로 Stage 2 후보지만 고객 다변화, OPM, inventory/receivables 확인 전 Green 금지다.
- Amorepacific은 K-beauty macro와 회사 실적을 분리해야 한다. COSRX plateau와 China exposure가 Green을 막는다.
- F&F TaylorMade 이벤트는 M&A optionality이며 Stage 3가 아니다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 137 R5 Loop 8 Consumer Retail Brand Price Validation

## 반영 내용
- R5 Loop 8 price-validation 라운드를 추가했다.
- K-food export, K-beauty device, indie-brand IPO overheat, ODM leverage, legacy K-beauty transition, apparel M&A optionality를 비교했다.
- Reuters/FT/MarketWatch/Business Insider reported price anchors로 가능한 MFE/MAE를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- repeat demand, export growth, ASP, channel sell-through, OPM 가중치 강화
- viral product, IPO first-month rally, retail talks without sell-through, M&A optionality 감점 강화
- K-beauty/K-food 4B-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r5_loop8_samyang_buldak_export_aligned","symbol":"003230","company_name":"삼양식품","case_type":"structural_success","primary_archetype":"EXPORT_RECURRING_CONSUMER","stage2_date":"2024-06-14","stage3_date":"2024-06-14","price_validation":{"price_data_source":"MarketWatch reported close/target anchor","stage3_price":647000,"mfe_1d":5.7,"implied_prior_close":611921,"target_price":830000,"target_upside_pct":28.3,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned_partial","rerating_result":"K_food_export_rerating_candidate","notes":"Buldak export, ASP uplift, OP revision and capacity support Stage 3 candidate; single SKU risk remains."}
{"case_id":"r5_loop8_nongshim_shin_global_staple","symbol":"004370","company_name":"농심","case_type":"success_candidate","primary_archetype":"K_FOOD_GLOBAL_STAPLE_BRAND","stage2_date":"2024-05-27","price_validation":{"price_data_source":"FT business evidence anchor","stage3_price":null,"north_america_sales_usd_mn":538,"us_sales_target_2030_usd_mn":1500,"implied_target_growth_pct":178.8,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"global_staple_brand_watch","notes":"Shin Ramyun global staple is strong, but Stage 3 requires OPM/EPS revision and channel sell-through."}
{"case_id":"r5_loop8_apr_medicube_device_4b","symbol":"278470","company_name":"APR","case_type":"structural_success","primary_archetype":"BEAUTY_DEVICE_EXPORT","stage2_date":"2025-07-08","stage3_date":"2025-10-20","stage4b_date":"2025-10-20","price_validation":{"price_data_source":"Business Insider/FT/Vogue reported anchors","stage2_price":158300,"implied_ipo_reference_price_max":90457,"ipo_to_stage2_mfe_min_pct":75.0,"market_cap_july_usd_bn":4.2,"market_cap_oct_usd_bn":6.0,"market_cap_mfe_july_to_oct_pct":42.9,"reported_mfe_since_january_pct":300.0,"price_validation_status":"reported_price_and_marketcap_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"K_beauty_device_true_rerating_plus_4B_watch","notes":"Overseas and U.S. sales mix support Stage 3; fourfold rally requires 4B-watch."}
{"case_id":"r5_loop8_dalba_global_ipo_overheat","symbol":"483650","company_name":"d'Alba Global","case_type":"overheat","primary_archetype":"K_BEAUTY_BRAND_US_CHANNEL","stage2_date":"2025-06-05","stage4b_date":"2025-06-05","price_validation":{"price_data_source":"Reuters reported return anchor","stage3_price":null,"reported_mfe_since_debut_pct":100.0,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"IPO_K_beauty_event_premium","notes":"Retail talks are Stage 2; sell-through and repeat orders required before Green."}
{"case_id":"r5_loop8_cosmax_kolmar_odm_leverage","symbol":"192820/161890","company_name":"코스맥스/한국콜마","case_type":"success_candidate","primary_archetype":"K_BEAUTY_OEM_ODM_SUPPLYCHAIN_KOREA","stage2_date":"2025-06-05","price_validation":{"price_data_source":"Reuters business evidence anchor","stage3_price":null,"k_beauty_output_usd_bn":13,"export_share_pct":80,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"ODM_supply_chain_watch","notes":"ODM leverage is strong, but Stage 3 needs customer diversification, OPM, inventory/receivables quality."}
{"case_id":"r5_loop8_amorepacific_transition_watch","symbol":"090430","company_name":"아모레퍼시픽","case_type":"failed_rerating","primary_archetype":"CHINA_CONSUMER_EXPOSURE_4C","stage2_date":"2025-06-05","price_validation":{"price_data_source":"Reuters business evidence anchor","stage3_price":null,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_failed_candidate","rerating_result":"legacy_K_beauty_transition_watch","notes":"K-beauty macro tailwind is not enough; China decline and COSRX plateau require Watch/Yellow."}
{"case_id":"r5_loop8_fnf_taylormade_event","symbol":"383220","company_name":"F&F","case_type":"event_premium","primary_archetype":"APPAREL_FAST_FASHION_BRAND_OEM","stage1_date":"2025-07-21","price_validation":{"price_data_source":"Reuters deal evidence anchor","stage3_price":null,"reported_taylormade_value_usd_bn":3.5,"ff_subordinated_equity_investment_krw_bn":358.0,"krw_equiv_value_trn":4.856,"ff_investment_vs_possible_value_pct":7.4,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium","rerating_result":"M&A_optionality_watch","notes":"TaylorMade acquisition optionality is not brand rerating; confirmed deal and EPS accretion required."}
```

## shadow weight row 초안

```csv
archetype,repeat_demand,export_growth,asp,channel_sellthrough,opm,inventory_quality,receivables_quality,event_penalty,4b_watch_sensitivity,notes
EXPORT_RECURRING_CONSUMER,+5,+5,+4,+4,+5,+4,+4,-2,+4,Samyang shows export/ASP/OP revision can be Stage 3 candidate but single-SKU risk remains.
K_FOOD_GLOBAL_STAPLE_BRAND,+5,+5,+3,+4,+4,+4,+4,-1,+3,Nongshim global staple is Stage 2 until OPM/EPS and channel sell-through confirm.
BEAUTY_DEVICE_EXPORT,+5,+5,+3,+5,+5,+3,+3,-2,+5,APR shows K-beauty device true rerating but fourfold rally requires 4B-watch.
K_BEAUTY_BRAND_US_CHANNEL,+3,+4,+2,+5,+4,+4,+4,-5,+5,d'Alba retail talks and IPO rally are not Stage 3 before sell-through.
K_BEAUTY_OEM_ODM_SUPPLYCHAIN_KOREA,+4,+4,+2,+4,+5,+5,+5,-2,+3,Cosmax/Kolmar ODM leverage needs customer diversification and working-capital quality.
CHINA_CONSUMER_EXPOSURE_4C,+2,+3,+2,+3,+4,+4,+4,-2,+4,Amorepacific requires China decline offset and brand mix recovery before Green.
APPAREL_FAST_FASHION_BRAND_OEM,+2,+2,+2,+2,+3,+3,+3,-5,+4,F&F TaylorMade optionality is event premium until confirmed EPS accretion.
```

---

# 이번 R5 Loop 8 결론

R5는 Stage 3 후보가 분명 있다. 하지만 viral·IPO·입점 논의·M&A 이벤트가 너무 많아서, Green gate를 느슨하게 주면 false positive가 빠르게 쌓인다.

```text
1. 삼양식품은 export + ASP + OP revision이 같이 확인되어 Stage 3 후보가 될 수 있다.
   647,000원 close, +5.7%, target upside +28.3% anchor가 있다.

2. 농심은 Shin Ramyun 글로벌 staple 구조가 강하지만,
   OPM/EPS revision과 sell-through 확인 전 Stage 3는 보류다.

3. APR은 R5의 가장 강한 구조 성공 후보 중 하나다.
   해외 매출 비중, 미국 매출 비중, 4배 이상 주가 상승이 확인된다.
   그러나 동시에 4B-watch가 반드시 붙어야 한다.

4. d’Alba는 U.S. retail talks와 IPO 후 2배 상승이 확인되지만,
   sell-through 전에는 Stage 3가 아니라 4B/event premium이다.

5. 코스맥스/한국콜마는 K-beauty ODM leverage가 좋지만,
   고객 다변화·OPM·재고/채권 안정 전 Green 금지다.

6. 아모레퍼시픽은 K-beauty macro와 회사 실적을 분리해야 한다.
   중국 둔화와 COSRX plateau가 있으면 Watch/Yellow다.

7. F&F의 TaylorMade 이벤트는 M&A optionality다.
   본업 브랜드 리레이팅이나 EPS accretion 전에는 Stage 3가 아니다.
```

한 문장으로 압축하면:

> **R5에서 진짜 Stage 3는 “K푸드·K뷰티가 핫하다”가 아니라, 반복구매·해외 채널 sell-through·ASP·OPM·재고/채권 품질이 실제 이익 체급 변화로 내려오는 순간이다.**
> **R5는 Green 후보가 있지만, viral·IPO·입점 논의·M&A optionality는 먼저 4B/Event Premium으로 분리해야 점수표가 산다.**

[1]: https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045?utm_source=chatgpt.com "Samyang Foods Set to Post Strong 2Q Earnings -- Market Talk"
[2]: https://www.ft.com/content/4218f2b8-5498-411b-81fe-e3c836868d64?utm_source=chatgpt.com "Maker of Shin instant ramen expands overseas as Korean noodles become hit"
[3]: https://www.businessinsider.com/south-korea-kim-byung-hoon-beauty-billionaire-kylie-jenner-fan-2025-7?utm_source=chatgpt.com "Meet South Korea's new millennial beauty billionaire, who counts Kylie Jenner as a fan of his skincare gadgets"
[4]: https://www.ft.com/content/6a0f7e2c-f3b9-4eb6-961c-d69af28f7183?utm_source=chatgpt.com "Kardashian endorsement of skincare gadget creates K-beauty champion"
[5]: https://www.vogue.com/article/how-k-beauty-brand-medicube-pulled-off-its-global-breakout?utm_source=chatgpt.com "How K-Beauty Brand Medicube Pulled Off Its Global Breakout"
[6]: https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/?utm_source=chatgpt.com "Korean beauty startups bet booming US demand outlasts tariff pain"
[7]: https://www.reuters.com/world/asia-pacific/s-korean-fashion-retailer-ff-hires-goldman-taylormade-acquisition-2025-07-21/?utm_source=chatgpt.com "S. Korean fashion retailer F&F hires Goldman for TaylorMade acquisition"
