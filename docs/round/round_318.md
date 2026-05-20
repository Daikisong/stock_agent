순서상 이번은 **R10 Loop 16 — 건설·부동산·건자재 trigger-level price validation 라운드**다.

이번 R10은 **해외 EPC 수주, 국내 주택공급, PF 구조조정, 건설 안전, 건자재·철강 input, 데이터센터·반도체 fab 시공**을 한 프레임으로 섞으면 안 된다. 건설주는 겉으로는 “수주”처럼 보이지만 실제 가격은 **수주잔고 → 마진 → 원가·공기 리스크 → 현금흐름 → PF·안전·금리 리스크**에서 갈린다.

```text
round = R10 Loop 16
round_id = round_246
large_sector = CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R11 Loop 16
```

이번 라운드도 KRX/Naver/Yahoo/Stooq 수정주가 일봉 OHLC 30D/90D/180D/1Y/2Y window는 안정적으로 확보하지 못했다. 그래서 full MFE/MAE는 만들지 않고 `price_data_unavailable_after_deep_search`로 분리한다. 대신 Reuters/WSJ/AP/WaPo의 **reported event return, event price, contract value, project value, PF delinquency, policy size, accident/fatality data**를 trigger anchor로 쓴다.

---

# 1. 이번 라운드 대섹터

```text
R10 = 건설·부동산·건자재
```

R10의 핵심 gate는 아래다.

```text
해외 EPC:
contract value → backlog → gross margin → working capital → cost escalation → completion risk

국내 주택:
housing supply policy → reconstruction easing → permits → pre-sales → PF refinancing → completion / occupancy

PF 구조조정:
PF delinquency → builder liquidity → guarantees → project profitability assessment → write-down → workout / default

건설 안전:
fatal accident → work suspension → license risk → operating-profit fine → compensation → brand/pre-sale risk

건자재:
steel/cement/material price → input cost → pass-through → public-project margin → anti-dumping / tariff

AI fab / data center construction:
domestic capex → builder backlog → schedule / materials → margin → customer demand durability
```

---

# 2. 대상 canonical archetype

```text
MIDDLE_EAST_EPC_BACKLOG_STAGE2_ACTIONABLE
MEGA_GAS_PIPELINE_EPC_STAGE2_WITH_MARGIN_GATE
PF_LIQUIDITY_RESTRUCTURING_4C_AND_RELIEF
HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_WITH_LTV_4B
CONSTRUCTION_SAFETY_HARD_4C
AI_FAB_CONSTRUCTION_STAGE2
BUILDING_MATERIAL_INPUT_COST_STAGE2_4B
RATE_CUT_HOUSING_POLICY_MIXED_STAGE2_4B
```

---

# 3. deep sub-archetype

```text
Samsung E&A / GS E&C:
- Aramco Fadhili gas expansion contracts worth $7.7B.
- Samsung E&A took about $6B share.
- Samsung E&A shares +8.5% to 26,750 won while KOSPI -1.4%.
- Fadhili gas capacity expansion from 2.5B scf/day to 4B scf/day.
- Completion expected Nov 2027.
- Stage2-Actionable EPC backlog, but Green requires margin and execution.

Hyundai E&C / Jafurah / main gas network:
- Aramco signed more than $25B contracts for Jafurah expansion and main gas network.
- Hyundai E&C consortium involved in Jafurah expansion.
- Jafurah expected 2B scf/day sales gas by 2030.
- Main gas network adds 4,000 km pipelines and 3.2B scf/day capacity.
- Stage2 mega-backlog, but no direct price anchor.

PF / Taeyoung / builders:
- Korea prepared 40.6T won support for SMEs and builders.
- Builder support through expanded guarantees, loans, market-stabilizing fund.
- Taeyoung E&C debt rescheduling triggered sector liquidity concern.
- FSS tightened PF project assessments.
- Real-estate PF delinquency rate rose to 2.70% end-2023 from 0.37% end-2021.
- Syndicated loan 1T won, expandable to 5T won.
- This is 4C-watch plus policy-relief Stage2.

Housing supply / reconstruction:
- Seoul LTV tightened from 50% to 40% in Gangnam/Yongsan.
- Government also plans to use state-run land and streamline reconstruction.
- Earlier Seoul prices rose 0.76% MoM, strongest since Dec 2019.
- Government targeted 400,000+ new homes over six years.
- Stage2 supply/reconstruction trigger, but demand-control 4B.

Construction safety:
- 2025 Anseong/Cheonan highway bridge collapse killed 4 workers.
- Hyundai Engineering was in charge of the site.
- Korea later proposed fines up to 5% of operating profit for companies with more than three worker deaths a year.
- Construction firms repeatedly suspended for fatal accidents could lose licenses.
- Hard 4C safety gate.

Samsung C&T / P5 fab construction:
- Samsung to add P5 semiconductor production line in Pyeongtaek.
- Parent group to invest 450T won in Korea over five years.
- P5 had been delayed since late 2023 and mass production is planned for 2028.
- Builder in public filings: Samsung C&T.
- Stage2 AI/fab construction backlog, but direct Samsung C&T price anchor unavailable.

Building-material / steel plate:
- Korea recommended 27.91~38.02% provisional anti-dumping duties on Chinese steel plates used in shipbuilding and construction.
- Hyundai Steel +5.8%, POSCO Holdings +3.9%, KOSPI -0.7%.
- For builders this is mixed: domestic steel/material suppliers benefit; construction input costs may rise.
```

---

# 4. 선정 case 요약

| bucket                     | case                                                      | 핵심 판정                                                                       |
| -------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------- |
| Stage2-Actionable          | Samsung E&A / Fadhili gas                                 | $6B contract, +8.5%, KOSPI -1.4%. EPC 수주 trigger는 강함                        |
| Stage2                     | Hyundai E&C / Jafurah gas                                 | Aramco $25B+ package, Hyundai E&C consortium 포함. 가격 anchor 없음               |
| failed_rerating / 4C-watch | PF / Taeyoung / builders                                  | PF delinquency 2.70%, Taeyoung debt rescheduling, builders liquidity stress |
| Stage2 relief + 4B         | Housing supply / reconstruction                           | 공급확대·재건축 완화는 Stage2, LTV 40% demand curb는 4B                                |
| hard 4C                    | Construction safety / Hyundai Engineering bridge collapse | 4명 사망, license/fine risk. 안전 hard gate                                      |
| Stage2                     | Samsung C&T / P5 fab construction                         | Pyeongtaek P5 재개, 450T won domestic investment. 가격 anchor 없음                |
| mixed Stage2/4B            | Steel plate anti-dumping                                  | 건자재 supplier에는 positive, builders input cost에는 4B                           |
| macro 4B                   | BOK rate-cut vs housing overheating                       | 금리인하 기대는 부동산 relief지만, 서울 과열·원화 약세·건설경기 둔화가 섞임                              |

---

# 5. Case별 trigger grid

## Case A — Samsung E&A / Aramco Fadhili gas expansion

```text
symbol = 028050
case_type = Stage2-Actionable EPC backlog
archetype = MIDDLE_EAST_EPC_BACKLOG_STAGE2_ACTIONABLE
```

| trigger |                    type | date       | 당시 공개 evidence                                                                            | 가격 anchor                                    | outcome    |
| ------- | ----------------------: | ---------- | ----------------------------------------------------------------------------------------- | -------------------------------------------- | ---------- |
| T0      |         Stage2 evidence | 2024-04-02 | Aramco awards $7.7B Fadhili gas expansion contracts to Samsung Engineering, GS E&C, Nesma | no price                                     |            |
| T1      |       Stage2-Actionable | 2024-04-03 | Samsung E&A signs around $6B contract share                                               | Samsung E&A +8.5% to 26,750 won, KOSPI -1.4% | excellent  |
| T2      |              validation | 2024-04-03 | Fadhili processing capacity to rise from 2.5B to 4B scf/day; completion Nov 2027          | same                                         | validation |
| T3      | Stage3-Yellow candidate | 2024~2027  | backlog large enough vs annual average contract wins, but margin/execution missing        | no Yellow                                    |            |
| T4      |                4B-watch | 2024~2027  | cost escalation, Middle East execution, working capital, claims risk                      | 4B                                           |            |
| T5      |            Stage3-Green | N/A        | project margin, cash conversion, full OHLC unavailable                                    | no Green                                     |            |

Samsung E&A는 이번 R10에서 가장 선명한 Stage2-Actionable이다. Aramco는 Fadhili gas plant expansion에 $7.7B EPC contracts를 부여했고, Samsung Engineering/Samsung E&A와 GS E&C가 수주자에 포함됐다. WSJ는 Samsung E&A가 약 $6B 규모를 따냈고, 주가가 장중 +8.5%로 26,750원까지 올랐으며, 같은 구간 KOSPI는 -1.4%였다고 보도했다. 이 정도면 “수주가 실제 주가를 밀었다”는 trigger-level alignment가 강하다. 다만 EPC는 계약금액이 끝이 아니라 **gross margin, working capital, claim, 공기 지연**이 Green gate다. ([Reuters][1])

```json
{
  "case_id": "r10_loop16_samsung_ea_fadhili",
  "symbol": "028050",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_EPC_backlog",
  "trigger_date": "2024-04-03",
  "aramco_total_contract_value_usd_bn": 7.7,
  "samsung_contract_value_context_usd_bn": 6.0,
  "event_return_pct": 8.5,
  "event_price_krw": 26750,
  "kospi_same_context_pct": -1.4,
  "market_relative_return_pp": 9.9,
  "fadhili_capacity_before_bscfd": 2.5,
  "fadhili_capacity_after_bscfd": 4.0,
  "completion_target": "2027-11",
  "stage3_gate_missing": [
    "project_gross_margin",
    "working_capital_profile",
    "cost_escalation_control",
    "claim_risk",
    "execution_progress",
    "full_OHLC_MFE_MAE"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_EPC_contract"
}
```

---

## Case B — Hyundai E&C / Aramco Jafurah + main gas network

```text
symbol = 000720
case_type = Stage2 mega-gas EPC backlog
archetype = MEGA_GAS_PIPELINE_EPC_STAGE2_WITH_MARGIN_GATE
```

| trigger |            type | date       | 당시 공개 evidence                                                                  | 가격 anchor            | outcome |
| ------- | --------------: | ---------- | ------------------------------------------------------------------------------- | -------------------- | ------- |
| T0      | Stage2 evidence | 2024-06-30 | Aramco signs $25B+ contracts for Jafurah phase 2 and main gas network expansion | no Hyundai E&C price |         |
| T1      |      validation | 2024-06-30 | Jafurah has 229T cubic feet gas and 75B barrels condensates                     | no price             |         |
| T2      |      validation | 2024-06-30 | main gas network adds 4,000 km pipelines and 3.2B scf/day capacity              | no price             |         |
| T3      |        4B-watch | 2024~2030  | consortium share, margin, schedule, Saudi execution risk unknown                | 4B                   |         |
| T4      |   Stage3-Yellow | N/A        | Hyundai E&C-specific backlog/margin not confirmed                               | no Yellow            |         |

Hyundai E&C의 Aramco/Jafurah trigger는 contract scale은 크지만, Samsung E&A Fadhili처럼 event price가 닫히지 않았다. Reuters에 따르면 Aramco는 Jafurah gas field phase 2와 main gas network phase 3에 $25B+ contracts를 체결했고, Hyundai E&C가 포함된 consortium이 Jafurah expansion에 포함됐다. Jafurah는 2030년 2B scf/day sales gas를 목표로 하고, main gas network는 4,000km pipeline과 3.2B scf/day capacity를 추가한다. 이건 Stage2 mega-backlog이지만, Hyundai E&C 몫·마진·현금흐름이 확인돼야 Yellow다. ([Reuters][2])

```json
{
  "case_id": "r10_loop16_hyundai_ec_jafurah_gas",
  "symbol": "000720",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_mega_gas_EPC",
  "trigger_date": "2024-06-30",
  "aramco_package_value_usd_bn": ">25",
  "jafurah_sales_gas_target_bscfd_2030": 2.0,
  "jafurah_gas_reserves_tcf": 229,
  "jafurah_condensates_billion_barrels": 75,
  "main_gas_network_added_pipeline_km": 4000,
  "main_gas_network_added_capacity_bscfd": 3.2,
  "direct_hyundai_ec_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "Hyundai_EC_contract_share",
    "project_margin",
    "schedule_progress",
    "Saudi_execution_risk",
    "cash_conversion",
    "full_OHLC_MFE_MAE"
  ],
  "trigger_outcome_label": "Stage2_mega_EPC_backlog_not_Green"
}
```

---

## Case C — PF liquidity / Taeyoung / builder support

```text
symbols = 009410 / construction_basket
case_type = PF liquidity 4C + policy relief
archetype = PF_LIQUIDITY_RESTRUCTURING_4C_AND_RELIEF
```

| trigger |               type | date       | 당시 공개 evidence                                                                                    | 가격 anchor       | outcome |
| ------- | -----------------: | ---------- | ------------------------------------------------------------------------------------------------- | --------------- | ------- |
| T0      |           4C-watch | 2023-12    | Taeyoung E&C debt rescheduling raises sector liquidity concern                                    | no direct price |         |
| T1      |      Stage2 relief | 2024-03-27 | Korea announces 40.6T won support for SMEs and builders, guarantees/loans/market stabilizing fund | no stock anchor |         |
| T2      |      4C validation | 2024-05-13 | FSS tightens PF project profitability assessment; PF delinquency 2.70% end-2023 vs 0.37% end-2021 | no price        |         |
| T3      | liquidity backstop | 2024-05-13 | syndicated loan 1T won, expandable to 5T won                                                      | no price        |         |
| T4      |      Stage3-Yellow | N/A        | project write-downs, successful refinancing, pre-sale recovery not confirmed                      | no Yellow       |         |

PF crisis는 R10에서 절대 빼면 안 되는 failed-rerating/4C-watch다. 한국 정부는 고금리와 원가 상승에 흔들리는 builders를 위해 40.6T won 규모의 지원을 발표했고, 보증 확대·추가대출·시장안정펀드로 “수익성 있는 부동산 프로젝트” 자금조달을 돕겠다고 했다. 이후 FSS는 부동산 PF 프로젝트 평가를 강화했고, PF delinquency rate는 2021년 말 0.37%에서 2023년 말 2.70%로 급등했다. 시중은행·보험사는 1T won syndicated loan을 마련했고 필요하면 5T won까지 키울 수 있다고 했다. 즉 지원책은 Stage2 relief지만, **PF 부실 자체는 4C-watch**다. ([Reuters][3])

```json
{
  "case_id": "r10_loop16_pf_taeyoung_builder_restructuring",
  "symbols": "009410/construction_basket",
  "best_trigger": "T1/T3",
  "best_trigger_type": "4C_PF_liquidity_with_Stage2_policy_relief",
  "taeyoung_debt_rescheduling_context": "2023-12",
  "support_announcement_date": "2024-03-27",
  "government_support_krw_trn": 40.6,
  "pf_restructuring_guideline_date": "2024-05-13",
  "pf_delinquency_end_2021_pct": 0.37,
  "pf_delinquency_end_2023_pct": 2.70,
  "syndicated_loan_initial_krw_trn": 1.0,
  "syndicated_loan_possible_max_krw_trn": 5.0,
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "successful_project_refinancing",
    "loss_recognition_completion",
    "pre_sale_recovery",
    "guarantee_exposure_reduction",
    "builder_cashflow_recovery"
  ],
  "trigger_outcome_label": "PF_4C_watch_with_policy_relief"
}
```

---

## Case D — Seoul housing supply / reconstruction easing / LTV tightening

```text
symbols = 000720 / 006360 / 294870 / 028260 / housing_builder_basket
case_type = Stage2 supply policy + 4B demand-control
archetype = HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_WITH_LTV_4B
```

| trigger |          type | date       | 당시 공개 evidence                                                                                          | 가격 anchor        | outcome |
| ------- | ------------: | ---------- | ------------------------------------------------------------------------------------------------------- | ---------------- | ------- |
| T0      |     awareness | 2024-08-16 | Seoul home prices +0.76% MoM, strongest since Dec 2019; reconstruction areas drive demand               | no builder price |         |
| T1      | Stage2 supply | 2024-08    | government targets 400,000+ new homes over six years                                                    | no price         |         |
| T2      |  mixed policy | 2025-09-07 | Seoul LTV in Gangnam/Yongsan cut from 50% to 40%; supply via state land and reconstruction-streamlining | no price         |         |
| T3      |      4B-watch | 2025       | demand curb can hurt pre-sales while supply easing helps backlog                                        | mixed            |         |
| T4      | Stage3-Yellow | N/A        | permits, pre-sales, builder margin not confirmed                                                        | no Yellow        |         |

Housing supply policy는 R10에서 “좋다/나쁘다” 한 줄로 못 본다. Seoul home prices는 2024년 7월 +0.76% MoM로 2019년 12월 이후 가장 강했고, reconstruction 지역이 record-high transactions를 만들었다. 정부는 6년간 400,000+ new homes 공급을 목표로 했다. 2025년 9월에는 Gangnam/Yongsan 등 Seoul 핵심지 LTV를 50%에서 40%로 낮추는 동시에, LH 등 state-run land 활용과 reconstruction 규제 완화로 공급을 늘리겠다고 했다. 즉 builders에는 **supply/reconstruction Stage2**지만, demand-control LTV는 **pre-sale 4B**다. ([Reuters][4])

```json
{
  "case_id": "r10_loop16_seoul_housing_supply_reconstruction",
  "symbols": "000720/006360/294870/028260/housing_builder_basket",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_supply_policy_with_LTV_4B",
  "seoul_price_mom_july_2024_pct": 0.76,
  "seoul_price_context": "strongest_monthly_rise_since_2019-12",
  "new_homes_target_six_years": ">400000",
  "ltv_tightening_date": "2025-09-07",
  "ltv_old_pct": 50,
  "ltv_new_pct": 40,
  "affected_areas": [
    "Gangnam",
    "Yongsan",
    "wealthy_Seoul_districts"
  ],
  "supply_measures": [
    "state_run_land_development",
    "Korea_Land_Housing_Corporation_land",
    "reconstruction_rule_streamlining"
  ],
  "direct_builder_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "permits",
    "actual_reconstruction_start",
    "pre_sale_ratio",
    "PF_refinancing",
    "builder_margin",
    "completion_cashflow"
  ],
  "trigger_outcome_label": "mixed_supply_policy_Stage2_with_demand_4B"
}
```

---

## Case E — Construction safety / Hyundai Engineering bridge collapse

```text
symbols = Hyundai_Engineering_private / construction_basket
case_type = hard 4C safety
archetype = CONSTRUCTION_SAFETY_HARD_4C
```

| trigger |             type | date       | 당시 공개 evidence                                                                                | 가격 anchor                   | outcome |
| ------- | ---------------: | ---------- | --------------------------------------------------------------------------------------------- | --------------------------- | ------- |
| T0      |          hard 4C | 2025-02-25 | highway bridge under construction collapses near Anseong/Cheonan, 4 workers killed, 6 injured | Hyundai Engineering private |         |
| T1      |       validation | 2025-02-25 | Hyundai Engineering was in charge of construction site, cooperating with investigation        | no listed price             |         |
| T2      | hard-gate policy | 2025-09-15 | Korea proposes fines up to 5% of operating profit for companies with >3 worker deaths a year  | no stock price              |         |
| T3      |       license 4C | 2025-09-15 | construction companies repeatedly suspended for fatal accidents could lose licenses           | no price                    |         |
| T4      |           relief | N/A        | investigation closure, compensation, safety remediation not confirmed                         | no relief                   |         |

Construction safety는 R10 hard 4C다. 2025년 2월 Anseong/Cheonan highway bridge collapse로 4명이 사망하고 6명이 다쳤고, WaPo는 Hyundai Engineering이 site를 맡았다고 보도했다. 2025년 9월에는 한국 정부가 1년에 3명 넘는 노동자가 사망한 기업에 operating profit의 최대 5% 벌금을 부과하고, 반복적으로 사망사고로 작업중지를 받는 건설사의 license를 취소할 수 있는 규제안을 추진했다. 건설사는 사고 하나가 단순 비용이 아니라 **license, work suspension, pre-sale brand, bidding score**를 동시에 때린다. ([AP News][5])

```json
{
  "case_id": "r10_loop16_construction_safety_hyundai_engineering_bridge",
  "symbols": "Hyundai_Engineering_private/construction_basket",
  "best_trigger": "T0/T3",
  "best_trigger_type": "hard_4C_construction_safety",
  "incident_date": "2025-02-25",
  "fatalities": 4,
  "injuries": 6,
  "site_company": "Hyundai_Engineering",
  "direct_price_anchor": "price_data_unavailable_private_company",
  "policy_date": "2025-09-15",
  "proposed_fine_pct_of_operating_profit": 5,
  "license_revocation_risk": true,
  "construction_worker_death_share_context": "nearly_half_of_589_job_related_deaths_last_year",
  "stage3_gate_missing": [
    "final_investigation_result",
    "compensation_cost",
    "work_suspension_duration",
    "license_impact",
    "safety_remediation",
    "future_bidding_penalty"
  ],
  "trigger_outcome_label": "hard_4C_success_construction_safety"
}
```

---

## Case F — Samsung C&T / Samsung P5 fab construction

```text
symbol = 028260
case_type = Stage2 AI/fab construction backlog
archetype = AI_FAB_CONSTRUCTION_STAGE2
```

| trigger |            type | date       | 당시 공개 evidence                                                                                          | 가격 anchor                            | outcome |
| ------- | --------------: | ---------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------- |
| T0      |       awareness | 2025-10-02 | Samsung affiliates including Samsung C&T rise on OpenAI/Stargate partnership context                    | Samsung C&T exact return unavailable |         |
| T1      | Stage2 evidence | 2025-11-16 | Samsung to add P5 chip production line at Pyeongtaek; group to invest 450T won in Korea over five years | no Samsung C&T price                 |         |
| T2      |      validation | 2025-11-16 | P5 had been delayed since late 2023; mass production planned 2028; builder filings cite Samsung C&T     | no price                             |         |
| T3      |        4B-watch | 2025~2028  | semiconductor capex cycle, construction margin, schedule, materials, AI demand volatility               | no OHLC                              |         |
| T4      |   Stage3-Yellow | N/A        | Samsung C&T order/margin and P5 construction cashflow not confirmed                                     | no Yellow                            |         |

Samsung C&T는 건설주지만, 전통 주택보다 **AI fab infrastructure**로 봐야 하는 case다. Reuters는 Samsung이 Pyeongtaek P5 line을 추가하고, Samsung group이 5년간 국내에 450T won을 투자할 것이라고 보도했다. P5는 2023년 말부터 delayed 상태였고, 2028년 mass production이 목표다. Reuters는 P5 builder 관련 public filings에서 Samsung C&T를 언급한다. 이건 Stage2 fab-construction backlog지만, Samsung C&T의 개별 수주·마진·공기 리스크가 닫혀야 Yellow다. ([Reuters][6])

```json
{
  "case_id": "r10_loop16_samsung_ct_p5_fab_construction",
  "symbol": "028260",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_AI_fab_construction",
  "trigger_date": "2025-11-16",
  "samsung_group_domestic_investment_krw_trn": 450,
  "investment_period_years": 5,
  "project": "Pyeongtaek_P5_chip_production_line",
  "p5_delay_context": "delayed_since_late_2023",
  "mass_production_target_year": 2028,
  "builder_context": "Samsung_C&T_public_filings",
  "direct_samsung_ct_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "Samsung_CT_order_value",
    "construction_margin",
    "schedule_progress",
    "materials_cost",
    "AI_memory_demand_durability",
    "cash_collection"
  ],
  "trigger_outcome_label": "Stage2_AI_fab_construction_not_Green"
}
```

---

## Case G — Building-material / steel plate anti-dumping

```text
symbols = 004020 / 005490 / construction_input_basket
case_type = mixed Stage2 / 4B
archetype = BUILDING_MATERIAL_INPUT_COST_STAGE2_4B
```

| trigger |                   type | date       | 당시 공개 evidence                                                                                                    | 가격 anchor                                     | outcome |
| ------- | ---------------------: | ---------- | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | ------- |
| T0      | Stage2 supplier relief | 2025-02-20 | Korea recommends provisional 27.91~38.02% anti-dumping duties on Chinese steel plates                             | Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7% |         |
| T1      |  construction input 4B | 2025-02-20 | steel plates used in shipbuilding and construction; imports from China $10.4B in 2024, 49% of total steel imports | mixed                                         |         |
| T2      |               4B-watch | 2025       | supplier margin positive, builder input cost negative unless pass-through                                         | no OHLC                                       |         |
| T3      |          Stage3-Yellow | N/A        | builder pass-through, material cost absorption not confirmed                                                      | no Yellow                                     |         |

건자재는 sector마다 방향이 반대다. 중국산 steel plate anti-dumping은 Hyundai Steel과 POSCO에는 Stage2 supplier relief였다. 발표 기대감에 Hyundai Steel은 +5.8%, POSCO Holdings는 +3.9%였고 KOSPI는 -0.7%였다. 하지만 해당 steel plate는 construction에도 쓰이는 input이다. 따라서 builders 입장에서는 input cost 4B가 될 수 있다. R10에서는 “건자재 상승 = 건설주 상승”으로 보면 안 된다. ([Reuters][7])

```json
{
  "case_id": "r10_loop16_steel_plate_antidumping_construction_input",
  "symbols": "004020/005490/construction_input_basket",
  "best_trigger": "T0/T2",
  "best_trigger_type": "mixed_supplier_Stage2_builder_4B",
  "trigger_date": "2025-02-20",
  "anti_dumping_rate_pct": "27.91-38.02",
  "china_steel_import_value_2024_usd_bn": 10.4,
  "china_share_of_korea_steel_imports_pct": 49,
  "hyundai_steel_event_return_pct": 5.8,
  "posco_event_return_pct": 3.9,
  "kospi_same_context_pct": -0.7,
  "construction_use_case": true,
  "stage3_gate_missing": [
    "builder_cost_pass_through",
    "public_project_escalation_clause",
    "materials_cost_absorption",
    "steel_supplier_margin",
    "construction_contract_margin"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "mixed_building_material_supplier_relief_builder_cost_4B"
}
```

---

## Case H — Rate-cut support vs housing overheating / construction downturn

```text
symbols = construction_basket / REITs / banks_readthrough
case_type = mixed macro Stage2/4B
archetype = RATE_CUT_HOUSING_POLICY_MIXED_STAGE2_4B
```

| trigger |                             type | date       | 당시 공개 evidence                                                                                 | 가격 anchor                      | outcome |
| ------- | -------------------------------: | ---------- | ---------------------------------------------------------------------------------------------- | ------------------------------ | ------- |
| T0      |                     macro relief | 2025-10-23 | BOK holds 2.50% but signals possible further cut to 2.25% or lower                             | KOSPI record, no builder price |         |
| T1      |                         4B watch | 2025-10-23 | won weakens to six-month low; home-price overheating limits easing                             | no price                       |         |
| T2      | construction downturn validation | 2025-10-23 | construction industry in downturn due labor/equipment costs and shortage of new housing supply | no price                       |         |
| T3      |                    Stage3-Yellow | N/A        | rate cuts translating to PF refinancing and pre-sales not confirmed                            | no Yellow                      |         |

금리인하 기대는 builders에 Stage2 relief가 될 수 있지만, R10에서는 항상 housing overheating과 같이 봐야 한다. BOK는 2025년 10월 기준금리를 2.50%로 유지했지만, 위원 6명 중 4명이 3개월 안에 2.25% 이하로 낮출 여지를 열어두었다. 동시에 won은 약세였고, 주택시장 과열이 금리인하를 제약했다. Reuters는 건설업이 인건비·장비비 상승과 신규주택 공급 부족으로 둔화 중이라고 설명했다. 따라서 rate-cut 기대는 Stage2 relief지만, 금융안정·부동산 과열·원화 약세는 4B다. ([Reuters][8])

```json
{
  "case_id": "r10_loop16_bok_rate_cut_housing_construction_mixed",
  "symbols": "construction_basket/REITs/banks_readthrough",
  "best_trigger": "T0/T2",
  "best_trigger_type": "mixed_rate_cut_relief_with_housing_4B",
  "trigger_date": "2025-10-23",
  "policy_rate_pct": 2.50,
  "possible_forward_rate_pct": "<=2.25",
  "board_members_open_to_cut": 4,
  "board_members_total_context": 6,
  "kospi_context": "fresh_record_high",
  "won_context": "about_six_month_low",
  "construction_downturn_drivers": [
    "labor_cost",
    "equipment_cost",
    "housing_supply_shortage",
    "financial_stability_risk"
  ],
  "direct_builder_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "PF_refinancing",
    "mortgage_demand_recovery",
    "pre_sale_recovery",
    "builder_margin_recovery",
    "rate_cut_execution"
  ],
  "trigger_outcome_label": "macro_relief_Stage2_with_housing_4B"
}
```

---

# 6. Trigger별 가격경로 검증 요약

| case                     | best trigger |     entry anchor |                    event MFE/MAE |       market-relative | full MFE/MAE | outcome                      |
| ------------------------ | ------------ | ---------------: | -------------------------------: | --------------------: | ------------ | ---------------------------- |
| Samsung E&A Fadhili      | T1/T2        |       26,750 won |                            +8.5% | +9.9pp vs KOSPI -1.4% | unavailable  | excellent Stage2-Actionable  |
| Hyundai E&C Jafurah      | T0/T2        |         no price |                  no direct price |                   N/A | unavailable  | Stage2 mega-backlog          |
| PF/Taeyoung/builders     | T1/T3        |         no price |                  no direct price |                   N/A | unavailable  | 4C-watch + relief            |
| Seoul housing supply     | T0/T2        |         no price |                  no direct price |                   N/A | unavailable  | mixed Stage2 + 4B            |
| Construction safety      | T0/T3        | private/no price |    fatality/license/fine trigger |                   N/A | unavailable  | hard 4C                      |
| Samsung C&T P5           | T1/T2        |         no price |                  no direct price |                   N/A | unavailable  | Stage2 AI/fab construction   |
| Steel plate anti-dumping | T0/T2        |            event | Hyundai Steel +5.8%, POSCO +3.9% |           KOSPI -0.7% | unavailable  | supplier Stage2 / builder 4B |
| BOK/housing macro        | T0/T2        |            macro |             KOSPI record context |      no builder price | unavailable  | macro Stage2 + 4B            |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
좋은 Stage2:
- Samsung E&A / Fadhili: contract value and price reaction both closed.
- Hyundai E&C / Jafurah: contract scale huge, but price anchor missing.
- Samsung C&T / P5: AI fab construction trigger, but order/margin missing.
- Housing supply/reconstruction: policy support exists, but LTV demand curb offsets.
```

## Stage2-Actionable entry 성과

```text
Actionable:
- Samsung E&A Fadhili: +8.5%, KOSPI -1.4%, $6B contract context.
- Steel plate anti-dumping from supplier side: Hyundai Steel +5.8%, POSCO +3.9%.

Actionable 보류:
- Hyundai E&C Jafurah: price anchor unavailable.
- Samsung C&T P5: price anchor and contract economics unavailable.
- Housing supply: policy is mixed, not clean.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Samsung E&A if Fadhili margin, execution progress and cash collection confirm.
- Hyundai E&C if Jafurah contract share and margin are disclosed.
- Samsung C&T if P5 order value and construction margin become visible.
- Housing builders if reconstruction permits, pre-sale ratios and PF refinancing improve.
```

## Stage3-Green

```text
이번 R10 Loop 16에서 확정 Green 없음.

이유:
- EPC 수주는 강하지만 margin/cash conversion이 없다.
- 주택공급 정책은 demand-control과 PF risk가 섞여 있다.
- PF 구조조정은 아직 relief이지 completion recovery가 아니다.
- 건설 안전은 hard 4C가 분명하다.
- 건자재 anti-dumping은 supplier와 builder 방향이 반대다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Samsung E&A Fadhili
- Steel plate anti-dumping supplier reaction
- Construction safety as hard 4C
- PF support as relief but not Green

Stage2_promote_candidate:
- Samsung E&A Fadhili
- Hyundai E&C Jafurah if price/margin confirms
- Samsung C&T P5 if order/margin confirms
- Housing supply/reconstruction if permits/pre-sales confirm

Stage3-Yellow candidate:
- Samsung E&A
- Hyundai E&C
- Samsung C&T
- select housing builders after PF/pre-sale recovery

evidence_good_but_price_failed_or_unavailable:
- Hyundai E&C Jafurah
- Samsung C&T P5
- Housing supply/reconstruction
- PF relief

failed_rerating:
- PF/Taeyoung builder liquidity stress
- construction downturn from labor/equipment cost and housing supply imbalance

event_premium:
- overseas EPC contract rally
- reconstruction/housing supply policy
- AI fab construction narrative

thesis_break_watch:
- PF delinquency
- construction safety fatal accidents
- LTV tightening / demand curb
- material input cost pass-through failure

hard_4C_success:
- construction safety / fatal bridge collapse industry gate
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
EPC_contract_value_visibility,+5,"수주금액과 주가반응이 동시에 닫히면 Stage2-Actionable","Samsung E&A"
EPC_margin_cash_conversion,+5,"EPC는 매출보다 margin/cash conversion이 Green gate","Samsung E&A, Hyundai E&C"
project_execution_progress,+4,"대형 해외공사는 공정률·claim·원가통제가 필요","Samsung E&A, Hyundai E&C"
PF_refinancing_success,+5,"PF crisis 이후 refinancing과 손실인식 완료가 핵심","Taeyoung/builders"
pre_sale_recovery,+5,"주택 공급정책은 pre-sale ratio가 닫혀야 Yellow","housing builders"
reconstruction_permit_conversion,+4,"재건축 완화는 실제 permits/착공 전에는 Stage2","housing basket"
construction_safety_license_risk,+5,"사망사고는 license/fine/work suspension hard gate","Hyundai Engineering/readthrough"
AI_fab_construction_backlog,+4,"AI fab capex는 builder backlog로 확인되면 승격","Samsung C&T"
material_cost_pass_through,+4,"건자재 상승은 pass-through가 없으면 builder margin 훼손","steel/construction basket"
```

## 내릴 축

```csv
axis,delta,reason,cases
contract_headline_without_margin,-5,"대형 수주만으로 Green 금지","Samsung E&A, Hyundai E&C"
housing_policy_without_presales,-5,"공급정책 headline은 분양률 전에는 Stage2","housing builders"
PF_support_without_writeoff,-5,"지원책은 부실 정리 전에는 Green이 아니다","Taeyoung/PF basket"
reconstruction_theme_without_start,-4,"재건축 기대만으로 Actionable 금지","housing basket"
AI_fab_headline_without_order_value,-4,"fab 시공 narrative는 order value/margin 필요","Samsung C&T"
material_supplier_rally_ignoring_builder_cost,-4,"건자재 supplier rally를 builder positive로 오독 금지","steel/construction basket"
safety_incident_treated_as_one_off,-5,"사망사고를 일회성 비용으로 보면 false positive","construction safety"
```

---

# 10. Stage2-Actionable 승격 조건

R10 Loop 16 shadow rule:

```text
R10에서 Stage2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. contract value가 명확하다.
2. event return이 +5% 이상이다.
3. market-relative return이 +5pp 이상이다.
4. project margin 또는 cash conversion visibility가 있다.
5. housing policy가 permits / pre-sales / PF refinancing으로 연결된다.
6. construction safety / license / fatal accident 4C overlay가 없다.
7. input material cost pass-through가 확인된다.
```

적용:

```text
Samsung E&A:
1,2,3 충족 → Stage2-Actionable.
4가 아직 없어서 Yellow 후보에 머문다.

Hyundai E&C:
1은 충족하지만 2,3,4 없음 → Stage2.

Housing policy:
5가 아직 없음, LTV 4B 있음 → Stage2 relief only.

PF support:
relief는 있지만 write-off/refinancing 확인 전 → 4C-watch + Stage2 relief.

Construction safety:
6 위반 → hard 4C.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
- Stage2-Actionable 이후 EPS/OP/FCF 경로 변화 가능성이 높아짐.
- 하지만 margin, cash collection, permits, PF refinancing, safety remediation 중 하나가 남은 상태.
```

Yellow 후보:

```text
Samsung E&A:
Fadhili margin and cash conversion 확인 시 Yellow.

Hyundai E&C:
Jafurah/Main Gas Network share, margin, execution schedule 확인 시 Yellow.

Samsung C&T:
P5 order value and fab construction margin 확인 시 Yellow.

Housing builders:
permits, pre-sale ratio, PF refinancing and cost pass-through 확인 시 Yellow.

PF recovery names:
project write-down completion and liquidity normalization 확인 시 Yellow.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- EPC backlog converts to profitable revenue and cash flow.
- project execution progresses without cost overrun or claim.
- housing policy converts to permits, pre-sales and PF refinancing.
- reconstruction projects actually start construction.
- construction safety risk is remediated.
- input cost pass-through is contractually protected.
- full-window MFE/MAE is favorable.
```

이번 R10 Loop 16에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + margin/PF/pre-sale/safety gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- overseas EPC contract rallies before margin/cash conversion.
- housing supply policy rallies before pre-sales and permits.
- PF support appears before loss recognition and refinancing.
- AI fab construction story appears before order value/margin.
- building-material supplier rally increases builder input costs.
- fatal construction accident triggers fine/license/work-suspension risk.
```

적용:

```text
Samsung E&A:
excellent Stage2, but execution/margin 4B remains.

Hyundai E&C:
mega contract Stage2, but no price/margin anchor.

Housing supply:
state land/reconstruction easing positive, LTV tightening negative.

PF support:
policy relief positive, delinquency and restructuring 4C remain.

Construction safety:
fatal accident hard 4C.

Steel plate anti-dumping:
supplier Stage2, builder input-cost 4B.
```

---

# 14. 4C hard gate 조건

```text
R10 4C:
- debt workout / PF default
- PF delinquency spike and failed refinancing
- fatal construction accident
- work suspension / license revocation risk
- major defect / collapse / safety investigation
- input-cost spike without pass-through
- housing demand collapse or pre-sale failure
```

이번 R10 Loop 16 hard 4C:

```text
construction safety fatal accident = hard_4C_success
PF delinquency / Taeyoung = 4C-watch, not hard_4C closed for all builders
```

Strong 4C-watch:

```text
- PF delinquency and project restructuring
- LTV tightening hurting demand
- construction input-cost pass-through failure
- safety regulation and license revocation risk
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R10 production 설계 원칙:

```text
1. overseas EPC contract value와 margin/cash conversion을 분리한다.
2. housing supply policy와 actual pre-sales를 분리한다.
3. PF liquidity support와 actual restructuring completion을 분리한다.
4. AI fab construction narrative와 builder order value/margin을 분리한다.
5. building-material supplier benefit과 builder input-cost risk를 분리한다.
6. fatal safety accident는 hard 4C로 즉시 차감한다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_246.md 요약

```md
# R10 Loop 16. Construction / Real Estate / Building Materials Trigger-level Price Validation

이번 라운드는 R10 Loop 16 trigger-level validation 라운드다.

핵심 결론:
- Samsung E&A / Fadhili is the cleanest Stage2-Actionable EPC case. Aramco awarded $7.7B Fadhili gas expansion contracts, Samsung E&A signed around $6B share, and Samsung E&A shares rose as much as 8.5% to 26,750 won while KOSPI fell 1.4%. Green requires project margin, cash conversion and execution progress.
- Hyundai E&C / Jafurah is Stage2 mega-EPC backlog. Aramco signed more than $25B contracts for Jafurah and main gas network expansion, and Hyundai E&C consortium was included. Direct price anchor and margin economics are unavailable.
- PF / Taeyoung / builders is 4C-watch with policy relief. Korea prepared 40.6T won support for SMEs and builders, while FSS tightened PF project assessment; PF delinquency rose to 2.70% at end-2023 from 0.37% at end-2021. Syndicated loan starts at 1T won and can expand to 5T won.
- Seoul housing supply / reconstruction is mixed Stage2 + 4B. Seoul prices rose 0.76% MoM in July 2024, strongest since Dec 2019, and the government targets 400,000+ new homes. But LTV in Gangnam/Yongsan was tightened from 50% to 40%.
- Construction safety is hard 4C. The Anseong/Cheonan highway bridge collapse killed four workers; Hyundai Engineering was in charge of the site. Korea later proposed fines up to 5% of operating profit for repeated fatal accidents and license revocation for repeated construction safety failures.
- Samsung C&T / P5 fab construction is Stage2. Samsung will add the P5 line at Pyeongtaek as part of 450T won domestic investment over five years; P5 mass production is planned for 2028. Samsung C&T order value and margin are unavailable.
- Steel plate anti-dumping is mixed. Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7% after Korea recommended 27.91~38.02% duties on Chinese steel plates. Supplier positive, builder input-cost 4B.
- BOK rate-cut guidance is macro relief but housing 4B. Rate cuts can help PF refinancing, but overheating Seoul property, won weakness and construction downturn remain constraints.

Main calibration:
- Raise EPC_contract_value_visibility, EPC_margin_cash_conversion, project_execution_progress, PF_refinancing_success, pre_sale_recovery, reconstruction_permit_conversion, construction_safety_license_risk, AI_fab_construction_backlog, material_cost_pass_through.
- Lower contract_headline_without_margin, housing_policy_without_presales, PF_support_without_writeoff, reconstruction_theme_without_start, AI_fab_headline_without_order_value, material_supplier_rally_ignoring_builder_cost, safety_incident_treated_as_one_off.
```

## docs/checkpoints/checkpoint_28a_round246_r10_loop16.md 요약

```md
# Checkpoint 28A Round 246 R10 Loop 16 Trigger-level Calibration

## 반영 내용
- R10 Loop 16 trigger-level validation을 수행했다.
- Samsung E&A Fadhili, Hyundai E&C Jafurah, PF/Taeyoung builder liquidity, Seoul housing supply/reconstruction, construction safety, Samsung C&T P5 fab construction, steel plate anti-dumping, BOK rate-cut/housing macro를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / WSJ / AP / WaPo의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- EPC 수주는 contract value보다 margin and cash conversion이 Green gate다.
- PF support is relief, not Green, until refinancing and write-offs are complete.
- Housing supply policy needs permits, pre-sales and PF financing.
- Construction safety fatal accident is hard 4C because it affects license, work suspension and bidding.
- AI fab construction is Stage2 until order value and margin are visible.
- Building-material supplier benefit and builder input-cost risk must be separated.
```

## data/e2r_case_library/cases_r10_loop16_round246.jsonl 초안

```jsonl
{"case_id":"r10_loop16_samsung_ea_fadhili","symbol":"028050","company_name":"Samsung E&A","case_type":"Stage2_Actionable_EPC_backlog","primary_archetype":"MIDDLE_EAST_EPC_BACKLOG_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2024-04-03","aramco_total_contract_value_usd_bn":7.7,"samsung_contract_value_context_usd_bn":6.0,"event_return_pct":8.5,"event_price_krw":26750,"kospi_same_context_pct":-1.4,"market_relative_return_pp":9.9,"completion_target":"2027-11","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_EPC_contract","notes":"Large EPC contract with strong relative price reaction; Green requires margin, cash conversion and execution progress."}
{"case_id":"r10_loop16_hyundai_ec_jafurah_gas","symbol":"000720","company_name":"Hyundai E&C","case_type":"Stage2_mega_gas_EPC","primary_archetype":"MEGA_GAS_PIPELINE_EPC_STAGE2_WITH_MARGIN_GATE","best_trigger":"T0/T2","stage_candidate":"Stage2","price_validation":{"trigger_date":"2024-06-30","aramco_package_value_usd_bn":">25","jafurah_sales_gas_target_bscfd_2030":2.0,"jafurah_gas_reserves_tcf":229,"main_gas_network_added_pipeline_km":4000,"main_gas_network_added_capacity_bscfd":3.2,"direct_hyundai_ec_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"Mega EPC backlog exists, but Hyundai E&C-specific share, price, margin and cash conversion are missing."}
{"case_id":"r10_loop16_pf_taeyoung_builder_restructuring","symbol":"009410/construction_basket","company_name":"Taeyoung E&C / Korean builders","case_type":"PF_4C_watch_with_policy_relief","primary_archetype":"PF_LIQUIDITY_RESTRUCTURING_4C_AND_RELIEF","best_trigger":"T1/T3","stage_candidate":"4C-watch + Stage2 relief","price_validation":{"support_announcement_date":"2024-03-27","government_support_krw_trn":40.6,"pf_restructuring_guideline_date":"2024-05-13","pf_delinquency_end_2021_pct":0.37,"pf_delinquency_end_2023_pct":2.70,"syndicated_loan_initial_krw_trn":1.0,"syndicated_loan_possible_max_krw_trn":5.0,"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"PF_4C_watch_with_relief","notes":"Policy support exists but PF write-offs, refinancing and pre-sale recovery are not confirmed."}
{"case_id":"r10_loop16_seoul_housing_supply_reconstruction","symbol":"000720/006360/294870/028260/housing_builder_basket","company_name":"Korean housing builders","case_type":"mixed_supply_policy_Stage2_with_demand_4B","primary_archetype":"HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_WITH_LTV_4B","best_trigger":"T0/T2","stage_candidate":"Stage2 + 4B-watch","price_validation":{"seoul_price_mom_july_2024_pct":0.76,"seoul_price_context":"strongest_monthly_rise_since_2019-12","new_homes_target_six_years":">400000","ltv_tightening_date":"2025-09-07","ltv_old_pct":50,"ltv_new_pct":40,"direct_builder_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"mixed_policy_stage2_4B","notes":"Supply/reconstruction easing helps backlog, but LTV tightening can hurt pre-sales."}
{"case_id":"r10_loop16_construction_safety_hyundai_engineering_bridge","symbol":"Hyundai_Engineering_private/construction_basket","company_name":"Hyundai Engineering / construction safety read-through","case_type":"hard_4C_construction_safety","primary_archetype":"CONSTRUCTION_SAFETY_HARD_4C","best_trigger":"T0/T3","stage_candidate":"4C","price_validation":{"incident_date":"2025-02-25","fatalities":4,"injuries":6,"site_company":"Hyundai_Engineering","direct_price_anchor":"price_data_unavailable_private_company","policy_date":"2025-09-15","proposed_fine_pct_of_operating_profit":5,"license_revocation_risk":true},"score_price_alignment":"hard_4C_success","notes":"Fatal construction accident and new fine/license framework are hard safety gates."}
{"case_id":"r10_loop16_samsung_ct_p5_fab_construction","symbol":"028260","company_name":"Samsung C&T","case_type":"Stage2_AI_fab_construction","primary_archetype":"AI_FAB_CONSTRUCTION_STAGE2","best_trigger":"T1/T2","stage_candidate":"Stage2","price_validation":{"trigger_date":"2025-11-16","samsung_group_domestic_investment_krw_trn":450,"investment_period_years":5,"project":"Pyeongtaek_P5_chip_production_line","p5_delay_context":"delayed_since_late_2023","mass_production_target_year":2028,"builder_context":"Samsung_C&T_public_filings","direct_samsung_ct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"AI fab construction backlog is plausible, but order value and margin are unavailable."}
{"case_id":"r10_loop16_steel_plate_antidumping_construction_input","symbol":"004020/005490/construction_input_basket","company_name":"Hyundai Steel / POSCO / construction input basket","case_type":"mixed_supplier_Stage2_builder_4B","primary_archetype":"BUILDING_MATERIAL_INPUT_COST_STAGE2_4B","best_trigger":"T0/T2","stage_candidate":"mixed Stage2/4B","price_validation":{"trigger_date":"2025-02-20","anti_dumping_rate_pct":"27.91-38.02","china_steel_import_value_2024_usd_bn":10.4,"china_share_of_korea_steel_imports_pct":49,"hyundai_steel_event_return_pct":5.8,"posco_event_return_pct":3.9,"kospi_same_context_pct":-0.7,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"mixed_supplier_relief_builder_cost_4B","notes":"Steel suppliers benefit, but builders face material-cost pass-through risk."}
{"case_id":"r10_loop16_bok_rate_cut_housing_construction_mixed","symbol":"construction_basket/REITs/banks_readthrough","company_name":"Construction macro / housing rate-cut basket","case_type":"mixed_rate_cut_relief_with_housing_4B","primary_archetype":"RATE_CUT_HOUSING_POLICY_MIXED_STAGE2_4B","best_trigger":"T0/T2","stage_candidate":"Stage2 macro relief + 4B","price_validation":{"trigger_date":"2025-10-23","policy_rate_pct":2.50,"possible_forward_rate_pct":"<=2.25","board_members_open_to_cut":4,"board_members_total_context":6,"kospi_context":"fresh_record_high","won_context":"about_six_month_low","direct_builder_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"macro_relief_stage2_with_housing_4B","notes":"Rate-cut expectations can help PF refinancing, but housing overheating and FX pressure constrain relief."}
```

## data/e2r_trigger_calibration/triggers_r10_loop16_round246.jsonl 초안

```jsonl
{"trigger_id":"r10l16_samsung_ea_fadhili_T1","case_id":"r10_loop16_samsung_ea_fadhili","trigger_type":"Stage2-Actionable_EPC","trigger_date":"2024-04-03","evidence_available":"Samsung E&A signed around $6B Fadhili contract share; shares +8.5% to 26,750 won while KOSPI -1.4%; Aramco total project $7.7B","event_return_pct":8.5,"entry_price_krw":26750,"trigger_outcome_label":"excellent_stage2_actionable_EPC_contract","promote_to":"Stage2-Actionable"}
{"trigger_id":"r10l16_hyundai_ec_jafurah_T0","case_id":"r10_loop16_hyundai_ec_jafurah_gas","trigger_type":"Stage2_mega_EPC","trigger_date":"2024-06-30","evidence_available":"Aramco signed more than $25B contracts for Jafurah and main gas network; Hyundai E&C consortium included; Jafurah target 2B scf/day sales gas by 2030","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_mega_EPC_not_Green","promote_to":"Stage2"}
{"trigger_id":"r10l16_pf_support_T1","case_id":"r10_loop16_pf_taeyoung_builder_restructuring","trigger_type":"Stage2_relief_plus_4C_PF","trigger_date":"2024-03-27/2024-05-13","evidence_available":"Korea prepared 40.6T won support for SMEs/builders; PF delinquency rose to 2.70% end-2023 from 0.37% end-2021; 1T won syndicated loan expandable to 5T won","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"PF_4C_watch_with_policy_relief","promote_to":"Stage2_relief+4C-watch"}
{"trigger_id":"r10l16_housing_supply_T2","case_id":"r10_loop16_seoul_housing_supply_reconstruction","trigger_type":"mixed_Stage2_supply_4B_demand","trigger_date":"2024-08-16/2025-09-07","evidence_available":"Seoul prices +0.76% MoM, government targets >400,000 homes, later tightens LTV from 50% to 40% while streamlining reconstruction and using state land","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"mixed_supply_policy_stage2_with_LTV_4B","promote_to":"Stage2+4B"}
{"trigger_id":"r10l16_construction_safety_T0","case_id":"r10_loop16_construction_safety_hyundai_engineering_bridge","trigger_type":"hard_4C_safety","trigger_date":"2025-02-25/2025-09-15","evidence_available":"Highway bridge collapse killed 4 workers and injured 6; Hyundai Engineering was in charge; later Korea proposed up to 5% operating-profit fine and license revocation risk for repeated fatal accidents","event_return_pct":"private_company_no_public_price","trigger_outcome_label":"hard_4C_success_construction_safety","promote_to":"4C"}
{"trigger_id":"r10l16_samsung_ct_p5_T1","case_id":"r10_loop16_samsung_ct_p5_fab_construction","trigger_type":"Stage2_AI_fab_construction","trigger_date":"2025-11-16","evidence_available":"Samsung to add P5 line at Pyeongtaek as part of 450T won domestic investment over five years; P5 mass production planned 2028; builder filings cite Samsung C&T","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_AI_fab_construction_not_Green","promote_to":"Stage2"}
{"trigger_id":"r10l16_steel_plate_input_T0","case_id":"r10_loop16_steel_plate_antidumping_construction_input","trigger_type":"mixed_supplier_Stage2_builder_4B","trigger_date":"2025-02-20","evidence_available":"Korea recommended 27.91-38.02% anti-dumping duties on Chinese steel plates; Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7%; plates used in construction","event_return_pct":"Hyundai Steel +5.8 / POSCO +3.9","trigger_outcome_label":"supplier_relief_builder_input_cost_4B","promote_to":"mixed_Stage2_4B"}
{"trigger_id":"r10l16_bok_rate_housing_T0","case_id":"r10_loop16_bok_rate_cut_housing_construction_mixed","trigger_type":"mixed_macro_Stage2_4B","trigger_date":"2025-10-23","evidence_available":"BOK held 2.50% but four of six board members open to <=2.25%; KOSPI record high, won six-month low, construction downturn due labor/equipment costs and housing supply shortage","event_return_pct":"builder_price_unavailable","trigger_outcome_label":"rate_cut_relief_with_housing_4B","promote_to":"Stage2+4B"}
```

## data/sector_taxonomy/score_weight_profiles_round246_r10_loop16_v1.csv 초안

```csv
archetype,epc_contract_value_visibility,epc_margin_cash_conversion,project_execution_progress,pf_refinancing_success,pre_sale_recovery,reconstruction_permit_conversion,construction_safety_license_risk,ai_fab_construction_backlog,material_cost_pass_through,contract_headline_without_margin_penalty,housing_policy_without_presales_penalty,pf_support_without_writeoff_penalty,reconstruction_theme_without_start_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
MIDDLE_EAST_EPC_BACKLOG_STAGE2_ACTIONABLE,+5,+5,+4,+0,+0,+0,+1,+0,+1,-5,-1,-1,-1,large EPC value and price reaction,margin/cash conversion missing,margin+execution+cash,Samsung E&A Fadhili.
MEGA_GAS_PIPELINE_EPC_STAGE2_WITH_MARGIN_GATE,+5,+5,+5,+0,+0,+0,+1,+0,+1,-5,-1,-1,-1,mega Aramco package,Hyundai E&C share/margin missing,contract share+margin+progress,Hyundai E&C Jafurah.
PF_LIQUIDITY_RESTRUCTURING_4C_AND_RELIEF,+0,+1,+1,+5,+4,+0,+3,+0,+1,-1,-2,-5,-1,PF support and delinquency,write-off/refinancing missing,refinancing+loss recognition+pre-sale,Taeyoung/builders.
HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_WITH_LTV_4B,+0,+1,+2,+4,+5,+5,+2,+0,+2,-1,-5,-2,-4,supply/reconstruction policy,LTV and pre-sale gate,permits+pre-sales+PF,housing builders.
CONSTRUCTION_SAFETY_HARD_4C,+0,+0,+1,+0,+1,+0,+5,+0,+0,-1,-1,-1,-1,fatal accident/license risk,remediation missing,N/A,Hyundai Engineering bridge collapse.
AI_FAB_CONSTRUCTION_STAGE2,+2,+4,+4,+0,+0,+0,+1,+5,+2,-4,-1,-1,-1,P5 fab construction narrative,order value/margin missing,order value+margin+schedule,Samsung C&T.
BUILDING_MATERIAL_INPUT_COST_STAGE2_4B,+1,+2,+1,+0,+1,+0,+1,+0,+5,-2,-1,-1,-1,anti-dumping supplier relief,builder pass-through missing,pass-through+contract margin,steel plate input.
RATE_CUT_HOUSING_POLICY_MIXED_STAGE2_4B,+0,+1,+1,+5,+4,+2,+1,+0,+1,-1,-4,-3,-1,rate-cut relief but housing overheating,PF/pre-sale conversion missing,refi+pre-sale+margin,BOK/housing macro.
```

---

# 이번 R10 Loop 16 결론

```text
1. Samsung E&A / Fadhili는 R10의 가장 좋은 Stage2-Actionable이다.
   $6B contract, +8.5%, KOSPI -1.4%가 닫혔다. 다만 margin/cash conversion 전에는 Green이 아니다.

2. Hyundai E&C / Jafurah는 Stage2 mega-backlog다.
   Aramco $25B+ package에 포함됐지만, Hyundai E&C 몫·주가·마진이 없다.

3. PF / Taeyoung / builders는 4C-watch + policy relief다.
   40.6T won support는 relief지만, PF delinquency 2.70%와 restructuring은 hard gate다.

4. Seoul housing supply/reconstruction은 mixed Stage2 + 4B다.
   공급확대와 재건축 완화는 좋지만, LTV 40% tightening은 demand/pre-sale 4B다.

5. Construction safety는 hard 4C다.
   fatal bridge collapse와 operating-profit fine/license revocation risk는 일회성 비용으로 보면 안 된다.

6. Samsung C&T / P5 fab construction은 Stage2다.
   AI fab capex는 좋지만 Samsung C&T order value/margin이 필요하다.

7. Steel plate anti-dumping은 supplier Stage2, builder 4B다.
   Hyundai Steel/POSCO에는 positive지만, 건설사에는 input-cost pass-through gate다.

8. BOK rate-cut guidance는 macro relief지만 housing 4B다.
   금리인하 기대는 PF refinancing에 좋지만, 서울 과열·원화 약세·건설경기 둔화가 같이 있다.
```

한 문장으로 압축하면:

> **R10 Loop 16에서 배운 핵심은 “수주·주택공급·PF지원·AI fab·건자재 headline”이 아니라, EPC margin/cash conversion, PF refinancing, pre-sale recovery, reconstruction permits, construction safety license risk, fab order value, input-cost pass-through가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 대형 수주, 공급정책, 지원책, 재건축 기대, fab narrative만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.reuters.com/markets/commodities/aramco-awards-77-bln-contracts-fadhili-gas-expansion-2024-04-02/?utm_source=chatgpt.com "Aramco awards $7.7 bln in contracts for Fadhili gas expansion"
[2]: https://www.reuters.com/business/energy/aramco-signs-over-25-bln-deals-main-gas-network-jafurah-gas-field-2024-06-30/?utm_source=chatgpt.com "Aramco signs over $25 bln of deals for main gas network and Jafurah gas field"
[3]: https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/?utm_source=chatgpt.com "South Korea prepares financial support for small businesses, builders"
[4]: https://www.reuters.com/markets/asia/home-prices-seoul-rise-fastest-pace-more-than-4-years-2024-08-16/?utm_source=chatgpt.com "Home prices in Seoul rise at fastest pace in more than 4 years"
[5]: https://apnews.com/article/72744767d151b6ee66eca37397810e0e?utm_source=chatgpt.com "An elevated part of a highway being built in South Korea collapses, killing 4 workers"
[6]: https://www.reuters.com/world/asia-pacific/samsung-electronics-add-chip-production-line-demand-rises-2025-11-16/?utm_source=chatgpt.com "Samsung, Hyundai announce domestic investments after US-South Korea trade deal"
[7]: https://www.reuters.com/markets/asia/south-korea-provisionally-slaps-tariffs-chinese-steel-plates-dumping-2025-02-20/?utm_source=chatgpt.com "South Korea provisionally slaps tariffs on Chinese steel plates for dumping"
[8]: https://www.reuters.com/world/asia-pacific/south-korea-holds-key-rate-hot-housing-market-narrows-scope-easing-2025-10-23/?utm_source=chatgpt.com "South Korea keeps rates on hold but surprises with nod to further cuts"
