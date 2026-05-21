순서상 이번은 **R9 Loop 11 — 모빌리티·운송·레저 가격경로 검증 라운드**다.

이번 R9 Loop 11은 이전처럼 “미래모빌리티 좋다 / LCC 통합 좋다 / 여행수요 좋다”에서 멈추지 않고, **자동차 주주환원·하이브리드 전략, 미국 관세, 중동 물류 차질, 항공 통합, 타이어·부품 공장 사고, 해운 freight cycle, 관광정책 이벤트**를 같이 본다.

```text
round = R9 Loop 11
round_id = round_180
large_sector = MOBILITY_TRANSPORT_LEISURE
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
```

KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC는 이번 환경에서 안정적으로 직접 확보하지 못했다. 대신 Reuters / WSJ / AP가 제공한 **가격 anchor, 이벤트 수익률, 실적·관세·물류·사고·정책 지표**만 계산했다. 계산 불가능한 30D/90D/180D full OHLC는 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R9 = 모빌리티·운송·레저
```

R9의 Stage 3는 “자동차가 잘 팔린다”, “하이브리드가 좋다”, “항공 통합이다”, “여행객이 온다”가 아니다.

**차량 판매 mix, tariff-adjusted margin, 물류비, route yield, load factor, fleet utilization, safety trust, supply-chain continuity, FCF**가 실제로 확인되어야 한다.

---

# 2. 대상 canonical archetype

```text
AUTO_HYBRID_SHAREHOLDER_RETURN
AUTO_TARIFF_MARGIN_SHOCK
AUTO_LOGISTICS_GEOPOLITICAL_DISRUPTION
AIRLINE_CONSOLIDATION_INTEGRATION
AUTO_SUPPLIER_FACTORY_FIRE_HARD_4C
AUTO_PARTS_WORKPLACE_SAFETY_HARD_4C
SHIPPING_FREIGHT_RATE_CYCLE
TOURISM_REDIRECT_POLICY_EVENT
EVENT_PREMIUM
CYCLICAL_SUCCESS
```

---

# 3. deep sub-archetype

```text
자동차:
- Hyundai Motor / Kia
- hybrid mix expansion
- EV slowdown response
- shareholder return / buyback
- U.S. tariff margin shock
- U.S. / Georgia localization

물류:
- Hyundai Glovis
- Middle East / Hormuz / Red Sea route disruption
- vehicle export logistics
- fuel cost / route diversion / port congestion

항공:
- Korean Air / Asiana
- Jin Air / Air Busan / Air Seoul integration
- Asiana cargo sale
- capacity / route optimization / antitrust remedy
- safety trust after Korean aviation incidents

자동차 부품·타이어:
- Kumho Tire
- Daejeon auto-parts supplier fire
- plant fire / production loss / customer supply disruption
- operational safety hard gate

해운:
- Pan Ocean / dry bulk / LNG carrier addition
- Red Sea freight rate cycle
- freight normalization risk

레저·관광:
- Lotte Tour Development
- Yellow Balloon
- Jeju / cruise reroute
- China visa-free group tourism
- arrivals vs spend / casino drop / hotel occupancy
```

---

# 4. 국장 신규 후보 case

## Case A — Hyundai Motor `success_candidate / hybrid + shareholder return`

```text
symbol = 005380
case_type = success_candidate
archetype = AUTO_HYBRID_SHAREHOLDER_RETURN
```

### stage date

```text
Stage 1:
2024-08-28
- EV 수요 둔화에 대응해 hybrid mix 강화
- annual global sales 5.55M by 2030 target
- hybrid sales target 1.33M by 2028
- shareholder return policy 강화

Stage 2:
2024-08-28
- 2025~2027년 최대 4T won buyback
- quarterly dividend minimum 2,500 won/share
- profit return policy 35%
- shares intraday +5%, close +4.7%

Stage 3:
보류
- hybrid mix, North America margin, tariff-adjusted OPM, FCF 확인 전 Green 금지

Stage 4B:
주주환원 + hybrid strategy 발표만으로 price가 먼저 rerating되면 후보

Stage 4C:
U.S. tariff margin hit, EV/hybrid competition, logistics disruption, labor/capex burden
```

Hyundai는 EV 둔화에 대응해 hybrid lineup을 확대하고, 2025~2027년 최대 4조 원 자사주 매입과 분기 최소 2,500원 배당을 제시했다. Reuters는 발표 당일 주가가 장중 최대 5%, 종가 기준 4.7% 상승했다고 보도했다. 이건 강한 Stage 2다. 하지만 Stage 3는 hybrid mix가 실제 ASP·OPM·FCF로 닫힐 때다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters investor-day / event-return anchor

entry_date:
2024-08-28

stage3_price:
N/A

event_MFE_1D:
+5.0%

event_close_return:
+4.7%

buyback_program:
up to 4T won over 2025~2027

quarterly_dividend_floor:
2,500 won/share

profit_return_policy:
35%

global_sales_target_2030:
5.55M vehicles

target_growth_vs_2023:
+30%

hybrid_sales_target_2028:
1.33M vehicles

EV_sales_target_2030:
2.0M vehicles

MFE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = hybrid_shareholder_return_watch
stage_failure_type = stage2_strategy_not_green
```

---

## Case B — Hyundai / Kia `4C-watch / U.S. tariff margin shock`

```text
symbols = 005380 / 000270
case_type = 4C-watch
archetype = AUTO_TARIFF_MARGIN_SHOCK
```

### stage date

```text
Stage 1:
2025-03-27
- Trump 25% import tariff on autos
- Korea auto export exposure to U.S. very high

Stage 4C-watch:
2025-03-27
- Hyundai Motor > -4%
- Kia > -3%
- Korea 2024 auto exports to U.S. $34.7B
- U.S. share 49% of total auto exports

Stage 4C-watch 강화:
2025-07-25
- Kia Q2 tariff hit 786B won / $570M
- operating profit -24% YoY to 2.76T won
- shares -1.7%

Stage 4C-watch 추가:
2025-07-31
- U.S. tariff set at 15% after trade deal
- Hyundai -4.5%
- Kia -6.6%
```

자동차 관세는 R9에서 가장 직접적인 margin 4C-watch다. 2025년 3월 미국 25% auto tariff 발표 후 Hyundai는 4% 이상, Kia는 3% 이상 하락했다. 한국의 2024년 대미 자동차 수출은 347억 달러로 전체 자동차 수출의 49%였다. 이후 Kia는 2025년 2분기 tariff cost가 7,860억 원, 약 5.7억 달러였고, 영업이익은 전년 대비 24% 감소했다. 7월 trade deal에서 15% tariff로 낮아졌음에도 Hyundai -4.5%, Kia -6.6%가 나왔다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters tariff / earnings / trade-deal anchors

stage3_price:
N/A

2025-03-27_event:
Hyundai Motor > -4%
Kia > -3%

U.S._auto_export_2024:
$34.7B

U.S._share_of_Korea_auto_exports:
49%

Kia_Q2_2025_tariff_hit:
786B won / $570M

Kia_Q2_2025_OP:
2.76T won

Kia_Q2_OP_decline:
-24% YoY

Kia_earnings_event_MAE:
-1.7%

2025-07-31_trade_deal_tariff:
15%

Hyundai_trade_deal_MAE:
-4.5%

Kia_trade_deal_MAE:
-6.6%

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = auto_tariff_margin_shock
stage_failure_type = 4C_watch_not_hard_4C
```

---

## Case C — Hyundai Motor / Hyundai Glovis `4C-watch / Middle East logistics disruption`

```text
symbols = 005380 / 086280
case_type = 4C-watch
archetype = AUTO_LOGISTICS_GEOPOLITICAL_DISRUPTION
```

### stage date

```text
Stage 1:
2026-03~04
- Middle East / Iran conflict
- vehicle export route disruption
- logistics cost / fuel cost / delivery delay

Stage 4C-watch:
2026-04-03
- Hyundai exports to Europe / North Africa disrupted
- Hyundai Glovis unable to access some Middle East routes
- cargo temporarily stored at alternative locations
- some shipments diverted to Sri Lanka
- Hyundai -1.2%, Glovis -0.7%, KOSPI +2.7%
```

Hyundai Motor와 Hyundai Glovis는 Hormuz/Middle East shock이 자동차 수출 물류로 직접 내려오는 case다. Hyundai는 유럽·북아프리카 수출이 차질을 받고 있다고 밝혔고, Glovis는 일부 중동 route 접근이 제한되어 화물을 대체 지역에 보관해야 했다고 설명했다. Reuters는 같은 날 Hyundai -1.2%, Hyundai Glovis -0.7%였고 KOSPI는 2.7% 상승했다고 보도했다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters logistics-disruption / event-return anchor

stage3_price:
N/A

Hyundai_event_MAE:
-1.2%

Hyundai_Glovis_event_MAE:
-0.7%

KOSPI_same_context:
+2.7%

Hyundai_relative_underperformance:
-1.2 - 2.7
= -3.9pp

Glovis_relative_underperformance:
-0.7 - 2.7
= -3.4pp

Hyundai_March_global_sales:
358,759 vehicles

Hyundai_March_sales_decline:
-2.3% YoY

domestic_sales_decline:
-2.0%

overseas_sales_decline:
-2.4%

Middle_East_shipments_decline:
-49%

route_disruption:
Europe / North Africa via Middle East

temporary_hub:
Sri Lanka mentioned as diverted intermediate hub

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = auto_export_logistics_disruption_watch
stage_failure_type = geopolitical_logistics_4C_watch
```

---

## Case D — Korean Air / Asiana `success_candidate / airline consolidation integration`

```text
symbols = 003490 / 020560 / 272450 / 298690
case_type = success_candidate
archetype = AIRLINE_CONSOLIDATION_INTEGRATION
```

### stage date

```text
Stage 1:
2020~2024
- Korean Air-Asiana consolidation
- aviation-market restructuring
- full-service carrier + LCC consolidation

Stage 2:
2024-12-12
- Korean Air completes acquisition of 63.88% Asiana stake
- deal about $1.3B
- group becomes one of Asia's largest carriers
- world’s 12th largest by international capacity

Stage 2 추가:
2024-11-29 / 2025-03-11
- Jin Air absorbs Air Busan and Air Seoul under one LCC brand
- combined LCC around 58 aircraft
- Asiana integration planned within two years
- new branding launched

Stage 3:
없음
- merger completion만으로 Green 금지
- load factor, yield, cost synergy, route optimization, debt/refinancing, safety/service quality 확인 필요

Stage 4B:
통합항공사 premium이 synergy 실적보다 먼저 가격에 반영되면 후보

Stage 4C:
integration delay, route-remedy pressure, service disruption, debt burden, safety accident
```

Korean Air는 Asiana 63.88% 지분 인수를 완료해 아시아 주요 대형 항공사 중 하나가 됐다. Reuters는 이 거래가 약 13억 달러 규모이고, 통합 그룹이 international capacity 기준 세계 12위가 된다고 보도했다. 또 Jin Air가 Air Busan·Air Seoul을 흡수해 약 58대 항공기를 가진 통합 LCC로 커질 수 있다. 다만 Stage 3는 실제 yield, load factor, cost synergy, integration cost, safety/service quality가 확인될 때다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters merger / fleet / integration anchors

stage3_price:
N/A

Korean_Air_Asiana_deal_value:
about $1.3B

Korean_Air_Asiana_stake:
63.88%

integration_timeline:
within two years

international_capacity_rank:
world's 12th largest by international capacity

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

combined_LCC_capacity_share_Nov_2024:
8%

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = airline_consolidation_integration_watch
stage_failure_type = stage2_merger_not_green
```

---

## Case E — Kumho Tire `hard 4C / factory fire supply disruption`

```text
symbol = 073240
case_type = 4C-thesis-break
archetype = AUTO_SUPPLIER_FACTORY_FIRE_HARD_4C
```

### stage date

```text
Stage 1:
2024~2025
- replacement tire / OE tire demand
- Hyundai / VW / Mercedes customer exposure
- revenue target +10% to 5T won

Stage 2:
없음

Stage 3:
없음

Stage 4C:
2025-05-17 / 2025-05-19
- Gwangju factory fire
- production suspended
- 12M tires/year capacity
- nearly 20% of global output
- shares -8%
- may cut 2025 revenue target
```

Kumho Tire는 R9의 direct-listed hard 4C다. Gwangju 공장은 연 1,200만 개 타이어 생산능력을 갖고 있으며 회사 글로벌 생산의 거의 20%를 차지한다. 화재로 생산이 중단됐고, Reuters는 주가가 8% 하락했다고 보도했다. 회사는 2025년 매출을 10% 늘려 5조 원으로 만들겠다는 목표를 낮춰야 할 수도 있다고 밝혔다. 고객은 Hyundai, Volkswagen, Mercedes-Benz 등이었다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters fire / production / event-return anchors

stage3_price:
N/A

event_MAE:
-8.0%

factory:
Gwangju factory

annual_capacity:
12M tires

share_of_global_capacity:
nearly 20%

production_status:
suspended

fire_extinguishment_context:
90~95% extinguished by May 19 report

revenue_target_before_fire:
+10% to 5T won / $3.58B

revenue_target_risk:
may need downward revision

customers:
Hyundai Motor
Volkswagen Group
Mercedes-Benz

injuries_initial:
1 employee + 2 firefighters

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
hard event itself
- 생산중단 공시/보도 당일 hard 4C.
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = tire_factory_supply_disruption
stage_failure_type = hard_4C
```

---

## Case F — Daejeon auto-parts supplier fire `sector hard 4C / workplace-safety supply-chain risk`

```text
listed_exposure = 005380 / 000270 supply-chain exposure
direct_company = Anjun Industrial unlisted
case_type = sector_hard_4C
archetype = AUTO_PARTS_WORKPLACE_SAFETY_HARD_4C
```

### stage date

```text
Stage 1:
2026-03 이전
- Hyundai / Kia supplier network
- engine valve supplier
- auto-parts production continuity

Stage 2:
없음

Stage 3:
없음

Stage 4C:
2026-03-20
- Daejeon car-parts factory fire
- 14 dead, 60 injured
- 25 seriously injured
- Anjun Industrial supplies Hyundai and Kia
```

Anjun Industrial은 비상장사지만, Hyundai/Kia supplier network의 hard safety gate로 기록해야 한다. Reuters는 Daejeon 자동차 부품 공장 화재로 14명이 사망하고 60명이 부상했으며, 이 중 25명이 중상이라고 보도했다. Anjun은 engine valve 제조사이고 Hyundai와 Kia 등에 공급한다고 보도됐다. 상장사 가격경로로 직접 계산할 수는 없지만, R9에서 supplier safety와 production continuity가 Green을 막는 hard gate라는 의미가 크다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters workplace-safety / supplier anchor

stage3_price:
N/A

direct_listed_ticker:
N/A

listed_exposure:
Hyundai Motor / Kia supplier network

fatalities:
14

injuries:
60

serious_injuries:
25

minor_injuries:
35

owner:
Anjun Industrial

product:
engine valves

customers:
Hyundai Motor / Kia and others

event_price_path:
price_data_unavailable_after_deep_search

reason:
- Anjun Industrial is not directly listed.
- Hyundai/Kia supplier-network stock impact not separable from macro/tariff/logistics factors in available sources.
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = auto_parts_workplace_safety_break
stage_failure_type = sector_hard_4C_direct_listed_mapping_unavailable
```

---

## Case G — Pan Ocean / shipping basket `cyclical_success + freight normalization watch`

```text
symbol = 028670
case_type = cyclical_success
archetype = SHIPPING_FREIGHT_RATE_CYCLE
```

### stage date

```text
Stage 1:
2024~2025
- Red Sea disruption
- dry bulk / tanker / LNG carrier utilization
- fleet expansion
- freight-rate cycle

Stage 2:
2024-05~06
- Daishin expects Pan Ocean 2024 OP +39% to 536B won
- target price 6,500원 → 6,700원
- shares -0.2% at 4,615원
- more LNG carriers due in 2H

Stage 2 / 4B-watch:
2025
- Red Sea disruption boosts rates
- but ceasefire / route normalization can depress freight rates

Stage 3:
없음
- freight-rate cycle만으로 Green 금지
- contract coverage, rate floor, FCF, deleveraging 확인 필요

Stage 4C:
Red Sea normalizes, freight rates fall 20~25%, overcapacity returns
```

Pan Ocean은 R9의 shipping cyclical_success case다. WSJ Market Talk는 Daishin이 Pan Ocean의 2024년 영업이익을 39% 증가한 5,360억 원으로 예상했고, target을 6,700원으로 올렸지만 주가는 4,615원에서 0.2% 하락했다고 보도했다. 동시에 Red Sea disruption이 freight rates를 지탱하는 cycle은 route normalization 시 꺼질 수 있다. DP World는 Red Sea attacks가 줄면 sea freight prices가 20~25% 하락할 수 있다고 봤고, Reuters는 Gaza ceasefire 기대가 Maersk 주가를 압박했다고 보도했다. ([월스트리트 저널][7])

### 실제 가격경로 검증

```text
price_data_source:
WSJ Market Talk / Reuters freight-cycle anchors

stage3_price:
N/A

Pan_Ocean_event_price:
4,615원

Pan_Ocean_event_MAE:
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

freight_rate_downside_if_Red_Sea_normalizes:
20~25% possible per DP World

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = cyclical_success
rerating_result = shipping_freight_cycle_watch
stage_failure_type = stage2_cycle_not_green
```

---

## Case H — Lotte Tour / Yellow Balloon / Jeju tourism `event_premium / tourism redirect`

```text
symbols = 032350 / 104620 / 004170 / tourism-leisure basket
case_type = event_premium
archetype = TOURISM_REDIRECT_POLICY_EVENT
```

### stage date

```text
Stage 1:
2025-08~09
- China group-tourist visa-free entry
- Korea tourism recovery
- department store / hotel / casino / travel agency basket rally

Stage 2:
2025-08-06
- Hyundai Department Store +7.1%
- Hotel Shilla +4.8%
- Paradise +2.9%
- Hankook Cosmetics +9.9%

Stage 2 추가:
2025-09-29
- Chinese groups of 3+ can stay 15 days visa-free
- programme runs to June 2026

Stage 2 / 4B:
2025-11-21
- China-Japan dispute reroutes cruise demand to Korea
- Lotte Tour +20%+
- Yellow Balloon +24%
- Shinsegae +6%

Stage 3:
없음
- 관광객 수 증가 기대만으로 Green 금지
- tourist spend, casino drop/hold, hotel occupancy, ADR, OPM 확인 필요

Stage 4C:
anti-Chinese rallies, low-spend tours, policy fade, visa programme 종료
```

관광·레저 basket은 R9의 전형적인 event premium이다. 중국 단체관광객 무비자 정책 발표 후 백화점·호텔·카지노·화장품주가 동반 상승했고, 9월부터 3명 이상 중국 단체관광객은 15일 무비자 체류가 가능해졌다. 이후 중국-일본 갈등으로 cruise operators가 일본 기항을 피하며 한국 관광주가 다시 튀었고 Lotte Tour는 20% 이상, Yellow Balloon은 24%, Shinsegae는 6% 상승했다. 하지만 업계는 실제 관광객 증가까지 시간이 걸릴 수 있다고 봤다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters tourism policy / redirect event anchors

stage3_price:
N/A

visa_policy_event:
Hyundai Department Store +7.1%
Hotel Shilla +4.8%
Paradise +2.9%
Hankook Cosmetics +9.9%

visa_free_period:
2025-09-29 to 2026-06

visa_free_stay:
15 days

group_condition:
3+ Chinese tourists

China_Japan_redirect_event:
Lotte Tour > +20%
Yellow Balloon +24%
Shinsegae +6%

Adora_Magic_City_schedule_change:
Japan stops cancelled / Jeju stay extended

usual_Jeju_schedule:
about 9 hours

new_Jeju_schedule:
31~57 hours

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = tourism_redirect_policy_watch
stage_failure_type = stage2_event_not_green
```

---

# 5. 이번 R9 case별 요약표

| case                              | 분류                |                                                                              실제 가격검증 | alignment         |
| --------------------------------- | ----------------- | -----------------------------------------------------------------------------------: | ----------------- |
| Hyundai hybrid/shareholder return | success_candidate |                                     event +5% intraday / +4.7% close, buyback 4T won | Stage 2           |
| Hyundai/Kia U.S. tariff           | 4C-watch          | Hyundai >-4%, Kia >-3%; Kia tariff hit 786B won; trade-deal Hyundai -4.5%, Kia -6.6% | margin shock      |
| Hyundai/Glovis logistics          | 4C-watch          |               Hyundai -1.2%, Glovis -0.7% vs KOSPI +2.7%; Middle East shipments -49% | logistics shock   |
| Korean Air/Asiana                 | success_candidate |                                       63.88% Asiana, $1.3B, combined LCC 58 aircraft | merger Stage 2    |
| Kumho Tire fire                   | hard 4C           |                                      -8%, 12M tires/year, nearly 20% global capacity | supply disruption |
| Daejeon auto-parts fire           | sector hard 4C    |                                         14 deaths, 60 injuries, Hyundai/Kia supplier | safety break      |
| Pan Ocean/shipping                | cyclical_success  |                                4,615원, -0.2%; target upside +45.2%; OP forecast +39% | cycle             |
| Lotte Tour/tourism                | event_premium     |                             Lotte +20%+, Yellow +24%, visa-free tourism basket rally | event premium     |

---

# 6. score-price alignment 판정

```text
success_candidate:
- Hyundai Motor hybrid/shareholder return
- Korean Air/Asiana integration

cyclical_success:
- Pan Ocean / shipping freight cycle

event_premium:
- Tourism redirect / China visa-free basket
- Hyundai shareholder-return day if price outruns OPM/FCF
- Korean Air/Asiana if synergy is priced before yield/load-factor proof

thesis_break_watch:
- Hyundai/Kia U.S. tariff margin shock
- Hyundai/Glovis Middle East logistics disruption

hard_4C:
- Kumho Tire Gwangju factory fire
- Daejeon auto-parts supplier fire as sector hard 4C

price_moved_without_evidence:
- tourism-policy rally before spend/occupancy/casino drop
- merger/integration rally before synergy
- shipping freight-rate rally before rate floor/FCF
```

---

# 7. 점수비중 교정

## 올릴 축

```text
unit_economics +5
tariff_adjusted_margin +5
hybrid_mix_profitability +4
FCF_after_capex +5
route_yield +5
load_factor +5
fleet_utilization +5
logistics_cost_control +5
supply_chain_continuity +5
safety_trust +5
tourist_spend_conversion +5
```

### 왜 올리나

Hyundai의 hybrid/shareholder-return 전략은 좋은 Stage 2지만, 이후 미국 관세와 중동 물류가 margin을 때렸다. Korean Air/Asiana는 대형 통합이지만 yield·load factor·cost synergy가 필요하다. Kumho Tire와 Anjun supplier fire는 production continuity와 safety trust가 R9에서 실제 earnings gate라는 것을 보여준다.

## 내릴 축

```text
strategy_day_only -4
shareholder_return_without_margin -4
tariff_relief_headline_only -5
fleet_count_without_yield -4
merger_without_synergy -5
tourism_policy_only -5
freight_rate_spike_only -5
factory_fire_or_supply_disruption -5
workplace_fatality -5
logistics_disruption -5
```

### 왜 내리나

R9는 수요가 좋아도 비용·물류·안전에서 쉽게 깨진다. Hyundai는 전략 day가 좋았지만 tariff와 logistics가 바로 RedTeam이 됐다. 관광주는 정책 발표만으로 뛰었지만 실제 spend가 Stage 3 조건이다. Kumho Tire처럼 생산능력 20%가 멈추면 demand narrative는 바로 무효화된다.

## Green gate 강화 조건

```text
R9 Stage 3-Green 필수:
1. unit economics 확인
2. tariff-adjusted margin 확인
3. FCF after capex 확인
4. route yield / load factor / fleet utilization 확인
5. logistics cost와 delivery delay 통제
6. supply-chain continuity 확인
7. safety / quality / operational trust 통과
8. 관광주는 arrivals보다 spend / occupancy / casino drop / OPM 확인
9. 가격경로가 evidence 이후 따라옴

금지:
전략발표만 있음
주주환원만 있음
통합항공사 headline만 있음
fleet count만 있음
관광정책만 있음
freight-rate spike만 있음
공장화재 / 사망사고 / 공급차질 존재
```

## 4B 조기감지 조건

```text
4B-watch:
전략발표일 주주환원으로 급등
항공 통합 premium이 synergy보다 먼저 반영
LCC 통합 fleet scale이 yield보다 먼저 가격화
관광정책 발표일 레저/카지노/면세주 동반 급등
freight-rate spike로 해운주가 먼저 rerating
물류차질 비용을 무시하고 수요만 반영

4B-elevated:
tariff cost가 분기 실적에 잡히기 시작
물류비 상승과 delivery delay 발생
factory utilization 손상
관광객은 늘지만 spend/OPM이 약함
shipping rate floor가 깨짐
```

## 4C hard gate 조건

```text
tariff cost causing OP collapse
factory fire / production suspension
fatal workplace accident
airline fatal or major safety accident
supply-chain disruption to key customers
logistics route closure / fuel cost shock
route launch failure
merger integration failure
tourist spend failure
freight-rate normalization collapse
```

이번 R9 Loop 11에서 확정 hard 4C는 **Kumho Tire Gwangju factory fire**다. **Daejeon auto-parts factory fire**는 직접 상장사는 아니지만 Hyundai/Kia supplier network의 sector hard 4C로 기록한다.

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

## docs/round/round_180.md 요약

```md
# R9 Loop 11. Mobility / Transport / Leisure Price Validation

이번 라운드는 R9 Loop 11 price-validation 라운드다.

핵심 결론:
- Hyundai Motor hybrid/shareholder return is Stage 2. Investor-day event drove +5% intraday and +4.7% close, with up to 4T won buyback over 2025~2027, 2,500 won quarterly dividend floor, and hybrid sales target 1.33M by 2028. Hybrid mix, tariff-adjusted margin and FCF required before Green.
- Hyundai/Kia U.S. tariff shock is 4C-watch. 25% tariff announcement hit Hyundai >-4% and Kia >-3%; Kia Q2 tariff cost was 786B won / $570M and OP fell 24%. Later 15% tariff trade deal still hit Hyundai -4.5% and Kia -6.6%.
- Hyundai/Hyundai Glovis Middle East logistics disruption is 4C-watch. Exports to Europe/North Africa were disrupted; Hyundai -1.2%, Glovis -0.7% vs KOSPI +2.7%; Middle East shipments fell 49%.
- Korean Air/Asiana is airline consolidation Stage 2. Korean Air acquired 63.88% of Asiana for about $1.3B, becoming world’s 12th-largest by international capacity. Combined LCC fleet around 58 aircraft. Yield/load factor/synergy required before Green.
- Kumho Tire factory fire is hard 4C. Shares -8%, Gwangju plant capacity 12M tires/year, nearly 20% of global capacity, production suspended, revenue target at risk.
- Daejeon auto-parts supplier fire is sector hard 4C. 14 deaths, 60 injuries, supplier Anjun Industrial provides engine valves to Hyundai/Kia.
- Pan Ocean is cyclical_success, not Green. OP forecast +39% to 536B won, target upside +45.2%, but shares -0.2%; Red Sea normalization could lower freight rates 20~25%.
- Lotte Tour / Yellow Balloon / tourism basket is event premium. Visa-free China group tourism and China-Japan reroute drove Lotte Tour >+20%, Yellow Balloon +24%, Shinsegae +6%, but tourist spend/occupancy/casino drop required.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 180 R9 Loop 11 Mobility Transport Leisure Price Validation

## 반영 내용
- R9 Loop 11 price-validation 라운드를 추가했다.
- Auto hybrid/shareholder-return, U.S. tariff shock, Middle East logistics disruption, airline consolidation, tire factory fire, auto-parts workplace safety, shipping freight cycle, tourism redirect event를 비교했다.
- Reuters/WSJ/AP anchors로 가능한 MFE/MAE 및 event/operational metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- unit economics, tariff-adjusted margin, FCF after capex, route yield, load factor, logistics cost control, supply-chain continuity, safety trust 가중치 강화
- strategy-day only, shareholder-return without margin, tariff-relief headline only, merger without synergy, tourism policy-only, freight-rate spike-only, factory fire/workplace fatality 감점 강화
- R9 operational hard 4C 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r9_loop11_hyundai_hybrid_shareholder_return","symbol":"005380","company_name":"Hyundai Motor","case_type":"success_candidate","primary_archetype":"AUTO_HYBRID_SHAREHOLDER_RETURN","stage2_date":"2024-08-28","price_validation":{"price_data_source":"Reuters investor-day/event-return anchor","stage3_price":null,"event_mfe_1d_pct":5.0,"event_close_return_pct":4.7,"buyback_program_krw_trn":4,"buyback_period":"2025-2027","quarterly_dividend_floor_krw":2500,"profit_return_policy_pct":35,"global_sales_target_2030_mn":5.55,"target_growth_vs_2023_pct":30,"hybrid_sales_target_2028_mn":1.33,"ev_sales_target_2030_mn":2.0,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"hybrid_shareholder_return_watch","notes":"Strong Stage 2; hybrid mix, tariff-adjusted margin and FCF required before Green."}
{"case_id":"r9_loop11_hyundai_kia_us_tariff_margin_shock","symbol":"005380/000270","company_name":"Hyundai Motor / Kia","case_type":"4c_watch","primary_archetype":"AUTO_TARIFF_MARGIN_SHOCK","stage4c_date":"2025-03-27/2025-07-25/2025-07-31","price_validation":{"price_data_source":"Reuters tariff/earnings/trade-deal anchors","stage3_price":null,"hyundai_mar27_mae_pct":-4.0,"kia_mar27_mae_pct":-3.0,"us_auto_exports_2024_usd_bn":34.7,"us_share_of_korea_auto_exports_pct":49,"kia_q2_2025_tariff_hit_krw_bn":786,"kia_q2_2025_tariff_hit_usd_mn":570,"kia_q2_2025_op_krw_trn":2.76,"kia_q2_op_decline_pct":-24,"kia_earnings_event_mae_pct":-1.7,"trade_deal_tariff_pct":15,"hyundai_trade_deal_mae_pct":-4.5,"kia_trade_deal_mae_pct":-6.6,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"auto_tariff_margin_shock","notes":"Tariff cost directly hit OP and stock reaction; 4C-watch until tariff-adjusted margins stabilize."}
{"case_id":"r9_loop11_hyundai_glovis_middle_east_logistics_disruption","symbol":"005380/086280","company_name":"Hyundai Motor / Hyundai Glovis","case_type":"4c_watch","primary_archetype":"AUTO_LOGISTICS_GEOPOLITICAL_DISRUPTION","stage4c_date":"2026-04-03","price_validation":{"price_data_source":"Reuters logistics-disruption/event-return anchor","stage3_price":null,"hyundai_event_mae_pct":-1.2,"glovis_event_mae_pct":-0.7,"kospi_same_context_pct":2.7,"hyundai_relative_underperformance_pp":-3.9,"glovis_relative_underperformance_pp":-3.4,"hyundai_march_global_sales":358759,"hyundai_march_sales_decline_pct":-2.3,"domestic_sales_decline_pct":-2.0,"overseas_sales_decline_pct":-2.4,"middle_east_shipments_decline_pct":-49,"route_disruption":"Europe/North Africa via Middle East","temporary_hub":"Sri Lanka mentioned as diverted intermediate hub","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"auto_export_logistics_disruption_watch","notes":"Middle East logistics disruption hit auto export chain; Green requires logistics cost and delivery stability."}
{"case_id":"r9_loop11_korean_air_asiana_consolidation","symbol":"003490/020560/272450/298690","company_name":"Korean Air / Asiana / Jin Air / Air Busan","case_type":"success_candidate","primary_archetype":"AIRLINE_CONSOLIDATION_INTEGRATION","stage2_date":"2024-12-12/2025-03-11","price_validation":{"price_data_source":"Reuters merger/fleet/integration anchors","stage3_price":null,"deal_value_usd_bn":1.3,"korean_air_asiana_stake_pct":63.88,"integration_timeline_years":2,"international_capacity_rank":12,"combined_lcc_aircraft":58,"jeju_air_aircraft":42,"tway_aircraft":39,"combined_lcc_aircraft_advantage_vs_jeju_pct":38.1,"combined_lcc_aircraft_advantage_vs_tway_pct":48.7,"combined_lcc_capacity_share_nov_2024_pct":8,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"airline_consolidation_integration_watch","notes":"Airline merger is Stage 2; load factor, yield, cost synergy, debt and safety/service quality required before Green."}
{"case_id":"r9_loop11_kumho_tire_gwangju_factory_fire_hard_4c","symbol":"073240","company_name":"Kumho Tire","case_type":"4c_thesis_break","primary_archetype":"AUTO_SUPPLIER_FACTORY_FIRE_HARD_4C","stage4c_date":"2025-05-17/2025-05-19","price_validation":{"price_data_source":"Reuters fire/production/event-return anchors","stage3_price":null,"event_mae_pct":-8.0,"factory":"Gwangju factory","annual_capacity_mn_tires":12,"share_of_global_capacity_pct":20,"production_status":"suspended","fire_extinguished_pct":"90-95 by May 19 report","revenue_target_before_fire":"increase 10pct to 5T won","revenue_target_risk":"may need downward revision","customers":["Hyundai Motor","Volkswagen Group","Mercedes-Benz"],"initial_injuries":"1 employee and 2 firefighters","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"tire_factory_supply_disruption","notes":"Factory fire suspended nearly 20% of global capacity; direct-listed hard 4C."}
{"case_id":"r9_loop11_daejeon_auto_parts_supplier_fire_sector_hard_4c","symbol":"005380/000270_supply_chain_exposure","company_name":"Anjun Industrial / Hyundai-Kia supplier network","case_type":"4c_thesis_break","primary_archetype":"AUTO_PARTS_WORKPLACE_SAFETY_HARD_4C","stage4c_date":"2026-03-20","price_validation":{"price_data_source":"Reuters workplace-safety/supplier anchor","stage3_price":null,"direct_listed_ticker":"N/A","listed_exposure":"Hyundai Motor / Kia supplier network","fatalities":14,"injuries":60,"serious_injuries":25,"minor_injuries":35,"owner":"Anjun Industrial","product":"engine valves","customers":["Hyundai Motor","Kia","others"],"price_validation_status":"sector_hard_4c_direct_listed_mapping_unavailable"},"score_price_alignment":"thesis_break","rerating_result":"auto_parts_workplace_safety_break","notes":"Unlisted supplier, but Hyundai/Kia supply-chain safety hard gate."}
{"case_id":"r9_loop11_pan_ocean_shipping_freight_cycle","symbol":"028670","company_name":"Pan Ocean","case_type":"cyclical_success","primary_archetype":"SHIPPING_FREIGHT_RATE_CYCLE","stage2_date":"2024-05/2025_cycle_watch","price_validation":{"price_data_source":"WSJ Market Talk / Reuters freight-cycle anchors","stage3_price":null,"event_price_krw":4615,"event_mae_pct":-0.2,"target_price_krw":6700,"target_price_before_krw":6500,"target_raise_pct":3.1,"target_upside_from_event_price_pct":45.2,"op_forecast_2024_krw_bn":536,"op_growth_forecast_pct":39,"implied_prior_op_krw_bn":385.6,"freight_rate_downside_if_red_sea_normalizes_pct":"20-25","price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"cyclical_success","rerating_result":"shipping_freight_cycle_watch","notes":"Freight-cycle benefit is Stage 2/cyclical; rate floor, contract coverage, FCF and deleveraging required before Green."}
{"case_id":"r9_loop11_lotte_tour_yellow_balloon_tourism_redirect","symbol":"032350/104620/004170/tourism_basket","company_name":"Lotte Tour / Yellow Balloon / Shinsegae / tourism basket","case_type":"event_premium","primary_archetype":"TOURISM_REDIRECT_POLICY_EVENT","stage2_date":"2025-08-06/2025-09-29/2025-11-21","stage4b_date":"2025-08-06/2025-11-21","price_validation":{"price_data_source":"Reuters tourism policy/redirect event anchors","stage3_price":null,"hyundai_department_event_mfe_pct":7.1,"hotel_shilla_event_mfe_pct":4.8,"paradise_event_mfe_pct":2.9,"hankook_cosmetics_event_mfe_pct":9.9,"visa_free_period":"2025-09-29_to_2026-06","visa_free_stay_days":15,"group_condition":"3+ Chinese tourists","lotte_tour_redirect_mfe_pct":20,"yellow_balloon_redirect_mfe_pct":24,"shinsegae_redirect_mfe_pct":6,"adora_magic_city_schedule_change":"Japan stops cancelled / Jeju stay extended","usual_jeju_schedule_hours":9,"new_jeju_schedule_hours":"31-57","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium","rerating_result":"tourism_redirect_policy_watch","notes":"Tourism policy/redirect event is Stage 2 and 4B; spend, occupancy, casino drop/hold and OPM required before Green."}
```

## shadow weight row 초안

```csv
archetype,unit_economics,tariff_adjusted_margin,hybrid_mix_profitability,fcf_after_capex,route_yield,load_factor,fleet_utilization,logistics_cost_control,supply_chain_continuity,safety_trust,tourist_spend,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
AUTO_HYBRID_SHAREHOLDER_RETURN,+5,+4,+5,+5,+0,+0,+0,+3,+3,+3,+0,-3,+4,+3,Hyundai hybrid/shareholder return is Stage 2 until margin and FCF confirm.
AUTO_TARIFF_MARGIN_SHOCK,+5,+5,+3,+5,+0,+0,+0,+2,+3,+3,+0,0,+3,+5,U.S. tariffs hit Kia OP and auto stock prices; strong 4C-watch.
AUTO_LOGISTICS_GEOPOLITICAL_DISRUPTION,+4,+4,+2,+4,+0,+0,+0,+5,+5,+3,+0,0,+4,+5,Middle East logistics disruption directly hit Hyundai/Glovis relative returns.
AIRLINE_CONSOLIDATION_INTEGRATION,+5,+3,+0,+5,+5,+5,+5,+3,+3,+5,+0,-4,+5,+4,Korean Air/Asiana needs yield/load factor/synergy and safety quality before Green.
AUTO_SUPPLIER_FACTORY_FIRE_HARD_4C,+0,+0,+0,+0,+0,+0,+0,+0,+5,+5,+0,0,+3,+5,Kumho Tire factory fire is direct-listed hard 4C.
AUTO_PARTS_WORKPLACE_SAFETY_HARD_4C,+0,+0,+0,+0,+0,+0,+0,+0,+5,+5,+0,0,+3,+5,Daejeon supplier fire is sector hard 4C for Hyundai/Kia supplier network.
SHIPPING_FREIGHT_RATE_CYCLE,+4,+0,+0,+5,+0,+0,+4,+4,+3,+2,+0,-5,+5,+4,Pan Ocean freight-cycle benefit needs rate floor/contract coverage/FCF.
TOURISM_REDIRECT_POLICY_EVENT,+3,+0,+0,+4,+0,+0,+3,+2,+2,+3,+5,-5,+5,+4,Tourism policy/redirect rally is event premium until spend/OPM confirm.
```

---

# 이번 R9 Loop 11 결론

R9는 **수요보다 비용·안전·물류가 먼저 깨질 수 있는 섹터**다.

```text
1. Hyundai Motor의 hybrid/shareholder-return 전략은 좋은 Stage 2다.
   하지만 tariff-adjusted margin과 FCF 전 Stage 3는 아니다.

2. Hyundai/Kia U.S. tariff shock은 4C-watch다.
   관세비용이 Kia 영업이익에 실제로 들어왔고, trade-deal에도 주가는 빠졌다.

3. Hyundai/Glovis Middle East logistics disruption은 물류 4C-watch다.
   수출 route가 막히면 demand가 있어도 delivery와 비용이 깨진다.

4. Korean Air/Asiana는 항공 통합 Stage 2다.
   하지만 load factor, yield, cost synergy, safety/service quality 전 Green은 아니다.

5. Kumho Tire 공장화재는 direct-listed hard 4C다.
   글로벌 생산능력 20% 가까운 공장이 멈추면 수요논리는 바로 무너진다.

6. Daejeon auto-parts supplier fire는 sector hard 4C다.
   직접 상장사는 아니지만 Hyundai/Kia supply-chain safety gate로 기록해야 한다.

7. Pan Ocean은 cyclical_success다.
   freight-rate cycle은 좋지만 Red Sea normalization이 rate floor를 깨면 Stage 3가 아니다.

8. Lotte Tour / Yellow Balloon tourism rally는 event premium이다.
   관광객 유입 기대보다 tourist spend, occupancy, casino drop, OPM이 Stage 3 조건이다.
```

한 문장으로 압축하면:

> **R9에서 진짜 Stage 3는 “자동차·항공·해운·관광 수요가 좋아진다”가 아니라, tariff-adjusted margin·물류비·route yield·load factor·fleet utilization·safety trust·FCF가 실제로 닫히는 순간이다.**

[1]: https://www.reuters.com/business/autos-transportation/hyundai-motor-targets-30-rise-sales-by-2030-it-expands-hybrid-lineup-2024-08-28/?utm_source=chatgpt.com "Hyundai targets 30% rise in sales by 2030, as it doubles hybrid lineups"
[2]: https://www.reuters.com/world/asia-pacific/south-korea-plans-emergency-response-over-us-tariffs-autos-2025-03-27/?utm_source=chatgpt.com "South Korea plans emergency response over US tariffs on autos"
[3]: https://www.reuters.com/business/autos-transportation/hyundai-motor-flags-export-disruptions-middle-east-conflict-hits-shipping-2026-04-03/?utm_source=chatgpt.com "Hyundai Motor flags export disruptions as Middle East conflict hits shipping"
[4]: https://www.reuters.com/markets/deals/korean-air-completes-asiana-takeover-form-one-asias-biggest-airlines-2024-12-12/?utm_source=chatgpt.com "Korean Air completes Asiana takeover to form one of Asia's biggest airlines"
[5]: https://www.reuters.com/en/south-koreas-kumho-tire-plant-production-suspended-due-fire-2025-05-17/?utm_source=chatgpt.com "South Korea's Kumho Tire plant production suspended due to fire"
[6]: https://www.reuters.com/world/asia-pacific/least-25-hurt-fire-car-parts-factory-south-korea-yonhap-says-2026-03-20/?utm_source=chatgpt.com "Fire at Korean car parts factory kills 14, injures 60"
[7]: https://www.wsj.com/business/autos/auto-transport-roundup-market-talk-b5c8f192?utm_source=chatgpt.com "Auto & Transport Roundup: Market Talk"
[8]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/?utm_source=chatgpt.com "South Korea to offer visa-free entry to Chinese tourists from late September"
