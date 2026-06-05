# E2R Stock-Web v12 Residual Research — R8 Loop 88 / L8 / C26

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R8
loop: 88
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: PERFORMANCE_MARKETING_PLATFORM_MARGIN_BRIDGE_VS_AD_TECH_THEME_AND_LEGACY_AGENCY_DECAY
sector: platform / ad revenue / performance marketing / ad-tech / operating leverage
output_file: e2r_stock_web_v12_residual_round_R8_loop_88_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R7 loop 88`.

```text
scheduled_round = R8
scheduled_loop = 88
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

R8 is restricted to platform / content / software / security.  
C26 is selected because the recent R8 sequence already covered:

```text
R8 loop85: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
R8 loop86: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
R8 loop87: C27_CONTENT_IP_GLOBAL_MONETIZATION
```

C26 remains under-covered and error-prone because ad-revenue and platform names can show sudden price pulses without operating leverage. The latest R13 cross-review also stressed that high or local MFE must not become positive evidence when the revenue, margin and retention bridge is missing.

No-Repeat Index snapshot:

```text
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
rows = 13
symbols = 10
good/bad Stage2 = 2/6
4B/4C = 0/1
top-covered = 042000, 214270, 237820, 030000, 035420, 035720
```

This loop avoids the C26 top-covered symbols and also avoids the prior R8 loop symbols:

```text
R8 loop85 C26: 067160, 089600, 123570
R8 loop86 C28: 030520, 053800, 049480
R8 loop87 C27: 251270, 035900, 352820
```

Selected symbols:

```text
230360, 216050, 273060
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"230360","company_name":"에코마케팅","profile_path":"atlas/symbol_profiles/230/230360.json","first_date":"2016-08-08","last_date":"2026-02-20","trading_day_count":2338,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2018-02-23","2018-03-16","2020-08-20","2020-09-10"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"216050","company_name":"인크로스","profile_path":"atlas/symbol_profiles/216/216050.json","first_date":"2016-10-31","last_date":"2026-02-20","trading_day_count":2283,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2017-11-14","2017-12-04","2022-07-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"273060","company_name":"와이즈버즈","profile_path":"atlas/symbol_profiles/273/273060.json","first_date":"2017-08-07","last_date":"2026-02-20","trading_day_count":1999,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2020-08-05"],"has_major_raw_discontinuity":true,"calibration_caveat":"SPAC/name-change corporate-action candidate exists before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"230360","trigger_type":"Stage2-Actionable-PerformanceMarketingOperatingLeverageBridge-Positive","entry_date":"2024-03-14","duplicate_status":"new C26 symbol/trigger/date combination outside top-covered and previous R8 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"216050","trigger_type":"Stage2-FalsePositive-LegacyAdPlatformRebound-NoRevenueMarginRetentionBridge","entry_date":"2024-01-11","duplicate_status":"new C26 symbol/trigger/date combination outside top-covered and previous R8 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"273060","trigger_type":"Stage2-FalsePositive-AdTechThemeBlowoff-NoOperatingLeverageBridge","entry_date":"2024-02-20","duplicate_status":"new C26 symbol/trigger/date combination outside top-covered and previous R8 loop symbols"}
```

## 4. Research question

C26 is not “광고 플랫폼이 튀었다.”  
The useful ad-platform signal must show a bridge from traffic and ad budget to economics: gross-billing recovery, advertiser retention, take-rate stability, performance-marketing ROAS, operating leverage, mix improvement, margin expansion, and cash conversion. Without that bridge, a spike in the chart is a banner impression, not a completed conversion.

Residual question:

```text
Can C26 distinguish:
1. performance-marketing / platform operating-leverage bridge with good MFE and tolerable early MAE,
2. legacy ad-platform rebound where advertiser budget, retention, take-rate and margin bridge fail,
3. ad-tech theme blowoff where MFE exists but is price-only and forward MAE exposes missing operating leverage?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C26_R8L88_230360_ECOMARKETING_OPERATING_LEVERAGE","symbol":"230360","company_name":"에코마케팅","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PERFORMANCE_MARKETING_PLATFORM_OPERATING_LEVERAGE_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-PerformanceMarketingOperatingLeverageBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_low_90D_MAE_late_drawdown","current_profile_verdict":"current_profile_correct_if_revenue_margin_retention_bridge_required","price_source":"Songdaiki/stock-web","notes":"Performance marketing / platform operating leverage proxy produced MFE90 above 35% with low early MAE. Later drawdown keeps Green strict."}
{"row_type":"case","case_id":"C26_R8L88_216050_INCROSS_LEGACY_AD_PLATFORM_DECAY","symbol":"216050","company_name":"인크로스","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LEGACY_AD_PLATFORM_REBOUND_WITHOUT_REVENUE_MARGIN_RETENTION_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LegacyAdPlatformRebound-NoRevenueMarginRetentionBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_legacy_ad_platform_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Legacy ad-platform rebound had tiny MFE and high MAE without advertiser retention, take-rate, revenue growth and margin bridge."}
{"row_type":"case","case_id":"C26_R8L88_273060_WISEBIRDS_ADTECH_BLOWOFF","symbol":"273060","company_name":"와이즈버즈","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"ADTECH_THEME_BLOWOFF_WITHOUT_OPERATING_LEVERAGE_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-AdTechThemeBlowoff-NoOperatingLeverageBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_only_MFE_but_high_MAE","current_profile_verdict":"current_profile_false_positive_if_adtech_theme_blowoff_overcredited","price_source":"Songdaiki/stock-web","notes":"Ad-tech theme blowoff had local MFE but then deep MAE without advertiser retention, revenue quality, margin and cash bridge. This is a price-only 4B case."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 230360 에코마케팅 — performance marketing / platform operating leverage positive

Entry row: `2024-03-14 c=10930`.  
Observed path: entry-day low `10500`, high `2024-04-17 h=14990`, and later low `2024-11-13 l=8720`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L88_C26_230360_20240314_STAGE2_PERFORMANCE_MARKETING_LEVERAGE","case_id":"C26_R8L88_230360_ECOMARKETING_OPERATING_LEVERAGE","symbol":"230360","company_name":"에코마케팅","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PERFORMANCE_MARKETING_PLATFORM_OPERATING_LEVERAGE_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-PerformanceMarketingOperatingLeverageBridge-Positive","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":10930.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_performance_marketing_platform_operating_leverage_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; ad-revenue recovery, performance marketing operating leverage and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["ad_budget_recovery_proxy","performance_marketing_ROAS_proxy","operating_leverage_proxy","relative_strength_turn"],"stage3_evidence_fields":["advertiser_retention_pending","take_rate_stability_pending","gross_billing_quality_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/230/230360/2024.csv","profile_path":"atlas/symbol_profiles/230/230360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":37.15,"MFE_90D_pct":37.15,"MFE_180D_pct":37.15,"MAE_30D_pct":-3.93,"MAE_90D_pct":-3.93,"MAE_180D_pct":-20.22,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-17","peak_price":14990.0,"max_drawdown_low_date":"2024-11-13","max_drawdown_low":8720.0,"drawdown_after_peak_pct":-41.83,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B; late drawdown blocks Green without exact revenue/retention/margin evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_low_90D_MAE_late_drawdown","current_profile_verdict":"current_profile_correct_if_revenue_margin_retention_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"230360_2024-03-14_10930","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C26 can allow Stage2/Yellow when platform strength is tied to advertiser retention, billing quality, take-rate stability, ROAS and margin bridge. Green still requires exact evidence."}
```

### 6.2 216050 인크로스 — legacy ad-platform rebound without revenue/margin/retention bridge

Entry row: `2024-01-11 c=12010`.  
Observed path: local high `2024-01-12 h=12260`, then lows `2024-04-19 l=8900`, autumn lows near `6700`, and weak late-year recovery.

```jsonl
{"row_type":"trigger","trigger_id":"R8L88_C26_216050_20240111_STAGE2_FALSE_POSITIVE_LEGACY_AD_PLATFORM","case_id":"C26_R8L88_216050_INCROSS_LEGACY_AD_PLATFORM_DECAY","symbol":"216050","company_name":"인크로스","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LEGACY_AD_PLATFORM_REBOUND_WITHOUT_REVENUE_MARGIN_RETENTION_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-LegacyAdPlatformRebound-NoRevenueMarginRetentionBridge","trigger_date":"2024-01-11","entry_date":"2024-01-11","entry_price":12010.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_legacy_ad_platform_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; ad-platform rebound treated as insufficient without advertiser retention, take-rate stability, gross billing recovery and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["legacy_ad_platform_rebound","relative_strength_local_rebound"],"stage3_evidence_fields":["advertiser_retention_missing","gross_billing_growth_missing","take_rate_margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","revenue_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/216/216050/2024.csv","profile_path":"atlas/symbol_profiles/216/216050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.08,"MFE_90D_pct":2.08,"MFE_180D_pct":2.08,"MAE_30D_pct":-10.57,"MAE_90D_pct":-25.90,"MAE_180D_pct":-44.21,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-12","peak_price":12260.0,"max_drawdown_low_date":"2024-10-07","max_drawdown_low":6700.0,"drawdown_after_peak_pct":-45.35,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"legacy_ad_platform_rebound_without_revenue_margin_retention_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","revenue_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_legacy_ad_platform_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"216050_2024-01-11_12010","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C26 should not promote legacy ad-platform rebounds without advertiser retention, gross billing recovery, take-rate and margin/cash bridge. Tiny MFE and high MAE route to 4B-watch."}
```

### 6.3 273060 와이즈버즈 — ad-tech theme blowoff without operating-leverage bridge

Entry row: `2024-02-20 c=1446`.  
Observed path: local event high `2024-03-06 h=1834`, then low `2024-04-11 l=1155`, autumn lows below 910, and year-end low `2024-12-24 l=710`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L88_C26_273060_20240220_STAGE2_FALSE_POSITIVE_ADTECH_THEME_BLOWOFF","case_id":"C26_R8L88_273060_WISEBIRDS_ADTECH_BLOWOFF","symbol":"273060","company_name":"와이즈버즈","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"ADTECH_THEME_BLOWOFF_WITHOUT_OPERATING_LEVERAGE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate;price_only_blowoff_stress_test","trigger_type":"Stage2-FalsePositive-AdTechThemeBlowoff-NoOperatingLeverageBridge","trigger_date":"2024-02-20","entry_date":"2024-02-20","entry_price":1446.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_adtech_theme_blowoff_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; ad-tech theme blowoff treated as insufficient without advertiser retention, billing growth, margin leverage and cash conversion","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["adtech_theme_blowoff","relative_strength_spike"],"stage3_evidence_fields":["advertiser_retention_missing","billing_growth_quality_missing","operating_leverage_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","operating_leverage_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/273/273060/2024.csv","profile_path":"atlas/symbol_profiles/273/273060.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.83,"MFE_90D_pct":26.83,"MFE_180D_pct":26.83,"MAE_30D_pct":-20.12,"MAE_90D_pct":-20.12,"MAE_180D_pct":-45.09,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-06","peak_price":1834.0,"max_drawdown_low_date":"2024-11-14","max_drawdown_low":794.0,"drawdown_after_peak_pct":-56.71,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"adtech_theme_price_blowoff_without_operating_leverage_bridge_should_be_4B_watch_not_positive_even_with_MFE","four_b_evidence_type":["price_only","operating_leverage_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_only_MFE_but_high_MAE","current_profile_verdict":"current_profile_false_positive_if_adtech_theme_blowoff_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"273060_2024-02-20_1446","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C26 should not count ad-tech theme MFE as positive evidence when advertiser retention, billing quality, operating leverage and margin/cash bridge are missing. This is a price-only 4B blowoff row."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C26_R8L88_230360_ECOMARKETING_OPERATING_LEVERAGE","trigger_id":"R8L88_C26_230360_20240314_STAGE2_PERFORMANCE_MARKETING_LEVERAGE","symbol":"230360","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C26 requires advertiser retention, billing quality, take-rate and margin bridge rather than platform/ad theme alone","raw_component_scores_before":{"ad_revenue_recovery_score":12,"advertiser_retention_score":10,"gross_billing_quality_score":10,"take_rate_score":8,"operating_leverage_score":12,"margin_bridge_score":9,"cash_conversion_score":6,"relative_strength_score":12,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"ad_revenue_recovery_score":15,"advertiser_retention_score":13,"gross_billing_quality_score":13,"take_rate_score":10,"operating_leverage_score":15,"margin_bridge_score":11,"cash_conversion_score":8,"relative_strength_score":13,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Revenue/margin operating-leverage bridge plus MFE90>35 supports Yellow-watch; late drawdown and proxy-only evidence block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C26_R8L88_216050_INCROSS_LEGACY_AD_PLATFORM_DECAY","trigger_id":"R8L88_C26_216050_20240111_STAGE2_FALSE_POSITIVE_LEGACY_AD_PLATFORM","symbol":"216050","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"legacy ad-platform rebound without retention and margin bridge should be blocked","raw_component_scores_before":{"ad_revenue_recovery_score":2,"advertiser_retention_score":0,"gross_billing_quality_score":1,"take_rate_score":1,"operating_leverage_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":5,"valuation_repricing_score":2,"execution_risk_score":-14,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"ad_revenue_recovery_score":0,"advertiser_retention_score":0,"gross_billing_quality_score":0,"take_rate_score":0,"operating_leverage_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and high MAE convert legacy ad-platform rebound into missing bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C26_R8L88_273060_WISEBIRDS_ADTECH_BLOWOFF","trigger_id":"R8L88_C26_273060_20240220_STAGE2_FALSE_POSITIVE_ADTECH_THEME_BLOWOFF","symbol":"273060","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"ad-tech theme blowoff without advertiser retention and operating leverage should be 4B-watch even when local MFE is high","raw_component_scores_before":{"ad_revenue_recovery_score":3,"advertiser_retention_score":0,"gross_billing_quality_score":1,"take_rate_score":1,"operating_leverage_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":14,"valuation_repricing_score":5,"execution_risk_score":-16,"theme_spike_risk":-20,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"ad_revenue_recovery_score":0,"advertiser_retention_score":0,"gross_billing_quality_score":0,"take_rate_score":0,"operating_leverage_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Local MFE is price-only; high MAE and missing revenue/margin bridge block Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R8L88_C26_P0_CURRENT","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C26 needs explicit advertiser retention, billing quality, take-rate, operating leverage and margin/cash bridge taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":22.02,"avg_MAE90_pct":-16.65,"avg_MFE180_pct":22.02,"avg_MAE180_pct":-36.51,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C26_revenue_margin_operating_leverage_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R8L88_C26_P1_SECTOR_SPECIFIC","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_id":"P1_L8_platform_ad_revenue_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L8 platform/ad signals need advertiser retention, gross billing recovery, take-rate stability, ROAS, operating leverage or margin/cash bridge before Stage2-Actionable","changed_axes":["ad_revenue_quality_required","advertiser_retention_required","adtech_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_retention_billing_take_rate_ROAS_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":22.02,"avg_MAE90_pct":-16.65,"avg_MFE180_pct":22.02,"avg_MAE180_pct":-36.51,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R8L88_C26_P2_CANONICAL","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_id":"P2_C26_revenue_margin_operating_leverage_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C26 should reward revenue-to-margin mechanics, not ad-tech or legacy platform theme labels","changed_axes":["C26_revenue_margin_retention_bridge_required","C26_adtech_theme_local_4B_guard","C26_price_only_MFE_not_positive_guard"],"changed_thresholds":{"stage2_yellow_gate":"advertiser_retention_or_billing_quality_plus_margin_or_take_rate_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":22.02,"avg_MAE90_pct":-16.65,"avg_MFE180_pct":22.02,"avg_MAE180_pct":-36.51,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R8L88_C26_P3_COUNTEREXAMPLE_GUARD","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_id":"P3_C26_price_only_high_MFE_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If bridge is missing and MAE90<=-20, route to Watch/4B even if MFE90>=20; if MFE90<5 and MAE90<=-20, hard-block Yellow/Green","changed_axes":["C26_price_only_MFE_guardrail","C26_low_MFE_high_MAE_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_MAE90_le_minus_20; hard_block_if_MFE90_lt_5_and_MAE90_le_minus_20"},"eligible_trigger_count":3,"avg_MFE90_pct":22.02,"avg_MAE90_pct":-16.65,"avg_MFE180_pct":22.02,"avg_MAE180_pct":-36.51,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_PERFORMANCE_MARKETING_POSITIVE_VS_ADTECH_LEGACY_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":22.02,"avg_MAE90_pct":-16.65,"avg_MFE180_pct":22.02,"avg_MAE180_pct":-36.51,"stage2_hit_rate_MFE90_ge_20":0.67,"stage2_bad_entry_rate_bridge_missing_MAE90_le_minus20":0.67,"interpretation":"C26 needs bridge discipline. 에코마케팅 shows performance marketing and operating-leverage bridge can support Yellow-watch, while 인크로스 and 와이즈버즈 show legacy ad-platform and ad-tech theme strength should not be promoted without advertiser retention, billing quality, take-rate, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"230360","trigger_type":"Stage2-Actionable-PerformanceMarketingOperatingLeverageBridge-Positive","entry_date":"2024-03-14","stage2_to_90D_outcome":"good_stage2_high_MFE_low_MAE","stage2_to_180D_outcome":"watch_positive_with_late_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when ad revenue is tied to retention, billing quality, take-rate and margin bridge; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"216050","trigger_type":"Stage2-FalsePositive-LegacyAdPlatformRebound-NoRevenueMarginRetentionBridge","entry_date":"2024-01-11","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_high_MAE","stage2_to_180D_outcome":"failed_legacy_ad_platform_decay","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Legacy ad-platform rebound without revenue/margin/retention bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"273060","trigger_type":"Stage2-FalsePositive-AdTechThemeBlowoff-NoOperatingLeverageBridge","entry_date":"2024-02-20","stage2_to_90D_outcome":"price_only_MFE_but_high_MAE","stage2_to_180D_outcome":"failed_adtech_theme_blowoff_deep_MAE","MFE90_ge_20":true,"MAE90_le_minus_20":true,"transition_note":"Ad-tech theme MFE without operating-leverage bridge should be treated as price-only 4B, not positive evidence."}
{"row_type":"residual_contribution","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","residual_type":"platform_ad_revenue_theme_overcredit_without_retention_billing_margin_bridge","contribution":"Adds one C26 performance-marketing operating-leverage positive and two 4B counterexamples, avoiding C26 top-covered and previous R8 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PERFORMANCE_MARKETING_PLATFORM_MARGIN_BRIDGE_VS_AD_TECH_THEME_AND_LEGACY_AGENCY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C26 now has non-top-symbol performance-marketing positive and legacy/ad-tech counterexamples; next R8 loops should exact-URL repair advertiser retention, gross billing quality, take-rate, ROAS, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","axis":"C26_revenue_margin_retention_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"230360 worked when revenue/margin operating-leverage proxy existed; 216050 and 273060 failed when only legacy platform or ad-tech theme existed."}
{"row_type":"shadow_weight","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","axis":"C26_adtech_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Ad-tech and legacy ad-platform rows showed missing bridge plus high MAE; one row had local MFE but still failed as price-only blowoff."}
{"row_type":"shadow_weight","round":"R8","loop":"88","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","axis":"C26_price_only_MFE_not_positive_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"273060 shows that MFE90>=20 should not be counted as positive evidence when advertiser retention, billing quality and margin bridge are missing and MAE90<=-20."}
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
  - platform_ad_revenue_theme_overcredit
  - advertiser_retention_bridge_missing
  - billing_quality_take_rate_bridge_missing
  - operating_leverage_margin_cash_bridge_missing
new_axis_proposed:
  - C26_revenue_margin_retention_bridge_required_shadow_only
  - C26_adtech_theme_local_4B_watch_guard_shadow_only
  - C26_price_only_MFE_not_positive_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C26
  - full_4b_requires_non_price_evidence within C26
  - hard_4c_thesis_break_routes_to_4c within C26
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
5. Confirm this loop avoided:
   - C26 top-covered symbols
   - previous R8 loop85 C26 symbols
   - previous R8 loop86 C28 symbols
   - previous R8 loop87 C27 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C26-scoped safe patch candidates:
   - C26_revenue_margin_retention_bridge_required
   - C26_adtech_theme_local_4B_watch_guard
   - C26_price_only_MFE_not_positive_guard
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R8
completed_loop = 88
next_round = R9
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE.
```
