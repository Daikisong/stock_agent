# E2R Stock-Web v12 Residual Research — R8 Loop 87 / L8 / C27

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R8
loop: 87
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_IP_GLOBAL_LAUNCH_MONETIZATION_BRIDGE_VS_ENTERTAINMENT_ARTIST_IP_PLATFORM_THEME_DECAY
sector: platform / content / game IP / entertainment IP / global monetization
output_file: e2r_stock_web_v12_residual_round_R8_loop_87_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R7 loop 87`.

```text
scheduled_round = R8
scheduled_loop = 87
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
```

R8 is restricted to platform / content / software / security.  
C27 is selected because recent R8 loops already used C26 platform/ad-revenue operating leverage and C28 software/security contract retention. C27 is the content-IP global monetization bucket.

The No-Repeat Index shows C27 as:

```text
C27_CONTENT_IP_GLOBAL_MONETIZATION
rows = 39
symbols = 15
good/bad Stage2 = 20/6
4B/4C = 3/1
top-covered = 263750, 112040, 122870, 293490, 259960, 376300
```

This loop avoids the top-covered list and also avoids the immediately previous R8 loop symbols:

```text
R8 loop85 C26: 067160, 089600, 123570
R8 loop86 C28: 030520, 053800, 049480
```

Selected symbols:

```text
251270, 035900, 352820
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"251270","company_name":"넷마블","profile_path":"atlas/symbol_profiles/251/251270.json","first_date":"2017-05-12","last_date":"2026-02-20","trading_day_count":2152,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"035900","company_name":"JYP Ent.","profile_path":"atlas/symbol_profiles/035/035900.json","first_date":"2001-08-30","last_date":"2026-02-20","trading_day_count":5935,"corporate_action_candidate_count":13,"corporate_action_candidate_dates":["2003-09-23","2004-05-24","2004-08-25","2004-09-02","2005-01-20","2005-04-21","2006-07-07","2007-10-04","2007-10-23","2008-04-28","2010-09-17","2011-01-20","2013-10-31"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"352820","company_name":"하이브","profile_path":"atlas/symbol_profiles/352/352820.json","first_date":"2020-10-15","last_date":"2026-02-20","trading_day_count":1312,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"251270","trigger_type":"Stage2-Actionable-GameIPGlobalLaunchMonetizationBridge-Positive","entry_date":"2024-04-29","duplicate_status":"new C27 symbol/trigger/date combination outside top-covered and previous R8 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"035900","trigger_type":"Stage2-FalsePositive-ArtistIPScheduleTheme-NoGlobalMonetizationMarginBridge","entry_date":"2024-01-02","duplicate_status":"new C27 symbol/trigger/date combination outside top-covered and previous R8 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"352820","trigger_type":"Stage2-FalsePositive-EntertainmentPlatformIPTheme-NoArtistStabilityMarginBridge","entry_date":"2024-04-01","duplicate_status":"new C27 symbol/trigger/date combination outside top-covered and previous R8 loop symbols"}
```

## 4. Research question

C27 is not “content or IP stock is famous.”  
The useful content-IP signal is the conversion bridge: launch hit ratio, global MAU or paying users, ARPPU/ARPDAU, live-service retention, artist schedule visibility, catalog monetization, platform take-rate, margin leverage, and cash conversion. Fame is not enough; a loud fandom is only a stadium. E2R needs to see ticketing, retention, and margins at the gate.

Residual question:

```text
Can C27 distinguish:
1. game-IP global launch and monetization bridge with strong MFE and shallow MAE,
2. artist/IP schedule theme where global monetization and margin bridge fail,
3. entertainment-platform IP theme where artist stability, catalog monetization and margin conversion are missing?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C27_R8L87_251270_NETMARBLE_GAME_IP_MONETIZATION","symbol":"251270","company_name":"넷마블","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LAUNCH_MONETIZATION_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-GameIPGlobalLaunchMonetizationBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_shallow_90D_MAE_later_fade","current_profile_verdict":"current_profile_correct_if_IP_launch_monetization_bridge_required","price_source":"Songdaiki/stock-web","notes":"Game-IP launch and monetization proxy produced a strong 30D/90D MFE with shallow initial MAE. Later fade keeps Green strict unless retention, paying-user and margin evidence are exact-repaired."}
{"row_type":"case","case_id":"C27_R8L87_035900_JYP_ARTIST_IP_THEME_DECAY","symbol":"035900","company_name":"JYP Ent.","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"ARTIST_IP_SCHEDULE_THEME_WITHOUT_GLOBAL_MONETIZATION_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ArtistIPScheduleTheme-NoGlobalMonetizationMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_artist_IP_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Artist/IP schedule theme had only a small early MFE and then deep MAE when global monetization, catalog margin and schedule-quality bridge did not confirm."}
{"row_type":"case","case_id":"C27_R8L87_352820_HYBE_PLATFORM_IP_THEME_NO_MARGIN","symbol":"352820","company_name":"하이브","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"ENTERTAINMENT_PLATFORM_IP_THEME_WITHOUT_ARTIST_STABILITY_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-EntertainmentPlatformIPTheme-NoArtistStabilityMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_platform_IP_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Entertainment-platform IP rebound had low MFE and large MAE when artist-stability, platform take-rate and margin-conversion bridge weakened."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 251270 넷마블 — game IP global launch / monetization bridge positive

Entry row: `2024-04-29 c=55500`.  
Observed path: entry-day low `53700`, high `2024-05-10 h=72400`, later lows `2024-06-24 l=52400` and `2024-11-15 l=46100`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L87_C27_251270_20240429_STAGE2_GAME_IP_GLOBAL_MONETIZATION","case_id":"C27_R8L87_251270_NETMARBLE_GAME_IP_MONETIZATION","symbol":"251270","company_name":"넷마블","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LAUNCH_MONETIZATION_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-GameIPGlobalLaunchMonetizationBridge-Positive","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":55500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_game_IP_launch_global_monetization_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; game-IP launch, global monetization and operating-leverage bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["global_launch_proxy","IP_monetization_proxy","paying_user_or_revenue_rank_proxy","relative_strength_turn"],"stage3_evidence_fields":["retention_metric_pending","ARPPU_ARPDAU_pending","margin_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","late_fade_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/251/251270/2024.csv","profile_path":"atlas/symbol_profiles/251/251270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":30.45,"MFE_90D_pct":30.45,"MFE_180D_pct":30.45,"MAE_30D_pct":-3.24,"MAE_90D_pct":-5.59,"MAE_180D_pct":-16.94,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-10","peak_price":72400.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":46100.0,"drawdown_after_peak_pct":-36.33,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B_without_retention_and_margin_slowdown_evidence; later fade blocks Green","four_b_evidence_type":["price_only","late_fade_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_shallow_90D_MAE_later_fade","current_profile_verdict":"current_profile_correct_if_IP_launch_monetization_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"251270_2024-04-29_55500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C27 can allow Stage2/Yellow when content strength is tied to global launch, paying-user/revenue rank, retention and margin bridge. Green still requires exact retention, ARPPU/ARPDAU and margin evidence."}
```

### 6.2 035900 JYP Ent. — artist/IP schedule theme without global monetization and margin bridge

Entry row: `2024-01-02 c=101400`.  
Observed path: early high `2024-01-05 h=106000`, then lows `2024-03-07 l=66300` and `2024-09-24 l=45300`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L87_C27_035900_20240102_STAGE2_FALSE_POSITIVE_ARTIST_IP_THEME","case_id":"C27_R8L87_035900_JYP_ARTIST_IP_THEME_DECAY","symbol":"035900","company_name":"JYP Ent.","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"ARTIST_IP_SCHEDULE_THEME_WITHOUT_GLOBAL_MONETIZATION_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-ArtistIPScheduleTheme-NoGlobalMonetizationMarginBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":101400.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_artist_IP_schedule_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; artist/IP schedule theme treated as insufficient without album/tour sell-through, global catalog monetization and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["artist_IP_schedule_theme","relative_strength_legacy_leader"],"stage3_evidence_fields":["global_monetization_bridge_missing","tour_album_sellthrough_missing","margin_bridge_missing","catalog_platform_take_rate_missing"],"stage4b_evidence_fields":["price_only_local_peak","monetization_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035900/2024.csv","profile_path":"atlas/symbol_profiles/035/035900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.54,"MFE_90D_pct":4.54,"MFE_180D_pct":4.54,"MAE_30D_pct":-19.63,"MAE_90D_pct":-34.62,"MAE_180D_pct":-55.33,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-05","peak_price":106000.0,"max_drawdown_low_date":"2024-09-24","max_drawdown_low":45300.0,"drawdown_after_peak_pct":-57.26,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"artist_IP_schedule_theme_without_global_monetization_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","monetization_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_artist_IP_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"035900_2024-01-02_101400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C27 should not upgrade artist/IP schedule labels without global monetization, sell-through and margin bridge. Low MFE and deep MAE force Watch/4B-risk routing."}
```

### 6.3 352820 하이브 — entertainment-platform IP theme without artist-stability and margin bridge

Entry row: `2024-04-01 c=226500`.  
Observed path: local high `2024-04-22 h=238500`, then lows `2024-07-24 l=177200`, `2024-08-05 l=160000`, and `2024-09-23 l=157700`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L87_C27_352820_20240401_STAGE2_FALSE_POSITIVE_PLATFORM_IP_THEME","case_id":"C27_R8L87_352820_HYBE_PLATFORM_IP_THEME_NO_MARGIN","symbol":"352820","company_name":"하이브","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"ENTERTAINMENT_PLATFORM_IP_THEME_WITHOUT_ARTIST_STABILITY_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-EntertainmentPlatformIPTheme-NoArtistStabilityMarginBridge","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":226500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_entertainment_platform_IP_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; entertainment platform/IP theme treated as insufficient without artist schedule stability, catalog monetization, platform take-rate and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["platform_IP_theme","entertainment_catalog_rebound"],"stage3_evidence_fields":["artist_stability_bridge_missing","platform_take_rate_missing","catalog_monetization_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","artist_stability_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/352/352820/2024.csv","profile_path":"atlas/symbol_profiles/352/352820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.30,"MFE_90D_pct":5.30,"MFE_180D_pct":5.30,"MAE_30D_pct":-11.79,"MAE_90D_pct":-21.77,"MAE_180D_pct":-30.38,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-22","peak_price":238500.0,"max_drawdown_low_date":"2024-09-23","max_drawdown_low":157700.0,"drawdown_after_peak_pct":-33.88,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"platform_IP_theme_without_artist_stability_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","artist_stability_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_platform_IP_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"352820_2024-04-01_226500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C27 should not promote entertainment-platform/IP theme without artist schedule stability, platform take-rate, catalog monetization and margin bridge. Low MFE and high MAE support Watch/4B-risk."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C27_R8L87_251270_NETMARBLE_GAME_IP_MONETIZATION","trigger_id":"R8L87_C27_251270_20240429_STAGE2_GAME_IP_GLOBAL_MONETIZATION","symbol":"251270","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C27 requires global launch, retention and monetization bridge rather than IP theme alone","raw_component_scores_before":{"IP_quality_score":12,"global_launch_score":13,"monetization_score":12,"retention_score":8,"platform_take_rate_or_margin_score":9,"cash_conversion_score":6,"relative_strength_score":12,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"IP_quality_score":15,"global_launch_score":16,"monetization_score":15,"retention_score":11,"platform_take_rate_or_margin_score":11,"cash_conversion_score":8,"relative_strength_score":13,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Global launch and monetization bridge plus high MFE support Yellow-watch; late fade and proxy-only retention evidence block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C27_R8L87_035900_JYP_ARTIST_IP_THEME_DECAY","trigger_id":"R8L87_C27_035900_20240102_STAGE2_FALSE_POSITIVE_ARTIST_IP_THEME","symbol":"035900","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"artist/IP schedule theme without monetization and margin bridge should be blocked","raw_component_scores_before":{"IP_quality_score":9,"global_launch_score":2,"monetization_score":2,"retention_score":1,"platform_take_rate_or_margin_score":1,"cash_conversion_score":0,"relative_strength_score":8,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"IP_quality_score":3,"global_launch_score":0,"monetization_score":0,"retention_score":0,"platform_take_rate_or_margin_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE convert artist/IP theme into missing monetization/margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C27_R8L87_352820_HYBE_PLATFORM_IP_THEME_NO_MARGIN","trigger_id":"R8L87_C27_352820_20240401_STAGE2_FALSE_POSITIVE_PLATFORM_IP_THEME","symbol":"352820","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"platform/IP rebound without artist stability and margin bridge should stay Watch/blocked","raw_component_scores_before":{"IP_quality_score":8,"global_launch_score":2,"monetization_score":3,"retention_score":2,"platform_take_rate_or_margin_score":1,"cash_conversion_score":1,"relative_strength_score":8,"valuation_repricing_score":4,"execution_risk_score":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":10,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"IP_quality_score":2,"global_launch_score":0,"monetization_score":0,"retention_score":0,"platform_take_rate_or_margin_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and high MAE require artist stability, take-rate and margin bridge before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R8L87_C27_P0_CURRENT","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C27 needs explicit monetization, retention, artist stability, take-rate and margin bridge taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":13.43,"avg_MAE90_pct":-20.66,"avg_MFE180_pct":13.43,"avg_MAE180_pct":-34.22,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C27_monetization_retention_margin_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R8L87_C27_P1_SECTOR_SPECIFIC","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_id":"P1_L8_content_IP_monetization_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L8 content/IP signals need global launch, paying-user revenue, retention, artist schedule quality, platform take-rate or margin bridge before Stage2-Actionable","changed_axes":["global_monetization_required","retention_margin_required","IP_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_global_launch_monetization_retention_take_rate_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":13.43,"avg_MAE90_pct":-20.66,"avg_MFE180_pct":13.43,"avg_MAE180_pct":-34.22,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R8L87_C27_P2_CANONICAL","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_id":"P2_C27_monetization_retention_margin_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C27 should reward monetization mechanics, not content/artist/platform theme labels","changed_axes":["C27_monetization_retention_bridge_required","C27_artist_IP_theme_local_4B_guard","C27_high_MAE_guard"],"changed_thresholds":{"stage2_yellow_gate":"IP_quality_plus_monetization_or_retention_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":13.43,"avg_MAE90_pct":-20.66,"avg_MFE180_pct":13.43,"avg_MAE180_pct":-34.22,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R8L87_C27_P3_COUNTEREXAMPLE_GUARD","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_id":"P3_C27_low_MFE_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-20 while monetization/retention bridge is missing, block Yellow/Green","changed_axes":["C27_low_MFE_guardrail","C27_high_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_20"},"eligible_trigger_count":3,"avg_MFE90_pct":13.43,"avg_MAE90_pct":-20.66,"avg_MFE180_pct":13.43,"avg_MAE180_pct":-34.22,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_IP_MONETIZATION_VS_ENTERTAINMENT_IP_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":13.43,"avg_MAE90_pct":-20.66,"avg_MFE180_pct":13.43,"avg_MAE180_pct":-34.22,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C27 needs bridge discipline. 넷마블 shows game-IP global launch/monetization can support a Yellow-watch rerating, while JYP Ent. and 하이브 show artist/platform IP themes can fail when global monetization, retention, artist stability, take-rate and margin bridge are missing."}
{"row_type":"stage_transition_summary","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"251270","trigger_type":"Stage2-Actionable-GameIPGlobalLaunchMonetizationBridge-Positive","entry_date":"2024-04-29","stage2_to_90D_outcome":"good_stage2_high_MFE_shallow_MAE","stage2_to_180D_outcome":"watch_positive_with_later_fade","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when global launch, paying-user monetization and retention bridge exists; Green requires exact retention and margin evidence."}
{"row_type":"stage_transition_summary","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"035900","trigger_type":"Stage2-FalsePositive-ArtistIPScheduleTheme-NoGlobalMonetizationMarginBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_artist_IP_theme_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Artist/IP schedule theme without global monetization and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"352820","trigger_type":"Stage2-FalsePositive-EntertainmentPlatformIPTheme-NoArtistStabilityMarginBridge","entry_date":"2024-04-01","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_platform_IP_theme_high_180D_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Entertainment-platform IP theme without artist stability, platform take-rate and margin bridge should stay Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","residual_type":"content_IP_theme_overcredit_without_global_monetization_retention_margin_bridge","contribution":"Adds two C27 local 4B/high-MAE counterexamples against one game-IP monetization positive, avoiding C27 top-covered and previous R8 C26/C28 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LAUNCH_MONETIZATION_BRIDGE_VS_ENTERTAINMENT_ARTIST_IP_PLATFORM_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C27 now has non-top-symbol game-IP positive and entertainment/artist-IP theme counterexamples; next R8 loops should exact-URL repair launch rank, retention, paying-user monetization, platform take-rate, artist stability, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","axis":"C27_global_monetization_retention_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"251270 worked when global launch/monetization proxy was present; 035900 and 352820 failed when content/artist/platform IP theme lacked retention, monetization and margin bridge."}
{"row_type":"shadow_weight","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","axis":"C27_artist_platform_IP_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Artist/platform IP theme rows showed low MFE and deep or high MAE without non-price monetization bridge."}
{"row_type":"shadow_weight","round":"R8","loop":"87","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","axis":"C27_low_MFE_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and MAE90<=-20 while monetization/retention bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - content_IP_theme_overcredit
  - global_monetization_bridge_missing
  - retention_take_rate_bridge_missing
  - artist_stability_margin_bridge_missing
new_axis_proposed:
  - C27_global_monetization_retention_margin_bridge_required_shadow_only
  - C27_artist_platform_IP_theme_local_4B_watch_guard_shadow_only
  - C27_low_MFE_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C27
  - full_4b_requires_non_price_evidence within C27
  - hard_4c_thesis_break_routes_to_4c within C27
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
3. Confirm R8 / L8 / C27 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C27 top-covered symbols
   - previous R8 loop85 C26 symbols
   - previous R8 loop86 C28 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C27-scoped safe patch candidates:
   - C27_global_monetization_retention_margin_bridge_required
   - C27_artist_platform_IP_theme_local_4B_watch_guard
   - C27_low_MFE_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R8
completed_loop = 87
next_round = R9
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.
```
