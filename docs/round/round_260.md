순서상 이번은 **R4 Loop 12 — 소재·스프레드·전략자원 가격경로 검증 라운드**다.

```text
round = R4 Loop 12
round_id = round_188
large_sector = MATERIALS_SPREAD_STRATEGIC_RESOURCES
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
```

이번 R4 Loop 12는 지난 R4의 POSCO/MinRes, L&F, Lotte/HD Hyundai 대표 케이스만 반복하지 않고, **Poongsan 방산·구리 optionality, Korea Zinc 전략광물/희석, 중국 rare-earth 압박, 철강 관세 양면성, Hyundai Steel 미국 CAPEX false positive, LG Chem/YNCC petrochemical restructuring, Lotte/HD Hyundai 구조조정 relief, critical-minerals policy relief**를 중심으로 본다.

---

# 1. 이번 라운드 대섹터

```text
R4 = 소재·스프레드·전략자원
```

R4의 Stage 3는 “전략자원”, “관세”, “희토류”, “구조조정”, “미국 공장”, “정책지원”이라는 단어가 아니다.

**제품 스프레드, 원가곡선, offtake, supply discipline, contract quality, working capital, FCF가 실제로 닫히는 순간**이다.

---

# 2. 대상 canonical archetype

```text
DEFENSE_METALS_AMMUNITION_OPTIONALITY
CRITICAL_MINERALS_RECYCLING_SMELTER
RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C
STEEL_TARIFF_TWO_SIDED_RELIEF_RISK
POLICY_CAPEX_FALSE_POSITIVE
PETROCHEMICAL_CAPACITY_RESTRUCTURING
STANDALONE_NCC_CREDIT_BREAK
CRITICAL_MINERALS_POLICY_RELIEF
```

---

# 3. deep sub-archetype

```text
방산·금속:
- Poongsan copper products + ammunition business
- Hanwha Aerospace acquisition rumor
- ammunition optionality vs unconfirmed M&A

전략광물:
- Korea Zinc U.S. Tennessee smelter
- antimony / gallium / germanium
- rare earth recycling from data-center waste
- share issuance / dilution / governance risk

희토류·중국:
- China letters to Korean firms
- rare-earth-containing products
- defense customers / U.S. end-use restriction
- transformer / battery / display / EV / aerospace exposure

철강:
- POSCO Holdings
- Hyundai Steel
- SeAH Steel
- domestic anti-dumping relief
- U.S. steel/aluminium tariff risk
- Vietnam anti-dumping export risk

석유화학:
- LG Chem
- Hanwha Solutions / DL Chemical / YNCC
- Lotte Chemical / HD Hyundai Chemical
- Daesan NCC shutdown
- capacity cuts / credit risk / overcapacity

정책·전략자원:
- Korea critical minerals plan
- 17 monitored minerals
- China cooperation + U.S.-led FORGE bloc
- 250B won overseas mining support
```

---

# 4. 국장 신규 후보 case

## Case A — Poongsan `event_premium / defense-metals optionality, not Green`

```text
symbol = 103140
case_type = event_premium / insufficient_price_data
archetype = DEFENSE_METALS_AMMUNITION_OPTIONALITY
```

### stage date

```text
Stage 1:
2026-04-03
- Hanwha Aerospace reportedly submitted bid for Poongsan defense business
- potential deal around 1.5T won / $1.1B
- Poongsan ammunition business supplies small-caliber rounds, large-caliber shells, missile warheads
- Poongsan also specializes in copper products

Stage 2:
보류
- M&A rumor itself is not business conversion
- copper spread / ammunition order / confirmed transaction needed

Stage 4B:
2026-04-03 ~ 2026-04-09
- potential sale rumor → then Hanwha drops acquisition review
- Poongsan says it is not pursuing sale of ammunition business
- rumor-driven optionality must be treated as 4B/event premium

Stage 3:
없음
- confirmed sale / defense order / copper spread / cash return 확인 전 Green 금지
```

Poongsan은 R4의 좋은 “방산 금속 optionality” 후보지만, 이번에는 오히려 **M&A rumor는 Green이 아니다**라는 교정 case로 둔다. Reuters는 Hanwha Aerospace가 Poongsan 방산 부문 인수를 검토했다는 보도와, 며칠 뒤 Hanwha가 검토를 중단했고 Poongsan도 탄약 사업 매각 계획이 없다고 공시한 내용을 보도했다. 즉 Poongsan의 copper·ammunition 구조는 관심 대상이지만, confirmed order나 spread가 아니라 rumor라면 4B다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters M&A rumor / denial anchors

stage3_price:
N/A

reported_potential_deal_value:
1.5T won / about $1.1B

business:
copper products
ammunition manufacturing
small-caliber rounds
large-caliber shells
missile warheads

transaction_status:
not confirmed
Hanwha dropped review
Poongsan denied sale plan

Poongsan_stock_OHLC:
price_data_unavailable_after_deep_search

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium / insufficient_price_data
rerating_result = defense_metals_M&A_optional_watch
stage_failure_type = rumor_not_green
```

---

## Case B — Korea Zinc `success_candidate + dilution/governance 4B-watch`

```text
symbol = 010130
case_type = success_candidate + 4B-watch
archetype = CRITICAL_MINERALS_RECYCLING_SMELTER
```

### stage date

```text
Stage 1:
2025~2026
- U.S. strategic critical minerals demand
- China export controls
- antimony / gallium / germanium scarcity
- data-center waste recycling optionality

Stage 2:
2026-03-12
- Korea Zinc in talks with U.S. tech firms to extract rare earths from data-center waste
- U.S. Tennessee smelter project $7.4B
- 540,000 metric tons non-ferrous metals
- 11 critical minerals including antimony, gallium, germanium
- 2025 OP 1.2T won
- target margin 17~19%

Stage 4B / dilution watch:
2025-12-31
- share issuance revised to 2.833T won / $1.94B
- funds for U.S. smelter
- project quality high, but dilution and governance remain RedTeam

Stage 3:
없음
- FID / permits / offtake / minimum price / margin / FCF 확인 전 Green 금지
```

Korea Zinc는 R4 전략광물 중 가장 구조적인 Stage 2 후보다. U.S. tech firms와 data-center waste rare-earth recycling을 논의 중이고, Tennessee smelter는 7.4B 달러, 11개 critical minerals, 17~19% target margin이라는 강한 구조를 갖는다. 그러나 2.833조 원 share issuance가 붙어 있어, strategic mineral quality와 dilution risk를 동시에 봐야 한다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters critical-minerals / share-issuance anchors

stage3_price:
N/A

U.S._smelter_project_value:
$7.4B

planned_output:
540,000 metric tons non-ferrous metals

critical_minerals:
11 including antimony, gallium, germanium

target_margin:
17~19%

2025_operating_profit:
1.2T won

antimony_price_2025:
$25/lb

share_issuance:
2.833T won / $1.94B

share_issuance_vs_project_value:
1.94 / 7.4
= 26.2%

planned_construction:
early 2027

planned_operation:
2030

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + dilution_watch
rerating_result = critical_minerals_project_watch
stage_failure_type = strategic_stage2_not_green_until_offtake_FCF
```

---

## Case C — China rare-earth pressure on Korean firms `4C-watch / strategic supply-chain overlay`

```text
symbols = transformers / batteries / displays / EV / aerospace / medical equipment basket
case_type = 4C-watch
archetype = RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C
```

### stage date

```text
Stage 1:
2025-04
- China rare-earth export restrictions
- U.S.-China tariff war
- Korean manufacturers caught between Chinese inputs and U.S. defense end-users

Stage 4C-watch:
2025-04-22
- China reportedly asks Korean companies not to export products using Chinese rare earths to U.S. defense firms
- affected sectors include power transformers, batteries, displays, EVs, aerospace, medical equipment
- letters warned sanctions for violation

Stage 3:
없음
- strategic material exposure is RedTeam overlay, not Green
```

이 case는 개별 종목이 아니라 R4 전체의 hard gate 후보 overlay다. 중국이 한국 기업에 중국산 rare earths를 사용한 제품을 미국 방산기업에 수출하지 말라고 압박했다는 보도는, transformer·battery·display·EV·aerospace·medical equipment까지 넓게 걸린다. “전략자원 수혜”와 동시에 “중국 원료 end-use restriction”이 붙는 구조다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters rare-earth export-control report

stage3_price:
N/A

affected_sectors:
power transformers
batteries
displays
electric vehicles
aerospace
medical equipment

reported_action:
China sent letters asking Korean companies not to export products using Chinese rare earths to U.S. defense firms

sanction_warning:
true

stock_OHLC:
price_data_unavailable_after_deep_search

MFE:
N/A

MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = rare_earth_end_use_restriction_overlay
stage_failure_type = sector_4C_watch
```

---

## Case D — POSCO / Hyundai Steel / SeAH Steel `two-sided tariff case`

```text
symbols = 005490 / 004020 / 306200
case_type = event_premium + 4C-watch
archetype = STEEL_TARIFF_TWO_SIDED_RELIEF_RISK
```

### stage date

```text
Stage 1:
2025-02~06
- Chinese steel dumping pressure
- U.S. steel / aluminium tariff escalation
- Korean steel export margin risk

Stage 2 relief:
2025-02-20
- Korea provisionally imposes 27.91~38.02% anti-dumping tariff on Chinese steel plates
- Hyundai Steel +5.8%
- POSCO Holdings +3.9%
- KOSPI -0.7%

Stage 4C-watch:
2025-02-10
- Trump talks 25% steel/aluminium tariff
- POSCO -3.6%
- Hyundai Steel -2.9%
- KOSPI -0.5%

Stage 4C-watch 강화:
2025-06-02
- U.S. steel/aluminium tariff to 50%
- POSCO / Hyundai Steel -3%
- SeAH Steel -8%
```

철강은 R4에서 **정책 relief와 export risk가 동시에 붙는 case**다. 한국의 중국산 steel plate anti-dumping tariff는 Hyundai Steel과 POSCO에 단기 relief를 줬지만, 미국 steel/aluminium tariff가 50%까지 올라가자 POSCO·Hyundai Steel·SeAH Steel이 동시에 맞았다. domestic protection만 보고 Green을 주면 안 된다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters steel tariff / event-return anchors

stage3_price:
N/A

Korea_anti_dumping_tariff:
27.91~38.02%

Hyundai_Steel_relief_MFE:
+5.8%

POSCO_relief_MFE:
+3.9%

KOSPI_same_context_relief:
-0.7%

Hyundai_relative_outperformance_relief:
5.8 - (-0.7)
= +6.5pp

POSCO_relative_outperformance_relief:
3.9 - (-0.7)
= +4.6pp

U.S._25pct_tariff_talk:
POSCO -3.6%
Hyundai Steel -2.9%
KOSPI -0.5%

U.S._50pct_tariff_event:
POSCO / Hyundai Steel -3%
SeAH Steel -8%

Korea_steel_imports_from_China_2024:
$10.4B

China_share_of_Korea_steel_imports:
49%

MFE_30D / MAE_30D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium + thesis_break_watch
rerating_result = steel_policy_relief_with_export_tariff_risk
stage_failure_type = policy_relief_not_green
```

---

## Case E — Hyundai Steel U.S. plant `failed_rerating / policy CAPEX false positive`

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
- low-carbon auto steel localization
- Hyundai Motor Group U.S. investment package

Stage 2:
2025-03-25
- Hyundai Steel announces $5.8B Louisiana plant
- annual capacity 2.7M tonnes
- part of Hyundai Motor Group $21B U.S. package
- shares initially > +5%, then -4.4%

Stage 4C-watch:
2025-04-22
- stock lost 21.2% since announcement
- POSCO -18.3%
- KOSPI -5.5%
- funding unclear
- project may be political signaling
- 50% borrowing, remaining equity/funding unclear

Stage 2 revision:
2026-01-26
- Hyundai Steel affiliate plans $2.9B capital increase
- total project $5.8B: $2.9B equity + $2.9B external borrowing
- ownership: Hyundai Steel USA 50%, POS-Louisiana 20%, Hyundai Motor America 15%, Kia America 15%
```

Hyundai Steel은 이번 R4의 대표 false-positive다. 미국 공장, tariff hedge, low-carbon steel이라는 말은 좋아 보였지만, 발표 직후 +5%에서 -4.4%로 뒤집혔고, 이후 -21.2%까지 밀렸다. 2026년에는 funding structure가 더 명확해졌지만, 아직 Green은 아니다. 실제 customer demand, spread, margin, FCF, tariff benefit이 필요하다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters U.S. steel plant / investor backlash / capital-increase anchors

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

2026_capital_increase:
$2.9B

total_project_funding:
$2.9B equity + $2.9B external borrowing

ownership:
Hyundai Steel USA 50%
POS-Louisiana 20%
Hyundai Motor America 15%
Kia America 15%

production_start_target:
2029

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = false_positive_score
rerating_result = policy_CAPEX_failed_rerating
stage_failure_type = CAPEX_without_confirmed_ROI
```

---

## Case F — LG Chem / Hanwha Solutions / DL Chemical / YNCC `4C-watch / petrochemical overcapacity`

```text
symbols = 051910 / 009830 / DL Chemical exposure
case_type = 4C-watch
archetype = STANDALONE_NCC_CREDIT_BREAK / PETROCHEMICAL_CAPACITY_RESTRUCTURING
```

### stage date

```text
Stage 1:
2025-08
- South Korea petrochemical oversupply
- China / Middle East capacity pressure
- government asks industry to cut 2.7~3.7M tpy NCC capacity

Stage 4C-watch:
2025-08-27
- standalone naphtha crackers likely to shut
- YNCC may shut one or two of three crackers
- YNCC debt-to-equity 249% at end-1H 2025
- No.3 cracker already shut in August

Stage 2 relief:
2025-12-19
- LG Chem submits petrochemical restructuring plan
- DL Chemical and Hanwha Solutions submit YNCC-related plans
- details undisclosed

Stage 3:
없음
- restructuring plan만으로 Green 금지
- capacity cut, spread recovery, OPM, FCF, debt cleanup 확인 필요
```

LG Chem·Hanwha Solutions·DL Chemical/YNCC는 R4 petrochemical의 4C-watch다. 정부가 최대 25% capacity cut을 요구한 건 sector crisis의 증거이고, YNCC debt-to-equity 249%, No.3 cracker shutdown은 hard gate에 가깝다. LG Chem과 YNCC 관련 주주들이 restructuring plan을 제출했지만, 내용이 공개되지 않았기 때문에 relief이지 Green은 아니다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters petrochemical overhaul / restructuring-plan anchors

stage3_price:
N/A

capacity_cut_target:
2.7M~3.7M tpy

capacity_cut_equivalent:
about 25% of South Korean capacity including Shaheen project

naphtha_feedstock_share_for_ethylene:
82%

YNCC_debt_to_equity_1H2025:
249%

YNCC_possible_shutdown:
one or two of three crackers

YNCC_No3_cracker_status:
shut in August 2025

Shaheen_new_supply_due_2026:
1.8M tpy ethylene

LG_Chem_plan:
submitted but details undisclosed

DL_Hanwha_YNCC_plan:
submitted but details undisclosed

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = petrochemical_credit_and_capacity_break_watch
stage_failure_type = restructuring_plan_not_green
```

---

## Case G — Lotte Chemical / HD Hyundai Chemical `restructuring relief, not Green`

```text
symbols = 011170 / 267250 exposure
case_type = failed_rerating_then_policy_relief
archetype = PETROCHEMICAL_CAPACITY_RESTRUCTURING
```

### stage date

```text
Stage 1:
2025-11-26
- HD Hyundai / Lotte Chemical submit restructuring plan
- Daesan NCC integration
- Korean petrochemical sector crisis

Stage 2:
2026-02-24
- government approves first petrochemical restructuring deal
- Lotte Daesan NCC 1.1M tpy shutdown for 3 years
- HD Hyundai Oilbank and Lotte Chemical each inject 600B won
- total capital increase 1.2T won
- support package >2T won
- utility-cost savings up to 115B won
- R&D funding 26B won

Stage 3:
없음
- capacity shutdown은 relief
- spread, OPM, FCF, debt cleanup 확인 전 Green 금지

Stage 4C:
China/Middle East oversupply persists, Shaheen adds supply, spread recovery fails
```

Lotte/HD Hyundai 구조조정은 R4에서 “relief와 Green의 차이”를 보여준다. Daesan NCC 110만 톤을 3년간 멈추고 1.2조 원 증자를 하며 정부 지원이 붙었지만, 이건 crisis relief다. spread·OPM·FCF가 돌아오기 전까지 Stage 3는 아니다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters first petrochemical restructuring approval anchors

stage3_price:
N/A

Daesan_NCC_shutdown_capacity:
1.1M tpy

shutdown_duration:
3 years

capital_increase:
1.2T won

each_parent_injection:
600B won

government_support_package:
>2T won

utility_cost_savings:
up to 115B won

R&D_funding:
26B won

equity_split_after_restructuring:
50:50

national_capacity_cut_target:
up to 3.7M tpy

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = failed_rerating_then_policy_relief
rerating_result = petrochemical_restructuring_relief
stage_failure_type = relief_not_green
```

---

## Case H — Korea critical-minerals policy `success_candidate policy relief, not Green`

```text
symbol = critical-minerals / battery / semiconductor / EV / petrochemical basket
case_type = success_candidate_policy_relief
archetype = CRITICAL_MINERALS_POLICY_RELIEF
```

### stage date

```text
Stage 1:
2026-02-05
- Korea joins U.S.-led critical minerals bloc
- simultaneously seeks China cooperation
- rare earth supply-chain fragility

Stage 2:
2026-02-05
- Korea to establish hotline and joint committee with China
- 17 critical minerals designated for monitoring
- cooperation with U.S., Vietnam, Laos
- 250B won support for companies developing overseas mining projects
- Korea chairs FORGE until June 2026

Stage 3:
없음
- policy relief만으로 소재주 Green 금지
- actual supply contracts, offtake, inventory, margin, FCF 확인 필요

Stage 4C:
China restriction recurrence, U.S.-China conflict, minerals shortage, sanction risk
```

한국의 critical-minerals policy는 R4 전체에 좋은 Stage 2 relief다. 다만 중국과 협력하면서 동시에 U.S.-led bloc에 참여하는 구조라, 안정적인 공급계약·재고·마진으로 내려오기 전까지는 Green이 아니다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters critical-minerals policy anchor

stage3_price:
N/A

critical_minerals_monitored:
17

overseas_mining_support:
250B won / about $172M

policy_tools:
China hotline
China joint committee
U.S.-led FORGE bloc
cooperation with Vietnam and Laos

FORGE_chair_period:
until June 2026

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_policy_relief
rerating_result = critical_minerals_supply_chain_policy_watch
stage_failure_type = policy_not_green
```

---

# 5. 이번 R4 case별 요약표

| case                         | 분류                                 |                                                           실제 가격검증 | alignment         |
| ---------------------------- | ---------------------------------- | ----------------------------------------------------------------: | ----------------- |
| Poongsan                     | event premium / insufficient       |                             1.5T won sale rumor → denied, no OHLC | rumor not Green   |
| Korea Zinc                   | success_candidate + dilution watch |                       $7.4B smelter, OP 1.2T, 2.833T won issuance | strategic Stage 2 |
| China rare-earth pressure    | 4C-watch                           | transformer/battery/display/EV/aerospace end-use restriction risk | sector overlay    |
| POSCO / Hyundai / SeAH steel | event + 4C-watch                   |     Hyundai +5.8% relief, POSCO +3.9%; U.S. tariff event SeAH -8% | two-sided tariff  |
| Hyundai Steel U.S. plant     | false_positive_score               |               +5% → -4.4%, then -21.2%; $2.9B equity + $2.9B debt | CAPEX fail        |
| LG Chem / Hanwha / DL / YNCC | 4C-watch                           |         capacity cut 25%, YNCC debt/equity 249%, plan undisclosed | credit break      |
| Lotte / HD Hyundai Chemical  | policy relief                      |             1.1M tpy shutdown, 1.2T capital increase, >2T support | relief not Green  |
| critical-minerals policy     | policy relief                      |                     17 minerals, 250B won overseas mining support | policy not Green  |

---

# 6. score-price alignment 판정

```text
success_candidate:
- Korea Zinc
- critical-minerals policy relief

event_premium:
- Poongsan M&A rumor
- Hyundai Steel/POSCO domestic anti-dumping relief

failed_rerating:
- Hyundai Steel U.S. plant

thesis_break_watch:
- China rare-earth end-use pressure
- U.S. steel/aluminium tariffs
- LG Chem / Hanwha / DL / YNCC petrochemical credit stress
- petrochemical overcapacity

policy_relief_not_green:
- Lotte / HD Hyundai restructuring
- critical-minerals policy
- Korean anti-dumping tariff

hard_4C_confirmed:
- false
```

---

# 7. 점수비중 교정

## 올릴 축

```text
product_spread +5
cost_curve_advantage +5
offtake_quality +5
supply_discipline +5
capacity_shutdown_confirmed +5
working_capital_control +5
FCF_after_restructuring +5
critical_minerals_supply_security +4
governance_and_dilution_control +4
export_control_resilience +5
```

### 왜 올리나

Korea Zinc는 전략광물 구조가 강하지만 share issuance와 project execution을 봐야 한다. 철강은 domestic anti-dumping relief가 있지만 U.S./Vietnam tariff risk가 있다. Petrochemical은 capacity shutdown이 있어도 spread와 FCF 전에는 relief다. R4는 결국 **spread와 cash**가 왕이다.

## 내릴 축

```text
M&A_rumor_only -5
policy_relief_only -5
strategic_material_headline_only -5
US_CAPEX_without_ROI -5
capacity_shutdown_without_spread_recovery -4
restructuring_plan_undisclosed -4
China_customer_or_material_concentration -5
rare_earth_end_use_restriction -5
tariff_export_risk -5
dilution_for_project_capex -4
```

### 왜 내리나

Poongsan은 rumor만으로 Green 불가다. Hyundai Steel U.S. plant는 policy CAPEX가 가격경로에서 실패했다. Petrochemical restructuring은 crisis relief이지 Green이 아니다. China rare-earth pressure는 R4 전체에 export-control overlay로 들어간다.

## Green gate 강화 조건

```text
R4 Stage 3-Green 필수:
1. product spread 개선 확인
2. cost curve advantage 확인
3. offtake / price floor / take-or-pay 존재
4. supply discipline 또는 capacity shutdown 실제 확인
5. restructuring 이후 OPM / FCF 개선
6. working capital 안정
7. China / tariff / rare-earth end-use risk 통과
8. dilution / governance risk 통과
9. 가격경로가 evidence 이후 따라옴

금지:
M&A rumor only
정책지원 only
전략자원 headline only
미국 CAPEX only
구조조정 계획 undisclosed
capacity shutdown만 있고 spread 회복 없음
희토류·중국 end-use restriction 존재
```

## 4B 조기감지 조건

```text
4B-watch:
M&A rumor로 소재주 급등
전략광물 headline로 price가 먼저 감
anti-dumping tariff relief로 철강주 급등
critical-minerals policy로 basket 급등
U.S. CAPEX announcement로 일시 급등 후 fade
restructuring relief로 petrochemical basket 상승

4B-elevated:
실제 spread가 회복되지 않음
CAPEX funding 불명
dilution 발생
중국 end-use restriction 발생
support package는 있지만 debt cleanup 불명
```

## 4C hard gate 조건

```text
rare-earth export restriction causing supply halt
China end-use sanction
U.S. tariff destroying export margin
project CAPEX funding failure
equity dilution without ROI
NCC credit break / workout
standalone cracker shutdown from distress
spread collapse
working capital blowout
offtake failure
```

이번 R4 Loop 12에서는 hard 4C를 억지로 확정하지 않는다. 대신 **Hyundai Steel CAPEX false positive**, **China rare-earth restriction overlay**, **petrochemical credit break**를 4C-watch로 강하게 둔다.

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

## docs/round/round_188.md 요약

```md
# R4 Loop 12. Materials / Spread / Strategic Resources Price Validation

이번 라운드는 R4 Loop 12 price-validation 라운드다.

핵심 결론:
- Poongsan is defense-metals optionality but not Green. Hanwha’s reported 1.5T won acquisition interest was later dropped, and Poongsan denied any sale plan. M&A rumor is 4B/event premium.
- Korea Zinc is critical-minerals Stage 2 plus dilution watch. U.S. Tennessee smelter $7.4B, 540,000 tons output, 11 critical minerals, 2025 OP 1.2T won, target margin 17~19%, but 2.833T won share issuance means dilution/governance gate.
- China rare-earth pressure is sector 4C-watch. Korean companies producing transformers, batteries, displays, EVs, aerospace and medical equipment could face sanctions if rare-earth-containing products are exported to U.S. defense firms.
- Steel tariff case is two-sided. Korea anti-dumping tariff drove Hyundai Steel +5.8% and POSCO +3.9%, but U.S. tariff risk hit POSCO/Hyundai -3% and SeAH Steel -8%.
- Hyundai Steel U.S. plant is policy-CAPEX false positive. Initial +5% reversed to -4.4%, then shares lost -21.2% after funding uncertainty; later financing clarified as $2.9B equity and $2.9B borrowing.
- LG Chem / Hanwha / DL / YNCC is petrochemical 4C-watch. Sector capacity cut target 2.7M~3.7M tpy, YNCC debt-to-equity 249%, No.3 cracker shut, restructuring plans undisclosed.
- Lotte / HD Hyundai Chemical restructuring is relief, not Green. Daesan NCC 1.1M tpy shutdown for three years, 1.2T won capital increase, >2T won support package; spread/OPM/FCF required.
- Korea critical-minerals policy is Stage 2 relief. 17 minerals monitored, 250B won support for overseas mining projects, China hotline and FORGE participation; actual supply/of-take/margin needed.
```

## docs/checkpoints/checkpoint_28a_round188_r4_loop12.md 요약

```md
# Checkpoint 28A Round 188 R4 Loop 12 Materials Spread Strategic Resources Price Validation

## 반영 내용
- R4 Loop 12 price-validation 라운드를 추가했다.
- Defense-metals M&A rumor, critical-minerals recycling/smelter, rare-earth export-control overlay, steel tariff two-sided risk, policy CAPEX false positive, petrochemical credit break, restructuring relief, critical-minerals policy relief를 비교했다.
- Reuters / MarketWatch anchors로 가능한 MFE/MAE 및 policy/project/spread metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- product spread, cost curve, offtake quality, supply discipline, capacity shutdown, working-capital control, FCF after restructuring, export-control resilience 가중치 강화
- M&A rumor-only, policy relief-only, strategic material headline-only, U.S. CAPEX without ROI, restructuring plan undisclosed, rare-earth end-use restriction, tariff export risk 감점 강화
```

## data/e2r_case_library/cases_r4_loop12_round188.jsonl 초안

```jsonl
{"case_id":"r4_loop12_poongsan_defense_metals_mna_rumor","symbol":"103140","company_name":"Poongsan","case_type":"event_premium","primary_archetype":"DEFENSE_METALS_AMMUNITION_OPTIONALITY","stage1_date":"2026-04-03","stage4b_date":"2026-04-09","price_validation":{"price_data_source":"Reuters M&A rumor / denial anchors","stage3_price":null,"reported_potential_deal_value_krw_trn":1.5,"reported_potential_deal_value_usd_bn":1.1,"businesses":["copper products","ammunition manufacturing","small-caliber rounds","large-caliber shells","missile warheads"],"transaction_status":"not confirmed; Hanwha dropped review; Poongsan denied sale plan","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_insufficient_price_data","rerating_result":"defense_metals_M&A_optional_watch","notes":"M&A rumor is not Green; confirmed order, copper spread or transaction/cash return needed."}
{"case_id":"r4_loop12_korea_zinc_critical_minerals_dilution_watch","symbol":"010130","company_name":"Korea Zinc","case_type":"success_candidate","primary_archetype":"CRITICAL_MINERALS_RECYCLING_SMELTER","stage2_date":"2026-03-12","stage4b_date":"2025-12-31","price_validation":{"price_data_source":"Reuters critical-minerals / share-issuance anchors","stage3_price":null,"us_smelter_project_value_usd_bn":7.4,"planned_output_tonnes":540000,"critical_minerals":["antimony","gallium","germanium","rare earths"],"target_margin_pct":"17-19","operating_profit_2025_krw_trn":1.2,"antimony_price_2025_usd_per_lb":25,"share_issuance_krw_trn":2.833,"share_issuance_usd_bn":1.94,"share_issuance_vs_project_value_pct":26.2,"planned_construction":"early_2027","planned_operation_year":2030,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_dilution_watch","rerating_result":"critical_minerals_project_watch","notes":"Strategic mineral project is Stage 2; offtake, minimum price, margin, FCF and dilution control required."}
{"case_id":"r4_loop12_china_rare_earth_end_use_restriction_overlay","symbol":"transformer/battery/display/EV/aerospace/medical_equipment_basket","company_name":"Korean rare-earth-dependent manufacturers","case_type":"4c_watch","primary_archetype":"RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C","stage4c_date":"2025-04-22","price_validation":{"price_data_source":"Reuters rare-earth export-control report","stage3_price":null,"affected_sectors":["power transformers","batteries","displays","electric vehicles","aerospace","medical equipment"],"reported_action":"China asked Korean companies not to export products using Chinese rare earths to U.S. defense firms","sanction_warning":true,"price_validation_status":"sector_overlay_no_company_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"rare_earth_end_use_restriction_overlay","notes":"Rare-earth end-use restrictions are sector 4C-watch and block strategic-material Green."}
{"case_id":"r4_loop12_posco_hyundai_seah_steel_tariff_two_sided","symbol":"005490/004020/306200","company_name":"POSCO Holdings / Hyundai Steel / SeAH Steel","case_type":"event_premium","primary_archetype":"STEEL_TARIFF_TWO_SIDED_RELIEF_RISK","stage2_date":"2025-02-20","stage4c_date":"2025-02-10/2025-06-02","price_validation":{"price_data_source":"Reuters steel tariff/event-return anchors","stage3_price":null,"korea_antidumping_tariff_pct":"27.91-38.02","hyundai_steel_relief_mfe_pct":5.8,"posco_relief_mfe_pct":3.9,"kospi_relief_context_pct":-0.7,"hyundai_relative_outperformance_pp":6.5,"posco_relative_outperformance_pp":4.6,"us_25pct_tariff_posco_mae_pct":-3.6,"us_25pct_tariff_hyundai_mae_pct":-2.9,"us_25pct_tariff_kospi_context_pct":-0.5,"us_50pct_tariff_posco_hyundai_mae_pct":-3.0,"seah_steel_50pct_tariff_mae_pct":-8.0,"china_steel_imports_2024_usd_bn":10.4,"china_share_of_korea_steel_imports_pct":49,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_thesis_break_watch","rerating_result":"steel_policy_relief_with_export_tariff_risk","notes":"Domestic anti-dumping relief is Stage 2; U.S./Vietnam export tariff risk blocks Green."}
{"case_id":"r4_loop12_hyundai_steel_us_capex_false_positive","symbol":"004020","company_name":"Hyundai Steel","case_type":"failed_rerating","primary_archetype":"POLICY_CAPEX_FALSE_POSITIVE","stage2_date":"2025-03-25","stage4c_date":"2025-04-22_watch","price_validation":{"price_data_source":"Reuters U.S. steel plant / funding uncertainty anchors","stage3_price":null,"plant_investment_usd_bn":5.8,"annual_capacity_mn_tonnes":2.7,"group_us_investment_package_usd_bn":21,"announcement_initial_mfe_pct":5.0,"announcement_session_mae_pct":-4.4,"post_announcement_drawdown_pct":-21.2,"posco_same_period_pct":-18.3,"kospi_same_period_pct":-5.5,"relative_underperformance_vs_kospi_pp":-15.7,"capital_increase_2026_usd_bn":2.9,"funding_structure":"$2.9B equity + $2.9B external borrowing","ownership":"Hyundai Steel USA 50%, POS-Louisiana 20%, Hyundai Motor America 15%, Kia America 15%","production_start_target":2029,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"false_positive_score","rerating_result":"policy_CAPEX_failed_rerating","notes":"U.S. CAPEX and tariff hedge were not Green; confirmed demand, spread, margin and FCF required."}
{"case_id":"r4_loop12_lgchem_hanwha_dl_yncc_petrochemical_credit_watch","symbol":"051910/009830/DL_Chemical_exposure","company_name":"LG Chem / Hanwha Solutions / DL Chemical / YNCC","case_type":"4c_watch","primary_archetype":"STANDALONE_NCC_CREDIT_BREAK","stage4c_date":"2025-08-27","stage2_date":"2025-12-19_relief","price_validation":{"price_data_source":"Reuters petrochemical overhaul / restructuring-plan anchors","stage3_price":null,"capacity_cut_target_mn_tpy":"2.7-3.7","capacity_cut_equivalent_pct":25,"naphtha_feedstock_share_for_ethylene_pct":82,"yncc_debt_to_equity_1h2025_pct":249,"yncc_possible_shutdown":"one or two of three crackers","yncc_no3_cracker_status":"shut in August 2025","shaheen_new_supply_2026_mn_tpy":1.8,"lg_chem_plan_status":"submitted; details undisclosed","dl_hanwha_yncc_plan_status":"submitted; details undisclosed","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"petrochemical_credit_and_capacity_break_watch","notes":"Restructuring plan is relief only; spread, OPM, FCF and debt cleanup required."}
{"case_id":"r4_loop12_lotte_hd_hyundai_chemical_restructuring_relief","symbol":"011170/267250_exposure","company_name":"Lotte Chemical / HD Hyundai Chemical","case_type":"failed_rerating_then_policy_relief","primary_archetype":"PETROCHEMICAL_CAPACITY_RESTRUCTURING","stage2_date":"2026-02-24","price_validation":{"price_data_source":"Reuters first petrochemical restructuring approval anchors","stage3_price":null,"daesan_ncc_shutdown_capacity_mn_tpy":1.1,"shutdown_duration_years":3,"capital_increase_krw_trn":1.2,"each_parent_injection_krw_bn":600,"government_support_package_krw_trn":2.0,"utility_cost_savings_krw_bn":115,"rnd_funding_krw_bn":26,"equity_split_after_restructuring":"50:50","national_capacity_cut_target_mn_tpy":3.7,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"failed_rerating_then_policy_relief","rerating_result":"petrochemical_restructuring_relief","notes":"Capacity shutdown and support package are relief; spread/OPM/FCF required before Green."}
{"case_id":"r4_loop12_korea_critical_minerals_policy_relief","symbol":"critical_minerals_basket","company_name":"Korea critical-minerals policy basket","case_type":"success_candidate_policy_relief","primary_archetype":"CRITICAL_MINERALS_POLICY_RELIEF","stage2_date":"2026-02-05","price_validation":{"price_data_source":"Reuters critical-minerals policy anchor","stage3_price":null,"critical_minerals_monitored":17,"overseas_mining_support_krw_bn":250,"overseas_mining_support_usd_mn":172,"policy_tools":["China hotline","China joint committee","U.S.-led FORGE bloc","cooperation with Vietnam and Laos"],"forge_chair_period":"until June 2026","price_validation_status":"policy_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_policy_relief","rerating_result":"critical_minerals_supply_chain_policy_watch","notes":"Policy relief is Stage 2; actual supply contracts, offtake, inventory, margin and FCF required."}
```

## data/sector_taxonomy/score_weight_profiles_round188_r4_loop12_v1.csv 초안

```csv
archetype,product_spread,cost_curve,offtake_quality,supply_discipline,capacity_shutdown,working_capital,fcf_after_restructuring,critical_minerals_security,governance_dilution,export_control_resilience,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
DEFENSE_METALS_AMMUNITION_OPTIONALITY,+3,+3,+4,+2,+0,+4,+4,+3,+3,+3,-5,+5,+3,Poongsan M&A rumor is event premium until confirmed transaction/order/spread.
CRITICAL_MINERALS_RECYCLING_SMELTER,+4,+5,+5,+3,+0,+5,+5,+5,+5,+5,-3,+5,+4,Korea Zinc is strong Stage 2 but dilution/offtake/project execution must clear.
RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C,+0,+0,+0,+0,+0,+3,+3,+5,+2,+5,0,+4,+5,China rare-earth end-use restriction is sector 4C-watch.
STEEL_TARIFF_TWO_SIDED_RELIEF_RISK,+5,+4,+2,+3,+0,+4,+4,+0,+3,+5,-4,+5,+5,Domestic tariff relief and export tariff risk must be scored together.
POLICY_CAPEX_FALSE_POSITIVE,+3,+3,+2,+1,+0,+5,+5,+1,+5,+4,-5,+5,+5,Hyundai Steel U.S. CAPEX failed price validation due funding/ROI uncertainty.
PETROCHEMICAL_CAPACITY_RESTRUCTURING,+5,+4,+1,+5,+5,+5,+5,+0,+3,+2,-3,+4,+5,Capacity shutdown is relief until spread/OPM/FCF improve.
STANDALONE_NCC_CREDIT_BREAK,+5,+3,+0,+5,+5,+5,+5,+0,+3,+2,0,+3,+5,YNCC debt/equity 249% and cracker shutdown are 4C-watch.
CRITICAL_MINERALS_POLICY_RELIEF,+2,+2,+3,+3,+0,+2,+2,+5,+2,+5,-5,+4,+4,Policy support is Stage 2 only; actual supply/of-take/margin required.
```

---

# 이번 R4 Loop 12 결론

```text
1. Poongsan은 방산·구리 optionality가 있지만, M&A rumor는 Green이 아니다.
   confirmed transaction, copper spread, ammunition order가 필요하다.

2. Korea Zinc는 전략광물 Stage 2가 강하다.
   하지만 2.833T won share issuance, offtake, FCF, project execution을 통과해야 한다.

3. China rare-earth pressure는 R4 전체 4C-watch다.
   transformer, battery, display, EV, aerospace까지 end-use restriction이 걸릴 수 있다.

4. 철강은 relief와 risk가 동시에 붙는다.
   한국 anti-dumping은 Hyundai/POSCO relief였지만, U.S. 50% tariff는 POSCO/HYUNDAI/SeAH를 때렸다.

5. Hyundai Steel U.S. plant는 policy CAPEX false positive다.
   발표 초기 +5%가 -4.4%로 뒤집혔고, 이후 -21.2% drawdown이 나왔다.

6. LG Chem / Hanwha / DL / YNCC는 petrochemical credit 4C-watch다.
   restructuring plan 제출만으로는 Green이 아니다.

7. Lotte / HD Hyundai 구조조정은 crisis relief다.
   1.1M tpy shutdown과 2T won support가 있어도 spread/OPM/FCF 전 Green 금지다.

8. Critical-minerals policy는 좋은 Stage 2 relief다.
   하지만 실제 공급계약, offtake, inventory, margin으로 닫혀야 한다.
```

한 문장으로 압축하면:

> **R4에서 진짜 Stage 3는 “전략자원·희토류·관세·구조조정·미국 CAPEX가 있다”가 아니라, 그 이벤트가 제품 스프레드·offtake·원가곡선·working capital·FCF로 잠기고, 중국 end-use restriction·관세·희석·신용위험을 통과하는 순간이다.**

* [Reuters](https://www.reuters.com/world/asia-pacific/hanwha-aerospace-drops-plan-acquire-poongsans-defence-unit-2026-04-09/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/korea-zinc-talks-with-us-tech-firms-extract-rare-earths-data-centre-waste-2026-03-12/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/commodities/china-asks-korea-not-export-products-using-rare-earths-us-defense-firms-paper-2025-04-22/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/asia/south-korea-provisionally-slaps-tariffs-chinese-steel-plates-dumping-2025-02-20/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/south-korea-minimise-impact-50-tariff-steel-products-ministry-says-2025-06-02/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/autos-transportation/hyundai-steels-6-bln-us-investment-draws-investor-ire-tests-seouls-tariff-2025-04-22/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/energy/south-korea-petrochemical-overhaul-likely-shut-small-stand-alone-naphtha-2025-08-27/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/south-korea-approves-first-petrochemical-restructuring-deal-supply-glut-weighs-2026-02-24/?utm_source=chatgpt.com)

[1]: https://www.reuters.com/world/asia-pacific/hanwha-seeks-buy-poongsans-ammunition-business-about-11-billion-newspaper-says-2026-04-03/?utm_source=chatgpt.com "Hanwha seeks to buy Poongsan's ammunition business for about $1.1 billion, newspaper says"
[2]: https://www.reuters.com/world/asia-pacific/korea-zinc-talks-with-us-tech-firms-extract-rare-earths-data-centre-waste-2026-03-12/?utm_source=chatgpt.com "Korea Zinc in talks with US tech firms to extract rare earths from data centre waste"
[3]: https://www.reuters.com/markets/commodities/china-asks-korea-not-export-products-using-rare-earths-us-defense-firms-paper-2025-04-22/?utm_source=chatgpt.com "China asks Korea not to export products using rare earths to US defense firms, paper reports"
[4]: https://www.reuters.com/markets/asia/south-korea-provisionally-slaps-tariffs-chinese-steel-plates-dumping-2025-02-20/?utm_source=chatgpt.com "South Korea provisionally slaps tariffs on Chinese steel plates for dumping"
[5]: https://www.reuters.com/markets/commodities/hyundai-steel-build-plant-louisiana-with-annual-output-27-million-tonnes-2025-03-25/?utm_source=chatgpt.com "Hyundai Steel unveils US factory plan, shares skid"
[6]: https://www.reuters.com/business/energy/south-korea-petrochemical-overhaul-likely-shut-small-stand-alone-naphtha-2025-08-27/?utm_source=chatgpt.com "South Korea petrochemical overhaul likely to shut small, stand-alone naphtha crackers"
[7]: https://www.reuters.com/world/asia-pacific/south-korea-approves-first-petrochemical-restructuring-deal-supply-glut-weighs-2026-02-24/?utm_source=chatgpt.com "South Korea approves first petrochemical restructuring deal as supply glut weighs"
[8]: https://www.reuters.com/world/asia-pacific/south-korea-seeks-closer-china-cooperation-secure-critical-mineral-supply-chains-2026-02-05/?utm_source=chatgpt.com "South Korea seeks critical minerals ties with China after joining US trade bloc"
