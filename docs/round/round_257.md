순서상 이번은 **R1 Loop 12 — 산업재·수주·인프라 가격경로 검증 라운드**다.

```text
round = R1 Loop 12
round_id = round_185
large_sector = INDUSTRIAL_ORDERS_INFRA
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
```

이번 R1 Loop 12는 이전 R1의 원전·조선 반복을 줄이고, **방산 수주, 미사일 방어, K2 전차 납품/현지생산, 전력망·변압기, 해외 EPC, 정책 CAPEX 실패**를 중심으로 본다. Full adjusted OHLC는 이번 환경에서 안정적으로 확보하지 못했기 때문에, Reuters / WSJ / FT가 제공한 **가격 anchor, 이벤트 수익률, 계약금액, backlog, dilution shock, policy-capex drawdown**만 계산했다. 30D/90D/180D full OHLC가 없는 항목은 명시적으로 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
```

R1에서 제일 위험한 착시는 “수주가 있다 = Stage 3”로 착각하는 것이다.

실제 Stage 3는 **계약 → 납품 → 매출 인식 → 마진 → 현금회수 → 반복 수주**까지 닫힐 때다. 특히 방산·EPC·전력기기는 수주 headline이 강하지만, 현지생산·기술이전·운전자본·증자·정책 CAPEX가 뒤에서 수익률을 갉아먹을 수 있다.

---

# 2. 대상 canonical archetype

```text
DEFENSE_EXPORT_BACKLOG_COMPOUNDING
MISSILE_DEFENSE_COMBAT_VALIDATION
ARMORED_VEHICLE_DELIVERY_TO_REVENUE
GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK
US_GRID_EQUIPMENT_LOCALIZATION
OVERSEAS_EPC_MEGA_ORDER
POLICY_CAPEX_FALSE_POSITIVE
DILUTION_AFTER_RERATING_4B
```

---

# 3. deep sub-archetype

```text
방산 수주:
- Hanwha Aerospace / Romania K9
- LIG Nex1 / Iraq Cheongung-II
- Hyundai Rotem / Poland K2
- backlog, delivery, local production, MRO, missile replenishment

전력망·변압기:
- LS Electric
- Hyosung Heavy / Hyosung HICO
- U.S. transformer shortage
- data-center grid demand
- lead time / slot pre-buying / copper-GOES input cost

해외 EPC:
- Samsung E&A / Saudi Aramco Fadhili
- mega-order event rally
- progress revenue / margin / working capital

반례:
- Hanwha Aerospace dilution after defense rerating
- Hyundai Steel U.S. steel CAPEX policy false positive
```

---

# 4. 국장 신규 후보 case

## Case A — Hanwha Aerospace / Romania K9 `structural_success_candidate + dilution 4B-watch`

```text
symbol = 012450
case_type = structural_success_candidate + 4B-watch
archetype = DEFENSE_EXPORT_BACKLOG_COMPOUNDING / DILUTION_AFTER_RERATING_4B
```

### stage date

```text
Stage 1:
2022~2024
- Russia-Ukraine war 이후 Europe rearmament
- K9 / K10 export cycle
- fast delivery + lower cost + maintenance ecosystem

Stage 2:
2024-07-10
- Romania K9 order 1.38T won / $1B
- 54 K9 howitzers + ammunition + 36 K10 resupply vehicles
- contract runs until July 2029
- Hanwha shares > +5% to record high
- wider market -0.1%
- land-defense backlog 5.1T won at end-2021 → about 30T won by March 2024

Stage 3:
보류
- backlog compounding은 강함
- delivery schedule, margin, working capital, local production economics, cash collection 확인 필요

Stage 4B:
2024-07-10
- record-high event rally

Stage 4B / 4C-watch:
2025-03~04
- 3.6T won capital raise shock
- shares -13%
- FSS revision order
- later 2.3T rights offering + 1.3T affiliate share issue
```

Hanwha Aerospace는 R1 방산 export backlog의 강한 성공 후보지만, 동시에 “대형 수주 후 증자”를 반드시 같이 봐야 하는 case다. Romania K9 계약은 1.38조 원, 약 10억 달러 규모이고, 54문 K9, 탄약, 36대 K10을 포함한다. Reuters는 발표 후 Hanwha Aerospace가 5% 넘게 올라 record high를 찍었고, land-defense backlog가 2021년 말 5.1조 원에서 2024년 3월 약 30조 원으로 늘었다고 보도했다. 그러나 2025년에는 3.6조 원 증자 계획이 투자자 반발과 -13% 급락을 불렀기 때문에, Stage 3와 dilution 4B-watch를 같이 둔다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters order / event-return / dilution anchors

stage3_price:
N/A

Romania_contract_value:
1.38T won / $1.0B

order_scope:
54 K9 howitzers
36 K10 resupply vehicles
ammunition and support package

contract_duration:
until July 2029

stage2_event_MFE:
> +5%

market_same_context:
-0.1%

relative_outperformance:
> +5.1pp

land_defense_backlog_end_2021:
5.1T won

land_defense_backlog_March_2024:
about 30T won

backlog_growth:
30 / 5.1 - 1
= +488.2%

capital_raise_initial:
3.6T won / $2.46B

capital_raise_event_MAE:
-13%

revised_rights_offering:
2.3T won

affiliate_share_issue:
1.3T won

total_revised_related_raise:
3.6T won

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_with_4B_dilution_watch
rerating_result = defense_backlog_compounding_but_capital_raise_risk
stage_failure_type = stage2_strong_not_green_until_delivery_margin_cash
```

---

## Case B — LIG Nex1 / Iraq Cheongung-II `success_candidate + geopolitical 4B-watch`

```text
symbol = 079550
case_type = success_candidate + 4B-watch
archetype = MISSILE_DEFENSE_COMBAT_VALIDATION
```

### stage date

```text
Stage 1:
2024
- Middle East missile-defense demand
- Cheongung-II / M-SAM II export expansion
- Saudi / UAE / Iraq customer base

Stage 2:
2024-09-20
- Iraq missile-system order 3.71T won / $2.8B
- shares +3.6%
- KOSPI +0.9%
- follows Saudi $3.2B deal for 10 M-SAM II batteries

Stage 3:
보류
- order size는 강함
- delivery, missile production rate, margin, replenishment demand, cash collection 확인 필요

Stage 4B:
2026 Iran conflict context
- FT reports LIG Nex1 shares nearly +47% since war began
- Cheongung-II cheaper than Patriot PAC-3 and faster production cycle
```

LIG Nex1은 R1/R11 경계에서 “방산 수주 + 전투검증 기대”가 만나는 case다. Iraq에 3.71조 원, 약 28억 달러 규모 missile-defense system을 수출하는 계약을 따냈고, 발표 후 주가는 3.6% 올랐다. 이후 Iran conflict 구간에서는 Cheongung-II가 Patriot 대체재로 부각되며 FT가 LIG Nex1 주가가 전쟁 이후 거의 47% 올랐다고 보도했다. 다만 실제 Stage 3는 납품·마진·생산능력·반복 보충수요가 확인되어야 한다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters Iraq order anchor / FT geopolitical-rerating anchor

stage3_price:
N/A

Iraq_contract_value:
3.71T won / $2.8B

event_MFE:
+3.6%

KOSPI_same_context:
+0.9%

relative_outperformance:
3.6 - 0.9
= +2.7pp

Saudi_prior_contract:
$3.2B for 10 M-SAM II batteries

Iran_war_return_context:
nearly +47% since war began

Cheongung_II_unit_price_context:
$1.1M per unit

Patriot_PAC3_unit_price_context:
$3.7M per missile

relative_cost_advantage:
1 - 1.1 / 3.7
= 70.3% cheaper

production_cycle_context:
LIG scalable in 9~12 months vs Patriot 4~6 years

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_geopolitical_4B_watch
rerating_result = missile_defense_export_watch
stage_failure_type = stage2_order_not_green_until_delivery_margin_replenishment
```

---

## Case C — Hyundai Rotem / Poland K2 `delivery-to-revenue success_candidate`

```text
symbol = 064350
case_type = success_candidate
archetype = ARMORED_VEHICLE_DELIVERY_TO_REVENUE
```

### stage date

```text
Stage 1:
2022~2024
- Poland first K2 contract
- rapid delivery defense export model
- tank export revenue recognition

Stage 2:
2024-04-09
- shares +9.3% to 41,300 won
- KOSPI -0.3%
- Q1 OP expected +85% YoY to 59.1B won
- consensus 44.4B won
- 18 K2 tanks shipped to Poland
- K2 export revenue expected 270B won, nearly one-third of quarterly revenue

Stage 2 강화:
2025-08-01
- Poland signs second 180 K2 tank contract
- value previously indicated around $6.5B
- 61 tanks to be produced in Poland
- first deliveries planned 2026
- Polish production planned 2028~2030

Stage 3:
보류
- delivery-to-revenue evidence는 좋음
- second-batch margin, local-production economics, working capital, cash collection 확인 필요
```

Hyundai Rotem은 R1에서 단순 수주보다 한 단계 좋은 “납품 → 매출” evidence가 있는 case다. WSJ는 Poland향 K2 18대 출하가 분기 매출 2,700억 원에 기여할 것으로 예상됐고, 이 기대에 주가가 9.3% 오른 41,300원을 기록했다고 보도했다. 이후 Poland는 두 번째 180대 K2 계약도 체결했고, Reuters는 해당 계약이 약 65억 달러로 제시됐으며 61대는 Poland에서 생산된다고 보도했다. ([월스트리트저널][3])

### 실제 가격경로 검증

```text
price_data_source:
WSJ price/earnings anchor + Reuters second-contract anchor

stage3_price:
N/A

stage2_event_price:
41,300 won

event_MFE:
+9.3%

KOSPI_same_context:
-0.3%

relative_outperformance:
9.3 - (-0.3)
= +9.6pp

Q1_OP_forecast:
59.1B won

Q1_OP_growth_forecast:
+85% YoY

consensus_OP:
44.4B won

OP_forecast_vs_consensus:
59.1 / 44.4 - 1
= +33.1%

K2_tanks_shipped_to_Poland:
18 units

K2_export_revenue_Q1:
270B won

second_contract:
180 K2 tanks

second_contract_value:
about $6.5B

local_production:
61 tanks in Poland

first_deliveries:
2026

Polish_production:
2028~2030

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = armored_vehicle_delivery_to_revenue_watch
stage_failure_type = stage2_delivery_evidence_not_green_until_margin_cash
```

---

## Case D — LS Electric / U.S. data-center transformer `success_candidate + price_data_unavailable`

```text
symbol = 010120
case_type = success_candidate + insufficient_price_data
archetype = GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK
```

### stage date

```text
Stage 1:
2025~2026
- U.S. transformer shortage
- data-center / factory / EV / renewable grid demand
- South Korea transformer export opportunity

Stage 2:
2025-11
- LS Electric announces $312M U.S. utility contract
- 525kV extra-high-voltage transformers
- supply to large-scale southeastern U.S. data center
- delivery 2027~2029

Stage 3:
없음
- contract는 강한 Stage 2
- production slot, margin, copper/GOES cost, delivery, cash collection 확인 필요

Stage 4B:
U.S. transformer super-cycle narrative로 valuation이 먼저 확장되면 후보

Stage 4C:
lead-time delay, input cost spike, U.S. localization risk, contract execution failure
```

LS Electric은 R1 전력망/변압기 bottleneck의 좋은 Stage 2다. Reuters는 U.S. transformer shortage가 data center, EV, factory, renewable grid 수요로 심해졌고, U.S. GSU transformer 수요가 2019~2025년 274%, substation transformer 수요가 116% 증가했다고 보도했다. 같은 기사에서 LS Electric은 2025년 11월 미국 utility와 3.12억 달러 계약을 맺고 525kV 초고압 변압기를 2027~2029년 southeastern U.S. 대형 data center에 공급한다고 언급됐다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters transformer-shortage / LS Electric contract anchor

stage3_price:
N/A

LS_Electric_contract:
$312M

product:
525kV extra-high-voltage transformers

customer:
U.S. utility

end_demand:
large-scale data center in southeastern U.S.

delivery_period:
2027~2029

U.S._GSU_transformer_demand_growth_2019_2025:
+274%

U.S._substation_transformer_demand_growth_2019_2025:
+116%

transformer_price_increase_5Y:
about +80%

large_transformer_lead_time:
up to 4 years

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_insufficient_price_data
rerating_result = grid_transformer_data_center_watch
stage_failure_type = stage2_contract_not_green_until_margin_delivery_cash
```

---

## Case E — Hyosung Heavy / Hyosung HICO `success_candidate + U.S. localization capex watch`

```text
symbol = 298040
case_type = success_candidate + capex_watch
archetype = US_GRID_EQUIPMENT_LOCALIZATION
```

### stage date

```text
Stage 1:
2025~2026
- U.S. grid bottleneck
- transformer supply shortage
- data-center and manufacturing power demand
- U.S. localization incentive

Stage 2:
2025-12
- Reuters reports Hyosung HICO among suppliers expanding U.S. grid-equipment production
- Hyosung HICO investment $157M
- global grid suppliers invest to ease supply shortage
- GSU transformer lead time around 143 weeks
- U.S. demand far outstrips supply

Stage 3:
없음
- localization capex만으로 Green 금지
- firm order backlog, utilization, margin, FCF 확인 필요

Stage 4B:
grid-equipment super-cycle이 실적보다 먼저 price에 반영되면 후보

Stage 4C:
U.S. factory ramp delay, copper/GOES cost, demand normalization, policy/regulatory bottleneck
```

Hyosung Heavy는 U.S. grid equipment localization의 Stage 2 후보로 둘 수 있다. Reuters는 grid-equipment makers가 미국 transformer shortage에 대응하기 위해 투자하고 있으며, Hyosung HICO도 1.57억 달러를 투자한다고 보도했다. U.S. GSU transformer lead time은 평균 143주로 제시됐다. 그러나 투자계획은 Green이 아니라 capacity Stage 2다. 실제 order backlog, utilization, OPM, FCF가 필요하다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters grid-equipment localization anchor

stage3_price:
N/A

Hyosung_HICO_U.S._investment:
$157M

GSU_transformer_demand_growth_2019_2025:
+274%

GSU_lead_time:
143 weeks average

drivers:
renewable generation
data centers
manufacturing
EVs
aging grid modernization

MFE / MAE:
price_data_unavailable_after_deep_search

reason:
- Reuters source gives industry investment and demand data.
- It does not provide Hyosung Heavy adjusted OHLC in this pass.
```

### alignment

```text
score_price_alignment = success_candidate_capex_watch
rerating_result = U.S._grid_equipment_localization_watch
stage_failure_type = stage2_capacity_not_green
```

---

## Case F — Samsung E&A / Saudi Fadhili `event_premium / EPC Stage 2`

```text
symbol = 028050
case_type = event_premium + success_candidate
archetype = OVERSEAS_EPC_MEGA_ORDER
```

### stage date

```text
Stage 1:
2024-04
- Saudi Aramco gas infrastructure expansion
- Middle East EPC cycle

Stage 2:
2024-04-03
- Samsung E&A wins estimated $6B Fadhili contract
- Aramco Fadhili package $7.7B
- gas capacity +60% to 4.0B cf/d
- sulfur production +2,300 metric tons
- completion expected November 2027
- shares +8.5% to 26,750 won
- KOSPI -1.4%

Stage 3:
없음
- signed mega-order는 Stage 2
- progress revenue, margin, working capital, cash collection 확인 전 Green 금지

Stage 4B:
2024-04-03
- +8.5% event rally before margin / cash collection
```

Samsung E&A는 R10에서도 봤지만, R1 EPC calibration에는 계속 필요한 기준점이다. 계약 규모는 크고 event return도 컸지만, EPC 특성상 원가율·공정률·운전자본이 확인되기 전에는 Stage 3가 아니다. ([월스트리트저널][6])

### 실제 가격경로 검증

```text
price_data_source:
WSJ contract / event-return anchor

stage3_price:
N/A

event_price:
26,750 won

event_MFE:
+8.5%

implied_prior_price:
26,750 / 1.085
= 24,654 won

KOSPI_same_context:
-1.4%

relative_outperformance:
+9.9pp

contract_value:
about $6B

Aramco_total_project:
$7.7B

contract_share:
6.0 / 7.7
= 77.9%

capacity_increase:
+60%

target_price:
35,000 won

target_upside:
35,000 / 26,750 - 1
= +30.8%

MFE_30D / MAE_30D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium_success_candidate
rerating_result = EPC_mega_order_watch
stage_failure_type = contract_stage2_not_green
```

---

## Case G — Hyundai Steel U.S. plant `failed_rerating / policy CAPEX false positive`

```text
symbol = 004020
case_type = failed_rerating
archetype = POLICY_CAPEX_FALSE_POSITIVE
```

### stage date

```text
Stage 1:
2025-03
- U.S. tariff pressure
- Hyundai Motor Group U.S. investment package
- automotive steel localization narrative

Stage 2:
2025-03-25
- Hyundai Steel announces $5.8B Louisiana plant
- annual capacity 2.7M tonnes
- part of Hyundai Motor Group $21B U.S. package
- shares initially > +5%, then -4.4% same session

Stage 4C-watch:
2025-04-22
- stock lost 21.2% since announcement
- funding details unclear
- project may be political signaling
- 50% funded by borrowing, rest unclear
- POSCO potential equity investor
- benchmark -5.5%, POSCO -18.3%

Stage 3:
없음
- policy CAPEX와 tariff hedge만으로 Green 금지
- customer demand, funding, margin, FCF, tariff benefit 확인 필요
```

Hyundai Steel은 R1의 대표 failed-rerating case다. 미국 tariff 대응과 자동차 steel localization이라는 말은 좋아 보였지만, 발표 당일 주가는 +5%에서 -4.4%로 뒤집혔고, 이후 -21.2%까지 밀렸다. Reuters는 투자자들이 funding detail과 장기 tariff benefit에 의문을 제기했다고 보도했다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters U.S. steel plant / funding-uncertainty anchors

stage3_price:
N/A

plant_investment:
$5.8B

annual_capacity:
2.7M tonnes

group_U.S._investment_package:
$21B

announcement_initial_MFE:
> +5%

announcement_session_MAE:
-4.4%

post_announcement_drawdown:
-21.2%

POSCO_same_period:
-18.3%

KOSPI_same_period:
-5.5%

relative_underperformance_vs_KOSPI:
-21.2 - (-5.5)
= -15.7pp

funding_plan:
50% borrowing, remaining funding unclear

potential_POSCO_equity:
under discussion

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = false_positive_score_prevention
rerating_result = policy_capex_failed_rerating
stage_failure_type = policy_capex_not_green
```

---

## Case H — Hanwha Aerospace capital raise `4B-watch / dilution after rerating`

```text
symbol = 012450
case_type = 4B-watch
archetype = DILUTION_AFTER_RERATING_4B
```

### stage date

```text
Stage 1:
2024~2025
- defense export boom
- overseas factories / missile / engine / drone investment need

Stage 2:
2025-03-21
- 3.6T won capital raise plan
- purpose: overseas production expansion, drone / engine / defense technologies

Stage 4B / 4C-watch:
2025-03-27
- market watchdog orders revised filing
- stock -13%
- worst day since Nov 2016
- investors question purpose and necessity

Stage 2 revision:
2025-04-18
- 1.3T won affiliate share issue at 758,000 won/share
- separate 2.3T rights offering
```

Hanwha Aerospace는 좋은 방산 수주 cycle이지만, 주가가 크게 오른 뒤 대형 증자를 하면 4B-watch가 즉시 떠야 한다. Reuters는 3.6조 원 증자 계획 후 주가가 13% 하락했고, 금융감독원이 투자자가 합리적으로 판단하기에 필요한 정보가 부족하다며 정정신고를 요구했다고 보도했다. 이후 1.3조 원 affiliate share issue와 2.3조 원 rights offering 구조로 바뀌었다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters capital-raise / dilution anchors

stage3_price:
N/A

initial_capital_raise:
3.6T won / $2.46B

capital_raise_event_MAE:
-13%

revised_affiliate_share_issue:
1.3T won

affiliate_issue_price:
758,000 won/share

separate_rights_offering:
2.3T won

total_revised_related_raise:
3.6T won

use_of_proceeds:
drones
engines
overseas defense expansion
production capacity

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = 4B_watch
rerating_result = defense_rerating_dilution_risk
stage_failure_type = dilution_after_rerating
```

---

# 5. 이번 R1 case별 요약표

| case                           | 분류                                     |                                                         실제 가격검증 | alignment                |
| ------------------------------ | -------------------------------------- | --------------------------------------------------------------: | ------------------------ |
| Hanwha Aerospace Romania K9    | structural_success_candidate + 4B      |    +5% record high, backlog 5.1T→30T, later -13% dilution shock | success + dilution watch |
| LIG Nex1 Iraq / Cheongung-II   | success_candidate + 4B                 |                    +3.6%, relative +2.7pp, Iran-war period +47% | missile-defense watch    |
| Hyundai Rotem K2 Poland        | success_candidate                      |        +9.3% to 41,300원, K2 revenue 270B, second contract $6.5B | delivery-to-revenue      |
| LS Electric transformer        | success_candidate / insufficient price | $312M U.S. data-center transformer order, U.S. GSU demand +274% | grid bottleneck          |
| Hyosung Heavy / HICO           | success_candidate / capex watch        |                   $157M U.S. expansion, GSU lead time 143 weeks | localization Stage 2     |
| Samsung E&A Fadhili            | event premium                          |                 +8.5% to 26,750원, $6B contract, relative +9.9pp | EPC Stage 2              |
| Hyundai Steel U.S. plant       | failed_rerating                        |                       +5% → -4.4%, then -21.2%, funding unclear | policy CAPEX fail        |
| Hanwha Aerospace capital raise | 4B-watch                               |                        3.6T won raise, -13%, FSS revision order | dilution 4B              |

---

# 6. score-price alignment 판정

```text
structural_success_candidate:
- Hanwha Aerospace
- LIG Nex1
- Hyundai Rotem

success_candidate_but_insufficient_price_data:
- LS Electric
- Hyosung Heavy / HICO

event_premium:
- Samsung E&A Fadhili +8.5%
- LIG Nex1 geopolitical rerating
- Hanwha Aerospace Romania contract record-high rally

failed_rerating:
- Hyundai Steel U.S. steel plant

4B-watch:
- Hanwha Aerospace dilution after rerating
- Samsung E&A contract rally before margin/cash collection
- LIG Nex1 Iran-war +47% if price outruns delivery/margin
- Hyundai Rotem second K2 contract if local-production economics not confirmed

hard_4C:
- hard_4C_not_confirmed
```

이번 R1 Loop 12에서 hard 4C는 억지로 확정하지 않는다. 대신 **Hyundai Steel policy CAPEX failure**와 **Hanwha Aerospace dilution shock**을 false-positive / 4B-watch calibration으로 강하게 둔다.

---

# 7. 점수비중 교정

## 올릴 축

```text
confirmed_order +5
delivery_to_revenue +5
backlog_compounding +5
local_production_economics +4
MRO_or_aftermarket_revenue +4
production_capacity_visibility +4
cash_collection_quality +5
working_capital_control +5
repeat_export_customer +4
price_path_alignment +5
```

### 왜 올리나

Hyundai Rotem은 K2 18대 출하가 분기 매출 2,700억 원으로 연결될 수 있다는 점이 확인됐다. Hanwha Aerospace는 Romania K9 수주와 backlog compounding이 강하다. LIG Nex1은 Iraq·Saudi customer expansion과 missile-defense system status가 뚜렷하다. LS Electric과 Hyosung은 U.S. grid bottleneck이라는 구조가 있다. 다만 모두 **delivery, margin, cash collection** 전에는 Green을 제한한다.

## 내릴 축

```text
contract_headline_only -5
policy_capex_without_funding -5
local_production_without_margin -4
defense_rally_without_delivery -4
EPC_order_without_working_capital -5
capacity_expansion_without_order -4
dilution_after_rerating -5
unconfirmed_geopolitical_replenishment -4
input_cost_unknown -3
```

### 왜 내리나

Hyundai Steel은 policy CAPEX만으로는 Green이 될 수 없다는 반례다. Hanwha Aerospace는 좋은 수주에도 증자가 4B risk를 만든다. Samsung E&A는 수주는 강하지만 EPC margin·working capital 전에는 Stage 2다. LS/Hyosung은 transformer shortage가 있어도 납품·마진·원재료 cost가 필요하다.

## Green gate 강화 조건

```text
R1 Stage 3-Green 필수:
1. confirmed order
2. delivery schedule 확인
3. delivery-to-revenue 또는 progress revenue 확인
4. OPM / gross margin 확인
5. working capital / receivables / cash collection 안정
6. local-production economics 확인
7. capex/dilution risk 통과
8. repeat customer / aftermarket / MRO revenue 확인
9. 가격경로가 evidence 이후 따라옴

금지:
수주 headline만 있음
정책 CAPEX만 있음
공장투자만 있음
현지생산 margin 불명
증자 shock 존재
운전자본 악화
geopolitical headline만 있음
```

## 4B 조기감지 조건

```text
4B-watch:
계약 발표일 +5~10% 급등
방산주 record high 이후 대형 증자
전쟁·지정학으로 방산주 +30~50% 급등
수주잔고는 크지만 납품·마진 미확인
EPC mega-order 발표 후 margin 확인 전 rally
전력망 shortage theme으로 capacity/value가 먼저 반영
현지생산·기술이전이 수익성보다 먼저 가격화

4B-elevated:
대형 rights offering / CB / affiliate issue
local production capex 증가
working capital 급증
계약 수주 후 매출 인식 지연
원재료 cost spike
고객·정부 예산 지연
```

## 4C hard gate 조건

```text
contract cancellation
export-license failure
customer budget cancellation
delivery delay
local-production margin failure
working-capital blowout
large dilution without clear ROI
policy CAPEX failure
factory ramp failure
geopolitical customer payment risk
EPC loss recognition
```

이번 R1 Loop 12에서는 hard 4C를 확정하지 않는다. 대신 `policy_capex_false_positive`, `dilution_after_rerating`, `contract_headline_not_green` 세 축을 shadow score에서 강하게 올린다.

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

## docs/round/round_185.md 요약

```md
# R1 Loop 12. Industrial Orders / Infrastructure Price Validation

이번 라운드는 R1 Loop 12 price-validation 라운드다.

핵심 결론:
- Hanwha Aerospace Romania K9 is strong defense-export Stage 2. It won a 1.38T won / $1B contract for 54 K9 howitzers, ammunition and 36 K10 vehicles. Shares rose more than 5% to a record high, while land-defense backlog grew from 5.1T won to about 30T won. But the later 3.6T won capital raise and -13% selloff require dilution 4B-watch.
- LIG Nex1 Iraq Cheongung-II is missile-defense Stage 2. Iraq order 3.71T won / $2.8B, shares +3.6% vs KOSPI +0.9%. Iran-war period reportedly lifted shares nearly +47%, so geopolitical 4B-watch is required.
- Hyundai Rotem K2 Poland is delivery-to-revenue Stage 2. Shares +9.3% to 41,300 won on expected Q1 OP +85% YoY and 270B won K2 export revenue from 18 tanks. Poland later signed second 180-tank contract indicated at about $6.5B.
- LS Electric is grid-transformer Stage 2. Reuters reports a $312M U.S. utility contract for 525kV transformers to a southeastern U.S. data center, amid U.S. GSU transformer demand +274% and transformer prices +80% over five years.
- Hyosung Heavy / HICO is U.S. grid-equipment localization Stage 2. Hyosung HICO investment $157M, with average GSU transformer lead time around 143 weeks.
- Samsung E&A Fadhili is EPC Stage 2 plus 4B-watch. Shares +8.5% to 26,750 won on estimated $6B Saudi Aramco contract, but progress revenue, margin and cash collection are required.
- Hyundai Steel U.S. plant is failed-rerating / policy CAPEX false positive. Initial +5% reversed to -4.4%, then shares lost -21.2% after unclear funding and strategic uncertainty.
- Hanwha Aerospace capital raise is 4B-watch. 3.6T won raise plan triggered -13% and FSS revision order; later structure was 2.3T rights offering plus 1.3T affiliate share issue.
```

## docs/checkpoints/checkpoint_28a_round185_r1_loop12.md 요약

```md
# Checkpoint 28A Round 185 R1 Loop 12 Industrial Orders Infra Price Validation

## 반영 내용
- R1 Loop 12 price-validation 라운드를 추가했다.
- Defense export backlog, missile-defense combat validation, armored-vehicle delivery-to-revenue, grid-transformer data-center bottleneck, U.S. grid-equipment localization, EPC mega-order, policy CAPEX false positive, dilution after rerating을 비교했다.
- Reuters / WSJ / FT anchors로 가능한 MFE/MAE 및 event metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- confirmed order, delivery-to-revenue, backlog compounding, local-production economics, MRO/aftermarket, working-capital control, cash collection 가중치 강화
- contract headline-only, policy CAPEX without funding, EPC order without margin, capacity expansion without order, dilution after rerating 감점 강화
```

## data/e2r_case_library/cases_r1_loop12_round185.jsonl 초안

```jsonl
{"case_id":"r1_loop12_hanwha_aerospace_romania_k9_dilution_watch","symbol":"012450","company_name":"Hanwha Aerospace","case_type":"success_candidate","primary_archetype":"DEFENSE_EXPORT_BACKLOG_COMPOUNDING","stage2_date":"2024-07-10","stage4b_date":"2024-07-10/2025-03","price_validation":{"price_data_source":"Reuters order/event/dilution anchors","stage3_price":null,"romania_contract_krw_trn":1.38,"romania_contract_usd_bn":1.0,"order_scope":["54 K9 howitzers","36 K10 resupply vehicles","ammunition/support package"],"contract_duration":"until_2029-07","stage2_event_mfe_pct":5.0,"market_same_context_pct":-0.1,"relative_outperformance_pp":5.1,"backlog_end_2021_krw_trn":5.1,"backlog_march_2024_krw_trn":30,"backlog_growth_pct":488.2,"capital_raise_initial_krw_trn":3.6,"capital_raise_event_mae_pct":-13,"revised_rights_offering_krw_trn":2.3,"affiliate_share_issue_krw_trn":1.3,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_with_4B_dilution_watch","rerating_result":"defense_backlog_compounding_but_capital_raise_risk","notes":"Strong export backlog, but delivery/margin/cash collection and dilution risk must be checked before Green."}
{"case_id":"r1_loop12_lig_nex1_iraq_cheongung_missile_defense","symbol":"079550","company_name":"LIG Nex1","case_type":"success_candidate","primary_archetype":"MISSILE_DEFENSE_COMBAT_VALIDATION","stage2_date":"2024-09-20","stage4b_date":"2026-iran_conflict_context","price_validation":{"price_data_source":"Reuters Iraq order / FT geopolitical rerating anchors","stage3_price":null,"iraq_contract_krw_trn":3.71,"iraq_contract_usd_bn":2.8,"event_mfe_pct":3.6,"kospi_same_context_pct":0.9,"relative_outperformance_pp":2.7,"saudi_prior_contract_usd_bn":3.2,"iran_war_return_context_pct":47,"cheongung_unit_price_usd_mn":1.1,"patriot_pac3_unit_price_usd_mn":3.7,"relative_cost_advantage_pct":70.3,"production_cycle_context":"9-12 months vs Patriot 4-6 years","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_geopolitical_4B_watch","rerating_result":"missile_defense_export_watch","notes":"Large Iraq order and combat-validation narrative; delivery/margin/replenishment demand required before Green."}
{"case_id":"r1_loop12_hyundai_rotem_k2_poland_delivery_to_revenue","symbol":"064350","company_name":"Hyundai Rotem","case_type":"success_candidate","primary_archetype":"ARMORED_VEHICLE_DELIVERY_TO_REVENUE","stage2_date":"2024-04-09/2025-08-01","price_validation":{"price_data_source":"WSJ price/earnings anchor + Reuters second-contract anchor","stage3_price":null,"stage2_event_price_krw":41300,"event_mfe_pct":9.3,"kospi_same_context_pct":-0.3,"relative_outperformance_pp":9.6,"q1_op_forecast_krw_bn":59.1,"q1_op_growth_forecast_pct":85,"consensus_op_krw_bn":44.4,"op_forecast_vs_consensus_pct":33.1,"k2_tanks_shipped_to_poland":18,"k2_export_revenue_q1_krw_bn":270,"second_contract_tanks":180,"second_contract_value_usd_bn":6.5,"local_production_tanks":61,"first_deliveries":2026,"polish_production":"2028-2030","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"armored_vehicle_delivery_to_revenue_watch","notes":"Delivery-to-revenue evidence is better than headline order; local-production margin/cash collection required before Green."}
{"case_id":"r1_loop12_ls_electric_us_datacenter_transformer","symbol":"010120","company_name":"LS Electric","case_type":"success_candidate","primary_archetype":"GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK","stage2_date":"2025-11","price_validation":{"price_data_source":"Reuters transformer-shortage / LS Electric contract anchor","stage3_price":null,"contract_value_usd_mn":312,"product":"525kV extra-high-voltage transformers","customer":"U.S. utility","end_demand":"large-scale data center in southeastern U.S.","delivery_period":"2027-2029","us_gsu_transformer_demand_growth_pct":274,"us_substation_transformer_demand_growth_pct":116,"transformer_price_increase_5y_pct":80,"large_transformer_lead_time_years":4,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_insufficient_price_data","rerating_result":"grid_transformer_data_center_watch","notes":"Strong U.S. grid/data-center Stage 2, but margin, delivery, input costs and cash collection required before Green."}
{"case_id":"r1_loop12_hyosung_hico_us_grid_equipment_localization","symbol":"298040","company_name":"Hyosung Heavy / Hyosung HICO","case_type":"success_candidate","primary_archetype":"US_GRID_EQUIPMENT_LOCALIZATION","stage2_date":"2025-12","price_validation":{"price_data_source":"Reuters grid-equipment localization anchor","stage3_price":null,"hyosung_hico_us_investment_usd_mn":157,"gsu_transformer_demand_growth_pct":274,"gsu_lead_time_weeks":143,"drivers":["renewable generation","data centers","manufacturing","EVs","aging grid modernization"],"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_capex_watch","rerating_result":"U.S._grid_equipment_localization_watch","notes":"Capacity localization is Stage 2; firm orders, utilization, margin and FCF required before Green."}
{"case_id":"r1_loop12_samsung_ea_fadhili_epc_stage2","symbol":"028050","company_name":"Samsung E&A","case_type":"event_premium","primary_archetype":"OVERSEAS_EPC_MEGA_ORDER","stage2_date":"2024-04-03","stage4b_date":"2024-04-03","price_validation":{"price_data_source":"WSJ contract/event-return anchor","stage3_price":null,"event_price_krw":26750,"event_mfe_pct":8.5,"implied_prior_price_krw":24654,"kospi_same_context_pct":-1.4,"relative_outperformance_pp":9.9,"contract_value_usd_bn":6.0,"aramco_total_project_usd_bn":7.7,"contract_share_pct":77.9,"capacity_increase_pct":60,"target_price_krw":35000,"target_upside_pct":30.8,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"EPC_mega_order_watch","notes":"Signed mega-order is Stage 2 and 4B-watch; progress revenue, margin, working capital and cash collection required before Green."}
{"case_id":"r1_loop12_hyundai_steel_us_policy_capex_false_positive","symbol":"004020","company_name":"Hyundai Steel","case_type":"failed_rerating","primary_archetype":"POLICY_CAPEX_FALSE_POSITIVE","stage2_date":"2025-03-25","stage4c_date":"2025-04-22_watch","price_validation":{"price_data_source":"Reuters U.S. steel plant/funding uncertainty anchors","stage3_price":null,"plant_investment_usd_bn":5.8,"annual_capacity_mn_tonnes":2.7,"group_us_investment_package_usd_bn":21,"announcement_initial_mfe_pct":5.0,"announcement_session_mae_pct":-4.4,"post_announcement_drawdown_pct":-21.2,"posco_same_period_pct":-18.3,"kospi_same_period_pct":-5.5,"relative_underperformance_vs_kospi_pp":-15.7,"funding_plan":"50% borrowing; remaining funding unclear","potential_posco_equity":"under discussion","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"false_positive_score_prevention","rerating_result":"policy_capex_failed_rerating","notes":"Policy CAPEX and tariff hedge are not Green without funding, customers, margin and FCF."}
{"case_id":"r1_loop12_hanwha_aerospace_capital_raise_dilution_4b","symbol":"012450","company_name":"Hanwha Aerospace","case_type":"4b_watch","primary_archetype":"DILUTION_AFTER_RERATING_4B","stage4b_date":"2025-03/2025-04","price_validation":{"price_data_source":"Reuters capital-raise/dilution anchors","stage3_price":null,"initial_capital_raise_krw_trn":3.6,"initial_capital_raise_usd_bn":2.46,"capital_raise_event_mae_pct":-13,"revised_affiliate_share_issue_krw_trn":1.3,"affiliate_issue_price_krw":758000,"separate_rights_offering_krw_trn":2.3,"total_revised_related_raise_krw_trn":3.6,"use_of_proceeds":["drones","engines","overseas defense expansion","production capacity"],"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"4B_watch","rerating_result":"defense_rerating_dilution_risk","notes":"Large capital raise after defense rerating is 4B/dilution watch."}
```

## data/sector_taxonomy/score_weight_profiles_round185_r1_loop12_v1.csv 초안

```csv
archetype,confirmed_order,delivery_to_revenue,backlog_compounding,local_production_economics,mro_aftermarket,production_capacity,cash_collection,working_capital,repeat_customer,price_path_alignment,event_penalty,dilution_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
DEFENSE_EXPORT_BACKLOG_COMPOUNDING,+5,+5,+5,+4,+4,+4,+5,+5,+4,+5,-2,+5,+5,+4,Hanwha/HRI/LIG show strong Stage 2 but delivery/margin/cash collection and dilution must clear.
MISSILE_DEFENSE_COMBAT_VALIDATION,+5,+4,+5,+4,+5,+5,+5,+4,+5,+5,-2,+2,+5,+4,LIG Nex1 has Iraq/Saudi orders and geopolitical validation, but replenishment/margin must confirm.
ARMORED_VEHICLE_DELIVERY_TO_REVENUE,+5,+5,+5,+4,+4,+4,+5,+5,+5,+5,-2,+2,+4,+4,Hyundai Rotem has delivery-to-revenue evidence; local production economics remain key.
GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK,+5,+4,+4,+2,+2,+5,+5,+5,+4,+4,-2,+1,+4,+4,LS Electric benefits from data-center transformer bottleneck but needs margin/input-cost/delivery proof.
US_GRID_EQUIPMENT_LOCALIZATION,+4,+3,+4,+4,+2,+5,+4,+5,+4,+3,-3,+2,+4,+4,Hyosung/HICO capacity localization is Stage 2 until utilization/order book/FCF confirm.
OVERSEAS_EPC_MEGA_ORDER,+5,+5,+4,+2,+1,+3,+5,+5,+4,+5,-5,+2,+5,+5,Samsung E&A shows EPC contract headline is not Green without margin/cash collection.
POLICY_CAPEX_FALSE_POSITIVE,+2,+1,+1,+1,+0,+3,+3,+5,+1,+5,-5,+4,+5,+5,Hyundai Steel U.S. plant is policy CAPEX false positive due funding and strategy uncertainty.
DILUTION_AFTER_RERATING_4B,+0,+0,+0,+0,+0,+2,+3,+5,+0,+4,-5,+5,+5,+4,Hanwha capital raise after rerating requires 4B/dilution penalty.
```

---

# 이번 R1 Loop 12 결론

```text
1. Hanwha Aerospace는 방산 수주 구조가 강하다.
   하지만 대형 증자 shock 때문에 Green과 4B-watch를 동시에 둬야 한다.

2. LIG Nex1은 missile-defense export Stage 2가 강하다.
   Iraq/Saudi 수주와 Iran-war rerating은 좋지만, delivery/margin/replenishment 전 Green은 아니다.

3. Hyundai Rotem은 delivery-to-revenue evidence가 있어 R1에서 높은 품질의 Stage 2다.
   다만 Poland local production economics와 cash collection 전 Stage 3는 보류다.

4. LS Electric과 Hyosung은 U.S. grid/transformer bottleneck의 좋은 Stage 2다.
   하지만 price path와 margin/input cost가 확보되지 않아 insufficient_price_data다.

5. Samsung E&A는 mega EPC order Stage 2다.
   +8.5% rally는 margin/working capital 전 4B-watch다.

6. Hyundai Steel U.S. plant는 policy CAPEX false positive다.
   funding 불확실성과 -21.2% drawdown 때문에 Green gate를 강화해야 한다.

7. 이번 R1 Loop 12에서는 hard 4C를 억지로 확정하지 않는다.
   대신 dilution_after_rerating, policy_capex_false_positive, contract_headline_not_green을 shadow weight에 강하게 반영한다.
```

한 문장으로 압축하면:

> **R1에서 진짜 Stage 3는 “방산·EPC·전력망 수주가 있다”가 아니라, 그 수주가 납품·매출·마진·현금회수로 닫히고, 증자·현지생산·운전자본·정책 CAPEX 리스크를 통과하는 순간이다.**

* [Reuters](https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-wins-1-bln-order-romania-k9-howitzers-2024-07-09/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/aerospace-defense/south-koreas-lig-nex1-wins-28-bln-deal-with-iraq-export-missile-systems-2024-09-19/?utm_source=chatgpt.com)
* [월스트리트저널](https://www.wsj.com/articles/hyundai-rotem-rallies-on-hopes-tank-exports-will-boost-earnings-9322d840?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/emerging/poland-signs-contract-buy-more-south-korean-battle-tanks-2025-08-01/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/energy/us-power-transformer-buyers-scramble-imports-factory-slots--reeii-2026-05-11/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/energy/grid-equipment-makers-invest-us-ease-supply-shortage--reeii-2025-12-02/?utm_source=chatgpt.com)
* [월스트리트저널](https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/autos-transportation/hyundai-steels-6-bln-us-investment-draws-investor-ire-tests-seouls-tariff-2025-04-22/?utm_source=chatgpt.com)

[1]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-wins-1-bln-order-romania-k9-howitzers-2024-07-09/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace wins $1 bln order from Romania for self-propelled howitzers"
[2]: https://www.reuters.com/business/aerospace-defense/south-koreas-lig-nex1-wins-28-bln-deal-with-iraq-export-missile-systems-2024-09-19/?utm_source=chatgpt.com "South Korea's LIG Nex1 wins $2.8 bln Iraq deal to export missile systems"
[3]: https://www.wsj.com/articles/hyundai-rotem-rallies-on-hopes-tank-exports-will-boost-earnings-9322d840?utm_source=chatgpt.com "Hyundai Rotem Rallies on Hopes Tank Exports Will Boost Earnings"
[4]: https://www.reuters.com/business/energy/us-power-transformer-buyers-scramble-imports-factory-slots--reeii-2026-05-11/?utm_source=chatgpt.com "US power transformer buyers scramble for imports, factory slots"
[5]: https://www.reuters.com/business/energy/grid-equipment-makers-invest-us-ease-supply-shortage--reeii-2025-12-02/?utm_source=chatgpt.com "Grid equipment makers invest in US to ease supply shortage"
[6]: https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4?utm_source=chatgpt.com "Samsung E&A Shares Rise on $6 Billion Saudi Contract Win"
[7]: https://www.reuters.com/markets/commodities/hyundai-steel-build-plant-louisiana-with-annual-output-27-million-tonnes-2025-03-25/?utm_source=chatgpt.com "Hyundai Steel unveils US factory plan, shares skid"
[8]: https://www.reuters.com/business/aerospace-defense/south-korea-market-watchdog-orders-hanwha-aerospace-revise-share-issuance-plan-2025-03-27/?utm_source=chatgpt.com "S. Korea watchdog blocks Hanwha Aerospace $2.5 billion capital raising plan"
