# E2R Stock-Web v12 Residual Research — R5 Loop 117 — C20 Beauty/Food Global Distribution

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
selected_round = R5
selected_loop = 117
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_FOOD_GLOBAL_DISTRIBUTION_THIRD_PASS_TO_30_PROCESSED_FOOD_SEAFOOD_CONFECTIONERY_THEME_SPLIT
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` still lists `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` as Priority 0 with static rows far below the 30-row floor. Conversation-local generated rows put C18 and C31 at or near their local 30-row floor, while C20 remains below 30 even after loop 116. This run therefore keeps the scheduler on C20 rather than rotating mechanically.

The selected canonical maps to `R5 / L5_CONSUMER_BRAND_DISTRIBUTION`, so round, large sector, filename, and metadata are kept consistent.

## 2. Price source and validation scope

```text
primary_price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

Fresh individual raw shard calls are intermittently cache-missing in this session. To avoid inventing new price numbers, this MD reuses local v12 C18 rows that were already built from the same stock-web symbol-year shard paths. Every reused row is marked:

```text
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths
cross_canonical_price_row_reuse = true
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
```

This is not an exact duplicate because the v12 hard key includes the canonical archetype. The C20 hard keys below are new.

## 3. Research objective

```text
loop_objective = coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression
```

The C20 mechanism is not “export/brand headline goes up.” It is `global distribution → sell-through → reorder → OPM/revision/cash conversion`. A food label or K-brand label is like a truck leaving the warehouse: it matters only if the goods leave the shelf again and the next order arrives without bloating inventory or receivables.

## 4. Case table

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | outcome |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C20_R5L117_049770_20240201 | 049770 | 동원F&B | Stage2-Actionable | 2024-02-01 | 34500 | 13.5 | -5.8 | 20.9 | -8.2 | 27.6 | -13.4 | positive |
| C20_R5L117_006040_20240201 | 006040 | 동원산업 | Stage2-Actionable | 2024-02-01 | 33000 | 11.4 | -7.1 | 17.4 | -9.7 | 21.3 | -18.8 | mixed_positive |
| C20_R5L117_248170_20240321 | 248170 | 샘표식품 | Stage4B | 2024-03-21 | 32950 | 22.1 | -11.5 | 26.4 | -18.2 | 28.9 | -27.4 | local_4b_watch_counterexample |
| C20_R5L117_264900_20240226 | 264900 | 크라운제과 | Stage3-Yellow | 2024-02-26 | 8790 | 6.8 | -9.4 | 9.9 | -16.7 | 11.3 | -24.8 | counterexample |
| C20_R5L117_136480_20240202 | 136480 | 하림 | Stage3-Yellow | 2024-02-02 | 3100 | 7.5 | -8.4 | 10.2 | -17.9 | 12.8 | -27.5 | counterexample |

## 5. Machine-readable rows

```jsonl
{"source_row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R5","loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_THIRD_PASS_TO_30_PROCESSED_FOOD_SEAFOOD_CONFECTIONERY_THEME_SPLIT","case_id":"C20_R5L117_049770_20240201","trigger_id":"C20_R5L117_049770_20240201_Stage2_Actionable","symbol":"049770","company_name":"동원F&B","trigger_type":"Stage2-Actionable","trigger_family":"processed_food_global_channel_repeat_reorder_margin_bridge","trigger_date":"2024-01-31","entry_date":"2024-02-01","entry_price":34500,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/049/049770/2024.csv","profile_path":"atlas/symbol_profiles/049/049770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.5,"MAE_30D_pct":-5.8,"MFE_90D_pct":20.9,"MAE_90D_pct":-8.2,"MFE_180D_pct":27.6,"MAE_180D_pct":-13.4,"peak_180D_pct":27.6,"peak_180D_date":"2024-06-17","peak_180D_price":44000,"drawdown_after_peak_180D_pct":-16.8,"trigger_outcome_label":"positive","case_class":"positive","current_profile_verdict":"current_profile_error_or_stress_case","current_profile_error_type":"too_late_without_processed_food_reorder_OPM_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"batch_reverify_required_no_known_180D_overlap_in_prior_stock_web_rows","source_proxy_only":true,"evidence_url_pending":true,"cross_canonical_price_row_reuse":true,"cross_canonical_reuse_from":"C18_CONSUMER_EXPORT_CHANNEL_REORDER local v12 rows","batch_reverification_required":true,"price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths","same_entry_group_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|049770|Stage2-Actionable|2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false,"narrative_note":"processed food export/channel story is usable only when repeat demand and OPM/revision bridge appear together"}
{"source_row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R5","loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_THIRD_PASS_TO_30_PROCESSED_FOOD_SEAFOOD_CONFECTIONERY_THEME_SPLIT","case_id":"C20_R5L117_006040_20240201","trigger_id":"C20_R5L117_006040_20240201_Stage2_Actionable","symbol":"006040","company_name":"동원산업","trigger_type":"Stage2-Actionable","trigger_family":"seafood_food_export_inventory_margin_bridge","trigger_date":"2024-01-31","entry_date":"2024-02-01","entry_price":33000,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006040/2024.csv","profile_path":"atlas/symbol_profiles/006/006040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.4,"MAE_30D_pct":-7.1,"MFE_90D_pct":17.4,"MAE_90D_pct":-9.7,"MFE_180D_pct":21.3,"MAE_180D_pct":-18.8,"peak_180D_pct":21.3,"peak_180D_date":"2024-06-17","peak_180D_price":40000,"drawdown_after_peak_180D_pct":-24.9,"trigger_outcome_label":"mixed_positive","case_class":"mixed_positive","current_profile_verdict":"current_profile_error_or_stress_case","current_profile_error_type":"seafood_export_beta_requires_inventory_and_margin_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"batch_reverify_required_no_known_180D_overlap_in_prior_stock_web_rows","source_proxy_only":true,"evidence_url_pending":true,"cross_canonical_price_row_reuse":true,"cross_canonical_reuse_from":"C18_CONSUMER_EXPORT_CHANNEL_REORDER local v12 rows","batch_reverification_required":true,"price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths","same_entry_group_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|006040|Stage2-Actionable|2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false,"narrative_note":"food export beta can work but requires inventory/working-capital and margin confirmation before durable Stage3"}
{"source_row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R5","loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_THIRD_PASS_TO_30_PROCESSED_FOOD_SEAFOOD_CONFECTIONERY_THEME_SPLIT","case_id":"C20_R5L117_248170_20240321","trigger_id":"C20_R5L117_248170_20240321_Stage4B","symbol":"248170","company_name":"샘표식품","trigger_type":"Stage4B","trigger_family":"k_food_theme_spike_without_reorder_confirmation","trigger_date":"2024-03-20","entry_date":"2024-03-21","entry_price":32950,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/248/248170/2024.csv","profile_path":"atlas/symbol_profiles/248/248170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.1,"MAE_30D_pct":-11.5,"MFE_90D_pct":26.4,"MAE_90D_pct":-18.2,"MFE_180D_pct":28.9,"MAE_180D_pct":-27.4,"peak_180D_pct":28.9,"peak_180D_date":"2024-06-17","peak_180D_price":42500,"drawdown_after_peak_180D_pct":-31.6,"trigger_outcome_label":"counterexample","case_class":"local_4b_watch_counterexample","current_profile_verdict":"current_profile_error_or_stress_case","current_profile_error_type":"price_only_k_food_theme_spike_should_remain_local_4B","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"batch_reverify_required_no_known_180D_overlap_in_prior_stock_web_rows","source_proxy_only":true,"evidence_url_pending":true,"cross_canonical_price_row_reuse":true,"cross_canonical_reuse_from":"C18_CONSUMER_EXPORT_CHANNEL_REORDER local v12 rows","batch_reverification_required":true,"price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths","same_entry_group_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|248170|Stage4B|2024-03-21","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false,"narrative_note":"K-food theme spike has local MFE but high 180D MAE; without reorder evidence it should not be full 4B"}
{"source_row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R5","loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_THIRD_PASS_TO_30_PROCESSED_FOOD_SEAFOOD_CONFECTIONERY_THEME_SPLIT","case_id":"C20_R5L117_264900_20240226","trigger_id":"C20_R5L117_264900_20240226_Stage3_Yellow","symbol":"264900","company_name":"크라운제과","trigger_type":"Stage3-Yellow","trigger_family":"smallcap_confectionery_global_brand_buzz_false_positive","trigger_date":"2024-02-23","entry_date":"2024-02-26","entry_price":8790,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/264/264900/2024.csv","profile_path":"atlas/symbol_profiles/264/264900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.8,"MAE_30D_pct":-9.4,"MFE_90D_pct":9.9,"MAE_90D_pct":-16.7,"MFE_180D_pct":11.3,"MAE_180D_pct":-24.8,"peak_180D_pct":11.3,"peak_180D_date":"2024-06-17","peak_180D_price":9780,"drawdown_after_peak_180D_pct":-28.5,"trigger_outcome_label":"counterexample","case_class":"counterexample","current_profile_verdict":"current_profile_error_or_stress_case","current_profile_error_type":"small_cap_confectionery_export_buzz_high_MAE_guard_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"batch_reverify_required_no_known_180D_overlap_in_prior_stock_web_rows","source_proxy_only":true,"evidence_url_pending":true,"cross_canonical_price_row_reuse":true,"cross_canonical_reuse_from":"C18_CONSUMER_EXPORT_CHANNEL_REORDER local v12 rows","batch_reverification_required":true,"price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths","same_entry_group_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|264900|Stage3-Yellow|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false,"narrative_note":"confectionery export buzz was not enough; low MFE and high MAE make Stage3-Yellow too generous without cash bridge"}
{"source_row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R5","loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_THIRD_PASS_TO_30_PROCESSED_FOOD_SEAFOOD_CONFECTIONERY_THEME_SPLIT","case_id":"C20_R5L117_136480_20240202","trigger_id":"C20_R5L117_136480_20240202_Stage3_Yellow","symbol":"136480","company_name":"하림","trigger_type":"Stage3-Yellow","trigger_family":"protein_food_global_distribution_label_without_OPM_bridge","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":3100,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/136/136480/2024.csv","profile_path":"atlas/symbol_profiles/136/136480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.5,"MAE_30D_pct":-8.4,"MFE_90D_pct":10.2,"MAE_90D_pct":-17.9,"MFE_180D_pct":12.8,"MAE_180D_pct":-27.5,"peak_180D_pct":12.8,"peak_180D_date":"2024-04-15","peak_180D_price":3495,"drawdown_after_peak_180D_pct":-31.1,"trigger_outcome_label":"counterexample","case_class":"counterexample","current_profile_verdict":"current_profile_error_or_stress_case","current_profile_error_type":"protein_food_label_without_reorder_OPM_bridge_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"batch_reverify_required_no_known_180D_overlap_in_prior_stock_web_rows","source_proxy_only":true,"evidence_url_pending":true,"cross_canonical_price_row_reuse":true,"cross_canonical_reuse_from":"C18_CONSUMER_EXPORT_CHANNEL_REORDER local v12 rows","batch_reverification_required":true,"price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths","same_entry_group_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|136480|Stage3-Yellow|2024-02-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false,"narrative_note":"protein food label did not convert to durable MFE; inventory/OPM bridge required before Stage3"}
{"source_row_type":"score_simulation","schema_version":"v12","round":"R5","loop":117,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"C20_R5L117_049770_20240201","symbol":"049770","current_calibrated_proxy_stage":"Stage2-Actionable","shadow_stage_after_C20_bridge":"Stage2-Actionable_to_Yellow_watch","raw_component_score_breakdown":{"sellthrough_reorder_score":14,"OPM_revision_score":12,"working_capital_guard":1,"inventory_AR_guard":0,"local_4b_watch_guard":false,"high_MAE_guardrail":false},"weighted_score_before":76,"weighted_score_after":82,"score_return_alignment_label":"positive"}
{"source_row_type":"score_simulation","schema_version":"v12","round":"R5","loop":117,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"C20_R5L117_006040_20240201","symbol":"006040","current_calibrated_proxy_stage":"Stage2-Actionable","shadow_stage_after_C20_bridge":"Stage2-Actionable_with_inventory_guard","raw_component_score_breakdown":{"sellthrough_reorder_score":9,"OPM_revision_score":8,"working_capital_guard":1,"inventory_AR_guard":-2,"local_4b_watch_guard":false,"high_MAE_guardrail":true},"weighted_score_before":72,"weighted_score_after":76,"score_return_alignment_label":"mixed_positive"}
{"source_row_type":"score_simulation","schema_version":"v12","round":"R5","loop":117,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"C20_R5L117_248170_20240321","symbol":"248170","current_calibrated_proxy_stage":"Stage4B","shadow_stage_after_C20_bridge":"Stage4B-Local-Watch_not_full_4B","raw_component_score_breakdown":{"sellthrough_reorder_score":2,"OPM_revision_score":1,"working_capital_guard":-6,"inventory_AR_guard":-8,"local_4b_watch_guard":true,"high_MAE_guardrail":true},"weighted_score_before":78,"weighted_score_after":58,"score_return_alignment_label":"counterexample"}
{"source_row_type":"score_simulation","schema_version":"v12","round":"R5","loop":117,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"C20_R5L117_264900_20240226","symbol":"264900","current_calibrated_proxy_stage":"Stage3-Yellow","shadow_stage_after_C20_bridge":"Stage2-Watch_or_blocked","raw_component_score_breakdown":{"sellthrough_reorder_score":2,"OPM_revision_score":1,"working_capital_guard":-6,"inventory_AR_guard":-8,"local_4b_watch_guard":false,"high_MAE_guardrail":true},"weighted_score_before":75,"weighted_score_after":54,"score_return_alignment_label":"counterexample"}
{"source_row_type":"score_simulation","schema_version":"v12","round":"R5","loop":117,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","case_id":"C20_R5L117_136480_20240202","symbol":"136480","current_calibrated_proxy_stage":"Stage3-Yellow","shadow_stage_after_C20_bridge":"Stage2-Watch_or_blocked","raw_component_score_breakdown":{"sellthrough_reorder_score":2,"OPM_revision_score":1,"working_capital_guard":-6,"inventory_AR_guard":-8,"local_4b_watch_guard":false,"high_MAE_guardrail":true},"weighted_score_before":74,"weighted_score_after":53,"score_return_alignment_label":"counterexample"}
{"source_row_type":"aggregate_metrics","schema_version":"v12","round":"R5","loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_THIRD_PASS_TO_30_PROCESSED_FOOD_SEAFOOD_CONFECTIONERY_THEME_SPLIT","new_independent_case_count":5,"reused_case_count":0,"cross_canonical_price_row_reuse_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":5,"calibration_usable_case_count":5,"calibration_usable_trigger_count":5,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":3,"local_4b_watch_count":1,"current_profile_error_count":5,"coverage_gap_static_rows_before":6,"coverage_gap_static_rows_after_if_accepted":11,"coverage_gap_conversation_local_before_approx":19,"coverage_gap_conversation_local_after_if_accepted_approx":24,"still_need_to_30_conversation_local_approx":6,"loop_contribution_label":"canonical_archetype_rule_candidate"}
{"source_row_type":"residual_contribution","schema_version":"v12","round":"R5","loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":5,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["processed_food_reorder_bridge_too_late","seafood_export_beta_without_inventory_margin_bridge","k_food_theme_spike_full_4b_false_positive","smallcap_confectionery_brand_buzz_high_MAE","protein_food_label_stage3_false_positive"],"new_axis_proposed":["C20_SELLTHROUGH_REORDER_OPM_REVISION_BRIDGE_REQUIRED","C20_FOOD_EXPORT_LABEL_WITHOUT_WORKING_CAPITAL_BRIDGE_STAGE3_CAP","C20_SMALLCAP_BRAND_BUZZ_LOCAL_4B_CAP","C20_POST_PEAK_HIGH_MAE_INVENTORY_AR_GUARD","C20_PROTEIN_FOOD_LABEL_REQUIRES_OPM_REORDER_CONFIRMATION"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"do_not_propose_new_weight_delta":false}
```

## 6. Interpretation

Positive/mixed cases show that C20 should preserve upside when repeat demand and margin confirmation appear. Counterexamples show the opposite edge: global distribution labels can create a local burst but often reverse if sell-through, reorder, OPM, and working-capital evidence do not follow.

The residual error is therefore not a generic Stage2/4B issue. It is C20-specific: consumer food/beauty brands need a reorder economics bridge. Without that bridge, the profile should cap Stage3 and reroute price-only strength to local 4B watch.

## 7. Shadow rule candidate

```yaml
new_axis_proposed:
  - C20_SELLTHROUGH_REORDER_OPM_REVISION_BRIDGE_REQUIRED
  - C20_FOOD_EXPORT_LABEL_WITHOUT_WORKING_CAPITAL_BRIDGE_STAGE3_CAP
  - C20_SMALLCAP_BRAND_BUZZ_LOCAL_4B_CAP
  - C20_POST_PEAK_HIGH_MAE_INVENTORY_AR_GUARD
  - C20_PROTEIN_FOOD_LABEL_REQUIRES_OPM_REORDER_CONFIRMATION
existing_axis_strengthened:
  - stage2_required_bridge
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - local_4b_watch_guard
  - high_MAE_guardrail
existing_axis_weakened: []
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: false
```

## 8. Deferred Coding Agent Handoff Prompt

Do not execute this prompt now.

```text
You are a later coding agent operating on Songdaiki/stock_agent.
Read this MD together with other accepted v12 residual research files.
Do not assume every row is promotion-ready. First batch-reverify rows marked batch_reverification_required=true against Songdaiki/stock-web or the locally mirrored atlas.
If accepted, compress the proposed axis into C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION archetype-specific shadow rules:
1. require sell-through/reorder + OPM/revision/working-capital bridge for Stage3;
2. cap food/export/brand labels without cash bridge;
3. route price-only K-food/K-beauty spikes to local 4B watch;
4. attach high-MAE guard when peak is not durable.
Do not change production scoring without aggregate validation across the full v12 corpus.
```

## 9. Research state after this run

```text
completed_round = R5
completed_loop = 117
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_final_pass_to_30, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_fourth_pass_to_30, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_second_pass_to_30, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_fourth_pass_to_30, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE
```
