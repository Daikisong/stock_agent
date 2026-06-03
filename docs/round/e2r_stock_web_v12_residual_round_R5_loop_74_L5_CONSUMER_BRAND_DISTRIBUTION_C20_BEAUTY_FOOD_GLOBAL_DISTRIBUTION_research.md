# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R5
scheduled_loop: 74
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R6
computed_next_loop: 74
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: C20_REORDER_CHANNEL_MARGIN_UTILIZATION_BRIDGE_GUARD
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

R5 maps to `L5_CONSUMER_BRAND_DISTRIBUTION`. The previous R5 loop used C19 retail/inventory margin, so this run shifts to C20 beauty/food/global distribution. The selected set avoids the top-covered C20 cluster and focuses on ODM/export-channel bridge quality versus legacy beauty-channel false starts.

| layer | id | definition |
|---|---|---|
| round | R5 | consumer / brand / distribution |
| large_sector | L5_CONSUMER_BRAND_DISTRIBUTION | consumer, brand, distribution, beauty, food, global channels |
| canonical | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | beauty/food global channel, reorder, margin, sell-through |
| fine | C20_REORDER_CHANNEL_MARGIN_UTILIZATION_BRIDGE_GUARD | global channel signal must become reorder/channel/margin evidence |
| deep | K_BEAUTY_ODM_GLOBAL_INDIE_BRAND_ORDER_TO_MARGIN_AND_EXPORT_CHANNEL | ODM/global indie-brand positive |
| deep | K_BEAUTY_ODM_REORDER_EXPORT_CHANNEL_TO_MARGIN_AND_OPERATING_LEVERAGE | ODM reorder/margin positive |
| deep | LEGACY_BRAND_CHINA_REOPENING_THEME_WITHOUT_REORDER_SELLTHROUGH_MARGIN_CONVERSION | legacy China-channel false start |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C20 top-covered symbols are `257720`, `090430`, `003230`, `018290`, `051900`, and `192820`. This run avoids that cluster and also avoids the prior R5/C19 retail representatives.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C20 | 241710 | new independent | not top-covered C20 symbol; ODM/global indie-brand order-margin bridge |
| C20 | 161890 | new independent | not top-covered C20 symbol; ODM reorder/export-channel margin bridge |
| C20 | 226320 | new independent | not top-covered C20 symbol; legacy beauty/China-channel false start |

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
241710 has 2018 corporate-action candidates, outside the selected 2024 representative window.
161890 has no corporate-action candidate dates.
226320 has corporate-action candidates ending 2017/2022, outside the selected 2024 window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 241710 | 코스메카코리아 | Stage2-Actionable | 2024-02-21 | 41600 | ODM/global indie-brand order-margin bridge worked |
| structural_success_low_MAE_after_margin_bridge | 161890 | 한국콜마 | Stage2-Actionable | 2024-04-01 | 51500 | ODM reorder/export-channel margin bridge worked |
| failed_legacy_beauty_channel_margin_false_start | 226320 | 잇츠한불 | Stage2-Actionable | 2024-04-01 | 12390 | legacy beauty/China-channel theme lacked reorder/sell-through/margin bridge |

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
| 241710 | 코스메카코리아 | Stage2-Actionable | 2024-02-21 | 41600 | 6.73 | 111.06 | 136.78 | -25.48 | -25.48 | -25.48 | 2024-09-27 | 98500 | -22.94 |
| 161890 | 한국콜마 | Stage2-Actionable | 2024-04-01 | 51500 | 11.07 | 44.66 | 52.82 | -7.38 | -7.38 | -7.38 | 2024-09-30 | 78700 | -10.55 |
| 226320 | 잇츠한불 | Stage2-Actionable | 2024-04-01 | 12390 | 2.66 | 24.54 | 24.54 | -6.46 | -11.06 | -11.06 | 2024-06-27 | 15430 | -28.58 |

## 9. Case-by-Case Notes

### 9.1 241710 / 코스메카코리아 — ODM/global indie-brand order-margin bridge

The entry row is 2024-02-21 at 41,600. The path had early MAE, but the wider 90D/180D window reached 87,800 and 98,500. This is a valid C20 case because the evidence is not just beauty-theme momentum. The bridge is global indie-brand pull-through, ODM utilization, export channel, and margin visibility. It still needs 4B watch after the rerating because beauty ODM moves can crowd quickly.

### 9.2 161890 / 한국콜마 — ODM reorder and margin operating leverage bridge

The entry row is 2024-04-01 at 51,500. The 90D high reaches 74,500 and the broader high reaches 78,700 while early MAE is relatively contained. This is the cleaner C20 positive: reorder, export-channel quality, margin, and operating leverage carried the rerating.

### 9.3 226320 / 잇츠한불 — legacy beauty/China-channel theme without durable bridge

The entry row is 2024-04-01 at 12,390. The path reaches 15,430, but later falls to 11,020. This is the C20 false-positive branch. A legacy beauty or China-channel reopening theme can produce some MFE, but if reorder, sell-through, channel quality, margin, and cashflow do not follow, the signal should stay 4B/watch rather than climb to Stage3.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C20 treats beauty/China-channel theme as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C20 needs reorder/channel/margin bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for legacy beauty-channel rows. |
| Full 4B non-price requirement appropriate? | Yes. 241710/161890 have non-price bridge evidence; 226320 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
241710:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after ODM order/channel/margin bridge
  Stage3-Green = wait for post-MFE 4B review and margin durability

161890:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after reorder/export-channel margin bridge
  Stage3-Green = reject unless margin and channel durability remain confirmed

226320:
  Stage2-Actionable = acceptable only as legacy-channel watch
  Stage3-Yellow = reject without reorder, sell-through, margin or cashflow bridge
  Stage3-Green = reject despite MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 241710 | 0.89 | 1.00 | good full-window 4B watch after ODM global-channel margin bridge |
| 161890 | 0.95 | 1.00 | low-MAE 4B watch after ODM reorder margin bridge |
| 226320 | 0.98 | 1.00 | legacy beauty theme MFE but no channel-margin bridge; keep 4B watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c20_requires_reorder_channel_margin_utilization_bridge

rule:
  For C20 beauty/food/global-distribution rows, do not promote beauty,
  food, China-channel, K-beauty, ODM, brand, or global-distribution Stage2
  signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  reorder, sell-through, export-channel quality, customer/channel mix,
  utilization, margin conversion, operating leverage, FCF/cash conversion,
  or earnings revision tied to global channel economics.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 60.09 | -14.64 | 33.3% | useful but can over-credit legacy beauty/channel theme |
| P0b e2r_2_0_baseline_reference | 3 | 60.09 | -14.64 | 0% | safer but may miss 241710/161890 |
| P1 sector_specific_candidate_profile | 3 | 60.09 | -14.64 | 33.3% | no broad L5 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 77.86 | -16.43 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected/watch | 24.54 | -11.06 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 241710 | current_profile_correct | ODM/global-channel bridge aligned with strong MFE despite early MAE |
| 161890 | current_profile_correct | reorder/export-channel margin bridge aligned with strong positive path |
| 226320 | current_profile_false_positive_if_green | legacy beauty theme MFE lacked durable channel-margin bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | C20_REORDER_CHANNEL_MARGIN_UTILIZATION_BRIDGE_GUARD | 2 | 1 | 3 | 2 | 3 | 0 | 3 | 3 | 1 | false | true | C20 non-top-covered beauty/global channel residual reduced |

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
- legacy beauty channel theme without reorder/margin bridge
- beauty ODM winner needs 4B watch
- early MAE before channel-margin confirmation
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
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_requires_reorder_channel_margin_utilization_bridge,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"C20 beauty/food/global distribution rows should not promote toward Stage3-Yellow/Green unless beauty/food/global signal converts into reorder, sell-through, export-channel quality, utilization, margin, operating leverage, or cashflow bridge","241710 and 161890 survive after ODM/reorder/channel margin bridge; 226320 fails when legacy beauty/China-channel theme lacks reorder/sell-through/margin bridge","TRG_R5L74_C20_241710_20240221_BEAUTY_ODM_GLOBAL_INDIE_BRAND_MARGIN_BRIDGE|TRG_R5L74_C20_161890_20240401_BEAUTY_ODM_MARGIN_REORDER_BRIDGE|TRG_R5L74_C20_226320_20240401_LEGACY_BEAUTY_CHINA_THEME_NO_CHANNEL_MARGIN_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_beauty_channel_4b_high_mae_watch_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,1,1,0,"Beauty/channel winners and legacy theme false starts can peak before reorder and margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 241710/161890 positives while preventing 226320 channel-theme false positive","TRG_R5L74_C20_241710_20240221_BEAUTY_ODM_GLOBAL_INDIE_BRAND_MARGIN_BRIDGE|TRG_R5L74_C20_161890_20240401_BEAUTY_ODM_MARGIN_REORDER_BRIDGE|TRG_R5L74_C20_226320_20240401_LEGACY_BEAUTY_CHINA_THEME_NO_CHANNEL_MARGIN_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R5L74_C20_241710_20240221_BEAUTY_ODM_GLOBAL_INDIE_BRAND_MARGIN_BRIDGE","symbol":"241710","company_name":"코스메카코리아","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"C20_BEAUTY_ODM_GLOBAL_INDIE_BRAND_MARGIN_BRIDGE","deep_sub_archetype_id":"K_BEAUTY_ODM_GLOBAL_INDIE_BRAND_ORDER_TO_MARGIN_AND_EXPORT_CHANNEL","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C20 beauty/food/global distribution rows require reorder, sell-through, export-channel quality, margin, utilization, operating leverage, or cashflow bridge; beauty/China/channel theme alone is insufficient."}
{"row_type":"case","case_id":"R5L74_C20_161890_20240401_BEAUTY_ODM_MARGIN_REORDER_BRIDGE","symbol":"161890","company_name":"한국콜마","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"C20_BEAUTY_ODM_REORDER_MARGIN_OPERATING_LEVERAGE_BRIDGE","deep_sub_archetype_id":"K_BEAUTY_ODM_REORDER_EXPORT_CHANNEL_TO_MARGIN_AND_OPERATING_LEVERAGE","case_type":"structural_success_low_MAE_after_margin_bridge","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C20 beauty/food/global distribution rows require reorder, sell-through, export-channel quality, margin, utilization, operating leverage, or cashflow bridge; beauty/China/channel theme alone is insufficient."}
{"row_type":"case","case_id":"R5L74_C20_226320_20240401_LEGACY_BEAUTY_CHINA_THEME_NO_CHANNEL_MARGIN_BRIDGE","symbol":"226320","company_name":"잇츠한불","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"C20_LEGACY_BEAUTY_CHINA_THEME_WITHOUT_CHANNEL_MARGIN_BRIDGE","deep_sub_archetype_id":"LEGACY_BRAND_CHINA_REOPENING_THEME_WITHOUT_REORDER_SELLTHROUGH_MARGIN_CONVERSION","case_type":"failed_legacy_beauty_channel_margin_false_start","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C20 beauty/food/global distribution rows require reorder, sell-through, export-channel quality, margin, utilization, operating leverage, or cashflow bridge; beauty/China/channel theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R5L74_C20_241710_20240221_BEAUTY_ODM_GLOBAL_INDIE_BRAND_MARGIN_BRIDGE","case_id":"R5L74_C20_241710_20240221_BEAUTY_ODM_GLOBAL_INDIE_BRAND_MARGIN_BRIDGE","symbol":"241710","company_name":"코스메카코리아","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"C20_BEAUTY_ODM_GLOBAL_INDIE_BRAND_MARGIN_BRIDGE","deep_sub_archetype_id":"K_BEAUTY_ODM_GLOBAL_INDIE_BRAND_ORDER_TO_MARGIN_AND_EXPORT_CHANNEL","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":41600,"evidence_available_at_that_date":"source_proxy_beauty_ODM_global_indie_brand_order_margin_export_channel_bridge; evidence_url_pending","evidence_source":"source_proxy_beauty_ODM_global_indie_brand_order_margin_export_channel_bridge; evidence_url_pending","bridge_summary":"global indie-brand and K-beauty ODM order route converted into export channel, utilization, margin and earnings visibility rather than beauty theme only","stage2_evidence_fields":["K_beauty_ODM_order","global_indie_brand_pullthrough","relative_strength","export_channel_visibility_proxy"],"stage3_evidence_fields":["order_to_revenue_visibility","ODM_utilization_margin_bridge","earnings_revision_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","beauty_ODM_crowding_after_margin_rerating"],"stage4c_evidence_fields":["early_MAE_watch_before_margin_confirmation"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/241/241710/2024.csv","profile_path":"atlas/symbol_profiles/241/241710.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.73,"MFE_90D_pct":111.06,"MFE_180D_pct":136.78,"MFE_1Y_pct":136.78,"MFE_2Y_pct":136.78,"MAE_30D_pct":-25.48,"MAE_90D_pct":-25.48,"MAE_180D_pct":-25.48,"MAE_1Y_pct":-25.48,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-27","peak_price":98500,"drawdown_after_peak_pct":-22.94,"green_lateness_ratio":"0.34","four_b_local_peak_proximity":0.89,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_ODM_global_channel_margin_bridge","four_b_evidence_type":"non_price_reorder_channel_margin_bridge","four_c_protection_label":"early_MAE_watch","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L74_C20_241710_20240221_BEAUTY_ODM_GLOBAL_INDIE_BRAND_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R5L74_C20_161890_20240401_BEAUTY_ODM_MARGIN_REORDER_BRIDGE","case_id":"R5L74_C20_161890_20240401_BEAUTY_ODM_MARGIN_REORDER_BRIDGE","symbol":"161890","company_name":"한국콜마","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"C20_BEAUTY_ODM_REORDER_MARGIN_OPERATING_LEVERAGE_BRIDGE","deep_sub_archetype_id":"K_BEAUTY_ODM_REORDER_EXPORT_CHANNEL_TO_MARGIN_AND_OPERATING_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":51500,"evidence_available_at_that_date":"source_proxy_beauty_ODM_reorder_export_channel_margin_operating_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_beauty_ODM_reorder_export_channel_margin_operating_leverage_bridge; evidence_url_pending","bridge_summary":"beauty ODM reorder and global channel recovery converted into margin and operating leverage visibility with relatively contained early MAE","stage2_evidence_fields":["beauty_ODM_reorder","global_channel_recovery","relative_strength","margin_leverage_proxy"],"stage3_evidence_fields":["reorder_to_revenue_visibility","margin_operating_leverage","export_channel_quality_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","beauty_ODM_margin_cycle_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv","profile_path":"atlas/symbol_profiles/161/161890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.07,"MFE_90D_pct":44.66,"MFE_180D_pct":52.82,"MFE_1Y_pct":52.82,"MFE_2Y_pct":52.82,"MAE_30D_pct":-7.38,"MAE_90D_pct":-7.38,"MAE_180D_pct":-7.38,"MAE_1Y_pct":-7.38,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-30","peak_price":78700,"drawdown_after_peak_pct":-10.55,"green_lateness_ratio":"0.42","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"low_MAE_4B_watch_after_ODM_reorder_margin_bridge","four_b_evidence_type":"non_price_reorder_channel_margin_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_low_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L74_C20_161890_20240401_BEAUTY_ODM_MARGIN_REORDER_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R5L74_C20_226320_20240401_LEGACY_BEAUTY_CHINA_THEME_NO_CHANNEL_MARGIN_BRIDGE","case_id":"R5L74_C20_226320_20240401_LEGACY_BEAUTY_CHINA_THEME_NO_CHANNEL_MARGIN_BRIDGE","symbol":"226320","company_name":"잇츠한불","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"C20_LEGACY_BEAUTY_CHINA_THEME_WITHOUT_CHANNEL_MARGIN_BRIDGE","deep_sub_archetype_id":"LEGACY_BRAND_CHINA_REOPENING_THEME_WITHOUT_REORDER_SELLTHROUGH_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":12390,"evidence_available_at_that_date":"source_proxy_legacy_beauty_China_channel_theme_without_reorder_sellthrough_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_legacy_beauty_China_channel_theme_without_reorder_sellthrough_margin_bridge; evidence_url_pending","bridge_summary":"legacy beauty/China-channel theme did not convert into durable reorder, sell-through, channel-quality, margin or cashflow bridge","stage2_evidence_fields":["legacy_beauty_reopening_theme","China_channel_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_theme_peak","channel_quality_bridge_absent","sellthrough_margin_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_channel_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/226/226320/2024.csv","profile_path":"atlas/symbol_profiles/226/226320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.66,"MFE_90D_pct":24.54,"MFE_180D_pct":24.54,"MFE_1Y_pct":24.54,"MFE_2Y_pct":24.54,"MAE_30D_pct":-6.46,"MAE_90D_pct":-11.06,"MAE_180D_pct":-11.06,"MAE_1Y_pct":-11.06,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-27","peak_price":15430,"drawdown_after_peak_pct":-28.58,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"legacy_beauty_theme_MFE_but_no_channel_margin_bridge_keep_4B_watch","four_b_evidence_type":"beauty_theme_without_channel_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_channel_margin_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L74_C20_226320_20240401_LEGACY_BEAUTY_CHINA_THEME_NO_CHANNEL_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L74_C20_241710_20240221_BEAUTY_ODM_GLOBAL_INDIE_BRAND_MARGIN_BRIDGE","trigger_id":"TRG_R5L74_C20_241710_20240221_BEAUTY_ODM_GLOBAL_INDIE_BRAND_MARGIN_BRIDGE","symbol":"241710","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"global_channel_score":12,"reorder_sellthrough_score":12,"margin_utilization_score":11,"brand_or_ODM_quality_score":10,"relative_strength_score":10,"risk_penalty":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"global_channel_score":15,"reorder_sellthrough_score":15,"margin_utilization_score":14,"brand_or_ODM_quality_score":13,"relative_strength_score":8,"risk_penalty":6},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow","changed_components":["global_channel_score","reorder_sellthrough_score","margin_utilization_score","brand_or_ODM_quality_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C20 row is promoted only because beauty/global distribution signal converts into reorder, export-channel quality, margin and utilization bridge.","MFE_90D_pct":111.06,"MAE_90D_pct":-25.48,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L74_C20_161890_20240401_BEAUTY_ODM_MARGIN_REORDER_BRIDGE","trigger_id":"TRG_R5L74_C20_161890_20240401_BEAUTY_ODM_MARGIN_REORDER_BRIDGE","symbol":"161890","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"global_channel_score":12,"reorder_sellthrough_score":12,"margin_utilization_score":11,"brand_or_ODM_quality_score":10,"relative_strength_score":10,"risk_penalty":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"global_channel_score":15,"reorder_sellthrough_score":15,"margin_utilization_score":14,"brand_or_ODM_quality_score":13,"relative_strength_score":8,"risk_penalty":6},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow","changed_components":["global_channel_score","reorder_sellthrough_score","margin_utilization_score","brand_or_ODM_quality_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C20 row is promoted only because beauty/global distribution signal converts into reorder, export-channel quality, margin and utilization bridge.","MFE_90D_pct":44.66,"MAE_90D_pct":-7.38,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L74_C20_226320_20240401_LEGACY_BEAUTY_CHINA_THEME_NO_CHANNEL_MARGIN_BRIDGE","trigger_id":"TRG_R5L74_C20_226320_20240401_LEGACY_BEAUTY_CHINA_THEME_NO_CHANNEL_MARGIN_BRIDGE","symbol":"226320","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"global_channel_score":8,"reorder_sellthrough_score":1,"margin_utilization_score":1,"brand_or_ODM_quality_score":3,"relative_strength_score":9,"risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"global_channel_score":4,"reorder_sellthrough_score":0,"margin_utilization_score":0,"brand_or_ODM_quality_score":1,"relative_strength_score":4,"risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["global_channel_score","reorder_sellthrough_score","margin_utilization_score","brand_or_ODM_quality_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C20 guard demotes legacy beauty/channel theme rows when reorder, sell-through, channel quality, margin or cashflow bridge is absent.","MFE_90D_pct":24.54,"MAE_90D_pct":-11.06,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_requires_reorder_channel_margin_utilization_bridge,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"C20 beauty/food/global distribution rows should not promote toward Stage3-Yellow/Green unless beauty/food/global signal converts into reorder, sell-through, export-channel quality, utilization, margin, operating leverage, or cashflow bridge","241710 and 161890 survive after ODM/reorder/channel margin bridge; 226320 fails when legacy beauty/China-channel theme lacks reorder/sell-through/margin bridge","TRG_R5L74_C20_241710_20240221_BEAUTY_ODM_GLOBAL_INDIE_BRAND_MARGIN_BRIDGE|TRG_R5L74_C20_161890_20240401_BEAUTY_ODM_MARGIN_REORDER_BRIDGE|TRG_R5L74_C20_226320_20240401_LEGACY_BEAUTY_CHINA_THEME_NO_CHANNEL_MARGIN_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_beauty_channel_4b_high_mae_watch_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,1,1,0,"Beauty/channel winners and legacy theme false starts can peak before reorder and margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 241710/161890 positives while preventing 226320 channel-theme false positive","TRG_R5L74_C20_241710_20240221_BEAUTY_ODM_GLOBAL_INDIE_BRAND_MARGIN_BRIDGE|TRG_R5L74_C20_161890_20240401_BEAUTY_ODM_MARGIN_REORDER_BRIDGE|TRG_R5L74_C20_226320_20240401_LEGACY_BEAUTY_CHINA_THEME_NO_CHANNEL_MARGIN_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"74","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["legacy_beauty_channel_theme_without_reorder_margin_bridge","beauty_ODM_winner_needs_4B_watch","early_MAE_before_channel_margin_confirmation"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- price-only/beauty-channel-theme-only rows cannot promote Stage2/Stage3.
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
11. Add validation that C20 beauty/food/global-distribution rows cannot promote without reorder, sell-through, export-channel quality, margin, utilization, operating leverage, FCF/cash conversion, or earnings-revision bridge.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R5
completed_loop = 74
next_round = R6
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
atlas/symbol_profiles/241/241710.json
atlas/symbol_profiles/161/161890.json
atlas/symbol_profiles/226/226320.json
atlas/ohlcv_tradable_by_symbol_year/241/241710/2024.csv
atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv
atlas/ohlcv_tradable_by_symbol_year/226/226320/2024.csv
```

This loop continues loop 74 with R5 and adds 3 new independent C20 representative cases, 2 positives, 1 counterexample/watch case, and 1 canonical-archetype residual guard candidate for R5/L5.
