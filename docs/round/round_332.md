순서상 이번은 **R11 Loop 17 — 정책·지정학·재난·이벤트 trigger-level price validation 라운드**다.

```text
round = R11 Loop 17
round_id = round_260
large_sector = POLICY_GEOPOLITICS_DISASTER_EVENT
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R12 Loop 17
```

이번 R11은 특정 업종보다 “이벤트가 국장 전체의 risk premium을 어떻게 흔드는가”를 보는 라운드다. KRX/Naver/Yahoo/Stooq 기준 수정주가 OHLC window는 안정적으로 확보하지 못했기 때문에 MFE/MAE/peak/drawdown은 만들지 않는다. 대신 Reuters/FT/AP/MarketWatch/Barron’s의 **reported event return, index move, 종목 당일 반응, 정책금액, liquidity amount, damage/fatality data**를 trigger anchor로 쓴다.

---

# 1. 이번 라운드 대섹터

```text
R11 = 정책·지정학·재난·이벤트
```

R11의 core gate는 아래다.

```text
정책 개혁:
법안 통과 → investor trust → foreign flow → valuation rerating → tax/regulatory reversal 4B

세제:
capital-gains threshold / transaction tax / dividend tax → retail sentiment → KOSPI beta → policy reversal

정치 리스크:
martial law / impeachment / constitutional crisis → won, KOSPI, ETF, liquidity injection → relief or prolonged discount

지정학·수출통제:
U.S. China chip controls / tariff / export license → Samsung·SK Hynix·battery·auto impact → license relief / supply-chain reset

산업정책:
semiconductor / auto / defense support package → subsidy / low-cost loan / infra → capex conversion → crowding-out or fiscal 4B

방산 지정학:
NATO/Russia/Ukraine threat → export order → backlog → dilution/capex → execution / geopolitical dependence 4B

노동·국가경제 이벤트:
strike threat at national-champion company → supply disruption → government arbitration → wage-cost reset / rival spillover

재난:
wildfire / flood / aviation / cyber / industrial accident → human loss / asset damage → insurance / rebuilding / safety regulation → hard 4C 가능
```

---

# 2. 대상 canonical archetype

```text
COMMERCIAL_ACT_VALUEUP_STAGE2_ACTIONABLE
TAX_POLICY_RELIEF_STAGE2_WITH_TAX_4B
MARTIAL_LAW_POLITICAL_RISK_4B
AI_WINDFALL_TAX_POLICY_OVERHANG_4B
CHIP_EXPORT_CONTROL_4B_WITH_POLICY_RELIEF
SEMICONDUCTOR_TARIFF_SUPPORT_STAGE2_RELIEF
DEFENSE_GEOPOLITICAL_EXPORT_STAGE2_WITH_DILUTION_4B
NATIONAL_CHAMPION_LABOR_STRIKE_4B
WILDFIRE_DISASTER_HARD_4C_NO_PUBLIC_PRICE
```

---

# 3. deep sub-archetype

```text
Commercial Act / Korea Discount:
- parliament passed revised Commercial Act expanding board duties to minority shareholders.
- KOSPI +1.34% to 3,116.27.
- Stage2-Actionable governance reform, but Green requires corporate action.

Capital-gains tax reversal:
- proposed lowering of large-shareholder threshold from 5B won to 1B won hurt sentiment.
- Aug 1 tax proposal shock: KOSPI -3.9%.
- Lee later said threshold cut was unnecessary; KOSPI +0.6% / FT says +0.9% record close.
- Stage2 policy relief.

Martial law crisis:
- Yoon’s sudden martial law declaration caused won plunge and market stress.
- government/BOK pledged unlimited liquidity and up to 10T won market stabilization fund.
- KOSPI -1.44%, Samsung -0.93%, won around 1,444 then 1,410.
- political-risk 4B; not stock-specific hard 4C because liquidity response worked.

AI windfall tax comment:
- policy secretary floated idea of national dividend from AI excess profits.
- KOSPI fell as much as 5%, closed -2.3%.
- presidential office later said personal view.
- 4B policy overhang for AI-heavy KOSPI, not hard 4C yet.

U.S. chip waiver revocation:
- U.S. removed Samsung/SK Hynix validated-end-user waivers for Chinese fabs.
- SK Hynix nearly -5%, Samsung >-2%.
- Commerce said licenses likely for existing fabs but not expansion/upgrades.
- geopolitical export-control 4B.

Semiconductor support package:
- Korea expanded semiconductor support to 33T won, up 26% from 26T won.
- includes loans, subsidies, R&D/manufacturing support, underground power infra for Yongin/Pyeongtaek.
- also 3T won auto support.
- Stage2 policy relief, but no direct event price anchor.

Defense export / Hanwha:
- Hanwha Aerospace won $1B Romania K9 order; shares +5% to record high.
- later 3.6T won / $2.5B share sale for overseas expansion caused shares -13%.
- Stage2 geopolitical export, 4B dilution.

Samsung strike:
- Samsung union strike threat sent shares -9.3%.
- government considered emergency arbitration; single-day halt estimated up to 1T won direct losses, prolonged disruption up to 100T won.
- national-champion labor 4B, not hard 4C unless strike disrupts production materially.

Wildfires:
- March 2025 southeastern wildfires caused at least 16 then 26 deaths in Reuters follow-up.
- around 48,000 hectares burned and thousands of buildings destroyed.
- disaster hard 4C at social/asset level; no public-stock price anchor.
```

---

# 4. 선정 case 요약

| bucket                                 | case                                               | 핵심 판정                                                                |
| -------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------- |
| structural_success / Stage2-Actionable | **Commercial Act / Korea Discount reform**         | KOSPI +1.34%, board duty to shareholders                             |
| Stage2 policy relief                   | **Capital-gains tax reversal**                     | tax shock KOSPI -3.9%, reversal KOSPI +0.6~0.9%                      |
| 4B political risk                      | **Martial law / liquidity intervention**           | KOSPI -1.44%, won shock, unlimited liquidity / 10T won stabilization |
| 4B policy overhang                     | **AI windfall tax comment**                        | KOSPI intraday -5%, close -2.3%                                      |
| 4B geopolitical export control         | **U.S. chip-waiver revocation**                    | SK Hynix -5%, Samsung -2%                                            |
| Stage2 policy relief                   | **33T won semiconductor support**                  | 33T won support, 3T won auto support, no event price                 |
| Stage2 + 4B                            | **Hanwha defense export / dilution**               | $1B Romania order +5%, later 3.6T won share sale -13%                |
| 4B labor event                         | **Samsung strike threat / government arbitration** | Samsung -9.3%, potential 1T won/day direct loss                      |
| hard 4C no-price                       | **2025 South Korea wildfires**                     | at least 26 deaths, 48,000ha burned, no listed price anchor          |

---

# 5. 각 case별 trigger grid

## Case A — Commercial Act / Korea Discount governance reform

```text
symbols = KOSPI / value-up basket / financials / holdcos
case_type = Stage2-Actionable market governance reform
archetype = COMMERCIAL_ACT_VALUEUP_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                                        | 가격 anchor              | outcome |
| ------- | ----------------: | ---------- | ------------------------------------------------------------------------------------- | ---------------------- | ------- |
| T0      |            Stage1 | 2024~2025  | Korea Discount, value-up reform, shareholder-rights debate                            | no entry               |         |
| T1      | Stage2-Actionable | 2025-07-03 | revised Commercial Act passed; board fiduciary duty expanded to minority shareholders | KOSPI +1.34%, 3,116.27 |         |
| T2      |        validation | 2025-07-03 | bipartisan compromise; President Lee supports Korea Discount removal                  | same                   |         |
| T3      |          4B-watch | 2025~      | enforcement, chaebol resistance, tax-policy inconsistency                             | 4B                     |         |
| T4      |     Stage3-Yellow | N/A        | actual buybacks/dividends/governance actions needed                                   | 보류                     |         |

Commercial Act reform은 R11의 가장 좋은 policy Stage2-Actionable이다. 단순 구호가 아니라 법안 통과라는 공개 evidence가 있고, KOSPI가 +1.34% 오른 가격반응도 있었다. 다만 이건 “시장 전체 재평가의 문”이 열린 것이지, 개별 종목 Green은 아니다. 실제 Stage3-Yellow는 board action, 자사주 소각, 배당, minority protection이 회사별로 닫힐 때만 준다. ([Reuters][1])

```json
{
  "case_id": "r11_loop17_commercial_act_valueup",
  "symbols": "KOSPI/valueup_basket/financials/holdcos",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_market_governance_reform",
  "trigger_date": "2025-07-03",
  "kospi_event_return_pct": 1.34,
  "kospi_close_points": 3116.27,
  "policy": "revised_Commercial_Act_expands_board_fiduciary_duty_to_shareholders",
  "4B_overlay": [
    "enforcement_uncertainty",
    "chaebol_resistance",
    "tax_policy_inconsistency",
    "company_specific_action_missing"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_policy_reform"
}
```

---

## Case B — Capital-gains tax proposal shock and reversal

```text
symbols = KOSPI / retail-sensitive basket / financials / brokers
case_type = Stage2 relief with tax-policy 4B
archetype = TAX_POLICY_RELIEF_STAGE2_WITH_TAX_4B
```

| trigger |          type | date       | 당시 공개 evidence                                                                                 | 가격 anchor                      | outcome |
| ------- | ------------: | ---------- | ---------------------------------------------------------------------------------------------- | ------------------------------ | ------- |
| T0      |  4B tax shock | 2025-08-01 | tax proposals: large-shareholder threshold 5B→1B won, corporate/dividend/transaction tax hikes | KOSPI -3.9%                    |         |
| T1      | Stage2 relief | 2025-09-11 | President Lee says lowering threshold unnecessary; leaves decision to parliament               | KOSPI +0.6% Reuters / +0.9% FT |         |
| T2      |    validation | 2025-09-11 | both major parties support unchanged threshold; market hits record high per FT                 | same                           |         |
| T3      |      4B-watch | 2025~      | transaction tax still planned 0.15%→0.2%; future tax uncertainty                               | 4B                             |         |
| T4      | Stage3-Yellow | N/A        | stable tax policy + retail/foreign flows needed                                                | 보류                             |         |

세제 case는 R11에서 매우 중요하다. 2025년 8월 tax package는 KOSPI를 -3.9% 떨어뜨렸고, 이후 Lee 대통령이 large-shareholder threshold 인하를 추진하지 않겠다고 하자 KOSPI는 다시 +0.6~0.9% 상승했다. 즉 세제는 국장 전체의 risk premium을 여닫는 스위치다. 하지만 transaction tax 인상 가능성이 남아 있어 relief Stage2이지 Green은 아니다. ([마켓워치][2])

```json
{
  "case_id": "r11_loop17_capital_gains_tax_reversal",
  "symbols": "KOSPI/retail_sensitive_basket/brokers/financials",
  "best_trigger": "T0/T3",
  "best_trigger_type": "tax_policy_4B_then_Stage2_relief",
  "tax_shock_date": "2025-08-01",
  "tax_shock_kospi_return_pct": -3.9,
  "relief_date": "2025-09-11",
  "relief_kospi_return_reuters_pct": 0.6,
  "relief_kospi_return_ft_pct": 0.9,
  "large_shareholder_threshold_original_krw_bn": 5,
  "large_shareholder_threshold_proposed_krw_bn": 1,
  "transaction_tax_before_pct": 0.15,
  "transaction_tax_proposed_pct": 0.2,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_policy_relief_with_tax_4B"
}
```

---

## Case C — Martial law crisis / emergency liquidity intervention

```text
symbols = KOSPI / won / EWY / banks / brokers / exporters
case_type = political-risk 4B with liquidity relief
archetype = MARTIAL_LAW_POLITICAL_RISK_4B
```

| trigger |                 type | date          | 당시 공개 evidence                                                                              | 가격 anchor               | outcome |
| ------- | -------------------: | ------------- | ------------------------------------------------------------------------------------------- | ----------------------- | ------- |
| T0      | hard political shock | 2024-12-03/04 | Yoon declares martial law; National Assembly votes to lift it                               | won plunges, KOSPI down |         |
| T1      |      4B price impact | 2024-12-04    | KOSPI -1.44%, Samsung -0.93%, won around 1,444 then 1,410                                   | political risk          |         |
| T2      |               relief | 2024-12-04    | finance ministry/BOK pledge unlimited liquidity; up to 10T won stabilization fund available | relief                  |         |
| T3      |             4B-watch | 2024~2025     | impeachment, constitutional crisis, policy paralysis                                        | 4B                      |         |
| T4      |        Stage3-Yellow | N/A           | political stabilization, FX normalization, foreign-flow return needed                       | 보류                      |         |

Martial law는 R11의 textbook political-risk 4B다. 가격반응은 KOSPI -1.44%, Samsung -0.93%, won shock로 나타났고, 정부와 BOK가 unlimited liquidity와 stabilization fund를 언급하면서 systemic crash를 막았다. 이건 hard political shock지만, 시장 기능이 닫히거나 상장기업 thesis가 영구적으로 깨진 것은 아니므로 hard 4C가 아니라 **political 4B + liquidity relief**로 분류한다. ([Reuters][3])

```json
{
  "case_id": "r11_loop17_martial_law_liquidity_intervention",
  "symbols": "KOSPI/KRW/EWY/banks/brokers/exporters",
  "best_trigger": "T0/T3",
  "best_trigger_type": "political_risk_4B_with_liquidity_relief",
  "trigger_date": "2024-12-04",
  "kospi_event_return_pct": -1.44,
  "samsung_electronics_event_return_pct": -0.93,
  "won_initial_shock_usdkrw_context": 1444,
  "won_later_context_usdkrw": 1410,
  "market_stabilization_fund_krw_trn": 10,
  "liquidity_response": "unlimited_liquidity_and_special_repo_operations",
  "4B_overlay": [
    "impeachment_risk",
    "policy_paralysis",
    "foreign_investor_confidence",
    "FX_volatility",
    "Korea_discount_repricing"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "political_risk_4B_not_hard_4C"
}
```

---

## Case D — AI windfall tax / national-dividend policy overhang

```text
symbols = KOSPI / Samsung Electronics / SK Hynix / AI memory basket
case_type = policy-overhang 4B
archetype = AI_WINDFALL_TAX_POLICY_OVERHANG_4B
```

| trigger |            type | date          | 당시 공개 evidence                                                        | 가격 anchor                       | outcome |
| ------- | --------------: | ------------- | --------------------------------------------------------------------- | ------------------------------- | ------- |
| T0      | 4B policy shock | 2026-05-11/12 | senior policy official floats AI excess-profit national dividend idea | KOSPI intraday -5%, close -2.3% |         |
| T1      |          relief | 2026-05-12    | presidential office says it was personal opinion                      | partial relief                  |         |
| T2      |        4B-watch | 2026          | AI-heavy market concentration, tax risk, populist policy overhang     | 4B                              |         |
| T3      |         hard 4C | N/A           | actual law/tax not confirmed                                          | hard 4C not confirmed           |         |

AI windfall tax comment는 R11의 “정책 한마디가 megacycle 주도주를 때리는” case다. KOSPI는 장중 -5%까지 빠졌고 종가는 -2.3%였다. 대통령실이 개인 의견이라고 진화했지만, AI memory supercycle이 national dividend/tax rhetoric의 대상이 될 수 있다는 점이 4B로 남았다. 실제 법안이 아니므로 hard 4C는 아니다. ([Barron's][4])

```json
{
  "case_id": "r11_loop17_ai_windfall_tax_policy_overhang",
  "symbols": "KOSPI/005930/000660/AI_memory_basket",
  "best_trigger": "T0/T2",
  "best_trigger_type": "4B_AI_windfall_tax_policy_overhang",
  "trigger_date": "2026-05-12",
  "kospi_intraday_drop_pct": -5.0,
  "kospi_close_return_pct": -2.3,
  "policy_context": "AI_excess_profit_national_dividend_comment",
  "relief_context": "presidential_office_called_comment_personal_opinion",
  "4B_overlay": [
    "policy_populism",
    "AI_profit_tax_risk",
    "index_concentration",
    "foreign_flow_sensitivity",
    "KOSPI_AI_overheat"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "AI_policy_overhang_4B_not_hard_4C"
}
```

---

## Case E — U.S. chip export-waiver revocation for China fabs

```text
symbols = 005930 / 000660 / semiconductor_supply_chain
case_type = geopolitical export-control 4B
archetype = CHIP_EXPORT_CONTROL_4B_WITH_POLICY_RELIEF
```

| trigger |              type | date         | 당시 공개 evidence                                                                    | 가격 anchor                         | outcome |
| ------- | ----------------: | ------------ | --------------------------------------------------------------------------------- | --------------------------------- | ------- |
| T0      | 4B export control | 2025-09-01   | U.S. removes VEU waivers for Samsung/SK Hynix China fabs                          | SK Hynix nearly -5%, Samsung >-2% |         |
| T1      |        validation | 2025-09-01   | existing-fab license applications likely allowed; expansion/upgrades not intended | 4B but not hard 4C                |         |
| T2      |            relief | 2026 context | annual license regime can keep operations but adds review risk                    | partial relief                    |         |
| T3      |     Stage3-Yellow | N/A          | license stability, capex rerouting, China fab strategy clarity needed             | 보류                                |         |

Chip-waiver revocation은 R11 지정학 4B다. U.S.가 Samsung과 SK Hynix의 China fab에 대한 validated end-user waiver를 제거하면서 SK Hynix는 거의 -5%, Samsung은 2% 이상 하락했다. 다만 existing fabs 운영 license는 허용될 가능성이 있었고 expansion/upgrades가 문제였기 때문에 hard 4C가 아니라 supply-chain 4B다. ([Financial Times][5])

```json
{
  "case_id": "r11_loop17_us_chip_waiver_revocation",
  "symbols": "005930/000660/semiconductor_supply_chain",
  "best_trigger": "T0/T2",
  "best_trigger_type": "4B_geopolitical_chip_export_control",
  "trigger_date": "2025-09-01",
  "sk_hynix_event_return_pct": "nearly_-5",
  "samsung_event_return_pct": "more_than_-2",
  "policy": "VEU_waiver_removed_for_China_fabs",
  "relief_context": "licenses_expected_for_existing_fab_operations_but_not_expansion_or_upgrade",
  "4B_overlay": [
    "China_fab_upgrade_limit",
    "US_license_dependency",
    "geopolitical_supply_chain",
    "capex_rerouting",
    "China_memory_competition"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "chip_export_control_4B_not_hard_4C"
}
```

---

## Case F — 33T won semiconductor support / tariff-policy relief

```text
symbols = 005930 / 000660 / 042700 / 141080 / chip_equipment_materials_basket
case_type = Stage2 policy relief no direct price
archetype = SEMICONDUCTOR_TARIFF_SUPPORT_STAGE2_RELIEF
```

| trigger |                  type | date       | 당시 공개 evidence                                                             | 가격 anchor              | outcome |
| ------- | --------------------: | ---------- | -------------------------------------------------------------------------- | ---------------------- | ------- |
| T0      | Stage2 policy support | 2025-04-15 | Korea expands semiconductor support to 33T won, +26% from prior 26T won    | no direct stock anchor |         |
| T1      |            validation | 2025-04-15 | loans, subsidies, R&D/manufacturing aid, power infra for Yongin/Pyeongtaek | no price               |         |
| T2      |           auto relief | 2025-04-15 | separate 3T won auto support program for tariff-hit auto sector            | no price               |         |
| T3      |              4B-watch | 2025~      | subsidy execution, fiscal crowding, capex timing, U.S. tariff path         | 4B                     |         |
| T4      |         Stage3-Yellow | N/A        | company-level capex/order conversion needed                                | 보류                     |         |

33T won semiconductor support는 policy Stage2 relief다. 산업정책 숫자가 크고, low-cost loans, subsidies, R&D/manufacturing support, power infrastructure가 명확하다. 그러나 source set에서 event-window stock reaction은 확인하지 못했으므로 Actionable이 아니라 Stage2 relief다. ([AP News][6])

```json
{
  "case_id": "r11_loop17_semiconductor_support_33t",
  "symbols": "005930/000660/chip_equipment_materials_basket",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage2_policy_relief_no_direct_price",
  "trigger_date": "2025-04-15",
  "semiconductor_support_krw_trn": 33,
  "prior_support_krw_trn": 26,
  "support_increase_pct": 26,
  "auto_support_krw_trn": 3,
  "policy_items": [
    "low_cost_loans",
    "subsidies",
    "R&D_support",
    "manufacturing_equipment_support",
    "Yongin_Pyeongtaek_power_infrastructure"
  ],
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_policy_relief_no_price"
}
```

---

## Case G — Hanwha Aerospace defense export and dilution risk

```text
symbol = 012450
case_type = geopolitical defense export Stage2 + dilution 4B
archetype = DEFENSE_GEOPOLITICAL_EXPORT_STAGE2_WITH_DILUTION_4B
```

| trigger |          type | date       | 당시 공개 evidence                                                                        | 가격 anchor                 | outcome |
| ------- | ------------: | ---------- | ------------------------------------------------------------------------------------- | ------------------------- | ------- |
| T0      | Stage2 export | 2024-07-09 | Hanwha wins $1B Romania K9 howitzer order                                             | shares +5% to record high |         |
| T1      |    validation | 2024-07-09 | order includes 54 K9, ammunition, 36 K10 vehicles; backlog around 30T won by Mar 2024 | Stage2                    |         |
| T2      |   4B dilution | 2025-04    | 3.6T won / $2.5B share sale for overseas expansion                                    | shares -13%               |         |
| T3      | Stage3-Yellow | N/A        | order margin, delivery, dilution absorption, cash-flow funding needed                 | 보류                        |         |

Hanwha Aerospace는 R11 지정학 수혜와 자본조달 4B가 같이 있는 case다. Romania K9 $1B order에서는 shares가 +5% to record high였고, backlog는 2021년 말 5.1T won에서 2024년 3월 약 30T won으로 확대된 상태였다. 하지만 이후 해외공장·파트너 지분 확보를 위한 3.6T won / $2.5B share sale 발표 후 shares는 -13% 하락했다. 즉 “방산 geopolitics = 무조건 Green”이 아니라, 수주와 희석/자금조달을 동시에 점수화해야 한다. ([Reuters][7])

```json
{
  "case_id": "r11_loop17_hanwha_defense_export_dilution",
  "symbol": "012450",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_defense_export_with_dilution_4B",
  "export_trigger_date": "2024-07-09",
  "romania_order_value_usd_bn": 1.0,
  "k9_units": 54,
  "k10_units": 36,
  "export_event_return_pct": 5,
  "order_backlog_mar_2024_krw_trn": 30,
  "share_sale_value_krw_trn": 3.6,
  "share_sale_value_usd_bn": 2.5,
  "dilution_event_return_pct": -13,
  "4B_overlay": [
    "share_dilution",
    "overseas_factory_capex",
    "delivery_execution",
    "geopolitical_budget_dependency",
    "cash_flow_vs_equity_financing"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "defense_export_stage2_with_dilution_4B"
}
```

---

## Case H — Samsung Electronics strike threat / government arbitration risk

```text
symbol = 005930
case_type = national-champion labor 4B
archetype = NATIONAL_CHAMPION_LABOR_STRIKE_4B
```

| trigger |              type | date          | 당시 공개 evidence                                                                                   | 가격 anchor             | outcome |
| ------- | ----------------: | ------------- | ------------------------------------------------------------------------------------------------ | --------------------- | ------- |
| T0      |    4B labor shock | 2026-05-15    | Samsung union sticks to 18-day strike plan; over 50,000 workers possible                         | Samsung shares -9.3%  |         |
| T1      | government relief | 2026-05-17~19 | government considers emergency arbitration; talks resume                                         | relief                |         |
| T2      |        validation | 2026-05       | government says one-day halt could cause 1T won direct loss; prolonged disruption up to 100T won | 4B                    |         |
| T3      |           hard 4C | N/A           | actual prolonged production halt not confirmed                                                   | hard 4C not confirmed |         |
| T4      |     Stage2 relief | N/A           | strike averted / labor-cost settlement clarity needed                                            | 보류                    |         |

Samsung strike threat는 R11 labor-policy event다. Samsung shares fell -9.3% when the union held to an 18-day strike plan. 정부는 emergency arbitration까지 검토했고, 하루 생산중단 손실이 1T won, 장기 disruption 손실이 100T won까지 갈 수 있다고 경고했다. 아직 장기 생산 차질은 확인되지 않았기 때문에 hard 4C가 아니라 **labor 4B + government relief watch**다. ([Reuters][8])

```json
{
  "case_id": "r11_loop17_samsung_strike_government_arbitration",
  "symbol": "005930",
  "best_trigger": "T0/T3",
  "best_trigger_type": "4B_national_champion_labor_strike",
  "trigger_date": "2026-05-15",
  "event_return_pct": -9.3,
  "potential_strike_duration_days": 18,
  "possible_workers_involved": ">50000",
  "government_tool": "emergency_arbitration_possible",
  "single_day_direct_loss_krw_trn": 1,
  "prolonged_disruption_loss_krw_trn": 100,
  "hard_4C_status": "not_confirmed",
  "4B_overlay": [
    "production_reliability",
    "labor_cost_reset",
    "HBM_supply_chain",
    "rival_spillover_to_SK_Hynix",
    "government_intervention"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "national_champion_labor_4B_not_hard_4C"
}
```

---

## Case I — 2025 South Korea wildfires / disaster hard 4C no public price

```text
symbols = insurers / rebuild basket / forestry / disaster-relief basket
case_type = disaster hard 4C no direct public-stock price
archetype = WILDFIRE_DISASTER_HARD_4C_NO_PUBLIC_PRICE
```

| trigger |                     type | date       | 당시 공개 evidence                                                                     | 가격 anchor               | outcome |
| ------- | -----------------------: | ---------- | ---------------------------------------------------------------------------------- | ----------------------- | ------- |
| T0      |         disaster trigger | 2025-03-25 | southeastern wildfires, at least 16 deaths, disaster zones                         | stock price unavailable |         |
| T1      | hard disaster validation | 2025-03-30 | at least 26 deaths, about 48,000 hectares burned, thousands of buildings destroyed | no listed anchor        |         |
| T2      |                4B/relief | 2025       | evacuation, reconstruction, insurance claims, climate disaster policy              | 4B/4C                   |         |
| T3      |            Stage2 relief | N/A        | rebuilding orders / insurance loss clarity needed                                  | 보류                      |         |

Wildfire case는 R11 재난 hard 4C다. 인명피해와 자산피해가 크지만, 이번 source set에서 국장 상장 종목의 event-window price anchor를 잡지 못했으므로 public-equity hard 4C 숫자는 만들지 않는다. 대신 disaster-level hard 4C로 기록하고, 건설·보험·복구·방재 basket은 별도 Stage2 relief 여부를 이후 확인한다. ([Reuters][9])

```json
{
  "case_id": "r11_loop17_south_korea_wildfire_disaster",
  "symbols": "insurers/rebuild_basket/forestry/disaster_relief_basket",
  "best_trigger": "T0/T2",
  "best_trigger_type": "disaster_hard_4C_no_public_price",
  "trigger_date": "2025-03-25_to_2025-03-30",
  "fatalities_initial_context": 16,
  "fatalities_followup_context": 26,
  "burned_area_hectares_context": 48000,
  "destroyed_structures_context": "thousands_of_buildings",
  "public_stock_price_anchor": "price_data_unavailable_after_deep_search",
  "hard_4C_status": "disaster_level_confirmed_public_stock_not_available",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "wildfire_disaster_hard_4C_no_public_price"
}
```

---

# 6. Trigger별 실제 가격경로 검증 요약

이번 R11 Loop 17은 full OHLC가 없으므로, 아래 표는 **reported event anchor 기준**이다.

| case                           | best trigger |                    event return / price |  market-relative | full MFE/MAE | outcome                         |
| ------------------------------ | -----------: | --------------------------------------: | ---------------: | ------------ | ------------------------------- |
| Commercial Act                 |           T1 |                  KOSPI +1.34%, 3,116.27 |         positive | unavailable  | Stage2-Actionable               |
| Capital-gains tax reversal     |        T0/T1 |         shock -3.9%, reversal +0.6~0.9% | policy-sensitive | unavailable  | Stage2 relief + tax 4B          |
| Martial law                    |        T0/T2 | KOSPI -1.44%, Samsung -0.93%, won shock |         negative | unavailable  | political 4B + liquidity relief |
| AI windfall tax comment        |        T0/T1 |         KOSPI intraday -5%, close -2.3% |         negative | unavailable  | AI policy 4B                    |
| U.S. chip-waiver revocation    |           T0 |       SK Hynix nearly -5%, Samsung >-2% |         negative | unavailable  | geopolitical export-control 4B  |
| 33T won chip support           |           T0 |                  no direct price anchor |              N/A | unavailable  | Stage2 policy relief            |
| Hanwha defense export/dilution |        T0/T2 |               export +5%, dilution -13% |            mixed | unavailable  | Stage2 + dilution 4B            |
| Samsung strike                 |        T0/T2 |                           Samsung -9.3% |         negative | unavailable  | labor 4B                        |
| Wildfires                      |        T0/T2 |                  no listed price anchor |              N/A | unavailable  | disaster hard 4C no-price       |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
가장 좋은 Stage2:
1. Commercial Act reform: 법안 통과 + KOSPI +1.34%.
2. Capital-gains tax reversal: 세제 shock 후 reversal이 index relief를 만들었다.
3. Hanwha Romania order: $1B 방산수주 + shares +5%.
4. Semiconductor 33T support: 산업정책 금액은 크지만 event price anchor 없음.
```

## Stage2-Actionable entry 성과

```text
Stage2-Actionable:
- Commercial Act reform.
- Capital-gains tax reversal relief.
- Hanwha defense export trigger, but dilution 4B 병기.

Stage2 relief:
- 33T won semiconductor support.
- Martial law liquidity response.
- Samsung strike government arbitration if strike is averted.

Actionable 금지:
- AI windfall tax comment.
- U.S. chip-waiver revocation.
- Samsung strike threat before settlement.
- wildfires disaster without listed-price anchor.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Commercial Act: actual company buyback/cancellation/dividend/governance actions.
- Tax reversal: stable tax regime and sustained retail/foreign flows.
- Hanwha defense: delivery/margin/cash-flow funding without additional dilution.
- Semiconductor support: company-level capex/order conversion.
- Samsung strike: strike averted and labor-cost reset contained.
```

## Stage3-Green

```text
이번 R11 Loop 17에서 확정 Green 없음.

이유:
- policy reform은 Stage2지만 company-level execution이 필요하다.
- tax relief는 좋지만 transaction tax and future tax risk가 남아 있다.
- geopolitical chip controls and AI windfall tax are 4B.
- defense exports are strong but dilution/capex risk가 크다.
- Samsung strike and wildfire are negative event risk.
- full OHLC/MFE/MAE가 없다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Commercial Act as Stage2-Actionable policy reform.
- Capital-gains tax reversal as Stage2 relief after tax 4B.
- Martial law as political-risk 4B with liquidity relief.
- AI windfall tax comment as policy-overhang 4B.
- U.S. chip waiver revocation as geopolitical export-control 4B.
- Semiconductor support as Stage2 relief no-price.
- Hanwha export as defense-geopolitical Stage2 plus dilution 4B.
- Samsung strike as labor/supply-chain 4B.
- Wildfire as disaster hard 4C no public price.

false_positive_score:
- Commercial Act를 개별종목 Green으로 바로 올리는 경우.
- tax reversal을 permanent tax clarity로 착각하는 경우.
- chip support를 company earnings로 바로 반영하는 경우.
- Hanwha defense order를 dilution 없이 Green으로 올리는 경우.
- AI windfall tax를 단순 noise로 무시하는 경우.

Stage2_promote_candidate:
- Commercial Act.
- tax reversal.
- Hanwha defense order.
- semiconductor support package.

price_moved_without_evidence:
- none in this R11 set; each major move had policy/event evidence.

evidence_good_but_price_failed:
- chip support lacks direct price anchor.
- Hanwha export later offset by dilution shock.

event_premium:
- Commercial Act / value-up.
- tax reversal.
- Hanwha defense export.
- semiconductor support.

thesis_break:
- wildfire disaster at social/asset level.
- martial law only if political instability becomes prolonged institutional damage.
- Samsung strike only if production actually stops materially.

hard_4C:
- wildfire disaster hard 4C no public price.
- no stock-specific hard 4C confirmed in R11 source set.
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
governance_reform_law,+5,"법안 통과와 KOSPI 반응이 같이 닫히면 Stage2-Actionable","Commercial Act"
tax_policy_relief,+5,"세제 불확실성 완화는 국장 beta를 직접 회복","capital gains tax reversal"
political_liquidity_backstop,+4,"martial law shock 뒤 liquidity backstop이 systemic crash를 막음","martial law"
geopolitical_export_control_risk,+5,"chip-waiver revocation은 AI/반도체 cycle의 핵심 4B","Samsung/SK Hynix"
industrial_policy_support,+3,"33T won chip package는 Stage2 relief","semiconductor support"
defense_export_backlog,+5,"geopolitical order와 backlog expansion은 Stage2","Hanwha"
labor_supply_chain_risk,+5,"national-champion strike threat는 macro/export 4B","Samsung strike"
disaster_hard_4c,+5,"wildfire/fatal disaster는 hard 4C 후보","wildfires"
```

## 내릴 축

```csv
axis,delta,reason,cases
policy_reform_without_company_action,-5,"Commercial Act만으로 개별종목 Green 금지","Commercial Act"
tax_relief_without_stability,-4,"세제 reversal 이후에도 transaction tax risk 남음","tax reversal"
liquidity_backstop_without_political_resolution,-4,"유동성 공급만으로 martial law risk 해소 금지","martial law"
AI_tax_noise_ignored,-5,"AI windfall tax comment는 KOSPI concentration 4B","AI tax"
chip_support_without_order_conversion,-4,"지원금만으로 장비/소재 수주 Green 금지","semiconductor support"
defense_order_without_dilution_adjustment,-5,"수주 뒤 증자 dilution 무시 금지","Hanwha"
strike_threat_without_cost_reset,-5,"파업 철회 전 Samsung Green 금지","Samsung strike"
disaster_without_price_anchor,-3,"재난 hard 4C는 public-stock anchor 없으면 basket MFE 금지","wildfires"
```

---

# 10. Stage2-Actionable 승격 조건

R11 Loop 17 shadow rule:

```text
R11에서 Stage2 evidence가 아래 중 4개 이상이면 Stage2-Actionable로 승격한다.

1. 법안/정책/계약/재난/노동 이벤트가 명확한 날짜에 공개된다.
2. event return 또는 index return이 +1% 이상 positive, 또는 negative 4B가 뚜렷하다.
3. 정책금액, 법안 내용, 계약금액, 피해규모가 숫자로 닫힌다.
4. 기업 EPS/OP/FCF 또는 market risk premium으로 연결되는 경로가 있다.
5. 반대축 4B, 예컨대 세금, dilution, 수출통제, 노동비용, 정치불안이 식별된다.
6. policy relief가 단순 발언이 아니라 집행 가능성이 있다.
7. price reaction이 evidence와 같은 방향으로 검증된다.
```

적용:

```text
Commercial Act:
1,2,3,4,5,6,7 충족 → Stage2-Actionable.

Tax reversal:
1,2,3,4,5,6,7 충족 → Stage2-Actionable relief.

Martial law:
1,2 negative,3,4,5,6,7 충족 → political 4B + relief.

AI windfall tax:
1,2 negative,4,5,7 충족 → 4B only.

Chip waiver:
1,2 negative,3,4,5,7 충족 → 4B only.

33T chip support:
1,3,4,5,6 충족 but price 없음 → Stage2 relief.

Hanwha:
1,2,3,4,5,7 충족 → Stage2 + dilution 4B.

Samsung strike:
1,2 negative,3,4,5,6,7 충족 → 4B labor.

Wildfires:
1,3,4,5 충족 but public price 없음 → disaster hard 4C no-price.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
Stage2 이후 아래 중 2개 이상이 추가로 닫히면 Yellow.

1. 법안이 실제 company-level capital return으로 전환.
2. 세제 안정성이 2개 이상 정책 사이클 동안 유지.
3. foreign/retail flow가 회복되고 index breadth가 넓어짐.
4. 수출통제 license가 안정화되고 capex/order risk가 낮아짐.
5. 산업지원이 실제 장비·소재·공장 주문으로 전환.
6. 방산 수주가 margin/backlog/cash-flow로 연결되고 dilution이 흡수.
7. 노동 리스크가 합의로 해소되고 고정 인건비 reset이 제한.
8. 재난 복구 수요가 수주/보험/정부지출로 변환.
```

Yellow 후보:

```text
Commercial Act:
company-level board action and capital return 확인 시 Yellow.

Tax reversal:
stable tax regime and flow recovery 확인 시 Yellow.

Hanwha defense:
delivery schedule + margin + dilution absorption 확인 시 Yellow.

Semiconductor support:
equipment/material order conversion 확인 시 Yellow.

Samsung strike:
strike averted and labor-cost reset limited 확인 시 Yellow relief.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- policy reform becomes recurring earnings/capital-return evidence.
- tax uncertainty is durably removed.
- geopolitical 4B is reduced through licenses, treaties or contracts.
- industrial-policy support converts into company-level revenue.
- defense export backlog converts into margin and cash flow.
- labor/disaster risk is resolved without structural damage.
- full-window MFE/MAE is favorable.
```

이번 R11 Loop 17에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + company-level execution / policy stability / flow recovery / license stability / labor settlement gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- tax policy contradicts value-up.
- martial law or political crisis threatens institutions.
- AI windfall tax rhetoric targets cycle leaders.
- U.S. export controls affect Korean strategic assets.
- support package lacks stock/order conversion.
- defense export financed by dilutive equity.
- national-champion strike risks production/export.
- disaster creates compensation/rebuilding/safety cost without price anchor.
```

적용:

```text
Commercial Act:
positive Stage2 but policy enforcement 4B.

Tax reversal:
relief but transaction tax/future policy 4B.

Martial law:
political risk 4B.

AI windfall tax:
AI concentration and tax-populism 4B.

Chip waiver:
US-China export-control 4B.

Hanwha:
dilution 4B.

Samsung:
labor supply-chain 4B.

Wildfires:
disaster hard 4C no-price.
```

---

# 14. 4C hard gate 조건

```text
R11 4C:
- disaster with fatalities and asset destruction plus listed-company earnings/price hit
- political crisis that freezes market function or capital flows
- export-control order that permanently blocks production or technology upgrade
- labor strike causing actual prolonged production halt and revenue cut
- policy/tax law that structurally removes cycle profits
```

이번 R11 Loop 17 hard/strong 4C:

```text
disaster-level hard 4C:
- 2025 South Korea wildfires.

stock-specific hard 4C:
- not confirmed with reliable public-stock price anchor in this source set.
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R11 production 설계 원칙:

```text
1. policy announcement와 company execution을 분리한다.
2. positive policy와 contradictory tax policy를 동시에 본다.
3. geopolitical export control은 AI/semiconductor score에서 선차감한다.
4. defense export는 backlog와 dilution을 같이 본다.
5. national-champion labor risk는 supply-chain 4B로 둔다.
6. disaster는 social hard 4C와 listed-stock hard 4C를 분리한다.
7. liquidity backstop은 relief이지 political-risk Green이 아니다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_260.md 요약

```md
# R11 Loop 17. Policy / Geopolitics / Disaster / Event Trigger-level Price Validation

이번 라운드는 R11 Loop 17 trigger-level validation 라운드다.

핵심 결론:
- Commercial Act reform is R11’s cleanest Stage2-Actionable policy trigger. Parliament passed the revised Commercial Act expanding fiduciary duties of boards to minority shareholders, and KOSPI rose 1.34% to 3,116.27.
- Capital-gains tax reversal is Stage2 policy relief. The August tax proposal shock drove KOSPI down 3.9%; Lee later said lowering the large-shareholder threshold was unnecessary, and KOSPI rose 0.6~0.9%.
- Martial law is political-risk 4B with liquidity relief. KOSPI fell 1.44%, Samsung Electronics -0.93%, won shocked around 1,444, while the government/BOK pledged unlimited liquidity and up to 10T won stabilization.
- AI windfall tax comment is policy-overhang 4B. KOSPI fell as much as 5% and closed down 2.3% after a senior policy official floated a national dividend from AI excess profits; the presidential office later called it a personal view.
- U.S. chip-waiver revocation is geopolitical export-control 4B. SK Hynix fell nearly 5% and Samsung more than 2% after U.S. removed VEU waivers for China fabs.
- 33T won semiconductor support is Stage2 relief no-price. Korea expanded support from 26T won to 33T won and added 3T won auto support, but direct stock-price anchor was not captured.
- Hanwha Aerospace defense export is Stage2 with dilution 4B. $1B Romania K9 order drove shares +5% to record high, but later 3.6T won / $2.5B share sale caused shares -13%.
- Samsung strike threat is national-champion labor 4B. Samsung shares fell 9.3%; government considered emergency arbitration, with one-day halt risk estimated at 1T won direct losses and prolonged disruption up to 100T won.
- 2025 wildfires are disaster hard 4C no public price. At least 26 deaths and around 48,000 hectares burned were reported, but no direct listed-stock price anchor was captured.

Main calibration:
- Raise governance_reform_law, tax_policy_relief, political_liquidity_backstop, geopolitical_export_control_risk, industrial_policy_support, defense_export_backlog, labor_supply_chain_risk, disaster_hard_4c.
- Lower policy_reform_without_company_action, tax_relief_without_stability, liquidity_backstop_without_political_resolution, AI_tax_noise_ignored, chip_support_without_order_conversion, defense_order_without_dilution_adjustment, strike_threat_without_cost_reset, disaster_without_price_anchor.
```

## docs/checkpoints/checkpoint_28a_round260_r11_loop17.md 요약

```md
# Checkpoint 28A Round 260 R11 Loop 17 Trigger-level Calibration

## 반영 내용
- R11 Loop 17 trigger-level validation을 수행했다.
- Commercial Act, capital-gains tax reversal, martial law liquidity intervention, AI windfall tax comment, U.S. chip-waiver revocation, 33T won semiconductor support, Hanwha defense export/dilution, Samsung strike threat, 2025 wildfires를 검토했다.
- full adjusted OHLC는 확보하지 못했으므로 Reuters / FT / AP / MarketWatch / Barron’s reported event return과 event price anchor를 사용했다.
- MFE/MAE는 조작하지 않고 price_data_unavailable_after_deep_search로 분리했다.

## 핵심 보정
- Policy reform is Stage2 until company-level execution appears.
- Tax policy can reverse or erase value-up premium.
- Liquidity backstop is relief, not Green.
- U.S. export controls are core 4B for Korean strategic assets.
- Defense orders must be adjusted for dilution and capex funding.
- National-champion labor risks can hit supply-chain reliability.
- Disaster hard 4C and listed-stock hard 4C must be separated.
```

## data/e2r_case_library/cases_r11_loop17_round260.jsonl 초안

```jsonl
{"case_id":"r11_loop17_commercial_act_valueup","symbol":"KOSPI/valueup_basket/financials/holdcos","company_name":"Korea market governance reform basket","case_type":"Stage2_Actionable_market_governance_reform","primary_archetype":"COMMERCIAL_ACT_VALUEUP_STAGE2_ACTIONABLE","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2025-07-03","kospi_event_return_pct":1.34,"kospi_close_points":3116.27,"policy":"revised_Commercial_Act_expands_board_fiduciary_duty_to_shareholders","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_policy_reform","notes":"Law passage and KOSPI reaction aligned; company-level capital return is Yellow gate."}
{"case_id":"r11_loop17_capital_gains_tax_reversal","symbol":"KOSPI/retail_sensitive_basket/brokers/financials","company_name":"Korea market tax-policy basket","case_type":"tax_policy_4B_then_Stage2_relief","primary_archetype":"TAX_POLICY_RELIEF_STAGE2_WITH_TAX_4B","best_trigger":"T0/T3","stage_candidate":"Stage2 relief + 4B-watch","price_validation":{"tax_shock_date":"2025-08-01","tax_shock_kospi_return_pct":-3.9,"relief_date":"2025-09-11","relief_kospi_return_reuters_pct":0.6,"relief_kospi_return_ft_pct":0.9,"large_shareholder_threshold_original_krw_bn":5,"large_shareholder_threshold_proposed_krw_bn":1,"transaction_tax_before_pct":0.15,"transaction_tax_proposed_pct":0.2,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_policy_relief_with_tax_4B","notes":"Tax relief restored market sentiment, but transaction tax and future tax uncertainty remain 4B."}
{"case_id":"r11_loop17_martial_law_liquidity_intervention","symbol":"KOSPI/KRW/EWY/banks/brokers/exporters","company_name":"Korea political-risk basket","case_type":"political_risk_4B_with_liquidity_relief","primary_archetype":"MARTIAL_LAW_POLITICAL_RISK_4B","best_trigger":"T0/T3","stage_candidate":"4B with relief","price_validation":{"trigger_date":"2024-12-04","kospi_event_return_pct":-1.44,"samsung_electronics_event_return_pct":-0.93,"won_initial_shock_usdkrw_context":1444,"won_later_context_usdkrw":1410,"market_stabilization_fund_krw_trn":10,"liquidity_response":"unlimited_liquidity_and_special_repo_operations","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"political_risk_4B_not_hard_4C","notes":"Political shock hit FX/stocks, but liquidity backstop prevented systemic hard 4C."}
{"case_id":"r11_loop17_ai_windfall_tax_policy_overhang","symbol":"KOSPI/005930/000660/AI_memory_basket","company_name":"AI memory / KOSPI concentration basket","case_type":"4B_AI_windfall_tax_policy_overhang","primary_archetype":"AI_WINDFALL_TAX_POLICY_OVERHANG_4B","best_trigger":"T0/T2","stage_candidate":"4B-watch","price_validation":{"trigger_date":"2026-05-12","kospi_intraday_drop_pct":-5.0,"kospi_close_return_pct":-2.3,"policy_context":"AI_excess_profit_national_dividend_comment","relief_context":"presidential_office_called_comment_personal_opinion","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"AI_policy_overhang_4B_not_hard_4C","notes":"AI tax rhetoric can hit concentrated KOSPI leaders even without enacted law."}
{"case_id":"r11_loop17_us_chip_waiver_revocation","symbol":"005930/000660/semiconductor_supply_chain","company_name":"Samsung Electronics / SK Hynix","case_type":"4B_geopolitical_chip_export_control","primary_archetype":"CHIP_EXPORT_CONTROL_4B_WITH_POLICY_RELIEF","best_trigger":"T0/T2","stage_candidate":"4B-watch","price_validation":{"trigger_date":"2025-09-01","sk_hynix_event_return_pct":"nearly_-5","samsung_event_return_pct":"more_than_-2","policy":"VEU_waiver_removed_for_China_fabs","relief_context":"licenses_expected_for_existing_fab_operations_but_not_expansion_or_upgrade","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"chip_export_control_4B_not_hard_4C","notes":"Export-control shock hit memory leaders, but existing-fab license relief prevents hard 4C."}
{"case_id":"r11_loop17_semiconductor_support_33t","symbol":"005930/000660/chip_equipment_materials_basket","company_name":"Korea semiconductor support basket","case_type":"Stage2_policy_relief_no_direct_price","primary_archetype":"SEMICONDUCTOR_TARIFF_SUPPORT_STAGE2_RELIEF","best_trigger":"T0/T3","stage_candidate":"Stage2 relief","price_validation":{"trigger_date":"2025-04-15","semiconductor_support_krw_trn":33,"prior_support_krw_trn":26,"support_increase_pct":26,"auto_support_krw_trn":3,"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_policy_relief_no_price","notes":"Large support package is relief, but company-level order/capex conversion and event-window price are missing."}
{"case_id":"r11_loop17_hanwha_defense_export_dilution","symbol":"012450","company_name":"Hanwha Aerospace","case_type":"Stage2_defense_export_with_dilution_4B","primary_archetype":"DEFENSE_GEOPOLITICAL_EXPORT_STAGE2_WITH_DILUTION_4B","best_trigger":"T0/T2","stage_candidate":"Stage2 + 4B-watch","price_validation":{"export_trigger_date":"2024-07-09","romania_order_value_usd_bn":1.0,"k9_units":54,"k10_units":36,"export_event_return_pct":5,"order_backlog_mar_2024_krw_trn":30,"share_sale_value_krw_trn":3.6,"share_sale_value_usd_bn":2.5,"dilution_event_return_pct":-13,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"defense_export_stage2_with_dilution_4B","notes":"Geopolitical export order was strong, but equity financing/dilution must be deducted."}
{"case_id":"r11_loop17_samsung_strike_government_arbitration","symbol":"005930","company_name":"Samsung Electronics","case_type":"4B_national_champion_labor_strike","primary_archetype":"NATIONAL_CHAMPION_LABOR_STRIKE_4B","best_trigger":"T0/T3","stage_candidate":"4B-watch","price_validation":{"trigger_date":"2026-05-15","event_return_pct":-9.3,"potential_strike_duration_days":18,"possible_workers_involved":">50000","government_tool":"emergency_arbitration_possible","single_day_direct_loss_krw_trn":1,"prolonged_disruption_loss_krw_trn":100,"hard_4C_status":"not_confirmed","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"national_champion_labor_4B_not_hard_4C","notes":"Strike threat hit Samsung; hard 4C requires actual sustained production disruption."}
{"case_id":"r11_loop17_south_korea_wildfire_disaster","symbol":"insurers/rebuild_basket/forestry/disaster_relief_basket","company_name":"South Korea wildfire disaster basket","case_type":"disaster_hard_4C_no_public_price","primary_archetype":"WILDFIRE_DISASTER_HARD_4C_NO_PUBLIC_PRICE","best_trigger":"T0/T2","stage_candidate":"disaster hard 4C no public price","price_validation":{"trigger_date":"2025-03-25_to_2025-03-30","fatalities_initial_context":16,"fatalities_followup_context":26,"burned_area_hectares_context":48000,"destroyed_structures_context":"thousands_of_buildings","public_stock_price_anchor":"price_data_unavailable_after_deep_search","hard_4C_status":"disaster_level_confirmed_public_stock_not_available"},"score_price_alignment":"wildfire_disaster_hard_4C_no_public_price","notes":"Disaster-level hard 4C confirmed, but no listed-stock price anchor for forward-return calculation."}
```

## data/e2r_trigger_calibration/triggers_r11_loop17_round260.jsonl 초안

```jsonl
{"trigger_id":"r11l17_commercial_act_T1","case_id":"r11_loop17_commercial_act_valueup","trigger_type":"Stage2-Actionable_governance_reform_law","trigger_date":"2025-07-03","event_return_pct":1.34,"trigger_outcome_label":"excellent_stage2_actionable_policy_reform","promote_to":"Stage2-Actionable"}
{"trigger_id":"r11l17_tax_shock_T0","case_id":"r11_loop17_capital_gains_tax_reversal","trigger_type":"4B_tax_policy_shock","trigger_date":"2025-08-01","event_return_pct":-3.9,"trigger_outcome_label":"tax_policy_4B","promote_to":"4B-watch"}
{"trigger_id":"r11l17_tax_reversal_T1","case_id":"r11_loop17_capital_gains_tax_reversal","trigger_type":"Stage2_tax_policy_relief","trigger_date":"2025-09-11","event_return_pct":"Reuters_+0.6_FT_+0.9","trigger_outcome_label":"Stage2_policy_relief","promote_to":"Stage2-Actionable"}
{"trigger_id":"r11l17_martial_law_T0","case_id":"r11_loop17_martial_law_liquidity_intervention","trigger_type":"4B_political_risk_martial_law","trigger_date":"2024-12-04","event_return_pct":-1.44,"trigger_outcome_label":"political_risk_4B_not_hard_4C","promote_to":"4B-watch"}
{"trigger_id":"r11l17_martial_liquidity_T2","case_id":"r11_loop17_martial_law_liquidity_intervention","trigger_type":"Stage2_liquidity_relief","trigger_date":"2024-12-04","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"liquidity_relief_not_Green","promote_to":"Stage2_relief"}
{"trigger_id":"r11l17_ai_windfall_tax_T0","case_id":"r11_loop17_ai_windfall_tax_policy_overhang","trigger_type":"4B_AI_policy_tax_overhang","trigger_date":"2026-05-12","event_return_pct":-2.3,"trigger_outcome_label":"AI_policy_overhang_4B","promote_to":"4B-watch"}
{"trigger_id":"r11l17_chip_waiver_T0","case_id":"r11_loop17_us_chip_waiver_revocation","trigger_type":"4B_chip_export_control","trigger_date":"2025-09-01","event_return_pct":"SKHynix_nearly_-5_Samsung_more_than_-2","trigger_outcome_label":"chip_export_control_4B","promote_to":"4B-watch"}
{"trigger_id":"r11l17_chip_support_T0","case_id":"r11_loop17_semiconductor_support_33t","trigger_type":"Stage2_semiconductor_policy_relief","trigger_date":"2025-04-15","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_policy_relief_no_price","promote_to":"Stage2_relief"}
{"trigger_id":"r11l17_hanwha_romania_T0","case_id":"r11_loop17_hanwha_defense_export_dilution","trigger_type":"Stage2_defense_export_geopolitical_order","trigger_date":"2024-07-09","event_return_pct":5,"trigger_outcome_label":"defense_export_stage2","promote_to":"Stage2"}
{"trigger_id":"r11l17_hanwha_dilution_T2","case_id":"r11_loop17_hanwha_defense_export_dilution","trigger_type":"4B_defense_dilution_equity_financing","trigger_date":"2025-04","event_return_pct":-13,"trigger_outcome_label":"dilution_4B_after_defense_rerating","promote_to":"4B-watch"}
{"trigger_id":"r11l17_samsung_strike_T0","case_id":"r11_loop17_samsung_strike_government_arbitration","trigger_type":"4B_national_champion_labor_strike","trigger_date":"2026-05-15","event_return_pct":-9.3,"trigger_outcome_label":"national_champion_labor_4B","promote_to":"4B-watch"}
{"trigger_id":"r11l17_wildfire_T0","case_id":"r11_loop17_south_korea_wildfire_disaster","trigger_type":"disaster_hard_4C_no_public_price","trigger_date":"2025-03-25_to_2025-03-30","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"wildfire_disaster_hard_4C_no_public_price","promote_to":"4C_disaster_watch"}
```

## data/sector_taxonomy/score_weight_profiles_round260_r11_loop17_v1.csv 초안

```csv
archetype,governance_reform_law,tax_policy_relief,political_liquidity_backstop,geopolitical_export_control_risk,industrial_policy_support,defense_export_backlog,labor_supply_chain_risk,disaster_hard_4c,policy_reform_without_company_action_penalty,tax_relief_without_stability_penalty,liquidity_backstop_without_political_resolution_penalty,AI_tax_noise_ignored_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
COMMERCIAL_ACT_VALUEUP_STAGE2_ACTIONABLE,+5,+1,+0,+0,+0,+0,+0,+0,-5,-1,-1,-1,Commercial Act + KOSPI +1.34,company action missing,buyback/dividend/governance execution,Commercial Act.
TAX_POLICY_RELIEF_STAGE2_WITH_TAX_4B,+2,+5,+0,+0,+0,+0,+0,+0,-2,-4,-1,-1,tax reversal after -3.9 shock,transaction tax remains,stable tax regime+flow recovery,tax policy.
MARTIAL_LAW_POLITICAL_RISK_4B,+0,+0,+5,+1,+0,+0,+0,+1,-1,-1,-5,-1,martial law KOSPI -1.44 and liquidity relief,political resolution missing,FX/foreign-flow stabilization,martial law.
AI_WINDFALL_TAX_POLICY_OVERHANG_4B,+0,+0,+0,+2,+0,+0,+0,+0,-1,-2,-1,-5,KOSPI -2.3 on AI tax comment,policy overhang,law risk removed and flow recovers,AI tax.
CHIP_EXPORT_CONTROL_4B_WITH_POLICY_RELIEF,+0,+0,+1,+5,+2,+0,+0,+0,-1,-1,-1,-1,US VEU waiver removal hit Samsung/SK Hynix,license dependency,license stability+capex clarity,chip waivers.
SEMICONDUCTOR_TARIFF_SUPPORT_STAGE2_RELIEF,+0,+1,+0,+3,+5,+0,+0,+0,-1,-1,-1,-1,33T won semiconductor package,no event price/order conversion,order/capex conversion,chip support.
DEFENSE_GEOPOLITICAL_EXPORT_STAGE2_WITH_DILUTION_4B,+0,+0,+0,+3,+1,+5,+0,+0,-1,-1,-1,-1,Hanwha Romania order +5 but dilution -13,dilution and capex,margin+delivery+dilution absorption,Hanwha.
NATIONAL_CHAMPION_LABOR_STRIKE_4B,+0,+0,+2,+1,+0,+0,+5,+0,-1,-1,-1,-1,Samsung strike threat -9.3,settlement missing,strike averted+cost reset contained,Samsung.
WILDFIRE_DISASTER_HARD_4C_NO_PUBLIC_PRICE,+0,+0,+1,+0,+1,+0,+0,+5,-1,-1,-1,-1,wildfire fatalities and property damage,no public price anchor,rebuilding/insurance conversion,wildfires.
```

---

# 이번 R11 Loop 17 결론

```text
1. Commercial Act reform은 R11의 가장 좋은 Stage2-Actionable이다.
   법안 통과와 KOSPI +1.34%가 동시에 닫혔다.

2. Capital-gains tax reversal은 Stage2 policy relief다.
   tax proposal shock은 KOSPI -3.9%, reversal은 +0.6~0.9%였다.

3. Martial law crisis는 political-risk 4B다.
   KOSPI -1.44%, won shock가 있었지만 unlimited liquidity와 10T won stabilization fund가 systemic hard 4C를 막았다.

4. AI windfall tax comment는 policy-overhang 4B다.
   KOSPI intraday -5%, close -2.3%; 실제 법안은 아니므로 hard 4C는 아니다.

5. U.S. chip-waiver revocation은 geopolitical chip 4B다.
   SK Hynix nearly -5%, Samsung >-2%; existing-fab license relief가 있어 hard 4C는 아니다.

6. 33T won semiconductor support는 Stage2 relief no-price다.
   지원금은 크지만 company-level order/capex conversion과 event-window price anchor가 없다.

7. Hanwha Aerospace는 defense export Stage2 + dilution 4B다.
   Romania $1B order는 shares +5%, 그러나 3.6T won share sale은 -13%였다.

8. Samsung strike threat는 national-champion labor 4B다.
   shares -9.3%, 정부 emergency arbitration watch; 실제 장기 생산중단 전까지 hard 4C는 아니다.

9. 2025 wildfires는 disaster hard 4C no public price다.
   최소 26명 사망, 48,000ha context가 있지만 listed-stock price anchor는 없다.
```

한 문장으로 압축하면:

> **R11 Loop 17에서 배운 핵심은 “정책·지정학·재난 headline”이 아니라, 법안 집행, 세제 안정성, liquidity backstop, export-license 안정성, 산업지원의 주문 전환, 방산수주의 dilution 흡수, 노동분쟁 해소, 재난의 listed-price anchor가 닫혀야 Stage3로 올릴 수 있다는 것이다. 좋은 정책도 회사별 실행 전에는 Stage2이고, AI tax·수출통제·파업·재난은 주도주를 바로 4B/4C로 끌어내릴 수 있다.**

다음 순서는 **R12 Loop 17 — 농업·생활서비스·기타**다.

[1]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-assembly-passes-commerce-bill-expanding-duty-boards-shareholders-2025-07-03/?utm_source=chatgpt.com "South Korea assembly passes commerce bill expanding duty of boards to shareholders"
[2]: https://www.marketwatch.com/story/south-koreas-new-tax-proposals-derail-one-of-the-worlds-best-performing-stock-markets-of-2025-9432538d?utm_source=chatgpt.com "South Korea's new tax proposals derail one of the world's best performing stock markets of 2025."
[3]: https://www.reuters.com/markets/asia/skorea-authorities-vow-stabilize-markets-parliament-votes-lift-martial-law-2024-12-03/?utm_source=chatgpt.com "South Korea rushes to stabilise markets after Yoon's martial law bid"
[4]: https://www.barrons.com/articles/ai-tax-stock-market-kospi-2e468921?utm_source=chatgpt.com "Why the World's Hottest Stock Market Got Derailed by Talk of an AI Tax"
[5]: https://www.ft.com/content/fd77488c-d5f3-4677-ba90-cc7e8de74333?utm_source=chatgpt.com "US chipmaking curbs hit Samsung and SK Hynix"
[6]: https://apnews.com/article/658f4ca0007ebef98d2b477ecd531867?utm_source=chatgpt.com "South Korea to boost support of semiconductor industry in the face of Trump's tariffs"
[7]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-wins-1-bln-order-romania-k9-howitzers-2024-07-09/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace wins $1 bln order from Romania for self-propelled howitzers"
[8]: https://www.reuters.com/business/world-at-work/samsung-elecs-union-says-samsung-proposed-unconditional-talks-strike-plan-holds-2026-05-15/?utm_source=chatgpt.com "Samsung's South Korean union sticks to strike plan after talks offer; shares slide"
[9]: https://www.reuters.com/world/asia-pacific/death-toll-south-korea-wildfires-rises-15-yonhap-says-2025-03-25/?utm_source=chatgpt.com "Death toll in South Korea wildfires rises to 16"
