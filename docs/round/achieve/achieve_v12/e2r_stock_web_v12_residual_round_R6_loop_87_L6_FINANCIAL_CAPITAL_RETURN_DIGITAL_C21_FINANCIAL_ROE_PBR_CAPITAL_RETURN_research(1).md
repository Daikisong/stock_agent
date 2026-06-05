# E2R Stock-Web v12 Residual Research — R6 Loop 87 / L6 / C21

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R6
loop: 87
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BROKERAGE_CAPITAL_RETURN_ROE_BRIDGE_VS_LATE_FINANCIAL_VALUEUP_EXTENSION
sector: financials / capital return / ROE / PBR / brokerage / bank value-up
output_file: e2r_stock_web_v12_residual_round_R6_loop_87_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R5 loop 87`.

```text
scheduled_round = R6
scheduled_loop = 87
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

R6 is restricted to financial / capital-return / digital-finance.  
The previous R6 loop used C22 insurance reserve-cycle evidence, so this loop returns to C21 with a new symbol set and a different residual question.

The No-Repeat Index shows C21 as:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
rows = 51
symbols = 19
good/bad Stage2 = 22/11
4B/4C = 7/0
top-covered = 006220, 016360, 071050, 105560, 138040, 139130
```

This loop avoids the top-covered set and also avoids the previous R6 loop85 C21 symbols:

```text
086790, 323410, 377300
```

Selected symbols:

```text
006800, 039490, 316140
```

`039490` is used as a late-extension counterexample, not as the early 2024 positive path. The hard no-repeat key remains new because trigger type and entry date differ.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"006800","company_name":"미래에셋증권","profile_path":"atlas/symbol_profiles/006/006800.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7765,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1999-09-27","1999-10-14","2000-05-22","2001-11-23","2011-11-16","2017-01-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here. Name changed from 미래에셋대우 to 미래에셋증권 in 2021, outside selected window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"039490","company_name":"키움증권","profile_path":"atlas/symbol_profiles/039/039490.json","first_date":"2004-04-23","last_date":"2026-02-20","trading_day_count":5390,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2008-12-24"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_late_entry"}
{"row_type":"price_source_validation","symbol":"316140","company_name":"우리금융지주","profile_path":"atlas/symbol_profiles/316/316140.json","first_date":"2019-02-13","last_date":"2026-02-20","trading_day_count":1725,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"006800","trigger_type":"Stage2-Actionable-BrokerageROEPBRCapitalReturnBridge-Positive","entry_date":"2024-01-25","duplicate_status":"new C21 symbol/trigger/date combination outside top-covered and previous R6 loop85 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"039490","trigger_type":"Stage2-FalsePositive-LateBrokerageValueupExtension-NoFreshROECapitalReturnBridge","entry_date":"2024-07-11","duplicate_status":"new C21 symbol/trigger/date combination outside top-covered and previous R6 loop85 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"316140","trigger_type":"Stage2-FalsePositive-LateBankValueupExtension-NoIncrementalCapitalReturnBridge","entry_date":"2024-07-26","duplicate_status":"new C21 symbol/trigger/date combination outside top-covered and previous R6 loop85 symbols"}
```

## 4. Research question

C21 is not “financial value-up stock went up.”  
The useful signal is the capital-return and ROE bridge: sustainable ROE, CET1 or capital buffer, buyback/cancellation, dividend visibility, PBR repair, cost discipline, and earnings durability. Without that bridge, a value-up rally can become a clean-looking banknote with no watermark.

Residual question:

```text
Can C21 distinguish:
1. brokerage/financial ROE-PBR-capital-return bridge with good MFE and shallow MAE,
2. late brokerage value-up extension where incremental ROE and shareholder-return evidence is missing,
3. late bank value-up extension where the price path is capped without fresh capital-return or earnings revision bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C21_R6L87_006800_MIRAE_BROKERAGE_ROE_CAPITAL_RETURN","symbol":"006800","company_name":"미래에셋증권","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BROKERAGE_ROE_PBR_CAPITAL_RETURN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-BrokerageROEPBRCapitalReturnBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_MFE90_ge20_shallow_MAE","current_profile_verdict":"current_profile_correct_if_ROE_capital_return_bridge_required","price_source":"Songdaiki/stock-web","notes":"Brokerage/ROE/PBR/capital-return proxy produced strong MFE and shallow initial MAE. Green still requires exact buyback/cancellation, ROE and capital buffer evidence."}
{"row_type":"case","case_id":"C21_R6L87_039490_KIWOOM_LATE_VALUEUP_EXTENSION","symbol":"039490","company_name":"키움증권","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LATE_BROKERAGE_VALUEUP_EXTENSION_WITHOUT_FRESH_ROE_CAPITAL_RETURN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LateBrokerageValueupExtension-NoFreshROECapitalReturnBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE_after_late_extension","current_profile_verdict":"current_profile_false_positive_if_late_brokerage_extension_overcredited","price_source":"Songdaiki/stock-web","notes":"Late brokerage value-up extension after a strong early move had low MFE and high MAE when incremental ROE and capital-return evidence was missing."}
{"row_type":"case","case_id":"C21_R6L87_316140_WOORI_LATE_BANK_VALUEUP_EXTENSION","symbol":"316140","company_name":"우리금융지주","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LATE_BANK_VALUEUP_EXTENSION_WITHOUT_INCREMENTAL_CAPITAL_RETURN_BRIDGE","case_type":"weak_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LateBankValueupExtension-NoIncrementalCapitalReturnBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_moderate_MAE_late_extension","current_profile_verdict":"current_profile_false_positive_if_late_bank_valueup_extension_overcredited","price_source":"Songdaiki/stock-web","notes":"Late bank value-up extension had capped MFE and moderate MAE. It should remain Watch unless incremental shareholder return, CET1/capital buffer and earnings bridge are exact-evidence repaired."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 006800 미래에셋증권 — brokerage ROE/PBR/capital-return bridge positive

Entry row: `2024-01-25 c=7140`.  
Observed path: entry low `2024-01-25 l=6770`, 30D high `2024-02-23 h=9200`, and later 180D highs around the autumn value-up window.

```jsonl
{"row_type":"trigger","trigger_id":"R6L87_C21_006800_20240125_STAGE2_BROKERAGE_ROE_CAPITAL_RETURN","case_id":"C21_R6L87_006800_MIRAE_BROKERAGE_ROE_CAPITAL_RETURN","symbol":"006800","company_name":"미래에셋증권","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BROKERAGE_ROE_PBR_CAPITAL_RETURN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-BrokerageROEPBRCapitalReturnBridge-Positive","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":7140.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_brokerage_ROE_PBR_capital_return_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; brokerage ROE/PBR repair and capital-return bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["ROE_recovery_proxy","PBR_repair_proxy","capital_return_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_buyback_cancellation_pending","capital_buffer_pending","earnings_durability_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006800/2024.csv","profile_path":"atlas/symbol_profiles/006/006800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.85,"MFE_90D_pct":28.85,"MFE_180D_pct":30.25,"MAE_30D_pct":-5.18,"MAE_90D_pct":-5.18,"MAE_180D_pct":-5.18,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":9300.0,"max_drawdown_low_date":"2024-01-25","max_drawdown_low":6770.0,"drawdown_after_peak_pct":-14.73,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","capital_return_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_MFE90_ge20_shallow_MAE","current_profile_verdict":"current_profile_correct_if_ROE_capital_return_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"006800_2024-01-25_7140","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C21 can allow Stage2/Yellow when financial value-up is tied to ROE recovery, PBR repair and capital-return bridge. Green still requires exact buyback/cancellation, capital buffer and earnings durability evidence."}
```

### 6.2 039490 키움증권 — late brokerage value-up extension without fresh ROE/capital-return bridge

Entry row: `2024-07-11 c=144600`.  
Observed path: next local high `2024-07-16 h=146400`, then low `2024-08-05 l=115200`, and later `2024-12-09 l=110500`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L87_C21_039490_20240711_STAGE2_FALSE_POSITIVE_LATE_BROKERAGE_EXTENSION","case_id":"C21_R6L87_039490_KIWOOM_LATE_VALUEUP_EXTENSION","symbol":"039490","company_name":"키움증권","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LATE_BROKERAGE_VALUEUP_EXTENSION_WITHOUT_FRESH_ROE_CAPITAL_RETURN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-LateBrokerageValueupExtension-NoFreshROECapitalReturnBridge","trigger_date":"2024-07-11","entry_date":"2024-07-11","entry_price":144600.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_late_brokerage_valueup_extension_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; late brokerage value-up extension treated as insufficient without incremental ROE, buyback/cancellation, dividend or capital buffer bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["late_valueup_extension","brokerage_relative_strength"],"stage3_evidence_fields":["incremental_ROE_bridge_missing","fresh_capital_return_bridge_missing","earnings_durability_missing","capital_buffer_missing"],"stage4b_evidence_fields":["price_only_local_peak","incremental_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039490/2024.csv","profile_path":"atlas/symbol_profiles/039/039490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.24,"MFE_90D_pct":1.24,"MFE_180D_pct":1.24,"MAE_30D_pct":-20.33,"MAE_90D_pct":-20.33,"MAE_180D_pct":-23.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-16","peak_price":146400.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":110500.0,"drawdown_after_peak_pct":-24.52,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_brokerage_valueup_extension_without_incremental_ROE_capital_return_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","incremental_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE_after_late_extension","current_profile_verdict":"current_profile_false_positive_if_late_brokerage_extension_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"039490_2024-07-11_144600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C21 should not upgrade a late brokerage value-up extension without fresh ROE, shareholder-return and capital-buffer bridge. Low MFE and high MAE force Watch/4B-risk routing."}
```

### 6.3 316140 우리금융지주 — late bank value-up extension without incremental capital-return bridge

Entry row: `2024-07-26 c=16180`.  
Observed path: local high `2024-07-29 h=16960`, low `2024-08-05 l=13740`, and later high `2024-12-03 h=17300`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L87_C21_316140_20240726_STAGE2_FALSE_POSITIVE_LATE_BANK_VALUEUP","case_id":"C21_R6L87_316140_WOORI_LATE_BANK_VALUEUP_EXTENSION","symbol":"316140","company_name":"우리금융지주","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LATE_BANK_VALUEUP_EXTENSION_WITHOUT_INCREMENTAL_CAPITAL_RETURN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-LateBankValueupExtension-NoIncrementalCapitalReturnBridge","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":16180.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_late_bank_valueup_extension_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; late bank value-up extension treated as insufficient without incremental CET1/capital buffer, shareholder return or earnings revision bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["late_bank_valueup_extension","relative_strength_extension"],"stage3_evidence_fields":["incremental_capital_return_bridge_missing","CET1_buffer_bridge_missing","earnings_revision_missing","PBR_repair_increment_missing"],"stage4b_evidence_fields":["price_only_local_extension","incremental_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv","profile_path":"atlas/symbol_profiles/316/316140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.82,"MFE_90D_pct":5.69,"MFE_180D_pct":6.92,"MAE_30D_pct":-15.08,"MAE_90D_pct":-15.08,"MAE_180D_pct":-15.08,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":17300.0,"max_drawdown_low_date":"2024-08-05","max_drawdown_low":13740.0,"drawdown_after_peak_pct":-11.79,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_bank_valueup_extension_without_incremental_capital_return_bridge_should_remain_watch_not_Yellow","four_b_evidence_type":["price_only","incremental_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_moderate_MAE_late_extension","current_profile_verdict":"current_profile_false_positive_if_late_bank_valueup_extension_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"316140_2024-07-26_16180","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C21 should not equate late bank value-up extension with incremental capital-return bridge. Low MFE and capped forward path argue for Watch until exact capital-return, CET1 and earnings evidence is repaired."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C21_R6L87_006800_MIRAE_BROKERAGE_ROE_CAPITAL_RETURN","trigger_id":"R6L87_C21_006800_20240125_STAGE2_BROKERAGE_ROE_CAPITAL_RETURN","symbol":"006800","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C21 requires ROE, capital-return and PBR repair bridge rather than financial value-up label alone","raw_component_scores_before":{"ROE_recovery_score":13,"PBR_repair_score":12,"capital_return_score":12,"buyback_cancellation_score":8,"capital_buffer_score":8,"earnings_durability_score":8,"relative_strength_score":12,"valuation_repricing_score":9,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"ROE_recovery_score":16,"PBR_repair_score":15,"capital_return_score":15,"buyback_cancellation_score":10,"capital_buffer_score":10,"earnings_durability_score":10,"relative_strength_score":13,"valuation_repricing_score":10,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"ROE/PBR/capital-return bridge and shallow MAE support Yellow-watch; exact buyback/cancellation and capital-buffer evidence still blocks Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C21_R6L87_039490_KIWOOM_LATE_VALUEUP_EXTENSION","trigger_id":"R6L87_C21_039490_20240711_STAGE2_FALSE_POSITIVE_LATE_BROKERAGE_EXTENSION","symbol":"039490","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_scope":"current_default_proxy","profile_hypothesis":"late financial extension without fresh ROE/capital-return bridge should be blocked","raw_component_scores_before":{"ROE_recovery_score":4,"PBR_repair_score":6,"capital_return_score":2,"buyback_cancellation_score":0,"capital_buffer_score":2,"earnings_durability_score":2,"relative_strength_score":13,"valuation_repricing_score":6,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":8,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"ROE_recovery_score":0,"PBR_repair_score":2,"capital_return_score":0,"buyback_cancellation_score":0,"capital_buffer_score":0,"earnings_durability_score":0,"relative_strength_score":4,"valuation_repricing_score":1,"execution_risk_score":-20,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and high MAE convert late value-up extension into missing bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C21_R6L87_316140_WOORI_LATE_BANK_VALUEUP_EXTENSION","trigger_id":"R6L87_C21_316140_20240726_STAGE2_FALSE_POSITIVE_LATE_BANK_VALUEUP","symbol":"316140","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_scope":"current_default_proxy","profile_hypothesis":"late bank value-up extension without incremental capital-return bridge should remain Watch/blocked","raw_component_scores_before":{"ROE_recovery_score":5,"PBR_repair_score":6,"capital_return_score":3,"buyback_cancellation_score":0,"capital_buffer_score":3,"earnings_durability_score":3,"relative_strength_score":11,"valuation_repricing_score":5,"execution_risk_score":-10,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":14,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"ROE_recovery_score":2,"PBR_repair_score":2,"capital_return_score":0,"buyback_cancellation_score":0,"capital_buffer_score":1,"earnings_durability_score":1,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Watch-Blocked","component_delta_explanation":"Low MFE and missing incremental capital-return evidence should block Yellow/Green even before extreme MAE appears."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R6L87_C21_P0_CURRENT","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C21 needs explicit incremental ROE, capital-return, buyback/cancellation and capital-buffer bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":11.93,"avg_MAE90_pct":-13.53,"avg_MFE180_pct":12.8,"avg_MAE180_pct":-14.61,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C21_incremental_capital_return_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R6L87_C21_P1_SECTOR_SPECIFIC","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P1_L6_ROE_capital_return_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L6 financial value-up signals need ROE recovery, capital return, buyback/cancellation, capital buffer or earnings durability bridge before Stage2-Actionable","changed_axes":["ROE_bridge_required","capital_return_required","late_valueup_extension_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_ROE_capital_return_buyback_capital_buffer_or_earnings_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":11.93,"avg_MAE90_pct":-13.53,"avg_MFE180_pct":12.8,"avg_MAE180_pct":-14.61,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R6L87_C21_P2_CANONICAL","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P2_C21_incremental_capital_return_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C21 should reward capital-return/ROE mechanics, not late financial value-up price extensions","changed_axes":["C21_incremental_capital_return_bridge_required","C21_late_extension_local_4B_watch_guard","C21_low_MFE_no_incremental_bridge_guard"],"changed_thresholds":{"stage2_yellow_gate":"ROE_or_capital_return_bridge_required; late extension requires incremental evidence"},"eligible_trigger_count":3,"avg_MFE90_pct":11.93,"avg_MAE90_pct":-13.53,"avg_MFE180_pct":12.8,"avg_MAE180_pct":-14.61,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R6L87_C21_P3_COUNTEREXAMPLE_GUARD","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P3_C21_low_MFE_late_extension_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<7 and incremental capital-return bridge is missing after a late extension, block Yellow/Green; if MAE90<=-20, force 4B-watch","changed_axes":["C21_low_MFE_guardrail","C21_late_extension_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_7_and_incremental_bridge_missing; hard_4B_if_MAE90_le_minus_20"},"eligible_trigger_count":3,"avg_MFE90_pct":11.93,"avg_MAE90_pct":-13.53,"avg_MFE180_pct":12.8,"avg_MAE180_pct":-14.61,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_BROKERAGE_CAPITAL_RETURN_VS_LATE_VALUEUP_EXTENSION","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":1,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":11.93,"avg_MAE90_pct":-13.53,"avg_MFE180_pct":12.8,"avg_MAE180_pct":-14.61,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_7":0.67,"stage2_bad_entry_rate_MAE90_le_minus_20":0.33,"interpretation":"C21 needs bridge discipline. 미래에셋증권 shows ROE/PBR/capital-return bridge can create a strong entry, while 키움증권 and 우리금융지주 show that late financial value-up extensions should not be promoted without incremental capital-return, capital buffer and earnings evidence."}
{"row_type":"stage_transition_summary","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"006800","trigger_type":"Stage2-Actionable-BrokerageROEPBRCapitalReturnBridge-Positive","entry_date":"2024-01-25","stage2_to_90D_outcome":"good_stage2_MFE90_ge20_shallow_MAE","stage2_to_180D_outcome":"positive_brokerage_ROE_capital_return_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when ROE/PBR/capital-return bridge exists; Green requires exact buyback/cancellation and capital-buffer evidence."}
{"row_type":"stage_transition_summary","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"039490","trigger_type":"Stage2-FalsePositive-LateBrokerageValueupExtension-NoFreshROECapitalReturnBridge","entry_date":"2024-07-11","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_late_brokerage_extension","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Late brokerage value-up extension without incremental ROE/capital-return bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"316140","trigger_type":"Stage2-FalsePositive-LateBankValueupExtension-NoIncrementalCapitalReturnBridge","entry_date":"2024-07-26","stage2_to_90D_outcome":"weak_stage2_low_MFE_moderate_MAE","stage2_to_180D_outcome":"capped_late_bank_valueup_extension","MFE90_ge_20":false,"MAE90_le_minus_20":false,"transition_note":"Late bank value-up extension without incremental capital-return and CET1 bridge should remain Watch/blocked from Yellow/Green."}
{"row_type":"residual_contribution","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","residual_type":"financial_valueup_late_extension_overcredit_without_incremental_ROE_capital_return_bridge","contribution":"Adds one C21 4B/high-MAE late-extension counterexample and one low-MFE Watch counterexample against one brokerage ROE/capital-return positive, avoiding C21 top-covered and previous R6 loop85 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BROKERAGE_CAPITAL_RETURN_ROE_BRIDGE_VS_LATE_FINANCIAL_VALUEUP_EXTENSION","positive_case_count":1,"counterexample_count":2,"4B_case_count":1,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C21 now has non-top-symbol brokerage/bank late-extension counterexamples; next R6 loops should exact-URL repair ROE, PBR, CET1/capital buffer, buyback/cancellation, dividend and earnings durability evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","axis":"C21_incremental_ROE_capital_return_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"006800 worked when ROE/PBR/capital-return proxy was present; 039490 and 316140 were weak when late extension lacked fresh ROE/capital-return evidence."}
{"row_type":"shadow_weight","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","axis":"C21_late_financial_valueup_extension_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Late financial value-up extension rows showed low MFE without incremental capital-return, CET1/capital buffer or earnings revision bridge."}
{"row_type":"shadow_weight","round":"R6","loop":"87","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","axis":"C21_low_MFE_late_extension_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<7 and incremental capital-return bridge is missing after a late extension, block Stage2-Actionable/Yellow; if MAE90<=-20, route to 4B-watch."}
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
  - financial_valueup_late_extension_overcredit
  - incremental_ROE_bridge_missing
  - capital_return_bridge_missing
  - CET1_or_capital_buffer_bridge_missing
new_axis_proposed:
  - C21_incremental_ROE_capital_return_bridge_required_shadow_only
  - C21_late_financial_valueup_extension_watch_guard_shadow_only
  - C21_low_MFE_late_extension_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C21
  - full_4b_requires_non_price_evidence within C21
  - hard_4c_thesis_break_routes_to_4c within C21
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
3. Confirm R6 / L6 / C21 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C21 top-covered symbols
   - previous R6 loop85 C21 symbols
   - previous R6 loop86 C22 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C21-scoped safe patch candidates:
   - C21_incremental_ROE_capital_return_bridge_required
   - C21_late_financial_valueup_extension_watch_guard
   - C21_low_MFE_late_extension_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R6
completed_loop = 87
next_round = R7
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 1 local 4B-watch row for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.
```
