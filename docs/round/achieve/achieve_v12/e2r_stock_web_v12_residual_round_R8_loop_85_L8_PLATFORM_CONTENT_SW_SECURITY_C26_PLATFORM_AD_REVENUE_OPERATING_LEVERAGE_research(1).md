# E2R Stock-Web v12 Residual Research — R8 Loop 85 / L8 / C26

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R8
loop: 85
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: LIVE_PLATFORM_AD_SUBSCRIPTION_OPERATING_LEVERAGE_VS_DIGITAL_AD_BETA_SPIKE
sector: platform / content / software / security / ad revenue operating leverage
output_file: e2r_stock_web_v12_residual_round_R8_loop_85_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R7 loop 85`.

```text
scheduled_round = R8
scheduled_loop = 85
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

R8 is restricted to platform / content / software / security.  
C26 is selected because the No-Repeat Index shows it is still thin and bad-heavy:

```text
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
rows = 13
symbols = 10
good/bad Stage2 = 2/6
4B/4C = 0/1
top-covered = 042000, 214270, 237820, 030000, 035420, 035720
```

This run avoids the top-covered set and tests the core C26 residual:

```text
Does platform/ad revenue operating leverage require verified monetization, retention, ARPU, ad-fill or subscription bridge, rather than just platform/ad-tech relative strength?
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"067160","company_name":"SOOP","profile_path":"atlas/symbol_profiles/067/067160.json","first_date":"2003-12-19","last_date":"2026-02-20","trading_day_count":5450,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["2005-12-27","2007-06-05","2007-06-14","2008-01-24","2011-01-27"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here; market changed from KOSDAQ to KOSDAQ GLOBAL on 2024-06-14 without a 2024 corporate-action candidate.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"089600","company_name":"KT나스미디어","profile_path":"atlas/symbol_profiles/089/089600.json","first_date":"2013-07-17","last_date":"2026-02-20","trading_day_count":3090,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window; historical name at trigger date was 나스미디어"}
{"row_type":"price_source_validation","symbol":"123570","company_name":"이엠넷","profile_path":"atlas/symbol_profiles/123/123570.json","first_date":"2011-11-25","last_date":"2026-02-20","trading_day_count":3497,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2016-08-11","2016-09-06","2018-06-14","2018-07-10"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"067160","trigger_type":"Stage2-Actionable-LivePlatformAdSubscriptionOperatingLeverage-Positive","entry_date":"2024-01-08","duplicate_status":"new C26 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"089600","trigger_type":"Stage2-FalsePositive-DigitalAdAgencyBeta-NoOperatingLeverageBridge","entry_date":"2024-01-24","duplicate_status":"new C26 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"123570","trigger_type":"Stage2-FalsePositive-SmallcapDigitalAdThemeSpike-NoRevenueRetentionBridge","entry_date":"2024-03-06","duplicate_status":"new C26 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C26 is not “platform/ad-tech stock moved.” The operating-leverage engine needs recurring monetization: ad fill, ARPU, creator/user retention, subscription or donation take-rate, enterprise advertiser quality, and margin expansion. If only the theme moves and the revenue bridge stays missing, the move is like a billboard lit with no traffic under it.

Residual question:

```text
Can C26 distinguish:
1. live platform monetization and operating leverage with sustained MFE,
2. digital ad agency/platform beta spike without revenue-retention bridge,
3. small-cap digital advertising theme spike with no ARPU, retention or margin conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C26_R8L85_067160_SOOP_LIVE_PLATFORM_OPERATING_LEVERAGE","symbol":"067160","company_name":"SOOP","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_PLATFORM_AD_SUBSCRIPTION_OPERATING_LEVERAGE_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-LivePlatformAdSubscriptionOperatingLeverage-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_monetization_bridge_required","price_source":"Songdaiki/stock-web","notes":"Live platform monetization/retention proxy produced strong MFE with tolerable early MAE. Green still requires exact revenue, ARPU, ad-fill and margin evidence."}
{"row_type":"case","case_id":"C26_R8L85_089600_NASMEDIA_DIGITAL_AD_BETA","symbol":"089600","company_name":"KT나스미디어","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"DIGITAL_AD_AGENCY_BETA_WITHOUT_OPERATING_LEVERAGE_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DigitalAdAgencyBeta-NoOperatingLeverageBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_ad_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"Digital ad rebound had a local peak but lacked ARPU, revenue-retention and margin bridge; forward path showed high MAE."}
{"row_type":"case","case_id":"C26_R8L85_123570_EMNET_SMALLCAP_AD_THEME","symbol":"123570","company_name":"이엠넷","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"SMALLCAP_DIGITAL_AD_THEME_SPIKE_WITHOUT_REVENUE_RETENTION_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SmallcapDigitalAdThemeSpike-NoRevenueRetentionBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_extreme_MAE_after_theme_peak","current_profile_verdict":"current_profile_false_positive_if_smallcap_ad_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Small-cap ad theme spike peaked immediately and later collapsed without revenue retention or margin bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 067160 SOOP — live platform monetization / operating leverage positive

Entry row: `2024-01-08 c=98800`.  
Observed path: same-day low `88300`, 30D high `2024-02-15 h=126000`, 90D high `2024-02-28 h=139600`, and 180D high `2024-07-11 h=143800`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L85_C26_067160_20240108_STAGE2_LIVE_PLATFORM_OPERATING_LEVERAGE","case_id":"C26_R8L85_067160_SOOP_LIVE_PLATFORM_OPERATING_LEVERAGE","symbol":"067160","company_name":"SOOP","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_PLATFORM_AD_SUBSCRIPTION_OPERATING_LEVERAGE_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-LivePlatformAdSubscriptionOperatingLeverage-Positive","trigger_date":"2024-01-08","entry_date":"2024-01-08","entry_price":98800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_live_platform_monetization_retention_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; live platform user/creator retention, subscription/donation take-rate and ad monetization treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["platform_user_retention_proxy","ad_revenue_or_subscription_monetization_proxy","operating_leverage_proxy","relative_strength_turn"],"stage3_evidence_fields":["ARPU_bridge_pending","ad_fill_or_take_rate_pending","margin_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.53,"MFE_90D_pct":41.30,"MFE_180D_pct":45.55,"MAE_30D_pct":-10.63,"MAE_90D_pct":-10.63,"MAE_180D_pct":-10.63,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":143800.0,"max_drawdown_low_date":"2024-09-30","max_drawdown_low":100300.0,"drawdown_after_peak_pct":-30.25,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_monetization_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window; market_category_change_only_on_2024-06-14","same_entry_group_id":"067160_2024-01-08_98800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C26 can allow Stage2/Yellow when platform strength is tied to monetization, retention and operating leverage. Green still requires exact ARPU, ad-fill/take-rate and margin evidence."}
```

### 6.2 089600 KT나스미디어 — digital ad beta without operating-leverage bridge

Entry row: `2024-01-24 c=25350`.  
Observed path: same-day high `26800`, then lows `2024-06-26 l=16150` and `2024-11-15 l=13720`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L85_C26_089600_20240124_STAGE2_FALSE_POSITIVE_DIGITAL_AD_BETA","case_id":"C26_R8L85_089600_NASMEDIA_DIGITAL_AD_BETA","symbol":"089600","company_name":"KT나스미디어","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"DIGITAL_AD_AGENCY_BETA_WITHOUT_OPERATING_LEVERAGE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-DigitalAdAgencyBeta-NoOperatingLeverageBridge","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":25350.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_digital_ad_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; digital ad agency/platform beta treated as insufficient without revenue retention, ARPU, advertiser quality and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["digital_ad_beta_spike","relative_strength_rebound"],"stage3_evidence_fields":["revenue_retention_missing","ARPU_bridge_missing","advertiser_quality_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","ad_cycle_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089600/2024.csv","profile_path":"atlas/symbol_profiles/089/089600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.72,"MFE_90D_pct":5.72,"MFE_180D_pct":5.72,"MAE_30D_pct":-15.98,"MAE_90D_pct":-36.29,"MAE_180D_pct":-45.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-24","peak_price":26800.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":13720.0,"drawdown_after_peak_pct":-48.81,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"digital_ad_beta_peak_without_operating_leverage_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","ad_cycle_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_ad_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"089600_2024-01-24_25350","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C26 should not upgrade digital ad beta without operating-leverage bridge. Local peak plus high MAE argues for Watch/4B-risk rather than Yellow/Green."}
```

### 6.3 123570 이엠넷 — small-cap digital ad theme spike without revenue retention

Entry row: `2024-03-06 c=4800`.  
Observed path: same-day high `5230`, then lows `2024-06-28 l=2975` and `2024-12-09 l=2150`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L85_C26_123570_20240306_STAGE2_FALSE_POSITIVE_SMALLCAP_AD_THEME","case_id":"C26_R8L85_123570_EMNET_SMALLCAP_AD_THEME","symbol":"123570","company_name":"이엠넷","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"SMALLCAP_DIGITAL_AD_THEME_SPIKE_WITHOUT_REVENUE_RETENTION_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-SmallcapDigitalAdThemeSpike-NoRevenueRetentionBridge","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":4800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_smallcap_digital_ad_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; small-cap digital ad theme spike treated as insufficient without revenue-retention, advertiser quality, operating leverage and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["smallcap_ad_theme_spike","relative_strength_extension"],"stage3_evidence_fields":["revenue_retention_missing","advertiser_quality_missing","operating_leverage_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/123/123570/2024.csv","profile_path":"atlas/symbol_profiles/123/123570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.96,"MFE_90D_pct":8.96,"MFE_180D_pct":8.96,"MAE_30D_pct":-23.75,"MAE_90D_pct":-38.02,"MAE_180D_pct":-55.21,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-06","peak_price":5230.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":2150.0,"drawdown_after_peak_pct":-58.89,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"smallcap_ad_theme_spike_without_revenue_retention_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_extreme_MAE_after_theme_peak","current_profile_verdict":"current_profile_false_positive_if_smallcap_ad_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"123570_2024-03-06_4800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Small-cap ad theme spike had low MFE and extreme MAE when revenue retention and operating leverage bridge were absent. C26 should route this to Watch/4B-risk."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_R8L85_067160_SOOP_LIVE_PLATFORM_OPERATING_LEVERAGE","trigger_id":"R8L85_C26_067160_20240108_STAGE2_LIVE_PLATFORM_OPERATING_LEVERAGE","symbol":"067160","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C26 requires monetization and retention bridge, not platform beta alone","raw_component_scores_before":{"platform_user_retention_score":14,"ad_revenue_bridge_score":13,"subscription_or_take_rate_score":12,"operating_leverage_score":12,"advertiser_quality_score":9,"relative_strength_score":14,"valuation_repricing_score":10,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"platform_user_retention_score":17,"ad_revenue_bridge_score":16,"subscription_or_take_rate_score":15,"operating_leverage_score":15,"advertiser_quality_score":11,"relative_strength_score":15,"valuation_repricing_score":11,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"User/creator retention and monetization bridge supports Yellow-watch, while exact ARPU, ad-fill/take-rate and margin evidence still block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_R8L85_089600_NASMEDIA_DIGITAL_AD_BETA","trigger_id":"R8L85_C26_089600_20240124_STAGE2_FALSE_POSITIVE_DIGITAL_AD_BETA","symbol":"089600","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"ad beta without retention and margin bridge should be blocked","raw_component_scores_before":{"platform_user_retention_score":2,"ad_revenue_bridge_score":5,"subscription_or_take_rate_score":0,"operating_leverage_score":3,"advertiser_quality_score":3,"relative_strength_score":13,"valuation_repricing_score":6,"execution_risk_score":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":28,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"platform_user_retention_score":0,"ad_revenue_bridge_score":2,"subscription_or_take_rate_score":0,"operating_leverage_score":0,"advertiser_quality_score":1,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and high MAE convert ad beta into missing operating-leverage bridge."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_R8L85_123570_EMNET_SMALLCAP_AD_THEME","trigger_id":"R8L85_C26_123570_20240306_STAGE2_FALSE_POSITIVE_SMALLCAP_AD_THEME","symbol":"123570","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"small-cap ad theme without revenue-retention bridge should remain Watch/blocked","raw_component_scores_before":{"platform_user_retention_score":1,"ad_revenue_bridge_score":4,"subscription_or_take_rate_score":0,"operating_leverage_score":2,"advertiser_quality_score":2,"relative_strength_score":15,"valuation_repricing_score":7,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":21,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"platform_user_retention_score":0,"ad_revenue_bridge_score":1,"subscription_or_take_rate_score":0,"operating_leverage_score":0,"advertiser_quality_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Price-only theme spike plus missing revenue-retention bridge and extreme MAE blocks Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R8L85_C26_P0_CURRENT","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C26 needs explicit monetization, ARPU, retention and margin bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":18.66,"avg_MAE90_pct":-28.31,"avg_MFE180_pct":20.08,"avg_MAE180_pct":-37.24,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C26_monetization_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R8L85_C26_P1_SECTOR_SPECIFIC","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_id":"P1_L8_platform_monetization_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L8 platform/ad signals need user retention, ad revenue, subscription/take-rate, advertiser quality or margin bridge before Stage2-Actionable","changed_axes":["monetization_bridge_required","retention_bridge_required","ad_beta_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_retention_ad_revenue_subscription_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":18.66,"avg_MAE90_pct":-28.31,"avg_MFE180_pct":20.08,"avg_MAE180_pct":-37.24,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R8L85_C26_P2_CANONICAL","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_id":"P2_C26_monetization_retention_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C26 should reward platform monetization and operating leverage, not ad-theme beta spikes","changed_axes":["C26_monetization_retention_bridge_required","C26_ad_beta_theme_spike_penalty","C26_smallcap_ad_theme_local_4B_guard"],"changed_thresholds":{"stage2_yellow_gate":"monetization_retention_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":18.66,"avg_MAE90_pct":-28.31,"avg_MFE180_pct":20.08,"avg_MAE180_pct":-37.24,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R8L85_C26_P3_COUNTEREXAMPLE_GUARD","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_id":"P3_C26_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-30 while monetization/retention bridge is missing, block Yellow/Green","changed_axes":["C26_high_MAE_guardrail","C26_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_30"},"eligible_trigger_count":3,"avg_MFE90_pct":18.66,"avg_MAE90_pct":-28.31,"avg_MFE180_pct":20.08,"avg_MAE180_pct":-37.24,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_PLATFORM_MONETIZATION_VS_AD_THEME_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":18.66,"avg_MAE90_pct":-28.31,"avg_MFE180_pct":20.08,"avg_MAE180_pct":-37.24,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE90_le_minus_30":0.67,"interpretation":"C26 needs bridge discipline. SOOP shows platform monetization and retention can rerate, while KT나스미디어 and 이엠넷 show digital ad/theme beta can fail without ad revenue retention, ARPU, advertiser quality and margin conversion."}
{"row_type":"stage_transition_summary","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"067160","trigger_type":"Stage2-Actionable-LivePlatformAdSubscriptionOperatingLeverage-Positive","entry_date":"2024-01-08","stage2_to_90D_outcome":"good_stage2_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_platform_monetization_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when user retention, ad/subscription monetization and operating leverage bridge exists; Green requires exact ARPU and margin evidence."}
{"row_type":"stage_transition_summary","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"089600","trigger_type":"Stage2-FalsePositive-DigitalAdAgencyBeta-NoOperatingLeverageBridge","entry_date":"2024-01-24","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_ad_beta_rebound","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Digital ad beta without revenue-retention and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"123570","trigger_type":"Stage2-FalsePositive-SmallcapDigitalAdThemeSpike-NoRevenueRetentionBridge","entry_date":"2024-03-06","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_smallcap_ad_theme_extreme_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Small-cap ad theme spike without revenue retention and operating leverage should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","residual_type":"platform_ad_theme_overcredit_without_monetization_retention_margin_bridge","contribution":"Adds two C26 local 4B/high-MAE counterexamples against one live-platform monetization bridge positive, avoiding C26 top-covered symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_PLATFORM_AD_SUBSCRIPTION_OPERATING_LEVERAGE_VS_DIGITAL_AD_BETA_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C26 now has non-top-symbol ad/theme beta counterexamples; next R8 loops should exact-URL repair ARPU, ad-fill, take-rate, advertiser quality, user retention and margin bridge evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","axis":"C26_monetization_retention_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"067160 worked with live platform monetization/retention bridge proxy; 089600 and 123570 failed when only digital ad beta or theme strength existed."}
{"row_type":"shadow_weight","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","axis":"C26_ad_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Digital ad beta and small-cap ad theme spikes showed low MFE and high/extreme MAE without non-price operating-leverage bridge."}
{"row_type":"shadow_weight","round":"R8","loop":"85","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","axis":"C26_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and MAE90<=-30 while monetization/retention bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - platform_ad_theme_overcredit
  - digital_ad_beta_no_operating_leverage_bridge
  - smallcap_ad_theme_no_revenue_retention_bridge
  - local_peak_high_MAE_without_monetization
new_axis_proposed:
  - C26_monetization_retention_margin_bridge_required_shadow_only
  - C26_ad_theme_local_4B_watch_guard_shadow_only
  - C26_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C26
  - full_4b_requires_non_price_evidence within C26
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
3. Confirm R8 / L8 / C26 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided C26 top-covered symbols.
6. If aggregate support remains stable after exact evidence URL repair, consider C26-scoped safe patch candidates:
   - C26_monetization_retention_margin_bridge_required
   - C26_ad_theme_local_4B_watch_guard
   - C26_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R8
completed_loop = 85
next_round = R9
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE.
```
