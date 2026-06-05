# E2R Stock-Web v12 Residual Research — R6 Loop 91 / L6 / C21

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R6
loop: 91
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: SECURITIES_DIVIDEND_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_SMALL_BROKERAGE_PBR_VOCABULARY_DECAY
sector: financial / brokerage / ROE / PBR / value-up / dividend / capital return / governance
output_file: e2r_stock_web_v12_residual_round_R6_loop_91_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R5 loop 91`.

```text
scheduled_round = R6
scheduled_loop = 91
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

R6 is restricted to financial / capital return / digital-financial names.  
C21 is selected because R6 loop90 used C22 insurance reserve/rate cycle, and the R6 lane rotates back to financial ROE/PBR/capital-return.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
rows = 51
symbols = 19
good/bad Stage2 = 22/11
4B/4C = 7/0
top-covered = 006220, 016360, 071050, 105560, 138040, 139130
```

This loop avoids the C21 top-covered list and recent R6 loop symbols:

```text
R6 loop87 C21: 006800, 039490, 316140
R6 loop88 C22: 138040, 211050, 244920
R6 loop89 C21: 024110, 001510, 001200
R6 loop90 C22: 032830, 088350, 000400
```

Candidate hygiene note:

```text
During this execution path, R5/C20 and earlier R2/R3/R4 candidate rows were touched in the surrounding tool calls.
Those rows are not used in this R6/C21 output.
```

Selected symbols:

```text
005940, 030610, 001290
```

The selected pocket is:

```text
large brokerage dividend / value-up / shareholder-return bridge
vs
small brokerage PBR/value-up vocabulary without explicit payout or ROE bridge
vs
turnaround brokerage/financial vocabulary without capital-quality or shareholder-return bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"005940","company_name":"NH투자증권","profile_path":"atlas/symbol_profiles/005/005940.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7765,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["1999-04-14","1999-11-01","2000-01-31","2011-12-08","2015-01-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical name-transition/corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"030610","company_name":"교보증권","profile_path":"atlas/symbol_profiles/030/030610.json","first_date":"1999-11-18","last_date":"2026-02-20","trading_day_count":6471,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2020-07-09","2023-09-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"001290","company_name":"상상인증권","profile_path":"atlas/symbol_profiles/001/001290.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7280,"corporate_action_candidate_count":13,"corporate_action_candidate_dates":["2000-02-08","2000-08-07","2002-02-20","2003-08-19","2004-05-28","2004-06-17","2004-08-24","2005-12-23","2013-05-20","2013-06-07","2014-01-20","2018-02-20","2019-04-09"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"005940","trigger_type":"Stage2-Actionable-LargeBrokerageDividendValueupCapitalReturnBridge-Positive","entry_date":"2024-01-29","duplicate_status":"new C21 symbol/trigger/date combination outside top-covered and recent R6 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"030610","trigger_type":"Stage2-FalsePositive-SmallBrokeragePBRValueupVocabularyNoExplicitPayoutROEBridge","entry_date":"2024-02-19","duplicate_status":"new C21 symbol/trigger/date combination outside top-covered and recent R6 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"001290","trigger_type":"Stage2-FalsePositive-TurnaroundBrokerageVocabularyNoCapitalQualityReturnBridge","entry_date":"2024-02-15","duplicate_status":"new C21 symbol/trigger/date combination outside top-covered and recent R6 loop symbols"}
```

## 4. Research question

C21 is not “저PBR 금융주가 움직였다.”  
The useful financial value-up signal must prove the bridge from valuation gap to shareholder economics:

```text
ROE durability
PBR discount closure path
dividend payout visibility
buyback or cancellation mechanism
capital buffer / CET1 or NCR
earnings quality
loss-absorption capacity
regulatory and board approval path
cash-return discipline
```

A PBR headline without that bridge is a bank vault with the door painted gold. The balance sheet may look cheap, but the shareholder only receives value when capital can be released safely and repeatedly.

Residual question:

```text
Can C21 distinguish:
1. large brokerage dividend/value-up bridge with high MFE and shallow early MAE,
2. small brokerage PBR/value-up vocabulary where MFE is weak without explicit payout/ROE bridge,
3. turnaround brokerage vocabulary where weak capital quality and no shareholder-return mechanism produce deep MAE?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C21_R6L91_005940_NH_BROKERAGE_CAPITAL_RETURN","symbol":"005940","company_name":"NH투자증권","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LARGE_BROKERAGE_DIVIDEND_VALUEUP_CAPITAL_RETURN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-LargeBrokerageDividendValueupCapitalReturnBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE90_low_entry_MAE_late_repricing_watch","current_profile_verdict":"current_profile_correct_if_ROE_payout_buyback_capital_buffer_bridge_required","price_source":"Songdaiki/stock-web","notes":"Large brokerage value-up/dividend proxy produced high MFE and shallow entry MAE. Green still requires exact payout, buyback/cancellation, capital buffer and ROE evidence."}
{"row_type":"case","case_id":"C21_R6L91_030610_KYOBO_SMALL_BROKERAGE_VALUEUP","symbol":"030610","company_name":"교보증권","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SMALL_BROKERAGE_PBR_VALUEUP_VOCABULARY_WITHOUT_EXPLICIT_PAYOUT_ROE_BRIDGE","case_type":"weak_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SmallBrokeragePBRValueupVocabularyNoExplicitPayoutROEBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_moderate_MAE_no_explicit_payout_bridge","current_profile_verdict":"current_profile_false_positive_if_small_brokerage_PBR_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Small brokerage value-up/PBR vocabulary after an initial spike had near-zero forward MFE and moderate drawdown without exact payout, buyback, ROE or capital-buffer evidence."}
{"row_type":"case","case_id":"C21_R6L91_001290_SANGSANGIN_TURNAROUND_BROKERAGE","symbol":"001290","company_name":"상상인증권","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"TURNAROUND_BROKERAGE_VOCABULARY_WITHOUT_CAPITAL_QUALITY_RETURN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-TurnaroundBrokerageVocabularyNoCapitalQualityReturnBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_extreme_MAE_no_capital_return_bridge","current_profile_verdict":"current_profile_false_positive_if_turnaround_brokerage_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Turnaround brokerage vocabulary had only low MFE and then extreme MAE without capital quality, shareholder-return mechanism, ROE durability or loss-absorption bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 005940 NH투자증권 — large brokerage dividend / value-up / capital-return bridge

Entry row: `2024-01-29 c=10430`.  
Observed path: same-day low `2024-01-29 l=10210`, 90D value-up peak `2024-03-14 h=13100`, and later full-window peak `2024-12-03 h=14530`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L91_C21_005940_20240129_STAGE2_BROKERAGE_CAPITAL_RETURN","case_id":"C21_R6L91_005940_NH_BROKERAGE_CAPITAL_RETURN","symbol":"005940","company_name":"NH투자증권","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LARGE_BROKERAGE_DIVIDEND_VALUEUP_CAPITAL_RETURN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-LargeBrokerageDividendValueupCapitalReturnBridge-Positive","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":10430.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_brokerage_valueup_dividend_capital_return_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; brokerage dividend/value-up, payout and capital-return bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["dividend_payout_proxy","valueup_PBR_discount_proxy","brokerage_ROE_recovery_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_payout_policy_pending","buyback_or_cancellation_pending","capital_buffer_source_pending","ROE_durability_pending"],"stage4b_evidence_fields":["price_extension_watch","late_repricing_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005940/2024.csv","profile_path":"atlas/symbol_profiles/005/005940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.33,"MFE_90D_pct":25.60,"MFE_180D_pct":39.31,"MAE_30D_pct":-2.11,"MAE_90D_pct":-2.11,"MAE_180D_pct":-2.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":14530.0,"max_drawdown_low_date":"2024-01-29","max_drawdown_low":10210.0,"drawdown_after_peak_pct":-9.58,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.90,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_payout_buyback_capital_buffer_ROE_evidence","four_b_evidence_type":["price_extension_watch","late_repricing_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE90_low_entry_MAE_late_repricing_watch","current_profile_verdict":"current_profile_correct_if_ROE_payout_buyback_capital_buffer_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"005940_2024-01-29_10430","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C21 can allow Stage2/Yellow when financial strength is tied to ROE durability, payout visibility, buyback/cancellation potential, capital buffer and cash-return discipline. Green still requires exact source-grade evidence."}
```

### 6.2 030610 교보증권 — small brokerage PBR/value-up vocabulary without explicit payout/ROE bridge

Entry row: `2024-02-19 c=5640`, after the initial small-brokerage value-up spike.  
Observed path: next-day high `2024-02-20 h=5720`, then drawdown to `2024-04-16 l=4775`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L91_C21_030610_20240219_STAGE2_FALSE_POSITIVE_SMALL_BROKERAGE_VALUEUP","case_id":"C21_R6L91_030610_KYOBO_SMALL_BROKERAGE_VALUEUP","symbol":"030610","company_name":"교보증권","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SMALL_BROKERAGE_PBR_VALUEUP_VOCABULARY_WITHOUT_EXPLICIT_PAYOUT_ROE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-SmallBrokeragePBRValueupVocabularyNoExplicitPayoutROEBridge","trigger_date":"2024-02-19","entry_date":"2024-02-19","entry_price":5640.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_small_brokerage_valueup_PBR_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; small brokerage PBR/value-up vocabulary treated as insufficient without explicit payout policy, buyback/cancellation, ROE durability and capital buffer","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["small_brokerage_valueup_keyword","PBR_discount_vocabulary","relative_strength_spike"],"stage3_evidence_fields":["explicit_payout_missing","buyback_cancellation_missing","ROE_durability_missing","capital_buffer_missing"],"stage4b_evidence_fields":["near_zero_MFE","payout_ROE_bridge_missing_watch","moderate_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/030/030610/2024.csv","profile_path":"atlas/symbol_profiles/030/030610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.42,"MFE_90D_pct":1.42,"MFE_180D_pct":1.60,"MAE_30D_pct":-7.98,"MAE_90D_pct":-15.34,"MAE_180D_pct":-15.34,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-20","peak_price":5760.0,"max_drawdown_low_date":"2024-04-16","max_drawdown_low":4775.0,"drawdown_after_peak_pct":-17.10,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.89,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"small_brokerage_PBR_valueup_vocabulary_without_explicit_payout_ROE_capital_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["near_zero_MFE","payout_ROE_bridge_missing_watch","moderate_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_moderate_MAE_no_explicit_payout_bridge","current_profile_verdict":"current_profile_false_positive_if_small_brokerage_PBR_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"030610_2024-02-19_5640","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C21 should not promote small brokerage value-up vocabulary unless explicit payout, buyback/cancellation, ROE durability and capital-buffer evidence are repaired. Near-zero MFE requires Watch/4B routing."}
```

### 6.3 001290 상상인증권 — turnaround brokerage vocabulary without capital-quality / return bridge

Entry row: `2024-02-15 c=800`, on a small-financial rebound.  
Observed path: high `2024-02-21 h=850`, then long decline to `2024-12-09 l=401`.

```jsonl
{"row_type":"trigger","trigger_id":"R6L91_C21_001290_20240215_STAGE2_FALSE_POSITIVE_TURNAROUND_BROKERAGE","case_id":"C21_R6L91_001290_SANGSANGIN_TURNAROUND_BROKERAGE","symbol":"001290","company_name":"상상인증권","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"TURNAROUND_BROKERAGE_VOCABULARY_WITHOUT_CAPITAL_QUALITY_RETURN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;capital_quality_4B_stress_test","trigger_type":"Stage2-FalsePositive-TurnaroundBrokerageVocabularyNoCapitalQualityReturnBridge","trigger_date":"2024-02-15","entry_date":"2024-02-15","entry_price":800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_turnaround_brokerage_financial_valueup_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; turnaround brokerage/financial vocabulary treated as insufficient without capital quality, ROE durability, loss cleanup, payout and cash-return bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["turnaround_brokerage_keyword","financial_valueup_vocabulary","relative_strength_rebound"],"stage3_evidence_fields":["capital_quality_missing","ROE_durability_missing","loss_cleanup_missing","shareholder_return_mechanism_missing"],"stage4b_evidence_fields":["low_MFE","capital_quality_bridge_missing_watch","extreme_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001290/2024.csv","profile_path":"atlas/symbol_profiles/001/001290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.25,"MFE_90D_pct":6.25,"MFE_180D_pct":6.25,"MAE_30D_pct":-6.75,"MAE_90D_pct":-20.88,"MAE_180D_pct":-49.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":850.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":401.0,"drawdown_after_peak_pct":-52.82,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"turnaround_brokerage_vocabulary_without_capital_quality_ROE_shareholder_return_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","capital_quality_bridge_missing_watch","extreme_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_extreme_MAE_no_capital_return_bridge","current_profile_verdict":"current_profile_false_positive_if_turnaround_brokerage_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"001290_2024-02-15_800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C21 should not count small brokerage turnaround vocabulary as capital-return evidence. Capital quality, ROE durability, loss cleanup, payout and buyback/cancellation bridge must be exact-repaired before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C21_R6L91_005940_NH_BROKERAGE_CAPITAL_RETURN","trigger_id":"R6L91_C21_005940_20240129_STAGE2_BROKERAGE_CAPITAL_RETURN","symbol":"005940","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C21 requires ROE durability, payout visibility, buyback/cancellation, capital buffer and shareholder-return discipline rather than low-PBR vocabulary alone","raw_component_scores_before":{"ROE_durability_score":12,"PBR_discount_closure_score":12,"dividend_payout_score":13,"buyback_cancellation_score":8,"capital_buffer_score":11,"earnings_quality_score":10,"regulatory_board_path_score":8,"cash_return_score":10,"relative_strength_score":14,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"ROE_durability_score":15,"PBR_discount_closure_score":15,"dividend_payout_score":16,"buyback_cancellation_score":10,"capital_buffer_score":13,"earnings_quality_score":12,"regulatory_board_path_score":10,"cash_return_score":12,"relative_strength_score":15,"valuation_repricing_score":10,"execution_risk_score":-3,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Dividend/value-up/capital-return bridge plus MFE90>20 and low MAE supports Yellow/Green-candidate watch; exact payout/buyback/capital evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C21_R6L91_030610_KYOBO_SMALL_BROKERAGE_VALUEUP","trigger_id":"R6L91_C21_030610_20240219_STAGE2_FALSE_POSITIVE_SMALL_BROKERAGE_VALUEUP","symbol":"030610","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_scope":"current_default_proxy","profile_hypothesis":"small brokerage value-up vocabulary without explicit payout and ROE bridge should be blocked","raw_component_scores_before":{"ROE_durability_score":2,"PBR_discount_closure_score":3,"dividend_payout_score":1,"buyback_cancellation_score":0,"capital_buffer_score":1,"earnings_quality_score":1,"regulatory_board_path_score":0,"cash_return_score":0,"relative_strength_score":5,"valuation_repricing_score":3,"execution_risk_score":-10,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"ROE_durability_score":0,"PBR_discount_closure_score":1,"dividend_payout_score":0,"buyback_cancellation_score":0,"capital_buffer_score":0,"earnings_quality_score":0,"regulatory_board_path_score":0,"cash_return_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and no explicit payout/ROE bridge keep the row in Watch/4B despite financial value-up vocabulary."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C21_R6L91_001290_SANGSANGIN_TURNAROUND_BROKERAGE","trigger_id":"R6L91_C21_001290_20240215_STAGE2_FALSE_POSITIVE_TURNAROUND_BROKERAGE","symbol":"001290","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_scope":"current_default_proxy","profile_hypothesis":"turnaround brokerage vocabulary without capital quality and return mechanism should remain Watch/4B","raw_component_scores_before":{"ROE_durability_score":0,"PBR_discount_closure_score":2,"dividend_payout_score":0,"buyback_cancellation_score":0,"capital_buffer_score":0,"earnings_quality_score":0,"regulatory_board_path_score":0,"cash_return_score":0,"relative_strength_score":6,"valuation_repricing_score":2,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"ROE_durability_score":0,"PBR_discount_closure_score":0,"dividend_payout_score":0,"buyback_cancellation_score":0,"capital_buffer_score":0,"earnings_quality_score":0,"regulatory_board_path_score":0,"cash_return_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-28,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and extreme MAE require capital quality, loss cleanup, ROE and cash-return evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R6L91_C21_P0_CURRENT","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C21 needs explicit ROE durability, payout, buyback/cancellation, capital buffer, earnings quality and small-brokerage vocabulary 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":11.09,"avg_MAE90_pct":-12.78,"avg_MFE180_pct":15.72,"avg_MAE180_pct":-22.44,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.93,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C21_ROE_payout_capital_return_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R6L91_C21_P1_SECTOR_SPECIFIC","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P1_L6_financial_capital_return_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L6 financial value-up signals need ROE durability, payout visibility, buyback/cancellation, capital buffer, earnings quality or cash return before Stage2-Actionable","changed_axes":["ROE_durability_required","payout_buyback_required","capital_quality_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_ROE_payout_buyback_capital_buffer_earnings_quality_or_cash_return_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":11.09,"avg_MAE90_pct":-12.78,"avg_MFE180_pct":15.72,"avg_MAE180_pct":-22.44,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R6L91_C21_P2_CANONICAL","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P2_C21_ROE_payout_capital_return_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C21 should reward capital-return mechanics, not low-PBR or brokerage vocabulary","changed_axes":["C21_ROE_payout_buyback_capital_buffer_bridge_required","C21_small_brokerage_turnaround_local_4B_guard","C21_low_MFE_no_return_mechanism_guard"],"changed_thresholds":{"stage2_yellow_gate":"ROE_durability_or_payout_plus_capital_buffer_or_buyback_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":11.09,"avg_MAE90_pct":-12.78,"avg_MFE180_pct":15.72,"avg_MAE180_pct":-22.44,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R6L91_C21_P3_COUNTEREXAMPLE_GUARD","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P3_C21_low_MFE_capital_quality_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If ROE/payout/capital-return bridge is missing, MFE90<10 or MAE180<=-20 should block Yellow/Green and route to 4B-watch","changed_axes":["C21_low_MFE_guardrail","C21_capital_quality_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_10_or_MAE180_le_minus_20)"},"eligible_trigger_count":3,"avg_MFE90_pct":11.09,"avg_MAE90_pct":-12.78,"avg_MFE180_pct":15.72,"avg_MAE180_pct":-22.44,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"C21_LARGE_BROKERAGE_POSITIVE_VS_SMALL_BROKERAGE_VALUEUP_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":11.09,"avg_MAE90_pct":-12.78,"avg_MFE180_pct":15.72,"avg_MAE180_pct":-22.44,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MFE90_lt10":0.67,"interpretation":"C21 needs bridge discipline. NH투자증권 shows large-brokerage dividend/value-up/capital-return bridge can support Yellow/Green-candidate-watch, while 교보증권 and 상상인증권 show brokerage/PBR/turnaround vocabulary should not be promoted without explicit payout, buyback/cancellation, ROE durability, capital quality and cash-return evidence."}
{"row_type":"stage_transition_summary","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"005940","trigger_type":"Stage2-Actionable-LargeBrokerageDividendValueupCapitalReturnBridge-Positive","entry_date":"2024-01-29","stage2_to_90D_outcome":"good_stage2_high_MFE90_low_MAE","stage2_to_180D_outcome":"positive_capital_return_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when financial strength is tied to ROE durability, payout, buyback/cancellation, capital buffer and cash-return bridge; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"030610","trigger_type":"Stage2-FalsePositive-SmallBrokeragePBRValueupVocabularyNoExplicitPayoutROEBridge","entry_date":"2024-02-19","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_bridge_missing","stage2_to_180D_outcome":"weak_small_brokerage_valueup_vocabulary_moderate_MAE","MFE90_ge20":false,"MFE90_lt10":true,"transition_note":"Small brokerage PBR/value-up vocabulary without explicit payout/ROE bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"001290","trigger_type":"Stage2-FalsePositive-TurnaroundBrokerageVocabularyNoCapitalQualityReturnBridge","entry_date":"2024-02-15","stage2_to_90D_outcome":"bad_stage2_low_MFE_capital_quality_missing","stage2_to_180D_outcome":"failed_turnaround_brokerage_extreme_MAE","MFE90_ge20":false,"MAE180_le_minus20":true,"transition_note":"Turnaround brokerage vocabulary without capital quality, ROE durability and shareholder-return bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","residual_type":"small_brokerage_PBR_valueup_vocabulary_overcredit_without_ROE_payout_capital_return_bridge","contribution":"Adds two C21 4B counterexamples against one large-brokerage capital-return positive, avoiding C21 top-covered and recent R6 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SECURITIES_DIVIDEND_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_SMALL_BROKERAGE_PBR_VOCABULARY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C21 now has non-top-symbol large-brokerage capital-return positive and two small-brokerage weak-bridge counterexamples; next R6 C21 loops should exact-URL repair ROE durability, payout policy, buyback/cancellation, capital buffer, earnings quality and cash-return evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","axis":"C21_ROE_payout_buyback_capital_buffer_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"005940 worked when brokerage dividend/value-up/capital-return proxy existed; 030610 and 001290 failed when financial vocabulary lacked explicit payout, ROE durability and capital-return mechanism."}
{"row_type":"shadow_weight","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","axis":"C21_small_brokerage_turnaround_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Small brokerage and turnaround brokerage rows showed low or near-zero MFE and drawdown when capital-return evidence was missing."}
{"row_type":"shadow_weight","round":"R6","loop":"91","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","axis":"C21_low_MFE_no_return_mechanism_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"030610 shows low MFE cannot be accepted as PBR discount closure without exact payout/ROE bridge; 001290 confirms the capital-quality failure mode."}
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
  - small_brokerage_valueup_vocabulary_overcredit
  - turnaround_brokerage_vocabulary_overcredit
  - explicit_payout_bridge_missing
  - ROE_capital_quality_bridge_missing
  - shareholder_return_cash_bridge_missing
new_axis_proposed:
  - C21_ROE_payout_buyback_capital_buffer_bridge_required_shadow_only
  - C21_small_brokerage_turnaround_local_4B_guard_shadow_only
  - C21_low_MFE_no_return_mechanism_guard_shadow_only
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
All three selected symbols have corporate-action or name-transition candidates before 2024; those candidates are outside the selected 2024 windows and do not contaminate this residual price-path analysis.  
`001290` has many older corporate-action/name-transition candidates, so production patching should require exact price-path and evidence repair.  
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
3. Confirm R6 / L6 / C21 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C21 top-covered symbols
   - previous R6 loop87 C21 symbols
   - previous R6 loop88 C22 symbols
   - previous R6 loop89 C21 symbols
   - previous R6 loop90 C22 symbols
6. Confirm accidentally touched R5/C20 and earlier R2/R3/R4 candidate rows are not ingested from this MD.
7. Keep 001290 in price-path/evidence repair watch before patch consideration.
8. If aggregate support remains stable after exact evidence URL repair, consider C21-scoped safe patch candidates:
   - C21_ROE_payout_buyback_capital_buffer_bridge_required
   - C21_small_brokerage_turnaround_local_4B_guard
   - C21_low_MFE_no_return_mechanism_guard
9. Do not loosen Stage3-Green.
10. Do not use future MFE/MAE in runtime scoring.
11. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R6
completed_loop = 91
next_round = R7
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.
```
