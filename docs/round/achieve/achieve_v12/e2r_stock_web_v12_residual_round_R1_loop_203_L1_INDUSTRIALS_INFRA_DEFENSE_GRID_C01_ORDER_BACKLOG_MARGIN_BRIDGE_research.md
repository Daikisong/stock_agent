# E2R Stock-Web v12 Residual Research — R1 / L1 / C01 Engine Supplier Backlog-Margin-FCF Gate

```text
selected_round = R1
selected_loop = 203
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance reinforcement / C01 backlog-to-FCF counterexample repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id = C01_ENGINE_SUPPLIER_BACKLOG_MARGIN_FCF_GATE
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Execution Scope

This file follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical calibration handoff.  It does not patch `stock_agent`, does not run live discovery, and does not change production scoring.

The loop uses C01 because the current No-Repeat ledger shows all C01~C32 archetypes already above the 80-row stability zone, making the next useful work a Priority 1 quality pass.  For C01 the current ledger points specifically to backlog that fails to convert into FCF/margin.  This loop therefore adds three supplier-style symbols that were not used in the recent visible C01 rows: HD Hyundai Marine Engine, Hanwha Engine, and SK Oceanplant.

This loop adds 6 new independent cases, 2 counterexamples, and 5 residual errors for R1/L1/C01.

## 2. Price Source Validation

```json
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Stock-Web manifest fields used here:

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| calibration_shard_root | `atlas/ohlcv_tradable_by_symbol_year` |
| schema | `d,o,h,l,c,v,a,mc,s,m` |

MFE/MAE formula used:

```text
MFE_N_pct = (max high from entry_date through N tradable sessions / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable sessions / entry_price - 1) * 100
peak_price = max high over 180D window
drawdown_after_peak_pct = min low after peak / peak_price - 1
```

## 3. Coverage / Novelty Check

| check | value |
|---|---:|
| calibration_usable_case_count | 6 |
| calibration_usable_trigger_count | 6 |
| new_independent_case_count | 6 |
| reused_case_count | 0 |
| new_symbol_count | 3 |
| same_archetype_new_symbol_count | 3 |
| same_archetype_new_trigger_family_count | 4 |
| positive_case_count | 4 |
| counterexample_count | 2 |
| current_profile_error_count | 5 |
| new_independent_case_ratio | 1.00 |
| source_proxy_only_count | 0 |
| evidence_url_pending_count | 0 |
| missing_required_mfe_mae_count | 0 |
| corporate_action_contaminated_180D_count | 0 |
| insufficient_forward_window_180D_count | 0 |

Diversity note: this is still the same canonical C01, but the case body shifts away from prime-yard shipbuilders and into engine/offshore-wind suppliers.  That is the point of the loop: C01 should not overfit only to yard-level backlog; it also needs supplier-level order-to-sales, margin, and cash-conversion gates.

## 4. Entry OHLC Rows

| symbol | entry_date | o | h | l | c | volume | shard | CA window |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 071970 | 2025-03-10 | 27200 | 30850 | 26900 | 29750 | 9804881 | `atlas/ohlcv_tradable_by_symbol_year/071/071970/2025.csv` | clean_no_candidate_overlap_180D_window |
| 071970 | 2025-04-24 | 33800 | 35900 | 33300 | 34700 | 1036676 | `atlas/ohlcv_tradable_by_symbol_year/071/071970/2025.csv` | clean_no_candidate_overlap_180D_window |
| 082740 | 2024-07-17 | 15300 | 15890 | 15170 | 15500 | 3777286 | `atlas/ohlcv_tradable_by_symbol_year/082/082740/2024.csv` | clean_no_candidate_overlap_180D_window |
| 082740 | 2025-05-21 | 28500 | 29700 | 28500 | 29150 | 883720 | `atlas/ohlcv_tradable_by_symbol_year/082/082740/2025.csv` | clean_no_candidate_overlap_180D_window |
| 100090 | 2024-06-27 | 14400 | 14750 | 14120 | 14210 | 407139 | `atlas/ohlcv_tradable_by_symbol_year/100/100090/2024.csv` | clean_no_candidate_overlap_180D_window |
| 100090 | 2024-08-16 | 14060 | 14640 | 13630 | 14440 | 693973 | `atlas/ohlcv_tradable_by_symbol_year/100/100090/2024.csv` | clean_no_candidate_overlap_180D_window |


## 5. Trigger-Level Backtest Table

| case_id | symbol | company | trigger | entry | entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak/date | max DD after peak | role | verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---|---:|---|---|
| C01_203_01_071970_SALES_DOUBLE_FORECAST | 071970 | HD Hyundai Marine Engine | Stage2-Actionable | 2025-03-10 | 29750 | 17.65/-17.65 | 90.92/-17.65 | 258.32/-17.65 | 106600 / 2025-11-03 | -30.96 | structural_success | current_profile_missed_structural_if_engine_supplier_bucket_ignored |
| C01_203_02_071970_Q1_ACTUAL_PROFIT_BRIDGE | 071970 | HD Hyundai Marine Engine | Stage3-Yellow | 2025-04-24 | 34700 | 30.12/-4.03 | 177.23/-4.03 | 207.2/-4.03 | 106600 / 2025-11-03 | -30.96 | structural_success | current_profile_too_late_if_actual_profit_bridge_not_promoted_to_yellow |
| C01_203_03_082740_Q2_EXPECTED_EARNINGS_DELIVERY_SCHEDULE | 082740 | Hanwha Engine | Stage2 | 2024-07-17 | 15500 | 10.71/-29.03 | 18.32/-29.03 | 85.48/-29.03 | 28750 / 2025-02-14 | -30.43 | high_mae_success | current_profile_correct_stage2_but_green_blocked_by_initial_mae |
| C01_203_04_082740_Q1_2025_ORDER_BACKLOG_MARGIN | 082740 | Hanwha Engine | Stage2-Actionable | 2025-05-21 | 29150 | 10.98/-9.95 | 66.72/-15.44 | 105.49/-15.44 | 59900 / 2026-02-04 | -13.86 | structural_success | current_profile_missed_structural_if_new_orders_and_margin_delivery_underweighted |
| C01_203_05_100090_OFFSHORE_WIND_FACILITY_LONG_LEAD | 100090 | SK Oceanplant | Stage2 | 2024-06-27 | 14210 | 3.8/-27.52 | 14/-27.52 | 14/-27.52 | 16200 / 2024-09-24 | -31.42 | failed_rerating | current_profile_false_positive_if_capacity_capex_treated_like_backlog_margin |
| C01_203_06_100090_ORDER_DELAY_GUIDANCE_CUT_OFFSET | 100090 | SK Oceanplant | Stage4B | 2024-08-16 | 14440 | 12.19/-7.55 | 12.19/-23.06 | 53.39/-23.06 | 22150 / 2025-05-19 | -10.07 | 4B_overlay_success | current_profile_overhard_4c_risk_if_guidance_cut_ignores_offset_quality |


## 6. Case Notes

### 6.1 HD Hyundai Marine Engine — sales double / margin conversion

The 2025-03-10 row is a positive C01 supplier row.  The evidence was no longer only a shipbuilding-cycle headline; it had engine volume, sales-doubling expectation, and operating-margin bridge.  Stock-Web confirms the bridge was not late: the 180D path from the entry close of 29,750 reached 106,600 high, with +258.32% MFE and -17.65% MAE.

The 2025-04-24 row is the higher-confirmation Yellow row.  The follow-up evidence connected the earlier setup to actual Q1 profit.  Because cash-flow and working-capital conversion were still not multi-source confirmed, the proposed shadow handling is Stage3-Yellow, not Stage3-Green.

### 6.2 Hanwha Engine — high-MAE early setup vs direct delivery/order bridge

The 2024-07-17 row shows why early supplier Stage2 can be correct even when MAE is high.  The delivery-schedule and dual-fuel-engine mix setup eventually produced +85.48% 180D MFE, but the entry first suffered -29.03% MAE.  This argues for Stage2 with a Green cap, not immediate rejection.

The 2025-05-21 row is stronger: public Q1 results gave sales, operating profit, OPM, new orders, backlog growth, and positive-margin projects entering delivery.  This is exactly the missing C01 second bridge: backlog -> delivery -> margin.

### 6.3 SK Oceanplant — long-lead capacity and order-delay watch

The 2024-06-27 investment row is the negative control.  A KRW1.12tn offshore-wind facility is strategic capacity, but the completion target was December 2026.  The 180D forward path showed only +14.00% MFE with -27.52% MAE, so the current profile should not treat long-lead capacity capex like a live backlog-margin bridge.

The 2024-08-16 row is a Stage4B watch, not hard 4C.  Sales guidance was cut and offshore-wind order timing was delayed, but the article also included high-margin change orders, a KRW465.7bn quarterly order number, KRW524bn backlog, and specialty-vessel sales recognition.  The 180D path later reached +53.39% MFE, so hard 4C would have been too harsh without an order-cancellation or cash-conversion break.

## 7. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| Would current `stage2_actionable_evidence_bonus` help? | Yes for 071970 and 082740 when supplier-level order/delivery/margin evidence is direct. |
| Where does it overfire? | 100090 2024-06-27 if long-lead facility capex is treated as backlog-to-margin conversion. |
| Is Yellow threshold 75 too strict? | Not for 071970 2025-04-24; actual profit bridge clears Yellow.  It remains appropriate for 082740 2024-07-17 because high MAE and forecast-only evidence should cap confirmation. |
| Is Green threshold 87 / revision 55 too strict? | Kept.  Engine supplier rows had huge MFE, but working-capital/FCF was not sufficiently multi-source at trigger date. |
| Was price-only blowoff guard relevant? | Kept.  All selected rows use non-price evidence; no price-only row is promoted. |
| Was full 4B non-price requirement relevant? | Strengthened.  SK Oceanplant 2024-08-16 had non-price delay/guidance-cut evidence, so Stage4B was valid. |
| Was hard 4C routing too harsh? | Yes if guidance cut or long-lead capex is treated as thesis break without order/cashflow failure. |

## 8. Shadow Rule Candidate

```text
canonical_rule_candidate = C01_SUPPLIER_ORDER_TO_MARGIN_AND_CASHFLOW_GATE
sector_rule_candidate = L1_ENGINE_SUPPLIER_BACKLOG_MARGIN_FCF_GATE
existing_axis_tested = stage2_required_bridge, stage2_actionable_evidence_bonus, stage3_yellow_total_min, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
existing_axis_strengthened = stage2_required_bridge, high_mae_green_cap
existing_axis_kept = stage3_green_strictness, hard_4c_requires_non_price_thesis_break
new_axis_proposed = false
```

Proposed C01-specific handling:

```text
1. Yard-level or supplier-level backlog/order headline alone may reach Stage2, but not Stage2-Actionable.
2. Stage2-Actionable requires at least one second bridge:
   - delivery schedule entering revenue,
   - positive-margin post-2022 order delivery,
   - engine/component volume route,
   - customer/order quality with margin evidence,
   - actual operating-profit conversion.
3. Stage3-Yellow requires actual profit bridge plus order/delivery visibility.
4. Stage3-Green remains blocked until FCF / working-capital / cash conversion is confirmed by multiple evidence families.
5. Long-lead facility capex without near-term shipment or cash conversion is capped at Stage2 or Stage4B-watch.
6. Guidance cuts or order delays become hard 4C only if order cancellation, backlog collapse, margin thesis break, or cash-conversion failure is confirmed.
```

## 9. Machine-Readable JSONL Rows

```jsonl
{"calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "manifest_max_date": "2026-02-20", "manifest_path": "atlas/manifest.json", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "row_type": "price_source_validation", "schema_path": "atlas/schema.json", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "universe_path": "atlas/universe/all_symbols.csv", "validation_status": "usable_for_historical_calibration"}
{"MAE_180D_pct": -17.65, "MAE_1Y_pct": null, "MAE_30D_pct": -17.65, "MAE_90D_pct": -17.65, "MFE_180D_pct": 258.32, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 17.65, "MFE_90D_pct": 90.92, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_203_01_071970_SALES_DOUBLE_FORECAST", "case_role": "structural_success", "company_name": "HD Hyundai Marine Engine", "component_delta_explanation": "C01 supplier rows require an order/backlog-to-margin/cash second bridge; long-lead capacity capex and guidance cuts are capped at Stage2/Stage4B unless order collapse, margin thesis break, or cash conversion failure is confirmed.", "corporate_action_window_status": "clean_no_candidate_overlap_180D_window", "current_profile_verdict": "current_profile_missed_structural_if_engine_supplier_bucket_ignored", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -30.96, "entry_date": "2025-03-10", "entry_high": 30850.0, "entry_low": 26900.0, "entry_open": 27200.0, "entry_price": 29750.0, "entry_volume": 9804881.0, "evidence_available_at_that_date": "same_day_or_next_tradable_close_per_timestamp_conservatism", "evidence_family": "marine_engine_sales_double_margin_above_10pct", "evidence_source": "https://www.hd-marineengine.com/page.do?BOARD_ID=3571&MENU_ID=U05-01-VW", "evidence_summary": "Company PR center / market coverage noted sales-doubling expectations and operating margin above 10%; this is a direct second-bridge row because backlog/order conversion was already translating into margin.", "fine_archetype_id": "C01_ENGINE_SUPPLIER_BACKLOG_MARGIN_FCF_GATE", "forward_window_last_date": "2025-12-01", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": "case_specific", "four_b_local_peak_proximity": "case_specific", "four_b_timing_verdict": "Stage4B used only when non-price delay/guidance evidence exists", "four_c_protection_label": "hard_4c_blocked_unless_order_or_cashflow_thesis_break_confirmed", "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 203, "loop_objective": ["residual_false_positive_mining", "stage2_actionable_bonus_stress_test", "sector_specific_rule_discovery", "counterexample_mining"], "peak_date": "2025-11-03", "peak_price": 106600.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/071/071970/2025.csv", "price_source": "Songdaiki/stock-web", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/071/071970.json", "raw_component_scores_after": {"bottleneck_pricing": 14, "capital_allocation": 3, "cash_conversion_quality": 8, "earnings_visibility": 15, "eps_fcf_explosion": 13, "execution_risk": -2, "high_mae_green_cap": 0, "information_confidence": 8, "margin_bridge_quality": 12, "market_mispricing": 8, "valuation_rerating": 8}, "raw_component_scores_before": {"bottleneck_pricing": 13, "capital_allocation": 3, "cash_conversion_quality": 7, "earnings_visibility": 14, "eps_fcf_explosion": 12, "execution_risk": -1, "information_confidence": 8, "margin_bridge_quality": 10, "market_mispricing": 9, "valuation_rerating": 9}, "research_file": "e2r_stock_web_v12_residual_round_R1_loop_203_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "reuse_reason": "same canonical allowed; symbol/trigger/date/evidence family not used in recent visible C01/C05/C13/C10 loops", "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_203::071970::Stage2-Actionable::2025-03-10", "schema_version": "e2r_stock_web_v12_residual.v1", "sector": "industrials_infra_defense_grid", "shares_change_pct_180D": 0.0, "stage2_evidence_fields": ["order_to_sales_conversion", "engine_volume_route", "margin_bridge"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stage_label_after": "Stage2-Actionable", "stage_label_before": "Stage2-Actionable", "stock_web_manifest_max_date": "2026-02-20", "symbol": "071970", "trigger_date": "2025-03-10", "trigger_id": "R1L203_C01_T01_071970_2025-03-10", "trigger_outcome_label": "true_stage2_actionable_engine_backlog_to_margin_bridge", "trigger_type": "Stage2-Actionable", "weighted_score_after": 78, "weighted_score_before": 72}
{"MAE_180D_pct": -4.03, "MAE_1Y_pct": null, "MAE_30D_pct": -4.03, "MAE_90D_pct": -4.03, "MFE_180D_pct": 207.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 30.12, "MFE_90D_pct": 177.23, "aggregate_group_role": "representative", "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_203_02_071970_Q1_ACTUAL_PROFIT_BRIDGE", "case_role": "structural_success", "company_name": "HD Hyundai Marine Engine", "component_delta_explanation": "C01 supplier rows require an order/backlog-to-margin/cash second bridge; long-lead capacity capex and guidance cuts are capped at Stage2/Stage4B unless order collapse, margin thesis break, or cash conversion failure is confirmed.", "corporate_action_window_status": "clean_no_candidate_overlap_180D_window", "current_profile_verdict": "current_profile_too_late_if_actual_profit_bridge_not_promoted_to_yellow", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -30.96, "entry_date": "2025-04-24", "entry_high": 35900.0, "entry_low": 33300.0, "entry_open": 33800.0, "entry_price": 34700.0, "entry_volume": 1036676.0, "evidence_available_at_that_date": "same_day_or_next_tradable_close_per_timestamp_conservatism", "evidence_family": "q1_actual_profit_conversion_after_sales_double_setup", "evidence_source": "https://biz.chosun.com/en/en-industry/2025/04/24/Z3JZ2H5ZOFGZDJ5XYHJI4ZIGYI/", "evidence_summary": "HD Korea Shipbuilding Q1 coverage cited HD Hyundai Marine Engine operating profit growth to KRW10.3bn, giving an actual profit bridge after the earlier order/sales rerating.", "fine_archetype_id": "C01_ENGINE_SUPPLIER_BACKLOG_MARGIN_FCF_GATE", "forward_window_last_date": "2026-01-20", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": "case_specific", "four_b_local_peak_proximity": "case_specific", "four_b_timing_verdict": "Stage4B used only when non-price delay/guidance evidence exists", "four_c_protection_label": "hard_4c_blocked_unless_order_or_cashflow_thesis_break_confirmed", "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 203, "loop_objective": ["residual_false_positive_mining", "stage2_actionable_bonus_stress_test", "sector_specific_rule_discovery", "counterexample_mining"], "peak_date": "2025-11-03", "peak_price": 106600.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/071/071970/2025.csv", "price_source": "Songdaiki/stock-web", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/071/071970.json", "raw_component_scores_after": {"bottleneck_pricing": 14, "capital_allocation": 3, "cash_conversion_quality": 8, "earnings_visibility": 15, "eps_fcf_explosion": 13, "execution_risk": -2, "high_mae_green_cap": 0, "information_confidence": 8, "margin_bridge_quality": 12, "market_mispricing": 8, "valuation_rerating": 8}, "raw_component_scores_before": {"bottleneck_pricing": 13, "capital_allocation": 3, "cash_conversion_quality": 7, "earnings_visibility": 14, "eps_fcf_explosion": 12, "execution_risk": -1, "information_confidence": 8, "margin_bridge_quality": 10, "market_mispricing": 9, "valuation_rerating": 9}, "research_file": "e2r_stock_web_v12_residual_round_R1_loop_203_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "reuse_reason": "same canonical allowed; symbol/trigger/date/evidence family not used in recent visible C01/C05/C13/C10 loops", "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_203::071970::Stage3-Yellow::2025-04-24", "schema_version": "e2r_stock_web_v12_residual.v1", "sector": "industrials_infra_defense_grid", "shares_change_pct_180D": 0.0, "stage2_evidence_fields": ["order_to_sales_conversion", "engine_volume_route"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stage_label_after": "Stage3-Yellow", "stage_label_before": "Stage3-Yellow", "stock_web_manifest_max_date": "2026-02-20", "symbol": "071970", "trigger_date": "2025-04-24", "trigger_id": "R1L203_C01_T02_071970_2025-04-24", "trigger_outcome_label": "yellow_confirmed_profit_bridge_not_green_until_cashflow_multi_source", "trigger_type": "Stage3-Yellow", "weighted_score_after": 82, "weighted_score_before": 76}
{"MAE_180D_pct": -29.03, "MAE_1Y_pct": null, "MAE_30D_pct": -29.03, "MAE_90D_pct": -29.03, "MFE_180D_pct": 85.48, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 10.71, "MFE_90D_pct": 18.32, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_203_03_082740_Q2_EXPECTED_EARNINGS_DELIVERY_SCHEDULE", "case_role": "high_mae_success", "company_name": "Hanwha Engine", "component_delta_explanation": "C01 supplier rows require an order/backlog-to-margin/cash second bridge; long-lead capacity capex and guidance cuts are capped at Stage2/Stage4B unless order collapse, margin thesis break, or cash conversion failure is confirmed.", "corporate_action_window_status": "clean_no_candidate_overlap_180D_window", "current_profile_verdict": "current_profile_correct_stage2_but_green_blocked_by_initial_mae", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -30.43, "entry_date": "2024-07-17", "entry_high": 15890.0, "entry_low": 15170.0, "entry_open": 15300.0, "entry_price": 15500.0, "entry_volume": 3777286.0, "evidence_available_at_that_date": "same_day_or_next_tradable_close_per_timestamp_conservatism", "evidence_family": "analyst_delivery_schedule_df_engine_mix_forecast", "evidence_source": "https://onereport.co.kr/53/?bmode=view&idx=44645271", "evidence_summary": "Korea Investment & Securities expected Q2 standalone operating profit to beat consensus by 41%, citing engine deliveries, dual-fuel engine mix, client delivery schedule reassessment, and added Chinese ship-engine volumes.", "fine_archetype_id": "C01_ENGINE_SUPPLIER_BACKLOG_MARGIN_FCF_GATE", "forward_window_last_date": "2025-04-15", "forward_window_trading_days": 180, "four_b_evidence_type": ["high_mae_entry_risk"], "four_b_full_window_peak_proximity": "case_specific", "four_b_local_peak_proximity": "case_specific", "four_b_timing_verdict": "Stage4B used only when non-price delay/guidance evidence exists", "four_c_protection_label": "hard_4c_blocked_unless_order_or_cashflow_thesis_break_confirmed", "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 203, "loop_objective": ["residual_false_positive_mining", "stage2_actionable_bonus_stress_test", "sector_specific_rule_discovery", "counterexample_mining"], "peak_date": "2025-02-14", "peak_price": 28750.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/082/082740/2024.csv", "price_source": "Songdaiki/stock-web", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/082/082740.json", "raw_component_scores_after": {"bottleneck_pricing": 14, "capital_allocation": 3, "cash_conversion_quality": 8, "earnings_visibility": 15, "eps_fcf_explosion": 13, "execution_risk": -2, "high_mae_green_cap": -3, "information_confidence": 8, "margin_bridge_quality": 12, "market_mispricing": 8, "valuation_rerating": 8}, "raw_component_scores_before": {"bottleneck_pricing": 13, "capital_allocation": 3, "cash_conversion_quality": 7, "earnings_visibility": 14, "eps_fcf_explosion": 12, "execution_risk": -1, "information_confidence": 8, "margin_bridge_quality": 10, "market_mispricing": 9, "valuation_rerating": 9}, "research_file": "e2r_stock_web_v12_residual_round_R1_loop_203_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "reuse_reason": "same canonical allowed; symbol/trigger/date/evidence family not used in recent visible C01/C05/C13/C10 loops", "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_203::082740::Stage2::2024-07-17", "schema_version": "e2r_stock_web_v12_residual.v1", "sector": "industrials_infra_defense_grid", "shares_change_pct_180D": 0.0, "stage2_evidence_fields": ["capacity_or_volume_route", "early_revision_signal", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["high_mae_entry_risk"], "stage4c_evidence_fields": [], "stage_label_after": "Stage2", "stage_label_before": "Stage2", "stock_web_manifest_max_date": "2026-02-20", "symbol": "082740", "trigger_date": "2024-07-17", "trigger_id": "R1L203_C01_T03_082740_2024-07-17", "trigger_outcome_label": "early_stage2_high_mae_engine_delivery_schedule_success", "trigger_type": "Stage2", "weighted_score_after": 67, "weighted_score_before": 65}
{"MAE_180D_pct": -15.44, "MAE_1Y_pct": null, "MAE_30D_pct": -9.95, "MAE_90D_pct": -15.44, "MFE_180D_pct": 105.49, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 10.98, "MFE_90D_pct": 66.72, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_203_04_082740_Q1_2025_ORDER_BACKLOG_MARGIN", "case_role": "structural_success", "company_name": "Hanwha Engine", "component_delta_explanation": "C01 supplier rows require an order/backlog-to-margin/cash second bridge; long-lead capacity capex and guidance cuts are capped at Stage2/Stage4B unless order collapse, margin thesis break, or cash conversion failure is confirmed.", "corporate_action_window_status": "clean_no_candidate_overlap_180D_window", "current_profile_verdict": "current_profile_missed_structural_if_new_orders_and_margin_delivery_underweighted", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -13.86, "entry_date": "2025-05-21", "entry_high": 29700.0, "entry_low": 28500.0, "entry_open": 28500.0, "entry_price": 29150.0, "entry_volume": 883720.0, "evidence_available_at_that_date": "same_day_or_next_tradable_close_per_timestamp_conservatism", "evidence_family": "q1_sales_op_new_orders_backlog_positive_margin_delivery", "evidence_source": "https://www.marketscreener.com/quote/stock/HANWHA-ENGINE-CO-LTD-10053425/news/Hanwha-Engine-performance-in-Q1-2025--50020981/", "evidence_summary": "Hanwha Engine 1Q25 disclosure showed sales KRW318.2bn, operating profit KRW22.3bn, 7% OPM, KRW834.2bn new orders, China/container order-driven backlog growth, and post-2022 positive-margin projects entering delivery.", "fine_archetype_id": "C01_ENGINE_SUPPLIER_BACKLOG_MARGIN_FCF_GATE", "forward_window_last_date": "2026-02-11", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": "case_specific", "four_b_local_peak_proximity": "case_specific", "four_b_timing_verdict": "Stage4B used only when non-price delay/guidance evidence exists", "four_c_protection_label": "hard_4c_blocked_unless_order_or_cashflow_thesis_break_confirmed", "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 203, "loop_objective": ["residual_false_positive_mining", "stage2_actionable_bonus_stress_test", "sector_specific_rule_discovery", "counterexample_mining"], "peak_date": "2026-02-04", "peak_price": 59900.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/082/082740/2025.csv", "price_source": "Songdaiki/stock-web", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/082/082740.json", "raw_component_scores_after": {"bottleneck_pricing": 14, "capital_allocation": 3, "cash_conversion_quality": 8, "earnings_visibility": 15, "eps_fcf_explosion": 13, "execution_risk": -2, "high_mae_green_cap": 0, "information_confidence": 8, "margin_bridge_quality": 12, "market_mispricing": 8, "valuation_rerating": 8}, "raw_component_scores_before": {"bottleneck_pricing": 13, "capital_allocation": 3, "cash_conversion_quality": 7, "earnings_visibility": 14, "eps_fcf_explosion": 12, "execution_risk": -1, "information_confidence": 8, "margin_bridge_quality": 10, "market_mispricing": 9, "valuation_rerating": 9}, "research_file": "e2r_stock_web_v12_residual_round_R1_loop_203_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "reuse_reason": "same canonical allowed; symbol/trigger/date/evidence family not used in recent visible C01/C05/C13/C10 loops", "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_203::082740::Stage2-Actionable::2025-05-21", "schema_version": "e2r_stock_web_v12_residual.v1", "sector": "industrials_infra_defense_grid", "shares_change_pct_180D": 0.0, "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stage_label_after": "Stage2-Actionable", "stage_label_before": "Stage2-Actionable", "stock_web_manifest_max_date": "2026-02-20", "symbol": "082740", "trigger_date": "2025-05-21", "trigger_id": "R1L203_C01_T04_082740_2025-05-21", "trigger_outcome_label": "stage2_actionable_order_backlog_margin_delivery_bridge", "trigger_type": "Stage2-Actionable", "weighted_score_after": 80, "weighted_score_before": 74}
{"MAE_180D_pct": -27.52, "MAE_1Y_pct": null, "MAE_30D_pct": -27.52, "MAE_90D_pct": -27.52, "MFE_180D_pct": 14.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 3.8, "MFE_90D_pct": 14.0, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_203_05_100090_OFFSHORE_WIND_FACILITY_LONG_LEAD", "case_role": "failed_rerating", "company_name": "SK Oceanplant", "component_delta_explanation": "C01 supplier rows require an order/backlog-to-margin/cash second bridge; long-lead capacity capex and guidance cuts are capped at Stage2/Stage4B unless order collapse, margin thesis break, or cash conversion failure is confirmed.", "corporate_action_window_status": "clean_no_candidate_overlap_180D_window", "current_profile_verdict": "current_profile_false_positive_if_capacity_capex_treated_like_backlog_margin", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -31.42, "entry_date": "2024-06-27", "entry_high": 14750.0, "entry_low": 14120.0, "entry_open": 14400.0, "entry_price": 14210.0, "entry_volume": 407139.0, "evidence_available_at_that_date": "same_day_or_next_tradable_close_per_timestamp_conservatism", "evidence_family": "long_lead_offshore_wind_facility_capex_without_near_term_fcf", "evidence_source": "https://www.investkorea.org/ik-en/bbs/i-465/detail.do?ntt_sn=492595", "evidence_summary": "SK Oceanplant announced a KRW1.12tn offshore-wind substructure facility investment with completion targeted for December 2026; this was strategic capacity, not a near-term margin/FCF bridge.", "fine_archetype_id": "C01_ENGINE_SUPPLIER_BACKLOG_MARGIN_FCF_GATE", "forward_window_last_date": "2025-03-26", "forward_window_trading_days": 180, "four_b_evidence_type": ["capital_raise_or_overhang", "contract_delay"], "four_b_full_window_peak_proximity": "case_specific", "four_b_local_peak_proximity": "case_specific", "four_b_timing_verdict": "Stage4B used only when non-price delay/guidance evidence exists", "four_c_protection_label": "hard_4c_blocked_unless_order_or_cashflow_thesis_break_confirmed", "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 203, "loop_objective": ["residual_false_positive_mining", "stage2_actionable_bonus_stress_test", "sector_specific_rule_discovery", "counterexample_mining"], "peak_date": "2024-09-24", "peak_price": 16200.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100090/2024.csv", "price_source": "Songdaiki/stock-web", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/100/100090.json", "raw_component_scores_after": {"bottleneck_pricing": 14, "capital_allocation": 3, "cash_conversion_quality": 1, "earnings_visibility": 15, "eps_fcf_explosion": 13, "execution_risk": -7, "high_mae_green_cap": -3, "information_confidence": 8, "margin_bridge_quality": 2, "market_mispricing": 8, "valuation_rerating": 8}, "raw_component_scores_before": {"bottleneck_pricing": 13, "capital_allocation": 3, "cash_conversion_quality": 2, "earnings_visibility": 14, "eps_fcf_explosion": 12, "execution_risk": -4, "information_confidence": 8, "margin_bridge_quality": 3, "market_mispricing": 9, "valuation_rerating": 9}, "research_file": "e2r_stock_web_v12_residual_round_R1_loop_203_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "reuse_reason": "same canonical allowed; symbol/trigger/date/evidence family not used in recent visible C01/C05/C13/C10 loops", "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_203::100090::Stage2::2024-06-27", "schema_version": "e2r_stock_web_v12_residual.v1", "sector": "industrials_infra_defense_grid", "shares_change_pct_180D": 0.0, "stage2_evidence_fields": ["capacity_or_volume_route", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["capital_raise_or_overhang", "contract_delay"], "stage4c_evidence_fields": [], "stage_label_after": "Stage2_capped", "stage_label_before": "Stage2", "stock_web_manifest_max_date": "2026-02-20", "symbol": "100090", "trigger_date": "2024-06-27", "trigger_id": "R1L203_C01_T05_100090_2024-06-27", "trigger_outcome_label": "stage2_false_positive_long_lead_capacity_without_cash_conversion", "trigger_type": "Stage2", "weighted_score_after": 56, "weighted_score_before": 66}
{"MAE_180D_pct": -23.06, "MAE_1Y_pct": null, "MAE_30D_pct": -7.55, "MAE_90D_pct": -23.06, "MFE_180D_pct": 53.39, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 12.19, "MFE_90D_pct": 12.19, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_203_06_100090_ORDER_DELAY_GUIDANCE_CUT_OFFSET", "case_role": "4B_overlay_success", "company_name": "SK Oceanplant", "component_delta_explanation": "C01 supplier rows require an order/backlog-to-margin/cash second bridge; long-lead capacity capex and guidance cuts are capped at Stage2/Stage4B unless order collapse, margin thesis break, or cash conversion failure is confirmed.", "corporate_action_window_status": "clean_no_candidate_overlap_180D_window", "current_profile_verdict": "current_profile_overhard_4c_risk_if_guidance_cut_ignores_offset_quality", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -10.07, "entry_date": "2024-08-16", "entry_high": 14640.0, "entry_low": 13630.0, "entry_open": 14060.0, "entry_price": 14440.0, "entry_volume": 693973.0, "evidence_available_at_that_date": "same_day_or_next_tradable_close_per_timestamp_conservatism", "evidence_family": "order_delay_guidance_cut_but_backlog_specialty_ship_offset", "evidence_source": "https://www.asiae.co.kr/en/article/2024081608001956333", "evidence_summary": "Q2 sales missed consensus; offshore-wind substructure orders were postponed; 2024 sales guidance was cut 10-15%, but high-margin change orders, KRW465.7bn Q2 new orders, KRW524bn backlog, and specialty-vessel sales provided offset.", "fine_archetype_id": "C01_ENGINE_SUPPLIER_BACKLOG_MARGIN_FCF_GATE", "forward_window_last_date": "2025-05-19", "forward_window_trading_days": 180, "four_b_evidence_type": ["contract_delay", "margin_or_backlog_slowdown", "explicit_event_cap"], "four_b_full_window_peak_proximity": "case_specific", "four_b_local_peak_proximity": "case_specific", "four_b_timing_verdict": "Stage4B used only when non-price delay/guidance evidence exists", "four_c_protection_label": "hard_4c_blocked_unless_order_or_cashflow_thesis_break_confirmed", "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 203, "loop_objective": ["residual_false_positive_mining", "stage2_actionable_bonus_stress_test", "sector_specific_rule_discovery", "counterexample_mining"], "peak_date": "2025-05-19", "peak_price": 22150.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100090/2024.csv", "price_source": "Songdaiki/stock-web", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/100/100090.json", "raw_component_scores_after": {"bottleneck_pricing": 14, "capital_allocation": 3, "cash_conversion_quality": 8, "earnings_visibility": 15, "eps_fcf_explosion": 13, "execution_risk": -2, "high_mae_green_cap": -3, "information_confidence": 8, "margin_bridge_quality": 12, "market_mispricing": 8, "valuation_rerating": 8}, "raw_component_scores_before": {"bottleneck_pricing": 13, "capital_allocation": 3, "cash_conversion_quality": 7, "earnings_visibility": 14, "eps_fcf_explosion": 12, "execution_risk": -1, "information_confidence": 8, "margin_bridge_quality": 10, "market_mispricing": 9, "valuation_rerating": 9}, "research_file": "e2r_stock_web_v12_residual_round_R1_loop_203_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "reuse_reason": "same canonical allowed; symbol/trigger/date/evidence family not used in recent visible C01/C05/C13/C10 loops", "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_203::100090::Stage4B::2024-08-16", "schema_version": "e2r_stock_web_v12_residual.v1", "sector": "industrials_infra_defense_grid", "shares_change_pct_180D": 0.0, "stage2_evidence_fields": ["backlog_or_delivery_visibility"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["contract_delay", "margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": [], "stage_label_after": "Stage4B", "stage_label_before": "Stage4B", "stock_web_manifest_max_date": "2026-02-20", "symbol": "100090", "trigger_date": "2024-08-16", "trigger_id": "R1L203_C01_T06_100090_2024-08-16", "trigger_outcome_label": "stage4b_watch_not_hard_4c_when_backlog_and_specialty_ship_offset_survive", "trigger_type": "Stage4B", "weighted_score_after": 49, "weighted_score_before": 42}
{"canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "counterexample_count": 2, "current_profile_error_count": 5, "diversity_score_summary": {"minimum_new_independent_case_ratio": 1.0, "new_symbols": ["071970", "082740", "100090"], "new_trigger_families": ["engine_supplier_sales_double_margin", "engine_delivery_schedule_df_mix", "offshore_wind_long_lead_capex", "order_delay_guidance_cut_offset"]}, "do_not_propose_new_weight_delta": false, "fine_archetype_id": "C01_ENGINE_SUPPLIER_BACKLOG_MARGIN_FCF_GATE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 203, "loop_contribution_label": "canonical_archetype_rule_candidate", "new_independent_case_count": 6, "new_symbol_count": 3, "new_trigger_family_count": 4, "positive_case_count": 4, "reused_case_count": 0, "round": "R1", "row_type": "aggregate", "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 4}
{"canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "contribution": "Adds engine-supplier and offshore-wind component supplier rows to separate true backlog-to-margin conversion from long-lead capex/order-delay false positives; no production scoring change.", "existing_axis_kept": ["stage3_green_strictness", "hard_4c_requires_non_price_thesis_break"], "existing_axis_strengthened": ["stage2_required_bridge", "high_mae_green_cap"], "existing_axis_tested": ["stage2_required_bridge", "stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "fine_archetype_id": "C01_ENGINE_SUPPLIER_BACKLOG_MARGIN_FCF_GATE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 203, "new_axis_proposed": false, "ready_for_batch_ingest": true, "round": "R1", "row_type": "residual_contribution"}
```

## 10. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 2
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 11. Residual Contribution Summary

```text
loop_contribution_label = canonical_archetype_rule_candidate
independent_evidence_weight = 1.0
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = false
```

This loop broadens C01 beyond prime-yard shipbuilders.  It adds supplier-level order-to-sales rows, a direct margin-positive engine row, and an offshore-wind component false-positive path.  The bridge behaves like a valve: when backlog flows through delivery and margin, Stage2-Actionable is valid; when it stops at long-lead capacity or delayed orders, the pressure should stay in Stage2/4B-watch rather than flooding Yellow/Green.

## 12. Deferred Coding Agent Handoff Prompt

Do not execute this handoff in the research session.

```text
Later batch implementation may parse this MD with other v12 residual files and test a C01-scoped shadow patch named C01_SUPPLIER_ORDER_TO_MARGIN_AND_CASHFLOW_GATE.

Patch intent:
- keep global Stage3-Green thresholds unchanged;
- only adjust C01 supplier-level handling;
- require second-bridge evidence for Stage2-Actionable;
- route long-lead facility capex without shipment/cash evidence to Stage2 cap or Stage4B-watch;
- preserve hard 4C only for order cancellation, backlog collapse, margin thesis break, or cash-conversion failure.

Before promotion, confirm no hard duplicate key:
canonical_archetype_id + symbol + trigger_type + entry_date.
```

## 13. Next Research State

```text
completed_round = R1
completed_loop = 203
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance reinforcement / C01 backlog-to-FCF counterexample repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes =
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP_HARD_4C_DIRECT_BREAK_ONLY
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
  - C15_MATERIAL_SPREAD_SUPERCYCLE_STRATEGIC_RESOURCE_4C_OFFSET_REPAIR
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
```
