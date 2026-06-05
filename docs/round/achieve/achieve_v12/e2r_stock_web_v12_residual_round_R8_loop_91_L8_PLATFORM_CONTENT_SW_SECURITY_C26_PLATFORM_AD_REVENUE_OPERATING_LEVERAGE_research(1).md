# E2R Stock-Web v12 Residual Research — R8 Loop 91 / L8 / C26

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R8
loop: 91
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: MULTI_PLATFORM_PAYMENT_GAME_MARGIN_BRIDGE_VS_REWARD_AD_MUSIC_PLATFORM_THEME_DECAY
sector: platform / ad revenue / payment / game / music platform / reward adtech / operating leverage
output_file: e2r_stock_web_v12_residual_round_R8_loop_91_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R7 loop 91`.

```text
scheduled_round = R8
scheduled_loop = 91
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

R8 is restricted to platform / content / software / security.  
C26 is selected because R8 loop90 used C27 content/IP, while the recent R8 rotation is:

```text
R8 loop85: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
R8 loop86: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
R8 loop87: C27_CONTENT_IP_GLOBAL_MONETIZATION
R8 loop88: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
R8 loop89: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
R8 loop90: C27_CONTENT_IP_GLOBAL_MONETIZATION
```

No-Repeat Index snapshot used only as duplicate ledger:

```text
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
rows = 13
symbols = 10
good/bad Stage2 = 2/6
4B/4C = 0/1
top-covered = 042000, 214270, 237820, 030000, 035420, 035720
```

This loop avoids the C26 top-covered list and recent R8 loop symbols:

```text
R8 loop85 C26: 067160, 089600, 123570
R8 loop86 C28: 030520, 053800, 049480
R8 loop87 C27: 251270, 035900, 352820
R8 loop88 C26: 230360, 216050, 273060
R8 loop89 C28: 060850, 067920, 304100
R8 loop90 C27: 035760, 241840, 206560
```

Candidate hygiene note:

```text
During this execution path, R7/C23, R6/C21 and earlier candidate rows were touched in surrounding tool calls.
Those rows are not used in this R8/C26 output.
```

Selected symbols:

```text
181710, 236810, 104200
```

This loop tests:

```text
multi-platform / payment / game operating-leverage bridge
vs
reward-adtech platform spike without durable advertiser retention / take-rate / margin bridge
vs
music-platform content rebound without ad/subscription ARPU and operating-leverage bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"181710","company_name":"NHN","profile_path":"atlas/symbol_profiles/181/181710.json","first_date":"2013-08-29","last_date":"2026-02-20","trading_day_count":3060,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2015-04-07","2021-12-29","2022-01-24"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"236810","company_name":"엔비티","profile_path":"atlas/symbol_profiles/236/236810.json","first_date":"2021-01-21","last_date":"2026-02-20","trading_day_count":1245,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2022-05-30","2022-06-21"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"104200","company_name":"NHN벅스","profile_path":"atlas/symbol_profiles/104/104200.json","first_date":"2009-10-06","last_date":"2026-02-20","trading_day_count":4033,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2010-04-26"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical name-transition/corporate-action candidate exists long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"181710","trigger_type":"Stage2-Actionable-MultiPlatformPaymentGameOperatingLeverageBridge-Positive","entry_date":"2024-01-29","duplicate_status":"new C26 symbol/trigger/date combination outside top-covered and previous R8 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"236810","trigger_type":"Stage2-FalsePositive-RewardAdtechPlatformSpikeNoAdvertiserRetentionTakeRateBridge","entry_date":"2024-01-03","duplicate_status":"new C26 symbol/trigger/date combination outside top-covered and previous R8 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"104200","trigger_type":"Stage2-FalsePositive-MusicPlatformContentThemeNoARPUOperatingLeverageBridge","entry_date":"2024-01-19","duplicate_status":"new C26 symbol/trigger/date combination outside top-covered and previous R8 loop symbols"}
```

## 4. Research question

C26 is not “플랫폼주가 반등했다.”  
The useful platform/ad-revenue signal must prove a revenue-to-margin bridge:

```text
traffic or user base quality
ad inventory quality
advertiser retention or budget expansion
take-rate / ARPU
payment or game revenue mix
cost discipline
operating leverage
margin bridge
cash conversion
```

A platform headline without this bridge is a busy lobby with no checkout counter. The crowd matters only when traffic turns into monetized inventory, take-rate, margin, and cash.

Residual question:

```text
Can C26 distinguish:
1. multi-platform / payment / game operating-leverage bridge with high MFE and controlled early MAE,
2. reward-adtech platform spike where advertiser-retention, take-rate and margin evidence are missing,
3. music-platform / content rebound where ARPU, subscription/ad mix and operating leverage are not repaired?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C26_R8L91_181710_NHN_MULTI_PLATFORM_OPERATING_LEVERAGE","symbol":"181710","company_name":"NHN","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"MULTI_PLATFORM_PAYMENT_GAME_OPERATING_LEVERAGE_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-MultiPlatformPaymentGameOperatingLeverageBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_MFE90_ge30_low_entry_MAE_but_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_ARPU_mix_cost_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Multi-platform/payment/game operating-leverage proxy produced MFE90 above 30 with shallow entry MAE. Later drawdown keeps Green strict and requires exact revenue mix, cost and margin/cash evidence."}
{"row_type":"case","case_id":"C26_R8L91_236810_NBT_REWARD_ADTECH_SPIKE","symbol":"236810","company_name":"엔비티","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"REWARD_ADTECH_PLATFORM_SPIKE_WITHOUT_ADVERTISER_RETENTION_TAKERATE_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-RewardAdtechPlatformSpikeNoAdvertiserRetentionTakeRateBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub_Yellow_MFE_extreme_MAE_no_ad_revenue_bridge","current_profile_verdict":"current_profile_false_positive_if_reward_adtech_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Reward-adtech platform spike had sub-Yellow MFE from the selected entry and extreme later MAE without advertiser retention, take-rate, margin and cash bridge."}
{"row_type":"case","case_id":"C26_R8L91_104200_NHN_BUGS_MUSIC_PLATFORM_THEME","symbol":"104200","company_name":"NHN벅스","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"MUSIC_PLATFORM_CONTENT_THEME_WITHOUT_ARPU_OPERATING_LEVERAGE_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-MusicPlatformContentThemeNoARPUOperatingLeverageBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_ARPU_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_music_platform_content_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Music-platform/content rebound had only local MFE and later deep drawdown without ad/subscription ARPU, user retention, operating leverage or cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 181710 NHN — multi-platform / payment / game operating-leverage bridge

Entry row: `2024-01-29 c=22450`.  
Observed path: entry low `2024-01-29 l=21650`, 90D peak `2024-02-20 h=29250`, and late-year low `2024-10-25 l=15640`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L91_C26_181710_20240129_STAGE2_PLATFORM_OPERATING_LEVERAGE","case_id":"C26_R8L91_181710_NHN_MULTI_PLATFORM_OPERATING_LEVERAGE","symbol":"181710","company_name":"NHN","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"MULTI_PLATFORM_PAYMENT_GAME_OPERATING_LEVERAGE_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-MultiPlatformPaymentGameOperatingLeverageBridge-Positive","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":22450.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_multi_platform_payment_game_operating_leverage_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; platform/payment/game revenue mix, cost discipline and operating leverage bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["platform_revenue_mix_proxy","payment_or_game_revenue_proxy","cost_discipline_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_ARPU_or_take_rate_source_pending","revenue_mix_source_pending","margin_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/181/181710/2024.csv","profile_path":"atlas/symbol_profiles/181/181710.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":30.29,"MFE_90D_pct":30.29,"MFE_180D_pct":30.29,"MAE_30D_pct":-3.56,"MAE_90D_pct":-3.56,"MAE_180D_pct":-30.33,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-20","peak_price":29250.0,"max_drawdown_low_date":"2024-10-25","max_drawdown_low":15640.0,"drawdown_after_peak_pct":-46.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_ARPU_revenue_mix_cost_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_MFE90_ge30_low_entry_MAE_but_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_ARPU_mix_cost_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"181710_2024-01-29_22450","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C26 can allow Stage2/Yellow when platform strength is tied to traffic quality, revenue mix, take-rate or ARPU, cost discipline, margin and cash conversion. Green still requires exact source-grade evidence."}
```

### 6.2 236810 엔비티 — reward-adtech platform spike without advertiser-retention / take-rate bridge

Entry row: `2024-01-03 c=9010`.  
Observed path: local high `2024-01-08 h=10600`, then a persistent collapse to `2024-12-09 l=2825`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L91_C26_236810_20240103_STAGE2_FALSE_POSITIVE_REWARD_ADTECH","case_id":"C26_R8L91_236810_NBT_REWARD_ADTECH_SPIKE","symbol":"236810","company_name":"엔비티","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"REWARD_ADTECH_PLATFORM_SPIKE_WITHOUT_ADVERTISER_RETENTION_TAKERATE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-RewardAdtechPlatformSpikeNoAdvertiserRetentionTakeRateBridge","trigger_date":"2024-01-03","entry_date":"2024-01-03","entry_price":9010.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_reward_adtech_platform_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; reward-adtech platform spike treated as insufficient without advertiser retention, budget expansion, take-rate, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["reward_adtech_theme","platform_spike","relative_strength_spike"],"stage3_evidence_fields":["advertiser_retention_missing","take_rate_ARPU_missing","gross_margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["sub_Yellow_MFE","ad_revenue_bridge_missing_watch","extreme_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/236/236810/2024.csv","profile_path":"atlas/symbol_profiles/236/236810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.65,"MFE_90D_pct":17.65,"MFE_180D_pct":17.65,"MAE_30D_pct":-22.75,"MAE_90D_pct":-38.62,"MAE_180D_pct":-68.65,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-08","peak_price":10600.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":2825.0,"drawdown_after_peak_pct":-73.35,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"reward_adtech_platform_spike_without_advertiser_retention_take_rate_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["sub_Yellow_MFE","ad_revenue_bridge_missing_watch","extreme_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub_Yellow_MFE_extreme_MAE_no_ad_revenue_bridge","current_profile_verdict":"current_profile_false_positive_if_reward_adtech_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"236810_2024-01-03_9010","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C26 should not promote adtech price spikes unless advertiser retention, budget expansion, take-rate/ARPU, margin and cash evidence are repaired. Sub-Yellow MFE and extreme MAE require Watch/4B routing."}
```

### 6.3 104200 NHN벅스 — music-platform content theme without ARPU / operating leverage bridge

Entry row: `2024-01-19 c=4805`, after a content/music-platform spike.  
Observed path: local high `2024-03-07 h=5840`, then late-year low `2024-12-09 l=2600`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L91_C26_104200_20240119_STAGE2_FALSE_POSITIVE_MUSIC_PLATFORM","case_id":"C26_R8L91_104200_NHN_BUGS_MUSIC_PLATFORM_THEME","symbol":"104200","company_name":"NHN벅스","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"MUSIC_PLATFORM_CONTENT_THEME_WITHOUT_ARPU_OPERATING_LEVERAGE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;platform_content_theme_4B_stress_test","trigger_type":"Stage2-FalsePositive-MusicPlatformContentThemeNoARPUOperatingLeverageBridge","trigger_date":"2024-01-19","entry_date":"2024-01-19","entry_price":4805.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_music_platform_content_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; music/content platform theme treated as insufficient without subscription/ad ARPU, user retention, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["music_platform_theme","content_platform_keyword","relative_strength_rebound"],"stage3_evidence_fields":["subscription_ARPU_missing","ad_monetization_missing","user_retention_missing","operating_margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE_watch","ARPU_margin_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/104/104200/2024.csv","profile_path":"atlas/symbol_profiles/104/104200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.93,"MFE_90D_pct":21.54,"MFE_180D_pct":21.54,"MAE_30D_pct":-11.86,"MAE_90D_pct":-11.86,"MAE_180D_pct":-45.89,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":5840.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":2600.0,"drawdown_after_peak_pct":-55.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.51,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"music_platform_content_theme_MFE_without_ARPU_retention_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE_watch","ARPU_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_ARPU_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_music_platform_content_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_name_transition_pre_2024; selected_window_clean","same_entry_group_id":"104200_2024-01-19_4805","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C26 should not count music/content platform MFE as ad-revenue operating leverage unless ARPU, user retention, ad/subscription mix, margin and cash evidence are exact-repaired."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_R8L91_181710_NHN_MULTI_PLATFORM_OPERATING_LEVERAGE","trigger_id":"R8L91_C26_181710_20240129_STAGE2_PLATFORM_OPERATING_LEVERAGE","symbol":"181710","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C26 requires ARPU/take-rate, revenue mix, user quality, cost discipline, margin and cash bridge rather than platform vocabulary alone","raw_component_scores_before":{"traffic_user_quality_score":10,"ad_inventory_quality_score":7,"ARPU_take_rate_score":11,"revenue_mix_score":12,"cost_discipline_score":12,"operating_leverage_score":12,"margin_bridge_score":10,"cash_conversion_score":7,"relative_strength_score":13,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"traffic_user_quality_score":12,"ad_inventory_quality_score":9,"ARPU_take_rate_score":13,"revenue_mix_score":15,"cost_discipline_score":15,"operating_leverage_score":15,"margin_bridge_score":12,"cash_conversion_score":9,"relative_strength_score":14,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Platform revenue-mix/cost-discipline bridge plus MFE90>30 supports Yellow-watch; late drawdown and proxy-only evidence block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_R8L91_236810_NBT_REWARD_ADTECH_SPIKE","trigger_id":"R8L91_C26_236810_20240103_STAGE2_FALSE_POSITIVE_REWARD_ADTECH","symbol":"236810","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"reward-adtech spike without advertiser retention and take-rate bridge should be blocked","raw_component_scores_before":{"traffic_user_quality_score":2,"ad_inventory_quality_score":2,"ARPU_take_rate_score":0,"revenue_mix_score":1,"cost_discipline_score":0,"operating_leverage_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":9,"valuation_repricing_score":4,"execution_risk_score":-18,"theme_spike_risk":-20,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"traffic_user_quality_score":0,"ad_inventory_quality_score":0,"ARPU_take_rate_score":0,"revenue_mix_score":0,"cost_discipline_score":0,"operating_leverage_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":0,"execution_risk_score":-28,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-Yellow MFE and extreme MAE require advertiser retention, take-rate, margin and cash evidence before any Yellow/Green promotion."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_R8L91_104200_NHN_BUGS_MUSIC_PLATFORM_THEME","trigger_id":"R8L91_C26_104200_20240119_STAGE2_FALSE_POSITIVE_MUSIC_PLATFORM","symbol":"104200","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"music/content platform MFE without ARPU, retention and operating leverage should remain Watch/4B","raw_component_scores_before":{"traffic_user_quality_score":2,"ad_inventory_quality_score":1,"ARPU_take_rate_score":1,"revenue_mix_score":1,"cost_discipline_score":0,"operating_leverage_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":10,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"traffic_user_quality_score":1,"ad_inventory_quality_score":0,"ARPU_take_rate_score":0,"revenue_mix_score":0,"cost_discipline_score":0,"operating_leverage_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":0,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Price MFE without ARPU and margin bridge is not C26 validation; deep 180D MAE keeps it in 4B-watch."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R8L91_C26_P0_CURRENT","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C26 needs explicit ARPU/take-rate, advertiser retention, revenue mix, cost discipline, margin/cash and platform-theme 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":23.16,"avg_MAE90_pct":-18.01,"avg_MFE180_pct":23.16,"avg_MAE180_pct":-48.29,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.84,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C26_ARPU_revenue_mix_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R8L91_C26_P1_SECTOR_SPECIFIC","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_id":"P1_L8_platform_revenue_operating_leverage_candidate","profile_scope":"sector_specific","profile_hypothesis":"L8 platform signals need user/traffic quality, ad inventory, ARPU/take-rate, advertiser retention, revenue mix, operating leverage or cash conversion before Stage2-Actionable","changed_axes":["ARPU_take_rate_required","advertiser_retention_required","operating_leverage_margin_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_user_quality_ad_inventory_ARPU_take_rate_revenue_mix_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":23.16,"avg_MAE90_pct":-18.01,"avg_MFE180_pct":23.16,"avg_MAE180_pct":-48.29,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R8L91_C26_P2_CANONICAL","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_id":"P2_C26_ARPU_revenue_mix_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C26 should reward monetization-to-margin mechanics, not platform/adtech/music vocabulary","changed_axes":["C26_ARPU_take_rate_revenue_mix_margin_cash_bridge_required","C26_reward_adtech_music_theme_local_4B_guard","C26_price_MFE_not_operating_leverage_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"ARPU_or_take_rate_or_ad_retention_plus_margin_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":23.16,"avg_MAE90_pct":-18.01,"avg_MFE180_pct":23.16,"avg_MAE180_pct":-48.29,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R8L91_C26_P3_COUNTEREXAMPLE_GUARD","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","profile_id":"P3_C26_sub20_or_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If ARPU/ad-retention/margin bridge is missing, MFE90<20 or MAE180<=-35 should block Yellow/Green and route to 4B-watch","changed_axes":["C26_sub20_MFE_guardrail","C26_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_20_or_MAE180_le_minus_35)"},"eligible_trigger_count":3,"avg_MFE90_pct":23.16,"avg_MAE90_pct":-18.01,"avg_MFE180_pct":23.16,"avg_MAE180_pct":-48.29,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_NHN_PLATFORM_POSITIVE_VS_REWARD_AD_MUSIC_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":23.16,"avg_MAE90_pct":-18.01,"avg_MFE180_pct":23.16,"avg_MAE180_pct":-48.29,"stage2_hit_rate_MFE90_ge20":0.67,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE180_le_minus35":0.67,"interpretation":"C26 needs bridge discipline. NHN shows platform revenue-mix and cost-discipline operating-leverage bridge can support Yellow-watch, while 엔비티 and NHN벅스 show reward-adtech or music-platform vocabulary should not be promoted without advertiser retention, ARPU/take-rate, user retention, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"181710","trigger_type":"Stage2-Actionable-MultiPlatformPaymentGameOperatingLeverageBridge-Positive","entry_date":"2024-01-29","stage2_to_90D_outcome":"good_stage2_MFE90_ge30_low_MAE","stage2_to_180D_outcome":"positive_platform_revenue_mix_bridge_but_late_drawdown_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when platform strength is tied to revenue mix, ARPU/take-rate, cost discipline, margin and cash bridge; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"236810","trigger_type":"Stage2-FalsePositive-RewardAdtechPlatformSpikeNoAdvertiserRetentionTakeRateBridge","entry_date":"2024-01-03","stage2_to_90D_outcome":"bad_stage2_sub_Yellow_MFE_deep_MAE","stage2_to_180D_outcome":"failed_reward_adtech_spike_extreme_MAE","MFE90_ge20":false,"MAE180_le_minus35":true,"transition_note":"Reward-adtech platform spike without advertiser retention/take-rate/margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"104200","trigger_type":"Stage2-FalsePositive-MusicPlatformContentThemeNoARPUOperatingLeverageBridge","entry_date":"2024-01-19","stage2_to_90D_outcome":"price_MFE_without_ARPU_margin_bridge","stage2_to_180D_outcome":"failed_music_platform_theme_deep_MAE","MFE90_ge20":true,"MAE180_le_minus35":true,"transition_note":"Music/content platform MFE without ARPU, retention and margin/cash bridge should be treated as 4B-watch, not positive C26 evidence."}
{"row_type":"residual_contribution","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","residual_type":"reward_adtech_music_platform_vocabulary_overcredit_without_ARPU_revenue_mix_margin_cash_bridge","contribution":"Adds two C26 4B counterexamples against one multi-platform operating-leverage positive, avoiding C26 top-covered and recent R8 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"MULTI_PLATFORM_PAYMENT_GAME_MARGIN_BRIDGE_VS_REWARD_AD_MUSIC_PLATFORM_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C26 now has non-top-symbol multi-platform operating-leverage positive and two reward-ad/music-platform weak-bridge counterexamples; next R8 C26 loops should exact-URL repair traffic/user quality, advertiser retention, take-rate/ARPU, revenue mix, cost discipline, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","axis":"C26_ARPU_take_rate_revenue_mix_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"181710 worked when revenue mix and cost-discipline proxy existed; 236810 and 104200 failed when platform vocabulary lacked ARPU/take-rate, advertiser/user retention, margin and cash evidence."}
{"row_type":"shadow_weight","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","axis":"C26_reward_adtech_music_theme_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Reward-adtech and music-platform rows showed sub-20 or price-only MFE plus deep 180D MAE when monetization evidence was missing."}
{"row_type":"shadow_weight","round":"R8","loop":"91","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","axis":"C26_price_MFE_not_operating_leverage_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"104200 shows MFE90 above 20 should not count as positive C26 evidence when ARPU/retention/margin bridge is missing and MAE180 is deep."}
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
  - reward_adtech_platform_spike_overcredit
  - music_platform_content_theme_overcredit
  - advertiser_retention_bridge_missing
  - ARPU_take_rate_margin_bridge_missing
  - price_MFE_without_operating_leverage_validation
new_axis_proposed:
  - C26_ARPU_take_rate_revenue_mix_margin_cash_bridge_required_shadow_only
  - C26_reward_adtech_music_theme_local_4B_guard_shadow_only
  - C26_price_MFE_not_operating_leverage_validation_guard_shadow_only
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
`181710`, `236810`, and `104200` have only historical corporate-action or name-transition candidates before the selected 2024 windows.  
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
3. Confirm R8 / L8 / C26 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C26 top-covered symbols
   - previous R8 loop85 C26 symbols
   - previous R8 loop86 C28 symbols
   - previous R8 loop87 C27 symbols
   - previous R8 loop88 C26 symbols
   - previous R8 loop89 C28 symbols
   - previous R8 loop90 C27 symbols
6. Confirm accidentally touched R7/C23, R6/C21 and earlier candidate rows are not ingested from this MD.
7. If aggregate support remains stable after exact evidence URL repair, consider C26-scoped safe patch candidates:
   - C26_ARPU_take_rate_revenue_mix_margin_cash_bridge_required
   - C26_reward_adtech_music_theme_local_4B_guard
   - C26_price_MFE_not_operating_leverage_validation_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R8
completed_loop = 91
next_round = R9
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE.
```
