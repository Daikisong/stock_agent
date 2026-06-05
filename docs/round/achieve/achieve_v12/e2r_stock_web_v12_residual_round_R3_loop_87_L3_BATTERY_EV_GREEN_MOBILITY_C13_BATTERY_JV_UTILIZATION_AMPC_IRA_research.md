# E2R Stock-Web v12 Residual Research — R3 Loop 87 / L3 / C13

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R3
loop: 87
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: BATTERY_JV_AMPC_UTILIZATION_BRIDGE_VS_COPPERFOIL_CHEMICAL_AMPC_THEME_DECAY
sector: battery / EV / JV / AMPC / IRA / utilization
output_file: e2r_stock_web_v12_residual_round_R3_loop_87_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R2 loop 87`.

```text
scheduled_round = R3
scheduled_loop = 87
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

R3 is restricted to battery / EV / green mobility.  
C13 is selected because the immediately previous R3 loops used C11 orderbook rerating and C12 customer-contract call-off risk. C13 is the AMPC / IRA / JV utilization bucket.

The No-Repeat Index shows C13 as:

```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA
rows = 23
symbols = 16
good/bad Stage2 = 9/2
4B/4C = 2/0
top-covered = 005070, 020150, 003670, 025900, 348370, 002710
```

This loop avoids the top-covered set and also avoids the immediately previous R3 loop85/86 symbols:

```text
R3 loop85 C11: 078600, 247540, 393890
R3 loop86 C12: 317330, 066970, 361610
```

Selected symbols:

```text
096770, 011790, 051910
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"096770","company_name":"SK이노베이션","profile_path":"atlas/symbol_profiles/096/096770.json","first_date":"2007-07-25","last_date":"2026-02-20","trading_day_count":4579,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2024-11-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"The selected entry window is before the 2024-11-20 raw discontinuity candidate. Returns use only the pre-candidate selected forward window for calibration read.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_2024_forward_window_clean_before_2024-11-20_candidate"}
{"row_type":"price_source_validation","symbol":"011790","company_name":"SKC","profile_path":"atlas/symbol_profiles/011/011790.json","first_date":"1997-07-18","last_date":"2026-02-20","trading_day_count":7105,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["1998-01-03","2001-12-21"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"051910","company_name":"LG화학","profile_path":"atlas/symbol_profiles/051/051910.json","first_date":"2001-04-25","last_date":"2026-02-20","trading_day_count":6110,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"096770","trigger_type":"Stage2-Actionable-BatteryJVAMPCUtilizationBridge-Positive","entry_date":"2024-01-22","duplicate_status":"new C13 symbol/trigger/date combination outside top-covered and previous R3 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"011790","trigger_type":"Stage2-FalsePositive-CopperFoilJVAMPCTheme-NoUtilizationMarginBridge","entry_date":"2024-06-14","duplicate_status":"new C13 symbol/trigger/date combination outside top-covered and previous R3 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"051910","trigger_type":"Stage2-FalsePositive-BatteryChemAMPCTheme-NoDirectUtilizationPassThroughBridge","entry_date":"2024-02-16","duplicate_status":"new C13 symbol/trigger/date combination outside top-covered and previous R3 loop symbols"}
```

## 4. Research question

C13 is not “battery stock has IRA or AMPC language.”  
The useful signal is whether the policy credit or JV structure actually passes into utilization, shipment, fixed-cost absorption, customer call-off, margin, and cash conversion. AMPC without utilization is a coupon for a factory that is not yet full.

Residual question:

```text
Can C13 distinguish:
1. battery JV / AMPC / utilization bridge with usable positive rerating,
2. copper-foil or battery-material AMPC/JV theme blowoff without utilization and margin pass-through,
3. large-cap battery-chemical theme where policy credit or vertical-chain wording does not translate into earnings and cash conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C13_R3L87_096770_SKINNOVATION_JV_AMPC_UTILIZATION","symbol":"096770","company_name":"SK이노베이션","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_JV_AMPC_UTILIZATION_BRIDGE","case_type":"watch_positive_control","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-BatteryJVAMPCUtilizationBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_MFE90_ge20_tolerable_180D_MAE","current_profile_verdict":"current_profile_correct_if_JV_AMPC_utilization_bridge_required","price_source":"Songdaiki/stock-web","notes":"JV/AMPC/utilization proxy produced a usable 20%+ MFE with tolerable forward MAE before later corporate-action contamination. This supports Watch/Yellow-control, not Green loosening."}
{"row_type":"case","case_id":"C13_R3L87_011790_SKC_COPPERFOIL_JV_THEME","symbol":"011790","company_name":"SKC","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"COPPERFOIL_JV_AMPC_THEME_WITHOUT_UTILIZATION_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CopperFoilJVAMPCTheme-NoUtilizationMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_late_blowoff_low_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_AMPC_JV_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Copper-foil/JV/AMPC beta near a local extension had low MFE and then extreme MAE when utilization, shipment and margin bridge failed to confirm."}
{"row_type":"case","case_id":"C13_R3L87_051910_LGCHEM_BATTERY_CHEM_THEME","symbol":"051910","company_name":"LG화학","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_CHEM_AMPC_THEME_WITHOUT_DIRECT_UTILIZATION_PASSTHROUGH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-BatteryChemAMPCTheme-NoDirectUtilizationPassThroughBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_credit_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Battery-chemical/policy-credit theme did not produce durable utilization or margin pass-through. Low MFE and deep MAE support Watch/4B-risk routing."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 096770 SK이노베이션 — JV/AMPC utilization bridge positive control

Entry row: `2024-01-22 c=108300`.  
Observed path: entry-day low `2024-01-22 l=108300`, rebound high `2024-02-06 h=130900`, and later selected-window low `2024-08-05 l=91700`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L87_C13_096770_20240122_STAGE2_JV_AMPC_UTILIZATION","case_id":"C13_R3L87_096770_SKINNOVATION_JV_AMPC_UTILIZATION","symbol":"096770","company_name":"SK이노베이션","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_JV_AMPC_UTILIZATION_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-BatteryJVAMPCUtilizationBridge-Positive","trigger_date":"2024-01-22","entry_date":"2024-01-22","entry_price":108300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_battery_JV_AMPC_utilization_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; battery JV/AMPC/utilization bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["JV_structure_proxy","AMPC_credit_proxy","utilization_absorption_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_utilization_source_pending","shipment_calloff_pending","margin_pass_through_pending","cash_conversion_pending"],"stage4b_evidence_fields":["policy_credit_theme_watch","price_only_extension_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv","profile_path":"atlas/symbol_profiles/096/096770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.87,"MFE_90D_pct":20.87,"MFE_180D_pct":20.87,"MAE_30D_pct":0.0,"MAE_90D_pct":-5.26,"MAE_180D_pct":-15.33,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-02-06","peak_price":130900.0,"max_drawdown_low_date":"2024-08-05","max_drawdown_low":91700.0,"drawdown_after_peak_pct":-29.95,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B_without_exact_non_price_utilization_slowdown","four_b_evidence_type":["policy_credit_theme_watch","price_only_extension_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_MFE90_ge20_tolerable_180D_MAE","current_profile_verdict":"current_profile_correct_if_JV_AMPC_utilization_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"selected_window_before_2024-11-20_candidate","same_entry_group_id":"096770_2024-01-22_108300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C13 can allow Watch/Yellow when JV/AMPC is tied to utilization, shipment and fixed-cost absorption. Green still requires exact utilization and margin-pass-through evidence."}
```

### 6.2 011790 SKC — copper-foil/JV/AMPC theme without utilization and margin bridge

Entry row: `2024-06-14 c=195300`.  
Observed path: local high `2024-06-18 h=200000`, then lows `2024-09-24 l=129100` and `2024-12-09 l=90300`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L87_C13_011790_20240614_STAGE2_FALSE_POSITIVE_COPPERFOIL_JV_AMPC","case_id":"C13_R3L87_011790_SKC_COPPERFOIL_JV_THEME","symbol":"011790","company_name":"SKC","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"COPPERFOIL_JV_AMPC_THEME_WITHOUT_UTILIZATION_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-CopperFoilJVAMPCTheme-NoUtilizationMarginBridge","trigger_date":"2024-06-14","entry_date":"2024-06-14","entry_price":195300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_copperfoil_JV_AMPC_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; copper-foil/JV/AMPC theme treated as insufficient without utilization, customer shipment, ASP and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["copperfoil_JV_AMPC_theme","relative_strength_blowoff"],"stage3_evidence_fields":["utilization_bridge_missing","customer_shipment_bridge_missing","ASP_margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","utilization_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv","profile_path":"atlas/symbol_profiles/011/011790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.41,"MFE_90D_pct":2.41,"MFE_180D_pct":2.41,"MAE_30D_pct":-24.63,"MAE_90D_pct":-33.90,"MAE_180D_pct":-53.76,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":200000.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":90300.0,"drawdown_after_peak_pct":-54.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"copperfoil_JV_AMPC_blowoff_without_utilization_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","utilization_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_late_blowoff_low_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_AMPC_JV_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"011790_2024-06-14_195300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C13 should not upgrade AMPC/JV theme blowoff unless utilization, customer shipment, margin and cash pass-through are verified. Low MFE and extreme MAE require 4B-watch routing."}
```

### 6.3 051910 LG화학 — battery-chemical/policy-credit theme without direct utilization pass-through bridge

Entry row: `2024-02-16 c=504000`.  
Observed path: near-term high `2024-02-19 h=520000`, then lows `2024-06-28 l=336500`, `2024-11-06 l=299000`, and later `2024-12-09 l=246000`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L87_C13_051910_20240216_STAGE2_FALSE_POSITIVE_BATTERY_CHEM_AMPC","case_id":"C13_R3L87_051910_LGCHEM_BATTERY_CHEM_THEME","symbol":"051910","company_name":"LG화학","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_CHEM_AMPC_THEME_WITHOUT_DIRECT_UTILIZATION_PASSTHROUGH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-BatteryChemAMPCTheme-NoDirectUtilizationPassThroughBridge","trigger_date":"2024-02-16","entry_date":"2024-02-16","entry_price":504000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_battery_chemical_AMPC_policy_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; battery chemical/AMPC/vertical chain theme treated as insufficient without direct utilization, earnings pass-through, shipment and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["battery_chemical_policy_credit_theme","vertical_chain_rebound"],"stage3_evidence_fields":["direct_utilization_bridge_missing","earnings_pass_through_missing","shipment_visibility_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","pass_through_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv","profile_path":"atlas/symbol_profiles/051/051910.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.17,"MFE_90D_pct":3.17,"MFE_180D_pct":3.17,"MAE_30D_pct":-14.68,"MAE_90D_pct":-33.23,"MAE_180D_pct":-40.67,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":520000.0,"max_drawdown_low_date":"2024-11-06","max_drawdown_low":299000.0,"drawdown_after_peak_pct":-42.50,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"battery_chemical_AMPC_theme_without_direct_utilization_pass_through_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","pass_through_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_credit_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"051910_2024-02-16_504000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C13 should not promote battery-chemical policy-credit theme without direct utilization, earnings pass-through, shipment and margin bridge. Low MFE and deep MAE support Watch/4B-risk."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C13_R3L87_096770_SKINNOVATION_JV_AMPC_UTILIZATION","trigger_id":"R3L87_C13_096770_20240122_STAGE2_JV_AMPC_UTILIZATION","symbol":"096770","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C13 requires JV/AMPC utilization and shipment bridge rather than policy-credit wording alone","raw_component_scores_before":{"AMPC_credit_quality_score":12,"JV_structure_score":11,"utilization_bridge_score":10,"shipment_calloff_score":8,"margin_pass_through_score":7,"cash_conversion_score":5,"relative_strength_score":10,"valuation_repricing_score":6,"execution_risk_score":-6,"theme_spike_risk":-3,"information_confidence":5},"weighted_score_before":65,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"AMPC_credit_quality_score":15,"JV_structure_score":13,"utilization_bridge_score":13,"shipment_calloff_score":10,"margin_pass_through_score":9,"cash_conversion_score":7,"relative_strength_score":11,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":6},"weighted_score_after":77,"stage_label_after":"Stage2-Actionable/Stage3-Yellow-Watch","component_delta_explanation":"JV/AMPC/utilization bridge and MFE90>=20 support Yellow-watch, but exact utilization and margin-pass-through evidence still blocks Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C13_R3L87_011790_SKC_COPPERFOIL_JV_THEME","trigger_id":"R3L87_C13_011790_20240614_STAGE2_FALSE_POSITIVE_COPPERFOIL_JV_AMPC","symbol":"011790","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_scope":"current_default_proxy","profile_hypothesis":"copper-foil AMPC/JV beta without utilization and margin bridge should be blocked","raw_component_scores_before":{"AMPC_credit_quality_score":7,"JV_structure_score":5,"utilization_bridge_score":1,"shipment_calloff_score":1,"margin_pass_through_score":0,"cash_conversion_score":0,"relative_strength_score":14,"valuation_repricing_score":6,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":2,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"AMPC_credit_quality_score":2,"JV_structure_score":1,"utilization_bridge_score":0,"shipment_calloff_score":0,"margin_pass_through_score":0,"cash_conversion_score":0,"relative_strength_score":4,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and extreme MAE convert AMPC/JV blowoff into missing utilization/margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C13_R3L87_051910_LGCHEM_BATTERY_CHEM_THEME","trigger_id":"R3L87_C13_051910_20240216_STAGE2_FALSE_POSITIVE_BATTERY_CHEM_AMPC","symbol":"051910","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_scope":"current_default_proxy","profile_hypothesis":"battery-chemical policy-credit theme without direct utilization pass-through should remain Watch/blocked","raw_component_scores_before":{"AMPC_credit_quality_score":6,"JV_structure_score":3,"utilization_bridge_score":1,"shipment_calloff_score":1,"margin_pass_through_score":0,"cash_conversion_score":0,"relative_strength_score":9,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"AMPC_credit_quality_score":1,"JV_structure_score":0,"utilization_bridge_score":0,"shipment_calloff_score":0,"margin_pass_through_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Low MFE and deep MAE require direct utilization, shipment and margin pass-through before Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R3L87_C13_P0_CURRENT","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C13 needs explicit AMPC quality, JV structure, utilization, shipment and margin-pass-through distinction","eligible_trigger_count":3,"avg_MFE90_pct":8.82,"avg_MAE90_pct":-24.13,"avg_MFE180_pct":8.82,"avg_MAE180_pct":-36.59,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.67,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C13_AMPC_utilization_pass_through_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R3L87_C13_P1_SECTOR_SPECIFIC","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_id":"P1_L3_AMPC_utilization_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L3 AMPC/IRA signals need utilization, shipment call-off, fixed-cost absorption, margin pass-through or cash conversion bridge before Stage2-Actionable","changed_axes":["AMPC_utilization_required","shipment_margin_pass_through_required","policy_credit_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_utilization_shipment_margin_cash_or_fixed_cost_absorption_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":8.82,"avg_MAE90_pct":-24.13,"avg_MFE180_pct":8.82,"avg_MAE180_pct":-36.59,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R3L87_C13_P2_CANONICAL","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_id":"P2_C13_AMPC_utilization_pass_through_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C13 should reward AMPC/JV utilization conversion, not policy-credit or copper-foil beta blowoffs","changed_axes":["C13_utilization_pass_through_required","C13_policy_credit_theme_local_4B_guard","C13_high_MAE_guard"],"changed_thresholds":{"stage2_yellow_gate":"AMPC_or_JV_plus_utilization_or_margin_pass_through_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":8.82,"avg_MAE90_pct":-24.13,"avg_MFE180_pct":8.82,"avg_MAE180_pct":-36.59,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R3L87_C13_P3_COUNTEREXAMPLE_GUARD","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_id":"P3_C13_low_MFE_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<5 and MAE90<=-25 while utilization/pass-through bridge is missing, block Yellow/Green","changed_axes":["C13_low_MFE_guardrail","C13_high_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_5_and_MAE90_le_minus_25"},"eligible_trigger_count":3,"avg_MFE90_pct":8.82,"avg_MAE90_pct":-24.13,"avg_MFE180_pct":8.82,"avg_MAE180_pct":-36.59,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_JV_AMPC_UTILIZATION_VS_POLICY_CREDIT_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":8.82,"avg_MAE90_pct":-24.13,"avg_MFE180_pct":8.82,"avg_MAE180_pct":-36.59,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_5":0.67,"stage2_bad_entry_rate_MAE90_le_minus_25":0.67,"interpretation":"C13 needs bridge discipline. SK이노베이션 shows JV/AMPC/utilization bridge can produce a usable watch-positive rerating, while SKC and LG화학 show that AMPC/JV or policy-credit wording fails without utilization, shipment, margin pass-through and cash conversion."}
{"row_type":"stage_transition_summary","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"096770","trigger_type":"Stage2-Actionable-BatteryJVAMPCUtilizationBridge-Positive","entry_date":"2024-01-22","stage2_to_90D_outcome":"good_stage2_MFE90_ge20_tolerable_MAE","stage2_to_180D_outcome":"watch_positive_AMPC_utilization_bridge","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when AMPC/JV is tied to utilization, shipment and margin-pass-through bridge; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"011790","trigger_type":"Stage2-FalsePositive-CopperFoilJVAMPCTheme-NoUtilizationMarginBridge","entry_date":"2024-06-14","stage2_to_90D_outcome":"bad_stage2_low_MFE_extreme_MAE","stage2_to_180D_outcome":"failed_copperfoil_JV_AMPC_blowoff","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Copper-foil/JV/AMPC blowoff without utilization and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"051910","trigger_type":"Stage2-FalsePositive-BatteryChemAMPCTheme-NoDirectUtilizationPassThroughBridge","entry_date":"2024-02-16","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_battery_chemical_policy_credit_theme","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Battery-chemical policy-credit theme without direct utilization and pass-through bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","residual_type":"AMPC_JV_policy_credit_theme_overcredit_without_utilization_shipment_margin_pass_through","contribution":"Adds two C13 local 4B/high-MAE counterexamples against one JV/AMPC utilization positive, avoiding C13 top-covered and previous R3 C11/C12 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_JV_AMPC_UTILIZATION_BRIDGE_VS_COPPERFOIL_CHEMICAL_AMPC_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C13 now has non-top-symbol AMPC/JV utilization controls and theme-decay counterexamples; next R3 loops should exact-URL repair AMPC quality, JV ownership, utilization, shipment call-off, margin pass-through and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"C13_AMPC_utilization_margin_pass_through_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"096770 worked when AMPC/JV was tied to utilization proxy; 011790 and 051910 failed when policy-credit/JV theme lacked utilization, shipment, margin and cash pass-through."}
{"row_type":"shadow_weight","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"C13_policy_credit_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Copper-foil and battery-chemical policy-credit theme rows showed low MFE and deep/extreme MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R3","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"C13_low_MFE_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<5 and MAE90<=-25 while utilization/pass-through bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - AMPC_policy_credit_overcredit
  - JV_theme_no_utilization_bridge
  - margin_pass_through_missing
  - cash_conversion_bridge_missing
new_axis_proposed:
  - C13_AMPC_utilization_margin_pass_through_required_shadow_only
  - C13_policy_credit_theme_local_4B_watch_guard_shadow_only
  - C13_low_MFE_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C13
  - full_4b_requires_non_price_evidence within C13
  - hard_4c_thesis_break_routes_to_4c within C13
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

All selected triggers use actual Stock-Web tradable raw OHLC rows and clean selected forward windows, with the 096770 selected read explicitly constrained before the later 2024 raw discontinuity candidate.  
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
3. Confirm R3 / L3 / C13 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C13 top-covered symbols
   - previous R3 loop85 C11 symbols
   - previous R3 loop86 C12 symbols
6. Confirm the 096770 read is not imported across the 2024-11-20 raw discontinuity candidate.
7. If aggregate support remains stable after exact evidence URL repair, consider C13-scoped safe patch candidates:
   - C13_AMPC_utilization_margin_pass_through_required
   - C13_policy_credit_theme_local_4B_watch_guard
   - C13_low_MFE_high_MAE_guardrail
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R3
completed_loop = 87
next_round = R4
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R3/L3_BATTERY_EV_GREEN_MOBILITY/C13_BATTERY_JV_UTILIZATION_AMPC_IRA.
```
