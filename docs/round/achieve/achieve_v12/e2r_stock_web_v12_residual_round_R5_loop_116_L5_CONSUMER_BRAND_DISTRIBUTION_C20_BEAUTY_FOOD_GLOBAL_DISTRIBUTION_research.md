# E2R Stock-Web v12 Residual Research — R5 Loop 116 — C20 Beauty/Food Global Distribution

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
selected_round = R5
selected_loop = 116
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_FOOD_BEAUTY_GLOBAL_DISTRIBUTION_SECOND_PASS_TO_30_REORDER_SELLTHROUGH_OPM_BRIDGE
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` still treats `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` as a Priority 0 under-covered archetype. Static index rows are 6, so the canonical remains far below the 30-row minimum. Conversation-local C20 rows were also still below the local 30-row floor after the prior C20 pass, so this loop continues C20 rather than rotating mechanically by round.

This loop deliberately does not make current/live recommendations and does not patch `stock_agent`. It only produces historical trigger-level residual calibration rows that a later batch coding agent can ingest or reject.

## 2. Price source and validation scope

```text
primary_price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

Fresh raw shard calls for some `stock-web` symbol-year URLs remain intermittently cache-miss in this session. To keep the C20 row set usable without inventing unverified values, this MD uses price rows already present in local v12 artifacts whose stock-web shard paths were previously checked. Every reused row is marked `cross_canonical_price_row_reuse = true`, `source_proxy_only = true`, `evidence_url_pending = true`, and `batch_reverification_required = true`.

```text
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths
cross_canonical_price_row_reuse_count = 5
batch_reverification_required = true
fresh_live_scan_used = false
current_stock_discovery_used = false
```

## 3. Novelty and duplicate gate

Hard duplicate key format:

```text
canonical_archetype_id | symbol | trigger_type | entry_date
```

The loop avoids prior C20 hard keys such as:

```text
C20|257720|Stage2-Actionable|2024-05-09
C20|257720|Stage4B|2024-06-12
C20|161890|Stage2-Actionable|2024-04-01
C20|192820|Stage3-Yellow|2024-04-01
C20|003230|Stage2-Actionable|2024-05-10
C20|004370|Stage2-Actionable|2024-02-01
C20|007310|Stage3-Yellow|2024-02-02
C20|001680|Stage2-Actionable|2024-02-01
C20|005610|Stage4B|2024-05-17
C20|003960|Stage2-Actionable|2024-02-01
```

This loop uses either new symbols for C20 or new trigger families/entry dates under C20. Several price paths overlap with C18, but the canonical hard key is new for C20 and the reuse is explicitly disclosed.

## 4. Case table

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | outcome | current profile error |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| C20_R5L116_003230_20240417 | 003230 | 삼양식품 | Stage3-Yellow | 2024-04-17 | 260500 | 131.9 | -3.5 | 175.6 | -3.5 | 197.5 | -3.5 | positive | too_late_without_food_global_distribution_bridge |
| C20_R5L116_005180_20240517 | 005180 | 빙그레 | Stage2-Actionable | 2024-05-17 | 88300 | 34.09 | -9.29 | 34.09 | -32.96 | 34.09 | -32.96 | mixed_positive | high_MAE_success_needs_peak_guard |
| C20_R5L116_005180_20240611 | 005180 | 빙그레 | Stage4B | 2024-06-11 | 109000 | 8.62 | -25.5 | 8.62 | -45.69 | 8.62 | -45.69 | counterexample | price_only_4B_must_not_be_full_4B |
| C20_R5L116_271560_20240116 | 271560 | 오리온 | Stage2 | 2024-01-16 | 96600 | 2.9 | -7.14 | 2.9 | -7.66 | 10.46 | -15.32 | counterexample | overseas_channel_label_without_cash_bridge_false_positive |
| C20_R5L116_145990_20240522 | 145990 | 삼양사 | Stage2-Actionable | 2024-05-22 | 45200 | 13.6 | -8.1 | 20.2 | -12.9 | 25.5 | -17.6 | mixed_positive | ingredient_export_beta_needs_ASP_mix_OPM_bridge |

## 5. Residual interpretation

C20 is not simply “food/beauty stock went up.” The useful signal is a chain: overseas channel or distributor traction → sell-through/reorder evidence → product mix or ASP improvement → OPM/revision or working-capital confirmation. When that chain is visible, the calibrated profile can be too late because it treats the move as generic consumer beta. When only a K-food/K-beauty label or one-off channel buzz exists, the same price strength becomes a local 4B watch or a Stage2 false positive.

This loop therefore reinforces a C20-specific bridge rule while preserving the global guardrails already applied in v12: price-only blowoffs remain capped, full 4B still requires non-price evidence, and high-MAE paths need a post-peak guard.

## 6. Machine-readable trigger rows

```jsonl
{"source_row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R5","loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_BEAUTY_GLOBAL_DISTRIBUTION_SECOND_PASS_TO_30_REORDER_SELLTHROUGH_OPM_BRIDGE","case_id":"C20_R5L116_003230_20240417","trigger_id":"C20_R5L116_003230_20240417_Stage3_Yellow","symbol":"003230","company_name":"삼양식품","trigger_type":"Stage3-Yellow","trigger_date":"2024-04-16","entry_date":"2024-04-17","entry_price":260500,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":131.9,"MAE_30D_pct":-3.5,"MFE_90D_pct":175.6,"MAE_90D_pct":-3.5,"MFE_180D_pct":197.5,"MAE_180D_pct":-3.5,"peak_180D_date":"2025-01-02","peak_180D_price":775000,"trough_180D_date":"2024-04-17","trough_180D_price":251500,"drawdown_after_peak_180D_pct":-35.5,"trigger_outcome_label":"positive","current_profile_verdict":"current_profile_too_late","current_profile_error_type":"too_late_without_food_global_distribution_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"batch_reverify_required_no_known_180D_overlap_in_prior_rows","source_proxy_only":true,"evidence_url_pending":true,"cross_canonical_price_row_reuse":true,"batch_reverification_required":true,"same_entry_group_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|003230|Stage3-Yellow|2024-04-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false}
{"source_row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R5","loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_BEAUTY_GLOBAL_DISTRIBUTION_SECOND_PASS_TO_30_REORDER_SELLTHROUGH_OPM_BRIDGE","case_id":"C20_R5L116_005180_20240517","trigger_id":"C20_R5L116_005180_20240517_Stage2_Actionable","symbol":"005180","company_name":"빙그레","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":88300,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv","profile_path":"atlas/symbol_profiles/005/005180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":34.09,"MAE_30D_pct":-9.29,"MFE_90D_pct":34.09,"MAE_90D_pct":-32.96,"MFE_180D_pct":34.09,"MAE_180D_pct":-32.96,"peak_180D_date":"2024-06-11","peak_180D_price":118400,"trough_180D_date":"2024-11-15","trough_180D_price":59200,"drawdown_after_peak_180D_pct":-50.0,"trigger_outcome_label":"mixed_positive","current_profile_verdict":"current_profile_undercredits_bridge_but_needs_high_MAE_guard","current_profile_error_type":"high_MAE_success_needs_peak_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_corporate_action_dates_before_1999_in_prior_rows","source_proxy_only":true,"evidence_url_pending":true,"cross_canonical_price_row_reuse":true,"batch_reverification_required":true,"same_entry_group_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|005180|Stage2-Actionable|2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false}
{"source_row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R5","loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_BEAUTY_GLOBAL_DISTRIBUTION_SECOND_PASS_TO_30_REORDER_SELLTHROUGH_OPM_BRIDGE","case_id":"C20_R5L116_005180_20240611","trigger_id":"C20_R5L116_005180_20240611_Stage4B","symbol":"005180","company_name":"빙그레","trigger_type":"Stage4B","trigger_date":"2024-06-11","entry_date":"2024-06-11","entry_price":109000,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv","profile_path":"atlas/symbol_profiles/005/005180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.62,"MAE_30D_pct":-25.5,"MFE_90D_pct":8.62,"MAE_90D_pct":-45.69,"MFE_180D_pct":8.62,"MAE_180D_pct":-45.69,"peak_180D_date":"2024-06-11","peak_180D_price":118400,"trough_180D_date":"2024-11-15","trough_180D_price":59200,"drawdown_after_peak_180D_pct":-50.0,"four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":0.91,"trigger_outcome_label":"counterexample","current_profile_verdict":"current_profile_false_positive_if_price_only_4B_promoted","current_profile_error_type":"price_only_4B_must_not_be_full_4B","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_corporate_action_dates_before_1999_in_prior_rows","source_proxy_only":true,"evidence_url_pending":true,"cross_canonical_price_row_reuse":true,"batch_reverification_required":true,"same_entry_group_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|005180|Stage4B|2024-06-11","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false}
{"source_row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R5","loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_BEAUTY_GLOBAL_DISTRIBUTION_SECOND_PASS_TO_30_REORDER_SELLTHROUGH_OPM_BRIDGE","case_id":"C20_R5L116_271560_20240116","trigger_id":"C20_R5L116_271560_20240116_Stage2","symbol":"271560","company_name":"오리온","trigger_type":"Stage2","trigger_date":"2024-01-16","entry_date":"2024-01-16","entry_price":96600,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv","profile_path":"atlas/symbol_profiles/271/271560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.9,"MAE_30D_pct":-7.14,"MFE_90D_pct":2.9,"MAE_90D_pct":-7.66,"MFE_180D_pct":10.46,"MAE_180D_pct":-15.32,"peak_180D_date":"2024-06-18","peak_180D_price":106700,"trough_180D_date":"2024-07-17","trough_180D_price":81800,"drawdown_after_peak_180D_pct":-23.34,"trigger_outcome_label":"counterexample","current_profile_verdict":"current_profile_false_positive","current_profile_error_type":"overseas_channel_label_without_cash_bridge_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_no_corporate_action_candidate_in_prior_rows","source_proxy_only":true,"evidence_url_pending":true,"cross_canonical_price_row_reuse":true,"batch_reverification_required":true,"same_entry_group_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|271560|Stage2|2024-01-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false}
{"source_row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R5","loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_BEAUTY_GLOBAL_DISTRIBUTION_SECOND_PASS_TO_30_REORDER_SELLTHROUGH_OPM_BRIDGE","case_id":"C20_R5L116_145990_20240522","trigger_id":"C20_R5L116_145990_20240522_Stage2_Actionable","symbol":"145990","company_name":"삼양사","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-21","entry_date":"2024-05-22","entry_price":45200,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145990/2024.csv","profile_path":"atlas/symbol_profiles/145/145990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.6,"MAE_30D_pct":-8.1,"MFE_90D_pct":20.2,"MAE_90D_pct":-12.9,"MFE_180D_pct":25.5,"MAE_180D_pct":-17.6,"peak_180D_date":"2024-08-12","peak_180D_price":56700,"trough_180D_date":"2024-11-12","trough_180D_price":37200,"drawdown_after_peak_180D_pct":-24.0,"trigger_outcome_label":"mixed_positive","current_profile_verdict":"current_profile_undercredits_bridge_but_needs_ASP_mix_guard","current_profile_error_type":"ingredient_export_beta_needs_ASP_mix_OPM_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"batch_reverify_required_no_known_180D_overlap_in_prior_rows","source_proxy_only":true,"evidence_url_pending":true,"cross_canonical_price_row_reuse":true,"batch_reverification_required":true,"same_entry_group_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|145990|Stage2-Actionable|2024-05-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false}
```

## 7. Score simulation rows

```jsonl
{"source_row_type":"score_simulation","schema_version":"v12","round":"R5","loop":116,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"C20_R5L116_003230_20240417","symbol":"003230","current_profile_stage_proxy":"Stage2-Actionable_or_late_Stage3","shadow_stage_after_C20_bridge":"Stage3-Yellow","raw_component_score_breakdown":{"sellthrough_reorder_score":16,"OPM_revision_score":15,"relative_strength_score":15,"inventory_AR_guard":0,"local_4b_watch_guard":false,"high_MAE_guardrail":false},"weighted_score_before":74,"weighted_score_after":83,"score_return_alignment_label":"positive"}
{"source_row_type":"score_simulation","schema_version":"v12","round":"R5","loop":116,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"C20_R5L116_005180_20240517","symbol":"005180","current_profile_stage_proxy":"Stage2-Actionable","shadow_stage_after_C20_bridge":"Stage2-Actionable_with_high_MAE_watch","raw_component_score_breakdown":{"sellthrough_reorder_score":12,"OPM_revision_score":10,"relative_strength_score":12,"inventory_AR_guard":-4,"local_4b_watch_guard":false,"high_MAE_guardrail":true},"weighted_score_before":73,"weighted_score_after":77,"score_return_alignment_label":"mixed_positive_high_MAE"}
{"source_row_type":"score_simulation","schema_version":"v12","round":"R5","loop":116,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"C20_R5L116_005180_20240611","symbol":"005180","current_profile_stage_proxy":"Stage4B_if_price_extension_only","shadow_stage_after_C20_bridge":"Stage4B-Local-Watch_not_full_4B","raw_component_score_breakdown":{"sellthrough_reorder_score":4,"OPM_revision_score":2,"relative_strength_score":10,"inventory_AR_guard":-8,"local_4b_watch_guard":true,"high_MAE_guardrail":true},"weighted_score_before":75,"weighted_score_after":58,"score_return_alignment_label":"counterexample"}
{"source_row_type":"score_simulation","schema_version":"v12","round":"R5","loop":116,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"C20_R5L116_271560_20240116","symbol":"271560","current_profile_stage_proxy":"Stage2","shadow_stage_after_C20_bridge":"Stage2-Watch_or_blocked","raw_component_score_breakdown":{"sellthrough_reorder_score":3,"OPM_revision_score":0,"relative_strength_score":4,"inventory_AR_guard":-6,"local_4b_watch_guard":false,"high_MAE_guardrail":true},"weighted_score_before":70,"weighted_score_after":55,"score_return_alignment_label":"counterexample"}
{"source_row_type":"score_simulation","schema_version":"v12","round":"R5","loop":116,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"C20_R5L116_145990_20240522","symbol":"145990","current_profile_stage_proxy":"Stage2-Actionable","shadow_stage_after_C20_bridge":"Stage2-Actionable_with_ASP_mix_watch","raw_component_score_breakdown":{"sellthrough_reorder_score":9,"OPM_revision_score":8,"relative_strength_score":8,"inventory_AR_guard":-2,"local_4b_watch_guard":false,"high_MAE_guardrail":true},"weighted_score_before":70,"weighted_score_after":74,"score_return_alignment_label":"mixed_positive"}
```

## 8. Aggregate and shadow rule rows

```jsonl
{"source_row_type":"aggregate_metrics","schema_version":"v12","round":"R5","loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_BEAUTY_GLOBAL_DISTRIBUTION_SECOND_PASS_TO_30_REORDER_SELLTHROUGH_OPM_BRIDGE","new_independent_case_count":5,"reused_case_count":0,"cross_canonical_price_row_reuse_count":5,"same_archetype_new_symbol_count":4,"same_symbol_new_trigger_family_count":1,"same_archetype_new_trigger_family_count":5,"calibration_usable_case_count":5,"calibration_usable_trigger_count":5,"positive_case_count":1,"mixed_positive_count":2,"counterexample_count":2,"local_4b_watch_count":1,"current_profile_error_count":5,"avg_MFE_30D_pct":38.22,"avg_MAE_30D_pct":-10.71,"avg_MFE_90D_pct":48.26,"avg_MAE_90D_pct":-20.54,"avg_MFE_180D_pct":55.23,"avg_MAE_180D_pct":-22.83,"coverage_gap_static_rows_before":6,"coverage_gap_static_rows_after_if_accepted":11,"coverage_gap_conversation_local_before_approx":13,"coverage_gap_conversation_local_after_if_accepted_approx":18,"still_need_to_30_approx":12,"loop_contribution_label":"canonical_archetype_rule_candidate"}
{"source_row_type":"shadow_weight_candidate","schema_version":"v12","round":"R5","loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","do_not_propose_new_weight_delta":false,"new_axis_proposed":["C20_REORDER_SELLTHROUGH_OPM_REVISION_BRIDGE_REQUIRED","C20_HIGH_MAE_EXPORT_FOOD_SUCCESS_REQUIRES_PEAK_GUARD","C20_GLOBAL_DISTRIBUTION_LABEL_WITHOUT_CASH_BRIDGE_STAGE2_CAP","C20_PRICE_ONLY_LOCAL_4B_BRAND_BUZZ_CAP","C20_INGREDIENT_EXPORT_ASP_MIX_OPM_BRIDGE_REQUIRED"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[],"confidence":"medium_low_until_batch_reverification","notes":"C20 needs a sector-specific bridge, but all reused rows remain source_proxy_only/evidence_url_pending until batch re-verification."}
{"source_row_type":"residual_contribution","schema_version":"v12","round":"R5","loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":5,"reused_case_count":0,"tested_existing_calibrated_axes":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive","high_MAE_after_export_success","price_only_local_4B_overpromotion"],"new_axis_proposed":["C20_REORDER_SELLTHROUGH_OPM_REVISION_BRIDGE_REQUIRED","C20_GLOBAL_DISTRIBUTION_LABEL_WITHOUT_CASH_BRIDGE_STAGE2_CAP"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research run.

Later coding-agent task:
1. Read this MD and validate every JSONL trigger row.
2. Re-fetch stock-web profile and tradable shard paths listed in each row.
3. Confirm 30D/90D/180D MFE and MAE from raw_unadjusted_marcap tradable rows.
4. Reject any row with missing entry price, missing trigger_type, incomplete MFE/MAE, contaminated 180D corporate-action window, or duplicate hard key.
5. If accepted, add C20-specific shadow rule candidates only as scoped profile changes; do not weaken global price-only 4B or high-MAE guardrails.
6. Keep source_proxy_only/evidence_url_pending flags unless exact historical evidence URLs are verified.
```

## 10. Research state

```text
completed_round = R5
completed_loop = 116
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
next_recommended_archetypes = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_third_pass_to_30, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
