순서상 이번은 **R4 Loop 15 — 소재·스프레드·전략자원 trigger-level price validation 라운드**다.

이번 R4의 핵심은 “소재주가 올랐다”가 아니라, **스프레드·원재료 가격·전략자원 규제·관세·지배권 premium·capex·TC/RC가 어느 trigger에서 실제 entry가 됐고, 어느 trigger는 4B/4C였는지**를 보는 것이다.

```text
round = R4 Loop 15
round_id = round_227
large_sector = MATERIALS_SPREAD_STRATEGIC_RESOURCES
method = trigger_level_backtest_v1
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R5 Loop 15
```

이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 30D/90D/180D/1Y window를 안정적으로 직접 추출하지 못했다. 그래서 full MFE/MAE는 `price_data_unavailable_after_deep_search`로 두고, Reuters/FT/WSJ/MarketWatch의 **reported event return, event price, tender price, tariff rate, lithium/copper price, deal value, capex value, spread/TC·RC data**를 trigger anchor로 쓴다. 단, **OHLC 미확보를 이유로 Stage 후보 자체를 강등하지 않는다.**

---

# 1. 이번 라운드 대섹터

```text
R4 = 소재·스프레드·전략자원
```

R4의 핵심 gate는 아래다.

```text
철강:
수요 물량 → ASP → 원재료/전력비 → 중국 저가 수입 → 관세/덤핑 → spread → utilization

비철금속:
금속 가격 → TC/RC → concentrate supply → smelter margin → 재고/hedging → FCF

리튬:
spot price → spodumene / carbonate → 원가/ASP pass-through → downstream margin → inventory write-down

흑연/전략광물:
중국 의존도 → FEOC/IRA → 관세/수출통제 → non-China capacity → 품질/고객 인증 → 실제 매출

지배권·전략자산:
control premium → tender / buyback / dilution → 전략자원 논리 → operating cashflow 분리

localization capex:
정책/동맹 명분 → funding plan → IRR → 고객 수요 → ROIC
```

---

# 2. 대상 canonical archetype

```text
GRAPHITE_TARIFF_STAGE2_ACTIONABLE
LITHIUM_PRICE_EVENT_PREMIUM
UPSTREAM_LITHIUM_SUPPLY_SECURITY_STAGE2
STEEL_ANTIDUMPING_SPREAD_STAGE2_ACTIONABLE
STEEL_WEAK_DEMAND_FAILED_RERATING
LOCALIZATION_CAPEX_FALSE_POSITIVE
KOREA_ZINC_CONTROL_PREMIUM_4B
CRITICAL_MINERALS_SMELTER_STAGE2_WITH_DILUTION_4B
COPPER_TCRC_SPREAD_4C_WATCH
CHINA_STRATEGIC_MINERAL_EXPORT_CONTROL_4C
```

---

# 3. deep sub-archetype

```text
Graphite / anode:
- POSCO Future M
- U.S. 93.5% anti-dumping tariff on Chinese graphite / anode active materials
- China graphite dominance / FEOC risk
- tariff relief vs actual non-China capacity / quality / customer certification

Lithium:
- POSCO / MinRes
- CATL Yichun / Jianxiawo mine suspension
- lithium price event premium
- spodumene still far below 2022 peak
- upstream supply security vs downstream margin

Steel:
- Hyundai Steel / POSCO Holdings
- weak construction demand / rebar price decline
- Chinese steel plate anti-dumping tariff
- U.S. steel plant capex / localization false positive

Korea Zinc:
- MBK / Young Poong tender battle
- control premium vs operating cashflow
- national core technology ruling
- U.S.-backed $7.4B critical minerals refinery
- new share issuance / injunction / governance 4B

Copper / smelting:
- LS MnM / Korea Zinc / copper smelter read-through
- copper record price
- Korea/Taiwan LME inventory withdrawal
- TC/RC collapsing / negative processing margin risk

China strategic minerals:
- graphite, antimony, gallium, germanium, rare-earth magnet technology
- export controls / bans
- Korea battery/material supply-chain exposure
```

---

# 4. 선정 case 요약

| bucket                 | case                                   | 핵심 판정                                                                        |
| ---------------------- | -------------------------------------- | ---------------------------------------------------------------------------- |
| Stage2-Actionable      | POSCO Future M / graphite tariff       | U.S. 93.5% tariff, POSCO Future M +20%. 단 non-China quality/capacity gate 남음 |
| event_premium          | CATL lithium mine suspension           | POSCO Future M +8.3%, L&F +10%. CATL “no material impact”라 Stage3 금지         |
| Stage2 supply-security | POSCO / MinRes lithium JV              | $765M, Wodgina/Mt Marion indirect 15%. 가격 cycle risk 남음                      |
| Stage2-Actionable      | Hyundai Steel/POSCO anti-dumping       | Hyundai Steel +5.8%, POSCO +3.9%, tariff 27.91~38.02%                        |
| failed_rerating        | Hyundai Steel weak demand              | rebar -10%, NP estimate -73%, 주가 -1.2%                                       |
| false_positive_score   | Hyundai Steel U.S. plant               | 초기 +5% 후 -4.4%, 이후 -21.2%. funding/IRR 미확정                                   |
| 4B-watch               | Korea Zinc tender battle               | tender +24%, 이후 +29.9% upper limit. control premium이지 operating Green 아님     |
| Stage2 + 4B            | Korea Zinc critical minerals smelter   | U.S.-backed $7.4B refinery, +27%, 이후 share-sale injunction에 -13%             |
| 4C-watch               | Copper TC/RC squeeze                   | copper record price는 좋지만 TC/RC 붕괴는 smelter margin 4C                         |
| 4C strategic reference | China critical mineral export controls | graphite/antimony/gallium/germanium/rare earth 등 공급망 hard gate               |

---

# 5. Case별 trigger grid

## Case A — POSCO Future M / U.S. graphite tariff

```text
symbol = 003670
case_type = Stage2-Actionable / 4B-watch
archetype = GRAPHITE_TARIFF_STAGE2_ACTIONABLE
```

### Trigger grid

| trigger | type                    |                                date | 당시 공개 evidence                                                                                                                                     | 가격 anchor                                           | outcome                            |
| ------- | ----------------------- | ----------------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ---------------------------------- |
| T0      | awareness               |                          2024-04-26 | South Korea warns Chinese graphite dominance can collapse IRA subsidy logic; China controls >99% battery-grade graphite and 69% synthetic graphite | no KRX price                                        | strategic watch                    |
| T1      | Stage2 evidence         |                          2025-07-18 | U.S. announces 93.5% anti-dumping tariff on Chinese anode active materials / graphite                                                              | POSCO Future M +20%                                 | Stage2-Actionable                  |
| T2      | Stage3-Yellow candidate |                          2025-07-18 | total tariff on Chinese graphite roughly 160%, non-China producers rally                                                                           | Syrah +22%, Nouveau Monde +26%, POSCO Future M +20% | Yellow candidate, pending capacity |
| T3      | 4B-watch                |                          2025-07-18 | FT notes skepticism over non-China producers’ ability to meet EV makers’ quality/supply needs                                                      | no follow-through OHLC                              | 4B quality gate                    |
| T4      | 4C-watch                | if non-China capacity/quality fails | not confirmed                                                                                                                                      | pending                                             | no hard 4C                         |

POSCO Future M graphite tariff trigger는 R4에서 가장 중요한 `Stage2-Actionable` 후보 중 하나다. U.S.가 중국산 graphite/anode active materials에 93.5% anti-dumping duty를 부과했고, FT는 이로 인해 POSCO Future M이 +20% 올랐다고 보도했다. 하지만 같은 보도는 non-China graphite producers가 EV makers의 quality와 supply needs를 충족할 수 있을지 의문이 남아 있다고도 짚었다. 그래서 이 trigger는 **Stage2-Actionable 또는 Stage3-Yellow 후보**지만, Green은 아니다. ([Financial Times][1])

### Trigger price validation row

```json
{
  "case_id": "r4_loop15_posco_future_m_graphite_tariff",
  "symbol": "003670",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_to_Stage3-Yellow_candidate",
  "trigger_date": "2025-07-18",
  "us_graphite_antidumping_tariff_pct": 93.5,
  "approx_total_us_tariff_on_chinese_graphite_pct": 160,
  "posco_future_m_event_mfe_pct": 20,
  "syrah_resources_event_mfe_pct": 22,
  "nouveau_monde_event_mfe_pct": 26,
  "novonix_event_mfe_pct": 15,
  "china_battery_grade_graphite_control_pct": 99,
  "china_synthetic_graphite_control_pct": 69,
  "stage3_gate_missing": [
    "non_china_capacity",
    "quality_certification",
    "customer_award",
    "anode_margin",
    "IRA_FEOC_compliance_cashflow"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_promote_candidate_with_quality_capacity_4B_watch"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
new_rule = graphite tariff + non-China supply chain premium은 Stage2-Actionable 가능
but = 품질/생산능력/customer award 없으면 Green 금지
```

---

## Case B — CATL Yichun lithium mine suspension / Korean materials rally

```text
symbols = 003670 / 066970 / 006400 / 373220
case_type = event_premium / 4B-watch
archetype = LITHIUM_PRICE_EVENT_PREMIUM
```

### Trigger grid

| trigger | type            |       date | 당시 공개 evidence                                                                                                 | 가격 anchor                                             | outcome              |
| ------- | --------------- | ---------: | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | -------------------- |
| T0      | awareness       |    2025-08 | lithium price down up to 90% from 2022 peak, supply glut easing speculation                                    | no KRX price                                          | cycle watch          |
| T1      | Stage2 evidence | 2025-08-11 | CATL suspends Yichun/Jianxiawo lithium mine after license expiry                                               | Ganfeng +21%, Tianqi +18%                             | lithium supply shock |
| T2      | event premium   | 2025-08-11 | Korean materials/battery rally                                                                                 | POSCO Future M +8.3%, L&F +10%, SDI +3.2%, LGES +2.8% | event premium        |
| T3      | 4B-watch        | 2025-08-18 | CME lithium carbonate +27% since August start, but Reuters says speculative excess and fundamentals still weak | no direct KRX                                         | 4B-watch             |
| T4      | Stage3-Yellow   |        N/A | durable lithium price / margin not confirmed                                                                   | N/A                                                   | no Yellow            |

CATL lithium mine suspension은 R4 소재 스프레드에서 전형적인 event premium이다. 한국에서는 POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%가 나왔지만, CATL은 license renewal 시 생산 재개가 가능하고 material operational impact는 없다고 밝혔다. Reuters도 이후 lithium carbonate rally가 27%까지 확대됐지만, 투기적 과열과 약한 fundamentals가 섞여 있다고 평가했다. ([Reuters][2])

### Trigger price validation row

```json
{
  "case_id": "r4_loop15_catl_yichun_lithium_event",
  "symbols": "003670/066970/006400/373220",
  "best_trigger": "T2",
  "best_trigger_type": "event_premium",
  "trigger_date": "2025-08-11",
  "posco_future_m_event_mfe_pct": 8.3,
  "lnf_event_mfe_pct": 10.0,
  "samsung_sdi_event_mfe_pct": 3.2,
  "lges_event_mfe_pct": 2.8,
  "ganfeng_lithium_event_mfe_pct": 21,
  "tianqi_lithium_event_mfe_pct": 18,
  "cme_lithium_carbonate_august_rally_pct": 27,
  "lithium_price_decline_from_2022_peak_pct": -90,
  "catl_material_impact_claim": "no_material_impact",
  "license_renewal_possible": true,
  "stage3_gate_missing": [
    "durable_lithium_price",
    "inventory_drawdown",
    "ASP_pass_through",
    "material_margin",
    "customer_calloff"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "event_premium_not_stage3"
}
```

### 판정

```text
score_price_alignment = event_premium
new_rule = lithium mine suspension은 가격 event지만 durable spread/margin 전에는 Stage3 금지
```

---

## Case C — POSCO / MinRes lithium JV

```text
symbols = 005490 / 003670
case_type = Stage2 supply-security
archetype = UPSTREAM_LITHIUM_SUPPLY_SECURITY_STAGE2
```

### Trigger grid

| trigger | type                        |       date | 당시 공개 evidence                                                                         | 가격 anchor                      | outcome           |
| ------- | --------------------------- | ---------: | -------------------------------------------------------------------------------------- | ------------------------------ | ----------------- |
| T0      | awareness                   |  2022~2025 | POSCO battery materials / lithium vertical integration narrative                       | no current OHLC                | Stage1            |
| T1      | Stage2 evidence             | 2025-11-11 | POSCO buys 30% stake in MinRes lithium JV for $765M                                    | MinRes +10.8%                  | Stage2            |
| T2      | Stage2-Actionable candidate | 2025-11-11 | Wodgina and Mt Marion indirect 15% exposure, proportional spodumene concentrate rights | POSCO direct price unavailable | candidate         |
| T3      | 4C-watch                    | 2025-11-11 | spodumene $880/t vs 2022 peak >$6,000; lithium market still depressed                  | no direct KRX                  | price-cycle watch |
| T4      | Stage3-Yellow               |        N/A | downstream margin / cost advantage not confirmed                                       | N/A                            | no Yellow         |

POSCO/MinRes trigger는 R4에서 **supply-security Stage2**다. POSCO는 $765M을 들여 MinRes lithium JV 30%를 인수하고, Wodgina와 Mt Marion에 각각 간접 15% exposure를 갖게 된다. 다만 Reuters는 spodumene price가 2022년 $6,000/t 이상에서 2025년 6월 $610까지 내려갔고, 8월 $880으로 반등했지만 peak에는 한참 못 미친다고 설명했다. 따라서 upstream 확보는 좋지만, **cost advantage와 downstream margin 확인 전에는 Green이 아니다.** ([Reuters][3])

### Trigger price validation row

```json
{
  "case_id": "r4_loop15_posco_minres_lithium_jv",
  "symbols": "005490/003670",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_supply_security",
  "trigger_date": "2025-11-11",
  "minres_deal_value_usd_mn": 765,
  "minres_event_mfe_pct": 10.8,
  "posco_effective_interest_wodgina_pct": 15,
  "posco_effective_interest_mt_marion_pct": 15,
  "spodumene_mid_2025_low_usd_t": 610,
  "spodumene_august_2025_usd_t": 880,
  "spodumene_2022_peak_usd_t": 6000,
  "operator": "MinRes",
  "posco_direct_price_anchor": "price_data_unavailable_after_deep_search",
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_supply_security_not_Green"
}
```

### 판정

```text
score_price_alignment = success_candidate_stage2
new_rule = upstream lithium stake는 supply-security Stage2
but = lithium price와 downstream margin 없으면 Yellow/Green 금지
```

---

## Case D — Hyundai Steel / POSCO Chinese steel-plate anti-dumping

```text
symbols = 004020 / 005490
case_type = Stage2-Actionable / spread relief
archetype = STEEL_ANTIDUMPING_SPREAD_STAGE2_ACTIONABLE
```

### Trigger grid

| trigger | type                    |       date | 당시 공개 evidence                                                                               | 가격 anchor                                     | outcome                 |
| ------- | ----------------------- | ---------: | -------------------------------------------------------------------------------------------- | --------------------------------------------- | ----------------------- |
| T0      | awareness               |  2024~2025 | Chinese cheap steel import pressure, Korean steel spread squeeze                             | no price                                      | Stage1                  |
| T1      | Stage2 evidence         | 2025-02-20 | Korea provisionally imposes 27.91~38.02% anti-dumping tariffs on Chinese steel plates        | Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7% | Stage2-Actionable       |
| T2      | Stage3-Yellow candidate | 2025-02-20 | steel plates used in shipbuilding/construction; 2024 Chinese steel imports $10.4B, 49% share | same                                          | margin relief candidate |
| T3      | 4B-watch                | 2025-02-20 | tariff relief does not equal demand recovery; U.S. steel tariff risk remains                 | no full OHLC                                  | 4B-watch                |
| T4      | Stage3-Green            |        N/A | ASP / utilization / margin confirmed? not yet                                                | N/A                                           | no Green                |

Hyundai Steel/POSCO anti-dumping trigger는 R4에서 **Stage2-Actionable**에 가깝다. 철강판은 조선·건설에 쓰이고, 중국산 저가 수입이 domestic spread를 압박하던 상황에서 27.91~38.02% provisional duty가 나왔다. 현대제철은 +5.8%, POSCO Holdings는 +3.9%, KOSPI는 -0.7%였다. 이 조합은 “관세 headline”만은 아니고, spread relief evidence + relative strength가 붙은 trigger다. 다만 ASP, volume, utilization, margin이 실제로 개선되기 전에는 Green이 아니다. ([Reuters][4])

### Trigger price validation row

```json
{
  "case_id": "r4_loop15_hyundai_posco_steel_antidumping",
  "symbols": "004020/005490",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable",
  "trigger_date": "2025-02-20",
  "anti_dumping_tariff_pct": "27.91-38.02",
  "chinese_steel_imports_2024_usd_bn": 10.4,
  "chinese_share_of_korea_steel_imports_pct": 49,
  "hyundai_steel_event_mfe_pct": 5.8,
  "posco_event_mfe_pct": 3.9,
  "kospi_same_context_pct": -0.7,
  "hyundai_market_relative_pp": 6.5,
  "posco_market_relative_pp": 4.6,
  "steel_product_use": [
    "shipbuilding",
    "construction"
  ],
  "stage3_gate_missing": [
    "ASP_recovery",
    "volume_recovery",
    "utilization",
    "raw_material_spread",
    "steel_margin"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_spread_relief"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
new_rule = anti-dumping + relative strength + import-share evidence는 Stage2-Actionable
but = margin/ASP 확인 전 Green 금지
```

---

## Case E — Hyundai Steel weak construction/shipbuilding demand

```text
symbol = 004020
case_type = failed_rerating / 4C-watch
archetype = STEEL_WEAK_DEMAND_FAILED_RERATING
```

### Trigger grid

| trigger | type            |                          date | 당시 공개 evidence                                                             | 가격 anchor                       | outcome         |
| ------- | --------------- | ----------------------------: | -------------------------------------------------------------------------- | ------------------------------- | --------------- |
| T0      | awareness       |                          2024 | 건설·조선 steel demand 둔화                                                      | no full OHLC                    | watch           |
| T1      | 4C-watch        |                    2024-06-21 | Nomura expects rebar price -10%; 2024 net profit estimate -73% to 215B won | Hyundai Steel -1.2%, 29,000 won | thesis watch    |
| T2      | failed_rerating |                    2024-06-21 | target -14% to 30,000 won, Neutral maintained                              | same                            | failed rerating |
| T3      | relief trigger  |                    2025-02-20 | anti-dumping tariff                                                        | +5.8%                           | Stage2 relief   |
| T4      | 4C              | if demand/price keeps falling | not confirmed                                                              | pending                         |                 |

현대제철 weak-demand trigger는 R4 steel spread의 downside calibration이다. Nomura는 2024년 rebar price가 10% 하락할 수 있다고 봤고, 2024년 net-profit forecast를 73% 낮춰 215B won으로 조정했다. 목표주가도 14% 낮춘 30,000 won, 당시 주가는 -1.2%로 29,000 won이었다. 이 trigger는 “소재주는 정책으로만 보면 안 되고 최종수요와 spread가 먼저”라는 반례다. ([마켓워치][5])

### Trigger price validation row

```json
{
  "case_id": "r4_loop15_hyundai_steel_weak_demand",
  "symbol": "004020",
  "best_trigger": "T1/T2",
  "best_trigger_type": "4C-watch",
  "trigger_date": "2024-06-21",
  "entry_price_anchor_krw": 29000,
  "event_mae_pct": -1.2,
  "rebar_price_decline_expected_pct": -10,
  "net_profit_estimate_after_cut_krw_bn": 215,
  "net_profit_estimate_cut_pct": -73,
  "target_price_krw": 30000,
  "target_price_cut_pct": -14,
  "sector_risk": [
    "construction_demand",
    "shipbuilding_plate_competition",
    "Japanese_Chinese_steel_competition"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "failed_rerating_4C_watch"
}
```

### 판정

```text
score_price_alignment = thesis_break_watch
new_rule = rebar price / net-profit estimate cut은 소재 spread 4C-watch
```

---

## Case F — Hyundai Steel U.S. localization capex

```text
symbol = 004020
case_type = false_positive_score
archetype = LOCALIZATION_CAPEX_FALSE_POSITIVE
```

### Trigger grid

| trigger | type            |          date | 당시 공개 evidence                                                                                           | 가격 anchor                                                   | outcome                        |
| ------- | --------------- | ------------: | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------ |
| T0      | Stage2 headline | 2025-03-24/25 | Hyundai Steel $5.8~6B U.S. plant, Louisiana, 2.7M tonnes capacity, Hyundai Motor Group $21B U.S. package | initially +5%, then -4.4%                                   | evidence_good_but_price_failed |
| T1      | false_positive  |    2025-04-22 | funding details unclear, 50% debt, possible POSCO equity, plant output above Hyundai/Kia U.S. target     | Hyundai Steel -21.2% since announcement                     | false positive                 |
| T2      | 4C-watch        |    2025-04-22 | weak domestic demand, cheap Chinese imports, labor disputes, tariff strategy uncertainty                 | POSCO -18.3%, KOSPI -5.5%, Hyundai Motor -12.9% same period | capex/IRR watch                |
| T3      | Stage3          |           N/A | customer contract / IRR / funding not confirmed                                                          | N/A                                                         | no Stage3                      |

현대제철 U.S. plant case는 R4의 대표 false positive다. 처음에는 미국 현지화와 tariff hedge처럼 보였고, 장중 +5% 이상도 나왔다. 하지만 같은 날 -4.4%로 반전했고, 이후 Reuters는 발표 이후 현대제철 주가가 -21.2% 빠졌다고 보도했다. 투자자들이 문제 삼은 건 공장 자체가 아니라 **funding detail, IRR, 생산능력 대비 실제 수요, tariff saving durability**였다. ([Reuters][6])

### Trigger price validation row

```json
{
  "case_id": "r4_loop15_hyundai_steel_us_localization_capex",
  "symbol": "004020",
  "best_trigger": "T1",
  "best_trigger_type": "false_positive_score",
  "t0_date": "2025-03-25",
  "t0_initial_mfe_pct": 5.0,
  "t0_close_event_return_pct": -4.4,
  "us_plant_investment_usd_bn": 5.8,
  "us_plant_capacity_mn_tonnes": 2.7,
  "hyundai_group_us_package_usd_bn": 21,
  "t1_stock_decline_since_announcement_pct": -21.2,
  "posco_same_period_decline_pct": -18.3,
  "kospi_same_period_decline_pct": -5.5,
  "hyundai_motor_same_period_decline_pct": -12.9,
  "planned_output_vehicle_equivalent_mn": 1.8,
  "hyundai_kia_us_production_target_mn": 1.2,
  "debt_funding_share_pct": 50,
  "full_funding_plan_disclosed": false,
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "false_positive_score"
}
```

### 판정

```text
score_price_alignment = false_positive_score
new_rule = localization capex는 funding/IRR/customer demand 없으면 Green 금지
```

---

## Case G — Korea Zinc / MBK-Young Poong tender battle

```text
symbols = 010130 / 000670
case_type = 4B-watch / control premium
archetype = KOREA_ZINC_CONTROL_PREMIUM_4B
```

### Trigger grid

| trigger | type                   |          date | 당시 공개 evidence                                                                               | 가격 anchor                                  | outcome                |
| ------- | ---------------------- | ------------: | -------------------------------------------------------------------------------------------- | ------------------------------------------ | ---------------------- |
| T0      | awareness              |    2024-09-13 | MBK/Young Poong $1.5B tender offer, offer price 660,000 won, 19% premium                     | Korea Zinc +24%, high 690,000; KOSPI -0.2% | control premium 4B     |
| T1      | 4B extension           |    2024-10-08 | FSS orders probe into tender offers; Korea Zinc +13% MTD after +29% previous month           | record levels                              | governance 4B          |
| T2      | 4B overheat            | 2024-10-24/25 | Korea Zinc tender/buyback battle; stock +29.9% upper limit previous day, then high 1,470,000 | +10.2% after +29% intraday                 | retail/control premium |
| T3      | Stage2 strategic asset |    2024-11-18 | battery material technology subject to export controls / national core technology ruling     | price unavailable                          | strategic asset        |
| T4      | 4C-watch               |       ongoing | debt-funded buyback, governance fight, share issuance risk                                   | no full OHLC                               | control risk           |

Korea Zinc tender battle은 R4의 대표 4B다. Korea Zinc는 세계 최대 refined zinc producer라는 소재/전략자산 narrative가 있지만, 2024년 9~10월 주가 움직임의 본체는 zinc spread가 아니라 **control premium**이었다. MBK/Young Poong tender offer는 660,000 won, 전일 종가 대비 19% premium이었고 Korea Zinc는 장중 +24%로 690,000 won을 찍었다. 이후 FSS probe, buyback, tender battle이 격화되면서 +29.9% upper limit, 1,470,000 won 고점까지 나왔다. 이건 operating Stage3가 아니라 **4B control-premium overlay**다. ([월스트리트저널][7])

### Trigger price validation row

```json
{
  "case_id": "r4_loop15_korea_zinc_control_premium",
  "symbols": "010130/000670",
  "best_trigger": "T0/T2",
  "best_trigger_type": "4B_control_premium",
  "t0_date": "2024-09-13",
  "tender_offer_value_krw_trn": 2.0,
  "tender_offer_value_usd_bn": 1.5,
  "offer_price_krw": 660000,
  "prior_close_krw": 556000,
  "tender_premium_pct": 18.7,
  "korea_zinc_event_mfe_pct": 24,
  "korea_zinc_event_high_krw": 690000,
  "kospi_same_context_pct": -0.2,
  "target_stake_max_pct": 14.6,
  "t2_upper_limit_return_pct": 29.9,
  "t2_record_high_krw": 1470000,
  "young_poong_mbk_stake_context_pct": 38.5,
  "operating_cashflow_improvement_confirmed": false,
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "event_premium_4B_control_premium"
}
```

### 판정

```text
score_price_alignment = event_premium_4B_watch
new_rule = control premium과 operating spread/margin을 분리
```

---

## Case H — Korea Zinc / U.S. critical minerals refinery + share-sale fight

```text
symbol = 010130
case_type = Stage2 strategic-resource + 4B dilution/governance overlay
archetype = CRITICAL_MINERALS_SMELTER_STAGE2_WITH_DILUTION_4B
```

### Trigger grid

| trigger | type                        |       date | 당시 공개 evidence                                                                                            | 가격 anchor                      | outcome                     |
| ------- | --------------------------- | ---------: | --------------------------------------------------------------------------------------------------------- | ------------------------------ | --------------------------- |
| T0      | Stage2 strategic asset      | 2024-11-18 | Korea Zinc battery material technology found subject to export controls / national core technology ruling | price unavailable              | strategic asset             |
| T1      | Stage2 evidence             | 2025-12-15 | U.S. backs $7.4B Tennessee critical minerals processing plant                                             | shares +27% local-media report | Stage2                      |
| T2      | Stage2-Actionable candidate | 2025-12-15 | antimony, germanium, gallium, zinc, lead, copper, gold, silver; operations 2027~2029                      | no full OHLC                   | candidate                   |
| T3      | 4B / false-positive risk    | 2025-12-16 | MBK/Young Poong seek injunction against share issuance; shares -13%                                       | -13%                           | dilution/governance overlay |
| T4      | Stage3-Green                |        N/A | funding finalized, no injunction, customer offtake / margin not confirmed                                 | N/A                            | no Green                    |

Korea Zinc critical minerals refinery trigger는 R4에서 Stage2 strategic-resource다. FT는 U.S. government가 Korea Zinc의 $7.4B Tennessee critical minerals processing plant를 backed 했고, 이 facility가 antimony, germanium, gallium, zinc, lead, copper, gold, silver 등을 처리할 것이라고 보도했다. local media 보도 후 Korea Zinc shares는 +27%까지 올랐다. 하지만 다음 날 Reuters는 MBK/Young Poong이 해당 share-sale plan을 막기 위한 injunction을 냈고, Korea Zinc shares가 -13% 하락했다고 보도했다. 따라서 이 case는 **Stage2 strategic asset + 4B dilution/governance overlay**로 병기해야 한다. ([Financial Times][8])

### Trigger price validation row

```json
{
  "case_id": "r4_loop15_korea_zinc_us_critical_minerals_smelter",
  "symbol": "010130",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_strategic_resource_with_4B_overlay",
  "t0_national_core_technology_ruling": true,
  "t1_date": "2025-12-15",
  "us_refinery_investment_usd_bn": 7.4,
  "materials": [
    "antimony",
    "germanium",
    "gallium",
    "zinc",
    "lead",
    "copper",
    "gold",
    "silver"
  ],
  "commercial_operation_period": "2027-2029",
  "t1_event_mfe_pct": 27,
  "t3_date": "2025-12-16",
  "t3_event_mae_pct": -13,
  "mbk_youngpoong_combined_stake_pct": 44,
  "share_issuance_objected": true,
  "funding_plan_finalized": false,
  "offtake_or_margin_confirmed": false,
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_with_4B_dilution_governance_overlay"
}
```

### 판정

```text
score_price_alignment = Stage2_with_4B_overlay
new_rule = strategic-minerals capex는 funding/governance/offtake 확인 전 Green 금지
```

---

## Case I — Copper TC/RC squeeze and Korea smelter margin

```text
symbols = LS MnM / Korea Zinc / copper-smelter read-through
case_type = 4C-watch
archetype = COPPER_TCRC_SPREAD_4C_WATCH
```

### Trigger grid

| trigger | type          |       date | 당시 공개 evidence                                                                                                          | 가격 anchor       | outcome              |
| ------- | ------------- | ---------: | ----------------------------------------------------------------------------------------------------------------------- | --------------- | -------------------- |
| T0      | awareness     | 2025-10-15 | Japan/Spain/South Korea warn copper TC/RCs have become unsustainable                                                    | no listed price | smelter margin watch |
| T1      | 4C-watch      | 2025-10-15 | TC/RCs falling, some Chinese smelters process for free/loss, global smelters consider scale-down/exit                   | no KRX price    | spread 4C            |
| T2      | price event   | 2025-10-30 | copper record $11,200/t, up 27% YTD, mine supply concern                                                                | no KRX          | price event          |
| T3      | squeeze event | 2025-12-04 | Mercuria withdraws >40,000t copper from LME Korea/Taiwan warehouses; copper $11,540/t; cancelled warrants 35% of stocks | no direct price | supply squeeze       |
| T4      | Stage3-Yellow |        N/A | smelter margin recovery not confirmed                                                                                   | no              | no Yellow            |

Copper는 가격만 보면 bullish지만, Korea smelter 관점에서는 TC/RC가 핵심이다. Reuters는 Japan·Spain·South Korea가 copper treatment/refining charges의 붕괴를 두고 공동 우려를 냈고, 일부 중국 smelter가 free 또는 loss로 처리하는 상황까지 언급했다고 보도했다. 반면 copper price는 record high를 찍고, Mercuria가 Korea/Taiwan LME warehouse에서 40,000t 이상을 withdraw하면서 supply squeeze가 커졌다. 이건 **copper price bullish와 smelter margin bullish가 다르다**는 R4 핵심 교정값이다. ([Reuters][9])

### Trigger price validation row

```json
{
  "case_id": "r4_loop15_copper_tcrc_smelt_margin_watch",
  "symbols": "LS_MnM/Korea_Zinc/copper_smelter_readthrough",
  "best_trigger": "T1",
  "best_trigger_type": "4C-watch",
  "trigger_date": "2025-10-15/2025-12-04",
  "tcrc_market_condition": "unsustainable",
  "some_chinese_smelters_processing_fee_condition": "free_or_loss",
  "global_smelter_scale_down_exit_watch": true,
  "copper_record_price_oct_2025_usd_t": 11200,
  "copper_ytd_gain_2025_pct": 27,
  "copper_record_price_dec_2025_usd_t": 11540,
  "mercuria_withdrawal_tonnes": 40000,
  "cancelled_lme_warrants_tonnes": 56875,
  "cancelled_warrants_share_lme_stocks_pct": 35,
  "copper_value_withdrawn_usd_mn": 460,
  "direct_listed_price_anchor": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "4C_watch_for_smilter_spread_despite_copper_price_bullish"
}
```

### 판정

```text
score_price_alignment = thesis_break_watch
new_rule = copper price와 smelter TC/RC spread를 분리해서 scoring
```

---

## Case J — China strategic mineral export controls

```text
symbols = 003670 / 051910 / 010130 / strategic-materials basket
case_type = 4C strategic reference
archetype = CHINA_STRATEGIC_MINERAL_EXPORT_CONTROL_4C
```

### Trigger grid

| trigger | type                |                                          date | 당시 공개 evidence                                                                                                           | 가격 anchor       | outcome              |
| ------- | ------------------- | --------------------------------------------: | ------------------------------------------------------------------------------------------------------------------------ | --------------- | -------------------- |
| T0      | awareness           |                               2023-07~2023-10 | gallium/germanium restrictions, graphite permits                                                                         | no direct price | strategic watch      |
| T1      | 4C-watch            |                                    2024-08-15 | China limits antimony and related technology; rare-earth magnet tech ban, graphite export permits context                | no direct KRX   | 4C reference         |
| T2      | 4C-watch            |                                    2025-02-04 | tungsten, bismuth, indium, tellurium, molybdenum controls; battery/lithium/gallium processing tech proposed restrictions | no price        | broadening hard gate |
| T3      | hard gate candidate | if export denial causes production disruption | not confirmed                                                                                                            | pending         | no hard 4C           |

China strategic mineral export controls는 R4 전 섹터의 hard reference다. Reuters는 China가 graphite export permits, rare-earth magnet technology ban, antimony controls, gallium/germanium restrictions, tungsten/bismuth/indium/tellurium/molybdenum controls, battery/lithium/gallium processing technology restrictions 등을 연쇄적으로 적용하거나 제안했다고 정리했다. 이는 POSCO Future M, LG Chem, Korea Zinc, battery material supply chain 모두에 4C overlay가 필요한 이유다. ([Reuters][10])

### Trigger price validation row

```json
{
  "case_id": "r4_loop15_china_strategic_mineral_export_controls",
  "symbols": "003670/051910/010130/strategic_materials_basket",
  "best_trigger": "T1/T2",
  "best_trigger_type": "4C_strategic_reference",
  "controlled_materials": [
    "graphite",
    "rare_earth_magnet_technology",
    "antimony",
    "gallium",
    "germanium",
    "tungsten",
    "bismuth",
    "indium",
    "tellurium",
    "molybdenum",
    "battery_processing_technology",
    "lithium_processing_technology"
  ],
  "china_graphite_refining_share_context_pct": 90,
  "hard_4c_confirmed_for_specific_krx_name": false,
  "direct_listed_price_anchor": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "strategic_materials_4C_watch_reference"
}
```

### 판정

```text
score_price_alignment = thesis_break_reference
new_rule = 소재 Stage3에는 China export-control exposure를 항상 overlay
```

---

# 6. Trigger별 가격경로 검증 요약

| case                      | best trigger |             entry anchor |                  event MFE/MAE |      market-relative | full MFE/MAE | outcome                              |
| ------------------------- | ------------ | -----------------------: | -----------------------------: | -------------------: | ------------ | ------------------------------------ |
| POSCO Future M graphite   | T1/T2        |           no exact price |                           +20% |          unavailable | unavailable  | Stage2-Actionable / Yellow candidate |
| CATL lithium event        | T2           |                    event |       POSCO FM +8.3%, L&F +10% |          unavailable | unavailable  | event premium                        |
| POSCO/MinRes              | T1/T2        |        POSCO unavailable |                  MinRes +10.8% |          unavailable | unavailable  | Stage2 supply-security               |
| Steel anti-dumping        | T1/T2        |                    event |     Hyundai +5.8%, POSCO +3.9% |      +6.5pp / +4.6pp | unavailable  | Stage2-Actionable                    |
| Hyundai Steel weak demand | T1           |                   29,000 |                          -1.2% |          unavailable | unavailable  | 4C-watch                             |
| Hyundai Steel U.S. capex  | T0/T1        |                    event |      +5% → -4.4%, later -21.2% | underperformed KOSPI | unavailable  | false positive                       |
| Korea Zinc tender         | T0/T2        | 690,000 / 1,470,000 high | +24%, later +29.9% upper limit |               strong | unavailable  | control premium 4B                   |
| Korea Zinc U.S. refinery  | T1/T3        |                    event |                +27%, then -13% |          unavailable | unavailable  | Stage2 + 4B                          |
| Copper TC/RC              | T1           |          no direct price |                            N/A |                  N/A | unavailable  | 4C-watch                             |
| China export controls     | T1/T2        |          no direct price |                            N/A |                  N/A | unavailable  | 4C reference                         |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
POSCO/MinRes:
supply-security Stage2. 직접 POSCO 가격 anchor는 없지만, deal structure는 명확.

LG Chem/Toyota류와 유사한 FEOC/전략자원 risk reduction:
Stage2는 가능하지만 cashflow 전환 전 Yellow 보류.

China export-control reference:
가격 trigger라기보다 모든 소재 case에 붙는 4C overlay.
```

## Stage 2-Actionable entry 성과

```text
POSCO Future M graphite tariff:
+20% event move. tariff rate, China dependence, strategic supply-chain thesis가 강함.
다만 capacity/quality/customer award gate가 남아 Stage3-Green은 금지.

Hyundai Steel/POSCO anti-dumping:
Hyundai +5.8%, POSCO +3.9%, KOSPI -0.7%.
spread relief + relative strength라 Stage2-Actionable 가능.
```

## Stage 3-Yellow 후보

```text
POSCO Future M graphite tariff:
tariff + non-China premium + strong price response.
하지만 quality/capacity/customer certification이 남아 Yellow candidate.

Korea Zinc U.S. critical minerals refinery:
strategic minerals + U.S. backing + +27%.
하지만 funding/share issuance/governance/offtake margin이 남아 Yellow 보류 또는 Stage2 + 4B.
```

## Stage3-Green

```text
이번 R4 Loop 15에서 확정 Green 없음.

이유:
- graphite는 capacity/quality/customer award 미확인
- lithium은 durable price/margin 미확인
- steel tariff는 margin/ASP 미확인
- Korea Zinc refinery는 funding/governance/offtake 미확인
- copper price는 smelter TC/RC와 충돌
```

## 기존 점수표가 놓쳤을 가능성

```text
Stage2_promote_candidate:
- POSCO Future M graphite tariff
- Hyundai Steel/POSCO anti-dumping
- Korea Zinc strategic minerals refinery, 단 4B overlay

missed_structural 가능성:
- graphite tariff trigger는 full OHLC에서 MFE/MAE가 좋으면 Stage3-Yellow 승격 가능.
- steel anti-dumping도 full OHLC에서 spread 개선이 확인되면 Stage2→Yellow 승격 가능.

false positive risk:
- Hyundai Steel U.S. capex
- Korea Zinc control premium
- CATL lithium event
```

---

# 8. score-price alignment 판정

```text
Stage2_promote_candidate:
- POSCO Future M graphite tariff
- Hyundai Steel/POSCO anti-dumping
- Korea Zinc U.S. critical minerals refinery, but with 4B overlay

Stage3-Yellow candidate:
- POSCO Future M graphite tariff
- Korea Zinc strategic minerals refinery, only if funding/offtake cleared
- steel anti-dumping, only if ASP/margin confirmed

Stage3-Green:
- 없음

event_premium:
- CATL lithium mine suspension
- Korea Zinc tender battle
- Korea Zinc U.S. refinery first pop
- steel anti-dumping first reaction

false_positive_score:
- Hyundai Steel U.S. localization capex

thesis_break_watch:
- Hyundai Steel weak demand
- copper TC/RC squeeze
- China strategic mineral export controls
- Korea Zinc share issuance / governance injunction

price_moved_without_evidence:
- lithium rally if no durable price/margin evidence
- control-premium rally if treated as operating Green
```

---

# 9. 점수비중 교정

## 올릴 축

```text
tariff_rate_and_import_share +5
china_dependency_reduction +5
non_china_capacity_quality_certification +5
spread_margin_visibility +5
raw_material_price_durability +4
tcrc_smelt_margin +5
strategic_resource_offtake_contract +5
funding_irr_capex_clarity +5
control_premium_separation +5
export_control_exposure +5
```

### 근거

POSCO Future M graphite tariff는 tariff와 China dependency reduction이 강한 trigger였지만, capacity/quality/certification이 남았다. Hyundai Steel anti-dumping은 import-share와 tariff rate가 분명해 Stage2-Actionable이었다. Korea Zinc는 strategic resource premium이 강하지만 control premium과 capex/dilution을 분리해야 한다. Copper case는 metal price가 좋아도 TC/RC가 무너지면 smelter margin이 악화될 수 있음을 보여준다.

## 내릴 축

```text
commodity_price_event_only -5
control_premium_as_operating_green -5
localization_capex_without_funding -5
upstream_stake_without_downstream_margin -4
tariff_headline_without_ASP_volume -4
lithium_supply_shock_without_inventory_draw -4
metal_price_without_spread -5
strategic_resource_label_only -4
```

### 근거

CATL mine suspension은 소재주를 띄웠지만 durable lithium margin은 아니었다. Korea Zinc tender battle은 operating cashflow가 아니라 control premium이었다. Hyundai Steel U.S. plant는 localization capex headline이 오히려 -21.2% false positive가 됐다. Copper record high는 smelter TC/RC collapse와 충돌했다.

---

# 10. Stage 2-Actionable 승격 조건

R4 Loop 15 shadow rule:

```text
R4에서 Stage 2 evidence가 아래 중 3개 이상을 충족하면 Stage2-Actionable로 승격한다.

1. tariff rate / anti-dumping duty / import share가 숫자로 확인된다.
2. 중국 의존도 또는 FEOC/export-control risk가 구조적으로 낮아진다.
3. trigger 당일 market-relative +5pp 이상 가격 반응이 있다.
4. spread 개선 가능성이 ASP/원재료/수입단가 측면에서 설명 가능하다.
5. 고객 인증, capacity, offtake, quality gate 중 최소 하나가 일부 확인된다.
6. 단순 commodity spot rally가 아니라 기업 margin으로 연결될 가능성이 있다.
```

적용:

```text
POSCO Future M graphite tariff:
tariff + China dependency + +20%.
Stage2-Actionable.

Hyundai Steel/POSCO anti-dumping:
tariff 27.91~38.02% + import share 49% + relative strength.
Stage2-Actionable.

Korea Zinc U.S. critical minerals refinery:
strategic resource + U.S. backing + +27%.
Stage2, but 4B overlay strong.
```

---

# 11. Stage 3-Yellow 조건

```text
Stage3-Yellow:
- spread improvement 또는 strategic resource cashflow 가능성이 숫자로 보임
- 하지만 capacity, customer qualification, offtake, funding, IRR 중 하나가 남아 있음
```

후보:

```text
POSCO Future M graphite tariff:
Yellow candidate, but quality/capacity/customer award missing.

Hyundai Steel anti-dumping:
Yellow candidate only if ASP/margin improvement follows.

Korea Zinc U.S. refinery:
Yellow candidate only if funding/offtake/governance clears.
```

---

# 12. Stage 3-Green 조건

```text
Stage3-Green:
- spread 개선이 실제 실적에 반영됨
- ASP/volume/utilization/margin이 확인됨
- upstream stake가 downstream cost advantage로 연결됨
- strategic resource project funding과 offtake가 확정됨
- control premium이 아니라 operating FCF가 개선됨
- full-window MFE/MAE가 우호적
```

이번 R4 Loop 15에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- control premium으로 +20~30% 급등
- commodity spot event로 +8~20% 급등하지만 margin evidence 없음
- strategic-resource capex가 +20% 이상 띄운 뒤 funding/share issuance 불확실
- localization capex 발표 후 세부 funding/IRR 부재
- tender/buyback/share issuance가 operating thesis보다 가격을 지배
```

적용:

```text
Korea Zinc tender battle:
4B control premium.

Korea Zinc U.S. refinery:
Stage2 strategic asset + 4B dilution/governance overlay.

CATL lithium event:
event premium / 4B-watch.

Hyundai Steel U.S. plant:
false positive / 4B-to-4C failure.
```

---

# 14. 4C hard gate 조건

```text
R4 4C:
- TC/RC가 collapse하여 smelter margin이 무너짐
- commodity price rally가 기업 spread로 연결되지 않음
- 중국 export-control로 graphite/rare earth/antimony/gallium/germanium sourcing이 막힘
- capex funding gap / dilution / injunction 발생
- control premium 소멸 후 operating valuation으로 복귀
- lithium price 재하락 / inventory write-down / ASP pass-through 실패
```

이번 R4 Loop 15에서 **hard 4C 확정은 없음**.

```text
hard_4c_not_confirmed = true
```

하지만 strong 4C-watch는 있다.

```text
- Copper TC/RC collapse
- China strategic mineral export controls
- Hyundai Steel weak demand
- Hyundai Steel U.S. plant funding/IRR failure
- Korea Zinc share issuance / governance injunction
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_227.md 요약

```md
# R4 Loop 15. Materials / Spread / Strategic Resources Trigger-level Price Validation

이번 라운드는 R4 Loop 15 trigger-level validation 라운드다.

핵심 결론:
- POSCO Future M graphite tariff is Stage2-Actionable / Stage3-Yellow candidate. U.S. announced 93.5% anti-dumping tariff on Chinese graphite/anode active materials; POSCO Future M +20%, Syrah +22%, Nouveau Monde +26%. But non-China quality, capacity and customer certification remain gates.
- CATL Yichun/Jianxiawo lithium mine suspension is event premium. POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%. CATL said no material impact and license renewal could resume output; lithium rally may be speculative.
- POSCO / MinRes lithium JV is Stage2 supply-security. POSCO pays $765M for 30% lithium JV stake, gaining indirect 15% interest in Wodgina and Mt Marion. Spodumene prices remain far below 2022 highs, so Green requires cost advantage and downstream margin.
- Hyundai Steel / POSCO anti-dumping is Stage2-Actionable. Korea imposed provisional 27.91~38.02% tariffs on Chinese steel plates; Chinese steel imports were $10.4B and 49% of Korea steel imports. Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7%.
- Hyundai Steel weak demand is 4C-watch. Rebar price expected -10%, 2024 net-profit estimate cut 73% to 215B won, target cut 14%, shares -1.2% at 29,000 won.
- Hyundai Steel U.S. plant is localization capex false positive. Initial +5% reversed to -4.4%; later shares had lost 21.2% since the announcement due unclear funding, IRR and demand.
- Korea Zinc tender battle is control-premium 4B. MBK/Young Poong tender offer at 660,000 won sent Korea Zinc +24%; later takeover battle drove upper-limit +29.9% and 1,470,000 won high. This is not operating spread Green.
- Korea Zinc U.S. critical minerals refinery is Stage2 strategic-resource with 4B overlay. U.S.-backed $7.4B refinery drove +27%, but share-sale injunction news later sent shares -13%.
- Copper TC/RC squeeze is 4C-watch. Copper record price is bullish, but Japan/Spain/South Korea warned that collapsing TC/RCs make smelter operations unsustainable.
- China strategic mineral export controls are R4 hard reference. Graphite, rare-earth magnet technology, antimony, gallium/germanium, tungsten/bismuth/indium/tellurium/molybdenum controls require persistent 4C overlay.

Main calibration:
- Raise tariff_rate_and_import_share, China dependency reduction, non-China capacity/quality certification, spread margin visibility, raw material price durability, TC/RC smelt margin, strategic resource offtake, funding/IRR capex clarity, control-premium separation, export-control exposure.
- Lower commodity price event-only, control premium as operating Green, localization capex without funding, upstream stake without downstream margin, tariff headline without ASP/volume, lithium supply shock without inventory draw, metal price without spread.
```

## docs/checkpoints/checkpoint_28a_round227_r4_loop15.md 요약

```md
# Checkpoint 28A Round 227 R4 Loop 15 Trigger-level Calibration

## 반영 내용
- R4 Loop 15 trigger-level validation을 수행했다.
- POSCO Future M graphite tariff, CATL lithium event, POSCO/MinRes lithium JV, Hyundai Steel/POSCO anti-dumping, Hyundai Steel weak demand, Hyundai Steel U.S. capex, Korea Zinc tender battle, Korea Zinc U.S. critical-minerals refinery, copper TC/RC squeeze, China strategic mineral export controls를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / FT / WSJ / MarketWatch의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- tariff + import share + China dependency reduction + relative strength 조합은 Stage2-Actionable 승격 후보.
- commodity spot rally는 durable spread/margin 전까지 event premium.
- strategic-resource capex는 funding/IRR/offtake/governance 확인 전 Green 금지.
- metal price와 smelter TC/RC spread를 분리해서 scoring한다.
- control premium은 operating cashflow와 분리한다.
```

## data/e2r_case_library/cases_r4_loop15_round227.jsonl 초안

```jsonl
{"case_id":"r4_loop15_posco_future_m_graphite_tariff","symbol":"003670","company_name":"POSCO Future M","case_type":"Stage2_promote_candidate","primary_archetype":"GRAPHITE_TARIFF_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable_to_Stage3-Yellow_candidate","price_validation":{"us_graphite_antidumping_tariff_pct":93.5,"approx_total_us_tariff_on_chinese_graphite_pct":160,"posco_future_m_event_mfe_pct":20,"syrah_resources_event_mfe_pct":22,"nouveau_monde_event_mfe_pct":26,"novonix_event_mfe_pct":15,"china_battery_grade_graphite_control_pct":99,"china_synthetic_graphite_control_pct":69,"stage3_gate_missing":["non_china_capacity","quality_certification","customer_award","anode_margin","IRA_FEOC_compliance_cashflow"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Graphite tariff and China dependency reduction justify Stage2-Actionable, but quality/capacity/customer award gates remain."}
{"case_id":"r4_loop15_catl_yichun_lithium_event","symbol":"003670/066970/006400/373220","company_name":"POSCO Future M / L&F / Samsung SDI / LGES","case_type":"event_premium","primary_archetype":"LITHIUM_PRICE_EVENT_PREMIUM","best_trigger":"T2","stage_candidate":"event_premium","price_validation":{"posco_future_m_event_mfe_pct":8.3,"lnf_event_mfe_pct":10.0,"samsung_sdi_event_mfe_pct":3.2,"lges_event_mfe_pct":2.8,"ganfeng_lithium_event_mfe_pct":21,"tianqi_lithium_event_mfe_pct":18,"cme_lithium_carbonate_august_rally_pct":27,"lithium_price_decline_from_2022_peak_pct":-90,"catl_material_impact_claim":"no_material_impact","license_renewal_possible":true,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium","notes":"Lithium supply-shock rally requires durable lithium price, inventory drawdown and material margin before Stage3."}
{"case_id":"r4_loop15_posco_minres_lithium_jv","symbol":"005490/003670","company_name":"POSCO Holdings / POSCO Future M","case_type":"success_candidate_stage2","primary_archetype":"UPSTREAM_LITHIUM_SUPPLY_SECURITY_STAGE2","best_trigger":"T1/T2","stage_candidate":"Stage2_supply_security","price_validation":{"minres_deal_value_usd_mn":765,"minres_event_mfe_pct":10.8,"posco_effective_interest_wodgina_pct":15,"posco_effective_interest_mt_marion_pct":15,"spodumene_mid_2025_low_usd_t":610,"spodumene_august_2025_usd_t":880,"spodumene_2022_peak_usd_t":6000,"operator":"MinRes","posco_direct_price_anchor":"price_data_unavailable_after_deep_search","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"Upstream lithium stake improves supply security, but Stage3 requires cost advantage and downstream margin."}
{"case_id":"r4_loop15_hyundai_posco_steel_antidumping","symbol":"004020/005490","company_name":"Hyundai Steel / POSCO Holdings","case_type":"Stage2_promote_candidate","primary_archetype":"STEEL_ANTIDUMPING_SPREAD_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"anti_dumping_tariff_pct":"27.91-38.02","chinese_steel_imports_2024_usd_bn":10.4,"chinese_share_of_korea_steel_imports_pct":49,"hyundai_steel_event_mfe_pct":5.8,"posco_event_mfe_pct":3.9,"kospi_same_context_pct":-0.7,"hyundai_market_relative_pp":6.5,"posco_market_relative_pp":4.6,"steel_product_use":["shipbuilding","construction"],"stage3_gate_missing":["ASP_recovery","volume_recovery","utilization","raw_material_spread","steel_margin"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Anti-dumping tariff, import share and relative strength make this Stage2-Actionable; Green needs ASP/volume/margin."}
{"case_id":"r4_loop15_hyundai_steel_weak_demand","symbol":"004020","company_name":"Hyundai Steel","case_type":"failed_rerating_4c_watch","primary_archetype":"STEEL_WEAK_DEMAND_FAILED_RERATING","best_trigger":"T1/T2","stage_candidate":"4C-watch","price_validation":{"entry_price_anchor_krw":29000,"event_mae_pct":-1.2,"rebar_price_decline_expected_pct":-10,"net_profit_estimate_after_cut_krw_bn":215,"net_profit_estimate_cut_pct":-73,"target_price_krw":30000,"target_price_cut_pct":-14,"sector_risk":["construction_demand","shipbuilding_plate_competition","Japanese_Chinese_steel_competition"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"Rebar price and net-profit estimate cuts are materials spread 4C-watch triggers."}
{"case_id":"r4_loop15_hyundai_steel_us_localization_capex","symbol":"004020","company_name":"Hyundai Steel","case_type":"false_positive_score","primary_archetype":"LOCALIZATION_CAPEX_FALSE_POSITIVE","best_trigger":"T1","stage_candidate":"false_positive_score","price_validation":{"initial_mfe_pct":5.0,"close_event_return_pct":-4.4,"us_plant_investment_usd_bn":5.8,"us_plant_capacity_mn_tonnes":2.7,"hyundai_group_us_package_usd_bn":21,"stock_decline_since_announcement_pct":-21.2,"posco_same_period_decline_pct":-18.3,"kospi_same_period_decline_pct":-5.5,"hyundai_motor_same_period_decline_pct":-12.9,"planned_output_vehicle_equivalent_mn":1.8,"hyundai_kia_us_production_target_mn":1.2,"debt_funding_share_pct":50,"full_funding_plan_disclosed":false,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"false_positive_score","notes":"Localization capex requires funding, IRR, customer demand and tariff saving clarity before Green."}
{"case_id":"r4_loop15_korea_zinc_control_premium","symbol":"010130/000670","company_name":"Korea Zinc / Young Poong / MBK","case_type":"event_premium_4b_watch","primary_archetype":"KOREA_ZINC_CONTROL_PREMIUM_4B","best_trigger":"T0/T2","stage_candidate":"4B-watch","price_validation":{"tender_offer_value_krw_trn":2.0,"tender_offer_value_usd_bn":1.5,"offer_price_krw":660000,"prior_close_krw":556000,"tender_premium_pct":18.7,"korea_zinc_event_mfe_pct":24,"korea_zinc_event_high_krw":690000,"kospi_same_context_pct":-0.2,"target_stake_max_pct":14.6,"upper_limit_return_pct":29.9,"record_high_krw":1470000,"young_poong_mbk_stake_context_pct":38.5,"operating_cashflow_improvement_confirmed":false,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_4B_watch","notes":"Control premium must be separated from smelter spread, zinc price and operating cashflow."}
{"case_id":"r4_loop15_korea_zinc_us_critical_minerals_smelter","symbol":"010130","company_name":"Korea Zinc","case_type":"Stage2_with_4B_overlay","primary_archetype":"CRITICAL_MINERALS_SMELTER_STAGE2_WITH_DILUTION_4B","best_trigger":"T1/T3","stage_candidate":"Stage2_strategic_resource_with_4B_overlay","price_validation":{"national_core_technology_ruling":true,"us_refinery_investment_usd_bn":7.4,"materials":["antimony","germanium","gallium","zinc","lead","copper","gold","silver"],"commercial_operation_period":"2027-2029","event_mfe_pct":27,"injunction_event_mae_pct":-13,"mbk_youngpoong_combined_stake_pct":44,"share_issuance_objected":true,"funding_plan_finalized":false,"offtake_or_margin_confirmed":false,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_with_4B_overlay","notes":"Strategic-resource capex needs funding, governance, offtake and margin before Green."}
{"case_id":"r4_loop15_copper_tcrc_smelt_margin_watch","symbol":"LS_MnM/Korea_Zinc/copper_smelter_readthrough","company_name":"Copper smelter read-through","case_type":"4c_watch","primary_archetype":"COPPER_TCRC_SPREAD_4C_WATCH","best_trigger":"T1","stage_candidate":"4C-watch","price_validation":{"tcrc_market_condition":"unsustainable","some_chinese_smelters_processing_fee_condition":"free_or_loss","global_smelter_scale_down_exit_watch":true,"copper_record_price_oct_2025_usd_t":11200,"copper_ytd_gain_2025_pct":27,"copper_record_price_dec_2025_usd_t":11540,"mercuria_withdrawal_tonnes":40000,"cancelled_lme_warrants_tonnes":56875,"cancelled_warrants_share_lme_stocks_pct":35,"copper_value_withdrawn_usd_mn":460,"direct_listed_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"Copper price bullishness and smelter TC/RC economics must be scored separately."}
{"case_id":"r4_loop15_china_strategic_mineral_export_controls","symbol":"003670/051910/010130/strategic_materials_basket","company_name":"Strategic materials export-control reference","case_type":"4c_reference","primary_archetype":"CHINA_STRATEGIC_MINERAL_EXPORT_CONTROL_4C","best_trigger":"T1/T2","stage_candidate":"4C-watch_reference","price_validation":{"controlled_materials":["graphite","rare_earth_magnet_technology","antimony","gallium","germanium","tungsten","bismuth","indium","tellurium","molybdenum","battery_processing_technology","lithium_processing_technology"],"china_graphite_refining_share_context_pct":90,"hard_4c_confirmed_for_specific_krx_name":false,"direct_listed_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_reference","notes":"China export-control exposure must be explicit overlay for all strategic-materials Stage3 candidates."}
```

## data/e2r_trigger_calibration/triggers_r4_loop15_round227.jsonl 초안

```jsonl
{"trigger_id":"r4l15_poscofm_graphite_T1","case_id":"r4_loop15_posco_future_m_graphite_tariff","trigger_type":"Stage2-Actionable","trigger_date":"2025-07-18","evidence_available":"U.S. 93.5% tariff on Chinese graphite/anode active materials, China graphite dominance, POSCO Future M +20%","event_return_pct":20,"trigger_outcome_label":"Stage2_promote_candidate","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r4l15_lithium_catl_T2","case_id":"r4_loop15_catl_yichun_lithium_event","trigger_type":"event_premium","trigger_date":"2025-08-11","evidence_available":"CATL Yichun mine suspension; POSCO Future M +8.3%, L&F +10%, but CATL says no material impact","event_return_pct":"POSCO Future M +8.3 / L&F +10 / SDI +3.2 / LGES +2.8","trigger_outcome_label":"event_premium_not_stage3","promote_to":"4B-watch"}
{"trigger_id":"r4l15_posco_minres_T1","case_id":"r4_loop15_posco_minres_lithium_jv","trigger_type":"Stage2_supply_security","trigger_date":"2025-11-11","evidence_available":"POSCO pays $765M for 30% MinRes lithium JV, 15% indirect Wodgina/Mt Marion exposure","event_return_pct":"MinRes +10.8 / POSCO unavailable","trigger_outcome_label":"success_candidate_stage2","promote_to":"Stage2"}
{"trigger_id":"r4l15_steel_antidumping_T1","case_id":"r4_loop15_hyundai_posco_steel_antidumping","trigger_type":"Stage2-Actionable","trigger_date":"2025-02-20","evidence_available":"Korea imposes 27.91-38.02% tariff on Chinese steel plates; Chinese steel imports 49% of Korea steel imports","event_return_pct":"Hyundai Steel +5.8 / POSCO +3.9 / KOSPI -0.7","market_relative_return_pp":"6.5/4.6","trigger_outcome_label":"Stage2_promote_candidate","promote_to":"Stage2-Actionable"}
{"trigger_id":"r4l15_hyundai_steel_weak_T1","case_id":"r4_loop15_hyundai_steel_weak_demand","trigger_type":"4C-watch","trigger_date":"2024-06-21","evidence_available":"Rebar price expected -10%, net profit estimate cut 73% to 215B won, target cut 14%","entry_price_krw":29000,"event_return_pct":-1.2,"trigger_outcome_label":"failed_rerating_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r4l15_hyundai_steel_capex_T1","case_id":"r4_loop15_hyundai_steel_us_localization_capex","trigger_type":"false_positive_score","trigger_date":"2025-04-22","evidence_available":"U.S. plant funding unclear, 50% debt, stock lost 21.2% since announcement","event_return_pct":-21.2,"trigger_outcome_label":"false_positive_score","promote_to":"4C-watch"}
{"trigger_id":"r4l15_koreazinc_tender_T0","case_id":"r4_loop15_korea_zinc_control_premium","trigger_type":"4B-watch","trigger_date":"2024-09-13","evidence_available":"MBK/Young Poong tender offer 660,000 won, 19% premium; Korea Zinc +24%","event_return_pct":24,"trigger_outcome_label":"event_premium_4B_control_premium","promote_to":"4B-watch"}
{"trigger_id":"r4l15_koreazinc_refinery_T1","case_id":"r4_loop15_korea_zinc_us_critical_minerals_smelter","trigger_type":"Stage2_strategic_resource","trigger_date":"2025-12-15","evidence_available":"U.S.-backed $7.4B critical minerals refinery, antimony/germanium/gallium etc, shares +27%","event_return_pct":27,"trigger_outcome_label":"Stage2_with_4B_overlay","promote_to":"Stage2"}
{"trigger_id":"r4l15_koreazinc_refinery_T3","case_id":"r4_loop15_korea_zinc_us_critical_minerals_smelter","trigger_type":"4B-watch","trigger_date":"2025-12-16","evidence_available":"MBK/Young Poong seek injunction to block share issuance; shares -13%","event_return_pct":-13,"trigger_outcome_label":"4B_governance_dilution_overlay","promote_to":"4B-watch"}
{"trigger_id":"r4l15_copper_tcrc_T1","case_id":"r4_loop15_copper_tcrc_smelt_margin_watch","trigger_type":"4C-watch","trigger_date":"2025-10-15","evidence_available":"Japan/Spain/South Korea warn copper TC/RCs unsustainable, some Chinese smelters process for free/loss","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"thesis_break_watch","promote_to":"4C-watch"}
{"trigger_id":"r4l15_china_export_controls_T2","case_id":"r4_loop15_china_strategic_mineral_export_controls","trigger_type":"4C-watch_reference","trigger_date":"2025-02-04","evidence_available":"China controls tungsten, bismuth, indium, tellurium, molybdenum and proposes battery/lithium/gallium processing tech restrictions","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"strategic_materials_4C_reference","promote_to":"4C-watch"}
```

## data/sector_taxonomy/score_weight_profiles_round227_r4_loop15_v1.csv 초안

```csv
archetype,tariff_rate_and_import_share,china_dependency_reduction,non_china_capacity_quality_certification,spread_margin_visibility,raw_material_price_durability,tcrc_smelt_margin,strategic_resource_offtake_contract,funding_irr_capex_clarity,control_premium_separation,export_control_exposure,commodity_price_event_only_penalty,control_premium_as_operating_green_penalty,localization_capex_without_funding_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
GRAPHITE_TARIFF_STAGE2_ACTIONABLE,+5,+5,+5,+3,+3,+0,+3,+2,+1,+5,-4,-2,-2,tariff+China dependency+relative strength,capacity/quality/customer gate pending,customer award+margin+capacity,POSCO Future M graphite tariff is Stage2-Actionable.
LITHIUM_PRICE_EVENT_PREMIUM,+1,+2,+1,+3,+5,+0,+1,+1,+1,+2,-5,-1,-1,lithium supply shock price move,durable price/margin pending,ASP pass-through+inventory draw, CATL mine suspension remains event premium.
UPSTREAM_LITHIUM_SUPPLY_SECURITY_STAGE2,+1,+4,+2,+3,+5,+0,+4,+3,+1,+3,-3,-1,-2,upstream stake/offtake rights,cost advantage pending,downstream margin confirmed,POSCO/MinRes is supply security Stage2.
STEEL_ANTIDUMPING_SPREAD_STAGE2_ACTIONABLE,+5,+2,+1,+5,+3,+0,+0,+1,+0,+2,-3,-1,-1,tariff+import share+relative strength,ASP/utilization pending,spread margin confirmed,Hyundai/POSCO anti-dumping is Stage2-Actionable.
STEEL_WEAK_DEMAND_FAILED_RERATING,+1,+1,+0,+5,+3,+0,+0,+1,+0,+1,-1,-1,-1,price/profit estimate cut,demand recovery pending,ASP/volume/margin recovery,Hyundai Steel weak demand is 4C-watch.
LOCALIZATION_CAPEX_FALSE_POSITIVE,+1,+2,+1,+3,+2,+0,+2,+5,+1,+2,-2,-1,-5,capex headline,IRR/funding/customer demand pending,firm funding+IRR+offtake,Hyundai Steel U.S. plant is false positive.
KOREA_ZINC_CONTROL_PREMIUM_4B,+1,+2,+1,+3,+3,+3,+2,+3,+5,+4,-2,-5,-2,tender/control premium,operating cashflow missing,margin/FCF confirmed,Korea Zinc tender is 4B not Green.
CRITICAL_MINERALS_SMELTER_STAGE2_WITH_DILUTION_4B,+2,+5,+3,+4,+4,+3,+5,+5,+5,+5,-2,-4,-4,strategic resource capex+U.S. backing,funding/governance/offtake pending,commercial operation+offtake+FCF,Korea Zinc refinery needs 4B overlay.
COPPER_TCRC_SPREAD_4C_WATCH,+0,+1,+0,+5,+5,+5,+1,+1,+1,+3,-4,-1,-1,copper price vs TC/RC spread,smelter margin pending,TC/RC normalization+margin,Copper price rally can be bad for smelters if TC/RC collapses.
CHINA_STRATEGIC_MINERAL_EXPORT_CONTROL_4C,+1,+5,+4,+3,+4,+1,+4,+2,+1,+5,-2,-1,-1,export controls on strategic materials,license/sourcing uncertainty,alternative supply/customer certification,Always overlay export-control exposure in R4.
```

---

# 이번 R4 Loop 15 결론

```text
1. POSCO Future M graphite tariff는 Stage2-Actionable이다.
   +20% event는 강하지만 non-China capacity, quality, customer certification 전에는 Green이 아니다.

2. CATL lithium mine suspension은 event premium이다.
   POSCO Future M +8.3%, L&F +10%였지만 CATL은 no material impact라고 했고, Reuters는 speculative excess를 경고했다.

3. POSCO/MinRes lithium JV는 supply-security Stage2다.
   upstream exposure는 좋지만 lithium price와 downstream margin이 닫혀야 한다.

4. Hyundai Steel/POSCO anti-dumping은 Stage2-Actionable이다.
   tariff rate, import share, relative strength가 있어 plain Stage2보다 강하다.

5. Hyundai Steel weak demand는 4C-watch다.
   rebar price -10%, net-profit estimate -73%는 소재 spread가 깨진 신호다.

6. Hyundai Steel U.S. plant는 false positive다.
   localization capex는 funding/IRR/customer demand 없이 Green이 아니다.

7. Korea Zinc tender battle은 control-premium 4B다.
   세계 최대 zinc smelter라 해도 tender premium은 operating cashflow와 분리해야 한다.

8. Korea Zinc U.S. critical minerals refinery는 Stage2 + 4B overlay다.
   전략자원 capex는 강하지만 share issuance/governance/funding/offtake가 남아 있다.

9. Copper TC/RC squeeze는 4C-watch다.
   copper price가 record여도 smelter processing margin이 무너지면 소재주 score는 다르게 봐야 한다.

10. China strategic mineral export controls는 R4 전역의 4C overlay다.
   graphite, antimony, gallium, germanium, rare earth, tungsten 등은 모든 Stage3 후보에 공급망 risk로 붙인다.
```

한 문장으로 압축하면:

> **R4 Loop 15에서 배운 핵심은 “원자재 가격이 올랐다”가 아니라, tariff·import share·China dependency reduction·spread margin·TC/RC·funding/IRR·offtake가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 commodity event, control premium, localization capex headline은 4B/false positive로 쉽게 변한다.**

[1]: https://www.ft.com/content/d76f744c-cc19-4aaf-9aa5-69c7b92e2cc4 "https://www.ft.com/content/d76f744c-cc19-4aaf-9aa5-69c7b92e2cc4"
[2]: https://www.reuters.com/markets/commodities/lithiums-rally-is-super-charged-with-speculative-spice-2025-08-18/ "https://www.reuters.com/markets/commodities/lithiums-rally-is-super-charged-with-speculative-spice-2025-08-18/"
[3]: https://www.reuters.com/business/energy/australias-minres-sell-30-lithium-jv-stake-posco-765-mln-2025-11-11/ "https://www.reuters.com/business/energy/australias-minres-sell-30-lithium-jv-stake-posco-765-mln-2025-11-11/"
[4]: https://www.reuters.com/markets/asia/south-korea-provisionally-slaps-tariffs-chinese-steel-plates-dumping-2025-02-20/ "https://www.reuters.com/markets/asia/south-korea-provisionally-slaps-tariffs-chinese-steel-plates-dumping-2025-02-20/"
[5]: https://www.marketwatch.com/story/hyundai-steel-s-2024-earnings-could-be-hit-by-weak-demand-market-talk-bcbe77c8 "https://www.marketwatch.com/story/hyundai-steel-s-2024-earnings-could-be-hit-by-weak-demand-market-talk-bcbe77c8"
[6]: https://www.reuters.com/markets/commodities/hyundai-steel-build-plant-louisiana-with-annual-output-27-million-tonnes-2025-03-25/ "https://www.reuters.com/markets/commodities/hyundai-steel-build-plant-louisiana-with-annual-output-27-million-tonnes-2025-03-25/"
[7]: https://www.wsj.com/world/asia/korea-zinc-shares-hit-record-high-after-mbks-1-5-billion-tender-offer-ff915b9b "https://www.wsj.com/world/asia/korea-zinc-shares-hit-record-high-after-mbks-1-5-billion-tender-offer-ff915b9b"
[8]: https://www.ft.com/content/d885ab55-b4f8-4c8f-a213-94f2778863ac "https://www.ft.com/content/d885ab55-b4f8-4c8f-a213-94f2778863ac"
[9]: https://www.reuters.com/world/asia-pacific/japan-spain-south-korea-warn-over-unsustainable-copper-processing-fees-2025-10-15/ "https://www.reuters.com/world/asia-pacific/japan-spain-south-korea-warn-over-unsustainable-copper-processing-fees-2025-10-15/"
[10]: https://www.reuters.com/markets/commodities/chinas-curbs-exports-strategic-minerals-2024-08-15/ "https://www.reuters.com/markets/commodities/chinas-curbs-exports-strategic-minerals-2024-08-15/"
