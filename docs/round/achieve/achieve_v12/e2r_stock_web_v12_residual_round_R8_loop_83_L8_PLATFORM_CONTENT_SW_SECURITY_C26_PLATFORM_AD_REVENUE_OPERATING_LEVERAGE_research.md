# E2R Stock-Web v12 Residual Research — R8 Loop 83 / L8 / C26

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R8
loop: 83
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: LIVESTREAM_PLATFORM_TRAFFIC_MIGRATION_AD_OPERATING_LEVERAGE_VS_ADTECH_RECOVERY_PRICE_SPIKE
sector: 플랫폼·콘텐츠·SW·보안 / platform ad revenue operating leverage
output_file: e2r_stock_web_v12_residual_round_R8_loop_83_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the sequential v12 scheduler after the latest working-state `R7 loop 83` result.

```text
scheduled_round = R8
scheduled_loop = 83
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

This is not a live stock recommendation, not a `stock_agent` patch, and not a production scoring change. It is a standalone historical calibration note using `Songdaiki/stock-web` 1D tradable raw OHLC rows.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"067160","company_name":"SOOP","profile_path":"atlas/symbol_profiles/067/067160.json","first_date":"2003-12-19","last_date":"2026-02-20","trading_day_count":5450,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["2005-12-27","2007-06-05","2007-06-14","2008-01-24","2011-01-27"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates are historical and do not contaminate the 2024 forward windows used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"089600","company_name":"KT나스미디어","profile_path":"atlas/symbol_profiles/089/089600.json","first_date":"2013-07-17","last_date":"2026-02-20","trading_day_count":3090,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"230360","company_name":"에코마케팅","profile_path":"atlas/symbol_profiles/230/230360.json","first_date":"2016-08-08","last_date":"2026-02-20","trading_day_count":2338,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2018-02-23","2018-03-16","2020-08-20","2020-09-10"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates are historical and do not contaminate the 2024 forward windows used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger. In the latest ledger, C26 has relatively thin coverage: 13 rows, 10 symbols, good/bad Stage2 = 2/6, and 4B/4C = 0/1. The top-covered symbols include `042000`, `214270`, `237820`, `030000`, `035420`, and `035720`, so this loop avoids those and uses three new C26 symbol lanes.

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novel keys introduced here:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"067160","trigger_type":"Stage2-Actionable-LivestreamTrafficMigration-AdOperatingLeverage-Positive","entry_date":"2024-01-08","duplicate_status":"selected as new C26 positive structural bridge; exact hard key not reused"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"089600","trigger_type":"Stage2-FalsePositive-AdTechRecovery-NoOperatingLeverageBridge","entry_date":"2024-04-11","duplicate_status":"selected as new C26 ad-tech false-positive; exact hard key not reused"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"230360","trigger_type":"Stage2-FalsePositive-PerformanceMarketingRecovery-ChannelInstability","entry_date":"2024-04-11","duplicate_status":"selected as new C26 performance-marketing false-positive; exact hard key not reused"}
```

## 4. Research question

C26 should reward true platform operating leverage: traffic or ad inventory migration, monetization lift, and cost discipline that converts into earnings visibility. It should not reward every digital-ad recovery bounce. The difference is similar to a store owning the mall entrance versus a flyer distributor hoping foot traffic returns; both see more people, but only one has a durable toll booth.

Residual question for this loop:

```text
Can the current calibrated profile distinguish:
1. platform traffic migration + monetization bridge with durable MFE,
2. digital-ad recovery bounce with no operating leverage bridge,
3. performance-marketing channel rebound that round-trips into high MAE?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C26_R8L83_067160_SOOP_TRAFFIC_MIGRATION_OPERATING_LEVERAGE","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVESTREAM_PLATFORM_TRAFFIC_MIGRATION_AD_OPERATING_LEVERAGE","symbol":"067160","company_name":"SOOP","case_role":"positive_structural_success","case_summary":"Livestream platform traffic migration proxy had strong 30/90/180D MFE and controlled forward MAE; C26 should allow Stage2/Yellow only when traffic migration is tied to monetization and operating leverage bridge."}
{"row_type":"case","case_id":"C26_R8L83_089600_NASMEDIA_ADTECH_RECOVERY_FALSE_POSITIVE","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"ADTECH_RECOVERY_WITHOUT_OPERATING_LEVERAGE_BRIDGE","symbol":"089600","company_name":"KT나스미디어","case_role":"failed_rerating","case_summary":"Ad-tech recovery narrative produced almost no upside and deep 30/90/180D MAE; C26 should block Stage2/Yellow if ad-market recovery lacks margin/retention bridge."}
{"row_type":"case","case_id":"C26_R8L83_230360_ECOMARKETING_PERFORMANCE_MARKETING_ROUNDTRIP","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PERFORMANCE_MARKETING_CHANNEL_INSTABILITY_PRICE_SPIKE","symbol":"230360","company_name":"에코마케팅","case_role":"failed_rerating","case_summary":"Performance-marketing rebound had a small local MFE but then deep MAE; local 4B/watch guard should trigger when channel economics and repeat advertiser bridge are not confirmed."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 067160 SOOP — positive platform traffic migration bridge

Stock-Web profile has historical corporate-action candidates only before 2012; the 2024 forward window is clean. The entry row is `2024-01-08 c=98,800`; the 30D peak is `2024-02-15 h=126,000`, the 90D peak is `2024-02-28 h=139,600`, and the 180D peak is `2024-07-11 h=143,800`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L83_C26_067160_20240108_STAGE2_LIVESTREAM_TRAFFIC_MIGRATION_POSITIVE","case_id":"C26_R8L83_067160_SOOP_TRAFFIC_MIGRATION_OPERATING_LEVERAGE","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVESTREAM_PLATFORM_TRAFFIC_MIGRATION_AD_OPERATING_LEVERAGE","sector":"platform_content_software_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"residual_missed_structural_mining;positive_control;canonical_archetype_rule_candidate","symbol":"067160","company_name":"SOOP","trigger_type":"Stage2-Actionable-LivestreamTrafficMigration-AdOperatingLeverage-Positive","trigger_date":"2024-01-08","evidence_available_at_that_date":true,"evidence_source_type":"historical_public_event_proxy","evidence_source":"source-name-level proxy; exact URL pending; livestream traffic migration / platform monetization bridge treated as non-price proxy, not citation-grade evidence","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge_proxy","financial_visibility_proxy","repeat_order_or_conversion_proxy"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-08","entry_price":98800.0,"entry_price_basis":"close","entry_row_exists":true,"MFE_30D_pct":27.53,"MFE_90D_pct":41.30,"MFE_180D_pct":45.55,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.63,"MAE_90D_pct":-10.63,"MAE_180D_pct":-10.63,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-07-11","peak_price":143800.0,"drawdown_after_peak_pct":-39.85,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"do_not_treat_price_only_local_peak_as_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_controlled_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"C26_067160_20240108_98800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"positive_or_counterexample":"positive","reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Positive path supports a C26 bridge rule, not a global loosening: traffic migration must connect to ad monetization and operating leverage."}
```

### 6.2 089600 KT나스미디어 — ad-tech recovery false positive

Stock-Web profile is clean with no corporate-action candidate dates. The entry row is `2024-04-11 c=23,700`; the local high was `h=23,900`, while the 180D low reached `2024-11-15 l=13,720`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L83_C26_089600_20240411_STAGE2_FALSE_POSITIVE_ADTECH_RECOVERY","case_id":"C26_R8L83_089600_NASMEDIA_ADTECH_RECOVERY_FALSE_POSITIVE","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"ADTECH_RECOVERY_WITHOUT_OPERATING_LEVERAGE_BRIDGE","sector":"platform_content_software_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","symbol":"089600","company_name":"KT나스미디어","trigger_type":"Stage2-FalsePositive-AdTechRecovery-NoOperatingLeverageBridge","trigger_date":"2024-04-11","evidence_available_at_that_date":true,"evidence_source_type":"historical_public_report_consensus_proxy","evidence_source":"source-name-level proxy; exact URL pending; digital ad recovery narrative treated as insufficient unless retention/margin/operating leverage bridge is verified","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["relative_strength","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089600/2024.csv","profile_path":"atlas/symbol_profiles/089/089600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-11","entry_price":23700.0,"entry_price_basis":"close","entry_row_exists":true,"MFE_30D_pct":0.84,"MFE_90D_pct":0.84,"MFE_180D_pct":0.84,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-22.70,"MAE_90D_pct":-32.78,"MAE_180D_pct":-42.11,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-11","peak_price":23900.0,"drawdown_after_peak_pct":-42.59,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_peak_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"C26_089600_20240411_23700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"positive_or_counterexample":"counterexample","reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C26 must not equate ad-market recovery with platform operating leverage; no retention/margin bridge led to almost zero MFE and deep MAE."}
```

### 6.3 230360 에코마케팅 — performance-marketing channel instability

Stock-Web profile has old corporate-action candidates in 2018/2020 only; the 2024 forward window is clean. The entry row is `2024-04-11 c=13,880`; the 30D/90D/180D high was `2024-04-17 h=14,990`, but the 180D low reached `2024-11-13 l=8,720`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L83_C26_230360_20240411_STAGE2_FALSE_POSITIVE_PERFORMANCE_MARKETING_RECOVERY","case_id":"C26_R8L83_230360_ECOMARKETING_PERFORMANCE_MARKETING_ROUNDTRIP","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PERFORMANCE_MARKETING_CHANNEL_INSTABILITY_PRICE_SPIKE","sector":"platform_content_software_security","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"residual_false_positive_mining;4B_non_price_requirement_stress_test;counterexample_mining","symbol":"230360","company_name":"에코마케팅","trigger_type":"Stage2-FalsePositive-PerformanceMarketingRecovery-ChannelInstability","trigger_date":"2024-04-11","evidence_available_at_that_date":true,"evidence_source_type":"historical_public_report_consensus_proxy","evidence_source":"source-name-level proxy; exact URL pending; performance-marketing recovery narrative treated as insufficient unless advertiser retention and channel economics are verified","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["relative_strength","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/230/230360/2024.csv","profile_path":"atlas/symbol_profiles/230/230360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-11","entry_price":13880.0,"entry_price_basis":"close","entry_row_exists":true,"MFE_30D_pct":8.00,"MFE_90D_pct":8.00,"MFE_180D_pct":8.00,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.02,"MAE_90D_pct":-18.59,"MAE_180D_pct":-37.18,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-17","peak_price":14990.0,"drawdown_after_peak_pct":-41.83,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_4B_watch_only_without_advertiser_retention_bridge","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_small_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"C26_230360_20240411_13880","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"positive_or_counterexample":"counterexample","reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"A small local price spike did not validate durable platform leverage; C26 needs advertiser retention / channel unit-economics bridge before Yellow/Green."}
```

## 7. Score simulation rows

These are proxy rows for calibration analysis only. They do not change production scoring.

```jsonl
{"row_type":"score_simulation","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"067160","profile":"P0b_current_e2r_2_2_rolling_calibrated_proxy","eps_fcf_explosion":20,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":13,"valuation_rerating":11,"capital_allocation":4,"information_confidence":5,"raw_total_proxy":85,"weighted_total_proxy":82,"simulated_stage":"Stage2-Actionable/Stage3-Yellow-Watch","simulation_note":"Strong price path with non-price traffic migration proxy; do not loosen Green without exact URL-grade evidence."}
{"row_type":"score_simulation","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"089600","profile":"P0b_current_e2r_2_2_rolling_calibrated_proxy","eps_fcf_explosion":12,"earnings_visibility":10,"bottleneck_pricing":8,"market_mispricing":13,"valuation_rerating":7,"capital_allocation":3,"information_confidence":4,"raw_total_proxy":57,"weighted_total_proxy":55,"simulated_stage":"Stage2-Watch/FalsePositive","simulation_note":"Ad recovery without margin or retention bridge should be blocked before Yellow."}
{"row_type":"score_simulation","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"230360","profile":"P0b_current_e2r_2_2_rolling_calibrated_proxy","eps_fcf_explosion":13,"earnings_visibility":11,"bottleneck_pricing":8,"market_mispricing":14,"valuation_rerating":8,"capital_allocation":3,"information_confidence":4,"raw_total_proxy":61,"weighted_total_proxy":58,"simulated_stage":"Stage2-Watch/4B-risk","simulation_note":"Performance-marketing rebound needs advertiser retention and channel-economics bridge; otherwise local 4B watch only."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R8L83_C26_P0_VS_P3","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile":"P0_e2r_2_0_baseline","profile_role":"rollback_reference","expected_error":"Would over-credit digital-ad recovery and price momentum without separating owned-platform traffic migration from agency/ad-tech beta."}
{"row_type":"profile_comparison","comparison_id":"R8L83_C26_P0B_CURRENT","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile":"P0b_e2r_2_2_rolling_calibrated","profile_role":"current_default_proxy","expected_error":"Global guards are directionally correct, but C26 needs a local bridge requirement: monetizable traffic migration, advertiser retention, or margin/operating leverage conversion."}
{"row_type":"profile_comparison","comparison_id":"R8L83_C26_P1_BRIDGE_REQUIRED","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile":"P1_shadow_C26_platform_monetization_bridge_required","profile_role":"shadow_candidate","expected_effect":"Stage2/Yellow requires non-price monetization bridge: traffic migration, ad inventory yield, advertiser retention, or operating leverage."}
{"row_type":"profile_comparison","comparison_id":"R8L83_C26_P2_LOCAL_4B_WATCH","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile":"P2_shadow_C26_adtech_recovery_4B_watch_guard","profile_role":"shadow_candidate","expected_effect":"If MFE90 < 10 and MAE90 <= -15 for ad-tech/performance marketing recovery, keep Watch or local 4B-risk until margin/retention bridge is repaired."}
{"row_type":"profile_comparison","comparison_id":"R8L83_C26_P3_RECOMMENDED","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile":"P3_recommended_shadow_only","profile_role":"recommended_shadow_rule","expected_effect":"No production change now; record C26-scoped bridge requirement and ad-tech/performance-marketing local 4B watch guard for later batch planner."}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_PLATFORM_AD_LEVERAGE_VS_ADTECH_RECOVERY_STRESS","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":16.71,"avg_MAE90_pct":-20.67,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_15":0.67,"interpretation":"C26 has an asymmetry: owned platform traffic migration can work, but ad-tech/performance marketing recovery without retention or margin bridge creates low-MFE/high-MAE false positives."}
{"row_type":"stage_transition_summary","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"067160","trigger_type":"Stage2-Actionable-LivestreamTrafficMigration-AdOperatingLeverage-Positive","entry_date":"2024-01-08","stage2_to_90D_outcome":"good_stage2","stage2_to_180D_outcome":"positive_re_rating_path","MFE90_ge_20":true,"MAE90_le_minus_15":false,"transition_note":"Allow Stage2/Yellow watch when traffic migration is tied to monetization/operating leverage proxy; URL repair needed before promotion."}
{"row_type":"stage_transition_summary","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"089600","trigger_type":"Stage2-FalsePositive-AdTechRecovery-NoOperatingLeverageBridge","entry_date":"2024-04-11","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"4B_watch_or_counterexample","MFE90_ge_20":false,"MAE90_le_minus_15":true,"transition_note":"Ad-tech recovery without retention/margin bridge produced deep MAE; block Yellow/Green."}
{"row_type":"stage_transition_summary","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"230360","trigger_type":"Stage2-FalsePositive-PerformanceMarketingRecovery-ChannelInstability","entry_date":"2024-04-11","stage2_to_90D_outcome":"bad_stage2_roundtrip","stage2_to_180D_outcome":"4B_watch_or_counterexample","MFE90_ge_20":false,"MAE90_le_minus_15":true,"transition_note":"Small local MFE turned into deep 180D MAE; local 4B watch guard should activate."}
{"row_type":"residual_contribution","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","residual_type":"C26_platform_bridge_vs_adtech_false_positive","contribution":"Adds two C26 counterexamples and one positive structural bridge, improving the distinction between owned-platform operating leverage and ad-tech/performance-marketing beta.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_rows":3,"new_symbols":3,"new_positive":1,"new_counterexample":2,"new_4B_watch":2,"new_4C":0,"source_proxy_only":3,"evidence_url_pending":3,"calibration_usable":3,"next_gap":"Exact URL repair for traffic migration/ad monetization and advertiser-retention evidence; future R8 loops can test C28 software/security 4B/4C gap."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","axis":"platform_monetization_bridge_required","scope":"canonical_archetype","candidate_delta":0.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"SOOP positive path required traffic migration + monetization bridge; ad-tech recovery without retention/margin bridge failed."}
{"row_type":"shadow_weight","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","axis":"adtech_performance_marketing_local_4b_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"089600 and 230360 show low MFE / high MAE after ad recovery or performance marketing price spikes; require advertiser retention or operating leverage bridge before Yellow/Green."}
{"row_type":"shadow_weight","round":"R8","loop":"83","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","axis":"C26_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"Historical C26 stress trigger: if MFE90<10 and MAE90<=-15, classify as Watch/local 4B-risk unless non-price bridge is repaired."}
```

Interpretation:

```text
C26 should not mean "online ad stock went up." It should mean the platform owns a monetizable traffic choke point or a retention-backed ad/commerce loop.

Allow:
- traffic migration,
- ad inventory/yield conversion,
- advertiser retention,
- margin/operating leverage bridge.

Guard:
- ad-market recovery with no retention bridge,
- performance marketing rebound with unstable channel economics,
- price-only local peak masquerading as platform operating leverage.
```

## 11. Required output fields

```jsonl
{"row_type":"narrative_only","scheduled_round":"R8","scheduled_loop":"83","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":2,"diversity_score_summary":"C26 uses three non-top-covered symbols: 067160/SOOP positive platform traffic migration, 089600/KT나스미디어 ad-tech false positive, 230360/에코마케팅 performance-marketing roundtrip; adds two high-MAE counterexamples and one positive bridge.","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"sector_specific_rule_candidate":false,"canonical_archetype_rule_candidate":true,"existing_axis_tested":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"existing_axis_strengthened":["price_only_blowoff_blocks_positive_stage within C26","full_4b_requires_non_price_evidence within C26"],"new_axis_proposed":["C26_platform_monetization_bridge_required_shadow_only","C26_adtech_performance_marketing_local_4B_watch_guard_shadow_only"],"existing_axis_weakened":null}
```

One-line contribution:

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE.
```

## 12. Data-quality caveat

All three cases use actual Stock-Web OHLC rows and clean tradable shards. However, the non-price evidence layer is still source-name/proxy level in this MD. Therefore:

```text
- calibration_usable = true for price-path residual analysis
- evidence_url_pending = true
- source_proxy_only = true
- promotion should prefer hold / data-quality repair until exact URLs are added
```

## 13. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not execute this handoff during the research-writing session.

When a later batch implementation is requested:
1. Ingest this MD through run-v12-calibration.
2. Confirm all trigger rows validate with price_data_source=Songdaiki/stock-web, price_basis=tradable_raw, price_adjustment_status=raw_unadjusted_marcap.
3. Check that C26 rows are representative and not hard duplicates by canonical_archetype_id + symbol + trigger_type + entry_date.
4. If aggregate support remains stable after exact evidence URL repair, consider a C26-scoped safe patch:
   - platform_monetization_bridge_required for Stage2/Yellow,
   - adtech_performance_marketing_local_4b_watch_guard for ad recovery / performance marketing spikes,
   - high-MAE guard when MFE90 < 10 and MAE90 <= -15.
5. Do not loosen Stage3-Green. Do not use future MFE/MAE in runtime scoring. Use this only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R8
completed_loop = 83
next_round = R9
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```
