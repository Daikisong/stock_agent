# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R1
scheduled_loop: 74
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R2
computed_next_loop: 74
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: C02_GRID_DATACENTER_CABLE_ORDER_MARGIN_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

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

## 2. Round / Large Sector / Canonical Archetype Scope

R13 / loop 73 has closed, so the scheduler rolls to `R1 / loop 74`. R1 maps to `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`. This run avoids the immediately prior R1/C01 backlog-margin and R11/C03 defense-linked work, and uses C02 where the current coverage matrix has many positives but relatively fewer bad Stage2 examples.

| layer | id | definition |
|---|---|---|
| round | R1 | industrials / infrastructure / defense / grid |
| large_sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | infrastructure, grid, power equipment, defense, industrial CAPEX |
| canonical | C02_POWER_GRID_DATACENTER_CAPEX | power grid, datacenter power, cable, grid-equipment CAPEX |
| fine | C02_GRID_DATACENTER_CABLE_ORDER_MARGIN_BRIDGE_GUARD | grid/datacenter signal must become order and margin evidence |
| deep | POWER_CABLE_GRID_DATACENTER_CAPEX_TO_ORDER_MARGIN_AND_COPPER_PASS_THROUGH | cable/grid positive |
| deep | GRID_CABLE_HOLDCO_CAPEX_TO_SUBSIDIARY_ORDER_MARGIN_REPRICING | holdco grid/cable positive with 4B guard |
| deep | POWER_SUPPLY_DATACENTER_AI_THEME_WITHOUT_CUSTOMER_ORDER_OR_MARGIN_CONVERSION | power-supply/datacenter theme false start |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C02 top-covered symbols are `010120`, `267260`, `298040`, `006340`, `103590`, and `017040`. This run avoids that top-covered cluster and also avoids the immediately prior R1/C01 and R11/C03 representative symbols.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C02 | 000500 | new independent | not top-covered C02 symbol; power cable/grid/datacenter CAPEX bridge |
| C02 | 006260 | new independent | not top-covered C02 symbol; grid/cable holdco CAPEX bridge with 4B guard |
| C02 | 037030 | new independent | not top-covered C02 symbol; power-supply/datacenter theme counterexample |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web assumptions:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable columns = d,o,h,l,c,v,a,mc,s,m
```

## 5. Historical Eligibility Gate

```text
entry row exists = true
forward 180 trading days available = true
MFE/MAE 30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Corporate-action caveat:

```text
000500 has corporate-action candidate dates on 2022-11-08, 2024-11-11, and 2025-02-20; the selected 2024-01-29 forward window is treated as clean before the 2024-11-11 candidate.
006260 has only old corporate-action candidates ending 1999, outside the selected 2024 window.
037030 has corporate-action candidates ending 2018, outside the selected 2024 window.
001440/대한전선 was inspected but excluded as representative because the 2024-04-02 candidate complicates the post-January 2024 forward window.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 000500 | 가온전선 | Stage2-Actionable | 2024-01-29 | 23050 | power cable/grid/datacenter CAPEX bridge worked |
| structural_success_with_4B_drawdown_watch | 006260 | LS | Stage2-Actionable | 2024-01-29 | 85000 | grid/cable holdco CAPEX bridge worked, but high-MAE guard needed |
| failed_rerating_low_MFE_high_MAE | 037030 | 파워넷 | Stage2-Actionable | 2024-01-29 | 2985 | power-supply/datacenter theme lacked customer order and margin bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 3
4C_or_high_MAE_watch_count: 2
calibration_usable_case_count: 3
current_profile_error_count: 1
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 000500 | 가온전선 | Stage2-Actionable | 2024-01-29 | 23050 | 38.83 | 223.21 | 223.21 | -5.86 | -5.86 | -5.86 | 2024-05-13 | 74500 | -43.96 |
| 006260 | LS | Stage2-Actionable | 2024-01-29 | 85000 | 27.29 | 129.18 | 129.18 | -3.06 | -3.06 | -3.06 | 2024-05-21 | 194800 | -51.75 |
| 037030 | 파워넷 | Stage2-Actionable | 2024-01-29 | 2985 | 13.07 | 13.07 | 13.07 | -1.84 | -16.58 | -16.58 | 2024-02-19 | 3375 | -26.22 |

## 9. Case-by-Case Notes

### 9.1 000500 / 가온전선 — power cable CAPEX bridge

The entry row is 2024-01-29 at 23,050. The 30D path reaches 32,000 and the 90D/180D path reaches 74,500. This is a valid C02 route because the signal is not merely cable-price heat. The bridge is grid/datacenter CAPEX, order visibility, copper pass-through, and margin conversion. It still needs 4B watch after the fast rerating.

### 9.2 006260 / LS — holdco grid/cable CAPEX bridge with drawdown guard

The entry row is 2024-01-29 at 85,000. The path reaches 194,800, then later draws down sharply. This is a useful C02 positive because subsidiary cable/grid CAPEX and margin leverage can reach the holdco/NAV layer. It is also a warning: once the grid theme becomes crowded, 4B/high-MAE guard should stay awake.

### 9.3 037030 / 파워넷 — power-supply/datacenter theme false start

The entry row is 2024-01-29 at 2,985. The local high reaches 3,375, but the later path falls to 2,490. This is the C02 false-positive shape: power supply, datacenter, or AI-power optionality can sound adjacent to the grid supercycle, but without customer orders, revenue, margin, or CAPEX pull-through it remains a small spark without a transmission line.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C02 treats power/datacenter/AI theme adjacency as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C02 needs order/revenue/margin/CAPEX bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for small power-theme rows. |
| Full 4B non-price requirement appropriate? | Yes. 000500/006260 have non-price bridge evidence; 037030 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
000500:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after order/margin/copper pass-through bridge
  Stage3-Green = wait for stronger cash conversion and post-MFE 4B review

006260:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after grid/cable CAPEX and subsidiary-margin bridge
  Stage3-Green = reject unless holdco/NAV repricing and drawdown risk clear

037030:
  Stage2-Actionable = too generous if based only on power-supply/datacenter theme
  Stage3-Yellow = reject without customer order, margin or CAPEX pull-through bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 000500 | 0.98 | 1.00 | good full-window 4B watch after power cable CAPEX bridge |
| 006260 | 0.95 | 1.00 | good 4B watch but requires holdco/grid drawdown guard |
| 037030 | 1.00 | 1.00 | power-supply theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c02_requires_grid_datacenter_order_margin_pass_through_bridge

rule:
  For C02 power-grid/datacenter CAPEX rows, do not promote power equipment,
  cable, wire, AI-power, datacenter, or grid-adjacent Stage2 signals into Stage3-Yellow/Green
  unless at least one non-price bridge is visible:
  customer order, backlog-to-revenue conversion, datacenter/grid CAPEX pull-through,
  copper/raw-material pass-through, margin conversion, operating leverage, or FCF/cash conversion.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 121.82 | -8.5 | 33.3% | useful but can over-credit small power-theme rows |
| P0b e2r_2_0_baseline_reference | 3 | 121.82 | -8.5 | 0% | safer but may miss 000500/006260 |
| P1 sector_specific_candidate_profile | 3 | 121.82 | -8.5 | 33.3% | no broad L1 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 176.19 | -4.46 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 13.07 | -16.58 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 000500 | current_profile_correct | grid/datacenter cable order-margin bridge aligned with strong MFE |
| 006260 | current_profile_partially_correct | bridge worked, but drawdown requires 4B/high-MAE watch |
| 037030 | current_profile_false_positive | power-supply/datacenter theme produced shallow MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | C02_GRID_DATACENTER_CABLE_ORDER_MARGIN_BRIDGE_GUARD | 2 | 1 | 3 | 2 | 3 | 0 | 3 | 3 | 1 | false | true | C02 non-top-covered grid/cable/datacenter CAPEX residual reduced |

## 17. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail
residual_error_types_found:
- power-supply/datacenter theme without order/margin bridge
- grid/cable winner needs 4B watch
- holdco grid repricing high-MAE after peak
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_watch_guard
existing_axis_weakened: null
existing_axis_kept:
- stage3_green_total_min
- stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
```

## 18. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- MFE/MAE/peak/drawdown
- round/sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean forward windows
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
- 001440 as representative row because 2024-04-02 corporate-action candidate complicates the post-January 2024 window
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c02_requires_grid_datacenter_order_margin_pass_through_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"C02 grid/datacenter CAPEX rows should not promote toward Stage3-Yellow/Green unless power/grid/datacenter signal converts into customer order, backlog-to-revenue, margin/pass-through, operating leverage, or CAPEX pull-through bridge","000500 and 006260 survive with strong MFE after grid/cable/order/margin bridge; 037030 fails when power-supply/datacenter theme lacks customer order and margin bridge","TRG_R1L74_C02_000500_20240129_POWER_CABLE_DATACENTER_CAPEX_MARGIN_BRIDGE|TRG_R1L74_C02_006260_20240129_GRID_HOLDCO_CABLE_CAPEX_OPERATING_LEVERAGE_BRIDGE|TRG_R1L74_C02_037030_20240129_POWER_SUPPLY_DATACENTER_THEME_NO_ORDER_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c02_grid_capex_4b_high_mae_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,1,1,0,"Grid/cable CAPEX winners and small power-theme failures can peak before order and margin durability is confirmed; local/full-window 4B and high-MAE watch must remain active","preserves 000500/006260 positives while preventing 037030 power-theme false positive","TRG_R1L74_C02_000500_20240129_POWER_CABLE_DATACENTER_CAPEX_MARGIN_BRIDGE|TRG_R1L74_C02_006260_20240129_GRID_HOLDCO_CABLE_CAPEX_OPERATING_LEVERAGE_BRIDGE|TRG_R1L74_C02_037030_20240129_POWER_SUPPLY_DATACENTER_THEME_NO_ORDER_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R1L74_C02_000500_20240129_POWER_CABLE_DATACENTER_CAPEX_MARGIN_BRIDGE","symbol":"000500","company_name":"가온전선","round":"R1","loop":"74","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_POWER_CABLE_DATACENTER_CAPEX_MARGIN_BRIDGE","deep_sub_archetype_id":"POWER_CABLE_GRID_DATACENTER_CAPEX_TO_ORDER_MARGIN_AND_COPPER_PASS_THROUGH","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C02 grid/datacenter CAPEX rows require customer/order, backlog-to-revenue, margin, copper pass-through, operating leverage, or grid/datacenter CAPEX pull-through; power/AI/datacenter theme alone is insufficient."}
{"row_type":"case","case_id":"R1L74_C02_006260_20240129_GRID_HOLDCO_CABLE_CAPEX_OPERATING_LEVERAGE_BRIDGE","symbol":"006260","company_name":"LS","round":"R1","loop":"74","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_HOLDCO_CABLE_CAPEX_OPERATING_LEVERAGE_BRIDGE","deep_sub_archetype_id":"GRID_CABLE_HOLDCO_CAPEX_TO_SUBSIDIARY_ORDER_MARGIN_REPRICING","case_type":"structural_success_with_4B_drawdown_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct","price_source":"Songdaiki/stock-web","notes":"C02 grid/datacenter CAPEX rows require customer/order, backlog-to-revenue, margin, copper pass-through, operating leverage, or grid/datacenter CAPEX pull-through; power/AI/datacenter theme alone is insufficient."}
{"row_type":"case","case_id":"R1L74_C02_037030_20240129_POWER_SUPPLY_DATACENTER_THEME_NO_ORDER_BRIDGE","symbol":"037030","company_name":"파워넷","round":"R1","loop":"74","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_POWER_SUPPLY_DATACENTER_THEME_WITHOUT_ORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"POWER_SUPPLY_DATACENTER_AI_THEME_WITHOUT_CUSTOMER_ORDER_OR_MARGIN_CONVERSION","case_type":"failed_rerating_low_MFE_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C02 grid/datacenter CAPEX rows require customer/order, backlog-to-revenue, margin, copper pass-through, operating leverage, or grid/datacenter CAPEX pull-through; power/AI/datacenter theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R1L74_C02_000500_20240129_POWER_CABLE_DATACENTER_CAPEX_MARGIN_BRIDGE","case_id":"R1L74_C02_000500_20240129_POWER_CABLE_DATACENTER_CAPEX_MARGIN_BRIDGE","symbol":"000500","company_name":"가온전선","round":"R1","loop":"74","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_POWER_CABLE_DATACENTER_CAPEX_MARGIN_BRIDGE","deep_sub_archetype_id":"POWER_CABLE_GRID_DATACENTER_CAPEX_TO_ORDER_MARGIN_AND_COPPER_PASS_THROUGH","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":23050,"evidence_available_at_that_date":"source_proxy_power_cable_grid_datacenter_capex_order_margin_copper_pass_through_bridge; evidence_url_pending","evidence_source":"source_proxy_power_cable_grid_datacenter_capex_order_margin_copper_pass_through_bridge; evidence_url_pending","bridge_summary":"power cable/datacenter-grid CAPEX theme converted into order visibility, copper pass-through and margin bridge rather than pure wire theme heat","stage2_evidence_fields":["power_cable_grid_CAPEX","datacenter_power_demand_proxy","relative_strength","order_margin_bridge_proxy"],"stage3_evidence_fields":["order_to_revenue_visibility","copper_pass_through_margin_bridge","grid_customer_pullthrough"],"stage4b_evidence_fields":["post_MFE_peak_watch","cable_grid_crowding_after_CAPEX_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000500/2024.csv","profile_path":"atlas/symbol_profiles/000/000500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":38.83,"MFE_90D_pct":223.21,"MFE_180D_pct":223.21,"MFE_1Y_pct":223.21,"MFE_2Y_pct":223.21,"MAE_30D_pct":-5.86,"MAE_90D_pct":-5.86,"MAE_180D_pct":-5.86,"MAE_1Y_pct":-5.86,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-13","peak_price":74500,"drawdown_after_peak_pct":-43.96,"green_lateness_ratio":"0.33","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_power_cable_capex_margin_bridge","four_b_evidence_type":"non_price_grid_datacenter_order_margin_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L74_C02_000500_20240129_POWER_CABLE_DATACENTER_CAPEX_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L74_C02_006260_20240129_GRID_HOLDCO_CABLE_CAPEX_OPERATING_LEVERAGE_BRIDGE","case_id":"R1L74_C02_006260_20240129_GRID_HOLDCO_CABLE_CAPEX_OPERATING_LEVERAGE_BRIDGE","symbol":"006260","company_name":"LS","round":"R1","loop":"74","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_HOLDCO_CABLE_CAPEX_OPERATING_LEVERAGE_BRIDGE","deep_sub_archetype_id":"GRID_CABLE_HOLDCO_CAPEX_TO_SUBSIDIARY_ORDER_MARGIN_REPRICING","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":85000,"evidence_available_at_that_date":"source_proxy_grid_holdco_cable_CAPEX_subsidiary_order_margin_operating_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_grid_holdco_cable_CAPEX_subsidiary_order_margin_operating_leverage_bridge; evidence_url_pending","bridge_summary":"grid/cable CAPEX repricing reached the holdco through subsidiary order and margin leverage, but post-peak drawdown requires 4B/high-MAE watch","stage2_evidence_fields":["grid_cable_CAPEX","holdco_subsidiary_pullthrough","relative_strength","order_margin_operating_leverage_proxy"],"stage3_evidence_fields":["subsidiary_order_to_NAV_visibility","margin_operating_leverage","grid_CAPEX_customer_bridge"],"stage4b_evidence_fields":["post_MFE_peak_watch","holdco_valuation_repricing_after_grid_rerating"],"stage4c_evidence_fields":["high_MAE_watch_after_peak"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv","profile_path":"atlas/symbol_profiles/006/006260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.29,"MFE_90D_pct":129.18,"MFE_180D_pct":129.18,"MFE_1Y_pct":129.18,"MFE_2Y_pct":129.18,"MAE_30D_pct":-3.06,"MAE_90D_pct":-3.06,"MAE_180D_pct":-3.06,"MAE_1Y_pct":-3.06,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":194800,"drawdown_after_peak_pct":-51.75,"green_lateness_ratio":"0.37","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_4B_watch_but_requires_holdco_grid_drawdown_guard","four_b_evidence_type":"non_price_grid_datacenter_order_margin_bridge","four_c_protection_label":"high_MAE_watch_after_peak","trigger_outcome_label":"structural_success_but_needs_4B_high_MAE_guard","current_profile_verdict":"current_profile_partially_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L74_C02_006260_20240129_GRID_HOLDCO_CABLE_CAPEX_OPERATING_LEVERAGE_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L74_C02_037030_20240129_POWER_SUPPLY_DATACENTER_THEME_NO_ORDER_BRIDGE","case_id":"R1L74_C02_037030_20240129_POWER_SUPPLY_DATACENTER_THEME_NO_ORDER_BRIDGE","symbol":"037030","company_name":"파워넷","round":"R1","loop":"74","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_POWER_SUPPLY_DATACENTER_THEME_WITHOUT_ORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"POWER_SUPPLY_DATACENTER_AI_THEME_WITHOUT_CUSTOMER_ORDER_OR_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":2985,"evidence_available_at_that_date":"source_proxy_power_supply_datacenter_AI_theme_without_customer_order_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_power_supply_datacenter_AI_theme_without_customer_order_margin_bridge; evidence_url_pending","bridge_summary":"power-supply/datacenter or AI power theme did not convert into visible customer order, margin, or grid CAPEX bridge; upside stayed shallow and MAE expanded","stage2_evidence_fields":["power_supply_datacenter_theme","AI_power_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","customer_order_bridge_absent","margin_conversion_absent"],"stage4c_evidence_fields":["high_MAE_without_order_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/037/037030/2024.csv","profile_path":"atlas/symbol_profiles/037/037030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.07,"MFE_90D_pct":13.07,"MFE_180D_pct":13.07,"MFE_1Y_pct":13.07,"MFE_2Y_pct":13.07,"MAE_30D_pct":-1.84,"MAE_90D_pct":-16.58,"MAE_180D_pct":-16.58,"MAE_1Y_pct":-16.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":3375,"drawdown_after_peak_pct":-26.22,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"power_supply_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"power_theme_without_order_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L74_C02_037030_20240129_POWER_SUPPLY_DATACENTER_THEME_NO_ORDER_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L74_C02_000500_20240129_POWER_CABLE_DATACENTER_CAPEX_MARGIN_BRIDGE","trigger_id":"TRG_R1L74_C02_000500_20240129_POWER_CABLE_DATACENTER_CAPEX_MARGIN_BRIDGE","symbol":"000500","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"grid_CAPEX_score":12,"datacenter_power_score":11,"order_backlog_score":12,"margin_pass_through_score":11,"relative_strength_score":10,"risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"grid_CAPEX_score":15,"datacenter_power_score":13,"order_backlog_score":15,"margin_pass_through_score":14,"relative_strength_score":8,"risk_penalty":5},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow","changed_components":["grid_CAPEX_score","datacenter_power_score","order_backlog_score","margin_pass_through_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C02 row is promoted only because power/grid CAPEX converts into customer order, margin/pass-through and revenue visibility.","MFE_90D_pct":223.21,"MAE_90D_pct":-5.86,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L74_C02_006260_20240129_GRID_HOLDCO_CABLE_CAPEX_OPERATING_LEVERAGE_BRIDGE","trigger_id":"TRG_R1L74_C02_006260_20240129_GRID_HOLDCO_CABLE_CAPEX_OPERATING_LEVERAGE_BRIDGE","symbol":"006260","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"grid_CAPEX_score":11,"datacenter_power_score":10,"order_backlog_score":11,"margin_pass_through_score":9,"relative_strength_score":11,"risk_penalty":6},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"grid_CAPEX_score":14,"datacenter_power_score":12,"order_backlog_score":14,"margin_pass_through_score":12,"relative_strength_score":8,"risk_penalty":10},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["grid_CAPEX_score","datacenter_power_score","order_backlog_score","margin_pass_through_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C02 bridge works, but post-peak drawdown and holdco repricing risk require 4B/high-MAE guard and prevent Green loosening.","MFE_90D_pct":129.18,"MAE_90D_pct":-3.06,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L74_C02_037030_20240129_POWER_SUPPLY_DATACENTER_THEME_NO_ORDER_BRIDGE","trigger_id":"TRG_R1L74_C02_037030_20240129_POWER_SUPPLY_DATACENTER_THEME_NO_ORDER_BRIDGE","symbol":"037030","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"grid_CAPEX_score":6,"datacenter_power_score":8,"order_backlog_score":1,"margin_pass_through_score":1,"relative_strength_score":8,"risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"grid_CAPEX_score":3,"datacenter_power_score":4,"order_backlog_score":0,"margin_pass_through_score":0,"relative_strength_score":4,"risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["grid_CAPEX_score","datacenter_power_score","order_backlog_score","margin_pass_through_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C02 guard demotes power-supply/datacenter theme rows when customer order, margin or CAPEX pull-through bridge is absent.","MFE_90D_pct":13.07,"MAE_90D_pct":-16.58,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c02_requires_grid_datacenter_order_margin_pass_through_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"C02 grid/datacenter CAPEX rows should not promote toward Stage3-Yellow/Green unless power/grid/datacenter signal converts into customer order, backlog-to-revenue, margin/pass-through, operating leverage, or CAPEX pull-through bridge","000500 and 006260 survive with strong MFE after grid/cable/order/margin bridge; 037030 fails when power-supply/datacenter theme lacks customer order and margin bridge","TRG_R1L74_C02_000500_20240129_POWER_CABLE_DATACENTER_CAPEX_MARGIN_BRIDGE|TRG_R1L74_C02_006260_20240129_GRID_HOLDCO_CABLE_CAPEX_OPERATING_LEVERAGE_BRIDGE|TRG_R1L74_C02_037030_20240129_POWER_SUPPLY_DATACENTER_THEME_NO_ORDER_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c02_grid_capex_4b_high_mae_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,1,1,0,"Grid/cable CAPEX winners and small power-theme failures can peak before order and margin durability is confirmed; local/full-window 4B and high-MAE watch must remain active","preserves 000500/006260 positives while preventing 037030 power-theme false positive","TRG_R1L74_C02_000500_20240129_POWER_CABLE_DATACENTER_CAPEX_MARGIN_BRIDGE|TRG_R1L74_C02_006260_20240129_GRID_HOLDCO_CABLE_CAPEX_OPERATING_LEVERAGE_BRIDGE|TRG_R1L74_C02_037030_20240129_POWER_SUPPLY_DATACENTER_THEME_NO_ORDER_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"74","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["power_supply_datacenter_theme_without_order_margin_bridge","grid_cable_winner_needs_4B_watch","holdco_grid_repricing_high_MAE_after_peak"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

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
- price-only/power-theme-only rows cannot promote Stage2/Stage3.
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
11. Add validation that C02 grid/datacenter CAPEX rows cannot promote without customer order, backlog-to-revenue, datacenter/grid CAPEX pull-through, pass-through, margin, operating leverage, or FCF bridge.
12. Add validation that corporate-action-contaminated candidates, such as 001440's 2024-04-02 window, are not representative rows unless a clean forward window is available.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R1
completed_loop = 74
next_round = R2
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

## 23. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

Stock-web:
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/000/000500.json
atlas/symbol_profiles/006/006260.json
atlas/symbol_profiles/037/037030.json
atlas/symbol_profiles/001/001440.json
atlas/ohlcv_tradable_by_symbol_year/000/000500/2024.csv
atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv
atlas/ohlcv_tradable_by_symbol_year/037/037030/2024.csv
atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv
```

This loop starts loop 74 with R1 and adds 3 new independent C02 representative cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R1/L1.
