순서상 이번은 **R9 Loop 15 — 모빌리티·운송·레저 trigger-level price validation 라운드**다.

이번 R9의 핵심은 “자동차 좋다 / 항공 통합 좋다 / 여행 회복 좋다 / 운임 좋다”가 아니라, **하이브리드 mix, 주주환원, 관세, 현지화 capex, 로보틱스 optionality, 항공 M&A, 안전사고, 관광객 실제 유입, 해운 운임 cycle**을 각각 다른 trigger로 분리하는 것이다.

```text
round = R9 Loop 15
round_id = round_232
large_sector = MOBILITY_TRANSPORT_LEISURE
method = trigger_level_backtest_v1
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R10 Loop 15
```

이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 30D/90D/180D/1Y window를 안정적으로 직접 추출하지 못했다. 그래서 full MFE/MAE는 `price_data_unavailable_after_deep_search`로 두고, Reuters/FT/WSJ/AP의 **reported event return, event price, tariff hit, sales target, M&A value, sector-index return, booking cancellation, freight-rate index**를 trigger anchor로 쓴다. OHLC 미확보를 이유로 Stage 후보 자체를 강등하지 않는다.

---

# 1. 이번 라운드 대섹터

```text
R9 = 모빌리티·운송·레저
```

R9의 core gate는 아래다.

```text
자동차:
판매량 → ASP/mix → 하이브리드/EV/EREV mix → 관세/인센티브 → 영업이익 → 주주환원

자동차부품/로보틱스:
OEM capex → 양산 일정 → plant deployment → unit economics → 반복수주 → valuation overlay

항공:
수요 회복 → 탑승률/yield → 연료비/환율 → 통합 시너지 → 안전 신뢰 → 규제/경쟁 조건

여행·레저:
비자정책 → 실제 입국자 → 항공/호텔/면세/카지노 매출 → 객단가 → 정치·외교 리스크

해운:
운임지수 → Red Sea/Suez capacity shock → spot vs contract rate → fuel/canal cost → overcapacity → earnings cycle
```

---

# 2. 대상 canonical archetype

```text
HYBRID_MIX_SHAREHOLDER_RETURN_STAGE2_YELLOW
AUTO_TARIFF_MARGIN_4C_WATCH
ROBOTICS_OPTIONALITY_STAGE2_WITH_4B
AUTO_LOCALIZATION_CAPEX_OPERATIONAL_4C
AIRLINE_CONSOLIDATION_STAGE2
AIRLINE_SAFETY_HARD_4C
TOURISM_VISA_WAIVER_STAGE2_ACTIONABLE
CONTAINER_FREIGHT_CYCLICAL_STAGE2_4B
```

---

# 3. deep sub-archetype

```text
Hyundai Motor:
- hybrid lineup doubling
- 5.55M global sales target by 2030
- 4T won buyback 2025~2027
- 35% shareholder return target
- EREV production in North America/China
- shares +4.7%

Kia:
- 2030 EV target cut from 1.6M to 1.26M
- 993k hybrid target
- Q2 2025 tariff hit 786B won / $570M
- OP -24%
- U.S. sales +5%, Carnival hybrid strength
- shares -1.7%

Hyundai Robotics / Boston Dynamics:
- Atlas / Boston Dynamics commercialization
- CEO change trigger +5.9% Hyundai, +4.6% Kia
- Hyundai shares nearly doubled in 2026 vs KOSPI +40%
- 9T won / $6.3B AI data-center and robot-factory investment
- +11% day move
- robotics optionality vs auto earnings/tariff reality

Hyundai Georgia localization:
- $7.6B EV/battery campus
- ICE raid detained 475 people, mostly Korean nationals
- battery plant delay and safety/labor risk
- localization capex is not Green without workforce/visa/compliance execution

Korean Air / Asiana:
- $1.3B acquisition, 63.88% stake
- Asiana subsidiary, integration by 2027
- LCC consolidation, route/fleet/network optimization
- competition-condition and integration gate

Jeju Air:
- 179 deaths
- Jeju Air -15.7% intraday, -8.5% at Reuters timestamp
- 95.7B won market-cap loss
- AK Holdings -12%
- travel agencies and LCC sentiment hit
- hard aviation safety 4C

Chinese tourist visa-free / leisure:
- China group tourists visa-free Sep 29 2025~Jun 2026
- Hyundai Department +7.1%
- Hotel Shilla +4.8%
- Paradise +2.9%
- Hankook Cosmetics +9.9%
- flight capacity Korea-China 105% of pre-pandemic
- anti-Chinese protest risk

HMM / container freight:
- Red Sea rerouting tied up 5~9% global vessel capacity
- Freightos index +40% in six weeks to $5,068
- freight rate spike from $1,200 pre-crisis to $4,500 in June 2024
- 2026 Suez return / overcapacity may free 6~7% capacity
```

---

# 4. 선정 case 요약

| bucket                                      | case                                      | 핵심 판정                                                                                           |
| ------------------------------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Stage2-Actionable / Stage3-Yellow candidate | Hyundai Motor hybrid + shareholder return | 하이브리드 목표 +40%, 4T won buyback, 35% shareholder return, +4.7%. Mix/OP margin 확인 시 Yellow         |
| 4C-watch / pivot                            | Kia EV target cut + tariff hit            | EV 목표 -20%+, hybrid 993k target. Q2 tariff hit 786B won, OP -24%, 주가 -1.7%                      |
| Stage2 + 4B                                 | Hyundai/Boston Dynamics robotics          | CEO change +5.9%, robot/AI factory +11%, 2026 99% rally. robotics optionality 강하지만 valuation 4B |
| 4C operational watch                        | Hyundai Georgia localization              | ICE raid 475 detained, project delay/safety risk. 현지화 capex는 workforce/visa/compliance gate     |
| Stage2 consolidation                        | Korean Air / Asiana                       | $1.3B, 63.88%, integration by 2027. route/LCC synergy 전에는 Green 아님                              |
| hard 4C                                     | Jeju Air crash                            | -15.7% intraday, 179 deaths, 95.7B won market cap loss. aviation safety hard gate               |
| Stage2-Actionable                           | China tourism / leisure basket            | visa-free policy + travel/leisure stocks rally. 실제 arrivals/spending/yield 전에는 Green 아님         |
| cyclical event premium                      | HMM / Red Sea freight                     | freight-rate spike is Stage2 cyclical, but Suez normalization/overcapacity turns 4B/4C-watch    |

---

# 5. Case별 trigger grid

## Case A — Hyundai Motor / hybrid mix + shareholder return

```text
symbol = 005380
case_type = Stage2-Actionable / Stage3-Yellow candidate
archetype = HYBRID_MIX_SHAREHOLDER_RETURN_STAGE2_YELLOW
```

| trigger | type                    |       date | 당시 공개 evidence                                                                                                        | 가격 anchor                  | outcome           |
| ------- | ----------------------- | ---------: | --------------------------------------------------------------------------------------------------------------------- | -------------------------- | ----------------- |
| T0      | awareness               |    2024-H1 | EV slowdown, hybrid demand resilience                                                                                 | no exact price             | Stage1            |
| T1      | Stage2 evidence         | 2024-08-28 | 2030 global sales target 5.55M, +30% vs 2023; hybrid lineup doubling                                                  | shares +4.7%, intraday +5% | Stage2-Actionable |
| T2      | Stage2-Actionable       | 2024-08-28 | 2028 hybrid target 1.33M, +40%; 14 hybrid models; North America focus                                                 | same                       | Actionable        |
| T3      | Stage3-Yellow candidate | 2024-08-28 | 4T won buyback 2025~2027, quarterly dividend minimum 2,500 won, profit return target 35%, margin target 9~10% by 2027 | same                       | Yellow candidate  |
| T4      | 4B/4C-watch             |  2025~2026 | U.S. tariffs hit Hyundai earnings; tariff uncertainty persists                                                        | Hyundai/Kia downside later | tariff overlay    |
| T5      | Stage3-Green            |        N/A | actual hybrid sales mix / OP margin / buyback execution not fully verified                                            | N/A                        | no Green          |

Hyundai의 2024년 8월 investor day는 R9에서 plain Stage2보다 강하다. 현대차는 2030년 global annual sales 5.55M대를 목표로 제시했고, EV 둔화에 대응해 hybrid lineup을 두 배로 늘리며 2028년 hybrid sales target을 기존보다 40% 올린 1.33M대로 제시했다. 동시에 2025~2027년 최대 4T won buyback, 분기배당 최소 2,500 won, profit return 35% 목표를 제시했고, 주가는 장중 +5%, 종가 +4.7%였다. 이 조합은 `Stage2-Actionable`, margin과 실행이 따라오면 `Stage3-Yellow`다. ([Reuters][1])

```json
{
  "case_id": "r9_loop15_hyundai_hybrid_shareholder_return",
  "symbol": "005380",
  "best_trigger": "T1/T2/T3",
  "best_trigger_type": "Stage2-Actionable_to_Stage3-Yellow_candidate",
  "trigger_date": "2024-08-28",
  "event_mfe_pct_intraday": 5.0,
  "event_close_return_pct": 4.7,
  "global_sales_target_2030_mn_units": 5.55,
  "global_sales_target_growth_vs_2023_pct": 30,
  "hybrid_target_2028_mn_units": 1.33,
  "hybrid_target_raise_pct": 40,
  "hybrid_models_count": 14,
  "buyback_2025_2027_krw_trn": 4,
  "quarterly_dividend_min_krw": 2500,
  "shareholder_return_target_pct": 35,
  "op_margin_target_2027_pct": "9-10",
  "stage3_gate_missing": [
    "actual_hybrid_sales_mix",
    "ASP_margin_by_powertrain",
    "buyback_execution",
    "tariff_absorption",
    "U.S._localization_margin"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_promote_candidate"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
new_rule = hybrid mix + shareholder return + margin target + price reaction은 Stage2-Actionable 이상
but = 실제 hybrid mix/OP margin/buyback execution 전에는 Green 금지
```

---

## Case B — Kia / EV target cut, hybrid pivot, tariff hit

```text
symbol = 000270
case_type = 4C-watch + Stage2 pivot
archetype = AUTO_TARIFF_MARGIN_4C_WATCH
```

| trigger | type              |       date | 당시 공개 evidence                                                | 가격 anchor         | outcome             |
| ------- | ----------------- | ---------: | ------------------------------------------------------------- | ----------------- | ------------------- |
| T0      | awareness         |  2024~2025 | EV demand uncertainty, U.S. policy risk                       | no price          | watch               |
| T1      | 4C/pivot evidence | 2025-04-09 | Kia cuts 2030 EV target from 1.6M to 1.26M, more than 20% cut | price unavailable | EV thesis softening |
| T2      | Stage2 pivot      | 2025-04-09 | 2030 hybrid target 993k units                                 | price unavailable | hybrid pivot        |
| T3      | 4C margin hit     | 2025-07-25 | Q2 tariff hit 786B won / $570M, OP -24% to 2.76T won          | Kia shares -1.7%  | margin 4C-watch     |
| T4      | partial relief    | 2025-07-25 | U.S. sales +5%, Carnival hybrid strong                        | same              | offset evidence     |
| T5      | hard 4C           |        N/A | structural market-share loss not confirmed                    | N/A               | no hard 4C          |

Kia는 “EV growth story → hybrid pivot → tariff margin hit”를 한 case 안에서 분리해야 한다. 2025년 4월 Kia는 2030 EV sales target을 기존 1.6M대에서 1.26M대로 20% 이상 낮추고, 대신 2030 hybrid target 993k대를 제시했다. 이 trigger는 EV thesis softening이지만 동시에 hybrid pivot Stage2다. ([Reuters][2])

2025년 7월에는 tariff가 실제 P&L을 때렸다. Kia는 Q2에 U.S. tariffs로 786B won, 약 $570M의 타격을 받았고, operating profit은 전년 대비 24% 감소한 2.76T won이었다. U.S. sales는 선구매 효과로 +5%였고 Carnival hybrid sales는 좋았지만, 주가는 -1.7%였다. 따라서 이 trigger는 `Stage2 pivot`이 아니라 `margin 4C-watch`도 같이 붙어야 한다. ([Reuters][3])

```json
{
  "case_id": "r9_loop15_kia_ev_cut_hybrid_tariff",
  "symbol": "000270",
  "best_trigger": "T1/T3",
  "best_trigger_type": "EV_thesis_softening_plus_tariff_4C_watch",
  "ev_target_before_2030_mn_units": 1.6,
  "ev_target_after_2030_mn_units": 1.26,
  "ev_target_cut_pct": -21.25,
  "hybrid_target_2030_units": 993000,
  "q2_2025_tariff_hit_krw_bn": 786,
  "q2_2025_tariff_hit_usd_mn": 570,
  "q2_2025_op_krw_trn": 2.76,
  "q2_2025_op_yoy_pct": -24,
  "us_sales_growth_pct": 5,
  "event_return_pct": -1.7,
  "positive_offset": ["Carnival hybrid sales", "U.S. pre-buy demand"],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "4C_margin_watch_with_hybrid_pivot"
}
```

### 판정

```text
score_price_alignment = thesis_break_watch
new_rule = EV target cut은 4C-watch지만 hybrid pivot evidence가 있으면 Stage2 pivot으로도 분리
```

---

## Case C — Hyundai Motor / Boston Dynamics robotics optionality

```text
symbol = 005380
case_type = Stage2 robotics optionality + 4B valuation overlay
archetype = ROBOTICS_OPTIONALITY_STAGE2_WITH_4B
```

| trigger | type                   |                    date | 당시 공개 evidence                                                                   | 가격 anchor                                | outcome    |
| ------- | ---------------------- | ----------------------: | -------------------------------------------------------------------------------- | ---------------------------------------- | ---------- |
| T0      | awareness              |               2021~2025 | Hyundai owns Boston Dynamics majority stake / indirect exposure                  | no trigger                               | Stage1     |
| T1      | Stage2 evidence        |                 2026-01 | Atlas humanoid public demo, product version to deploy at Georgia plant by 2028   | price source from later reports          | Stage2     |
| T2      | Stage2-Actionable      |              2026-02-11 | Boston Dynamics CEO stepping down; commercialization expectation                 | Hyundai +5.9%, Kia +4.6%                 | Actionable |
| T3      | Stage2-Actionable / 4B | 2026-02-27 / 2026-03-04 | Hyundai group to invest about 9T won / $6.3B in AI data center and robot factory | Hyundai +11% day, 2026 YTD +99% by Mar 3 | 4B overlay |
| T4      | Stage3-Yellow          |                     N/A | robot unit economics / customer orders / deployment revenue missing              | N/A                                      | no Yellow  |
| T5      | 4B-watch               |                    2026 | rally driven by robotics optionality despite tariff-hit auto earnings            | valuation watch                          | 4B         |

Hyundai robotics는 R9 mobility 안에서도 “자동차 판매”와 전혀 다른 optionality다. Reuters는 Boston Dynamics CEO 사임 뉴스가 Hyundai의 robot commercialization 기대를 자극해 Hyundai Motor +5.9%, Kia +4.6%를 기록했다고 보도했다. AP는 Atlas가 CES 2026에서 공개됐고, product version이 2028년 Hyundai Georgia EV facility에서 car assembly를 도울 예정이라고 설명했다. ([Reuters][4])

다만 이 trigger는 valuation 4B overlay가 강하다. Reuters Breakingviews는 Hyundai shares가 2026년 초부터 3월 3일까지 99% 올랐고, Seoul government와 Hyundai group이 AI data center와 robot factory 등에 약 9T won, $6.3B를 투자한다는 소식에 하루 +11% 올랐다고 설명했다. 자동차 영업이익이 아니라 robotics optionality가 market cap을 끌어올린 구조라, Stage2-Actionable이지만 Green은 robot orders/unit economics가 필요하다. ([Reuters][5])

```json
{
  "case_id": "r9_loop15_hyundai_boston_dynamics_robotics",
  "symbol": "005380",
  "best_trigger": "T2/T3",
  "best_trigger_type": "Stage2-Actionable_with_4B_overlay",
  "atlas_public_demo_date": "2026-01",
  "planned_factory_deployment_year": 2028,
  "ceo_change_event_return_hyundai_pct": 5.9,
  "ceo_change_event_return_kia_pct": 4.6,
  "ai_robot_factory_investment_krw_trn": 9,
  "ai_robot_factory_investment_usd_bn": 6.3,
  "robotics_event_return_pct": 11,
  "hyundai_2026_ytd_return_to_mar3_pct": 99,
  "hyundai_indirect_boston_dynamics_stake_pct": 27.9,
  "stage3_gate_missing": [
    "robot_unit_economics",
    "factory_deployment_success",
    "external_customer_orders",
    "recurring_robot_revenue",
    "valuation_vs_auto_core"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_robotics_optionality_with_4B_valuation_overlay"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate_with_4B
new_rule = robotics optionality는 자동차 실적과 분리해서 Stage2로 기록하되, parabolic rerating은 4B overlay
```

---

## Case D — Hyundai Georgia localization / workforce and compliance risk

```text
symbols = 005380 / 373220 read-through
case_type = operational 4C-watch
archetype = AUTO_LOCALIZATION_CAPEX_OPERATIONAL_4C
```

| trigger | type                 |       date | 당시 공개 evidence                                                                       | 가격 anchor           | outcome                     |
| ------- | -------------------- | ---------: | ------------------------------------------------------------------------------------ | ------------------- | --------------------------- |
| T0      | Stage2 capex         |  2023~2025 | Hyundai Georgia EV/battery campus, localization/tariff hedge                         | no direct price     | Stage2                      |
| T1      | 4C operational watch | 2025-09-04 | ICE raid detains 475 workers at Hyundai-LG battery construction site                 | no KRX price anchor | operational shock           |
| T2      | 4C validation        |    2025-09 | plant delay / diplomatic tension / visa-system issue                                 | no direct price     | localization execution risk |
| T3      | safety watch         |    2025-10 | WSJ/Reuters report three worker deaths and serious injuries since construction began | no price            | safety/compliance overlay   |
| T4      | relief               |   2025-09~ | Hyundai recommits $2.7B expansion; capacity +200k by 2028                            | no price            | relief but not Green        |

Hyundai Georgia case는 “미국 현지화 capex = Green”이 아님을 보여준다. AP는 Georgia Hyundai-LG battery construction site에서 475명이 detain됐고 대부분이 한국 국적자였으며, 이는 단일 site 최대급 enforcement action이었다고 보도했다. 해당 site는 Hyundai의 $7.6B project와 LG Energy Solution JV가 포함된 핵심 현지화 자산이다. ([AP News][6])

이후 Reuters는 Hyundai Georgia plant에서 2022년 이후 세 명의 worker deaths와 12명 이상의 serious injuries가 있었다는 WSJ 보도를 전했고, Hyundai가 safety protocols를 강화했다고 설명했다. AP는 Hyundai가 raid 이후에도 Georgia plant expansion에 $2.7B를 추가 투자해 2028년까지 연 200k units capacity를 늘릴 계획이라고 보도했다. 이 case는 localization capex 자체보다 **visa/workforce/compliance/safety execution**이 R9 4C overlay라는 뜻이다. ([Reuters][7])

```json
{
  "case_id": "r9_loop15_hyundai_georgia_localization_operational_4c",
  "symbols": "005380/373220_readthrough",
  "best_trigger": "T1/T2",
  "best_trigger_type": "4C_operational_watch",
  "raid_date": "2025-09-04",
  "detained_workers_count": 475,
  "majority_nationality_context": "mostly South Korean nationals",
  "georgia_project_value_usd_bn": 7.6,
  "hyundai_lges_battery_jv_context": true,
  "worker_deaths_since_2022": 3,
  "serious_injuries_context": "more_than_a_dozen",
  "additional_expansion_usd_bn": 2.7,
  "capacity_addition_units_per_year": 200000,
  "target_capacity_by_2028_units": 500000,
  "direct_krx_price_anchor": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "localization_capex_operational_4C_watch"
}
```

### 판정

```text
score_price_alignment = thesis_break_watch
new_rule = localization capex는 tariff hedge지만 workforce/visa/compliance/safety가 닫히지 않으면 4C overlay
```

---

## Case E — Korean Air / Asiana consolidation

```text
symbols = 003490 / 020560
case_type = Stage2 consolidation
archetype = AIRLINE_CONSOLIDATION_STAGE2
```

| trigger | type                        |       date | 당시 공개 evidence                                                                                   | 가격 anchor                | outcome        |
| ------- | --------------------------- | ---------: | ------------------------------------------------------------------------------------------------ | ------------------------ | -------------- |
| T0      | awareness                   |  2020~2024 | Korean Air-Asiana merger process, antitrust reviews                                              | no price                 | Stage1         |
| T1      | Stage2 evidence             | 2024-12-12 | Korean Air completes Asiana takeover, $1.3B acquisition, 63.88% stake                            | direct price unavailable | Stage2         |
| T2      | Stage2-Actionable candidate | 2025-03-11 | new branding; Asiana to remain subsidiary until full integration under Korean Air by 2027        | direct price unavailable | candidate      |
| T3      | 4B/watch                    |  2024~2027 | route remedies, cargo divestiture, LCC integration, loyalty integration, safety/service pressure | no direct price          | execution gate |
| T4      | Stage3-Yellow               |        N/A | cost synergy/yield/load factor/debt reduction not confirmed                                      | N/A                      | no Yellow      |

Korean Air-Asiana는 R9 항공 consolidation Stage2다. Reuters는 Korean Air가 $1.3B 규모 Asiana 인수를 완료해 63.88% stake를 보유하게 됐고, Asiana는 일단 subsidiary로 운영되며 약 2년 안에 integration을 추진한다고 보도했다. 이후 Korean Air는 신규 branding을 공개했고 Asiana는 2027년까지 Korean Air brand 아래로 통합될 예정이다. ([Reuters][8])

다만 Green은 아니다. 통합은 route/fleet scheduling, LCC integration, frequent flyer program, cargo business sale, staff reassignment, competition remedies가 모두 닫혀야 한다. WSJ도 EU approval을 위해 Europe routes를 T’way에 넘기고 Asiana cargo business를 Air Incheon에 470B won에 매각하기로 했다고 보도했다. ([월스트리트저널][9])

```json
{
  "case_id": "r9_loop15_korean_air_asiana_consolidation",
  "symbols": "003490/020560",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_airline_consolidation",
  "completion_date": "2024-12-12",
  "acquisition_value_usd_bn": 1.3,
  "korean_air_asiana_stake_pct": 63.88,
  "full_integration_target_year": 2027,
  "asiana_cargo_sale_value_krw_bn": 470,
  "stage3_gate_missing": [
    "cost_synergy",
    "route_yield_improvement",
    "load_factor",
    "LCC_integration",
    "frequent_flyer_integration",
    "debt_reduction",
    "regulatory_remedy_execution"
  ],
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_consolidation_not_Green"
}
```

### 판정

```text
score_price_alignment = success_candidate_stage2
new_rule = 항공 M&A는 closing이 Stage2, synergy/yield/load-factor 확인 전 Green 금지
```

---

## Case F — Jeju Air crash / aviation safety hard 4C

```text
symbol = 089590
case_type = hard_4C
archetype = AIRLINE_SAFETY_HARD_4C
```

| trigger | type          |          date | 당시 공개 evidence                                                                   | 가격 anchor                                                | outcome             |
| ------- | ------------- | ------------: | -------------------------------------------------------------------------------- | -------------------------------------------------------- | ------------------- |
| T0      | hard 4C       | 2024-12-29/30 | Muan crash, 179 deaths, Jeju Air first fatal accident                            | Jeju Air -15.7% intraday to 6,920 won, -8.5% at 0312 GMT | hard 4C             |
| T1      | 4C validation |    2024-12-30 | 95.7B won market-cap loss; AK Holdings -12%; emergency safety inspection ordered | same                                                     | hard validation     |
| T2      | sector spread |    2024-12-30 | Korean Air -1.3%, Asiana -0.8%, Hanatour -7%, Very Good Tour -11%                | sector hit                                               | safety trust spread |
| T3      | demand impact |    2024-12-30 | tour package cancellations doubled, bookings halved for one operator             | no price                                                 | travel sentiment    |
| T4      | relief        |           N/A | cause and safety remediation not yet fully priced                                | N/A                                                      | no relief           |

Jeju Air는 R9의 hard 4C reference다. Reuters는 Jeju Air shares가 crash 이후 record low를 찍었고, 장중 최대 -15.7%로 6,920 won까지 내려가며 95.7B won market cap이 사라졌다고 보도했다. 사고는 179명이 사망한 한국 최악의 항공 참사였고, AK Holdings도 -12%까지 하락했다. ([Reuters][10])

이 trigger는 개별 Jeju Air만이 아니라 항공/여행 trust shock이다. 같은 Reuters 보도에서 Korean Air -1.3%, Asiana -0.8%, Hanatour -7%, Very Good Tour -11%가 언급됐고, 여행 패키지 취소가 두 배, 예약이 반토막 난 사례도 나왔다. Guardian은 Jeju Air가 crash 이후 국내 33k, 국제 34k 예약 취소를 확인했고, 정부가 모든 항공 운영 안전점검을 지시했다고 보도했다. ([Reuters][10])

```json
{
  "case_id": "r9_loop15_jeju_air_crash_safety_4c",
  "symbol": "089590",
  "best_trigger": "T0/T1",
  "best_trigger_type": "hard_4C",
  "crash_date": "2024-12-29",
  "market_reaction_date": "2024-12-30",
  "fatalities": 179,
  "survivors": 2,
  "intraday_mae_pct": -15.7,
  "intraday_low_krw": 6920,
  "reported_midday_return_pct": -8.5,
  "market_cap_loss_krw_bn": 95.7,
  "ak_holdings_intraday_mae_pct": -12,
  "korean_air_event_return_pct": -1.3,
  "asiana_event_return_pct": -0.8,
  "hanatour_event_return_pct": -7,
  "very_good_tour_event_return_pct": -11,
  "domestic_reservation_cancellations": 33000,
  "international_reservation_cancellations": 34000,
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "hard_4c_success"
}
```

### 판정

```text
score_price_alignment = hard_4c_success
new_rule = aviation safety accident는 R9 hard 4C이며 항공/여행 basket으로 전염된다
```

---

## Case G — Chinese tourist visa-free / travel-leisure basket

```text
symbols = 008770 / 069960 / 034230 / 123690 / travel_airline_basket
company_scope = Hotel Shilla / Hyundai Department Store / Paradise / Hankook Cosmetics / airlines-read-through
case_type = Stage2-Actionable
archetype = TOURISM_VISA_WAIVER_STAGE2_ACTIONABLE
```

| trigger | type              |       date | 당시 공개 evidence                                                                                                             | 가격 anchor                                                             | outcome               |
| ------- | ----------------- | ---------: | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------- |
| T0      | awareness         | 2025-03-20 | South Korea plans visa waiver for Chinese visitors; 2024 visitors 16.4M, Chinese 28% share                                 | no price                                                              | Stage1                |
| T1      | Stage2 evidence   | 2025-08-06 | visa-free Chinese tourist groups Sep 29~Jun 2026 confirmed                                                                 | Hyundai Dept +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook +9.9% | Stage2-Actionable     |
| T2      | Stage2 validation | 2025-09-29 | program starts; groups of 3+ can stay 15 days visa-free                                                                    | no stock price                                                        | validation            |
| T3      | 4B/4C-watch       | 2025-10-02 | anti-Chinese / anti-foreigner rallies risk image and economy; crackdown ordered                                            | no stock price                                                        | social/political risk |
| T4      | 4B-watch          | 2025-08-26 | China-Korea flight capacity 105% of pre-pandemic, but Chinese airline profits unlikely to improve due oversupply/low fares | no KRX price                                                          | yield watch           |
| T5      | Stage3-Yellow     |        N/A | actual arrivals/card spending/hotel ADR/casino drop/yield not confirmed                                                    | N/A                                                                   | no Yellow             |

관광/레저 basket은 R9에서 Stage2-Actionable이다. 2025년 8월 South Korea가 Chinese tourist groups에 Sep 29 2025~Jun 2026 visa-free entry를 제공한다고 발표하자 Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%가 올랐다. 이는 policy headline만이 아니라 department/hotel/casino/beauty basket이 동시에 움직인 consumption trigger다. ([Reuters][11])

하지만 Green은 아니다. 9월 29일 실제 program이 시작됐고 groups of three or more가 15일간 무비자 체류할 수 있게 됐지만, 실제 항공 yield, hotel ADR, duty-free sales, casino drop, card spending이 확인돼야 Stage3다. Reuters는 Korea-China flight capacity가 이미 pre-pandemic의 105%까지 회복됐지만, route oversupply와 낮은 ticket price 때문에 airline profit 개선은 제한적일 수 있다고 분석했다. 반중/반외국인 집회 리스크도 4C-watch다. ([Reuters][12])

```json
{
  "case_id": "r9_loop15_china_tourism_travel_leisure",
  "symbols": "008770/069960/034230/123690/travel_airline_basket",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable",
  "visa_free_period": "2025-09-29_to_2026-06",
  "hyundai_department_store_event_return_pct": 7.1,
  "hotel_shilla_event_return_pct": 4.8,
  "paradise_event_return_pct": 2.9,
  "hankook_cosmetics_event_return_pct": 9.9,
  "group_size_min": 3,
  "visa_free_stay_days": 15,
  "korea_2024_visitors_mn": 16.4,
  "china_share_of_2024_visitors_pct": 28,
  "korea_china_flight_capacity_vs_prepandemic_pct": 105,
  "stage3_gate_missing": [
    "actual_arrivals",
    "airline_yield",
    "hotel_ADR",
    "duty_free_sales",
    "casino_drop",
    "foreign_card_spending"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_tourism_leisure"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
new_rule = tourism policy + multi-stock consumer/travel rally는 Stage2-Actionable
but = arrivals/spending/yield 전에는 Green 금지
```

---

## Case H — HMM / Red Sea container freight cycle

```text
symbol = 011200
case_type = cyclical_success / event premium / 4B-watch
archetype = CONTAINER_FREIGHT_CYCLICAL_STAGE2_4B
```

| trigger | type              |                                              date | 당시 공개 evidence                                                                               | 가격 anchor                    | outcome                  |
| ------- | ----------------- | ------------------------------------------------: | -------------------------------------------------------------------------------------------- | ---------------------------- | ------------------------ |
| T0      | awareness         |                                    late 2023~2024 | Red Sea attacks force rerouting around Cape of Good Hope                                     | global shipping evidence     | Stage1                   |
| T1      | Stage2 evidence   |                                        2024-06~07 | Freightos 40-foot index +40% in six weeks to $5,068; rerouting ties 5~9% global capacity     | HMM direct price unavailable | Stage2 cyclical          |
| T2      | Stage2-Actionable |                                           2024-06 | freight rates over triple pre-crisis level, roughly $1,200 → $4,500                          | HMM price unavailable        | cyclical entry candidate |
| T3      | 4B-watch          |                                   2025-10~2026-02 | Suez/Red Sea return could release capacity and pressure rates; Maersk warns 2026 EBITDA drop | global price evidence        | cycle peak watch         |
| T4      | Stage3-Yellow     |                                               N/A | HMM-specific spot/contract mix, earnings, dividend not confirmed                             | N/A                          | no Yellow                |
| T5      | 4C                | if Red Sea normalizes and overcapacity hits rates | not hard confirmed for HMM                                                                   | watch                        |                          |

HMM shipping cycle은 R9에서 “운임 spike = cyclic Stage2, not structural Green”의 template다. Reuters는 Red Sea rerouting과 port congestion이 global vessel capacity 5~9%를 묶었고, Freightos spot container index가 6주간 40% 올라 $5,068에 도달했다고 전했다. Breakingviews도 freight rates가 pre-crisis 약 $1,200에서 2024년 6월 $4,500까지 올라 3배 이상이 됐다고 설명했다. HMM direct price anchor는 이번 검색에서 확보하지 못했지만, 운임 trigger 자체는 컨테이너 선사에 명확한 Stage2 cyclical evidence다. ([Reuters][13])

문제는 4B timing이다. 2026년에는 Suez/Red Sea route 복귀와 overcapacity가 freight rates를 압박할 수 있고, Maersk는 2026년 EBITDA가 2025년 $9.53B에서 $4.5~7B range로 크게 낮아질 수 있다고 경고했다. Red Sea route 재개는 6~7%의 global container capacity를 풀 수 있다는 점에서 shipping cycle에는 명확한 4B/4C-watch다. ([Reuters][14])

```json
{
  "case_id": "r9_loop15_hmm_red_sea_freight_cycle",
  "symbol": "011200",
  "best_trigger": "T1/T3",
  "best_trigger_type": "cyclical_Stage2_with_4B_watch",
  "freightos_index_usd_40ft": 5068,
  "freightos_six_week_change_pct": 40,
  "global_capacity_tied_by_rerouting_pct": "5-9",
  "freight_rate_pre_crisis_usd": 1200,
  "freight_rate_june_2024_usd": 4500,
  "freight_rate_multiple_vs_precrisis": 3.75,
  "suez_return_capacity_release_pct": "6-7",
  "maersk_2025_ebitda_usd_bn": 9.53,
  "maersk_2026_ebitda_guidance_usd_bn": "4.5-7.0",
  "hmm_direct_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "HMM_spot_contract_mix",
    "quarterly_OP",
    "dividend_or_buyback",
    "capacity_discipline",
    "Red_Sea_duration"
  ],
  "trigger_outcome_label": "cyclical_success_event_premium_with_4B_watch"
}
```

### 판정

```text
score_price_alignment = cyclical_success / event_premium
new_rule = 운임 spike는 Stage2 cyclical trigger지만, Suez normalization/overcapacity가 보이면 4B trigger를 앞당김
```

---

# 6. Trigger별 가격경로 검증 요약

| case                              | best trigger |       entry anchor |                                                         event MFE/MAE |       market-relative | full MFE/MAE | outcome                              |
| --------------------------------- | ------------ | -----------------: | --------------------------------------------------------------------: | --------------------: | ------------ | ------------------------------------ |
| Hyundai hybrid/shareholder return | T1/T2/T3     |              event |                                             +5% intraday, +4.7% close |           unavailable | unavailable  | Stage2-Actionable / Yellow candidate |
| Kia EV cut/tariff                 | T1/T3        |              event |                                                   -1.7% on tariff hit |           unavailable | unavailable  | 4C-watch + hybrid pivot              |
| Hyundai robotics                  | T2/T3        |              event |                             +5.9%, later +11%; 2026 YTD +99% to Mar 3 |      +? vs KOSPI +40% | unavailable  | Stage2 + 4B                          |
| Hyundai Georgia                   | T1/T2        |           no price |                                                   no direct KRX price |                   N/A | unavailable  | operational 4C-watch                 |
| Korean Air/Asiana                 | T1/T2        |           no price |                                                       no direct price |                   N/A | unavailable  | Stage2 consolidation                 |
| Jeju Air crash                    | T0/T1        | 6,920 intraday low |                                       -15.7% intraday, -8.5% reported |       severe negative | unavailable  | hard 4C                              |
| China tourism/leisure             | T1/T2        |              event | Hyundai Dept +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook +9.9% |           unavailable | unavailable  | Stage2-Actionable                    |
| HMM freight cycle                 | T1/T3        |      freight index |                                   Freightos +40%, rates $1,200→$4,500 | HMM price unavailable | unavailable  | cyclical Stage2 + 4B                 |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
Korean Air/Asiana:
M&A closing은 Stage2 consolidation.
synergy/yield/load factor 전에는 Yellow 금지.

Hyundai Georgia:
localization capex는 Stage2지만 raid/safety/workforce risk가 4C overlay.

HMM:
freight-rate spike는 Stage2 cyclical evidence.
HMM-specific earnings 전에는 Yellow 보류.
```

## Stage 2-Actionable entry 성과

```text
Hyundai Motor:
hybrid target + shareholder return + margin target + +4.7% close.
Actionable 이상.

Hyundai robotics:
Boston Dynamics commercialization triggers +5.9% / +11%.
Actionable이지만 valuation 4B.

China tourism/leisure:
visa-free policy + multi-stock rally.
Actionable이지만 spending/yield conversion 필요.
```

## Stage3-Yellow 후보

```text
Hyundai Motor:
actual hybrid mix, ASP, OP margin, buyback execution 확인 시 Yellow.

Hyundai robotics:
robot deployment and external orders 확인 시 Yellow.

Korean Air:
integration synergy, route optimization, LCC consolidation, load factor/yield 확인 시 Yellow.

HMM:
spot/contract mix and quarterly OP 확인 시 Yellow.
```

## Stage3-Green

```text
이번 R9 Loop 15에서 확정 Green 없음.

이유:
- 현대차 hybrid는 실제 mix/OP margin 검증 필요.
- 로보틱스는 valuation optionality가 앞섰고 unit economics가 없음.
- 항공 M&A는 synergy realization 필요.
- 관광은 실제 spending/yield 필요.
- 해운은 운임 cycle이며 Suez normalization risk가 큼.
```

## 기존 점수표가 놓쳤을 가능성

```text
Stage2_promote_candidate:
- Hyundai Motor hybrid/shareholder return
- Hyundai robotics optionality
- China tourism/leisure basket
- HMM freight-rate cyclical trigger

missed_structural 가능성:
- Hyundai hybrid trigger가 이후 실제 margin/volume으로 이어졌다면 old Stage2 gate는 늦음.
- Hyundai robotics가 실제 robot deployment/order로 이어지면 Stage2→Yellow 승격 가능.

false positive risk:
- Hyundai robotics after +99% YTD if unit economics absent.
- Korean Air/Asiana if merger closing is treated as synergy Green.
- Tourism policy if arrivals/spending fail.
- HMM freight spike if Red Sea normalizes.
```

---

# 8. score-price alignment 판정

```text
Stage2_promote_candidate:
- Hyundai Motor hybrid/shareholder return
- Hyundai robotics / Boston Dynamics
- Chinese tourism/leisure basket
- HMM Red Sea freight cycle

Stage3-Yellow candidate:
- Hyundai Motor, if hybrid mix and margin confirm
- Hyundai robotics, if deployment/orders confirm
- Korean Air, if integration synergy confirms
- HMM, if spot/contract mix and earnings confirm

Stage3-Green:
- 없음

cyclical_success:
- HMM / Red Sea freight rate
- Korean Air if passenger/yield and integration improve later

event_premium:
- Hyundai robotics after +99% YTD
- Tourism visa-free first reaction
- Korean Air merger closing if treated as immediate synergy

evidence_good_but_price_failed:
- Kia hybrid pivot overshadowed by tariff OP hit
- Hyundai Georgia expansion overshadowed by workforce/visa risk

thesis_break_watch:
- Kia tariff margin hit
- Hyundai Georgia raid / safety
- shipping Suez normalization
- tourism social/political backlash

hard_4C_success:
- Jeju Air crash
```

---

# 9. 점수비중 교정

## 올릴 축

```text
hybrid_mix_margin_visibility +5
actual_vehicle_sales_mix +5
shareholder_return_execution +4
tariff_absorption_capacity +5
robotics_deployment_order_visibility +5
localization_workforce_compliance +5
airline_integration_synergy +4
aviation_safety_trust +5
tourism_spending_conversion +5
freight_rate_duration_and_contract_mix +5
```

### 근거

Hyundai investor day에서 하이브리드 목표, buyback, margin target이 동시에 나왔을 때 주가가 +4.7% 반응했기 때문에 `hybrid_mix_margin_visibility`와 `shareholder_return_execution`을 올린다. Kia는 tariff가 실제 OP를 -24% 때렸기 때문에 `tariff_absorption_capacity`를 올린다. Jeju Air는 안전 신뢰가 항공 valuation의 hard gate임을 보여줬고, HMM/Red Sea는 운임 지속기간과 spot/contract mix가 shipping scoring의 핵심임을 보여줬다.

## 내릴 축

```text
ev_growth_headline_only -5
localization_capex_headline_only -5
robotics_optional_value_without_orders -5
merger_closing_without_synergy -4
tourism_policy_without_spending -4
freight_rate_spike_without_duration -4
airline_demand_without_safety_trust -5
```

### 근거

Kia의 EV target cut은 EV headline만으로 scoring하면 안 된다는 신호다. Hyundai Georgia는 localization capex가 workforce/visa/compliance 없이 4C가 될 수 있음을 보여줬다. Korean Air-Asiana는 merger closing만으로 Green을 줄 수 없고, tourism visa-free는 실제 지출 전에는 Stage2다. Hyundai robotics는 optionality가 강하지만 order/unit economics 없이 +99% YTD가 나오면 4B다.

---

# 10. Stage 2-Actionable 승격 조건

R9 Loop 15 shadow rule:

```text
R9에서 Stage 2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. 실제 판매 mix 변화가 숫자로 제시된다. 예: hybrid target, EREV target, sales mix.
2. shareholder return / buyback / dividend policy가 구체적이고 실행 가능하다.
3. event 당일 market-relative 가격 반응이 강하다.
4. tariffs, fuel, FX, freight, labor 등 비용 shock을 흡수할 margin evidence가 있다.
5. mobility optionality가 실제 deployment schedule 또는 customer/order로 연결된다.
6. 관광/항공은 policy가 아니라 arrivals/spending/yield/load factor로 연결될 수 있다.
7. 해운은 freight-rate spike가 spot/contract mix와 duration으로 연결된다.
```

적용:

```text
Hyundai Motor:
hybrid target + buyback + margin target + +4.7%.

Hyundai robotics:
deployment plan + commercialization expectation + +5.9%/+11%, 단 4B overlay.

Chinese tourism:
visa-free policy + multi-stock rally.

HMM:
freight-rate spike + capacity tied up, but HMM direct earnings needed.
```

---

# 11. Stage 3-Yellow 조건

```text
Stage3-Yellow:
- mobility/transport trigger가 EPS/OP/FCF 경로를 바꿀 수 있는 숫자로 보임
- 하지만 핵심 gate 하나가 남음
```

후보:

```text
Hyundai Motor:
hybrid mix and shareholder return. 남은 gate: actual OP margin and tariff absorption.

Hyundai robotics:
robot deployment. 남은 gate: unit economics and external orders.

Korean Air:
Asiana integration. 남은 gate: load factor, route yield, cost synergy.

HMM:
Red Sea freight rate. 남은 gate: HMM spot/contract mix and earnings.
```

---

# 12. Stage 3-Green 조건

```text
Stage3-Green:
- vehicle sales mix and ASP/margin are confirmed
- tariff absorption and U.S. localization work
- robotics optionality becomes actual deployment/order revenue
- airline merger produces cost/yield/load-factor improvement
- tourism policy becomes spending/yield/ADR/casino-drop revenue
- freight-rate spike lasts long enough to show in earnings and cash return
- full-window MFE/MAE is favorable
```

이번 R9 Loop 15에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- robotics optionality로 자동차주가 core auto earnings보다 빠르게 재평가됨
- tariff-hit earnings에도 long-term optionality만으로 주가가 급등
- merger closing으로 airline synergy를 선반영하지만 execution data 없음
- tourism policy로 leisure stocks가 급등하지만 actual spending data 없음
- freight rates 급등 뒤 Suez/Red Sea normalization 또는 overcapacity signal이 나옴
```

적용:

```text
Hyundai robotics:
+99% YTD / +11% day move after AI robot factory trigger → 4B overlay.

HMM:
freight-rate spike는 좋지만 2026 Suez return / overcapacity → 4B.

Korean Air:
merger closing은 Stage2, synergy 전에는 4B-watch.

China tourism:
policy reaction은 Stage2, spending 전에는 4B-watch.
```

---

# 14. 4C hard gate 조건

```text
R9 4C:
- aviation fatal accident / fleet safety failure
- airline consumer trust collapse
- auto tariff shock destroying margins
- localization project delay due workforce/visa/compliance failure
- robotics optionality fails deployment
- tourism policy reversal / diplomatic backlash
- freight-rate normalization causing shipping earnings collapse
```

이번 R9 Loop 15 hard 4C:

```text
Jeju Air crash = hard_4C_success
```

Strong 4C-watch:

```text
- Kia tariff margin hit
- Hyundai Georgia raid / safety / visa risk
- HMM Suez normalization / overcapacity
- tourism anti-foreigner backlash
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_232.md 요약

```md
# R9 Loop 15. Mobility / Transport / Leisure Trigger-level Price Validation

이번 라운드는 R9 Loop 15 trigger-level validation 라운드다.

핵심 결론:
- Hyundai Motor hybrid/shareholder-return trigger is Stage2-Actionable / Stage3-Yellow candidate. On 2024-08-28 Hyundai raised its 2028 hybrid target by 40% to 1.33M units, doubled hybrid lineup plans, announced up to 4T won buyback for 2025~2027, and targeted 35% shareholder return. Shares closed +4.7%. Green requires actual mix, margin and buyback execution.
- Kia is EV thesis softening plus hybrid pivot. Kia cut its 2030 EV target from 1.6M to 1.26M units while targeting 993k hybrids. Q2 2025 tariffs cost 786B won / $570M, OP fell 24% to 2.76T won, and shares fell 1.7%.
- Hyundai/Boston Dynamics robotics is Stage2-Actionable with 4B overlay. CEO change triggered Hyundai +5.9% and Kia +4.6%; later AI data-center / robot-factory investment around 9T won drove Hyundai +11%, with shares +99% YTD by Mar 3, 2026.
- Hyundai Georgia localization is operational 4C-watch. ICE raid detained 475 workers at Hyundai-LG battery site; worker-safety issues and visa/compliance risk show localization capex is not Green without workforce execution.
- Korean Air/Asiana is Stage2 consolidation. Korean Air completed the $1.3B acquisition of a 63.88% stake; Asiana integration is planned by 2027. Green requires cost synergy, route yield, LCC integration, debt reduction and loyalty integration.
- Jeju Air crash is hard R9 4C. Jeju Air fell as much as 15.7% intraday to 6,920 won after the Muan crash killed 179 people, wiping out up to 95.7B won market cap. AK Holdings -12%, Korean Air -1.3%, Asiana -0.8%, Hanatour -7%, Very Good Tour -11%.
- Chinese tourist visa-free leisure basket is Stage2-Actionable. Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9% after Chinese group visa-free policy. Green requires arrivals, spending, ADR, duty-free sales and airline yield.
- HMM / Red Sea freight cycle is cyclical Stage2 with 4B-watch. Freightos 40-foot index +40% in six weeks to $5,068; freight rates rose from roughly $1,200 to $4,500, but 2026 Suez normalization and overcapacity may release 6~7% global capacity.

Main calibration:
- Raise hybrid mix margin visibility, actual vehicle sales mix, shareholder-return execution, tariff absorption capacity, robotics deployment/order visibility, localization workforce compliance, airline integration synergy, aviation safety trust, tourism spending conversion, freight-rate duration/contract mix.
- Lower EV growth headline-only, localization capex headline-only, robotics optionality without orders, merger closing without synergy, tourism policy without spending, freight-rate spike without duration, airline demand without safety trust.
```

## docs/checkpoints/checkpoint_28a_round232_r9_loop15.md 요약

```md
# Checkpoint 28A Round 232 R9 Loop 15 Trigger-level Calibration

## 반영 내용
- R9 Loop 15 trigger-level validation을 수행했다.
- Hyundai Motor hybrid/shareholder return, Kia EV target cut/tariff, Hyundai robotics, Hyundai Georgia localization risk, Korean Air/Asiana, Jeju Air crash, China tourism/leisure basket, HMM Red Sea freight cycle을 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / FT / WSJ / AP의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- 자동차 Stage3는 EV headline이 아니라 hybrid mix, ASP, OP margin, tariff absorption, shareholder-return execution으로 올라간다.
- Robotics optionality는 mobility Stage2지만, unit economics/order 없이 parabolic rerating이면 4B overlay다.
- 항공 M&A는 closing이 Stage2이고, integration synergy/yield/load factor 확인 전 Green 금지다.
- 항공 safety accident는 hard 4C다.
- 관광 policy는 실제 arrivals/spending/yield conversion으로 승격한다.
- 해운 운임 spike는 cyclical Stage2이며, Suez normalization/overcapacity가 보이면 4B trigger를 앞당긴다.
```

## data/e2r_case_library/cases_r9_loop15_round232.jsonl 초안

```jsonl
{"case_id":"r9_loop15_hyundai_hybrid_shareholder_return","symbol":"005380","company_name":"Hyundai Motor","case_type":"Stage2_promote_candidate","primary_archetype":"HYBRID_MIX_SHAREHOLDER_RETURN_STAGE2_YELLOW","best_trigger":"T1/T2/T3","stage_candidate":"Stage2-Actionable_to_Stage3-Yellow_candidate","price_validation":{"trigger_date":"2024-08-28","event_mfe_pct_intraday":5.0,"event_close_return_pct":4.7,"global_sales_target_2030_mn_units":5.55,"global_sales_target_growth_vs_2023_pct":30,"hybrid_target_2028_mn_units":1.33,"hybrid_target_raise_pct":40,"hybrid_models_count":14,"buyback_2025_2027_krw_trn":4,"quarterly_dividend_min_krw":2500,"shareholder_return_target_pct":35,"op_margin_target_2027_pct":"9-10","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Hybrid target, buyback, shareholder return and +4.7% close make this Stage2-Actionable; Green requires actual mix/margin/execution."}
{"case_id":"r9_loop15_kia_ev_cut_hybrid_tariff","symbol":"000270","company_name":"Kia","case_type":"4C_watch_with_hybrid_pivot","primary_archetype":"AUTO_TARIFF_MARGIN_4C_WATCH","best_trigger":"T1/T3","stage_candidate":"4C-watch / Stage2 hybrid pivot","price_validation":{"ev_target_before_2030_mn_units":1.6,"ev_target_after_2030_mn_units":1.26,"ev_target_cut_pct":-21.25,"hybrid_target_2030_units":993000,"q2_2025_tariff_hit_krw_bn":786,"q2_2025_tariff_hit_usd_mn":570,"q2_2025_op_krw_trn":2.76,"q2_2025_op_yoy_pct":-24,"us_sales_growth_pct":5,"event_return_pct":-1.7,"positive_offset":["Carnival hybrid sales","U.S. pre-buy demand"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"EV target cut softens EV thesis; tariff hit is margin 4C-watch, while hybrid target gives pivot evidence."}
{"case_id":"r9_loop15_hyundai_boston_dynamics_robotics","symbol":"005380","company_name":"Hyundai Motor / Boston Dynamics","case_type":"Stage2_promote_candidate_with_4B_overlay","primary_archetype":"ROBOTICS_OPTIONALITY_STAGE2_WITH_4B","best_trigger":"T2/T3","stage_candidate":"Stage2-Actionable + 4B-watch","price_validation":{"atlas_public_demo_date":"2026-01","planned_factory_deployment_year":2028,"ceo_change_event_return_hyundai_pct":5.9,"ceo_change_event_return_kia_pct":4.6,"ai_robot_factory_investment_krw_trn":9,"ai_robot_factory_investment_usd_bn":6.3,"robotics_event_return_pct":11,"hyundai_2026_ytd_return_to_mar3_pct":99,"hyundai_indirect_boston_dynamics_stake_pct":27.9,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate_with_4B","notes":"Robotics commercialization is Stage2-Actionable, but parabolic rerating requires valuation overlay."}
{"case_id":"r9_loop15_hyundai_georgia_localization_operational_4c","symbol":"005380/373220_readthrough","company_name":"Hyundai Motor / LG Energy Solution Georgia site","case_type":"4C_operational_watch","primary_archetype":"AUTO_LOCALIZATION_CAPEX_OPERATIONAL_4C","best_trigger":"T1/T2","stage_candidate":"4C-watch","price_validation":{"raid_date":"2025-09-04","detained_workers_count":475,"majority_nationality_context":"mostly South Korean nationals","georgia_project_value_usd_bn":7.6,"hyundai_lges_battery_jv_context":true,"worker_deaths_since_2022":3,"serious_injuries_context":"more_than_a_dozen","additional_expansion_usd_bn":2.7,"capacity_addition_units_per_year":200000,"target_capacity_by_2028_units":500000,"direct_krx_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"Localization capex needs workforce, visa, compliance and safety execution; otherwise 4C overlay."}
{"case_id":"r9_loop15_korean_air_asiana_consolidation","symbol":"003490/020560","company_name":"Korean Air / Asiana Airlines","case_type":"success_candidate_stage2","primary_archetype":"AIRLINE_CONSOLIDATION_STAGE2","best_trigger":"T1/T2","stage_candidate":"Stage2_consolidation","price_validation":{"completion_date":"2024-12-12","acquisition_value_usd_bn":1.3,"korean_air_asiana_stake_pct":63.88,"full_integration_target_year":2027,"asiana_cargo_sale_value_krw_bn":470,"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"Merger closing is Stage2; Green requires cost synergy, route yield, LCC/frequent-flyer integration and debt reduction."}
{"case_id":"r9_loop15_jeju_air_crash_safety_4c","symbol":"089590","company_name":"Jeju Air","case_type":"hard_4c","primary_archetype":"AIRLINE_SAFETY_HARD_4C","best_trigger":"T0/T1","stage_candidate":"4C","price_validation":{"crash_date":"2024-12-29","market_reaction_date":"2024-12-30","fatalities":179,"survivors":2,"intraday_mae_pct":-15.7,"intraday_low_krw":6920,"reported_midday_return_pct":-8.5,"market_cap_loss_krw_bn":95.7,"ak_holdings_intraday_mae_pct":-12,"korean_air_event_return_pct":-1.3,"asiana_event_return_pct":-0.8,"hanatour_event_return_pct":-7,"very_good_tour_event_return_pct":-11,"domestic_reservation_cancellations":33000,"international_reservation_cancellations":34000,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"hard_4c_success","notes":"Fatal aviation accident is R9 hard 4C and contaminates airline/travel sentiment."}
{"case_id":"r9_loop15_china_tourism_travel_leisure","symbol":"008770/069960/034230/123690/travel_airline_basket","company_name":"Hotel Shilla / Hyundai Department Store / Paradise / Hankook Cosmetics / travel-airline basket","case_type":"Stage2_promote_candidate","primary_archetype":"TOURISM_VISA_WAIVER_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"visa_free_period":"2025-09-29_to_2026-06","hyundai_department_store_event_return_pct":7.1,"hotel_shilla_event_return_pct":4.8,"paradise_event_return_pct":2.9,"hankook_cosmetics_event_return_pct":9.9,"group_size_min":3,"visa_free_stay_days":15,"korea_2024_visitors_mn":16.4,"china_share_of_2024_visitors_pct":28,"korea_china_flight_capacity_vs_prepandemic_pct":105,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Visa-free policy plus multi-stock travel/leisure rally is Stage2-Actionable; Green requires arrivals, spending and yield."}
{"case_id":"r9_loop15_hmm_red_sea_freight_cycle","symbol":"011200","company_name":"HMM / container-shipping read-through","case_type":"cyclical_success_event_premium_with_4B_watch","primary_archetype":"CONTAINER_FREIGHT_CYCLICAL_STAGE2_4B","best_trigger":"T1/T3","stage_candidate":"cyclical Stage2 + 4B-watch","price_validation":{"freightos_index_usd_40ft":5068,"freightos_six_week_change_pct":40,"global_capacity_tied_by_rerouting_pct":"5-9","freight_rate_pre_crisis_usd":1200,"freight_rate_june_2024_usd":4500,"freight_rate_multiple_vs_precrisis":3.75,"suez_return_capacity_release_pct":"6-7","maersk_2025_ebitda_usd_bn":9.53,"maersk_2026_ebitda_guidance_usd_bn":"4.5-7.0","hmm_direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"cyclical_success_event_premium","notes":"Freight-rate spike is cyclical Stage2; Suez normalization and overcapacity are 4B/4C-watch."}
```

## data/e2r_trigger_calibration/triggers_r9_loop15_round232.jsonl 초안

```jsonl
{"trigger_id":"r9l15_hyundai_hybrid_T1","case_id":"r9_loop15_hyundai_hybrid_shareholder_return","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-28","evidence_available":"Hyundai raises hybrid target by 40% to 1.33M by 2028, 14 hybrid models, 4T won buyback, 35% shareholder return target","event_return_pct":4.7,"trigger_outcome_label":"Stage2_promote_candidate","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r9l15_kia_tariff_T3","case_id":"r9_loop15_kia_ev_cut_hybrid_tariff","trigger_type":"4C-watch","trigger_date":"2025-07-25","evidence_available":"Kia Q2 tariff hit 786B won / $570M, OP -24% to 2.76T won, shares -1.7%","event_return_pct":-1.7,"trigger_outcome_label":"tariff_margin_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r9l15_hyundai_robotics_T2","case_id":"r9_loop15_hyundai_boston_dynamics_robotics","trigger_type":"Stage2-Actionable+4B-watch","trigger_date":"2026-02-11","evidence_available":"Boston Dynamics CEO change spurs commercialization expectation; Hyundai +5.9%, Kia +4.6%","event_return_pct":5.9,"trigger_outcome_label":"Stage2_robotics_optionality","promote_to":"Stage2-Actionable"}
{"trigger_id":"r9l15_hyundai_georgia_T1","case_id":"r9_loop15_hyundai_georgia_localization_operational_4c","trigger_type":"4C-watch","trigger_date":"2025-09-04","evidence_available":"ICE raid detains 475 people at Hyundai-LG Georgia battery construction site; project and diplomatic risk","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"localization_operational_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r9l15_koreanair_asiana_T1","case_id":"r9_loop15_korean_air_asiana_consolidation","trigger_type":"Stage2_consolidation","trigger_date":"2024-12-12","evidence_available":"Korean Air completes $1.3B Asiana acquisition, 63.88% stake, integration planned by 2027","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"success_candidate_stage2","promote_to":"Stage2"}
{"trigger_id":"r9l15_jejuair_crash_T0","case_id":"r9_loop15_jeju_air_crash_safety_4c","trigger_type":"hard_4C","trigger_date":"2024-12-30","evidence_available":"Jeju Air crash kills 179; shares down as much as 15.7% to 6,920 won, 95.7B won market cap loss","event_return_pct":-15.7,"trigger_outcome_label":"hard_4c_success","promote_to":"4C"}
{"trigger_id":"r9l15_china_tourism_T1","case_id":"r9_loop15_china_tourism_travel_leisure","trigger_type":"Stage2-Actionable","trigger_date":"2025-08-06","evidence_available":"China tourist group visa-free policy; Hyundai Dept +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%","event_return_pct":"7.1/4.8/2.9/9.9","trigger_outcome_label":"Stage2_promote_candidate","promote_to":"Stage2-Actionable"}
{"trigger_id":"r9l15_hmm_redsea_T1","case_id":"r9_loop15_hmm_red_sea_freight_cycle","trigger_type":"cyclical_Stage2","trigger_date":"2024-06/2024-07","evidence_available":"Red Sea rerouting ties 5-9% global capacity; Freightos index +40% to $5,068; rates from $1,200 to $4,500","event_return_pct":"HMM price unavailable","trigger_outcome_label":"cyclical_success_event_premium","promote_to":"Stage2_cyclical"}
{"trigger_id":"r9l15_hmm_suez_T3","case_id":"r9_loop15_hmm_red_sea_freight_cycle","trigger_type":"4B-watch","trigger_date":"2026-02-05","evidence_available":"Suez return and overcapacity may release 6-7% capacity; Maersk 2026 EBITDA guidance far below 2025","event_return_pct":"HMM price unavailable","trigger_outcome_label":"shipping_cycle_4B_watch","promote_to":"4B-watch"}
```

## data/sector_taxonomy/score_weight_profiles_round232_r9_loop15_v1.csv 초안

```csv
archetype,hybrid_mix_margin_visibility,actual_vehicle_sales_mix,shareholder_return_execution,tariff_absorption_capacity,robotics_deployment_order_visibility,localization_workforce_compliance,airline_integration_synergy,aviation_safety_trust,tourism_spending_conversion,freight_rate_duration_contract_mix,ev_growth_headline_only_penalty,localization_capex_headline_only_penalty,robotics_optional_value_without_orders_penalty,merger_closing_without_synergy_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
HYBRID_MIX_SHAREHOLDER_RETURN_STAGE2_YELLOW,+5,+5,+4,+4,+0,+2,+0,+1,+0,+0,-5,-2,-1,-1,hybrid target+buyback+margin target,actual mix/margin pending,hybrid sales+margin+buyback execution,Hyundai hybrid investor-day trigger.
AUTO_TARIFF_MARGIN_4C_WATCH,+4,+4,+2,+5,+0,+3,+0,+1,+0,+0,-5,-2,-1,-1,tariff hit or EV target cut,hybrid offset pending,tariff absorption+hybrid margin,Kia tariff and EV cut case.
ROBOTICS_OPTIONALITY_STAGE2_WITH_4B,+1,+1,+1,+2,+5,+3,+0,+1,+0,+0,-2,-2,-5,-1,robotics deployment/commercialization trigger,orders/unit economics pending,external orders+unit economics,Hyundai/Boston Dynamics.
AUTO_LOCALIZATION_CAPEX_OPERATIONAL_4C,+2,+2,+1,+5,+1,+5,+0,+2,+0,+0,-2,-5,-2,-1,localization capex plus operational risk,visa/workforce/safety pending,stable local production+compliance,Hyundai Georgia localization.
AIRLINE_CONSOLIDATION_STAGE2,+0,+0,+0,+1,+0,+0,+5,+5,+3,+0,-1,-1,-1,-4,airline merger closing,synergy/yield/load factor pending,synergy+yield+load factor,Korean Air-Asiana consolidation.
AIRLINE_SAFETY_HARD_4C,+0,+0,+0,+1,+0,+0,+1,+5,+3,+0,-1,-1,-1,-1,safety accident,investigation/remediation pending,safety trust recovery,Jeju Air hard 4C.
TOURISM_VISA_WAIVER_STAGE2_ACTIONABLE,+0,+0,+0,+0,+0,+0,+1,+2,+5,+0,-1,-1,-1,-1,visa policy+multi-stock rally,arrivals/spending/yield pending,spending/ADR/yield conversion,Chinese tourism leisure basket.
CONTAINER_FREIGHT_CYCLICAL_STAGE2_4B,+0,+0,+2,+0,+0,+0,+0,+1,+0,+5,-1,-1,-1,-1,freight-rate spike/capacity disruption,HMM earnings/contract mix pending,sustained rates+earnings+cash return,HMM Red Sea freight cycle.
```

---

# 이번 R9 Loop 15 결론

```text
1. Hyundai Motor hybrid/shareholder-return trigger는 Stage2-Actionable이다.
   하이브리드 목표, buyback, shareholder return, margin target이 동시에 있었고 주가도 +4.7%였다.

2. Kia는 EV thesis softening + hybrid pivot + tariff 4C-watch다.
   EV target cut은 부정적이지만 hybrid target이 pivot evidence이고, tariff hit는 실제 OP를 때렸다.

3. Hyundai robotics는 Stage2-Actionable + 4B overlay다.
   Boston Dynamics / Atlas / robot factory는 mobility optionality지만, orders와 unit economics 전에는 Green이 아니다.

4. Hyundai Georgia localization은 operational 4C-watch다.
   미국 현지화 capex는 workforce/visa/safety/compliance가 닫혀야 한다.

5. Korean Air/Asiana는 Stage2 consolidation이다.
   closing은 끝났지만 route/yield/LCC/frequent-flyer/debt synergy가 확인되어야 한다.

6. Jeju Air crash는 R9 hard 4C다.
   fatal safety event는 항공/여행 valuation을 바로 깬다.

7. Chinese tourism/leisure basket은 Stage2-Actionable이다.
   비자정책과 다수 소비·레저주 동반 상승은 강하지만 실제 arrivals/spending/yield 전에는 Green이 아니다.

8. HMM/Red Sea freight cycle은 cyclical Stage2 + 4B-watch다.
   운임 spike는 좋지만 Suez normalization과 overcapacity가 보이면 4B를 앞당겨야 한다.
```

한 문장으로 압축하면:

> **R9 Loop 15에서 배운 핵심은 “자동차·항공·여행·해운 headline”이 아니라, hybrid mix와 margin, tariff absorption, robotics order visibility, localization compliance, airline safety, actual tourism spending, freight-rate duration이 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 EV growth headline, merger closing, capex localization, robotics optionality, freight-rate spike만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.reuters.com/business/autos-transportation/hyundai-motor-targets-30-rise-sales-by-2030-it-expands-hybrid-lineup-2024-08-28/?utm_source=chatgpt.com "Hyundai targets 30% rise in sales by 2030, as it doubles hybrid lineups"
[2]: https://www.reuters.com/business/autos-transportation/south-koreas-kia-cuts-ev-sales-target-2025-04-09/?utm_source=chatgpt.com "South Korea's Kia cuts EV sales target by more than 20% for 2030"
[3]: https://www.reuters.com/business/autos-transportation/kia-corp-takes-570-million-hit-us-tariffs-second-quarter-2025-07-25/?utm_source=chatgpt.com "Kia Corp takes $570 million hit from US tariffs in second quarter"
[4]: https://www.reuters.com/business/autos-transportation/ceo-boston-dynamics-step-down-hyundais-robot-strategy-focus-2026-02-11/?utm_source=chatgpt.com "CEO of Boston Dynamics to step down, as Hyundai's robot strategy in focus"
[5]: https://www.reuters.com/commentary/breakingviews/hyundai-motors-robots-herald-hardware-reboot-2026-03-04/?utm_source=chatgpt.com "Hyundai Motor's robots herald hardware reboot"
[6]: https://apnews.com/article/9394482c195664d7cc3db67ae998ac05?utm_source=chatgpt.com "Homeland security official says 475 people were detained during an immigration raid in Georgia"
[7]: https://www.reuters.com/business/autos-transportation/three-workers-died-hyundais-georgia-plant-since-2022-before-us-immigration-raid-2025-10-12/?utm_source=chatgpt.com "Three workers died at Hyundai's Georgia plant since 2022, before US immigration raid, WSJ reports"
[8]: https://www.reuters.com/markets/deals/korean-air-completes-asiana-takeover-form-one-asias-biggest-airlines-2024-12-12/?utm_source=chatgpt.com "Korean Air completes Asiana takeover to form one of Asia's biggest airlines"
[9]: https://www.wsj.com/business/airlines/korean-air-acquires-controlling-stake-in-rival-asiana-concludes-takeover-7a0f4e03?utm_source=chatgpt.com "Korean Air Acquires Controlling Stake in Rival Asiana, Concludes Takeover"
[10]: https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com "Jeju Air shares plummet to record low after deadly plane crash"
[11]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/?utm_source=chatgpt.com "South Korea to offer visa-free entry to Chinese tourists from late September"
[12]: https://www.reuters.com/world/china/south-korea-pilot-visa-free-entry-chinese-tourist-groups-cctv-reports-2025-09-29/?utm_source=chatgpt.com "South Korea begins visa-free entry for Chinese tourist groups"
[13]: https://www.reuters.com/markets/hapag-lloyd-ceo-sees-solid-shipping-demand-driving-up-freight-rates-2024-07-03/?utm_source=chatgpt.com "Hapag-Lloyd CEO sees solid shipping demand driving up freight rates"
[14]: https://www.reuters.com/business/maersk-q4-meets-forecasts-falling-freight-rates-weigh-2026-profits-2026-02-05/?utm_source=chatgpt.com "Maersk flags 2026 earnings hit as Suez return, overcapacity hit freight rates"
