# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R3_loop_95_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
selected_round: R3
selected_loop: 95
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: CHEM_BATTERY_EV_DEMAND_SLOWDOWN_UTILIZATION_MARGIN_HARD_4C
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

This loop adds 3 new independent C14 rows and moves C14 from static 21 rows to local projected 24 after loop79, then to projected 27 after this loop.

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

C14 is the battery/EV demand slowdown protection archetype. The important split is not “battery sector is weak.” The split is whether company-level utilization, call-off, customer demand, margin, ASP, or volume conversion is actually broken.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| static C14 rows | 21 |
| static C14 symbols | 17 |
| static C14 good/bad Stage2 | 3 / 3 |
| static C14 4B/4C | 5 / 7 |
| static C14 URL pending/proxy | 21 / 15 |
| static top covered symbols | 336370, 222080, 361610, 011790, 014820, 025900 |
| local C14 loop79 projected rows | 24 |
| this loop projected rows | 27 |

Selected symbols avoid the static C14 top-covered list and local loop79 C14 symbols `247540`, `006400`, `373220`.

| symbol | company | status |
|---|---|---|
| 051910 | LG화학 | new C14 symbol versus static top-covered and local C14 loop |
| 005070 | 코스모신소재 | new C14 symbol versus static top-covered and local C14 loop |
| 137400 | 피엔티 | new C14 symbol; reused only across different canonical C11 loop94 |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local C14 memory.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 051910 / 2024-02-21 | true | true | clean_180D_window | true |
| 005070 / 2024-02-21 | true | true | clean_180D_window | true |
| 137400 / 2024-03-05 | true | true | clean_180D_window | true |

Corporate-action notes:

- LG화학 has zero corporate-action candidates.
- 코스모신소재 has corporate-action candidates before 2020 only.
- 피엔티 has corporate-action candidates in 2012 and 2019 only.
- 에코프로(086520) was considered but rejected because its profile has a 2024-04-25 corporate-action candidate overlapping the candidate window.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| CHEM_BATTERY_EV_DEMAND_SLOWDOWN_UTILIZATION_MARGIN_HARD_4C | C14 | large-cap battery/chemical exposure with demand/utilization/margin break |
| CATHODE_EV_DEMAND_SLOWDOWN_PRICE_PEAK_MARGIN_HARD_4C | C14 | cathode relief peak fails when demand/utilization/margin bridge breaks |
| BATTERY_EQUIPMENT_BROAD_EV_SLOWDOWN_FALSE_HARD_4C_ORDERBOOK_OFFSET | C14 | broad EV fear alone can over-block if company-specific orderbook bridge offsets |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C14_LGCHEM_051910_2024_02_21_EV_DEMAND_SLOWDOWN_CHEM_BATTERY_HARD_4C | 051910 | LG화학 | hard_4c_protection_success | positive | low MFE and deep MAE validated demand/utilization protection |
| C14_COSMO_005070_2024_02_21_CATHODE_EV_DEMAND_SLOWDOWN_HARD_4C | 005070 | 코스모신소재 | hard_4c_protection_success | positive | cathode relief peak failed without demand/utilization resolution |
| C14_PNT_137400_2024_03_05_FALSE_4C_BROAD_EV_SLOWDOWN_OVERBLOCK | 137400 | 피엔티 | failed_hard_4c_overblock | counterexample | broad EV slowdown fear would have over-blocked a >100% MFE orderbook route |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 3 |
| 4C_case_count | 3 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| local_symbol_reuse_across_canonical | 1 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 051910 | source_proxy_only | EV/battery demand slowdown and utilization/margin pressure | required before promotion |
| 005070 | source_proxy_only | cathode demand slowdown and utilization/margin risk | required before promotion |
| 137400 | source_proxy_only | broad slowdown fear only; company orderbook/CAPA bridge offsets hard 4C | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 051910 | atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv | atlas/symbol_profiles/051/051910.json |
| 005070 | atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv | atlas/symbol_profiles/005/005070.json |
| 137400 | atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv | atlas/symbol_profiles/137/137400.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| LGCHEM_051910_2024_02_21_4C_EV_DEMAND_SLOWDOWN | 4C-Protective | 2024-02-21 | 2024-02-21 | 500000 | EV demand / utilization / margin pressure |
| COSMO_005070_2024_02_21_4C_EV_DEMAND_SLOWDOWN | 4C-Protective | 2024-02-21 | 2024-02-21 | 184500 | cathode demand slowdown / price peak |
| PNT_137400_2024_03_05_FALSE_4C_BROAD_EV_SLOWDOWN | 4C-FalsePositive | 2024-03-05 | 2024-03-05 | 44050 | broad EV slowdown fear without company-specific break |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 051910 | 2024-02-21 | 500000 | 0.80 | -21.00 | 0.80 | -32.70 | 0.80 | -47.30 | 2024-02-21 | 504000 | -47.72 |
| 005070 | 2024-02-21 | 184500 | 5.31 | -18.00 | 5.31 | -24.12 | 5.31 | -47.70 | 2024-02-21 | 194300 | -50.33 |
| 137400 | 2024-03-05 | 44050 | 9.42 | -17.59 | 103.18 | -17.59 | 103.18 | -17.59 | 2024-06-19 | 89500 | -48.66 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 051910 | Stage2/4B-watch risk if slowdown evidence underweighted | low MFE, deep MAE | current_profile_4C_too_late |
| 005070 | Stage2/4B-watch risk if cathode relief rally over-credited | low MFE, deep MAE | current_profile_4C_too_late |
| 137400 | hard 4C risk if broad EV fear overgeneralized | >100% MFE before 4B drawdown | current_profile_overprotective_4C |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C14 interpretation:

- Stage2/Yellow should be capped when company-specific EV demand, utilization, ASP, margin, or customer pull-through breaks.
- Hard 4C should not fire on broad sector fear alone.
- Battery-equipment names with orderbook/CAPA bridge need 4B audit after rerating, not automatic hard 4C.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 051910 | 1.00 | 1.00 | valuation overhang / weak follow-through | local peak aligned; hard 4C needed |
| 005070 | 1.00 | 1.00 | cathode relief peak / valuation overhang | local peak aligned; hard 4C needed |
| 137400 | 0.49 | 1.00 | orderbook offset / company bridge present | broad slowdown fear alone was false hard 4C |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 051910 | hard_4c_success | company-level demand/utilization/margin risk protected against deep MAE |
| 005070 | hard_4c_success | cathode demand/utilization risk protected against deep MAE |
| 137400 | false_4c_overblock | broad EV slowdown fear alone would have blocked a large orderbook-driven rerating |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L3_BATTERY_EV_GREEN_MOBILITY
confidence = medium
```

Candidate:

> In L3 battery/EV names, C14 hard 4C requires company-specific demand break: utilization delay, customer call-off, ASP/margin pressure, inventory/capacity imbalance, or volume conversion failure. Broad EV slowdown fear alone should cap optimism but should not hard-block companies with confirmed orderbook/CAPA bridge.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C14_EV_DEMAND_SLOWDOWN_4B_4C
confidence = medium
```

Candidate C14 rule:

```text
C14_company_specific_demand_break_required =
  ev_demand_slowdown
  AND (utilization_break OR customer_call_off OR asp_pressure OR margin_bridge_failure OR volume_conversion_failure OR inventory_capacity_imbalance)

if broad_ev_slowdown_fear and company_specific_break_absent and orderbook_capa_bridge_present:
    cap_stage = Stage2-watch
    do_not_route_hard_4C = true

if MFE_90D < 10 and MAE_180D < -40:
    classify_as C14_protective_4C_success

if MFE_90D > 50 and broad_ev_slowdown_fear_only:
    classify_as C14_false_4C_overblock_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false 4C | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 36.43 | -24.8 | 36.43 | -37.53 | 1 | C14 needs company-specific demand-break split |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 36.43 | -24.8 | 36.43 | -37.53 | 1 | over-credits relief rallies and broad fear |
| P1 sector_specific_candidate_profile | L3 | 2 protective + 1 false-4C guard | 3.05 | -28.41 | 3.05 | -47.5 | 0 | better after company-specific demand gate |
| P2 canonical_archetype_candidate_profile | C14 | 2 protective + 1 false-4C guard | 3.05 | -28.41 | 3.05 | -47.5 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C14 guard | 2 protective + 1 false-4C guard | 3.05 | -28.41 | 3.05 | -47.5 | 0 | avoids broad-fear hard 4C |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 051910 | protective 4C aligned; Stage2 would be false positive | current_profile_4C_too_late |
| 005070 | protective 4C aligned; relief-rally Stage2 would fail | current_profile_4C_too_late |
| 137400 | hard 4C overblocked orderbook rerating path | current_profile_overprotective_4C |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | mixed C14 fine ids | 2 | 1 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | true | true | static 21 -> local 24 -> projected 27; still need 3 to reach 30 |

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
new_axis_proposed: C14_company_specific_demand_break_required|C14_false_4c_overblock_guard|C14_protective_4c_low_mfe_high_mae
existing_axis_strengthened:
  - hard_4c_thesis_break_routes_to_4c
  - full_4b_requires_non_price_evidence
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
- Avoids static C14 top-covered symbols and local loop79 C14 symbols.
- Rejects 086520 because of a corporate-action candidate inside the candidate 2024 window.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_company_specific_demand_break_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"051910/005070 show hard 4C works when company-level demand/utilization/margin break is visible, while 137400 shows broad fear alone over-blocks","preserves protective 4C but avoids false hard-4C for orderbook-offset names","LGCHEM_051910_2024_02_21_4C_EV_DEMAND_SLOWDOWN|COSMO_005070_2024_02_21_4C_EV_DEMAND_SLOWDOWN|PNT_137400_2024_03_05_FALSE_4C_BROAD_EV_SLOWDOWN",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C14_false_4c_overblock_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"137400 rallied >100% despite broad EV slowdown fear because orderbook/CAPA bridge was company-specific positive","prevents broad EV slowdown from automatic hard 4C","PNT_137400_2024_03_05_FALSE_4C_BROAD_EV_SLOWDOWN",1,1,1,medium,canonical_shadow_only,"false-4C guardrail"
shadow_weight,C14_protective_4c_low_mfe_high_mae,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"051910/005070 had low MFE and deep MAE after EV demand/utilization break","routes company-specific demand break to hard 4C before Stage2 promotion","LGCHEM_051910_2024_02_21_4C_EV_DEMAND_SLOWDOWN|COSMO_005070_2024_02_21_4C_EV_DEMAND_SLOWDOWN",2,2,0,medium,canonical_shadow_only,"4C/protection calibration only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C14_LGCHEM_051910_2024_02_21_EV_DEMAND_SLOWDOWN_CHEM_BATTERY_HARD_4C","symbol":"051910","company_name":"LG화학","round":"R3","loop":"95","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CHEM_BATTERY_EV_DEMAND_SLOWDOWN_UTILIZATION_MARGIN_HARD_4C","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive","best_trigger":"LGCHEM_051910_2024_02_21_4C_EV_DEMAND_SLOWDOWN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"EV/battery demand slowdown and utilization-margin pressure protected against a low-MFE, high-MAE path","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"new C14 symbol versus static top-covered list and local C14 loop79; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C14_COSMO_005070_2024_02_21_CATHODE_EV_DEMAND_SLOWDOWN_HARD_4C","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":"95","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_EV_DEMAND_SLOWDOWN_PRICE_PEAK_MARGIN_HARD_4C","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive","best_trigger":"COSMO_005070_2024_02_21_4C_EV_DEMAND_SLOWDOWN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"cathode EV-demand slowdown and utilization/margin pressure had only ~5% MFE before deep 180D MAE","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"symbol appeared in local C13 loop85 under a different canonical; C14 evidence family is demand-slowdown hard-4C, not JV/utilization positive routing"}
{"row_type":"case","case_id":"C14_PNT_137400_2024_03_05_FALSE_4C_BROAD_EV_SLOWDOWN_OVERBLOCK","symbol":"137400","company_name":"피엔티","round":"R3","loop":"95","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_EQUIPMENT_BROAD_EV_SLOWDOWN_FALSE_HARD_4C_ORDERBOOK_OFFSET","case_type":"failed_hard_4c_overblock","positive_or_counterexample":"counterexample","best_trigger":"PNT_137400_2024_03_05_FALSE_4C_BROAD_EV_SLOWDOWN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"score_price_alignment":"broad EV slowdown fear alone would have over-blocked a battery-equipment orderbook route that later produced >100% MFE","current_profile_verdict":"current_profile_overprotective_4C","price_source":"Songdaiki/stock-web","notes":"same symbol appeared in C11 loop94, but this is a separate C14 false-4C overblock test; independent evidence weight reduced to 0.85 for local symbol reuse"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"LGCHEM_051910_2024_02_21_4C_EV_DEMAND_SLOWDOWN","case_id":"C14_LGCHEM_051910_2024_02_21_EV_DEMAND_SLOWDOWN_CHEM_BATTERY_HARD_4C","symbol":"051910","company_name":"LG화학","round":"R3","loop":"95","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CHEM_BATTERY_EV_DEMAND_SLOWDOWN_UTILIZATION_MARGIN_HARD_4C","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_stress_test|canonical_archetype_compression","trigger_type":"4C-Protective","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":500000.0,"evidence_available_at_that_date":"source_proxy_only: EV battery demand slowdown, utilization/margin pressure, cell/materials valuation peak, and weak forward order visibility; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["battery_relief_rally","chemical_battery_largecap_route"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["valuation_overhang","weak_follow_through","peak_proximity"],"stage4c_evidence_fields":["ev_demand_slowdown","utilization_risk","margin_bridge_absent","customer_demand_pressure"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv","profile_path":"atlas/symbol_profiles/051/051910.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.8,"MFE_90D_pct":0.8,"MFE_180D_pct":0.8,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-21.0,"MAE_90D_pct":-32.7,"MAE_180D_pct":-47.3,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":504000.0,"drawdown_after_peak_pct":-47.72,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_relief_peak_aligned_but_hard_4C_required_for_ev_demand_and_margin_break","four_b_evidence_type":["valuation_overhang","weak_follow_through"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"positive_protective_4c_low_mfe_high_mae","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_051910_2024_02_21_500000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"COSMO_005070_2024_02_21_4C_EV_DEMAND_SLOWDOWN","case_id":"C14_COSMO_005070_2024_02_21_CATHODE_EV_DEMAND_SLOWDOWN_HARD_4C","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":"95","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_EV_DEMAND_SLOWDOWN_PRICE_PEAK_MARGIN_HARD_4C","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_stress_test|canonical_archetype_compression","trigger_type":"4C-Protective","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":184500.0,"evidence_available_at_that_date":"source_proxy_only: cathode material EV demand slowdown, utilization/margin risk, and price peak after relief rally; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["cathode_material_relief_rally","customer_capacity_route"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["price_peak","valuation_overhang","utilization_bridge_pending"],"stage4c_evidence_fields":["ev_demand_slowdown","utilization_risk","margin_bridge_absent","customer_volume_risk"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv","profile_path":"atlas/symbol_profiles/005/005070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.31,"MFE_90D_pct":5.31,"MFE_180D_pct":5.31,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-18.0,"MAE_90D_pct":-24.12,"MAE_180D_pct":-47.7,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":194300.0,"drawdown_after_peak_pct":-50.33,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"cathode_relief_peak_aligned_but_hard_4C_needed_without_demand_utilization_resolution","four_b_evidence_type":["price_peak","valuation_overhang"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"positive_protective_4c_low_mfe_high_mae","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_005070_2024_02_21_184500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"PNT_137400_2024_03_05_FALSE_4C_BROAD_EV_SLOWDOWN","case_id":"C14_PNT_137400_2024_03_05_FALSE_4C_BROAD_EV_SLOWDOWN_OVERBLOCK","symbol":"137400","company_name":"피엔티","round":"R3","loop":"95","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_EQUIPMENT_BROAD_EV_SLOWDOWN_FALSE_HARD_4C_ORDERBOOK_OFFSET","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_stress_test|canonical_archetype_compression","trigger_type":"4C-FalsePositive","trigger_date":"2024-03-05","entry_date":"2024-03-05","entry_price":44050.0,"evidence_available_at_that_date":"source_proxy_only: broad EV slowdown fear existed at sector level, but company-specific battery-equipment orderbook/CAPA bridge remained positive; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["battery_equipment_orderbook_route","capa_bridge","relative_strength"],"stage3_evidence_fields":["orderbook_conversion_partial","margin_bridge_pending"],"stage4b_evidence_fields":["event_positioning","peak_proximity_after_rerating"],"stage4c_evidence_fields":["broad_ev_slowdown_fear_only","company_specific_call_off_not_confirmed","utilization_break_not_confirmed"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv","profile_path":"atlas/symbol_profiles/137/137400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.42,"MFE_90D_pct":103.18,"MFE_180D_pct":103.18,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-17.59,"MAE_90D_pct":-17.59,"MAE_180D_pct":-17.59,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":89500.0,"drawdown_after_peak_pct":-48.66,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.49,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"broad_sector_slowdown_fear_was_not_sufficient_for_C14_hard_4C","four_b_evidence_type":["orderbook_offset","company_specific_bridge_present"],"four_c_protection_label":"false_4c_overblock","trigger_outcome_label":"counterexample_false_4c_high_mfe_orderbook_offset","current_profile_verdict":"current_profile_overprotective_4C","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_137400_2024_03_05_44050","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same symbol was used in C11 loop94, but this row tests a different C14 false-4C overblock condition","independent_evidence_weight":0.85,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_LGCHEM_051910_2024_02_21_EV_DEMAND_SLOWDOWN_CHEM_BATTERY_HARD_4C","trigger_id":"LGCHEM_051910_2024_02_21_4C_EV_DEMAND_SLOWDOWN","symbol":"051910","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2 false-positive / 4B-watch risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":45,"stage_label_after":"4C-Protective, not Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"EV demand/utilization/margin break should route LG화학 to C14 protective 4C instead of Stage2.","MFE_90D_pct":0.8,"MAE_90D_pct":-32.7,"score_return_alignment_label":"protective_4c_success","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_COSMO_005070_2024_02_21_CATHODE_EV_DEMAND_SLOWDOWN_HARD_4C","trigger_id":"COSMO_005070_2024_02_21_4C_EV_DEMAND_SLOWDOWN","symbol":"005070","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2 false-positive / cathode relief-rally risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":46,"stage_label_after":"4C-Protective, not Stage2","changed_components":["contract_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Cathode relief peak plus unresolved demand/utilization risk should route to C14 hard 4C.","MFE_90D_pct":5.31,"MAE_90D_pct":-24.12,"score_return_alignment_label":"protective_4c_success","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_PNT_137400_2024_03_05_FALSE_4C_BROAD_EV_SLOWDOWN_OVERBLOCK","trigger_id":"PNT_137400_2024_03_05_FALSE_4C_BROAD_EV_SLOWDOWN","symbol":"137400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":6,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":9,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable with C11/C02-style bridge, but C14 false-4C risk","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":6,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":9,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable / not hard 4C; 4B audit after rerating","changed_components":[],"component_delta_explanation":"Broad EV slowdown fear alone should not hard-block when company-specific orderbook/CAPA bridge is present.","MFE_90D_pct":103.18,"MAE_90D_pct":-17.59,"score_return_alignment_label":"false_4c_overblock_guard_needed","current_profile_verdict":"current_profile_overprotective_4C"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"95","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c","stage2_actionable_evidence_bonus"],"residual_error_types_found":["current_profile_4C_too_late","current_profile_overprotective_4C"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 95
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C14_EV_DEMAND_SLOWDOWN_4B_4C, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
```

If this loop is accepted together with local loop79, C14 moves to projected 27 rows and still needs 3 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C14 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/051/051910.json
  - atlas/symbol_profiles/005/005070.json
  - atlas/symbol_profiles/137/137400.json
- Rejected due to corporate-action contamination risk:
  - atlas/symbol_profiles/086/086520.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
