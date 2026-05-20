순서상 이번은 **R3 Loop 17 — 2차전지·전기차·친환경 trigger-level price validation 라운드**다.

```text
round = R3 Loop 17
round_id = round_252
large_sector = SECONDARY_BATTERY_EV_GREEN
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R4 Loop 17
```

이번 라운드도 KRX/Naver/Yahoo/Stooq 수정주가 일봉 OHLC window를 안정적으로 확보하지 못했다. 그래서 MFE/MAE/peak/drawdown 숫자는 만들지 않는다. 대신 Reuters/FT/WSJ/MarketWatch/AP의 **reported event return, event price, 계약금액, 수요·정책 trigger**를 가격 anchor로 쓴다. 즉 `MFE_30D/90D/180D/1Y/2Y = price_data_unavailable_after_deep_search`다.

---

# 1. 이번 라운드 대섹터

```text
R3 = 2차전지·전기차·친환경
```

R3의 core gate는 아래다.

```text
EV battery:
EV 수요 → OEM 계약 → 공장 가동률 → AMPC / IRA credit → margin → 계약 취소 / subsidy change

ESS / data-center battery:
AI data-center 전력수요 → ESS LFP 계약 → EV line 전환 → utilization 회복 → margin

Battery materials:
lithium / nickel / cathode price → 재고평가 → cathode ASP → customer volume → margin

Solid-state / next-gen:
technology timeline → pilot / mass production → customer adoption → ASP → actual revenue

Recycling / circular:
policy / raw material shortage → recycling volume → black mass sourcing → margin

4B / 4C:
EV subsidy rollback, OEM contract cancellation, capital raise dilution, lithium price reversal,
line conversion execution, LFP price competition, customer concentration
```

---

# 2. 대상 canonical archetype

```text
ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE
EV_CONTRACT_CANCELLATION_4C
SK_ON_ESS_PIVOT_STAGE2_WITH_PARENT_READTHROUGH
LITHIUM_PRICE_REBOUND_CYCLICAL_STAGE2
SOLID_STATE_TIMELINE_STAGE2_YELLOW_CANDIDATE
IRA_AMPC_EARNINGS_WITH_POLICY_4B
CAPITAL_RAISE_DILUTION_4B
UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE
```

---

# 3. deep sub-archetype

```text
Samsung SDI / ESS LFP:
- Samsung SDI America signs 2T won+ / $1.36B LFP ESS battery deal.
- deliveries for three years from 2027.
- U.S. plant existing lines to be converted.
- shares +6.1%, KOSPI -0.1%.
- Stage2-Actionable, but customer undisclosed and delivery starts 2027.

LG Energy Solution / Ford-Freudenberg cancellations:
- Ford terminates 9.6T won / $6.5B EV battery supply deal.
- LGES shares -7.6%, KOSPI -1.4%.
- Freudenberg contract 3.9T won / $2.7B also cancelled.
- total lost expected revenue about 13.5T won in less than 10 days.
- 4C thesis-break for EV contract quality and European utilization.

SK On / ESS pivot:
- SK On signs Flatiron Energy ESS LFP deal up to 7.2GWh, 2026~2030.
- Georgia EV lines to be converted for ESS.
- Ford JV split: Ford takes Kentucky plants, SK On Tennessee.
- SK On Q3 2025 OP loss 124.8B won.
- Stage2 pivot, but SK On is unlisted; parent/readthrough price unavailable.

POSCO Future M / L&F / lithium rebound:
- CATL suspends Yichun lithium mine after license expiry.
- POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%, KOSPI -0.1%.
- lithium had fallen up to 90% from 2022 peak.
- cyclical Stage2, not Green, because license renewal and lithium oversupply remain 4B.

Samsung SDI / all-solid-state timeline:
- Samsung SDI says all-solid-state battery mass production from 2027.
- shares +11% to 405,500 won, KOSPI +0.3%.
- also plans larger cylindrical batteries by 2025 and LFP by 2026.
- Stage2 / Yellow candidate, but no customer revenue yet.

LGES / IRA AMPC earnings:
- Q2 operating profit estimate 492B won, +152% YoY.
- sales -9.7%.
- excluding AMPC, operating profit only 1.4B won and margin 0.03%.
- shares +2.4%, but year-to-date down over 8%.
- evidence good but policy-credit dependency 4B.

Samsung SDI / capital raise:
- 2T won / $1.4B share issuance.
- offering price cut 14%, 169,200 won → 146,200 won.
- shares down 29.5% YTD and down 1% on the day.
- dilution / capex financing 4B.

POSCO / MinRes lithium JV:
- POSCO to buy 30% stake in part of MinRes lithium business for $765M.
- POSCO gains effective 15% in Wodgina and Mt Marion lithium mines.
- MinRes shares +10.8%; direct POSCO KRX price unavailable.
- strategic upstream Stage2, no Green without lithium price / offtake / margin.
```

---

# 4. 선정 case 요약

| bucket                                 | case                                     | 핵심 판정                                                      |
| -------------------------------------- | ---------------------------------------- | ---------------------------------------------------------- |
| structural_success / Stage2-Actionable | **Samsung SDI ESS LFP deal**             | 2T won+ ESS 계약, +6.1%, EV line → ESS 전환                    |
| 4C-thesis-break                        | **LGES Ford/Freudenberg cancellations**  | Ford 9.6T won, Freudenberg 3.9T won 취소, LGES -7.6%         |
| Stage2 pivot                           | **SK On ESS / Flatiron + Ford JV split** | 7.2GWh ESS, EV 수요 둔화 대응, parent price unavailable          |
| cyclical_success / Stage2              | **POSCO Future M / L&F lithium rebound** | CATL mine suspension, POSCO Future M +8.3%, L&F +10%       |
| Stage3-Yellow candidate                | **Samsung SDI all-solid-state timeline** | +11%, 2027 전고체 양산 timeline                                 |
| evidence_good_but_policy_4B            | **LGES IRA AMPC earnings**               | OP +152%지만 AMPC 제외하면 margin 0.03%                          |
| 4B-watch                               | **Samsung SDI capital raise**            | 2T won 증자, 발행가 14% 인하                                      |
| Stage2 no-price                        | **POSCO / MinRes lithium JV**            | $765M upstream lithium stake, POSCO direct price anchor 없음 |

---

# 5. 각 case별 trigger grid

## Case A — Samsung SDI ESS LFP contract

```text
symbol = 006400
case_type = Stage2-Actionable ESS pivot
archetype = ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE
```

| trigger |              type | date          | 당시 공개 evidence                                                             | 가격 anchor                      | outcome |
| ------- | ----------------: | ------------- | -------------------------------------------------------------------------- | ------------------------------ | ------- |
| T0      |            Stage1 | 2025H2        | EV 수요 둔화, ESS/data-center battery 수요 부상                                    | no entry                       |         |
| T1      | Stage2-Actionable | 2025-12-09/10 | Samsung SDI America, U.S. customer에 LFP ESS battery 2T won+ 공급계약           | Samsung SDI +6.1%, KOSPI -0.1% |         |
| T2      |        validation | 2025-12-09/10 | 2027년부터 3년간 공급, 기존 U.S. plant line 전환                                      | same                           |         |
| T3      |          4B-watch | 2025~2027     | customer undisclosed, delivery 2027, LFP margin, line conversion execution | no full OHLC                   |         |
| T4      |     Stage3-Yellow | N/A           | ESS line conversion, margin, delivery visibility 필요                        | 보류                             |         |

Samsung SDI ESS LFP deal은 R3의 가장 깨끗한 Stage2-Actionable이다. 계약금액은 2조원 이상, 약 $1.36B이고, 발표 후 Samsung SDI는 장중 +6.1% 오른 반면 KOSPI는 -0.1%였다. 핵심은 EV line 일부를 ESS용 LFP로 전환한다는 점이다. EV 수요 둔화가 있는 상황에서 “공장 가동률을 ESS로 방어하는 trigger”라서 점수를 올릴 수 있다. 다만 고객 비공개, 2027년 공급 시작, LFP margin이 gate다. ([Reuters][1])

```json
{
  "case_id": "r3_loop17_samsung_sdi_ess_lfp",
  "symbol": "006400",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_ESS_LFP_line_conversion",
  "trigger_date": "2025-12-09",
  "contract_value_krw_trn": ">2.0",
  "contract_value_usd_bn": 1.36,
  "delivery_period": "3_years_from_2027",
  "event_return_pct": 6.1,
  "kospi_same_context_pct": -0.1,
  "market_relative_return_pp": 6.2,
  "line_conversion": "existing_US_EV_lines_to_ESS_LFP",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "customer_name",
    "firm_delivery_schedule",
    "LFP_margin",
    "line_conversion_cost",
    "ESS_repeat_orders",
    "full_OHLC_MFE_MAE"
  ],
  "trigger_outcome_label": "excellent_stage2_actionable_ESS_pivot"
}
```

---

## Case B — LG Energy Solution Ford / Freudenberg cancellations

```text
symbol = 373220
case_type = 4C contract cancellation
archetype = EV_CONTRACT_CANCELLATION_4C
```

| trigger |          type | date          | 당시 공개 evidence                                                              | 가격 anchor                | outcome |
| ------- | ------------: | ------------- | --------------------------------------------------------------------------- | ------------------------ | ------- |
| T0      |    4C trigger | 2025-12-17/18 | Ford cancels LGES EV battery supply deal worth 9.6T won / $6.5B             | LGES -7.6%, KOSPI -1.4%  |         |
| T1      |    validation | 2025-12-18    | contract was to start Jan 2027; European plant utilization delay likely     | same                     |         |
| T2      | 4C escalation | 2025-12-26    | Freudenberg contract 3.9T won / $2.7B also cancelled                        | no stock price in source |         |
| T3      |  thesis-break | 2025-12       | total expected revenue loss about 13.5T won in <10 days; >half 2024 revenue | 4C                       |         |
| T4      |        relief | N/A           | replacement orders / ESS conversion / utilization recovery not confirmed    | 보류                       |         |

LGES는 이번 R3의 가장 강한 4C다. Ford가 9.6조원, 약 $6.5B EV battery supply agreement를 취소했고, LGES 주가는 장중 -7.6% 하락했다. 같은 구간 KOSPI는 -1.4%였다. 이어 Freudenberg Battery Power Systems 계약 3.9조원, 약 $2.7B도 종료되어, 10일도 안 되는 기간에 약 13.5조원 expected revenue가 사라졌다. 이건 단순 bad news가 아니라 **계약 품질과 유럽 공장 utilization thesis가 깨진 case**다. ([Reuters][2])

```json
{
  "case_id": "r3_loop17_lges_ford_freudenberg_cancellation",
  "symbol": "373220",
  "best_trigger": "T0/T3",
  "best_trigger_type": "4C_EV_contract_cancellation",
  "ford_cancellation_date": "2025-12-17",
  "ford_contract_value_krw_trn": 9.6,
  "ford_contract_value_usd_bn": 6.5,
  "ford_event_return_pct": -7.6,
  "kospi_same_context_pct": -1.4,
  "market_relative_return_pp": -6.2,
  "freudenberg_cancellation_date": "2025-12-26",
  "freudenberg_contract_value_krw_trn": 3.9,
  "freudenberg_contract_value_usd_bn": 2.7,
  "expected_revenue_loss_krw_trn": 13.5,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "recovery_gate_missing": [
    "replacement_orders",
    "European_plant_utilization",
    "ESS_line_conversion",
    "margin_recovery",
    "OEM_demand_recovery"
  ],
  "trigger_outcome_label": "hard_4C_contract_quality_break"
}
```

---

## Case C — SK On ESS pivot / Flatiron deal and Ford JV split

```text
symbol = 096770 readthrough
case_type = Stage2 ESS pivot with parent readthrough unavailable
archetype = SK_ON_ESS_PIVOT_STAGE2_WITH_PARENT_READTHROUGH
```

| trigger |               type | date       | 당시 공개 evidence                                                                       | 가격 anchor                | outcome |
| ------- | -----------------: | ---------- | ------------------------------------------------------------------------------------ | ------------------------ | ------- |
| T0      |       Stage2 pivot | 2025-09-03 | SK On signs Flatiron Energy deal to supply up to 7.2GWh LFP ESS batteries, 2026~2030 | SK On unlisted           |         |
| T1      |         validation | 2025-09-03 | Georgia EV lines to be converted for ESS; LFP capability planned in Korea            | parent price unavailable |         |
| T2      | 4B / restructuring | 2025-12-11 | SK On and Ford end U.S. battery JV; Ford takes Kentucky, SK On Tennessee             | no clean price           |         |
| T3      |         validation | 2025-12-11 | SK On Q3 2025 OP loss 124.8B won; fixed-cost/profitability pressure                  | 4B                       |         |
| T4      |      Stage3-Yellow | N/A        | parent valuation / SK On margin recovery / ESS revenue not confirmed                 | 보류                       |         |

SK On은 상장사가 아니므로 direct KRX price anchor가 없다. 그래도 R3에서는 중요한 구조다. Flatiron Energy에 2026~2030년 최대 7.2GWh LFP ESS를 공급하고, Georgia EV lines 일부를 ESS로 전환한다. 반면 Ford와의 $11.4B U.S. battery JV는 해체되고, SK On은 Tennessee facility를 맡는다. 이는 “EV 수요 둔화 → ESS 전환”이라는 Stage2 pivot이지만, Q3 2025 OP loss 124.8B won과 JV 구조조정이 4B다. ([Reuters][3])

```json
{
  "case_id": "r3_loop17_sk_on_ess_flatiron_ford_jv",
  "symbol": "096770_readthrough",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage2_ESS_pivot_with_4B_restructuring",
  "flatiron_deal_date": "2025-09-03",
  "ess_volume_gwh": 7.2,
  "supply_period": "2026-2030",
  "technology": "LFP_ESS",
  "georgia_line_conversion": true,
  "ford_jv_split_date": "2025-12-11",
  "original_ford_sk_investment_usd_bn": 11.4,
  "sk_on_q3_2025_operating_loss_krw_bn": 124.8,
  "direct_price_anchor": "price_data_unavailable_unlisted_subsidiary",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "SK_On_margin_recovery",
    "parent_SK_Innovation_valuation_impact",
    "Tennessee_plant_utilization",
    "ESS_delivery_margin",
    "fixed_cost_reduction"
  ],
  "trigger_outcome_label": "Stage2_ESS_pivot_with_parent_readthrough_unavailable"
}
```

---

## Case D — POSCO Future M / L&F lithium rebound after CATL mine suspension

```text
symbols = 003670 / 066970 / 006400 / 373220
case_type = cyclical Stage2 lithium-price rebound
archetype = LITHIUM_PRICE_REBOUND_CYCLICAL_STAGE2
```

| trigger |            type | date       | 당시 공개 evidence                                                         | 가격 anchor                      | outcome |
| ------- | --------------: | ---------- | ---------------------------------------------------------------------- | ------------------------------ | ------- |
| T0      | cyclical Stage2 | 2025-08-11 | CATL suspends Yichun lithium mine after license expiry                 | POSCO Future M +8.3%, L&F +10% |         |
| T1      |      validation | 2025-08-11 | Samsung SDI +3.2%, LGES +2.8%, KOSPI -0.1%                             | same                           |         |
| T2      |        4B-watch | 2025-08    | lithium had fallen up to 90% from 2022 peak; license renewal possible  | 4B                             |         |
| T3      |   Stage3-Yellow | N/A        | lithium price durability / cathode ASP / margin recovery not confirmed | 보류                             |         |

이 case는 cyclical success다. CATL의 Yichun lithium mine license가 만료되어 생산이 중단되자 lithium supply squeeze 기대가 생겼고, POSCO Future M은 +8.3%, L&F는 +10% 상승했다. 삼성SDI와 LGES도 각각 +3.2%, +2.8% 올랐고, KOSPI는 -0.1%였다. 다만 lithium price는 2022년 peak에서 최대 90% 하락한 뒤 반등한 상황이었고, CATL license renewal 가능성이 있었다. 따라서 이건 **Stage2 cyclical rebound**이지 Green이 아니다. ([월스트리트저널][4])

```json
{
  "case_id": "r3_loop17_lithium_rebound_posco_future_m_lnf",
  "symbols": "003670/066970/006400/373220",
  "best_trigger": "T0/T2",
  "best_trigger_type": "cyclical_Stage2_lithium_rebound",
  "trigger_date": "2025-08-11",
  "catalyst": "CATL_Yichun_lithium_mine_license_expiry_and_suspension",
  "posco_future_m_event_return_pct": 8.3,
  "lnf_event_return_pct": 10,
  "samsung_sdi_event_return_pct": 3.2,
  "lges_event_return_pct": 2.8,
  "kospi_same_context_pct": -0.1,
  "lithium_price_drawdown_from_2022_peak_pct": "up_to_90",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "lithium_price_sustained_rebound",
    "CATL_license_nonrenewal",
    "cathode_ASP_recovery",
    "inventory_valuation_gain",
    "customer_volume",
    "margin_recovery"
  ],
  "trigger_outcome_label": "cyclical_lithium_stage2_not_green"
}
```

---

## Case E — Samsung SDI all-solid-state battery timeline

```text
symbol = 006400
case_type = Stage2 / Stage3-Yellow candidate
archetype = SOLID_STATE_TIMELINE_STAGE2_YELLOW_CANDIDATE
```

| trigger |                    type | date       | 당시 공개 evidence                                                              | 가격 anchor                        | outcome |
| ------- | ----------------------: | ---------- | --------------------------------------------------------------------------- | -------------------------------- | ------- |
| T0      |         Stage2 evidence | 2024-03-07 | Samsung SDI plans all-solid-state mass production from 2027                 | +11% to 405,500 won, KOSPI +0.3% |         |
| T1      |              validation | 2024-03-07 | larger cylindrical batteries by 2025, LFP by 2026                           | same                             |         |
| T2      | Stage3-Yellow candidate | 2024~2027  | technology roadmap and first-mover possibility                              | no customer revenue              |         |
| T3      |                4B-watch | 2024~      | solid-state ASP, luxury-only initial market, yield, commercialization delay | 4B                               |         |
| T4      |            Stage3-Green | N/A        | customer adoption / pilot / revenue not confirmed                           | 보류                               |         |

Samsung SDI의 all-solid-state timeline은 기술 roadmap trigger로는 강했다. 전고체 battery 2027년 양산 계획과 2025년 대형 cylindrical, 2026년 LFP 계획이 제시되자 주가는 장중 +11%, 405,500원까지 올랐고 KOSPI는 +0.3%였다. 하지만 이건 아직 제품 매출이 아니라 기술 timeline이다. 그래서 Yellow 후보는 가능하지만, Green은 customer adoption, pilot yield, ASP/margin이 필요하다. ([월스트리트저널][5])

```json
{
  "case_id": "r3_loop17_samsung_sdi_solid_state_timeline",
  "symbol": "006400",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage3-Yellow_candidate_solid_state_timeline",
  "trigger_date": "2024-03-07",
  "event_return_pct": 11,
  "event_price_krw": 405500,
  "kospi_same_context_pct": 0.3,
  "solid_state_mass_production_target": 2027,
  "large_cylindrical_mass_production_target": 2025,
  "lfp_mass_production_target": 2026,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_green_gate_missing": [
    "pilot_yield",
    "customer_adoption",
    "solid_state_ASP",
    "luxury_EV_order_volume",
    "mass_production_cost",
    "actual_revenue"
  ],
  "trigger_outcome_label": "solid_state_stage2_yellow_candidate_not_green"
}
```

---

## Case F — LGES IRA AMPC earnings

```text
symbol = 373220
case_type = evidence good but policy-credit 4B
archetype = IRA_AMPC_EARNINGS_WITH_POLICY_4B
```

| trigger |            type | date       | 당시 공개 evidence                                              | 가격 anchor         | outcome |
| ------- | --------------: | ---------- | ----------------------------------------------------------- | ----------------- | ------- |
| T0      | Stage2 earnings | 2025-07-07 | Q2 OP 492B won, +152% YoY, above consensus                  | shares +2.4%      |         |
| T1      |   4B validation | 2025-07-07 | sales -9.7%; excluding AMPC, OP only 1.4B won, margin 0.03% | policy-dependency |         |
| T2      |        4B-watch | 2025~      | EV subsidy changes, tariff risk, EV demand slowdown         | no OHLC           |         |
| T3      |   Stage3-Yellow | N/A        | non-credit margin and utilization recovery not confirmed    | 보류                |         |

LGES Q2 earnings는 겉으로는 좋아 보인다. OP는 492B won으로 +152% YoY였고 주가도 +2.4% 올랐다. 하지만 매출은 -9.7%였고, AMPC를 제외하면 OP는 1.4B won, operating margin은 0.03%에 불과했다. 이건 **실적 개선이 정책 credit에 기대고 있다**는 뜻이다. 따라서 Stage2 earnings evidence는 맞지만, Green은 non-credit operating margin과 EV/ESS utilization이 확인되어야 한다. ([Financial Times][6])

```json
{
  "case_id": "r3_loop17_lges_ira_ampc_earnings",
  "symbol": "373220",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_earnings_with_policy_credit_4B",
  "trigger_date": "2025-07-07",
  "operating_profit_q2_2025_krw_bn": 492,
  "operating_profit_yoy_pct": 152,
  "sales_yoy_pct": -9.7,
  "operating_profit_ex_ampc_krw_bn": 1.4,
  "operating_margin_ex_ampc_pct": 0.03,
  "event_return_pct": 2.4,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "non_credit_operating_margin",
    "EV_line_utilization",
    "ESS_revenue_mix",
    "AMPC_durability",
    "tariff_policy_stability"
  ],
  "trigger_outcome_label": "earnings_good_but_policy_credit_4B"
}
```

---

## Case G — Samsung SDI capital raise / dilution 4B

```text
symbol = 006400
case_type = 4B capital raise dilution
archetype = CAPITAL_RAISE_DILUTION_4B
```

| trigger |            type | date       | 당시 공개 evidence                                               | 가격 anchor                    | outcome |
| ------- | --------------: | ---------- | ------------------------------------------------------------ | ---------------------------- | ------- |
| T0      |      4B trigger | 2025-03~04 | Samsung SDI plans 11.821M new shares to raise 2T won / $1.4B | stock down YTD               |         |
| T1      |      validation | 2025-04-09 | offering price cut 14%, 169,200 won → 146,200 won            | Samsung SDI -1%, KOSPI -0.5% |         |
| T2      |        4B-watch | 2025       | proceeds for GM JV, Hungary expansion, capex funding         | dilution                     |         |
| T3      | Stage3 recovery | N/A        | capex ROI / utilization / margin not confirmed               | 보류                           |         |

Samsung SDI capital raise는 “성장투자라도 dilution 4B”의 대표 case다. 2조원, 약 $1.4B 규모의 신주발행 가격을 169,200원에서 146,200원으로 14% 낮췄고, 주가는 당일 -1%, KOSPI는 -0.5%였다. 주가는 YTD -29.5% 상태였다. 자금 용도는 GM JV와 Hungary capacity expansion 등 성장투자였지만, EV 수요가 약한 구간에서 증자는 4B로 봐야 한다. ([Reuters][7])

```json
{
  "case_id": "r3_loop17_samsung_sdi_capital_raise_dilution",
  "symbol": "006400",
  "best_trigger": "T0/T2",
  "best_trigger_type": "4B_capital_raise_dilution",
  "trigger_date": "2025-04-09",
  "capital_raise_krw_trn": 2.0,
  "capital_raise_usd_bn": 1.4,
  "new_shares_count": 11821000,
  "offering_price_old_krw": 169200,
  "offering_price_new_krw": 146200,
  "offering_price_cut_pct": 14,
  "event_return_pct": -1,
  "kospi_same_context_pct": -0.5,
  "ytd_return_context_pct": -29.5,
  "use_of_proceeds": [
    "US_GM_joint_venture",
    "Hungary_factory_expansion",
    "battery_capacity_capex"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "recovery_gate_missing": [
    "capex_ROI",
    "factory_utilization",
    "GM_JV_volume",
    "Hungary_margin",
    "EV_demand_recovery"
  ],
  "trigger_outcome_label": "capital_raise_4B"
}
```

---

## Case H — POSCO / MinRes lithium JV

```text
symbol = 005490 / POSCO battery-material readthrough
case_type = Stage2 upstream lithium supply no direct price
archetype = UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE
```

| trigger |                    type | date       | 당시 공개 evidence                                                       | 가격 anchor                              | outcome |
| ------- | ----------------------: | ---------- | -------------------------------------------------------------------- | -------------------------------------- | ------- |
| T0      | Stage2 strategic supply | 2025-11-11 | POSCO to buy 30% stake in part of MinRes lithium business for $765M  | MinRes +10.8%, POSCO price unavailable |         |
| T1      |              validation | 2025-11-11 | POSCO gains effective 15% stakes in Wodgina and Mt Marion mines      | no KRX price                           |         |
| T2      |                4B-watch | 2025       | lithium price slump, MinRes debt pressure, upstream price volatility | 4B                                     |         |
| T3      |           Stage3-Yellow | N/A        | offtake economics / lithium recovery / POSCO margin unavailable      | 보류                                     |         |

POSCO/MinRes deal은 upstream supply Stage2다. POSCO는 MinRes lithium business 일부 30% stake를 $765M에 인수해 Wodgina와 Mt Marion lithium mines에 각각 effective 15% interest를 확보한다. MinRes는 +10.8% 급등했지만, POSCO KRX direct price anchor는 확보하지 못했다. 이건 battery-material chain에서 strategic raw-material 확보로 볼 수 있지만, lithium 가격이 여전히 약한 구간이고 offtake/margin이 확인되지 않아 Green은 아니다. ([Reuters][8])

```json
{
  "case_id": "r3_loop17_posco_minres_lithium_jv",
  "symbol": "005490_battery_material_readthrough",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_upstream_lithium_supply_no_direct_price",
  "trigger_date": "2025-11-11",
  "deal_value_usd_mn": 765,
  "stake_in_minres_lithium_business_pct": 30,
  "effective_stakes": [
    "15pct_Wodgina",
    "15pct_Mt_Marion"
  ],
  "minres_event_return_pct": 10.8,
  "direct_posco_price_anchor": "price_data_unavailable_after_deep_search",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "offtake_terms",
    "lithium_price_recovery",
    "hydroxide_conversion_margin",
    "POSCO_materials_revenue_link",
    "capital_intensity",
    "full_OHLC_MFE_MAE"
  ],
  "trigger_outcome_label": "Stage2_upstream_lithium_supply_not_Green"
}
```

---

# 6. Trigger별 실제 가격경로 검증 요약

이번 R3 Loop 17은 full OHLC가 없으므로, 아래 표는 **reported event anchor 기준**이다.

| case                         | best trigger |             event return / price |        market-relative | full MFE/MAE | outcome                                      |
| ---------------------------- | -----------: | -------------------------------: | ---------------------: | ------------ | -------------------------------------------- |
| Samsung SDI ESS LFP          |           T1 |                            +6.1% |  +6.2pp vs KOSPI -0.1% | unavailable  | excellent Stage2-Actionable                  |
| LGES Ford cancellation       |           T0 |                            -7.6% |  -6.2pp vs KOSPI -1.4% | unavailable  | 4C contract break                            |
| SK On ESS pivot              |        T0/T2 |                price unavailable |                    N/A | unavailable  | Stage2 pivot, parent readthrough unavailable |
| POSCO Future M / L&F lithium |           T0 |                     +8.3% / +10% |  strong vs KOSPI -0.1% | unavailable  | cyclical Stage2                              |
| Samsung SDI solid-state      |           T0 |              +11% to 405,500 won | +10.7pp vs KOSPI +0.3% | unavailable  | Yellow candidate                             |
| LGES AMPC earnings           |           T0 |                            +2.4% |            unavailable | unavailable  | evidence good but policy-credit 4B           |
| Samsung SDI capital raise    |           T1 |                 -1%, KOSPI -0.5% |                 -0.5pp | unavailable  | dilution 4B                                  |
| POSCO / MinRes lithium       |           T0 | MinRes +10.8%, POSCO unavailable |                    N/A | unavailable  | Stage2 no-price                              |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
가장 좋은 Stage2:
1. Samsung SDI ESS LFP contract
2. Samsung SDI solid-state battery timeline
3. POSCO Future M / L&F lithium rebound
4. Open-ended: SK On ESS pivot, but unlisted
5. POSCO / MinRes upstream lithium, but direct KRX price unavailable
```

## Stage2-Actionable entry 성과

```text
Stage2-Actionable:
- Samsung SDI ESS LFP: contract value + price reaction + EV line conversion.
- Samsung SDI solid-state: +11% reaction, but technology timeline not revenue.
- POSCO Future M / L&F lithium rebound: strong event return, but cyclical.

Actionable 금지:
- LGES Ford/Freudenberg cancellations.
- Samsung SDI capital raise.
- LGES AMPC earnings if non-credit margin remains near zero.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Samsung SDI ESS if customer/delivery/margin confirmed.
- Samsung SDI solid-state if pilot yield, customer adoption and ASP/margin confirmed.
- POSCO Future M / L&F if lithium rebound persists and cathode ASP/margin recover.
- SK On if ESS revenue/margin and parent value contribution become visible.
```

## Stage3-Green

```text
이번 R3 Loop 17에서 확정 Green 없음.

이유:
- ESS는 강하지만 delivery starts 2027, customer undisclosed.
- solid-state는 timeline일 뿐 revenue가 없다.
- lithium rebound는 supply/license event라 cyclical이다.
- LGES contract cancellation and Samsung SDI dilution 4B가 sector-wide risk를 보여준다.
- SK On and POSCO upstream cases lack direct KRX price anchors.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Samsung SDI ESS LFP deal
- LGES Ford cancellation / Freudenberg cancellation
- POSCO Future M / L&F lithium rebound
- Samsung SDI solid-state timeline
- Samsung SDI capital raise 4B

Stage2_promote_candidate:
- Samsung SDI ESS LFP
- Samsung SDI solid-state timeline
- POSCO Future M / L&F lithium rebound, but cyclical
- SK On ESS pivot, if parent readthrough and margin appear

Stage3-Yellow candidate:
- Samsung SDI ESS with delivery/margin
- Samsung SDI solid-state with customer adoption/pilot yield
- POSCO Future M/L&F with sustained lithium/cathode margin recovery

false_positive_score:
- LGES earnings promoted to Green while AMPC-ex margin is 0.03%
- lithium rebound promoted to Green without sustained price recovery
- solid-state timeline promoted to Green without revenue
- SK On ESS pivot promoted without parent value / margin

evidence_good_but_price_failed:
- Samsung SDI capital raise / dilution
- LGES AMPC earnings if judged without policy-credit adjustment

cyclical_success:
- POSCO Future M / L&F lithium rebound

event_premium:
- Samsung SDI solid-state +11%
- Samsung SDI ESS LFP +6.1%

thesis_break:
- LGES Ford/Freudenberg cancellations

4B-watch:
- EV subsidy rollback
- contract cancellations
- AMPC dependency
- lithium price reversal
- capital raise dilution
- ESS line conversion execution
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
ESS_LFP_contract_visibility,+5,"ESS 계약금액과 가격반응이 닫히면 Stage2-Actionable","Samsung SDI"
line_conversion_utilization,+5,"EV line을 ESS로 전환해 가동률 방어하면 점수 상승","Samsung SDI, SK On"
contract_cancellation_risk,+5,"OEM 계약 취소는 4C 핵심","LGES"
lithium_price_inventory_rebound,+4,"소재주는 lithium price와 재고평가가 단기 가격 trigger","POSCO Future M, L&F"
solid_state_commercialization_timeline,+4,"전고체 timeline은 Yellow 후보 가능","Samsung SDI"
non_credit_operating_margin,+5,"AMPC 제외 margin이 진짜 이익 체력","LGES"
upstream_lithium_supply_control,+4,"광산/원료 지분은 장기 supply-chain 점수","POSCO"
market_relative_return,+4,"KOSPI 대비 event alpha는 trigger quality","Samsung SDI, POSCO Future M/L&F"
```

## 내릴 축

```csv
axis,delta,reason,cases
EV_contract_backlog_without_cancellation_check,-5,"계약잔고 숫자만 보고 4C risk 무시 금지","LGES"
AMPC_credit_dependency_ignored,-5,"AMPC 제외 margin이 거의 없으면 Green 금지","LGES"
ESS_headline_without_customer_margin,-4,"ESS 계약도 customer/margin/delivery 전에는 Green 금지","Samsung SDI, SK On"
solid_state_timeline_without_revenue,-5,"전고체 timeline만으로 Green 금지","Samsung SDI"
lithium_rebound_without_durability,-5,"CATL license event는 지속성 없으면 cyclical","POSCO Future M, L&F"
capital_raise_dilution_ignored,-5,"증자/발행가 인하 무시하면 false positive","Samsung SDI"
unlisted_subsidiary_readthrough_overstated,-4,"SK On event를 parent valuation으로 과대반영 금지","SK On/SK Innovation"
```

---

# 10. Stage2-Actionable 승격 조건

R3 Loop 17 shadow rule:

```text
R3에서 Stage2 evidence가 아래 중 4개 이상이면 Stage2-Actionable로 승격한다.

1. event return +5% 이상
2. market-relative return +5pp 이상
3. 계약금액 / 공급량 / policy credit / 생산 timeline이 명확하다
4. EV line utilization 회복 또는 ESS 전환으로 연결된다
5. customer/delivery start/margin gate가 식별 가능하다
6. contract cancellation / subsidy rollback / dilution / lithium reversal 4B가 없다
7. 소재주는 commodity price rebound가 ASP/margin으로 연결될 가능성이 있다
```

적용:

```text
Samsung SDI ESS:
1,2,3,4,5 충족 → Stage2-Actionable.

Samsung SDI solid-state:
1,2,3 충족, 5 일부. revenue 없음 → Stage2 / Yellow candidate.

POSCO Future M/L&F lithium:
1,2,7 충족. commodity durability 없음 → cyclical Stage2.

LGES Ford cancellation:
contract cancellation 4C → 승격 금지.

LGES AMPC:
3 충족, but AMPC dependency → Green 금지.

SK On:
3,4 충족, direct price 없음 → Stage2 only.

Samsung SDI capital raise:
dilution 4B → 승격 금지.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
Stage2-Actionable 이후 아래 중 2개 이상이 추가로 닫히면 Yellow.

1. binding customer and delivery schedule
2. ESS or EV line utilization recovery
3. gross margin or non-credit operating margin improvement
4. sustained lithium/cathode ASP recovery
5. solid-state pilot yield and customer adoption
6. capex/dilution overhang resolved
7. policy-credit dependency reduced
```

Yellow 후보:

```text
Samsung SDI ESS:
customer name, delivery schedule, ESS margin 확인 시 Yellow.

Samsung SDI solid-state:
pilot yield and customer adoption 확인 시 Yellow.

POSCO Future M/L&F:
lithium rebound 지속 + cathode ASP/margin 회복 시 Yellow.

SK On:
ESS production start + parent value contribution 확인 시 Yellow.

LGES:
replacement orders and non-credit margin recovery 확인 전까지 Yellow 금지.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- ESS/EV contract is final and delivery starts.
- factory utilization and margin recover.
- non-credit operating margin is positive and durable.
- lithium/cathode rebound is not just inventory valuation but ASP/margin.
- solid-state moves from timeline to customer revenue.
- capex/dilution and contract-cancellation risk are resolved.
- full-window MFE/MAE is favorable.
```

이번 R3 Loop 17에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + customer/margin/utilization/non-credit-profit gates not closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- EV contract cancellation.
- ESS contract before customer/margin/delivery.
- AMPC-driven profit with weak underlying margin.
- capital raise / offering price cut.
- lithium price rebound from temporary mine/license event.
- unlisted subsidiary event over-read into parent.
- solid-state timeline without revenue.
```

적용:

```text
LGES:
Ford/Freudenberg cancellation = 4C.

Samsung SDI:
ESS good, but customer/margin 4B.
Solid-state +11%, but timeline/revenue 4B.
Capital raise = dilution 4B.

POSCO Future M/L&F:
lithium rebound good, but cyclical 4B.

LGES AMPC:
credit-dependent earnings 4B.

SK On:
ESS pivot good, but unlisted and parent readthrough 4B.
```

---

# 14. 4C hard gate 조건

```text
R3 4C:
- large OEM contract cancellation
- repeated contract cancellation across customers
- factory utilization thesis break
- EV subsidy rollback causing permanent demand reset
- capex/dilution spiral
- safety recall or fire defect with compensation
```

이번 R3 Loop 17 hard/strong 4C:

```text
LGES Ford + Freudenberg cancellations = strong_4C_contract_quality_break
```

Strong 4B:

```text
- Samsung SDI capital raise
- LGES AMPC dependency
- lithium rebound durability risk
- SK On Ford JV split / OP loss
- ESS line conversion execution
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R3 production 설계 원칙:

```text
1. EV 계약잔고와 계약취소 risk를 분리한다.
2. ESS 전환은 utilization 회복 trigger로 별도 점수화한다.
3. AMPC/IRA credit은 underlying margin과 분리한다.
4. 전고체 timeline은 revenue 전까지 Green 금지한다.
5. lithium rebound는 commodity cyclical로 취급하고 duration을 본다.
6. 증자/발행가 인하/dilution은 4B overlay로 즉시 병기한다.
7. unlisted SK On event는 parent readthrough를 과대평가하지 않는다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_252.md 요약

```md
# R3 Loop 17. Secondary Battery / EV / Green Trigger-level Price Validation

이번 라운드는 R3 Loop 17 trigger-level validation 라운드다.

핵심 결론:
- Samsung SDI ESS LFP deal is the cleanest Stage2-Actionable. Samsung SDI America signed a 2T won+ / $1.36B LFP ESS battery deal with a U.S. customer. Shares rose as much as 6.1% while KOSPI fell 0.1%. Existing U.S. EV lines will be converted for ESS. Green requires customer disclosure, delivery execution and LFP margin.
- LG Energy Solution contract cancellations are strong 4C. Ford cancelled a 9.6T won / $6.5B EV battery supply deal, and LGES fell 7.6% while KOSPI fell 1.4%. Freudenberg also cancelled a 3.9T won / $2.7B contract. Total expected revenue lost was around 13.5T won in less than 10 days.
- SK On ESS pivot is Stage2 with parent-readthrough unavailable. It signed a Flatiron Energy deal for up to 7.2GWh LFP ESS batteries from 2026 to 2030, while later ending the Ford U.S. JV. SK On is unlisted and Q3 2025 OP loss was 124.8B won.
- POSCO Future M / L&F lithium rebound is cyclical Stage2. CATL’s Yichun mine suspension drove POSCO Future M +8.3% and L&F +10%, but lithium had fallen up to 90% from its 2022 peak and license renewal remained possible.
- Samsung SDI solid-state timeline is Stage2 / Yellow candidate. Shares rose 11% to 405,500 won after it set 2027 all-solid-state mass production, 2025 larger cylindrical and 2026 LFP timelines. Green requires pilot yield, customer adoption and revenue.
- LGES AMPC earnings are evidence-good but policy-credit 4B. Q2 OP was 492B won, +152% YoY, but sales fell 9.7%; excluding AMPC, OP was only 1.4B won and margin 0.03%.
- Samsung SDI capital raise is dilution 4B. It cut its 2T won share-sale price by 14% from 169,200 won to 146,200 won after stock weakness.
- POSCO / MinRes lithium JV is upstream Stage2 without direct KRX price validation. POSCO paid $765M for a stake giving effective 15% interests in Wodgina and Mt Marion; MinRes rose 10.8%.

Main calibration:
- Raise ESS_LFP_contract_visibility, line_conversion_utilization, contract_cancellation_risk, lithium_price_inventory_rebound, solid_state_commercialization_timeline, non_credit_operating_margin, upstream_lithium_supply_control, market_relative_return.
- Lower EV_contract_backlog_without_cancellation_check, AMPC_credit_dependency_ignored, ESS_headline_without_customer_margin, solid_state_timeline_without_revenue, lithium_rebound_without_durability, capital_raise_dilution_ignored, unlisted_subsidiary_readthrough_overstated.
```

## docs/checkpoints/checkpoint_28a_round252_r3_loop17.md 요약

```md
# Checkpoint 28A Round 252 R3 Loop 17 Trigger-level Calibration

## 반영 내용
- R3 Loop 17 trigger-level validation을 수행했다.
- Samsung SDI ESS LFP, LGES Ford/Freudenberg cancellations, SK On ESS pivot, POSCO Future M/L&F lithium rebound, Samsung SDI solid-state timeline, LGES AMPC earnings, Samsung SDI capital raise, POSCO/MinRes lithium JV를 검토했다.
- full adjusted OHLC는 확보하지 못했으므로 Reuters / FT / WSJ / MarketWatch / AP reported event return과 event price anchor를 사용했다.
- MFE/MAE는 조작하지 않고 price_data_unavailable_after_deep_search로 분리했다.

## 핵심 보정
- ESS line conversion can promote Stage2 when contract value and price reaction are clear.
- EV contract cancellation is a hard 4C contract-quality break.
- AMPC/IRA credit must be separated from underlying operating margin.
- Solid-state timelines are Yellow candidates only after pilot yield and customer adoption.
- Lithium rebound is cyclical unless price durability and cathode margin recovery are proven.
- Capital raise and offering price cuts are 4B dilution overlays.
```

## data/e2r_case_library/cases_r3_loop17_round252.jsonl 초안

```jsonl
{"case_id":"r3_loop17_samsung_sdi_ess_lfp","symbol":"006400","company_name":"Samsung SDI","case_type":"Stage2_Actionable_ESS_LFP_line_conversion","primary_archetype":"ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2025-12-09","contract_value_krw_trn":">2.0","contract_value_usd_bn":1.36,"delivery_period":"3_years_from_2027","event_return_pct":6.1,"kospi_same_context_pct":-0.1,"market_relative_return_pp":6.2,"line_conversion":"existing_US_EV_lines_to_ESS_LFP","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_ESS_pivot","notes":"ESS LFP contract and line conversion are strong, but customer/margin/delivery remain gates."}
{"case_id":"r3_loop17_lges_ford_freudenberg_cancellation","symbol":"373220","company_name":"LG Energy Solution","case_type":"4C_EV_contract_cancellation","primary_archetype":"EV_CONTRACT_CANCELLATION_4C","best_trigger":"T0/T3","stage_candidate":"4C","price_validation":{"ford_cancellation_date":"2025-12-17","ford_contract_value_krw_trn":9.6,"ford_contract_value_usd_bn":6.5,"ford_event_return_pct":-7.6,"kospi_same_context_pct":-1.4,"market_relative_return_pp":-6.2,"freudenberg_cancellation_date":"2025-12-26","freudenberg_contract_value_krw_trn":3.9,"freudenberg_contract_value_usd_bn":2.7,"expected_revenue_loss_krw_trn":13.5,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"hard_4C_contract_quality_break","notes":"Repeated OEM/customer contract cancellations impair backlog quality and utilization thesis."}
{"case_id":"r3_loop17_sk_on_ess_flatiron_ford_jv","symbol":"096770_readthrough","company_name":"SK On / SK Innovation readthrough","case_type":"Stage2_ESS_pivot_with_4B_restructuring","primary_archetype":"SK_ON_ESS_PIVOT_STAGE2_WITH_PARENT_READTHROUGH","best_trigger":"T0/T3","stage_candidate":"Stage2 + 4B-watch","price_validation":{"flatiron_deal_date":"2025-09-03","ess_volume_gwh":7.2,"supply_period":"2026-2030","technology":"LFP_ESS","georgia_line_conversion":true,"ford_jv_split_date":"2025-12-11","original_ford_sk_investment_usd_bn":11.4,"sk_on_q3_2025_operating_loss_krw_bn":124.8,"direct_price_anchor":"price_data_unavailable_unlisted_subsidiary"},"score_price_alignment":"Stage2_ESS_pivot_with_parent_readthrough_unavailable","notes":"ESS pivot is real, but SK On is unlisted and profitability/fixed-cost risk remains."}
{"case_id":"r3_loop17_lithium_rebound_posco_future_m_lnf","symbol":"003670/066970/006400/373220","company_name":"POSCO Future M / L&F / Samsung SDI / LGES","case_type":"cyclical_Stage2_lithium_rebound","primary_archetype":"LITHIUM_PRICE_REBOUND_CYCLICAL_STAGE2","best_trigger":"T0/T2","stage_candidate":"cyclical Stage2","price_validation":{"trigger_date":"2025-08-11","catalyst":"CATL_Yichun_lithium_mine_license_expiry_and_suspension","posco_future_m_event_return_pct":8.3,"lnf_event_return_pct":10,"samsung_sdi_event_return_pct":3.2,"lges_event_return_pct":2.8,"kospi_same_context_pct":-0.1,"lithium_price_drawdown_from_2022_peak_pct":"up_to_90","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"cyclical_lithium_stage2_not_green","notes":"Lithium rebound moved materials stocks, but license renewal and oversupply make it cyclical, not Green."}
{"case_id":"r3_loop17_samsung_sdi_solid_state_timeline","symbol":"006400","company_name":"Samsung SDI","case_type":"Stage3_Yellow_candidate_solid_state_timeline","primary_archetype":"SOLID_STATE_TIMELINE_STAGE2_YELLOW_CANDIDATE","best_trigger":"T0/T3","stage_candidate":"Stage3-Yellow_candidate","price_validation":{"trigger_date":"2024-03-07","event_return_pct":11,"event_price_krw":405500,"kospi_same_context_pct":0.3,"solid_state_mass_production_target":2027,"large_cylindrical_mass_production_target":2025,"lfp_mass_production_target":2026,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"solid_state_stage2_yellow_candidate_not_green","notes":"Technology timeline caused strong rally, but customer adoption, yield and revenue remain missing."}
{"case_id":"r3_loop17_lges_ira_ampc_earnings","symbol":"373220","company_name":"LG Energy Solution","case_type":"Stage2_earnings_with_policy_credit_4B","primary_archetype":"IRA_AMPC_EARNINGS_WITH_POLICY_4B","best_trigger":"T0/T2","stage_candidate":"Stage2 + 4B-watch","price_validation":{"trigger_date":"2025-07-07","operating_profit_q2_2025_krw_bn":492,"operating_profit_yoy_pct":152,"sales_yoy_pct":-9.7,"operating_profit_ex_ampc_krw_bn":1.4,"operating_margin_ex_ampc_pct":0.03,"event_return_pct":2.4,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"earnings_good_but_policy_credit_4B","notes":"Headline profit improved but underlying margin excluding AMPC was nearly zero."}
{"case_id":"r3_loop17_samsung_sdi_capital_raise_dilution","symbol":"006400","company_name":"Samsung SDI","case_type":"4B_capital_raise_dilution","primary_archetype":"CAPITAL_RAISE_DILUTION_4B","best_trigger":"T0/T2","stage_candidate":"4B-watch","price_validation":{"trigger_date":"2025-04-09","capital_raise_krw_trn":2.0,"capital_raise_usd_bn":1.4,"new_shares_count":11821000,"offering_price_old_krw":169200,"offering_price_new_krw":146200,"offering_price_cut_pct":14,"event_return_pct":-1,"kospi_same_context_pct":-0.5,"ytd_return_context_pct":-29.5,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"capital_raise_4B","notes":"Growth capex funded by discounted share issuance is a dilution overlay."}
{"case_id":"r3_loop17_posco_minres_lithium_jv","symbol":"005490_battery_material_readthrough","company_name":"POSCO / MinRes lithium JV","case_type":"Stage2_upstream_lithium_supply_no_direct_price","primary_archetype":"UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE","best_trigger":"T0/T2","stage_candidate":"Stage2","price_validation":{"trigger_date":"2025-11-11","deal_value_usd_mn":765,"stake_in_minres_lithium_business_pct":30,"effective_stakes":["15pct_Wodgina","15pct_Mt_Marion"],"minres_event_return_pct":10.8,"direct_posco_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_upstream_lithium_supply_not_Green","notes":"Upstream lithium control is strategic, but direct KRX price, offtake terms and margin are missing."}
```

## data/e2r_trigger_calibration/triggers_r3_loop17_round252.jsonl 초안

```jsonl
{"trigger_id":"r3l17_samsung_sdi_ess_T1","case_id":"r3_loop17_samsung_sdi_ess_lfp","trigger_type":"Stage2-Actionable_ESS_LFP_contract","trigger_date":"2025-12-09","event_return_pct":6.1,"market_relative_pp":6.2,"trigger_outcome_label":"excellent_stage2_actionable_ESS_pivot","promote_to":"Stage2-Actionable"}
{"trigger_id":"r3l17_lges_ford_cancel_T0","case_id":"r3_loop17_lges_ford_freudenberg_cancellation","trigger_type":"4C_contract_cancellation","trigger_date":"2025-12-17","event_return_pct":-7.6,"market_relative_pp":-6.2,"trigger_outcome_label":"hard_4C_contract_quality_break","promote_to":"4C"}
{"trigger_id":"r3l17_lges_freudenberg_cancel_T2","case_id":"r3_loop17_lges_ford_freudenberg_cancellation","trigger_type":"4C_contract_cancellation_escalation","trigger_date":"2025-12-26","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"contract_cancellation_escalation","promote_to":"4C"}
{"trigger_id":"r3l17_sk_on_flatiron_T0","case_id":"r3_loop17_sk_on_ess_flatiron_ford_jv","trigger_type":"Stage2_ESS_pivot","trigger_date":"2025-09-03","event_return_pct":"price_data_unavailable_unlisted_subsidiary","trigger_outcome_label":"Stage2_ESS_pivot_parent_readthrough_unavailable","promote_to":"Stage2"}
{"trigger_id":"r3l17_lithium_rebound_T0","case_id":"r3_loop17_lithium_rebound_posco_future_m_lnf","trigger_type":"cyclical_Stage2_lithium_rebound","trigger_date":"2025-08-11","event_return_pct":"POSCO_Future_M_+8.3_L&F_+10","trigger_outcome_label":"cyclical_lithium_stage2_not_green","promote_to":"Stage2_cyclical"}
{"trigger_id":"r3l17_samsung_sdi_solid_state_T0","case_id":"r3_loop17_samsung_sdi_solid_state_timeline","trigger_type":"Stage3-Yellow_candidate_solid_state_timeline","trigger_date":"2024-03-07","event_return_pct":11,"entry_price_krw":405500,"trigger_outcome_label":"solid_state_yellow_candidate_not_green","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r3l17_lges_ampc_T0","case_id":"r3_loop17_lges_ira_ampc_earnings","trigger_type":"Stage2_earnings_policy_credit_4B","trigger_date":"2025-07-07","event_return_pct":2.4,"trigger_outcome_label":"earnings_good_but_policy_credit_4B","promote_to":"Stage2+4B"}
{"trigger_id":"r3l17_samsung_sdi_capital_raise_T1","case_id":"r3_loop17_samsung_sdi_capital_raise_dilution","trigger_type":"4B_capital_raise_dilution","trigger_date":"2025-04-09","event_return_pct":-1,"trigger_outcome_label":"capital_raise_dilution_4B","promote_to":"4B-watch"}
{"trigger_id":"r3l17_posco_minres_lithium_T0","case_id":"r3_loop17_posco_minres_lithium_jv","trigger_type":"Stage2_upstream_lithium_supply_no_price","trigger_date":"2025-11-11","event_return_pct":"MinRes_+10.8_POSCO_unavailable","trigger_outcome_label":"Stage2_upstream_lithium_no_direct_price","promote_to":"Stage2"}
```

## data/sector_taxonomy/score_weight_profiles_round252_r3_loop17_v1.csv 초안

```csv
archetype,ess_lfp_contract_visibility,line_conversion_utilization,contract_cancellation_risk,lithium_price_inventory_rebound,solid_state_commercialization_timeline,non_credit_operating_margin,upstream_lithium_supply_control,market_relative_return,ev_contract_backlog_without_cancellation_check_penalty,ampc_credit_dependency_ignored_penalty,ess_headline_without_customer_margin_penalty,solid_state_timeline_without_revenue_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE,+5,+5,+1,+0,+1,+3,+0,+4,-2,-2,-4,-1,ESS LFP contract with +6.1% event return,customer/margin/delivery missing,customer+margin+delivery,Samsung SDI.
EV_CONTRACT_CANCELLATION_4C,+0,+0,+5,+0,+0,+2,+0,+3,-5,-1,-1,-1,large OEM contract cancellations,utilization break,Replacement orders/utilization recovery,LGES.
SK_ON_ESS_PIVOT_STAGE2_WITH_PARENT_READTHROUGH,+4,+5,+2,+0,+0,+3,+0,+1,-2,-2,-4,-1,ESS pivot with unlisted subsidiary,parent readthrough missing,ESS revenue+margin+parent contribution,SK On.
LITHIUM_PRICE_REBOUND_CYCLICAL_STAGE2,+0,+0,+1,+5,+0,+2,+3,+4,-1,-1,-1,-1,lithium mine suspension triggered materials rally,durability missing,lithium price sustained+cathode margin,POSCO Future M/L&F.
SOLID_STATE_TIMELINE_STAGE2_YELLOW_CANDIDATE,+1,+1,+0,+0,+5,+2,+0,+5,-1,-1,-1,-5,strong technology timeline rally,revenue/yield missing,pilot yield+customer adoption,Samsung SDI.
IRA_AMPC_EARNINGS_WITH_POLICY_4B,+0,+1,+1,+0,+0,+5,+0,+1,-2,-5,-1,-1,headline profit credit-dependent,underlying margin missing,non-credit margin+utilization,LGES.
CAPITAL_RAISE_DILUTION_4B,+1,+2,+1,+0,+0,+2,+0,-2,-1,-1,-1,-1,discounted share issuance,dilution/capex ROI missing,capex ROI+utilization,Samsung SDI.
UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE,+0,+0,+1,+3,+0,+2,+5,+1,-1,-1,-1,-1,upstream lithium stake,POSCO direct price unavailable,offtake+margin+lithium recovery,POSCO/MinRes.
```

---

# 이번 R3 Loop 17 결론

```text
1. Samsung SDI ESS LFP는 R3의 가장 좋은 Stage2-Actionable이다.
   2T won+ 계약, +6.1%, KOSPI -0.1%, EV line → ESS 전환이 닫혔다.

2. LGES Ford/Freudenberg cancellation은 강한 4C다.
   Ford 9.6T won, Freudenberg 3.9T won 계약이 취소됐고, LGES는 Ford trigger에서 -7.6%였다.

3. SK On ESS pivot은 Stage2지만 parent readthrough가 불완전하다.
   Flatiron 7.2GWh ESS 계약은 좋지만 SK On은 비상장이고 Ford JV split/OP loss가 있다.

4. POSCO Future M / L&F lithium rebound는 cyclical Stage2다.
   +8.3% / +10%는 강하지만 CATL license issue와 lithium oversupply risk가 있다.

5. Samsung SDI solid-state timeline은 Stage3-Yellow 후보다.
   +11% 반응은 좋지만 pilot yield/customer adoption/revenue 전에는 Green 금지다.

6. LGES AMPC earnings는 evidence good but policy-credit 4B다.
   OP +152%지만 AMPC 제외 margin이 0.03%면 Green이 아니다.

7. Samsung SDI capital raise는 dilution 4B다.
   2T won 증자, 발행가 14% 인하, YTD -29.5% context는 dilution overlay다.

8. POSCO / MinRes lithium JV는 upstream supply Stage2다.
   $765M 전략지분은 좋지만 POSCO direct price와 offtake/margin이 없다.
```

한 문장으로 압축하면:

> **R3 Loop 17에서 배운 핵심은 “EV/배터리/친환경”이라는 테마명이 아니라, ESS 계약의 고객·마진·가동률, EV 계약취소 risk, AMPC 제외 실제 margin, lithium rebound 지속성, 전고체 revenue conversion, 증자 dilution을 따로 봐야 한다는 것이다. Stage2를 너무 보수적으로 두면 Samsung SDI ESS 같은 entry를 놓치고, headline만 믿고 Green을 주면 LGES 계약취소·AMPC 의존·전고체 timeline·lithium 일시반등에 false positive가 난다.**

다음 순서는 **R4 Loop 17 — 소재·스프레드·전략자원**이다.

[1]: https://www.reuters.com/world/asia-pacific/samsung-sdis-us-unit-signs-14-bln-lfp-battery-deal-us-customer-2025-12-09/ "https://www.reuters.com/world/asia-pacific/samsung-sdis-us-unit-signs-14-bln-lfp-battery-deal-us-customer-2025-12-09/"
[2]: https://www.reuters.com/business/energy/shares-south-koreas-lges-drop-more-than-7-after-ford-cancels-ev-battery-deal-2025-12-18/ "https://www.reuters.com/business/energy/shares-south-koreas-lges-drop-more-than-7-after-ford-cancels-ev-battery-deal-2025-12-18/"
[3]: https://www.reuters.com/business/energy/south-koreas-sk-signs-energy-storage-battery-supply-deal-with-flatiron-energy-2025-09-03/ "https://www.reuters.com/business/energy/south-koreas-sk-signs-energy-storage-battery-supply-deal-with-flatiron-energy-2025-09-03/"
[4]: https://www.wsj.com/finance/commodities-futures/ev-battery-giant-catl-suspends-mining-project-67693725 "https://www.wsj.com/finance/commodities-futures/ev-battery-giant-catl-suspends-mining-project-67693725"
[5]: https://www.wsj.com/articles/samsung-sdi-rallies-as-it-sets-timeline-for-new-battery-production-ec7838dc "https://www.wsj.com/articles/samsung-sdi-rallies-as-it-sets-timeline-for-new-battery-production-ec7838dc"
[6]: https://www.ft.com/content/c8059c0c-b0a8-42dd-8b9c-2e0fb010ae13 "https://www.ft.com/content/c8059c0c-b0a8-42dd-8b9c-2e0fb010ae13"
[7]: https://www.reuters.com/markets/asia/samsung-sdi-cuts-stock-offering-price-by-14-2025-04-09/ "https://www.reuters.com/markets/asia/samsung-sdi-cuts-stock-offering-price-by-14-2025-04-09/"
[8]: https://www.reuters.com/business/energy/australias-minres-sell-30-lithium-jv-stake-posco-765-mln-2025-11-11/ "https://www.reuters.com/business/energy/australias-minres-sell-30-lithium-jv-stake-posco-765-mln-2025-11-11/"
