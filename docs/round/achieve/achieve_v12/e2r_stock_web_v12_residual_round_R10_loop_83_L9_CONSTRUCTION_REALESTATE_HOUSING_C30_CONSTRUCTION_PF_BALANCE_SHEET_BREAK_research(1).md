# E2R Stock-Web v12 Residual Research — R10 Loop 83 / L9 / C30

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R10
loop: 83
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_LIQUIDITY_REPAIR_BRIDGE_VS_CONSTRUCTION_RELIEF_PRICE_SPIKE
sector: construction / real estate / housing / PF balance-sheet break
output_file: e2r_stock_web_v12_residual_round_R10_loop_83_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the sequential v12 scheduler after the completed `R9 loop 83` mobility result.

```text
scheduled_round = R10
scheduled_loop = 83
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

R10 is the construction/PF balance-sheet lane. It is not a live stock recommendation and it does not patch `stock_agent`. The single output is a standalone historical calibration Markdown file using `Songdaiki/stock-web` 1D tradable raw OHLC rows.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC. Corporate actions are not adjusted. Zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked from calibration by default."}
{"row_type":"price_source_validation","symbol":"014790","company_name":"HL D&I","profile_path":"atlas/symbol_profiles/014/014790.json","first_date":"1995-05-03","last_date":"2026-02-20","trading_day_count":7728,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1996-01-03","1997-11-03","1997-12-27","1999-12-21","2010-04-28","2012-02-06"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate windows are blocked by default; selected 2024-06-04 entry through 180D window has no candidate overlap.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_2025_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"047040","company_name":"대우건설","profile_path":"atlas/symbol_profiles/047/047040.json","first_date":"2001-03-23","last_date":"2026-02-20","trading_day_count":6127,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2001-07-13","2003-11-18","2011-01-18"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate windows are blocked by default; selected 2024-07-15 entry through 180D window has no candidate overlap.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_2025_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"005960","company_name":"동부건설","profile_path":"atlas/symbol_profiles/005/005960.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7653,"corporate_action_candidate_count":7,"corporate_action_candidate_dates":["1997-01-31","1999-06-16","2000-02-22","2012-09-10","2014-05-16","2015-09-04","2016-11-04"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate windows are blocked by default; selected 2024-04-25 entry through 180D window has no candidate overlap.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_2025_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger. The latest C30 coverage is already large, so this run deliberately avoids the most repeated C30 symbols (`002990`, `294870`, `375500`, `004960`, `013580`, `006360`) and adds a small-cap repair control plus two new PF/relief-rally counterexamples.

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novel keys introduced here:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"014790","trigger_type":"Stage2-Actionable-PF-LiquidityRepairBridge-Positive","entry_date":"2024-06-04","duplicate_status":"selected as C30 repair-bridge positive control; exact hard key not reused"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"047040","trigger_type":"Stage2-FalsePositive-PF-ReliefPriceSpike-NoBalanceSheetBridge","entry_date":"2024-07-15","duplicate_status":"selected as C30 relief-rally high-MAE counterexample; exact hard key not reused"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"005960","trigger_type":"Stage2-FalsePositive-ConstructionLowLiquidity-NoRepairBridge","entry_date":"2024-04-25","duplicate_status":"selected as C30 low-liquidity/PF-exposure counterexample; exact hard key not reused"}
```

## 4. Research question

C30 is not a generic construction rebound bucket. It should ask whether the PF bridge is load-bearing: liquidity, refinancing, guarantee exposure, capital support, cash conversion, and balance-sheet repair. A construction stock can jump on policy relief, short covering, or rate-cut beta, but if the bridge is only mist around the pillar, the path usually gives it back.

Residual question for this loop:

```text
Can the current calibrated profile distinguish:
1. a clean PF/liquidity repair bridge with shallow MAE,
2. a relief-rally squeeze that reaches a local peak and then rolls into high MAE,
3. a low-liquidity construction/PF exposure rebound without balance-sheet repair?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C30_R10L83_014790_HLDNI_PF_LIQUIDITY_REPAIR_BRIDGE","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_LIQUIDITY_REPAIR_BRIDGE_SHALLOW_MAE","symbol":"014790","company_name":"HL D&I","case_role":"structural_success","case_summary":"Selected as positive repair-bridge control: 2024-06 entry had shallow MAE and a tradable 30/90/180D upside path, suggesting C30 should allow Stage2/Yellow only when liquidity/PF repair evidence exists."}
{"row_type":"case","case_id":"C30_R10L83_047040_DAEWOO_PF_RELIEF_SPIKE_HIGH_MAE","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_RELIEF_PRICE_SPIKE_NO_BALANCE_SHEET_BRIDGE","symbol":"047040","company_name":"대우건설","case_role":"failed_rerating","case_summary":"Selected as relief-rally high-MAE counterexample: local spike to 2024-07-18 high quickly turned into 90/180D drawdown without clear balance-sheet repair bridge."}
{"row_type":"case","case_id":"C30_R10L83_005960_DONGBU_LOW_LIQUIDITY_NO_REPAIR_BRIDGE","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_LOW_LIQUIDITY_PF_EXPOSURE_NO_REPAIR_BRIDGE","symbol":"005960","company_name":"동부건설","case_role":"failed_rerating","case_summary":"Selected as low-liquidity construction/PF counterexample: early 2024 bounce had almost no upside and then slipped into a 180D drawdown, supporting a stronger C30 balance-sheet bridge requirement."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 014790 HL D&I — PF repair bridge positive control

Entry row checked from `atlas/ohlcv_tradable_by_symbol_year/014/014790/2024.csv`: `2024-06-04 c=2105`. 30D/90D peak was `2024-06-20 h=2660`. The 180D forward window remains clean; the lowest observed low through the usable 180D path was the entry-day low `2015`, with a later post-peak retracement to `2025-02-06 l=2070`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L83_C30_014790_20240604_STAGE2_PF_REPAIR_BRIDGE_POSITIVE","case_id":"C30_R10L83_014790_HLDNI_PF_LIQUIDITY_REPAIR_BRIDGE","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_LIQUIDITY_REPAIR_BRIDGE_SHALLOW_MAE","sector":"construction_realestate_housing","primary_archetype":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","loop_objective":"residual_missed_structural_mining;green_strictness_stress_test;canonical_archetype_rule_candidate","symbol":"014790","company_name":"HL D&I","trigger_type":"Stage2-Actionable-PF-LiquidityRepairBridge-Positive","trigger_date":"2024-06-04","evidence_available_at_that_date":"historical public liquidity/PF repair proxy; exact URL pending","evidence_source":"source-name-level proxy; exact disclosure/report URL pending; used only as non-price bridge proxy, not citation-grade evidence","stage2_evidence_fields":["public_event_or_disclosure_proxy","balance_sheet_repair_proxy","relative_strength"],"stage3_evidence_fields":["financial_visibility_proxy","repeat_conversion_pending"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014790/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/014/014790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-04","entry_price":2105.0,"MFE_30D_pct":26.37,"MFE_90D_pct":26.37,"MFE_180D_pct":26.37,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.28,"MAE_90D_pct":-4.28,"MAE_180D_pct":-4.28,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-06-20","peak_price":2660.0,"drawdown_after_peak_pct":-22.18,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_low_MAE_repair_bridge","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"C30_014790_20240604_2105","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 6.2 047040 대우건설 — relief-rally high-MAE counterexample

Entry row checked from `atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv`: `2024-07-15 c=4260`. The local peak arrived almost immediately at `2024-07-18 h=4965`, but the same 180D route later saw `2025-04-09 l=2940`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L83_C30_047040_20240715_STAGE2_FALSE_POSITIVE_PF_RELIEF_SPIKE","case_id":"C30_R10L83_047040_DAEWOO_PF_RELIEF_SPIKE_HIGH_MAE","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_RELIEF_PRICE_SPIKE_NO_BALANCE_SHEET_BRIDGE","sector":"construction_realestate_housing","primary_archetype":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","loop_objective":"residual_false_positive_mining;4B_non_price_requirement_stress_test;counterexample_mining","symbol":"047040","company_name":"대우건설","trigger_type":"Stage2-FalsePositive-PF-ReliefPriceSpike-NoBalanceSheetBridge","trigger_date":"2024-07-15","evidence_available_at_that_date":"historical public PF relief/rate-cycle proxy; exact URL pending","evidence_source":"source-name-level proxy; exact disclosure/report URL pending; price spike treated as insufficient without guarantee-exposure or liquidity repair bridge","stage2_evidence_fields":["relative_strength","public_event_or_disclosure_proxy"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-15","entry_price":4260.0,"MFE_30D_pct":16.55,"MFE_90D_pct":16.55,"MFE_180D_pct":16.55,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.78,"MAE_90D_pct":-20.77,"MAE_180D_pct":-30.99,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":4965.0,"drawdown_after_peak_pct":-40.79,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_local_spike_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"C30_047040_20240715_4260","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 6.3 005960 동부건설 — low-liquidity construction/PF exposure false positive

Entry row checked from `atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv`: `2024-04-25 c=5140`. The 30/90/180D path had almost no upside while the 180D usable route later reached `2025-01-15 l=3570`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L83_C30_005960_20240425_STAGE2_FALSE_POSITIVE_LOW_LIQUIDITY_NO_REPAIR","case_id":"C30_R10L83_005960_DONGBU_LOW_LIQUIDITY_NO_REPAIR_BRIDGE","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_LOW_LIQUIDITY_PF_EXPOSURE_NO_REPAIR_BRIDGE","sector":"construction_realestate_housing","primary_archetype":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","symbol":"005960","company_name":"동부건설","trigger_type":"Stage2-FalsePositive-ConstructionLowLiquidity-NoRepairBridge","trigger_date":"2024-04-25","evidence_available_at_that_date":"historical public construction/PF exposure proxy; exact URL pending","evidence_source":"source-name-level proxy; exact disclosure/report URL pending; construction rebound treated as insufficient until liquidity/guarantee repair is verified","stage2_evidence_fields":["public_event_or_disclosure_proxy","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","liquidity_overhang"],"stage4c_evidence_fields":["thesis_evidence_broken_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/005/005960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-25","entry_price":5140.0,"MFE_30D_pct":1.95,"MFE_90D_pct":1.95,"MFE_180D_pct":1.95,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.64,"MAE_90D_pct":-18.77,"MAE_180D_pct":-30.54,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-02","peak_price":5240.0,"drawdown_after_peak_pct":-31.87,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only","capital_raise_or_overhang"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"C30_005960_20240425_5140","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

## 7. Score simulation rows

Proxy scoring only. Production scoring is not changed.

```jsonl
{"row_type":"score_simulation","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"014790","profile":"P0b_current_e2r_2_2_rolling_calibrated_proxy","eps_fcf_explosion":14,"earnings_visibility":17,"bottleneck_pricing":7,"market_mispricing":13,"valuation_rerating":10,"capital_allocation":7,"information_confidence":5,"raw_total_proxy":73,"weighted_total_proxy":76,"simulated_stage":"Stage2-Actionable/Stage3-Yellow-Watch","simulation_note":"Positive path requires balance-sheet/PF repair bridge. URL-grade evidence still pending, so no Green loosening."}
{"row_type":"score_simulation","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"047040","profile":"P0b_current_e2r_2_2_rolling_calibrated_proxy","eps_fcf_explosion":10,"earnings_visibility":11,"bottleneck_pricing":4,"market_mispricing":15,"valuation_rerating":9,"capital_allocation":4,"information_confidence":4,"raw_total_proxy":57,"weighted_total_proxy":61,"simulated_stage":"Stage2-Watch/4B-risk","simulation_note":"Relief spike without repair bridge should be blocked from Yellow/Green; high-MAE path supports local guard."}
{"row_type":"score_simulation","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"005960","profile":"P0b_current_e2r_2_2_rolling_calibrated_proxy","eps_fcf_explosion":8,"earnings_visibility":9,"bottleneck_pricing":3,"market_mispricing":14,"valuation_rerating":8,"capital_allocation":3,"information_confidence":3,"raw_total_proxy":48,"weighted_total_proxy":54,"simulated_stage":"Stage2-FalsePositive-Watch","simulation_note":"Low-liquidity construction rebound without repair evidence had weak MFE and large 180D MAE."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R10L83_C30_P0_REFERENCE","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile":"P0_e2r_2_0_baseline","profile_role":"rollback_reference","expected_error":"Would over-credit construction relief beta and under-detect balance-sheet/PF bridge absence."}
{"row_type":"profile_comparison","comparison_id":"R10L83_C30_P0B_CURRENT","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile":"P0b_e2r_2_2_rolling_calibrated_proxy","profile_role":"current_default_proxy","expected_error":"Global price-only guard is directionally correct, but C30 needs a local distinction between repair bridge and PF-relief spike."}
{"row_type":"profile_comparison","comparison_id":"R10L83_C30_P1_REPAIR_BRIDGE_REQUIRED","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile":"P1_shadow_C30_balance_sheet_repair_bridge_required","profile_role":"shadow_candidate","expected_effect":"Stage2/Yellow requires liquidity/refinancing/guarantee-exposure repair bridge; construction beta alone remains Watch."}
{"row_type":"profile_comparison","comparison_id":"R10L83_C30_P2_HIGH_MAE_GUARD","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile":"P2_shadow_C30_high_MAE_guardrail","profile_role":"shadow_candidate","expected_effect":"If MFE90 is below 5 or MAE90 <= -15 without repair evidence, block Yellow/Green and route to local 4B/watch."}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_LIQUIDITY_REPAIR_BRIDGE_VS_RELIEF_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":14.96,"avg_MAE90_pct":-14.61,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_15":0.67,"interpretation":"C30 needs asymmetric bridge discipline: one repair-bridge path works, but two relief/no-repair paths show high-MAE or weak-MFE behavior."}
{"row_type":"stage_transition_summary","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"014790","trigger_type":"Stage2-Actionable-PF-LiquidityRepairBridge-Positive","entry_date":"2024-06-04","stage2_to_90D_outcome":"good_stage2","stage2_to_180D_outcome":"positive_repair_bridge_path","MFE90_ge_20":true,"MAE90_le_minus_15":false,"transition_note":"Allow Stage2/Yellow watch only when PF/liquidity repair bridge exists; no Green relaxation without exact evidence URL."}
{"row_type":"stage_transition_summary","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"047040","trigger_type":"Stage2-FalsePositive-PF-ReliefPriceSpike-NoBalanceSheetBridge","entry_date":"2024-07-15","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"4B_watch_or_counterexample","MFE90_ge_20":false,"MAE90_le_minus_15":true,"transition_note":"Local squeeze had tradable MFE but much larger downside; C30 should demand non-price repair evidence."}
{"row_type":"stage_transition_summary","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"005960","trigger_type":"Stage2-FalsePositive-ConstructionLowLiquidity-NoRepairBridge","entry_date":"2024-04-25","stage2_to_90D_outcome":"bad_stage2_low_MFE","stage2_to_180D_outcome":"4B_watch_or_counterexample","MFE90_ge_20":false,"MAE90_le_minus_15":true,"transition_note":"Low-liquidity rebound with no repair bridge produced almost no upside and a large 180D drawdown."}
{"row_type":"residual_contribution","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"C30_repair_bridge_vs_relief_spike","contribution":"Adds one shallow-MAE repair bridge positive and two high-MAE/low-MFE counterexamples, improving C30 balance-sheet bridge discipline without proposing a global rule.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_rows":3,"new_symbols":3,"new_positive":1,"new_counterexample":2,"new_4B_watch":2,"new_4C":0,"source_proxy_only":3,"evidence_url_pending":3,"calibration_usable":3,"next_gap":"Repair exact disclosure/report URLs and distinguish C30 liquidity repair from construction beta/relief spike before any promotion."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"stage2_required_bridge","scope":"canonical_archetype","candidate_delta":0.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"C30 Stage2/Yellow should require liquidity/refinancing/guarantee-exposure repair evidence; relief price spike alone is insufficient."}
{"row_type":"shadow_weight","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"local_4b_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Relief-rally and low-liquidity construction cases showed price-only local peaks and then high MAE; keep as Watch unless non-price repair evidence confirms."}
{"row_type":"shadow_weight","round":"R10","loop":"83","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"high_mae_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90 < 5 or MAE90 <= -15 without repair bridge, C30 should block Yellow/Green and require evidence-quality repair."}
```

Interpretation:

```text
C30 is a bridge inspection problem, not a rebound problem.
A price jump is only the traffic on the bridge.
The actual load-bearing structure is liquidity, refinancing, guarantee exposure, capital support, and cash conversion.
Without that structure, relief rallies should remain Watch / local 4B guard.
```

## 11. Data-quality caveat

All three cases use actual Stock-Web tradable raw OHLC rows and clean selected forward windows. The non-price evidence layer remains source-name/proxy level in this MD.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
promotion should prefer hold / data-quality repair until exact URLs are added
```

## 12. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not execute this handoff during the research-writing session.

When a later batch implementation is requested:
1. Ingest this MD through run-v12-calibration.
2. Confirm all trigger rows validate with price_data_source=Songdaiki/stock-web, price_basis=tradable_raw, price_adjustment_status=raw_unadjusted_marcap.
3. Check that C30 rows are representative and not hard duplicates by canonical_archetype_id + symbol + trigger_type + entry_date.
4. If aggregate support remains stable after exact evidence URL repair, consider C30-scoped safe patch candidates:
   - stage2_required_bridge for liquidity/refinancing/guarantee-exposure repair,
   - local_4b_watch_guard for construction relief rallies without repair evidence,
   - high_mae_guardrail when MFE90 < 5 or MAE90 <= -15 without repair bridge.
5. Do not loosen Stage3-Green. Do not use future MFE/MAE in runtime scoring. Use this only for calibration profile planning.
```

## 13. Round state

```text
completed_round = R10
completed_loop = 83
next_round = R11
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 14. Required final summary fields

```text
scheduled_round = R10
scheduled_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_trigger_family_count = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 2
diversity_score_summary = C30 top-covered symbols avoided; 014790, 047040, 005960 added as new symbols; repair-bridge positive versus relief/no-repair counterexamples separated.
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.
