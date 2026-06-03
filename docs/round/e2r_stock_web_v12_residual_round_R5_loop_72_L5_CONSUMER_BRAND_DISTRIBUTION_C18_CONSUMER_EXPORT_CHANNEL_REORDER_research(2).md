# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R5
scheduled_loop: 72
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R6
computed_next_loop: 72
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: C18_K_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE_GUARD
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

R5 maps to `L5_CONSUMER_BRAND_DISTRIBUTION`. This run uses C18 rather than repeating C19 from the prior R5 loop. The residual target is the gap between real export-channel reorder and simple K-food price heat.

| layer | id | definition |
|---|---|---|
| round | R5 | consumer / brand / distribution |
| large_sector | L5_CONSUMER_BRAND_DISTRIBUTION | consumer brand, export channel, retail/distribution |
| canonical | C18_CONSUMER_EXPORT_CHANNEL_REORDER | export channel expansion, sell-through, reorder and margin bridge |
| fine | C18_K_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE_GUARD | K-food/export channel must become sell-through/reorder/margin |
| deep | GLOBAL_SNACK_ICECREAM_CHANNEL_SELLTHROUGH_TO_REORDER | global snack/ice-cream channel success |
| deep | SAUCE_FOOD_EXPORT_SELLTHROUGH_TO_MARGIN_LEVERAGE | sauce/food export success with drawdown watch |
| deep | K_FOOD_THEME_WITHOUT_CHANNEL_SELLTHROUGH_OR_MARGIN_CONVERSION | food theme false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C18 top-covered symbols are `003230`, `005180`, `004370`, `192820`, `097950`, and `271560`. This run avoids that cluster and uses new-symbol C18 rows to stress the export-channel/reorder bridge.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C18 | 280360 | new independent | not top-covered C18 symbol; global food channel/reorder positive |
| C18 | 001680 | new independent | not top-covered C18 symbol; food export/margin bridge positive |
| C18 | 248170 | new independent | not top-covered C18 symbol; food theme without reorder bridge counterexample |

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

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 280360 | 롯데웰푸드 | Stage2-Actionable | 2024-04-22 | 132100 | global channel/reorder bridge worked |
| structural_success_with_drawdown_watch | 001680 | 대상 | Stage2-Actionable | 2024-04-22 | 21900 | food export/channel margin bridge worked, but 4B/high-MAE guard needed |
| failed_rerating_high_MAE | 248170 | 샘표식품 | Stage2-Actionable | 2024-06-18 | 40350 | K-food/food theme without reorder bridge failed |

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
| 280360 | 롯데웰푸드 | Stage2-Actionable | 2024-04-22 | 132100 | 22.86 | 57.83 | 57.83 | -4.16 | -4.16 | -11.36 | 2024-06-18 | 208500 | -43.84 |
| 001680 | 대상 | Stage2-Actionable | 2024-04-22 | 21900 | 12.79 | 41.1 | 41.1 | -3.88 | -5.48 | -10.55 | 2024-06-17 | 30900 | -36.6 |
| 248170 | 샘표식품 | Stage2-Actionable | 2024-06-18 | 40350 | 12.76 | 12.76 | 12.76 | -25.4 | -33.58 | -33.58 | 2024-06-20 | 45500 | -41.1 |

## 9. Case-by-Case Notes

### 9.1 280360 / 롯데웰푸드 — global channel/reorder bridge positive

The entry row is 2024-04-22 at 132,100. The 30D path reaches 162,300 and the later path reaches 208,500. This is the valid C18 pattern: export channel expansion becomes sell-through and reorder, then price can carry. The later drawdown still requires 4B/high-MAE watch rather than Green loosening.

### 9.2 001680 / 대상 — food export/channel margin bridge positive with drawdown watch

The entry row is 2024-04-22 at 21,900. The path reaches 30,900, then later gives back much of the move. This supports Stage2/Yellow when export channel and margin mix evidence exists, but it also argues that C18 winners are not exempt from peak and durability checks.

### 9.3 248170 / 샘표식품 — K-food theme without reorder bridge

The entry row is 2024-06-18 at 40,350. The 90D high is only 45,500 while the low falls to 26,800. This is the C18 trap: a food-theme flare can look like a channel story, but without sell-through/reorder/margin conversion, it is only a candle in the wind.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C18 treats K-food/food theme price strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C18 needs channel sell-through/reorder/margin bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 248170 near the local food-theme peak. |
| Full 4B non-price requirement appropriate? | Yes. 280360/001680 have non-price channel/reorder bridge; 248170 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
280360:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after export channel / reorder bridge
  Stage3-Green = wait for stronger margin/FCF durability and post-MFE 4B check

001680:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed with 4B/high-MAE watch active
  Stage3-Green = reject unless reorder durability clears drawdown risk

248170:
  Stage2-Actionable = too generous if based only on K-food/food theme price strength
  Stage3-Yellow = reject without channel sell-through or reorder bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 280360 | 0.89 | 1.00 | good full-window 4B watch after export channel/reorder bridge |
| 001680 | 0.93 | 1.00 | good 4B watch but requires reorder durability guard |
| 248170 | 1.00 | 1.00 | price/theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c18_requires_channel_sellthrough_reorder_margin_bridge

rule:
  For C18 consumer export/channel rows, do not promote food/brand/export theme Stage2 signals
  into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  channel sell-through, reorder confirmation, export channel expansion, margin mix improvement,
  inventory normalization, or earnings revision linked to channel conversion.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 37.23 | -14.41 | 33.3% | useful but can over-credit food theme |
| P0b e2r_2_0_baseline_reference | 3 | 37.23 | -14.41 | 0% | safer but may miss channel/reorder bridge winners |
| P1 sector_specific_candidate_profile | 3 | 37.23 | -14.41 | 33.3% | no broad L5 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 49.47 | -4.82 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 12.76 | -33.58 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 280360 | current_profile_correct | export channel/reorder bridge aligned with strong MFE |
| 001680 | current_profile_partially_correct | bridge worked, but drawdown requires 4B/high-MAE watch |
| 248170 | current_profile_false_positive | food theme produced shallow MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | C18_K_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE_GUARD | 2 | 1 | 3 | 3 | 3 | 0 | 3 | 3 | 1 | false | true | C18 non-top-covered channel/reorder residual reduced |

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
- K-food theme without channel/reorder bridge
- consumer export winner needs 4B watch
- post-MFE high-MAE after food theme price spike
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
shadow_weight,c18_requires_channel_sellthrough_reorder_margin_bridge,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"C18 consumer export/channel rows should not promote toward Stage3-Yellow/Green unless export channel expansion converts into sell-through, reorder, margin mix, or earnings visibility","280360 and 001680 survive with strong MFE after channel/reorder bridge; 248170 fails when K-food theme lacks channel sell-through/reorder bridge","TRG_R5L72_C18_280360_20240422_KFOOD_EXPORT_CHANNEL_REORDER_BRIDGE|TRG_R5L72_C18_001680_20240422_FOOD_EXPORT_CHANNEL_MARGIN_BRIDGE|TRG_R5L72_C18_248170_20240618_FOOD_THEME_WITHOUT_REORDER_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c18_consumer_export_4b_high_mae_watch_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,1,1,0,"Consumer export winners and food-theme failures can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 280360/001680 positives while preventing 248170 theme false positive","TRG_R5L72_C18_280360_20240422_KFOOD_EXPORT_CHANNEL_REORDER_BRIDGE|TRG_R5L72_C18_001680_20240422_FOOD_EXPORT_CHANNEL_MARGIN_BRIDGE|TRG_R5L72_C18_248170_20240618_FOOD_THEME_WITHOUT_REORDER_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R5L72_C18_280360_20240422_KFOOD_EXPORT_CHANNEL_REORDER_BRIDGE","symbol":"280360","company_name":"롯데웰푸드","round":"R5","loop":"72","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"C18_K_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE","deep_sub_archetype_id":"GLOBAL_SNACK_ICECREAM_CHANNEL_SELLTHROUGH_TO_REORDER","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C18 consumer export/channel rows require channel sell-through/reorder and margin conversion bridge; K-food theme or price spike alone is insufficient."}
{"row_type":"case","case_id":"R5L72_C18_001680_20240422_FOOD_EXPORT_CHANNEL_MARGIN_BRIDGE","symbol":"001680","company_name":"대상","round":"R5","loop":"72","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"C18_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"SAUCE_FOOD_EXPORT_SELLTHROUGH_TO_MARGIN_LEVERAGE","case_type":"structural_success_with_drawdown_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct","price_source":"Songdaiki/stock-web","notes":"C18 consumer export/channel rows require channel sell-through/reorder and margin conversion bridge; K-food theme or price spike alone is insufficient."}
{"row_type":"case","case_id":"R5L72_C18_248170_20240618_FOOD_THEME_WITHOUT_REORDER_BRIDGE","symbol":"248170","company_name":"샘표식품","round":"R5","loop":"72","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"C18_FOOD_THEME_PRICE_SPIKE_WITHOUT_REORDER_BRIDGE","deep_sub_archetype_id":"K_FOOD_THEME_WITHOUT_CHANNEL_SELLTHROUGH_OR_MARGIN_CONVERSION","case_type":"failed_rerating_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C18 consumer export/channel rows require channel sell-through/reorder and margin conversion bridge; K-food theme or price spike alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R5L72_C18_280360_20240422_KFOOD_EXPORT_CHANNEL_REORDER_BRIDGE","case_id":"R5L72_C18_280360_20240422_KFOOD_EXPORT_CHANNEL_REORDER_BRIDGE","symbol":"280360","company_name":"롯데웰푸드","round":"R5","loop":"72","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"C18_K_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE","deep_sub_archetype_id":"GLOBAL_SNACK_ICECREAM_CHANNEL_SELLTHROUGH_TO_REORDER","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-22","entry_date":"2024-04-22","entry_price":132100,"evidence_available_at_that_date":"source_proxy_K_food_global_channel_reorder_and_margin_mix_bridge; evidence_url_pending","evidence_source":"source_proxy_K_food_global_channel_reorder_and_margin_mix_bridge; evidence_url_pending","bridge_summary":"global snack/ice-cream channel sell-through and export reorder route converted into MFE, not just K-food theme price strength","stage2_evidence_fields":["export_channel_expansion","global_food_reorder_proxy","relative_strength","margin_mix_bridge"],"stage3_evidence_fields":["sellthrough_to_reorder_visibility","export_channel_margin_bridge","earnings_revision_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","global_food_distribution_crowding"],"stage4c_evidence_fields":["post_peak_high_MAE_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv","profile_path":"atlas/symbol_profiles/280/280360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.86,"MFE_90D_pct":57.83,"MFE_180D_pct":57.83,"MFE_1Y_pct":57.83,"MFE_2Y_pct":57.83,"MAE_30D_pct":-4.16,"MAE_90D_pct":-4.16,"MAE_180D_pct":-11.36,"MAE_1Y_pct":-11.36,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":208500,"drawdown_after_peak_pct":-43.84,"green_lateness_ratio":"0.34","four_b_local_peak_proximity":0.89,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_export_channel_reorder_bridge","four_b_evidence_type":"non_price_channel_reorder_margin_bridge","four_c_protection_label":"high_MAE_watch_after_peak","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L72_C18_280360_20240422_KFOOD_EXPORT_CHANNEL_REORDER_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R5L72_C18_001680_20240422_FOOD_EXPORT_CHANNEL_MARGIN_BRIDGE","case_id":"R5L72_C18_001680_20240422_FOOD_EXPORT_CHANNEL_MARGIN_BRIDGE","symbol":"001680","company_name":"대상","round":"R5","loop":"72","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"C18_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"SAUCE_FOOD_EXPORT_SELLTHROUGH_TO_MARGIN_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-22","entry_date":"2024-04-22","entry_price":21900,"evidence_available_at_that_date":"source_proxy_food_export_channel_sellthrough_reorder_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_food_export_channel_sellthrough_reorder_margin_bridge; evidence_url_pending","bridge_summary":"food export/channel reorder proxy translated into margin and earnings visibility, but post-peak drawdown requires watch discipline","stage2_evidence_fields":["food_export_channel","reorder_or_sellthrough_proxy","relative_strength","margin_mix_improvement"],"stage3_evidence_fields":["export_channel_conversion","earnings_visibility_proxy","non_price_reorder_bridge"],"stage4b_evidence_fields":["post_MFE_reversal_watch","consumer_export_crowding"],"stage4c_evidence_fields":["high_MAE_watch_after_peak"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001680/2024.csv","profile_path":"atlas/symbol_profiles/001/001680.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.79,"MFE_90D_pct":41.1,"MFE_180D_pct":41.1,"MFE_1Y_pct":41.1,"MFE_2Y_pct":41.1,"MAE_30D_pct":-3.88,"MAE_90D_pct":-5.48,"MAE_180D_pct":-10.55,"MAE_1Y_pct":-10.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-17","peak_price":30900,"drawdown_after_peak_pct":-36.6,"green_lateness_ratio":"0.38","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_4B_watch_but_requires_reorder_durability_guard","four_b_evidence_type":"non_price_channel_reorder_margin_bridge","four_c_protection_label":"high_MAE_watch_after_peak","trigger_outcome_label":"structural_success_but_needs_4B_high_MAE_guard","current_profile_verdict":"current_profile_partially_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L72_C18_001680_20240422_FOOD_EXPORT_CHANNEL_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R5L72_C18_248170_20240618_FOOD_THEME_WITHOUT_REORDER_BRIDGE","case_id":"R5L72_C18_248170_20240618_FOOD_THEME_WITHOUT_REORDER_BRIDGE","symbol":"248170","company_name":"샘표식품","round":"R5","loop":"72","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"C18_FOOD_THEME_PRICE_SPIKE_WITHOUT_REORDER_BRIDGE","deep_sub_archetype_id":"K_FOOD_THEME_WITHOUT_CHANNEL_SELLTHROUGH_OR_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-18","entry_date":"2024-06-18","entry_price":40350,"evidence_available_at_that_date":"source_proxy_K_food_theme_price_spike_without_reorder_or_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_K_food_theme_price_spike_without_reorder_or_margin_bridge; evidence_url_pending","bridge_summary":"food/K-food theme price spike lacked channel sell-through, reorder, or margin conversion bridge and reversed into high MAE","stage2_evidence_fields":["food_theme","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","weak_follow_through","reorder_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_channel_reorder_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/248/248170/2024.csv","profile_path":"atlas/symbol_profiles/248/248170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.76,"MFE_90D_pct":12.76,"MFE_180D_pct":12.76,"MFE_1Y_pct":12.76,"MFE_2Y_pct":12.76,"MAE_30D_pct":-25.4,"MAE_90D_pct":-33.58,"MAE_180D_pct":-33.58,"MAE_1Y_pct":-33.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-20","peak_price":45500,"drawdown_after_peak_pct":-41.1,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"price_theme_without_reorder_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L72_C18_248170_20240618_FOOD_THEME_WITHOUT_REORDER_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L72_C18_280360_20240422_KFOOD_EXPORT_CHANNEL_REORDER_BRIDGE","trigger_id":"TRG_R5L72_C18_280360_20240422_KFOOD_EXPORT_CHANNEL_REORDER_BRIDGE","symbol":"280360","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"export_channel_score":12,"reorder_bridge_score":12,"margin_mix_score":9,"relative_strength_score":10,"inventory_risk_score":3,"risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"export_channel_score":14,"reorder_bridge_score":16,"margin_mix_score":12,"relative_strength_score":8,"inventory_risk_score":4,"risk_penalty":4},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["export_channel_score","reorder_bridge_score","margin_mix_score","relative_strength_score","inventory_risk_score","risk_penalty"],"component_delta_explanation":"C18 row is promoted only because export channel expansion converts into sell-through/reorder and margin mix.","MFE_90D_pct":57.83,"MAE_90D_pct":-4.16,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L72_C18_001680_20240422_FOOD_EXPORT_CHANNEL_MARGIN_BRIDGE","trigger_id":"TRG_R5L72_C18_001680_20240422_FOOD_EXPORT_CHANNEL_MARGIN_BRIDGE","symbol":"001680","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"export_channel_score":11,"reorder_bridge_score":10,"margin_mix_score":8,"relative_strength_score":10,"inventory_risk_score":5,"risk_penalty":6},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"export_channel_score":12,"reorder_bridge_score":13,"margin_mix_score":9,"relative_strength_score":7,"inventory_risk_score":7,"risk_penalty":8},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["export_channel_score","reorder_bridge_score","margin_mix_score","relative_strength_score","inventory_risk_score","risk_penalty"],"component_delta_explanation":"C18 export/reorder bridge works, but post-MFE drawdown prevents Green loosening.","MFE_90D_pct":41.1,"MAE_90D_pct":-5.48,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L72_C18_248170_20240618_FOOD_THEME_WITHOUT_REORDER_BRIDGE","trigger_id":"TRG_R5L72_C18_248170_20240618_FOOD_THEME_WITHOUT_REORDER_BRIDGE","symbol":"248170","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","raw_component_scores_before":{"export_channel_score":6,"reorder_bridge_score":1,"margin_mix_score":1,"relative_strength_score":12,"inventory_risk_score":9,"risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"export_channel_score":3,"reorder_bridge_score":0,"margin_mix_score":0,"relative_strength_score":5,"inventory_risk_score":12,"risk_penalty":14},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["export_channel_score","reorder_bridge_score","margin_mix_score","relative_strength_score","inventory_risk_score","risk_penalty"],"component_delta_explanation":"C18 guard demotes K-food/food theme price spikes when channel sell-through/reorder bridge is absent.","MFE_90D_pct":12.76,"MAE_90D_pct":-33.58,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c18_requires_channel_sellthrough_reorder_margin_bridge,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"C18 consumer export/channel rows should not promote toward Stage3-Yellow/Green unless export channel expansion converts into sell-through, reorder, margin mix, or earnings visibility","280360 and 001680 survive with strong MFE after channel/reorder bridge; 248170 fails when K-food theme lacks channel sell-through/reorder bridge","TRG_R5L72_C18_280360_20240422_KFOOD_EXPORT_CHANNEL_REORDER_BRIDGE|TRG_R5L72_C18_001680_20240422_FOOD_EXPORT_CHANNEL_MARGIN_BRIDGE|TRG_R5L72_C18_248170_20240618_FOOD_THEME_WITHOUT_REORDER_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c18_consumer_export_4b_high_mae_watch_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,1,1,0,"Consumer export winners and food-theme failures can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 280360/001680 positives while preventing 248170 theme false positive","TRG_R5L72_C18_280360_20240422_KFOOD_EXPORT_CHANNEL_REORDER_BRIDGE|TRG_R5L72_C18_001680_20240422_FOOD_EXPORT_CHANNEL_MARGIN_BRIDGE|TRG_R5L72_C18_248170_20240618_FOOD_THEME_WITHOUT_REORDER_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"72","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["K_food_theme_without_channel_reorder_bridge","consumer_export_winner_needs_4B_watch","post_MFE_high_MAE_after_food_theme_price_spike"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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

## 22. Next Round State

```text
completed_round = R5
completed_loop = 72
next_round = R6
next_loop = 72
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
atlas/symbol_profiles/280/280360.json
atlas/symbol_profiles/001/001680.json
atlas/symbol_profiles/248/248170.json
atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv
atlas/ohlcv_tradable_by_symbol_year/001/001680/2024.csv
atlas/ohlcv_tradable_by_symbol_year/248/248170/2024.csv
```

This loop adds 3 new independent C18 cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R5/L5.
