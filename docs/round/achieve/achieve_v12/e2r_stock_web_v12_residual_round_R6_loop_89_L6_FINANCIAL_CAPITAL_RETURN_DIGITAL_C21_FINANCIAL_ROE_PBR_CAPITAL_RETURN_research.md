# E2R Stock-Web v12 Residual Research — R6 Loop 89 / L6 / C21

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R6
loop: 89
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_SMALL_BROKERAGE_THEME_BLOWOFF_DECAY
sector: financial / bank / brokerage / value-up / ROE / PBR / capital return
output_file: e2r_stock_web_v12_residual_round_R6_loop_89_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R5 loop 89`.

```text
scheduled_round = R6
scheduled_loop = 89
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

R6 is restricted to financial / capital-return / digital-financial names.  
C21 is selected because the immediately previous R6 loop used C22 insurance reserve-cycle, while C21 still needs more distinction between true ROE/PBR/capital-return bridge and small brokerage / value-up theme price bursts.

No-Repeat Index snapshot:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
rows = 51
symbols = 19
good/bad Stage2 = 22/11
4B/4C = 7/0
top-covered = 006220, 016360, 071050, 105560, 138040, 139130
```

This loop avoids the C21 top-covered list and the recent R6 loop symbols:

```text
R6 loop87 C21: 006800, 039490, 316140
R6 loop88 C22: 138040, 211050, 244920
```

Selected symbols:

```text
024110, 001510, 001200
```

The selected pocket is:

```text
bank value-up / dividend / capital-return bridge
vs
small brokerage rebound without durable ROE or shareholder-return bridge
vs
small brokerage price-only blowoff with high MFE but missing capital-return bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"024110","company_name":"기업은행","profile_path":"atlas/symbol_profiles/024/024110.json","first_date":"1996-07-01","last_date":"2026-02-20","trading_day_count":7398,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1998-10-27","1998-11-05","2000-02-02","2003-12-24"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"001510","company_name":"SK증권","profile_path":"atlas/symbol_profiles/001/001510.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7752,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["1998-03-28","1999-01-08","1999-08-27","1999-10-21","2018-12-24"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"001200","company_name":"유진투자증권","profile_path":"atlas/symbol_profiles/001/001200.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7746,"corporate_action_candidate_count":7,"corporate_action_candidate_dates":["1999-02-23","1999-03-30","2001-07-02","2005-07-05","2007-05-16","2011-07-18","2014-10-10"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"024110","trigger_type":"Stage2-Actionable-BankValueupDividendCapitalReturnBridge-Positive","entry_date":"2024-01-24","duplicate_status":"new C21 symbol/trigger/date combination outside top-covered and previous R6 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"001510","trigger_type":"Stage2-FalsePositive-SmallBrokerageRebound-NoROECapitalReturnBridge","entry_date":"2024-02-01","duplicate_status":"new C21 symbol/trigger/date combination outside top-covered and previous R6 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"001200","trigger_type":"Stage2-FalsePositive-SmallBrokeragePriceOnlyBlowoff-NoDurableCapitalReturnBridge","entry_date":"2024-02-22","duplicate_status":"new C21 symbol/trigger/date combination outside top-covered and previous R6 loop symbols"}
```

## 4. Research question

C21 is not “금융주가 오른다.”  
The useful signal must prove a bridge from cheap PBR to shareholder economics: sustainable ROE, CET1 or capital buffer, dividend payout, buyback or cancellation visibility, NIM/fee resilience, credit-cost control, earnings durability and capital-allocation policy. A low PBR without those mechanics is like a locked safe with a bargain sticker; it looks cheap, but it does not open.

Residual question:

```text
Can C21 distinguish:
1. bank value-up / dividend / capital-return bridge with MFE90 above 30% and shallow early MAE,
2. small brokerage rebound where ROE, capital buffer and shareholder-return bridge are missing,
3. brokerage price-only blowoff where MFE can be high but deep later MAE proves it should not be counted as capital-return evidence?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C21_R6L89_024110_IBK_BANK_VALUEUP_CAPITAL_RETURN","symbol":"024110","company_name":"기업은행","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_DIVIDEND_CAPITAL_RETURN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-BankValueupDividendCapitalReturnBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_MFE90_ge30_shallow_MAE","current_profile_verdict":"current_profile_correct_if_ROE_PBR_capital_return_bridge_required","price_source":"Songdaiki/stock-web","notes":"Bank value-up / dividend / capital-return proxy produced MFE90 above 30% with shallow MAE. Green still requires exact ROE, capital buffer, payout and buyback/cancellation evidence."}
{"row_type":"case","case_id":"C21_R6L89_001510_SK_SMALL_BROKERAGE_REBOUND","symbol":"001510","company_name":"SK증권","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SMALL_BROKERAGE_REBOUND_WITHOUT_ROE_CAPITAL_RETURN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SmallBrokerageRebound-NoROECapitalReturnBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_small_brokerage_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Small brokerage rebound had low MFE and deep forward MAE without durable ROE, capital buffer, dividend/buyback or earnings-quality bridge."}
{"row_type":"case","case_id":"C21_R6L89_001200_EUGENE_BROKERAGE_PRICE_ONLY_BLOWOFF","symbol":"001200","company_name":"유진투자증권","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SMALL_BROKERAGE_PRICE_ONLY_BLOWOFF_WITHOUT_DURABLE_CAPITAL_RETURN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SmallBrokeragePriceOnlyBlowoff-NoDurableCapitalReturnBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_only_high_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_brokerage_price_blowoff_counted_as_capital_return","price_source":"Songdaiki/stock-web","notes":"Brokerage price-only blowoff produced high local MFE but later deep MAE. Without ROE/capital-return bridge, MFE should not count as positive C21 evidence."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 024110 기업은행 — bank value-up / dividend / capital-return bridge positive

Entry row: `2024-01-24 c=11870`.  
Observed path: early low `2024-01-24 l=11670`, high `2024-03-15 h=16010`, and later sustained path that remained above entry during the selected forward window.

```jsonl
{"row_type":"trigger","trigger_id":"R6L89_C21_024110_20240124_STAGE2_BANK_VALUEUP_CAPITAL_RETURN","case_id":"C21_R6L89_024110_IBK_BANK_VALUEUP_CAPITAL_RETURN","symbol":"024110","company_name":"기업은행","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_DIVIDEND_CAPITAL_RETURN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-BankValueupDividendCapitalReturnBridge-Positive","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":11870.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_bank_valueup_dividend_capital_return_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; bank ROE/PBR, dividend, capital buffer and shareholder-return bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["low_PBR_valueup_proxy","dividend_payout_proxy","capital_buffer_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_CET1_or_capital_buffer_pending","payout_policy_pending","buyback_or_cancellation_pending","credit_cost_resilience_pending"],"stage4b_evidence_fields":["price_extension_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv","profile_path":"atlas/symbol_profiles/024/024110.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.39,"MFE_90D_pct":34.88,"MFE_180D_pct":34.88,"MAE_30D_pct":-1.68,"MAE_90D_pct":-1.68,"MAE_180D_pct":-1.68,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-15","peak_price":16010.0,"max_drawdown_low_date":"2024-01-24","max_drawdown_low":11670.0,"drawdown_after_peak_pct":-18.43,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_ROE_capital_buffer_payout_and_buyback_evidence","four_b_evidence_type":["price_extension_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_MFE90_ge30_shallow_MAE","current_profile_verdict":"current_profile_correct_if_ROE_PBR_capital_return_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"024110_2024-01-24_11870","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C21 can allow Stage2/Yellow when financial strength is tied to sustainable ROE, PBR rerating, capital buffer, dividend and shareholder-return bridge. Green still requires exact source-grade capital-return evidence."}
```

### 6.2 001510 SK증권 — small brokerage rebound without ROE/capital-return bridge

Entry row: `2024-02-01 c=647`.  
Observed path: high `2024-02-21 h=669`, then a long decay to `2024-12-09 l=452`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L89_C21_001510_20240201_STAGE2_FALSE_POSITIVE_SMALL_BROKERAGE_REBOUND","case_id":"C21_R6L89_001510_SK_SMALL_BROKERAGE_REBOUND","symbol":"001510","company_name":"SK증권","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SMALL_BROKERAGE_REBOUND_WITHOUT_ROE_CAPITAL_RETURN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-SmallBrokerageRebound-NoROECapitalReturnBridge","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":647.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_small_brokerage_valueup_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; small brokerage rebound treated as insufficient without sustainable ROE, capital buffer, payout, buyback/cancellation and earnings-quality bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["small_brokerage_rebound","financial_valueup_theme","relative_strength_rebound"],"stage3_evidence_fields":["sustainable_ROE_missing","capital_buffer_missing","shareholder_return_policy_missing","earnings_quality_missing"],"stage4b_evidence_fields":["price_only_local_peak","capital_return_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001510/2024.csv","profile_path":"atlas/symbol_profiles/001/001510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.40,"MFE_90D_pct":3.40,"MFE_180D_pct":3.40,"MAE_30D_pct":-5.87,"MAE_90D_pct":-13.91,"MAE_180D_pct":-22.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":669.0,"max_drawdown_low_date":"2024-10-22","max_drawdown_low":498.0,"drawdown_after_peak_pct":-25.56,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"small_brokerage_rebound_without_ROE_capital_return_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","capital_return_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_small_brokerage_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"001510_2024-02-01_647","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C21 should not promote small brokerage rebounds without sustainable ROE, capital buffer, dividend/buyback and earnings-quality bridge. Low MFE and later MAE expansion force Watch/4B-risk routing."}
```

### 6.3 001200 유진투자증권 — brokerage price-only blowoff without durable capital-return bridge

Entry row: `2024-02-22 c=4365`.  
Observed path: immediate local high `2024-02-22 h=4725`, later price-only blowoff high `2024-06-25 h=6460`, then lows `2024-11-29 l=2630` and `2024-12-09 l=2320`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L89_C21_001200_20240222_STAGE2_FALSE_POSITIVE_BROKERAGE_PRICE_BLOWOFF","case_id":"C21_R6L89_001200_EUGENE_BROKERAGE_PRICE_ONLY_BLOWOFF","symbol":"001200","company_name":"유진투자증권","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SMALL_BROKERAGE_PRICE_ONLY_BLOWOFF_WITHOUT_DURABLE_CAPITAL_RETURN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate;price_only_blowoff_stress_test","trigger_type":"Stage2-FalsePositive-SmallBrokeragePriceOnlyBlowoff-NoDurableCapitalReturnBridge","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":4365.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_brokerage_valueup_price_blowoff_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; brokerage price blowoff treated as insufficient without ROE durability, capital buffer, dividend/buyback, earnings quality and shareholder-return bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["brokerage_valueup_theme","price_momentum_spike"],"stage3_evidence_fields":["ROE_durability_missing","capital_buffer_missing","dividend_buyback_bridge_missing","earnings_quality_missing"],"stage4b_evidence_fields":["price_only_high_MFE","late_rebound_not_capital_return_validation","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001200/2024.csv","profile_path":"atlas/symbol_profiles/001/001200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.45,"MFE_90D_pct":47.99,"MFE_180D_pct":47.99,"MAE_30D_pct":-12.49,"MAE_90D_pct":-12.49,"MAE_180D_pct":-39.75,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-25","peak_price":6460.0,"max_drawdown_low_date":"2024-11-29","max_drawdown_low":2630.0,"drawdown_after_peak_pct":-59.29,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"brokerage_price_only_high_MFE_without_ROE_capital_return_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only_high_MFE","capital_return_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_only_high_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_brokerage_price_blowoff_counted_as_capital_return","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"001200_2024-02-22_4365","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C21 should not count brokerage price-only MFE as capital-return evidence. If ROE durability, capital buffer, payout and buyback/cancellation bridge are missing, high MFE plus deep later MAE remains Watch/4B-risk."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C21_R6L89_024110_IBK_BANK_VALUEUP_CAPITAL_RETURN","trigger_id":"R6L89_C21_024110_20240124_STAGE2_BANK_VALUEUP_CAPITAL_RETURN","symbol":"024110","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C21 requires sustainable ROE, capital buffer, dividend/buyback and earnings-quality bridge rather than low-PBR financial beta alone","raw_component_scores_before":{"ROE_durability_score":13,"PBR_valueup_score":14,"capital_buffer_score":13,"dividend_payout_score":13,"buyback_cancellation_score":8,"credit_cost_control_score":10,"earnings_quality_score":10,"relative_strength_score":12,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"ROE_durability_score":16,"PBR_valueup_score":17,"capital_buffer_score":16,"dividend_payout_score":16,"buyback_cancellation_score":10,"credit_cost_control_score":12,"earnings_quality_score":12,"relative_strength_score":13,"valuation_repricing_score":10,"execution_risk_score":-3,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":89,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Bank value-up and dividend/capital-return bridge plus MFE90 above 30% supports Yellow/Green-candidate watch; exact payout/buyback/capital-buffer evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C21_R6L89_001510_SK_SMALL_BROKERAGE_REBOUND","trigger_id":"R6L89_C21_001510_20240201_STAGE2_FALSE_POSITIVE_SMALL_BROKERAGE_REBOUND","symbol":"001510","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_scope":"current_default_proxy","profile_hypothesis":"small brokerage rebound without ROE and capital-return bridge should be blocked","raw_component_scores_before":{"ROE_durability_score":1,"PBR_valueup_score":4,"capital_buffer_score":0,"dividend_payout_score":0,"buyback_cancellation_score":0,"credit_cost_control_score":1,"earnings_quality_score":1,"relative_strength_score":7,"valuation_repricing_score":3,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"ROE_durability_score":0,"PBR_valueup_score":1,"capital_buffer_score":0,"dividend_payout_score":0,"buyback_cancellation_score":0,"credit_cost_control_score":0,"earnings_quality_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and later MAE expansion convert small brokerage rebound into missing ROE/capital-return bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C21_R6L89_001200_EUGENE_BROKERAGE_PRICE_ONLY_BLOWOFF","trigger_id":"R6L89_C21_001200_20240222_STAGE2_FALSE_POSITIVE_BROKERAGE_PRICE_BLOWOFF","symbol":"001200","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_scope":"current_default_proxy","profile_hypothesis":"price-only brokerage blowoff should be 4B-watch even when local MFE is high if capital-return bridge is missing","raw_component_scores_before":{"ROE_durability_score":1,"PBR_valueup_score":5,"capital_buffer_score":0,"dividend_payout_score":0,"buyback_cancellation_score":0,"credit_cost_control_score":1,"earnings_quality_score":1,"relative_strength_score":15,"valuation_repricing_score":6,"execution_risk_score":-16,"theme_spike_risk":-22,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"ROE_durability_score":0,"PBR_valueup_score":1,"capital_buffer_score":0,"dividend_payout_score":0,"buyback_cancellation_score":0,"credit_cost_control_score":0,"earnings_quality_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"High MFE is price-only; deep later MAE and missing ROE/capital-return bridge block Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R6L89_C21_P0_CURRENT","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C21 needs explicit ROE, capital buffer, payout, buyback/cancellation, earnings quality and price-only brokerage blowoff taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":28.76,"avg_MAE90_pct":-9.36,"avg_MFE180_pct":28.76,"avg_MAE180_pct":-21.33,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.67,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C21_ROE_capital_return_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R6L89_C21_P1_SECTOR_SPECIFIC","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P1_L6_financial_ROE_capital_return_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L6 financial signals need sustainable ROE, capital buffer, dividend payout, buyback/cancellation, credit-cost control or earnings durability before Stage2-Actionable","changed_axes":["ROE_durability_required","capital_return_required","small_brokerage_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_ROE_capital_buffer_dividend_buyback_credit_cost_or_earnings_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":28.76,"avg_MAE90_pct":-9.36,"avg_MFE180_pct":28.76,"avg_MAE180_pct":-21.33,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R6L89_C21_P2_CANONICAL","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P2_C21_ROE_capital_return_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C21 should reward ROE/PBR-to-shareholder-return mechanics, not small brokerage price labels","changed_axes":["C21_ROE_capital_return_bridge_required","C21_small_brokerage_local_4B_guard","C21_price_only_MFE_not_capital_return_proof_guard"],"changed_thresholds":{"stage2_yellow_gate":"ROE_or_capital_buffer_plus_dividend_or_buyback_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":28.76,"avg_MAE90_pct":-9.36,"avg_MFE180_pct":28.76,"avg_MAE180_pct":-21.33,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R6L89_C21_P3_COUNTEREXAMPLE_GUARD","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P3_C21_price_only_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If ROE/capital-return bridge is missing, high MFE cannot validate a brokerage theme row when MAE180<=-30; if MFE90<5 and MAE180<=-20, hard-block Yellow/Green","changed_axes":["C21_price_only_MFE_guardrail","C21_low_MFE_MAE_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_MAE180_le_minus_30; hard_block_if_MFE90_lt_5_and_MAE180_le_minus_20"},"eligible_trigger_count":3,"avg_MFE90_pct":28.76,"avg_MAE90_pct":-9.36,"avg_MFE180_pct":28.76,"avg_MAE180_pct":-21.33,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_BANK_VALUEUP_POSITIVE_VS_SMALL_BROKERAGE_BLOWOFF_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":28.76,"avg_MAE90_pct":-9.36,"avg_MFE180_pct":28.76,"avg_MAE180_pct":-21.33,"stage2_hit_rate_MFE90_ge_20":0.67,"stage2_bad_entry_rate_bridge_missing":0.67,"price_only_high_MFE_high_MAE_count":1,"interpretation":"C21 needs bridge discipline. 기업은행 shows bank value-up/dividend/capital-return bridge can support Yellow-watch, while SK증권 and 유진투자증권 show small brokerage rebound or price-only MFE should not be promoted without sustainable ROE, capital buffer, payout, buyback/cancellation and earnings-quality evidence."}
{"row_type":"stage_transition_summary","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"024110","trigger_type":"Stage2-Actionable-BankValueupDividendCapitalReturnBridge-Positive","entry_date":"2024-01-24","stage2_to_90D_outcome":"good_stage2_MFE90_ge30_shallow_MAE","stage2_to_180D_outcome":"positive_bank_capital_return_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when ROE/PBR rerating is tied to capital buffer, dividend, buyback/cancellation and earnings-quality bridge; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"001510","trigger_type":"Stage2-FalsePositive-SmallBrokerageRebound-NoROECapitalReturnBridge","entry_date":"2024-02-01","stage2_to_90D_outcome":"weak_stage2_low_MFE","stage2_to_180D_outcome":"failed_small_brokerage_rebound_MAE_expansion","MFE90_ge_20":false,"MAE180_le_minus_20":true,"transition_note":"Small brokerage rebound without ROE/capital-return bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"001200","trigger_type":"Stage2-FalsePositive-SmallBrokeragePriceOnlyBlowoff-NoDurableCapitalReturnBridge","entry_date":"2024-02-22","stage2_to_90D_outcome":"price_only_high_MFE_without_bridge","stage2_to_180D_outcome":"failed_brokerage_blowoff_deep_MAE","MFE90_ge_20":true,"MAE180_le_minus_30":true,"transition_note":"Brokerage price-only MFE without ROE/capital-return bridge should be treated as 4B-watch, not positive evidence."}
{"row_type":"residual_contribution","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","residual_type":"small_brokerage_valueup_theme_overcredit_without_ROE_capital_return_bridge","contribution":"Adds two C21 4B counterexamples against one bank capital-return positive, including one high-MFE price-only blowoff case, avoiding C21 top-covered and previous R6 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_SMALL_BROKERAGE_THEME_BLOWOFF_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C21 now has non-top-symbol bank value-up positive and two small-brokerage weak-bridge counterexamples; next R6 loops should exact-URL repair ROE durability, capital buffer, dividend payout, buyback/cancellation, credit-cost control and earnings-quality evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","axis":"C21_ROE_capital_return_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"024110 worked when bank value-up/dividend/capital-return proxy was present; 001510 and 001200 lacked durable ROE and shareholder-return evidence."}
{"row_type":"shadow_weight","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","axis":"C21_small_brokerage_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Small brokerage rows either showed low MFE or price-only high MFE followed by deep MAE when capital-return bridge was missing."}
{"row_type":"shadow_weight","round":"R6","loop":"89","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","axis":"C21_price_only_MFE_not_capital_return_proof_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"001200 shows that MFE90>=20 should not count as C21 positive evidence when ROE/capital-return bridge is missing and MAE180<=-30."}
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
  - small_brokerage_valueup_theme_overcredit
  - price_only_financial_MFE_overcredit
  - ROE_durability_bridge_missing
  - capital_return_payout_buyback_bridge_missing
new_axis_proposed:
  - C21_ROE_capital_return_bridge_required_shadow_only
  - C21_small_brokerage_local_4B_watch_guard_shadow_only
  - C21_price_only_MFE_not_capital_return_proof_guard_shadow_only
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
3. Confirm R6 / L6 / C21 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C21 top-covered symbols
   - previous R6 loop87 C21 symbols
   - previous R6 loop88 C22 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C21-scoped safe patch candidates:
   - C21_ROE_capital_return_bridge_required
   - C21_small_brokerage_local_4B_watch_guard
   - C21_price_only_MFE_not_capital_return_proof_guard
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R6
completed_loop = 89
next_round = R7
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.
```
