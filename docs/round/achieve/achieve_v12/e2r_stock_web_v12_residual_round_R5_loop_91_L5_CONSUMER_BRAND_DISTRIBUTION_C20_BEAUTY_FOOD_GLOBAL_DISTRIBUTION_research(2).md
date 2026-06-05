# E2R Stock-Web v12 Residual Research — R5 Loop 91 / L5 / C20

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R5
loop: 91
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_MANUFACTURING_EXPORT_CHANNEL_BRIDGE_VS_LEGACY_BEAUTY_FOOD_GLOBAL_VOCABULARY_DECAY
sector: consumer / beauty / food / global distribution / export channel / margin / reorder
output_file: e2r_stock_web_v12_residual_round_R5_loop_91_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R4 loop 91`.

```text
scheduled_round = R5
scheduled_loop = 91
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```

R5 is restricted to consumer / brand / distribution.  
C20 is selected because the recent R5 sequence rotated through C18 → C19 → C20, and R5 loop90 used C19.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
rows = 19
symbols = 11
good/bad Stage2 = 8/2
4B/4C = 4/0
top-covered = 226320, 161890, 192820, 214420, 241710, 439090
```

This loop avoids the C20 top-covered list and recent R5 loop symbols:

```text
R5 loop86 C18: 003230, 005610, 007310
R5 loop87 C19: 069960, 008770, 031430
R5 loop88 C20: 352480, 237880, 018250
R5 loop89 C18: 005180, 101530, 248170
R5 loop90 C19: 090430, 383220, 020000
```

Candidate hygiene note:

```text
During this execution path, R2/C07, R3/C13 and R4/C15 candidate rows were touched in surrounding tool calls.
Those rows are not used in this R5/C20 output.
```

Selected symbols:

```text
003350, 051900, 004370
```

The selected pocket is:

```text
K-beauty manufacturing / export-channel / reorder-margin bridge
vs
legacy large beauty brand global-channel vocabulary without fresh sell-through and margin bridge
vs
food global distribution vocabulary after the move without fresh SKU/reorder and margin-cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"003350","company_name":"한국화장품제조","profile_path":"atlas/symbol_profiles/003/003350.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7736,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["1999-04-26","2010-06-01"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"051900","company_name":"LG생활건강","profile_path":"atlas/symbol_profiles/051/051900.json","first_date":"2001-04-25","last_date":"2026-02-20","trading_day_count":6125,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"004370","company_name":"농심","profile_path":"atlas/symbol_profiles/004/004370.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7742,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1997-05-08","1997-07-21","2000-07-28","2003-07-18"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"003350","trigger_type":"Stage2-Actionable-KBeautyManufacturingExportChannelBridge-Positive","entry_date":"2024-04-15","duplicate_status":"new C20 symbol/trigger/date combination outside top-covered and previous R5 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"051900","trigger_type":"Stage2-FalsePositive-LegacyBeautyGlobalChannelVocabularyNoFreshSellthroughMarginBridge","entry_date":"2024-04-30","duplicate_status":"new C20 symbol/trigger/date combination outside top-covered and previous R5 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"004370","trigger_type":"Stage2-FalsePositive-FoodGlobalDistributionPostMoveNoFreshReorderMarginBridge","entry_date":"2024-06-14","duplicate_status":"new C20 symbol/trigger/date combination outside top-covered and previous R5 loop symbols"}
```

## 4. Research question

C20 is not “뷰티·식품 글로벌 이야기가 있다.”  
The useful signal must prove the channel-to-margin chain:

```text
global channel expansion
export sell-through
customer reorder
SKU expansion or product mix
ODM / manufacturing leverage
distribution partner quality
gross-margin repair
working-capital discipline
cash conversion
```

A global distribution headline without this bridge is a product placed on a foreign shelf with no repeat order. It looks exported, but the business only changes when the customer returns, the SKU mix improves, and cash comes back through the channel.

Residual question:

```text
Can C20 distinguish:
1. K-beauty manufacturing/export-channel bridge with very high MFE and low entry MAE,
2. legacy beauty global-channel vocabulary where entry comes after the first move and no fresh sell-through/margin bridge is repaired,
3. food global distribution vocabulary where post-move entry has low MFE and deep later MAE without fresh reorder and cash bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C20_R5L91_003350_KBEAUTY_MANUFACTURING_EXPORT","symbol":"003350","company_name":"한국화장품제조","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_MANUFACTURING_EXPORT_CHANNEL_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-KBeautyManufacturingExportChannelBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_extreme_MFE90_and_MFE180_low_MAE_export_channel_bridge","current_profile_verdict":"current_profile_correct_if_export_channel_reorder_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"K-beauty manufacturing/export-channel bridge proxy produced extreme 90D/180D MFE with shallow MAE. Green still requires exact sell-through, reorder, SKU/mix, margin and cash evidence."}
{"row_type":"case","case_id":"C20_R5L91_051900_LG_HNH_LEGACY_BEAUTY_CHANNEL","symbol":"051900","company_name":"LG생활건강","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LEGACY_BEAUTY_GLOBAL_CHANNEL_VOCABULARY_WITHOUT_FRESH_SELLTHROUGH_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LegacyBeautyGlobalChannelVocabularyNoFreshSellthroughMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub_Yellow_MFE_deep_MAE_no_fresh_channel_bridge","current_profile_verdict":"current_profile_false_positive_if_legacy_beauty_channel_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Legacy beauty global-channel vocabulary had sub-Yellow MFE from the selected post-rebound entry and later deep MAE without fresh sell-through, reorder, gross-margin and cash bridge."}
{"row_type":"case","case_id":"C20_R5L91_004370_NONGSHIM_FOOD_GLOBAL_DISTRIBUTION_POSTMOVE","symbol":"004370","company_name":"농심","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"FOOD_GLOBAL_DISTRIBUTION_POSTMOVE_WITHOUT_FRESH_REORDER_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-FoodGlobalDistributionPostMoveNoFreshReorderMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_reorder_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_food_global_distribution_postmove_overcredited","price_source":"Songdaiki/stock-web","notes":"Food global distribution vocabulary after the first move had low MFE and deep later MAE without fresh SKU/reorder, margin and cash conversion bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 003350 한국화장품제조 — K-beauty manufacturing / export-channel bridge

Entry row: `2024-04-15 c=25500`.  
Observed path: early low `2024-04-16 l=24600`, 90D peak `2024-07-11 h=72800`, and full-window peak `2024-10-18 h=89400`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L91_C20_003350_20240415_STAGE2_KBEAUTY_EXPORT_MANUFACTURING","case_id":"C20_R5L91_003350_KBEAUTY_MANUFACTURING_EXPORT","symbol":"003350","company_name":"한국화장품제조","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_MANUFACTURING_EXPORT_CHANNEL_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-KBeautyManufacturingExportChannelBridge-Positive","trigger_date":"2024-04-15","entry_date":"2024-04-15","entry_price":25500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_K_beauty_manufacturing_export_channel_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; K-beauty manufacturing, export channel, reorder and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["K_beauty_export_channel_proxy","manufacturing_leverage_proxy","reorder_SKU_mix_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_export_channel_source_pending","customer_reorder_source_pending","SKU_mix_or_ODM_margin_source_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003350/2024.csv","profile_path":"atlas/symbol_profiles/003/003350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":121.96,"MFE_90D_pct":185.49,"MFE_180D_pct":250.59,"MAE_30D_pct":-3.53,"MAE_90D_pct":-3.53,"MAE_180D_pct":-3.53,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-18","peak_price":89400.0,"max_drawdown_low_date":"2024-04-16","max_drawdown_low":24600.0,"drawdown_after_peak_pct":-52.80,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.81,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_export_sellthrough_reorder_SKU_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_extreme_MFE90_and_MFE180_low_MAE_export_channel_bridge","current_profile_verdict":"current_profile_correct_if_export_channel_reorder_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"003350_2024-04-15_25500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C20 can allow Stage2/Yellow when beauty strength is tied to global channel sell-through, reorder, SKU mix, manufacturing/ODM margin and cash conversion. Green still requires exact source-grade evidence."}
```

### 6.2 051900 LG생활건강 — legacy beauty global-channel vocabulary without fresh bridge

Entry row: `2024-04-30 c=420000`, after the first global-channel/beauty rebound.  
Observed path: peak `2024-05-23 h=480000`, then drawdown to `2024-12-27 l=304000`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L91_C20_051900_20240430_STAGE2_FALSE_POSITIVE_LEGACY_BEAUTY_CHANNEL","case_id":"C20_R5L91_051900_LG_HNH_LEGACY_BEAUTY_CHANNEL","symbol":"051900","company_name":"LG생활건강","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LEGACY_BEAUTY_GLOBAL_CHANNEL_VOCABULARY_WITHOUT_FRESH_SELLTHROUGH_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-LegacyBeautyGlobalChannelVocabularyNoFreshSellthroughMarginBridge","trigger_date":"2024-04-30","entry_date":"2024-04-30","entry_price":420000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_legacy_beauty_global_channel_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; large beauty/global-channel vocabulary treated as insufficient without fresh sell-through, reorder, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["legacy_beauty_brand_vocabulary","global_channel_rebound","relative_strength_after_rebound"],"stage3_evidence_fields":["fresh_sellthrough_missing","customer_reorder_missing","gross_margin_repair_missing","cash_conversion_missing"],"stage4b_evidence_fields":["sub_Yellow_MFE","channel_margin_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv","profile_path":"atlas/symbol_profiles/051/051900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.29,"MFE_90D_pct":14.29,"MFE_180D_pct":14.29,"MAE_30D_pct":-0.95,"MAE_90D_pct":-19.05,"MAE_180D_pct":-27.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-23","peak_price":480000.0,"max_drawdown_low_date":"2024-12-27","max_drawdown_low":304000.0,"drawdown_after_peak_pct":-36.67,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"legacy_beauty_global_channel_vocabulary_without_fresh_sellthrough_reorder_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["sub_Yellow_MFE","channel_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub_Yellow_MFE_deep_MAE_no_fresh_channel_bridge","current_profile_verdict":"current_profile_false_positive_if_legacy_beauty_channel_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"051900_2024-04-30_420000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C20 should not promote legacy beauty/global-channel rebound unless fresh sell-through, reorder, margin and cash evidence are repaired. Sub-Yellow MFE and deep 180D MAE require Watch/4B routing."}
```

### 6.3 004370 농심 — food global distribution post-move without fresh reorder/margin bridge

Entry row: `2024-06-14 c=548000`, after the first food-export/global-distribution run.  
Observed path: high `2024-06-17 h=589000`, then drawdown to `2024-11-15 l=317000`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L91_C20_004370_20240614_STAGE2_FALSE_POSITIVE_FOOD_GLOBAL_POSTMOVE","case_id":"C20_R5L91_004370_NONGSHIM_FOOD_GLOBAL_DISTRIBUTION_POSTMOVE","symbol":"004370","company_name":"농심","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"FOOD_GLOBAL_DISTRIBUTION_POSTMOVE_WITHOUT_FRESH_REORDER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;post_move_entry_guard","trigger_type":"Stage2-FalsePositive-FoodGlobalDistributionPostMoveNoFreshReorderMarginBridge","trigger_date":"2024-06-14","entry_date":"2024-06-14","entry_price":548000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_food_global_distribution_postmove_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; food export/global distribution vocabulary treated as insufficient after the first move without fresh SKU/reorder, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["food_global_distribution_vocabulary","post_move_relative_strength","export_SKU_keyword"],"stage3_evidence_fields":["fresh_reorder_missing","SKU_mix_bridge_missing","gross_margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["low_MFE_watch","post_move_entry_watch","reorder_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004370/2024.csv","profile_path":"atlas/symbol_profiles/004/004370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.48,"MFE_90D_pct":7.48,"MFE_180D_pct":7.48,"MAE_30D_pct":-18.07,"MAE_90D_pct":-30.57,"MAE_180D_pct":-42.15,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-17","peak_price":589000.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":317000.0,"drawdown_after_peak_pct":-46.18,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"food_global_distribution_postmove_without_fresh_reorder_SKU_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","post_move_entry_watch","reorder_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_reorder_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_food_global_distribution_postmove_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"004370_2024-06-14_548000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C20 should not count food export/global distribution vocabulary as fresh reorder evidence after the first move. Fresh SKU/reorder, margin and cash conversion must be exact-repaired before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_R5L91_003350_KBEAUTY_MANUFACTURING_EXPORT","trigger_id":"R5L91_C20_003350_20240415_STAGE2_KBEAUTY_EXPORT_MANUFACTURING","symbol":"003350","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C20 requires global channel sell-through, reorder, SKU/product mix, manufacturing/ODM leverage, margin and cash bridge rather than beauty/food vocabulary alone","raw_component_scores_before":{"global_channel_score":13,"export_sellthrough_score":12,"customer_reorder_score":12,"SKU_product_mix_score":11,"manufacturing_leverage_score":13,"gross_margin_score":11,"cash_conversion_score":7,"relative_strength_score":16,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"global_channel_score":16,"export_sellthrough_score":15,"customer_reorder_score":15,"SKU_product_mix_score":13,"manufacturing_leverage_score":16,"gross_margin_score":13,"cash_conversion_score":9,"relative_strength_score":17,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":90,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"K-beauty manufacturing/export-channel bridge plus extreme MFE supports Yellow/Green-candidate watch; exact sell-through/reorder/margin evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_R5L91_051900_LG_HNH_LEGACY_BEAUTY_CHANNEL","trigger_id":"R5L91_C20_051900_20240430_STAGE2_FALSE_POSITIVE_LEGACY_BEAUTY_CHANNEL","symbol":"051900","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_scope":"current_default_proxy","profile_hypothesis":"legacy beauty/global-channel vocabulary without fresh sell-through and reorder bridge should be blocked","raw_component_scores_before":{"global_channel_score":3,"export_sellthrough_score":1,"customer_reorder_score":0,"SKU_product_mix_score":1,"manufacturing_leverage_score":0,"gross_margin_score":0,"cash_conversion_score":0,"relative_strength_score":8,"valuation_repricing_score":3,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"global_channel_score":1,"export_sellthrough_score":0,"customer_reorder_score":0,"SKU_product_mix_score":0,"manufacturing_leverage_score":0,"gross_margin_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-Yellow MFE and deep MAE convert legacy beauty channel vocabulary into missing sell-through/reorder bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_R5L91_004370_NONGSHIM_FOOD_GLOBAL_DISTRIBUTION_POSTMOVE","trigger_id":"R5L91_C20_004370_20240614_STAGE2_FALSE_POSITIVE_FOOD_GLOBAL_POSTMOVE","symbol":"004370","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_scope":"current_default_proxy","profile_hypothesis":"food global distribution post-move without fresh reorder and margin bridge should remain Watch/4B","raw_component_scores_before":{"global_channel_score":4,"export_sellthrough_score":2,"customer_reorder_score":0,"SKU_product_mix_score":1,"manufacturing_leverage_score":0,"gross_margin_score":0,"cash_conversion_score":0,"relative_strength_score":9,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"global_channel_score":1,"export_sellthrough_score":0,"customer_reorder_score":0,"SKU_product_mix_score":0,"manufacturing_leverage_score":0,"gross_margin_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE require fresh reorder, SKU/mix, margin and cash evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R5L91_C20_P0_CURRENT","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C20 needs explicit global channel, sell-through, reorder, SKU mix, margin/cash and post-move entry taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":69.09,"avg_MAE90_pct":-17.72,"avg_MFE180_pct":90.79,"avg_MAE180_pct":-24.43,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.94,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C20_export_reorder_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R5L91_C20_P1_SECTOR_SPECIFIC","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_id":"P1_L5_beauty_food_global_channel_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L5 beauty/food global distribution signals need sell-through, customer reorder, SKU/product mix, margin or cash conversion before Stage2-Actionable","changed_axes":["global_sellthrough_required","reorder_SKU_margin_required","postmove_global_vocabulary_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_global_channel_sellthrough_reorder_SKU_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":69.09,"avg_MAE90_pct":-17.72,"avg_MFE180_pct":90.79,"avg_MAE180_pct":-24.43,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R5L91_C20_P2_CANONICAL","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_id":"P2_C20_export_reorder_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C20 should reward channel-to-reorder-to-margin mechanics, not beauty/food global vocabulary","changed_axes":["C20_export_reorder_SKU_margin_cash_bridge_required","C20_legacy_brand_food_postmove_local_4B_guard","C20_price_only_postmove_not_distribution_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"global_channel_or_sellthrough_plus_reorder_or_margin_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":69.09,"avg_MAE90_pct":-17.72,"avg_MFE180_pct":90.79,"avg_MAE180_pct":-24.43,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R5L91_C20_P3_COUNTEREXAMPLE_GUARD","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_id":"P3_C20_sub20_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If fresh sell-through/reorder/margin bridge is missing, MFE90<20 or MAE180<=-25 should block Yellow/Green and route to 4B-watch","changed_axes":["C20_sub20_MFE_guardrail","C20_deep_MAE_4B_guardrail","C20_postmove_entry_watch"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_20_or_MAE180_le_minus_25)"},"eligible_trigger_count":3,"avg_MFE90_pct":69.09,"avg_MAE90_pct":-17.72,"avg_MFE180_pct":90.79,"avg_MAE180_pct":-24.43,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"C20_KBEAUTY_EXPORT_POSITIVE_VS_LEGACY_BEAUTY_FOOD_POSTMOVE_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":69.09,"avg_MAE90_pct":-17.72,"avg_MFE180_pct":90.79,"avg_MAE180_pct":-24.43,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE180_le_minus25":0.67,"interpretation":"C20 needs bridge discipline. 한국화장품제조 shows K-beauty manufacturing/export-channel/reorder bridge can support Yellow/Green-candidate-watch, while LG생활건강 and 농심 show legacy beauty or food global distribution vocabulary should not be promoted after the move without fresh sell-through, reorder, SKU/mix, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"003350","trigger_type":"Stage2-Actionable-KBeautyManufacturingExportChannelBridge-Positive","entry_date":"2024-04-15","stage2_to_90D_outcome":"good_stage2_extreme_MFE90_low_MAE","stage2_to_180D_outcome":"positive_export_channel_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when beauty strength is tied to export sell-through, reorder, SKU/mix, margin and cash bridge; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"051900","trigger_type":"Stage2-FalsePositive-LegacyBeautyGlobalChannelVocabularyNoFreshSellthroughMarginBridge","entry_date":"2024-04-30","stage2_to_90D_outcome":"bad_stage2_sub_Yellow_MFE_bridge_missing","stage2_to_180D_outcome":"failed_legacy_beauty_global_channel_deep_MAE","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Legacy beauty channel vocabulary without fresh sell-through and margin/cash bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"004370","trigger_type":"Stage2-FalsePositive-FoodGlobalDistributionPostMoveNoFreshReorderMarginBridge","entry_date":"2024-06-14","stage2_to_90D_outcome":"bad_stage2_low_MFE_postmove_entry","stage2_to_180D_outcome":"failed_food_global_distribution_postmove_deep_MAE","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Food global distribution vocabulary after the first move requires fresh reorder/SKU/margin evidence; without it, stay Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","residual_type":"legacy_beauty_food_global_vocabulary_overcredit_without_fresh_sellthrough_reorder_margin_cash_bridge","contribution":"Adds two C20 4B counterexamples against one K-beauty manufacturing/export-channel positive, avoiding C20 top-covered and recent R5 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_MANUFACTURING_EXPORT_CHANNEL_BRIDGE_VS_LEGACY_BEAUTY_FOOD_GLOBAL_VOCABULARY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C20 now has non-top-symbol K-beauty manufacturing/export-channel positive and two legacy beauty/food post-move weak-bridge counterexamples; next R5 C20 loops should exact-URL repair global channel, sell-through, customer reorder, SKU mix, ODM/manufacturing leverage, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","axis":"C20_export_reorder_SKU_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"003350 worked when K-beauty manufacturing/export-channel proxy existed; 051900 and 004370 failed when global-channel or food-distribution vocabulary lacked fresh sell-through/reorder/margin evidence."}
{"row_type":"shadow_weight","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","axis":"C20_legacy_brand_food_postmove_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Legacy beauty and food global distribution rows showed sub-20 MFE90 and deep 180D MAE when fresh reorder/margin evidence was missing."}
{"row_type":"shadow_weight","round":"R5","loop":"91","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","axis":"C20_price_only_postmove_not_distribution_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"004370 shows a post-move entry should not be validated by prior global-distribution vocabulary unless fresh trigger-date reorder/SKU/margin evidence exists."}
```

## 11. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - legacy_beauty_global_channel_vocabulary_overcredit
  - food_global_distribution_postmove_overcredit
  - fresh_sellthrough_reorder_bridge_missing
  - SKU_margin_cash_bridge_missing
new_axis_proposed:
  - C20_export_reorder_SKU_margin_cash_bridge_required_shadow_only
  - C20_legacy_brand_food_postmove_local_4B_guard_shadow_only
  - C20_price_only_postmove_not_distribution_validation_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C20
  - full_4b_requires_non_price_evidence within C20
  - hard_4c_thesis_break_routes_to_4c within C20
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 12. Data-quality caveat

All selected triggers use Stock-Web tradable raw OHLC rows and clean selected 2024 entry windows.  
`003350` and `004370` have older corporate-action or name-transition candidates before 2024; `051900` has no corporate-action candidate in the profile.  
The selected 2024 windows are usable for price-path residual analysis.  
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
promotion should prefer hold / data-quality repair until exact URLs are added
```

## 13. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not execute this handoff during the research-writing session.

When a later batch implementation is requested:
1. Ingest this MD through run-v12-calibration.
2. Confirm all trigger rows validate with:
   - price_data_source=Songdaiki/stock-web
   - price_basis=tradable_raw
   - price_adjustment_status=raw_unadjusted_marcap
3. Confirm R5 / L5 / C20 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C20 top-covered symbols
   - previous R5 loop86 C18 symbols
   - previous R5 loop87 C19 symbols
   - previous R5 loop88 C20 symbols
   - previous R5 loop89 C18 symbols
   - previous R5 loop90 C19 symbols
6. Confirm accidentally touched R2/C07, R3/C13 and R4/C15 candidate rows are not ingested from this MD.
7. If aggregate support remains stable after exact evidence URL repair, consider C20-scoped safe patch candidates:
   - C20_export_reorder_SKU_margin_cash_bridge_required
   - C20_legacy_brand_food_postmove_local_4B_guard
   - C20_price_only_postmove_not_distribution_validation_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R5
completed_loop = 91
next_round = R6
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION.
```
