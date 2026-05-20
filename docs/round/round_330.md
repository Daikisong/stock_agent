순서상 이번은 **R9 Loop 17 — 모빌리티·운송·레저 trigger-level price validation 라운드**다.

```text
round = R9 Loop 17
round_id = round_258
large_sector = MOBILITY_TRANSPORT_LEISURE
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R10 Loop 17
```

이번에도 KRX/Naver/Yahoo/Stooq 수정주가 일봉 OHLC window를 직접 안정적으로 확보하지 못했다. 그래서 MFE/MAE/peak/drawdown 숫자는 만들지 않고 `price_data_unavailable_after_deep_search`로 둔다. 대신 Reuters/WSJ/AP의 **reported event return, issue price, close price, tariff rate, deal value, passenger-capacity/market-structure data, crash-loss data, investment amount**를 trigger anchor로 사용한다.

---

# 1. 이번 라운드 대섹터

```text
R9 = 모빌리티·운송·레저
```

R9의 core gate는 아래다.

```text
자동차:
hybrid/EREV mix → ASP/margin → U.S. tariff/localization → buyback/dividend → production capacity → robotics/autonomous optionality

자동차부품/로보틱스:
OEM platform → supplier content per vehicle → plant automation/robot deployment → capex ROI → customer diversification

항공:
consolidation → route capacity → fare/yield → fuel/FX → safety/trust → regulator/remediation

LCC/여행:
visitor demand → booking/cancellation → load factor → yield → safety event / consumer confidence

해운/운송서비스:
freight rate / ship-service demand → vessel retrofits → aftermarket margin → IPO/valuation → KKR/parent overhang

조선/해양운송 인프라:
U.S.-Korea shipbuilding cooperation → naval/icebreaker demand → merger/capacity → execution / exchange ratio / defense contract

레저/관광:
visa policy → visitor volume → basket size → casino/hotel/duty-free spend → low-spend tourism / short policy window 4B
```

---

# 2. 대상 canonical archetype

```text
AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE
AUTO_TARIFF_LOCALIZATION_4B
MOBILITY_ROBOTICS_AI_FACTORY_STAGE2_OVERHEAT
AIRLINE_CONSOLIDATION_STAGE2_NO_PRICE
LCC_SAFETY_TRUST_HARD_4C
CHINA_TOURISM_LEISURE_STAGE2_ACTIONABLE
MARINE_AFTERMARKET_IPO_STAGE2_ACTIONABLE
SHIPBUILDING_MERGER_US_NAVAL_STAGE2_ACTIONABLE
```

---

# 3. deep sub-archetype

```text
Hyundai Motor / hybrid + value-up:
- Hyundai targets 5.55M global sales by 2030, +30% vs 2023.
- hybrid sales target raised 40% to 1.33M by 2028.
- buyback up to 4T won / $3B from 2025~2027.
- shareholder-return ratio to 35% of profit.
- shares +5% intraday and closed +4.7%.
- Stage2-Actionable.

Hyundai/Kia / U.S. auto tariff:
- U.S.-Korea trade deal set auto import tariff at 15%.
- Hyundai -4.5%, Kia -6.6%.
- removes prior 2.5% tariff advantage over Japan.
- 4B tariff/price reset, not hard 4C because uncertainty partly reduced.

Hyundai/Kia / robotics, AI factory, Saemangeum:
- Hyundai/Kia surged on reports of 10T won / $7B Saemangeum investment.
- Hyundai +10.5%, Kia +15%.
- robotics, AI data center, hydrogen infrastructure.
- prior Nvidia AI-chip / AI factory plan and Boston Dynamics robot capacity target.
- Stage2 robotics/AI mobility optionality, but overheat/capex ROI 4B.

Korean Air / Asiana consolidation:
- Korean Air completed $1.3B acquisition, 63.88% stake in Asiana.
- creates one of Asia’s largest airlines, world’s 12th-largest by international capacity.
- Asiana integrated by 2027, LCC units to be merged.
- Stage2 consolidation, but direct price anchor unavailable.

Jeju Air crash:
- Jeju Air shares fell as much as 15.7% to record low after fatal crash with 179 deaths.
- about 95.7B won market cap wiped.
- safety inspection of all airline operations, booking cancellations, LCC/travel agency pressure.
- hard 4C safety/trust break.

China visa-free tourism leisure basket:
- South Korea offers visa-free entry for Chinese tourist groups from Sep 29, 2025 to Jun 2026.
- Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%.
- R9 leisure/tourism Stage2-Actionable, but visitor basket/OP gate remains.

HD Hyundai Marine Solution:
- IPO priced at 83,400 won, raised about 742B won / $546M.
- shares opened almost +44% and WSJ reported close +97% at 163,900 won.
- marine after-sales, repair, retrofit, green-vessel servicing.
- Stage2-Actionable marine aftermarket IPO.

HD Hyundai Heavy / Hyundai Mipo merger:
- merger aimed at U.S.-Korea shipbuilding cooperation and MASGA project.
- HD Hyundai Heavy +11.3%, Hyundai Mipo +14.6%, both record highs.
- exchange ratio 1 Mipo share for 1.04059146 HD Hyundai Heavy shares.
- Stage2-Actionable shipbuilding/transport-infra consolidation, but merger execution and defense contract gate.
```

---

# 4. 선정 case 요약

| bucket                                 | case                                             | 핵심 판정                                                               |
| -------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------- |
| structural_success / Stage2-Actionable | **Hyundai Motor hybrid + value-up**              | +4.7% close, 4T won buyback, hybrid target +40%                     |
| 4B-watch                               | **Hyundai/Kia U.S. auto tariff**                 | Hyundai -4.5%, Kia -6.6%, 15% tariff removes tariff edge            |
| Stage2 overheat / Yellow candidate     | **Hyundai/Kia robotics·AI factory**              | Hyundai +10.5%, Kia +15%, 10T won Saemangeum AI/robot/hydrogen      |
| Stage2 no-price                        | **Korean Air / Asiana consolidation**            | $1.3B acquisition, 63.88% stake, LCC integration                    |
| hard 4C                                | **Jeju Air fatal crash**                         | -15.7% intraday, record low, 179 deaths, 95.7B won market cap wiped |
| Stage2-Actionable leisure              | **China visa-free tourism basket**               | Hotel/casino/department-store/cosmetics basket rally                |
| Stage2-Actionable IPO                  | **HD Hyundai Marine Solution IPO**               | 83,400 won IPO → 163,900 won close, +97%                            |
| Stage2-Actionable merger               | **HD Hyundai Heavy / Hyundai Mipo MASGA merger** | +11.3% / +14.6%, record highs                                       |

---

# 5. 각 case별 trigger grid

## Case A — Hyundai Motor hybrid + shareholder-return value-up

```text
symbol = 005380
case_type = Stage2-Actionable auto hybrid + capital return
archetype = AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                          | 가격 anchor                 | outcome |
| ------- | ----------------: | ---------- | ----------------------------------------------------------------------- | ------------------------- | ------- |
| T0      |            Stage1 | 2024H1     | EV demand slowdown, hybrid demand recovery                              | no entry                  |         |
| T1      | Stage2-Actionable | 2024-08-28 | 2030 sales 5.55M, hybrid target +40%, buyback up to 4T won              | intraday +5%, close +4.7% |         |
| T2      |        validation | 2024-08-28 | shareholder return to 35% of profit, quarterly dividend floor 2,500 won | same                      |         |
| T3      |          4B-watch | 2025~      | U.S. tariff, Georgia localization, hybrid margin, China weakness        | 4B                        |         |
| T4      |     Stage3-Yellow | N/A        | hybrid sales/margin and buyback execution confirmation needed           | 보류                        |         |

Hyundai Motor는 이번 R9의 가장 깨끗한 Stage2-Actionable이다. 2024년 8월 28일 투자자행사에서 Hyundai는 2030년 global sales 5.55M대, 2028년 hybrid sales 1.33M대, 2025~2027년 최대 4T won buyback, profit의 35% shareholder return을 제시했다. Reuters는 발표 후 주가가 장중 +5%, 종가 +4.7%였다고 보도했다. 이 trigger가 좋은 이유는 “EV 둔화 방어”와 “capital return”이 동시에 닫혔기 때문이다. 다만 U.S. tariff와 localization cost, hybrid margin이 4B다. ([Reuters][1])

```json
{
  "case_id": "r9_loop17_hyundai_hybrid_valueup",
  "symbol": "005380",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_auto_hybrid_valueup",
  "trigger_date": "2024-08-28",
  "global_sales_target_2030_mn_units": 5.55,
  "sales_growth_vs_2023_pct": 30,
  "hybrid_sales_target_2028_mn_units": 1.33,
  "hybrid_target_raise_pct": 40,
  "buyback_2025_2027_krw_trn": 4.0,
  "shareholder_return_ratio_pct": 35,
  "event_return_intraday_pct": 5.0,
  "event_return_close_pct": 4.7,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_hybrid_valueup"
}
```

---

## Case B — Hyundai/Kia U.S. auto tariff reset

```text
symbols = 005380 / 000270 / 012330
case_type = 4B tariff / localization risk
archetype = AUTO_TARIFF_LOCALIZATION_4B
```

| trigger |          type | date       | 당시 공개 evidence                                                       | 가격 anchor                | outcome |
| ------- | ------------: | ---------- | -------------------------------------------------------------------- | ------------------------ | ------- |
| T0      |     4B tariff | 2025-07-31 | U.S.-Korea trade deal sets auto import tariff at 15%                 | Hyundai -4.5%, Kia -6.6% |         |
| T1      |    validation | 2025-07-31 | tariff lower than 25%, but removes Korea’s 2.5% advantage over Japan | 4B                       |         |
| T2      |   relief / 4B | 2026-01-27 | Trump 25% post: Hyundai -4.8% early → +1.1%; Kia -6% early → -1%     | volatile                 |         |
| T3      | Stage2 relief | N/A        | tariff finality + U.S. localization margin needed                    | 보류                       |         |

Hyundai/Kia tariff case는 R9의 핵심 4B다. 2025년 7월 U.S.-Korea trade deal에서 auto import tariff가 15%로 정해지자 Hyundai는 -4.5%, Kia는 -6.6% 하락했다. 15%는 기존 25%보다 낮지만, Korea-U.S. FTA 아래 한국차가 일본차 대비 누리던 2.5% tariff advantage가 사라진다는 점이 부정적이었다. 2026년 1월 Trump가 25% 인상을 시사했을 때도 Hyundai는 장초반 -4.8%에서 +1.1%로 회복하고 Kia도 -6%에서 -1%로 회복했으나, 이는 “tariff uncertainty 4B”가 여전히 살아 있다는 뜻이다. ([Reuters][2])

```json
{
  "case_id": "r9_loop17_hyundai_kia_us_auto_tariff",
  "symbols": "005380/000270/012330",
  "best_trigger": "T0/T2",
  "best_trigger_type": "4B_auto_tariff_localization_risk",
  "trigger_date": "2025-07-31",
  "us_auto_tariff_rate_pct": 15,
  "hyundai_event_return_pct": -4.5,
  "kia_event_return_pct": -6.6,
  "lost_tariff_advantage_vs_japan_pct": 2.5,
  "relief_trigger_date": "2026-01-27",
  "hyundai_early_drop_pct": -4.8,
  "hyundai_relief_return_pct": 1.1,
  "kia_early_drop_pct": -6.0,
  "kia_relief_return_pct": -1.0,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "tariff_4B_not_hard_4C"
}
```

---

## Case C — Hyundai/Kia robotics, AI factory, Saemangeum investment

```text
symbols = 005380 / 000270
case_type = Stage2 mobility robotics / AI factory overheat
archetype = MOBILITY_ROBOTICS_AI_FACTORY_STAGE2_OVERHEAT
```

| trigger |                        type | date       | 당시 공개 evidence                                                                          | 가격 anchor                | outcome |
| ------- | --------------------------: | ---------- | --------------------------------------------------------------------------------------- | ------------------------ | ------- |
| T0      |                      Stage1 | 2026-01    | Hyundai/Boston Dynamics Atlas robot public demo; 30,000 robot units/year by 2028 target | no stock anchor          |         |
| T1      |          Stage2 speculative | 2026-02-11 | Boston Dynamics CEO stepping down; robot commercialization expectation                  | Hyundai +5.9%, Kia +4.6% |         |
| T2      | Stage2-Actionable candidate | 2026-02-25 | reports of 10T won / $7B Saemangeum robotics·AI data-center·hydrogen investment         | Hyundai +10.5%, Kia +15% |         |
| T3      |                    4B-watch | 2026~      | capex ROI, robotics commercialization, AI-chip depreciation, policy-location risk       | 4B                       |         |
| T4      |               Stage3-Yellow | N/A        | robot deployment revenue/productivity and AI factory utilization needed                 | 보류                       |         |

Hyundai/Kia robotics는 단순 auto가 아니라 “mobility → AI factory/robotics”로 rerating되는 Stage2다. Reuters는 2026년 2월 25일 Saemangeum 지역 10T won, 약 $7B 투자 보도에 Hyundai +10.5%, Kia +15%가 급등했다고 보도했고, 투자 내용은 robotics, AI data center, hydrogen infrastructure로 설명됐다. 앞서 Boston Dynamics CEO 교체 보도 때도 Hyundai +5.9%, Kia +4.6% 반응이 있었다. 다만 이건 아직 revenue가 아니라 optionality와 capex라서 Green은 아니다. ([Reuters][3])

```json
{
  "case_id": "r9_loop17_hyundai_kia_robotics_ai_factory",
  "symbols": "005380/000270",
  "best_trigger": "T2/T3",
  "best_trigger_type": "Stage2_mobility_robotics_AI_factory_overheat",
  "ceo_change_trigger_date": "2026-02-11",
  "hyundai_ceo_change_event_return_pct": 5.9,
  "kia_ceo_change_event_return_pct": 4.6,
  "saemangeum_trigger_date": "2026-02-25",
  "saemangeum_investment_krw_trn": 10,
  "saemangeum_investment_usd_bn": 7,
  "hyundai_saemangeum_event_return_pct": 10.5,
  "kia_saemangeum_event_return_pct": 15,
  "robot_capacity_target_annual_units_2028": 30000,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_robotics_AI_optional_overheat_not_Green"
}
```

---

## Case D — Korean Air / Asiana airline consolidation

```text
symbols = 003490 / 020560 / 180640 / 089590
case_type = Stage2 airline consolidation no direct price
archetype = AIRLINE_CONSOLIDATION_STAGE2_NO_PRICE
```

| trigger |              type | date       | 당시 공개 evidence                                                            | 가격 anchor         | outcome |
| ------- | ----------------: | ---------- | ------------------------------------------------------------------------- | ----------------- | ------- |
| T0      |   Stage2 approval | 2024-11-29 | Korean Air to combine Jin Air with Asiana LCC units after EU approval     | price unavailable |         |
| T1      | Stage2 completion | 2024-12-12 | Korean Air completes $1.3B acquisition, 63.88% stake in Asiana            | price unavailable |         |
| T2      |        validation | 2025-03-11 | new branding; Asiana to operate subsidiary until full integration by 2027 | no price          |         |
| T3      |          4B-watch | 2024~2027  | route remedies, mileage integration, labor, fuel/FX, fare-cap scrutiny    | 4B                |         |
| T4      |     Stage3-Yellow | N/A        | synergy, yield, cost, LCC integration evidence needed                     | 보류                |         |

Korean Air/Asiana는 항공 consolidation Stage2다. Reuters는 Korean Air가 Asiana 63.88% stake 인수를 완료해 Asia-Pacific 대형 airline group을 만들었고, 국제 capacity 기준 세계 12위권 carrier가 된다고 보도했다. LCC 쪽에서는 Jin Air가 Air Busan/Air Seoul을 흡수해 대형 budget carrier를 만들 계획이다. 다만 direct stock price anchor를 확보하지 못했고, route remedies, mileage program, LCC integration, fuel/FX가 4B다. ([Reuters][4])

```json
{
  "case_id": "r9_loop17_korean_air_asiana_consolidation",
  "symbols": "003490/020560/180640/089590",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_airline_consolidation_no_direct_price",
  "completion_date": "2024-12-12",
  "deal_value_usd_bn": 1.3,
  "korean_air_asiana_stake_pct": 63.88,
  "global_capacity_rank_context": 12,
  "full_integration_target": 2027,
  "lcc_integration": "Jin_Air_to_absorb_Air_Busan_Air_Seoul",
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_airline_consolidation_no_price"
}
```

---

## Case E — Jeju Air fatal crash / LCC safety trust break

```text
symbol = 089590
case_type = hard 4C airline safety / consumer-trust break
archetype = LCC_SAFETY_TRUST_HARD_4C
```

| trigger |       type | date          | 당시 공개 evidence                                                              | 가격 anchor                            | outcome |
| ------- | ---------: | ------------- | --------------------------------------------------------------------------- | ------------------------------------ | ------- |
| T0      |    hard 4C | 2024-12-29/30 | fatal Jeju Air crash at Muan, 179 deaths                                    | Jeju Air -15.7% intraday, record low |         |
| T1      | validation | 2024-12-30    | about 95.7B won market cap wiped; first fatal crash for Jeju Air since 2005 | 4C                                   |         |
| T2      |  sector 4B | 2024-12~2025  | all-airline safety inspections, B737-800 reviews, package cancellations     | LCC/travel pressure                  |         |
| T3      |   recovery | N/A           | compensation finality, safety audit, booking/load-factor recovery needed    | 보류                                   |         |

Jeju Air는 R9의 hard 4C다. Reuters는 179명이 사망한 fatal crash 이후 Jeju Air 주가가 장중 최대 -15.7% 하락해 record low를 찍고, 약 95.7B won market cap이 사라졌다고 보도했다. 이는 단순 항공주 조정이 아니라 safety/trust thesis break다. 이후 정부는 항공운항 전반에 대한 safety inspection을 지시했고, LCC와 여행사에도 booking cancellation pressure가 발생했다. ([Reuters][5])

```json
{
  "case_id": "r9_loop17_jeju_air_crash_hard_4c",
  "symbol": "089590",
  "best_trigger": "T0/T3",
  "best_trigger_type": "hard_4C_LCC_safety_trust_break",
  "trigger_date": "2024-12-30",
  "fatalities": 179,
  "intraday_event_return_pct": -15.7,
  "market_cap_wiped_krw_bn": 95.7,
  "price_context": "record_low",
  "regulatory_response": [
    "system_wide_airline_safety_inspection",
    "Boeing_737_800_review",
    "Jeju_Air_safety_rating_review"
  ],
  "recovery_gate_missing": [
    "compensation_finality",
    "booking_recovery",
    "load_factor_recovery",
    "safety_audit_completion",
    "brand_trust_repair"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "hard_4C_success_airline_safety"
}
```

---

## Case F — China visa-free tourism / leisure basket

```text
symbols = 008770 / 034230 / 069960 / 123690 / travel_basket
case_type = Stage2-Actionable leisure / inbound tourism
archetype = CHINA_TOURISM_LEISURE_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                                            | 가격 anchor            | outcome |
| ------- | ----------------: | ---------- | ----------------------------------------------------------------------------------------- | -------------------- | ------- |
| T0      |     Stage2 policy | 2025-08-06 | Korea announces visa-free entry for Chinese tourist groups from Sep 29 to Jun 2026        | leisure basket rally |         |
| T1      | Stage2-Actionable | 2025-08-06 | Hyundai Dept +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%           | direct event returns |         |
| T2      |        validation | 2025-09-29 | groups of 3+ can stay 15 days; Shilla organizes cruise tours; Chinese payments integrated | no new price         |         |
| T3      |          4B-watch | 2025~2026  | temporary window, low-spend tourism, geopolitical/protest risk, basket size               | 4B                   |         |
| T4      |     Stage3-Yellow | N/A        | visitor volume, casino/duty-free/hotel OP conversion needed                               | 보류                   |         |

이 case는 R5에서도 소비재 관점으로 봤지만, R9에서는 leisure/transport demand trigger로 다시 의미가 있다. Reuters는 visa-free entry 정책 발표 후 Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%가 올랐다고 보도했다. R9에서는 이 trigger를 “항공/호텔/카지노/면세 inbound demand”로 보되, visitor count가 아니라 basket size와 OP conversion이 Yellow gate다. ([Reuters][6])

```json
{
  "case_id": "r9_loop17_china_visa_free_leisure_basket",
  "symbols": "008770/034230/069960/123690/travel_basket",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_leisure_inbound_tourism",
  "trigger_date": "2025-08-06",
  "visa_free_period": "2025-09-29_to_2026-06",
  "hyundai_department_store_event_return_pct": 7.1,
  "hotel_shilla_event_return_pct": 4.8,
  "paradise_event_return_pct": 2.9,
  "hankook_cosmetics_event_return_pct": 9.9,
  "pilot_rule": "Chinese_tour_groups_3_or_more_can_stay_15_days",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_inbound_leisure"
}
```

---

## Case G — HD Hyundai Marine Solution IPO / marine aftermarket

```text
symbol = 443060
case_type = Stage2-Actionable marine aftermarket IPO
archetype = MARINE_AFTERMARKET_IPO_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                             | 가격 anchor              | outcome |
| ------- | ----------------: | ---------- | -------------------------------------------------------------------------- | ---------------------- | ------- |
| T0      |       IPO pricing | 2024-04-24 | IPO priced at 83,400 won, raised 742B won / $546M                          | no trading yet         |         |
| T1      | Stage2-Actionable | 2024-05-08 | shares opened almost +44%; WSJ says closed +97% at 163,900 won             | +44% open / +97% close |         |
| T2      |        validation | 2024       | marine after-sales, retrofit, repair, green-vessel demand, OP +42% in 2023 | same                   |         |
| T3      |          4B-watch | 2024~      | KKR stake overhang, valuation, shipping cycle, parent control              | 4B                     |         |
| T4      |     Stage3-Yellow | N/A        | recurring retrofit demand and margin durability needed                     | 보류                     |         |

HD Hyundai Marine Solution은 R9의 clean Stage2-Actionable IPO다. Reuters Breakingviews는 IPO가 742B won, $546M를 조달했고, debut에서 shares가 early trading +40% 이상 올랐다고 보도했다. WSJ는 issue price 83,400원 대비 종가 163,900원으로 +97%였다고 보도했다. 사업은 ship repair, maintenance, reconstruction, green-vessel retrofit after-sales라서 R9 운송서비스/해양 aftermarket에 들어간다. 단, KKR overhang과 shipping cycle이 4B다. ([Reuters][7])

```json
{
  "case_id": "r9_loop17_hd_hyundai_marine_solution_ipo",
  "symbol": "443060",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_marine_aftermarket_IPO",
  "ipo_date": "2024-05-08",
  "issue_price_krw": 83400,
  "debut_open_price_krw": 119900,
  "early_trading_return_pct": 44,
  "close_price_krw": 163900,
  "close_return_pct": 97,
  "ipo_raise_krw_bn": 742.26,
  "ipo_raise_usd_mn": 546,
  "market_cap_close_krw_trn": 7.29,
  "business": [
    "ship_repair",
    "marine_after_sales",
    "retrofit",
    "maintenance",
    "green_vessel_servicing"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_marine_aftermarket_IPO"
}
```

---

## Case H — HD Hyundai Heavy / HD Hyundai Mipo MASGA merger

```text
symbols = 329180 / 010620
case_type = Stage2-Actionable shipbuilding / transport infra consolidation
archetype = SHIPBUILDING_MERGER_US_NAVAL_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                                                    | 가격 anchor                                  | outcome |
| ------- | ----------------: | ---------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------ | ------- |
| T0      |            Stage1 | 2025       | U.S.-Korea shipbuilding cooperation, MASGA, naval/icebreaker demand                               | no entry                                   |         |
| T1      | Stage2-Actionable | 2025-08-27 | HD Hyundai Heavy to merge with HD Hyundai Mipo                                                    | HD Heavy +11.3%, Mipo +14.6%, record highs |         |
| T2      |        validation | 2025-08-27 | exchange ratio 1 Mipo share for 1.04059146 HD Heavy shares; merger launch target December         | same                                       |         |
| T3      |          4B-watch | 2025~      | merger execution, U.S. contract conversion, valuation/exchange-ratio disputes, defense-cycle risk | 4B                                         |         |
| T4      |     Stage3-Yellow | N/A        | U.S. naval/icebreaker contract and margin backlog needed                                          | 보류                                         |         |

HD Hyundai Heavy/Mipo merger는 R9 transport-infrastructure/shipbuilding Stage2-Actionable이다. Reuters는 HD Hyundai Heavy가 U.S.-Korea shipbuilding cooperation, MASGA project, K-defense/naval demand를 겨냥해 affiliate HD Hyundai Mipo와 합병한다고 보도했고, 발표 전후 HD Hyundai Heavy는 +11.3%, HD Hyundai Mipo는 +14.6%로 record highs를 기록했다. 다만 실제 Green은 U.S. naval/icebreaker contracts, backlog margin, merger execution이 닫혀야 한다. ([Reuters][8])

```json
{
  "case_id": "r9_loop17_hd_hyundai_heavy_mipo_masga_merger",
  "symbols": "329180/010620",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_shipbuilding_transport_infra_merger",
  "trigger_date": "2025-08-27",
  "hd_hyundai_heavy_event_return_pct": 11.3,
  "hd_hyundai_mipo_event_return_pct": 14.6,
  "price_context": "both_record_highs",
  "share_exchange_ratio": "1_Mipo_share_for_1.04059146_HD_Hyundai_Heavy_shares",
  "merger_launch_target": "2025-12",
  "strategic_logic": [
    "MASGA",
    "US_Korea_shipbuilding_cooperation",
    "naval_vessel_demand",
    "icebreaker_demand",
    "K_defence_shipbuilding"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_shipbuilding_merger"
}
```

---

# 6. Trigger별 실제 가격경로 검증 요약

이번 R9 Loop 17은 full OHLC가 없으므로, 아래 표는 **reported event anchor 기준**이다.

| case                      | best trigger |                                   event return / price | market-relative | full MFE/MAE | outcome                            |
| ------------------------- | -----------: | -----------------------------------------------------: | --------------: | ------------ | ---------------------------------- |
| Hyundai hybrid + value-up |           T1 |                              +5% intraday, +4.7% close |     unavailable | unavailable  | excellent Stage2-Actionable        |
| Hyundai/Kia tariff        |           T0 |                               Hyundai -4.5%, Kia -6.6% |     unavailable | unavailable  | auto tariff 4B                     |
| Hyundai/Kia robotics AI   |           T2 |                               Hyundai +10.5%, Kia +15% |          strong | unavailable  | Stage2 overheat / Yellow candidate |
| Korean Air / Asiana       |           T1 |                                      price unavailable |             N/A | unavailable  | Stage2 consolidation no-price      |
| Jeju Air crash            |           T0 |      -15.7% intraday, record low, 95.7B won mcap wiped |        negative | unavailable  | hard 4C                            |
| China tourism leisure     |           T1 | Hotel Shilla +4.8%, Paradise +2.9%, Hyundai Dept +7.1% |        positive | unavailable  | Stage2-Actionable                  |
| HD Hyundai Marine IPO     |           T1 |                       83,400 → 163,900 won, +97% close |          strong | unavailable  | Stage2-Actionable                  |
| HD Hyundai Heavy/Mipo     |           T1 |                          +11.3% / +14.6%, record highs |          strong | unavailable  | Stage2-Actionable                  |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
가장 좋은 Stage2:
1. HD Hyundai Marine Solution IPO: +97% close, clear IPO/aftermarket trigger.
2. HD Hyundai Heavy / Mipo merger: +11.3% / +14.6%, MASGA/U.S. shipbuilding trigger.
3. Hyundai Motor hybrid + value-up: +4.7% close, 4T won buyback, hybrid sales target.
4. Hyundai/Kia robotics AI: +10.5% / +15%, but capex/overheat risk.
5. China tourism leisure basket: direct hotel/casino/retail stock reaction.
```

## Stage2-Actionable entry 성과

```text
Stage2-Actionable:
- Hyundai Motor hybrid + value-up.
- HD Hyundai Marine Solution IPO.
- HD Hyundai Heavy / Hyundai Mipo MASGA merger.
- China visa-free tourism leisure basket.

Actionable 보류:
- Hyundai/Kia robotics AI: price reaction strong, but capex ROI and commercialization are missing.
- Korean Air/Asiana: consolidation strong, but direct price unavailable.
- Hyundai/Kia tariff: negative 4B.
- Jeju Air crash: hard 4C, no positive entry.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Hyundai Motor if hybrid sales/margin and buyback execution confirm.
- Hyundai/Kia robotics if robot deployment/productivity and AI-factory utilization appear.
- Korean Air if synergy, route yield, LCC integration and margin confirm.
- HD Hyundai Marine if recurring retrofit/aftermarket demand and margin durability confirm.
- HD Hyundai Heavy/Mipo if U.S. naval/icebreaker contracts and merger integration confirm.
- China leisure basket if visitor volume, casino/drop, hotel occupancy and duty-free basket convert to OP.
```

## Stage3-Green

```text
이번 R9 Loop 17에서 확정 Green 없음.

이유:
- full OHLC/MFE/MAE가 없다.
- auto hybrid/value-up은 좋지만 tariff and localization 4B가 있다.
- robotics/AI는 revenue가 아니라 optionality/capex다.
- airline consolidation은 synergy and fare/yield evidence가 아직 없다.
- leisure tourism은 visitor basket and OP conversion이 필요하다.
- shipping/shipbuilding IPO/merger는 강하지만 cycle and execution gates가 남아 있다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Hyundai hybrid + value-up as Stage2-Actionable.
- Hyundai/Kia tariff as 4B.
- Hyundai/Kia robotics AI as Stage2 overheat / Yellow candidate.
- Korean Air/Asiana as Stage2 no-price.
- Jeju Air crash as hard 4C.
- China tourism leisure as Stage2-Actionable.
- HD Hyundai Marine IPO as Stage2-Actionable.
- HD Hyundai Heavy/Mipo merger as Stage2-Actionable.

false_positive_score:
- Hyundai robotics promoted to Green without revenue/capex ROI.
- Korean Air promoted to Green without synergy/yield price validation.
- tourism basket promoted to Green without basket size and OP.
- Hyundai hybrid promoted without tariff/localization adjustment.
- HD Hyundai Marine or Heavy/Mipo promoted without cycle/execution check.

evidence_good_but_price_failed:
- none primary in R9 with clear positive evidence and negative close, except tariff-negative autos are classified as 4B.

event_premium:
- Hyundai/Kia robotics AI.
- HD Hyundai Marine IPO.
- HD Hyundai Heavy/Mipo MASGA merger.
- China tourism leisure basket.

thesis_break:
- Jeju Air crash.

hard_4C:
- Jeju Air safety/trust break confirmed.
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
hybrid_mix_margin,+5,"EV 둔화 국면에서 hybrid mix and margin 방어가 auto Stage2 핵심","Hyundai"
shareholder_return_auto,+4,"buyback/dividend 정책이 가격반응과 닫히면 Stage2-Actionable","Hyundai"
robotics_AI_mobility_optionality,+4,"AI factory/robotics는 mobility rerating option","Hyundai/Kia"
airline_consolidation_synergy,+4,"항공 consolidation은 route/yield/cost synergy 확인 시 Yellow 후보","Korean Air/Asiana"
safety_trust_risk,+5,"항공 fatal accident는 hard 4C","Jeju Air"
inbound_tourism_policy,+4,"visa-free 정책과 stock basket reaction이 닫히면 Stage2","Hotel Shilla/Paradise"
marine_aftermarket_demand,+5,"green-vessel retrofit and ship-service demand는 transport aftermarket Stage2","HD Hyundai Marine"
shipbuilding_US_naval_demand,+5,"MASGA/U.S. naval demand와 가격반응이 닫히면 Stage2","HD Hyundai Heavy/Mipo"
```

## 내릴 축

```csv
axis,delta,reason,cases
auto_growth_without_tariff_adjustment,-5,"U.S. tariff를 빼지 않으면 auto false positive","Hyundai/Kia"
robotics_AI_without_revenue,-5,"robotics/AI factory는 매출·productivity 전 Green 금지","Hyundai/Kia"
airline_merger_without_synergy,-4,"항공합병 headline만으로 Green 금지","Korean Air/Asiana"
tourism_headline_without_basket_size,-5,"입국객 숫자만으로 leisure Green 금지","Hotel Shilla/Paradise"
IPO_without_cycle_risk,-4,"marine/transport IPO는 shipping cycle and overhang 조정 필요","HD Hyundai Marine"
shipbuilding_merger_without_contract,-4,"MASGA 기대만으로 Green 금지, 실제 contract 필요","HD Hyundai Heavy/Mipo"
safety_event_ignored,-5,"fatal crash and cancellations를 무시하면 LCC false positive","Jeju Air"
localization_without_execution,-4,"U.S./domestic localization capex는 execution/cost 확인 전 Green 금지","Hyundai/Kia"
```

---

# 10. Stage2-Actionable 승격 조건

R9 Loop 17 shadow rule:

```text
R9에서 Stage2 evidence가 아래 중 4개 이상이면 Stage2-Actionable로 승격한다.

1. event return +5% 이상 또는 clear reported positive price anchor
2. hybrid/production/capacity/route/visitor/shipping demand가 구체적이다
3. buyback/dividend/IPO/merger/deal value가 숫자로 닫힌다
4. margin path가 hybrid mix, yield, load factor, retrofit, contract backlog로 연결된다
5. tariff/safety/fuel/FX/capex/cycle 4B가 식별 가능하다
6. price reaction이 evidence와 같은 방향으로 검증된다
7. one-off headline이 아니라 반복 매출/수익률로 이어질 path가 있다
```

적용:

```text
Hyundai hybrid:
2,3,4,5,6 충족 → Stage2-Actionable.

HD Hyundai Marine:
1,2,3,4,5,6 충족 → Stage2-Actionable.

HD Hyundai Heavy/Mipo:
1,2,3,4,5,6 충족 → Stage2-Actionable.

China leisure:
1,2,5,6 충족. OP conversion 부족 → Stage2-Actionable.

Hyundai robotics:
1,2,3,5,6 충족 but 4/7 미흡 → Stage2 overheat / Yellow candidate.

Korean Air:
2,3,4,5 충족 but price 없음 → Stage2 no-price.

Jeju Air:
negative hard 4C → 승격 금지.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
Stage2-Actionable 이후 아래 중 2개 이상이 추가로 닫히면 Yellow.

1. hybrid sales/margin and U.S. localization cost are confirmed.
2. buyback/dividend execution continues.
3. robotics deployment creates productivity/revenue signal.
4. airline consolidation produces yield/cost/load-factor improvement.
5. tourism visitor volume converts into basket size and OP.
6. marine aftermarket demand produces recurring margin.
7. shipbuilding merger converts into U.S. naval/icebreaker contracts.
8. safety/trust 4C is contained and bookings recover.
```

Yellow 후보:

```text
Hyundai:
hybrid margin + buyback execution + tariff mitigation.

Hyundai/Kia robotics:
robot units deployed + AI factory utilization + productivity.

Korean Air:
Asiana/LCC integration + route yield + cost synergy.

HD Hyundai Marine:
aftermarket order growth + margin durability.

HD Hyundai Heavy/Mipo:
U.S. shipbuilding contracts + merger execution.

China leisure:
visitor/basket/OP conversion.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- Stage2 trigger converts into recurring EPS/OP/FCF.
- tariff/fuel/FX/capex/safety 4B is reduced.
- transportation demand shows volume and yield.
- robotics/AI optionality becomes measurable productivity or revenue.
- IPO/merger execution proves margin and backlog.
- full-window MFE/MAE is favorable.
```

이번 R9 Loop 17에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + margin/yield/load-factor/basket/contract/productivity gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- U.S. auto tariff reset.
- hybrid strategy without actual margin.
- robotics/AI capex without revenue.
- airline merger without synergy.
- fuel/FX shock.
- tourism policy without basket size.
- shipping IPO/merger cycle overheat.
- fatal safety accident / inspection / cancellation.
```

적용:

```text
Hyundai/Kia:
tariff and localization 4B.

Hyundai robotics:
capex ROI and commercialization 4B.

Korean Air:
integration/yield/fuel/FX 4B.

Jeju Air:
hard 4C safety/trust.

China tourism:
temporary policy window and low-spend tourism 4B.

HD Hyundai Marine:
IPO valuation/cycle/KKR overhang 4B.

HD Hyundai Heavy/Mipo:
merger execution and contract conversion 4B.
```

---

# 14. 4C hard gate 조건

```text
R9 4C:
- fatal safety accident with stock crash and system-wide inspection
- regulatory grounding / flight suspension
- large compensation and booking collapse
- production plant shutdown from legal/safety event
- tariff shock causing structural export-margin break
- merger failure after consolidation premium
```

이번 R9 Loop 17 hard/strong 4C:

```text
Jeju Air fatal crash = hard_4C_success
```

Hard 4C not yet confirmed:

```text
Hyundai/Kia tariff = 4B, not hard 4C.
Korean Air/Asiana integration = Stage2 no-price, not 4C.
Hyundai Georgia/robotics capex = Stage2/4B, not 4C.
HD Hyundai Marine IPO and HD Hyundai Heavy/Mipo merger = Stage2-Actionable, not 4C.
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R9 production 설계 원칙:

```text
1. auto sales strategy와 tariff-adjusted margin을 분리한다.
2. hybrid/value-up은 Stage2-Actionable이 될 수 있지만, Green은 margin and execution 확인 후다.
3. robotics/AI mobility는 optionality와 revenue/productivity를 분리한다.
4. airline consolidation은 synergy/yield/load factor 확인 전까지 Stage2다.
5. fatal aviation safety event는 hard 4C다.
6. tourism policy는 visitor count가 아니라 basket size and OP conversion을 본다.
7. marine IPO/shipbuilding merger는 shipping cycle, overhang, actual contract를 확인한다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_258.md 요약

```md
# R9 Loop 17. Mobility / Transport / Leisure Trigger-level Price Validation

이번 라운드는 R9 Loop 17 trigger-level validation 라운드다.

핵심 결론:
- Hyundai Motor hybrid + value-up is the cleanest R9 auto Stage2-Actionable. Hyundai targeted 5.55M global sales by 2030, raised its hybrid target to 1.33M by 2028, announced up to 4T won buyback from 2025~2027 and a 35% profit shareholder-return policy. Shares rose as much as 5% and closed +4.7%.
- Hyundai/Kia U.S. auto tariff is 4B. After the U.S.-Korea trade deal set auto tariffs at 15%, Hyundai fell 4.5% and Kia 6.6%. The lower tariff reduced uncertainty but removed Korea's prior 2.5% edge over Japanese automakers.
- Hyundai/Kia robotics and AI factory is Stage2 overheat / Yellow candidate. Hyundai +10.5% and Kia +15% on reports of 10T won / $7B Saemangeum robotics, AI data-center and hydrogen investment. Green requires robot deployment revenue/productivity and capex ROI.
- Korean Air / Asiana is Stage2 consolidation no-price. Korean Air completed a $1.3B acquisition of 63.88% of Asiana, creating one of Asia's largest airlines and planning LCC integration. Direct price anchor unavailable.
- Jeju Air crash is hard 4C. Jeju Air shares fell as much as 15.7% to record low after a crash that killed 179 people, wiping about 95.7B won in market cap. System-wide safety inspection and booking cancellations followed.
- China visa-free tourism is Stage2-Actionable leisure. Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9% and Hankook Cosmetics +9.9% after visa-free Chinese group-tour policy was confirmed.
- HD Hyundai Marine Solution IPO is Stage2-Actionable marine aftermarket. IPO price was 83,400 won, the stock opened almost +44% and WSJ reported it closed +97% at 163,900 won.
- HD Hyundai Heavy / Hyundai Mipo MASGA merger is Stage2-Actionable. HD Hyundai Heavy +11.3%, Hyundai Mipo +14.6%, both record highs, on merger plan targeting U.S.-Korea shipbuilding cooperation.

Main calibration:
- Raise hybrid_mix_margin, shareholder_return_auto, robotics_AI_mobility_optionality, airline_consolidation_synergy, safety_trust_risk, inbound_tourism_policy, marine_aftermarket_demand, shipbuilding_US_naval_demand.
- Lower auto_growth_without_tariff_adjustment, robotics_AI_without_revenue, airline_merger_without_synergy, tourism_headline_without_basket_size, IPO_without_cycle_risk, shipbuilding_merger_without_contract, safety_event_ignored, localization_without_execution.
```

## docs/checkpoints/checkpoint_28a_round258_r9_loop17.md 요약

```md
# Checkpoint 28A Round 258 R9 Loop 17 Trigger-level Calibration

## 반영 내용
- R9 Loop 17 trigger-level validation을 수행했다.
- Hyundai hybrid/value-up, Hyundai/Kia tariff, Hyundai/Kia robotics AI, Korean Air/Asiana, Jeju Air crash, China tourism leisure, HD Hyundai Marine Solution IPO, HD Hyundai Heavy/Mipo merger를 검토했다.
- full adjusted OHLC는 확보하지 못했으므로 Reuters / WSJ / AP reported event return과 event price anchor를 사용했다.
- MFE/MAE는 조작하지 않고 price_data_unavailable_after_deep_search로 분리했다.

## 핵심 보정
- Hybrid strategy plus shareholder return can be Stage2-Actionable.
- Auto tariffs must be deducted before any Green classification.
- Robotics/AI mobility needs measurable revenue or productivity before Yellow/Green.
- Airline consolidation needs yield/cost/load-factor synergy before Green.
- Fatal aviation safety event with stock crash is hard 4C.
- Tourism policy needs basket-size and OP conversion before Yellow/Green.
- Marine aftermarket IPO and shipbuilding merger need cycle/contract/execution checks.
```

## data/e2r_case_library/cases_r9_loop17_round258.jsonl 초안

```jsonl
{"case_id":"r9_loop17_hyundai_hybrid_valueup","symbol":"005380","company_name":"Hyundai Motor","case_type":"Stage2_Actionable_auto_hybrid_valueup","primary_archetype":"AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2024-08-28","global_sales_target_2030_mn_units":5.55,"sales_growth_vs_2023_pct":30,"hybrid_sales_target_2028_mn_units":1.33,"hybrid_target_raise_pct":40,"buyback_2025_2027_krw_trn":4.0,"shareholder_return_ratio_pct":35,"event_return_intraday_pct":5.0,"event_return_close_pct":4.7,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_hybrid_valueup","notes":"Hybrid strategy and shareholder return aligned with price reaction; tariff/localization and margin remain gates."}
{"case_id":"r9_loop17_hyundai_kia_us_auto_tariff","symbol":"005380/000270/012330","company_name":"Hyundai Motor / Kia / Hyundai Mobis","case_type":"4B_auto_tariff_localization_risk","primary_archetype":"AUTO_TARIFF_LOCALIZATION_4B","best_trigger":"T0/T2","stage_candidate":"4B-watch","price_validation":{"trigger_date":"2025-07-31","us_auto_tariff_rate_pct":15,"hyundai_event_return_pct":-4.5,"kia_event_return_pct":-6.6,"lost_tariff_advantage_vs_japan_pct":2.5,"relief_trigger_date":"2026-01-27","hyundai_early_drop_pct":-4.8,"hyundai_relief_return_pct":1.1,"kia_early_drop_pct":-6.0,"kia_relief_return_pct":-1.0,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"tariff_4B_not_hard_4C","notes":"Tariff reset remains a margin 4B, not a hard 4C while localization and negotiated rate remain manageable."}
{"case_id":"r9_loop17_hyundai_kia_robotics_ai_factory","symbol":"005380/000270","company_name":"Hyundai Motor / Kia / Boston Dynamics","case_type":"Stage2_mobility_robotics_AI_factory_overheat","primary_archetype":"MOBILITY_ROBOTICS_AI_FACTORY_STAGE2_OVERHEAT","best_trigger":"T2/T3","stage_candidate":"Stage2_promote_candidate","price_validation":{"ceo_change_trigger_date":"2026-02-11","hyundai_ceo_change_event_return_pct":5.9,"kia_ceo_change_event_return_pct":4.6,"saemangeum_trigger_date":"2026-02-25","saemangeum_investment_krw_trn":10,"saemangeum_investment_usd_bn":7,"hyundai_saemangeum_event_return_pct":10.5,"kia_saemangeum_event_return_pct":15,"robot_capacity_target_annual_units_2028":30000,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_robotics_AI_optional_overheat_not_Green","notes":"Robotics/AI optionality moved stocks, but commercialization, productivity and capex ROI are missing."}
{"case_id":"r9_loop17_korean_air_asiana_consolidation","symbol":"003490/020560/180640/089590","company_name":"Korean Air / Asiana / Jin Air / Air Busan","case_type":"Stage2_airline_consolidation_no_direct_price","primary_archetype":"AIRLINE_CONSOLIDATION_STAGE2_NO_PRICE","best_trigger":"T1/T3","stage_candidate":"Stage2","price_validation":{"completion_date":"2024-12-12","deal_value_usd_bn":1.3,"korean_air_asiana_stake_pct":63.88,"global_capacity_rank_context":12,"full_integration_target":2027,"lcc_integration":"Jin_Air_to_absorb_Air_Busan_Air_Seoul","direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_airline_consolidation_no_price","notes":"Airline consolidation is structural, but synergy/yield/load-factor and direct stock-price validation are missing."}
{"case_id":"r9_loop17_jeju_air_crash_hard_4c","symbol":"089590","company_name":"Jeju Air","case_type":"hard_4C_LCC_safety_trust_break","primary_archetype":"LCC_SAFETY_TRUST_HARD_4C","best_trigger":"T0/T3","stage_candidate":"4C","price_validation":{"trigger_date":"2024-12-30","fatalities":179,"intraday_event_return_pct":-15.7,"market_cap_wiped_krw_bn":95.7,"price_context":"record_low","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"hard_4C_success_airline_safety","notes":"Fatal crash, record-low stock reaction, market cap wipeout and system-wide safety inspection confirm hard 4C."}
{"case_id":"r9_loop17_china_visa_free_leisure_basket","symbol":"008770/034230/069960/123690/travel_basket","company_name":"Hotel Shilla / Paradise / Hyundai Department Store / Hankook Cosmetics","case_type":"Stage2_Actionable_leisure_inbound_tourism","primary_archetype":"CHINA_TOURISM_LEISURE_STAGE2_ACTIONABLE","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2025-08-06","visa_free_period":"2025-09-29_to_2026-06","hyundai_department_store_event_return_pct":7.1,"hotel_shilla_event_return_pct":4.8,"paradise_event_return_pct":2.9,"hankook_cosmetics_event_return_pct":9.9,"pilot_rule":"Chinese_tour_groups_3_or_more_can_stay_15_days","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_inbound_leisure","notes":"Policy and leisure stock reaction aligned; basket size and OP conversion remain gates."}
{"case_id":"r9_loop17_hd_hyundai_marine_solution_ipo","symbol":"443060","company_name":"HD Hyundai Marine Solution","case_type":"Stage2_Actionable_marine_aftermarket_IPO","primary_archetype":"MARINE_AFTERMARKET_IPO_STAGE2_ACTIONABLE","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable","price_validation":{"ipo_date":"2024-05-08","issue_price_krw":83400,"debut_open_price_krw":119900,"early_trading_return_pct":44,"close_price_krw":163900,"close_return_pct":97,"ipo_raise_krw_bn":742.26,"ipo_raise_usd_mn":546,"market_cap_close_krw_trn":7.29,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_marine_aftermarket_IPO","notes":"IPO and aftermarket demand price reaction aligned; shipping cycle and KKR overhang remain 4B."}
{"case_id":"r9_loop17_hd_hyundai_heavy_mipo_masga_merger","symbol":"329180/010620","company_name":"HD Hyundai Heavy Industries / HD Hyundai Mipo","case_type":"Stage2_Actionable_shipbuilding_transport_infra_merger","primary_archetype":"SHIPBUILDING_MERGER_US_NAVAL_STAGE2_ACTIONABLE","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2025-08-27","hd_hyundai_heavy_event_return_pct":11.3,"hd_hyundai_mipo_event_return_pct":14.6,"price_context":"both_record_highs","share_exchange_ratio":"1_Mipo_share_for_1.04059146_HD_Hyundai_Heavy_shares","merger_launch_target":"2025-12","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_shipbuilding_merger","notes":"MASGA/U.S.-Korea shipbuilding trigger aligned with stock reaction; actual contract and merger execution are Yellow gates."}
```

## data/e2r_trigger_calibration/triggers_r9_loop17_round258.jsonl 초안

```jsonl
{"trigger_id":"r9l17_hyundai_hybrid_T1","case_id":"r9_loop17_hyundai_hybrid_valueup","trigger_type":"Stage2-Actionable_auto_hybrid_valueup","trigger_date":"2024-08-28","event_return_pct":4.7,"trigger_outcome_label":"excellent_stage2_actionable_hybrid_valueup","promote_to":"Stage2-Actionable"}
{"trigger_id":"r9l17_auto_tariff_T0","case_id":"r9_loop17_hyundai_kia_us_auto_tariff","trigger_type":"4B_auto_tariff_margin_reset","trigger_date":"2025-07-31","event_return_pct":"Hyundai_-4.5_Kia_-6.6","trigger_outcome_label":"auto_tariff_4B","promote_to":"4B-watch"}
{"trigger_id":"r9l17_hyundai_robotics_T2","case_id":"r9_loop17_hyundai_kia_robotics_ai_factory","trigger_type":"Stage2_robotics_AI_mobility_overheat","trigger_date":"2026-02-25","event_return_pct":"Hyundai_+10.5_Kia_+15","trigger_outcome_label":"Stage2_robotics_AI_optional_overheat","promote_to":"Stage2_promote_candidate"}
{"trigger_id":"r9l17_korean_air_asiana_T1","case_id":"r9_loop17_korean_air_asiana_consolidation","trigger_type":"Stage2_airline_consolidation_no_price","trigger_date":"2024-12-12","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"airline_consolidation_stage2_no_price","promote_to":"Stage2"}
{"trigger_id":"r9l17_jeju_air_crash_T0","case_id":"r9_loop17_jeju_air_crash_hard_4c","trigger_type":"hard_4C_airline_safety_trust_break","trigger_date":"2024-12-30","event_return_pct":-15.7,"trigger_outcome_label":"hard_4C_success_airline_safety","promote_to":"4C"}
{"trigger_id":"r9l17_china_leisure_T1","case_id":"r9_loop17_china_visa_free_leisure_basket","trigger_type":"Stage2-Actionable_inbound_leisure_policy","trigger_date":"2025-08-06","event_return_pct":"HyundaiDept_+7.1_HotelShilla_+4.8_Paradise_+2.9_HankookCosmetics_+9.9","trigger_outcome_label":"excellent_stage2_actionable_inbound_leisure","promote_to":"Stage2-Actionable"}
{"trigger_id":"r9l17_hd_hyundai_marine_ipo_T1","case_id":"r9_loop17_hd_hyundai_marine_solution_ipo","trigger_type":"Stage2-Actionable_marine_aftermarket_IPO","trigger_date":"2024-05-08","event_return_pct":97,"entry_price_krw":163900,"trigger_outcome_label":"excellent_stage2_actionable_marine_aftermarket_IPO","promote_to":"Stage2-Actionable"}
{"trigger_id":"r9l17_hd_hyundai_mipo_merger_T1","case_id":"r9_loop17_hd_hyundai_heavy_mipo_masga_merger","trigger_type":"Stage2-Actionable_shipbuilding_transport_infra_merger","trigger_date":"2025-08-27","event_return_pct":"HDHeavy_+11.3_Mipo_+14.6","trigger_outcome_label":"excellent_stage2_actionable_shipbuilding_merger","promote_to":"Stage2-Actionable"}
```

## data/sector_taxonomy/score_weight_profiles_round258_r9_loop17_v1.csv 초안

```csv
archetype,hybrid_mix_margin,shareholder_return_auto,robotics_AI_mobility_optionality,airline_consolidation_synergy,safety_trust_risk,inbound_tourism_policy,marine_aftermarket_demand,shipbuilding_US_naval_demand,auto_growth_without_tariff_adjustment_penalty,robotics_AI_without_revenue_penalty,airline_merger_without_synergy_penalty,tourism_headline_without_basket_size_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE,+5,+5,+1,+0,+1,+0,+0,+0,-5,-1,-1,-1,Hyundai hybrid+buyback +4.7%,tariff/localization margin gate,hybrid margin+buyback execution,Hyundai.
AUTO_TARIFF_LOCALIZATION_4B,+1,+0,+0,+0,+1,+0,+0,+0,-5,-1,-1,-1,U.S. tariff hits Hyundai/Kia,negative 4B,tariff relief+localized margin,Hyundai/Kia.
MOBILITY_ROBOTICS_AI_FACTORY_STAGE2_OVERHEAT,+1,+1,+5,+0,+1,+0,+0,+0,-1,-5,-1,-1,Hyundai/Kia robotics AI rally,capex/revenue missing,robot deployment+productivity,Hyundai/Kia.
AIRLINE_CONSOLIDATION_STAGE2_NO_PRICE,+0,+0,+0,+5,+3,+2,+0,+0,-1,-1,-5,-1,Korean Air/Asiana consolidation,price unavailable,route yield+cost synergy,Korean Air.
LCC_SAFETY_TRUST_HARD_4C,+0,+0,+0,+0,+5,+0,+0,+0,-1,-1,-1,-1,Jeju Air fatal crash hard 4C,recovery missing,safety audit+booking recovery,Jeju Air.
CHINA_TOURISM_LEISURE_STAGE2_ACTIONABLE,+0,+0,+0,+1,+1,+5,+0,+0,-1,-1,-1,-5,visa-free tourism leisure rally,basket/OP gate,visitor+basket+OP,Hotel Shilla/Paradise.
MARINE_AFTERMARKET_IPO_STAGE2_ACTIONABLE,+0,+0,+0,+0,+0,+0,+5,+2,-1,-1,-1,-1,HD Hyundai Marine IPO +97%,cycle/overhang,recurring retrofit margin,HD Hyundai Marine.
SHIPBUILDING_MERGER_US_NAVAL_STAGE2_ACTIONABLE,+0,+0,+0,+1,+0,+0,+1,+5,-1,-1,-2,-1,HD Heavy/Mipo MASGA merger,contract/execution gate,U.S. naval contracts+merger execution,HD Hyundai Heavy/Mipo.
```

---

# 이번 R9 Loop 17 결론

```text
1. Hyundai Motor hybrid + value-up은 R9 auto의 가장 좋은 Stage2-Actionable이다.
   4T won buyback, hybrid target +40%, 2030 sales target, +4.7% close가 닫혔다.

2. Hyundai/Kia U.S. tariff는 4B다.
   Hyundai -4.5%, Kia -6.6%; tariff uncertainty는 줄었지만 margin edge가 사라졌다.

3. Hyundai/Kia robotics·AI factory는 Stage2 overheat / Yellow 후보다.
   Hyundai +10.5%, Kia +15%였지만 robot revenue/productivity and capex ROI가 필요하다.

4. Korean Air / Asiana는 Stage2 consolidation no-price다.
   $1.3B deal, 63.88% stake, LCC integration은 구조적이지만 price anchor가 없다.

5. Jeju Air fatal crash는 hard 4C다.
   -15.7%, record low, 179 deaths, 95.7B won market cap wipeout, safety inspection이 같이 닫혔다.

6. China visa-free tourism basket은 R9 leisure Stage2-Actionable이다.
   Hotel Shilla +4.8%, Paradise +2.9%, Hyundai Dept +7.1%, Hankook Cosmetics +9.9% 반응이 있다.

7. HD Hyundai Marine Solution IPO는 Stage2-Actionable이다.
   83,400 won IPO에서 163,900 won close, +97%로 marine aftermarket demand가 가격검증됐다.

8. HD Hyundai Heavy / Hyundai Mipo MASGA merger도 Stage2-Actionable이다.
   +11.3% / +14.6%, record highs; 하지만 actual U.S. naval/icebreaker contract가 Yellow gate다.
```

한 문장으로 압축하면:

> **R9 Loop 17에서 배운 핵심은 “자동차 판매·관광객·항공합병·조선 headline”이 아니라, hybrid margin, tariff-adjusted profitability, robot productivity, airline yield, booking trust, visitor basket size, marine aftermarket margin, U.S. shipbuilding contract가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 safety crash는 이 모든 성장논리를 한 번에 끊는 hard 4C다.**

다음 순서는 **R10 Loop 17 — 건설·부동산·건자재**다.

* [Reuters](https://www.reuters.com/business/autos-transportation/hyundai-motor-targets-30-rise-sales-by-2030-it-expands-hybrid-lineup-2024-08-28/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/autos-transportation/south-korea-automaker-shares-slip-after-us-trade-deal-2025-07-31/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/retail-consumer/hyundai-motor-eyes-multi-billion-dollar-investment-south-korea-say-sources-2026-02-25/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/deals/korean-air-completes-asiana-takeover-form-one-asias-biggest-airlines-2024-12-12/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/breakingviews/ship-ipo-puts-wind-back-korea-incs-sails-2024-05-08/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/emerging/south-korean-shipbuilder-hd-hyundai-heavy-merge-with-affiliate-hd-hyundai-mipo-2025-08-27/?utm_source=chatgpt.com)

[1]: https://www.reuters.com/business/autos-transportation/hyundai-motor-targets-30-rise-sales-by-2030-it-expands-hybrid-lineup-2024-08-28/ "Hyundai targets 30% rise in sales by 2030, as it doubles hybrid lineups | Reuters"
[2]: https://www.reuters.com/business/autos-transportation/south-korea-automaker-shares-slip-after-us-trade-deal-2025-07-31/?utm_source=chatgpt.com "South Korea automaker shares slip after US trade deal"
[3]: https://www.reuters.com/business/retail-consumer/hyundai-motor-eyes-multi-billion-dollar-investment-south-korea-say-sources-2026-02-25/?utm_source=chatgpt.com "Hyundai Motor to unveil multi-billion-dollar investment in South Korea, source says"
[4]: https://www.reuters.com/markets/deals/korean-air-completes-asiana-takeover-form-one-asias-biggest-airlines-2024-12-12/?utm_source=chatgpt.com "Korean Air completes Asiana takeover to form one of Asia's biggest airlines"
[5]: https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com "Jeju Air shares plummet to record low after deadly plane crash"
[6]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/ "South Korea to offer visa-free entry to Chinese tourists from late September | Reuters"
[7]: https://www.reuters.com/breakingviews/ship-ipo-puts-wind-back-korea-incs-sails-2024-05-08/?utm_source=chatgpt.com "Ship IPO puts wind back in Korea Inc's sails"
[8]: https://www.reuters.com/markets/emerging/south-korean-shipbuilder-hd-hyundai-heavy-merge-with-affiliate-hd-hyundai-mipo-2025-08-27/?utm_source=chatgpt.com "South Korean shipbuilder HD Hyundai Heavy to merge with affiliate HD Hyundai Mipo"
