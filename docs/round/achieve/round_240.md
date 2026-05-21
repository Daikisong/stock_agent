순서상 이번은 **R10 Loop 10 — 건설·부동산·건자재 가격경로 검증 라운드**다.

이번 R10은 기존의 Fadhili/Jafurah EPC만 반복하지 않고, **원전 인프라 수주, 항만 인프라 준공, 서울 주택정책, PF 구조조정, 건설 안전사고, AI 데이터센터 real asset, 건자재 수요 약화**를 같이 본다.

```text
round = R10 Loop 10
round_id = round_168
large_sector = CONSTRUCTION_REAL_ESTATE_MATERIALS
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
```

이번 환경에서는 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC를 안정적으로 직접 확보하지 못했다. 대신 Reuters / AP / MarketWatch / Washington Post가 제공한 **가격 anchor, 이벤트 수익률, 계약금액, 정책금액, 사고·규제 지표**로 계산 가능한 값만 계산했다.

---

# 1. 이번 라운드 대섹터

```text
R10 = 건설·부동산·건자재
```

R10의 Stage 3는 “수주가 있다”, “정책이 있다”, “개발계획이 있다”가 아니다. **수주·자산·개발계획이 마진·현금회수·NOI/AFFO·PF 안정·안전신뢰로 닫히는 순간**이다.

---

# 2. 대상 canonical archetype

```text
NUCLEAR_INFRA_EPC_EXPORT
PORT_INFRA_DELIVERY
HOUSING_POLICY_SUPPLY_EVENT
REAL_ESTATE_PF_CREDIT_BREAK
CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C
WORKPLACE_FATALITY_REGULATORY_4C
AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT
BUILDING_MATERIALS_DEMAND_CYCLE
PRICE_ONLY_POLICY_RALLY
EVIDENCE_GOOD_BUT_PRICE_UNPROVEN
```

---

# 3. deep sub-archetype

```text
원전 인프라:
- KHNP / KEPCO / Doosan Enerbility / KEPCO E&C
- Czech Dukovany nuclear project
- preferred bidder → court block → signed deal
- contract value vs actual subcontract / margin / working capital

항만 인프라:
- Daewoo E&C
- Iraq Grand Faw Port
- five docks handed over
- operation begins 2026, 3.5M container capacity by 2028
- infrastructure delivery vs new revenue backlog

주택정책:
- Seoul housing supply
- LTV tightening 50% → 40%
- reconstruction simplification
- state-owned land development
- policy event vs company-level presales / margin / FCF

PF:
- Taeyoung / construction PF basket
- delinquency 0.37% → 2.70%
- 1T syndicated loan expandable to 5T
- liquidity support is not Green

건설안전:
- Hyundai Engineering highway bridge collapse
- POSCO E&C site shutdowns
- DL Construction executive resignations
- fatal-accident fine up to 5% operating profit
- license revocation risk

데이터센터 real asset:
- SK/AWS Ulsan AI data center
- OpenAI / Samsung SDS / SK Telecom data centers
- Samsung C&T / Samsung Heavy floating data centers
- tenant / power / water / capex per share before Green

건자재:
- Hyundai Steel rebar proxy
- construction demand weakness
- rebar price decline
- net profit estimate cut
```

---

# 4. 국장 신규 후보 case

## Case A — Czech nuclear infra / Doosan Enerbility·KEPCO E&C `success_candidate + legal-delay watch`

```text
symbols = 034020 / 052690 / 051600 / 015760
case_type = success_candidate + legal_watch
archetype = NUCLEAR_INFRA_EPC_EXPORT
```

### stage date

```text
Stage 1:
2024-07-17
- KHNP selected as preferred bidder for Czech Dukovany reactors
- South Korea’s first large-scale overseas nuclear order since 2009
- related nuclear EPC names rally

Stage 2:
2025-06-04
- Czech government signs contract with KHNP after court clears signing
- two new Dukovany reactors
- total cost 407B koruna / $18.7B
- first trial operation expected 2036, second around 2038

Stage 3:
없음
- KHNP contract signing 자체는 Stage 2
- Doosan / KEPCO E&C / KEPCO Plant S&E의 실제 package amount, margin, cashflow 확인 전 Green 금지

Stage 4B:
preferred-bidder 뉴스 후 관련주가 이미 크게 오른 구간

Stage 4C-watch:
2025-05-06
- Czech court temporarily blocked signing after EDF complaint
- legal challenge / localization / contract finalization risk
```

KHNP가 2024년 7월 Czech Dukovany 원전 2기 우선협상대상자로 선정되자 두산에너빌리티, 한전기술, 한전KPS 같은 관련주가 이미 큰 폭으로 올랐다. Reuters는 당시 두산에너빌리티가 3개월 동안 48%, 한전KPS가 14%, 한전기술이 41% 올랐다고 보도했다. 이후 2025년 5월 EDF 소송으로 계약 서명이 잠시 막혔지만, 2025년 6월 Czech 정부와 KHNP는 법원 판단 이후 407B koruna, 약 187억 달러 규모의 2기 계약을 체결했다. 즉 이건 강한 Stage 2지만, 상장사별 실제 수주·마진·현금흐름 전 Stage 3는 아니다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP nuclear-contract and sector-return anchors

stage3_price:
N/A

related_stock_reported_3M_MFE_before_2024-07-17:
Doosan Enerbility +48%
KEPCO Plant S&E +14%
KEPCO E&C +41%

Czech_contract_value:
407B koruna / $18.7B

Reuters_prior_contract_expectation:
at least 400B crowns / $17.56B

reactors:
2 new Dukovany units

unit_cost_context_2024:
200B crowns / $8.65B per unit when building two at same site

trial_operation_expected:
first reactor 2036
second reactor around 2038

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

reason:
- Reuters/AP give sector/event returns and contract value, not raw OHLC for each Korean listed supplier.
- KRX/Naver/Yahoo/Stooq raw OHLC unavailable in this pass.
```

### alignment

```text
score_price_alignment = success_candidate + legal_watch
rerating_result = nuclear_EPC_export_watch
stage_failure_type = stage2_watch_success_not_green
```

---

## Case B — Daewoo E&C / Iraq Grand Faw Port `success_candidate / infrastructure delivery`

```text
symbol = 047040
case_type = success_candidate
archetype = PORT_INFRA_DELIVERY
```

### stage date

```text
Stage 1:
2023~2024
- Iraq Development Road
- Grand Faw Port infrastructure
- Middle East-Europe logistics corridor

Stage 2:
2024-11-12
- Daewoo E&C completed five docks at Grand Faw Port
- docks handed over to Iraqi port authorities
- operation planned to start in 2026
- expected capacity 3.5M containers by 2028
- part of Iraq’s $17B Development Road project

Stage 3:
보류
- dock completion은 delivery evidence
- 하지만 신규 공사수익, 추가 EPC backlog, margin, cash collection 확인 전 Green 금지

Stage 4B:
transport corridor headline로 관련주가 먼저 rerating되면 후보

Stage 4C:
operation delay, Iraq payment risk, security/geopolitical disruption, 추가 발주 부재 시 후보
```

Daewoo E&C는 Iraq Grand Faw Port의 5개 dock 공사를 완료했고, 이 시설은 2026년 운영 시작, 2028년 최대 350만 컨테이너 처리능력을 목표로 한다. 이 항만은 Iraq가 Middle East와 Europe을 Turkey를 통해 연결하려는 170억 달러 Development Road 프로젝트의 핵심이다. 이건 R10에서 드문 “완공·인도” evidence지만, 회사의 신규 Stage 3는 추가 수주, margin, cash collection이 확인되어야 한다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters infrastructure-delivery anchor

stage3_price:
N/A

Daewoo_E&C_stock_OHLC:
price_data_unavailable_after_deep_search

completed_docks:
5

operation_start_target:
2026

maximum_capacity_target:
3.5M containers by 2028

Development_Road_project_value:
$17B

MFE / MAE:
price_data_unavailable_after_deep_search

reason:
- Reuters provides project completion and capacity metrics, not Daewoo E&C stock-price path.
- KRX/Naver/Yahoo/Stooq raw OHLC unavailable.
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = port_infrastructure_delivery_watch
stage_failure_type = stage2_delivery_not_green
```

---

## Case C — Seoul housing supply / mortgage-tightening basket `event_premium / policy watch`

```text
symbols = GS E&C / DL E&C / HDC / Daewoo E&C / housing-construction basket
case_type = event_premium / policy_watch
archetype = HOUSING_POLICY_SUPPLY_EVENT
```

### stage date

```text
Stage 1:
2025-03-19
- wealthy Seoul districts apartment trading permit rules tightened
- Gangnam / Seocho / Songpa / Yongsan transaction permit zones
- speculation-control policy

Stage 2:
2025-09-07
- LTV in Gangnam / Yongsan reduced 50% → 40%
- state-owned land development
- reconstruction rule simplification
- affordable housing supply expansion

Stage 3:
없음
- 정책 이벤트만으로 건설주 Green 금지
- presales, margin, PF stability, land cost, FCF 확인 필요

Stage 4B:
공급정책·재건축 완화만으로 건설주가 먼저 급등하면 후보

Stage 4C:
LTV tightening demand shock, unsold inventory, PF refinancing stress, construction-cost inflation 시 후보
```

서울 주택정책은 R10에서 양면성이 크다. 정부는 강남·용산 등의 LTV를 50%에서 40%로 낮춰 수요를 누르는 동시에, LH 등 공공기관 보유 토지 활용과 재건축 규제 단순화로 공급을 늘리겠다고 밝혔다. 또 2025년 3월에는 강남·서초·송파·용산의 거래허가제를 강화했다. 이는 건설주에 Stage 1~2 정책 event일 수 있지만, Green은 분양률·원가율·PF 안정·FCF로 확인해야 한다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters housing-policy evidence

stage3_price:
N/A

housing_basket_OHLC:
price_data_unavailable_after_deep_search

LTV_before:
50%

LTV_after:
40%

LTV_reduction_absolute:
-10pp

LTV_reduction_relative:
40 / 50 - 1
= -20%

affected_high-end_districts:
Gangnam / Yongsan for LTV
Gangnam / Seocho / Songpa / Yongsan for permit-zone tightening

policy_mix:
demand control + supply support

MFE / MAE:
price_data_unavailable_after_deep_search

reason:
- Reuters gives housing policy facts, not raw OHLC for construction basket.
- KRX/Naver/Yahoo/Stooq raw OHLC unavailable.
```

### alignment

```text
score_price_alignment = event_premium / policy_watch
rerating_result = housing_supply_policy_watch
stage_failure_type = stage1_or_stage2_attention_only
```

---

## Case D — Taeyoung / construction PF basket `hard 4C / PF credit break`

```text
symbol = 009410 / construction PF basket
case_type = 4C-thesis-break
archetype = REAL_ESTATE_PF_CREDIT_BREAK
```

### stage date

```text
Stage 1:
2023
- high rates
- housing-market downturn
- construction PF refinancing stress

Stage 2:
없음
- liquidity support / debt reschedule은 positive stage가 아니라 RedTeam input

Stage 3:
없음

Stage 4C:
2023-12 / 2024-05-13
- Taeyoung debt reschedule triggers liquidity concern
- real estate PF delinquency 0.37% → 2.70%
- FSS expands/toughens project assessment
- syndicated loan 1T won, expandable to 5T won
```

Taeyoung debt reschedule은 R10에서 hard 4C 기준점이다. FSS는 부동산 PF 연체율이 2021년 말 0.37%에서 2022년 말 1.19%, 2023년 말 2.70%로 올랐다고 밝혔고, PF 사업성 평가를 강화했다. 정부는 건설사·중소기업을 위한 40.6조 원 금융지원책도 마련했지만, 이것은 Green이 아니라 crisis relief다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters PF stress / policy-support anchors

stage3_price:
N/A

Taeyoung_stock_OHLC:
price_data_unavailable_after_deep_search

PF_delinquency_2021_end:
0.37%

PF_delinquency_2022_end:
1.19%

PF_delinquency_2023_end:
2.70%

PF_delinquency_increase_2021_to_2023_absolute:
2.70 - 0.37
= +2.33pp

PF_delinquency_increase_2021_to_2023_relative:
2.70 / 0.37 - 1
= +629.7%

PF_delinquency_2022_to_2023_relative:
2.70 / 1.19 - 1
= +126.9%

syndicated_loan_initial:
1T won

syndicated_loan_max:
5T won

loan_expandability:
5x

government_support_package:
40.6T won

MFE:
N/A

MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = PF_credit_break
stage_failure_type = hard_4C
```

---

## Case E — Hyundai Engineering highway bridge collapse `sector hard 4C / direct-listed mapping unclear`

```text
listed_exposure = Hyundai group / Hyundai E&C sentiment only
case_type = 4C-thesis-break / direct_ticker_unclear
archetype = CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C
```

### stage date

```text
Stage 1:
2025-02 이전
- expressway expansion project
- civil engineering construction

Stage 2:
없음

Stage 3:
없음

Stage 4C:
2025-02-25
- highway bridge under construction collapsed near Cheonan / Anseong
- 4 workers killed, 6 injured
- 10 workers fell
- Hyundai Engineering in charge of construction site
- direct listed vehicle unclear
```

2025년 2월 25일 서울 남쪽 고속도로 건설 현장에서 교량 구조물이 붕괴해 4명이 사망하고 6명이 다쳤다. Washington Post는 Hyundai Engineering이 해당 현장 담당 회사였고, 당국 조사에 협조 중이라고 전했다. Reuters와 AP도 사고의 사망·부상 규모와 구조 작업을 보도했다. 현대엔지니어링은 직접 상장사가 아니므로 이 case는 특정 종목 가격검증보다는 R10의 **sector hard safety gate**로 기록한다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP / Washington Post safety-event evidence

stage3_price:
N/A

listed_stock_mapping:
unclear / Hyundai Engineering not directly listed

stock_OHLC:
N/A or price_data_unavailable_after_deep_search

fatalities:
4

injuries:
6

workers_fell:
10

critical_injuries:
5 of 6 survivors described as critical in some reports

event_type:
partially constructed highway bridge collapse

MFE:
N/A

MAE:
N/A

Stage 4C 큰 하락 이전 포착 여부:
event itself
- 사고 전 정량 예측은 어렵지만, fatal construction accident 발생 즉시 hard 4C gate.
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = construction_safety_trust_break
stage_failure_type = sector_hard_4C_direct_listed_mapping_unclear
```

---

## Case F — POSCO E&C / DL Construction safety crackdown `4C-watch / recurring fatal-accident regulation`

```text
listed_exposure = POSCO Holdings / DL Construction exposure
case_type = 4C-watch
archetype = WORKPLACE_FATALITY_REGULATORY_4C
```

### stage date

```text
Stage 1:
2025
- workplace safety crackdown
- construction fatality regulation 강화

Stage 2:
없음

Stage 3:
없음

Stage 4C-watch:
2025
- POSCO E&C CEO dismissed
- 103 construction sites halted
- DL Construction about 80 executives tendered resignations
- recurring fatal accident regulation risk

추가 4C-watch:
2025-09-15
- companies with >3 worker deaths/year may face fines up to 5% of operating profit
- repeated construction work suspensions can lead to license revocation
```

South Korea는 건설업 사망사고에 대한 규제를 강화하고 있다. Reuters는 건설 사망률이 15.9명/10만 명으로 OECD 회원국 중 두 번째로 높고, 2024년 산업재해 사망 589명 중 거의 절반이 건설업에서 발생했다고 보도했다. POSCO E&C는 expressway builder deaths 이후 CEO를 해임하고 103개 공사현장을 중단했으며, DL Construction에서는 사망사고 이후 약 80명의 임원이 사의를 냈다. 정부는 반복 사망사고 기업에 영업이익의 최대 5% 벌금과 면허취소 가능성을 추진했다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters safety-regulation / operational evidence anchors

stage3_price:
N/A

direct_listed_stock_OHLC:
price_data_unavailable_after_deep_search

Korea_industrial_death_rate_2023:
3.9 per 100,000 workers

OECD_average:
2.6 per 100,000 workers

relative_excess_vs_OECD:
3.9 / 2.6 - 1
= +50.0%

Korea_construction_death_rate:
15.9 per 100,000 workers

2024_workplace_deaths:
589

construction_share:
nearly half

POSCO_E&C_sites_halted:
103

DL_Construction_executives_resigned:
about 80

proposed_fine:
up to 5% of operating profit

license_revocation_risk:
true for repeated fatal incidents / repeated work-suspension builders

MFE:
N/A

MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = operational_safety_redteam
stage_failure_type = 4C_watch_not_company_hard_4C_yet
```

---

## Case G — SK/AWS·OpenAI/Samsung data-center real asset `success_candidate + event_premium`

```text
listed_exposure = SK group / Samsung SDS / SK Telecom / Samsung C&T / Samsung Heavy
case_type = success_candidate + event_premium
archetype = AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT
```

### stage date

```text
Stage 1:
2025-06-20
- SK / AWS Ulsan AI data center
- 7조 원 / $5.11B investment
- 100MW initial capacity, 2029 full operation
- potential 1GW expansion

Stage 2:
2025-10~2026-02
- OpenAI / Samsung SDS / SK Telecom Korea data-center JV plan
- two data centers, 20MW initial capacity
- Samsung C&T / Samsung Heavy floating data-center collaboration

Stage 3:
없음
- 데이터센터 headline만으로 Green 금지
- tenant contract, power, water, permitting, capex per share, NOI/AFFO 확인 필요

Stage 4B:
2025-06-20
- AI data center policy/event rally
- SK Hynix +3% 이상
- Kakao +11%
- LG CNS +9%

Stage 4C:
power/water/permitting failure, tenant revenue absence, capex dilution, funding cost spike 시 후보
```

SK Group과 AWS는 Ulsan에 약 7조 원, 51.1억 달러 규모 AI data center를 짓기로 했고, 2029년 100MW 완전가동 및 향후 1GW 확장 가능성을 제시했다. 발표일에는 AI 관련주가 랠리해 SK Hynix가 3% 이상, Kakao가 11%, LG CNS가 9% 올랐다. 이후 OpenAI, Samsung SDS, SK Telecom은 한국 내 두 개 데이터센터, 초기 20MW 규모 계획을 추진했고, Samsung C&T·Samsung Heavy는 floating data center 기술 협력을 논의했다. 그러나 R10 Green은 tenant·NOI/AFFO·전력·용수·인허가·capex per share가 확인되어야 한다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP investment and event-return anchors

stage3_price:
N/A

SK_AWS_investment:
7.0T won / $5.11B

AWS_component:
$4B

initial_capacity:
100MW

potential_expansion:
1GW

capacity_expansion_potential:
1GW / 100MW
= 10x

construction_start:
2025-09 planned

full_operation:
2029 planned

OpenAI_Samsung_SK_initial_capacity:
20MW

event_basket_MFE_1D:
SK Hynix > +3%
Kakao +11%
LG CNS +9%

floating_data_center:
Samsung C&T / Samsung Heavy / OpenAI collaboration discussed

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + event_premium
rerating_result = AI_data_center_real_asset_watch
stage_failure_type = stage2_evidence_not_green
```

---

## Case H — Hyundai Steel / rebar construction-demand proxy `4C-watch / building-material demand cycle`

```text
symbol = 004020
case_type = 4C-watch
archetype = BUILDING_MATERIALS_DEMAND_CYCLE
```

### stage date

```text
Stage 1:
2024
- construction demand slowdown
- rebar / building-material weakness
- shipbuilding steel plate competition

Stage 2:
없음
- weak demand event는 positive stage가 아님

Stage 3:
없음
- 건설회복 전 Green 금지

Stage 4C-watch:
2024-06-21
- Nomura cuts Hyundai Steel 2024 net-profit forecast by 73%
- target price -14% to 30,000원
- shares -1.2% to 29,000원
- rebar price expected -10% in 2024
```

현대제철은 R10 건자재·철근 수요 proxy로 적합하다. Nomura는 건설·조선 수요 약화로 2024년 실적이 타격을 받을 수 있다고 봤고, 순이익 추정치를 73% 낮춰 2,150억 원으로 조정했다. 목표가는 14% 낮춘 30,000원, 주가는 1.2% 하락한 29,000원으로 보도됐다. 철근 가격은 2024년 10% 하락 가능성이 제기됐다. ([마켓워치][8])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch reported price / target / estimate anchor

stage3_price:
N/A

event_price_anchor:
29,000원

event_MAE:
-1.2%

implied_pre_event_reference_price:
29,000 / (1 - 0.012)
= 약 29,352원

target_price:
30,000원

target_cut:
-14%

implied_prior_target:
30,000 / (1 - 0.14)
= 약 34,884원

target_upside_from_event_price:
(30,000 / 29,000) - 1
= +3.45%

net_profit_forecast_2024:
215B won

net_profit_forecast_cut:
-73%

implied_prior_net_profit_forecast:
215B / (1 - 0.73)
= 약 796.3B won

rebar_price_expected_decline:
-10%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = building_materials_demand_cycle_watch
stage_failure_type = should_have_been_yellow_or_red
```

---

# 5. 이번 R10 case별 요약표

| case                                | 분류                              |                                                     실제 가격검증 | alignment         |
| ----------------------------------- | ------------------------------- | ----------------------------------------------------------: | ----------------- |
| Czech nuclear infra                 | success_candidate + legal watch |      Doosan +48% 3M, KEPCO E&C +41%; contract $18.7B signed | Stage 2           |
| Daewoo E&C Grand Faw                | success_candidate               | five docks completed, 3.5M containers by 2028, $17B project | delivery Stage 2  |
| Seoul housing policy                | event/policy watch              |                         LTV 50%→40%, permit-zone tightening | policy event      |
| Taeyoung / PF basket                | hard 4C                         |          PF delinquency 0.37%→2.70%, +629.7%; support 40.6T | PF credit break   |
| Hyundai Engineering bridge collapse | sector hard 4C                  |                 4 killed, 6 injured, listed mapping unclear | safety break      |
| POSCO E&C / DL safety               | 4C-watch                        |      103 sites halted, ~80 execs resigned, fine up to 5% OP | safety regulation |
| SK/AWS·OpenAI data center           | success_candidate + event       |                   7T won, 100MW→1GW; Kakao +11%, LG CNS +9% | Stage 2/event     |
| Hyundai Steel rebar proxy           | 4C-watch                        |                29,000원, -1.2%; NP forecast -73%; rebar -10% | demand watch      |

---

# 6. score-price alignment 판정

```text
success_candidate:
- Czech nuclear infra
- Daewoo E&C Grand Faw Port
- SK/AWS·OpenAI data center

event_premium / policy_watch:
- Seoul housing supply / mortgage tightening
- AI data center related basket rally

thesis_break:
- Taeyoung / construction PF stress
- Hyundai Engineering bridge collapse as sector safety hard gate

thesis_break_watch:
- POSCO E&C / DL Construction safety crackdown
- Hyundai Steel rebar / construction demand weakness

price_moved_without_evidence:
- housing policy rally before presales/margin/FCF
- AI data center rally before tenant/NOI/AFFO/power-water confirmation
- nuclear preferred-bidder rally before subcontract revenue/margin

4B-watch:
- nuclear related names after preferred-bidder surge
- AI data center event rally
- housing/reconstruction policy rally

hard_4C:
- PF credit break
- fatal construction safety accident as sector hard gate

4C-watch:
- workplace fatality regulation
- building-material demand weakness
- legal-delay risk in nuclear infra
```

---

# 7. 점수비중 교정

## 올릴 축

```text
cash_flow_after_working_capital +5
EPC_margin_visibility +5
project_cost_control +5
progress_revenue_visibility +4
handover_milestone +4
PF_credit_cleanup +5
funding_cost_control +5
tenant_contract_quality +5
NOI_AFFO_visibility +5
power_water_permitting_secured +4
safety_quality_trust +5
```

### 왜 올리나

Daewoo E&C Grand Faw처럼 실제 dock completion이 있는 경우는 단순 수주보다 높게 봐야 한다. Czech nuclear도 preferred bidder에서 signed contract로 넘어갔으므로 Stage 2 강도가 올라간다. 그러나 둘 다 회사별 margin·cash collection·working capital 전 Stage 3는 아니다. Data center도 투자금액보다 tenant·NOI/AFFO·전력·용수가 중요하다.

## 내릴 축

```text
contract_headline_only -5
preferred_bidder_only -4
PF_relief_policy_only -5
real_estate_rebound_theme_only -4
housing_supply_policy_only -4
data_center_theme_without_tenant -5
asset_headline_without_NOI_AFFO -5
EPC_backlog_without_margin -5
low_margin_order_risk -4
capex_per_share_dilution -4
quality_safety_incident -5
workplace_fatality_repeated -5
building_material_demand_weakness -4
```

### 왜 내리나

PF 지원책은 Green이 아니라 crisis relief다. 주택공급 정책은 분양률·원가율·PF 안정 없이는 Stage 3가 아니다. Data center는 임차인과 NOI/AFFO가 빠지면 테마주다. 건설 안전사고는 수주잔고보다 강한 4C gate다.

## Green gate 강화 조건

```text
R10 Stage 3-Green 필수:
1. 계약 또는 준공 milestone이 회사 단위로 확인됨
2. margin 또는 NOI/AFFO가 확인됨
3. 현금흐름이 working capital에 먹히지 않음
4. PF / funding cost 리스크 통과
5. 공정률 / 원가율 안정
6. tenant / occupancy / utilization 확인
7. capex per share / dilution 통과
8. 안전·품질 hard risk 없음
9. 가격경로가 evidence 이후 따라옴

금지:
preferred bidder만 있음
수주 headline만 있음
PF 지원책만 있음
주택공급 정책만 있음
데이터센터 테마만 있음
자산 보유 headline만 있음
안전사고 발생
working capital 악화
저마진 EPC 수주
```

## 4B 조기감지 조건

```text
4B-watch:
preferred bidder 뉴스 후 관련주 급등
대형 해외 EPC/인프라 수주 발표 직후 급등
PF 지원책으로 건설주 동반 급등
데이터센터 테마로 부동산/건설주 일괄 상승
REIT가 금리 인하 기대만으로 급등
주택공급 정책 발표일 건설주 급등
준공 milestone 없이 개발계획만으로 가격 급등

4B-elevated:
수주는 늘지만 마진 가시성이 약함
PF 부실이 아직 정리되지 않음
공사비·인건비·금융비용 상승
데이터센터 tenant는 있지만 power/water/capex 문제가 남음
AFFO보다 배당 기대가 먼저 반영
```

## 4C hard gate 조건

```text
PF workout / 채무재조정
부동산 PF 연체율 급등
미분양 / 분양 실패
공사비 원가율 급등
working capital 악화
수주 취소 / 발주처 지급 지연
저마진 EPC 손실 인식
아파트 붕괴 / 교량 붕괴 / 품질사고
사망사고 반복 / 현장중단
면허 취소 리스크
tenant 부재
power/water/permitting failure
AFFO integrity 훼손
capex dilution
```

이번 R10 Loop 10에서는 **PF credit break**와 **fatal construction safety accident**를 hard 4C로 둔다. 단, 현대엔지니어링 case는 direct listed mapping이 불명확하므로 sector hard gate로 기록한다.

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

## docs/round/round_168.md 요약

```md
# R10 Loop 10. Construction / Real Estate / Building Materials Price Validation

이번 라운드는 R10 Loop 10 price-validation 라운드다.

핵심 결론:
- Czech nuclear infra is Stage 2, not Green. Doosan Enerbility rose 48% in three months, KEPCO Plant S&E +14%, KEPCO E&C +41% around the preferred-bidder period. The final Czech contract is 407B koruna / $18.7B for two reactors, but listed-company subcontract, margin and cashflow must be confirmed.
- Daewoo E&C Grand Faw Port is infrastructure-delivery Stage 2. Five docks were completed and handed over; operation is expected in 2026 and 3.5M container capacity by 2028. New order/margin/cash collection required before Green.
- Seoul housing policy is policy watch. LTV in Gangnam/Yongsan was tightened from 50% to 40%, while supply through state land and reconstruction-rule simplification was proposed. Presales, margin, PF stability and FCF required.
- Taeyoung / construction PF is hard 4C. PF delinquency rose from 0.37% to 2.70%, +629.7%, and liquidity support is relief, not Green.
- Hyundai Engineering bridge collapse is sector hard 4C. Four workers were killed and six injured; direct listed mapping is unclear.
- POSCO E&C / DL Construction safety crackdown is 4C-watch. POSCO E&C halted 103 sites; about 80 DL Construction executives resigned; repeated fatal-accident firms may face fines up to 5% of operating profit.
- SK/AWS·OpenAI data center is Stage 2 + event premium. Ulsan project is 7T won, 100MW by 2029 with possible 1GW expansion. Tenant, NOI/AFFO, power/water/permitting and capex per share required before Green.
- Hyundai Steel rebar proxy is building-material 4C-watch. Shares were 29,000 won, -1.2%; 2024 net-profit forecast was cut 73%; rebar price expected -10%.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 168 R10 Loop 10 Construction Real Estate Materials Price Validation

## 반영 내용
- R10 Loop 10 price-validation 라운드를 추가했다.
- Nuclear infra EPC export, port infra delivery, housing policy, PF credit break, construction safety hard gate, workplace fatality regulation, AI data center real asset, building-material demand cycle을 비교했다.
- Reuters/AP/MarketWatch/Washington Post reported anchors로 가능한 MFE/MAE 및 contract/safety/PF/policy metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- cash flow after working capital, EPC margin, project cost control, handover milestone, tenant/NOI/AFFO, safety trust 가중치 강화
- preferred bidder-only, contract headline-only, PF relief-only, housing policy-only, data-center theme without tenant, safety incident 감점 강화
- PF hard 4C와 construction safety hard gate 강화
```

## case row 초안

```jsonl
{"case_id":"r10_loop10_czech_nuclear_infra_korea_epc","symbol":"034020/052690/051600/015760","company_name":"Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E / KEPCO","case_type":"success_candidate","primary_archetype":"NUCLEAR_INFRA_EPC_EXPORT","stage1_date":"2024-07-17","stage2_date":"2025-06-04","stage4c_date":"2025-05-06_watch","price_validation":{"price_data_source":"Reuters/AP nuclear-contract and sector-return anchors","stage3_price":null,"doosan_3m_mfe_pct":48,"kepco_plant_se_3m_mfe_pct":14,"kepco_ec_3m_mfe_pct":41,"czech_contract_value_koruna_bn":407,"czech_contract_value_usd_bn":18.7,"reactor_count":2,"unit_cost_context_koruna_bn":200,"unit_cost_context_usd_bn":8.65,"trial_operation_expected":"2036_first_reactor_2038_second_reactor","price_validation_status":"reported_sector_return_not_full_ohlc"},"score_price_alignment":"success_candidate_legal_watch","rerating_result":"nuclear_EPC_export_watch","notes":"Preferred bidder to signed contract is Stage 2; listed-company package, margin and cash collection required before Green."}
{"case_id":"r10_loop10_daewoo_enc_grand_faw_port_delivery","symbol":"047040","company_name":"Daewoo E&C","case_type":"success_candidate","primary_archetype":"PORT_INFRA_DELIVERY","stage2_date":"2024-11-12","price_validation":{"price_data_source":"Reuters infrastructure-delivery anchor","stage3_price":null,"completed_docks":5,"operation_start_target_year":2026,"maximum_capacity_target_mn_containers":3.5,"capacity_target_year":2028,"development_road_project_value_usd_bn":17,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"port_infrastructure_delivery_watch","notes":"Dock completion is stronger than a mere order headline, but additional backlog, margin and cash collection are required before Stage 3."}
{"case_id":"r10_loop10_seoul_housing_policy_supply_watch","symbol":"housing_construction_basket","company_name":"Seoul housing supply / mortgage tightening basket","case_type":"event_premium","primary_archetype":"HOUSING_POLICY_SUPPLY_EVENT","stage1_date":"2025-03-19","stage2_date":"2025-09-07","price_validation":{"price_data_source":"Reuters housing-policy evidence","stage3_price":null,"ltv_before_pct":50,"ltv_after_pct":40,"ltv_reduction_pp":-10,"ltv_reduction_relative_pct":-20,"affected_districts":["Gangnam","Yongsan","Gangnam/Seocho/Songpa/Yongsan permit zone"],"policy_mix":"demand_control_plus_supply_support","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_policy_watch","rerating_result":"housing_supply_policy_watch","notes":"Housing policy is Stage 1/2; presales, margin, PF stability and FCF required before Green."}
{"case_id":"r10_loop10_taeyoung_pf_credit_hard_4c","symbol":"009410/PF_basket","company_name":"Taeyoung / construction PF stress","case_type":"4c_thesis_break","primary_archetype":"REAL_ESTATE_PF_CREDIT_BREAK","stage4c_date":"2023-12/2024-05-13","price_validation":{"price_data_source":"Reuters PF stress/policy-support anchors","stage3_price":null,"pf_delinquency_2021_pct":0.37,"pf_delinquency_2022_pct":1.19,"pf_delinquency_2023_pct":2.70,"pf_delinquency_increase_2021_to_2023_pp":2.33,"pf_delinquency_increase_2021_to_2023_pct":629.7,"pf_delinquency_increase_2022_to_2023_pct":126.9,"syndicated_loan_initial_krw_trn":1,"syndicated_loan_max_krw_trn":5,"loan_expandability_multiple":5,"government_support_package_krw_trn":40.6,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break","rerating_result":"PF_credit_break","notes":"Debt reschedule and PF delinquency spike are hard 4C; liquidity support is relief, not Green."}
{"case_id":"r10_loop10_hyundai_engineering_bridge_collapse_sector_hard_4c","symbol":"unlisted_Hyundai_Engineering/sector_exposure","company_name":"Hyundai Engineering bridge-collapse sector case","case_type":"4c_thesis_break","primary_archetype":"CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C","stage4c_date":"2025-02-25","price_validation":{"price_data_source":"Reuters/AP/Washington Post safety-event evidence","stage3_price":null,"listed_stock_mapping":"unclear_not_direct_listed_vehicle","fatalities":4,"injuries":6,"workers_fell":10,"critical_injuries":5,"event_type":"partially constructed highway bridge collapse","price_validation_status":"not_direct_listed_stock_price_unavailable"},"score_price_alignment":"thesis_break","rerating_result":"construction_safety_trust_break","notes":"Fatal bridge collapse is sector hard 4C; direct listed mapping unclear."}
{"case_id":"r10_loop10_posco_dl_construction_safety_regulation","symbol":"POSCO_EC/DL_Construction_exposure","company_name":"POSCO E&C / DL Construction safety cases","case_type":"4c_watch","primary_archetype":"WORKPLACE_FATALITY_REGULATORY_4C","stage4c_date":"2025","price_validation":{"price_data_source":"Reuters safety-regulation evidence","stage3_price":null,"korea_industrial_death_rate_per_100k":3.9,"oecd_average_death_rate_per_100k":2.6,"relative_excess_vs_oecd_pct":50.0,"korea_construction_death_rate_per_100k":15.9,"workplace_deaths_2024":589,"construction_share":"nearly_half","posco_ec_sites_halted":103,"dl_construction_executives_resigned":80,"proposed_fine_pct_of_operating_profit":5,"license_revocation_risk":true,"price_validation_status":"direct_listed_event_ohlc_unavailable"},"score_price_alignment":"thesis_break_watch","rerating_result":"operational_safety_redteam","notes":"Recurring fatal accidents and site shutdowns require 4C-watch and safety-trust gate."}
{"case_id":"r10_loop10_ai_data_center_real_asset_event","symbol":"SK_group/Samsung_SDS/SK_Telecom/Samsung_CT/Samsung_Heavy_related","company_name":"SK/AWS·OpenAI·Samsung data-center real asset","case_type":"success_candidate","primary_archetype":"AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT","stage1_date":"2025-06-20","stage2_date":"2025-10_to_2026-02","stage4b_date":"2025-06-20","price_validation":{"price_data_source":"Reuters/AP investment and event-return anchors","stage3_price":null,"sk_aws_investment_krw_trn":7.0,"sk_aws_investment_usd_bn":5.11,"aws_component_usd_bn":4.0,"initial_capacity_mw":100,"potential_expansion_gw":1.0,"capacity_expansion_potential_multiple":10,"construction_start_planned":"2025-09","full_operation_planned_year":2029,"openai_samsung_sk_initial_capacity_mw":20,"sk_hynix_event_mfe_pct":3,"kakao_event_mfe_pct":11,"lg_cns_event_mfe_pct":9,"floating_data_center_collaboration":true,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"AI_data_center_real_asset_watch","notes":"AI data-center investment is Stage 1/2; tenant, NOI/AFFO, power/water/permitting and capex per share required before Green."}
{"case_id":"r10_loop10_hyundai_steel_rebar_construction_demand_watch","symbol":"004020","company_name":"Hyundai Steel / rebar construction demand proxy","case_type":"4c_watch","primary_archetype":"BUILDING_MATERIALS_DEMAND_CYCLE","stage4c_date":"2024-06-21","price_validation":{"price_data_source":"MarketWatch reported price/target/estimate anchor","stage3_price":null,"event_price_anchor":29000,"event_mae_pct":-1.2,"implied_pre_event_reference_price":29352,"target_price":30000,"target_cut_pct":-14,"implied_prior_target":34884,"target_upside_from_event_price_pct":3.45,"net_profit_forecast_2024_krw_bn":215,"net_profit_forecast_cut_pct":-73,"implied_prior_net_profit_forecast_krw_bn":796.3,"rebar_price_expected_decline_pct":-10,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"building_materials_demand_cycle_watch","notes":"Rebar/construction-demand weakness blocks building-material Green until demand, spread and margin stabilize."}
```

## shadow weight row 초안

```csv
archetype,cash_flow_after_wc,epc_margin,project_cost_control,progress_revenue,handover_milestone,pf_cleanup,funding_cost,tenant_noi_affo,safety_trust,event_penalty,hard_4c_sensitivity,notes
NUCLEAR_INFRA_EPC_EXPORT,+5,+5,+5,+4,+4,+0,+4,+0,+3,-4,+4,Nuclear preferred bidder/signed contract is Stage 2 until listed-company margin/cashflow confirm.
PORT_INFRA_DELIVERY,+5,+5,+4,+4,+5,+0,+3,+0,+3,-3,+4,Daewoo Grand Faw dock completion is Stage 2 but needs new revenue/margin/cash collection.
HOUSING_POLICY_SUPPLY_EVENT,+3,+2,+3,+2,+0,+4,+4,+0,+2,-5,+4,Housing supply policy is not Green before presales/margin/PF/FCF confirm.
REAL_ESTATE_PF_CREDIT_BREAK,+5,+0,+0,+0,+0,+5,+5,+0,+2,-5,+5,PF delinquency spike and debt reschedule are hard 4C.
CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C,+0,+0,+0,+0,+0,+0,+0,+0,+5,0,+5,Fatal construction accident is sector hard 4C even if direct listed mapping is unclear.
WORKPLACE_FATALITY_REGULATORY_4C,+0,+0,+0,+0,+0,+0,+0,+0,+5,0,+5,Recurring fatal accidents create fine/license risk and block Green.
AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT,+4,+0,+4,+2,+0,+0,+5,+5,+3,-5,+4,Data-center theme is Stage 1/2 until tenant, NOI/AFFO, power/water and capex per share confirm.
BUILDING_MATERIALS_DEMAND_CYCLE,+4,+4,+3,+0,+0,+3,+4,+0,+2,-4,+4,Rebar/building-material demand weakness requires margin and demand stabilization before Green.
```

---

# 이번 R10 Loop 10 결론

R10은 **Stage 2 evidence가 많아도 Stage 3는 매우 늦게 줘야 하는 섹터**다.

```text
1. Czech nuclear infra는 preferred bidder에서 signed contract로 승격됐으므로 강한 Stage 2다.
   하지만 Doosan/KEPCO 계열의 실제 package, margin, cashflow 전 Green은 아니다.

2. Daewoo E&C Grand Faw Port는 dock completion이라는 의미 있는 delivery evidence가 있다.
   그러나 신규 수주·마진·현금회수 전 Stage 3는 아니다.

3. 서울 주택정책은 수요억제와 공급확대가 동시에 붙은 policy event다.
   분양률, 원가율, PF 안정, FCF 확인 전 Green 금지다.

4. PF stress는 R10 hard 4C다.
   연체율 +629.7%와 debt reschedule은 liquidity relief로도 Green이 될 수 없다.

5. Hyundai Engineering bridge collapse는 sector hard 4C다.
   직접 상장사 mapping은 불명확하지만, fatal construction accident는 safety gate를 즉시 닫는다.

6. POSCO E&C / DL Construction safety crackdown은 4C-watch다.
   현장중단, 임원사퇴, 벌금·면허취소 리스크가 건설주 Green을 막는다.

7. AI data center real asset은 Stage 2 후보지만,
   tenant·NOI/AFFO·전력·용수·인허가·capex per share 전 Stage 3가 아니다.

8. Hyundai Steel rebar proxy는 건설·건자재 수요 약화 4C-watch다.
   철근 가격과 순이익 추정치가 동시에 꺾이면 건자재 Green은 막아야 한다.
```

한 문장으로 압축하면:

> **R10에서 진짜 Stage 3는 “수주·정책·개발계획·데이터센터가 있다”가 아니라, 그 계약과 자산이 마진·현금흐름·NOI/AFFO로 잠기고 PF·안전·funding cost를 통과하는 순간이다.**
> **R10은 PF와 안전사고를 가장 강한 4C gate로 두고, preferred bidder·housing policy·data-center headline은 먼저 Stage 2/Event Premium으로 분리해야 한다.**

[1]: https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/?utm_source=chatgpt.com "South Korea's winning bid for Czech nuclear power project"
[2]: https://www.reuters.com/world/middle-east/iraq-shortlists-11-firms-grand-faw-port-operation-decision-january-2025-2024-11-12/?utm_source=chatgpt.com "Iraq shortlists 11 firms for Grand Faw port operation, decision in January 2025"
[3]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-tighten-mortgage-rules-seoul-boost-housing-supply-2025-09-07/?utm_source=chatgpt.com "South Korea to tighten mortgage rules in Seoul, boost housing supply"
[4]: https://www.reuters.com/markets/asia/south-korea-tightens-scrutiny-speed-up-real-estate-restructuring-2024-05-13/?utm_source=chatgpt.com "South Korea tightens scrutiny to speed up real estate restructuring"
[5]: https://www.reuters.com/world/asia-pacific/three-people-dead-five-hurt-south-korea-highway-construction-site-yonhap-says-2025-02-25/?utm_source=chatgpt.com "At least three dead in South Korea highway construction project collapse"
[6]: https://www.reuters.com/sustainability/sustainable-finance-reporting/south-korea-fine-companies-up-5-profit-recurring-fatal-accidents-ministry-says-2025-09-15/?utm_source=chatgpt.com "South Korea to fine companies up to 5% of profit for recurring fatal accidents, ministry says"
[7]: https://www.reuters.com/business/retail-consumer/south-korea-says-sk-amazon-invest-5-bln-countrys-biggest-data-centre-2025-06-20/?utm_source=chatgpt.com "South Korea says SK and Amazon to invest $5 billion in country's biggest data centre"
[8]: https://www.marketwatch.com/story/hyundai-steel-s-2024-earnings-could-be-hit-by-weak-demand-market-talk-bcbe77c8?utm_source=chatgpt.com "Hyundai Steel's 2024 Earnings Could Be Hit by Weak Demand -- Market Talk"
