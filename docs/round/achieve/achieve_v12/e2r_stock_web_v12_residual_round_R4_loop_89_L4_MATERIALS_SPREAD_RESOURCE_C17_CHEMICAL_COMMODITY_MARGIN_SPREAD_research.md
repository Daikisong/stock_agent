# E2R Stock-Web v12 Residual Research — R4 Loop 89 / L4 / C17

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R4
loop: 89
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHLOR_ALKALI_SPECIALTY_CHEMICAL_SPREAD_BRIDGE_VS_PETROCHEM_BATTERY_CHEMICAL_REBOUND_DECAY
sector: materials / chemical / commodity spread / chlor-alkali / petrochemical / battery chemical
output_file: e2r_stock_web_v12_residual_round_R4_loop_89_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R3 loop 89`.

```text
scheduled_round = R4
scheduled_loop = 89
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```

R4 is restricted to materials / spread / resource.  
C17 is selected because the recent R4 loop sequence already covered:

```text
R4 loop86: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
R4 loop87: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
R4 loop88: C15_MATERIAL_SPREAD_SUPERCYCLE
```

No-Repeat Index snapshot:

```text
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
rows = 21
symbols = 15
good/bad Stage2 = 8/3
4B/4C = 4/0
top-covered = 004000, 006650, 011780, 014680, 298020, 001390
```

This loop avoids the C17 top-covered symbols and also avoids the recent R4 loop symbols:

```text
R4 loop86 C17: 120110, 010060, 009830
R4 loop87 C16: 006260, 073570, 131400
R4 loop88 C15: 024840, 006110, 004430
```

Selected symbols:

```text
001340, 298000, 161000
```

This loop tests a different C17 pocket:

```text
chlor-alkali / high-purity chemical spread bridge
vs
petrochemical rebound without spread or leverage bridge
vs
battery-chemical / plasticizer rebound without demand, utilization or cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"001340","company_name":"백광산업","current_or_latest_name":"PKC","profile_path":"atlas/symbol_profiles/001/001340.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7511,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2008-04-01","2012-05-10","2015-06-17"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window. 2024 data starts after non-tradable rows; selected entry is after active tradable sequence resumes.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_2024_forward_window_usable_with_resume_watch"}
{"row_type":"price_source_validation","symbol":"298000","company_name":"효성화학","profile_path":"atlas/symbol_profiles/298/298000.json","first_date":"2018-07-13","last_date":"2025-02-28","trading_day_count":1629,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"2024 forward window is tradable; later listing status outside 2024 should remain data-quality watch before production patch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"161000","company_name":"애경케미칼","profile_path":"atlas/symbol_profiles/161/161000.json","first_date":"2012-09-17","last_date":"2026-02-20","trading_day_count":3281,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2016-09-06","2021-11-16"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"001340","trigger_type":"Stage2-Actionable-ChlorAlkaliHighPurityChemicalSpreadBridge-Positive","entry_date":"2024-05-22","duplicate_status":"new C17 symbol/trigger/date combination outside top-covered and recent R4 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"298000","trigger_type":"Stage2-FalsePositive-PetrochemicalReboundNoSpreadLeverageBridge","entry_date":"2024-01-02","duplicate_status":"new C17 symbol/trigger/date combination outside top-covered and recent R4 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"161000","trigger_type":"Stage2-FalsePositive-BatteryChemicalPlasticizerReboundNoDemandMarginBridge","entry_date":"2024-01-02","duplicate_status":"new C17 symbol/trigger/date combination outside top-covered and recent R4 loop symbols"}
```

## 4. Research question

C17 is not “화학주가 올랐다.”  
The useful chemical spread signal must prove a conversion bridge: feedstock cost lag, ASP pass-through, spread widening, product mix, utilization, customer demand, inventory leverage, margin expansion and cash conversion. A chemical price headline without this bridge is only steam escaping the pipe; it proves pressure, not profitable flow.

Residual question:

```text
Can C17 distinguish:
1. chlor-alkali / high-purity chemical spread bridge with very high MFE,
2. petrochemical rebound where structural spread and operating leverage are missing,
3. battery chemical / plasticizer rebound where demand, utilization and margin/cash bridge are absent?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C17_R4L89_001340_BAEKWANG_CHLOR_ALKALI_SPREAD","symbol":"001340","company_name":"백광산업","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHLOR_ALKALI_HIGH_PURITY_CHEMICAL_SPREAD_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-ChlorAlkaliHighPurityChemicalSpreadBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_tolerable_MAE_resume_watch","current_profile_verdict":"current_profile_correct_if_spread_ASP_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Chlor-alkali/high-purity chemical spread proxy produced very high MFE. Selected after active 2024 tradable sequence resumes; Green still requires exact ASP, spread, margin and cash evidence."}
{"row_type":"case","case_id":"C17_R4L89_298000_HYOSUNG_CHEM_PETROCHEM_NO_SPREAD","symbol":"298000","company_name":"효성화학","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PETROCHEMICAL_REBOUND_WITHOUT_SPREAD_LEVERAGE_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-PetrochemicalReboundNoSpreadLeverageBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_petrochemical_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Petrochemical rebound had near-zero MFE from the selected entry and extreme MAE as spread, utilization, leverage and cash bridge failed."}
{"row_type":"case","case_id":"C17_R4L89_161000_AEKYUNG_BATTERY_CHEM_NO_DEMAND_MARGIN","symbol":"161000","company_name":"애경케미칼","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"BATTERY_CHEMICAL_PLASTICIZER_REBOUND_WITHOUT_DEMAND_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-BatteryChemicalPlasticizerReboundNoDemandMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_battery_chemical_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Battery-chemical/plasticizer rebound had small MFE and severe 180D MAE without demand recovery, utilization, spread/margin and cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 001340 백광산업 — chlor-alkali / high-purity chemical spread bridge positive

Entry row: `2024-05-22 c=7970`.  
Observed path: entry-day low `7170`, peak `2024-06-12 h=18440`, and late-year low `2024-12-27 l=6550`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L89_C17_001340_20240522_STAGE2_CHLOR_ALKALI_SPREAD","case_id":"C17_R4L89_001340_BAEKWANG_CHLOR_ALKALI_SPREAD","symbol":"001340","company_name":"백광산업","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHLOR_ALKALI_HIGH_PURITY_CHEMICAL_SPREAD_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-ChlorAlkaliHighPurityChemicalSpreadBridge-Positive","trigger_date":"2024-05-22","entry_date":"2024-05-22","entry_price":7970.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_chlor_alkali_high_purity_chemical_spread_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; chlor-alkali/high-purity chemical spread, ASP pass-through and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["chemical_spread_proxy","ASP_pass_through_proxy","high_purity_product_mix_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_spread_source_pending","customer_demand_pending","margin_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","data_quality_resume_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001340/2024.csv","profile_path":"atlas/symbol_profiles/001/001340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":131.37,"MFE_90D_pct":131.37,"MFE_180D_pct":131.37,"MAE_30D_pct":-10.04,"MAE_90D_pct":-10.04,"MAE_180D_pct":-17.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-12","peak_price":18440.0,"max_drawdown_low_date":"2024-12-27","max_drawdown_low":6550.0,"drawdown_after_peak_pct":-64.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_price_extension_and_resume_data_quality_watch; Green requires exact spread/margin/cash evidence","four_b_evidence_type":["price_extension_watch","data_quality_resume_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_tolerable_MAE_resume_watch","current_profile_verdict":"current_profile_correct_if_spread_ASP_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["resume_watch_due_to_2024_tradable_sequence_start"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_entry_after_active_2024_tradable_sequence_resumes","same_entry_group_id":"001340_2024-05-22_7970","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C17 can allow Stage2/Yellow when chemical strength is tied to spread, ASP pass-through, product mix, margin and cash bridge. Green still requires exact evidence and data-quality repair."}
```

### 6.2 298000 효성화학 — petrochemical rebound without spread/leverage bridge

Entry row: `2024-01-02 c=86300`.  
Observed path: same-day high `86500`, then lows through spring and late-year decline to `2024-11-27 l=28150`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L89_C17_298000_20240102_STAGE2_FALSE_POSITIVE_PETROCHEM_REBOUND","case_id":"C17_R4L89_298000_HYOSUNG_CHEM_PETROCHEM_NO_SPREAD","symbol":"298000","company_name":"효성화학","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PETROCHEMICAL_REBOUND_WITHOUT_SPREAD_LEVERAGE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-PetrochemicalReboundNoSpreadLeverageBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":86300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_petrochemical_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; petrochemical rebound treated as insufficient without feedstock spread, utilization recovery, operating leverage and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["petrochemical_rebound_theme","relative_strength_rebound"],"stage3_evidence_fields":["feedstock_spread_bridge_missing","utilization_recovery_missing","operating_leverage_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","spread_leverage_bridge_missing_watch","extreme_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298000/2024.csv","profile_path":"atlas/symbol_profiles/298/298000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.23,"MFE_90D_pct":0.23,"MFE_180D_pct":0.23,"MAE_30D_pct":-24.57,"MAE_90D_pct":-31.40,"MAE_180D_pct":-54.23,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-02","peak_price":86500.0,"max_drawdown_low_date":"2024-11-27","max_drawdown_low":28150.0,"drawdown_after_peak_pct":-67.46,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"petrochemical_rebound_without_spread_leverage_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","spread_leverage_bridge_missing_watch","extreme_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_petrochemical_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window; later_listing_status_watch_outside_window","same_entry_group_id":"298000_2024-01-02_86300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C17 should not promote petrochemical rebound labels without spread expansion, utilization, operating leverage and cash conversion. Near-zero MFE and extreme MAE require 4B-watch."}
```

### 6.3 161000 애경케미칼 — battery chemical/plasticizer rebound without demand-margin bridge

Entry row: `2024-01-02 c=16740`.  
Observed path: local high `2024-01-03 h=17110`, then low `2024-12-09 l=6510`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L89_C17_161000_20240102_STAGE2_FALSE_POSITIVE_BATTERY_CHEM_REBOUND","case_id":"C17_R4L89_161000_AEKYUNG_BATTERY_CHEM_NO_DEMAND_MARGIN","symbol":"161000","company_name":"애경케미칼","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"BATTERY_CHEMICAL_PLASTICIZER_REBOUND_WITHOUT_DEMAND_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-BatteryChemicalPlasticizerReboundNoDemandMarginBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":16740.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_battery_chemical_plasticizer_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; battery chemical/plasticizer rebound treated as insufficient without customer demand, utilization, spread/margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["battery_chemical_rebound","plasticizer_material_theme","relative_strength_rebound"],"stage3_evidence_fields":["customer_demand_bridge_missing","utilization_recovery_missing","spread_margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","demand_margin_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/161/161000/2024.csv","profile_path":"atlas/symbol_profiles/161/161000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.21,"MFE_90D_pct":2.21,"MFE_180D_pct":2.21,"MAE_30D_pct":-28.26,"MAE_90D_pct":-28.26,"MAE_180D_pct":-61.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-03","peak_price":17110.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":6510.0,"drawdown_after_peak_pct":-61.95,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"battery_chemical_rebound_without_demand_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","demand_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_battery_chemical_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"161000_2024-01-02_16740","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C17 should not equate battery-chemical or plasticizer rebound with margin-spread rerating. Demand, utilization, spread/margin and cash bridge are required before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C17_R4L89_001340_BAEKWANG_CHLOR_ALKALI_SPREAD","trigger_id":"R4L89_C17_001340_20240522_STAGE2_CHLOR_ALKALI_SPREAD","symbol":"001340","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C17 requires spread, ASP pass-through, product mix, margin and cash bridge rather than chemical theme alone","raw_component_scores_before":{"chemical_spread_score":15,"ASP_pass_through_score":13,"product_mix_score":12,"customer_demand_score":10,"utilization_score":9,"margin_bridge_score":11,"cash_conversion_score":7,"relative_strength_score":15,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"chemical_spread_score":18,"ASP_pass_through_score":16,"product_mix_score":15,"customer_demand_score":12,"utilization_score":11,"margin_bridge_score":14,"cash_conversion_score":9,"relative_strength_score":16,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Spread/ASP/margin bridge plus very high MFE supports Yellow/Green-candidate watch; resume/data-quality watch and proxy-only evidence block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C17_R4L89_298000_HYOSUNG_CHEM_PETROCHEM_NO_SPREAD","trigger_id":"R4L89_C17_298000_20240102_STAGE2_FALSE_POSITIVE_PETROCHEM_REBOUND","symbol":"298000","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_scope":"current_default_proxy","profile_hypothesis":"petrochemical rebound without spread and leverage bridge should be blocked","raw_component_scores_before":{"chemical_spread_score":1,"ASP_pass_through_score":0,"product_mix_score":0,"customer_demand_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":2,"execution_risk_score":-18,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"chemical_spread_score":0,"ASP_pass_through_score":0,"product_mix_score":0,"customer_demand_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-26,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and extreme MAE convert petrochemical rebound into missing spread/leverage bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C17_R4L89_161000_AEKYUNG_BATTERY_CHEM_NO_DEMAND_MARGIN","trigger_id":"R4L89_C17_161000_20240102_STAGE2_FALSE_POSITIVE_BATTERY_CHEM_REBOUND","symbol":"161000","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_scope":"current_default_proxy","profile_hypothesis":"battery-chemical/material rebound without demand and margin bridge should remain Watch/blocked","raw_component_scores_before":{"chemical_spread_score":2,"ASP_pass_through_score":0,"product_mix_score":1,"customer_demand_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":5,"valuation_repricing_score":2,"execution_risk_score":-16,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"chemical_spread_score":0,"ASP_pass_through_score":0,"product_mix_score":0,"customer_demand_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE require demand, utilization, spread/margin and cash evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R4L89_C17_P0_CURRENT","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C17 needs explicit spread/ASP/product-mix/utilization/margin/cash bridge and commodity rebound 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":44.6,"avg_MAE90_pct":-23.23,"avg_MFE180_pct":44.6,"avg_MAE180_pct":-48.98,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C17_spread_ASP_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R4L89_C17_P1_SECTOR_SPECIFIC","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_id":"P1_L4_chemical_spread_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L4 chemical-spread signals need feedstock spread, ASP pass-through, product mix, customer demand, utilization, margin or cash conversion before Stage2-Actionable","changed_axes":["spread_ASP_required","utilization_margin_required","commodity_rebound_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_spread_ASP_mix_demand_utilization_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":44.6,"avg_MAE90_pct":-23.23,"avg_MFE180_pct":44.6,"avg_MAE180_pct":-48.98,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R4L89_C17_P2_CANONICAL","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_id":"P2_C17_spread_ASP_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C17 should reward spread-to-margin mechanics, not petrochemical or battery-chemical rebound labels","changed_axes":["C17_spread_ASP_margin_cash_bridge_required","C17_commodity_rebound_local_4B_guard","C17_resume_data_quality_watch"],"changed_thresholds":{"stage2_yellow_gate":"spread_or_ASP_pass_through_plus_margin_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":44.6,"avg_MAE90_pct":-23.23,"avg_MFE180_pct":44.6,"avg_MAE180_pct":-48.98,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R4L89_C17_P3_COUNTEREXAMPLE_GUARD","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_id":"P3_C17_low_MFE_extreme_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<5 and MAE90<=-20 while spread/margin bridge is missing, block Yellow/Green and route to 4B-watch","changed_axes":["C17_low_MFE_guardrail","C17_extreme_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_5_and_MAE90_le_minus_20_with_spread_bridge_missing"},"eligible_trigger_count":3,"avg_MFE90_pct":44.6,"avg_MAE90_pct":-23.23,"avg_MFE180_pct":44.6,"avg_MAE180_pct":-48.98,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_CHLOR_ALKALI_POSITIVE_VS_PETROCHEM_BATTERY_CHEM_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":44.6,"avg_MAE90_pct":-23.23,"avg_MFE180_pct":44.6,"avg_MAE180_pct":-48.98,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_5":0.67,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C17 needs bridge discipline. 백광산업 shows chlor-alkali/high-purity chemical spread bridge can produce very high MFE, while 효성화학 and 애경케미칼 show petrochemical/battery-chemical rebounds should not be promoted without spread, demand, utilization, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"001340","trigger_type":"Stage2-Actionable-ChlorAlkaliHighPurityChemicalSpreadBridge-Positive","entry_date":"2024-05-22","stage2_to_90D_outcome":"good_stage2_very_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"watch_positive_with_resume_data_quality_watch","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when chemical spread, ASP pass-through, product mix and margin bridge exists; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"298000","trigger_type":"Stage2-FalsePositive-PetrochemicalReboundNoSpreadLeverageBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_deep_MAE","stage2_to_180D_outcome":"failed_petrochemical_rebound_extreme_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Petrochemical rebound without spread/leverage/cash bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"161000","trigger_type":"Stage2-FalsePositive-BatteryChemicalPlasticizerReboundNoDemandMarginBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_battery_chemical_rebound_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Battery-chemical/plasticizer rebound without demand and margin bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","residual_type":"chemical_commodity_rebound_overcredit_without_spread_ASP_margin_cash_bridge","contribution":"Adds two C17 local 4B/deep-MAE counterexamples against one chlor-alkali spread positive, avoiding C17 top-covered and previous R4 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHLOR_ALKALI_SPECIALTY_CHEMICAL_SPREAD_BRIDGE_VS_PETROCHEM_BATTERY_CHEMICAL_REBOUND_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C17 now has non-top-symbol chlor-alkali/high-purity chemical positive and petrochemical/battery-chemical weak-bridge counterexamples; next R4 loops should exact-URL repair feedstock spread, ASP pass-through, product mix, utilization, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","axis":"C17_spread_ASP_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"001340 worked when spread/ASP/product-mix proxy was present; 298000 and 161000 failed when only petrochemical or battery-chemical rebound labels existed."}
{"row_type":"shadow_weight","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","axis":"C17_commodity_rebound_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Petrochemical and battery-chemical rebound rows showed low/near-zero MFE and deep MAE without non-price spread bridge."}
{"row_type":"shadow_weight","round":"R4","loop":"89","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","axis":"C17_resume_data_quality_watch","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"001340 is useful price-path evidence but should keep resume/data-quality watch before any production patch because 2024 tradable rows start after non-tradable rows."}
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
  - chemical_commodity_rebound_overcredit
  - petrochemical_rebound_overcredit
  - feedstock_spread_bridge_missing
  - ASP_margin_cash_bridge_missing
new_axis_proposed:
  - C17_spread_ASP_margin_cash_bridge_required_shadow_only
  - C17_commodity_rebound_local_4B_watch_guard_shadow_only
  - C17_resume_data_quality_watch_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C17
  - full_4b_requires_non_price_evidence within C17
  - hard_4c_thesis_break_routes_to_4c within C17
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
`001340` is selected after the active 2024 tradable sequence resumes; it remains usable for price-path calibration but should keep data-quality/resume watch before any production patch.  
The non-price evidence layer remains source-name/proxy level.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
data_quality_watch = true for 001340 active-tradable-sequence resume
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
3. Confirm R4 / L4 / C17 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C17 top-covered symbols
   - previous R4 loop86 C17 symbols
   - previous R4 loop87 C16 symbols
   - previous R4 loop88 C15 symbols
6. Keep 001340 in data-quality/resume watch before patch consideration.
7. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C17-scoped safe patch candidates:
   - C17_spread_ASP_margin_cash_bridge_required
   - C17_commodity_rebound_local_4B_watch_guard
   - C17_resume_data_quality_watch
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R4
completed_loop = 89
next_round = R5
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.
```
