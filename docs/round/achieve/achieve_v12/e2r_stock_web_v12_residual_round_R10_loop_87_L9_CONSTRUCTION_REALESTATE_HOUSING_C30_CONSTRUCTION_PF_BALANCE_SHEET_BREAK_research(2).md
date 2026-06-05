# E2R Stock-Web v12 Residual Research — R10 Loop 87 / L9 / C30

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R10
loop: 87
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: MIDCAP_REAL_ESTATE_BALANCE_SHEET_REPAIR_BRIDGE_VS_SMALLCAP_CONSTRUCTION_POLICY_THEME_DECAY
sector: construction / real estate / housing / PF balance sheet / liquidity repair
output_file: e2r_stock_web_v12_residual_round_R10_loop_87_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R9 loop 87`.

```text
scheduled_round = R10
scheduled_loop = 87
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

R10 is restricted to construction / real estate / housing.  
C30 remains the target because it is still the most error-prone construction bucket: PF exposure, financing trust, backlog quality, liquidity bridge, and cash conversion can diverge sharply from construction-policy price spikes.

The No-Repeat Index shows C30 as:

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
R10 loop86: 012630, 000720, 003070
R10 loop85: 021320, 001840, 002410
R10 loop84: 035890, 001470, 002780
R10 loop83: 047040, 014790, 005960
```

Selected symbols:

```text
010780, 001260, 013360
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"010780","company_name":"아이에스동서","profile_path":"atlas/symbol_profiles/010/010780.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7705,"corporate_action_candidate_count":10,"corporate_action_candidate_dates":["1997-01-03","1999-08-10","2002-03-18","2002-05-20","2004-06-15","2005-06-17","2005-09-15","2005-10-10","2008-08-08","2011-07-29"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"001260","company_name":"남광토건","profile_path":"atlas/symbol_profiles/001/001260.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7561,"corporate_action_candidate_count":10,"corporate_action_candidate_dates":["1999-05-13","1999-05-20","2004-05-06","2005-06-03","2007-12-26","2009-07-02","2012-04-17","2013-02-15","2015-04-20","2016-02-05"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"013360","company_name":"일성건설","profile_path":"atlas/symbol_profiles/013/013360.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7709,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1996-01-03","1998-12-21","2000-04-21","2000-08-18","2003-01-07","2017-05-18"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"010780","trigger_type":"Stage2-Actionable-MidcapRealEstateBalanceSheetRepairBridge-Positive","entry_date":"2024-01-25","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and previous R10 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"001260","trigger_type":"Stage2-FalsePositive-SmallcapConstructionPolicyTheme-NoPFBacklogCashBridge","entry_date":"2024-01-02","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and previous R10 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"013360","trigger_type":"Stage2-FalsePositive-ConstructionPolicyThemeNoLiquidityBridge-LateReboundNotValidation","entry_date":"2024-01-02","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and previous R10 loop sets"}
```

## 4. Research question

C30 is not “construction stock bounced.”  
The useful construction signal must prove a balance-sheet bridge: PF exposure containment, liquidity repair, financing trust, backlog quality, margin protection, and cash conversion. Without that bridge, a policy headline is only scaffolding in the wind. It can move, but it does not carry the building.

Residual question:

```text
Can C30 distinguish:
1. midcap real-estate / balance-sheet repair with usable 20%+ MFE,
2. small-cap construction-policy theme where PF/backlog/cash bridge is absent,
3. construction-policy theme where a much later rebound should not validate the weak original entry?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C30_R10L87_010780_ISDONGSEO_BALANCE_SHEET_REPAIR","symbol":"010780","company_name":"아이에스동서","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MIDCAP_REAL_ESTATE_BALANCE_SHEET_REPAIR_BRIDGE","case_type":"watch_positive_control","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-MidcapRealEstateBalanceSheetRepairBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_MFE90_ge20_low_MAE_later_drawdown","current_profile_verdict":"current_profile_correct_if_PF_liquidity_backlog_bridge_required","price_source":"Songdaiki/stock-web","notes":"Midcap real-estate/PF repair proxy generated MFE90 above 20% with low early MAE. Later drawdown keeps Green strict."}
{"row_type":"case","case_id":"C30_R10L87_001260_NAMKWANG_POLICY_THEME_NO_BRIDGE","symbol":"001260","company_name":"남광토건","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALLCAP_CONSTRUCTION_POLICY_THEME_WITHOUT_PF_BACKLOG_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SmallcapConstructionPolicyTheme-NoPFBacklogCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Small-cap construction-policy theme had near-zero MFE and high MAE without PF repair, backlog quality or cash conversion bridge."}
{"row_type":"case","case_id":"C30_R10L87_013360_ILSUNG_POLICY_THEME_LATE_REBOUND_NOT_VALIDATION","symbol":"013360","company_name":"일성건설","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_POLICY_THEME_WITHOUT_LIQUIDITY_BRIDGE_LATE_REBOUND_NOT_VALIDATION","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ConstructionPolicyThemeNoLiquidityBridge-LateReboundNotValidation","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE_original_entry_late_rebound_not_validation","current_profile_verdict":"current_profile_false_positive_if_late_rebound_retroactively_validates_weak_entry","price_source":"Songdaiki/stock-web","notes":"Original January construction-policy entry had low MFE and high MAE before a much later speculative rebound. Late rebound should not validate the original weak-bridge entry."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 010780 아이에스동서 — midcap real-estate/PF balance-sheet repair positive control

Entry row: `2024-01-25 c=24850`.  
Observed path: entry-day low `23650`, 30D high `2024-03-08 h=30300`, 90D high `2024-03-22 h=31200`, and later drawdown into autumn.

```jsonl
{"row_type":"trigger","trigger_id":"R10L87_C30_010780_20240125_STAGE2_MIDCAP_REPAIR","case_id":"C30_R10L87_010780_ISDONGSEO_BALANCE_SHEET_REPAIR","symbol":"010780","company_name":"아이에스동서","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MIDCAP_REAL_ESTATE_BALANCE_SHEET_REPAIR_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-MidcapRealEstateBalanceSheetRepairBridge-Positive","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":24850.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_midcap_realestate_PF_balance_sheet_repair_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; PF exposure containment, NAV repair, liquidity and financing trust treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["PF_exposure_repair_proxy","liquidity_bridge_proxy","financing_trust_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_PF_exposure_source_pending","backlog_quality_pending","cash_conversion_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv","profile_path":"atlas/symbol_profiles/010/010780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.93,"MFE_90D_pct":25.55,"MFE_180D_pct":25.55,"MAE_30D_pct":-4.83,"MAE_90D_pct":-4.83,"MAE_180D_pct":-16.70,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-22","peak_price":31200.0,"max_drawdown_low_date":"2024-10-23","max_drawdown_low":20700.0,"drawdown_after_peak_pct":-33.65,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B_without_exact_PF_liquidity_cash_evidence; later drawdown blocks Green","four_b_evidence_type":["price_only","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_MFE90_ge20_low_MAE_later_drawdown","current_profile_verdict":"current_profile_correct_if_PF_liquidity_backlog_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"010780_2024-01-25_24850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 can allow Stage2/Yellow when PF repair is tied to liquidity, financing trust, backlog quality and cash bridge. Green still requires exact source-grade evidence."}
```

### 6.2 001260 남광토건 — small-cap construction-policy theme without PF/backlog/cash bridge

Entry row: `2024-01-02 c=7890`.  
Observed path: same-day high `8010`, then lows `2024-01-29 l=6740`, `2024-04-18 l=5660`, and weak follow-through afterward.

```jsonl
{"row_type":"trigger","trigger_id":"R10L87_C30_001260_20240102_STAGE2_FALSE_POSITIVE_POLICY_THEME","case_id":"C30_R10L87_001260_NAMKWANG_POLICY_THEME_NO_BRIDGE","symbol":"001260","company_name":"남광토건","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALLCAP_CONSTRUCTION_POLICY_THEME_WITHOUT_PF_BACKLOG_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-SmallcapConstructionPolicyTheme-NoPFBacklogCashBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":7890.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_smallcap_construction_policy_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; small-cap construction policy theme treated as insufficient without PF exposure repair, backlog quality, liquidity and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["construction_policy_theme","smallcap_relative_strength"],"stage3_evidence_fields":["PF_repair_bridge_missing","backlog_quality_missing","liquidity_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","PF_backlog_cash_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001260/2024.csv","profile_path":"atlas/symbol_profiles/001/001260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.52,"MFE_90D_pct":1.52,"MFE_180D_pct":1.52,"MAE_30D_pct":-14.58,"MAE_90D_pct":-28.26,"MAE_180D_pct":-28.26,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-02","peak_price":8010.0,"max_drawdown_low_date":"2024-04-18","max_drawdown_low":5660.0,"drawdown_after_peak_pct":-29.34,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"smallcap_construction_policy_theme_without_PF_backlog_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","PF_backlog_cash_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"001260_2024-01-02_7890","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 should not promote construction-policy theme without PF/backlog/cash bridge. Near-zero MFE and high MAE require Watch/4B-risk routing."}
```

### 6.3 013360 일성건설 — construction-policy theme with late rebound not validating weak original entry

Entry row: `2024-01-02 c=1548`.  
Observed path: same-day high `1653`, then lows `2024-01-25 l=1264`, `2024-03-07 l=1110`, and a much later November/December speculative rebound that should not validate the January weak-bridge entry.

```jsonl
{"row_type":"trigger","trigger_id":"R10L87_C30_013360_20240102_STAGE2_FALSE_POSITIVE_POLICY_LATE_REBOUND","case_id":"C30_R10L87_013360_ILSUNG_POLICY_THEME_LATE_REBOUND_NOT_VALIDATION","symbol":"013360","company_name":"일성건설","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_POLICY_THEME_WITHOUT_LIQUIDITY_BRIDGE_LATE_REBOUND_NOT_VALIDATION","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-ConstructionPolicyThemeNoLiquidityBridge-LateReboundNotValidation","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":1548.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_construction_policy_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; construction policy theme treated as insufficient without PF repair, financing trust, liquidity and backlog/cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["construction_policy_theme","relative_strength_spike"],"stage3_evidence_fields":["liquidity_bridge_missing","PF_repair_bridge_missing","financing_trust_missing","backlog_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","late_rebound_not_entry_validation"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/013/013360/2024.csv","profile_path":"atlas/symbol_profiles/013/013360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.78,"MFE_90D_pct":6.78,"MFE_180D_pct":6.78,"MAE_30D_pct":-18.35,"MAE_90D_pct":-28.29,"MAE_180D_pct":-28.29,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-02","peak_price":1653.0,"max_drawdown_low_date":"2024-03-07","max_drawdown_low":1110.0,"drawdown_after_peak_pct":-32.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"original_entry_should_be_4B_watch; late speculative rebound should not retroactively validate weak bridge entry","four_b_evidence_type":["price_only","late_rebound_not_entry_validation"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE_original_entry_late_rebound_not_validation","current_profile_verdict":"current_profile_false_positive_if_late_rebound_retroactively_validates_weak_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"013360_2024-01-02_1548","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 should not retroactively validate a weak January construction-policy entry because of a much later unrelated rebound. Missing liquidity/PF/backlog/cash bridge plus low MFE and high MAE require Watch/4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C30_R10L87_010780_ISDONGSEO_BALANCE_SHEET_REPAIR","trigger_id":"R10L87_C30_010780_20240125_STAGE2_MIDCAP_REPAIR","symbol":"010780","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C30 requires PF/liquidity/backlog/cash bridge rather than construction rebound alone","raw_component_scores_before":{"PF_exposure_repair":12,"liquidity_bridge":11,"financing_trust":10,"backlog_quality":9,"margin_bridge":7,"cash_conversion":6,"relative_strength_score":11,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":67,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"PF_exposure_repair":15,"liquidity_bridge":14,"financing_trust":13,"backlog_quality":11,"margin_bridge":9,"cash_conversion":8,"relative_strength_score":12,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":79,"stage_label_after":"Stage2-Actionable/Stage3-Yellow-Watch","component_delta_explanation":"PF/liquidity repair proxy and MFE90>=20 support Yellow-watch; later drawdown and proxy-only evidence block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C30_R10L87_001260_NAMKWANG_POLICY_THEME_NO_BRIDGE","trigger_id":"R10L87_C30_001260_20240102_STAGE2_FALSE_POSITIVE_POLICY_THEME","symbol":"001260","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"small-cap construction-policy theme without PF/backlog/cash bridge should be blocked","raw_component_scores_before":{"PF_exposure_repair":2,"liquidity_bridge":1,"financing_trust":1,"backlog_quality":1,"margin_bridge":0,"cash_conversion":0,"relative_strength_score":6,"valuation_repricing_score":3,"execution_risk_score":-14,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":0,"margin_bridge":0,"cash_conversion":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and high MAE convert policy theme into missing bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C30_R10L87_013360_ILSUNG_POLICY_THEME_LATE_REBOUND_NOT_VALIDATION","trigger_id":"R10L87_C30_013360_20240102_STAGE2_FALSE_POSITIVE_POLICY_LATE_REBOUND","symbol":"013360","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"late rebound should not validate the original weak construction-policy entry","raw_component_scores_before":{"PF_exposure_repair":2,"liquidity_bridge":1,"financing_trust":1,"backlog_quality":1,"margin_bridge":0,"cash_conversion":0,"relative_strength_score":8,"valuation_repricing_score":3,"execution_risk_score":-14,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":0,"margin_bridge":0,"cash_conversion":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and high MAE before the late rebound keep the original entry Watch/4B; no retroactive validation."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R10L87_C30_P0_CURRENT","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C30 needs explicit PF/liquidity/financing/backlog/cash bridge gates and late-rebound non-validation rule","eligible_trigger_count":3,"avg_MFE90_pct":11.28,"avg_MAE90_pct":-20.46,"avg_MFE180_pct":11.28,"avg_MAE180_pct":-24.42,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C30_PF_liquidity_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R10L87_C30_P1_SECTOR_SPECIFIC","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P1_L9_PF_liquidity_cash_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L9 construction signals need PF exposure containment, liquidity repair, financing trust, backlog quality, margin or cash bridge before Stage2-Actionable","changed_axes":["PF_exposure_repair_required","liquidity_financing_required","construction_policy_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_PF_repair_liquidity_financing_backlog_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":11.28,"avg_MAE90_pct":-20.46,"avg_MFE180_pct":11.28,"avg_MAE180_pct":-24.42,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R10L87_C30_P2_CANONICAL","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P2_C30_PF_liquidity_cash_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C30 should reward balance-sheet repair mechanics, not policy-theme or late speculative rebounds","changed_axes":["C30_PF_liquidity_cash_bridge_required","C30_policy_theme_local_4B_guard","C30_late_rebound_not_entry_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"PF_repair_liquidity_financing_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":11.28,"avg_MAE90_pct":-20.46,"avg_MFE180_pct":11.28,"avg_MAE180_pct":-24.42,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R10L87_C30_P3_COUNTEREXAMPLE_GUARD","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P3_C30_low_MFE_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-25 while PF/liquidity/cash bridge is missing, block Yellow/Green; preserve late-rebound non-validation","changed_axes":["C30_low_MFE_guardrail","C30_high_MAE_4B_guardrail","C30_late_rebound_not_validation"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_25"},"eligible_trigger_count":3,"avg_MFE90_pct":11.28,"avg_MAE90_pct":-20.46,"avg_MFE180_pct":11.28,"avg_MAE180_pct":-24.42,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_MIDCAP_REPAIR_VS_POLICY_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":11.28,"avg_MAE90_pct":-20.46,"avg_MFE180_pct":11.28,"avg_MAE180_pct":-24.42,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE90_le_minus_25":0.67,"interpretation":"C30 needs bridge discipline. 아이에스동서 shows PF/liquidity repair can support Yellow-watch, while 남광토건 and 일성건설 show construction-policy themes should stay Watch/4B unless PF, liquidity, backlog and cash evidence are repaired."}
{"row_type":"stage_transition_summary","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"010780","trigger_type":"Stage2-Actionable-MidcapRealEstateBalanceSheetRepairBridge-Positive","entry_date":"2024-01-25","stage2_to_90D_outcome":"good_stage2_MFE90_ge20_low_MAE","stage2_to_180D_outcome":"watch_positive_with_later_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when PF repair, liquidity, financing trust and backlog/cash bridge exists; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"001260","trigger_type":"Stage2-FalsePositive-SmallcapConstructionPolicyTheme-NoPFBacklogCashBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_high_MAE","stage2_to_180D_outcome":"failed_smallcap_policy_theme","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Small-cap construction-policy theme without PF/backlog/cash bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"013360","trigger_type":"Stage2-FalsePositive-ConstructionPolicyThemeNoLiquidityBridge-LateReboundNotValidation","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_original_entry_late_rebound_not_validation","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Late speculative rebound should not validate the original weak-bridge construction-policy entry."}
{"row_type":"residual_contribution","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"construction_policy_theme_overcredit_without_PF_liquidity_backlog_cash_bridge_and_late_rebound_not_validation","contribution":"Adds two C30 local 4B/high-MAE construction-policy counterexamples against one midcap PF/liquidity repair positive, avoiding C30 top-covered and previous R10 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MIDCAP_REAL_ESTATE_BALANCE_SHEET_REPAIR_BRIDGE_VS_SMALLCAP_CONSTRUCTION_POLICY_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C30 now has non-top-symbol midcap repair control and two small-cap policy-theme counterexamples; next R10 loops should exact-URL repair PF exposure, liquidity, financing trust, backlog quality, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_PF_liquidity_backlog_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"010780 worked when PF/liquidity repair proxy was present; 001260 and 013360 failed when only construction-policy theme existed."}
{"row_type":"shadow_weight","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_construction_policy_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Small-cap policy theme rows showed near-zero/low MFE and high MAE without PF/liquidity/backlog/cash bridge."}
{"row_type":"shadow_weight","round":"R10","loop":"87","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_late_rebound_not_entry_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"013360 shows a much later speculative rebound should not retroactively validate the original weak-bridge entry."}
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
  - construction_policy_theme_overcredit
  - PF_liquidity_bridge_missing
  - backlog_cash_conversion_bridge_missing
  - late_rebound_not_entry_validation
new_axis_proposed:
  - C30_PF_liquidity_backlog_cash_bridge_required_shadow_only
  - C30_construction_policy_theme_local_4B_watch_guard_shadow_only
  - C30_late_rebound_not_entry_validation_guard_shadow_only
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
3. Confirm R10 / L9 / C30 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C30 top-covered symbols
   - previous R10 loop86 symbols
   - previous R10 loop85 symbols
   - previous R10 loop84 symbols
   - previous R10 loop83 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C30-scoped safe patch candidates:
   - C30_PF_liquidity_backlog_cash_bridge_required
   - C30_construction_policy_theme_local_4B_watch_guard
   - C30_late_rebound_not_entry_validation_guard
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R10
completed_loop = 87
next_round = R11
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.
```
