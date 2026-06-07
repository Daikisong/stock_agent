# E2R Stock-Web v12 Residual Research — R10 Loop 92 / L9 / C30

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R10
loop: 92
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: CEMENT_MARGIN_CASH_POSITIVE_WATCH_VS_PF_WORKOUT_AND_CA_LATE_PRICE_NONVALIDATION
sector: construction / real estate / housing / cement / PF liquidity / workout / trading halt / balance-sheet break / data quality
output_file: e2r_stock_web_v12_residual_round_R10_loop_92_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R9 loop 92`.

```text
scheduled_round = R10
scheduled_loop = 92
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

R10 is restricted to construction / real-estate / housing.
C30 remains the correct R10 archetype because the L9 lane is primarily PF / liquidity / backlog / construction-material balance-sheet stress.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rows = 97
guidance = PF/유동성/재무제표 hard break 검증 위주
```

This loop avoids known top-covered and recent R10 symbols:

```text
C30 previously top-covered or congested in recent notes:
002990, 294870, 375500, 004960, 013580, 006360

R10 loop83: 047040, 014790, 005960
R10 loop84: 035890, 001470, 002780
R10 loop85: 021320, 001840, 002410
R10 loop86: 012630, 000720, 003070
R10 loop87: 010780, 001260, 013360
R10 loop88: 028050, 002460, 091590
R10 loop89: 004980, 007110, 006920
R10 loop90: 300720, 023410, 014280
R10 loop91: 006390, 002290, 025750
```

Candidate hygiene note:

```text
During this execution path, stale R8/C28, R7/C25 and earlier-sector candidate rows were touched while checking alternatives.
Those rows are not used in this R10/C30 output.
```

Selected symbols:

```text
183190, 009410, 034300
```

The selected pocket is:

```text
cement ASP / materials-margin / cash bridge positive-watch
vs
PF workout / liquidity hard break / trading-halt 4C stress
vs
construction balance-sheet repair vocabulary where late corporate-action price behavior does not validate the original PF/backlog/cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"183190","company_name":"아세아시멘트","profile_path":"atlas/symbol_profiles/183/183190.json","first_date":"2013-11-06","last_date":"2026-02-20","trading_day_count":3013,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2022-04-06"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"009410","company_name":"태영건설","profile_path":"atlas/symbol_profiles/009/009410.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7576,"corporate_action_candidate_count":"profile_tail_not_fetched_in_this_run","corporate_action_candidate_dates":"historical_name_transition_watch; 2024_trading_halt_and_share_count_change_watch","has_major_raw_discontinuity":true,"calibration_caveat":"2024 path has PF workout / trading-halt / restructuring-style discontinuity; usable as hard-break stress only, not ordinary MFE-positive data.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_hard_break_trading_halt_share_count_change_watch"}
{"row_type":"price_source_validation","symbol":"034300","company_name":"신세계건설","profile_path":"atlas/symbol_profiles/034/034300.json","first_date":"1999-06-25","last_date":"2025-01-24","trading_day_count":6312,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["1999-11-16","2024-02-06"],"has_major_raw_discontinuity":true,"calibration_caveat":"2024-02-06 corporate-action candidate and later inactive-like profile status; usable as data-quality/late-price non-validation stress before patching.","status_inferred":"inactive_or_delisted_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_CA_candidate_after_selected_entry; inactive_like_watch"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"183190","trigger_type":"Stage2-Actionable-CementASPMaterialsMarginCashBridge-PositiveWatch","entry_date":"2024-01-29","duplicate_status":"new C30 symbol/trigger/date combination outside recent R10 loop symbols and top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"009410","trigger_type":"Stage2-4C-Validated-PFWorkoutLiquidityHardBreakTradingHalt","entry_date":"2024-01-03","duplicate_status":"new C30 symbol/trigger/date combination outside recent R10 loop symbols; hard 4C/data-quality stress"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"034300","trigger_type":"Stage2-FalsePositive-ConstructionBalanceSheetRepairLatePriceNonValidation","entry_date":"2024-01-18","duplicate_status":"new C30 symbol/trigger/date combination outside recent R10 loop symbols; 2024 CA/inactive-like data-quality watch"}
```

## 4. Research question

C30 is not “건설·시멘트·부동산 단어가 있다.”
The useful C30 signal must prove a balance-sheet and project-cash bridge:

```text
PF exposure containment
liquidity / financing trust
backlog quality
project margin
input-cost pass-through
materials ASP or spread repair
working-capital discipline
cash conversion
hard break / workout / trading-halt / capital event handling
```

A construction headline without this bridge is scaffolding in a storm. It can look tall, but without cash-flow bolts and balance-sheet anchors, the structure does not hold.

Residual question:

```text
Can C30 distinguish:
1. cement/materials ASP-margin-cash bridge that is only positive-watch, not Green,
2. PF workout / liquidity hard break that must be 4C/data-quality stress, not a bargain rebound,
3. late corporate-action or inactive-like price behavior that should not retroactively validate the original weak PF/backlog/cash entry?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C30_R10L92_183190_ASIA_CEMENT_MARGIN","symbol":"183190","company_name":"아세아시멘트","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_ASP_MATERIALS_MARGIN_CASH_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-CementASPMaterialsMarginCashBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_watch_moderate_MFE_low_MAE_materials_margin_cash_bridge","current_profile_verdict":"current_profile_correct_if_ASP_input_cost_margin_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"Cement/materials ASP-margin proxy produced moderate MFE and shallow early MAE. It is useful as Yellow/positive-watch only; exact ASP, cost pass-through, working-capital and cash evidence are required before Green."}
{"row_type":"case","case_id":"C30_R10L92_009410_TAEYOUNG_PF_WORKOUT_HARD_BREAK","symbol":"009410","company_name":"태영건설","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_WORKOUT_LIQUIDITY_HARD_BREAK_TRADING_HALT","case_type":"validated_4C_hard_break","positive_or_counterexample":"counterexample","best_trigger":"Stage2-4C-Validated-PFWorkoutLiquidityHardBreakTradingHalt","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.8,"score_price_alignment":"hard_4C_PF_workout_high_volatility_high_MAE_trading_halt_share_count_change_watch","current_profile_verdict":"current_profile_correct_if_PF_workout_liquidity_hard_break_routes_to_4C_not_bargain_rebound","price_source":"Songdaiki/stock-web","notes":"PF workout/liquidity hard break showed violent MFE/MAE and trading-halt/share-count discontinuity. This is 4C/data-quality stress, not positive C30 evidence."}
{"row_type":"case","case_id":"C30_R10L92_034300_SHINSEGAE_CONSTRUCTION_CA_LATE_PRICE","symbol":"034300","company_name":"신세계건설","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_BALANCE_SHEET_REPAIR_LATE_PRICE_NONVALIDATION","case_type":"failed_entry_data_quality_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ConstructionBalanceSheetRepairLatePriceNonValidation","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"score_price_alignment":"counterexample_CA_late_price_not_original_PF_backlog_cash_validation","current_profile_verdict":"current_profile_false_positive_if_late_corporate_action_price_behavior_validates_original_weak_entry","price_source":"Songdaiki/stock-web","notes":"Construction balance-sheet repair vocabulary had a later price stabilization/spike after corporate-action conditions, but this should not validate the original PF/backlog/cash bridge. Inactive-like status and 2024 CA candidate require repair."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 183190 아세아시멘트 — cement ASP / materials-margin / cash bridge positive-watch

Entry row: `2024-01-29 c=10260`.
Observed path: entry-area low `2024-04-12 l=9790`, 90D high `2024-03-05 h=11610`, and late-year high `2024-10-16 h=11550`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L92_C30_183190_20240129_STAGE2_CEMENT_MARGIN_CASH","case_id":"C30_R10L92_183190_ASIA_CEMENT_MARGIN","symbol":"183190","company_name":"아세아시멘트","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_ASP_MATERIALS_MARGIN_CASH_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-CementASPMaterialsMarginCashBridge-PositiveWatch","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":10260.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_cement_ASP_input_cost_margin_cash_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; cement ASP/input-cost pass-through, materials margin and cash bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["cement_ASP_proxy","input_cost_pass_through_proxy","materials_margin_proxy","cash_conversion_proxy"],"stage3_evidence_fields":["exact_ASP_source_pending","input_cost_source_pending","working_capital_source_pending","cash_conversion_pending"],"stage4b_evidence_fields":["moderate_MFE_watch","Green_strict_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/183/183190/2024.csv","profile_path":"atlas/symbol_profiles/183/183190.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.16,"MFE_90D_pct":13.16,"MFE_180D_pct":13.16,"MAE_30D_pct":-2.34,"MAE_90D_pct":-4.58,"MAE_180D_pct":-4.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-05","peak_price":11610.0,"max_drawdown_low_date":"2024-04-12","max_drawdown_low":9790.0,"drawdown_after_peak_pct":-19.29,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_only; moderate_MFE_requires_exact_ASP_cost_margin_cash_evidence_before_Green","four_b_evidence_type":["moderate_MFE_watch","Green_strict_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_watch_moderate_MFE_low_MAE_materials_margin_cash_bridge","current_profile_verdict":"current_profile_correct_if_ASP_input_cost_margin_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"183190_2024-01-29_10260","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 can allow Yellow/positive-watch when construction-material strength is tied to ASP, input-cost pass-through, margin repair, working-capital discipline and cash conversion. Moderate MFE blocks automatic Green."}
```

### 6.2 009410 태영건설 — PF workout / liquidity hard break / trading halt 4C stress

Entry row: `2024-01-03 c=3245`, during PF/workout volatility.
Observed path: local high `2024-01-11 h=4110`, but drawdown to `2024-01-25 l=2180`, followed by a large trading discontinuity / resumption-style path later in the year. This is not ordinary price discovery.

```jsonl
{"row_type":"trigger","trigger_id":"R10L92_C30_009410_20240103_STAGE2_4C_PF_WORKOUT_HARD_BREAK","case_id":"C30_R10L92_009410_TAEYOUNG_PF_WORKOUT_HARD_BREAK","symbol":"009410","company_name":"태영건설","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_WORKOUT_LIQUIDITY_HARD_BREAK_TRADING_HALT","loop_objective":"hard_4C_confirmation;PF_liquidity_break;data_quality_watch","trigger_type":"Stage2-4C-Validated-PFWorkoutLiquidityHardBreakTradingHalt","trigger_date":"2024-01-03","entry_date":"2024-01-03","entry_price":3245.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_PF_workout_liquidity_hard_break_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; PF workout, liquidity hard break, creditor/restructuring and trading-halt risk treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_credit_event_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["PF_workout_proxy","liquidity_hard_break_proxy","creditor_restructuring_proxy","trading_halt_risk_proxy"],"stage3_evidence_fields":["PF_repair_missing","liquidity_trust_missing","backlog_cash_bridge_missing","ordinary_price_quality_missing"],"stage4b_evidence_fields":["high_volatility","high_MAE","trading_halt_share_count_change_watch"],"stage4c_evidence_fields":["PF_workout_hard_break_watch","liquidity_break_watch","ordinary_rebound_disallowed"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv","profile_path":"atlas/symbol_profiles/009/009410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.66,"MFE_90D_pct":26.66,"MFE_180D_pct":26.66,"MAE_30D_pct":-32.82,"MAE_90D_pct":-32.82,"MAE_180D_pct":-32.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-11","peak_price":4110.0,"max_drawdown_low_date":"2024-01-25","max_drawdown_low":2180.0,"drawdown_after_peak_pct":-46.96,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"PF_workout_liquidity_hard_break_routes_to_4C_not_positive_even_when_local_MFE_exists","four_b_evidence_type":["high_volatility","high_MAE","trading_halt_share_count_change_watch"],"four_c_protection_label":"PF_workout_liquidity_hard_break_ordinary_rebound_disallowed","trigger_outcome_label":"hard_4C_PF_workout_high_volatility_high_MAE_trading_halt_share_count_change_watch","current_profile_verdict":"current_profile_correct_if_PF_workout_liquidity_hard_break_routes_to_4C_not_bargain_rebound","calibration_usable":true,"forward_window_trading_days":"disrupted_by_trading_halt_or_restructuring_watch","calibration_block_reasons":["trading_halt_or_restructuring_share_count_change_watch","hard_4C_credit_event_watch"],"corporate_action_window_status":"2024_discontinuity_watch; ordinary_forward_window_not_clean","same_entry_group_id":"009410_2024-01-03_3245","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.8,"do_not_count_as_new_case":false,"current_profile_residual":"C30 should hard-route PF workout / liquidity hard break / restructuring rows to 4C/data-quality watch. Local MFE is not a positive signal when ordinary tradability and balance-sheet trust are broken."}
```

### 6.3 034300 신세계건설 — construction balance-sheet repair vocabulary / late price non-validation

Entry row: `2024-01-18 c=12600`, during construction balance-sheet repair / liquidity concern vocabulary.
Observed path: same-day high `2024-01-18 h=13920`, then drawdown to `2024-01-25 l=10200`; later price behavior after the 2024-02-06 corporate-action candidate and inactive-like end-state should not validate the original entry.

```jsonl
{"row_type":"trigger","trigger_id":"R10L92_C30_034300_20240118_STAGE2_FALSE_POSITIVE_LATE_PRICE_NONVALIDATION","case_id":"C30_R10L92_034300_SHINSEGAE_CONSTRUCTION_CA_LATE_PRICE","symbol":"034300","company_name":"신세계건설","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_BALANCE_SHEET_REPAIR_LATE_PRICE_NONVALIDATION","loop_objective":"residual_false_positive_mining;data_quality_watch;late_price_not_entry_validation","trigger_type":"Stage2-FalsePositive-ConstructionBalanceSheetRepairLatePriceNonValidation","trigger_date":"2024-01-18","entry_date":"2024-01-18","entry_price":12600.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_construction_balance_sheet_repair_liquidity_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; construction balance-sheet repair vocabulary treated as insufficient without PF repair, liquidity trust, backlog quality, project margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["balance_sheet_repair_vocabulary","construction_liquidity_keyword","relative_strength_spike"],"stage3_evidence_fields":["PF_repair_missing","backlog_quality_missing","project_margin_missing","cash_conversion_missing"],"stage4b_evidence_fields":["post_candidate_data_quality_watch","late_price_not_entry_validation","PF_cash_bridge_missing_watch"],"stage4c_evidence_fields":["inactive_like_or_corporate_action_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv","profile_path":"atlas/symbol_profiles/034/034300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.48,"MFE_90D_pct":10.48,"MFE_180D_pct":45.56,"MAE_30D_pct":-19.05,"MAE_90D_pct":-19.05,"MAE_180D_pct":-19.05,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-30","peak_price":18340.0,"max_drawdown_low_date":"2024-01-25","max_drawdown_low":10200.0,"drawdown_after_peak_pct":-1.58,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.23,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_price_after_CA_or_inactive_like_context_does_not_validate_original_PF_backlog_cash_bridge","four_b_evidence_type":["post_candidate_data_quality_watch","late_price_not_entry_validation","PF_cash_bridge_missing_watch"],"four_c_protection_label":"inactive_like_or_corporate_action_watch_only","trigger_outcome_label":"counterexample_CA_late_price_not_original_PF_backlog_cash_validation","current_profile_verdict":"current_profile_false_positive_if_late_corporate_action_price_behavior_validates_original_weak_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["2024-02-06_corporate_action_candidate_after_entry","inactive_like_profile_watch"],"corporate_action_window_status":"selected_entry_before_2024-02-06_candidate; inactive_like_watch","same_entry_group_id":"034300_2024-01-18_12600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"do_not_count_as_new_case":false,"current_profile_residual":"C30 should not allow late corporate-action or inactive-like price behavior to retroactively validate an original weak PF/backlog/cash entry. Fresh trigger-date evidence and data-quality repair are required."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L92_183190_ASIA_CEMENT_MARGIN","trigger_id":"R10L92_C30_183190_20240129_STAGE2_CEMENT_MARGIN_CASH","symbol":"183190","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C30 requires PF/liquidity/backlog or construction-materials ASP/margin/cash bridge rather than construction theme alone","raw_component_scores_before":{"PF_exposure_repair":3,"liquidity_bridge":4,"financing_trust":4,"backlog_quality":5,"materials_margin_score":10,"input_cost_pass_through":10,"cash_conversion":7,"relative_strength_score":6,"valuation_repricing_score":4,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":55,"stage_label_before":"Stage2-Watch/PositiveControl","raw_component_scores_after":{"PF_exposure_repair":4,"liquidity_bridge":5,"financing_trust":5,"backlog_quality":6,"materials_margin_score":13,"input_cost_pass_through":13,"cash_conversion":9,"relative_strength_score":7,"valuation_repricing_score":5,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":70,"stage_label_after":"Stage2-PositiveWatch/BelowYellow","component_delta_explanation":"Cement ASP/input-cost/margin bridge is constructive but only moderate MFE; exact evidence needed before Yellow/Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L92_009410_TAEYOUNG_PF_WORKOUT_HARD_BREAK","trigger_id":"R10L92_C30_009410_20240103_STAGE2_4C_PF_WORKOUT_HARD_BREAK","symbol":"009410","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"PF workout / liquidity hard break should route to hard 4C even if local MFE appears","raw_component_scores_before":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":0,"materials_margin_score":0,"input_cost_pass_through":0,"cash_conversion":0,"relative_strength_score":5,"valuation_repricing_score":1,"execution_risk_score":-34,"theme_spike_risk":-24,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage1/4C-Watch","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":0,"materials_margin_score":0,"input_cost_pass_through":0,"cash_conversion":0,"relative_strength_score":0,"valuation_repricing_score":0,"execution_risk_score":-45,"theme_spike_risk":-28,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Hard-4C/DataQualityWatch","component_delta_explanation":"Credit-event volatility, trading halt/share-count discontinuity and missing PF repair bridge block all positive stages."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L92_034300_SHINSEGAE_CONSTRUCTION_CA_LATE_PRICE","trigger_id":"R10L92_C30_034300_20240118_STAGE2_FALSE_POSITIVE_LATE_PRICE_NONVALIDATION","symbol":"034300","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"late price after corporate-action/inactive-like context should not validate an original weak PF/backlog/cash entry","raw_component_scores_before":{"PF_exposure_repair":1,"liquidity_bridge":1,"financing_trust":1,"backlog_quality":1,"materials_margin_score":0,"input_cost_pass_through":0,"cash_conversion":0,"relative_strength_score":6,"valuation_repricing_score":3,"execution_risk_score":-16,"theme_spike_risk":-16,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"financing_trust":0,"backlog_quality":0,"materials_margin_score":0,"input_cost_pass_through":0,"cash_conversion":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-26,"theme_spike_risk":-20,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Corporate-action candidate and inactive-like end-state require data-quality repair; late price does not backfill original PF/backlog evidence."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R10L92_C30_P0_CURRENT","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C30 needs explicit PF/liquidity/backlog/materials-margin/cash bridge, hard 4C credit-event taxonomy and corporate-action late-price non-validation taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":16.77,"avg_MAE90_pct":-18.82,"avg_MFE180_pct":28.46,"avg_MAE180_pct":-18.82,"false_positive_rate":0.67,"hard_4C_count":1,"data_quality_watch_count":2,"late_price_not_validation_count":1,"score_return_alignment_verdict":"mixed_without_C30_PF_liquidity_hard_break_and_CA_late_price_guard"}
{"row_type":"profile_comparison","comparison_id":"R10L92_C30_P1_SECTOR_SPECIFIC","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P1_L9_PF_liquidity_materials_cash_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L9 construction signals need PF containment, liquidity trust, backlog quality, margin/cost pass-through or cash bridge before positive stage; PF workout routes to hard 4C","changed_axes":["PF_liquidity_required","materials_margin_cash_required","hard_4C_PF_workout_guard","CA_late_price_nonvalidation"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_PF_repair_liquidity_financing_backlog_margin_or_cash_proxy","hard_4C_gate":"PF_workout_or_liquidity_hard_break_or_trading_halt_watch"},"eligible_trigger_count":3,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R10L92_C30_P2_CANONICAL","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P2_C30_PF_liquidity_hard_break_and_CA_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C30 should reward balance-sheet/cash mechanics and hard-block PF workout/trading-halt credit events; late corporate-action price behavior cannot validate the original entry","changed_axes":["C30_PF_backlog_margin_cash_bridge_required","C30_PF_workout_liquidity_hard_4C_guard","C30_corporate_action_late_price_not_entry_validation_guard","C30_inactive_like_data_quality_guard"],"changed_thresholds":{"stage2_yellow_gate":"PF_or_liquidity_or_backlog_or_materials_margin_plus_cash_bridge_required","hard_4C_gate":"PF_workout_or_trading_halt_or_liquidity_break"},"eligible_trigger_count":3,"hard_4C_count":1,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R10L92_C30_P3_COUNTEREXAMPLE_GUARD","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P3_C30_high_MAE_or_data_quality_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If PF/backlog/cash bridge is missing, high MAE or corporate-action/data-quality watch blocks Yellow/Green; PF workout is 4C, not 4B","changed_axes":["C30_MAE_expansion_guardrail","C30_data_quality_4B_guardrail","C30_hard_4C_credit_event_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MAE90_le_minus20_or_CA_watch_or_inactive_like_watch); hard_4C_if_PF_workout_liquidity_break"},"eligible_trigger_count":3,"hard_4C_count":1,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_CEMENT_MARGIN_POSITIVE_WATCH_VS_PF_WORKOUT_CA_NONVALIDATION","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":1,"4C_case_count":1,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":2,"avg_MFE90_pct":16.77,"avg_MAE90_pct":-18.82,"avg_MFE180_pct":28.46,"avg_MAE180_pct":-18.82,"stage2_hit_rate_MFE90_ge15":0.67,"hard_4C_PF_workout_count":1,"late_price_not_entry_validation_count":1,"interpretation":"C30 needs bridge discipline. 아세아시멘트 shows cement/materials margin bridge can support only positive-watch, while 태영건설 is hard 4C PF/liquidity-break stress and 신세계건설 shows late corporate-action price behavior should not validate an original weak PF/backlog/cash entry."}
{"row_type":"stage_transition_summary","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"183190","trigger_type":"Stage2-Actionable-CementASPMaterialsMarginCashBridge-PositiveWatch","entry_date":"2024-01-29","stage2_to_90D_outcome":"positive_watch_moderate_MFE_low_MAE","stage2_to_180D_outcome":"cement_margin_bridge_but_Green_strict","MFE90_ge15":false,"MAE90_le_minus20":false,"transition_note":"Allow only positive-watch when materials strength is tied to ASP/input-cost/margin/cash bridge; moderate MFE blocks Green."}
{"row_type":"stage_transition_summary","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"009410","trigger_type":"Stage2-4C-Validated-PFWorkoutLiquidityHardBreakTradingHalt","entry_date":"2024-01-03","stage2_to_90D_outcome":"hard_4C_high_volatility_high_MAE","stage2_to_180D_outcome":"PF_workout_trading_halt_share_count_watch_not_bargain_rebound","MFE90_ge20":true,"MAE90_le_minus20":true,"transition_note":"PF workout/liquidity hard break routes to hard 4C/data-quality watch even if local MFE exists."}
{"row_type":"stage_transition_summary","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"034300","trigger_type":"Stage2-FalsePositive-ConstructionBalanceSheetRepairLatePriceNonValidation","entry_date":"2024-01-18","stage2_to_90D_outcome":"weak_original_entry_CA_watch","stage2_to_180D_outcome":"late_price_not_original_entry_validation","MFE180_ge20":true,"CA_watch":true,"transition_note":"Corporate-action/inactive-like late price behavior requires fresh trigger-date PF/backlog/cash evidence; do not retroactively validate original weak entry."}
{"row_type":"residual_contribution","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"PF_workout_hard_4C_and_corporate_action_late_price_nonvalidation","contribution":"Adds one C30 positive-watch, one hard 4C PF/workout stress row, and one CA/inactive-like late-price non-validation row, avoiding C30 top-covered and recent R10 loop symbols.","needs_coding_agent":true,"handoff_priority":"high"}
{"row_type":"coverage_matrix","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_MARGIN_CASH_POSITIVE_WATCH_VS_PF_WORKOUT_AND_CA_LATE_PRICE_NONVALIDATION","positive_case_count":1,"counterexample_count":2,"4B_case_count":1,"4C_case_count":1,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C30 now has non-top-symbol cement-margin positive-watch, PF workout hard 4C stress, and late corporate-action price non-validation stress; next R10 loops should exact-URL repair PF exposure, creditor/liquidity events, trading halt/share-count flags, backlog cash conversion, and materials ASP evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_PF_backlog_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"183190 only supports positive-watch when cement ASP/margin/cash proxy exists; 034300 shows construction repair vocabulary alone does not validate PF/backlog/cash."}
{"row_type":"shadow_weight","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_PF_workout_liquidity_hard_4C_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"hard_4C_guard","apply_now":false,"shadow_only":true,"evidence_basis":"009410 shows PF workout/liquidity hard break with trading discontinuity should route to hard 4C/data-quality watch, not positive or ordinary 4B."}
{"row_type":"shadow_weight","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_corporate_action_late_price_not_entry_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"034300 shows late price behavior after corporate-action/inactive-like context should not retroactively validate an original weak C30 entry."}
{"row_type":"shadow_weight","round":"R10","loop":"92","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_inactive_like_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"034300 has inactive-like profile status and a 2024 corporate-action candidate; production patching requires price-path/evidence repair."}
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
  - PF_workout_liquidity_hard_break_4C
  - trading_halt_share_count_change_data_quality_watch
  - corporate_action_late_price_not_entry_validation
  - inactive_like_data_quality_watch
  - moderate_MFE_Green_strict_watch
new_axis_proposed:
  - C30_PF_backlog_margin_cash_bridge_required_shadow_only
  - C30_PF_workout_liquidity_hard_4C_guard_shadow_only
  - C30_corporate_action_late_price_not_entry_validation_guard_shadow_only
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
`183190` has an older 2022 corporate-action candidate before the selected 2024 window; the selected 2024 window is usable.
`009410` has 2024 PF/workout/trading-halt/share-count style discontinuity, so it is hard 4C/data-quality stress only.
`034300` has a 2024-02-06 corporate-action candidate after the selected entry and inactive-like profile status, so it is data-quality watch before production patching.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for residual price-path analysis
evidence_url_pending = true
source_proxy_only = true
hard_4C_credit_event_watch = true for 009410
inactive_like_data_quality_watch = true for 034300
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
   - C30 previously top-covered/congested symbols
   - previous R10 loop83 symbols
   - previous R10 loop84 symbols
   - previous R10 loop85 symbols
   - previous R10 loop86 symbols
   - previous R10 loop87 symbols
   - previous R10 loop88 symbols
   - previous R10 loop89 symbols
   - previous R10 loop90 symbols
   - previous R10 loop91 symbols
6. Confirm stale R8/C28, R7/C25 and earlier-sector candidate rows are not ingested from this MD.
7. Keep 009410 as hard 4C/data-quality stress only.
8. Keep 034300 in corporate-action / inactive-like data-quality watch before patch consideration.
9. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C30-scoped safe patch candidates:
   - C30_PF_backlog_margin_cash_bridge_required
   - C30_PF_workout_liquidity_hard_4C_guard
   - C30_corporate_action_late_price_not_entry_validation_guard
   - C30_inactive_like_data_quality_guard
10. Do not loosen Stage3-Green.
11. Do not use future MFE/MAE in runtime scoring.
12. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R10
completed_loop = 92
next_round = R11
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive-watch, 1 4B/data-quality counterexample, and 1 hard 4C PF-workout stress row for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.
```
