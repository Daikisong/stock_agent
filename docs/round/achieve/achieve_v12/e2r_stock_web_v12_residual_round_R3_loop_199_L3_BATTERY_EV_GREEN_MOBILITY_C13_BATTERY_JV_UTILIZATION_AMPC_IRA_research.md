# E2R Stock-Web v12 Residual Research — R3 loop 199 / L3_BATTERY_EV_GREEN_MOBILITY / C13_BATTERY_JV_UTILIZATION_AMPC_IRA

## 0. Execution Metadata

```text
selected_round: R3
selected_loop: 199
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 quality / balance reinforcement after URL-proxy and missing-price repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: BATTERY_JV_AMPC_UTILIZATION_OFFSET_QUALITY_REPAIR
research_mode: post_calibrated_residual_historical_research_v12
loop_objective: AMPC/IRA/JV headline quality, utilization bridge, ex-subsidy margin, reversible-vs-irreversible 4C timing
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt Compliance Summary

This run follows the MAIN execution prompt as a historical calibration pass, not a code patch or live discovery pass. `stock_agent` production code was not opened or modified. The No-Repeat Index was used only as a duplicate and coverage ledger. The selected target is not the next sequential R-number; it is selected by the coverage-index-first rule and then mapped back to R3/L3 through the canonical archetype metadata.

Required v12 fields are included below: actual Stock-Web 1D entry rows, stock-web shard paths, 30/90/180D MFE and MAE, peak and drawdown, corporate-action contamination flags, forward-window usability, raw component score simulation, shadow-only residual contribution, machine-readable JSONL rows, batch ingest self-audit, and next research state.

## 2. Why this archetype was selected

The current No-Repeat Index has already crossed the 80-row threshold for every C01~C32 canonical archetype. Therefore this run is a quality and balance repair, not a raw-row fill. `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` remains a Priority 1 style candidate because AMPC/IRA persistence, JV utilization, and failure/offset quality are still the failure modes most likely to create false Stage2 or false hard-4C decisions.

Recent completed local outputs covered C05, C01, C13, C15, C10, C14, C02, and R13 checkpoint scopes. To avoid immediately repeating the last R13 accounting/4B/Stage2 taxonomy cleanup, this run returns to a source canonical: C13. The chosen fine axis focuses on whether policy credit and North American capacity are translating into utilization, customer pull, ex-subsidy margin, and durable backlog conversion.

## 3. No-Repeat / Novelty Audit

Hard duplicate key: `canonical_archetype_id + symbol + trigger_type + entry_date`.

| hard_duplicate_key | novelty reason |
|---|---|
| `C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|Stage2-Actionable|2023-01-27` | actual_AMPC_backlog_GMJV_ramp / positive_structural_stage2_control |
| `C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|Stage4B|2023-10-25` | AMPC_positive_but_demand_slowdown_ASP_pressure / offset_quality_guardrail |
| `C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|Stage2|2023-07-27` | premium_EV_P5_record_quarter_without_forward_utilization_margin_bridge / false_positive_control |
| `C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|Stage4B|2024-01-30` | annual_EV_battery_growth_but_Q4_raw_material_margin_pressure / reversible_weakness_guardrail |
| `C13_BATTERY_JV_UTILIZATION_AMPC_IRA|051910|Stage2|2023-12-20` | Tennessee_cathode_capex_2026_start_without_near_term_utilization / long_lead_capex_false_positive |
| `C13_BATTERY_JV_UTILIZATION_AMPC_IRA|011790|Stage2-Actionable|2023-08-07` | exclusive_copper_foil_customer_supply_deal / high_MAE_true_late_winner_control |
| `C13_BATTERY_JV_UTILIZATION_AMPC_IRA|247540|Stage2|2023-12-04` | single_large_cathode_supply_contract_customer_concentration / single_large_supply_deal_cycle_peak_counterexample |
| `C13_BATTERY_JV_UTILIZATION_AMPC_IRA|247540|Stage4B|2024-02-07` | JV_and_supply_contract_offset_but_customer_concentration_and_demand_risk / contract_offset_local_4B_guardrail |

Batch novelty is not based on new tickers only. Korean C13 investable coverage is concentrated in a few cell/material/copper-foil names, so the independent unit here is the distinct trigger family and entry date. The batch uses eight new hard keys, five symbols, and at least seven distinct evidence mechanisms: AMPC-recognized profit, AMPC-with-demand-slowdown, premium-P5 record quarter, raw-material margin pressure, long-lead cathode capex, exclusive copper-foil customer supply, large cathode supply contract, and JV-contract-offset 4B watch.

## 4. Price Source Validation

```text
primary_price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
manifest_path: atlas/manifest.json
schema_path: atlas/schema.json
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
tradable_columns: d,o,h,l,c,v,a,mc,s,m
MFE_N_pct: (max high from entry_date through N tradable rows / entry_close - 1) * 100
MAE_N_pct: (min low from entry_date through N tradable rows / entry_close - 1) * 100
```
Corporate-action contamination was checked at the profile/window level. `373220` has no profile candidate; `006400` candidates are historical and outside the selected windows; `011790` candidates are historical and outside the selected windows; `247540` candidates are in 2022 and outside these 2023/2024 windows. The `096770` candidate in 2024 is not used in this batch. `051910` is treated as usable for the selected 2023-12-20 to 2024-09-12 180D window, with no candidate overlap applied in the calibration row.

## 5. Case Table

| case_id | symbol | company | trigger | entry close | role | outcome | 180D MFE / MAE | profile verdict |
|---|---:|---|---|---:|---|---|---:|---|
| C13_LGES_2023FY22_GMJV_AMPC_BACKLOG | 373220 | LG Energy Solution | Stage2-Actionable / 2023-01-27 | 506,000 | positive_structural_stage2_control | positive_control | 22.53 / -13.93 | current_profile_correct_but_green_blocked |
| C13_LGES_2023Q3_IRA_GMJV_DEMAND_SLOWDOWN | 373220 | LG Energy Solution | Stage4B / 2023-10-25 | 409,500 | offset_quality_guardrail | guardrail_success | 22.10 / -21.25 | current_profile_correct_4B_not_4C |
| C13_SDI_2023Q2_PREMIUM_P5_RECORD_BUT_CYCLE_PEAK | 006400 | Samsung SDI | Stage2 / 2023-07-27 | 662,000 | false_positive_control | counterexample | 5.89 / -48.34 | current_profile_false_positive |
| C13_SDI_2023FY_Q4_RAW_MATERIAL_PRESSURE_LOCAL_4B | 006400 | Samsung SDI | Stage4B / 2024-01-30 | 374,500 | reversible_weakness_guardrail | guardrail_success | 32.04 / -21.36 | current_profile_correct_local_4B |
| C13_LGCHEM_2023_TENNESSEE_CATHODE_LONG_LEAD_CAPEX | 051910 | LG Chem | Stage2 / 2023-12-20 | 504,000 | long_lead_capex_false_positive | counterexample | 3.17 / -47.72 | current_profile_false_positive |
| C13_SKC_2023_SKNEXILIS_VARTA_COPPER_FOIL_DEAL | 011790 | SKC | Stage2-Actionable / 2023-08-07 | 96,000 | high_MAE_true_late_winner_control | positive_control_high_MAE | 55.94 / -29.17 | current_profile_correct_but_green_blocked |
| C13_ECOPROBM_2023_SDI_44T_SUPPLY_CYCLE_PEAK | 247540 | EcoPro BM | Stage2 / 2023-12-04 | 323,000 | single_large_supply_deal_cycle_peak_counterexample | counterexample | 9.60 / -49.23 | current_profile_false_positive |
| C13_ECOPROBM_2024_CAM7_JV_CONTRACT_OFFSET_4B | 247540 | EcoPro BM | Stage4B / 2024-02-07 | 230,500 | contract_offset_local_4B_guardrail | guardrail_success | 29.50 / -35.49 | current_profile_correct_4B_not_4C |

## 6. Actual Stock-Web 1D Entry Rows and Forward Path

| case_id | shard | actual entry OHLCV | MFE30 / MAE30 | MFE90 / MAE90 | MFE180 / MAE180 | 180D peak | 180D trough | post-peak drawdown |
|---|---|---|---:|---:|---:|---|---|---:|
| C13_LGES_2023FY22_GMJV_AMPC_BACKLOG | `atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv` | 2023-01-27 o=525,000 h=526,000 l=504,000 c=506,000 v=459,245 | 12.65 / -3.16 | 21.15 / -3.16 | 22.53 / -13.93 | 2023-07-26 / 620,000 | 2023-10-20 / 435,500 | -29.76% |
| C13_LGES_2023Q3_IRA_GMJV_DEMAND_SLOWDOWN | `atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv` | 2023-10-25 o=449,000 h=449,500 l=409,000 c=409,500 v=1,005,968 | 22.10 / -8.30 | 22.10 / -11.60 | 22.10 / -21.25 | 2023-11-06 / 500,000 | 2024-06-28 / 322,500 | -35.50% |
| C13_SDI_2023Q2_PREMIUM_P5_RECORD_BUT_CYCLE_PEAK | `atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv` | 2023-07-27 o=700,000 h=701,000 l=660,000 c=662,000 v=560,783 | 5.89 / -11.93 | 5.89 / -37.01 | 5.89 / -48.34 | 2023-07-27 / 701,000 | 2024-01-26 / 342,000 | -51.21% |
| C13_SDI_2023FY_Q4_RAW_MATERIAL_PRESSURE_LOCAL_4B | `atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv` | 2024-01-30 o=383,500 h=390,000 l=373,500 c=374,500 v=524,836 | 25.10 / -3.07 | 32.04 / -3.07 | 32.04 / -21.36 | 2024-03-25 / 494,500 | 2024-08-05 / 294,500 | -40.44% |
| C13_LGCHEM_2023_TENNESSEE_CATHODE_LONG_LEAD_CAPEX | `atlas/ohlcv_tradable_by_symbol_year/051/051910/2023.csv` | 2023-12-20 o=502,000 h=507,000 l=501,000 c=504,000 v=197,344 | 0.60 / -23.91 | 3.17 / -27.38 | 3.17 / -47.72 | 2024-02-19 / 520,000 | 2024-08-05 / 263,500 | -49.33% |
| C13_SKC_2023_SKNEXILIS_VARTA_COPPER_FOIL_DEAL | `atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv` | 2023-08-07 o=98,300 h=99,800 l=95,700 c=96,000 v=226,633 | 9.90 / -18.75 | 9.90 / -29.17 | 55.94 / -29.17 | 2024-04-09 / 149,700 | 2023-10-23 / 68,000 | -29.73% |
| C13_ECOPROBM_2023_SDI_44T_SUPPLY_CYCLE_PEAK | `atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv` | 2023-12-04 o=320,000 h=354,000 l=307,500 c=323,000 v=6,062,155 | 9.60 / -17.96 | 9.60 / -34.67 | 9.60 / -49.23 | 2023-12-04 / 354,000 | 2024-08-05 / 164,000 | -53.67% |
| C13_ECOPROBM_2024_CAM7_JV_CONTRACT_OFFSET_4B | `atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv` | 2024-02-07 o=226,000 h=250,000 l=225,500 c=230,500 v=2,845,259 | 21.69 / -2.17 | 29.50 / -21.26 | 29.50 / -35.49 | 2024-03-27 / 298,500 | 2024-09-10 / 148,700 | -50.18% |

## 7. Evidence Notes

### C13_LGES_2023FY22_GMJV_AMPC_BACKLOG — LG Energy Solution (373220)
- Trigger: `Stage2-Actionable` on `2023-01-27`; entry row `2023-01-27` close `506,000`.
- Evidence family: `actual_AMPC_backlog_GMJV_ramp`.
- Evidence: FY2022 revenue and operating profit reached record levels; 2023 guidance targeted 25-30% revenue growth, more than 50% capex growth, GM JV ramp-up in Ohio, and KRW385T order backlog.
- Source URL: https://news.lgensol.com/company-news/press-releases/1377/
- Calibration verdict: `current_profile_correct_but_green_blocked` / residual label `valid_stage2_but_not_green_without_ex_ampc_margin_and_low_MAE`.

### C13_LGES_2023Q3_IRA_GMJV_DEMAND_SLOWDOWN — LG Energy Solution (373220)
- Trigger: `Stage4B` on `2023-10-25`; entry row `2023-10-25` close `409,500`.
- Evidence family: `AMPC_positive_but_demand_slowdown_ASP_pressure`.
- Evidence: Q3 2023 operating profit improved and IRA tax credit was recognized, but management also cited Europe demand slowdown, OEM production adjustment, and ASP erosion.
- Source URL: https://news.lgensol.com/company-news/press-releases/2220/
- Calibration verdict: `current_profile_correct_4B_not_4C` / residual label `AMPC_and_GMJV_offset_prevents_hard_4C_but_keeps_4B_watch`.

### C13_SDI_2023Q2_PREMIUM_P5_RECORD_BUT_CYCLE_PEAK — Samsung SDI (006400)
- Trigger: `Stage2` on `2023-07-27`; entry row `2023-07-27` close `662,000`.
- Evidence family: `premium_EV_P5_record_quarter_without_forward_utilization_margin_bridge`.
- Evidence: Q2 2023 revenue and operating profit were record Q2 levels, with Automotive & ESS sales/profit helped by premium vehicles and P5; however the later price path shows this evidence sat near a cycle peak.
- Source URL: https://news.samsungsdi.com/global/articleView?seq=51
- Calibration verdict: `current_profile_false_positive` / residual label `record_quarter_language_without_forward_demand_bridge_is_not_actionable`.

### C13_SDI_2023FY_Q4_RAW_MATERIAL_PRESSURE_LOCAL_4B — Samsung SDI (006400)
- Trigger: `Stage4B` on `2024-01-30`; entry row `2024-01-30` close `374,500`.
- Evidence family: `annual_EV_battery_growth_but_Q4_raw_material_margin_pressure`.
- Evidence: FY2023 battery results were strong, with EV battery revenue and operating profit up sharply, but Q4 revenue/profit declined and raw-material-price effects pressured the energy business.
- Source URL: https://samsungsdi.com/sdi-now/sdi-news/3502.html?idx=3502
- Calibration verdict: `current_profile_correct_local_4B` / residual label `q4_margin_pressure_should_warn_but_annual_growth_offset_blocks_hard_4C`.

### C13_LGCHEM_2023_TENNESSEE_CATHODE_LONG_LEAD_CAPEX — LG Chem (051910)
- Trigger: `Stage2` on `2023-12-20`; entry row `2023-12-20` close `504,000`.
- Evidence family: `Tennessee_cathode_capex_2026_start_without_near_term_utilization`.
- Evidence: LG Chem broke ground on a Tennessee cathode plant, targeting 60,000 tons annual capacity and 2026 production, with GM/Toyota supply context. The evidence is real but long-lead rather than near-term utilization.
- Source URL: https://www.lgcorp.com/media/release/27138
- Calibration verdict: `current_profile_false_positive` / residual label `long_lead_2026_capacity_should_not_trigger_actionable_2023_entry`.

### C13_SKC_2023_SKNEXILIS_VARTA_COPPER_FOIL_DEAL — SKC (011790)
- Trigger: `Stage2-Actionable` on `2023-08-07`; entry row `2023-08-07` close `96,000`.
- Evidence family: `exclusive_copper_foil_customer_supply_deal`.
- Evidence: SK Nexilis secured an exclusive copper foil supply deal for Varta EV batteries. The row shows a painful initial MAE but eventual 180D upside, so C13 should not treat high MAE alone as a Stage2 blocker.
- Source URL: https://en.yna.co.kr/view/AEN20230807002300320
- Calibration verdict: `current_profile_correct_but_green_blocked` / residual label `direct_customer_supply_can_be_true_stage2_even_with_high_MAE_but_green_blocker_stays`.

### C13_ECOPROBM_2023_SDI_44T_SUPPLY_CYCLE_PEAK — EcoPro BM (247540)
- Trigger: `Stage2` on `2023-12-04`; entry row `2023-12-04` close `323,000`.
- Evidence family: `single_large_cathode_supply_contract_customer_concentration`.
- Evidence: EcoPro BM announced a five-year KRW44T cathode supply deal to Samsung SDI. The contract was large and real, but the stock-web path marks it as a cycle-peak false positive without near-term margin/utilization confirmation.
- Source URL: https://koreajoongangdaily.joins.com/news/2023-12-03/business/industry/EcoPro-BM-secures-34-billion-deal-as-Samsung-SDIs-cathode-supplier/1926748
- Calibration verdict: `current_profile_false_positive` / residual label `large_contract_size_without_margin_and_demand_bridge_is_cycle_peak_false_positive`.

### C13_ECOPROBM_2024_CAM7_JV_CONTRACT_OFFSET_4B — EcoPro BM (247540)
- Trigger: `Stage4B` on `2024-02-07`; entry row `2024-02-07` close `230,500`.
- Evidence family: `JV_and_supply_contract_offset_but_customer_concentration_and_demand_risk`.
- Evidence: The Samsung SDI JV/supply relationship remained a real offset, but the forward path still showed a deep drawdown. This is a local 4B watch, not automatic hard 4C while contract offset remains explicit.
- Source URL: https://www.koreatimes.co.kr/business/companies/20221021/ecopro-bm-samsung-sdi-jv-completes-construction-of-new-cathode-plant-in-pohang
- Calibration verdict: `current_profile_correct_4B_not_4C` / residual label `contract_offset_blocks_hard_4C_but_demand_risk_keeps_4B_watch`.

## 8. Residual Interpretation

C13 is not a single policy-credit switch. It is a three-valve pipe: AMPC/IRA credit is the first valve, actual utilization is the second, and customer pull or contract conversion is the third. A headline becomes Stage2-Actionable only when the water gets through at least two valves. The false-positive rows show what happens when the system opens the first valve and mistakes pressure noise for flow.

The 2023 Samsung SDI, LG Chem, and EcoPro BM rows form the false-positive cluster. Each had real evidence — premium EV battery sales, a large Tennessee cathode plant, or a KRW44T supply contract — but the evidence was either cycle-peak, long-lead, or not yet tied to utilization/margin conversion. Their 180D MAEs were -48.34%, -47.72%, and -49.23%, while 180D MFE remained only 5.89%, 3.17%, and 9.60%.

The LGES and SKC rows prevent over-tightening. LGES 2023 and SKC 2023 show that real North America/JV/customer-supply evidence can still be valid even with post-entry drawdown. These rows argue against blocking Stage2 purely because MAE is high. They argue for a Green blocker, not a Stage2 blocker.

The 4B rows are the timing lesson. AMPC that masks operating weakness, raw-material margin pressure, or contract-offset-with-demand-risk should become local 4B/watch. It should not automatically become hard 4C unless utilization, customer call-off, margin break, or JV impairment is irreversible.

## 9. Stage / Score / Return Alignment

| case_id | weighted score before -> after | stage before -> after | changed axes | alignment label |
|---|---:|---|---|---|
| C13_LGES_2023FY22_GMJV_AMPC_BACKLOG | 82 -> 76 | Stage2-Actionable -> Stage2-Actionable capped below Green | utilization, AMPC quality, ex-subsidy margin, execution risk, accounting trust | valid_stage2_but_not_green_without_ex_ampc_margin_and_low_MAE |
| C13_LGES_2023Q3_IRA_GMJV_DEMAND_SLOWDOWN | 67 -> 58 | Stage2/Watch -> Stage4B | utilization, AMPC quality, ex-subsidy margin, execution risk, accounting trust | AMPC_and_GMJV_offset_prevents_hard_4C_but_keeps_4B_watch |
| C13_SDI_2023Q2_PREMIUM_P5_RECORD_BUT_CYCLE_PEAK | 74 -> 55 | Stage2 -> Stage1/Watch | utilization, AMPC quality, ex-subsidy margin, execution risk, accounting trust | record_quarter_language_without_forward_demand_bridge_is_not_actionable |
| C13_SDI_2023FY_Q4_RAW_MATERIAL_PRESSURE_LOCAL_4B | 62 -> 57 | Stage2/Watch -> Stage4B | utilization, AMPC quality, ex-subsidy margin, execution risk, accounting trust | q4_margin_pressure_should_warn_but_annual_growth_offset_blocks_hard_4C |
| C13_LGCHEM_2023_TENNESSEE_CATHODE_LONG_LEAD_CAPEX | 72 -> 50 | Stage2 -> Stage1/Watch | utilization, AMPC quality, ex-subsidy margin, execution risk, accounting trust | long_lead_2026_capacity_should_not_trigger_actionable_2023_entry |
| C13_SKC_2023_SKNEXILIS_VARTA_COPPER_FOIL_DEAL | 77 -> 71 | Stage2-Actionable -> Stage2-Actionable high-MAE capped | utilization, AMPC quality, ex-subsidy margin, execution risk, accounting trust | direct_customer_supply_can_be_true_stage2_even_with_high_MAE_but_green_blocker_stays |
| C13_ECOPROBM_2023_SDI_44T_SUPPLY_CYCLE_PEAK | 78 -> 54 | Stage2-Actionable -> Stage1/Watch | utilization, AMPC quality, ex-subsidy margin, execution risk, accounting trust | large_contract_size_without_margin_and_demand_bridge_is_cycle_peak_false_positive |
| C13_ECOPROBM_2024_CAM7_JV_CONTRACT_OFFSET_4B | 61 -> 56 | Stage2/Watch -> Stage4B | utilization, AMPC quality, ex-subsidy margin, execution risk, accounting trust | contract_offset_blocks_hard_4C_but_demand_risk_keeps_4B_watch |

Aggregate return separation:

```text
all_cases_avg_MFE_90D_pct: 16.67
all_cases_avg_MAE_90D_pct: -20.91
all_cases_avg_MFE_180D_pct: 22.6
all_cases_avg_MAE_180D_pct: -33.31
positive_control_avg_MFE_180D_pct: 39.23
positive_control_avg_MAE_180D_pct: -21.55
false_positive_avg_MFE_180D_pct: 6.22
false_positive_avg_MAE_180D_pct: -48.43
guardrail_avg_MFE_180D_pct: 27.88
guardrail_avg_MAE_180D_pct: -26.03
```
## 10. Candidate Shadow Rules

```text
sector_specific_rule_candidate: L3_C13_AMPC_UTILIZATION_BRIDGE_GATE
canonical_archetype_rule_candidate: C13_AMPC_JV_UTILIZATION_QUALITY_SPLIT
counterexample_guard_candidate: C13_LONG_LEAD_CAPEX_AND_SINGLE_CONTRACT_STAGE2_CAP
4C_guard_candidate: C13_HARD_4C_IRREVERSIBLE_UTILIZATION_BREAK_REQUIRED
new_axis_proposed: false
weight_delta_proposed: false
rule_gate_candidate: true
production_scoring_changed: false
shadow_weight_only: true
```
Rule language:

1. AMPC/IRA/JV language alone can support Stage2 watch, but not Stage2-Actionable unless one additional bridge is present: actual utilization, customer pull/call-off, shipment schedule, order/backlog conversion, ex-subsidy margin, or cost-reduction evidence.

2. A long-lead plant/capacity announcement with production start more than four quarters away should be capped at Stage1/Stage2 watch until utilization or shipment evidence appears.

3. A large customer supply contract should not be treated as a Green bridge if the entry is cycle-peak and 90D MAE breaches -25% without margin/revision confirmation.

4. Hard 4C requires irreversible utilization/call-off/customer/JV impairment plus weak offset quality. Demand slowdown or raw-material pressure alone remains 4B/watch when recovery, ESS/non-EV reallocation, or explicit cost-reduction offset is present.

## 11. Shadow Weight Before / After

| profile | eps_fcf | earnings_visibility | bottleneck_pricing | market_mispricing | valuation_rerating | capital_allocation | information_confidence | note |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| before C13 index profile | 20 | 18 | 14 | 12 | 10 | 10 | 16 | current canonical profile from No-Repeat coverage summary |
| after shadow | 20 | 18 | 14 | 12 | 10 | 10 | 16 | no numeric weight delta proposed; add rule-gate overlay only |

The residual is better expressed as a gate than as a broad weight move. A weight cut would hurt the true-positive LGES/SKC cases; a gate blocks the false-positive cluster while preserving early structural winners.

## 12. Machine-Readable JSONL Rows

```jsonl
{"row_type":"trigger_result","research_file":"e2r_stock_web_v12_residual_round_R3_loop_199_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","research_mode":"post_calibrated_residual_historical_research_v12","selected_round":"R3","selected_loop":199,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_JV_AMPC_UTILIZATION_OFFSET_QUALITY_REPAIR","hard_duplicate_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|Stage2-Actionable|2023-01-27","case_id":"C13_LGES_2023FY22_GMJV_AMPC_BACKLOG","symbol":"373220","company":"LG Energy Solution","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-27","entry_date":"2023-01-27","entry_price":506000,"actual_1D_OHLCV":{"d":"2023-01-27","o":525000,"h":526000,"l":504000,"c":506000,"v":459245},"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":["d","o","h","l","c","v","a","mc","s","m"],"corporate_action_candidate_overlap_180D":false,"corporate_action_note":"profile corporate_action_candidate_count=0","insufficient_forward_window_180D":false,"forward_available_tradable_days":747},"MFE_30D_pct":12.65,"MAE_30D_pct":-3.16,"MFE_90D_pct":21.15,"MAE_90D_pct":-3.16,"MFE_180D_pct":22.53,"MAE_180D_pct":-13.93,"peak_180D_date":"2023-07-26","peak_180D_price":620000,"trough_180D_date":"2023-10-20","trough_180D_price":435500,"drawdown_after_peak_pct":-29.76,"drawdown_trough_after_peak_date":"2023-10-20","case_role":"positive_structural_stage2_control","outcome_label":"positive_control","profile_verdict":"current_profile_correct_but_green_blocked","evidence_family":"actual_AMPC_backlog_GMJV_ramp","evidence_summary":"FY2022 revenue and operating profit reached record levels; 2023 guidance targeted 25-30% revenue growth, more than 50% capex growth, GM JV ramp-up in Ohio, and KRW385T order backlog.","evidence_url":"https://news.lgensol.com/company-news/press-releases/1377/","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false,"score_simulation":{"raw_component_scores_before":{"contract_backlog":8,"utilization_bridge":7,"ampc_quality":8,"ex_subsidy_margin":5,"customer_pull":8,"revision_quality":6,"execution_risk_inverse":6,"accounting_trust":7},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_backlog":8,"utilization_bridge":7,"ampc_quality":7,"ex_subsidy_margin":4,"customer_pull":8,"revision_quality":5,"execution_risk_inverse":5,"accounting_trust":6},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable capped below Green","changed_component_axes":["utilization_bridge","ampc_quality","ex_subsidy_margin","execution_risk_inverse","accounting_trust"],"residual_label":"valid_stage2_but_not_green_without_ex_ampc_margin_and_low_MAE"},"calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger_result","research_file":"e2r_stock_web_v12_residual_round_R3_loop_199_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","research_mode":"post_calibrated_residual_historical_research_v12","selected_round":"R3","selected_loop":199,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_JV_AMPC_UTILIZATION_OFFSET_QUALITY_REPAIR","hard_duplicate_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|Stage4B|2023-10-25","case_id":"C13_LGES_2023Q3_IRA_GMJV_DEMAND_SLOWDOWN","symbol":"373220","company":"LG Energy Solution","trigger_type":"Stage4B","trigger_date":"2023-10-25","entry_date":"2023-10-25","entry_price":409500,"actual_1D_OHLCV":{"d":"2023-10-25","o":449000,"h":449500,"l":409000,"c":409500,"v":1005968},"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":["d","o","h","l","c","v","a","mc","s","m"],"corporate_action_candidate_overlap_180D":false,"corporate_action_note":"profile corporate_action_candidate_count=0","insufficient_forward_window_180D":false,"forward_available_tradable_days":565},"MFE_30D_pct":22.1,"MAE_30D_pct":-8.3,"MFE_90D_pct":22.1,"MAE_90D_pct":-11.6,"MFE_180D_pct":22.1,"MAE_180D_pct":-21.25,"peak_180D_date":"2023-11-06","peak_180D_price":500000,"trough_180D_date":"2024-06-28","trough_180D_price":322500,"drawdown_after_peak_pct":-35.5,"drawdown_trough_after_peak_date":"2024-06-28","case_role":"offset_quality_guardrail","outcome_label":"guardrail_success","profile_verdict":"current_profile_correct_4B_not_4C","evidence_family":"AMPC_positive_but_demand_slowdown_ASP_pressure","evidence_summary":"Q3 2023 operating profit improved and IRA tax credit was recognized, but management also cited Europe demand slowdown, OEM production adjustment, and ASP erosion.","evidence_url":"https://news.lgensol.com/company-news/press-releases/2220/","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false,"score_simulation":{"raw_component_scores_before":{"contract_backlog":7,"utilization_bridge":5,"ampc_quality":7,"ex_subsidy_margin":3,"customer_pull":5,"revision_quality":4,"execution_risk_inverse":4,"accounting_trust":5},"weighted_score_before":67,"stage_label_before":"Stage2/Watch","raw_component_scores_after":{"contract_backlog":7,"utilization_bridge":4,"ampc_quality":5,"ex_subsidy_margin":2,"customer_pull":4,"revision_quality":3,"execution_risk_inverse":3,"accounting_trust":4},"weighted_score_after":58,"stage_label_after":"Stage4B","changed_component_axes":["utilization_bridge","ampc_quality","ex_subsidy_margin","execution_risk_inverse","accounting_trust"],"residual_label":"AMPC_and_GMJV_offset_prevents_hard_4C_but_keeps_4B_watch"},"calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger_result","research_file":"e2r_stock_web_v12_residual_round_R3_loop_199_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","research_mode":"post_calibrated_residual_historical_research_v12","selected_round":"R3","selected_loop":199,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_JV_AMPC_UTILIZATION_OFFSET_QUALITY_REPAIR","hard_duplicate_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|Stage2|2023-07-27","case_id":"C13_SDI_2023Q2_PREMIUM_P5_RECORD_BUT_CYCLE_PEAK","symbol":"006400","company":"Samsung SDI","trigger_type":"Stage2","trigger_date":"2023-07-27","entry_date":"2023-07-27","entry_price":662000,"actual_1D_OHLCV":{"d":"2023-07-27","o":700000,"h":701000,"l":660000,"c":662000,"v":560783},"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":["d","o","h","l","c","v","a","mc","s","m"],"corporate_action_candidate_overlap_180D":false,"corporate_action_note":"profile candidates 1996-01-03, 1998-11-03, 2014-07-15; no overlap with 2023-07-27 +180D","insufficient_forward_window_180D":false,"forward_available_tradable_days":623},"MFE_30D_pct":5.89,"MAE_30D_pct":-11.93,"MFE_90D_pct":5.89,"MAE_90D_pct":-37.01,"MFE_180D_pct":5.89,"MAE_180D_pct":-48.34,"peak_180D_date":"2023-07-27","peak_180D_price":701000,"trough_180D_date":"2024-01-26","trough_180D_price":342000,"drawdown_after_peak_pct":-51.21,"drawdown_trough_after_peak_date":"2024-01-26","case_role":"false_positive_control","outcome_label":"counterexample","profile_verdict":"current_profile_false_positive","evidence_family":"premium_EV_P5_record_quarter_without_forward_utilization_margin_bridge","evidence_summary":"Q2 2023 revenue and operating profit were record Q2 levels, with Automotive & ESS sales/profit helped by premium vehicles and P5; however the later price path shows this evidence sat near a cycle peak.","evidence_url":"https://news.samsungsdi.com/global/articleView?seq=51","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false,"score_simulation":{"raw_component_scores_before":{"contract_backlog":5,"utilization_bridge":5,"ampc_quality":3,"ex_subsidy_margin":5,"customer_pull":6,"revision_quality":5,"execution_risk_inverse":4,"accounting_trust":6},"weighted_score_before":74,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_backlog":5,"utilization_bridge":3,"ampc_quality":2,"ex_subsidy_margin":3,"customer_pull":5,"revision_quality":3,"execution_risk_inverse":2,"accounting_trust":5},"weighted_score_after":55,"stage_label_after":"Stage1/Watch","changed_component_axes":["utilization_bridge","ampc_quality","ex_subsidy_margin","execution_risk_inverse","accounting_trust"],"residual_label":"record_quarter_language_without_forward_demand_bridge_is_not_actionable"},"calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger_result","research_file":"e2r_stock_web_v12_residual_round_R3_loop_199_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","research_mode":"post_calibrated_residual_historical_research_v12","selected_round":"R3","selected_loop":199,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_JV_AMPC_UTILIZATION_OFFSET_QUALITY_REPAIR","hard_duplicate_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|Stage4B|2024-01-30","case_id":"C13_SDI_2023FY_Q4_RAW_MATERIAL_PRESSURE_LOCAL_4B","symbol":"006400","company":"Samsung SDI","trigger_type":"Stage4B","trigger_date":"2024-01-30","entry_date":"2024-01-30","entry_price":374500,"actual_1D_OHLCV":{"d":"2024-01-30","o":383500,"h":390000,"l":373500,"c":374500,"v":524836},"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":["d","o","h","l","c","v","a","mc","s","m"],"corporate_action_candidate_overlap_180D":false,"corporate_action_note":"profile candidates 1996-01-03, 1998-11-03, 2014-07-15; no overlap with 2024-01-30 +180D","insufficient_forward_window_180D":false,"forward_available_tradable_days":499},"MFE_30D_pct":25.1,"MAE_30D_pct":-3.07,"MFE_90D_pct":32.04,"MAE_90D_pct":-3.07,"MFE_180D_pct":32.04,"MAE_180D_pct":-21.36,"peak_180D_date":"2024-03-25","peak_180D_price":494500,"trough_180D_date":"2024-08-05","trough_180D_price":294500,"drawdown_after_peak_pct":-40.44,"drawdown_trough_after_peak_date":"2024-08-05","case_role":"reversible_weakness_guardrail","outcome_label":"guardrail_success","profile_verdict":"current_profile_correct_local_4B","evidence_family":"annual_EV_battery_growth_but_Q4_raw_material_margin_pressure","evidence_summary":"FY2023 battery results were strong, with EV battery revenue and operating profit up sharply, but Q4 revenue/profit declined and raw-material-price effects pressured the energy business.","evidence_url":"https://samsungsdi.com/sdi-now/sdi-news/3502.html?idx=3502","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false,"score_simulation":{"raw_component_scores_before":{"contract_backlog":5,"utilization_bridge":4,"ampc_quality":2,"ex_subsidy_margin":4,"customer_pull":5,"revision_quality":3,"execution_risk_inverse":5,"accounting_trust":6},"weighted_score_before":62,"stage_label_before":"Stage2/Watch","raw_component_scores_after":{"contract_backlog":5,"utilization_bridge":4,"ampc_quality":2,"ex_subsidy_margin":3,"customer_pull":5,"revision_quality":3,"execution_risk_inverse":4,"accounting_trust":5},"weighted_score_after":57,"stage_label_after":"Stage4B","changed_component_axes":["utilization_bridge","ampc_quality","ex_subsidy_margin","execution_risk_inverse","accounting_trust"],"residual_label":"q4_margin_pressure_should_warn_but_annual_growth_offset_blocks_hard_4C"},"calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger_result","research_file":"e2r_stock_web_v12_residual_round_R3_loop_199_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","research_mode":"post_calibrated_residual_historical_research_v12","selected_round":"R3","selected_loop":199,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_JV_AMPC_UTILIZATION_OFFSET_QUALITY_REPAIR","hard_duplicate_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|051910|Stage2|2023-12-20","case_id":"C13_LGCHEM_2023_TENNESSEE_CATHODE_LONG_LEAD_CAPEX","symbol":"051910","company":"LG Chem","trigger_type":"Stage2","trigger_date":"2023-12-20","entry_date":"2023-12-20","entry_price":504000,"actual_1D_OHLCV":{"d":"2023-12-20","o":502000,"h":507000,"l":501000,"c":504000,"v":197344},"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051910/2023.csv","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":["d","o","h","l","c","v","a","mc","s","m"],"corporate_action_candidate_overlap_180D":false,"corporate_action_note":"no corporate-action candidate overlap was used for entry~180D validation window","insufficient_forward_window_180D":false,"forward_available_tradable_days":525},"MFE_30D_pct":0.6,"MAE_30D_pct":-23.91,"MFE_90D_pct":3.17,"MAE_90D_pct":-27.38,"MFE_180D_pct":3.17,"MAE_180D_pct":-47.72,"peak_180D_date":"2024-02-19","peak_180D_price":520000,"trough_180D_date":"2024-08-05","trough_180D_price":263500,"drawdown_after_peak_pct":-49.33,"drawdown_trough_after_peak_date":"2024-08-05","case_role":"long_lead_capex_false_positive","outcome_label":"counterexample","profile_verdict":"current_profile_false_positive","evidence_family":"Tennessee_cathode_capex_2026_start_without_near_term_utilization","evidence_summary":"LG Chem broke ground on a Tennessee cathode plant, targeting 60,000 tons annual capacity and 2026 production, with GM/Toyota supply context. The evidence is real but long-lead rather than near-term utilization.","evidence_url":"https://www.lgcorp.com/media/release/27138","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false,"score_simulation":{"raw_component_scores_before":{"contract_backlog":6,"utilization_bridge":2,"ampc_quality":2,"ex_subsidy_margin":2,"customer_pull":5,"revision_quality":3,"execution_risk_inverse":4,"accounting_trust":6},"weighted_score_before":72,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_backlog":6,"utilization_bridge":1,"ampc_quality":1,"ex_subsidy_margin":1,"customer_pull":4,"revision_quality":2,"execution_risk_inverse":2,"accounting_trust":5},"weighted_score_after":50,"stage_label_after":"Stage1/Watch","changed_component_axes":["utilization_bridge","ampc_quality","ex_subsidy_margin","execution_risk_inverse","accounting_trust"],"residual_label":"long_lead_2026_capacity_should_not_trigger_actionable_2023_entry"},"calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger_result","research_file":"e2r_stock_web_v12_residual_round_R3_loop_199_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","research_mode":"post_calibrated_residual_historical_research_v12","selected_round":"R3","selected_loop":199,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_JV_AMPC_UTILIZATION_OFFSET_QUALITY_REPAIR","hard_duplicate_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|011790|Stage2-Actionable|2023-08-07","case_id":"C13_SKC_2023_SKNEXILIS_VARTA_COPPER_FOIL_DEAL","symbol":"011790","company":"SKC","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-07","entry_date":"2023-08-07","entry_price":96000,"actual_1D_OHLCV":{"d":"2023-08-07","o":98300,"h":99800,"l":95700,"c":96000,"v":226633},"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":["d","o","h","l","c","v","a","mc","s","m"],"corporate_action_candidate_overlap_180D":false,"corporate_action_note":"profile candidates 1998-01-03 and 2001-12-21; no overlap with 2023-08-07 +180D","insufficient_forward_window_180D":false,"forward_available_tradable_days":583},"MFE_30D_pct":9.9,"MAE_30D_pct":-18.75,"MFE_90D_pct":9.9,"MAE_90D_pct":-29.17,"MFE_180D_pct":55.94,"MAE_180D_pct":-29.17,"peak_180D_date":"2024-04-09","peak_180D_price":149700,"trough_180D_date":"2023-10-23","trough_180D_price":68000,"drawdown_after_peak_pct":-29.73,"drawdown_trough_after_peak_date":"2024-04-26","case_role":"high_MAE_true_late_winner_control","outcome_label":"positive_control_high_MAE","profile_verdict":"current_profile_correct_but_green_blocked","evidence_family":"exclusive_copper_foil_customer_supply_deal","evidence_summary":"SK Nexilis secured an exclusive copper foil supply deal for Varta EV batteries. The row shows a painful initial MAE but eventual 180D upside, so C13 should not treat high MAE alone as a Stage2 blocker.","evidence_url":"https://en.yna.co.kr/view/AEN20230807002300320","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false,"score_simulation":{"raw_component_scores_before":{"contract_backlog":7,"utilization_bridge":5,"ampc_quality":1,"ex_subsidy_margin":3,"customer_pull":7,"revision_quality":4,"execution_risk_inverse":4,"accounting_trust":6},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_backlog":7,"utilization_bridge":5,"ampc_quality":1,"ex_subsidy_margin":2,"customer_pull":7,"revision_quality":3,"execution_risk_inverse":3,"accounting_trust":6},"weighted_score_after":71,"stage_label_after":"Stage2-Actionable high-MAE capped","changed_component_axes":["utilization_bridge","ampc_quality","ex_subsidy_margin","execution_risk_inverse","accounting_trust"],"residual_label":"direct_customer_supply_can_be_true_stage2_even_with_high_MAE_but_green_blocker_stays"},"calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger_result","research_file":"e2r_stock_web_v12_residual_round_R3_loop_199_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","research_mode":"post_calibrated_residual_historical_research_v12","selected_round":"R3","selected_loop":199,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_JV_AMPC_UTILIZATION_OFFSET_QUALITY_REPAIR","hard_duplicate_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|247540|Stage2|2023-12-04","case_id":"C13_ECOPROBM_2023_SDI_44T_SUPPLY_CYCLE_PEAK","symbol":"247540","company":"EcoPro BM","trigger_type":"Stage2","trigger_date":"2023-12-04","entry_date":"2023-12-04","entry_price":323000,"actual_1D_OHLCV":{"d":"2023-12-04","o":320000,"h":354000,"l":307500,"c":323000,"v":6062155},"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":["d","o","h","l","c","v","a","mc","s","m"],"corporate_action_candidate_overlap_180D":false,"corporate_action_note":"profile candidates 2022-06-27 and 2022-07-15; no overlap with 2023-12-04 +180D","insufficient_forward_window_180D":false,"forward_available_tradable_days":262},"MFE_30D_pct":9.6,"MAE_30D_pct":-17.96,"MFE_90D_pct":9.6,"MAE_90D_pct":-34.67,"MFE_180D_pct":9.6,"MAE_180D_pct":-49.23,"peak_180D_date":"2023-12-04","peak_180D_price":354000,"trough_180D_date":"2024-08-05","trough_180D_price":164000,"drawdown_after_peak_pct":-53.67,"drawdown_trough_after_peak_date":"2024-08-05","case_role":"single_large_supply_deal_cycle_peak_counterexample","outcome_label":"counterexample","profile_verdict":"current_profile_false_positive","evidence_family":"single_large_cathode_supply_contract_customer_concentration","evidence_summary":"EcoPro BM announced a five-year KRW44T cathode supply deal to Samsung SDI. The contract was large and real, but the stock-web path marks it as a cycle-peak false positive without near-term margin/utilization confirmation.","evidence_url":"https://koreajoongangdaily.joins.com/news/2023-12-03/business/industry/EcoPro-BM-secures-34-billion-deal-as-Samsung-SDIs-cathode-supplier/1926748","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false,"score_simulation":{"raw_component_scores_before":{"contract_backlog":8,"utilization_bridge":3,"ampc_quality":1,"ex_subsidy_margin":3,"customer_pull":7,"revision_quality":4,"execution_risk_inverse":3,"accounting_trust":6},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_backlog":8,"utilization_bridge":1,"ampc_quality":1,"ex_subsidy_margin":1,"customer_pull":5,"revision_quality":2,"execution_risk_inverse":1,"accounting_trust":5},"weighted_score_after":54,"stage_label_after":"Stage1/Watch","changed_component_axes":["utilization_bridge","ampc_quality","ex_subsidy_margin","execution_risk_inverse","accounting_trust"],"residual_label":"large_contract_size_without_margin_and_demand_bridge_is_cycle_peak_false_positive"},"calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger_result","research_file":"e2r_stock_web_v12_residual_round_R3_loop_199_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","research_mode":"post_calibrated_residual_historical_research_v12","selected_round":"R3","selected_loop":199,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_JV_AMPC_UTILIZATION_OFFSET_QUALITY_REPAIR","hard_duplicate_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|247540|Stage4B|2024-02-07","case_id":"C13_ECOPROBM_2024_CAM7_JV_CONTRACT_OFFSET_4B","symbol":"247540","company":"EcoPro BM","trigger_type":"Stage4B","trigger_date":"2024-02-07","entry_date":"2024-02-07","entry_price":230500,"actual_1D_OHLCV":{"d":"2024-02-07","o":226000,"h":250000,"l":225500,"c":230500,"v":2845259},"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":["d","o","h","l","c","v","a","mc","s","m"],"corporate_action_candidate_overlap_180D":false,"corporate_action_note":"profile candidates 2022-06-27 and 2022-07-15; no overlap with 2024-02-07 +180D","insufficient_forward_window_180D":false,"forward_available_tradable_days":218},"MFE_30D_pct":21.69,"MAE_30D_pct":-2.17,"MFE_90D_pct":29.5,"MAE_90D_pct":-21.26,"MFE_180D_pct":29.5,"MAE_180D_pct":-35.49,"peak_180D_date":"2024-03-27","peak_180D_price":298500,"trough_180D_date":"2024-09-10","trough_180D_price":148700,"drawdown_after_peak_pct":-50.18,"drawdown_trough_after_peak_date":"2024-09-10","case_role":"contract_offset_local_4B_guardrail","outcome_label":"guardrail_success","profile_verdict":"current_profile_correct_4B_not_4C","evidence_family":"JV_and_supply_contract_offset_but_customer_concentration_and_demand_risk","evidence_summary":"The Samsung SDI JV/supply relationship remained a real offset, but the forward path still showed a deep drawdown. This is a local 4B watch, not automatic hard 4C while contract offset remains explicit.","evidence_url":"https://www.koreatimes.co.kr/business/companies/20221021/ecopro-bm-samsung-sdi-jv-completes-construction-of-new-cathode-plant-in-pohang","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false,"score_simulation":{"raw_component_scores_before":{"contract_backlog":7,"utilization_bridge":2,"ampc_quality":1,"ex_subsidy_margin":2,"customer_pull":5,"revision_quality":2,"execution_risk_inverse":2,"accounting_trust":5},"weighted_score_before":61,"stage_label_before":"Stage2/Watch","raw_component_scores_after":{"contract_backlog":7,"utilization_bridge":2,"ampc_quality":1,"ex_subsidy_margin":1,"customer_pull":4,"revision_quality":2,"execution_risk_inverse":1,"accounting_trust":5},"weighted_score_after":56,"stage_label_after":"Stage4B","changed_component_axes":["utilization_bridge","ampc_quality","ex_subsidy_margin","execution_risk_inverse","accounting_trust"],"residual_label":"contract_offset_blocks_hard_4C_but_demand_risk_keeps_4B_watch"},"calibration_usable":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"batch_aggregate","research_file":"e2r_stock_web_v12_residual_round_R3_loop_199_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","selected_round":"R3","selected_loop":199,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_JV_AMPC_UTILIZATION_OFFSET_QUALITY_REPAIR","new_independent_case_count":8,"new_independent_trigger_count":8,"same_symbol_new_trigger_count":3,"unique_symbol_count":5,"calibration_usable_case_count":8,"positive_case_count":2,"counterexample_case_count":3,"guardrail_case_count":3,"current_profile_error_count":3,"source_proxy_only_count":0,"evidence_url_pending_count":0,"missing_required_mfe_mae_count":0,"corporate_action_contaminated_180D_count":0,"insufficient_forward_window_180D_count":0,"avg_MFE_90D_pct":16.67,"avg_MAE_90D_pct":-20.91,"avg_MFE_180D_pct":22.6,"avg_MAE_180D_pct":-33.31,"new_independent_ratio":1.0,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"shadow_weight_audit","research_file":"e2r_stock_web_v12_residual_round_R3_loop_199_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_weight_before":{"eps_fcf_explosion":20,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":10,"information_confidence":16},"profile_weight_after_shadow":{"eps_fcf_explosion":20,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":10,"information_confidence":16},"weight_delta_proposed":false,"guardrail_overlay_candidate":{"name":"C13_AMPC_JV_UTILIZATION_QUALITY_SPLIT","stage2_actionable_requires":"AMPC/IRA/JV headline plus at least one of utilization, customer pull/call-off, shipment schedule, ex-subsidy margin, or order/backlog conversion.","green_blocker":"AMPC credit exceeds or masks reported operating profit, or 90D MAE is worse than -25% without a second bridge.","hard_4c_requires":"utilization collapse or customer/JV impairment plus weak offset quality; demand slowdown alone is 4B/watch when recovery guidance or ESS/non-EV offset is explicit."},"production_scoring_changed":false,"shadow_weight_only":true}
```
## 13. Batch Ingest Self-Audit

```text
research_file: e2r_stock_web_v12_residual_round_R3_loop_199_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
selected_round: R3
selected_loop: 199
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: BATTERY_JV_AMPC_UTILIZATION_OFFSET_QUALITY_REPAIR
batch_new_independent_case_count: 8
batch_new_independent_trigger_count: 8
unique_symbol_count: 5
same_symbol_new_trigger_count: 3
positive_case_count: 2
counterexample_case_count: 3
guardrail_case_count: 3
current_profile_error_count: 3
calibration_usable_case_count: 8
calibration_usable_trigger_count: 8
jsonl_trigger_row_count: 8
source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_entry_price_count: 0
missing_required_entry_date_count: 0
missing_required_mfe_mae_count: 0
insufficient_forward_window_180D_count: 0
corporate_action_contaminated_180D_count: 0
duplicate_hard_key_count_in_batch: 0
new_independent_ratio: 1.00
price_source_validation_status: pass
stage_transition_analysis_included: true
raw_component_breakdown_included: true
shadow_weight_before_after_included: true
production_scoring_changed: false
shadow_weight_only: true
coding_agent_handoff_embedded_but_not_executed: true
```
## 14. Deferred Coding-Agent Handoff Prompt — Embedded, Not Executed

```text
You are the stock_agent coding agent. Do not act on this handoff unless explicitly invoked by the user in a separate coding session.

Candidate only: inspect v12 calibration aggregate rows for C13_BATTERY_JV_UTILIZATION_AMPC_IRA and test whether a non-production guard overlay named C13_AMPC_JV_UTILIZATION_QUALITY_SPLIT improves Stage2-Actionable precision without hurting true positive C13 rows.

Do not change production scoring by default. Start with tests around the parsed JSONL fields: evidence_family, utilization_bridge, ex_subsidy_margin, customer_pull, and hard_4c_irreversibility. Any implementation must keep stage3_green_not_loosened_by_v12 and price_only_blowoff_blocks_positive_stage intact.
```
## 15. Next Research State

```text
completed_round: R3
completed_loop: 199
completed_large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
completed_canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
completed_fine_archetype_id: BATTERY_JV_AMPC_UTILIZATION_OFFSET_QUALITY_REPAIR
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP_4C_TIMING_DIRECT_URL_REPAIR
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE_FCF_COUNTEREXAMPLE_REPAIR
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA_UTILIZATION_DIRECT_ROW_REPAIR
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_CONVERSION_REPAIR
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
```
