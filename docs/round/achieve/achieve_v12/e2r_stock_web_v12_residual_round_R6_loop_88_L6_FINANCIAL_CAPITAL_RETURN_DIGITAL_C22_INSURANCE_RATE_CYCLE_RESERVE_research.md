# E2R Stock-Web v12 Residual Research — R6 Loop 88 / L6 / C22

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R6
loop: 88
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: INSURANCE_HOLDCO_CAPITAL_RETURN_RESERVE_BRIDGE_VS_GA_DISTRIBUTION_THEME_EXTENSION_NO_RESERVE_BRIDGE
sector: financials / insurance / reserve cycle / capital return / GA distribution
output_file: e2r_stock_web_v12_residual_round_R6_loop_88_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R5 loop 88`.

```text
scheduled_round = R6
scheduled_loop = 88
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
```

R6 is restricted to financial / capital-return / insurance.  
C22 is selected because the immediately previous R6 loop used C21 financial ROE/PBR/capital-return, and the latest R13 cross-review reinforced a key rule: **theme or price-extension MFE is not enough if the reserve/capital bridge is missing**.

No-Repeat Index snapshot:

```text
C22_INSURANCE_RATE_CYCLE_RESERVE
rows = 37
symbols = 12
good/bad Stage2 = 10/11
4B/4C = 2/0
top-covered = 000370, 003690, 082640, 000540, 000810, 005830
```

This loop avoids the C22 top-covered symbols and also avoids previous C22 loop symbols:

```text
R6 loop84 C22: 032830, 001450, 088350
R6 loop86 C22: 001450, 000400, 085620
```

It also avoids the immediately previous R6 loop87 C21 set:

```text
006800, 039490, 316140
```

Selected symbols:

```text
138040, 211050, 244920
```

`138040` is a financial/insurance holdco positive-control row. It is already top-covered in C21, but not in C22; this row is used specifically for insurance capital-return / reserve-cycle bridge behavior, not for generic C21 ROE/PBR scoring.  
`211050` and `244920` are insurance distribution / GA channel rows used as **weak-bridge counterexamples**: distribution beta is not the same as reserve quality, capital buffer, loss-ratio discipline, buyback/dividend bridge, or insurance float compounding.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"138040","company_name":"메리츠금융지주","profile_path":"atlas/symbol_profiles/138/138040.json","first_date":"2011-05-13","last_date":"2026-02-20","trading_day_count":3633,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2011-08-09","2014-10-13","2023-02-21","2023-04-25"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here. 2024 selected path is clean for this entry.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"211050","company_name":"인카금융서비스","profile_path":"atlas/symbol_profiles/211/211050.json","first_date":"2015-11-18","last_date":"2026-02-20","trading_day_count":2224,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2018-07-18","2022-06-22","2022-07-13","2024-04-29"],"has_major_raw_discontinuity":true,"calibration_caveat":"A 2024-04-29 corporate-action candidate exists. The selected counterexample entry is after that candidate and is marked with data-quality watch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_entry_after_2024-04-29_candidate; data_quality_watch"}
{"row_type":"price_source_validation","symbol":"244920","company_name":"에이플러스에셋","profile_path":"atlas/symbol_profiles/244/244920.json","first_date":"2020-11-20","last_date":"2026-02-20","trading_day_count":1286,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"138040","trigger_type":"Stage2-Actionable-InsuranceHoldcoReserveCapitalReturnBridge-Positive","entry_date":"2024-01-31","duplicate_status":"new C22 symbol/trigger/date combination outside C22 top-covered and previous C22 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"211050","trigger_type":"Stage2-FalsePositive-GADistributionSpike-NoReserveCapitalBridge","entry_date":"2024-11-15","duplicate_status":"new C22 symbol/trigger/date combination outside top-covered and previous C22 loop symbols; selected after 2024-04-29 corporate-action candidate"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"244920","trigger_type":"Stage2-FalsePositive-InsuranceDistributionTheme-NoLossRatioReserveBridge","entry_date":"2024-05-20","duplicate_status":"new C22 symbol/trigger/date combination outside top-covered and previous C22 loop symbols"}
```

## 4. Research question

C22 is not “보험·금융주가 올랐다.”  
The useful C22 signal is a reserve and capital bridge: loss-ratio discipline, reserve adequacy, CSM or float quality, rate-cycle sensitivity, capital buffer, dividend or buyback/cancellation visibility, and earnings durability. A distributor or GA channel theme can look like insurance beta, but if it does not own the reserve/capital mechanics, it is more like selling umbrellas during a storm than underwriting the weather.

Residual question:

```text
Can C22 distinguish:
1. insurance holdco / reserve-cycle / capital-return bridge with strong MFE and shallow MAE,
2. GA distribution spike where commission-channel beta lacks reserve quality and capital-return bridge,
3. insurance-distribution theme that has modest MFE but no loss-ratio, reserve, CSM or capital-buffer bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C22_R6L88_138040_MERITZ_HOLDCO_RESERVE_CAPITAL_RETURN","symbol":"138040","company_name":"메리츠금융지주","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_HOLDCO_RESERVE_CAPITAL_RETURN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-InsuranceHoldcoReserveCapitalReturnBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_shallow_MAE","current_profile_verdict":"current_profile_correct_if_reserve_capital_return_bridge_required","price_source":"Songdaiki/stock-web","notes":"Insurance holdco/capital-return bridge produced high MFE with shallow drawdown. Green still requires exact reserve, capital buffer and shareholder-return evidence."}
{"row_type":"case","case_id":"C22_R6L88_211050_INCAR_GA_DISTRIBUTION_SPIKE","symbol":"211050","company_name":"인카금융서비스","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"GA_DISTRIBUTION_SPIKE_WITHOUT_RESERVE_CAPITAL_BRIDGE","case_type":"weak_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-GADistributionSpike-NoReserveCapitalBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_moderate_MAE_data_quality_watch","current_profile_verdict":"current_profile_false_positive_if_GA_distribution_beta_promoted_as_C22","price_source":"Songdaiki/stock-web","notes":"GA distribution spike is not reserve/capital-return evidence. MFE after the selected late entry was small and drawdown risk was visible; selected after the 2024-04-29 corporate-action candidate."}
{"row_type":"case","case_id":"C22_R6L88_244920_APLUS_INSURANCE_DISTRIBUTION_THEME","symbol":"244920","company_name":"에이플러스에셋","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_DISTRIBUTION_THEME_WITHOUT_LOSS_RATIO_RESERVE_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-InsuranceDistributionTheme-NoLossRatioReserveBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub_Yellow_MFE_no_reserve_bridge","current_profile_verdict":"current_profile_false_positive_if_distribution_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Insurance distribution theme had insufficient C22 bridge: no loss-ratio, reserve, capital buffer or shareholder-return mechanics. Later movement should not be read as reserve-cycle validation."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 138040 메리츠금융지주 — insurance holdco / reserve-cycle / capital-return bridge positive

Entry row: `2024-01-31 c=68500`.  
Observed path: early low `2024-02-06 l=67100`, high `2024-03-15 h=88300`, and later full-window high `2024-10-21 h=107200`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L88_C22_138040_20240131_STAGE2_INSURANCE_HOLDCO_CAPITAL_RETURN","case_id":"C22_R6L88_138040_MERITZ_HOLDCO_RESERVE_CAPITAL_RETURN","symbol":"138040","company_name":"메리츠금융지주","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_HOLDCO_RESERVE_CAPITAL_RETURN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-InsuranceHoldcoReserveCapitalReturnBridge-Positive","trigger_date":"2024-01-31","entry_date":"2024-01-31","entry_price":68500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_insurance_holdco_reserve_cycle_capital_return_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; reserve-cycle, capital-return and shareholder-yield bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["reserve_cycle_proxy","capital_return_proxy","shareholder_yield_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_reserve_quality_pending","capital_buffer_pending","buyback_cancellation_pending","earnings_durability_pending"],"stage4b_evidence_fields":["price_extension_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv","profile_path":"atlas/symbol_profiles/138/138040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.84,"MFE_90D_pct":28.91,"MFE_180D_pct":56.50,"MAE_30D_pct":-2.04,"MAE_90D_pct":-2.04,"MAE_180D_pct":-2.04,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-21","peak_price":107200.0,"max_drawdown_low_date":"2024-02-06","max_drawdown_low":67100.0,"drawdown_after_peak_pct":-7.46,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_reserve_capital_return_evidence","four_b_evidence_type":["price_only_extension_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_shallow_MAE","current_profile_verdict":"current_profile_correct_if_reserve_capital_return_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"138040_2024-01-31_68500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C22 can allow Stage2/Yellow when insurance strength is tied to reserve cycle, capital buffer and shareholder-return bridge. Green still requires exact reserve and capital-return evidence."}
```

### 6.2 211050 인카금융서비스 — GA distribution spike without reserve/capital bridge

Entry row: `2024-11-15 c=6400`, selected after the 2024-04-29 corporate-action candidate.  
Observed path: high `2024-11-28~12-02 h=6750`, later low `2024-12-18 l=5380`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L88_C22_211050_20241115_STAGE2_FALSE_POSITIVE_GA_DISTRIBUTION_SPIKE","case_id":"C22_R6L88_211050_INCAR_GA_DISTRIBUTION_SPIKE","symbol":"211050","company_name":"인카금융서비스","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"GA_DISTRIBUTION_SPIKE_WITHOUT_RESERVE_CAPITAL_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-GADistributionSpike-NoReserveCapitalBridge","trigger_date":"2024-11-15","entry_date":"2024-11-15","entry_price":6400.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_GA_distribution_financial_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; GA distribution spike treated as insufficient for C22 without reserve quality, loss-ratio discipline, capital buffer or capital-return bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["GA_distribution_theme","financial_beta_spike"],"stage3_evidence_fields":["reserve_quality_missing","loss_ratio_bridge_missing","capital_buffer_missing","shareholder_return_bridge_missing"],"stage4b_evidence_fields":["price_only_local_spike","reserve_capital_bridge_missing_watch","data_quality_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/211/211050/2024.csv","profile_path":"atlas/symbol_profiles/211/211050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.47,"MFE_90D_pct":5.47,"MFE_180D_pct":5.47,"MAE_30D_pct":-15.94,"MAE_90D_pct":-15.94,"MAE_180D_pct":-15.94,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-28","peak_price":6750.0,"max_drawdown_low_date":"2024-12-18","max_drawdown_low":5380.0,"drawdown_after_peak_pct":-20.30,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"GA_distribution_spike_without_reserve_capital_bridge_should_remain_watch_not_Yellow","four_b_evidence_type":["price_only","reserve_capital_bridge_missing_watch","data_quality_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_moderate_MAE_data_quality_watch","current_profile_verdict":"current_profile_false_positive_if_GA_distribution_beta_promoted_as_C22","calibration_usable":true,"forward_window_trading_days":"partial_2024_window_only; selected_entry_after_2024-04-29_candidate","calibration_block_reasons":["data_quality_watch_due_to_2024_corporate_action_candidate_before_entry","late_entry_partial_window"],"corporate_action_window_status":"selected_entry_after_2024-04-29_candidate","same_entry_group_id":"211050_2024-11-15_6400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.75,"do_not_count_as_new_case":false,"current_profile_residual":"C22 should not promote GA distribution spikes as reserve-cycle positives. Reserve quality, loss-ratio, capital buffer and shareholder-return evidence are required before Yellow/Green."}
```

### 6.3 244920 에이플러스에셋 — insurance distribution theme without loss-ratio/reserve bridge

Entry row: `2024-05-20 c=4420`.  
Observed path: local high around `2024-05-20 h=4500`, then the move lost strength into summer, with no C22 reserve or capital-return bridge attached.

```jsonl
{"row_type":"trigger","trigger_id":"R6L88_C22_244920_20240520_STAGE2_FALSE_POSITIVE_INSURANCE_DISTRIBUTION","case_id":"C22_R6L88_244920_APLUS_INSURANCE_DISTRIBUTION_THEME","symbol":"244920","company_name":"에이플러스에셋","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_DISTRIBUTION_THEME_WITHOUT_LOSS_RATIO_RESERVE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-InsuranceDistributionTheme-NoLossRatioReserveBridge","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":4420.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_insurance_distribution_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; insurance distribution theme treated as insufficient without loss-ratio, reserve, CSM/capital buffer, dividend or buyback bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["insurance_distribution_theme","financial_beta_rebound"],"stage3_evidence_fields":["loss_ratio_bridge_missing","reserve_quality_missing","capital_buffer_missing","capital_return_missing"],"stage4b_evidence_fields":["distribution_theme_watch","reserve_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/244/244920/2024.csv","profile_path":"atlas/symbol_profiles/244/244920.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.81,"MFE_90D_pct":1.81,"MFE_180D_pct":52.71,"MAE_30D_pct":-4.86,"MAE_90D_pct":-10.86,"MAE_180D_pct":-15.84,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-02","peak_price":6750.0,"max_drawdown_low_date":"2024-07-08","max_drawdown_low":3930.0,"drawdown_after_peak_pct":-20.30,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_rebound_not_reserve_cycle_validation; original insurance_distribution_theme_lacked_C22_bridge","four_b_evidence_type":["late_rebound_not_entry_validation","reserve_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub_Yellow_MFE_no_reserve_bridge","current_profile_verdict":"current_profile_false_positive_if_distribution_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"244920_2024-05-20_4420","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C22 should not retroactively validate an early weak insurance-distribution entry because of a later price rally. The original entry lacked reserve, loss-ratio, capital-buffer and capital-return bridge."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C22_R6L88_138040_MERITZ_HOLDCO_RESERVE_CAPITAL_RETURN","trigger_id":"R6L88_C22_138040_20240131_STAGE2_INSURANCE_HOLDCO_CAPITAL_RETURN","symbol":"138040","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C22 requires reserve quality and capital-return bridge rather than financial beta alone","raw_component_scores_before":{"reserve_quality_score":13,"loss_ratio_discipline_score":12,"capital_buffer_score":12,"capital_return_score":14,"buyback_dividend_score":12,"earnings_durability_score":10,"relative_strength_score":12,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"reserve_quality_score":16,"loss_ratio_discipline_score":14,"capital_buffer_score":15,"capital_return_score":17,"buyback_dividend_score":15,"earnings_durability_score":12,"relative_strength_score":13,"valuation_repricing_score":10,"execution_risk_score":-3,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Reserve-cycle and capital-return bridge plus high MFE support Yellow/Green-candidate watch; exact reserve and buyback/cancellation evidence still blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C22_R6L88_211050_INCAR_GA_DISTRIBUTION_SPIKE","trigger_id":"R6L88_C22_211050_20241115_STAGE2_FALSE_POSITIVE_GA_DISTRIBUTION_SPIKE","symbol":"211050","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_scope":"current_default_proxy","profile_hypothesis":"GA distribution spike without reserve/capital bridge should be blocked from C22 Yellow/Green","raw_component_scores_before":{"reserve_quality_score":0,"loss_ratio_discipline_score":0,"capital_buffer_score":0,"capital_return_score":1,"buyback_dividend_score":0,"earnings_durability_score":2,"relative_strength_score":9,"valuation_repricing_score":4,"execution_risk_score":-10,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"reserve_quality_score":0,"loss_ratio_discipline_score":0,"capital_buffer_score":0,"capital_return_score":0,"buyback_dividend_score":0,"earnings_durability_score":1,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Watch-Blocked","component_delta_explanation":"Distribution beta is not reserve-cycle evidence. Data-quality watch remains because of the earlier 2024 corporate-action candidate."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C22_R6L88_244920_APLUS_INSURANCE_DISTRIBUTION_THEME","trigger_id":"R6L88_C22_244920_20240520_STAGE2_FALSE_POSITIVE_INSURANCE_DISTRIBUTION","symbol":"244920","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_scope":"current_default_proxy","profile_hypothesis":"insurance distribution theme without loss-ratio/reserve bridge should remain Watch even if later price rebounds","raw_component_scores_before":{"reserve_quality_score":0,"loss_ratio_discipline_score":0,"capital_buffer_score":0,"capital_return_score":1,"buyback_dividend_score":0,"earnings_durability_score":2,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-8,"theme_spike_risk":-8,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"reserve_quality_score":0,"loss_ratio_discipline_score":0,"capital_buffer_score":0,"capital_return_score":0,"buyback_dividend_score":0,"earnings_durability_score":1,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-12,"theme_spike_risk":-12,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Watch-Blocked","component_delta_explanation":"Later price rally should not validate the original entry because no reserve, loss-ratio, capital-buffer or capital-return bridge was present."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R6L88_C22_P0_CURRENT","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C22 needs explicit reserve/loss-ratio/capital-buffer/capital-return bridge and insurance-distribution theme block","eligible_trigger_count":3,"avg_MFE90_pct":12.06,"avg_MAE90_pct":-9.61,"avg_MFE180_pct":38.23,"avg_MAE180_pct":-11.27,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.67,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C22_reserve_capital_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R6L88_C22_P1_SECTOR_SPECIFIC","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P1_L6_insurance_reserve_capital_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"Insurance signals need reserve quality, loss-ratio discipline, capital buffer, dividend/buyback, CSM/float quality or earnings durability before Stage2-Actionable","changed_axes":["reserve_quality_required","capital_buffer_required","distribution_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_reserve_loss_ratio_capital_buffer_capital_return_or_earnings_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":12.06,"avg_MAE90_pct":-9.61,"avg_MFE180_pct":38.23,"avg_MAE180_pct":-11.27,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R6L88_C22_P2_CANONICAL","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P2_C22_reserve_capital_return_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C22 should reward insurance balance-sheet mechanics, not GA/distribution theme labels","changed_axes":["C22_reserve_capital_return_bridge_required","C22_GA_distribution_theme_local_4B_guard","C22_late_rebound_not_reserve_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"reserve_quality_or_loss_ratio_plus_capital_return_or_buffer_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":12.06,"avg_MAE90_pct":-9.61,"avg_MFE180_pct":38.23,"avg_MAE180_pct":-11.27,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R6L88_C22_P3_COUNTEREXAMPLE_GUARD","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P3_C22_distribution_theme_missing_bridge_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If reserve/capital bridge is missing, distribution-theme rows cannot become Yellow/Green solely from price path; later rebounds do not validate the original weak entry","changed_axes":["C22_distribution_theme_guardrail","C22_late_rebound_not_validation"],"changed_thresholds":{"bad_entry_filter":"reserve_capital_bridge_missing_and_distribution_theme_only"},"eligible_trigger_count":3,"avg_MFE90_pct":12.06,"avg_MAE90_pct":-9.61,"avg_MFE180_pct":38.23,"avg_MAE180_pct":-11.27,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_INSURANCE_HOLDCO_BRIDGE_VS_DISTRIBUTION_THEME","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":12.06,"avg_MAE90_pct":-9.61,"avg_MFE180_pct":38.23,"avg_MAE180_pct":-11.27,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"interpretation":"C22 needs bridge discipline. 메리츠금융지주 shows reserve/capital-return mechanics can support a strong Stage2/Yellow path, while 인카금융서비스 and 에이플러스에셋 show insurance distribution or GA-channel themes should not be promoted without reserve, loss-ratio, capital-buffer and shareholder-return evidence."}
{"row_type":"stage_transition_summary","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"138040","trigger_type":"Stage2-Actionable-InsuranceHoldcoReserveCapitalReturnBridge-Positive","entry_date":"2024-01-31","stage2_to_90D_outcome":"good_stage2_high_MFE_shallow_MAE","stage2_to_180D_outcome":"positive_insurance_holdco_capital_return_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when reserve-cycle and capital-return bridge exists; Green requires exact reserve/capital-buffer/buyback evidence."}
{"row_type":"stage_transition_summary","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"211050","trigger_type":"Stage2-FalsePositive-GADistributionSpike-NoReserveCapitalBridge","entry_date":"2024-11-15","stage2_to_90D_outcome":"weak_stage2_low_MFE_moderate_MAE_partial_window","stage2_to_180D_outcome":"partial_window_watch_no_reserve_bridge","MFE90_ge_20":false,"MAE90_le_minus_20":false,"transition_note":"GA distribution spike without reserve/capital bridge should remain Watch; selected after 2024-04-29 candidate and marked data-quality watch."}
{"row_type":"stage_transition_summary","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"244920","trigger_type":"Stage2-FalsePositive-InsuranceDistributionTheme-NoLossRatioReserveBridge","entry_date":"2024-05-20","stage2_to_90D_outcome":"weak_stage2_sub_Yellow_MFE","stage2_to_180D_outcome":"late_rebound_not_original_entry_validation","MFE90_ge_20":false,"MAE90_le_minus_20":false,"transition_note":"Insurance distribution theme without loss-ratio/reserve bridge should remain Watch even if later price rallies."}
{"row_type":"residual_contribution","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","residual_type":"insurance_distribution_theme_overcredit_without_reserve_loss_ratio_capital_return_bridge","contribution":"Adds two C22 weak-bridge distribution/GA counterexamples against one insurance holdco reserve-capital-return positive, avoiding C22 top-covered and previous C22 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_HOLDCO_CAPITAL_RETURN_RESERVE_BRIDGE_VS_GA_DISTRIBUTION_THEME_EXTENSION_NO_RESERVE_BRIDGE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C22 now has a non-top-symbol insurance-holdco capital-return positive and two distribution/GA weak-bridge counterexamples; next R6 loops should exact-URL repair reserve quality, loss ratio, capital buffer, dividend/buyback and earnings durability evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","axis":"C22_reserve_capital_return_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"138040 worked when reserve/capital-return bridge proxy was present; 211050 and 244920 lacked reserve/loss-ratio/capital-return mechanics despite insurance-distribution theme exposure."}
{"row_type":"shadow_weight","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","axis":"C22_GA_distribution_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"GA and insurance-distribution rows should not become C22 positives without reserve quality, loss ratio, capital buffer and shareholder-return bridge."}
{"row_type":"shadow_weight","round":"R6","loop":"88","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","axis":"C22_late_rebound_not_reserve_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"244920 shows that later price movement should not validate the original distribution-theme entry when reserve/capital bridge was missing."}
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
  - GA_distribution_theme_overcredit
  - insurance_distribution_theme_overcredit
  - reserve_quality_bridge_missing
  - capital_return_bridge_missing
new_axis_proposed:
  - C22_reserve_capital_return_bridge_required_shadow_only
  - C22_GA_distribution_theme_local_4B_watch_guard_shadow_only
  - C22_late_rebound_not_reserve_validation_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C22
  - full_4b_requires_non_price_evidence within C22
  - hard_4c_thesis_break_routes_to_4c within C22
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
`211050` has a 2024-04-29 corporate-action candidate before the selected entry, so it remains usable as post-candidate price-path evidence but should keep a data-quality watch before any production patch.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
data_quality_watch = true for 211050
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
3. Confirm R6 / L6 / C22 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C22 top-covered symbols
   - previous R6 loop84 C22 symbols
   - previous R6 loop86 C22 symbols
   - previous R6 loop87 C21 symbols
6. Keep 211050 in data-quality watch because of the 2024-04-29 corporate-action candidate.
7. If aggregate support remains stable after exact evidence URL repair, consider C22-scoped safe patch candidates:
   - C22_reserve_capital_return_bridge_required
   - C22_GA_distribution_theme_local_4B_watch_guard
   - C22_late_rebound_not_reserve_validation_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R6
completed_loop = 88
next_round = R7
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C22_INSURANCE_RATE_CYCLE_RESERVE.
```
