# E2R Stock-Web v12 Residual Research — R5 Loop 84 / L5 / C18

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R5
loop: 84
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE_VS_THEME_SPIKE_AND_DOMESTIC_CHANNEL_STALL
sector: consumer / brand / distribution / export-channel reorder
output_file: e2r_stock_web_v12_residual_round_R5_loop_84_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R4 loop 84`.

```text
scheduled_round = R5
scheduled_loop = 84
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
```

R5 is restricted to consumer / brand / distribution.  
C18 is selected because the No-Repeat ledger shows C18 has broad positive coverage but no explicit 4B/4C cases and still needs a clearer split between durable channel reorder and theme-only consumer export spikes.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"005180","company_name":"빙그레","profile_path":"atlas/symbol_profiles/005/005180.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7764,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1995-09-29","1996-09-25","1998-12-15"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"011150","company_name":"CJ씨푸드","profile_path":"atlas/symbol_profiles/011/011150.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7587,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2002-04-22"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"005610","company_name":"SPC삼립","profile_path":"atlas/symbol_profiles/005/005610.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7664,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1996-01-03","1997-05-27","1999-03-05","2002-11-25"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
For C18, the top-covered symbols are `001680`, `280360`, `UNKNOWN_SYMBOL`, `049770`, `271560`, and `003960`. This run avoids that repeated set and introduces three different symbols.

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced here:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"005180","trigger_type":"Stage2-Actionable-KFoodExportChannelReorder-Positive","entry_date":"2024-04-15","duplicate_status":"new C18 symbol/trigger/date combination"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"011150","trigger_type":"Stage2-FalsePositive-SeafoodExportThemeSpike-NoReorderBridge","entry_date":"2024-06-14","duplicate_status":"new C18 symbol/trigger/date combination"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"005610","trigger_type":"Stage2-FalsePositive-DomesticBakeryChannelSpike-NoReorderMarginBridge","entry_date":"2024-06-14","duplicate_status":"new C18 symbol/trigger/date combination"}
```

## 4. Research question

C18 should read “channel reorder” like a merchant reads inventory velocity: one excited order is not enough; the shelf has to empty and refill again. Export/channel headlines become E2R-relevant only when reorder, sell-through, margin, and repeat distribution evidence appear together.

Residual question:

```text
Can C18 distinguish:
1. export/channel reorder with sustained sell-through and margin proxy,
2. K-food/seafood theme spike with no repeat reorder bridge,
3. domestic consumer-channel spike with no margin/reorder confirmation?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C18_R5L84_005180_BINGGRAE_EXPORT_REORDER_BRIDGE","symbol":"005180","company_name":"빙그레","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_CHANNEL_REORDER_WITH_MARGIN_PROXY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-KFoodExportChannelReorder-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_reorder_bridge_required","price_source":"Songdaiki/stock-web","notes":"Export/channel reorder proxy and price path aligned; supports Stage2/Yellow, not Green without exact channel and margin evidence."}
{"row_type":"case","case_id":"C18_R5L84_011150_CJSEAFOOD_EXPORT_THEME_SPIKE","symbol":"011150","company_name":"CJ씨푸드","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"SEAFOOD_EXPORT_THEME_SPIKE_WITHOUT_REPEAT_REORDER_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SeafoodExportThemeSpike-NoReorderBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE_after_theme_peak","current_profile_verdict":"current_profile_false_positive_if_theme_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Theme spike gave a near-term local peak but no durable reorder/margin bridge; later high MAE argues for C18 local 4B watch guard."}
{"row_type":"case","case_id":"C18_R5L84_005610_SPC_CHANNEL_SPIKE_NO_MARGIN_BRIDGE","symbol":"005610","company_name":"SPC삼립","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"DOMESTIC_CHANNEL_STOCKING_SPIKE_NO_MARGIN_REORDER_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DomesticBakeryChannelSpike-NoReorderMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_channel_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Channel/food-consumption spike lacked repeat order and margin bridge; high MAE shows C18 should not treat domestic channel rebound as export reorder by default."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 005180 빙그레 — K-food export/channel reorder bridge positive

Entry row: `2024-04-15 c=61900`.  
Forward path: same-day low `57800`, 30D high `2024-05-22 h=97700`, and 90D/180D high `2024-06-11 h=118400`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L84_C18_005180_20240415_STAGE2_KFOOD_EXPORT_REORDER_BRIDGE","case_id":"C18_R5L84_005180_BINGGRAE_EXPORT_REORDER_BRIDGE","symbol":"005180","company_name":"빙그레","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_CHANNEL_REORDER_WITH_MARGIN_PROXY","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-KFoodExportChannelReorder-Positive","trigger_date":"2024-04-15","entry_date":"2024-04-15","entry_price":61900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_export_channel_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; K-food export/channel reorder thesis treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["export_channel_reorder_proxy","repeat_sellthrough_proxy","relative_strength_turn"],"stage3_evidence_fields":["margin_bridge_proxy","multi_quarter_reorder_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv","profile_path":"atlas/symbol_profiles/005/005180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":57.84,"MFE_90D_pct":91.28,"MFE_180D_pct":91.28,"MAE_30D_pct":-6.62,"MAE_90D_pct":-6.62,"MAE_180D_pct":-6.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":118400.0,"max_drawdown_low_date":"2024-04-15","max_drawdown_low":57800.0,"drawdown_after_peak_pct":-48.31,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_reorder_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"005180_2024-04-15_61900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C18 can work when channel reorder and sell-through proxies support the price path. Still, Green should require exact export/channel evidence and margin durability."}
```

### 6.2 011150 CJ씨푸드 — seafood/K-food theme spike without reorder bridge

Entry row: `2024-06-14 c=6320`.  
Forward path: only `2024-06-17 h=6490` local upside, then high-MAE decline to `2024-07-22 l=4180` and `2024-12-09 l=2530`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L84_C18_011150_20240614_STAGE2_FALSE_POSITIVE_SEAFOOD_EXPORT_THEME","case_id":"C18_R5L84_011150_CJSEAFOOD_EXPORT_THEME_SPIKE","symbol":"011150","company_name":"CJ씨푸드","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"SEAFOOD_EXPORT_THEME_SPIKE_WITHOUT_REPEAT_REORDER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-SeafoodExportThemeSpike-NoReorderBridge","trigger_date":"2024-06-14","entry_date":"2024-06-14","entry_price":6320.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_K_food_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; seafood/K-food export theme spike treated as insufficient without repeat reorder, sell-through, and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["theme_relative_strength","export_keyword_proxy"],"stage3_evidence_fields":["repeat_reorder_missing","sellthrough_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011150/2024.csv","profile_path":"atlas/symbol_profiles/011/011150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.69,"MFE_90D_pct":2.69,"MFE_180D_pct":2.69,"MAE_30D_pct":-33.86,"MAE_90D_pct":-52.06,"MAE_180D_pct":-59.97,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-17","peak_price":6490.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":2530.0,"drawdown_after_peak_pct":-61.02,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_peak_without_reorder_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_theme_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"011150_2024-06-14_6320","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C18 needs a local repeat-reorder guard. Seafood/K-food theme spikes can create a local peak but collapse without channel sell-through and margin evidence."}
```

### 6.3 005610 SPC삼립 — domestic channel spike without reorder/margin bridge

Entry row: `2024-06-14 c=65500`.  
Forward path: same-day high `66700`, then low `2024-11-13 l=43350`; the price path is a channel-stocking false positive, not export-channel reorder.

```jsonl
{"row_type":"trigger","trigger_id":"R5L84_C18_005610_20240614_STAGE2_FALSE_POSITIVE_DOMESTIC_CHANNEL_SPIKE","case_id":"C18_R5L84_005610_SPC_CHANNEL_SPIKE_NO_MARGIN_BRIDGE","symbol":"005610","company_name":"SPC삼립","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"DOMESTIC_CHANNEL_STOCKING_SPIKE_NO_MARGIN_REORDER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-DomesticBakeryChannelSpike-NoReorderMarginBridge","trigger_date":"2024-06-14","entry_date":"2024-06-14","entry_price":65500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_domestic_channel_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; domestic food-channel stocking rebound treated as insufficient for C18 export-channel reorder without repeat sell-through and margin bridge","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["channel_restocking_proxy","relative_strength_rebound"],"stage3_evidence_fields":["export_reorder_missing","repeat_sellthrough_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005610/2024.csv","profile_path":"atlas/symbol_profiles/005/005610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.83,"MFE_90D_pct":1.83,"MFE_180D_pct":1.83,"MAE_30D_pct":-16.49,"MAE_90D_pct":-25.42,"MAE_180D_pct":-33.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":66700.0,"max_drawdown_low_date":"2024-11-13","max_drawdown_low":43350.0,"drawdown_after_peak_pct":-35.01,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"domestic_channel_peak_without_export_reorder_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_channel_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"005610_2024-06-14_65500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C18 should not count domestic channel rebound as export-channel reorder without repeat sell-through and margin bridge. Low MFE/high MAE path supports local guardrail."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C18_R5L84_005180_BINGGRAE_EXPORT_REORDER_BRIDGE","trigger_id":"R5L84_C18_005180_20240415_STAGE2_KFOOD_EXPORT_REORDER_BRIDGE","symbol":"005180","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C18 requires repeat reorder/sell-through bridge","raw_component_scores_before":{"export_channel_score":15,"repeat_sellthrough_score":13,"margin_bridge_score":10,"revision_score":9,"relative_strength_score":15,"brand_quality_score":12,"inventory_risk_score":-3,"valuation_repricing_score":10,"execution_risk_score":-3,"information_confidence":5},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable/Stage3-Yellow-Watch","raw_component_scores_after":{"export_channel_score":18,"repeat_sellthrough_score":16,"margin_bridge_score":12,"revision_score":11,"relative_strength_score":16,"brand_quality_score":13,"inventory_risk_score":-2,"valuation_repricing_score":11,"execution_risk_score":-2,"information_confidence":6},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Export/channel reorder bridge and shallow MAE support Yellow-watch; exact channel and margin evidence still block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C18_R5L84_011150_CJSEAFOOD_EXPORT_THEME_SPIKE","trigger_id":"R5L84_C18_011150_20240614_STAGE2_FALSE_POSITIVE_SEAFOOD_EXPORT_THEME","symbol":"011150","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_scope":"current_default_proxy","profile_hypothesis":"theme spike without reorder bridge should be blocked","raw_component_scores_before":{"export_channel_score":6,"repeat_sellthrough_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":15,"brand_quality_score":4,"inventory_risk_score":-8,"valuation_repricing_score":8,"execution_risk_score":-12,"information_confidence":3},"weighted_score_before":43,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_channel_score":3,"repeat_sellthrough_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":7,"brand_quality_score":3,"inventory_risk_score":-12,"valuation_repricing_score":3,"execution_risk_score":-18,"information_confidence":2},"weighted_score_after":18,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Low MFE and deep MAE convert seafood/K-food theme spike into reorder-bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C18_R5L84_005610_SPC_CHANNEL_SPIKE_NO_MARGIN_BRIDGE","trigger_id":"R5L84_C18_005610_20240614_STAGE2_FALSE_POSITIVE_DOMESTIC_CHANNEL_SPIKE","symbol":"005610","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_scope":"current_default_proxy","profile_hypothesis":"domestic channel spike without export/reorder/margin bridge should stay Watch or blocked","raw_component_scores_before":{"export_channel_score":3,"repeat_sellthrough_score":4,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":10,"brand_quality_score":7,"inventory_risk_score":-6,"valuation_repricing_score":6,"execution_risk_score":-8,"information_confidence":4},"weighted_score_before":44,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_channel_score":1,"repeat_sellthrough_score":1,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":5,"brand_quality_score":6,"inventory_risk_score":-10,"valuation_repricing_score":3,"execution_risk_score":-14,"information_confidence":3},"weighted_score_after":21,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Domestic channel restocking is not C18 export-channel reorder unless repeat sell-through and margin bridge are verified."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R5L84_C18_P0_CURRENT","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C18 still needs explicit repeat-reorder/sell-through bridge distinction","eligible_trigger_count":3,"avg_MFE_90D_pct":31.93,"avg_MAE_90D_pct":-28.03,"avg_MFE_180D_pct":31.93,"avg_MAE_180D_pct":-33.47,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C18_reorder_guard"}
{"row_type":"profile_comparison","comparison_id":"R5L84_C18_P1_SECTOR_SPECIFIC","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P1_L5_reorder_sellthrough_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L5 consumer export/channel signals need repeat sell-through and margin bridge before Stage2-Actionable","changed_axes":["repeat_reorder_required","sellthrough_bridge_required","margin_bridge_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_export_reorder_or_repeat_sellthrough_proxy"},"eligible_trigger_count":3,"avg_MFE_90D_pct":31.93,"avg_MAE_90D_pct":-28.03,"avg_MFE_180D_pct":31.93,"avg_MAE_180D_pct":-33.47,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R5L84_C18_P2_CANONICAL","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P2_C18_repeat_reorder_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C18 should reward repeat reorder, not theme spikes or domestic channel restocking alone","changed_axes":["C18_repeat_reorder_required","C18_theme_spike_penalty","C18_domestic_channel_not_export_guard"],"changed_thresholds":{"stage2_yellow_gate":"repeat_reorder_or_sellthrough_bridge_required"},"eligible_trigger_count":3,"avg_MFE_90D_pct":31.93,"avg_MAE_90D_pct":-28.03,"avg_MFE_180D_pct":31.93,"avg_MAE_180D_pct":-33.47,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R5L84_C18_P3_COUNTEREXAMPLE_GUARD","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P3_C18_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-20 while reorder/sell-through bridge is missing, block Yellow/Green","changed_axes":["C18_high_MAE_guardrail","C18_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_20"},"eligible_trigger_count":3,"avg_MFE_90D_pct":31.93,"avg_MAE_90D_pct":-28.03,"avg_MFE_180D_pct":31.93,"avg_MAE_180D_pct":-33.47,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"C18_K_FOOD_EXPORT_CHANNEL_REORDER_VS_THEME_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":31.93,"avg_MAE90_pct":-28.03,"avg_MFE180_pct":31.93,"avg_MAE180_pct":-33.47,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C18 needs bridge discipline. 005180 shows a real export/channel reorder path, while 011150 and 005610 show theme or domestic channel spikes that fail without repeat reorder and margin bridge."}
{"row_type":"stage_transition_summary","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"005180","trigger_type":"Stage2-Actionable-KFoodExportChannelReorder-Positive","entry_date":"2024-04-15","stage2_to_90D_outcome":"good_stage2_high_MFE","stage2_to_180D_outcome":"positive_re_rating_path","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when repeat export/channel reorder and sell-through bridge exists; Green requires exact URL and margin durability."}
{"row_type":"stage_transition_summary","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"011150","trigger_type":"Stage2-FalsePositive-SeafoodExportThemeSpike-NoReorderBridge","entry_date":"2024-06-14","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"failed_rerating_theme_spike","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"K-food/seafood theme spike without repeat reorder should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"005610","trigger_type":"Stage2-FalsePositive-DomesticBakeryChannelSpike-NoReorderMarginBridge","entry_date":"2024-06-14","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"failed_rerating_domestic_channel_spike","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Domestic channel rebound should not be upgraded to export-channel reorder without repeat sell-through and margin bridge."}
{"row_type":"residual_contribution","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","residual_type":"consumer_export_channel_theme_spike_overcredit_without_reorder_bridge","contribution":"Adds two C18 high-MAE counterexamples against one bridge-positive case and introduces explicit 4B-watch rows for C18, which previously had no 4B/4C cases in the ledger.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_CHANNEL_REORDER_BRIDGE_VS_THEME_SPIKE_AND_DOMESTIC_CHANNEL_STALL","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C18 now has local 4B-watch and high-MAE theme-spike counterexamples; next R5 loops should exact-URL repair repeat sell-through and export channel evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","axis":"C18_repeat_reorder_sellthrough_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"005180 worked with export/channel reorder proxy; 011150 and 005610 failed without repeat reorder/sell-through bridge."}
{"row_type":"shadow_weight","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","axis":"C18_theme_spike_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"K-food/seafood and domestic channel price spikes showed low MFE and high MAE without non-price reorder evidence."}
{"row_type":"shadow_weight","round":"R5","loop":"84","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","axis":"C18_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and MAE90<=-20 while reorder/sell-through bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
residual_error_types_found:
  - export_channel_theme_spike_overcredit
  - seafood_K_food_theme_local_peak_high_MAE
  - domestic_channel_restocking_not_export_reorder
new_axis_proposed:
  - C18_repeat_reorder_sellthrough_bridge_required_shadow_only
  - C18_theme_spike_local_4B_watch_guard_shadow_only
  - C18_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C18
  - full_4b_requires_non_price_evidence within C18
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 12. Data-quality caveat

All selected triggers use actual Stock-Web tradable raw OHLC rows and clean selected forward windows.  
The non-price evidence layer remains source-name/proxy level.

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
3. Confirm R5 / L5 / C18 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. If aggregate support remains stable after exact evidence URL repair, consider C18-scoped safe patch candidates:
   - C18_repeat_reorder_sellthrough_bridge_required
   - C18_theme_spike_local_4B_watch_guard
   - C18_high_MAE_guardrail
6. Do not loosen Stage3-Green.
7. Do not use future MFE/MAE in runtime scoring.
8. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R5
completed_loop = 84
next_round = R6
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C18_CONSUMER_EXPORT_CHANNEL_REORDER.
```
