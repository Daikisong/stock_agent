# E2R Stock-Web v12 Residual Research — R12 Loop 83 / L10 / C31

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R12
loop: 83
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: NUCLEAR_HYDROGEN_RENEWABLE_POLICY_EVENT_BRIDGE_VS_SUBSIDY_PRICE_SPIKE
sector: L10 policy/event + under-covered energy transition policy lane
output_file: e2r_stock_web_v12_residual_round_R12_loop_83_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after the latest completed `R11 loop 83` result.

```text
scheduled_round = R12
scheduled_loop = 83
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

R12 may use `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or relevant under-covered service/agri/policy lanes.  
This run chooses the L10 policy/event lane and tests whether policy/subsidy/legislation events become structural rerating only when they produce a contract, order, margin, or FCF bridge.

This is not a live stock recommendation, not a production patch, and not a scoring-profile change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"034020","company_name":"두산에너빌리티","profile_path":"atlas/symbol_profiles/034/034020.json","first_date":"2000-10-25","last_date":"2026-02-20","trading_day_count":6245,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2019-05-29","2020-02-18","2020-12-24"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"336260","company_name":"두산퓨얼셀","profile_path":"atlas/symbol_profiles/336/336260.json","first_date":"2019-10-18","last_date":"2026-02-20","trading_day_count":1556,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"009830","company_name":"한화솔루션","profile_path":"atlas/symbol_profiles/009/009830.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7741,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["1999-04-20","2008-07-04"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

The No-Repeat Index is used only as a duplicate-avoidance ledger.  
C31 is already well populated, so this run avoids the top-covered C31 symbols listed in the ledger, including `013990`, `003550`, `015760`, `032350`, `114090`, and `000270`.

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced here:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"034020","trigger_type":"Stage2-Actionable-NuclearPolicyProjectBridge-Positive","entry_date":"2024-03-11","duplicate_status":"new C31 symbol/trigger/date combination; not a C31 top-repeat symbol"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"336260","trigger_type":"Stage2-FalsePositive-HydrogenPolicySubsidySpike-NoOrderBridge","entry_date":"2024-05-22","duplicate_status":"new C31 symbol/trigger/date combination; hydrogen subsidy spike false-positive lane"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"009830","trigger_type":"Stage2-FalsePositive-SolarPolicyIRARebound-NoMarginBridge","entry_date":"2024-04-01","duplicate_status":"new C31 symbol/trigger/date combination; solar/IRA policy rebound high-MAE lane"}
```

## 4. Research question

Policy is only the spark. E2R should ask whether the spark lights a real furnace: contract conversion, customer order quality, margin bridge, or FCF path.

Residual question:

```text
Can C31 distinguish:
1. a policy event with visible industrial/project bridge,
2. a hydrogen subsidy theme spike with no order bridge,
3. a solar/IRA rebound spike that lacks margin and cash-flow conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C31_R12L83_034020_DOOSAN_ENERBILITY_NUCLEAR_POLICY_BRIDGE","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"NUCLEAR_POLICY_PROJECT_BRIDGE_WITH_ORDER_OPTIONALITY","symbol":"034020","company_name":"두산에너빌리티","case_role":"structural_success","case_summary":"Nuclear-policy/project event produced a strong forward MFE path from a Stage2 entry, but only after tolerating meaningful early MAE. Supports Stage2/Yellow policy bridge, not Green relaxation."}
{"row_type":"case","case_id":"C31_R12L83_336260_DOOSAN_FUELCELL_HYDROGEN_POLICY_SPIKE_NO_BRIDGE","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"HYDROGEN_POLICY_SUBSIDY_PRICE_SPIKE_WITHOUT_ORDER_BRIDGE","symbol":"336260","company_name":"두산퓨얼셀","case_role":"failed_rerating","case_summary":"Hydrogen policy/subsidy spike showed limited MFE and large 90/180D MAE, so policy optionality without customer/order bridge should stay Watch or 4B-risk."}
{"row_type":"case","case_id":"C31_R12L83_009830_HANWHA_SOLUTION_SOLAR_IRA_REBOUND_NO_MARGIN_BRIDGE","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"SOLAR_POLICY_IRA_REBOUND_WITH_MARGIN_BREAK","symbol":"009830","company_name":"한화솔루션","case_role":"failed_rerating","case_summary":"Solar/IRA rebound had an initial MFE but later collapsed into deep 180D MAE. Policy support did not overcome margin/spread and balance-sheet pressure."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 034020 두산에너빌리티 — nuclear policy/project bridge positive control

Entry row: `2024-03-11 c=16720`.  
Observed forward path: early drawdown to `2024-04-17 l=14320`, then policy/project repricing to `2024-07-18 h=25000`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L83_C31_034020_20240311_STAGE2_NUCLEAR_POLICY_PROJECT_BRIDGE","case_id":"C31_R12L83_034020_DOOSAN_ENERBILITY_NUCLEAR_POLICY_BRIDGE","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"NUCLEAR_POLICY_PROJECT_BRIDGE_WITH_ORDER_OPTIONALITY","sector":"policy/event; nuclear project linkage","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","symbol":"034020","company_name":"두산에너빌리티","trigger_type":"Stage2-Actionable-NuclearPolicyProjectBridge-Positive","trigger_date":"2024-03-11","evidence_available_at_that_date":"historical_public_policy_project_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; nuclear policy/project optionality treated as a non-price bridge proxy, not final citation-grade evidence","stage2_evidence_fields":["policy_or_regulatory_optionality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["repeat_order_or_conversion_pending","financial_visibility_pending","multiple_public_sources_pending"],"stage4b_evidence_fields":["price_only_local_peak_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv","profile_path":"atlas/symbol_profiles/034/034020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-11","entry_price":16720.0,"MFE_30D_pct":13.16,"MFE_90D_pct":49.52,"MFE_180D_pct":49.52,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.35,"MAE_90D_pct":-14.35,"MAE_180D_pct":-14.35,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":25000.0,"drawdown_after_peak_pct":-32.36,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_peak_watch_not_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_with_high_MAE_tolerance","current_profile_verdict":"current_profile_data_insufficient","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"034020_2024-03-11_16720","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C31 should allow Stage2/Yellow when policy optionality has project/order route, but early MAE means Green must require confirmed conversion and source-quality repair."}
```

### 6.2 336260 두산퓨얼셀 — hydrogen policy/subsidy spike without order bridge

Entry row: `2024-05-22 c=25000`.  
Observed forward path: small MFE to `2024-05-23 h=27300`, then high MAE to `2024-11-15 l=14100`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L83_C31_336260_20240522_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY_SPIKE","case_id":"C31_R12L83_336260_DOOSAN_FUELCELL_HYDROGEN_POLICY_SPIKE_NO_BRIDGE","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"HYDROGEN_POLICY_SUBSIDY_PRICE_SPIKE_WITHOUT_ORDER_BRIDGE","sector":"policy/event; hydrogen subsidy and green policy","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","symbol":"336260","company_name":"두산퓨얼셀","trigger_type":"Stage2-FalsePositive-HydrogenPolicySubsidySpike-NoOrderBridge","trigger_date":"2024-05-22","evidence_available_at_that_date":"historical_public_policy_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; hydrogen policy/subsidy narrative treated as insufficient unless order/revenue bridge is verified","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["repeat_order_or_conversion_missing","margin_bridge_missing","financial_visibility_missing"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336260/2024.csv","profile_path":"atlas/symbol_profiles/336/336260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-22","entry_price":25000.0,"MFE_30D_pct":9.2,"MFE_90D_pct":9.2,"MFE_180D_pct":9.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-21.2,"MAE_90D_pct":-27.92,"MAE_180D_pct":-43.6,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-23","peak_price":27300.0,"drawdown_after_peak_pct":-48.35,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_watch_timing_but_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"336260_2024-05-22_25000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Hydrogen policy/subsidy optionality alone would be over-credited. Require customer/order/revenue bridge before Stage2-Actionable or Yellow."}
```

### 6.3 009830 한화솔루션 — solar/IRA policy rebound without margin bridge

Entry row: `2024-04-01 c=29050`.  
Observed forward path: MFE reached `2024-05-28 h=34550`, but later collapsed to `2024-12-09 l=14860`.

```jsonl
{"row_type":"trigger","trigger_id":"R12L83_C31_009830_20240401_STAGE2_FALSE_POSITIVE_SOLAR_IRA_REBOUND","case_id":"C31_R12L83_009830_HANWHA_SOLUTION_SOLAR_IRA_REBOUND_NO_MARGIN_BRIDGE","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"SOLAR_POLICY_IRA_REBOUND_WITH_MARGIN_BREAK","sector":"policy/event; solar IRA subsidy and energy transition","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","symbol":"009830","company_name":"한화솔루션","trigger_type":"Stage2-FalsePositive-SolarPolicyIRARebound-NoMarginBridge","trigger_date":"2024-04-01","evidence_available_at_that_date":"historical_public_policy_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; solar/IRA support treated as insufficient without margin/spread and FCF bridge","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["margin_bridge_missing","financial_visibility_missing","low_red_team_risk_missing"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009830/2024.csv","profile_path":"atlas/symbol_profiles/009/009830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-01","entry_price":29050.0,"MFE_30D_pct":7.75,"MFE_90D_pct":18.93,"MFE_180D_pct":18.93,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.83,"MAE_90D_pct":-20.83,"MAE_180D_pct":-48.85,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-28","peak_price":34550.0,"drawdown_after_peak_pct":-56.99,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_4B_watch_should_activate_after_failed_margin_bridge","four_b_evidence_type":["margin_or_backlog_slowdown","price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MAE_after_initial_MFE","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"009830_2024-04-01_29050","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Solar/IRA policy rebound can look actionable but becomes false positive when margin/spread and cash-flow bridge fail. C31 needs a policy-to-economics bridge guard."}
```

## 7. Score simulation rows

These are proxy rows for calibration analysis only and do not change production scoring.

```jsonl
{"row_type":"score_simulation","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"034020","profile":"P0b_current_e2r_2_2_rolling_calibrated","eps_fcf_explosion":17,"earnings_visibility":15,"bottleneck_pricing":18,"market_mispricing":12,"valuation_rerating":11,"capital_allocation":3,"information_confidence":5,"raw_total_proxy":81,"weighted_total_proxy":76,"simulated_stage":"Stage2-Actionable/Stage3-Yellow-Watch","simulation_note":"Policy/project bridge exists, but early MAE and URL-pending evidence block Green relaxation."}
{"row_type":"score_simulation","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"336260","profile":"P0b_current_e2r_2_2_rolling_calibrated","eps_fcf_explosion":12,"earnings_visibility":9,"bottleneck_pricing":11,"market_mispricing":13,"valuation_rerating":7,"capital_allocation":3,"information_confidence":4,"raw_total_proxy":59,"weighted_total_proxy":57,"simulated_stage":"Stage2-Watch/FalsePositive","simulation_note":"Policy optionality without order bridge should not become actionable."}
{"row_type":"score_simulation","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"009830","profile":"P0b_current_e2r_2_2_rolling_calibrated","eps_fcf_explosion":11,"earnings_visibility":8,"bottleneck_pricing":10,"market_mispricing":14,"valuation_rerating":9,"capital_allocation":3,"information_confidence":4,"raw_total_proxy":59,"weighted_total_proxy":56,"simulated_stage":"Stage2-Watch/4B-risk","simulation_note":"Initial policy rebound was not durable; margin bridge and cash-flow evidence must be required."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R12L83_C31_P0_BASELINE","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile":"P0_e2r_2_0_baseline","profile_role":"rollback_reference","expected_error":"Would over-credit policy/subsidy headlines as Stage2 positives without verifying economics bridge."}
{"row_type":"profile_comparison","comparison_id":"R12L83_C31_P0B_CURRENT","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile":"P0b_e2r_2_2_rolling_calibrated","profile_role":"current_default_proxy","expected_error":"Global price-only guard helps, but C31 needs local policy-to-order/margin bridge requirement."}
{"row_type":"profile_comparison","comparison_id":"R12L83_C31_P1_POLICY_TO_ECONOMICS_BRIDGE","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile":"P1_shadow_C31_policy_to_economics_bridge","profile_role":"shadow_candidate","expected_effect":"Policy event is Watch unless at least one contract/order/margin/FCF bridge is present."}
{"row_type":"profile_comparison","comparison_id":"R12L83_C31_P2_SUBSIDY_SPIKE_GUARD","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile":"P2_shadow_C31_subsidy_spike_guard","profile_role":"shadow_candidate","expected_effect":"Hydrogen/solar subsidy spikes with MFE90<20 and MAE90<-20 remain Watch/4B-risk, not Yellow/Green."}
{"row_type":"profile_comparison","comparison_id":"R12L83_C31_P3_RECOMMENDED","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile":"P3_recommended_shadow_only","profile_role":"recommended_shadow_rule","expected_effect":"No production change; record C31 bridge and local 4B/high-MAE guard candidates for later batch planner."}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_EVENT_BRIDGE_VS_SUBSIDY_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":25.88,"avg_MAE90_pct":-21.03,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C31 policy events need local separation: nuclear/project bridge worked, while hydrogen and solar subsidy spikes produced high-MAE false positives."}
{"row_type":"stage_transition_summary","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"034020","trigger_type":"Stage2-Actionable-NuclearPolicyProjectBridge-Positive","entry_date":"2024-03-11","stage2_to_90D_outcome":"good_stage2_high_MFE_with_MAE_tolerance","stage2_to_180D_outcome":"positive_re_rating_path","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow only when policy route has project/order bridge; Green still requires confirmed economics."}
{"row_type":"stage_transition_summary","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"336260","trigger_type":"Stage2-FalsePositive-HydrogenPolicySubsidySpike-NoOrderBridge","entry_date":"2024-05-22","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"4B_watch_or_counterexample","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Policy/subsidy spike without order bridge should remain Watch."}
{"row_type":"stage_transition_summary","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"009830","trigger_type":"Stage2-FalsePositive-SolarPolicyIRARebound-NoMarginBridge","entry_date":"2024-04-01","stage2_to_90D_outcome":"bad_stage2_high_MAE_after_initial_MFE","stage2_to_180D_outcome":"failed_rerating_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Initial policy rally failed once margin/spread bridge broke."}
{"row_type":"residual_contribution","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"policy_event_bridge_vs_subsidy_spike_false_positive","contribution":"Adds one policy/project bridge positive and two subsidy-theme false positives, improving C31 local guardrail evidence beyond generic price-only rules.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_rows":3,"new_symbols":3,"new_positive":1,"new_counterexample":2,"new_4B_watch":2,"new_4C":0,"source_proxy_only":3,"evidence_url_pending":3,"calibration_usable":3,"next_gap":"Replace source-name proxies with exact policy/disclosure/report URLs before promotion; test under-covered agri/service policy lanes in future R12 loops."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","axis":"policy_to_economics_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"2/3 selected C31 policy/subsidy cases failed without order/margin/FCF bridge; require a bridge before Stage2-Actionable/Yellow."}
{"row_type":"shadow_weight","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","axis":"subsidy_theme_local_4b_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Hydrogen and solar subsidy spikes showed limited or unstable upside and deep MAE; treat as Watch/4B-risk without economics conversion."}
{"row_type":"shadow_weight","round":"R12","loop":"83","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","axis":"high_mae_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If C31 policy theme has MAE90<=-20 and no confirmed bridge, block Yellow/Green and route to evidence-quality repair."}
```

Interpretation:

```text
C31 should not read policy headlines as earnings power.
Policy is Stage2-Watch by default.
Policy becomes Stage2-Actionable/Yellow only when a real bridge appears:
- project/order route,
- customer/contract conversion,
- margin/spread improvement,
- FCF/cash conversion,
- or confirmed multi-source revision.
```

## 11. Data-quality caveat

All three cases use Stock-Web tradable raw OHLC rows and clean 2024 forward windows.  
However, the non-price evidence layer remains source-name/proxy level in this MD.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
promotion should prefer hold / data-quality repair until exact URLs are added
```

## 12. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not execute this handoff during the research-writing session.

When a later batch implementation is requested:
1. Ingest this MD through run-v12-calibration.
2. Confirm all trigger rows validate with price_data_source=Songdaiki/stock-web, price_basis=tradable_raw, price_adjustment_status=raw_unadjusted_marcap.
3. Confirm R12 / L10 / C31 round-sector consistency.
4. Check that C31 rows are not hard duplicates by canonical_archetype_id + symbol + trigger_type + entry_date.
5. If aggregate support remains stable after exact evidence URL repair, consider C31-scoped safe patch candidates:
   - policy_to_economics_bridge_required,
   - subsidy_theme_local_4b_watch_guard,
   - high_mae_guardrail when MAE90 <= -20 and bridge evidence is missing.
6. Do not loosen Stage3-Green. Do not use future MFE/MAE in runtime scoring. Use this only for calibration profile planning.
```

## 13. Round state

```text
completed_round = R12
completed_loop = 83
next_round = R13
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

## 14. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.
```
