순서상 이번은 **R9 Loop 16 — 모빌리티·운송·레저 trigger-level price validation 라운드**다.

이번 R9는 **완성차·부품·로봇·항공·해운·물류·관광·카지노/면세**를 한 번에 묶으면 안 된다. 실제 가격은 **관세 → 마진**, **현지화 투자 → tariff hedge**, **하이브리드/EREV 전략 → 판매·OP margin**, **로봇 → 장기 optionality와 노조 4B**, **항공 사고 → 안전 신뢰 hard 4C**, **중국 관광객 → 객단가/항공운임/카지노 drop**, **해운 운임 → freight rate duration**으로 따로 반응한다.

```text
round = R9 Loop 16
round_id = round_245
large_sector = MOBILITY_TRANSPORT_LEISURE
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R10 Loop 16
```

이번 세션에서는 KRX/Naver/Yahoo/Stooq 수정주가 일봉 OHLC window를 안정적으로 직접 확보하지 못했다. finance tool도 KRX ticker를 처리하지 못했다. 따라서 full MFE/MAE는 만들지 않고 `price_data_unavailable_after_deep_search`로 분리한다. 대신 Reuters/FT/WSJ/AP/MarketWatch가 보도한 **reported event return, event price, deal value, tariff rate, capacity, fatalities, user/passenger/visitor data**를 trigger anchor로 쓴다. Stage 판정과 OHLC backfill 상태는 분리한다.

---

# 1. 이번 라운드 대섹터

```text
R9 = 모빌리티·운송·레저
```

R9의 core gate는 아래다.

```text
완성차:
hybrid / EREV strategy → sales mix → ASP → OP margin → shareholder return → tariff impact

현지화 / 관세:
U.S. tariff → export margin → U.S. plant / steel sourcing / Georgia capacity → tariff hedge → capex ROI

로봇 / future mobility:
Boston Dynamics / humanoid → commercialization → plant deployment → unit economics → labor conflict → valuation

물류 / car carrier:
export route disruption → delivery delay → fuel cost → Hyundai Glovis utilization → automaker inventory / margin

항공:
merger approval → route rationalization → capacity / fare regulation → LCC consolidation → integration cost
accident → safety inspection → booking cancellation → aircraft utilization → insurance / regulatory penalty

해운:
Red Sea disruption → freight rates → capacity tied-up → HMM revenue → route normalization → freight-rate collapse

레저 / 관광:
visa-free policy → arrivals → per-capita spend → hotel/casino/duty-free revenue → margin
```

---

# 2. 대상 canonical archetype

```text
AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE
AUTO_TARIFF_4C_AND_LOCALIZATION_HEDGE
AUTO_ROBOTICS_OPTIONALITY_STAGE2_WITH_LABOR_4B
AUTO_EXPORT_LOGISTICS_DISRUPTION_4C_WATCH
AIRLINE_CONSOLIDATION_STAGE2_WITH_INTEGRATION_4B
AVIATION_SAFETY_HARD_4C
CHINA_TOURISM_LEISURE_STAGE2_EVENT
CONTAINER_SHIPPING_FREIGHT_BETA_STAGE2_WITH_NORMALIZATION_4B
```

---

# 3. deep sub-archetype

```text
Hyundai Motor / Kia:
- Hyundai investor day: 2030 global sales target 5.55M vehicles, +30% vs 2023.
- hybrid lineup doubled, hybrid sales target +40% to 1.33M by 2028.
- buyback up to 4T won / $3B between 2025~2027.
- profit return ratio 35%, +10pp from prior policy.
- shares +5% intraday, close +4.7%.
- Stage2-Actionable; Yellow requires sales mix and margin conversion.

Auto tariffs:
- U.S. auto tariff shock: 25% imported-car tariff; Hyundai fell >4%, Kia >3% after announcement.
- Later U.S.-Korea trade deal: 15% tariff; Hyundai -4.5%, Kia -6.6%.
- Hyundai says 2025 tariffs cost 4.1T won / $2.87B.
- 4C-watch unless U.S. localization offsets margin.

U.S. localization / Hyundai Steel:
- Hyundai Motor Group $21B U.S. investment.
- Hyundai Steel Louisiana $5.8B plant, 2.7M tonnes annual capacity.
- Hyundai Motor +7.5%, Kia +4.3%; Hyundai Steel reversed to -4.4%.
- For Hyundai/Kia, sourcing hedge is Stage2; for Hyundai Steel, capex 4B.

Robotics / Boston Dynamics:
- Hyundai +5.9%, Kia +4.6% after Boston Dynamics CEO step-down news and commercialization expectation.
- Hyundai plans Atlas humanoid deployment at Georgia plant from 2028 and 30,000 annual units.
- union warns robots could create employment shock.
- Stage2 optionality + labor/capex 4B.

Export logistics:
- Hyundai warned exports to Europe/North Africa disrupted by Middle East conflict.
- Hyundai Glovis unable to access some Middle East routes, storing cargo elsewhere.
- Hyundai -1.2%, Glovis -0.7% vs KOSPI +2.7%.
- 4C logistics watch.

Korean Air / Asiana:
- Korean Air completed $1.3B Asiana takeover, 63.88% stake.
- creates one of Asia’s largest airlines; world’s 12th-largest by international capacity.
- Asiana to operate as subsidiary until full integration by 2027.
- Jin Air to absorb Air Busan and Air Seoul.
- Stage2 consolidation; price anchor unavailable, integration/regulatory 4B.

Jeju Air:
- fatal crash killed 179 people.
- Jeju Air shares plunged as much as 15.7%, record low, market cap -95.7B won.
- South Korea ordered B737-800 inspections and safety review.
- booking cancellations rose.
- hard aviation-safety 4C.

Tourism / leisure:
- Chinese tourist group visa-free entry Sep 29, 2025 to Jun 2026.
- Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%.
- China-Korea route capacity 105% of pre-pandemic, but airline profitability pressured by low fares/oversupply.
- Stage2 event, not Green until spending/margin.

HMM / container shipping:
- Red Sea rerouting tied up 5~9% of global vessel capacity; Freightos index +40% in six weeks.
- Maersk later warned Red Sea/Suez return and overcapacity could halve 2026 earnings; shares -5.5%.
- HMM direct price anchor unavailable.
- cyclical freight-rate Stage2 with normalization 4B.
```

---

# 4. 선정 case 요약

| bucket               | case                                     | 핵심 판정                                                                             |
| -------------------- | ---------------------------------------- | --------------------------------------------------------------------------------- |
| Stage2-Actionable    | Hyundai Motor hybrid/value-up            | 하이브리드·EREV 전략 + 4T won buyback + +4.7% close. Yellow 후보                           |
| 4C + hedge           | Hyundai/Kia tariff and U.S. localization | 25%/15% tariff shock는 4C, U.S. 생산·steel sourcing은 Stage2 hedge                    |
| Stage2 + 4B          | Hyundai/Boston Dynamics robotics         | Hyundai +5.9%, Kia +4.6%. Atlas/robotics optionality지만 labor/capex 4B             |
| 4C-watch             | Hyundai/Glovis export disruption         | Middle East route disruption, Hyundai -1.2%, Glovis -0.7% vs KOSPI +2.7%          |
| Stage2 consolidation | Korean Air / Asiana                      | $1.3B takeover, 63.88%, global approval; integration/LCC/fare regulation 4B       |
| hard 4C              | Jeju Air crash                           | 179 deaths, Jeju Air -15.7%, record low, safety inspection                        |
| Stage2 leisure event | China visa-free / Paradise-Hotel Shilla  | Paradise +2.9%, Hotel Shilla +4.8%, but airline route profitability weak          |
| cyclical Stage2      | HMM / Red Sea freight beta               | Red Sea disruption boosts freight, but Suez normalization and overcapacity are 4B |

---

# 5. Case별 trigger grid

## Case A — Hyundai Motor hybrid / EREV / value-up investor day

```text
symbols = 005380 / 000270
case_type = Stage2-Actionable
archetype = AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE
```

| trigger |                    type | date       | 당시 공개 evidence                                                                                              | 가격 anchor                 | outcome             |
| ------- | ----------------------: | ---------- | ----------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------- |
| T0      |               awareness | 2024H1     | EV demand slowdown, hybrid mix importance rises                                                             | no price                  | Stage1              |
| T1      |       Stage2-Actionable | 2024-08-28 | Hyundai targets 5.55M annual global sales by 2030, +30% vs 2023; doubles hybrid lineup                      | intraday +5%, close +4.7% | excellent entry     |
| T2      |              validation | 2024-08-28 | buyback up to 4T won / $3B from 2025~2027; profit return ratio 35%; quarterly dividend minimum 2,500 won    | same                      | value-up validation |
| T3      | Stage3-Yellow candidate | 2024-08-28 | hybrid sales target 1.33M by 2028, EREV launch by end-2026, target OP margin 9~10% by 2027 and >10% by 2030 | same                      | Yellow candidate    |
| T4      |                4B-watch | 2025~2026  | U.S. tariff, China competition, EV slowdown, capex/robotics distraction                                     | no full OHLC              | 4B                  |
| T5      |            Stage3-Green | N/A        | sales mix, OP margin, tariff absorption, full OHLC unavailable                                              | no Green                  | 보류                  |

Hyundai investor day는 R9에서 가장 깨끗한 Stage2-Actionable이다. Hyundai는 2030년 글로벌 판매 목표를 2023년 대비 30% 증가한 5.55M vehicles로 제시했고, EV 둔화 대응으로 hybrid lineup을 두 배로 확대하며 2028년 hybrid sales target을 1.33M units로 높였다. 동시에 2025~2027년 최대 4T won, 약 $3B buyback과 quarterly dividend minimum 2,500 won, profit return ratio 35%를 발표했다. 주가는 발표 후 장중 +5%, 종가 +4.7%였다. 이건 **powertrain mix + shareholder return + margin target**이 같이 닫힌 Stage2-Actionable이다. 다만 Green은 hybrid mix가 실제 OP margin으로 닫혀야 한다. ([Reuters][1])

```json
{
  "case_id": "r9_loop16_hyundai_hybrid_valueup",
  "symbols": "005380/000270",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_to_Stage3-Yellow_candidate",
  "trigger_date": "2024-08-28",
  "hyundai_global_sales_target_2030_mn_units": 5.55,
  "sales_target_increase_vs_2023_pct": 30,
  "hybrid_sales_target_2028_mn_units": 1.33,
  "hybrid_sales_target_raise_pct": 40,
  "buyback_2025_2027_krw_trn": 4,
  "buyback_2025_2027_usd_bn": 3,
  "profit_return_ratio_pct": 35,
  "profit_return_ratio_increase_pp": 10,
  "quarterly_dividend_minimum_krw": 2500,
  "event_intraday_return_pct": 5,
  "event_close_return_pct": 4.7,
  "op_margin_target_2027_pct": "9-10",
  "op_margin_target_2030_pct": ">10",
  "stage3_gate_missing": [
    "hybrid_mix_margin",
    "EREV_launch_sales",
    "US_tariff_absorption",
    "China_competition_response",
    "full_OHLC_MFE_MAE"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_hybrid_valueup"
}
```

---

## Case B — Hyundai / Kia auto tariff shock and U.S. localization hedge

```text
symbols = 005380 / 000270 / 004020
case_type = 4C tariff shock + Stage2 localization hedge
archetype = AUTO_TARIFF_4C_AND_LOCALIZATION_HEDGE
```

| trigger |                type | date       | 당시 공개 evidence                                                                                                             | 가격 anchor                                               | outcome   |
| ------- | ------------------: | ---------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | --------- |
| T0      |            4C-watch | 2025-03-26 | U.S. announces 25% tariffs on imported cars                                                                                | Hyundai >-4%, Kia >-3% / Hyundai -3.4% in cited context | tariff 4C |
| T1      |        Stage2 hedge | 2025-03-25 | Hyundai Motor Group $21B U.S. investment; Hyundai Steel Louisiana $5.8B plant; Hyundai/Kia expected steel sourcing benefit | Hyundai +7.5%, Kia +4.3%                                | hedge     |
| T2      |       4C validation | 2025-07-31 | U.S.-Korea trade deal sets 15% auto tariff; Hyundai -4.5%, Kia -6.6%                                                       | -4.5 / -6.6                                             | 4C        |
| T3      | earnings validation | 2026-01-29 | Hyundai says 2025 tariffs cost 4.1T won / $2.87B; Q4 OP -40%, net profit -52%                                              | Hyundai +7.2% on robotics/long-term optimism            | mixed     |
| T4      |       Stage3-Yellow | N/A        | U.S. plant utilization/tariff savings and margin not confirmed                                                             | no Yellow                                               | 보류        |

Auto tariff는 R9의 textbook 4C-watch다. 2025년 3월 imported-car 25% tariff announcement 이후 Hyundai와 Kia shares는 각각 4%대·3%대 하락했고, 이후 15% tariff로 낮아진 U.S.-Korea trade deal에도 Hyundai -4.5%, Kia -6.6%가 나왔다. 15%는 25%보다 낮지만, KORUS FTA의 기존 zero tariff advantage가 사라지기 때문에 equity는 relief보다 margin damage를 봤다. 반대로 Hyundai Motor Group의 $21B U.S. investment와 Hyundai Steel $5.8B Louisiana plant는 Hyundai +7.5%, Kia +4.3%로 tariff hedge로 반응했다. ([Guardian][2])

```json
{
  "case_id": "r9_loop16_hyundai_kia_tariff_localization",
  "symbols": "005380/000270/004020",
  "best_trigger": "T0/T2",
  "best_trigger_type": "4C_tariff_shock_with_Stage2_localization_hedge",
  "tariff_25pct_announcement_date": "2025-03-26",
  "tariff_25pct_rate": 25,
  "hyundai_tariff_25pct_event_return_context": ">-4",
  "kia_tariff_25pct_event_return_context": ">-3",
  "localization_trigger_date": "2025-03-25",
  "hyundai_group_us_investment_usd_bn": 21,
  "hyundai_steel_louisiana_investment_usd_bn": 5.8,
  "hyundai_steel_capacity_mn_tons": 2.7,
  "hyundai_localization_event_return_pct": 7.5,
  "kia_localization_event_return_pct": 4.3,
  "trade_deal_date": "2025-07-31",
  "trade_deal_auto_tariff_pct": 15,
  "hyundai_trade_deal_event_return_pct": -4.5,
  "kia_trade_deal_event_return_pct": -6.6,
  "hyundai_2025_tariff_cost_krw_trn": 4.1,
  "hyundai_2025_tariff_cost_usd_bn": 2.87,
  "stage3_gate_missing": [
    "US_plant_utilization",
    "actual_tariff_savings",
    "Georgia_factory_margin",
    "steel_localization_ROI",
    "US_sales_mix",
    "full_OHLC_MFE_MAE"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "tariff_4C_with_localization_hedge"
}
```

---

## Case C — Hyundai / Boston Dynamics robotics optionality

```text
symbols = 005380 / 000270
case_type = Stage2 robotics optionality + labor 4B
archetype = AUTO_ROBOTICS_OPTIONALITY_STAGE2_WITH_LABOR_4B
```

| trigger |              type | date       | 당시 공개 evidence                                                                                         | 가격 anchor                | outcome  |
| ------- | ----------------: | ---------- | ------------------------------------------------------------------------------------------------------ | ------------------------ | -------- |
| T0      |         awareness | 2026-01    | Atlas humanoid showcased, Hyundai plans deployment at Georgia plant in 2028                            | no price in AP source    | Stage1   |
| T1      |  4B labor warning | 2026-01-22 | Hyundai union warns robots could cause employment shock; 30,000 annual Atlas production target by 2028 | no price                 | labor 4B |
| T2      | Stage2-Actionable | 2026-02-11 | Boston Dynamics CEO step-down spurs expectation of commercialization acceleration                      | Hyundai +5.9%, Kia +4.6% | Stage2   |
| T3      |     Stage3-Yellow | N/A        | robot unit economics, factory deployment productivity, labor agreement not confirmed                   | no Yellow                | 보류       |

Hyundai robotics는 R9에서 long-duration optionality다. Boston Dynamics CEO step-down 뉴스와 commercialization expectation에 Hyundai shares는 +5.9%, Kia는 +4.6% 올랐다. 별도 Reuters 보도에 따르면 Hyundai는 Atlas humanoid robots를 2028년부터 Georgia plant에 배치하고 연 30,000 units 생산을 목표로 한다. 그러나 union은 “노동자와 합의 없이 신기술 robot은 공장에 들어올 수 없다”고 경고했고, robot deployment가 employment shock를 만들 수 있다고 했다. 즉 Stage2 optionality는 맞지만 labor/capex 4B가 반드시 붙는다. ([Reuters][3])

```json
{
  "case_id": "r9_loop16_hyundai_boston_dynamics_robotics",
  "symbols": "005380/000270",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_robotics_optionality_with_labor_4B",
  "atlas_deployment_target_year": 2028,
  "atlas_annual_production_target_units": 30000,
  "robotics_event_date": "2026-02-11",
  "hyundai_event_return_pct": 5.9,
  "kia_event_return_pct": 4.6,
  "labor_warning_date": "2026-01-22",
  "labor_warning": "employment_shock_and_union_approval_required",
  "georgia_robot_deployment_target": true,
  "stage3_gate_missing": [
    "robot_unit_economics",
    "factory_productivity_gain",
    "labor_agreement",
    "capex_ROI",
    "commercial_customer_sales",
    "full_OHLC_MFE_MAE"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_robotics_optionality_with_4B_labor_overlay"
}
```

---

## Case D — Hyundai / Hyundai Glovis export logistics disruption

```text
symbols = 005380 / 086280
case_type = 4C-watch logistics disruption
archetype = AUTO_EXPORT_LOGISTICS_DISRUPTION_4C_WATCH
```

| trigger |       type | date       | 당시 공개 evidence                                                                                                        | 가격 anchor                                | outcome          |
| ------- | ---------: | ---------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ---------------- |
| T0      |   4C-watch | 2026-04-03 | Hyundai warns Europe/North Africa exports disrupted by Middle East conflict; logistics costs and delivery delays rise | Hyundai -1.2%, Glovis -0.7%, KOSPI +2.7% | logistics 4C     |
| T1      | validation | 2026-04-03 | Hyundai Glovis cannot access some Middle East routes, temporarily stores cargo elsewhere                              | same                                     | validation       |
| T2      | validation | 2026-04    | Hyundai March global sales -2.3%, domestic -2.0%, overseas -2.4%; Middle East shipments -49%                          | same                                     | demand/logistics |
| T3      |     relief | N/A        | route normalization and fuel-cost recovery not confirmed                                                              | no relief                                | 보류               |

이 case는 R9에서 완성차와 물류가 연결되는 4C-watch다. Hyundai는 Middle East conflict로 Europe/North Africa exports가 지연되고, logistics cost와 raw-material constraints가 부품사와 생산에 압박을 준다고 밝혔다. Hyundai Glovis는 일부 Middle East route 접근이 불가능해 대체지역에 cargo를 저장하고 있다고 설명했다. 발표일 Hyundai Motor는 -1.2%, Hyundai Glovis는 -0.7%였고 KOSPI는 +2.7%였다. 즉 시장이 오른 날도 supply chain disruption은 alpha를 깎았다. ([Reuters][4])

```json
{
  "case_id": "r9_loop16_hyundai_glovis_export_disruption",
  "symbols": "005380/086280",
  "best_trigger": "T0/T2",
  "best_trigger_type": "4C_watch_export_logistics",
  "trigger_date": "2026-04-03",
  "hyundai_event_return_pct": -1.2,
  "hyundai_glovis_event_return_pct": -0.7,
  "kospi_same_context_pct": 2.7,
  "hyundai_market_relative_pp": -3.9,
  "glovis_market_relative_pp": -3.4,
  "hyundai_march_global_sales_yoy_pct": -2.3,
  "hyundai_march_domestic_sales_yoy_pct": -2.0,
  "hyundai_march_overseas_sales_yoy_pct": -2.4,
  "middle_east_shipments_yoy_pct": -49,
  "disruption_channels": [
    "route_access_restriction",
    "fuel_cost",
    "delivery_delay",
    "temporary_cargo_storage",
    "parts_supplier_pressure"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "auto_export_logistics_4C_watch"
}
```

---

## Case E — Korean Air / Asiana consolidation

```text
symbols = 003490 / 020560 / 180640 / 298690 / Air_Busan_Air_Seoul_readthrough
case_type = Stage2 airline consolidation with integration 4B
archetype = AIRLINE_CONSOLIDATION_STAGE2_WITH_INTEGRATION_4B
```

| trigger |              type | date       | 당시 공개 evidence                                                                                | 가격 anchor         | outcome           |
| ------- | ----------------: | ---------- | --------------------------------------------------------------------------------------------- | ----------------- | ----------------- |
| T0      |   Stage2 evidence | 2024-11-29 | Jin Air to absorb Asiana LCCs Air Busan and Air Seoul after merger                            | no price anchor   | LCC consolidation |
| T1      | Stage2 validation | 2024-12-12 | Korean Air completes $1.3B Asiana takeover, 63.88% stake                                      | price unavailable | consolidation     |
| T2      |        validation | 2025-03-11 | new branding; Asiana to operate as subsidiary until full integration under Korean Air in 2027 | price unavailable | integration       |
| T3      |          4B-watch | 2024~2027  | route/fare regulation, labor, mileage integration, LCC integration, cargo divestiture         | no OHLC           | 4B                |
| T4      |     Stage3-Yellow | N/A        | synergy, cost savings, capacity discipline, fare regulation impact not confirmed              | no Yellow         | 보류                |

Korean Air-Asiana는 R9 항공 consolidation Stage2다. Korean Air는 $1.3B로 Asiana 63.88%를 인수해 Asia 최대급 airline group 중 하나를 만들었고, 세계 international capacity 기준 12위가 됐다. Asiana는 2027년까지 subsidiary로 운영된 뒤 Korean Air brand에 통합될 예정이며, Jin Air는 Air Busan과 Air Seoul을 흡수해 통합 LCC를 만들 계획이다. 하지만 route/fare regulation, mileage integration, labor, LCC consolidation cost가 남아 있어 Green은 아니다. ([Reuters][5])

```json
{
  "case_id": "r9_loop16_korean_air_asiana_consolidation",
  "symbols": "003490/020560/180640/298690",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_airline_consolidation_with_4B_integration",
  "takeover_completion_date": "2024-12-12",
  "deal_value_usd_bn": 1.3,
  "korean_air_asiana_stake_pct": 63.88,
  "international_capacity_rank_context": 12,
  "full_integration_target_year": 2027,
  "lcc_integration": [
    "Jin_Air",
    "Air_Busan",
    "Air_Seoul"
  ],
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "route_rationalization_savings",
    "fare_regulation_impact",
    "mileage_program_integration",
    "labor_integration",
    "cargo_divestiture_completion",
    "LCC_synergy"
  ],
  "trigger_outcome_label": "Stage2_airline_consolidation_not_Green"
}
```

---

## Case F — Jeju Air crash / aviation safety hard 4C

```text
symbol = 089590
case_type = hard aviation safety 4C
archetype = AVIATION_SAFETY_HARD_4C
```

| trigger |          type | date          | 당시 공개 evidence                                                                                     | 가격 anchor                              | outcome       |
| ------- | ------------: | ------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------- | ------------- |
| T0      |       hard 4C | 2024-12-29/30 | Jeju Air Boeing 737-800 crash at Muan, 179 deaths                                                  | Jeju Air as much as -15.7%, record low | hard 4C       |
| T1      |    validation | 2024-12-30    | market cap erased 95.7B won; first fatal Jeju Air crash since 2005 founding                        | same                                   | validation    |
| T2      | 4C validation | 2024-12-30    | South Korea orders inspections of all Boeing 737-800 aircraft; Jeju Air booking cancellations rise | same                                   | safety review |
| T3      |        relief | N/A           | final investigation, compensation, booking recovery, safety remediation not confirmed              | no relief                              | 보류            |

Jeju Air crash는 R9에서 억지로 “일시적 shock”로 보면 안 되는 hard 4C다. 2024년 12월 Muan crash로 181명 중 179명이 사망했고, Jeju Air shares는 장중 최대 -15.7%로 record low를 찍었으며 약 95.7B won market cap이 사라졌다. 정부는 국내 Boeing 737-800 전수 안전점검을 지시했고, Jeju Air booking cancellation도 증가했다. 이는 항공사의 가장 중요한 무형자산인 safety trust가 깨진 case다. ([Reuters][6])

```json
{
  "case_id": "r9_loop16_jeju_air_crash_safety_4c",
  "symbol": "089590",
  "best_trigger": "T0/T2",
  "best_trigger_type": "hard_4C_aviation_safety",
  "incident_date": "2024-12-29",
  "stock_reaction_date": "2024-12-30",
  "fatalities": 179,
  "survivors": 2,
  "aircraft_type": "Boeing_737-800",
  "airport": "Muan_International_Airport",
  "intraday_event_return_pct": -15.7,
  "market_cap_erased_krw_bn": 95.7,
  "record_low": true,
  "safety_inspection_scope": "all_Boeing_737-800_aircraft_in_South_Korea",
  "booking_cancellation_risk": true,
  "stage3_gate_missing": [
    "final_accident_report",
    "compensation_cost",
    "booking_recovery",
    "safety_remediation",
    "regulatory_penalty",
    "aircraft_utilization_recovery"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "hard_4C_success_aviation_safety"
}
```

---

## Case G — China visa-free tourism / leisure and transport demand

```text
symbols = 034230 / 008770 / 069960 / travel_airline_basket
case_type = Stage2 leisure event with airline-margin 4B
archetype = CHINA_TOURISM_LEISURE_STAGE2_EVENT
```

| trigger |          type | date       | 당시 공개 evidence                                                                                             | 가격 anchor                                                                       | outcome           |
| ------- | ------------: | ---------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------------- |
| T0      | Stage2 policy | 2025-03-20 | Korea announces temporary visa waiver for Chinese group tourists in Q3                                     | no stock price in first source                                                  | Stage2            |
| T1      |  Stage2 event | 2025-08-06 | visa-free entry from Sep 29, 2025 through Jun 2026                                                         | Hyundai Dept +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9% | event             |
| T2      |    validation | 2025-09-29 | groups of 3+ can stay 15 days visa-free; Shilla Duty Free organizes Chinese cruise tour                    | no new price                                                                    | validation        |
| T3      |      4B-watch | 2025-08-26 | China-Korea flight capacity 105% pre-pandemic, but low fares and oversupply pressure airline profitability | no KRX price                                                                    | airline-margin 4B |
| T4      | Stage3-Yellow | N/A        | arrivals, casino drop, hotel RevPAR, duty-free margin not confirmed                                        | no Yellow                                                                       | 보류                |

Tourism/leisure는 R9에 들어오지만, R5에서 봤던 consumer-retail과 분리해서 해석해야 한다. 2025년 8월 policy trigger에 Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%가 나왔다. 이후 실제 pilot이 시작되며 3명 이상 중국 단체관광객은 15일 visa-free 체류가 가능해졌고, Shilla Duty Free는 중국 cruise tour를 조직했다. 하지만 항공/운송 측면에서는 China-Korea flight capacity가 105% of pre-pandemic까지 회복돼 route oversupply와 low fares가 airline profitability를 누를 수 있다는 Reuters 분석도 있다. 따라서 leisure demand Stage2지만 airline margin은 4B다. ([Reuters][7])

```json
{
  "case_id": "r9_loop16_china_tourism_leisure_transport",
  "symbols": "034230/008770/069960/travel_airline_basket",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_leisure_event_with_airline_margin_4B",
  "announcement_date": "2025-08-06",
  "pilot_start_date": "2025-09-29",
  "pilot_end_date": "2026-06",
  "visa_free_stay_days": 15,
  "hyundai_department_store_event_return_pct": 7.1,
  "hotel_shilla_event_return_pct": 4.8,
  "paradise_event_return_pct": 2.9,
  "hankook_cosmetics_event_return_pct": 9.9,
  "china_korea_flight_capacity_vs_pre_pandemic_pct": 105,
  "airline_profitability_risks": [
    "route_oversupply",
    "low_ticket_prices",
    "price_sensitive_group_tourists",
    "temporary_policy_bump"
  ],
  "stage3_gate_missing": [
    "actual_arrivals",
    "casino_drop_amount",
    "hotel_RevPAR",
    "duty_free_margin",
    "airline_yield",
    "repeat_visits"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_leisure_event_not_Green"
}
```

---

## Case H — HMM / Red Sea freight beta and route normalization risk

```text
symbol = 011200
case_type = cyclical freight-rate Stage2 with normalization 4B
archetype = CONTAINER_SHIPPING_FREIGHT_BETA_STAGE2_WITH_NORMALIZATION_4B
```

| trigger |             type | date       | 당시 공개 evidence                                                                                              | 가격 anchor                    | outcome           |
| ------- | ---------------: | ---------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------- | ----------------- |
| T0      |  Stage2 cyclical | 2024-07-03 | Red Sea rerouting + demand ties up 5~9% vessel capacity; Freightos index +40% in six weeks                  | HMM direct price unavailable | freight beta      |
| T1      |       validation | 2025       | Red Sea insurance premium doubles after renewed Houthi attacks; up to 1% ship value                         | no HMM price                 | risk validation   |
| T2      | 4B normalization | 2026-02-05 | Maersk warns 2026 earnings could halve due overcapacity and expected Red Sea route resumption; Maersk -5.5% | HMM unavailable              | normalization 4B  |
| T3      |    4B validation | 2025-10-09 | Maersk -2% on Gaza ceasefire / Suez reopening expectations                                                  | no HMM price                 | freight-rate risk |
| T4      |    Stage3-Yellow | N/A        | HMM freight contract rate, capacity mix, direct OHLC unavailable                                            | no Yellow                    | 보류                |

HMM은 R9 해운 freight beta로 두되, 직접 KRX price anchor는 확보하지 못했다. 글로벌 proxy로는 Red Sea rerouting이 5~9% global vessel capacity를 묶고 Freightos spot container index가 6주간 +40% 오른 Stage2 freight event가 있었다. 반대로 2026년에는 Maersk가 Red Sea/Suez route normalization과 vessel overcapacity로 earnings가 크게 줄 수 있다고 경고했고, Maersk shares는 -5.5% 하락했다. 즉 HMM 같은 container shipping name은 “운임 상승”만으로 Green을 주면 안 되고, freight rate duration과 route normalization 4B를 같이 둬야 한다. ([Reuters][8])

```json
{
  "case_id": "r9_loop16_hmm_red_sea_freight_beta",
  "symbol": "011200",
  "best_trigger": "T0/T3",
  "best_trigger_type": "cyclical_Stage2_freight_beta_with_4B_normalization",
  "stage2_reference_date": "2024-07-03",
  "global_vessel_capacity_tied_pct": "5-9",
  "freightos_index_six_week_return_pct": 40,
  "red_sea_insurance_premium_context": "around_0.7pct_to_1pct_of_ship_value",
  "normalization_reference_date": "2026-02-05",
  "maersk_2026_earnings_warning": "earnings_could_fall_sharply_due_overcapacity_and_Red_Sea_return",
  "maersk_event_return_pct": -5.5,
  "direct_hmm_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "HMM_contract_freight_rates",
    "spot_vs_contract_mix",
    "vessel_utilization",
    "fuel_cost",
    "Suez_route_resumption_timing",
    "full_OHLC_MFE_MAE"
  ],
  "trigger_outcome_label": "cyclical_freight_beta_not_Green"
}
```

---

# 6. Trigger별 가격경로 검증 요약

| case                            | best trigger | entry anchor |                                                                event MFE/MAE |               market-relative | full MFE/MAE | outcome                              |
| ------------------------------- | ------------ | -----------: | ---------------------------------------------------------------------------: | ----------------------------: | ------------ | ------------------------------------ |
| Hyundai hybrid/value-up         | T1/T3        |        event |                                                    intraday +5%, close +4.7% |                   unavailable | unavailable  | Stage2-Actionable / Yellow candidate |
| Hyundai/Kia tariff-localization | T0/T2        |        event | tariff shock Hyundai -4.5%, Kia -6.6%; localization Hyundai +7.5%, Kia +4.3% |                         mixed | unavailable  | 4C + hedge                           |
| Hyundai robotics                | T1/T2        |        event |                                                     Hyundai +5.9%, Kia +4.6% |                   unavailable | unavailable  | Stage2 + labor 4B                    |
| Hyundai/Glovis logistics        | T0/T2        |        event |                                     Hyundai -1.2%, Glovis -0.7%, KOSPI +2.7% | Hyundai -3.9pp, Glovis -3.4pp | unavailable  | 4C-watch                             |
| Korean Air/Asiana               | T1/T3        |     no price |                                                              no direct price |                           N/A | unavailable  | Stage2 consolidation                 |
| Jeju Air crash                  | T0/T2        |        event |                                       Jeju Air -15.7%, market cap -95.7B won |                   unavailable | unavailable  | hard 4C                              |
| China tourism/leisure           | T1/T3        |        event |                       Hyundai Dept +7.1%, Hotel Shilla +4.8%, Paradise +2.9% |                   unavailable | unavailable  | Stage2 event + airline 4B            |
| HMM/Red Sea freight             | T0/T3        | global proxy |                                Freightos +40%; Maersk -5.5% on normalization |               HMM unavailable | unavailable  | cyclical Stage2 + 4B                 |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
좋은 Stage2:
- Hyundai hybrid/value-up investor day.
- Hyundai/Kia U.S. localization hedge.
- Hyundai/Boston Dynamics robotics optionality.
- Korean Air/Asiana consolidation.
- China visa-free leisure event.
- HMM/Red Sea freight beta.

약한 Stage2:
- Korean Air/Asiana는 direct price anchor가 없다.
- HMM은 direct KRX price anchor가 없다.
- China tourism은 airline yield가 약할 수 있다.
```

## Stage2-Actionable entry 성과

```text
Actionable:
- Hyundai hybrid/value-up: +4.7% close and concrete buyback/hybrid/margin targets.
- Hyundai/Kia localization: Hyundai +7.5%, Kia +4.3%.
- Hyundai robotics: Hyundai +5.9%, Kia +4.6%, but labor 4B.
- China leisure event: Hotel Shilla/Paradise reaction, but spending/margin gate.

반대 방향 Actionable 4C:
- Jeju Air crash: -15.7% and safety inspection.
- Hyundai/Glovis logistics disruption: market up but both underperformed.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Hyundai hybrid/value-up if hybrid/EREV mix converts into OP margin and buyback execution.
- Hyundai/Kia localization if U.S. production and steel sourcing reduce tariff margin damage.
- Hyundai robotics if Atlas deployment produces measurable productivity or external sales.
- Korean Air/Asiana if integration creates route/fare/cost synergies.
- China leisure if arrivals convert into casino drop/hotel RevPAR/duty-free margin.
```

## Stage3-Green

```text
이번 R9 Loop 16에서 확정 Green 없음.

이유:
- Hyundai는 strong Stage2지만 tariff and execution gates remain.
- Robotics는 optionality가 크지만 labor/capex/ROI gate가 크다.
- Korean Air-Asiana는 consolidation이지만 integration economics가 없다.
- Jeju Air crash는 hard 4C다.
- HMM freight beta는 duration보다 route normalization risk가 크다.
- Tourism/leisure는 policy event이지 spending/margin까지 아직 아니다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Hyundai hybrid/value-up investor day
- Hyundai/Kia tariff shock and localization hedge
- Hyundai robotics optionality
- Hyundai/Glovis logistics disruption
- Jeju Air crash hard 4C
- China leisure policy event

Stage2_promote_candidate:
- Hyundai hybrid/value-up
- Hyundai/Kia U.S. localization hedge
- Hyundai robotics, but with labor 4B
- China tourism/leisure, if spending/margin confirms

Stage3-Yellow candidate:
- Hyundai hybrid/value-up if OP margin and hybrid mix confirm
- Hyundai/Kia localization if tariff savings and U.S. plant utilization confirm
- Korean Air/Asiana if integration synergy confirms
- HMM if contract rates and freight duration confirm

evidence_good_but_price_failed_or_unavailable:
- Korean Air/Asiana merger due no direct price anchor
- HMM freight beta due no direct HMM anchor
- Hyundai Steel localization from automaker perspective positive, but Hyundai Steel itself reversed

cyclical_success:
- HMM/Red Sea freight beta
- China tourism policy event

event_premium:
- Hyundai robotics
- China visa-free leisure
- U.S. localization headline

thesis_break_watch:
- Jeju Air safety
- Hyundai/Glovis logistics disruption
- auto tariff
- Red Sea route normalization

hard_4C_success:
- Jeju Air crash
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
hybrid_mix_margin_conversion,+5,"hybrid/EREV 전략은 실제 OP margin으로 닫혀야 Yellow","Hyundai"
shareholder_return_execution,+4,"buyback/배당이 실제 실행되면 value-up score 상승","Hyundai"
tariff_absorption_localization,+5,"관세 shock에서 U.S. production/local sourcing은 핵심 hedge","Hyundai/Kia"
us_capacity_utilization,+5,"Georgia/U.S. plant utilization이 tariff hedge를 실제화","Hyundai/Kia"
robotics_commercialization,+4,"Boston Dynamics는 unit economics and deployment proof가 필요","Hyundai"
logistics_route_resilience,+5,"route disruption은 export margin과 delivery timing을 직접 훼손","Hyundai/Glovis"
airline_safety_trust,+5,"fatal crash는 항공사 hard 4C","Jeju Air"
airline_integration_synergy,+4,"Korean Air-Asiana는 merger synergy가 Stage3 gate","Korean Air"
tourism_spend_margin,+5,"visa-free policy는 arrivals보다 spending/margin이 핵심","Paradise/Hotel Shilla"
freight_rate_duration,+5,"해운은 spot rate보다 duration and contract mix가 중요","HMM"
```

## 내릴 축

```csv
axis,delta,reason,cases
ev_headline_without_margin,-4,"EV/hybrid headline만으로 Green 금지","Hyundai/Kia"
tariff_relief_without_savings,-5,"tariff rate 인하도 margin saving 전에는 4C","Hyundai/Kia"
robotics_hype_without_unit_economics,-5,"robotics optionality만으로 Green 금지","Hyundai/Boston Dynamics"
localization_capex_without_roi,-4,"U.S. plant capex는 utilization/ROI 전에는 4B","Hyundai/Kia/Hyundai Steel"
airline_merger_without_integration,-5,"항공 merger는 integration synergy 전에는 Stage2","Korean Air"
tourism_policy_without_yield,-5,"비자정책은 객단가/yield 전에는 Stage2","leisure basket"
freight_spike_without_contract_duration,-5,"운임 spike는 route normalization 때 깨질 수 있음","HMM"
safety_incident_treated_as_one_off,-5,"fatal crash를 일회성 비용으로 보면 false positive","Jeju Air"
```

---

# 10. Stage2-Actionable 승격 조건

R9 Loop 16 shadow rule:

```text
R9에서 Stage2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. event return이 +5% 이상이다.
2. market-relative return이 +5pp 이상이다.
3. 판매량/ASP/OP margin 목표가 구체적이다.
4. buyback/dividend/capital return이 실제 수치로 제시된다.
5. U.S./local capacity가 tariff hedge와 직접 연결된다.
6. 관광/레저는 arrivals뿐 아니라 spending/yield/drop/RevPAR가 확인된다.
7. 운송/해운은 freight rate duration 또는 contract mix가 확인된다.
8. safety accident, route disruption, tariff, labor conflict 4B/4C가 없다.
```

적용:

```text
Hyundai hybrid/value-up:
1,3,4 충족 → Stage2-Actionable / Yellow candidate.

Hyundai/Kia localization:
1,5 충족하지만 tariff 4C 병기 → Stage2 hedge.

Hyundai robotics:
1 충족, commercialization story 있음. 하지만 labor/capex 4B → Stage2 + 4B.

China tourism:
1 충족, but spending/yield missing → Stage2 event.

HMM:
freight beta evidence는 있으나 direct HMM price and contract duration missing → cyclical Stage2.

Jeju Air:
negative hard 4C. 승격 대상 아님.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
- Stage2-Actionable 이후 EPS/OP/FCF 경로 변화 가능성이 높아짐.
- 하지만 tariff, utilization, safety, yield, labor, freight duration 중 하나가 남은 상태.
```

Yellow 후보:

```text
Hyundai hybrid/value-up:
hybrid/EREV mix and buyback execution이 OP margin으로 연결되면 Yellow.

Hyundai/Kia localization:
Georgia/U.S. production and steel sourcing이 tariff cost를 줄이면 Yellow.

Hyundai robotics:
Atlas deployment productivity and labor agreement이 확인되면 Yellow.

Korean Air/Asiana:
route optimization, cost synergy, LCC integration, mileage plan이 닫히면 Yellow.

China leisure:
actual Chinese arrivals, casino drop, hotel RevPAR, duty-free margin 확인 시 Yellow.

HMM:
contract rates and freight duration 확인 시 Yellow.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- hybrid/EREV sales mix converts to OP margin.
- tariff exposure is offset by U.S. localization.
- robotics optionality converts to measurable productivity or sales.
- airline consolidation produces cost and route synergy without fare-regulation damage.
- tourism policy converts to spending/margin, not just arrivals.
- freight spike converts into contract-rate earnings across quarters.
- safety/regulatory issues are resolved.
- full-window MFE/MAE is favorable.
```

이번 R9 Loop 16에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + margin/utilization/safety/tariff/yield gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- tariff rate headline looks like relief but stock falls.
- localization capex rallies before ROI is proven.
- robotics optionality rallies before unit economics and labor agreement.
- airline merger completed before integration synergy.
- tourism policy rallies before spending/yield.
- freight rates spike before contract duration.
- fatal safety accident or route disruption hits customer trust.
```

적용:

```text
Hyundai/Kia:
15% tariff deal still caused selloff → tariff 4B/4C remains.

Hyundai robotics:
stock rallied, but labor warned against robots → 4B.

Korean Air/Asiana:
merger done, but integration/fare/mileage/labor gate → 4B.

China tourism:
stock rally, but route oversupply and low fares → 4B.

HMM:
freight-rate spike, but Red Sea normalization and overcapacity → 4B.

Jeju Air:
fatal crash → hard 4C.
```

---

# 14. 4C hard gate 조건

```text
R9 4C:
- fatal aviation accident
- national safety inspection or fleet grounding
- route disruption causing delivery delay and cost spike
- tariff cost directly hitting profit
- logistics route closure / war-risk insurance surge
- merger blocked or fare regulation undermines synergy
- tourism safety/image shock
```

이번 R9 Loop 16 hard 4C:

```text
Jeju Air crash = hard_4C_success
```

Strong 4C-watch:

```text
- Hyundai/Kia U.S. auto tariffs
- Hyundai/Glovis Middle East route disruption
- HMM Red Sea/Suez route normalization
- tourism anti-foreigner safety/image risk
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R9 production 설계 원칙:

```text
1. hybrid/EREV narrative와 OP margin conversion을 분리한다.
2. tariff headline과 actual tariff savings를 분리한다.
3. U.S. localization capex와 utilization/ROI를 분리한다.
4. robotics optionality와 unit economics/labor risk를 분리한다.
5. airline merger와 integration synergy를 분리한다.
6. fatal aviation accident는 hard 4C로 즉시 차감한다.
7. tourism policy와 spending/yield/margin을 분리한다.
8. freight-rate spike와 duration/contract mix를 분리한다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_245.md 요약

```md
# R9 Loop 16. Mobility / Transport / Leisure Trigger-level Price Validation

이번 라운드는 R9 Loop 16 trigger-level validation 라운드다.

핵심 결론:
- Hyundai Motor hybrid/value-up is the cleanest Stage2-Actionable case. Hyundai targeted 5.55M global sales by 2030, doubled hybrid lineup, raised 2028 hybrid target to 1.33M units, announced up to 4T won / $3B buyback from 2025 to 2027 and 35% profit-return ratio. Shares rose as much as 5% and closed +4.7%.
- Hyundai/Kia tariff exposure is 4C-watch, while U.S. localization is Stage2 hedge. The 25% auto tariff shock hit shares, and even a later 15% U.S.-Korea auto tariff deal pushed Hyundai -4.5% and Kia -6.6%. Hyundai Group’s $21B U.S. investment and Hyundai Steel Louisiana plant made Hyundai +7.5% and Kia +4.3%, but margin savings must be proven.
- Hyundai/Boston Dynamics robotics is Stage2 optionality with labor 4B. Hyundai +5.9% and Kia +4.6% on commercialization expectations, but union warned of employment shock and robot deployment requires labor agreement.
- Hyundai/Hyundai Glovis logistics disruption is 4C-watch. Middle East conflict disrupted exports to Europe/North Africa; Hyundai -1.2% and Glovis -0.7% while KOSPI +2.7%.
- Korean Air/Asiana is Stage2 airline consolidation. Korean Air completed $1.3B takeover, 63.88% stake, forming one of Asia’s largest airlines and world’s 12th-largest by international capacity. Integration/fare/labor/mileage gates remain.
- Jeju Air crash is hard 4C. The Muan crash killed 179 people; Jeju Air shares fell as much as 15.7% to a record low, erasing 95.7B won market cap. South Korea ordered B737-800 safety inspections.
- China visa-free tourism is Stage2 leisure event with airline-margin 4B. Hotel Shilla +4.8%, Paradise +2.9%, Hyundai Department Store +7.1%, Hankook Cosmetics +9.9%; however, route capacity is already 105% of pre-pandemic and low fares may limit airline profits.
- HMM/Red Sea is cyclical freight-rate Stage2 with normalization 4B. Red Sea rerouting tied up 5~9% global vessel capacity and Freightos index rose 40% in six weeks, but Maersk later warned of 2026 earnings pressure from overcapacity and Red Sea/Suez route normalization.

Main calibration:
- Raise hybrid_mix_margin_conversion, shareholder_return_execution, tariff_absorption_localization, us_capacity_utilization, robotics_commercialization, logistics_route_resilience, airline_safety_trust, airline_integration_synergy, tourism_spend_margin, freight_rate_duration.
- Lower ev_headline_without_margin, tariff_relief_without_savings, robotics_hype_without_unit_economics, localization_capex_without_roi, airline_merger_without_integration, tourism_policy_without_yield, freight_spike_without_contract_duration, safety_incident_treated_as_one_off.
```

## docs/checkpoints/checkpoint_28a_round245_r9_loop16.md 요약

```md
# Checkpoint 28A Round 245 R9 Loop 16 Trigger-level Calibration

## 반영 내용
- R9 Loop 16 trigger-level validation을 수행했다.
- Hyundai hybrid/value-up, Hyundai/Kia tariff and localization, Hyundai/Boston Dynamics robotics, Hyundai/Glovis logistics disruption, Korean Air/Asiana consolidation, Jeju Air crash, China tourism/leisure, HMM/Red Sea freight beta를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / FT / WSJ / AP / MarketWatch의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- Hybrid/EREV narrative is not Green unless it converts to OP margin.
- U.S. tariff relief headline can still be 4C if margin damage remains.
- U.S. localization is only Stage2 hedge until utilization and tariff savings are shown.
- Robotics optionality requires unit economics and labor agreement.
- Airline consolidation requires integration synergy, mileage/fare/labor clarity.
- Fatal aviation accident is hard 4C.
- Tourism policy rally is Stage2 until arrivals convert into spending/yield/margin.
- Freight-rate spike is cyclical until contract duration and route normalization risk are resolved.
```

## data/e2r_case_library/cases_r9_loop16_round245.jsonl 초안

```jsonl
{"case_id":"r9_loop16_hyundai_hybrid_valueup","symbol":"005380/000270","company_name":"Hyundai Motor / Kia","case_type":"Stage2_Actionable_to_Yellow_candidate","primary_archetype":"AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2024-08-28","hyundai_global_sales_target_2030_mn_units":5.55,"sales_target_increase_vs_2023_pct":30,"hybrid_sales_target_2028_mn_units":1.33,"hybrid_sales_target_raise_pct":40,"buyback_2025_2027_krw_trn":4,"buyback_2025_2027_usd_bn":3,"profit_return_ratio_pct":35,"event_intraday_return_pct":5,"event_close_return_pct":4.7,"op_margin_target_2027_pct":"9-10","op_margin_target_2030_pct":">10","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_hybrid_valueup","notes":"Powertrain strategy, buyback, margin target and price reaction align. Yellow requires hybrid mix margin and tariff absorption."}
{"case_id":"r9_loop16_hyundai_kia_tariff_localization","symbol":"005380/000270/004020","company_name":"Hyundai Motor / Kia / Hyundai Steel","case_type":"4C_tariff_shock_with_Stage2_localization_hedge","primary_archetype":"AUTO_TARIFF_4C_AND_LOCALIZATION_HEDGE","best_trigger":"T0/T2","stage_candidate":"4C-watch + Stage2 hedge","price_validation":{"tariff_25pct_announcement_date":"2025-03-26","tariff_25pct_rate":25,"localization_trigger_date":"2025-03-25","hyundai_group_us_investment_usd_bn":21,"hyundai_steel_louisiana_investment_usd_bn":5.8,"hyundai_steel_capacity_mn_tons":2.7,"hyundai_localization_event_return_pct":7.5,"kia_localization_event_return_pct":4.3,"trade_deal_date":"2025-07-31","trade_deal_auto_tariff_pct":15,"hyundai_trade_deal_event_return_pct":-4.5,"kia_trade_deal_event_return_pct":-6.6,"hyundai_2025_tariff_cost_krw_trn":4.1,"hyundai_2025_tariff_cost_usd_bn":2.87,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"tariff_4C_with_localization_hedge","notes":"Tariff remains 4C even after 15% deal; U.S. localization is hedge only if savings/margin prove out."}
{"case_id":"r9_loop16_hyundai_boston_dynamics_robotics","symbol":"005380/000270","company_name":"Hyundai Motor / Kia / Boston Dynamics","case_type":"Stage2_robotics_optionality_with_labor_4B","primary_archetype":"AUTO_ROBOTICS_OPTIONALITY_STAGE2_WITH_LABOR_4B","best_trigger":"T1/T2","stage_candidate":"Stage2 + 4B-watch","price_validation":{"atlas_deployment_target_year":2028,"atlas_annual_production_target_units":30000,"robotics_event_date":"2026-02-11","hyundai_event_return_pct":5.9,"kia_event_return_pct":4.6,"labor_warning_date":"2026-01-22","labor_warning":"employment_shock_and_union_approval_required","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_robotics_optionality_with_4B_labor_overlay","notes":"Robotics optionality has price reaction, but unit economics, labor agreement and capex ROI are gates."}
{"case_id":"r9_loop16_hyundai_glovis_export_disruption","symbol":"005380/086280","company_name":"Hyundai Motor / Hyundai Glovis","case_type":"4C_watch_export_logistics","primary_archetype":"AUTO_EXPORT_LOGISTICS_DISRUPTION_4C_WATCH","best_trigger":"T0/T2","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2026-04-03","hyundai_event_return_pct":-1.2,"hyundai_glovis_event_return_pct":-0.7,"kospi_same_context_pct":2.7,"hyundai_market_relative_pp":-3.9,"glovis_market_relative_pp":-3.4,"hyundai_march_global_sales_yoy_pct":-2.3,"middle_east_shipments_yoy_pct":-49,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"auto_export_logistics_4C_watch","notes":"Route disruption, fuel cost and cargo storage cut against auto/export margin."}
{"case_id":"r9_loop16_korean_air_asiana_consolidation","symbol":"003490/020560/180640/298690","company_name":"Korean Air / Asiana / Jin Air / Air Busan","case_type":"Stage2_airline_consolidation_with_4B_integration","primary_archetype":"AIRLINE_CONSOLIDATION_STAGE2_WITH_INTEGRATION_4B","best_trigger":"T1/T3","stage_candidate":"Stage2","price_validation":{"takeover_completion_date":"2024-12-12","deal_value_usd_bn":1.3,"korean_air_asiana_stake_pct":63.88,"international_capacity_rank_context":12,"full_integration_target_year":2027,"lcc_integration":["Jin_Air","Air_Busan","Air_Seoul"],"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_airline_consolidation_not_Green","notes":"Consolidation is real but integration, fare regulation, mileage, labor and LCC synergy are gates."}
{"case_id":"r9_loop16_jeju_air_crash_safety_4c","symbol":"089590","company_name":"Jeju Air","case_type":"hard_4C_aviation_safety","primary_archetype":"AVIATION_SAFETY_HARD_4C","best_trigger":"T0/T2","stage_candidate":"4C","price_validation":{"incident_date":"2024-12-29","stock_reaction_date":"2024-12-30","fatalities":179,"survivors":2,"aircraft_type":"Boeing_737-800","airport":"Muan_International_Airport","intraday_event_return_pct":-15.7,"market_cap_erased_krw_bn":95.7,"record_low":true,"safety_inspection_scope":"all_Boeing_737-800_aircraft_in_South_Korea","booking_cancellation_risk":true,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"hard_4C_success","notes":"Fatal crash, safety inspection and booking cancellations are hard aviation-safety 4C."}
{"case_id":"r9_loop16_china_tourism_leisure_transport","symbol":"034230/008770/069960/travel_airline_basket","company_name":"Paradise / Hotel Shilla / Hyundai Department Store / travel-airline basket","case_type":"Stage2_leisure_event_with_airline_margin_4B","primary_archetype":"CHINA_TOURISM_LEISURE_STAGE2_EVENT","best_trigger":"T1/T3","stage_candidate":"Stage2 event","price_validation":{"announcement_date":"2025-08-06","pilot_start_date":"2025-09-29","pilot_end_date":"2026-06","visa_free_stay_days":15,"hyundai_department_store_event_return_pct":7.1,"hotel_shilla_event_return_pct":4.8,"paradise_event_return_pct":2.9,"hankook_cosmetics_event_return_pct":9.9,"china_korea_flight_capacity_vs_pre_pandemic_pct":105,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_leisure_event_not_Green","notes":"Visa-free policy moves leisure names, but spending, hotel/casino/duty-free margin and airline yield are gates."}
{"case_id":"r9_loop16_hmm_red_sea_freight_beta","symbol":"011200","company_name":"HMM / container shipping read-through","case_type":"cyclical_freight_beta_with_4B_normalization","primary_archetype":"CONTAINER_SHIPPING_FREIGHT_BETA_STAGE2_WITH_NORMALIZATION_4B","best_trigger":"T0/T3","stage_candidate":"cyclical Stage2","price_validation":{"stage2_reference_date":"2024-07-03","global_vessel_capacity_tied_pct":"5-9","freightos_index_six_week_return_pct":40,"red_sea_insurance_premium_context":"around_0.7pct_to_1pct_of_ship_value","normalization_reference_date":"2026-02-05","maersk_event_return_pct":-5.5,"direct_hmm_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"cyclical_freight_beta_not_Green","notes":"Freight-rate spike is cyclical unless HMM contract-rate duration and route-normalization risk are resolved."}
```

## data/e2r_trigger_calibration/triggers_r9_loop16_round245.jsonl 초안

```jsonl
{"trigger_id":"r9l16_hyundai_hybrid_valueup_T1","case_id":"r9_loop16_hyundai_hybrid_valueup","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-28","evidence_available":"Hyundai targets 5.55M 2030 global sales, doubles hybrid lineup, raises hybrid target to 1.33M by 2028, announces up to 4T won buyback and 35% profit return; shares close +4.7%","event_return_pct":4.7,"trigger_outcome_label":"excellent_stage2_actionable_hybrid_valueup","promote_to":"Stage2-Actionable"}
{"trigger_id":"r9l16_hyundai_kia_tariff_T0","case_id":"r9_loop16_hyundai_kia_tariff_localization","trigger_type":"4C-watch_auto_tariff","trigger_date":"2025-03-26/2025-07-31","evidence_available":"U.S. auto tariff shock and later 15% tariff deal pressure Hyundai/Kia; Hyundai -4.5%, Kia -6.6% after 15% trade deal; tariff cost 4.1T won in 2025","event_return_pct":"Hyundai -4.5 / Kia -6.6","trigger_outcome_label":"auto_tariff_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r9l16_hyundai_kia_localization_T1","case_id":"r9_loop16_hyundai_kia_tariff_localization","trigger_type":"Stage2_localization_hedge","trigger_date":"2025-03-25","evidence_available":"Hyundai Group $21B U.S. investment and Hyundai Steel $5.8B Louisiana plant; Hyundai +7.5%, Kia +4.3% on expected steel sourcing/localization benefit","event_return_pct":"Hyundai +7.5 / Kia +4.3","trigger_outcome_label":"Stage2_tariff_hedge","promote_to":"Stage2"}
{"trigger_id":"r9l16_hyundai_robotics_T2","case_id":"r9_loop16_hyundai_boston_dynamics_robotics","trigger_type":"Stage2_robotics_optionality","trigger_date":"2026-02-11","evidence_available":"Boston Dynamics CEO step-down fuels commercialization expectations; Hyundai +5.9%, Kia +4.6%; Atlas deployment/30,000 annual units target but labor 4B","event_return_pct":"Hyundai +5.9 / Kia +4.6","trigger_outcome_label":"Stage2_robotics_with_labor_4B","promote_to":"Stage2+4B"}
{"trigger_id":"r9l16_hyundai_glovis_route_T0","case_id":"r9_loop16_hyundai_glovis_export_disruption","trigger_type":"4C-watch_logistics_disruption","trigger_date":"2026-04-03","evidence_available":"Hyundai warns exports to Europe/North Africa disrupted by Middle East conflict; Glovis cannot access some routes; Hyundai -1.2%, Glovis -0.7%, KOSPI +2.7%","event_return_pct":"Hyundai -1.2 / Glovis -0.7","trigger_outcome_label":"auto_export_logistics_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r9l16_korean_air_asiana_T1","case_id":"r9_loop16_korean_air_asiana_consolidation","trigger_type":"Stage2_airline_consolidation","trigger_date":"2024-12-12/2025-03-11","evidence_available":"Korean Air completes $1.3B Asiana takeover for 63.88% stake and launches integration branding; Asiana subsidiary until 2027; Jin Air to absorb Air Busan/Air Seoul","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_airline_consolidation_not_Green","promote_to":"Stage2"}
{"trigger_id":"r9l16_jeju_air_crash_T0","case_id":"r9_loop16_jeju_air_crash_safety_4c","trigger_type":"hard_4C_aviation_safety","trigger_date":"2024-12-29/2024-12-30","evidence_available":"Jeju Air crash at Muan killed 179; shares plunged as much as 15.7% to record low, erasing 95.7B won market cap; B737-800 safety inspections ordered","event_return_pct":-15.7,"trigger_outcome_label":"hard_4C_success_aviation_safety","promote_to":"4C"}
{"trigger_id":"r9l16_china_tourism_leisure_T1","case_id":"r9_loop16_china_tourism_leisure_transport","trigger_type":"Stage2_leisure_event","trigger_date":"2025-08-06/2025-09-29","evidence_available":"South Korea offers visa-free entry for Chinese tourist groups; Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%; airline route capacity already 105% of pre-pandemic","event_return_pct":"Hyundai Dept +7.1 / Hotel Shilla +4.8 / Paradise +2.9","trigger_outcome_label":"Stage2_leisure_event_with_airline_margin_4B","promote_to":"Stage2"}
{"trigger_id":"r9l16_hmm_redsea_T0","case_id":"r9_loop16_hmm_red_sea_freight_beta","trigger_type":"cyclical_Stage2_freight_beta","trigger_date":"2024-07-03/2026-02-05","evidence_available":"Red Sea rerouting ties up 5-9% global vessel capacity and Freightos index rises 40%; later Maersk warns overcapacity and route normalization could pressure 2026 earnings, shares -5.5%","event_return_pct":"HMM unavailable / global proxy Freightos +40 / Maersk -5.5","trigger_outcome_label":"cyclical_freight_beta_with_normalization_4B","promote_to":"Stage2_cyclical+4B"}
```

## data/sector_taxonomy/score_weight_profiles_round245_r9_loop16_v1.csv 초안

```csv
archetype,hybrid_mix_margin_conversion,shareholder_return_execution,tariff_absorption_localization,us_capacity_utilization,robotics_commercialization,logistics_route_resilience,airline_safety_trust,airline_integration_synergy,tourism_spend_margin,freight_rate_duration,ev_headline_without_margin_penalty,tariff_relief_without_savings_penalty,robotics_hype_without_unit_economics_penalty,localization_capex_without_roi_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE,+5,+4,+2,+2,+1,+1,+1,+0,+0,+0,-4,-2,-1,-1,hybrid/value-up event,margin/tariff conversion pending,hybrid mix+OP margin+buyback execution,Hyundai investor day.
AUTO_TARIFF_4C_AND_LOCALIZATION_HEDGE,+2,+1,+5,+5,+0,+3,+1,+0,+0,+0,-2,-5,-1,-4,tariff shock and localization hedge,actual savings missing,U.S. utilization+tariff savings,Hyundai/Kia.
AUTO_ROBOTICS_OPTIONALITY_STAGE2_WITH_LABOR_4B,+1,+0,+1,+2,+5,+1,+1,+0,+0,+0,-1,-1,-5,-3,robotics commercialization optionality,unit economics/labor agreement missing,productivity gain+external sales,Hyundai/Boston Dynamics.
AUTO_EXPORT_LOGISTICS_DISRUPTION_4C_WATCH,+0,+0,+2,+1,+0,+5,+1,+0,+0,+1,-1,-1,-1,-1,route disruption hits export margin,route normalization missing,N/A,Hyundai/Glovis.
AIRLINE_CONSOLIDATION_STAGE2_WITH_INTEGRATION_4B,+0,+0,+0,+0,+0,+1,+3,+5,+2,+0,-1,-1,-1,-1,airline consolidation,synergy/fare/labor gates missing,route and LCC synergy,Korean Air/Asiana.
AVIATION_SAFETY_HARD_4C,+0,+0,+0,+0,+0,+1,+5,+0,+1,+0,-1,-1,-1,-1,fatal crash/safety trust,remediation and booking recovery missing,N/A,Jeju Air.
CHINA_TOURISM_LEISURE_STAGE2_EVENT,+0,+0,+0,+0,+0,+1,+1,+0,+5,+0,-1,-1,-1,-1,visa-free tourism event,spending/yield missing,arrivals+spending+margin,Paradise/Hotel Shilla.
CONTAINER_SHIPPING_FREIGHT_BETA_STAGE2_WITH_NORMALIZATION_4B,+0,+0,+0,+0,+0,+4,+1,+0,+0,+5,-1,-1,-1,-1,freight-rate spike,contract duration/normalization missing,contract rates+duration,HMM/Red Sea.
```

---

# 이번 R9 Loop 16 결론

```text
1. Hyundai hybrid/value-up은 R9의 가장 좋은 Stage2-Actionable이다.
   hybrid lineup, EREV, 4T won buyback, 35% profit-return ratio, +4.7% price reaction이 닫혔다.

2. Hyundai/Kia tariff는 4C이고, U.S. localization은 Stage2 hedge다.
   15% tariff deal에도 Hyundai -4.5%, Kia -6.6%였고, 2025 tariff cost 4.1T won이 확인됐다.

3. Hyundai/Boston Dynamics robotics는 Stage2 + 4B다.
   Hyundai +5.9%, Kia +4.6%는 강하지만 unit economics and labor agreement가 필요하다.

4. Hyundai/Glovis export disruption은 4C-watch다.
   Middle East route disruption으로 market이 오른 날도 Hyundai와 Glovis가 underperform했다.

5. Korean Air/Asiana는 Stage2 consolidation이다.
   merger는 닫혔지만 integration, fare, mileage, labor, LCC synergy가 남아 있다.

6. Jeju Air crash는 hard 4C다.
   fatal accident, -15.7% plunge, national B737-800 inspection은 항공 safety trust를 깨는 hard gate다.

7. China tourism/leisure는 Stage2 event다.
   Paradise/Hotel Shilla 등 가격반응은 있었지만 spending/yield/margin 전에는 Green이 아니다.

8. HMM/Red Sea freight는 cyclical Stage2다.
   운임 상승은 좋지만 route normalization and overcapacity 4B를 반드시 병기해야 한다.
```

한 문장으로 압축하면:

> **R9 Loop 16에서 배운 핵심은 “모빌리티·항공·관광·해운 headline”이 아니라, hybrid mix margin, tariff savings, U.S. capacity utilization, robotics unit economics, airline integration, aviation safety trust, tourism spending/yield, freight-rate duration이 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 EV/hybrid headline, tariff relief headline, robotics hype, airline merger, visa-free tourism, freight spike만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.reuters.com/business/autos-transportation/hyundai-motor-targets-30-rise-sales-by-2030-it-expands-hybrid-lineup-2024-08-28/?utm_source=chatgpt.com "Hyundai targets 30% rise in sales by 2030, as it doubles hybrid lineups"
[2]: https://www.theguardian.com/us-news/2025/mar/26/trump-new-car-tariffs?utm_source=chatgpt.com "Donald Trump announces new 25% tariffs on cars from overseas"
[3]: https://www.reuters.com/business/autos-transportation/ceo-boston-dynamics-step-down-hyundais-robot-strategy-focus-2026-02-11/?utm_source=chatgpt.com "CEO of Boston Dynamics to step down, as Hyundai's robot strategy in focus"
[4]: https://www.reuters.com/business/autos-transportation/hyundai-motor-flags-export-disruptions-middle-east-conflict-hits-shipping-2026-04-03/?utm_source=chatgpt.com "Hyundai Motor flags export disruptions as Middle East conflict hits shipping"
[5]: https://www.reuters.com/markets/deals/korean-air-completes-asiana-takeover-form-one-asias-biggest-airlines-2024-12-12/?utm_source=chatgpt.com "Korean Air completes Asiana takeover to form one of Asia's biggest airlines"
[6]: https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com "Jeju Air shares plummet to record low after deadly plane crash"
[7]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/?utm_source=chatgpt.com "South Korea to offer visa-free entry to Chinese tourists from late September"
[8]: https://www.reuters.com/markets/hapag-lloyd-ceo-sees-solid-shipping-demand-driving-up-freight-rates-2024-07-03/?utm_source=chatgpt.com "Hapag-Lloyd CEO sees solid shipping demand driving up freight rates"
