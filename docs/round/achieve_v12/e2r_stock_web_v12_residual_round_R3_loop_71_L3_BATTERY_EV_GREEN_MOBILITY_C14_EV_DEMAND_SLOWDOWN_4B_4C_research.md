# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R3
loop = 71
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = mixed
selection_mode = auto_coverage_gap_fill
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

This file is a standalone historical residual research artifact. It is not a live watchlist, not a recommendation, and not a repository patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The purpose of this loop is not to re-prove the global axes. The residual question is narrower: in battery/EV names, when does EV demand slowdown become a real 4C thesis break, and when is it only a volatile 4B-watch overlay?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R3
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
loop_objective = coverage_gap_fill, counterexample_mining, sector_specific_rule_discovery, canonical_archetype_compression, 4C_thesis_break_timing_test, 4B_non_price_requirement_stress_test
```

Chosen canonical compression:

```text
CELL_MAKER_EV_DEMAND_CAPEX_CUT_AMPC_DEPENDENCY -> C14
EUROPE_CUSTOMER_EV_DEMAND_SLOWDOWN -> C14
CATHODE_MATERIAL_INVENTORY_UTILIZATION_READTHROUGH -> C14
BROAD_LITHIUM_PRICE_COLLAPSE_NOT_ENOUGH_FOR_HARD_4C -> C14
```

## 3. Previous Coverage / Duplicate Avoidance Check

A repository artifact search for `C14_EV_DEMAND_SLOWDOWN_4B_4C` returned no direct matched research artifact. Therefore this loop treats C14 as an auto-selected coverage gap, while still avoiding the already-heavy R1/R2 power/HBM/defense repetition pattern.

```text
auto_selected_coverage_gap = C14_EV_DEMAND_SLOWDOWN_4B_4C
new_canonical_archetype_count = 1
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
reused_case_count = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-web manifest validation:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The profiles inspected for this loop:

| symbol | company | profile_path | years | corporate_action_window_status |
|---:|---|---|---|---|
| 373220 | LG에너지솔루션 | atlas/symbol_profiles/373/373220.json | 2022-2026 | clean for tested 2024/2025 windows |
| 006400 | 삼성SDI | atlas/symbol_profiles/006/006400.json | 1995-2026 | historic corporate-action candidates outside tested 2024/2025 windows |
| 247540 | 에코프로비엠 | atlas/symbol_profiles/247/247540.json | 2019-2026 | corporate-action candidates in 2022 only; clean for tested 2024/2025 windows |
| 066970 | 엘앤에프 | atlas/symbol_profiles/066/066970.json | 2003-2026 | corporate-action candidates before tested 2024 window |

## 5. Historical Eligibility Gate

All four representative trigger rows satisfy the 180-trading-day calibration gate.

```text
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
blocked_for_weight_calibration = 0
narrative_only_count = 1
```

The one narrative-only row is a future-validation reminder: LGES 2025-07-25 had useful slowdown/ESS-offset evidence, but its 180D window is incomplete by manifest max_date.

## 6. Canonical Archetype Compression Map

C14 should absorb four fine patterns rather than create four separate scoring families:

| fine_archetype_id | canonical mapping | scoring reason |
|---|---|---|
| CELL_MAKER_EV_DEMAND_CAPEX_CUT_AMPC_DEPENDENCY | C14 | Slow EV demand plus capex cut and subsidy dependence acts as a thesis-break route. |
| EUROPE_CUSTOMER_EV_DEMAND_SLOWDOWN | C14 | Named customer/regional exposure makes the slowdown measurable. |
| CATHODE_MATERIAL_INVENTORY_UTILIZATION_READTHROUGH | C14 | Material suppliers can break after a cell-maker capex shock even without their own same-day disclosure. |
| BROAD_LITHIUM_PRICE_COLLAPSE_NOT_ENOUGH_FOR_HARD_4C | C14 | Commodity-only evidence can be directionally right but too early for hard 4C. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---|
| R3L71_C14_373220_20241028_LGES_CAPEX_CUT_4C | 373220 | LG에너지솔루션 | positive / 4C_success | 2024-10-28 Stage4C | 416500 | 4.56 | -21.37 | 4.56 | -36.13 | current_profile_correct |
| R3L71_C14_006400_20240625_SDI_EUROPE_EXPOSURE_4C | 006400 | 삼성SDI | positive / 4C_success | 2024-06-25 Stage4C | 368500 | 6.78 | -20.08 | 6.78 | -49.31 | current_profile_correct |
| R3L71_C14_247540_20241028_ECOPROBM_CATHODE_READTHROUGH | 247540 | 에코프로비엠 | positive / missed_structural | 2024-10-28 Stage4C | 172000 | 9.94 | -44.42 | 9.94 | -52.85 | current_profile_missed_structural |
| R3L71_C14_066970_20240125_LF_LITHIUM_PRICE_ONLY_COUNTEREXAMPLE | 066970 | 엘앤에프 | counterexample / high_mae_success | 2024-01-25 Stage4B-Watch | 157500 | 26.35 | -16.13 | 26.35 | -47.37 | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 1
calibration_usable_case_count = 4
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

The loop is deliberately not all bearish-success examples. L&F is included because a broad lithium/EV-demand shock was directionally right over 180D but allowed a +26.35% 90D rebound before the full drawdown. That is exactly the kind of residual timing error that a 4C guard should detect.

## 9. Evidence Source Map

| case_id | evidence date | evidence source | stage meaning |
|---|---|---|---|
| R3L71_C14_373220_20241028_LGES_CAPEX_CUT_4C | 2024-10-28 | Reuters: LGES Q3 profit drop, conservative 2025 revenue view, capex reduction, AMPC dependence | Hard 4C |
| R3L71_C14_006400_20240625_SDI_EUROPE_EXPOSURE_4C | 2024-06-25 | MarketWatch / WSJ Market Talk: Europe EV slowdown, customer concentration, earnings-estimate cut | Hard 4C |
| R3L71_C14_247540_20241028_ECOPROBM_MATERIAL_READTHROUGH | 2024-10-28 | Cell-maker capex cut read-through plus battery-mineral price pressure | Hard 4C / missed structural |
| R3L71_C14_066970_20240125_LF_LITHIUM_PRICE_ONLY_COUNTEREXAMPLE | 2024-01-25 | Broad battery-mineral collapse / lithium price collapse from lagging EV demand | 4B watch, not hard 4C |

## 10. Price Data Source Map

| symbol | entry_date | entry_price | price_shard_path | profile_path | basis |
|---:|---|---:|---|---|---|
| 373220 | 2024-10-28 | 416500 | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv | atlas/symbol_profiles/373/373220.json | tradable_raw |
| 006400 | 2024-06-25 | 368500 | atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv | atlas/symbol_profiles/006/006400.json | tradable_raw |
| 247540 | 2024-10-28 | 172000 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv | atlas/symbol_profiles/247/247540.json | tradable_raw |
| 066970 | 2024-01-25 | 157500 | atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv | atlas/symbol_profiles/066/066970.json | tradable_raw |

## 11. Case-by-Case Trigger Grid

| trigger_id | evidence family | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak | drawdown after peak | outcome |
|---|---|---|---:|---:|---:|---:|---|---:|---|
| TRG_C14_373220_20241028_LGES_CAPEX_CUT_4C | CELL_MAKER_EV_DEMAND_CAPEX_CUT_AMPC_DEPENDENCY | 2024-10-28 | 416500 | 4.56 / -10.92 | 4.56 / -21.37 | 4.56 / -36.13 | 2024-11-11 435500 | -38.92 | large_180D_drawdown_after_low_upside |
| TRG_C14_006400_20240625_SDI_EUROPE_EXPOSURE_4C | EUROPE_CUSTOMER_EV_DEMAND_SLOWDOWN | 2024-06-25 | 368500 | 5.83 / -20.08 | 6.78 / -20.08 | 6.78 / -49.31 | 2024-09-30 393500 | -52.53 | minor_upside_large_downside |
| TRG_C14_247540_20241028_ECOPROBM_CATHODE_READTHROUGH | CATHODE_MATERIAL_INVENTORY_UTILIZATION_READTHROUGH | 2024-10-28 | 172000 | 9.94 / -30.0 | 9.94 / -44.42 | 9.94 / -52.85 | 2024-11-04 189100 | -57.11 | material_readthrough_drawdown |
| TRG_C14_066970_20240125_LF_LITHIUM_PRICE_ONLY_COUNTEREXAMPLE | BROAD_LITHIUM_PRICE_COLLAPSE_NOT_ENOUGH_FOR_HARD_4C | 2024-01-25 | 157500 | 10.6 / -16.13 | 26.35 / -16.13 | 26.35 / -47.37 | 2024-03-25 199000 | -58.34 | large_intermediate_rebound_before_drawdown |


## 12. Trigger-Level OHLC Backtest Tables

The decisive comparison is not whether downside eventually occurred. It is whether the signal had enough non-price evidence to justify hard 4C at the trigger.

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | interpretation |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 373220 | 416500 | 4.56 | -10.92 | 4.56 | -21.37 | 4.56 | -36.13 | Strong hard-4C protection within 180D. |
| 006400 | 368500 | 5.83 | -20.08 | 6.78 | -20.08 | 6.78 | -49.31 | Named customer/regional demand exposure worked as real 4C. |
| 247540 | 172000 | 9.94 | -30.00 | 9.94 | -44.42 | 9.94 | -52.85 | Material read-through was severe; P0 may miss it. |
| 066970 | 157500 | 10.60 | -16.13 | 26.35 | -16.13 | 26.35 | -47.37 | Counterexample: commodity-only shock was too early for hard 4C. |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely judgment | result | stress verdict |
|---|---|---|---|
| LGES 2024-10-28 | Hard 4C or 4C-watch because non-price capex/revision evidence exists. | Correct. Low upside, large 180D downside. | existing_axis_strengthened: hard_4c_thesis_break_routes_to_4c |
| Samsung SDI 2024-06-25 | 4C-watch because customer/revision evidence exists. | Correct. Minor upside, large downside. | existing_axis_strengthened: full_4b_requires_non_price_evidence |
| EcoProBM 2024-10-28 | Possibly only 4B-watch because evidence is customer/cell-maker read-through, not direct company disclosure. | Too late / missed structural. | new_axis_proposed: material_readthrough_from_cellmaker_capex_cut |
| L&F 2024-01-25 | Could become hard 4C if broad price collapse is over-weighted. | False positive timing: +26.35% 90D MFE before deeper drawdown. | new_axis_proposed: broad_lithium_price_only_hard_4c_guard |

## 14. Stage2 / Yellow / Green Comparison

This loop is not primarily a Stage2-to-Green lateness audit. All representative rows are 4B/4C overlays. Therefore:

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger; C14 loop is a downside/protection calibration loop
```

However, the L&F counterexample shows why a Stage3 or 4C label cannot be pasted onto commodity price collapse alone. Price collapse can mark the road, but customer/call-off/revision evidence decides whether the bridge is actually gone.

## 15. 4B Local vs Full-window Timing Audit

| case_id | four_b_evidence_type | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---|---:|---:|---|
| LGES 2024-10-28 | revision_slowdown, margin_or_backlog_slowdown | null | null | Treat as 4C protection, not local 4B. |
| Samsung SDI 2024-06-25 | revision_slowdown, customer_or_order_quality | null | null | Non-price evidence justifies thesis-break watch. |
| EcoProBM 2024-10-28 | valuation_blowoff, margin_or_backlog_slowdown, material read-through | null | null | P0 too late if it demands direct same-company disclosure. |
| L&F 2024-01-25 | price_only, valuation_blowoff, broad commodity shock | null | null | Broad price/commodity-only evidence should remain 4B-watch. |

## 16. 4C Protection Audit

| case_id | 4C label | MAE180 | max drawdown after peak | protection read |
|---|---|---:|---:|---|
| LGES 2024-10-28 | hard_4c_success_180D_but_retest_after_1Y_recovery | -36.13 | -38.92 | Strong 180D protection, but later recovery means 4C should be reviewed when ESS/policy recovery appears. |
| Samsung SDI 2024-06-25 | hard_4c_success | -49.31 | -52.53 | Strong protection. |
| EcoProBM 2024-10-28 | hard_4c_success | -52.85 | -57.11 | Strong protection and missed-material-readthrough evidence. |
| L&F 2024-01-25 | false_break_if_hard_4c_without_customer_calloff | -47.37 | -58.34 | Directionally bearish but too early for hard 4C due +26.35% 90D rebound. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = battery_ev_demand_slowdown_severity_stack
proposal = In L3 battery/EV, slow EV demand should become hard 4C only when at least two non-price evidence blocks are present: named customer/regional exposure, confirmed revision, capex cut/call-off, inventory/utilization hit, or AMPC/IRA dependence.
shadow_delta = +1 for qualified C14 hard-4C candidates
counter_guard = broad lithium/commodity price collapse alone remains 4B-watch
confidence = medium
production_scoring_changed = false
```

Mechanism: a battery supply chain is not one company. It is a conveyor belt. If only the price of lithium falls, one belt is vibrating. If a cell maker cuts capex, customer demand slows, revision turns down, and inventory begins to swell, the whole conveyor slows. That is when the signal moves from 4B-watch to 4C protection.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
rule = hard_4c_demand_slowdown_combo_gate
requirements:
  - evidence is non-price
  - at least two of:
    1. named_customer_or_region_exposure
    2. confirmed_revision_or_guidance_cut
    3. capex_cut_or_contract_calloff
    4. inventory_or_utilization_bridge
    5. AMPC_or_policy_subsidy_dependency
block:
  - price-only blowoff
  - commodity-price-only lithium/nickel/cathode shock
  - macro-only EV slowdown without company/channel bridge
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global current | Keeps existing hard-4C and non-price 4B discipline but lacks C14 material-readthrough and broad-commodity guard. | 4 | 11.91 | -25.5 | 11.91 | -46.41 | 0.25 | 1 | Directionally good, but C14 residual errors remain. |
| P0b_e2r_2_0_baseline_reference | rollback | Lower evidence discipline; tends to confuse price/commodity shock with thesis break. | 4 | 11.91 | -25.5 | 11.91 | -46.41 | 0.50 | 1 | Worse: premature hard 4C and material-channel miss coexist. |
| P1_sector_specific_candidate_profile | L3 sector | Adds EV-demand slowdown severity stack: customer concentration, capex cut, AMPC dependence, inventory/utilization. | 4 | 11.91 | -25.5 | 11.91 | -46.41 | 0.25 | 0 | Better: catches cathode material read-through. |
| P2_canonical_archetype_candidate_profile | C14 | Hard 4C only when demand slowdown is tied to at least two non-price break evidences. | 4 | 11.91 | -25.5 | 11.91 | -46.41 | 0.00 | 0 | Best current fit: keeps LGES/SDI/EcoProBM, downgrades L&F to 4B-watch. |
| P3_counterexample_guard_profile | C14 guard | Broad lithium/commodity price shock alone cannot become hard 4C. | 4 | 11.91 | -25.5 | 11.91 | -46.41 | 0.00 | 1 | Useful guard; needs more positives to avoid over-tightening. |


## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | label_before | weighted_score_after | label_after | alignment |
|---|---:|---|---:|---|---|
| R3L71_C14_373220_20241028_LGES_CAPEX_CUT_4C | 86 | Stage4C-Watch | 91 | Hard-4C | large_180D_drawdown_after_low_upside |
| R3L71_C14_006400_20240625_SDI_EUROPE_EXPOSURE_4C | 81 | Stage4C-Watch | 88 | Hard-4C | minor_upside_large_downside |
| R3L71_C14_247540_20241028_ECOPROBM_CATHODE_READTHROUGH | 74 | Stage3-Yellow / 4B-Watch | 87 | Hard-4C | material_readthrough_drawdown |
| R3L71_C14_066970_20240125_LF_LITHIUM_PRICE_ONLY_COUNTEREXAMPLE | 82 | Hard-4C-if-ungated | 72 | Stage4B-Watch | large_intermediate_rebound_before_drawdown |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | mixed: LGES/SDI/cathode/L&F | 3 | 1 | 1 | 3 | 4 | 0 | 4 | 4 | 2 | true | true | C14 still needs additional OEM-side and recycler/material counterexamples, but core cell/material/counterexample coverage is no longer empty. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4
positive_case_count: 3
counterexample_count: 1
current_profile_error_count: 2
tested_existing_calibrated_axes:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - price_only_blowoff_blocks_positive_stage
residual_error_types_found:
  - material_readthrough_missed_structural
  - broad_commodity_signal_false_4C_timing
new_axis_proposed:
  - demand_slowdown_to_hard_4c_combo_gate
  - material_readthrough_from_cellmaker_capex_cut
  - broad_lithium_price_only_hard_4c_guard
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C14_EV_DEMAND_SLOWDOWN_4B_4C
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date read from atlas/manifest.json
- representative trigger rows use stock-web tradable shards
- entry_date / entry_price separated from trigger_date
- MFE / MAE / peak / drawdown computed from actual visible stock-web OHLC rows
- 180D forward window available for all representative rows
- corporate action contamination checked at profile level and not overlapping tested windows
```

Not validated:

```text
- production scoring code
- stock_agent src/e2r internals
- live candidate scan
- brokerage or auto-trading
- post-2026-02-20 stock-web price path
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,demand_slowdown_to_hard_4c_combo_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,none,require_2_of_named_customer_revision_capex_calloff_inventory_ampc,1,C14 hard 4C needs non-price demand evidence stack,reduces false hard-4C on L&F while keeping LGES/SDI/EcoProBM protection,TRG_C14_373220_20241028_LGES_CAPEX_CUT_4C|TRG_C14_006400_20240625_SDI_EUROPE_EXPOSURE_4C|TRG_C14_247540_20241028_ECOPROBM_CATHODE_READTHROUGH|TRG_C14_066970_20240125_LF_LITHIUM_PRICE_ONLY_COUNTEREXAMPLE,4,4,1,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,material_readthrough_from_cellmaker_capex_cut,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,underweighted,+1 readthrough score for cathode/materials when cell-maker capex cut is public,1,EcoproBM drawdown shows supplier-material channel is structural,raises missed structural case to hard 4C watch,TRG_C14_247540_20241028_ECOPROBM_CATHODE_READTHROUGH,1,1,0,low_to_medium,sector_shadow_only,needs more material names before production promotion
shadow_weight,broad_lithium_price_only_hard_4c_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,not_explicit,commodity-only evidence remains 4B-watch,1,L&F rebounded +26.35% before the 180D drawdown,reduces premature hard 4C when no customer/call-off/revision bridge exists,TRG_C14_066970_20240125_LF_LITHIUM_PRICE_ONLY_COUNTEREXAMPLE,1,1,1,medium,counterexample_guard_profile,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R3L71_C14_373220_20241028_LGES_CAPEX_CUT_4C","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CELL_MAKER_EV_DEMAND_CAPEX_CUT_AMPC_DEPENDENCY","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"large_180D_drawdown_after_low_upside","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Good example where slow EV demand plus capex cut and subsidy dependence is not just local overheat; it protects from a deep 180D drawdown."}
{"row_type":"case","case_id":"R3L71_C14_006400_20240625_SDI_EUROPE_EXPOSURE_4C","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EUROPE_CUSTOMER_EV_DEMAND_SLOWDOWN","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"minor_upside_large_downside","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Named regional/customer concentration turns a generic slowdown into a sector-specific 4C route."}
{"row_type":"case","case_id":"R3L71_C14_247540_20241028_ECOPROBM_CATHODE_READTHROUGH","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_MATERIAL_INVENTORY_UTILIZATION_READTHROUGH","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"material_readthrough_drawdown","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Residual error: current calibrated profile may under-weight materials when the trigger is not a direct company disclosure but a customer/cell-maker capex shock."}
{"row_type":"case","case_id":"R3L71_C14_066970_20240125_LF_LITHIUM_PRICE_ONLY_COUNTEREXAMPLE","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BROAD_LITHIUM_PRICE_COLLAPSE_NOT_ENOUGH_FOR_HARD_4C","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B-Watch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"large_intermediate_rebound_before_drawdown","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample: sector commodity shock was directionally right over 180D, but immediate hard 4C would have over-blocked a 26% rebound."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_C14_373220_20241028_LGES_CAPEX_CUT_4C","case_id":"R3L71_C14_373220_20241028_LGES_CAPEX_CUT_4C","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CELL_MAKER_EV_DEMAND_CAPEX_CUT_AMPC_DEPENDENCY","sector":"battery_ev_green_mobility","primary_archetype":"EV demand slowdown to 4B/4C","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery","trigger_type":"Stage4C","trigger_date":"2024-10-28","evidence_available_at_that_date":"Q3 2024 profit decline, conservative 2025 revenue view, explicit capex reduction and AMPC dependence under slow EV demand.","evidence_source":"Reuters 2024-10-28; LGES Q3 2024 slow EV demand / capex reduction / AMPC dependence","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["revision_slowdown","margin_or_backlog_slowdown","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken","call_off_or_order_cut"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-28","entry_price":416500,"MFE_30D_pct":4.56,"MFE_90D_pct":4.56,"MFE_180D_pct":4.56,"MFE_1Y_pct":26.53,"MFE_2Y_pct":null,"MAE_30D_pct":-10.92,"MAE_90D_pct":-21.37,"MAE_180D_pct":-36.13,"MAE_1Y_pct":-36.13,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-11","peak_price":435500,"drawdown_after_peak_pct":-38.92,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_full_4B; direct hard_4C protection route","four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success_180D_but_retest_after_1Y_recovery","trigger_outcome_label":"large_180D_drawdown_after_low_upside","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L71_C14_373220_20241028_LGES_CAPEX_CUT_4C::2024-10-28::416500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C14_006400_20240625_SDI_EUROPE_EXPOSURE_4C","case_id":"R3L71_C14_006400_20240625_SDI_EUROPE_EXPOSURE_4C","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EUROPE_CUSTOMER_EV_DEMAND_SLOWDOWN","sector":"battery_ev_green_mobility","primary_archetype":"EV demand slowdown to 4B/4C","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery","trigger_type":"Stage4C","trigger_date":"2024-06-25","evidence_available_at_that_date":"Europe-heavy EV battery customer mix, named automaker exposure and explicit earnings-estimate cut under Europe EV demand slowdown.","evidence_source":"MarketWatch / WSJ Market Talk 2024-06-25; Samsung SDI Europe EV demand slowdown and earnings cut","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources"],"stage4b_evidence_fields":["revision_slowdown","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-25","entry_price":368500,"MFE_30D_pct":5.83,"MFE_90D_pct":6.78,"MFE_180D_pct":6.78,"MFE_1Y_pct":6.78,"MFE_2Y_pct":null,"MAE_30D_pct":-20.08,"MAE_90D_pct":-20.08,"MAE_180D_pct":-49.31,"MAE_1Y_pct":-56.53,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-30","peak_price":393500,"drawdown_after_peak_pct":-52.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"good_full_window_4C_timing; non-price customer/revision evidence","four_b_evidence_type":["revision_slowdown","customer_or_order_quality"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"minor_upside_large_downside","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L71_C14_006400_20240625_SDI_EUROPE_EXPOSURE_4C::2024-06-25::368500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C14_247540_20241028_ECOPROBM_CATHODE_READTHROUGH","case_id":"R3L71_C14_247540_20241028_ECOPROBM_CATHODE_READTHROUGH","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_MATERIAL_INVENTORY_UTILIZATION_READTHROUGH","sector":"battery_ev_green_mobility","primary_archetype":"EV demand slowdown to 4B/4C","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery","trigger_type":"Stage4C","trigger_date":"2024-10-28","evidence_available_at_that_date":"Cell-maker capex cut and slow EV demand read through to cathode utilization, inventory, lithium/nickel spread and pricing risk.","evidence_source":"Reuters 2024-10-28 LGES capex cut; broad battery-mineral price collapse evidence from 2024 sector sources","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["confirmed_revision"],"stage4b_evidence_fields":["revision_slowdown","margin_or_backlog_slowdown","valuation_blowoff"],"stage4c_evidence_fields":["thesis_evidence_broken","call_off_or_order_cut"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-28","entry_price":172000,"MFE_30D_pct":9.94,"MFE_90D_pct":9.94,"MFE_180D_pct":9.94,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-30.0,"MAE_90D_pct":-44.42,"MAE_180D_pct":-52.85,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-04","peak_price":189100,"drawdown_after_peak_pct":-57.11,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"P0 too cell-maker-centric; material readthrough needs canonical C14 path","four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown","valuation_blowoff"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"material_readthrough_drawdown","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L71_C14_247540_20241028_ECOPROBM_CATHODE_READTHROUGH::2024-10-28::172000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C14_066970_20240125_LF_LITHIUM_PRICE_ONLY_COUNTEREXAMPLE","case_id":"R3L71_C14_066970_20240125_LF_LITHIUM_PRICE_ONLY_COUNTEREXAMPLE","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BROAD_LITHIUM_PRICE_COLLAPSE_NOT_ENOUGH_FOR_HARD_4C","sector":"battery_ev_green_mobility","primary_archetype":"EV demand slowdown to 4B/4C","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery","trigger_type":"Stage4B-Watch","trigger_date":"2024-01-25","evidence_available_at_that_date":"Broad lithium/battery-mineral collapse and EV demand lag created real downside, but price-only or commodity-only evidence allowed a large 90D rebound before the later drawdown.","evidence_source":"The Guardian 2024-01-19 battery-mineral price collapse; sector lithium/EV demand slowdown evidence","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-25","entry_price":157500,"MFE_30D_pct":10.6,"MFE_90D_pct":26.35,"MFE_180D_pct":26.35,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.13,"MAE_90D_pct":-16.13,"MAE_180D_pct":-47.37,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":199000,"drawdown_after_peak_pct":-58.34,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_or_commodity_only_4B_watch; hard_4C requires customer/call-off or revision bridge","four_b_evidence_type":["price_only","valuation_blowoff","margin_or_backlog_slowdown"],"four_c_protection_label":"false_break_if_hard_4c_without_customer_calloff","trigger_outcome_label":"large_intermediate_rebound_before_drawdown","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L71_C14_066970_20240125_LF_LITHIUM_PRICE_ONLY_COUNTEREXAMPLE::2024-01-25::157500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_proposed_shadow","case_id":"R3L71_C14_373220_20241028_LGES_CAPEX_CUT_4C","trigger_id":"TRG_C14_373220_20241028_LGES_CAPEX_CUT_4C","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":50,"margin_bridge_score":78,"revision_score":82,"relative_strength_score":44,"customer_quality_score":68,"policy_or_regulatory_score":72,"valuation_repricing_score":54,"execution_risk_score":65,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"demand_slowdown_score":86,"inventory_destocking_score":62,"ampc_dependency_risk_score":82,"capex_cut_score":90,"recovery_option_score":25},"weighted_score_before":86,"stage_label_before":"Stage4C-Watch","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":50,"margin_bridge_score":78,"revision_score":82,"relative_strength_score":44,"customer_quality_score":68,"policy_or_regulatory_score":72,"valuation_repricing_score":54,"execution_risk_score":65,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"demand_slowdown_score":86,"inventory_destocking_score":62,"ampc_dependency_risk_score":82,"capex_cut_score":90,"recovery_option_score":25,"guard_or_promotion_adjustment_applied":true},"weighted_score_after":91,"stage_label_after":"Hard-4C","changed_components":["capex_cut_score","ampc_dependency_risk_score","margin_bridge_score"],"component_delta_explanation":"Shadow-only adjustment. C14 promotes to hard 4C only when demand slowdown is tied to named customer exposure, confirmed revision, capex cut/call-off, AMPC dependency, or material inventory/utilization read-through; broad commodity/price-only shock remains 4B-watch.","MFE_90D_pct":4.56,"MAE_90D_pct":-21.37,"score_return_alignment_label":"large_180D_drawdown_after_low_upside","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_proposed_shadow","case_id":"R3L71_C14_006400_20240625_SDI_EUROPE_EXPOSURE_4C","trigger_id":"TRG_C14_006400_20240625_SDI_EUROPE_EXPOSURE_4C","symbol":"006400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":48,"margin_bridge_score":73,"revision_score":80,"relative_strength_score":39,"customer_quality_score":78,"policy_or_regulatory_score":35,"valuation_repricing_score":50,"execution_risk_score":67,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"demand_slowdown_score":88,"inventory_destocking_score":55,"ampc_dependency_risk_score":30,"capex_cut_score":45,"recovery_option_score":20},"weighted_score_before":81,"stage_label_before":"Stage4C-Watch","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":48,"margin_bridge_score":73,"revision_score":80,"relative_strength_score":39,"customer_quality_score":78,"policy_or_regulatory_score":35,"valuation_repricing_score":50,"execution_risk_score":67,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"demand_slowdown_score":88,"inventory_destocking_score":55,"ampc_dependency_risk_score":30,"capex_cut_score":45,"recovery_option_score":20,"guard_or_promotion_adjustment_applied":true},"weighted_score_after":88,"stage_label_after":"Hard-4C","changed_components":["customer_quality_score","revision_score","demand_slowdown_score"],"component_delta_explanation":"Shadow-only adjustment. C14 promotes to hard 4C only when demand slowdown is tied to named customer exposure, confirmed revision, capex cut/call-off, AMPC dependency, or material inventory/utilization read-through; broad commodity/price-only shock remains 4B-watch.","MFE_90D_pct":6.78,"MAE_90D_pct":-20.08,"score_return_alignment_label":"minor_upside_large_downside","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_proposed_shadow","case_id":"R3L71_C14_247540_20241028_ECOPROBM_CATHODE_READTHROUGH","trigger_id":"TRG_C14_247540_20241028_ECOPROBM_CATHODE_READTHROUGH","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":38,"margin_bridge_score":70,"revision_score":68,"relative_strength_score":32,"customer_quality_score":42,"policy_or_regulatory_score":35,"valuation_repricing_score":76,"execution_risk_score":73,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"demand_slowdown_score":84,"inventory_destocking_score":86,"ampc_dependency_risk_score":20,"capex_cut_score":72,"recovery_option_score":18},"weighted_score_before":74,"stage_label_before":"Stage3-Yellow / 4B-Watch","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":38,"margin_bridge_score":70,"revision_score":68,"relative_strength_score":32,"customer_quality_score":42,"policy_or_regulatory_score":35,"valuation_repricing_score":76,"execution_risk_score":73,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"demand_slowdown_score":84,"inventory_destocking_score":86,"ampc_dependency_risk_score":20,"capex_cut_score":72,"recovery_option_score":18,"guard_or_promotion_adjustment_applied":true},"weighted_score_after":87,"stage_label_after":"Hard-4C","changed_components":["inventory_destocking_score","capex_cut_score","material_readthrough_gate"],"component_delta_explanation":"Shadow-only adjustment. C14 promotes to hard 4C only when demand slowdown is tied to named customer exposure, confirmed revision, capex cut/call-off, AMPC dependency, or material inventory/utilization read-through; broad commodity/price-only shock remains 4B-watch.","MFE_90D_pct":9.94,"MAE_90D_pct":-44.42,"score_return_alignment_label":"material_readthrough_drawdown","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_proposed_shadow","case_id":"R3L71_C14_066970_20240125_LF_LITHIUM_PRICE_ONLY_COUNTEREXAMPLE","trigger_id":"TRG_C14_066970_20240125_LF_LITHIUM_PRICE_ONLY_COUNTEREXAMPLE","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":30,"margin_bridge_score":60,"revision_score":50,"relative_strength_score":38,"customer_quality_score":25,"policy_or_regulatory_score":20,"valuation_repricing_score":78,"execution_risk_score":64,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"demand_slowdown_score":74,"inventory_destocking_score":80,"ampc_dependency_risk_score":10,"capex_cut_score":15,"recovery_option_score":55},"weighted_score_before":82,"stage_label_before":"Hard-4C-if-ungated","raw_component_scores_after":{"contract_score":25,"backlog_visibility_score":30,"margin_bridge_score":60,"revision_score":50,"relative_strength_score":38,"customer_quality_score":25,"policy_or_regulatory_score":20,"valuation_repricing_score":78,"execution_risk_score":64,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"demand_slowdown_score":74,"inventory_destocking_score":80,"ampc_dependency_risk_score":10,"capex_cut_score":15,"recovery_option_score":55,"guard_or_promotion_adjustment_applied":true},"weighted_score_after":72,"stage_label_after":"Stage4B-Watch","changed_components":["broad_lithium_price_only_guard","customer_calloff_required","recovery_option_score"],"component_delta_explanation":"Shadow-only adjustment. C14 promotes to hard 4C only when demand slowdown is tied to named customer exposure, confirmed revision, capex cut/call-off, AMPC dependency, or material inventory/utilization read-through; broad commodity/price-only shock remains 4B-watch.","MFE_90D_pct":26.35,"MAE_90D_pct":-16.13,"score_return_alignment_label":"large_intermediate_rebound_before_drawdown","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,demand_slowdown_to_hard_4c_combo_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,none,require_2_of_named_customer_revision_capex_calloff_inventory_ampc,1,C14 hard 4C needs non-price demand evidence stack,reduces false hard-4C on L&F while keeping LGES/SDI/EcoProBM protection,TRG_C14_373220_20241028_LGES_CAPEX_CUT_4C|TRG_C14_006400_20240625_SDI_EUROPE_EXPOSURE_4C|TRG_C14_247540_20241028_ECOPROBM_CATHODE_READTHROUGH|TRG_C14_066970_20240125_LF_LITHIUM_PRICE_ONLY_COUNTEREXAMPLE,4,4,1,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,material_readthrough_from_cellmaker_capex_cut,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,underweighted,+1 readthrough score for cathode/materials when cell-maker capex cut is public,1,EcoproBM drawdown shows supplier-material channel is structural,raises missed structural case to hard 4C watch,TRG_C14_247540_20241028_ECOPROBM_CATHODE_READTHROUGH,1,1,0,low_to_medium,sector_shadow_only,needs more material names before production promotion
shadow_weight,broad_lithium_price_only_hard_4c_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,not_explicit,commodity-only evidence remains 4B-watch,1,L&F rebounded +26.35% before the 180D drawdown,reduces premature hard 4C when no customer/call-off/revision bridge exists,TRG_C14_066970_20240125_LF_LITHIUM_PRICE_ONLY_COUNTEREXAMPLE,1,1,1,medium,counterexample_guard_profile,not production; post-calibrated residual
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"positive_case_count":3,"counterexample_count":1,"current_profile_error_count":2,"tested_existing_calibrated_axes":["full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["material_readthrough_missed_structural","broad_commodity_signal_false_4C_timing"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"C14_EV_DEMAND_SLOWDOWN_4B_4C"}
```

### 25.7 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"R3L71_C14_373220_20250725_LGES_TARIFF_ESS_RECOVERY_NARRATIVE","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","reason":"evidence_available_but_forward_180D_unavailable_or_stock_web_price_window_blocked","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration","notes":"2025-07-25 LGES slowdown/tariff warning also included ESS offset/recovery logic; kept as future validation only because 180D forward window is not complete by manifest max_date."}
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
next_round = R3_loop_72_C11_BATTERY_ORDERBOOK_RERATING_or_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
preferred_next_objective = compare_orderbook_positive_vs_calloff_negative
reason = C14 now has first residual coverage; adjacent C11/C12 can separate orderbook rerating from order cut/call-off risk.
```

## 28. Source Notes

Stock-web price atlas:

- https://github.com/Songdaiki/stock-web
- atlas/manifest.json
- atlas/schema.json
- atlas/universe/all_symbols.csv
- atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv
- atlas/symbol_profiles/<prefix>/<ticker>.json

External evidence notes used for historical trigger timing:

- Reuters, 2024-10-28, LG Energy Solution Q3 profit / slow EV demand / capex cut / AMPC dependency.
- MarketWatch / WSJ Market Talk, 2024-06-25, Samsung SDI Europe EV demand slowdown and earnings-estimate cut.
- The Guardian, 2024-01-19, battery-mineral price collapse as EV demand lagged projections.
- Reuters, 2025-07-25, LGES slowing EV demand plus ESS offset, narrative-only because 180D forward window is unavailable by stock-web manifest max_date.

Final loop label:

```text
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
```
