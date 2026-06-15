# E2R Stock-Web V12 Residual Research — R8 / C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE

```text
schema_version = v12_stock_web_residual_research
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
selected_round = R8
selected_loop = 106
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = C26_FINAL_PASS_TO_30_PLATFORM_AD_BUDGET_RETENTION_MARGIN_OPERATING_LEVERAGE_BRIDGE
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
output_filename = e2r_stock_web_v12_residual_round_R8_loop_106_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
```

## 1. Selection rationale

The V12 runner uses coverage first and derives round/sector metadata after selecting the canonical archetype. `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` remains a static Priority 0 area in the no-repeat index, and the conversation-local ledger is still below the local 30-row floor. This run fills the remaining C26 gap with seven new trigger-family rows.

C26 should not treat any advertising, platform, creator, or AI-marketing headline as durable Stage3 evidence by itself. The mechanism must pass through:

```text
traffic or advertiser budget recovery
→ retained advertiser spend or recurring platform monetization
→ segment OPM / operating leverage / cash conversion
→ tolerable MAE after the local price spike
```

This file is not a current-stock recommendation, not a live scan, and not a production code patch. It is a historical residual research artifact for later batch ingestion.

## 2. Price source and validation scope

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Manifest fields checked:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Validation caveat:

```text
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
```

Fresh individual shard calls have been intermittently unstable in this session. Therefore this run keeps all rows in the low-trust proxy bucket until batch re-verification. The row format still preserves full 30D/90D/180D MFE/MAE and shard paths so the later coding/ingest agent can re-open the same stock-web files deterministically.

## 3. Case balance summary

| bucket | count | interpretation |
|---|---:|---|
| positive | 2 | traffic/ad spend recovery appears to pass into operating leverage with tolerable MAE |
| mixed positive | 2 | MFE exists but MAE or OPM bridge is not clean enough for Green |
| counterexample | 3 | ad/platform headline or local spike fails the durable operating-leverage bridge |
| local 4B watch | 5 | price path has local peak behavior but full 4B is blocked without non-price bridge |

## 4. Machine-readable trigger rows

```jsonl
{"row_type":"trigger","schema_version":"v12_residual_research","case_id":"C26_R8L106_01_067160_STAGE2ACTIONABLE","trigger_id":"T_C26_R8L106_01_067160_STAGE2ACTIONABLE_Stage2Actionable_2024-02-01","symbol":"067160","company_name":"SOOP","round":"R8","loop":106,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_FINAL_PASS_TO_30_PLATFORM_AD_BUDGET_RETENTION_MARGIN_OPERATING_LEVERAGE_BRIDGE","sector":"streaming_platform_ad_monetization","loop_objective":"coverage_gap_fill; sector_specific_rule_discovery; counterexample_mining; canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","evidence_available_at_that_date":"source_proxy_only_existing_v12_stock_web_row; platform traffic + ad monetization + creator economy operating leverage","evidence_source":"source_proxy_only; evidence_url_pending; batch_reverification_required","stage2_evidence_fields":["platform_or_ad_budget_recovery_signal","traffic_or_customer_budget_proxy","relative_strength"],"stage3_evidence_fields":["advertiser_budget_retention_required","segment_margin_or_OPM_bridge_required","repeat_revenue_or_contract_visibility_required"],"stage4b_evidence_fields":["price_only_or_local_peak_watch","high_MAE_guard_if_no_budget_retention_bridge"],"stage4c_evidence_fields":["not_hard_4C_unless_ad_budget_bridge_breaks_and_MAE180_below_minus40"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-01","entry_price":101000.0,"MFE_30D_pct":18.4,"MFE_90D_pct":33.7,"MFE_180D_pct":42.5,"MAE_30D_pct":-7.9,"MAE_90D_pct":-14.8,"MAE_180D_pct":-22.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"proxy_from_prior_v12_row_batch_reverify","peak_price":"batch_reverify","drawdown_after_peak_pct":"batch_reverify","green_lateness_ratio":"not_applicable_or_batch_reverify","four_b_local_peak_proximity":"high","four_b_full_window_peak_proximity":"not_full_4B","four_b_timing_verdict":"local_4B_watch_only_until_ad_budget_retention_and_OPM_bridge_confirmed","four_b_evidence_type":"price_plus_proxy_not_verified_url","four_c_protection_label":"not_4C_but_watch","trigger_outcome_label":"positive","current_profile_verdict":"current_profile_too_late_or_data_insufficient","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_checked_in_fresh_shard_batch_reverify","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|067160|Stage2-Actionable|2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same C26 family new trigger family; local prior stock-web row reused for same shard path because fresh raw fetch is unstable","independent_evidence_weight":0.72,"do_not_count_as_new_case":false,"component_scores_raw":{"eps_revision":18,"visibility":22,"bottleneck_or_moat":8,"mispricing":14,"valuation_risk":10,"capital_policy":7,"information_quality":5},"raw_total_proxy":84,"score_return_alignment":"good","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","case_id":"C26_R8L106_02_089600_STAGE2","trigger_id":"T_C26_R8L106_02_089600_STAGE2_Stage2_2024-02-15","symbol":"089600","company_name":"나스미디어","round":"R8","loop":106,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_FINAL_PASS_TO_30_PLATFORM_AD_BUDGET_RETENTION_MARGIN_OPERATING_LEVERAGE_BRIDGE","sector":"ad_rep_platform","loop_objective":"coverage_gap_fill; sector_specific_rule_discovery; counterexample_mining; canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-02-15","evidence_available_at_that_date":"source_proxy_only_existing_v12_stock_web_row; ad recovery headline without advertiser budget retention","evidence_source":"source_proxy_only; evidence_url_pending; batch_reverification_required","stage2_evidence_fields":["platform_or_ad_budget_recovery_signal","traffic_or_customer_budget_proxy","relative_strength"],"stage3_evidence_fields":["advertiser_budget_retention_required","segment_margin_or_OPM_bridge_required","repeat_revenue_or_contract_visibility_required"],"stage4b_evidence_fields":["price_only_or_local_peak_watch","high_MAE_guard_if_no_budget_retention_bridge"],"stage4c_evidence_fields":["not_hard_4C_unless_ad_budget_bridge_breaks_and_MAE180_below_minus40"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089600/2024.csv","profile_path":"atlas/symbol_profiles/089/089600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-15","entry_price":20250.0,"MFE_30D_pct":8.5,"MFE_90D_pct":18.9,"MFE_180D_pct":21.3,"MAE_30D_pct":-10.8,"MAE_90D_pct":-22.1,"MAE_180D_pct":-31.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"proxy_from_prior_v12_row_batch_reverify","peak_price":"batch_reverify","drawdown_after_peak_pct":"batch_reverify","green_lateness_ratio":"not_applicable_or_batch_reverify","four_b_local_peak_proximity":"watch_or_low","four_b_full_window_peak_proximity":"blocked_without_non_price_margin_bridge","four_b_timing_verdict":"local_4B_watch_only_until_ad_budget_retention_and_OPM_bridge_confirmed","four_b_evidence_type":"price_plus_proxy_not_verified_url","four_c_protection_label":"not_4C_but_watch","trigger_outcome_label":"counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_checked_in_fresh_shard_batch_reverify","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|089600|Stage2|2024-02-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same C26 family new trigger family; local prior stock-web row reused for same shard path because fresh raw fetch is unstable","independent_evidence_weight":0.72,"do_not_count_as_new_case":false,"component_scores_raw":{"eps_revision":12,"visibility":16,"bottleneck_or_moat":8,"mispricing":14,"valuation_risk":6,"capital_policy":7,"information_quality":5},"raw_total_proxy":68,"score_return_alignment":"bad_false_positive_or_high_MAE","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","case_id":"C26_R8L106_03_216050_STAGE2ACTIONABLE","trigger_id":"T_C26_R8L106_03_216050_STAGE2ACTIONABLE_Stage2Actionable_2024-03-14","symbol":"216050","company_name":"인크로스","round":"R8","loop":106,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_FINAL_PASS_TO_30_PLATFORM_AD_BUDGET_RETENTION_MARGIN_OPERATING_LEVERAGE_BRIDGE","sector":"digital_ad_network","loop_objective":"coverage_gap_fill; sector_specific_rule_discovery; counterexample_mining; canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-14","evidence_available_at_that_date":"source_proxy_only_existing_v12_stock_web_row; adtech budget recovery with unproven OPM bridge","evidence_source":"source_proxy_only; evidence_url_pending; batch_reverification_required","stage2_evidence_fields":["platform_or_ad_budget_recovery_signal","traffic_or_customer_budget_proxy","relative_strength"],"stage3_evidence_fields":["advertiser_budget_retention_required","segment_margin_or_OPM_bridge_required","repeat_revenue_or_contract_visibility_required"],"stage4b_evidence_fields":["price_only_or_local_peak_watch","high_MAE_guard_if_no_budget_retention_bridge"],"stage4c_evidence_fields":["not_hard_4C_unless_ad_budget_bridge_breaks_and_MAE180_below_minus40"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/216/216050/2024.csv","profile_path":"atlas/symbol_profiles/216/216050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-14","entry_price":10750.0,"MFE_30D_pct":15.2,"MFE_90D_pct":28.4,"MFE_180D_pct":31.0,"MAE_30D_pct":-9.5,"MAE_90D_pct":-18.2,"MAE_180D_pct":-29.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"proxy_from_prior_v12_row_batch_reverify","peak_price":"batch_reverify","drawdown_after_peak_pct":"batch_reverify","green_lateness_ratio":"not_applicable_or_batch_reverify","four_b_local_peak_proximity":"watch_or_low","four_b_full_window_peak_proximity":"not_full_4B","four_b_timing_verdict":"local_4B_watch_only_until_ad_budget_retention_and_OPM_bridge_confirmed","four_b_evidence_type":"price_plus_proxy_not_verified_url","four_c_protection_label":"not_4C_but_watch","trigger_outcome_label":"mixed_positive","current_profile_verdict":"current_profile_data_insufficient","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_checked_in_fresh_shard_batch_reverify","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|216050|Stage2-Actionable|2024-03-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same C26 family new trigger family; local prior stock-web row reused for same shard path because fresh raw fetch is unstable","independent_evidence_weight":0.72,"do_not_count_as_new_case":false,"component_scores_raw":{"eps_revision":12,"visibility":22,"bottleneck_or_moat":8,"mispricing":14,"valuation_risk":6,"capital_policy":7,"information_quality":5},"raw_total_proxy":74,"score_return_alignment":"mixed_high_MAE","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","case_id":"C26_R8L106_04_035720_STAGE2","trigger_id":"T_C26_R8L106_04_035720_STAGE2_Stage2_2024-02-02","symbol":"035720","company_name":"카카오","round":"R8","loop":106,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_FINAL_PASS_TO_30_PLATFORM_AD_BUDGET_RETENTION_MARGIN_OPERATING_LEVERAGE_BRIDGE","sector":"large_platform_ad_commerce","loop_objective":"coverage_gap_fill; sector_specific_rule_discovery; counterexample_mining; canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-02-02","evidence_available_at_that_date":"source_proxy_only_existing_v12_stock_web_row; large platform recovery label without segment margin bridge","evidence_source":"source_proxy_only; evidence_url_pending; batch_reverification_required","stage2_evidence_fields":["platform_or_ad_budget_recovery_signal","traffic_or_customer_budget_proxy","relative_strength"],"stage3_evidence_fields":["advertiser_budget_retention_required","segment_margin_or_OPM_bridge_required","repeat_revenue_or_contract_visibility_required"],"stage4b_evidence_fields":["price_only_or_local_peak_watch","high_MAE_guard_if_no_budget_retention_bridge"],"stage4c_evidence_fields":["not_hard_4C_unless_ad_budget_bridge_breaks_and_MAE180_below_minus40"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv","profile_path":"atlas/symbol_profiles/035/035720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-02","entry_price":56500.0,"MFE_30D_pct":10.2,"MFE_90D_pct":17.4,"MFE_180D_pct":22.8,"MAE_30D_pct":-8.6,"MAE_90D_pct":-19.5,"MAE_180D_pct":-33.8,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"proxy_from_prior_v12_row_batch_reverify","peak_price":"batch_reverify","drawdown_after_peak_pct":"batch_reverify","green_lateness_ratio":"not_applicable_or_batch_reverify","four_b_local_peak_proximity":"watch_or_low","four_b_full_window_peak_proximity":"blocked_without_non_price_margin_bridge","four_b_timing_verdict":"local_4B_watch_only_until_ad_budget_retention_and_OPM_bridge_confirmed","four_b_evidence_type":"price_plus_proxy_not_verified_url","four_c_protection_label":"not_4C_but_watch","trigger_outcome_label":"counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_checked_in_fresh_shard_batch_reverify","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035720|Stage2|2024-02-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same C26 family new trigger family; local prior stock-web row reused for same shard path because fresh raw fetch is unstable","independent_evidence_weight":0.72,"do_not_count_as_new_case":false,"component_scores_raw":{"eps_revision":12,"visibility":16,"bottleneck_or_moat":8,"mispricing":14,"valuation_risk":6,"capital_policy":7,"information_quality":5},"raw_total_proxy":68,"score_return_alignment":"bad_false_positive_or_high_MAE","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","case_id":"C26_R8L106_05_030000_STAGE2ACTIONABLE","trigger_id":"T_C26_R8L106_05_030000_STAGE2ACTIONABLE_Stage2Actionable_2024-04-25","symbol":"030000","company_name":"제일기획","round":"R8","loop":106,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_FINAL_PASS_TO_30_PLATFORM_AD_BUDGET_RETENTION_MARGIN_OPERATING_LEVERAGE_BRIDGE","sector":"agency_budget_cycle","loop_objective":"coverage_gap_fill; sector_specific_rule_discovery; counterexample_mining; canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-25","evidence_available_at_that_date":"source_proxy_only_existing_v12_stock_web_row; agency ad budget recovery but low operating leverage beta","evidence_source":"source_proxy_only; evidence_url_pending; batch_reverification_required","stage2_evidence_fields":["platform_or_ad_budget_recovery_signal","traffic_or_customer_budget_proxy","relative_strength"],"stage3_evidence_fields":["advertiser_budget_retention_required","segment_margin_or_OPM_bridge_required","repeat_revenue_or_contract_visibility_required"],"stage4b_evidence_fields":["price_only_or_local_peak_watch","high_MAE_guard_if_no_budget_retention_bridge"],"stage4c_evidence_fields":["not_hard_4C_unless_ad_budget_bridge_breaks_and_MAE180_below_minus40"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/030/030000/2024.csv","profile_path":"atlas/symbol_profiles/030/030000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-25","entry_price":18800.0,"MFE_30D_pct":9.8,"MFE_90D_pct":16.6,"MFE_180D_pct":24.2,"MAE_30D_pct":-5.1,"MAE_90D_pct":-10.3,"MAE_180D_pct":-14.9,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"proxy_from_prior_v12_row_batch_reverify","peak_price":"batch_reverify","drawdown_after_peak_pct":"batch_reverify","green_lateness_ratio":"not_applicable_or_batch_reverify","four_b_local_peak_proximity":"watch_or_low","four_b_full_window_peak_proximity":"not_full_4B","four_b_timing_verdict":"local_4B_watch_only_until_ad_budget_retention_and_OPM_bridge_confirmed","four_b_evidence_type":"price_plus_proxy_not_verified_url","four_c_protection_label":"not_4C_but_watch","trigger_outcome_label":"mixed_positive","current_profile_verdict":"current_profile_too_late_low_beta","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_checked_in_fresh_shard_batch_reverify","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|030000|Stage2-Actionable|2024-04-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same C26 family new trigger family; local prior stock-web row reused for same shard path because fresh raw fetch is unstable","independent_evidence_weight":0.72,"do_not_count_as_new_case":false,"component_scores_raw":{"eps_revision":12,"visibility":22,"bottleneck_or_moat":8,"mispricing":14,"valuation_risk":10,"capital_policy":7,"information_quality":5},"raw_total_proxy":78,"score_return_alignment":"mixed_high_MAE","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","case_id":"C26_R8L106_06_214320_STAGE3YELLOW","trigger_id":"T_C26_R8L106_06_214320_STAGE3YELLOW_Stage3Yellow_2024-05-17","symbol":"214320","company_name":"이노션","round":"R8","loop":106,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_FINAL_PASS_TO_30_PLATFORM_AD_BUDGET_RETENTION_MARGIN_OPERATING_LEVERAGE_BRIDGE","sector":"agency_global_ad_budget","loop_objective":"coverage_gap_fill; sector_specific_rule_discovery; counterexample_mining; canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-17","evidence_available_at_that_date":"source_proxy_only_existing_v12_stock_web_row; global agency recovery + OPM/capital return bridge","evidence_source":"source_proxy_only; evidence_url_pending; batch_reverification_required","stage2_evidence_fields":["platform_or_ad_budget_recovery_signal","traffic_or_customer_budget_proxy","relative_strength"],"stage3_evidence_fields":["advertiser_budget_retention_required","segment_margin_or_OPM_bridge_required","repeat_revenue_or_contract_visibility_required"],"stage4b_evidence_fields":["price_only_or_local_peak_watch","high_MAE_guard_if_no_budget_retention_bridge"],"stage4c_evidence_fields":["not_hard_4C_unless_ad_budget_bridge_breaks_and_MAE180_below_minus40"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214320/2024.csv","profile_path":"atlas/symbol_profiles/214/214320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":22100.0,"MFE_30D_pct":17.0,"MFE_90D_pct":29.5,"MFE_180D_pct":36.8,"MAE_30D_pct":-6.0,"MAE_90D_pct":-11.5,"MAE_180D_pct":-18.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"proxy_from_prior_v12_row_batch_reverify","peak_price":"batch_reverify","drawdown_after_peak_pct":"batch_reverify","green_lateness_ratio":"not_applicable_or_batch_reverify","four_b_local_peak_proximity":"high","four_b_full_window_peak_proximity":"not_full_4B","four_b_timing_verdict":"local_4B_watch_only_until_ad_budget_retention_and_OPM_bridge_confirmed","four_b_evidence_type":"price_plus_proxy_not_verified_url","four_c_protection_label":"not_4C_but_watch","trigger_outcome_label":"positive","current_profile_verdict":"current_profile_too_late_or_green_strictness_watch","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_checked_in_fresh_shard_batch_reverify","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|214320|Stage3-Yellow|2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same C26 family new trigger family; local prior stock-web row reused for same shard path because fresh raw fetch is unstable","independent_evidence_weight":0.72,"do_not_count_as_new_case":false,"component_scores_raw":{"eps_revision":18,"visibility":22,"bottleneck_or_moat":8,"mispricing":14,"valuation_risk":10,"capital_policy":7,"information_quality":5},"raw_total_proxy":84,"score_return_alignment":"good","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","case_id":"C26_R8L106_07_443250_STAGE2","trigger_id":"T_C26_R8L106_07_443250_STAGE2_Stage2_2024-02-26","symbol":"443250","company_name":"레뷰코퍼레이션","round":"R8","loop":106,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_FINAL_PASS_TO_30_PLATFORM_AD_BUDGET_RETENTION_MARGIN_OPERATING_LEVERAGE_BRIDGE","sector":"influencer_marketing_platform","loop_objective":"coverage_gap_fill; sector_specific_rule_discovery; counterexample_mining; canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-02-26","evidence_available_at_that_date":"source_proxy_only_existing_v12_stock_web_row; influencer marketing price spike without reorder retention bridge","evidence_source":"source_proxy_only; evidence_url_pending; batch_reverification_required","stage2_evidence_fields":["platform_or_ad_budget_recovery_signal","traffic_or_customer_budget_proxy","relative_strength"],"stage3_evidence_fields":["advertiser_budget_retention_required","segment_margin_or_OPM_bridge_required","repeat_revenue_or_contract_visibility_required"],"stage4b_evidence_fields":["price_only_or_local_peak_watch","high_MAE_guard_if_no_budget_retention_bridge"],"stage4c_evidence_fields":["not_hard_4C_unless_ad_budget_bridge_breaks_and_MAE180_below_minus40"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/443/443250/2024.csv","profile_path":"atlas/symbol_profiles/443/443250.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":16000.0,"MFE_30D_pct":40.0,"MFE_90D_pct":55.0,"MFE_180D_pct":60.0,"MAE_30D_pct":-15.0,"MAE_90D_pct":-28.0,"MAE_180D_pct":-45.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"proxy_from_prior_v12_row_batch_reverify","peak_price":"batch_reverify","drawdown_after_peak_pct":"batch_reverify","green_lateness_ratio":"not_applicable_or_batch_reverify","four_b_local_peak_proximity":"high","four_b_full_window_peak_proximity":"blocked_without_non_price_margin_bridge","four_b_timing_verdict":"local_4B_watch_only_until_ad_budget_retention_and_OPM_bridge_confirmed","four_b_evidence_type":"price_plus_proxy_not_verified_url","four_c_protection_label":"4C_watch_if_no_bridge_refresh","trigger_outcome_label":"counterexample","current_profile_verdict":"current_profile_4b_too_early_high_mae","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"not_checked_in_fresh_shard_batch_reverify","same_entry_group_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|443250|Stage2|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same C26 family new trigger family; local prior stock-web row reused for same shard path because fresh raw fetch is unstable","independent_evidence_weight":0.72,"do_not_count_as_new_case":false,"component_scores_raw":{"eps_revision":12,"visibility":16,"bottleneck_or_moat":8,"mispricing":14,"valuation_risk":6,"capital_policy":7,"information_quality":5},"raw_total_proxy":68,"score_return_alignment":"bad_false_positive_or_high_MAE","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
```

## 5. Aggregate metrics

```jsonl
{"row_type":"aggregate_metrics","schema_version":"v12","round":"R8","loop":106,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_FINAL_PASS_TO_30_PLATFORM_AD_BUDGET_RETENTION_MARGIN_OPERATING_LEVERAGE_BRIDGE","new_independent_case_count":7,"cross_canonical_price_row_reuse_count":0,"same_archetype_new_symbol_count":7,"same_archetype_new_trigger_family_count":7,"calibration_usable_case_count":7,"calibration_usable_trigger_count":7,"positive_case_count":2,"mixed_positive_count":2,"counterexample_count":3,"local_4b_watch_count":5,"current_profile_error_count":7,"avg_MFE_30D_pct":17.01,"avg_MAE_30D_pct":-8.99,"avg_MFE_90D_pct":28.5,"avg_MAE_90D_pct":-17.77,"avg_MFE_180D_pct":34.09,"avg_MAE_180D_pct":-27.81,"coverage_gap_static_rows_before":3,"coverage_gap_static_rows_after_if_accepted":10,"coverage_gap_conversation_local_before_approx":23,"coverage_gap_conversation_local_after_if_accepted_approx":30,"loop_contribution_label":"canonical_archetype_rule_candidate; C26 local 30-row floor reached"}
```

## 6. Shadow rule candidate

```jsonl
{"row_type":"shadow_weight_candidate","schema_version":"v12","round":"R8","loop":106,"canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","do_not_propose_new_weight_delta":false,"new_axis_proposed":["C26_PLATFORM_AD_BUDGET_RETENTION_OPM_BRIDGE_REQUIRED","C26_ADTECH_PRICE_ONLY_LOCAL_4B_CAP","C26_LARGE_PLATFORM_SEGMENT_MARGIN_BRIDGE_REQUIRED","C26_AGENCY_LOW_BETA_STAGE3_CAP_UNLESS_OPERATING_LEVERAGE_CONFIRMED","C26_INFLUENCER_MARKETING_REORDER_RETENTION_GUARD","C26_HIGH_MAE_POST_SPIKE_REVERSION_GUARD"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[]}
```

## 7. Residual contribution summary

```text
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
current_profile_error_count = 7
```

Observed residual error:

```text
1. C26 headlines often look strong when platform/ad/AI-marketing language appears, but the durable outcome depends on advertiser budget retention and OPM bridge.
2. Small adtech and influencer-marketing names can show large MFE, yet the same rows often carry deep MAE after the local spike.
3. Large platforms need segment-level margin confirmation; platform scale alone should not unlock Green.
4. Agency names can be low-beta positives, but Stage3-Green should require evidence that budget recovery becomes operating leverage, not merely revenue stabilization.
```

## 8. Proposed canonical rule compression

```text
C26_PLATFORM_AD_BUDGET_RETENTION_OPM_BRIDGE_REQUIRED:
    Promote C26 beyond Stage2 only when ad budget recovery is tied to retained advertiser spend, platform monetization, or repeat campaign revenue, and when OPM/segment margin is visible.

C26_ADTECH_PRICE_ONLY_LOCAL_4B_CAP:
    If the evidence is mostly price movement or AI/adtech narrative, cap as local 4B watch rather than full 4B or Stage3-Green.

C26_LARGE_PLATFORM_SEGMENT_MARGIN_BRIDGE_REQUIRED:
    For NAVER/Kakao-like platforms, require segment ad commerce margin or operating leverage, not just traffic or macro ad recovery.

C26_AGENCY_LOW_BETA_STAGE3_CAP_UNLESS_OPERATING_LEVERAGE_CONFIRMED:
    Agency ad recovery can be positive but should not receive Green unless OPM/revision/capital-return bridge is explicit.

C26_INFLUENCER_MARKETING_REORDER_RETENTION_GUARD:
    Creator/influencer platform spikes require reorder/retention proof; otherwise high-MFE/high-MAE rows remain counterexamples.
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research session.

When batch-applying this MD later:
1. Re-open the listed stock-web profile and tradable shard paths.
2. Verify entry_date, entry_price, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, and MAE_180D_pct.
3. Reject or mark narrative_only any row whose 180D forward window overlaps a corporate-action candidate window.
4. Preserve canonical trigger labels: Stage2, Stage2-Actionable, Stage3-Yellow, Stage3-Green, 4B, 4C.
5. If verified, add C26-specific guards for ad budget retention, OPM bridge, platform segment-margin bridge, and price-only local 4B cap.
6. Do not change production scoring directly from this MD; emit a patch spec for reviewer approval.
```

## 10. Next research state

```text
completed_round = R8
completed_loop = 106
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_final_pass_to_30, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_final_pass_to_30, C27_CONTENT_IP_GLOBAL_MONETIZATION_final_pass_to_30, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_second_pass_to_30, C05_EPC_MEGA_CONTRACT_MARGIN_GAP_second_pass_to_30, C02_POWER_GRID_DATACENTER_CAPEX_second_pass_to_30
```
