순서상 이번은 **R10 Loop 12 — 건설·부동산·건자재 가격경로 검증 라운드**다.

```text
round = R10 Loop 12
round_id = round_194
large_sector = CONSTRUCTION_REAL_ESTATE_MATERIALS
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true_for_safety_reference
direct_listed_hard_4c_confirmed = false
```

이번 R10 Loop 12는 지난 R10의 Samsung E&A Fadhili, PF/Taeyoung, SK/AWS data center를 그대로 반복하지 않고, **원전 EPC, 해외 원전 법적 리스크, 교량 붕괴·건설안전, 주택정책, 공공청사, LNG power infra, 건자재 수요 둔화**를 중심으로 다시 본다.

---

# 1. 이번 라운드 대섹터

```text
R10 = 건설·부동산·건자재
```

R10의 Stage 3는 “수주”, “정책”, “공공공사”, “원전”, “주택공급”, “데이터센터”, “건자재 반등”이 아니다.

진짜 Stage 3는 **계약 확정 → 착공·공정률 → 매출인식 → 원가율·마진 → 운전자본 → 현금회수 → 안전·품질·인허가 통과**까지 닫힐 때다.

---

# 2. 대상 canonical archetype

```text
NUCLEAR_EPC_EXPORT_STAGE2
NUCLEAR_EXPORT_LEGAL_4C_WATCH
CONSTRUCTION_SAFETY_HARD_REFERENCE
RECURRING_FATAL_ACCIDENT_REGULATORY_4C
HOUSING_SUPPLY_POLICY_EVENT
PUBLIC_INFRASTRUCTURE_POLICY_EVENT
LNG_POWER_INFRA_CONSORTIUM_OPTION
BUILDING_MATERIALS_DEMAND_BREAK
```

---

# 3. deep sub-archetype

```text
원전 EPC:
- KHNP / Hyundai E&C / Doosan Enerbility / KEPCO E&C
- Czech Dukovany
- Bulgaria Kozloduy
- preferred bidder vs final contract
- Westinghouse / EDF appeal
- contract value, design scope, margin, cash collection

건설 안전:
- Hyundai Engineering Anseong bridge collapse
- POSCO E&C / DL Construction safety regulation
- repeated fatalities
- license revocation / 5% OP fine
- site shutdown / executive resignations

주택·공공정책:
- Seoul LTV tightening
- LH/state-owned land supply
- reconstruction simplification
- Sejong presidential office

해외 LNG / power infra:
- Daewoo E&C consortium candidate
- Vietnam Nghi Son LNG power plant
- project selection before actual EPC contract

건자재:
- Hyundai Steel rebar proxy
- weak construction demand
- rebar price / profit forecast cut
```

---

# 4. 국장 신규 후보 case

## Case A — Czech nuclear / Doosan·KEPCO E&C·Hyundai E&C read-through `success_candidate + legal 4C-watch`

```text
symbols = 034020 / 052690 / 051600 / 000720
case_type = success_candidate + 4C-watch
archetype = NUCLEAR_EPC_EXPORT_STAGE2 / NUCLEAR_EXPORT_LEGAL_4C_WATCH
```

### stage date

```text
Stage 1:
2024-07-17
- KHNP selected as preferred bidder for Czech nuclear project
- first large overseas Korean nuclear order since UAE 2009
- Korea nuclear EPC export revival

Stage 2:
2024-07-17
- two new Czech reactors
- one unit at same site estimated 200B Czech crowns / $8.65B
- two-unit implied project size roughly $17.3B
- Reuters also cites legal/project context up to about $18B
- Doosan Enerbility +48% over three months
- KEPCO Plant S&E +14% over three months
- KEPCO E&C +41% over three months

Stage 4C-watch:
2024-08-27 / 2024-10-30 / 2025-05-06
- EDF / Westinghouse appeal
- Czech anti-monopoly office temporarily blocks contract signing
- later Czech court halted $18B contract signing after EDF complaint

Stage 3:
없음
- preferred bidder는 Stage 2
- final contract, scope split, margin, schedule, cash collection, legal clearance 전 Green 금지
```

Czech 원전은 R10에서 가장 강한 Stage 2 후보지만, 동시에 legal 4C-watch다. Reuters는 KHNP가 Czech 신규 원전 2기 preferred bidder로 선정됐고, Doosan Enerbility가 3개월 +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% 올랐다고 보도했다. 다만 final contract는 협상 대상이었고, 이후 EDF·Westinghouse 이의제기와 Czech court halt가 발생했기 때문에, Stage 3로 올리면 안 된다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP project and reported equity-return anchors

stage3_price:
N/A

project_anchor:
Czech new nuclear units

unit_cost_same_site:
200B Czech crowns / $8.65B

two_unit_implied_value:
$17.3B

court_halt_project_value_context:
$18B

Doosan_Enerbility_3M_MFE:
+48%

KEPCO_Plant_SE_3M_MFE:
+14%

KEPCO_EC_3M_MFE:
+41%

Doosan_vs_KEPCO_EC_spread:
48 - 41
= +7pp

Doosan_vs_KEPCO_Plant_SE_spread:
48 - 14
= +34pp

Stage_4C_before_hard_damage:
partial_success
- legal appeal was identifiable before final contract.
- price had already moved on preferred-bid evidence.

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_legal_4C_watch
rerating_result = nuclear_EPC_export_stage2
stage_failure_type = preferred_bidder_not_final_contract_green
```

---

## Case B — Hyundai E&C / Bulgaria Kozloduy `success_candidate, insufficient price data`

```text
symbol = 000720
case_type = success_candidate + insufficient_price_data
archetype = NUCLEAR_EPC_EXPORT_STAGE2
```

### stage date

```text
Stage 1:
2024-02-23
- Bulgaria parliament approves Hyundai E&C talks
- Kozloduy nuclear reactors
- Korean nuclear construction export pipeline

Stage 2:
2024-02-23
- Hyundai E&C approved to discuss construction of two reactors
- planned additional capacity 2,300MW
- Unit 7 expected by 2033
- Hyundai outbid Bechtel

Stage 3:
없음
- parliament nod / talks are not final contract
- EPC value, scope, margin, financing, payment schedule 확인 필요

Stage 4B:
nuclear export headline로 Hyundai E&C price가 먼저 움직이면 watch

Stage 4C:
Bulgaria political delay, financing, licensing, Westinghouse/IP issue, execution risk
```

Bulgaria Kozloduy는 Hyundai E&C의 원전 EPC option이지만 아직 Stage 3는 아니다. Reuters는 Bulgaria parliament가 Hyundai E&C와 원전 2기 건설 협상을 승인했고, 신규 원전이 2,300MW를 더할 수 있으며 Unit 7 완공 목표가 2033년이라고 보도했다. 하지만 협상 승인과 final EPC contract는 다르다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters project anchor

stage3_price:
N/A

new_reactors:
2

additional_capacity:
2,300MW

average_capacity_per_reactor:
2,300 / 2
= 1,150MW

Unit_7_completion_target:
2033

bid_context:
Hyundai outbid Bechtel

Hyundai_EC_OHLC:
price_data_unavailable_after_deep_search

reason:
- Reuters source gives project and approval evidence.
- No reliable adjusted OHLC/event price anchor found in this pass.
```

### alignment

```text
score_price_alignment = success_candidate_but_insufficient_price_data
rerating_result = nuclear_EPC_pipeline_watch
stage_failure_type = talks_not_contract
```

---

## Case C — Hyundai Engineering / Anseong bridge collapse `construction safety hard reference`

```text
direct_company = Hyundai Engineering, unlisted
listed_readthrough = Hyundai Motor Group / Hyundai E&C / construction safety basket
case_type = 4C-thesis-break reference
archetype = CONSTRUCTION_SAFETY_HARD_REFERENCE
```

### stage date

```text
Stage 1:
2025-02-25
- Sejong-Pocheon expressway / Anseong highway construction collapse
- bridge deck / support structure collapse
- construction safety trust shock

Stage 4C:
2025-02-25
- Reuters: at least 3 dead, 6 injured
- AP: 4 workers killed, 6 injured
- five 50m support structures collapsed sequentially
- authorities dispatched transport ministry officials
- AP and Washington Post context identify Hyundai Engineering as contractor / site manager

Stage 3:
N/A
```

Anseong bridge collapse는 direct listed price가 없더라도 R10 safety hard reference로 넣어야 한다. Reuters는 highway construction site에서 50m support structures가 연쇄 붕괴해 최소 3명이 사망하고 6명이 다쳤다고 보도했고, AP는 사망자를 4명으로 업데이트했다. 별도 보도들은 Hyundai Engineering이 현장 책임자로 조사를 받는 맥락을 제시했다. 이는 건설사의 “공사 수주”보다 safety execution이 먼저라는 기준점이다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP / Washington Post construction-collapse anchors

stage3_price:
N/A

direct_listed_ticker:
N/A

fatalities:
Reuters at least 3
AP 4

injured:
6

support_structures:
five 50m structures

collapse_type:
sequential collapse during bridge construction

listed_price_path:
price_data_unavailable_after_deep_search

reason:
- Hyundai Engineering is not directly listed.
- This is used as R10 sector hard reference, not direct KRX price row.
```

### alignment

```text
score_price_alignment = thesis_break_reference
rerating_result = construction_safety_hard_reference
stage_failure_type = unlisted_but_sector_4C_reference
```

---

## Case D — POSCO E&C / DL Construction safety regulation `4C-watch`

```text
listed_readthrough = construction basket / POSCO group / DL group exposure
case_type = 4C-watch
archetype = RECURRING_FATAL_ACCIDENT_REGULATORY_4C
```

### stage date

```text
Stage 1:
2025
- construction fatalities persist
- workplace safety crackdown under Lee administration
- subcontractor responsibility and repeated-fatality regulation

Stage 4C-watch:
2025-09-15
- companies with >3 worker deaths/year may face fines up to 5% of operating profit
- construction firms repeatedly ordered to suspend work after fatal accidents may lose licenses
- 2024 workplace deaths: 589, nearly half in construction

Stage 4C-watch validation:
2025-11-16
- nearly 80 DL Construction executives tendered resignations after death at construction site
- POSCO, DL and Hanwha resumed operations/construction after safety measures
```

R10 safety score는 일반 ESG가 아니라 hard gate다. Reuters는 South Korea가 반복 사망사고 기업에 영업이익 최대 5% 벌금과 건설사 면허취소 가능성을 추진한다고 보도했다. 또 2024년 산업재해 사망자 589명 중 거의 절반이 건설업이고, DL Construction 임원 약 80명이 현장 사망사고 후 사의를 냈다고 보도했다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters safety-regulation / company-response anchors

stage3_price:
N/A

proposed_fine:
up to 5% of operating profit

license_revocation_risk:
true

workplace_deaths_2024:
589

construction_share:
nearly half

implied_construction_deaths:
about 589 * 0.5
= about 295

DL_executives_resigned:
about 80

direct_OHLC:
price_data_unavailable_after_deep_search

MFE:
N/A

MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = recurring_fatal_accident_regulatory_watch
stage_failure_type = safety_4C_watch_not_green
```

---

## Case E — Seoul housing supply / LTV tightening `policy event, not Green`

```text
symbol = housing_construction_basket
case_type = event_premium / policy_watch
archetype = HOUSING_SUPPLY_POLICY_EVENT
```

### stage date

```text
Stage 1:
2025-09-07
- Seoul housing shortage
- mortgage demand control
- state-owned land supply
- reconstruction-rule simplification

Stage 2:
2025-09-07
- Gangnam / Yongsan LTV 50% → 40%
- affordable housing supply expansion
- state-run land including LH used for development
- apartment reconstruction rules streamlined

Stage 3:
없음
- housing policy is not construction-stock Green
- presales, margin, unsold inventory, PF stability, FCF 필요

Stage 4B:
정책 headline으로 건설주가 먼저 오르면 watch

Stage 4C:
LTV demand shock, unsold inventory, PF refinancing, construction-cost inflation
```

Seoul housing policy는 공급과 수요억제가 같이 붙는다. LTV를 50%에서 40%로 낮추는 것은 수요를 누르는 정책이고, LH 등 state-run land 활용과 재건축 간소화는 공급확대 정책이다. 건설주 Green은 이 정책이 실제 분양률·마진·PF 안정으로 연결될 때다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters housing-policy anchor

stage3_price:
N/A

LTV_before:
50%

LTV_after:
40%

LTV_change_absolute:
-10pp

LTV_change_relative:
40 / 50 - 1
= -20%

policy_supply_tools:
state-owned land / LH land
reconstruction-rule streamlining
affordable housing supply

housing_basket_OHLC:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium_policy_watch
rerating_result = housing_supply_policy_watch
stage_failure_type = policy_not_presales_margin_green
```

---

## Case F — Sejong presidential office `public infra headline, not Green`

```text
symbol = public_construction_basket
case_type = event_premium / insufficient_evidence
archetype = PUBLIC_INFRASTRUCTURE_POLICY_EVENT
```

### stage date

```text
Stage 1:
2026-04-14
- Sejong presidential office project
- public construction / regional development narrative

Stage 2:
2026-04-14
- construction to begin August 2027
- site area about 350,000㎡
- site preparation cost 9.8B won / $6.6M
- construction period about 14 months
- tender notice for site construction

Stage 3:
없음
- public infra headline is too small / too early for listed construction Green
- contractor award, contract value, margin, cash collection 필요

Stage 4B:
Sejong / public-infra theme로 price가 먼저 움직이면 watch
```

Sejong presidential office는 public-construction headline이지만 Green은 아니다. Reuters는 site area가 약 350,000㎡, site preparation cost가 98억 원, construction period가 약 14개월이라고 보도했다. listed construction company stage를 주려면 실제 낙찰사와 계약금액·마진이 필요하다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters public-infrastructure policy anchor

stage3_price:
N/A

site_area:
350,000㎡

site_preparation_cost:
9.8B won / $6.6M

site_preparation_cost_per_sqm:
9.8B / 350,000
= 28,000 won/㎡

construction_period:
about 14 months

construction_start_target:
August 2027

listed_contract_winner:
not disclosed

OHLC:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium_insufficient_evidence
rerating_result = public_infra_headline_watch
stage_failure_type = no_listed_contract_no_green
```

---

## Case G — Daewoo E&C / Vietnam Nghi Son LNG candidate `success_candidate, insufficient_evidence`

```text
symbol = 047040
case_type = success_candidate + insufficient_evidence
archetype = LNG_POWER_INFRA_CONSORTIUM_OPTION
```

### stage date

```text
Stage 1:
2024-08-21
- Vietnam Nghi Son LNG power plant
- South Korean consortium candidate
- LNG terminal / storage / regasification infra

Stage 2:
2024-08-21
- project value $2.5B
- designed capacity 1.5GW
- commercial operation target 2030
- five consortiums potentially include Korea Southern Power, KOGAS, Daewoo E&C, Gulf Energy, SK E&S

Stage 3:
없음
- potential candidate is not awarded contract
- investor selection, EPC scope, margin, financing, offtake 확인 필요

Stage 4B:
Vietnam LNG / power-infra headline로 price가 먼저 움직이면 watch
```

Nghi Son LNG는 Daewoo E&C의 potential Stage 2 option이지만, 아직 Green은 아니다. Reuters는 Vietnam Thanh Hoa province가 $2.5B, 1.5GW LNG power project 투자자를 선정할 예정이고, 후보 consortium에 Korea Southern Power, KOGAS, Daewoo E&C, SK E&S 등이 포함될 수 있다고 보도했다. 그러나 후보군과 award는 다르다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters Vietnam LNG power project anchor

stage3_price:
N/A

project_value:
$2.5B

capacity:
1.5GW

project_value_per_GW:
2.5 / 1.5
= $1.67B/GW

commercial_operation_target:
2030

potential_Korean_participants:
Korea Southern Power
KOGAS
Daewoo E&C
SK E&S

award_status:
not confirmed in source

Daewoo_EC_OHLC:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_but_insufficient_evidence
rerating_result = LNG_power_infra_consortium_option
stage_failure_type = candidate_not_award
```

---

## Case H — Hyundai Steel / rebar construction-demand proxy `building-material 4C-watch`

```text
symbol = 004020
case_type = 4C-watch
archetype = BUILDING_MATERIALS_DEMAND_BREAK
```

### stage date

```text
Stage 1:
2024-06-21
- construction demand weakness
- rebar price weakness
- shipbuilding steel-plate competition

Stage 4C-watch:
2024-06-21
- Nomura cuts 2024 net-profit forecast by 73% to 215B won
- target price -14% to 30,000 won
- shares -1.2% to 29,000 won
- rebar price expected -10% in 2024

Stage 3:
없음
- building-material Green requires construction demand recovery, spread, inventory, FCF
```

Hyundai Steel은 R10 건자재 demand-break proxy로 둔다. Nomura는 construction and shipbuilding demand weakness 때문에 2024년 순이익 전망을 73% 낮춰 2,150억 원으로 조정했고, rebar price가 2024년 10% 하락할 수 있다고 봤다. 이는 건설경기 부진이 건자재로 전이되는 4C-watch다. ([마켓워치][8])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch / Dow Jones Market Talk reported price and estimate anchor

stage3_price:
N/A

event_price:
29,000 won

event_MAE:
-1.2%

implied_pre_event_reference_price:
29,000 / (1 - 0.012)
= about 29,352 won

target_price:
30,000 won

target_cut:
-14%

implied_prior_target:
30,000 / (1 - 0.14)
= about 34,884 won

target_upside_from_event_price:
30,000 / 29,000 - 1
= +3.45%

2024_net_profit_forecast:
215B won

net_profit_forecast_cut:
-73%

implied_prior_net_profit_forecast:
215B / (1 - 0.73)
= about 796.3B won

expected_rebar_price_decline:
-10%

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = building_materials_demand_break
stage_failure_type = demand_spread_not_green
```

---

# 5. 이번 R10 case별 요약표

| case                                 | 분류                               |                                                              실제 가격검증 | alignment              |
| ------------------------------------ | -------------------------------- | -------------------------------------------------------------------: | ---------------------- |
| Czech nuclear / Doosan·KEPCO E&C     | success_candidate + 4C-watch     | Doosan +48%, KEPCO E&C +41%, KEPCO Plant +14%, later $18B legal halt | nuclear Stage 2        |
| Hyundai E&C Bulgaria                 | success_candidate / insufficient |                                  2 reactors, 2,300MW, Unit 7 by 2033 | talks not contract     |
| Hyundai Engineering Anseong collapse | hard reference                   |                       3~4 deaths, 6 injuries, direct listed OHLC N/A | safety hard reference  |
| POSCO E&C / DL safety                | 4C-watch                         |     5% OP fine risk, license revocation, 589 deaths, 80 resignations | safety regulation      |
| Seoul housing policy                 | event premium                    |                             LTV 50%→40%, -20% relative borrowing cap | policy not Green       |
| Sejong presidential office           | event / insufficient             |                              350,000㎡, 9.8B won prep cost, 14 months | no listed contract     |
| Daewoo E&C Nghi Son LNG              | success_candidate / insufficient |                                         $2.5B, 1.5GW, candidate only | not awarded            |
| Hyundai Steel rebar                  | 4C-watch                         |                         29,000원, -1.2%, NP forecast -73%, rebar -10% | materials demand break |

---

# 6. score-price alignment 판정

```text
success_candidate:
- Czech nuclear read-through
- Hyundai E&C Bulgaria
- Daewoo E&C Nghi Son LNG candidate

event_premium:
- Seoul housing policy
- Sejong presidential office
- Czech nuclear preferred-bid rally if price moves before final contract

price_moved_without_evidence:
- nuclear rally before final EPC contract / margin
- public-infra theme before listed contract award
- housing-policy rally before presales / margin / PF stability

thesis_break_watch:
- POSCO E&C / DL safety regulation
- Hyundai Steel rebar construction-demand weakness
- Czech nuclear legal appeal risk

hard_reference:
- Hyundai Engineering Anseong bridge collapse

hard_4C_confirmed:
- direct listed hard 4C not confirmed
- sector hard safety reference confirmed
```

---

# 7. 점수비중 교정

## 올릴 축

```text
final_contract_signed +5
progress_revenue_visibility +5
construction_margin_visibility +5
working_capital_control +5
cash_collection_quality +5
safety_execution_trust +5
permit_and_legal_clearance +5
presales_and_unsold_inventory +5
building_material_spread +4
public_contract_award_quality +4
```

### 왜 올리나

Czech nuclear와 Bulgaria는 headline이 강하지만 final contract·legal clearance·scope·margin이 필요하다. Nghi Son LNG도 candidate와 award를 분리해야 한다. Housing policy는 presales·PF stability 없이는 Green이 아니다. Safety cases는 R10에서 가장 강한 hard gate다.

## 내릴 축

```text
preferred_bidder_only -5
talks_or_MOU_only -5
public_infra_headline_only -5
housing_policy_only -5
candidate_consortium_only -5
safety_incident -5
recurring_fatality_risk -5
license_revocation_risk -5
rebar_demand_weakness -4
legal_appeal_pending -4
```

### 왜 내리나

Preferred bidder, talks, candidate consortium, public tender notice는 Stage 2 또는 Stage 1일 뿐이다. Anseong collapse와 recurring fatal-accident regulation은 safety score를 즉시 Red로 돌려야 한다. Hyundai Steel rebar는 건설수요 부진이 건자재 spread로 내려오는 warning이다.

## Green gate 강화 조건

```text
R10 Stage 3-Green 필수:
1. final contract signed
2. scope / value / payment schedule confirmed
3. progress revenue 또는 delivery milestone 확인
4. construction margin / OPM 확인
5. working capital / receivables 안정
6. legal appeal / permit / license risk 해소
7. safety incident 없음
8. presales / unsold inventory / PF stability 확인
9. price path가 evidence 이후 따라옴

금지:
preferred bidder only
talks only
candidate consortium only
public infra headline only
housing policy only
safety incident unresolved
legal appeal pending
building-material demand break
```

## 4B 조기감지 조건

```text
4B-watch:
원전 preferred bidder 뉴스로 +10~40% 선반영
housing supply / reconstruction policy로 건설주 급등
public-infra tender notice로 theme rally
LNG consortium candidate만으로 price rally
안전사고 후 relief bounce가 사고조사 전 과도
건자재 price가 demand 회복 없이 반등

4B-elevated:
final contract 없음
legal appeal pending
contract value/scope 미확정
margin / working capital 미확인
site accident investigation ongoing
PF / unsold inventory unresolved
```

## 4C hard gate 조건

```text
fatal construction collapse
repeated fatal accidents
license revocation
work suspension
major defect / collapse investigation
legal block on project signing
contract cancellation
PF refinancing failure
unsold inventory spike
construction-cost overrun
rebar / cement / materials demand collapse
```

이번 R10 Loop 12에서는 direct listed hard 4C는 확정하지 않는다. 대신 **Anseong bridge collapse를 sector hard safety reference**, **Czech nuclear legal halt를 contract-signing 4C-watch**, **Hyundai Steel rebar weakness를 building-material demand 4C-watch**로 기록한다.

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

## docs/round/round_194.md 요약

```md
# R10 Loop 12. Construction / Real Estate / Building Materials Price Validation

이번 라운드는 R10 Loop 12 price-validation 라운드다.

핵심 결론:
- Czech nuclear read-through is strong Stage 2 plus legal 4C-watch. Doosan Enerbility +48%, KEPCO E&C +41%, KEPCO Plant S&E +14% over three months after KHNP was selected as preferred bidder. But appeals and later court halt on the $18B contract block Green.
- Hyundai E&C Bulgaria Kozloduy is nuclear EPC Stage 2. Talks approved for two reactors adding 2,300MW, with Unit 7 targeted by 2033. But talks are not final contract.
- Hyundai Engineering Anseong bridge collapse is sector hard safety reference. Reuters reported at least 3 deaths and AP later reported 4 deaths. Hyundai Engineering is not directly listed, so this is a sector 4C reference rather than direct KRX price row.
- POSCO E&C / DL safety regulation is 4C-watch. Repeated fatal accidents may trigger fines up to 5% of operating profit and construction license revocation. 2024 workplace deaths were 589, nearly half in construction.
- Seoul housing policy is event premium / policy watch. LTV in Gangnam/Yongsan falls from 50% to 40%, while LH/state land and reconstruction simplification aim to boost supply. Presales, margin, PF stability and FCF required.
- Sejong presidential office is public-infra headline, not Green. Site area 350,000㎡, prep cost 9.8B won, construction period 14 months, but no listed contractor or contract value yet.
- Daewoo E&C / Nghi Son LNG is consortium-option Stage 2. Project value $2.5B, capacity 1.5GW, commercial operation target 2030, but Daewoo is only a potential candidate in source.
- Hyundai Steel rebar proxy is building-material demand 4C-watch. Shares 29,000 won, -1.2%; net-profit forecast cut 73% to 215B won; rebar price expected -10%.
```

## docs/checkpoints/checkpoint_28a_round194_r10_loop12.md 요약

```md
# Checkpoint 28A Round 194 R10 Loop 12 Construction Real Estate Materials Price Validation

## 반영 내용
- R10 Loop 12 price-validation 라운드를 추가했다.
- Nuclear EPC preferred-bid, Bulgaria nuclear talks, construction safety collapse, recurring fatal-accident regulation, housing policy, public infrastructure, Vietnam LNG power candidate, rebar demand break를 비교했다.
- Reuters / AP / MarketWatch anchors로 가능한 MFE/MAE 및 event metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- final contract signed, progress revenue, construction margin, working capital, cash collection, safety execution trust, legal clearance, presales/unsold inventory, building-material spread 가중치 강화
- preferred bidder-only, talks-only, public-infra headline-only, housing policy-only, candidate consortium-only, safety incident, license revocation risk, legal appeal pending 감점 강화
```

## data/e2r_case_library/cases_r10_loop12_round194.jsonl 초안

```jsonl
{"case_id":"r10_loop12_czech_nuclear_preferred_bid_legal_watch","symbol":"034020/052690/051600/000720","company_name":"Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E / Hyundai E&C read-through","case_type":"success_candidate","primary_archetype":"NUCLEAR_EPC_EXPORT_STAGE2","stage2_date":"2024-07-17","stage4c_date":"2024-08-27/2024-10-30/2025-05_watch","price_validation":{"price_data_source":"Reuters/AP project and reported equity-return anchors","stage3_price":null,"unit_cost_same_site_czk_bn":200,"unit_cost_same_site_usd_bn":8.65,"two_unit_implied_value_usd_bn":17.3,"court_halt_project_value_context_usd_bn":18,"doosan_enerbility_3m_mfe_pct":48,"kepco_plant_se_3m_mfe_pct":14,"kepco_ec_3m_mfe_pct":41,"doosan_vs_kepco_ec_spread_pp":7,"doosan_vs_kepco_plant_spread_pp":34,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_legal_4C_watch","rerating_result":"nuclear_EPC_export_stage2","notes":"Preferred bidder is Stage 2; final contract, legal clearance, scope, margin and cash collection required before Green."}
{"case_id":"r10_loop12_hyundai_ec_bulgaria_kozloduy_talks","symbol":"000720","company_name":"Hyundai E&C","case_type":"success_candidate","primary_archetype":"NUCLEAR_EPC_EXPORT_STAGE2","stage2_date":"2024-02-23","price_validation":{"price_data_source":"Reuters Bulgaria nuclear talks anchor","stage3_price":null,"new_reactors":2,"additional_capacity_mw":2300,"average_capacity_per_reactor_mw":1150,"unit7_completion_target":2033,"bid_context":"Hyundai outbid Bechtel","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_insufficient_price_data","rerating_result":"nuclear_EPC_pipeline_watch","notes":"Parliament nod and talks are Stage 2; final EPC value, scope, margin, financing and payment schedule required."}
{"case_id":"r10_loop12_hyundai_engineering_anseong_bridge_collapse","symbol":"unlisted_Hyundai_Engineering/construction_safety_basket","company_name":"Hyundai Engineering / Anseong bridge collapse","case_type":"4c_reference","primary_archetype":"CONSTRUCTION_SAFETY_HARD_REFERENCE","stage4c_date":"2025-02-25","price_validation":{"price_data_source":"Reuters/AP/Washington Post construction-collapse anchors","stage3_price":null,"direct_listed_ticker":"N/A","fatalities_reuters":"at least 3","fatalities_ap":4,"injured":6,"support_structures":"five 50m structures","collapse_type":"sequential collapse during bridge construction","price_validation_status":"unlisted_sector_reference"},"score_price_alignment":"thesis_break_reference","rerating_result":"construction_safety_hard_reference","notes":"Fatal collapse is sector hard 4C reference; Hyundai Engineering is not directly listed."}
{"case_id":"r10_loop12_posco_dl_recurring_fatal_accident_regulation","symbol":"construction_safety_basket","company_name":"POSCO E&C / DL Construction safety read-through","case_type":"4c_watch","primary_archetype":"RECURRING_FATAL_ACCIDENT_REGULATORY_4C","stage4c_date":"2025-09-15/2025-11-16_watch","price_validation":{"price_data_source":"Reuters safety-regulation/company-response anchors","stage3_price":null,"proposed_fine_pct_of_operating_profit":5,"license_revocation_risk":true,"workplace_deaths_2024":589,"construction_share":"nearly_half","implied_construction_deaths_approx":295,"dl_executives_resigned":80,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"recurring_fatal_accident_regulatory_watch","notes":"Repeated fatality regulation is 4C-watch; safety execution must override backlog and policy-score."}
{"case_id":"r10_loop12_seoul_housing_ltv_supply_policy","symbol":"housing_construction_basket","company_name":"Seoul housing policy / construction basket","case_type":"event_premium","primary_archetype":"HOUSING_SUPPLY_POLICY_EVENT","stage2_date":"2025-09-07","price_validation":{"price_data_source":"Reuters housing-policy anchor","stage3_price":null,"ltv_before_pct":50,"ltv_after_pct":40,"ltv_change_pp":-10,"ltv_change_relative_pct":-20,"policy_supply_tools":["state-owned land / LH land","reconstruction-rule streamlining","affordable housing supply"],"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_policy_watch","rerating_result":"housing_supply_policy_watch","notes":"Policy mix is Stage 2; presales, margin, PF stability, unsold inventory and FCF required before Green."}
{"case_id":"r10_loop12_sejong_presidential_office_public_infra","symbol":"public_construction_basket","company_name":"Sejong presidential office public-infra basket","case_type":"event_premium","primary_archetype":"PUBLIC_INFRASTRUCTURE_POLICY_EVENT","stage2_date":"2026-04-14","price_validation":{"price_data_source":"Reuters public-infrastructure policy anchor","stage3_price":null,"site_area_sqm":350000,"site_preparation_cost_krw_bn":9.8,"site_preparation_cost_usd_mn":6.6,"site_preparation_cost_per_sqm_krw":28000,"construction_period_months":14,"construction_start_target":"2027-08","listed_contract_winner":"not_disclosed","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_insufficient_evidence","rerating_result":"public_infra_headline_watch","notes":"Public-infra headline is not Green without listed contractor, contract value, margin and cash collection."}
{"case_id":"r10_loop12_daewoo_ec_nghi_son_lng_candidate","symbol":"047040","company_name":"Daewoo E&C / Nghi Son LNG candidate","case_type":"success_candidate","primary_archetype":"LNG_POWER_INFRA_CONSORTIUM_OPTION","stage1_date":"2024-08-21","price_validation":{"price_data_source":"Reuters Vietnam LNG power project anchor","stage3_price":null,"project_value_usd_bn":2.5,"capacity_gw":1.5,"project_value_per_gw_usd_bn":1.67,"commercial_operation_target":2030,"potential_korean_participants":["Korea Southern Power","KOGAS","Daewoo E&C","SK E&S"],"award_status":"not confirmed in source","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_insufficient_evidence","rerating_result":"LNG_power_infra_consortium_option","notes":"Consortium candidate is not award; EPC scope, value, margin, financing and offtake required before Green."}
{"case_id":"r10_loop12_hyundai_steel_rebar_construction_demand_break","symbol":"004020","company_name":"Hyundai Steel / rebar proxy","case_type":"4c_watch","primary_archetype":"BUILDING_MATERIALS_DEMAND_BREAK","stage4c_date":"2024-06-21","price_validation":{"price_data_source":"MarketWatch/Dow Jones Market Talk price and estimate anchor","stage3_price":null,"event_price_krw":29000,"event_mae_pct":-1.2,"implied_pre_event_reference_price_krw":29352,"target_price_krw":30000,"target_cut_pct":-14,"implied_prior_target_krw":34884,"target_upside_from_event_price_pct":3.45,"net_profit_forecast_2024_krw_bn":215,"net_profit_forecast_cut_pct":-73,"implied_prior_net_profit_forecast_krw_bn":796.3,"expected_rebar_price_decline_pct":-10,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"building_materials_demand_break","notes":"Weak construction demand and rebar-price decline block building-material Green until spread, inventory and FCF recover."}
```

## data/sector_taxonomy/score_weight_profiles_round194_r10_loop12_v1.csv 초안

```csv
archetype,final_contract_signed,progress_revenue,construction_margin,working_capital,cash_collection,safety_execution,legal_clearance,presales_unsold_pf,building_material_spread,public_contract_quality,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
NUCLEAR_EPC_EXPORT_STAGE2,+5,+5,+5,+5,+5,+4,+5,+0,+0,+4,-5,+5,+5,Czech/Bulgaria nuclear is Stage 2 until final contract and legal clearance confirm.
NUCLEAR_EXPORT_LEGAL_4C_WATCH,+0,+0,+0,+0,+0,+2,+5,+0,+0,+0,0,+4,+5,EDF/Westinghouse/Czech court halt requires legal 4C-watch.
CONSTRUCTION_SAFETY_HARD_REFERENCE,+0,+0,+0,+0,+0,+5,+2,+0,+0,+0,0,+3,+5,Anseong bridge collapse is sector hard safety reference.
RECURRING_FATAL_ACCIDENT_REGULATORY_4C,+0,+0,+0,+0,+0,+5,+5,+0,+0,+0,0,+4,+5,Recurring fatalities can trigger 5% OP fine and license revocation.
HOUSING_SUPPLY_POLICY_EVENT,+2,+2,+3,+4,+4,+2,+3,+5,+1,+2,-5,+5,+4,Housing policy requires presales, margin, PF stability and FCF.
PUBLIC_INFRASTRUCTURE_POLICY_EVENT,+3,+3,+3,+3,+3,+3,+3,+0,+0,+5,-5,+4,+3,Public-infra headline needs listed award, contract value and margin.
LNG_POWER_INFRA_CONSORTIUM_OPTION,+4,+4,+4,+4,+4,+3,+4,+0,+0,+4,-5,+4,+4,Consortium candidate is not award; EPC scope/value/offtake required.
BUILDING_MATERIALS_DEMAND_BREAK,+0,+0,+0,+4,+4,+2,+0,+3,+5,+0,0,+3,+5,Rebar/construction demand weakness requires spread/inventory/FCF watch.
```

---

# 이번 R10 Loop 12 결론

```text
1. Czech nuclear는 강한 Stage 2지만 Green은 아니다.
   preferred bidder 후 price가 움직였고, legal halt가 뒤따랐으므로 final contract / legal clearance gate를 강화해야 한다.

2. Hyundai E&C Bulgaria는 원전 EPC pipeline Stage 2다.
   talks와 parliament nod는 final contract가 아니다.

3. Anseong bridge collapse는 unlisted지만 R10 sector hard safety reference다.
   fatal collapse는 수주·정책 점수를 즉시 덮어야 한다.

4. POSCO E&C / DL safety regulation은 4C-watch다.
   5% OP fine과 license revocation risk는 R10 hard gate 후보다.

5. Seoul housing policy는 event premium이다.
   LTV tightening과 supply expansion이 같이 있어 presales/margin/PF 확인 전 Green 금지다.

6. Sejong presidential office는 public-infra headline이다.
   listed contractor와 contract value가 없으므로 Stage 3가 아니다.

7. Daewoo E&C Nghi Son LNG는 consortium option이다.
   candidate와 award를 분리해야 한다.

8. Hyundai Steel rebar proxy는 building-material demand 4C-watch다.
   건설수요 부진이 rebar price와 profit forecast로 내려온 case다.
```

한 문장으로 압축하면:

> **R10에서 진짜 Stage 3는 “원전·주택정책·공공공사·LNG·건자재 테마가 있다”가 아니라, final contract·공정률·마진·운전자본·현금회수·안전·법적 리스크가 실제로 통과되는 순간이다.**

[1]: https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/?utm_source=chatgpt.com "South Korea's winning bid for Czech nuclear power project"
[2]: https://www.reuters.com/business/energy/hyundai-wins-bulgaria-parliament-nod-nuclear-reactor-talks-2024-02-23/?utm_source=chatgpt.com "Hyundai wins Bulgaria parliament nod for nuclear reactor talks"
[3]: https://www.reuters.com/world/asia-pacific/three-people-dead-five-hurt-south-korea-highway-construction-site-yonhap-says-2025-02-25/?utm_source=chatgpt.com "At least three dead in South Korea highway construction project collapse"
[4]: https://www.reuters.com/sustainability/sustainable-finance-reporting/south-korea-fine-companies-up-5-profit-recurring-fatal-accidents-ministry-says-2025-09-15/?utm_source=chatgpt.com "South Korea to fine companies up to 5% of profit for recurring fatal accidents, ministry says"
[5]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-tighten-mortgage-rules-seoul-boost-housing-supply-2025-09-07/?utm_source=chatgpt.com "South Korea to tighten mortgage rules in Seoul, boost housing supply"
[6]: https://www.reuters.com/world/asia-pacific/south-korea-start-building-sejong-presidential-office-august-2027-2026-04-14/?utm_source=chatgpt.com "South Korea to start building Sejong presidential office in August 2027"
[7]: https://www.reuters.com/business/energy/vietnam-select-investor-25-bln-nghi-son-lng-power-plant-by-october-2024-08-21/?utm_source=chatgpt.com "Vietnam to select investor for $2.5 bln Nghi Son LNG power plant by October"
[8]: https://www.marketwatch.com/story/hyundai-steel-s-2024-earnings-could-be-hit-by-weak-demand-market-talk-bcbe77c8?utm_source=chatgpt.com "Hyundai Steel's 2024 Earnings Could Be Hit by Weak Demand -- Market Talk"
