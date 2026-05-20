순서상 이번은 **R4 Loop 11 — 소재·스프레드·전략자원 가격경로 검증 라운드**다.

이번 R4 Loop 11은 “원자재가 오른다”, “전략광물이다”, “구조조정이다” 같은 말을 한 번 더 깎아서 본다. 핵심은 **스프레드·offtake·cost curve·계약품질·지배구조·현금흐름**이다.

```text
round = R4 Loop 11
round_id = round_175
large_sector = MATERIALS_SPREAD_STRATEGIC_RESOURCES
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
```

이번에도 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC 전체 구간은 안정적으로 확보하지 못했다. 대신 Reuters / FT / WSJ / MarketWatch가 제공한 **가격 anchor, 이벤트 수익률, 계약금액, 구조조정 수치, 원자재 가격, 정책·제재 지표**로 계산 가능한 값만 계산했다. 30D/90D/180D full OHLC가 없는 항목은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R4 = 소재·스프레드·전략자원
```

R4의 Stage 3는 “전략자원”, “리튬”, “반중국 공급망”, “철강 관세”, “구조조정”이라는 단어가 아니라, **제품 스프레드·원가곡선·offtake·수급규율·현금전환이 실제 이익 체급을 바꾸는 순간**이다.

---

# 2. 대상 canonical archetype

```text
CRITICAL_MINERALS_SUPPLY_CHAIN
STRATEGIC_METALS_DILUTION_GOVERNANCE
PETROCHEMICAL_CAPACITY_RESTRUCTURING
STANDALONE_NCC_CREDIT_BREAK
STEEL_ANTIDUMPING_POLICY_RELIEF
STEEL_TARIFF_EXPORT_RISK
CATHODE_SUPPLY_CHAIN_DERISKING
LITHIUM_RESOURCE_SECURITY
NON_CHINA_POLYSILICON_OPTIONALITY
BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK
COMMODITY_PRICE_EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
전략광물:
- Korea Zinc
- antimony / gallium / germanium / rare earth recycling
- U.S. Tennessee smelter
- U.S. government-backed supply chain
- share issuance / dilution / governance fight

석유화학:
- Lotte Chemical / HD Hyundai Chemical
- Daesan NCC shutdown
- Yeochun NCC / DL Chemical / Hanwha Solutions exposure
- China / Middle East overcapacity
- restructuring relief vs spread recovery

철강:
- Hyundai Steel / POSCO Holdings
- Chinese steel plate anti-dumping tariff
- U.S. / Vietnam tariff risk
- domestic protection vs export competitiveness
- policy relief vs demand/capex failure

양극재 / 배터리소재:
- LG Chem / Toyota Tsusho / Huayou stake reduction
- L&F / Tesla 4680 contract collapse
- customer-name headline vs actual call-off

리튬:
- POSCO Holdings / MinRes
- Wodgina / Mt Marion
- spodumene collapse and rebound
- resource security vs downstream margin

폴리실리콘:
- OCI Holdings / OCI TerraSus
- non-China polysilicon
- SpaceX unconfirmed media report
- U.S. solar/data-center power demand
```

---

# 4. 국장 신규 후보 case

## Case A — Korea Zinc `success_candidate + governance/dilution 4B-watch`

```text
symbol = 010130
case_type = success_candidate + governance_watch
archetype = CRITICAL_MINERALS_SUPPLY_CHAIN / STRATEGIC_METALS_DILUTION_GOVERNANCE
```

### stage date

```text
Stage 1:
2024~2025
- MBK / YoungPoong control battle
- antimony / zinc / critical-minerals supply-chain narrative
- China rare-earth export controls 이후 U.S. strategic mineral demand 확대

Stage 2:
2025-12~2026-03
- Tennessee critical-minerals refinery
- $7.4B project
- 540,000 metric tons non-ferrous metals
- 11 critical minerals including antimony, gallium, germanium
- 2025 operating profit 1.2T won
- data-center waste rare-earth recycling talks

Stage 3:
보류
- project FID / construction / offtake / minimum price / margin / FCF 필요
- strategic mineral headline만으로 Green 금지

Stage 4B:
전략광물·antimony·U.S. national-security narrative가 가격에 먼저 반영되면 후보

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

Korea Zinc는 R4에서 “좋은 구조 후보”와 “지배구조·희석 RedTeam”이 같이 붙는 대표 케이스다. 회사는 Tennessee에 74억 달러 규모 critical-minerals smelter를 추진하고, 540,000톤 비철금속과 antimony·gallium·germanium 등 11개 critical minerals 생산을 목표로 한다. 2025년 영업이익은 antimony 호조에 힘입어 1.2조 원을 기록했고, Reuters는 Korea Zinc가 미국 tech firms와 data-center waste에서 rare earths를 추출하는 방안도 논의 중이라고 보도했다. 다만 MBK·YoungPoong이 $1.9B share sale을 막기 위해 injunction을 신청하자 주가는 13% 하락했고, 법원 기각 후에는 Korea Zinc가 최대 5% 오르고 YoungPoong이 최대 10.5% 하락했다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters critical-minerals / governance / share-issuance anchors

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

share_issue_revised:
2.833T won / $1.94B

share_issue_vs_project_value:
1.94 / 7.4
= 26.2%

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

## Case B — Lotte Chemical / HD Hyundai Chemical `failed_rerating + restructuring relief`

```text
symbols = 011170 / HD Hyundai Chemical exposure
case_type = failed_rerating + restructuring_watch
archetype = PETROCHEMICAL_CAPACITY_RESTRUCTURING
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
- HD Hyundai / Lotte Chemical restructuring plan submitted
- Lotte Daesan unit spin-off and merger with HD Hyundai Chemical
- government aims to cut up to 3.7M tpy NCC capacity
- industry asked to cut up to 25% annual capacity

Stage 2 relief:
2026-02-24
- government approves first petrochemical restructuring deal
- Lotte Daesan NCC 1.1M tpy shutdown for 3 years
- HD Hyundai Oilbank and Lotte Chemical each inject 600B won
- combined capital increase 1.2T won
- support package >2T won

Stage 3:
없음
- 구조조정 승인만으로 Green 금지
- spread, OPM, FCF, debt/funding cost 확인 필요

Stage 4B:
구조조정 기대만으로 chemical basket이 급등하면 후보

Stage 4C:
oversupply 지속, spread reversal, inventory build, debt burden, capacity cut insufficient
```

Lotte Chemical / HD Hyundai Chemical 구조조정은 Green이 아니라 **relief**다. Reuters는 정부가 석유화학 공급과잉을 해결하기 위해 NCC capacity를 최대 370만 톤, 전체의 약 25%까지 줄이는 구조조정을 추진하고 있다고 보도했다. 이후 승인된 첫 구조조정은 Lotte Daesan NCC 110만 톤 설비를 3년간 중단하고, HD Hyundai Oilbank와 Lotte Chemical이 각각 6,000억 원을 넣어 1.2조 원 증자를 진행하며, 정부가 2조 원 이상 지원 package를 붙이는 방식이다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters restructuring evidence

stage3_price:
N/A

Daesan_NCC_capacity_halted:
1.1M tpy

shutdown_duration:
3 years

capital_increase:
1.2T won

each_parent_injection:
600B won

government_support_package:
>2.0T won

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

## Case C — YNCC / standalone NCC risk `4C-watch / credit-spread break`

```text
symbols = DL Chemical / Hanwha Solutions exposure
case_type = 4C-watch
archetype = STANDALONE_NCC_CREDIT_BREAK
```

### stage date

```text
Stage 1:
2025-08
- South Korea petrochemical restructuring road map
- small standalone cracker closure risk
- naphtha demand decline

Stage 2:
없음
- weak financials / forced restructuring is not positive evidence

Stage 3:
없음

Stage 4C-watch:
2025-08-27
- YNCC flagged as least competitive by Citi
- YNCC debt-to-equity ratio 249% by end-1H 2025
- possible shutdown of one or two of three crackers
- No.3 cracker already shut in August
```

YNCC는 상장 직접종목은 아니지만 DL Chemical·Hanwha Solutions exposure로 R4 RedTeam에 넣어야 한다. Reuters는 Yeochun NCC가 한국 3위 ethylene producer이고, Citi가 “weak financials and lack of integration” 때문에 가장 취약하다고 봤다고 보도했다. YNCC의 debt-to-equity ratio는 2025년 상반기 말 249%였고, No.3 cracker는 이미 8월에 shut down됐으며, 하나 또는 두 개 cracker shutdown 가능성이 거론됐다. 이건 구조조정 수혜가 아니라 credit-spread 4C-watch다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters petrochemical overhaul / YNCC credit-risk anchor

stage3_price:
N/A

YNCC_debt_to_equity_1H2025:
249%

YNCC_position:
South Korea's third-largest ethylene producer

possible_shutdown:
one or two of three crackers

No3_cracker_status:
shut in August 2025

national_capacity_cut_target:
2.7M~3.7M tpy

national_capacity_cut_equivalent:
about 25% of capacity including Shaheen project

naphtha_feedstock_share_for_ethlyene:
82%

Shaheen_new_supply:
1.8M tpy ethylene due in 2026

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = standalone_NCC_credit_risk
stage_failure_type = 4C_watch
```

---

## Case D — Hyundai Steel / POSCO Holdings `policy relief + tariff risk`

```text
symbols = 004020 / 005490
case_type = event_premium + 4C-watch
archetype = STEEL_ANTIDUMPING_POLICY_RELIEF / STEEL_TARIFF_EXPORT_RISK
```

### stage date

```text
Stage 1:
2024~2025
- cheap Chinese steel inflow
- domestic steel-plate margin pressure
- U.S. steel/aluminium tariff uncertainty

Stage 2:
2025-02-20
- Korea provisionally imposes anti-dumping duties 27.91%~38.02% on Chinese steel plates
- Hyundai Steel +5.8%
- POSCO Holdings +3.9%
- KOSPI -0.7%

Stage 4C-watch:
2025-06-02
- Trump tariff threat: steel/aluminium tariff 25% → 50%
- Hyundai Steel as much as -5.1%
- POSCO Holdings as much as -3.2%
- KOSPI -0.2%

Stage 3:
없음
- domestic anti-dumping relief만으로 Green 금지
- actual plate spread, export margin, utilization, FCF 확인 필요
```

철강은 같은 정책이 relief와 risk를 동시에 만든다. 한국 정부가 중국산 steel plate에 27.91%~38.02% 반덤핑 관세를 잠정 부과하기로 하자 Hyundai Steel은 5.8%, POSCO Holdings는 3.9% 올랐고 KOSPI는 0.7% 하락했다. 반대로 미국이 steel/aluminium tariffs를 25%에서 50%로 올릴 수 있다는 threat가 나오자 Hyundai Steel은 최대 5.1%, POSCO Holdings는 최대 3.2% 하락했다. R4에서는 “관세 수혜”를 단순 Green으로 주지 말고 **domestic spread relief와 export/tariff risk**를 동시에 본다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ tariff-policy and event-return anchors

stage3_price:
N/A

Korea_anti_dumping_tariff:
27.91%~38.02%

Chinese_steel_imports_2024:
$10.4B

Chinese_share_of_Korea_steel_imports:
49%

Hyundai_Steel_relief_MFE:
+5.8%

POSCO_Holdings_relief_MFE:
+3.9%

KOSPI_same_context:
-0.7%

Hyundai_relative_outperformance:
5.8 - (-0.7)
= +6.5pp

POSCO_relative_outperformance:
3.9 - (-0.7)
= +4.6pp

U.S._tariff_threat:
25% → 50%

Hyundai_Steel_tariff_threat_MAE:
-5.1%

POSCO_Holdings_tariff_threat_MAE:
-3.2%

KOSPI_tariff_threat_context:
-0.2%

MFE_30D / MAE_30D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium + tariff_4C_watch
rerating_result = steel_policy_relief_with_export_risk
stage_failure_type = policy_stage2_not_green
```

---

## Case E — LG Chem / Toyota Tsusho cathode plant `success_candidate / China-exposure derisking`

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
cathode demand slowdown, customer call-off failure, lithium/nickel price reversal, utilization failure
```

LG Chem의 cathode plant 지분구조 변화는 R4의 좋은 Stage 2다. Toyota Tsusho가 25% 지분을 취득해 두 번째로 큰 주주가 됐고, 중국 Huayou Cobalt 지분은 49%에서 24%로 낮아졌다. 이건 China-exposure derisking으로 해석할 수 있지만, cathode volume·customer offtake·OPM·FCF 확인 전에는 Green이 아니다. ([Reuters][5])

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

## Case F — POSCO Holdings / MinRes lithium JV `success_candidate + lithium cycle watch`

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

POSCO의 MinRes lithium JV는 resource-security Stage 2다. POSCO는 7.65억 달러를 내고 MinRes lithium business 일부 30%를 인수하며, Wodgina와 Mt Marion에 각각 간접 15% 지분을 얻는다. MinRes 주가는 최대 10.8% 상승했다. 하지만 spodumene 가격은 2022년 톤당 6,000달러 이상에서 2025년 6월 610달러 부근까지 떨어진 뒤 880달러로 반등했을 뿐, 여전히 고점 대비 85% 이상 낮다. 즉 resource security는 좋지만, lithium cycle과 downstream margin을 통과해야 한다. ([Reuters][6])

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

## Case G — OCI Holdings / OCI TerraSus `success_candidate + unconfirmed media 4B-watch`

```text
symbol = 010060
case_type = success_candidate + event_premium
archetype = NON_CHINA_POLYSILICON_OPTIONALITY
```

### stage date

```text
Stage 1:
2025-06-07
- U.S. solar-cell expansion
- non-China solar supply chain
- AI data-center power demand

Stage 2:
2025-06-07
- Texas plant capacity expansion
- $1.2B investment
- target 10GW by 2027

Stage 2 / 4B-watch:
2026-04-14
- OCI TerraSus / SpaceX polysilicon supply talk media report
- SpaceX did not respond
- OCI spokesperson could not confirm

Stage 3:
없음
- capex-heavy project / media report만으로 Green 금지
- confirmed customer contract, polysilicon offtake, margin, FCF 확인 필요

Stage 4C:
SpaceX deal not confirmed, subsidy rollback, polysilicon price decline, capex overrun
```

OCI는 non-China polysilicon 후보지만, SpaceX 보도는 아직 미확정 media report다. FT는 OCI가 Texas plant capacity를 2027년까지 10GW로 늘리기 위해 12억 달러를 투자한다고 보도했다. 이후 Reuters는 OCI TerraSus가 SpaceX와 multi-year polysilicon supply contract를 논의 중이라는 한국 언론 보도를 전했지만, SpaceX는 답변하지 않았고 OCI spokesperson은 확인할 수 없다고 밝혔다. 즉 U.S. solar/data-center power demand는 Stage 2지만, SpaceX headline은 4B/event premium이다. ([Financial Times][7])

### 실제 가격경로 검증

```text
price_data_source:
FT / Reuters capacity and media-report anchors

stage3_price:
N/A

U.S._investment:
$1.2B

target_capacity:
10GW by 2027

capacity_equivalent:
roughly 10 nuclear power plants equivalent, per FT framing

SpaceX_contract_status:
unconfirmed media report

SpaceX_response:
no response reported

OCI_response:
could not confirm report

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

## Case H — L&F / Tesla 4680 cathode `hard 4C / contract quality break`

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
약함
- 고객명과 계약금액 headline 존재

Stage 3:
없음
- actual call-off, volume, margin, FCF 확인 전 Green 금지

Stage 4C:
2025-12-29
- Tesla cathode supply deal value $2.9B → $7,386
- 4680 production yield issue / EV demand slowdown
- Cybertruck demand disappointment
```

L&F는 R3/R4 전체에서 가장 명확한 contract-quality hard 4C다. Reuters는 L&F의 Tesla high-nickel cathode supply deal 가치가 29억 달러에서 7,386달러로 사실상 붕괴했다고 보도했다. 배경에는 Tesla 4680 생산 ramp 문제, EV demand slowdown, Cybertruck 부진이 언급됐다. 고객명과 계약금액 headline만으로 Green을 주면 안 되는 이유다. ([Reuters][8])

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

# 5. 이번 R4 case별 요약표

| case                         | 분류                             |                                                                 실제 가격검증 | alignment              |
| ---------------------------- | ------------------------------ | ----------------------------------------------------------------------: | ---------------------- |
| Korea Zinc                   | success_candidate + governance |                     $7.4B smelter, OP 1.2T, injunction -13%, relief +5% | Stage 2 + governance   |
| Lotte / HD Hyundai petrochem | failed_rerating + relief       |            Daesan 1.1M tpy shutdown, 1.2T capital increase, >2T support | restructuring relief   |
| YNCC / standalone NCC        | 4C-watch                       |                         debt/equity 249%, possible 1~2 cracker shutdown | credit watch           |
| Hyundai Steel / POSCO tariff | event + 4C-watch               | China plate tariff relief: +5.8%/+3.9%; U.S. tariff threat: -5.1%/-3.2% | policy two-sided       |
| LG Chem / Toyota Tsusho      | success_candidate              |                                              Toyota 25%, Huayou 49%→24% | supply-chain derisking |
| POSCO / MinRes lithium       | success_candidate              |                     $765M, MinRes +10.8%, spodumene still -85%+ vs peak | resource Stage 2       |
| OCI / SpaceX polysilicon     | event premium                  |                               $1.2B Texas expansion, SpaceX unconfirmed | non-China optionality  |
| L&F / Tesla cathode          | hard 4C                        |                                             $2.9B → $7,386, -99.999745% | contract-quality break |

---

# 6. score-price alignment 판정

```text
success_candidate:
- Korea Zinc critical minerals
- LG Chem / Toyota Tsusho cathode derisking
- POSCO / MinRes lithium resource security
- OCI non-China polysilicon

failed_rerating / restructuring relief:
- Lotte Chemical / HD Hyundai Chemical restructuring

event_premium:
- Hyundai Steel / POSCO anti-dumping relief
- OCI / SpaceX unconfirmed report

thesis_break_watch:
- YNCC standalone NCC credit risk
- steel tariff export risk
- Korea Zinc governance / dilution
- petrochemical oversupply

hard_4C:
- L&F contract-quality collapse

price_moved_without_evidence:
- SpaceX polysilicon unconfirmed media report
- lithium resource rally without downstream margin
- anti-dumping relief rally without spread / margin
```

---

# 7. 점수비중 교정

## 올릴 축

```text
product_spread +5
cost_curve_advantage +5
offtake_quality +5
contract_quality +5
FCF_after_working_capital +5
supply_discipline_confirmed +5
capacity_shutdown_confirmed +4
China_exposure_reduction +4
resource_security_with_downstream_margin +4
governance_cleanliness +4
```

### 왜 올리나

R4는 원자재·전략자원·스프레드가 모두 “말”로는 좋아 보인다. 하지만 Korea Zinc도 FID·offtake·margin·dilution을 통과해야 하고, POSCO lithium도 downstream margin이 필요하다. Lotte/HD Hyundai 구조조정처럼 실제 capacity shutdown이 있는 경우는 높게 보되, spread·FCF 확인 전 Stage 3는 보류해야 한다.

## 내릴 축

```text
commodity_price_up_only -5
strategic_material_headline_only -5
policy_relief_only -5
unconfirmed_media_report -5
restructuring_plan_without_margin -4
capacity_cut_without_spread_recovery -4
contract_headline_without_calloff -5
customer_name_without_volume -5
governance_dilution_risk -5
China_customer_or_supply_chain_concentration -4
```

### 왜 내리나

L&F는 고객명과 계약금액 headline이 있어도 actual call-off가 없으면 hard 4C가 된다는 기준점이다. OCI/SpaceX는 미확정 media report라 4B다. Korea Zinc는 전략광물 구조가 좋아도 share issuance와 governance fight가 RedTeam이다.

## Green gate 강화 조건

```text
R4 Stage 3-Green 필수:
1. product spread 개선이 실제 확인됨
2. cost curve advantage 있음
3. supply discipline 또는 capacity shutdown이 확인됨
4. offtake / price floor / take-or-pay 존재
5. FCF 전환 또는 working capital 개선
6. contract quality 확인
7. China / tariff / sanction / governance risk 통과
8. capex burden과 dilution risk 통과
9. 가격경로가 evidence 이후 따라옴

금지:
commodity price spike
strategic mineral headline only
정책 지원 기대
unconfirmed media report
구조조정 계획만 있음
고객명만 있는 소재계약
offtake 없는 resource deal
희석·지배구조 이슈 미해결
```

## 4B 조기감지 조건

```text
4B-watch:
원자재 가격 반등으로 소재주 동반 급등
전략광물 headline로 가격이 먼저 감
anti-dumping / tariff relief만으로 철강주 급등
구조조정 기대만으로 petrochemical basket 상승
미확정 고객 보도에 급등
리튬 resource security 뉴스로 price가 먼저 감
governance fight / tender / share issue가 가격을 끌고 감

4B-elevated:
수익보다 정책·뉴스가 먼저 가격화
offtake 불명
working capital 악화
capex와 dilution이 커짐
가격 반등이 재고평가 이익에 그침
```

## 4C hard gate 조건

```text
contract value collapse
contract cancellation
spread reversal
China oversupply
standalone cracker credit break
inventory build
NCC shutdown from distress
share issuance / governance abuse
tariff shock causing export margin damage
unconfirmed deal failure
resource project write-down
offtake failure
FCF deterioration
```

이번 R4 Loop 11에서 확정 hard 4C는 **L&F / Tesla cathode contract value collapse**다. YNCC, Korea Zinc governance, steel tariff, OCI unconfirmed report는 hard 4C가 아니라 4C-watch 또는 4B/event premium이다.

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

## docs/round/round_175.md 요약

```md
# R4 Loop 11. Materials / Spread / Strategic Resources Price Validation

이번 라운드는 R4 Loop 11 price-validation 라운드다.

핵심 결론:
- Korea Zinc is strategic-minerals Stage 2 plus governance/dilution watch. $7.4B Tennessee smelter, 540,000 tons output, 11 critical minerals, 2025 OP 1.2T won, but $1.94B share issue and governance fight caused -13% injunction shock and +5% court-relief bounce.
- Lotte Chemical / HD Hyundai Chemical restructuring is relief, not Green. Daesan NCC 1.1M tpy shutdown for 3 years, 1.2T won capital increase, >2T won support package. Spread/OPM/FCF required.
- YNCC / standalone NCC is 4C-watch. Debt-to-equity 249%, possible shutdown of one or two crackers, No.3 cracker already shut in August 2025.
- Hyundai Steel / POSCO tariff case is two-sided policy event. Korean anti-dumping tariffs on Chinese steel plates drove Hyundai Steel +5.8% and POSCO Holdings +3.9%, but U.S. tariff threat later hit Hyundai Steel -5.1% and POSCO -3.2%.
- LG Chem / Toyota Tsusho cathode plant is supply-chain derisking Stage 2. Toyota Tsusho acquired 25%; Huayou fell from 49% to 24%.
- POSCO / MinRes lithium JV is resource-security Stage 2. POSCO pays $765M for indirect 15% Wodgina/Mt Marion interests; MinRes +10.8%; spodumene remains far below 2022 peak.
- OCI Holdings is non-China polysilicon optionality Stage 2, but SpaceX report is unconfirmed event premium. Texas $1.2B expansion to 10GW by 2027 is positive; SpaceX supply talk was not confirmed.
- L&F is hard 4C. Tesla cathode deal value collapsed from $2.9B to $7,386.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 175 R4 Loop 11 Materials Spread Strategic Resources Price Validation

## 반영 내용
- R4 Loop 11 price-validation 라운드를 추가했다.
- Strategic minerals, petrochemical restructuring, standalone NCC credit break, steel tariff relief/risk, cathode derisking, lithium resource security, non-China polysilicon optionality, battery-material contract hard 4C를 비교했다.
- Reuters/FT/WSJ/MarketWatch anchors로 가능한 MFE/MAE 및 spread/contract/project metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- product spread, cost curve, offtake quality, contract quality, FCF after working capital, supply discipline, China exposure reduction 가중치 강화
- commodity price-only, strategic material headline-only, policy relief-only, unconfirmed media report, restructuring without margin, customer name without volume 감점 강화
- L&F contract-value collapse hard 4C 유지
```

## case row 초안

```jsonl
{"case_id":"r4_loop11_korea_zinc_critical_minerals_governance","symbol":"010130","company_name":"Korea Zinc","case_type":"success_candidate","primary_archetype":"CRITICAL_MINERALS_SUPPLY_CHAIN","stage2_date":"2025-12/2026-03","stage4c_date":"2025-12-16_watch","price_validation":{"price_data_source":"Reuters critical-minerals/governance/share-issuance anchors","stage3_price":null,"us_smelter_project_value_usd_bn":7.4,"planned_output_tons":540000,"critical_minerals_count":11,"target_margin_pct":"17-19","planned_construction_start":"early_2027","planned_operation_year":2030,"operating_profit_2025_krw_trn":1.2,"share_issue_revised_krw_trn":2.833,"share_issue_revised_usd_bn":1.94,"share_issue_vs_project_value_pct":26.2,"new_investor_stake_pct":10,"injunction_event_mae_pct":-13,"court_rejection_event_mfe_pct":5,"youngpoong_court_event_mae_pct":-10.5,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_governance_watch","rerating_result":"strategic_minerals_project_watch","notes":"Strategic minerals are Stage 2; FID/offtake/margin/FCF and governance/dilution must clear before Green."}
{"case_id":"r4_loop11_lotte_hd_petrochemical_restructuring","symbol":"011170/HD_Hyundai_Chemical","company_name":"Lotte Chemical / HD Hyundai Chemical","case_type":"failed_rerating","primary_archetype":"PETROCHEMICAL_CAPACITY_RESTRUCTURING","stage2_date":"2025-11-26/2026-02-24","price_validation":{"price_data_source":"Reuters restructuring evidence","stage3_price":null,"daesan_ncc_capacity_mn_tpy":1.1,"shutdown_duration_years":3,"capital_increase_krw_trn":1.2,"each_parent_injection_krw_bn":600,"support_package_krw_trn":2.0,"utility_cost_savings_krw_bn":115,"rnd_funding_krw_bn":26,"equity_split_after_restructuring":"50:50","target_capacity_cut_national_mn_tpy":3.7,"industry_capacity_cut_goal_pct":25,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"failed_rerating_then_restructuring_watch","rerating_result":"petrochemical_restructuring_relief","notes":"Capacity shutdown/support is Stage 2 relief; spread, OPM and FCF recovery required for Green."}
{"case_id":"r4_loop11_yncc_standalone_ncc_credit_watch","symbol":"DL_Chemical/Hanwha_Solutions_exposure","company_name":"Yeochun NCC / DL Chemical / Hanwha Solutions exposure","case_type":"4c_watch","primary_archetype":"STANDALONE_NCC_CREDIT_BREAK","stage4c_date":"2025-08-27","price_validation":{"price_data_source":"Reuters petrochemical overhaul/YNCC credit-risk anchor","stage3_price":null,"yncc_debt_to_equity_1h2025_pct":249,"yncc_position":"third-largest South Korean ethylene producer","possible_shutdown":"one_or_two_of_three_crackers","no3_cracker_status":"shut_in_August_2025","national_capacity_cut_target_mn_tpy":"2.7-3.7","capacity_cut_equivalent_pct":25,"naphtha_feedstock_share_for_ethylene_pct":82,"shaheen_new_supply_mn_tpy":1.8,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"standalone_NCC_credit_risk","notes":"Weak financials and standalone NCC exposure require 4C-watch, not restructuring Green."}
{"case_id":"r4_loop11_hyundai_posco_steel_tariff_two_sided","symbol":"004020/005490","company_name":"Hyundai Steel / POSCO Holdings","case_type":"event_premium","primary_archetype":"STEEL_ANTIDUMPING_POLICY_RELIEF","stage2_date":"2025-02-20","stage4c_date":"2025-06-02_watch","price_validation":{"price_data_source":"Reuters/WSJ tariff-policy and event-return anchors","stage3_price":null,"korea_antidumping_tariff_pct":"27.91-38.02","chinese_steel_imports_2024_usd_bn":10.4,"chinese_share_of_korea_steel_imports_pct":49,"hyundai_steel_relief_mfe_pct":5.8,"posco_holdings_relief_mfe_pct":3.9,"kospi_same_context_pct":-0.7,"hyundai_relative_outperformance_pp":6.5,"posco_relative_outperformance_pp":4.6,"us_tariff_threat_pct":"25_to_50","hyundai_tariff_threat_mae_pct":-5.1,"posco_tariff_threat_mae_pct":-3.2,"kospi_tariff_threat_context_pct":-0.2,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_tariff_4c_watch","rerating_result":"steel_policy_relief_with_export_risk","notes":"Anti-dumping relief helps domestic spread but export tariff risk blocks Green until spread/margin/FCF confirm."}
{"case_id":"r4_loop11_lg_chem_toyota_cathode_derisking","symbol":"051910","company_name":"LG Chem","case_type":"success_candidate","primary_archetype":"CATHODE_SUPPLY_CHAIN_DERISKING","stage2_date":"2025-09-09","price_validation":{"price_data_source":"Reuters ownership-structure anchor","stage3_price":null,"toyota_tsusho_stake_pct":25,"huayou_stake_before_pct":49,"huayou_stake_after_pct":24,"huayou_stake_reduction_pp":-25,"huayou_stake_reduction_relative_pct":-51.0,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"cathode_supply_chain_derisking_watch","notes":"Ownership derisking is Stage 2; cathode volume, customer offtake, OPM and FCF required before Green."}
{"case_id":"r4_loop11_posco_minres_lithium_resource_security","symbol":"005490","company_name":"POSCO Holdings / MinRes lithium JV","case_type":"success_candidate","primary_archetype":"LITHIUM_RESOURCE_SECURITY","stage2_date":"2025-11-11","price_validation":{"price_data_source":"Reuters lithium transaction/commodity anchors","stage3_price":null,"transaction_value_usd_mn":765,"posco_indirect_stake_pct":15,"assets":["Wodgina","Mt Marion"],"minres_event_mfe_pct":10.8,"spodumene_peak_2022_usd_per_t":6000,"spodumene_low_2025_usd_per_t":610,"spodumene_drawdown_peak_to_low_pct":-89.8,"spodumene_rebound_610_to_880_pct":44.3,"spodumene_880_vs_peak_pct":-85.3,"price_validation_status":"posco_stock_ohlc_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_cyclical_watch","rerating_result":"lithium_resource_security_watch","notes":"Resource security is Stage 2; downstream margin, offtake economics and FCF required before Green."}
{"case_id":"r4_loop11_oci_non_china_polysilicon_spacex_watch","symbol":"010060","company_name":"OCI Holdings / OCI TerraSus","case_type":"success_candidate","primary_archetype":"NON_CHINA_POLYSILICON_OPTIONALITY","stage2_date":"2025-06-07","stage4b_date":"2026-04-14","price_validation":{"price_data_source":"FT/Reuters capacity and media-report anchors","stage3_price":null,"us_investment_usd_bn":1.2,"target_capacity_gw":10,"target_year":2027,"capacity_equivalent":"roughly_10_nuclear_power_plants","spacex_contract_status":"unconfirmed_media_report","spacex_response":"no_response_reported","oci_response":"could_not_confirm_report","spacex_solar_satellite_constellation":1000000,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_event_premium","rerating_result":"non_China_polysilicon_watch","notes":"U.S. expansion is Stage 2; unconfirmed SpaceX report is event premium until contract/offtake/margin/FCF confirm."}
{"case_id":"r4_loop11_lnf_tesla_cathode_contract_hard_4c","symbol":"066970","company_name":"L&F","case_type":"4c_thesis_break","primary_archetype":"BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK","stage4c_date":"2025-12-29","price_validation":{"price_data_source":"Reuters contract-value collapse anchor","stage3_price":null,"initial_contract_value_usd_bn":2.9,"revised_contract_value_usd":7386,"contract_value_drawdown_pct":-99.999745,"contract_period":"2024-2025","product":"high-nickel cathode materials for Tesla 4680 cells","reason_context":["4680_yield_issue","EV_demand_slowdown","Cybertruck_demand_disappointment"],"price_validation_status":"reported_contract_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"battery_material_contract_quality_failure","notes":"Customer name and contract headline cannot be Green without actual call-off and volume/margin conversion."}
```

## shadow weight row 초안

```csv
archetype,product_spread,cost_curve,offtake_quality,contract_quality,fcf_after_wc,supply_discipline,capacity_shutdown,china_exposure_reduction,governance_cleanliness,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
CRITICAL_MINERALS_SUPPLY_CHAIN,+3,+5,+5,+4,+5,+3,+0,+4,+4,-3,+5,+4,Korea Zinc strategic minerals are Stage 2 but governance/dilution blocks Green.
STRATEGIC_METALS_DILUTION_GOVERNANCE,+2,+4,+4,+3,+5,+2,+0,+3,+5,-5,+5,+5,Share issuance/control fight requires governance RedTeam.
PETROCHEMICAL_CAPACITY_RESTRUCTURING,+5,+4,+1,+2,+5,+5,+5,+0,+3,-3,+3,+5,Restructuring relief requires spread/OPM/FCF before Green.
STANDALONE_NCC_CREDIT_BREAK,+5,+3,+0,+0,+5,+5,+5,+0,+3,0,+3,+5,YNCC weak financials and shutdown risk are 4C-watch.
STEEL_ANTIDUMPING_POLICY_RELIEF,+5,+3,+1,+2,+4,+3,+0,+0,+3,-3,+4,+4,Anti-dumping tariff is Stage 2 relief, not Green before spread/FCF.
STEEL_TARIFF_EXPORT_RISK,+4,+3,+1,+2,+4,+2,+0,+0,+3,-4,+4,+5,U.S./Vietnam tariff risk offsets domestic relief.
CATHODE_SUPPLY_CHAIN_DERISKING,+3,+3,+5,+4,+5,+2,+0,+5,+3,-2,+3,+4,LG Chem/Toyota reduces China exposure but needs offtake and margin.
LITHIUM_RESOURCE_SECURITY,+2,+4,+5,+3,+5,+2,+0,+2,+3,-5,+4,+4,POSCO lithium JV is resource-security Stage 2 but lithium cycle risk remains.
NON_CHINA_POLYSILICON_OPTIONALITY,+4,+3,+5,+3,+5,+3,+0,+5,+3,-5,+5,+4,OCI U.S. expansion is Stage 2; SpaceX report is unconfirmed.
BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK,+1,+2,+5,+5,+5,+0,+0,+1,+3,0,+3,+5,L&F Tesla contract collapse is hard 4C.
```

---

# 이번 R4 Loop 11 결론

R4는 **Stage 2와 착시가 가장 비슷하게 생긴 섹터**다. 원자재·정책·전략자원 뉴스는 겉으로는 구조적으로 보이지만, 실제로는 스프레드와 현금흐름이 닫혀야 한다.

```text
1. Korea Zinc는 전략광물 후보지만,
   governance / dilution / offtake / FCF를 통과해야 Stage 3다.

2. Lotte Chemical / HD Hyundai Chemical 구조조정은 relief다.
   capacity shutdown은 좋지만 spread·OPM·FCF 회복 전 Green 금지다.

3. YNCC는 standalone NCC credit 4C-watch다.
   재무가 약한 cracker는 구조조정 수혜가 아니라 생존 리스크로 봐야 한다.

4. Hyundai Steel / POSCO tariff case는 양면 정책이다.
   중국산 반덤핑은 relief지만, U.S. tariff threat는 export-margin RedTeam이다.

5. LG Chem / Toyota Tsusho는 China exposure derisking Stage 2다.
   그러나 cathode offtake와 margin 전 Green은 아니다.

6. POSCO / MinRes lithium JV는 resource security Stage 2다.
   lithium 가격 cycle과 downstream margin을 통과해야 한다.

7. OCI는 non-China polysilicon optionality가 있지만,
   SpaceX 보도는 미확정 media report라 4B/event premium이다.

8. L&F는 R4 hard 4C 기준점이다.
   Tesla 고객명과 $2.9B 계약 headline이 있어도 actual call-off가 무너지면 Green은 즉시 깨진다.
```

한 문장으로 압축하면:

> **R4에서 진짜 Stage 3는 “전략자원·리튬·관세·구조조정·폴리실리콘 뉴스가 좋다”가 아니라, product spread·offtake·cost curve·contract quality·FCF가 실제로 잠겨서 이익 체급이 바뀌는 순간이다.**

[1]: https://www.reuters.com/world/asia-pacific/korea-zinc-talks-with-us-tech-firms-extract-rare-earths-data-centre-waste-2026-03-12/?utm_source=chatgpt.com "Korea Zinc in talks with US tech firms to extract rare earths from data centre waste"
[2]: https://www.reuters.com/world/asia-pacific/south-koreas-hd-hyundai-lotte-chemical-submit-plan-restructure-petrochemical-2025-11-26/?utm_source=chatgpt.com "South Korea's HD Hyundai, Lotte Chemical submit plan to restructure petrochemical businesses"
[3]: https://www.reuters.com/business/energy/south-korea-petrochemical-overhaul-likely-shut-small-stand-alone-naphtha-2025-08-27/?utm_source=chatgpt.com "South Korea petrochemical overhaul likely to shut small, stand-alone naphtha crackers"
[4]: https://www.reuters.com/markets/asia/south-korea-provisionally-slaps-tariffs-chinese-steel-plates-dumping-2025-02-20/?utm_source=chatgpt.com "South Korea provisionally slaps tariffs on Chinese steel plates for dumping"
[5]: https://www.reuters.com/markets/emerging/lg-chem-says-japans-toyota-tsusho-acquires-25-stake-its-south-korea-cathode-2025-09-08/?utm_source=chatgpt.com "LG Chem says Japan's Toyota Tsusho acquires 25% stake in its South Korea cathode material plant"
[6]: https://www.reuters.com/business/energy/australias-minres-sell-30-lithium-jv-stake-posco-765-mln-2025-11-11/?utm_source=chatgpt.com "Australia's MinRes inks $765 million deal with POSCO for lithium JV stake, shares surge"
[7]: https://www.ft.com/content/e618a7e3-6388-42f9-beb8-c32599f7239d?utm_source=chatgpt.com "Solar group OCI doubles down on US despite Donald Trump's war on clean energy"
[8]: https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/?utm_source=chatgpt.com "South Korea's L&F slashes value of battery material supply deal with Tesla"
