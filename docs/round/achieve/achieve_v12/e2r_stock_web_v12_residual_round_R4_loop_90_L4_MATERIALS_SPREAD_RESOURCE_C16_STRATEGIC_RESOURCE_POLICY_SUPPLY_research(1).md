# E2R Stock-Web v12 Residual Research — R4 Loop 90 / L4 / C16

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R4
loop: 90
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: ALUMINUM_NONFERROUS_SUPPLY_POLICY_BRIDGE_VS_LITHIUM_ALUMINUM_THEME_DECAY
sector: materials / strategic resource / nonferrous metals / aluminum / lithium-materials theme / supply policy
output_file: e2r_stock_web_v12_residual_round_R4_loop_90_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R3 loop 90`.

```text
scheduled_round = R4
scheduled_loop = 90
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```

R4 is restricted to materials / spread / resource.  
C16 is selected because the immediately previous R4 loop used C17 chemical commodity margin spread, while C16 still has a large mixture of true strategic-supply cases and price-only resource theme rebounds.

No-Repeat Index snapshot:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
rows = 36
symbols = 23
good/bad Stage2 = 14/9
4B/4C = 2/0
top-covered = 047400, 005490, 012320, 001570, 081150, 101670
```

This loop avoids the C16 top-covered list and recent R4 symbols:

```text
R4 loop86 C17: 120110, 010060, 009830
R4 loop87 C16: 006260, 073570, 131400
R4 loop88 C15: 024840, 006110, 004430
R4 loop89 C17: 001340, 298000, 161000
```

Selected symbols:

```text
128660, 009520, 018470
```

This loop tests:

```text
aluminum / nonferrous resource supply bridge
vs
lithium-materials / POSCO-chain theme spike without fresh resource-supply margin bridge
vs
aluminum foil/sheet rebound without customer demand, spread or cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"128660","company_name":"피제이메탈","profile_path":"atlas/symbol_profiles/128/128660.json","first_date":"2010-12-13","last_date":"2026-02-20","trading_day_count":3735,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"009520","company_name":"포스코엠텍","profile_path":"atlas/symbol_profiles/009/009520.json","first_date":"1997-11-10","last_date":"2026-02-20","trading_day_count":6770,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1999-03-30","1999-04-22","2011-01-05","2012-05-14"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 window. Market segment changed to KOSDAQ GLOBAL on 2024-06-14, but price path remains usable as raw tradable row evidence.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry; market_segment_change_watch"}
{"row_type":"price_source_validation","symbol":"018470","company_name":"조일알미늄","profile_path":"atlas/symbol_profiles/018/018470.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7738,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1996-01-03","1999-12-07","2012-05-04"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist long before selected 2024 window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"128660","trigger_type":"Stage2-Actionable-AluminumNonferrousSupplyPolicyBridge-Positive","entry_date":"2024-04-12","duplicate_status":"new C16 symbol/trigger/date combination outside top-covered and previous R4 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"009520","trigger_type":"Stage2-FalsePositive-LithiumMaterialsThemeNoFreshSupplyMarginBridge","entry_date":"2024-06-11","duplicate_status":"new C16 symbol/trigger/date combination outside top-covered and previous R4 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"018470","trigger_type":"Stage2-FalsePositive-AluminumSheetReboundNoCustomerSpreadCashBridge","entry_date":"2024-02-20","duplicate_status":"new C16 symbol/trigger/date combination outside top-covered and previous R4 loop symbols"}
```

## 4. Research question

C16 is not “자원주가 올랐다.”  
The useful strategic-resource signal must prove a supply-chain bridge:

```text
resource policy or supply security
nonferrous/strategic material demand
customer offtake or downstream channel
inventory discipline
capacity or utilization
spread / ASP pass-through
margin bridge
cash conversion
```

A resource headline without this bridge is ore still inside the mountain. The market may point to it, but E2R needs the mine-mouth logistics, customer route and margin conversion.

Residual question:

```text
Can C16 distinguish:
1. aluminum / nonferrous supply-policy bridge with high MFE and controlled early MAE,
2. lithium-materials / POSCO-chain theme spike where no fresh supply, offtake, margin or cash bridge exists,
3. aluminum foil/sheet rebound where customer demand and spread conversion fail to materialize?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C16_R4L90_128660_PJ_METAL_ALUMINUM_SUPPLY","symbol":"128660","company_name":"피제이메탈","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"ALUMINUM_NONFERROUS_SUPPLY_POLICY_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-AluminumNonferrousSupplyPolicyBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_low_early_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_supply_policy_spread_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Aluminum/nonferrous supply-policy proxy produced high MFE with shallow early MAE. Later drawdown keeps Green strict and requires exact resource policy, customer demand, spread and cash evidence."}
{"row_type":"case","case_id":"C16_R4L90_009520_POSCO_MTECH_LITHIUM_THEME","symbol":"009520","company_name":"포스코엠텍","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_MATERIALS_THEME_WITHOUT_FRESH_SUPPLY_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LithiumMaterialsThemeNoFreshSupplyMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_lithium_materials_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Lithium/materials theme spike had sub-10 MFE from selected entry and deep later MAE without fresh offtake, resource supply, spread/margin and cash bridge."}
{"row_type":"case","case_id":"C16_R4L90_018470_CHOIL_ALUMINUM_SHEET_REBOUND","symbol":"018470","company_name":"조일알미늄","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"ALUMINUM_SHEET_REBOUND_WITHOUT_CUSTOMER_SPREAD_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-AluminumSheetReboundNoCustomerSpreadCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_aluminum_sheet_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Aluminum foil/sheet rebound had low local MFE and deep 180D MAE without confirmed customer demand, spread, margin or cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 128660 피제이메탈 — aluminum / nonferrous supply-policy bridge positive

Entry row: `2024-04-12 c=3315`.  
Observed path: entry-area low `2024-04-12 l=3255`, peak `2024-05-21 h=5390`, and late low `2024-12-09 l=2575`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L90_C16_128660_20240412_STAGE2_ALUMINUM_SUPPLY","case_id":"C16_R4L90_128660_PJ_METAL_ALUMINUM_SUPPLY","symbol":"128660","company_name":"피제이메탈","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"ALUMINUM_NONFERROUS_SUPPLY_POLICY_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-AluminumNonferrousSupplyPolicyBridge-Positive","trigger_date":"2024-04-12","entry_date":"2024-04-12","entry_price":3315.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_aluminum_nonferrous_supply_policy_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; aluminum/nonferrous supply policy, demand and spread bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["aluminum_supply_policy_proxy","nonferrous_demand_proxy","spread_ASP_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_policy_source_pending","customer_demand_source_pending","inventory_or_capacity_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/128/128660/2024.csv","profile_path":"atlas/symbol_profiles/128/128660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":62.59,"MFE_90D_pct":62.59,"MFE_180D_pct":62.59,"MAE_30D_pct":-1.81,"MAE_90D_pct":-1.81,"MAE_180D_pct":-22.32,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":5390.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":2575.0,"drawdown_after_peak_pct":-52.23,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_resource_policy_spread_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_low_early_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_supply_policy_spread_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"128660_2024-04-12_3315","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C16 can allow Stage2/Yellow when resource strength is tied to nonferrous supply policy, customer demand, spread/ASP pass-through, margin and cash conversion. Green still requires exact source-grade evidence."}
```

### 6.2 009520 포스코엠텍 — lithium/materials theme without fresh supply-margin bridge

Entry row: `2024-06-11 c=22550`, on a materials/resource theme spike.  
Observed path: same-day high `2024-06-11 h=24700`, then drawdown to `2024-12-27 l=11700`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L90_C16_009520_20240611_STAGE2_FALSE_POSITIVE_LITHIUM_THEME","case_id":"C16_R4L90_009520_POSCO_MTECH_LITHIUM_THEME","symbol":"009520","company_name":"포스코엠텍","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_MATERIALS_THEME_WITHOUT_FRESH_SUPPLY_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-LithiumMaterialsThemeNoFreshSupplyMarginBridge","trigger_date":"2024-06-11","entry_date":"2024-06-11","entry_price":22550.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_lithium_POSCO_materials_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; lithium/POSCO-chain materials theme treated as insufficient without fresh resource supply, offtake, capacity, spread/margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["lithium_materials_theme","POSCO_chain_keyword","relative_strength_spike"],"stage3_evidence_fields":["fresh_supply_bridge_missing","offtake_or_customer_demand_missing","capacity_utilization_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_MFE","supply_margin_bridge_missing_watch","deep_180D_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009520/2024.csv","profile_path":"atlas/symbol_profiles/009/009520.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.53,"MFE_90D_pct":9.53,"MFE_180D_pct":9.53,"MAE_30D_pct":-13.44,"MAE_90D_pct":-22.84,"MAE_180D_pct":-48.12,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":24700.0,"max_drawdown_low_date":"2024-12-27","max_drawdown_low":11700.0,"drawdown_after_peak_pct":-52.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"lithium_materials_theme_without_resource_supply_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","supply_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_lithium_materials_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["market_segment_change_watch_KOSDAQ_to_KOSDAQ_GLOBAL_after_entry"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean; market_segment_change_watch","same_entry_group_id":"009520_2024-06-11_22550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C16 should not promote lithium/materials price spikes unless fresh resource supply, offtake/customer demand, capacity, spread/margin and cash bridge are repaired. Low MFE and deep MAE require 4B-watch."}
```

### 6.3 018470 조일알미늄 — aluminum sheet rebound without customer/spread/cash bridge

Entry row: `2024-02-20 c=2095`.  
Observed path: same-day high `2024-02-20 h=2220`, later commodity/theme bursts but final 180D path decayed to `2024-12-09 l=1264`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L90_C16_018470_20240220_STAGE2_FALSE_POSITIVE_ALUMINUM_SHEET","case_id":"C16_R4L90_018470_CHOIL_ALUMINUM_SHEET_REBOUND","symbol":"018470","company_name":"조일알미늄","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"ALUMINUM_SHEET_REBOUND_WITHOUT_CUSTOMER_SPREAD_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-AluminumSheetReboundNoCustomerSpreadCashBridge","trigger_date":"2024-02-20","entry_date":"2024-02-20","entry_price":2095.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_aluminum_sheet_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; aluminum sheet/foil rebound treated as insufficient without confirmed customer demand, supply-policy pass-through, spread/margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["aluminum_sheet_rebound","nonferrous_theme","relative_strength_rebound"],"stage3_evidence_fields":["customer_demand_bridge_missing","spread_ASP_bridge_missing","capacity_utilization_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE_watch","customer_spread_bridge_missing_watch","deep_180D_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018470/2024.csv","profile_path":"atlas/symbol_profiles/018/018470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.97,"MFE_90D_pct":5.97,"MFE_180D_pct":5.97,"MAE_30D_pct":-5.25,"MAE_90D_pct":-6.78,"MAE_180D_pct":-39.67,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-20","peak_price":2220.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":1264.0,"drawdown_after_peak_pct":-43.06,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"aluminum_sheet_rebound_without_customer_spread_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","customer_spread_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_aluminum_sheet_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"018470_2024-02-20_2095","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C16 should not equate aluminum sheet price rebound with strategic supply bridge. Customer demand, spread/ASP pass-through, utilization, margin and cash conversion must be exact-repaired before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C16_R4L90_128660_PJ_METAL_ALUMINUM_SUPPLY","trigger_id":"R4L90_C16_128660_20240412_STAGE2_ALUMINUM_SUPPLY","symbol":"128660","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C16 requires resource policy, customer demand, capacity/inventory, spread/margin and cash bridge rather than resource theme alone","raw_component_scores_before":{"resource_policy_score":12,"supply_security_score":12,"customer_demand_score":10,"capacity_utilization_score":9,"spread_ASP_score":11,"margin_bridge_score":9,"cash_conversion_score":6,"relative_strength_score":14,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":71,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"resource_policy_score":15,"supply_security_score":15,"customer_demand_score":12,"capacity_utilization_score":11,"spread_ASP_score":14,"margin_bridge_score":11,"cash_conversion_score":8,"relative_strength_score":15,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Aluminum supply/spread bridge plus high MFE supports Yellow-watch; late drawdown and proxy-only evidence block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C16_R4L90_009520_POSCO_MTECH_LITHIUM_THEME","trigger_id":"R4L90_C16_009520_20240611_STAGE2_FALSE_POSITIVE_LITHIUM_THEME","symbol":"009520","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_scope":"current_default_proxy","profile_hypothesis":"lithium/materials theme without fresh supply and margin bridge should be blocked","raw_component_scores_before":{"resource_policy_score":3,"supply_security_score":2,"customer_demand_score":1,"capacity_utilization_score":0,"spread_ASP_score":1,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":10,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"resource_policy_score":1,"supply_security_score":0,"customer_demand_score":0,"capacity_utilization_score":0,"spread_ASP_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep 180D MAE convert lithium/materials theme into missing supply-margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C16_R4L90_018470_CHOIL_ALUMINUM_SHEET_REBOUND","trigger_id":"R4L90_C16_018470_20240220_STAGE2_FALSE_POSITIVE_ALUMINUM_SHEET","symbol":"018470","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_scope":"current_default_proxy","profile_hypothesis":"aluminum sheet rebound without customer/spread/cash bridge should remain Watch/4B","raw_component_scores_before":{"resource_policy_score":2,"supply_security_score":2,"customer_demand_score":0,"capacity_utilization_score":1,"spread_ASP_score":1,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":6,"valuation_repricing_score":2,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"resource_policy_score":0,"supply_security_score":0,"customer_demand_score":0,"capacity_utilization_score":0,"spread_ASP_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-20,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero/low MFE and deep 180D MAE require customer demand, spread, margin and cash evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R4L90_C16_P0_CURRENT","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C16 needs explicit resource policy, supply security, customer demand, spread/margin/cash and price-only resource-theme taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":26.03,"avg_MAE90_pct":-10.48,"avg_MFE180_pct":26.03,"avg_MAE180_pct":-36.70,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C16_supply_spread_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R4L90_C16_P1_SECTOR_SPECIFIC","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_id":"P1_L4_strategic_resource_supply_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L4 strategic-resource signals need policy specificity, supply security, customer demand, capacity/utilization, spread/ASP, margin or cash conversion before Stage2-Actionable","changed_axes":["resource_policy_required","supply_spread_margin_required","resource_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_policy_supply_customer_capacity_spread_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":26.03,"avg_MAE90_pct":-10.48,"avg_MFE180_pct":26.03,"avg_MAE180_pct":-36.70,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R4L90_C16_P2_CANONICAL","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_id":"P2_C16_supply_spread_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C16 should reward supply-to-margin mechanics, not lithium/aluminum price labels","changed_axes":["C16_supply_spread_margin_cash_bridge_required","C16_lithium_aluminum_theme_local_4B_guard","C16_price_only_MFE_not_supply_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"policy_or_supply_security_plus_spread_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":26.03,"avg_MAE90_pct":-10.48,"avg_MFE180_pct":26.03,"avg_MAE180_pct":-36.70,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R4L90_C16_P3_COUNTEREXAMPLE_GUARD","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","profile_id":"P3_C16_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If supply/spread bridge is missing, MFE90<10 or MAE180<=-35 should block Yellow/Green and route to 4B-watch","changed_axes":["C16_low_MFE_guardrail","C16_deep_180D_MAE_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_10_or_MAE180_le_minus_35)"},"eligible_trigger_count":3,"avg_MFE90_pct":26.03,"avg_MAE90_pct":-10.48,"avg_MFE180_pct":26.03,"avg_MAE180_pct":-36.70,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_ALUMINUM_SUPPLY_POSITIVE_VS_RESOURCE_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":26.03,"avg_MAE90_pct":-10.48,"avg_MFE180_pct":26.03,"avg_MAE180_pct":-36.70,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE180_le_minus35":0.67,"interpretation":"C16 needs bridge discipline. 피제이메탈 shows aluminum/nonferrous supply-policy bridge can support Yellow-watch, while 포스코엠텍 and 조일알미늄 show lithium/aluminum theme rebounds should not be promoted without fresh supply, customer demand, spread, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"128660","trigger_type":"Stage2-Actionable-AluminumNonferrousSupplyPolicyBridge-Positive","entry_date":"2024-04-12","stage2_to_90D_outcome":"good_stage2_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_supply_bridge_but_late_drawdown_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when resource policy is tied to supply, demand, spread/margin and cash bridge; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"009520","trigger_type":"Stage2-FalsePositive-LithiumMaterialsThemeNoFreshSupplyMarginBridge","entry_date":"2024-06-11","stage2_to_90D_outcome":"bad_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"failed_lithium_materials_theme_deep_MAE","MFE90_ge20":false,"MAE180_le_minus35":true,"transition_note":"Lithium/materials theme without fresh supply and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"018470","trigger_type":"Stage2-FalsePositive-AluminumSheetReboundNoCustomerSpreadCashBridge","entry_date":"2024-02-20","stage2_to_90D_outcome":"weak_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"failed_aluminum_sheet_rebound_deep_MAE","MFE90_ge20":false,"MAE180_le_minus35":true,"transition_note":"Aluminum sheet rebound without demand/spread/cash bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","residual_type":"lithium_aluminum_theme_overcredit_without_supply_spread_margin_cash_bridge","contribution":"Adds two C16 4B counterexamples against one aluminum/nonferrous supply positive, avoiding C16 top-covered and recent R4 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"ALUMINUM_NONFERROUS_SUPPLY_POLICY_BRIDGE_VS_LITHIUM_ALUMINUM_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C16 now has non-top-symbol aluminum/nonferrous supply positive and two lithium/aluminum weak-bridge counterexamples; next R4 C16 loops should exact-URL repair resource policy, supply security, customer demand, capacity/inventory, spread/ASP, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","axis":"C16_supply_spread_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"128660 worked when aluminum/nonferrous supply-spread proxy existed; 009520 and 018470 failed when resource theme lacked supply, spread, margin and cash bridge."}
{"row_type":"shadow_weight","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","axis":"C16_lithium_aluminum_theme_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Lithium and aluminum-sheet theme rows showed MFE90 below 10 and deep 180D MAE when non-price supply/margin evidence was missing."}
{"row_type":"shadow_weight","round":"R4","loop":"90","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","axis":"C16_price_only_MFE_not_supply_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"009520 and 018470 show local resource-theme MFE should not validate C16 unless supply, spread/margin and cash evidence are repaired."}
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
  - lithium_materials_theme_overcredit
  - aluminum_rebound_overcredit
  - resource_policy_supply_bridge_missing
  - spread_margin_cash_bridge_missing
new_axis_proposed:
  - C16_supply_spread_margin_cash_bridge_required_shadow_only
  - C16_lithium_aluminum_theme_local_4B_guard_shadow_only
  - C16_price_only_MFE_not_supply_validation_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows and clean selected 2024 entry windows.  
`009520` has a 2024 market-segment change to KOSDAQ GLOBAL after the selected entry; the price path is usable but should keep market-segment-change watch before patching.  
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
market_segment_change_watch = true for 009520
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
   - previous R4 loop86 C17 symbols
   - previous R4 loop87 C16 symbols
   - previous R4 loop88 C15 symbols
   - previous R4 loop89 C17 symbols
6. Keep 009520 in market-segment-change watch before patch consideration.
7. If aggregate support remains stable after exact evidence URL repair, consider C16-scoped safe patch candidates:
   - C16_supply_spread_margin_cash_bridge_required
   - C16_lithium_aluminum_theme_local_4B_guard
   - C16_price_only_MFE_not_supply_validation_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R4
completed_loop = 90
next_round = R5
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.
```
