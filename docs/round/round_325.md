순서상 이번은 **R4 Loop 17 — 소재·스프레드·전략자원 trigger-level price validation 라운드**다.

```text
round = R4 Loop 17
round_id = round_253
large_sector = MATERIALS_SPREADS_STRATEGIC_RESOURCES
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R5 Loop 17
```

이번 라운드에서도 국장 수정주가 일봉 OHLC를 안정적으로 직접 확보하지 못했다. 따라서 MFE/MAE/peak/drawdown은 만들지 않고 `price_data_unavailable_after_deep_search`로 둔다. 대신 Reuters/FT/WSJ/MarketWatch의 **reported event return, event price, tender price, tariff rate, treatment charge, contract value, capacity-cut data**를 trigger anchor로 쓴다. 숫자를 억지로 만들지 않는 쪽이 이번 라운드의 원칙에 맞다.

---

# 1. 이번 라운드 대섹터

```text
R4 = 소재·스프레드·전략자원
```

R4의 core gate는 아래다.

```text
비철 / strategic metals:
지배권 premium → strategic resource control → capex / dilution → treatment charge → smelter margin → governance 4B

철강:
anti-dumping / tariff → domestic spread support → export tariff damage → U.S. localization hedge → utilization / margin

석유화학:
naphtha spread → China/Middle East overcapacity → NCC shutdown / restructuring → working capital → credit support

정유 / energy spread:
crude price → refining margin → inventory effect → petrochemical/battery losses → consolidated earnings

lithium / critical minerals:
mine stake / offtake → lithium price → hydroxide conversion margin → downstream battery material margin

rare earth / export control:
China export curbs → Korean downstream products → defense/transformer/battery/display sanctions risk → alternative processing capacity
```

---

# 2. 대상 canonical archetype

```text
CONTROL_PREMIUM_STRATEGIC_METALS_STAGE2_WITH_DILUTION_4B
SMELTER_TC_SPREAD_4B
CRITICAL_MINERALS_US_PROCESSING_STAGE2_WITH_CAPEX_4B
STEEL_ANTIDUMPING_PROTECTION_STAGE2
STEEL_TARIFF_AND_LOCALIZATION_HEDGE_STAGE2_4B
PETROCHEMICAL_RESTRUCTURING_STAGE2_RELIEF
PETROCHEMICAL_OVERSUPPLY_4B
REFINING_MARGIN_SPREAD_PRICE_FAILED
UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE
RARE_EARTH_EXPORT_CONTROL_4B
```

---

# 3. deep sub-archetype

```text
Korea Zinc control premium:
- MBK / Young Poong launched 2T won tender at 660,000 won.
- Korea Zinc shares +19.8%; Young Poong +30%.
- Later Korea Zinc / Bain buyback tender and court ruling pushed Korea Zinc to record high.
- Shares +6.4% to 877,000 won after court cleared buyback.
- But share issuance / regulator investigation created 4B.

Korea Zinc zinc smelting spread:
- Teck/Korea Zinc treatment charge cut to $165/t from $274/t.
- 40% TC cut means concentrate scarcity and smelter-margin pressure.
- This is operating spread 4B, separate from control premium.

Korea Zinc U.S. critical minerals:
- U.S.-backed Tennessee plant plan reported at $7.4B.
- Reuters later reported Korea Zinc revised share issuance to 2.833T won / $1.94B.
- Target products include antimony and gallium.
- Stage2 strategic-resource trigger, but funding/dilution/construction 4B.

Hyundai Steel / POSCO steel plate anti-dumping:
- Korea recommends 27.91~38.02% provisional tariffs on Chinese steel plates.
- Hyundai Steel +5.8%, POSCO Holdings +3.9%, KOSPI -0.7%.
- Stage2 domestic-spread protection.

Trump steel tariffs:
- Trump 25% steel/aluminum tariff talk: POSCO -3.6%, Hyundai Steel -2.9%.
- Later 50% threat: Hyundai Steel down as much as 5.1%, POSCO down 3.2% context.
- Steel protection can flip from positive to export 4B.

Hyundai / POSCO Louisiana steel plant:
- Hyundai Steel and Hyundai Motor Group to invest $5.8B in Louisiana steel plant.
- Annual capacity 2.7M tons, production slated for 2029.
- POSCO to invest equity / consider offtake.
- Stage2 localization hedge, but MOU/final ROI/utilization 4B.

Petrochemical oversupply / restructuring:
- Lotte Chemical 2024 operating loss widened 157% to 895B won.
- LG Chem 2024 OP fell 63.75% to 916.8B won; petrochemical division Q4 loss 99B won.
- Korea later approved Daesan restructuring: Lotte Daesan NCC 1.1M t/y shutdown for 3 years.
- Government support package up to 2T won.

SK Innovation refining spread:
- 2025 Q1 unexpected operating loss of 45B won; shares down 2.5% before announcement.
- 2025 Q2 loss deepened to 418B won.
- 2026 Q1 operating profit recovered to 2.2T won, but company warned refining normalization would take time.
- Spread recovery trigger exists but mixed with battery/petrochemical losses.

POSCO / MinRes lithium:
- POSCO buys 30% stake in part of MinRes lithium business for $765M.
- Effective 15% interests in Wodgina and Mt Marion.
- MinRes shares +10.8%; POSCO direct price unavailable.
- Strategic upstream Stage2, no Green without lithium price/offtake/margin.

Rare earth export control:
- China asked Korean firms not to export products using Chinese rare earths to U.S. defense firms.
- Affected products include transformers, batteries, displays, EVs, aerospace, medical equipment.
- Sector-wide strategic-resource 4B, no clean single-stock price anchor.
```

---

# 4. 선정 case 요약

| bucket                          | case                                        | 핵심 판정                                                                |
| ------------------------------- | ------------------------------------------- | -------------------------------------------------------------------- |
| Stage2 / control premium        | **Korea Zinc tender & buyback battle**      | +19.8%, +6.4% record high, but dilution/regulator 4B                 |
| 4B spread                       | **Korea Zinc / Teck treatment charge cut**  | TC $274/t → $165/t, smelter margin 4B                                |
| Stage2 strategic resource       | **Korea Zinc U.S. critical minerals plant** | $7.4B project, 2.833T won issuance, antimony/gallium                 |
| Stage2-Actionable               | **Hyundai Steel / POSCO anti-dumping**      | Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7%                        |
| Stage2 + 4B                     | **Hyundai/POSCO Louisiana steel plant**     | $5.8B, 2.7M t/y, 2029, localization hedge                            |
| failed_rerating / restructuring | **Lotte/LG Chem petrochemical oversupply**  | Lotte -895B won OP loss, restructuring support 2T won                |
| spread recovery candidate       | **SK Innovation refining margin**           | 2025 losses → 2026 Q1 2.2T OP, but normalization slow                |
| Stage2 no-price                 | **POSCO / MinRes lithium JV**               | $765M upstream lithium stake, MinRes +10.8%, POSCO price unavailable |
| sector 4B                       | **China rare earth export control**         | Korean transformer/battery/display/EV/aerospace supply-chain 4B      |

---

# 5. 각 case별 trigger grid

## Case A — Korea Zinc control premium / tender battle

```text
symbol = 010130
case_type = control premium Stage2 + dilution/regulator 4B
archetype = CONTROL_PREMIUM_STRATEGIC_METALS_STAGE2_WITH_DILUTION_4B
```

| trigger |                      type | date       | 당시 공개 evidence                                                            | 가격 anchor                                   | outcome |
| ------- | ------------------------: | ---------- | ------------------------------------------------------------------------- | ------------------------------------------- | ------- |
| T0      |    Stage2 control premium | 2024-09-13 | MBK/Young Poong 2T won tender, 660,000 won/share                          | Korea Zinc +19.8%, Young Poong +30%         |         |
| T1      |         Stage2 escalation | 2024-10-04 | MBK/Young Poong tender raised to 830,000 won/share, matching counteroffer | Korea Zinc +8.8%, KOSPI +0.3%               |         |
| T2      | Stage2 buyback validation | 2024-10-21 | Court rejects attempt to block Korea Zinc buyback                         | Korea Zinc +6.4% to 877,000 won             |         |
| T3      |     4B dilution/regulator | 2024-10~11 | share issuance plan, FSS investigation, revision order, selloff           | Korea Zinc -8% on suspension filing context |         |
| T4      |             Stage3-Yellow | N/A        | control outcome, debt load, governance, strategic capex finality 필요       | 보류                                          |         |

Korea Zinc의 control premium은 R4에서 가장 뚜렷한 Stage2 가격 trigger다. MBK/Young Poong이 2조원 tender offer를 시작하자 Korea Zinc는 +19.8%, Young Poong은 상한가 +30%를 기록했다. 이후 tender price가 830,000원으로 올라가자 Korea Zinc는 +8.8% 추가 반응했고, court가 Korea Zinc의 buyback을 막아달라는 Young Poong 측 요청을 기각하자 주가는 +6.4%로 877,000원 record high에 근접했다. 그러나 이후 대규모 신주발행 계획, FSS 조사, revision order가 나오면서 이 case는 “operating Stage3”가 아니라 **control premium Stage2 + dilution/governance 4B**다. ([Reuters][1])

```json
{
  "case_id": "r4_loop17_korea_zinc_control_premium",
  "symbol": "010130",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage2_control_premium_with_dilution_4B",
  "trigger_date": "2024-09-13",
  "initial_tender_value_krw_trn": 2.0,
  "initial_tender_price_krw": 660000,
  "korea_zinc_initial_event_return_pct": 19.8,
  "young_poong_initial_event_return_pct": 30,
  "raised_tender_price_krw": 830000,
  "raised_tender_event_return_pct": 8.8,
  "court_clearance_event_return_pct": 6.4,
  "court_clearance_close_krw": 877000,
  "4B_overlay": [
    "debt_load_after_buyback",
    "share_issuance_dilution",
    "FSS_investigation",
    "control_premium_not_operating_margin"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "control_premium_stage2_with_4B"
}
```

---

## Case B — Korea Zinc / Teck zinc treatment-charge cut

```text
symbol = 010130
case_type = smelter spread 4B
archetype = SMELTER_TC_SPREAD_4B
```

| trigger |          type | date       | 당시 공개 evidence                                                   | 가격 anchor       | outcome |
| ------- | ------------: | ---------- | ---------------------------------------------------------------- | --------------- | ------- |
| T0      |     4B spread | 2024-04-02 | Teck/Korea Zinc zinc treatment charge set at $165/t              | no stock anchor |         |
| T1      |    validation | 2024-04-02 | TC down 40% from $274/t; lowest since 2021                       | no price        |         |
| T2      |      4B-watch | 2024~      | mine output tightness, concentrate scarcity, smelter competition | no OHLC         |         |
| T3      | Stage2 relief | N/A        | zinc price recovery or TC rebound not confirmed                  | 보류              |         |

이 case는 control premium과 완전히 따로 봐야 한다. Korea Zinc 주가가 지배권 premium으로 올랐더라도, operating spread에서는 Teck과의 zinc treatment charge가 $274/t에서 $165/t로 40% 하락했다. TC는 광산업체가 smelter에 지급하는 가공수수료라서, 낮아지면 concentrate가 부족하고 smelter들이 원료를 놓고 경쟁한다는 뜻이다. 즉 Korea Zinc operating margin에는 4B다. ([Reuters][2])

```json
{
  "case_id": "r4_loop17_korea_zinc_teck_tc_cut",
  "symbol": "010130",
  "best_trigger": "T0/T2",
  "best_trigger_type": "4B_zinc_treatment_charge_spread",
  "trigger_date": "2024-04-02",
  "treatment_charge_2024_usd_per_ton": 165,
  "treatment_charge_prior_year_usd_per_ton": 274,
  "tc_decline_pct": 40,
  "tc_context": "lowest_since_2021",
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "smelter_margin_4B"
}
```

---

## Case C — Korea Zinc U.S. critical-minerals processing plant

```text
symbol = 010130
case_type = Stage2 strategic-resource capex + funding 4B
archetype = CRITICAL_MINERALS_US_PROCESSING_STAGE2_WITH_CAPEX_4B
```

| trigger |                      type | date       | 당시 공개 evidence                                                                  | 가격 anchor                       | outcome |
| ------- | ------------------------: | ---------- | ------------------------------------------------------------------------------- | ------------------------------- | ------- |
| T0      | Stage2 strategic resource | 2025-12-15 | U.S.-backed Tennessee critical-minerals plant, $7.4B investment                 | local media report: shares +27% |         |
| T1      |                funding 4B | 2025-12-31 | Korea Zinc revises share issuance to 2.833T won / $1.94B                        | no OHLC                         |         |
| T2      |                validation | 2025-12    | target products include antimony, gallium and other non-ferrous/precious metals | no price                        |         |
| T3      |             Stage3-Yellow | N/A        | funding completion, construction, offtake, U.S. support terms needed            | 보류                              |         |

Korea Zinc의 Tennessee critical-minerals plant는 R4 전략자원 Stage2다. FT는 U.S.가 Korea Zinc의 $7.4B critical-minerals processing plant를 지원하며, antimony, germanium, gallium 등 defense/semiconductor용 소재를 생산할 계획이라고 보도했고, 관련 보도 뒤 Korea Zinc shares가 최대 +27% 올랐다고 전했다. 이후 Reuters는 Korea Zinc가 U.S. Tennessee core-minerals smelter funding을 위해 share issuance를 2.833조원, 약 $1.94B로 확정했다고 보도했다. 좋은 전략자원 trigger지만, funding/dilution/construction이 4B다. ([Financial Times][3])

```json
{
  "case_id": "r4_loop17_korea_zinc_us_critical_minerals",
  "symbol": "010130",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_critical_minerals_processing_with_capex_4B",
  "trigger_date": "2025-12-15",
  "project_value_usd_bn": 7.4,
  "reported_share_return_context_pct": 27,
  "share_issuance_krw_trn": 2.833,
  "share_issuance_usd_bn": 1.94,
  "target_materials": [
    "antimony",
    "gallium",
    "germanium",
    "zinc",
    "lead",
    "copper",
    "gold",
    "silver"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "funding_finality",
    "construction_timeline",
    "US_government_support_terms",
    "offtake_contracts",
    "capex_ROI",
    "dilution_absorption"
  ],
  "trigger_outcome_label": "strategic_resource_stage2_with_capex_4B"
}
```

---

## Case D — Hyundai Steel / POSCO Holdings Chinese steel-plate anti-dumping

```text
symbols = 004020 / 005490
case_type = Stage2 domestic spread protection
archetype = STEEL_ANTIDUMPING_PROTECTION_STAGE2
```

| trigger |              type | date       | 당시 공개 evidence                                                                        | 가격 anchor                                     | outcome |
| ------- | ----------------: | ---------- | ------------------------------------------------------------------------------------- | --------------------------------------------- | ------- |
| T0      | Stage2 protection | 2025-02-20 | Korea recommends 27.91~38.02% provisional anti-dumping duties on Chinese steel plates | Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7% |         |
| T1      |        validation | 2025-02-20 | Chinese steel imports $10.4B in 2024, 49% of total Korean steel imports               | same                                          |         |
| T2      |          4B-watch | 2025       | U.S. tariffs and export competitiveness risk                                          | 4B                                            |         |
| T3      |     Stage3-Yellow | N/A        | domestic steel spread/margin recovery not confirmed                                   | 보류                                            |         |

Hyundai Steel/POSCO anti-dumping은 R4에서 가장 깨끗한 Stage2-Actionable에 가깝다. 한국이 중국산 steel plate에 27.91~38.02% provisional anti-dumping duties를 권고하자 Hyundai Steel은 +5.8%, POSCO Holdings는 +3.9%였고 KOSPI는 -0.7%였다. 중국산 steel imports는 2024년 $10.4B, 한국 steel imports의 49%였다. 다만 이 trigger는 내수 spread에는 긍정적이지만, 동시에 U.S. tariff/export competitiveness 4B가 붙는다. ([Reuters][4])

```json
{
  "case_id": "r4_loop17_hyundai_steel_posco_antidumping",
  "symbols": "004020/005490",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2-Actionable_domestic_steel_spread_protection",
  "trigger_date": "2025-02-20",
  "anti_dumping_rate_pct": "27.91-38.02",
  "hyundai_steel_event_return_pct": 5.8,
  "posco_event_return_pct": 3.9,
  "kospi_same_context_pct": -0.7,
  "china_steel_import_value_2024_usd_bn": 10.4,
  "china_share_of_korea_steel_imports_pct": 49,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "domestic_spread_recovery",
    "shipbuilding_demand",
    "construction_demand",
    "export_tariff_impact",
    "raw_material_cost"
  ],
  "trigger_outcome_label": "good_stage2_domestic_steel_protection"
}
```

---

## Case E — Hyundai / POSCO Louisiana steel plant localization hedge

```text
symbols = 004020 / 005490 / 005380 readthrough
case_type = Stage2 localization hedge + MOU 4B
archetype = STEEL_TARIFF_AND_LOCALIZATION_HEDGE_STAGE2_4B
```

| trigger |          type | date       | 당시 공개 evidence                                                                     | 가격 anchor                                                                        | outcome |
| ------- | ------------: | ---------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------- |
| T0      | 4B background | 2025-02~06 | U.S. steel/aluminum tariff risk hits Korean steel shares                           | POSCO -3.6%, Hyundai Steel -2.9%; later Hyundai Steel -5.1%, POSCO -3.2% context |         |
| T1      |  Stage2 hedge | 2025-04-21 | Hyundai Steel / Hyundai Motor Group $5.8B Louisiana steel plant, 2.7M t/y capacity | no clean price                                                                   |         |
| T2      |    validation | 2025-04-21 | POSCO to invest equity and consider offtake; production slated for 2029            | no price                                                                         |         |
| T3      |      4B-watch | 2025~2029  | MOU, construction, capex ROI, U.S. demand, tariff durability                       | 4B                                                                               |         |

U.S. tariff risk is negative for Korean steel exporters. Trump의 25% steel/aluminum tariff talk 때 POSCO는 -3.6%, Hyundai Steel은 -2.9%까지 하락했고, 이후 50% tariff threat 국면에서도 Hyundai Steel이 최대 -5.1%, POSCO Holdings가 -3.2% 하락한 보도가 있었다. Hyundai Steel의 Louisiana plant는 이런 risk에 대한 localization hedge다. 다만 $5.8B, 2.7M t/y, 2029년 생산이라는 장기 capex이며 POSCO participation도 MOU 성격이므로 Stage2 hedge이지 Green은 아니다. ([Reuters][5])

```json
{
  "case_id": "r4_loop17_hyundai_posco_louisiana_steel_plant",
  "symbols": "004020/005490/005380_readthrough",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage2_localization_hedge_with_tariff_4B",
  "tariff_background_date": "2025-02-10",
  "posco_tariff_event_return_pct": -3.6,
  "hyundai_steel_tariff_event_return_pct": -2.9,
  "later_50pct_tariff_context": {
    "hyundai_steel_max_drop_pct": -5.1,
    "posco_holdings_max_drop_pct": -3.2
  },
  "louisiana_plant_investment_usd_bn": 5.8,
  "annual_capacity_mn_tons": 2.7,
  "production_start_target": 2029,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "final_investment_decision",
    "construction_progress",
    "US_demand",
    "tariff_durability",
    "capex_ROI",
    "utilization"
  ],
  "trigger_outcome_label": "tariff_4B_with_localization_stage2"
}
```

---

## Case F — Lotte Chemical / LG Chem petrochemical oversupply and restructuring

```text
symbols = 011170 / 051910 / HD_Hyundai_Oilbank_readthrough
case_type = failed_rerating + restructuring relief
archetype = PETROCHEMICAL_RESTRUCTURING_STAGE2_RELIEF
```

| trigger |                        type | date       | 당시 공개 evidence                                                                             | 가격 anchor      | outcome |
| ------- | --------------------------: | ---------- | ------------------------------------------------------------------------------------------ | -------------- | ------- |
| T0      |        4B / failed rerating | 2025-02-07 | Lotte Chemical 2024 OP loss 895B won; LG Chem OP -63.75% YoY                               | no clean price |         |
| T1      |                  validation | 2025-02-07 | LG Chem petrochemical division Q4 loss 99B won; overcapacity in China/Middle East persists | no price       |         |
| T2      | Stage2 restructuring relief | 2026-02-24 | Korea approves first petrochemical restructuring; Daesan NCC 1.1M t/y shutdown for 3 years | no stock price |         |
| T3      |              policy support | 2026-02-24 | up to 2T won support, 1.2T won capital increase, tax/utility/R&D support                   | no price       |         |
| T4      |               Stage3-Yellow | N/A        | spread recovery, demand recovery, shutdown discipline needed                               | 보류             |         |

Petrochemical은 R4에서 대표 failed_rerating이다. Lotte Chemical의 2024 operating loss는 895B won으로 전년 대비 157% 확대됐고, LG Chem의 2024 operating profit은 63.75% 감소했으며 petrochemical division은 Q4에 99B won loss를 냈다. 이후 정부는 Lotte Chemical/HD Hyundai Oilbank/HD Hyundai Chemical의 Daesan restructuring을 승인했고, Lotte Daesan NCC 1.1M t/y를 3년 shutdown하는 구조조정과 최대 2T won 지원 package를 제시했다. 구조조정은 Stage2 relief지만, oversupply가 완전히 해결된 것은 아니다. ([Reuters][6])

```json
{
  "case_id": "r4_loop17_petrochemical_oversupply_restructuring",
  "symbols": "011170/051910/HD_Hyundai_Oilbank_readthrough",
  "best_trigger": "T0/T3",
  "best_trigger_type": "failed_rerating_with_stage2_restructuring_relief",
  "lotte_chemical_2024_op_loss_krw_bn": 895,
  "lotte_chemical_op_loss_yoy_widening_pct": 157,
  "lg_chem_2024_op_decline_pct": 63.75,
  "lg_chem_petrochemical_q4_loss_krw_bn": 99,
  "restructuring_approval_date": "2026-02-24",
  "daesan_ncc_shutdown_capacity_mn_tons_per_year": 1.1,
  "shutdown_period_years": 3,
  "government_support_krw_trn": 2.0,
  "capital_increase_krw_trn": 1.2,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "naphtha_spread_recovery",
    "China_demand_recovery",
    "actual_capacity_discipline",
    "working_capital_relief",
    "credit_spread_stabilization"
  ],
  "trigger_outcome_label": "petrochemical_failed_rerating_with_restructuring_relief"
}
```

---

## Case G — SK Innovation refining margin spread cycle

```text
symbol = 096770
case_type = refining spread recovery candidate, mixed with battery/petrochemical losses
archetype = REFINING_MARGIN_SPREAD_PRICE_FAILED
```

| trigger |              type | date       | 당시 공개 evidence                                                     | 가격 anchor                        | outcome |
| ------- | ----------------: | ---------- | ------------------------------------------------------------------ | -------------------------------- | ------- |
| T0      | 4B / price failed | 2025-02-06 | SK Innovation expects 2025 refining margins flat; Q4 OP 159.9B won | shares -2.9%, KOSPI +0.7%        |         |
| T1      |           4B loss | 2025-04-30 | Q1 2025 OP loss 45B won vs expected 393B profit                    | shares -2.5% before announcement |         |
| T2      |     4B validation | 2025-07-31 | Q2 2025 OP loss deepened to 418B won vs expected 140B loss         | no price                         |         |
| T3      |   Stage2 recovery | 2026-05-13 | Q1 2026 OP 2.2T won vs 30B loss year earlier; beat 1.4T estimate   | no share anchor                  |         |
| T4      |          4B-watch | 2026       | company says refining normalization will take time                 | 4B                               |         |

SK Innovation은 R4 spread case로 중요하다. 2025년 초에는 refining margins flat 전망과 함께 주가가 -2.9%로 KOSPI +0.7%를 크게 밑돌았고, Q1 2025에는 45B won unexpected loss를 냈다. Q2 2025 loss는 418B won으로 더 커졌다. 2026년 Q1에는 OP가 2.2T won으로 강하게 회복됐지만, 회사는 refining production/logistics normalization이 시간이 걸릴 것이라고 경고했다. 즉 refining spread recovery는 Stage2 candidate지만, battery/petrochemical losses와 normalization 4B를 같이 둬야 한다. ([Reuters][7])

```json
{
  "case_id": "r4_loop17_sk_innovation_refining_margin_spread",
  "symbol": "096770",
  "best_trigger": "T0/T4",
  "best_trigger_type": "mixed_refining_spread_recovery_with_4B",
  "flat_margin_trigger_date": "2025-02-06",
  "flat_margin_event_return_pct": -2.9,
  "kospi_same_context_pct": 0.7,
  "q1_2025_op_loss_krw_bn": 45,
  "q2_2025_op_loss_krw_bn": 418,
  "q1_2026_op_krw_trn": 2.2,
  "q1_2026_consensus_context_krw_trn": 1.4,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "refining_margin_sustained_recovery",
    "battery_loss_reduction",
    "petrochemical_loss_reduction",
    "logistics_normalization",
    "inventory_effect_normalization"
  ],
  "trigger_outcome_label": "refining_spread_recovery_candidate_with_4B"
}
```

---

## Case H — POSCO / MinRes lithium JV

```text
symbol = 005490
case_type = upstream lithium strategic supply no direct price
archetype = UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE
```

| trigger |                   type | date       | 당시 공개 evidence                                                        | 가격 anchor                        | outcome |
| ------- | ---------------------: | ---------- | --------------------------------------------------------------------- | -------------------------------- | ------- |
| T0      | Stage2 upstream supply | 2025-11-11 | POSCO buys 30% stake in part of MinRes lithium business for $765M     | MinRes +10.8%, POSCO unavailable |         |
| T1      |             validation | 2025-11-11 | POSCO gains effective 15% in Wodgina and Mt Marion                    | no KRX price                     |         |
| T2      |               4B-watch | 2025       | lithium price collapsed from 2022 highs; offtake/margin terms unclear | 4B                               |         |
| T3      |          Stage3-Yellow | N/A        | lithium recovery, offtake economics, downstream margin needed         | 보류                               |         |

POSCO/MinRes deal은 R4의 upstream strategic-material Stage2다. POSCO는 MinRes lithium business 일부 30% stake를 $765M에 사며 Wodgina와 Mt Marion에 각각 effective 15% interest를 확보한다. 발표 후 MinRes는 +10.8%로 1년여 고점까지 올랐지만, POSCO의 직접 KRX price anchor는 확보하지 못했다. 전략적 원료 확보는 좋지만, lithium price, offtake, hydroxide conversion margin이 닫히지 않아 Green은 아니다. ([Reuters][8])

```json
{
  "case_id": "r4_loop17_posco_minres_lithium_jv",
  "symbol": "005490",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_upstream_lithium_supply_no_direct_price",
  "trigger_date": "2025-11-11",
  "deal_value_usd_mn": 765,
  "stake_in_minres_lithium_business_pct": 30,
  "effective_stake_wodgina_pct": 15,
  "effective_stake_mt_marion_pct": 15,
  "minres_event_return_pct": 10.8,
  "posco_direct_price_anchor": "price_data_unavailable_after_deep_search",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "offtake_terms",
    "spodumene_price_recovery",
    "lithium_hydroxide_margin",
    "downstream_POSCO_materials_link",
    "capex_intensity"
  ],
  "trigger_outcome_label": "strategic_upstream_stage2_not_green"
}
```

---

## Case I — China rare-earth export control / Korea supply-chain 4B

```text
symbols = transformer_battery_display_EV_aerospace_medical_basket
case_type = sector-wide strategic-resource 4B
archetype = RARE_EARTH_EXPORT_CONTROL_4B
```

| trigger |                  type | date       | 당시 공개 evidence                                                                                 | 가격 anchor                | outcome |
| ------- | --------------------: | ---------- | ---------------------------------------------------------------------------------------------- | ------------------------ | ------- |
| T0      | 4B strategic resource | 2025-04-22 | China asks Korean firms not to export products using Chinese rare earths to U.S. defense firms | no stock-specific anchor |         |
| T1      |            validation | 2025       | affected products: transformers, batteries, displays, EVs, aerospace, medical equipment        | no price                 |         |
| T2      |            escalation | 2026       | rare-earth controls still bite despite truce talks; heavy rare-earth exports restricted        | no KRX price             |         |
| T3      |                relief | N/A        | non-China supply/processing capacity not sufficient yet                                        | 보류                       |         |

Rare earth export control은 R4에서 sector-wide 4B로 둬야 한다. 중국은 한국 기업들에게 중국산 rare earth를 사용한 제품을 U.S. defense firms에 수출하지 말라고 요청했고, 적용 제품은 transformers, batteries, displays, EVs, aerospace, medical equipment까지 넓다. 이후에도 heavy rare earth restrictions는 truce discussions에도 계속 영향을 주는 것으로 보도됐다. 이는 특정 종목 하나의 Stage3가 아니라, 한국 소재·전력기기·방산·배터리 chain 전체의 strategic-resource 4B다. ([Reuters][9])

```json
{
  "case_id": "r4_loop17_china_rare_earth_export_control_korea",
  "symbols": "transformer_battery_display_EV_aerospace_medical_basket",
  "best_trigger": "T0/T2",
  "best_trigger_type": "sector_4B_strategic_resource_control",
  "trigger_date": "2025-04-22",
  "affected_product_categories": [
    "power_transformers",
    "batteries",
    "displays",
    "electric_vehicles",
    "aerospace",
    "medical_equipment"
  ],
  "direct_stock_price_anchor": "price_data_unavailable_after_deep_search",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "non_China_supply_substitution",
    "export_license_clarity",
    "US_Korea_policy_support",
    "company_specific_cost_impact",
    "customer_order_impact"
  ],
  "trigger_outcome_label": "rare_earth_export_control_4B"
}
```

---

# 6. Trigger별 실제 가격경로 검증 요약

이번 R4 Loop 17은 full OHLC가 없으므로, 아래 표는 **reported event anchor 기준**이다.

| case                              | best trigger |                                    event return / price | market-relative | full MFE/MAE | outcome                         |
| --------------------------------- | -----------: | ------------------------------------------------------: | --------------: | ------------ | ------------------------------- |
| Korea Zinc control premium        |        T0/T3 |  +19.8%, +8.8%, +6.4% to 877,000 won; later -8% context |          strong | unavailable  | Stage2 control premium + 4B     |
| Korea Zinc TC cut                 |           T0 |                                      TC $274/t → $165/t |        no price | unavailable  | smelter spread 4B               |
| Korea Zinc U.S. critical minerals |        T0/T1 |                       +27% context, 2.833T won issuance |         no OHLC | unavailable  | Stage2 strategic + funding 4B   |
| Hyundai Steel/POSCO anti-dumping  |           T0 |                               +5.8%, +3.9%, KOSPI -0.7% |          strong | unavailable  | Stage2 steel protection         |
| Hyundai/POSCO Louisiana steel     |        T0/T2 |                        tariff selloff; project no price |           mixed | unavailable  | tariff 4B + localization Stage2 |
| Petrochemical restructuring       |        T0/T3 |                                          no clean price |             N/A | unavailable  | failed_rerating + relief        |
| SK Innovation refining spread     |        T0/T4 | -2.9% vs KOSPI +0.7%; later OP recovery no share anchor |           mixed | unavailable  | spread recovery candidate       |
| POSCO/MinRes lithium              |           T0 |                        MinRes +10.8%, POSCO unavailable | no POSCO anchor | unavailable  | Stage2 no-price                 |
| Rare earth control                |        T0/T2 |                                no stock-specific anchor |             N/A | unavailable  | sector 4B                       |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
가장 좋은 Stage2:
1. Hyundai Steel / POSCO anti-dumping: price reaction and tariff evidence both closed.
2. Korea Zinc control premium: very strong price reaction, but operating thesis와 분리해야 함.
3. Korea Zinc U.S. critical minerals: strategic-resource trigger, but dilution/capex 4B.
4. POSCO / MinRes lithium JV: strategic upstream trigger, direct POSCO price unavailable.
5. Lotte/HD Hyundai petrochemical restructuring: industry relief, no price anchor.
```

## Stage2-Actionable entry 성과

```text
Stage2-Actionable:
- Hyundai Steel / POSCO anti-dumping.
- Korea Zinc control premium, but control-premium only.
- Korea Zinc U.S. critical minerals if funding terms and offtake confirm.

Actionable 보류:
- POSCO / MinRes lithium JV: POSCO direct price and offtake economics unavailable.
- Petrochemical restructuring: restructuring helps, but spread recovery not confirmed.
- SK Innovation refining spread: 2026 OP recovery strong, but prior price-failed and normalization risk remain.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Hyundai Steel/POSCO if anti-dumping translates into sustained spread and margin recovery.
- Korea Zinc U.S. critical minerals if capex funding, construction and offtake are confirmed.
- Petrochemical restructuring if NCC shutdown discipline produces naphtha-spread recovery.
- SK Innovation if refining spread recovery sustains and battery/petrochemical losses narrow.
- POSCO lithium if offtake and downstream margin become visible.
```

## Stage3-Green

```text
이번 R4 Loop 17에서 확정 Green 없음.

이유:
- control premium은 operating margin이 아니다.
- anti-dumping은 good Stage2지만 export tariff 4B가 있다.
- petrochemical restructuring은 relief이지 spread recovery가 아니다.
- critical-minerals capex는 funding/dilution/construction이 크다.
- lithium JV는 POSCO direct price and offtake economics가 없다.
- rare earth export control은 sector 4B다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Korea Zinc control premium as Stage2, not operating Green.
- Hyundai Steel/POSCO anti-dumping as Stage2-Actionable.
- Korea Zinc TC cut as smelter-margin 4B.
- SK Innovation refining spread as mixed spread recovery candidate.
- Lotte/LG Chem petrochemical oversupply as failed_rerating.
- China rare earth export control as sector 4B.

Stage2_promote_candidate:
- Hyundai Steel/POSCO anti-dumping.
- Korea Zinc U.S. critical-minerals plant after funding/offtake clarity.
- Lotte/HD Hyundai Chemical restructuring after real spread recovery.
- POSCO/MinRes lithium after offtake and POSCO price validation.

evidence_good_but_price_failed:
- SK Innovation 2025 flat refining-margin guide / Q1 loss sequence.
- Korea Zinc strategic capex if dilution dominates.

cyclical_success:
- steel anti-dumping domestic spread.
- lithium JV / lithium rebound if price cycle turns.

event_premium:
- Korea Zinc control/tender battle.
- Korea Zinc U.S. critical-minerals plant.
- Hyundai Steel/POSCO anti-dumping.

thesis_break / 4B:
- Korea Zinc TC compression.
- petrochemical oversupply.
- Trump tariff risk.
- rare-earth export controls.
- capital issuance / dilution.

hard_4C:
- hard stock-specific 4C not confirmed in this R4 round.
- strongest 4C-watch: petrochemical prolonged overcapacity, Korea Zinc governance/dilution, rare-earth export control.
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
domestic_spread_protection,+5,"anti-dumping이 price reaction과 같이 닫히면 Stage2-Actionable","Hyundai Steel, POSCO"
control_premium_detection,+4,"지배권 premium은 가격 trigger로 강하지만 operating score와 분리","Korea Zinc"
critical_minerals_strategic_value,+5,"antimony/gallium/rare metals processing은 strategic-resource value","Korea Zinc"
upstream_resource_control,+4,"mine stake/offtake는 장기 raw-material control score","POSCO/MinRes"
capacity_shutdown_discipline,+5,"petrochemical 구조조정은 실제 capacity cut이 확인될 때 점수 상승","Lotte/HD Hyundai Chemical"
refining_spread_recovery,+4,"정유 spread 회복은 OP recovery로 검증 가능","SK Innovation"
rare_earth_export_control_risk,+5,"중국 rare-earth control은 sector-wide 4B","Korean materials/equipment/battery chain"
treatment_charge_sensitivity,+5,"zinc TC는 smelter margin 핵심","Korea Zinc"
```

## 내릴 축

```csv
axis,delta,reason,cases
control_premium_as_operating_growth,-5,"지배권 premium을 operating Stage3로 오인 금지","Korea Zinc"
critical_capex_without_funding_clarity,-5,"전략자원 capex도 funding/dilution 확인 전 Green 금지","Korea Zinc Tennessee"
anti_dumping_without_margin_recovery,-4,"관세/반덤핑 headline만으로 Green 금지","Hyundai Steel, POSCO"
tariff_export_risk_ignored,-5,"U.S. steel tariff/export risk 무시 금지","Hyundai Steel, POSCO"
petrochemical_restructuring_without_spread,-5,"구조조정 승인만으로 spread recovery 판단 금지","Lotte/LG Chem"
refining_OP_without_segment_quality,-4,"정유 OP 회복을 battery/petrochemical loss와 분리해야 함","SK Innovation"
upstream_lithium_without_offtake_margin,-4,"광산지분만으로 downstream margin Green 금지","POSCO/MinRes"
rare_earth_headline_without_company_impact,-4,"rare earth risk를 종목별 cost/order impact 없이 과대평가 금지","sector basket"
```

---

# 10. Stage2-Actionable 승격 조건

R4 Loop 17 shadow rule:

```text
R4에서 Stage2 evidence가 아래 중 4개 이상이면 Stage2-Actionable로 승격한다.

1. event return +5% 이상
2. market-relative return +5pp 이상
3. tariff / anti-dumping / tender / contract / capex value가 명확하다
4. spread, treatment charge, commodity price, utilization 중 하나가 실제 margin으로 연결될 수 있다
5. strategic resource control이 customer/offtake/capacity로 연결된다
6. dilution / export tariff / regulatory investigation / TC compression 4B가 식별 가능하다
7. price reaction이 headline과 같은 방향으로 검증된다
```

적용:

```text
Hyundai Steel/POSCO anti-dumping:
1,2,3,4,7 충족 → Stage2-Actionable.

Korea Zinc control premium:
1,2,3,7 충족. 하지만 operating margin이 아니므로 control-premium Stage2 only.

Korea Zinc U.S. critical minerals:
3,5 충족. share issuance/dilution 4B 큼 → Stage2, Yellow 보류.

Korea Zinc TC cut:
4B negative trigger. Actionable 금지.

SK Innovation:
OP recovery는 있으나 segment quality and prior price failure → Stage2 recovery candidate.

Lotte restructuring:
capacity cut and support confirmed. Spread/margin recovery 전까지 Stage2 relief.

POSCO/MinRes:
3,5 충족. POSCO price/offtake margin 없음 → Stage2 no-price.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
Stage2-Actionable 이후 아래 중 2개 이상이 추가로 닫히면 Yellow.

1. sustained spread / margin recovery
2. capacity shutdown or utilization improvement
3. offtake / customer contract finality
4. funding clarity without excessive dilution
5. export-tariff risk reduced
6. treatment charge / raw-material spread stabilizes
7. stock-specific price validation with MFE/MAE
```

Yellow 후보:

```text
Hyundai Steel/POSCO:
domestic spread recovery and export tariff mitigation 확인 시 Yellow.

Korea Zinc U.S. minerals:
funding clarity + offtake + construction timeline 확인 시 Yellow.

Lotte/HD Hyundai Chemical:
Daesan shutdown이 naphtha spread improvement로 이어지면 Yellow.

SK Innovation:
refining spread recovery and battery/petrochemical losses reduction 확인 시 Yellow.

POSCO/MinRes:
offtake economics and lithium/hydroxide margin visibility 확인 시 Yellow.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- spread improvement is visible in earnings.
- strategic resource capex has funding, offtake, construction and margin clarity.
- commodity price rebound is durable.
- treatment charge / raw-material costs are stable.
- dilution/regulatory/tariff 4B is reduced.
- full-window MFE/MAE is favorable.
```

이번 R4 Loop 17에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + spread/margin/offtake/funding/dilution gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- control premium rallies without operating improvement.
- strategic-resource capex funded by large share issuance.
- zinc TC compression.
- U.S. steel tariff threat.
- anti-dumping protection without margin recovery.
- petrochemical restructuring without demand recovery.
- refining OP recovery mixed with battery/petrochemical losses.
- lithium JV without offtake economics.
- rare-earth export controls without alternative supply.
```

적용:

```text
Korea Zinc:
control premium good, TC and dilution/regulator 4B.

Hyundai Steel/POSCO:
anti-dumping good, U.S. tariff/export 4B.

Lotte/LG Chem:
restructuring relief, but China/Middle East oversupply 4B.

SK Innovation:
refining recovery, but normalization and battery/petrochemical losses 4B.

POSCO/MinRes:
upstream supply good, but lithium price/offtake 4B.

Rare earth:
sector-wide export-control 4B.
```

---

# 14. 4C hard gate 조건

```text
R4 4C:
- permanent loss of resource access
- regulatory block / criminal investigation materially impairing capital plan
- structural spread collapse without capacity closure
- large dilution spiral
- export-control sanction stopping downstream shipments
- commodity price collapse breaking debt/capex model
```

이번 R4 Loop 17에서는 **hard stock-specific 4C 확정은 없음**.

```text
hard_4c_not_confirmed = true
strong_4c_watch = [
  "Korea Zinc governance/dilution/regulatory investigation",
  "petrochemical prolonged oversupply",
  "rare earth export control",
  "zinc TC compression if sustained",
  "U.S. steel tariff escalation"
]
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R4 production 설계 원칙:

```text
1. control premium과 operating spread를 분리한다.
2. anti-dumping/tariff headline과 actual margin recovery를 분리한다.
3. treatment charge는 smelter margin 4B로 독립 반영한다.
4. petrochemical restructuring은 spread recovery 전까지 relief로만 둔다.
5. strategic-resource capex는 funding/dilution/offtake를 확인해야 한다.
6. upstream mine stake는 offtake economics and downstream margin 확인 전 Green 금지한다.
7. rare-earth export control은 sector-wide 4B로 병기한다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_253.md 요약

```md
# R4 Loop 17. Materials / Spreads / Strategic Resources Trigger-level Price Validation

이번 라운드는 R4 Loop 17 trigger-level validation 라운드다.

핵심 결론:
- Korea Zinc control premium is Stage2, not operating Green. MBK/Young Poong launched a 2T won tender at 660,000 won/share; Korea Zinc rose 19.8% and Young Poong 30%. Later buyback/court triggers pushed Korea Zinc to a record high, but share issuance, debt load and FSS investigation created 4B.
- Korea Zinc smelter spread is 4B. Teck/Korea Zinc zinc treatment charge fell 40% to $165/t from $274/t, the lowest since 2021, implying concentrate scarcity and smelter-margin pressure.
- Korea Zinc U.S. critical-minerals plant is Stage2 with capex/dilution 4B. The U.S.-backed Tennessee project was reported at $7.4B, while Reuters later reported share issuance of 2.833T won / $1.94B to fund the plant targeting antimony and gallium.
- Hyundai Steel/POSCO anti-dumping is Stage2-Actionable. Korea recommended 27.91~38.02% provisional duties on Chinese steel plates; Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7%.
- Hyundai/POSCO Louisiana steel plant is Stage2 localization hedge with tariff 4B. Hyundai Steel/Hyundai Motor Group plan $5.8B, 2.7M t/y Louisiana plant for 2029; POSCO to invest equity and consider offtake.
- Lotte/LG Chem petrochemical oversupply is failed_rerating with restructuring relief. Lotte Chemical 2024 OP loss widened 157% to 895B won; LG Chem OP fell 63.75%. Korea later approved Daesan restructuring with a 1.1M t/y NCC shutdown and up to 2T won support.
- SK Innovation refining spread is a mixed recovery candidate. 2025 refining weakness and losses were followed by 2026 Q1 OP of 2.2T won, but management warned normalization would take time.
- POSCO/MinRes lithium JV is upstream Stage2 with no POSCO direct price validation. POSCO paid $765M for a 30% stake in part of MinRes lithium business, giving effective 15% interests in Wodgina and Mt Marion; MinRes +10.8%.
- China rare-earth export control is sector 4B. China asked Korean firms not to export products using Chinese rare earths to U.S. defense firms, affecting transformers, batteries, displays, EVs, aerospace and medical equipment.

Main calibration:
- Raise domestic_spread_protection, control_premium_detection, critical_minerals_strategic_value, upstream_resource_control, capacity_shutdown_discipline, refining_spread_recovery, rare_earth_export_control_risk, treatment_charge_sensitivity.
- Lower control_premium_as_operating_growth, critical_capex_without_funding_clarity, anti_dumping_without_margin_recovery, tariff_export_risk_ignored, petrochemical_restructuring_without_spread, refining_OP_without_segment_quality, upstream_lithium_without_offtake_margin, rare_earth_headline_without_company_impact.
```

## docs/checkpoints/checkpoint_28a_round253_r4_loop17.md 요약

```md
# Checkpoint 28A Round 253 R4 Loop 17 Trigger-level Calibration

## 반영 내용
- R4 Loop 17 trigger-level validation을 수행했다.
- Korea Zinc control premium, Korea Zinc TC cut, Korea Zinc U.S. critical-minerals plant, Hyundai Steel/POSCO anti-dumping, Hyundai/POSCO Louisiana steel plant, petrochemical restructuring, SK Innovation refining spread, POSCO/MinRes lithium JV, rare-earth export controls를 검토했다.
- full adjusted OHLC는 확보하지 못했으므로 Reuters / FT / WSJ / MarketWatch reported event return과 event price anchor를 사용했다.
- MFE/MAE는 조작하지 않고 price_data_unavailable_after_deep_search로 분리했다.

## 핵심 보정
- Control premium is not operating Green.
- Anti-dumping helps domestic spread, but tariff/export risk remains 4B.
- Zinc treatment-charge compression is a smelter-margin 4B.
- Petrochemical restructuring is relief only until spreads and utilization improve.
- Critical-minerals capex needs funding/offtake/dilution clarity.
- Upstream lithium stake needs offtake and downstream margin.
- Rare-earth export controls are sector-wide 4B overlays.
```

## data/e2r_case_library/cases_r4_loop17_round253.jsonl 초안

```jsonl
{"case_id":"r4_loop17_korea_zinc_control_premium","symbol":"010130","company_name":"Korea Zinc","case_type":"Stage2_control_premium_with_dilution_4B","primary_archetype":"CONTROL_PREMIUM_STRATEGIC_METALS_STAGE2_WITH_DILUTION_4B","best_trigger":"T0/T3","stage_candidate":"Stage2 + 4B-watch","price_validation":{"trigger_date":"2024-09-13","initial_tender_value_krw_trn":2.0,"initial_tender_price_krw":660000,"korea_zinc_initial_event_return_pct":19.8,"young_poong_initial_event_return_pct":30,"raised_tender_price_krw":830000,"raised_tender_event_return_pct":8.8,"court_clearance_event_return_pct":6.4,"court_clearance_close_krw":877000,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"control_premium_stage2_with_4B","notes":"Strong control-premium price reaction, but not operating Green; dilution/regulator/debt are 4B."}
{"case_id":"r4_loop17_korea_zinc_teck_tc_cut","symbol":"010130","company_name":"Korea Zinc","case_type":"4B_zinc_treatment_charge_spread","primary_archetype":"SMELTER_TC_SPREAD_4B","best_trigger":"T0/T2","stage_candidate":"4B-watch","price_validation":{"trigger_date":"2024-04-02","treatment_charge_2024_usd_per_ton":165,"treatment_charge_prior_year_usd_per_ton":274,"tc_decline_pct":40,"tc_context":"lowest_since_2021","direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"smelter_margin_4B","notes":"TC compression signals concentrate scarcity and smelter-margin pressure."}
{"case_id":"r4_loop17_korea_zinc_us_critical_minerals","symbol":"010130","company_name":"Korea Zinc","case_type":"Stage2_critical_minerals_processing_with_capex_4B","primary_archetype":"CRITICAL_MINERALS_US_PROCESSING_STAGE2_WITH_CAPEX_4B","best_trigger":"T0/T2","stage_candidate":"Stage2 + 4B-watch","price_validation":{"trigger_date":"2025-12-15","project_value_usd_bn":7.4,"reported_share_return_context_pct":27,"share_issuance_krw_trn":2.833,"share_issuance_usd_bn":1.94,"target_materials":["antimony","gallium","germanium","zinc","lead","copper","gold","silver"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"strategic_resource_stage2_with_capex_4B","notes":"Strategic minerals plant is a strong Stage2, but funding/dilution/construction/offtake are gates."}
{"case_id":"r4_loop17_hyundai_steel_posco_antidumping","symbol":"004020/005490","company_name":"Hyundai Steel / POSCO Holdings","case_type":"Stage2_Actionable_domestic_steel_spread_protection","primary_archetype":"STEEL_ANTIDUMPING_PROTECTION_STAGE2","best_trigger":"T0/T2","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2025-02-20","anti_dumping_rate_pct":"27.91-38.02","hyundai_steel_event_return_pct":5.8,"posco_event_return_pct":3.9,"kospi_same_context_pct":-0.7,"china_steel_import_value_2024_usd_bn":10.4,"china_share_of_korea_steel_imports_pct":49,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"good_stage2_domestic_steel_protection","notes":"Anti-dumping trigger aligned with stock reaction; export/tariff risk remains 4B."}
{"case_id":"r4_loop17_hyundai_posco_louisiana_steel_plant","symbol":"004020/005490/005380_readthrough","company_name":"Hyundai Steel / POSCO / Hyundai Motor Group","case_type":"Stage2_localization_hedge_with_tariff_4B","primary_archetype":"STEEL_TARIFF_AND_LOCALIZATION_HEDGE_STAGE2_4B","best_trigger":"T0/T3","stage_candidate":"Stage2 + 4B-watch","price_validation":{"tariff_background_date":"2025-02-10","posco_tariff_event_return_pct":-3.6,"hyundai_steel_tariff_event_return_pct":-2.9,"later_50pct_tariff_context":{"hyundai_steel_max_drop_pct":-5.1,"posco_holdings_max_drop_pct":-3.2},"louisiana_plant_investment_usd_bn":5.8,"annual_capacity_mn_tons":2.7,"production_start_target":2029,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"tariff_4B_with_localization_stage2","notes":"U.S. steel plant is a localization hedge, but MOU/ROI/utilization/tariff durability remain gates."}
{"case_id":"r4_loop17_petrochemical_oversupply_restructuring","symbol":"011170/051910/HD_Hyundai_Oilbank_readthrough","company_name":"Lotte Chemical / LG Chem / HD Hyundai Chemical","case_type":"failed_rerating_with_stage2_restructuring_relief","primary_archetype":"PETROCHEMICAL_RESTRUCTURING_STAGE2_RELIEF","best_trigger":"T0/T3","stage_candidate":"failed_rerating + Stage2 relief","price_validation":{"lotte_chemical_2024_op_loss_krw_bn":895,"lotte_chemical_op_loss_yoy_widening_pct":157,"lg_chem_2024_op_decline_pct":63.75,"lg_chem_petrochemical_q4_loss_krw_bn":99,"restructuring_approval_date":"2026-02-24","daesan_ncc_shutdown_capacity_mn_tons_per_year":1.1,"shutdown_period_years":3,"government_support_krw_trn":2.0,"capital_increase_krw_trn":1.2,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"petrochemical_failed_rerating_with_restructuring_relief","notes":"Oversupply caused losses; restructuring is relief but not Green until spreads recover."}
{"case_id":"r4_loop17_sk_innovation_refining_margin_spread","symbol":"096770","company_name":"SK Innovation","case_type":"mixed_refining_spread_recovery_with_4B","primary_archetype":"REFINING_MARGIN_SPREAD_PRICE_FAILED","best_trigger":"T0/T4","stage_candidate":"Stage2 recovery candidate + 4B-watch","price_validation":{"flat_margin_trigger_date":"2025-02-06","flat_margin_event_return_pct":-2.9,"kospi_same_context_pct":0.7,"q1_2025_op_loss_krw_bn":45,"q2_2025_op_loss_krw_bn":418,"q1_2026_op_krw_trn":2.2,"q1_2026_consensus_context_krw_trn":1.4,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"refining_spread_recovery_candidate_with_4B","notes":"Refining OP recovered, but normalization, battery losses and petrochemical losses remain gates."}
{"case_id":"r4_loop17_posco_minres_lithium_jv","symbol":"005490","company_name":"POSCO Holdings / Mineral Resources","case_type":"Stage2_upstream_lithium_supply_no_direct_price","primary_archetype":"UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE","best_trigger":"T0/T2","stage_candidate":"Stage2","price_validation":{"trigger_date":"2025-11-11","deal_value_usd_mn":765,"stake_in_minres_lithium_business_pct":30,"effective_stake_wodgina_pct":15,"effective_stake_mt_marion_pct":15,"minres_event_return_pct":10.8,"posco_direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"strategic_upstream_stage2_not_green","notes":"Strategic lithium supply stake, but POSCO direct price and offtake/downstream margin are unavailable."}
{"case_id":"r4_loop17_china_rare_earth_export_control_korea","symbol":"transformer_battery_display_EV_aerospace_medical_basket","company_name":"Korea strategic-resource downstream basket","case_type":"sector_4B_strategic_resource_control","primary_archetype":"RARE_EARTH_EXPORT_CONTROL_4B","best_trigger":"T0/T2","stage_candidate":"4B-watch","price_validation":{"trigger_date":"2025-04-22","affected_product_categories":["power_transformers","batteries","displays","electric_vehicles","aerospace","medical_equipment"],"direct_stock_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"rare_earth_export_control_4B","notes":"China rare-earth restrictions create sector-wide strategic-resource 4B, but stock-specific impact is not yet quantified."}
```

## data/e2r_trigger_calibration/triggers_r4_loop17_round253.jsonl 초안

```jsonl
{"trigger_id":"r4l17_korea_zinc_tender_T0","case_id":"r4_loop17_korea_zinc_control_premium","trigger_type":"Stage2_control_premium","trigger_date":"2024-09-13","event_return_pct":19.8,"trigger_outcome_label":"control_premium_stage2_not_operating_green","promote_to":"Stage2"}
{"trigger_id":"r4l17_korea_zinc_buyback_T2","case_id":"r4_loop17_korea_zinc_control_premium","trigger_type":"Stage2_buyback_control_validation","trigger_date":"2024-10-21","event_return_pct":6.4,"entry_price_krw":877000,"trigger_outcome_label":"control_premium_buyback_stage2","promote_to":"Stage2"}
{"trigger_id":"r4l17_korea_zinc_tc_T0","case_id":"r4_loop17_korea_zinc_teck_tc_cut","trigger_type":"4B_treatment_charge_spread","trigger_date":"2024-04-02","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"smelter_margin_4B","promote_to":"4B-watch"}
{"trigger_id":"r4l17_korea_zinc_us_minerals_T0","case_id":"r4_loop17_korea_zinc_us_critical_minerals","trigger_type":"Stage2_critical_minerals_capex","trigger_date":"2025-12-15","event_return_pct":"reported_context_+27","trigger_outcome_label":"strategic_resource_stage2_with_capex_4B","promote_to":"Stage2+4B"}
{"trigger_id":"r4l17_steel_antidumping_T0","case_id":"r4_loop17_hyundai_steel_posco_antidumping","trigger_type":"Stage2-Actionable_steel_antidumping","trigger_date":"2025-02-20","event_return_pct":"Hyundai_Steel_+5.8_POSCO_+3.9","market_relative_pp":"Hyundai_+6.5_POSCO_+4.6","trigger_outcome_label":"good_stage2_domestic_steel_protection","promote_to":"Stage2-Actionable"}
{"trigger_id":"r4l17_us_steel_tariff_T0","case_id":"r4_loop17_hyundai_posco_louisiana_steel_plant","trigger_type":"4B_export_tariff","trigger_date":"2025-02-10","event_return_pct":"POSCO_-3.6_Hyundai_Steel_-2.9","trigger_outcome_label":"steel_export_tariff_4B","promote_to":"4B-watch"}
{"trigger_id":"r4l17_louisiana_steel_T1","case_id":"r4_loop17_hyundai_posco_louisiana_steel_plant","trigger_type":"Stage2_localization_hedge","trigger_date":"2025-04-21","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"localization_hedge_stage2_not_green","promote_to":"Stage2"}
{"trigger_id":"r4l17_petrochemical_loss_T0","case_id":"r4_loop17_petrochemical_oversupply_restructuring","trigger_type":"failed_rerating_petrochemical_oversupply","trigger_date":"2025-02-07","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"petrochemical_oversupply_failed_rerating","promote_to":"4B-watch"}
{"trigger_id":"r4l17_petrochemical_restructuring_T2","case_id":"r4_loop17_petrochemical_oversupply_restructuring","trigger_type":"Stage2_restructuring_relief","trigger_date":"2026-02-24","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"capacity_cut_relief_not_green","promote_to":"Stage2_relief"}
{"trigger_id":"r4l17_sk_innovation_refining_T0","case_id":"r4_loop17_sk_innovation_refining_margin_spread","trigger_type":"evidence_good_but_price_failed_refining_spread","trigger_date":"2025-02-06","event_return_pct":-2.9,"market_relative_pp":-3.6,"trigger_outcome_label":"refining_margin_price_failed","promote_to":"no_actionable"}
{"trigger_id":"r4l17_sk_innovation_recovery_T3","case_id":"r4_loop17_sk_innovation_refining_margin_spread","trigger_type":"Stage2_refining_recovery_candidate","trigger_date":"2026-05-13","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"refining_OP_recovery_with_normalization_4B","promote_to":"Stage2"}
{"trigger_id":"r4l17_posco_minres_lithium_T0","case_id":"r4_loop17_posco_minres_lithium_jv","trigger_type":"Stage2_upstream_lithium_supply","trigger_date":"2025-11-11","event_return_pct":"MinRes_+10.8_POSCO_unavailable","trigger_outcome_label":"strategic_upstream_stage2_no_direct_price","promote_to":"Stage2"}
{"trigger_id":"r4l17_rare_earth_control_T0","case_id":"r4_loop17_china_rare_earth_export_control_korea","trigger_type":"sector_4B_rare_earth_export_control","trigger_date":"2025-04-22","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"rare_earth_export_control_4B","promote_to":"4B-watch"}
```

## data/sector_taxonomy/score_weight_profiles_round253_r4_loop17_v1.csv 초안

```csv
archetype,domestic_spread_protection,control_premium_detection,critical_minerals_strategic_value,upstream_resource_control,capacity_shutdown_discipline,refining_spread_recovery,rare_earth_export_control_risk,treatment_charge_sensitivity,control_premium_as_operating_growth_penalty,critical_capex_without_funding_clarity_penalty,anti_dumping_without_margin_recovery_penalty,tariff_export_risk_ignored_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
CONTROL_PREMIUM_STRATEGIC_METALS_STAGE2_WITH_DILUTION_4B,+1,+5,+3,+1,+0,+0,+1,+2,-5,-3,-1,-1,control premium strong,operating margin not confirmed,governance+funding clarity,Korea Zinc.
SMELTER_TC_SPREAD_4B,+0,+0,+2,+0,+0,+0,+1,+5,-1,-1,-1,-1,TC cut pressures smelter margin,relief missing,TC stabilization+zinc spread,Korea Zinc/Teck.
CRITICAL_MINERALS_US_PROCESSING_STAGE2_WITH_CAPEX_4B,+0,+2,+5,+3,+0,+0,+4,+1,-2,-5,-1,-1,strategic minerals project,capex/funding/dilution missing,offtake+funding+construction,Korea Zinc Tennessee.
STEEL_ANTIDUMPING_PROTECTION_STAGE2,+5,+0,+0,+0,+1,+0,+0,+0,-1,-1,-4,-4,anti-dumping and price reaction aligned,margin/export risk missing,spread+margin recovery,Hyundai Steel/POSCO.
STEEL_TARIFF_AND_LOCALIZATION_HEDGE_STAGE2_4B,+2,+0,+1,+0,+0,+0,+0,+0,-1,-2,-2,-5,localization hedge vs tariff risk,MOU/ROI missing,FID+utilization+tariff clarity,Hyundai/POSCO.
PETROCHEMICAL_RESTRUCTURING_STAGE2_RELIEF,+0,+0,+0,+0,+5,+1,+0,+0,-1,-1,-1,-2,capacity cut relief,spread recovery missing,naphtha spread+utilization,Lotte/LG Chem.
PETROCHEMICAL_OVERSUPPLY_4B,+0,+0,+0,+0,+4,+0,+0,+0,-1,-1,-1,-2,global overcapacity loss,structural downturn,capacity closure+demand recovery,Lotte/LG Chem.
REFINING_MARGIN_SPREAD_PRICE_FAILED,+0,+0,+0,+0,+0,+5,+0,+0,-1,-1,-1,-1,refining OP recovery candidate,segment quality missing,sustained margin+loss reduction,SK Innovation.
UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE,+0,+0,+3,+5,+0,+0,+1,+0,-1,-4,-1,-1,upstream lithium stake,POSCO price/offtake missing,offtake+lithium margin,POSCO/MinRes.
RARE_EARTH_EXPORT_CONTROL_4B,+0,+0,+5,+3,+0,+0,+5,+0,-1,-1,-1,-3,China export-control risk,stock-specific impact missing,license clarity+non-China supply,Korea downstream basket.
```

---

# 이번 R4 Loop 17 결론

```text
1. Korea Zinc control premium은 Stage2지만 operating Green이 아니다.
   +19.8%, +8.8%, +6.4% 가격반응은 강하지만, dilution/regulator/debt 4B가 크다.

2. Korea Zinc Teck TC cut은 smelter spread 4B다.
   TC $274/t → $165/t, -40%는 concentrate scarcity and smelter-margin pressure다.

3. Korea Zinc U.S. critical-minerals plant는 Stage2 strategic resource다.
   $7.4B 프로젝트와 antimony/gallium 생산은 강하지만, 2.833T won issuance와 capex 4B가 있다.

4. Hyundai Steel/POSCO anti-dumping은 R4의 가장 좋은 Stage2-Actionable이다.
   27.91~38.02% 관세, Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7%가 닫혔다.

5. Hyundai/POSCO Louisiana steel plant는 localization hedge Stage2다.
   $5.8B, 2.7M t/y, 2029 생산 목표는 좋지만 MOU/ROI/utilization gate가 남는다.

6. Petrochemical은 failed_rerating + restructuring relief다.
   Lotte/LG Chem 손실은 구조적이고, Daesan NCC shutdown과 2T won support는 relief지만 spread 회복 전에는 Green이 아니다.

7. SK Innovation refining spread는 recovery candidate다.
   2026 Q1 OP 회복은 좋지만 2025 losses, battery/petrochemical drag, normalization delay가 있다.

8. POSCO/MinRes lithium JV는 upstream Stage2다.
   $765M deal과 MinRes +10.8%는 좋지만 POSCO direct price/offtake/margin이 없다.

9. China rare-earth export control은 sector-wide 4B다.
   transformer, battery, display, EV, aerospace, medical chain에 걸리지만 stock-specific impact 전까지 basket 4B다.
```

한 문장으로 압축하면:

> **R4 Loop 17에서 배운 핵심은 “소재/전략자원 headline”이 아니라 spread가 실제 margin으로 닫히는지다. control premium, anti-dumping, critical-minerals capex, lithium mine stake, petrochemical restructuring은 모두 Stage2가 될 수 있지만, TC compression·dilution·tariff·offtake 부재·spread 미회복·rare-earth export control을 무시하면 false positive가 난다.**

다음 순서는 **R5 Loop 17 — 소비재·유통·브랜드**다.

[1]: https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/ "https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/"
[2]: https://www.reuters.com/markets/commodities/korea-zinc-agrees-40-fee-cut-turn-tecks-mined-zinc-into-metal-sources-say-2024-04-02/ "https://www.reuters.com/markets/commodities/korea-zinc-agrees-40-fee-cut-turn-tecks-mined-zinc-into-metal-sources-say-2024-04-02/"
[3]: https://www.ft.com/content/d885ab55-b4f8-4c8f-a213-94f2778863ac "https://www.ft.com/content/d885ab55-b4f8-4c8f-a213-94f2778863ac"
[4]: https://www.reuters.com/markets/asia/south-korea-provisionally-slaps-tariffs-chinese-steel-plates-dumping-2025-02-20/ "https://www.reuters.com/markets/asia/south-korea-provisionally-slaps-tariffs-chinese-steel-plates-dumping-2025-02-20/"
[5]: https://www.reuters.com/markets/asia/shares-south-korean-steelmakers-drop-trump-talks-tariffs-2025-02-10/ "https://www.reuters.com/markets/asia/shares-south-korean-steelmakers-drop-trump-talks-tariffs-2025-02-10/"
[6]: https://www.reuters.com/markets/commodities/south-korean-petrochemical-firms-profits-plunge-2024-oversupply-persists-2025-02-07/ "https://www.reuters.com/markets/commodities/south-korean-petrochemical-firms-profits-plunge-2024-oversupply-persists-2025-02-07/"
[7]: https://www.reuters.com/business/energy/south-koreas-sk-innovation-expects-2025-refining-margins-remain-flat-2025-02-06/ "https://www.reuters.com/business/energy/south-koreas-sk-innovation-expects-2025-refining-margins-remain-flat-2025-02-06/"
[8]: https://www.reuters.com/business/energy/australias-minres-sell-30-lithium-jv-stake-posco-765-mln-2025-11-11/ "https://www.reuters.com/business/energy/australias-minres-sell-30-lithium-jv-stake-posco-765-mln-2025-11-11/"
[9]: https://www.reuters.com/markets/commodities/china-asks-korea-not-export-products-using-rare-earths-us-defense-firms-paper-2025-04-22/ "https://www.reuters.com/markets/commodities/china-asks-korea-not-export-products-using-rare-earths-us-defense-firms-paper-2025-04-22/"
