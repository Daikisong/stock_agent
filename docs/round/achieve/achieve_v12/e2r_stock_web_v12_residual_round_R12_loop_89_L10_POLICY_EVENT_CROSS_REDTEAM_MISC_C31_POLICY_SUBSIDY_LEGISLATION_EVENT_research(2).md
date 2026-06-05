# E2R Stock-Web v12 Residual Research — R12 Loop 89 / L10 / C31

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R12
loop: 89
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: UTILITY_TARIFF_VALUEUP_POLICY_BRIDGE_VS_CASINO_TRAVEL_POLICY_THEME_DECAY
sector: policy / subsidy / legislation / tariff / tourism / casino / value-up
output_file: e2r_stock_web_v12_residual_round_R12_loop_89_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R11 loop 89`.

```text
scheduled_round = R12
scheduled_loop = 89
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

R12 is the policy / event / governance / cross-misc lane.  
C31 is selected because the immediately previous R12 loop used C32 governance / tender-cap, while C31 still needs more examples that separate **policy economics** from **policy vocabulary**.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
rows = 97
symbols = 70
good/bad Stage2 = 35/25
4B/4C = 5/0
top-covered = 013990, 003550, 015760, 032350, 114090, 000270
```

This loop avoids the C31 top-covered symbols and recent R12 loop symbols:

```text
R12 loop85 C31: 055550, 034730, 004020
R12 loop86 C32: 028260, 001040, 004990
R12 loop87 C31: 036460, 004090, 024060
R12 loop88 C32: 000240, 001230, 004800
```

Candidate hygiene note:

```text
A separate R11/C02 grid candidate sweep was touched during source lookup.
Those candidates are not used in this R12/C31 output.
```

Selected symbols:

```text
071320, 035250, 039130
```

This loop tests:

```text
utility tariff / value-up policy bridge
vs
casino regulatory / tourism policy theme without durable capex, payout or demand-to-margin bridge
vs
travel/tourism policy rebound without durable demand conversion, margin and cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"071320","company_name":"지역난방공사","profile_path":"atlas/symbol_profiles/071/071320.json","first_date":"2010-01-29","last_date":"2026-02-20","trading_day_count":3953,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"035250","company_name":"강원랜드","profile_path":"atlas/symbol_profiles/035/035250.json","first_date":"2001-10-25","last_date":"2026-02-20","trading_day_count":5998,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2003-11-04"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"039130","company_name":"하나투어","profile_path":"atlas/symbol_profiles/039/039130.json","first_date":"2000-11-28","last_date":"2026-02-20","trading_day_count":6221,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2003-09-09","2003-09-30","2004-11-19"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"071320","trigger_type":"Stage2-Actionable-UtilityTariffValueupPolicyBridge-Positive","entry_date":"2024-01-26","duplicate_status":"new C31 symbol/trigger/date combination outside top-covered and previous R12 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"035250","trigger_type":"Stage2-FalsePositive-CasinoRegulatoryPolicyRebound-NoDurablePayoutDemandBridge","entry_date":"2024-02-06","duplicate_status":"new C31 symbol/trigger/date combination outside top-covered and previous R12 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"039130","trigger_type":"Stage2-FalsePositive-TravelPolicyRebound-NoDemandMarginCashBridge","entry_date":"2024-01-31","duplicate_status":"new C31 symbol/trigger/date combination outside top-covered and previous R12 loop symbols"}
```

## 4. Research question

C31 is not “정책 뉴스가 있다.”  
The useful signal must connect policy wording to economics:

```text
tariff or subsidy pass-through
regulated cost recovery
capital return / payout mechanism
legal or regulatory certainty
confirmed funding or demand channel
beneficiary scope
margin bridge
cash conversion
```

A policy headline without that bridge is a permit stamp on an empty warehouse: it authorizes possibility, not cash flow.

Residual question:

```text
Can C31 distinguish:
1. utility tariff/value-up policy bridge that repairs economics and produces a large MFE path,
2. casino regulatory-policy rebound where a theme exists but payout/capex/demand conversion is not durable enough,
3. travel-policy rebound where tourism keywords do not prove demand-to-margin and cash conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C31_R12L89_071320_DISTRICT_HEATING_TARIFF_VALUEUP","symbol":"071320","company_name":"지역난방공사","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"UTILITY_TARIFF_VALUEUP_POLICY_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-UtilityTariffValueupPolicyBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_low_MAE_policy_bridge","current_profile_verdict":"current_profile_correct_if_tariff_cost_recovery_capital_return_bridge_required","price_source":"Songdaiki/stock-web","notes":"Utility tariff/cost-recovery and value-up proxy produced very high MFE with controlled early MAE. Green still requires exact tariff, cost recovery, payout/capital-return and regulatory evidence."}
{"row_type":"case","case_id":"C31_R12L89_035250_KANGWON_CASINO_POLICY_REBOUND","symbol":"035250","company_name":"강원랜드","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CASINO_REGULATORY_POLICY_REBOUND_WITHOUT_DURABLE_PAYOUT_DEMAND_BRIDGE","case_type":"weak_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CasinoRegulatoryPolicyRebound-NoDurablePayoutDemandBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_moderate_MAE_no_policy_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_casino_policy_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Casino regulatory-policy rebound generated only low MFE and later drawdown without durable demand conversion, payout/capex or capital-return bridge."}
{"row_type":"case","case_id":"C31_R12L89_039130_HANA_TRAVEL_POLICY_REBOUND","symbol":"039130","company_name":"하나투어","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"TRAVEL_POLICY_REBOUND_WITHOUT_DEMAND_MARGIN_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-TravelPolicyRebound-NoDemandMarginCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_travel_policy_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Travel/tourism policy rebound had limited MFE and deep 180D MAE without durable demand conversion, margin mix and cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 071320 지역난방공사 — utility tariff / value-up policy bridge positive

Entry row: `2024-01-26 c=29000`.  
Observed path: early low `2024-01-26 l=27500`, strong policy/value-up rerating into `2024-02-26 h=51300`, and later full-window high `2024-06-18 h=53900`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L89_C31_071320_20240126_STAGE2_UTILITY_TARIFF_VALUEUP","case_id":"C31_R12L89_071320_DISTRICT_HEATING_TARIFF_VALUEUP","symbol":"071320","company_name":"지역난방공사","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"UTILITY_TARIFF_VALUEUP_POLICY_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-UtilityTariffValueupPolicyBridge-Positive","trigger_date":"2024-01-26","entry_date":"2024-01-26","entry_price":29000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_utility_tariff_cost_recovery_valueup_policy_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; tariff/cost recovery, regulated return and value-up/capital-return bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_policy_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["tariff_cost_recovery_proxy","regulated_return_proxy","valueup_policy_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_tariff_source_pending","cost_recovery_source_pending","payout_or_capital_return_pending","regulatory_certainty_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/071/071320/2024.csv","profile_path":"atlas/symbol_profiles/071/071320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":76.90,"MFE_90D_pct":76.90,"MFE_180D_pct":85.86,"MAE_30D_pct":-5.17,"MAE_90D_pct":-5.17,"MAE_180D_pct":-5.17,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":53900.0,"max_drawdown_low_date":"2024-01-26","max_drawdown_low":27500.0,"drawdown_after_peak_pct":-25.60,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_tariff_cost_recovery_and_capital_return_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_low_MAE_policy_bridge","current_profile_verdict":"current_profile_correct_if_tariff_cost_recovery_capital_return_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"071320_2024-01-26_29000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C31 can allow Stage2/Yellow when policy strength is tied to tariff cost recovery, regulated return, value-up/capital-return and regulatory certainty. Green still requires exact source-grade evidence."}
```

### 6.2 035250 강원랜드 — casino regulatory-policy rebound without durable payout/demand bridge

Entry row: `2024-02-06 c=16560`.  
Observed path: high `2024-02-20 h=18120`, later drawdown toward `2024-06-27 l=13720`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L89_C31_035250_20240206_STAGE2_FALSE_POSITIVE_CASINO_POLICY","case_id":"C31_R12L89_035250_KANGWON_CASINO_POLICY_REBOUND","symbol":"035250","company_name":"강원랜드","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CASINO_REGULATORY_POLICY_REBOUND_WITHOUT_DURABLE_PAYOUT_DEMAND_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-CasinoRegulatoryPolicyRebound-NoDurablePayoutDemandBridge","trigger_date":"2024-02-06","entry_date":"2024-02-06","entry_price":16560.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_casino_regulatory_policy_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; casino regulatory policy rebound treated as insufficient without durable visitor demand, capex scope, payout/capital-return and margin bridge","evidence_source_type":"historical_public_policy_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["casino_regulatory_policy_theme","tourism_recovery_keyword","relative_strength_rebound"],"stage3_evidence_fields":["durable_visitor_demand_missing","payout_capital_return_bridge_missing","capex_scope_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE_watch","policy_theme_bridge_missing","moderate_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035250/2024.csv","profile_path":"atlas/symbol_profiles/035/035250.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.42,"MFE_90D_pct":9.42,"MFE_180D_pct":9.42,"MAE_30D_pct":-2.42,"MAE_90D_pct":-11.78,"MAE_180D_pct":-17.15,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-20","peak_price":18120.0,"max_drawdown_low_date":"2024-06-27","max_drawdown_low":13720.0,"drawdown_after_peak_pct":-24.28,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"casino_policy_rebound_without_durable_payout_demand_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","policy_theme_bridge_missing","payout_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_moderate_MAE_no_policy_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_casino_policy_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"035250_2024-02-06_16560","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C31 should not promote casino regulatory-policy rebound without durable demand, payout/capital-return, capex scope, margin and cash bridge. Low MFE and later MAE require Watch/4B-risk."}
```

### 6.3 039130 하나투어 — travel/tourism policy rebound without demand-margin-cash bridge

Entry row: `2024-01-31 c=63700`.  
Observed path: high `2024-03-26 h=70600`, then low `2024-09-24 l=47300`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L89_C31_039130_20240131_STAGE2_FALSE_POSITIVE_TRAVEL_POLICY","case_id":"C31_R12L89_039130_HANA_TRAVEL_POLICY_REBOUND","symbol":"039130","company_name":"하나투어","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"TRAVEL_POLICY_REBOUND_WITHOUT_DEMAND_MARGIN_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-TravelPolicyRebound-NoDemandMarginCashBridge","trigger_date":"2024-01-31","entry_date":"2024-01-31","entry_price":63700.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_travel_tourism_policy_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; travel/tourism policy rebound treated as insufficient without durable outbound/inbound demand conversion, package ASP, margin mix and cash bridge","evidence_source_type":"historical_public_policy_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["travel_policy_rebound","tourism_reopening_keyword","relative_strength_turn"],"stage3_evidence_fields":["demand_conversion_missing","package_ASP_bridge_missing","margin_mix_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["low_MFE_watch","demand_margin_bridge_missing_watch","deep_180D_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039130/2024.csv","profile_path":"atlas/symbol_profiles/039/039130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.83,"MFE_90D_pct":10.83,"MFE_180D_pct":10.83,"MAE_30D_pct":-5.49,"MAE_90D_pct":-18.05,"MAE_180D_pct":-25.75,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-26","peak_price":70600.0,"max_drawdown_low_date":"2024-09-24","max_drawdown_low":47300.0,"drawdown_after_peak_pct":-33.00,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"travel_policy_rebound_without_demand_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","demand_margin_bridge_missing_watch","deep_180D_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_travel_policy_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"039130_2024-01-31_63700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C31 should not count tourism-policy rebound as positive without demand conversion, ASP/margin mix and cash bridge. Low MFE and deep 180D MAE require 4B-watch."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_R12L89_071320_DISTRICT_HEATING_TARIFF_VALUEUP","trigger_id":"R12L89_C31_071320_20240126_STAGE2_UTILITY_TARIFF_VALUEUP","symbol":"071320","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C31 requires tariff/cost recovery, regulated return, capital return, legal certainty and cash bridge rather than policy label alone","raw_component_scores_before":{"policy_specificity_score":13,"tariff_pass_through_score":14,"cost_recovery_score":14,"legal_certainty_score":10,"capital_return_score":10,"beneficiary_scope_score":9,"margin_cash_score":10,"relative_strength_score":15,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"policy_specificity_score":16,"tariff_pass_through_score":17,"cost_recovery_score":17,"legal_certainty_score":12,"capital_return_score":12,"beneficiary_scope_score":11,"margin_cash_score":12,"relative_strength_score":16,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":87,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Tariff/cost-recovery policy bridge and very high MFE support Yellow/Green-candidate watch; exact tariff/payout/regulatory evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_R12L89_035250_KANGWON_CASINO_POLICY_REBOUND","trigger_id":"R12L89_C31_035250_20240206_STAGE2_FALSE_POSITIVE_CASINO_POLICY","symbol":"035250","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_scope":"current_default_proxy","profile_hypothesis":"casino regulatory-policy rebound without payout/demand bridge should be blocked","raw_component_scores_before":{"policy_specificity_score":5,"tariff_pass_through_score":0,"cost_recovery_score":0,"legal_certainty_score":4,"capital_return_score":1,"beneficiary_scope_score":3,"margin_cash_score":1,"relative_strength_score":7,"execution_risk_score":-10,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"policy_specificity_score":2,"tariff_pass_through_score":0,"cost_recovery_score":0,"legal_certainty_score":1,"capital_return_score":0,"beneficiary_scope_score":1,"margin_cash_score":0,"relative_strength_score":2,"execution_risk_score":-16,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and missing durable demand/payout/margin bridge turn the casino policy rebound into weak bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_R12L89_039130_HANA_TRAVEL_POLICY_REBOUND","trigger_id":"R12L89_C31_039130_20240131_STAGE2_FALSE_POSITIVE_TRAVEL_POLICY","symbol":"039130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_scope":"current_default_proxy","profile_hypothesis":"travel/tourism policy rebound without demand-to-margin bridge should remain Watch/blocked","raw_component_scores_before":{"policy_specificity_score":4,"tariff_pass_through_score":0,"cost_recovery_score":0,"legal_certainty_score":2,"capital_return_score":0,"beneficiary_scope_score":4,"margin_cash_score":1,"relative_strength_score":7,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"policy_specificity_score":1,"tariff_pass_through_score":0,"cost_recovery_score":0,"legal_certainty_score":1,"capital_return_score":0,"beneficiary_scope_score":1,"margin_cash_score":0,"relative_strength_score":2,"execution_risk_score":-20,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Limited MFE and deep 180D MAE require demand conversion, ASP/margin and cash bridge before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R12L89_C31_P0_CURRENT","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C31 needs explicit policy-to-cash bridge and tourism/casino theme 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":32.38,"avg_MAE90_pct":-11.67,"avg_MFE180_pct":35.37,"avg_MAE180_pct":-16.02,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C31_policy_economic_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R12L89_C31_P1_SECTOR_SPECIFIC","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P1_L10_policy_economic_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L10 policy signals need tariff/subsidy pass-through, regulated return, legal certainty, beneficiary scope, capital return, margin or cash conversion before Stage2-Actionable","changed_axes":["policy_specificity_required","economic_pass_through_required","policy_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_tariff_subsidy_cost_recovery_legal_certainty_capital_return_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":32.38,"avg_MAE90_pct":-11.67,"avg_MFE180_pct":35.37,"avg_MAE180_pct":-16.02,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R12L89_C31_P2_CANONICAL","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P2_C31_policy_to_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C31 should reward policy-to-economics mechanics, not policy label or tourism/casino rebound labels","changed_axes":["C31_policy_to_cash_bridge_required","C31_tourism_casino_policy_theme_local_4B_guard","C31_low_MFE_policy_theme_guard"],"changed_thresholds":{"stage2_yellow_gate":"specific_policy_plus_pass_through_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":32.38,"avg_MAE90_pct":-11.67,"avg_MFE180_pct":35.37,"avg_MAE180_pct":-16.02,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R12L89_C31_P3_COUNTEREXAMPLE_GUARD","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P3_C31_low_MFE_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<12 and policy-to-cash bridge is missing, block Yellow/Green; if MAE180<=-25, route to 4B-watch even when policy theme is plausible","changed_axes":["C31_low_MFE_guardrail","C31_deep_180D_MAE_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_12_with_policy_cash_bridge_missing; MAE180_le_minus_25_with_bridge_missing"},"eligible_trigger_count":3,"avg_MFE90_pct":32.38,"avg_MAE90_pct":-11.67,"avg_MFE180_pct":35.37,"avg_MAE180_pct":-16.02,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_UTILITY_TARIFF_POSITIVE_VS_TOURISM_CASINO_POLICY_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":32.38,"avg_MAE90_pct":-11.67,"avg_MFE180_pct":35.37,"avg_MAE180_pct":-16.02,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_12":0.67,"stage2_bad_entry_rate_bridge_missing":0.67,"interpretation":"C31 needs policy-to-economics discipline. 지역난방공사 shows tariff/cost-recovery/value-up bridge can produce large MFE, while 강원랜드 and 하나투어 show casino/travel policy rebounds should not be promoted without durable demand, payout, margin and cash-conversion evidence."}
{"row_type":"stage_transition_summary","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"071320","trigger_type":"Stage2-Actionable-UtilityTariffValueupPolicyBridge-Positive","entry_date":"2024-01-26","stage2_to_90D_outcome":"good_stage2_very_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_policy_to_cash_rerating_with_Green_strictness","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when policy is tied to tariff/cost recovery, regulated return and capital-return bridge; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"035250","trigger_type":"Stage2-FalsePositive-CasinoRegulatoryPolicyRebound-NoDurablePayoutDemandBridge","entry_date":"2024-02-06","stage2_to_90D_outcome":"weak_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"casino_policy_rebound_decayed_without_demand_payout_bridge","MFE90_ge_20":false,"MAE180_le_minus_15":true,"transition_note":"Casino regulatory-policy rebound without demand/payout/margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"039130","trigger_type":"Stage2-FalsePositive-TravelPolicyRebound-NoDemandMarginCashBridge","entry_date":"2024-01-31","stage2_to_90D_outcome":"weak_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_travel_policy_rebound_deep_180D_MAE","MFE90_ge_20":false,"MAE180_le_minus_25":true,"transition_note":"Travel/tourism policy rebound without demand-to-margin and cash bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"tourism_casino_policy_theme_overcredit_without_policy_to_cash_bridge","contribution":"Adds two C31 local 4B/Watch counterexamples against one utility tariff/value-up policy positive, avoiding C31 top-covered and previous R12 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"UTILITY_TARIFF_VALUEUP_POLICY_BRIDGE_VS_CASINO_TRAVEL_POLICY_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C31 now has non-top-symbol utility tariff/value-up positive and two tourism/casino policy weak-bridge counterexamples; next R12 loops should exact-URL repair tariff/cost recovery, policy beneficiary scope, capital return, demand conversion, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","axis":"C31_policy_to_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"071320 worked when tariff/cost-recovery/value-up proxy existed; 035250 and 039130 were weak when policy label lacked durable demand, payout, margin and cash bridge."}
{"row_type":"shadow_weight","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","axis":"C31_tourism_casino_policy_theme_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Casino and travel-policy rows showed low MFE and later MAE expansion when non-price economics were missing."}
{"row_type":"shadow_weight","round":"R12","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","axis":"C31_low_MFE_policy_theme_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"035250 and 039130 show policy theme labels with MFE90 below 12 should not be promoted unless exact policy-to-cash bridge is repaired."}
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
  - tourism_policy_theme_overcredit
  - casino_policy_theme_overcredit
  - policy_to_cash_bridge_missing
  - demand_margin_cash_bridge_missing
new_axis_proposed:
  - C31_policy_to_cash_bridge_required_shadow_only
  - C31_tourism_casino_policy_theme_local_4B_guard_shadow_only
  - C31_low_MFE_policy_theme_guard_shadow_only
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
3. Confirm R12 / L10 / C31 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C31 top-covered symbols
   - previous R12 loop85 C31 symbols
   - previous R12 loop86 C32 symbols
   - previous R12 loop87 C31 symbols
   - previous R12 loop88 C32 symbols
6. Confirm accidentally touched R11/C02 candidate rows are not ingested from this MD.
7. If aggregate support remains stable after exact evidence URL repair, consider C31-scoped safe patch candidates:
   - C31_policy_to_cash_bridge_required
   - C31_tourism_casino_policy_theme_local_4B_guard
   - C31_low_MFE_policy_theme_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R12
completed_loop = 89
next_round = R13
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.
```
