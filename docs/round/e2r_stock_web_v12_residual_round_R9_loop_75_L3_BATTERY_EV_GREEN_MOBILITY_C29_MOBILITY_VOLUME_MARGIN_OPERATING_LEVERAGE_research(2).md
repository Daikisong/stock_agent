# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R9
scheduled_loop: 75
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R10
computed_next_loop: 75
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
r9_branch: L3_MOBILITY_BRANCH_ALLOWED
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

R9 allows either the L3 mobility branch or the L9 construction/real-estate branch. The previous R9/R10 path used L9/C30 construction repeatedly, so this run rotates to the allowed L3/C29 mobility branch. The target is not the top-covered completed vehicle and tire cluster. It is the auto-parts/mobility supplier layer where MFE only matters if volume, mix, margin and operating leverage are visible.

| layer | id | definition |
|---|---|---|
| round | R9 | mobility or construction bridge round |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | EV, mobility, auto parts, green mobility |
| canonical | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | volume, margin, operating leverage and mobility cycle |
| fine | C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_GUARD | mobility signal must become volume/mix/margin evidence |
| deep | AUTO_LAMP_AND_ELECTRONICS_CUSTOMER_VOLUME_MIX_TO_MARGIN_OPERATING_LEVERAGE | lamp/electronics positive |
| deep | POWERTRAIN_ELECTRIFICATION_ROBOTICS_OPTIONALITY_WITHOUT_VOLUME_MARGIN_OR_BACKLOG_CONVERSION | powertrain/robotics false positive |
| deep | WIRE_HARNESS_AUTO_PARTS_THEME_WITHOUT_CUSTOMER_VOLUME_MARGIN_OR_CASHFLOW_CONVERSION | wire harness false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C29 top-covered symbols are `UNKNOWN_SYMBOL`, `000270`, `161390`, `012330`, `005380`, and `018880`. This run avoids that cluster and also avoids the recent R9/L9 construction branch.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C29 | 005850 | new independent | not top-covered C29 symbol; auto lamp/electronics volume-mix margin bridge |
| C29 | 011210 | new independent | not top-covered C29 symbol; powertrain/electrification/robotics MFE without durable margin bridge |
| C29 | 019180 | new independent | not top-covered C29 symbol; wire harness theme low-quality MFE/high-MAE counterexample |
| reviewed | 204320 | not used | clean profile, but selected set had clearer positive/counterexample balance |

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
005850 has corporate-action candidates ending 2019-04-16, outside the selected 2024 representative window.
011210 has no corporate-action candidate dates.
019180 has corporate-action candidates ending 2006-05-08, outside the selected 2024 representative window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| auto_lamp_volume_mix_success_then_4B_drawdown_watch | 005850 | 에스엘 | Stage2-Actionable | 2024-04-29 | 34150 | auto lamp/electronics volume-mix margin bridge worked, but post-peak drawdown required 4B |
| powertrain_robotics_MFE_then_drawdown_counterexample | 011210 | 현대위아 | Stage2-Actionable | 2024-02-01 | 60400 | powertrain/electrification/robotics MFE lacked durable volume/margin bridge |
| wire_harness_theme_low_MFE_high_MAE_counterexample | 019180 | 티에이치엔 | Stage2-Actionable | 2024-02-28 | 3850 | wire-harness auto-parts spike lacked customer-volume/margin/cashflow bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 3
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 005850 | 에스엘 | Stage2-Actionable | 2024-04-29 | 34150 | 30.16 | 39.53 | 39.53 | -5.27 | -10.98 | -16.84 | 2024-06-17 | 47650 | -40.4 |
| 011210 | 현대위아 | Stage2-Actionable | 2024-02-01 | 60400 | 10.93 | 10.93 | 10.93 | -6.46 | -7.95 | -24.75 | 2024-02-05 | 67000 | -32.16 |
| 019180 | 티에이치엔 | Stage2-Actionable | 2024-02-28 | 3850 | 9.87 | 9.87 | 9.87 | -8.05 | -12.99 | -23.38 | 2024-02-28 | 4230 | -30.26 |

## 9. Case-by-Case Notes

### 9.1 005850 / 에스엘 — auto lamp volume-mix margin bridge

The entry row is 2024-04-29 at 34,150. The path reached 44,450 in the early recovery window and 47,650 at the full-window peak. This is a valid C29 positive because the evidence family is not just mobility beta. The bridge is customer mix, auto-lamp/electronics volume, margin and operating leverage. The post-peak low still requires 4B/drawdown watch.

### 9.2 011210 / 현대위아 — powertrain/robotics theme without durable bridge

The entry row is 2024-02-01 at 60,400. It reached 67,000, but the later low reached 45,450. The initial MFE did not prove volume, backlog-to-revenue, operating leverage or margin durability. This row should stay 4B/high-MAE watch rather than Stage3-Green evidence.

### 9.3 019180 / 티에이치엔 — wire harness low-quality MFE

The entry row is 2024-02-28 at 3,850. The same local window reached 4,230, but the 180D low fell to 2,950. This is the C29 false-positive shape: auto-parts or wire-harness theme heat without customer-volume, margin and cashflow bridge is a local spark, not an engine.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C29 treats mobility/auto-parts MFE as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C29 needs volume/mix/margin/operating-leverage bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 019180 local spike and 011210 MFE fade. |
| Full 4B non-price requirement appropriate? | Yes. 005850 has bridge evidence; 011210/019180 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
005850:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after customer volume / mix / margin bridge
  Stage3-Green = reject unless post-peak drawdown and margin durability clear

011210:
  Stage2-Actionable = acceptable only as powertrain/robotics watch
  Stage3-Yellow = reject without volume, backlog-to-revenue, margin and operating leverage bridge
  Stage3-Green = reject despite MFE

019180:
  Stage2-Actionable = too generous if based only on wire-harness/auto-parts theme
  Stage3-Yellow = reject without customer-volume, margin and cashflow bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 005850 | 0.93 | 1.00 | auto lamp volume/mix bridge positive but full-window 4B/drawdown watch |
| 011210 | 1.00 | 1.00 | powertrain/robotics MFE but no durable margin bridge; keep 4B/high-MAE watch |
| 019180 | 1.00 | 1.00 | wire-harness theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c29_requires_volume_mix_margin_operating_leverage_bridge

rule:
  For C29 mobility volume/margin rows, do not promote EV, mobility,
  auto parts, lamps/electronics, powertrain, robotics, wire harness, or supplier-cycle
  Stage2 signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  customer volume, mix improvement, operating leverage, margin conversion,
  backlog-to-revenue conversion, utilization recovery, FCF/cash conversion,
  or earnings revision tied to mobility volume economics.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 20.11 | -10.64 | 66.7% | too generous to mobility/auto-parts theme MFE |
| P0b e2r_2_0_baseline_reference | 3 | 20.11 | -10.64 | 33.3% | safer but may miss 005850 |
| P1 sector_specific_candidate_profile | 3 | 20.11 | -10.64 | 66.7% | no broad L3 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 39.53 | -10.98 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 10.4 | -10.47 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 005850 | current_profile_correct_but_no_green | volume/mix/margin bridge aligned with MFE, but post-peak drawdown blocks Green |
| 011210 | current_profile_false_positive_if_green | powertrain/robotics MFE lacked durable volume/margin bridge |
| 019180 | current_profile_false_positive | wire-harness theme produced low-quality local MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R9 allowed L3/C29 non-top-covered mobility residual reduced |

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
- mobility theme without volume/margin bridge
- auto lamp winner needs 4B watch
- wire-harness low-quality MFE high-MAE
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
- R9 allowed L3 branch consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/report URLs
- exact customer/order announcement URLs
- production scoring behavior
- live candidate status
- 204320 as representative row; reviewed but not selected
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_requires_volume_mix_margin_operating_leverage_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"C29 mobility rows should not promote toward Stage3-Yellow/Green unless mobility/auto-parts signal converts into customer volume, mix, operating leverage, margin, backlog-to-revenue, utilization, or cashflow bridge","005850 survives after auto-lamp volume/mix-margin bridge; 011210 and 019180 are demoted because powertrain/robotics or wire-harness themes lacked durable volume/margin bridge","TRG_R9L75_C29_005850_20240429_AUTO_LAMP_VOLUME_MIX_MARGIN_BRIDGE|TRG_R9L75_C29_011210_20240201_POWERTRAIN_ROBOTICS_THEME_NO_DURABLE_MARGIN_BRIDGE|TRG_R9L75_C29_019180_20240228_WIRE_HARNESS_THEME_LOW_QUALITY_MFE",3,3,2,medium,canonical_shadow_only,"not production; R9 allowed L3 mobility branch"
shadow_weight,c29_mobility_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,1,1,0,"Mobility/auto-parts winners and theme false starts can peak before volume/margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 005850 guarded positive while preventing 011210/019180 mobility-theme false positives","TRG_R9L75_C29_005850_20240429_AUTO_LAMP_VOLUME_MIX_MARGIN_BRIDGE|TRG_R9L75_C29_011210_20240201_POWERTRAIN_ROBOTICS_THEME_NO_DURABLE_MARGIN_BRIDGE|TRG_R9L75_C29_019180_20240228_WIRE_HARNESS_THEME_LOW_QUALITY_MFE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R9L75_C29_005850_20240429_AUTO_LAMP_VOLUME_MIX_MARGIN_BRIDGE","symbol":"005850","company_name":"에스엘","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_AUTO_LAMP_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE","deep_sub_archetype_id":"AUTO_LAMP_AND_ELECTRONICS_CUSTOMER_VOLUME_MIX_TO_MARGIN_OPERATING_LEVERAGE","case_type":"auto_lamp_volume_mix_success_then_4B_drawdown_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R9 allowed L3 branch. C29 mobility rows require customer volume, mix, operating leverage, margin, backlog-to-revenue, utilization, or cashflow bridge; auto-parts/mobility theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R9L75_C29_011210_20240201_POWERTRAIN_ROBOTICS_THEME_NO_DURABLE_MARGIN_BRIDGE","symbol":"011210","company_name":"현대위아","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_POWERTRAIN_ROBOTICS_THEME_WITHOUT_DURABLE_MARGIN_BRIDGE","deep_sub_archetype_id":"POWERTRAIN_ELECTRIFICATION_ROBOTICS_OPTIONALITY_WITHOUT_VOLUME_MARGIN_OR_BACKLOG_CONVERSION","case_type":"powertrain_robotics_MFE_then_drawdown_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"R9 allowed L3 branch. C29 mobility rows require customer volume, mix, operating leverage, margin, backlog-to-revenue, utilization, or cashflow bridge; auto-parts/mobility theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R9L75_C29_019180_20240228_WIRE_HARNESS_THEME_LOW_QUALITY_MFE","symbol":"019180","company_name":"티에이치엔","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_WIRE_HARNESS_THEME_WITHOUT_VOLUME_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"WIRE_HARNESS_AUTO_PARTS_THEME_WITHOUT_CUSTOMER_VOLUME_MARGIN_OR_CASHFLOW_CONVERSION","case_type":"wire_harness_theme_low_MFE_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R9 allowed L3 branch. C29 mobility rows require customer volume, mix, operating leverage, margin, backlog-to-revenue, utilization, or cashflow bridge; auto-parts/mobility theme MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R9L75_C29_005850_20240429_AUTO_LAMP_VOLUME_MIX_MARGIN_BRIDGE","case_id":"R9L75_C29_005850_20240429_AUTO_LAMP_VOLUME_MIX_MARGIN_BRIDGE","symbol":"005850","company_name":"에스엘","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_AUTO_LAMP_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE","deep_sub_archetype_id":"AUTO_LAMP_AND_ELECTRONICS_CUSTOMER_VOLUME_MIX_TO_MARGIN_OPERATING_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":34150,"evidence_available_at_that_date":"source_proxy_auto_lamp_customer_mix_volume_margin_operating_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_auto_lamp_customer_mix_volume_margin_operating_leverage_bridge; evidence_url_pending","bridge_summary":"auto lamp/electronics customer mix and volume path converted into margin and operating-leverage bridge, but post-peak sector drawdown required 4B watch","stage2_evidence_fields":["auto_lamp_volume","customer_mix_proxy","relative_strength","margin_leverage_proxy"],"stage3_evidence_fields":["volume_to_revenue_visibility","mix_margin_bridge","operating_leverage_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","auto_parts_crowding_after_margin_rerating"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv","profile_path":"atlas/symbol_profiles/005/005850.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":30.16,"MFE_90D_pct":39.53,"MFE_180D_pct":39.53,"MFE_1Y_pct":39.53,"MFE_2Y_pct":39.53,"MAE_30D_pct":-5.27,"MAE_90D_pct":-10.98,"MAE_180D_pct":-16.84,"MAE_1Y_pct":-16.84,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-17","peak_price":47650,"drawdown_after_peak_pct":-40.4,"green_lateness_ratio":"0.43","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"auto_lamp_volume_mix_bridge_positive_but_full_window_4B_drawdown_watch","four_b_evidence_type":"non_price_volume_mix_margin_bridge","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L75_C29_005850_20240429_AUTO_LAMP_VOLUME_MIX_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R9L75_C29_011210_20240201_POWERTRAIN_ROBOTICS_THEME_NO_DURABLE_MARGIN_BRIDGE","case_id":"R9L75_C29_011210_20240201_POWERTRAIN_ROBOTICS_THEME_NO_DURABLE_MARGIN_BRIDGE","symbol":"011210","company_name":"현대위아","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_POWERTRAIN_ROBOTICS_THEME_WITHOUT_DURABLE_MARGIN_BRIDGE","deep_sub_archetype_id":"POWERTRAIN_ELECTRIFICATION_ROBOTICS_OPTIONALITY_WITHOUT_VOLUME_MARGIN_OR_BACKLOG_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":60400,"evidence_available_at_that_date":"source_proxy_powertrain_electrification_robotics_theme_without_volume_margin_backlog_bridge; evidence_url_pending","evidence_source":"source_proxy_powertrain_electrification_robotics_theme_without_volume_margin_backlog_bridge; evidence_url_pending","bridge_summary":"powertrain/electrification/robotics optionality produced MFE, but volume, backlog-to-revenue, operating leverage and margin bridge did not become durable","stage2_evidence_fields":["powertrain_electrification_theme","robotics_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["theme_local_peak","volume_margin_bridge_absent","operating_leverage_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_volume_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011210/2024.csv","profile_path":"atlas/symbol_profiles/011/011210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.93,"MFE_90D_pct":10.93,"MFE_180D_pct":10.93,"MFE_1Y_pct":10.93,"MFE_2Y_pct":10.93,"MAE_30D_pct":-6.46,"MAE_90D_pct":-7.95,"MAE_180D_pct":-24.75,"MAE_1Y_pct":-24.75,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-05","peak_price":67000,"drawdown_after_peak_pct":-32.16,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"powertrain_robotics_theme_MFE_but_no_margin_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"mobility_theme_without_volume_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"MFE_then_drawdown_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L75_C29_011210_20240201_POWERTRAIN_ROBOTICS_THEME_NO_DURABLE_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R9L75_C29_019180_20240228_WIRE_HARNESS_THEME_LOW_QUALITY_MFE","case_id":"R9L75_C29_019180_20240228_WIRE_HARNESS_THEME_LOW_QUALITY_MFE","symbol":"019180","company_name":"티에이치엔","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_WIRE_HARNESS_THEME_WITHOUT_VOLUME_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"WIRE_HARNESS_AUTO_PARTS_THEME_WITHOUT_CUSTOMER_VOLUME_MARGIN_OR_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":3850,"evidence_available_at_that_date":"source_proxy_wire_harness_auto_parts_theme_without_customer_volume_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_wire_harness_auto_parts_theme_without_customer_volume_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"wire-harness/auto-parts theme produced a local price spike but lacked customer-volume, margin, operating leverage and cashflow bridge","stage2_evidence_fields":["wire_harness_theme","auto_parts_beta","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_theme_peak","customer_volume_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_volume_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/019/019180/2024.csv","profile_path":"atlas/symbol_profiles/019/019180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.87,"MFE_90D_pct":9.87,"MFE_180D_pct":9.87,"MFE_1Y_pct":9.87,"MFE_2Y_pct":9.87,"MAE_30D_pct":-8.05,"MAE_90D_pct":-12.99,"MAE_180D_pct":-23.38,"MAE_1Y_pct":-23.38,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-28","peak_price":4230,"drawdown_after_peak_pct":-30.26,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"wire_harness_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"mobility_theme_without_volume_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"low_quality_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L75_C29_019180_20240228_WIRE_HARNESS_THEME_LOW_QUALITY_MFE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L75_C29_005850_20240429_AUTO_LAMP_VOLUME_MIX_MARGIN_BRIDGE","trigger_id":"TRG_R9L75_C29_005850_20240429_AUTO_LAMP_VOLUME_MIX_MARGIN_BRIDGE","symbol":"005850","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"volume_score":12,"mix_margin_score":12,"operating_leverage_score":11,"cashflow_bridge_score":9,"relative_strength_score":10,"theme_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"volume_score":15,"mix_margin_score":15,"operating_leverage_score":14,"cashflow_bridge_score":12,"relative_strength_score":8,"theme_risk_penalty":8},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["volume_score","mix_margin_score","operating_leverage_score","cashflow_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C29 row is promoted only because mobility/auto-parts signal converts into customer volume, mix, margin and operating-leverage bridge; post-MFE 4B drawdown watch blocks Green.","MFE_90D_pct":39.53,"MAE_90D_pct":-10.98,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L75_C29_011210_20240201_POWERTRAIN_ROBOTICS_THEME_NO_DURABLE_MARGIN_BRIDGE","trigger_id":"TRG_R9L75_C29_011210_20240201_POWERTRAIN_ROBOTICS_THEME_NO_DURABLE_MARGIN_BRIDGE","symbol":"011210","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"volume_score":4,"mix_margin_score":2,"operating_leverage_score":1,"cashflow_bridge_score":0,"relative_strength_score":10,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"volume_score":1,"mix_margin_score":0,"operating_leverage_score":0,"cashflow_bridge_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["volume_score","mix_margin_score","operating_leverage_score","cashflow_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C29 guard demotes mobility/auto-parts theme rows when customer-volume, mix-margin, operating-leverage and cashflow bridge are absent.","MFE_90D_pct":10.93,"MAE_90D_pct":-7.95,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L75_C29_019180_20240228_WIRE_HARNESS_THEME_LOW_QUALITY_MFE","trigger_id":"TRG_R9L75_C29_019180_20240228_WIRE_HARNESS_THEME_LOW_QUALITY_MFE","symbol":"019180","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"volume_score":4,"mix_margin_score":2,"operating_leverage_score":1,"cashflow_bridge_score":0,"relative_strength_score":10,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"volume_score":1,"mix_margin_score":0,"operating_leverage_score":0,"cashflow_bridge_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["volume_score","mix_margin_score","operating_leverage_score","cashflow_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C29 guard demotes mobility/auto-parts theme rows when customer-volume, mix-margin, operating-leverage and cashflow bridge are absent.","MFE_90D_pct":9.87,"MAE_90D_pct":-12.99,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_requires_volume_mix_margin_operating_leverage_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"C29 mobility rows should not promote toward Stage3-Yellow/Green unless mobility/auto-parts signal converts into customer volume, mix, operating leverage, margin, backlog-to-revenue, utilization, or cashflow bridge","005850 survives after auto-lamp volume/mix-margin bridge; 011210 and 019180 are demoted because powertrain/robotics or wire-harness themes lacked durable volume/margin bridge","TRG_R9L75_C29_005850_20240429_AUTO_LAMP_VOLUME_MIX_MARGIN_BRIDGE|TRG_R9L75_C29_011210_20240201_POWERTRAIN_ROBOTICS_THEME_NO_DURABLE_MARGIN_BRIDGE|TRG_R9L75_C29_019180_20240228_WIRE_HARNESS_THEME_LOW_QUALITY_MFE",3,3,2,medium,canonical_shadow_only,"not production; R9 allowed L3 mobility branch"
shadow_weight,c29_mobility_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,1,1,0,"Mobility/auto-parts winners and theme false starts can peak before volume/margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 005850 guarded positive while preventing 011210/019180 mobility-theme false positives","TRG_R9L75_C29_005850_20240429_AUTO_LAMP_VOLUME_MIX_MARGIN_BRIDGE|TRG_R9L75_C29_011210_20240201_POWERTRAIN_ROBOTICS_THEME_NO_DURABLE_MARGIN_BRIDGE|TRG_R9L75_C29_019180_20240228_WIRE_HARNESS_THEME_LOW_QUALITY_MFE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["mobility_theme_without_volume_margin_bridge","auto_lamp_winner_needs_4B_watch","wire_harness_low_quality_MFE_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R9-specific handling

- R9 may use `L3_BATTERY_EV_GREEN_MOBILITY` or `L9_CONSTRUCTION_REALESTATE_HOUSING`.
- This MD uses the allowed L3 mobility branch.
- Validate `round_schedule_status=valid` and `round_sector_consistency=pass` before accepting rows.

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
- price-only/mobility-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R9 allowed branch and large_sector_id.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C29 mobility volume/margin rows cannot promote without customer volume, mix improvement, operating leverage, margin conversion, backlog-to-revenue conversion, utilization recovery, FCF/cash conversion, or earnings revision tied to mobility volume economics.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R9
completed_loop = 75
next_round = R10
next_loop = 75
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
atlas/symbol_profiles/005/005850.json
atlas/symbol_profiles/011/011210.json
atlas/symbol_profiles/019/019180.json
atlas/symbol_profiles/204/204320.json
atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv
atlas/ohlcv_tradable_by_symbol_year/011/011210/2024.csv
atlas/ohlcv_tradable_by_symbol_year/019/019180/2024.csv
atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv
```

This loop continues loop 75 with R9 and adds 3 new independent C29 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R9/L3.
