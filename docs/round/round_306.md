순서상 이번은 **R11 Loop 15 — 정책·지정학·재난·이벤트 trigger-level price validation 라운드**다.

이번 R11의 핵심은 “방산 좋다 / 정책 좋다 / 위기 수혜다”가 아니라, **정책 발표 → 실제 계약·예산·라이선스·수출통제·에너지 공급·노동 리스크·재난 비용** 중 어느 trigger가 실제 entry였고, 어느 trigger는 4B/4C였는지를 분리하는 것이다.

```text
round = R11 Loop 15
round_id = round_234
large_sector = POLICY_GEOPOLITICS_DISASTER_EVENT
method = trigger_level_backtest_v1
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R12 Loop 15
```

이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 30D/90D/180D/1Y window를 안정적으로 직접 추출하지 못했다. 따라서 full MFE/MAE는 만들지 않고 `price_data_unavailable_after_deep_search`로 둔다. 대신 Reuters/FT/WSJ/MarketWatch/AP/Barron’s가 보도한 **reported event return, contract value, market-relative return, ETF move, policy amount, strike-loss estimate, disaster damage, energy-route volume**을 trigger anchor로 쓴다. 계산 불가능한 MFE/MAE는 만들지 않는다.

---

# 1. 이번 라운드 대섹터

```text
R11 = 정책·지정학·재난·이벤트
```

R11의 core gate는 아래다.

```text
방산·지정학:
전쟁/위협 → 국방예산 → preferred supplier → signed contract → delivery → local production / tech transfer → margin

수출통제·무역정책:
정책 발표 → license change → 생산능력/업그레이드 제한 → margin/market-share 영향 → 대체 생산지 → relief license

정치 이벤트:
정치 shock → 환율/ETF/index reaction → 정책 continuity → 투자심리 → 소비/외국인 flow

에너지 지정학:
해협/전쟁 shock → 유가/환율 → KOSPI drawdown → alternative supply route → refinery/chemical margin

노동·사회정책:
파업예고 → 생산차질 가능성 → 정부중재/긴급중재 → 실제 생산손실 → supply-chain impact

재난:
사망/피해/특별재난지역 → 복구예산 → 보험/건설/인프라 수요 → 직접 비용 → hard trust gate
```

---

# 2. 대상 canonical archetype

```text
DEFENSE_EXPORT_BACKLOG_STAGE2_ACTIONABLE
GROUND_WEAPON_EXPORT_DELIVERY_STAGE2_YELLOW
CHIP_EXPORT_CONTROL_4C_WATCH
SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH
POLITICAL_SYSTEM_SHOCK_MARKET_4C
HORMUZ_ENERGY_SECURITY_4C_WITH_POLICY_RELIEF
NAVAL_SHIPBUILDING_GEOPOLITICAL_STAGE2_WITH_DILUTION_4B
NATURAL_DISASTER_RECOVERY_STAGE2_REFERENCE
```

---

# 3. deep sub-archetype

```text
Hanwha Aerospace:
- Romania K9 order
- $1B / 54 K9 / 36 K10 / ammunition
- shares +5% to record high
- defense backlog 5.1T won end-2021 → 30T won Mar-2024
- global howitzer export share >50%
- but share sale / dilution 4B possible

Hyundai Rotem:
- Poland K2 tank exports
- 18 K2 shipments to Poland in Q1 2024
- shares +9.3%, KOSPI -0.3%
- Q1 OP expected +85%
- second Poland contract $6.5B / 180 tanks
- local production / delivery / political-delay gate

Samsung / SK Hynix:
- U.S. revokes export authorizations for China fabs
- Samsung -2.3%, SK Hynix -4.4%, KOSPI -0.7%
- China fabs >1/3 Samsung DRAM, 30~40% SK Hynix DRAM/NAND
- later annual license / site-license relief possible

Samsung labor strike:
- 45k~50k+ workers strike threat
- Samsung shares -9.3%
- estimated operating loss up to $20.79B
- DRAM supply -4%, NAND -3% possible
- government/emergency arbitration watch

Political shock:
- Dec 2024 martial law crisis
- Korea ETF initially -7% then -1.7%
- Samsung London -3.7% or deeper intraday
- won weakness / consumer sentiment / retail sales hit
- broad 4C market shock, later false-break relief after order lifted

Hormuz / Middle East energy shock:
- KOSPI -6% to -12% circuit-breaker shock
- Samsung -7.8%, SK Hynix -9.5%, Hyundai -8.3%
- Korea depends heavily on Middle East oil/LNG
- policy relief: 273M barrels crude and 2.1M tons naphtha via alternative routes

Hanwha Ocean:
- U.S. naval shipbuilding / frigate / nuclear-sub policy optionality
- Hanwha Ocean +6% after Trump comments on U.S. frigates
- Hanwha Ocean +139% YTD 2025 on U.S.-Korea cooperation optimism
- but Hanwha Aerospace share sale / dilution and technology-transfer gates

Wildfire disaster:
- 2025 worst wildfires
- 26~32 deaths depending report timing/source
- 48k hectares / 4,000 structures in Reuters report
- 118k acres / 30k displaced in AP report
- special disaster zones / recovery budget
- no direct KRX equity trigger found
```

---

# 4. 선정 case 요약

| bucket                               | case                                       | 핵심 판정                                                                                      |
| ------------------------------------ | ------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Stage2-Actionable                    | Hanwha Aerospace / Romania K9              | $1B order, +5% record high, backlog 5.1T→30T. 방산 export 구조적 trigger                        |
| Stage2-Actionable / Yellow candidate | Hyundai Rotem / Poland K2                  | +9.3%, KOSPI -0.3%, Q1 OP +85% 예상, Poland K2 shipment가 실제 실적 trigger                       |
| 4C-watch                             | Samsung/SK Hynix / U.S. China export curbs | Samsung -2.3%, SK Hynix -4.4%, KOSPI -0.7%. 생산 업그레이드 제한 hard overlay                       |
| 4C-watch                             | Samsung labor strike                       | shares -9.3%, 45k~50k+ strike threat, $20.79B loss estimate. labor policy hard overlay     |
| hard market 4C / false-break relief  | Martial law crisis                         | Korea ETF -7%→-1.7%, Samsung London down. 정치제도 shock                                       |
| hard geopolitical 4C + policy relief | Hormuz energy crisis                       | KOSPI -6~12%, Samsung/SK Hynix/Hyundai 급락. 273M barrels alternative route는 relief          |
| Stage2 + 4B                          | Hanwha Ocean / U.S. naval shipbuilding     | +6% on U.S. frigate comments, +139% YTD 2025. 정책 optionality지만 tech-transfer/dilution gate |
| disaster reference                   | 2025 wildfires                             | worst wildfire disaster, fatalities/evacuation/structures damaged. 직접 상장사 trigger 없음       |

---

# 5. Case별 trigger grid

## Case A — Hanwha Aerospace / Romania K9 order

```text
symbol = 012450
case_type = Stage2-Actionable / defense export structural success
archetype = DEFENSE_EXPORT_BACKLOG_STAGE2_ACTIONABLE
```

| trigger | type                    |       date | 당시 공개 evidence                                                                                     | 가격 anchor                                     | outcome           |
| ------- | ----------------------- | ---------: | -------------------------------------------------------------------------------------------------- | --------------------------------------------- | ----------------- |
| T0      | awareness               |  2022~2024 | Russia-Ukraine war 이후 Europe rearmament, K-defense export demand                                   | no full OHLC                                  | Stage1            |
| T1      | Stage2 evidence         | 2024-07-09 | Romania K9 contract: $1B, 54 K9 howitzers, 36 K10 vehicles, ammunition                             | shares +5% to record high                     | Stage2-Actionable |
| T2      | Stage3-Yellow candidate | 2024-07-09 | defense backlog 5.1T won end-2021 → around 30T won by Mar-2024; >50% global howitzer export market | same                                          | Yellow candidate  |
| T3      | 4B-watch                |       2025 | large share sale / overseas expansion funding / dilution risk                                      | Hanwha Aerospace -13% after share sale report | 4B dilution       |
| T4      | Stage3-Green            |        N/A | delivery, margin, cash collection not fully verified                                               | N/A                                           | no Green          |

Hanwha Aerospace의 Romania K9 order는 R11 방산에서 가장 정석적인 Stage2-Actionable trigger다. Reuters는 Hanwha Aerospace가 Romania와 $1B 규모 계약을 맺어 54 K9 self-propelled howitzers, ammunition, 36 K10 resupply vehicles를 공급한다고 보도했고, 주가는 early trading에서 5% 이상 올라 record high를 찍었다고 전했다. 같은 보도에서 Hanwha의 defense backlog가 2021년 말 5.1T won에서 2024년 3월 약 30T won으로 늘었고, global howitzer export market share가 50%를 넘는다고 설명했다. 이 조합은 단순 지정학 테마가 아니라 **계약금액·backlog·market share·price reaction**이 닫힌 Stage2-Actionable이다. ([Reuters][1])

```json
{
  "case_id": "r11_loop15_hanwha_aerospace_romania_k9",
  "symbol": "012450",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_to_Stage3-Yellow_candidate",
  "trigger_date": "2024-07-09",
  "contract_value_usd_bn": 1.0,
  "k9_howitzers_count": 54,
  "k10_resupply_vehicles_count": 36,
  "delivery_end": "2029-07",
  "event_return_pct": 5.0,
  "event_price_status": "record_high_reported",
  "defense_backlog_end_2021_krw_trn": 5.1,
  "defense_backlog_mar_2024_krw_trn": 30,
  "global_howitzer_export_share_pct": 50,
  "stage3_gate_missing": [
    "delivery_schedule_execution",
    "gross_margin",
    "cash_collection",
    "localization_offset_terms",
    "share_sale_dilution_absorption"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable"
}
```

---

## Case B — Hyundai Rotem / Poland K2 deliveries and second contract

```text
symbol = 064350
case_type = Stage2-Actionable / Stage3-Yellow candidate
archetype = GROUND_WEAPON_EXPORT_DELIVERY_STAGE2_YELLOW
```

| trigger | type                    |       date | 당시 공개 evidence                                                                                               | 가격 anchor                 | outcome                   |
| ------- | ----------------------- | ---------: | ------------------------------------------------------------------------------------------------------------ | ------------------------- | ------------------------- |
| T0      | awareness               |       2022 | Poland 180 K2 first contract, Russia-Ukraine war rearmament                                                  | no current OHLC           | Stage1                    |
| T1      | Stage2-Actionable       | 2024-04-09 | 18 K2 tanks shipped to Poland; Q1 OP expected +85% YoY to 59.1B won, consensus 44.4B                         | shares +9.3%, KOSPI -0.3% | excellent entry           |
| T2      | Stage3-Yellow candidate | 2024-04-09 | K2 exports to Poland expected to contribute 270B won revenue, nearly one-third of quarterly revenue forecast | same                      | Yellow candidate          |
| T3      | Stage2 validation       | 2025-08-01 | Poland signs second deal for 180 K2 tanks, value in Hyundai filing $6.5B                                     | price unavailable         | validation                |
| T4      | 4B-watch                |       2025 | second contract delayed partly by Korea political crisis; local production 2028~2030                         | no full OHLC              | political/execution watch |
| T5      | Stage3-Green            |        N/A | actual OP/margin/cash collection over multiple quarters not fully verified                                   | N/A                       | no Green                  |

Hyundai Rotem은 R11에서 **“계약 headline”보다 “delivery → earnings estimate”가 더 좋은 trigger**임을 보여준다. WSJ/Dow Jones는 2024년 4월 9일 Hyundai Rotem shares가 9.3% 올라 41,300 won이 됐고, KOSPI는 -0.3%였다고 보도했다. KB Securities는 Q1 OP가 K2 tank exports to Poland 덕분에 +85% YoY인 59.1B won으로 consensus 44.4B를 웃돌 수 있고, 18 K2 shipments가 quarter revenue forecast의 거의 3분의 1인 270B won을 만들 수 있다고 봤다. ([월스트리트저널][2])

2025년 8월 Poland는 Hyundai Rotem과 두 번째 대형 K2 계약을 체결했다. Reuters는 180 tanks second batch, Polish local production, support/training/service package를 보도했고, Hyundai filing 기준 value가 $6.5B였다고 전했다. 다만 일부 생산이 Poland에서 2028~2030년에 이뤄지기 때문에 local production과 execution gate가 남는다. ([Reuters][3])

```json
{
  "case_id": "r11_loop15_hyundai_rotem_poland_k2",
  "symbol": "064350",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_to_Stage3-Yellow_candidate",
  "t1_date": "2024-04-09",
  "t1_event_return_pct": 9.3,
  "t1_price_krw": 41300,
  "kospi_same_context_pct": -0.3,
  "market_relative_return_pp": 9.6,
  "q1_op_estimate_krw_bn": 59.1,
  "q1_op_estimate_yoy_pct": 85,
  "q1_op_consensus_krw_bn": 44.4,
  "k2_shipments_to_poland_count": 18,
  "k2_poland_revenue_contribution_krw_bn": 270,
  "t3_date": "2025-08-01",
  "second_contract_tanks_count": 180,
  "second_contract_value_usd_bn": 6.5,
  "polish_local_production_count": 61,
  "polish_local_production_period": "2028-2030",
  "stage3_gate_missing": [
    "multi_quarter_delivery",
    "gross_margin",
    "cash_collection",
    "local_production_execution",
    "political_delay_absorption"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_delivery_trigger"
}
```

---

## Case C — Samsung / SK Hynix U.S. export curbs on China fabs

```text
symbols = 005930 / 000660 / 067310 / 042700
case_type = 4C-watch / trade-policy shock
archetype = CHIP_EXPORT_CONTROL_4C_WATCH
```

| trigger | type             |         date | 당시 공개 evidence                                                               | 가격 anchor                                  | outcome             |
| ------- | ---------------- | -----------: | ---------------------------------------------------------------------------- | ------------------------------------------ | ------------------- |
| T0      | awareness        |    2022~2024 | U.S. export controls on China chip equipment; Korea makers had waivers       | no price                                   | Stage1              |
| T1      | 4C-watch         |   2025-09-01 | U.S. revokes authorizations for U.S. chip equipment to Samsung/SK China fabs | Samsung -2.3%, SK Hynix -4.4%, KOSPI -0.7% | hard watch          |
| T2      | 4C validation    |   2025-09-01 | >1/3 Samsung DRAM from China; 30~40% SK Hynix DRAM/NAND in China             | same                                       | exposure quantified |
| T3      | relief candidate | 2025-09~2026 | annual/site license system may allow maintenance but not expansion/upgrade   | no KRX price                               | partial relief      |
| T4      | Stage3-Yellow    |          N/A | no growth trigger; this is risk overlay                                      | N/A                                        | N/A                 |

이 case는 R11 trade-policy hard overlay다. Reuters는 2025년 9월 1일 Washington이 Samsung과 SK Hynix의 China fabs에 U.S. semiconductor manufacturing equipment를 들여보낼 수 있게 했던 authorizations를 revoked 했고, Samsung shares는 -2.3%, SK Hynix는 -4.4%, KOSPI는 -0.7%였다고 보도했다. China exposure도 컸다. Reuters는 Samsung DRAM output의 3분의 1 이상, SK Hynix DRAM/NAND output의 30~40%가 China 기반이라고 전했다. ([Reuters][4])

FT도 같은 사건을 보도하며 U.S. Commerce Department가 기존 fabs의 운영용 license는 허용할 의향이 있지만, capacity expansion이나 technology upgrade 용도로는 license를 내주지 않겠다는 취지였다고 설명했다. 즉 이 trigger는 “단기 조업중단”보다 **technology-upgrade ceiling / China fab stranded-capex risk**다. ([Financial Times][5])

```json
{
  "case_id": "r11_loop15_samsung_skhynix_us_china_export_curbs",
  "symbols": "005930/000660/067310/042700",
  "best_trigger": "T1/T2",
  "best_trigger_type": "4C-watch_trade_policy",
  "trigger_date": "2025-09-01",
  "samsung_event_return_pct": -2.3,
  "sk_hynix_event_return_pct": -4.4,
  "kospi_same_context_pct": -0.7,
  "samsung_market_relative_pp": -1.6,
  "skhynix_market_relative_pp": -3.7,
  "samsung_china_dram_output_share": ">33%",
  "skhynix_china_dram_nand_output_share_pct": "30-40",
  "hana_micron_event_return_pct": -1.7,
  "hanmi_semiconductor_event_return_pct": -4.4,
  "policy_effective_delay_days": 120,
  "license_policy": "maintenance_possible_but_no_capacity_expansion_or_upgrade",
  "trigger_outcome_label": "trade_policy_4C_watch"
}
```

---

## Case D — Samsung Electronics labor strike risk

```text
symbol = 005930
case_type = 4C-watch / labor-policy shock
archetype = SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH
```

| trigger |             type | date                                  | 당시 공개 evidence                                                                                                                                          | 가격 anchor               | outcome        |
| ------- | ---------------: | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | -------------- |
| T0      |        awareness | 2024~2026                             | Samsung unionization grows amid AI memory boom and SK Hynix bonus reform                                                                                | no price                | watch          |
| T1      |         4C-watch | 2026-05-12                            | Samsung and union fail to reach pay deal; 50k+ strike risk, PM urges strike to be averted                                                               | no price in that source | watch          |
| T2      | 4C price trigger | 2026-05-15                            | union sticks to 18-day strike plan; Samsung shares -9.3%                                                                                                | -9.3%                   | hard watch     |
| T3      |    4C validation | 2026-05-19                            | strike could reduce DRAM supply 4%, NAND 3%; potential chip-production loss $19.9B; possible $20.79B operating loss estimate in earlier strike coverage | no new price            | validated risk |
| T4      |           relief | if emergency arbitration / settlement | not confirmed                                                                                                                                           | pending                 | no relief      |

Samsung strike risk is an R11 labor-policy hard overlay. Reuters reported that Samsung and its labor union failed to reach a pay agreement even after government-mediated talks, and more than 50,000 workers could participate in a strike starting May 21, with Prime Minister urging talks to avert economic fallout. Semiconductors were 37% of Korea’s exports in April, so this is not a normal company-level labor issue. ([Reuters][6])

On May 15, Reuters reported the union was sticking to the planned 18-day strike and Samsung shares slid 9.3%, as investors priced delivery reliability and supply-chain disruption risk. Reuters later reported that strike action could reduce DRAM supply by up to 4% and NAND by 3%, while the government worried about a potential $19.9B hit to chip production. ([Reuters][7])

```json
{
  "case_id": "r11_loop15_samsung_labor_strike_risk",
  "symbol": "005930",
  "best_trigger": "T1/T2/T3",
  "best_trigger_type": "4C-watch_labor_policy",
  "t1_date": "2026-05-12",
  "potential_strike_workers": ">50000",
  "semiconductors_share_of_exports_april_pct": 37,
  "t2_date": "2026-05-15",
  "samsung_event_return_pct": -9.3,
  "strike_duration_days": 18,
  "t3_date": "2026-05-19",
  "potential_dram_supply_reduction_pct": 4,
  "potential_nand_supply_reduction_pct": 3,
  "potential_chip_production_loss_usd_bn": 19.9,
  "operating_loss_estimate_usd_bn": 20.79,
  "stage3_gate_missing": [
    "settlement",
    "emergency_arbitration_result",
    "actual_wafer_output_loss",
    "delivery_schedule_impact",
    "customer_allocation_shift_to_SKHynix"
  ],
  "trigger_outcome_label": "labor_policy_4C_watch"
}
```

---

## Case E — 2024 martial-law political shock

```text
symbols = KOSPI / EWY / Samsung ADR-London / broad Korea basket
case_type = hard political-market 4C / false-break relief
archetype = POLITICAL_SYSTEM_SHOCK_MARKET_4C
```

| trigger | type          |                                           date | 당시 공개 evidence                                                 | 가격 anchor                                                        | outcome            |
| ------- | ------------- | ---------------------------------------------: | -------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------ |
| T0      | hard 4C       |                                     2024-12-03 | President Yoon declares martial law; first since 1979          | Korea ETF initially -7%; Samsung London -3.7% or deeper intraday | hard market shock  |
| T1      | relief        |                                     2024-12-04 | parliament overturns martial law, Yoon lifts order hours later | ETF trims drop to -1.7%                                          | false-break relief |
| T2      | 4C validation |                                   2024-12~2025 | impeachment proceedings, won weakness, retail sales decline    | macro drag                                                       | political overhang |
| T3      | hard 4C       | if policy continuity or market access impaired | not continuous after order lifted                              | no hard ongoing market closure                                   |                    |

Martial-law shock is a pure R11 system-risk case. MarketWatch reported that U.S.-listed Korea assets were initially hit hard: the iShares MSCI South Korea ETF initially dropped around 7% before trimming losses to about 1.7% after the order was lifted, and Samsung’s London-traded shares were down earlier in the session. This is the clearest example of a **hard political-event 4C with immediate false-break relief**: the initial trigger was severe, but parliament’s vote and the order’s reversal sharply reduced the tail risk. ([마켓워치][8])

Reuters later linked the political upheaval to weak consumer spending, noting December retail sales fell 0.6% month-on-month, car and home-appliance sales fell 4.1%, entertainment spending fell 0.6%, and the won hit a 15-year low amid the crisis. That means the event was not just an overseas ETF blip; it bled into consumption and macro confidence. ([Reuters][9])

```json
{
  "case_id": "r11_loop15_martial_law_political_shock",
  "symbols": "KOSPI/EWY/005930_readthrough/broad_Korea_basket",
  "best_trigger": "T0/T1",
  "best_trigger_type": "hard_4C_political_shock_with_false_break_relief",
  "trigger_date": "2024-12-03/2024-12-04",
  "korea_etf_initial_mae_pct": -7.0,
  "korea_etf_trimmed_loss_pct": -1.7,
  "parliament_vote_to_lift": true,
  "order_lifted_within_hours": true,
  "dec_retail_sales_mom_pct": -0.6,
  "car_home_appliance_sales_mom_pct": -4.1,
  "entertainment_spending_mom_pct": -0.6,
  "won_15y_low_context": true,
  "trigger_outcome_label": "hard_4C_false_break_relief"
}
```

---

## Case F — Hormuz / Middle East energy shock and Korea relief sourcing

```text
symbols = KOSPI / 005930 / 000660 / 005380 / refiners-chemicals basket
case_type = hard geopolitical 4C + policy relief
archetype = HORMUZ_ENERGY_SECURITY_4C_WITH_POLICY_RELIEF
```

| trigger | type          |          date | 당시 공개 evidence                                                                              | 가격 anchor                                                                                | outcome                       |
| ------- | ------------- | ------------: | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------- |
| T0      | hard 4C       | 2026-03-03/04 | Middle East conflict / oil spike / Hormuz constraint triggers Korean market circuit breaker | KOSPI -7% to -12% depending source; Samsung -9.88% / SK Hynix -11.5% in MarketWatch case | hard geopolitical 4C          |
| T1      | 4C validation |    2026-03-09 | oil >$100, Kospi -6%, Samsung -7.8%, SK Hynix -9.5%, Hyundai -8.3%                          | broad market crash                                                                       | validated                     |
| T2      | Stage2 relief |    2026-04-15 | Korea secures 273M barrels crude and 2.1M tons naphtha via non-Hormuz routes                | no stock price                                                                           | policy relief                 |
| T3      | 4B-watch      |       2026-05 | Korea considers phased Hormuz security role after attack on South Korean-flagged cargo ship | no price                                                                                 | geopolitical escalation watch |
| T4      | Green         |           N/A | only relief, not growth                                                                     | N/A                                                                                      | no Green                      |

Hormuz is the R11 energy-security hard 4C. MarketWatch reported that on March 3, 2026, KOSPI plunged 7%, Samsung fell 9.88%, SK Hynix 11.5%, the won weakened 1.34%, and the selloff was tied to oil-price spikes after U.S.-Israeli strikes on Iran; South Korea needs about 2.7M barrels of crude daily and roughly 70% comes from the Middle East. MoneyWeek separately described a March 4 circuit breaker after KOSPI fell 8.1% early and ended about 12% lower. ([마켓워치][10])

The shock persisted. Barron’s reported on March 9 that KOSPI slumped 6%, Samsung fell 7.8%, SK Hynix 9.5%, and Hyundai Motor 8.3% as oil topped $100; it also noted that almost 70% of Korea’s oil imports and 16% of LNG imports came from the Middle East. Reuters later reported policy relief: Korea secured 273M barrels of crude and 2.1M tons of naphtha via alternative routes unrelated to a potential Hormuz closure, covering more than three months of crude and about a month of naphtha under normal conditions. ([Barron's][11])

```json
{
  "case_id": "r11_loop15_hormuz_energy_security_market_shock",
  "symbols": "KOSPI/005930/000660/005380/refiners_chemicals_basket",
  "best_trigger": "T0/T2",
  "best_trigger_type": "hard_4C_geopolitical_energy_shock_with_policy_relief",
  "t0_date": "2026-03-03/2026-03-04",
  "kospi_event_mae_pct_range": "-7_to_-12",
  "samsung_marketwatch_event_return_pct": -9.88,
  "skhynix_marketwatch_event_return_pct": -11.5,
  "won_event_move_pct": -1.34,
  "t1_date": "2026-03-09",
  "kospi_barrons_event_return_pct": -6,
  "samsung_barrons_event_return_pct": -7.8,
  "skhynix_barrons_event_return_pct": -9.5,
  "hyundai_motor_barrons_event_return_pct": -8.3,
  "oil_middle_east_import_share_pct": 70,
  "lng_middle_east_import_share_pct": 16,
  "t2_date": "2026-04-15",
  "alternative_route_crude_secured_mn_barrels": 273,
  "alternative_route_naphtha_secured_mn_tons": 2.1,
  "normal_crude_coverage_months": 3,
  "normal_naphtha_coverage_months": 1,
  "trigger_outcome_label": "hard_4C_with_policy_relief"
}
```

---

## Case G — Hanwha Ocean / U.S. naval shipbuilding and nuclear-submarine optionality

```text
symbols = 042660 / 012450
case_type = Stage2 geopolitical optionality + 4B dilution/technology-transfer overlay
archetype = NAVAL_SHIPBUILDING_GEOPOLITICAL_STAGE2_WITH_DILUTION_4B
```

| trigger | type              |       date | 당시 공개 evidence                                                                        | 가격 anchor                | outcome                 |
| ------- | ----------------- | ---------: | ------------------------------------------------------------------------------------- | ------------------------ | ----------------------- |
| T0      | awareness         |  2024~2025 | Hanwha acquisition of Philly Shipyard / U.S.-Korea naval cooperation                  | no price                 | Stage1                  |
| T1      | Stage2 evidence   | 2025-04-28 | Hanwha Ocean +139% YTD 2025 on U.S.-Korea cooperation optimism; KDB stake-sale report | no intraday event return | Stage2 / overheat watch |
| T2      | Stage2-Actionable | 2025-12-23 | Trump says Hanwha Ocean involved in building new U.S. frigates                        | Hanwha Ocean +6%         | Actionable              |
| T3      | Stage2 policy     |   2025-10~ | U.S. to share nuclear-powered submarine tech / Philly Shipyard context                | no direct price          | policy optionality      |
| T4      | 4B-watch          |       2025 | Hanwha Aerospace 3.6T won / $2.5B share sale, shares -13%, expansion funding/dilution | dilution watch           | 4B                      |
| T5      | Stage3-Yellow     |        N/A | actual U.S. Navy contract, tech transfer, shipyard capex, margin not confirmed        | N/A                      | no Yellow               |

Hanwha Ocean is a strong R11 geopolitical optionality case. Reuters reported that Hanwha Ocean shares had surged 139% in 2025 amid optimism around U.S.-South Korea shipbuilding cooperation and Trump outreach to Korean shipbuilders. Later, Reuters reported Hanwha Ocean shares jumped 6% after Trump said the company would be involved in building a new class of U.S. frigates. ([Reuters][12])

The nuclear-submarine policy optionality is also real but not yet Green. AP reported Trump said the U.S. would share nuclear-powered submarine technology with South Korea, while noting that such technology is highly sensitive and rarely shared; it also reported Trump said South Korea would build its nuclear sub at Philly Shipyard, owned by Hanwha Group. The missing gates are technology-transfer details, legal framework, contract allocation, shipyard capex, delivery schedule, and margin. ([AP News][13])

```json
{
  "case_id": "r11_loop15_hanwha_ocean_us_naval_shipbuilding",
  "symbols": "042660/012450",
  "best_trigger": "T1/T2/T3",
  "best_trigger_type": "Stage2_geopolitical_optionality_with_4B_overlay",
  "hanwha_ocean_2025_ytd_return_pct": 139,
  "trump_frigate_comment_event_return_pct": 6,
  "us_naval_shipbuilding_context": true,
  "philly_shipyard_context": true,
  "nuclear_submarine_technology_sharing_claim": true,
  "share_sale_hanwha_aerospace_krw_trn": 3.6,
  "share_sale_hanwha_aerospace_usd_bn": 2.5,
  "hanwha_aerospace_share_sale_event_return_pct": -13,
  "stage3_gate_missing": [
    "formal_US_Navy_contract",
    "technology_transfer_terms",
    "nuclear_fuel_legal_framework",
    "shipyard_capacity_capex",
    "delivery_schedule",
    "program_margin"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_policy_optionality_with_4B_dilution_overlay"
}
```

---

## Case H — 2025 South Korea wildfires

```text
symbols = disaster_recovery_basket / insurers / construction / utilities read-through
case_type = disaster reference / price unavailable
archetype = NATURAL_DISASTER_RECOVERY_STAGE2_REFERENCE
```

| trigger | type                     |          date | 당시 공개 evidence                                                                                        | 가격 anchor           | outcome            |
| ------- | ------------------------ | ------------: | ----------------------------------------------------------------------------------------------------- | ------------------- | ------------------ |
| T0      | disaster 4C              | 2025-03-21~30 | wildfires spread across southeast / Uiseong / Sancheong                                               | no direct KRX price | disaster reference |
| T1      | hard disaster validation |    2025-03-30 | police link family grave rite to largest wildfire; at least 26 deaths, 48k hectares, 4,000 structures | no stock price      | hard disaster      |
| T2      | relief/policy            |    2025-03~04 | special disaster zones / emergency response / recovery resources                                      | no listed trigger   | relief Stage2      |
| T3      | Stage3                   |           N/A | no direct listed beneficiary evidence                                                                 | N/A                 | no Stage3          |

Wildfires are included as R11 disaster calibration, but not as an equity trigger. Reuters reported that South Korea’s Uiseong wildfire became the country’s largest wildfire, causing at least 26 deaths, burning about 48,000 hectares and destroying around 4,000 structures. AP separately described the fires as the worst in South Korea’s history, with 28 deaths, 37 injuries, more than 30,000 displaced, and 118,265 acres burned. No reliable direct KRX beneficiary/security price trigger was found in this search, so this row is `price_data_unavailable_after_deep_search` and should be used only as a disaster-hard-gate/reference row. ([Reuters][14])

```json
{
  "case_id": "r11_loop15_2025_korea_wildfires_disaster_reference",
  "symbols": "disaster_recovery_basket/insurers/construction/utilities_readthrough",
  "best_trigger": "T0/T1",
  "best_trigger_type": "disaster_reference_price_unavailable",
  "event_period": "2025-03-21_to_2025-03-30",
  "reported_deaths_reuters": 26,
  "reported_burned_area_hectares_reuters": 48000,
  "reported_structures_destroyed_reuters": 4000,
  "reported_deaths_ap": 28,
  "reported_injuries_ap": 37,
  "reported_displaced_people_ap": 30000,
  "reported_burned_area_acres_ap": 118265,
  "direct_krx_price_anchor": "price_data_unavailable_after_deep_search",
  "sources_checked": [
    "Reuters wildfire reports",
    "AP wildfire reports",
    "general KRX beneficiary search"
  ],
  "trigger_outcome_label": "disaster_reference_not_equity_stage3"
}
```

---

# 6. Trigger별 가격경로 검증 요약

| case                          | best trigger |         entry anchor |                                  event MFE/MAE |                market-relative | full MFE/MAE | outcome                     |
| ----------------------------- | ------------ | -------------------: | ---------------------------------------------: | -----------------------------: | ------------ | --------------------------- |
| Hanwha Aerospace Romania K9   | T1/T2        | record high reported |                                            +5% |                    unavailable | unavailable  | excellent Stage2-Actionable |
| Hyundai Rotem Poland K2       | T1/T3        |           41,300 won |                                          +9.3% |          +9.6pp vs KOSPI -0.3% | unavailable  | excellent Stage2-Actionable |
| Samsung/SK Hynix export curbs | T1/T2        |                event |                       Samsung -2.3%, SKH -4.4% | -1.6pp / -3.7pp vs KOSPI -0.7% | unavailable  | 4C-watch                    |
| Samsung labor strike          | T1/T2/T3     |                event |                                  Samsung -9.3% |                    unavailable | unavailable  | labor 4C-watch              |
| Martial law crisis            | T0/T1        |            ETF/event |                          Korea ETF -7% → -1.7% |                    unavailable | unavailable  | hard 4C false-break relief  |
| Hormuz energy shock           | T0/T2        |          index/event | KOSPI -6~12%, Samsung/SKH/Hyundai sharply down |                 broad negative | unavailable  | hard 4C + policy relief     |
| Hanwha Ocean naval            | T1/T2/T3     |                event |                    +6%, 2025 YTD +139% context |                    unavailable | unavailable  | Stage2 + 4B                 |
| Wildfires                     | T0/T1        |                  N/A |                            no direct KRX price |                            N/A | unavailable  | disaster reference          |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
Hanwha Ocean:
U.S. naval shipbuilding and nuclear-sub policy optionality is Stage2, but tech-transfer and contract allocation are missing.

Wildfire:
disaster reference only. No direct listed equity trigger found.

Martial-law relief:
parliament reversal created false-break relief, but not a growth trigger.
```

## Stage 2-Actionable entry 성과

```text
Hanwha Aerospace:
Romania $1B K9 contract + +5% record high + backlog expansion.
Actionable.

Hyundai Rotem:
K2 deliveries to Poland + Q1 OP estimate beat + +9.3%.
Very strong Actionable; closer to Yellow than headline contract alone.

Hanwha Ocean:
+6% U.S. frigate trigger is Actionable, but 2025 +139% context and dilution risk require 4B overlay.
```

## Stage 3-Yellow 후보

```text
Hyundai Rotem:
delivery-to-revenue evidence already exists. Multi-quarter margin/cash collection could make it Yellow.

Hanwha Aerospace:
large backlog and export market share make it Yellow candidate if delivery/margin confirms.

Hanwha Ocean:
formal U.S. Navy contract and shipyard capex execution could make it Yellow.
```

## Stage3-Green

```text
이번 R11 Loop 15에서 확정 Green 없음.

이유:
- 방산은 수주/납품은 강하지만 margin/cash collection과 local production terms가 남아 있다.
- chip export curbs and labor strike are risk overlays, not growth.
- Hormuz relief is supply stabilization, not earnings growth.
- political shock and disaster cases are hard risk references.
```

---

# 8. score-price alignment 판정

```text
Stage2_promote_candidate:
- Hanwha Aerospace Romania K9
- Hyundai Rotem Poland K2
- Hanwha Ocean U.S. naval shipbuilding, with 4B overlay

Stage3-Yellow candidate:
- Hyundai Rotem, if delivery/margin continues
- Hanwha Aerospace, if backlog converts to OP/cash
- Hanwha Ocean, if formal U.S. Navy contract and tech-transfer terms close

event_premium:
- Hanwha Ocean +139% YTD / +6% Trump comment if no formal contract
- Defense basket if priced only on geopolitical beta

evidence_good_but_price_failed:
- N/A in selected rows, but export-curb relief licenses would need price verification

false_positive_score:
- Treating defense preferred-policy talk as actual contract
- Treating Hormuz alternative crude routing as growth rather than relief
- Treating political false-break relief as structural improvement

thesis_break_watch:
- U.S. chip export curbs
- Samsung labor strike
- Korea political-system shock
- Hormuz energy chokepoint risk

hard_4C_success:
- Martial-law initial market shock
- Hormuz circuit-breaker shock
- Disaster reference, but no stock row
```

---

# 9. 점수비중 교정

## 올릴 축

```text
signed_defense_contract_value +5
delivery_to_revenue_conversion +5
defense_backlog_growth +5
local_production_technology_transfer_terms +4
trade_policy_license_risk +5
labor_disruption_output_risk +5
political_system_stability +5
energy_chokepoint_exposure +5
alternative_supply_route_relief +4
disaster_direct_cost_and_recovery +4
```

### 근거

Hyundai Rotem은 단순 Poland contract headline보다 **18 K2 shipments → revenue contribution → OP estimate beat**가 더 좋은 trigger였다. Hanwha Aerospace는 $1B Romania contract와 backlog 5.1T→30T가 같이 닫혀 Stage2-Actionable이다. 반대로 Samsung/SK Hynix는 U.S. China export-license policy가 기술 업그레이드 ceiling이 될 수 있고, Samsung strike는 실제 supply와 고객 납기 리스크를 만든다.

## 내릴 축

```text
geopolitical_theme_only -5
preferred_supplier_without_signed_contract -4
defense_order_without_delivery_margin -4
policy_relief_without_earnings -5
energy_supply_relief_as_growth -4
political_false_break_as_structural -4
technology_transfer_headline_only -5
```

### 근거

Hanwha Ocean의 naval/nuclear-sub optionality는 크지만 formal U.S. Navy contract와 tech-transfer details 전에는 Green이 아니다. Hormuz alternative supply 확보는 국가 경제 안정에는 중요하지만 기업 EPS 성장 trigger가 아니라 relief다. Martial-law reversal도 false-break relief이지 structural Stage3가 아니다.

---

# 10. Stage 2-Actionable 승격 조건

R11 Loop 15 shadow rule:

```text
R11에서 Stage 2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. 정책/지정학 headline이 signed contract 또는 delivery로 닫힌다.
2. 계약금액이 회사 backlog나 revenue에 의미 있게 크다.
3. 당일 market-relative +5pp 이상 가격반응이 있다.
4. delivery-to-revenue 또는 OP estimate revision이 확인된다.
5. 방산은 local production / tech transfer / service package까지 조건이 구체적이다.
6. 정책 relief가 실제 supply route, license, budget, procurement로 전환된다.
7. 반대로 political shock, labor strike, export controls, disaster는 growth가 아니라 4C overlay로 분리한다.
```

적용:

```text
Hyundai Rotem:
shipments + revenue + OP estimate + +9.3% → Stage2-Actionable / Yellow candidate.

Hanwha Aerospace:
signed contract + backlog expansion + +5% → Stage2-Actionable.

Hanwha Ocean:
U.S. frigate comment + +6% → Stage2-Actionable, but formal contract missing and 4B overlay strong.
```

---

# 11. Stage 3-Yellow 조건

```text
Stage3-Yellow:
- 정책/지정학 trigger가 EPS/OP/FCF 경로를 바꿀 수 있는 숫자로 보임
- 하지만 margin, delivery, local-production execution, license, legal/political continuity 중 하나가 남음
```

후보:

```text
Hyundai Rotem:
delivery-to-revenue and OP estimate beat already visible.
남은 gate: margin, multi-quarter cash collection, second contract execution.

Hanwha Aerospace:
backlog and contract visibility high.
남은 gate: delivery, margin, dilution/share-sale absorption.

Hanwha Ocean:
U.S. naval shipbuilding optionality.
남은 gate: formal Navy contract, tech transfer, shipyard economics.
```

---

# 12. Stage 3-Green 조건

```text
Stage3-Green:
- defense contract delivers into revenue and margin
- local production / technology transfer terms do not destroy margin
- policy relief becomes recurring procurement, budget, license, or formal contract
- labor/export-control/political/geopolitical risks are cleared
- full-window MFE/MAE is favorable
```

이번 R11 Loop 15에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- defense stocks rerate on geopolitics before signed contract
- naval/nuclear-sub story rises before formal U.S. Navy contract or tech-transfer terms
- policy relief after energy shock is treated as growth
- political shock reverses quickly but underlying governance risk remains
- labor strike threat rises/fades on negotiation headlines without actual output data
```

적용:

```text
Hanwha Ocean:
+139% YTD and +6% event require 4B valuation/policy overlay.

Hanwha Aerospace:
large share sale/dilution after defense rally is 4B.

Hormuz:
alternative crude routes are relief, not growth.

Martial law:
order reversal is false-break relief, not structural positive.
```

---

# 14. 4C hard gate 조건

```text
R11 4C:
- martial law / political-system shock
- export-license revocation affecting production upgrade
- labor strike threatening core national export output
- energy chokepoint closure / oil shock / circuit breaker
- defense contract cancellation or political delay
- disaster causing direct economic damage and recovery cost
```

이번 R11 Loop 15 hard 4C:

```text
- Martial-law initial market shock
- Hormuz energy shock / market circuit-breaker
```

Strong 4C-watch:

```text
- Samsung/SK Hynix export controls
- Samsung labor strike
- Defense contract political-delay / local-production margin
- Wildfire disaster recovery without listed price trigger
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_234.md 요약

```md
# R11 Loop 15. Policy / Geopolitics / Disaster / Event Trigger-level Price Validation

이번 라운드는 R11 Loop 15 trigger-level validation 라운드다.

핵심 결론:
- Hanwha Aerospace / Romania K9 is Stage2-Actionable. $1B contract for 54 K9 howitzers, ammunition and 36 K10 resupply vehicles; shares rose more than 5% to a record high. Defense backlog rose from 5.1T won at end-2021 to about 30T won by Mar-2024.
- Hyundai Rotem / Poland K2 is Stage2-Actionable and near Stage3-Yellow. Shares rose 9.3% to 41,300 won while KOSPI fell 0.3%; Q1 OP was expected +85% YoY to 59.1B won, above 44.4B consensus, helped by 18 K2 shipments to Poland. Second Poland K2 contract is $6.5B for 180 tanks.
- Samsung / SK Hynix U.S. China export curbs are 4C-watch. Samsung fell 2.3%, SK Hynix 4.4%, KOSPI 0.7%; more than one-third of Samsung DRAM output and 30~40% of SK Hynix DRAM/NAND output are China-based.
- Samsung labor strike is labor-policy 4C-watch. 50k+ workers could strike; Samsung shares slid 9.3% after union held its strike plan; potential DRAM/NAND supply reductions and chip-production losses are material.
- Martial-law crisis is hard political-market 4C with false-break relief. Korea ETF initially dropped around 7% then trimmed losses to about 1.7% after the order was lifted. Later retail sales and won weakness showed macro spillover.
- Hormuz / Middle East energy shock is hard geopolitical 4C with policy relief. KOSPI fell 6~12% across reported shock days, Samsung/SK Hynix/Hyundai sold off, and Korea later secured 273M barrels of crude and 2.1M tons of naphtha via alternative non-Hormuz routes.
- Hanwha Ocean / U.S. naval shipbuilding is Stage2 geopolitical optionality with 4B overlay. Shares jumped 6% after Trump comments on U.S. frigates and had risen 139% YTD 2025 on U.S.-Korea cooperation optimism. Formal contracts, tech transfer and shipyard economics remain gates.
- 2025 South Korea wildfires are disaster reference, not equity Stage3. Reuters/AP reported mass casualties and extensive damage, but no reliable direct KRX beneficiary trigger was found.

Main calibration:
- Raise signed_defense_contract_value, delivery_to_revenue_conversion, defense_backlog_growth, local_production_technology_transfer_terms, trade_policy_license_risk, labor_disruption_output_risk, political_system_stability, energy_chokepoint_exposure, alternative_supply_route_relief, disaster_direct_cost_and_recovery.
- Lower geopolitical_theme_only, preferred_supplier_without_signed_contract, defense_order_without_delivery_margin, policy_relief_without_earnings, energy_supply_relief_as_growth, political_false_break_as_structural, technology_transfer_headline_only.
```

## docs/checkpoints/checkpoint_28a_round234_r11_loop15.md 요약

```md
# Checkpoint 28A Round 234 R11 Loop 15 Trigger-level Calibration

## 반영 내용
- R11 Loop 15 trigger-level validation을 수행했다.
- Hanwha Aerospace Romania K9, Hyundai Rotem Poland K2, Samsung/SK Hynix U.S. export curbs, Samsung labor strike, martial-law crisis, Hormuz energy shock, Hanwha Ocean U.S. naval shipbuilding, 2025 wildfires를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / FT / WSJ / MarketWatch / AP / Barron’s의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- 지정학 theme는 signed contract, delivery-to-revenue, backlog growth로 승격한다.
- 방산은 preferred supplier가 아니라 delivery/margin/cash collection이 Stage gate다.
- 수출통제, 파업, 정치 shock, 에너지 chokepoint는 growth trigger가 아니라 4C overlay다.
- 정책 relief는 earnings growth가 아니라 downside containment로 분리한다.
```

## data/e2r_case_library/cases_r11_loop15_round234.jsonl 초안

```jsonl
{"case_id":"r11_loop15_hanwha_aerospace_romania_k9","symbol":"012450","company_name":"Hanwha Aerospace","case_type":"Stage2_promote_candidate","primary_archetype":"DEFENSE_EXPORT_BACKLOG_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable_to_Stage3-Yellow_candidate","price_validation":{"trigger_date":"2024-07-09","contract_value_usd_bn":1.0,"k9_howitzers_count":54,"k10_resupply_vehicles_count":36,"delivery_end":"2029-07","event_return_pct":5.0,"event_price_status":"record_high_reported","defense_backlog_end_2021_krw_trn":5.1,"defense_backlog_mar_2024_krw_trn":30,"global_howitzer_export_share_pct":50,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Signed contract, backlog expansion and price reaction make this Stage2-Actionable; Green requires delivery/margin/cash collection."}
{"case_id":"r11_loop15_hyundai_rotem_poland_k2","symbol":"064350","company_name":"Hyundai Rotem","case_type":"Stage2_promote_candidate","primary_archetype":"GROUND_WEAPON_EXPORT_DELIVERY_STAGE2_YELLOW","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable_to_Stage3-Yellow_candidate","price_validation":{"t1_date":"2024-04-09","t1_event_return_pct":9.3,"t1_price_krw":41300,"kospi_same_context_pct":-0.3,"market_relative_return_pp":9.6,"q1_op_estimate_krw_bn":59.1,"q1_op_estimate_yoy_pct":85,"q1_op_consensus_krw_bn":44.4,"k2_shipments_to_poland_count":18,"k2_poland_revenue_contribution_krw_bn":270,"t3_date":"2025-08-01","second_contract_tanks_count":180,"second_contract_value_usd_bn":6.5,"polish_local_production_count":61,"polish_local_production_period":"2028-2030","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Delivery-to-revenue and OP estimate beat are stronger than defense headline alone."}
{"case_id":"r11_loop15_samsung_skhynix_us_china_export_curbs","symbol":"005930/000660/067310/042700","company_name":"Samsung Electronics / SK Hynix / Hana Micron / Hanmi Semiconductor","case_type":"4c_watch","primary_archetype":"CHIP_EXPORT_CONTROL_4C_WATCH","best_trigger":"T1/T2","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2025-09-01","samsung_event_return_pct":-2.3,"sk_hynix_event_return_pct":-4.4,"kospi_same_context_pct":-0.7,"samsung_market_relative_pp":-1.6,"skhynix_market_relative_pp":-3.7,"samsung_china_dram_output_share":">33%","skhynix_china_dram_nand_output_share_pct":"30-40","hana_micron_event_return_pct":-1.7,"hanmi_semiconductor_event_return_pct":-4.4,"policy_effective_delay_days":120,"license_policy":"maintenance_possible_but_no_capacity_expansion_or_upgrade"},"score_price_alignment":"thesis_break_watch","notes":"Export-license revocation is a technology-upgrade ceiling and must be 4C overlay."}
{"case_id":"r11_loop15_samsung_labor_strike_risk","symbol":"005930","company_name":"Samsung Electronics","case_type":"4c_watch","primary_archetype":"SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH","best_trigger":"T1/T2/T3","stage_candidate":"4C-watch","price_validation":{"potential_strike_workers":">50000","semiconductors_share_of_exports_april_pct":37,"samsung_event_return_pct":-9.3,"strike_duration_days":18,"potential_dram_supply_reduction_pct":4,"potential_nand_supply_reduction_pct":3,"potential_chip_production_loss_usd_bn":19.9,"operating_loss_estimate_usd_bn":20.79,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"Labor disruption can impair national export output and chip supply reliability."}
{"case_id":"r11_loop15_martial_law_political_shock","symbol":"KOSPI/EWY/005930_readthrough/broad_Korea_basket","company_name":"Korea broad market / political shock reference","case_type":"hard_4c_false_break_relief","primary_archetype":"POLITICAL_SYSTEM_SHOCK_MARKET_4C","best_trigger":"T0/T1","stage_candidate":"4C","price_validation":{"trigger_date":"2024-12-03/2024-12-04","korea_etf_initial_mae_pct":-7.0,"korea_etf_trimmed_loss_pct":-1.7,"parliament_vote_to_lift":true,"order_lifted_within_hours":true,"dec_retail_sales_mom_pct":-0.6,"car_home_appliance_sales_mom_pct":-4.1,"entertainment_spending_mom_pct":-0.6,"won_15y_low_context":true},"score_price_alignment":"hard_4c_false_break_relief","notes":"Political-system shock is hard 4C, even if fast reversal creates false-break relief."}
{"case_id":"r11_loop15_hormuz_energy_security_market_shock","symbol":"KOSPI/005930/000660/005380/refiners_chemicals_basket","company_name":"Korea broad market / energy security basket","case_type":"hard_4c_with_policy_relief","primary_archetype":"HORMUZ_ENERGY_SECURITY_4C_WITH_POLICY_RELIEF","best_trigger":"T0/T2","stage_candidate":"4C + Stage2 relief","price_validation":{"kospi_event_mae_pct_range":"-7_to_-12","samsung_marketwatch_event_return_pct":-9.88,"skhynix_marketwatch_event_return_pct":-11.5,"won_event_move_pct":-1.34,"kospi_barrons_event_return_pct":-6,"samsung_barrons_event_return_pct":-7.8,"skhynix_barrons_event_return_pct":-9.5,"hyundai_motor_barrons_event_return_pct":-8.3,"oil_middle_east_import_share_pct":70,"lng_middle_east_import_share_pct":16,"alternative_route_crude_secured_mn_barrels":273,"alternative_route_naphtha_secured_mn_tons":2.1,"normal_crude_coverage_months":3,"normal_naphtha_coverage_months":1},"score_price_alignment":"hard_4c_with_policy_relief","notes":"Energy chokepoint shock is hard 4C; alternative supply routes are relief, not growth."}
{"case_id":"r11_loop15_hanwha_ocean_us_naval_shipbuilding","symbol":"042660/012450","company_name":"Hanwha Ocean / Hanwha Aerospace","case_type":"Stage2_policy_optionality_with_4B_overlay","primary_archetype":"NAVAL_SHIPBUILDING_GEOPOLITICAL_STAGE2_WITH_DILUTION_4B","best_trigger":"T1/T2/T3","stage_candidate":"Stage2 + 4B-watch","price_validation":{"hanwha_ocean_2025_ytd_return_pct":139,"trump_frigate_comment_event_return_pct":6,"us_naval_shipbuilding_context":true,"philly_shipyard_context":true,"nuclear_submarine_technology_sharing_claim":true,"share_sale_hanwha_aerospace_krw_trn":3.6,"share_sale_hanwha_aerospace_usd_bn":2.5,"hanwha_aerospace_share_sale_event_return_pct":-13,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_policy_optionality_with_4B_overlay","notes":"U.S. naval/nuclear-sub optionality is Stage2; formal contracts, tech transfer and dilution absorption are gates."}
{"case_id":"r11_loop15_2025_korea_wildfires_disaster_reference","symbol":"disaster_recovery_basket/insurers/construction/utilities_readthrough","company_name":"2025 South Korea wildfire disaster reference","case_type":"disaster_reference_price_unavailable","primary_archetype":"NATURAL_DISASTER_RECOVERY_STAGE2_REFERENCE","best_trigger":"T0/T1","stage_candidate":"N/A_reference","price_validation":{"event_period":"2025-03-21_to_2025-03-30","reported_deaths_reuters":26,"reported_burned_area_hectares_reuters":48000,"reported_structures_destroyed_reuters":4000,"reported_deaths_ap":28,"reported_injuries_ap":37,"reported_displaced_people_ap":30000,"reported_burned_area_acres_ap":118265,"direct_krx_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"disaster_reference_not_equity_stage3","notes":"Use as disaster hard-gate/recovery reference only; no reliable listed equity price trigger found."}
```

## data/e2r_trigger_calibration/triggers_r11_loop15_round234.jsonl 초안

```jsonl
{"trigger_id":"r11l15_hanwha_k9_romania_T1","case_id":"r11_loop15_hanwha_aerospace_romania_k9","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-09","evidence_available":"$1B Romania K9 contract, 54 K9 howitzers, 36 K10 resupply vehicles, backlog 5.1T to 30T won, shares +5% to record high","event_return_pct":5.0,"trigger_outcome_label":"excellent_stage2_actionable","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r11l15_hyundai_rotem_poland_T1","case_id":"r11_loop15_hyundai_rotem_poland_k2","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-09","evidence_available":"18 K2 shipments to Poland, Q1 OP estimate +85% YoY, shares +9.3% while KOSPI -0.3%","event_return_pct":9.3,"market_relative_return_pp":9.6,"trigger_outcome_label":"excellent_stage2_actionable_delivery_trigger","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r11l15_chip_export_curbs_T1","case_id":"r11_loop15_samsung_skhynix_us_china_export_curbs","trigger_type":"4C-watch","trigger_date":"2025-09-01","evidence_available":"U.S. revokes equipment export authorizations for Samsung/SK Hynix China fabs; Samsung -2.3%, SK Hynix -4.4%, KOSPI -0.7%","event_return_pct":"Samsung -2.3 / SK Hynix -4.4","trigger_outcome_label":"trade_policy_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r11l15_samsung_strike_T2","case_id":"r11_loop15_samsung_labor_strike_risk","trigger_type":"4C-watch","trigger_date":"2026-05-15","evidence_available":"Samsung union sticks to 18-day strike plan; shares slide 9.3%; delivery reliability and supply disruption risk","event_return_pct":-9.3,"trigger_outcome_label":"labor_policy_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r11l15_martial_law_T0","case_id":"r11_loop15_martial_law_political_shock","trigger_type":"hard_4C","trigger_date":"2024-12-03","evidence_available":"Martial law declaration triggers Korea ETF initial -7% drop and broad Korean asset stress","event_return_pct":-7.0,"trigger_outcome_label":"hard_4c_political_shock","promote_to":"4C"}
{"trigger_id":"r11l15_martial_law_T1","case_id":"r11_loop15_martial_law_political_shock","trigger_type":"false_break_relief","trigger_date":"2024-12-04","evidence_available":"Parliament overturns martial law and Yoon lifts order; ETF loss trimmed to about -1.7%","event_return_pct":-1.7,"trigger_outcome_label":"false_break_relief","promote_to":"4C-watch_relief"}
{"trigger_id":"r11l15_hormuz_T0","case_id":"r11_loop15_hormuz_energy_security_market_shock","trigger_type":"hard_4C","trigger_date":"2026-03-03/2026-03-09","evidence_available":"Hormuz/Middle East oil shock triggers KOSPI circuit-breaker selloff; Samsung/SK Hynix/Hyundai sharply down","event_return_pct":"KOSPI -6_to_-12 / Samsung -7.8_to_-9.88 / SKH -9.5_to_-11.5 / Hyundai -8.3","trigger_outcome_label":"hard_4c_geopolitical_energy","promote_to":"4C"}
{"trigger_id":"r11l15_hormuz_T2","case_id":"r11_loop15_hormuz_energy_security_market_shock","trigger_type":"Stage2_relief","trigger_date":"2026-04-15","evidence_available":"Korea secures 273M barrels crude and 2.1M tons naphtha through routes outside Hormuz","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"policy_relief_not_growth","promote_to":"Stage2_relief"}
{"trigger_id":"r11l15_hanwha_ocean_T2","case_id":"r11_loop15_hanwha_ocean_us_naval_shipbuilding","trigger_type":"Stage2_policy_optionality","trigger_date":"2025-12-23","evidence_available":"Hanwha Ocean shares +6% after Trump comments on building U.S. frigates","event_return_pct":6.0,"trigger_outcome_label":"Stage2_policy_optionality_with_4B","promote_to":"Stage2-Actionable"}
{"trigger_id":"r11l15_wildfire_T1","case_id":"r11_loop15_2025_korea_wildfires_disaster_reference","trigger_type":"disaster_reference","trigger_date":"2025-03-30","evidence_available":"Korea's largest wildfire killed at least 26, burned 48k hectares and destroyed around 4k structures; no direct KRX price trigger found","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"disaster_reference_not_equity_stage3","promote_to":"N/A_reference"}
```

## data/sector_taxonomy/score_weight_profiles_round234_r11_loop15_v1.csv 초안

```csv
archetype,signed_defense_contract_value,delivery_to_revenue_conversion,defense_backlog_growth,local_production_technology_transfer_terms,trade_policy_license_risk,labor_disruption_output_risk,political_system_stability,energy_chokepoint_exposure,alternative_supply_route_relief,disaster_direct_cost_recovery,geopolitical_theme_only_penalty,preferred_supplier_without_signed_contract_penalty,defense_order_without_delivery_margin_penalty,policy_relief_without_earnings_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
DEFENSE_EXPORT_BACKLOG_STAGE2_ACTIONABLE,+5,+4,+5,+4,+1,+0,+1,+1,+0,+0,-5,-4,-4,-2,signed contract+backlog+price reaction,delivery/margin pending,delivery+margin+cash collection,Hanwha Aerospace Romania K9.
GROUND_WEAPON_EXPORT_DELIVERY_STAGE2_YELLOW,+5,+5,+4,+5,+1,+0,+1,+1,+0,+0,-4,-3,-3,-2,shipments+revenue+OP estimate,local production/margin pending,multi-quarter delivery+margin,Hyundai Rotem Poland K2.
CHIP_EXPORT_CONTROL_4C_WATCH,+0,+0,+0,+0,+5,+0,+2,+1,+1,+0,-1,-1,-1,-2,license revocation,relief annual license pending,China fab upgrade stability,Samsung/SK Hynix export curbs.
SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH,+0,+0,+0,+0,+2,+5,+2,+1,+0,+0,-1,-1,-1,-2,strike threat,settlement/output loss pending,production stability,Samsung strike risk.
POLITICAL_SYSTEM_SHOCK_MARKET_4C,+0,+0,+0,+0,+1,+1,+5,+2,+1,+1,-1,-1,-1,-4,political shock,order reversal/continuity pending,stability restored,Martial-law shock.
HORMUZ_ENERGY_SECURITY_4C_WITH_POLICY_RELIEF,+0,+0,+0,+0,+1,+0,+2,+5,+4,+1,-1,-1,-1,-5,energy chokepoint shock,alternative routes pending,supply stabilized,Hormuz energy crisis.
NAVAL_SHIPBUILDING_GEOPOLITICAL_STAGE2_WITH_DILUTION_4B,+4,+3,+3,+5,+2,+0,+2,+2,+0,+0,-5,-4,-4,-2,naval policy optionality,formal contract/tech transfer pending,Navy contract+shipyard margin,Hanwha Ocean U.S. naval.
NATURAL_DISASTER_RECOVERY_STAGE2_REFERENCE,+0,+0,+0,+0,+0,+0,+2,+1,+2,+5,-1,-1,-1,-3,disaster and recovery,listed equity trigger missing,N/A,Wildfire reference only.
```

---

# 이번 R11 Loop 15 결론

```text
1. Hanwha Aerospace / Romania K9은 Stage2-Actionable이다.
   $1B 계약, +5% record high, backlog 5.1T→30T won이 닫혔다.

2. Hyundai Rotem / Poland K2는 Stage2-Actionable을 넘어 Yellow 후보에 가깝다.
   18대 납품 → 매출 270B won → Q1 OP +85% 예상 → 주가 +9.3%가 연결됐다.

3. Samsung/SK Hynix U.S. China export curbs는 4C-watch다.
   장비 license와 China fab upgrade ceiling은 반도체 Stage3에 hard overlay다.

4. Samsung labor strike는 R11 labor-policy 4C-watch다.
   파업은 단순 임금 이슈가 아니라 memory supply, export output, customer delivery risk다.

5. Martial-law crisis는 hard political-market 4C다.
   빠른 reversal로 false-break relief가 나왔지만, 정치제도 shock 자체는 hard gate다.

6. Hormuz/Middle East energy shock는 hard geopolitical 4C다.
   alternative crude/naphtha route는 relief이지 growth trigger가 아니다.

7. Hanwha Ocean U.S. naval shipbuilding은 Stage2 optionality + 4B다.
   +6% event와 +139% YTD는 강하지만 formal contract와 tech-transfer gate가 남는다.

8. 2025 wildfires는 disaster reference다.
   직접 KRX price trigger가 없어서 Stage3 판단에는 쓰지 않고, 재난 hard-gate/reference로만 둔다.
```

한 문장으로 압축하면:

> **R11 Loop 15에서 배운 핵심은 “정책·지정학 headline”이 아니라, signed contract, delivery-to-revenue, license stability, labor-output continuity, political-system stability, energy-route security가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 방산 테마, 에너지 relief, 정치 false-break, 기술이전 headline만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-wins-1-bln-order-romania-k9-howitzers-2024-07-09/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace wins $1 bln order from Romania for self-propelled howitzers"
[2]: https://www.wsj.com/articles/hyundai-rotem-rallies-on-hopes-tank-exports-will-boost-earnings-9322d840?utm_source=chatgpt.com "Hyundai Rotem Rallies on Hopes Tank Exports Will Boost Earnings"
[3]: https://www.reuters.com/markets/emerging/poland-signs-contract-buy-more-south-korean-battle-tanks-2025-08-01/?utm_source=chatgpt.com "Poland signs contract to buy more South Korean battle tanks"
[4]: https://www.reuters.com/world/china/shares-samsung-sk-hynix-drop-after-us-makes-it-harder-make-chips-china-2025-09-01/?utm_source=chatgpt.com "Shares in Samsung, SK Hynix drop after US makes it harder to make chips in China"
[5]: https://www.ft.com/content/fd77488c-d5f3-4677-ba90-cc7e8de74333?utm_source=chatgpt.com "US chipmaking curbs hit Samsung and SK Hynix"
[6]: https://www.reuters.com/business/world-at-work/samsung-elec-labour-union-fail-reach-pay-deal-strike-looms-2026-05-12/?utm_source=chatgpt.com "Samsung Electronics fails to reach deal with union; PM says strike must be averted"
[7]: https://www.reuters.com/business/world-at-work/samsung-elecs-union-says-samsung-proposed-unconditional-talks-strike-plan-holds-2026-05-15/?utm_source=chatgpt.com "Samsung's South Korean union sticks to strike plan after talks offer; shares slide"
[8]: https://www.marketwatch.com/story/korean-stocks-hammered-after-declaration-of-martial-law-6becdf7e?utm_source=chatgpt.com "Korean stocks trim declines after president lifts martial-law order"
[9]: https://www.reuters.com/markets/asia/south-korea-dec-retail-sales-decline-amid-political-upheaval-2025-02-03/?utm_source=chatgpt.com "South Korea December retail sales decline amid political upheaval"
[10]: https://www.marketwatch.com/story/worlds-hottest-stock-market-suddenly-blows-cold-with-a-7-tumble-c1f15650?utm_source=chatgpt.com "World's hottest stock market suddenly blows cold with a 7% tumble"
[11]: https://www.barrons.com/articles/korean-stocks-kospi-slump-iran-oil-samsung-d8a85e2e?utm_source=chatgpt.com "Korean Stocks Slump 6%. Why Surging Energy Prices Are a Grave Threat."
[12]: https://www.reuters.com/markets/europe/korea-development-bank-sell-shares-hanwha-ocean-paper-reports-2025-04-28/?utm_source=chatgpt.com "Korea Development Bank to sell shares in Hanwha Ocean, paper reports"
[13]: https://apnews.com/article/ce3ad17d6288573696bf42ca089e76c5?utm_source=chatgpt.com "US will share tech to let South Korea build a nuclear-powered submarine, Trump says"
[14]: https://www.reuters.com/world/asia-pacific/south-korea-police-say-rite-family-grave-led-deadly-wildfire-2025-03-30/?utm_source=chatgpt.com "South Korea police say rite at family grave led to deadly wildfire"
