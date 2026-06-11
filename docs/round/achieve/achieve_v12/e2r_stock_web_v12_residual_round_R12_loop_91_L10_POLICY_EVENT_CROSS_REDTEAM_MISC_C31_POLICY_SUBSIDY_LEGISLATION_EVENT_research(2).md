# E2R Stock-Web v12 Residual Research — R12 Loop 91 / L10 / C31

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R12
loop: 91
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: VALUEUP_CAPITAL_RETURN_POLICY_TO_CASH_BRIDGE_VS_CASINO_LOW_BIRTH_POLICY_VOCABULARY_DECAY
sector: policy / subsidy / legislation / value-up / tourism-casino policy / low-birth policy / policy-to-cash bridge
output_file: e2r_stock_web_v12_residual_round_R12_loop_91_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R11 loop 91`.

```text
scheduled_round = R12
scheduled_loop = 91
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

R12 is restricted to policy / event / cross-redteam / misc.
C31 is selected because the immediately previous R12 loop used C32 governance/control-premium, so the R12 lane rotates back into policy/subsidy/legislation-event residuals.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
rows = 97
symbols = 70
good/bad Stage2 = 35/25
4B/4C = 5/0
top-covered = 013990, 003550, 015760, 032350, 114090, 000270
```

This loop avoids the C31 top-covered list and recent R12 loop symbols:

```text
R12 loop85 C31: 055550, 034730, 004020
R12 loop86 C32: 028260, 001040, 004990
R12 loop87 C31: 036460, 004090, 024060
R12 loop88 C32: 000240, 001230, 004800
R12 loop89 C31: 071320, 035250, 039130
R12 loop90 C32: 008930, 006840, 003030
```

Candidate hygiene note:

```text
During this execution path, R11/C04 and stale R10/C30 candidate rows were touched in surrounding tool calls.
Those rows are not used in this R12/C31 output.
```

Selected symbols:

```text
086790, 034230, 068290
```

The selected pocket is:

```text
corporate value-up policy to capital-return bridge
vs
casino/tourism policy vocabulary without fresh policy-to-cash and market-segment-change repair
vs
low-birth/childcare policy vocabulary price spike without revenue/cash conversion bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"086790","company_name":"하나금융지주","profile_path":"atlas/symbol_profiles/086/086790.json","first_date":"2005-12-12","last_date":"2026-02-20","trading_day_count":4980,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"034230","company_name":"파라다이스","profile_path":"atlas/symbol_profiles/034/034230.json","first_date":"2002-11-05","last_date":"2026-02-20","trading_day_count":5749,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"Market moved from KOSDAQ to KOSPI on 2024-06-24, after selected entry; retain market-segment-change watch before production patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry; market_segment_change_watch"}
{"row_type":"price_source_validation","symbol":"068290","company_name":"삼성출판사","profile_path":"atlas/symbol_profiles/068/068290.json","first_date":"2002-08-05","last_date":"2026-02-20","trading_day_count":5777,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2008-06-05"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"086790","trigger_type":"Stage2-Actionable-ValueupCapitalReturnPolicyToCashBridge-Positive","entry_date":"2024-01-29","duplicate_status":"new C31 symbol/trigger/date combination outside C31 top-covered and previous R12 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"034230","trigger_type":"Stage2-FalsePositive-CasinoTourismPolicyVocabularyNoFreshPolicyToCashBridge","entry_date":"2024-04-01","duplicate_status":"new C31 symbol/trigger/date combination outside C31 top-covered and previous R12 loop symbols; market-segment-change watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"068290","trigger_type":"Stage2-FalsePositive-LowBirthChildcarePolicyVocabularyNoRevenueCashBridge","entry_date":"2024-01-10","duplicate_status":"new C31 symbol/trigger/date combination outside C31 top-covered and previous R12 loop symbols; same policy family as low-birth basket but different symbol/failure mode from top-covered 013990"}
```

## 4. Research question

C31 is not “정책 단어가 붙었다.”
The useful policy/subsidy/legislation-event signal must prove a policy-to-cash bridge:

```text
named policy or legislation
implementation timetable
eligible recipient or asset owner
board / regulatory / ministry execution path
subsidy or capital-return mechanism
volume / traffic / revenue channel
margin bridge
working-capital discipline
cash conversion
```

A policy headline without this bridge is a government stamp still drying on the paper. The market can cheer the ink, but the company only changes when the policy enters contracts, prices, volume, payout, margin, or cash.

Residual question:

```text
Can C31 distinguish:
1. value-up policy plus concrete capital-return bridge with high MFE and shallow MAE,
2. casino/tourism policy vocabulary where no fresh traffic, tax/regulation, margin or cash bridge repairs the entry,
3. low-birth/childcare policy vocabulary where price MFE exists but no policy-to-revenue/cash bridge follows?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C31_R12L91_086790_HANA_VALUEUP_CAPITAL_RETURN","symbol":"086790","company_name":"하나금융지주","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_POLICY_TO_CAPITAL_RETURN_CASH_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-ValueupCapitalReturnPolicyToCashBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE90_low_MAE_policy_to_cash_bridge","current_profile_verdict":"current_profile_correct_if_policy_timetable_payout_capital_return_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Corporate value-up policy plus payout/capital-return proxy produced high MFE and shallow entry MAE. Green still requires exact board policy, payout/buyback/cancellation, capital buffer and cash-return evidence."}
{"row_type":"case","case_id":"C31_R12L91_034230_PARADISE_CASINO_TOURISM_POLICY","symbol":"034230","company_name":"파라다이스","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CASINO_TOURISM_POLICY_VOCABULARY_WITHOUT_FRESH_TRAFFIC_MARGIN_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CasinoTourismPolicyVocabularyNoFreshPolicyToCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.95,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_market_segment_watch","current_profile_verdict":"current_profile_false_positive_if_tourism_casino_policy_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Casino/tourism policy vocabulary after the first rebound had near-zero MFE and deep MAE without fresh VIP traffic, regulation/tax change, margin or cash bridge. KOSDAQ-to-KOSPI transfer requires data-quality watch."}
{"row_type":"case","case_id":"C31_R12L91_068290_SAMSUNG_PUBLISHING_LOWBIRTH_POLICY","symbol":"068290","company_name":"삼성출판사","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"LOW_BIRTH_CHILDCARE_POLICY_VOCABULARY_WITHOUT_REVENUE_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LowBirthChildcarePolicyVocabularyNoRevenueCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_MFE_but_deep_MAE_no_policy_to_revenue_bridge","current_profile_verdict":"current_profile_false_positive_if_low_birth_policy_price_MFE_overcredited","price_source":"Songdaiki/stock-web","notes":"Low-birth/childcare policy vocabulary produced local price MFE but then deep MAE. Without named implementation, beneficiary economics, revenue channel and cash bridge, price MFE should remain 4B-watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 086790 하나금융지주 — value-up policy to capital-return bridge positive-control

Entry row: `2024-01-29 c=46400`.
Observed path: entry-area low `2024-01-29 l=44800`, 90D peak `2024-05-13 h=65300`, and full-window peak `2024-10-25 h=69200`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L91_C31_086790_20240129_STAGE2_VALUEUP_POLICY_CAPITAL_RETURN","case_id":"C31_R12L91_086790_HANA_VALUEUP_CAPITAL_RETURN","symbol":"086790","company_name":"하나금융지주","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_POLICY_TO_CAPITAL_RETURN_CASH_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-ValueupCapitalReturnPolicyToCashBridge-Positive","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":46400.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_corporate_valueup_policy_capital_return_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; value-up policy, payout/buyback/cancellation and capital-return bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_policy_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["valueup_policy_proxy","payout_policy_proxy","capital_return_proxy","relative_strength_policy_turn"],"stage3_evidence_fields":["exact_board_policy_source_pending","buyback_or_cancellation_source_pending","capital_buffer_source_pending","cash_return_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","policy_execution_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","profile_path":"atlas/symbol_profiles/086/086790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":29.31,"MFE_90D_pct":40.73,"MFE_180D_pct":49.14,"MAE_30D_pct":-3.45,"MAE_90D_pct":-3.45,"MAE_180D_pct":-3.45,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":69200.0,"max_drawdown_low_date":"2024-01-29","max_drawdown_low":44800.0,"drawdown_after_peak_pct":-18.21,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.42,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_policy_timetable_board_payout_buyback_capital_cash_evidence","four_b_evidence_type":["price_extension_watch","policy_execution_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE90_low_MAE_policy_to_cash_bridge","current_profile_verdict":"current_profile_correct_if_policy_timetable_payout_capital_return_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"086790_2024-01-29_46400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C31 can allow Stage2/Yellow when policy strength is tied to implementation timetable, board execution, payout/buyback/cancellation, capital buffer and cash return. Green still requires exact source-grade evidence."}
```

### 6.2 034230 파라다이스 — casino/tourism policy vocabulary without fresh policy-to-cash bridge

Entry row: `2024-04-01 c=15310`, after the first tourism/casino policy rebound.
Observed path: local high `2024-05-02 h=15710`, then deep decline to `2024-11-14 l=9020`. Market segment changed from KOSDAQ to KOSPI on `2024-06-24`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L91_C31_034230_20240401_STAGE2_FALSE_POSITIVE_CASINO_TOURISM_POLICY","case_id":"C31_R12L91_034230_PARADISE_CASINO_TOURISM_POLICY","symbol":"034230","company_name":"파라다이스","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CASINO_TOURISM_POLICY_VOCABULARY_WITHOUT_FRESH_TRAFFIC_MARGIN_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;market_segment_change_watch","trigger_type":"Stage2-FalsePositive-CasinoTourismPolicyVocabularyNoFreshPolicyToCashBridge","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":15310.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_casino_tourism_policy_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; tourism/casino policy vocabulary treated as insufficient without fresh regulatory/tax change, VIP traffic, hold rate, margin and cash bridge","evidence_source_type":"historical_public_policy_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["casino_tourism_policy_vocabulary","post_rebound_relative_strength"],"stage3_evidence_fields":["fresh_regulatory_or_tax_change_missing","VIP_traffic_recovery_missing","margin_cash_bridge_missing","policy_execution_timetable_missing"],"stage4b_evidence_fields":["near_zero_MFE","market_segment_change_watch","policy_cash_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034230/2024.csv","profile_path":"atlas/symbol_profiles/034/034230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.61,"MFE_90D_pct":2.61,"MFE_180D_pct":2.61,"MAE_30D_pct":-6.66,"MAE_90D_pct":-19.92,"MAE_180D_pct":-41.08,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-02","peak_price":15710.0,"max_drawdown_low_date":"2024-11-14","max_drawdown_low":9020.0,"drawdown_after_peak_pct":-42.58,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"casino_tourism_policy_vocabulary_without_fresh_traffic_margin_cash_bridge_should_be_4B_watch_not_positive; market_segment_change_requires_repair","four_b_evidence_type":["near_zero_MFE","market_segment_change_watch","policy_cash_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_market_segment_watch","current_profile_verdict":"current_profile_false_positive_if_tourism_casino_policy_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["market_segment_change_watch_KOSDAQ_to_KOSPI_after_entry"],"corporate_action_window_status":"clean; market_segment_changed_after_entry","same_entry_group_id":"034230_2024-04-01_15310","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.95,"do_not_count_as_new_case":false,"current_profile_residual":"C31 should not promote tourism/casino policy vocabulary unless a fresh policy execution path, traffic/revenue channel, margin and cash bridge are repaired. Market-segment-change rows need data-quality repair before patching."}
```

### 6.3 068290 삼성출판사 — low-birth/childcare policy vocabulary without revenue/cash bridge

Entry row: `2024-01-10 c=24000`, on a low-birth/childcare policy spike.
Observed path: local peak `2024-02-06 h=29950`, then sustained decline to `2024-11-15 l=12880` and later December lows near `13820`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L91_C31_068290_20240110_STAGE2_FALSE_POSITIVE_LOWBIRTH_CHILDCARE_POLICY","case_id":"C31_R12L91_068290_SAMSUNG_PUBLISHING_LOWBIRTH_POLICY","symbol":"068290","company_name":"삼성출판사","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"LOW_BIRTH_CHILDCARE_POLICY_VOCABULARY_WITHOUT_REVENUE_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;price_only_MFE_policy_stress_test","trigger_type":"Stage2-FalsePositive-LowBirthChildcarePolicyVocabularyNoRevenueCashBridge","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":24000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_low_birth_childcare_policy_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; low-birth/childcare policy vocabulary treated as insufficient without beneficiary mapping, revenue channel, implementation timetable, margin and cash bridge","evidence_source_type":"historical_public_policy_theme_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["low_birth_policy_vocabulary","childcare_policy_keyword","relative_strength_spike"],"stage3_evidence_fields":["eligible_beneficiary_mapping_missing","implementation_timetable_missing","revenue_channel_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_MFE","policy_to_revenue_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/068/068290/2024.csv","profile_path":"atlas/symbol_profiles/068/068290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.79,"MFE_90D_pct":24.79,"MFE_180D_pct":24.79,"MAE_30D_pct":-16.67,"MAE_90D_pct":-22.88,"MAE_180D_pct":-46.33,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-06","peak_price":29950.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":12880.0,"drawdown_after_peak_pct":-57.00,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"low_birth_childcare_policy_MFE_without_policy_to_revenue_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only_MFE","policy_to_revenue_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_MFE_but_deep_MAE_no_policy_to_revenue_bridge","current_profile_verdict":"current_profile_false_positive_if_low_birth_policy_price_MFE_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"068290_2024-01-10_24000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C31 should not count low-birth/childcare policy MFE as policy-to-cash evidence unless the company has a mapped beneficiary channel, implementation timetable, revenue/margin bridge and cash conversion."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_R12L91_086790_HANA_VALUEUP_CAPITAL_RETURN","trigger_id":"R12L91_C31_086790_20240129_STAGE2_VALUEUP_POLICY_CAPITAL_RETURN","symbol":"086790","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C31 requires named policy, implementation path, board/regulatory execution, payout/buyback/cancellation and cash-return bridge rather than policy label alone","raw_component_scores_before":{"named_policy_score":13,"implementation_timetable_score":10,"eligible_recipient_score":12,"regulatory_board_execution_score":11,"subsidy_or_return_mechanism_score":13,"volume_or_revenue_channel_score":9,"margin_cash_score":9,"relative_strength_score":14,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"named_policy_score":16,"implementation_timetable_score":12,"eligible_recipient_score":14,"regulatory_board_execution_score":14,"subsidy_or_return_mechanism_score":16,"volume_or_revenue_channel_score":11,"margin_cash_score":11,"relative_strength_score":15,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Value-up policy-to-cash bridge plus high MFE and low MAE supports Yellow/Green-candidate watch; exact board/payout/buyback/capital evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_R12L91_034230_PARADISE_CASINO_TOURISM_POLICY","trigger_id":"R12L91_C31_034230_20240401_STAGE2_FALSE_POSITIVE_CASINO_TOURISM_POLICY","symbol":"034230","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_scope":"current_default_proxy","profile_hypothesis":"casino/tourism policy vocabulary without fresh traffic, regulation/tax and margin bridge should be blocked","raw_component_scores_before":{"named_policy_score":3,"implementation_timetable_score":1,"eligible_recipient_score":2,"regulatory_board_execution_score":0,"subsidy_or_return_mechanism_score":0,"volume_or_revenue_channel_score":1,"margin_cash_score":0,"relative_strength_score":3,"valuation_repricing_score":2,"execution_risk_score":-12,"theme_spike_risk":-16,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/MarketSegmentWatch","raw_component_scores_after":{"named_policy_score":1,"implementation_timetable_score":0,"eligible_recipient_score":0,"regulatory_board_execution_score":0,"subsidy_or_return_mechanism_score":0,"volume_or_revenue_channel_score":0,"margin_cash_score":0,"relative_strength_score":0,"valuation_repricing_score":0,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Near-zero MFE, deep MAE and market-segment change require fresh policy-to-cash evidence before Yellow/Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_R12L91_068290_SAMSUNG_PUBLISHING_LOWBIRTH_POLICY","trigger_id":"R12L91_C31_068290_20240110_STAGE2_FALSE_POSITIVE_LOWBIRTH_CHILDCARE_POLICY","symbol":"068290","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_scope":"current_default_proxy","profile_hypothesis":"low-birth/childcare policy price MFE without beneficiary-to-revenue bridge should remain 4B-watch","raw_component_scores_before":{"named_policy_score":4,"implementation_timetable_score":1,"eligible_recipient_score":1,"regulatory_board_execution_score":0,"subsidy_or_return_mechanism_score":0,"volume_or_revenue_channel_score":0,"margin_cash_score":0,"relative_strength_score":12,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-20,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"named_policy_score":1,"implementation_timetable_score":0,"eligible_recipient_score":0,"regulatory_board_execution_score":0,"subsidy_or_return_mechanism_score":0,"volume_or_revenue_channel_score":0,"margin_cash_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Price MFE is theme-only; deep MAE and missing policy-to-revenue/cash bridge block Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R12L91_C31_P0_CURRENT","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C31 needs explicit named policy, implementation timetable, eligible recipient, execution path, subsidy/return mechanism, revenue channel and cash bridge","eligible_trigger_count":3,"avg_MFE90_pct":22.71,"avg_MAE90_pct":-10.07,"avg_MFE180_pct":25.51,"avg_MAE180_pct":-30.29,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.81,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C31_policy_to_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R12L91_C31_P1_SECTOR_SPECIFIC","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P1_L10_policy_to_cash_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L10 policy signals need named policy plus implementation/eligible-recipient/revenue-or-return/cash bridge before Stage2-Actionable","changed_axes":["implementation_timetable_required","eligible_recipient_required","policy_to_cash_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_implementation_timetable_eligible_recipient_regulatory_execution_subsidy_return_revenue_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":22.71,"avg_MAE90_pct":-10.07,"avg_MFE180_pct":25.51,"avg_MAE180_pct":-30.29,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R12L91_C31_P2_CANONICAL","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P2_C31_policy_to_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C31 should reward policy-to-contract/revenue/capital-return mechanics, not policy vocabulary or price MFE","changed_axes":["C31_policy_to_cash_bridge_required","C31_casino_lowbirth_vocabulary_local_4B_guard","C31_price_MFE_not_policy_validation_guard","C31_market_segment_change_data_quality_guard"],"changed_thresholds":{"stage2_yellow_gate":"named_policy_plus_implementation_or_return_or_revenue_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":22.71,"avg_MAE90_pct":-10.07,"avg_MFE180_pct":25.51,"avg_MAE180_pct":-30.29,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R12L91_C31_P3_COUNTEREXAMPLE_GUARD","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P3_C31_price_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If policy-to-cash bridge is missing, price MFE does not validate; MFE90<5 or MAE180<=-30 routes to 4B-watch","changed_axes":["C31_near_zero_MFE_guardrail","C31_deep_MAE_4B_guardrail","C31_price_only_policy_MFE_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_5_or_MAE180_le_minus_30); high_MFE_without_bridge_not_positive"},"eligible_trigger_count":3,"avg_MFE90_pct":22.71,"avg_MAE90_pct":-10.07,"avg_MFE180_pct":25.51,"avg_MAE180_pct":-30.29,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_VALUEUP_POLICY_POSITIVE_VS_CASINO_LOWBIRTH_VOCABULARY_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":22.71,"avg_MAE90_pct":-10.07,"avg_MFE180_pct":25.51,"avg_MAE180_pct":-30.29,"stage2_hit_rate_MFE90_ge20":0.67,"price_MFE_without_bridge_counterexample_count":1,"stage2_bad_entry_rate_bridge_missing":0.67,"interpretation":"C31 needs bridge discipline. 하나금융지주 shows value-up policy-to-capital-return bridge can support Yellow/Green-candidate-watch, while 파라다이스 and 삼성출판사 show casino/tourism or low-birth/childcare policy vocabulary should not be promoted without implementation timetable, eligible beneficiary mapping, revenue/traffic channel, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"086790","trigger_type":"Stage2-Actionable-ValueupCapitalReturnPolicyToCashBridge-Positive","entry_date":"2024-01-29","stage2_to_90D_outcome":"good_stage2_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_valueup_policy_to_cash_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when policy is tied to executable payout/buyback/cancellation/capital-return and cash bridge; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"034230","trigger_type":"Stage2-FalsePositive-CasinoTourismPolicyVocabularyNoFreshPolicyToCashBridge","entry_date":"2024-04-01","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_policy_cash_bridge_missing","stage2_to_180D_outcome":"failed_casino_tourism_policy_vocabulary_deep_MAE_market_segment_watch","MFE90_ge20":false,"MAE180_le_minus30":true,"transition_note":"Casino/tourism policy vocabulary without fresh traffic/revenue/margin bridge should stay Watch/4B-risk; market-segment change needs repair."}
{"row_type":"stage_transition_summary","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"068290","trigger_type":"Stage2-FalsePositive-LowBirthChildcarePolicyVocabularyNoRevenueCashBridge","entry_date":"2024-01-10","stage2_to_90D_outcome":"price_MFE_without_policy_to_revenue_bridge","stage2_to_180D_outcome":"failed_lowbirth_policy_vocabulary_deep_MAE","MFE90_ge20":true,"MAE180_le_minus30":true,"transition_note":"Low-birth policy price MFE without beneficiary/revenue/cash bridge should be 4B-watch, not positive C31 evidence."}
{"row_type":"residual_contribution","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"policy_vocabulary_and_price_MFE_overcredit_without_implementation_revenue_cash_bridge","contribution":"Adds two C31 4B counterexamples against one value-up policy-to-cash positive, avoiding C31 top-covered and previous R12 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_CAPITAL_RETURN_POLICY_TO_CASH_BRIDGE_VS_CASINO_LOW_BIRTH_POLICY_VOCABULARY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C31 now has non-top-symbol value-up policy-to-cash positive and two casino/low-birth weak-bridge counterexamples; next R12 C31 loops should exact-URL repair implementation timetable, eligible beneficiary, board/regulatory execution, subsidy/capital-return mechanism, revenue channel, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","axis":"C31_policy_to_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"086790 worked when value-up policy was linked to capital-return/cash proxy; 034230 and 068290 failed when policy vocabulary lacked implementation/revenue/cash bridge."}
{"row_type":"shadow_weight","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","axis":"C31_casino_lowbirth_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Casino/tourism and low-birth/childcare policy rows should remain Watch/4B unless beneficiary economics, revenue channel and cash conversion are exact-repaired."}
{"row_type":"shadow_weight","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","axis":"C31_price_MFE_not_policy_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"068290 shows MFE90 above 20 should not count as positive C31 evidence when policy-to-revenue bridge is missing and MAE180 is deep."}
{"row_type":"shadow_weight","round":"R12","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","axis":"C31_market_segment_change_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"034230 changed market segment from KOSDAQ to KOSPI after selected entry, so patch consideration needs price-path and evidence repair."}
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
  - policy_vocabulary_overcredit
  - casino_tourism_policy_vocabulary_overcredit
  - low_birth_childcare_policy_price_MFE_overcredit
  - implementation_timetable_bridge_missing
  - revenue_margin_cash_bridge_missing
  - market_segment_change_watch
new_axis_proposed:
  - C31_policy_to_cash_bridge_required_shadow_only
  - C31_casino_lowbirth_vocabulary_local_4B_guard_shadow_only
  - C31_price_MFE_not_policy_validation_guard_shadow_only
  - C31_market_segment_change_data_quality_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C31
  - full_4b_requires_non_price_evidence within C31
  - hard_4c_thesis_break_routes_to_4c within C31
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
`086790` has clean selected 2024 window.
`034230` has no corporate-action candidate, but market segment changed from KOSDAQ to KOSPI after selected entry, so it remains market-segment-change watch.
`068290` has an old 2008 corporate-action candidate before the selected 2024 window; the 2024 window is usable for residual price-path analysis.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
market_segment_change_watch = true for 034230
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
3. Confirm R12 / L10 / C31 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C31 top-covered symbols
   - previous R12 loop85 C31 symbols
   - previous R12 loop86 C32 symbols
   - previous R12 loop87 C31 symbols
   - previous R12 loop88 C32 symbols
   - previous R12 loop89 C31 symbols
   - previous R12 loop90 C32 symbols
6. Confirm accidentally touched R11/C04 and stale R10/C30 candidate rows are not ingested from this MD.
7. Keep 034230 in market-segment-change watch before patch consideration.
8. Treat 068290 as policy-price-MFE failure-mode stress only; do not promote without exact implementation/revenue/cash evidence.
9. If aggregate support remains stable after exact evidence URL repair, consider C31-scoped safe patch candidates:
   - C31_policy_to_cash_bridge_required
   - C31_casino_lowbirth_vocabulary_local_4B_guard
   - C31_price_MFE_not_policy_validation_guard
   - C31_market_segment_change_data_quality_guard
10. Do not loosen Stage3-Green.
11. Do not use future MFE/MAE in runtime scoring.
12. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R12
completed_loop = 91
next_round = R13
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.
```
