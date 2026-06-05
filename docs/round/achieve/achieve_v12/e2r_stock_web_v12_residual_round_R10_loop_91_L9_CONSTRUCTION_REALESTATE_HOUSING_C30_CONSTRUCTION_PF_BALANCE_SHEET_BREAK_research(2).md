# E2R Stock-Web v12 Residual Research — R10 Loop 91 / L9 / C30

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R10
loop: 91
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: CEMENT_ASP_MARGIN_CASH_BRIDGE_VS_SMALL_CONSTRUCTION_HOME_MATERIALS_VOCABULARY_DECAY
sector: construction / housing / cement / home materials / small construction / PF liquidity / backlog / cash conversion
output_file: e2r_stock_web_v12_residual_round_R10_loop_91_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R9 loop 91`.

```text
scheduled_round = R10
scheduled_loop = 91
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

R10 is restricted to construction / real-estate / housing.  
C30 remains the correct R10 archetype because the L9 lane is primarily PF / liquidity / backlog / construction-material balance-sheet stress.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rows = 81
symbols = 31
good/bad Stage2 = 16/29
4B/4C = 3/4
top-covered = 002990, 294870, 375500, 004960, 013580, 006360
```

This loop avoids the top-covered list and previous R10 loop symbols:

```text
R10 loop83: 047040, 014790, 005960
R10 loop84: 035890, 001470, 002780
R10 loop85: 021320, 001840, 002410
R10 loop86: 012630, 000720, 003070
R10 loop87: 010780, 001260, 013360
R10 loop88: 028050, 002460, 091590
R10 loop89: 004980, 007110, 006920
R10 loop90: 300720, 023410, 014280
```

Candidate hygiene note:

```text
During this execution path, several unused R9/C29 and earlier-sector candidate rows were touched while checking price paths.
Those rows are not used in this R10/C30 output.
```

Selected symbols:

```text
006390, 002290, 025750
```

This loop tests:

```text
cement ASP / input-cost / margin / cash bridge
vs
small construction contract-policy vocabulary without PF/backlog/cash bridge
vs
home-materials / remodeling vocabulary without housing demand, margin and working-capital bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"006390","company_name":"한일현대시멘트","profile_path":"atlas/symbol_profiles/006/006390.json","first_date":"1995-05-02","last_date":"2025-10-29","trading_day_count":7476,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["2000-01-10","2014-04-21","2014-05-16","2014-06-27","2016-10-28"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 forward window; profile is later inactive-like, so keep data-quality watch for production patching.","status_inferred":"inactive_or_delisted_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry; inactive_like_watch"}
{"row_type":"price_source_validation","symbol":"002290","company_name":"삼일기업공사","profile_path":"atlas/symbol_profiles/002/002290.json","first_date":"1996-07-26","last_date":"2026-02-20","trading_day_count":6578,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["1998-02-23","1998-03-21","1998-05-30","1999-07-05","2014-05-16"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"025750","company_name":"한솔홈데코","profile_path":"atlas/symbol_profiles/025/025750.json","first_date":"2003-11-04","last_date":"2026-02-20","trading_day_count":5504,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"006390","trigger_type":"Stage2-Actionable-CementASPMarginCashBridge-PositiveWatch","entry_date":"2024-05-31","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and previous R10 loop symbols; inactive_like_watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002290","trigger_type":"Stage2-FalsePositive-SmallConstructionContractPolicyVocabularyNoPFBacklogCashBridge","entry_date":"2024-01-02","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and previous R10 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"025750","trigger_type":"Stage2-FalsePositive-HomeMaterialsRemodelingVocabularyNoHousingMarginCashBridge","entry_date":"2024-01-10","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and previous R10 loop symbols"}
```

## 4. Research question

C30 is not “건설·자재주가 올랐다.”  
The useful C30 signal must prove a balance-sheet and project-cash bridge:

```text
PF exposure containment
liquidity / financing trust
backlog quality
project margin
input-cost pass-through
materials spread or ASP repair
working-capital discipline
cash conversion
```

A construction-policy or materials spike without this bridge is scaffolding painted gold. It can catch the eye, but it cannot hold the project ledger unless the bolts are in place.

Residual question:

```text
Can C30 distinguish:
1. cement/materials ASP and margin-cash bridge with moderate MFE and controlled early MAE,
2. small construction policy/contract vocabulary where later price spikes do not repair original weak PF/backlog evidence,
3. home-materials/remodeling vocabulary where housing demand, inventory turn, margin and cash conversion are missing?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C30_R10L91_006390_HANIL_HYUNDAI_CEMENT_MARGIN","symbol":"006390","company_name":"한일현대시멘트","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_ASP_INPUT_COST_MARGIN_CASH_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-CementASPMarginCashBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"score_price_alignment":"positive_watch_moderate_MFE_low_entry_MAE_but_inactive_like_data_quality_watch","current_profile_verdict":"current_profile_correct_if_ASP_input_cost_margin_cash_bridge_required_and_data_quality_repaired","price_source":"Songdaiki/stock-web","notes":"Cement ASP/input-cost/margin proxy produced moderate MFE with controlled entry MAE. Positive-watch only; exact ASP/margin/cash evidence and inactive-like data-quality repair are required before any patch."}
{"row_type":"case","case_id":"C30_R10L91_002290_SAMIL_SMALL_CONSTRUCTION_POLICY","symbol":"002290","company_name":"삼일기업공사","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_CONSTRUCTION_CONTRACT_POLICY_VOCABULARY_WITHOUT_PF_BACKLOG_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SmallConstructionContractPolicyVocabularyNoPFBacklogCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_local_MFE_deep_MAE_late_spike_not_validation","current_profile_verdict":"current_profile_false_positive_if_small_construction_policy_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Small construction policy/contract vocabulary had low local MFE and deep drawdown. A later Q4 spike should not validate the original entry without fresh backlog/cash evidence."}
{"row_type":"case","case_id":"C30_R10L91_025750_HANSOL_HOMEDECO_DECAY","symbol":"025750","company_name":"한솔홈데코","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"HOME_MATERIALS_REMODELING_VOCABULARY_WITHOUT_HOUSING_MARGIN_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-HomeMaterialsRemodelingVocabularyNoHousingMarginCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_no_housing_margin_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_home_materials_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Home-materials/remodeling vocabulary had near-zero MFE and persistent decline without housing demand, inventory turn, gross-margin or cash-conversion bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 006390 한일현대시멘트 — cement ASP / input-cost / margin-cash bridge positive-watch

Entry row: `2024-05-31 c=14980`.  
Observed path: entry-area low `2024-06-28 l=14700`, spike peak `2024-06-07 h=17200`, later full-window low `2024-12-09 l=13100`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L91_C30_006390_20240531_STAGE2_CEMENT_ASP_MARGIN","case_id":"C30_R10L91_006390_HANIL_HYUNDAI_CEMENT_MARGIN","symbol":"006390","company_name":"한일현대시멘트","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_ASP_INPUT_COST_MARGIN_CASH_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test;data_quality_watch","trigger_type":"Stage2-Actionable-CementASPMarginCashBridge-PositiveWatch","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":14980.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_cement_ASP_input_cost_margin_cash_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; cement ASP/input-cost pass-through, margin and cash bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["cement_ASP_proxy","input_cost_pass_through_proxy","margin_cash_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_ASP_source_pending","input_cost_source_pending","working_capital_source_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","inactive_like_data_quality_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006390/2024.csv","profile_path":"atlas/symbol_profiles/006/006390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.82,"MFE_90D_pct":14.82,"MFE_180D_pct":14.82,"MAE_30D_pct":-1.87,"MAE_90D_pct":-9.21,"MAE_180D_pct":-12.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-07","peak_price":17200.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":13100.0,"drawdown_after_peak_pct":-23.84,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_but_Green_requires_exact_ASP_margin_working_capital_cash_evidence_and_inactive_like_data_quality_repair","four_b_evidence_type":["price_extension_watch","inactive_like_data_quality_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_watch_moderate_MFE_low_entry_MAE_but_inactive_like_data_quality_watch","current_profile_verdict":"current_profile_correct_if_ASP_input_cost_margin_cash_bridge_required_and_data_quality_repaired","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["inactive_like_profile_watch_before_patch"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean; inactive_like_watch","same_entry_group_id":"006390_2024-05-31_14980","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"do_not_count_as_new_case":false,"current_profile_residual":"C30 can allow Stage2/Yellow-watch when cement/material strength is tied to ASP, input-cost pass-through, margin repair, working-capital discipline and cash conversion. Green requires exact source-grade evidence and data-quality repair."}
```

### 6.2 002290 삼일기업공사 — small construction policy/contract vocabulary without PF/backlog/cash bridge

Entry row: `2024-01-02 c=4220`.  
Observed path: local early high `2024-01-03 h=4325`, deep drawdown to `2024-10-25 l=2800`, and later Q4 spike `2024-12-19 h=4880`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L91_C30_002290_20240102_STAGE2_FALSE_POSITIVE_SMALL_CONSTRUCTION_POLICY","case_id":"C30_R10L91_002290_SAMIL_SMALL_CONSTRUCTION_POLICY","symbol":"002290","company_name":"삼일기업공사","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_CONSTRUCTION_CONTRACT_POLICY_VOCABULARY_WITHOUT_PF_BACKLOG_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;late_spike_not_entry_validation","trigger_type":"Stage2-FalsePositive-SmallConstructionContractPolicyVocabularyNoPFBacklogCashBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":4220.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_small_construction_contract_policy_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; small construction/policy/contract vocabulary treated as insufficient without PF repair, liquidity, backlog quality, project margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["small_construction_policy_keyword","contract_vocabulary","relative_strength_rebound"],"stage3_evidence_fields":["PF_repair_missing","backlog_quality_missing","project_margin_missing","cash_conversion_missing"],"stage4b_evidence_fields":["low_local_MFE","late_spike_not_entry_validation","PF_cash_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002290/2024.csv","profile_path":"atlas/symbol_profiles/002/002290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.49,"MFE_90D_pct":2.49,"MFE_180D_pct":15.64,"MAE_30D_pct":-15.88,"MAE_90D_pct":-19.67,"MAE_180D_pct":-33.65,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-19","peak_price":4880.0,"max_drawdown_low_date":"2024-10-25","max_drawdown_low":2800.0,"drawdown_after_peak_pct":-21.62,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.16,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"small_construction_policy_vocabulary_without_PF_backlog_margin_cash_bridge_should_be_4B_watch_not_positive; late_Q4_spike_requires_fresh_trigger_and_fresh_evidence","four_b_evidence_type":["low_local_MFE","late_spike_not_entry_validation","PF_cash_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_local_MFE_deep_MAE_late_spike_not_validation","current_profile_verdict":"current_profile_false_positive_if_small_construction_policy_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"002290_2024-01-02_4220","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 should not count small construction policy/contract vocabulary as PF/backlog/cash evidence. A late Q4 spike must use a fresh trigger and fresh non-price bridge, not validate the original weak entry."}
```

### 6.3 025750 한솔홈데코 — home-materials/remodeling vocabulary without housing-margin-cash bridge

Entry row: `2024-01-10 c=873`.  
Observed path: entry-area high `2024-01-10 h=887`, then persistent decline to `2024-12-09 l=569`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L91_C30_025750_20240110_STAGE2_FALSE_POSITIVE_HOME_MATERIALS","case_id":"C30_R10L91_025750_HANSOL_HOMEDECO_DECAY","symbol":"025750","company_name":"한솔홈데코","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"HOME_MATERIALS_REMODELING_VOCABULARY_WITHOUT_HOUSING_MARGIN_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-HomeMaterialsRemodelingVocabularyNoHousingMarginCashBridge","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":873.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_home_materials_remodeling_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; home-materials/remodeling vocabulary treated as insufficient without housing demand, SKU/order recovery, gross-margin and working-capital cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["home_materials_vocabulary","remodeling_housing_keyword","relative_strength_rebound"],"stage3_evidence_fields":["housing_demand_missing","SKU_order_recovery_missing","gross_margin_bridge_missing","working_capital_cash_missing"],"stage4b_evidence_fields":["near_zero_MFE","housing_margin_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/025/025750/2024.csv","profile_path":"atlas/symbol_profiles/025/025750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.60,"MFE_90D_pct":1.60,"MFE_180D_pct":1.60,"MAE_30D_pct":-8.36,"MAE_90D_pct":-13.86,"MAE_180D_pct":-34.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-10","peak_price":887.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":569.0,"drawdown_after_peak_pct":-35.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"home_materials_remodeling_vocabulary_without_housing_margin_working_capital_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["near_zero_MFE","housing_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_housing_margin_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_home_materials_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"025750_2024-01-10_873","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 should not promote home-materials/remodeling vocabulary without housing demand, order recovery, gross-margin and working-capital cash bridge. Near-zero MFE and persistent drawdown require Watch/4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L91_006390_HANIL_HYUNDAI_CEMENT_MARGIN","trigger_id":"R10L91_C30_006390_20240531_STAGE2_CEMENT_ASP_MARGIN","symbol":"006390","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C30 requires PF/liquidity/backlog or construction-materials ASP/margin/cash bridge rather than construction theme alone","raw_component_scores_before":{"PF_exposure_repair":4,"liquidity_bridge":5,"financing_trust":5,"backlog_quality":6,"materials_margin_score":12,"input_cost_pass_through":12,"cash_conversion":8,"relative_strength_score":10,"valuation_repricing_score":6,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":65,"stage_label_before":"Stage2-Watch/PositiveControl/DataQualityWatch","raw_component_scores_after":{"PF_exposure_repair":5,"liquidity_bridge":6,"financing_trust":6,"backlog_quality":7,"materials_margin_score":15,"input_cost_pass_through":15,"cash_conversion":10,"relative_strength_score":11,"valuation_repricing_score":7,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":77,"stage_label_after":"Stage2-Actionable/Yellow-Watch/DataQualityWatch","component_delta_explanation":"Cement ASP/input-cost/margin bridge supports Yellow-watch only; inactive-like profile and source-proxy evidence block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L91_002290_SAMIL_SMALL_CONSTRUCTION_POLICY","trigger_id":"R10L91_C30_002290_20240102_STAGE2_FALSE_POSITIVE_SMALL_CONSTRUCTION_POLICY","symbol":"002290","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"small construction policy/contract vocabulary without PF/backlog/cash bridge should be blocked even if a later price spike appears","raw_component_scores_before":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":1,"materials_margin_score":0,"input_cost_pass_through":0,"cash_conversion":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":0,"materials_margin_score":0,"input_cost_pass_through":0,"cash_conversion":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low local MFE, deep MAE and missing PF/backlog/cash bridge block Yellow/Green; Q4 spike needs fresh trigger."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L91_025750_HANSOL_HOMEDECO_DECAY","trigger_id":"R10L91_C30_025750_20240110_STAGE2_FALSE_POSITIVE_HOME_MATERIALS","symbol":"025750","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"home-materials/remodeling vocabulary without housing demand and margin/cash bridge should remain Watch/4B","raw_component_scores_before":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":0,"materials_margin_score":1,"input_cost_pass_through":0,"cash_conversion":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-12,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":0,"materials_margin_score":0,"input_cost_pass_through":0,"cash_conversion":0,"relative_strength_score":0,"valuation_repricing_score":0,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE require housing demand, order recovery, gross-margin and working-capital evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R10L91_C30_P0_CURRENT","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C30 needs explicit PF/liquidity/backlog/materials-margin/cash bridge and construction-policy/home-materials 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":6.30,"avg_MAE90_pct":-14.25,"avg_MFE180_pct":10.69,"avg_MAE180_pct":-27.01,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.72,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C30_PF_backlog_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R10L91_C30_P1_SECTOR_SPECIFIC","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P1_L9_PF_liquidity_materials_cash_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L9 construction signals need PF containment, liquidity, financing trust, backlog quality, margin/cost pass-through or cash bridge before Stage2-Actionable","changed_axes":["PF_liquidity_required","materials_margin_cash_required","construction_policy_home_materials_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_PF_repair_liquidity_financing_backlog_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":6.30,"avg_MAE90_pct":-14.25,"avg_MFE180_pct":10.69,"avg_MAE180_pct":-27.01,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R10L91_C30_P2_CANONICAL","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P2_C30_PF_backlog_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C30 should reward balance-sheet and cash mechanics, not small-construction or home-materials vocabulary","changed_axes":["C30_PF_backlog_margin_cash_bridge_required","C30_small_construction_home_materials_local_4B_guard","C30_late_spike_not_entry_validation_guard","C30_inactive_like_data_quality_guard"],"changed_thresholds":{"stage2_yellow_gate":"PF_or_liquidity_or_backlog_or_materials_margin_plus_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":6.30,"avg_MAE90_pct":-14.25,"avg_MFE180_pct":10.69,"avg_MAE180_pct":-27.01,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R10L91_C30_P3_COUNTEREXAMPLE_GUARD","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P3_C30_low_MFE_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If PF/backlog/cash bridge is missing, local MFE90<5 or MAE180<=-25 should block Yellow/Green and route to Watch/4B","changed_axes":["C30_low_local_MFE_guardrail","C30_MAE_expansion_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_5_or_MAE180_le_minus_25)"},"eligible_trigger_count":3,"avg_MFE90_pct":6.30,"avg_MAE90_pct":-14.25,"avg_MFE180_pct":10.69,"avg_MAE180_pct":-27.01,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_CEMENT_MARGIN_POSITIVE_VS_SMALL_CONSTRUCTION_HOME_MATERIALS_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":6.30,"avg_MAE90_pct":-14.25,"avg_MFE180_pct":10.69,"avg_MAE180_pct":-27.01,"stage2_hit_rate_MFE90_ge10":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE180_le_minus25":0.67,"interpretation":"C30 needs bridge discipline. 한일현대시멘트 shows cement ASP/input-cost/margin bridge can support only Yellow-watch after data-quality repair, while 삼일기업공사 and 한솔홈데코 show small construction or home-materials vocabulary should not be promoted without PF, liquidity, backlog, housing demand, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"006390","trigger_type":"Stage2-Actionable-CementASPMarginCashBridge-PositiveWatch","entry_date":"2024-05-31","stage2_to_90D_outcome":"positive_watch_moderate_MFE_low_entry_MAE","stage2_to_180D_outcome":"cement_margin_bridge_but_inactive_like_data_quality_Green_strict","MFE90_ge10":true,"MAE90_le_minus20":false,"transition_note":"Allow only Yellow-watch when cement/material strength is tied to ASP, input-cost pass-through, margin and cash bridge; Green requires exact evidence plus inactive-like data-quality repair."}
{"row_type":"stage_transition_summary","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002290","trigger_type":"Stage2-FalsePositive-SmallConstructionContractPolicyVocabularyNoPFBacklogCashBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_low_local_MFE_bridge_missing","stage2_to_180D_outcome":"failed_small_construction_policy_deep_MAE_late_spike_not_validation","MFE90_ge10":false,"MAE180_le_minus25":true,"transition_note":"Small construction policy/contract vocabulary without PF/backlog/cash bridge should stay Watch/4B-risk; late Q4 spike needs fresh trigger evidence."}
{"row_type":"stage_transition_summary","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"025750","trigger_type":"Stage2-FalsePositive-HomeMaterialsRemodelingVocabularyNoHousingMarginCashBridge","entry_date":"2024-01-10","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_housing_bridge_missing","stage2_to_180D_outcome":"failed_home_materials_rebound_deep_MAE","MFE90_ge10":false,"MAE180_le_minus25":true,"transition_note":"Home-materials/remodeling vocabulary without housing demand, gross-margin and working-capital bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"small_construction_home_materials_vocabulary_overcredit_without_PF_backlog_margin_cash_bridge","contribution":"Adds two C30 4B counterexamples against one cement-margin positive-watch, avoiding C30 top-covered and previous R10 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_ASP_MARGIN_CASH_BRIDGE_VS_SMALL_CONSTRUCTION_HOME_MATERIALS_VOCABULARY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C30 now has non-top-symbol cement ASP/margin positive-watch and two small-construction/home-materials weak-bridge counterexamples; next R10 loops should exact-URL repair PF exposure, liquidity, financing trust, backlog quality, housing demand, input-cost/ASP margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_PF_backlog_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"006390 worked only as positive-watch when cement ASP/margin proxy existed; 002290 and 025750 failed when construction/home-materials vocabulary lacked PF/backlog/margin/cash mechanics."}
{"row_type":"shadow_weight","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_small_construction_home_materials_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Small construction and home-materials rows showed near-zero local MFE and deep MAE when non-price bridge evidence was missing."}
{"row_type":"shadow_weight","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_late_spike_not_entry_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"002290 shows late Q4 price spikes should not retroactively validate an original weak C30 entry without fresh trigger-date evidence."}
{"row_type":"shadow_weight","round":"R10","loop":"91","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_inactive_like_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"006390 is usable for 2024 residual price-path analysis but has inactive-like profile status later, so patch promotion requires data-quality repair."}
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
  - small_construction_policy_vocabulary_overcredit
  - home_materials_remodeling_vocabulary_overcredit
  - PF_backlog_cash_bridge_missing
  - housing_margin_working_capital_bridge_missing
  - late_spike_not_entry_validation
  - inactive_like_data_quality_watch
new_axis_proposed:
  - C30_PF_backlog_margin_cash_bridge_required_shadow_only
  - C30_small_construction_home_materials_local_4B_guard_shadow_only
  - C30_late_spike_not_entry_validation_guard_shadow_only
  - C30_inactive_like_data_quality_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows.  
`006390` has historical corporate-action candidates before 2024 and later inactive-like profile status, so it is positive-watch only and must not be patched without price-path/evidence repair.  
`002290` has historical corporate-action candidates before 2024, but the selected 2024 window is usable.  
`025750` has no corporate-action candidate in the profile and the selected 2024 window is clean.  
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
inactive_like_data_quality_watch = true for 006390
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
5. Confirm this loop avoided:
   - C30 top-covered symbols
   - previous R10 loop83 symbols
   - previous R10 loop84 symbols
   - previous R10 loop85 symbols
   - previous R10 loop86 symbols
   - previous R10 loop87 symbols
   - previous R10 loop88 symbols
   - previous R10 loop89 symbols
   - previous R10 loop90 symbols
6. Confirm accidentally touched R9/C29 and earlier-sector candidate rows are not ingested from this MD.
7. Keep 006390 in inactive-like / data-quality repair watch before patch consideration.
8. If aggregate support remains stable after exact evidence URL repair, consider C30-scoped safe patch candidates:
   - C30_PF_backlog_margin_cash_bridge_required
   - C30_small_construction_home_materials_local_4B_guard
   - C30_late_spike_not_entry_validation_guard
   - C30_inactive_like_data_quality_guard
9. Do not loosen Stage3-Green.
10. Do not use future MFE/MAE in runtime scoring.
11. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R10
completed_loop = 91
next_round = R11
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive-watch, 2 counterexamples, and 2 local 4B-watch rows for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.
```
