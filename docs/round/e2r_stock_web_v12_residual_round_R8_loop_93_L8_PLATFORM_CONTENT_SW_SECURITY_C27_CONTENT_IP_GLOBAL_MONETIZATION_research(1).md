# E2R Stock-Web v12 Residual Research — R8 Loop 93 / L8 / C27

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R8
loop: 93
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: FAN_PLATFORM_SUBSCRIPTION_IP_MONETIZATION_VS_LABEL_CONTENT_PIPELINE_AND_STUDIO_IP_DECAY
sector: platform / content / IP / entertainment / fan platform / subscription / K-pop / studio content / global monetization / margin / cash conversion
output_file: e2r_stock_web_v12_residual_round_R8_loop_93_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the current v12 coverage-index-first scheduler after local loop93 expansions in C09, C01, C07, C06, C10, C11 and C19.

```text
selected_round = R8
selected_loop = 93
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
```

Reason for selecting C27:

```text
v12 scheduler = coverage_index_first
sequential_round_cycle_required = false
coverage_gap_can_override_previous_round = true
selected_archetype_drives_round = true
```

No-Repeat Index Priority 0 snapshot used as duplicate-avoidance ledger:

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY = 14 rows
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF = 15 rows
C01_ORDER_BACKLOG_MARGIN_BRIDGE = 16 rows
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH = 18 rows
C06_HBM_MEMORY_CUSTOMER_CAPACITY = 21 rows
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE = 21 rows
C14_EV_DEMAND_SLOWDOWN_4B_4C = 21 rows
C11_BATTERY_ORDERBOOK_RERATING = 23 rows
C02_POWER_GRID_DATACENTER_CAPEX = 24 rows
C19_BRAND_RETAIL_INVENTORY_MARGIN = 24 rows
C27_CONTENT_IP_GLOBAL_MONETIZATION = 24 rows
```

Local run-stream hygiene:

```text
C19 was just expanded in loop93.
C27 is the next still-thin Priority-0 archetype outside the recently repeated semiconductor/battery/consumer C19 stream.
```

This loop avoids recent R8 symbols and top-covered C27 symbols:

```text
C27 top-covered = 035760, 251270, 035900, 194480, 419530, 036420

R8 loop85 C26: 067160, 089600, 123570
R8 loop86 C28: 030520, 053800, 049480
R8 loop87 C27: 251270, 035900, 352820
R8 loop88 C26: 230360, 216050, 273060
R8 loop89 C28: 060850, 067920, 304100
R8 loop90 C27: 035760, 241840, 206560
R8 loop91 C26: 181710, 236810, 104200
R8 loop92 C28: 012510, 150900, 042510
```

Candidate hygiene note:

```text
During this execution path, recently touched C19 and C11 candidate rows were available from the stream.
They are excluded from this C27 output because the valid output must be R8/L8/C27.
```

Selected symbols:

```text
376300, 041510, 253450
```

The selected pocket is:

```text
fan-platform subscription / artist-IP monetization / recurring revenue bridge positive-control
vs
K-pop label global-content vocabulary after a price spike without durable release-margin-cash bridge
vs
studio content pipeline / global OTT vocabulary without fresh hit-rate, licensing-margin and cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"376300","company_name":"디어유","profile_path":"atlas/symbol_profiles/376/376300.json","first_date":"2021-11-10","last_date":"2026-02-20","trading_day_count":1047,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"041510","company_name":"에스엠","profile_path":"atlas/symbol_profiles/041/041510.json","first_date":"2000-04-27","last_date":"2026-02-20","trading_day_count":6364,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2002-04-30","2005-07-08","2005-08-02"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist long before selected 2024 forward window. Visible 2024 share-count movement around March is retained as data-quality watch before patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable; share_count_movement_watch"}
{"row_type":"price_source_validation","symbol":"253450","company_name":"스튜디오드래곤","profile_path":"atlas/symbol_profiles/253/253450.json","first_date":"2017-11-24","last_date":"2026-02-20","trading_day_count":2020,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"Market flag changes from KOSDAQ to KOSDAQ GLOBAL after 2024-06-14; keep market-segment data-quality watch before patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable; market_segment_change_watch"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"376300","trigger_type":"Stage2-Actionable-FanPlatformSubscriptionArtistIPMonetizationBridge-Positive","entry_date":"2024-10-10","duplicate_status":"new C27 symbol/trigger/date combination outside C27 top-covered and recent R8 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"041510","trigger_type":"Stage2-FalsePositive-KpopLabelGlobalContentVocabularyNoDurableReleaseMarginCashBridge","entry_date":"2024-05-27","duplicate_status":"new C27 symbol/trigger/date combination outside C27 top-covered and recent R8 loop symbols; share-count watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"253450","trigger_type":"Stage2-FalsePositive-StudioContentPipelineVocabularyNoFreshHitLicensingMarginBridge","entry_date":"2024-01-02","duplicate_status":"new C27 symbol/trigger/date combination outside C27 top-covered and recent R8 loop symbols; market-segment-change watch"}
```

## 4. Research question

C27 is not “콘텐츠 IP가 있다.”
The useful content-IP monetization signal must prove the IP-to-cash chain:

```text
content or artist IP with global demand
platform / distribution channel
subscriber, ticket, licensing, MD, ad or royalty monetization path
release or content pipeline visibility
hit-rate or engagement evidence
gross-margin or operating leverage bridge
working-capital discipline
cash conversion
renewal / retention / recurring revenue where applicable
```

A content headline without this bridge is a stage with the lights on but no paying audience through the gate. E2R needs the ticket, subscription, license, margin and cash.

Residual question:

```text
Can C27 distinguish:
1. fan-platform subscription / artist-IP monetization bridge with high MFE and shallow MAE,
2. K-pop label global-content vocabulary where price spike lacked durable release-margin-cash bridge,
3. studio content pipeline / OTT vocabulary where market-segment change and missing hit-rate/licensing bridge block promotion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C27_R8L93_376300_DEARU_FAN_PLATFORM","symbol":"376300","company_name":"디어유","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"FAN_PLATFORM_SUBSCRIPTION_ARTIST_IP_MONETIZATION_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-FanPlatformSubscriptionArtistIPMonetizationBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_extreme_MFE90_low_MAE_subscription_artist_IP_bridge","current_profile_verdict":"current_profile_correct_if_subscription_retention_artist_lineup_margin_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"Fan-platform subscription / artist-IP monetization proxy after October reset produced high MFE90 with shallow MAE. Green still requires exact subscriber, artist-lineup, retention, ARPU, margin and cash evidence."}
{"row_type":"case","case_id":"C27_R8L93_041510_SM_LABEL_GLOBAL_CONTENT_DECAY","symbol":"041510","company_name":"에스엠","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_LABEL_GLOBAL_CONTENT_VOCABULARY_WITHOUT_DURABLE_RELEASE_MARGIN_CASH_BRIDGE","case_type":"failed_entry_data_quality_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-KpopLabelGlobalContentVocabularyNoDurableReleaseMarginCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"counterexample_low_MFE_deep_MAE_after_spike_no_durable_release_margin_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_Kpop_global_content_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"K-pop label/global-content vocabulary after a price burst had low forward MFE and deep later drawdown without durable release schedule, artist monetization, margin or cash bridge. 2024 share-count movement requires repair."}
{"row_type":"case","case_id":"C27_R8L93_253450_STUDIO_DRAGON_CONTENT_PIPELINE_DECAY","symbol":"253450","company_name":"스튜디오드래곤","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"STUDIO_CONTENT_PIPELINE_VOCABULARY_WITHOUT_FRESH_HIT_LICENSING_MARGIN_BRIDGE","case_type":"failed_entry_data_quality_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-StudioContentPipelineVocabularyNoFreshHitLicensingMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_no_fresh_hit_licensing_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_studio_content_pipeline_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Studio/OTT pipeline vocabulary had near-zero MFE and deep MAE without fresh hit-rate, licensing, margin or cash evidence. Market-segment change keeps data-quality watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 376300 디어유 — fan-platform subscription / artist-IP monetization bridge

Entry row: `2024-10-10 c=21550`, after a reset and renewed artist-platform monetization path.
Observed path: peak `2024-11-25 h=41950` and shallow entry-zone low `2024-10-14 l=20750`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L93_C27_376300_20241010_STAGE2_FAN_PLATFORM_SUBSCRIPTION","case_id":"C27_R8L93_376300_DEARU_FAN_PLATFORM","symbol":"376300","company_name":"디어유","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"FAN_PLATFORM_SUBSCRIPTION_ARTIST_IP_MONETIZATION_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-FanPlatformSubscriptionArtistIPMonetizationBridge-Positive","trigger_date":"2024-10-10","entry_date":"2024-10-10","entry_price":21550.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_fan_platform_subscription_artist_IP_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; fan-platform subscription, artist lineup, retention, ARPU, operating leverage and cash bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["fan_platform_subscription_proxy","artist_IP_monetization_proxy","subscriber_retention_proxy","ARPU_margin_proxy"],"stage3_evidence_fields":["exact_subscriber_source_pending","artist_lineup_source_pending","retention_ARPU_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","Green_exact_evidence_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/376/376300/2024.csv","profile_path":"atlas/symbol_profiles/376/376300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":87.94,"MFE_90D_pct":94.66,"MFE_180D_pct":94.66,"MAE_30D_pct":-3.71,"MAE_90D_pct":-3.71,"MAE_180D_pct":-3.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-25","peak_price":41950.0,"max_drawdown_low_date":"2024-10-14","max_drawdown_low":20750.0,"drawdown_after_peak_pct":-22.65,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_subscriber_artist_lineup_retention_ARPU_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","Green_exact_evidence_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_extreme_MFE90_low_MAE_subscription_artist_IP_bridge","current_profile_verdict":"current_profile_correct_if_subscription_retention_artist_lineup_margin_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"376300_2024-10-10_21550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C27 can allow Stage2/Yellow or Green-candidate-watch when content IP monetization is tied to subscription, artist lineup, retention, ARPU, margin and cash conversion. Green still requires exact source-grade evidence."}
```

### 6.2 041510 에스엠 — K-pop label global-content vocabulary without durable release / margin-cash bridge

Entry row: `2024-05-27 c=95800`, after a global-content / label price burst.
Observed path: same-day high `2024-05-27 h=100700`, then decline to `2024-09-24 l=59400`. A 2024 share-count movement watch remains.

```jsonl
{"row_type":"trigger","trigger_id":"R8L93_C27_041510_20240527_STAGE2_FALSE_POSITIVE_KPOP_LABEL_SPIKE","case_id":"C27_R8L93_041510_SM_LABEL_GLOBAL_CONTENT_DECAY","symbol":"041510","company_name":"에스엠","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_LABEL_GLOBAL_CONTENT_VOCABULARY_WITHOUT_DURABLE_RELEASE_MARGIN_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;post_spike_entry_guard;data_quality_watch","trigger_type":"Stage2-FalsePositive-KpopLabelGlobalContentVocabularyNoDurableReleaseMarginCashBridge","trigger_date":"2024-05-27","entry_date":"2024-05-27","entry_price":95800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_Kpop_label_global_content_price_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; K-pop label/global-content vocabulary treated as insufficient without durable release schedule, artist IP monetization, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["Kpop_global_content_keyword","artist_IP_vocabulary","post_spike_relative_strength"],"stage3_evidence_fields":["durable_release_schedule_missing","artist_monetization_bridge_missing","margin_cash_bridge_missing","share_count_repair_pending"],"stage4b_evidence_fields":["low_forward_MFE","deep_MAE","post_spike_entry_watch","share_count_movement_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2024.csv","profile_path":"atlas/symbol_profiles/041/041510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.11,"MFE_90D_pct":5.11,"MFE_180D_pct":5.11,"MAE_30D_pct":-20.67,"MAE_90D_pct":-27.35,"MAE_180D_pct":-37.99,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-27","peak_price":100700.0,"max_drawdown_low_date":"2024-09-24","max_drawdown_low":59400.0,"drawdown_after_peak_pct":-41.01,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"Kpop_label_global_content_spike_without_release_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_forward_MFE","deep_MAE","post_spike_entry_watch","share_count_movement_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_after_spike_no_durable_release_margin_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_Kpop_global_content_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["2024_share_count_movement_watch"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_usable; 2024_share_count_watch","same_entry_group_id":"041510_2024-05-27_95800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C27 should not promote K-pop label/global-content vocabulary after a spike unless release schedule, artist monetization, margin and cash evidence are repaired. Low MFE and deep MAE force Watch/4B routing."}
```

### 6.3 253450 스튜디오드래곤 — studio content pipeline vocabulary without fresh hit / licensing-margin bridge

Entry row: `2024-01-02 c=52300`, on studio content-pipeline / OTT global monetization vocabulary.
Observed path: early high `2024-01-03 h=52600`, then decline to `2024-08-14 l=34200`. Market flag changed to KOSDAQ GLOBAL after `2024-06-14`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L93_C27_253450_20240102_STAGE2_FALSE_POSITIVE_STUDIO_PIPELINE","case_id":"C27_R8L93_253450_STUDIO_DRAGON_CONTENT_PIPELINE_DECAY","symbol":"253450","company_name":"스튜디오드래곤","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"STUDIO_CONTENT_PIPELINE_VOCABULARY_WITHOUT_FRESH_HIT_LICENSING_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;market_segment_change_watch;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-StudioContentPipelineVocabularyNoFreshHitLicensingMarginBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":52300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_studio_content_pipeline_OTT_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; studio/OTT content-pipeline vocabulary treated as insufficient without fresh hit-rate, licensing terms, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["studio_content_pipeline_keyword","global_OTT_vocabulary","IP_monetization_vocabulary"],"stage3_evidence_fields":["fresh_hit_rate_missing","licensing_margin_bridge_missing","cash_conversion_missing","market_segment_repair_pending"],"stage4b_evidence_fields":["near_zero_MFE","deep_MAE","market_segment_change_watch","licensing_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253450/2024.csv","profile_path":"atlas/symbol_profiles/253/253450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.57,"MFE_90D_pct":0.57,"MFE_180D_pct":0.57,"MAE_30D_pct":-13.86,"MAE_90D_pct":-19.89,"MAE_180D_pct":-34.61,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-03","peak_price":52600.0,"max_drawdown_low_date":"2024-08-14","max_drawdown_low":34200.0,"drawdown_after_peak_pct":-34.98,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"studio_content_pipeline_vocabulary_without_fresh_hit_licensing_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["near_zero_MFE","deep_MAE","market_segment_change_watch","licensing_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_fresh_hit_licensing_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_studio_content_pipeline_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["market_segment_change_watch_KOSDAQ_to_KOSDAQ_GLOBAL_after_2024-06-14"],"corporate_action_window_status":"clean; market_segment_change_watch","same_entry_group_id":"253450_2024-01-02_52300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C27 should not promote studio/OTT pipeline vocabulary unless fresh hit-rate, licensing terms, margin and cash evidence are repaired. Market-segment rows need data-quality repair."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_R8L93_376300_DEARU_FAN_PLATFORM","trigger_id":"R8L93_C27_376300_20241010_STAGE2_FAN_PLATFORM_SUBSCRIPTION","symbol":"376300","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C27 requires monetization path, subscription or licensing revenue, retention/engagement, margin and cash bridge rather than IP vocabulary alone","raw_component_scores_before":{"content_IP_demand_score":12,"platform_distribution_score":13,"subscription_recurring_revenue_score":14,"artist_lineup_score":12,"retention_engagement_score":11,"ARPU_monetization_score":10,"margin_bridge_score":10,"cash_conversion_score":8,"relative_strength_score":15,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"content_IP_demand_score":15,"platform_distribution_score":16,"subscription_recurring_revenue_score":17,"artist_lineup_score":15,"retention_engagement_score":13,"ARPU_monetization_score":12,"margin_bridge_score":12,"cash_conversion_score":10,"relative_strength_score":16,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":90,"stage_label_after":"Stage3-Green-candidate-watch","component_delta_explanation":"Fan-platform subscription and artist-IP bridge plus extreme MFE supports Green-candidate watch; exact subscriber/ARPU/margin evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_R8L93_041510_SM_LABEL_GLOBAL_CONTENT_DECAY","trigger_id":"R8L93_C27_041510_20240527_STAGE2_FALSE_POSITIVE_KPOP_LABEL_SPIKE","symbol":"041510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"K-pop label/global-content vocabulary after a spike without release/margin/cash bridge should be blocked","raw_component_scores_before":{"content_IP_demand_score":4,"platform_distribution_score":2,"subscription_recurring_revenue_score":0,"artist_lineup_score":3,"retention_engagement_score":1,"ARPU_monetization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":5,"execution_risk_score":-16,"theme_spike_risk":-20,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"content_IP_demand_score":1,"platform_distribution_score":0,"subscription_recurring_revenue_score":0,"artist_lineup_score":1,"retention_engagement_score":0,"ARPU_monetization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"execution_risk_score":-26,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Low MFE and deep MAE require durable release, monetization, margin and cash evidence before any promotion."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_R8L93_253450_STUDIO_DRAGON_CONTENT_PIPELINE_DECAY","trigger_id":"R8L93_C27_253450_20240102_STAGE2_FALSE_POSITIVE_STUDIO_PIPELINE","symbol":"253450","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"studio/OTT content-pipeline vocabulary without fresh hit and licensing-margin bridge should remain Watch/4B","raw_component_scores_before":{"content_IP_demand_score":2,"platform_distribution_score":1,"subscription_recurring_revenue_score":0,"artist_lineup_score":0,"retention_engagement_score":0,"ARPU_monetization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"execution_risk_score":-14,"theme_spike_risk":-14,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"content_IP_demand_score":0,"platform_distribution_score":0,"subscription_recurring_revenue_score":0,"artist_lineup_score":0,"retention_engagement_score":0,"ARPU_monetization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":0,"execution_risk_score":-24,"theme_spike_risk":-20,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Near-zero MFE, deep MAE and market-segment change require evidence repair; studio pipeline vocabulary alone is not C27 monetization evidence."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R8L93_C27_P0_CURRENT","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C27 needs explicit subscription/licensing/engagement/margin/cash bridge and data-quality taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":33.45,"avg_MAE90_pct":-16.98,"avg_MFE180_pct":33.45,"avg_MAE180_pct":-25.44,"false_positive_rate":0.67,"data_quality_watch_count":2,"score_return_alignment_verdict":"mixed_without_C27_subscription_licensing_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R8L93_C27_P1_SECTOR_SPECIFIC","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_id":"P1_L8_content_IP_monetization_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L8 content-IP signals need subscription/licensing/ticket/royalty monetization, engagement/retention, release pipeline, margin or cash conversion before Stage2-Actionable","changed_axes":["monetization_path_required","retention_engagement_required","licensing_margin_required","data_quality_guard"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_subscription_licensing_engagement_margin_or_cash_proxy"},"eligible_trigger_count":3,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R8L93_C27_P2_CANONICAL","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_id":"P2_C27_monetization_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C27 should reward IP monetization-to-cash mechanics, not label/studio vocabulary","changed_axes":["C27_subscription_licensing_margin_cash_bridge_required","C27_label_studio_vocabulary_local_4B_guard","C27_share_count_market_segment_data_quality_guard","C27_Green_exact_evidence_guard"],"changed_thresholds":{"stage2_yellow_gate":"IP_demand_plus_subscription_or_licensing_margin_cash_bridge_required"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R8L93_C27_P3_COUNTEREXAMPLE_GUARD","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_id":"P3_C27_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If monetization/margin bridge is missing, MFE90<10 or MAE180<=-25 blocks Yellow/Green and routes to Watch/4B","changed_axes":["C27_low_MFE_guardrail","C27_deep_MAE_4B_guardrail","C27_bridge_missing_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_10_or_MAE180_le_minus25)"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_FAN_PLATFORM_POSITIVE_VS_LABEL_STUDIO_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":2,"avg_MFE90_pct":33.45,"avg_MAE90_pct":-16.98,"avg_MFE180_pct":33.45,"avg_MAE180_pct":-25.44,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"interpretation":"C27 needs monetization bridge discipline. 디어유 shows fan-platform subscription/artist-IP monetization can support Green-candidate-watch, while 에스엠 and 스튜디오드래곤 show label/studio content vocabulary should not be promoted without release, subscriber, licensing, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"376300","trigger_type":"Stage2-Actionable-FanPlatformSubscriptionArtistIPMonetizationBridge-Positive","entry_date":"2024-10-10","stage2_to_90D_outcome":"good_stage2_extreme_MFE_low_MAE","stage2_to_180D_outcome":"fan_platform_subscription_bridge_but_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow/Green-candidate when IP strength is tied to subscription, artist lineup, retention, ARPU and cash bridge; exact evidence required for Green."}
{"row_type":"stage_transition_summary","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"041510","trigger_type":"Stage2-FalsePositive-KpopLabelGlobalContentVocabularyNoDurableReleaseMarginCashBridge","entry_date":"2024-05-27","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE_after_spike","stage2_to_180D_outcome":"failed_Kpop_label_content_vocabulary_no_margin_cash_bridge_share_count_watch","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"K-pop label vocabulary after a spike without durable release/margin/cash bridge should stay Watch/4B-risk; share-count repair required."}
{"row_type":"stage_transition_summary","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"253450","trigger_type":"Stage2-FalsePositive-StudioContentPipelineVocabularyNoFreshHitLicensingMarginBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_bridge_missing","stage2_to_180D_outcome":"failed_studio_content_pipeline_no_hit_licensing_margin_bridge_market_segment_watch","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Studio/OTT pipeline vocabulary without fresh hit/licensing/margin evidence should remain Watch/4B; market-segment repair required."}
{"row_type":"residual_contribution","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","residual_type":"label_studio_content_vocabulary_overcredit_without_subscription_licensing_margin_cash_bridge","contribution":"Adds two C27 4B counterexamples against one fan-platform subscription/IP monetization positive-control, selected because C27 is Priority-0 under-30 coverage.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"FAN_PLATFORM_SUBSCRIPTION_IP_MONETIZATION_VS_LABEL_CONTENT_PIPELINE_AND_STUDIO_IP_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C27 now has one fan-platform subscription/IP positive-control and two label/studio weak-bridge counterexamples; next C27 loops should exact-URL repair subscriber retention, artist lineup, licensing terms, release schedule, hit-rate, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","axis":"C27_subscription_licensing_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"376300 worked when fan-platform subscription/IP monetization proxy existed; 041510 and 253450 failed when durable release/licensing/margin/cash evidence was missing."}
{"row_type":"shadow_weight","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","axis":"C27_label_studio_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"041510 and 253450 showed low/near-zero MFE and deep MAE when label/studio content vocabulary was not tied to monetization bridge."}
{"row_type":"shadow_weight","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","axis":"C27_share_count_market_segment_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"041510 has 2024 share-count movement and 253450 has market-segment change; production patching requires price-path/evidence repair."}
{"row_type":"shadow_weight","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","axis":"C27_Green_exact_evidence_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"evidence_basis":"376300 has extreme MFE but remains source-proxy-only; Green requires exact subscriber/ARPU/margin/cash evidence."}
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
  - label_content_vocabulary_overcredit
  - studio_content_pipeline_vocabulary_overcredit
  - subscription_licensing_margin_cash_bridge_missing
  - share_count_movement_watch
  - market_segment_change_watch
new_axis_proposed:
  - C27_subscription_licensing_margin_cash_bridge_required_shadow_only
  - C27_label_studio_vocabulary_local_4B_guard_shadow_only
  - C27_share_count_market_segment_data_quality_guard_shadow_only
  - C27_Green_exact_evidence_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows.
`376300` has no corporate-action candidate and the selected 2024 window is clean.
`041510` has only older corporate-action candidates, but 2024 share-count movement is visible and remains data-quality watch.
`253450` has no corporate-action candidate, but market flag changes from KOSDAQ to KOSDAQ GLOBAL after 2024-06-14, so it remains data-quality watch before patching.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
share_count_watch = true for 041510
market_segment_change_watch = true for 253450
promotion should prefer hold / exact evidence repair until exact URLs are added
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
5. Confirm this loop was selected by coverage-index-first after recent C08/C09/C01/C07/C06/C10/C11/C19 local expansions.
6. Confirm this loop avoided:
   - C27 top-covered symbols
   - previous R8 loop85 C26 symbols
   - previous R8 loop86 C28 symbols
   - previous R8 loop87 C27 symbols
   - previous R8 loop88 C26 symbols
   - previous R8 loop89 C28 symbols
   - previous R8 loop90 C27 symbols
   - previous R8 loop91 C26 symbols
   - previous R8 loop92 C28 symbols
7. Confirm touched C19/C11 and earlier candidate rows are not ingested from this MD.
8. Keep 041510 in share-count data-quality watch before patch consideration.
9. Keep 253450 in market-segment data-quality watch before patch consideration.
10. Treat 041510 and 253450 as weak-bridge failure modes unless exact release/licensing/margin/cash evidence is added later.
11. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C27-scoped safe patch candidates:
   - C27_subscription_licensing_margin_cash_bridge_required
   - C27_label_studio_vocabulary_local_4B_guard
   - C27_share_count_market_segment_data_quality_guard
   - C27_Green_exact_evidence_guard
12. Do not loosen Stage3-Green.
13. Do not use future MFE/MAE in runtime scoring.
14. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R8
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = remaining under-30 archetype from No-Repeat Index, preferably C17/C23/C24/C26/C28 depending on newest coverage pressure and recent-loop avoidance
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 fan-platform subscription/IP positive-control, 2 weak-bridge counterexamples, and 2 local 4B-watch rows for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.
```
