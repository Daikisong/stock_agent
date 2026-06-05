# E2R Stock-Web v12 Residual Research — R8 Loop 90 / L8 / C27

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R8
loop: 90
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: MEDIA_COMMERCE_IP_MONETIZATION_BRIDGE_VS_DRAMA_VFX_CONTENT_THEME_DECAY
sector: platform / content / IP / media commerce / drama production / VFX / global monetization
output_file: e2r_stock_web_v12_residual_round_R8_loop_90_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R7 loop 90`.

```text
scheduled_round = R8
scheduled_loop = 90
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
```

R8 is restricted to platform / content / software / security.  
C27 is selected because the recent R8 sequence moved through:

```text
R8 loop85: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
R8 loop86: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
R8 loop87: C27_CONTENT_IP_GLOBAL_MONETIZATION
R8 loop88: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
R8 loop89: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

After C28, the R8 lane returns to C27.

No-Repeat Index snapshot:

```text
C27_CONTENT_IP_GLOBAL_MONETIZATION
rows = 39
symbols = 15
good/bad Stage2 = 20/6
4B/4C = 3/1
top-covered = 263750, 112040, 122870, 293490, 259960, 376300
```

This loop avoids the C27 top-covered symbols and recent R8 loop symbols:

```text
R8 loop85 C26: 067160, 089600, 123570
R8 loop86 C28: 030520, 053800, 049480
R8 loop87 C27: 251270, 035900, 352820
R8 loop88 C26: 230360, 216050, 273060
R8 loop89 C28: 060850, 067920, 304100
```

Candidate hygiene note:

```text
During this execution path, a R7/C24 bio candidate sweep was visible in the surrounding session history.
Those rows are not used in this R8/C27 output.
```

Selected symbols:

```text
035760, 241840, 206560
```

This loop tests:

```text
media-commerce / content IP monetization bridge
vs
drama production IP rebound without new global distribution / margin bridge
vs
VFX / virtual-production content theme spike without backlog, licensing and margin bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"035760","company_name":"CJ ENM","profile_path":"atlas/symbol_profiles/035/035760.json","first_date":"1999-11-23","last_date":"2026-02-20","trading_day_count":6448,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2006-09-12","2010-09-30","2018-07-18"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-change candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"241840","company_name":"에이스토리","profile_path":"atlas/symbol_profiles/241/241840.json","first_date":"2019-07-19","last_date":"2026-02-20","trading_day_count":1617,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"206560","company_name":"덱스터","profile_path":"atlas/symbol_profiles/206/206560.json","first_date":"2015-12-22","last_date":"2026-02-20","trading_day_count":2491,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2016-12-21","2017-01-09"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"035760","trigger_type":"Stage2-Actionable-MediaCommerceContentIPMonetizationBridge-Positive","entry_date":"2024-01-22","duplicate_status":"new C27 symbol/trigger/date combination outside top-covered and previous R8 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"241840","trigger_type":"Stage2-FalsePositive-DramaProductionIPRebound-NoGlobalDistributionMarginBridge","entry_date":"2024-01-02","duplicate_status":"new C27 symbol/trigger/date combination outside top-covered and previous R8 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"206560","trigger_type":"Stage2-FalsePositive-VFXVirtualProductionTheme-NoBacklogLicensingMarginBridge","entry_date":"2024-01-09","duplicate_status":"new C27 symbol/trigger/date combination outside top-covered and previous R8 loop symbols"}
```

## 4. Research question

C27 is not “콘텐츠주가 움직였다.”  
The useful content/IP signal must prove the bridge from attention to monetization:

```text
global distribution contract
IP ownership or revenue share
platform/channel quality
library monetization
seasonality and release slate
production-margin discipline
licensing / merchandising / commerce conversion
cash collection
```

A content headline without that bridge is a trailer with no distribution contract behind it. The audience sees the light, but the producer has not yet booked the cash waterfall.

Residual question:

```text
Can C27 distinguish:
1. media-commerce / content IP monetization bridge with strong MFE and tolerable early MAE,
2. drama-production IP rebound where no new global distribution, licensing or margin bridge exists,
3. VFX / virtual-production content theme spike where price movement is not backlog, licensing or cash-flow evidence?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C27_R8L90_035760_CJENM_MEDIA_COMMERCE_IP","symbol":"035760","company_name":"CJ ENM","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MEDIA_COMMERCE_CONTENT_IP_MONETIZATION_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-MediaCommerceContentIPMonetizationBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_MFE90_ge30_tolerable_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_distribution_IP_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Media-commerce / content IP monetization proxy produced MFE90 above 30% with tolerable early MAE. Green still requires exact distribution, IP ownership/revenue-share, margin and cash evidence."}
{"row_type":"case","case_id":"C27_R8L90_241840_ASTORY_DRAMA_IP_REBOUND","symbol":"241840","company_name":"에이스토리","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"DRAMA_PRODUCTION_IP_REBOUND_WITHOUT_GLOBAL_DISTRIBUTION_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DramaProductionIPRebound-NoGlobalDistributionMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_distribution_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_drama_IP_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Drama-production IP rebound had low forward MFE and deep drawdown without confirmed global distribution, licensing, release slate, margin or cash bridge."}
{"row_type":"case","case_id":"C27_R8L90_206560_DEXTER_VFX_THEME","symbol":"206560","company_name":"덱스터","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"VFX_VIRTUAL_PRODUCTION_THEME_WITHOUT_BACKLOG_LICENSING_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-VFXVirtualProductionTheme-NoBacklogLicensingMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_late_spike_not_validation","current_profile_verdict":"current_profile_false_positive_if_VFX_content_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"VFX/virtual-production content theme spike had only small original-entry MFE and deep later MAE. Later December volatility should not validate the original weak bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 035760 CJ ENM — media-commerce / content IP monetization bridge positive

Entry row: `2024-01-22 c=66500`.  
Observed path: early low `2024-01-22 l=62500`, high `2024-02-08 h=89300`, and late-year low `2024-12-27 l=53400`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L90_C27_035760_20240122_STAGE2_MEDIA_COMMERCE_IP","case_id":"C27_R8L90_035760_CJENM_MEDIA_COMMERCE_IP","symbol":"035760","company_name":"CJ ENM","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MEDIA_COMMERCE_CONTENT_IP_MONETIZATION_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-MediaCommerceContentIPMonetizationBridge-Positive","trigger_date":"2024-01-22","entry_date":"2024-01-22","entry_price":66500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_media_commerce_content_IP_monetization_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; media-commerce content IP distribution, library monetization and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["global_distribution_proxy","content_IP_revenue_share_proxy","commerce_monetization_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_distribution_contract_pending","IP_ownership_or_revenue_share_pending","margin_bridge_pending","cash_collection_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035760/2024.csv","profile_path":"atlas/symbol_profiles/035/035760.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":34.29,"MFE_90D_pct":34.29,"MFE_180D_pct":34.29,"MAE_30D_pct":-6.02,"MAE_90D_pct":-6.02,"MAE_180D_pct":-19.70,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-08","peak_price":89300.0,"max_drawdown_low_date":"2024-12-27","max_drawdown_low":53400.0,"drawdown_after_peak_pct":-40.20,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_distribution_IP_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_MFE90_ge30_tolerable_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_distribution_IP_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"035760_2024-01-22_66500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C27 can allow Stage2/Yellow when content strength is tied to distribution, IP monetization, commerce conversion, production-margin discipline and cash collection. Green still requires exact source-grade evidence."}
```

### 6.2 241840 에이스토리 — drama-production IP rebound without global distribution / margin bridge

Entry row: `2024-01-02 c=13800`.  
Observed path: high `2024-01-03 h=14360`, then long decline toward `2024-10-25 l=6610` and late-year lows around `2024-12-09 l=7260`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L90_C27_241840_20240102_STAGE2_FALSE_POSITIVE_DRAMA_IP","case_id":"C27_R8L90_241840_ASTORY_DRAMA_IP_REBOUND","symbol":"241840","company_name":"에이스토리","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"DRAMA_PRODUCTION_IP_REBOUND_WITHOUT_GLOBAL_DISTRIBUTION_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-DramaProductionIPRebound-NoGlobalDistributionMarginBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":13800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_drama_production_IP_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; drama-production IP rebound treated as insufficient without fresh global distribution, release slate, licensing, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["drama_IP_rebound","content_theme_keyword","relative_strength_rebound"],"stage3_evidence_fields":["global_distribution_missing","fresh_release_slate_missing","licensing_bridge_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE_watch","distribution_margin_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/241/241840/2024.csv","profile_path":"atlas/symbol_profiles/241/241840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.06,"MFE_90D_pct":4.06,"MFE_180D_pct":4.06,"MAE_30D_pct":-18.55,"MAE_90D_pct":-29.57,"MAE_180D_pct":-52.10,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-03","peak_price":14360.0,"max_drawdown_low_date":"2024-10-25","max_drawdown_low":6610.0,"drawdown_after_peak_pct":-53.97,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"drama_IP_rebound_without_global_distribution_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","distribution_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_distribution_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_drama_IP_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"241840_2024-01-02_13800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C27 should not promote drama-production IP rebound without fresh global distribution, licensing, release-slate visibility, margin and cash bridge. Low MFE and deep MAE require Watch/4B routing."}
```

### 6.3 206560 덱스터 — VFX / virtual-production theme without backlog/licensing/margin bridge

Entry row: `2024-01-09 c=10280`, on a VFX/content theme spike.  
Observed path: same-day high `2024-01-09 h=10620`, then lows around `2024-12-09 l=5900`. Later December volatility is not counted as original-entry validation.

```jsonl
{"row_type":"trigger","trigger_id":"R8L90_C27_206560_20240109_STAGE2_FALSE_POSITIVE_VFX_THEME","case_id":"C27_R8L90_206560_DEXTER_VFX_THEME","symbol":"206560","company_name":"덱스터","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"VFX_VIRTUAL_PRODUCTION_THEME_WITHOUT_BACKLOG_LICENSING_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;late_rebound_not_entry_validation","trigger_type":"Stage2-FalsePositive-VFXVirtualProductionTheme-NoBacklogLicensingMarginBridge","trigger_date":"2024-01-09","entry_date":"2024-01-09","entry_price":10280.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_VFX_virtual_production_content_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; VFX/virtual-production content theme treated as insufficient without production backlog, licensing, global channel quality, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["VFX_content_theme","virtual_production_keyword","relative_strength_spike"],"stage3_evidence_fields":["production_backlog_missing","licensing_bridge_missing","global_channel_quality_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_MFE","late_spike_not_entry_validation","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/206/206560/2024.csv","profile_path":"atlas/symbol_profiles/206/206560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.31,"MFE_90D_pct":3.31,"MFE_180D_pct":3.31,"MAE_30D_pct":-23.15,"MAE_90D_pct":-27.24,"MAE_180D_pct":-42.61,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-09","peak_price":10620.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":5900.0,"drawdown_after_peak_pct":-44.44,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"VFX_content_theme_without_backlog_licensing_margin_bridge_should_be_4B_watch; late_December_spike_not_original_entry_validation","four_b_evidence_type":["price_only","late_spike_not_entry_validation","backlog_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_late_spike_not_validation","current_profile_verdict":"current_profile_false_positive_if_VFX_content_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"206560_2024-01-09_10280","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C27 should not count VFX/theme price movement as IP monetization evidence. Backlog, licensing, global channel quality, margin and cash evidence must be repaired before Yellow/Green; late spikes need fresh trigger dates."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_R8L90_035760_CJENM_MEDIA_COMMERCE_IP","trigger_id":"R8L90_C27_035760_20240122_STAGE2_MEDIA_COMMERCE_IP","symbol":"035760","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C27 requires global distribution, IP ownership/revenue share, monetization channel, margin and cash bridge rather than content theme alone","raw_component_scores_before":{"global_distribution_score":12,"IP_ownership_score":10,"revenue_share_score":10,"platform_channel_quality_score":11,"library_monetization_score":10,"margin_bridge_score":10,"cash_collection_score":7,"relative_strength_score":13,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"global_distribution_score":15,"IP_ownership_score":12,"revenue_share_score":12,"platform_channel_quality_score":13,"library_monetization_score":12,"margin_bridge_score":12,"cash_collection_score":9,"relative_strength_score":14,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Distribution/IP monetization bridge plus MFE90>30 supports Yellow-watch; exact distribution and cash evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_R8L90_241840_ASTORY_DRAMA_IP_REBOUND","trigger_id":"R8L90_C27_241840_20240102_STAGE2_FALSE_POSITIVE_DRAMA_IP","symbol":"241840","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"drama IP rebound without fresh global distribution and margin bridge should be blocked","raw_component_scores_before":{"global_distribution_score":2,"IP_ownership_score":2,"revenue_share_score":1,"platform_channel_quality_score":1,"library_monetization_score":1,"margin_bridge_score":0,"cash_collection_score":0,"relative_strength_score":5,"valuation_repricing_score":2,"execution_risk_score":-12,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"global_distribution_score":0,"IP_ownership_score":1,"revenue_share_score":0,"platform_channel_quality_score":0,"library_monetization_score":0,"margin_bridge_score":0,"cash_collection_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-20,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE convert drama IP rebound into missing distribution/margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_R8L90_206560_DEXTER_VFX_THEME","trigger_id":"R8L90_C27_206560_20240109_STAGE2_FALSE_POSITIVE_VFX_THEME","symbol":"206560","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"VFX/theme spike without backlog/licensing and margin bridge should remain Watch/4B even if later spike appears","raw_component_scores_before":{"global_distribution_score":1,"IP_ownership_score":0,"revenue_share_score":0,"platform_channel_quality_score":1,"library_monetization_score":0,"margin_bridge_score":0,"cash_collection_score":0,"relative_strength_score":8,"valuation_repricing_score":3,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"global_distribution_score":0,"IP_ownership_score":0,"revenue_share_score":0,"platform_channel_quality_score":0,"library_monetization_score":0,"margin_bridge_score":0,"cash_collection_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Local MFE is price-only; deep MAE and missing backlog/licensing bridge block Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R8L90_C27_P0_CURRENT","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C27 needs explicit global distribution, IP monetization, licensing, margin/cash and late-spike validation taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":13.89,"avg_MAE90_pct":-20.94,"avg_MFE180_pct":13.89,"avg_MAE180_pct":-38.14,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":0.67,"score_return_alignment_verdict":"mixed_without_C27_distribution_IP_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R8L90_C27_P1_SECTOR_SPECIFIC","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_id":"P1_L8_content_IP_monetization_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L8 content/IP signals need global distribution, IP ownership, revenue share, platform/channel quality, licensing, margin or cash conversion before Stage2-Actionable","changed_axes":["global_distribution_required","IP_monetization_required","content_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_distribution_IP_revenue_share_channel_licensing_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":13.89,"avg_MAE90_pct":-20.94,"avg_MFE180_pct":13.89,"avg_MAE180_pct":-38.14,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R8L90_C27_P2_CANONICAL","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_id":"P2_C27_distribution_IP_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C27 should reward IP monetization mechanics, not drama/VFX content labels","changed_axes":["C27_distribution_IP_margin_cash_bridge_required","C27_drama_VFX_theme_local_4B_guard","C27_late_spike_not_entry_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"distribution_or_IP_ownership_plus_margin_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":13.89,"avg_MAE90_pct":-20.94,"avg_MFE180_pct":13.89,"avg_MAE180_pct":-38.14,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R8L90_C27_P3_COUNTEREXAMPLE_GUARD","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","profile_id":"P3_C27_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If distribution/IP bridge is missing, MFE90<10 or MAE180<=-35 should block Yellow/Green; late spikes require fresh trigger and fresh evidence","changed_axes":["C27_low_MFE_guardrail","C27_deep_MAE_4B_guardrail","C27_late_spike_not_validation"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_10_or_MAE180_le_minus_35)"},"eligible_trigger_count":3,"avg_MFE90_pct":13.89,"avg_MAE90_pct":-20.94,"avg_MFE180_pct":13.89,"avg_MAE180_pct":-38.14,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_MEDIA_COMMERCE_POSITIVE_VS_DRAMA_VFX_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":13.89,"avg_MAE90_pct":-20.94,"avg_MFE180_pct":13.89,"avg_MAE180_pct":-38.14,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE180_le_minus35":0.67,"interpretation":"C27 needs bridge discipline. CJ ENM shows media-commerce/content IP monetization can support Yellow-watch, while 에이스토리 and 덱스터 show drama/VFX content theme moves should not be promoted without global distribution, licensing, IP revenue-share, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"035760","trigger_type":"Stage2-Actionable-MediaCommerceContentIPMonetizationBridge-Positive","entry_date":"2024-01-22","stage2_to_90D_outcome":"good_stage2_MFE90_ge30_tolerable_MAE","stage2_to_180D_outcome":"positive_IP_monetization_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when content strength is tied to distribution, IP monetization, margin and cash bridge; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"241840","trigger_type":"Stage2-FalsePositive-DramaProductionIPRebound-NoGlobalDistributionMarginBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"failed_drama_IP_rebound_deep_MAE","MFE90_ge20":false,"MAE180_le_minus35":true,"transition_note":"Drama IP rebound without fresh distribution and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","symbol":"206560","trigger_type":"Stage2-FalsePositive-VFXVirtualProductionTheme-NoBacklogLicensingMarginBridge","entry_date":"2024-01-09","stage2_to_90D_outcome":"price_only_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_VFX_theme_late_spike_not_validation","MFE90_ge20":false,"MAE180_le_minus35":true,"transition_note":"VFX/content theme without backlog/licensing/margin bridge should be treated as 4B-watch; late spike does not validate original entry."}
{"row_type":"residual_contribution","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","residual_type":"drama_VFX_content_theme_overcredit_without_distribution_IP_margin_cash_bridge","contribution":"Adds two C27 4B counterexamples against one media-commerce/IP monetization positive, avoiding C27 top-covered and recent R8 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MEDIA_COMMERCE_IP_MONETIZATION_BRIDGE_VS_DRAMA_VFX_CONTENT_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C27 now has non-top-symbol media-commerce/content IP positive and two drama/VFX weak-bridge counterexamples; next R8 C27 loops should exact-URL repair global distribution, IP ownership/revenue share, platform/channel quality, licensing, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","axis":"C27_distribution_IP_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"035760 worked when media-commerce/content IP bridge existed; 241840 and 206560 failed when content theme lacked distribution, licensing, margin and cash bridge."}
{"row_type":"shadow_weight","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","axis":"C27_drama_VFX_theme_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Drama and VFX rows showed MFE90 below 10 and deep 180D MAE when non-price IP monetization evidence was missing."}
{"row_type":"shadow_weight","round":"R8","loop":"90","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","axis":"C27_late_spike_not_entry_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"206560 shows late volatility should not retroactively validate the original weak entry unless a fresh trigger and fresh distribution/IP bridge evidence exist."}
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
  - content_theme_overcredit
  - drama_IP_rebound_overcredit
  - VFX_theme_price_overcredit
  - distribution_IP_margin_cash_bridge_missing
new_axis_proposed:
  - C27_distribution_IP_margin_cash_bridge_required_shadow_only
  - C27_drama_VFX_theme_local_4B_guard_shadow_only
  - C27_late_spike_not_entry_validation_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows and clean selected 2024 entry windows.  
`035760` and `206560` have historical corporate-action/name-change candidates before 2024, but the selected 2024 windows are usable for price-path residual analysis.  
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
3. Confirm R8 / L8 / C27 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C27 top-covered symbols
   - previous R8 loop85 C26 symbols
   - previous R8 loop86 C28 symbols
   - previous R8 loop87 C27 symbols
   - previous R8 loop88 C26 symbols
   - previous R8 loop89 C28 symbols
6. Confirm accidentally touched R7/C24 candidate rows are not ingested from this MD.
7. If aggregate support remains stable after exact evidence URL repair, consider C27-scoped safe patch candidates:
   - C27_distribution_IP_margin_cash_bridge_required
   - C27_drama_VFX_theme_local_4B_guard
   - C27_late_spike_not_entry_validation_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R8
completed_loop = 90
next_round = R9
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.
```
