# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R9
scheduled_loop: 73
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R10
computed_next_loop: 73
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: C29_AUTO_PARTS_CUSTOMER_VOLUME_MIX_MARGIN_BRIDGE_GUARD
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

R9 permits the L3 mobility branch or the L9 construction branch. This run stays in the L3/C29 mobility branch, but avoids the previous R9 shipping/logistics sub-branch and the top-covered OEM/auto cluster. The residual target is auto-parts-specific: customer/OEM volume, product mix, margin, and operating leverage must be visible before auto electronics or EV/smartcar price strength can travel upward.

| layer | id | definition |
|---|---|---|
| round | R9 | mobility / transport bridge round |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | mobility, transport, auto-parts, logistics, EV-adjacent |
| canonical | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | mobility volume, mix, margin and operating leverage |
| fine | C29_AUTO_PARTS_CUSTOMER_VOLUME_MIX_MARGIN_BRIDGE_GUARD | auto-parts signal must become customer volume and margin bridge |
| deep | GLOBAL_OEM_LIGHTING_EV_MIX_TO_MARGIN_OPERATING_LEVERAGE | lighting/EV mix margin success |
| deep | GLOBAL_AUTO_CHASSIS_VOLUME_OPERATING_LEVERAGE_TO_PEAK_REVERSAL | chassis volume/margin success with 4B guard |
| deep | SMARTCAR_ELECTRONICS_THEME_PRICE_SPIKE_WITHOUT_CUSTOMER_VOLUME_MARGIN_CONVERSION | smartcar/auto-electronics false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C29 top-covered symbols are `UNKNOWN_SYMBOL`, `000270`, `161390`, `012330`, `005380`, and `018880`. This run avoids that top cluster and also avoids the previous R9 transport/logistics representatives `028670`, `086280`, and `005880`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C29 | 005850 | new independent | not top-covered C29 symbol; lighting/OEM mix margin bridge |
| C29 | 010690 | new independent | not top-covered C29 symbol; chassis/OEM volume margin bridge with 4B guard |
| C29 | 012860 | new independent | not top-covered C29 symbol; smartcar/auto-electronics theme counterexample |

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
005850 has historical corporate-action candidates through 2019, outside the selected 2023 window.
010690 has historical corporate-action candidates through 2001, outside the selected 2023 window.
012860 has historical corporate-action candidates through 2020, outside the selected 2023 window.
All three representative windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 005850 | 에스엘 | Stage2-Actionable | 2023-03-23 | 26100 | lighting/OEM volume-mix margin bridge worked |
| structural_success_with_high_MAE_watch | 010690 | 화신 | Stage2-Actionable | 2023-03-23 | 11400 | chassis/OEM volume-margins worked but high-MAE guard required |
| failed_rerating_low_MFE_high_MAE | 012860 | 모베이스전자 | Stage2-Actionable | 2023-05-09 | 3200 | smartcar/auto-electronics theme lacked customer/margin bridge |

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
| 005850 | 에스엘 | Stage2-Actionable | 2023-03-23 | 26100 | 30.46 | 62.45 | 62.45 | -2.3 | -2.3 | -2.3 | 2023-07-17 | 42400 | -32.78 |
| 010690 | 화신 | Stage2-Actionable | 2023-03-23 | 11400 | 42.46 | 99.12 | 99.12 | -5.35 | -5.35 | -12.81 | 2023-07-06 | 22700 | -56.21 |
| 012860 | 모베이스전자 | Stage2-Actionable | 2023-05-09 | 3200 | 5.0 | 5.0 | 5.0 | -26.25 | -33.13 | -43.06 | 2023-05-09 | 3360 | -45.77 |

## 9. Case-by-Case Notes

### 9.1 005850 / 에스엘 — lighting/OEM volume-mix bridge

The entry row is 2023-03-23 at 26,100. The 30D path reaches 34,050 and the wider path reaches 42,400. This is a clean C29 auto-parts positive: global OEM volume recovery, lighting/EV mix, and margin/operating leverage are the bridge. The correct output is Yellow plus 4B watch, not Green loosening.

### 9.2 010690 / 화신 — chassis/OEM margin bridge with high-MAE watch

The entry row is 2023-03-23 at 11,400. The 90D path reaches 22,700, but the post-peak drawdown is deep. This validates the customer-volume and margin bridge, while also showing that auto-parts reratings can become crowded and need high-MAE guard after a fast peak.

### 9.3 012860 / 모베이스전자 — smartcar/auto-electronics theme false positive

The entry row is 2023-05-09 at 3,200. The upside only extends to 3,360, while the broader low falls to 1,822. This is the C29 false-positive shape: smartcar or auto-electronics words can make a spark, but without customer volume, margin, and operating leverage, the spark has no fuel line.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C29 treats smartcar/auto-electronics price strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C29 needs customer-volume, mix/margin, or operating-leverage bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 012860 and after 010690's peak. |
| Full 4B non-price requirement appropriate? | Yes. 005850/010690 have bridge evidence; 012860 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
005850:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after OEM volume / mix-margin bridge
  Stage3-Green = wait for stronger margin durability and post-MFE 4B review

010690:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed with active 4B/high-MAE watch
  Stage3-Green = reject unless post-peak drawdown and margin-cycle risk clear

012860:
  Stage2-Actionable = too generous if based only on smartcar/auto-electronics theme
  Stage3-Yellow = reject without customer-volume or margin bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 005850 | 0.90 | 1.00 | good full-window 4B watch after volume/mix margin bridge |
| 010690 | 0.94 | 1.00 | good 4B watch but requires margin-cycle drawdown guard |
| 012860 | 1.00 | 1.00 | auto-electronics theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c29_auto_parts_requires_customer_volume_mix_margin_bridge

rule:
  For C29 auto-parts/mobility rows, do not promote auto-electronics, smartcar,
  EV component, auto-parts theme, or mobility price strength into Stage3-Yellow/Green unless
  at least one non-price bridge is visible:
  OEM/customer volume, product mix improvement, margin conversion, operating leverage,
  order/backlog pull-through, customer-quality evidence, or FCF/cash conversion.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 55.52 | -13.59 | 33.3% | useful but can over-credit auto-electronics theme |
| P0b e2r_2_0_baseline_reference | 3 | 55.52 | -13.59 | 0% | safer but may miss 005850/010690 |
| P1 sector_specific_candidate_profile | 3 | 55.52 | -13.59 | 33.3% | no broad L3 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 80.78 | -3.82 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 5.0 | -33.13 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 005850 | current_profile_correct | OEM volume/mix margin bridge aligned with strong MFE |
| 010690 | current_profile_partially_correct | bridge worked, but drawdown requires 4B/high-MAE watch |
| 012860 | current_profile_false_positive | smartcar theme produced low MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29_AUTO_PARTS_CUSTOMER_VOLUME_MIX_MARGIN_BRIDGE_GUARD | 2 | 1 | 3 | 2 | 3 | 0 | 3 | 3 | 1 | false | true | C29 non-top-covered auto-parts volume/mix margin residual reduced |

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
- auto electronics theme without customer-volume/margin bridge
- auto-parts winner needs 4B watch
- chassis volume/margin high-MAE after peak
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
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
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_auto_parts_requires_customer_volume_mix_margin_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"C29 auto-parts rows should not promote toward Stage3-Yellow/Green unless mobility/auto signal converts into OEM/customer volume, mix-margin, operating leverage, or customer-quality bridge","005850 and 010690 survive with strong MFE after customer/mix/margin bridge; 012860 fails when smartcar/auto-electronics theme lacks customer-volume and margin bridge","TRG_R9L73_C29_005850_20230323_AUTO_LIGHTING_VOLUME_MIX_MARGIN_BRIDGE|TRG_R9L73_C29_010690_20230323_CHASSIS_VOLUME_MARGIN_BRIDGE_WITH_HIGH_MAE_WATCH|TRG_R9L73_C29_012860_20230509_AUTO_ELECTRONICS_SMARTCAR_THEME_NO_MARGIN_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_auto_parts_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,1,1,0,"Auto-parts winners and smartcar-theme failures can peak before margin durability is confirmed; local 4B/high-MAE watch should remain active after MFE","preserves 005850/010690 positives while preventing 012860 smartcar-theme false positive","TRG_R9L73_C29_005850_20230323_AUTO_LIGHTING_VOLUME_MIX_MARGIN_BRIDGE|TRG_R9L73_C29_010690_20230323_CHASSIS_VOLUME_MARGIN_BRIDGE_WITH_HIGH_MAE_WATCH|TRG_R9L73_C29_012860_20230509_AUTO_ELECTRONICS_SMARTCAR_THEME_NO_MARGIN_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R9L73_C29_005850_20230323_AUTO_LIGHTING_VOLUME_MIX_MARGIN_BRIDGE","symbol":"005850","company_name":"에스엘","round":"R9","loop":"73","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_AUTO_LIGHTING_VOLUME_MIX_MARGIN_BRIDGE","deep_sub_archetype_id":"GLOBAL_OEM_LIGHTING_EV_MIX_TO_MARGIN_OPERATING_LEVERAGE","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C29 auto-parts rows require customer/OEM volume, mix, margin, or operating-leverage bridge; smartcar/EV/auto-electronics theme alone is insufficient."}
{"row_type":"case","case_id":"R9L73_C29_010690_20230323_CHASSIS_VOLUME_MARGIN_BRIDGE_WITH_HIGH_MAE_WATCH","symbol":"010690","company_name":"화신","round":"R9","loop":"73","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_AUTO_CHASSIS_VOLUME_MARGIN_BRIDGE_WITH_4B_GUARD","deep_sub_archetype_id":"GLOBAL_AUTO_CHASSIS_VOLUME_OPERATING_LEVERAGE_TO_PEAK_REVERSAL","case_type":"structural_success_with_high_MAE_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct","price_source":"Songdaiki/stock-web","notes":"C29 auto-parts rows require customer/OEM volume, mix, margin, or operating-leverage bridge; smartcar/EV/auto-electronics theme alone is insufficient."}
{"row_type":"case","case_id":"R9L73_C29_012860_20230509_AUTO_ELECTRONICS_SMARTCAR_THEME_NO_MARGIN_BRIDGE","symbol":"012860","company_name":"모베이스전자","round":"R9","loop":"73","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_AUTO_ELECTRONICS_SMARTCAR_THEME_WITHOUT_VOLUME_MARGIN_BRIDGE","deep_sub_archetype_id":"SMARTCAR_ELECTRONICS_THEME_PRICE_SPIKE_WITHOUT_CUSTOMER_VOLUME_MARGIN_CONVERSION","case_type":"failed_rerating_low_MFE_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C29 auto-parts rows require customer/OEM volume, mix, margin, or operating-leverage bridge; smartcar/EV/auto-electronics theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R9L73_C29_005850_20230323_AUTO_LIGHTING_VOLUME_MIX_MARGIN_BRIDGE","case_id":"R9L73_C29_005850_20230323_AUTO_LIGHTING_VOLUME_MIX_MARGIN_BRIDGE","symbol":"005850","company_name":"에스엘","round":"R9","loop":"73","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_AUTO_LIGHTING_VOLUME_MIX_MARGIN_BRIDGE","deep_sub_archetype_id":"GLOBAL_OEM_LIGHTING_EV_MIX_TO_MARGIN_OPERATING_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-23","entry_date":"2023-03-23","entry_price":26100,"evidence_available_at_that_date":"source_proxy_auto_lighting_global_OEM_volume_mix_margin_operating_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_auto_lighting_global_OEM_volume_mix_margin_operating_leverage_bridge; evidence_url_pending","bridge_summary":"global OEM lighting/EV mix and volume recovery converted into margin and operating-leverage visibility rather than simple auto-parts theme","stage2_evidence_fields":["auto_parts_volume_recovery","global_OEM_customer_mix","EV_lighting_mix_proxy","relative_strength"],"stage3_evidence_fields":["volume_to_margin_visibility","customer_mix_operating_leverage","earnings_revision_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","auto_parts_margin_cycle_repricing"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005850/2023.csv","profile_path":"atlas/symbol_profiles/005/005850.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":30.46,"MFE_90D_pct":62.45,"MFE_180D_pct":62.45,"MFE_1Y_pct":62.45,"MFE_2Y_pct":62.45,"MAE_30D_pct":-2.3,"MAE_90D_pct":-2.3,"MAE_180D_pct":-2.3,"MAE_1Y_pct":-2.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-17","peak_price":42400,"drawdown_after_peak_pct":-32.78,"green_lateness_ratio":"0.38","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_volume_mix_margin_bridge","four_b_evidence_type":"non_price_customer_volume_mix_margin_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L73_C29_005850_20230323_AUTO_LIGHTING_VOLUME_MIX_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R9L73_C29_010690_20230323_CHASSIS_VOLUME_MARGIN_BRIDGE_WITH_HIGH_MAE_WATCH","case_id":"R9L73_C29_010690_20230323_CHASSIS_VOLUME_MARGIN_BRIDGE_WITH_HIGH_MAE_WATCH","symbol":"010690","company_name":"화신","round":"R9","loop":"73","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_AUTO_CHASSIS_VOLUME_MARGIN_BRIDGE_WITH_4B_GUARD","deep_sub_archetype_id":"GLOBAL_AUTO_CHASSIS_VOLUME_OPERATING_LEVERAGE_TO_PEAK_REVERSAL","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-23","entry_date":"2023-03-23","entry_price":11400,"evidence_available_at_that_date":"source_proxy_auto_chassis_global_OEM_volume_margin_operating_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_auto_chassis_global_OEM_volume_margin_operating_leverage_bridge; evidence_url_pending","bridge_summary":"auto chassis/OEM volume and margin leverage created strong MFE, but post-peak reversal requires 4B/high-MAE overlay","stage2_evidence_fields":["auto_chassis_volume_recovery","global_OEM_pullthrough","relative_strength","margin_leverage_proxy"],"stage3_evidence_fields":["volume_to_margin_visibility","operating_leverage_proxy","customer_volume_bridge"],"stage4b_evidence_fields":["post_MFE_peak_watch","auto_parts_crowding_after_margin_rerating"],"stage4c_evidence_fields":["high_MAE_after_peak_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010690/2023.csv","profile_path":"atlas/symbol_profiles/010/010690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":42.46,"MFE_90D_pct":99.12,"MFE_180D_pct":99.12,"MFE_1Y_pct":99.12,"MFE_2Y_pct":99.12,"MAE_30D_pct":-5.35,"MAE_90D_pct":-5.35,"MAE_180D_pct":-12.81,"MAE_1Y_pct":-12.81,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-06","peak_price":22700,"drawdown_after_peak_pct":-56.21,"green_lateness_ratio":"0.35","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_4B_watch_but_requires_margin_cycle_drawdown_guard","four_b_evidence_type":"non_price_customer_volume_mix_margin_bridge","four_c_protection_label":"high_MAE_watch_after_peak","trigger_outcome_label":"structural_success_but_needs_4B_high_MAE_guard","current_profile_verdict":"current_profile_partially_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L73_C29_010690_20230323_CHASSIS_VOLUME_MARGIN_BRIDGE_WITH_HIGH_MAE_WATCH_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R9L73_C29_012860_20230509_AUTO_ELECTRONICS_SMARTCAR_THEME_NO_MARGIN_BRIDGE","case_id":"R9L73_C29_012860_20230509_AUTO_ELECTRONICS_SMARTCAR_THEME_NO_MARGIN_BRIDGE","symbol":"012860","company_name":"모베이스전자","round":"R9","loop":"73","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_AUTO_ELECTRONICS_SMARTCAR_THEME_WITHOUT_VOLUME_MARGIN_BRIDGE","deep_sub_archetype_id":"SMARTCAR_ELECTRONICS_THEME_PRICE_SPIKE_WITHOUT_CUSTOMER_VOLUME_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-09","entry_date":"2023-05-09","entry_price":3200,"evidence_available_at_that_date":"source_proxy_auto_electronics_smartcar_theme_without_customer_volume_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_auto_electronics_smartcar_theme_without_customer_volume_margin_bridge; evidence_url_pending","bridge_summary":"smartcar/auto electronics theme price spike lacked customer-volume, margin, and operating-leverage bridge and later collapsed into high MAE","stage2_evidence_fields":["auto_electronics_theme","smartcar_or_EV_optionality","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_theme_local_peak","customer_volume_bridge_absent","margin_conversion_absent"],"stage4c_evidence_fields":["high_MAE_without_volume_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012860/2023.csv","profile_path":"atlas/symbol_profiles/012/012860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.0,"MFE_90D_pct":5.0,"MFE_180D_pct":5.0,"MFE_1Y_pct":5.0,"MFE_2Y_pct":5.0,"MAE_30D_pct":-26.25,"MAE_90D_pct":-33.13,"MAE_180D_pct":-43.06,"MAE_1Y_pct":-43.06,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-09","peak_price":3360,"drawdown_after_peak_pct":-45.77,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"auto_electronics_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"price_theme_without_customer_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L73_C29_012860_20230509_AUTO_ELECTRONICS_SMARTCAR_THEME_NO_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L73_C29_005850_20230323_AUTO_LIGHTING_VOLUME_MIX_MARGIN_BRIDGE","trigger_id":"TRG_R9L73_C29_005850_20230323_AUTO_LIGHTING_VOLUME_MIX_MARGIN_BRIDGE","symbol":"005850","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"customer_volume_score":12,"mix_margin_score":12,"operating_leverage_score":10,"OEM_customer_quality_score":10,"relative_strength_score":10,"theme_risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"customer_volume_score":15,"mix_margin_score":15,"operating_leverage_score":13,"OEM_customer_quality_score":12,"relative_strength_score":8,"theme_risk_penalty":5},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["customer_volume_score","mix_margin_score","operating_leverage_score","OEM_customer_quality_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C29 row is promoted only because auto-parts signal converts into OEM/customer volume, mix-margin and operating-leverage bridge.","MFE_90D_pct":62.45,"MAE_90D_pct":-2.3,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L73_C29_010690_20230323_CHASSIS_VOLUME_MARGIN_BRIDGE_WITH_HIGH_MAE_WATCH","trigger_id":"TRG_R9L73_C29_010690_20230323_CHASSIS_VOLUME_MARGIN_BRIDGE_WITH_HIGH_MAE_WATCH","symbol":"010690","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"customer_volume_score":11,"mix_margin_score":10,"operating_leverage_score":9,"OEM_customer_quality_score":9,"relative_strength_score":11,"theme_risk_penalty":6},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"customer_volume_score":14,"mix_margin_score":13,"operating_leverage_score":11,"OEM_customer_quality_score":11,"relative_strength_score":8,"theme_risk_penalty":10},"weighted_score_after":77,"stage_label_after":"Stage3-Yellow","changed_components":["customer_volume_score","mix_margin_score","operating_leverage_score","OEM_customer_quality_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C29 auto-parts bridge works, but high post-peak drawdown requires 4B/high-MAE guard and prevents Green loosening.","MFE_90D_pct":99.12,"MAE_90D_pct":-5.35,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L73_C29_012860_20230509_AUTO_ELECTRONICS_SMARTCAR_THEME_NO_MARGIN_BRIDGE","trigger_id":"TRG_R9L73_C29_012860_20230509_AUTO_ELECTRONICS_SMARTCAR_THEME_NO_MARGIN_BRIDGE","symbol":"012860","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"customer_volume_score":3,"mix_margin_score":1,"operating_leverage_score":1,"OEM_customer_quality_score":2,"relative_strength_score":12,"theme_risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"customer_volume_score":0,"mix_margin_score":0,"operating_leverage_score":0,"OEM_customer_quality_score":0,"relative_strength_score":5,"theme_risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["customer_volume_score","mix_margin_score","operating_leverage_score","OEM_customer_quality_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C29 guard demotes smartcar/auto-electronics theme rows when customer volume, margin and operating-leverage bridge is absent.","MFE_90D_pct":5.0,"MAE_90D_pct":-33.13,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_auto_parts_requires_customer_volume_mix_margin_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"C29 auto-parts rows should not promote toward Stage3-Yellow/Green unless mobility/auto signal converts into OEM/customer volume, mix-margin, operating leverage, or customer-quality bridge","005850 and 010690 survive with strong MFE after customer/mix/margin bridge; 012860 fails when smartcar/auto-electronics theme lacks customer-volume and margin bridge","TRG_R9L73_C29_005850_20230323_AUTO_LIGHTING_VOLUME_MIX_MARGIN_BRIDGE|TRG_R9L73_C29_010690_20230323_CHASSIS_VOLUME_MARGIN_BRIDGE_WITH_HIGH_MAE_WATCH|TRG_R9L73_C29_012860_20230509_AUTO_ELECTRONICS_SMARTCAR_THEME_NO_MARGIN_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_auto_parts_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,1,1,0,"Auto-parts winners and smartcar-theme failures can peak before margin durability is confirmed; local 4B/high-MAE watch should remain active after MFE","preserves 005850/010690 positives while preventing 012860 smartcar-theme false positive","TRG_R9L73_C29_005850_20230323_AUTO_LIGHTING_VOLUME_MIX_MARGIN_BRIDGE|TRG_R9L73_C29_010690_20230323_CHASSIS_VOLUME_MARGIN_BRIDGE_WITH_HIGH_MAE_WATCH|TRG_R9L73_C29_012860_20230509_AUTO_ELECTRONICS_SMARTCAR_THEME_NO_MARGIN_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"73","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["auto_electronics_theme_without_customer_volume_margin_bridge","auto_parts_winner_needs_4B_watch","chassis_volume_margin_high_MAE_after_peak"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- price-only/auto-theme-only rows cannot promote Stage2/Stage3.
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
11. Add validation that C29 auto-parts/mobility rows cannot promote without customer-volume, product-mix, margin, operating-leverage, order/backlog pull-through, or FCF bridge.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R9
completed_loop = 73
next_round = R10
next_loop = 73
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
atlas/symbol_profiles/010/010690.json
atlas/symbol_profiles/012/012860.json
atlas/ohlcv_tradable_by_symbol_year/005/005850/2023.csv
atlas/ohlcv_tradable_by_symbol_year/010/010690/2023.csv
atlas/ohlcv_tradable_by_symbol_year/012/012860/2023.csv
```

This loop continues loop 73 with R9 and adds 3 new independent C29 representative cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R9/L3.
