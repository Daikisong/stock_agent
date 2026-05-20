순서상 이번은 **R10 Loop 11 — 건설·부동산·건자재 가격경로 검증 라운드**다.

```text
round = R10 Loop 11
round_id = round_181
large_sector = CONSTRUCTION_REAL_ESTATE_MATERIALS
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
```

이번에도 KRX/Naver/Yahoo/Stooq의 원시 수정주가 일봉 OHLC 전체 구간은 안정적으로 확보하지 못했다. 대신 Reuters / WSJ / AP가 제공한 **계약금액, 이벤트 수익률, 정책금액, 사고·규제 지표, 가격 anchor**만 계산했다. 30D/90D/180D 전체 OHLC가 없는 항목은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R10 = 건설·부동산·건자재
```

R10의 Stage 3는 “대형 수주”, “부동산 정책”, “데이터센터”, “PF 지원”, “재건축 완화”가 아니다.

**계약이 실제 공정률·매출·마진·현금회수로 닫히고, PF·원가율·안전·인허가·tenant/NOI/AFFO를 통과하는 순간**이다.

---

# 2. 대상 canonical archetype

```text
OVERSEAS_EPC_MEGA_ORDER
GAS_INFRA_DELIVERY_VALIDATION
AI_DATA_CENTER_REAL_ASSET
HOUSING_POLICY_SUPPLY_EVENT
REAL_ESTATE_PF_CREDIT_BREAK
CONSTRUCTION_SAFETY_REGULATORY_4C
BUILDING_MATERIALS_DEMAND_CYCLE
PORT_INFRA_DELIVERY
```

---

# 3. deep sub-archetype

```text
해외 EPC:
- Samsung E&A / GS E&C
- Saudi Aramco Fadhili gas expansion
- contract size / project duration / margin / working capital

가스 인프라:
- Hyundai E&C
- Aramco Jafurah / main gas network
- first-phase production vs Korean contractor package

AI 데이터센터 real asset:
- SK / AWS Ulsan AI data center
- OpenAI / Samsung SDS / SK Telecom Korea data centers
- Samsung C&T / Samsung Heavy floating data center
- tenant / power / water / permitting / capex per share

주택정책:
- Seoul LTV tightening
- state-owned land supply
- reconstruction simplification
- policy event vs presales / margin / PF stability

PF:
- Taeyoung / construction PF basket
- PF delinquency spike
- liquidity support is relief, not Green

건설안전:
- POSCO E&C / DL Construction
- fatal accident fine up to 5% OP
- site shutdown / license revocation risk

건자재:
- Hyundai Steel rebar proxy
- construction demand weakness
- target / profit estimate cut

항만 인프라:
- Daewoo E&C Grand Faw Port
- completed docks / 2026 operation / 2028 capacity
```

---

# 4. 국장 신규 후보 case

## Case A — Samsung E&A / Fadhili gas `success_candidate + 4B-watch`

```text
symbol = 028050
case_type = success_candidate + 4B-watch
archetype = OVERSEAS_EPC_MEGA_ORDER
```

### stage date

```text
Stage 1:
2024-04-02
- Saudi Aramco Fadhili gas plant expansion
- Korean EPC overseas order cycle
- Middle East gas infrastructure demand

Stage 2:
2024-04-03
- Samsung E&A wins about $6B contract
- total Aramco Fadhili project $7.7B
- gas processing capacity 2.5B cf/d → 4.0B cf/d
- completion expected November 2027
- shares +8.5% to 26,750 won while KOSPI -1.4%

Stage 3:
없음
- 계약 headline은 강하지만 아직 Green 아님
- 공정률, 매출 인식, OPM, working capital, cash collection 확인 필요

Stage 4B:
2024-04-03
- 계약 발표 직후 +8.5%
- project margin / cash conversion 전 가격 선반영
```

Samsung E&A는 Fadhili gas plant expansion에서 약 60억 달러 계약을 따냈고, 전체 Fadhili expansion package는 77억 달러 규모였다. WSJ는 Samsung E&A가 장중 8.5% 오른 26,750원까지 상승했고, 같은 시점 KOSPI는 1.4% 하락했다고 보도했다. 계약 자체는 강한 Stage 2지만, R10 Green은 공정률·마진·현금회수 확인 뒤다. ([월스트리트 저널][1])

### 실제 가격경로 검증

```text
price_data_source:
WSJ / Reuters contract and event-return anchors

entry_date:
2024-04-03

stage3_price:
N/A

stage2_event_price:
26,750원

event_MFE_1D:
+8.5%

implied_prior_price:
26,750 / 1.085
= 약 24,654원

KOSPI_same_context:
-1.4%

relative_outperformance:
8.5 - (-1.4)
= +9.9pp

Samsung_E&A_contract_value:
about $6.0B

total_Fadhili_package:
$7.7B

Samsung_contract_share_of_total:
6.0 / 7.7
= 77.9%

Fadhili_capacity_before:
2.5B cf/d

Fadhili_capacity_after:
4.0B cf/d

capacity_increase:
4.0 / 2.5 - 1
= +60%

target_price:
35,000원

target_upside_from_event_price:
35,000 / 26,750 - 1
= +30.8%

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_event_premium
rerating_result = overseas_EPC_mega_order_watch
stage_failure_type = stage2_contract_not_green
```

---

## Case B — Hyundai E&C / Aramco Jafurah `success_candidate / gas infra delivery watch`

```text
symbol = 000720
case_type = success_candidate
archetype = GAS_INFRA_DELIVERY_VALIDATION
```

### stage date

```text
Stage 1:
2024-06-30
- Aramco Jafurah phase 2 / main gas network expansion
- Hyundai E&C consortium included in awarded companies
- Saudi gas infrastructure capex cycle

Stage 2:
2024-06-30
- Aramco signs >$25B contracts
- Jafurah reserves 229T cf raw gas + 75B barrels condensate
- main gas network adds 4,000 km pipelines
- network capacity +3.2B cf/d

Stage 2 validation:
2025-12-02
- Jafurah first phase begins output
- first-phase capacity 450M cf/d
- long-term target 2B cf/d by 2030

Stage 3:
없음
- Aramco project milestone은 좋지만 Hyundai E&C package/margin/cashflow 확인 필요

Stage 4B:
Jafurah / Middle East gas order cycle로 건설주 price가 먼저 움직이면 후보

Stage 4C:
cost overrun, local labor / execution delay, Saudi payment risk, low-margin EPC
```

Hyundai E&C는 Aramco Jafurah 및 main gas network expansion에서 Stage 2 후보로 볼 수 있다. Aramco는 2024년 6월 Jafurah 2단계와 main gas network 3단계 확장에 250억 달러 이상 계약을 체결했고, Jafurah는 229조 cf raw gas와 750억 배럴 condensate가 있는 대형 gas field다. 2025년 12월에는 Jafurah 1단계가 450M cf/d 규모로 생산을 시작했다. 다만 Hyundai E&C 상장사 단위의 package, margin, cash collection이 확인되지 않아 Stage 3는 보류한다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters Aramco/Jafurah project anchors

stage3_price:
N/A

Hyundai_E&C_stock_OHLC:
price_data_unavailable_after_deep_search

Aramco_contract_package:
>$25B

Jafurah_project_value_context:
$100B

Jafurah_raw_gas_reserves:
229T cf

Jafurah_condensate:
75B barrels

target_sales_gas_2030:
2B cf/d

first_phase_output:
450M cf/d

first_phase_vs_2030_target:
450M / 2B
= 22.5%

main_gas_network_addition:
4,000 km pipelines

main_gas_network_capacity_boost:
+3.2B cf/d

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = gas_infra_EPC_delivery_watch
stage_failure_type = stage2_project_milestone_not_green
```

---

## Case C — SK/AWS·OpenAI/Samsung data-center real asset `success_candidate + event premium`

```text
listed_exposure = SK group / Samsung SDS / SK Telecom / Samsung C&T / Samsung Heavy
case_type = success_candidate + event_premium
archetype = AI_DATA_CENTER_REAL_ASSET
```

### stage date

```text
Stage 1:
2025-06-20
- SK / AWS Ulsan AI data center
- 7T won / $5.11B investment
- 100MW initial capacity by 2029
- possible 1GW expansion

Stage 2:
2025-10~2026-02
- OpenAI / Samsung SDS / SK Telecom Korea data-center JV plan
- two data centers, initial 20MW
- construction planned from March 2026
- Samsung C&T / Samsung Heavy floating data center collaboration

Stage 3:
없음
- 데이터센터 headline만으로 Green 금지
- tenant contract, power, water, permitting, capex per share, NOI/AFFO 확인 필요

Stage 4B:
AI data-center / floating data-center headline로 건설·부동산·조선주가 먼저 움직이면 후보

Stage 4C:
power/water/permitting failure, tenant revenue absence, capex dilution, funding cost spike
```

AI data center real asset은 R10의 새 구조 후보지만, Green은 아직 아니다. SK Group과 AWS는 Ulsan에 약 7조 원, 51.1억 달러 규모 AI data center를 짓기로 했고, 초기 100MW에서 1GW 확장 가능성이 제시됐다. OpenAI, Samsung SDS, SK Telecom은 한국 내 2개 data center, 초기 20MW 규모 JV를 추진했고, Samsung C&T와 Samsung Heavy는 floating data center 개발 협력을 발표했다. 그래도 R10 Green은 tenant·NOI/AFFO·전력·용수·인허가·capex per share가 확인되어야 한다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP data-center investment and partnership anchors

stage3_price:
N/A

SK_AWS_investment:
7T won / $5.11B

AWS_component:
$4B

initial_capacity:
100MW

potential_expansion:
1GW

capacity_expansion_multiple:
1GW / 100MW
= 10x

full_operation_target:
2029

OpenAI_Samsung_SK_initial_capacity:
20MW

construction_start_target:
March 2026

floating_data_center_partners:
Samsung C&T / Samsung Heavy / OpenAI

MFE_30D / 90D:
price_data_unavailable_after_deep_search

reason:
- sources provide investment/capacity/partnership anchors, not adjusted OHLC for construction names.
```

### alignment

```text
score_price_alignment = success_candidate_event_premium
rerating_result = AI_data_center_real_asset_watch
stage_failure_type = stage2_headline_not_green
```

---

## Case D — Seoul housing supply / mortgage tightening `policy_watch / event premium`

```text
symbol = housing_construction_basket
case_type = event_premium / policy_watch
archetype = HOUSING_POLICY_SUPPLY_EVENT
```

### stage date

```text
Stage 1:
2025-09-07
- Seoul housing-price pressure
- demand-control and supply-support policy mix

Stage 2:
2025-09-07
- LTV in Gangnam / Yongsan reduced 50% → 40%
- state-owned land development
- reconstruction rule simplification
- affordable housing supply expansion

Stage 3:
없음
- 주택정책만으로 건설주 Green 금지
- presales, margin, PF stability, land cost, FCF 확인 필요

Stage 4B:
공급정책·재건축 완화만으로 건설주가 먼저 급등하면 후보

Stage 4C:
LTV tightening demand shock, unsold inventory, PF refinancing stress, construction-cost inflation
```

서울 주택정책은 R10에서 양면성이 크다. 정부는 강남·용산 등의 LTV를 50%에서 40%로 낮춰 수요를 누르는 동시에, 공공기관 보유 토지 활용과 재건축 규제 단순화로 공급을 늘리겠다고 밝혔다. 이건 건설주 Stage 1~2 policy event일 수 있지만, Green은 분양률·원가율·PF 안정·FCF 확인 뒤다. ([Reuters][4])

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
Gangnam / Yongsan

policy_mix:
demand control + supply support

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium_policy_watch
rerating_result = housing_supply_policy_watch
stage_failure_type = stage1_or_stage2_attention_only
```

---

## Case E — Construction PF / Taeyoung basket `hard 4C / credit break`

```text
symbol = 009410 / construction_PF_basket
case_type = 4C-thesis-break
archetype = REAL_ESTATE_PF_CREDIT_BREAK
```

### stage date

```text
Stage 1:
2023~2024
- high rates
- housing-market downturn
- construction PF refinancing stress

Stage 2:
없음
- liquidity support / debt reschedule은 positive stage가 아니라 RedTeam input

Stage 3:
없음

Stage 4C:
2024-03~05
- construction firms receive liquidity support after Taeyoung debt-reschedule concern
- PF delinquency 0.37% → 2.70%
- FSS tightens project assessment
- support package 40.6T won
- syndicated loan 1T won, expandable to 5T won
```

PF stress는 R10 hard 4C다. 정부는 고금리와 원자재 부담으로 어려워진 건설사와 중소기업에 40.6조 원 금융지원책을 준비했고, 이 배경에는 Taeyoung Engineering & Construction의 debt reschedule과 construction PF liquidity 우려가 있었다. FSS는 부동산 PF 연체율이 2021년 말 0.37%에서 2023년 말 2.70%로 급등했다고 밝혔다. 지원책은 Green이 아니라 crisis relief다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters PF stress / policy-support anchors

stage3_price:
N/A

Taeyoung_stock_OHLC:
price_data_unavailable_after_deep_search

government_support_package:
40.6T won

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

## Case F — POSCO E&C / DL Construction safety regulation `4C-watch / operating-license risk`

```text
listed_exposure = POSCO Holdings / DL Construction exposure
case_type = 4C-watch
archetype = CONSTRUCTION_SAFETY_REGULATORY_4C
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

Stage 4C-watch 강화:
2025-09-15
- >3 worker deaths/year firms may face fines up to 5% of operating profit
- repeated construction work suspension can lead to license revocation
```

건설 안전은 R10에서 단순 ESG가 아니라 hard gate다. Reuters는 한국이 반복 사망사고 기업에 영업이익 최대 5% 벌금과 건설사 면허취소 가능성을 추진한다고 보도했다. 별도 기사에서는 POSCO E&C가 103개 공사현장을 중단했고, DL Construction 임원 약 80명이 사의를 냈으며, 2024년 한국 산업재해 사망 589명 중 거의 절반이 건설업에서 발생했다고 정리했다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters safety-regulation / operational evidence anchors

stage3_price:
N/A

direct_listed_event_OHLC:
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
true

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

## Case G — Hyundai Steel / rebar construction-demand proxy `4C-watch / building-material demand cycle`

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

Hyundai Steel은 R10 건자재·철근 수요 proxy로 적합하다. Nomura는 건설·조선 수요 약화로 2024년 실적이 타격을 받을 수 있다고 봤고, 순이익 추정치를 73% 낮춰 2,150억 원으로 조정했다. 목표가는 14% 낮춘 30,000원, 주가는 1.2% 하락한 29,000원으로 보도됐다. 철근 가격은 2024년 10% 하락 가능성이 제기됐다. ([마켓워치][7])

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
30,000 / 29,000 - 1
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

## Case H — Daewoo E&C / Grand Faw Port `success_candidate / infra delivery`

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
- operation planned 2026
- capacity target 3.5M containers by 2028
- part of Iraq’s $17B Development Road project

Stage 3:
보류
- dock completion은 delivery evidence
- 하지만 추가 EPC backlog, margin, cash collection 확인 전 Green 금지

Stage 4B:
transport corridor headline로 price가 먼저 rerating되면 후보

Stage 4C:
operation delay, Iraq payment risk, security/geopolitical disruption, 추가 발주 부재
```

Daewoo E&C는 Grand Faw Port의 5개 dock 공사를 완료해 Iraqi port authorities에 인도했다. 이 항만은 2026년 운영 시작, 2028년 350만 container capacity를 목표로 하며, Iraq의 170억 달러 Development Road project 일부다. 이건 단순 수주보다 높은 delivery evidence지만, 상장사 Stage 3는 추가 수주·마진·현금회수가 확인되어야 한다. ([Reuters][8])

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
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = port_infrastructure_delivery_watch
stage_failure_type = stage2_delivery_not_green
```

---

# 5. 이번 R10 case별 요약표

| case                      | 분류                        |                                                 실제 가격검증 | alignment           |
| ------------------------- | ------------------------- | ------------------------------------------------------: | ------------------- |
| Samsung E&A Fadhili       | success_candidate + 4B    |           +8.5%, 26,750원, contract $6B, relative +9.9pp | EPC Stage 2         |
| Hyundai E&C Jafurah       | success_candidate         |             Aramco >$25B package, first phase 450M cf/d | gas infra Stage 2   |
| SK/AWS·OpenAI data center | success_candidate + event |                 7T won / 100MW → 1GW, OpenAI Korea 20MW | data center Stage 2 |
| Seoul housing policy      | event premium             |              LTV 50%→40%, supply/reconstruction support | policy watch        |
| PF / Taeyoung basket      | hard 4C                   |      PF delinquency 0.37%→2.70%, +629.7%; 40.6T support | PF credit break     |
| POSCO E&C / DL safety     | 4C-watch                  |   103 sites halted, 80 execs resigned, fine up to 5% OP | safety regulation   |
| Hyundai Steel rebar       | 4C-watch                  |            29,000원, -1.2%; NP forecast -73%; rebar -10% | demand watch        |
| Daewoo E&C Grand Faw      | success_candidate         | 5 docks complete, 3.5M containers by 2028, $17B project | delivery Stage 2    |

---

# 6. score-price alignment 판정

```text
success_candidate:
- Samsung E&A Fadhili
- Hyundai E&C Jafurah
- SK/AWS·OpenAI data center
- Daewoo E&C Grand Faw Port

event_premium:
- Samsung E&A +8.5% contract rally
- Seoul housing supply / reconstruction policy
- AI data center / floating data center headlines

evidence_good_but_price_failed:
- Hyundai Steel rebar proxy

thesis_break:
- PF / Taeyoung basket

thesis_break_watch:
- POSCO E&C / DL safety regulation
- Hyundai Steel building-material demand weakness

price_moved_without_evidence:
- housing policy rally before presales/margin/FCF
- AI data center rally before tenant/NOI/AFFO/power-water confirmation
- overseas EPC rally before margin/cash collection

hard_4C:
- PF credit break

4C-watch:
- construction safety / license risk
- building-material demand weakness
- data center power/water/permitting risk
```

---

# 7. 점수비중 교정

## 올릴 축

```text
signed_contract +5
progress_revenue_visibility +5
EPC_margin_visibility +5
cash_collection_quality +5
working_capital_control +5
handover_milestone +4
tenant_NOI_AFFO_visibility +5
power_water_permitting_secured +4
PF_credit_cleanup +5
safety_quality_trust +5
```

### 왜 올리나

Samsung E&A는 단순 기대가 아니라 약 60억 달러 계약과 +8.5% price reaction이 있었다. Daewoo E&C는 Grand Faw 5개 dock 완공·인도라는 delivery evidence가 있다. 다만 R10은 **계약·인도 이후에도 margin, working capital, cash collection**에서 무너질 수 있으므로 Stage 3 gate는 느리게 줘야 한다.

## 내릴 축

```text
contract_headline_only -5
policy_supply_headline_only -5
data_center_theme_without_tenant -5
preferred_project_without_company_margin -4
PF_relief_policy_only -5
working_capital_worsening -5
safety_incident -5
fatality_recurrence -5
building_material_demand_weakness -4
```

### 왜 내리나

PF 지원책은 Green이 아니라 crisis relief다. 주택 공급정책은 분양률·마진·PF 안정 없이는 Stage 3가 아니다. AI data center는 tenant, NOI/AFFO, 전력·용수·인허가 전에는 real asset 테마일 뿐이다. 안전사고는 수주잔고보다 강한 gate다.

## Green gate 강화 조건

```text
R10 Stage 3-Green 필수:
1. signed contract 또는 delivery milestone 확인
2. 공정률 / 매출 인식 확인
3. OPM 또는 gross margin 확인
4. working capital / cash collection 안정
5. PF / funding cost risk 통과
6. tenant / occupancy / NOI/AFFO 확인
7. power / water / permitting 통과
8. safety / quality hard risk 없음
9. 가격경로가 evidence 이후 따라옴

금지:
수주 headline만 있음
정책 headline만 있음
data center theme만 있음
PF 지원책만 있음
safety incident 존재
working capital 악화
저마진 EPC 수주
```

## 4B 조기감지 조건

```text
4B-watch:
대형 EPC 계약 발표일 +5~10% 급등
AI data center headline로 건설·부동산·조선주 동반 상승
주택공급 / 재건축 완화 정책으로 건설주 급등
PF relief로 건설주 basket 상승
준공 milestone 없이 개발계획만으로 valuation 확장

4B-elevated:
수주는 늘지만 margin visibility 약함
working capital 악화
공사비·인건비·금융비용 상승
data center tenant는 있지만 power/water/capex issue 남음
PF refinancing unresolved
```

## 4C hard gate 조건

```text
PF workout / 채무재조정
PF delinquency spike
분양 실패 / 미분양 증가
working capital 급증
수주 취소 / 발주처 지급 지연
저마진 EPC 손실 인식
fatal construction accident
repeated site shutdown
license revocation risk
tenant 부재
power/water/permitting failure
AFFO integrity 훼손
capex dilution
```

이번 R10 Loop 11에서 확정 hard 4C는 **construction PF credit break**다. POSCO E&C / DL safety는 4C-watch이고, 반복 사망사고가 실제 벌금·면허취소·대형 현장중단으로 연결되면 hard 4C로 승격한다.

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

## docs/round/round_181.md 요약

```md
# R10 Loop 11. Construction / Real Estate / Building Materials Price Validation

이번 라운드는 R10 Loop 11 price-validation 라운드다.

핵심 결론:
- Samsung E&A Fadhili is overseas EPC Stage 2 plus 4B-watch. Contract about $6B, total Fadhili project $7.7B, shares +8.5% to 26,750 won while KOSPI -1.4%. Margin, progress revenue and cash collection required before Green.
- Hyundai E&C Jafurah is gas-infra Stage 2. Aramco signed >$25B contracts, Hyundai E&C consortium included, Jafurah first phase began output at 450M cf/d. Company-level package, margin and cashflow required.
- SK/AWS·OpenAI data center real asset is Stage 2. SK/AWS Ulsan project 7T won / $5.11B, 100MW initial capacity with potential 1GW expansion; OpenAI/Samsung SDS/SK Telecom Korea data centers initial 20MW; Samsung C&T/Samsung Heavy floating data-center concept. Tenant, NOI/AFFO, power/water/permitting required.
- Seoul housing policy is event/policy watch. LTV in Gangnam/Yongsan 50%→40%, with state-owned land supply and reconstruction simplification. Presales, margin, PF stability and FCF required.
- PF / Taeyoung basket is hard 4C. PF delinquency rose 0.37%→2.70%, +629.7%, and 40.6T won support is crisis relief, not Green.
- POSCO E&C / DL Construction safety regulation is 4C-watch. POSCO E&C halted 103 sites, about 80 DL executives resigned, and repeated fatal-accident firms may face fines up to 5% of operating profit.
- Hyundai Steel rebar proxy is building-material 4C-watch. Shares 29,000 won, -1.2%; target cut 14%; 2024 net-profit forecast cut 73%; rebar price expected -10%.
- Daewoo E&C Grand Faw Port is infrastructure-delivery Stage 2. Five docks completed, operation planned 2026, capacity target 3.5M containers by 2028, part of Iraq’s $17B Development Road.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 181 R10 Loop 11 Construction Real Estate Materials Price Validation

## 반영 내용
- R10 Loop 11 price-validation 라운드를 추가했다.
- Overseas EPC mega-order, gas infrastructure, AI data-center real asset, Seoul housing policy, PF credit break, construction safety regulation, building-material demand cycle, port infrastructure delivery를 비교했다.
- Reuters/WSJ/AP anchors로 가능한 MFE/MAE 및 contract/policy/safety/PF metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- signed contract, progress revenue, EPC margin, cash collection, working-capital control, tenant/NOI/AFFO, power/water/permitting, PF cleanup, safety trust 가중치 강화
- contract headline-only, housing policy-only, data-center theme without tenant, PF relief-only, safety incident, building-material demand weakness 감점 강화
- PF hard 4C와 safety 4C-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r10_loop11_samsung_ea_fadhili_epc_4b","symbol":"028050","company_name":"Samsung E&A","case_type":"success_candidate","primary_archetype":"OVERSEAS_EPC_MEGA_ORDER","stage2_date":"2024-04-03","stage4b_date":"2024-04-03","price_validation":{"price_data_source":"WSJ/Reuters contract and event-return anchors","stage3_price":null,"stage2_event_price_krw":26750,"event_mfe_1d_pct":8.5,"implied_prior_price_krw":24654,"kospi_same_context_pct":-1.4,"relative_outperformance_pp":9.9,"contract_value_usd_bn":6.0,"total_fadhili_package_usd_bn":7.7,"contract_share_of_total_pct":77.9,"fadhili_capacity_before_bcf_d":2.5,"fadhili_capacity_after_bcf_d":4.0,"capacity_increase_pct":60,"target_price_krw":35000,"target_upside_from_event_price_pct":30.8,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_event_premium","rerating_result":"overseas_EPC_mega_order_watch","notes":"Mega EPC contract is Stage 2 and 4B-watch; progress revenue, OPM, working capital and cash collection required before Green."}
{"case_id":"r10_loop11_hyundai_enc_jafurah_gas_infra","symbol":"000720","company_name":"Hyundai E&C","case_type":"success_candidate","primary_archetype":"GAS_INFRA_DELIVERY_VALIDATION","stage2_date":"2024-06-30/2025-12-02","price_validation":{"price_data_source":"Reuters Aramco/Jafurah project anchors","stage3_price":null,"aramco_contract_package_usd_bn":25,"jafurah_project_value_usd_bn":100,"jafurah_raw_gas_reserves_tcf":229,"jafurah_condensate_billion_barrels":75,"target_sales_gas_2030_bcf_d":2.0,"first_phase_output_mcf_d":450,"first_phase_vs_2030_target_pct":22.5,"main_gas_network_addition_km":4000,"main_gas_network_capacity_boost_bcf_d":3.2,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"gas_infra_EPC_delivery_watch","notes":"Jafurah milestone is Stage 2; Hyundai E&C package, margin and cashflow required before Green."}
{"case_id":"r10_loop11_ai_data_center_real_asset","symbol":"SK_group/Samsung_SDS/SK_Telecom/Samsung_CT/Samsung_Heavy","company_name":"SK/AWS·OpenAI·Samsung data-center real asset basket","case_type":"success_candidate","primary_archetype":"AI_DATA_CENTER_REAL_ASSET","stage2_date":"2025-06-20/2026-02-11","price_validation":{"price_data_source":"Reuters/AP data-center investment and partnership anchors","stage3_price":null,"sk_aws_investment_krw_trn":7.0,"sk_aws_investment_usd_bn":5.11,"aws_component_usd_bn":4.0,"initial_capacity_mw":100,"potential_expansion_gw":1.0,"capacity_expansion_multiple":10,"full_operation_target_year":2029,"openai_samsung_sk_initial_capacity_mw":20,"construction_start_target":"2026-03","floating_data_center_partners":["Samsung C&T","Samsung Heavy","OpenAI"],"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_event_premium","rerating_result":"AI_data_center_real_asset_watch","notes":"AI data-center theme is Stage 2; tenant, NOI/AFFO, power/water/permitting and capex per share required before Green."}
{"case_id":"r10_loop11_seoul_housing_policy_supply_watch","symbol":"housing_construction_basket","company_name":"Seoul housing policy / construction basket","case_type":"event_premium","primary_archetype":"HOUSING_POLICY_SUPPLY_EVENT","stage2_date":"2025-09-07","price_validation":{"price_data_source":"Reuters housing-policy evidence","stage3_price":null,"ltv_before_pct":50,"ltv_after_pct":40,"ltv_reduction_pp":-10,"ltv_reduction_relative_pct":-20,"affected_districts":["Gangnam","Yongsan"],"policy_mix":"demand_control_plus_supply_support","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_policy_watch","rerating_result":"housing_supply_policy_watch","notes":"Housing policy is Stage 1/2; presales, margin, PF stability and FCF required before Green."}
{"case_id":"r10_loop11_pf_credit_break_taeyoung_basket","symbol":"009410/construction_PF_basket","company_name":"Taeyoung / construction PF stress basket","case_type":"4c_thesis_break","primary_archetype":"REAL_ESTATE_PF_CREDIT_BREAK","stage4c_date":"2024-03/2024-05","price_validation":{"price_data_source":"Reuters PF stress/policy-support anchors","stage3_price":null,"government_support_package_krw_trn":40.6,"pf_delinquency_2021_pct":0.37,"pf_delinquency_2022_pct":1.19,"pf_delinquency_2023_pct":2.70,"pf_delinquency_increase_2021_to_2023_pp":2.33,"pf_delinquency_increase_2021_to_2023_pct":629.7,"pf_delinquency_increase_2022_to_2023_pct":126.9,"syndicated_loan_initial_krw_trn":1,"syndicated_loan_max_krw_trn":5,"loan_expandability_multiple":5,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break","rerating_result":"PF_credit_break","notes":"PF delinquency spike and builder liquidity support are hard 4C/crisis relief, not Green."}
{"case_id":"r10_loop11_posco_dl_construction_safety_regulation","symbol":"POSCO_EC/DL_Construction_exposure","company_name":"POSCO E&C / DL Construction safety regulation basket","case_type":"4c_watch","primary_archetype":"CONSTRUCTION_SAFETY_REGULATORY_4C","stage4c_date":"2025-09-15","price_validation":{"price_data_source":"Reuters safety-regulation evidence","stage3_price":null,"korea_industrial_death_rate_per_100k":3.9,"oecd_average_death_rate_per_100k":2.6,"relative_excess_vs_oecd_pct":50.0,"korea_construction_death_rate_per_100k":15.9,"workplace_deaths_2024":589,"construction_share":"nearly_half","posco_ec_sites_halted":103,"dl_construction_executives_resigned":80,"proposed_fine_pct_of_operating_profit":5,"license_revocation_risk":true,"price_validation_status":"direct_listed_event_ohlc_unavailable"},"score_price_alignment":"thesis_break_watch","rerating_result":"operational_safety_redteam","notes":"Repeated fatal accidents and site shutdowns require 4C-watch; hard 4C if fines/license/site shutdown materially impair business."}
{"case_id":"r10_loop11_hyundai_steel_rebar_construction_demand_watch","symbol":"004020","company_name":"Hyundai Steel / rebar construction demand proxy","case_type":"4c_watch","primary_archetype":"BUILDING_MATERIALS_DEMAND_CYCLE","stage4c_date":"2024-06-21","price_validation":{"price_data_source":"MarketWatch reported price/target/estimate anchor","stage3_price":null,"event_price_anchor_krw":29000,"event_mae_pct":-1.2,"implied_pre_event_reference_price_krw":29352,"target_price_krw":30000,"target_cut_pct":-14,"implied_prior_target_krw":34884,"target_upside_from_event_price_pct":3.45,"net_profit_forecast_2024_krw_bn":215,"net_profit_forecast_cut_pct":-73,"implied_prior_net_profit_forecast_krw_bn":796.3,"rebar_price_expected_decline_pct":-10,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"building_materials_demand_cycle_watch","notes":"Rebar/construction-demand weakness blocks building-material Green until demand, spread and margin stabilize."}
{"case_id":"r10_loop11_daewoo_enc_grand_faw_port_delivery","symbol":"047040","company_name":"Daewoo E&C","case_type":"success_candidate","primary_archetype":"PORT_INFRA_DELIVERY","stage2_date":"2024-11-12","price_validation":{"price_data_source":"Reuters infrastructure-delivery anchor","stage3_price":null,"completed_docks":5,"operation_start_target_year":2026,"maximum_capacity_target_mn_containers":3.5,"capacity_target_year":2028,"development_road_project_value_usd_bn":17,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"port_infrastructure_delivery_watch","notes":"Dock completion is stronger than a mere order headline, but additional backlog, margin and cash collection are required before Stage 3."}
```

## shadow weight row 초안

```csv
archetype,signed_contract,progress_revenue,epc_margin,cash_collection,working_capital,handover_milestone,tenant_noi_affo,power_water_permitting,pf_cleanup,safety_trust,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
OVERSEAS_EPC_MEGA_ORDER,+5,+5,+5,+5,+5,+3,+0,+0,+0,+3,-3,+5,+4,Samsung E&A Fadhili is Stage 2 and 4B until margin/cash collection confirm.
GAS_INFRA_DELIVERY_VALIDATION,+5,+5,+5,+5,+5,+4,+0,+0,+0,+3,-2,+4,+4,Hyundai E&C Jafurah milestone is Stage 2; company package/margin/FCF required.
AI_DATA_CENTER_REAL_ASSET,+3,+2,+3,+4,+4,+0,+5,+5,+0,+3,-5,+5,+4,AI data center theme requires tenant, NOI/AFFO, power/water and permitting.
HOUSING_POLICY_SUPPLY_EVENT,+2,+2,+3,+3,+3,+0,+0,+0,+4,+2,-5,+5,+4,Housing policy is not Green before presales/margin/PF/FCF confirm.
REAL_ESTATE_PF_CREDIT_BREAK,+0,+0,+0,+0,+0,+0,+0,+0,+5,+2,0,+3,+5,PF delinquency spike and builder liquidity support are hard 4C/crisis relief.
CONSTRUCTION_SAFETY_REGULATORY_4C,+0,+0,+0,+0,+0,+0,+0,+0,+0,+5,0,+3,+5,Repeated fatal accidents create fine/license risk and block Green.
BUILDING_MATERIALS_DEMAND_CYCLE,+2,+0,+4,+4,+4,+0,+0,+0,+3,+2,-4,+4,+4,Hyundai Steel rebar weakness requires demand/spread/margin stabilization.
PORT_INFRA_DELIVERY,+5,+5,+5,+5,+5,+5,+0,+0,+0,+3,-2,+3,+4,Daewoo Grand Faw dock completion is Stage 2 but needs new backlog/margin/cash collection.
```

---

# 이번 R10 Loop 11 결론

R10은 **수주와 정책이 가장 그럴듯해 보이지만, 실제 돈으로 닫히기 전까지는 Green을 늦게 줘야 하는 섹터**다.

```text
1. Samsung E&A Fadhili는 좋은 Stage 2다.
   하지만 +8.5% 계약 rally는 margin/working capital 전 4B-watch다.

2. Hyundai E&C Jafurah는 gas infra Stage 2다.
   프로젝트 milestone은 있지만 company-level package와 cashflow 확인 전 Stage 3는 아니다.

3. AI data center real asset은 R10의 새 구조 후보지만,
   tenant, NOI/AFFO, power/water/permitting 전에는 theme에 가깝다.

4. Seoul housing policy는 policy event다.
   presales, margin, PF stability, FCF 전 Green 금지다.

5. Construction PF는 hard 4C다.
   연체율 +629.7%와 40.6T won support는 crisis relief다.

6. POSCO E&C / DL Construction safety regulation은 4C-watch다.
   반복 사망사고가 벌금·면허취소로 이어지면 hard 4C다.

7. Hyundai Steel rebar proxy는 건자재 demand 4C-watch다.
   순이익 추정치 -73%와 철근 -10%는 건설수요 약화를 직접 보여준다.

8. Daewoo E&C Grand Faw Port는 delivery Stage 2다.
   dock completion은 좋지만 추가 backlog, margin, cash collection 전 Stage 3는 아니다.
```

한 문장으로 압축하면:

> **R10에서 진짜 Stage 3는 “수주·정책·데이터센터·항만·주택공급이 있다”가 아니라, 그 이벤트가 공정률·마진·현금회수·tenant/NOI/AFFO로 잠기고 PF·안전·funding cost를 통과하는 순간이다.**

[1]: https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4?utm_source=chatgpt.com "Samsung E&A Shares Rise on $6 Billion Saudi Contract Win"
[2]: https://www.reuters.com/business/energy/aramco-signs-over-25-bln-deals-main-gas-network-jafurah-gas-field-2024-06-30/?utm_source=chatgpt.com "Aramco signs over $25 bln of deals for main gas network and Jafurah gas field"
[3]: https://www.reuters.com/business/retail-consumer/south-korea-says-sk-amazon-invest-5-bln-countrys-biggest-data-centre-2025-06-20/?utm_source=chatgpt.com "South Korea says SK and Amazon to invest $5 billion in country's biggest data centre"
[4]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-tighten-mortgage-rules-seoul-boost-housing-supply-2025-09-07/?utm_source=chatgpt.com "South Korea to tighten mortgage rules in Seoul, boost housing supply"
[5]: https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/?utm_source=chatgpt.com "South Korea prepares financial support for small businesses, builders"
[6]: https://www.reuters.com/sustainability/sustainable-finance-reporting/south-korea-fine-companies-up-5-profit-recurring-fatal-accidents-ministry-says-2025-09-15/?utm_source=chatgpt.com "South Korea to fine companies up to 5% of profit for recurring fatal accidents, ministry says"
[7]: https://www.marketwatch.com/story/hyundai-steel-s-2024-earnings-could-be-hit-by-weak-demand-market-talk-bcbe77c8?utm_source=chatgpt.com "Hyundai Steel's 2024 Earnings Could Be Hit by Weak Demand -- Market Talk"
[8]: https://www.reuters.com/world/middle-east/iraq-shortlists-11-firms-grand-faw-port-operation-decision-january-2025-2024-11-12/?utm_source=chatgpt.com "Iraq shortlists 11 firms for Grand Faw port operation, decision in January 2025"
