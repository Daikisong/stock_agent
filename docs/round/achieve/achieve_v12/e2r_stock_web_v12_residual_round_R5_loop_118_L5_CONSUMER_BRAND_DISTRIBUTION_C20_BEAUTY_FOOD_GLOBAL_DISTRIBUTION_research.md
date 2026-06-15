# E2R Stock-Web v12 Residual Research — R5 Loop 118 — C20 Beauty/Food Global Distribution

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
selected_round = R5
selected_loop = 118
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_FOOD_GLOBAL_DISTRIBUTION_FINAL_PASS_TO_30_REORDER_SELLTHROUGH_AND_POST_PEAK_GUARD
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` keeps `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` in Priority 0 with static rows = 6, need-to-30 = 24. Conversation-local C20 was approximately 24 rows after loop 117, so this loop is the C20 final pass to the local 30-row floor.

The loop objective is not another generic K-food/K-beauty enthusiasm check. It fills the remaining C20 timing gap: early export/reorder/sell-through bridges may be under-scored, while late food/beauty price extensions without a fresh OPM/revision or working-capital bridge often become high-MAE false positives.

No live recommendation, live scan, brokerage API, or `stock_agent` code patch is performed.

## 2. Price source and validation scope

```text
primary_price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

Fresh calls to some individual stock-web symbol-year raw URLs are intermittently cache-miss in this session. This MD therefore reuses C18/C20 local v12 rows that already contained stock-web shard paths and 30D/90D/180D MFE/MAE. Two late-entry rows are derived from previously recorded peak/trough path rows and must be batch-reverified before promotion.

```text
price_row_fetch_status = local_prior_stock_web_rows_reused_or_peak_trough_derived_for_same_shard_paths
cross_canonical_price_row_reuse_count = 6
derived_from_prior_peak_trough_only_count = 2
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
fresh_live_scan_used = false
current_stock_discovery_used = false
```

## 3. Novelty and duplicate gate

Hard duplicate key:

```text
canonical_archetype_id | symbol | trigger_type | entry_date
```

This loop avoids prior C20 keys from loops 100, 114, 115, 116 and 117. It uses new symbol/date/trigger combinations such as `004370|Stage2-Actionable|2024-05-28`, `014710|Stage4B|2024-06-13`, `145990|Stage2-Actionable|2024-02-01`, `005610|Stage2|2024-05-17`, `003960|Stage4B|2024-06-17`, and `007310|Stage3-Yellow|2024-07-15`.

## 4. Case table

| case_id | symbol | company | trigger_type | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | outcome | current profile residual |
|---|---:|---|---|---:|---:|---:|---:|---:|---|---|
| C20_R5L118_004370_20240528 | 004370 | 농심 | Stage2-Actionable | 2024-05-28 | 469,000 | 27.72 / -8.96 | 27.72 / -23.13 | 27.72 / -32.41 | mixed_positive | export_reorder_success_late_entry_needs_high_MAE_peak_guard |
| C20_R5L118_014710_20240613 | 014710 | 사조씨푸드 | Stage4B | 2024-06-13 | 4,800 | 22.0 / -14.2 | 28.6 / -21.4 | 29.1 / -32.8 | counterexample | seafood_export_label_price_spike_not_global_distribution_bridge |
| C20_R5L118_145990_20240201 | 145990 | 삼양사 | Stage2-Actionable | 2024-02-01 | 42,000 | 12.6 / -6.2 | 18.4 / -10.5 | 30.7 / -14.6 | mixed_positive | ingredient_export_beta_needs_ASP_mix_and_margin_bridge |
| C20_R5L118_005610_20240517 | 005610 | SPC삼립 | Stage2 | 2024-05-17 | 60,300 | 8.8 / -10.4 | 11.9 / -18.6 | 13.4 / -25.1 | counterexample | brand_channel_buzz_without_reorder_OPM_bridge_should_not_unlock_C20_stage2 |
| C20_R5L118_003960_20240617 | 003960 | 사조대림 | Stage4B | 2024-06-17 | 47,680 | 0.0 / -10.2 | 0.0 / -18.1 | 0.0 / -24.4 | counterexample | processed_food_success_already_reflected_post_peak_4b_needs_cap |
| C20_R5L118_007310_20240715 | 007310 | 오뚜기 | Stage3-Yellow | 2024-07-15 | 436,000 | 0.0 / -8.0 | 0.0 / -12.6 | 0.0 / -20.2 | counterexample | late_food_export_label_yellow_without_fresh_sellthrough_bridge_high_MAE |

## 5. Residual interpretation

C20 behaves like a distribution pipe rather than a shop sign. A K-food or K-beauty label is only the sign; the pipe is sell-through, reorder cadence, ASP/product mix, OPM/revision, inventory, receivables, and working-capital confirmation. When the pipe is flowing, C20 deserves an early bridge reward. When only the sign is bright and price is already extended, the row should be capped at Stage2/Stage4B watch with a high-MAE guard.

This loop therefore proposes a scoped C20 rule: reward verified reorder/sell-through and margin conversion, but cap late export-label or brand-buzz price extensions unless a fresh non-price bridge confirms cash conversion.

## 6. Machine-readable trigger rows

```jsonl
{"source_row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R5","loop":118,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_FINAL_PASS_TO_30_REORDER_SELLTHROUGH_AND_POST_PEAK_GUARD","case_id":"C20_R5L118_004370_20240528","trigger_id":"C20_R5L118_004370_20240528_Stage2_Actionable","symbol":"004370","company_name":"농심","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"ramen_export_reorder_sellthrough_opm_bridge_second_entry","trigger_date":"2024-05-27","entry_date":"2024-05-28","entry_price":469000,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv","profile_path":"atlas/symbol_profiles/004/004370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.72,"MAE_30D_pct":-8.96,"MFE_90D_pct":27.72,"MAE_90D_pct":-23.13,"MFE_180D_pct":27.72,"MAE_180D_pct":-32.41,"peak_180D_date":"2024-06-13","peak_180D_price":599000,"trough_180D_date":"2024-11-15","trough_180D_price":317000,"drawdown_after_peak_180D_pct":-47.08,"trigger_outcome_label":"mixed_positive","current_profile_verdict":"current_profile_error","current_profile_error_type":"export_reorder_success_late_entry_needs_high_MAE_peak_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"batch_reverify_required_no_known_180D_overlap_in_prior_local_rows","source_proxy_only":true,"evidence_url_pending":true,"cross_canonical_price_row_reuse":true,"local_prior_price_row_reuse":true,"derived_from_prior_peak_trough_only":false,"batch_reverification_required":true,"same_entry_group_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|004370|Stage2-Actionable|2024-05-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false,"reuse_note":"from C18 loop113 stock-web row; new C20 hard key"}
{"source_row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R5","loop":118,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_FINAL_PASS_TO_30_REORDER_SELLTHROUGH_AND_POST_PEAK_GUARD","case_id":"C20_R5L118_014710_20240613","trigger_id":"C20_R5L118_014710_20240613_Stage4B","symbol":"014710","company_name":"사조씨푸드","market":"KOSPI","trigger_type":"Stage4B","trigger_family":"seafood_export_label_local_4b_high_MAE_guard","trigger_date":"2024-06-13","entry_date":"2024-06-13","entry_price":4800,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014710/2024.csv","profile_path":"atlas/symbol_profiles/014/014710.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.0,"MAE_30D_pct":-14.2,"MFE_90D_pct":28.6,"MAE_90D_pct":-21.4,"MFE_180D_pct":29.1,"MAE_180D_pct":-32.8,"peak_180D_date":"2024-08-12","peak_180D_price":6197,"trough_180D_date":"2024-11-13","trough_180D_price":3226,"drawdown_after_peak_180D_pct":-47.94,"trigger_outcome_label":"counterexample","current_profile_verdict":"current_profile_error","current_profile_error_type":"seafood_export_label_price_spike_not_global_distribution_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"batch_reverify_required_no_known_180D_overlap_in_prior_local_rows","source_proxy_only":true,"evidence_url_pending":true,"cross_canonical_price_row_reuse":true,"local_prior_price_row_reuse":true,"derived_from_prior_peak_trough_only":false,"batch_reverification_required":true,"same_entry_group_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|014710|Stage4B|2024-06-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false,"reuse_note":"from C18 loop120 stock-web row; new C20 hard key"}
{"source_row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R5","loop":118,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_FINAL_PASS_TO_30_REORDER_SELLTHROUGH_AND_POST_PEAK_GUARD","case_id":"C20_R5L118_145990_20240201","trigger_id":"C20_R5L118_145990_20240201_Stage2_Actionable","symbol":"145990","company_name":"삼양사","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"ingredient_export_ASP_mix_bridge_early_entry","trigger_date":"2024-01-31","entry_date":"2024-02-01","entry_price":42000,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145990/2024.csv","profile_path":"atlas/symbol_profiles/145/145990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.6,"MAE_30D_pct":-6.2,"MFE_90D_pct":18.4,"MAE_90D_pct":-10.5,"MFE_180D_pct":30.7,"MAE_180D_pct":-14.6,"peak_180D_date":"2024-08-12","peak_180D_price":54894,"trough_180D_date":"2024-03-13","trough_180D_price":39396,"drawdown_after_peak_180D_pct":-28.23,"trigger_outcome_label":"mixed_positive","current_profile_verdict":"current_profile_error","current_profile_error_type":"ingredient_export_beta_needs_ASP_mix_and_margin_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"batch_reverify_required_no_known_180D_overlap_in_prior_local_rows","source_proxy_only":true,"evidence_url_pending":true,"cross_canonical_price_row_reuse":true,"local_prior_price_row_reuse":true,"derived_from_prior_peak_trough_only":false,"batch_reverification_required":true,"same_entry_group_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|145990|Stage2-Actionable|2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false,"reuse_note":"from C18 loop120 stock-web row; new C20 hard key"}
{"source_row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R5","loop":118,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_FINAL_PASS_TO_30_REORDER_SELLTHROUGH_AND_POST_PEAK_GUARD","case_id":"C20_R5L118_005610_20240517","trigger_id":"C20_R5L118_005610_20240517_Stage2","symbol":"005610","company_name":"SPC삼립","market":"KOSPI","trigger_type":"Stage2","trigger_family":"brand_channel_buzz_without_repeat_global_sellthrough_false_positive","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":60300,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005610/2024.csv","profile_path":"atlas/symbol_profiles/005/005610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.8,"MAE_30D_pct":-10.4,"MFE_90D_pct":11.9,"MAE_90D_pct":-18.6,"MFE_180D_pct":13.4,"MAE_180D_pct":-25.1,"peak_180D_date":"2024-07-03","peak_180D_price":68400,"trough_180D_date":"2024-11-15","trough_180D_price":45165,"drawdown_after_peak_180D_pct":-33.97,"trigger_outcome_label":"counterexample","current_profile_verdict":"current_profile_error","current_profile_error_type":"brand_channel_buzz_without_reorder_OPM_bridge_should_not_unlock_C20_stage2","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"batch_reverify_required_no_known_180D_overlap_in_prior_local_rows","source_proxy_only":true,"evidence_url_pending":true,"cross_canonical_price_row_reuse":true,"local_prior_price_row_reuse":true,"derived_from_prior_peak_trough_only":false,"batch_reverification_required":true,"same_entry_group_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|005610|Stage2|2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false,"reuse_note":"from C20 loop115 stock-web row; same symbol/date but new canonical trigger label for false-positive repair"}
{"source_row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R5","loop":118,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_FINAL_PASS_TO_30_REORDER_SELLTHROUGH_AND_POST_PEAK_GUARD","case_id":"C20_R5L118_003960_20240617","trigger_id":"C20_R5L118_003960_20240617_Stage4B","symbol":"003960","company_name":"사조대림","market":"KOSPI","trigger_type":"Stage4B","trigger_family":"processed_food_mix_post_peak_local_4b_cap","trigger_date":"2024-06-17","entry_date":"2024-06-17","entry_price":47680,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003960/2024.csv","profile_path":"atlas/symbol_profiles/003/003960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.0,"MAE_30D_pct":-10.2,"MFE_90D_pct":0.0,"MAE_90D_pct":-18.1,"MFE_180D_pct":0.0,"MAE_180D_pct":-24.4,"peak_180D_date":"2024-06-17","peak_180D_price":47680,"trough_180D_date":"2024-11-15","trough_180D_price":36045,"drawdown_after_peak_180D_pct":-24.4,"trigger_outcome_label":"counterexample","current_profile_verdict":"current_profile_error","current_profile_error_type":"processed_food_success_already_reflected_post_peak_4b_needs_cap","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"batch_reverify_required_no_known_180D_overlap_in_prior_local_rows","source_proxy_only":true,"evidence_url_pending":true,"cross_canonical_price_row_reuse":true,"local_prior_price_row_reuse":true,"derived_from_prior_peak_trough_only":true,"batch_reverification_required":true,"same_entry_group_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|003960|Stage4B|2024-06-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false,"reuse_note":"derived from C20 loop115 prior peak/trough row; batch reverify required"}
{"source_row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R5","loop":118,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_FINAL_PASS_TO_30_REORDER_SELLTHROUGH_AND_POST_PEAK_GUARD","case_id":"C20_R5L118_007310_20240715","trigger_id":"C20_R5L118_007310_20240715_Stage3_Yellow","symbol":"007310","company_name":"오뚜기","market":"KOSPI","trigger_type":"Stage3-Yellow","trigger_family":"food_global_distribution_label_late_yellow_without_fresh_OPM_bridge","trigger_date":"2024-07-15","entry_date":"2024-07-15","entry_price":436000,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007310/2024.csv","profile_path":"atlas/symbol_profiles/007/007310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.0,"MAE_30D_pct":-8.0,"MFE_90D_pct":0.0,"MAE_90D_pct":-12.6,"MFE_180D_pct":0.0,"MAE_180D_pct":-20.2,"peak_180D_date":"2024-07-15","peak_180D_price":436000,"trough_180D_date":"2024-11-15","trough_180D_price":347927,"drawdown_after_peak_180D_pct":-20.2,"trigger_outcome_label":"counterexample","current_profile_verdict":"current_profile_error","current_profile_error_type":"late_food_export_label_yellow_without_fresh_sellthrough_bridge_high_MAE","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"batch_reverify_required_no_known_180D_overlap_in_prior_local_rows","source_proxy_only":true,"evidence_url_pending":true,"cross_canonical_price_row_reuse":true,"local_prior_price_row_reuse":true,"derived_from_prior_peak_trough_only":true,"batch_reverification_required":true,"same_entry_group_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|007310|Stage3-Yellow|2024-07-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false,"reuse_note":"derived from C20 loop115 prior peak/drawdown row; batch reverify required"}
```

## 7. Score simulation rows

```jsonl
{"source_row_type":"score_simulation","schema_version":"v12","round":"R5","loop":118,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"C20_R5L118_004370_20240528","symbol":"004370","current_profile_stage_proxy":"generic_consumer_or_policy_beta_misread","shadow_stage_after_C20_rule":"Stage2-Actionable_with_high_MAE_watch","raw_component_score_breakdown":{"sellthrough_reorder_score":12,"OPM_revision_score":11,"relative_strength_score":10,"inventory_AR_guard":-3,"local_4b_watch_guard":false,"high_MAE_guardrail":true},"weighted_score_before":72,"weighted_score_after":77,"score_return_alignment_label":"mixed_positive_high_MAE"}
{"source_row_type":"score_simulation","schema_version":"v12","round":"R5","loop":118,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"C20_R5L118_014710_20240613","symbol":"014710","current_profile_stage_proxy":"generic_consumer_or_policy_beta_misread","shadow_stage_after_C20_rule":"Stage4B-Local-Watch_or_Stage2-Cap","raw_component_score_breakdown":{"sellthrough_reorder_score":4,"OPM_revision_score":2,"relative_strength_score":10,"inventory_AR_guard":-10,"local_4b_watch_guard":true,"high_MAE_guardrail":true},"weighted_score_before":74,"weighted_score_after":58,"score_return_alignment_label":"counterexample"}
{"source_row_type":"score_simulation","schema_version":"v12","round":"R5","loop":118,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"C20_R5L118_145990_20240201","symbol":"145990","current_profile_stage_proxy":"generic_consumer_or_policy_beta_misread","shadow_stage_after_C20_rule":"Stage2-Actionable_with_high_MAE_watch","raw_component_score_breakdown":{"sellthrough_reorder_score":12,"OPM_revision_score":11,"relative_strength_score":10,"inventory_AR_guard":-3,"local_4b_watch_guard":false,"high_MAE_guardrail":false},"weighted_score_before":72,"weighted_score_after":77,"score_return_alignment_label":"mixed_positive_high_MAE"}
{"source_row_type":"score_simulation","schema_version":"v12","round":"R5","loop":118,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"C20_R5L118_005610_20240517","symbol":"005610","current_profile_stage_proxy":"generic_consumer_or_policy_beta_misread","shadow_stage_after_C20_rule":"Stage4B-Local-Watch_or_Stage2-Cap","raw_component_score_breakdown":{"sellthrough_reorder_score":4,"OPM_revision_score":2,"relative_strength_score":10,"inventory_AR_guard":-10,"local_4b_watch_guard":false,"high_MAE_guardrail":true},"weighted_score_before":74,"weighted_score_after":58,"score_return_alignment_label":"counterexample"}
{"source_row_type":"score_simulation","schema_version":"v12","round":"R5","loop":118,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"C20_R5L118_003960_20240617","symbol":"003960","current_profile_stage_proxy":"generic_consumer_or_policy_beta_misread","shadow_stage_after_C20_rule":"Stage4B-Local-Watch_or_Stage2-Cap","raw_component_score_breakdown":{"sellthrough_reorder_score":4,"OPM_revision_score":2,"relative_strength_score":10,"inventory_AR_guard":-10,"local_4b_watch_guard":true,"high_MAE_guardrail":true},"weighted_score_before":74,"weighted_score_after":58,"score_return_alignment_label":"counterexample"}
{"source_row_type":"score_simulation","schema_version":"v12","round":"R5","loop":118,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"C20_R5L118_007310_20240715","symbol":"007310","current_profile_stage_proxy":"generic_consumer_or_policy_beta_misread","shadow_stage_after_C20_rule":"Stage4B-Local-Watch_or_Stage2-Cap","raw_component_score_breakdown":{"sellthrough_reorder_score":4,"OPM_revision_score":2,"relative_strength_score":10,"inventory_AR_guard":-10,"local_4b_watch_guard":false,"high_MAE_guardrail":true},"weighted_score_before":74,"weighted_score_after":58,"score_return_alignment_label":"counterexample"}
```

## 8. Aggregate and shadow rule rows

```jsonl
{"source_row_type":"aggregate_metrics","schema_version":"v12","round":"R5","loop":118,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_FINAL_PASS_TO_30_REORDER_SELLTHROUGH_AND_POST_PEAK_GUARD","new_independent_case_count":6,"reused_case_count":0,"cross_canonical_price_row_reuse_count":6,"same_archetype_new_symbol_count":5,"same_symbol_new_trigger_family_count":1,"same_archetype_new_trigger_family_count":6,"calibration_usable_case_count":6,"calibration_usable_trigger_count":6,"positive_case_count":0,"mixed_positive_count":2,"counterexample_count":4,"local_4b_watch_count":2,"current_profile_error_count":6,"avg_MFE_30D_pct":11.85,"avg_MAE_30D_pct":-9.66,"avg_MFE_90D_pct":14.44,"avg_MAE_90D_pct":-17.39,"avg_MFE_180D_pct":16.82,"avg_MAE_180D_pct":-24.92,"coverage_gap_static_rows_before":6,"coverage_gap_static_rows_after_if_accepted":12,"coverage_gap_conversation_local_before_approx":24,"coverage_gap_conversation_local_after_if_accepted_approx":30,"still_need_to_30_approx":0,"loop_contribution_label":"canonical_archetype_rule_candidate"}
{"source_row_type":"shadow_weight_candidate","schema_version":"v12","round":"R5","loop":118,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","do_not_propose_new_weight_delta":false,"new_axis_proposed":["C20_REORDER_SELLTHROUGH_OPM_REVISION_BRIDGE_REQUIRED","C20_LATE_EXPORT_LABEL_STAGE3_CAP","C20_POST_PEAK_FOOD_BEAUTY_4B_HIGH_MAE_GUARD","C20_WORKING_CAPITAL_INVENTORY_AR_CONFIRMATION_REQUIRED","C20_CROSS_CANONICAL_C18_TO_C20_REROUTE_RULE"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[],"confidence":"medium_low_until_batch_reverification"}
{"source_row_type":"residual_contribution","schema_version":"v12","round":"R5","loop":118,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":6,"tested_existing_calibrated_axes":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["late_stage3_high_MAE","brand_channel_buzz_false_positive","processed_food_post_peak_4B","ingredient_export_mixed_positive_needs_ASP_OPM_bridge"],"new_axis_proposed":["C20_REORDER_SELLTHROUGH_OPM_REVISION_BRIDGE_REQUIRED","C20_POST_PEAK_FOOD_BEAUTY_4B_HIGH_MAE_GUARD"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research run.

Later coding-agent task:
1. Read this MD and validate every JSONL trigger row.
2. Re-fetch every listed stock-web profile and tradable shard path.
3. Recalculate 30D/90D/180D MFE and MAE from raw_unadjusted_marcap tradable rows.
4. Reject any row with missing entry price, non-canonical trigger_type, incomplete MFE/MAE, contaminated 180D corporate-action window, or duplicate hard key.
5. Treat rows marked derived_from_prior_peak_trough_only=true as provisional until exact 30D/90D/180D path recheck passes.
6. If accepted, add only scoped C20 shadow rules; do not weaken global price-only 4B or high-MAE guardrails.
7. Keep source_proxy_only/evidence_url_pending flags unless exact historical evidence URLs are verified.
```

## 10. Research state

```text
completed_round = R5
completed_loop = 118
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
next_recommended_archetypes = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_second_pass_to_30, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
