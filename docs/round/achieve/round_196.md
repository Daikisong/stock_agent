좋아. 순서상 이번은 **R5 Loop 7 — 소비재·유통·브랜드 가격경로 검증 라운드**로 진행한다.

이번 R5는 R3·R4보다 분위기가 다르다. 배터리·소재는 false Green 차단이 핵심이었다면, R5는 **진짜 구조적 수출 소비재와 viral/event premium을 가르는 라운드**야. K푸드·K뷰티는 실제로 강한 글로벌 수요가 있지만, 그 안에서도 “반복소비·채널 sell-through·OPM·재고·매출채권”이 확인된 기업과 “틱톡·IPO·브랜드 열기·인수 루머”만 있는 기업을 나눠야 한다.

---

# 1. 이번 라운드 대섹터

```text
R5 = 소비재·유통·브랜드
large_sector = CONSUMER_RETAIL_BRAND
round = R5 Loop 7 / price-path validation
목표 = Stage 3 / 4B / 4C가 실제 가격경로와 맞았는지 검증하고 shadow weight 보정
```

R5의 기본 영역은 K푸드, 편의점/오프라인 유통, 이커머스, 콜드체인, K뷰티, ODM, 의류, 홈·리빙, 렌탈, 규제 소비재다. Round 40 지도에서도 R5 validation focus는 `export_growth`, `channel_expansion`, `repeat_demand`, `opm`, `inventory`, `receivables`, `recall_regulation`으로 잡혀 있다. 

Round 119 기준으로 R5에서 부족한 증거는 `viral_product`, `brand_heat`이고, 필요한 증거는 `repeat_demand`, `asp`, `channel_sell_through`, `opm`, `inventory_quality`다. Green blocker는 `fad_normalization`, `channel_stuffing`, `recall_or_regulation`이다. 

---

# 2. 대상 canonical archetype

이번 R5 Loop 7에서는 새 archetype을 늘리지 않고, 기존 R5 안에서 가격경로 검증이 필요한 축을 사용한다.

```text
EXPORT_RECURRING_CONSUMER
K_FOOD_GLOBAL_STAPLE_BRAND
K_FOOD_SINGLE_SKU_RISK
K_BEAUTY_EXPORT_DISTRIBUTION
K_BEAUTY_BRAND_US_CHANNEL
K_BEAUTY_OEM_ODM_SUPPLYCHAIN_KOREA
K_BEAUTY_RETAIL_PLATFORM
BEAUTY_DEVICE_EXPORT
RETAIL_ECOMMERCE_LOGISTICS
APPAREL_FAST_FASHION_BRAND_OEM
EVENT_PREMIUM_GOVERNANCE_OVERLAY
CHANNEL_STUFFING_INVENTORY_OVERLAY
TARIFF_IMPORT_MARGIN_OVERLAY
CHINA_CONSUMER_EXPOSURE_4C
DISCLOSURE_CONFIDENCE_CAP
```

이번 R5의 핵심 질문은 이거다.

```text
이 회사는 K푸드 / K뷰티 / 소비재 수혜주인가?
아니면 반복수요, 채널 확장, sell-through, OPM, FCF로 이익 체급이 바뀌는 회사인가?
```

---

# 3. deep sub-archetype

```text
K푸드:
- ramen export
- Shin Ramyun / premium ramen
- U.S. Costco / Walmart / Kroger channel
- repeat consumption
- overseas manufacturing
- ASP mix
- one-product dependence
- food safety / recall

K뷰티 브랜드:
- indie K-beauty
- U.S. Amazon / Ulta / Sephora / Target / Costco channel
- TikTok viral product
- offline shelf expansion
- repeat purchase
- U.S. tariff burden
- China decline
- product-cycle fade

K뷰티 ODM:
- Cosmax / Kolmar
- Foxconn of fast beauty
- brand portfolio breadth
- customer concentration
- order visibility
- inventory / receivables
- margin pass-through
- tariff cost pass-through

K뷰티 디바이스:
- Medicube / APR
- skincare device
- influencer endorsement
- overseas sales mix
- beauty-tech category expansion
- valuation crowding
- competition / regulation

유통 / 플랫폼:
- Olive Young
- global online mall
- first U.S. store
- holdco link cap
- private affiliate valuation
- listed parent discount

의류 / 브랜드:
- F&F
- TaylorMade event
- China fashion exposure
- brand cycle
- acquisition / governance event premium
```

---

# 4. 국장 신규 후보 case

## Case A — 농심 `success_candidate / K-food staple export`

```text
symbol = 004370
archetype = K_FOOD_GLOBAL_STAPLE_BRAND / EXPORT_RECURRING_CONSUMER
case_type = success_candidate
```

농심은 기존 삼양식품 대표 case를 반복하지 않고 K푸드 수출형 R5를 검증할 수 있는 좋은 후보야. 2024년 5월 FT는 농심의 신라면 2023년 매출이 1.2조 원, 약 8.83억 달러로 사상 최대였고, 그중 거의 60%가 해외에서 나왔다고 보도했다. 또한 북미 매출은 2023년에 5.38억 달러로 10% 증가했고, 농심은 2030년까지 미국 매출을 15억 달러로 키우겠다는 목표를 제시했다. ([Financial Times][1])

### stage date 후보

```text
Stage 1:
2023~2024
- K푸드 / 라면 수출 성장
- 미국·유럽 채널 확장

Stage 2:
2024-05-27
- 신라면 매출 1.2조 원
- 해외 매출 비중 약 60%
- 북미 매출 성장 및 2030년 미국 매출 목표 제시

Stage 3:
보류 또는 조건부 후보
- 반복소비와 해외 채널은 강함
- 다만 OPM, ASP, 미국 공장 가동률, EPS revision 확인 필요

Stage 4B:
없음
- 단, K푸드 수출주가 이미 valuation rerating을 크게 받았다면 4B-watch

Stage 4C:
없음
- food safety, 원가상승, 미국 channel sell-through 둔화 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음 또는 2024-05-27 Stage 2 기준 OHLC backfill 필요.

MFE_30D / 90D / 180D / 1Y / 2Y:
Stage 2 기준 backfill 가능.
Stage 3 기준은 OPM/EPS confirmation 전 보류.

MAE_30D / 90D / 180D / 1Y:
needs_ohlc_backfill

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate
rerating_result = unknown / possible_true_rerating
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

농심은 R5에서 `repeat_demand`, `overseas_channel`, `premium_mix`, `localized_manufacturing`을 올려줄 수 있다. 하지만 삼양식품처럼 제품 하나가 viral하게 폭발한 구조와 달리, 농심은 **스테디셀러 글로벌 staple** 쪽이므로 Stage 3 조건은 `수출 매출 성장 + OPM 개선 + EPS revision`까지 확인해야 한다.

---

## Case B — APR `structural_success + 4B-watch`

```text
symbol = 278470
archetype = BEAUTY_DEVICE_EXPORT / K_BEAUTY_BRAND_US_CHANNEL
case_type = structural_success + 4B-watch
```

APR은 R5에서 “좋은 구조가 맞지만 4B가 빨리 붙어야 하는” 케이스다. 2025년 10월 FT는 APR이 Medicube skincare device 성공으로 한국에서 가장 가치 있는 화장품 그룹이 됐고, 주가가 2025년 1월 이후 4배 이상 올랐으며, 시가총액이 약 60억 달러에 도달했다고 보도했다. FT는 2025년 2분기 APR 매출의 거의 80%가 해외에서 나왔고, 미국이 거의 30%를 차지했다고 정리했다. ([Financial Times][2])

이건 단순 K뷰티 테마보다 훨씬 강하다. 제품이 디바이스이고, 해외 매출 비중이 높고, 미국 매출이 실제로 커졌기 때문이다. 다만 4배 상승과 60억 달러 valuation은 명백히 4B-watch가 필요하다. FT도 경쟁 심화, 미국 관세, 유럽 규제·문화 차이, 경쟁 제품 출시 우려를 언급했다. ([Financial Times][2])

### stage date 후보

```text
Stage 1:
2024-02 IPO / Medicube beauty device story

Stage 2:
2025년 상반기
- Kylie Jenner / TikTok / U.S. expansion
- Medicube device overseas demand

Stage 3:
2025년 2Q 실적 확인 구간 후보
- 해외 매출 거의 80%
- 미국 매출 약 30%
- device category가 매출로 확인

Stage 4B:
2025-10-20
- 주가 2025년 1월 이후 4배 이상
- 시총 약 60억 달러
- K-beauty device 프리미엄 crowding

Stage 4C:
없음
- 단, 미국 sell-through 둔화, tariff margin squeeze, device 경쟁 심화 시 후보
```

### 가격경로 검증

```text
stage3_price:
2025년 2Q 실적 발표일 OHLC backfill 필요.

MFE_30D / 90D / 180D / 1Y / 2Y:
needs_ohlc_backfill
다만 2025년 1월 이후 4배 이상 상승 anchor 확인.

MAE_30D / 90D / 180D / 1Y:
needs_ohlc_backfill

below_stage3_price_flag:
needs_ohlc_backfill

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = aligned
rerating_result = true_rerating + 4B-watch
stage_failure_type = green_success 후보
```

### 교정 포인트

APR은 R5에서 `overseas_sales_mix`, `U.S._sales_mix`, `category_creation`, `OPM`, `repeat_purchase`를 올려준다. 동시에 `viral_influencer_dependence`, `competition`, `tariff_margin_squeeze`, `valuation_4B`를 강하게 붙여야 한다.

---

## Case C — d’Alba Global `overheat / 4B-watch`

```text
symbol = 483650
archetype = K_BEAUTY_BRAND_US_CHANNEL / K_BEAUTY_SINGLE_PRODUCT_RISK
case_type = overheat / 4B-watch
```

d’Alba Global은 “미국 채널 확장 기대와 IPO 후 주가 과열”을 분리하는 케이스다. Reuters는 2025년 6월 d’Alba가 Costco, Ulta Beauty, Target과 미국 매장 입점을 논의 중이라고 보도했고, d’Alba Global 주가가 전월 상장 이후 2배 이상 올랐다고 전했다. 같은 기사에서 한국은 2024년 미국 화장품 수출국 1위가 됐고, 미국 e-commerce 상위 5개 한국 화장품 브랜드 매출은 2년간 평균 71% 증가했다고 설명했다. ([Reuters][3])

하지만 `입점 논의`와 `상장 직후 2배 상승`은 Stage 3가 아니다. Stage 3는 실제 매장 sell-through, 반복구매, OPM, 재고/매출채권이 확인돼야 한다.

### stage date 후보

```text
Stage 1:
2025년 IPO / K-beauty U.S. expansion story

Stage 2:
2025-06-05
- Costco / Ulta / Target 입점 논의
- U.S. K-beauty e-commerce 성장 배경

Stage 3:
없음
- 입점 논의만으로는 부족
- sell-through, repeat order, OPM, inventory quality 확인 필요

Stage 4B:
2025-06-05
- 상장 후 한 달 만에 주가 2배 이상
- IPO + K-beauty U.S. channel 기대 과열

Stage 4C:
없음
- 단, 입점 실패, 매장 회전율 부진, tariff 부담, 재고 증가 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2025-06-05 OHLC backfill 필요.

MFE / MAE:
IPO 이후 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = price_moved_without_evidence 후보
rerating_result = event_premium / theme_overheat
stage_failure_type = should_have_been_4B_watch_not_green
```

### 교정 포인트

d’Alba는 `U.S._retail_talks`와 `confirmed_U.S._sell_through`를 분리해야 한다.

```text
입점 논의:
Stage 2 attention

매장 입점 + 반복 발주 + OPM 개선:
Stage 3 후보

상장 직후 2배:
4B-watch
```

---

## Case D — 코스맥스 / 한국콜마 `success_candidate / ODM channel leverage`

```text
symbols = 192820 / 161890
archetype = K_BEAUTY_OEM_ODM_SUPPLYCHAIN_KOREA
case_type = success_candidate
```

코스맥스와 한국콜마는 K뷰티 브랜드가 아니라 **K뷰티 supply-chain leverage**를 보는 케이스다. Reuters는 2025년 6월 한국 indie K-beauty 브랜드들이 높은 품질과 낮은 가격, 빠른 마케팅으로 미국 시장을 공략하고 있으며, 이들 중 상당수가 Cosmax와 Kolmar 같은 contract manufacturer, 즉 “fast beauty의 Foxconn”에 생산을 맡긴다고 보도했다. ([Reuters][3])

이 구조는 R5에서 꽤 좋은 Stage 2 후보다. 다만 ODM은 브랜드보다 고객 다변화와 order visibility가 강점인 대신, 브랜드 sell-through가 약해지면 발주가 바로 흔들릴 수 있다. 따라서 Stage 3는 `수주 증가`, `고객 다변화`, `OPM`, `재고/매출채권`, `미국/유럽 물량` 확인 후에 줘야 한다.

### stage date 후보

```text
Stage 1:
2024~2025
- K-beauty 미국 수출 확대
- indie brand 성장

Stage 2:
2025-06-05
- Reuters가 Cosmax / Kolmar를 K-beauty outsourcing 핵심 supply chain으로 언급
- fast beauty Foxconn 구조 확인

Stage 3:
보류
- 회사별 주문, 매출, OPM, 고객 다변화, 재고/채권 확인 필요

Stage 4B:
없음
- ODM주가 브랜드보다 뒤늦게 일괄 rerating되면 4B-watch

Stage 4C:
없음
- 고객 브랜드 성장 둔화, channel stuffing, 재고 증가, tariff cost squeeze 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2025-06-05 OHLC backfill 필요.

MFE / MAE:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate
rerating_result = unknown
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

ODM은 R5에서 좋은 구조지만, 무작정 Green을 주면 안 된다.

```text
올릴 축:
customer_diversification
order_visibility
ODM operating leverage
U.S./Europe brand portfolio
OPM improvement

내릴 축:
single hot brand dependence
receivables growth
inventory build
tariff pass-through failure
```

---

## Case E — 아모레퍼시픽 `failed_rerating / China-to-U.S. transition watch`

```text
symbol = 090430
archetype = K_BEAUTY_BRAND_US_CHANNEL / CHINA_CONSUMER_EXPOSURE_4C
case_type = failed_rerating / transition_watch
```

아모레퍼시픽은 R5에서 “기존 대형 K뷰티 브랜드가 곧바로 Green이 되는 것은 아니다”라는 케이스다. Reuters는 2025년 6월 K뷰티 브랜드의 미국 진출이 강해지고 있지만, 기존 최대 시장이던 중국 수출은 지정학과 경쟁 때문에 하락했고, COSRX처럼 아모레퍼시픽에 편입된 브랜드도 경쟁 심화와 저가 대체재 때문에 성장 plateau 조짐이 있다고 전했다. ([Reuters][3])

즉 아모레퍼시픽은 K뷰티 수출 수혜라는 큰 그림에는 들어가지만, Stage 3-Green을 주려면 중국 의존 감소, 미국/유럽 sell-through, 인수 브랜드 성장 지속, OPM 회복이 같이 확인돼야 한다.

### stage date 후보

```text
Stage 1:
2024~2025
- K-beauty 미국 수출 확대
- COSRX / Laneige / Sulwhasoo global expansion 기대

Stage 2:
2025-06-05
- K-beauty U.S. push 확인
- 다만 중국 수출 하락과 COSRX plateau 우려 동반

Stage 3:
없음
- 대형 브랜드 turnaround, OPM, 미국 sell-through 확인 전 Green 금지

Stage 4B:
없음

Stage 4C:
중국 매출 둔화 / brand growth plateau가 실적 훼손으로 확인되면 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2025-06-05 OHLC backfill 필요.

MFE / MAE:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = evidence_good_but_price_failed 후보
rerating_result = transition_watch
stage_failure_type = should_have_been_yellow_or_watch
```

### 교정 포인트

아모레퍼시픽은 R5에서 `legacy K-beauty brand`를 indie K-beauty 성장주와 분리해야 한다.

```text
K-beauty macro tailwind
≠ company-level Stage 3

Stage 3 조건:
중국 둔화 상쇄
미국/유럽 매출 성장
OPM 개선
brand mix 회복
inventory 안정
```

---

## Case F — CJ / 올리브영 노출 `success_candidate + holdco cap`

```text
symbol = 001040 또는 CJ 계열 exposure
archetype = K_BEAUTY_RETAIL_PLATFORM / STRONG_PRIVATE_PLATFORM_BUT_HOLDCO_LINK_CAP
case_type = success_candidate / holdco_link_cap
```

CJ올리브영은 K뷰티 유통 플랫폼으로는 매우 강한 구조지만, 상장 순수주가 아니라 CJ 계열·비상장 플랫폼 노출로 봐야 하므로 holdco link cap이 필요하다. Reuters는 2025년 6월 Olive Young이 올해 이르면 로스앤젤레스에 첫 미국 매장을 열 계획이라고 보도했고, K뷰티 수출이 미국에서 강하게 성장하는 가운데 Olive Young의 글로벌 온라인 플랫폼 고객이 특히 캘리포니아에 많다고 설명했다. ([Reuters][3])

### stage date 후보

```text
Stage 1:
2024~2025
- Olive Young global platform / K-beauty curation

Stage 2:
2025-06-05
- LA 첫 미국 매장 계획
- global online customer base 확인

Stage 3:
보류
- 상장 순수 노출 아님
- CJ parent에 대한 가치 반영률, 매출/OPM, 해외 매장 sell-through 확인 필요

Stage 4B:
없음
- CJ 주가가 Olive Young IPO/valuation 기대만으로 급등하면 event premium watch

Stage 4C:
없음
- 미국 매장 실패, 플랫폼 성장 둔화, private valuation discount 확대 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2025-06-05 CJ Corp / 관련주 OHLC backfill 필요.

MFE / MAE:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate / private_or_holdco_link_cap
rerating_result = unknown
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

CJ/올리브영은 R5에서 `좋은 비상장 플랫폼`과 `상장주 수익률`을 분리해야 한다.

```text
좋은 사업:
Olive Young global curation

Green 차단:
listed exposure 불명확
holdco discount
IPO event premium
```

---

## Case G — F&F `event_premium / governance-acquisition watch`

```text
symbol = 383220
archetype = APPAREL_FAST_FASHION_BRAND_OEM / EVENT_PREMIUM_GOVERNANCE_OVERLAY
case_type = event_premium / insufficient_evidence
```

F&F는 R5에서 의류 브랜드 본업보다 TaylorMade 인수 이벤트와 거버넌스 분쟁이 부각된 케이스다. 2025년 7월 Reuters는 F&F가 TaylorMade 인수를 위해 Goldman Sachs를 자문사로 선임했고, 기존 보유자인 Centroid의 별도 매각 절차에 대해 법적 대응도 준비한다고 보도했다. F&F는 2021년 TaylorMade 인수에 3,580억 원의 후순위 지분투자를 했고, 핵심 의사결정에 대한 동의권과 우선매수권을 주장했다. 해당 거래가 성사될 경우 TaylorMade 기업가치는 약 35억 달러로 거론됐다. ([Reuters][4])

이건 본업 의류 브랜드의 반복매출·OPM 개선이 아니라 M&A/event premium에 가깝다. Stage 3-Green을 주면 안 된다.

### stage date 후보

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
- acquisition event가 반복소비·OPM·FCF 체급 변화로 확인되지 않음

Stage 4B:
거래 기대만으로 급등했다면 event premium 4B-watch

Stage 4C:
거래 무산, 법적 분쟁, 투자손상, 본업 중국/브랜드 부진 확인 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
2025-07-21 OHLC backfill 필요.

MFE / MAE:
event 기준 MFE_5D / 20D / 60D 측정 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = event_premium / unknown_insufficient_evidence
rerating_result = event_premium
stage_failure_type = should_have_been_stage1_only
```

### 교정 포인트

F&F는 R5에서 `M&A optionality`를 `brand rerating`으로 착각하지 말라는 케이스다.

```text
인수 루머 / ROFR / 법적 분쟁:
event premium

Stage 3 조건:
본업 매출 회복
중국/글로벌 채널 안정
OPM / FCF 개선
인수 후 EPS accretion 확인
```

---

# 5. 이번 R5 case별 요약표

| case          | 분류                                 | Stage 3 판정 |                       4B/4C 판정 | 가격경로 1차 판단                              |
| ------------- | ---------------------------------- | ---------: | -----------------------------: | --------------------------------------- |
| 농심            | success_candidate                  |     조건부 보류 |                             없음 | K푸드 반복수요는 강하지만 OPM/EPS 확인 필요            |
| APR           | structural_success + 4B-watch      |      가능 후보 |         2025년 4배 상승으로 4B-watch | 해외 매출 비중·미국 매출 확인, valuation crowding   |
| d’Alba Global | overheat / 4B-watch                |         없음 |             IPO 후 2배는 4B-watch | 입점 논의는 Stage 2, sell-through 전 Green 금지 |
| 코스맥스/한국콜마     | success_candidate                  |         보류 |                             없음 | ODM 구조는 좋지만 order/OPM 확인 필요             |
| 아모레퍼시픽        | failed_rerating / transition watch |         없음 |      중국 둔화·COSRX plateau watch | K뷰티 macro와 회사 실적 분리                     |
| CJ/올리브영       | success_candidate + holdco cap     |         보류 |      IPO/valuation event watch | 비상장 플랫폼 노출 한계                           |
| F&F           | event_premium                      |         없음 | TaylorMade event / legal watch | M&A 이벤트는 Stage 3 아님                     |

---

# 6. 각 case별 stage date 후보 요약

```text
농심:
Stage 1 = 2023~2024 K푸드 / 라면 수출 성장
Stage 2 = 2024-05-27 신라면 해외 매출 비중·북미 성장 확인
Stage 3 = 보류 / OPM·EPS revision 확인 필요
Stage 4B = K푸드 valuation crowding 시 후보
Stage 4C = food safety / channel sell-through 둔화 시 후보

APR:
Stage 1 = 2024-02 IPO / Medicube device story
Stage 2 = 2025년 상반기 U.S. expansion / influencer adoption
Stage 3 = 2025년 2Q 실적 확인 구간 후보
Stage 4B = 2025-10-20 주가 4배, 시총 약 60억 달러
Stage 4C = tariff / competition / device fade 시 후보

d’Alba Global:
Stage 1 = 2025 IPO / K-beauty U.S. channel story
Stage 2 = 2025-06-05 Costco / Ulta / Target 입점 논의
Stage 3 = 없음
Stage 4B = 2025-06-05 상장 후 2배 이상
Stage 4C = 입점 실패 / sell-through 부진 시 후보

코스맥스/한국콜마:
Stage 1 = 2024~2025 K-beauty indie brand boom
Stage 2 = 2025-06-05 ODM supply-chain leverage 확인
Stage 3 = 보류
Stage 4B = ODM주 동반 rerating 과열 시 후보
Stage 4C = 고객 둔화 / inventory / receivables 증가 시 후보

아모레퍼시픽:
Stage 1 = K-beauty global expansion
Stage 2 = 2025-06-05 U.S. push 확인, 동시에 China/COSRX 우려
Stage 3 = 없음
Stage 4B = 없음
Stage 4C = China exposure / brand plateau가 실적 훼손 시 후보

CJ/올리브영:
Stage 1 = Olive Young global curation platform
Stage 2 = 2025-06-05 LA 첫 미국 매장 계획
Stage 3 = 보류
Stage 4B = IPO/valuation 기대 급등 시 후보
Stage 4C = 미국 매장 부진 / holdco discount 확대 시 후보

F&F:
Stage 1 = 2025-07-21 TaylorMade acquisition event
Stage 2 = 없음 또는 약한 Stage 2
Stage 3 = 없음
Stage 4B = 거래 기대 급등 시 후보
Stage 4C = 거래 무산 / 법적 분쟁 / 투자손상 시 후보
```

---

# 7. 가격경로 검증

이번 R5는 정확한 OHLC backfill 없이 수익률을 확정하면 안 된다. 특히 APR·d’Alba처럼 이미 기사에서 큰 상승이 확인된 케이스는 4B anchor는 잡을 수 있지만, Stage 3 가격과 MFE/MAE는 실적 발표일 기준 일봉이 필요하다.

| case          |             stage3_price | MFE/MAE                        | below_stage3   | peak/drawdown                |
| ------------- | -----------------------: | ------------------------------ | -------------- | ---------------------------- |
| 농심            |               Stage 3 보류 | Stage 2 기준 backfill            | N/A            | 수출 성장 이후 peak/drawdown 필요    |
| APR           | 2025년 2Q 실적 발표일 backfill | 주가 4배 anchor는 있으나 exact MFE 필요 | needs backfill | 2025 4B peak/drawdown 필요     |
| d’Alba Global |               Stage 3 없음 | IPO 이후 backfill                | N/A            | 상장 후 2배 이후 drawdown 필요       |
| 코스맥스/한국콜마     |               Stage 3 보류 | Stage 2 기준 backfill            | N/A            | ODM rerating 여부 backfill     |
| 아모레퍼시픽        |               Stage 3 없음 | Stage 2 기준 backfill            | N/A            | 중국 둔화 이후 price path 필요       |
| CJ/올리브영       |               Stage 3 없음 | CJ 계열 Stage 2 기준 backfill      | N/A            | IPO/valuation event backfill |
| F&F           |               Stage 3 없음 | M&A event 기준 backfill          | N/A            | event fade drawdown 필요       |

핵심은 이거다.

```text
R5에서 가격이 먼저 움직이는 이유는 많다.
K뷰티 viral, IPO, 인수 이벤트, 중국 리오프닝 기대, 미국 입점 기대.
하지만 Stage 3는 반복수요·sell-through·OPM·FCF로만 인정한다.
```

---

# 8. score-price alignment 판정

```text
농심:
alignment = success_candidate
K푸드 staple 구조는 좋지만 Stage 3는 OPM/EPS 확인 전 보류.

APR:
alignment = aligned + 4B-watch
해외 매출과 device demand는 강하지만 valuation crowding 감시.

d’Alba Global:
alignment = price_moved_without_evidence 후보
입점 논의와 IPO 후 2배 상승은 Stage 3가 아님.

코스맥스/한국콜마:
alignment = success_candidate
ODM leverage는 좋지만 고객 주문·OPM·재고 검증 필요.

아모레퍼시픽:
alignment = evidence_good_but_price_failed 후보
K뷰티 macro는 좋지만 legacy China exposure와 brand plateau가 걸림.

CJ/올리브영:
alignment = success_candidate + private_or_holdco_link_cap
좋은 플랫폼이지만 listed exposure가 불명확.

F&F:
alignment = event_premium
TaylorMade event는 본업 브랜드 리레이팅 증거가 아님.
```

---

# 9. 점수비중 교정

## 올릴 축

```text
repeat_demand +4
channel_sell_through +4
overseas_sales_mix +3
U.S._retail_channel_confirmed +3
OPM_improvement +4
inventory_quality +3
receivables_quality +3
brand_portfolio_breadth +2
ODM_customer_diversification +3
localized_manufacturing +2
```

R5에서 진짜 강한 건 “유행”이 아니라 **반복구매와 채널 회전**이다. 같은 매출 성장이라도 online viral보다 Costco/Ulta/Target/Sephora/Walmart 같은 채널에서 반복 발주가 확인되는 쪽이 훨씬 강하다.

## 내릴 축

```text
viral_product_only -5
brand_heat_only -4
ipo_first_month_rally -4
retail_talks_without_sell_through -3
influencer_endorsement_only -3
single_sku_dependence -4
china_exposure_without_offset -3
holdco_or_private_link_cap -3
mna_event_premium -4
tariff_margin_uncertainty -2
inventory_or_receivables_build -4
```

d’Alba, F&F, CJ/올리브영, 아모레퍼시픽 때문에 이 감점축이 필요하다.

## Green gate 강화 조건

R5 Stage 3-Green은 앞으로 이렇게 줘야 한다.

```text
필수 gate:
1. 반복구매 증거
2. 해외 매출 비중 증가
3. 채널 sell-through 확인
4. OPM 개선
5. 재고·매출채권 안정
6. ASP 또는 product mix 개선
7. 한 제품 의존도가 과하지 않음
8. tariff / regulation / recall 통과
9. 가격경로가 증거 이후 따라옴

금지:
틱톡 viral만 있음
입점 논의만 있음
IPO 직후 급등
인플루언서 endorsement만 있음
M&A 이벤트만 있음
비상장 자회사 가치만 있음
중국 둔화 상쇄 증거 없음
```

## 4B 조기감지 조건

```text
4B-watch:
Stage 3 이후 2~4배 이상 상승
상장 직후 valuation이 먼저 확장
single SKU / single device 의존도가 높음
보고서가 K-beauty/K-food macro만 반복
미국 입점 기대가 sell-through보다 먼저 가격에 반영
해외 매출은 좋지만 OPM 개선이 둔화
tariff 부담을 가격에 전가하지 못함

4B-elevated:
경쟁 제품 대거 출시
채널 확장 후 재고 증가
매출채권 증가
미국/유럽 규제비용 증가
China exposure와 U.S. expansion이 동시에 흔들림

4B-graduated:
실적 beat에도 주가 반응 둔화
신규 채널 입점이 더 이상 surprise가 아님
성장률이 normalize
```

## 4C hard gate 조건

```text
recall / food safety issue
channel stuffing
inventory build
receivables spike
single product fad collapse
U.S. tariff margin squeeze
retail channel sell-through failure
China sales collapse not offset by U.S./Europe
brand acquisition impairment
M&A event failure
privacy / data / consumer regulation issue
```

---

# 10. shadow-only 기록

이번 R5 Loop 7은 production scoring에 바로 반영하면 안 된다.

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
needs_ohlc_backfill = true
```

레포에 넣는다면 파일명은 이렇게 가는 게 자연스럽다.

```text
docs/round/round_124.md
docs/checkpoints/checkpoint_28a_round124_r5_loop7_consumer_retail_brand_price_validation.md
src/e2r/sector/round124_r5_loop7_consumer_retail_brand.py
data/e2r_case_library/cases_r5_loop7_round124.jsonl
data/sector_taxonomy/score_weight_profiles_round124_r5_loop7_v7.csv
output/e2r_round124_r5_loop7_consumer_retail_brand/
```

---

# 이번 R5 Loop 7 결론

R5는 R3·R4보다 Stage 3 후보가 더 많다. 특히 **K푸드 staple, K뷰티 device, K뷰티 ODM**은 진짜 구조 후보가 될 수 있다. 하지만 동시에 viral/IPO/event premium이 너무 많아서 Green gate를 느슨하게 주면 금방 false positive가 쌓인다.

이번 라운드의 핵심 교정은 이거다.

```text
1. K푸드는 반복소비와 해외 채널이 확인되면 Stage 2~3 후보가 될 수 있다.
   단, OPM/EPS revision 확인 전에는 보류한다.

2. K뷰티 디바이스는 강한 구조가 가능하다.
   APR처럼 해외 매출과 미국 매출이 확인되면 Stage 3 후보지만,
   4배 상승 이후에는 4B-watch가 반드시 붙어야 한다.

3. K뷰티 indie brand는 입점 논의와 sell-through를 분리해야 한다.
   d’Alba처럼 IPO 후 2배 상승은 4B-watch이지 Stage 3가 아니다.

4. ODM은 좋은 supply-chain leverage지만,
   고객 다변화·주문·OPM·재고/채권 확인 전 Green 금지다.

5. 대형 legacy K뷰티는 macro 수혜와 회사 실적을 분리해야 한다.
   중국 둔화, 브랜드 plateau, 재고 문제가 있으면 Watch/Yellow다.

6. M&A, IPO, 비상장 자회사 가치, 인플루언서 viral은 event premium이다.
   반복매출·채널 회전·FCF로 승격되기 전 Stage 3가 아니다.
```

한 문장으로 압축하면:

> **R5에서 진짜 Stage 3는 “K푸드·K뷰티가 핫하다”가 아니라, 반복구매와 채널 sell-through가 OPM·EPS·FCF로 내려오는 순간이다.**
> **R5는 Green 후보가 분명 있지만, viral·IPO·입점 논의·M&A 이벤트를 4B/watch로 분리해야 점수표가 살아난다.**

[1]: https://www.ft.com/content/4218f2b8-5498-411b-81fe-e3c836868d64?utm_source=chatgpt.com "Maker of Shin instant ramen expands overseas as Korean noodles become hit"
[2]: https://www.ft.com/content/6a0f7e2c-f3b9-4eb6-961c-d69af28f7183?utm_source=chatgpt.com "Kardashian endorsement of skincare gadget creates K-beauty champion"
[3]: https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/?utm_source=chatgpt.com "Korean beauty startups bet booming US demand outlasts tariff pain"
[4]: https://www.reuters.com/world/asia-pacific/s-korean-fashion-retailer-ff-hires-goldman-taylormade-acquisition-2025-07-21/?utm_source=chatgpt.com "S. Korean fashion retailer F&F hires Goldman for TaylorMade acquisition"
