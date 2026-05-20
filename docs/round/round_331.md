순서상 이번은 **R10 Loop 17 — 건설·부동산·건자재 trigger-level price validation 라운드**다.

```text
round = R10 Loop 17
round_id = round_259
large_sector = CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R11 Loop 17
```

이번에도 KRX/Naver/Yahoo/Stooq 기준 수정주가 일봉 OHLC window를 안정적으로 확보하지 못했다. 그래서 MFE/MAE/peak/drawdown은 만들지 않고 `price_data_unavailable_after_deep_search`로 둔다. 대신 **reported event return, close/intraday price, contract value, policy amount, delinquency rate, syndicate-loan size, safety-failure facts**를 trigger anchor로 사용한다.

---

# 1. 이번 라운드 대섹터

```text
R10 = 건설·부동산·건자재
```

R10의 core gate는 아래다.

```text
해외 EPC / 플랜트:
계약금액 → 발주처 신뢰도 → 공정기간 → 원가/환율/인력 → margin → change order / delay 4B

원전·인프라 EPC:
preferred bidder → final contract → legal appeal / EU subsidy review → 기자재·시공 참여 범위 → margin / schedule

주택·재건축:
주택공급 정책 → 인허가·재건축 규제완화 → 분양물량 → 미분양·PF → 원가·분양가 → cash conversion

부동산 PF:
연체율 → 차환/보증/유동성 지원 → 부실 프로젝트 정리 → 시행사·시공사 손실 → 4B/4C

건자재:
시멘트/레미콘/철근 demand → 주택 착공 → 가격 전가 → 에너지/물류비 → margin

건설 안전:
붕괴·사망사고 → 공사중지·벌점·입찰제한 → 브랜드/수주 타격 → hard 4C 가능

건설 holding/value-up:
건설·상사·바이오·지분가치 → 자사주/배당 → 주주제안 → governance discount
```

---

# 2. 대상 canonical archetype

```text
OVERSEAS_EPC_MEGA_CONTRACT_STAGE2_ACTIONABLE
NUCLEAR_INFRA_EPC_STAGE2_WITH_LEGAL_4B
HOUSING_SUPPLY_RECONSTRUCTION_POLICY_STAGE2_NO_PRICE
REAL_ESTATE_PF_RESTRUCTURING_4B
CONSTRUCTION_HOLDCO_VALUEUP_FAILED_RERATING
CONSTRUCTION_SITE_SAFETY_HARD_4C_NO_PUBLIC_PRICE
BUILDER_LIQUIDITY_SUPPORT_STAGE2_RELIEF
```

---

# 3. deep sub-archetype

```text
Samsung E&A / Saudi Fadhili:
- Saudi Aramco Fadhili gas plant expansion contract around $6B.
- Samsung E&A shares +8.5% to 26,750 won while KOSPI -1.4%.
- project raises gas processing capacity by 60% to 4 bcf/day, completion due Nov 2027.
- Stage2-Actionable overseas EPC.

Czech nuclear / KHNP / Doosan / KEPCO E&C:
- KHNP selected preferred bidder for two Czech reactors, first major Korean overseas nuclear order since 2009.
- Czech estimated new unit cost at 200B crowns / $8.65B when building two at same site.
- Doosan Enerbility +48% in three months, KEPCO Plant S&E +14%, KEPCO E&C +41%.
- Later legal/competition appeals and court/anti-monopoly delays create 4B.

Seoul housing supply / reconstruction:
- Seoul home prices rose 0.76% in July 2024, fastest since Dec 2019.
- government earlier targeted 400,000+ new homes over six years.
- 2025 measures tightened LTV to 40% in Gangnam/Yongsan while using state-owned land and streamlining reconstruction.
- Stage2 policy, but builder-stock price unavailable.

PF restructuring:
- March 2024 support package 40.6T won for SMEs/builders, liquidity support via guarantees/loans/stabilization fund.
- May 2024 FSS tightened project-finance restructuring.
- real-estate project delinquency rose to 2.70% by end-2023 from 1.19% a year before and 0.37% end-2021.
- syndicated loan 1T won, expandable to 5T won.
- 4B for builders and financials, relief only after bad projects are removed.

Samsung C&T value-up failure:
- activist-backed proposal for higher dividends/buybacks failed.
- Samsung C&T shares closed almost -10%.
- shows construction/holding-company value-up needs board/treasury action, not only undervaluation.

Highway construction collapse:
- elevated highway/bridge structure under construction collapsed near Anseong/Cheonan in Feb 2025.
- at least 3~4 workers killed, several injured/critically hurt.
- Hyundai Engineering was managing the site according to later reporting, but it is not a listed pure-play stock.
- construction safety hard 4C at sector/project level, public-stock price unavailable.

Builder liquidity / housing-price macro:
- construction sector still caught between Seoul housing shortage and PF stress.
- policy supply trigger helps reconstruction builders only if permits, pre-sales and PF funding reopen.
- BOK caution and mortgage tightening mean Stage2 policy does not automatically become Green.
```

---

# 4. 선정 case 요약

| bucket                                 | case                                             | 핵심 판정                                                                          |
| -------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------ |
| structural_success / Stage2-Actionable | **Samsung E&A / Saudi Fadhili gas EPC**          | $6B contract, +8.5%, KOSPI -1.4%                                               |
| Stage2_promote_candidate + 4B          | **Czech nuclear EPC / Doosan·KEPCO E&C**         | Doosan +48%, KEPCO E&C +41% in 3mo, later legal delay                          |
| Stage2 no-price                        | **Seoul housing supply / reconstruction policy** | Seoul +0.76% home price, 400k+ supply, LTV 40%, reconstruction streamlining    |
| 4B / relief                            | **Real-estate PF restructuring**                 | delinquency 2.70%, 1T→5T syndicated loan, builder liquidity support            |
| failed_rerating                        | **Samsung C&T value-up proposal failure**        | activist proposal failed, shares almost -10%                                   |
| hard 4C sector                         | **Highway construction collapse**                | 3~4 deaths, serious injuries, site-safety thesis break; listed-price anchor 없음 |
| Stage2 relief                          | **Builder liquidity package**                    | 40.6T won SME/builder support, but relief not Green                            |

---

# 5. 각 case별 trigger grid

## Case A — Samsung E&A / Saudi Fadhili gas plant EPC

```text
symbol = 028050
case_type = Stage2-Actionable overseas EPC mega contract
archetype = OVERSEAS_EPC_MEGA_CONTRACT_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                                          | 가격 anchor           | outcome |
| ------- | ----------------: | ---------- | --------------------------------------------------------------------------------------- | ------------------- | ------- |
| T0      |            Stage1 | 2024Q1     | Middle East gas/infrastructure EPC order 기대                                             | no entry            |         |
| T1      | Stage2-Actionable | 2024-04-03 | Saudi Aramco Fadhili expansion contract, Samsung E&A share around $6B                   | +8.5% to 26,750 won |         |
| T2      |        validation | 2024-04-03 | Aramco Fadhili gas capacity +60% to 4 bcf/day, sulfur +2,300 t/day, completion Nov 2027 | KOSPI -1.4%         |         |
| T3      |          4B-watch | 2024~2027  | cost overrun, labor/material FX, schedule, Middle East receivables, change order        | 4B                  |         |
| T4      |     Stage3-Yellow | N/A        | backlog margin, progress billing, cost control 확인 필요                                    | 보류                  |         |

Samsung E&A는 이번 R10의 가장 깨끗한 Stage2-Actionable이다. Saudi Aramco Fadhili gas plant expansion에서 Samsung E&A가 약 $6B 계약을 따냈고, 주가는 장중 +8.5%로 26,750원까지 올랐다. 같은 시점 KOSPI는 -1.4%였기 때문에 시장 상대강도도 분명하다. 프로젝트는 Fadhili gas processing capacity를 60% 늘려 하루 4B cubic feet로 만들고, 2027년 11월 완공 예정으로 보도됐다. ([월스트리트저널][1])

```json
{
  "case_id": "r10_loop17_samsung_ena_fadhili_epc",
  "symbol": "028050",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_overseas_EPC_mega_contract",
  "trigger_date": "2024-04-03",
  "contract_value_usd_bn": 6.0,
  "aramco_project_total_value_usd_bn": 7.7,
  "event_return_pct": 8.5,
  "event_price_krw": 26750,
  "kospi_same_context_pct": -1.4,
  "gas_capacity_increase_pct": 60,
  "target_capacity_bcf_per_day": 4,
  "completion_target": "2027-11",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_overseas_EPC"
}
```

---

## Case B — Czech nuclear EPC / Doosan Enerbility·KEPCO Plant S&E·KEPCO E&C

```text
symbols = 034020 / 051600 / 052690 / 015760_readthrough
case_type = Stage2 nuclear infrastructure EPC + legal 4B
archetype = NUCLEAR_INFRA_EPC_STAGE2_WITH_LEGAL_4B
```

| trigger |          type | date         | 당시 공개 evidence                                                                                                        | 가격 anchor                                                       | outcome |
| ------- | ------------: | ------------ | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ------- |
| T0      |     awareness | 2024H1       | Czech nuclear tender 기대, global nuclear revival                                                                       | sector rallied before award                                     |         |
| T1      |        Stage2 | 2024-07-17   | KHNP selected as preferred bidder for two Czech reactors                                                              | Doosan +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% over 3 months |         |
| T2      |    validation | 2024-07-17   | first major Korean overseas nuclear order since 2009; Czech estimated 200B crowns / $8.65B per unit when building two | same                                                            |         |
| T3      |      4B legal | 2024-10~2025 | Czech antitrust/legal appeals; contract signing temporarily blocked/delayed                                           | 4B                                                              |         |
| T4      | Stage3-Yellow | N/A          | final contract, consortium scope, margin, schedule 확인 필요                                                              | 보류                                                              |         |

Czech nuclear case는 R10의 **Stage2_promote_candidate**다. KHNP가 Czech government의 preferred bidder로 선정되면서 한국의 2009년 UAE 이후 첫 major overseas nuclear order가 될 수 있는 trigger가 생겼고, Reuters는 Doosan Enerbility가 3개월 동안 +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% 올랐다고 보도했다. 다만 최종 계약은 협상/법적 이슈가 남아 있었고, 이후 Czech competition watchdog와 court/legal challenge가 계약 체결을 지연시키는 4B로 붙었다. ([Reuters][2])

```json
{
  "case_id": "r10_loop17_czech_nuclear_epc",
  "symbols": "034020/051600/052690/015760_readthrough",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_nuclear_EPC_with_legal_4B",
  "trigger_date": "2024-07-17",
  "doosan_enerbility_3m_return_pct": 48,
  "kepco_plant_service_3m_return_pct": 14,
  "kepco_ec_3m_return_pct": 41,
  "czech_estimated_unit_cost_czk_bn": 200,
  "czech_estimated_unit_cost_usd_bn": 8.65,
  "4B_overlay": [
    "final_contract_not_signed_at_trigger",
    "EDF_Westinghouse_appeals",
    "Czech_antitrust_watchdog_delay",
    "court_challenge",
    "margin_and_scope_uncertain"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_promote_candidate_with_legal_4B"
}
```

---

## Case C — Seoul housing supply / reconstruction policy

```text
symbols = 000720 / 006360 / 047040 / 028050 / 294870 / builder_basket
case_type = Stage2 housing-supply and reconstruction policy no direct price
archetype = HOUSING_SUPPLY_RECONSTRUCTION_POLICY_STAGE2_NO_PRICE
```

| trigger |              type | date       | 당시 공개 evidence                                                             | 가격 anchor                     | outcome |
| ------- | ----------------: | ---------- | -------------------------------------------------------------------------- | ----------------------------- | ------- |
| T0      |            Stage1 | 2024-07~08 | Seoul home prices accelerating, reconstruction demand                      | Seoul +0.76% MoM in July 2024 |         |
| T1      |     Stage2 policy | 2024-08    | government targets 400k+ new homes over six years                          | stock price unavailable       |         |
| T2      | Stage2 refinement | 2025-09-07 | LTV Gangnam/Yongsan 50%→40%, state-owned land, reconstruction streamlining | no builder event return       |         |
| T3      |          4B-watch | 2025~      | mortgage tightening, household debt, PF funding, pre-sale absorption       | 4B                            |         |
| T4      |     Stage3-Yellow | N/A        | permits, pre-sales, actual builder backlog/margin needed                   | 보류                            |         |

주택공급/재건축은 R10에서 중요한 Stage2지만, 이번 source set에서는 builder basket의 직접 price anchor가 없다. Seoul home prices는 2024년 7월 +0.76%로 2019년 12월 이후 가장 빠른 월간 상승률을 보였고, 정부는 6년간 400,000채 이상 공급 목표를 제시했다. 2025년 9월에는 Gangnam/Yongsan 등 일부 지역 LTV를 50%에서 40%로 낮추는 동시에, state-run firms 보유 토지 활용과 재건축 규제 간소화를 언급했다. 이는 builders에 Stage2 policy trigger지만, mortgage tightening과 PF funding이 4B다. ([Reuters][3])

```json
{
  "case_id": "r10_loop17_seoul_housing_supply_reconstruction",
  "symbols": "000720/006360/047040/028050/294870/builder_basket",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_housing_supply_reconstruction_policy_no_price",
  "trigger_period": "2024-08_to_2025-09",
  "seoul_home_price_mom_july_2024_pct": 0.76,
  "housing_supply_target_units_over_6y": ">400000",
  "ltv_tightening_target_areas": [
    "Gangnam",
    "Yongsan"
  ],
  "ltv_after_policy_pct": 40,
  "ltv_before_policy_pct": 50,
  "direct_builder_price_anchor": "price_data_unavailable_after_deep_search",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_policy_no_direct_price"
}
```

---

## Case D — Real-estate PF restructuring / builder liquidity stress

```text
symbols = 009410 / 000720 / 006360 / 047040 / PF_exposed_builder_basket
case_type = 4B real-estate PF restructuring
archetype = REAL_ESTATE_PF_RESTRUCTURING_4B
```

| trigger |              type | date       | 당시 공개 evidence                                                                  | 가격 anchor            | outcome |
| ------- | ----------------: | ---------- | ------------------------------------------------------------------------------- | -------------------- | ------- |
| T0      |     4B background | 2023-12    | Taeyoung E&C debt-rescheduling triggered broader builder-liquidity concern      | price unavailable    |         |
| T1      |     Stage2 relief | 2024-03-27 | 40.6T won support for SMEs/builders; guarantees, loans, stabilizing fund        | no stock anchor      |         |
| T2      |      4B hardening | 2024-05-13 | FSS tightens project assessment; delinquency 2.70% end-2023 vs 1.19% prior year | no price             |         |
| T3      | relief validation | 2024-05-13 | 1T won syndicated loan, expandable to 5T won                                    | relief but not Green |         |
| T4      |     Stage3-Yellow | N/A        | bad-project writeoff, PF rollover, pre-sale cash recovery needed                | 보류                   |         |

PF restructuring은 R10의 핵심 4B다. 2024년 3월 정부는 중소기업과 건설사에 40.6T won 규모 지원책을 준비했고, 건설사에는 보증 확대, 추가 대출, market-stabilizing fund를 통한 liquidity support를 제시했다. 그러나 2024년 5월 FSS는 부실 부동산 PF project restructuring을 더 엄격히 하겠다고 밝혔고, real-estate project delinquency rate가 2021년 말 0.37% → 2022년 말 1.19% → 2023년 말 2.70%로 뛰었다. 1T won syndicated loan은 필요하면 5T won까지 확대 가능하지만, 이건 Green이 아니라 “부실 정리용 완충재”다. ([Reuters][4])

```json
{
  "case_id": "r10_loop17_real_estate_pf_restructuring",
  "symbols": "009410/000720/006360/047040/PF_exposed_builder_basket",
  "best_trigger": "T1/T3",
  "best_trigger_type": "4B_real_estate_PF_restructuring_with_relief",
  "support_date": "2024-03-27",
  "support_package_krw_trn": 40.6,
  "pf_restructuring_date": "2024-05-13",
  "project_delinquency_end_2021_pct": 0.37,
  "project_delinquency_end_2022_pct": 1.19,
  "project_delinquency_end_2023_pct": 2.70,
  "syndicated_loan_initial_krw_trn": 1.0,
  "syndicated_loan_max_krw_trn": 5.0,
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "PF_4B_with_policy_relief_not_Green"
}
```

---

## Case E — Samsung C&T value-up / activist proposal failure

```text
symbol = 028260
case_type = failed_rerating / construction-holdco value-up
archetype = CONSTRUCTION_HOLDCO_VALUEUP_FAILED_RERATING
```

| trigger |            type | date       | 당시 공개 evidence                                                                     | 가격 anchor                 | outcome |
| ------- | --------------: | ---------- | ---------------------------------------------------------------------------------- | ------------------------- | ------- |
| T0      |          Stage1 | 2024Q1     | Korea value-up, Samsung C&T undervaluation, activist proposals                     | optimism                  |         |
| T1      | failed_rerating | 2024-03-15 | activist-backed dividend/buyback proposal failed                                   | shares almost -10%        |         |
| T2      |      validation | 2024-03-15 | Norway oil fund / Canadian pension support insufficient; NPS sided with management | failed governance trigger |         |
| T3      |        4B-watch | 2024~      | holding discount, board control, capital return credibility                        | 4B                        |         |
| T4      |   Stage3-Yellow | N/A        | board-approved capital return and cancellation needed                              | 보류                        |         |

Samsung C&T는 R10에서 “건설사/holding value-up”이 왜 Green으로 바로 못 가는지 보여주는 failed_rerating case다. Activist-backed proposal for higher dividends and buybacks가 실패하자 Samsung C&T shares는 거의 -10%로 마감했다. Norway oil fund와 Canadian pension giants가 지지했지만 NPS가 management 편에 섰다는 점은, undervaluation 자체보다 **실제 board action / treasury action**이 Stage2-Actionable의 핵심이라는 뜻이다. ([Financial Times][5])

```json
{
  "case_id": "r10_loop17_samsung_ct_valueup_failed",
  "symbol": "028260",
  "best_trigger": "T1/T3",
  "best_trigger_type": "failed_rerating_construction_holdco_valueup",
  "trigger_date": "2024-03-15",
  "event_return_pct": "almost_-10",
  "proposal": [
    "higher_dividend",
    "share_buyback"
  ],
  "supporters": [
    "Norway_oil_fund",
    "Canadian_pension_giants",
    "activist_investors"
  ],
  "negative_driver": "NPS_sided_with_management",
  "4B_overlay": [
    "holding_company_discount",
    "board_control",
    "weak_capital_return_commitment",
    "construction_holdco_governance"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "failed_rerating_valueup_governance"
}
```

---

## Case F — Highway construction collapse / construction-site safety

```text
symbols = Hyundai_Engineering_private / construction_safety_basket
case_type = construction safety hard 4C at sector/project level
archetype = CONSTRUCTION_SITE_SAFETY_HARD_4C_NO_PUBLIC_PRICE
```

| trigger |                type | date       | 당시 공개 evidence                                                                             | 가격 anchor                      | outcome |
| ------- | ------------------: | ---------- | ------------------------------------------------------------------------------------------ | ------------------------------ | ------- |
| T0      |   hard safety event | 2025-02-25 | elevated highway/bridge construction structure collapsed near Anseong/Cheonan              | public-stock price unavailable |         |
| T1      |          validation | 2025-02-25 | at least 3~4 deaths, 6 injured, several critically injured                                 | sector hard 4C                 |         |
| T2      | attribution context | 2025-02-25 | later reporting identified Hyundai Engineering as construction manager; private/not listed | no listed price                |         |
| T3      |         4B/4C-watch | 2025~      | investigation, work suspension, penalties, safety-score/brand damage                       | 4B/4C                          |         |
| T4      |              relief | N/A        | final investigation and public-company financial impact needed                             | 보류                             |         |

건설 안전사고는 R10에서 hard 4C가 될 수 있다. 2025년 2월 elevated highway/bridge structure collapse로 최소 3~4명이 사망하고 여러 명이 중상 또는 위중한 상태였다고 보도됐다. Reuters는 50m steel structures가 순차적으로 collapse했다고 보도했고, 이후 보도에서는 Hyundai Engineering이 site를 관리하고 있었다고 설명됐다. 다만 Hyundai Engineering은 listed pure-play가 아니므로 public-stock MFE/MAE는 계산하지 않는다. 이 case는 **sector/project-level hard safety 4C**, public-price unavailable이다. ([Reuters][6])

```json
{
  "case_id": "r10_loop17_highway_construction_collapse_safety",
  "symbols": "Hyundai_Engineering_private/construction_safety_basket",
  "best_trigger": "T0/T3",
  "best_trigger_type": "hard_4C_construction_site_safety_no_public_price",
  "trigger_date": "2025-02-25",
  "fatalities_context": "at_least_3_to_4",
  "injured_context": 6,
  "critical_injuries_context": "several",
  "structure_context": "five_50m_steel_support_structures_collapsed",
  "public_stock_price_anchor": "price_data_unavailable_after_deep_search",
  "hard_4C_status": "sector_project_level_confirmed_public_stock_not_available",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "construction_safety_hard_4C_no_public_price"
}
```

---

## Case G — Builder liquidity support / rate-housing macro relief

```text
symbols = builder_basket / banks_PF_readthrough
case_type = Stage2 relief, not Green
archetype = BUILDER_LIQUIDITY_SUPPORT_STAGE2_RELIEF
```

| trigger |          type | date       | 당시 공개 evidence                                                                         | 가격 anchor      | outcome |
| ------- | ------------: | ---------- | -------------------------------------------------------------------------------------- | -------------- | ------- |
| T0      |      4B macro | 2024~2026  | high rates, weak construction sector, Seoul housing imbalance                          | no price       |         |
| T1      | Stage2 relief | 2024-03-27 | guarantees/loans for viable real-estate projects                                       | no stock price |         |
| T2      |    rate macro | 2025-10-23 | BOK held 2.50%, surprised with possible cuts; construction sector weak but housing hot | macro relief   |         |
| T3      |            4B | 2026-02    | BOK expected to keep 2.50% through 2026 due FX/housing risks                           | cuts delayed   |         |
| T4      | Stage3-Yellow | N/A        | financing costs, PF rollover and pre-sale recovery needed                              | 보류             |         |

Builder liquidity relief는 Stage2 relief이지 Green이 아니다. 2024년 3월 support package는 viable PF projects에 보증과 대출을 제공하는 방식이었고, 2025년 10월 BOK는 2.50% 동결에도 추가 cut 가능성을 열어 시장을 밀어올렸지만, housing overheating과 weak construction sector가 같이 존재했다. 2026년 poll에서는 BOK가 2026년 내내 2.50%를 유지할 것으로 예상됐는데, 이유는 won weakness와 housing risk였다. 즉 R10에서 금리완화 기대는 좋지만, 실제 PF rollover와 pre-sale cash 회복 전까지 Green은 아니다. ([Reuters][4])

```json
{
  "case_id": "r10_loop17_builder_liquidity_rate_relief",
  "symbols": "builder_basket/banks_PF_readthrough",
  "best_trigger": "T1/T4",
  "best_trigger_type": "Stage2_relief_builder_liquidity_rate_macro",
  "support_date": "2024-03-27",
  "support_package_krw_trn": 40.6,
  "bok_hold_rate_2025_10_23_pct": 2.50,
  "bok_expected_rate_2026_pct": 2.50,
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "4B_overlay": [
    "FX_weakness",
    "housing_overheating",
    "PF_refinancing",
    "construction_sector_weakness",
    "pre_sale_absorption"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "builder_relief_stage2_not_green"
}
```

---

# 6. Trigger별 실제 가격경로 검증 요약

이번 R10 Loop 17은 full OHLC가 없으므로 아래 표는 **reported event anchor 기준**이다.

| case                          | best trigger |                          event return / price |     market-relative | full MFE/MAE | outcome                     |
| ----------------------------- | -----------: | --------------------------------------------: | ------------------: | ------------ | --------------------------- |
| Samsung E&A / Fadhili         |           T1 |                                +8.5%, 26,750원 | KOSPI -1.4%, +9.9pp | unavailable  | excellent Stage2-Actionable |
| Czech nuclear EPC             |        T1/T3 |            Doosan +48%, KEPCO E&C +41% in 3mo |       sector strong | unavailable  | Stage2 with legal 4B        |
| Seoul housing/reconstruction  |        T1/T3 |    stock price unavailable; Seoul home +0.76% |                 N/A | unavailable  | Stage2 policy no-price      |
| PF restructuring              |        T1/T3 | no stock price; delinquency 2.70%, 1T→5T loan |                 N/A | unavailable  | PF 4B with relief           |
| Samsung C&T value-up failure  |           T1 |                                   almost -10% |            negative | unavailable  | failed_rerating             |
| Highway collapse              |        T0/T3 |                      public stock unavailable |                 N/A | unavailable  | sector/project hard 4C      |
| Builder liquidity/rate relief |        T1/T4 |                               no direct price |                 N/A | unavailable  | Stage2 relief, not Green    |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
가장 좋은 Stage2:
1. Samsung E&A / Fadhili: contract value + price reaction + market-relative return이 모두 닫힘.
2. Czech nuclear EPC: 3개월 sector return은 강하지만 final contract/legal 4B.
3. Seoul housing/reconstruction policy: policy trigger는 강하지만 builder price anchor 없음.
4. Builder liquidity support: relief는 있지만 PF 부실정리 전까지 Green 불가.
```

## Stage2-Actionable entry 성과

```text
Stage2-Actionable:
- Samsung E&A / Fadhili.

Stage2_promote_candidate:
- Czech nuclear EPC basket.
- Seoul reconstruction/housing supply basket, price anchor 확보 시.
- Builder liquidity relief, PF rollover and pre-sales 회복 확인 시.

Actionable 금지:
- Samsung C&T value-up proposal failure.
- PF restructuring without loss recognition.
- construction safety collapse.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Samsung E&A: progress billing, backlog margin, cost control 확인 시.
- Czech nuclear: final contract, legal appeal clearance, consortium scope/margin 확인 시.
- Housing/reconstruction: actual permits, pre-sales and builder backlog 확인 시.
- PF restructuring: non-performing project writeoff, refinancing and pre-sale cash recovery 확인 시.
```

## Stage3-Green

```text
이번 R10 Loop 17에서 확정 Green 없음.

이유:
- full OHLC/MFE/MAE가 없다.
- Samsung E&A는 좋은 Stage2지만 cost/schedule/margin gate가 남는다.
- Czech nuclear는 법적 appeal/final contract가 남는다.
- housing policy는 stock price와 분양/인허가 conversion이 없다.
- PF relief는 부실 정리 전에는 Green이 아니라 4B 완충재다.
- safety event는 hard 4C가 될 수 있지만 listed price anchor가 없다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Samsung E&A / Fadhili as excellent Stage2-Actionable.
- Czech nuclear EPC as Stage2_promote_candidate with legal 4B.
- Seoul housing/reconstruction as Stage2 no-price.
- PF restructuring as 4B with policy relief.
- Samsung C&T activist failure as failed_rerating.
- highway collapse as sector-level construction safety hard 4C without public price.
- builder liquidity/rate relief as Stage2 relief, not Green.

false_positive_score:
- housing policy를 builder Green으로 바로 올리는 경우.
- Czech nuclear preferred bidder를 final contract 없이 Green으로 올리는 경우.
- PF liquidity support를 부실 해소로 착각하는 경우.
- Samsung C&T undervaluation을 board action 없이 Green으로 올리는 경우.
- construction support package를 actual earnings recovery 없이 Green으로 올리는 경우.

Stage2_promote_candidate:
- Samsung E&A / Fadhili.
- Czech nuclear EPC basket.
- Seoul reconstruction/housing supply.
- builder liquidity support after PF rollover.

evidence_good_but_price_failed:
- Samsung C&T value-up failure.
- PF relief if builder prices fail despite support.

event_premium:
- Samsung E&A Saudi mega contract.
- Czech nuclear preferred bidder.
- housing supply/reconstruction policy.

thesis_break:
- construction-site fatal collapse at project/sector level.
- PF default cascade if support fails.

hard_4C:
- public-listed hard 4C not confirmed in R10 source set.
- sector/project hard 4C confirmed for highway construction collapse, but no listed-stock price anchor.
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
overseas_EPC_contract_value,+5,"계약금액과 가격반응이 같이 닫히면 R10 Stage2-Actionable","Samsung E&A"
market_relative_contract_reaction,+5,"KOSPI 하락 중 +8.5%면 강한 trigger","Samsung E&A"
nuclear_infra_EPC_optionality,+4,"preferred bidder와 sector rerating이 같이 나오면 Stage2 후보","Czech nuclear"
housing_supply_policy,+3,"주택공급·재건축 규제완화는 builder Stage2 후보","Seoul supply policy"
PF_restructuring_recognition,+5,"PF 부실 인식과 정리 속도가 R10 핵심 4B","PF restructuring"
liquidity_relief,+3,"보증·대출·stabilization fund는 relief score","builder support"
capital_return_governance,+4,"건설 holding은 board-approved return이 중요","Samsung C&T"
construction_safety_risk,+5,"사망사고·붕괴는 hard 4C 가능","highway collapse"
```

## 내릴 축

```csv
axis,delta,reason,cases
preferred_bidder_without_final_contract,-5,"최종계약 전 Green 금지","Czech nuclear"
policy_without_builder_price,-4,"정책만 있고 주가/분양/수주 anchor 없으면 Actionable 금지","housing supply"
liquidity_support_without_loss_cleanup,-5,"유동성 지원만으로 PF 부실 해소 판단 금지","PF restructuring"
overseas_EPC_without_margin_visibility,-4,"대형 EPC도 원가·공기·환율 확인 전 Green 금지","Samsung E&A"
valueup_without_board_action,-5,"주주제안 실패는 value-up false positive","Samsung C&T"
construction_safety_ignored,-5,"붕괴·사망사고 무시 금지","highway collapse"
housing_price_rally_without_affordability,-4,"집값 상승만으로 builder Green 금지","Seoul housing"
rate_cut_hope_without_refinancing,-4,"금리 기대만으로 PF rollover 회복 판단 금지","builder liquidity"
```

---

# 10. Stage2-Actionable 승격 조건

R10 Loop 17 shadow rule:

```text
R10에서 Stage2 evidence가 아래 중 4개 이상이면 Stage2-Actionable로 승격한다.

1. event return +5% 이상 또는 market-relative +5pp 이상
2. contract / policy / support / deal value가 숫자로 명확하다
3. 수익경로가 EPC backlog, progress billing, pre-sale cash, PF rollover, rental/yield로 연결된다
4. cost/schedule/PF/safety/legal 4B가 식별 가능하다
5. price reaction이 evidence와 같은 방향으로 검증된다
6. 단순 preferred bidder가 아니라 final contract 또는 high-probability conversion path가 있다
7. recurring margin or cash conversion으로 이어질 수 있다
```

적용:

```text
Samsung E&A:
1,2,3,4,5,7 충족 → Stage2-Actionable.

Czech nuclear:
1,2,3,4,5 충족하지만 6 미충족 → Stage2_promote_candidate + 4B.

Housing supply:
2,3,4 충족하지만 1/5 없음 → Stage2 no-price.

PF restructuring:
2,3,4 충족하지만 negative/relief trigger → 4B with relief.

Samsung C&T:
1 negative, 4 충족 → failed_rerating.

Highway collapse:
negative safety 4C, public price 없음 → sector hard 4C no-price.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
Stage2 이후 아래 중 2개 이상이 추가로 닫히면 Yellow.

1. EPC progress billing and margin visibility.
2. final contract / legal appeal clearance.
3. housing permits and pre-sales convert to backlog.
4. PF rollover / delinquency stabilizes.
5. raw-material and labor cost pass-through.
6. board-approved buyback/dividend/cancellation.
7. safety/regulatory investigation closed without material penalty.
```

Yellow 후보:

```text
Samsung E&A:
progress billing + cost control + margin 확인 시 Yellow.

Czech nuclear:
final contract + appeal clearance + consortium scope 확인 시 Yellow.

Housing supply:
actual permits + builder backlog + pre-sale absorption 확인 시 Yellow.

Builder liquidity:
PF rollover + bad-project writeoff + funding cost stabilization 확인 시 Yellow.

Samsung C&T:
board-approved capital return and cancellation 확인 시 Yellow.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- contract backlog converts into margin and cash flow.
- PF delinquency falls and refinancing channels reopen.
- housing policy converts into permits, starts, pre-sales and OP.
- preferred bidder becomes signed contract.
- safety/legal/governance 4B is contained.
- full-window MFE/MAE is favorable.
```

이번 R10 Loop 17에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + margin/PF/final-contract/pre-sale/safety-clearance gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- preferred bidder without final contract.
- large EPC contract without margin and schedule control.
- housing supply policy without actual permits/pre-sales.
- PF support without loss recognition.
- mortgage tightening that suppresses demand.
- activist value-up failure.
- construction safety accident.
- raw-material/labor cost inflation.
```

적용:

```text
Samsung E&A:
cost/schedule/change-order 4B.

Czech nuclear:
legal appeal and final-contract 4B.

Housing supply:
mortgage tightening/PF funding 4B.

PF restructuring:
delinquency and bad-project cleanup 4B.

Samsung C&T:
governance/value-up failure 4B.

Highway collapse:
safety hard 4C at project level.

Builder liquidity:
rate and refinancing 4B.
```

---

# 14. 4C hard gate 조건

```text
R10 4C:
- listed builder debt workout / court receivership with stock crash
- fatal collapse with public-company price collapse and regulatory sanction
- PF default cascade causing equity impairment
- final-contract cancellation after preferred-bidder premium
- large EPC cost overrun destroying margin
- safety/license suspension blocking bidding
```

이번 R10 Loop 17 hard/strong 4C:

```text
sector/project hard 4C:
- highway construction collapse confirmed as safety thesis break.

listed-stock hard 4C:
- not confirmed with reliable price anchor in this source set.
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R10 production 설계 원칙:

```text
1. overseas EPC headline과 margin/cash conversion을 분리한다.
2. preferred bidder와 final contract를 분리한다.
3. housing supply policy와 actual permits/pre-sales를 분리한다.
4. PF liquidity support와 bad-project cleanup을 분리한다.
5. construction holding value-up은 board action/cancellation이 있어야 한다.
6. fatal construction safety event는 hard 4C 후보지만 listed price anchor가 필요하다.
7. Stage2 relief와 Stage3 Green을 분리한다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_259.md 요약

```md
# R10 Loop 17. Construction / Real Estate / Building Materials Trigger-level Price Validation

이번 라운드는 R10 Loop 17 trigger-level validation 라운드다.

핵심 결론:
- Samsung E&A / Saudi Fadhili is the cleanest R10 Stage2-Actionable case. Samsung E&A won around $6B of Saudi Aramco’s Fadhili gas plant expansion contract; shares rose as much as 8.5% to 26,750 won while KOSPI fell 1.4%.
- Czech nuclear EPC is Stage2_promote_candidate with legal 4B. KHNP was selected as preferred bidder for two Czech reactors; Doosan Enerbility rose 48%, KEPCO Plant S&E 14%, and KEPCO E&C 41% over three months, but final contract and legal appeals remain 4B.
- Seoul housing supply / reconstruction policy is Stage2 no-price. Seoul home prices rose 0.76% in July 2024 and government targeted 400k+ homes, later tightening LTV to 40% in wealthy Seoul districts while using state-owned land and streamlining reconstruction.
- Real-estate PF restructuring is 4B with policy relief. Builder support of 40.6T won and a 1T won syndicated loan expandable to 5T won help liquidity, but real-estate project delinquency rose to 2.70% by end-2023.
- Samsung C&T value-up failure is failed_rerating. Activist-backed dividend/buyback proposals failed, sending shares almost 10% lower.
- Highway construction collapse is sector/project hard 4C no public price. An elevated bridge/highway construction collapse killed at least 3~4 workers; listed-stock price anchor was unavailable.
- Builder liquidity support is Stage2 relief, not Green. Rate-cut hopes, guarantees and loans are only useful after PF rollover, pre-sales and bad-project cleanup improve.

Main calibration:
- Raise overseas_EPC_contract_value, market_relative_contract_reaction, nuclear_infra_EPC_optionality, housing_supply_policy, PF_restructuring_recognition, liquidity_relief, capital_return_governance, construction_safety_risk.
- Lower preferred_bidder_without_final_contract, policy_without_builder_price, liquidity_support_without_loss_cleanup, overseas_EPC_without_margin_visibility, valueup_without_board_action, construction_safety_ignored, housing_price_rally_without_affordability, rate_cut_hope_without_refinancing.
```

## docs/checkpoints/checkpoint_28a_round259_r10_loop17.md 요약

```md
# Checkpoint 28A Round 259 R10 Loop 17 Trigger-level Calibration

## 반영 내용
- R10 Loop 17 trigger-level validation을 수행했다.
- Samsung E&A Fadhili, Czech nuclear EPC, Seoul housing/reconstruction policy, PF restructuring, Samsung C&T value-up failure, highway construction collapse, builder liquidity/rate relief를 검토했다.
- full adjusted OHLC는 확보하지 못했으므로 Reuters / WSJ / FT / AP reported event return과 event price anchor를 사용했다.
- MFE/MAE는 조작하지 않고 price_data_unavailable_after_deep_search로 분리했다.

## 핵심 보정
- Overseas EPC can be Stage2-Actionable when contract size and price reaction close together.
- Preferred bidder is not final contract.
- Housing policy must convert into permits, starts, pre-sales and backlog.
- PF liquidity support is relief, not Green, until bad-project cleanup occurs.
- Construction-holdco value-up needs board-approved capital return.
- Fatal safety events are hard 4C candidates, but listed-stock price anchor is required for public-equity classification.
```

## data/e2r_case_library/cases_r10_loop17_round259.jsonl 초안

```jsonl
{"case_id":"r10_loop17_samsung_ena_fadhili_epc","symbol":"028050","company_name":"Samsung E&A","case_type":"Stage2_Actionable_overseas_EPC_mega_contract","primary_archetype":"OVERSEAS_EPC_MEGA_CONTRACT_STAGE2_ACTIONABLE","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2024-04-03","contract_value_usd_bn":6.0,"aramco_project_total_value_usd_bn":7.7,"event_return_pct":8.5,"event_price_krw":26750,"kospi_same_context_pct":-1.4,"gas_capacity_increase_pct":60,"target_capacity_bcf_per_day":4,"completion_target":"2027-11","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_overseas_EPC","notes":"Mega EPC contract and market-relative price reaction aligned; cost, schedule and margin are Yellow gates."}
{"case_id":"r10_loop17_czech_nuclear_epc","symbol":"034020/051600/052690/015760_readthrough","company_name":"Doosan Enerbility / KEPCO Plant S&E / KEPCO E&C / KEPCO readthrough","case_type":"Stage2_nuclear_EPC_with_legal_4B","primary_archetype":"NUCLEAR_INFRA_EPC_STAGE2_WITH_LEGAL_4B","best_trigger":"T1/T3","stage_candidate":"Stage2_promote_candidate + 4B-watch","price_validation":{"trigger_date":"2024-07-17","doosan_enerbility_3m_return_pct":48,"kepco_plant_service_3m_return_pct":14,"kepco_ec_3m_return_pct":41,"czech_estimated_unit_cost_czk_bn":200,"czech_estimated_unit_cost_usd_bn":8.65,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate_with_legal_4B","notes":"Preferred bidder and sector rerating aligned, but final contract/legal appeals remain 4B."}
{"case_id":"r10_loop17_seoul_housing_supply_reconstruction","symbol":"000720/006360/047040/028050/294870/builder_basket","company_name":"Korea builder basket","case_type":"Stage2_housing_supply_reconstruction_policy_no_price","primary_archetype":"HOUSING_SUPPLY_RECONSTRUCTION_POLICY_STAGE2_NO_PRICE","best_trigger":"T1/T3","stage_candidate":"Stage2 no-price","price_validation":{"trigger_period":"2024-08_to_2025-09","seoul_home_price_mom_july_2024_pct":0.76,"housing_supply_target_units_over_6y":">400000","ltv_after_policy_pct":40,"ltv_before_policy_pct":50,"direct_builder_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_policy_no_direct_price","notes":"Housing supply/reconstruction policy is Stage2, but builder price, permits and pre-sale conversion are missing."}
{"case_id":"r10_loop17_real_estate_pf_restructuring","symbol":"009410/000720/006360/047040/PF_exposed_builder_basket","company_name":"Taeyoung E&C / builder PF basket","case_type":"4B_real_estate_PF_restructuring_with_relief","primary_archetype":"REAL_ESTATE_PF_RESTRUCTURING_4B","best_trigger":"T1/T3","stage_candidate":"4B with relief","price_validation":{"support_date":"2024-03-27","support_package_krw_trn":40.6,"pf_restructuring_date":"2024-05-13","project_delinquency_end_2021_pct":0.37,"project_delinquency_end_2022_pct":1.19,"project_delinquency_end_2023_pct":2.70,"syndicated_loan_initial_krw_trn":1.0,"syndicated_loan_max_krw_trn":5.0,"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"PF_4B_with_policy_relief_not_Green","notes":"PF support is relief; bad-project cleanup and refinancing must improve before Yellow."}
{"case_id":"r10_loop17_samsung_ct_valueup_failed","symbol":"028260","company_name":"Samsung C&T","case_type":"failed_rerating_construction_holdco_valueup","primary_archetype":"CONSTRUCTION_HOLDCO_VALUEUP_FAILED_RERATING","best_trigger":"T1/T3","stage_candidate":"failed_rerating + 4B-watch","price_validation":{"trigger_date":"2024-03-15","event_return_pct":"almost_-10","proposal":["higher_dividend","share_buyback"],"negative_driver":"NPS_sided_with_management","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"failed_rerating_valueup_governance","notes":"Undervaluation and activist support were not enough; board action/capital return failed."}
{"case_id":"r10_loop17_highway_construction_collapse_safety","symbol":"Hyundai_Engineering_private/construction_safety_basket","company_name":"Hyundai Engineering private / construction safety basket","case_type":"hard_4C_construction_site_safety_no_public_price","primary_archetype":"CONSTRUCTION_SITE_SAFETY_HARD_4C_NO_PUBLIC_PRICE","best_trigger":"T0/T3","stage_candidate":"sector/project hard 4C","price_validation":{"trigger_date":"2025-02-25","fatalities_context":"at_least_3_to_4","injured_context":6,"critical_injuries_context":"several","structure_context":"five_50m_steel_support_structures_collapsed","public_stock_price_anchor":"price_data_unavailable_after_deep_search","hard_4C_status":"sector_project_level_confirmed_public_stock_not_available"},"score_price_alignment":"construction_safety_hard_4C_no_public_price","notes":"Fatal construction collapse is a hard safety thesis break, but no listed pure-play price anchor was available."}
{"case_id":"r10_loop17_builder_liquidity_rate_relief","symbol":"builder_basket/banks_PF_readthrough","company_name":"Korea builder liquidity basket","case_type":"Stage2_relief_builder_liquidity_rate_macro","primary_archetype":"BUILDER_LIQUIDITY_SUPPORT_STAGE2_RELIEF","best_trigger":"T1/T4","stage_candidate":"Stage2 relief","price_validation":{"support_date":"2024-03-27","support_package_krw_trn":40.6,"bok_hold_rate_2025_10_23_pct":2.50,"bok_expected_rate_2026_pct":2.50,"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"builder_relief_stage2_not_green","notes":"Liquidity/rate relief is not Green until PF rollover, pre-sales and bad-project cleanup improve."}
```

## data/e2r_trigger_calibration/triggers_r10_loop17_round259.jsonl 초안

```jsonl
{"trigger_id":"r10l17_samsung_ena_fadhili_T1","case_id":"r10_loop17_samsung_ena_fadhili_epc","trigger_type":"Stage2-Actionable_overseas_EPC_contract","trigger_date":"2024-04-03","event_return_pct":8.5,"event_price_krw":26750,"market_relative_pp":9.9,"trigger_outcome_label":"excellent_stage2_actionable_overseas_EPC","promote_to":"Stage2-Actionable"}
{"trigger_id":"r10l17_czech_nuclear_T1","case_id":"r10_loop17_czech_nuclear_epc","trigger_type":"Stage2_nuclear_EPC_preferred_bidder","trigger_date":"2024-07-17","event_return_pct":"Doosan_3m_+48_KEPCO_EC_3m_+41","trigger_outcome_label":"Stage2_promote_candidate_with_legal_4B","promote_to":"Stage2_promote_candidate"}
{"trigger_id":"r10l17_czech_legal_T3","case_id":"r10_loop17_czech_nuclear_epc","trigger_type":"4B_legal_appeal_final_contract_delay","trigger_date":"2024-10_to_2025","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"legal_contract_delay_4B","promote_to":"4B-watch"}
{"trigger_id":"r10l17_housing_supply_T1","case_id":"r10_loop17_seoul_housing_supply_reconstruction","trigger_type":"Stage2_housing_supply_reconstruction_policy","trigger_date":"2024-08_to_2025-09","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_policy_no_direct_price","promote_to":"Stage2"}
{"trigger_id":"r10l17_pf_support_T1","case_id":"r10_loop17_real_estate_pf_restructuring","trigger_type":"Stage2_relief_builder_PF_support","trigger_date":"2024-03-27","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"PF_relief_not_Green","promote_to":"Stage2_relief"}
{"trigger_id":"r10l17_pf_restructuring_T2","case_id":"r10_loop17_real_estate_pf_restructuring","trigger_type":"4B_real_estate_PF_restructuring","trigger_date":"2024-05-13","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"PF_restructuring_4B","promote_to":"4B-watch"}
{"trigger_id":"r10l17_samsung_ct_valueup_T1","case_id":"r10_loop17_samsung_ct_valueup_failed","trigger_type":"failed_rerating_valueup_governance","trigger_date":"2024-03-15","event_return_pct":"almost_-10","trigger_outcome_label":"valueup_failed_rerating","promote_to":"no_actionable"}
{"trigger_id":"r10l17_highway_collapse_T0","case_id":"r10_loop17_highway_construction_collapse_safety","trigger_type":"hard_4C_construction_safety_no_public_price","trigger_date":"2025-02-25","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"sector_project_hard_4C_no_public_stock","promote_to":"4C_sector_watch"}
{"trigger_id":"r10l17_builder_liquidity_T1","case_id":"r10_loop17_builder_liquidity_rate_relief","trigger_type":"Stage2_builder_liquidity_relief","trigger_date":"2024-03-27","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"builder_relief_stage2_not_Green","promote_to":"Stage2_relief"}
```

## data/sector_taxonomy/score_weight_profiles_round259_r10_loop17_v1.csv 초안

```csv
archetype,overseas_EPC_contract_value,market_relative_contract_reaction,nuclear_infra_EPC_optionality,housing_supply_policy,PF_restructuring_recognition,liquidity_relief,capital_return_governance,construction_safety_risk,preferred_bidder_without_final_contract_penalty,policy_without_builder_price_penalty,liquidity_support_without_loss_cleanup_penalty,overseas_EPC_without_margin_visibility_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
OVERSEAS_EPC_MEGA_CONTRACT_STAGE2_ACTIONABLE,+5,+5,+0,+0,+0,+0,+0,+1,-1,-1,-1,-4,Samsung E&A $6B +8.5 vs KOSPI -1.4,cost/schedule margin missing,progress billing+margin+cost control,Samsung E&A.
NUCLEAR_INFRA_EPC_STAGE2_WITH_LEGAL_4B,+2,+3,+5,+0,+0,+1,+0,+1,-5,-1,-1,-3,Czech nuclear preferred bidder drove sector rerating,final contract/legal 4B,final contract+scope+margin,Doosan/KEPCO E&C.
HOUSING_SUPPLY_RECONSTRUCTION_POLICY_STAGE2_NO_PRICE,+0,+0,+0,+5,+2,+2,+0,+1,-1,-4,-2,-1,Seoul supply/reconstruction policy,price/pre-sale missing,permits+pre-sales+backlog,builder basket.
REAL_ESTATE_PF_RESTRUCTURING_4B,+0,+0,+0,+1,+5,+4,+0,+1,-1,-2,-5,-1,PF delinquency 2.70% and restructuring,relief not Green,bad-project cleanup+refinancing,PF basket.
CONSTRUCTION_HOLDCO_VALUEUP_FAILED_RERATING,+0,+0,+0,+0,+1,+0,+5,+0,-1,-1,-1,-1,Samsung C&T activist failure -10,board action missing,board-approved return+cancellation,Samsung C&T.
CONSTRUCTION_SITE_SAFETY_HARD_4C_NO_PUBLIC_PRICE,+0,+0,+0,+0,+1,+0,+0,+5,-1,-1,-1,-1,fatal construction collapse,listed price unavailable,regulatory closure+penalty visibility,sector safety.
BUILDER_LIQUIDITY_SUPPORT_STAGE2_RELIEF,+0,+0,+0,+2,+4,+5,+0,+1,-1,-2,-5,-1,40.6T builder support,PF rollover/pre-sale missing,refinancing+cash conversion,builder basket.
```

---

# 이번 R10 Loop 17 결론

```text
1. Samsung E&A / Saudi Fadhili는 R10의 가장 좋은 Stage2-Actionable이다.
   $6B contract, +8.5%, KOSPI -1.4%로 contract size와 price validation이 같이 닫혔다.

2. Czech nuclear EPC는 Stage2_promote_candidate다.
   Doosan +48%, KEPCO E&C +41%의 sector rerating은 강하지만 final contract와 legal appeal 4B가 있다.

3. Seoul housing supply / reconstruction policy는 Stage2 no-price다.
   Seoul home price +0.76%, 400k+ supply, LTV 40%, reconstruction streamlining은 좋지만 builder price/pre-sale conversion이 없다.

4. Real-estate PF restructuring은 R10 핵심 4B다.
   delinquency 2.70%, 1T→5T syndicated loan, 40.6T support는 relief이지 Green이 아니다.

5. Samsung C&T value-up은 failed_rerating이다.
   activist proposal이 실패하자 shares almost -10%; undervaluation만으로는 Stage3가 안 된다.

6. Highway construction collapse는 sector/project hard 4C다.
   사망자와 중상자가 발생했고, construction safety thesis가 깨졌지만 listed pure-play price anchor는 없다.

7. Builder liquidity/rate relief는 Stage2 relief다.
   금리 기대와 유동성 지원은 PF rollover, 분양 cash, 부실 프로젝트 정리 전까지 Green이 아니다.
```

한 문장으로 압축하면:

> **R10 Loop 17에서 배운 핵심은 “수주·재건축·정책·유동성 headline”이 아니라, EPC margin, final contract, permits, pre-sales, PF rollover, board action, safety clearance가 닫혀야 Stage3로 올릴 수 있다는 것이다. Samsung E&A처럼 계약금액과 주가가 동시에 닫히면 Stage2-Actionable이지만, preferred bidder·정책지원·PF지원·value-up 기대만으로 Green을 주면 false positive가 난다.**

다음 순서는 **R11 Loop 17 — 정책·지정학·재난·이벤트**다.

[1]: https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4?utm_source=chatgpt.com "Samsung E&A Shares Rise on $6 Billion Saudi Contract Win"
[2]: https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/?utm_source=chatgpt.com "South Korea's winning bid for Czech nuclear power project"
[3]: https://www.reuters.com/markets/asia/home-prices-seoul-rise-fastest-pace-more-than-4-years-2024-08-16/?utm_source=chatgpt.com "Home prices in Seoul rise at fastest pace in more than 4 years"
[4]: https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/?utm_source=chatgpt.com "South Korea prepares financial support for small businesses, builders"
[5]: https://www.ft.com/content/647fe2ef-9b01-4ab9-a93b-15b18f474563?utm_source=chatgpt.com "Samsung quashes activist proposals backed by Norway's oil fund"
[6]: https://www.reuters.com/world/asia-pacific/three-people-dead-five-hurt-south-korea-highway-construction-site-yonhap-says-2025-02-25/?utm_source=chatgpt.com "At least three dead in South Korea highway construction project collapse"
