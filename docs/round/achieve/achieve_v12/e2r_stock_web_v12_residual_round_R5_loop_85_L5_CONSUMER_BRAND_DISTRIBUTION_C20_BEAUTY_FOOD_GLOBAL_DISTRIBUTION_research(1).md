# E2R Stock-Web v12 Residual Research — R5 Loop 85 / L5 / C20

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R5
loop: 85
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_BRIDGE_VS_CHINA_REOPENING_THEME_SPIKE
sector: consumer / brand / distribution / beauty-food global distribution
output_file: e2r_stock_web_v12_residual_round_R5_loop_85_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R4 loop 85`.

```text
scheduled_round = R5
scheduled_loop = 85
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```

R5 is restricted to consumer / brand / distribution.  
C20 is selected because the previous R5 loop used C18, while C20 still needs a cleaner split between true global distribution / sell-through bridge and broad beauty-China reopening or theme-beta spikes.

The selected symbols avoid the C20 top-covered list in the No-Repeat Index:

```text
226320, 161890, 192820, 214420, 241710, 439090
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"018290","company_name":"브이티","profile_path":"atlas/symbol_profiles/018/018290.json","first_date":"1996-07-03","last_date":"2026-02-20","trading_day_count":6972,"corporate_action_candidate_count":12,"corporate_action_candidate_dates":["1996-12-12","1999-03-16","1999-09-29","1999-11-24","1999-12-13","2006-05-17","2007-12-21","2016-01-08","2016-01-15","2016-03-23","2016-09-13","2019-11-08"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"051900","company_name":"LG생활건강","profile_path":"atlas/symbol_profiles/051/051900.json","first_date":"2001-04-25","last_date":"2026-02-20","trading_day_count":6125,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"090430","company_name":"아모레퍼시픽","profile_path":"atlas/symbol_profiles/090/090430.json","first_date":"2006-06-29","last_date":"2026-02-20","trading_day_count":4834,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2015-05-08"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"018290","trigger_type":"Stage2-Actionable-KBeautyGlobalSellthroughBridge-Positive","entry_date":"2024-03-21","duplicate_status":"new C20 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"051900","trigger_type":"Stage2-FalsePositive-BeautyChinaReopeningRebound-NoGlobalSellthroughBridge","entry_date":"2024-05-10","duplicate_status":"new C20 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"090430","trigger_type":"Stage2-FalsePositive-BeautyLargecapChannelSpike-NoMarginReorderBridge","entry_date":"2024-05-31","duplicate_status":"new C20 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C20 should not read every cosmetics/food rebound as global distribution power. The real bridge is repeat sell-through, channel reorder, overseas SKU expansion, distributor quality, margin leverage, inventory discipline, and revision quality. A reopening or theme-beta rally without those gears is just shelf traffic; it is not proof the shelf keeps emptying and refilling.

Residual question:

```text
Can C20 distinguish:
1. K-beauty global sell-through/distribution bridge with large sustained MFE,
2. legacy beauty-China rebound without visible global sell-through and margin bridge,
3. large-cap beauty channel spike where price peaks before reorder/margin durability appears?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C20_R5L85_018290_VT_KBEAUTY_GLOBAL_SELLTHROUGH","symbol":"018290","company_name":"브이티","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-KBeautyGlobalSellthroughBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_shallow_MAE","current_profile_verdict":"current_profile_correct_if_sellthrough_distribution_bridge_required","price_source":"Songdaiki/stock-web","notes":"K-beauty/global distribution proxy produced large MFE with shallow initial MAE. Supports Stage2/Yellow; Green still requires exact channel/reorder/margin evidence."}
{"row_type":"case","case_id":"C20_R5L85_051900_LGHNH_REOPENING_REBOUND_NO_BRIDGE","symbol":"051900","company_name":"LG생활건강","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LEGACY_BEAUTY_CHINA_REOPENING_REBOUND_WITHOUT_GLOBAL_SELLTHROUGH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-BeautyChinaReopeningRebound-NoGlobalSellthroughBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_reopening_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"Beauty-China reopening rebound had tiny MFE and high MAE when global sell-through and margin recovery failed to confirm."}
{"row_type":"case","case_id":"C20_R5L85_090430_AMOREPACIFIC_CHANNEL_SPIKE_NO_MARGIN_REORDER","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LARGECAP_BEAUTY_CHANNEL_SPIKE_WITHOUT_MARGIN_REORDER_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-BeautyLargecapChannelSpike-NoMarginReorderBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_after_local_peak","current_profile_verdict":"current_profile_false_positive_if_channel_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Large-cap beauty rally peaked locally and collapsed without repeat reorder and margin durability. C20 should route this to Watch/4B-risk."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 018290 브이티 — K-beauty global sell-through/distribution bridge positive

Entry row: `2024-03-21 c=16370`.  
Observed path: early low `2024-03-22 l=15680`, strong 30D high `2024-05-02 h=23400`, 90D high `2024-06-19 h=40000`, and later high `2024-12-16 h=44000`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L85_C20_018290_20240321_STAGE2_KBEAUTY_GLOBAL_SELLTHROUGH_BRIDGE","case_id":"C20_R5L85_018290_VT_KBEAUTY_GLOBAL_SELLTHROUGH","symbol":"018290","company_name":"브이티","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-KBeautyGlobalSellthroughBridge-Positive","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":16370.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_K_beauty_global_distribution_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; K-beauty global sell-through/distribution bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["global_distribution_proxy","channel_sellthrough_proxy","repeat_reorder_proxy","relative_strength_turn"],"stage3_evidence_fields":["margin_bridge_pending","inventory_discipline_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv","profile_path":"atlas/symbol_profiles/018/018290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":42.94,"MFE_90D_pct":144.35,"MFE_180D_pct":168.78,"MAE_30D_pct":-4.21,"MAE_90D_pct":-4.21,"MAE_180D_pct":-4.21,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-16","peak_price":44000.0,"max_drawdown_low_date":"2024-03-22","max_drawdown_low":15680.0,"drawdown_after_peak_pct":-35.34,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_shallow_MAE","current_profile_verdict":"current_profile_correct_if_sellthrough_distribution_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"018290_2024-03-21_16370","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C20 can allow Stage2/Yellow when beauty/consumer strength is tied to global sell-through, reorder and distribution bridge. Green still requires exact channel, inventory and margin evidence."}
```

### 6.2 051900 LG생활건강 — beauty China/reopening rebound without global sell-through bridge

Entry row: `2024-05-10 c=466000`.  
Observed path: local high `2024-05-23 h=480000`, then lows `2024-08-05 l=321000` and `2024-12-27 l=304000`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L85_C20_051900_20240510_STAGE2_FALSE_POSITIVE_BEAUTY_REOPENING_REBOUND","case_id":"C20_R5L85_051900_LGHNH_REOPENING_REBOUND_NO_BRIDGE","symbol":"051900","company_name":"LG생활건강","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LEGACY_BEAUTY_CHINA_REOPENING_REBOUND_WITHOUT_GLOBAL_SELLTHROUGH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-BeautyChinaReopeningRebound-NoGlobalSellthroughBridge","trigger_date":"2024-05-10","entry_date":"2024-05-10","entry_price":466000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_legacy_beauty_reopening_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; beauty/China reopening rebound treated as insufficient without global sell-through, channel reorder and margin recovery bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["beauty_reopening_beta","relative_strength_rebound"],"stage3_evidence_fields":["global_sellthrough_bridge_missing","channel_reorder_missing","margin_bridge_missing","inventory_quality_missing"],"stage4b_evidence_fields":["price_only_local_peak","margin_recovery_failure_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv","profile_path":"atlas/symbol_profiles/051/051900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.00,"MFE_90D_pct":3.00,"MFE_180D_pct":3.00,"MAE_30D_pct":-22.85,"MAE_90D_pct":-31.12,"MAE_180D_pct":-34.76,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-23","peak_price":480000.0,"max_drawdown_low_date":"2024-12-27","max_drawdown_low":304000.0,"drawdown_after_peak_pct":-36.67,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"reopening_rebound_without_sellthrough_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","margin_recovery_failure_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_reopening_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"051900_2024-05-10_466000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C20 should not upgrade legacy beauty reopening beta without global sell-through, channel reorder and margin recovery bridge. Low MFE and high MAE support local 4B guard."}
```

### 6.3 090430 아모레퍼시픽 — large-cap beauty channel spike without margin/reorder bridge

Entry row: `2024-05-31 c=194200`.  
Observed path: same-day high `h=200500`, then lows `2024-07-04 l=145900`, `2024-10-25 l=117000`, and `2024-12-09 l=99500`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L85_C20_090430_20240531_STAGE2_FALSE_POSITIVE_BEAUTY_CHANNEL_SPIKE","case_id":"C20_R5L85_090430_AMOREPACIFIC_CHANNEL_SPIKE_NO_MARGIN_REORDER","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LARGECAP_BEAUTY_CHANNEL_SPIKE_WITHOUT_MARGIN_REORDER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-BeautyLargecapChannelSpike-NoMarginReorderBridge","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":194200.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_largecap_beauty_channel_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; large-cap beauty/channel spike treated as insufficient without repeat reorder, global distribution and margin durability bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["beauty_channel_spike","relative_strength_extension"],"stage3_evidence_fields":["repeat_reorder_missing","margin_durability_missing","global_distribution_quality_missing"],"stage4b_evidence_fields":["price_only_local_peak","channel_margin_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv","profile_path":"atlas/symbol_profiles/090/090430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.24,"MFE_90D_pct":3.24,"MFE_180D_pct":3.24,"MAE_30D_pct":-24.87,"MAE_90D_pct":-35.89,"MAE_180D_pct":-48.76,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-31","peak_price":200500.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":99500.0,"drawdown_after_peak_pct":-50.37,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"largecap_beauty_peak_without_reorder_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","channel_margin_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_after_local_peak","current_profile_verdict":"current_profile_false_positive_if_channel_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"090430_2024-05-31_194200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C20 beauty channel spike without repeat reorder, global distribution and margin bridge produced tiny MFE and severe MAE. Keep Watch/4B-risk, not Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_R5L85_018290_VT_KBEAUTY_GLOBAL_SELLTHROUGH","trigger_id":"R5L85_C20_018290_20240321_STAGE2_KBEAUTY_GLOBAL_SELLTHROUGH_BRIDGE","symbol":"018290","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C20 requires global sell-through/reorder bridge rather than beauty theme alone","raw_component_scores_before":{"global_distribution_score":15,"sellthrough_reorder_score":14,"brand_quality_score":12,"margin_bridge_score":9,"inventory_discipline_score":8,"relative_strength_score":15,"valuation_repricing_score":10,"execution_risk_score":-4,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"global_distribution_score":18,"sellthrough_reorder_score":17,"brand_quality_score":14,"margin_bridge_score":11,"inventory_discipline_score":10,"relative_strength_score":16,"valuation_repricing_score":11,"execution_risk_score":-3,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Global distribution and sell-through bridge support Yellow/Green-candidate watch, but exact reorder/margin evidence still blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_R5L85_051900_LGHNH_REOPENING_REBOUND_NO_BRIDGE","trigger_id":"R5L85_C20_051900_20240510_STAGE2_FALSE_POSITIVE_BEAUTY_REOPENING_REBOUND","symbol":"051900","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_scope":"current_default_proxy","profile_hypothesis":"legacy beauty reopening beta without sell-through/margin bridge should be blocked","raw_component_scores_before":{"global_distribution_score":5,"sellthrough_reorder_score":3,"brand_quality_score":9,"margin_bridge_score":2,"inventory_discipline_score":2,"relative_strength_score":12,"valuation_repricing_score":7,"execution_risk_score":-10,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":31,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"global_distribution_score":2,"sellthrough_reorder_score":0,"brand_quality_score":7,"margin_bridge_score":0,"inventory_discipline_score":0,"relative_strength_score":5,"valuation_repricing_score":3,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and high MAE convert reopening beta into evidence-quality failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C20_R5L85_090430_AMOREPACIFIC_CHANNEL_SPIKE_NO_MARGIN_REORDER","trigger_id":"R5L85_C20_090430_20240531_STAGE2_FALSE_POSITIVE_BEAUTY_CHANNEL_SPIKE","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_scope":"current_default_proxy","profile_hypothesis":"beauty channel spike without reorder and margin durability should remain Watch/blocked","raw_component_scores_before":{"global_distribution_score":6,"sellthrough_reorder_score":3,"brand_quality_score":10,"margin_bridge_score":3,"inventory_discipline_score":2,"relative_strength_score":13,"valuation_repricing_score":7,"execution_risk_score":-12,"theme_spike_risk":-13,"information_confidence":3},"weighted_score_before":33,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"global_distribution_score":2,"sellthrough_reorder_score":0,"brand_quality_score":8,"margin_bridge_score":0,"inventory_discipline_score":0,"relative_strength_score":4,"valuation_repricing_score":3,"execution_risk_score":-18,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Local price peak plus missing reorder/margin bridge requires local 4B guard."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R5L85_C20_P0_CURRENT","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C20 needs explicit sell-through, reorder and margin bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":50.20,"avg_MAE90_pct":-23.74,"avg_MFE180_pct":58.34,"avg_MAE180_pct":-29.24,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C20_sellthrough_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R5L85_C20_P1_SECTOR_SPECIFIC","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_id":"P1_L5_global_distribution_sellthrough_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L5 beauty/food global signals need channel sell-through, repeat reorder, distribution quality or margin bridge before Stage2-Actionable","changed_axes":["global_sellthrough_bridge_required","repeat_reorder_required","margin_bridge_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_sellthrough_reorder_distribution_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":50.20,"avg_MAE90_pct":-23.74,"avg_MFE180_pct":58.34,"avg_MAE180_pct":-29.24,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R5L85_C20_P2_CANONICAL","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_id":"P2_C20_sellthrough_margin_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C20 should reward global distribution conversion, not beauty reopening or channel theme spikes","changed_axes":["C20_sellthrough_reorder_bridge_required","C20_legacy_reopening_beta_penalty","C20_channel_spike_local_4B_guard"],"changed_thresholds":{"stage2_yellow_gate":"sellthrough_reorder_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":50.20,"avg_MAE90_pct":-23.74,"avg_MFE180_pct":58.34,"avg_MAE180_pct":-29.24,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R5L85_C20_P3_COUNTEREXAMPLE_GUARD","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","profile_id":"P3_C20_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-20 while sell-through/reorder bridge is missing, block Yellow/Green","changed_axes":["C20_high_MAE_guardrail","C20_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_20"},"eligible_trigger_count":3,"avg_MFE90_pct":50.20,"avg_MAE90_pct":-23.74,"avg_MFE180_pct":58.34,"avg_MAE180_pct":-29.24,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"C20_K_BEAUTY_GLOBAL_DISTRIBUTION_VS_REOPENING_CHANNEL_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":50.20,"avg_MAE90_pct":-23.74,"avg_MFE180_pct":58.34,"avg_MAE180_pct":-29.24,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C20 needs bridge discipline. 018290 shows true global distribution/sell-through bridge, while 051900 and 090430 show beauty reopening/channel spikes that fail without repeat reorder, inventory discipline and margin durability."}
{"row_type":"stage_transition_summary","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"018290","trigger_type":"Stage2-Actionable-KBeautyGlobalSellthroughBridge-Positive","entry_date":"2024-03-21","stage2_to_90D_outcome":"good_stage2_very_high_MFE_shallow_MAE","stage2_to_180D_outcome":"positive_global_distribution_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when global distribution, sell-through and reorder bridge exists; Green requires exact channel and margin evidence."}
{"row_type":"stage_transition_summary","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"051900","trigger_type":"Stage2-FalsePositive-BeautyChinaReopeningRebound-NoGlobalSellthroughBridge","entry_date":"2024-05-10","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_reopening_rebound","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Legacy beauty reopening beta without global sell-through and margin recovery should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"090430","trigger_type":"Stage2-FalsePositive-BeautyLargecapChannelSpike-NoMarginReorderBridge","entry_date":"2024-05-31","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_channel_spike_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Beauty channel spike without repeat reorder and margin durability should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","residual_type":"beauty_food_global_distribution_theme_overcredit_without_sellthrough_reorder_margin_bridge","contribution":"Adds two C20 local 4B/high-MAE counterexamples against one global sell-through bridge positive, avoiding C20 top-covered symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_BRIDGE_VS_CHINA_REOPENING_THEME_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C20 now has non-top-symbol beauty reopening/channel-spike counterexamples; next R5 loops should exact-URL repair global channel, reorder, inventory discipline and margin bridge evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","axis":"C20_sellthrough_reorder_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"018290 worked with global sell-through/distribution proxy; 051900 and 090430 failed when reopening/channel strength lacked repeat reorder and margin bridge."}
{"row_type":"shadow_weight","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","axis":"C20_beauty_reopening_channel_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Legacy beauty reopening and large-cap channel spikes showed low MFE and high/deep MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R5","loop":"85","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","axis":"C20_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and MAE90<=-20 while sell-through/reorder/margin bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - beauty_reopening_beta_overcredit
  - channel_spike_no_sellthrough_reorder_bridge
  - margin_recovery_failure_high_MAE
new_axis_proposed:
  - C20_sellthrough_reorder_margin_bridge_required_shadow_only
  - C20_beauty_reopening_channel_local_4B_watch_guard_shadow_only
  - C20_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C20
  - full_4b_requires_non_price_evidence within C20
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
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
3. Confirm R5 / L5 / C20 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided C20 top-covered symbols.
6. If aggregate support remains stable after exact evidence URL repair, consider C20-scoped safe patch candidates:
   - C20_sellthrough_reorder_margin_bridge_required
   - C20_beauty_reopening_channel_local_4B_watch_guard
   - C20_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R5
completed_loop = 85
next_round = R6
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION.
```
