# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R3_loop_85_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
selected_round: R3
selected_loop: 85
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: CATHODE_JV_UTILIZATION_IRA_CUSTOMER_CAPACITY_4B_WATCH
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 3 independent cases, 2 C13 utilization/capacity success paths, and 1 CAPA/IRA false-positive counterexample for R3/L3/C13.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C13:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R3 -> L3_BATTERY_EV_GREEN_MOBILITY
C13 -> C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

C13 is the battery “factory economics” archetype. A JV, IRA/AMPC label, or CAPA plan is only a route marker. The calibration bridge is whether capacity is actually utilized, whether subsidy economics turn into cash, and whether margin/revision follows.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C13 current rows | 27 |
| C13 current symbols | 17 |
| C13 good/bad Stage2 | 6 / 6 |
| C13 4B/4C | 3 / 3 |
| C13 URL pending/proxy | 24 / 18 |
| top covered symbols | 373220, 393890, 006400, 014820, 051910, 096770 |

Selected symbols avoid the C13 top-covered symbols:

| symbol | company | status |
|---|---|---|
| 066970 | 엘앤에프 | new C13 symbol versus top-covered C13 list |
| 005070 | 코스모신소재 | new C13 symbol versus top-covered C13 list |
| 450080 | 에코프로머티 | new C13 symbol versus top-covered C13 list |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 066970 / 2024-02-14 | true | true | clean_180D_window | true |
| 005070 / 2024-02-02 | true | true | clean_180D_window | true |
| 450080 / 2024-02-13 | true | true | clean_180D_window | true |

Corporate-action notes:

- 엘앤에프 has corporate-action candidates only in 2016 and 2021; selected 2024 window is clean.
- 코스모신소재 has corporate-action candidates before 2020; selected 2024 window is clean.
- 에코프로머티 has zero corporate-action candidates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| CATHODE_JV_UTILIZATION_IRA_CUSTOMER_CAPACITY_4B_WATCH | C13 | cathode/JV/IRA route works only if utilization and cash bridge follow |
| CATHODE_CAPA_UTILIZATION_CUSTOMER_RAMP_4B_WATCH | C13 | CAPA/customer ramp can open Stage2A but needs utilization/cash conversion |
| PRECURSOR_CAPA_IRA_UTILIZATION_BRIDGE_ABSENT_FALSE_POSITIVE | C13 | precursor/CAPA/IRA label without utilization bridge is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C13_LNF_066970_2024_02_14_CATHODE_JV_UTILIZATION_IRA_RERATING | 066970 | 엘앤에프 | 4B_overlay_success | positive | JV/IRA utilization route produced useful MFE, then deep drawdown |
| C13_COSMO_005070_2024_02_02_CATHODE_CAPA_UTILIZATION_RERATING | 005070 | 코스모신소재 | high_mfe_success | positive | CAPA/utilization route produced MFE with low early MAE |
| C13_ECOPROMAT_450080_2024_02_13_PRECURSOR_CAPA_UTILIZATION_FALSE_POSITIVE | 450080 | 에코프로머티 | failed_rerating | counterexample | CAPA/IRA label had nearly no MFE and severe MAE without utilization/cash bridge |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |

Minimum conditions pass:

```text
positive_case_count >= 1
counterexample_count >= 1
calibration_usable_case_count >= 3
new_independent_case_ratio = 1.00
```

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 066970 | source_proxy_only | cathode/JV utilization and IRA localization route; cash bridge pending | required before promotion |
| 005070 | source_proxy_only | CAPA/customer ramp and utilization route; cash bridge pending | required before promotion |
| 450080 | source_proxy_only | precursor/CAPA/IRA theme but utilization/cash bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 066970 | atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv | atlas/symbol_profiles/066/066970.json |
| 005070 | atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv | atlas/symbol_profiles/005/005070.json |
| 450080 | atlas/ohlcv_tradable_by_symbol_year/450/450080/2024.csv | atlas/symbol_profiles/450/450080.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| LNF_066970_2024_02_14_STAGE2A_CATHODE_JV_UTILIZATION_IRA | Stage2-Actionable | 2024-02-14 | 2024-02-14 | 144700 | cathode/JV/utilization/IRA localization route |
| COSMO_005070_2024_02_02_STAGE2A_CATHODE_CAPA_UTILIZATION | Stage2-Actionable | 2024-02-02 | 2024-02-02 | 146500 | cathode CAPA/customer ramp/utilization route |
| ECOPROMAT_450080_2024_02_13_STAGE2_FALSE_POSITIVE_PRECURSOR_CAPA_IRA | Stage2 | 2024-02-13 | 2024-02-13 | 209500 | precursor/CAPA/IRA theme without utilization/cash bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 066970 | 2024-02-14 | 144700 | 37.53 | -4.56 | 37.53 | -7.32 | 37.53 | -42.71 | 2024-03-25 | 199000 | -58.34 |
| 005070 | 2024-02-02 | 146500 | 32.63 | -4.44 | 32.63 | -4.44 | 32.63 | -31.67 | 2024-02-21 | 194300 | -48.48 |
| 450080 | 2024-02-13 | 209500 | 0.95 | -38.33 | 0.95 | -63.96 | 0.95 | -63.96 | 2024-02-14 | 211500 | -64.30 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 066970 | Stage2A/Yellow possible; 4B after rerating | useful MFE then deep 180D drawdown | current_profile_4B_too_late |
| 005070 | Stage2A possible; Green needs cash/utilization proof | useful MFE and then later drawdown | current_profile_4B_too_late |
| 450080 | Stage2 risk if CAPA/IRA label is over-credited | almost no MFE and severe MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C13 interpretation:

- Stage2A can work when JV/CAPA/IRA narrative is tied to customer capacity or utilization.
- Yellow/Green require utilization, AMPC/IRA cash capture, margin bridge, revision, and FCF conversion.
- CAPA or IRA labels without utilization/cash bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 066970 | 1.00 | 1.00 | utilization bridge pending / valuation | good 4B audit after cathode JV/IRA rerating |
| 005070 | 1.00 | 1.00 | utilization bridge pending / valuation | Stage2A ok; Green blocked until cash conversion |
| 450080 | 1.00 | 1.00 | price-only CAPA/IRA peak | not Stage3; should be false-positive guardrail |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 066970 | thesis_break_watch_only | not hard 4C, but 4B cap needed after rerating |
| 005070 | thesis_break_watch_only | not hard 4C, but cash-conversion audit needed |
| 450080 | hard_4c_late | missing utilization/cash bridge should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L3_BATTERY_EV_GREEN_MOBILITY
confidence = low_to_medium
```

Candidate:

> In L3 battery material names, JV/CAPA/IRA/AMPC labels can open Stage2A only if utilization, customer capacity, or cash-subsidy conversion is visible. Without utilization and margin/FCF bridge, cap at Stage1/Stage2-watch and route to C13 false-positive or 4C-watch.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
confidence = low_to_medium
```

Candidate C13 rule:

```text
C13_utilization_cash_bridge_required =
  jv_or_capa_or_ampc_ira_label
  AND (utilization_confirmation OR customer_capacity_pullthrough OR ampc_cash_capture OR margin_bridge OR confirmed_revision)

if jv_capa_ira_label and utilization_cash_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 25 and drawdown_after_peak < -40:
    add C13_peak_proximity_4B_audit = true

if MFE_90D < 5 and MAE_90D < -30:
    classify_as C13_capa_ira_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 23.7 | -25.24 | 23.7 | -46.11 | 1 | useful but C13 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 23.7 | -25.24 | 23.7 | -46.11 | 1 | over-credits CAPA/IRA labels |
| P1 sector_specific_candidate_profile | L3 | 2 promoted + 1 guard | 35.08 | -5.88 | 35.08 | -37.19 | 0 | better after utilization/cash bridge gate |
| P2 canonical_archetype_candidate_profile | C13 | 2 promoted + 1 guard | 35.08 | -5.88 | 35.08 | -37.19 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C13 guard | 2 promoted + 1 guard | 35.08 | -5.88 | 35.08 | -37.19 | 0 | adds CAPA/IRA false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 066970 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 005070 | Stage2A aligned; Green block needed | current_profile_4B_too_late |
| 450080 | Stage2 false positive if utilization bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | mixed C13 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | 27 -> projected 30 rows; reaches minimum stability threshold |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_4B_too_late
  - current_profile_false_positive
new_axis_proposed: C13_utilization_cash_bridge_required|C13_peak_proximity_4B_audit|C13_capa_ira_false_positive_guardrail
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Uses stock-web tradable OHLC rows.
- Uses manifest max_date 2026-02-20.
- Uses clean 180D windows.
- Uses C13 Priority 0 coverage gap.
- Uses three symbols not in the C13 top-covered symbol list.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C13_utilization_cash_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"450080 shows CAPA/IRA label can fail without utilization/cash bridge while 066970/005070 worked only as Stage2A with later 4B audit","blocks 450080 false positive while preserving 066970/005070 Stage2A","LNF_066970_2024_02_14_STAGE2A_CATHODE_JV_UTILIZATION_IRA|COSMO_005070_2024_02_02_STAGE2A_CATHODE_CAPA_UTILIZATION|ECOPROMAT_450080_2024_02_13_STAGE2_FALSE_POSITIVE_PRECURSOR_CAPA_IRA",3,3,1,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C13_peak_proximity_4B_audit,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"066970/005070 positive Stage2A cases still needed 4B audit after rerating and later drawdown","adds 4B audit after C13 MFE when utilization/cash bridge remains partial","LNF_066970_2024_02_14_STAGE2A_CATHODE_JV_UTILIZATION_IRA|COSMO_005070_2024_02_02_STAGE2A_CATHODE_CAPA_UTILIZATION",2,2,0,low_to_medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C13_capa_ira_false_positive_guardrail,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"450080 had almost no forward MFE and severe MAE despite CAPA/IRA theme","requires utilization/AMPC cash capture before Stage2/Yellow promotion","ECOPROMAT_450080_2024_02_13_STAGE2_FALSE_POSITIVE_PRECURSOR_CAPA_IRA",1,1,1,low_to_medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C13_LNF_066970_2024_02_14_CATHODE_JV_UTILIZATION_IRA_RERATING","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"CATHODE_JV_UTILIZATION_IRA_CUSTOMER_CAPACITY_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"LNF_066970_2024_02_14_STAGE2A_CATHODE_JV_UTILIZATION_IRA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"cathode/JV/utilization and IRA route captured roughly 37% MFE, but later drawdown required 4B utilization audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C13 symbol versus top-covered C13 list; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C13_COSMO_005070_2024_02_02_CATHODE_CAPA_UTILIZATION_RERATING","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"CATHODE_CAPA_UTILIZATION_CUSTOMER_RAMP_4B_WATCH","case_type":"high_mfe_success","positive_or_counterexample":"positive","best_trigger":"COSMO_005070_2024_02_02_STAGE2A_CATHODE_CAPA_UTILIZATION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"capacity/utilization rerating captured 32% MFE with low early MAE, but later drawdown shows AMPC/JV/cash conversion must be audited","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C13 symbol; source_proxy_only evidence"}
{"row_type":"case","case_id":"C13_ECOPROMAT_450080_2024_02_13_PRECURSOR_CAPA_UTILIZATION_FALSE_POSITIVE","symbol":"450080","company_name":"에코프로머티","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"PRECURSOR_CAPA_IRA_UTILIZATION_BRIDGE_ABSENT_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"ECOPROMAT_450080_2024_02_13_STAGE2_FALSE_POSITIVE_PRECURSOR_CAPA_IRA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"precursor/CAPA/IRA narrative had almost no forward MFE and then deep 90D/180D MAE when utilization/cash bridge failed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C13 symbol; counterexample for CAPA/IRA label without utilization and cash conversion"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"LNF_066970_2024_02_14_STAGE2A_CATHODE_JV_UTILIZATION_IRA","case_id":"C13_LNF_066970_2024_02_14_CATHODE_JV_UTILIZATION_IRA_RERATING","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"CATHODE_JV_UTILIZATION_IRA_CUSTOMER_CAPACITY_4B_WATCH","sector":"battery / EV / green mobility","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":144700.0,"evidence_available_at_that_date":"source_proxy_only: cathode customer/JV utilization route, IRA localization narrative, and recovery in battery-material relative strength; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["cathode_customer_route","jv_utilization_route","ira_localization_route","relative_strength"],"stage3_evidence_fields":["utilization_bridge_partial","revision_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","peak_proximity","battery_materials_positioning"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":37.53,"MFE_90D_pct":37.53,"MFE_180D_pct":37.53,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.56,"MAE_90D_pct":-7.32,"MAE_180D_pct":-42.71,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":199000.0,"drawdown_after_peak_pct":-58.34,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_4B_audit_after_cathode_jv_utilization_rerating","four_b_evidence_type":["valuation_rerating","utilization_bridge_pending"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_mfe_with_4b_drawdown","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C13_066970_2024_02_14_144700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"COSMO_005070_2024_02_02_STAGE2A_CATHODE_CAPA_UTILIZATION","case_id":"C13_COSMO_005070_2024_02_02_CATHODE_CAPA_UTILIZATION_RERATING","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"CATHODE_CAPA_UTILIZATION_CUSTOMER_RAMP_4B_WATCH","sector":"battery / EV / green mobility","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":146500.0,"evidence_available_at_that_date":"source_proxy_only: cathode capacity expansion, customer ramp, and IRA localization route; utilization/cash conversion bridge partial; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["cathode_capacity_route","customer_ramp_route","utilization_route","ira_localization_route"],"stage3_evidence_fields":["utilization_bridge_partial","margin_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv","profile_path":"atlas/symbol_profiles/005/005070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":32.63,"MFE_90D_pct":32.63,"MFE_180D_pct":32.63,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.44,"MAE_90D_pct":-4.44,"MAE_180D_pct":-31.67,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":194300.0,"drawdown_after_peak_pct":-48.48,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_stage2a_but_4B_required_without_utilization_cash_bridge","four_b_evidence_type":["valuation_rerating","cash_conversion_pending"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_mfe_with_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C13_005070_2024_02_02_146500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"ECOPROMAT_450080_2024_02_13_STAGE2_FALSE_POSITIVE_PRECURSOR_CAPA_IRA","case_id":"C13_ECOPROMAT_450080_2024_02_13_PRECURSOR_CAPA_UTILIZATION_FALSE_POSITIVE","symbol":"450080","company_name":"에코프로머티","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"PRECURSOR_CAPA_IRA_UTILIZATION_BRIDGE_ABSENT_FALSE_POSITIVE","sector":"battery / EV / green mobility","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":209500.0,"evidence_available_at_that_date":"source_proxy_only: precursor/CAPA/IRA theme and battery-material beta visible, but utilization, AMPC cash capture, and margin bridge absent","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["precursor_capa_narrative","ira_localization_theme","battery_materials_beta"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["price_only_peak","valuation_blowoff","utilization_bridge_absent"],"stage4c_evidence_fields":["utilization_bridge_absent","cash_conversion_absent","margin_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/450/450080/2024.csv","profile_path":"atlas/symbol_profiles/450/450080.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.95,"MFE_90D_pct":0.95,"MFE_180D_pct":0.95,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-38.33,"MAE_90D_pct":-63.96,"MAE_180D_pct":-63.96,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-14","peak_price":211500.0,"drawdown_after_peak_pct":-64.3,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_capa_ira_peak_without_utilization_cash_bridge_not_stage3","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_utilization_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C13_450080_2024_02_13_209500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_LNF_066970_2024_02_14_CATHODE_JV_UTILIZATION_IRA_RERATING","trigger_id":"LNF_066970_2024_02_14_STAGE2A_CATHODE_JV_UTILIZATION_IRA","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":3,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable / Yellow-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":3,"valuation_repricing_score":3,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage2-Actionable with utilization/4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"JV/IRA route can open Stage2A, but Green requires utilization, AMPC/cash capture, and revision bridge.","MFE_90D_pct":37.53,"MAE_90D_pct":-7.32,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_COSMO_005070_2024_02_02_CATHODE_CAPA_UTILIZATION_RERATING","trigger_id":"COSMO_005070_2024_02_02_STAGE2A_CATHODE_CAPA_UTILIZATION","symbol":"005070","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable with cash-conversion audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Capacity/utilization route produced good MFE, but late drawdown says cash conversion and utilization proof must cap Yellow/Green.","MFE_90D_pct":32.63,"MAE_90D_pct":-4.44,"score_return_alignment_label":"stage2_good_green_block_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_ECOPROMAT_450080_2024_02_13_PRECURSOR_CAPA_UTILIZATION_FALSE_POSITIVE","trigger_id":"ECOPROMAT_450080_2024_02_13_STAGE2_FALSE_POSITIVE_PRECURSOR_CAPA_IRA","symbol":"450080","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":4,"valuation_repricing_score":7,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":2,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":45,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["contract_score","backlog_visibility_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C13 should not give Stage2 credit to CAPA/IRA labels without utilization, AMPC/cash capture, margin, or revision bridge.","MFE_90D_pct":0.95,"MAE_90D_pct":-63.96,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R3
completed_loop = 85
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C24_BIO_TRIAL_DATA_EVENT_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION, C02_POWER_GRID_DATACENTER_CAPEX
```

If this loop is accepted, C13 moves from 27 to a projected 30 rows and reaches the minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C13 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/450/450080/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/066/066970.json
  - atlas/symbol_profiles/005/005070.json
  - atlas/symbol_profiles/450/450080.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
