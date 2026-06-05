# E2R Stock-Web v12 Residual Research — R10 Loop 86 / L9 / C30

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R10
loop: 86
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: REAL_ESTATE_HOLDCO_REPAIR_BRIDGE_VS_LARGECAP_EPC_AND_CONSTRUCTION_THEME_DECAY
sector: construction / real estate / housing / PF balance sheet / liquidity repair
output_file: e2r_stock_web_v12_residual_round_R10_loop_86_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R9 loop 86`.

```text
scheduled_round = R10
scheduled_loop = 86
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

R10 is restricted to construction / real estate / housing.  
C30 is selected because it is still bad-heavy and stress-heavy in the No-Repeat Index:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rows = 81
symbols = 31
good/bad Stage2 = 16/29
4B/4C = 3/4
top-covered = 002990, 294870, 375500, 004960, 013580, 006360
```

This loop avoids the top-covered list and also avoids the previous R10 loop sets:

```text
R10 loop85: 021320, 001840, 002410
R10 loop84: 035890, 001470, 002780
R10 loop83: 047040, 014790, 005960
```

One symbol, `000720`, appeared in R1/C05 loop86 with a different canonical and trigger family. It is reused here only because C30 has a different failure question: not EPC contract margin, but construction/PF balance-sheet and liquidity bridge. The hard no-repeat key is still new:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"012630","company_name":"HDC","profile_path":"atlas/symbol_profiles/012/012630.json","first_date":"1996-07-01","last_date":"2026-02-20","trading_day_count":7392,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["1997-01-03","1998-12-28","1999-04-12","2018-06-12","2018-10-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"000720","company_name":"현대건설","profile_path":"atlas/symbol_profiles/000/000720.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7740,"corporate_action_candidate_count":7,"corporate_action_candidate_dates":["1998-05-23","1998-11-19","1999-03-05","2001-07-06","2001-07-12","2004-01-13","2004-04-07"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"003070","company_name":"코오롱글로벌","profile_path":"atlas/symbol_profiles/003/003070.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7724,"corporate_action_candidate_count":9,"corporate_action_candidate_dates":["1997-01-03","1999-10-22","2004-12-30","2010-11-23","2012-01-11","2014-05-23","2017-08-01","2023-01-31","2025-12-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here. 2025-12-11 candidate is outside the 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"012630","trigger_type":"Stage2-Actionable-RealEstateHoldcoBalanceSheetRepairBridge-Positive","entry_date":"2024-01-25","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and previous R10 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"000720","trigger_type":"Stage2-FalsePositive-LargecapConstructionPFTheme-NoLiquidityMarginBridge","entry_date":"2024-04-29","duplicate_status":"new C30 symbol/trigger/date combination; same symbol appeared in C05 but not this C30 hard key"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"003070","trigger_type":"Stage2-FalsePositive-ConstructionPolicyThemeSpike-NoPFBacklogCashBridge","entry_date":"2024-06-20","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered and previous R10 loop sets"}
```

## 4. Research question

C30 is not simply “construction stock moved.” It is a balance-sheet and liquidity chamber. The bridge must show PF exposure containment, financing trust, backlog quality, margin protection, and cash conversion. If the market only hears “construction rebound” or “policy support,” the price can jump like a scaffold in wind; without beams, it does not carry weight.

Residual question:

```text
Can C30 distinguish:
1. real-estate holdco / construction balance-sheet repair with low MAE and strong MFE,
2. large-cap construction rebound where PF/liquidity/margin bridge is missing,
3. construction-policy spike where backlog and cash conversion do not support the price?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C30_R10L86_012630_HDC_REALESTATE_HOLDCO_REPAIR","symbol":"012630","company_name":"HDC","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REAL_ESTATE_HOLDCO_BALANCE_SHEET_REPAIR_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-RealEstateHoldcoBalanceSheetRepairBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct_if_balance_sheet_repair_bridge_required","price_source":"Songdaiki/stock-web","notes":"Real-estate holdco/PF-repair proxy produced a strong 2024 rerating with low MAE. Green still requires exact financing trust, PF exposure and NAV/cash bridge evidence."}
{"row_type":"case","case_id":"C30_R10L86_000720_HYUNDAI_CONSTRUCTION_THEME_NO_BRIDGE","symbol":"000720","company_name":"현대건설","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"LARGECAP_CONSTRUCTION_THEME_WITHOUT_LIQUIDITY_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LargecapConstructionPFTheme-NoLiquidityMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_largecap_construction_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Large-cap construction/PF relief theme had almost no MFE and deep 180D MAE without liquidity, financing, backlog-quality and margin bridge."}
{"row_type":"case","case_id":"C30_R10L86_003070_KOLONGLOBAL_POLICY_SPIKE_NO_CASH_BRIDGE","symbol":"003070","company_name":"코오롱글로벌","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_POLICY_THEME_SPIKE_WITHOUT_PF_BACKLOG_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ConstructionPolicyThemeSpike-NoPFBacklogCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_after_theme_spike","current_profile_verdict":"current_profile_false_positive_if_policy_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Construction/policy spike near a local blowoff produced low MFE and deep drawdown when PF/backlog/cash bridge did not follow."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 012630 HDC — real-estate holdco balance-sheet repair bridge positive

Entry row: `2024-01-25 c=6640`.  
Observed path: early low `2024-01-25 l=6470`, 30D high `2024-02-07 h=8820`, 90D high `2024-04-15 h=8890`, and later high `2024-10-17 h=11460`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L86_C30_012630_20240125_STAGE2_HOLDCO_REPAIR","case_id":"C30_R10L86_012630_HDC_REALESTATE_HOLDCO_REPAIR","symbol":"012630","company_name":"HDC","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REAL_ESTATE_HOLDCO_BALANCE_SHEET_REPAIR_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-RealEstateHoldcoBalanceSheetRepairBridge-Positive","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":6640.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_realestate_holdco_balance_sheet_repair_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; real-estate holdco PF exposure repair and NAV/financing trust bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["PF_exposure_repair_proxy","holdco_NAV_repair_proxy","financing_trust_proxy","relative_strength_turn"],"stage3_evidence_fields":["liquidity_bridge_pending","backlog_quality_pending","cash_conversion_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012630/2024.csv","profile_path":"atlas/symbol_profiles/012/012630.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":32.83,"MFE_90D_pct":33.89,"MFE_180D_pct":72.59,"MAE_30D_pct":-2.56,"MAE_90D_pct":-2.56,"MAE_180D_pct":-2.56,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-17","peak_price":11460.0,"max_drawdown_low_date":"2024-01-25","max_drawdown_low":6470.0,"drawdown_after_peak_pct":-10.56,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_repair_path_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct_if_balance_sheet_repair_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"012630_2024-01-25_6640","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 can allow Stage2/Yellow when real-estate/PF repair is tied to financing trust, NAV repair and low-MAE price path. Green still requires exact liquidity, backlog and cash-conversion evidence."}
```

### 6.2 000720 현대건설 — large-cap construction/PF theme without liquidity and margin bridge

Entry row: `2024-04-29 c=35400`.  
Observed path: local high `2024-05-09 h=36000`, then lows `2024-06-27 l=31450`, `2024-10-25 l=27800`, and `2024-12-09 l=24100`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L86_C30_000720_20240429_STAGE2_FALSE_POSITIVE_LARGECAP_CONSTRUCTION","case_id":"C30_R10L86_000720_HYUNDAI_CONSTRUCTION_THEME_NO_BRIDGE","symbol":"000720","company_name":"현대건설","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"LARGECAP_CONSTRUCTION_THEME_WITHOUT_LIQUIDITY_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-LargecapConstructionPFTheme-NoLiquidityMarginBridge","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":35400.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_largecap_construction_PF_relief_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; construction/PF relief theme treated as insufficient without liquidity repair, financing trust, backlog quality and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["construction_PF_relief_theme","relative_strength_rebound"],"stage3_evidence_fields":["liquidity_bridge_missing","financing_trust_missing","margin_bridge_missing","backlog_quality_missing"],"stage4b_evidence_fields":["price_only_local_peak","liquidity_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.69,"MFE_90D_pct":1.69,"MFE_180D_pct":1.69,"MAE_30D_pct":-8.33,"MAE_90D_pct":-11.16,"MAE_180D_pct":-31.92,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-09","peak_price":36000.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":24100.0,"drawdown_after_peak_pct":-33.06,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"construction_theme_peak_without_liquidity_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","liquidity_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_largecap_construction_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"000720_2024-04-29_35400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 should not upgrade construction/PF relief theme without liquidity, financing trust and margin bridge. Near-zero MFE and deep 180D MAE support Watch/4B-risk."}
```

### 6.3 003070 코오롱글로벌 — construction-policy spike without PF/backlog/cash bridge

Entry row: `2024-06-20 c=15740`.  
Observed path: local high `2024-06-21 h=16110`, then lows `2024-07-22 l=10690`, `2024-10-25 l=8660`, and `2024-12-09 l=7920`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L86_C30_003070_20240620_STAGE2_FALSE_POSITIVE_POLICY_SPIKE","case_id":"C30_R10L86_003070_KOLONGLOBAL_POLICY_SPIKE_NO_CASH_BRIDGE","symbol":"003070","company_name":"코오롱글로벌","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_POLICY_THEME_SPIKE_WITHOUT_PF_BACKLOG_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-ConstructionPolicyThemeSpike-NoPFBacklogCashBridge","trigger_date":"2024-06-20","entry_date":"2024-06-20","entry_price":15740.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_construction_policy_theme_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; construction policy/spike treated as insufficient without PF exposure repair, backlog quality, cash conversion and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["construction_policy_theme_spike","relative_strength_extension"],"stage3_evidence_fields":["PF_repair_bridge_missing","backlog_quality_missing","cash_conversion_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","PF_backlog_cash_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv","profile_path":"atlas/symbol_profiles/003/003070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.35,"MFE_90D_pct":2.35,"MFE_180D_pct":2.35,"MAE_30D_pct":-32.08,"MAE_90D_pct":-44.98,"MAE_180D_pct":-49.68,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-21","peak_price":16110.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":7920.0,"drawdown_after_peak_pct":-50.84,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"construction_policy_spike_without_PF_backlog_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","PF_backlog_cash_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_after_theme_spike","current_profile_verdict":"current_profile_false_positive_if_policy_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window; 2025-12-11_candidate_outside_window","same_entry_group_id":"003070_2024-06-20_15740","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 should treat construction-policy blowoff without PF/backlog/cash bridge as 4B-risk. Low MFE and severe MAE show why price-only extension must not become Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C30_R10L86_012630_HDC_REALESTATE_HOLDCO_REPAIR","trigger_id":"R10L86_C30_012630_20240125_STAGE2_HOLDCO_REPAIR","symbol":"012630","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C30 requires PF/liquidity/NAV repair bridge rather than construction rebound alone","raw_component_scores_before":{"PF_exposure_repair":13,"liquidity_bridge":11,"financing_trust":12,"backlog_quality":9,"margin_bridge":7,"NAV_discount_repair":10,"relative_strength_score":12,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"PF_exposure_repair":16,"liquidity_bridge":13,"financing_trust":14,"backlog_quality":11,"margin_bridge":9,"NAV_discount_repair":12,"relative_strength_score":13,"valuation_repricing_score":10,"execution_risk_score":-3,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"PF repair, financing trust and low MAE support Yellow-watch; exact liquidity/backlog/cash bridge still blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C30_R10L86_000720_HYUNDAI_CONSTRUCTION_THEME_NO_BRIDGE","trigger_id":"R10L86_C30_000720_20240429_STAGE2_FALSE_POSITIVE_LARGECAP_CONSTRUCTION","symbol":"000720","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"construction/PF relief theme without liquidity and margin bridge should be blocked","raw_component_scores_before":{"PF_exposure_repair":4,"liquidity_bridge":2,"financing_trust":2,"backlog_quality":5,"margin_bridge":1,"NAV_discount_repair":2,"relative_strength_score":8,"valuation_repricing_score":4,"execution_risk_score":-13,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":24,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":2,"margin_bridge":0,"NAV_discount_repair":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep 180D MAE convert construction/PF theme into missing-bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C30_R10L86_003070_KOLONGLOBAL_POLICY_SPIKE_NO_CASH_BRIDGE","trigger_id":"R10L86_C30_003070_20240620_STAGE2_FALSE_POSITIVE_POLICY_SPIKE","symbol":"003070","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"construction-policy spike without PF/backlog/cash bridge should remain Watch/blocked","raw_component_scores_before":{"PF_exposure_repair":3,"liquidity_bridge":1,"financing_trust":1,"backlog_quality":2,"margin_bridge":0,"NAV_discount_repair":1,"relative_strength_score":13,"valuation_repricing_score":5,"execution_risk_score":-16,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":0,"margin_bridge":0,"NAV_discount_repair":0,"relative_strength_score":4,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Price-only spike plus missing PF/backlog/cash bridge and high MAE blocks Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R10L86_C30_P0_CURRENT","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C30 needs explicit PF exposure, liquidity, financing trust, backlog quality and cash bridge gates","eligible_trigger_count":3,"avg_MFE90_pct":12.64,"avg_MAE90_pct":-19.57,"avg_MFE180_pct":25.54,"avg_MAE180_pct":-28.05,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C30_PF_liquidity_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R10L86_C30_P1_SECTOR_SPECIFIC","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P1_L9_PF_liquidity_financing_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L9 construction signals need PF exposure containment, liquidity repair, financing trust, backlog quality, margin or cash bridge before Stage2-Actionable","changed_axes":["PF_exposure_repair_required","liquidity_financing_bridge_required","construction_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_PF_repair_liquidity_financing_backlog_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":12.64,"avg_MAE90_pct":-19.57,"avg_MFE180_pct":25.54,"avg_MAE180_pct":-28.05,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R10L86_C30_P2_CANONICAL","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P2_C30_PF_liquidity_backlog_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C30 should reward balance-sheet repair, not construction policy or PF-relief price themes","changed_axes":["C30_PF_liquidity_bridge_required","C30_backlog_cash_bridge_required","C30_theme_spike_local_4B_guard"],"changed_thresholds":{"stage2_yellow_gate":"PF_repair_liquidity_financing_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":12.64,"avg_MAE90_pct":-19.57,"avg_MFE180_pct":25.54,"avg_MAE180_pct":-28.05,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R10L86_C30_P3_COUNTEREXAMPLE_GUARD","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P3_C30_low_MFE_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<5 and MAE180<=-30 while PF/liquidity/cash bridge is missing, block Yellow/Green","changed_axes":["C30_high_MAE_guardrail","C30_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_5_and_MAE180_le_minus_30"},"eligible_trigger_count":3,"avg_MFE90_pct":12.64,"avg_MAE90_pct":-19.57,"avg_MFE180_pct":25.54,"avg_MAE180_pct":-28.05,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_HOLDCO_REPAIR_VS_CONSTRUCTION_THEME_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":12.64,"avg_MAE90_pct":-19.57,"avg_MFE180_pct":25.54,"avg_MAE180_pct":-28.05,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_5":0.67,"stage2_bad_entry_rate_MAE180_le_minus_30":0.67,"interpretation":"C30 needs bridge discipline. HDC shows balance-sheet/PF repair can rerate with low MAE, while 현대건설 and 코오롱글로벌 show construction/PF-policy themes can fail without liquidity, financing trust, backlog quality and cash conversion."}
{"row_type":"stage_transition_summary","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"012630","trigger_type":"Stage2-Actionable-RealEstateHoldcoBalanceSheetRepairBridge-Positive","entry_date":"2024-01-25","stage2_to_90D_outcome":"good_stage2_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_holdco_PF_repair_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when PF repair, liquidity, financing trust and NAV bridge exists; Green requires exact backlog/cash evidence."}
{"row_type":"stage_transition_summary","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"000720","trigger_type":"Stage2-FalsePositive-LargecapConstructionPFTheme-NoLiquidityMarginBridge","entry_date":"2024-04-29","stage2_to_90D_outcome":"weak_stage2_near_zero_MFE","stage2_to_180D_outcome":"failed_largecap_construction_theme_deep_MAE","MFE90_ge_20":false,"MAE180_le_minus_30":true,"transition_note":"Construction/PF theme without liquidity and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"003070","trigger_type":"Stage2-FalsePositive-ConstructionPolicyThemeSpike-NoPFBacklogCashBridge","entry_date":"2024-06-20","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_policy_spike_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Construction-policy spike without PF/backlog/cash bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"construction_theme_overcredit_without_PF_liquidity_backlog_cash_bridge","contribution":"Adds two C30 local 4B/high-MAE counterexamples against one balance-sheet repair positive, avoiding C30 top-covered and previous R10 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REAL_ESTATE_HOLDCO_REPAIR_BRIDGE_VS_LARGECAP_EPC_AND_CONSTRUCTION_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C30 now has a non-top-symbol holdco repair control and two construction/PF theme counterexamples; next R10 loops should exact-URL repair PF exposure, financing trust, liquidity, backlog quality, margin and cash conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_PF_liquidity_financing_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"012630 worked with PF/holdco repair bridge proxy; 000720 and 003070 failed when construction/PF-policy themes lacked liquidity, financing, backlog and cash bridge."}
{"row_type":"shadow_weight","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_construction_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Construction/PF-policy theme rows showed near-zero or low MFE and deep MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R10","loop":"86","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_low_MFE_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<5 and MAE180<=-30 while PF/liquidity/cash bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - construction_theme_overcredit
  - PF_liquidity_bridge_missing
  - financing_trust_bridge_missing
  - backlog_cash_bridge_missing
  - price_only_policy_spike_local_4B
new_axis_proposed:
  - C30_PF_liquidity_financing_bridge_required_shadow_only
  - C30_construction_theme_local_4B_watch_guard_shadow_only
  - C30_low_MFE_high_MAE_guardrail_shadow_only
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
5. Confirm this loop avoided:
   - C30 top-covered symbols
   - previous R10 loop85 symbols
   - previous R10 loop84 symbols
   - previous R10 loop83 symbols
6. Accept the 000720 reuse only as cross-canonical reuse, not as duplicate C30 evidence.
7. If aggregate support remains stable after exact evidence URL repair, consider C30-scoped safe patch candidates:
   - C30_PF_liquidity_financing_bridge_required
   - C30_construction_theme_local_4B_watch_guard
   - C30_low_MFE_high_MAE_guardrail
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R10
completed_loop = 86
next_round = R11
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.
```
