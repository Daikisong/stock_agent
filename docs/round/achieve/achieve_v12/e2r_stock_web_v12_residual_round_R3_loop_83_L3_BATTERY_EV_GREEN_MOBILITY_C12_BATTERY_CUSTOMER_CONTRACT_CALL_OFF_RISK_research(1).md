# E2R Stock-Web v12 Residual Research — R3 Loop 83 / L3 / C12

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R3
loop: 83
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: CUSTOMER_CALL_OFF_RISK_ELECTROLYTE_BRIDGE_VS_CATHODE_DEMAND_BREAK
sector: 배터리·EV·green mobility / customer contract call-off risk
output_file: e2r_stock_web_v12_residual_round_R3_loop_83_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-argue the global rules. It tests whether C12 battery customer-call-off risk needs a tighter canonical bridge guard after the already-calibrated profile.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R3
scheduled_loop = 83
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = CUSTOMER_CALL_OFF_RISK_ELECTROLYTE_BRIDGE_VS_CATHODE_DEMAND_BREAK
round_schedule_status = valid
round_sector_consistency = pass
```

R3 allows L3 battery/EV/green mobility. C12 is selected inside the scheduled round because the No-Repeat snapshot shows C12 has many rows but still a useful residual: customer/offtake headlines can look like Stage2, while actual call-off/demand/margin paths can produce deep MAE.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index is used only as a duplicate-avoidance ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected novelty:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"348370","trigger_type":"Stage2-Actionable-Electrolyte-ContractBridge-CalloffRiskOverruled","entry_date":"2024-01-12","duplicate_status":"soft_reuse_positive_control; do not over-weight; used to contrast bridge-positive electrolyte path against new cathode failures"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"066970","trigger_type":"Stage2-FalsePositive-Cathode-Offtake-CallOff-NoMarginBridge","entry_date":"2024-03-22","duplicate_status":"new_symbol_for_C12; new failure mode and trigger family"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"003670","trigger_type":"Stage2-FalsePositive-Cathode-Orderbook-CallOff-DemandBreak","entry_date":"2024-03-22","duplicate_status":"new_symbol_for_C12; new failure mode and trigger family"}
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"348370","company_name":"엔켐","profile_path":"atlas/symbol_profiles/348/348370.json","first_date":"2021-11-01","last_date":"2026-02-20","trading_day_count":1053,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"066970","company_name":"엘앤에프","profile_path":"atlas/symbol_profiles/066/066970.json","first_date":"2003-01-02","last_date":"2026-02-20","trading_day_count":5711,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2016-02-19","2021-08-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates are outside the 2024 selected forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"003670","company_name":"포스코퓨처엠","profile_path":"atlas/symbol_profiles/003/003670.json","first_date":"2001-11-01","last_date":"2026-02-20","trading_day_count":5985,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2015-05-04","2021-02-03"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates are outside the 2024 selected forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 5. Historical Eligibility Gate

All three representative trigger rows satisfy the price-path gate:

```text
entry_date exists in tradable shard = true
forward_180D_available_by_manifest_max_date = true
MFE/MAE 30D/90D/180D computed = true
corporate_action_contaminated_180D_window = false
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

The evidence layer is intentionally conservative:

```text
evidence_url_pending = true
source_proxy_only = true
promotion implication = hold or data-quality repair before any production patch
```

## 6. Canonical Archetype Compression Map

```text
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
  ├─ ELECTROLYTE_CUSTOMER_LOCALIZATION_CONTRACT_BRIDGE_CALL_OFF_RISK_OVERRULED
  ├─ CATHODE_OFFTAKE_PRICE_DOWN_CUSTOMER_CALL_OFF_BREAK
  └─ CATHODE_ORDERBOOK_CALL_OFF_RISK_WITH_UTILIZATION_DEMAND_BREAK
```

The compression point is simple: C12 should not punish every battery supply-chain name. It should separate electrolyte/localization demand bridge from cathode orderbook headlines where customer call-off, utilization and margin visibility are missing.

## 7. Case Selection Summary

```jsonl
{"row_type":"case","case_id":"C12_R3L83_348370_ENCHEM_ELECTROLYTE_CONTRACT_BRIDGE","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ELECTROLYTE_CUSTOMER_LOCALIZATION_CONTRACT_BRIDGE_CALL_OFF_RISK_OVERRULED","symbol":"348370","company_name":"엔켐","case_type":"structural_success","positive_or_counterexample":"positive","case_role":"positive_structural_success_soft_reuse","best_trigger":"Stage2-Actionable-Electrolyte-ContractBridge-CalloffRiskOverruled","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"C12 top-covered symbol in No-Repeat Index; reused only as positive control with different trigger-family framing against new cathode counterexamples.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"score_price_alignment":"positive high-MFE / low initial MAE, but later requires valuation 4B watch","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C12_R3L83_066970_LNF_CATHODE_OFFTAKE_CALL_OFF_BREAK","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_OFFTAKE_PRICE_DOWN_CUSTOMER_CALL_OFF_BREAK","symbol":"066970","company_name":"엘앤에프","case_type":"failed_rerating","positive_or_counterexample":"counterexample","case_role":"new_counterexample","best_trigger":"Stage2-FalsePositive-Cathode-Offtake-CallOff-NoMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"low-MFE / high-MAE false positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C12_R3L83_003670_POSCOFUTUREM_ORDERBOOK_CALL_OFF_RISK","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_ORDERBOOK_CALL_OFF_RISK_WITH_UTILIZATION_DEMAND_BREAK","symbol":"003670","company_name":"포스코퓨처엠","case_type":"failed_rerating","positive_or_counterexample":"counterexample","case_role":"new_counterexample","best_trigger":"Stage2-FalsePositive-Cathode-Orderbook-CallOff-DemandBreak","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"low-MFE / high-MAE false positive","current_profile_verdict":"current_profile_false_positive"}
```

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
calibration_usable_case_count = 3
new_independent_case_count = 2
reused_case_count = 1
new_independent_case_ratio = 0.67
```

The positive is deliberately a soft-reused control, not a new overweighted signal. The two new independent rows are C12 cathode/offtake failure modes.

## 9. Evidence Source Map

| symbol | evidence mode | stage2 bridge | stage3 bridge | 4B/4C risk |
|---|---|---|---|---|
| 348370 | source-name proxy | customer/localization bridge | partial repeat conversion proxy | valuation/positioning 4B watch |
| 066970 | source-name proxy | weak offtake headline | missing margin/revision bridge | call-off / demand break |
| 003670 | source-name proxy | orderbook headline | missing utilization bridge | call-off / demand break |

## 10. Price Data Source Map

| symbol | profile | shard | entry |
|---|---|---|---|
| 348370 | `atlas/symbol_profiles/348/348370.json` | `atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv` | 2024-01-12 close 93,100 |
| 066970 | `atlas/symbol_profiles/066/066970.json` | `atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv` | 2024-03-22 close 186,100 |
| 003670 | `atlas/symbol_profiles/003/003670.json` | `atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv` | 2024-03-22 close 318,500 |

## 11. Case-by-Case Trigger Grid

| symbol | trigger_type | entry | MFE90 | MAE90 | outcome |
|---|---|---:|---:|---:|---|
| 348370 | Stage2-Actionable-Electrolyte-ContractBridge-CalloffRiskOverruled | 93,100 | 323.74% | -2.04% | positive bridge, later 4B watch |
| 066970 | Stage2-FalsePositive-Cathode-Offtake-CallOff-NoMarginBridge | 186,100 | 6.93% | -41.32% | false positive / high MAE |
| 003670 | Stage2-FalsePositive-Cathode-Orderbook-CallOff-DemandBreak | 318,500 | 2.20% | -24.18% | false positive / high MAE |

## 12. Trigger-Level OHLC Backtest Tables

```jsonl
{"row_type":"trigger","trigger_id":"R3L83_C12_348370_20240112_STAGE2_ELECTROLYTE_CONTRACT_BRIDGE","case_id":"C12_R3L83_348370_ENCHEM_ELECTROLYTE_CONTRACT_BRIDGE","symbol":"348370","company_name":"엔켐","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ELECTROLYTE_CUSTOMER_LOCALIZATION_CONTRACT_BRIDGE_CALL_OFF_RISK_OVERRULED","sector":"battery electrolyte / customer localization","primary_archetype":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","loop_objective":"holdout_validation;sector_specific_rule_discovery;4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable-Electrolyte-ContractBridge-CalloffRiskOverruled","trigger_date":"2024-01-12","entry_date":"2024-01-12","entry_price":93100.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_event_proxy; exact URL pending","evidence_source":"source-name-level proxy for electrolyte localization/customer demand bridge; used as positive control only, not URL-grade promotion evidence","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["repeat_order_or_conversion","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv","profile_path":"atlas/symbol_profiles/348/348370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":285.07,"MFE_90D_pct":323.74,"MFE_180D_pct":323.74,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.04,"MAE_90D_pct":-2.04,"MAE_180D_pct":-2.04,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-04-08","peak_price":394500.0,"drawdown_after_peak_pct":-55.13,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_overheat_confirmed","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_low_initial_MAE_but_4B_watch_needed","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"348370_2024-01-12_93100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"soft reuse as positive control; different trigger family framing for C12 bridge-vs-calloff contrast","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L83_C12_066970_20240322_STAGE2_FALSE_POSITIVE_CATHODE_CALLOFF","case_id":"C12_R3L83_066970_LNF_CATHODE_OFFTAKE_CALL_OFF_BREAK","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_OFFTAKE_PRICE_DOWN_CUSTOMER_CALL_OFF_BREAK","sector":"battery cathode / customer offtake risk","primary_archetype":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-Cathode-Offtake-CallOff-NoMarginBridge","trigger_date":"2024-03-22","entry_date":"2024-03-22","entry_price":186100.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_event_proxy; exact URL pending","evidence_source":"source-name-level proxy for cathode offtake / EV demand / customer call-off risk; exact URL pending","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["customer_or_order_quality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.93,"MFE_90D_pct":6.93,"MFE_180D_pct":6.93,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.45,"MAE_90D_pct":-41.32,"MAE_180D_pct":-54.06,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":199000.0,"drawdown_after_peak_pct":-57.04,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"price_only_local_4B_too_early_without_non_price_bridge","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"066970_2024-03-22_186100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L83_C12_003670_20240322_STAGE2_FALSE_POSITIVE_ORDERBOOK_CALLOFF","case_id":"C12_R3L83_003670_POSCOFUTUREM_ORDERBOOK_CALL_OFF_RISK","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_ORDERBOOK_CALL_OFF_RISK_WITH_UTILIZATION_DEMAND_BREAK","sector":"battery cathode / orderbook utilization risk","primary_archetype":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","loop_objective":"residual_false_positive_mining;yellow_threshold_stress_test;counterexample_mining","trigger_type":"Stage2-FalsePositive-Cathode-Orderbook-CallOff-DemandBreak","trigger_date":"2024-03-22","entry_date":"2024-03-22","entry_price":318500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_event_proxy; exact URL pending","evidence_source":"source-name-level proxy for cathode orderbook/utilization/demand-break risk; exact URL pending","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.2,"MFE_90D_pct":2.2,"MFE_180D_pct":2.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-22.29,"MAE_90D_pct":-24.18,"MAE_180D_pct":-51.4,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":325500.0,"drawdown_after_peak_pct":-52.44,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"watch_or_4C_risk_before_positive_stage","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"003670_2024-03-22_318500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

## 13. Current Calibrated Profile Stress Test

```text
1. Current profile likely allows 348370 as Stage2/Yellow watch because non-price bridge proxy exists. Actual path validates the early signal but also demands 4B overlay.
2. Current profile can still be too early for cathode orderbook/offtake headlines in 066970 and 003670 if margin/revision/utilization bridge is absent.
3. Stage2 actionable bonus is not globally wrong; C12 needs bridge scoping.
4. Yellow threshold 75 is adequate if C12 risk fields reduce bridge credit.
5. Green threshold 87 / revision 55 should not be loosened.
6. price-only blowoff guard is strengthened, not weakened.
7. full 4B non-price requirement remains correct.
8. hard 4C routing should remain thesis-break based; these rows support earlier watch rather than automatic 4C.
```

Verdicts:

```jsonl
{"row_type":"narrative_only","symbol":"348370","current_profile_verdict":"current_profile_correct","reason":"positive bridge but 4B overlay needed after extreme MFE"}
{"row_type":"narrative_only","symbol":"066970","current_profile_verdict":"current_profile_false_positive","reason":"low MFE / high MAE after weak bridge"}
{"row_type":"narrative_only","symbol":"003670","current_profile_verdict":"current_profile_false_positive","reason":"orderbook headline did not protect against customer demand/utilization break"}
```

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is asserted from hindsight. Green lateness is therefore:

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C12 conclusion:

```text
Stage2/Yellow can be valid for electrolyte/localization bridge.
Stage2/Yellow should be blocked for cathode/offtake/orderbook headlines if customer demand, utilization, margin and revision bridge are missing.
Stage3-Green should not be relaxed.
```

## 15. 4B Local vs Full-window Timing Audit

| symbol | local/full peak issue | verdict |
|---|---|---|
| 348370 | full-window peak reached after large positive rerating | good full-window 4B timing if non-price overheat confirms |
| 066970 | local high immediately after entry, then persistent drawdown | price-only local 4B too early; better classified as call-off risk watch |
| 003670 | small local high, then prolonged drawdown | watch/4C-risk before positive stage |

## 16. 4C Protection Audit

```text
348370 = not_applicable for hard 4C; positive path later needs 4B watch
066970 = thesis_break_watch_only; hard 4C not asserted without exact evidence URL
003670 = thesis_break_watch_only; hard 4C not asserted without exact evidence URL
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

This is not broad L3 relaxation/tightening. It is a C12-specific bridge rule.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
new_axis_proposed = C12_customer_calloff_bridge_required_shadow_only
```

Candidate rule:

```text
If C12 and evidence is cathode/offtake/orderbook headline only:
    require customer demand + utilization + margin/revision bridge
    else route to Stage2-Watch / 4C-risk-watch

If historical calibration shows MFE90 < 10 and MAE90 <= -20:
    strengthen C12 high-MAE guard
    do not promote Yellow/Green without exact non-price bridge evidence
```

## 19. Before / After Backtest Comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R3L83_C12_P0_CURRENT","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_role":"current_default_proxy","expected_error":"Still can over-credit cathode order/offtake headlines when customer call-off and margin bridge are not separated."}
{"row_type":"profile_comparison","comparison_id":"R3L83_C12_P1_BRIDGE_REQUIRED","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile":"P1_shadow_C12_customer_calloff_bridge_required","profile_role":"shadow_candidate","expected_effect":"Require confirmed customer demand, utilization and margin/revision bridge before Stage2/Yellow."}
{"row_type":"profile_comparison","comparison_id":"R3L83_C12_P2_HIGH_MAE_GUARD","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile":"P2_shadow_C12_MAE90_guard","profile_role":"shadow_candidate","expected_effect":"If MFE90 is under 10 and MAE90 is below -20, move from Stage2-Actionable to Watch/4C-risk unless exact non-price bridge exists."}
{"row_type":"profile_comparison","comparison_id":"R3L83_C12_P3_RECOMMENDED","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile":"P3_recommended_shadow_only","profile_role":"recommended_shadow_rule","expected_effect":"No production change now; add canonical C12 bridge-required + high-MAE guard candidate for later batch planner."}
```

## 20. Score-Return Alignment Matrix

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_R3L83_348370_ENCHEM_ELECTROLYTE_CONTRACT_BRIDGE","trigger_id":"R3L83_C12_348370_20240112_STAGE2_ELECTROLYTE_CONTRACT_BRIDGE","symbol":"348370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":10,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":18,"customer_quality_score":14,"policy_or_regulatory_score":4,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"contract_score":13,"backlog_visibility_score":11,"margin_bridge_score":9,"revision_score":11,"relative_strength_score":18,"customer_quality_score":15,"policy_or_regulatory_score":4,"valuation_repricing_score":10,"execution_risk_score":9,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_after":83,"stage_label_after":"Stage2-Actionable/Yellow-Watch-with-4B-overlay","changed_components":["customer_quality_score","+1","margin_bridge_score","+1","valuation_repricing_score","-2"],"component_delta_explanation":"Positive bridge is allowed, but post-peak drawdown means C12 must keep 4B watch once valuation/positioning overheats.","MFE_90D_pct":323.74,"MAE_90D_pct":-2.04,"score_return_alignment_label":"aligned_positive_but_requires_4B_watch","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_R3L83_066970_LNF_CATHODE_OFFTAKE_CALL_OFF_BREAK","trigger_id":"R3L83_C12_066970_20240322_STAGE2_FALSE_POSITIVE_CATHODE_CALLOFF","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":13,"customer_quality_score":7,"policy_or_regulatory_score":2,"valuation_repricing_score":10,"execution_risk_score":14,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable false positive risk","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":5,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":6,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":6,"execution_risk_score":18,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-Watch/4C-risk-watch","changed_components":["contract_score","-3","backlog_visibility_score","-5","relative_strength_score","-7","execution_risk_score","+4"],"component_delta_explanation":"Call-off/cathode demand risk should remove Stage2 bridge credit when margin/revision evidence is absent and MAE90 is deeply negative.","MFE_90D_pct":6.93,"MAE_90D_pct":-41.32,"score_return_alignment_label":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_R3L83_003670_POSCOFUTUREM_ORDERBOOK_CALL_OFF_RISK","trigger_id":"R3L83_C12_003670_20240322_STAGE2_FALSE_POSITIVE_ORDERBOOK_CALLOFF","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":12,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":11,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":9,"execution_risk_score":13,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable false positive risk","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":6,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":18,"legal_or_contract_risk_score":7,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_after":60,"stage_label_after":"Stage2-Watch/4C-risk-watch","changed_components":["backlog_visibility_score","-6","customer_quality_score","-4","execution_risk_score","+5"],"component_delta_explanation":"Orderbook headline without utilization/margin bridge behaves like C12 call-off risk; Yellow/Green should be blocked.","MFE_90D_pct":2.2,"MAE_90D_pct":-24.18,"score_return_alignment_label":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive"}
```

## 21. Coverage Matrix

```jsonl
{"row_type":"coverage_matrix","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CUSTOMER_CALL_OFF_RISK_ELECTROLYTE_BRIDGE_VS_CATHODE_DEMAND_BREAK","positive_case_count":1,"counterexample_count":2,"4B_case_count":1,"4C_case_count":0,"new_independent_case_count":2,"reused_case_count":1,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"Still needs exact URL repair and additional non-cathode positive cases outside reused 348370."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 2
reused_case_count: 1
reused_case_ids: C12_R3L83_348370_ENCHEM_ELECTROLYTE_CONTRACT_BRIDGE
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
residual_error_types_found: C12_cathode_orderbook_false_positive; C12_calloff_high_MAE_tail; C12_positive_bridge_needs_4B_overlay
new_axis_proposed: C12_customer_calloff_bridge_required_shadow_only; C12_high_MAE_guardrail_shadow_only
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage within C12; full_4b_requires_non_price_evidence within C12
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min; stage3_green_revision_min; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 2 new independent cases, 2 counterexamples, and 2 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-Web profile rows
- Stock-Web tradable raw OHLC rows
- entry_date / entry_price
- MFE / MAE / peak / drawdown
- clean 180D forward windows
- scheduled round and sector consistency
- no-repeat duplicate avoidance at key level
```

Non-validation scope:

```text
- exact external evidence URLs are not resolved in this MD
- production scoring is not changed
- live candidate discovery is not performed
- broker/API/trading is not touched
```

## 24. Shadow Weight Calibration

```jsonl
{"row_type":"shadow_weight","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"stage2_required_bridge","scope":"canonical_archetype","baseline_value":0,"tested_value":1,"delta":"+1 guard","reason":"Cathode/offtake orderbook headlines produced two high-MAE false positives; require customer demand + utilization + margin/revision bridge.","backtest_effect":"066970 and 003670 would remain Watch instead of Stage2-Actionable; 348370 positive control remains allowed but with 4B overlay.","trigger_ids":"R3L83_C12_066970_20240322_STAGE2_FALSE_POSITIVE_CATHODE_CALLOFF|R3L83_C12_003670_20240322_STAGE2_FALSE_POSITIVE_ORDERBOOK_CALLOFF|R3L83_C12_348370_20240112_STAGE2_ELECTROLYTE_CONTRACT_BRIDGE","calibration_usable_count":3,"new_independent_case_count":2,"counterexample_count":2,"confidence":"medium_low_due_source_proxy","proposal_type":"canonical_archetype_shadow_only","notes":"not production; post-calibrated residual"}
{"row_type":"shadow_weight","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"high_mae_guardrail","scope":"canonical_archetype","baseline_value":0,"tested_value":1,"delta":"+1 risk guard","reason":"MFE90 < 10 and MAE90 <= -20 separated failed cathode cases from electrolyte positive bridge.","backtest_effect":"Blocks Yellow/Green for C12 cathode cases until exact non-price bridge is verified.","trigger_ids":"R3L83_C12_066970_20240322_STAGE2_FALSE_POSITIVE_CATHODE_CALLOFF|R3L83_C12_003670_20240322_STAGE2_FALSE_POSITIVE_ORDERBOOK_CALLOFF","calibration_usable_count":2,"new_independent_case_count":2,"counterexample_count":2,"confidence":"medium","proposal_type":"canonical_archetype_shadow_only","notes":"not production; high-MAE calibration only"}
{"row_type":"shadow_weight","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"local_4b_watch_guard","scope":"canonical_archetype","baseline_value":0,"tested_value":1,"delta":"+1 watch","reason":"Even positive C12 electrolyte bridge became valuation/positioning overheat after extreme MFE; full 4B still requires non-price evidence.","backtest_effect":"Keeps 348370 positive Stage2/Yellow but adds 4B watch once full-window peak proximity is high.","trigger_ids":"R3L83_C12_348370_20240112_STAGE2_ELECTROLYTE_CONTRACT_BRIDGE","calibration_usable_count":1,"new_independent_case_count":0,"counterexample_count":0,"confidence":"low_due_soft_reuse","proposal_type":"canonical_archetype_shadow_only","notes":"not production; positive control is reused so weight should be capped"}
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"348370","company_name":"엔켐","profile_path":"atlas/symbol_profiles/348/348370.json","first_date":"2021-11-01","last_date":"2026-02-20","trading_day_count":1053,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"066970","company_name":"엘앤에프","profile_path":"atlas/symbol_profiles/066/066970.json","first_date":"2003-01-02","last_date":"2026-02-20","trading_day_count":5711,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2016-02-19","2021-08-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates are outside the 2024 selected forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"003670","company_name":"포스코퓨처엠","profile_path":"atlas/symbol_profiles/003/003670.json","first_date":"2001-11-01","last_date":"2026-02-20","trading_day_count":5985,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2015-05-04","2021-02-03"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates are outside the 2024 selected forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C12_R3L83_348370_ENCHEM_ELECTROLYTE_CONTRACT_BRIDGE","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ELECTROLYTE_CUSTOMER_LOCALIZATION_CONTRACT_BRIDGE_CALL_OFF_RISK_OVERRULED","symbol":"348370","company_name":"엔켐","case_type":"structural_success","positive_or_counterexample":"positive","case_role":"positive_structural_success_soft_reuse","best_trigger":"Stage2-Actionable-Electrolyte-ContractBridge-CalloffRiskOverruled","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"C12 top-covered symbol in No-Repeat Index; reused only as positive control with different trigger-family framing against new cathode counterexamples.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"score_price_alignment":"positive high-MFE / low initial MAE, but later requires valuation 4B watch","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C12_R3L83_066970_LNF_CATHODE_OFFTAKE_CALL_OFF_BREAK","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_OFFTAKE_PRICE_DOWN_CUSTOMER_CALL_OFF_BREAK","symbol":"066970","company_name":"엘앤에프","case_type":"failed_rerating","positive_or_counterexample":"counterexample","case_role":"new_counterexample","best_trigger":"Stage2-FalsePositive-Cathode-Offtake-CallOff-NoMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"low-MFE / high-MAE false positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C12_R3L83_003670_POSCOFUTUREM_ORDERBOOK_CALL_OFF_RISK","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_ORDERBOOK_CALL_OFF_RISK_WITH_UTILIZATION_DEMAND_BREAK","symbol":"003670","company_name":"포스코퓨처엠","case_type":"failed_rerating","positive_or_counterexample":"counterexample","case_role":"new_counterexample","best_trigger":"Stage2-FalsePositive-Cathode-Orderbook-CallOff-DemandBreak","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"low-MFE / high-MAE false positive","current_profile_verdict":"current_profile_false_positive"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R3L83_C12_348370_20240112_STAGE2_ELECTROLYTE_CONTRACT_BRIDGE","case_id":"C12_R3L83_348370_ENCHEM_ELECTROLYTE_CONTRACT_BRIDGE","symbol":"348370","company_name":"엔켐","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ELECTROLYTE_CUSTOMER_LOCALIZATION_CONTRACT_BRIDGE_CALL_OFF_RISK_OVERRULED","sector":"battery electrolyte / customer localization","primary_archetype":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","loop_objective":"holdout_validation;sector_specific_rule_discovery;4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable-Electrolyte-ContractBridge-CalloffRiskOverruled","trigger_date":"2024-01-12","entry_date":"2024-01-12","entry_price":93100.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_event_proxy; exact URL pending","evidence_source":"source-name-level proxy for electrolyte localization/customer demand bridge; used as positive control only, not URL-grade promotion evidence","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["repeat_order_or_conversion","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv","profile_path":"atlas/symbol_profiles/348/348370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":285.07,"MFE_90D_pct":323.74,"MFE_180D_pct":323.74,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.04,"MAE_90D_pct":-2.04,"MAE_180D_pct":-2.04,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-04-08","peak_price":394500.0,"drawdown_after_peak_pct":-55.13,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_overheat_confirmed","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_low_initial_MAE_but_4B_watch_needed","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"348370_2024-01-12_93100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"soft reuse as positive control; different trigger family framing for C12 bridge-vs-calloff contrast","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L83_C12_066970_20240322_STAGE2_FALSE_POSITIVE_CATHODE_CALLOFF","case_id":"C12_R3L83_066970_LNF_CATHODE_OFFTAKE_CALL_OFF_BREAK","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_OFFTAKE_PRICE_DOWN_CUSTOMER_CALL_OFF_BREAK","sector":"battery cathode / customer offtake risk","primary_archetype":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-Cathode-Offtake-CallOff-NoMarginBridge","trigger_date":"2024-03-22","entry_date":"2024-03-22","entry_price":186100.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_event_proxy; exact URL pending","evidence_source":"source-name-level proxy for cathode offtake / EV demand / customer call-off risk; exact URL pending","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["customer_or_order_quality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.93,"MFE_90D_pct":6.93,"MFE_180D_pct":6.93,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.45,"MAE_90D_pct":-41.32,"MAE_180D_pct":-54.06,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":199000.0,"drawdown_after_peak_pct":-57.04,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"price_only_local_4B_too_early_without_non_price_bridge","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"066970_2024-03-22_186100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L83_C12_003670_20240322_STAGE2_FALSE_POSITIVE_ORDERBOOK_CALLOFF","case_id":"C12_R3L83_003670_POSCOFUTUREM_ORDERBOOK_CALL_OFF_RISK","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_ORDERBOOK_CALL_OFF_RISK_WITH_UTILIZATION_DEMAND_BREAK","sector":"battery cathode / orderbook utilization risk","primary_archetype":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","loop_objective":"residual_false_positive_mining;yellow_threshold_stress_test;counterexample_mining","trigger_type":"Stage2-FalsePositive-Cathode-Orderbook-CallOff-DemandBreak","trigger_date":"2024-03-22","entry_date":"2024-03-22","entry_price":318500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_event_proxy; exact URL pending","evidence_source":"source-name-level proxy for cathode orderbook/utilization/demand-break risk; exact URL pending","evidence_url_pending":true,"source_proxy_only":true,"stage2_evidence_fields":["customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.2,"MFE_90D_pct":2.2,"MFE_180D_pct":2.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-22.29,"MAE_90D_pct":-24.18,"MAE_180D_pct":-51.4,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":325500.0,"drawdown_after_peak_pct":-52.44,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"watch_or_4C_risk_before_positive_stage","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"003670_2024-03-22_318500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_R3L83_348370_ENCHEM_ELECTROLYTE_CONTRACT_BRIDGE","trigger_id":"R3L83_C12_348370_20240112_STAGE2_ELECTROLYTE_CONTRACT_BRIDGE","symbol":"348370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":10,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":18,"customer_quality_score":14,"policy_or_regulatory_score":4,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"contract_score":13,"backlog_visibility_score":11,"margin_bridge_score":9,"revision_score":11,"relative_strength_score":18,"customer_quality_score":15,"policy_or_regulatory_score":4,"valuation_repricing_score":10,"execution_risk_score":9,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_after":83,"stage_label_after":"Stage2-Actionable/Yellow-Watch-with-4B-overlay","changed_components":["customer_quality_score","+1","margin_bridge_score","+1","valuation_repricing_score","-2"],"component_delta_explanation":"Positive bridge is allowed, but post-peak drawdown means C12 must keep 4B watch once valuation/positioning overheats.","MFE_90D_pct":323.74,"MAE_90D_pct":-2.04,"score_return_alignment_label":"aligned_positive_but_requires_4B_watch","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_R3L83_066970_LNF_CATHODE_OFFTAKE_CALL_OFF_BREAK","trigger_id":"R3L83_C12_066970_20240322_STAGE2_FALSE_POSITIVE_CATHODE_CALLOFF","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":13,"customer_quality_score":7,"policy_or_regulatory_score":2,"valuation_repricing_score":10,"execution_risk_score":14,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable false positive risk","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":5,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":6,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":6,"execution_risk_score":18,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-Watch/4C-risk-watch","changed_components":["contract_score","-3","backlog_visibility_score","-5","relative_strength_score","-7","execution_risk_score","+4"],"component_delta_explanation":"Call-off/cathode demand risk should remove Stage2 bridge credit when margin/revision evidence is absent and MAE90 is deeply negative.","MFE_90D_pct":6.93,"MAE_90D_pct":-41.32,"score_return_alignment_label":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_R3L83_003670_POSCOFUTUREM_ORDERBOOK_CALL_OFF_RISK","trigger_id":"R3L83_C12_003670_20240322_STAGE2_FALSE_POSITIVE_ORDERBOOK_CALLOFF","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":12,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":11,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":9,"execution_risk_score":13,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable false positive risk","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":6,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":18,"legal_or_contract_risk_score":7,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_after":60,"stage_label_after":"Stage2-Watch/4C-risk-watch","changed_components":["backlog_visibility_score","-6","customer_quality_score","-4","execution_risk_score","+5"],"component_delta_explanation":"Orderbook headline without utilization/margin bridge behaves like C12 call-off risk; Yellow/Green should be blocked.","MFE_90D_pct":2.2,"MAE_90D_pct":-24.18,"score_return_alignment_label":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 profile_comparison rows

```jsonl
{"row_type":"profile_comparison","comparison_id":"R3L83_C12_P0_CURRENT","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_role":"current_default_proxy","expected_error":"Still can over-credit cathode order/offtake headlines when customer call-off and margin bridge are not separated."}
{"row_type":"profile_comparison","comparison_id":"R3L83_C12_P1_BRIDGE_REQUIRED","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile":"P1_shadow_C12_customer_calloff_bridge_required","profile_role":"shadow_candidate","expected_effect":"Require confirmed customer demand, utilization and margin/revision bridge before Stage2/Yellow."}
{"row_type":"profile_comparison","comparison_id":"R3L83_C12_P2_HIGH_MAE_GUARD","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile":"P2_shadow_C12_MAE90_guard","profile_role":"shadow_candidate","expected_effect":"If MFE90 is under 10 and MAE90 is below -20, move from Stage2-Actionable to Watch/4C-risk unless exact non-price bridge exists."}
{"row_type":"profile_comparison","comparison_id":"R3L83_C12_P3_RECOMMENDED","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile":"P3_recommended_shadow_only","profile_role":"recommended_shadow_rule","expected_effect":"No production change now; add canonical C12 bridge-required + high-MAE guard candidate for later batch planner."}
```

### 25.6 aggregate / transition / residual rows

```jsonl
{"row_type":"aggregate_metric","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CUSTOMER_CALL_OFF_RISK_ELECTROLYTE_BRIDGE_VS_CATHODE_DEMAND_BREAK","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":1,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"new_independent_case_count":2,"reused_case_count":1,"avg_MFE90_pct":110.96,"avg_MAE90_pct":-22.51,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C12 needs a bridge filter: electrolyte/customer-localization positive path works, but cathode order/offtake headlines without utilization and margin bridge create high-MAE false positives."}
{"row_type":"stage_transition_summary","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"348370","trigger_type":"Stage2-Actionable-Electrolyte-ContractBridge-CalloffRiskOverruled","entry_date":"2024-01-12","stage2_to_90D_outcome":"good_stage2","stage2_to_180D_outcome":"positive_then_4B_watch","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Positive control; high upside but later post-peak drawdown validates separate 4B overlay."}
{"row_type":"stage_transition_summary","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"066970","trigger_type":"Stage2-FalsePositive-Cathode-Offtake-CallOff-NoMarginBridge","entry_date":"2024-03-22","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"4C_watch_or_counterexample","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Cathode/offtake headline lacked margin/revision bridge and quickly produced high MAE."}
{"row_type":"stage_transition_summary","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"003670","trigger_type":"Stage2-FalsePositive-Cathode-Orderbook-CallOff-DemandBreak","entry_date":"2024-03-22","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"4C_watch_or_counterexample","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Orderbook/long-term contract narrative failed without utilization and customer demand bridge."}
{"row_type":"residual_contribution","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":2,"reused_case_count":1,"new_symbol_count":2,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["C12_cathode_orderbook_false_positive","C12_calloff_high_MAE_tail","C12_positive_bridge_needs_4B_overlay"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"coverage_matrix","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CUSTOMER_CALL_OFF_RISK_ELECTROLYTE_BRIDGE_VS_CATHODE_DEMAND_BREAK","positive_case_count":1,"counterexample_count":2,"4B_case_count":1,"4C_case_count":0,"new_independent_case_count":2,"reused_case_count":1,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"Still needs exact URL repair and additional non-cathode positive cases outside reused 348370."}
```

### 25.7 shadow_weight rows

```jsonl
{"row_type":"shadow_weight","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"stage2_required_bridge","scope":"canonical_archetype","baseline_value":0,"tested_value":1,"delta":"+1 guard","reason":"Cathode/offtake orderbook headlines produced two high-MAE false positives; require customer demand + utilization + margin/revision bridge.","backtest_effect":"066970 and 003670 would remain Watch instead of Stage2-Actionable; 348370 positive control remains allowed but with 4B overlay.","trigger_ids":"R3L83_C12_066970_20240322_STAGE2_FALSE_POSITIVE_CATHODE_CALLOFF|R3L83_C12_003670_20240322_STAGE2_FALSE_POSITIVE_ORDERBOOK_CALLOFF|R3L83_C12_348370_20240112_STAGE2_ELECTROLYTE_CONTRACT_BRIDGE","calibration_usable_count":3,"new_independent_case_count":2,"counterexample_count":2,"confidence":"medium_low_due_source_proxy","proposal_type":"canonical_archetype_shadow_only","notes":"not production; post-calibrated residual"}
{"row_type":"shadow_weight","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"high_mae_guardrail","scope":"canonical_archetype","baseline_value":0,"tested_value":1,"delta":"+1 risk guard","reason":"MFE90 < 10 and MAE90 <= -20 separated failed cathode cases from electrolyte positive bridge.","backtest_effect":"Blocks Yellow/Green for C12 cathode cases until exact non-price bridge is verified.","trigger_ids":"R3L83_C12_066970_20240322_STAGE2_FALSE_POSITIVE_CATHODE_CALLOFF|R3L83_C12_003670_20240322_STAGE2_FALSE_POSITIVE_ORDERBOOK_CALLOFF","calibration_usable_count":2,"new_independent_case_count":2,"counterexample_count":2,"confidence":"medium","proposal_type":"canonical_archetype_shadow_only","notes":"not production; high-MAE calibration only"}
{"row_type":"shadow_weight","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"local_4b_watch_guard","scope":"canonical_archetype","baseline_value":0,"tested_value":1,"delta":"+1 watch","reason":"Even positive C12 electrolyte bridge became valuation/positioning overheat after extreme MFE; full 4B still requires non-price evidence.","backtest_effect":"Keeps 348370 positive Stage2/Yellow but adds 4B watch once full-window peak proximity is high.","trigger_ids":"R3L83_C12_348370_20240112_STAGE2_ELECTROLYTE_CONTRACT_BRIDGE","calibration_usable_count":1,"new_independent_case_count":0,"counterexample_count":0,"confidence":"low_due_soft_reuse","proposal_type":"canonical_archetype_shadow_only","notes":"not production; positive control is reused so weight should be capped"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update C12 canonical shadow profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R3
completed_loop = 83
next_round = R4
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 28. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

PRICE ATLAS:
Songdaiki/stock-web
manifest: atlas/manifest.json
profiles:
- atlas/symbol_profiles/348/348370.json
- atlas/symbol_profiles/066/066970.json
- atlas/symbol_profiles/003/003670.json
shards:
- atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv
```
