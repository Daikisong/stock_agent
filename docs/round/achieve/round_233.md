순서상 이번은 **R3 Loop 10 — 2차전지·전기차·친환경 가격경로 검증 라운드**다.

이번 R3 Loop 10은 **EV 둔화 → ESS 전환**, **JV 재편**, **소재 공급망 재구성**, **리튬 이벤트**, **태양광 현지화**, **수소 CAPEX**를 같이 본다. R3의 기본값은 Green이 아니라 **Stage 2 / Watch / 4B / 4C**다.

```text
round = R3 Loop 10
round_id = round_161
large_sector = BATTERY_EV_GREEN
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
```

이번 환경에서는 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC를 안정적으로 직접 확보하지 못했다. 대신 Reuters / AP / MarketWatch / WSJ가 제공한 **이벤트 수익률, 계약 GWh, 투자금액, 공장 가동·해고·JV 재편·원자재 가격 지표**로 계산 가능한 값만 계산했다. 원시 OHLC가 없는 구간은 `price_data_unavailable_after_deep_search`로 표시했다.

---

# 1. 이번 라운드 대섹터

```text
R3 = 2차전지·전기차·친환경
```

R3의 핵심은 “배터리·ESS·친환경 수혜”가 아니라, **계약이 actual call-off·GWh·가동률·OPM·FCF로 내려오는가**다. 특히 2025~2026년 R3는 EV 둔화와 ESS 전환이 동시에 나타난다.

---

# 2. 대상 canonical archetype

```text
ESS_LFP_GRID_STORAGE
EV_TO_ESS_CAPACITY_REDEPLOYMENT
EV_BATTERY_JV_RESTRUCTURING
EV_BATTERY_FACTORY_UTILIZATION_4C
BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE
CATHODE_SUPPLY_CHAIN_DERISKING
BATTERY_MATERIALS_CYCLE_OVERLAY
LITHIUM_CYCLE_EVENT_PREMIUM
SOLAR_US_SUPPLY_CHAIN_LOCALIZATION
SOLAR_CUSTOMS_UFLPA_4C_WATCH
HYDROGEN_FUEL_CELL_CAPEX
PRICE_ONLY_RALLY
EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
ESS 전환:
- LG Energy Solution
- SK On
- LFP ESS
- EV line conversion
- Hanwha QCells / Flatiron Energy
- data-center / grid storage demand
- delivery starts 2026~2030
- utilization / OPM / FCF before Green

EV battery JV 재편:
- LGES / Stellantis NextStar
- LGES / GM Michigan / Ohio / Tennessee
- SK On / Ford BlueOval SK
- Samsung SDI / GM Indiana
- EV demand slowdown
- tax credit expiration
- factory utilization / layoffs

소재 공급망:
- LG Chem / Toyota Tsusho cathode plant
- Huayou stake reduction
- China exposure reduction
- cathode localization
- offtake and margin before Green

태양광:
- Hanwha Solutions / Qcells
- U.S. solar localization
- UFLPA customs detention
- Georgia furloughs
- component supply risk

소재 cycle:
- POSCO Future M
- L&F
- lithium price rally
- CATL Yichun mine license event
- commodity event premium vs structural margin

수소:
- Hyundai hydrogen fuel-cell plant
- fuel cells / electrolyzers
- completion 2027
- utilization / order book / FCF before Green
```

---

# 4. 국장 신규 후보 case

## Case A — LG에너지솔루션 `success_candidate + EV-to-ESS restructuring watch`

```text
symbol = 373220
case_type = success_candidate + restructuring_watch
archetype = ESS_LFP_GRID_STORAGE / EV_TO_ESS_CAPACITY_REDEPLOYMENT
```

### stage date

```text
Stage 1:
2025
- EV demand slowdown
- U.S. tax credit expiration
- battery JV restructuring
- ESS as growth hedge

Stage 2:
2026-02-04
- Hanwha QCells USA와 5GWh ESS battery supply contract
- LFP cells
- supply period 2028~2030
- Holland, Michigan plant production

추가 Stage 2:
2026-02-06
- LGES buys Stellantis’ 49% NextStar stake for nominal $100
- NextStar to focus on ESS batteries
- more than C$5B invested to date

추가 Stage 2 / 4C-watch:
2026-05-12
- GM-LG Ohio Ultium restart date uncertain
- around 850 workers laid off since January
- Tennessee workers recalled for ESS cells instead of EV cells

Stage 3:
보류
- ESS 계약은 강한 Stage 2
- 하지만 ESS 매출, utilization, OPM, FCF 확인 전 Green 금지

Stage 4B:
ESS 전환 기대만으로 multiple이 먼저 확장되면 후보

Stage 4C:
EV 공장 utilization failure, 추가 JV 재편, tax credit 종료 후 수요 부진, ESS margin failure 시 후보
```

LGES는 R3에서 “EV 둔화 이후 ESS 전환”의 대표 후보가 됐다. Hanwha QCells USA에 2028~2030년 5GWh 규모 LFP ESS battery를 공급하기로 했고, Stellantis와의 캐나다 NextStar JV에서는 Stellantis의 49% 지분을 명목상 100달러에 인수해 ESS 중심 운영으로 전환하겠다고 밝혔다. 동시에 GM-LG Ohio battery plant는 2026년 5월 기준 full restart 일정이 불확실하고, 약 850명 layoff 이후 일부만 복귀하는 상황이라 EV factory utilization 4C-watch도 같이 붙는다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported ESS/JV/restart anchors

stage3_price:
N/A

Hanwha_QCells_ESS_contract:
5GWh

supply_period:
2028~2030

cell_chemistry:
LFP

production_site:
Holland, Michigan

NextStar_stake_acquired:
49%

NextStar_purchase_price:
$100 nominal

NextStar_investment_to_date:
> C$5B / about $3.65B

Ohio_Ultium_layoffs_since_January:
about 850 workers

Ohio_Ultium_prior_employee_context:
about 1,330 before halt

indefinite_layoff_context:
another 480 workers

ESS_redeployment:
Tennessee plant workers recalled to produce ESS cells

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate + 4C_watch
rerating_result = ESS_pivot_watch_with_EV_utilization_risk
stage_failure_type = stage2_watch_success
```

---

## Case B — SK On / SK이노베이션 `success_candidate + failed_rerating_watch`

```text
symbol = 096770
case_type = success_candidate + failed_rerating_watch
archetype = ESS_LFP_GRID_STORAGE / EV_BATTERY_JV_RESTRUCTURING
```

### stage date

```text
Stage 1:
2024~2025
- EV demand slowdown
- SK On profitability pressure
- ESS pivot 필요성 증가

Stage 2:
2025-09-03
- Flatiron Energy와 ESS LFP battery supply deal
- up to 7.2GWh
- supply period 2026~2030
- SK On’s first LFP ESS order
- Georgia EV battery lines partly converted for ESS

Stage 3:
없음
- value not disclosed
- ESS revenue / utilization / OPM / FCF 확인 필요

Stage 4B:
ESS pivot headline만으로 주가가 먼저 급등하면 후보

Stage 4C:
Ford JV dissolution, EV order slowdown, loss persistence, utilization failure 시 후보
```

SK On은 Flatiron Energy Development에 2026~2030년 최대 7.2GWh LFP ESS battery를 공급하기로 했다. 이건 SK On의 첫 ESS용 LFP order이고, 기존 Georgia EV battery line 일부를 ESS용으로 전환하는 계획이 포함된다. 다만 계약금액은 공개되지 않았고, EV 수요 둔화에 대응하는 구조라서 Stage 3가 아니라 Stage 2다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported ESS contract anchor

stage3_price:
N/A

Flatiron_ESS_contract_volume:
up to 7.2GWh

supply_period:
2026~2030

chemistry:
LFP

first_SK_On_LFP_ESS_order:
true

production_plan:
mass production in 2H 2026

capacity_redeployment:
some Georgia EV battery lines to be converted for ESS use

contract_value:
not disclosed

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = SK_On_ESS_pivot_watch
stage_failure_type = stage2_watch_success_not_green
```

---

## Case C — 삼성SDI `success_candidate + EV-demand delay watch`

```text
symbol = 006400
case_type = success_candidate + 4C-watch
archetype = EV_BATTERY_JV_CAPEX / EV_DEMAND_DELAY_OVERLAY
```

### stage date

```text
Stage 1:
2023~2024
- GM / Samsung SDI U.S. battery JV
- North America EV battery localization

Stage 2:
2024-08-28
- Samsung SDI and GM finalize Indiana battery JV
- investment about $3.5B
- initial capacity 27GWh
- possible expansion to 36GWh
- mass production target 2027
- Samsung SDI shares +3.2%, KOSPI -0.3%

Stage 3:
없음
- JV finalization만으로 Green 금지
- GM EV demand, plant utilization, cell margin, FCF 확인 필요

Stage 4B:
U.S. localization / IRA / EV capacity narrative로 가격이 먼저 확장되면 후보

Stage 4C-watch:
- mass production moved to 2027 vs earlier 2026 plan
- GM cut 2024 EV production forecast upper end from 300k to 250k
```

삼성SDI는 GM과 Indiana EV battery JV를 확정했고, 약 35억 달러 투자, 초기 27GWh capacity, 36GWh 확장 가능성, 2027년 mass production 목표가 제시됐다. 발표 당시 삼성SDI 주가는 3.2% 올랐고 KOSPI는 0.3% 하락했다. 그러나 GM은 2024년 EV 생산 전망 상단을 300,000대에서 250,000대로 낮췄고, 당초 2026년으로 예상됐던 생산 시작도 2027년으로 밀린 구조라 Stage 3는 보류한다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported JV and event-return anchors

stage3_price:
N/A

JV_investment:
$3.5B

initial_capacity:
27GWh

potential_capacity:
36GWh

capacity_expansion_potential:
36 / 27 - 1
= +33.3%

mass_production_target:
2027

Samsung_SDI_event_MFE:
+3.2%

KOSPI_same_context:
-0.3%

relative_outperformance:
3.2 - (-0.3)
= +3.5pp

GM_2024_EV_production_forecast_upper_before:
300,000 units

GM_2024_EV_production_forecast_upper_after:
250,000 units

forecast_cut:
250,000 / 300,000 - 1
= -16.7%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + demand_watch
rerating_result = EV_battery_localization_watch
stage_failure_type = stage2_watch_success
```

---

## Case D — LG화학 / Toyota Tsusho cathode plant `success_candidate / China-exposure derisking`

```text
symbol = 051910
case_type = success_candidate
archetype = CATHODE_SUPPLY_CHAIN_DERISKING
```

### stage date

```text
Stage 1:
2025
- cathode supply-chain derisking
- Japan/Korea collaboration
- China JV exposure reduction

Stage 2:
2025-09-09
- Toyota Tsusho acquires 25% stake in LG Chem’s South Korea cathode plant
- becomes second-largest shareholder
- Huayou Cobalt stake reduced from 49% to 24%

Stage 3:
없음
- ownership derisking만으로 Green 금지
- cathode volume, customer offtake, OPM, FCF 확인 필요

Stage 4B:
China-exposure derisking narrative로 가격이 먼저 움직이면 후보

Stage 4C:
cathode demand slowdown, customer call-off failure, lithium/nickel price reversal, utilization failure 시 후보
```

LG Chem의 한국 cathode material plant에 Toyota Tsusho가 25% 지분을 취득하면서 두 번째로 큰 주주가 됐고, 중국 Huayou Cobalt의 지분은 49%에서 24%로 낮아졌다. 이건 R3에서 의미 있는 supply-chain derisking Stage 2지만, cathode volume·offtake·OPM·FCF로 내려오기 전 Stage 3는 아니다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters ownership-structure anchor

stage3_price:
N/A

Toyota_Tsusho_stake:
25%

Huayou_Cobalt_stake_before:
49%

Huayou_Cobalt_stake_after:
24%

Huayou_stake_reduction_absolute:
49 - 24
= -25pp

Huayou_stake_reduction_relative:
24 / 49 - 1
= -51.0%

company_stock_OHLC:
price_data_unavailable_after_deep_search

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = cathode_supply_chain_derisking_watch
stage_failure_type = stage2_evidence_not_green
```

---

## Case E — Hanwha Solutions / Qcells `success_candidate + supply-chain 4C-watch`

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
- Qcells Georgia full solar supply-chain buildout
- IRA / tariff protection 기대

Stage 2:
2025
- Qcells continues U.S. supply-chain investment
- Cartersville facility about $2.3B

Stage 3:
없음
- U.S. localization만으로 Green 금지
- component flow, utilization, gross margin, FCF 확인 필요

Stage 4C-watch:
2025-11
- U.S. Customs detains imported components under forced-labor law
- Qcells reduces pay/hours for about 1,000 of 3,000 Georgia employees
- lays off 300 contract workers
```

Qcells는 미국 Georgia에서 full solar supply chain을 구축하는 Stage 2 후보지만, 2025년 U.S. Customs가 forced-labor import law 관련 부품을 억류하면서 약 1,000명의 Georgia 직원 근무시간·임금을 줄이고 300명의 contract workers를 해고했다. Qcells는 supply-chain transparency를 주장하고 정상화를 예상했지만, R3에서는 이것을 **solar localization 4C-watch**로 둔다. ([AP News][5])

### 실제 가격경로 검증

```text
price_data_source:
AP supply-chain disruption anchor

stage3_price:
N/A

Qcells_Georgia_employee_context:
about 3,000 employees

furloughed_or_reduced_pay_hours:
about 1,000 employees

contract_workers_laid_off:
300

affected_direct_workers_total:
1,300

affected_share_of_employee_context:
1,000 / 3,000
= 33.3% for employee furlough/pay-hour reduction only

Cartersville_facility_investment:
about $2.3B

cause:
U.S. Customs detentions under forced-labor import law

company_stock_OHLC:
price_data_unavailable_after_deep_search

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + thesis_break_watch
rerating_result = solar_localization_watch_with_supply_chain_risk
stage_failure_type = stage2_watch_success_with_4C_watch
```

---

## Case F — SKIET / EcoPro Materials / EV supply chain `4C-watch / EV-demand shock`

```text
symbols = 361610 / 450080 / battery-supply-chain basket
case_type = 4C-watch
archetype = SEPARATOR_EV_DEMAND_CYCLE / PRECURSOR_SUPPLY_CHAIN_SHOCK
```

### stage date

```text
Stage 1:
2023~2024
- separator / precursor / battery supply-chain vertical integration theme
- Ford / Korean battery exposure

Stage 2:
없음 또는 약함
- customer shipment / utilization / OPM 확인 전 Green 금지

Stage 3:
없음

Stage 4B:
EV 소재·분리막 theme overheat 구간 후보

Stage 4C-watch:
2025-12
- Ford takes about $20B charge and pivots away from full EV intensity
- Korean battery supply-chain stocks hit:
  SK Innovation -3%
  LGES -6%
  SK IE Technology -5%
  EcoPro Materials -5%
```

Ford의 EV 전략 후퇴와 hybrid 전환은 한국 배터리 공급망에 직접적인 4C-watch를 만들었다. MarketWatch는 Ford가 약 200억 달러 charge를 인식하는 가운데 SK Innovation, LGES, SK IE Technology, EcoPro Materials가 각각 3~6% 하락했다고 보도했고, Citi는 F-150 Lightning 중단과 lower-battery-content hybrid 전환이 한국 배터리 공급망에 부정적이라고 봤다. ([마켓워치][6])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch reported event-return anchors

stage3_price:
N/A

Ford_charge:
about $20B

SK_Innovation_event_MAE:
-3.0%

LGES_event_MAE:
-6.0%

SK_IE_Technology_event_MAE:
-5.0%

EcoPro_Materials_event_MAE:
-5.0%

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
score_price_alignment = thesis_break_watch
rerating_result = EV_supply_chain_demand_shock
stage_failure_type = should_have_been_red_or_watch
```

---

## Case G — POSCO Future M / L&F lithium event `cyclical_success / commodity event premium`

```text
symbols = 003670 / 066970
case_type = cyclical_success / event_premium
archetype = LITHIUM_CYCLE_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-08-11
- CATL Yichun lithium mine license expiry
- production suspension
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

CATL이 Yichun lithium mine license 만료로 채굴을 중단하면서 lithium carbonate futures가 8% 급등했다. WSJ는 South Korean battery-material suppliers인 POSCO Future M과 L&F가 각각 8.3%, 10% 상승했고, Samsung SDI와 LGES도 3.2%, 2.8% 올랐다고 보도했다. 하지만 CATL은 license가 갱신되면 생산 재개가 가능하다고 밝혔고, lithium 가격은 2022년 고점 대비 최대 90% 하락한 상태였으므로 구조적 Stage 3가 아니라 **commodity event premium**이다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ commodity and event-return anchors

stage3_price:
N/A

lithium_carbonate_futures_event_return:
+8%

POSCO_Future_M_event_MFE:
+8.3%

L&F_event_MFE:
+10.0%

Samsung_SDI_event_MFE:
+3.2%

LGES_event_MFE:
+2.8%

lithium_price_decline_from_2022_peak:
up to -90%

CATL_statement:
production resumes if license renewed

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = cyclical_success / event_premium
rerating_result = lithium_price_event_watch
stage_failure_type = should_not_be_green
```

---

## Case H — 현대차 수소연료전지 plant `success_candidate / hydrogen capex Stage 2`

```text
symbol = 005380
case_type = success_candidate
archetype = HYDROGEN_FUEL_CELL_CAPEX
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

현대차는 울산에 9,300억 원, 약 6.54억 달러 규모 hydrogen fuel-cell 생산시설을 착공했다. 이 시설은 승용차, 상용 트럭·버스, 건설장비, 선박, electrolyzer 용도를 겨냥하며 2027년 완공 예정이다. 하지만 R3에서는 CAPEX 발표가 아니라 **가동률·주문·마진·FCF**가 Stage 3 조건이다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters capex/facility evidence

stage3_price:
N/A

stock_OHLC:
price_data_unavailable_after_deep_search

reason:
- Reuters는 현대차 주가 reaction anchor를 제공하지 않음.
- KRX / Naver / Yahoo / Stooq 원시 수정주가 일봉 OHLC 직접 확보 실패.

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
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = hydrogen_fuel_cell_capex_watch
stage_failure_type = stage2_watch_success
```

---

# 5. 이번 R3 case별 요약표

| case                     | 분류                                  |                                                                실제 가격검증 | alignment                        |
| ------------------------ | ----------------------------------- | ---------------------------------------------------------------------: | -------------------------------- |
| LGES                     | success_candidate + 4C-watch        |                      5GWh ESS, NextStar 49% for $100, Ohio 850 layoffs | ESS pivot + EV utilization watch |
| SK On                    | success_candidate                   |       Flatiron ESS up to 7.2GWh, 2026~2030, Georgia EV line conversion | Stage 2 watch                    |
| Samsung SDI              | success_candidate + EV demand watch |                      $3.5B GM JV, 27→36GWh, +3.2%, GM EV target -16.7% | Stage 2                          |
| LG Chem                  | success_candidate                   |                                       Toyota Tsusho 25%, Huayou 49→24% | supply-chain derisking           |
| Hanwha Qcells            | success_candidate + 4C-watch        | 1,000 furlough/pay-hour reduction, 300 contractors cut, $2.3B facility | supply-chain watch               |
| SKIET / EcoPro Materials | 4C-watch                            |                      SKIET -5%, EcoPro Materials -5%, Ford $20B charge | EV demand shock                  |
| POSCO Future M / L&F     | event premium                       |                    POSCO Future M +8.3%, L&F +10%, lithium futures +8% | lithium event                    |
| Hyundai hydrogen plant   | success_candidate                   |                                     930B won, 43,000㎡, 2027 completion | capex Stage 2                    |

---

# 6. score-price alignment 판정

```text
success_candidate:
- LGES ESS pivot
- SK On ESS LFP order
- Samsung SDI / GM JV
- LG Chem / Toyota Tsusho cathode derisking
- Hyundai hydrogen fuel-cell capex

success_candidate + 4C-watch:
- Hanwha Qcells U.S. localization with customs/component disruption
- LGES EV-to-ESS pivot with Ohio plant restart uncertainty

thesis_break_watch:
- SKIET / EcoPro Materials EV demand shock
- Ford-driven battery supply-chain drawdown

cyclical_success / event_premium:
- POSCO Future M / L&F lithium event

price_moved_without_evidence:
- lithium event rally without company-level call-off / margin
- hydrogen CAPEX theme if stock rallies before utilization
- ESS pivot rally before ESS OPM/FCF

hard_4C_confirmed:
- false in this loop
```

---

# 7. 점수비중 교정

## 올릴 축

```text
actual_calloff +5
GWh_volume +5
ESS_revenue_conversion +5
utilization_rate +5
OPM_visibility +5
FCF_after_capex +5
customer_quality +4
supply_chain_derisking +4
localization_with_real_utilization +4
```

### 왜 올리나

LGES와 SK On의 ESS 계약은 EV 둔화 이후 실제 수요축이 ESS로 이동하고 있음을 보여준다. 특히 SK On은 7.2GWh, LGES는 Hanwha QCells향 5GWh ESS 계약이 있다. 다만 GWh 계약이 곧 Stage 3는 아니며, 실제 매출·가동률·OPM·FCF 확인이 필요하다. ([Reuters][2])

## 내릴 축

```text
EV_Capacity_announcement_only -5
ESS_theme_only -4
JV_restructuring_relief_only -4
factory_ownership_without_utilization -4
customer_name_without_calloff -5
lithium_price_event -5
subsidy_dependent_profit -5
negative_FCF_or_debt_burden -5
supply_chain_customs_disruption -5
EV_demand_shock -5
```

### 왜 내리나

Samsung SDI/GM JV, LGES/NextStar, Hyundai hydrogen plant 모두 Stage 2 후보지만, 공장과 CAPEX는 아직 돈을 벌지 않는다. 반대로 Ford의 EV 전략 후퇴와 Qcells의 UFLPA component disruption은 R3에서 바로 4C-watch로 붙여야 한다. ([Reuters][3])

## Green gate 강화 조건

```text
R3 Stage 3-Green 필수:
1. binding contract
2. actual call-off
3. GWh / tonnage volume
4. utilization improvement
5. OPM or gross margin improvement
6. FCF after capex
7. subsidy 제외 이익 품질 확인
8. customer EV strategy risk 통과
9. supply-chain disruption risk 통과
10. price path follows evidence

금지:
고객명만 있음
공장 착공만 있음
JV 재편만 있음
ESS/LFP 테마만 있음
CAPA 전환만 있음
리튬 가격 이벤트만 있음
AMPC/보조금 제외 적자
EV 수요 둔화 무시
```

## 4B 조기감지 조건

```text
4B-watch:
ESS/LFP 계약 발표만으로 주가 급등
EV line conversion headline으로 valuation 확장
리튬 가격 이벤트로 소재주 동반 급등
hydrogen CAPEX 발표만으로 테마 급등
U.S. localization 기대가 utilization보다 먼저 가격에 반영
battery factory ownership이 utilization보다 먼저 valuation에 반영

4B-elevated:
EV 수요 둔화에도 CAPEX valuation 유지
고객 주문 확인 없이 공장·JV 기대만 반영
리튬 가격 반등이 재고평가 이익으로만 연결
supply-chain localization 기대가 customs/부품 지연을 무시
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
debt burden / emergency restructuring
JV termination / ownership transfer under weak demand
subsidy-quality profit collapse
share issuance / dilution under weak demand
supply-chain customs detention
production furlough
```

이번 R3 Loop 10에서는 hard 4C를 억지로 확정하지 않는다. 다만 **EV demand shock**, **factory utilization failure**, **supply-chain customs disruption**, **JV restructuring under weak demand**는 모두 강한 4C-watch다.

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

## docs/round/round_161.md 요약

```md
# R3 Loop 10. Battery / EV / Green Price Validation

이번 라운드는 R3 Loop 10 price-validation 라운드다.

핵심 결론:
- LGES is an ESS pivot success_candidate but also EV utilization 4C-watch. It signed a 5GWh LFP ESS contract with Hanwha QCells for 2028~2030, bought Stellantis’ 49% NextStar stake for $100, and faces uncertain Ohio Ultium restart after around 850 layoffs.
- SK On signed its first LFP ESS order with Flatiron Energy, up to 7.2GWh from 2026~2030, with Georgia EV lines partly converted for ESS. This is Stage 2, not Green.
- Samsung SDI / GM Indiana JV is Stage 2. $3.5B investment, 27GWh initial capacity, possible 36GWh expansion, +3.2% event reaction. But GM EV production forecast cut and 2027 mass-production timing block Green.
- LG Chem / Toyota Tsusho cathode plant is supply-chain derisking Stage 2. Toyota Tsusho took 25%, Huayou fell from 49% to 24%. Cathode volume/offtake/OPM/FCF required before Green.
- Hanwha Qcells is U.S. solar localization candidate but UFLPA/customs disruption creates 4C-watch. About 1,000 workers had reduced pay/hours, and 300 contract workers were cut.
- SKIET / EcoPro Materials were hit by Ford EV demand shock. Ford’s $20B charge drove Korean battery supply-chain names down 3~6%.
- POSCO Future M / L&F lithium rally is commodity event premium. CATL mine suspension lifted lithium futures +8%, POSCO Future M +8.3%, L&F +10%, but this is not Stage 3.
- Hyundai hydrogen fuel-cell plant is Stage 2 capex watch. 930B won plant, 43,000㎡, 2027 completion, but utilization/order/margin/FCF required before Green.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 161 R3 Loop 10 Battery EV Green Price Validation

## 반영 내용
- R3 Loop 10 price-validation 라운드를 추가했다.
- ESS LFP contracts, EV-to-ESS capacity redeployment, EV battery JV restructuring, Samsung SDI/GM localization, cathode supply-chain derisking, solar UFLPA disruption, lithium event premium, hydrogen fuel-cell capex를 비교했다.
- Reuters/AP/MarketWatch/WSJ reported anchors로 가능한 MFE/MAE 및 contract/factory/commodity metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- actual call-off, GWh volume, ESS revenue conversion, utilization, OPM/FCF, supply-chain derisking 가중치 강화
- EV capacity announcement-only, ESS theme-only, JV restructuring relief-only, lithium price event, factory ownership without utilization 감점 강화
- EV demand shock, factory restart uncertainty, customs/component disruption 4C-watch 강화
```

## case row 초안

```jsonl
{"case_id":"r3_loop10_lges_ess_pivot_ev_utilization_watch","symbol":"373220","company_name":"LG Energy Solution","case_type":"success_candidate","primary_archetype":"ESS_LFP_GRID_STORAGE","stage2_date":"2026-02-04/2026-02-06","stage4c_date":"2026-05-12","price_validation":{"price_data_source":"Reuters ESS/JV/restart anchors","stage3_price":null,"hanwha_qcells_ess_contract_gwh":5,"supply_period":"2028-2030","cell_chemistry":"LFP","production_site":"Holland_Michigan","nextstar_stake_acquired_pct":49,"nextstar_purchase_price_usd":100,"nextstar_investment_to_date_cad_bn":5,"ohio_ultium_layoffs_since_january":850,"ohio_prior_employee_context":1330,"indefinite_layoff_context":480,"ess_redeployment":"Tennessee plant workers recalled to produce ESS cells","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_4c_watch","rerating_result":"ESS_pivot_watch_with_EV_utilization_risk","notes":"ESS pivot is Stage 2; EV plant restart uncertainty and utilization risk require 4C-watch."}
{"case_id":"r3_loop10_skon_flatiron_lfp_ess_order","symbol":"096770","company_name":"SK Innovation / SK On","case_type":"success_candidate","primary_archetype":"ESS_LFP_GRID_STORAGE","stage2_date":"2025-09-03","price_validation":{"price_data_source":"Reuters ESS contract anchor","stage3_price":null,"flatiron_ess_contract_gwh":7.2,"supply_period":"2026-2030","chemistry":"LFP","first_sk_on_lfp_ess_order":true,"production_start":"2H_2026","capacity_redeployment":"some Georgia EV battery lines converted for ESS use","contract_value":"not_disclosed","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"SK_On_ESS_pivot_watch","notes":"First LFP ESS order is Stage 2; contract value, utilization, OPM and FCF required before Green."}
{"case_id":"r3_loop10_samsung_sdi_gm_indiana_ev_jv","symbol":"006400","company_name":"Samsung SDI","case_type":"success_candidate","primary_archetype":"EV_BATTERY_JV_CAPEX","stage2_date":"2024-08-28","price_validation":{"price_data_source":"Reuters JV and event-return anchors","stage3_price":null,"jv_investment_usd_bn":3.5,"initial_capacity_gwh":27,"potential_capacity_gwh":36,"capacity_expansion_potential_pct":33.3,"mass_production_target_year":2027,"event_mfe_pct":3.2,"kospi_same_context_pct":-0.3,"relative_outperformance_pp":3.5,"gm_ev_forecast_upper_before_units":300000,"gm_ev_forecast_upper_after_units":250000,"forecast_cut_pct":-16.7,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_demand_watch","rerating_result":"EV_battery_localization_watch","notes":"JV localization is Stage 2; GM demand cut and 2027 production timing block Green until utilization/margin/FCF confirm."}
{"case_id":"r3_loop10_lg_chem_toyota_cathode_derisking","symbol":"051910","company_name":"LG Chem","case_type":"success_candidate","primary_archetype":"CATHODE_SUPPLY_CHAIN_DERISKING","stage2_date":"2025-09-09","price_validation":{"price_data_source":"Reuters ownership-structure anchor","stage3_price":null,"toyota_tsusho_stake_pct":25,"huayou_stake_before_pct":49,"huayou_stake_after_pct":24,"huayou_stake_reduction_pp":-25,"huayou_stake_reduction_relative_pct":-51.0,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"cathode_supply_chain_derisking_watch","notes":"Ownership derisking is Stage 2; cathode volume, customer offtake, OPM and FCF required before Green."}
{"case_id":"r3_loop10_hanwha_qcells_uflpa_supply_chain_watch","symbol":"009830","company_name":"Hanwha Solutions / Qcells","case_type":"success_candidate","primary_archetype":"SOLAR_US_SUPPLY_CHAIN_LOCALIZATION","stage2_date":"2025","stage4c_date":"2025-11","price_validation":{"price_data_source":"AP supply-chain disruption anchor","stage3_price":null,"qcells_georgia_employee_context":3000,"furlough_or_reduced_pay_hours_workers":1000,"contract_workers_laid_off":300,"affected_direct_workers_total":1300,"affected_share_employee_context_pct":33.3,"cartersville_facility_investment_usd_bn":2.3,"cause":"U.S. Customs component detentions under forced-labor import law","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_thesis_break_watch","rerating_result":"solar_localization_watch_with_supply_chain_risk","notes":"Solar localization is Stage 2; UFLPA/customs disruption and furloughs create 4C-watch."}
{"case_id":"r3_loop10_ev_supply_chain_ford_shock_skiet_ecopro","symbol":"361610/450080","company_name":"SK IE Technology / EcoPro Materials / battery supply-chain basket","case_type":"4c_watch","primary_archetype":"SEPARATOR_EV_DEMAND_CYCLE","stage4c_date":"2025-12","price_validation":{"price_data_source":"MarketWatch event-return anchors","stage3_price":null,"ford_charge_usd_bn":20,"sk_innovation_event_mae_pct":-3.0,"lges_event_mae_pct":-6.0,"sk_ie_technology_event_mae_pct":-5.0,"ecopro_materials_event_mae_pct":-5.0,"quantumscape_premarket_mae_pct":-2.0,"price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"EV_supply_chain_demand_shock","notes":"Ford EV retreat and hybrid pivot hit Korean battery supply chain; separator/precursor Green requires utilization and demand confirmation."}
{"case_id":"r3_loop10_posco_future_m_lnf_lithium_event","symbol":"003670/066970","company_name":"POSCO Future M / L&F","case_type":"event_premium","primary_archetype":"LITHIUM_CYCLE_EVENT_PREMIUM","stage1_date":"2025-08-11","stage4b_date":"2025-08-11","price_validation":{"price_data_source":"Reuters/WSJ commodity and event-return anchors","stage3_price":null,"lithium_carbonate_futures_event_return_pct":8,"posco_future_m_event_mfe_pct":8.3,"lnf_event_mfe_pct":10.0,"samsung_sdi_event_mfe_pct":3.2,"lges_event_mfe_pct":2.8,"lithium_price_decline_from_2022_peak_pct":-90,"catl_resume_if_license_renewed":true,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"cyclical_success_event_premium","rerating_result":"lithium_price_event_watch","notes":"Lithium event is not Stage 3 without company-level call-off, OPM, FCF and inventory quality."}
{"case_id":"r3_loop10_hyundai_hydrogen_fuel_cell_capex","symbol":"005380","company_name":"Hyundai Motor hydrogen fuel-cell plant","case_type":"success_candidate","primary_archetype":"HYDROGEN_FUEL_CELL_CAPEX","stage2_date":"2025-10-30","price_validation":{"price_data_source":"Reuters capex/facility evidence","stage3_price":null,"investment_krw_bn":930,"investment_usd_mn":654,"facility_area_sqm":43000,"completion_target_year":2027,"target_applications":["passenger_cars","commercial_trucks_and_buses","construction_equipment","marine_vessels","electrolyzers"],"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"hydrogen_fuel_cell_capex_watch","notes":"Hydrogen capex is Stage 2; utilization, orders, margin and FCF required before Green."}
```

## shadow weight row 초안

```csv
archetype,actual_calloff,gwh_volume,ess_revenue_conversion,utilization,opm_fcf,customer_quality,supply_chain_derisking,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
ESS_LFP_GRID_STORAGE,+5,+5,+5,+5,+5,+4,+3,-2,+4,+4,LGES/SK On ESS contracts are Stage 2; revenue/utilization/OPM/FCF required.
EV_TO_ESS_CAPACITY_REDEPLOYMENT,+4,+5,+5,+5,+5,+3,+3,-3,+4,+5,EV line conversion is positive only if utilization and ESS margins confirm.
EV_BATTERY_JV_CAPEX,+4,+5,+3,+5,+5,+4,+3,-4,+4,+4,Samsung SDI/GM JV is Stage 2; demand delay and utilization risk remain.
CATHODE_SUPPLY_CHAIN_DERISKING,+4,+4,+2,+5,+5,+4,+5,-2,+3,+4,LG Chem/Toyota reduces China exposure but needs offtake and margin.
SOLAR_US_SUPPLY_CHAIN_LOCALIZATION,+3,+3,+2,+5,+5,+4,+5,-3,+4,+5,Qcells localization is Stage 2; customs/component disruption is 4C-watch.
SEPARATOR_EV_DEMAND_CYCLE,+3,+4,+2,+5,+5,+4,+3,-5,+4,+5,Ford EV retreat shows EV demand shock for separator/precursor names.
LITHIUM_CYCLE_EVENT_PREMIUM,+1,+1,+0,+2,+3,+1,+2,-5,+5,+4,Lithium price rally is event premium unless call-off/OPM/FCF confirm.
HYDROGEN_FUEL_CELL_CAPEX,+2,+2,+1,+5,+5,+3,+3,-4,+4,+4,Hydrogen plant capex is Stage 2 until order/utilization/margin/FCF confirm.
```

---

# 이번 R3 Loop 10 결론

R3는 여전히 **Green 발굴보다 false Green 차단이 더 중요한 섹터**다.

```text
1. LGES와 SK On의 ESS 전환은 Stage 2 후보로 인정한다.
   하지만 ESS 매출·가동률·OPM/FCF 전 Stage 3는 아니다.

2. Samsung SDI / GM JV는 U.S. localization Stage 2다.
   GM EV target cut과 2027 production timing이 Green을 막는다.

3. LG Chem / Toyota Tsusho cathode plant는 supply-chain derisking이다.
   하지만 지분구조 변화는 Stage 2이고, offtake·마진·FCF가 Stage 3다.

4. Hanwha Qcells는 U.S. solar localization 후보지만,
   UFLPA/customs disruption과 furlough가 4C-watch다.

5. SKIET / EcoPro Materials는 Ford EV retreat에 바로 흔들렸다.
   EV 소재·분리막은 customer strategy와 utilization을 강하게 봐야 한다.

6. POSCO Future M / L&F lithium rally는 commodity event premium이다.
   lithium futures +8%, 소재주 +8~10%여도 Stage 3가 아니다.

7. Hyundai hydrogen fuel-cell plant는 친환경 CAPEX Stage 2다.
   수요·가동률·마진·FCF 전 Stage 3는 아니다.
```

한 문장으로 압축하면:

> **R3에서 진짜 Stage 3는 “배터리·ESS·친환경 수혜”가 아니라, 계약이 actual call-off·GWh·가동률·OPM·FCF로 내려오고 고객 EV 전략과 공급망 리스크를 통과하는 순간이다.**
> **현재 R3는 ESS 전환과 친환경 CAPEX를 Stage 2로 인정하되, EV demand shock·factory utilization failure·supply-chain disruption을 가장 강한 4C-watch로 봐야 한다.**

[1]: https://www.reuters.com/business/energy/lg-energy-solution-signs-contract-with-hanwha-qcells-supply-5gwh-ess-battery-2026-02-04/?utm_source=chatgpt.com "LG Energy Solution signs contract with Hanwha QCells to supply 5GWh ESS battery"
[2]: https://www.reuters.com/business/energy/south-koreas-sk-signs-energy-storage-battery-supply-deal-with-flatiron-energy-2025-09-03/?utm_source=chatgpt.com "South Korea's SK On signs energy storage battery supply deal with Flatiron Energy"
[3]: https://www.reuters.com/markets/deals/samsung-sdi-signs-deal-with-gm-its-joint-ev-battery-factory-us-2024-08-27/?utm_source=chatgpt.com "Samsung SDI finalizes deal with GM to build $3.5 bln joint EV battery factory in US"
[4]: https://www.reuters.com/markets/emerging/lg-chem-says-japans-toyota-tsusho-acquires-25-stake-its-south-korea-cathode-2025-09-08/?utm_source=chatgpt.com "LG Chem says Japan's Toyota Tsusho acquires 25% stake in its South Korea cathode material plant"
[5]: https://apnews.com/article/f49d0579e0584d689f1feec36ff16ad1?utm_source=chatgpt.com "South Korean solar firm cuts pay and hours for Georgia workers as US officials detain imports"
[6]: https://www.marketwatch.com/story/while-ford-shares-are-remarkably-steady-after-20-billion-charge-these-stocks-are-getting-battered-bbbcfa04?utm_source=chatgpt.com "While Ford shares are remarkably steady after $20 billion charge, these stocks are getting battered"
[7]: https://www.reuters.com/world/china/catl-says-it-has-suspended-mining-operations-yichun-project-2025-08-11/?utm_source=chatgpt.com "CATL says it has suspended mining operations at Yichun project"
[8]: https://www.reuters.com/world/asia-pacific/hyundai-motor-breaks-ground-680-million-hydrogen-fuel-cell-plant-south-korea-2025-10-30/?utm_source=chatgpt.com "Hyundai Motor breaks ground on $680 million hydrogen fuel cell plant in South Korea"
