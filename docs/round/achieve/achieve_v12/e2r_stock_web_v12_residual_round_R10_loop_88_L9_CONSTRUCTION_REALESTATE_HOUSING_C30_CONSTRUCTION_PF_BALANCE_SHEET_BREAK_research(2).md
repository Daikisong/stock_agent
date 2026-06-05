# E2R Stock-Web v12 Residual Research — R10 Loop 88 / L9 / C30

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R10
loop: 88
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: ENGINEERING_BACKLOG_CASH_BRIDGE_VS_REGIONAL_CONSTRUCTION_POLICY_THEME_DECAY
sector: construction / real estate / housing / PF balance-sheet / engineering backlog / liquidity repair
output_file: e2r_stock_web_v12_residual_round_R10_loop_88_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R9 loop 88`.

```text
scheduled_round = R10
scheduled_loop = 88
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

R10 is restricted to construction / real estate / housing.  
C30 remains the target because the construction bucket is still dominated by PF exposure, liquidity, financing trust, backlog quality, margin protection and cash conversion gaps.

No-Repeat Index snapshot:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rows = 81
symbols = 31
good/bad Stage2 = 16/29
4B/4C = 3/4
top-covered = 002990, 294870, 375500, 004960, 013580, 006360
```

This loop avoids the top-covered list and also avoids previous R10 loop sets:

```text
R10 loop87: 010780, 001260, 013360
R10 loop86: 012630, 000720, 003070
R10 loop85: 021320, 001840, 002410
R10 loop84: 035890, 001470, 002780
R10 loop83: 047040, 014790, 005960
```

Candidate notes:

```text
001880/DL건설 was rejected as a representative because 2024 forward coverage ended early around delisting/merger behavior.
009410/태영건설 was rejected as a representative because the 2024 path includes large suspension/reopening/corporate-action contamination.
```

Selected symbols:

```text
028050, 002460, 091590
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"028050","company_name":"삼성E&A","profile_path":"atlas/symbol_profiles/028/028050.json","first_date":"1997-01-03","last_date":"2026-02-20","trading_day_count":7265,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["1997-08-22","1999-01-13","1999-05-26","1999-09-29","2016-02-26"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window. Name changes from 삼성엔지니어링 to 삼성E&A during 2024, but price path remains continuous.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"002460","company_name":"HS화성","profile_path":"atlas/symbol_profiles/002/002460.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7764,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1996-01-03","1997-12-17","2002-02-08"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window. Name changes from 화성산업 to HS화성 during 2024, but selected price path is continuous.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"091590","company_name":"남화토건","profile_path":"atlas/symbol_profiles/091/091590.json","first_date":"2012-01-31","last_date":"2026-02-20","trading_day_count":3454,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"028050","trigger_type":"Stage2-Actionable-EngineeringBacklogCashBridge-Positive","entry_date":"2024-02-01","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and prior R10 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002460","trigger_type":"Stage2-FalsePositive-RegionalConstructionValueRebound-NoPFBacklogCashBridge","entry_date":"2024-02-05","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and prior R10 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"091590","trigger_type":"Stage2-FalsePositive-SmallcapConstructionPolicyTheme-NoLiquidityCashBridge","entry_date":"2024-01-02","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and prior R10 loop sets"}
```

## 4. Research question

C30 is not “construction stock bounced.”  
The useful signal must prove a balance-sheet bridge: PF exposure containment, liquidity repair, financing trust, backlog quality, margin protection and cash conversion. Without that bridge, a construction-policy rebound is scaffolding with no bolts; it can sway in the wind but should not carry model weight.

Residual question:

```text
Can C30 distinguish:
1. engineering / plant backlog / cash bridge with usable MFE and controlled early MAE,
2. regional construction value rebound without PF/backlog/cash bridge,
3. small-cap construction-policy theme where low MFE and deep MAE expose missing liquidity and cash conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C30_R10L88_028050_SAMSUNG_EA_ENGINEERING_BACKLOG_CASH","symbol":"028050","company_name":"삼성E&A","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"ENGINEERING_BACKLOG_CASH_BRIDGE","case_type":"watch_positive_control","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-EngineeringBacklogCashBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_MFE90_ge20_low_MAE_later_drawdown","current_profile_verdict":"current_profile_correct_if_backlog_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Engineering/backlog/cash proxy generated a 20%+ MFE with low early MAE. Later drawdown keeps Green strict and requires exact backlog/margin/cash evidence."}
{"row_type":"case","case_id":"C30_R10L88_002460_HS_REGIONAL_CONSTRUCTION_NO_BRIDGE","symbol":"002460","company_name":"HS화성","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_CONSTRUCTION_VALUE_REBOUND_WITHOUT_PF_BACKLOG_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-RegionalConstructionValueRebound-NoPFBacklogCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_moderate_to_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_regional_construction_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Regional construction/value rebound had almost no MFE and later MAE without PF exposure repair, backlog quality or cash bridge."}
{"row_type":"case","case_id":"C30_R10L88_091590_NAMHWA_SMALLCAP_POLICY_THEME","symbol":"091590","company_name":"남화토건","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALLCAP_CONSTRUCTION_POLICY_THEME_WITHOUT_LIQUIDITY_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SmallcapConstructionPolicyTheme-NoLiquidityCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_smallcap_policy_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Small-cap construction-policy theme had near-zero MFE and deep MAE without PF/liquidity/backlog/cash bridge. Later small rebounds should not validate the original entry."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 028050 삼성E&A — engineering backlog / margin / cash bridge positive control

Entry row: `2024-02-01 c=23250`.  
Observed path: early low `2024-02-01 l=22350`, high `2024-03-15 h=28150`, and later low `2024-12-09 l=16300`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L88_C30_028050_20240201_STAGE2_ENGINEERING_BACKLOG_CASH","case_id":"C30_R10L88_028050_SAMSUNG_EA_ENGINEERING_BACKLOG_CASH","symbol":"028050","company_name":"삼성E&A","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"ENGINEERING_BACKLOG_CASH_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-EngineeringBacklogCashBridge-Positive","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":23250.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_engineering_backlog_cash_bridge_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; engineering backlog quality, project margin and cash conversion treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["engineering_backlog_quality_proxy","project_margin_proxy","cash_conversion_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_backlog_source_pending","order_margin_source_pending","working_capital_pending","source_url_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.08,"MFE_90D_pct":21.08,"MFE_180D_pct":21.08,"MAE_30D_pct":-3.87,"MAE_90D_pct":-3.87,"MAE_180D_pct":-29.89,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-15","peak_price":28150.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":16300.0,"drawdown_after_peak_pct":-42.10,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B; late drawdown blocks Green without exact backlog/margin/cash evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_MFE90_ge20_low_MAE_later_drawdown","current_profile_verdict":"current_profile_correct_if_backlog_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window; name_change_to_Samsung_EA_inside_2024_but_price_path_continuous","same_entry_group_id":"028050_2024-02-01_23250","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 can allow Stage2/Yellow when construction-adjacent strength is tied to engineering backlog, margin and cash conversion. Green remains strict because late drawdown can be large without exact evidence."}
```

### 6.2 002460 HS화성 — regional construction/value rebound without PF/backlog/cash bridge

Entry row: `2024-02-05 c=11170`.  
Observed path: local high `2024-02-06 h=11200`, mid-year grind lower, and late-year low `2024-12-09 l=8320`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L88_C30_002460_20240205_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION","case_id":"C30_R10L88_002460_HS_REGIONAL_CONSTRUCTION_NO_BRIDGE","symbol":"002460","company_name":"HS화성","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_CONSTRUCTION_VALUE_REBOUND_WITHOUT_PF_BACKLOG_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-RegionalConstructionValueRebound-NoPFBacklogCashBridge","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":11170.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_regional_construction_value_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; regional construction/value rebound treated as insufficient without PF exposure repair, backlog quality, liquidity and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["regional_construction_rebound","low_PBR_value_theme","relative_strength_rebound"],"stage3_evidence_fields":["PF_exposure_repair_missing","backlog_quality_missing","liquidity_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","PF_backlog_cash_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002460/2024.csv","profile_path":"atlas/symbol_profiles/002/002460.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.27,"MFE_90D_pct":0.27,"MFE_180D_pct":0.27,"MAE_30D_pct":-10.03,"MAE_90D_pct":-14.23,"MAE_180D_pct":-25.51,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-06","peak_price":11200.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":8320.0,"drawdown_after_peak_pct":-25.71,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"regional_construction_rebound_without_PF_backlog_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","PF_backlog_cash_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_moderate_to_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_regional_construction_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window; name_change_to_HS_Hwasung_inside_2024_but_price_path_continuous","same_entry_group_id":"002460_2024-02-05_11170","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 should not promote regional construction/value rebounds without PF repair, liquidity, backlog quality and cash conversion. Near-zero MFE plus moderate-to-deep MAE routes to 4B-watch."}
```

### 6.3 091590 남화토건 — small-cap construction-policy theme without liquidity/cash bridge

Entry row: `2024-01-02 c=7140`.  
Observed path: same-day high `2024-01-02 h=7260`, spring drawdown, and later low `2024-12-09 l=3720`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L88_C30_091590_20240102_STAGE2_FALSE_POSITIVE_SMALLCAP_POLICY","case_id":"C30_R10L88_091590_NAMHWA_SMALLCAP_POLICY_THEME","symbol":"091590","company_name":"남화토건","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALLCAP_CONSTRUCTION_POLICY_THEME_WITHOUT_LIQUIDITY_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-SmallcapConstructionPolicyTheme-NoLiquidityCashBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":7140.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_smallcap_construction_policy_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; small-cap construction policy theme treated as insufficient without liquidity repair, PF containment, backlog quality and cash conversion","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["smallcap_construction_policy_theme","regional_project_keyword","relative_strength_spike"],"stage3_evidence_fields":["liquidity_bridge_missing","PF_repair_missing","backlog_quality_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","liquidity_cash_bridge_missing_watch","late_rebound_not_entry_validation"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/091/091590/2024.csv","profile_path":"atlas/symbol_profiles/091/091590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.68,"MFE_90D_pct":1.68,"MFE_180D_pct":1.68,"MAE_30D_pct":-18.77,"MAE_90D_pct":-33.00,"MAE_180D_pct":-47.90,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-02","peak_price":7260.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":3720.0,"drawdown_after_peak_pct":-48.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"smallcap_construction_policy_theme_without_liquidity_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","liquidity_cash_bridge_missing_watch","late_rebound_not_entry_validation"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_smallcap_policy_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"091590_2024-01-02_7140","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 should not promote small-cap construction-policy themes without liquidity, PF repair, backlog and cash bridge. Near-zero MFE and deep MAE force 4B-watch; later small rebounds do not validate the original entry."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C30_R10L88_028050_SAMSUNG_EA_ENGINEERING_BACKLOG_CASH","trigger_id":"R10L88_C30_028050_20240201_STAGE2_ENGINEERING_BACKLOG_CASH","symbol":"028050","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C30 rewards backlog, margin and cash bridge rather than construction rebound alone","raw_component_scores_before":{"PF_exposure_repair":8,"liquidity_bridge":9,"financing_trust":9,"backlog_quality":13,"margin_bridge":11,"cash_conversion":10,"relative_strength_score":11,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":68,"stage_label_before":"Stage2-Watch/Yellow-candidate","raw_component_scores_after":{"PF_exposure_repair":10,"liquidity_bridge":11,"financing_trust":11,"backlog_quality":16,"margin_bridge":14,"cash_conversion":12,"relative_strength_score":12,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":81,"stage_label_after":"Stage2-Actionable/Stage3-Yellow-Watch","component_delta_explanation":"Backlog/margin/cash bridge and MFE90>=20 support Yellow-watch; late drawdown and proxy-only evidence block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C30_R10L88_002460_HS_REGIONAL_CONSTRUCTION_NO_BRIDGE","trigger_id":"R10L88_C30_002460_20240205_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION","symbol":"002460","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"regional construction/value rebound without PF/backlog/cash bridge should be blocked","raw_component_scores_before":{"PF_exposure_repair":1,"liquidity_bridge":1,"financing_trust":1,"backlog_quality":2,"margin_bridge":0,"cash_conversion":0,"relative_strength_score":5,"valuation_repricing_score":3,"execution_risk_score":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":0,"margin_bridge":0,"cash_conversion":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and later MAE convert regional construction rebound into missing PF/backlog/cash bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C30_R10L88_091590_NAMHWA_SMALLCAP_POLICY_THEME","trigger_id":"R10L88_C30_091590_20240102_STAGE2_FALSE_POSITIVE_SMALLCAP_POLICY","symbol":"091590","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"small-cap construction-policy theme without liquidity/cash bridge should remain Watch/blocked","raw_component_scores_before":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":1,"margin_bridge":0,"cash_conversion":0,"relative_strength_score":6,"valuation_repricing_score":2,"execution_risk_score":-16,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":0,"margin_bridge":0,"cash_conversion":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE require liquidity/PF/backlog/cash bridge before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R10L88_C30_P0_CURRENT","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C30 needs explicit backlog/liquidity/PF/cash bridge gates and theme-rebound 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":7.68,"avg_MAE90_pct":-17.03,"avg_MFE180_pct":7.68,"avg_MAE180_pct":-34.43,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C30_PF_liquidity_backlog_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R10L88_C30_P1_SECTOR_SPECIFIC","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P1_L9_PF_liquidity_backlog_cash_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L9 construction signals need PF exposure containment, liquidity repair, financing trust, backlog quality, margin or cash bridge before Stage2-Actionable","changed_axes":["PF_exposure_repair_required","liquidity_financing_required","construction_rebound_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_PF_repair_liquidity_financing_backlog_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":7.68,"avg_MAE90_pct":-17.03,"avg_MFE180_pct":7.68,"avg_MAE180_pct":-34.43,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R10L88_C30_P2_CANONICAL","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P2_C30_PF_liquidity_backlog_cash_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C30 should reward balance-sheet and backlog mechanics, not low-PBR construction or policy-theme labels","changed_axes":["C30_PF_liquidity_backlog_cash_bridge_required","C30_regional_construction_rebound_local_4B_guard","C30_low_MFE_deep_MAE_guard"],"changed_thresholds":{"stage2_yellow_gate":"PF_repair_liquidity_financing_backlog_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":7.68,"avg_MAE90_pct":-17.03,"avg_MFE180_pct":7.68,"avg_MAE180_pct":-34.43,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R10L88_C30_P3_COUNTEREXAMPLE_GUARD","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P3_C30_near_zero_MFE_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<5 and MAE180<=-25 while PF/liquidity/cash bridge is missing, block Yellow/Green and route to 4B-watch","changed_axes":["C30_near_zero_MFE_guardrail","C30_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_5_and_MAE180_le_minus_25"},"eligible_trigger_count":3,"avg_MFE90_pct":7.68,"avg_MAE90_pct":-17.03,"avg_MFE180_pct":7.68,"avg_MAE180_pct":-34.43,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_ENGINEERING_BACKLOG_VS_REGIONAL_CONSTRUCTION_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":7.68,"avg_MAE90_pct":-17.03,"avg_MFE180_pct":7.68,"avg_MAE180_pct":-34.43,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_5":0.67,"stage2_bad_entry_rate_MAE180_le_minus_25":1.0,"interpretation":"C30 needs bridge discipline. 삼성E&A shows engineering backlog/margin/cash bridge can support Yellow-watch, while HS화성 and 남화토건 show regional/small-cap construction rebounds should not be promoted without PF, liquidity, backlog and cash evidence."}
{"row_type":"stage_transition_summary","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"028050","trigger_type":"Stage2-Actionable-EngineeringBacklogCashBridge-Positive","entry_date":"2024-02-01","stage2_to_90D_outcome":"good_stage2_MFE90_ge20_low_MAE","stage2_to_180D_outcome":"watch_positive_with_later_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when backlog, margin and cash bridge exists; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002460","trigger_type":"Stage2-FalsePositive-RegionalConstructionValueRebound-NoPFBacklogCashBridge","entry_date":"2024-02-05","stage2_to_90D_outcome":"weak_stage2_near_zero_MFE","stage2_to_180D_outcome":"failed_regional_construction_rebound_MAE_expansion","MFE90_ge_20":false,"MAE180_le_minus_25":true,"transition_note":"Regional construction rebound without PF/backlog/cash bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"091590","trigger_type":"Stage2-FalsePositive-SmallcapConstructionPolicyTheme-NoLiquidityCashBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_high_MAE","stage2_to_180D_outcome":"failed_smallcap_policy_theme_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Small-cap construction-policy theme without liquidity/cash bridge should stay Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"regional_smallcap_construction_rebound_overcredit_without_PF_liquidity_backlog_cash_bridge","contribution":"Adds two C30 local 4B/MAE counterexamples against one engineering backlog/cash positive, avoiding C30 top-covered and previous R10 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"ENGINEERING_BACKLOG_CASH_BRIDGE_VS_REGIONAL_CONSTRUCTION_POLICY_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C30 now has non-top-symbol engineering backlog/cash positive and two regional/small-cap construction weak-bridge counterexamples; next R10 loops should exact-URL repair PF exposure, liquidity, financing trust, backlog quality, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_PF_liquidity_backlog_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"028050 worked when backlog/margin/cash proxy was present; 002460 and 091590 failed when only regional construction/value or small-cap policy theme existed."}
{"row_type":"shadow_weight","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_regional_construction_rebound_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Regional and small-cap construction rows showed near-zero MFE and MAE expansion without PF/liquidity/backlog/cash bridge."}
{"row_type":"shadow_weight","round":"R10","loop":"88","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_late_drawdown_Green_strict_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"028050 is a positive-control path but later drawdown shows that Green should require exact backlog, margin, working-capital and cash evidence."}
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
  - regional_construction_rebound_overcredit
  - smallcap_construction_policy_theme_overcredit
  - PF_liquidity_bridge_missing
  - backlog_cash_conversion_bridge_missing
new_axis_proposed:
  - C30_PF_liquidity_backlog_cash_bridge_required_shadow_only
  - C30_regional_construction_rebound_local_4B_watch_guard_shadow_only
  - C30_late_drawdown_Green_strict_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C30
  - full_4b_requires_non_price_evidence within C30
  - hard_4c_thesis_break_routes_to_4c within C30
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
3. Confirm R10 / L9 / C30 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C30 top-covered symbols
   - previous R10 loop87 symbols
   - previous R10 loop86 symbols
   - previous R10 loop85 symbols
   - previous R10 loop84 symbols
   - previous R10 loop83 symbols
6. Confirm 001880 and 009410 were not used as representative rows because of forward-window / suspension / corporate-action contamination.
7. If aggregate support remains stable after exact evidence URL repair, consider C30-scoped safe patch candidates:
   - C30_PF_liquidity_backlog_cash_bridge_required
   - C30_regional_construction_rebound_local_4B_watch_guard
   - C30_late_drawdown_Green_strict_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R10
completed_loop = 88
next_round = R11
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.
```
