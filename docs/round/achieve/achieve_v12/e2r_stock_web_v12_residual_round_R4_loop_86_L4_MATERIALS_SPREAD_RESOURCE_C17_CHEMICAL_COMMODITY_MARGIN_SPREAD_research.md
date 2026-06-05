# E2R Stock-Web v12 Residual Research — R4 Loop 86 / L4 / C17

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R4
loop: 86
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHEMICAL_MARGIN_SPREAD_RECOVERY_BRIDGE_VS_COMMODITY_BETA_AND_SOLAR_CHEMICAL_THEME_DECAY
sector: materials / chemical / commodity margin spread / solar-polysilicon risk
output_file: e2r_stock_web_v12_residual_round_R4_loop_86_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R3 loop 86`.

```text
scheduled_round = R4
scheduled_loop = 86
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```

R4 is restricted to L4 materials / spread / resource.  
C17 is selected because recent R4 work already used C15 and C16, while C17 still has a useful false-positive gap:

```text
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
rows = 21
symbols = 15
good/bad Stage2 = 8/3
4B/4C = 4/0
top-covered = 004000, 006650, 011780, 014680, 298020, 001390
```

This loop avoids that top-covered list and uses a different symbol set:

```text
120110, 010060, 009830
```

This is not a live stock recommendation, not a production scoring change, and not a code patch.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"120110","company_name":"코오롱인더","profile_path":"atlas/symbol_profiles/120/120110.json","first_date":"2010-02-01","last_date":"2026-02-20","trading_day_count":3952,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2010-12-27"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"010060","company_name":"OCI홀딩스","profile_path":"atlas/symbol_profiles/010/010060.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7724,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1999-04-16","2001-05-18","2023-05-30","2023-10-13"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"009830","company_name":"한화솔루션","profile_path":"atlas/symbol_profiles/009/009830.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7741,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["1999-04-20","2008-07-04"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"120110","trigger_type":"Stage2-Actionable-ChemicalIndustrialMarginSpreadBridge-Positive","entry_date":"2024-04-23","duplicate_status":"new C17 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"010060","trigger_type":"Stage2-FalsePositive-PolysiliconChemicalSpreadRebound-NoMarginBridge","entry_date":"2024-01-10","duplicate_status":"new C17 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"009830","trigger_type":"Stage2-FalsePositive-SolarChemicalCommodityBeta-NoSpreadRecoveryBridge","entry_date":"2024-01-10","duplicate_status":"new C17 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C17 is not “chemical stock bounced.”  
Commodity chemicals are spread machines. The signal needs feedstock/product spread recovery, inventory reset, utilization, demand visibility, pricing power, and margin/cash conversion. Without that bridge, price is just a flare over a still-compressed spread.

Residual question:

```text
Can C17 distinguish:
1. industrial/chemical margin-spread recovery with usable MFE,
2. polysilicon or chemical spread rebound that lacks durable margin bridge,
3. solar-chemical commodity beta where price-only rebound decays into deep MAE?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C17_R4L86_120110_KOLONIND_CHEM_MARGIN_SPREAD_BRIDGE","symbol":"120110","company_name":"코오롱인더","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_INDUSTRIAL_MARGIN_SPREAD_RECOVERY_BRIDGE","case_type":"watch_positive_control","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-ChemicalIndustrialMarginSpreadBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_moderate_MFE_low_90D_MAE_later_drawdown","current_profile_verdict":"current_profile_correct_if_margin_spread_bridge_required","price_source":"Songdaiki/stock-web","notes":"Spring 2024 price path supports a Watch/Yellow-control row when spread/margin recovery proxy exists. Later drawdown keeps Green strict."}
{"row_type":"case","case_id":"C17_R4L86_010060_OCI_POLYSILICON_REBOUND_NO_MARGIN_BRIDGE","symbol":"010060","company_name":"OCI홀딩스","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"POLYSILICON_CHEMICAL_REBOUND_WITHOUT_DURABLE_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-PolysiliconChemicalSpreadRebound-NoMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_commodity_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"January rebound was not backed by durable spread/margin recovery; low MFE and high MAE support 4B-watch routing."}
{"row_type":"case","case_id":"C17_R4L86_009830_HANWHA_SOLAR_CHEMICAL_BETA","symbol":"009830","company_name":"한화솔루션","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SOLAR_CHEMICAL_COMMODITY_BETA_WITHOUT_SPREAD_RECOVERY","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SolarChemicalCommodityBeta-NoSpreadRecoveryBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_solar_chemical_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"Solar/chemical beta had a shallow rebound and then severe forward MAE without spread, utilization and earnings bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 120110 코오롱인더 — chemical/industrial margin-spread bridge positive

Entry row: `2024-04-23 c=36600`.  
Observed path: early low `2024-04-23 l=35500`, high `2024-05-22 h=44150`, and later low `2024-12-09 l=25700`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L86_C17_120110_20240423_STAGE2_CHEM_MARGIN_SPREAD_BRIDGE","case_id":"C17_R4L86_120110_KOLONIND_CHEM_MARGIN_SPREAD_BRIDGE","symbol":"120110","company_name":"코오롱인더","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_INDUSTRIAL_MARGIN_SPREAD_RECOVERY_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-ChemicalIndustrialMarginSpreadBridge-Positive","trigger_date":"2024-04-23","entry_date":"2024-04-23","entry_price":36600.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_industrial_chemical_margin_spread_recovery_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; chemical spread and margin recovery bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["spread_recovery_proxy","inventory_reset_proxy","margin_bridge_proxy","relative_strength_turn"],"stage3_evidence_fields":["utilization_bridge_pending","cash_conversion_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/120/120110/2024.csv","profile_path":"atlas/symbol_profiles/120/120110.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.63,"MFE_90D_pct":20.63,"MFE_180D_pct":20.63,"MAE_30D_pct":-3.01,"MAE_90D_pct":-3.01,"MAE_180D_pct":-29.78,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-22","peak_price":44150.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":25700.0,"drawdown_after_peak_pct":-41.79,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_moderate_MFE_low_90D_MAE_later_drawdown","current_profile_verdict":"current_profile_correct_if_margin_spread_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"120110_2024-04-23_36600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C17 can allow Watch/Yellow when spread recovery and margin bridge exist. Later drawdown requires exact utilization, margin and cash-conversion evidence before Green."}
```

### 6.2 010060 OCI홀딩스 — polysilicon/chemical rebound without durable margin bridge

Entry row: `2024-01-10 c=113700`.  
Observed path: same-week high `2024-01-11 h=116400`, then lows `2024-01-17 l=91000`, `2024-04-11 l=88300`, and `2024-07-19 l=78700`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L86_C17_010060_20240110_STAGE2_FALSE_POSITIVE_POLYSILICON_REBOUND","case_id":"C17_R4L86_010060_OCI_POLYSILICON_REBOUND_NO_MARGIN_BRIDGE","symbol":"010060","company_name":"OCI홀딩스","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"POLYSILICON_CHEMICAL_REBOUND_WITHOUT_DURABLE_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-PolysiliconChemicalSpreadRebound-NoMarginBridge","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":113700.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_polysilicon_chemical_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; polysilicon/chemical rebound treated as insufficient without durable spread, utilization and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["commodity_rebound_theme","price_spread_keyword_proxy"],"stage3_evidence_fields":["durable_margin_bridge_missing","utilization_recovery_missing","inventory_reset_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","spread_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010060/2024.csv","profile_path":"atlas/symbol_profiles/010/010060.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.37,"MFE_90D_pct":2.37,"MFE_180D_pct":2.37,"MAE_30D_pct":-19.96,"MAE_90D_pct":-22.34,"MAE_180D_pct":-30.78,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-11","peak_price":116400.0,"max_drawdown_low_date":"2024-07-19","max_drawdown_low":78700.0,"drawdown_after_peak_pct":-32.39,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"commodity_rebound_without_durable_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","spread_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_commodity_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"010060_2024-01-10_113700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C17 should block commodity rebound labels when durable margin spread and utilization bridge are missing. Low MFE and high MAE argue for Watch/4B-risk."}
```

### 6.3 009830 한화솔루션 — solar/chemical commodity beta without spread recovery

Entry row: `2024-01-10 c=38550`.  
Observed path: same-day high `39300`, then lows `2024-02-23 l=26500`, `2024-10-23 l=20000`, and `2024-12-09 l=14860`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L86_C17_009830_20240110_STAGE2_FALSE_POSITIVE_SOLAR_CHEMICAL_BETA","case_id":"C17_R4L86_009830_HANWHA_SOLAR_CHEMICAL_BETA","symbol":"009830","company_name":"한화솔루션","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SOLAR_CHEMICAL_COMMODITY_BETA_WITHOUT_SPREAD_RECOVERY","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-SolarChemicalCommodityBeta-NoSpreadRecoveryBridge","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":38550.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_solar_chemical_commodity_beta_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; solar/chemical beta treated as insufficient without spread recovery, utilization, inventory reset and earnings bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["solar_chemical_beta","commodity_rebound_keyword"],"stage3_evidence_fields":["spread_recovery_missing","utilization_bridge_missing","earnings_revision_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","spread_and_inventory_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009830/2024.csv","profile_path":"atlas/symbol_profiles/009/009830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.95,"MFE_90D_pct":1.95,"MFE_180D_pct":1.95,"MAE_30D_pct":-31.26,"MAE_90D_pct":-31.26,"MAE_180D_pct":-61.45,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-10","peak_price":39300.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":14860.0,"drawdown_after_peak_pct":-62.19,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"solar_chemical_beta_without_spread_recovery_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","spread_and_inventory_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_solar_chemical_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"009830_2024-01-10_38550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C17 should not promote solar/chemical commodity beta without spread and margin recovery. Near-zero MFE and extreme MAE require local 4B guard."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C17_R4L86_120110_KOLONIND_CHEM_MARGIN_SPREAD_BRIDGE","trigger_id":"R4L86_C17_120110_20240423_STAGE2_CHEM_MARGIN_SPREAD_BRIDGE","symbol":"120110","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C17 requires spread and margin bridge rather than chemical beta alone","raw_component_scores_before":{"spread_recovery_score":13,"margin_bridge_score":12,"inventory_reset_score":10,"utilization_bridge_score":8,"pricing_power_score":8,"relative_strength_score":10,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"spread_recovery_score":16,"margin_bridge_score":15,"inventory_reset_score":12,"utilization_bridge_score":10,"pricing_power_score":10,"relative_strength_score":11,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":76,"stage_label_after":"Stage2-Watch/Yellow-control","component_delta_explanation":"Moderate MFE and low 90D MAE support Watch/Yellow-control, but later drawdown blocks Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C17_R4L86_010060_OCI_POLYSILICON_REBOUND_NO_MARGIN_BRIDGE","trigger_id":"R4L86_C17_010060_20240110_STAGE2_FALSE_POSITIVE_POLYSILICON_REBOUND","symbol":"010060","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_scope":"current_default_proxy","profile_hypothesis":"commodity rebound without durable margin bridge should be blocked","raw_component_scores_before":{"spread_recovery_score":5,"margin_bridge_score":2,"inventory_reset_score":2,"utilization_bridge_score":1,"pricing_power_score":2,"relative_strength_score":9,"valuation_repricing_score":5,"execution_risk_score":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":20,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"spread_recovery_score":1,"margin_bridge_score":0,"inventory_reset_score":0,"utilization_bridge_score":0,"pricing_power_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and high MAE convert commodity rebound into missing-spread bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C17_R4L86_009830_HANWHA_SOLAR_CHEMICAL_BETA","trigger_id":"R4L86_C17_009830_20240110_STAGE2_FALSE_POSITIVE_SOLAR_CHEMICAL_BETA","symbol":"009830","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_scope":"current_default_proxy","profile_hypothesis":"solar/chemical beta without spread recovery should remain Watch/blocked","raw_component_scores_before":{"spread_recovery_score":3,"margin_bridge_score":1,"inventory_reset_score":1,"utilization_bridge_score":0,"pricing_power_score":1,"relative_strength_score":8,"valuation_repricing_score":4,"execution_risk_score":-15,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"spread_recovery_score":0,"margin_bridge_score":0,"inventory_reset_score":0,"utilization_bridge_score":0,"pricing_power_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Near-zero MFE and extreme MAE require spread/margin bridge before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R4L86_C17_P0_CURRENT","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C17 needs explicit spread, margin, utilization and inventory bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":8.32,"avg_MAE90_pct":-18.87,"avg_MFE180_pct":8.32,"avg_MAE180_pct":-40.67,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C17_spread_margin_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R4L86_C17_P1_SECTOR_SPECIFIC","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_id":"P1_L4_chemical_spread_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L4 chemical signals need spread recovery, inventory reset, utilization, pricing power or margin bridge before Stage2-Actionable","changed_axes":["spread_margin_bridge_required","inventory_utilization_bridge_required","commodity_beta_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_spread_margin_inventory_utilization_or_pricing_power_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":8.32,"avg_MAE90_pct":-18.87,"avg_MFE180_pct":8.32,"avg_MAE180_pct":-40.67,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R4L86_C17_P2_CANONICAL","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_id":"P2_C17_spread_margin_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C17 should reward spread/margin recovery, not commodity beta rebound","changed_axes":["C17_spread_margin_bridge_required","C17_commodity_beta_local_4B_guard","C17_solar_chemical_beta_penalty"],"changed_thresholds":{"stage2_yellow_gate":"spread_margin_or_inventory_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":8.32,"avg_MAE90_pct":-18.87,"avg_MFE180_pct":8.32,"avg_MAE180_pct":-40.67,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R4L86_C17_P3_COUNTEREXAMPLE_GUARD","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_id":"P3_C17_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<5 and MAE180<=-30 while spread/margin bridge is missing, block Yellow/Green","changed_axes":["C17_high_MAE_guardrail","C17_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_5_and_MAE180_le_minus_30"},"eligible_trigger_count":3,"avg_MFE90_pct":8.32,"avg_MAE90_pct":-18.87,"avg_MFE180_pct":8.32,"avg_MAE180_pct":-40.67,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_CHEMICAL_SPREAD_RECOVERY_VS_COMMODITY_BETA_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":8.32,"avg_MAE90_pct":-18.87,"avg_MFE180_pct":8.32,"avg_MAE180_pct":-40.67,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_5":0.67,"stage2_bad_entry_rate_MAE180_le_minus_30":0.67,"interpretation":"C17 needs bridge discipline. 코오롱인더 shows a usable spread/margin recovery control, while OCI홀딩스 and 한화솔루션 show commodity/solar-chemical beta can fail badly without durable spread, utilization and margin recovery."}
{"row_type":"stage_transition_summary","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"120110","trigger_type":"Stage2-Actionable-ChemicalIndustrialMarginSpreadBridge-Positive","entry_date":"2024-04-23","stage2_to_90D_outcome":"good_stage2_moderate_MFE_low_MAE","stage2_to_180D_outcome":"watch_positive_with_later_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Watch/Yellow-control when spread and margin bridge exists; Green requires exact utilization and cash evidence."}
{"row_type":"stage_transition_summary","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"010060","trigger_type":"Stage2-FalsePositive-PolysiliconChemicalSpreadRebound-NoMarginBridge","entry_date":"2024-01-10","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_polysilicon_chemical_rebound","MFE90_ge_20":false,"MAE180_le_minus_30":true,"transition_note":"Commodity rebound without durable margin and utilization bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"009830","trigger_type":"Stage2-FalsePositive-SolarChemicalCommodityBeta-NoSpreadRecoveryBridge","entry_date":"2024-01-10","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_extreme_MAE","stage2_to_180D_outcome":"failed_solar_chemical_beta","MFE90_ge_20":false,"MAE180_le_minus_30":true,"transition_note":"Solar/chemical beta without spread recovery and earnings bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","residual_type":"chemical_commodity_beta_overcredit_without_spread_margin_utilization_bridge","contribution":"Adds two C17 local 4B/high-MAE counterexamples against one spread/margin recovery control, avoiding C17 top-covered symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_MARGIN_SPREAD_RECOVERY_BRIDGE_VS_COMMODITY_BETA_AND_SOLAR_CHEMICAL_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C17 now has non-top-symbol commodity-beta counterexamples; next R4 loops should exact-URL repair feedstock/product spread, inventory, utilization, pricing power and margin/cash evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","axis":"C17_spread_margin_utilization_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"120110 worked when spread/margin recovery proxy was present; 010060 and 009830 failed when only commodity/solar chemical beta existed."}
{"row_type":"shadow_weight","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","axis":"C17_commodity_beta_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Commodity/solar-chemical rebound rows showed near-zero MFE and high or extreme MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R4","loop":"86","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","axis":"C17_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<5 and MAE180<=-30 while spread/margin bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - chemical_commodity_beta_overcredit
  - spread_recovery_missing
  - utilization_margin_bridge_missing
  - solar_chemical_beta_extreme_MAE
new_axis_proposed:
  - C17_spread_margin_utilization_bridge_required_shadow_only
  - C17_commodity_beta_local_4B_watch_guard_shadow_only
  - C17_high_MAE_guardrail_shadow_only
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
3. Confirm R4 / L4 / C17 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided C17 top-covered symbols and did not repeat R4 loop84/85 C15/C16 rows.
6. If aggregate support remains stable after exact evidence URL repair, consider C17-scoped safe patch candidates:
   - C17_spread_margin_utilization_bridge_required
   - C17_commodity_beta_local_4B_watch_guard
   - C17_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R4
completed_loop = 86
next_round = R5
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.
```
