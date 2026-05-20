순서상 이번은 **R9 Loop 8 — 모빌리티·운송·레저 가격경로 검증 라운드**다.

이번 라운드도 원시 수정주가 일봉 OHLC를 안정적으로 직접 추출하지 못한 종목은 숫자를 만들지 않았다. 대신 Reuters / FT / WSJ / MarketWatch / AP / Business Insider에 남은 **가격 anchor, 이벤트 수익률, 계약·투자·운임·관광 지표**로 계산 가능한 값은 직접 계산했다.

```text
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

---

# 1. 이번 라운드 대섹터

```text
R9 = 모빌리티·운송·레저
large_sector = MOBILITY_TRANSPORT_LEISURE
round = R9 Loop 8 / price-path validation
```

R9의 기본 검증축은 `fcf`, `hybrid_mix`, `shareholder_return`, `customer_diversification`, `freight_rate`, `tourist_mix`, `government_contract`다. R9는 완성차, 부품, 타이어, 항공, 여행·레저, 카지노·면세, 해운, 렌터카, UAM, 우주·위성통신까지 포함하지만, 핵심은 “수요 회복”이 아니라 **unit economics, FCF, hybrid mix, load factor, freight rate durability, tourist spend, safety trust**가 확인되는가다. 

Round 119 기준으로 R9에서 부족한 증거는 `robotaxi_name`, `autonomous_truck_story`, `travel_reopening`이고, 필요한 증거는 `unit_economics`, `safety`, `fleet_utilization`, `margin`, `repeat_revenue`다. Green blocker는 `safety_failure`, `utilization_weak`, `cycle_normalization`이다. 

---

# 2. 대상 canonical archetype

```text
AUTO_HYBRID_VALUEUP
AUTO_TARIFF_LOCALIZATION
AUTO_SDV_DELAY_CAPEX_OVERLAY
AUTO_PRICE_WAR_EUROPE_OVERLAY
AIRLINE_INTEGRATION_SCALE
AIRLINE_SAFETY_REGULATORY_OVERLAY
SHIPPING_FREIGHT_CYCLE
CASINO_DUTYFREE_TOURISM
TRAVEL_LEISURE_REOPENING
FLEET_UNIT_ECONOMICS_OVERLAY
PRICE_ONLY_RALLY
THESIS_BREAK_4C
```

이번 R9의 핵심 질문은 이거다.

```text
자동차·항공·해운·관광 회복 테마인가?
아니면 hybrid mix, FCF, 주주환원, 통합 시너지, 운임 지속성, tourist spend가
실제 이익 체급을 바꾸는가?
```

---

# 3. deep sub-archetype

```text
완성차 / hybrid / value-up:
- Hyundai Motor
- Kia
- hybrid sales mix
- buyback / dividend
- U.S. localization
- Georgia plant
- tariff margin hit
- EREV / pickup / hybrid production

SDV / AI mobility:
- Kia SDV delay
- Google DeepMind / Nvidia partnership
- humanoid robots
- capex burden
- EV target cut
- software revenue before Green

항공 통합:
- Korean Air + Asiana
- integration synergy
- route optimization
- LCC consolidation
- frequent-flyer integration
- safety and service trust
- large aircraft capex

항공 safety:
- Jeju Air crash
- Boeing 737-800 inspection
- consumer trust break
- booking cancellation
- hard 4C

해운:
- HMM
- Red Sea disruption
- container freight rate spike
- Freightos index
- capacity tied up
- freight normalization risk

관광 / 면세 / 카지노:
- Hotel Shilla
- Paradise
- Lotte Tour Development
- Chinese group visa-free entry
- tourist arrivals
- tourist spend
- casino drop / hold
- event premium vs actual utilization
```

---

# 4. 국장 신규 후보 case

## Case A — 현대차 `structural_success 후보 + tariff 4C-watch`

```text
symbol = 005380
case_type = structural_success 후보 + 4C-watch
archetype = AUTO_HYBRID_VALUEUP / AUTO_TARIFF_LOCALIZATION
```

### evidence

2024년 8월 28일 현대차는 2030년 글로벌 판매 555만 대, 2028년 hybrid 판매 133만 대, 2025~2027년 최대 4조 원 자사주 매입, 분기 최소 배당 2,500원, 이익 35% 주주환원, 장기 10% 이상 영업이익률 목표를 제시했다. 발표 당일 주가는 장중 최대 5% 상승했고 종가는 4.7% 올랐다. 이건 단순 자동차 테마가 아니라 **hybrid mix + shareholder return + margin target**이 같이 나온 Stage 2~3 후보 evidence다. ([Reuters][1])

2025년 9월 18일 현대차는 미국 관세 부담 때문에 2025년 영업이익률 목표를 기존 7~8%에서 6~7%로 낮췄고, 미국 판매 차량의 80% 이상을 2030년까지 현지 생산하겠다고 밝혔다. 같은 보도에서 2025년 2분기 관세 비용은 8,280억 원, 조지아 공장 생산능력은 2028년 50만 대 목표로 제시됐다. 이건 hard 4C는 아니지만, R9에서 **tariff margin 4C-watch**로 잡아야 한다. ([Reuters][2])

### stage date

```text
Stage 1:
2024년
- EV 수요 둔화 이후 hybrid 재평가
- value-up / 주주환원 기대

Stage 2:
2024-08-28
- hybrid 판매 목표 상향
- 4조 원 buyback
- 배당 확대
- 장기 OPM 10%+ 목표
- 주가 종가 +4.7%

Stage 3:
조건부 후보
- hybrid mix, FCF, buyback execution, OPM이 실제 실적에서 확인되면 Stage 3 가능

Stage 4B:
hybrid/value-up narrative로 주가가 이미 크게 rerating된 구간이면 후보

Stage 4C-watch:
2025-09-18
- tariff로 2025 OPM target 7~8% → 6~7%
- Q2 tariff cost 8,280억 원
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event returns / margin target anchors

stage3_price:
price_data_unavailable_after_deep_search
- Reuters는 2024-08-28 종가 절대값을 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

Stage2_event_MFE_1D_intraday:
+5.0%

Stage2_event_close_return:
+4.7%

2030_sales_target:
5.55M vehicles

sales_target_growth_vs_2023:
+30%

hybrid_sales_target_2028:
1.33M vehicles

hybrid_target_increase:
+40%

buyback_plan:
4.0T won

shareholder_return_policy:
35% of profit, +10pp from prior policy

tariff_margin_target_midpoint_change:
7.5% → 6.5%
relative_margin_target_cut:
(6.5 / 7.5) - 1 = -13.3%

Q2_2025_tariff_cost:
828B won

MFE_30D / 90D / 180D / 1Y:
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
rerating_result = hybrid_valueup_rerating_candidate
stage_failure_type = green_success_candidate_with_tariff_watch
```

### 교정

현대차는 R9에서 `hybrid_mix`, `shareholder_return_execution`, `operating_margin_durability`, `FCF_after_capex`를 올려준다. 다만 tariff가 margin target을 실제로 깎았으므로 `tariff_margin_cut`과 `localization_capex`는 4C-watch로 둬야 한다.

---

## Case B — 기아 `success_candidate + SDV delay / capex watch`

```text
symbol = 000270
case_type = success_candidate + evidence_good_but_price_failed
archetype = AUTO_HYBRID_VALUEUP / AUTO_SDV_DELAY_CAPEX_OVERLAY
```

### evidence

2026년 4월 9일 기아는 software-defined vehicle 출시를 기존 2027년에서 2028년으로 1년 연기했고, 2026~2029년 투자계획을 41.4조 원, 약 280억 달러로 30% 상향했다. 동시에 2030년 EV 판매 목표를 약 20% 낮춰 100만 대로 줄이고, hybrid 판매는 2030년 110만 대까지 늘리겠다고 했다. 발표 후 기아 주가는 종가 기준 5.5% 하락했고, 같은 날 KOSPI는 1.6% 하락했다. ([Reuters][3])

### stage date

```text
Stage 1:
2024~2026
- hybrid / value-up / SDV / AI mobility 기대

Stage 2:
2026-04-09
- hybrid 확대 계획
- SDV / AI 투자계획
- 그러나 SDV delay, EV target cut, capex burden 동반

Stage 3:
없음
- SDV/AI mobility는 유료 SW 매출, OTA/subscription, margin 확인 전 Green 금지

Stage 4B:
AI/SDV narrative가 가격에 먼저 반영된 구간이면 후보

Stage 4C-watch:
2026-04-09
- SDV 출시 1년 연기
- 투자계획 30% 증가
- EV 판매목표 약 20% 하향
- 주가 -5.5%
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event return / capex target anchors

stage3_price:
N/A

stage2_event_MAE_1D:
-5.5%

KOSPI_same_day_return:
-1.6%

relative_underperformance:
-5.5 - (-1.6)
= -3.9 percentage points

investment_plan:
41.4T won / $28B

investment_plan_increase:
+30%

implied_prior_investment_plan:
41.4T / 1.30
= 31.85T won

2030_EV_target:
1.0M units

EV_target_cut:
about -20%

2030_sales_target:
4.13M units

2025_sales:
3.14M units

2030_sales_target_growth_vs_2025:
4.13 / 3.14 - 1
= +31.5%

2030_hybrid_target:
1.1M units

hybrid_target_increase:
+60%

implied_prior_hybrid_target:
1.1M / 1.60
= 0.6875M units

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = hybrid_success_candidate_but_SDV_delay_watch
stage_failure_type = should_have_been_yellow_or_watch
```

### 교정

기아는 `hybrid_mix`는 올릴 수 있지만, `SDV_story_only`, `AI_mobility_capex_without_revenue`, `EV_target_cut`, `capex_burden`은 Green을 막아야 한다.

---

## Case C — 대한항공 `success_candidate / airline integration scale`

```text
symbol = 003490
case_type = success_candidate
archetype = AIRLINE_INTEGRATION_SCALE
```

### evidence

2024년 12월 12일 대한항공은 아시아나항공 인수를 완료해 63.88% 지분을 확보했다. Reuters는 이 13억 달러 거래가 4년간 경쟁당국 심사를 거쳐 완료됐고, 합병 항공그룹이 국제선 수송능력 기준 세계 12위권이 될 것이라고 보도했다. 대한항공은 중복 인력 해고 없이 노선 최적화, 단일 LCC 통합, 신규 목적지 확대, 마일리지 통합을 추진할 계획이다. ([Reuters][4])

2025년 3월 대한항공은 아시아나 인수 이후 새 브랜드를 공개했고, 아시아나는 2027년까지 자회사로 운영된 뒤 완전 통합될 예정이라고 밝혔다. Reuters는 통합 항공사가 한국 passenger capacity의 절반 이상을 차지할 수 있으며, CEO가 최근 항공사고 이후 안전과 서비스 품질을 강조했다고 전했다. ([Reuters][5])

2025년 8월에는 대한항공이 Boeing 항공기 103대, 총 362억 달러 규모를 발주했다. Business Insider는 이 주문이 대한항공 사상 최대 항공기 주문이며, Asiana 통합 이후 장거리·미주 노선 확장 전략과 연결된다고 보도했다. 이건 scale-up과 동시에 capex/lease burden watch로 봐야 한다. ([Business Insider][6])

### stage date

```text
Stage 1:
2020~2024
- Korean Air / Asiana integration 기대
- 항공산업 구조조정

Stage 2:
2024-12-12
- Asiana acquisition complete
- 63.88% stake
- 12th-largest by international capacity

Stage 3:
보류
- 통합 시너지, route optimization, load factor, yield, debt, FCF 확인 필요

Stage 4B:
통합 기대와 aircraft order가 가격에 선반영되면 후보

Stage 4C:
integration failure, safety/service issue, fuel cost shock, regulatory remedy cost, debt/capex burden 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters / Business Insider transaction anchors

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- Reuters는 대한항공 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

Asiana_stake_acquired:
63.88%

Asiana_deal_value:
$1.3B

international_capacity_rank:
12th largest

Boeing_order_value:
$36.2B

aircraft_order_count:
103 aircraft

spare_engine_purchase:
$690M

GE_engine_maintenance_contract:
$13B over 20 years

capex_scale_vs_Asiana_deal:
36.2B / 1.3B
= 27.8x

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = airline_integration_scale_watch
stage_failure_type = stage2_watch_success
```

### 교정

대한항공은 R9에서 `merger_completion`은 Stage 2로 인정할 수 있지만, Stage 3는 **integration synergy, load factor, yield, debt, FCF**가 확인된 뒤다. 항공기 대량 발주는 성장 전략이면서 동시에 capex/debt watch다.

---

## Case D — 제주항공 `hard 4C / operational safety trust break`

```text
symbol = 089590
case_type = 4C-thesis-break
archetype = AIRLINE_SAFETY_REGULATORY_OVERLAY / OPERATIONAL_TRUST_BREAK
```

### evidence

2024년 12월 30일 제주항공 주가는 전날 무안공항 사고 이후 장중 최대 15.7% 하락해 6,920원까지 떨어졌고, 상장 이후 최저가를 기록했다. Reuters는 사고로 179명이 사망했고, 제주항공 시가총액이 최대 957억 원 증발했으며, 한국 정부가 항공 운영 시스템 전반에 대한 긴급 안전 점검을 지시했다고 보도했다. ([Reuters][7])

### stage date

```text
Stage 1:
2023~2024
- LCC 여행수요 회복
- 일본/동남아 노선 회복

Stage 2:
없음
- LCC 회복은 사이클성이고 safety trust 확인 필요

Stage 3:
없음

Stage 4B:
여행수요 회복만으로 LCC주가 과열된 구간이 있으면 후보

Stage 4C:
2024-12-30
- fatal crash
- 179명 사망
- 주가 장중 -15.7%, 6,920원 record low
- operational trust hard break
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported price anchor / event return

stage3_price:
N/A

stage4c_price_anchor:
6,920원

stage4c_event_MAE_1D:
-15.7%

implied_pre_event_reference_price:
6,920 / (1 - 0.157)
= 약 8,209원

market_cap_wipeout:
95.7B won

AK_Holdings_event_MAE:
-12%

Korean_Air_event_MAE:
-1.3%

Asiana_event_MAE:
-0.8%

Hanatour_event_MAE:
-7%

Very_Good_Tour_event_MAE:
-11%

MFE:
N/A

below_stage3_price_flag:
N/A

drawdown_after_peak:
at least -15.7% on event day

Stage 4C 큰 하락 이전 포착 여부:
hard gate event itself
- 사고 이전에 수치로 포착하기 어려운 tail risk지만, 사고 발생 시 즉시 hard 4C.
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = operational_safety_trust_break
stage_failure_type = hard_4C
```

### 교정

제주항공은 R9에서 `safety_failure`를 가장 강한 4C gate로 올린다. 항공주는 travel demand가 좋아도 fatal accident가 나면 Stage 3-Green은 즉시 차단해야 한다.

---

## Case E — HMM / 해운 cycle `cyclical_success / freight-rate 4B-watch`

```text
symbol = 011200
case_type = cyclical_success
archetype = SHIPPING_FREIGHT_CYCLE
```

### evidence

2024년 7월 Hapag-Lloyd CEO는 Red Sea 우회와 아시아 항만 혼잡이 글로벌 선복의 5~9%를 묶어두고 있으며, Freightos spot container index가 6주 동안 40% 상승해 40-foot 컨테이너 평균 $5,068까지 올랐다고 말했다. Hapag-Lloyd 주식은 5월 중순 이후 7% 상승했다. 이는 HMM 같은 컨테이너 선사에 Stage 2 cycle evidence가 될 수 있다. ([Reuters][8])

2025년 2월 WSJ는 Maersk가 Red Sea disruption에 따른 운임 상승으로 2024년 4분기 순이익 20.85억 달러를 기록해 전년 4.36억 달러 손실에서 흑자전환했다고 보도했다. 같은 기사에서 shipping rates는 38%, ocean segment freight revenue는 49% 상승했고, EBIT는 전년 -9.20억 달러에서 16억 달러로 개선됐다. ([월스트리트저널][9])

### stage date

```text
Stage 1:
2024-05~07
- Red Sea disruption
- container freight rebound
- global vessel capacity tied up

Stage 2:
2024-07-03
- Freightos index +40% in six weeks
- capacity tied up 5~9%
- Hapag shares +7%

추가 Stage 2:
2025-02-06
- Maersk Q4 profit swing
- shipping rates +38%
- ocean freight revenue +49%

Stage 3:
없음
- freight-rate spike는 cycle
- multi-quarter rate floor, contract mix, FCF, capital return 확인 전 Green 금지

Stage 4B:
freight-rate spike로 해운주가 동반 급등하면 후보

Stage 4C:
Red Sea 정상화, freight normalization, container oversupply 재부각 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ freight-rate and proxy stock anchors

HMM_stage3_price:
N/A

HMM_stock_OHLC:
price_data_unavailable_after_deep_search
- Reuters/WSJ는 HMM 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

Freightos_index:
$5,068

Freightos_index_6w_return:
+40%

implied_prior_Freightos_index:
5,068 / 1.40
= 약 $3,620

global_capacity_tied_up:
5~9%

Hapag_Lloyd_proxy_stock_return:
+7% since mid-May

Maersk_Q4_2024_net_profit:
$2.085B

Maersk_Q4_2023_net_loss:
-$436M

Maersk_profit_swing:
2.085B - (-0.436B)
= +$2.521B

Maersk_shipping_rate_increase:
+38%

Maersk_ocean_freight_revenue_increase:
+49%

Maersk_EBIT_swing:
$1.6B - (-$0.92B)
= +$2.52B

MFE / MAE:
HMM stock OHLC unavailable
```

### alignment

```text
score_price_alignment = cyclical_success
rerating_result = freight_cycle_watch
stage_failure_type = stage2_watch_success
```

### 교정

HMM/해운은 R9에서 `freight_rate_up`을 Stage 3로 직접 올리면 안 된다. Stage 3는 **contract mix, FCF, dividend, deleveraging, multi-quarter freight floor** 확인 뒤다.

---

## Case F — 호텔신라 / Paradise 관광 basket `event_premium / tourism reopening watch`

```text
symbols = 008770 / 034230
case_type = success_candidate + event_premium
archetype = CASINO_DUTYFREE_TOURISM / TRAVEL_LEISURE_REOPENING
```

### evidence

2025년 3월 한국 정부는 중국 단체관광객에 대한 한시적 무비자 입국 도입 계획을 발표했다. 2024년 한국 방문객은 1,640만 명으로 전년 대비 48% 증가했고, 중국인이 28%로 가장 큰 비중을 차지했다. 정부는 2025년 방문객 1,850만 명을 목표로 제시했다. ([Reuters][10])

2025년 8월 6일 한국 정부가 2025년 9월 29일부터 2026년 6월까지 중국 단체관광객 무비자 입국을 시행한다고 밝히자, Hotel Shilla는 4.8%, Paradise는 2.9%, Hyundai Department Store는 7.1%, Hankook Cosmetics는 9.9% 상승했다. ([Reuters][11])

2025년 9월 29일 제도가 시작되면서 중국 단체관광객 3명 이상은 최대 15일간 무비자로 입국할 수 있게 됐고, Shilla Duty Free는 중국 크루즈 투어를 조직했다. 하지만 같은 기간 중국행 항공노선은 이미 105%의 pre-pandemic capacity까지 회복됐고, Reuters는 단기 여행 수요 증가는 가능하지만 항공사 수익성에는 큰 도움이 되지 않을 수 있다고 분석했다. ([Reuters][12]) ([Reuters][13])

### stage date

```text
Stage 1:
2025-03-20
- 중국 단체관광객 무비자 정책 발표
- tourist arrival recovery 기대

Stage 2:
2025-08-06
- temporary visa-free entry from 2025-09-29 to 2026-06
- Hotel Shilla +4.8%, Paradise +2.9%

Stage 3:
없음
- tourist arrivals만으로 Green 금지
- duty-free sales, tourist spend, casino drop/hold, OPM 확인 필요

Stage 4B:
2025-08-06
- 정책 발표일 tourism basket 동반 급등

Stage 4C:
tourist spend 부진, anti-Chinese rallies, capacity oversupply, low ticket price, consumption weakness 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event returns / tourism metrics

stage3_price:
N/A

Hotel_Shilla_event_MFE_1D:
+4.8%

Paradise_event_MFE_1D:
+2.9%

Hyundai_Department_event_MFE_1D:
+7.1%

Hankook_Cosmetics_event_MFE_1D:
+9.9%

2024_visitors_to_Korea:
16.4M

visitor_growth_2024:
+48%

Chinese_share_of_visitors:
28%

2025_target_visitors:
18.5M

visitor_target_growth_vs_2024:
18.5 / 16.4 - 1
= +12.8%

Korea_China_flight_capacity:
105% of pre-pandemic level

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
rerating_result = tourism_reopening_watch
stage_failure_type = stage2_watch_success
```

### 교정

호텔신라/Paradise는 `tourist_arrivals`와 `tourist_spend`를 분리해야 한다.

```text
Stage 2:
visa-free policy
arrival growth

Stage 3:
duty-free sales
casino drop / hold
hotel occupancy
OPM
FCF
```

---

## Case G — 롯데관광개발 / 관광·카지노 event `event_premium / utilization watch`

```text
symbol = 032350
case_type = event_premium / utilization_watch
archetype = CASINO_DUTYFREE_TOURISM / TRAVEL_LEISURE_REOPENING
```

### evidence

2026년 1월 FT는 한국 외국인전용 카지노·리조트 산업이 중국 관광객에 크게 의존한다고 설명하면서, Mohegan의 Inspire Resort가 성장 covenant를 충족하지 못해 Bain Capital이 프로젝트를 장악한 사례를 보도했다. FT는 한국 외국인전용 카지노 sector가 Paradise, GKL, Lotte Tour 등과 경쟁하며, tourism weakness, 정치 불안, 운영 미스가 리조트 성과를 악화시켰다고 설명했다. ([Financial Times][14])

2025년 11월에는 중국-일본 외교갈등으로 중국 크루즈선이 일본 기항을 피하고 한국으로 우회할 가능성이 커지면서, Reuters는 롯데관광개발이 20% 이상 상승했고, Yellow Balloon Tour는 24%, Shinsegae는 6% 상승했다고 보도했다. 다만 관광업계는 실제 중국 관광객 증가까지 시간이 걸릴 수 있다고 봤다. ([Reuters][15])

### stage date

```text
Stage 1:
2025-09~11
- 중국 단체관광 무비자
- 중국-일본 외교갈등에 따른 한국 관광 redirect 기대

Stage 2:
2025-11-21
- 중국 크루즈선 일본 회피 / 한국행 기대
- Lotte Tour Development +20% 이상
- Yellow Balloon +24%

Stage 3:
없음
- casino drop, hold rate, hotel occupancy, ADR, FCF 확인 전 Green 금지

Stage 4B:
2025-11-21
- 관광 redirect 기대만으로 Lotte Tour +20% 이상

Stage 4C:
utilization failure, repeat visitor 부진, political instability, casino license / refinancing risk 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters / FT reported event returns and industry risk anchors

stage3_price:
N/A

Lotte_Tour_event_MFE:
> +20%

Yellow_Balloon_event_MFE:
+24%

Shinsegae_event_MFE:
+6%

Inspire_project_value:
$1.6B

Bain_loan_called:
$275M

Mohegan_equity_investment:
>$300M

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

Stage 4B peak-before 여부:
success
- actual drop/hold/occupancy 전 +20% 이상은 4B/event premium.
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = tourism_redirect_watch
stage_failure_type = should_have_been_stage1_or_4B_watch
```

### 교정

롯데관광개발은 `tourist policy / China-Japan dispute`만으로 Stage 3 금지다. Stage 3는 **casino drop, hold rate, occupancy, ADR, FCF**가 확인될 때만 준다.

---

# 5. 이번 R9 case별 요약표

| case                    | 분류                        |                                                                    실제 가격검증 | alignment                      |
| ----------------------- | ------------------------- | -------------------------------------------------------------------------: | ------------------------------ |
| 현대차                     | structural_success 후보     | Investor Day +4.7% close; OPM midpoint 7.5→6.5, -13.3%; tariff cost 8,280억 | aligned_partial + tariff watch |
| 기아                      | success_candidate / watch |                           SDV delay 발표 -5.5%, KOSPI -1.6%, relative -3.9pp | evidence_good_but_price_failed |
| 대한항공                    | success_candidate         |              Asiana 63.88%, $1.3B; Boeing order $36.2B = Asiana deal 27.8x | success_candidate              |
| 제주항공                    | hard 4C                   |                           6,920원, -15.7%; implied prior 8,209원; 시총 957억 증발 | thesis_break                   |
| HMM / shipping cycle    | cyclical_success          | Freightos +40% to $5,068; capacity tied 5~9%; Maersk profit swing +$2.521B | cyclical_success               |
| Hotel Shilla / Paradise | event premium             |             Hotel Shilla +4.8%, Paradise +2.9%; 2025 visitor target +12.8% | event_premium                  |
| Lotte Tour / casino     | event premium             |       Lotte Tour +20%+, Yellow Balloon +24%; Inspire covenant failure risk | event_premium                  |

---

# 6. score-price alignment 판정

```text
aligned / structural_success_candidate:
- 현대차

evidence_good_but_price_failed:
- 기아 SDV delay / capex burden

success_candidate:
- 대한항공 integration scale

thesis_break:
- 제주항공 fatal crash

cyclical_success:
- HMM / Red Sea freight-rate cycle

event_premium:
- Hotel Shilla / Paradise 중국 무비자 정책
- Lotte Tour / Yellow Balloon 중국-일본 관광 redirect

price_moved_without_evidence:
- 관광·카지노 basket 중 actual tourist spend / casino drop 확인 전 급등한 구간

4B-watch:
- 관광정책 발표일
- 중국-일본 외교갈등에 따른 관광주 급등
- 해운 운임 spike
- SDV/AI mobility narrative가 실제 SW revenue 전 가격에 반영된 구간

4C-hard:
- 제주항공 fatal safety accident
```

---

# 7. 점수비중 교정

## 올릴 축

```text
hybrid_mix +5
fcf_after_capex +5
shareholder_return_execution +5
operating_margin_durability +5
localization_tariff_hedge +4
unit_economics +5
load_factor_with_yield +4
integration_synergy_realized +4
freight_contract_mix +4
tourist_spend_conversion +5
casino_drop_and_hold +5
safety_record_and_operational_trust +5
```

### 이유

현대차는 hybrid 목표 상향, 4조 원 buyback, 배당 확대, 장기 OPM 목표가 함께 나온 좋은 Stage 2~3 후보였다. 하지만 tariff가 실제 OPM target을 낮췄기 때문에, R9에서는 **좋은 구조와 margin shock을 동시에 점수화**해야 한다. ([Reuters][1])

## 내릴 축

```text
travel_reopening_only -5
freight_rate_spike_only -5
robotaxi_or_SDV_story_only -5
tourist_arrival_policy_only -5
merger_completion_without_synergy -4
EV_or_AI_mobility_theme_only -4
capex_heavy_localization_without_margin -4
safety_failure -5
tariff_margin_cut -5
utilization_weak -5
cycle_normalization -5
```

### 이유

기아는 SDV/AI mobility 계획을 제시했지만 SDV가 1년 지연되고 투자계획이 30% 늘자 주가가 -5.5% 하락했다. Hotel Shilla·Paradise·Lotte Tour는 정책/관광 이벤트에 급등했지만, actual tourist spend와 casino drop/hold 전에는 Stage 3가 아니다. ([Reuters][3])

## Green gate 강화 조건

```text
R9 Stage 3-Green 필수:
1. unit economics 확인
2. FCF after capex 확인
3. margin durability 확인
4. hybrid mix / load factor / freight contract / tourist spend 중 해당 지표 확인
5. shareholder return 또는 deleveraging 확인
6. safety / operational trust 통과
7. tariff / fuel / FX / freight normalization stress test 통과
8. 가격경로가 evidence 이후 따라옴

금지:
여행수요 회복만 있음
운임 급등만 있음
SDV/로보택시/AI mobility 스토리만 있음
중국 무비자 정책만 있음
합병 완료만 있음
안전사고 발생
마진 가이던스 하향
```

## 4B 조기감지 조건

```text
4B-watch:
hybrid/value-up 발표 후 빠른 rerating
SDV/AI mobility가 software revenue보다 먼저 가격에 반영
합병 완료 뉴스만으로 항공주 급등
Red Sea 운임 spike로 해운주 동반 급등
중국 무비자/관광정책 뉴스로 면세·카지노주 급등
중국-일본 외교갈등으로 관광주가 실제 매출 전 급등

4B-elevated:
margin guidance cut
tariff cost 증가
fuel cost 상승
freight rate peak
tourist spend가 arrivals를 못 따라감
통합비용이 시너지보다 먼저 발생
capex 부담 확대
```

## 4C hard gate 조건

```text
fatal safety accident
operational trust break
margin guidance cut with structural cause
tariff shock not offset by localization
fuel cost spike not passed through
freight rate collapse
container overcapacity
integration failure
regulatory block
tourist spend failure
casino utilization collapse
debt / capex burden
```

제주항공은 `fatal_safety_accident_hard_4C`, 현대차는 `tariff_margin_4C_watch`, 기아는 `SDV_delay_capex_watch`, HMM은 `freight_cycle_4B_and_normalization_watch`, 관광주는 `tourist_spend_before_green`으로 분리한다.

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

이번 세션에서 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉을 안정적으로 직접 확보하지 못했다. 대신 Reuters / FT / WSJ / MarketWatch / AP / Business Insider의 가격 anchor와 이벤트 수익률을 사용해 계산 가능한 부분은 직접 계산했다.

---

# 9. patch-ready 출력

## docs/round/round_141.md 요약

```md
# R9 Loop 8. Mobility / Transport / Leisure Price Validation

이번 라운드는 R9 price-validation 라운드다.

핵심 결론:
- 현대차는 hybrid mix, 4조 원 buyback, OPM target, 주주환원이 같이 나온 Stage 2~3 후보이며, 2024-08-28 종가 +4.7%로 가격 반응도 확인된다. 다만 2025 tariff로 OPM midpoint가 7.5%에서 6.5%로 내려가 -13.3% relative cut이 발생해 4C-watch가 필요하다.
- 기아는 hybrid 확대는 좋지만 SDV 지연, EV target cut, capex +30% 때문에 주가가 -5.5% 하락했다. SDV/AI mobility는 Stage 3가 아니다.
- 대한항공은 Asiana 63.88% 인수 완료로 Stage 2 integration candidate지만, integration synergy / FCF / load factor 전 Green 금지다. $36.2B Boeing order는 growth capex watch다.
- 제주항공은 fatal crash 이후 6,920원, 장중 -15.7%, 시총 957억 원 증발로 hard 4C 기준점이다.
- HMM/shipping은 Red Sea disruption으로 Freightos +40%, Maersk profit swing +$2.521B 등 cycle success가 확인되지만 structural Stage 3는 아니다.
- Hotel Shilla/Paradise는 중국 무비자 정책에 +4.8% / +2.9% 반응했지만 tourist spend / casino drop 전 Stage 3 금지다.
- Lotte Tour는 중국-일본 외교갈등에 따른 tourism redirect 기대만으로 +20% 이상 상승했다. 이는 4B/event premium이다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 141 R9 Loop 8 Mobility Transport Leisure Price Validation

## 반영 내용
- R9 Loop 8 price-validation 라운드를 추가했다.
- Hybrid/value-up, SDV delay, airline integration, safety hard 4C, freight-cycle, tourism/casino event premium을 비교했다.
- Reuters/FT/WSJ/MarketWatch/AP/Business Insider reported anchors로 가능한 MFE/MAE 및 operating metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- hybrid mix, FCF after capex, shareholder return, operating margin durability, safety trust 가중치 강화
- SDV story-only, travel reopening-only, freight-rate spike-only, tourist-arrival-only 감점 강화
- fatal safety accident hard 4C 강화
- tourism and freight cycle 4B-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r9_loop8_hyundai_hybrid_valueup_tariff_watch","symbol":"005380","company_name":"현대차","case_type":"structural_success_candidate","primary_archetype":"AUTO_HYBRID_VALUEUP","stage2_date":"2024-08-28","stage4c_date":"2025-09-18","price_validation":{"price_data_source":"Reuters reported event anchors","stage3_price":null,"stage2_event_mfe_intraday_pct":5.0,"stage2_event_close_return_pct":4.7,"sales_target_2030_mn":5.55,"sales_target_growth_pct":30,"hybrid_sales_target_2028_mn":1.33,"hybrid_target_increase_pct":40,"buyback_plan_krw_trn":4.0,"shareholder_return_pct":35,"margin_midpoint_before_pct":7.5,"margin_midpoint_after_pct":6.5,"relative_margin_cut_pct":-13.3,"q2_tariff_cost_krw_bn":828,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"aligned_partial","rerating_result":"hybrid_valueup_rerating_candidate","notes":"Hybrid/value-up supports Stage 3 candidate; tariff margin cut creates 4C-watch."}
{"case_id":"r9_loop8_kia_sdv_delay_capex_watch","symbol":"000270","company_name":"기아","case_type":"evidence_good_but_price_failed","primary_archetype":"AUTO_SDV_DELAY_CAPEX_OVERLAY","stage2_date":"2026-04-09","stage4c_date":"2026-04-09","price_validation":{"price_data_source":"Reuters reported event anchors","stage3_price":null,"stage2_event_mae_1d_pct":-5.5,"kospi_same_day_return_pct":-1.6,"relative_underperformance_pp":-3.9,"investment_plan_krw_trn":41.4,"investment_plan_increase_pct":30,"implied_prior_investment_plan_krw_trn":31.85,"ev_target_2030_mn":1.0,"ev_target_cut_pct":20,"sales_target_2030_mn":4.13,"sales_2025_mn":3.14,"sales_target_growth_pct":31.5,"hybrid_target_2030_mn":1.1,"hybrid_target_increase_pct":60,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"hybrid_success_candidate_but_SDV_delay_watch","notes":"Hybrid plan is positive, but SDV delay, EV target cut and capex burden block Green."}
{"case_id":"r9_loop8_korean_air_asiana_integration","symbol":"003490","company_name":"대한항공","case_type":"success_candidate","primary_archetype":"AIRLINE_INTEGRATION_SCALE","stage2_date":"2024-12-12","price_validation":{"price_data_source":"Reuters/Business Insider transaction anchors","stage3_price":null,"asiana_stake_pct":63.88,"asiana_deal_value_usd_bn":1.3,"international_capacity_rank":12,"boeing_order_value_usd_bn":36.2,"aircraft_order_count":103,"spare_engine_purchase_usd_mn":690,"ge_maintenance_contract_usd_bn":13,"boeing_order_vs_asiana_deal_multiple":27.8,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"airline_integration_scale_watch","notes":"Merger completion is Stage 2; integration synergy, FCF, load factor and debt/capex burden must be checked before Green."}
{"case_id":"r9_loop8_jeju_air_fatal_crash_hard_4c","symbol":"089590","company_name":"제주항공","case_type":"4c_thesis_break","primary_archetype":"AIRLINE_SAFETY_REGULATORY_OVERLAY","stage4c_date":"2024-12-30","price_validation":{"price_data_source":"Reuters reported price/event anchors","stage3_price":null,"stage4c_price_anchor":6920,"stage4c_event_mae_1d_pct":-15.7,"implied_pre_event_reference_price":8209,"market_cap_wipeout_krw_bn":95.7,"ak_holdings_mae_pct":-12,"korean_air_mae_pct":-1.3,"asiana_mae_pct":-0.8,"hanatour_mae_pct":-7,"very_good_tour_mae_pct":-11,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"operational_safety_trust_break","notes":"Fatal crash is hard 4C and blocks any travel-demand Green."}
{"case_id":"r9_loop8_hmm_red_sea_freight_cycle","symbol":"011200","company_name":"HMM","case_type":"cyclical_success","primary_archetype":"SHIPPING_FREIGHT_CYCLE","stage2_date":"2024-07-03","price_validation":{"price_data_source":"Reuters/WSJ freight-cycle anchors","stage3_price":null,"freightos_index_usd":5068,"freightos_6w_return_pct":40,"implied_prior_freightos_index_usd":3620,"capacity_tied_up_pct":"5-9","hapag_lloyd_proxy_return_pct":7,"maersk_q4_2024_net_profit_usd_bn":2.085,"maersk_q4_2023_net_loss_usd_bn":-0.436,"maersk_profit_swing_usd_bn":2.521,"maersk_shipping_rate_increase_pct":38,"maersk_ocean_freight_revenue_increase_pct":49,"maersk_ebit_swing_usd_bn":2.52,"price_validation_status":"hmm_stock_price_data_unavailable_after_deep_search"},"score_price_alignment":"cyclical_success","rerating_result":"freight_cycle_watch","notes":"Freight spike is Stage 2/cyclical; Stage 3 requires multi-quarter rate floor, contract mix, FCF and capital return."}
{"case_id":"r9_loop8_hotel_shilla_paradise_china_visa_event","symbol":"008770/034230","company_name":"호텔신라/파라다이스","case_type":"event_premium","primary_archetype":"CASINO_DUTYFREE_TOURISM","stage1_date":"2025-03-20","stage2_date":"2025-08-06","stage4b_date":"2025-08-06","price_validation":{"price_data_source":"Reuters reported event returns and tourism metrics","stage3_price":null,"hotel_shilla_event_mfe_1d_pct":4.8,"paradise_event_mfe_1d_pct":2.9,"hyundai_department_event_mfe_1d_pct":7.1,"hankook_cosmetics_event_mfe_1d_pct":9.9,"visitors_2024_mn":16.4,"visitor_growth_2024_pct":48,"chinese_share_pct":28,"target_visitors_2025_mn":18.5,"visitor_target_growth_vs_2024_pct":12.8,"korea_china_flight_capacity_vs_pre_covid_pct":105,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"tourism_reopening_watch","notes":"Visa-free tourist policy is Stage 1/2; tourist spend, duty-free sales, casino drop/hold and OPM required before Green."}
{"case_id":"r9_loop8_lotte_tour_china_japan_redirect","symbol":"032350","company_name":"롯데관광개발","case_type":"event_premium","primary_archetype":"TRAVEL_LEISURE_REOPENING","stage1_date":"2025-11-21","stage4b_date":"2025-11-21","price_validation":{"price_data_source":"Reuters/FT reported event and industry-risk anchors","stage3_price":null,"lotte_tour_event_mfe_pct":20,"yellow_balloon_event_mfe_pct":24,"shinsegae_event_mfe_pct":6,"inspire_project_value_usd_bn":1.6,"bain_loan_called_usd_mn":275,"mohegan_equity_investment_usd_mn":300,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium","rerating_result":"tourism_redirect_watch","notes":"Tourism redirect event is not Stage 3; casino drop, hold rate, occupancy, ADR and FCF required before Green."}
```

## shadow weight row 초안

```csv
archetype,unit_economics,fcf_after_capex,hybrid_mix,shareholder_return,margin_durability,localization_hedge,safety_trust,event_penalty,cycle_normalization_redteam,4b_watch_sensitivity,notes
AUTO_HYBRID_VALUEUP,+5,+5,+5,+5,+5,+4,+3,-1,+2,+4,Hyundai supports Stage 3 candidate but tariff margin cut requires 4C-watch.
AUTO_SDV_DELAY_CAPEX_OVERLAY,+2,+3,+2,+1,+3,+2,+3,-5,+4,+5,Kia SDV delay and capex hike block Green despite hybrid plan.
AIRLINE_INTEGRATION_SCALE,+4,+5,+0,+2,+4,+0,+5,-3,+3,+4,Korean Air merger is Stage 2 until synergy/load factor/FCF confirm.
AIRLINE_SAFETY_REGULATORY_OVERLAY,+0,+0,+0,+0,+0,+0,+5,-0,+5,+5,Jeju Air fatal crash is hard 4C.
SHIPPING_FREIGHT_CYCLE,+4,+5,+0,+2,+3,+0,+2,-5,+5,+5,HMM/Red Sea freight is cyclical success, not structural Green.
CASINO_DUTYFREE_TOURISM,+5,+5,+0,+1,+4,+0,+3,-5,+4,+5,Hotel Shilla/Paradise visa event needs spend/drop/hold/OPM before Green.
TRAVEL_LEISURE_REOPENING,+4,+4,+0,+1,+3,+0,+3,-5,+4,+5,Lotte Tour tourism redirect is event premium until utilization and cashflow confirm.
```

---

# 이번 R9 Loop 8 결론

R9는 Stage 3 후보가 있지만, 섹터 내부 성격이 완전히 다르다.

```text
1. 현대차는 hybrid/value-up/주주환원으로 Stage 3 후보가 될 수 있다.
   다만 tariff가 OPM target을 실제로 깎았기 때문에 4C-watch가 동시에 필요하다.

2. 기아는 hybrid 확대는 좋지만 SDV 지연, EV target cut, capex +30% 때문에 Green을 막아야 한다.
   SDV/AI mobility는 유료 SW 매출 전 Stage 3가 아니다.

3. 대한항공은 Asiana 인수 완료로 Stage 2 후보지만,
   통합 시너지·load factor·yield·FCF 전 Stage 3 금지다.

4. 제주항공 사고는 R9의 hard 4C 기준점이다.
   여행수요가 좋아도 safety failure는 모든 Green을 차단한다.

5. HMM과 해운주는 freight-rate spike가 돈이 될 수 있지만 구조적 E2R은 아니다.
   freight rate floor와 FCF 확인 전에는 cyclical_success로 둔다.

6. Hotel Shilla/Paradise/Lotte Tour는 관광정책·외교 이벤트로 가격이 먼저 움직인다.
   tourist spend, duty-free sales, casino drop/hold, occupancy, FCF 전 Stage 3 금지다.
```

한 문장으로 압축하면:

> **R9에서 진짜 Stage 3는 “자동차·항공·해운·관광이 좋아진다”가 아니라, hybrid mix·unit economics·FCF·통합 시너지·freight durability·tourist spend가 실제 이익 체급을 바꾸는 순간이다.**
> **R9는 safety failure와 cycle normalization을 가장 강한 4C gate로 둬야 한다.**

[1]: https://www.reuters.com/business/autos-transportation/hyundai-motor-targets-30-rise-sales-by-2030-it-expands-hybrid-lineup-2024-08-28/?utm_source=chatgpt.com "Hyundai targets 30% rise in sales by 2030, as it doubles hybrid lineups"
[2]: https://www.reuters.com/business/autos-transportation/hyundai-motor-ramp-up-us-output-trims-profit-margin-goal-tariff-hit-2025-09-18/?utm_source=chatgpt.com "Hyundai Motor to ramp up US output, trims profit margin goal on tariff hit"
[3]: https://www.reuters.com/business/autos-transportation/south-koreas-kia-cuts-2030-ev-target-over-20-plans-humanoid-robots-us-factory-2026-04-09/?utm_source=chatgpt.com "Kia delays launch of software-focused cars, unveils big hike to investment plans"
[4]: https://www.reuters.com/markets/deals/korean-air-completes-asiana-takeover-form-one-asias-biggest-airlines-2024-12-12/?utm_source=chatgpt.com "Korean Air completes Asiana takeover to form one of Asia's biggest airlines"
[5]: https://www.reuters.com/business/aerospace-defense/korean-air-launches-new-branding-after-13-billion-asiana-acquisition-2025-03-11/?utm_source=chatgpt.com "Korean Air launches new branding after $1.3 billion Asiana acquisition"
[6]: https://www.businessinsider.com/korean-air-giving-boeing-36-billion-boost-2025-8?utm_source=chatgpt.com "Korean Air is giving Boeing a $36 billion boost"
[7]: https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com "Jeju Air shares plummet to record low after deadly plane crash"
[8]: https://www.reuters.com/markets/hapag-lloyd-ceo-sees-solid-shipping-demand-driving-up-freight-rates-2024-07-03/?utm_source=chatgpt.com "Hapag-Lloyd CEO sees solid shipping demand driving up freight rates"
[9]: https://www.wsj.com/business/earnings/a-p-moller-maersk-swings-to-profit-as-red-sea-disruptions-boost-freight-rates-eaf183a2?utm_source=chatgpt.com "A.P. Moller-Maersk Swings to Profit as Red Sea Disruptions Boost Freight Rates"
[10]: https://www.reuters.com/world/asia-pacific/south-korea-offer-visa-free-entry-chinese-visitors-boost-tourism-2025-03-20/?utm_source=chatgpt.com "South Korea to offer visa-free entry to Chinese visitors to boost tourism"
[11]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/?utm_source=chatgpt.com "South Korea to offer visa-free entry to Chinese tourists from late September"
[12]: https://www.reuters.com/world/china/south-korea-pilot-visa-free-entry-chinese-tourist-groups-cctv-reports-2025-09-29/?utm_source=chatgpt.com "South Korea begins visa-free entry for Chinese tourist groups"
[13]: https://www.reuters.com/markets/asia/south-korea-visa-waiver-lift-travel-not-chinese-airline-profits-2025-08-26/?utm_source=chatgpt.com "South Korea visa waiver to lift travel but not Chinese airline profits"
[14]: https://www.ft.com/content/d8a84f6d-f227-4698-9e19-ff170791b8c2?utm_source=chatgpt.com "How Bain took over a $1.6bn Native American casino in South Korea"
[15]: https://www.reuters.com/world/asia-pacific/chinese-cruise-ships-look-steer-clear-japan-amid-diplomatic-dispute-2025-11-21/?utm_source=chatgpt.com "Chinese cruise ships look to steer clear of Japan amid diplomatic dispute"
