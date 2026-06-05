# E2R Stock-Web v12 Residual Research — R4 Loop 88 / L4 / C15

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R4
loop: 88
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_METAL_SUPERCYCLE_SPREAD_BRIDGE_VS_ALUMINUM_CHEMICAL_REBOUND_NO_MARGIN_BRIDGE
sector: materials / copper / aluminum / specialty chemical / spread / margin bridge
output_file: e2r_stock_web_v12_residual_round_R4_loop_88_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R3 loop 88`.

```text
scheduled_round = R4
scheduled_loop = 88
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
```

R4 is restricted to L4 materials / spread / resource.  
C15 is selected because recent R4 loops used C17 chemical commodity margin spread and C16 strategic resource policy supply. C15 is the material-spread / supercycle bucket.

No-Repeat Index snapshot:

```text
C15_MATERIAL_SPREAD_SUPERCYCLE
rows = 28
symbols = 11
good/bad Stage2 = 13/0
4B/4C = 3/0
top-covered = 103140, 012800, 025820, 004560, 021050, 001780
```

This loop avoids the top-covered symbols and also avoids recent R4 loop symbols:

```text
R4 loop86 C17: 120110, 010060, 009830
R4 loop87 C16: 006260, 073570, 131400
```

Selected symbols:

```text
024840, 006110, 004430
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"024840","company_name":"KBI메탈","profile_path":"atlas/symbol_profiles/024/024840.json","first_date":"1996-07-23","last_date":"2026-02-20","trading_day_count":6478,"corporate_action_candidate_count":15,"has_major_raw_discontinuity":true,"calibration_caveat":"Profile has historical corporate-action candidates; selected 2024 price window is used with share-count-change watch and should be exact-data repaired before any production patch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_2024_price_path_usable_with_data_quality_watch"}
{"row_type":"price_source_validation","symbol":"006110","company_name":"삼아알미늄","profile_path":"atlas/symbol_profiles/006/006110.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7041,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["2000-10-16","2000-11-14","2007-05-04","2011-04-26","2023-02-09"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"004430","company_name":"송원산업","profile_path":"atlas/symbol_profiles/004/004430.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7707,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1997-01-03","2004-02-10","2004-04-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"024840","trigger_type":"Stage2-Actionable-CopperMetalSupercycleSpreadBridge-Positive","entry_date":"2024-04-12","duplicate_status":"new C15 symbol/trigger/date combination outside top-covered and recent R4 C16/C17 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"006110","trigger_type":"Stage2-FalsePositive-AluminumFoilMaterialRebound-NoDemandMarginBridge","entry_date":"2024-02-20","duplicate_status":"new C15 symbol/trigger/date combination outside top-covered and recent R4 C16/C17 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"004430","trigger_type":"Stage2-FalsePositive-SpecialtyChemicalSpreadRebound-NoMarginCashBridge","entry_date":"2024-01-02","duplicate_status":"new C15 symbol/trigger/date combination outside top-covered and recent R4 C16/C17 symbols"}
```

## 4. Research question

C15 is not “소재 가격이 올랐다.”  
The useful material-spread signal must prove a bridge from commodity tape to company economics: inventory leverage, procurement cost lag, ASP pass-through, customer demand, utilization, spread expansion, contract discipline, and cash conversion. A copper or aluminum price headline alone is like a furnace without feedstock control; it glows, but it may not make margin.

Residual question:

```text
Can C15 distinguish:
1. copper/metal supercycle spread bridge with very high MFE and controlled MAE,
2. aluminum foil/material rebound where EV demand and spread/margin bridge fail,
3. specialty chemical spread rebound where low MFE and deep MAE show missing margin/cash conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C15_R4L88_024840_KBI_COPPER_METAL_SUPERCYCLE","symbol":"024840","company_name":"KBI메탈","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_METAL_SUPERCYCLE_SPREAD_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-CopperMetalSupercycleSpreadBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_low_MAE_data_quality_watch","current_profile_verdict":"current_profile_correct_if_inventory_ASP_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Copper/metal supercycle proxy produced extremely high MFE with controlled entry MAE. Data-quality repair is required because the profile contains historical corporate-action candidates and the selected 2024 path deserves share-count-change review."}
{"row_type":"case","case_id":"C15_R4L88_006110_SAMA_ALUMINUM_REBOUND_NO_DEMAND_MARGIN","symbol":"006110","company_name":"삼아알미늄","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINUM_FOIL_MATERIAL_REBOUND_WITHOUT_DEMAND_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-AluminumFoilMaterialRebound-NoDemandMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_aluminum_material_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Aluminum foil/material rebound had low MFE and deep MAE without EV demand, customer call-off, utilization and margin bridge."}
{"row_type":"case","case_id":"C15_R4L88_004430_SONGWON_SPECIALTY_CHEM_SPREAD","symbol":"004430","company_name":"송원산업","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"SPECIALTY_CHEMICAL_SPREAD_REBOUND_WITHOUT_MARGIN_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SpecialtyChemicalSpreadRebound-NoMarginCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_chemical_spread_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Specialty chemical/material spread rebound had near-zero MFE and large forward MAE without ASP pass-through, demand, margin and cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 024840 KBI메탈 — copper/metal supercycle spread bridge positive

Entry row: `2024-04-12 c=1641`.  
Observed path: entry-day low `1525`, high `2024-05-21 h=4745`, and later low `2024-12-09 l=1667`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L88_C15_024840_20240412_STAGE2_COPPER_METAL_SPREAD","case_id":"C15_R4L88_024840_KBI_COPPER_METAL_SUPERCYCLE","symbol":"024840","company_name":"KBI메탈","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_METAL_SUPERCYCLE_SPREAD_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-CopperMetalSupercycleSpreadBridge-Positive","trigger_date":"2024-04-12","entry_date":"2024-04-12","entry_price":1641.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_copper_metal_supercycle_spread_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; copper/metal spread, inventory and ASP pass-through bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["copper_price_supercycle_proxy","metal_inventory_leverage_proxy","ASP_pass_through_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_inventory_source_pending","customer_demand_bridge_pending","margin_spread_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_only_extension_watch","data_quality_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/024/024840/2024.csv","profile_path":"atlas/symbol_profiles/024/024840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":189.15,"MFE_90D_pct":189.15,"MFE_180D_pct":189.15,"MAE_30D_pct":-7.07,"MAE_90D_pct":-7.07,"MAE_180D_pct":-7.07,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":4745.0,"max_drawdown_low_date":"2024-04-12","max_drawdown_low":1525.0,"drawdown_after_peak_pct":-64.87,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_price_extension_and_data_quality_watch; Green requires exact inventory/margin/cash evidence","four_b_evidence_type":["price_only_extension_watch","data_quality_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_low_MAE_data_quality_watch","current_profile_verdict":"current_profile_correct_if_inventory_ASP_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["data_quality_repair_required_before_patch"],"corporate_action_window_status":"profile_has_historical_candidates; selected_2024_price_path_usable_with_share_count_change_watch","same_entry_group_id":"024840_2024-04-12_1641","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C15 can allow Stage2/Yellow when copper/metal strength is tied to inventory leverage, ASP pass-through, spread expansion and cash bridge. Green requires exact evidence and data-quality repair."}
```

### 6.2 006110 삼아알미늄 — aluminum foil/material rebound without demand-margin bridge

Entry row: `2024-02-20 c=108600`.  
Observed path: high `2024-02-21 h=116400`, low `2024-04-08 l=73800`, and later low `2024-11-15 l=35050`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L88_C15_006110_20240220_STAGE2_FALSE_POSITIVE_ALUMINUM_REBOUND","case_id":"C15_R4L88_006110_SAMA_ALUMINUM_REBOUND_NO_DEMAND_MARGIN","symbol":"006110","company_name":"삼아알미늄","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINUM_FOIL_MATERIAL_REBOUND_WITHOUT_DEMAND_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-AluminumFoilMaterialRebound-NoDemandMarginBridge","trigger_date":"2024-02-20","entry_date":"2024-02-20","entry_price":108600.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_aluminum_foil_material_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; aluminum foil/material rebound treated as insufficient without EV demand, customer call-off, utilization and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["aluminum_material_rebound","battery_foil_theme","relative_strength_rebound"],"stage3_evidence_fields":["EV_demand_bridge_missing","customer_calloff_missing","utilization_bridge_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","demand_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv","profile_path":"atlas/symbol_profiles/006/006110.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.18,"MFE_90D_pct":7.18,"MFE_180D_pct":7.18,"MAE_30D_pct":-25.41,"MAE_90D_pct":-32.04,"MAE_180D_pct":-67.73,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":116400.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":35050.0,"drawdown_after_peak_pct":-69.89,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"aluminum_material_rebound_without_demand_utilization_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","demand_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_aluminum_material_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"006110_2024-02-20_108600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C15 should not promote aluminum/battery-foil rebound without EV demand, customer call-off, utilization and margin bridge. Low MFE and severe MAE require 4B-watch routing."}
```

### 6.3 004430 송원산업 — specialty chemical/material spread rebound without margin-cash bridge

Entry row: `2024-01-02 c=16630`.  
Observed path: same-day high `16670`, lows through spring and late year around `2024-12-09 l=9930`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L88_C15_004430_20240102_STAGE2_FALSE_POSITIVE_CHEM_SPREAD","case_id":"C15_R4L88_004430_SONGWON_SPECIALTY_CHEM_SPREAD","symbol":"004430","company_name":"송원산업","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"SPECIALTY_CHEMICAL_SPREAD_REBOUND_WITHOUT_MARGIN_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-SpecialtyChemicalSpreadRebound-NoMarginCashBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":16630.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_specialty_chemical_material_spread_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; specialty chemical/material spread rebound treated as insufficient without ASP pass-through, demand recovery, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["specialty_chemical_spread_rebound","material_price_theme"],"stage3_evidence_fields":["ASP_pass_through_missing","demand_recovery_missing","margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","margin_cash_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004430/2024.csv","profile_path":"atlas/symbol_profiles/004/004430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.24,"MFE_90D_pct":0.24,"MFE_180D_pct":0.24,"MAE_30D_pct":-8.54,"MAE_90D_pct":-18.82,"MAE_180D_pct":-38.73,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-02","peak_price":16670.0,"max_drawdown_low_date":"2024-09-24","max_drawdown_low":10190.0,"drawdown_after_peak_pct":-38.87,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"specialty_chemical_spread_rebound_without_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","margin_cash_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_chemical_spread_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"004430_2024-01-02_16630","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C15 should not promote specialty chemical/material spread rebound without ASP pass-through, demand, margin and cash bridge. Near-zero MFE and large MAE route to Watch/4B-risk."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C15_R4L88_024840_KBI_COPPER_METAL_SUPERCYCLE","trigger_id":"R4L88_C15_024840_20240412_STAGE2_COPPER_METAL_SPREAD","symbol":"024840","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C15 requires inventory/ASP/spread/margin bridge rather than material price theme alone","raw_component_scores_before":{"commodity_spread_score":14,"inventory_leverage_score":12,"ASP_pass_through_score":11,"customer_demand_score":10,"margin_bridge_score":10,"cash_conversion_score":6,"relative_strength_score":15,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-3,"information_confidence":4},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"commodity_spread_score":18,"inventory_leverage_score":15,"ASP_pass_through_score":14,"customer_demand_score":12,"margin_bridge_score":12,"cash_conversion_score":8,"relative_strength_score":16,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Copper/metal spread bridge plus very high MFE support Yellow-watch; Green requires exact inventory, margin, cash and data-quality repair."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C15_R4L88_006110_SAMA_ALUMINUM_REBOUND_NO_DEMAND_MARGIN","trigger_id":"R4L88_C15_006110_20240220_STAGE2_FALSE_POSITIVE_ALUMINUM_REBOUND","symbol":"006110","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","profile_scope":"current_default_proxy","profile_hypothesis":"aluminum foil/material rebound without demand and margin bridge should be blocked","raw_component_scores_before":{"commodity_spread_score":6,"inventory_leverage_score":1,"ASP_pass_through_score":1,"customer_demand_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":8,"valuation_repricing_score":4,"execution_risk_score":-16,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"commodity_spread_score":1,"inventory_leverage_score":0,"ASP_pass_through_score":0,"customer_demand_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and severe MAE convert aluminum/material rebound into missing demand/margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C15_R4L88_004430_SONGWON_SPECIALTY_CHEM_SPREAD","trigger_id":"R4L88_C15_004430_20240102_STAGE2_FALSE_POSITIVE_CHEM_SPREAD","symbol":"004430","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","profile_scope":"current_default_proxy","profile_hypothesis":"specialty chemical spread rebound without margin/cash bridge should remain Watch/blocked","raw_component_scores_before":{"commodity_spread_score":3,"inventory_leverage_score":0,"ASP_pass_through_score":0,"customer_demand_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-14,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"commodity_spread_score":0,"inventory_leverage_score":0,"ASP_pass_through_score":0,"customer_demand_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-22,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE require ASP pass-through, demand and margin/cash evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R4L88_C15_P0_CURRENT","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C15 needs explicit inventory/ASP/pass-through/margin/cash bridge and material-theme 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":65.52,"avg_MAE90_pct":-19.31,"avg_MFE180_pct":65.52,"avg_MAE180_pct":-37.84,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C15_spread_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R4L88_C15_P1_SECTOR_SPECIFIC","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","profile_id":"P1_L4_material_spread_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L4 material-spread signals need inventory leverage, ASP pass-through, customer demand, margin spread or cash conversion before Stage2-Actionable","changed_axes":["spread_margin_bridge_required","ASP_pass_through_required","material_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_inventory_ASP_demand_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":65.52,"avg_MAE90_pct":-19.31,"avg_MFE180_pct":65.52,"avg_MAE180_pct":-37.84,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R4L88_C15_P2_CANONICAL","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","profile_id":"P2_C15_inventory_ASP_margin_cash_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C15 should reward material spread conversion, not commodity/chemical rebound labels","changed_axes":["C15_inventory_ASP_margin_bridge_required","C15_material_theme_local_4B_guard","C15_data_quality_watch_for_corporate_action_candidates"],"changed_thresholds":{"stage2_yellow_gate":"spread_or_inventory_plus_margin_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":65.52,"avg_MAE90_pct":-19.31,"avg_MFE180_pct":65.52,"avg_MAE180_pct":-37.84,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R4L88_C15_P3_COUNTEREXAMPLE_GUARD","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","profile_id":"P3_C15_low_MFE_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-20 while margin/cash bridge is missing, block Yellow/Green; if MFE90<1 and MAE180<=-35, route to 4B-watch","changed_axes":["C15_low_MFE_guardrail","C15_high_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_20_or_MFE90_lt_1_and_MAE180_le_minus_35"},"eligible_trigger_count":3,"avg_MFE90_pct":65.52,"avg_MAE90_pct":-19.31,"avg_MFE180_pct":65.52,"avg_MAE180_pct":-37.84,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_COPPER_SPREAD_BRIDGE_VS_ALUMINUM_CHEMICAL_REBOUND","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":65.52,"avg_MAE90_pct":-19.31,"avg_MFE180_pct":65.52,"avg_MAE180_pct":-37.84,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE180_le_minus_35":0.67,"interpretation":"C15 needs bridge discipline. KBI메탈 shows copper/metal spread can produce a very high MFE path, while 삼아알미늄 and 송원산업 show material/chemical rebounds should not be promoted without demand, ASP pass-through, margin and cash bridge."}
{"row_type":"stage_transition_summary","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"024840","trigger_type":"Stage2-Actionable-CopperMetalSupercycleSpreadBridge-Positive","entry_date":"2024-04-12","stage2_to_90D_outcome":"good_stage2_very_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_copper_spread_rerating_with_data_quality_watch","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when copper/metal spread is tied to inventory, ASP and margin bridge; Green requires exact evidence and data-quality repair."}
{"row_type":"stage_transition_summary","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"006110","trigger_type":"Stage2-FalsePositive-AluminumFoilMaterialRebound-NoDemandMarginBridge","entry_date":"2024-02-20","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_aluminum_material_rebound_severe_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Aluminum/material rebound without EV demand, call-off, utilization and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"004430","trigger_type":"Stage2-FalsePositive-SpecialtyChemicalSpreadRebound-NoMarginCashBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"weak_stage2_near_zero_MFE","stage2_to_180D_outcome":"failed_specialty_chemical_spread_rebound_large_MAE","MFE90_ge_20":false,"MAE180_le_minus_35":true,"transition_note":"Specialty chemical/material spread rebound without ASP pass-through and margin/cash bridge should stay Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","residual_type":"material_spread_theme_overcredit_without_inventory_ASP_margin_cash_bridge","contribution":"Adds two C15 local 4B/deep-MAE counterexamples against one copper/metal spread positive, avoiding C15 top-covered and previous R4 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_METAL_SUPERCYCLE_SPREAD_BRIDGE_VS_ALUMINUM_CHEMICAL_REBOUND_NO_MARGIN_BRIDGE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C15 now has non-top-symbol copper/metal positive and aluminum/chemical material rebound counterexamples; next R4 loops should exact-URL repair inventory leverage, ASP pass-through, customer demand, spread expansion, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","axis":"C15_inventory_ASP_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"024840 worked when copper/metal spread proxy was present; 006110 and 004430 failed when material/chemical rebound lacked demand, ASP, margin and cash bridge."}
{"row_type":"shadow_weight","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","axis":"C15_material_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Aluminum and specialty chemical rebound rows showed low or near-zero MFE and deep MAE without non-price spread bridge."}
{"row_type":"shadow_weight","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","axis":"C15_data_quality_watch_for_corporate_action_candidates","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"KBI메탈 is useful price-path evidence but should receive exact data-quality repair before production consideration because the profile has many corporate-action candidates and selected 2024 rows show share-count drift."}
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
  - material_spread_theme_overcredit
  - demand_bridge_missing
  - ASP_pass_through_bridge_missing
  - margin_cash_conversion_bridge_missing
new_axis_proposed:
  - C15_inventory_ASP_margin_cash_bridge_required_shadow_only
  - C15_material_theme_local_4B_watch_guard_shadow_only
  - C15_data_quality_watch_for_corporate_action_candidates_shadow_only
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

All selected triggers use actual Stock-Web tradable raw OHLC rows.  
However, the non-price evidence layer remains source-name/proxy level, and the KBI메탈 positive row requires data-quality repair before any production patch because the profile has multiple historical corporate-action candidates and the 2024 path deserves share-count-change review.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
data_quality_repair_required = true for 024840 before any patch
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
6. Before considering any patch from 024840, repair data quality:
   - inspect raw share-count changes
   - confirm no split/rights issue contaminates MFE/MAE
   - verify exact non-price inventory/ASP/margin evidence
7. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C15-scoped safe patch candidates:
   - C15_inventory_ASP_margin_cash_bridge_required
   - C15_material_theme_local_4B_watch_guard
   - C15_data_quality_watch_for_corporate_action_candidates
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R4
completed_loop = 88
next_round = R5
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE.
```
