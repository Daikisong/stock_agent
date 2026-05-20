순서상 이번은 **R4 Loop 16 — 소재·스프레드·전략자원 trigger-level price validation 라운드**다.

이번 R4의 핵심은 “원자재 가격이 올랐다 / 전략자원 중요하다 / 구조조정한다”가 아니라, **원자재 가격 → 스프레드 → 회사 마진**, **전략자원 투자 → 실제 offtake / 수요 / capex ROI**, **보호무역 → 국내 spread 개선 또는 수출마진 훼손**, **지배구조·희석·규제 → 4B/4C**를 분리하는 것이다.

```text
round = R4 Loop 16
round_id = round_240
large_sector = MATERIALS_SPREAD_STRATEGIC_RESOURCES
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R5 Loop 16
```

이번에도 full adjusted OHLC 30D/90D/180D/1Y/2Y window는 안정적으로 확보하지 못했다. 그래서 full MFE/MAE는 만들지 않고 `price_data_unavailable_after_deep_search`로 분리한다. 대신 Reuters/WSJ/FT/Barron’s/MarketWatch의 **reported event return, event price, contract value, capacity, loss, tariff rate, spread condition**을 trigger anchor로 사용한다. 숫자를 만들지 않고, Stage 판정과 OHLC backfill 상태를 분리한다.

---

# 1. 이번 라운드 대섹터

```text
R4 = 소재·스프레드·전략자원
```

R4의 core gate는 아래다.

```text
철강:
관세 / 반덤핑 → ASP 방어 → 원재료 비용 → 수출마진 → domestic spread → capex ROI

석유화학:
naphtha spread → oversupply → capacity cut → 구조조정 → operating loss 축소 → margin recovery

리튬·배터리 소재:
lithium price → cathode/anode ASP → inventory write-down reversal → offtake → margin

전략광물:
critical minerals refinery / smelter → government funding → share issuance/dilution → offtake demand → governance risk

구리:
copper price → product ASP / cable demand → smelter TC/RC → refining margin → inventory / supply squeeze

소재 M&A / JV:
asset acquisition → resource security → offtake → balance sheet → minority stake economics → price confirmation

4B / 4C:
dilution, control battle, export tariff, anti-dumping reversal, oversupply, regulatory investigation, mine restart risk
```

---

# 2. 대상 canonical archetype

```text
STEEL_TARIFF_4C_AND_ANTIDUMPING_RELIEF
STEEL_US_LOCALIZATION_CAPEX_4B
PETROCHEMICAL_OVER_SUPPLY_FAILED_RERATING
PETROCHEMICAL_CAPACITY_RESTRUCTURING_STAGE2_RELIEF
CRITICAL_MINERALS_REFINERY_STAGE2_WITH_DILUTION_4B
LITHIUM_MINE_JV_STRATEGIC_RESOURCE_STAGE2
LITHIUM_PRICE_BETA_CYCLICAL_STAGE2
COPPER_TC_RC_SPREAD_4C_WATCH
SODIUM_ION_MATERIAL_OPTIONALITY_STAGE2
```

---

# 3. deep sub-archetype

```text
Hyundai Steel / POSCO Holdings:
- U.S. 25% steel/aluminum tariff shock
- POSCO Holdings -3.6% to 230,500 won
- Hyundai Steel -2.9% record low
- KOSPI -0.5%
- Korea provisional anti-dumping duties on Chinese steel plates 27.91~38.02%
- Hyundai Steel +5.8%, POSCO Holdings +3.9%, KOSPI -0.7%
- Hyundai Steel Louisiana plant $5.8B / 2.7M tonnes, intraday +5% then -4.4%

Lotte Chemical / LG Chem:
- 2024 petrochemical losses from oversupply
- Lotte Chemical operating loss 895B won, +157% YoY, biggest since 2011
- LG Chem OP -63.75% YoY to 916.8B won, lowest since 2019
- LG Chem petrochemical division Q4 loss 99B won
- global glut from China/Middle East capacity

Lotte Chemical / HD Hyundai Chemical:
- restructuring plan filed
- Lotte Daesan 1.1M ton naphtha-cracking capacity
- HD Hyundai Chemical 850k ton capacity
- government wants up to 25% annual capacity cut
- target cut up to 3.7M metric tons per year

Korea Zinc:
- U.S. Tennessee critical minerals refinery $7.4B
- $1.9B new shares to U.S. government-led JV
- JV to own around 10%
- Korea Zinc -13% after injunction news
- court rejection later: Korea Zinc up as much as 5%, YoungPoong down 10.5%
- strategic resource positive + dilution/control 4B

POSCO / Mineral Resources:
- POSCO buys 30% stake in part of MinRes lithium business for $765M
- gives POSCO indirect 15% stakes in Wodgina and Mt Marion
- MinRes +10.8%
- spodumene around $880/t after low near $610/t, far below 2022 >$6,000/t
- strategic resource entry at downcycle, but POSCO price anchor unavailable

CATL Yichun lithium:
- mine suspension after license expiry
- lithium carbonate futures +8%
- POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%
- lithium prices down up to 90% from 2022 peak
- cyclical lithium beta, not structural margin guarantee

Copper TC/RC:
- Japan, Spain, South Korea warn copper treatment/refining charges unsustainable
- tight concentrate supply and Chinese smelting capacity expansion
- Chinese smelters processing at zero or loss
- smelter margin 4C-watch even if copper price rises

LG Chem / Sinopec sodium-ion:
- sodium-ion material JV/partnership
- China sodium-ion market expected 10GWh 2025 → 292GWh 2034
- Stage2 optionality, but commercialization/revenue missing
```

---

# 4. 선정 case 요약

| bucket                     | case                                               | 핵심 판정                                                                                |
| -------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------ |
| 4C-watch + Stage2 relief   | Hyundai Steel / POSCO steel tariff vs anti-dumping | U.S. tariff는 4C, 중국산 후판 반덤핑은 domestic spread relief                                  |
| 4B / evidence-price failed | Hyundai Steel Louisiana plant                      | $5.8B capex, 2.7M tonnes, 장중 +5% 후 -4.4%. capex ROI 미확인                              |
| failed_rerating            | Lotte Chemical / LG Chem petrochemical oversupply  | Lotte 895B won OP loss, LG Chem OP -63.75%. spread 구조 악화                             |
| Stage2 relief              | Lotte + HD Hyundai petrochemical restructuring     | capacity cut policy는 relief지만, margin recovery 전 Green 금지                            |
| Stage2 + 4B/4C             | Korea Zinc critical minerals refinery              | $7.4B 전략광물 refinery, $1.9B share sale, governance/dilution overlay                   |
| Stage2 strategic resource  | POSCO / MinRes lithium JV                          | $765M lithium mine stake, offtake security, downcycle entry. POSCO price unavailable |
| cyclical Stage2            | CATL Yichun lithium suspension                     | POSCO Future M +8.3%, L&F +10%. lithium beta, structural margin 아님                   |
| 4C-watch                   | copper TC/RC compression                           | copper price 강세와 별개로 smelter processing spread 악화                                    |
| Stage2 optionality         | LG Chem / Sinopec sodium-ion                       | 차세대 소재 옵션, but commercialization/revenue 전 Green 금지                                  |

---

# 5. Case별 trigger grid

## Case A — Hyundai Steel / POSCO: U.S. tariff shock vs Korea anti-dumping relief

```text
symbols = 004020 / 005490
case_type = 4C-watch + Stage2 policy relief
archetype = STEEL_TARIFF_4C_AND_ANTIDUMPING_RELIEF
```

| trigger |          type | date       | 당시 공개 evidence                                                                                 | 가격 anchor                                                    | outcome                |
| ------- | ------------: | ---------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------------- |
| T0      |      4C-watch | 2025-02-10 | Trump says new 25% tariffs on all U.S. steel/aluminum imports                                  | POSCO -3.6% to 230,500 won, Hyundai Steel -2.9%, KOSPI -0.5% | export-margin 4C       |
| T1      | Stage2 relief | 2025-02-20 | Korea provisionally recommends 27.91~38.02% anti-dumping duties on Chinese steel plate imports | Hyundai Steel +5.8%, POSCO Holdings +3.9%, KOSPI -0.7%       | domestic spread relief |
| T2      |      4B-watch | 2025~      | U.S. tariff hurts export profitability; domestic anti-dumping helps local ASP                  | mixed                                                        | mixed spread           |
| T3      | Stage3-Yellow | N/A        | actual ASP, import volume decline, margin recovery not confirmed                               | N/A                                                          | no Yellow              |
| T4      |  Stage3-Green | N/A        | full OHLC + margin conversion unavailable                                                      | N/A                                                          | no Green               |

철강은 R4에서 한 방향으로 보면 안 된다. 2025년 2월 10일 U.S. 25% steel/aluminum tariff 뉴스에는 POSCO Holdings가 장중 -3.6%로 230,500원까지 밀렸고, Hyundai Steel은 -2.9%로 record low를 찍었으며 KOSPI는 -0.5%였다. 이건 수출마진 4C-watch다. 반대로 2월 20일 한국 정부가 중국산 후판에 27.91~38.02% provisional anti-dumping duties를 권고하자 Hyundai Steel +5.8%, POSCO Holdings +3.9%, KOSPI -0.7%였다. 이건 domestic spread relief다. 두 trigger를 같은 점수로 섞으면 안 된다. ([Reuters][1])

```json
{
  "case_id": "r4_loop16_hyundai_steel_posco_tariff_antidumping",
  "symbols": "004020/005490",
  "best_trigger": "T0/T1",
  "best_trigger_type": "4C_tariff_shock_plus_Stage2_antidumping_relief",
  "us_tariff_date": "2025-02-10",
  "us_steel_aluminum_tariff_pct": 25,
  "posco_tariff_event_return_pct": -3.6,
  "posco_tariff_event_price_krw": 230500,
  "hyundai_steel_tariff_event_return_pct": -2.9,
  "kospi_tariff_context_pct": -0.5,
  "korea_antidumping_date": "2025-02-20",
  "china_steel_plate_antidumping_rate_pct": "27.91-38.02",
  "hyundai_steel_antidumping_event_return_pct": 5.8,
  "posco_antidumping_event_return_pct": 3.9,
  "kospi_antidumping_context_pct": -0.7,
  "china_steel_import_value_2024_usd_bn": 10.4,
  "china_share_of_korea_steel_imports_pct": 49,
  "stage3_gate_missing": [
    "domestic_ASP_recovery",
    "import_volume_reduction",
    "export_margin_absorption",
    "raw_material_cost_pass_through",
    "quarterly_steel_spread"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "mixed_tariff_4C_and_antidumping_relief"
}
```

---

## Case B — Hyundai Steel / Louisiana U.S. plant capex

```text
symbol = 004020
case_type = 4B capex / evidence-price failed
archetype = STEEL_US_LOCALIZATION_CAPEX_4B
```

| trigger |            type | date       | 당시 공개 evidence                                                            | 가격 anchor                      | outcome                                |
| ------- | --------------: | ---------- | ------------------------------------------------------------------------- | ------------------------------ | -------------------------------------- |
| T0      | Stage2 evidence | 2025-03-25 | Hyundai Steel to build $5.8B Louisiana plant, 2.7M tonnes annual capacity | initially +5%, later -4.4%     | price reversal                         |
| T1      |        4B-watch | 2025-03-25 | part of Hyundai Motor Group’s $21B U.S. investment plan                   | Hyundai Motor +7.5%, Kia +4.3% | supplier/captive benefit, capex burden |
| T2      |   Stage3-Yellow | N/A        | plant margin, utilization, capex ROI, tariff savings not confirmed        | N/A                            | no Yellow                              |
| T3      |    Stage3-Green | N/A        | actual production/cash return unavailable                                 | N/A                            | no Green                               |

Hyundai Steel Louisiana plant는 “현지화 capex = 무조건 호재”가 아님을 보여준다. $5.8B 투자와 2.7M tonnes capacity는 전략적으로 크지만, 주가는 처음 +5% 이상 올랐다가 같은 session에서 -4.4%로 뒤집혔다. 현대차와 기아는 sourcing benefit 기대에 각각 +7.5%, +4.3% 올랐지만, Hyundai Steel equity에는 capex burden과 ROI gate가 더 크게 보였다. ([Reuters][2])

```json
{
  "case_id": "r4_loop16_hyundai_steel_louisiana_capex",
  "symbol": "004020",
  "best_trigger": "T0/T1",
  "best_trigger_type": "Stage2_capex_with_4B_ROI_gate",
  "trigger_date": "2025-03-25",
  "plant_investment_usd_bn": 5.8,
  "annual_capacity_mn_tons": 2.7,
  "initial_event_return_pct": 5,
  "late_session_event_return_pct": -4.4,
  "hyundai_motor_event_return_pct": 7.5,
  "kia_event_return_pct": 4.3,
  "hyundai_group_us_investment_usd_bn": 21,
  "stage3_gate_missing": [
    "plant_completion",
    "utilization",
    "tariff_savings",
    "capex_ROI",
    "steel_margin",
    "customer_offtake_terms"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "capex_localization_price_reversal_4B"
}
```

---

## Case C — LG Chem / Lotte Chemical petrochemical oversupply

```text
symbols = 051910 / 011170
case_type = failed_rerating / spread 4C
archetype = PETROCHEMICAL_OVER_SUPPLY_FAILED_RERATING
```

| trigger |          type | date                | 당시 공개 evidence                                                                         | 가격 anchor                | outcome        |
| ------- | ------------: | ------------------- | -------------------------------------------------------------------------------------- | ------------------------ | -------------- |
| T0      |   4C evidence | 2025-02-07          | 2024 petrochemical losses deepen due China/Middle East oversupply                      | no event price in source | failed spread  |
| T1      |    validation | 2025-02-07          | Lotte Chemical OP loss 895B won, +157% YoY; biggest operating loss since 2011          | no price                 | 4C             |
| T2      |    validation | 2025-02-07          | LG Chem OP -63.75% YoY to 916.8B won, lowest since 2019; petrochemical Q4 loss 99B won | no price                 | 4C             |
| T3      | Stage2 relief | later restructuring | capacity-cut policy needed                                                             | N/A                      | relief pending |
| T4      | Stage3-Yellow | N/A                 | naphtha spread recovery / China demand / capacity cuts not confirmed                   | N/A                      | no Yellow      |

석유화학은 R4의 failed-rerating template다. Lotte Chemical은 2024년 operating loss가 895B won으로 전년 대비 약 157% 확대됐고, 2011년 이후 최대 영업손실이었다. LG Chem은 2024년 operating profit이 전년 대비 63.75% 감소한 916.8B won으로 2019년 이후 최저였고, petrochemical division은 Q4에 99B won 손실을 냈다. 두 회사 모두 China/Middle East capacity expansion과 Northeast Asia oversupply를 핵심 원인으로 제시했다. ([Reuters][3])

```json
{
  "case_id": "r4_loop16_lgchem_lotte_petrochemical_oversupply",
  "symbols": "051910/011170",
  "best_trigger": "T0/T2",
  "best_trigger_type": "4C_watch_failed_spread",
  "trigger_date": "2025-02-07",
  "lotte_chemical_2024_op_loss_krw_bn": 895,
  "lotte_chemical_op_loss_yoy_pct": 157,
  "lotte_loss_context": "largest_operating_loss_since_2011",
  "lg_chem_2024_op_krw_bn": 916.8,
  "lg_chem_op_yoy_pct": -63.75,
  "lg_chem_op_context": "lowest_since_2019",
  "lg_chem_petrochemical_q4_loss_krw_bn": 99,
  "oversupply_sources": [
    "China_capacity",
    "Middle_East_capacity",
    "weak_China_recovery",
    "global_trade_uncertainty"
  ],
  "direct_event_price_anchor": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "failed_rerating_spread_4C_watch"
}
```

---

## Case D — Lotte Chemical / HD Hyundai Chemical petrochemical restructuring

```text
symbols = 011170 / HD_Hyundai_Chemical_readthrough
case_type = Stage2 restructuring relief
archetype = PETROCHEMICAL_CAPACITY_RESTRUCTURING_STAGE2_RELIEF
```

| trigger |          type | date       | 당시 공개 evidence                                                                                | 가격 anchor       | outcome                  |
| ------- | ------------: | ---------- | --------------------------------------------------------------------------------------------- | --------------- | ------------------------ |
| T0      | Stage2 relief | 2025-11-26 | Lotte to spin off Daesan and merge with HD Hyundai Chemical                                   | no price anchor | relief                   |
| T1      |    validation | 2025-11-26 | government pushes petrochemical firms to cut up to 25% annual capacity                        | no price        | policy support           |
| T2      |    validation | 2025-11-26 | target capacity cut up to 3.7M metric tons/year; Lotte Daesan 1.1M tons, HD Hyundai 850k tons | no price        | capacity rationalization |
| T3      |      4B-watch | 2025~      | facility adjustment and legal/tax support not finalized                                       | N/A             | execution gate           |
| T4      | Stage3-Yellow | N/A        | actual shutdown, spread improvement, loss reduction not confirmed                             | N/A             | no Yellow                |

구조조정은 Stage2 relief다. Lotte는 Daesan business를 spin off한 뒤 HD Hyundai Chemical과 합병해 naphtha-cracking oversupply를 완화하려고 한다. 정부는 2025년 8월부터 석유화학 업계에 annual capacity 최대 25% 감축을 요구했고, 목표는 naphtha-cracking capacity를 연간 최대 3.7M metric tons 줄이는 것이다. Lotte Daesan은 1.1M ton, HD Hyundai Chemical은 850k ton capacity다. 다만 실제 facility closure, tax/legal support, spread improvement가 나오기 전에는 Stage3가 아니다. ([Reuters][4])

```json
{
  "case_id": "r4_loop16_lotte_hdhyundai_petrochemical_restructuring",
  "symbols": "011170/HD_Hyundai_Chemical_readthrough",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_restructuring_relief",
  "trigger_date": "2025-11-26",
  "lotte_daesan_capacity_mn_tons": 1.1,
  "hd_hyundai_chemical_capacity_mn_tons": 0.85,
  "government_capacity_cut_target_pct": 25,
  "national_capacity_cut_target_mn_tons_per_year": 3.7,
  "restructuring_mechanism": [
    "Lotte_Daesan_spinoff",
    "merge_with_HD_Hyundai_Chemical",
    "facility_adjustment",
    "tax_and_legal_support_review"
  ],
  "direct_event_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "actual_capacity_shutdown",
    "naphtha_spread_recovery",
    "operating_loss_reduction",
    "tax_support_confirmed",
    "legal_support_confirmed"
  ],
  "trigger_outcome_label": "Stage2_relief_not_Green"
}
```

---

## Case E — Korea Zinc / U.S. critical minerals refinery

```text
symbols = 010130 / 000670
case_type = Stage2 strategic resource + dilution/governance 4B
archetype = CRITICAL_MINERALS_REFINERY_STAGE2_WITH_DILUTION_4B
```

| trigger |              type | date          | 당시 공개 evidence                                                                                | 가격 anchor                             | outcome                |
| ------- | ----------------: | ------------- | --------------------------------------------------------------------------------------------- | ------------------------------------- | ---------------------- |
| T0      |   Stage2 evidence | 2025-12-15/16 | Korea Zinc announces $7.4B Tennessee critical minerals refinery, funded largely by Washington | Korea Zinc -13% after injunction news | Stage2 + governance 4B |
| T1      |       4B/dilution | 2025-12       | $1.9B new shares to U.S. government-led JV, around 10% stake                                  | same                                  | dilution/control       |
| T2      | relief validation | 2025-12-24    | court rejects injunction; Korea Zinc up as much as 5%, YoungPoong down 10.5%                  | +5%, -10.5%                           | relief                 |
| T3      |     Stage3-Yellow | N/A           | offtake, refinery economics, dilution terms, governance settlement not confirmed              | N/A                                   | no Yellow              |

Korea Zinc는 R4 전략광물의 상징적인 case다. $7.4B Tennessee critical minerals refinery는 U.S.-Korea supply-chain restructuring과 China dependence reduction이라는 명확한 Stage2 strategic resource trigger다. 그러나 $1.9B 신주 발행으로 U.S. government-led JV가 약 10% stake를 갖는 구조라, dilution과 control battle overlay가 붙는다. MBK/YoungPoong의 injunction 소식에는 Korea Zinc가 -13% 급락했고, 이후 법원이 injunction을 기각하자 Korea Zinc는 최대 +5%, YoungPoong은 최대 -10.5% 하락했다. 즉 `strategic resource positive + governance/dilution 4B`다. ([Reuters][5])

```json
{
  "case_id": "r4_loop16_korea_zinc_tennessee_critical_minerals",
  "symbols": "010130/000670",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_strategic_resource_with_dilution_4B",
  "refinery_project_value_usd_bn": 7.4,
  "new_share_sale_value_usd_bn": 1.9,
  "us_government_led_jv_stake_pct": 10,
  "injunction_news_event_return_pct": -13,
  "court_rejection_date": "2025-12-24",
  "korea_zinc_relief_event_return_pct": 5,
  "young_poong_relief_event_return_pct": -10.5,
  "strategic_rationale": [
    "critical_minerals_supply_chain",
    "US_Korea_cooperation",
    "reduce_reliance_on_China",
    "chips_electronics_weapons_materials"
  ],
  "4B_overlay": [
    "dilution",
    "control_battle",
    "fairness_of_terms",
    "board_process",
    "governance_risk"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_strategic_resource_with_governance_4B"
}
```

---

## Case F — POSCO / Mineral Resources lithium mine JV

```text
symbol = 005490
case_type = Stage2 strategic resource / downcycle acquisition
archetype = LITHIUM_MINE_JV_STRATEGIC_RESOURCE_STAGE2
```

| trigger |            type | date       | 당시 공개 evidence                                                                                                | 가격 anchor                              | outcome          |
| ------- | --------------: | ---------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ---------------- |
| T0      | Stage2 evidence | 2025-11-11 | POSCO to buy 30% stake in part of MinRes lithium business for $765M                                           | MinRes +10.8%, POSCO price unavailable | Stage2           |
| T1      |      validation | 2025-11-11 | JV gives POSCO indirect 15% interest in Wodgina and Mt Marion mines                                           | same                                   | strategic supply |
| T2      |        4B-watch | 2025       | lithium prices still far below 2022 peak; spodumene around $880/t after low near $610/t, vs >$6,000/t in 2022 | no POSCO price                         | cycle risk       |
| T3      |   Stage3-Yellow | N/A        | offtake margin, lithium hydroxide economics, POSCO balance-sheet impact not confirmed                         | N/A                                    | no Yellow        |

POSCO-MinRes lithium JV는 “좋은 strategic resource entry이지만 downcycle 4B를 붙여야 하는” case다. POSCO는 MinRes lithium business 일부의 30% stake를 $765M에 취득해 Wodgina와 Mt Marion lithium mines에 각각 indirect 15% interest를 갖게 된다. MinRes 주가는 +10.8% 올랐지만, POSCO의 직접 가격 anchor는 확보하지 못했다. Reuters는 spodumene price가 mid-June low $610/t에서 August 약 $880/t로 반등했지만, 2022 peak $6,000/t 이상과 비교하면 여전히 크게 낮다고 보도했다. 즉 Stage2 strategic resource지만, lithium downcycle과 offtake economics가 gate다. ([Reuters][6])

```json
{
  "case_id": "r4_loop16_posco_minres_lithium_jv",
  "symbol": "005490",
  "best_trigger": "T0/T1",
  "best_trigger_type": "Stage2_strategic_resource_downcycle",
  "trigger_date": "2025-11-11",
  "transaction_value_usd_mn": 765,
  "stake_in_minres_lithium_business_pct": 30,
  "indirect_stake_wodgina_pct": 15,
  "indirect_stake_mt_marion_pct": 15,
  "minres_event_return_pct": 10.8,
  "posco_direct_price_anchor": "price_data_unavailable_after_deep_search",
  "spodumene_mid_june_low_usd_per_ton": 610,
  "spodumene_august_rebound_usd_per_ton": 880,
  "spodumene_2022_peak_usd_per_ton": ">6000",
  "stage3_gate_missing": [
    "POSCO_offtake_terms",
    "lithium_hydroxide_margin",
    "mine_cost_curve",
    "balance_sheet_impact",
    "battery_material_customer_demand"
  ],
  "trigger_outcome_label": "Stage2_strategic_resource_not_Green"
}
```

---

## Case G — CATL Yichun suspension / Korean lithium-material beta

```text
symbols = 003670 / 066970 / 006400 / 373220
case_type = cyclical Stage2 / event premium
archetype = LITHIUM_PRICE_BETA_CYCLICAL_STAGE2
```

| trigger |                    type | date       | 당시 공개 evidence                                                                   | 가격 anchor           | outcome         |
| ------- | ----------------------: | ---------- | -------------------------------------------------------------------------------- | ------------------- | --------------- |
| T0      |         Stage2 cyclical | 2025-08-11 | CATL suspends Yichun mine after license expiry                                   | lithium futures +8% | cyclical        |
| T1      | material-stock reaction | 2025-08-11 | POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%                    | strong event        | Stage2 cyclical |
| T2      |                4B-watch | 2025-09/10 | license renewal/restart risk; CATL later sourcing external ore while mine closed | no full OHLC        | 4B              |
| T3      |           Stage3-Yellow | N/A        | cathode ASP/margin and inventory reversal not confirmed                          | N/A                 | no Yellow       |

CATL Yichun mine suspension은 R4에서 “전략자원 가격 beta”를 calibrate하는 데 좋다. CATL의 license expiry로 Yichun mine이 중단되자 lithium carbonate futures는 +8% limit-up이었고, POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%가 나왔다. 그러나 CATL은 license renewal 시 재개할 수 있다고 했고, lithium price는 2022 peak 대비 최대 90% 하락한 뒤의 반등이었다. 따라서 이 trigger는 `cyclical Stage2 / event premium`이지 Green이 아니다. ([월스트리트저널][7])

```json
{
  "case_id": "r4_loop16_catl_yichun_korea_lithium_beta",
  "symbols": "003670/066970/006400/373220",
  "best_trigger": "T0/T1",
  "best_trigger_type": "cyclical_Stage2_event_premium",
  "trigger_date": "2025-08-11",
  "catl_mine": "Yichun_Jianxiawo",
  "license_expiry_date": "2025-08-09",
  "lithium_futures_event_return_pct": 8,
  "posco_future_m_event_return_pct": 8.3,
  "l_and_f_event_return_pct": 10,
  "samsung_sdi_event_return_pct": 3.2,
  "lges_event_return_pct": 2.8,
  "lithium_price_decline_from_2022_peak_pct": 90,
  "mine_capacity_lce_tons_per_year": 46000,
  "forecast_global_output_share_2025_pct": 3,
  "stage3_gate_missing": [
    "sustained_lithium_price_rebound",
    "cathode_ASP_pass_through",
    "inventory_write_down_reversal",
    "material_margin_recovery",
    "customer_order_recovery"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "cyclical_lithium_beta_not_Green"
}
```

---

## Case H — Copper TC/RC compression / smelter spread 4C

```text
symbols = copper_smelter_basket / 010130_readthrough / LS_MnM_private_readthrough
case_type = 4C-watch / spread compression
archetype = COPPER_TC_RC_SPREAD_4C_WATCH
```

| trigger |            type | date       | 당시 공개 evidence                                                                                    | 가격 anchor             | outcome           |
| ------- | --------------: | ---------- | ------------------------------------------------------------------------------------------------- | --------------------- | ----------------- |
| T0      |       awareness | 2025       | copper price strong due AI/grid/construction demand and mine disruptions                          | no Korean stock price | Stage1            |
| T1      | 4C spread watch | 2025-10-15 | Japan, Spain, South Korea warn copper TC/RCs unsustainable                                        | no KRX price          | smelter spread 4C |
| T2      |      validation | 2025-10-15 | tight concentrate supply + Chinese smelting expansion, some Chinese smelters process at zero/loss | no price              | margin pressure   |
| T3      |   Stage2 relief | N/A        | TC/RC recovery not confirmed                                                                      | N/A                   | no relief         |

구리는 R4에서 가장 중요한 “가격과 스프레드가 반대로 갈 수 있는” 소재다. copper price가 강하더라도 smelter가 돈을 버는 건 별개다. Japan, Spain, South Korea는 copper treatment/refining charges가 unsustainable하게 떨어졌다고 공동으로 우려를 표명했고, tight concentrate supply와 China smelting capacity expansion 때문에 smelter margin이 압박되고 있다. 일부 Chinese smelter는 Antofagasta 물량을 무상 또는 손실로 처리하기도 했다. 따라서 copper price bullish headline만으로 Korea Zinc/LS MnM/Poongsan류 소재 score를 올리면 false positive가 된다. ([Reuters][8])

```json
{
  "case_id": "r4_loop16_copper_tcrc_spread_watch",
  "symbols": "copper_smelter_basket/010130_readthrough/LS_MnM_private_readthrough",
  "best_trigger": "T1/T2",
  "best_trigger_type": "4C_watch_spread_compression",
  "trigger_date": "2025-10-15",
  "countries_warning": [
    "Japan",
    "Spain",
    "South_Korea"
  ],
  "issue": "copper_treatment_refining_charges_unsustainable",
  "drivers": [
    "tight_copper_concentrate_supply",
    "China_smelting_capacity_expansion",
    "smelters_processing_at_zero_or_loss",
    "negative_TC_RC_risk"
  ],
  "direct_krx_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "TC_RC_recovery",
    "smelter_margin_recovery",
    "concentrate_supply_contracts",
    "refined_copper_premium",
    "product_mix"
  ],
  "trigger_outcome_label": "copper_price_not_equal_smelter_margin"
}
```

---

## Case I — LG Chem / Sinopec sodium-ion battery materials

```text
symbol = 051910
case_type = Stage2 optionality
archetype = SODIUM_ION_MATERIAL_OPTIONALITY_STAGE2
```

| trigger |            type | date       | 당시 공개 evidence                                                                                   | 가격 anchor        | outcome            |
| ------- | --------------: | ---------- | ------------------------------------------------------------------------------------------------ | ---------------- | ------------------ |
| T0      | Stage2 evidence | 2025-11-04 | Sinopec and LG Chem sign agreement to develop sodium-ion battery materials                       | no LG Chem price | Stage2 optionality |
| T1      |      validation | 2025-11-04 | focus on ESS and low-speed EVs in China/global; sodium-ion China market 10GWh 2025 → 292GWh 2034 | no price         | future market      |
| T2      |        4B-watch | 2025~      | commercialization, customer contract, margin, China policy dependence missing                    | no OHLC          | 4B                 |
| T3      |   Stage3-Yellow | N/A        | actual revenue / customer adoption not confirmed                                                 | N/A              | no Yellow          |

LG Chem–Sinopec sodium-ion partnership는 R4 소재 optionality다. Sinopec과 LG Chem은 sodium-ion battery materials를 공동개발하기로 했고, target은 ESS와 low-speed EV다. Sinopec은 China sodium-ion market이 2025년 10GWh에서 2034년 292GWh로 성장할 수 있다고 제시했다. 다만 이건 commercialization 전의 Stage2 optionality일 뿐, customer contract·매출·margin이 없으면 Yellow가 아니다. ([Reuters][9])

```json
{
  "case_id": "r4_loop16_lgchem_sinopec_sodium_ion_materials",
  "symbol": "051910",
  "best_trigger": "T0/T1",
  "best_trigger_type": "Stage2_material_optionality",
  "trigger_date": "2025-11-04",
  "partner": "Sinopec",
  "technology": "sodium_ion_battery_materials",
  "target_markets": [
    "energy_storage_systems",
    "low_speed_EVs",
    "China",
    "global"
  ],
  "china_sodium_ion_market_2025_gwh": 10,
  "china_sodium_ion_market_2034_gwh": 292,
  "china_global_output_share_2030_pct": ">90",
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "commercialization_timeline",
    "customer_contract",
    "material_ASP",
    "gross_margin",
    "plant_capacity",
    "non_lithium_cost_advantage_validation"
  ],
  "trigger_outcome_label": "Stage2_optionality_not_Green"
}
```

---

# 6. Trigger별 가격경로 검증 요약

| case                           | best trigger |             entry anchor |                                            event MFE/MAE |          market-relative | full MFE/MAE | outcome                   |
| ------------------------------ | ------------ | -----------------------: | -------------------------------------------------------: | -----------------------: | ------------ | ------------------------- |
| Hyundai Steel/POSCO tariff     | T0/T1        | POSCO 230,500 tariff low | POSCO -3.6%, Hyundai Steel -2.9%; later +3.9/+5.8 relief |                    mixed | unavailable  | 4C + Stage2 relief        |
| Hyundai Steel Louisiana        | T0/T1        |                    event |                               initially +5%, later -4.4% | failed intraday reversal | unavailable  | capex 4B                  |
| LG Chem/Lotte oversupply       | T0/T2        |                 no price |                                           no event price |                      N/A | unavailable  | failed_rerating           |
| Lotte/HD Hyundai restructuring | T0/T2        |                 no price |                                           no event price |                      N/A | unavailable  | Stage2 relief             |
| Korea Zinc refinery            | T0/T2        |                    event |     -13% injunction, later +5% relief; YoungPoong -10.5% |                    mixed | unavailable  | Stage2 + 4B               |
| POSCO/MinRes lithium JV        | T0/T1        |             MinRes event |                         MinRes +10.8%, POSCO unavailable |                      N/A | unavailable  | Stage2 strategic resource |
| CATL lithium beta              | T0/T1        |                    event |    POSCO Future M +8.3%, L&F +10%, SDI +3.2%, LGES +2.8% |              unavailable | unavailable  | cyclical Stage2           |
| Copper TC/RC                   | T1/T2        |                 no price |                                          no Korean price |                      N/A | unavailable  | spread 4C-watch           |
| LG Chem/Sinopec sodium-ion     | T0/T1        |                 no price |                                          no Korean price |                      N/A | unavailable  | Stage2 optionality        |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
좋은 Stage2:
- Korea Zinc / U.S. critical minerals refinery
- POSCO / MinRes lithium JV
- LG Chem / Sinopec sodium-ion
- Lotte/HD Hyundai petrochemical restructuring

단, 이들은 모두 Green이 아니다.
- Korea Zinc는 dilution/governance 4B.
- POSCO lithium JV는 downcycle and offtake/margin gate.
- LG Chem sodium-ion은 commercialization gate.
- petrochemical restructuring은 actual capacity cut and spread recovery gate.
```

## Stage2-Actionable entry 성과

```text
강한 Actionable에 가까운 trigger:
- Hyundai Steel/POSCO anti-dumping relief: Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7%.
- CATL lithium beta: POSCO Future M +8.3%, L&F +10%.

하지만 둘 다 Green은 아니다.
- anti-dumping은 domestic spread recovery 확인 필요.
- lithium beta는 cathode margin 확인 필요.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Hyundai Steel/POSCO: anti-dumping 이후 ASP/margin 회복 확인 시.
- Lotte/HD Hyundai restructuring: actual shutdown and naphtha spread recovery 확인 시.
- Korea Zinc: refinery offtake and dilution/governance terms clear 시.
- POSCO lithium JV: offtake and lithium hydroxide margin 확인 시.
- LG Chem/Sinopec: sodium-ion material customer contract 확인 시.
```

## Stage3-Green

```text
이번 R4 Loop 16에서 확정 Green 없음.

이유:
- steel은 tariff와 anti-dumping이 상충한다.
- petrochemical은 아직 restructuring relief 단계다.
- lithium은 cyclical rebound and downcycle acquisition 단계다.
- Korea Zinc는 strategic resource와 dilution/governance가 같이 있다.
- copper는 price 상승과 smelter TC/RC margin이 반대로 갈 수 있다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Hyundai Steel/POSCO anti-dumping relief
- Korea Zinc injunction/court-relief sequence
- CATL lithium beta rally

Stage2_promote_candidate:
- Hyundai Steel/POSCO anti-dumping if domestic margin confirms
- Korea Zinc refinery if dilution/governance cleared
- POSCO MinRes lithium JV if offtake/margin visible
- Lotte/HD Hyundai restructuring if capacity cuts become real

evidence_good_but_price_failed_or_muted:
- Hyundai Steel Louisiana plant: +5% initial then -4.4% reversal
- POSCO MinRes lithium JV: strategic evidence good but POSCO price unavailable
- LG Chem/Sinopec: optionality good but price unavailable

cyclical_success:
- CATL Yichun lithium suspension / POSCO Future M / L&F rally

failed_rerating:
- Lotte Chemical / LG Chem petrochemical oversupply

event_premium:
- lithium mine suspension
- anti-dumping relief before actual spread recovery

thesis_break_watch:
- U.S. steel tariff shock
- petrochemical oversupply
- copper TC/RC compression
- Korea Zinc dilution/governance risk

hard_4C_success:
- 이번 R4에서는 confirmed hard 4C 없음
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
domestic_spread_recovery,+5,"anti-dumping은 실제 ASP/margin이 확인될 때 Stage2→Yellow","Hyundai Steel/POSCO"
tariff_exposure_absorption,+5,"U.S. tariff는 export spread 4C","POSCO/Hyundai Steel"
actual_capacity_cut,+5,"석화 구조조정은 shutdown/merger execution이 핵심","Lotte/HD Hyundai"
naphtha_spread_recovery,+5,"석화는 policy보다 spread가 이익을 결정","LG Chem/Lotte"
strategic_resource_offtake,+5,"전략광물 투자도 offtake/margin이 핵심","Korea Zinc/POSCO"
dilution_governance_overlay,+5,"전략자원 투자라도 신주발행·control battle이면 4B","Korea Zinc"
lithium_price_duration,+4,"일회성 mine suspension보다 가격 지속성이 중요","CATL/POSCO Future M/L&F"
smelter_TC_RC_margin,+5,"copper price와 smelter margin은 다르다","copper TC/RC case"
commercialization_contract,+4,"sodium-ion은 customer contract 전까지 Stage2","LG Chem/Sinopec"
```

## 내릴 축

```csv
axis,delta,reason,cases
commodity_price_headline_without_margin,-5,"가격상승만으로 소재주 Green 금지","CATL lithium, copper"
tariff_policy_without_spread_proof,-4,"관세/반덤핑은 실제 spread 확인 전 Stage2","steel"
strategic_resource_capex_without_offtake,-5,"전략자원 capex는 offtake 없으면 4B","Korea Zinc/POSCO"
restructuring_plan_without_shutdown,-5,"구조조정 계획은 capacity cut 전까지 relief","Lotte/HD Hyundai"
petrochemical_recovery_without_capacity_cut,-5,"중국 수요 회복 기대만으로 Green 금지","LG Chem/Lotte"
lithium_JV_without_price_anchor,-3,"상대방 주가만 오르면 POSCO Actionable 확정 보류","POSCO/MinRes"
copper_bull_without_TCRC,-5,"copper price bull은 smelter spread를 보장하지 않음","copper TC/RC"
```

---

# 10. Stage2-Actionable 승격 조건

R4 Loop 16 shadow rule:

```text
R4에서 Stage2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. 원자재 가격 또는 정책 변화가 company ASP/margin으로 연결된다.
2. event return이 +5% 이상이다.
3. market-relative return이 +5pp 이상이다.
4. supply restriction이 일회성이 아니라 duration을 가진다.
5. 전략광물 투자가 offtake, customer, government funding, margin으로 연결된다.
6. 구조조정이 실제 capacity shutdown 또는 merger execution으로 확인된다.
7. dilution/governance/export tariff/TC-RC squeeze 4B·4C overlay가 없다.
```

적용:

```text
Hyundai Steel anti-dumping:
event return은 좋지만 margin recovery 확인 전 Stage2 relief.

CATL lithium beta:
event return은 좋지만 cathode margin 확인 전 cyclical Stage2.

Korea Zinc:
strategic resource는 좋지만 dilution/governance 4B로 Actionable 제한.

POSCO MinRes:
strategic resource는 좋지만 POSCO price anchor and offtake margin missing.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
- Stage2-Actionable 이후 EPS/OP/FCF 경로 변화 가능성이 높아진 상태.
- 하지만 spread, margin, offtake, capacity cut, dilution risk 중 하나가 남은 상태.
```

Yellow 후보:

```text
Steel:
anti-dumping 이후 domestic ASP and spread recovery가 분기 실적에 보이면 Yellow.

Petrochemical:
actual NCC capacity reduction and naphtha spread recovery가 보이면 Yellow.

Korea Zinc:
critical minerals refinery offtake and dilution/governance resolution이 보이면 Yellow.

POSCO lithium:
mine stake → offtake → lithium hydroxide margin이 보이면 Yellow.

LG Chem sodium-ion:
customer contract and commercialization timeline이 보이면 Yellow.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- commodity price or policy change converts to gross margin and OP.
- strategic resource investment has clear offtake/customer demand.
- dilution/governance overhang is resolved or priced.
- restructuring results in real capacity cut and spread improvement.
- lithium/copper/steel spread is durable across quarters.
- full-window MFE/MAE is favorable.
```

이번 R4 Loop 16에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + spread/margin/offtake/dilution gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- strategic mineral investment requires large share issuance.
- commodity price spike has no margin confirmation.
- plant localization capex reverses price intraday.
- restructuring plan is announced but shutdown not executed.
- lithium mine suspension can be reversed by license renewal.
- copper price rises while TC/RC collapses.
```

적용:

```text
Korea Zinc:
critical minerals refinery + $1.9B share sale → 4B dilution/governance.

Hyundai Steel:
Louisiana capex + price reversal → 4B ROI risk.

CATL lithium:
license renewal risk → 4B cyclical event.

Petrochemical restructuring:
plan before shutdown → 4B execution risk.

Copper:
price bullish but TC/RC bearish → 4B/4C spread risk.
```

---

# 14. 4C hard gate 조건

```text
R4 4C:
- export tariff that destroys spread
- commodity spread collapse
- smelter TC/RC negative economics
- refinery/capex project funding through dilutive issuance under control battle
- petrochemical oversupply causing persistent operating losses
- strategic mine acquisition with no offtake and falling commodity price
- regulatory/prosecutor investigation into share issuance or governance
```

이번 R4 Loop 16 hard 4C 확정은 없다.

```text
hard_4c_not_confirmed = true
```

Strong 4C-watch:

```text
- LG Chem / Lotte petrochemical oversupply
- U.S. steel tariffs
- Korea Zinc governance/dilution
- copper TC/RC compression
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R4 production 설계 원칙:

```text
1. 원자재 가격과 회사 spread를 분리한다.
2. 전략자원 capex와 offtake/margin을 분리한다.
3. 구조조정 발표와 실제 capacity cut을 분리한다.
4. 반덤핑·관세는 domestic spread와 export spread를 반대로 계산한다.
5. lithium/copper beta는 cyclical label로 별도 처리한다.
6. dilution/governance는 strategic resource positive 위에 반드시 overlay한다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_240.md 요약

```md
# R4 Loop 16. Materials / Spread / Strategic Resources Trigger-level Price Validation

이번 라운드는 R4 Loop 16 trigger-level validation 라운드다.

핵심 결론:
- Hyundai Steel / POSCO show steel policy is mixed, not one-way. U.S. 25% steel/aluminum tariff shock sent POSCO Holdings -3.6% to 230,500 won and Hyundai Steel -2.9% while KOSPI -0.5%. Korea’s provisional anti-dumping duties of 27.91~38.02% on Chinese steel plates later sent Hyundai Steel +5.8%, POSCO Holdings +3.9% while KOSPI -0.7%. Tariff is 4C; anti-dumping is Stage2 spread relief.
- Hyundai Steel Louisiana capex is 4B. $5.8B plant with 2.7M tonnes capacity initially pushed shares up more than 5%, but shares reversed to -4.4%. Capex ROI and tariff savings are unconfirmed.
- LG Chem / Lotte Chemical petrochemical oversupply is failed rerating. Lotte Chemical 2024 OP loss deepened to 895B won, +157% YoY; LG Chem 2024 OP fell 63.75% YoY to 916.8B won and petrochemical Q4 loss was 99B won.
- Lotte / HD Hyundai petrochemical restructuring is Stage2 relief. Government pushed up to 25% annual capacity cut, targeting up to 3.7M tons/year. Actual shutdown and spread recovery are not confirmed.
- Korea Zinc Tennessee critical minerals refinery is Stage2 strategic resource with dilution/governance 4B. $7.4B refinery, $1.9B new share sale to U.S. government-led JV. Korea Zinc -13% after injunction news, then up to +5% after court rejected injunction; YoungPoong fell 10.5%.
- POSCO / MinRes lithium JV is Stage2 strategic resource. POSCO buys 30% stake in part of MinRes lithium business for $765M, giving indirect 15% stakes in Wodgina and Mt Marion. MinRes +10.8%, but POSCO price anchor and offtake economics are unavailable.
- CATL Yichun suspension is cyclical lithium beta. POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%. Lithium futures +8%, but license renewal and margin pass-through are missing.
- Copper TC/RC compression is 4C-watch. Japan, Spain and South Korea warned copper processing fees are unsustainable; copper price strength does not guarantee smelter margin.
- LG Chem / Sinopec sodium-ion is Stage2 optionality. China sodium-ion market could grow from 10GWh in 2025 to 292GWh in 2034, but commercialization and customer contracts are missing.

Main calibration:
- Raise domestic_spread_recovery, tariff_exposure_absorption, actual_capacity_cut, naphtha_spread_recovery, strategic_resource_offtake, dilution_governance_overlay, lithium_price_duration, smelter_TC_RC_margin, commercialization_contract.
- Lower commodity_price_headline_without_margin, tariff_policy_without_spread_proof, strategic_resource_capex_without_offtake, restructuring_plan_without_shutdown, petrochemical_recovery_without_capacity_cut, copper_bull_without_TCRC.
```

## docs/checkpoints/checkpoint_28a_round240_r4_loop16.md 요약

```md
# Checkpoint 28A Round 240 R4 Loop 16 Trigger-level Calibration

## 반영 내용
- R4 Loop 16 trigger-level validation을 수행했다.
- Hyundai Steel/POSCO tariff and anti-dumping, Hyundai Steel Louisiana capex, LG Chem/Lotte petrochemical oversupply, Lotte/HD Hyundai restructuring, Korea Zinc Tennessee refinery, POSCO/MinRes lithium JV, CATL lithium beta, copper TC/RC compression, LG Chem/Sinopec sodium-ion materials를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / WSJ / FT / Barron’s / MarketWatch의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- 원자재 가격과 회사 spread를 분리한다.
- 전략자원 투자는 offtake/margin 없이 Green 금지다.
- 관세와 반덤핑은 export spread와 domestic spread를 반대로 볼 수 있다.
- 석유화학 구조조정은 실제 capacity cut and spread recovery 전에는 Stage2 relief다.
- lithium price spike는 material margin 확인 전 cyclical event premium이다.
- copper price bull은 smelter TC/RC margin을 보장하지 않는다.
```

## data/e2r_case_library/cases_r4_loop16_round240.jsonl 초안

```jsonl
{"case_id":"r4_loop16_hyundai_steel_posco_tariff_antidumping","symbol":"004020/005490","company_name":"Hyundai Steel / POSCO Holdings","case_type":"mixed_tariff_4C_and_antidumping_relief","primary_archetype":"STEEL_TARIFF_4C_AND_ANTIDUMPING_RELIEF","best_trigger":"T0/T1","stage_candidate":"4C-watch + Stage2_relief","price_validation":{"us_tariff_date":"2025-02-10","us_steel_aluminum_tariff_pct":25,"posco_tariff_event_return_pct":-3.6,"posco_tariff_event_price_krw":230500,"hyundai_steel_tariff_event_return_pct":-2.9,"kospi_tariff_context_pct":-0.5,"korea_antidumping_date":"2025-02-20","china_steel_plate_antidumping_rate_pct":"27.91-38.02","hyundai_steel_antidumping_event_return_pct":5.8,"posco_antidumping_event_return_pct":3.9,"kospi_antidumping_context_pct":-0.7,"china_steel_import_value_2024_usd_bn":10.4,"china_share_of_korea_steel_imports_pct":49,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"mixed_tariff_4C_and_antidumping_relief","notes":"U.S. tariff hurts export spread; Korea anti-dumping supports domestic spread. Separate scoring required."}
{"case_id":"r4_loop16_hyundai_steel_louisiana_capex","symbol":"004020","company_name":"Hyundai Steel","case_type":"capex_localization_price_reversal_4B","primary_archetype":"STEEL_US_LOCALIZATION_CAPEX_4B","best_trigger":"T0/T1","stage_candidate":"Stage2_capex + 4B-watch","price_validation":{"trigger_date":"2025-03-25","plant_investment_usd_bn":5.8,"annual_capacity_mn_tons":2.7,"initial_event_return_pct":5,"late_session_event_return_pct":-4.4,"hyundai_motor_event_return_pct":7.5,"kia_event_return_pct":4.3,"hyundai_group_us_investment_usd_bn":21,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_failed_intraday","notes":"Localization capex is not Green before utilization, tariff savings and capex ROI."}
{"case_id":"r4_loop16_lgchem_lotte_petrochemical_oversupply","symbol":"051910/011170","company_name":"LG Chem / Lotte Chemical","case_type":"failed_rerating_spread_4C_watch","primary_archetype":"PETROCHEMICAL_OVER_SUPPLY_FAILED_RERATING","best_trigger":"T0/T2","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2025-02-07","lotte_chemical_2024_op_loss_krw_bn":895,"lotte_chemical_op_loss_yoy_pct":157,"lotte_loss_context":"largest_operating_loss_since_2011","lg_chem_2024_op_krw_bn":916.8,"lg_chem_op_yoy_pct":-63.75,"lg_chem_op_context":"lowest_since_2019","lg_chem_petrochemical_q4_loss_krw_bn":99,"direct_event_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"failed_rerating","notes":"Petrochemical oversupply and spread collapse are 4C-watch until capacity cut and spread recovery."}
{"case_id":"r4_loop16_lotte_hdhyundai_petrochemical_restructuring","symbol":"011170/HD_Hyundai_Chemical_readthrough","company_name":"Lotte Chemical / HD Hyundai Chemical","case_type":"Stage2_restructuring_relief","primary_archetype":"PETROCHEMICAL_CAPACITY_RESTRUCTURING_STAGE2_RELIEF","best_trigger":"T0/T2","stage_candidate":"Stage2_relief","price_validation":{"trigger_date":"2025-11-26","lotte_daesan_capacity_mn_tons":1.1,"hd_hyundai_chemical_capacity_mn_tons":0.85,"government_capacity_cut_target_pct":25,"national_capacity_cut_target_mn_tons_per_year":3.7,"direct_event_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_relief_not_Green","notes":"Restructuring plan needs actual shutdown, tax/legal support and spread recovery before Yellow."}
{"case_id":"r4_loop16_korea_zinc_tennessee_critical_minerals","symbol":"010130/000670","company_name":"Korea Zinc / YoungPoong","case_type":"Stage2_strategic_resource_with_governance_4B","primary_archetype":"CRITICAL_MINERALS_REFINERY_STAGE2_WITH_DILUTION_4B","best_trigger":"T0/T2","stage_candidate":"Stage2 + 4B-watch","price_validation":{"refinery_project_value_usd_bn":7.4,"new_share_sale_value_usd_bn":1.9,"us_government_led_jv_stake_pct":10,"injunction_news_event_return_pct":-13,"court_rejection_date":"2025-12-24","korea_zinc_relief_event_return_pct":5,"young_poong_relief_event_return_pct":-10.5,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_strategic_resource_with_governance_4B","notes":"Critical minerals refinery is strategic Stage2, but dilution/control battle must be overlaid."}
{"case_id":"r4_loop16_posco_minres_lithium_jv","symbol":"005490","company_name":"POSCO Holdings / Mineral Resources","case_type":"Stage2_strategic_resource_downcycle","primary_archetype":"LITHIUM_MINE_JV_STRATEGIC_RESOURCE_STAGE2","best_trigger":"T0/T1","stage_candidate":"Stage2","price_validation":{"trigger_date":"2025-11-11","transaction_value_usd_mn":765,"stake_in_minres_lithium_business_pct":30,"indirect_stake_wodgina_pct":15,"indirect_stake_mt_marion_pct":15,"minres_event_return_pct":10.8,"posco_direct_price_anchor":"price_data_unavailable_after_deep_search","spodumene_mid_june_low_usd_per_ton":610,"spodumene_august_rebound_usd_per_ton":880,"spodumene_2022_peak_usd_per_ton":">6000","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_strategic_resource_not_Green","notes":"Lithium mine stake improves resource security, but POSCO price and offtake economics are missing."}
{"case_id":"r4_loop16_catl_yichun_korea_lithium_beta","symbol":"003670/066970/006400/373220","company_name":"POSCO Future M / L&F / Samsung SDI / LGES","case_type":"cyclical_lithium_beta_event_premium","primary_archetype":"LITHIUM_PRICE_BETA_CYCLICAL_STAGE2","best_trigger":"T0/T1","stage_candidate":"cyclical_Stage2","price_validation":{"trigger_date":"2025-08-11","catl_mine":"Yichun_Jianxiawo","license_expiry_date":"2025-08-09","lithium_futures_event_return_pct":8,"posco_future_m_event_return_pct":8.3,"l_and_f_event_return_pct":10,"samsung_sdi_event_return_pct":3.2,"lges_event_return_pct":2.8,"lithium_price_decline_from_2022_peak_pct":90,"mine_capacity_lce_tons_per_year":46000,"forecast_global_output_share_2025_pct":3,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"cyclical_success_event_premium","notes":"Lithium beta rally is not Green unless cathode ASP and margin recover."}
{"case_id":"r4_loop16_copper_tcrc_spread_watch","symbol":"copper_smelter_basket/010130_readthrough/LS_MnM_private_readthrough","company_name":"Copper smelter spread basket","case_type":"4C_watch_spread_compression","primary_archetype":"COPPER_TC_RC_SPREAD_4C_WATCH","best_trigger":"T1/T2","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2025-10-15","countries_warning":["Japan","Spain","South_Korea"],"issue":"copper_treatment_refining_charges_unsustainable","direct_krx_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"Copper price strength does not equal smelter margin when TC/RC collapses."}
{"case_id":"r4_loop16_lgchem_sinopec_sodium_ion_materials","symbol":"051910","company_name":"LG Chem / Sinopec","case_type":"Stage2_material_optionality","primary_archetype":"SODIUM_ION_MATERIAL_OPTIONALITY_STAGE2","best_trigger":"T0/T1","stage_candidate":"Stage2","price_validation":{"trigger_date":"2025-11-04","partner":"Sinopec","technology":"sodium_ion_battery_materials","china_sodium_ion_market_2025_gwh":10,"china_sodium_ion_market_2034_gwh":292,"china_global_output_share_2030_pct":">90","direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"Sodium-ion material partnership is optionality until commercialization and customer contracts appear."}
```

## data/e2r_trigger_calibration/triggers_r4_loop16_round240.jsonl 초안

```jsonl
{"trigger_id":"r4l16_steel_us_tariff_T0","case_id":"r4_loop16_hyundai_steel_posco_tariff_antidumping","trigger_type":"4C-watch","trigger_date":"2025-02-10","evidence_available":"Trump announces planned 25% tariffs on steel/aluminum imports; POSCO -3.6% to 230,500 won, Hyundai Steel -2.9%, KOSPI -0.5%","event_return_pct":"POSCO -3.6 / Hyundai Steel -2.9","trigger_outcome_label":"tariff_export_spread_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r4l16_steel_antidumping_T1","case_id":"r4_loop16_hyundai_steel_posco_tariff_antidumping","trigger_type":"Stage2_relief","trigger_date":"2025-02-20","evidence_available":"Korea recommends 27.91-38.02% provisional anti-dumping duties on Chinese steel plates; Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7%","event_return_pct":"Hyundai Steel +5.8 / POSCO +3.9","trigger_outcome_label":"domestic_spread_relief","promote_to":"Stage2_relief"}
{"trigger_id":"r4l16_hyundai_steel_louisiana_T1","case_id":"r4_loop16_hyundai_steel_louisiana_capex","trigger_type":"Stage2_capex_with_4B","trigger_date":"2025-03-25","evidence_available":"Hyundai Steel announces $5.8B Louisiana plant with 2.7M tonnes annual capacity; shares initially +5% then -4.4%","event_return_pct":-4.4,"trigger_outcome_label":"capex_ROI_4B_price_reversal","promote_to":"4B-watch"}
{"trigger_id":"r4l16_petrochem_oversupply_T0","case_id":"r4_loop16_lgchem_lotte_petrochemical_oversupply","trigger_type":"4C-watch","trigger_date":"2025-02-07","evidence_available":"Lotte Chemical 2024 OP loss 895B won, +157% YoY; LG Chem OP -63.75% YoY, petrochemical Q4 loss 99B won","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"failed_rerating_spread_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r4l16_petrochem_restructuring_T0","case_id":"r4_loop16_lotte_hdhyundai_petrochemical_restructuring","trigger_type":"Stage2_relief","trigger_date":"2025-11-26","evidence_available":"Lotte to spin off Daesan and merge with HD Hyundai Chemical; government seeks up to 25% capacity cut and 3.7M tons/year reduction","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"restructuring_relief_not_Green","promote_to":"Stage2_relief"}
{"trigger_id":"r4l16_koreazinc_refinery_T0","case_id":"r4_loop16_korea_zinc_tennessee_critical_minerals","trigger_type":"Stage2+4B","trigger_date":"2025-12-16","evidence_available":"Korea Zinc plans $7.4B Tennessee critical minerals refinery funded largely by Washington; $1.9B share sale to U.S. government-led JV; shares -13% after injunction news","event_return_pct":-13,"trigger_outcome_label":"strategic_resource_with_dilution_4B","promote_to":"Stage2+4B"}
{"trigger_id":"r4l16_koreazinc_court_T2","case_id":"r4_loop16_korea_zinc_tennessee_critical_minerals","trigger_type":"relief_validation","trigger_date":"2025-12-24","evidence_available":"Court rejects injunction to block Korea Zinc share sale; Korea Zinc up as much as 5%, YoungPoong down 10.5%","event_return_pct":"Korea Zinc +5 / YoungPoong -10.5","trigger_outcome_label":"legal_relief_but_governance_4B_remains","promote_to":"Stage2_relief"}
{"trigger_id":"r4l16_posco_minres_T0","case_id":"r4_loop16_posco_minres_lithium_jv","trigger_type":"Stage2_strategic_resource","trigger_date":"2025-11-11","evidence_available":"POSCO buys 30% stake in part of MinRes lithium business for $765M, giving indirect 15% stakes in Wodgina and Mt Marion; MinRes +10.8%","event_return_pct":"MinRes +10.8 / POSCO unavailable","trigger_outcome_label":"Stage2_strategic_resource_not_Green","promote_to":"Stage2"}
{"trigger_id":"r4l16_catl_lithium_T0","case_id":"r4_loop16_catl_yichun_korea_lithium_beta","trigger_type":"cyclical_Stage2","trigger_date":"2025-08-11","evidence_available":"CATL Yichun mine suspension; lithium futures +8%, POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%","event_return_pct":"POSCO Future M +8.3 / L&F +10","trigger_outcome_label":"cyclical_lithium_beta","promote_to":"Stage2_cyclical"}
{"trigger_id":"r4l16_copper_tcrc_T1","case_id":"r4_loop16_copper_tcrc_spread_watch","trigger_type":"4C-watch","trigger_date":"2025-10-15","evidence_available":"Japan, Spain, South Korea warn copper TC/RCs are unsustainable amid tight concentrate supply and China smelting expansion","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"copper_spread_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r4l16_lgchem_sinopec_sodium_T0","case_id":"r4_loop16_lgchem_sinopec_sodium_ion_materials","trigger_type":"Stage2_optionality","trigger_date":"2025-11-04","evidence_available":"Sinopec and LG Chem agree to jointly develop sodium-ion battery materials; China sodium-ion market expected 10GWh in 2025 to 292GWh in 2034","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_material_optionality_not_Green","promote_to":"Stage2"}
```

## data/sector_taxonomy/score_weight_profiles_round240_r4_loop16_v1.csv 초안

```csv
archetype,domestic_spread_recovery,tariff_exposure_absorption,actual_capacity_cut,naphtha_spread_recovery,strategic_resource_offtake,dilution_governance_overlay,lithium_price_duration,smelter_tcrc_margin,commercialization_contract,commodity_price_headline_without_margin_penalty,tariff_policy_without_spread_proof_penalty,strategic_resource_capex_without_offtake_penalty,restructuring_plan_without_shutdown_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
STEEL_TARIFF_4C_AND_ANTIDUMPING_RELIEF,+5,+5,+0,+0,+0,+1,+0,+0,+0,-2,-4,-1,-1,anti-dumping/tariff event,actual spread missing,ASP+spread+margin,Hyundai Steel/POSCO tariff vs anti-dumping.
STEEL_US_LOCALIZATION_CAPEX_4B,+2,+5,+0,+0,+0,+2,+0,+0,+0,-2,-3,-4,-1,U.S. plant capex,capex ROI missing,utilization+tariff savings+margin,Hyundai Steel Louisiana.
PETROCHEMICAL_OVER_SUPPLY_FAILED_RERATING,+0,+0,+4,+5,+0,+1,+0,+0,+0,-3,-1,-1,-5,oversupply/losses,capacity cuts missing,N/A,LG Chem/Lotte oversupply.
PETROCHEMICAL_CAPACITY_RESTRUCTURING_STAGE2_RELIEF,+0,+0,+5,+5,+0,+1,+0,+0,+0,-2,-1,-1,-5,restructuring plan,shutdown/spread missing,capacity cut+spread recovery,Lotte/HD Hyundai.
CRITICAL_MINERALS_REFINERY_STAGE2_WITH_DILUTION_4B,+0,+0,+0,+0,+5,+5,+2,+2,+2,-2,-1,-5,-1,critical minerals refinery,offtake/governance missing,offtake+margin+dilution clarity,Korea Zinc.
LITHIUM_MINE_JV_STRATEGIC_RESOURCE_STAGE2,+0,+0,+0,+0,+5,+2,+5,+0,+2,-5,-1,-5,-1,lithium mine stake,offtake/margin missing,offtake+hydroxide margin,POSCO/MinRes.
LITHIUM_PRICE_BETA_CYCLICAL_STAGE2,+0,+0,+0,+0,+2,+0,+5,+0,+0,-5,-1,-2,-1,lithium price spike,duration/margin missing,cathode ASP+margin,CATL/POSCO Future M/L&F.
COPPER_TC_RC_SPREAD_4C_WATCH,+0,+0,+0,+0,+2,+1,+0,+5,+0,-5,-1,-2,-1,copper TC/RC compression,margin recovery missing,N/A,copper smelter spread.
SODIUM_ION_MATERIAL_OPTIONALITY_STAGE2,+0,+0,+0,+0,+2,+0,+1,+0,+5,-2,-1,-3,-1,sodium-ion material partnership,commercialization missing,customer contract+margin,LG Chem/Sinopec.
```

---

# 이번 R4 Loop 16 결론

```text
1. Hyundai Steel/POSCO는 정책 방향이 섞여 있다.
   U.S. steel tariff는 export spread 4C이고, Korea anti-dumping은 domestic spread Stage2 relief다.

2. Hyundai Steel Louisiana capex는 4B다.
   현지화 capex는 좋지만, intraday reversal이 capex ROI 불확실성을 보여줬다.

3. LG Chem/Lotte Chemical petrochemical은 failed rerating이다.
   oversupply와 naphtha spread 악화가 숫자로 확인됐다.

4. Lotte/HD Hyundai restructuring은 Stage2 relief다.
   실제 capacity cut과 spread recovery 전에는 Yellow가 아니다.

5. Korea Zinc Tennessee refinery는 Stage2 strategic resource + 4B다.
   critical minerals는 좋지만 share dilution과 control battle이 동시에 붙었다.

6. POSCO/MinRes lithium JV는 Stage2 strategic resource다.
   lithium downcycle에서 자원 확보는 좋지만 POSCO price anchor와 offtake margin이 없다.

7. CATL Yichun suspension은 cyclical lithium beta다.
   POSCO Future M/L&F 급등은 강하지만, cathode margin이 확인되지 않았다.

8. Copper TC/RC compression은 4C-watch다.
   copper price bull과 smelter margin은 같은 것이 아니다.

9. LG Chem/Sinopec sodium-ion은 Stage2 optionality다.
   commercialization and customer contract 전에는 Green이 아니다.
```

한 문장으로 압축하면:

> **R4 Loop 16에서 배운 핵심은 “원자재 가격·전략자원 headline”이 아니라, domestic spread, naphtha spread, TC/RC, offtake, capacity cut, dilution/governance, commercialization contract가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 steel tariff/anti-dumping, lithium spike, critical minerals capex, sodium-ion partnership, restructuring plan만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.reuters.com/markets/asia/shares-south-korean-steelmakers-drop-trump-talks-tariffs-2025-02-10/?utm_source=chatgpt.com "Shares of South Korean steelmakers drop as Trump talks tariffs"
[2]: https://www.reuters.com/markets/commodities/hyundai-steel-build-plant-louisiana-with-annual-output-27-million-tonnes-2025-03-25/?utm_source=chatgpt.com "Hyundai Steel unveils US factory plan, shares skid"
[3]: https://www.reuters.com/markets/commodities/south-korean-petrochemical-firms-profits-plunge-2024-oversupply-persists-2025-02-07/?utm_source=chatgpt.com "South Korean petrochemical firms' profits plunge in 2024 as oversupply persists"
[4]: https://www.reuters.com/world/asia-pacific/south-koreas-hd-hyundai-lotte-chemical-submit-plan-restructure-petrochemical-2025-11-26/?utm_source=chatgpt.com "South Korea's HD Hyundai, Lotte Chemical submit plan to restructure petrochemical businesses"
[5]: https://www.reuters.com/world/asia-pacific/mbk-youngpoong-seek-court-injunction-block-korea-zincs-share-sale-plan-2025-12-16/?utm_source=chatgpt.com "MBK, YoungPoong seek court injunction to block Korea Zinc's share sale plan"
[6]: https://www.reuters.com/business/energy/australias-minres-sell-30-lithium-jv-stake-posco-765-mln-2025-11-11/?utm_source=chatgpt.com "Australia's MinRes inks $765 million deal with POSCO for lithium JV stake, shares surge"
[7]: https://www.wsj.com/finance/commodities-futures/ev-battery-giant-catl-suspends-mining-project-67693725?utm_source=chatgpt.com "EV Battery Giant CATL Suspends Mining Project"
[8]: https://www.reuters.com/world/asia-pacific/japan-spain-south-korea-warn-over-unsustainable-copper-processing-fees-2025-10-15/?utm_source=chatgpt.com "Japan, Spain, South Korea warn over unsustainable copper processing fees"
[9]: https://www.reuters.com/business/energy/china-oil-major-sinopec-partners-with-south-koreas-lg-chem-develop-battery-2025-11-04/?utm_source=chatgpt.com "China oil major Sinopec partners with South Korea's LG Chem to develop battery materials"
