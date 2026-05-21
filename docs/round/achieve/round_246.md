순서상 이번은 **R3 Loop 11 — 2차전지·전기차·친환경 가격경로 검증 라운드**다.

이번 R3 Loop 11은 이전처럼 단순히 “EV가 둔화됐다 / ESS가 좋다”가 아니라, **EV line → ESS 전환이 실제 계약으로 찍혔는지**, **계약이 고객명·GWh·납기·마진·가동률로 닫히는지**, **EV 수요 후퇴가 공급망을 얼마나 깨는지**, **태양광·리튬·미국 현지화가 정책 이벤트인지 실제 수익인지**를 나눠 본다.

```text
round = R3 Loop 11
round_id = round_174
large_sector = BATTERY_EV_GREEN
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
```

---

# 1. 이번 라운드 대섹터

```text
R3 = 2차전지·전기차·친환경
```

R3의 Stage 3는 “ESS 수혜”, “LFP 전환”, “리튬 확보”, “태양광 현지화”가 아니다. **계약이 GWh·offtake·가동률·OPM·FCF로 닫히고, EV 수요 둔화와 정책 리스크를 통과하는 순간**이다.

---

# 2. 대상 canonical archetype

```text
ESS_LFP_GRID_STORAGE
EV_TO_ESS_CAPACITY_REDEPLOYMENT
US_BATTERY_LOCALIZATION
EV_BATTERY_CONTRACT_QUALITY_BREAK
BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK
LITHIUM_RESOURCE_SECURITY
LITHIUM_OFFTAKE_DLE_OPTIONALITY
SOLAR_US_SUPPLY_CHAIN_LOCALIZATION
SOLAR_CUSTOMS_UFLPA_4C_WATCH
EV_FACTORY_EXECUTION_LABOR_IMMIGRATION_RISK
```

---

# 3. deep sub-archetype

```text
ESS 전환:
- Samsung SDI America LFP ESS
- LGES Tesla / unnamed customer LFP ESS
- SK On Flatiron Energy LFP ESS
- EV line conversion / retrofit
- data-center / grid storage demand

계약 품질:
- LGES Ford EV contract cancellation
- LGES Freudenberg contract cancellation
- expected revenue loss vs prior revenue
- contract headline vs actual call-off

소재·리튬:
- POSCO / MinRes lithium JV
- Wodgina / Mt Marion
- spodumene price collapse / rebound
- EnergyX / Anson / DLE / U.S. lithium offtake

태양광:
- Hanwha Qcells U.S. solar localization
- UFLPA customs detention
- furlough / contract-worker cuts
- domestic U.S. supply-chain buildout

EV 공장 execution:
- Hyundai-LG Georgia battery plant
- immigration raid / skilled-worker visa risk
- construction delay / restart

공급망 demand shock:
- Ford EV retreat
- LGES / Samsung SDI / POSCO Future M / EcoPro Materials / SK IE Technology drawdown
```

---

# 4. 국장 신규 후보 case

## Case A — Samsung SDI America `success_candidate + ESS conversion 4B-watch`

```text
symbol = 006400
case_type = success_candidate
archetype = ESS_LFP_GRID_STORAGE / EV_TO_ESS_CAPACITY_REDEPLOYMENT
```

### stage date

```text
Stage 1:
2025
- EV demand slowdown
- U.S. EV subsidy phase-out
- data-center / grid storage demand
- EV battery line → ESS line conversion 필요성 증가

Stage 2:
2025-12-09
- Samsung SDI America signs LFP ESS battery deal
- contract value >2T won / $1.36B
- deliveries begin 2027
- 3-year contract
- U.S. plant existing line retrofit
- shares up as much as +6.1%
- KOSPI -0.1%

Stage 3:
보류
- 고객명 비공개
- actual delivery, utilization, ESS OPM, FCF 확인 전 Green 금지

Stage 4B:
2025-12-09
- EV line conversion / ESS narrative로 주가 +6.1%
- 좋은 Stage 2지만 아직 매출·마진 전

Stage 4C:
고객 call-off 실패, retrofit 지연, ESS margin failure, LFP price pressure
```

Samsung SDI는 R3 Loop 11에서 가장 깔끔한 ESS 전환 Stage 2 후보 중 하나다. Reuters는 Samsung SDI America가 미국 에너지 인프라 개발·운영 회사에 LFP ESS battery를 공급하는 2조 원 이상, 약 13.6억 달러 규모 계약을 맺었고, 2027년부터 3년간 납품한다고 보도했다. 발표 후 Samsung SDI 주가는 장중 최대 6.1% 상승했고, KOSPI는 0.1% 하락했다. 다만 고객명은 공개되지 않았고, 기존 미국 생산라인 retrofit으로 생산하기 때문에 가동률·마진·FCF 확인 전 Stage 3는 보류한다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported contract / event-return anchor

entry_date:
2025-12-09

stage3_price:
N/A

contract_value:
>2T won / $1.36B

delivery_start:
2027

contract_duration:
3 years

customer:
unnamed U.S. energy infrastructure development and operations company

battery_type:
prismatic LFP ESS batteries

production_method:
retrofitting existing Samsung SDI U.S. plant lines

event_MFE_1D:
+6.1%

KOSPI_same_context:
-0.1%

relative_outperformance:
6.1 - (-0.1)
= +6.2pp

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = ESS_LFP_contract_watch
stage_failure_type = stage2_watch_success_not_green
```

---

## Case B — LG Energy Solution / Tesla LFP ESS `success_candidate + customer-confidentiality watch`

```text
symbol = 373220
case_type = success_candidate
archetype = ESS_LFP_GRID_STORAGE / US_BATTERY_LOCALIZATION
```

### stage date

```text
Stage 1:
2025
- U.S. LFP supply-chain localization
- China-dominated LFP battery market
- data-center / grid storage demand

Stage 2:
2025-07-30
- LGES signs $4.3B global LFP battery supply contract
- Reuters source says customer is Tesla
- supply from U.S. factory
- contract period August 2027 to July 2030
- extension option up to 7 years
- volume increase option

Stage 3:
보류
- LGES did not officially identify customer due to confidentiality
- actual delivery, utilization, ESS margin, FCF 필요

Stage 4B:
Tesla name / LFP ESS narrative로 주가가 먼저 과열되면 후보

Stage 4C:
customer call-off failure, U.S. LFP price competition, tariff/subsidy reversal, line ramp delay
```

LGES의 LFP ESS 계약은 구조적으로 강하다. Reuters는 LGES가 43억 달러 규모 LFP battery supply 계약을 체결했고, 사안에 정통한 소식통이 고객이 Tesla라고 말했다고 보도했다. LGES는 고객명을 공식 공개하지 않았지만, 계약 기간은 2027년 8월부터 2030년 7월까지이며, 최대 7년 연장과 물량 확대 옵션이 있다. 미국 LFP 생산 기반은 중국 업체가 지배해온 LFP 시장에서 의미 있는 Stage 2다. 그러나 고객명 비공개·납품 전·마진 전이므로 Green은 아니다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters contract / source-based customer anchor

stage3_price:
N/A

contract_value:
$4.3B

reported_customer:
Tesla, according to Reuters source

official_customer_disclosure:
not disclosed by LGES

contract_period:
2027-08 to 2030-07

extension_option:
up to 7 years

volume_increase_option:
true

production_site:
LGES U.S. factory

LFP_production_status:
LGES started LFP production at Michigan plant in May 2025

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = U.S._LFP_ESS_localization_watch
stage_failure_type = stage2_contract_not_green
```

---

## Case C — SK On / Flatiron Energy `success_candidate + EV-to-ESS redeployment`

```text
symbol = 096770 parent exposure
case_type = success_candidate
archetype = ESS_LFP_GRID_STORAGE / EV_TO_ESS_CAPACITY_REDEPLOYMENT
```

### stage date

```text
Stage 1:
2025
- EV slowdown
- SK On profitability pressure
- ESS pivot 필요성 증가

Stage 2:
2025-09-03
- SK On signs Flatiron Energy ESS supply deal
- up to 7.2GWh
- 2026~2030 supply period
- first SK On LFP ESS order
- some Georgia EV battery lines to be converted to ESS

Stage 3:
없음
- contract value not disclosed
- utilization / ESS OPM / FCF 확인 전 Green 금지

Stage 4B:
ESS pivot headline로 주가가 먼저 rerating되면 후보

Stage 4C:
Ford JV termination, EV line underutilization, LFP margin failure, debt/cash burn
```

SK On은 Flatiron Energy Development와 최대 7.2GWh 규모 LFP ESS battery supply deal을 체결했다. Reuters는 이 계약이 SK On의 첫 ESS용 LFP order이며, 2026~2030년 공급하고, 일부 Georgia EV battery line을 ESS용으로 전환할 계획이라고 보도했다. 계약금액은 공개되지 않았으므로 Stage 2다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters ESS contract anchor

stage3_price:
N/A

contract_volume:
up to 7.2GWh

supply_period:
2026~2030

battery_type:
LFP ESS

first_SK_On_LFP_ESS_order:
true

production_start:
2H 2026

capacity_redeployment:
some Georgia EV battery lines to ESS

contract_value:
not disclosed

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = SK_On_ESS_pivot_watch
stage_failure_type = stage2_watch_success_not_green
```

---

## Case D — LGES Ford / Freudenberg cancellations `hard 4C / contract quality break`

```text
symbol = 373220
case_type = 4C-thesis-break
archetype = EV_BATTERY_CONTRACT_QUALITY_BREAK
```

### stage date

```text
Stage 1:
2024~2025
- Ford Europe EV battery supply
- Freudenberg battery systems supply
- EV battery backlog headline

Stage 2:
약함
- contract headline 존재

Stage 3:
없음
- customer EV strategy / call-off / utilization / margin 확인 전 Green 금지

Stage 4C:
2025-12-17
- Ford cancels EV battery deal worth 9.6T won / $6.5B

Stage 4C 추가:
2025-12-26
- Freudenberg contract worth 3.9T won / $2.7B cancelled
- total expected revenue loss 13.5T won
- LGES 2024 revenue 25.62T won
```

LGES는 R3의 hard 4C 기준점이다. Ford는 EV 모델 축소와 수요 둔화를 이유로 LGES와의 9.6조 원, 65억 달러 규모 EV battery supply deal을 취소했다. 이후 Freudenberg Battery Power Systems도 battery business 철수로 3.9조 원, 27억 달러 계약을 취소했다. Reuters는 두 계약 취소로 LGES가 10일도 안 돼 약 13.5조 원의 기대매출을 잃었고, 이는 2024년 매출 25.62조 원의 절반을 넘는다고 보도했다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters contract-cancellation and event-return anchors

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

LGES_event_MAE_after_Ford_cancellation:
-7.6% intraday on Dec 18, 2025

KOSPI_same_context:
-1.4%

relative_underperformance:
-7.6 - (-1.4)
= -6.2pp

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- Ford cancellation 당일 hard 4C.
- Freudenberg cancellation은 hard 4C 강화.
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = battery_contract_quality_failure
stage_failure_type = hard_4C
```

---

## Case E — POSCO Holdings / MinRes lithium JV `success_candidate + lithium cycle watch`

```text
symbol = 005490
case_type = success_candidate + cyclical_watch
archetype = LITHIUM_RESOURCE_SECURITY
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
- POSCO gets indirect 15% interests in Wodgina and Mt Marion
- POSCO receives spodumene concentrate in proportion to JV stake
- MinRes shares +10.8%

Stage 3:
없음
- resource security는 Stage 2
- lithium hydroxide margin, offtake economics, downstream FCF 확인 전 Green 금지

Stage 4B:
lithium price rebound로 POSCO / 소재주가 먼저 움직이면 후보

Stage 4C:
lithium price 재하락, project write-down, demand slowdown, downstream margin failure
```

POSCO의 MinRes lithium JV는 R3/R4 경계의 Stage 2 후보다. POSCO는 7.65억 달러를 내고 Wodgina와 Mt Marion lithium mine에 각각 간접 15% 지분을 얻으며, JV 지분에 비례해 spodumene concentrate를 받을 수 있다. 그러나 Reuters는 spodumene 가격이 2022년 톤당 6,000달러 이상에서 2025년 6월 약 610달러까지 빠졌고, 이후 880달러로 반등했지만 여전히 고점 대비 크게 낮다고 보도했다. 즉 resource security는 좋지만 lithium cycle과 downstream margin을 통과해야 한다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters lithium transaction / commodity anchors

stage3_price:
N/A

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

POSCO_stock_OHLC:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate / cyclical_watch
rerating_result = lithium_resource_security_watch
stage_failure_type = stage2_watch_success_not_green
```

---

## Case F — Hanwha Qcells / Hanwha Solutions `4C-watch / solar customs disruption`

```text
symbol = 009830 / 000880 exposure
case_type = success_candidate + 4C-watch
archetype = SOLAR_US_SUPPLY_CHAIN_LOCALIZATION / SOLAR_CUSTOMS_UFLPA_4C_WATCH
```

### stage date

```text
Stage 1:
2024~2025
- U.S. solar localization
- IRA / domestic clean-energy manufacturing
- Qcells Georgia supply-chain buildout

Stage 2:
2024-08-08
- U.S. DOE conditional loan guarantee up to $1.45B
- Cartersville plant investment about $2.5B
- cells / ingots / wafers / panels
- nearly 2,000 jobs when fully operational

Stage 4C-watch:
2025-11-08
- U.S. customs detains components under forced-labor import law
- Qcells furloughs about 1,000 workers
- cuts about 300 staffing agency workers
- reduced hours at Georgia plants

Stage 3:
없음
- localization capex / loan guarantee만으로 Green 금지
- component flow, utilization, gross margin, FCF 확인 필요
```

Qcells는 미국 태양광 현지화 Stage 2 후보지만, 동시에 supply-chain 4C-watch다. U.S. DOE는 Qcells의 Georgia Cartersville plant에 최대 14.5억 달러 conditional loan guarantee를 제공하겠다고 밝혔고, 이 공장은 25억 달러 규모로 cells, ingots, wafers, panels를 생산해 미국 supply chain을 강화할 계획이었다. 그러나 2025년 11월에는 U.S. customs가 forced-labor import law와 관련해 overseas component shipments를 지연시키면서 Qcells가 약 1,000명을 furlough하고, staffing agency workers 약 300명을 감축했다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP solar-localization and customs-disruption anchors

stage3_price:
N/A

DOE_conditional_loan_guarantee:
up to $1.45B

Cartersville_facility_investment:
$2.5B according to Reuters
$2.3B according to AP context

facility_scope:
solar panels, cells, ingots, wafers

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

stock_OHLC:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + thesis_break_watch
rerating_result = solar_localization_watch_with_supply_chain_risk
stage_failure_type = stage2_watch_success_with_4C_watch
```

---

## Case G — Ford EV retreat supply-chain basket `4C-watch / demand shock`

```text
symbols = 373220 / 006400 / 003670 / 361610 / 450080
case_type = 4C-watch
archetype = BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK
```

### stage date

```text
Stage 1:
2025
- Ford EV strategy reset
- EV battery supply chain demand risk
- U.S. policy/subsidy shift

Stage 4C-watch:
2025-12-16
- Ford retreats from EV push
- LGES -6%
- Samsung SDI -3.5%
- POSCO Future M -8.2%

추가 4C-watch:
2025-12
- Ford cancels LGES contract
- SK On / Ford JV dissolution
- EV supply-chain volume risk 확산
```

Ford의 EV retreat는 R3 공급망 전체의 4C-watch다. Reuters는 Ford가 EV 모델을 중단한다는 발표 이후 LGES가 6%, Samsung SDI가 3.5%, cathode maker POSCO Future M이 8.2% 하락했다고 보도했다. 이는 EV demand shock이 특정 battery maker뿐 아니라 cathode, separator, precursor, recycling 등 소재 공급망 전체에 번질 수 있음을 보여준다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters event-return anchor

stage3_price:
N/A

LGES_event_MAE:
-6.0%

Samsung_SDI_event_MAE:
-3.5%

POSCO_Future_M_event_MAE:
-8.2%

Ford_context:
EV retreat / model cuts

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = EV_supply_chain_demand_shock
stage_failure_type = should_have_been_yellow_or_red
```

---

## Case H — Hyundai-LG Georgia battery plant raid `4C-watch / factory execution risk`

```text
listed_exposure = 005380 / 000270 / 373220
case_type = 4C-watch
archetype = EV_FACTORY_EXECUTION_LABOR_IMMIGRATION_RISK
```

### stage date

```text
Stage 1:
2024~2025
- U.S. EV / battery localization
- Hyundai Georgia EV site
- Hyundai-LG battery plant construction

Stage 2:
약한 Stage 2
- local production / IRA localization 기대

Stage 3:
없음
- factory construction만으로 Green 금지
- line start, utilization, local labor, visa stability, FCF 확인 필요

Stage 4C-watch:
2025-09
- U.S. immigration raid at Hyundai Georgia EV/battery site
- more than 300 Korean workers detained
- battery plant construction shut down temporarily
- skilled-worker visa policy risk

4C relief:
2025-11
- some workers returned
- construction resumed
- HL-GA Battery targets production in H1 2026
```

Hyundai-LG Georgia battery plant는 “미국 현지화”가 항상 매끄러운 Green이 아니라는 사례다. AP는 2025년 9월 Hyundai Georgia EV site의 battery plant 공사 현장에서 300명 넘는 한국인 근로자가 detained됐고, 이로 인해 battery plant work가 중단됐다고 보도했다. 이후 11월 일부 근로자가 돌아와 공사가 재개됐고, HL-GA Battery는 2026년 상반기 생산 개시를 목표로 한다고 밝혔다. 이건 hard 4C는 아니지만, 미국 현지 공장 건설에는 visa / skilled-worker / labor execution risk가 있다는 강한 4C-watch다. ([AP News][8])

### 실제 가격경로 검증

```text
price_data_source:
AP immigration-raid and restart anchors

stage3_price:
N/A

detained_workers:
over 300 Korean workers
AP later reports 330 detainees, 316 Koreans in one update

project:
Hyundai Georgia EV site / battery plant under construction

operator:
HL-GA Battery Co., Hyundai-LG joint venture

disruption:
construction shut down after raid

4C_relief:
some workers returned and construction resumed

production_target:
H1 2026

stock_OHLC:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = U.S._battery_factory_execution_watch
stage_failure_type = 4C_watch_not_hard_4C
```

---

# 5. 이번 R3 case별 요약표

| case                                | 분류                |                                                   실제 가격검증 | alignment              |
| ----------------------------------- | ----------------- | --------------------------------------------------------: | ---------------------- |
| Samsung SDI America LFP ESS         | success_candidate |                      >2T won / $1.36B, +6.1%, KOSPI -0.1% | Stage 2                |
| LGES / Tesla LFP ESS                | success_candidate |                 $4.3B, 2027~2030, extension up to 7 years | Stage 2                |
| SK On / Flatiron ESS                | success_candidate |                up to 7.2GWh, 2026~2030, value undisclosed | Stage 2                |
| LGES Ford/Freudenberg cancellations | hard 4C           | 13.5T won lost revenue, 52.7% of 2024 revenue; LGES -7.6% | contract break         |
| POSCO / MinRes lithium JV           | success_candidate |      $765M, indirect 15% Wodgina/Mt Marion, MinRes +10.8% | resource Stage 2       |
| Hanwha Qcells customs               | 4C-watch          |         $1.45B loan guarantee; 1,000 furloughs + 300 cuts | supply-chain watch     |
| Ford EV retreat basket              | 4C-watch          |         LGES -6%, Samsung SDI -3.5%, POSCO Future M -8.2% | demand shock           |
| Hyundai-LG Georgia raid             | 4C-watch          |   300+ workers detained, construction halted then resumed | factory execution risk |

---

# 6. score-price alignment 판정

```text
success_candidate:
- Samsung SDI America LFP ESS
- LGES / Tesla LFP ESS
- SK On / Flatiron ESS
- POSCO / MinRes lithium resource security

hard_4C:
- LGES Ford / Freudenberg contract cancellations

thesis_break_watch:
- Hanwha Qcells customs detention / furlough
- Ford EV retreat supply-chain shock
- Hyundai-LG Georgia battery plant raid

event_premium / 4B-watch:
- Samsung SDI +6.1% ESS event
- LGES Tesla-source contract if price moves before customer/disclosure and delivery
- POSCO lithium resource deal if lithium price rebound drives price before margin

price_moved_without_evidence:
- ESS/LFP theme rally without delivery or margin
- lithium-resource rally without downstream margin
- solar-localization rally without component-flow and utilization
```

---

# 7. 점수비중 교정

## 올릴 축

```text
binding_contract +5
GWh_volume +5
delivery_schedule +5
ESS_revenue_conversion +5
line_retrofit_execution +4
utilization_rate +5
OPM_visibility +5
FCF_after_capex +5
customer_quality +4
resource_security_with_offtake +4
```

### 왜 올리나

Samsung SDI와 SK On은 실제 GWh와 납기, line conversion이 있는 ESS Stage 2를 보여준다. LGES/Tesla도 U.S. LFP ESS localization 측면에서 강한 후보지만, 고객 비공개와 delivery 전이라는 약점이 있다. POSCO/MinRes는 resource security지만, lithium cycle과 downstream margin을 통과해야 한다.

## 내릴 축

```text
EV_capacity_announcement_only -5
ESS_theme_only -4
customer_name_without_calloff -5
contract_value_without_utilization -4
unofficial_customer_source_only -3
lithium_price_rebound_only -5
solar_localization_without_component_flow -5
factory_construction_without_labor_execution -4
subsidy_dependent_profit -5
EV_demand_shock -5
contract_cancellation -5
```

### 왜 내리나

LGES contract cancellations는 계약 headline이 actual revenue가 아니라는 점을 보여준다. Qcells는 현지화 투자가 있어도 customs detention 하나로 1,000명 furlough가 발생했다. Hyundai-LG Georgia case는 미국 현지화도 visa/labor execution risk를 통과해야 함을 보여준다.

## Green gate 강화 조건

```text
R3 Stage 3-Green 필수:
1. binding contract
2. customer / GWh / supply period 확인
3. actual delivery 또는 revenue recognition 시작
4. utilization improvement
5. OPM 또는 gross margin 확인
6. FCF after capex 확인
7. subsidy 제외 이익 품질 확인
8. customer EV strategy / ESS demand risk 통과
9. supply-chain / customs / labor execution risk 통과
10. price path follows evidence

금지:
EV capacity announcement만 있음
ESS/LFP theme만 있음
고객명만 있음
비공식 고객 보도만 있음
공장 건설만 있음
리튬 resource headline만 있음
태양광 현지화 headline만 있음
보조금 제외 적자
```

## 4B 조기감지 조건

```text
4B-watch:
ESS/LFP 계약 발표만으로 주가 급등
EV line conversion headline으로 valuation 확장
고객명 비공식 보도만으로 급등
리튬 resource security 뉴스로 price가 먼저 움직임
solar localization 기대가 utilization보다 먼저 반영
battery factory ownership / construction이 utilization보다 먼저 valuation에 반영

4B-elevated:
EV 수요 둔화에도 CAPEX valuation 유지
고객 주문 확인 없이 공장·JV 기대만 반영
리튬 가격 반등이 재고평가 이익으로만 연결
customs/labor/visa risk가 무시됨
```

## 4C hard gate 조건

```text
contract cancellation
contract value collapse
customer EV model cancellation
customer strategy pullback
GWh call-off failure
utilization delay
factory restart uncertainty
negative FCF
JV termination / ownership transfer under weak demand
subsidy-quality profit collapse
supply-chain customs detention
production furlough
immigration / skilled-worker execution failure
```

이번 R3 Loop 11에서 확정 hard 4C는 **LGES Ford/Freudenberg contract cancellations**다. Qcells customs detention과 Hyundai-LG Georgia raid는 hard 4C가 아니라 강한 4C-watch다.

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

## docs/round/round_174.md 요약

```md
# R3 Loop 11. Battery / EV / Green Price Validation

이번 라운드는 R3 Loop 11 price-validation 라운드다.

핵심 결론:
- Samsung SDI America is an ESS LFP Stage 2 success_candidate. It signed a >2T won / $1.36B LFP ESS contract with an unnamed U.S. energy infrastructure company, deliveries starting 2027 for three years, and shares rose +6.1% vs KOSPI -0.1%.
- LGES / Tesla LFP ESS is Stage 2. Reuters source says customer is Tesla for a $4.3B LFP supply contract from August 2027 to July 2030, with extension up to seven years and volume increase option. Customer identity was not officially disclosed.
- SK On / Flatiron is Stage 2. Up to 7.2GWh LFP ESS supply from 2026 to 2030, first LFP ESS order, with some Georgia EV lines converted to ESS. Contract value undisclosed.
- LGES Ford / Freudenberg cancellations are hard 4C. Ford cancelled a 9.6T won / $6.5B EV battery deal, Freudenberg cancelled 3.9T won / $2.7B, causing 13.5T won expected revenue loss, 52.7% of LGES 2024 revenue. LGES fell as much as -7.6% after Ford cancellation.
- POSCO / MinRes lithium JV is resource-security Stage 2. POSCO pays $765M for indirect 15% stakes in Wodgina and Mt Marion; MinRes shares +10.8%. Lithium cycle remains the main RedTeam.
- Hanwha Qcells is solar localization Stage 2 plus 4C-watch. U.S. DOE conditional loan guarantee up to $1.45B for a $2.5B Georgia plant, but customs delays forced about 1,000 furloughs and 300 staffing-worker cuts.
- Ford EV retreat is supply-chain 4C-watch. LGES -6%, Samsung SDI -3.5%, POSCO Future M -8.2%.
- Hyundai-LG Georgia battery plant raid is factory-execution 4C-watch. More than 300 Korean workers were detained, construction shut down, then some workers returned and production target remains H1 2026.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 174 R3 Loop 11 Battery EV Green Price Validation

## 반영 내용
- R3 Loop 11 price-validation 라운드를 추가했다.
- ESS LFP contracts, EV-to-ESS capacity redeployment, LGES contract cancellations, lithium resource security, U.S. solar localization, EV supply-chain demand shock, U.S. battery factory execution risk를 비교했다.
- Reuters/AP anchors로 가능한 MFE/MAE 및 contract/factory/commodity metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- binding contract, GWh volume, delivery schedule, ESS revenue conversion, line retrofit execution, utilization, OPM/FCF 가중치 강화
- ESS theme-only, unofficial customer source-only, lithium rebound-only, solar localization without component flow, factory construction without labor execution, contract cancellation 감점 강화
- LGES contract cancellation hard 4C 추가
```

## case row 초안

```jsonl
{"case_id":"r3_loop11_samsung_sdi_lfp_ess_us_contract","symbol":"006400","company_name":"Samsung SDI","case_type":"success_candidate","primary_archetype":"ESS_LFP_GRID_STORAGE","stage2_date":"2025-12-09","stage4b_date":"2025-12-09_watch","price_validation":{"price_data_source":"Reuters contract/event-return anchor","stage3_price":null,"contract_value_krw_trn":2.0,"contract_value_usd_bn":1.36,"delivery_start_year":2027,"contract_duration_years":3,"customer":"unnamed U.S. energy infrastructure development and operations company","battery_type":"prismatic LFP ESS batteries","production_method":"retrofitting existing U.S. plant lines","event_mfe_1d_pct":6.1,"kospi_same_context_pct":-0.1,"relative_outperformance_pp":6.2,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"ESS_LFP_contract_watch","notes":"Strong ESS Stage 2; customer, delivery, utilization, OPM and FCF must confirm before Green."}
{"case_id":"r3_loop11_lges_tesla_lfp_ess_contract","symbol":"373220","company_name":"LG Energy Solution","case_type":"success_candidate","primary_archetype":"ESS_LFP_GRID_STORAGE","stage2_date":"2025-07-30","price_validation":{"price_data_source":"Reuters source-based contract anchor","stage3_price":null,"contract_value_usd_bn":4.3,"reported_customer":"Tesla according to Reuters source","official_customer_disclosure":"not disclosed by LGES","contract_period":"2027-08_to_2030-07","extension_option_years":7,"volume_increase_option":true,"production_site":"LGES U.S. factory","lfp_production_status":"Michigan plant started LFP production in May 2025","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"U.S._LFP_ESS_localization_watch","notes":"Strong ESS/localization Stage 2; official customer disclosure, delivery, utilization and margin required before Green."}
{"case_id":"r3_loop11_skon_flatiron_lfp_ess","symbol":"096770_parent_exposure","company_name":"SK On / SK Innovation exposure","case_type":"success_candidate","primary_archetype":"ESS_LFP_GRID_STORAGE","stage2_date":"2025-09-03","price_validation":{"price_data_source":"Reuters ESS contract anchor","stage3_price":null,"contract_volume_gwh":7.2,"supply_period":"2026-2030","battery_type":"LFP ESS","first_sk_on_lfp_ess_order":true,"production_start":"2H_2026","capacity_redeployment":"some Georgia EV battery lines converted to ESS","contract_value":"not_disclosed","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"SK_On_ESS_pivot_watch","notes":"ESS pivot is Stage 2; contract value, utilization, OPM and FCF required before Green."}
{"case_id":"r3_loop11_lges_ford_freudenberg_contract_hard_4c","symbol":"373220","company_name":"LG Energy Solution","case_type":"4c_thesis_break","primary_archetype":"EV_BATTERY_CONTRACT_QUALITY_BREAK","stage4c_date":"2025-12-17/2025-12-26","price_validation":{"price_data_source":"Reuters contract cancellation and event-return anchors","stage3_price":null,"ford_cancelled_contract_krw_trn":9.6,"ford_cancelled_contract_usd_bn":6.5,"freudenberg_cancelled_contract_krw_trn":3.9,"freudenberg_cancelled_contract_usd_bn":2.7,"total_lost_expected_revenue_krw_trn":13.5,"lges_2024_revenue_krw_trn":25.62,"lost_revenue_vs_2024_revenue_pct":52.7,"lges_event_mae_after_ford_pct":-7.6,"kospi_same_context_pct":-1.4,"relative_underperformance_pp":-6.2,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"battery_contract_quality_failure","notes":"Ford/Freudenberg cancellations are hard 4C; contract headline cannot be Green without actual call-off and utilization."}
{"case_id":"r3_loop11_posco_minres_lithium_resource_security","symbol":"005490","company_name":"POSCO Holdings / MinRes lithium JV","case_type":"success_candidate","primary_archetype":"LITHIUM_RESOURCE_SECURITY","stage2_date":"2025-11-11","price_validation":{"price_data_source":"Reuters lithium transaction/commodity anchors","stage3_price":null,"transaction_value_usd_mn":765,"posco_indirect_stake_pct":15,"assets":["Wodgina","Mt Marion"],"minres_event_mfe_pct":10.8,"spodumene_peak_2022_usd_per_t":6000,"spodumene_low_2025_usd_per_t":610,"spodumene_drawdown_peak_to_low_pct":-89.8,"spodumene_rebound_610_to_880_pct":44.3,"spodumene_880_vs_peak_pct":-85.3,"price_validation_status":"posco_stock_ohlc_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_cyclical_watch","rerating_result":"lithium_resource_security_watch","notes":"Resource security is Stage 2; downstream margin, offtake economics and FCF required before Green."}
{"case_id":"r3_loop11_hanwha_qcells_customs_supply_chain_4c_watch","symbol":"009830/000880_exposure","company_name":"Hanwha Qcells / Hanwha Solutions exposure","case_type":"4c_watch","primary_archetype":"SOLAR_US_SUPPLY_CHAIN_LOCALIZATION","stage2_date":"2024-08-08","stage4c_date":"2025-11-08","price_validation":{"price_data_source":"Reuters/AP solar localization and customs-disruption anchors","stage3_price":null,"doe_conditional_loan_guarantee_usd_bn":1.45,"cartersville_facility_investment_usd_bn":"2.3-2.5","facility_scope":["solar panels","cells","ingots","wafers"],"jobs_when_fully_operational":2000,"furloughed_or_reduced_hours_workers":1000,"contract_workers_cut":300,"affected_direct_workers_total":1300,"cause":"U.S. customs detentions under forced-labor import law / UFLPA context","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_thesis_break_watch","rerating_result":"solar_localization_watch_with_supply_chain_risk","notes":"Solar localization is Stage 2; customs/component disruption and furloughs create 4C-watch."}
{"case_id":"r3_loop11_ford_ev_retreat_supply_chain_shock","symbol":"373220/006400/003670/361610/450080","company_name":"LGES / Samsung SDI / POSCO Future M / SKIET / EcoPro Materials basket","case_type":"4c_watch","primary_archetype":"BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK","stage4c_date":"2025-12-16","price_validation":{"price_data_source":"Reuters event-return anchor","stage3_price":null,"lges_event_mae_pct":-6.0,"samsung_sdi_event_mae_pct":-3.5,"posco_future_m_event_mae_pct":-8.2,"ford_context":"EV retreat / model cuts","price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"EV_supply_chain_demand_shock","notes":"Ford EV retreat shows demand shock across Korean battery/cathode supply chain."}
{"case_id":"r3_loop11_hyundai_lg_georgia_battery_raid_execution_watch","symbol":"005380/000270/373220","company_name":"Hyundai-LG Georgia battery plant / HL-GA Battery","case_type":"4c_watch","primary_archetype":"EV_FACTORY_EXECUTION_LABOR_IMMIGRATION_RISK","stage4c_date":"2025-09","price_validation":{"price_data_source":"AP immigration raid and restart anchors","stage3_price":null,"detained_workers":"over_300_Korean_workers; AP_update_330_detainees_316_Koreans","project":"Hyundai Georgia EV site / battery plant under construction","operator":"HL-GA Battery Co., Hyundai-LG joint venture","disruption":"construction shut down after raid","relief":"some workers returned and construction resumed","production_target":"H1_2026","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"U.S._battery_factory_execution_watch","notes":"U.S. localization requires visa/skilled-worker/labor execution; construction alone is not Green."}
```

## shadow weight row 초안

```csv
archetype,binding_contract,gwh_volume,delivery_schedule,ess_revenue_conversion,line_retrofit_execution,utilization,opm_fcf,customer_quality,event_penalty,execution_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
ESS_LFP_GRID_STORAGE,+5,+5,+5,+5,+4,+5,+5,+4,-2,+2,+4,+4,Samsung SDI/LGES/SK On ESS contracts are Stage 2 until delivery/utilization/margin/FCF confirm.
EV_TO_ESS_CAPACITY_REDEPLOYMENT,+4,+5,+5,+5,+5,+5,+5,+3,-3,+4,+4,+5,EV line conversion is positive only if utilization and ESS margins confirm.
US_BATTERY_LOCALIZATION,+4,+4,+4,+4,+5,+5,+5,+4,-3,+5,+4,+5,U.S. localization must pass customs/visa/labor execution risks.
EV_BATTERY_CONTRACT_QUALITY_BREAK,+0,+0,+0,+0,+0,+0,+0,+0,0,+5,+3,+5,LGES Ford/Freudenberg cancellations are hard 4C.
LITHIUM_RESOURCE_SECURITY,+3,+3,+3,+2,+0,+3,+5,+3,-4,+2,+4,+4,POSCO/MinRes is Stage 2; lithium cycle and downstream margin matter.
SOLAR_US_SUPPLY_CHAIN_LOCALIZATION,+3,+3,+4,+3,+4,+5,+5,+4,-4,+5,+4,+5,Qcells localization is blocked by customs/component flow risk.
BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK,+0,+0,+0,+0,+0,+0,+0,+0,0,+5,+3,+5,Ford EV retreat is 4C-watch for Korean battery/cathode supply chain.
EV_FACTORY_EXECUTION_LABOR_IMMIGRATION_RISK,+0,+0,+0,+0,+3,+3,+3,+2,0,+5,+4,+5,Georgia raid shows U.S. plant execution risk beyond capex headline.
```

---

# 이번 R3 Loop 11 결론

R3는 **ESS 전환이라는 진짜 Stage 2 후보가 늘고 있지만, 아직 Stage 3는 매우 보수적으로 줘야 하는 섹터**다.

```text
1. Samsung SDI America LFP ESS는 좋은 Stage 2다.
   계약금액, 납기, line retrofit이 있지만 delivery·utilization·OPM/FCF 전 Green은 아니다.

2. LGES/Tesla LFP ESS도 강한 Stage 2다.
   그러나 고객 비공식 source, 납품 전, 마진 전이라는 약점이 있다.

3. SK On/Flatiron은 EV-to-ESS 전환의 좋은 후보지만,
   계약금액 비공개와 가동률 확인 전 Stage 3는 아니다.

4. LGES Ford/Freudenberg cancellations는 hard 4C다.
   13.5T won expected revenue loss는 계약 headline의 취약성을 보여준다.

5. POSCO/MinRes lithium JV는 resource-security Stage 2다.
   하지만 lithium 가격 cycle과 downstream margin을 통과해야 한다.

6. Hanwha Qcells는 U.S. solar localization 후보지만,
   customs detention과 furlough가 4C-watch다.

7. Ford EV retreat는 battery/cathode supply chain 전체의 demand 4C-watch다.

8. Hyundai-LG Georgia raid는 U.S. localization도 visa/labor execution risk를 통과해야 함을 보여준다.
```

한 문장으로 압축하면:

> **R3에서 진짜 Stage 3는 “ESS·LFP·리튬·태양광 현지화가 좋다”가 아니라, binding contract가 GWh·delivery·utilization·OPM·FCF로 닫히고 EV 수요·customs·labor·계약취소 리스크를 통과하는 순간이다.**

[1]: https://www.reuters.com/world/asia-pacific/samsung-sdis-us-unit-signs-14-bln-lfp-battery-deal-us-customer-2025-12-09/?utm_source=chatgpt.com "Samsung SDI unit signs US battery deal worth over $1.36 bln for energy storage systems"
[2]: https://www.reuters.com/business/energy/lg-energy-solution-tesla-sign-43-billion-battery-supply-deal-source-says-2025-07-30/?utm_source=chatgpt.com "LG Energy Solution, Tesla sign $4.3 billion battery supply deal, source says"
[3]: https://www.reuters.com/business/energy/south-koreas-sk-signs-energy-storage-battery-supply-deal-with-flatiron-energy-2025-09-03/?utm_source=chatgpt.com "South Korea's SK On signs energy storage battery supply deal with Flatiron Energy"
[4]: https://www.reuters.com/business/finance/south-koreas-lg-energy-solution-ends-65-billion-ev-battery-supply-deal-with-ford-2025-12-17/?utm_source=chatgpt.com "Ford cancels EV battery deal worth $6.5 billion with South Korea's LG Energy Solution"
[5]: https://www.reuters.com/business/energy/australias-minres-sell-30-lithium-jv-stake-posco-765-mln-2025-11-11/?utm_source=chatgpt.com "Australia's MinRes inks $765 million deal with POSCO for lithium JV stake, shares surge"
[6]: https://www.reuters.com/business/energy/us-offers-15-bln-conditional-loan-guarantee-qcells-solar-facility-georgia-2024-08-08/?utm_source=chatgpt.com "US offers $1.5 bln conditional loan guarantee to Qcells for solar facility in Georgia"
[7]: https://www.reuters.com/world/asia-pacific/shares-lg-energy-solution-fall-6-after-ford-retreats-ev-push-2025-12-16/?utm_source=chatgpt.com "Shares of LG Energy Solution fall 6% after Ford retreats from EV push"
[8]: https://apnews.com/article/25f04d539eb2556f3ff2fad49db0f74e?utm_source=chatgpt.com "South Korea says detained Korean workers released from Georgia facility before flight home"
