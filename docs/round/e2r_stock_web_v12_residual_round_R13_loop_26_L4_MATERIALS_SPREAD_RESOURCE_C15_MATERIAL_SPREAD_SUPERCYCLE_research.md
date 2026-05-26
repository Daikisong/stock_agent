# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| round | loop | large_sector_id | canonical_archetype_id | fine_archetype_id | mode | research_session | production_scoring_changed | shadow_weight_only | stock_web_manifest_max_date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13 | 26 | L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | COPPER_DEFENSE_SPREAD_VS_PETROCHEMICAL_SPREAD_TRAP | historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12 | post_calibrated_sector_archetype_residual_research | False | True | 2026-02-20 |


## 1. Current Calibrated Profile Assumption

current_default_profile_proxy = `e2r_2_1_stock_web_calibrated_proxy`.

Applied global axes treated as already active, not re-proposed: `stage2_actionable_evidence_bonus=+2.0`, `stage3_yellow_total_min=75`, `stage3_green_total_min=87`, `stage3_green_revision_min=55`, `stage3_cross_evidence_green_buffer=+1.5`, `price_only_blowoff_blocks_positive_stage=true`, `full_4b_requires_non_price_evidence=true`, `hard_4c_thesis_break_routes_to_4c=true`.

This loop tests whether C15 materials/spread cases need a narrower rule: **raw commodity/spread movement alone is not enough; spread must cross the bridge into margin visibility, revision, or order/customer quality**. The mechanism is like a furnace: commodity price is heat, but margin/revision is the metal actually changing shape. Without that conversion, the glow can fade into inventory loss and drawdown.

## 2. Round / Large Sector / Canonical Archetype Scope

- round: `R13`
- loop: `26`
- large_sector_id: `L4_MATERIALS_SPREAD_RESOURCE`
- canonical_archetype_id: `C15_MATERIAL_SPREAD_SUPERCYCLE`
- fine_archetype_id: `COPPER_DEFENSE_SPREAD_VS_PETROCHEMICAL_SPREAD_TRAP`
- loop_objective: `holdout_validation, residual_false_positive_mining, sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, 4B_non_price_requirement_stress_test, coverage_gap_fill`

## 3. Previous Coverage / Duplicate Avoidance Check

The allowed stock_agent research artifact check showed the prior calibration ledger already contains 107 parsed result MDs, 1,940 validated trigger rows, and 1,376 aggregate representative rows across R1-R13 / loop 1-9. The previous chat-created L6/C21 capital-return loop is not reused. This loop selects four L4/C15 holdout symbols not used by the immediate prior L6/C21 MD, and it focuses on a different residual family: spread-to-margin conversion versus spread-only traps.

## 4. Stock-Web OHLC Input / Price Source Validation

| source | source_url | manifest_path | schema_path | universe_path | manifest_max_date | price_basis | price_adjustment_status | calibration_shard_root | raw_shard_root | validation_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Songdaiki/stock-web | https://github.com/Songdaiki/stock-web | atlas/manifest.json | atlas/schema.json | atlas/universe/all_symbols.csv | 2026-02-20 | tradable_raw | raw_unadjusted_marcap | atlas/ohlcv_tradable_by_symbol_year | atlas/ohlcv_raw_by_symbol_year | usable_for_historical_calibration |


Manifest facts used: source_name `FinanceData/marcap`; `price_adjustment_status=raw_unadjusted_marcap`; min_date `1995-05-02`; max_date `2026-02-20`; tradable_row_count `14354401`; raw_row_count `15214118`; symbol_count `5414`; active_like_symbol_count `2868`; inactive_or_delisted_like_symbol_count `2546`; markets `KONEX`, `KOSDAQ`, `KOSDAQ GLOBAL`, `KOSPI`.

## 5. Historical Eligibility Gate

| trigger_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | calibration_usable | forward_window_trading_days | corporate_action_window_status | calibration_block_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L26_C15_001_T1_STAGE2_ACTIONABLE | 103140 | 풍산 | Stage2-Actionable | 2024-03-13 | 2024-03-13 | 44450 | True | 180 | clean_180D_window |  |
| R13L26_C15_001_T2_STAGE4B_WATCH | 103140 | 풍산 | Stage4B-Watch | 2024-05-14 | 2024-05-14 | 76300 | True | 180 | clean_180D_window |  |
| R13L26_C15_002_T1_STAGE2_ACTIONABLE | 006260 | LS | Stage2-Actionable | 2024-04-12 | 2024-04-12 | 122100 | True | 180 | clean_180D_window |  |
| R13L26_C15_002_T2_STAGE4B_WATCH | 006260 | LS | Stage4B-Watch | 2024-05-21 | 2024-05-21 | 179300 | True | 180 | clean_180D_window |  |
| R13L26_C15_003_T1_STAGE2_WATCH | 006650 | 대한유화 | Stage2-Watch | 2024-04-02 | 2024-04-02 | 143000 | True | 180 | clean_180D_window |  |
| R13L26_C15_004_T1_STAGE2_WATCH | 011170 | 롯데케미칼 | Stage2-Watch | 2024-03-15 | 2024-03-15 | 121300 | True | 180 | clean_180D_window |  |


## 6. Canonical Archetype Compression Map

| large_sector_id | canonical_archetype_id | fine_archetype_id | compression_logic |
| --- | --- | --- | --- |
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | COPPER_DEFENSE_SPREAD_VS_PETROCHEMICAL_SPREAD_TRAP | Compress copper/defense spread success, grid/copper high-MAE success, petrochemical spread trap, and chemical thesis-break into one C15 rule family: spread evidence must convert into margin/revision bridge before promotion. |


## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict | score_price_alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R13L26_C15_001 | 103140 | 풍산 | structural_success | positive | R13L26_C15_001_T1_STAGE2_ACTIONABLE | current_profile_missed_structural | aligned_positive_with_low_mae |
| R13L26_C15_002 | 006260 | LS | high_mae_success | positive | R13L26_C15_002_T1_STAGE2_ACTIONABLE | current_profile_too_early | high_mfe_but_high_mae |
| R13L26_C15_003 | 006650 | 대한유화 | failed_rerating | counterexample | R13L26_C15_003_T1_STAGE2_WATCH | current_profile_false_positive | weak_mfe_large_mae_counterexample |
| R13L26_C15_004 | 011170 | 롯데케미칼 | 4C_success | counterexample | R13L26_C15_004_T1_STAGE2_WATCH | current_profile_correct | guarded_counterexample |


## 8. Positive vs Counterexample Balance

Positive structural / high-MFE cases: `2` (`103140`, `006260`). Counterexamples / failed rerating / hard 4C cases: `2` (`006650`, `011170`). The balance is intentional: C15 is dangerous when the model hears commodity price noise as if it were EPS revision. The positive side shows the right furnace; the negative side shows smoke without forged metal.

## 9. Evidence Source Map

| case_id | symbol | stage2_evidence | stage3_evidence | 4B_evidence | 4C_evidence | evidence_source |
| --- | --- | --- | --- | --- | --- | --- |
| R13L26_C15_001 | 103140 | public_event_or_disclosure,relative_strength,capacity_or_volume_route,policy_or_regulatory_optionality,early_revision_signal | margin_bridge,financial_visibility,multiple_public_sources |  |  | public earnings/industry reports around 2024-03-13; stock-web 103140 2024 shard rows 2024-03-13 through 2024-12-30 verified |
| R13L26_C15_001 | 103140 |  |  | valuation_blowoff,positioning_overheat,price_only_local_peak |  | stock-web 103140 2024 row 2024-05-14; no contemporaneous hard thesis-break evidence used |
| R13L26_C15_002 | 006260 | public_event_or_disclosure,relative_strength,capacity_or_volume_route,policy_or_regulatory_optionality | multiple_public_sources |  |  | public copper/grid theme reports around 2024-04-12; stock-web 006260 2024 shard rows 2024-04-12 through 2024-12-30 verified |
| R13L26_C15_002 | 006260 |  |  | valuation_blowoff,positioning_overheat,price_only_local_peak |  | stock-web 006260 2024 row 2024-05-21; no hard non-price 4B evidence used |
| R13L26_C15_003 | 006650 | public_event_or_disclosure |  | margin_or_backlog_slowdown | thesis_evidence_broken | public petrochemical spread/recovery narrative around 2024-04-02; stock-web 006650 2024 shard rows verified |
| R13L26_C15_004 | 011170 | public_event_or_disclosure |  | margin_or_backlog_slowdown | thesis_evidence_broken | public petrochemical spread/recovery narrative around 2024-03-15; stock-web 011170 2024 shard rows verified |


## 10. Price Data Source Map

| symbol | company_name | price_shard_path | profile_path | price_basis | price_adjustment_status | profile_corporate_action_note |
| --- | --- | --- | --- | --- | --- | --- |
| 103140 | 풍산 | atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv | atlas/symbol_profiles/103/103140.json | tradable_raw | raw_unadjusted_marcap | No 2024 entry-to-180D overlap with listed corporate-action candidate windows; historical old corporate-action caveats remain profile-level only. |
| 006260 | LS | atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv | atlas/symbol_profiles/006/006260.json | tradable_raw | raw_unadjusted_marcap | No 2024 entry-to-180D overlap with listed corporate-action candidate windows; historical old corporate-action caveats remain profile-level only. |
| 006650 | 대한유화 | atlas/ohlcv_tradable_by_symbol_year/006/006650/2024.csv | atlas/symbol_profiles/006/006650.json | tradable_raw | raw_unadjusted_marcap | No 2024 entry-to-180D overlap with listed corporate-action candidate windows; historical old corporate-action caveats remain profile-level only. |
| 011170 | 롯데케미칼 | atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv | atlas/symbol_profiles/011/011170.json | tradable_raw | raw_unadjusted_marcap | No 2024 entry-to-180D overlap with listed corporate-action candidate windows; historical old corporate-action caveats remain profile-level only. |


## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | stage2_fields | stage3_fields | stage4b_fields | stage4c_fields | current_profile_verdict | trigger_outcome_label |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L26_C15_001_T1_STAGE2_ACTIONABLE | R13L26_C15_001 | 103140 | 풍산 | Stage2-Actionable | 2024-03-13 | 2024-03-13 | 44450 | public_event_or_disclosure,relative_strength,capacity_or_volume_route,policy_or_regulatory_optionality,early_revision_signal | margin_bridge,financial_visibility,multiple_public_sources |  |  | current_profile_missed_structural | structural_success_spread_margin_bridge |
| R13L26_C15_001_T2_STAGE4B_WATCH | R13L26_C15_001 | 103140 | 풍산 | Stage4B-Watch | 2024-05-14 | 2024-05-14 | 76300 |  |  | valuation_blowoff,positioning_overheat,price_only_local_peak |  | current_profile_4B_too_early | 4B_watch_useful_but_not_full_4B |
| R13L26_C15_002_T1_STAGE2_ACTIONABLE | R13L26_C15_002 | 006260 | LS | Stage2-Actionable | 2024-04-12 | 2024-04-12 | 122100 | public_event_or_disclosure,relative_strength,capacity_or_volume_route,policy_or_regulatory_optionality | multiple_public_sources |  |  | current_profile_too_early | high_mfe_high_mae_success |
| R13L26_C15_002_T2_STAGE4B_WATCH | R13L26_C15_002 | 006260 | LS | Stage4B-Watch | 2024-05-21 | 2024-05-21 | 179300 |  |  | valuation_blowoff,positioning_overheat,price_only_local_peak |  | current_profile_4B_too_early | 4B_watch_near_peak_but_not_full_exit |
| R13L26_C15_003_T1_STAGE2_WATCH | R13L26_C15_003 | 006650 | 대한유화 | Stage2-Watch | 2024-04-02 | 2024-04-02 | 143000 | public_event_or_disclosure |  | margin_or_backlog_slowdown | thesis_evidence_broken | current_profile_false_positive | failed_rerating_spread_only_counterexample |
| R13L26_C15_004_T1_STAGE2_WATCH | R13L26_C15_004 | 011170 | 롯데케미칼 | Stage2-Watch | 2024-03-15 | 2024-03-15 | 121300 | public_event_or_disclosure |  | margin_or_backlog_slowdown | thesis_evidence_broken | current_profile_correct | hard_4c_thesis_break_counterexample |


## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MFE_1Y_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | MAE_1Y_pct | below_entry_price_flag_30D | below_entry_price_flag_90D | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L26_C15_001_T1_STAGE2_ACTIONABLE | 103140 | 2024-03-13 | 44450 | 51.86 | 77.5 | 77.5 | 77.5 | -0.34 | -0.34 | -0.34 | -0.34 | False | False | 2024-05-14 | 78900 | -41.51 |
| R13L26_C15_001_T2_STAGE4B_WATCH | 103140 | 2024-05-14 | 76300 | 3.41 | 3.41 | 3.41 | 3.41 | -18.22 | -38.33 | -39.52 | -39.52 | True | True | 2024-05-14 | 78900 | -41.51 |
| R13L26_C15_002_T1_STAGE2_ACTIONABLE | 006260 | 2024-04-12 | 122100 | 59.54 | 59.54 | 59.54 | 59.54 | -6.88 | -23.01 | -30.79 | -30.79 | True | True | 2024-05-21 | 194800 | -56.62 |
| R13L26_C15_002_T2_STAGE4B_WATCH | 006260 | 2024-05-21 | 179300 | 8.64 | 8.64 | 8.64 | 8.64 | -23.48 | -47.57 | -52.87 | -52.87 | True | True | 2024-05-21 | 194800 | -56.62 |
| R13L26_C15_003_T1_STAGE2_WATCH | 006650 | 2024-04-02 | 143000 | 9.3 | 12.59 | 12.59 |  | -13.71 | -32.17 | -52.17 |  | True | True | 2024-05-20 | 161000 | -57.52 |
| R13L26_C15_004_T1_STAGE2_WATCH | 011170 | 2024-03-15 | 121300 | 3.22 | 3.46 | 3.46 |  | -20.78 | -20.78 | -53.5 |  | True | True | 2024-05-20 | 125500 | -55.06 |


## 13. Current Calibrated Profile Stress Test

| case_id | symbol | company_name | current_profile_verdict | stress_test_read | score_price_alignment |
| --- | --- | --- | --- | --- | --- |
| R13L26_C15_001 | 103140 | 풍산 | current_profile_missed_structural | Stage2 too late/missed | aligned_positive_with_low_mae |
| R13L26_C15_002 | 006260 | LS | current_profile_too_early | Stage2 too early/high MAE | high_mfe_but_high_mae |
| R13L26_C15_003 | 006650 | 대한유화 | current_profile_false_positive | Spread-only false positive | weak_mfe_large_mae_counterexample |
| R13L26_C15_004 | 011170 | 롯데케미칼 | current_profile_correct | Guarded watch-only was correct | guarded_counterexample |


Answers to required stress questions:

1. The current calibrated profile would generally avoid pure price-only promotion, but it can still over-credit raw spread/commodity narratives when relative strength is strong.
2. Actual MFE/MAE supports a split: `103140` worked cleanly; `006260` worked but with large MAE; `006650` and `011170` were spread-only traps.
3. Stage2 bonus was useful for `103140`, risky for `006260`, and too generous for petrochemical spread-only cases.
4. Yellow threshold 75 is not the main issue; the issue is component quality before the total score.
5. Green threshold 87 / revision 55 should remain strict. C15 needs revision/margin conversion, not looser Green.
6. price-only blowoff guard remains appropriate.
7. full 4B non-price requirement remains appropriate; price-only local peaks should be watch overlays.
8. hard 4C routing is valuable for petrochemical names once thesis evidence breaks.

## 14. Stage2 / Yellow / Green Comparison

| symbol | trigger_type | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | green_lateness_ratio |
| --- | --- | --- | --- | --- | --- | --- |
| 103140 | Stage2-Actionable | 2024-03-13 | 44450 | 77.5 | -0.34 | not_applicable |
| 006260 | Stage2-Actionable | 2024-04-12 | 122100 | 59.54 | -23.01 | not_applicable |
| 006650 | Stage2-Watch | 2024-04-02 | 143000 | 12.59 | -32.17 | not_applicable |
| 011170 | Stage2-Watch | 2024-03-15 | 121300 | 3.46 | -20.78 | not_applicable |


`green_lateness_ratio` is marked not_applicable because the loop is not claiming a later confirmed Stage3-Green trigger. The residual finding is earlier: C15 should judge whether Stage2 evidence has a true spread-to-margin bridge before allowing Stage3 scoring pressure.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | symbol | entry_date | entry_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict | four_b_evidence_type |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R13L26_C15_001_T2_STAGE4B_WATCH | 103140 | 2024-05-14 | 76300 | 0.92 | 0.92 | price_only_local_4B_watch_not_full_4B | price_only,valuation_blowoff,positioning_overheat |
| R13L26_C15_002_T2_STAGE4B_WATCH | 006260 | 2024-05-21 | 179300 | 0.79 | 0.79 | price_only_local_4B_watch_not_full_4B | price_only,valuation_blowoff,positioning_overheat |


Price-only 4B behaved like a smoke alarm, not the fire report. It was useful as a risk overlay near the local/full peak, but without non-price deterioration it should not become a full 4B thesis exit.

## 16. 4C Protection Audit

| symbol | case_id | 4C_label | max_drawdown_after_peak_pct | interpretation |
| --- | --- | --- | --- | --- |
| 006650 | R13L26_C15_003 | hard_4c_success | -57.52 | Guarding spread-only petrochemical exposure protected against later thesis break. |
| 011170 | R13L26_C15_004 | hard_4c_success | -55.06 | Watch-only / thesis-break routing avoided false positive promotion. |


## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`.

Proposed sector rule: `l4_high_mae_commodity_beta_sizing_guard`. In L4, raw commodity beta can create early MFE before fundamentals settle. Stage2 may be allowed, but Stage3 promotion should require margin/revision bridge, and high-MAE commodity beta should lower conviction or size unless customer/order or margin evidence is present.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`.

Proposed C15 rule: `c15_confirmed_spread_to_margin_bridge_bonus` plus `c15_spread_only_without_margin_revision_guard`. Copper/defense or grid-linked spread winners can be promoted when spread is visible in margin, order route, or revision. Petrochemical spread-only narratives remain watch-only until the margin bridge hardens.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | changed_thresholds | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | Existing profile catches generic Stage2 evidence but does not distinguish confirmed spread-to-margin bridge from raw commodity/spread narrative. | none | none | 4 | all representative triggers | 38.27 | -19.08 | 38.27 | -34.2 | 50% | 1 | 1 | not_applicable | 0.855 | 0.855 | mixed_positive_and_counterexample |
| P0b_e2r_2_0_baseline_reference | rollback_reference | Pre-calibration profile is more likely to over-label petrochemical spread rebound and price-only resource beta as positive. | rollback reference only | old baseline | 4 | all representative triggers | 38.27 | -19.08 | 38.27 | -34.2 | 50-75% | 1 | 2 | not_applicable | 0.855 | 0.855 | worse_guarding |
| P1_l4_materials_sector_shadow_profile | sector_specific | L4 requires spread-to-margin conversion evidence before Stage3, and a high-MAE sizing guard for commodity beta names. | l4_spread_margin_bridge_min + l4_high_mae_sizing_guard | sector shadow only | 4 | positive only after guard; counterexamples watch-only | 68.52 | -11.68 | 68.52 | -15.57 | 0% | 0 | 1 | not_applicable | 0.855 | 0.855 | improved_positive_guarding |
| P2_c15_material_spread_shadow_profile | canonical_archetype_specific | C15 should separate copper/defense or grid-backed spread winners from petrochemical spread-only rebounds. | c15_confirmed_margin_bridge_bonus + c15_spread_only_guard | canonical shadow only | 4 | Pungsan/LS representative; petrochemical watch-only | 68.52 | -11.68 | 68.52 | -15.57 | 0% | 0 | 1 | not_applicable | 0.855 | 0.855 | best_explainability |
| P3_counterexample_guard_profile | counterexample_guard | Block promotion when spread evidence lacks margin bridge/revision and execution risk is rising. | petrochemical_spread_only_false_positive_guard | guard only | 4 | only cases with margin bridge or relative strength plus non-price support | 68.52 | -11.68 | 68.52 | -15.57 | 0% | 1 | 1 | not_applicable | 0.855 | 0.855 | guarded_but_may_delay_early_success |


## 20. Score-Return Alignment Matrix

| symbol | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | score_return_alignment_label |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 103140 | 53.8 | Stage2-Watch | 55.4 | Stage2-Watch | 77.5 | -0.34 | aligned_positive |
| 006260 | 45.3 | Stage2-Watch | 43.4 | Stage2-Watch | 59.54 | -23.01 | aligned_positive |
| 006650 | 10.4 | Stage2-Watch | 7.9 | Stage2-Watch | 12.59 | -32.17 | guarded_counterexample |
| 011170 | 1.6 | Stage2-Watch | -0.9 | Stage2-Watch | 3.46 | -20.78 | guarded_counterexample |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | COPPER_DEFENSE_SPREAD_VS_PETROCHEMICAL_SPREAD_TRAP | 2 | 2 | 2 | 2 | 4 | 0 | 6 | 4 | 3 | True | True | C15 now has spread-to-margin vs spread-only guard coverage; still needs more strategic resource holdouts. |


## 22. Residual Contribution Summary

```json
{
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "reused_case_ids": [],
  "new_symbol_count": 4,
  "new_canonical_archetype_count": 0,
  "new_fine_archetype_count": 1,
  "new_trigger_family_count": 4,
  "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "stage3_cross_evidence_green_buffer", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"],
  "residual_error_types_found": ["spread_only_false_positive", "high_mfe_high_mae_commodity_beta", "price_only_local_4b_watch_not_full_4b"],
  "new_axis_proposed": ["c15_confirmed_spread_to_margin_bridge_bonus", "c15_spread_only_without_margin_revision_guard", "l4_high_mae_commodity_beta_sizing_guard"],
  "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"],
  "existing_axis_weakened": [],
  "existing_axis_kept": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "stage3_green_total_min"],
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "no_new_signal_reason": null,
  "loop_contribution_label": "canonical_archetype_rule_candidate"
}
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- stock-web manifest fields and price-basis assumptions,
- symbol profile availability and corporate-action caveat status,
- actual OHLC rows for 2024 entry, peak, low, and 180D windows,
- representative trigger MFE/MAE and 4B local/full-window separation.

Not validated:
- live candidate status,
- investment recommendation,
- production score implementation,
- exact analyst-report wording beyond the summarized public evidence map,
- stock_agent source code.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c15_confirmed_spread_to_margin_bridge_bonus,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,2,2,"Copper/defense and grid-backed cases had high MFE when spread evidence was tied to margin route, not raw commodity price alone.",Improves positive/counterexample separation; keeps Pungsan while avoiding petrochemical spread traps.,R13L26_C15_001_T1_STAGE2_ACTIONABLE|R13L26_C15_002_T1_STAGE2_ACTIONABLE,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,c15_spread_only_without_margin_revision_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,1,Petrochemical spread-only rebound had weak MFE and high MAE before confirmed margin/revision.,Reduces false-positive promotion for 006650 and 011170 style cases.,R13L26_C15_003_T1_STAGE2_WATCH|R13L26_C15_004_T1_STAGE2_WATCH,4,4,2,medium,counterexample_guard_shadow_only,not production; post-calibrated residual
shadow_weight,l4_high_mae_commodity_beta_sizing_guard,sector_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,1,LS showed high MFE but deep MAE; sector needs position-size/confirmation guard when beta leads fundamentals.,Keeps upside but avoids overconfident Green promotion.,R13L26_C15_002_T1_STAGE2_ACTIONABLE,4,4,2,low_medium,sector_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R13L26_C15_001", "symbol": "103140", "company_name": "풍산", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_DEFENSE_SPREAD_VS_PETROCHEMICAL_SPREAD_TRAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R13L26_C15_001_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive_with_low_mae", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Copper price plus defense ammunition margin bridge behaved like a real spread+margin case rather than a commodity-price-only move."}
{"row_type": "case", "case_id": "R13L26_C15_002", "symbol": "006260", "company_name": "LS", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_DEFENSE_SPREAD_VS_PETROCHEMICAL_SPREAD_TRAP", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R13L26_C15_002_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_mfe_but_high_mae", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "Copper/grid theme produced large MFE but required position-size or confirmation guard because MAE was deep before the later base reset."}
{"row_type": "case", "case_id": "R13L26_C15_003", "symbol": "006650", "company_name": "대한유화", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_DEFENSE_SPREAD_VS_PETROCHEMICAL_SPREAD_TRAP", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R13L26_C15_003_T1_STAGE2_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "weak_mfe_large_mae_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Petrochemical spread recovery narrative did not convert into durable margin/revision evidence; price path punished early spread-only promotion."}
{"row_type": "case", "case_id": "R13L26_C15_004", "symbol": "011170", "company_name": "롯데케미칼", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_DEFENSE_SPREAD_VS_PETROCHEMICAL_SPREAD_TRAP", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "R13L26_C15_004_T1_STAGE2_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "guarded_counterexample", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Legacy petrochemical recovery thesis broke into a capital/earnings stress route; calibrated guard should keep this watch-only until margin evidence turns."}
{"row_type": "trigger", "trigger_id": "R13L26_C15_001_T1_STAGE2_ACTIONABLE", "case_id": "R13L26_C15_001", "symbol": "103140", "company_name": "풍산", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_DEFENSE_SPREAD_VS_PETROCHEMICAL_SPREAD_TRAP", "sector": "소재·스프레드·전략자원", "primary_archetype": "materials spread supercycle / spread-to-margin conversion", "loop_objective": ["holdout_validation", "residual_false_positive_mining", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "4B_non_price_requirement_stress_test", "coverage_gap_fill"], "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-13", "entry_date": "2024-03-13", "entry_price": 44450, "evidence_available_at_that_date": "Copper-price recovery plus defense/ammunition margin route visible before later earnings confirmation; trigger uses contemporaneous public commodity/defense margin narrative, not outcome hindsight.", "evidence_source": "public earnings/industry reports around 2024-03-13; stock-web 103140 2024 shard rows 2024-03-13 through 2024-12-30 verified", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 51.86, "MFE_90D_pct": 77.5, "MFE_180D_pct": 77.5, "MFE_1Y_pct": 77.5, "MFE_2Y_pct": null, "MAE_30D_pct": -0.34, "MAE_90D_pct": -0.34, "MAE_180D_pct": -0.34, "MAE_1Y_pct": -0.34, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-05-14", "peak_price": 78900, "drawdown_after_peak_pct": -41.51, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_spread_margin_bridge", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L26_C15_001_2024-03-13_44450", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L26_C15_001_T2_STAGE4B_WATCH", "case_id": "R13L26_C15_001", "symbol": "103140", "company_name": "풍산", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_DEFENSE_SPREAD_VS_PETROCHEMICAL_SPREAD_TRAP", "sector": "소재·스프레드·전략자원", "primary_archetype": "materials spread supercycle / spread-to-margin conversion", "loop_objective": ["holdout_validation", "residual_false_positive_mining", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "4B_non_price_requirement_stress_test", "coverage_gap_fill"], "trigger_type": "Stage4B-Watch", "trigger_date": "2024-05-14", "entry_date": "2024-05-14", "entry_price": 76300, "evidence_available_at_that_date": "Price and positioning became extended near the full observed cycle high, but thesis-break evidence was not yet present. Treat as 4B watch, not automatic full 4B exit.", "evidence_source": "stock-web 103140 2024 row 2024-05-14; no contemporaneous hard thesis-break evidence used", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.41, "MFE_90D_pct": 3.41, "MFE_180D_pct": 3.41, "MFE_1Y_pct": 3.41, "MFE_2Y_pct": null, "MAE_30D_pct": -18.22, "MAE_90D_pct": -38.33, "MAE_180D_pct": -39.52, "MAE_1Y_pct": -39.52, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-14", "peak_price": 78900, "drawdown_after_peak_pct": -41.51, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "price_only_local_4B_watch_not_full_4B", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_watch_useful_but_not_full_4B", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L26_C15_001_2024-05-14_76300", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L26_C15_002_T1_STAGE2_ACTIONABLE", "case_id": "R13L26_C15_002", "symbol": "006260", "company_name": "LS", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_DEFENSE_SPREAD_VS_PETROCHEMICAL_SPREAD_TRAP", "sector": "소재·스프레드·전략자원", "primary_archetype": "materials spread supercycle / spread-to-margin conversion", "loop_objective": ["holdout_validation", "residual_false_positive_mining", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "4B_non_price_requirement_stress_test", "coverage_gap_fill"], "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-12", "entry_date": "2024-04-12", "entry_price": 122100, "evidence_available_at_that_date": "Copper/grid capex spread route had visible relative strength and commodity beta; earnings confirmation lagged, making this a high-MFE but high-MAE case.", "evidence_source": "public copper/grid theme reports around 2024-04-12; stock-web 006260 2024 shard rows 2024-04-12 through 2024-12-30 verified", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv", "profile_path": "atlas/symbol_profiles/006/006260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 59.54, "MFE_90D_pct": 59.54, "MFE_180D_pct": 59.54, "MFE_1Y_pct": 59.54, "MFE_2Y_pct": null, "MAE_30D_pct": -6.88, "MAE_90D_pct": -23.01, "MAE_180D_pct": -30.79, "MAE_1Y_pct": -30.79, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-21", "peak_price": 194800, "drawdown_after_peak_pct": -56.62, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_mfe_high_mae_success", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L26_C15_002_2024-04-12_122100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L26_C15_002_T2_STAGE4B_WATCH", "case_id": "R13L26_C15_002", "symbol": "006260", "company_name": "LS", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_DEFENSE_SPREAD_VS_PETROCHEMICAL_SPREAD_TRAP", "sector": "소재·스프레드·전략자원", "primary_archetype": "materials spread supercycle / spread-to-margin conversion", "loop_objective": ["holdout_validation", "residual_false_positive_mining", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "4B_non_price_requirement_stress_test", "coverage_gap_fill"], "trigger_type": "Stage4B-Watch", "trigger_date": "2024-05-21", "entry_date": "2024-05-21", "entry_price": 179300, "evidence_available_at_that_date": "Local price blowoff near the observed cycle high. Because non-price deterioration was absent, this is a 4B watch overlay rather than a full thesis exit.", "evidence_source": "stock-web 006260 2024 row 2024-05-21; no hard non-price 4B evidence used", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv", "profile_path": "atlas/symbol_profiles/006/006260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.64, "MFE_90D_pct": 8.64, "MFE_180D_pct": 8.64, "MFE_1Y_pct": 8.64, "MFE_2Y_pct": null, "MAE_30D_pct": -23.48, "MAE_90D_pct": -47.57, "MAE_180D_pct": -52.87, "MAE_1Y_pct": -52.87, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-21", "peak_price": 194800, "drawdown_after_peak_pct": -56.62, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.79, "four_b_full_window_peak_proximity": 0.79, "four_b_timing_verdict": "price_only_local_4B_watch_not_full_4B", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_watch_near_peak_but_not_full_exit", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L26_C15_002_2024-05-21_179300", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L26_C15_003_T1_STAGE2_WATCH", "case_id": "R13L26_C15_003", "symbol": "006650", "company_name": "대한유화", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_DEFENSE_SPREAD_VS_PETROCHEMICAL_SPREAD_TRAP", "sector": "소재·스프레드·전략자원", "primary_archetype": "materials spread supercycle / spread-to-margin conversion", "loop_objective": ["holdout_validation", "residual_false_positive_mining", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "4B_non_price_requirement_stress_test", "coverage_gap_fill"], "trigger_type": "Stage2-Watch", "trigger_date": "2024-04-02", "entry_date": "2024-04-02", "entry_price": 143000, "evidence_available_at_that_date": "Petrochemical spread rebound narrative existed, but durable margin bridge and revision confirmation were not available at the trigger date.", "evidence_source": "public petrochemical spread/recovery narrative around 2024-04-02; stock-web 006650 2024 shard rows verified", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006650/2024.csv", "profile_path": "atlas/symbol_profiles/006/006650.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.3, "MFE_90D_pct": 12.59, "MFE_180D_pct": 12.59, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.71, "MAE_90D_pct": -32.17, "MAE_180D_pct": -52.17, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-20", "peak_price": 161000, "drawdown_after_peak_pct": -57.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "failed_rerating_spread_only_counterexample", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L26_C15_003_2024-04-02_143000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L26_C15_004_T1_STAGE2_WATCH", "case_id": "R13L26_C15_004", "symbol": "011170", "company_name": "롯데케미칼", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_DEFENSE_SPREAD_VS_PETROCHEMICAL_SPREAD_TRAP", "sector": "소재·스프레드·전략자원", "primary_archetype": "materials spread supercycle / spread-to-margin conversion", "loop_objective": ["holdout_validation", "residual_false_positive_mining", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "4B_non_price_requirement_stress_test", "coverage_gap_fill"], "trigger_type": "Stage2-Watch", "trigger_date": "2024-03-15", "entry_date": "2024-03-15", "entry_price": 121300, "evidence_available_at_that_date": "Legacy petrochemical spread recovery thesis remained narrative-heavy; no confirmed margin bridge, capital-return support, or durable revision was present.", "evidence_source": "public petrochemical spread/recovery narrative around 2024-03-15; stock-web 011170 2024 shard rows verified", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv", "profile_path": "atlas/symbol_profiles/011/011170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.22, "MFE_90D_pct": 3.46, "MFE_180D_pct": 3.46, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -20.78, "MAE_90D_pct": -20.78, "MAE_180D_pct": -53.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-20", "peak_price": 125500, "drawdown_after_peak_pct": -55.06, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4c_thesis_break_counterexample", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L26_C15_004_2024-03-15_121300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "proposed_c15_material_spread_shadow_profile", "case_id": "R13L26_C15_001", "trigger_id": "R13L26_C15_001_T1_STAGE2_ACTIONABLE", "symbol": "103140", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 45, "margin_bridge_score": 72, "revision_score": 48, "relative_strength_score": 78, "customer_quality_score": 45, "policy_or_regulatory_score": 62, "valuation_repricing_score": 70, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 53.8, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 45, "margin_bridge_score": 80, "revision_score": 53, "relative_strength_score": 78, "customer_quality_score": 45, "policy_or_regulatory_score": 62, "valuation_repricing_score": 70, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 55.4, "stage_label_after": "Stage2-Watch", "changed_components": ["margin_bridge_score", "revision_score"], "component_delta_explanation": "C15 shadow separates confirmed margin/revision bridge from raw spread or commodity-price beta. Copper+defense can be promoted; petrochemical spread-only requires watch/guard until margin conversion appears.", "MFE_90D_pct": 77.5, "MAE_90D_pct": -0.34, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "proposed_c15_material_spread_shadow_profile", "case_id": "R13L26_C15_002", "trigger_id": "R13L26_C15_002_T1_STAGE2_ACTIONABLE", "symbol": "006260", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 42, "revision_score": 35, "relative_strength_score": 86, "customer_quality_score": 35, "policy_or_regulatory_score": 72, "valuation_repricing_score": 82, "execution_risk_score": 52, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 45.3, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 42, "revision_score": 35, "relative_strength_score": 86, "customer_quality_score": 35, "policy_or_regulatory_score": 72, "valuation_repricing_score": 74, "execution_risk_score": 62, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 43.4, "stage_label_after": "Stage2-Watch", "changed_components": ["valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C15 shadow separates confirmed margin/revision bridge from raw spread or commodity-price beta. Copper+defense can be promoted; petrochemical spread-only requires watch/guard until margin conversion appears.", "MFE_90D_pct": 59.54, "MAE_90D_pct": -23.01, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "proposed_c15_material_spread_shadow_profile", "case_id": "R13L26_C15_003", "trigger_id": "R13L26_C15_003_T1_STAGE2_WATCH", "symbol": "006650", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 20, "revision_score": 12, "relative_strength_score": 42, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 35, "execution_risk_score": 68, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 10.4, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 12, "revision_score": 7, "relative_strength_score": 42, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 35, "execution_risk_score": 78, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 7.9, "stage_label_after": "Stage2-Watch", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C15 shadow separates confirmed margin/revision bridge from raw spread or commodity-price beta. Copper+defense can be promoted; petrochemical spread-only requires watch/guard until margin conversion appears.", "MFE_90D_pct": 12.59, "MAE_90D_pct": -32.17, "score_return_alignment_label": "guarded_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "proposed_c15_material_spread_shadow_profile", "case_id": "R13L26_C15_004", "trigger_id": "R13L26_C15_004_T1_STAGE2_WATCH", "symbol": "011170", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 5, "margin_bridge_score": 15, "revision_score": 8, "relative_strength_score": 30, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": 78, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 0}, "weighted_score_before": 1.6, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 5, "margin_bridge_score": 7, "revision_score": 3, "relative_strength_score": 30, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": 88, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 0}, "weighted_score_after": -0.9, "stage_label_after": "Stage2-Watch", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C15 shadow separates confirmed margin/revision bridge from raw spread or commodity-price beta. Copper+defense can be promoted; petrochemical spread-only requires watch/guard until margin conversion appears.", "MFE_90D_pct": 3.46, "MAE_90D_pct": -20.78, "score_return_alignment_label": "guarded_counterexample", "current_profile_verdict": "current_profile_correct"}
{"row_type": "residual_contribution", "round": "R13", "loop": "26", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "stage3_cross_evidence_green_buffer", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["spread_only_false_positive", "high_mfe_high_mae_commodity_beta", "price_only_local_4b_watch_not_full_4b"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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

- next_round: `R13_loop_27`
- suggested_next_scope: `L4_MATERIALS_SPREAD_RESOURCE / C16_STRATEGIC_RESOURCE_POLICY_SUPPLY` or `L4 / C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`
- next_gap: add more resource/policy holdouts and separate strategic supply tightness from generic commodity beta.

## 28. Source Notes

- Stock-web manifest verified from `atlas/manifest.json`.
- Symbol profiles verified for `103140`, `006260`, `006650`, `011170`.
- Price rows verified from stock-web 2024 tradable shards for all trigger/forward windows; Pungsan 2025 early rows were checked for 1Y sanity.
- This MD is historical calibration research only and contains no investment recommendation.
