순서상 이번은 **R11 Loop 16 — 정책·지정학·재난·이벤트 trigger-level price validation 라운드**다.

이번 R11은 “정책 수혜”, “방산 수출”, “원전 수주”, “재난 복구”, “정치 리스크”를 한 번에 섞으면 안 된다. R11의 가격은 **정책 방향 → 실제 법/계약/예산 → 기업별 매출·마진 → 규제/소송/정치 리스크 → 시장 신뢰** 순서로 움직였다.

```text
round = R11 Loop 16
round_id = round_247
large_sector = POLICY_GEOPOLITICS_DISASTER_EVENT
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R12 Loop 16
```

이번 라운드도 KRX/Naver/Yahoo/Stooq 수정주가 일봉 OHLC 30D/90D/180D/1Y/2Y window는 안정적으로 확보하지 못했다. 그래서 full MFE/MAE는 만들지 않고 `price_data_unavailable_after_deep_search`로 분리한다. 대신 Reuters/FT/WSJ/AP/MarketWatch가 보도한 **reported event return, event price, contract value, court/rule/fine/policy trigger, disaster damage data**를 trigger anchor로 사용한다.

---

# 1. 이번 라운드 대섹터

```text
R11 = 정책·지정학·재난·이벤트
```

R11의 core gate는 아래다.

```text
방산 / 지정학:
war-risk → export order → backlog → production capacity → delivery → margin → dilution / localization risk

원전 / 에너지안보:
preferred bidder → final contract → legal challenge → financing → EPC share → fuel/service attach → margin

시장제도 / 밸류업:
policy pledge → law passed → board duty / buyback / dividend / foreign capital inflow → valuation rerating

정치 리스크:
political shock → KRW / KOSPI / ETF drawdown → policy continuity → credit-rating / foreign outflow risk

재난:
wildfire / flood / industrial disaster → special disaster zone → reconstruction spending → insurance / supply disruption → local demand

공매도 / 시장감시:
ban / lift / monitoring system → liquidity / foreign access → illegal short-selling penalty → market trust

정책형 이벤트:
headline rally → legal implementation → budget / contract / revenue → execution
```

---

# 2. 대상 canonical archetype

```text
GEOPOLITICAL_DEFENSE_EXPORT_STAGE2_ACTIONABLE
MISSILE_DEFENSE_COMBAT_VALIDATION_STAGE3_YELLOW
NUCLEAR_EXPORT_POLICY_STAGE2_WITH_LEGAL_4B
POLITICAL_CRISIS_MARKET_HARD_4C
COMMERCIAL_ACT_VALUEUP_STAGE2_POLICY
FOREIGN_STRATEGIC_CAPITAL_POLICY_STAGE2_ACTIONABLE
SHORT_SELLING_MARKET_INTEGRITY_STAGE2_4B
NATURAL_DISASTER_RECONSTRUCTION_4C_RELIEF
```

---

# 3. deep sub-archetype

```text
Hanwha Aerospace / European rearmament:
- Romania K9/K10 $1B order.
- Hanwha shares +5% to record high.
- Order backlog rose from 5.1T won at end-2021 to around 30T won by Mar 2024.
- More than 50% global howitzer export share.
- Later share sale / dilution 4B: Hanwha Aerospace announced 1.3T won new shares and broader 3.6T won equity raise; shares dropped 13%.

LIG Nex1 / missile defense:
- Iraq M-SAM II / Cheongung II order 3.71T won / $2.8B.
- LIG shares +3.6%, KOSPI +0.9%.
- Saudi Arabia $3.2B deal already won.
- FT later reported LIG shares nearly +47% since Iran war began, Cheongung-II combat validation with reported 96% success rate.
- Stage2 to Stage3-Yellow candidate if export backlog converts to margin and production scale.

Czech nuclear / KHNP:
- KHNP selected as preferred bidder for two Dukovany reactors.
- Each unit estimated 200B Czech crowns / $8.65B.
- South Korea’s first large overseas nuclear order since 2009.
- Doosan Enerbility +48% over three months, KEPCO Plant S&E +14%, KEPCO E&C +41%.
- Later Czech court halted final contract signing after EDF complaint.
- Stage2 nuclear export + legal 4B.

Martial law political shock:
- Yoon declared martial law Dec 3, 2024, reversed after parliament rejected.
- KOSPI down nearly 2%, won near two-year low.
- South Korea ETFs cut losses after reversal, but political uncertainty remained.
- Hard political 4C for market risk, not company-specific structural entry.

Commercial Act / Value-Up:
- Parliament passed revised Commercial Act expanding directors’ fiduciary duty to minority shareholders.
- KOSPI +1.34% to 3,116.27.
- Korea Discount reform Stage2.
- Green requires actual board behavior, buybacks, dividends, tender-offer fairness.

Samsung SDS / KKR:
- KKR to buy $820M Samsung SDS convertible bonds.
- Samsung SDS shares +20.8% intraday, +19.4% morning vs KOSPI +3.0%.
- KKR to advise on M&A, capital allocation, AI expansion.
- Foreign strategic capital + governance reform Stage2-Actionable, but CB dilution/AI execution gate.

Short-selling / market integrity:
- Market-wide short-selling ban imposed since Nov 2023 after illegal naked short-selling findings.
- Ban lifted in Mar 2025 after monitoring system.
- July 2025: one-strike-out policy; severe violations get fines up to 100% of short-sale orders, business suspension, trading restrictions.
- Stage2 market-integrity policy; no clean stock-specific price anchor.

2025 South Korea wildfires:
- At least 26 deaths in Uiseong disaster context, about 48,000 hectares burned, around 4,000 structures destroyed.
- Several regions designated disaster zones.
- Disaster hard 4C for exposed local assets/tourism/insurance; reconstruction relief is Stage2 but stock-specific price anchor unavailable.
```

---

# 4. 선정 case 요약

| bucket                  | case                                     | 핵심 판정                                                                                                     |
| ----------------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Stage2-Actionable       | Hanwha Aerospace / Romania K9            | $1B order, shares +5% record high, backlog expansion                                                      |
| Stage3-Yellow candidate | LIG Nex1 / Iraq + Iran combat validation | Iraq $2.8B, shares +3.6%, later Iran-war combat validation +47% context                                   |
| Stage2 + 4B             | KHNP / Czech nuclear export              | nuclear export win, Doosan +48% three-month context, later Czech court/EDF 4B                             |
| hard 4C                 | Martial law political shock              | KOSPI nearly -2%, won two-year-low zone, market credibility shock                                         |
| Stage2 policy           | Commercial Act / Value-Up                | KOSPI +1.34%, board duty to minority shareholders                                                         |
| Stage2-Actionable       | Samsung SDS / KKR strategic capital      | $820M CB, Samsung SDS +20.8%, AI/capital allocation advisory                                              |
| Stage2 + 4B             | Short-selling / market integrity         | ban lift + one-strike penalties; trust positive but liquidity/foreign-flow mixed                          |
| disaster 4C + relief    | 2025 wildfires                           | deadliest/widest wildfire disaster context, disaster-zone/reconstruction relief but no stock price anchor |

---

# 5. Case별 trigger grid

## Case A — Hanwha Aerospace / Romania K9 export, European rearmament

```text
symbol = 012450
case_type = Stage2-Actionable defense export
archetype = GEOPOLITICAL_DEFENSE_EXPORT_STAGE2_ACTIONABLE
```

| trigger |                    type | date       | 당시 공개 evidence                                                                  | 가격 anchor                 | outcome            |
| ------- | ----------------------: | ---------- | ------------------------------------------------------------------------------- | ------------------------- | ------------------ |
| T0      |               awareness | 2022~2024  | Russia-Ukraine war drives European rearmament and Korean defense export demand  | no entry                  |                    |
| T1      |         Stage2 evidence | 2024-07-09 | Hanwha wins $1B Romania order for 54 K9 howitzers, ammunition, 36 K10 vehicles  | shares +5% to record high | excellent          |
| T2      |              validation | 2024-07-09 | defense backlog rose from 5.1T won end-2021 to ~30T won by Mar 2024             | same                      | backlog validation |
| T3      | Stage3-Yellow candidate | 2024~2025  | export backlog scale and global howitzer share >50% support structural rerating | no full OHLC              |                    |
| T4      |                4B-watch | 2025-04    | new-share issuance / rights offering dilution for overseas expansion            | shares -13% in FT report  | 4B                 |
| T5      |            Stage3-Green | N/A        | production margin, delivery cash conversion, dilution absorption unavailable    | no Green                  |                    |

Hanwha Aerospace는 R11 방산 수출에서 가장 깨끗한 Stage2-Actionable case다. Romania K9/K10 order는 약 $1B 규모였고, 54대 K9 self-propelled howitzers, ammunition, 36대 K10 resupply vehicles를 포함했다. 발표 후 Hanwha shares는 장초반 +5% 이상 올라 record high를 찍었다. Reuters는 Hanwha의 defense backlog가 2021년 말 5.1T won에서 2024년 3월 약 30T won으로 늘었고, Hanwha가 global howitzer export market의 50% 이상을 차지한다고 설명했다. 다만 2025년 대규모 equity raise 이후 주가가 -13% 반응했다는 FT 보도는 **growth capex/dilution 4B**를 붙여야 한다는 신호다. ([Reuters][1])

```json
{
  "case_id": "r11_loop16_hanwha_aerospace_romania_defense_export",
  "symbol": "012450",
  "best_trigger": "T1/T4",
  "best_trigger_type": "Stage2-Actionable_defense_export_with_dilution_4B",
  "trigger_date": "2024-07-09",
  "contract_value_usd_bn": 1.0,
  "items": [
    "54_K9_self_propelled_howitzers",
    "ammunition",
    "36_K10_resupply_vehicles"
  ],
  "event_return_pct": ">5",
  "event_price_context": "record_high",
  "defense_backlog_end_2021_krw_trn": 5.1,
  "defense_backlog_mar_2024_krw_trn": 30,
  "global_howitzer_export_share_pct": ">50",
  "dilution_4b_trigger": "2025_share_sale",
  "dilution_event_return_pct": -13,
  "stage3_gate_missing": [
    "delivery_schedule_execution",
    "export_margin",
    "working_capital",
    "production_capacity",
    "dilution_absorption",
    "full_OHLC_MFE_MAE"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_defense_export_with_4B_dilution"
}
```

---

## Case B — LIG Nex1 / Iraq M-SAM II and Iran-war combat validation

```text
symbol = 079550
case_type = Stage2 export → Stage3-Yellow candidate
archetype = MISSILE_DEFENSE_COMBAT_VALIDATION_STAGE3_YELLOW
```

| trigger |                    type | date       | 당시 공개 evidence                                                                                | 가격 anchor              | outcome           |
| ------- | ----------------------: | ---------- | --------------------------------------------------------------------------------------------- | ---------------------- | ----------------- |
| T0      |         Stage2 evidence | 2024-09-20 | LIG Nex1 wins Iraq M-SAM II order 3.71T won / $2.8B                                           | LIG +3.6%, KOSPI +0.9% | good              |
| T1      |              validation | 2024-09-20 | Iraq becomes 4th Cheongung-II operator after Korea, UAE, Saudi Arabia                         | same                   | export validation |
| T2      | Stage3-Yellow candidate | 2026-03-11 | Iran war lifts missile-defense demand; FT reports LIG shares nearly +47% since conflict began | +47% context           | combat validation |
| T3      |                4B-watch | 2026       | production scale, delivery time, export finance, customer concentration, war-event premium    | no full OHLC           | 4B                |
| T4      |            Stage3-Green | N/A        | margin, delivery cash conversion, sustained orderbook unavailable                             | no Green               |                   |

LIG Nex1은 R11에서 Stage2를 Yellow 후보로 올려야 하는 case다. 2024년 Iraq M-SAM II export order는 3.71T won, $2.8B 규모였고, 발표 직후 LIG shares는 +3.6%, KOSPI는 +0.9%였다. 이후 FT는 Iran war 이후 Cheongung-II의 combat validation과 missile-defense demand가 부각되며 LIG shares가 전쟁 시작 이후 거의 +47% 올랐다고 보도했다. 즉 단순 “계약”이 아니라 **수출 operator 확장 + 실전 수요 검증 + 주가 반응**이 연결됐다. 다만 Green은 생산능력·납기·마진·반복수주가 확인돼야 한다. ([Reuters][2])

```json
{
  "case_id": "r11_loop16_lig_nex1_iraq_msam_iran_validation",
  "symbol": "079550",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_export_to_Stage3-Yellow_candidate",
  "iraq_contract_date": "2024-09-20",
  "iraq_contract_value_krw_trn": 3.71,
  "iraq_contract_value_usd_bn": 2.8,
  "event_return_pct": 3.6,
  "kospi_same_context_pct": 0.9,
  "market_relative_return_pp": 2.7,
  "prior_saudi_contract_value_usd_bn": 3.2,
  "operator_count_after_iraq": 4,
  "iran_war_validation_date": "2026-03-11",
  "iran_war_share_return_context_pct": 47,
  "cheongung_reported_success_rate_pct": 96,
  "stage3_gate_missing": [
    "delivery_capacity",
    "export_margin",
    "repeat_middle_east_orders",
    "production_ramp",
    "working_capital",
    "full_OHLC_MFE_MAE"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage3_Yellow_candidate_missile_defense_export"
}
```

---

## Case C — KHNP / Czech nuclear export and EDF legal challenge

```text
symbols = 034020 / 052690 / 051600 / 015760
case_type = Stage2 nuclear export + legal 4B
archetype = NUCLEAR_EXPORT_POLICY_STAGE2_WITH_LEGAL_4B
```

| trigger |            type | date       | 당시 공개 evidence                                                                                | 가격 anchor                                                       | outcome    |
| ------- | --------------: | ---------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ---------- |
| T0      |       awareness | 2024H1     | Czech nuclear tender expectations drive nuclear-related shares                                | Doosan +48% in 3 months before/around win                       |            |
| T1      | Stage2 evidence | 2024-07-17 | KHNP selected preferred bidder for two Dukovany reactors                                      | Doosan +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% over 3 months | Stage2     |
| T2      |      validation | 2024-07-17 | each unit estimated 200B Czech crowns / $8.65B; first large overseas nuclear order since 2009 | same                                                            | validation |
| T3      |        4B legal | 2025-05-06 | Czech court blocks signing after EDF complaint                                                | direct KRX price unavailable                                    | 4B         |
| T4      |   Stage3-Yellow | N/A        | final contract, Korean EPC/fuel/service share, litigation resolution not confirmed            | no Yellow                                                       |            |

Czech nuclear export는 R11의 대표 Stage2 policy/geopolitics case다. KHNP가 Czech Dukovany two-reactor project의 preferred bidder로 선정됐고, 이는 2009년 UAE Barakah 이후 한국의 첫 대형 해외 원전 수주였다. Reuters는 기대감 속에서 Doosan Enerbility가 3개월간 +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% 올랐다고 보도했다. 하지만 2025년 Czech court가 EDF complaint를 이유로 최종 계약 signing을 막으면서 legal 4B가 발생했다. 그래서 이 case는 “nuclear export Stage2”이지 final Green이 아니다. ([Reuters][3])

```json
{
  "case_id": "r11_loop16_khnp_czech_nuclear_export",
  "symbols": "034020/052690/051600/015760",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_nuclear_export_with_legal_4B",
  "preferred_bidder_date": "2024-07-17",
  "reactor_count": 2,
  "unit_cost_czk_bn": 200,
  "unit_cost_usd_bn": 8.65,
  "first_large_overseas_order_since": 2009,
  "doosan_3m_return_context_pct": 48,
  "kepco_plant_service_3m_return_context_pct": 14,
  "kepco_ec_3m_return_context_pct": 41,
  "legal_4b_date": "2025-05-06",
  "legal_4b_event": "Czech_court_blocks_contract_signing_after_EDF_complaint",
  "stage3_gate_missing": [
    "final_contract_signing",
    "EDF_legal_resolution",
    "Korean_supplier_workshare",
    "project_financing",
    "margin",
    "full_OHLC_MFE_MAE"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "nuclear_export_stage2_with_legal_4B"
}
```

---

## Case D — 2024 martial-law political shock

```text
symbols = KOSPI / EWY / KRW / broad_market
case_type = hard political 4C
archetype = POLITICAL_CRISIS_MARKET_HARD_4C
```

| trigger |     type | date          | 당시 공개 evidence                                                           | 가격 anchor                               | outcome           |
| ------- | -------: | ------------- | ------------------------------------------------------------------------ | --------------------------------------- | ----------------- |
| T0      |  hard 4C | 2024-12-03/04 | President Yoon declares martial law, parliament rejects, decree reversed | KOSPI nearly -2%, won near two-year low | hard political 4C |
| T1      |   relief | 2024-12-04    | cabinet reverses martial law, ETFs cut losses                            | market still weak                       | relief            |
| T2      | 4B-watch | 2024-12~2025  | impeachment risk, snap-election risk, policy continuity uncertainty      | no company trigger                      |                   |
| T3      |   Stage2 | N/A           | no investible company-specific trigger                                   | no Stage2                               |                   |

Martial-law shock는 R11의 hard political 4C다. Reuters는 KOSPI가 nearly -2% 하락했고, won은 two-year low 근처에 머물렀다고 보도했다. Yoon의 martial law는 의회가 거부한 뒤 철회됐지만, 시장은 단순 “하루짜리 이벤트”로 보지 않았다. 정치 리스크는 기업 EPS가 아니라 **foreign capital confidence, KRW, credit perception, policy continuity**를 흔든다. 이 case는 company-specific Stage2가 아니라 broad-market 4C로 기록해야 한다. ([Reuters][4])

```json
{
  "case_id": "r11_loop16_martial_law_political_shock",
  "symbols": "KOSPI/KRW/EWY/broad_market",
  "best_trigger": "T0/T1",
  "best_trigger_type": "hard_4C_political_crisis_with_relief",
  "trigger_date": "2024-12-03/2024-12-04",
  "kospi_event_return_context_pct": "nearly_-2",
  "krw_context": "near_two_year_low",
  "martial_law_reversed": true,
  "parliament_rejection": true,
  "company_specific_trigger": false,
  "stage3_gate_missing": [
    "political_stability",
    "impeachment_resolution",
    "policy_continuity",
    "foreign_flow_stabilization",
    "KRW_stabilization"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search_broad_market",
  "trigger_outcome_label": "hard_4C_success_political_crisis"
}
```

---

## Case E — Commercial Act / minority-shareholder duty / Value-Up reform

```text
symbols = KOSPI / holding_company_basket / financials / chaebol_basket
case_type = Stage2 policy reform
archetype = COMMERCIAL_ACT_VALUEUP_STAGE2_POLICY
```

| trigger |          type | date       | 당시 공개 evidence                                                                             | 가격 anchor                 | outcome    |
| ------- | ------------: | ---------- | ------------------------------------------------------------------------------------------ | ------------------------- | ---------- |
| T0      |        Stage1 | 2024~2025  | Korea Discount / Value-Up reform debate                                                    | no entry                  |            |
| T1      | Stage2 policy | 2025-07-03 | parliament passes revised Commercial Act expanding fiduciary duty to minority shareholders | KOSPI +1.34% to 3,116.27  | Stage2     |
| T2      |    validation | 2025~2026  | governance reform supports Korea Discount rerating narrative                               | KOSPI 5,000 later context | validation |
| T3      |      4B-watch | 2025~      | actual board behavior, family-control resistance, tender-offer fairness, tax reform        | no company-specific OHLC  |            |
| T4      | Stage3-Yellow | N/A        | company-specific buyback/dividend/governance action required                               | no Yellow                 |            |

Commercial Act revision은 R11 policy reform Stage2다. South Korea’s parliament passed a revised Commercial Act expanding board fiduciary duty to protect minority shareholders, and Reuters reported KOSPI +1.34% to 3,116.27 after the passage. This is not just “sentiment.” It changes the legal frame around the Korea Discount. But it is still Stage2: Green needs company-specific actions such as buyback cancellation, dividend increases, board reform, tender-offer fairness, or minority-holder protection in actual transactions. ([Reuters][5])

```json
{
  "case_id": "r11_loop16_commercial_act_valueup",
  "symbols": "KOSPI/holding_company_basket/financials/chaebol_basket",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_policy_reform_with_execution_4B",
  "trigger_date": "2025-07-03",
  "policy": "Commercial_Act_revision_expanding_director_fiduciary_duty_to_minority_shareholders",
  "kospi_event_return_pct": 1.34,
  "kospi_event_close": 3116.27,
  "reform_target": "Korea_Discount",
  "stage3_gate_missing": [
    "company_specific_board_action",
    "dividend_policy_change",
    "buyback_cancellation",
    "tender_offer_fairness",
    "minority_shareholder_case_law",
    "full_OHLC_MFE_MAE"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search_broad_market",
  "trigger_outcome_label": "Stage2_policy_reform_not_Green"
}
```

---

## Case F — Samsung SDS / KKR strategic capital and Korea reform premium

```text
symbol = 018260
case_type = Stage2-Actionable foreign strategic capital
archetype = FOREIGN_STRATEGIC_CAPITAL_POLICY_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                                        | 가격 anchor                                       | outcome    |
| ------- | ----------------: | ---------- | ------------------------------------------------------------------------------------- | ----------------------------------------------- | ---------- |
| T0      |         awareness | 2025~2026  | corporate reform and foreign capital interest in Korea                                | no entry                                        |            |
| T1      | Stage2-Actionable | 2026-04-15 | KKR to buy $820M newly issued Samsung SDS convertible bonds                           | Samsung SDS +20.8%, +19.4% morning, KOSPI +3.0% | excellent  |
| T2      |        validation | 2026-04-15 | KKR to advise on M&A, capital allocation, AI expansion; Samsung SDS has 6.4T won cash | same                                            | validation |
| T3      |          4B-watch | 2026       | CB dilution, AI execution, stablecoin/physical-AI overextension                       | no full OHLC                                    |            |
| T4      |     Stage3-Yellow | N/A        | actual M&A/AI revenue/capital allocation execution needed                             | no Yellow                                       |            |

Samsung SDS/KKR은 R11에서 “정책 개혁이 외국 전략자본으로 연결되는” clean Stage2-Actionable이다. KKR은 Samsung SDS의 신규 CB $820M를 매입하기로 했고, Samsung SDS shares는 장중 +20.8%, 오전 기준 +19.4%로 KOSPI +3.0%를 크게 웃돌았다. KKR은 6년간 M&A, capital allocation, AI offering expansion에 advisory role을 제공하기로 했고, Samsung SDS는 6.4T won cash와 CB 자금을 global growth/AI infrastructure에 쓰겠다고 했다. 다만 CB는 dilution 4B를 함께 달고 간다. ([Reuters][6])

```json
{
  "case_id": "r11_loop16_samsung_sds_kkr_strategic_capital",
  "symbol": "018260",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_foreign_strategic_capital_with_CB_4B",
  "trigger_date": "2026-04-15",
  "convertible_bond_value_usd_mn": 820,
  "event_intraday_return_pct": 20.8,
  "event_morning_return_pct": 19.4,
  "kospi_same_context_pct": 3.0,
  "market_relative_morning_pp": 16.4,
  "cash_balance_krw_trn": 6.4,
  "kkr_advisory_period_years": 6,
  "strategic_focus": [
    "M&A",
    "capital_allocation",
    "AI_offerings",
    "physical_AI",
    "stablecoins"
  ],
  "4B_overlay": [
    "CB_dilution",
    "AI_execution",
    "M&A_ROIC",
    "policy_theme_overextension"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_foreign_capital_policy_reform"
}
```

---

## Case G — Short-selling ban/lift and one-strike-out market-integrity policy

```text
symbols = KOSPI / KOSDAQ / brokerage_basket / foreign_flow
case_type = Stage2 market-integrity policy + liquidity 4B
archetype = SHORT_SELLING_MARKET_INTEGRITY_STAGE2_4B
```

| trigger |          type | date       | 당시 공개 evidence                                                                                                                                        | 가격 anchor            | outcome |
| ------- | ------------: | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------- |
| T0      | 4B background | 2023-11    | market-wide short-selling ban imposed after illegal naked short-selling findings                                                                      | no direct case price |         |
| T1      | Stage2 system | 2025-03    | ban lifted after monitoring system to detect illegal trades                                                                                           | no clean event price |         |
| T2      | Stage2 policy | 2025-07-09 | regulators announce one-strike-out approach; serious violations face fines up to 100% of short-sale orders, business suspension, trading restrictions | no clean price       |         |
| T3      |      4B-watch | 2025       | liquidity/foreign access vs retail trust/political pressure                                                                                           | no OHLC              |         |
| T4      | Stage3-Yellow | N/A        | foreign flow and market-liquidity improvement not quantified                                                                                          | no Yellow            |         |

Short-selling policy는 R11에서 “시장제도 Stage2”다. Reuters에 따르면 Korea는 2023년 11월 illegal naked short-selling 적발 뒤 market-wide short-selling ban을 부과했고, 2025년 3월 detection system을 준비한 뒤 ban을 해제했다. 이후 2025년 7월 regulators는 Lee Jae Myung 대통령의 one-strike-out 지시에 따라 severe violations에는 short-sale order의 100% fine, business suspension, trading restrictions를 부과하겠다고 밝혔다. 이건 market trust에는 positive지만, liquidity/foreign access와 retail-politics를 같이 봐야 해서 4B가 붙는다. ([Reuters][7])

```json
{
  "case_id": "r11_loop16_short_selling_market_integrity",
  "symbols": "KOSPI/KOSDAQ/brokerage_basket/foreign_flow",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_market_integrity_with_liquidity_4B",
  "ban_start_context": "2023-11",
  "ban_lift_context": "2025-03",
  "one_strike_policy_date": "2025-07-09",
  "fine_for_serious_violation_pct_of_short_sale_orders": 100,
  "penalties": [
    "business_suspension",
    "trading_restrictions",
    "illicit_gain_recovery"
  ],
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "foreign_flow_improvement",
    "market_liquidity_improvement",
    "illegal_short_selling_reduction",
    "retail_trust",
    "MSCI_developed_market_access"
  ],
  "trigger_outcome_label": "Stage2_market_integrity_policy_not_Green"
}
```

---

## Case H — 2025 South Korea wildfires / disaster-zone relief

```text
symbols = insurance / construction_repair / tourism_local_assets / disaster_basket
case_type = disaster hard 4C + relief
archetype = NATURAL_DISASTER_RECONSTRUCTION_4C_RELIEF
```

| trigger |             type | date          | 당시 공개 evidence                                                                | 가격 anchor                | outcome |
| ------- | ---------------: | ------------- | ----------------------------------------------------------------------------- | ------------------------ | ------- |
| T0      | hard disaster 4C | 2025-03-21~30 | massive wildfires across southern/southeastern Korea                          | no stock-specific anchor |         |
| T1      |       validation | 2025-03-30    | at least 26 deaths, about 48,000 hectares burned, ~4,000 structures destroyed | no price                 |         |
| T2      |           relief | 2025-03       | special disaster zones, government mobilization, reconstruction need          | no price                 |         |
| T3      |           Stage2 | N/A           | stock-specific reconstruction beneficiary not identified with price anchor    | no investible Stage2     |         |
| T4      |         4C-watch | 2025~         | insurance loss, tourism/local asset disruption, climate risk                  | no OHLC                  |         |

2025 wildfires는 R11 disaster hard 4C다. Reuters는 Uiseong wildfire가 Korea’s largest wildfire로 확산됐고, at least 26 deaths, around 48,000 hectares burned, about 4,000 structures destroyed를 보도했다. AP도 southern Korea wildfires가 수만 명 evacuation과 구조물 피해를 일으켰다고 전했다. 이건 주식시장 전체의 theme라기보다 **지역자산·관광·보험·재건 수요**를 흔드는 disaster gate다. stock-specific price anchor가 없으므로 `disaster_4C_relief_reference`로 둔다. ([Reuters][8])

```json
{
  "case_id": "r11_loop16_2025_wildfire_disaster_relief",
  "symbols": "insurance/construction_repair/tourism_local_assets/disaster_basket",
  "best_trigger": "T0/T2",
  "best_trigger_type": "hard_4C_disaster_with_relief_reference",
  "trigger_period": "2025-03-21_to_2025-03-30",
  "fatalities_context": "at_least_26",
  "area_burned_hectares_context": 48000,
  "structures_destroyed_context": 4000,
  "evacuation_context": "tens_of_thousands",
  "special_disaster_zone_context": true,
  "direct_stock_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "insurance_loss_estimate",
    "reconstruction_budget_allocation",
    "listed_company_contracts",
    "tourism_recovery",
    "local_asset_damage_quantification"
  ],
  "trigger_outcome_label": "natural_disaster_4C_relief_reference"
}
```

---

# 6. Trigger별 가격경로 검증 요약

| case                       | best trigger |        entry anchor |                                  event MFE/MAE |      market-relative | full MFE/MAE | outcome                 |
| -------------------------- | ------------ | ------------------: | ---------------------------------------------: | -------------------: | ------------ | ----------------------- |
| Hanwha Aerospace / Romania | T1/T4        | record high context |                      +5%+, later dilution -13% |          unavailable | unavailable  | Stage2-Actionable + 4B  |
| LIG Nex1 / Iraq-Iran       | T0/T2        |               event |       +3.6% vs KOSPI +0.9%; later +47% context | +2.7pp first trigger | unavailable  | Yellow candidate        |
| KHNP / Czech nuclear       | T1/T3        |     3-month context | Doosan +48%, KEPCO E&C +41%, later legal block |          unavailable | unavailable  | Stage2 + legal 4B       |
| Martial law                | T0/T1        |        broad market |        KOSPI nearly -2%, KRW near two-year low |         broad market | unavailable  | hard political 4C       |
| Commercial Act             | T1/T3        |        broad market |                       KOSPI +1.34% to 3,116.27 |         broad market | unavailable  | Stage2 policy           |
| Samsung SDS / KKR          | T1/T3        |               event |          +20.8%, +19.4% morning vs KOSPI +3.0% |      +16.4pp morning | unavailable  | Stage2-Actionable       |
| Short-selling policy       | T1/T3        |      no clean price |                                    unavailable |                  N/A | unavailable  | Stage2 market integrity |
| 2025 wildfires             | T0/T2        |      no stock price |                                    unavailable |                  N/A | unavailable  | disaster 4C reference   |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
좋은 Stage2:
- Hanwha Aerospace Romania K9/K10 export.
- LIG Nex1 Iraq M-SAM II export.
- KHNP Czech nuclear preferred-bidder event.
- Commercial Act / Value-Up policy.
- Samsung SDS / KKR foreign strategic capital.
- Short-selling market-integrity policy.

약한 Stage2:
- Short-selling policy has no clean stock-specific event return.
- Wildfire disaster has no listed reconstruction beneficiary with price anchor.
- Nuclear Czech win has strong three-month context, but final contract legal risk remains.
```

## Stage2-Actionable entry 성과

```text
Actionable:
- Hanwha Aerospace: contract + price reaction + backlog.
- LIG Nex1: contract + price reaction + later combat validation.
- Samsung SDS / KKR: foreign strategic capital + +20.8% event reaction.
- Commercial Act broad-market: KOSPI +1.34%, but company-specific action needed.

Actionable 보류:
- KHNP/Czech nuclear: legal 4B after preferred bidder.
- Short-selling reform: market integrity positive, but liquidity/foreign-flow impact unquantified.
- Wildfire disaster: relief/reference, not investible Stage2.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- LIG Nex1 if export orders convert into repeat backlog, production margin and delivery cash flow.
- Hanwha Aerospace if delivery schedule, margin and dilution absorption are confirmed.
- Nuclear basket if Czech final contract is signed and Korean supplier workshare is disclosed.
- Samsung SDS if KKR advisory leads to actual M&A/AI revenue/capital allocation execution.
```

## Stage3-Green

```text
이번 R11 Loop 16에서 확정 Green 없음.

이유:
- 방산은 수주가 강하지만 production/delivery/margin이 필요하다.
- 원전은 preferred bidder 이후 legal challenge가 붙었다.
- 밸류업은 법 통과가 Stage2지만 company-specific action이 필요하다.
- 정치/재난 이벤트는 broad 4C이지 개별 EPS Green이 아니다.
- 공매도 제도는 market trust positive지만 liquidity/foreign-flow effect가 확인되지 않았다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Hanwha Aerospace Romania defense export
- LIG Nex1 Iraq missile export and later Iran-war validation
- Czech nuclear export as Stage2 with legal 4B
- Martial-law political shock as hard 4C
- Commercial Act Value-Up as Stage2 broad-market policy
- Samsung SDS / KKR as foreign-capital Stage2-Actionable

Stage2_promote_candidate:
- Hanwha Aerospace
- LIG Nex1
- Samsung SDS
- nuclear supplier basket after final Czech contract

Stage3-Yellow candidate:
- LIG Nex1
- Hanwha Aerospace
- nuclear basket if legal challenge clears
- Samsung SDS if AI/capital allocation execution appears

evidence_good_but_price_failed_or_unavailable:
- Short-selling market-integrity policy
- wildfires disaster/reconstruction reference
- Czech nuclear after legal challenge due no direct post-court KRX anchor

cyclical_success:
- defense/geopolitical demand, but not purely cyclical; more structural if backlog/margin repeat

event_premium:
- defense rally on Europe/Iran war
- nuclear export preferred-bidder rally
- Samsung SDS KKR strategic-capital premium
- Commercial Act broad policy premium

thesis_break_watch:
- Hanwha dilution
- Czech EDF legal challenge
- martial-law political instability
- short-selling/liquidity backlash
- natural-disaster climate risk

hard_4C_success:
- martial-law political shock
- 2025 wildfire disaster as disaster reference, not stock-specific
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
defense_export_contract_value,+5,"방산은 계약금액과 price reaction이 함께 닫히면 Stage2-Actionable","Hanwha,LIG"
defense_backlog_delivery_visibility,+5,"수주는 delivery/margin/cash conversion이 Green gate","Hanwha,LIG"
combat_validation,+5,"실전 검증은 missile defense 제품의 Yellow 승격 요건","LIG Nex1"
nuclear_final_contract_signing,+5,"preferred bidder만으로 Green 금지, final contract가 필요","KHNP/Doosan/KEPCO E&C"
nuclear_legal_resolution,+5,"EDF 법적 challenge는 4B 핵심","Czech nuclear"
board_fiduciary_reform_execution,+4,"Commercial Act는 company-specific board action 필요","Value-Up basket"
foreign_strategic_capital_execution,+4,"KKR/Samsung SDS는 실제 AI/M&A/capital allocation 실행 필요","Samsung SDS"
market_integrity_enforcement,+4,"short-selling reform은 trust 개선 축","short-selling policy"
political_stability_risk,+5,"martial-law 같은 정치 shock는 broad hard 4C","KOSPI/KRW"
disaster_reconstruction_budget,+4,"재난은 피해액보다 reconstruction budget/contract가 Stage2","wildfire basket"
```

## 내릴 축

```csv
axis,delta,reason,cases
defense_order_without_capacity,-5,"수주만 있고 생산능력/납기 없으면 Green 금지","Hanwha,LIG"
defense_growth_with_dilution_ignored,-5,"방산 성장도 equity raise dilution 있으면 4B","Hanwha"
preferred_bidder_without_contract,-5,"preferred bidder는 final contract 전까지 Stage2","Czech nuclear"
policy_reform_without_company_action,-5,"법 통과만으로 Green 금지","Commercial Act"
foreign_capital_without_ROIC,-4,"전략자본 유입도 ROIC/M&A 실행 전에는 Stage2","Samsung SDS"
market_rule_without_flow_data,-4,"공매도 제도개편은 외국인 flow/liquidity 데이터 필요","short-selling"
political_crisis_treated_as_one_day_event,-5,"정치 crisis를 하루짜리 shock로 보면 false positive","martial law"
disaster_relief_without_listed_contract,-4,"재난복구 headline만으로 listed beneficiary 만들지 않기","wildfire"
```

---

# 10. Stage2-Actionable 승격 조건

R11 Loop 16 shadow rule:

```text
R11에서 Stage2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. contract/order value가 명확하다.
2. event return이 +5% 이상이다.
3. market-relative return이 +5pp 이상이다.
4. policy/legal trigger가 실제 law, contract, budget, fine, enforcement로 닫혔다.
5. defense/nuclear는 delivery, workshare, margin, final contract 중 하나 이상이 확인된다.
6. governance/value-up은 company-specific capital allocation or board action으로 연결된다.
7. political/disaster/security 4C overlay가 없다.
```

적용:

```text
Hanwha Aerospace:
1,2 충족. backlog도 강함. 하지만 dilution 4B → Stage2-Actionable + 4B.

LIG Nex1:
1 충족, initial event return은 +5% 미만이지만 later combat-validation +47% context가 강함 → Yellow candidate.

Czech nuclear:
1 일부, policy trigger 강함. 하지만 final contract/legal resolution 없음 → Stage2 + 4B.

Samsung SDS:
1,2,3,4 충족 → Stage2-Actionable. CB dilution and AI execution 4B.

Commercial Act:
4 충족, broad market reaction 있음. company-specific action 전에는 Stage2.

Wildfire:
4C/disaster reference. listed contract 없으므로 Actionable 금지.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
- Stage2-Actionable 이후 EPS/OP/FCF 경로 변화 가능성이 높아짐.
- 하지만 delivery, legal resolution, final budget, company-specific execution 중 하나가 남은 상태.
```

Yellow 후보:

```text
LIG Nex1:
Iraq/Saudi/Middle East demand + Iran combat validation. Production and margin confirmation needed.

Hanwha Aerospace:
Europe orders and backlog are strong. Dilution absorption and delivery/margin needed.

Czech nuclear basket:
final contract signing and Korean workshare disclosure needed.

Samsung SDS:
KKR advisory must convert into AI revenue, M&A discipline, capital allocation.

Commercial Act beneficiaries:
actual buyback cancellation, dividend policy, minority-shareholder friendly transactions needed.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- defense export backlog converts to deliveries and margin.
- nuclear preferred bidder converts to final contract and supplier workshare.
- policy reform converts to company-specific capital allocation.
- foreign strategic capital converts to ROIC and earnings.
- market-integrity reform improves foreign flow and liquidity without retail backlash.
- disaster relief converts into listed-company contracts.
- political risk is resolved and foreign-capital confidence returns.
- full-window MFE/MAE is favorable.
```

이번 R11 Loop 16에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + delivery/final-contract/legal/company-execution gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- defense export rally followed by equity dilution.
- nuclear preferred-bidder rally before final contract.
- policy reform rally before company-specific governance action.
- foreign strategic capital rally before ROIC.
- short-selling reform improves trust but may reduce liquidity/foreign participation.
- political shock hits KRW/KOSPI/ETF confidence.
- disaster damage lacks listed-company reconstruction contract.
```

적용:

```text
Hanwha:
export rally strong, but dilution 4B.

LIG:
combat validation strong, but war-event premium and production scaling 4B.

Czech nuclear:
preferred bidder strong, but EDF/Czech court 4B.

Commercial Act:
policy positive, but company execution 4B.

Samsung SDS:
KKR positive, but CB dilution and AI execution 4B.

Martial law:
hard political 4C.

Wildfire:
disaster 4C, not an automatic reconstruction stock trigger.
```

---

# 14. 4C hard gate 조건

```text
R11 4C:
- martial law / constitutional crisis
- final contract blocked by court or rival bidder challenge
- defense contract cancelled or delivery blocked
- large equity dilution after geopolitics-driven rally
- disaster causing deaths and large asset destruction
- market-integrity scandal or illegal trading undermining trust
- sanctions/export-control shock
```

이번 R11 Loop 16 hard 4C:

```text
martial_law_political_shock = hard_4C_success
wildfire_disaster = disaster_4C_reference
```

Strong 4C-watch:

```text
- Czech nuclear EDF legal challenge
- Hanwha Aerospace dilution
- short-selling / market-integrity enforcement risk
- defense war-event premium reversal
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R11 production 설계 원칙:

```text
1. policy headline과 actual law/contract/budget을 분리한다.
2. defense order와 delivery/margin/capacity를 분리한다.
3. nuclear preferred bidder와 final contract/legal clearance를 분리한다.
4. Value-Up law와 company-specific capital allocation을 분리한다.
5. disaster relief와 listed-company reconstruction contract를 분리한다.
6. political shock는 broad hard 4C로 별도 처리한다.
7. market-integrity policy는 trust와 liquidity를 동시에 본다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_247.md 요약

```md
# R11 Loop 16. Policy / Geopolitics / Disaster / Event Trigger-level Price Validation

이번 라운드는 R11 Loop 16 trigger-level validation 라운드다.

핵심 결론:
- Hanwha Aerospace / Romania K9 export is Stage2-Actionable. Hanwha won a $1B Romania order for 54 K9 self-propelled howitzers, ammunition and 36 K10 vehicles; shares rose more than 5% to a record high. Defense backlog rose from 5.1T won at end-2021 to around 30T won by Mar 2024. But later share-sale dilution created 4B.
- LIG Nex1 / Iraq M-SAM II is Stage3-Yellow candidate. LIG won a 3.71T won / $2.8B Iraq order, shares +3.6% vs KOSPI +0.9%, and later Iran-war combat validation pushed LIG shares almost 47% higher since the conflict began. Green requires delivery, margin and production ramp.
- Czech nuclear export is Stage2 with legal 4B. KHNP was selected preferred bidder for two Dukovany reactors, and Doosan Enerbility rose 48% over three months, KEPCO Plant S&E +14%, KEPCO E&C +41%. But a Czech court later blocked final signing after EDF complaint.
- Martial-law political shock is hard 4C. Yoon’s surprise martial-law declaration and reversal drove KOSPI nearly -2% and won near a two-year low. This is broad political-risk hard gate, not company-specific Stage2.
- Commercial Act / Value-Up is Stage2 policy reform. Revised Commercial Act expanded fiduciary duty to minority shareholders; KOSPI +1.34% to 3,116.27. Green requires company-specific board action, buyback cancellation, dividend policy and fair transactions.
- Samsung SDS / KKR is Stage2-Actionable foreign strategic capital. KKR bought $820M CBs; Samsung SDS +20.8% intraday and +19.4% morning vs KOSPI +3.0%. CB dilution and AI execution are 4B.
- Short-selling / market-integrity policy is Stage2 with liquidity 4B. Ban lifted after detection system; one-strike-out policy can impose fines of 100% of short-sale orders, business suspensions and trading restrictions.
- 2025 wildfires are disaster hard 4C reference. At least 26 deaths, around 48,000 hectares burned and about 4,000 structures destroyed. Reconstruction relief is Stage2 only if listed-company contracts appear.

Main calibration:
- Raise defense_export_contract_value, defense_backlog_delivery_visibility, combat_validation, nuclear_final_contract_signing, nuclear_legal_resolution, board_fiduciary_reform_execution, foreign_strategic_capital_execution, market_integrity_enforcement, political_stability_risk, disaster_reconstruction_budget.
- Lower defense_order_without_capacity, defense_growth_with_dilution_ignored, preferred_bidder_without_contract, policy_reform_without_company_action, foreign_capital_without_ROIC, market_rule_without_flow_data, political_crisis_treated_as_one_day_event, disaster_relief_without_listed_contract.
```

## docs/checkpoints/checkpoint_28a_round247_r11_loop16.md 요약

```md
# Checkpoint 28A Round 247 R11 Loop 16 Trigger-level Calibration

## 반영 내용
- R11 Loop 16 trigger-level validation을 수행했다.
- Hanwha Aerospace Romania defense export, LIG Nex1 Iraq/Iran missile-defense validation, KHNP Czech nuclear export, martial-law political shock, Commercial Act Value-Up reform, Samsung SDS/KKR, short-selling market-integrity policy, 2025 wildfires를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / FT / WSJ / AP / MarketWatch의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- Policy headline must be separated from actual law, contract, budget and enforcement.
- Defense export orders need delivery, production capacity and margin before Green.
- Nuclear preferred bidder status is Stage2 until final contract and legal challenge resolution.
- Value-Up law is Stage2 until company-specific board/capital-allocation action.
- Foreign strategic capital is Stage2-Actionable only if ROIC and execution follow.
- Political crisis is broad hard 4C.
- Natural disaster relief is not investible Stage2 unless listed-company contracts are identified.
```

## data/e2r_case_library/cases_r11_loop16_round247.jsonl 초안

```jsonl
{"case_id":"r11_loop16_hanwha_aerospace_romania_defense_export","symbol":"012450","company_name":"Hanwha Aerospace","case_type":"Stage2_Actionable_defense_export_with_dilution_4B","primary_archetype":"GEOPOLITICAL_DEFENSE_EXPORT_STAGE2_ACTIONABLE","best_trigger":"T1/T4","stage_candidate":"Stage2-Actionable + 4B-watch","price_validation":{"trigger_date":"2024-07-09","contract_value_usd_bn":1.0,"event_return_pct":">5","event_price_context":"record_high","defense_backlog_end_2021_krw_trn":5.1,"defense_backlog_mar_2024_krw_trn":30,"global_howitzer_export_share_pct":">50","dilution_event_return_pct":-13,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_with_dilution_4B","notes":"Defense export contract and backlog are strong, but equity dilution must be overlaid."}
{"case_id":"r11_loop16_lig_nex1_iraq_msam_iran_validation","symbol":"079550","company_name":"LIG Nex1","case_type":"Stage3_Yellow_candidate_missile_defense_export","primary_archetype":"MISSILE_DEFENSE_COMBAT_VALIDATION_STAGE3_YELLOW","best_trigger":"T0/T2","stage_candidate":"Stage3-Yellow_candidate","price_validation":{"iraq_contract_date":"2024-09-20","iraq_contract_value_krw_trn":3.71,"iraq_contract_value_usd_bn":2.8,"event_return_pct":3.6,"kospi_same_context_pct":0.9,"market_relative_return_pp":2.7,"prior_saudi_contract_value_usd_bn":3.2,"operator_count_after_iraq":4,"iran_war_share_return_context_pct":47,"cheongung_reported_success_rate_pct":96,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage3_Yellow_candidate","notes":"Export order plus combat validation lifts this above simple Stage2, but production and margin are still Green gates."}
{"case_id":"r11_loop16_khnp_czech_nuclear_export","symbol":"034020/052690/051600/015760","company_name":"Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E / KEPCO read-through","case_type":"Stage2_nuclear_export_with_legal_4B","primary_archetype":"NUCLEAR_EXPORT_POLICY_STAGE2_WITH_LEGAL_4B","best_trigger":"T1/T3","stage_candidate":"Stage2 + 4B-watch","price_validation":{"preferred_bidder_date":"2024-07-17","reactor_count":2,"unit_cost_czk_bn":200,"unit_cost_usd_bn":8.65,"first_large_overseas_order_since":2009,"doosan_3m_return_context_pct":48,"kepco_plant_service_3m_return_context_pct":14,"kepco_ec_3m_return_context_pct":41,"legal_4b_date":"2025-05-06","legal_4b_event":"Czech_court_blocks_contract_signing_after_EDF_complaint","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"nuclear_export_stage2_with_legal_4B","notes":"Preferred bidder status drove nuclear names, but final contract and legal resolution are required."}
{"case_id":"r11_loop16_martial_law_political_shock","symbol":"KOSPI/KRW/EWY/broad_market","company_name":"South Korea broad market","case_type":"hard_4C_political_crisis","primary_archetype":"POLITICAL_CRISIS_MARKET_HARD_4C","best_trigger":"T0/T1","stage_candidate":"4C","price_validation":{"trigger_date":"2024-12-03/2024-12-04","kospi_event_return_context_pct":"nearly_-2","krw_context":"near_two_year_low","martial_law_reversed":true,"parliament_rejection":true,"company_specific_trigger":false,"full_ohlc_status":"price_data_unavailable_after_deep_search_broad_market"},"score_price_alignment":"hard_4C_success","notes":"Political crisis hit KOSPI/KRW confidence; this is broad market 4C, not stock-specific Stage2."}
{"case_id":"r11_loop16_commercial_act_valueup","symbol":"KOSPI/holding_company_basket/financials/chaebol_basket","company_name":"Korea Value-Up policy basket","case_type":"Stage2_policy_reform","primary_archetype":"COMMERCIAL_ACT_VALUEUP_STAGE2_POLICY","best_trigger":"T1/T3","stage_candidate":"Stage2","price_validation":{"trigger_date":"2025-07-03","policy":"Commercial_Act_revision_expanding_director_fiduciary_duty_to_minority_shareholders","kospi_event_return_pct":1.34,"kospi_event_close":3116.27,"reform_target":"Korea_Discount","full_ohlc_status":"price_data_unavailable_after_deep_search_broad_market"},"score_price_alignment":"Stage2_policy_reform_not_Green","notes":"Legal reform is real, but Green requires company-specific governance and capital-allocation action."}
{"case_id":"r11_loop16_samsung_sds_kkr_strategic_capital","symbol":"018260","company_name":"Samsung SDS","case_type":"Stage2_Actionable_foreign_strategic_capital_with_CB_4B","primary_archetype":"FOREIGN_STRATEGIC_CAPITAL_POLICY_STAGE2_ACTIONABLE","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable + 4B-watch","price_validation":{"trigger_date":"2026-04-15","convertible_bond_value_usd_mn":820,"event_intraday_return_pct":20.8,"event_morning_return_pct":19.4,"kospi_same_context_pct":3.0,"market_relative_morning_pp":16.4,"cash_balance_krw_trn":6.4,"kkr_advisory_period_years":6,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_foreign_capital","notes":"Foreign strategic capital and AI/capital-allocation advisory triggered strong rerating, but CB dilution and execution are 4B."}
{"case_id":"r11_loop16_short_selling_market_integrity","symbol":"KOSPI/KOSDAQ/brokerage_basket/foreign_flow","company_name":"Korea short-selling market-integrity policy","case_type":"Stage2_market_integrity_with_liquidity_4B","primary_archetype":"SHORT_SELLING_MARKET_INTEGRITY_STAGE2_4B","best_trigger":"T1/T3","stage_candidate":"Stage2 + 4B-watch","price_validation":{"ban_start_context":"2023-11","ban_lift_context":"2025-03","one_strike_policy_date":"2025-07-09","fine_for_serious_violation_pct_of_short_sale_orders":100,"penalties":["business_suspension","trading_restrictions","illicit_gain_recovery"],"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_policy_not_Green","notes":"Market integrity is positive, but liquidity and foreign-flow impact remain unquantified."}
{"case_id":"r11_loop16_2025_wildfire_disaster_relief","symbol":"insurance/construction_repair/tourism_local_assets/disaster_basket","company_name":"2025 South Korea wildfire disaster reference","case_type":"hard_4C_disaster_with_relief_reference","primary_archetype":"NATURAL_DISASTER_RECONSTRUCTION_4C_RELIEF","best_trigger":"T0/T2","stage_candidate":"disaster_4C_reference","price_validation":{"trigger_period":"2025-03-21_to_2025-03-30","fatalities_context":"at_least_26","area_burned_hectares_context":48000,"structures_destroyed_context":4000,"evacuation_context":"tens_of_thousands","special_disaster_zone_context":true,"direct_stock_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"disaster_4C_reference_not_investible_stage2","notes":"Disaster relief is not a listed-company Stage2 unless reconstruction contracts or insurance losses are identified."}
```

## data/e2r_trigger_calibration/triggers_r11_loop16_round247.jsonl 초안

```jsonl
{"trigger_id":"r11l16_hanwha_romania_T1","case_id":"r11_loop16_hanwha_aerospace_romania_defense_export","trigger_type":"Stage2-Actionable_defense_export","trigger_date":"2024-07-09","evidence_available":"Hanwha Aerospace won $1B Romania order for 54 K9 howitzers, ammunition and 36 K10 vehicles; shares rose more than 5% to a record high; backlog around 30T won by Mar 2024","event_return_pct":">5","trigger_outcome_label":"excellent_stage2_actionable_defense_export","promote_to":"Stage2-Actionable"}
{"trigger_id":"r11l16_hanwha_dilution_T4","case_id":"r11_loop16_hanwha_aerospace_romania_defense_export","trigger_type":"4B_dilution_overlay","trigger_date":"2025-04","evidence_available":"Hanwha Aerospace announced large share sale/equity raise for overseas expansion; shares dropped 13% after announcement","event_return_pct":-13,"trigger_outcome_label":"defense_growth_with_dilution_4B","promote_to":"4B-watch"}
{"trigger_id":"r11l16_lig_iraq_T0","case_id":"r11_loop16_lig_nex1_iraq_msam_iran_validation","trigger_type":"Stage2_defense_export","trigger_date":"2024-09-20","evidence_available":"LIG Nex1 won 3.71T won / $2.8B Iraq Cheongung-II order; shares +3.6%, KOSPI +0.9%; Iraq becomes fourth operator after Korea, UAE and Saudi Arabia","event_return_pct":3.6,"trigger_outcome_label":"good_stage2_defense_export","promote_to":"Stage2"}
{"trigger_id":"r11l16_lig_iran_validation_T2","case_id":"r11_loop16_lig_nex1_iraq_msam_iran_validation","trigger_type":"Stage3-Yellow_candidate_combat_validation","trigger_date":"2026-03-11","evidence_available":"FT reported Cheongung-II combat validation and LIG shares nearly +47% since Iran war began; reported 96% success rate against Iranian missile and drone attacks","event_return_pct":47,"trigger_outcome_label":"Stage3_Yellow_candidate_combat_validation","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r11l16_czech_nuclear_T1","case_id":"r11_loop16_khnp_czech_nuclear_export","trigger_type":"Stage2_nuclear_export","trigger_date":"2024-07-17","evidence_available":"KHNP selected preferred bidder for two Dukovany reactors; each unit estimated 200B Czech crowns / $8.65B; Doosan +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% over three months","event_return_pct":"3m_context_Doosan_+48_KEPCO_EC_+41","trigger_outcome_label":"Stage2_nuclear_export","promote_to":"Stage2"}
{"trigger_id":"r11l16_czech_nuclear_legal_T3","case_id":"r11_loop16_khnp_czech_nuclear_export","trigger_type":"4B_legal_challenge","trigger_date":"2025-05-06","evidence_available":"Czech court blocked final contract signing after EDF complaint; deal cannot be signed until court reviews the case","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"nuclear_export_legal_4B","promote_to":"4B-watch"}
{"trigger_id":"r11l16_martial_law_T0","case_id":"r11_loop16_martial_law_political_shock","trigger_type":"hard_4C_political_crisis","trigger_date":"2024-12-03/2024-12-04","evidence_available":"President Yoon declared martial law, parliament rejected it, decree reversed; KOSPI nearly -2%, won near two-year low","event_return_pct":"KOSPI_nearly_-2","trigger_outcome_label":"hard_4C_success_political_crisis","promote_to":"4C"}
{"trigger_id":"r11l16_commercial_act_T1","case_id":"r11_loop16_commercial_act_valueup","trigger_type":"Stage2_policy_reform","trigger_date":"2025-07-03","evidence_available":"Parliament passed revised Commercial Act expanding fiduciary duty to minority shareholders; KOSPI +1.34% to 3,116.27","event_return_pct":1.34,"trigger_outcome_label":"Stage2_policy_reform_not_Green","promote_to":"Stage2"}
{"trigger_id":"r11l16_samsung_sds_kkr_T1","case_id":"r11_loop16_samsung_sds_kkr_strategic_capital","trigger_type":"Stage2-Actionable_foreign_strategic_capital","trigger_date":"2026-04-15","evidence_available":"KKR to buy $820M Samsung SDS CBs; Samsung SDS shares +20.8% intraday and +19.4% morning vs KOSPI +3.0%; KKR to advise on M&A, capital allocation and AI expansion","event_return_pct":20.8,"trigger_outcome_label":"excellent_stage2_actionable_foreign_strategic_capital","promote_to":"Stage2-Actionable"}
{"trigger_id":"r11l16_short_selling_integrity_T1","case_id":"r11_loop16_short_selling_market_integrity","trigger_type":"Stage2_market_integrity_policy","trigger_date":"2025-03/2025-07-09","evidence_available":"Korea lifted short-selling ban after detection system; regulators later announced one-strike-out policy, fines up to 100% of short-sale orders, business suspensions and trading restrictions","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_market_integrity_with_liquidity_4B","promote_to":"Stage2+4B"}
{"trigger_id":"r11l16_wildfire_disaster_T0","case_id":"r11_loop16_2025_wildfire_disaster_relief","trigger_type":"hard_4C_disaster_reference","trigger_date":"2025-03-21_to_2025-03-30","evidence_available":"South Korea wildfires caused at least 26 deaths, burned around 48,000 hectares and destroyed about 4,000 structures; special disaster relief context but no listed-company price anchor","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"natural_disaster_4C_relief_reference","promote_to":"4C_reference"}
```

## data/sector_taxonomy/score_weight_profiles_round247_r11_loop16_v1.csv 초안

```csv
archetype,defense_export_contract_value,defense_backlog_delivery_visibility,combat_validation,nuclear_final_contract_signing,nuclear_legal_resolution,board_fiduciary_reform_execution,foreign_strategic_capital_execution,market_integrity_enforcement,political_stability_risk,disaster_reconstruction_budget,defense_order_without_capacity_penalty,defense_growth_with_dilution_ignored_penalty,preferred_bidder_without_contract_penalty,policy_reform_without_company_action_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
GEOPOLITICAL_DEFENSE_EXPORT_STAGE2_ACTIONABLE,+5,+5,+2,+0,+0,+0,+0,+0,+2,+0,-5,-5,-1,-1,defense export order+price reaction,delivery/margin/dilution pending,delivery+margin+capacity,Hanwha Aerospace.
MISSILE_DEFENSE_COMBAT_VALIDATION_STAGE3_YELLOW,+5,+5,+5,+0,+0,+0,+0,+0,+2,+0,-5,-2,-1,-1,export order+combat validation,production/margin pending,repeat orders+delivery+margin,LIG Nex1.
NUCLEAR_EXPORT_POLICY_STAGE2_WITH_LEGAL_4B,+2,+2,+0,+5,+5,+0,+0,+0,+2,+0,-1,-1,-5,-1,preferred bidder and nuclear-policy win,final contract/legal resolution missing,final contract+workshare+margin,Czech nuclear basket.
POLITICAL_CRISIS_MARKET_HARD_4C,+0,+0,+0,+0,+0,+0,+0,+1,+5,+0,-1,-1,-1,-1,martial-law shock,political stability missing,N/A,KOSPI/KRW.
COMMERCIAL_ACT_VALUEUP_STAGE2_POLICY,+0,+0,+0,+0,+0,+5,+2,+2,+1,+0,-1,-1,-1,-5,law passed with market reaction,company action missing,buyback/dividend/board action,Value-Up.
FOREIGN_STRATEGIC_CAPITAL_POLICY_STAGE2_ACTIONABLE,+0,+0,+0,+0,+0,+3,+5,+1,+1,+0,-1,-3,-1,-2,KKR/Samsung SDS strategic capital,ROIC/AI execution/CB dilution pending,AI revenue+M&A ROIC+capital allocation,Samsung SDS.
SHORT_SELLING_MARKET_INTEGRITY_STAGE2_4B,+0,+0,+0,+0,+0,+1,+0,+5,+2,+0,-1,-1,-1,-2,market integrity enforcement,flow/liquidity data missing,foreign flow+liquidity+trust,short-selling policy.
NATURAL_DISASTER_RECONSTRUCTION_4C_RELIEF,+0,+0,+0,+0,+0,+0,+0,+1,+2,+5,-1,-1,-1,-1,wildfire disaster relief,listed contracts missing,reconstruction contracts+insurance loss clarity,wildfire reference.
```

---

# 이번 R11 Loop 16 결론

```text
1. Hanwha Aerospace / Romania K9 export는 R11의 강한 Stage2-Actionable이다.
   $1B order, +5% record high, backlog expansion이 닫혔다. 단, dilution 4B를 반드시 붙인다.

2. LIG Nex1 / Iraq + Iran validation은 Stage3-Yellow 후보다.
   $2.8B Iraq order, +3.6%, 이후 combat validation +47% context가 붙었다. 생산능력·마진·납기 전에는 Green이 아니다.

3. Czech nuclear export는 Stage2 + legal 4B다.
   preferred bidder와 nuclear basket rally는 강하지만 EDF/Czech court legal challenge가 final contract를 막았다.

4. Martial-law shock는 hard political 4C다.
   KOSPI nearly -2%, KRW two-year-low zone은 하루짜리 noise가 아니라 market confidence shock다.

5. Commercial Act / Value-Up은 Stage2 policy reform이다.
   KOSPI +1.34%로 반응했지만, company-specific board/capital allocation action이 필요하다.

6. Samsung SDS / KKR은 Stage2-Actionable이다.
   $820M CB, +20.8% price reaction은 강하지만 CB dilution and AI execution 4B가 있다.

7. Short-selling market-integrity policy는 Stage2 + liquidity 4B다.
   enforcement는 trust에 좋지만 foreign flow/liquidity impact가 닫혀야 한다.

8. 2025 wildfire는 disaster 4C reference다.
   재건 수요는 가능하지만 listed-company contract 없이는 투자 trigger로 만들면 안 된다.
```

한 문장으로 압축하면:

> **R11 Loop 16에서 배운 핵심은 “정책·방산·원전·재난 headline”이 아니라, defense delivery/margin, nuclear final contract, legal resolution, company-specific Value-Up action, foreign-capital ROIC, market-integrity flow data, political stability, disaster reconstruction contract가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 수주 headline, preferred bidder, 법 통과, 외국자본 유입, 재난복구 narrative만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-wins-1-bln-order-romania-k9-howitzers-2024-07-09/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace wins $1 bln order from Romania for self-propelled howitzers"
[2]: https://www.reuters.com/business/aerospace-defense/south-koreas-lig-nex1-wins-28-bln-deal-with-iraq-export-missile-systems-2024-09-19/?utm_source=chatgpt.com "South Korea's LIG Nex1 wins $2.8 bln Iraq deal to export missile systems"
[3]: https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/?utm_source=chatgpt.com "South Korea's winning bid for Czech nuclear power project"
[4]: https://www.reuters.com/world/asia-pacific/south-korea-president-yoon-declares-martial-law-2024-12-03/?utm_source=chatgpt.com "South Korea's President Yoon reverses martial law after lawmakers defy him"
[5]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-assembly-passes-commerce-bill-expanding-duty-boards-shareholders-2025-07-03/?utm_source=chatgpt.com "South Korea assembly passes commerce bill expanding duty of boards to shareholders"
[6]: https://www.reuters.com/world/asia-pacific/kkr-buy-820-million-samsung-sds-convertible-bonds-shares-jump-20-2026-04-15/?utm_source=chatgpt.com "KKR to buy $820 million of Samsung SDS convertible bonds, shares jump 20%"
[7]: https://www.reuters.com/business/finance/south-korean-court-clears-hsbc-charges-violating-short-selling-rules-yonhap-2025-02-11/?utm_source=chatgpt.com "South Korean court clears HSBC of violating short-selling rules"
[8]: https://www.reuters.com/world/asia-pacific/south-korea-police-say-rite-family-grave-led-deadly-wildfire-2025-03-30/?utm_source=chatgpt.com "South Korea police say rite at family grave led to deadly wildfire"
