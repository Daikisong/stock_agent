# E2R Stock-Web v12 Residual Research — R6 Loop 86 / L6 / C22

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R6
loop: 86
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: INSURANCE_RATE_CYCLE_CAPITAL_RETURN_RESERVE_BRIDGE_VS_SMALLCAP_INSURANCE_BETA_MNA_SPIKE
sector: financials / insurance / rate cycle / reserve / capital return
output_file: e2r_stock_web_v12_residual_round_R6_loop_86_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R5 loop 86`.

```text
scheduled_round = R6
scheduled_loop = 86
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
```

R6 is restricted to financial / capital return / digital finance.  
C22 is selected because the previous R6 loop used C21 bank/ROE/PBR/capital-return evidence, while C22 remains the insurance rate/reserve cycle bucket.

The No-Repeat Index shows C22 as:

```text
C22_INSURANCE_RATE_CYCLE_RESERVE
rows = 37
symbols = 12
good/bad Stage2 = 10/11
4B/4C = 2/0
top-covered = 000370, 003690, 082640, 000540, 000810, 005830
```

This loop avoids those top-covered symbols and also avoids the immediately previous R6 loop85 C21 digital-finance/bank symbols:

```text
086790, 323410, 377300
```

The question is not whether insurance can rerate in a rate/capital-return cycle. It can. The residual question is whether C22 can distinguish actual reserve/capital-return bridge from small-cap insurance beta, M&A rumor, or rate-cycle headline without capital quality.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"001450","company_name":"현대해상","profile_path":"atlas/symbol_profiles/001/001450.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7761,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2004-07-13"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"000400","company_name":"롯데손해보험","profile_path":"atlas/symbol_profiles/000/000400.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7717,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["2001-02-23","2002-01-28","2006-05-17","2012-12-26","2015-06-25","2019-10-25"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"085620","company_name":"미래에셋생명","profile_path":"atlas/symbol_profiles/085/085620.json","first_date":"2015-07-08","last_date":"2026-02-20","trading_day_count":2606,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2018-03-23"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"001450","trigger_type":"Stage2-Actionable-PandCReserveCycleCapitalReturnBridge-Positive","entry_date":"2024-01-24","duplicate_status":"new C22 symbol/trigger/date combination outside top-covered list and previous R6 loop85 C21 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"000400","trigger_type":"Stage2-FalsePositive-SmallcapInsuranceMnaBeta-NoReserveCapitalBridge","entry_date":"2024-04-23","duplicate_status":"new C22 symbol/trigger/date combination outside top-covered list and previous R6 loop85 C21 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"085620","trigger_type":"Stage2-FalsePositive-LifeInsuranceRateBeta-NoCapitalReturnReserveBridge","entry_date":"2024-02-13","duplicate_status":"new C22 symbol/trigger/date combination outside top-covered list and previous R6 loop85 C21 symbols"}
```

## 4. Research question

C22 is not “insurance name is up because rates are high.”  
The useful insurance signal is the underwriting and reserve machine: reserve burden normalization, CSM or embedded-value quality, loss-ratio stability, capital buffer, dividend/buyback credibility, and valuation repair. If only the rate-cycle or M&A headline moves first, the stock can flare and then leak like an under-reserved book.

Residual question:

```text
Can C22 distinguish:
1. P&C insurance reserve/capital-return bridge with positive MFE and low MAE,
2. small-cap insurance/M&A beta spike without reserve/capital bridge,
3. life-insurance rate-cycle beta where capital return and reserve quality remain unverified?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C22_R6L86_001450_HYUNDAIMARINE_RESERVE_CAPITAL_RETURN","symbol":"001450","company_name":"현대해상","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"PANDC_RESERVE_CYCLE_CAPITAL_RETURN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-PandCReserveCycleCapitalReturnBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_MFE90_ge20_low_MAE","current_profile_verdict":"current_profile_correct_if_reserve_capital_return_bridge_required","price_source":"Songdaiki/stock-web","notes":"P&C reserve/capital-return proxy produced MFE above 20% and shallow MAE. Green still needs exact reserve, loss-ratio, CSM/capital and shareholder-return evidence."}
{"row_type":"case","case_id":"C22_R6L86_000400_LOTTEINSURANCE_MNA_BETA_NO_RESERVE_BRIDGE","symbol":"000400","company_name":"롯데손해보험","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"SMALLCAP_INSURANCE_MNA_BETA_WITHOUT_RESERVE_CAPITAL_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SmallcapInsuranceMnaBeta-NoReserveCapitalBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_MNA_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"Small-cap insurer/M&A beta had only low MFE and severe MAE when reserve quality, capital buffer and capital-return bridge were missing."}
{"row_type":"case","case_id":"C22_R6L86_085620_MIRAE_LIFE_RATE_BETA_NO_CAPITAL_RETURN","symbol":"085620","company_name":"미래에셋생명","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_RATE_BETA_WITHOUT_CAPITAL_RETURN_RESERVE_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LifeInsuranceRateBeta-NoCapitalReturnReserveBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE_then_late_rebound","current_profile_verdict":"current_profile_false_positive_if_rate_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"Life-insurance rate-cycle beta produced low MFE and high early MAE before later unrelated rebound; without reserve/capital-return bridge it should not be Yellow/Green."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 001450 현대해상 — P&C reserve/capital-return bridge positive

Entry row: `2024-01-24 c=30150`.  
Observed path: early low `2024-01-24 l=29550`, local high `2024-02-05 h=36800`, and later lows around `2024-04-12 l=28700`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L86_C22_001450_20240124_STAGE2_PANDC_RESERVE_CAPITAL_RETURN","case_id":"C22_R6L86_001450_HYUNDAIMARINE_RESERVE_CAPITAL_RETURN","symbol":"001450","company_name":"현대해상","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"PANDC_RESERVE_CYCLE_CAPITAL_RETURN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-PandCReserveCycleCapitalReturnBridge-Positive","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":30150.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_insurance_rate_cycle_reserve_capital_return_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; P&C reserve cycle, capital buffer and shareholder-return thesis treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["reserve_normalization_proxy","loss_ratio_quality_proxy","capital_return_proxy","relative_strength_turn"],"stage3_evidence_fields":["CSM_or_capital_buffer_pending","dividend_buyback_confirmation_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.06,"MFE_90D_pct":22.06,"MFE_180D_pct":22.06,"MAE_30D_pct":-1.99,"MAE_90D_pct":-4.81,"MAE_180D_pct":-4.81,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-05","peak_price":36800.0,"max_drawdown_low_date":"2024-04-12","max_drawdown_low":28700.0,"drawdown_after_peak_pct":-22.01,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_MFE90_ge20_low_MAE","current_profile_verdict":"current_profile_correct_if_reserve_capital_return_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"001450_2024-01-24_30150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C22 can allow Watch/Yellow when P&C reserve, loss-ratio and capital-return bridge exists. Green still requires exact reserve/capital/shareholder-return evidence."}
```

### 6.2 000400 롯데손해보험 — small-cap insurer/M&A beta without reserve/capital bridge

Entry row: `2024-04-23 c=3850`.  
Observed path: local highs `2024-04-25 h=4035` and `2024-06-26 h=4090`, then lows `2024-07-02 l=2505`, `2024-10-25 l=2150`, and `2024-12-09 l=1814`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L86_C22_000400_20240423_STAGE2_FALSE_POSITIVE_SMALLCAP_INSURANCE_MNA_BETA","case_id":"C22_R6L86_000400_LOTTEINSURANCE_MNA_BETA_NO_RESERVE_BRIDGE","symbol":"000400","company_name":"롯데손해보험","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"SMALLCAP_INSURANCE_MNA_BETA_WITHOUT_RESERVE_CAPITAL_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-SmallcapInsuranceMnaBeta-NoReserveCapitalBridge","trigger_date":"2024-04-23","entry_date":"2024-04-23","entry_price":3850.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_smallcap_insurance_MNA_beta_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; small-cap insurance/M&A beta treated as insufficient without reserve quality, capital buffer, loss-ratio stability and shareholder-return bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["smallcap_insurance_beta","MNA_or_valueup_theme","relative_strength_spike"],"stage3_evidence_fields":["reserve_quality_missing","capital_buffer_missing","loss_ratio_bridge_missing","capital_return_confirmation_missing"],"stage4b_evidence_fields":["price_only_local_peak","reserve_capital_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv","profile_path":"atlas/symbol_profiles/000/000400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.81,"MFE_90D_pct":6.23,"MFE_180D_pct":6.23,"MAE_30D_pct":-20.39,"MAE_90D_pct":-34.94,"MAE_180D_pct":-52.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-26","peak_price":4090.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":1814.0,"drawdown_after_peak_pct":-55.65,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"smallcap_insurance_beta_without_reserve_capital_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","reserve_capital_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_MNA_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"000400_2024-04-23_3850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C22 should not upgrade small-cap insurance/M&A beta without reserve/capital bridge. Low MFE and severe MAE require Watch/4B-risk routing."}
```

### 6.3 085620 미래에셋생명 — life-insurance rate beta without capital-return/reserve bridge

Entry row: `2024-02-13 c=5950`.  
Observed path: local high `2024-02-13 h=6420`, early low `2024-04-02 l=4425`, later rebound to `2024-07-04 h=5940`, but the weak original entry is not rehabilitated by the later unrelated bounce.

```jsonl
{"row_type":"trigger","trigger_id":"R6L86_C22_085620_20240213_STAGE2_FALSE_POSITIVE_LIFE_INSURANCE_RATE_BETA","case_id":"C22_R6L86_085620_MIRAE_LIFE_RATE_BETA_NO_CAPITAL_RETURN","symbol":"085620","company_name":"미래에셋생명","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_RATE_BETA_WITHOUT_CAPITAL_RETURN_RESERVE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-LifeInsuranceRateBeta-NoCapitalReturnReserveBridge","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":5950.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_life_insurance_rate_cycle_beta_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; life-insurance rate-cycle beta treated as insufficient without capital return, reserve quality, CSM/EV and shareholder-return bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["life_insurance_rate_beta","relative_strength_spike"],"stage3_evidence_fields":["capital_return_bridge_missing","reserve_quality_missing","CSM_EV_bridge_missing","shareholder_return_confirmation_missing"],"stage4b_evidence_fields":["price_only_local_peak","capital_return_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv","profile_path":"atlas/symbol_profiles/085/085620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.90,"MFE_90D_pct":7.90,"MFE_180D_pct":7.90,"MAE_30D_pct":-24.37,"MAE_90D_pct":-25.63,"MAE_180D_pct":-25.63,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-13","peak_price":6420.0,"max_drawdown_low_date":"2024-04-02","max_drawdown_low":4425.0,"drawdown_after_peak_pct":-31.07,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"life_insurance_rate_beta_without_capital_return_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","capital_return_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE_then_late_rebound","current_profile_verdict":"current_profile_false_positive_if_rate_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"085620_2024-02-13_5950","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C22 should not promote life-insurance rate beta without capital-return and reserve-quality bridge. The original low-MFE/high-MAE entry should stay Watch/4B even if a later rebound appears."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L86_001450_HYUNDAIMARINE_RESERVE_CAPITAL_RETURN","trigger_id":"R6L86_C22_001450_20240124_STAGE2_PANDC_RESERVE_CAPITAL_RETURN","symbol":"001450","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C22 requires reserve and capital-return bridge rather than insurance beta alone","raw_component_scores_before":{"rate_cycle_score":12,"reserve_quality_score":13,"loss_ratio_quality_score":12,"capital_buffer_score":10,"capital_return_score":11,"relative_strength_score":10,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":68,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"rate_cycle_score":14,"reserve_quality_score":16,"loss_ratio_quality_score":14,"capital_buffer_score":12,"capital_return_score":14,"relative_strength_score":11,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable/Stage3-Yellow-Watch","component_delta_explanation":"Reserve/capital-return bridge and low MAE support Yellow-watch; exact CSM/capital buffer and dividend/buyback evidence still blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L86_000400_LOTTEINSURANCE_MNA_BETA_NO_RESERVE_BRIDGE","trigger_id":"R6L86_C22_000400_20240423_STAGE2_FALSE_POSITIVE_SMALLCAP_INSURANCE_MNA_BETA","symbol":"000400","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_scope":"current_default_proxy","profile_hypothesis":"small-cap insurance/M&A beta without reserve/capital bridge should be blocked","raw_component_scores_before":{"rate_cycle_score":8,"reserve_quality_score":1,"loss_ratio_quality_score":1,"capital_buffer_score":1,"capital_return_score":0,"relative_strength_score":13,"valuation_repricing_score":6,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"rate_cycle_score":3,"reserve_quality_score":0,"loss_ratio_quality_score":0,"capital_buffer_score":0,"capital_return_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE convert small-cap insurance beta into reserve/capital bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L86_085620_MIRAE_LIFE_RATE_BETA_NO_CAPITAL_RETURN","trigger_id":"R6L86_C22_085620_20240213_STAGE2_FALSE_POSITIVE_LIFE_INSURANCE_RATE_BETA","symbol":"085620","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_scope":"current_default_proxy","profile_hypothesis":"life-insurance rate beta without shareholder-return bridge should remain Watch/blocked","raw_component_scores_before":{"rate_cycle_score":9,"reserve_quality_score":2,"loss_ratio_quality_score":2,"capital_buffer_score":2,"capital_return_score":0,"relative_strength_score":12,"valuation_repricing_score":6,"execution_risk_score":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":12,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"rate_cycle_score":4,"reserve_quality_score":0,"loss_ratio_quality_score":0,"capital_buffer_score":1,"capital_return_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and high MAE require reserve/capital-return bridge before any Yellow/Green promotion. Later rebound does not validate the original weak entry."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R6L86_C22_P0_CURRENT","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C22 needs explicit reserve, loss-ratio, capital buffer and capital-return bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":12.06,"avg_MAE90_pct":-21.79,"avg_MFE180_pct":12.06,"avg_MAE180_pct":-27.77,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C22_reserve_capital_return_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R6L86_C22_P1_SECTOR_SPECIFIC","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P1_L6_insurance_reserve_capital_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L6 insurance signals need reserve quality, loss ratio, CSM/capital buffer, shareholder return or EV/earnings bridge before Stage2-Actionable","changed_axes":["reserve_quality_required","capital_buffer_required","insurance_beta_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_reserve_quality_loss_ratio_capital_buffer_or_capital_return_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":12.06,"avg_MAE90_pct":-21.79,"avg_MFE180_pct":12.06,"avg_MAE180_pct":-27.77,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R6L86_C22_P2_CANONICAL","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P2_C22_reserve_capital_return_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C22 should reward reserve/capital-return mechanics, not small-cap insurance or life-insurance rate beta","changed_axes":["C22_reserve_capital_return_bridge_required","C22_smallcap_insurance_beta_local_4B_guard","C22_late_rebound_not_entry_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"reserve_quality_or_capital_return_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":12.06,"avg_MAE90_pct":-21.79,"avg_MFE180_pct":12.06,"avg_MAE180_pct":-27.77,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R6L86_C22_P3_COUNTEREXAMPLE_GUARD","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","profile_id":"P3_C22_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-20 while reserve/capital bridge is missing, block Yellow/Green","changed_axes":["C22_high_MAE_guardrail","C22_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_20"},"eligible_trigger_count":3,"avg_MFE90_pct":12.06,"avg_MAE90_pct":-21.79,"avg_MFE180_pct":12.06,"avg_MAE180_pct":-27.77,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_RESERVE_CAPITAL_RETURN_VS_INSURANCE_BETA_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":12.06,"avg_MAE90_pct":-21.79,"avg_MFE180_pct":12.06,"avg_MAE180_pct":-27.77,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C22 needs bridge discipline. 현대해상 shows insurance reserve/capital-return bridge can produce a usable rerating, while 롯데손해보험 and 미래에셋생명 show that small-cap/M&A/rate-cycle beta fails when reserve, capital buffer and shareholder-return evidence are missing."}
{"row_type":"stage_transition_summary","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"001450","trigger_type":"Stage2-Actionable-PandCReserveCycleCapitalReturnBridge-Positive","entry_date":"2024-01-24","stage2_to_90D_outcome":"good_stage2_MFE90_ge20_low_MAE","stage2_to_180D_outcome":"watch_positive_reserve_capital_bridge","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when reserve/loss-ratio/capital-return bridge exists; Green requires exact CSM/capital/shareholder-return evidence."}
{"row_type":"stage_transition_summary","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"000400","trigger_type":"Stage2-FalsePositive-SmallcapInsuranceMnaBeta-NoReserveCapitalBridge","entry_date":"2024-04-23","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_smallcap_insurance_beta","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Small-cap insurance/M&A beta without reserve and capital bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"085620","trigger_type":"Stage2-FalsePositive-LifeInsuranceRateBeta-NoCapitalReturnReserveBridge","entry_date":"2024-02-13","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"weak_original_entry_later_rebound_not_validation","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Life-insurance rate beta without capital-return/reserve bridge should stay Watch/4B-risk. Later bounce should not validate the original weak entry."}
{"row_type":"residual_contribution","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","residual_type":"insurance_rate_cycle_beta_overcredit_without_reserve_capital_return_bridge","contribution":"Adds two C22 local 4B/high-MAE counterexamples against one P&C reserve/capital-return bridge positive, avoiding C22 top-covered symbols and previous R6 loop85 C21 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_RATE_CYCLE_CAPITAL_RETURN_RESERVE_BRIDGE_VS_SMALLCAP_INSURANCE_BETA_MNA_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C22 now has non-top-symbol small-cap/life-insurance beta counterexamples; next R6 loops should exact-URL repair reserve quality, CSM/EV, loss-ratio, capital buffer and capital-return evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","axis":"C22_reserve_capital_return_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"001450 worked with reserve/capital-return bridge proxy; 000400 and 085620 failed when only insurance/M&A/rate beta existed."}
{"row_type":"shadow_weight","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","axis":"C22_insurance_beta_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Small-cap insurance and life-insurance rate beta rows showed low MFE and high/deep MAE without reserve/capital bridge."}
{"row_type":"shadow_weight","round":"R6","loop":"86","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","axis":"C22_late_rebound_not_entry_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If the original insurance beta entry has MFE90<10 and MAE90<=-20 with missing reserve/capital bridge, a later rebound should not retroactively validate Stage2-Actionable/Yellow."}
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
  - insurance_rate_cycle_beta_overcredit
  - reserve_quality_bridge_missing
  - capital_return_bridge_missing
  - smallcap_MNA_beta_local_4B
  - late_rebound_not_entry_validation
new_axis_proposed:
  - C22_reserve_capital_return_bridge_required_shadow_only
  - C22_insurance_beta_local_4B_watch_guard_shadow_only
  - C22_late_rebound_not_entry_validation_guard_shadow_only
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
3. Confirm R6 / L6 / C22 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C22 top-covered symbols
   - previous R6 loop85 C21 symbols listed in the MD
6. If aggregate support remains stable after exact evidence URL repair, consider C22-scoped safe patch candidates:
   - C22_reserve_capital_return_bridge_required
   - C22_insurance_beta_local_4B_watch_guard
   - C22_late_rebound_not_entry_validation_guard
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R6
completed_loop = 86
next_round = R7
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C22_INSURANCE_RATE_CYCLE_RESERVE.
```
