# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R5
scheduled_loop: 75
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R6
computed_next_loop: 75
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: C18_EXPORT_REORDER_SELLTHROUGH_MARGIN_CASHFLOW_BRIDGE_GUARD
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

R5 maps directly to `L5_CONSUMER_BRAND_DISTRIBUTION`. The previous R5 loop used C20 beauty/food/global distribution, and earlier R5 work already touched C19 retail/inventory margin. This run rotates to C18 consumer export/channel reorder, with a focus on K-food export/reorder winners versus legacy food-channel theme rows.

| layer | id | definition |
|---|---|---|
| round | R5 | consumer / brand / distribution |
| large_sector | L5_CONSUMER_BRAND_DISTRIBUTION | consumer, food, beauty, brand, distribution, global channel |
| canonical | C18_CONSUMER_EXPORT_CHANNEL_REORDER | consumer export channel, reorder, sell-through and margin bridge |
| fine | C18_EXPORT_REORDER_SELLTHROUGH_MARGIN_CASHFLOW_BRIDGE_GUARD | consumer signal must become export/reorder/margin evidence |
| deep | K_FOOD_SEAFOOD_PROCESSING_EXPORT_CHANNEL_REORDER_TO_MARGIN_OPERATING_LEVERAGE | K-food export positive |
| deep | HEALTH_FOOD_US_GLOBAL_CHANNEL_RECOVERY_TO_MARGIN_AND_OPERATING_LEVERAGE | global food channel positive |
| deep | LEGACY_PACKAGED_FOOD_CHANNEL_OPTIONALITY_WITHOUT_EXPORT_REORDER_SELLTHROUGH_MARGIN_CONVERSION | legacy channel false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C18 top-covered symbols are `003230`, `005180`, `004370`, `192820`, `097950`, and `271560`. This run avoids that cluster and also avoids the previous R5/C20 representative set.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C18 | 003960 | new independent | not top-covered C18 symbol; K-food/export reorder margin bridge |
| C18 | 017810 | new independent | not top-covered C18 symbol; health/global food channel margin bridge |
| C18 | 049770 | new independent | not top-covered C18 symbol; legacy packaged-food channel MFE without durable reorder/margin bridge |

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
003960 has only historical corporate-action/name-transition candidate periods before the selected 2024 window.
017810 has corporate-action candidates ending 2019-05-07, outside the selected 2024 representative window.
049770 has a 2023-04-19 corporate-action candidate, outside the selected 2024 representative window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 003960 | 사조대림 | Stage2-Actionable | 2024-02-01 | 37000 | K-food/export reorder margin bridge worked, but post-peak 4B required |
| global_food_channel_success_then_4B_watch | 017810 | 풀무원 | Stage2-Actionable | 2024-04-01 | 11100 | global/health food channel margin bridge worked, but high-MAE watch required |
| legacy_food_theme_MFE_then_high_MAE_counterexample | 049770 | 동원F&B | Stage2-Actionable | 2024-04-01 | 33850 | legacy packaged-food/channel MFE lacked durable reorder/margin bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 3
4C_or_high_MAE_watch_count: 3
calibration_usable_case_count: 3
current_profile_error_count: 1
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 003960 | 사조대림 | Stage2-Actionable | 2024-02-01 | 37000 | 10.27 | 116.22 | 197.03 | -5.14 | -10.27 | -10.27 | 2024-07-09 | 109900 | -57.6 |
| 017810 | 풀무원 | Stage2-Actionable | 2024-04-01 | 11100 | 9.82 | 55.41 | 55.41 | -6.76 | -9.82 | -9.82 | 2024-06-28 | 17250 | -41.97 |
| 049770 | 동원F&B | Stage2-Actionable | 2024-04-01 | 33850 | 8.12 | 36.04 | 36.04 | -9.31 | -9.31 | -8.57 | 2024-07-02 | 46050 | -32.79 |

## 9. Case-by-Case Notes

### 9.1 003960 / 사조대림 — K-food export reorder margin bridge

The entry row is 2024-02-01 at 37,000. The early path was modest, but the wider window reached 109,900. This is a valid C18 positive because the move is not just food-theme momentum. The bridge is export channel, reorder pull-through, processed-food mix, margin and operating leverage. The post-peak low still requires 4B/drawdown watch.

### 9.2 017810 / 풀무원 — global healthy-food channel bridge

The entry row is 2024-04-01 at 11,100. The path reached 17,250 by the wider window, then later fell back toward 10,010. This is another C18 positive, but not a Green-loosening case. It needs global channel recovery, reorder and margin bridge to survive, while high-MAE keeps 4B active.

### 9.3 049770 / 동원F&B — legacy food channel MFE without durable bridge

The entry row is 2024-04-01 at 33,850. The path reached 46,050, but later fell to 30,950. This is a useful counterexample: legacy packaged-food/channel optionality can produce MFE, but without durable export reorder, sell-through, channel mix, margin or cashflow bridge, it should remain 4B/high-MAE watch rather than Stage3-Green.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C18 treats consumer/food MFE as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C18 needs export/reorder/sell-through/margin bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially after 003960/017810 peaks. |
| Full 4B non-price requirement appropriate? | Yes. 003960/017810 have stronger non-price bridges; 049770 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
003960:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after export/reorder/margin bridge
  Stage3-Green = reject unless post-peak channel durability and drawdown risk clear

017810:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after global-channel / margin / operating-leverage bridge
  Stage3-Green = reject because high-MAE and channel crowding remain active

049770:
  Stage2-Actionable = acceptable only as legacy-channel watch
  Stage3-Yellow = reject without export reorder, sell-through, margin or cashflow bridge
  Stage3-Green = reject despite MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 003960 | 0.73 | 1.00 | K-food export bridge positive but full-window 4B/drawdown watch |
| 017810 | 0.85 | 1.00 | global food channel bridge positive but 4B/high-MAE watch |
| 049770 | 0.91 | 1.00 | legacy food MFE but no reorder-margin bridge; keep 4B/high-MAE watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c18_requires_export_reorder_sellthrough_margin_cashflow_bridge

rule:
  For C18 consumer export/channel reorder rows, do not promote food,
  packaged food, K-food, health food, global channel, or consumer export Stage2
  signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  export-channel expansion, reorder, sell-through, channel mix, inventory normalization,
  margin conversion, operating leverage, FCF/cash conversion, or earnings revision.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 69.22 | -9.8 | 33.3% | useful but can over-credit legacy food/channel MFE |
| P0b e2r_2_0_baseline_reference | 3 | 69.22 | -9.8 | 0% | safer but may miss 003960/017810 |
| P1 sector_specific_candidate_profile | 3 | 69.22 | -9.8 | 33.3% | no broad L5 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 85.81 | -10.04 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected/watch | 36.04 | -9.31 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 003960 | current_profile_correct_but_no_green | export/reorder bridge aligned with large MFE, but post-peak drawdown blocks Green |
| 017810 | current_profile_correct_with_drawdown_guard | global-channel margin bridge aligned with MFE, but high-MAE requires 4B |
| 049770 | current_profile_false_positive_if_green | MFE existed but durable reorder/margin bridge was weak |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18_EXPORT_REORDER_SELLTHROUGH_MARGIN_CASHFLOW_BRIDGE_GUARD | 2 | 1 | 3 | 3 | 3 | 0 | 3 | 3 | 1 | false | true | R5/C18 non-top-covered consumer export/reorder residual reduced |

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
- legacy food channel theme without reorder/margin bridge
- K-food export winner needs 4B watch
- global food channel winner needs drawdown guard
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
- R5 direct L5 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/report URLs
- exact export/reorder announcement URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c18_requires_export_reorder_sellthrough_margin_cashflow_bridge,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"C18 consumer export/channel reorder rows should not promote toward Stage3-Yellow/Green unless consumer/food signal converts into export channel, reorder, sell-through, channel mix, margin, operating leverage, or cashflow bridge","003960 and 017810 survive after export/global-channel reorder-margin bridge; 049770 is demoted because legacy food-channel MFE lacked durable reorder and margin bridge","TRG_R5L75_C18_003960_20240201_KFOOD_EXPORT_REORDER_MARGIN_BRIDGE|TRG_R5L75_C18_017810_20240401_HEALTH_FOOD_GLOBAL_CHANNEL_MARGIN_BRIDGE|TRG_R5L75_C18_049770_20240401_LEGACY_FOOD_CHANNEL_THEME_NO_REORDER_MARGIN_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c18_consumer_export_4b_high_mae_watch_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,1,1,0,"Consumer export winners and legacy food-channel theme false starts can peak before reorder and margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 003960/017810 positives while preventing 049770 consumer-channel theme false positive","TRG_R5L75_C18_003960_20240201_KFOOD_EXPORT_REORDER_MARGIN_BRIDGE|TRG_R5L75_C18_017810_20240401_HEALTH_FOOD_GLOBAL_CHANNEL_MARGIN_BRIDGE|TRG_R5L75_C18_049770_20240401_LEGACY_FOOD_CHANNEL_THEME_NO_REORDER_MARGIN_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R5L75_C18_003960_20240201_KFOOD_EXPORT_REORDER_MARGIN_BRIDGE","symbol":"003960","company_name":"사조대림","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"C18_KFOOD_EXPORT_REORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"K_FOOD_SEAFOOD_PROCESSING_EXPORT_CHANNEL_REORDER_TO_MARGIN_OPERATING_LEVERAGE","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C18 consumer export/channel reorder rows require export channel, reorder, sell-through, channel mix, margin, operating leverage, or cashflow bridge; consumer/food theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R5L75_C18_017810_20240401_HEALTH_FOOD_GLOBAL_CHANNEL_MARGIN_BRIDGE","symbol":"017810","company_name":"풀무원","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"C18_HEALTH_FOOD_GLOBAL_CHANNEL_MARGIN_BRIDGE","deep_sub_archetype_id":"HEALTH_FOOD_US_GLOBAL_CHANNEL_RECOVERY_TO_MARGIN_AND_OPERATING_LEVERAGE","case_type":"global_food_channel_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard","price_source":"Songdaiki/stock-web","notes":"C18 consumer export/channel reorder rows require export channel, reorder, sell-through, channel mix, margin, operating leverage, or cashflow bridge; consumer/food theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R5L75_C18_049770_20240401_LEGACY_FOOD_CHANNEL_THEME_NO_REORDER_MARGIN_BRIDGE","symbol":"049770","company_name":"동원F&B","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"C18_LEGACY_FOOD_CHANNEL_THEME_WITHOUT_REORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"LEGACY_PACKAGED_FOOD_CHANNEL_OPTIONALITY_WITHOUT_EXPORT_REORDER_SELLTHROUGH_MARGIN_CONVERSION","case_type":"legacy_food_theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C18 consumer export/channel reorder rows require export channel, reorder, sell-through, channel mix, margin, operating leverage, or cashflow bridge; consumer/food theme MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R5L75_C18_003960_20240201_KFOOD_EXPORT_REORDER_MARGIN_BRIDGE","case_id":"R5L75_C18_003960_20240201_KFOOD_EXPORT_REORDER_MARGIN_BRIDGE","symbol":"003960","company_name":"사조대림","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"C18_KFOOD_EXPORT_REORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"K_FOOD_SEAFOOD_PROCESSING_EXPORT_CHANNEL_REORDER_TO_MARGIN_OPERATING_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":37000,"evidence_available_at_that_date":"source_proxy_K_food_export_reorder_channel_margin_operating_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_K_food_export_reorder_channel_margin_operating_leverage_bridge; evidence_url_pending","bridge_summary":"K-food export/reorder and processed-food channel pull-through converted into revenue, margin and operating-leverage visibility rather than food-theme price heat","stage2_evidence_fields":["K_food_export_channel","reorder_pullthrough","relative_strength","margin_leverage_proxy"],"stage3_evidence_fields":["export_channel_to_revenue_visibility","reorder_margin_bridge","operating_leverage_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","K_food_export_crowding_after_rerating"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003960/2024.csv","profile_path":"atlas/symbol_profiles/003/003960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.27,"MFE_90D_pct":116.22,"MFE_180D_pct":197.03,"MFE_1Y_pct":197.03,"MFE_2Y_pct":197.03,"MAE_30D_pct":-5.14,"MAE_90D_pct":-10.27,"MAE_180D_pct":-10.27,"MAE_1Y_pct":-10.27,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-09","peak_price":109900,"drawdown_after_peak_pct":-57.6,"green_lateness_ratio":"0.36","four_b_local_peak_proximity":0.73,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"K_food_export_bridge_positive_but_full_window_4B_drawdown_watch","four_b_evidence_type":"non_price_export_reorder_margin_bridge","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L75_C18_003960_20240201_KFOOD_EXPORT_REORDER_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R5L75_C18_017810_20240401_HEALTH_FOOD_GLOBAL_CHANNEL_MARGIN_BRIDGE","case_id":"R5L75_C18_017810_20240401_HEALTH_FOOD_GLOBAL_CHANNEL_MARGIN_BRIDGE","symbol":"017810","company_name":"풀무원","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"C18_HEALTH_FOOD_GLOBAL_CHANNEL_MARGIN_BRIDGE","deep_sub_archetype_id":"HEALTH_FOOD_US_GLOBAL_CHANNEL_RECOVERY_TO_MARGIN_AND_OPERATING_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":11100,"evidence_available_at_that_date":"source_proxy_health_food_US_global_channel_margin_operating_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_health_food_US_global_channel_margin_operating_leverage_bridge; evidence_url_pending","bridge_summary":"healthy-food/global channel recovery converted into margin and operating-leverage visibility, but post-peak drawdown required 4B watch","stage2_evidence_fields":["health_food_global_channel","US_channel_recovery_proxy","relative_strength","margin_leverage_proxy"],"stage3_evidence_fields":["channel_revenue_visibility","margin_operating_leverage","global_food_reorder_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","global_food_channel_crowding_after_rerating"],"stage4c_evidence_fields":["post_peak_high_MAE_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/017/017810/2024.csv","profile_path":"atlas/symbol_profiles/017/017810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.82,"MFE_90D_pct":55.41,"MFE_180D_pct":55.41,"MFE_1Y_pct":55.41,"MFE_2Y_pct":55.41,"MAE_30D_pct":-6.76,"MAE_90D_pct":-9.82,"MAE_180D_pct":-9.82,"MAE_1Y_pct":-9.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":17250,"drawdown_after_peak_pct":-41.97,"green_lateness_ratio":"0.46","four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"global_food_channel_bridge_positive_but_4B_high_MAE_watch","four_b_evidence_type":"non_price_export_reorder_margin_bridge","four_c_protection_label":"post_peak_high_MAE_watch","trigger_outcome_label":"global_food_channel_success_then_4B_watch","current_profile_verdict":"current_profile_correct_with_drawdown_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L75_C18_017810_20240401_HEALTH_FOOD_GLOBAL_CHANNEL_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R5L75_C18_049770_20240401_LEGACY_FOOD_CHANNEL_THEME_NO_REORDER_MARGIN_BRIDGE","case_id":"R5L75_C18_049770_20240401_LEGACY_FOOD_CHANNEL_THEME_NO_REORDER_MARGIN_BRIDGE","symbol":"049770","company_name":"동원F&B","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"C18_LEGACY_FOOD_CHANNEL_THEME_WITHOUT_REORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"LEGACY_PACKAGED_FOOD_CHANNEL_OPTIONALITY_WITHOUT_EXPORT_REORDER_SELLTHROUGH_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":33850,"evidence_available_at_that_date":"source_proxy_legacy_packaged_food_channel_theme_without_export_reorder_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_legacy_packaged_food_channel_theme_without_export_reorder_margin_bridge; evidence_url_pending","bridge_summary":"legacy packaged-food/channel theme produced MFE, but durable export reorder, sell-through, channel mix, margin or cashflow bridge was not strong enough","stage2_evidence_fields":["legacy_food_channel_theme","packaged_food_repricing_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["theme_MFE_peak","reorder_sellthrough_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_reorder_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/049/049770/2024.csv","profile_path":"atlas/symbol_profiles/049/049770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.12,"MFE_90D_pct":36.04,"MFE_180D_pct":36.04,"MFE_1Y_pct":36.04,"MFE_2Y_pct":36.04,"MAE_30D_pct":-9.31,"MAE_90D_pct":-9.31,"MAE_180D_pct":-8.57,"MAE_1Y_pct":-8.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-02","peak_price":46050,"drawdown_after_peak_pct":-32.79,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"legacy_food_MFE_but_no_reorder_margin_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"consumer_food_theme_without_reorder_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"legacy_food_theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L75_C18_049770_20240401_LEGACY_FOOD_CHANNEL_THEME_NO_REORDER_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L75_C18_003960_20240201_KFOOD_EXPORT_REORDER_MARGIN_BRIDGE","trigger_id":"TRG_R5L75_C18_003960_20240201_KFOOD_EXPORT_REORDER_MARGIN_BRIDGE","symbol":"003960","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"export_channel_score":12,"reorder_sellthrough_score":12,"margin_operating_leverage_score":11,"cashflow_bridge_score":9,"relative_strength_score":11,"theme_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"export_channel_score":15,"reorder_sellthrough_score":15,"margin_operating_leverage_score":14,"cashflow_bridge_score":11,"relative_strength_score":8,"theme_risk_penalty":8},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["export_channel_score","reorder_sellthrough_score","margin_operating_leverage_score","cashflow_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C18 row is promoted only because consumer/food signal converts into export channel, reorder, margin and operating-leverage bridge; 4B drawdown watch blocks Green.","MFE_90D_pct":116.22,"MAE_90D_pct":-10.27,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L75_C18_017810_20240401_HEALTH_FOOD_GLOBAL_CHANNEL_MARGIN_BRIDGE","trigger_id":"TRG_R5L75_C18_017810_20240401_HEALTH_FOOD_GLOBAL_CHANNEL_MARGIN_BRIDGE","symbol":"017810","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"export_channel_score":12,"reorder_sellthrough_score":12,"margin_operating_leverage_score":11,"cashflow_bridge_score":9,"relative_strength_score":11,"theme_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"export_channel_score":15,"reorder_sellthrough_score":15,"margin_operating_leverage_score":14,"cashflow_bridge_score":11,"relative_strength_score":8,"theme_risk_penalty":8},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["export_channel_score","reorder_sellthrough_score","margin_operating_leverage_score","cashflow_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C18 row is promoted only because consumer/food signal converts into export channel, reorder, margin and operating-leverage bridge; 4B drawdown watch blocks Green.","MFE_90D_pct":55.41,"MAE_90D_pct":-9.82,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L75_C18_049770_20240401_LEGACY_FOOD_CHANNEL_THEME_NO_REORDER_MARGIN_BRIDGE","trigger_id":"TRG_R5L75_C18_049770_20240401_LEGACY_FOOD_CHANNEL_THEME_NO_REORDER_MARGIN_BRIDGE","symbol":"049770","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"export_channel_score":7,"reorder_sellthrough_score":2,"margin_operating_leverage_score":2,"cashflow_bridge_score":1,"relative_strength_score":9,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"export_channel_score":3,"reorder_sellthrough_score":0,"margin_operating_leverage_score":0,"cashflow_bridge_score":0,"relative_strength_score":4,"theme_risk_penalty":15},"weighted_score_after":40,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["export_channel_score","reorder_sellthrough_score","margin_operating_leverage_score","cashflow_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C18 guard demotes consumer/food channel theme rows when export reorder, sell-through, margin and cashflow bridge are absent.","MFE_90D_pct":36.04,"MAE_90D_pct":-9.31,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c18_requires_export_reorder_sellthrough_margin_cashflow_bridge,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"C18 consumer export/channel reorder rows should not promote toward Stage3-Yellow/Green unless consumer/food signal converts into export channel, reorder, sell-through, channel mix, margin, operating leverage, or cashflow bridge","003960 and 017810 survive after export/global-channel reorder-margin bridge; 049770 is demoted because legacy food-channel MFE lacked durable reorder and margin bridge","TRG_R5L75_C18_003960_20240201_KFOOD_EXPORT_REORDER_MARGIN_BRIDGE|TRG_R5L75_C18_017810_20240401_HEALTH_FOOD_GLOBAL_CHANNEL_MARGIN_BRIDGE|TRG_R5L75_C18_049770_20240401_LEGACY_FOOD_CHANNEL_THEME_NO_REORDER_MARGIN_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c18_consumer_export_4b_high_mae_watch_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,1,1,0,"Consumer export winners and legacy food-channel theme false starts can peak before reorder and margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 003960/017810 positives while preventing 049770 consumer-channel theme false positive","TRG_R5L75_C18_003960_20240201_KFOOD_EXPORT_REORDER_MARGIN_BRIDGE|TRG_R5L75_C18_017810_20240401_HEALTH_FOOD_GLOBAL_CHANNEL_MARGIN_BRIDGE|TRG_R5L75_C18_049770_20240401_LEGACY_FOOD_CHANNEL_THEME_NO_REORDER_MARGIN_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"75","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["legacy_food_channel_theme_without_reorder_margin_bridge","K_food_export_winner_needs_4B_watch","global_food_channel_winner_needs_drawdown_guard"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R5-specific handling

- R5 maps to `L5_CONSUMER_BRAND_DISTRIBUTION`.
- This MD uses `C18_CONSUMER_EXPORT_CHANNEL_REORDER`.
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
- price-only/consumer-food-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R5 direct L5 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C18 consumer export/channel reorder rows cannot promote without export-channel expansion, reorder, sell-through, channel mix, inventory normalization, margin conversion, operating leverage, FCF/cash conversion, or earnings revision.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R5
completed_loop = 75
next_round = R6
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
atlas/symbol_profiles/003/003960.json
atlas/symbol_profiles/017/017810.json
atlas/symbol_profiles/049/049770.json
atlas/ohlcv_tradable_by_symbol_year/003/003960/2024.csv
atlas/ohlcv_tradable_by_symbol_year/017/017810/2024.csv
atlas/ohlcv_tradable_by_symbol_year/049/049770/2024.csv
```

This loop continues loop 75 with R5 and adds 3 new independent C18 representative cases, 2 positives, 1 counterexample/watch case, and 1 canonical-archetype residual guard candidate for R5/L5.
