# E2R Stock-Web v12 Residual Research — R10 Loop 84 / L9 / C30

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R10
loop: 84
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: REGIONAL_CONSTRUCTION_BALANCE_SHEET_REPAIR_VS_PF_THEME_SPIKE_AND_THESIS_BREAK
sector: construction / real estate / housing / PF balance sheet
output_file: e2r_stock_web_v12_residual_round_R10_loop_84_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R9 loop 84`.

```text
scheduled_round = R10
scheduled_loop = 84
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

R10 is restricted to construction / real estate / housing.  
C30 is selected because it is the core construction/PF balance-sheet bucket. This run avoids the No-Repeat top-covered C30 symbols:

```text
002990, 294870, 375500, 004960, 013580, 006360
```

It also avoids the previous R10 loop83 symbols:

```text
047040, 014790, 005960
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"035890","company_name":"서희건설","profile_path":"atlas/symbol_profiles/035/035890.json","first_date":"1999-12-24","last_date":"2025-08-11","trading_day_count":6310,"corporate_action_candidate_count":9,"corporate_action_candidate_dates":["2000-10-23","2000-11-07","2003-12-10","2004-11-19","2005-05-17","2006-02-17","2007-07-19","2012-01-06","2012-07-12"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024/2025 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_2025_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"001470","company_name":"삼부토건","profile_path":"atlas/symbol_profiles/001/001470.json","first_date":"1995-05-02","last_date":"2025-03-31","trading_day_count":7422,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1996-01-03","2016-05-13","2016-12-23","2017-10-31","2018-09-18","2019-05-02"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"002780","company_name":"진흥기업","profile_path":"atlas/symbol_profiles/002/002780.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7618,"corporate_action_candidate_count":11,"corporate_action_candidate_dates":["1998-01-20","2002-08-16","2006-12-08","2007-11-06","2008-02-22","2009-04-28","2010-08-10","2012-04-17","2013-04-10","2015-01-20","2015-01-28"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"035890","trigger_type":"Stage2-Actionable-RegionalHousingBalanceSheetRepair-Positive","entry_date":"2024-09-24","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered list and previous R10 loop83 set"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"001470","trigger_type":"Stage2-FalsePositive-PFReconstructionThemeSpike-ThesisBreak","entry_date":"2024-03-15","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered list and previous R10 loop83 set"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002780","trigger_type":"Stage2-FalsePositive-ConstructionReliefSpike-NoBacklogMarginBridge","entry_date":"2024-04-09","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered list and previous R10 loop83 set"}
```

## 4. Research question

C30 is not a construction rebound bucket. It is a balance-sheet stress chamber. A construction stock can rise because PF fear cools for a week, but a real E2R bridge needs liquidity repair, PF exposure containment, backlog quality, margin conversion, and financing trust.

Residual question:

```text
Can C30 distinguish:
1. regional housing/contractor repair with low MAE and slow balance-sheet rerating,
2. PF/reconstruction theme spike that breaks into severe thesis failure,
3. small-construction relief spike without backlog/margin/financing bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C30_R10L84_035890_SEOHEE_REGIONAL_HOUSING_REPAIR","symbol":"035890","company_name":"서희건설","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_HOUSING_BALANCE_SHEET_REPAIR_LOW_MAE","case_type":"watch_positive_control","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-RegionalHousingBalanceSheetRepair-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_slow_MFE_low_MAE","current_profile_verdict":"current_profile_correct_if_balance_sheet_repair_bridge_required","price_source":"Songdaiki/stock-web","notes":"Low-MAE slow rerating path supports Watch/Yellow when balance-sheet/PF repair proxy exists; Green still requires exact financing and margin evidence."}
{"row_type":"case","case_id":"C30_R10L84_001470_SAMBU_PF_THEME_THESIS_BREAK","symbol":"001470","company_name":"삼부토건","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_RECONSTRUCTION_THEME_SPIKE_WITH_THESIS_BREAK","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-PFReconstructionThemeSpike-ThesisBreak","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_theme_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"PF/reconstruction theme spike broke into severe drawdown. C30 should route this to Watch/4B-risk or 4C thesis-break rather than Stage2-Actionable."}
{"row_type":"case","case_id":"C30_R10L84_002780_JINHEUNG_RELIEF_SPIKE_NO_BRIDGE","symbol":"002780","company_name":"진흥기업","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_RELIEF_SPIKE_WITHOUT_BACKLOG_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ConstructionReliefSpike-NoBacklogMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_relief_rally_overcredited","price_source":"Songdaiki/stock-web","notes":"Small-construction relief spike had weak upside and persistent high MAE without backlog/margin/financing bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 035890 서희건설 — regional housing balance-sheet repair control

Entry row: `2024-09-24 c=1515`.  
Forward path: 30D high `2024-10-10 h=1621`, 90/180D high `2024-12-18 h=1680`, and low `2024-11-12 l=1391`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L84_C30_035890_20240924_STAGE2_REGIONAL_HOUSING_REPAIR","case_id":"C30_R10L84_035890_SEOHEE_REGIONAL_HOUSING_REPAIR","symbol":"035890","company_name":"서희건설","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_HOUSING_BALANCE_SHEET_REPAIR_LOW_MAE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-RegionalHousingBalanceSheetRepair-Positive","trigger_date":"2024-09-24","entry_date":"2024-09-24","entry_price":1515.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_balance_sheet_repair_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; regional housing/PF balance-sheet repair and financing trust proxy treated as non-price bridge proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["PF_exposure_containment_proxy","balance_sheet_repair_proxy","regional_housing_backlog_proxy","relative_strength_turn"],"stage3_evidence_fields":["margin_bridge_pending","cash_conversion_pending","financing_trust_source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/035/035890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.0,"MFE_90D_pct":10.89,"MFE_180D_pct":10.89,"MAE_30D_pct":-8.12,"MAE_90D_pct":-8.18,"MAE_180D_pct":-8.18,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-18","peak_price":1680.0,"max_drawdown_low_date":"2024-11-12","max_drawdown_low":1391.0,"drawdown_after_peak_pct":-17.2,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_slow_MFE_low_MAE","current_profile_verdict":"current_profile_correct_if_balance_sheet_repair_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_2025_window","same_entry_group_id":"035890_2024-09-24_1515","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 should allow Watch/Yellow when balance-sheet/PF repair has low MAE and slow follow-through. This is not enough to loosen Green without URL-grade financing, backlog-quality, and margin evidence."}
```

### 6.2 001470 삼부토건 — PF/reconstruction theme spike with thesis break

Entry row: `2024-03-15 c=2690`.  
Forward path: same-day peak `h=2865`, then severe break to `2024-04-23 l=1245` and `2024-10-28 l=440`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L84_C30_001470_20240315_STAGE2_FALSE_POSITIVE_PF_THEME_BREAK","case_id":"C30_R10L84_001470_SAMBU_PF_THEME_THESIS_BREAK","symbol":"001470","company_name":"삼부토건","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_RECONSTRUCTION_THEME_SPIKE_WITH_THESIS_BREAK","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_4C_guardrail_review","trigger_type":"Stage2-FalsePositive-PFReconstructionThemeSpike-ThesisBreak","trigger_date":"2024-03-15","entry_date":"2024-03-15","entry_price":2690.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_PF_reconstruction_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; PF/reconstruction/news-theme spike treated as insufficient without liquidity, financing, backlog-quality and going-concern evidence","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["PF_relief_theme","reconstruction_theme_relative_strength"],"stage3_evidence_fields":["liquidity_bridge_missing","financing_trust_missing","backlog_quality_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_break_watch","financing_trust_break_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001470/2024.csv","profile_path":"atlas/symbol_profiles/001/001470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.51,"MFE_90D_pct":6.51,"MFE_180D_pct":6.51,"MAE_30D_pct":-53.72,"MAE_90D_pct":-53.72,"MAE_180D_pct":-83.64,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-15","peak_price":2865.0,"max_drawdown_low_date":"2024-10-28","max_drawdown_low":440.0,"drawdown_after_peak_pct":-84.64,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_peak_without_non_price_bridge_should_be_4B_watch_or_4C_thesis_break","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"hard_4c_candidate_if_financing_or_trust_break_confirmed","trigger_outcome_label":"counterexample_low_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_theme_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"001470_2024-03-15_2690","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 needs a hard financing-trust and liquidity bridge gate. PF/reconstruction theme strength without balance-sheet repair produced extreme MAE and should be blocked from Stage2-Actionable/Yellow."}
```

### 6.3 002780 진흥기업 — construction relief spike without backlog/margin bridge

Entry row: `2024-04-09 c=1511`.  
Forward path: local high `2024-04-09 h=1570`, then lows reached `2024-06-25 l=870` and `2024-10-25 l=720`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L84_C30_002780_20240409_STAGE2_FALSE_POSITIVE_RELIEF_SPIKE","case_id":"C30_R10L84_002780_JINHEUNG_RELIEF_SPIKE_NO_BRIDGE","symbol":"002780","company_name":"진흥기업","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_RELIEF_SPIKE_WITHOUT_BACKLOG_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-ConstructionReliefSpike-NoBacklogMarginBridge","trigger_date":"2024-04-09","entry_date":"2024-04-09","entry_price":1511.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_construction_relief_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; construction relief rally treated as insufficient without backlog, margin, PF exposure containment, and financing bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["construction_relief_price_spike","policy_or_PF_relief_theme"],"stage3_evidence_fields":["backlog_quality_missing","margin_bridge_missing","financing_bridge_missing","PF_exposure_repair_missing"],"stage4b_evidence_fields":["price_only_local_peak","theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002780/2024.csv","profile_path":"atlas/symbol_profiles/002/002780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.9,"MFE_90D_pct":3.9,"MFE_180D_pct":3.9,"MAE_30D_pct":-39.97,"MAE_90D_pct":-42.42,"MAE_180D_pct":-52.35,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-09","peak_price":1570.0,"max_drawdown_low_date":"2024-10-25","max_drawdown_low":720.0,"drawdown_after_peak_pct":-54.14,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"relief_spike_without_backlog_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_relief_rally_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"002780_2024-04-09_1511","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Construction relief spike without backlog-quality, margin and financing bridge produced low MFE and high MAE. C30 should keep it Watch/4B-risk rather than actionable."}
```

## 7. Score simulation rows

These rows are research proxy simulations only and do not change production scoring.

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L84_035890_SEOHEE_REGIONAL_HOUSING_REPAIR","trigger_id":"R10L84_C30_035890_20240924_STAGE2_REGIONAL_HOUSING_REPAIR","symbol":"035890","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C30 recognizes low-MAE balance-sheet/PF repair but keeps Green strict","raw_component_scores_before":{"PF_exposure_repair":12,"liquidity_bridge":11,"backlog_quality":10,"margin_bridge":7,"financing_trust":10,"relative_strength_score":8,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":63,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"PF_exposure_repair":15,"liquidity_bridge":13,"backlog_quality":12,"margin_bridge":8,"financing_trust":12,"relative_strength_score":9,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":72,"stage_label_after":"Stage2-Watch/Yellow-repair-control","component_delta_explanation":"Low MAE and repair proxy allow Watch/Yellow control, but exact financing/margin/cash conversion evidence still blocks Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L84_001470_SAMBU_PF_THEME_THESIS_BREAK","trigger_id":"R10L84_C30_001470_20240315_STAGE2_FALSE_POSITIVE_PF_THEME_BREAK","symbol":"001470","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"PF/reconstruction theme without financing trust and liquidity bridge should be blocked or routed to 4C if thesis break is confirmed","raw_component_scores_before":{"PF_exposure_repair":2,"liquidity_bridge":0,"backlog_quality":2,"margin_bridge":0,"financing_trust":0,"relative_strength_score":14,"valuation_repricing_score":8,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage1/Stage2-Watch-Blocked","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"backlog_quality":0,"margin_bridge":0,"financing_trust":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-25,"theme_spike_risk":-24,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4C-watch","component_delta_explanation":"Extreme MAE and missing financing bridge convert the theme spike into evidence-quality failure and potential 4C watch."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L84_002780_JINHEUNG_RELIEF_SPIKE_NO_BRIDGE","trigger_id":"R10L84_C30_002780_20240409_STAGE2_FALSE_POSITIVE_RELIEF_SPIKE","symbol":"002780","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"construction relief spike without backlog/margin/financing bridge should be blocked","raw_component_scores_before":{"PF_exposure_repair":3,"liquidity_bridge":2,"backlog_quality":2,"margin_bridge":1,"financing_trust":2,"relative_strength_score":12,"valuation_repricing_score":6,"execution_risk_score":-14,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":15,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"PF_exposure_repair":1,"liquidity_bridge":0,"backlog_quality":0,"margin_bridge":0,"financing_trust":1,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-20,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Low MFE and high MAE require a C30 local bridge guard before any Yellow/Green upgrade."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R10L84_C30_P0_CURRENT","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C30 needs explicit financing-trust, liquidity, backlog-quality and margin bridge gates","eligible_trigger_count":3,"avg_MFE_90D_pct":7.1,"avg_MAE_90D_pct":-34.77,"avg_MFE_180D_pct":7.1,"avg_MAE_180D_pct":-48.06,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C30_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R10L84_C30_P1_SECTOR_SPECIFIC","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P1_L9_balance_sheet_repair_candidate","profile_scope":"sector_specific","profile_hypothesis":"L9 construction signals need PF exposure containment, liquidity repair, backlog quality, or financing trust bridge before Stage2-Actionable","changed_axes":["PF_exposure_repair_required","liquidity_bridge_required","financing_trust_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_PF_repair_liquidity_financing_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE_90D_pct":7.1,"avg_MAE_90D_pct":-34.77,"avg_MFE_180D_pct":7.1,"avg_MAE_180D_pct":-48.06,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R10L84_C30_P2_CANONICAL","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P2_C30_balance_sheet_financing_trust_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C30 should reward balance-sheet repair, not PF/reconstruction or relief theme spikes","changed_axes":["C30_financing_trust_bridge_required","C30_PF_liquidity_repair_required","C30_theme_spike_penalty"],"changed_thresholds":{"stage2_yellow_gate":"PF_repair_or_financing_trust_bridge_required"},"eligible_trigger_count":3,"avg_MFE_90D_pct":7.1,"avg_MAE_90D_pct":-34.77,"avg_MFE_180D_pct":7.1,"avg_MAE_180D_pct":-48.06,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R10L84_C30_P3_COUNTEREXAMPLE_GUARD","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P3_C30_high_MAE_or_4C_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-35 while financing/PF repair bridge is missing, block Yellow/Green; if trust/liquidity thesis breaks, route to 4C-watch","changed_axes":["C30_high_MAE_guardrail","C30_local_4B_watch_guard","C30_financing_trust_4C_watch"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_35"},"eligible_trigger_count":3,"avg_MFE_90D_pct":7.1,"avg_MAE_90D_pct":-34.77,"avg_MFE_180D_pct":7.1,"avg_MAE_180D_pct":-48.06,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_BALANCE_SHEET_REPAIR_VS_PF_THEME_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":1,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":7.1,"avg_MAE90_pct":-34.77,"avg_MFE180_pct":7.1,"avg_MAE180_pct":-48.06,"stage2_hit_rate_MFE90_ge_20":0.0,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"stage2_bad_entry_rate_MAE180_le_minus_30":0.67,"interpretation":"C30 needs bridge discipline. 서희건설 is a slow repair control with low MAE, while 삼부토건 and 진흥기업 show that PF/reconstruction/relief theme spikes can become severe high-MAE false positives without financing and backlog-quality bridge."}
{"row_type":"stage_transition_summary","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"035890","trigger_type":"Stage2-Actionable-RegionalHousingBalanceSheetRepair-Positive","entry_date":"2024-09-24","stage2_to_90D_outcome":"watch_positive_low_MAE","stage2_to_180D_outcome":"slow_repair_path","MFE90_ge_20":false,"MAE90_le_minus_20":false,"transition_note":"Allow Watch/Yellow-control only when PF/balance-sheet repair bridge exists; Green remains blocked."}
{"row_type":"stage_transition_summary","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"001470","trigger_type":"Stage2-FalsePositive-PFReconstructionThemeSpike-ThesisBreak","entry_date":"2024-03-15","stage2_to_90D_outcome":"bad_stage2_extreme_MAE","stage2_to_180D_outcome":"4C_watch_or_thesis_break","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"PF/reconstruction theme without financing trust and liquidity bridge should be blocked or routed to 4C-watch."}
{"row_type":"stage_transition_summary","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002780","trigger_type":"Stage2-FalsePositive-ConstructionReliefSpike-NoBacklogMarginBridge","entry_date":"2024-04-09","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"failed_relief_spike","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Relief spike without backlog/margin/financing bridge should stay Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"construction_PF_theme_overcredit_without_financing_liquidity_backlog_bridge","contribution":"Adds two high-MAE C30 false positives and one low-MAE repair control while avoiding C30 top-covered and previous-loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_CONSTRUCTION_BALANCE_SHEET_REPAIR_VS_PF_THEME_SPIKE_AND_THESIS_BREAK","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":1,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C30 now has additional non-top-symbol high-MAE theme-spike rows and one repair control; next R10 loops should exact-URL repair financing trust, PF exposure and backlog quality evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_financing_liquidity_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"035890 low-MAE repair path requires balance-sheet/PF repair bridge; 001470 and 002780 failed without financing/liquidity/backlog-quality bridge."}
{"row_type":"shadow_weight","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_theme_spike_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"PF/reconstruction and construction-relief price spikes showed low MFE and severe MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R10","loop":"84","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_financing_trust_4C_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If liquidity/financing trust breaks and MAE90<=-35 with MFE90<10, block Yellow/Green and route to 4C-watch or evidence-quality repair."}
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
  - construction_PF_theme_overcredit
  - financing_trust_bridge_missing
  - backlog_margin_bridge_missing
  - extreme_MAE_thesis_break_watch
new_axis_proposed:
  - C30_financing_liquidity_bridge_required_shadow_only
  - C30_theme_spike_local_4B_watch_guard_shadow_only
  - C30_financing_trust_4C_watch_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C30
  - full_4b_requires_non_price_evidence within C30
  - hard_4c_thesis_break_routes_to_4c within C30
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
3. Confirm R10 / L9 / C30 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided C30 top-covered symbols and previous R10 loop83 symbols.
6. If aggregate support remains stable after exact evidence URL repair, consider C30-scoped safe patch candidates:
   - C30_financing_liquidity_bridge_required
   - C30_theme_spike_local_4B_watch_guard
   - C30_financing_trust_4C_watch_guard
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R10
completed_loop = 84
next_round = R11
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, 2 local 4B-watch rows, and 1 4C-watch candidate for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.
```
