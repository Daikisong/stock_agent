# E2R Stock-Web v12 Residual Research — R10 Loop 89 / L9 / C30

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R10
loop: 89
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: CEMENT_MATERIALS_MARGIN_BRIDGE_VS_STONE_CONCRETE_POLICY_THEME_BLOWOFF_DECAY
sector: construction / real estate / housing / cement / building materials / PF-liquidity bridge
output_file: e2r_stock_web_v12_residual_round_R10_loop_89_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R9 loop 89`.

```text
scheduled_round = R10
scheduled_loop = 89
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

R10 is restricted to construction / real estate / housing.  
C30 is selected again because it remains the main R10 housing/PF balance-sheet archetype and still has a high false-positive share.

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
R10 loop88: 028050, 002460, 091590
R10 loop87: 010780, 001260, 013360
R10 loop86: 012630, 000720, 003070
R10 loop85: 021320, 001840, 002410
R10 loop84: 035890, 001470, 002780
R10 loop83: 047040, 014790, 005960
```

Selected symbols:

```text
004980, 007110, 006920
```

A separate R9/C29 auto-parts candidate sweep was accidentally touched during source lookup. Those rows are not used in this R10/C30 output.

This loop tests:

```text
cement/materials margin bridge as a construction balance-sheet stabilizer
vs
stone / real-estate policy theme spike without PF-liquidity-backlog bridge
vs
ready-mix concrete policy blowoff without backlog/cash evidence
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"004980","company_name":"성신양회","profile_path":"atlas/symbol_profiles/004/004980.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7757,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1998-12-11","1999-03-15","2001-02-01"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"007110","company_name":"일신석재","profile_path":"atlas/symbol_profiles/007/007110.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7708,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1997-01-03","1998-12-21","2000-04-18","2001-01-17","2004-12-02","2005-10-13"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"006920","company_name":"모헨즈","profile_path":"atlas/symbol_profiles/006/006920.json","first_date":"1996-07-29","last_date":"2026-02-20","trading_day_count":6491,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1997-05-26","1999-06-24","2000-03-28","2000-07-31","2000-12-22","2009-06-15"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window; historical zero-volume periods exist but selected 2024 window is tradable.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"004980","trigger_type":"Stage2-Actionable-CementMaterialsMarginCashBridge-Positive","entry_date":"2024-02-01","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and previous R10 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"007110","trigger_type":"Stage2-FalsePositive-StoneRealEstatePolicyTheme-NoPFLiquidityBacklogBridge","entry_date":"2024-01-12","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and previous R10 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"006920","trigger_type":"Stage2-FalsePositive-ReadyMixConcretePolicyBlowoff-NoBacklogCashBridge","entry_date":"2024-02-23","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and previous R10 loop symbols"}
```

## 4. Research question

C30 is not “건설·부동산 관련주가 올랐다.”  
The useful signal must prove a balance-sheet bridge:

```text
PF exposure containment
liquidity repair
financing trust
backlog quality
project margin
working-capital discipline
materials spread or input-cost pass-through
cash conversion
```

A construction-policy theme without that bridge is scaffolding without bolts; it may rise fast, but it cannot safely carry weight.

Residual question:

```text
Can C30 distinguish:
1. cement/materials margin bridge that stabilizes a construction-adjacent balance-sheet case,
2. stone / real-estate policy theme spikes where late political MFE should not validate the original weak entry,
3. ready-mix concrete blowoff where price-only MFE is not PF/liquidity/backlog proof?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C30_R10L89_004980_SUNGSHIN_CEMENT_MARGIN_CASH","symbol":"004980","company_name":"성신양회","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_MATERIALS_MARGIN_CASH_BRIDGE","case_type":"watch_positive_control","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-CementMaterialsMarginCashBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"watch_positive_MFE90_ge15_low_early_MAE_late_drawdown","current_profile_verdict":"current_profile_correct_if_materials_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Cement/materials margin proxy produced a moderate MFE with low early MAE. This is a Yellow-watch positive-control, not a Green loosening case."}
{"row_type":"case","case_id":"C30_R10L89_007110_ILSHIN_STONE_POLICY_THEME","symbol":"007110","company_name":"일신석재","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"STONE_REALESTATE_POLICY_THEME_WITHOUT_PF_LIQUIDITY_BACKLOG_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-StoneRealEstatePolicyTheme-NoPFLiquidityBacklogBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_original_MFE_late_spike_not_validation","current_profile_verdict":"current_profile_false_positive_if_policy_theme_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Stone / real-estate policy theme had weak original bridge. Q4 price bursts should not retroactively validate the January entry without PF/liquidity/backlog/cash evidence."}
{"row_type":"case","case_id":"C30_R10L89_006920_MOHENZ_READY_MIX_POLICY_BLOWOFF","symbol":"006920","company_name":"모헨즈","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"READY_MIX_CONCRETE_POLICY_BLOWOFF_WITHOUT_BACKLOG_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ReadyMixConcretePolicyBlowoff-NoBacklogCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_only_MFE_deep_MAE_no_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_ready_mix_policy_blowoff_counted_as_C30_bridge","price_source":"Songdaiki/stock-web","notes":"Ready-mix concrete policy blowoff produced high local MFE but no PF repair, backlog quality, margin or cash bridge. The move should stay 4B-watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 004980 성신양회 — cement/materials margin-cash bridge watch-positive

Entry row: `2024-02-01 c=8120`.  
Observed path: early low `2024-02-01 l=7970`, high `2024-02-21 h=9590`, and late low `2024-12-09 l=6850`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L89_C30_004980_20240201_STAGE2_CEMENT_MARGIN_CASH","case_id":"C30_R10L89_004980_SUNGSHIN_CEMENT_MARGIN_CASH","symbol":"004980","company_name":"성신양회","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_MATERIALS_MARGIN_CASH_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-CementMaterialsMarginCashBridge-Positive","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":8120.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_cement_materials_margin_cash_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; cement/materials price, input cost and margin/cash bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["cement_margin_proxy","input_cost_pass_through_proxy","cash_conversion_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_margin_source_pending","working_capital_source_pending","PF_exposure_link_pending","cash_conversion_pending"],"stage4b_evidence_fields":["moderate_MFE_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004980/2024.csv","profile_path":"atlas/symbol_profiles/004/004980.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.10,"MFE_90D_pct":18.10,"MFE_180D_pct":18.10,"MAE_30D_pct":-1.85,"MAE_90D_pct":-1.85,"MAE_180D_pct":-15.64,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":9590.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":6850.0,"drawdown_after_peak_pct":-28.57,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_Green; exact cement margin, working-capital and cash evidence required","four_b_evidence_type":["moderate_MFE_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"watch_positive_MFE90_ge15_low_early_MAE_late_drawdown","current_profile_verdict":"current_profile_correct_if_materials_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"004980_2024-02-01_8120","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 can allow Yellow-watch when construction-materials strength is tied to input-cost pass-through, margin and cash conversion. This row does not support Green loosening."}
```

### 6.2 007110 일신석재 — stone / real-estate policy theme without PF-liquidity-backlog bridge

Entry row: `2024-01-12 c=1238`.  
Observed path: local high `2024-01-23 h=1309`, Q4 policy spike highs above `2024-11-27 h=2105` and `2024-12-16 h=2760`, but those late moves are not original-entry validation.

```jsonl
{"row_type":"trigger","trigger_id":"R10L89_C30_007110_20240112_STAGE2_FALSE_POSITIVE_STONE_POLICY","case_id":"C30_R10L89_007110_ILSHIN_STONE_POLICY_THEME","symbol":"007110","company_name":"일신석재","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"STONE_REALESTATE_POLICY_THEME_WITHOUT_PF_LIQUIDITY_BACKLOG_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;late_rebound_not_entry_validation","trigger_type":"Stage2-FalsePositive-StoneRealEstatePolicyTheme-NoPFLiquidityBacklogBridge","trigger_date":"2024-01-12","entry_date":"2024-01-12","entry_price":1238.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_stone_real_estate_policy_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; stone/real-estate policy theme treated as insufficient without PF repair, liquidity, backlog and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["real_estate_policy_theme","stone_materials_keyword","relative_strength_spike"],"stage3_evidence_fields":["PF_repair_missing","liquidity_bridge_missing","backlog_quality_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_late_spike","late_spike_not_entry_validation","PF_cash_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007110/2024.csv","profile_path":"atlas/symbol_profiles/007/007110.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.74,"MFE_90D_pct":5.74,"MFE_180D_pct":5.74,"MAE_30D_pct":-12.36,"MAE_90D_pct":-14.38,"MAE_180D_pct":-14.38,"late_full_year_MFE_pct":122.94,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-23","peak_price":1309.0,"max_drawdown_low_date":"2024-03-21","max_drawdown_low":1060.0,"drawdown_after_peak_pct":-19.02,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"late_policy_spike_should_not_validate_original_weak_entry_without_PF_liquidity_backlog_bridge","four_b_evidence_type":["price_only_late_spike","late_spike_not_entry_validation","PF_cash_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_original_MFE_late_spike_not_validation","current_profile_verdict":"current_profile_false_positive_if_policy_theme_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"007110_2024-01-12_1238","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 should not promote stone/real-estate policy themes unless PF exposure, liquidity, backlog quality and cash bridge are repaired. Late political spikes are not original-entry validation."}
```

### 6.3 006920 모헨즈 — ready-mix concrete policy blowoff without backlog/cash bridge

Entry row: `2024-02-23 c=3775`.  
Observed path: high `2024-02-27 h=5290`, then low `2024-04-11 l=3580` and weak follow-through after the blowoff.

```jsonl
{"row_type":"trigger","trigger_id":"R10L89_C30_006920_20240223_STAGE2_FALSE_POSITIVE_READY_MIX_BLOWOFF","case_id":"C30_R10L89_006920_MOHENZ_READY_MIX_POLICY_BLOWOFF","symbol":"006920","company_name":"모헨즈","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"READY_MIX_CONCRETE_POLICY_BLOWOFF_WITHOUT_BACKLOG_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;price_only_blowoff_stress_test","trigger_type":"Stage2-FalsePositive-ReadyMixConcretePolicyBlowoff-NoBacklogCashBridge","trigger_date":"2024-02-23","entry_date":"2024-02-23","entry_price":3775.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_ready_mix_concrete_policy_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; ready-mix concrete/policy theme treated as insufficient without backlog, project margin, PF/liquidity and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["ready_mix_concrete_theme","regional_policy_keyword","relative_strength_spike"],"stage3_evidence_fields":["backlog_quality_missing","project_margin_missing","PF_liquidity_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_high_MFE","backlog_cash_bridge_missing_watch","blowoff_followthrough_decay"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006920/2024.csv","profile_path":"atlas/symbol_profiles/006/006920.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":40.13,"MFE_90D_pct":40.13,"MFE_180D_pct":40.13,"MAE_30D_pct":-5.17,"MAE_90D_pct":-5.17,"MAE_180D_pct":-5.17,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-27","peak_price":5290.0,"max_drawdown_low_date":"2024-04-11","max_drawdown_low":3580.0,"drawdown_after_peak_pct":-32.33,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_ready_mix_policy_blowoff_without_backlog_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only_high_MFE","backlog_cash_bridge_missing_watch","blowoff_followthrough_decay"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_only_MFE_deep_MAE_no_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_ready_mix_policy_blowoff_counted_as_C30_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"006920_2024-02-23_3775","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 should not count ready-mix concrete policy MFE as PF/backlog/cash evidence. Without backlog quality, project margin, liquidity and cash bridge, high MFE remains price-only 4B."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L89_004980_SUNGSHIN_CEMENT_MARGIN_CASH","trigger_id":"R10L89_C30_004980_20240201_STAGE2_CEMENT_MARGIN_CASH","symbol":"004980","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C30 requires PF/liquidity/backlog or construction-materials margin/cash bridge rather than construction theme alone","raw_component_scores_before":{"PF_exposure_repair":4,"liquidity_bridge":5,"financing_trust":5,"backlog_quality":6,"materials_margin_score":11,"cash_conversion":8,"relative_strength_score":8,"valuation_repricing_score":5,"execution_risk_score":-5,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_before":58,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"PF_exposure_repair":6,"liquidity_bridge":7,"financing_trust":7,"backlog_quality":8,"materials_margin_score":14,"cash_conversion":10,"relative_strength_score":9,"valuation_repricing_score":6,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":75,"stage_label_after":"Stage2-Actionable/Stage3-Yellow-Watch","component_delta_explanation":"Materials margin/cash bridge can lift the row to Yellow-watch, but moderate MFE and late drawdown block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L89_007110_ILSHIN_STONE_POLICY_THEME","trigger_id":"R10L89_C30_007110_20240112_STAGE2_FALSE_POSITIVE_STONE_POLICY","symbol":"007110","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"stone/real-estate policy theme without PF/liquidity/backlog bridge should be blocked despite late spike","raw_component_scores_before":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":1,"materials_margin_score":1,"cash_conversion":0,"relative_strength_score":9,"valuation_repricing_score":3,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":0,"materials_margin_score":0,"cash_conversion":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Original MFE is low and late spike is not validation. Missing PF/liquidity/backlog/cash bridge blocks Yellow/Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L89_006920_MOHENZ_READY_MIX_POLICY_BLOWOFF","trigger_id":"R10L89_C30_006920_20240223_STAGE2_FALSE_POSITIVE_READY_MIX_BLOWOFF","symbol":"006920","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"ready-mix/concrete policy blowoff without backlog/cash bridge should be 4B-watch even with high local MFE","raw_component_scores_before":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":1,"materials_margin_score":2,"cash_conversion":0,"relative_strength_score":14,"valuation_repricing_score":4,"execution_risk_score":-16,"theme_spike_risk":-22,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":0,"materials_margin_score":0,"cash_conversion":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"High MFE is price-only; without backlog, project margin, liquidity and cash conversion, it should not count as C30 positive evidence."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R10L89_C30_P0_CURRENT","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C30 needs explicit PF/liquidity/backlog/materials-margin/cash bridge and late-policy-spike validation taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":21.32,"avg_MAE90_pct":-7.13,"avg_MFE180_pct":21.32,"avg_MAE180_pct":-11.73,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":0.67,"score_return_alignment_verdict":"mixed_without_C30_PF_liquidity_backlog_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R10L89_C30_P1_SECTOR_SPECIFIC","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P1_L9_PF_liquidity_materials_cash_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L9 construction signals need PF containment, liquidity, financing trust, backlog quality, margin/cost pass-through or cash bridge before Stage2-Actionable","changed_axes":["PF_liquidity_required","materials_margin_cash_required","policy_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_PF_repair_liquidity_financing_backlog_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":21.32,"avg_MAE90_pct":-7.13,"avg_MFE180_pct":21.32,"avg_MAE180_pct":-11.73,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R10L89_C30_P2_CANONICAL","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P2_C30_PF_liquidity_backlog_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C30 should reward balance-sheet and cash mechanics, not construction-policy or materials price labels","changed_axes":["C30_PF_liquidity_backlog_cash_bridge_required","C30_policy_materials_theme_local_4B_guard","C30_late_policy_spike_not_entry_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"PF_or_liquidity_or_backlog_or_materials_margin_plus_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":21.32,"avg_MAE90_pct":-7.13,"avg_MFE180_pct":21.32,"avg_MAE180_pct":-11.73,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R10L89_C30_P3_COUNTEREXAMPLE_GUARD","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P3_C30_price_only_policy_spike_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If bridge is missing, high policy-theme MFE cannot validate Stage2/Yellow; late spikes do not validate original weak entries","changed_axes":["C30_price_only_MFE_guardrail","C30_late_spike_not_validation"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_price_only_MFE; late_spike_not_original_entry_validation"},"eligible_trigger_count":3,"avg_MFE90_pct":21.32,"avg_MAE90_pct":-7.13,"avg_MFE180_pct":21.32,"avg_MAE180_pct":-11.73,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_CEMENT_MARGIN_POSITIVE_VS_POLICY_MATERIALS_BLOWOFF_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":21.32,"avg_MAE90_pct":-7.13,"avg_MFE180_pct":21.32,"avg_MAE180_pct":-11.73,"stage2_hit_rate_MFE90_ge_15":0.67,"price_only_policy_spike_count":2,"late_spike_not_entry_validation_count":1,"interpretation":"C30 needs bridge discipline. 성신양회 is a Yellow-watch construction-materials margin/cash bridge, while 일신석재 and 모헨즈 show policy/materials theme MFE should not be promoted without PF, liquidity, backlog and cash evidence."}
{"row_type":"stage_transition_summary","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"004980","trigger_type":"Stage2-Actionable-CementMaterialsMarginCashBridge-Positive","entry_date":"2024-02-01","stage2_to_90D_outcome":"watch_positive_MFE90_ge15_low_MAE","stage2_to_180D_outcome":"watch_positive_with_late_drawdown","MFE90_ge_15":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when materials margin and cash bridge exists; Green requires exact margin, working-capital and cash evidence."}
{"row_type":"stage_transition_summary","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"007110","trigger_type":"Stage2-FalsePositive-StoneRealEstatePolicyTheme-NoPFLiquidityBacklogBridge","entry_date":"2024-01-12","stage2_to_90D_outcome":"weak_stage2_low_original_MFE","stage2_to_180D_outcome":"late_spike_not_original_entry_validation","MFE90_ge_20":false,"late_full_year_MFE_high":true,"transition_note":"Stone/real-estate policy theme without PF/liquidity/backlog bridge should stay Watch/4B-risk; late spike cannot validate original entry."}
{"row_type":"stage_transition_summary","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"006920","trigger_type":"Stage2-FalsePositive-ReadyMixConcretePolicyBlowoff-NoBacklogCashBridge","entry_date":"2024-02-23","stage2_to_90D_outcome":"price_only_high_MFE_without_bridge","stage2_to_180D_outcome":"blowoff_followthrough_decay","MFE90_ge_20":true,"price_only":true,"transition_note":"Ready-mix concrete policy MFE without backlog/cash bridge should be treated as 4B-watch, not positive evidence."}
{"row_type":"residual_contribution","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"construction_policy_materials_theme_overcredit_without_PF_liquidity_backlog_cash_bridge","contribution":"Adds two C30 local 4B/Watch counterexamples against one cement/materials cash bridge positive-control, avoiding C30 top-covered and previous R10 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_MATERIALS_MARGIN_BRIDGE_VS_STONE_CONCRETE_POLICY_THEME_BLOWOFF_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C30 now has non-top-symbol cement/materials margin positive-control and two stone/concrete policy-theme weak-bridge counterexamples; next R10 loops should exact-URL repair PF exposure, liquidity, financing trust, backlog quality, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_PF_liquidity_backlog_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"004980 is usable only when materials margin/cash bridge exists; 007110 and 006920 demonstrate policy/theme price action without PF/liquidity/backlog bridge should not be promoted."}
{"row_type":"shadow_weight","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_policy_materials_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Stone and ready-mix concrete rows showed price-only or policy-theme MFE without non-price balance-sheet/cash mechanics."}
{"row_type":"shadow_weight","round":"R10","loop":"89","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_late_policy_spike_not_entry_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"007110 shows late Q4 policy spikes should not retroactively validate the original weak January entry unless PF/liquidity/backlog evidence is repaired."}
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
  - construction_policy_theme_overcredit
  - materials_theme_MFE_overcredit
  - PF_liquidity_bridge_missing
  - backlog_margin_cash_bridge_missing
new_axis_proposed:
  - C30_PF_liquidity_backlog_cash_bridge_required_shadow_only
  - C30_policy_materials_theme_local_4B_watch_guard_shadow_only
  - C30_late_policy_spike_not_entry_validation_guard_shadow_only
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
5. Confirm this loop avoided:
   - C30 top-covered symbols
   - previous R10 loop88 symbols
   - previous R10 loop87 symbols
   - previous R10 loop86 symbols
   - previous R10 loop85 symbols
   - previous R10 loop84 symbols
   - previous R10 loop83 symbols
6. Confirm accidentally touched R9/C29 candidate rows are not ingested from this MD.
7. If aggregate support remains stable after exact evidence URL repair, consider C30-scoped safe patch candidates:
   - C30_PF_liquidity_backlog_cash_bridge_required
   - C30_policy_materials_theme_local_4B_watch_guard
   - C30_late_policy_spike_not_entry_validation_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R10
completed_loop = 89
next_round = R11
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 watch-positive control, 2 counterexamples, and 2 local 4B-watch rows for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.
```
