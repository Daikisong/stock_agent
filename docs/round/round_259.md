순서상 이번은 **R3 Loop 12 — 2차전지·전기차·친환경 가격경로 검증 라운드**다.

```text
round = R3 Loop 12
round_id = round_187
large_sector = BATTERY_EV_GREEN
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
```

이번 R3 Loop 12는 R3 Loop 11의 ESS 대표 case를 그대로 반복하지 않고, **EV JV 해체, EV plant idling, battery contract quality break, separator/precursor supply-chain shock, silicon-anode optionality, solar UFLPA supply-chain break, hydrogen fuel-cell capex, U.S. battery-factory visa/execution risk**를 중심으로 본다.

---

# 1. 이번 라운드 대섹터

```text
R3 = 2차전지·전기차·친환경
```

R3에서 진짜 Stage 3는 “ESS 전환”, “LFP”, “리튬”, “수소”, “태양광 현지화”가 아니라, **계약이 GWh·납기·가동률·OPM·FCF로 닫히고, EV 수요 후퇴·보조금 종료·관세·customs·노동/visa execution risk를 통과하는 순간**이다.

---

# 2. 대상 canonical archetype

```text
EV_BATTERY_CONTRACT_QUALITY_BREAK
EV_BATTERY_JV_RESTRUCTURING
EV_TO_ESS_CAPACITY_REDEPLOYMENT
US_BATTERY_LOCALIZATION_DILUTION
BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK
SILICON_ANODE_OPTIONALITY
SOLAR_US_SUPPLY_CHAIN_LOCALIZATION
SOLAR_CUSTOMS_UFLPA_4C_WATCH
HYDROGEN_FUELCELL_CAPEX_OPTIONALITY
US_FACTORY_EXECUTION_VISA_RISK
```

---

# 3. deep sub-archetype

```text
EV battery contract quality:
- LG Energy Solution / Ford / Freudenberg
- lost expected revenue
- customer EV strategy reversal
- call-off failure

EV battery JV restructuring:
- SK On / Ford JV dissolution
- Ultium GM-LGES Ohio plant restart uncertainty
- Samsung SDI / Stellantis StarPlus exit report
- Samsung SDI share-sale dilution

ESS pivot:
- SK On Flatiron LFP ESS
- Ultium Tennessee ESS conversion
- EV line redeployment

Battery supply-chain shock:
- POSCO Future M
- SK IE Technology
- EcoPro Materials
- SK Innovation / SK On
- cathode / separator / precursor demand shock

Alternative battery materials:
- SK / Group14 silicon-carbon anode
- Korea BAM factory control
- optionality vs actual offtake

Solar:
- Hanwha Qcells
- DOE loan guarantee
- UFLPA customs detention
- furlough / contract-worker cuts

Hydrogen:
- Hyundai Motor Ulsan hydrogen fuel-cell plant
- fuel cells / electrolyzers
- capex vs offtake / utilization

Factory execution:
- Hyundai-LG Georgia battery plant
- immigration raid / visa rules
- construction delay / restart
```

---

# 4. 국장 신규 후보 case

## Case A — Samsung SDI / StarPlus + share-sale `failed_rerating + dilution / JV 4C-watch`

```text
symbol = 006400
case_type = failed_rerating + 4C-watch
archetype = US_BATTERY_LOCALIZATION_DILUTION / EV_BATTERY_JV_RESTRUCTURING
```

### stage date

```text
Stage 1:
2024~2025
- U.S. battery localization
- GM / Stellantis JV capex
- IRA / tariff hedge expectation

Stage 2:
2025-03~04
- Samsung SDI plans 2T won share issuance
- proceeds for U.S. GM JV, Hungary capacity expansion, other battery investments
- share-sale price cut from 169,200 won to 146,200 won

Stage 4B / 4C-watch:
2025-04-09
- share-sale pricing cut by 14%
- Samsung SDI stock down 29.5% YTD
- stock down 1% that day vs KOSPI -0.5%

Stage 4C-watch:
2026-02-10
- Stellantis reportedly seeks to exit U.S. Samsung SDI battery JV
- Stellantis EV writedowns > $26.5B
- no final decision confirmed
```

Samsung SDI는 “미국 현지화 CAPEX = Green”이 아니라는 반례다. 2조 원 유상증자는 GM JV와 Hungary 증설 등에는 필요하지만, 시장에서는 기존 주주 희석과 EV 수요 둔화 우려로 받아들였다. Reuters는 신주 발행가가 169,200원에서 146,200원으로 14% 낮아졌고, 당시 주가가 연초 대비 29.5% 하락했다고 보도했다. 이후 Stellantis가 Samsung SDI와의 StarPlus Energy JV에서 빠지는 방안을 검토한다는 보도까지 나왔다. 이는 아직 확정 hard 4C는 아니지만, EV battery JV quality에 강한 4C-watch다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters share-sale / JV-exit report anchors

stage3_price:
N/A

planned_share_issuance:
2T won / $1.4B

new_shares:
11,821,000 shares

initial_offering_price:
169,200 won

revised_offering_price:
146,200 won

offering_price_cut:
146,200 / 169,200 - 1
= -13.59%

reported_price_cut:
-14%

Samsung_SDI_YTD_drawdown_context:
-29.5%

event_day_Samsung_SDI_MAE:
-1.0%

KOSPI_same_context:
-0.5%

relative_underperformance:
-1.0 - (-0.5)
= -0.5pp

Stellantis_writedown_context:
> $26.5B

StarPlus_exit_status:
reported / not final decision

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = failed_rerating / 4C_watch
rerating_result = US_battery_localization_dilution_watch
stage_failure_type = policy_capex_and_jv_not_green
```

---

## Case B — LG Energy Solution / Ford·Freudenberg·Ultium `hard 4C + utilization break`

```text
symbol = 373220
case_type = 4C-thesis-break
archetype = EV_BATTERY_CONTRACT_QUALITY_BREAK / EV_BATTERY_JV_RESTRUCTURING
```

### stage date

```text
Stage 1:
2024~2025
- Ford Europe EV battery supply
- Freudenberg battery systems supply
- GM-LGES Ultium U.S. battery localization
- EV backlog headline

Stage 2:
약함
- headline contract 존재
- U.S. JV plant capacity 존재

Stage 3:
없음
- actual call-off / utilization / margin 전 Green 금지

Stage 4C:
2025-12-17
- Ford cancels 9.6T won / $6.5B LGES EV battery deal
- LGES shares as much as -7.6% on Dec 18
- KOSPI -1.4%

Stage 4C 강화:
2025-12-26
- Freudenberg cancels 3.9T won / $2.7B order
- total expected revenue loss 13.5T won
- LGES 2024 revenue 25.62T won

Stage 4C / utilization watch:
2026-05-12
- GM-LGES Ultium Ohio full restart date uncertain
- around 850 workers laid off since January
- pre-idle workforce around 1,330
- 480 workers laid off indefinitely
```

LGES는 이번 R3 Loop 12의 확정 hard 4C다. Ford와 Freudenberg 계약 취소로 약 13.5조 원 기대매출이 사라졌고, 이는 2024년 LGES 매출 25.62조 원의 52.7%다. 여기에 GM-LGES Ultium Ohio 공장 restart uncertainty가 붙으면서, “계약 headline”과 “실제 utilization”을 분리해야 한다는 점이 더 강해졌다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters cancellation / event-return / Ultium restart anchors

stage3_price:
N/A

Ford_cancelled_contract:
9.6T won / $6.5B

Freudenberg_cancelled_contract:
3.9T won / $2.7B

total_lost_expected_revenue:
13.5T won

LGES_2024_revenue:
25.62T won

lost_revenue_vs_2024_revenue:
13.5 / 25.62
= 52.7%

LGES_Ford_event_MAE:
-7.6%

KOSPI_same_context:
-1.4%

relative_underperformance:
-7.6 - (-1.4)
= -6.2pp

Ultium_Ohio_workers_laid_off_since_January:
about 850

Ultium_pre_idle_workforce:
about 1,330

indefinite_layoffs:
480

full_restart_status:
uncertain

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = EV_battery_contract_and_utilization_break
stage_failure_type = hard_4C
```

---

## Case C — SK On / Ford JV split + ESS pivot `4C-watch + success_candidate`

```text
symbol = 096770 parent exposure
case_type = 4C-watch + success_candidate
archetype = EV_BATTERY_JV_RESTRUCTURING / EV_TO_ESS_CAPACITY_REDEPLOYMENT
```

### stage date

```text
Stage 1:
2024~2025
- Ford-SK U.S. battery JV
- BlueOval SK Kentucky / Tennessee plants
- EV battery demand expectation

Stage 4C-watch:
2025-12-11
- SK On and Ford end U.S. battery JV
- original investment $11.4B
- Ford takes Kentucky plants
- SK On takes Tennessee plant
- SK On Q3 2025 OP loss 124.8B won
- previous quarter loss 66.4B won

Stage 2 / ESS pivot:
2025-09-03
- SK On signs Flatiron LFP ESS supply deal
- up to 7.2GWh
- 2026~2030 supply period
- some Georgia EV lines to be converted to ESS

Stage 3:
없음
- JV split 이후 ESS pivot은 Stage 2
- contract value, utilization, OPM, FCF 확인 전 Green 금지
```

SK On은 “EV battery overbuild → ESS redeployment”를 봐야 하는 case다. Ford와의 11.4억 달러가 아니라 **$11.4B** 규모 JV가 해체되고, SK On은 Tennessee plant를 가져가며 ESS pivot을 가속한다. 다만 Q3 2025 영업손실은 1,248억 원으로 직전 분기 664억 원의 거의 두 배다. Flatiron 7.2GWh ESS 계약은 좋은 Stage 2지만, 아직 contract value와 margin은 없다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters JV termination / ESS contract anchors

stage3_price:
N/A

original_Ford_SK_JV_investment:
$11.4B

asset_split:
Ford takes Kentucky battery plants
SK On takes Tennessee plant

SK_On_Q3_2025_OP_loss:
124.8B won

previous_quarter_OP_loss:
66.4B won

loss_worsening:
124.8 / 66.4 - 1
= +88.0%

Flatiron_ESS_contract_volume:
up to 7.2GWh

Flatiron_supply_period:
2026~2030

contract_value:
not disclosed

production_start:
2H 2026 target

capacity_redeployment:
some Georgia EV lines to ESS

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = 4C_watch_plus_success_candidate
rerating_result = EV_JV_break_then_ESS_pivot_watch
stage_failure_type = stage2_pivot_not_green
```

---

## Case D — POSCO Future M / SK IE Tech / EcoPro Materials basket `supply-chain demand shock`

```text
symbols = 003670 / 361610 / 450080 / 096770 / 373220 / 006400
case_type = 4C-watch
archetype = BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK
```

### stage date

```text
Stage 1:
2025
- Ford EV strategy reset
- lower-battery-content hybrid pivot
- cathode / separator / precursor demand risk

Stage 4C-watch:
2025-12-16
- Ford kills several EV models
- LGES -6%
- Samsung SDI -3.5%
- POSCO Future M -8.2%

Stage 4C-watch 추가:
2025-12-16
- SK Innovation -3%
- SK IE Technology -5%
- EcoPro Materials -5%
- Ford F-150 Lightning halt / lower battery content hybrid shift
```

이 basket은 R3 소재·분리막·전구체의 “고객 EV model risk”를 보여준다. Ford가 EV 모델을 축소하고 hybrid로 선회하자 LGES, Samsung SDI뿐 아니라 POSCO Future M, SK IE Technology, EcoPro Materials까지 동반 하락했다. 공급망 기업은 셀 업체보다 더 민감하게 빠질 수 있다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / MarketWatch battery supply-chain shock anchors

stage3_price:
N/A

LGES_event_MAE:
-6.0%

Samsung_SDI_event_MAE:
-3.5%

POSCO_Future_M_event_MAE:
-8.2%

SK_Innovation_event_MAE:
-3.0%

SK_IE_Technology_event_MAE:
-5.0%

EcoPro_Materials_event_MAE:
-5.0%

relative_POSCO_Future_M_vs_LGES:
-8.2 - (-6.0)
= -2.2pp

Ford_policy:
EV model cuts / lower-battery-content hybrid shift

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = battery_material_separator_precursor_demand_shock
stage_failure_type = 4C_watch
```

---

## Case E — SK / Group14 silicon-anode optionality `success_candidate / not Green`

```text
symbol = 034730 exposure
case_type = success_candidate
archetype = SILICON_ANODE_OPTIONALITY
```

### stage date

```text
Stage 1:
2025
- silicon-carbon anode material
- faster charging / higher energy density
- Korea BAM factory / regional supply chain

Stage 2:
2025-08-20
- Group14 raises $463M Series D led by SK
- total equity raised > $1B
- Group14 acquires remaining 75% of JV with SK
- gains full control of South Korea BAM factory
- Korea factory produces SCC55 at EV scale

Stage 3:
없음
- 투자·소재 optionality만으로 Green 금지
- customer offtake, Korean plant utilization, margin, SK equity-method value 확인 필요

Stage 4B:
silicon-anode / fast-charging theme로 SK or battery-material basket이 먼저 움직이면 후보

Stage 4C:
technology adoption delay, customer qualification failure, valuation impairment
```

SK의 Group14 exposure는 alternative battery material Stage 2다. Group14는 SK가 주도한 $463M Series D를 마쳤고, SK와의 JV 잔여 75%를 인수해 한국 battery active material factory를 완전히 소유하게 됐다. 다만 SK 주주 관점에서는 아직 Green이 아니다. actual offtake, utilization, margin, equity-method value가 필요하다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters Group14 financing / JV control anchor

stage3_price:
N/A

Series_D_funding:
$463M

lead_investor:
SK

total_equity_raised:
> $1B

JV_stake_acquired_by_Group14:
remaining 75%

Korea_BAM_factory:
fully controlled by Group14 after transaction

material:
SCC55 silicon-carbon composite

valuation:
higher than >$1B 2022 round, exact value not disclosed

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = silicon_anode_optional_materials_watch
stage_failure_type = investment_optional_not_green
```

---

## Case F — Hanwha Qcells `success_candidate + customs 4C-watch`

```text
symbol = 009830 / 000880 exposure
case_type = success_candidate + 4C-watch
archetype = SOLAR_US_SUPPLY_CHAIN_LOCALIZATION / SOLAR_CUSTOMS_UFLPA_4C_WATCH
```

### stage date

```text
Stage 1:
2024-08-08
- U.S. solar supply-chain localization
- IRA domestic manufacturing support
- Qcells Georgia vertical supply-chain buildout

Stage 2:
2024-08-08
- DOE conditional loan guarantee up to $1.45B
- Cartersville facility investment $2.5B
- panels / cells / ingots / wafers
- nearly 2,000 jobs when fully operational

Stage 4C-watch:
2025-11-08
- U.S. customs detains components under forced-labor import law
- Qcells furloughs about 1,000 workers
- cuts about 300 staffing-agency workers
- reduced hours / production curtailment

Stage 3:
없음
- loan guarantee / localization alone is not Green
- component flow, utilization, gross margin, FCF 확인 필요
```

Qcells는 “미국 현지화 = Green”이 아니라는 solar-side 반례다. DOE loan guarantee와 $2.5B plant는 좋은 Stage 2지만, UFLPA/customs detention 하나로 약 1,000명 furlough와 300명 contract-worker cut이 발생했다. 즉 R3 solar는 subsidy보다 **component-flow reliability**가 먼저다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters Qcells DOE loan / customs disruption anchors

stage3_price:
N/A

DOE_conditional_loan_guarantee:
up to $1.45B

Cartersville_facility_investment:
$2.5B

facility_scope:
solar panels
cells
ingots
wafers

jobs_when_fully_operational:
nearly 2,000

furloughed_or_reduced_hours_workers:
about 1,000

contract_workers_cut:
about 300

affected_direct_workers_total:
about 1,300

cause:
U.S. customs detentions under forced-labor import law / UFLPA context

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_plus_4C_watch
rerating_result = solar_localization_with_supply_chain_break_watch
stage_failure_type = localization_not_green_until_component_flow_margin_FCF
```

---

## Case G — Hyundai Motor hydrogen fuel-cell plant `success_candidate / capex optionality`

```text
symbol = 005380
case_type = success_candidate
archetype = HYDROGEN_FUELCELL_CAPEX_OPTIONALITY
```

### stage date

```text
Stage 1:
2025-10-30
- hydrogen-powered mobility
- fuel cells and electrolyzers
- future mobility / green industrial conversion

Stage 2:
2025-10-30
- Hyundai breaks ground on Ulsan hydrogen fuel-cell facility
- investment 930B won / $654M
- 43,000 square meters
- products: fuel cells and electrolyzers
- applications: passenger cars, trucks, buses, construction machinery, marine vessels
- completion expected 2027

Stage 3:
없음
- capex와 plant construction만으로 Green 금지
- customer offtake, utilization, hydrogen economics, margin, FCF 확인 필요

Stage 4B:
hydrogen theme로 price가 먼저 움직이면 후보

Stage 4C:
hydrogen adoption delay, utilization failure, policy subsidy rollback, capex drag
```

Hyundai hydrogen plant는 R3의 green-industrial optionality다. 9,300억 원 capex, fuel cell·electrolyzer 생산, 2027년 완공 목표는 Stage 2가 될 수 있다. 그러나 hydrogen은 특히 utilization과 offtake가 없으면 투자 story에 머물기 쉽다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters hydrogen fuel-cell plant anchor

stage3_price:
N/A

investment:
930B won / $654M

facility_area:
43,000 square meters

completion_target:
2027

products:
fuel cells
electrolyzers

applications:
passenger cars
commercial trucks
buses
construction equipment
marine vessels

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = hydrogen_fuelcell_capex_watch
stage_failure_type = capex_not_green_until_offtake_utilization_margin
```

---

## Case H — Hyundai-LG Georgia battery plant raid `factory execution / visa 4C-watch`

```text
symbols = 005380 / 373220
case_type = 4C-watch
archetype = US_FACTORY_EXECUTION_VISA_RISK
```

### stage date

```text
Stage 1:
2025
- U.S. battery localization
- Hyundai-LG battery plant construction
- skilled Korean installation workforce dependence

Stage 4C-watch:
2025-09
- U.S. raid at Hyundai-LG Georgia battery site
- about 475 workers detained in Reuters context
- more than 300 Korean workers detained in AP context
- plant operations delayed 2~3 months

Stage 4C relief:
2025-11
- some workers returned and resumed work
- construction back on track
- HL-GA Battery targets production in H1 2026
```

Hyundai-LG Georgia case는 “미국 현지화”의 숨은 병목을 보여준다. 자본과 공장부지는 있어도 skilled installation workforce, visa, subcontractor compliance가 막히면 공장 start-up이 지연된다. Reuters는 raid 이후 LGES North America president가 future ICE raid 회피를 낙관했지만, 이미 operation이 2~3개월 지연됐다고 보도했다. AP는 일부 workers가 복귀해 공사가 다시 정상화됐고, HL-GA Battery가 2026년 상반기 생산 개시를 목표로 한다고 보도했다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP factory execution and visa-risk anchors

stage3_price:
N/A

detained_workers_Reuters_context:
about 475

detained_Korean_workers_AP_context:
over 300

startup_delay:
2~3 months

project:
Hyundai-LG Georgia battery plant / HL-GA Battery

4C_relief:
some workers returned and construction resumed

production_target:
H1 2026

local_hiring:
ongoing

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = US_battery_factory_execution_visa_watch
stage_failure_type = 4C_watch_not_hard_4C
```

---

# 5. 이번 R3 case별 요약표

| case                                      | 분류                           |                                                                        실제 가격검증 | alignment                  |
| ----------------------------------------- | ---------------------------- | -----------------------------------------------------------------------------: | -------------------------- |
| Samsung SDI / StarPlus                    | failed_rerating + 4C-watch   |                    share-sale price -13.6%, YTD -29.5%, Stellantis exit report | JV/dilution watch          |
| LGES / Ford·Freudenberg·Ultium            | hard 4C                      | lost revenue 13.5T won, 52.7% of 2024 revenue, -7.6%, Ultium restart uncertain | contract/utilization break |
| SK On / Ford JV + ESS                     | 4C-watch + success_candidate |                             $11.4B JV split, Q3 loss +88%, Flatiron 7.2GWh ESS | pivot Stage 2              |
| POSCO Future M / SKIET / EcoPro Materials | 4C-watch                     |                          POSCO Future M -8.2%, SKIET -5%, EcoPro Materials -5% | supply-chain demand shock  |
| SK / Group14                              | success_candidate            |                     $463M Series D, total equity >$1B, Korea BAM plant control | silicon-anode Stage 2      |
| Hanwha Qcells                             | success_candidate + 4C-watch |                                DOE $1.45B guarantee, 1,000 furloughs, 300 cuts | solar supply-chain watch   |
| Hyundai hydrogen plant                    | success_candidate            |                                      930B won capex, 43,000m², completion 2027 | hydrogen capex Stage 2     |
| Hyundai-LG Georgia                        | 4C-watch                     |                      475 detained, delay 2~3 months, production target H1 2026 | factory execution risk     |

---

# 6. score-price alignment 판정

```text
success_candidate:
- SK On ESS pivot
- SK / Group14 silicon-anode optionality
- Hanwha Qcells U.S. solar localization, but with 4C-watch
- Hyundai hydrogen fuel-cell plant

failed_rerating:
- Samsung SDI share-sale / JV capex dilution

hard_4C:
- LGES Ford/Freudenberg contract-quality break

4C-watch:
- SK On / Ford JV split
- POSCO Future M / SKIET / EcoPro Materials supply-chain shock
- Hanwha Qcells customs/UFLPA disruption
- Hyundai-LG Georgia visa/factory execution risk
- Samsung SDI / Stellantis JV exit report

price_moved_without_evidence:
- hydrogen capex rally before offtake/utilization
- silicon-anode optionality before customer volume
- ESS pivot headline before contract value / OPM / FCF
```

---

# 7. 점수비중 교정

## 올릴 축

```text
actual_calloff +5
take_or_pay_quality +5
GWh_volume +5
delivery_schedule +5
utilization_visibility +5
ESS_revenue_conversion +5
line_redeployment_execution +4
OPM_visibility +5
FCF_after_capex +5
supply_chain_flow_reliability +5
factory_execution_readiness +5
```

### 왜 올리나

LGES hard 4C는 contract headline이 actual call-off로 닫히지 않으면 무너진다는 증거다. SK On은 ESS pivot이 좋지만 contract value와 margin이 없다. Qcells는 subsidy와 plant가 있어도 customs flow가 막히면 production이 끊긴다. Hyundai-LG Georgia는 공장 현지화가 visa/workforce execution을 통과해야 한다.

## 내릴 축

```text
EV_JV_headline_only -5
U.S._localization_capex_only -5
share_issuance_for_capex -5
customer_exit_report -5
ESS_pivot_without_contract_value -4
silicon_anode_optionality_only -4
hydrogen_capex_without_offtake -5
solar_loan_guarantee_without_component_flow -5
factory_startup_visa_risk -5
EV_demand_shock -5
```

### 왜 내리나

Samsung SDI는 capex 조달이 필요했지만 시장은 dilution과 EV demand risk로 봤다. SK On/Ford split은 ESS pivot의 이유이면서도 기존 EV investment thesis의 손상이다. Hyundai hydrogen은 capex는 크지만 offtake가 없다. Qcells는 U.S. localization이 있어도 component detention으로 바로 생산차질이 났다.

## Green gate 강화 조건

```text
R3 Stage 3-Green 필수:
1. actual call-off / take-or-pay 확인
2. GWh volume과 supply period 확인
3. delivery / revenue recognition 시작
4. utilization 개선
5. OPM / gross margin 확인
6. FCF after capex 확인
7. subsidy 제외 unit economics 확인
8. customs / visa / labor / supply-chain flow risk 통과
9. price path가 evidence 이후 따라옴

금지:
EV JV headline만 있음
미국 현지화 capex만 있음
ESS pivot만 있음
hydrogen plant만 있음
silicon-anode optionality만 있음
loan guarantee만 있음
contract cancellation 존재
customs detention 존재
factory startup delay 존재
```

## 4B 조기감지 조건

```text
4B-watch:
ESS pivot 뉴스로 급등
EV line conversion headline로 valuation 확장
silicon-anode / hydrogen / solar localization theme 급등
loan guarantee 발표 후 revenue 전 price 상승
U.S. factory opening 기대가 utilization보다 먼저 반영
capex funding / share issuance 뒤에도 valuation 유지
```

## 4C hard gate 조건

```text
contract cancellation
contract value collapse
customer EV model cancellation
JV dissolution / customer exit
plant idling
utilization failure
large layoff / restart uncertainty
customs detention causing production cut
visa raid / factory startup delay
share issuance dilution with weak demand
OPM collapse
FCF deterioration
```

이번 R3 Loop 12의 확정 hard 4C는 **LGES Ford/Freudenberg contract-quality break**다. Samsung SDI/Stellantis, SK On/Ford, Qcells UFLPA, Hyundai-LG Georgia는 hard 4C가 아니라 강한 4C-watch로 둔다.

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

## docs/round/round_187.md 요약

```md
# R3 Loop 12. Battery / EV / Green Price Validation

이번 라운드는 R3 Loop 12 price-validation 라운드다.

핵심 결론:
- Samsung SDI is failed-rerating / JV 4C-watch. The planned 2T won share issuance price was cut from 169,200 won to 146,200 won, or -13.6%, while shares were down 29.5% YTD. Stellantis reportedly considered exiting its Samsung SDI U.S. battery JV after >$26.5B writedowns.
- LGES is hard 4C. Ford cancelled 9.6T won / $6.5B and Freudenberg cancelled 3.9T won / $2.7B, total lost expected revenue 13.5T won, or 52.7% of 2024 revenue. LGES fell as much as -7.6%. Ultium Ohio restart remains uncertain.
- SK On is 4C-watch plus ESS success_candidate. Ford/SK $11.4B JV will end; SK On takes Tennessee, Ford takes Kentucky. Q3 OP loss worsened to 124.8B won from 66.4B won. Flatiron ESS deal up to 7.2GWh is Stage 2, not Green.
- POSCO Future M / SK IE Technology / EcoPro Materials are battery supply-chain 4C-watch. Ford EV retreat hit POSCO Future M -8.2%, SK IE Tech -5%, EcoPro Materials -5%.
- SK / Group14 is silicon-anode Stage 2. Group14 raised $463M led by SK and acquired the remaining 75% of the JV, gaining full control of the Korea BAM factory. Offtake/utilization/margin required.
- Hanwha Qcells is solar localization Stage 2 plus UFLPA 4C-watch. DOE loan guarantee up to $1.45B for a $2.5B plant, but customs delays caused about 1,000 furloughs and 300 contract-worker cuts.
- Hyundai hydrogen fuel-cell plant is green-industrial capex Stage 2. 930B won / $654M plant, 43,000m², completion 2027. Offtake/utilization/hydrogen economics required.
- Hyundai-LG Georgia battery plant raid is factory-execution 4C-watch. About 475 workers were detained in Reuters context, over 300 Koreans in AP context, startup delayed 2~3 months, but construction later resumed with H1 2026 production target.
```

## docs/checkpoints/checkpoint_28a_round187_r3_loop12.md 요약

```md
# Checkpoint 28A Round 187 R3 Loop 12 Battery EV Green Price Validation

## 반영 내용
- R3 Loop 12 price-validation 라운드를 추가했다.
- EV battery contract break, EV JV restructuring, ESS redeployment, supply-chain shock, silicon-anode optionality, solar UFLPA disruption, hydrogen capex, U.S. factory visa risk를 비교했다.
- Reuters / FT / AP / MarketWatch anchors로 가능한 MFE/MAE 및 event metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- actual call-off, take-or-pay, GWh volume, delivery schedule, utilization, ESS revenue conversion, OPM/FCF, component-flow reliability, factory-execution readiness 가중치 강화
- EV JV headline-only, U.S. localization capex-only, share issuance for capex, ESS pivot without contract value, hydrogen capex without offtake, customs/visa risk 감점 강화
```

## data/e2r_case_library/cases_r3_loop12_round187.jsonl 초안

```jsonl
{"case_id":"r3_loop12_samsung_sdi_starplus_share_sale_4c_watch","symbol":"006400","company_name":"Samsung SDI","case_type":"failed_rerating","primary_archetype":"US_BATTERY_LOCALIZATION_DILUTION","stage2_date":"2025-03/2025-04","stage4c_date":"2026-02-10_watch","price_validation":{"price_data_source":"Reuters share-sale and JV-exit report anchors","stage3_price":null,"planned_share_issuance_krw_trn":2.0,"new_shares":11821000,"initial_offering_price_krw":169200,"revised_offering_price_krw":146200,"offering_price_cut_pct":-13.59,"reported_price_cut_pct":-14,"samsung_sdi_ytd_drawdown_context_pct":-29.5,"event_day_samsung_sdi_mae_pct":-1.0,"kospi_same_context_pct":-0.5,"relative_underperformance_pp":-0.5,"stellantis_writedown_context_usd_bn":26.5,"starplus_exit_status":"reported_not_final","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"failed_rerating_4C_watch","rerating_result":"US_battery_localization_dilution_watch","notes":"U.S. localization capex and JV story are not Green when dilution and customer-exit risk are unresolved."}
{"case_id":"r3_loop12_lges_contract_quality_ultium_utilization_break","symbol":"373220","company_name":"LG Energy Solution","case_type":"4c_thesis_break","primary_archetype":"EV_BATTERY_CONTRACT_QUALITY_BREAK","stage4c_date":"2025-12-17/2025-12-26/2026-05-12","price_validation":{"price_data_source":"Reuters cancellation/event-return/Ultium restart anchors","stage3_price":null,"ford_cancelled_contract_krw_trn":9.6,"ford_cancelled_contract_usd_bn":6.5,"freudenberg_cancelled_contract_krw_trn":3.9,"freudenberg_cancelled_contract_usd_bn":2.7,"total_lost_expected_revenue_krw_trn":13.5,"lges_2024_revenue_krw_trn":25.62,"lost_revenue_vs_2024_revenue_pct":52.7,"lges_ford_event_mae_pct":-7.6,"kospi_same_context_pct":-1.4,"relative_underperformance_pp":-6.2,"ultium_ohio_laid_off_since_january":850,"ultium_pre_idle_workforce":1330,"indefinite_layoffs":480,"full_restart_status":"uncertain","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"EV_battery_contract_and_utilization_break","notes":"Contract cancellations and plant restart uncertainty are hard 4C."}
{"case_id":"r3_loop12_skon_ford_jv_split_ess_pivot","symbol":"096770_parent_exposure","company_name":"SK On / SK Innovation","case_type":"4c_watch","primary_archetype":"EV_BATTERY_JV_RESTRUCTURING","stage4c_date":"2025-12-11","stage2_date":"2025-09-03","price_validation":{"price_data_source":"Reuters JV termination and ESS contract anchors","stage3_price":null,"original_ford_sk_jv_investment_usd_bn":11.4,"asset_split":"Ford takes Kentucky plants; SK On takes Tennessee plant","sk_on_q3_2025_op_loss_krw_bn":124.8,"previous_quarter_op_loss_krw_bn":66.4,"loss_worsening_pct":88.0,"flatiron_ess_contract_volume_gwh":7.2,"flatiron_supply_period":"2026-2030","contract_value":"not_disclosed","production_start":"2H_2026_target","capacity_redeployment":"some Georgia EV lines to ESS","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"4C_watch_plus_success_candidate","rerating_result":"EV_JV_break_then_ESS_pivot_watch","notes":"JV split is EV thesis damage; ESS pivot is Stage 2 until contract value/utilization/margin/FCF confirm."}
{"case_id":"r3_loop12_battery_supply_chain_ford_demand_shock","symbol":"003670/361610/450080/096770/373220/006400","company_name":"POSCO Future M / SK IE Tech / EcoPro Materials / battery supply-chain basket","case_type":"4c_watch","primary_archetype":"BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK","stage4c_date":"2025-12-16","price_validation":{"price_data_source":"Reuters/MarketWatch battery supply-chain shock anchors","stage3_price":null,"lges_event_mae_pct":-6.0,"samsung_sdi_event_mae_pct":-3.5,"posco_future_m_event_mae_pct":-8.2,"sk_innovation_event_mae_pct":-3.0,"sk_ie_technology_event_mae_pct":-5.0,"ecopro_materials_event_mae_pct":-5.0,"posco_future_m_relative_vs_lges_pp":-2.2,"ford_policy":"EV model cuts / lower-battery-content hybrid shift","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"battery_material_separator_precursor_demand_shock","notes":"Ford EV retreat hit cathode/separator/precursor names; 4C-watch for demand shock."}
{"case_id":"r3_loop12_sk_group14_silicon_anode_optional","symbol":"034730_exposure","company_name":"SK / Group14 Technologies","case_type":"success_candidate","primary_archetype":"SILICON_ANODE_OPTIONALITY","stage2_date":"2025-08-20","price_validation":{"price_data_source":"Reuters Group14 financing/JV control anchor","stage3_price":null,"series_d_funding_usd_mn":463,"lead_investor":"SK","total_equity_raised_usd_bn":1.0,"jv_stake_acquired_by_group14_pct":75,"korea_bam_factory":"fully controlled by Group14 after transaction","material":"SCC55 silicon-carbon composite","valuation":"higher than >$1B 2022 round; exact value not disclosed","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"silicon_anode_optional_materials_watch","notes":"Silicon-anode optionality is Stage 2; offtake, utilization, margin and SK equity value required before Green."}
{"case_id":"r3_loop12_hanwha_qcells_solar_uflpa_4c_watch","symbol":"009830/000880_exposure","company_name":"Hanwha Qcells / Hanwha Solutions exposure","case_type":"success_candidate_4c_watch","primary_archetype":"SOLAR_US_SUPPLY_CHAIN_LOCALIZATION","stage2_date":"2024-08-08","stage4c_date":"2025-11-08","price_validation":{"price_data_source":"Reuters Qcells loan/customs disruption anchors","stage3_price":null,"doe_conditional_loan_guarantee_usd_bn":1.45,"cartersville_facility_investment_usd_bn":2.5,"facility_scope":["solar panels","cells","ingots","wafers"],"jobs_when_fully_operational":2000,"furloughed_or_reduced_hours_workers":1000,"contract_workers_cut":300,"affected_direct_workers_total":1300,"cause":"U.S. customs detentions under forced-labor import law / UFLPA context","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_plus_4C_watch","rerating_result":"solar_localization_with_supply_chain_break_watch","notes":"Loan guarantee and U.S. localization are Stage 2; component-flow reliability required before Green."}
{"case_id":"r3_loop12_hyundai_hydrogen_fuelcell_capex","symbol":"005380","company_name":"Hyundai Motor hydrogen fuel-cell plant","case_type":"success_candidate","primary_archetype":"HYDROGEN_FUELCELL_CAPEX_OPTIONALITY","stage2_date":"2025-10-30","price_validation":{"price_data_source":"Reuters hydrogen fuel-cell plant anchor","stage3_price":null,"investment_krw_bn":930,"investment_usd_mn":654,"facility_area_sqm":43000,"completion_target_year":2027,"products":["fuel cells","electrolyzers"],"applications":["passenger cars","commercial trucks","buses","construction equipment","marine vessels"],"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"hydrogen_fuelcell_capex_watch","notes":"Hydrogen fuel-cell capex is Stage 2; offtake, utilization, hydrogen economics, margin and FCF required before Green."}
{"case_id":"r3_loop12_hyundai_lg_georgia_factory_visa_execution_watch","symbol":"005380/373220","company_name":"Hyundai-LG Georgia battery plant / HL-GA Battery","case_type":"4c_watch","primary_archetype":"US_FACTORY_EXECUTION_VISA_RISK","stage4c_date":"2025-09","price_validation":{"price_data_source":"Reuters/AP factory execution and visa-risk anchors","stage3_price":null,"detained_workers_reuters_context":475,"detained_korean_workers_ap_context":300,"startup_delay_months":"2-3","project":"Hyundai-LG Georgia battery plant / HL-GA Battery","relief":"some workers returned and construction resumed","production_target":"H1_2026","local_hiring":"ongoing","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"US_battery_factory_execution_visa_watch","notes":"U.S. factory localization needs visa/skilled-worker/subcontractor execution, not just capex."}
```

## data/sector_taxonomy/score_weight_profiles_round187_r3_loop12_v1.csv 초안

```csv
archetype,actual_calloff,take_or_pay,gwh_volume,delivery_schedule,utilization,ess_revenue,line_redeployment,opm_visibility,fcf_after_capex,supply_chain_flow,factory_execution,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
EV_BATTERY_CONTRACT_QUALITY_BREAK,+5,+5,+5,+5,+5,+0,+0,+5,+5,+3,+3,0,+3,+5,LGES/Ford/Freudenberg shows contract headline can become hard 4C without actual call-off.
EV_BATTERY_JV_RESTRUCTURING,+4,+4,+5,+4,+5,+3,+4,+5,+5,+3,+5,-5,+4,+5,SK On/Ford and Samsung/Stellantis JV risks require 4C-watch.
EV_TO_ESS_CAPACITY_REDEPLOYMENT,+4,+4,+5,+5,+5,+5,+5,+5,+5,+3,+4,-3,+5,+4,ESS pivot is Stage 2 until contract value/utilization/margin/FCF confirm.
US_BATTERY_LOCALIZATION_DILUTION,+3,+3,+4,+4,+4,+2,+3,+4,+5,+4,+5,-5,+4,+5,Samsung SDI share issuance shows capex localization can fail without demand/funding clarity.
BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK,+0,+0,+0,+0,+0,+0,+0,+4,+4,+4,+3,0,+3,+5,Ford EV retreat hit cathode/separator/precursor names directly.
SILICON_ANODE_OPTIONALITY,+3,+3,+3,+3,+4,+0,+0,+4,+5,+3,+3,-4,+4,+4,Group14/SK is Stage 2 optionality until offtake and utilization confirm.
SOLAR_US_SUPPLY_CHAIN_LOCALIZATION,+3,+3,+4,+4,+5,+0,+0,+5,+5,+5,+5,-4,+4,+5,Qcells loan guarantee is Stage 2; customs/component flow can create 4C-watch.
HYDROGEN_FUELCELL_CAPEX_OPTIONALITY,+2,+2,+2,+4,+5,+0,+0,+5,+5,+3,+4,-5,+4,+4,Hyundai hydrogen plant is capex Stage 2 until offtake/utilization/margin confirm.
US_FACTORY_EXECUTION_VISA_RISK,+0,+0,+0,+0,+5,+0,+0,+4,+5,+3,+5,0,+3,+5,Hyundai-LG Georgia raid proves U.S. factory execution risk must be a hard gate candidate.
```

---

# 이번 R3 Loop 12 결론

```text
1. LGES는 R3 hard 4C다.
   Ford/Freudenberg 취소와 Ultium restart uncertainty가 계약·가동률 리스크를 동시에 보여준다.

2. Samsung SDI는 미국 현지화 capex가 Green이 아니라 dilution/JV 4C-watch가 될 수 있음을 보여준다.

3. SK On은 Ford JV split 이후 ESS pivot Stage 2다.
   그러나 contract value, utilization, OPM, FCF 전에는 Green이 아니다.

4. POSCO Future M / SKIET / EcoPro Materials는 EV demand shock의 공급망 전이 case다.
   셀보다 소재·분리막·전구체가 더 크게 빠질 수 있다.

5. SK / Group14는 silicon-anode optionality Stage 2다.
   고객 offtake와 한국 BAM factory utilization 전 Stage 3 금지다.

6. Qcells는 solar localization Stage 2이지만 UFLPA/customs 4C-watch다.
   subsidy보다 component-flow reliability가 먼저다.

7. Hyundai hydrogen plant는 green-industrial capex Stage 2다.
   offtake, utilization, hydrogen economics 전에는 Green이 아니다.

8. Hyundai-LG Georgia raid는 U.S. battery localization의 execution 4C-watch다.
   visa와 skilled-worker bottleneck도 R3 Green gate에 들어가야 한다.
```

한 문장으로 압축하면:

> **R3에서 진짜 Stage 3는 “EV·ESS·수소·태양광·소재 현지화가 좋다”가 아니라, actual call-off·GWh·납기·가동률·OPM·FCF가 확인되고, contract cancellation·customs·visa·dilution·EV demand shock을 통과하는 순간이다.**

* [Reuters](https://www.reuters.com/business/energy/lg-energy-solution-cancels-39-trillion-won-battery-order-with-freudenberg-2025-12-26/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/legal/litigation/gms-restart-date-ohio-battery-plant-uncertain-2026-05-12/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/autos-transportation/south-koreas-sk-ford-motor-end-us-battery-joint-venture-2025-12-11/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/autos-transportation/stellantis-seeks-exit-battery-venture-with-samsung-ev-losses-mount-bloomberg-2026-02-10/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/asia/samsung-sdi-cuts-stock-offering-price-by-14-2025-04-09/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/shares-lg-energy-solution-fall-6-after-ford-retreats-ev-push-2025-12-16/?utm_source=chatgpt.com)
* [마켓워치](https://www.marketwatch.com/story/while-ford-shares-are-remarkably-steady-after-20-billion-charge-these-stocks-are-getting-battered-bbbcfa04?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/sustainability/climate-energy/qcells-furloughs-1000-workers-us-solar-factories-due-stalled-shipments-2025-11-08/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/hyundai-motor-breaks-ground-680-million-hydrogen-fuel-cell-plant-south-korea-2025-10-30/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/autos-transportation/lges-executive-is-optimistic-battery-maker-will-avoid-future-ice-raids-2025-09-16/?utm_source=chatgpt.com)

[1]: https://www.reuters.com/markets/asia/samsung-sdi-cuts-stock-offering-price-by-14-2025-04-09/?utm_source=chatgpt.com "Samsung SDI cuts pricing of $1.4 billion share-sale as global markets tumble"
[2]: https://www.reuters.com/business/finance/south-koreas-lg-energy-solution-ends-65-billion-ev-battery-supply-deal-with-ford-2025-12-17/?utm_source=chatgpt.com "Ford cancels EV battery deal worth $6.5 billion with South Korea's LG Energy Solution"
[3]: https://www.reuters.com/business/autos-transportation/south-koreas-sk-ford-motor-end-us-battery-joint-venture-2025-12-11/?utm_source=chatgpt.com "South Korea's SK On, Ford Motor to end US battery joint venture"
[4]: https://www.reuters.com/world/asia-pacific/shares-lg-energy-solution-fall-6-after-ford-retreats-ev-push-2025-12-16/?utm_source=chatgpt.com "Shares of LG Energy Solution fall 6% after Ford retreats from EV push"
[5]: https://www.reuters.com/business/finance/porsche-backed-group14-closes-new-funding-takes-control-jvs-battery-material-2025-08-20/?utm_source=chatgpt.com "Porsche-backed Group14 closes new funding, takes control of JV's battery material plant"
[6]: https://www.reuters.com/business/energy/us-offers-15-bln-conditional-loan-guarantee-qcells-solar-facility-georgia-2024-08-08/?utm_source=chatgpt.com "US offers $1.5 bln conditional loan guarantee to Qcells for solar facility in Georgia"
[7]: https://www.reuters.com/world/asia-pacific/hyundai-motor-breaks-ground-680-million-hydrogen-fuel-cell-plant-south-korea-2025-10-30/?utm_source=chatgpt.com "Hyundai Motor breaks ground on $680 million hydrogen fuel cell plant in South Korea"
[8]: https://www.reuters.com/business/autos-transportation/lges-executive-is-optimistic-battery-maker-will-avoid-future-ice-raids-2025-09-16/?utm_source=chatgpt.com "LGES executive is optimistic the battery maker will avoid future ICE raids"
