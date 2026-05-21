순서상 이번은 **R3 Loop 9 — 2차전지·전기차·친환경 가격경로 검증 라운드**다.

이번 R3 Loop 9는 이전 R3처럼 LGES·L&F hard 4C만 반복하지 않고, **ESS 전환, 전고체/차세대 배터리, SK On 구조조정, 태양광/Qcells, 리튬 이벤트, 공급망 하락, 수소/친환경 CAPEX**까지 섞어서 본다.

```text
round = R3 Loop 9
round_id = round_148
large_sector = BATTERY_EV_GREEN
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
```

원시 수정주가 일봉 OHLC는 이번 환경에서 안정적으로 직접 확보하지 못했다. 대신 Reuters / WSJ / MarketWatch / AP가 제공한 **가격 anchor, 이벤트 수익률, 계약금액, 손실·투자·원자재 지표**로 계산 가능한 값만 계산했다.

---

# 1. 이번 라운드 대섹터

```text
R3 = 2차전지·전기차·친환경
```

R3의 핵심은 “배터리·ESS·친환경 수혜”가 아니라, **계약이 실제 GWh/call-off/가동률/OPM/FCF로 내려오는가**다. 특히 2025~2026년 R3는 EV 수요 둔화와 ESS 전환이 동시에 나타난다. 그래서 Stage 3-Green은 매우 늦게 줘야 한다.

---

# 2. 대상 canonical archetype

```text
ESS_LFP_GRID_STORAGE
EV_TO_ESS_CAPACITY_REDEPLOYMENT
SOLID_STATE_BATTERY_TIMELINE
BATTERY_CONTRACT_CANCELLATION_4C
BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE
EV_BATTERY_JV_RESTRUCTURING
SEPARATOR_EV_DEMAND_CYCLE
BATTERY_MATERIALS_CAPEX_OVERHEAT
LITHIUM_CYCLE_OVERLAY
SOLAR_US_SUPPLY_CHAIN_LOCALIZATION
SOLAR_CUSTOMS_UFLPA_4C_WATCH
HYDROGEN_FUEL_CELL_CAPEX
PRICE_ONLY_RALLY
EVENT_PREMIUM
THESIS_BREAK_4C
```

---

# 3. deep sub-archetype

```text
ESS 전환:
- Samsung SDI LFP ESS
- LGES LFP ESS
- EV line conversion to ESS
- data-center storage demand
- U.S. subsidy phase-out
- delivery starts 2027
- utilization / OPM / FCF before Green

EV battery stress:
- LGES Ford cancellation
- LGES Freudenberg cancellation
- SK On / Ford JV termination
- SK On Q3 loss
- EV demand slowdown
- subsidy loss
- fixed-cost cut / debt reduction

전고체 / 차세대:
- Samsung SDI all-solid-state battery
- mass production target 2027
- price premium vs current lithium-ion
- technology timeline vs revenue conversion

소재 / 분리막:
- L&F Tesla 4680 cathode contract collapse
- POSCO Future M lithium event
- SK IE Technology separator demand shock
- EcoPro Materials precursor / supply-chain shock
- lithium price rally vs inventory valuation

태양광 / 친환경:
- Hanwha Qcells U.S. supply chain
- UFLPA customs detentions
- tariffs on Southeast Asian solar imports
- furloughs / reduced hours
- domestic localization vs operational disruption

수소:
- Hyundai Motor hydrogen fuel-cell plant
- electrolyzer / commercial vehicle / marine use
- CAPEX before utilization
```

---

# 4. 국장 신규 후보 case

## Case A — 삼성SDI `success_candidate / ESS Stage 2 + 전고체 timeline watch`

```text
symbol = 006400
case_type = success_candidate + event_premium_watch
archetype = ESS_LFP_GRID_STORAGE / SOLID_STATE_BATTERY_TIMELINE
```

### stage date

```text
Stage 1:
2024-03-07
- 전고체 배터리 양산 timeline 제시
- 2027년 mass production 목표
- larger cylindrical 2025, LFP 2026 계획

Stage 2:
2025-12-10
- U.S. LFP ESS supply deal >2조 원
- deliveries from 2027 for three years
- 기존 EV line을 ESS line으로 전환
- 주가 장중 +6.1%

Stage 3:
없음
- 전고체 timeline과 ESS 계약만으로 Green 금지
- 2027년 이후 delivery, utilization, OPM, FCF 확인 필요

Stage 4B:
전고체/ESS 기대만으로 주가가 급등하면 4B-watch

Stage 4C-watch:
2025-03-05
- CEO says EV demand sluggish until H1 2026
- Q4 2024 operating loss 2,570억 원
```

2024년 3월 삼성SDI는 전고체 배터리를 2027년부터 양산하겠다고 제시했고, 주가는 장중 11% 올라 405,500원을 기록했다. 하지만 전고체는 timeline이지 매출이 아니다. 당시 기존 리튬이온 대비 전고체 초기 판매가격은 훨씬 높을 것으로 예상됐고, 대량생산 후에야 가격 하락 가능성이 언급됐다. ([월스트리트저널][1])

2025년 12월 삼성SDI 미국 법인은 2조 원 이상 규모의 LFP ESS 공급계약을 체결했다. 배송은 2027년부터 3년간 진행될 예정이고, 기존 생산라인을 전환해 ESS용 LFP 배터리를 생산한다. 발표 후 삼성SDI 주가는 장중 6.1% 상승했으나, 이건 Stage 2다. 2025년 3월 CEO가 EV 수요가 2026년 상반기까지 부진할 것이라고 말했고, 삼성SDI는 2024년 4분기 2,570억 원 영업손실을 냈기 때문이다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
WSJ / Reuters reported price and contract anchors

stage3_price:
N/A

solid_state_event_peak_price:
405,500원

solid_state_event_MFE_1D:
+11.0%

implied_pre_event_reference_price:
405,500 / 1.11
= 약 365,315원

solid_state_target_mass_production:
2027

Hanwha_Securities_target_price:
700,000원

target_upside_from_solid_state_event_peak:
(700,000 / 405,500) - 1
= +72.6%

ESS_contract_value:
>2.0T won / $1.36B

ESS_stage2_event_MFE_1D:
+6.1%

KOSPI_same_context:
-0.1%

relative_outperformance_vs_KOSPI:
6.1 - (-0.1)
= +6.2pp

delivery_start:
2027

contract_duration:
3 years

Q4_2024_operating_loss:
257B won

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

reason:
- Reuters/WSJ는 event-day anchor만 제공.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC는 이번 세션에서 안정적으로 직접 확보하지 못함.

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = ESS_stage2_watch + solid_state_timeline_watch
stage_failure_type = stage2_watch_success
```

### 교정

삼성SDI는 R3에서 `confirmed_ESS_contract`는 올려주되, `delivery_after_2027`, `EV_demand_sluggish`, `line_conversion_execution`, `OPM/FCF_unconfirmed`를 Green blocker로 둬야 한다.

---

## Case B — SK이노베이션 / SK On `failed_rerating + ESS restructuring relief`

```text
symbol = 096770
case_type = failed_rerating + restructuring_relief
archetype = EV_BATTERY_JV_RESTRUCTURING / EV_TO_ESS_CAPACITY_REDEPLOYMENT
```

### stage date

```text
Stage 1:
2021~2023
- SK On global EV battery growth
- Ford / Hyundai / U.S. battery plant expansion

Stage 2:
2024-08-27
- SK Innovation / SK E&S merger approved
- shares +5%
- restructuring relief

추가 Stage 2:
2025-12-11
- SK On / Ford U.S. battery JV termination
- Ford takes Kentucky plants, SK On takes Tennessee plant
- ESS expansion pivot

Stage 3:
없음
- SK On은 profitability, utilization, debt reduction, ESS revenue conversion 전 Green 금지

Stage 4C-watch:
2024-07~2025-12
- SK On never profitable since split-off
- cumulative losses / debt burden
- Q3 2025 operating loss 1,248억 원
- Ford JV termination
```

SK Innovation 주주들은 2024년 8월 SK E&S와의 합병을 승인했고, 주가는 장중 최대 5% 올랐다. 하지만 이건 SK On을 살리기 위한 restructuring relief다. SK On은 2021년 분사 이후 흑자를 낸 적이 없고, EV battery shipment 둔화로 어려움을 겪었다. ([Reuters][3])

2025년 12월 SK On은 Ford와의 미국 battery JV를 종료하기로 했다. 2022년 양사는 114억 달러를 투자해 미국 Kentucky와 Tennessee에 배터리 공장을 짓기로 했지만, EV 수요 둔화와 보조금 종료 속에서 Ford는 Kentucky plants를 가져가고 SK On은 Tennessee plant를 맡는 구조로 재편됐다. SK On은 Q3 2025에 1,248억 원 영업손실을 냈고, 이는 전 분기 664억 원 손실의 거의 두 배였다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported transaction / event anchors

stage3_price:
N/A

merger_approval_event_MFE_1D:
+5.0%

KOSPI_same_context:
-0.5%

relative_outperformance:
5.0 - (-0.5)
= +5.5pp

merged_entity_assets:
100T won

SK_E&S_2023_operating_profit:
1.3T won

SK_E&S_2023_sales:
11.2T won

SK_E&S_OP_margin:
1.3 / 11.2
= 11.6%

SK_Innovation_2023_operating_profit:
1.9T won

SK_Innovation_2023_sales:
77.3T won

SK_Innovation_OP_margin:
1.9 / 77.3
= 2.46%

Ford_SK_On_JV_original_investment:
$11.4B

SK_On_Q3_2025_operating_loss:
124.8B won

previous_quarter_loss:
66.4B won

loss_worsening_QoQ:
124.8 / 66.4 - 1
= +88.0%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

reason:
- Reuters는 event-day return은 제공하지만 원시 OHLC를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = failed_rerating_then_restructuring_relief
rerating_result = EV_battery_growth_thesis_failed_then_ESS_reposition
stage_failure_type = should_have_been_red_or_watch
```

### 교정

SK On은 R3에서 `negative_FCF`, `loss_making_battery_unit`, `parent_support_dependency`, `JV_restructuring`을 강한 감점축으로 둬야 한다. ESS pivot은 Stage 2 가능성이 있지만, Green은 **흑자전환·가동률·부채감소·ESS 매출** 확인 뒤다.

---

## Case C — LG에너지솔루션 / L&F `contract-quality hard 4C anchor`

```text
symbols = 373220 / 066970
case_type = 4C-thesis-break
archetype = BATTERY_CONTRACT_CANCELLATION_4C / BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE
```

### stage date

```text
LGES Stage 4C:
2025-12-18
- Ford EV battery supply deal cancellation
- 주가 장중 -7.6%

LGES 추가 4C:
2025-12-26
- Freudenberg 3.9조 원 계약 종료
- Ford + Freudenberg 총 13.5조 원 기대매출 손실

L&F Stage 4C:
2025-12-29
- Tesla cathode material supply deal value $2.9B → $7,386
```

Ford는 LGES와의 9.6조 원 EV battery supply deal을 취소했고, LGES 주가는 다음 날 장중 최대 7.6% 하락했다. 이후 Freudenberg 계약 3.9조 원까지 종료되면서 LGES는 10일도 안 되는 기간에 약 13.5조 원의 기대매출을 잃었다. 이는 LGES 2024년 매출 25.62조 원의 절반을 넘는 규모다. ([Reuters][5])

L&F는 Tesla향 high-nickel cathode 공급계약 예상가치가 29억 달러에서 7,386달러로 줄었다고 밝혔다. Tesla 4680 ramp 부진과 EV 수요 둔화가 핵심 배경으로 설명됐다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event return and contract-value anchors

stage3_price:
N/A

LGES_Ford_cancellation_MAE_1D:
-7.6%

KOSPI_same_context:
-1.4%

LGES_relative_underperformance:
-7.6 - (-1.4)
= -6.2pp

Ford_cancelled_contract:
9.6T won / $6.5B

Freudenberg_cancelled_contract:
3.9T won / $2.7B

LGES_total_lost_expected_revenue:
13.5T won

LGES_2024_revenue:
25.62T won

lost_revenue_vs_2024_revenue:
13.5 / 25.62
= 52.7%

L&F_initial_contract_value:
$2.9B

L&F_revised_contract_value:
$7,386

L&F_contract_value_drawdown:
1 - 7,386 / 2,900,000,000
= 99.999745% collapse

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = contract_quality_failure
stage_failure_type = false_green_prevention_case
```

### 교정

R3에서 `고객명`, `계약금액 headline`, `계약 체결 공시`는 Stage 3 충분조건이 아니다.

```text
Stage 3 조건:
actual call-off
take-or-pay
GWh / tonnage delivery
customer ramp confirmation
OPM
FCF
```

---

## Case D — Hanwha Solutions / Qcells `solar localization success_candidate + supply-chain 4C-watch`

```text
symbol = 009830
case_type = success_candidate + 4C-watch
archetype = SOLAR_US_SUPPLY_CHAIN_LOCALIZATION / SOLAR_CUSTOMS_UFLPA_4C_WATCH
```

### stage date

```text
Stage 1:
2023~2025
- U.S. solar localization
- IRA / tariff protection
- Qcells Georgia supply-chain buildout

Stage 2:
2025-04-21
- U.S. finalizes tariffs on Southeast Asian solar imports
- Hanwha Qcells among petitioners
- localization policy support

추가 Stage 2:
2025~2026
- Qcells continues U.S. supply-chain investment

Stage 3:
없음
- tariff support와 local factory buildout만으로 Green 금지
- utilization, margin, component supply, FCF 확인 필요

Stage 4C-watch:
2025-11-08
- Qcells furloughs 1,000 workers at Georgia factories
- customs delays under forced-labor import law
- 300 contract workers cut
```

Qcells는 미국 내 전체 solar panel supply chain을 구축하기 위해 25억 달러를 투자하고 있으며, 미국 solar localization의 대표 수혜 후보로 볼 수 있다. 2025년 미국은 Southeast Asia solar imports에 대해 높은 tariff를 확정했고, Hanwha Qcells와 First Solar 등이 속한 미국 제조사 측이 이 조사를 제기했다. 이건 Stage 2 policy support다. ([Reuters][7])

하지만 2025년 11월 Qcells는 미국 Georgia 공장에서 약 1,000명을 furlough했다. 해외 부품 선적이 미국 forced-labor import law에 따라 지연됐고, 300명가량의 contract workers도 줄였다. Qcells는 생산 정상화를 예상한다고 밝혔지만, 이는 solar localization의 **supply-chain 4C-watch**다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP policy and operational anchors

stage3_price:
N/A

stock_OHLC:
price_data_unavailable_after_deep_search

reason:
- Reuters/AP는 Hanwha Solutions 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.

Qcells_US_supply_chain_investment:
$2.5B

furloughed_workers:
1,000

contract_workers_cut:
300

total_direct_workforce_affected_if_combined:
1,300

AP_reported_US_workers_context:
about 3,000 employees

furloughed_share_of_3,000:
1,000 / 3,000
= 33.3%

tariff_policy:
U.S. tariffs finalized on Southeast Asian solar goods

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate + thesis_break_watch
rerating_result = solar_localization_watch_with_supply_chain_risk
stage_failure_type = stage2_watch_success_with_4C_watch
```

### 교정

태양광 localization은 R3에서 좋은 Stage 2 후보지만, Stage 3는 **component flow, utilization, gross margin, FCF, subsidy/tariff durability** 확인 뒤다. UFLPA/customs delay는 4C-watch다.

---

## Case E — POSCO Future M / L&F lithium event `cyclical_success / commodity event premium`

```text
symbols = 003670 / 066970
case_type = cyclical_success / event_premium
archetype = LITHIUM_CYCLE_OVERLAY / BATTERY_MATERIALS_CAPEX_OVERHEAT
```

### stage date

```text
Stage 1:
2025-08-11
- CATL Yichun lithium mine license expiry / production suspension
- lithium supply sentiment rebound

Stage 2:
없음 또는 약한 Stage 2
- commodity price event는 회사 단위 call-off / OPM / FCF evidence가 아님

Stage 3:
없음
- lithium price rally만으로 Green 금지

Stage 4B:
2025-08-11
- POSCO Future M +8.3%
- L&F +10%
- Samsung SDI +3.2%
- LGES +2.8%

Stage 4C:
CATL license renewal, lithium price 재하락, inventory valuation reversal 시 후보
```

CATL이 중국 Yichun lithium mine project를 중단하자 lithium supply 축소 기대가 커졌고, 한국 battery-material suppliers인 POSCO Future M은 8.3%, L&F는 10% 상승했다. 하지만 WSJ는 lithium prices가 2022년 peak 이후 최대 90% 하락했고, CATL이 license가 갱신되면 생산을 재개할 수 있다고 설명했다. 이건 구조적 Stage 3가 아니라 **commodity event premium**이다. ([월스트리트저널][9])

### 실제 가격경로 검증

```text
price_data_source:
WSJ reported event return and commodity context

stage3_price:
N/A

POSCO_Future_M_event_MFE_1D:
+8.3%

L&F_event_MFE_1D:
+10.0%

Samsung_SDI_event_MFE_1D:
+3.2%

LGES_event_MFE_1D:
+2.8%

KOSPI_same_context:
-0.1%

POSCO_Future_M_relative_outperformance:
8.3 - (-0.1)
= +8.4pp

L&F_relative_outperformance:
10.0 - (-0.1)
= +10.1pp

lithium_price_decline_from_2022_peak:
up to -90%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = cyclical_success / event_premium
rerating_result = lithium_price_event_watch
stage_failure_type = should_not_be_green
```

### 교정

R3 소재주는 `lithium_price_event`를 Stage 3로 올리면 안 된다. Stage 3는 **actual call-off, OPM, FCF, inventory quality** 확인 뒤다.

---

## Case F — SK IE Technology / EcoPro Materials `EV supply-chain shock / 4C-watch`

```text
symbols = 361610 / 450080
case_type = 4C-watch / overheat
archetype = SEPARATOR_EV_DEMAND_CYCLE / PRECURSOR_SUPPLY_CHAIN_SHOCK
```

### stage date

```text
Stage 1:
2023~2024
- EV separator / precursor vertical integration theme
- SK On / Ford / Korean battery supply-chain exposure

Stage 2:
없음 또는 약함
- customer shipment / utilization / OPM 확인 전 Green 금지

Stage 3:
없음

Stage 4B:
EV 소재·분리막 theme overheat 구간 후보

Stage 4C-watch:
2025-12-16
- Ford shifts away from EVs to hybrids
- SK Innovation -3%
- LGES -6%
- SK IE Technology -5%
- EcoPro Materials -5%
```

Ford가 약 200억 달러 charge를 인식하고 EV에서 hybrid 중심으로 전략을 바꾸자, 한국 battery supply chain은 동반 하락했다. MarketWatch는 SK Innovation -3%, LGES -6%, SK IE Technology -5%, EcoPro Materials -5%를 보도했다. Citi는 F-150 Lightning 중단과 lower-battery-content hybrid 전환이 한국 배터리 공급망에 부정적이라고 봤다. ([마켓워치][10])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch reported event return anchors

stage3_price:
N/A

SK_Innovation_event_MAE:
-3.0%

LGES_event_MAE:
-6.0%

SK_IE_Technology_event_MAE:
-5.0%

EcoPro_Materials_event_MAE:
-5.0%

Ford_charge:
about $20B

QuantumScape_premarket_MAE:
-2.0%

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = thesis_break_watch / price_moved_without_evidence
rerating_result = EV_supply_chain_demand_shock
stage_failure_type = should_have_been_red_or_watch
```

### 교정

SKIET/EcoPro Materials는 R3에서 `essential_material`, `separator/precursor_story`, `vertical_integration`만으로 Green 금지다. 고객 EV 전략 후퇴에 민감하기 때문에 `customer_strategy_risk`와 `utilization`을 강하게 봐야 한다.

---

## Case G — 현대차 수소연료전지 plant `success_candidate / hydrogen capex Stage 2`

```text
symbol = 005380
case_type = success_candidate
archetype = HYDROGEN_FUEL_CELL_CAPEX / GREEN_MOBILITY_INFRASTRUCTURE
```

### stage date

```text
Stage 1:
2025-10-30
- Hyundai hydrogen fuel-cell plant groundbreaking
- mobility / commercial vehicle / marine / electrolyzer use case

Stage 2:
2025-10-30
- 9,300억 원 Ulsan hydrogen fuel-cell facility
- completion expected 2027
- 43,000 square metres
- former internal combustion transmission site repurposed

Stage 3:
없음
- plant construction만으로 Green 금지
- utilization, order book, margin, fuel-cell vehicle/electrolyzer demand, FCF 확인 필요

Stage 4B:
hydrogen theme으로 가격이 먼저 급등하면 후보

Stage 4C:
hydrogen demand delay, utilization failure, subsidy cut, infrastructure buildout delay 시 후보
```

현대차는 2025년 10월 울산에 9,300억 원 규모 hydrogen fuel cell 생산시설 착공을 발표했다. 이 시설은 승용차, 상용 트럭·버스, 건설장비, 해양 선박, electrolyzer 용도까지 겨냥하며, 2027년 완공 예정이다. 다만 이는 R3 친환경 CAPEX Stage 2이지 Stage 3는 아니다. ([Reuters][11])

### 실제 가격경로 검증

```text
price_data_source:
Reuters capex / facility evidence

stage3_price:
N/A

stock_OHLC:
price_data_unavailable_after_deep_search
- Reuters는 현대차 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.

investment:
930B won / $654M

facility_area:
43,000 square metres

completion_target:
2027

target_applications:
passenger cars
commercial trucks and buses
construction equipment
marine vessels
electrolyzers

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = hydrogen_fuel_cell_capex_watch
stage_failure_type = stage2_watch_success
```

### 교정

수소는 R3에서 policy/CAPEX narrative가 강하지만, Stage 3는 **수요·가동률·마진·FCF**가 나와야 한다.

---

# 5. 이번 R3 case별 요약표

| case                         | 분류                           |                                                           실제 가격검증 | alignment          |
| ---------------------------- | ---------------------------- | ----------------------------------------------------------------: | ------------------ |
| 삼성SDI                        | success_candidate            |          전고체 event +11%, 405,500원; ESS deal +6.1%, Q4 loss 2,570억 | Stage 2 watch      |
| SK이노베이션/SK On                | failed_rerating / relief     |          merger approval +5%; Ford JV $11.4B 종료; Q3 loss +88% QoQ | failed_rerating    |
| LGES / L&F                   | hard 4C                      |    LGES -7.6%, lost revenue 13.5T; L&F contract value -99.999745% | thesis_break       |
| Hanwha Solutions/Qcells      | success_candidate + 4C-watch |     $2.5B U.S. supply chain; 1,000 furloughs, 300 contractors cut | supply-chain watch |
| POSCO Future M / L&F lithium | event premium                | POSCO Future M +8.3%, L&F +10%, lithium peak-to-trough up to -90% | cyclical_success   |
| SKIET / EcoPro Materials     | 4C-watch                     |                SKIET -5%, EcoPro Materials -5% on Ford EV retreat | thesis_break_watch |
| Hyundai hydrogen plant       | success_candidate            |                          930B won plant, 43,000㎡, 2027 completion | Stage 2 watch      |

---

# 6. score-price alignment 판정

```text
success_candidate:
- Samsung SDI ESS / solid-state timeline
- Hanwha Solutions / Qcells localization
- Hyundai hydrogen fuel-cell capex

failed_rerating:
- SK Innovation / SK On EV battery growth thesis

thesis_break / hard 4C:
- LGES contract cancellations
- L&F Tesla contract value collapse

cyclical_success / event_premium:
- POSCO Future M / L&F lithium event

thesis_break_watch:
- SKIET / EcoPro Materials EV supply-chain shock
- Qcells customs/UFLPA disruption

price_moved_without_evidence:
- lithium event rally if no company-level call-off / margin
- solid-state timeline rally if no revenue path
```

---

# 7. 점수비중 교정

## 올릴 축

```text
binding_contract_quality +5
actual_calloff +5
GWh_or_tonnage_volume +5
utilization_rate +5
OPM_visibility +5
FCF_after_capex +5
ESS_revenue_conversion +4
subsidy_quality_adjustment +4
customer_quality +4
supply_chain_localization_with_utilization +4
```

### 왜 올리나

Samsung SDI의 ESS 계약과 LGES의 ESS 전환은 R3에서 Stage 2 후보가 될 수 있다. 다만 delivery가 2027년 이후이고, EV line conversion이 실제 가동률·마진·FCF로 연결되는지 확인해야 한다. Qcells도 미국 local supply chain은 장기적으로 의미가 있지만, customs delay와 furlough가 보여주듯 공급망 실행이 Green gate다.

## 내릴 축

```text
ev_theme_only -5
ess_theme_only -4
solid_state_timeline_only -4
customer_name_only -5
contract_value_headline_without_calloff -5
capa_announcement -4
subsidy_dependent_profit -5
negative_fcf_or_debt_burden -5
jv_restructuring_relief -4
lithium_price_event -4
supply_chain_disruption -4
```

### 왜 내리나

L&F는 Tesla 고객명과 계약금액 headline이 있었지만, 계약가치가 사실상 0에 가깝게 줄었다. SK On은 EV 배터리 성장 스토리였지만 Ford JV를 재편했고, Q3 손실도 악화됐다. Lithium event는 POSCO Future M과 L&F를 밀었지만, 구조적 Stage 3가 아니라 commodity event premium이다.

## Green gate 강화 조건

```text
R3 Stage 3-Green 필수:
1. binding contract
2. actual call-off
3. GWh / tonnage volume
4. utilization improvement
5. OPM or gross margin improvement
6. FCF after capex
7. AMPC / subsidy 제외 이익 품질 확인
8. customer EV strategy risk 통과
9. supply-chain disruption risk 통과
10. price path follows evidence

금지:
고객명만 있음
계약금액 headline만 있음
ESS/LFP 테마만 있음
전고체 timeline만 있음
CAPA 전환만 있음
AMPC 제외 적자
EV 수요 둔화 무시
리튬 가격 이벤트만 있음
```

## 4B 조기감지 조건

```text
4B-watch:
전고체 timeline 발표 후 큰 급등
ESS/LFP 계약 발표만으로 주가 급등
리튬 가격 이벤트로 소재주 동반 급등
배터리 소재주가 call-off 없이 valuation만 확장
IPO/수직계열화 narrative로 주가가 먼저 감
보조금 포함 이익으로만 실적 서프라이즈

4B-elevated:
EV 수요 둔화에도 valuation 유지
고객 주문 확인 없이 CAPA 전환 기대만 반영
리튬 가격 반등이 재고평가 이익으로만 연결
supply-chain localization 기대가 customs/부품 지연을 무시
```

## 4C hard gate 조건

```text
contract cancellation
contract value collapse
customer EV model cancellation
customer strategy pullback
take-or-pay absence confirmed
GWh call-off failure
utilization delay
negative FCF
debt burden / emergency management
JV termination / restructuring under weak demand
subsidy-quality profit collapse
share issuance / dilution under weak demand
supply-chain customs detention
production furlough
```

이번 라운드에서 **LGES·L&F는 hard 4C**, **SK On·SKIET·EcoPro Materials·Qcells는 4C-watch**, **Samsung SDI·Hyundai hydrogen·Qcells localization은 Stage 2 watch**로 둔다.

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

## docs/round/round_148.md 요약

```md
# R3 Loop 9. Battery / EV / Green Price Validation

이번 라운드는 R3 Loop 9 price-validation 라운드다.

핵심 결론:
- Samsung SDI는 전고체 timeline event에서 +11%, ESS LFP contract에서 +6.1% 반응했다. 그러나 전고체와 ESS 모두 2027년 이후 delivery/utilization/OPM/FCF 확인 전 Stage 3는 아니다.
- SK Innovation/SK On은 EV battery growth thesis가 failed rerating으로 바뀐 케이스다. SK E&S merger approval은 +5% restructuring relief였고, Ford JV termination은 EV demand stress를 확인한다.
- LGES와 L&F는 contract-quality hard 4C 기준점이다. LGES는 Ford/Freudenberg 계약 종료로 기대매출 13.5T won을 잃었고, L&F Tesla 계약가치는 $2.9B에서 $7,386로 사실상 붕괴했다.
- Hanwha Solutions/Qcells는 U.S. solar localization Stage 2 후보지만, customs/UFLPA delay로 1,000 workers furloughed, 300 contractors cut이 발생해 supply-chain 4C-watch다.
- POSCO Future M/L&F lithium rally는 CATL mine suspension에 따른 event premium이다. POSCO Future M +8.3%, L&F +10%였지만 lithium price는 2022 peak 대비 최대 -90%였다.
- SKIET/EcoPro Materials는 Ford EV retreat에 -5%씩 하락했다. Separator/precursor story만으로 Green 금지다.
- Hyundai hydrogen fuel-cell plant는 930B won CAPEX Stage 2 후보지만 utilization/margin/FCF 전 Green 금지다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 148 R3 Loop 9 Battery EV Green Price Validation

## 반영 내용
- R3 Loop 9 price-validation 라운드를 추가했다.
- ESS LFP, solid-state timeline, SK On restructuring, contract-quality hard 4C, solar localization supply-chain risk, lithium event premium, separator/precursor demand shock, hydrogen fuel-cell capex를 비교했다.
- Reuters/WSJ/MarketWatch/AP reported anchors로 가능한 MFE/MAE 및 contract/financial/operational metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- binding contract quality, actual call-off, GWh volume, utilization, OPM/FCF 가중치 강화
- ESS theme-only, solid-state timeline-only, customer-name-only, lithium event, subsidy-dependent profit 감점 강화
- contract cancellation / contract value collapse hard 4C 강화
- supply-chain disruption and JV restructuring 4C-watch 추가
```

## case row 초안

```jsonl
{"case_id":"r3_loop9_samsung_sdi_ess_solid_state_watch","symbol":"006400","company_name":"삼성SDI","case_type":"success_candidate","primary_archetype":"ESS_LFP_GRID_STORAGE","stage1_date":"2024-03-07","stage2_date":"2025-12-10","price_validation":{"price_data_source":"WSJ/Reuters reported anchors","stage3_price":null,"solid_state_event_peak_price":405500,"solid_state_event_mfe_1d_pct":11.0,"implied_pre_event_reference_price":365315,"solid_state_mass_production_target_year":2027,"hanwha_target_price":700000,"target_upside_from_event_peak_pct":72.6,"ess_contract_value_krw_trn":2.0,"ess_contract_value_usd_bn":1.36,"ess_stage2_event_mfe_1d_pct":6.1,"kospi_same_context_pct":-0.1,"relative_outperformance_pp":6.2,"delivery_start_year":2027,"contract_duration_years":3,"q4_2024_operating_loss_krw_bn":257,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"ESS_stage2_watch_solid_state_timeline_watch","notes":"ESS and solid-state are Stage 2/timeline evidence; utilization, OPM and FCF required for Green."}
{"case_id":"r3_loop9_sk_innovation_skon_restructuring_relief","symbol":"096770","company_name":"SK이노베이션/SK On","case_type":"failed_rerating","primary_archetype":"EV_BATTERY_JV_RESTRUCTURING","stage2_date":"2024-08-27","stage4c_date":"2025-12-11","price_validation":{"price_data_source":"Reuters reported transaction/event anchors","stage3_price":null,"merger_approval_event_mfe_1d_pct":5.0,"kospi_same_context_pct":-0.5,"relative_outperformance_pp":5.5,"merged_entity_assets_krw_trn":100,"sk_ens_2023_op_krw_trn":1.3,"sk_ens_2023_sales_krw_trn":11.2,"sk_ens_op_margin_pct":11.6,"sk_innovation_2023_op_krw_trn":1.9,"sk_innovation_2023_sales_krw_trn":77.3,"sk_innovation_op_margin_pct":2.46,"ford_sk_on_jv_original_investment_usd_bn":11.4,"sk_on_q3_2025_operating_loss_krw_bn":124.8,"previous_quarter_loss_krw_bn":66.4,"loss_worsening_qoq_pct":88.0,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"failed_rerating_then_restructuring_relief","rerating_result":"EV_battery_growth_thesis_failed_then_ESS_reposition","notes":"SK On remains a Watch/Red case until profitability, utilization and debt reduction are proven."}
{"case_id":"r3_loop9_lges_lnf_contract_quality_hard_4c","symbol":"373220/066970","company_name":"LG에너지솔루션/L&F","case_type":"4c_thesis_break","primary_archetype":"BATTERY_CONTRACT_CANCELLATION_4C","stage4c_date":"2025-12-18/2025-12-29","price_validation":{"price_data_source":"Reuters reported event and contract-value anchors","stage3_price":null,"lges_ford_cancellation_mae_1d_pct":-7.6,"kospi_same_context_pct":-1.4,"lges_relative_underperformance_pp":-6.2,"ford_cancelled_contract_krw_trn":9.6,"freudenberg_cancelled_contract_krw_trn":3.9,"lges_total_lost_expected_revenue_krw_trn":13.5,"lges_2024_revenue_krw_trn":25.62,"lost_revenue_vs_2024_revenue_pct":52.7,"lnf_initial_contract_value_usd_bn":2.9,"lnf_revised_contract_value_usd":7386,"lnf_contract_value_drawdown_pct":-99.999745,"price_validation_status":"reported_event_and_contract_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"contract_quality_failure","notes":"Customer name and contract headline cannot be Green without actual call-off/take-or-pay/delivery/margin."}
{"case_id":"r3_loop9_hanwha_solutions_qcells_solar_supply_chain_watch","symbol":"009830","company_name":"Hanwha Solutions / Qcells","case_type":"success_candidate","primary_archetype":"SOLAR_US_SUPPLY_CHAIN_LOCALIZATION","stage2_date":"2025-04-21","stage4c_date":"2025-11-08","price_validation":{"price_data_source":"Reuters/AP policy and operational anchors","stage3_price":null,"qcells_us_supply_chain_investment_usd_bn":2.5,"furloughed_workers":1000,"contract_workers_cut":300,"total_direct_workforce_affected":1300,"reported_us_workers_context":3000,"furloughed_share_of_workers_pct":33.3,"tariff_policy":"U.S. finalized tariffs on Southeast Asian solar imports","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_thesis_break_watch","rerating_result":"solar_localization_watch_with_supply_chain_risk","notes":"Solar localization is Stage 2; customs/UFLPA delay and furloughs create 4C-watch until utilization and FCF confirm."}
{"case_id":"r3_loop9_posco_future_m_lnf_lithium_event","symbol":"003670/066970","company_name":"POSCO Future M / L&F","case_type":"event_premium","primary_archetype":"LITHIUM_CYCLE_OVERLAY","stage1_date":"2025-08-11","stage4b_date":"2025-08-11","price_validation":{"price_data_source":"WSJ reported event/commodity anchors","stage3_price":null,"posco_future_m_event_mfe_1d_pct":8.3,"lnf_event_mfe_1d_pct":10.0,"samsung_sdi_event_mfe_1d_pct":3.2,"lges_event_mfe_1d_pct":2.8,"kospi_same_context_pct":-0.1,"posco_future_m_relative_outperformance_pp":8.4,"lnf_relative_outperformance_pp":10.1,"lithium_price_decline_from_2022_peak_pct":-90,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"cyclical_success_event_premium","rerating_result":"lithium_price_event_watch","notes":"Lithium event is not Stage 3 without call-off, OPM, FCF and inventory quality."}
{"case_id":"r3_loop9_skiet_ecopro_materials_ford_supply_chain_shock","symbol":"361610/450080","company_name":"SK IE Technology / EcoPro Materials","case_type":"4c_watch","primary_archetype":"SEPARATOR_EV_DEMAND_CYCLE","stage4c_date":"2025-12-16","price_validation":{"price_data_source":"MarketWatch reported event returns","stage3_price":null,"sk_innovation_event_mae_pct":-3.0,"lges_event_mae_pct":-6.0,"sk_ie_technology_event_mae_pct":-5.0,"ecopro_materials_event_mae_pct":-5.0,"ford_charge_usd_bn":20,"quantumscape_premarket_mae_pct":-2.0,"price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"EV_supply_chain_demand_shock","notes":"Separator/precursor story requires utilization and customer demand; Ford EV retreat is 4C-watch."}
{"case_id":"r3_loop9_hyundai_hydrogen_fuel_cell_capex","symbol":"005380","company_name":"현대차 hydrogen fuel-cell plant","case_type":"success_candidate","primary_archetype":"HYDROGEN_FUEL_CELL_CAPEX","stage2_date":"2025-10-30","price_validation":{"price_data_source":"Reuters capex/facility evidence","stage3_price":null,"investment_krw_bn":930,"investment_usd_mn":654,"facility_area_sqm":43000,"completion_target_year":2027,"target_applications":["passenger cars","commercial trucks and buses","construction equipment","marine vessels","electrolyzers"],"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"hydrogen_fuel_cell_capex_watch","notes":"Hydrogen capex is Stage 2; utilization, orders, margin and FCF required before Green."}
```

## shadow weight row 초안

```csv
archetype,binding_contract,actual_calloff,gwh_volume,utilization,opm_fcf,subsidy_quality,supply_chain_execution,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
ESS_LFP_GRID_STORAGE,+4,+5,+5,+5,+5,+4,+4,-2,+4,+4,Samsung SDI ESS deal is Stage 2; delivery/utilization/OPM/FCF required.
SOLID_STATE_BATTERY_TIMELINE,+2,+2,+2,+3,+4,+1,+2,-4,+5,+3,Solid-state timeline rally is not Stage 3 before production/revenue.
EV_BATTERY_JV_RESTRUCTURING,+2,+3,+3,+5,+5,+4,+4,-3,+4,+5,SK On restructuring relief is not Green until profitability and debt reduction.
BATTERY_CONTRACT_CANCELLATION_4C,+5,+5,+5,+4,+5,+3,+3,0,+3,+5,LGES/L&F show contract cancellation/value collapse hard 4C.
SOLAR_US_SUPPLY_CHAIN_LOCALIZATION,+3,+3,+3,+5,+5,+5,+5,-2,+4,+4,Qcells localization is Stage 2 but customs/furlough risk is 4C-watch.
LITHIUM_CYCLE_OVERLAY,+1,+1,+1,+2,+3,+0,+2,-5,+5,+4,Lithium price rally is event premium unless OPM/FCF and call-off confirm.
SEPARATOR_EV_DEMAND_CYCLE,+3,+4,+3,+5,+5,+3,+3,-4,+4,+5,SKIET/EcoPro shock shows EV demand and customer strategy risk.
HYDROGEN_FUEL_CELL_CAPEX,+2,+2,+2,+5,+5,+3,+3,-4,+4,+4,Hydrogen plant capex is Stage 2 until utilization/order/margin/FCF confirm.
```

---

# 이번 R3 Loop 9 결론

R3는 여전히 **Green 발굴보다 false Green 차단이 더 중요한 섹터**다.

```text
1. Samsung SDI는 ESS와 전고체 모두 Stage 2 후보지만,
   2027년 delivery·양산·가동률·OPM/FCF 전 Stage 3가 아니다.

2. SK On은 EV battery growth thesis가 restructuring relief로 바뀐 케이스다.
   Ford JV termination과 Q3 loss 악화는 강한 RedTeam이다.

3. LGES와 L&F는 contract-quality hard 4C 기준점이다.
   계약 취소와 계약가치 붕괴는 고객명·계약금액 headline을 완전히 무너뜨린다.

4. Qcells는 U.S. solar localization 후보지만,
   customs delay와 1,000명 furlough는 supply-chain 4C-watch다.

5. POSCO Future M/L&F lithium rally는 commodity event premium이다.
   리튬 가격 반등만으로 Stage 3 금지다.

6. SKIET/EcoPro Materials는 Ford EV retreat에 바로 흔들렸다.
   separator/precursor story는 customer demand와 utilization 전 Green이 아니다.

7. Hyundai hydrogen fuel-cell plant는 친환경 CAPEX Stage 2지만,
   수요·가동률·마진·FCF 전 Stage 3는 아니다.
```

한 문장으로 압축하면:

> **R3에서 진짜 Stage 3는 “배터리·ESS·친환경 수혜”가 아니라, 계약이 actual call-off·GWh·가동률·OPM·FCF로 내려오고 고객 EV 전략과 보조금 리스크를 통과하는 순간이다.**
> **현재 R3는 ESS 전환과 친환경 CAPEX는 Stage 2로 인정하되, contract-quality 4C와 EV demand shock을 가장 강하게 봐야 한다.**

[1]: https://www.wsj.com/articles/samsung-sdi-rallies-as-it-sets-timeline-for-new-battery-production-ec7838dc?utm_source=chatgpt.com "Samsung SDI Rallies as It Sets Timeline for New Battery Production"
[2]: https://www.reuters.com/world/asia-pacific/samsung-sdis-us-unit-signs-14-bln-lfp-battery-deal-us-customer-2025-12-09/?utm_source=chatgpt.com "Samsung SDI unit signs US battery deal worth over $1.36 bln for energy storage systems"
[3]: https://www.reuters.com/markets/deals/sk-innovation-shareholders-approve-merger-plan-with-sk-es-yonhap-reports-2024-08-27/?utm_source=chatgpt.com "SK Innovation shareholders approve merger seen shoring up loss-making battery unit"
[4]: https://www.reuters.com/business/autos-transportation/south-koreas-sk-ford-motor-end-us-battery-joint-venture-2025-12-11/?utm_source=chatgpt.com "South Korea's SK On, Ford Motor to end US battery joint venture"
[5]: https://www.reuters.com/business/energy/shares-south-koreas-lges-drop-more-than-7-after-ford-cancels-ev-battery-deal-2025-12-18/?utm_source=chatgpt.com "Shares in South Korea's LGES drop more than 7% after Ford cancels EV battery deal"
[6]: https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/?utm_source=chatgpt.com "South Korea's L&F slashes value of battery material supply deal with Tesla"
[7]: https://www.reuters.com/sustainability/climate-energy/us-commerce-dept-finalizes-tariff-rates-solar-goods-southeast-asia-2025-04-21/?utm_source=chatgpt.com "US finalizes tariffs on Southeast Asian solar imports"
[8]: https://www.reuters.com/sustainability/climate-energy/qcells-furloughs-1000-workers-us-solar-factories-due-stalled-shipments-2025-11-08/?utm_source=chatgpt.com "Qcells furloughs 1,000 workers at US solar factories due to stalled shipments"
[9]: https://www.wsj.com/finance/commodities-futures/ev-battery-giant-catl-suspends-mining-project-67693725?utm_source=chatgpt.com "EV Battery Giant CATL Suspends Mining Project"
[10]: https://www.marketwatch.com/story/while-ford-shares-are-remarkably-steady-after-20-billion-charge-these-stocks-are-getting-battered-bbbcfa04?utm_source=chatgpt.com "While Ford shares are remarkably steady after $20 billion charge, these stocks are getting battered"
[11]: https://www.reuters.com/world/asia-pacific/hyundai-motor-breaks-ground-680-million-hydrogen-fuel-cell-plant-south-korea-2025-10-30/?utm_source=chatgpt.com "Hyundai Motor breaks ground on $680 million hydrogen fuel cell plant in South Korea"
