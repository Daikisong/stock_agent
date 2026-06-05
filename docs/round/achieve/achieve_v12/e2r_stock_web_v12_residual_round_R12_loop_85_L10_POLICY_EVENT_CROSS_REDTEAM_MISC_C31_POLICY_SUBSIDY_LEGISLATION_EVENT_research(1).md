# E2R Stock-Web v12 Residual Research — R12 Loop 85 / L10 / C31

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R12
loop: 85
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: VALUEUP_POLICY_CAPITAL_RETURN_BRIDGE_VS_POLICY_THEME_SPIKE_NO_EARNINGS_OR_RETURN_CONVERSION
sector: policy / legislation / subsidy / value-up / cross-redteam
output_file: e2r_stock_web_v12_residual_round_R12_loop_85_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R11 loop 85`.

```text
scheduled_round = R12
scheduled_loop = 85
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

R12 is the policy / event / cross-redteam / miscellaneous lane.  
C31 is selected because the previous R12 loop used C32 governance/control-premium evidence. This loop tests whether policy-event enthusiasm should be promoted only when a real bridge appears: capital return, earnings revision, subsidy monetization, legislation execution, financing, or customer/order conversion.

The selected symbols avoid the C31 top-covered list in the No-Repeat Index:

```text
013990, 003550, 015760, 032350, 114090, 000270
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"055550","company_name":"신한지주","profile_path":"atlas/symbol_profiles/055/055550.json","first_date":"2001-09-10","last_date":"2026-02-20","trading_day_count":6031,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"034730","company_name":"SK","profile_path":"atlas/symbol_profiles/034/034730.json","first_date":"2009-11-11","last_date":"2026-02-20","trading_day_count":4007,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2015-08-17"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"004020","company_name":"현대제철","profile_path":"atlas/symbol_profiles/004/004020.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7764,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1997-01-03","1997-10-16","1999-03-25","1999-07-14","2000-04-12","2014-01-24"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"055550","trigger_type":"Stage2-Actionable-ValueupPolicyCapitalReturnBridge-Positive","entry_date":"2024-01-29","duplicate_status":"new C31 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"034730","trigger_type":"Stage2-FalsePositive-HoldcoValueupPolicyTheme-NoDirectReturnBridge","entry_date":"2024-02-19","duplicate_status":"new C31 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"004020","trigger_type":"Stage2-FalsePositive-CyclicalValueupPolicyTheme-NoEarningsBridge","entry_date":"2024-01-29","duplicate_status":"new C31 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C31 is not “policy headline appeared.”  
A policy event only becomes E2R-grade when it crosses the bridge into an executable economic mechanism: capital return, subsidy monetization, legislative passage, tariff/rate pass-through, order conversion, financing trust, or earnings revision. Otherwise the market is only voting on the announcement smoke, not on the engine.

Residual question:

```text
Can C31 distinguish:
1. value-up policy plus bank capital-return bridge with sustained rerating,
2. holding-company value-up policy theme without direct shareholder-return / NAV conversion,
3. cyclical low-PBR value-up theme without earnings, spread, or capital-return bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C31_R12L85_055550_SHINHAN_VALUEUP_POLICY_CAPITAL_RETURN","symbol":"055550","company_name":"신한지주","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_POLICY_CAPITAL_RETURN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-ValueupPolicyCapitalReturnBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_shallow_MAE","current_profile_verdict":"current_profile_correct_if_policy_to_capital_return_bridge_required","price_source":"Songdaiki/stock-web","notes":"Value-up policy worked when joined to visible bank capital-return/PBR repair proxy; Green still needs exact dividend/buyback and capital-buffer evidence."}
{"row_type":"case","case_id":"C31_R12L85_034730_SK_HOLDCO_VALUEUP_THEME_NO_RETURN_BRIDGE","symbol":"034730","company_name":"SK","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"HOLDCO_VALUEUP_POLICY_THEME_WITHOUT_DIRECT_RETURN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-HoldcoValueupPolicyTheme-NoDirectReturnBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_valueup_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Holding-company value-up policy rebound failed when the direct shareholder-return/NAV/capital-allocation bridge did not confirm."}
{"row_type":"case","case_id":"C31_R12L85_004020_HYUNDAISTEEL_CYCLICAL_VALUEUP_THEME","symbol":"004020","company_name":"현대제철","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CYCLICAL_LOW_PBR_VALUEUP_THEME_WITHOUT_EARNINGS_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CyclicalValueupPolicyTheme-NoEarningsBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_lowPBR_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Low-PBR/policy theme in a cyclical name had limited MFE and persistent MAE without earnings, spread or capital-return bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 055550 신한지주 — value-up policy plus capital-return bridge positive

Entry row: `2024-01-29 c=40500`.  
Observed path: early low `2024-02-26 l=39850`, 30D/90D high `2024-03-14 h=51500`, and later full-window high `2024-10-25 h=59900`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L85_C31_055550_20240129_STAGE2_VALUEUP_POLICY_CAPITAL_RETURN","case_id":"C31_R12L85_055550_SHINHAN_VALUEUP_POLICY_CAPITAL_RETURN","symbol":"055550","company_name":"신한지주","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_POLICY_CAPITAL_RETURN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-ValueupPolicyCapitalReturnBridge-Positive","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":40500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_valueup_policy_capital_return_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; value-up policy plus bank capital-return/PBR repair thesis treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_policy_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["policy_event_proxy","capital_return_proxy","PBR_discount_repair_proxy","relative_strength_turn"],"stage3_evidence_fields":["dividend_buyback_confirmation_pending","capital_buffer_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv","profile_path":"atlas/symbol_profiles/055/055550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.16,"MFE_90D_pct":27.16,"MFE_180D_pct":47.90,"MAE_30D_pct":-1.60,"MAE_90D_pct":-1.60,"MAE_180D_pct":-1.60,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":59900.0,"max_drawdown_low_date":"2024-02-26","max_drawdown_low":39850.0,"drawdown_after_peak_pct":-19.45,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_shallow_MAE","current_profile_verdict":"current_profile_correct_if_policy_to_capital_return_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"055550_2024-01-29_40500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C31 can allow Stage2/Yellow when policy event connects to a concrete capital-return/PBR repair bridge. Green still requires exact capital-return and policy execution evidence."}
```

### 6.2 034730 SK — holdco value-up policy theme without direct return bridge

Entry row: `2024-02-19 c=207500`.  
Observed path: local high `2024-02-23 h=212000`, then low `2024-05-29 l=144400`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L85_C31_034730_20240219_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP_THEME","case_id":"C31_R12L85_034730_SK_HOLDCO_VALUEUP_THEME_NO_RETURN_BRIDGE","symbol":"034730","company_name":"SK","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"HOLDCO_VALUEUP_POLICY_THEME_WITHOUT_DIRECT_RETURN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-HoldcoValueupPolicyTheme-NoDirectReturnBridge","trigger_date":"2024-02-19","entry_date":"2024-02-19","entry_price":207500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_valueup_holdco_policy_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; holding-company value-up policy theme treated as insufficient without direct shareholder-return, NAV repair or capital-allocation bridge","evidence_source_type":"historical_public_policy_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["valueup_policy_theme","holdco_lowPBR_theme","relative_strength_rebound"],"stage3_evidence_fields":["direct_shareholder_return_bridge_missing","NAV_discount_repair_missing","capital_allocation_confirmation_missing"],"stage4b_evidence_fields":["price_only_local_peak","policy_theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034730/2024.csv","profile_path":"atlas/symbol_profiles/034/034730.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.17,"MFE_90D_pct":2.17,"MFE_180D_pct":2.17,"MAE_30D_pct":-14.07,"MAE_90D_pct":-30.41,"MAE_180D_pct":-30.41,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-23","peak_price":212000.0,"max_drawdown_low_date":"2024-05-29","max_drawdown_low":144400.0,"drawdown_after_peak_pct":-31.89,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"policy_theme_peak_without_direct_return_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","policy_theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_valueup_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"034730_2024-02-19_207500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C31 should block policy-theme upgrades when direct shareholder-return/NAV/capital-allocation bridge is missing. Low MFE and high MAE support Watch/4B-risk."}
```

### 6.3 004020 현대제철 — cyclical low-PBR policy theme without earnings bridge

Entry row: `2024-01-29 c=35700`.  
Observed path: local high `2024-02-13 h=37500`, then lows `2024-06-11 l=28500` and `2024-07-19 l=27750`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L85_C31_004020_20240129_STAGE2_FALSE_POSITIVE_CYCLICAL_VALUEUP_THEME","case_id":"C31_R12L85_004020_HYUNDAISTEEL_CYCLICAL_VALUEUP_THEME","symbol":"004020","company_name":"현대제철","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CYCLICAL_LOW_PBR_VALUEUP_THEME_WITHOUT_EARNINGS_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-CyclicalValueupPolicyTheme-NoEarningsBridge","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":35700.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_lowPBR_valueup_cyclical_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; low-PBR/value-up policy theme treated as insufficient without earnings revision, spread/margin bridge or capital-return confirmation","evidence_source_type":"historical_public_policy_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["valueup_policy_theme","lowPBR_cyclical_theme","relative_strength_spike"],"stage3_evidence_fields":["earnings_revision_missing","spread_margin_bridge_missing","capital_return_confirmation_missing"],"stage4b_evidence_fields":["price_only_local_peak","earnings_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004020/2024.csv","profile_path":"atlas/symbol_profiles/004/004020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.04,"MFE_90D_pct":5.04,"MFE_180D_pct":5.04,"MAE_30D_pct":-3.64,"MAE_90D_pct":-20.17,"MAE_180D_pct":-22.27,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-13","peak_price":37500.0,"max_drawdown_low_date":"2024-07-19","max_drawdown_low":27750.0,"drawdown_after_peak_pct":-26.00,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"lowPBR_policy_theme_without_earnings_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","earnings_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_lowPBR_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"004020_2024-01-29_35700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C31 policy/low-PBR theme is not enough when earnings/spread/capital-return bridge is missing. Low MFE and high MAE argue for Watch/4B-risk."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C31_R12L85_055550_SHINHAN_VALUEUP_POLICY_CAPITAL_RETURN","trigger_id":"R12L85_C31_055550_20240129_STAGE2_VALUEUP_POLICY_CAPITAL_RETURN","symbol":"055550","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C31 requires policy-to-economic bridge rather than policy headline alone","raw_component_scores_before":{"policy_event_quality":13,"execution_probability":12,"capital_return_or_subsidy_monetization":14,"earnings_revision_bridge":9,"valuation_repricing_score":12,"relative_strength_score":12,"source_quality":5,"implementation_delay_risk":-4,"theme_spike_risk":-2},"weighted_score_before":71,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"policy_event_quality":15,"execution_probability":14,"capital_return_or_subsidy_monetization":17,"earnings_revision_bridge":11,"valuation_repricing_score":13,"relative_strength_score":13,"source_quality":6,"implementation_delay_risk":-3,"theme_spike_risk":-1},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Policy event plus capital-return bridge supports Yellow-watch; exact dividend/buyback and policy implementation evidence still blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C31_R12L85_034730_SK_HOLDCO_VALUEUP_THEME_NO_RETURN_BRIDGE","trigger_id":"R12L85_C31_034730_20240219_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP_THEME","symbol":"034730","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_scope":"current_default_proxy","profile_hypothesis":"policy theme without direct economic bridge should be blocked","raw_component_scores_before":{"policy_event_quality":10,"execution_probability":4,"capital_return_or_subsidy_monetization":2,"earnings_revision_bridge":1,"valuation_repricing_score":6,"relative_strength_score":9,"source_quality":3,"implementation_delay_risk":-12,"theme_spike_risk":-14},"weighted_score_before":9,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"policy_event_quality":5,"execution_probability":1,"capital_return_or_subsidy_monetization":0,"earnings_revision_bridge":0,"valuation_repricing_score":2,"relative_strength_score":3,"source_quality":2,"implementation_delay_risk":-18,"theme_spike_risk":-20},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and high MAE convert policy-theme rebound into missing-bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C31_R12L85_004020_HYUNDAISTEEL_CYCLICAL_VALUEUP_THEME","trigger_id":"R12L85_C31_004020_20240129_STAGE2_FALSE_POSITIVE_CYCLICAL_VALUEUP_THEME","symbol":"004020","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_scope":"current_default_proxy","profile_hypothesis":"cyclical low-PBR policy theme without earnings/spread bridge should remain Watch/blocked","raw_component_scores_before":{"policy_event_quality":9,"execution_probability":3,"capital_return_or_subsidy_monetization":2,"earnings_revision_bridge":1,"valuation_repricing_score":6,"relative_strength_score":8,"source_quality":3,"implementation_delay_risk":-10,"theme_spike_risk":-12},"weighted_score_before":7,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"policy_event_quality":4,"execution_probability":1,"capital_return_or_subsidy_monetization":0,"earnings_revision_bridge":0,"valuation_repricing_score":2,"relative_strength_score":3,"source_quality":2,"implementation_delay_risk":-16,"theme_spike_risk":-18},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Policy/low-PBR label does not offset missing earnings and capital-return bridge."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R12L85_C31_P0_CURRENT","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C31 needs explicit policy-to-economic bridge taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":11.46,"avg_MAE90_pct":-17.39,"avg_MFE180_pct":18.37,"avg_MAE180_pct":-18.09,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C31_policy_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R12L85_C31_P1_SECTOR_SPECIFIC","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P1_L10_policy_execution_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L10 policy signals need execution, capital return, subsidy monetization, legislation pass-through or earnings revision before Stage2-Actionable","changed_axes":["policy_execution_bridge_required","economic_conversion_required","theme_spike_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_capital_return_subsidy_monetization_legislation_execution_or_earnings_revision_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":11.46,"avg_MAE90_pct":-17.39,"avg_MFE180_pct":18.37,"avg_MAE180_pct":-18.09,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R12L85_C31_P2_CANONICAL","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P2_C31_policy_to_economic_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C31 should reward policy implementation bridges, not policy headline beta","changed_axes":["C31_policy_to_economic_bridge_required","C31_valueup_theme_without_return_penalty","C31_lowPBR_theme_local_4B_guard"],"changed_thresholds":{"stage2_yellow_gate":"policy_plus_economic_conversion_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":11.46,"avg_MAE90_pct":-17.39,"avg_MFE180_pct":18.37,"avg_MAE180_pct":-18.09,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R12L85_C31_P3_COUNTEREXAMPLE_GUARD","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P3_C31_low_MFE_no_bridge_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<6 and MAE90<=-20 while policy-to-economic bridge is missing, block Yellow/Green","changed_axes":["C31_low_MFE_guardrail","C31_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_6_and_MAE90_le_minus_20"},"eligible_trigger_count":3,"avg_MFE90_pct":11.46,"avg_MAE90_pct":-17.39,"avg_MFE180_pct":18.37,"avg_MAE180_pct":-18.09,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_VALUEUP_POLICY_BRIDGE_VS_POLICY_THEME_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":11.46,"avg_MAE90_pct":-17.39,"avg_MFE180_pct":18.37,"avg_MAE180_pct":-18.09,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_6":0.67,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C31 needs bridge discipline. 신한지주 shows policy plus capital-return bridge can rerate, while SK and 현대제철 show policy/value-up/low-PBR themes can fail without direct economic conversion."}
{"row_type":"stage_transition_summary","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"055550","trigger_type":"Stage2-Actionable-ValueupPolicyCapitalReturnBridge-Positive","entry_date":"2024-01-29","stage2_to_90D_outcome":"good_stage2_high_MFE_shallow_MAE","stage2_to_180D_outcome":"positive_policy_capital_return_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when policy is tied to capital-return/PBR repair bridge; Green requires exact execution evidence."}
{"row_type":"stage_transition_summary","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"034730","trigger_type":"Stage2-FalsePositive-HoldcoValueupPolicyTheme-NoDirectReturnBridge","entry_date":"2024-02-19","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_holdco_policy_theme","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Holding-company policy theme without direct return/NAV bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"004020","trigger_type":"Stage2-FalsePositive-CyclicalValueupPolicyTheme-NoEarningsBridge","entry_date":"2024-01-29","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_cyclical_lowPBR_policy_theme","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Low-PBR policy theme without earnings/spread/capital-return bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"policy_event_overcredit_without_economic_conversion_bridge","contribution":"Adds two C31 local 4B/weak-bridge counterexamples against one value-up capital-return positive, avoiding C31 top-covered symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_POLICY_CAPITAL_RETURN_BRIDGE_VS_POLICY_THEME_SPIKE_NO_EARNINGS_OR_RETURN_CONVERSION","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C31 now has non-top-symbol value-up/policy-theme counterexamples; next R12 loops should exact-URL repair policy execution, legislation/subsidy monetization, capital return and earnings revision evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","axis":"C31_policy_to_economic_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"055550 worked with policy plus capital-return bridge proxy; 034730 and 004020 failed when policy theme lacked direct economic conversion."}
{"row_type":"shadow_weight","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","axis":"C31_policy_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Policy/value-up/low-PBR theme spikes showed low MFE and high MAE without capital-return, earnings, or subsidy/legislation execution bridge."}
{"row_type":"shadow_weight","round":"R12","loop":"85","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","axis":"C31_low_MFE_no_bridge_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<6 and MAE90<=-20 while policy-to-economic bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - policy_event_overcredit
  - valueup_theme_no_direct_return_bridge
  - lowPBR_cyclical_theme_no_earnings_bridge
  - policy_headline_without_economic_conversion
new_axis_proposed:
  - C31_policy_to_economic_bridge_required_shadow_only
  - C31_policy_theme_local_4B_watch_guard_shadow_only
  - C31_low_MFE_no_bridge_guardrail_shadow_only
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
3. Confirm R12 / L10 / C31 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided C31 top-covered symbols.
6. If aggregate support remains stable after exact evidence URL repair, consider C31-scoped safe patch candidates:
   - C31_policy_to_economic_bridge_required
   - C31_policy_theme_local_4B_watch_guard
   - C31_low_MFE_no_bridge_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R12
completed_loop = 85
next_round = R13
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.
```
