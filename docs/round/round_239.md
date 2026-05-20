순서상 이번은 **R9 Loop 10 — 모빌리티·운송·레저 가격경로 검증 라운드**다.

이번 R9는 지난 라운드의 현대차 hybrid·대한항공·HMM 반복을 줄이고, **미래모빌리티 capex, 자동차부품 품질 리스크, 철도 수출, LCC 장거리 노선, LCC 통합, dry bulk/shipping, 관광 reroute, 항공 safety hard gate**를 섞어서 본다.

```text
round = R9 Loop 10
round_id = round_167
large_sector = MOBILITY_TRANSPORT_LEISURE
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
```

이번 환경에서는 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC를 안정적으로 직접 확보하지 못했다. 대신 Reuters / MarketWatch / WSJ가 제공한 **가격 anchor, 이벤트 수익률, 계약금액, 투자금액, 항공기·열차·선박 수, 수요·안전·관광 지표**로 계산 가능한 값만 계산했다.

---

# 1. 이번 라운드 대섹터

```text
R9 = 모빌리티·운송·레저
```

R9의 Stage 3는 “자동차·항공·철도·관광 수요가 좋아진다”가 아니다. **unit economics, FCF after capex, utilization, load factor/yield, contract delivery, safety trust, tourist spend**가 실제 이익으로 닫히는 순간이다.

---

# 2. 대상 canonical archetype

```text
FUTURE_MOBILITY_AI_ROBOTICS_CAPEX
AUTO_PARTS_QUALITY_RECALL_4C
RAIL_EXPORT_ORDER_TO_DELIVERY
LCC_LONG_HAUL_ROUTE_ALLOCATION
LCC_CONSOLIDATION_INTEGRATION
SHIPPING_DRY_BULK_CYCLE
TOURISM_REDIRECT_EVENT_PREMIUM
AIRLINE_SAFETY_OPERATIONAL_TRUST_4C
PRICE_ONLY_RALLY
EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
미래모빌리티:
- Hyundai / Kia
- Saemangeum AI / robotics / hydrogen infrastructure
- Nvidia AI chip allocation
- Boston Dynamics Atlas
- robotics production capacity
- labor union / domestic production displacement risk

자동차부품:
- Hyundai Mobis
- HL Mando
- ICCU defect / EV recall
- ADAS / chassis / thermal / electrification parts
- quality cost / reputation cost

철도 수출:
- Hyundai Rotem
- Morocco ONCF 110 urban trains
- 2030 World Cup transport expansion
- concessionary financing
- delivery / margin / working capital before Green

LCC / 항공:
- T’way Air Europe routes
- Korean Air-Asiana merger remedy
- Jin Air + Air Busan + Air Seoul integration
- long-haul LCC opportunity vs aircraft lease / crew / maintenance cost
- LCC consolidation vs safety trust

해운:
- Pan Ocean
- dry bulk / LNG carrier fleet addition
- freight rate cycle
- operating profit forecast vs actual rate floor

관광·레저:
- Lotte Tour Development
- Yellow Balloon
- Shinsegae
- China-Japan diplomatic dispute redirect
- actual arrivals / casino drop / hotel occupancy before Green

안전:
- Jeju Air fatal crash
- consumer trust break
- B737-800 inspections
- travel-agency cancellation / booking shock
```

---

# 4. 국장 신규 후보 case

## Case A — 현대차·기아 `event_premium + future-mobility capex watch`

```text
symbols = 005380 / 000270
case_type = success_candidate + event_premium + labor_capex_watch
archetype = FUTURE_MOBILITY_AI_ROBOTICS_CAPEX
```

### stage date

```text
Stage 1:
2025~2026
- AI factory / autonomous driving / robotics / hydrogen infrastructure 기대
- Boston Dynamics Atlas production version
- Nvidia AI chip allocation

Stage 2:
2026-02-25
- Hyundai Motor Group potential 10T won Saemangeum investment report
- robotics, AI data center, hydrogen infrastructure
- Hyundai shares +10.5%
- Kia shares +15%

Stage 3:
없음
- 투자·AI·robotics headline만으로 Green 금지
- robot shipment, paid software, utilization, FCF, margin 확인 필요

Stage 4B:
2026-02-25
- 실제 매출 전 현대차 +10.5%, 기아 +15%
- future-mobility event premium

Stage 4C-watch:
2026-01-22
- Hyundai union warns against humanoid robots without labor-management agreement
- employment shock / domestic production displacement concern
```

현대차그룹은 새만금 지역에 5년간 약 10조 원을 투자해 robotics, AI data center, hydrogen infrastructure를 구축할 수 있다는 보도만으로 현대차가 10.5%, 기아가 15% 급등했다. Reuters는 이 계획이 기존 2026~2030년 국내 투자 125.2조 원, Nvidia AI chip 최대 50,000개 조달, AI factory 구축, 2028년 humanoid robot 30,000대 생산능력 목표와 연결된다고 보도했다. 다만 노조는 humanoid robot 도입이 고용 충격을 만들 수 있다며 사전 합의 없이는 도입을 허용하지 않겠다고 경고했다. 이는 Stage 2 future-mobility capex 후보이지만, 실제 robot shipment·software revenue·FCF 전에는 Green이 아니다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported investment / event-return / labor-risk anchors

stage3_price:
N/A

Hyundai_event_MFE_1D:
+10.5%

Kia_event_MFE_1D:
+15.0%

Saemangeum_investment_report:
10T won / about $7B over five years

Hyundai_group_domestic_investment_plan_2026_2030:
125.2T won

Nvidia_AI_chip_allocation:
up to 50,000 chips

robotics_capacity_target:
30,000 robot units annually by 2028

Georgia_factory_capacity_target:
500,000 vehicles annually by 2028

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- 실제 robot/software 매출 전 +10~15% 급등은 4B/event premium.
```

### alignment

```text
score_price_alignment = event_premium_success_candidate
rerating_result = future_mobility_capex_watch
stage_failure_type = stage2_event_not_green
```

---

## Case B — 현대모비스 `4C-watch / auto-parts quality recall`

```text
symbol = 012330
case_type = 4C-watch / evidence_good_but_quality_failed
archetype = AUTO_PARTS_QUALITY_RECALL_4C
```

### stage date

```text
Stage 1:
2024
- EV parts / electrification / ADAS supplier narrative
- Hyundai-Kia electrification value chain

Stage 2:
없음
- 품질 리스크가 먼저 확인된 구간

Stage 3:
없음
- EV component exposure만으로 Green 금지

Stage 4C-watch:
2024-05
- recurring ICCU quality issue
- Hyundai / Kia EV recall in Korea and U.S.
- Kiwoom downgrades Hyundai Mobis
- target price cut 12% to 265,000원
- shares -0.7% to 225,500원
```

현대모비스는 EV 부품 exposure만 보면 R9 후보처럼 보이지만, Integrated Control Charging Unit, 즉 ICCU 결함 반복이 품질 RedTeam을 만든다. WSJ/MarketWatch Market Talk는 Kiwoom이 현대모비스를 buy에서 outperform으로 낮추고 target을 12% 낮춘 265,000원으로 제시했다고 전했다. 같은 코멘트에서 Hyundai/Kia가 ICCU 결함으로 한국과 미국에서 EV recall을 진행했으며, 현대모비스 주가는 0.7% 하락한 225,500원이었다고 보도됐다. ([월스트리트저널][2])

### 실제 가격경로 검증

```text
price_data_source:
WSJ / MarketWatch Market Talk price and recall-risk anchor

stage3_price:
N/A

event_price:
225,500원

event_MAE:
-0.7%

target_price:
265,000원

target_cut:
-12%

implied_prior_target:
265,000 / 0.88
= 약 301,136원

target_upside_from_event_price:
(265,000 / 225,500) - 1
= +17.5%

recall_issue:
Integrated Control Charging Unit defect

affected_parent_customers:
Hyundai Motor / Kia EV recall in Korea and U.S.

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- 품질 이슈가 earnings/reputation risk로 명시되어 4C-watch 가능.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = auto_parts_quality_recall_watch
stage_failure_type = should_have_been_yellow_or_red
```

---

## Case C — 현대 로템 철도부문 `success_candidate / rail export order`

```text
symbol = 064350
case_type = success_candidate
archetype = RAIL_EXPORT_ORDER_TO_DELIVERY
```

### stage date

```text
Stage 1:
2024~2025
- Morocco rail expansion
- 2030 World Cup transport infrastructure
- Korean rail export platform

Stage 2:
2025-02-26
- Morocco ONCF order
- Hyundai Rotem wins around 2.2T won / $1.54B order
- 110 urban / double-decker trains
- largest railway-business order for Hyundai Rotem

Stage 3:
보류
- order headline은 강함
- delivery schedule, margin, working capital, cash collection 확인 전 Green 금지

Stage 4B:
철도 수출 headline로 주가가 먼저 과열되면 후보

Stage 4C:
concessionary financing delay, delivery delay, cost overrun, FX/margin deterioration 시 후보
```

현대 로템은 R9에서 방산이 아니라 **철도 수출**로도 Stage 2 후보가 된다. Reuters는 Morocco 국영 철도 운영사 ONCF가 168대 열차를 구매하는 29억 달러 프로그램에서 현대 로템이 110대 urban trains, 약 2.2조 원·15.4억 달러 규모의 주문을 따냈고, 이는 현대 로템 철도사업부 역대 최대 수주라고 보도했다. 이 계약은 Morocco가 2030년 월드컵을 앞두고 고속철·도시철도망을 확장하는 계획과 연결된다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters contract evidence

stage3_price:
N/A

Hyundai_Rotem_stock_OHLC:
price_data_unavailable_after_deep_search

Morocco_total_train_purchase:
168 trains

Morocco_total_program_value:
$2.9B

Hyundai_Rotem_order_value:
2.2T won / $1.54B

Hyundai_Rotem_train_count:
110 urban trains

Hyundai_order_share_of_total_program:
1.54 / 2.9
= 53.1%

other_orders:
Alstom 18 high-speed trains
CAF 40 intercity trains

Morocco_network_expansion_target:
43 cities / 87% of population by 2040

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = rail_export_order_watch
stage_failure_type = stage2_watch_success
```

---

## Case D — T’way Air `success_candidate / long-haul LCC route allocation`

```text
symbol = 091810
case_type = success_candidate
archetype = LCC_LONG_HAUL_ROUTE_ALLOCATION
```

### stage date

```text
Stage 1:
2024-02~03
- Korean Air-Asiana merger remedy
- profitable Europe route transfer to T’way
- long-haul LCC differentiation

Stage 2:
2024-03-07
- T’way receives Paris, Rome, Barcelona, Frankfurt routes
- Korean Air to lease five A330-200 aircraft
- Korean Air to provide 100 pilots and maintenance support
- T’way expects 30~40% growth in 2024

Stage 3:
없음
- route allocation만으로 Green 금지
- load factor, yield, aircraft lease cost, crew cost, fuel hedge, on-time operation 확인 필요

Stage 4B:
장거리 LCC 기대가 실적보다 먼저 가격에 반영되면 후보

Stage 4C:
Europe route underutilization, fuel cost, crew shortage, safety/service issue, Korean Air support 종료 시 후보
```

T’way Air는 Korean Air-Asiana merger remedy의 수혜를 받은 Stage 2 후보로 볼 수 있다. Reuters는 T’way가 Paris, Rome, Barcelona, Frankfurt 노선을 받았고, Korean Air가 A330-200 5대와 100명의 조종사, maintenance support를 제공한다고 보도했다. T’way 경영진은 이 노선들이 crowded LCC market에서 장거리 carrier로 차별화할 rare opportunity라며 2024년 30~40% 성장을 예상했다. 하지만 route allocation은 아직 Stage 3가 아니다. 실제 load factor, yield, lease cost, crew cost, fuel cost를 봐야 한다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters route-allocation evidence

stage3_price:
N/A

Tway_stock_OHLC:
price_data_unavailable_after_deep_search

new_Europe_routes:
Paris / Rome / Barcelona / Frankfurt

Korean_Air_support:
5 A330-200 aircraft lease
100 pilots
maintenance support

growth_expectation_2024:
+30~40%

existing_A330_300_count:
3 aircraft

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = long_haul_LCC_route_watch
stage_failure_type = stage2_watch_success
```

---

## Case E — Jin Air / Air Busan / Air Seoul 통합 `success_candidate / LCC consolidation`

```text
symbols = 272450 / 298690 / Asiana LCC exposure
case_type = success_candidate
archetype = LCC_CONSOLIDATION_INTEGRATION
```

### stage date

```text
Stage 1:
2024-11~12
- Korean Air-Asiana merger
- LCC consolidation expectation
- Jin Air + Air Busan + Air Seoul single brand plan

Stage 2:
2024-11-29
- Korean Air says Jin Air will absorb Asiana’s Air Busan and Air Seoul
- combined LCC fleet around 58 aircraft
- Jeju Air 42 aircraft, T’way 39 aircraft
- combined LCC operated 8% of Korea domestic/international capacity in November

Stage 3:
없음
- 통합계획만으로 Green 금지
- integration cost, route optimization, load factor/yield, safety/service quality 확인 필요

Stage 4B:
LCC consolidation 기대만으로 Jin Air/Air Busan이 먼저 급등하면 후보

Stage 4C:
integration delay, competition remedy, safety incident, brand/service disruption 시 후보
```

Korean Air는 Asiana 인수 후 Jin Air를 중심으로 Air Busan과 Air Seoul을 통합해 하나의 budget airline을 만들 계획이라고 밝혔다. Reuters는 통합 LCC가 약 58대 항공기를 보유해 Jeju Air의 42대, T’way의 39대보다 큰 규모가 될 수 있고, 2024년 11월 기준 국내·국제 capacity 8%를 운영했다고 보도했다. 하지만 LCC 통합은 Stage 2다. Stage 3는 integration cost, route optimization, yield, safety/service quality가 확인되어야 한다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters LCC integration evidence

stage3_price:
N/A

Jin_Air_or_Air_Busan_OHLC:
price_data_unavailable_after_deep_search

combined_LCC_aircraft:
58

Jeju_Air_aircraft:
42

Tway_aircraft:
39

combined_LCC_aircraft_advantage_vs_Jeju:
58 / 42 - 1
= +38.1%

combined_LCC_aircraft_advantage_vs_Tway:
58 / 39 - 1
= +48.7%

combined_capacity_share_Nov_2024:
8%

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = LCC_consolidation_watch
stage_failure_type = stage2_watch_success
```

---

## Case F — Pan Ocean `cyclical_success / dry bulk and LNG fleet expansion`

```text
symbol = 028670
case_type = cyclical_success
archetype = SHIPPING_DRY_BULK_CYCLE
```

### stage date

```text
Stage 1:
2024
- dry bulk freight rate recovery
- fleet expansion
- LNG carrier addition
- shipping cycle rebound

Stage 2:
2024-05~06
- Daishin expects Pan Ocean OP to rise 39% to 536B won in 2024
- target price raised to 6,700원 from 6,500원
- shares -0.2% to 4,615원
- more LNG carriers expected in 2H

Stage 3:
없음
- shipping rate / fleet expansion은 cycle
- freight-rate floor, contract coverage, FCF, deleveraging 확인 전 Green 금지

Stage 4B:
freight-rate recovery로 shipping basket이 먼저 rerating되면 후보

Stage 4C:
freight normalization, overcapacity, China demand slowdown, vessel oversupply 시 후보
```

Pan Ocean은 shipping cycle Stage 2 후보지만 구조적 Green은 아니다. WSJ/MarketWatch Market Talk는 Daishin이 Pan Ocean의 2024년 영업이익을 39% 증가한 5,360억 원으로 예상하고 target을 6,700원으로 높였다고 전했다. 하지만 같은 코멘트에서 주가는 0.2% 낮은 4,615원이었다. 더 많은 bulk carriers와 2H LNG carriers가 수익성 개선 요인으로 제시됐지만, shipping은 freight-rate floor와 FCF 확인 전에는 cyclical_success다. ([월스트리트저널][2])

### 실제 가격경로 검증

```text
price_data_source:
WSJ / MarketWatch Market Talk shipping anchor

stage3_price:
N/A

event_price:
4,615원

event_MAE:
-0.2%

target_price:
6,700원

target_price_before:
6,500원

target_raise:
6,700 / 6,500 - 1
= +3.1%

target_upside_from_event_price:
6,700 / 4,615 - 1
= +45.2%

2024_OP_forecast:
536B won

OP_growth_forecast:
+39%

implied_prior_OP:
536B / 1.39
= 약 385.6B won

LNG_carrier_addition:
more LNG carriers due in 2H

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = cyclical_success / evidence_good_but_price_failed
rerating_result = dry_bulk_shipping_cycle_watch
stage_failure_type = stage2_cycle_not_green
```

---

## Case G — Lotte Tour / Yellow Balloon / Shinsegae `event_premium / China-Japan redirect`

```text
symbols = 032350 / 104620 / 004170
case_type = event_premium / price_moved_without_evidence
archetype = TOURISM_REDIRECT_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-11-17~21
- China-Japan diplomatic dispute
- China travel warning against Japan
- Chinese cruise ships cancel Japan stops
- South Korea redirect expectation

Stage 2:
2025-11-21
- Chinese cruise ships consider avoiding Japan
- Jeju stays extended
- Lotte Tour Development +20%+
- Yellow Balloon +24%
- Shinsegae +6%

Stage 3:
없음
- redirect expectation만으로 Green 금지
- actual arrivals, casino drop, hotel occupancy, ADR, duty-free sales, FCF 확인 필요

Stage 4B:
2025-11-21
- actual spend 전 관광주 +20% 이상 급등

Stage 4C:
redirect fails, dispute fades, tourist spend weak, casino utilization weak, debt/refinancing risk 시 후보
```

중국-일본 외교갈등으로 중국 cruise operators가 일본 기항을 피하고 한국으로 우회하는 방안을 검토하자, Reuters는 Lotte Tour Development가 20% 이상, Yellow Balloon이 24%, Shinsegae가 6% 상승했다고 보도했다. 하지만 업계 관계자들은 실제 중국 관광객 증가까지는 시간이 걸릴 수 있다고 조심스럽게 봤다. 즉 이건 tourism redirect Stage 1~2 event이자 4B/event premium이지, Stage 3가 아니다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters tourism-redirect event anchor

stage3_price:
N/A

Lotte_Tour_event_MFE:
> +20%

Yellow_Balloon_event_MFE:
+24%

Shinsegae_event_MFE:
+6%

Japan_stops_cancelled:
Adora Magic City cancels Fukuoka and Nagasaki stops and extends Jeju stay

South_Korea_redirect_status:
early signs only

historical_context:
2013 China-Japan territorial dispute led to >50% jump in Chinese tourists to Korea

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- actual arrivals/spend 전 +20% 이상 상승은 4B/event premium.
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = tourism_redirect_watch
stage_failure_type = should_have_been_stage1_or_4B_watch
```

---

## Case H — Jeju Air `hard 4C / operational safety trust break`

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
- Muan route expansion

Stage 2:
없음

Stage 3:
없음

Stage 4C:
2024-12-30
- fatal crash
- 179 fatalities
- Jeju Air intraday -15.7%
- event low 6,920원
- market cap wipeout up to 95.7B won
- consumer trust shock
```

Jeju Air 사고는 R9의 hard 4C 기준점이다. Reuters는 Muan crash로 179명이 사망했고, Jeju Air 주가가 장중 15.7% 급락해 6,920원까지 내려가 상장 이후 최저치를 기록했으며, 최대 957억 원의 시가총액이 사라졌다고 보도했다. 같은 기사에서 AK Holdings는 최대 12% 하락했고, Korean Air와 Asiana도 각각 1.3%, 0.8% 하락했다. 여행사 주식도 약세였고, 일부 여행사에서 package cancellation이 두 배, booking이 절반으로 줄었다는 보도도 있었다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported crash / price / travel-agency anchors

stage3_price:
N/A

Jeju_Air_event_MAE_1D:
-15.7%

event_low_price:
6,920원

implied_pre_event_reference_price:
6,920 / (1 - 0.157)
= 약 8,209원

market_cap_wipeout:
95.7B won

fatalities:
179

AK_Holdings_MAE:
-12%

Korean_Air_MAE:
-1.3%

Asiana_MAE:
-0.8%

Air_Busan_MFE:
> +15%

Jin_Air_initial_MFE:
+5.4%, then faded

Tway_Air_initial_MFE:
+7.3%, then faded

Hanatour_MAE:
-7%

Very_Good_Tour_MAE:
-11%

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

# 5. 이번 R9 case별 요약표

| case                        | 분류                     |                                                             실제 가격검증 | alignment           |
| --------------------------- | ---------------------- | ------------------------------------------------------------------: | ------------------- |
| Hyundai/Kia future mobility | success_candidate + 4B |                      현대차 +10.5%, 기아 +15%, 10T won Saemangeum report | event premium       |
| Hyundai Mobis ICCU          | 4C-watch               |                   225,500원, -0.7%; target cut 12%; ICCU recall risk | quality watch       |
| Hyundai Rotem rail          | success_candidate      |                         Morocco 2.2T won / $1.54B, 110 urban trains | rail Stage 2        |
| T’way Air EU routes         | success_candidate      | Paris/Rome/Barcelona/Frankfurt, five A330-200, 30~40% growth target | route Stage 2       |
| Jin Air/Air Busan/Air Seoul | success_candidate      |                             combined 58 aircraft, 8% capacity share | integration Stage 2 |
| Pan Ocean                   | cyclical_success       |               4,615원, -0.2%; target upside +45.2%; OP forecast +39% | cycle watch         |
| Lotte Tour/Yellow Balloon   | event premium          |                Lotte Tour +20%+, Yellow Balloon +24%, Shinsegae +6% | price-before-spend  |
| Jeju Air                    | hard 4C                |                    -15.7%, 6,920원, 시총 95.7B wipeout, 179 fatalities | safety thesis break |

---

# 6. score-price alignment 판정

```text
success_candidate:
- 현대 로템 rail export
- T’way Air Europe route allocation
- Jin Air / Air Busan / Air Seoul LCC integration
- Hyundai/Kia future-mobility capex, 단 Stage 2

cyclical_success:
- Pan Ocean dry bulk / shipping cycle

event_premium:
- Hyundai/Kia Saemangeum AI/robotics/hydrogen event
- Lotte Tour / Yellow Balloon China-Japan redirect event

price_moved_without_evidence:
- Hyundai/Kia +10~15% future-mobility capex event before robot/software revenue
- tourism redirect rally before arrivals/spend/casino drop
- LCC route/integration rally before yield/load factor

evidence_good_but_price_failed:
- Pan Ocean forecast/target raise but shares -0.2%

thesis_break_watch:
- Hyundai Mobis ICCU quality issue

hard_4C:
- Jeju Air fatal safety accident

4B-watch:
- Hyundai/Kia future-mobility event rally
- tourism redirect +20~24%
- LCC integration/route allocation if price outruns utilization
- shipping cycle rally if freight rate floor not proven

4C-watch:
- Hyundai Mobis quality recall
- Hyundai robotics labor friction
- LCC safety / operational trust
- shipping cycle normalization
```

---

# 7. 점수비중 교정

## 올릴 축

```text
unit_economics +5
FCF_after_capex +5
utilization +5
contract_delivery_schedule +4
load_factor_with_yield +5
route_profitability +5
fleet_integration_synergy +4
maintenance_safety_trust +5
quality_recall_control +5
tourist_spend_conversion +5
casino_drop_and_hold +4
freight_rate_floor +4
```

### 왜 올리나

Hyundai Rotem은 실제 2.2조 원 철도 수주가 있고, T’way는 Europe routes를 배정받았고, Jin Air 통합 LCC는 fleet scale이 있다. 하지만 이들 모두 Stage 3는 **납품·load factor·yield·integration synergy·FCF**로 확인해야 한다. R9는 바퀴가 굴러가는 것보다 그 바퀴가 돈을 벌고 있는지가 중요하다.

## 내릴 축

```text
future_mobility_capex_headline -5
robotics_AI_city_theme_only -5
route_allocation_without_yield -4
fleet_count_without_margin -4
tourism_redirect_event_only -5
freight_rate_cycle_only -5
quality_recall_issue -5
safety_trust_break -5
labor_disruption_risk -4
capex_without_FCF -4
```

### 왜 내리나

Hyundai/Kia는 10조 원 투자설만으로 +10~15% 뛰었지만 robot/software revenue는 아직 없다. Lotte Tour와 Yellow Balloon은 actual spend 전 +20% 이상 올랐다. 현대모비스는 EV parts exposure가 있어도 ICCU quality issue가 먼저 보였다. Jeju Air는 safety trust가 깨지면 여행수요가 아무 의미 없음을 보여준다.

## Green gate 강화 조건

```text
R9 Stage 3-Green 필수:
1. unit economics 확인
2. FCF after capex 확인
3. utilization / load factor / fleet productivity 확인
4. route yield 또는 contract margin 확인
5. safety / quality / operational trust 통과
6. labor / integration / maintenance risk 통과
7. 관광주는 arrivals보다 spend / occupancy / casino drop / OPM 확인
8. 해운주는 freight-rate floor와 contract coverage 확인
9. 가격경로가 evidence 이후 따라옴

금지:
AI city / robotics capex headline만 있음
route allocation만 있음
fleet count만 있음
freight-rate cycle만 있음
tourism redirect 기대만 있음
quality recall 발생
fatal safety accident 발생
```

## 4B 조기감지 조건

```text
4B-watch:
미래모빌리티 투자설로 +10~15% 급등
관광 reroute 기대만으로 +20% 이상 급등
route allocation 뉴스로 LCC가 실적 전 급등
fleet integration 기대가 integration cost보다 먼저 가격화
freight-rate cycle로 shipping stock이 먼저 rerating
robotics / AI city / hydrogen infrastructure headline으로 valuation 확장

4B-elevated:
capex는 늘지만 FCF bridge 없음
labor friction 발생
quality issue 반복
route load factor가 기대 미달
tourist spend가 arrivals를 못 따라감
shipping rate가 peak-out
```

## 4C hard gate 조건

```text
fatal safety accident
operational trust break
quality recall with earnings/reputation damage
route launch failure
fleet integration failure
labor disruption blocking deployment
capex overrun
FCF deterioration
freight rate collapse
tourist spend failure
casino utilization collapse
consumer trust shock
```

이번 R9 Loop 10에서는 **Jeju Air fatal crash를 hard 4C로 확정**한다. Hyundai Mobis ICCU issue와 Hyundai robotics labor friction은 4C-watch다.

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

## docs/round/round_167.md 요약

```md
# R9 Loop 10. Mobility / Transport / Leisure Price Validation

이번 라운드는 R9 Loop 10 price-validation 라운드다.

핵심 결론:
- Hyundai/Kia future-mobility capex is Stage 2 + 4B-watch. A reported 10T won Saemangeum AI/robotics/hydrogen investment drove Hyundai +10.5% and Kia +15%, but robot/software revenue and FCF are not yet proven.
- Hyundai Mobis is quality-risk 4C-watch. Recurring ICCU defect/recall risk led Kiwoom to cut target by 12% to 265,000 won; shares were -0.7% at 225,500 won.
- Hyundai Rotem rail export is Stage 2. Morocco ONCF order is around 2.2T won / $1.54B for 110 urban trains, the largest railway-business order for Hyundai Rotem.
- T’way Air Europe route allocation is Stage 2. Paris/Rome/Barcelona/Frankfurt routes, five A330-200 aircraft, 100 pilots and maintenance support from Korean Air, and 30~40% growth target are positive, but load factor/yield must confirm.
- Jin Air / Air Busan / Air Seoul integration is Stage 2. Combined LCC fleet around 58 aircraft vs Jeju Air 42 and T’way 39, but integration cost and route profitability are required.
- Pan Ocean is cyclical_success, not Green. Daishin expected 2024 OP +39% to 536B won and target upside +45.2%, but shares were -0.2% at 4,615 won.
- Lotte Tour / Yellow Balloon China-Japan redirect is event premium. Lotte Tour +20%+, Yellow Balloon +24%, Shinsegae +6% before actual arrivals/spend/occupancy.
- Jeju Air is hard 4C. Fatal crash killed 179, shares fell as much as -15.7% to 6,920 won, wiping out up to 95.7B won market cap.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 167 R9 Loop 10 Mobility Transport Leisure Price Validation

## 반영 내용
- R9 Loop 10 price-validation 라운드를 추가했다.
- Future mobility capex, auto-parts quality recall, rail export, LCC Europe routes, LCC consolidation, dry bulk shipping cycle, tourism redirect event, airline safety hard 4C를 비교했다.
- Reuters/MarketWatch/WSJ reported anchors로 가능한 MFE/MAE 및 contract/event/operational metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- unit economics, FCF after capex, utilization, route yield, fleet integration, safety/quality trust, tourist spend conversion 가중치 강화
- future-mobility capex headline, route allocation without yield, tourism redirect-only, freight-rate cycle-only, quality recall, safety trust break 감점 강화
- R9 4B-watch와 airline safety hard 4C 강화
```

## case row 초안

```jsonl
{"case_id":"r9_loop10_hyundai_kia_future_mobility_capex_4b","symbol":"005380/000270","company_name":"Hyundai Motor / Kia","case_type":"success_candidate","primary_archetype":"FUTURE_MOBILITY_AI_ROBOTICS_CAPEX","stage2_date":"2026-02-25","stage4b_date":"2026-02-25","stage4c_date":"2026-01-22_watch","price_validation":{"price_data_source":"Reuters investment/event-return/labor-risk anchors","stage3_price":null,"hyundai_event_mfe_1d_pct":10.5,"kia_event_mfe_1d_pct":15.0,"saemangeum_investment_krw_trn":10,"hyundai_group_domestic_investment_2026_2030_krw_trn":125.2,"nvidia_ai_chip_allocation":50000,"robotics_capacity_target_annual_units":30000,"robotics_capacity_target_year":2028,"georgia_factory_capacity_target_units":500000,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"future_mobility_capex_watch","notes":"Future-mobility capex is Stage 2 and 4B-watch; robot/software revenue and FCF required before Green."}
{"case_id":"r9_loop10_hyundai_mobis_iccu_quality_recall_watch","symbol":"012330","company_name":"Hyundai Mobis","case_type":"4c_watch","primary_archetype":"AUTO_PARTS_QUALITY_RECALL_4C","stage4c_date":"2024-05","price_validation":{"price_data_source":"WSJ/MarketWatch Market Talk price and recall-risk anchor","stage3_price":null,"event_price_krw":225500,"event_mae_pct":-0.7,"target_price_krw":265000,"target_cut_pct":-12,"implied_prior_target_krw":301136,"target_upside_from_event_price_pct":17.5,"recall_issue":"Integrated Control Charging Unit defect","affected_parent_customers":["Hyundai Motor","Kia"],"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"auto_parts_quality_recall_watch","notes":"EV-parts exposure cannot become Green while recurring ICCU defect threatens earnings and reputation."}
{"case_id":"r9_loop10_hyundai_rotem_morocco_rail_order","symbol":"064350","company_name":"Hyundai Rotem","case_type":"success_candidate","primary_archetype":"RAIL_EXPORT_ORDER_TO_DELIVERY","stage2_date":"2025-02-26","price_validation":{"price_data_source":"Reuters rail-contract evidence","stage3_price":null,"morocco_total_train_purchase":168,"morocco_total_program_value_usd_bn":2.9,"hyundai_rotem_order_krw_trn":2.2,"hyundai_rotem_order_usd_bn":1.54,"hyundai_train_count":110,"hyundai_order_share_of_total_program_pct":53.1,"alstom_high_speed_trains":18,"caf_intercity_trains":40,"morocco_network_target_cities":43,"morocco_population_coverage_target_pct":87,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"rail_export_order_watch","notes":"Rail export order is Stage 2; delivery, margin, working capital and cash collection required before Green."}
{"case_id":"r9_loop10_tway_europe_route_allocation","symbol":"091810","company_name":"T'way Air","case_type":"success_candidate","primary_archetype":"LCC_LONG_HAUL_ROUTE_ALLOCATION","stage2_date":"2024-03-07","price_validation":{"price_data_source":"Reuters route-allocation evidence","stage3_price":null,"new_europe_routes":["Paris","Rome","Barcelona","Frankfurt"],"korean_air_support_aircraft":"five A330-200 aircraft","korean_air_support_pilots":100,"maintenance_support":true,"growth_expectation_2024_pct":"30-40","existing_a330_300_count":3,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"long_haul_LCC_route_watch","notes":"Route allocation is Stage 2; load factor, yield, aircraft cost, crew cost, fuel and safety/service execution required before Green."}
{"case_id":"r9_loop10_jin_air_air_busan_air_seoul_integration","symbol":"272450/298690/Asiana_LCC_exposure","company_name":"Jin Air / Air Busan / Air Seoul","case_type":"success_candidate","primary_archetype":"LCC_CONSOLIDATION_INTEGRATION","stage2_date":"2024-11-29","price_validation":{"price_data_source":"Reuters LCC integration evidence","stage3_price":null,"combined_lcc_aircraft":58,"jeju_air_aircraft":42,"tway_aircraft":39,"combined_lcc_aircraft_advantage_vs_jeju_pct":38.1,"combined_lcc_aircraft_advantage_vs_tway_pct":48.7,"combined_capacity_share_nov_2024_pct":8,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"LCC_consolidation_watch","notes":"LCC consolidation is Stage 2; integration cost, route optimization, load factor/yield and safety/service quality required before Green."}
{"case_id":"r9_loop10_pan_ocean_dry_bulk_cycle","symbol":"028670","company_name":"Pan Ocean","case_type":"cyclical_success","primary_archetype":"SHIPPING_DRY_BULK_CYCLE","stage2_date":"2024-05/2024-06","price_validation":{"price_data_source":"WSJ/MarketWatch Market Talk shipping anchor","stage3_price":null,"event_price_krw":4615,"event_mae_pct":-0.2,"target_price_krw":6700,"target_price_before_krw":6500,"target_raise_pct":3.1,"target_upside_from_event_price_pct":45.2,"op_forecast_2024_krw_bn":536,"op_growth_forecast_pct":39,"implied_prior_op_krw_bn":385.6,"lng_carrier_addition":"more LNG carriers due in 2H","price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"cyclical_success_evidence_good_but_price_failed","rerating_result":"dry_bulk_shipping_cycle_watch","notes":"Dry bulk/fleet expansion is Stage 2/cycle; freight-rate floor, contract coverage, FCF and deleveraging required before Green."}
{"case_id":"r9_loop10_lotte_tour_yellow_balloon_china_japan_redirect","symbol":"032350/104620/004170","company_name":"Lotte Tour / Yellow Balloon / Shinsegae","case_type":"event_premium","primary_archetype":"TOURISM_REDIRECT_EVENT_PREMIUM","stage2_date":"2025-11-21","stage4b_date":"2025-11-21","price_validation":{"price_data_source":"Reuters tourism-redirect event anchor","stage3_price":null,"lotte_tour_event_mfe_pct":20,"yellow_balloon_event_mfe_pct":24,"shinsegae_event_mfe_pct":6,"japan_stops_cancelled":"Adora Magic City cancels Fukuoka/Nagasaki and extends Jeju stay","redirect_status":"early_signs_only","historical_context_china_tourist_jump_2013_pct":50,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium","rerating_result":"tourism_redirect_watch","notes":"China-Japan redirect expectation drove price before actual arrivals, occupancy, casino drop, ADR and FCF."}
{"case_id":"r9_loop10_jeju_air_fatal_crash_hard_4c","symbol":"089590","company_name":"Jeju Air","case_type":"4c_thesis_break","primary_archetype":"AIRLINE_SAFETY_OPERATIONAL_TRUST_4C","stage4c_date":"2024-12-30","price_validation":{"price_data_source":"Reuters crash/price/travel-agency anchors","stage3_price":null,"jeju_air_event_mae_1d_pct":-15.7,"event_low_price_krw":6920,"implied_pre_event_reference_price_krw":8209,"market_cap_wipeout_krw_bn":95.7,"fatalities":179,"ak_holdings_mae_pct":-12,"korean_air_mae_pct":-1.3,"asiana_mae_pct":-0.8,"air_busan_mfe_pct":15,"jin_air_initial_mfe_pct":5.4,"tway_air_initial_mfe_pct":7.3,"hanatour_mae_pct":-7,"very_good_tour_mae_pct":-11,"tour_package_cancellations":"doubled_for_one_operator","bookings":"halved_for_one_operator","price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"operational_safety_trust_break","notes":"Fatal crash is hard 4C and blocks travel-demand Green."}
```

## shadow weight row 초안

```csv
archetype,unit_economics,fcf_after_capex,utilization,contract_delivery,route_yield,fleet_synergy,safety_trust,quality_recall_control,tourist_spend,event_penalty,cycle_normalization_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
FUTURE_MOBILITY_AI_ROBOTICS_CAPEX,+3,+5,+4,+2,+0,+0,+3,+2,+0,-5,+2,+5,+4,Hyundai/Kia AI/robotics capex is Stage 2 and 4B-watch before robot/software revenue.
AUTO_PARTS_QUALITY_RECALL_4C,+4,+5,+4,+3,+0,+0,+5,+5,+0,-2,+3,+4,+5,Hyundai Mobis ICCU defect requires quality/reputation RedTeam.
RAIL_EXPORT_ORDER_TO_DELIVERY,+5,+5,+5,+5,+0,+0,+4,+3,+0,-2,+3,+3,+4,Hyundai Rotem rail order is Stage 2; delivery/margin/cash collection required.
LCC_LONG_HAUL_ROUTE_ALLOCATION,+5,+5,+5,+2,+5,+3,+5,+3,+0,-4,+3,+5,+4,T'way Europe routes require load factor/yield and cost control before Green.
LCC_CONSOLIDATION_INTEGRATION,+5,+5,+5,+2,+5,+5,+5,+3,+0,-3,+3,+4,+4,Jin/Air Busan/Air Seoul integration is Stage 2 until synergy and safety/service quality confirm.
SHIPPING_DRY_BULK_CYCLE,+4,+5,+4,+2,+0,+0,+2,+0,+0,-5,+5,+5,+4,Pan Ocean is cyclical success; freight floor/FCF/deleveraging required.
TOURISM_REDIRECT_EVENT_PREMIUM,+4,+4,+4,+0,+0,+0,+3,+0,+5,-5,+4,+5,+4,Lotte Tour/Yellow Balloon redirect rally is event premium until spend/occupancy/casino drop confirm.
AIRLINE_SAFETY_OPERATIONAL_TRUST_4C,+0,+0,+0,+0,+0,+0,+5,+5,+0,0,+5,+5,+5,Jeju Air fatal crash is hard 4C.
```

---

# 이번 R9 Loop 10 결론

R9는 **Stage 2가 많고 Stage 3는 드문 섹터**다. 수요가 보인다고 바로 Green이 아니다.

```text
1. Hyundai/Kia future mobility는 좋은 Stage 2 후보지만,
   +10~15% 급등은 robot/software 매출 전 4B/event premium이다.

2. Hyundai Mobis는 EV parts exposure가 있어도 ICCU 품질 이슈가 먼저다.
   품질·recall 비용은 R9에서 강한 4C-watch다.

3. Hyundai Rotem rail export는 2.2조 원 Morocco order로 Stage 2다.
   하지만 납품·마진·working capital 전 Stage 3 금지다.

4. T’way Europe routes는 좋은 long-haul LCC 기회지만,
   load factor, yield, aircraft/crew/fuel cost 전 Green이 아니다.

5. Jin Air / Air Busan / Air Seoul 통합은 fleet scale Stage 2다.
   integration cost와 safety/service quality를 통과해야 한다.

6. Pan Ocean은 dry bulk/fleet expansion cycle 후보다.
   하지만 shipping은 freight-rate floor와 FCF 전에는 cyclical_success다.

7. Lotte Tour / Yellow Balloon은 China-Japan redirect event로 급등했다.
   actual arrivals, spend, casino drop, occupancy 전에는 event premium이다.

8. Jeju Air는 R9 hard 4C 기준점이다.
   fatal accident는 여행수요와 LCC 성장논리를 즉시 차단한다.
```

한 문장으로 압축하면:

> **R9에서 진짜 Stage 3는 “미래모빌리티·철도·항공·관광 수요가 좋아진다”가 아니라, unit economics·utilization·route yield·fleet synergy·FCF와 safety/quality trust가 실제로 확인되는 순간이다.**
> **R9는 capex headline, route allocation, fleet count, tourism redirect, freight-rate cycle을 먼저 4B/Event Premium으로 분리하고, safety/quality failure를 hard 4C gate로 둬야 한다.**

[1]: https://www.reuters.com/business/retail-consumer/hyundai-motor-eyes-multi-billion-dollar-investment-south-korea-say-sources-2026-02-25/?utm_source=chatgpt.com "Hyundai Motor to unveil multi-billion-dollar investment in South Korea, source says"
[2]: https://www.wsj.com/business/autos/auto-transport-roundup-market-talk-b5c8f192?utm_source=chatgpt.com "Auto & Transport Roundup: Market Talk"
[3]: https://www.reuters.com/business/autos-transportation/morocco-buy-168-trains-france-spain-south-korea-29-bln-2025-02-26/?utm_source=chatgpt.com "Morocco to buy 168 trains from France, Spain and South Korea for $2.9 bln"
[4]: https://www.reuters.com/business/aerospace-defense/skoreas-tway-air-sees-golden-opportunity-new-eu-routes-2024-03-07/?utm_source=chatgpt.com "S.Korea's T'way Air sees 'golden opportunity' from new EU routes"
[5]: https://www.reuters.com/business/aerospace-defense/korean-airs-budget-jin-air-brand-absorb-asiana-low-cost-carriers-after-merger-2024-11-29/?utm_source=chatgpt.com "Korean Air's budget Jin Air brand to absorb Asiana low-cost carriers after merger"
[6]: https://www.reuters.com/world/asia-pacific/chinese-cruise-ships-look-steer-clear-japan-amid-diplomatic-dispute-2025-11-21/?utm_source=chatgpt.com "Chinese cruise ships look to steer clear of Japan amid diplomatic dispute"
[7]: https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com "Jeju Air shares plummet to record low after deadly plane crash"
