순서상 이번은 **R9 Loop 12 — 모빌리티·운송·레저 가격경로 검증 라운드**다.

```text
round = R9 Loop 12
round_id = round_193
large_sector = MOBILITY_TRANSPORT_LEISURE
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
```

이번 R9 Loop 12는 이전 R9의 Hyundai tariff·Korean Air 통합·Kumho Tire 화재만 반복하지 않고, **항공 안전사고, LCC route-remedy, 자동차 부품 hybrid/EREV, Mobis lighting divestiture, HMM/Hormuz shipping security, container freight normalization, 중국 관광 redirect, 여행·카지노 event premium**을 중심으로 본다.

---

# 1. 이번 라운드 대섹터

```text
R9 = 모빌리티·운송·레저
```

R9에서 Stage 3는 “항공 통합”, “하이브리드 수요”, “장거리 노선”, “중국 관광객”, “해운 운임”, “전장부품”이라는 말이 아니다.

진짜 Stage 3는 **load factor, route yield, fleet utilization, safety trust, logistics continuity, component ASP, repeat travel demand, 카지노·호텔 실매출, freight rate floor, FCF**가 같이 닫히는 순간이다.

---

# 2. 대상 canonical archetype

```text
AVIATION_SAFETY_HARD_4C
LCC_ROUTE_REMEDY_LONG_HAUL_OPTION
AUTO_COMPONENT_HYBRID_EREV_ASP
AUTO_PARTS_PORTFOLIO_RESTRUCTURING
SHIPPING_GEOPOLITICAL_SECURITY_4C
SHIPPING_FREIGHT_NORMALIZATION_4C
TOURISM_REDIRECT_EVENT_PREMIUM
TRAVEL_CASINO_DEMAND_CONVERSION
```

---

# 3. deep sub-archetype

```text
항공 안전:
- Jeju Air Muan crash
- Air Busan aircraft fire
- consumer trust / cancellation / safety inspection
- LCC credibility premium collapse

항공 route remedy:
- T'way Air European routes
- Korean Air-Asiana merger remedies
- Paris / Rome / Barcelona / Frankfurt
- wet-lease / A330 / pilot and maintenance support

자동차 부품:
- HL Mando integrated dynamic brake / smart damping control
- hybrid / EREV higher-ASP components
- Hyundai Mobis lighting-business divestiture / OPmobility combination

해운:
- HMM Namu Hormuz attack
- Korean commercial vessel security
- container freight normalization after Red Sea/Suez reopen
- Maersk/Hapag-Lloyd as global freight-cycle proxy

관광·레저:
- Lotte Tour Development
- Yellow Balloon Tour
- Shinsegae
- Jeju cruise rerouting
- China-Japan diplomatic dispute
- visa-free Chinese group tourism
```

---

# 4. 국장 신규 후보 case

## Case A — Jeju Air `hard 4C / aviation safety trust break`

```text
symbol = 089590
case_type = 4C-thesis-break
archetype = AVIATION_SAFETY_HARD_4C
```

### stage date

```text
Stage 1:
2024-12-29
- Muan International Airport crash
- 179 fatalities
- Jeju Air first fatal flight since founding
- LCC consumer trust shock

Stage 4C:
2024-12-30
- Jeju Air shares as much as -15.7%
- record low 6,920 won
- -8.5% at Reuters timestamp
- market cap wipeout up to 95.7B won
- AK Holdings as much as -12%
- HanaTour as much as -7%
- Very Good Tour as much as -11%

Stage 4C validation:
2025-12-22
- parliament passes independent probe bill
- 18-member parliamentary panel
- bird strike / engine shutdown / runway embankment / cover-up questions investigated

Stage 3:
N/A
```

Jeju Air는 이번 R9 Loop 12의 direct hard 4C다. 항공사는 load factor와 unit cost보다 먼저 **safety trust**가 깨지면 valuation engine이 바로 멈춘다. Reuters는 사고 직후 Jeju Air가 장중 -15.7%까지 떨어져 6,920원을 기록했고, 시가총액이 최대 957억 원 증발했다고 보도했다. 이후 국회가 독립조사법을 통과시키며, bird strike, engine shutdown, runway embankment, 조사 은폐 여부까지 검토 대상으로 올라갔다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event-return / investigation anchors

entry_date:
N/A, no Stage 3

stage3_price:
N/A

event_low_price:
6,920 won

event_intraday_MAE:
-15.7%

implied_pre_event_reference_price:
6,920 / (1 - 0.157)
= about 8,210 won

event_timestamp_MAE:
-8.5%

market_cap_wipeout:
95.7B won / $65.2M

AK_Holdings_MAE:
-12%

HanaTour_MAE:
-7%

Very_Good_Tour_MAE:
-11%

MFE_30D / 90D / 180D:
N/A

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
event itself = hard 4C trigger
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = aviation_safety_trust_break
stage_failure_type = hard_4C
```

---

## Case B — Air Busan `4C-watch / aircraft fire safety overhang`

```text
symbol = 298690
case_type = 4C-watch
archetype = AVIATION_SAFETY_HARD_4C
```

### stage date

```text
Stage 1:
2025-01-28
- aircraft fire incident
- one month after Jeju Air fatal crash
- Korean LCC safety sensitivity high

Stage 4C-watch:
2025-01-31
- Air Busan shares as much as -6.1%
- low price 2,325 won
- -3.8% at Reuters timestamp
- T'way Air +9%
- Jeju Air -0.8%
- Korean Air and Asiana flat

Stage 3:
N/A
```

Air Busan은 hard 4C로 확정하진 않지만, aviation safety 4C-watch다. 사망자가 확인된 Jeju Air case와 달리 사고 규모가 다르므로 hard 4C는 아니지만, 안전사고가 발생한 순간 Air Busan은 같은 세션에서 -6.1%까지 빠졌다. 이건 항공주 scoring에서 safety incident를 일반 뉴스가 아니라 **즉시 gate**로 둬야 한다는 뜻이다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters aircraft-fire / event-return anchor

stage3_price:
N/A

event_low_price:
2,325 won

event_intraday_MAE:
-6.1%

implied_pre_event_reference_price:
2,325 / (1 - 0.061)
= about 2,476 won

event_timestamp_MAE:
-3.8%

Tway_same_context:
+9%

Jeju_Air_same_context:
-0.8%

Korean_Air / Asiana:
flat

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = aviation_safety_incident_watch
stage_failure_type = 4C_watch_not_hard_4C
```

---

## Case C — T’way Air `success_candidate / route-remedy long-haul option`

```text
symbol = 091810
case_type = success_candidate
archetype = LCC_ROUTE_REMEDY_LONG_HAUL_OPTION
```

### stage date

```text
Stage 1:
2024-02~03
- Korean Air-Asiana merger remedy
- EU route surrender requirement
- T'way becomes long-haul LCC beneficiary

Stage 2:
2024-03-07
- T'way receives profitable European routes
- Paris starts June
- Rome starts August
- Barcelona starts September
- Frankfurt starts October
- Korean Air to lease 5 A330-200 aircraft
- Korean Air to provide 100 pilots and maintenance support
- management expects 30~40% growth in 2024

Stage 3:
없음
- route rights are Stage 2
- route yield, load factor, fuel cost, lease cost, pilot cost, long-haul execution 확인 필요

Stage 4B:
route-remedy headline로 price가 먼저 rerating되면 watch

Stage 4C:
long-haul load factor miss, aircraft lease cost, fuel spike, route delay, safety incident
```

T’way Air는 R9에서 “merger remedy가 실제 growth option이 될 수 있는가”를 보는 case다. EU remedy로 T’way는 Paris, Rome, Barcelona, Frankfurt 노선을 받았고, Korean Air가 A330-200 5대와 100명 pilot, maintenance support를 제공한다. 경영진은 이 route opportunity로 2024년 30~40% 성장을 기대했다. 다만 Stage 3는 route yield와 load factor가 확인될 때다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters route-remedy / operational anchor

stage3_price:
N/A

new_Europe_routes:
Paris
Rome
Barcelona
Frankfurt

route_start_schedule:
Paris: June 2024
Rome: August 2024
Barcelona: September 2024
Frankfurt: October 2024

aircraft_support:
5 A330-200 from Korean Air

pilot_support:
100 pilots

management_growth_expectation:
+30~40% in 2024

Tway_event_OHLC:
price_data_unavailable_after_deep_search

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_but_insufficient_price_data
rerating_result = LCC_longhaul_route_remedy_watch
stage_failure_type = route_rights_not_yield_green
```

---

## Case D — HL Mando `success_candidate / hybrid-EREV component ASP`

```text
symbol = 204320
case_type = success_candidate
archetype = AUTO_COMPONENT_HYBRID_EREV_ASP
```

### stage date

```text
Stage 1:
2024-06
- hybrid / EREV demand rising
- integrated dynamic brake / smart damping control content uplift
- Hyundai/Kia hybrid mix expansion read-through

Stage 2:
2024-06-25
- HL Mando shares close +11% at 49,600 won
- Samsung Securities raises target price by 42% to 58,000 won
- integrated dynamic brake ASP 70% above conventional
- smart damping control ASP 50% above conventional

Stage 3:
없음
- component ASP uplift is Stage 2
- customer take-rate, margin, order backlog, FCF 확인 전 Green 금지

Stage 4B:
hybrid/EREV component narrative로 price가 먼저 움직이면 watch

Stage 4C:
hybrid demand miss, OEM price pressure, China competition, raw material cost
```

HL Mando는 R9에서 자동차 부품의 좋은 Stage 2다. 단순 “자동차가 많이 팔린다”가 아니라 hybrid·EREV에서 advanced braking/suspension content가 올라간다. WSJ Market Talk는 integrated dynamic brake와 smart damping control의 ASP가 기존 대비 각각 70%, 50% 높고, 이 기대에 HL Mando가 11% 오른 49,600원에 마감했다고 전했다. ([월스트리트저널][4])

### 실제 가격경로 검증

```text
price_data_source:
WSJ / MarketWatch Market Talk price and component-ASP anchor

stage3_price:
N/A

event_price:
49,600 won

event_MFE:
+11%

implied_pre_event_reference_price:
49,600 / 1.11
= about 44,685 won

target_price:
58,000 won

target_price_raise:
+42%

target_upside_from_event_price:
58,000 / 49,600 - 1
= +16.9%

IDB_ASP_premium:
+70%

SDC_ASP_premium:
+50%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = hybrid_EREV_component_ASP_watch
stage_failure_type = ASP_uplift_not_margin_FCF_green
```

---

## Case E — Hyundai Mobis lighting divestiture `success_candidate / portfolio restructuring`

```text
symbol = 012330
case_type = success_candidate
archetype = AUTO_PARTS_PORTFOLIO_RESTRUCTURING
```

### stage date

```text
Stage 1:
2025-12~2026-01
- Hyundai Mobis explores lighting-business competitiveness options
- OPmobility seeks Asian footprint / lighting growth
- lighting increasingly important for design and safety

Stage 2:
2026-01-27
- OPmobility signs agreement to explore controlling stake in Hyundai Mobis lighting division
- Hyundai Mobis lighting business estimated >€1B annual revenue
- OPmobility exterior and lighting business about €4B revenue in first nine months 2025
- OPmobility shares +1% early trading

Stage 2 validation:
2026-02-25 / 2026-04-21
- OPmobility expects deal finalization by end-2026
- OPmobility 2025 operating margin improves to 4.8% from 4.2%
- OPmobility Q1 2026 revenue -0.4%, better than global auto production -3.4%

Stage 3:
없음
- Mobis Green requires transaction value, retained proceeds, margin improvement, capital allocation, shareholder return

Stage 4B:
divestiture headline로 Mobis price가 먼저 rerating되면 watch

Stage 4C:
deal delay, valuation disappointment, lighting margin weakness, Europe auto weakness
```

Hyundai Mobis는 “비핵심/저마진 사업 정리 → portfolio upgrade” 후보로 본다. OPmobility는 Hyundai Mobis lighting division의 controlling stake 인수를 검토하는 agreement를 체결했고, 해당 사업은 연매출 10억 유로 이상으로 추정됐다. 다만 Mobis 주주 관점에서는 transaction value, proceeds use, margin improvement, capital return이 나와야 Stage 3다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters OPmobility / Hyundai Mobis lighting transaction anchors

stage3_price:
N/A

Hyundai_Mobis_lighting_revenue_estimate:
>€1B per year

OPmobility_exterior_lighting_revenue_9M2025:
about €4B / $4.8B

OPmobility_total_2025_revenue:
€11.54B

OPmobility_2025_operating_margin:
4.8%

OPmobility_2024_operating_margin:
4.2%

margin_improvement:
+0.6pp

OPmobility_Q1_2026_revenue_decline:
-0.4%

global_auto_production_decline_context:
-3.4%

OPmobility_relative_industry_outperformance:
-0.4 - (-3.4)
= +3.0pp

OPmobility_event_MFE:
+1% early Paris trading

Hyundai_Mobis_OHLC:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_but_price_data_unavailable
rerating_result = auto_parts_portfolio_restructuring_watch
stage_failure_type = divestiture_plan_not_green_until_value_and_proceeds
```

---

## Case F — HMM / Hormuz vessel attack `shipping security 4C-watch`

```text
symbol = 011200
case_type = 4C-watch
archetype = SHIPPING_GEOPOLITICAL_SECURITY_4C
```

### stage date

```text
Stage 1:
2026-05-04
- HMM-operated cargo ship Namu attacked near Strait of Hormuz
- engine-room fire caused by port stern damage
- Korean commercial-vessel security risk

Stage 4C-watch:
2026-05-11
- Blue House strongly condemns attack
- forensic inspection in Dubai
- HMM Namu not in violation of rules
- South Korea vows response after identifying source

Stage 4C-watch 강화:
2026-05-14
- senior official says unlikely anyone but Iran was behind attack, Yonhap reported
- investigation continues
- South Korea weighs phased maritime-security role after U.S. talks

Stage 3:
N/A
```

HMM case는 direct Korean shipper의 shipping-security 4C-watch다. 선박 운임이 좋아도 물류 경로 자체가 공격받으면 보험료, rerouting, delay, security cost가 모두 바뀐다. Reuters는 HMM-operated vessel Namu가 Hormuz 부근에서 공격을 받아 engine room fire가 발생했고, 한국 정부가 강하게 규탄하며 forensic inspection을 진행했다고 보도했다. 이후 한국은 미국과 Hormuz maritime-security role을 단계적으로 논의했다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters HMM Namu attack / policy-response anchors

stage3_price:
N/A

vessel:
HMM Namu

incident:
attack near Strait of Hormuz / damage to port stern / engine-room fire

forensic_location:
Dubai port

government_position:
strong condemnation
response after source identified

possible_source_context:
senior official reportedly said unlikely anyone but Iran, investigation ongoing

HMM_event_OHLC:
price_data_unavailable_after_deep_search

MFE:
N/A

MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = shipping_security_4C_watch
stage_failure_type = geopolitical_shipping_security_not_green
```

---

## Case G — HMM / Pan Ocean shipping basket `freight normalization 4C-watch`

```text
symbols = 011200 / 028670
case_type = cyclical_success + 4C-watch
archetype = SHIPPING_FREIGHT_NORMALIZATION_4C
```

### stage date

```text
Stage 1:
2024~2025
- Red Sea rerouting supports container freight rates
- Korean shipping cyclicality
- HMM / Pan Ocean beta to freight and route disruption

Stage 4B:
2025~2026
- freight-rate support from route disruption can be cyclical success
- but not structural Green unless contract coverage / FCF / deleveraging confirm

Stage 4C-watch:
2026-02-05
- Maersk warns 2026 earnings could fall sharply
- 2026 EBITDA expected $4.5B~$7B vs $9.53B in 2025
- shares -5.5%
- Red Sea return could free 6~7% global container capacity
- new vessels add 5% capacity

Stage 4C-watch validation:
2026-02-09
- Hapag-Lloyd 2025 EBIT $1.1B vs $2.8B in 2024
- average freight rates -8%, volumes +8%
```

Korean shippers는 direct price anchor가 부족했지만, freight-cycle overlay는 명확하다. Maersk는 2026년 EBITDA가 2025년 $9.53B에서 $4.5B~$7B로 낮아질 수 있다고 봤고, Red Sea/Suez 복귀가 6~7% capacity를 풀 수 있다고 경고했다. Hapag-Lloyd도 평균 freight rate -8%가 volume +8%를 상쇄하며 EBIT가 $2.8B에서 $1.1B로 줄었다. 즉 R9 shipping은 “운임이 올랐다”가 Stage 3가 아니라, freight floor와 FCF가 유지되는지 봐야 한다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters global container-shipping cycle anchors

stage3_price:
N/A

Maersk_2025_EBITDA:
$9.53B

Maersk_2026_EBITDA_guidance:
$4.5B~$7B

Maersk_2026_EBITDA_decline_low_end:
4.5 / 9.53 - 1
= -52.8%

Maersk_2026_EBITDA_decline_high_end:
7 / 9.53 - 1
= -26.5%

Maersk_event_MAE:
-5.5%

Red_Sea_route_return_capacity_release:
6~7%

new_vessel_capacity_addition:
+5%

Hapag_2025_EBIT:
$1.1B

Hapag_2024_EBIT:
$2.8B

Hapag_EBIT_decline:
1.1 / 2.8 - 1
= -60.7%

Hapag_volume_growth:
+8%

Hapag_average_freight_rate_decline:
-8%

HMM / PanOcean_full_OHLC:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = cyclical_success_plus_4C_watch
rerating_result = shipping_freight_normalization_watch
stage_failure_type = freight_cycle_not_green
```

---

## Case H — Lotte Tour / Yellow Balloon / Shinsegae `tourism redirect event premium`

```text
symbols = 032350 / 104620 / 004170
case_type = event_premium
archetype = TOURISM_REDIRECT_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-09-29
- Chinese group tourists 3+ allowed visa-free entry
- 15-day stay
- pilot programme through June 2026

Stage 2:
2025-11-17
- China-Japan diplomatic dispute over Taiwan comments
- China advises citizens against Japan travel
- South Korea tourism beneficiary narrative
- Lotte Tour Development +9.6%

Stage 4B:
2025-11-21
- Chinese cruise operators reroute away from Japan
- Lotte Tour Development > +20%
- Yellow Balloon Tour +24%
- Shinsegae +6%
- Adora Magic City Jeju stay extended to 31~57 hours vs usual 9 hours

Stage 3:
없음
- tourism redirect is event premium
- hotel occupancy, casino drop, duty-free spend, package margin, ADR 확인 필요
```

이 case는 관광·레저의 전형적인 event premium이다. 중국 단체관광 비자면제와 China-Japan 갈등이 겹치면서 한국 관광주가 튀었다. Reuters는 11월 17일 Lotte Tour가 9.6% 올랐고, 11월 21일에는 Lotte Tour가 20% 이상, Yellow Balloon이 24%, Shinsegae가 6% 올랐다고 보도했다. 그러나 실제 Stage 3는 관광객 수보다 **hotel occupancy, casino drop, duty-free spend, package margin**으로 닫혀야 한다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters tourism redirect / visa-free / cruise rerouting anchors

stage3_price:
N/A

visa_free_group_condition:
3+ mainland Chinese tourists

visa_free_stay:
15 days

programme_period:
2025-09-29 to 2026-06

Lotte_Tour_2025-11-17_MFE:
+9.6%

Lotte_Tour_2025-11-21_context_MFE:
> +20%

Yellow_Balloon_MFE:
+24%

Shinsegae_MFE:
+6%

Adora_Magic_City_usual_Jeju_stay:
9 hours

Adora_Magic_City_new_Jeju_stay:
31~57 hours

Jeju_stay_extension_low:
31 / 9 - 1
= +244.4%

Jeju_stay_extension_high:
57 / 9 - 1
= +533.3%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = tourism_redirect_watch
stage_failure_type = tourist_flow_headline_not_spend_green
```

---

# 5. 이번 R9 case별 요약표

| case                         | 분류                          |                                                     실제 가격검증 | alignment               |
| ---------------------------- | --------------------------- | ----------------------------------------------------------: | ----------------------- |
| Jeju Air crash               | hard 4C                     |                               -15.7%, 6,920원, 시총 -95.7B won | safety trust break      |
| Air Busan fire               | 4C-watch                    |                                               -6.1%, 2,325원 | safety incident watch   |
| T’way EU routes              | success_candidate           |  4 Europe routes, 5 A330, 100 pilots, +30~40% growth target | route Stage 2           |
| HL Mando                     | success_candidate           |           +11%, 49,600원, target upside +16.9%, IDB ASP +70% | component ASP           |
| Hyundai Mobis lighting       | success_candidate           |              lighting revenue >€1B, Mobis price unavailable | portfolio restructuring |
| HMM Namu attack              | 4C-watch                    |                 direct HMM vessel attack, price unavailable | shipping security       |
| HMM/Pan Ocean shipping cycle | cyclical_success + 4C-watch | Maersk -5.5%, EBITDA guide -26.5%~-52.8%, Hapag EBIT -60.7% | freight normalization   |
| Lotte Tour / Yellow Balloon  | event premium               |                      Lotte >20%, Yellow +24%, Shinsegae +6% | tourism redirect        |

---

# 6. score-price alignment 판정

```text
aligned:
- hard 4C: Jeju Air crash
- 4C-watch: Air Busan fire
- 4B/event premium: Lotte Tour / Yellow Balloon tourism redirect

success_candidate:
- T’way Air route remedy
- HL Mando hybrid/EREV component ASP
- Hyundai Mobis lighting-business restructuring

cyclical_success:
- HMM / Pan Ocean shipping cycle if freight rates remain elevated

event_premium:
- tourism redirect
- T’way long-haul route remedy if price moves before yield/load factor
- Mobis divestiture if price moves before transaction value/proceeds

thesis_break_watch:
- HMM Namu Hormuz attack
- shipping freight normalization
- aviation safety incidents

price_moved_without_evidence:
- tourism stocks before hotel/casino/duty-free spend confirmation
- route-remedy stocks before route yield/load factor confirmation
- auto-component stocks before take-rate/margin confirmation
```

---

# 7. 점수비중 교정

## 올릴 축

```text
safety_trust +5
route_yield +5
load_factor +5
fleet_utilization +5
component_take_rate +5
component_ASP_uplift +4
transaction_value_and_proceeds +4
freight_rate_floor +5
logistics_security +5
tourism_spend_conversion +5
```

### 왜 올리나

Jeju Air와 Air Busan은 항공에서 safety trust가 가장 먼저라는 것을 보여준다. T’way는 route rights만으로는 부족하고 route yield·load factor가 필요하다. HL Mando는 ASP uplift가 명확하므로 component_take_rate를 봐야 한다. HMM/Hormuz와 Maersk/Hapag은 freight-rate와 route security가 동시에 중요하다는 것을 보여준다. Lotte Tour/Yellow Balloon은 관광객 headline보다 spend conversion이 Stage 3 조건이다.

## 내릴 축

```text
route_rights_only -5
aviation_safety_incident -5
tourist_arrival_headline_only -5
freight_spike_only -5
shipping_security_event -5
divestiture_headline_only -4
component_ASP_without_margin -4
fleet_count_without_yield -4
China_travel_redirect_only -4
```

### 왜 내리나

T’way route remedy는 좋은 Stage 2지만 route economics 전 Green이 아니다. Jeju Air는 safety hard 4C다. Lotte Tour와 Yellow Balloon은 관광객 redirect로 price가 먼저 갔지만 hotel/casino spend가 없다. HMM은 운임보다 먼저 shipping security가 깨질 수 있다. Mobis divestiture도 transaction value와 proceeds가 없으면 Stage 2다.

## Green gate 강화 조건

```text
R9 Stage 3-Green 필수:
1. route yield / load factor / fleet utilization 확인
2. safety trust risk 없음
3. component ASP가 margin/FCF로 전환
4. divestiture는 transaction value와 proceeds use 확인
5. shipping은 freight floor와 route security 확인
6. tourism은 arrivals보다 spend / hotel occupancy / casino drop / ADR 확인
7. logistics cost / insurance / fuel cost 통제
8. price path가 evidence 이후 따라옴

금지:
route rights only
fleet count only
tourist arrival headline only
freight spike only
safety incident unresolved
divestiture headline only
geopolitical shipping attack unresolved
```

## 4B 조기감지 조건

```text
4B-watch:
route-remedy headline로 LCC 급등
tourism redirect로 여행/카지노/백화점 급등
component ASP narrative로 부품주 급등
divestiture headline로 auto-parts stock 급등
freight-rate spike로 해운주 급등
safety 사건 이후 relief bounce가 과도할 때

4B-elevated:
route yield / load factor 미확인
tourism spend 미확인
component margin 미확인
transaction value 미공개
insurance/fuel/security cost 상승
safety investigation ongoing
```

## 4C hard gate 조건

```text
fatal aviation accident
major aircraft fire / repeated safety incident
independent probe / safety cover-up risk
shipping vessel attack
route closure / war-risk premium spike
freight normalization causing rate collapse
tourism boycott / diplomatic travel ban
hotel/casino spend failure
component take-rate failure
divestiture failure / valuation disappointment
```

이번 R9 Loop 12의 hard 4C는 **Jeju Air crash**로 확정한다. Air Busan, HMM/Hormuz, shipping freight normalization은 4C-watch다.

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
```

---

# 9. patch-ready 출력

## docs/round/round_193.md 요약

```md
# R9 Loop 12. Mobility / Transport / Leisure Price Validation

이번 라운드는 R9 Loop 12 price-validation 라운드다.

핵심 결론:
- Jeju Air crash is direct hard 4C. Shares fell as much as -15.7% to 6,920 won, wiping out up to 95.7B won market cap. AK Holdings -12%, HanaTour -7%, Very Good Tour -11%. Later independent probe bill extended safety overhang.
- Air Busan plane fire is 4C-watch. Shares fell as much as -6.1% to 2,325 won and were down -3.8% at Reuters timestamp.
- T’way Air route remedy is Stage 2. It receives Paris, Rome, Barcelona and Frankfurt routes, with Korean Air leasing five A330-200 aircraft and providing 100 pilots plus maintenance support. Management expected 30~40% growth.
- HL Mando is hybrid/EREV component ASP Stage 2. Shares closed +11% at 49,600 won, target price 58,000 won, IDB ASP +70%, SDC ASP +50%.
- Hyundai Mobis lighting divestiture is portfolio-restructuring Stage 2. OPmobility explores controlling stake in Mobis lighting business, estimated at >€1B annual revenue. Transaction value and proceeds use required.
- HMM Namu attack is shipping-security 4C-watch. HMM-operated cargo ship was attacked near Hormuz, causing engine-room fire and forensic inspection in Dubai.
- HMM/Pan Ocean shipping basket is cyclical_success plus 4C-watch. Maersk expects 2026 EBITDA $4.5B~$7B vs $9.53B in 2025; Red Sea route return could release 6~7% capacity. Hapag-Lloyd 2025 EBIT fell to $1.1B from $2.8B.
- Lotte Tour / Yellow Balloon / Shinsegae tourism redirect is event premium. Lotte Tour >+20%, Yellow Balloon +24%, Shinsegae +6% after Chinese cruises rerouted from Japan to Korea. Spend conversion required before Green.
```

## docs/checkpoints/checkpoint_28a_round193_r9_loop12.md 요약

```md
# Checkpoint 28A Round 193 R9 Loop 12 Mobility Transport Leisure Price Validation

## 반영 내용
- R9 Loop 12 price-validation 라운드를 추가했다.
- Aviation safety hard 4C, LCC route remedy, hybrid/EREV component ASP, auto-parts portfolio restructuring, shipping security, freight normalization, tourism redirect event premium을 비교했다.
- Reuters / WSJ / MarketWatch anchors로 가능한 MFE/MAE 및 event metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- safety trust, route yield, load factor, fleet utilization, component take-rate, component ASP, freight-rate floor, logistics security, tourism spend conversion 가중치 강화
- route rights-only, tourist-arrival headline-only, freight spike-only, safety incident, shipping security event, divestiture headline-only 감점 강화
```

## data/e2r_case_library/cases_r9_loop12_round193.jsonl 초안

```jsonl
{"case_id":"r9_loop12_jeju_air_muan_crash_hard_4c","symbol":"089590","company_name":"Jeju Air","case_type":"4c_thesis_break","primary_archetype":"AVIATION_SAFETY_HARD_4C","stage4c_date":"2024-12-30","price_validation":{"price_data_source":"Reuters crash / event-return / probe anchors","stage3_price":null,"event_low_price_krw":6920,"event_intraday_mae_pct":-15.7,"implied_pre_event_reference_price_krw":8210,"event_timestamp_mae_pct":-8.5,"market_cap_wipeout_krw_bn":95.7,"market_cap_wipeout_usd_mn":65.2,"ak_holdings_mae_pct":-12,"hanatour_mae_pct":-7,"very_good_tour_mae_pct":-11,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"aviation_safety_trust_break","notes":"Fatal accident is hard 4C; safety trust overrides route/load-factor thesis."}
{"case_id":"r9_loop12_air_busan_plane_fire_4c_watch","symbol":"298690","company_name":"Air Busan","case_type":"4c_watch","primary_archetype":"AVIATION_SAFETY_HARD_4C","stage4c_date":"2025-01-31_watch","price_validation":{"price_data_source":"Reuters aircraft-fire event-return anchor","stage3_price":null,"event_low_price_krw":2325,"event_intraday_mae_pct":-6.1,"implied_pre_event_reference_price_krw":2476,"event_timestamp_mae_pct":-3.8,"tway_same_context_pct":9.0,"jeju_air_same_context_pct":-0.8,"korean_air_asiana_context":"flat","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"aviation_safety_incident_watch","notes":"Non-fatal fire is 4C-watch, not hard 4C, but safety gate must be elevated."}
{"case_id":"r9_loop12_tway_eu_route_remedy","symbol":"091810","company_name":"T'way Air","case_type":"success_candidate","primary_archetype":"LCC_ROUTE_REMEDY_LONG_HAUL_OPTION","stage2_date":"2024-03-07","price_validation":{"price_data_source":"Reuters route-remedy operational anchor","stage3_price":null,"new_europe_routes":["Paris","Rome","Barcelona","Frankfurt"],"route_start_schedule":{"Paris":"2024-06","Rome":"2024-08","Barcelona":"2024-09","Frankfurt":"2024-10"},"aircraft_support":"5 A330-200 from Korean Air","pilot_support":100,"management_growth_expectation_pct":"30-40","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_insufficient_price_data","rerating_result":"LCC_longhaul_route_remedy_watch","notes":"Route rights are Stage 2; route yield, load factor, fuel/lease cost and execution required before Green."}
{"case_id":"r9_loop12_hl_mando_hybrid_erev_component_asp","symbol":"204320","company_name":"HL Mando","case_type":"success_candidate","primary_archetype":"AUTO_COMPONENT_HYBRID_EREV_ASP","stage2_date":"2024-06-25","price_validation":{"price_data_source":"WSJ/MarketWatch Market Talk price and ASP anchor","stage3_price":null,"event_price_krw":49600,"event_mfe_pct":11,"implied_pre_event_reference_price_krw":44685,"target_price_krw":58000,"target_price_raise_pct":42,"target_upside_from_event_price_pct":16.9,"idb_asp_premium_pct":70,"sdc_asp_premium_pct":50,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"hybrid_EREV_component_ASP_watch","notes":"Component ASP uplift is Stage 2; customer take-rate, backlog, margin and FCF required before Green."}
{"case_id":"r9_loop12_hyundai_mobis_lighting_divestiture","symbol":"012330","company_name":"Hyundai Mobis","case_type":"success_candidate","primary_archetype":"AUTO_PARTS_PORTFOLIO_RESTRUCTURING","stage2_date":"2026-01-27","price_validation":{"price_data_source":"Reuters OPmobility / Hyundai Mobis lighting transaction anchors","stage3_price":null,"hyundai_mobis_lighting_revenue_estimate_eur_bn":1.0,"opmobility_exterior_lighting_revenue_9m2025_eur_bn":4.0,"opmobility_total_2025_revenue_eur_bn":11.54,"opmobility_2025_margin_pct":4.8,"opmobility_2024_margin_pct":4.2,"opmobility_margin_improvement_pp":0.6,"opmobility_q1_2026_revenue_decline_pct":-0.4,"global_auto_production_decline_context_pct":-3.4,"opmobility_relative_industry_outperformance_pp":3.0,"opmobility_event_mfe_pct":1.0,"price_validation_status":"hyundai_mobis_price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_price_data_unavailable","rerating_result":"auto_parts_portfolio_restructuring_watch","notes":"Divestiture is Stage 2 until transaction value, proceeds use, margin improvement and shareholder return confirm."}
{"case_id":"r9_loop12_hmm_namu_hormuz_shipping_security","symbol":"011200","company_name":"HMM","case_type":"4c_watch","primary_archetype":"SHIPPING_GEOPOLITICAL_SECURITY_4C","stage4c_date":"2026-05-11_watch","price_validation":{"price_data_source":"Reuters HMM Namu attack / Hormuz policy-response anchors","stage3_price":null,"vessel":"HMM Namu","incident":"attack near Strait of Hormuz; port stern damage; engine-room fire","forensic_location":"Dubai port","government_position":"strong condemnation and response after source identification","possible_source_context":"senior official reportedly said unlikely anyone but Iran, investigation ongoing","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"shipping_security_4C_watch","notes":"Direct Korean shipper security event; insurance, rerouting, delay and security cost must be monitored."}
{"case_id":"r9_loop12_hmm_panocean_freight_normalization_watch","symbol":"011200/028670","company_name":"HMM / Pan Ocean shipping basket","case_type":"cyclical_success","primary_archetype":"SHIPPING_FREIGHT_NORMALIZATION_4C","stage4c_date":"2026-02-05_watch","price_validation":{"price_data_source":"Reuters Maersk/Hapag global shipping-cycle anchors","stage3_price":null,"maersk_2025_ebitda_usd_bn":9.53,"maersk_2026_ebitda_guidance_usd_bn":"4.5-7.0","maersk_2026_ebitda_decline_low_end_pct":-52.8,"maersk_2026_ebitda_decline_high_end_pct":-26.5,"maersk_event_mae_pct":-5.5,"red_sea_route_return_capacity_release_pct":"6-7","new_vessel_capacity_addition_pct":5,"hapag_2025_ebit_usd_bn":1.1,"hapag_2024_ebit_usd_bn":2.8,"hapag_ebit_decline_pct":-60.7,"hapag_volume_growth_pct":8,"hapag_average_freight_rate_decline_pct":-8,"price_validation_status":"korean_shipping_ohlc_unavailable_after_deep_search"},"score_price_alignment":"cyclical_success_plus_4C_watch","rerating_result":"shipping_freight_normalization_watch","notes":"Freight spike is cyclical; rate floor, contract coverage, FCF and deleveraging required before Green."}
{"case_id":"r9_loop12_lotte_yellowballoon_tourism_redirect","symbol":"032350/104620/004170","company_name":"Lotte Tour Development / Yellow Balloon / Shinsegae","case_type":"event_premium","primary_archetype":"TOURISM_REDIRECT_EVENT_PREMIUM","stage2_date":"2025-11-17","stage4b_date":"2025-11-21","price_validation":{"price_data_source":"Reuters tourism visa-free / China-Japan dispute / cruise rerouting anchors","stage3_price":null,"visa_free_group_condition":"3+ mainland Chinese tourists","visa_free_stay_days":15,"programme_period":"2025-09-29_to_2026-06","lotte_tour_20251117_mfe_pct":9.6,"lotte_tour_20251121_mfe_pct":20,"yellow_balloon_mfe_pct":24,"shinsegae_mfe_pct":6,"adora_usual_jeju_stay_hours":9,"adora_new_jeju_stay_hours":"31-57","jeju_stay_extension_low_pct":244.4,"jeju_stay_extension_high_pct":533.3,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium","rerating_result":"tourism_redirect_watch","notes":"Tourism redirect is 4B/event premium until hotel occupancy, casino drop, duty-free spend and package margin confirm."}
```

## data/sector_taxonomy/score_weight_profiles_round193_r9_loop12_v1.csv 초안

```csv
archetype,safety_trust,route_yield,load_factor,fleet_utilization,component_take_rate,component_asp,transaction_value_proceeds,freight_rate_floor,logistics_security,tourism_spend_conversion,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
AVIATION_SAFETY_HARD_4C,+5,+3,+3,+3,+0,+0,+0,+0,+3,+0,0,+4,+5,Jeju Air hard 4C and Air Busan 4C-watch prove safety trust must override airline growth thesis.
LCC_ROUTE_REMEDY_LONG_HAUL_OPTION,+4,+5,+5,+5,+0,+0,+0,+0,+2,+0,-4,+5,+4,T'way route rights are Stage 2; route yield/load factor/lease cost required before Green.
AUTO_COMPONENT_HYBRID_EREV_ASP,+2,+0,+0,+0,+5,+5,+0,+0,+1,+0,-3,+4,+3,HL Mando ASP uplift is Stage 2 until take-rate, margin, backlog and FCF confirm.
AUTO_PARTS_PORTFOLIO_RESTRUCTURING,+2,+0,+0,+0,+3,+3,+5,+0,+1,+0,-4,+4,+3,Hyundai Mobis lighting divestiture needs transaction value/proceeds and margin improvement.
SHIPPING_GEOPOLITICAL_SECURITY_4C,+0,+0,+0,+0,+0,+0,+0,+4,+5,+0,0,+4,+5,HMM Namu attack is shipping security 4C-watch.
SHIPPING_FREIGHT_NORMALIZATION_4C,+0,+0,+0,+0,+0,+0,+0,+5,+4,+0,-5,+5,+5,Maersk/Hapag show freight normalization can crush shipping earnings.
TOURISM_REDIRECT_EVENT_PREMIUM,+2,+0,+0,+0,+0,+0,+0,+0,+1,+5,-5,+5,+3,Lotte/Yellow Balloon tourism redirect is event premium until spend conversion confirms.
TRAVEL_CASINO_DEMAND_CONVERSION,+3,+0,+0,+0,+0,+0,+0,+0,+1,+5,-4,+5,+4,Hotel/casino/tourism Green requires occupancy, casino drop, ADR and package margin.
```

---

# 이번 R9 Loop 12 결론

```text
1. Jeju Air crash는 R9 hard 4C다.
   항공주는 safety trust가 깨지면 load factor·route growth보다 먼저 valuation이 무너진다.

2. Air Busan fire는 4C-watch다.
   fatal accident는 아니지만, 같은 safety gate에 넣어야 한다.

3. T’way EU route remedy는 Stage 2다.
   route rights와 aircraft/pilot support는 좋지만 route yield와 load factor 전 Green 금지다.

4. HL Mando는 hybrid/EREV component ASP Stage 2다.
   ASP uplift는 좋지만 take-rate, backlog, margin, FCF가 필요하다.

5. Hyundai Mobis lighting divestiture는 portfolio restructuring Stage 2다.
   transaction value, proceeds use, capital return이 나와야 Stage 3다.

6. HMM Namu attack은 shipping security 4C-watch다.
   운임보다 먼저 항로 안전·보험·rerouting cost가 gate다.

7. HMM/Pan Ocean shipping cycle은 cyclical_success와 4C-watch가 동시에 붙는다.
   Red Sea/Suez 정상화와 신조선 유입은 freight rate floor를 깰 수 있다.

8. Lotte Tour / Yellow Balloon tourism redirect는 event premium이다.
   중국 관광객 redirect가 price를 먼저 움직였지만, hotel occupancy·casino drop·spend 전에는 Stage 3가 아니다.
```

한 문장으로 압축하면:

> **R9에서 진짜 Stage 3는 “노선·관광객·운임·하이브리드·부품·물류 테마가 좋다”가 아니라, safety trust·route yield·load factor·component margin·freight floor·logistics security·tourism spend가 실제 돈으로 닫히는 순간이다.**

[1]: https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com "Jeju Air shares plummet to record low after deadly plane crash"
[2]: https://www.reuters.com/business/aerospace-defense/south-koreas-air-busan-shares-drop-after-plane-fire-2025-01-31/?utm_source=chatgpt.com "South Korea's Air Busan shares drop after plane fire"
[3]: https://www.reuters.com/business/aerospace-defense/skoreas-tway-air-sees-golden-opportunity-new-eu-routes-2024-03-07/?utm_source=chatgpt.com "S.Korea's T'way Air sees 'golden opportunity' from new EU routes"
[4]: https://www.wsj.com/finance/stocks/auto-transport-roundup-market-talk-3ea39623?utm_source=chatgpt.com "Auto & Transport Roundup: Market Talk"
[5]: https://www.reuters.com/business/opmobility-signs-deal-explore-buying-hyundai-mobis-lighting-business-2026-01-27/?utm_source=chatgpt.com "OPmobility signs deal to explore buying Hyundai Mobis' lighting business"
[6]: https://www.reuters.com/world/asia-pacific/south-korea-condemns-attack-cargo-ship-strait-hormuz-vows-response-2026-05-11/?utm_source=chatgpt.com "South Korea condemns attack on cargo ship in Strait of Hormuz, vows response"
[7]: https://www.reuters.com/business/maersk-q4-meets-forecasts-falling-freight-rates-weigh-2026-profits-2026-02-05/?utm_source=chatgpt.com "Maersk flags 2026 earnings hit as Suez return, overcapacity hit freight rates"
[8]: https://www.reuters.com/world/china/south-korea-pilot-visa-free-entry-chinese-tourist-groups-cctv-reports-2025-09-29/?utm_source=chatgpt.com "South Korea begins visa-free entry for Chinese tourist groups"
