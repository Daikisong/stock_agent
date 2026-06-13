# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round


## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R10
selected_loop = 124
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = mixed_c30_pf_hard_break_vs_balance_sheet_repair_leaf_set
loop_objective = coverage_gap_fill|counterexample_mining|4B_4C_path|canonical_archetype_rule_discovery
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-prove the global axes. It tests whether C30 needs a narrower construction/PF/balance-sheet repair gate.

## 2. Round / Large Sector / Canonical Archetype Scope

C30 maps to R10 / L9. This is a construction, real estate, PF, liquidity, cost-rate, balance-sheet hard-break and repair archetype. The loop deliberately avoids previous C30 top-covered symbols from the No-Repeat index (`009410`, `034300`, `183190`) and uses new symbols `294870`, `006360`, `047040`, and `375500`.

```text
selected_round = R10
selected_loop = 124
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
invalid_round_sector_pair = false
```

## 3. Previous Coverage / Duplicate Avoidance Check

The index marks C30 as Priority 0 with 3 representative rows before this run. This loop adds 5 representative trigger rows if accepted.

```text
coverage_before_C30_rows = 3
representative_rows_added_if_accepted = 5
coverage_after_if_accepted = 8
need_to_30_after_if_accepted = 22
need_to_50_after_if_accepted = 42
hard_duplicate_keys_reused = 0
reused_case_count = 0
new_symbols = 294870|006360|047040|375500
```

Hard duplicate key rule applied: `canonical_archetype_id + symbol + trigger_type + entry_date`. The same Daewoo symbol appears twice only because the 2023 and 2025 triggers are different years, different evidence families, different entry dates, and opposite residual outcomes.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
price_data_repo = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

## 5. Historical Eligibility Gate

All trigger rows below satisfy: historical trigger date, stock-web tradable entry row, entry close price, at least 180 forward tradable rows, complete 30D/90D/180D MFE and MAE, and clean 180D corporate-action window.

|symbol|entry_date|entry_price|forward_window_trading_days|price_shard_path|profile_path|corporate_action_window_status|calibration_usable|
|---|---|---|---|---|---|---|---|
|294870|2022-01-12|20850.0|484|atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv|atlas/symbol_profiles/294/294870.json|clean_180D_window|true|
|006360|2023-07-06|14520.0|605|atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv|atlas/symbol_profiles/006/006360.json|clean_180D_window|true|
|047040|2023-02-01|4615.0|744|atlas/ohlcv_tradable_by_symbol_year/047/047040/2023.csv|atlas/symbol_profiles/047/047040.json|clean_180D_window|true|
|375500|2024-11-01|31200.0|316|atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv|atlas/symbol_profiles/375/375500.json|clean_180D_window|true|
|047040|2025-04-29|3520.0|197|atlas/ohlcv_tradable_by_symbol_year/047/047040/2025.csv|atlas/symbol_profiles/047/047040.json|clean_180D_window|true|
|375500|2025-05-23|48200.0|182|atlas/ohlcv_tradable_by_symbol_year/375/375500/2025.csv|atlas/symbol_profiles/375/375500.json|clean_180D_window|true|

## 6. Canonical Archetype Compression Map

| fine/deep leaf | canonical compression | rule meaning |
|---|---|---|
| SAFETY_TRUST_HARD_4C_COLLAPSE | C30 | Collapse/safety/trust failure routes to 4C even if later rebound exists. |
| REBUILD_COST_REGULATORY_SUSPENSION_BREAK | C30 | Rebuild cost and business-suspension risk block positive Stage2. |
| RECORD_EARNINGS_WITHOUT_CASH_PF_REPAIR_FALSE_POSITIVE | C30 | OP/backlog headline alone is insufficient if PF/cash/cost-rate repair is missing. |
| COST_RATE_NET_CASH_REPAIR_BARGAIN_REBOUND | C30 | Cost-rate repair and net cash can unlock Stage2/Yellow earlier. |
| PROFIT_BACKLOG_BALANCE_SHEET_REPAIR | C30 | Profit plus order/backlog repair can be valid, if legal/trust risk is low. |
| PRICE_EXTENSION_4B_WATCH_ONLY | C30 | Price-only local extension is watch-only unless non-price deterioration appears. |

## 7. Case Selection Summary

|case_id|symbol|company_name|case_type|positive_or_counterexample|best_trigger|current_profile_verdict|score_price_alignment|
|---|---|---|---|---|---|---|---|
|C30_R10L124_294870_HDC_GWANGJU_COLLAPSE_HARD_4C|294870|HDC현대산업개발|4C_success|counterexample|R10L124_C30_294870_20220112_STAGE4C_HDC_GWANGJU_COLLAPSE|current_profile_correct|hard_4c_correctly_avoids_stage2_despite_local_rebound_risk|
|C30_R10L124_006360_GS_GEOMDAN_REBUILD_COST_HARD_BREAK|006360|GS건설|4C_success|counterexample|R10L124_C30_006360_20230706_STAGE4C_GEOMDAN_REBUILD_COST|current_profile_correct_if_rebuild_cost_and_suspension_risk_blocks_stage2_positive|stage4c_or_watch_blocks_false_repair_signal_even_with_later_mfe|
|C30_R10L124_047040_DAEWOO_RECORD_EARNINGS_NO_FOLLOW_THROUGH|047040|대우건설|failed_rerating|counterexample|R10L124_C30_047040_20230201_STAGE2_FALSEPOSITIVE_RECORD_EARNINGS|current_profile_false_positive|headline_record_earnings_backlog_not_enough_when_balance_sheet_cash_repair_missing|
|C30_R10L124_375500_DLENC_COST_RATE_NET_CASH_REPAIR|375500|DL이앤씨|structural_success|positive|R10L124_C30_375500_20241101_STAGE2_DLENC_COST_RATE_REPAIR|current_profile_missed_structural|cost_rate_improvement_and_net_cash_repair_align_with_low_mae_high_mfe|
|C30_R10L124_047040_DAEWOO_2025_Q1_PROFIT_BACKLOG_REPAIR|047040|대우건설|structural_success|positive|R10L124_C30_047040_20250429_STAGE2_DAEWOO_Q1_PROFIT_BACKLOG_REPAIR|current_profile_missed_structural|improved_profit_and_new_orders_backlog_path_aligns_with_positive_mfe_mae|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
4B_case_count = 1
4C_case_count = 2
calibration_usable_case_count = 5
calibration_usable_trigger_count = 6
```

## 9. Evidence Source Map

| case_id | evidence source | interpretation |
|---|---|---|
| C30_R10L124_294870_HDC_GWANGJU_COLLAPSE_HARD_4C | Reuters/Yonhap on Gwangju collapse and chairman resignation | Safety/trust break, project suspension, investigation. |
| C30_R10L124_006360_GS_GEOMDAN_REBUILD_COST_HARD_BREAK | Yonhap on Geomdan collapse, rebuild cost, and suspension push | Rebuild cost and regulatory block. |
| C30_R10L124_047040_DAEWOO_RECORD_EARNINGS_NO_FOLLOW_THROUGH | The Investor on 2022 record earnings/order backlog | Headline earnings/backlog without repair follow-through. |
| C30_R10L124_375500_DLENC_COST_RATE_NET_CASH_REPAIR | DL E&C Q3 2024 release | Cost-rate improvement, operating-profit rebound, cash/net-cash stability. |
| C30_R10L124_047040_DAEWOO_2025_Q1_PROFIT_BACKLOG_REPAIR | Yonhap on Q1 2025 operating profit, new orders, backlog | Profit/new-order/backlog repair with improved price path. |

## 10. Price Data Source Map

|trigger_id|symbol|price_shard_path|profile_path|price_basis|price_adjustment_status|stock_web_manifest_max_date|
|---|---|---|---|---|---|---|
|R10L124_C30_294870_20220112_STAGE4C_HDC_GWANGJU_COLLAPSE|294870|atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv|atlas/symbol_profiles/294/294870.json|tradable_raw|raw_unadjusted_marcap|2026-02-20|
|R10L124_C30_006360_20230706_STAGE4C_GEOMDAN_REBUILD_COST|006360|atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv|atlas/symbol_profiles/006/006360.json|tradable_raw|raw_unadjusted_marcap|2026-02-20|
|R10L124_C30_047040_20230201_STAGE2_FALSEPOSITIVE_RECORD_EARNINGS|047040|atlas/ohlcv_tradable_by_symbol_year/047/047040/2023.csv|atlas/symbol_profiles/047/047040.json|tradable_raw|raw_unadjusted_marcap|2026-02-20|
|R10L124_C30_375500_20241101_STAGE2_DLENC_COST_RATE_REPAIR|375500|atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv|atlas/symbol_profiles/375/375500.json|tradable_raw|raw_unadjusted_marcap|2026-02-20|
|R10L124_C30_047040_20250429_STAGE2_DAEWOO_Q1_PROFIT_BACKLOG_REPAIR|047040|atlas/ohlcv_tradable_by_symbol_year/047/047040/2025.csv|atlas/symbol_profiles/047/047040.json|tradable_raw|raw_unadjusted_marcap|2026-02-20|
|R10L124_C30_375500_20250523_STAGE4B_DLENC_PRICE_EXTENSION_WATCH|375500|atlas/ohlcv_tradable_by_symbol_year/375/375500/2025.csv|atlas/symbol_profiles/375/375500.json|tradable_raw|raw_unadjusted_marcap|2026-02-20|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company_name|trigger_type|trigger_date|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|current_profile_verdict|aggregate_group_role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R10L124_C30_294870_20220112_STAGE4C_HDC_GWANGJU_COLLAPSE|294870|HDC현대산업개발|Stage4C|2022-01-11|2022-01-12|20850.0|8.87|-35.25|8.87|-36.93|8.87|-50.84|2022-01-12|22700.0|-59.07|current_profile_correct|representative|
|R10L124_C30_006360_20230706_STAGE4C_GEOMDAN_REBUILD_COST|006360|GS건설|Stage4C|2023-07-06|2023-07-06|14520.0|10.12|-7.92|10.12|-12.74|19.83|-12.74|2025-06-12|24850.0|-28.41|current_profile_correct_if_rebuild_cost_and_suspension_risk_blocks_stage2_positive|representative|
|R10L124_C30_047040_20230201_STAGE2_FALSEPOSITIVE_RECORD_EARNINGS|047040|대우건설|Stage2-Actionable|2023-02-01|2023-02-01|4615.0|4.01|-10.51|4.01|-14.63|4.01|-17.66|2026-02-20|8260.0|-8.35|current_profile_false_positive|representative|
|R10L124_C30_375500_20241101_STAGE2_DLENC_COST_RATE_REPAIR|375500|DL이앤씨|Stage2-Actionable|2024-10-31|2024-11-01|31200.0|11.54|-6.09|50.48|-6.09|91.35|-6.09|2025-06-26|59700.0|-35.59|current_profile_missed_structural|representative|
|R10L124_C30_047040_20250429_STAGE2_DAEWOO_Q1_PROFIT_BACKLOG_REPAIR|047040|대우건설|Stage2-Actionable|2025-04-29|2025-04-29|3520.0|36.51|-3.12|36.51|-3.12|63.64|-5.68|2026-02-20|8260.0|-8.35|current_profile_missed_structural|representative|
|R10L124_C30_375500_20250523_STAGE4B_DLENC_PRICE_EXTENSION_WATCH|375500|DL이앤씨|Stage4B|2025-05-23|2025-05-23|48200.0|23.86|-7.05|23.86|-16.49|23.86|-20.23|2025-06-26|59700.0|-35.59|current_profile_correct|4B_overlay_only|

## 12. Trigger-Level OHLC Backtest Tables

The calculation follows the stock-web schema: MFE_N uses max high from entry date through N tradable rows; MAE_N uses min low from entry date through N tradable rows.

|trigger_id|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|below_entry_price_flag_30D|below_entry_price_flag_90D|peak_date|peak_price|drawdown_after_peak_pct|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R10L124_C30_294870_20220112_STAGE4C_HDC_GWANGJU_COLLAPSE|8.87|-35.25|8.87|-36.93|8.87|-50.84|true|true|2022-01-12|22700.0|-59.07|
|R10L124_C30_006360_20230706_STAGE4C_GEOMDAN_REBUILD_COST|10.12|-7.92|10.12|-12.74|19.83|-12.74|true|true|2025-06-12|24850.0|-28.41|
|R10L124_C30_047040_20230201_STAGE2_FALSEPOSITIVE_RECORD_EARNINGS|4.01|-10.51|4.01|-14.63|4.01|-17.66|true|true|2026-02-20|8260.0|-8.35|
|R10L124_C30_375500_20241101_STAGE2_DLENC_COST_RATE_REPAIR|11.54|-6.09|50.48|-6.09|91.35|-6.09|true|true|2025-06-26|59700.0|-35.59|
|R10L124_C30_047040_20250429_STAGE2_DAEWOO_Q1_PROFIT_BACKLOG_REPAIR|36.51|-3.12|36.51|-3.12|63.64|-5.68|true|true|2026-02-20|8260.0|-8.35|
|R10L124_C30_375500_20250523_STAGE4B_DLENC_PRICE_EXTENSION_WATCH|23.86|-7.05|23.86|-16.49|23.86|-20.23|true|true|2025-06-26|59700.0|-35.59|

## 13. Current Calibrated Profile Stress Test

| case_id | current profile verdict | actual path interpretation | residual diagnosis |
|---|---|---|---|
| HDC collapse | current_profile_correct | 180D MAE -50.84% | Hard 4C routing is necessary. |
| GS Geomdan | current_profile_correct_if_rebuild_cost_and_suspension_risk_blocks_stage2_positive | Later MFE exists but first risk was hard break. | Rebound must not erase 4C/4B watch evidence. |
| Daewoo 2023 record OP | current_profile_false_positive | MFE 90D/180D only 4.01%, MAE 180D -17.66% | C30 needs balance-sheet/cost-rate/cash repair bridge. |
| DL E&C 2024 repair | current_profile_missed_structural | MFE 90D 50.48%, MAE 90D -6.09% | C30 should promote clean cost-rate/net-cash repair earlier. |
| Daewoo 2025 Q1 repair | current_profile_missed_structural | MFE 180D 63.64%, MAE 180D -5.68% | Profit/order/backlog repair deserves earlier Stage2/Yellow. |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is introduced in this loop. The C30 issue is earlier: deciding which construction rebound deserves Stage2/Stage3-Yellow and which should be blocked as 4C/4B watch.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
Stage2_Actionable_positive_examples = 375500_20241101, 047040_20250429
Stage2_false_positive_example = 047040_20230201
Stage4C_examples = 294870_20220112, 006360_20230706
```

## 15. 4B Local vs Full-window Timing Audit

DL E&C's 2025-05-23 row is an overlay-only 4B watch. It has price extension after the 2024 repair entry, but no new non-price deterioration, so it should not become full 4B.

|trigger_id|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|four_b_local_peak_proximity|four_b_full_window_peak_proximity|four_b_timing_verdict|four_b_evidence_type|aggregate_group_role|
|---|---|---|---|---|---|---|---|---|---|
|R10L124_C30_375500_20250523_STAGE4B_DLENC_PRICE_EXTENSION_WATCH|2025-05-23|48200.0|23.86|-16.49|0.6|0.6|watch_only_price_extension_not_full_4B_without_non_price_deterioration|price_only, positioning_overheat|4B_overlay_only|

## 16. 4C Protection Audit

HDC and GS are 4C/hard-break calibration rows. They demonstrate that C30 needs an explicit hard-break router for safety, regulatory, and trust failures. The GS case also warns that a later rebound can coexist with an initial non-price thesis break; the stage should be protection/watch first, not positive promotion.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
sector_specific_rule_candidate = L9_C30_PF_HARD_BREAK_VS_REPAIR_GATE_V1
rule_summary = In L9 construction/realtors, Stage2 requires a visible repair bridge: cost-rate improvement, net cash/debt stability, order/backlog quality, PF/liquidity risk reduction, or credible margin conversion. Safety/trust/legal/PF hard breaks route to 4C or 4B watch before any bargain-rebound promotion.
positive_support = 375500_20241101|047040_20250429
counterexample_support = 294870_20220112|006360_20230706|047040_20230201
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_rule_candidate = C30_BALANCE_SHEET_REPAIR_OR_HARD_BREAK_GATE_V1
new_axis_proposed = c30_balance_sheet_repair_or_hard_break_gate
implementation_intent = shadow_only
positive_gate = margin_bridge AND (net_cash_or_debt_stability OR order_backlog_repair OR cost_rate_improvement) AND low_legal_trust_risk
negative_gate = safety_trust_break OR regulatory_suspension_risk OR rebuild_cost_hard_break OR PF_liquidity_break
4B_gate = price_extension_only_is_watch; full_4B_requires_non_price_deterioration
4C_gate = hard_non_price_thesis_break_routes_to_4C_even_if_later_mfe_exists
```

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|eligible_trigger_count|selected_entry_trigger_per_case|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_proxy|5|5|22.0|-14.7|37.54|-18.6|0.2|2|mixed_residual_errors|
|P0b_e2r_2_0_baseline_reference|rollback_reference|5|5|22.0|-14.7|37.54|-18.6|0.6|1|worse_on_hard_break_routing|
|P1_L9_sector_specific_candidate|sector_specific|5|5|26.49|-14.72|45.92|-18.84|0.0|1|improves_false_positive_guard|
|P2_C30_canonical_candidate|canonical_archetype_specific|5|2|43.49|-4.61|77.5|-5.88|0.0|0|best_alignment_in_this_loop|
|P3_C30_counterexample_guard_profile|counterexample_guard|5|5|22.0|-14.7|37.54|-18.6|0.0|1|safer_but_can_be_too_conservative|

## 20. Score-Return Alignment Matrix

|case_id|trigger_id|symbol|weighted_score_before|stage_label_before|weighted_score_after|stage_label_after|MFE_90D_pct|MAE_90D_pct|score_return_alignment_label|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|---|
|C30_R10L124_294870_HDC_GWANGJU_COLLAPSE_HARD_4C|R10L124_C30_294870_20220112_STAGE4C_HDC_GWANGJU_COLLAPSE|294870|18|Stage4C|12|Stage4C|8.87|-36.93|hard_4c_correctly_avoids_stage2_despite_local_rebound_risk|current_profile_correct|
|C30_R10L124_006360_GS_GEOMDAN_REBUILD_COST_HARD_BREAK|R10L124_C30_006360_20230706_STAGE4C_GEOMDAN_REBUILD_COST|006360|24|Stage4C|16|Stage4C|10.12|-12.74|stage4c_or_watch_blocks_false_repair_signal_even_with_later_mfe|current_profile_correct_if_rebuild_cost_and_suspension_risk_blocks_stage2_positive|
|C30_R10L124_047040_DAEWOO_RECORD_EARNINGS_NO_FOLLOW_THROUGH|R10L124_C30_047040_20230201_STAGE2_FALSEPOSITIVE_RECORD_EARNINGS|047040|71|Stage2-Actionable|58|Stage2-Watch|4.01|-14.63|headline_record_earnings_backlog_not_enough_when_balance_sheet_cash_repair_missing|current_profile_false_positive|
|C30_R10L124_375500_DLENC_COST_RATE_NET_CASH_REPAIR|R10L124_C30_375500_20241101_STAGE2_DLENC_COST_RATE_REPAIR|375500|69|Stage2-Watch|78|Stage3-Yellow|50.48|-6.09|cost_rate_improvement_and_net_cash_repair_align_with_low_mae_high_mfe|current_profile_missed_structural|
|C30_R10L124_047040_DAEWOO_2025_Q1_PROFIT_BACKLOG_REPAIR|R10L124_C30_047040_20250429_STAGE2_DAEWOO_Q1_PROFIT_BACKLOG_REPAIR|047040|72|Stage2-Watch|80|Stage3-Yellow|36.51|-3.12|improved_profit_and_new_orders_backlog_path_aligns_with_positive_mfe_mae|current_profile_missed_structural|

## 21. Coverage Matrix

```text
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = mixed_c30_pf_hard_break_vs_balance_sheet_repair_leaf_set
positive_case_count = 2
counterexample_count = 3
4B_case_count = 1
4C_case_count = 2
new_independent_case_count = 5
reused_case_count = 0
calibration_usable_trigger_count = 6
representative_trigger_count = 5
current_profile_error_count = 3
sector_rule_candidate = L9_C30_PF_HARD_BREAK_VS_REPAIR_GATE_V1
canonical_rule_candidate = C30_BALANCE_SHEET_REPAIR_OR_HARD_BREAK_GATE_V1
coverage_gap_after_this_loop = C30 rows 3 -> 8; need 22 to 30 and 42 to 50
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 6
new_trigger_family_count: 6
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus|price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
residual_error_types_found: record_earnings_backlog_false_positive_without_balance_sheet_repair|balance_sheet_cost_rate_repair_missed_structural|hard_safety_regulatory_break_requires_c30_4c_routing
new_axis_proposed: c30_balance_sheet_repair_or_hard_break_gate
existing_axis_strengthened: full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus|stage3_yellow_total_min|stage3_green_total_min|price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: L9_C30_PF_HARD_BREAK_VS_REPAIR_GATE_V1
canonical_archetype_rule_candidate: C30_BALANCE_SHEET_REPAIR_OR_HARD_BREAK_GATE_V1
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: event-date aligned historical evidence, stock-web tradable OHLC entry close, 30/90/180D MFE/MAE, clean 180D corporate-action windows, canonical trigger labels, representative-vs-overlay dedupe fields.

Not validated: revised-adjusted OHLC, intraday exact publication timestamp where article timing is unknown, 1Y/2Y promotion where forward window or corporate-action windows are not clean, production scoring code impact, live candidate discovery, investment recommendation.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_balance_sheet_repair_or_hard_break_gate,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 needs positive repair evidence and negative hard-break routing","reduces 2023 Daewoo false positive while promoting DL E&C and 2025 Daewoo repair rows","R10L124_C30_047040_20230201_STAGE2_FALSEPOSITIVE_RECORD_EARNINGS|R10L124_C30_375500_20241101_STAGE2_DLENC_COST_RATE_REPAIR|R10L124_C30_047040_20250429_STAGE2_DAEWOO_Q1_PROFIT_BACKLOG_REPAIR",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_safety_regulatory_trust_break_4c_router,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"safety collapse/rebuild-cost/suspension risk must dominate bargain rebound","protects HDC and GS hard-break cases","R10L124_C30_294870_20220112_STAGE4C_HDC_GWANGJU_COLLAPSE|R10L124_C30_006360_20230706_STAGE4C_GEOMDAN_REBUILD_COST",2,2,2,medium,guardrail_shadow_only,"not production; 4C protection calibration"
shadow_weight,c30_price_only_4b_watch_not_full_4b,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"DL E&C price extension had no non-price deterioration","keeps 4B overlay as watch-only","R10L124_C30_375500_20250523_STAGE4B_DLENC_PRICE_EXTENSION_WATCH",1,0,0,low,overlay_shadow_only,"not production; same-case 4B overlay"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C30_R10L124_294870_HDC_GWANGJU_COLLAPSE_HARD_4C","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"124","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SAFETY_TRUST_HARD_4C_COLLAPSE","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"R10L124_C30_294870_20220112_STAGE4C_HDC_GWANGJU_COLLAPSE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard_4c_correctly_avoids_stage2_despite_local_rebound_risk","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Gwangju exterior wall collapse creates safety/trust break; price path shows deep 180D MAE."}
{"row_type":"case","case_id":"C30_R10L124_006360_GS_GEOMDAN_REBUILD_COST_HARD_BREAK","symbol":"006360","company_name":"GS건설","round":"R10","loop":"124","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REBUILD_COST_REGULATORY_SUSPENSION_BREAK","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"R10L124_C30_006360_20230706_STAGE4C_GEOMDAN_REBUILD_COST","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"stage4c_or_watch_blocks_false_repair_signal_even_with_later_mfe","current_profile_verdict":"current_profile_correct_if_rebuild_cost_and_suspension_risk_blocks_stage2_positive","price_source":"Songdaiki/stock-web","notes":"Geomdan collapse, rebuild cost, and suspension risk make any bargain rebound a risk overlay first."}
{"row_type":"case","case_id":"C30_R10L124_047040_DAEWOO_RECORD_EARNINGS_NO_FOLLOW_THROUGH","symbol":"047040","company_name":"대우건설","round":"R10","loop":"124","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"RECORD_EARNINGS_WITHOUT_CASH_PF_REPAIR_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R10L124_C30_047040_20230201_STAGE2_FALSEPOSITIVE_RECORD_EARNINGS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"headline_record_earnings_backlog_not_enough_when_balance_sheet_cash_repair_missing","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Record OP/order backlog headline did not translate into 90D/180D upside in raw path."}
{"row_type":"case","case_id":"C30_R10L124_375500_DLENC_COST_RATE_NET_CASH_REPAIR","symbol":"375500","company_name":"DL이앤씨","round":"R10","loop":"124","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"COST_RATE_NET_CASH_REPAIR_BARGAIN_REBOUND","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R10L124_C30_375500_20241101_STAGE2_DLENC_COST_RATE_REPAIR","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"cost_rate_improvement_and_net_cash_repair_align_with_low_mae_high_mfe","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Cost-rate improvement plus net cash/debt stability created a clean repair entry."}
{"row_type":"case","case_id":"C30_R10L124_047040_DAEWOO_2025_Q1_PROFIT_BACKLOG_REPAIR","symbol":"047040","company_name":"대우건설","round":"R10","loop":"124","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PROFIT_BACKLOG_BALANCE_SHEET_REPAIR","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R10L124_C30_047040_20250429_STAGE2_DAEWOO_Q1_PROFIT_BACKLOG_REPAIR","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"improved_profit_and_new_orders_backlog_path_aligns_with_positive_mfe_mae","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"2025 Q1 OP/new-order/backlog repair gives a better C30 Stage2 path than the 2023 record-earnings headline."}
{"row_type":"trigger","trigger_id":"R10L124_C30_294870_20220112_STAGE4C_HDC_GWANGJU_COLLAPSE","case_id":"C30_R10L124_294870_HDC_GWANGJU_COLLAPSE_HARD_4C","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"124","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SAFETY_TRUST_HARD_4C_COLLAPSE","sector":"construction_realestate_housing","primary_archetype":"PF_balance_sheet_break_vs_repair","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_path|canonical_archetype_rule_discovery","trigger_type":"Stage4C","trigger_date":"2022-01-11","evidence_available_at_that_date":"2022-01-11 after-market collapse; 2022-01-17 public resignation/probe confirmation used as hard 4C evidence; entry anchored to first tradable day after collapse.","evidence_source":"Reuters; Yonhap — HDC Gwangju collapse/chairman resignation; https://www.reuters.com/world/asia-pacific/skorea-builder-hdcs-chairman-steps-down-after-apartment-complex-collapse-2022-01-17/ ; https://en.yna.co.kr/view/AEN20220117002800320","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["safety_or_trial_failure","accounting_or_trust_break","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-01-12","entry_price":20850.0,"MFE_30D_pct":8.87,"MFE_90D_pct":8.87,"MFE_180D_pct":8.87,"MFE_1Y_pct":8.87,"MFE_2Y_pct":null,"MAE_30D_pct":-35.25,"MAE_90D_pct":-36.93,"MAE_180D_pct":-50.84,"MAE_1Y_pct":-55.44,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-01-12","peak_price":22700.0,"drawdown_after_peak_pct":-59.07,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"safety_trust_hard_4c_collapse","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":484,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|294870|2022-01-12|Stage4C","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L124_C30_006360_20230706_STAGE4C_GEOMDAN_REBUILD_COST","case_id":"C30_R10L124_006360_GS_GEOMDAN_REBUILD_COST_HARD_BREAK","symbol":"006360","company_name":"GS건설","round":"R10","loop":"124","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REBUILD_COST_REGULATORY_SUSPENSION_BREAK","sector":"construction_realestate_housing","primary_archetype":"PF_balance_sheet_break_vs_repair","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_path|canonical_archetype_rule_discovery","trigger_type":"Stage4C","trigger_date":"2023-07-06","evidence_available_at_that_date":"2023-07-06 intraday/public article: government fault finding, full rebuild decision, 0.5T-1.0T won cost range, broker downgrades.","evidence_source":"Yonhap — GS E&C dips on Geomdan rebuild cost; https://en.yna.co.kr/view/AEN20230706002200320 ; Yonhap — government seeks 10-month suspension; https://en.yna.co.kr/view/AEN20230827002451320","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","margin_or_backlog_slowdown","explicit_event_cap"],"stage4c_evidence_fields":["regulatory_rejection","accounting_or_trust_break","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-06","entry_price":14520.0,"MFE_30D_pct":10.12,"MFE_90D_pct":10.12,"MFE_180D_pct":19.83,"MFE_1Y_pct":23.62,"MFE_2Y_pct":71.14,"MAE_30D_pct":-7.92,"MAE_90D_pct":-12.74,"MAE_180D_pct":-12.74,"MAE_1Y_pct":-12.74,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-12","peak_price":24850.0,"drawdown_after_peak_pct":-28.41,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"rebuild_cost_regulatory_suspension_hard_break","current_profile_verdict":"current_profile_correct_if_rebuild_cost_and_suspension_risk_blocks_stage2_positive","calibration_usable":true,"forward_window_trading_days":605,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|006360|2023-07-06|Stage4C","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L124_C30_047040_20230201_STAGE2_FALSEPOSITIVE_RECORD_EARNINGS","case_id":"C30_R10L124_047040_DAEWOO_RECORD_EARNINGS_NO_FOLLOW_THROUGH","symbol":"047040","company_name":"대우건설","round":"R10","loop":"124","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"RECORD_EARNINGS_WITHOUT_CASH_PF_REPAIR_FALSE_POSITIVE","sector":"construction_realestate_housing","primary_archetype":"PF_balance_sheet_break_vs_repair","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_path|canonical_archetype_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-01","evidence_available_at_that_date":"2023-02-01 earnings/order backlog headline was available as a public article.","evidence_source":"The Investor — Daewoo E&C posts record earnings on robust housing projects; https://www.theinvestor.co.kr/article/3051947","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2023.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-01","entry_price":4615.0,"MFE_30D_pct":4.01,"MFE_90D_pct":4.01,"MFE_180D_pct":4.01,"MFE_1Y_pct":4.01,"MFE_2Y_pct":7.58,"MAE_30D_pct":-10.51,"MAE_90D_pct":-14.63,"MAE_180D_pct":-17.66,"MAE_1Y_pct":-17.66,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2026-02-20","peak_price":8260.0,"drawdown_after_peak_pct":-8.35,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"record_earnings_without_balance_sheet_repair_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":744,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|047040|2023-02-01|Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L124_C30_375500_20241101_STAGE2_DLENC_COST_RATE_REPAIR","case_id":"C30_R10L124_375500_DLENC_COST_RATE_NET_CASH_REPAIR","symbol":"375500","company_name":"DL이앤씨","round":"R10","loop":"124","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"COST_RATE_NET_CASH_REPAIR_BARGAIN_REBOUND","sector":"construction_realestate_housing","primary_archetype":"PF_balance_sheet_break_vs_repair","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_path|canonical_archetype_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-10-31","evidence_available_at_that_date":"2024-10-31 company announcement; entry uses next tradable close because release time was not assumed intraday-tradable.","evidence_source":"DL E&C — Q3 2024 cost-rate improvement and rebound in operating profit; https://www.dlenc.co.kr/eng/daelim/pr/NewsView.do?cd_mnu=EU035&currentPage=1&idx=25384&keyword=all&searchword=","stage2_evidence_fields":["public_event_or_disclosure","margin_bridge","financial_visibility"],"stage3_evidence_fields":["margin_bridge","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv","profile_path":"atlas/symbol_profiles/375/375500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-11-01","entry_price":31200.0,"MFE_30D_pct":11.54,"MFE_90D_pct":50.48,"MFE_180D_pct":91.35,"MFE_1Y_pct":91.35,"MFE_2Y_pct":null,"MAE_30D_pct":-6.09,"MAE_90D_pct":-6.09,"MAE_180D_pct":-6.09,"MAE_1Y_pct":-6.09,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-26","peak_price":59700.0,"drawdown_after_peak_pct":-35.59,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"cost_rate_net_cash_repair_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":316,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|375500|2024-11-01|Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L124_C30_047040_20250429_STAGE2_DAEWOO_Q1_PROFIT_BACKLOG_REPAIR","case_id":"C30_R10L124_047040_DAEWOO_2025_Q1_PROFIT_BACKLOG_REPAIR","symbol":"047040","company_name":"대우건설","round":"R10","loop":"124","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PROFIT_BACKLOG_BALANCE_SHEET_REPAIR","sector":"construction_realestate_housing","primary_archetype":"PF_balance_sheet_break_vs_repair","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_path|canonical_archetype_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2025-04-29","evidence_available_at_that_date":"2025-04-29 public earnings article and regulatory filing summary; treated as same-day close because article was before/around market day.","evidence_source":"Yonhap — Daewoo E&C Q1 operating profit up 31.8%, new orders/backlog; https://en.yna.co.kr/view/AEN20250429001851320","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2025.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-04-29","entry_price":3520.0,"MFE_30D_pct":36.51,"MFE_90D_pct":36.51,"MFE_180D_pct":63.64,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.12,"MAE_90D_pct":-3.12,"MAE_180D_pct":-5.68,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2026-02-20","peak_price":8260.0,"drawdown_after_peak_pct":-8.35,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"profit_backlog_balance_sheet_repair_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":197,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|047040|2025-04-29|Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L124_C30_375500_20250523_STAGE4B_DLENC_PRICE_EXTENSION_WATCH","case_id":"C30_R10L124_375500_DLENC_COST_RATE_NET_CASH_REPAIR","symbol":"375500","company_name":"DL이앤씨","round":"R10","loop":"124","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PRICE_EXTENSION_4B_WATCH_ONLY","sector":"construction_realestate_housing","primary_archetype":"PF_balance_sheet_break_vs_repair","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_path|canonical_archetype_rule_discovery","trigger_type":"Stage4B","trigger_date":"2025-05-23","evidence_available_at_that_date":"Price extension after Stage2 repair; no separate non-price deterioration, so overlay-only watch.","evidence_source":"Stock-web price path overlay; no new non-price deterioration source used for full 4B.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/375/375500/2025.csv","profile_path":"atlas/symbol_profiles/375/375500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-05-23","entry_price":48200.0,"MFE_30D_pct":23.86,"MFE_90D_pct":23.86,"MFE_180D_pct":23.86,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.05,"MAE_90D_pct":-16.49,"MAE_180D_pct":-20.23,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-26","peak_price":59700.0,"drawdown_after_peak_pct":-35.59,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.6,"four_b_full_window_peak_proximity":0.6,"four_b_timing_verdict":"watch_only_price_extension_not_full_4B_without_non_price_deterioration","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"price_extension_4b_watch_only_after_structural_repair","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":182,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|375500|2025-05-23|Stage4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case as DL E&C 2024 repair; used only for 4B local-vs-full timing overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"P2_C30_canonical_candidate_shadow","case_id":"C30_R10L124_294870_HDC_GWANGJU_COLLAPSE_HARD_4C","trigger_id":"R10L124_C30_294870_20220112_STAGE4C_HDC_GWANGJU_COLLAPSE","symbol":"294870","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":20,"valuation_repricing_score":0,"execution_risk_score":95,"legal_or_contract_risk_score":95,"dilution_cb_risk_score":0,"accounting_trust_risk_score":85},"weighted_score_before":18,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":0,"execution_risk_score":98,"legal_or_contract_risk_score":98,"dilution_cb_risk_score":0,"accounting_trust_risk_score":92},"weighted_score_after":12,"stage_label_after":"Stage4C","changed_components":["policy_or_regulatory_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"hard safety/trust break should dominate any valuation or bargain-rebound logic","MFE_90D_pct":8.87,"MAE_90D_pct":-36.93,"score_return_alignment_label":"hard_4c_correctly_avoids_stage2_despite_local_rebound_risk","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"P2_C30_canonical_candidate_shadow","case_id":"C30_R10L124_006360_GS_GEOMDAN_REBUILD_COST_HARD_BREAK","trigger_id":"R10L124_C30_006360_20230706_STAGE4C_GEOMDAN_REBUILD_COST","symbol":"006360","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":40,"valuation_repricing_score":20,"execution_risk_score":90,"legal_or_contract_risk_score":92,"dilution_cb_risk_score":0,"accounting_trust_risk_score":78},"weighted_score_before":24,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":30,"valuation_repricing_score":10,"execution_risk_score":96,"legal_or_contract_risk_score":96,"dilution_cb_risk_score":0,"accounting_trust_risk_score":85},"weighted_score_after":16,"stage_label_after":"Stage4C","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"rebuild cost and suspension risk block Stage2 even if later rebound appears","MFE_90D_pct":10.12,"MAE_90D_pct":-12.74,"score_return_alignment_label":"stage4c_or_watch_blocks_false_repair_signal_even_with_later_mfe","current_profile_verdict":"current_profile_correct_if_rebuild_cost_and_suspension_risk_blocks_stage2_positive"}
{"row_type":"score_simulation","profile_id":"P2_C30_canonical_candidate_shadow","case_id":"C30_R10L124_047040_DAEWOO_RECORD_EARNINGS_NO_FOLLOW_THROUGH","trigger_id":"R10L124_C30_047040_20230201_STAGE2_FALSEPOSITIVE_RECORD_EARNINGS","symbol":"047040","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":50,"backlog_visibility_score":75,"margin_bridge_score":55,"revision_score":45,"relative_strength_score":35,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":50,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":0,"accounting_trust_risk_score":35},"weighted_score_before":71,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":55,"margin_bridge_score":35,"revision_score":30,"relative_strength_score":25,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":35,"execution_risk_score":62,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":0,"accounting_trust_risk_score":40},"weighted_score_after":58,"stage_label_after":"Stage2-Watch","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"record earnings/backlog without cash/PF repair should be demoted from actionable","MFE_90D_pct":4.01,"MAE_90D_pct":-14.63,"score_return_alignment_label":"headline_record_earnings_backlog_not_enough_when_balance_sheet_cash_repair_missing","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"P2_C30_canonical_candidate_shadow","case_id":"C30_R10L124_375500_DLENC_COST_RATE_NET_CASH_REPAIR","trigger_id":"R10L124_C30_375500_20241101_STAGE2_DLENC_COST_RATE_REPAIR","symbol":"375500","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":65,"revision_score":45,"relative_strength_score":40,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":35,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":15},"weighted_score_before":69,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":45,"margin_bridge_score":82,"revision_score":58,"relative_strength_score":55,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":60,"execution_risk_score":25,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"cost-rate repair and net cash evidence deserve earlier C30 promotion to Yellow/watchlist","MFE_90D_pct":50.48,"MAE_90D_pct":-6.09,"score_return_alignment_label":"cost_rate_improvement_and_net_cash_repair_align_with_low_mae_high_mfe","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"P2_C30_canonical_candidate_shadow","case_id":"C30_R10L124_047040_DAEWOO_2025_Q1_PROFIT_BACKLOG_REPAIR","trigger_id":"R10L124_C30_047040_20250429_STAGE2_DAEWOO_Q1_PROFIT_BACKLOG_REPAIR","symbol":"047040","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":65,"margin_bridge_score":60,"revision_score":50,"relative_strength_score":45,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":40,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":0,"accounting_trust_risk_score":25},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":65,"backlog_visibility_score":78,"margin_bridge_score":68,"revision_score":58,"relative_strength_score":60,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":62,"execution_risk_score":30,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":18},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"profit plus order/backlog repair differentiates this from the 2023 headline-only false positive","MFE_90D_pct":36.51,"MAE_90D_pct":-3.12,"score_return_alignment_label":"improved_profit_and_new_orders_backlog_path_aligns_with_positive_mfe_mae","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"residual_contribution","round":"R10","loop":"124","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["record_earnings_backlog_false_positive_without_balance_sheet_repair","balance_sheet_cost_rate_repair_missed_structural","hard_safety_regulatory_break_requires_c30_4c_routing"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks
1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output
- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R10
completed_loop = 124
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C31_POLICY_SUBSIDY_LEGISLATION_EVENT|C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|C15_MATERIAL_SPREAD_SUPERCYCLE|C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- MAIN execution prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web, atlas/manifest.json, atlas/schema.json, atlas/universe/all_symbols.csv, symbol-year tradable shards.
- External evidence sources were used only to anchor historical trigger dates and non-price evidence; price calculations use only stock-web OHLC.


## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
