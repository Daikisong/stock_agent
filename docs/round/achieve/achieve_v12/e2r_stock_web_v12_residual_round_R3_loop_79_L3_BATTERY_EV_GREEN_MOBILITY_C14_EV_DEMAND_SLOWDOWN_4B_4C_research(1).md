# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R3_loop_79_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
selected_round: R3
selected_loop: 79
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: CATHODE_EV_DEMAND_SLOWDOWN_PRICE_PEAK_HARD_4C
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_4C_protection_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 3 independent cases, 2 protective hard-4C successes, and 1 false-4C counterexample for R3/L3/C14.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C14:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R3 -> L3_BATTERY_EV_GREEN_MOBILITY
C14 -> C14_EV_DEMAND_SLOWDOWN_4B_4C
```

C14 is not a generic “battery stock fell” bucket. It is a thesis-break / protection archetype. It should fire when EV demand slowdown is tied to utilization, call-off, customer delay, inventory/capacity imbalance, or margin bridge failure. Broad sector fear alone is not enough for hard 4C.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C14 current rows | 21 |
| C14 need to 30 | 9 |
| C14 need to 50 | 29 |
| C14 조사 포인트 | EV 수요 둔화, utilization, call-off, hard 4C 확인 |

This session locally generated C08/C09/C01/C07/C06/C10 loops before this file, so C14 is selected as the next under-covered Priority 0 archetype.

Selected symbols:

| symbol | company | status |
|---|---|---|
| 247540 | 에코프로비엠 | new local C14 symbol |
| 006400 | 삼성SDI | new local C14 symbol |
| 373220 | LG에너지솔루션 | new local C14 symbol |

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
| 247540 / 2024-03-25 | true | true | clean_180D_window | true |
| 006400 / 2024-03-25 | true | true | clean_180D_window | true |
| 373220 / 2024-04-08 | true | true | clean_180D_window | true |

Corporate-action notes:

- 에코프로비엠 has corporate-action candidates in 2022 only; selected 2024 window is clean.
- 삼성SDI has corporate-action candidates only before 2015; selected 2024 window is clean.
- LG에너지솔루션 has zero corporate-action candidates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| CATHODE_EV_DEMAND_SLOWDOWN_PRICE_PEAK_HARD_4C | C14 | cathode price peak plus demand/utilization/capacity risk routes to protective 4C |
| BATTERY_CELL_EV_DEMAND_SLOWDOWN_RELIEF_RALLY_FAIL | C14 | cell relief rally failed because demand/utilization bridge remained weak |
| CELL_LEADER_EV_SLOWDOWN_FALSE_HARD_4C_WITH_RECOVERY | C14 | broad EV fear without explicit call-off/utilization proof can over-block |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C14_ECOPROBM_247540_2024_03_25_EV_DEMAND_SLOWDOWN_HARD_4C_SUCCESS | 247540 | 에코프로비엠 | hard_4c_protection_success | positive | local peak had almost no MFE and deep 180D MAE |
| C14_SDI_006400_2024_03_25_EV_DEMAND_SLOWDOWN_RELIEF_RALLY_FAIL | 006400 | 삼성SDI | hard_4c_protection_success | positive | relief rally failed; 180D drawdown exceeded -50% |
| C14_LGES_373220_2024_04_08_EV_DEMAND_SLOWDOWN_FALSE_4C | 373220 | LG에너지솔루션 | failed_hard_4c_overblock | counterexample | broad EV fear alone would have over-blocked a later recovery path |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 3 |
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
| 247540 | source_proxy_only | EV slowdown plus cathode overcapacity/utilization risk | required before promotion |
| 006400 | source_proxy_only | EV cell demand slowdown plus relief-rally failure risk | required before promotion |
| 373220 | source_proxy_only | broad slowdown fear but call-off/utilization bridge unclear | required; useful as counterexample |

This loop does not use price-only evidence to promote Stage3. Protective 4C rows require non-price thesis-break evidence; the LGES row shows why broad fear alone should not hard-block.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 247540 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv | atlas/symbol_profiles/247/247540.json |
| 006400 | atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv | atlas/symbol_profiles/006/006400.json |
| 373220 | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv | atlas/symbol_profiles/373/373220.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| ECOPROBM_247540_2024_03_25_4C_EV_DEMAND_SLOWDOWN | 4C-Protective | 2024-03-25 | 2024-03-25 | 291000 | cathode overcapacity / EV demand slowdown / utilization risk |
| SDI_006400_2024_03_25_4C_EV_DEMAND_SLOWDOWN_RELIEF_RALLY_FAIL | 4C-Protective | 2024-03-25 | 2024-03-25 | 486000 | cell demand slowdown / relief-rally failure |
| LGES_373220_2024_04_08_FALSE_4C_EV_DEMAND_SLOWDOWN | 4C-FalsePositive | 2024-04-08 | 2024-04-08 | 373000 | broad EV slowdown fear without explicit utilization/call-off bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 247540 | 2024-03-25 | 291000 | 1.89 | -26.12 | 1.89 | -41.37 | 1.89 | -63.37 | 2024-03-25 | 296500 | -64.05 |
| 006400 | 2024-03-25 | 486000 | 1.75 | -16.26 | 1.75 | -27.78 | 1.75 | -50.93 | 2024-03-25 | 494500 | -51.77 |
| 373220 | 2024-04-08 | 373000 | 6.43 | -4.69 | 6.43 | -16.62 | 19.03 | -16.62 | 2024-10-08 | 444000 | -23.31 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 247540 | Stage2/4B-watch if slowdown evidence is underweighted | very low MFE, severe 180D MAE | current_profile_4C_too_late |
| 006400 | relief-rally Stage2 risk if demand slowdown is underweighted | very low MFE, severe 180D MAE | current_profile_4C_too_late |
| 373220 | hard 4C risk if broad EV fear is overgeneralized | later +19% 180D MFE with moderate MAE | current_profile_overprotective_4C |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C14 interpretation:

- Stage2/Yellows in battery names should be capped when utilization/call-off/customer demand bridge is broken.
- Hard 4C is justified when demand slowdown is tied to cathode overcapacity, utilization risk, customer delay, or margin bridge failure.
- Broad EV slowdown fear alone can be a false 4C; it needs a company-specific bridge.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 247540 | 1.00 | 1.00 | valuation / demand slowdown | local 4B aligned; hard 4C needed |
| 006400 | 1.00 | 1.00 | relief-rally / demand slowdown | local 4B aligned; hard 4C needed |
| 373220 | 0.84 | 1.00 | broad sector fear only | hard 4C would have been overprotective |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 247540 | hard_4c_success | demand/utilization/capacity risk correctly protected against large MAE |
| 006400 | hard_4c_success | relief rally should have been capped by demand slowdown guard |
| 373220 | false_4c_overblock | broad EV fear without call-off/utilization bridge should not hard-block |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L3_BATTERY_EV_GREEN_MOBILITY
confidence = low_to_medium
```

Candidate:

> In L3 battery/EV names, EV demand slowdown becomes a hard 4C only when it is attached to company-level utilization, call-off, customer delay, inventory/capacity imbalance, or margin bridge failure. Broad sector fear without that bridge should cap optimism but should not automatically hard-block cell leaders.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C14_EV_DEMAND_SLOWDOWN_4B_4C
confidence = low_to_medium
```

Candidate C14 rule:

```text
C14_hard_4c_bridge_required =
  ev_demand_slowdown
  AND (utilization_break OR customer_call_off OR inventory_overhang OR capacity_overbuild OR margin_bridge_failure)

if broad_ev_slowdown_fear and company_specific_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_route_hard_4C = true

if MFE_90D < 5 and MAE_90D < -25:
    classify_as C14_protective_4C_success

if MFE_180D > 15 and MAE_90D > -20:
    classify_as C14_false_4C_overblock
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false 4C | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 3.36 | -28.59 | 7.56 | -43.64 | 1 | needs bridge-specific C14 split |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 3.36 | -28.59 | 7.56 | -43.64 | 1 | over-credits relief rallies and broad fear |
| P1 sector_specific_candidate_profile | L3 | 2 protective + 1 watch | 1.82 | -34.58 | 1.82 | -57.15 | 0 | better after company-specific 4C bridge |
| P2 canonical_archetype_candidate_profile | C14 | 2 protective + 1 watch | 1.82 | -34.58 | 1.82 | -57.15 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C14 guard | 2 protective + 1 watch | 1.82 | -34.58 | 1.82 | -57.15 | 0 | avoids broad-fear hard 4C |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 247540 | protective 4C aligned; Stage2 would be false positive | current_profile_4C_too_late |
| 006400 | protective 4C aligned; relief-rally Stage2 would fail | current_profile_4C_too_late |
| 373220 | hard 4C overblocked recovery path | current_profile_overprotective_4C |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | mixed C14 fine ids | 2 | 1 | 2 | 3 | 3 | 0 | 3 | 3 | 3 | true | true | 21 -> projected 24 rows; still need 6 to reach 30 |

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
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - stage2_actionable_evidence_bonus
residual_error_types_found:
  - current_profile_4C_too_late
  - current_profile_overprotective_4C
new_axis_proposed: C14_hard_4c_company_specific_bridge_required|C14_false_4c_overblock_guard
existing_axis_strengthened:
  - hard_4c_thesis_break_routes_to_4c
  - price_only_blowoff_blocks_positive_stage
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
- Uses C14 Priority 0 coverage gap.
- Uses three local-new C14 symbols.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_hard_4c_company_specific_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"247540/006400 show demand slowdown plus utilization/capacity risk needs protective 4C, while 373220 shows broad fear alone can over-block","preserves protective 4C for high-MAE names while avoiding LGES false hard-4C","ECOPROBM_247540_2024_03_25_4C_EV_DEMAND_SLOWDOWN|SDI_006400_2024_03_25_4C_EV_DEMAND_SLOWDOWN_RELIEF_RALLY_FAIL|LGES_373220_2024_04_08_FALSE_4C_EV_DEMAND_SLOWDOWN",3,3,1,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C14_false_4c_overblock_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"373220 recovered despite broad EV fear because call-off/utilization bridge was not explicit","prevents broad sector fear from automatic hard 4C","LGES_373220_2024_04_08_FALSE_4C_EV_DEMAND_SLOWDOWN",1,1,1,low_to_medium,canonical_shadow_only,"counterexample guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C14_ECOPROBM_247540_2024_03_25_EV_DEMAND_SLOWDOWN_HARD_4C_SUCCESS","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"79","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_EV_DEMAND_SLOWDOWN_PRICE_PEAK_HARD_4C","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive","best_trigger":"ECOPROBM_247540_2024_03_25_4C_EV_DEMAND_SLOWDOWN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"EV demand slowdown / cathode overcapacity guardrail protected against a -63% 180D MAE from the local peak zone","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"new local C14 symbol; evidence is source_proxy_only and requires URL repair"}
{"row_type":"case","case_id":"C14_SDI_006400_2024_03_25_EV_DEMAND_SLOWDOWN_RELIEF_RALLY_FAIL","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"79","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_CELL_EV_DEMAND_SLOWDOWN_RELIEF_RALLY_FAIL","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive","best_trigger":"SDI_006400_2024_03_25_4C_EV_DEMAND_SLOWDOWN_RELIEF_RALLY_FAIL","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Relief rally had almost no forward MFE and later -50% 180D MAE; C14 guardrail should cap Stage2/Yellow","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"new local C14 symbol; source_proxy_only evidence"}
{"row_type":"case","case_id":"C14_LGES_373220_2024_04_08_EV_DEMAND_SLOWDOWN_FALSE_4C","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"79","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CELL_LEADER_EV_SLOWDOWN_FALSE_HARD_4C_WITH_RECOVERY","case_type":"failed_hard_4c_overblock","positive_or_counterexample":"counterexample","best_trigger":"LGES_373220_2024_04_08_FALSE_4C_EV_DEMAND_SLOWDOWN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Broad EV slowdown fear alone would have over-blocked a later +19% 180D recovery path; utilization/call-off bridge is required","current_profile_verdict":"current_profile_overprotective_4C","price_source":"Songdaiki/stock-web","notes":"counterexample: C14 hard 4C should require explicit utilization/call-off/customer demand bridge, not broad sector fear"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"ECOPROBM_247540_2024_03_25_4C_EV_DEMAND_SLOWDOWN","case_id":"C14_ECOPROBM_247540_2024_03_25_EV_DEMAND_SLOWDOWN_HARD_4C_SUCCESS","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"79","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_EV_DEMAND_SLOWDOWN_PRICE_PEAK_HARD_4C","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_stress_test|canonical_archetype_compression","trigger_type":"4C-Protective","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":291000.0,"evidence_available_at_that_date":"source_proxy_only: EV demand slowdown, cathode inventory/overcapacity risk, valuation peak, and utilization/call-off risk narrative; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["battery_materials_theme_beta","short_relief_rally"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["valuation_peak","price_extension","positioning_overheat"],"stage4c_evidence_fields":["ev_demand_slowdown","utilization_risk","cathode_overcapacity_risk","call_off_risk"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.89,"MFE_90D_pct":1.89,"MFE_180D_pct":1.89,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-26.12,"MAE_90D_pct":-41.37,"MAE_180D_pct":-63.37,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":296500.0,"drawdown_after_peak_pct":-64.05,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_4B_peak_aligned_but_hard_4C_required_for_thesis_break","four_b_evidence_type":["valuation_blowoff","price_extension"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"positive_protective_4c_high_mae","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_247540_2024_03_25_291000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"SDI_006400_2024_03_25_4C_EV_DEMAND_SLOWDOWN_RELIEF_RALLY_FAIL","case_id":"C14_SDI_006400_2024_03_25_EV_DEMAND_SLOWDOWN_RELIEF_RALLY_FAIL","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"79","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_CELL_EV_DEMAND_SLOWDOWN_RELIEF_RALLY_FAIL","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_stress_test|canonical_archetype_compression","trigger_type":"4C-Protective","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":486000.0,"evidence_available_at_that_date":"source_proxy_only: EV cell demand slowdown, utilization risk, customer demand uncertainty, and relief-rally price extension; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["battery_cell_relief_rally","relative_strength_short_burst"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["relief_rally_peak","valuation_extension"],"stage4c_evidence_fields":["ev_demand_slowdown","utilization_risk","customer_order_risk","margin_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.75,"MFE_90D_pct":1.75,"MFE_180D_pct":1.75,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-16.26,"MAE_90D_pct":-27.78,"MAE_180D_pct":-50.93,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":494500.0,"drawdown_after_peak_pct":-51.77,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"relief_rally_peak_aligned_but_4C_needed_to_block_stage2","four_b_evidence_type":["valuation_blowoff","relief_rally_peak"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"positive_protective_4c_high_mae","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_006400_2024_03_25_486000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"LGES_373220_2024_04_08_FALSE_4C_EV_DEMAND_SLOWDOWN","case_id":"C14_LGES_373220_2024_04_08_EV_DEMAND_SLOWDOWN_FALSE_4C","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"79","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CELL_LEADER_EV_SLOWDOWN_FALSE_HARD_4C_WITH_RECOVERY","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_stress_test|canonical_archetype_compression","trigger_type":"4C-FalsePositive","trigger_date":"2024-04-08","entry_date":"2024-04-08","entry_price":373000.0,"evidence_available_at_that_date":"source_proxy_only: broad EV demand slowdown fear without sufficiently explicit utilization/call-off/customer bridge; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["cell_leader_scale","policy_or_ira_support_possible"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["sector_weakness"],"stage4c_evidence_fields":["broad_ev_slowdown_fear_only","call_off_not_confirmed","utilization_bridge_unclear"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.43,"MFE_90D_pct":6.43,"MFE_180D_pct":19.03,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.69,"MAE_90D_pct":-16.62,"MAE_180D_pct":-16.62,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-08","peak_price":444000.0,"drawdown_after_peak_pct":-23.31,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.84,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"broad_slowdown_fear_was_not_sufficient_for_hard_4c","four_b_evidence_type":["sector_weakness_only"],"four_c_protection_label":"false_4c_overblock","trigger_outcome_label":"counterexample_false_4c_recovery","current_profile_verdict":"current_profile_overprotective_4C","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_373220_2024_04_08_373000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_ECOPROBM_247540_2024_03_25_EV_DEMAND_SLOWDOWN_HARD_4C_SUCCESS","trigger_id":"ECOPROBM_247540_2024_03_25_4C_EV_DEMAND_SLOWDOWN","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage2 false-positive / 4B-watch risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":45,"stage_label_after":"4C-Protective, not Stage2","changed_components":["relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"EV demand slowdown plus overcapacity/utilization risk should route to protective 4C and block Stage2.","MFE_90D_pct":1.89,"MAE_90D_pct":-41.37,"score_return_alignment_label":"protective_4c_success","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_SDI_006400_2024_03_25_EV_DEMAND_SLOWDOWN_RELIEF_RALLY_FAIL","trigger_id":"SDI_006400_2024_03_25_4C_EV_DEMAND_SLOWDOWN_RELIEF_RALLY_FAIL","symbol":"006400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive / relief-rally risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":50,"stage_label_after":"4C-Protective / Stage1-watch","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Relief rally lacked durable utilization/order bridge and needed 4C protection.","MFE_90D_pct":1.75,"MAE_90D_pct":-27.78,"score_return_alignment_label":"protective_4c_success","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_LGES_373220_2024_04_08_EV_DEMAND_SLOWDOWN_FALSE_4C","trigger_id":"LGES_373220_2024_04_08_FALSE_4C_EV_DEMAND_SLOWDOWN","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":3,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":58,"stage_label_before":"4C risk / Stage1-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage1/Stage2-watch, not hard 4C","changed_components":["relative_strength_score","execution_risk_score"],"component_delta_explanation":"Broad EV slowdown fear without call-off/utilization proof should not hard-block a cell leader that later recovered.","MFE_90D_pct":6.43,"MAE_90D_pct":-16.62,"score_return_alignment_label":"false_4c_overblock_guard_needed","current_profile_verdict":"current_profile_overprotective_4C"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"79","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c","stage2_actionable_evidence_bonus"],"residual_error_types_found":["current_profile_4C_too_late","current_profile_overprotective_4C"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 79
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION
```

If this loop is accepted, C14 moves from 21 to a projected 24 rows. It remains below 30-row minimum stability, but the next run should re-read the latest No-Repeat Index before selecting another C14 case.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/247/247540.json
  - atlas/symbol_profiles/006/006400.json
  - atlas/symbol_profiles/373/373220.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
