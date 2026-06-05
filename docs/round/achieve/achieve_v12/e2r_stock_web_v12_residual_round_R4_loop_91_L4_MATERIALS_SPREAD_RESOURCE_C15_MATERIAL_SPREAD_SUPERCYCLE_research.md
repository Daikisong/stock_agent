# E2R Stock-Web v12 Residual Research — R4 Loop 91 / L4 / C15

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R4
loop: 91
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_WIRE_SPREAD_INVENTORY_BRIDGE_VS_COPPER_HOLDCO_ALUMINUM_THEME_DECAY
sector: materials / copper / aluminum / wire / nonferrous spread / inventory / margin bridge
output_file: e2r_stock_web_v12_residual_round_R4_loop_91_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R3 loop 91`.

```text
scheduled_round = R4
scheduled_loop = 91
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
```

R4 is restricted to materials / spread / resource.  
C15 is selected because the recent R4 sequence used C17, C16, and now returns to material spread / supercycle residuals.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C15_MATERIAL_SPREAD_SUPERCYCLE
rows = 28
symbols = 11
good/bad Stage2 = 13/0
4B/4C = 3/0
top-covered = 103140, 012800, 025820, 004560, 021050, 001780
```

This loop avoids the C15 top-covered list and recent R4 loop symbols:

```text
R4 loop86 C17: 120110, 010060, 009830
R4 loop87 C16: 006260, 073570, 131400
R4 loop88 C15: 024840, 006110, 004430
R4 loop89 C17: 001340, 298000, 161000
R4 loop90 C16: 128660, 009520, 018470
```

Candidate hygiene note:

```text
During this execution path, R2/C07 and R3/C13 candidate rows were touched in surrounding tool calls.
Those rows are not used in this R4/C15 output.
```

Selected symbols:

```text
006340, 005810, 008350
```

The selected pocket is:

```text
copper wire / inventory / spread bridge positive-control
vs
copper holding-company / subsidiary spread vocabulary without direct ASP-margin bridge
vs
aluminum extrusion theme rebound without spread, customer demand and cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"006340","company_name":"대원전선","profile_path":"atlas/symbol_profiles/006/006340.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7742,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1996-11-29","1997-06-19","1999-09-10","2000-03-21","2007-01-25","2010-05-07"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"005810","company_name":"풍산홀딩스","profile_path":"atlas/symbol_profiles/005/005810.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7741,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["1999-06-30","2008-07-30","2008-09-26","2021-02-18","2024-03-22"],"has_major_raw_discontinuity":true,"calibration_caveat":"2024 corporate-action candidate exists before selected 2024-04-11 entry; keep post-candidate data-quality watch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_entry_after_2024-03-22_candidate; data_quality_watch"}
{"row_type":"price_source_validation","symbol":"008350","company_name":"남선알미늄","profile_path":"atlas/symbol_profiles/008/008350.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7695,"corporate_action_candidate_count":11,"corporate_action_candidate_dates":["1996-01-03","1997-09-08","1999-05-04","1999-05-26","2001-12-21","2001-12-28","2002-09-25","2002-11-11","2004-03-11","2008-12-09","2009-10-13"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"006340","trigger_type":"Stage2-Actionable-CopperWireInventorySpreadBridge-Positive","entry_date":"2024-03-14","duplicate_status":"new C15 symbol/trigger/date combination outside C15 top-covered and previous R4 loop symbols; cross-archetype cable/grid overlap watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"005810","trigger_type":"Stage2-FalsePositive-CopperHoldcoVocabularyNoDirectSpreadMarginBridge","entry_date":"2024-04-11","duplicate_status":"new C15 symbol/trigger/date combination outside C15 top-covered and previous R4 loop symbols; post-candidate data-quality watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"008350","trigger_type":"Stage2-FalsePositive-AluminumExtrusionThemeNoSpreadCustomerCashBridge","entry_date":"2024-02-13","duplicate_status":"new C15 symbol/trigger/date combination outside C15 top-covered and previous R4 loop symbols"}
```

## 4. Research question

C15 is not “구리·알루미늄 테마가 있다.”  
The useful material-spread signal must prove the bridge from commodity move to corporate economics:

```text
input/output spread visibility
inventory revaluation or low-cost inventory benefit
ASP pass-through
customer demand / shipment
utilization
margin repair
working-capital discipline
cash conversion
```

A metal-price headline without this bridge is molten metal still inside the furnace. It glows, but the plant has not rolled, shipped, invoiced, and collected it.

Residual question:

```text
Can C15 distinguish:
1. copper-wire / inventory / spread bridge with explosive MFE and controlled MAE,
2. copper holding-company vocabulary where the underlying spread story is indirect and post-candidate data-quality watch is needed,
3. aluminum extrusion theme rebound where no spread, customer demand, margin or cash bridge appears and the path decays?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C15_R4L91_006340_DAEWON_COPPER_WIRE_SPREAD","symbol":"006340","company_name":"대원전선","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_WIRE_INVENTORY_SPREAD_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-CopperWireInventorySpreadBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"positive_extreme_MFE90_low_MAE_inventory_spread_bridge","current_profile_verdict":"current_profile_correct_if_inventory_spread_ASP_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Copper wire/inventory spread proxy produced extreme MFE with shallow MAE. Cross-archetype cable/grid overlap watch is retained; C15 contribution is only the material spread/inventory bridge."}
{"row_type":"case","case_id":"C15_R4L91_005810_POONGSAN_HOLDINGS_COPPER_HOLDCO","symbol":"005810","company_name":"풍산홀딩스","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_HOLDCO_VOCABULARY_WITHOUT_DIRECT_SPREAD_MARGIN_BRIDGE","case_type":"weak_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CopperHoldcoVocabularyNoDirectSpreadMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"score_price_alignment":"counterexample_low_MFE_moderate_MAE_post_candidate_watch","current_profile_verdict":"current_profile_false_positive_if_copper_holdco_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Copper holding-company vocabulary had low MFE and later drawdown when direct spread, ASP, shipment, margin and cash bridge were not repaired. 2024 post-candidate data-quality watch is retained."}
{"row_type":"case","case_id":"C15_R4L91_008350_NAMSUN_ALUMINUM_THEME","symbol":"008350","company_name":"남선알미늄","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINUM_EXTRUSION_THEME_WITHOUT_SPREAD_CUSTOMER_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-AluminumExtrusionThemeNoSpreadCustomerCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_no_spread_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_aluminum_theme_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Aluminum extrusion/materials rebound had near-zero MFE and deep 180D MAE without spread, customer demand, margin and cash evidence."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 006340 대원전선 — copper wire / inventory spread bridge positive-control

Entry row: `2024-03-14 c=1358`.  
Observed path: entry-area low `2024-03-14 l=1302`, copper/wire spread ramp to `2024-05-13 h=5450`, and later full-window low `2024-12-09 l=2205`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L91_C15_006340_20240314_STAGE2_COPPER_WIRE_SPREAD","case_id":"C15_R4L91_006340_DAEWON_COPPER_WIRE_SPREAD","symbol":"006340","company_name":"대원전선","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_WIRE_INVENTORY_SPREAD_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-CopperWireInventorySpreadBridge-Positive","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":1358.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_copper_wire_inventory_spread_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; copper wire inventory, ASP pass-through and spread/margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["copper_wire_spread_proxy","inventory_revaluation_proxy","ASP_pass_through_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_inventory_source_pending","ASP_customer_source_pending","shipment_volume_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","cross_archetype_grid_overlap_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv","profile_path":"atlas/symbol_profiles/006/006340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":129.75,"MFE_90D_pct":301.33,"MFE_180D_pct":301.33,"MAE_30D_pct":-4.12,"MAE_90D_pct":-4.12,"MAE_180D_pct":-4.12,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-13","peak_price":5450.0,"max_drawdown_low_date":"2024-03-14","max_drawdown_low":1302.0,"drawdown_after_peak_pct":-59.54,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.57,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_inventory_ASP_customer_margin_cash_evidence_and_cross_archetype_overlap_check","four_b_evidence_type":["price_extension_watch","cross_archetype_overlap_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_extreme_MFE90_low_MAE_inventory_spread_bridge","current_profile_verdict":"current_profile_correct_if_inventory_spread_ASP_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["cross_archetype_cable_grid_overlap_watch"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"006340_2024-03-14_1358","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C15 can allow Stage2/Yellow when material strength is tied to copper wire inventory, ASP pass-through, shipment/customer demand, margin and cash conversion. Green still requires exact source-grade evidence and overlap repair."}
```

### 6.2 005810 풍산홀딩스 — copper holding-company vocabulary without direct spread-margin bridge

Entry row: `2024-04-11 c=31600`, after the 2024-03-22 corporate-action candidate.  
Observed path: local high `2024-05-13 h=34000`, then low `2024-12-09 l=23950`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L91_C15_005810_20240411_STAGE2_FALSE_POSITIVE_COPPER_HOLDCO","case_id":"C15_R4L91_005810_POONGSAN_HOLDINGS_COPPER_HOLDCO","symbol":"005810","company_name":"풍산홀딩스","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_HOLDCO_VOCABULARY_WITHOUT_DIRECT_SPREAD_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;data_quality_watch","trigger_type":"Stage2-FalsePositive-CopperHoldcoVocabularyNoDirectSpreadMarginBridge","trigger_date":"2024-04-11","entry_date":"2024-04-11","entry_price":31600.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_copper_holdco_subsidiary_material_spread_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; holding-company/subsidiary copper vocabulary treated as insufficient without direct inventory, ASP, spread, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["copper_holdco_vocabulary","subsidiary_material_theme","relative_strength_rebound"],"stage3_evidence_fields":["direct_inventory_bridge_missing","ASP_pass_through_missing","spread_margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["low_MFE_watch","post_candidate_data_quality_watch","direct_spread_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005810/2024.csv","profile_path":"atlas/symbol_profiles/005/005810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.59,"MFE_90D_pct":7.59,"MFE_180D_pct":7.59,"MAE_30D_pct":-7.75,"MAE_90D_pct":-15.35,"MAE_180D_pct":-24.21,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-13","peak_price":34000.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":23950.0,"drawdown_after_peak_pct":-29.56,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"copper_holdco_vocabulary_without_direct_inventory_ASP_margin_cash_bridge_should_be_4B_watch_not_positive; post_candidate_data_quality_watch_before_patch","four_b_evidence_type":["low_MFE","post_candidate_data_quality_watch","direct_spread_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_moderate_MAE_post_candidate_watch","current_profile_verdict":"current_profile_false_positive_if_copper_holdco_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["post_2024_corporate_action_candidate_data_quality_watch"],"corporate_action_window_status":"selected_entry_after_2024-03-22_candidate; data_quality_watch","same_entry_group_id":"005810_2024-04-11_31600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"do_not_count_as_new_case":false,"current_profile_residual":"C15 should not promote copper holding-company vocabulary unless direct inventory, ASP, spread/margin and cash evidence are repaired. Low MFE and data-quality watch require 4B/evidence-repair routing."}
```

### 6.3 008350 남선알미늄 — aluminum extrusion theme without spread/customer/cash bridge

Entry row: `2024-02-13 c=2155`.  
Observed path: same-day high `2024-02-13 h=2180`, then prolonged decay to `2024-12-09 l=1200`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L91_C15_008350_20240213_STAGE2_FALSE_POSITIVE_ALUMINUM_EXTRUSION","case_id":"C15_R4L91_008350_NAMSUN_ALUMINUM_THEME","symbol":"008350","company_name":"남선알미늄","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINUM_EXTRUSION_THEME_WITHOUT_SPREAD_CUSTOMER_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-AluminumExtrusionThemeNoSpreadCustomerCashBridge","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":2155.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_aluminum_extrusion_material_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; aluminum extrusion/material theme treated as insufficient without spread/ASP, customer demand, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["aluminum_extrusion_theme","material_price_keyword","relative_strength_rebound"],"stage3_evidence_fields":["spread_ASP_bridge_missing","customer_demand_missing","margin_cash_bridge_missing","inventory_bridge_missing"],"stage4b_evidence_fields":["near_zero_MFE","spread_cash_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008350/2024.csv","profile_path":"atlas/symbol_profiles/008/008350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.16,"MFE_90D_pct":1.16,"MFE_180D_pct":1.16,"MAE_30D_pct":-11.14,"MAE_90D_pct":-18.84,"MAE_180D_pct":-44.32,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-13","peak_price":2180.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":1200.0,"drawdown_after_peak_pct":-44.95,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"aluminum_extrusion_theme_without_spread_customer_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["near_zero_MFE","spread_cash_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_spread_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_aluminum_theme_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"008350_2024-02-13_2155","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C15 should not equate aluminum theme vocabulary with material spread evidence. Spread/ASP pass-through, customer demand, margin and cash bridge must be exact-repaired before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C15_R4L91_006340_DAEWON_COPPER_WIRE_SPREAD","trigger_id":"R4L91_C15_006340_20240314_STAGE2_COPPER_WIRE_SPREAD","symbol":"006340","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C15 requires inventory/spread/ASP/customer/margin/cash bridge rather than copper theme alone","raw_component_scores_before":{"material_spread_score":14,"inventory_revaluation_score":13,"ASP_pass_through_score":12,"customer_shipment_score":10,"utilization_score":9,"margin_bridge_score":11,"cash_conversion_score":7,"relative_strength_score":16,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"material_spread_score":17,"inventory_revaluation_score":16,"ASP_pass_through_score":15,"customer_shipment_score":12,"utilization_score":11,"margin_bridge_score":13,"cash_conversion_score":9,"relative_strength_score":17,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":90,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Copper wire inventory/spread bridge plus extreme MFE supports Yellow/Green-candidate watch; exact evidence and cross-archetype overlap repair block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C15_R4L91_005810_POONGSAN_HOLDINGS_COPPER_HOLDCO","trigger_id":"R4L91_C15_005810_20240411_STAGE2_FALSE_POSITIVE_COPPER_HOLDCO","symbol":"005810","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","profile_scope":"current_default_proxy","profile_hypothesis":"copper holdco vocabulary without direct spread/margin bridge should be blocked or kept data-quality-watch","raw_component_scores_before":{"material_spread_score":3,"inventory_revaluation_score":1,"ASP_pass_through_score":1,"customer_shipment_score":1,"utilization_score":1,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":6,"valuation_repricing_score":3,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"material_spread_score":1,"inventory_revaluation_score":0,"ASP_pass_through_score":0,"customer_shipment_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-20,"theme_spike_risk":-18,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Low MFE, moderate MAE and post-candidate data-quality watch block Yellow/Green until direct spread and price-path repair."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C15_R4L91_008350_NAMSUN_ALUMINUM_THEME","trigger_id":"R4L91_C15_008350_20240213_STAGE2_FALSE_POSITIVE_ALUMINUM_EXTRUSION","symbol":"008350","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","profile_scope":"current_default_proxy","profile_hypothesis":"aluminum extrusion/material theme without spread and customer cash bridge should remain Watch/4B","raw_component_scores_before":{"material_spread_score":2,"inventory_revaluation_score":0,"ASP_pass_through_score":1,"customer_shipment_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":2,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"material_spread_score":0,"inventory_revaluation_score":0,"ASP_pass_through_score":0,"customer_shipment_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE require spread/ASP, customer demand, margin and cash evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R4L91_C15_P0_CURRENT","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C15 needs explicit inventory/spread/ASP/customer/margin/cash bridge and holdco/aluminum vocabulary 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":103.36,"avg_MAE90_pct":-12.77,"avg_MFE180_pct":103.36,"avg_MAE180_pct":-24.22,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.86,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C15_inventory_spread_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R4L91_C15_P1_SECTOR_SPECIFIC","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","profile_id":"P1_L4_material_spread_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L4 material-spread signals need input/output spread, inventory benefit, ASP pass-through, shipment/customer demand, margin or cash conversion before Stage2-Actionable","changed_axes":["spread_inventory_required","ASP_margin_cash_required","holdco_material_vocabulary_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_spread_inventory_ASP_customer_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":103.36,"avg_MAE90_pct":-12.77,"avg_MFE180_pct":103.36,"avg_MAE180_pct":-24.22,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R4L91_C15_P2_CANONICAL","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","profile_id":"P2_C15_inventory_spread_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C15 should reward inventory-to-spread-to-margin mechanics, not copper/aluminum vocabulary","changed_axes":["C15_inventory_spread_ASP_margin_cash_bridge_required","C15_holdco_aluminum_vocabulary_local_4B_guard","C15_cross_archetype_overlap_data_quality_guard"],"changed_thresholds":{"stage2_yellow_gate":"inventory_or_spread_plus_ASP_or_margin_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":103.36,"avg_MAE90_pct":-12.77,"avg_MFE180_pct":103.36,"avg_MAE180_pct":-24.22,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R4L91_C15_P3_COUNTEREXAMPLE_GUARD","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","profile_id":"P3_C15_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If spread/margin bridge is missing, MFE90<10 or MAE180<=-20 should block Yellow/Green and route to 4B-watch","changed_axes":["C15_low_MFE_guardrail","C15_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_10_or_MAE180_le_minus_20)"},"eligible_trigger_count":3,"avg_MFE90_pct":103.36,"avg_MAE90_pct":-12.77,"avg_MFE180_pct":103.36,"avg_MAE180_pct":-24.22,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_COPPER_WIRE_POSITIVE_VS_COPPER_HOLDCO_ALUMINUM_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":103.36,"avg_MAE90_pct":-12.77,"avg_MFE180_pct":103.36,"avg_MAE180_pct":-24.22,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"data_quality_watch_count":1,"interpretation":"C15 needs bridge discipline. 대원전선 shows copper-wire inventory/spread bridge can generate extreme MFE, while 풍산홀딩스 and 남선알미늄 show copper-holdco or aluminum vocabulary should not be promoted without direct spread, ASP, customer demand, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"006340","trigger_type":"Stage2-Actionable-CopperWireInventorySpreadBridge-Positive","entry_date":"2024-03-14","stage2_to_90D_outcome":"good_stage2_extreme_MFE_low_MAE","stage2_to_180D_outcome":"positive_inventory_spread_bridge_but_cross_archetype_overlap_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when copper strength is tied to inventory/spread/ASP/margin bridge; Green requires exact evidence and overlap repair."}
{"row_type":"stage_transition_summary","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"005810","trigger_type":"Stage2-FalsePositive-CopperHoldcoVocabularyNoDirectSpreadMarginBridge","entry_date":"2024-04-11","stage2_to_90D_outcome":"weak_stage2_low_MFE_data_quality_watch","stage2_to_180D_outcome":"failed_copper_holdco_vocabulary_moderate_MAE","MFE90_ge20":false,"MAE180_le_minus20":true,"transition_note":"Copper holdco vocabulary without direct inventory/spread and margin/cash bridge should stay Watch/4B-risk; post-candidate data-quality watch remains."}
{"row_type":"stage_transition_summary","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"008350","trigger_type":"Stage2-FalsePositive-AluminumExtrusionThemeNoSpreadCustomerCashBridge","entry_date":"2024-02-13","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_bridge_missing","stage2_to_180D_outcome":"failed_aluminum_theme_deep_MAE","MFE90_ge20":false,"MAE180_le_minus20":true,"transition_note":"Aluminum extrusion/materials rebound without spread/customer/margin bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","residual_type":"copper_holdco_aluminum_materials_vocabulary_overcredit_without_inventory_spread_margin_cash_bridge","contribution":"Adds two C15 4B/data-quality-watch counterexamples against one copper-wire spread positive, avoiding C15 top-covered and recent R4 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_WIRE_SPREAD_INVENTORY_BRIDGE_VS_COPPER_HOLDCO_ALUMINUM_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C15 now has non-top-symbol copper-wire spread positive and two copper-holdco/aluminum weak-bridge counterexamples; next R4 C15 loops should exact-URL repair inventory, ASP pass-through, customer shipments, utilization, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","axis":"C15_inventory_spread_ASP_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"006340 worked when copper-wire inventory/spread proxy existed; 005810 and 008350 failed when material vocabulary lacked direct spread, ASP, margin and cash evidence."}
{"row_type":"shadow_weight","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","axis":"C15_holdco_aluminum_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Copper-holdco and aluminum-extrusion vocabulary rows showed low or near-zero MFE and drawdown when direct spread/margin evidence was missing."}
{"row_type":"shadow_weight","round":"R4","loop":"91","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","axis":"C15_cross_archetype_overlap_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"006340 has cable/grid overlap risk and 005810 has post-2024-candidate data-quality watch; both require repair before patch consideration."}
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
  - copper_holdco_vocabulary_overcredit
  - aluminum_materials_theme_overcredit
  - direct_inventory_spread_bridge_missing
  - ASP_margin_cash_bridge_missing
  - cross_archetype_overlap_watch
new_axis_proposed:
  - C15_inventory_spread_ASP_margin_cash_bridge_required_shadow_only
  - C15_holdco_aluminum_vocabulary_local_4B_guard_shadow_only
  - C15_cross_archetype_overlap_data_quality_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C15
  - full_4b_requires_non_price_evidence within C15
  - hard_4c_thesis_break_routes_to_4c within C15
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
`006340` has only historical corporate-action candidates before 2024, but it also carries cable/grid overlap watch because the same symbol can be interpreted through C02 if non-price evidence is sloppy.  
`005810` has a 2024-03-22 corporate-action candidate before the selected entry, so it remains data-quality-watch before any production patch.  
`008350` has old corporate-action candidates before 2024; the selected 2024 forward window is usable.  
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
data_quality_watch = true for 005810
cross_archetype_overlap_watch = true for 006340
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
3. Confirm R4 / L4 / C15 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C15 top-covered symbols
   - previous R4 loop86 C17 symbols
   - previous R4 loop87 C16 symbols
   - previous R4 loop88 C15 symbols
   - previous R4 loop89 C17 symbols
   - previous R4 loop90 C16 symbols
6. Confirm accidentally touched R2/C07 and R3/C13 candidate rows are not ingested from this MD.
7. Keep 005810 in post-candidate data-quality watch before patch consideration.
8. Treat 006340 as C15 material-spread evidence only after exact inventory/ASP/customer evidence repair; do not let C02 grid/cable overlap double-count.
9. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C15-scoped safe patch candidates:
   - C15_inventory_spread_ASP_margin_cash_bridge_required
   - C15_holdco_aluminum_vocabulary_local_4B_guard
   - C15_cross_archetype_overlap_data_quality_guard
10. Do not loosen Stage3-Green.
11. Do not use future MFE/MAE in runtime scoring.
12. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R4
completed_loop = 91
next_round = R5
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE.
```
