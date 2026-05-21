순서상 이번은 **R9 Loop 9 — 모빌리티·운송·레저 가격경로 검증 라운드**다.

이번 라운드는 자동차·부품·항공·해운·물류·여행을 같이 봤다. 핵심은 “수요 회복”이나 “합병/정책 이벤트”가 아니라, **unit economics, FCF, hybrid mix, load factor/yield, freight-rate durability, logistics volume, tourist spend, safety trust**가 실제 이익 체급으로 닫히는지다.

```text
round = R9 Loop 9
round_id = round_154
large_sector = MOBILITY_TRANSPORT_LEISURE
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
```

원시 수정주가 일봉 OHLC는 이번 환경에서 안정적으로 직접 확보하지 못했다. 대신 Reuters / WSJ / AP / MarketWatch가 제공한 **가격 anchor, 이벤트 수익률, 계약·투자·운임·관광 지표**로 계산 가능한 값만 계산했다.

---

# 1. 이번 라운드 대섹터

```text
R9 = 모빌리티·운송·레저
```

---

# 2. 대상 canonical archetype

```text
AUTO_HYBRID_VALUEUP
AUTO_TARIFF_MARGIN_4C_WATCH
AUTO_SDV_DELAY_CAPEX_OVERLAY
AUTO_PARTS_THERMAL_MANAGEMENT_MNA
LOGISTICS_ECOMMERCE_CONTRACT
AIRLINE_INTEGRATION_SCALE
AIRLINE_CAPEX_DEBT_WATCH
AIRLINE_SAFETY_OPERATIONAL_TRUST_4C
SHIPPING_FREIGHT_CYCLE
TOURISM_DUTYFREE_CASINO_EVENT
TRAVEL_REDIRECT_EVENT_PREMIUM
PRICE_ONLY_RALLY
EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
완성차:
- Hyundai Motor hybrid / EREV / value-up
- Kia SDV delay / EV target cut / AI mobility capex
- U.S. tariff margin hit
- Georgia localization / U.S. investment

부품·물류:
- Hanon Systems thermal management / Hankook acquisition watch
- CJ Logistics / Shinsegae e-commerce parcel partnership
- volume growth vs margin / overseas recovery

항공:
- Korean Air / Asiana integration
- Boeing + GE aircraft/engine mega-order
- integration synergy vs capex/debt burden
- Jeju Air fatal accident / consumer trust break

해운:
- HMM / container shipping cycle
- Red Sea disruption
- Freightos index
- Maersk profit swing
- rate floor vs cycle normalization

관광·레저:
- Hotel Shilla / Paradise / Hyundai Department Store
- Lotte Tour Development / Yellow Balloon
- China visa-free policy
- China-Japan diplomatic reroute event
- tourist arrivals vs tourist spend / casino drop / duty-free OPM
```

---

# 4. 국장 신규 후보 case

## Case A — 현대차 `structural_success_candidate + tariff 4C-watch`

```text
symbol = 005380
case_type = structural_success_candidate + 4C-watch
archetype = AUTO_HYBRID_VALUEUP / AUTO_TARIFF_MARGIN_4C_WATCH
```

### stage date

```text
Stage 1:
2024년
- EV 수요 둔화 이후 hybrid 재평가
- shareholder return / value-up 기대

Stage 2:
2024-08-28
- 2030 global sales target 5.55M units
- 2028 hybrid sales target 1.33M units, +40%
- 2025~2027 buyback up to 4T won
- 35% profit shareholder return policy
- shares +5% intraday, +4.7% close

Stage 3:
조건부 후보
- hybrid mix, OPM, FCF, buyback execution이 실제 실적으로 확인되면 가능

Stage 4B:
hybrid/value-up narrative로 주가가 이미 크게 rerating된 구간이면 후보

Stage 4C-watch:
2025-07-31
- U.S. tariff 15% on Korean imports including autos
- Hyundai -4.5%, Kia -6.6%

추가 4C-watch:
2026 Q4 report
- Hyundai Q4 2025 net profit -52%
- 2025 tariff cost estimated 4.1T won
- operating profit -40%
```

현대차는 2024년 8월 hybrid 확대와 주주환원 패키지를 동시에 발표했고, 당일 주가는 장중 5%, 종가 4.7% 상승했다. 이건 R9에서 단순 EV/auto theme이 아니라 **hybrid mix + buyback + margin target**이 같이 나온 강한 Stage 2~3 후보 evidence다. 다만 2025년 U.S. tariff 이벤트에서는 현대차와 기아가 각각 -4.5%, -6.6% 하락했고, 2025년에는 관세 비용이 현대차에 약 4.1조 원 부담으로 작용하며 Q4 순이익 -52%, 영업이익 -40%가 보고됐다. 이 때문에 `tariff_margin_cut`은 4C-watch로 붙인다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ reported event and financial anchors

stage3_price:
N/A

2024-08-28_event_MFE_intraday:
+5.0%

2024-08-28_event_close_return:
+4.7%

2030_sales_target:
5.55M vehicles

sales_target_growth_vs_2023:
+30%

2028_hybrid_sales_target:
1.33M vehicles

hybrid_target_increase:
+40%

buyback_plan:
4.0T won

shareholder_return_policy:
35% of profit

2025-07-31_tariff_event:
Hyundai Motor = -4.5%
Kia = -6.6%

2025_tariff_cost:
4.1T won

Q4_2025_net_profit_decline:
-52%

Q4_2025_operating_profit_decline:
-40%

Q4_2025_revenue_growth:
+0.5%

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
score_price_alignment = aligned_partial + tariff_watch
rerating_result = hybrid_valueup_rerating_candidate
stage_failure_type = green_success_candidate_with_margin_4C_watch
```

---

## Case B — 기아 `evidence_good_but_price_failed / SDV delay capex watch`

```text
symbol = 000270
case_type = evidence_good_but_price_failed + 4C-watch
archetype = AUTO_SDV_DELAY_CAPEX_OVERLAY
```

### stage date

```text
Stage 1:
2024~2026
- hybrid / SDV / AI mobility 기대
- Google DeepMind / Nvidia / humanoid robot partnership narrative

Stage 2:
2026-04-09
- SDV launch delayed from 2027 to 2028
- investment plan 2026~2029 = 41.4T won / $28B
- investment plan +30%
- 2030 EV target cut about 20% to 1M units
- 2030 hybrid target 1.1M units

Stage 3:
없음
- SDV/AI mobility narrative만으로 Green 금지
- paid software revenue, OTA/subscription, unit margin, FCF 확인 필요

Stage 4B:
AI/SDV narrative가 실제 software revenue보다 먼저 가격에 반영되면 후보

Stage 4C-watch:
2026-04-09
- SDV delay
- EV target cut
- capex burden
```

기아는 2026년 4월 SDV 출시를 2027년에서 2028년으로 1년 미뤘고, 2026~2029년 투자계획을 41.4조 원으로 30% 늘렸다. 동시에 2030년 EV 판매 목표를 약 20% 낮춰 100만 대로 조정하고, hybrid 판매 목표는 110만 대로 올렸다. 이 구조는 hybrid 쪽에는 positive지만, SDV/AI mobility를 Stage 3로 주기에는 아직 이르다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported strategy / capex anchor

stage3_price:
N/A

stage2_event_price:
price_data_unavailable_after_deep_search

investment_plan:
41.4T won / about $28B

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

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed_candidate
rerating_result = hybrid_positive_but_SDV_delay_capex_watch
stage_failure_type = should_have_been_yellow_or_watch
```

---

## Case C — CJ대한통운 `success_candidate / logistics contract but price failed`

```text
symbol = 000120
case_type = success_candidate + evidence_good_but_price_failed
archetype = LOGISTICS_ECOMMERCE_CONTRACT
```

### stage date

```text
Stage 1:
2024년
- e-commerce parcel delivery
- Shinsegae / SSG.com logistics partnership 기대

Stage 2:
2024-04
- Shinsegae와 3년 logistics partnership
- annual revenue boost about 300B won expected
- Daiwa keeps outperform but cuts target 17% to 116,000원
- shares -0.2%, 99,100원

Stage 3:
없음
- 물류계약만으로 Green 금지
- parcel volume, margin, automation efficiency, overseas recovery, FCF 확인 필요

Stage 4B:
e-commerce logistics narrative로 valuation만 먼저 확장되면 후보

Stage 4C:
domestic parcel slowdown, overseas recovery delay, labor/cost inflation, margin compression 시 후보
```

CJ대한통운은 Shinsegae Group과의 3년 logistics partnership으로 연간 약 3,000억 원 매출 증가가 기대됐지만, Daiwa는 국내 성장 둔화와 해외사업 회복 지연을 이유로 목표주가를 17% 낮춰 116,000원으로 제시했다. 보도 시점 주가는 0.2% 하락한 99,100원이었다. 즉 계약은 Stage 2 후보지만, 가격은 즉시 강하게 반응하지 않았다. ([마켓워치][3])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch reported price / target / revenue anchor

stage3_price:
N/A

stage2_price_anchor:
99,100원

stage2_event_MAE:
-0.2%

expected_annual_revenue_boost:
300B won

target_price:
116,000원

target_upside_from_stage2_price:
(116,000 / 99,100) - 1
= +17.1%

target_cut:
-17%

implied_prior_target:
116,000 / (1 - 0.17)
= 약 139,759원

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = logistics_contract_watch
stage_failure_type = stage2_watch_not_green
```

---

## Case D — 대한항공 `success_candidate / integration scale + capex watch`

```text
symbol = 003490
case_type = success_candidate + capex_watch
archetype = AIRLINE_INTEGRATION_SCALE / AIRLINE_CAPEX_DEBT_WATCH
```

### stage date

```text
Stage 1:
2020~2024
- Korean Air / Asiana integration
- 항공산업 구조조정
- Incheon hub competitiveness

Stage 2:
2024-12-12
- Korean Air completes Asiana acquisition
- 63.88% stake
- $1.3B deal
- group becomes 12th-largest by international capacity

추가 Stage 2:
2025-08-25
- Korean Air orders 103 Boeing aircraft
- $36.2B aircraft order
- $690M spare engines
- $13B GE engine maintenance contract
- total package roughly $49.9B

Stage 3:
보류
- integration synergy, load factor, yield, debt/capex burden, FCF 확인 필요

Stage 4B:
integration 기대와 aircraft order가 가격에 선반영되면 후보

Stage 4C:
integration failure, safety/service issue, fuel cost shock, capex/debt burden, regulatory remedy cost 시 후보
```

대한항공은 2024년 12월 아시아나항공 63.88% 지분 인수를 완료했고, 이 거래는 4년간 경쟁당국 심사를 거쳐 성사됐다. Reuters는 합병 항공그룹이 국제선 수송능력 기준 세계 12위권이 될 것이라고 보도했고, 2025년에는 아시아나 통합 후 신규 branding과 2027년 완전 통합 계획도 공개됐다. 이후 대한항공은 103대 Boeing 항공기, 19개 spare engines, 20년 engine maintenance를 포함한 약 500억 달러 규모 package를 발표했다. 이는 scale-up evidence이면서 동시에 capex/debt watch다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP transaction and aircraft-order anchors

stage3_price:
N/A

Korean_Air_stock_OHLC:
price_data_unavailable_after_deep_search

reason:
- Reuters/AP는 merger/order metrics는 제공하지만 대한항공 event-day OHLC anchor는 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.

Asiana_stake_acquired:
63.88%

Asiana_deal_value:
$1.3B

international_capacity_rank:
12th largest

Boeing_order_value:
$36.2B

aircraft_order_count:
103

spare_engine_purchase:
$690M

GE_engine_maintenance_contract:
$13B over 20 years

total_package:
36.2B + 0.69B + 13B
= $49.89B

aircraft_order_vs_Asiana_deal:
36.2 / 1.3
= 27.8x

total_package_vs_Asiana_deal:
49.89 / 1.3
= 38.4x

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

---

## Case E — 제주항공 `hard 4C / operational safety trust break`

```text
symbol = 089590
case_type = 4C-thesis-break
archetype = AIRLINE_SAFETY_OPERATIONAL_TRUST_4C
```

### stage date

```text
Stage 1:
2023~2024
- LCC travel recovery
- Japan / Southeast Asia leisure demand

Stage 2:
없음
- safety trust break 이후 positive stage 부여 금지

Stage 3:
없음

Stage 4C:
2024-12-30
- fatal crash
- 179 fatalities
- Jeju Air intraday -15.7%
- market cap wipeout up to 95.7B won
- tour-package cancellations doubled / bookings halved for one operator
```

제주항공은 무안공항 사고 이후 주가가 장중 15.7% 하락해 record low를 기록했고, 약 957억 원의 시가총액이 증발했다. Reuters는 이 사고로 179명이 사망했고, LCC 소비자 신뢰가 훼손될 수 있다고 보도했다. 같은 보도에서 Hanatour는 최대 7%, Very Good Tour는 최대 11% 하락했으며, 패키지 취소가 두 배로 늘고 한 여행사 booking은 절반으로 줄었다는 내용도 나왔다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event-return and travel-agency anchors

stage3_price:
N/A

Jeju_Air_event_MAE_1D:
-15.7%

market_cap_wipeout:
95.7B won

Korean_Air_event_MAE:
-1.3%

Asiana_event_MAE:
-0.8%

Hanatour_event_MAE:
-7.0%

Very_Good_Tour_event_MAE:
-11.0%

Air_Busan_event:
+15% 이상

Jin_Air / T'way:
rose intraday then fell

tour_package_cancellations:
doubled for one operator

bookings:
halved for one operator

MFE:
N/A

below_stage3_price_flag:
N/A

Stage 4C 큰 하락 이전 포착 여부:
hard gate event itself
- 사고 이전 정량 예측은 어렵지만, fatal accident 발생 즉시 hard 4C.
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = operational_safety_trust_break
stage_failure_type = hard_4C
```

---

## Case F — HMM / 해운 cycle `cyclical_success / freight-rate 4B-watch`

```text
symbol = 011200
case_type = cyclical_success
archetype = SHIPPING_FREIGHT_CYCLE
```

### stage date

```text
Stage 1:
2024-05~07
- Red Sea rerouting
- container capacity tied up
- spot freight-rate rebound

Stage 2:
2024-07-03
- Freightos spot container index +40% in six weeks to $5,068
- global vessel capacity tied up 5~9%
- Hapag-Lloyd shares +7% since mid-May

추가 Stage 2:
2025-02-06
- Maersk Q4 2024 net profit $2.085B vs prior-year loss $436M
- shipping rates +38%
- ocean freight revenue +49%
- EBIT $1.6B vs prior-year loss $920M

Stage 3:
없음
- freight-rate spike는 cycle
- HMM company-level contract mix, FCF, dividend/deleveraging 확인 전 Green 금지

Stage 4B:
freight-rate spike로 해운주가 동반 급등하면 후보

Stage 4C:
Red Sea 정상화, freight normalization, overcapacity, average freight-rate decline 시 후보
```

Red Sea 우회와 항만 혼잡은 global vessel capacity 5~9%를 묶어두며 spot rate를 밀어올렸다. Reuters는 Freightos spot container index가 6주 동안 40% 올라 $5,068이 됐다고 보도했다. WSJ도 Maersk가 Red Sea disruption으로 Q4 2024 순이익 $2.085B를 기록해 전년 $436M 손실에서 흑자전환했고, shipping rates +38%, ocean freight revenue +49%가 나왔다고 보도했다. 다만 2025년 이후 Hapag-Lloyd의 평균 운임 하락과 이익 감소 보도는 해운이 구조적 Stage 3가 아니라 cycle임을 다시 보여준다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ freight-rate and proxy-company anchors

HMM_stage3_price:
N/A

HMM_stock_OHLC:
price_data_unavailable_after_deep_search

reason:
- Reuters/WSJ는 HMM 직접 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.

Freightos_index:
$5,068

Freightos_6w_return:
+40%

implied_prior_Freightos_index:
5,068 / 1.40
= 약 $3,620

global_capacity_tied_up:
5~9%

Hapag_Lloyd_proxy_return:
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

---

## Case G — 호텔신라 / 파라다이스 / 관광 retail basket `event_premium / tourism recovery watch`

```text
symbols = 008770 / 034230 / 069960
case_type = success_candidate + event_premium
archetype = TOURISM_DUTYFREE_CASINO_EVENT
```

### stage date

```text
Stage 1:
2025-03-20
- 중국 단체관광객 무비자 정책 발표
- tourist retail / duty-free / casino recovery 기대

Stage 2:
2025-08-06
- visa-free entry from 2025-09-29 to 2026-06
- Hotel Shilla +4.8%
- Paradise +2.9%
- Hyundai Department Store +7.1%
- Hankook Cosmetics +9.9%

Stage 3:
없음
- tourist arrivals만으로 Green 금지
- duty-free sales, tourist spend, casino drop/hold, hotel occupancy, OPM 확인 필요

Stage 4B:
정책 발표일 tourism basket 동반 급등

Stage 4C:
tourist spend 부진, low-price tour mix, anti-Chinese protests, capacity oversupply, margin weakness 시 후보
```

한국은 2025년 9월 29일부터 2026년 6월까지 중국 단체관광객에게 15일 무비자 입국을 허용하는 pilot programme을 시작했다. 발표 당시 백화점·호텔·카지노·화장품 등 중국 소비 관련주가 동반 반응했고, 이후 실제 시행 시점에는 Shilla Duty Free가 중국 cruise tour를 조직하고 배달앱이 Alipay·WeChat Pay를 도입하는 등 수요 capture 시도가 나왔다. 다만 이건 Stage 2 event이며, Stage 3는 관광객 수가 아니라 **객단가·면세 매출·casino drop/hold·OPM**으로 확인해야 한다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters tourism-policy and event-return anchors

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

visa-free_stay:
up to 15 days

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

## Case H — 롯데관광개발 / Yellow Balloon `event premium / China-Japan redirect`

```text
symbols = 032350 / 104620
case_type = event_premium
archetype = TRAVEL_REDIRECT_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-11-17~21
- China-Japan diplomatic dispute
- Chinese tourists canceling Japan trips
- Korea as redirect destination

Stage 2:
2025-11-21
- Chinese cruise ships consider avoiding Japan
- Jeju stays extended
- Lotte Tour Development +20%+
- Yellow Balloon +24%
- Shinsegae +6%

Stage 3:
없음
- tourist redirect expectation만으로 Green 금지
- actual arrivals, casino drop, occupancy, ADR, FCF 확인 필요

Stage 4B:
2025-11-21
- tourism redirect expectation alone drives +20%+ rally

Stage 4C:
redirect fails, dispute fades, tourist spend weak, casino utilization weak, debt/refinancing risk 시 후보
```

중국-일본 외교갈등으로 중국 cruise operators가 일본 기항을 피하고 한국으로 우회하는 방안을 검토하면서, Reuters는 롯데관광개발이 20% 이상, Yellow Balloon이 24%, Shinsegae가 6% 올랐다고 보도했다. 다만 Reuters는 업계가 실제 중국 관광객 증가까지는 시간이 걸릴 수 있다고 조심스럽게 봤다. 이건 전형적인 travel redirect event premium이다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters event-return and tourism-redirect anchors

stage3_price:
N/A

Lotte_Tour_event_MFE:
> +20%

Yellow_Balloon_event_MFE:
+24%

Shinsegae_event_MFE:
+6%

Japan_booking_loss_example:
East Japan International Travel Service lost 80% of bookings for remainder of year

China_to_Korea_redirect:
early signs only

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

Stage 4B peak-before 여부:
success
- actual drop/occupancy/sales 전 +20% 이상은 4B/event premium.
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = tourism_redirect_watch
stage_failure_type = should_have_been_stage1_or_4B_watch
```

---

# 5. 이번 R9 case별 요약표

| case                                     | 분류                               |                                                                  실제 가격검증 | alignment                      |
| ---------------------------------------- | -------------------------------- | -----------------------------------------------------------------------: | ------------------------------ |
| 현대차                                      | structural_success + 4C-watch    |    Investor Day +4.7%; tariff event Hyundai -4.5%; 2025 tariff cost 4.1T | aligned_partial + tariff watch |
| 기아                                       | evidence_good_but_price_failed   |              SDV delay, capex +30%, EV target -20%, raw OHLC unavailable | yellow/watch                   |
| CJ대한통운                                   | success_candidate / price failed |                 99,100원, -0.2%; revenue boost 300B; target upside +17.1% | evidence_good_but_price_failed |
| 대한항공                                     | success_candidate + capex watch  |         Asiana 63.88%, $1.3B; Boeing package $49.89B = Asiana deal 38.4x | integration watch              |
| 제주항공                                     | hard 4C                          |      -15.7%; market cap wipeout 95.7B; Hanatour -7%, Very Good Tour -11% | thesis_break                   |
| HMM / shipping                           | cyclical_success                 |                   Freightos +40% to $5,068; Maersk profit swing +$2.521B | cyclical_success               |
| Hotel Shilla / Paradise / tourism retail | event premium                    | Shilla +4.8%, Paradise +2.9%, Hyundai Dept +7.1%, target visitors +12.8% | event_premium                  |
| Lotte Tour / Yellow Balloon              | event premium                    |                     Lotte Tour +20%+, Yellow Balloon +24%, Shinsegae +6% | price_moved_before_spend       |

---

# 6. score-price alignment 판정

```text
aligned / structural_success_candidate:
- 현대차 hybrid/value-up

evidence_good_but_price_failed:
- CJ대한통운
- 기아 SDV/capex watch

success_candidate:
- 대한항공 integration scale
- Hotel Shilla / Paradise tourism recovery, 단 Stage 2

thesis_break / hard 4C:
- 제주항공 fatal accident

cyclical_success:
- HMM / Red Sea freight cycle

event_premium:
- 중국 무비자 tourism basket
- Lotte Tour / Yellow Balloon China-Japan redirect event

price_moved_without_evidence:
- 관광 redirect 기대만으로 +20% 이상 상승한 tourism basket
- 정책 발표일 tourist spend 확인 전 급등한 retail/leisure basket

4B-watch:
- Lotte Tour +20%+
- Yellow Balloon +24%
- tourism policy-day basket rally
- freight-rate spike
- SDV/AI mobility narrative가 SW revenue 전 가격에 반영된 구간

4C-hard:
- 제주항공 fatal safety accident

4C-watch:
- 현대차/Kia tariff margin shock
- 기아 SDV delay / capex burden
- 대한항공 aircraft capex/debt burden
- shipping freight normalization
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
logistics_contract_margin +4
load_factor_with_yield +4
integration_synergy_realized +4
freight_contract_mix +4
tourist_spend_conversion +5
casino_drop_and_hold +5
safety_record_and_operational_trust +5
```

### 이유

현대차는 hybrid mix와 shareholder return이 동시에 확인되어 R9에서 좋은 Stage 2~3 후보가 될 수 있다. CJ대한통운은 물류계약이 있어도 가격이 실패했고, 대한항공은 합병 scale이 있어도 대형 항공기 발주가 capex/debt watch를 만든다. 따라서 R9 Green은 항상 **unit economics + FCF + safety/operational trust**로 닫아야 한다.

## 내릴 축

```text
travel_reopening_only -5
freight_rate_spike_only -5
robotaxi_or_SDV_story_only -5
tourist_arrival_policy_only -5
tourism_redirect_event_only -5
merger_completion_without_synergy -4
EV_or_AI_mobility_theme_only -4
capex_heavy_localization_without_margin -4
safety_failure -5
tariff_margin_cut -5
utilization_weak -5
cycle_normalization -5
logistics_contract_without_margin -3
```

### 이유

기아는 SDV/AI mobility 계획보다 SDV delay와 capex burden이 먼저 보였고, 관광·여행주는 무비자 정책이나 중국-일본 갈등 같은 event만으로 주가가 먼저 움직였다. HMM은 freight-rate spike가 돈이 될 수 있지만, rate floor와 FCF 확인 전에는 cycle이다. 제주항공은 safety failure가 모든 Green을 즉시 차단하는 hard 4C 기준점이다.

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
관광 redirect 기대만 있음
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
대형 항공기 발주가 growth로만 해석되고 capex 부담이 무시됨
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

## docs/round/round_154.md 요약

```md
# R9 Loop 9. Mobility / Transport / Leisure Price Validation

이번 라운드는 R9 Loop 9 price-validation 라운드다.

핵심 결론:
- Hyundai Motor는 hybrid mix, buyback, shareholder return으로 Stage 2~3 후보가 될 수 있다. 2024 Investor Day에서 +4.7% close가 확인됐다. 다만 U.S. tariff event에서 Hyundai -4.5%, 2025 tariff cost 4.1T won, Q4 net profit -52%가 확인되어 tariff margin 4C-watch가 필요하다.
- Kia는 hybrid 확대는 긍정적이지만 SDV launch delay, EV target cut, capex +30% 때문에 Stage 3가 아니라 watch다.
- CJ Logistics는 Shinsegae logistics partnership으로 annual revenue boost 300B won이 기대됐지만, shares -0.2% to 99,100원이고 target was cut 17%. Evidence good but price failed.
- Korean Air는 Asiana 63.88% acquisition과 world 12th international capacity scale로 Stage 2 후보지만, Boeing/GE package $49.89B가 Asiana deal 38.4x로 capex/debt watch를 만든다.
- Jeju Air fatal crash는 hard 4C 기준점이다. Jeju Air -15.7%, market cap wipeout 95.7B won, Hanatour -7%, Very Good Tour -11%.
- HMM/shipping은 Red Sea freight cycle로 Freightos +40%, Maersk profit swing +$2.521B가 확인되지만, structural Stage 3가 아니라 cyclical_success다.
- Hotel Shilla/Paradise/tourism retail은 China visa-free policy로 Stage 2 event candidate지만 tourist spend/OPM 전 Green 금지다.
- Lotte Tour/Yellow Balloon은 China-Japan diplomatic redirect expectation으로 +20%/+24% 급등했다. This is 4B/event premium until actual arrivals, spend, casino drop, occupancy and FCF confirm.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 154 R9 Loop 9 Mobility Transport Leisure Price Validation

## 반영 내용
- R9 Loop 9 price-validation 라운드를 추가했다.
- Hybrid/value-up, SDV delay, logistics contract, airline integration/capex, airline safety hard 4C, freight cycle, tourism visa-free event, tourism redirect event를 비교했다.
- Reuters/WSJ/AP/MarketWatch reported anchors로 가능한 MFE/MAE 및 operating metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- hybrid mix, FCF after capex, shareholder return execution, operating margin durability, logistics margin, safety trust 가중치 강화
- travel reopening-only, freight-rate spike-only, SDV story-only, tourist policy-only, tourism redirect-only 감점 강화
- fatal safety accident hard 4C 강화
- tourism and freight cycle 4B-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r9_loop9_hyundai_hybrid_valueup_tariff_watch","symbol":"005380","company_name":"현대차","case_type":"structural_success_candidate","primary_archetype":"AUTO_HYBRID_VALUEUP","stage2_date":"2024-08-28","stage4c_date":"2025-07-31","price_validation":{"price_data_source":"Reuters/WSJ reported event and financial anchors","stage3_price":null,"investor_day_mfe_intraday_pct":5.0,"investor_day_close_return_pct":4.7,"sales_target_2030_mn":5.55,"sales_target_growth_pct":30,"hybrid_sales_target_2028_mn":1.33,"hybrid_target_increase_pct":40,"buyback_plan_krw_trn":4.0,"shareholder_return_pct":35,"tariff_event_hyundai_mae_pct":-4.5,"tariff_event_kia_mae_pct":-6.6,"tariff_cost_2025_krw_trn":4.1,"q4_2025_net_profit_decline_pct":-52,"q4_2025_operating_profit_decline_pct":-40,"q4_2025_revenue_growth_pct":0.5,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"aligned_partial_tariff_watch","rerating_result":"hybrid_valueup_rerating_candidate","notes":"Hybrid/value-up supports Stage 3 candidate, but tariff margin cost creates 4C-watch."}
{"case_id":"r9_loop9_kia_sdv_delay_capex_watch","symbol":"000270","company_name":"기아","case_type":"evidence_good_but_price_failed","primary_archetype":"AUTO_SDV_DELAY_CAPEX_OVERLAY","stage2_date":"2026-04-09","stage4c_date":"2026-04-09","price_validation":{"price_data_source":"Reuters strategy/capex anchor","stage3_price":null,"investment_plan_krw_trn":41.4,"investment_plan_usd_bn":28,"investment_plan_increase_pct":30,"implied_prior_investment_plan_krw_trn":31.85,"ev_target_2030_mn":1.0,"ev_target_cut_pct":20,"sales_target_2030_mn":4.13,"sales_2025_mn":3.14,"sales_target_growth_pct":31.5,"hybrid_target_2030_mn":1.1,"hybrid_target_increase_pct":60,"implied_prior_hybrid_target_mn":0.6875,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_failed_candidate","rerating_result":"hybrid_positive_but_SDV_delay_capex_watch","notes":"Hybrid target is positive, but SDV delay, EV target cut and capex hike block Green."}
{"case_id":"r9_loop9_cj_logistics_shinsegae_contract_price_failed","symbol":"000120","company_name":"CJ대한통운","case_type":"success_candidate","primary_archetype":"LOGISTICS_ECOMMERCE_CONTRACT","stage2_date":"2024-04","price_validation":{"price_data_source":"MarketWatch reported price/target/revenue anchor","stage3_price":null,"stage2_price_anchor":99100,"stage2_event_mae_pct":-0.2,"expected_annual_revenue_boost_krw_bn":300,"target_price":116000,"target_upside_pct":17.1,"target_cut_pct":-17,"implied_prior_target":139759,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"logistics_contract_watch","notes":"Shinsegae logistics contract is Stage 2; margin, parcel volume, automation efficiency and FCF required before Green."}
{"case_id":"r9_loop9_korean_air_asiana_integration_capex_watch","symbol":"003490","company_name":"대한항공","case_type":"success_candidate","primary_archetype":"AIRLINE_INTEGRATION_SCALE","stage2_date":"2024-12-12","price_validation":{"price_data_source":"Reuters/AP transaction and aircraft-order anchors","stage3_price":null,"asiana_stake_pct":63.88,"asiana_deal_value_usd_bn":1.3,"international_capacity_rank":12,"boeing_order_value_usd_bn":36.2,"aircraft_order_count":103,"spare_engine_purchase_usd_mn":690,"ge_engine_maintenance_contract_usd_bn":13,"total_package_usd_bn":49.89,"aircraft_order_vs_asiana_deal_multiple":27.8,"total_package_vs_asiana_deal_multiple":38.4,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"airline_integration_scale_watch","notes":"Merger completion is Stage 2; synergy/load factor/yield/FCF and capex burden determine Stage 3."}
{"case_id":"r9_loop9_jeju_air_fatal_crash_hard_4c","symbol":"089590","company_name":"제주항공","case_type":"4c_thesis_break","primary_archetype":"AIRLINE_SAFETY_OPERATIONAL_TRUST_4C","stage4c_date":"2024-12-30","price_validation":{"price_data_source":"Reuters reported event-return and travel-agency anchors","stage3_price":null,"jeju_air_event_mae_1d_pct":-15.7,"market_cap_wipeout_krw_bn":95.7,"korean_air_mae_pct":-1.3,"asiana_mae_pct":-0.8,"hanatour_mae_pct":-7.0,"very_good_tour_mae_pct":-11.0,"air_busan_mfe_pct":15.0,"tour_package_cancellations":"doubled_for_one_operator","bookings":"halved_for_one_operator","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"operational_safety_trust_break","notes":"Fatal crash is hard 4C and blocks any travel-demand Green."}
{"case_id":"r9_loop9_hmm_red_sea_shipping_cycle","symbol":"011200","company_name":"HMM / container shipping cycle","case_type":"cyclical_success","primary_archetype":"SHIPPING_FREIGHT_CYCLE","stage2_date":"2024-07-03","price_validation":{"price_data_source":"Reuters/WSJ freight-rate and proxy-company anchors","stage3_price":null,"freightos_index_usd":5068,"freightos_6w_return_pct":40,"implied_prior_freightos_index_usd":3620,"capacity_tied_up_pct":"5-9","hapag_lloyd_proxy_return_pct":7,"maersk_q4_2024_net_profit_usd_bn":2.085,"maersk_q4_2023_net_loss_usd_bn":-0.436,"maersk_profit_swing_usd_bn":2.521,"maersk_shipping_rate_increase_pct":38,"maersk_ocean_freight_revenue_increase_pct":49,"maersk_ebit_swing_usd_bn":2.52,"price_validation_status":"hmm_stock_price_data_unavailable_after_deep_search"},"score_price_alignment":"cyclical_success","rerating_result":"freight_cycle_watch","notes":"Freight spike is Stage 2/cyclical; Stage 3 requires contract mix, rate floor, FCF and capital return."}
{"case_id":"r9_loop9_tourism_visa_free_retail_casino_event","symbol":"008770/034230/069960","company_name":"호텔신라/파라다이스/현대백화점","case_type":"event_premium","primary_archetype":"TOURISM_DUTYFREE_CASINO_EVENT","stage2_date":"2025-08-06","stage4b_date":"2025-08-06","price_validation":{"price_data_source":"Reuters tourism-policy and event-return anchors","stage3_price":null,"hotel_shilla_event_mfe_1d_pct":4.8,"paradise_event_mfe_1d_pct":2.9,"hyundai_department_event_mfe_1d_pct":7.1,"hankook_cosmetics_event_mfe_1d_pct":9.9,"visitors_2024_mn":16.4,"visitor_growth_2024_pct":48,"chinese_share_pct":28,"target_visitors_2025_mn":18.5,"target_growth_vs_2024_pct":12.8,"visa_free_stay_days":15,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"tourism_retail_recovery_watch","notes":"Visa-free policy is Stage 2/event; tourist spend, duty-free sales, casino drop/hold and OPM required before Green."}
{"case_id":"r9_loop9_lotte_tour_china_japan_redirect_event","symbol":"032350/104620","company_name":"롯데관광개발/Yellow Balloon","case_type":"event_premium","primary_archetype":"TRAVEL_REDIRECT_EVENT_PREMIUM","stage2_date":"2025-11-21","stage4b_date":"2025-11-21","price_validation":{"price_data_source":"Reuters tourism-redirect event anchors","stage3_price":null,"lotte_tour_event_mfe_pct":20,"yellow_balloon_event_mfe_pct":24,"shinsegae_event_mfe_pct":6,"japan_booking_loss_example_pct":80,"redirect_status":"early_signs_only","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium","rerating_result":"tourism_redirect_watch","notes":"China-Japan redirect expectation drove price before actual arrivals, occupancy, casino drop, ADR and FCF."}
```

## shadow weight row 초안

```csv
archetype,unit_economics,fcf_after_capex,hybrid_mix,shareholder_return,margin_durability,localization_hedge,logistics_margin,safety_trust,event_penalty,cycle_normalization_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
AUTO_HYBRID_VALUEUP,+5,+5,+5,+5,+5,+4,+0,+3,-1,+2,+4,+4,Hyundai supports Stage 3 candidate but tariff margin shock requires 4C-watch.
AUTO_TARIFF_MARGIN_4C_WATCH,+3,+5,+3,+2,+5,+5,+0,+2,-2,+5,+3,+5,Tariff cost can override hybrid/value-up if margin durability fails.
AUTO_SDV_DELAY_CAPEX_OVERLAY,+2,+3,+2,+1,+3,+2,+0,+3,-5,+4,+5,+4,Kia SDV delay and capex hike block Green despite hybrid plan.
LOGISTICS_ECOMMERCE_CONTRACT,+4,+5,+0,+1,+5,+0,+5,+2,-3,+3,+3,+3,CJ Logistics contract needs margin, volume and FCF; price failed on event.
AIRLINE_INTEGRATION_SCALE,+4,+5,+0,+2,+4,+0,+0,+5,-3,+3,+4,+4,Korean Air merger is Stage 2 until synergy/load factor/yield/FCF confirm.
AIRLINE_CAPEX_DEBT_WATCH,+2,+5,+0,+1,+3,+0,+0,+4,-4,+4,+4,+4,Large aircraft order is growth plus capex/debt watch.
AIRLINE_SAFETY_OPERATIONAL_TRUST_4C,+0,+0,+0,+0,+0,+0,+0,+5,0,+5,+5,+5,Jeju Air fatal crash is hard 4C.
SHIPPING_FREIGHT_CYCLE,+4,+5,+0,+2,+3,+0,+0,+2,-5,+5,+5,+4,HMM/Red Sea freight is cyclical success, not structural Green.
TOURISM_DUTYFREE_CASINO_EVENT,+5,+5,+0,+1,+4,+0,+0,+3,-5,+4,+5,+4,Visa-free tourism event needs spend/drop/hold/OPM before Green.
TRAVEL_REDIRECT_EVENT_PREMIUM,+4,+4,+0,+1,+3,+0,+0,+3,-5,+4,+5,+4,Lotte Tour redirect rally is event premium until utilization and cashflow confirm.
```

---

# 이번 R9 Loop 9 결론

R9는 **좋은 Stage 2 후보가 많지만, Green은 숫자로 닫히기 전까지 늦게 줘야 하는 섹터**다.

```text
1. 현대차는 hybrid/value-up/주주환원으로 Stage 3 후보가 될 수 있다.
   하지만 tariff가 실제 손익을 때렸기 때문에 margin 4C-watch가 동시에 필요하다.

2. 기아는 hybrid 확대는 긍정적이지만,
   SDV delay, EV target cut, capex +30% 때문에 Green을 막아야 한다.

3. CJ대한통운은 물류계약이 있어도 가격이 실패했다.
   물류는 volume보다 margin과 FCF가 Stage 3다.

4. 대한항공은 Asiana 인수 완료로 Stage 2 후보지만,
   Boeing/GE mega-order는 성장전략인 동시에 capex/debt watch다.

5. 제주항공 사고는 R9 hard 4C 기준점이다.
   여행수요가 좋아도 fatal accident는 모든 Green을 차단한다.

6. HMM과 해운은 freight-rate spike가 돈이 될 수 있지만 구조적 E2R은 아니다.
   rate floor와 FCF 확인 전에는 cyclical_success다.

7. Hotel Shilla/Paradise/tourism retail은 중국 무비자 정책 수혜 후보지만,
   tourist spend와 OPM 전에는 event premium이다.

8. Lotte Tour/Yellow Balloon은 China-Japan redirect 기대만으로 급등했다.
   실제 arrivals, occupancy, casino drop, FCF 전에는 4B/event premium이다.
```

한 문장으로 압축하면:

> **R9에서 진짜 Stage 3는 “자동차·항공·해운·관광이 좋아진다”가 아니라, hybrid mix·unit economics·FCF·통합 시너지·freight durability·tourist spend가 실제 이익 체급을 바꾸는 순간이다.**
> **R9는 safety failure와 cycle normalization을 가장 강한 4C gate로 둬야 한다.**

[1]: https://www.reuters.com/business/autos-transportation/hyundai-motor-targets-30-rise-sales-by-2030-it-expands-hybrid-lineup-2024-08-28/?utm_source=chatgpt.com "Hyundai targets 30% rise in sales by 2030, as it doubles hybrid lineups"
[2]: https://www.reuters.com/business/autos-transportation/south-koreas-kia-cuts-2030-ev-target-over-20-plans-humanoid-robots-us-factory-2026-04-09/?utm_source=chatgpt.com "Kia delays launch of software-focused cars, unveils big hike to investment plans"
[3]: https://www.marketwatch.com/story/cj-logistics-set-to-gain-from-stronger-ties-with-retailer-shinsegae-market-talk-5d3e0c7a?utm_source=chatgpt.com "CJ Logistics Set to Gain From Stronger Ties With Retailer Shinsegae -- Market Talk"
[4]: https://www.reuters.com/markets/deals/korean-air-completes-asiana-takeover-form-one-asias-biggest-airlines-2024-12-12/?utm_source=chatgpt.com "Korean Air completes Asiana takeover to form one of Asia's biggest airlines"
[5]: https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com "Jeju Air shares plummet to record low after deadly plane crash"
[6]: https://www.reuters.com/markets/hapag-lloyd-ceo-sees-solid-shipping-demand-driving-up-freight-rates-2024-07-03/?utm_source=chatgpt.com "Hapag-Lloyd CEO sees solid shipping demand driving up freight rates"
[7]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/?utm_source=chatgpt.com "South Korea to offer visa-free entry to Chinese tourists from late September"
[8]: https://www.reuters.com/world/asia-pacific/chinese-cruise-ships-look-steer-clear-japan-amid-diplomatic-dispute-2025-11-21/?utm_source=chatgpt.com "Chinese cruise ships look to steer clear of Japan amid diplomatic dispute"
