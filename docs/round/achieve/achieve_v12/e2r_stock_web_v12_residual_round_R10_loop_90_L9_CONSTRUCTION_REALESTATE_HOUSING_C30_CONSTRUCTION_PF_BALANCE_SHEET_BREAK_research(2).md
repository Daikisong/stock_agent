# E2R Stock-Web v12 Residual Research — R10 Loop 90 / L9 / C30

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R10
loop: 90
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: CEMENT_MARGIN_CASH_BRIDGE_VS_READY_MIX_FORMWORK_POLICY_THEME_DECAY
sector: construction / housing / cement / ready-mix concrete / formwork / PF liquidity / backlog / cash conversion
output_file: e2r_stock_web_v12_residual_round_R10_loop_90_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R9 loop 90`.

```text
scheduled_round = R10
scheduled_loop = 90
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

R10 is restricted to construction / real-estate / housing.  
C30 remains the correct R10 archetype because the L9 lane is primarily PF / liquidity / backlog / construction-material balance-sheet stress.

No-Repeat Index snapshot:

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
```

Candidate hygiene note:

```text
During this execution path, R9/C29 mobility candidates and one R8/C27 file-generation path were touched in the surrounding tool calls.
Those rows are not used in this R10/C30 output.
```

Selected symbols:

```text
300720, 023410, 014280
```

This loop tests:

```text
cement input-cost / ASP / margin / cash bridge
vs
ready-mix concrete policy spike without PF-liquidity / backlog / cash bridge
vs
formwork / construction-material rebound without project backlog, margin and working-capital bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"300720","company_name":"한일시멘트","profile_path":"atlas/symbol_profiles/300/300720.json","first_date":"2018-08-06","last_date":"2026-02-20","trading_day_count":1847,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2020-08-14","2021-09-13"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"023410","company_name":"유진기업","profile_path":"atlas/symbol_profiles/023/023410.json","first_date":"1996-07-30","last_date":"2026-02-20","trading_day_count":6791,"corporate_action_candidate_count":9,"corporate_action_candidate_dates":["1996-09-23","1996-11-27","1996-12-26","1997-09-13","2000-01-19","2000-06-09","2006-01-11","2006-05-10","2007-12-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"014280","company_name":"금강공업","profile_path":"atlas/symbol_profiles/014/014280.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7740,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2001-02-13","2002-01-03","2019-05-07"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"300720","trigger_type":"Stage2-Actionable-CementInputCostMarginCashBridge-Positive","entry_date":"2024-01-29","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and previous R10 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"023410","trigger_type":"Stage2-FalsePositive-ReadyMixConcretePolicySpike-NoPFLiquidityBacklogCashBridge","entry_date":"2024-02-23","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and previous R10 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"014280","trigger_type":"Stage2-FalsePositive-FormworkConstructionMaterialRebound-NoBacklogMarginCashBridge","entry_date":"2024-02-13","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and previous R10 loop symbols"}
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
1. cement/materials margin and cash bridge with strong MFE and low early MAE,
2. ready-mix concrete policy spike where local MFE does not prove PF liquidity, backlog or cash conversion,
3. formwork / construction-material rebound where project backlog and margin bridge are missing and later MAE expands?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C30_R10L90_300720_HANIL_CEMENT_MARGIN_CASH","symbol":"300720","company_name":"한일시멘트","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_INPUT_COST_MARGIN_CASH_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-CementInputCostMarginCashBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE90_low_MAE_materials_margin_bridge","current_profile_verdict":"current_profile_correct_if_materials_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Cement/materials margin-cash proxy produced strong MFE with shallow early MAE. Green still requires exact input-cost, ASP, working-capital and cash evidence."}
{"row_type":"case","case_id":"C30_R10L90_023410_EUGENE_READY_MIX_POLICY_SPIKE","symbol":"023410","company_name":"유진기업","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"READY_MIX_CONCRETE_POLICY_SPIKE_WITHOUT_PF_LIQUIDITY_BACKLOG_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ReadyMixConcretePolicySpike-NoPFLiquidityBacklogCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_local_MFE_but_MAE_expansion_no_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_ready_mix_policy_MFE_overcredited","price_source":"Songdaiki/stock-web","notes":"Ready-mix concrete policy spike had local MFE but lacked PF/liquidity/backlog/cash bridge, then drifted into a deeper drawdown."}
{"row_type":"case","case_id":"C30_R10L90_014280_KUMKANG_FORMWORK_REBOUND","symbol":"014280","company_name":"금강공업","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"FORMWORK_CONSTRUCTION_MATERIAL_REBOUND_WITHOUT_BACKLOG_MARGIN_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-FormworkConstructionMaterialRebound-NoBacklogMarginCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_backlog_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_formwork_material_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Formwork/construction-material rebound had low MFE and deep 180D MAE without project backlog, margin and working-capital bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 300720 한일시멘트 — cement input-cost / margin / cash bridge positive

Entry row: `2024-01-29 c=11550`.  
Observed path: entry-area low `2024-01-29 l=11410`, local peak `2024-02-20 h=12910`, and full-window peak `2024-06-05 h=16880`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L90_C30_300720_20240129_STAGE2_CEMENT_MARGIN_CASH","case_id":"C30_R10L90_300720_HANIL_CEMENT_MARGIN_CASH","symbol":"300720","company_name":"한일시멘트","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_INPUT_COST_MARGIN_CASH_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-CementInputCostMarginCashBridge-Positive","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":11550.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_cement_input_cost_ASP_margin_cash_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; cement input-cost pass-through, ASP, margin and cash bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["cement_ASP_proxy","input_cost_pass_through_proxy","margin_cash_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_ASP_source_pending","input_cost_source_pending","working_capital_source_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/300/300720/2024.csv","profile_path":"atlas/symbol_profiles/300/300720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.77,"MFE_90D_pct":46.15,"MFE_180D_pct":46.15,"MAE_30D_pct":-1.21,"MAE_90D_pct":-1.21,"MAE_180D_pct":-1.21,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-05","peak_price":16880.0,"max_drawdown_low_date":"2024-01-29","max_drawdown_low":11410.0,"drawdown_after_peak_pct":-22.75,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.28,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_ASP_margin_working_capital_cash_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE90_low_MAE_materials_margin_bridge","current_profile_verdict":"current_profile_correct_if_materials_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"300720_2024-01-29_11550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 can allow Stage2/Yellow when construction-material strength is tied to ASP, input-cost pass-through, margin repair, working-capital discipline and cash conversion. Green still requires exact source-grade evidence."}
```

### 6.2 023410 유진기업 — ready-mix concrete policy spike without PF/liquidity/backlog/cash bridge

Entry row: `2024-02-23 c=3980`, on a ready-mix / construction-material spike.  
Observed path: same-day high `2024-02-23 h=4580`, followed by drift to `2024-11-15 l=3180` and `2024-12-09 l=3215`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L90_C30_023410_20240223_STAGE2_FALSE_POSITIVE_READY_MIX_POLICY","case_id":"C30_R10L90_023410_EUGENE_READY_MIX_POLICY_SPIKE","symbol":"023410","company_name":"유진기업","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"READY_MIX_CONCRETE_POLICY_SPIKE_WITHOUT_PF_LIQUIDITY_BACKLOG_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;price_only_blowoff_stress_test","trigger_type":"Stage2-FalsePositive-ReadyMixConcretePolicySpike-NoPFLiquidityBacklogCashBridge","trigger_date":"2024-02-23","entry_date":"2024-02-23","entry_price":3980.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_ready_mix_concrete_policy_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; ready-mix concrete/construction-policy spike treated as insufficient without PF repair, liquidity, backlog quality, project margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["ready_mix_concrete_theme","construction_policy_keyword","relative_strength_spike"],"stage3_evidence_fields":["PF_repair_missing","liquidity_bridge_missing","backlog_quality_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_MFE","PF_cash_bridge_missing_watch","MAE_expansion"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/023/023410/2024.csv","profile_path":"atlas/symbol_profiles/023/023410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.08,"MFE_90D_pct":15.08,"MFE_180D_pct":15.08,"MAE_30D_pct":-11.56,"MAE_90D_pct":-13.57,"MAE_180D_pct":-20.10,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-23","peak_price":4580.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":3180.0,"drawdown_after_peak_pct":-30.57,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"ready_mix_policy_spike_without_PF_liquidity_backlog_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","PF_cash_bridge_missing_watch","MAE_expansion"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_local_MFE_but_MAE_expansion_no_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_ready_mix_policy_MFE_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"023410_2024-02-23_3980","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 should not count ready-mix concrete policy MFE as PF/backlog/cash evidence. Without liquidity, backlog quality, project margin and cash conversion, local MFE remains 4B-watch."}
```

### 6.3 014280 금강공업 — formwork / construction-material rebound without backlog/margin/cash bridge

Entry row: `2024-02-13 c=6390`.  
Observed path: high `2024-03-04 h=6540`, then decline to `2024-10-25 l=3975` and `2024-12-09 l=3800`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L90_C30_014280_20240213_STAGE2_FALSE_POSITIVE_FORMWORK_REBOUND","case_id":"C30_R10L90_014280_KUMKANG_FORMWORK_REBOUND","symbol":"014280","company_name":"금강공업","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"FORMWORK_CONSTRUCTION_MATERIAL_REBOUND_WITHOUT_BACKLOG_MARGIN_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-FormworkConstructionMaterialRebound-NoBacklogMarginCashBridge","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":6390.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_formwork_construction_material_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; formwork/construction-material rebound treated as insufficient without project backlog, margin, working-capital and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["formwork_material_rebound","construction_material_keyword","relative_strength_rebound"],"stage3_evidence_fields":["project_backlog_missing","project_margin_missing","working_capital_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["low_MFE_watch","backlog_margin_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014280/2024.csv","profile_path":"atlas/symbol_profiles/014/014280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.35,"MFE_90D_pct":2.35,"MFE_180D_pct":2.35,"MAE_30D_pct":-12.83,"MAE_90D_pct":-17.21,"MAE_180D_pct":-37.79,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-04","peak_price":6540.0,"max_drawdown_low_date":"2024-10-25","max_drawdown_low":3975.0,"drawdown_after_peak_pct":-39.22,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"formwork_material_rebound_without_project_backlog_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","backlog_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_backlog_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_formwork_material_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"014280_2024-02-13_6390","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 should not promote construction-material rebound without project backlog, project margin, working-capital and cash bridge. Low MFE and deep MAE require Watch/4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L90_300720_HANIL_CEMENT_MARGIN_CASH","trigger_id":"R10L90_C30_300720_20240129_STAGE2_CEMENT_MARGIN_CASH","symbol":"300720","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C30 requires PF/liquidity/backlog or construction-materials ASP/margin/cash bridge rather than construction theme alone","raw_component_scores_before":{"PF_exposure_repair":5,"liquidity_bridge":6,"financing_trust":6,"backlog_quality":7,"materials_margin_score":13,"input_cost_pass_through":12,"cash_conversion":9,"relative_strength_score":12,"valuation_repricing_score":7,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"PF_exposure_repair":7,"liquidity_bridge":8,"financing_trust":8,"backlog_quality":9,"materials_margin_score":16,"input_cost_pass_through":15,"cash_conversion":11,"relative_strength_score":13,"valuation_repricing_score":8,"execution_risk_score":-3,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Cement ASP/input-cost/margin/cash bridge plus MFE90 above 40 supports Yellow/Green-candidate watch; exact evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L90_023410_EUGENE_READY_MIX_POLICY_SPIKE","trigger_id":"R10L90_C30_023410_20240223_STAGE2_FALSE_POSITIVE_READY_MIX_POLICY","symbol":"023410","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"ready-mix policy spike without PF/backlog/cash bridge should be blocked even with local MFE","raw_component_scores_before":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":1,"materials_margin_score":2,"input_cost_pass_through":1,"cash_conversion":0,"relative_strength_score":12,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":0,"materials_margin_score":0,"input_cost_pass_through":0,"cash_conversion":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Local MFE is price-only; PF/liquidity/backlog/cash bridge missing and MAE expansion block Yellow/Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L90_014280_KUMKANG_FORMWORK_REBOUND","trigger_id":"R10L90_C30_014280_20240213_STAGE2_FALSE_POSITIVE_FORMWORK_REBOUND","symbol":"014280","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"formwork/material rebound without project backlog and margin bridge should remain Watch/4B","raw_component_scores_before":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":1,"materials_margin_score":2,"input_cost_pass_through":1,"cash_conversion":0,"relative_strength_score":5,"valuation_repricing_score":2,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":0,"materials_margin_score":0,"input_cost_pass_through":0,"cash_conversion":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-20,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE require project backlog, margin and cash evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R10L90_C30_P0_CURRENT","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C30 needs explicit PF/liquidity/backlog/materials-margin/cash bridge and price-only construction-material theme taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":21.19,"avg_MAE90_pct":-10.66,"avg_MFE180_pct":21.19,"avg_MAE180_pct":-19.70,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.76,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C30_PF_backlog_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R10L90_C30_P1_SECTOR_SPECIFIC","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P1_L9_PF_liquidity_materials_cash_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L9 construction signals need PF containment, liquidity, financing trust, backlog quality, margin/cost pass-through or cash bridge before Stage2-Actionable","changed_axes":["PF_liquidity_required","materials_margin_cash_required","construction_material_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_PF_repair_liquidity_financing_backlog_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":21.19,"avg_MAE90_pct":-10.66,"avg_MFE180_pct":21.19,"avg_MAE180_pct":-19.70,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R10L90_C30_P2_CANONICAL","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P2_C30_PF_backlog_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C30 should reward balance-sheet and cash mechanics, not ready-mix/formwork price labels","changed_axes":["C30_PF_backlog_margin_cash_bridge_required","C30_ready_mix_formwork_local_4B_guard","C30_price_only_MFE_not_PF_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"PF_or_liquidity_or_backlog_or_materials_margin_plus_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":21.19,"avg_MAE90_pct":-10.66,"avg_MFE180_pct":21.19,"avg_MAE180_pct":-19.70,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R10L90_C30_P3_COUNTEREXAMPLE_GUARD","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P3_C30_low_MFE_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If PF/backlog/cash bridge is missing, MFE90<20 or MAE180<=-20 should block Yellow/Green and route to Watch/4B","changed_axes":["C30_low_MFE_guardrail","C30_MAE_expansion_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_20_or_MAE180_le_minus_20)"},"eligible_trigger_count":3,"avg_MFE90_pct":21.19,"avg_MAE90_pct":-10.66,"avg_MFE180_pct":21.19,"avg_MAE180_pct":-19.70,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_CEMENT_MARGIN_POSITIVE_VS_READY_MIX_FORMWORK_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":21.19,"avg_MAE90_pct":-10.66,"avg_MFE180_pct":21.19,"avg_MAE180_pct":-19.70,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MFE90_lt20":0.67,"interpretation":"C30 needs bridge discipline. 한일시멘트 shows cement ASP/input-cost/margin/cash bridge can support Yellow/Green-candidate-watch, while 유진기업 and 금강공업 show ready-mix/formwork construction-material price action should not be promoted without PF, liquidity, backlog, project margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"300720","trigger_type":"Stage2-Actionable-CementInputCostMarginCashBridge-Positive","entry_date":"2024-01-29","stage2_to_90D_outcome":"good_stage2_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_materials_margin_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when cement/material strength is tied to ASP, input-cost pass-through, margin and cash bridge; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"023410","trigger_type":"Stage2-FalsePositive-ReadyMixConcretePolicySpike-NoPFLiquidityBacklogCashBridge","entry_date":"2024-02-23","stage2_to_90D_outcome":"price_only_local_MFE_bridge_missing","stage2_to_180D_outcome":"ready_mix_policy_spike_MAE_expansion","MFE90_ge20":false,"MAE180_le_minus20":true,"transition_note":"Ready-mix concrete policy MFE without PF/liquidity/backlog/cash bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"014280","trigger_type":"Stage2-FalsePositive-FormworkConstructionMaterialRebound-NoBacklogMarginCashBridge","entry_date":"2024-02-13","stage2_to_90D_outcome":"bad_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"failed_formwork_rebound_deep_MAE","MFE90_ge20":false,"MAE180_le_minus20":true,"transition_note":"Formwork/material rebound without project backlog and margin/cash bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"construction_material_policy_theme_overcredit_without_PF_backlog_margin_cash_bridge","contribution":"Adds two C30 4B counterexamples against one cement-margin/cash positive, avoiding C30 top-covered and previous R10 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_MARGIN_CASH_BRIDGE_VS_READY_MIX_FORMWORK_POLICY_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C30 now has a non-top-symbol cement/materials positive and two ready-mix/formwork weak-bridge counterexamples; next R10 loops should exact-URL repair PF exposure, liquidity, financing trust, backlog quality, input-cost/ASP margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_PF_backlog_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"300720 worked when cement ASP/margin/cash proxy existed; 023410 and 014280 failed when construction-material price action lacked PF/backlog/cash mechanics."}
{"row_type":"shadow_weight","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_ready_mix_formwork_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Ready-mix and formwork rows showed MFE90 below 20 and later MAE expansion when non-price PF/backlog/margin evidence was missing."}
{"row_type":"shadow_weight","round":"R10","loop":"90","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_price_only_MFE_not_PF_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"023410 shows local MFE should not validate C30 unless PF/liquidity/backlog/cash bridge is exact-repaired."}
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
  - construction_material_theme_overcredit
  - ready_mix_policy_MFE_overcredit
  - PF_liquidity_bridge_missing
  - backlog_margin_cash_bridge_missing
new_axis_proposed:
  - C30_PF_backlog_margin_cash_bridge_required_shadow_only
  - C30_ready_mix_formwork_local_4B_guard_shadow_only
  - C30_price_only_MFE_not_PF_validation_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows and clean selected 2024 entry windows.  
`023410` and `014280` have historical corporate-action candidates before 2024, and `300720` also has pre-2024 candidates; none contaminate the selected 2024 forward entry windows for this residual analysis.  
The non-price evidence layer remains source-name/proxy level for all three rows.

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
5. Confirm this loop avoided:
   - C30 top-covered symbols
   - previous R10 loop83 symbols
   - previous R10 loop84 symbols
   - previous R10 loop85 symbols
   - previous R10 loop86 symbols
   - previous R10 loop87 symbols
   - previous R10 loop88 symbols
   - previous R10 loop89 symbols
6. Confirm accidentally touched R9/C29 and R8/C27 candidate rows are not ingested from this MD.
7. If aggregate support remains stable after exact evidence URL repair, consider C30-scoped safe patch candidates:
   - C30_PF_backlog_margin_cash_bridge_required
   - C30_ready_mix_formwork_local_4B_guard
   - C30_price_only_MFE_not_PF_validation_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R10
completed_loop = 90
next_round = R11
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.
```
