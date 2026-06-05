# E2R Stock-Web v12 Residual Research — R4 Loop 87 / L4 / C16

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R4
loop: 87
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: COPPER_GRID_RESOURCE_SUPPLY_BRIDGE_VS_LITHIUM_RESOURCE_POLICY_THEME_DECAY
sector: materials / resource / strategic supply / copper / lithium / policy supply chain
output_file: e2r_stock_web_v12_residual_round_R4_loop_87_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R3 loop 87`.

```text
scheduled_round = R4
scheduled_loop = 87
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```

R4 is restricted to L4 materials / spread / resource.  
C16 is selected because the immediately previous R4 loop used C17 chemical commodity margin spread, while C16 is the strategic-resource / policy-supply bucket.

The No-Repeat Index shows C16 as:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
rows = 36
symbols = 23
good/bad Stage2 = 14/9
4B/4C = 2/0
top-covered = 047400, 005490, 012320, 001570, 081150, 101670
```

This loop avoids those top-covered symbols and also avoids the previous R4 loop86 C17 symbols:

```text
120110, 010060, 009830
```

Selected symbols:

```text
006260, 073570, 131400
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"006260","company_name":"LS","profile_path":"atlas/symbol_profiles/006/006260.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7765,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1996-01-04","1996-12-04","1999-06-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"073570","company_name":"리튬포어스","profile_path":"atlas/symbol_profiles/073/073570.json","first_date":"2004-01-06","last_date":"2026-02-20","trading_day_count":5314,"corporate_action_candidate_count":14,"corporate_action_candidate_dates":["2006-04-12","2006-05-08","2006-07-24","2010-03-05","2015-07-17","2015-10-05","2017-11-15","2017-11-17","2018-01-18","2019-01-18","2020-04-24","2022-11-18","2022-12-12","2025-06-09"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before or after the selected 2024 forward window; selected 2024 window has no listed corporate-action candidate.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"131400","company_name":"이브이첨단소재","profile_path":"atlas/symbol_profiles/131/131400.json","first_date":"2010-12-27","last_date":"2026-02-20","trading_day_count":3707,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2021-08-25","2021-09-15","2023-01-03","2023-03-28"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"006260","trigger_type":"Stage2-Actionable-CopperGridStrategicSupplyBridge-Positive","entry_date":"2024-03-14","duplicate_status":"new C16 symbol/trigger/date combination outside top-covered list and previous R4 C17 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"073570","trigger_type":"Stage2-FalsePositive-LithiumResourcePolicyTheme-NoSupplyCustomerMarginBridge","entry_date":"2024-03-29","duplicate_status":"new C16 symbol/trigger/date combination outside top-covered list and previous R4 C17 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"131400","trigger_type":"Stage2-FalsePositive-LithiumEVResourceTheme-NoCustomerSupplyBridge","entry_date":"2024-01-24","duplicate_status":"new C16 symbol/trigger/date combination outside top-covered list and previous R4 C17 symbols"}
```

## 4. Research question

C16 is not “resource or policy theme moved.”  
A strategic-resource signal must prove a supply bridge: copper or lithium availability, customer quality, offtake or contract visibility, inventory tightness, margin spread, policy funding, logistics, and cash conversion. A resource headline without supply conversion is a map with no mine road; the market can point to it, but no tonnage moves.

Residual question:

```text
Can C16 distinguish:
1. copper/grid strategic supply bridge with very high MFE and tolerable MAE,
2. lithium resource policy theme that spikes but collapses without supply, customer and margin bridge,
3. EV/lithium resource theme rebound that lacks customer/offtake and supply-chain conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C16_R4L87_006260_LS_COPPER_GRID_STRATEGIC_SUPPLY","symbol":"006260","company_name":"LS","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_GRID_STRATEGIC_SUPPLY_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-CopperGridStrategicSupplyBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_shallow_90D_MAE_later_180D_drawdown","current_profile_verdict":"current_profile_correct_if_supply_customer_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Copper/grid strategic supply proxy produced very high 90D MFE. Later drawdown means Green still requires exact customer, offtake, margin and cash evidence."}
{"row_type":"case","case_id":"C16_R4L87_073570_LITHIUMFORCE_POLICY_THEME_DECAY","symbol":"073570","company_name":"리튬포어스","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_POLICY_THEME_WITHOUT_SUPPLY_CUSTOMER_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LithiumResourcePolicyTheme-NoSupplyCustomerMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_lithium_policy_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Lithium/resource theme blowoff had near-zero MFE and extreme MAE without credible supply, customer/offtake and margin bridge."}
{"row_type":"case","case_id":"C16_R4L87_131400_EVADV_LITHIUM_THEME_DECAY","symbol":"131400","company_name":"이브이첨단소재","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_EV_RESOURCE_THEME_WITHOUT_CUSTOMER_SUPPLY_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LithiumEVResourceTheme-NoCustomerSupplyBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_EV_resource_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"EV/lithium resource rebound had only modest initial MFE and then high MAE without customer/offtake, supply-chain and margin bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 006260 LS — copper/grid strategic supply bridge positive

Entry row: `2024-03-14 c=101300`.  
Observed path: early low `2024-03-15 l=99900`, 30D high `2024-04-18 h=130500`, 90D high `2024-05-21 h=194800`, and later low `2024-11-18 l=84500`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L87_C16_006260_20240314_STAGE2_COPPER_GRID_SUPPLY","case_id":"C16_R4L87_006260_LS_COPPER_GRID_STRATEGIC_SUPPLY","symbol":"006260","company_name":"LS","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_GRID_STRATEGIC_SUPPLY_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-CopperGridStrategicSupplyBridge-Positive","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":101300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_copper_grid_resource_supply_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; copper/grid strategic supply, inventory tightness and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["copper_grid_supply_proxy","resource_inventory_tightness_proxy","customer_quality_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_offtake_or_customer_source_pending","margin_spread_bridge_pending","cash_conversion_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv","profile_path":"atlas/symbol_profiles/006/006260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.83,"MFE_90D_pct":92.30,"MFE_180D_pct":92.30,"MAE_30D_pct":-1.38,"MAE_90D_pct":-1.38,"MAE_180D_pct":-16.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":194800.0,"max_drawdown_low_date":"2024-11-18","max_drawdown_low":84500.0,"drawdown_after_peak_pct":-56.62,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_price_extension_watch; do not upgrade to Green without exact offtake/customer/margin evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_shallow_90D_MAE_later_180D_drawdown","current_profile_verdict":"current_profile_correct_if_supply_customer_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"006260_2024-03-14_101300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C16 can allow Stage2/Yellow when strategic-resource strength is tied to copper/grid supply, customer quality and margin bridge. Green still requires exact offtake/customer/margin/cash evidence."}
```

### 6.2 073570 리튬포어스 — lithium resource policy theme without supply/customer/margin bridge

Entry row: `2024-03-29 c=8170`.  
Observed path: local high `2024-03-29 h=8400`, then lows `2024-05-29 l=4215`, `2024-07-22 l=2600`, and `2024-12-09 l=1660`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L87_C16_073570_20240329_STAGE2_FALSE_POSITIVE_LITHIUM_POLICY","case_id":"C16_R4L87_073570_LITHIUMFORCE_POLICY_THEME_DECAY","symbol":"073570","company_name":"리튬포어스","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_POLICY_THEME_WITHOUT_SUPPLY_CUSTOMER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-LithiumResourcePolicyTheme-NoSupplyCustomerMarginBridge","trigger_date":"2024-03-29","entry_date":"2024-03-29","entry_price":8170.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_lithium_resource_policy_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; lithium resource policy theme treated as insufficient without verified supply, customer/offtake, cost curve, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["lithium_resource_policy_theme","relative_strength_blowoff"],"stage3_evidence_fields":["verified_supply_bridge_missing","customer_offtake_missing","margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","supply_customer_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/073/073570/2024.csv","profile_path":"atlas/symbol_profiles/073/073570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.82,"MFE_90D_pct":2.82,"MFE_180D_pct":2.82,"MAE_30D_pct":-48.41,"MAE_90D_pct":-68.18,"MAE_180D_pct":-79.68,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-29","peak_price":8400.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":1660.0,"drawdown_after_peak_pct":-80.24,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"lithium_policy_theme_without_verified_supply_customer_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","supply_customer_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_lithium_policy_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"073570_2024-03-29_8170","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C16 should not upgrade lithium policy/resource labels without verified supply, customer/offtake, margin and cash bridge. Near-zero MFE and extreme MAE force Watch/4B-risk routing."}
```

### 6.3 131400 이브이첨단소재 — EV/lithium resource theme without customer/offtake bridge

Entry row: `2024-01-24 c=3165`.  
Observed path: local high `2024-01-24 h=3565`, then lows `2024-04-17 l=2320`, `2024-07-23 l=2180`, and `2024-12-09 l=1660`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L87_C16_131400_20240124_STAGE2_FALSE_POSITIVE_EV_LITHIUM_RESOURCE","case_id":"C16_R4L87_131400_EVADV_LITHIUM_THEME_DECAY","symbol":"131400","company_name":"이브이첨단소재","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_EV_RESOURCE_THEME_WITHOUT_CUSTOMER_SUPPLY_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-LithiumEVResourceTheme-NoCustomerSupplyBridge","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":3165.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_EV_lithium_resource_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; EV/lithium resource theme treated as insufficient without customer/offtake, verified supply-chain conversion, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["EV_lithium_resource_theme","relative_strength_rebound"],"stage3_evidence_fields":["customer_offtake_bridge_missing","verified_supply_chain_bridge_missing","margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","customer_supply_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131400/2024.csv","profile_path":"atlas/symbol_profiles/131/131400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.64,"MFE_90D_pct":12.64,"MFE_180D_pct":12.64,"MAE_30D_pct":-7.42,"MAE_90D_pct":-26.70,"MAE_180D_pct":-47.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-24","peak_price":3565.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":1660.0,"drawdown_after_peak_pct":-53.44,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"EV_lithium_resource_theme_without_customer_supply_bridge_should_remain_watch_4B_not_Yellow","four_b_evidence_type":["price_only","customer_supply_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_EV_resource_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"131400_2024-01-24_3165","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C16 should not promote EV/lithium resource rebound without customer/offtake and verified supply bridge. Initial MFE below 15% plus high MAE argues for Watch/4B rather than Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C16_R4L87_006260_LS_COPPER_GRID_STRATEGIC_SUPPLY","trigger_id":"R4L87_C16_006260_20240314_STAGE2_COPPER_GRID_SUPPLY","symbol":"006260","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C16 requires strategic supply/customer/margin bridge rather than resource policy theme alone","raw_component_scores_before":{"strategic_resource_supply_score":14,"customer_offtake_score":11,"inventory_tightness_score":12,"policy_supply_support_score":10,"margin_spread_score":9,"cash_conversion_score":6,"relative_strength_score":14,"valuation_repricing_score":9,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"strategic_resource_supply_score":17,"customer_offtake_score":14,"inventory_tightness_score":15,"policy_supply_support_score":12,"margin_spread_score":11,"cash_conversion_score":8,"relative_strength_score":15,"valuation_repricing_score":10,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":87,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Copper/grid supply and customer-quality proxy plus very high MFE support Yellow/Green-candidate watch, but later drawdown and proxy-only evidence keep Green strict."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C16_R4L87_073570_LITHIUMFORCE_POLICY_THEME_DECAY","trigger_id":"R4L87_C16_073570_20240329_STAGE2_FALSE_POSITIVE_LITHIUM_POLICY","symbol":"073570","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_scope":"current_default_proxy","profile_hypothesis":"lithium resource policy theme without verified supply/customer bridge should be blocked","raw_component_scores_before":{"strategic_resource_supply_score":5,"customer_offtake_score":0,"inventory_tightness_score":2,"policy_supply_support_score":7,"margin_spread_score":0,"cash_conversion_score":0,"relative_strength_score":13,"valuation_repricing_score":5,"execution_risk_score":-18,"theme_spike_risk":-20,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"strategic_resource_supply_score":0,"customer_offtake_score":0,"inventory_tightness_score":0,"policy_supply_support_score":1,"margin_spread_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-28,"theme_spike_risk":-26,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and extreme MAE convert lithium policy theme into verified-supply/customer bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C16_R4L87_131400_EVADV_LITHIUM_THEME_DECAY","trigger_id":"R4L87_C16_131400_20240124_STAGE2_FALSE_POSITIVE_EV_LITHIUM_RESOURCE","symbol":"131400","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_scope":"current_default_proxy","profile_hypothesis":"EV/lithium resource rebound without customer/offtake and supply conversion should remain Watch/blocked","raw_component_scores_before":{"strategic_resource_supply_score":4,"customer_offtake_score":0,"inventory_tightness_score":2,"policy_supply_support_score":5,"margin_spread_score":0,"cash_conversion_score":0,"relative_strength_score":10,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"strategic_resource_supply_score":0,"customer_offtake_score":0,"inventory_tightness_score":0,"policy_supply_support_score":1,"margin_spread_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"MFE below Yellow threshold and high MAE require customer/offtake and supply-chain bridge before promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R4L87_C16_P0_CURRENT","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C16 needs explicit verified supply, customer/offtake, inventory tightness, margin and cash bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":35.92,"avg_MAE90_pct":-32.75,"avg_MFE180_pct":35.92,"avg_MAE180_pct":-47.94,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C16_verified_supply_customer_margin_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R4L87_C16_P1_SECTOR_SPECIFIC","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_id":"P1_L4_verified_supply_customer_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L4 strategic resource signals need verified supply, customer/offtake, inventory tightness, policy monetization, margin or cash bridge before Stage2-Actionable","changed_axes":["verified_supply_required","customer_offtake_required","resource_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_verified_supply_customer_offtake_inventory_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":35.92,"avg_MAE90_pct":-32.75,"avg_MFE180_pct":35.92,"avg_MAE180_pct":-47.94,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R4L87_C16_P2_CANONICAL","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_id":"P2_C16_verified_supply_customer_margin_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C16 should reward strategic supply conversion, not lithium/resource policy blowoffs","changed_axes":["C16_verified_supply_customer_bridge_required","C16_lithium_policy_theme_local_4B_guard","C16_high_MAE_guard"],"changed_thresholds":{"stage2_yellow_gate":"verified_supply_plus_customer_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":35.92,"avg_MAE90_pct":-32.75,"avg_MFE180_pct":35.92,"avg_MAE180_pct":-47.94,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R4L87_C16_P3_COUNTEREXAMPLE_GUARD","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_id":"P3_C16_low_MFE_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<15 and MAE90<=-25 while verified supply/customer bridge is missing, block Yellow/Green","changed_axes":["C16_low_MFE_guardrail","C16_high_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_15_and_MAE90_le_minus_25"},"eligible_trigger_count":3,"avg_MFE90_pct":35.92,"avg_MAE90_pct":-32.75,"avg_MFE180_pct":35.92,"avg_MAE180_pct":-47.94,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_COPPER_GRID_SUPPLY_VS_LITHIUM_RESOURCE_THEME","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":35.92,"avg_MAE90_pct":-32.75,"avg_MFE180_pct":35.92,"avg_MAE180_pct":-47.94,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_15":0.67,"stage2_bad_entry_rate_MAE90_le_minus_25":0.67,"interpretation":"C16 needs bridge discipline. LS shows copper/grid strategic supply can rerate sharply, while 리튬포어스 and 이브이첨단소재 show lithium/resource policy themes can collapse without verified supply, customer/offtake, margin and cash conversion."}
{"row_type":"stage_transition_summary","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"006260","trigger_type":"Stage2-Actionable-CopperGridStrategicSupplyBridge-Positive","entry_date":"2024-03-14","stage2_to_90D_outcome":"good_stage2_very_high_MFE_shallow_MAE","stage2_to_180D_outcome":"positive_resource_supply_rerating_with_later_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when strategic resource strength is tied to verified supply/customer/margin bridge; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"073570","trigger_type":"Stage2-FalsePositive-LithiumResourcePolicyTheme-NoSupplyCustomerMarginBridge","entry_date":"2024-03-29","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_extreme_MAE","stage2_to_180D_outcome":"failed_lithium_policy_theme_extreme_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Lithium policy/resource theme without verified supply/customer bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"131400","trigger_type":"Stage2-FalsePositive-LithiumEVResourceTheme-NoCustomerSupplyBridge","entry_date":"2024-01-24","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_EV_lithium_resource_theme","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"EV/lithium resource rebound without customer/offtake and supply-chain bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","residual_type":"strategic_resource_policy_theme_overcredit_without_verified_supply_customer_margin_bridge","contribution":"Adds two C16 local 4B/high-MAE counterexamples against one copper/grid strategic supply positive, avoiding C16 top-covered and previous R4 C17 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_GRID_RESOURCE_SUPPLY_BRIDGE_VS_LITHIUM_RESOURCE_POLICY_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C16 now has non-top-symbol copper/grid positive and lithium/resource theme-decay counterexamples; next R4 loops should exact-URL repair verified supply, customer/offtake, inventory, margin spread, policy monetization and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","axis":"C16_verified_supply_customer_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"006260 worked when strategic copper/grid supply proxy was present; 073570 and 131400 failed when resource policy theme lacked verified supply, customer/offtake and margin bridge."}
{"row_type":"shadow_weight","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","axis":"C16_lithium_resource_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Lithium/resource theme rows showed low or near-zero MFE and high/extreme MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R4","loop":"87","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","axis":"C16_low_MFE_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<15 and MAE90<=-25 while verified supply/customer bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - strategic_resource_policy_theme_overcredit
  - lithium_resource_theme_no_verified_supply
  - customer_offtake_bridge_missing
  - margin_cash_conversion_bridge_missing
new_axis_proposed:
  - C16_verified_supply_customer_margin_bridge_required_shadow_only
  - C16_lithium_resource_theme_local_4B_watch_guard_shadow_only
  - C16_low_MFE_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C16
  - full_4b_requires_non_price_evidence within C16
  - hard_4c_thesis_break_routes_to_4c within C16
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
3. Confirm R4 / L4 / C16 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C16 top-covered symbols
   - previous R4 loop86 C17 symbols listed in the MD
6. If aggregate support remains stable after exact evidence URL repair, consider C16-scoped safe patch candidates:
   - C16_verified_supply_customer_margin_bridge_required
   - C16_lithium_resource_theme_local_4B_watch_guard
   - C16_low_MFE_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R4
completed_loop = 87
next_round = R5
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.
```
