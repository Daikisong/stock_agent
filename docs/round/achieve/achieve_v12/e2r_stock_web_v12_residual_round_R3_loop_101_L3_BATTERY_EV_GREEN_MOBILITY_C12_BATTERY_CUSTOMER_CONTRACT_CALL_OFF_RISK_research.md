---
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 101
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_TO_CASH_BRIDGE_VS_BATTERY_SUPPLY_CHAIN_LABEL_FALSE_POSITIVE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

# E2R Stock-Web v12 Residual Research — R3/L3/C12 Battery Customer Contract Call-off Risk

```text
output_file = e2r_stock_web_v12_residual_round_R3_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
selected_round = R3
selected_loop = 101
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_TO_CASH_BRIDGE_VS_BATTERY_SUPPLY_CHAIN_LABEL_FALSE_POSITIVE
```

## 1. Coverage-index selection

`V12_Research_No_Repeat_Index.md` places C12 at Priority 0 with 16 representative rows, 11 symbols, positives/counter 1/2, and 4B/4C 1/4. The current row count is below the 30-row Priority 0 floor, and the covered-symbol list already includes 005070, 020150, 078600, 121600, 003670, and 006400. This loop therefore avoids using those as the primary repeated C12 sample set and adds four C12-mapped symbols from adjacent battery customer-demand / utilization / call-off paths.

```text
selection_reason = C12 remains under-covered; call-off/utilization false-positive guard needs more stock-web path-confirmed rows.
selected_priority_bucket = Priority 0
same_canonical_archetype_research = allowed
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_count = 0
```

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","price_source":"Songdaiki/stock-web","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK"}
{"row_type":"price_source_validation","symbol":"348370","name":"엔켐","profile":"atlas/symbol_profiles/348/348370.json","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv","corporate_action_candidate_count":0,"has_major_raw_discontinuity":false,"calibration_caveat":"","calibration_usable":true}
{"row_type":"price_source_validation","symbol":"247540","name":"에코프로비엠","profile":"atlas/symbol_profiles/247/247540.json","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2022-06-27","2022-07-15"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate windows are outside 2024 entry-to-180D windows used here.","calibration_usable":true}
{"row_type":"price_source_validation","symbol":"361610","name":"SK아이이테크놀로지","profile":"atlas/symbol_profiles/361/361610.json","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv","corporate_action_candidate_count":0,"has_major_raw_discontinuity":false,"calibration_caveat":"","calibration_usable":true}
{"row_type":"price_source_validation","symbol":"278280","name":"천보","profile":"atlas/symbol_profiles/278/278280.json","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv","corporate_action_candidate_count":0,"has_major_raw_discontinuity":false,"calibration_caveat":"","calibration_usable":true}
```

## 3. Case thesis compression

C12 is not a generic “battery rebound” archetype. It is the narrower bridge from customer contract / offtake / call-off to actual utilization, shipment, margin, and cash conversion. A supplier can have a named customer, IRA/AMPC vocabulary, or capacity expansion language, but if customer call-off weakens, utilization falls, or inventory correction dominates, the price path should be treated as Stage4B/4C risk rather than Stage3 unlock.

The four cases below intentionally separate:

```text
1. massive MFE with unstable non-price bridge = price-only or event-cap local 4B
2. cathode demand slowdown = call-off risk / utilization break
3. separator utilization break = hard customer-demand counterexample
4. electrolyte/additive demand label with weak follow-through = false-positive counterexample
```

## 4. Machine-readable case rows

```jsonl
{"row_type":"case","case_id":"C12_R3_L101_CASE_001","symbol":"348370","name":"엔켐","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","case_role":"mixed_positive_local_4b_watch","trigger_family":"electrolyte_customer_capacity_label_to_utilization_cash_bridge","entry_date":"2024-01-15","entry_price":107000.0,"evidence_url_pending":true,"source_proxy_only":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C12_R3_L101_CASE_002","symbol":"247540","name":"에코프로비엠","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","case_role":"failed_rerating_calloff_counterexample","trigger_family":"cathode_customer_calloff_utilization_warning","entry_date":"2024-01-22","entry_price":248000.0,"evidence_url_pending":true,"source_proxy_only":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C12_R3_L101_CASE_003","symbol":"361610","name":"SK아이이테크놀로지","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","case_role":"failed_rerating_utilization_counterexample","trigger_family":"separator_customer_demand_slowdown_utilization_break","entry_date":"2024-01-15","entry_price":80100.0,"evidence_url_pending":true,"source_proxy_only":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C12_R3_L101_CASE_004","symbol":"278280","name":"천보","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","case_role":"failed_rerating_electrolyte_additive_counterexample","trigger_family":"electrolyte_additive_customer_recovery_label_without_calloff_followthrough","entry_date":"2024-02-21","entry_price":95600.0,"evidence_url_pending":true,"source_proxy_only":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

## 5. Trigger-level stock-web backtest rows

All `row_type="trigger"` rows below use canonical trigger labels only. Entry price is the stock-web close on `entry_date`. MFE/MAE use stock-web tradable daily high/low over 30/90/180 forward trading-day windows. Corporate-action candidate dates do not overlap the used entry-to-180D windows.

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C12_R3_L101_CASE_001","same_entry_group_id":"C12_348370_2024-01-15_Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","selected_round":"R3","selected_loop":101,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_TO_CASH_BRIDGE_VS_BATTERY_SUPPLY_CHAIN_LABEL_FALSE_POSITIVE","symbol":"348370","name":"엔켐","trigger_type":"Stage2-Actionable","trigger_family":"electrolyte_customer_capacity_label_to_utilization_cash_bridge","entry_date":"2024-01-15","entry_price":107000.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":235.05,"MAE_30D_pct":-6.36,"MFE_90D_pct":268.69,"MAE_90D_pct":-6.36,"MFE_180D_pct":268.69,"MAE_180D_pct":-6.36,"peak_180D_price":394500.0,"trough_180D_price":100200.0,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"case_role":"mixed_positive_local_4b_watch","profile_error_type":"price_success_but_current_profile_still_needs_non_price_calloff_cash_bridge","evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C12_R3_L101_CASE_002","same_entry_group_id":"C12_247540_2024-01-22_Stage4C","dedupe_for_aggregate":true,"aggregate_group_role":"representative","selected_round":"R3","selected_loop":101,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_TO_CASH_BRIDGE_VS_BATTERY_SUPPLY_CHAIN_LABEL_FALSE_POSITIVE","symbol":"247540","name":"에코프로비엠","trigger_type":"Stage4C","trigger_family":"cathode_customer_calloff_utilization_warning","entry_date":"2024-01-22","entry_price":248000.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":10.08,"MAE_30D_pct":-14.92,"MFE_90D_pct":10.08,"MAE_90D_pct":-26.81,"MFE_180D_pct":10.08,"MAE_180D_pct":-40.04,"peak_180D_price":273000.0,"trough_180D_price":148700.0,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"case_role":"failed_rerating_calloff_counterexample","profile_error_type":"battery_label_can_hold_stage2_too_long_without_calloff_utilization_break","evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C12_R3_L101_CASE_003","same_entry_group_id":"C12_361610_2024-01-15_Stage4C","dedupe_for_aggregate":true,"aggregate_group_role":"representative","selected_round":"R3","selected_loop":101,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_TO_CASH_BRIDGE_VS_BATTERY_SUPPLY_CHAIN_LABEL_FALSE_POSITIVE","symbol":"361610","name":"SK아이이테크놀로지","trigger_type":"Stage4C","trigger_family":"separator_customer_demand_slowdown_utilization_break","entry_date":"2024-01-15","entry_price":80100.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":1.75,"MAE_30D_pct":-18.73,"MFE_90D_pct":1.75,"MAE_90D_pct":-46.19,"MFE_180D_pct":1.75,"MAE_180D_pct":-62.48,"peak_180D_price":81500.0,"trough_180D_price":30050.0,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"case_role":"failed_rerating_utilization_counterexample","profile_error_type":"utilization_break_should_override_battery_customer_contract_vocabulary","evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C12_R3_L101_CASE_004","same_entry_group_id":"C12_278280_2024-02-21_Stage4B","dedupe_for_aggregate":true,"aggregate_group_role":"representative","selected_round":"R3","selected_loop":101,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_TO_CASH_BRIDGE_VS_BATTERY_SUPPLY_CHAIN_LABEL_FALSE_POSITIVE","symbol":"278280","name":"천보","trigger_type":"Stage4B","trigger_family":"electrolyte_additive_customer_recovery_label_without_calloff_followthrough","entry_date":"2024-02-21","entry_price":95600.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":3.35,"MAE_30D_pct":-13.70,"MFE_90D_pct":3.35,"MAE_90D_pct":-25.73,"MFE_180D_pct":3.35,"MAE_180D_pct":-59.78,"peak_180D_price":98800.0,"trough_180D_price":38450.0,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"case_role":"failed_rerating_electrolyte_additive_counterexample","profile_error_type":"weak_customer_calloff_followthrough_should_cap_stage2_actionable_bonus","evidence_url_pending":true,"source_proxy_only":true}
```

## 6. Score/return alignment and current profile stress test

```jsonl
{"row_type":"score_simulation","case_id":"C12_R3_L101_CASE_001","symbol":"348370","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"EPS_FCF":15,"Visibility":18,"Bottleneck":17,"MarketMispricing":15,"ValuationRunway":10,"CapitalAllocation":5,"InformationConfidence":8},"simulated_total":88,"current_profile_expected_stage":"Stage3-Yellow_or_Green_candidate_if_price_only_ignored","observed_path":"huge_MFE_then_local_4B_watch","alignment":"mixed","stress_test_result":"price-success exists, but non-price utilization/cash bridge must be mandatory before Green"}
{"row_type":"score_simulation","case_id":"C12_R3_L101_CASE_002","symbol":"247540","trigger_type":"Stage4C","raw_component_score_breakdown":{"EPS_FCF":6,"Visibility":8,"Bottleneck":10,"MarketMispricing":10,"ValuationRunway":8,"CapitalAllocation":6,"InformationConfidence":18},"simulated_total":66,"current_profile_expected_stage":"Stage2_or_watch_if_battery_beta_allowed","observed_path":"low_MFE_high_MAE_180D","alignment":"counterexample","stress_test_result":"customer call-off/utilization break should route to 4C or hard watch"}
{"row_type":"score_simulation","case_id":"C12_R3_L101_CASE_003","symbol":"361610","trigger_type":"Stage4C","raw_component_score_breakdown":{"EPS_FCF":5,"Visibility":8,"Bottleneck":9,"MarketMispricing":9,"ValuationRunway":7,"CapitalAllocation":5,"InformationConfidence":20},"simulated_total":63,"current_profile_expected_stage":"Stage2_recovery_watch_if_contract_label_overweighted","observed_path":"MFE nearly absent and MAE severe","alignment":"counterexample","stress_test_result":"utilization break must override separator/customer-label vocabulary"}
{"row_type":"score_simulation","case_id":"C12_R3_L101_CASE_004","symbol":"278280","trigger_type":"Stage4B","raw_component_score_breakdown":{"EPS_FCF":6,"Visibility":10,"Bottleneck":9,"MarketMispricing":11,"ValuationRunway":7,"CapitalAllocation":5,"InformationConfidence":20},"simulated_total":68,"current_profile_expected_stage":"Stage2_watch_if additive recovery label accepted","observed_path":"weak MFE and deep 180D MAE","alignment":"counterexample","stress_test_result":"recovery label without call-off shipment bridge should be capped at 4B/watch"}
```

## 7. Aggregate metric rows

```jsonl
{"row_type":"aggregate_metric","selected_round":"R3","selected_loop":101,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","representative_trigger_count":4,"calibration_usable_trigger_count":4,"mean_MFE_30D_pct":62.13,"mean_MAE_30D_pct":-13.43,"mean_MFE_90D_pct":70.97,"mean_MAE_90D_pct":-26.27,"mean_MFE_180D_pct":70.97,"mean_MAE_180D_pct":-42.17,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":3,"local_4b_watch_count":2,"current_profile_error_count":4}
{"row_type":"coverage_matrix","selected_round":"R3","selected_loop":101,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","prior_rows_from_no_repeat_index":16,"new_candidate_rows_if_accepted":4,"post_acceptance_rows_estimate":20,"still_priority_0":true,"rows_to_priority0_floor":10,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4}
```

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","selected_round":"R3","selected_loop":101,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"C12_customer_calloff_utilization_to_cash_bridge_required","direction":"strengthen","proposed_delta":{"InformationConfidence":3,"Visibility":2,"EPS_FCF":-1},"rationale":"C12 should not accept battery customer/contract vocabulary unless shipment, utilization, and cash conversion are visible."}
{"row_type":"shadow_weight","selected_round":"R3","selected_loop":101,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"C12_high_MAE_calloff_guard","direction":"strengthen","proposed_delta":{"InformationConfidence":4,"ValuationRunway":-2,"MarketMispricing":-1},"rationale":"C12 false positives show high 180D MAE when call-off or utilization breaks emerge after label-driven Stage2 watch."}
{"row_type":"shadow_weight","selected_round":"R3","selected_loop":101,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"price_only_blowoff_blocks_positive_stage","direction":"keep_and_specialize","existing_axis_strengthened":true,"rationale":"348370 demonstrates that even massive MFE should remain local-4B watch unless customer call-off and cash bridge are separately confirmed."}
```

## 9. Residual contribution

```jsonl
{"row_type":"residual_contribution","selected_round":"R3","selected_loop":101,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"C12_customer_calloff_utilization_to_cash_bridge_required | C12_high_MAE_calloff_guard","existing_axis_strengthened":"stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail","existing_axis_weakened":null,"current_profile_error_count":4,"do_not_propose_new_weight_delta":false}
{"row_type":"residual_contribution","selected_round":"R3","selected_loop":101,"summary":"This loop adds 4 new independent C12 cases, 3 counterexamples, and 4 residual errors for R3/L3/C12."}
```

## 10. Interpretation

C12 behaves like a weak bridge in an electrical circuit. The label wire can carry voltage for a while: customer name, contract phrase, IRA/AMPC policy word, or capacity expansion. But if the circuit does not close through call-off, utilization, shipment, margin, and cash conversion, the current does not reach earnings. In price-path terms, the stock may spark, but the arc burns out into high MAE.

The main residual error is not that E2R needs to become more bullish on battery recovery. It is the opposite: C12 needs a stricter bridge than a generic Stage2 battery label. C12 positive treatment should require customer call-off and utilization follow-through; otherwise the profile should prefer Stage4B watch or Stage4C when thesis break is explicit.

## 11. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 4
calibration_usable_trigger_count: 4
representative_trigger_count: 4
new_weight_evidence_candidate_count: 4
guardrail_candidate_count: 4
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 12. Final research state

```text
completed_round = R3
completed_loop = 101
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_TO_CASH_BRIDGE_VS_BATTERY_SUPPLY_CHAIN_LABEL_FALSE_POSITIVE
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 3
current_profile_error_count = 4
diversity_score_summary = Priority 0 C12 shortage fill; existing 005070/020150/078600/121600/003670/006400 C12 top rows avoided; 348370/247540/361610/278280 added as new C12 mapped symbols.
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
next_recommended_archetypes = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C02_POWER_GRID_DATACENTER_CAPEX, C18_CONSUMER_EXPORT_CHANNEL_REORDER, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

## 13. Deferred Coding Agent Handoff Prompt

```text
You are the later coding agent for Songdaiki/stock_agent. Do not rerun this research. Ingest this v12 standalone MD together with the other v12 residual research files. Validate only rows with row_type="trigger" and calibration_usable=true. Ensure canonical_archetype_id=C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK maps to R3/L3_BATTERY_EV_GREEN_MOBILITY. Candidate implementation axes: C12_customer_calloff_utilization_to_cash_bridge_required and C12_high_MAE_calloff_guard. Do not apply a production scoring change directly from this single file; batch it with the aggregate v12 pipeline and preserve rollback to the current calibrated profile.
```
