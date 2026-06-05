# E2R Stock-Web v12 Residual Research — R6 Loop 90 / L6 / C22

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R6
loop: 90
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_AND_NONLIFE_THEME_SPIKE_DECAY
sector: financial / insurance / life insurance / non-life insurance / rate cycle / reserve / capital return
output_file: e2r_stock_web_v12_residual_round_R6_loop_90_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R5 loop 90`.

```text
scheduled_round = R6
scheduled_loop = 90
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
```

R6 is restricted to financial / capital-return / digital-financial names.  
C22 is selected because the immediately previous R6 loop used C21 financial ROE/PBR/capital-return, so the R6 lane rotates back into insurance rate-cycle / reserve quality.

No-Repeat Index snapshot:

```text
C22_INSURANCE_RATE_CYCLE_RESERVE
rows = 37
symbols = 12
good/bad Stage2 = 10/11
4B/4C = 2/0
top-covered = 000370, 003690, 082640, 000540, 000810, 005830
```

This loop avoids the C22 top-covered list and recent R6 loop symbols:

```text
R6 loop87 C21: 006800, 039490, 316140
R6 loop88 C22: 138040, 211050, 244920
R6 loop89 C21: 024110, 001510, 001200
```

Candidate hygiene note:

```text
During this execution path, R5/C19 consumer-brand candidates were touched while reading price files.
Those rows are not used in this R6/C22 output.
```

Selected symbols:

```text
032830, 088350, 000400
```

This loop tests:

```text
life-insurance rate / reserve / capital-buffer bridge
vs
life-insurance price spike without durable reserve/payout bridge
vs
non-life insurance M&A / theme spike without reserve-cycle and shareholder-return mechanics
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"032830","company_name":"삼성생명","profile_path":"atlas/symbol_profiles/032/032830.json","first_date":"2010-05-12","last_date":"2026-02-20","trading_day_count":3883,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"088350","company_name":"한화생명","profile_path":"atlas/symbol_profiles/088/088350.json","first_date":"2010-03-17","last_date":"2026-02-20","trading_day_count":3922,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"000400","company_name":"롯데손해보험","profile_path":"atlas/symbol_profiles/000/000400.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7717,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["2001-02-23","2002-01-28","2006-05-17","2012-12-26","2015-06-25","2019-10-25"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"032830","trigger_type":"Stage2-Actionable-LifeInsuranceRateReserveCapitalBufferBridge-Positive","entry_date":"2024-01-24","duplicate_status":"new C22 symbol/trigger/date combination outside C22 top-covered and previous R6 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"088350","trigger_type":"Stage2-FalsePositive-LifeInsurancePriceSpikeNoDurableReservePayoutBridge","entry_date":"2024-02-13","duplicate_status":"new C22 symbol/trigger/date combination outside C22 top-covered and previous R6 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"000400","trigger_type":"Stage2-FalsePositive-NonlifeInsuranceMNAThemeNoReserveCycleCapitalReturnBridge","entry_date":"2024-02-13","duplicate_status":"new C22 symbol/trigger/date combination outside C22 top-covered and previous R6 loop symbols"}
```

## 4. Research question

C22 is not “보험주가 올랐다.”  
The useful insurance rate-cycle signal must prove the bridge from rate and accounting regime into durable shareholder economics:

```text
CSM / reserve quality
capital buffer / K-ICS resilience
asset-liability duration fit
new-business margin or loss-ratio improvement
rate-cycle sensitivity
dividend payout visibility
buyback or cancellation possibility
earnings durability
cash and solvency discipline
```

A rate-cycle headline without that bridge is an insurance policy with no underwriting file attached. The premium is visible, but the reserve quality and capital release are still unproven.

Residual question:

```text
Can C22 distinguish:
1. life-insurance rate/reserve/capital-buffer bridge with very high MFE and low entry MAE,
2. life-insurance price spike where a rate/value-up label is not enough without durable reserve and payout bridge,
3. non-life insurance M&A/theme spike where MFE is price-only and later MAE proves it is not a reserve-cycle signal?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C22_R6L90_032830_SAMSUNG_LIFE_RATE_RESERVE_CAPITAL","symbol":"032830","company_name":"삼성생명","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-LifeInsuranceRateReserveCapitalBufferBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_low_MAE_capital_return_bridge","current_profile_verdict":"current_profile_correct_if_reserve_capital_buffer_payout_bridge_required","price_source":"Songdaiki/stock-web","notes":"Life-insurance rate/reserve/capital-buffer proxy produced very high MFE with shallow entry MAE. Green still requires exact CSM/reserve quality, capital buffer, payout and earnings durability evidence."}
{"row_type":"case","case_id":"C22_R6L90_088350_HANWHA_LIFE_PRICE_SPIKE","symbol":"088350","company_name":"한화생명","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_PRICE_SPIKE_WITHOUT_DURABLE_RESERVE_PAYOUT_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LifeInsurancePriceSpikeNoDurableReservePayoutBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_reserve_payout_bridge","current_profile_verdict":"current_profile_false_positive_if_life_insurance_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Life-insurance price spike had low forward MFE and later deep MAE without exact reserve-quality, capital-buffer and payout bridge."}
{"row_type":"case","case_id":"C22_R6L90_000400_LOTTE_NONLIFE_MNA_THEME","symbol":"000400","company_name":"롯데손해보험","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_INSURANCE_MNA_THEME_WITHOUT_RESERVE_CYCLE_CAPITAL_RETURN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-NonlifeInsuranceMNAThemeNoReserveCycleCapitalReturnBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_only_local_MFE_deep_MAE_no_reserve_cycle_bridge","current_profile_verdict":"current_profile_false_positive_if_MNA_theme_counted_as_C22_rate_cycle","price_source":"Songdaiki/stock-web","notes":"Non-life insurance M&A/theme spike had local price MFE but no reserve-cycle, capital buffer, payout or underwriting-quality bridge; later deep MAE makes it 4B-watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 032830 삼성생명 — life-insurance rate/reserve/capital-buffer bridge positive

Entry row: `2024-01-24 c=62600`.  
Observed path: early low `2024-01-24 l=61700`, strong peak `2024-03-08 h=108500`, and later Q4 high `2024-11-18 h=111000`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L90_C22_032830_20240124_STAGE2_LIFE_RATE_RESERVE_CAPITAL","case_id":"C22_R6L90_032830_SAMSUNG_LIFE_RATE_RESERVE_CAPITAL","symbol":"032830","company_name":"삼성생명","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-LifeInsuranceRateReserveCapitalBufferBridge-Positive","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":62600.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_life_insurance_rate_reserve_capital_buffer_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; CSM/reserve quality, capital buffer, payout and value-up bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["rate_cycle_proxy","reserve_quality_proxy","capital_buffer_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_CSM_or_reserve_source_pending","KICS_or_capital_buffer_pending","payout_policy_pending","earnings_durability_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv","profile_path":"atlas/symbol_profiles/032/032830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":73.32,"MFE_90D_pct":73.32,"MFE_180D_pct":73.32,"MAE_30D_pct":-1.44,"MAE_90D_pct":-1.44,"MAE_180D_pct":-1.44,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-08","peak_price":108500.0,"max_drawdown_low_date":"2024-01-24","max_drawdown_low":61700.0,"drawdown_after_peak_pct":-18.43,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_reserve_capital_payout_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_low_MAE_capital_return_bridge","current_profile_verdict":"current_profile_correct_if_reserve_capital_buffer_payout_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"032830_2024-01-24_62600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C22 can allow Stage2/Yellow when insurance strength is tied to reserve quality, rate-cycle sensitivity, capital buffer, payout policy and earnings durability. Green still requires exact source-grade evidence."}
```

### 6.2 088350 한화생명 — life-insurance price spike without durable reserve/payout bridge

Entry row: `2024-02-13 c=3550`, after the sharp value-up / life-insurance spike.  
Observed path: same-day high `2024-02-13 h=3815`, then later low `2024-12-17 l=2440`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L90_C22_088350_20240213_STAGE2_FALSE_POSITIVE_LIFE_PRICE_SPIKE","case_id":"C22_R6L90_088350_HANWHA_LIFE_PRICE_SPIKE","symbol":"088350","company_name":"한화생명","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_PRICE_SPIKE_WITHOUT_DURABLE_RESERVE_PAYOUT_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-LifeInsurancePriceSpikeNoDurableReservePayoutBridge","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":3550.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_life_insurance_valueup_price_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; life-insurance value-up/price spike treated as insufficient without durable reserve quality, capital buffer, payout and earnings durability bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["life_insurance_price_spike","valueup_keyword","relative_strength_spike"],"stage3_evidence_fields":["durable_reserve_quality_missing","capital_buffer_missing","payout_visibility_missing","earnings_durability_missing"],"stage4b_evidence_fields":["low_MFE_watch","reserve_payout_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv","profile_path":"atlas/symbol_profiles/088/088350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.46,"MFE_90D_pct":7.46,"MFE_180D_pct":7.46,"MAE_30D_pct":-13.52,"MAE_90D_pct":-21.27,"MAE_180D_pct":-30.70,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-13","peak_price":3815.0,"max_drawdown_low_date":"2024-12-17","max_drawdown_low":2440.0,"drawdown_after_peak_pct":-36.04,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"life_insurance_price_spike_without_durable_reserve_payout_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","reserve_payout_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_reserve_payout_bridge","current_profile_verdict":"current_profile_false_positive_if_life_insurance_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"088350_2024-02-13_3550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C22 should not promote life-insurance price spikes unless reserve quality, capital buffer, payout visibility and earnings durability are exact-repaired. Low MFE and deep MAE require Watch/4B routing."}
```

### 6.3 000400 롯데손해보험 — non-life insurance M&A/theme spike without reserve-cycle bridge

Entry row: `2024-02-13 c=3370`, on a sharp non-life insurance / M&A-theme spike.  
Observed path: local high `2024-02-16 h=3670`, then drawdown to `2024-12-09 l=1814`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L90_C22_000400_20240213_STAGE2_FALSE_POSITIVE_NONLIFE_MNA_THEME","case_id":"C22_R6L90_000400_LOTTE_NONLIFE_MNA_THEME","symbol":"000400","company_name":"롯데손해보험","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_INSURANCE_MNA_THEME_WITHOUT_RESERVE_CYCLE_CAPITAL_RETURN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;price_only_blowoff_stress_test","trigger_type":"Stage2-FalsePositive-NonlifeInsuranceMNAThemeNoReserveCycleCapitalReturnBridge","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":3370.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_nonlife_insurance_MNA_theme_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; non-life insurance M&A/theme spike treated as insufficient for C22 without underwriting quality, reserve cycle, capital buffer, payout and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["nonlife_insurance_MNA_theme","relative_strength_spike"],"stage3_evidence_fields":["underwriting_quality_missing","reserve_cycle_bridge_missing","capital_buffer_missing","payout_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_MFE","MNA_theme_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv","profile_path":"atlas/symbol_profiles/000/000400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.90,"MFE_90D_pct":8.90,"MFE_180D_pct":8.90,"MAE_30D_pct":-17.51,"MAE_90D_pct":-23.59,"MAE_180D_pct":-46.17,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-16","peak_price":3670.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":1814.0,"drawdown_after_peak_pct":-50.57,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"nonlife_MNA_theme_without_reserve_cycle_capital_return_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","MNA_theme_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_only_local_MFE_deep_MAE_no_reserve_cycle_bridge","current_profile_verdict":"current_profile_false_positive_if_MNA_theme_counted_as_C22_rate_cycle","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"000400_2024-02-13_3370","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C22 should not count M&A/theme MFE as reserve-cycle evidence. Underwriting quality, reserve/capital bridge, payout visibility and cash conversion must be repaired before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L90_032830_SAMSUNG_LIFE_RATE_RESERVE_CAPITAL","trigger_id":"R6L90_C22_032830_20240124_STAGE2_LIFE_RATE_RESERVE_CAPITAL","symbol":"032830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C22 requires reserve quality, capital buffer, rate sensitivity, payout visibility and earnings durability rather than insurance price strength alone","raw_component_scores_before":{"reserve_quality_score":13,"capital_buffer_score":14,"rate_cycle_sensitivity_score":12,"asset_liability_fit_score":11,"payout_visibility_score":10,"earnings_durability_score":10,"cash_solvency_score":8,"relative_strength_score":15,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"reserve_quality_score":16,"capital_buffer_score":17,"rate_cycle_sensitivity_score":15,"asset_liability_fit_score":13,"payout_visibility_score":12,"earnings_durability_score":12,"cash_solvency_score":10,"relative_strength_score":16,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":90,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Reserve/capital/payout bridge plus very high MFE supports Yellow/Green-candidate watch; exact CSM/K-ICS/payout evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L90_088350_HANWHA_LIFE_PRICE_SPIKE","trigger_id":"R6L90_C22_088350_20240213_STAGE2_FALSE_POSITIVE_LIFE_PRICE_SPIKE","symbol":"088350","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_scope":"current_default_proxy","profile_hypothesis":"life-insurance price spike without durable reserve/capital/payout bridge should be blocked","raw_component_scores_before":{"reserve_quality_score":2,"capital_buffer_score":1,"rate_cycle_sensitivity_score":4,"asset_liability_fit_score":1,"payout_visibility_score":0,"earnings_durability_score":1,"cash_solvency_score":1,"relative_strength_score":10,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"reserve_quality_score":0,"capital_buffer_score":0,"rate_cycle_sensitivity_score":1,"asset_liability_fit_score":0,"payout_visibility_score":0,"earnings_durability_score":0,"cash_solvency_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE convert the life-insurance price spike into missing reserve/payout bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L90_000400_LOTTE_NONLIFE_MNA_THEME","trigger_id":"R6L90_C22_000400_20240213_STAGE2_FALSE_POSITIVE_NONLIFE_MNA_THEME","symbol":"000400","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_scope":"current_default_proxy","profile_hypothesis":"non-life M&A/theme spike without reserve-cycle and capital-return bridge should remain Watch/4B even with local MFE","raw_component_scores_before":{"reserve_quality_score":1,"capital_buffer_score":1,"rate_cycle_sensitivity_score":1,"asset_liability_fit_score":0,"payout_visibility_score":0,"earnings_durability_score":0,"cash_solvency_score":0,"relative_strength_score":13,"valuation_repricing_score":4,"execution_risk_score":-16,"theme_spike_risk":-22,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"reserve_quality_score":0,"capital_buffer_score":0,"rate_cycle_sensitivity_score":0,"asset_liability_fit_score":0,"payout_visibility_score":0,"earnings_durability_score":0,"cash_solvency_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Local MFE is price-only; deep MAE and missing underwriting/reserve/payout bridge block Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R6L90_C22_P0_CURRENT","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C22 needs explicit reserve quality, capital buffer, rate sensitivity, payout, earnings durability and insurance-theme 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":29.89,"avg_MAE90_pct":-15.43,"avg_MFE180_pct":29.89,"avg_MAE180_pct":-26.10,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C22_reserve_capital_payout_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R6L90_C22_P1_SECTOR_SPECIFIC","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P1_L6_insurance_reserve_capital_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L6 insurance signals need reserve quality, K-ICS/capital buffer, rate-cycle sensitivity, asset-liability fit, payout or earnings durability before Stage2-Actionable","changed_axes":["reserve_quality_required","capital_buffer_payout_required","insurance_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_reserve_quality_capital_buffer_rate_sensitivity_ALM_payout_or_earnings_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":29.89,"avg_MAE90_pct":-15.43,"avg_MFE180_pct":29.89,"avg_MAE180_pct":-26.10,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R6L90_C22_P2_CANONICAL","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P2_C22_reserve_capital_payout_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C22 should reward reserve-to-capital-return mechanics, not insurance theme or M&A labels","changed_axes":["C22_reserve_capital_payout_bridge_required","C22_life_nonlife_theme_local_4B_guard","C22_MNA_price_only_not_reserve_cycle_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"reserve_quality_or_capital_buffer_plus_payout_or_earnings_durability_required"},"eligible_trigger_count":3,"avg_MFE90_pct":29.89,"avg_MAE90_pct":-15.43,"avg_MFE180_pct":29.89,"avg_MAE180_pct":-26.10,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R6L90_C22_P3_COUNTEREXAMPLE_GUARD","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P3_C22_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If reserve/capital/payout bridge is missing, MFE90<10 or MAE180<=-25 should block Yellow/Green and route to 4B-watch","changed_axes":["C22_low_MFE_guardrail","C22_deep_MAE_4B_guardrail","C22_MNA_theme_watch_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_10_or_MAE180_le_minus_25)"},"eligible_trigger_count":3,"avg_MFE90_pct":29.89,"avg_MAE90_pct":-15.43,"avg_MFE180_pct":29.89,"avg_MAE180_pct":-26.10,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_LIFE_RESERVE_POSITIVE_VS_INSURANCE_THEME_SPIKE_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":29.89,"avg_MAE90_pct":-15.43,"avg_MFE180_pct":29.89,"avg_MAE180_pct":-26.10,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE180_le_minus25":0.67,"interpretation":"C22 needs bridge discipline. 삼성생명 shows life-insurance reserve/capital-buffer/payout bridge can support Yellow/Green-candidate-watch, while 한화생명 and 롯데손해보험 show insurance price spikes or M&A themes should not be promoted without reserve quality, capital buffer, payout, earnings durability and cash/solvency evidence."}
{"row_type":"stage_transition_summary","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"032830","trigger_type":"Stage2-Actionable-LifeInsuranceRateReserveCapitalBufferBridge-Positive","entry_date":"2024-01-24","stage2_to_90D_outcome":"good_stage2_very_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_reserve_capital_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when insurance strength is tied to reserve quality, capital buffer, rate sensitivity, payout and earnings durability; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"088350","trigger_type":"Stage2-FalsePositive-LifeInsurancePriceSpikeNoDurableReservePayoutBridge","entry_date":"2024-02-13","stage2_to_90D_outcome":"bad_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"failed_life_insurance_spike_deep_MAE","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Life-insurance price spike without durable reserve/capital/payout bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"000400","trigger_type":"Stage2-FalsePositive-NonlifeInsuranceMNAThemeNoReserveCycleCapitalReturnBridge","entry_date":"2024-02-13","stage2_to_90D_outcome":"price_only_local_MFE_no_reserve_bridge","stage2_to_180D_outcome":"failed_MNA_theme_deep_MAE","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Non-life M&A/theme MFE without reserve-cycle and capital-return bridge should be treated as 4B-watch, not positive C22 evidence."}
{"row_type":"residual_contribution","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","residual_type":"insurance_price_theme_overcredit_without_reserve_capital_payout_bridge","contribution":"Adds two C22 4B counterexamples against one life-insurance reserve/capital positive, avoiding C22 top-covered and recent R6 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_AND_NONLIFE_THEME_SPIKE_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C22 now has non-top-symbol life-insurance reserve/capital positive and two insurance-theme weak-bridge counterexamples; next R6 C22 loops should exact-URL repair CSM/reserve quality, K-ICS/capital buffer, ALM, payout policy, underwriting quality, earnings durability and cash/solvency evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","axis":"C22_reserve_capital_payout_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"032830 worked when reserve/capital/payout proxy existed; 088350 and 000400 failed when insurance price action lacked durable reserve/capital-return evidence."}
{"row_type":"shadow_weight","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","axis":"C22_life_nonlife_theme_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Life/non-life theme rows showed MFE90 below 10 and MAE180 below -25 when non-price reserve/capital/payout evidence was missing."}
{"row_type":"shadow_weight","round":"R6","loop":"90","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","axis":"C22_MNA_price_only_not_reserve_cycle_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"000400 shows local M&A/theme MFE should not validate C22 unless reserve-cycle, underwriting, capital and payout evidence are repaired."}
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
  - insurance_theme_overcredit
  - MNA_theme_overcredit
  - reserve_quality_bridge_missing
  - capital_buffer_payout_bridge_missing
new_axis_proposed:
  - C22_reserve_capital_payout_bridge_required_shadow_only
  - C22_life_nonlife_theme_local_4B_guard_shadow_only
  - C22_MNA_price_only_not_reserve_cycle_validation_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows and clean selected 2024 entry windows.  
`000400` has historical corporate-action candidate dates before 2024, but the selected 2024 window is usable for price-path residual calibration.  
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
3. Confirm R6 / L6 / C22 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C22 top-covered symbols
   - previous R6 loop87 C21 symbols
   - previous R6 loop88 C22 symbols
   - previous R6 loop89 C21 symbols
6. Confirm accidentally touched R5/C19 candidate rows are not ingested from this MD.
7. If aggregate support remains stable after exact evidence URL repair, consider C22-scoped safe patch candidates:
   - C22_reserve_capital_payout_bridge_required
   - C22_life_nonlife_theme_local_4B_guard
   - C22_MNA_price_only_not_reserve_cycle_validation_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R6
completed_loop = 90
next_round = R7
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C22_INSURANCE_RATE_CYCLE_RESERVE.
```
