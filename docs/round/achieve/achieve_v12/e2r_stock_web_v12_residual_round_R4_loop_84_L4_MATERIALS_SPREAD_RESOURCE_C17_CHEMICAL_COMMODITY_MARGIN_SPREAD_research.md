# E2R Stock-Web v12 Residual Research — R4 Loop 84 / L4 / C17

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R4
loop: 84
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHEMICAL_SILICONE_SOLAR_PETROCHEM_SPREAD_TO_MARGIN_BRIDGE_VS_PRICE_REBOUND
sector: materials / chemicals / commodity margin spread
output_file: e2r_stock_web_v12_residual_round_R4_loop_84_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R3 loop 84`.

```text
scheduled_round = R4
scheduled_loop = 84
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```

R4 is restricted to L4 materials / spread / resource.  
C17 is selected because the No-Repeat ledger shows materially thinner bad-stage coverage than several other buckets in R4. The loop tests whether a chemical/material spread narrative becomes a real rerating only when it converts into margin, earnings revision, and cash conversion.

This is not a current stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"002380","company_name":"KCC","profile_path":"atlas/symbol_profiles/002/002380.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7740,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2000-04-17"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"011170","company_name":"롯데케미칼","profile_path":"atlas/symbol_profiles/011/011170.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7764,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2023-02-13"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"009830","company_name":"한화솔루션","profile_path":"atlas/symbol_profiles/009/009830.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7741,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["1999-04-20","2008-07-04"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
For C17, the top-covered symbols include `004000`, `006650`, `011780`, `014680`, `298020`, and `001390`. This run avoids that repeated set.

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced here:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"002380","trigger_type":"Stage2-Actionable-SiliconePaintMarginSpreadBridge-Positive","entry_date":"2024-04-19","duplicate_status":"new C17 symbol/trigger/date combination"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"011170","trigger_type":"Stage2-FalsePositive-PetrochemicalSpreadRebound-NoMarginBridge","entry_date":"2024-02-16","duplicate_status":"new C17 symbol/trigger/date combination"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"009830","trigger_type":"Stage2-FalsePositive-SolarChemicalSpreadRebound-NoFCFBridge","entry_date":"2024-04-01","duplicate_status":"new C17 symbol/trigger/date combination; same symbol appeared in prior C31 policy loop but canonical key is different"}
```

## 4. Research question

C17 should not reward commodity-spread headlines by themselves. Spread is the steam; margin and cash conversion are the turbine. Without the turbine, price rebounds become hot air and leave high MAE.

Residual question:

```text
Can C17 distinguish:
1. specialty/paint/silicone margin-spread bridge with sustained MFE,
2. petrochemical spread rebound that fails without margin bridge,
3. solar/chemical policy-spread rebound that fails without FCF and margin conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C17_R4L84_002380_KCC_SILICONE_PAINT_MARGIN_BRIDGE","symbol":"002380","company_name":"KCC","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SILICONE_PAINT_MARGIN_SPREAD_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-SiliconePaintMarginSpreadBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_shallow_MAE","current_profile_verdict":"current_profile_correct_if_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"C17 can work when spread improvement is tied to specialty/material margin bridge and price path confirms sustained MFE."}
{"row_type":"case","case_id":"C17_R4L84_011170_LOTTECHEM_PETROCHEM_SPREAD_FALSE_POSITIVE","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PETROCHEMICAL_SPREAD_REBOUND_WITHOUT_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-PetrochemicalSpreadRebound-NoMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_spread_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Petrochemical spread rebound had tiny MFE and deep MAE; margin/cash bridge was missing."}
{"row_type":"case","case_id":"C17_R4L84_009830_HANWHA_SOLUTION_SOLAR_CHEMICAL_SPREAD_FALSE_POSITIVE","symbol":"009830","company_name":"한화솔루션","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SOLAR_CHEMICAL_SPREAD_REBOUND_WITHOUT_FCF_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SolarChemicalSpreadRebound-NoFCFBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same symbol previously used under C31 policy scope, but this is a new C17 spread/margin trigger family","independent_evidence_weight":1.0,"score_price_alignment":"counterexample_initial_MFE_then_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_spread_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Initial spread/policy rebound failed when margin, spread, and FCF bridge did not hold."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 002380 KCC — silicone/paint margin spread bridge positive

Entry row: `2024-04-19 c=230000`.  
Forward path shows shallow MAE and strong MFE: `2024-05-21 h=327500` and `2024-07-17 h=345000`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L84_C17_002380_20240419_STAGE2_SILICONE_PAINT_MARGIN_BRIDGE","case_id":"C17_R4L84_002380_KCC_SILICONE_PAINT_MARGIN_BRIDGE","symbol":"002380","company_name":"KCC","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SILICONE_PAINT_MARGIN_SPREAD_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-SiliconePaintMarginSpreadBridge-Positive","trigger_date":"2024-04-19","entry_date":"2024-04-19","entry_price":230000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_margin_spread_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; silicone/paint margin-spread bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["asp_or_spread_score","margin_bridge_proxy","relative_strength_turn"],"stage3_evidence_fields":["earnings_revision_proxy","cash_conversion_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002380/2024.csv","profile_path":"atlas/symbol_profiles/002/002380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":42.39,"MFE_90D_pct":50.00,"MFE_180D_pct":50.00,"MAE_30D_pct":-0.22,"MAE_90D_pct":-0.22,"MAE_180D_pct":-5.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-17","peak_price":345000.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":216500.0,"drawdown_after_peak_pct":-37.25,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_shallow_MAE","current_profile_verdict":"current_profile_correct_if_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"002380_2024-04-19_230000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C17 should allow Stage2/Yellow when a spread move is tied to actual margin bridge. Green still requires exact evidence URL, revision, and cash conversion."}
```

### 6.2 011170 롯데케미칼 — petrochemical spread rebound false positive

Entry row: `2024-02-16 c=137300`.  
The rebound peaked almost immediately at `2024-02-19 h=139300`, then fell to `2024-04-19 l=96100` and later `2024-11-18 l=64800`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L84_C17_011170_20240216_STAGE2_FALSE_POSITIVE_PETROCHEM_SPREAD","case_id":"C17_R4L84_011170_LOTTECHEM_PETROCHEM_SPREAD_FALSE_POSITIVE","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PETROCHEMICAL_SPREAD_REBOUND_WITHOUT_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-PetrochemicalSpreadRebound-NoMarginBridge","trigger_date":"2024-02-16","entry_date":"2024-02-16","entry_price":137300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_petrochemical_spread_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; petrochemical spread rebound treated as insufficient without margin/FCF bridge","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["asp_or_spread_score","relative_strength_rebound"],"stage3_evidence_fields":["margin_bridge_missing","revision_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv","profile_path":"atlas/symbol_profiles/011/011170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.46,"MFE_90D_pct":1.46,"MFE_180D_pct":1.46,"MAE_30D_pct":-14.93,"MAE_90D_pct":-30.01,"MAE_180D_pct":-52.80,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":139300.0,"max_drawdown_low_date":"2024-11-18","max_drawdown_low":64800.0,"drawdown_after_peak_pct":-53.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_peak_without_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_spread_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"011170_2024-02-16_137300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Petrochemical spread rebound without margin and cash conversion bridge produced almost no upside and deep MAE. C17 needs a spread-to-margin bridge guard."}
```

### 6.3 009830 한화솔루션 — solar/chemical spread rebound without FCF bridge

Entry row: `2024-04-01 c=29050`.  
The path had a tradable rally to `2024-05-28 h=34550`, but later broke to `2024-12-09 l=14860`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L84_C17_009830_20240401_STAGE2_FALSE_POSITIVE_SOLAR_CHEMICAL_SPREAD","case_id":"C17_R4L84_009830_HANWHA_SOLUTION_SOLAR_CHEMICAL_SPREAD_FALSE_POSITIVE","symbol":"009830","company_name":"한화솔루션","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SOLAR_CHEMICAL_SPREAD_REBOUND_WITHOUT_FCF_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-SolarChemicalSpreadRebound-NoFCFBridge","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":29050.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_solar_chemical_spread_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; solar/chemical spread rebound treated as insufficient without margin/FCF bridge","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["asp_or_spread_score","policy_or_regulatory_score","relative_strength_rebound"],"stage3_evidence_fields":["margin_bridge_missing","FCF_bridge_missing","revision_quality_missing"],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009830/2024.csv","profile_path":"atlas/symbol_profiles/009/009830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.75,"MFE_90D_pct":18.93,"MFE_180D_pct":18.93,"MAE_30D_pct":-20.83,"MAE_90D_pct":-20.83,"MAE_180D_pct":-48.85,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-28","peak_price":34550.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":14860.0,"drawdown_after_peak_pct":-56.99,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_4B_watch_should_activate_after_failed_margin_FCF_bridge","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_initial_MFE_then_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_spread_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"009830_2024-04-01_29050","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same symbol previously used under C31 policy scope, but this is a new C17 chemical-spread trigger family","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Solar/chemical spread rebound can generate initial MFE, but without FCF and margin bridge it becomes a high-MAE false positive. C17 should require economics conversion before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C17_R4L84_002380_KCC_SILICONE_PAINT_MARGIN_BRIDGE","trigger_id":"R4L84_C17_002380_20240419_STAGE2_SILICONE_PAINT_MARGIN_BRIDGE","symbol":"002380","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C17 requires margin bridge and not just spread headline","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":15,"revision_score":10,"relative_strength_score":13,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":12,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":17,"fcf_conversion_score":9},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable/Stage3-Yellow-Watch","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":18,"revision_score":12,"relative_strength_score":15,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":12,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":19,"fcf_conversion_score":11},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Spread-to-margin bridge and shallow MAE support Yellow-watch; exact URL and cash conversion still block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C17_R4L84_011170_LOTTECHEM_PETROCHEM_SPREAD_FALSE_POSITIVE","trigger_id":"R4L84_C17_011170_20240216_STAGE2_FALSE_POSITIVE_PETROCHEM_SPREAD","symbol":"011170","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_scope":"current_default_proxy","profile_hypothesis":"spread rebound without margin bridge should be blocked","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":9,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":12,"fcf_conversion_score":2},"weighted_score_before":48,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":-18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":6,"fcf_conversion_score":0},"weighted_score_after":22,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Tiny MFE and deep MAE convert spread rebound into margin-bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C17_R4L84_009830_HANWHA_SOLUTION_SOLAR_CHEMICAL_SPREAD_FALSE_POSITIVE","trigger_id":"R4L84_C17_009830_20240401_STAGE2_FALSE_POSITIVE_SOLAR_CHEMICAL_SPREAD","symbol":"009830","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_scope":"current_default_proxy","profile_hypothesis":"policy/spread rebound without FCF bridge should stay Watch/4B-risk","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":12,"customer_quality_score":4,"policy_or_regulatory_score":9,"valuation_repricing_score":9,"execution_risk_score":-11,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":13,"fcf_conversion_score":2},"weighted_score_before":56,"stage_label_before":"Stage2-Watch/4B-risk","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":7,"customer_quality_score":3,"policy_or_regulatory_score":7,"valuation_repricing_score":5,"execution_risk_score":-17,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":7,"fcf_conversion_score":0},"weighted_score_after":31,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Initial price rebound cannot offset missing margin, spread durability, and FCF bridge."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R4L84_C17_P0_CURRENT","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C17 needs explicit spread-to-margin/FCF bridge distinction","eligible_trigger_count":3,"avg_MFE_90D_pct":23.46,"avg_MAE_90D_pct":-17.02,"avg_MFE_180D_pct":23.46,"avg_MAE_180D_pct":-35.84,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C17_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R4L84_C17_P1_SECTOR_SPECIFIC","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_id":"P1_L4_spread_to_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L4 spread signals need margin/revision/FCF bridge before Stage2-Actionable","changed_axes":["spread_to_margin_bridge_required","FCF_bridge_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_margin_or_FCF_proxy"},"eligible_trigger_count":3,"avg_MFE_90D_pct":23.46,"avg_MAE_90D_pct":-17.02,"avg_MFE_180D_pct":23.46,"avg_MAE_180D_pct":-35.84,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R4L84_C17_P2_CANONICAL","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_id":"P2_C17_spread_margin_FCF_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C17 should allow spread only when margin and cash conversion evidence exists","changed_axes":["C17_spread_to_margin_bridge_required","C17_FCF_conversion_guard","C17_headline_spread_penalty"],"changed_thresholds":{"stage2_yellow_gate":"margin_or_FCF_bridge_required"},"eligible_trigger_count":3,"avg_MFE_90D_pct":23.46,"avg_MAE_90D_pct":-17.02,"avg_MFE_180D_pct":23.46,"avg_MAE_180D_pct":-35.84,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R4L84_C17_P3_COUNTEREXAMPLE_GUARD","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_id":"P3_C17_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<20 and MAE180<=-35 while margin/FCF bridge is missing, block Yellow/Green","changed_axes":["C17_high_MAE_guardrail","C17_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_20_and_MAE180_le_minus_35"},"eligible_trigger_count":3,"avg_MFE_90D_pct":23.46,"avg_MAE_90D_pct":-17.02,"avg_MFE_180D_pct":23.46,"avg_MAE_180D_pct":-35.84,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_CHEMICAL_SPREAD_TO_MARGIN_BRIDGE_VS_REBOUND_FALSE_POSITIVE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":23.46,"avg_MAE90_pct":-17.02,"avg_MFE180_pct":23.46,"avg_MAE180_pct":-35.84,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_20":0.33,"interpretation":"C17 requires economics conversion. KCC shows a valid spread-to-margin bridge, while Lotte Chemical and Hanwha Solution show rebound traps without margin/FCF bridge."}
{"row_type":"stage_transition_summary","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"002380","trigger_type":"Stage2-Actionable-SiliconePaintMarginSpreadBridge-Positive","entry_date":"2024-04-19","stage2_to_90D_outcome":"good_stage2_high_MFE_shallow_MAE","stage2_to_180D_outcome":"positive_re_rating_path","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when spread-to-margin bridge is visible; Green requires revision and FCF confirmation."}
{"row_type":"stage_transition_summary","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"011170","trigger_type":"Stage2-FalsePositive-PetrochemicalSpreadRebound-NoMarginBridge","entry_date":"2024-02-16","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_rerating_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Petrochemical spread rebound without margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"009830","trigger_type":"Stage2-FalsePositive-SolarChemicalSpreadRebound-NoFCFBridge","entry_date":"2024-04-01","stage2_to_90D_outcome":"bad_stage2_high_MAE_after_initial_MFE","stage2_to_180D_outcome":"failed_rerating_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Initial solar/chemical spread rally failed once FCF and margin bridge did not materialize."}
{"row_type":"residual_contribution","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","residual_type":"chemical_spread_headline_overcredit_without_margin_FCF_bridge","contribution":"Adds two C17 counterexamples against one bridge-positive case, improving counterexample balance and defining a C17-specific spread-to-margin guard.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SILICONE_SOLAR_PETROCHEM_SPREAD_TO_MARGIN_BRIDGE_VS_PRICE_REBOUND","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C17 counterexample balance improved; next R4 loops should add exact URL repair and 4C thesis-break rows for commodity spread reversals."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","axis":"C17_spread_to_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"KCC worked with margin-spread bridge; Lotte Chemical and Hanwha Solution failed without margin/FCF conversion."}
{"row_type":"shadow_weight","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","axis":"C17_FCF_conversion_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Chemical/solar spread rebound can show initial price strength but becomes high-MAE when FCF bridge is missing."}
{"row_type":"shadow_weight","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","axis":"C17_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<20 and MAE180<=-35 without margin/FCF bridge, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - chemical_spread_headline_overcredit
  - petrochemical_rebound_no_margin_bridge
  - solar_chemical_spread_no_FCF_bridge
new_axis_proposed:
  - C17_spread_to_margin_bridge_required_shadow_only
  - C17_FCF_conversion_guard_shadow_only
  - C17_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C17
  - full_4b_requires_non_price_evidence within C17
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
5. If aggregate support remains stable after exact evidence URL repair, consider C17-scoped safe patch candidates:
   - C17_spread_to_margin_bridge_required
   - C17_FCF_conversion_guard
   - C17_high_MAE_guardrail
6. Do not loosen Stage3-Green.
7. Do not use future MFE/MAE in runtime scoring.
8. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R4
completed_loop = 84
next_round = R5
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.
```
