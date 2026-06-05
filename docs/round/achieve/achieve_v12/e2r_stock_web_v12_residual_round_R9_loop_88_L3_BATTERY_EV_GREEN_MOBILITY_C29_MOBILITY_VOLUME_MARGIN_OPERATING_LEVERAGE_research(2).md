# E2R Stock-Web v12 Residual Research — R9 Loop 88 / L3 / C29

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R9
loop: 88
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE_VS_EV_BODY_PARTS_LATE_SPIKE_NO_FRESH_ORDER_CASH_BRIDGE
sector: mobility / auto parts / EV body parts / customer volume / margin / operating leverage
output_file: e2r_stock_web_v12_residual_round_R9_loop_88_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R8 loop 88`.

```text
scheduled_round = R9
scheduled_loop = 88
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

R9 is the mobility / transport / operating-leverage lane.  
C29 remains the target, but this loop avoids the C29 top-covered list:

```text
011210, 000270, 005380, 005850, 010690, 018880
```

It also avoids prior C29 loop sets:

```text
R9 loop87: 004490, 009900, 024900
R9 loop86: 073240, 118990, 090080
R9 loop85: 000120, 003620, 215360
R9 loop84: 086280, 161390, 271940
earlier known C29 set: 012330, 002350, 204320
```

Selected symbols:

```text
200880, 092200, 123040
```

This loop tests a different C29 pocket: global auto-parts volume/mix/margin bridge versus EV drivetrain/body-parts late spikes or late extensions that do not prove fresh order, customer volume, margin or cash conversion.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"200880","company_name":"서연이화","profile_path":"atlas/symbol_profiles/200/200880.json","first_date":"2014-08-08","last_date":"2026-02-20","trading_day_count":2829,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"092200","company_name":"디아이씨","profile_path":"atlas/symbol_profiles/092/092200.json","first_date":"2007-10-18","last_date":"2026-02-20","trading_day_count":4514,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2008-05-14","2019-08-28"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"123040","company_name":"엠에스오토텍","profile_path":"atlas/symbol_profiles/123/123040.json","first_date":"2010-08-06","last_date":"2026-02-20","trading_day_count":3823,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2014-11-28","2017-12-22","2024-08-30"],"has_major_raw_discontinuity":true,"calibration_caveat":"A 2024-08-30 corporate-action candidate exists. The selected entry is 2024-09-26, after that candidate, and remains data-quality-watch before any patch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_entry_after_2024-08-30_candidate; data_quality_watch"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"200880","trigger_type":"Stage2-Actionable-GlobalAutoPartsVolumeMixMarginBridge-Positive","entry_date":"2024-02-01","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and prior C29 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"092200","trigger_type":"Stage2-FalsePositive-EVDrivetrainLateSpike-NoFreshVolumeMarginBridge","entry_date":"2024-06-26","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and prior C29 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"123040","trigger_type":"Stage2-FalsePositive-EVBodyPartsLateExtension-NoFreshOrderCashBridge","entry_date":"2024-09-26","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and prior C29 loop sets; selected after 2024-08-30 corporate-action candidate"}
```

## 4. Research question

C29 is not “auto-parts or mobility theme moved.”  
The useful signal is the operating bridge: customer volume, global model exposure, mix, utilization, pricing, margin expansion, working-capital discipline and cash conversion. Without this bridge, the stock is only revving in neutral; price noise makes sound, but no operating leverage moves the car.

Residual question:

```text
Can C29 distinguish:
1. global auto-parts volume / mix / margin bridge with usable rerating,
2. EV drivetrain late spike where MFE exists but fresh order and margin/cash bridge are missing,
3. EV body-parts late extension after corporate-action candidate where price path decays without customer volume or cash bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C29_R9L88_200880_SEOYON_GLOBAL_AUTOPARTS_VOLUME_MARGIN","symbol":"200880","company_name":"서연이화","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"GLOBAL_AUTOPARTS_VOLUME_MIX_MARGIN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-GlobalAutoPartsVolumeMixMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_low_90D_MAE_late_drawdown","current_profile_verdict":"current_profile_correct_if_volume_mix_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Global auto-parts volume/mix/margin proxy produced a strong MFE with tolerable early MAE. Later drawdown keeps Green strict and requires exact customer-volume/margin/cash evidence."}
{"row_type":"case","case_id":"C29_R9L88_092200_DIC_EV_DRIVETRAIN_LATE_SPIKE","symbol":"092200","company_name":"디아이씨","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_DRIVETRAIN_LATE_SPIKE_WITHOUT_FRESH_VOLUME_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-EVDrivetrainLateSpike-NoFreshVolumeMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_after_late_spike","current_profile_verdict":"current_profile_false_positive_if_late_EV_drivetrain_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Late EV/drivetrain spike had only limited MFE from the selected entry and then deep forward MAE when fresh order, volume, mix, margin and cash bridge failed to confirm."}
{"row_type":"case","case_id":"C29_R9L88_123040_MSAUTOTECH_BODY_PARTS_LATE_EXTENSION","symbol":"123040","company_name":"엠에스오토텍","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_BODY_PARTS_LATE_EXTENSION_WITHOUT_FRESH_ORDER_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-EVBodyPartsLateExtension-NoFreshOrderCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_data_quality_watch","current_profile_verdict":"current_profile_false_positive_if_body_parts_late_extension_overcredited","price_source":"Songdaiki/stock-web","notes":"EV body-parts late extension after the 2024-08-30 candidate had near-zero MFE and deep MAE without fresh order, customer volume, margin and cash bridge. It is usable as a data-quality-watch counterexample."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 200880 서연이화 — global auto-parts volume / mix / margin bridge positive

Entry row: `2024-02-01 c=18000`.  
Observed path: entry low `2024-02-01 l=16730`, high `2024-02-07 h=25000`, and later drawdown into autumn and winter.

```jsonl
{"row_type":"trigger","trigger_id":"R9L88_C29_200880_20240201_STAGE2_GLOBAL_AUTOPARTS_VOLUME_MARGIN","case_id":"C29_R9L88_200880_SEOYON_GLOBAL_AUTOPARTS_VOLUME_MARGIN","symbol":"200880","company_name":"서연이화","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"GLOBAL_AUTOPARTS_VOLUME_MIX_MARGIN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-GlobalAutoPartsVolumeMixMarginBridge-Positive","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":18000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_global_autoparts_volume_mix_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; global auto-parts customer volume, mix and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["customer_volume_proxy","global_model_mix_proxy","operating_leverage_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_order_pending","margin_mix_bridge_pending","utilization_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/200/200880/2024.csv","profile_path":"atlas/symbol_profiles/200/200880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":38.89,"MFE_90D_pct":38.89,"MFE_180D_pct":38.89,"MAE_30D_pct":-7.06,"MAE_90D_pct":-7.06,"MAE_180D_pct":-26.78,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-07","peak_price":25000.0,"max_drawdown_low_date":"2024-10-29","max_drawdown_low":13180.0,"drawdown_after_peak_pct":-47.28,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B; late drawdown blocks Green without exact volume/mix/margin/cash evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_low_90D_MAE_late_drawdown","current_profile_verdict":"current_profile_correct_if_volume_mix_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"200880_2024-02-01_18000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 can allow Stage2/Yellow when mobility strength is tied to global customer volume, mix, margin, utilization and cash bridge. Green still requires exact source-grade evidence because later drawdown can be large."}
```

### 6.2 092200 디아이씨 — EV drivetrain late spike without fresh volume/margin bridge

Entry row: `2024-06-26 c=6290`.  
Observed path: same-day high `2024-06-26 h=6920`, later lows `2024-07-22 l=4580`, `2024-11-13 l=3165`, and `2024-12-09 l=3335`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L88_C29_092200_20240626_STAGE2_FALSE_POSITIVE_EV_DRIVETRAIN_SPIKE","case_id":"C29_R9L88_092200_DIC_EV_DRIVETRAIN_LATE_SPIKE","symbol":"092200","company_name":"디아이씨","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_DRIVETRAIN_LATE_SPIKE_WITHOUT_FRESH_VOLUME_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-EVDrivetrainLateSpike-NoFreshVolumeMarginBridge","trigger_date":"2024-06-26","entry_date":"2024-06-26","entry_price":6290.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_EV_drivetrain_customer_volume_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; EV drivetrain spike treated as insufficient without fresh customer volume, mix, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["EV_drivetrain_theme","late_relative_strength_spike"],"stage3_evidence_fields":["fresh_customer_volume_missing","mix_margin_bridge_missing","utilization_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","volume_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/092/092200/2024.csv","profile_path":"atlas/symbol_profiles/092/092200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.02,"MFE_90D_pct":10.02,"MFE_180D_pct":10.02,"MAE_30D_pct":-27.19,"MAE_90D_pct":-43.64,"MAE_180D_pct":-49.68,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-26","peak_price":6920.0,"max_drawdown_low_date":"2024-11-13","max_drawdown_low":3165.0,"drawdown_after_peak_pct":-54.26,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_EV_drivetrain_spike_without_fresh_volume_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","volume_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_after_late_spike","current_profile_verdict":"current_profile_false_positive_if_late_EV_drivetrain_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"092200_2024-06-26_6290","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 should not promote late EV drivetrain spikes without fresh customer volume, mix, margin, utilization and cash bridge. Low MFE with deep MAE forces Watch/4B-risk routing."}
```

### 6.3 123040 엠에스오토텍 — EV body-parts late extension without fresh order/cash bridge

Entry row: `2024-09-26 c=3530`, selected after the `2024-08-30` corporate-action candidate.  
Observed path: local high `2024-09-27 h=3585`, then lows `2024-11-14 l=2500` and `2024-12-09 l=2170`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L88_C29_123040_20240926_STAGE2_FALSE_POSITIVE_BODY_PARTS_LATE_EXTENSION","case_id":"C29_R9L88_123040_MSAUTOTECH_BODY_PARTS_LATE_EXTENSION","symbol":"123040","company_name":"엠에스오토텍","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_BODY_PARTS_LATE_EXTENSION_WITHOUT_FRESH_ORDER_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-EVBodyPartsLateExtension-NoFreshOrderCashBridge","trigger_date":"2024-09-26","entry_date":"2024-09-26","entry_price":3530.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_EV_body_parts_late_extension_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; EV body-parts late extension treated as insufficient without fresh order, customer volume, utilization, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["EV_body_parts_late_extension","relative_strength_rebound"],"stage3_evidence_fields":["fresh_order_bridge_missing","customer_volume_bridge_missing","margin_cash_bridge_missing","utilization_bridge_missing"],"stage4b_evidence_fields":["price_only_late_extension","fresh_order_cash_bridge_missing_watch","data_quality_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/123/123040/2024.csv","profile_path":"atlas/symbol_profiles/123/123040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.56,"MFE_90D_pct":1.56,"MFE_180D_pct":1.56,"MAE_30D_pct":-14.45,"MAE_90D_pct":-38.53,"MAE_180D_pct":-38.53,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-27","peak_price":3585.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":2170.0,"drawdown_after_peak_pct":-39.47,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"EV_body_parts_late_extension_without_fresh_order_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","fresh_order_cash_bridge_missing_watch","data_quality_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_data_quality_watch","current_profile_verdict":"current_profile_false_positive_if_body_parts_late_extension_overcredited","calibration_usable":true,"forward_window_trading_days":"partial_post_candidate_2024_window","calibration_block_reasons":["data_quality_watch_due_to_2024-08-30_corporate_action_candidate_before_entry"],"corporate_action_window_status":"selected_entry_after_2024-08-30_candidate","same_entry_group_id":"123040_2024-09-26_3530","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"do_not_count_as_new_case":false,"current_profile_residual":"C29 should not treat post-candidate body-parts late extension as fresh order evidence. Near-zero MFE and deep MAE require 4B-watch and data-quality repair before any patch."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C29_R9L88_200880_SEOYON_GLOBAL_AUTOPARTS_VOLUME_MARGIN","trigger_id":"R9L88_C29_200880_20240201_STAGE2_GLOBAL_AUTOPARTS_VOLUME_MARGIN","symbol":"200880","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C29 requires global customer volume, mix, margin and cash bridge rather than mobility theme alone","raw_component_scores_before":{"customer_volume_score":13,"global_model_mix_score":12,"operating_leverage_score":12,"utilization_score":10,"margin_bridge_score":10,"cash_conversion_score":7,"relative_strength_score":12,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"customer_volume_score":16,"global_model_mix_score":15,"operating_leverage_score":15,"utilization_score":12,"margin_bridge_score":12,"cash_conversion_score":9,"relative_strength_score":13,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Customer volume/mix/margin bridge and high MFE support Yellow-watch; late drawdown and proxy-only evidence block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C29_R9L88_092200_DIC_EV_DRIVETRAIN_LATE_SPIKE","trigger_id":"R9L88_C29_092200_20240626_STAGE2_FALSE_POSITIVE_EV_DRIVETRAIN_SPIKE","symbol":"092200","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"EV drivetrain late spike without fresh volume/margin bridge should be 4B-watch","raw_component_scores_before":{"customer_volume_score":4,"global_model_mix_score":2,"operating_leverage_score":1,"utilization_score":1,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":12,"valuation_repricing_score":5,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_volume_score":0,"global_model_mix_score":0,"operating_leverage_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE convert late EV drivetrain spike into missing volume/margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C29_R9L88_123040_MSAUTOTECH_BODY_PARTS_LATE_EXTENSION","trigger_id":"R9L88_C29_123040_20240926_STAGE2_FALSE_POSITIVE_BODY_PARTS_LATE_EXTENSION","symbol":"123040","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"EV body-parts late extension without fresh order/cash bridge should remain Watch/blocked","raw_component_scores_before":{"customer_volume_score":3,"global_model_mix_score":1,"operating_leverage_score":1,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":8,"valuation_repricing_score":3,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_volume_score":0,"global_model_mix_score":0,"operating_leverage_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE require fresh order, customer volume, margin and cash bridge before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R9L88_C29_P0_CURRENT","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C29 needs explicit customer volume, mix, utilization, margin and cash bridge taxonomy plus post-corporate-action data-quality watch","eligible_trigger_count":3,"avg_MFE90_pct":16.82,"avg_MAE90_pct":-29.74,"avg_MFE180_pct":16.82,"avg_MAE180_pct":-38.33,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C29_volume_mix_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R9L88_C29_P1_SECTOR_SPECIFIC","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P1_L3_mobility_volume_mix_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L3 mobility signals need customer volume, mix, utilization, operating leverage, margin or cash conversion before Stage2-Actionable","changed_axes":["customer_volume_required","mix_margin_bridge_required","late_extension_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_volume_mix_utilization_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":16.82,"avg_MAE90_pct":-29.74,"avg_MFE180_pct":16.82,"avg_MAE180_pct":-38.33,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R9L88_C29_P2_CANONICAL","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P2_C29_volume_mix_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C29 should reward operating-leverage mechanics, not EV drivetrain/body-parts price spikes","changed_axes":["C29_volume_mix_margin_cash_bridge_required","C29_late_spike_extension_local_4B_guard","C29_post_corporate_action_data_quality_watch"],"changed_thresholds":{"stage2_yellow_gate":"customer_volume_or_fresh_order_plus_margin_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":16.82,"avg_MAE90_pct":-29.74,"avg_MFE180_pct":16.82,"avg_MAE180_pct":-38.33,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R9L88_C29_P3_COUNTEREXAMPLE_GUARD","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P3_C29_low_MFE_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<12 and MAE90<=-25 while fresh volume/margin/cash bridge is missing, block Yellow/Green; if post corporate-action candidate, keep data-quality watch","changed_axes":["C29_low_MFE_guardrail","C29_high_MAE_4B_guardrail","C29_data_quality_watch_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_12_and_MAE90_le_minus_25"},"eligible_trigger_count":3,"avg_MFE90_pct":16.82,"avg_MAE90_pct":-29.74,"avg_MFE180_pct":16.82,"avg_MAE180_pct":-38.33,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_GLOBAL_AUTOPARTS_VOLUME_MARGIN_VS_LATE_EV_PARTS_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":16.82,"avg_MAE90_pct":-29.74,"avg_MFE180_pct":16.82,"avg_MAE180_pct":-38.33,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_12":0.67,"stage2_bad_entry_rate_MAE90_le_minus_25":0.67,"interpretation":"C29 needs bridge discipline. 서연이화 shows global auto-parts volume/mix/margin bridge can create a usable rerating, while 디아이씨 and 엠에스오토텍 show late EV drivetrain/body-parts spikes should not be promoted without fresh order, customer volume, utilization, margin and cash conversion."}
{"row_type":"stage_transition_summary","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"200880","trigger_type":"Stage2-Actionable-GlobalAutoPartsVolumeMixMarginBridge-Positive","entry_date":"2024-02-01","stage2_to_90D_outcome":"good_stage2_high_MFE_low_MAE","stage2_to_180D_outcome":"watch_positive_with_late_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when customer volume, global model mix, utilization, margin and cash bridge exists; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"092200","trigger_type":"Stage2-FalsePositive-EVDrivetrainLateSpike-NoFreshVolumeMarginBridge","entry_date":"2024-06-26","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_late_EV_drivetrain_spike_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Late EV drivetrain spike without fresh volume/margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"123040","trigger_type":"Stage2-FalsePositive-EVBodyPartsLateExtension-NoFreshOrderCashBridge","entry_date":"2024-09-26","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_deep_MAE","stage2_to_180D_outcome":"failed_post_candidate_late_extension_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"EV body-parts late extension after the 2024-08-30 candidate should remain 4B-watch and data-quality-watch."}
{"row_type":"residual_contribution","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"late_EV_autoparts_spike_extension_overcredit_without_fresh_volume_mix_margin_cash_bridge","contribution":"Adds two C29 late-spike/late-extension 4B counterexamples against one global auto-parts volume/margin positive, avoiding C29 top-covered and previous C29 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE_VS_EV_BODY_PARTS_LATE_SPIKE_NO_FRESH_ORDER_CASH_BRIDGE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C29 now has non-top-symbol global auto-parts positive and two late EV drivetrain/body-parts counterexamples; next R9 loops should exact-URL repair customer volume, fresh order, utilization, mix/margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_volume_mix_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"200880 worked when global volume/mix/margin proxy was present; 092200 and 123040 failed when late EV drivetrain/body-parts strength lacked fresh order and margin/cash bridge."}
{"row_type":"shadow_weight","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_late_spike_extension_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Late EV parts rows had low or near-zero MFE and deep MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_post_corporate_action_data_quality_watch","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"123040 selected entry is after the 2024-08-30 candidate and should keep data-quality watch before any production consideration."}
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
  - late_EV_autoparts_spike_extension_overcredit
  - fresh_order_bridge_missing
  - customer_volume_bridge_missing
  - mix_margin_cash_conversion_bridge_missing
new_axis_proposed:
  - C29_volume_mix_margin_cash_bridge_required_shadow_only
  - C29_late_spike_extension_local_4B_guard_shadow_only
  - C29_post_corporate_action_data_quality_watch_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C29
  - full_4b_requires_non_price_evidence within C29
  - hard_4c_thesis_break_routes_to_4c within C29
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

All selected triggers use Stock-Web tradable raw OHLC rows.  
`123040` has a 2024-08-30 corporate-action candidate before the selected entry. The row is selected after that candidate and is usable as a post-candidate counterexample, but it remains data-quality-watch before any production patch.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
data_quality_watch = true for 123040
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
3. Confirm R9 / L3 / C29 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C29 top-covered symbols
   - R9 loop87 C29 symbols
   - R9 loop86 C29 symbols
   - R9 loop85 C29 symbols
   - R9 loop84 C29 symbols
   - earlier known C29 symbols listed in this MD
6. Keep 123040 in data-quality watch because of the 2024-08-30 corporate-action candidate.
7. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C29-scoped safe patch candidates:
   - C29_volume_mix_margin_cash_bridge_required
   - C29_late_spike_extension_local_4B_guard
   - C29_post_corporate_action_data_quality_watch
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R9
completed_loop = 88
next_round = R10
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.
```
