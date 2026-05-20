순서상 이번은 **R10 Loop 13 — 건설·부동산·건자재 가격경로 검증 라운드**다.

```text
round = R10 Loop 13
round_id = round_207
large_sector = CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true_for_sector_safety_reference
direct_listed_hard_4c_confirmed = false
next_round = R11 Loop 13
```

이번 R10은 **부동산 PF/건설사 유동성, 해외 EPC 수주, 원전 인프라 수주, 철강·건자재 수요, 서울 부동산 규제, 건설현장 안전사고**를 같이 본다.

이번에도 KRX/Naver/Yahoo/Stooq 기준 **수정주가 일봉 OHLC 전체 구간**은 안정적으로 확보하지 못했다. 그래서 30D/90D/180D/1Y full MFE·MAE는 임의로 만들지 않고, Reuters/WSJ/MarketWatch가 제공한 **event return, event price, 수주금액, 정책금액, PF 연체율, 건설 안전사고 anchor**만 계산했다. full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R10 = 건설·부동산·건자재
```

R10에서 진짜 Stage 3는 “PF 지원”, “해외수주”, “원전수주”, “아파트 가격 상승”, “금리인하”, “건자재 가격 반등”이라는 말이 아니다.

진짜 Stage 3는 아래가 닫히는 순간이다.

```text
건설사:
수주 → 착공 → 공정률 → 원가율 → 운전자본 → 미청구공사 / 매출채권 회수 → FCF

부동산:
분양률 → PF 차환 → 미분양 해소 → 입주 리스크 해소 → 금융비용 안정

건자재:
실수요 물량 → 가격전가 → 원재료비 / 전력비 / 인건비 → spread → 현금흐름

인프라:
preferred bidder / 정책지원이 아니라 최종계약, EPC margin, funding, legal risk, completion risk
```

---

# 2. 대상 canonical archetype

```text
REAL_ESTATE_PF_LIQUIDITY_4C_WATCH
OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN
NUCLEAR_INFRA_PREFERRED_BIDDER_STAGE2
CONSTRUCTION_MATERIAL_DEMAND_BREAK
SEOUL_PROPERTY_POLICY_EVENT_PREMIUM
CONSTRUCTION_SAFETY_HARD_REFERENCE
STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK
HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF
```

---

# 3. deep sub-archetype

```text
PF / 주택:
- Taeyoung E&C workout reference
- real estate project financing delinquency
- market stabilisation fund
- syndicated loan 1T → 5T won
- profitable projects only support
- house-price rebound vs household debt gate

해외 EPC:
- Samsung E&A / GS E&C
- Saudi Aramco Fadhili gas plant
- $7.7B total project
- Samsung E&A estimated $6B contract
- order headline vs EPC margin / working capital / completion risk

원전 인프라:
- KHNP / KEPCO / Doosan Enerbility / KEPCO E&C
- Czech nuclear preferred bidder
- $8.65B per unit cost estimate / up to $18B project context
- legal appeals from EDF / Westinghouse
- preferred bidder ≠ final contract

건자재 / 철강:
- Hyundai Steel rebar / steel plate
- construction and shipbuilding weak demand
- rebar price forecast -10%
- net-profit forecast cut -73%
- steel plate anti-dumping relief vs U.S. tariff export risk

부동산 정책:
- Seoul land-transaction permit zone
- Gangnam / Seocho / Songpa / Yongsan
- mortgage tightening / household debt
- rate-cut cycle constrained by property-price risk

안전:
- Anseong highway bridge construction collapse
- fatal construction-site accident
- hard gate for contractors and civil-engineering projects
```

---

# 4. 국장 신규 후보 case

## Case A — Real-estate PF / Taeyoung E&C reference `4C-watch + policy relief`

```text
symbol = 009410 / builders-PF basket
case_type = 4C-watch + policy_relief
archetype = REAL_ESTATE_PF_LIQUIDITY_4C_WATCH
```

### stage date

```text
Stage 1:
2023-12
- Taeyoung Engineering & Construction plans to reschedule debt
- mid-sized builder liquidity trouble becomes sector signal
- real-estate PF rollover risk spreads to non-bank lenders

Stage 4C-watch:
2024-03-27
- government prepares 40.6T won support for small businesses and builders
- construction firms receive guarantees, extra loans and market-stabilising fund support
- support targeted to profitable real-estate projects
- Taeyoung debt rescheduling cited as liquidity-risk trigger

Stage 4C-watch 강화:
2024-05-13
- real-estate project delinquency rate rises to 2.70% at end-2023
- from 1.19% a year earlier and 0.37% at end-2021
- FSS expands and toughens profitability/risk assessments
- commercial banks and insurers prepare 1T won syndicated loan, expandable to 5T won

Stage 3:
없음
- PF 지원책은 relief
- 건설사 Green은 PF 차환, 미분양 해소, 분양률, 원가율, 현금회수 확인 후
```

PF case는 R10에서 가장 중요한 4C-watch다. 정부가 40.6조 원 지원책을 마련했지만, 이건 구조적 Green이 아니라 유동성 방어다. FSS는 부동산 PF 연체율이 2021년 말 0.37%에서 2023년 말 2.70%로 올라갔다고 밝혔고, 1조 원 syndicated loan을 필요 시 5조 원까지 늘릴 수 있게 준비했다. 즉 PF score는 “정부가 막아준다”보다 “어느 프로젝트가 실제로 살아남는가”를 봐야 한다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters PF/liquidity support and FSS restructuring anchors",
  "entry_date": "N/A",
  "stage3_price": null,
  "government_support_krw_trn": 40.6,
  "pf_delinquency_end_2021_pct": 0.37,
  "pf_delinquency_end_2022_pct": 1.19,
  "pf_delinquency_end_2023_pct": 2.70,
  "pf_delinquency_increase_2021_to_2023_pct": 629.7,
  "pf_delinquency_increase_2022_to_2023_pct": 126.9,
  "syndicated_loan_initial_krw_trn": 1.0,
  "syndicated_loan_max_krw_trn": 5.0,
  "taeyoung_reference": "debt rescheduling trigger for builder liquidity concern",
  "stage3_mfe_mae": "N/A",
  "price_validation_status": "sector_policy_anchor_not_full_ohlc"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch_plus_policy_relief
rerating_result = real_estate_PF_liquidity_watch
stage_failure_type = liquidity_support_not_cashflow_green
```

---

## Case B — Samsung E&A / GS E&C Fadhili `overseas EPC Stage 2 + 4B-watch`

```text
symbols = 028050 / 006360
case_type = success_candidate + event_premium
archetype = OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN
```

### stage date

```text
Stage 1:
2024-04-02
- Saudi Aramco Fadhili gas expansion
- overseas plant EPC order cycle
- Korean EPC contractors participate in gas infrastructure expansion

Stage 2:
2024-04-02 / 2024-04-03
- Aramco awards $7.7B contracts
- Samsung E&A and GS E&C among EPC contractors
- Fadhili gas plant capacity to rise from 2.5B scfd to 4.0B scfd
- completion expected November 2027
- additional sulphur production 2,300 metric tons/day

Stage 4B:
2024-04-03
- Samsung E&A shares +8.5% to 26,750 won
- KOSPI -1.4%
- estimated Samsung E&A contract around $6B
- KB Securities target 35,000 won

Stage 3:
없음
- overseas EPC order는 Stage 2
- 원가율, 설계변경, 선수금, 미청구공사, working capital, completion margin 확인 전 Green 금지
```

Fadhili는 R10의 좋은 overseas EPC Stage 2다. Samsung E&A는 $6B로 추정되는 대형 계약을 따냈고, 주가는 당일 +8.5%로 26,750원까지 올랐다. 하지만 EPC는 수주가 끝이 아니라 시작이다. 공정률, cost overrun, variation order, 미청구공사, 현금회수가 닫혀야 Green이다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Aramco Fadhili contract + WSJ Samsung E&A event-return anchor",
  "stage3_price": null,
  "stage2_date": "2024-04-02/2024-04-03",
  "project_total_value_usd_bn": 7.7,
  "samsung_estimated_contract_value_usd_bn": 6.0,
  "samsung_contract_share_of_total_pct": 77.9,
  "fadhili_capacity_before_bscfd": 2.5,
  "fadhili_capacity_after_bscfd": 4.0,
  "capacity_increase_pct": 60.0,
  "additional_sulphur_tpd": 2300,
  "completion_target": "2027-11",
  "samsung_event_price_krw": 26750,
  "samsung_event_mfe_pct": 8.5,
  "implied_prior_price_krw": 24654,
  "kospi_same_context_pct": -1.4,
  "relative_outperformance_pp": 9.9,
  "target_price_krw": 35000,
  "target_upside_from_event_price_pct": 30.8,
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_success_candidate
rerating_result = overseas_EPC_mega_order_stage2
stage_failure_type = order_headline_not_EPC_margin_cash_green
```

---

## Case C — Czech nuclear infrastructure / Doosan Enerbility / KEPCO E&C `success_candidate + legal 4C-watch`

```text
symbols = 034020 / 052690 / 051600 / 015760
case_type = success_candidate + 4C-watch
archetype = NUCLEAR_INFRA_PREFERRED_BIDDER_STAGE2
```

### stage date

```text
Stage 1:
2024-07-17
- KHNP selected as preferred bidder for Czech nuclear project
- first major Korean overseas nuclear order since UAE 2009
- nuclear infrastructure export revival

Stage 2:
2024-07-17
- Czech government picks KHNP for two reactors
- cost estimate: 200B Czech crowns / $8.65B per unit when building two at same site
- final contract/value to be negotiated, target signing by March
- Korean bid cited cost and schedule discipline
- Doosan Enerbility +48% over prior three months
- KEPCO Plant S&E +14%
- KEPCO E&C +41%

Stage 4C-watch:
2024-09-03 / 2024-10-30
- Westinghouse and EDF appeal tender
- Czech anti-monopoly office starts proceedings
- later temporary block on concluding contract
- project expected up to $18B context
- legal disputes could delay final contract

Stage 3:
없음
- preferred bidder는 Stage 2
- final contract, legal clearance, EPC allocation, margin, financing, completion risk 확인 필요
```

Czech nuclear는 R10 인프라의 강한 success_candidate다. 하지만 preferred bidder는 최종계약이 아니다. Reuters는 Doosan Enerbility가 Czech 기대감으로 3개월간 +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% 올랐다고 보도했다. 이후 Westinghouse/EDF appeal과 Czech watchdog temporary block이 나오면서 legal 4C-watch가 붙었다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Czech nuclear preferred-bidder and appeal anchors",
  "stage3_price": null,
  "stage2_date": "2024-07-17",
  "estimated_unit_cost_czk_bn": 200,
  "estimated_unit_cost_usd_bn": 8.65,
  "project_context_max_usd_bn": 18,
  "doosan_enerbility_3m_return_pct": 48,
  "kepco_plant_service_3m_return_pct": 14,
  "kepco_ec_3m_return_pct": 41,
  "final_contract_signed": false,
  "appeal_parties": ["Westinghouse", "EDF"],
  "temporary_contract_block": true,
  "first_reactor_target_context": 2036,
  "mfe_30d_90d_180d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_4C_watch
rerating_result = nuclear_infra_preferred_bidder_stage2
stage_failure_type = preferred_bidder_not_final_contract_green
```

---

## Case D — Hyundai Steel / construction-material demand `evidence_good_but_price_failed`

```text
symbol = 004020
case_type = evidence_good_but_price_failed
archetype = CONSTRUCTION_MATERIAL_DEMAND_BREAK
```

### stage date

```text
Stage 1:
2024-06-21
- weak demand for steel in construction and shipbuilding
- rebar price and steel-plate competition pressure
- construction downturn flows into building-material margin

Stage 4C-watch:
2024-06-21
- Nomura expects reinforcing-bar price to decline 10% in 2024
- competition from Japanese and Chinese steelmakers in shipbuilding steel plates
- 2024 net-profit estimate cut 73% to 215B won
- target price cut 14% to 30,000 won
- shares -1.2% to 29,000 won

Stage 2 relief:
2025-02-20
- Korea provisionally imposes 27.91~38.02% anti-dumping tariffs on Chinese steel plates
- Hyundai Steel +5.8%
- POSCO +3.9%
- KOSPI -0.7%

Stage 3:
없음
- tariff relief is not Green
- rebar demand, construction volume, spread, inventory, FCF 확인 필요
```

Hyundai Steel은 R10 건자재 수요 break case다. 건설·조선 수요 부진으로 rebar 가격 -10%가 예상됐고, 순이익 전망은 73% 삭감됐다. 이후 중국산 steel plate anti-dumping tariff로 주가는 +5.8% 반등했지만, 이건 relief이지 Green이 아니다. 건자재 Green은 가격 event가 아니라 실제 물량과 spread다. ([마켓워치][4])

### 실제 가격경로 검증

```json
{
  "price_data_source": "MarketWatch Hyundai Steel demand-risk anchor + Reuters steel anti-dumping anchor",
  "stage3_price": null,
  "weak_demand_event_date": "2024-06-21",
  "hyundai_steel_price_krw": 29000,
  "weak_demand_event_mae_pct": -1.2,
  "expected_rebar_price_decline_2024_pct": -10,
  "net_profit_estimate_after_cut_krw_bn": 215,
  "net_profit_estimate_cut_pct": -73,
  "implied_prior_net_profit_estimate_krw_bn": 796.3,
  "target_price_krw": 30000,
  "target_price_cut_pct": -14,
  "target_upside_from_event_price_pct": 3.4,
  "anti_dumping_tariff_pct": "27.91-38.02",
  "anti_dumping_event_mfe_pct": 5.8,
  "kospi_anti_dumping_context_pct": -0.7,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed_then_relief
rerating_result = construction_material_demand_break_watch
stage_failure_type = policy_tariff_relief_not_spread_green
```

---

## Case E — Seoul property regulation / rate-cut cycle `event_premium + macroprudential gate`

```text
symbols = residential developers / REITs / construction-finance basket
case_type = event_premium + 4C-watch
archetype = SEOUL_PROPERTY_POLICY_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2024-07-18
- Seoul and metropolitan-area apartment prices start rising faster
- government vows all-out effort to stabilise real estate
- supply expansion, PF restructuring, household-debt control

Stage 2:
2025-03-19
- Korea tightens apartment trading rules in Gangnam, Seocho, Songpa, Yongsan
- transactions require prior local-council permit until 2025-09-30
- purchase must be for primary residence
- mortgage rules tightened for multiple-home owners
- median Seoul apartment prices doubled over five years and exceeded 1B won

Stage 4C-watch:
2025-03-19 / 2025-06-12 / 2025-11-27
- BOK warns household debt and property prices can limit easing cycle
- excessive rate cuts could revive property-price upswing
- BOK holds rate at 2.50% in November while waiting for property-cooling measures
- won weakness reduces room for cuts

Stage 3:
없음
- 부동산 규제·금리 완화 기대는 event
- developer Green은 분양률, 미분양, PF 차환, 마진, FCF 확인 필요
```

서울 부동산 정책은 R10에서 price premium과 macroprudential gate를 동시에 만든다. 서울 고가 지역 거래허가제 강화는 speculation 억제이고, 금리인하 기대는 부동산 가격을 다시 밀어올릴 수 있어 BOK의 완화 여지를 제한한다. 따라서 건설·REIT basket을 단순 “금리인하 수혜”로 Green 주면 안 된다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters property policy / BOK macroprudential anchors",
  "stage3_price": null,
  "seoul_house_price_mom_june_2024_pct": 0.38,
  "korea_house_price_mom_june_2024_pct": 0.04,
  "land_transaction_permit_areas": ["Gangnam", "Seocho", "Songpa", "Yongsan"],
  "permit_rule_end_date": "2025-09-30",
  "median_seoul_apartment_price_krw_bn": 1.0,
  "median_seoul_price_5y_change": "doubled",
  "household_debt_2024_krw_trn": 1927.3,
  "household_debt_2024_growth_pct": 2.2,
  "bok_rate_nov_2025_pct": 2.50,
  "stage3_mfe_mae": "N/A",
  "price_validation_status": "policy_macro_anchor_not_full_ohlc"
}
```

### alignment

```text
score_price_alignment = event_premium_macroprudential_watch
rerating_result = property_policy_rate_cut_stage2
stage_failure_type = property_policy_not_developer_cashflow_green
```

---

## Case F — Construction-site safety reference / Anseong highway collapse `hard 4C reference`

```text
symbols = civil-engineering / highway contractors / construction-safety basket
case_type = hard_4C_reference
archetype = CONSTRUCTION_SAFETY_HARD_REFERENCE
```

### stage date

```text
Stage 1:
2025-02-25
- highway construction site collapse in Anseong
- steel structures supporting bridge collapse sequentially
- civil-engineering safety and worksite-control risk

Stage 4C-reference:
2025-02-25
- at least 3 dead and 6 injured
- 5 critically injured
- five 50m steel structures collapse after being hoisted by crane
- acting president orders maximum personnel and resources
- transport ministry dispatches officials

Stage 3:
N/A
```

건설 safety는 R10 hard gate다. Reuters는 Anseong highway construction site에서 50m steel structures가 연쇄 붕괴해 최소 3명이 사망하고 6명이 다쳤다고 보도했다. 직접 상장사 price anchor는 확인되지 않았지만, R10 scoring에서는 fatal worksite event를 일반 RedTeam이 아니라 hard reference로 둬야 한다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters construction-site collapse safety anchor",
  "stage3_price": null,
  "event_date": "2025-02-25",
  "fatalities": 3,
  "injured": 6,
  "critically_injured": 5,
  "collapsed_steel_structures": 5,
  "structure_length_meters": 50,
  "collapse_context": "bridge-supporting steel structures collapsed sequentially after being hoisted by crane",
  "listed_company_price_anchor": "price_data_unavailable_after_deep_search",
  "hard_4c_reference": true,
  "mfe_mae": "N/A"
}
```

### alignment

```text
score_price_alignment = thesis_break_reference
rerating_result = construction_safety_hard_reference
stage_failure_type = fatal_worksite_safety_gate
```

---

## Case G — Korean builders liquidity package `policy relief, not Green`

```text
symbols = 000720 / 006360 / 047040 / 375500 / 009410 basket
case_type = success_candidate_policy_relief
archetype = HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF
```

### stage date

```text
Stage 1:
2024-03-27
- builders hurt by high raw material costs and interest rates
- domestic demand weak
- profitable real estate projects still need refinancing support

Stage 2:
2024-03-27
- 40.6T won financial support package
- loan guarantees and lower interest rates for SMEs
- builders get expanded guarantees, extra loans, market-stabilising fund
- support designed to finance profitable projects

Stage 2 추가:
2024-07-18
- government to increase housing supply
- speed up PF restructuring
- control household-debt growth

Stage 3:
없음
- 지원책은 liquidity relief
- 건설주 Green은 profitable-project filtering 후 margin/FCF 회복 확인 필요
```

건설사 liquidity package는 Stage 2 relief다. 정부 지원은 부실 프로젝트를 살리는 Green이 아니라, 살아남을 수 있는 프로젝트의 유동성을 보강하는 장치다. 따라서 R10 scoring은 “지원 규모”보다 “지원 대상 프로젝트의 분양률과 cash collection”을 더 세게 봐야 한다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters builders support / housing supply policy anchors",
  "stage3_price": null,
  "support_package_krw_trn": 40.6,
  "support_tools": [
    "loan guarantees",
    "lower interest rates",
    "expanded guarantees",
    "additional loans",
    "market stabilising fund"
  ],
  "target_projects": "profitable real-estate projects",
  "housing_supply_policy": true,
  "pf_restructuring_policy": true,
  "household_debt_control_policy": true,
  "stage3_mfe_mae": "N/A",
  "price_validation_status": "policy_relief_anchor_not_full_ohlc"
}
```

### alignment

```text
score_price_alignment = success_candidate_policy_relief
rerating_result = builder_liquidity_relief_stage2
stage_failure_type = policy_support_not_project_cashflow_green
```

---

## Case H — Construction steel plate anti-dumping `event premium, not Green`

```text
symbols = 004020 / 005490 / building-steel basket
case_type = event_premium
archetype = STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK
```

### stage date

```text
Stage 1:
2025-02-20
- low-cost Chinese steel plate inflow
- construction / shipbuilding steel material pressure
- domestic producers file complaints

Stage 2:
2025-02-20
- Korea provisionally imposes 27.91~38.02% anti-dumping tariff on Chinese steel plates
- Chinese steel products were $10.4B in 2024
- 49% of Korea’s total steel imports
- Hyundai Steel +5.8%
- POSCO +3.9%
- KOSPI -0.7%

Stage 4C-watch:
2025-02 onward
- U.S. steel/aluminium tariffs can reduce U.S. demand and erode exporter profitability
- domestic relief and export pressure coexist

Stage 3:
없음
- tariff relief is not 건자재 Green
- 실제 물량, 가격전가, 건설 수요, spread, FCF 확인 필요
```

Anti-dumping tariff는 건자재/철강주에 relief를 줬지만, Stage 3는 아니다. Hyundai Steel +5.8%, POSCO +3.9%는 좋은 event reaction이지만, 중국산 dumping relief와 U.S. export-tariff pressure가 동시에 존재한다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters steel plate anti-dumping anchor",
  "stage3_price": null,
  "anti_dumping_tariff_pct": "27.91-38.02",
  "chinese_steel_imports_2024_usd_bn": 10.4,
  "chinese_share_of_total_steel_imports_pct": 49,
  "hyundai_steel_event_mfe_pct": 5.8,
  "posco_event_mfe_pct": 3.9,
  "kospi_same_context_pct": -0.7,
  "hyundai_relative_outperformance_pp": 6.5,
  "posco_relative_outperformance_pp": 4.6,
  "u_s_tariff_export_risk": true,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_policy_relief
rerating_result = construction_steel_material_relief_watch
stage_failure_type = anti_dumping_relief_not_demand_spread_green
```

---

# 5. 이번 R10 case별 stage date 요약

| case                         | Stage 1         | Stage 2           | Stage 3 | Stage 4B                | Stage 4C                      |
| ---------------------------- | --------------- | ----------------- | ------- | ----------------------- | ----------------------------- |
| Real-estate PF / Taeyoung    | 2023-12         | 2024-03/05 relief | N/A     | N/A                     | PF liquidity watch            |
| Samsung E&A / GS E&C Fadhili | 2024-04-02      | 2024-04-03        | N/A     | 2024-04-03              | EPC margin watch              |
| Czech nuclear                | 2024-07-17      | 2024-07-17        | N/A     | nuclear basket rally    | 2024-09/10 legal watch        |
| Hyundai Steel materials      | 2024-06-21      | 2025-02-20 relief | N/A     | anti-dumping rally      | weak demand watch             |
| Seoul property policy        | 2024-07/2025-03 | 2025-03           | N/A     | property/rate-cut watch | household-debt/property watch |
| Anseong construction safety  | 2025-02-25      | N/A               | N/A     | N/A                     | hard reference                |
| Builder liquidity package    | 2024-03-27      | 2024-03-27        | N/A     | policy relief watch     | PF profitability gate         |
| Steel plate anti-dumping     | 2025-02-20      | 2025-02-20        | N/A     | 2025-02-20              | export-tariff watch           |

---

# 6. 실제 가격경로 검증 총괄

| case                    |                                                         anchor | MFE / MAE 해석                       | 판정                             |
| ----------------------- | -------------------------------------------------------------: | ---------------------------------- | ------------------------------ |
| PF / Taeyoung reference |                  PF delinquency 0.37%→2.70%, support 40.6T won | 정책 relief, PF hard watch           | thesis_break_watch             |
| Samsung E&A Fadhili     |                               +8.5% to 26,750 won, KOSPI -1.4% | mega-order event premium           | success_candidate              |
| Czech nuclear           |                      Doosan +48%, KEPCO E&C +41%, appeal block | preferred bidder + legal 4C-watch  | success_candidate              |
| Hyundai Steel demand    |     shares -1.2%, net-profit estimate -73%, later +5.8% relief | weak construction-material demand  | evidence_good_but_price_failed |
| Seoul property policy   | Seoul prices +0.38% MoM, permit zones, household debt 1,927.3T | rate-cut/property macro gate       | event_premium                  |
| Anseong safety          |               3 dead, 6 injured, five 50m structures collapsed | construction safety hard reference | thesis_break_reference         |
| Builder liquidity       |                                                  40.6T support | support not project cashflow       | policy_relief                  |
| Steel anti-dumping      |                                     Hyundai +5.8%, POSCO +3.9% | tariff event not structural demand | event_premium                  |

---

# 7. score-price alignment 판정

```text
success_candidate:
- Samsung E&A / GS E&C Fadhili
- Czech nuclear infrastructure basket

success_candidate_policy_relief:
- builder liquidity package
- Seoul property supply / PF restructuring policy

evidence_good_but_price_failed:
- Hyundai Steel construction-material demand

event_premium:
- Samsung E&A +8.5% Fadhili order reaction
- Doosan/KEPCO nuclear preferred-bidder rally
- steel anti-dumping relief
- Seoul property/rate-cut policy expectations

price_moved_without_evidence:
- nuclear basket if preferred bidder is treated as final EPC Green
- steel plate relief if tariff headline is treated as spread/FCF Green
- construction shares if liquidity support is treated as cashflow recovery

thesis_break_watch:
- PF delinquency / Taeyoung reference
- Czech nuclear legal appeal
- Seoul property overheating / household debt
- EPC working-capital and cost-overrun risk

thesis_break_reference:
- Anseong construction-site fatal collapse

hard_4C_confirmed:
- direct listed hard 4C: false
- sector hard reference: construction-site fatal safety event
```

---

# 8. 점수비중 교정

## 올릴 축

```text
PF_refinancing_success +5
project_profitability_filter +5
pre_sale_ratio +5
unsold_inventory_reduction +5
EPC_margin_visibility +5
working_capital_control +5
unbilled_receivables_control +5
final_contract_signed +5
legal_appeal_clearance +5
construction_safety_trust +5
```

### 왜 올리나

PF case는 연체율이 0.37%에서 2.70%까지 올라간 상태에서 정부가 40.6조 원을 넣은 relief다. 삼성E&A Fadhili는 +8.5% event premium이지만 EPC margin과 working capital이 닫혀야 한다. Czech nuclear는 Doosan +48%, KEPCO E&C +41%로 가격은 먼저 움직였지만 final contract와 legal appeal이 남았다. Anseong collapse는 R10에서 safety가 hard gate임을 보여준다.

## 내릴 축

```text
order_headline_only -5
preferred_bidder_only -5
policy_support_only -5
tariff_relief_only -5
rate_cut_property_expectation_only -5
housing_price_rebound_without_cashflow -4
PF_support_without_profitability -5
EPC_backlog_without_margin -5
safety_incident_unresolved -5
```

### 왜 내리나

수주·preferred bidder·정책지원은 모두 Stage 2다. R10은 현금이 늦게 들어오는 산업이라, headline과 cashflow 사이가 길다. PF 지원은 부실 프로젝트를 살리는 게 아니라 구조조정을 빠르게 하기 위한 장치다. 원전도 final contract와 legal risk를 통과해야 한다.

## Green gate 강화 조건

```text
R10 Stage 3-Green 필수:
1. PF 차환 성공
2. 분양률 / pre-sale ratio 확인
3. 미분양 감소 확인
4. project profitability 확인
5. EPC final contract signed
6. 공정률 / 원가율 / variation order 확인
7. 미청구공사 / 매출채권 / working capital 안정
8. 원전·해외공사는 legal appeal / sovereign funding 통과
9. 건자재는 실수요 물량과 spread 확인
10. safety incident 없음
11. price path가 evidence 이후 따라옴

금지:
수주 headline only
preferred bidder only
정책지원 only
금리인하 기대 only
부동산 가격상승 only
tariff relief only
```

## 4B 조기감지 조건

```text
4B-watch:
해외 EPC 수주일 +5~10% 급등
원전 preferred bidder로 관련주 3개월 +40% 이상
anti-dumping tariff로 건자재/철강주 단기 급등
PF support headline로 건설주 단기 반등
금리인하 기대와 서울 아파트 가격상승으로 건설/REIT basket 선반영

4B-elevated:
final contract 미체결
legal appeal 있음
PF 수익성 assessment 미완료
분양률 / 미분양 자료 없음
EPC cost overrun 가능
미청구공사 증가
건설현장 safety issue
```

## 4C hard gate 조건

```text
PF default / workout / debt rescheduling
project financing delinquency spike
fatal construction-site accident
EPC contract cancellation
sovereign legal appeal blocking contract
cost overrun / unbilled receivables surge
pre-sale failure / unsold inventory spike
rate cuts blocked by property/household debt
construction material demand collapse
```

이번 R10 Loop 13에서는 direct listed hard 4C를 확정하지 않는다. 대신 **PF delinquency / Taeyoung reference**와 **Anseong construction-site fatal accident**를 강한 hard reference로 두고, **Czech nuclear legal appeal**, **Samsung E&A EPC margin**, **Seoul property/household debt gate**를 4C-watch로 둔다.

---

# 9. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 10. 레포 반영용 patch-ready 출력

## docs/round/round_207.md 요약

```md
# R10 Loop 13. Construction / Real Estate / Building Materials Price Validation

이번 라운드는 R10 Loop 13 price-validation 라운드다.

핵심 결론:
- Real-estate PF / Taeyoung reference is 4C-watch plus policy relief. Government support package 40.6T won; PF delinquency rose from 0.37% at end-2021 to 2.70% at end-2023. Banks/insurers prepared a 1T won syndicated loan expandable to 5T won. Policy support is not cashflow Green.
- Samsung E&A / GS E&C Fadhili is overseas EPC Stage 2 plus 4B-watch. Aramco awarded $7.7B contracts; Samsung E&A estimated $6B contract, shares +8.5% to 26,750 won while KOSPI -1.4%. EPC margin and working capital required.
- Czech nuclear infrastructure is preferred-bidder Stage 2 plus legal 4C-watch. Doosan Enerbility +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% over three months. Final contract/legal appeal clearance required.
- Hyundai Steel construction-material demand is evidence_good_but_price_failed. Rebar price expected -10%, net-profit estimate cut -73% to 215B won, shares -1.2% to 29,000 won. Anti-dumping relief later drove +5.8%, but spread/volume needed.
- Seoul property policy is event premium plus macroprudential gate. Seoul house prices rose +0.38% MoM in June 2024; wealthy districts require transaction permits through Sept. 30, 2025; household debt and property-price risk constrain rate cuts.
- Construction-site safety reference is hard gate. Anseong highway construction collapse killed at least 3 and injured 6; five 50m steel structures collapsed sequentially after crane hoisting.
- Builder liquidity package is policy relief, not Green. 40.6T won support includes guarantees, lower rates, extra loans and market-stabilising fund, targeted to profitable projects.
- Steel plate anti-dumping is event premium, not Green. Provisional 27.91~38.02% tariffs drove Hyundai Steel +5.8% and POSCO +3.9%, while KOSPI -0.7%; export-tariff risk remains.
```

## docs/checkpoints/checkpoint_28a_round207_r10_loop13.md 요약

```md
# Checkpoint 28A Round 207 R10 Loop 13 Construction Real Estate Building Materials Price Validation

## 반영 내용
- R10 Loop 13 price-validation 라운드를 추가했다.
- Real-estate PF/Taeyoung reference, Samsung E&A/GS E&C Fadhili EPC, Czech nuclear infrastructure, Hyundai Steel construction-material demand, Seoul property policy, Anseong construction-site safety, builder liquidity support, steel plate anti-dumping relief를 비교했다.
- Reuters / WSJ / MarketWatch anchors로 가능한 event MFE/MAE 및 policy/project metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- PF refinancing success, project profitability filter, pre-sale ratio, unsold inventory reduction, EPC margin visibility, working capital control, unbilled receivables control, final contract signed, legal appeal clearance, construction safety trust 가중치 강화
- order headline-only, preferred bidder-only, policy support-only, tariff relief-only, rate-cut property expectation-only, PF support without profitability, EPC backlog without margin 감점 강화
```

## data/e2r_case_library/cases_r10_loop13_round207.jsonl 초안

```jsonl
{"case_id":"r10_loop13_real_estate_pf_taeyoung_liquidity_watch","symbol":"009410/builders_PF_basket","company_name":"Taeyoung E&C reference / Korea real-estate PF","case_type":"4c_watch_policy_relief","primary_archetype":"REAL_ESTATE_PF_LIQUIDITY_4C_WATCH","stage1_date":"2023-12","stage4c_date":"2024-03-27/2024-05-13_watch","price_validation":{"price_data_source":"Reuters PF/liquidity support and FSS restructuring anchors","stage3_price":null,"government_support_krw_trn":40.6,"pf_delinquency_end_2021_pct":0.37,"pf_delinquency_end_2022_pct":1.19,"pf_delinquency_end_2023_pct":2.70,"pf_delinquency_increase_2021_to_2023_pct":629.7,"pf_delinquency_increase_2022_to_2023_pct":126.9,"syndicated_loan_initial_krw_trn":1.0,"syndicated_loan_max_krw_trn":5.0,"taeyoung_reference":"debt rescheduling trigger for builder liquidity concern","price_validation_status":"sector_policy_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch_plus_policy_relief","rerating_result":"real_estate_PF_liquidity_watch","notes":"Liquidity support is not Green; project profitability, PF refinancing, pre-sale and cash collection required."}
{"case_id":"r10_loop13_samsung_ena_gs_fadhili_epc_order_stage2","symbol":"028050/006360","company_name":"Samsung E&A / GS E&C Fadhili EPC","case_type":"success_candidate_event_premium","primary_archetype":"OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN","stage2_date":"2024-04-02/2024-04-03","stage4b_date":"2024-04-03","price_validation":{"price_data_source":"Reuters Aramco Fadhili contract + WSJ Samsung E&A event-return anchor","stage3_price":null,"project_total_value_usd_bn":7.7,"samsung_estimated_contract_value_usd_bn":6.0,"samsung_contract_share_of_total_pct":77.9,"fadhili_capacity_before_bscfd":2.5,"fadhili_capacity_after_bscfd":4.0,"capacity_increase_pct":60.0,"additional_sulphur_tpd":2300,"completion_target":"2027-11","samsung_event_price_krw":26750,"samsung_event_mfe_pct":8.5,"implied_prior_price_krw":24654,"kospi_same_context_pct":-1.4,"relative_outperformance_pp":9.9,"target_price_krw":35000,"target_upside_from_event_price_pct":30.8,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"overseas_EPC_mega_order_stage2","notes":"Mega-order is Stage 2; EPC margin, cost control, unbilled receivables, working capital and cash collection required."}
{"case_id":"r10_loop13_czech_nuclear_infra_preferred_bidder_legal_watch","symbol":"034020/052690/051600/015760","company_name":"Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E / KEPCO Czech nuclear basket","case_type":"success_candidate_4c_watch","primary_archetype":"NUCLEAR_INFRA_PREFERRED_BIDDER_STAGE2","stage2_date":"2024-07-17","stage4c_date":"2024-09-03/2024-10-30_watch","price_validation":{"price_data_source":"Reuters Czech nuclear preferred-bidder and appeal anchors","stage3_price":null,"estimated_unit_cost_czk_bn":200,"estimated_unit_cost_usd_bn":8.65,"project_context_max_usd_bn":18,"doosan_enerbility_3m_return_pct":48,"kepco_plant_service_3m_return_pct":14,"kepco_ec_3m_return_pct":41,"final_contract_signed":false,"appeal_parties":["Westinghouse","EDF"],"temporary_contract_block":true,"first_reactor_target_context":2036,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_4C_watch","rerating_result":"nuclear_infra_preferred_bidder_stage2","notes":"Preferred bidder is Stage 2; final contract, legal clearance, EPC allocation, margin and financing required."}
{"case_id":"r10_loop13_hyundai_steel_construction_material_demand_break","symbol":"004020","company_name":"Hyundai Steel","case_type":"evidence_good_but_price_failed","primary_archetype":"CONSTRUCTION_MATERIAL_DEMAND_BREAK","stage4c_date":"2024-06-21_watch","stage2_date":"2025-02-20_relief","price_validation":{"price_data_source":"MarketWatch Hyundai Steel demand-risk anchor + Reuters steel anti-dumping anchor","stage3_price":null,"weak_demand_event_date":"2024-06-21","hyundai_steel_price_krw":29000,"weak_demand_event_mae_pct":-1.2,"expected_rebar_price_decline_2024_pct":-10,"net_profit_estimate_after_cut_krw_bn":215,"net_profit_estimate_cut_pct":-73,"implied_prior_net_profit_estimate_krw_bn":796.3,"target_price_krw":30000,"target_price_cut_pct":-14,"target_upside_from_event_price_pct":3.4,"anti_dumping_tariff_pct":"27.91-38.02","anti_dumping_event_mfe_pct":5.8,"kospi_anti_dumping_context_pct":-0.7,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed_then_relief","rerating_result":"construction_material_demand_break_watch","notes":"Weak construction demand cut profit estimates; tariff relief is not Green without demand, spread and FCF."}
{"case_id":"r10_loop13_seoul_property_policy_ratecut_macro_gate","symbol":"residential_developers_REITs_construction_finance_basket","company_name":"Seoul property policy / rate-cut macroprudential basket","case_type":"event_premium_4c_watch","primary_archetype":"SEOUL_PROPERTY_POLICY_EVENT_PREMIUM","stage1_date":"2024-07-18","stage2_date":"2025-03-19","stage4c_date":"2025_macroprudential_watch","price_validation":{"price_data_source":"Reuters property policy / BOK macroprudential anchors","stage3_price":null,"seoul_house_price_mom_june_2024_pct":0.38,"korea_house_price_mom_june_2024_pct":0.04,"land_transaction_permit_areas":["Gangnam","Seocho","Songpa","Yongsan"],"permit_rule_end_date":"2025-09-30","median_seoul_apartment_price_krw_bn":1.0,"median_seoul_price_5y_change":"doubled","household_debt_2024_krw_trn":1927.3,"household_debt_2024_growth_pct":2.2,"bok_rate_nov_2025_pct":2.50,"price_validation_status":"policy_macro_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_macroprudential_watch","rerating_result":"property_policy_rate_cut_stage2","notes":"Property/rate-cut expectations are not Green until pre-sale, unsold inventory, PF refinancing and developer FCF confirm."}
{"case_id":"r10_loop13_anseong_highway_construction_safety_reference","symbol":"civil_engineering_construction_safety_basket","company_name":"Anseong highway construction collapse reference","case_type":"hard_4c_reference","primary_archetype":"CONSTRUCTION_SAFETY_HARD_REFERENCE","stage4c_date":"2025-02-25","price_validation":{"price_data_source":"Reuters construction-site collapse safety anchor","stage3_price":null,"fatalities":3,"injured":6,"critically_injured":5,"collapsed_steel_structures":5,"structure_length_meters":50,"collapse_context":"bridge-supporting steel structures collapsed sequentially after being hoisted by crane","listed_company_price_anchor":"price_data_unavailable_after_deep_search","hard_4c_reference":true,"price_validation_status":"sector_safety_reference"},"score_price_alignment":"thesis_break_reference","rerating_result":"construction_safety_hard_reference","notes":"Fatal construction-site accident is R10 hard reference; safety trust is mandatory gate."}
{"case_id":"r10_loop13_builder_liquidity_package_policy_relief","symbol":"000720/006360/047040/375500/009410_basket","company_name":"Korean builders liquidity support package","case_type":"success_candidate_policy_relief","primary_archetype":"HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF","stage2_date":"2024-03-27","price_validation":{"price_data_source":"Reuters builders support / housing supply policy anchors","stage3_price":null,"support_package_krw_trn":40.6,"support_tools":["loan guarantees","lower interest rates","expanded guarantees","additional loans","market stabilising fund"],"target_projects":"profitable real-estate projects","housing_supply_policy":true,"pf_restructuring_policy":true,"household_debt_control_policy":true,"price_validation_status":"policy_relief_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_policy_relief","rerating_result":"builder_liquidity_relief_stage2","notes":"Support package is relief only; profitable-project filtering, margin and cash collection required."}
{"case_id":"r10_loop13_steel_plate_anti_dumping_construction_relief","symbol":"004020/005490/building_steel_basket","company_name":"Hyundai Steel / POSCO Holdings / construction steel plate basket","case_type":"event_premium_policy_relief","primary_archetype":"STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK","stage2_date":"2025-02-20","stage4c_date":"export_tariff_watch","price_validation":{"price_data_source":"Reuters steel plate anti-dumping anchor","stage3_price":null,"anti_dumping_tariff_pct":"27.91-38.02","chinese_steel_imports_2024_usd_bn":10.4,"chinese_share_of_total_steel_imports_pct":49,"hyundai_steel_event_mfe_pct":5.8,"posco_event_mfe_pct":3.9,"kospi_same_context_pct":-0.7,"hyundai_relative_outperformance_pp":6.5,"posco_relative_outperformance_pp":4.6,"u_s_tariff_export_risk":true,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_policy_relief","rerating_result":"construction_steel_material_relief_watch","notes":"Anti-dumping relief is event premium; demand volume, spread and FCF required before Green."}
```

## data/sector_taxonomy/score_weight_profiles_round207_r10_loop13_v1.csv 초안

```csv
archetype,pf_refinancing_success,project_profitability_filter,pre_sale_ratio,unsold_inventory_reduction,epc_margin_visibility,working_capital_control,unbilled_receivables_control,final_contract_signed,legal_appeal_clearance,construction_safety_trust,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
REAL_ESTATE_PF_LIQUIDITY_4C_WATCH,+5,+5,+5,+5,+1,+5,+5,+1,+2,+3,0,+4,+5,PF support is relief; refinancing/pre-sale/cash collection are core gates.
OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN,+1,+3,+0,+0,+5,+5,+5,+5,+4,+4,-5,+5,+5,Fadhili shows order headline is not EPC margin/cashflow Green.
NUCLEAR_INFRA_PREFERRED_BIDDER_STAGE2,+1,+3,+0,+0,+5,+5,+5,+5,+5,+4,-5,+5,+5,Czech nuclear needs final contract, legal clearance, funding and EPC margin.
CONSTRUCTION_MATERIAL_DEMAND_BREAK,+2,+3,+2,+2,+1,+4,+3,+2,+2,+3,0,+4,+4,Hyundai Steel shows weak construction demand can break building-material margin.
SEOUL_PROPERTY_POLICY_EVENT_PREMIUM,+5,+5,+5,+5,+0,+4,+4,+0,+0,+2,-5,+5,+4,Property/rate-cut headlines need pre-sale, inventory and PF cashflow confirmation.
CONSTRUCTION_SAFETY_HARD_REFERENCE,+0,+0,+0,+0,+0,+0,+0,+0,+0,+5,0,+3,+5,Fatal worksite accidents are hard reference for R10.
HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF,+5,+5,+5,+5,+1,+5,+5,+1,+1,+3,-5,+4,+4,Builder support package is relief until project cashflow proves out.
STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK,+2,+3,+2,+2,+1,+4,+3,+2,+2,+3,-5,+5,+4,Tariff relief is not Green without construction demand, spread and export-risk control.
```

---

# 이번 R10 Loop 13 결론

```text
1. Real-estate PF는 R10의 핵심 4C-watch다.
   PF 연체율 0.37% → 2.70%, 정부지원 40.6T won은 Green이 아니라 liquidity relief다.

2. Samsung E&A / GS E&C Fadhili는 해외 EPC Stage 2다.
   Samsung E&A +8.5%는 강한 event reaction이지만, EPC margin과 working capital 전에는 Stage 3 금지다.

3. Czech nuclear는 strong success_candidate다.
   Doosan +48%, KEPCO E&C +41%가 나왔지만 preferred bidder일 뿐이고 legal appeal이 남아 있다.

4. Hyundai Steel은 건자재 demand break다.
   construction demand weakness로 net-profit estimate -73%, shares -1.2%; tariff relief는 별도 event다.

5. Seoul property policy는 event premium + macroprudential gate다.
   집값 상승과 금리인하 기대가 있어도 household debt와 규제 때문에 Green이 아니다.

6. Anseong construction collapse는 R10 safety hard reference다.
   fatal worksite event는 수주·PF보다 먼저 보는 hard gate다.

7. Builder liquidity package는 policy relief다.
   지원 대상이 profitable project인지, 분양률과 현금회수가 되는지가 중요하다.

8. Steel plate anti-dumping은 건자재 relief지만 Stage 3가 아니다.
   실제 수요·가격전가·spread·FCF가 확인되어야 한다.
```

한 문장으로 압축하면:

> **R10에서 진짜 Stage 3는 “PF 지원·해외수주·원전 preferred bidder·부동산 가격상승·tariff relief가 있다”가 아니라, PF 차환·분양률·EPC margin·working capital·final contract·건자재 spread·safety trust가 실제 숫자로 닫히는 순간이다.**

[1]: https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/?utm_source=chatgpt.com "South Korea prepares financial support for small businesses, builders"
[2]: https://www.reuters.com/markets/commodities/aramco-awards-77-bln-contracts-fadhili-gas-expansion-2024-04-02/?utm_source=chatgpt.com "Aramco awards $7.7 bln in contracts for Fadhili gas expansion"
[3]: https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/?utm_source=chatgpt.com "South Korea's winning bid for Czech nuclear power project"
[4]: https://www.marketwatch.com/story/hyundai-steel-s-2024-earnings-could-be-hit-by-weak-demand-market-talk-bcbe77c8?utm_source=chatgpt.com "Hyundai Steel's 2024 Earnings Could Be Hit by Weak Demand -- Market Talk"
[5]: https://www.reuters.com/markets/asia/south-korea-vows-all-out-effort-stabilise-rising-house-prices-2024-07-18/?utm_source=chatgpt.com "South Korea vows all-out effort to stabilise rising house prices"
[6]: https://www.reuters.com/world/asia-pacific/three-people-dead-five-hurt-south-korea-highway-construction-site-yonhap-says-2025-02-25/?utm_source=chatgpt.com "At least three dead in South Korea highway construction project collapse"
[7]: https://www.reuters.com/markets/asia/south-korea-provisionally-slaps-tariffs-chinese-steel-plates-dumping-2025-02-20/?utm_source=chatgpt.com "South Korea provisionally slaps tariffs on Chinese steel plates for dumping"
