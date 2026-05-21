순서상 이번은 **R4 Loop 10 — 소재·스프레드·전략자원 가격경로 검증 라운드**다.

이번 R4는 “전략자원”, “구조조정”, “리튬”, “정유 스프레드”, “비중국 공급망”처럼 좋아 보이는 말들을 모두 한 번씩 의심한다. R4에서 Stage 3는 원자재 뉴스가 아니라 **스프레드·offtake·cost curve·현금흐름·공급규율이 실제 이익 체급으로 잠기는 순간**이다.

```text
round = R4 Loop 10
round_id = round_162
large_sector = MATERIALS_SPREAD_STRATEGIC_RESOURCES
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
```

---

# 1. 이번 라운드 대섹터

```text
R4 = 소재·스프레드·전략자원
```

R4는 다른 섹터보다 **가격 그 자체가 속임수**가 되기 쉽다. 원자재 가격이 오르면 모든 게 좋아 보이고, 구조조정 뉴스가 나오면 바닥을 친 것처럼 보이고, 전략광물 뉴스가 나오면 바로 장기 성장주처럼 보인다. 하지만 E2R에서는 그걸 바로 Green으로 올리지 않는다.

---

# 2. 대상 canonical archetype

```text
STRATEGIC_MINERALS_SUPPLY_CHAIN
CRITICAL_MINERALS_US_REFINERY
GOVERNANCE_DILUTION_EVENT
PETROCHEMICAL_RESTRUCTURING_KOREA
REFINING_SPREAD_CYCLE
LITHIUM_RESOURCE_SECURITY
LITHIUM_CYCLE_OVERLAY
STEEL_POLICY_CAPEX_TARIFF_HEDGE
BUILDING_MATERIALS_DEMAND_CYCLE
BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK
POLYSILICON_NON_CHINA_SUPPLY_OPTION
COPPER_PROCESSING_PLUS_DEFENSE
M_AND_A_OPTIONALITY_EVENT
PRICE_ONLY_RALLY
EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
전략광물:
- Korea Zinc
- antimony / rare earth recycling / gallium / germanium
- U.S. critical-minerals refinery
- U.S. government-linked funding
- governance / dilution / share-sale risk

석유화학:
- Lotte Chemical
- HD Hyundai Chemical
- Daesan NCC shutdown
- China / Middle East oversupply
- restructuring relief vs true spread recovery

정유:
- SK Innovation
- S-Oil
- crack spread
- Middle East disruption
- battery-unit drag
- cyclical rebound vs structural Stage 3

리튬 / 원재료:
- POSCO Holdings
- MinRes Wodgina / Mt Marion
- spodumene offtake
- lithium price cycle
- downstream margin

철강 / 건자재:
- Hyundai Steel
- U.S. steel plant capex
- tariff hedge
- rebar / construction demand weakness
- Chinese import pressure

배터리 소재:
- L&F
- Tesla 4680 cathode contract
- contract value collapse
- customer-name false Green prevention

폴리실리콘:
- OCI Holdings
- non-China polysilicon
- U.S. solar cell capacity
- SpaceX unconfirmed media report

구리·방산:
- Poongsan
- copper processing
- ammunition optionality
- Hanwha acquisition rumor fade
```

---

# 4. 국장 신규 후보 case

## Case A — 고려아연 `success_candidate + governance/dilution 4B·4C-watch`

```text
symbol = 010130
case_type = success_candidate + governance_watch
archetype = STRATEGIC_MINERALS_SUPPLY_CHAIN / CRITICAL_MINERALS_US_REFINERY
```

### stage date

```text
Stage 1:
2024~2025
- MBK / YoungPoong control battle
- antimony / zinc / critical-minerals supply-chain narrative

Stage 2:
2025-12~2026-03
- U.S. Tennessee critical-minerals refinery
- $7.4B project
- 540,000 metric tons non-ferrous metals
- 11 critical minerals including antimony, gallium, germanium
- rare-earth extraction from data-center waste talks
- 2025 operating profit 1.2T won, partly driven by antimony

Stage 3:
보류
- project FID, offtake, margin, FCF, dilution 통과 필요
- strategic mineral narrative만으로 Green 금지

Stage 4B:
U.S. strategic-mineral project / antimony price narrative로 가격이 먼저 확장되면 후보

Stage 4C-watch:
2025-12-16
- MBK / YoungPoong injunction
- Korea Zinc -13%

4C relief but governance watch remains:
2025-12-24
- court rejects injunction
- Korea Zinc up to +5%
- YoungPoong -10.5%
```

고려아연은 R4에서 가장 “진짜 구조 후보”와 “지배구조 RedTeam”이 동시에 붙는 케이스다. 회사는 미국 Tennessee에 74억 달러 규모 critical-minerals refinery를 추진하고 있고, 540,000톤 규모 비철금속과 11개 critical minerals를 생산하는 계획을 제시했다. Reuters는 고려아연이 미국 tech firms와 데이터센터 폐기물에서 rare earths를 추출하는 방안도 논의 중이며, 2025년 영업이익 1.2조 원이 antimony 판매 호조에 힘입었다고 보도했다. 그러나 19억 달러 share issue와 경영권 분쟁이 붙으면서 MBK·영풍 injunction 뉴스에 주가가 13% 하락했고, 법원 기각 후에는 고려아연이 최대 5% 오르는 대신 영풍이 최대 10.5% 하락했다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters critical-minerals / governance event anchors

stage3_price:
N/A

U.S._smelter_project_value:
$7.4B

planned_output:
540,000 metric tons non-ferrous metals

critical_minerals:
11 minerals including antimony, gallium, germanium

target_margin:
17~19%

planned_construction_start:
early 2027

planned_operation:
2030

2025_operating_profit:
1.2T won

share_issue_for_project:
$1.9B

share_issue_vs_project_value:
1.9 / 7.4
= 25.7%

new_investor_stake:
about 10%

injunction_event_MAE:
-13%

court_rejection_event_MFE:
+5%

YoungPoong_court_event_MAE:
-10.5%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + governance_watch
rerating_result = strategic_minerals_project_watch
stage_failure_type = stage2_evidence_not_green
```

---

## Case B — 롯데케미칼 / HD현대케미칼 `failed_rerating + restructuring relief`

```text
symbols = 011170 / HD Hyundai Chemical exposure
case_type = failed_rerating + restructuring_watch
archetype = PETROCHEMICAL_RESTRUCTURING_KOREA
```

### stage date

```text
Stage 1:
2024~2025
- China / Middle East oversupply
- petrochemical spread collapse
- NCC restructuring expectation

Stage 2:
2025-11-26
- restructuring plan submitted
- Korea aims to cut up to 3.7M tons annual NCC capacity
- industry asked to cut up to 25% of annual capacity

Stage 2 relief:
2026-02-24
- government approves first petrochemical restructuring deal
- Lotte Daesan NCC 1.1M tpy shut for 3 years
- HD Hyundai Chemical integrated entity
- 1.2T won capital increase
- support package >2T won

Stage 3:
없음
- 구조조정 승인만으로 Green 금지
- spread, OPM, FCF, debt/funding cost 확인 필요

Stage 4B:
구조조정 기대만으로 chemical basket이 급등하면 후보

Stage 4C:
oversupply 지속, spread reversal, inventory build, debt burden, capacity cut insufficient 시 후보
```

롯데케미칼·HD현대케미칼 구조조정은 “바닥 신호”일 수는 있지만, 아직 Stage 3는 아니다. 정부는 석유화학 공급과잉을 해결하기 위해 업체들에게 연간 생산능력 최대 25% 감축을 요구했고, 전체적으로 최대 370만 톤의 NCC capacity 감축을 목표로 했다. 이후 승인된 구조조정은 롯데 대산 NCC 110만 톤 설비를 3년간 중단하고, 1.2조 원 증자와 2조 원 이상 지원 package를 붙이는 방식이다. 이건 spread 회복 전까지 **restructuring relief**다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters restructuring evidence

stage3_price:
N/A

stock_OHLC:
price_data_unavailable_after_deep_search

Daesan_NCC_capacity_halted:
1.1M tpy

shutdown_duration:
3 years

government_support_package:
>2.0T won

capital_increase:
1.2T won

utility_cost_savings_estimate:
up to 115B won

R&D_funding:
26B won

equity_split_after_restructuring:
50:50

target_capacity_cut_national:
up to 3.7M tpy

industry_capacity_cut_goal:
up to 25%

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = failed_rerating_then_restructuring_watch
rerating_result = petrochemical_restructuring_relief
stage_failure_type = stage2_relief_not_green
```

---

## Case C — SK이노베이션 / S-Oil `cyclical_success / refining spread watch`

```text
symbols = 096770 / 010950
case_type = cyclical_success
archetype = REFINING_SPREAD_CYCLE
```

### stage date

```text
Stage 1:
2025~2026
- refining margin recovery
- supply disruption
- low oil price policy
- Middle East disruption

Stage 2:
2025-10-31
- SK Innovation Q3 OP 573B won vs prior-year loss 423B won
- estimate 304B won beat
- revenue +16.3%
- shares +0.2%, KOSPI +0.3%
- SK On loss widened to 124.8B won

Stage 2:
2026-01-28
- Q4 OP 295B won vs 176B won YoY
- but forecast 351B won miss
- SK On Q4 loss 441B won vs prior quarter 125B won
- shares +0.4%, KOSPI +1.3%

추가 Stage 2:
2026-05-13
- Q1 OP 2.2T won vs prior-year loss 30B won
- LSEG estimate 1.4T won beat

Stage 3:
없음
- 정유마진은 cycle
- multi-quarter margin floor, FCF, deleveraging, capital return, battery drag control 필요

Stage 4B:
geopolitical refining margin spike로 정유주가 먼저 rerating되면 후보

Stage 4C:
margin normalization, crude cost shock, battery loss 재확대, working capital drag 시 후보
```

SK이노베이션은 정유 스프레드가 실적을 살릴 수 있음을 보여줬지만, 동시에 왜 R4에서 정유를 구조적 Stage 3로 너무 빨리 올리면 안 되는지도 보여준다. Q3 2025에는 5,730억 원 영업이익으로 흑자전환했고, Q1 2026에는 2.2조 원 영업이익으로 추정치를 크게 넘겼다. 하지만 Q4 2025는 추정치를 밑돌았고, SK On 손실이 Q3 1,248억 원, Q4 4,410억 원으로 확대되며 battery drag가 계속 붙었다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters refining-cycle financial and price anchors

stage3_price:
N/A

Q3_2025_OP:
573B won

Q3_2024_OP:
-423B won

Q3_profit_swing:
573 - (-423)
= +996B won

Q3_estimate:
304B won

Q3_beat_vs_estimate:
573 / 304 - 1
= +88.5%

Q3_revenue_growth:
+16.3%

Q3_event_return:
+0.2%

KOSPI_Q3_context:
+0.3%

Q4_2025_OP:
295B won

Q4_2024_OP:
176B won

Q4_OP_growth:
295 / 176 - 1
= +67.6%

Q4_forecast:
351B won

Q4_miss_vs_forecast:
295 / 351 - 1
= -16.0%

Q4_event_return:
+0.4%

KOSPI_Q4_context:
+1.3%

Q4_relative_underperformance:
0.4 - 1.3
= -0.9pp

SK_On_Q4_loss:
441B won

SK_On_prior_quarter_loss:
125B won

SK_On_loss_worsening:
441 / 125 - 1
= +252.8%

Q1_2026_OP:
2.2T won

Q1_2025_comparable:
-30B won

Q1_profit_swing:
2.2T - (-0.03T)
= +2.23T won

LSEG_estimate:
1.4T won

Q1_beat_vs_estimate:
2.2 / 1.4 - 1
= +57.1%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = cyclical_success
rerating_result = refining_cycle_rebound_with_battery_drag
stage_failure_type = stage2_watch_success
```

---

## Case D — POSCO Holdings / MinRes lithium JV `success_candidate / resource-security watch`

```text
symbol = 005490
case_type = success_candidate + cyclical_watch
archetype = LITHIUM_RESOURCE_SECURITY / LITHIUM_CYCLE_OVERLAY
```

### stage date

```text
Stage 1:
2023~2025
- POSCO lithium raw-material internalization
- Australia hard-rock lithium exposure
- downstream lithium hydroxide strategy

Stage 2:
2025-11-11
- MinRes sells 30% stake in part of lithium business to POSCO for $765M
- POSCO obtains indirect 15% interests in Wodgina and Mt Marion
- POSCO receives spodumene concentrate in proportion to JV stake
- MinRes shares +10.8%

Stage 3:
없음
- resource security는 Stage 2
- lithium hydroxide margin, offtake economics, downstream FCF 확인 전 Green 금지

Stage 4B:
lithium price rebound로 POSCO / 소재주가 먼저 움직이면 후보

Stage 4C:
lithium price 재하락, project write-down, demand slowdown, downstream margin failure 시 후보
```

POSCO의 MinRes lithium JV는 R4에서 “좋은 Stage 2”의 예다. POSCO는 7.65억 달러를 내고 Wodgina·Mt Marion에 각각 간접 15% 지분을 얻으며, JV 지분에 비례해 spodumene concentrate를 받을 수 있다. 그러나 Reuters는 spodumene 가격이 2022년 톤당 6,000달러 이상에서 2025년 6월 약 610달러까지 빠진 뒤 880달러로 반등했지만 여전히 고점 대비 크게 낮다고 설명했다. 즉 resource security는 좋지만, lithium cycle과 downstream margin을 통과해야 한다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters lithium transaction / commodity anchors

stage3_price:
N/A

POSCO_stock_OHLC:
price_data_unavailable_after_deep_search

transaction_value:
$765M

POSCO_indirect_stake:
15% in Wodgina and Mt Marion each

MinRes_event_MFE:
+10.8%

spodumene_peak_2022:
> $6,000/t

spodumene_low_2025_June:
about $610/t

spodumene_drawdown_peak_to_low:
1 - 610 / 6000
= -89.8% 이상

spodumene_rebound_610_to_880:
880 / 610 - 1
= +44.3%

spodumene_880_vs_6000_peak:
880 / 6000 - 1
= -85.3% 이상

MFE / MAE:
POSCO stock OHLC unavailable
```

### alignment

```text
score_price_alignment = success_candidate / cyclical_watch
rerating_result = resource_security_watch
stage_failure_type = stage2_watch_success
```

---

## Case E — 현대제철 `failed_rerating + steel demand 4C-watch`

```text
symbol = 004020
case_type = failed_rerating / 4C-watch
archetype = STEEL_POLICY_CAPEX_TARIFF_HEDGE / BUILDING_MATERIALS_DEMAND_CYCLE
```

### stage date

```text
Stage 1:
2024~2025
- U.S. tariff pressure
- steel localization / U.S. plant narrative
- weak domestic construction demand

Stage 2:
2025-03-25
- Hyundai Steel announces $5.8B Louisiana plant
- annual capacity 2.7M tonnes
- initial shares +5% then reversed to -4.4%

Stage 4C-watch:
2025-04-22
- investors criticized funding uncertainty
- shares lost 21.2% after announcement
- POSCO Holdings -18.3%, benchmark -5.5%
- weak domestic demand / cheap Chinese imports / labor disputes

추가 4C-watch:
2024-06-21
- Nomura cuts 2024 net profit forecast by 73% to 215B won
- rebar price expected -10%
- shares -1.2% to 29,000 won
```

현대제철은 R4의 대표적 false-positive 방지 케이스다. 미국 공장 CAPEX는 tariff hedge처럼 보였고, 발표 직후 주가는 5% 넘게 올랐지만 같은 세션에서 -4.4%로 뒤집혔다. 이후 funding detail 부족과 투자 실효성 우려로 주가는 발표 후 21.2% 하락했다. 더 근본적으로 2024년에는 건설·조선 수요 약화로 순이익 추정치가 73% 낮아졌고, 철근 가격은 10% 하락 가능성이 제기됐다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / MarketWatch capex and weak-demand anchors

stage3_price:
N/A

U.S._plant_investment:
$5.8B~$6.0B

U.S._plant_capacity:
2.7M tonnes/year

announcement_session_initial_MFE:
> +5%

announcement_session_MAE:
-4.4%

post_announcement_drawdown:
-21.2%

POSCO_Holdings_same_period:
-18.3%

benchmark_same_period:
-5.5%

relative_underperformance_vs_benchmark:
-21.2 - (-5.5)
= -15.7pp

funding_plan:
50% borrowing, rest unclear / possible POSCO equity

2024_net_profit_forecast:
215B won

net_profit_forecast_cut:
-73%

implied_prior_net_profit_forecast:
215B / (1 - 0.73)
= 796.3B won

rebar_price_expected_decline:
-10%

weak_demand_event_price:
29,000 won

weak_demand_event_MAE:
-1.2%

MFE / MAE_30D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = false_positive_score_prevention
rerating_result = policy_capex_without_funding_failed
stage_failure_type = 4C_watch
```

---

## Case F — L&F `hard 4C / battery-material contract quality break`

```text
symbol = 066970
case_type = 4C-thesis-break
archetype = BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK
```

### stage date

```text
Stage 1:
2023
- Tesla 4680 high-nickel cathode material supply deal
- customer-name / EV-material growth narrative

Stage 2:
없음 또는 약함
- 고객명과 계약금액 headline만으로 Green 금지

Stage 3:
없음

Stage 4C:
2025-12-29
- Tesla cathode supply deal value $2.9B → $7,386
- 4680 production yield issue / EV demand slowdown
- Cybertruck demand disappointment
```

L&F는 R4 소재에서도 중요한 hard 4C 기준점이다. 2023년 Tesla향 high-nickel cathode 공급계약은 고객명과 29억 달러 규모 때문에 Stage 3처럼 보일 수 있었지만, 2025년 말 계약가치는 7,386달러로 사실상 사라졌다. Reuters는 Tesla 4680 ramp 문제, EV demand slowdown, Cybertruck 부진 등이 원인으로 지목됐다고 보도했다. 고객명과 계약금액 headline만으로 Green을 주면 안 된다는 가장 좋은 반례다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters contract-value collapse anchor

stage3_price:
N/A

initial_contract_value:
$2.9B

revised_contract_value:
$7,386

contract_value_drawdown:
1 - 7,386 / 2,900,000,000
= 99.999745% collapse

contract_period:
2024~2025

product:
high-nickel cathode materials for Tesla 4680 cells

reason_context:
4680 yield issue
EV demand slowdown
Cybertruck demand disappointment

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = battery_material_contract_quality_failure
stage_failure_type = hard_4C
```

---

## Case G — OCI Holdings `success_candidate + unconfirmed media 4B-watch`

```text
symbol = 010060
case_type = success_candidate + event_premium
archetype = POLYSILICON_NON_CHINA_SUPPLY_OPTION
```

### stage date

```text
Stage 1:
2025-06-07
- U.S. solar-cell expansion
- non-China solar supply chain
- AI data center power demand

Stage 2:
2025-06-07
- Texas plant capacity expansion
- $1.2B investment
- target 10GW by 2027

Stage 3:
없음
- capex-heavy project
- confirmed customer contract, margin, FCF 확인 전 Green 금지

Stage 4B:
2026-04-14
- OCI TerraSus / SpaceX polysilicon supply talk media report
- SpaceX did not respond
- OCI spokesperson could not confirm

Stage 4C:
SpaceX deal not confirmed, subsidy rollback, polysilicon price decline, capex overrun 시 후보
```

OCI는 비중국 polysilicon / U.S. solar supply-chain 후보로 볼 수 있다. FT는 OCI가 Texas plant capacity를 2027년까지 10GW로 늘리기 위해 12억 달러를 투자한다고 보도했다. 하지만 Reuters가 전한 SpaceX supply talk는 아직 미확정 media report다. SpaceX는 답변하지 않았고, OCI 측도 보도를 확인할 수 없다고 밝혔다. R4에서는 **U.S. capacity expansion은 Stage 2, SpaceX 보도는 4B/event premium**으로 분리해야 한다. ([Financial Times][7])

### 실제 가격경로 검증

```text
price_data_source:
FT / Reuters capacity and media-report anchors

stage3_price:
N/A

stock_OHLC:
price_data_unavailable_after_deep_search

U.S._investment:
$1.2B

target_capacity:
10GW by 2027

capacity_equivalent:
roughly 10 nuclear power plants equivalent, per FT framing

SpaceX_contract_status:
unconfirmed media report

SpaceX_planned_satellite_constellation:
1M solar-powered satellites, according to filing cited by Reuters

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + event_premium
rerating_result = non_China_polysilicon_watch
stage_failure_type = stage2_evidence_not_green
```

---

## Case H — 풍산 `event_premium / M&A optionality fade`

```text
symbol = 103140
case_type = event_premium / price_moved_without_evidence
archetype = COPPER_PROCESSING_PLUS_DEFENSE / M_AND_A_OPTIONALITY_EVENT
```

### stage date

```text
Stage 1:
2026-04-03
- Hanwha Aerospace bid report for Poongsan ammunition business
- reported value about 1.5T won / $1.1B
- copper + defense optionality

Stage 2:
없음 또는 약한 Stage 2
- confirmed transaction 없음

Stage 3:
없음
- M&A optionality만으로 Green 금지
- confirmed transaction, financing, EPS accretion, integration plan 필요

Stage 4B:
M&A 기대만으로 가격이 급등하면 event premium

Stage 4C / event fade:
2026-04-09
- Hanwha Aerospace drops plan
- Poongsan says no plan to sell ammunition division
```

풍산은 구리 가공과 방산 탄약 optionality가 동시에 있는 기업이라 R4/R1 경계에 걸친 후보가 될 수 있다. 하지만 Hanwha Aerospace의 1.5조 원 인수설은 6일 만에 fade됐다. Reuters는 4월 3일 Hanwha가 풍산 방산사업 인수 제안을 했다는 보도를 전했고, 4월 9일에는 Hanwha가 검토를 중단했으며 풍산도 매각 계획이 없다고 공시했다고 보도했다. 따라서 이건 copper-defense Stage 3가 아니라 **M&A optionality event premium**이다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters M&A report / termination anchors

stage3_price:
N/A

stock_OHLC:
price_data_unavailable_after_deep_search

reported_deal_value:
1.5T won / about $1.1B

rumor_date:
2026-04-03

termination_date:
2026-04-09

rumor_duration:
6 calendar days

transaction_status:
not decided → dropped / no sale plan

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = copper_defense_M&A_optionality_fade
stage_failure_type = stage1_attention_only
```

---

# 5. 이번 R4 case별 요약표

| case                   | 분류                                   |                                                              실제 가격검증 | alignment              |
| ---------------------- | ------------------------------------ | -------------------------------------------------------------------: | ---------------------- |
| 고려아연                   | success_candidate + governance watch |             $7.4B U.S. smelter, OP 1.2T, injunction -13%, relief +5% | Stage 2 + governance   |
| 롯데케미칼 / HD현대케미칼        | failed_rerating + restructuring      | Daesan 1.1M tpy shutdown 3 years, support >2T, capital increase 1.2T | restructuring relief   |
| SK이노베이션 / S-Oil        | cyclical_success                     |                   Q1 OP 2.2T, estimate beat +57.1%, but battery drag | refining cycle         |
| POSCO lithium / MinRes | success_candidate                    |             $765M deal, MinRes +10.8%, spodumene still -85%+ vs peak | resource security      |
| 현대제철                   | failed_rerating / 4C-watch           |              U.S. capex 후 -21.2%, rebar price -10%, NP forecast -73% | policy capex failure   |
| L&F                    | hard 4C                              |                       Tesla cathode deal $2.9B → $7,386, -99.999745% | contract-quality break |
| OCI Holdings           | success_candidate + event            |              $1.2B Texas expansion, 10GW by 2027, SpaceX unconfirmed | Stage 2 + 4B           |
| 풍산                     | event premium                        |                       1.5T won acquisition rumor → dropped in 6 days | M&A rumor fade         |

---

# 6. score-price alignment 판정

```text
success_candidate:
- 고려아연 strategic minerals
- POSCO lithium resource security
- OCI non-China polysilicon

cyclical_success:
- SK Innovation / S-Oil refining spread

failed_rerating / restructuring relief:
- 롯데케미칼 / petrochemical restructuring
- 현대제철 U.S. capex / weak rebar demand

hard_4C:
- L&F battery-material contract collapse

event_premium:
- OCI SpaceX unconfirmed media report
- Poongsan M&A rumor
- Korea Zinc governance / share-sale event

thesis_break_watch:
- Korea Zinc governance / dilution
- Hyundai Steel policy capex / weak construction demand
- Lotte Chemical oversupply if spread does not recover

price_moved_without_evidence:
- Poongsan M&A rumor
- OCI SpaceX unconfirmed report
- commodity/lithium rebound rallies without margin evidence
```

---

# 7. 점수비중 교정

## 올릴 축

```text
actual_product_spread +5
fcf_after_working_capital +5
supply_discipline_confirmed +5
capacity_shutdown_confirmed +4
price_floor_or_offtake +5
cost_curve_advantage +4
strategic_customer_or_government_offtake +4
inventory_normalization +4
tariff_resilience +4
resource_security_with_downstream_margin +4
contract_quality +5
```

### 왜 올리나

고려아연은 antimony·critical minerals에서 진짜 전략자원 후보가 될 수 있고, POSCO의 MinRes deal도 resource security 관점에서 의미가 있다. 롯데케미칼 구조조정은 supply discipline의 초기 신호다. 하지만 모두 Stage 3로 가려면 **스프레드·offtake·마진·FCF**가 확인되어야 한다.

## 내릴 축

```text
commodity_price_up_only -5
strategic_material_headline_only -4
governance_premium_only -5
share_issue_dilution -5
restructuring_plan_without_margin -4
policy_capex_without_funding -5
M&A_rumor_without_transaction -5
unconfirmed_media_report -5
lithium_price_event -5
contract_headline_without_calloff -5
capex_heavy_project_pre_revenue -4
```

### 왜 내리나

현대제철은 tariff hedge CAPEX처럼 보였지만 funding·마진 clarity가 없자 실패했다. L&F는 Tesla 고객명과 29억 달러 계약 headline이 있어도 actual call-off가 무너지면 hard 4C가 된다. OCI와 풍산은 각각 SpaceX 보도와 Hanwha M&A 보도가 확정되지 않았거나 곧 fade됐다.

## Green gate 강화 조건

```text
R4 Stage 3-Green 필수:
1. product spread 개선이 실제 확인됨
2. cost curve advantage 있음
3. supply discipline 또는 capacity shutdown이 확인됨
4. inventory build가 아님
5. FCF 전환 또는 현금흐름 개선
6. price floor / offtake / long-term contract 존재
7. EPS revision이 1개 분기 이벤트가 아니라 중기 경로로 연결
8. capex 부담과 dilution risk 통과
9. 정책/관세/제재 stress를 통과
10. 가격경로가 evidence 이후 따라옴

금지:
commodity price spike
strategic mineral headline only
tender offer premium
governance battle
정책 지원 기대
미확정 media report
M&A rumor
구조조정 계획만 있음
리튬/폴리실리콘 가격 이벤트
고객명만 있는 소재계약
```

## 4B 조기감지 조건

```text
4B-watch:
원자재 가격 급등 후 관련주 동반 급등
구조조정 기대만으로 multiple 확장
공개매수 / 자사주 / governance battle로 주가 급등
리튬 / 폴리실리콘 supply discipline 뉴스로 소재주 동반 급등
정제마진 공급차질성 spike
미확정 고객 보도에 급등
M&A rumor에 급등
strategic-minerals headline이 offtake/FCF보다 먼저 가격화

4B-elevated:
실적보다 가격이 먼저 감
보고서가 commodity upside만 반복
신규 CAPEX 발표로 dilution / FCF 부담 커짐
계약보다 정책/루머가 주가를 끌고 감
```

## 4C hard gate 조건

```text
contract value collapse
contract cancellation
spread reversal
china_oversupply
middle_east_capacity_overhang
inventory_build
NCC 가동 중단
계약/매각/공개매수 이벤트 불발
regulator revision order
대규모 신주발행 / dilution
commodity price 재하락
project capex overrun
offtake 부재
FCF 악화
tariff shock causing export margin damage
policy capex funding failure
```

이번 R4 Loop 10에서 확정 hard 4C는 **L&F 계약가치 붕괴**다. 현대제철은 hard 4C보다는 강한 4C-watch / false-positive prevention이고, 고려아연은 구조 후보이지만 governance/dilution watch가 붙는다.

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

## docs/round/round_162.md 요약

```md
# R4 Loop 10. Materials / Spread / Strategic Resources Price Validation

이번 라운드는 R4 Loop 10 price-validation 라운드다.

핵심 결론:
- Korea Zinc is a strategic-minerals Stage 2 candidate, not Green. U.S. $7.4B smelter, 540,000 tons output, 11 critical minerals, 2025 OP 1.2T won are positive. But $1.9B share issue, governance battle, -13% injunction move and dilution risk block Stage 3.
- Lotte Chemical / HD Hyundai Chemical restructuring is relief, not Green. Daesan NCC 1.1M tpy shutdown for 3 years, 1.2T won capital increase, >2T won support package. Spread/OPM/FCF required.
- SK Innovation / S-Oil refining rebound is cyclical_success. Q1 2026 OP 2.2T won, estimate beat +57.1%, but refining is cycle and battery drag persists.
- POSCO / MinRes lithium JV is resource-security Stage 2. POSCO gains indirect 15% stakes in Wodgina and Mt Marion for $765M; MinRes +10.8%, but spodumene remains far below 2022 peak.
- Hyundai Steel is false-positive prevention. $5.8~6B U.S. steel plant narrative reversed; shares lost -21.2% after announcement, while weak rebar demand cut 2024 NP forecast by 73%.
- L&F is hard 4C contract-quality case. Tesla cathode deal value collapsed from $2.9B to $7,386.
- OCI Holdings is non-China polysilicon Stage 2, but SpaceX supply report is unconfirmed event premium. Texas $1.2B expansion to 10GW by 2027 is positive but capex-heavy.
- Poongsan is M&A optionality event premium. Hanwha acquisition report around 1.5T won faded in 6 days.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 162 R4 Loop 10 Materials Spread Strategic Resources Price Validation

## 반영 내용
- R4 Loop 10 price-validation 라운드를 추가했다.
- Strategic minerals, petrochemical restructuring, refining spread cycle, lithium resource security, steel policy capex, battery-material contract-quality break, non-China polysilicon, copper-defense M&A optionality를 비교했다.
- Reuters/FT/WSJ/MarketWatch reported anchors로 가능한 MFE/MAE 및 spread/contract/project metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- product spread, FCF after working capital, supply discipline, offtake, cost curve, contract quality 가중치 강화
- commodity price-only, strategic material headline-only, governance premium, share dilution, policy capex without funding, unconfirmed media report, M&A rumor 감점 강화
- L&F contract-value collapse hard 4C 추가
```

## case row 초안

```jsonl
{"case_id":"r4_loop10_korea_zinc_strategic_minerals_governance","symbol":"010130","company_name":"Korea Zinc","case_type":"success_candidate","primary_archetype":"STRATEGIC_MINERALS_SUPPLY_CHAIN","stage2_date":"2025-12/2026-03","stage4c_date":"2025-12-16","price_validation":{"price_data_source":"Reuters critical-minerals/governance anchors","stage3_price":null,"us_smelter_project_value_usd_bn":7.4,"planned_output_tons":540000,"critical_minerals_count":11,"target_margin_pct":"17-19","planned_construction_start":"early_2027","planned_operation_year":2030,"operating_profit_2025_krw_trn":1.2,"share_issue_usd_bn":1.9,"share_issue_vs_project_value_pct":25.7,"new_investor_stake_pct":10,"injunction_event_mae_pct":-13,"court_rejection_event_mfe_pct":5,"youngpoong_court_event_mae_pct":-10.5,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_governance_watch","rerating_result":"strategic_minerals_project_watch","notes":"Strategic minerals are Stage 2; dilution/governance/offtake/FCF must clear before Stage 3."}
{"case_id":"r4_loop10_lotte_hd_petrochemical_restructuring","symbol":"011170/HD_Hyundai_Chemical","company_name":"Lotte Chemical / HD Hyundai Chemical","case_type":"failed_rerating","primary_archetype":"PETROCHEMICAL_RESTRUCTURING_KOREA","stage2_date":"2025-11-26/2026-02-24","price_validation":{"price_data_source":"Reuters restructuring evidence","stage3_price":null,"daesan_ncc_capacity_mn_tpy":1.1,"shutdown_duration_years":3,"support_package_krw_trn":2.0,"capital_increase_krw_trn":1.2,"utility_cost_savings_krw_bn":115,"rnd_funding_krw_bn":26,"equity_split_after_restructuring":"50:50","target_capacity_cut_national_mn_tpy":3.7,"industry_capacity_cut_goal_pct":25,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"failed_rerating_then_restructuring_watch","rerating_result":"petrochemical_restructuring_relief","notes":"Capacity shutdown/support is Stage 2 relief; spread, OPM and FCF recovery required for Green."}
{"case_id":"r4_loop10_sk_innovation_soil_refining_cycle","symbol":"096770/010950","company_name":"SK Innovation / S-Oil","case_type":"cyclical_success","primary_archetype":"REFINING_SPREAD_CYCLE","stage2_date":"2025-10-31/2026-01-28/2026-05-13","price_validation":{"price_data_source":"Reuters refining-cycle financial and price anchors","stage3_price":null,"q3_2025_op_krw_bn":573,"q3_2024_op_krw_bn":-423,"q3_profit_swing_krw_bn":996,"q3_estimate_krw_bn":304,"q3_beat_vs_estimate_pct":88.5,"q3_revenue_growth_pct":16.3,"q3_event_return_pct":0.2,"kospi_q3_context_pct":0.3,"q4_2025_op_krw_bn":295,"q4_2024_op_krw_bn":176,"q4_op_growth_pct":67.6,"q4_forecast_krw_bn":351,"q4_miss_vs_forecast_pct":-16.0,"q4_event_return_pct":0.4,"kospi_q4_context_pct":1.3,"q4_relative_underperformance_pp":-0.9,"sk_on_q4_loss_krw_bn":441,"sk_on_loss_worsening_pct":252.8,"q1_2026_op_krw_trn":2.2,"q1_profit_swing_krw_trn":2.23,"q1_beat_vs_estimate_pct":57.1,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"cyclical_success","rerating_result":"refining_cycle_rebound_with_battery_drag","notes":"Refining rebound is cyclical; Stage 3 requires multi-quarter margin floor, FCF, deleveraging and battery-loss control."}
{"case_id":"r4_loop10_posco_minres_lithium_jv","symbol":"005490","company_name":"POSCO Holdings / MinRes lithium JV","case_type":"success_candidate","primary_archetype":"LITHIUM_RESOURCE_SECURITY","stage2_date":"2025-11-11","price_validation":{"price_data_source":"Reuters lithium transaction/commodity anchors","stage3_price":null,"transaction_value_usd_mn":765,"posco_indirect_stake_pct":15,"minres_event_mfe_pct":10.8,"spodumene_peak_2022_usd_per_t":6000,"spodumene_low_2025_usd_per_t":610,"spodumene_drawdown_peak_to_low_pct":-89.8,"spodumene_rebound_610_to_880_pct":44.3,"spodumene_880_vs_peak_pct":-85.3,"price_validation_status":"posco_stock_ohlc_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_cyclical_watch","rerating_result":"resource_security_watch","notes":"Lithium mine stake is Stage 2; Stage 3 requires offtake economics, downstream margin and FCF."}
{"case_id":"r4_loop10_hyundai_steel_policy_capex_rebar_4c","symbol":"004020","company_name":"Hyundai Steel","case_type":"failed_rerating","primary_archetype":"STEEL_POLICY_CAPEX_TARIFF_HEDGE","stage2_date":"2025-03-25","stage4c_date":"2025-04-22/2024-06-21","price_validation":{"price_data_source":"Reuters/MarketWatch capex and weak-demand anchors","stage3_price":null,"us_plant_investment_usd_bn":"5.8-6.0","us_plant_capacity_mn_tpy":2.7,"announcement_initial_mfe_pct":5,"announcement_session_mae_pct":-4.4,"post_announcement_drawdown_pct":-21.2,"posco_holdings_same_period_pct":-18.3,"benchmark_same_period_pct":-5.5,"relative_underperformance_vs_benchmark_pp":-15.7,"funding_plan":"50pct_borrowing_rest_unclear_possible_posco_equity","net_profit_forecast_2024_krw_bn":215,"net_profit_forecast_cut_pct":-73,"implied_prior_net_profit_forecast_krw_bn":796.3,"rebar_price_expected_decline_pct":-10,"weak_demand_event_price_krw":29000,"weak_demand_event_mae_pct":-1.2,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"false_positive_score_prevention","rerating_result":"policy_capex_without_funding_failed","notes":"Tariff-hedge capex and weak rebar demand block Green; funding/margin clarity required."}
{"case_id":"r4_loop10_lnf_tesla_cathode_contract_hard_4c","symbol":"066970","company_name":"L&F","case_type":"4c_thesis_break","primary_archetype":"BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK","stage4c_date":"2025-12-29","price_validation":{"price_data_source":"Reuters contract-value collapse anchor","stage3_price":null,"initial_contract_value_usd_bn":2.9,"revised_contract_value_usd":7386,"contract_value_drawdown_pct":-99.999745,"contract_period":"2024-2025","product":"high-nickel cathode materials for Tesla 4680 cells","reason_context":["4680_yield_issue","EV_demand_slowdown","Cybertruck_demand_disappointment"],"price_validation_status":"reported_contract_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"battery_material_contract_quality_failure","notes":"Customer name and contract headline cannot be Green without actual call-off and volume/margin conversion."}
{"case_id":"r4_loop10_oci_non_china_polysilicon_spacex_watch","symbol":"010060","company_name":"OCI Holdings","case_type":"success_candidate","primary_archetype":"POLYSILICON_NON_CHINA_SUPPLY_OPTION","stage2_date":"2025-06-07","stage4b_date":"2026-04-14","price_validation":{"price_data_source":"FT/Reuters capacity and media-report anchors","stage3_price":null,"us_investment_usd_bn":1.2,"target_capacity_gw":10,"target_year":2027,"spacex_contract_status":"unconfirmed_media_report","spacex_solar_satellite_constellation":1000000,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_event_premium","rerating_result":"non_China_polysilicon_watch","notes":"U.S. expansion is Stage 2; unconfirmed SpaceX report is event premium until contract terms/margin/FCF confirm."}
{"case_id":"r4_loop10_poongsan_hanwha_mna_rumor_fade","symbol":"103140","company_name":"Poongsan","case_type":"event_premium","primary_archetype":"COPPER_PROCESSING_PLUS_DEFENSE","stage1_date":"2026-04-03","stage4c_date":"2026-04-09","price_validation":{"price_data_source":"Reuters M&A report/termination anchors","stage3_price":null,"reported_deal_value_krw_trn":1.5,"reported_deal_value_usd_bn":1.1,"rumor_date":"2026-04-03","termination_date":"2026-04-09","rumor_duration_days":6,"transaction_status":"not_decided_to_dropped_no_sale_plan","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium","rerating_result":"copper_defense_M&A_optionality_fade","notes":"M&A rumor faded in six days; Stage 3 requires confirmed transaction or copper/ammunition margin/FCF."}
```

## shadow weight row 초안

```csv
archetype,product_spread,fcf_after_wc,supply_discipline,capacity_shutdown,offtake,contract_quality,cost_curve,tariff_resilience,resource_security,event_penalty,governance_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
STRATEGIC_MINERALS_SUPPLY_CHAIN,+3,+4,+3,+0,+5,+4,+4,+2,+5,-3,+5,+5,+4,Korea Zinc strategic minerals are Stage 2 but governance/dilution blocks Green.
PETROCHEMICAL_RESTRUCTURING_KOREA,+5,+5,+5,+5,+1,+2,+4,+0,+0,-3,+2,+3,+5,Lotte Daesan shutdown is restructuring relief, not Green before spread/FCF.
REFINING_SPREAD_CYCLE,+5,+4,+2,+0,+1,+2,+3,+0,+0,-3,+1,+4,+3,SK/S-Oil refining rebound is cyclical; battery drag and margin durability matter.
LITHIUM_RESOURCE_SECURITY,+2,+4,+2,+0,+5,+3,+4,+0,+5,-5,+1,+4,+4,POSCO lithium JV is resource-security Stage 2 but lithium cycle risk remains.
STEEL_POLICY_CAPEX_TARIFF_HEDGE,+4,+5,+3,+0,+2,+2,+3,+5,+0,-5,+2,+4,+5,Hyundai Steel policy capex without funding/margin clarity can fail.
BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK,+2,+5,+1,+0,+5,+5,+3,+0,+0,0,+1,+3,+5,L&F Tesla contract collapse is hard 4C.
POLYSILICON_NON_CHINA_SUPPLY_OPTION,+3,+4,+3,+0,+5,+3,+3,+2,+3,-5,+1,+5,+3,OCI U.S. expansion is Stage 2; unconfirmed SpaceX report is event premium.
COPPER_PROCESSING_PLUS_DEFENSE,+4,+4,+2,+0,+3,+3,+3,+1,+0,-5,+2,+5,+3,Poongsan M&A rumor faded; Green requires confirmed transaction or margin/FCF.
M_AND_A_OPTIONALITY_EVENT,+0,+0,+0,+0,+0,+0,+0,+0,+0,-5,+3,+5,+3,M&A rumor without signed transaction should not become Green.
```

---

# 이번 R4 Loop 10 결론

R4는 Stage 3를 아주 보수적으로 줘야 한다.

```text
1. 고려아연은 전략광물 후보지만,
   governance / dilution / offtake / FCF를 통과해야 Stage 3다.

2. 롯데케미칼 구조조정은 relief이지 Green이 아니다.
   spread·OPM·FCF 회복 전 Stage 3 금지다.

3. SK Innovation / S-Oil 정유 rebound는 cyclical_success다.
   multi-quarter margin floor와 FCF 전에는 구조적 Green이 아니다.

4. POSCO lithium JV는 resource-security Stage 2다.
   리튬 가격 cycle과 downstream margin을 통과해야 한다.

5. 현대제철은 policy capex false-positive 방지 사례다.
   tariff hedge처럼 보였지만 funding·마진 불확실성이 가격을 깨뜨렸다.

6. L&F는 R4 소재계약 hard 4C 기준점이다.
   Tesla 고객명과 계약금액 headline이 있어도 actual call-off가 무너지면 Green은 즉시 깨진다.

7. OCI는 non-China polysilicon 후보지만,
   SpaceX 보도는 미확정 media report라 4B/event premium이다.

8. Poongsan은 copper + defense optionality가 있어도,
   Hanwha M&A rumor가 6일 만에 fade됐으므로 Stage 3 금지다.
```

한 문장으로 압축하면:

> **R4에서 진짜 Stage 3는 “원자재·관세·전략자원 뉴스가 좋다”가 아니라, 제품 스프레드·offtake·cost curve·supply discipline·FCF가 실제로 잠겨서 이익 체급이 바뀌는 순간이다.**
> **이번 R4 Loop 10은 전략자원과 구조조정 Stage 2를 인정하되, governance/dilution·policy capex failure·contract collapse·미확정 media report·M&A rumor를 4B/4C로 분리하는 라운드다.**

[1]: https://www.reuters.com/world/asia-pacific/korea-zinc-talks-with-us-tech-firms-extract-rare-earths-data-centre-waste-2026-03-12/?utm_source=chatgpt.com "Korea Zinc in talks with US tech firms to extract rare earths from data centre waste"
[2]: https://www.reuters.com/world/asia-pacific/south-koreas-hd-hyundai-lotte-chemical-submit-plan-restructure-petrochemical-2025-11-26/?utm_source=chatgpt.com "South Korea's HD Hyundai, Lotte Chemical submit plan to restructure petrochemical businesses"
[3]: https://www.reuters.com/business/energy/sk-innovation-swings-quarterly-profit-expects-resilient-q4-refining-margins-2025-10-31/?utm_source=chatgpt.com "SK Innovation swings to quarterly profit, expects resilient Q4 refining margins"
[4]: https://www.reuters.com/business/energy/australias-minres-sell-30-lithium-jv-stake-posco-765-mln-2025-11-11/?utm_source=chatgpt.com "Australia's MinRes inks $765 million deal with POSCO for lithium JV stake, shares surge"
[5]: https://www.reuters.com/markets/commodities/hyundai-steel-build-plant-louisiana-with-annual-output-27-million-tonnes-2025-03-25/?utm_source=chatgpt.com "Hyundai Steel unveils US factory plan, shares skid"
[6]: https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/?utm_source=chatgpt.com "South Korea's L&F slashes value of battery material supply deal with Tesla"
[7]: https://www.ft.com/content/e618a7e3-6388-42f9-beb8-c32599f7239d?utm_source=chatgpt.com "Solar group OCI doubles down on US despite Donald Trump's war on clean energy"
[8]: https://www.reuters.com/world/asia-pacific/hanwha-seeks-buy-poongsans-ammunition-business-about-11-billion-newspaper-says-2026-04-03/?utm_source=chatgpt.com "Hanwha seeks to buy Poongsan's ammunition business for about $1.1 billion, newspaper says"
