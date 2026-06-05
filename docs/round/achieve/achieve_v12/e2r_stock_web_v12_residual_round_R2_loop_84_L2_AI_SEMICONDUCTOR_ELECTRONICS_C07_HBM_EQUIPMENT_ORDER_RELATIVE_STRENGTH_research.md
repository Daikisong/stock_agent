# E2R Stock-Web v12 Residual Research — R2 Loop 84 / L2 / C07

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 84
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_VS_TEST_EQUIPMENT_NO_REVENUE_BRIDGE
sector: AI·semiconductor·electronics / HBM equipment / test-handler order relative strength
output_file: e2r_stock_web_v12_residual_round_R2_loop_84_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after the completed `R1 loop 84` result.

```text
scheduled_round = R2
scheduled_loop = 84
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
```

R2 is restricted to AI / semiconductor / electronics.  
C07 is selected because the No-Repeat ledger shows C07 has strong good-stage coverage but almost no bad Stage2 counterexample coverage. It is therefore a good place to test whether HBM equipment order relative strength is being over-credited.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"232140","company_name":"와이씨","profile_path":"atlas/symbol_profiles/232/232140.json","first_date":"2015-12-24","last_date":"2026-02-20","trading_day_count":2425,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2017-04-05"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"092870","company_name":"엑시콘","profile_path":"atlas/symbol_profiles/092/092870.json","first_date":"2014-12-24","last_date":"2026-02-20","trading_day_count":2730,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2015-10-22","2024-07-31"],"has_major_raw_discontinuity":true,"calibration_caveat":"Entry is deliberately placed after the 2024-07-31 corporate-action candidate to avoid contamination.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"post_2024-07-31_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"089790","company_name":"제이티","profile_path":"atlas/symbol_profiles/089/089790.json","first_date":"2006-10-27","last_date":"2026-02-20","trading_day_count":4745,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2010-04-19","2010-04-26"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
The C07 top-covered symbols are `042700`, `064760`, `003160`, `036200`, `036540`, and `039440`. This run avoids that repeated set.

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced here:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"232140","trigger_type":"Stage2-Actionable-HBMTesterOrderRS-RevenueBridge-Positive","entry_date":"2024-04-17","duplicate_status":"new C07 symbol/trigger/date combination"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"092870","trigger_type":"Stage2-FalsePositive-HBMTesterNarrative-NoRevenueBridge-HighMAE","entry_date":"2024-09-26","duplicate_status":"new C07 post-corporate-action trigger/date combination"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"089790","trigger_type":"Stage2-FalsePositive-TestHandlerRelativeStrength-NoOrderBridge","entry_date":"2024-03-28","duplicate_status":"new C07 symbol/trigger/date combination"}
```

## 4. Research question

C07 is an order-strength lane. It should reward genuine HBM equipment order conversion, but it must not confuse a test-equipment narrative rebound with a revenue bridge.

Residual question:

```text
Can C07 distinguish:
1. real HBM tester/order relative strength that becomes a structural rerating,
2. post-event tester rebound with no revenue/order bridge,
3. old test-handler relative strength that fades into high-MAE without confirmed order conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C07_R2L84_232140_YC_HBM_TESTER_ORDER_BRIDGE","symbol":"232140","company_name":"와이씨","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TESTER_ORDER_RELATIVE_STRENGTH_REVENUE_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-HBMTesterOrderRS-RevenueBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_with_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_non_price_bridge_required","price_source":"Songdaiki/stock-web","notes":"HBM/tester order relative strength worked when price path showed large sustained MFE and evidence proxy suggested order/revenue bridge."}
{"row_type":"case","case_id":"C07_R2L84_092870_EXICON_TESTER_REBOUND_NO_BRIDGE","symbol":"092870","company_name":"엑시콘","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TESTER_NARRATIVE_POST_EVENT_REBOUND_NO_REVENUE_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-HBMTesterNarrative-NoRevenueBridge-HighMAE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_relative_strength_overcredited","price_source":"Songdaiki/stock-web","notes":"Entry placed after 2024-07-31 corporate action candidate; rebound had low MFE and deep MAE until late re-bounce."}
{"row_type":"case","case_id":"C07_R2L84_089790_JT_TEST_HANDLER_NO_ORDER_BRIDGE","symbol":"089790","company_name":"제이티","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"TEST_HANDLER_RELATIVE_STRENGTH_WITHOUT_ORDER_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-TestHandlerRelativeStrength-NoOrderBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_very_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive_if_order_bridge_missing","price_source":"Songdaiki/stock-web","notes":"Relative strength and test-handler narrative did not convert into durable order/revenue bridge; forward path collapsed."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 232140 와이씨 — HBM/tester order bridge positive

Entry row: `2024-04-17 c=7280`.  
Stock-Web path shows same-day low `l=6280`, 30D high `2024-05-31 h=17910`, and 90/180D high `2024-06-13 h=22950`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L84_C07_232140_20240417_STAGE2_HBM_TESTER_ORDER_BRIDGE","case_id":"C07_R2L84_232140_YC_HBM_TESTER_ORDER_BRIDGE","symbol":"232140","company_name":"와이씨","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TESTER_ORDER_RELATIVE_STRENGTH_REVENUE_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-HBMTesterOrderRS-RevenueBridge-Positive","trigger_date":"2024-04-17","entry_date":"2024-04-17","entry_price":7280.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_order_report_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; HBM tester/order bridge thesis treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["relative_strength_score","order_intake_quality_proxy","customer_quality_proxy"],"stage3_evidence_fields":["revenue_bridge_proxy","margin_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv","profile_path":"atlas/symbol_profiles/232/232140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":146.02,"MFE_90D_pct":215.25,"MFE_180D_pct":215.25,"MAE_30D_pct":-13.74,"MAE_90D_pct":-13.74,"MAE_180D_pct":-13.74,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":22950.0,"max_drawdown_low_date":"2024-04-17","max_drawdown_low":6280.0,"drawdown_after_peak_pct":-63.79,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_non_price_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"232140_2024-04-17_7280","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C07 can work when relative strength is tied to tester/order and revenue bridge. Still, Green should wait for URL-grade order/customer/margin confirmation."}
```

### 6.2 092870 엑시콘 — post-corporate-action tester rebound without bridge

Entry row: `2024-09-26 c=13810`, after the `2024-07-31` corporate-action candidate.  
Near-term upside was small; the 90D low reached `2024-12-09 l=8410`, while a later rebound reached `2025-02-14 h=15760`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L84_C07_092870_20240926_STAGE2_FALSE_POSITIVE_HBM_TESTER_REBOUND","case_id":"C07_R2L84_092870_EXICON_TESTER_REBOUND_NO_BRIDGE","symbol":"092870","company_name":"엑시콘","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TESTER_NARRATIVE_POST_EVENT_REBOUND_NO_REVENUE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-HBMTesterNarrative-NoRevenueBridge-HighMAE","trigger_date":"2024-09-26","entry_date":"2024-09-26","entry_price":13810.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_tester_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; tester/HBM narrative treated as insufficient unless customer order and revenue conversion are verified","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["relative_strength_rebound","tester_theme_proxy"],"stage3_evidence_fields":["order_bridge_missing","revenue_bridge_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/092/092870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.15,"MFE_90D_pct":14.12,"MFE_180D_pct":14.12,"MAE_30D_pct":-20.64,"MAE_90D_pct":-39.10,"MAE_180D_pct":-39.10,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-14","peak_price":15760.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":8410.0,"drawdown_after_peak_pct":-46.64,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"weak_bridge_rebound_should_remain_watch_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_relative_strength_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"entry_after_2024-07-31_candidate_clean_forward_window","same_entry_group_id":"092870_2024-09-26_13810","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C07 relative strength can rebound after a technical/corporate-action event, but without order/revenue bridge it becomes high-MAE false positive."}
```

### 6.3 089790 제이티 — test-handler relative strength without order bridge

Entry row: `2024-03-28 c=10830`.  
Forward path had only `2024-04-12 h=11360` upside, then collapsed to `2024-12-09 l=3025`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L84_C07_089790_20240328_STAGE2_FALSE_POSITIVE_TEST_HANDLER_NO_ORDER_BRIDGE","case_id":"C07_R2L84_089790_JT_TEST_HANDLER_NO_ORDER_BRIDGE","symbol":"089790","company_name":"제이티","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"TEST_HANDLER_RELATIVE_STRENGTH_WITHOUT_ORDER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-TestHandlerRelativeStrength-NoOrderBridge","trigger_date":"2024-03-28","entry_date":"2024-03-28","entry_price":10830.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_test_handler_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; test-handler relative strength treated as insufficient unless order/customer/revenue bridge is verified","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["relative_strength_score","test_handler_theme_proxy"],"stage3_evidence_fields":["order_bridge_missing","customer_quality_missing","revenue_bridge_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","thesis_break_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089790/2024.csv","profile_path":"atlas/symbol_profiles/089/089790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.89,"MFE_90D_pct":4.89,"MFE_180D_pct":4.89,"MAE_30D_pct":-19.67,"MAE_90D_pct":-34.99,"MAE_180D_pct":-72.07,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-12","peak_price":11360.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":3025.0,"drawdown_after_peak_pct":-73.37,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_peak_without_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_very_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive_if_order_bridge_missing","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"089790_2024-03-28_10830","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C07 needs a local order/revenue bridge guard. Test-handler RS without order bridge produced very high MAE and almost no durable MFE."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_R2L84_232140_YC_HBM_TESTER_ORDER_BRIDGE","trigger_id":"R2L84_C07_232140_20240417_STAGE2_HBM_TESTER_ORDER_BRIDGE","symbol":"232140","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_scope":"current_default_proxy","profile_hypothesis":"current calibrated profile works when C07 relative strength has non-price order/revenue bridge","raw_component_scores_before":{"contract_score":11,"backlog_visibility_score":13,"margin_bridge_score":9,"revision_score":11,"relative_strength_score":20,"customer_quality_score":12,"policy_or_regulatory_score":2,"valuation_repricing_score":13,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable/Stage3-Yellow-Watch","raw_component_scores_after":{"contract_score":13,"backlog_visibility_score":16,"margin_bridge_score":12,"revision_score":13,"relative_strength_score":20,"customer_quality_score":14,"policy_or_regulatory_score":2,"valuation_repricing_score":13,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Order/revenue bridge strengthens C07 but source URL and margin confirmation still block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_R2L84_092870_EXICON_TESTER_REBOUND_NO_BRIDGE","trigger_id":"R2L84_C07_092870_20240926_STAGE2_FALSE_POSITIVE_HBM_TESTER_REBOUND","symbol":"092870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_scope":"current_default_proxy","profile_hypothesis":"relative-strength rebound without order/revenue bridge should be blocked from Yellow/Green","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":5,"relative_strength_score":14,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":7,"execution_risk_score":-10,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":-2,"accounting_trust_risk_score":0},"weighted_score_before":55,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":4,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":5,"execution_risk_score":-14,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":-2,"accounting_trust_risk_score":0},"weighted_score_after":39,"stage_label_after":"Stage1/Stage2-Watch-Blocked","component_delta_explanation":"Post-event rebound and weak bridge evidence trigger C07 high-MAE guard."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_R2L84_089790_JT_TEST_HANDLER_NO_ORDER_BRIDGE","trigger_id":"R2L84_C07_089790_20240328_STAGE2_FALSE_POSITIVE_TEST_HANDLER_NO_ORDER_BRIDGE","symbol":"089790","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_scope":"current_default_proxy","profile_hypothesis":"test-handler RS without order/customer bridge should not become actionable","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":4,"relative_strength_score":15,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":-13,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":48,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":7,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":-18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":24,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Extreme MAE and missing order bridge convert the RS signal into evidence-quality failure."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R2L84_C07_P0_CURRENT","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global price-only guard helps but C07 needs explicit order/revenue bridge guard","eligible_trigger_count":3,"avg_MFE_90D_pct":78.09,"avg_MAE_90D_pct":-29.28,"avg_MFE_180D_pct":78.09,"avg_MAE_180D_pct":-41.64,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C07_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R2L84_C07_P1_SECTOR_SPECIFIC","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"P1_L2_HBM_equipment_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L2 HBM equipment relative strength needs at least one order/customer/revenue bridge","changed_axes":["order_bridge_required","customer_quality_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_order_or_revenue_proxy"},"eligible_trigger_count":3,"avg_MFE_90D_pct":78.09,"avg_MAE_90D_pct":-29.28,"avg_MFE_180D_pct":78.09,"avg_MAE_180D_pct":-41.64,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R2L84_C07_P2_CANONICAL","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"P2_C07_order_revenue_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C07 should allow RS only when it is tied to order/revenue/customer-quality evidence","changed_axes":["C07_order_revenue_bridge_required","C07_relative_strength_overcredit_penalty"],"changed_thresholds":{"stage2_yellow_gate":"non_price_bridge_required"},"eligible_trigger_count":3,"avg_MFE_90D_pct":78.09,"avg_MAE_90D_pct":-29.28,"avg_MFE_180D_pct":78.09,"avg_MAE_180D_pct":-41.64,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R2L84_C07_P3_COUNTEREXAMPLE_GUARD","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"P3_C07_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<20 and MAE90<=-30 while bridge evidence is missing, block Yellow/Green","changed_axes":["C07_high_MAE_guardrail","C07_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_20_and_MAE90_le_minus_30"},"eligible_trigger_count":3,"avg_MFE_90D_pct":78.09,"avg_MAE_90D_pct":-29.28,"avg_MFE_180D_pct":78.09,"avg_MAE_180D_pct":-41.64,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_TEST_EQUIPMENT_BRIDGE_VS_RELATIVE_STRENGTH_FALSE_POSITIVE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":78.09,"avg_MAE90_pct":-29.28,"avg_MFE180_pct":78.09,"avg_MAE180_pct":-41.64,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C07 needs a local bridge guard: true order/revenue bridge works, while test-equipment relative strength without bridge produces high-MAE false positives."}
{"row_type":"stage_transition_summary","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"232140","trigger_type":"Stage2-Actionable-HBMTesterOrderRS-RevenueBridge-Positive","entry_date":"2024-04-17","stage2_to_90D_outcome":"good_stage2_high_MFE","stage2_to_180D_outcome":"positive_re_rating_path","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when order/revenue/customer bridge exists; Green requires source-quality repair."}
{"row_type":"stage_transition_summary","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"092870","trigger_type":"Stage2-FalsePositive-HBMTesterNarrative-NoRevenueBridge-HighMAE","entry_date":"2024-09-26","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"4B_watch_or_counterexample","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Post-event tester rebound without bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"089790","trigger_type":"Stage2-FalsePositive-TestHandlerRelativeStrength-NoOrderBridge","entry_date":"2024-03-28","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"failed_rerating_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Test-handler relative strength without order bridge is a high-MAE false positive."}
{"row_type":"residual_contribution","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","residual_type":"HBM_equipment_relative_strength_overcredit_without_order_bridge","contribution":"Adds two C07 high-MAE counterexamples against one genuine order-bridge positive, filling the prior C07 counterexample gap.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_VS_TEST_EQUIPMENT_NO_REVENUE_BRIDGE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C07 now has explicit counterexamples; next R2 loops should test C06 customer-capacity and C08 socket/customer-quality URL repair."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","axis":"C07_order_revenue_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"232140 worked with order/revenue bridge proxy; 092870 and 089790 failed without verified order/customer/revenue bridge."}
{"row_type":"shadow_weight","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","axis":"C07_relative_strength_overcredit_penalty","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Relative strength alone produced high-MAE false positives in C07; require non-price bridge before Stage2-Actionable/Yellow."}
{"row_type":"shadow_weight","round":"R2","loop":"84","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","axis":"C07_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<20 and MAE90<=-30 while bridge evidence is missing, block Yellow/Green and route to Watch/4B-risk."}
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
residual_error_types_found:
  - relative_strength_overcredit_without_order_bridge
  - HBM_tester_rebound_high_MAE
  - test_handler_no_revenue_bridge_false_positive
new_axis_proposed:
  - C07_order_revenue_bridge_required_shadow_only
  - C07_relative_strength_overcredit_penalty_shadow_only
  - C07_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C07
  - full_4b_requires_non_price_evidence within C07
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 12. Data-quality caveat

All selected triggers use actual Stock-Web tradable raw OHLC rows.  
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
3. Confirm R2 / L2 / C07 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm 092870 entry is after the 2024-07-31 corporate-action candidate.
6. If aggregate support remains stable after exact evidence URL repair, consider C07-scoped safe patch candidates:
   - C07_order_revenue_bridge_required
   - C07_relative_strength_overcredit_penalty
   - C07_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R2
completed_loop = 84
next_round = R3
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.
```
