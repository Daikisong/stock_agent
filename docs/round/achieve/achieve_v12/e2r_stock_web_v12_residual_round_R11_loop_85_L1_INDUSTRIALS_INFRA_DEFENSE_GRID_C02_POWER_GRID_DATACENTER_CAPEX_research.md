# E2R Stock-Web v12 Residual Research — R11 Loop 85 / L1 / C02

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R11
loop: 85
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: POWER_GRID_TRANSFORMER_DATACENTER_CAPEX_BRIDGE_VS_PRICE_ONLY_GRID_BETA_EXTENSION
sector: industrials / power grid / transformer / data-center capex / policy-defense linkage lane
output_file: e2r_stock_web_v12_residual_round_R11_loop_85_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R10 loop 85`.

```text
scheduled_round = R11
scheduled_loop = 85
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
```

R11 may use the L1 industrials / infra / defense / grid lane when the research target is policy-defense or infrastructure linkage.  
This loop deliberately selects C02 rather than repeating the previous R11/C03 defense-export round. C02 is useful here because the 2024 Korean power-grid theme had both real transformer-order / data-center CAPEX winners and late-cycle price-only beta traps.

The selected symbols avoid the C02 top-covered list in the No-Repeat Index:

```text
000500, 006340, 033100, 001440, 017040, 189860
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"267260","company_name":"HD현대일렉트릭","profile_path":"atlas/symbol_profiles/267/267260.json","first_date":"2017-05-10","last_date":"2026-02-20","trading_day_count":2154,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["2017-11-17","2017-11-28","2017-12-11","2018-11-23","2018-12-18","2019-12-30"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"010120","company_name":"LS ELECTRIC","profile_path":"atlas/symbol_profiles/010/010120.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7749,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1995-09-28","1999-04-08","1999-07-26","2003-04-16"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"103590","company_name":"일진전기","profile_path":"atlas/symbol_profiles/103/103590.json","first_date":"2008-08-01","last_date":"2026-02-20","trading_day_count":4329,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2024-02-13"],"has_major_raw_discontinuity":true,"calibration_caveat":"2024 corporate-action candidate is before the selected entries; selected windows start after the candidate.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"entry_after_2024-02-13_candidate_clean_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"267260","trigger_type":"Stage2-Actionable-TransformerDatacenterCapexOrderBridge-Positive","entry_date":"2024-01-29","duplicate_status":"new C02 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"010120","trigger_type":"Stage2-FalsePositive-GridCapexPriceOnlyExtension-NoFreshBridge","entry_date":"2024-07-16","duplicate_status":"new C02 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"103590","trigger_type":"Stage2-FalsePositive-WireTransformerBetaExtension-NoFreshOrderMarginBridge","entry_date":"2024-07-15","duplicate_status":"new C02 symbol/trigger/date combination outside top-covered list; entry after 2024-02-13 corporate-action candidate"}
```

## 4. Research question

C02 is not “power-grid stock went up.” It is the bridge between grid/data-center CAPEX and executable backlog: transformer capacity, utility/data-center customer quality, order visibility, delivery slot scarcity, margin conversion, and cash conversion.

Residual question:

```text
Can C02 distinguish:
1. a real transformer/data-center CAPEX order bridge with very high MFE,
2. a late grid-CAPEX price-only extension after the bridge is already widely priced,
3. a wire/transformer beta extension with no fresh order/margin evidence and high MAE?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C02_R11L85_267260_HDHE_TRANSFORMER_CAPEX_BRIDGE","symbol":"267260","company_name":"HD현대일렉트릭","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_DATACENTER_CAPEX_ORDER_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-TransformerDatacenterCapexOrderBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_shallow_MAE","current_profile_verdict":"current_profile_correct_if_order_capacity_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Transformer/data-center CAPEX bridge produced very high MFE and shallow MAE. Supports Stage2/Yellow, but Green still requires exact customer/order/margin/cash evidence."}
{"row_type":"case","case_id":"C02_R11L85_010120_LSELECTRIC_PRICE_ONLY_GRID_EXTENSION","symbol":"010120","company_name":"LS ELECTRIC","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_CAPEX_PRICE_ONLY_EXTENSION_WITHOUT_FRESH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-GridCapexPriceOnlyExtension-NoFreshBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_high_MAE_after_late_extension","current_profile_verdict":"current_profile_false_positive_if_price_extension_overcredited","price_source":"Songdaiki/stock-web","notes":"A good C02 name can become a bad C02 entry when the signal is price-only late extension without fresh order/margin bridge."}
{"row_type":"case","case_id":"C02_R11L85_103590_ILJIN_WIRE_TRANSFORMER_BETA_EXTENSION","symbol":"103590","company_name":"일진전기","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"WIRE_TRANSFORMER_BETA_EXTENSION_WITHOUT_FRESH_ORDER_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-WireTransformerBetaExtension-NoFreshOrderMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE_then_choppy_rebound","current_profile_verdict":"current_profile_false_positive_if_wire_transformer_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"Wire/transformer beta extension showed low MFE and high MAE without fresh order, delivery-slot, margin and cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 267260 HD현대일렉트릭 — transformer/data-center CAPEX order bridge positive

Entry row: `2024-01-29 c=101200`.  
Observed path: early low `2024-02-01 l=97500`, 30D high around `2024-03-14 h=157600`, 90D high around `2024-05-27 h=314000`, and later high `2024-11-12 h=413500`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L85_C02_267260_20240129_STAGE2_TRANSFORMER_DATACENTER_CAPEX","case_id":"C02_R11L85_267260_HDHE_TRANSFORMER_CAPEX_BRIDGE","symbol":"267260","company_name":"HD현대일렉트릭","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_DATACENTER_CAPEX_ORDER_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-TransformerDatacenterCapexOrderBridge-Positive","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":101200.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_transformer_datacenter_capex_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; transformer/data-center CAPEX order bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["datacenter_capex_proxy","transformer_order_visibility_proxy","delivery_slot_scarcity_proxy","relative_strength_turn"],"stage3_evidence_fields":["margin_bridge_pending","cash_conversion_pending","customer_quality_source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv","profile_path":"atlas/symbol_profiles/267/267260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":55.73,"MFE_90D_pct":210.28,"MFE_180D_pct":308.60,"MAE_30D_pct":-3.66,"MAE_90D_pct":-3.66,"MAE_180D_pct":-3.66,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-12","peak_price":413500.0,"max_drawdown_low_date":"2024-02-01","max_drawdown_low":97500.0,"drawdown_after_peak_pct":-19.23,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_shallow_MAE","current_profile_verdict":"current_profile_correct_if_order_capacity_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"267260_2024-01-29_101200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C02 can allow Stage2/Yellow when grid CAPEX is tied to transformer order visibility, customer quality, delivery-slot scarcity and margin bridge. Green still requires exact source repair."}
```

### 6.2 010120 LS ELECTRIC — grid CAPEX price-only extension without fresh bridge

Entry row: `2024-07-16 c=234000`.  
Observed path: next-day high `2024-07-17 h=236000`, then lows `2024-10-28 l=147300` and `2024-11-21 l=131100`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L85_C02_010120_20240716_STAGE2_FALSE_POSITIVE_GRID_PRICE_EXTENSION","case_id":"C02_R11L85_010120_LSELECTRIC_PRICE_ONLY_GRID_EXTENSION","symbol":"010120","company_name":"LS ELECTRIC","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_CAPEX_PRICE_ONLY_EXTENSION_WITHOUT_FRESH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-GridCapexPriceOnlyExtension-NoFreshBridge","trigger_date":"2024-07-16","entry_date":"2024-07-16","entry_price":234000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_grid_capex_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; late grid-CAPEX extension treated as insufficient without fresh order, margin, delivery-slot or customer bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["grid_capex_relative_strength_extension","price_momentum"],"stage3_evidence_fields":["fresh_order_bridge_missing","incremental_margin_bridge_missing","customer_quality_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","fresh_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.85,"MFE_90D_pct":0.85,"MFE_180D_pct":0.85,"MAE_30D_pct":-17.74,"MAE_90D_pct":-37.05,"MAE_180D_pct":-43.97,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-17","peak_price":236000.0,"max_drawdown_low_date":"2024-11-21","max_drawdown_low":131100.0,"drawdown_after_peak_pct":-44.45,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_grid_capex_price_extension_without_fresh_order_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","positioning_overheat","fresh_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_high_MAE_after_late_extension","current_profile_verdict":"current_profile_false_positive_if_price_extension_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"010120_2024-07-16_234000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C02 should not upgrade a good name when the entry is only a late price extension. Without fresh order, margin and customer bridge, route to Watch/4B-risk."}
```

### 6.3 103590 일진전기 — wire/transformer beta extension without fresh order/margin bridge

Entry row: `2024-07-15 c=29400`.  
Observed path: local high `2024-07-16 h=30200`, then lows `2024-09-25 l=21000` and `2024-11-29 l=20500`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L85_C02_103590_20240715_STAGE2_FALSE_POSITIVE_WIRE_TRANSFORMER_BETA","case_id":"C02_R11L85_103590_ILJIN_WIRE_TRANSFORMER_BETA_EXTENSION","symbol":"103590","company_name":"일진전기","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"WIRE_TRANSFORMER_BETA_EXTENSION_WITHOUT_FRESH_ORDER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-WireTransformerBetaExtension-NoFreshOrderMarginBridge","trigger_date":"2024-07-15","entry_date":"2024-07-15","entry_price":29400.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_wire_transformer_beta_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; wire/transformer beta extension treated as insufficient without fresh order, customer, delivery-slot and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["wire_transformer_beta_extension","relative_strength_rebound"],"stage3_evidence_fields":["fresh_order_bridge_missing","delivery_slot_bridge_missing","margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","fresh_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv","profile_path":"atlas/symbol_profiles/103/103590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.72,"MFE_90D_pct":2.72,"MFE_180D_pct":2.72,"MAE_30D_pct":-23.13,"MAE_90D_pct":-28.57,"MAE_180D_pct":-30.27,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-16","peak_price":30200.0,"max_drawdown_low_date":"2024-11-29","max_drawdown_low":20500.0,"drawdown_after_peak_pct":-32.12,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"wire_transformer_beta_extension_without_fresh_order_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","fresh_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE_then_choppy_rebound","current_profile_verdict":"current_profile_false_positive_if_wire_transformer_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"entry_after_2024-02-13_candidate_clean_forward_window","same_entry_group_id":"103590_2024-07-15_29400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Wire/transformer beta without fresh order, delivery-slot and margin bridge created low MFE and high MAE. C02 needs a price-extension 4B guard."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R11L85_267260_HDHE_TRANSFORMER_CAPEX_BRIDGE","trigger_id":"R11L85_C02_267260_20240129_STAGE2_TRANSFORMER_DATACENTER_CAPEX","symbol":"267260","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C02 requires transformer/data-center CAPEX order bridge rather than price-only grid beta","raw_component_scores_before":{"datacenter_capex_score":16,"order_visibility_score":15,"delivery_slot_scarcity_score":14,"customer_quality_score":13,"margin_bridge_score":10,"relative_strength_score":14,"valuation_repricing_score":10,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable/Stage3-Yellow-Watch","raw_component_scores_after":{"datacenter_capex_score":19,"order_visibility_score":18,"delivery_slot_scarcity_score":17,"customer_quality_score":15,"margin_bridge_score":12,"relative_strength_score":15,"valuation_repricing_score":11,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Transformer order/capacity bridge and huge MFE support upgrade, but exact customer, margin and cash evidence still block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R11L85_010120_LSELECTRIC_PRICE_ONLY_GRID_EXTENSION","trigger_id":"R11L85_C02_010120_20240716_STAGE2_FALSE_POSITIVE_GRID_PRICE_EXTENSION","symbol":"010120","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_scope":"current_default_proxy","profile_hypothesis":"late grid-CAPEX price extension without fresh order/margin bridge should be blocked","raw_component_scores_before":{"datacenter_capex_score":9,"order_visibility_score":4,"delivery_slot_scarcity_score":4,"customer_quality_score":5,"margin_bridge_score":3,"relative_strength_score":13,"valuation_repricing_score":7,"execution_risk_score":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":31,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"datacenter_capex_score":5,"order_visibility_score":0,"delivery_slot_scarcity_score":1,"customer_quality_score":2,"margin_bridge_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and high MAE convert late price-only extension into bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R11L85_103590_ILJIN_WIRE_TRANSFORMER_BETA_EXTENSION","trigger_id":"R11L85_C02_103590_20240715_STAGE2_FALSE_POSITIVE_WIRE_TRANSFORMER_BETA","symbol":"103590","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_scope":"current_default_proxy","profile_hypothesis":"wire/transformer beta without fresh customer/order bridge should remain Watch/blocked","raw_component_scores_before":{"datacenter_capex_score":7,"order_visibility_score":4,"delivery_slot_scarcity_score":3,"customer_quality_score":4,"margin_bridge_score":2,"relative_strength_score":12,"valuation_repricing_score":6,"execution_risk_score":-11,"theme_spike_risk":-11,"information_confidence":3},"weighted_score_before":29,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"datacenter_capex_score":3,"order_visibility_score":0,"delivery_slot_scarcity_score":0,"customer_quality_score":1,"margin_bridge_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-16,"theme_spike_risk":-16,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Low MFE and high MAE require fresh order/margin/customer bridge before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R11L85_C02_P0_CURRENT","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C02 needs explicit fresh order, customer, delivery-slot, margin and cash bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":71.28,"avg_MAE90_pct":-23.09,"avg_MFE180_pct":104.06,"avg_MAE180_pct":-25.97,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C02_fresh_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R11L85_C02_P1_SECTOR_SPECIFIC","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_id":"P1_L1_grid_capex_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 grid/data-center signals need order visibility, delivery-slot scarcity, customer quality, margin or cash bridge before Stage2-Actionable","changed_axes":["fresh_order_bridge_required","delivery_slot_bridge_required","price_extension_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_order_customer_delivery_slot_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":71.28,"avg_MAE90_pct":-23.09,"avg_MFE180_pct":104.06,"avg_MAE180_pct":-25.97,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R11L85_C02_P2_CANONICAL","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_id":"P2_C02_fresh_order_margin_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C02 should reward transformer/data-center CAPEX conversion, not late price-only grid beta","changed_axes":["C02_fresh_order_margin_bridge_required","C02_price_only_grid_extension_penalty","C02_delivery_slot_customer_quality_gate"],"changed_thresholds":{"stage2_yellow_gate":"fresh_order_customer_delivery_slot_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":71.28,"avg_MAE90_pct":-23.09,"avg_MFE180_pct":104.06,"avg_MAE180_pct":-25.97,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R11L85_C02_P3_COUNTEREXAMPLE_GUARD","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_id":"P3_C02_high_MAE_late_extension_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<5 and MAE90<=-25 while fresh bridge is missing, block Yellow/Green","changed_axes":["C02_high_MAE_guardrail","C02_late_extension_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_5_and_MAE90_le_minus_25"},"eligible_trigger_count":3,"avg_MFE90_pct":71.28,"avg_MAE90_pct":-23.09,"avg_MFE180_pct":104.06,"avg_MAE180_pct":-25.97,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_CAPEX_BRIDGE_VS_PRICE_ONLY_EXTENSION","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":71.28,"avg_MAE90_pct":-23.09,"avg_MFE180_pct":104.06,"avg_MAE180_pct":-25.97,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_5":0.67,"stage2_bad_entry_rate_MAE90_le_minus_25":0.67,"interpretation":"C02 needs bridge discipline. 267260 shows transformer/data-center CAPEX order bridge can create a huge rerating, while 010120 and 103590 show that late price-only grid beta extension can create near-zero MFE and high MAE without fresh order/margin bridge."}
{"row_type":"stage_transition_summary","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"267260","trigger_type":"Stage2-Actionable-TransformerDatacenterCapexOrderBridge-Positive","entry_date":"2024-01-29","stage2_to_90D_outcome":"good_stage2_very_high_MFE_shallow_MAE","stage2_to_180D_outcome":"positive_transformer_capex_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when transformer order/customer/margin bridge exists; Green requires exact customer and cash-conversion evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"010120","trigger_type":"Stage2-FalsePositive-GridCapexPriceOnlyExtension-NoFreshBridge","entry_date":"2024-07-16","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_high_MAE","stage2_to_180D_outcome":"failed_late_grid_beta_extension","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Late grid-CAPEX price extension without fresh order/margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"103590","trigger_type":"Stage2-FalsePositive-WireTransformerBetaExtension-NoFreshOrderMarginBridge","entry_date":"2024-07-15","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_or_choppy_wire_transformer_beta_extension","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Wire/transformer beta without fresh customer/order/margin bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","residual_type":"power_grid_datacenter_capex_overcredit_when_only_late_price_extension_exists","contribution":"Adds two C02 local 4B/high-MAE counterexamples against one transformer/data-center CAPEX bridge positive, avoiding C02 top-covered symbols and previous R11 C03 defense evidence.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_GRID_TRANSFORMER_DATACENTER_CAPEX_BRIDGE_VS_PRICE_ONLY_GRID_BETA_EXTENSION","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C02 now has non-top-symbol late-extension counterexamples; next R11 loops should exact-URL repair order visibility, delivery-slot scarcity, customer quality, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","axis":"C02_fresh_order_customer_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"267260 worked with transformer/data-center CAPEX order bridge proxy; 010120 and 103590 failed when entry depended on late price extension without fresh order, customer or margin bridge."}
{"row_type":"shadow_weight","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","axis":"C02_late_grid_beta_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Late grid-CAPEX beta extension showed near-zero/low MFE and high MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R11","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","axis":"C02_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<5 and MAE90<=-25 while fresh order/margin bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - grid_capex_price_only_extension
  - fresh_order_customer_bridge_missing
  - delivery_slot_margin_bridge_missing
  - late_beta_high_MAE_after_valid_theme
new_axis_proposed:
  - C02_fresh_order_customer_margin_bridge_required_shadow_only
  - C02_late_grid_beta_local_4B_watch_guard_shadow_only
  - C02_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C02
  - full_4b_requires_non_price_evidence within C02
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
  - hard_4c_thesis_break_routes_to_4c
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
3. Confirm R11 / L1 / C02 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided C02 top-covered symbols and did not repeat R11 loop84 C03 symbols.
6. Confirm 103590 selected entries are after the 2024-02-13 corporate-action candidate.
7. If aggregate support remains stable after exact evidence URL repair, consider C02-scoped safe patch candidates:
   - C02_fresh_order_customer_margin_bridge_required
   - C02_late_grid_beta_local_4B_watch_guard
   - C02_high_MAE_guardrail
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R11
completed_loop = 85
next_round = R12
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R11/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX.
```
