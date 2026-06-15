# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 97
selected_priority_bucket: Priority 0
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER
deep_sub_archetype_id: C14_DEEP_2024_2025_EV_DEMAND_HARD_4C_VS_RECOVERY_MFE_EXCEPTION_BY_MATERIAL_CELL_MODULE_ROUTE
loop_objective: coverage_gap_fill + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery
primary_price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
auto_trading_allowed: false
```

This loop adds 6 new independent cases, 3 counterexamples, and 3 residual errors for L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.  It is not a live watchlist and not an investment recommendation.

## 1. Current Calibrated Profile Assumption

- current_default_profile_proxy: `e2r_2_1_stock_web_calibrated_proxy`
- rollback_reference_profile_id: `e2r_2_0_baseline_reference`
- already-applied global axes tested, not blindly repeated: `stage2_actionable_evidence_bonus`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, `hard_4c_thesis_break_routes_to_4c`.
- New residual question: in C14, when should EV-demand slowdown become hard Stage4C, and when should it stay as local Stage4B watch because a recovery-MFE band remains visible?

## 2. Round / Large Sector / Canonical Archetype Scope

C14 maps to `R3 / L3_BATTERY_EV_GREEN_MOBILITY`.  This file does not use R13 because the scope is not cross-archetype red-team; it is a C14 sector/canonical residual calibration file.

## 3. Previous Coverage / Duplicate Avoidance Check

The No-Repeat Index lists `C14_EV_DEMAND_SLOWDOWN_4B_4C` as Priority 0 with 11 representative rows, needing 19 rows to reach 30 and 39 rows to reach 50.  Local earlier C14 loop95 and loop96 added 12 representative/usable rows in this session, so C14 is still under the 30-row stability zone before this file.

Prior local C14 symbols avoided as new-symbol claims: `247540, 003670, 393890, 066970, 373220, 361610, 278280, 005070, 348370, 006400, 051910, 020150, 093370, 121600, 137400, 011790, 222080`.  `011790` appears once as a deliberately reused symbol, but the entry date, trigger family, and reuse reason are explicitly changed to a 2025 recovery-band exception.

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{"calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "manifest_max_date": "2026-02-20", "manifest_path": "atlas/manifest.json", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "raw_row_count": 15214118, "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "row_type": "price_source_validation", "schema_path": "atlas/schema.json", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "symbol_count": 5414, "tradable_row_count": 14354401, "universe_path": "atlas/universe/all_symbols.csv", "validation_status": "usable_for_historical_calibration"}
```

Manifest and schema checks used by this file:

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| max_date | 2026-02-20 |
| price_adjustment_status | raw_unadjusted_marcap |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |

## 5. Historical Eligibility Gate

All `row_type="trigger"` rows below have: entry date in a Stock-Web tradable shard, close-based entry price, 180 forward trading-day path, canonical 30/90/180D MFE and MAE fields, and no 180D corporate-action contamination by profile-date screen.

| symbol | company_name | profile_path | last_date | trading_day_count | corp_action_count | corp_action_dates | 180D_window_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 006110 | 삼아알미늄 | atlas/symbol_profiles/006/006110.json | 2026-02-20 | 7041 | 5 | ["2000-10-16", "2000-11-14", "2007-05-04", "2011-04-26", "2023-02-09"] | clean_180D_window_after_profile_corporate_action_date_check |
| 005420 | 코스모화학 | atlas/symbol_profiles/005/005420.json | 2026-02-20 | 7697 | 7 | ["1998-12-21", "2000-04-11", "2000-08-14", "2001-09-28", "2003-06-18", "2004-05-06", "2019-12-24"] | clean_180D_window_after_profile_corporate_action_date_check |
| 336370 | 솔루스첨단소재 | atlas/symbol_profiles/336/336370.json | 2026-02-20 | 1557 | 2 | ["2024-01-08", "2024-01-30"] | clean_180D_window_after_profile_corporate_action_date_check |
| 096770 | SK이노베이션 | atlas/symbol_profiles/096/096770.json | 2026-02-20 | 4579 | 1 | ["2024-11-20"] | clean_180D_window_after_profile_corporate_action_date_check |
| 417200 | LS머트리얼즈 | atlas/symbol_profiles/417/417200.json | 2026-02-20 | 531 | 0 | [] | clean_180D_window_after_profile_corporate_action_date_check |
| 078600 | 대주전자재료 | atlas/symbol_profiles/078/078600.json | 2026-02-20 | 5230 | 0 | [] | clean_180D_window_after_profile_corporate_action_date_check |
| 011790 | SKC | atlas/symbol_profiles/011/011790.json | 2026-02-20 | 7105 | 2 | ["1998-01-03", "2001-12-21"] | clean_180D_window_after_profile_corporate_action_date_check |


## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine_archetype_id | deep_sub_archetype_id | compression logic |
|---|---|---|---|
| C14_EV_DEMAND_SLOWDOWN_4B_4C | C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER | C14_DEEP_2024_2025_EV_DEMAND_HARD_4C_VS_RECOVERY_MFE_EXCEPTION_BY_MATERIAL_CELL_MODULE_ROUTE | Battery material/cell/module names exposed to EV-demand reset are compressed into one C14 rule: hard 4C only after utilization/call-off/margin break is confirmed and no recovery-MFE band is visible. |

## 7. Case Selection Summary

| case_id | symbol | company_name | trigger_type | case_role | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C14-R3L97-01-006110 | 006110 | 삼아알미늄 | Stage4C | hard_4c_success | 2024-10-31 | 51000 | 1.18 | -31.27 | 1.18 | -46.96 | 1.18 | -65.59 | current_profile_correct |
| C14-R3L97-02-005420 | 005420 | 코스모화학 | Stage4C | hard_4c_success | 2024-04-30 | 32150 | 3.11 | -13.84 | 3.11 | -48.68 | 3.11 | -54.28 | current_profile_correct |
| C14-R3L97-03-336370 | 336370 | 솔루스첨단소재 | Stage4C | hard_4c_success | 2024-07-31 | 15200 | 3.95 | -26.32 | 3.95 | -50.0 | 3.95 | -55.59 | current_profile_correct |
| C14-R3L97-04-096770 | 096770 | SK이노베이션 | Stage4C | hard_4c_success | 2025-01-31 | 127500 | 9.96 | -5.88 | 9.96 | -36.63 | 9.96 | -36.63 | current_profile_correct_but_requires_post_corporate_action_entry |
| C14-R3L97-05-417200 | 417200 | LS머트리얼즈 | Stage4B | 4B_watch_recovery_exception | 2025-03-31 | 10640 | 9.59 | -14.94 | 15.32 | -14.94 | 48.5 | -14.94 | current_profile_false_positive_if_hard_4c_without_recovery_band |
| C14-R3L97-06-078600 | 078600 | 대주전자재료 | Stage4B | 4B_watch_recovery_exception | 2024-04-30 | 93900 | 74.01 | -2.88 | 74.01 | -4.79 | 74.01 | -24.39 | current_profile_false_positive_if_hard_4c_without_recovery_band |
| C14-R3L97-07-011790 | 011790 | SKC | Stage4B | 4B_watch_reused_symbol_new_trigger_family | 2025-03-31 | 102900 | 5.44 | -16.23 | 15.45 | -16.52 | 34.6 | -16.52 | current_profile_false_positive_if_hard_4c_without_recovery_band |


## 8. Positive vs Counterexample Balance

- positive_case_count: `4`
- counterexample_count: `3`
- Stage4B watch / recovery exception count: `3`
- Stage4C hard-break count: `4`
- current_profile_error_count: `3`

Interpretation: the hard-break group averaged MFE90 `4.55%` and MAE90 `-45.57%`.  The recovery-exception group averaged MFE90 `34.93%` and MAE90 `-12.08%`.  That split is exactly the C14 residual: the same EV-demand headline becomes a different state depending on whether recovery MFE survives before non-price break confirmation.

## 9. Evidence Source Map

| symbol | evidence_source_status | evidence_family | trigger_family | promotion note |
|---|---|---|---|---|
| 006110 | source_proxy_only_url_repair_pending | aluminum_foil_ev_battery_material_margin_reset | late_2024_battery_foil_demand_margin_break | promotion_blocked_until_url_repair=true |
| 005420 | source_proxy_only_url_repair_pending | battery_precursor_material_downcycle | spring_2024_precursor_material_margin_break | promotion_blocked_until_url_repair=true |
| 336370 | source_proxy_only_url_repair_pending | copper_foil_ev_demand_margin_pressure | mid_2024_copper_foil_demand_reset | promotion_blocked_until_url_repair=true |
| 096770 | source_proxy_only_url_repair_pending | cellmaker_loss_demand_reset_and_balance_sheet_absorption | post_merger_battery_cell_loss_and_ev_demand_reset | promotion_blocked_until_url_repair=true |
| 417200 | source_proxy_only_url_repair_pending | green_mobility_power_module_recovery_band | 2025_power_module_capacitor_recovery_mfe_exception | promotion_blocked_until_url_repair=true |
| 078600 | source_proxy_only_url_repair_pending | silicon_anode_capacity_customer_optionality | spring_2024_silicon_anode_recovery_band_exception | promotion_blocked_until_url_repair=true |
| 011790 | source_proxy_only_url_repair_pending | copper_foil_parent_mix_recovery_exception | 2025_copper_foil_recovery_band_after_prior_2024_reset | promotion_blocked_until_url_repair=true |


## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | manifest_max_date | price_basis | adjustment |
|---|---|---|---|---|---|
| 006110 | atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv; atlas/ohlcv_tradable_by_symbol_year/006/006110/2025.csv | atlas/symbol_profiles/006/006110.json | 2026-02-20 | tradable_raw | raw_unadjusted_marcap |
| 005420 | atlas/ohlcv_tradable_by_symbol_year/005/005420/2024.csv; atlas/ohlcv_tradable_by_symbol_year/005/005420/2025.csv | atlas/symbol_profiles/005/005420.json | 2026-02-20 | tradable_raw | raw_unadjusted_marcap |
| 336370 | atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv; atlas/ohlcv_tradable_by_symbol_year/336/336370/2025.csv | atlas/symbol_profiles/336/336370.json | 2026-02-20 | tradable_raw | raw_unadjusted_marcap |
| 096770 | atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv; atlas/ohlcv_tradable_by_symbol_year/096/096770/2025.csv | atlas/symbol_profiles/096/096770.json | 2026-02-20 | tradable_raw | raw_unadjusted_marcap |
| 417200 | atlas/ohlcv_tradable_by_symbol_year/417/417200/2024.csv; atlas/ohlcv_tradable_by_symbol_year/417/417200/2025.csv; atlas/ohlcv_tradable_by_symbol_year/417/417200/2026.csv | atlas/symbol_profiles/417/417200.json | 2026-02-20 | tradable_raw | raw_unadjusted_marcap |
| 078600 | atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv; atlas/ohlcv_tradable_by_symbol_year/078/078600/2025.csv | atlas/symbol_profiles/078/078600.json | 2026-02-20 | tradable_raw | raw_unadjusted_marcap |
| 011790 | atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv; atlas/ohlcv_tradable_by_symbol_year/011/011790/2025.csv | atlas/symbol_profiles/011/011790.json | 2026-02-20 | tradable_raw | raw_unadjusted_marcap |


## 11. Case-by-Case Trigger Grid

| case_id | symbol | company_name | trigger_type | case_role | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C14-R3L97-01-006110 | 006110 | 삼아알미늄 | Stage4C | hard_4c_success | 2024-10-31 | 51000 | 1.18 | -46.96 | 1.18 | -65.59 | current_profile_correct |
| C14-R3L97-02-005420 | 005420 | 코스모화학 | Stage4C | hard_4c_success | 2024-04-30 | 32150 | 3.11 | -48.68 | 3.11 | -54.28 | current_profile_correct |
| C14-R3L97-03-336370 | 336370 | 솔루스첨단소재 | Stage4C | hard_4c_success | 2024-07-31 | 15200 | 3.95 | -50.0 | 3.95 | -55.59 | current_profile_correct |
| C14-R3L97-04-096770 | 096770 | SK이노베이션 | Stage4C | hard_4c_success | 2025-01-31 | 127500 | 9.96 | -36.63 | 9.96 | -36.63 | current_profile_correct_but_requires_post_corporate_action_entry |
| C14-R3L97-05-417200 | 417200 | LS머트리얼즈 | Stage4B | 4B_watch_recovery_exception | 2025-03-31 | 10640 | 15.32 | -14.94 | 48.5 | -14.94 | current_profile_false_positive_if_hard_4c_without_recovery_band |
| C14-R3L97-06-078600 | 078600 | 대주전자재료 | Stage4B | 4B_watch_recovery_exception | 2024-04-30 | 93900 | 74.01 | -4.79 | 74.01 | -24.39 | current_profile_false_positive_if_hard_4c_without_recovery_band |
| C14-R3L97-07-011790 | 011790 | SKC | Stage4B | 4B_watch_reused_symbol_new_trigger_family | 2025-03-31 | 102900 | 15.45 | -16.52 | 34.6 | -16.52 | current_profile_false_positive_if_hard_4c_without_recovery_band |


## 12. Trigger-Level OHLC Backtest Tables

| case_id | symbol | entry_date | entry_price | peak_30D | min_30D | peak_90D | min_90D | peak_180D | min_180D | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C14-R3L97-01-006110 | 006110 | 2024-10-31 | 51000 | 2024-11-04@51600 | 2024-11-15@35050 | 2024-11-04@51600 | 2025-03-05@27050 | 2024-11-04@51600 | 2025-07-01@17550 | -65.99 |
| C14-R3L97-02-005420 | 005420 | 2024-04-30 | 32150 | 2024-06-11@33150 | 2024-05-24@27700 | 2024-06-11@33150 | 2024-08-05@16500 | 2024-06-11@33150 | 2025-01-02@14700 | -55.66 |
| C14-R3L97-03-336370 | 336370 | 2024-07-31 | 15200 | 2024-08-01@15800 | 2024-09-10@11200 | 2024-08-01@15800 | 2024-12-10@7600 | 2024-08-01@15800 | 2025-04-09@6750 | -57.28 |
| C14-R3L97-04-096770 | 096770 | 2025-01-31 | 127500 | 2025-03-13@140200 | 2025-02-10@120000 | 2025-03-13@140200 | 2025-05-23@80800 | 2025-03-13@140200 | 2025-05-23@80800 | -42.37 |
| C14-R3L97-05-417200 | 417200 | 2025-03-31 | 10640 | 2025-05-15@11660 | 2025-04-09@9050 | 2025-06-25@12270 | 2025-04-09@9050 | 2025-11-04@15800 | 2025-04-09@9050 | -28.61 |
| C14-R3L97-06-078600 | 078600 | 2024-04-30 | 93900 | 2024-06-12@163400 | 2024-05-07@91200 | 2024-06-12@163400 | 2024-09-09@89400 | 2024-06-12@163400 | 2025-01-02@71000 | -56.55 |
| C14-R3L97-07-011790 | 011790 | 2025-03-31 | 102900 | 2025-05-14@108500 | 2025-04-09@86200 | 2025-06-26@118800 | 2025-05-23@85900 | 2025-11-04@138500 | 2025-05-23@85900 | -26.5 |


## 13. Current Calibrated Profile Stress Test

| case_id | symbol | stage_before | score_before | stage_after | score_after | MFE_90D_pct | MAE_90D_pct | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C14-R3L97-01-006110 | 006110 | Stage4B-watch_or_late_4C_proxy | 74 | Stage4C | 66 | 1.18 | -46.96 | hard_4c_aligned_low_mfe_high_mae |
| C14-R3L97-02-005420 | 005420 | Stage4B-watch_or_late_4C_proxy | 74 | Stage4C | 66 | 3.11 | -48.68 | hard_4c_aligned_low_mfe_high_mae |
| C14-R3L97-03-336370 | 336370 | Stage4B-watch_or_late_4C_proxy | 74 | Stage4C | 66 | 3.95 | -50.0 | hard_4c_aligned_low_mfe_high_mae |
| C14-R3L97-04-096770 | 096770 | Stage4B-watch_or_late_4C_proxy | 71 | Stage4C | 64 | 9.96 | -36.63 | hard_4c_aligned_low_mfe_high_mae |
| C14-R3L97-05-417200 | 417200 | Stage4C_if_macro_slowdown_overrouted | 72 | Stage4B-watch_not_full_4C | 77 | 15.32 | -14.94 | hard_4c_would_be_false_positive_recovery_mfe_present |
| C14-R3L97-06-078600 | 078600 | Stage4C_if_macro_slowdown_overrouted | 72 | Stage4B-watch_not_full_4C | 77 | 74.01 | -4.79 | hard_4c_would_be_false_positive_recovery_mfe_present |
| C14-R3L97-07-011790 | 011790 | Stage4C_if_macro_slowdown_overrouted | 72 | Stage4B-watch_not_full_4C | 74 | 15.45 | -16.52 | hard_4c_would_be_false_positive_recovery_mfe_present |


Current profile stress-test answer:

1. It is directionally correct for low-MFE material/cell hard breaks (`006110`, `005420`, `336370`, `096770`).
2. It is still vulnerable to false hard-4C routing for names that retain a recovery-MFE band before confirmed non-price thesis break (`417200`, `078600`, and reused-symbol/new-trigger `011790`).
3. The Stage2 bonus is not the key residual here; the residual lives in the Stage4B/4C branch.
4. Yellow/Green thresholds are not relaxed.
5. Price-only blowoff guard remains appropriate.
6. Full 4B non-price requirement remains appropriate.
7. Hard 4C routing should be narrowed by a C14 recovery-band exception filter.

## 14. Stage2 / Yellow / Green Comparison

No Stage3-Green row is created here.  These are Stage4B/Stage4C timing rows.  Therefore `green_lateness_ratio = not_applicable_no_confirmed_Stage3_Green_trigger` for all trigger rows.

## 15. 4B Local vs Full-window Timing Audit

- Stage4B watch rows: `417200`, `078600`, `011790`.
- These rows should not become full hard 4C merely because EV-demand headlines or local price weakness are visible.
- The full-window result shows large remaining MFE bands: `417200` MFE180 `48.50%`, `078600` MFE180 `74.01%`, `011790` MFE180 `34.60%`.
- Therefore their `four_b_timing_verdict` is `price_only_local_4B_watch_not_full_4C`.

## 16. 4C Protection Audit

- Stage4C success rows: `006110`, `005420`, `336370`, `096770`.
- Their average MFE180 is `4.55%`; average MAE180 is `-53.02%`.
- This supports hard 4C only for confirmed material/cell margin/utilization/call-off break with absent recovery band.
- `096770` is intentionally entered after the Stock-Web corporate-action candidate date `2024-11-20`; the 180D forward window starts at `2025-01-31` and is treated as clean.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
candidate_rule = Do not route EV-demand slowdown into hard 4C solely from macro/price weakness. Require utilization/call-off/margin break and absent recovery-MFE band; otherwise keep Stage4B watch.
sector_specific_rule_candidate = true
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
new_axis_proposed = C14_hard_4c_requires_utilization_calloff_margin_break_plus_absent_recovery_mfe_band_before_Stage4C
existing_axis_strengthened = hard_4c_confirmation, local_4b_watch_guard, full_4b_requires_non_price_evidence
existing_axis_weakened = hard_4c_thesis_break_routes_to_4c_when_only_macro_ev_slowdown_or_price_weakness_is_present
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current proxy | hard 4C may fire on EV-demand label once thesis-break proxy appears | 7 | 17.57 | -31.22 | 25.04 | -38.28 | 0.43 | 0 | mixed: correct on material/cell hard breaks, false-positive on recovery-band exceptions |
| P0b_e2r_2_0_baseline_reference | rollback reference | weaker 4C routing and looser price-led reactions | 7 | 17.57 | -31.22 | 25.04 | -38.28 | 0.57 | 2 | weaker protection; misses some low-MFE hard breaks |
| P1_L3_sector_candidate | sector shadow | EV slowdown needs utilization/call-off/margin confirmation, but not all green-mobility names are hard 4C | 7 | 17.57 | -31.22 | 25.04 | -38.28 | 0.14 | 0 | improved split between hard breaks and recovery exceptions |
| P2_C14_canonical_candidate | canonical shadow | add recovery-MFE exception filter to C14 hard-4C route | 7 | 17.57 | -31.22 | 25.04 | -38.28 | 0.00 | 0 | best alignment for this loop |
| P3_counterexample_guard_profile | guard profile | hold Stage4B watch if recovery MFE appears before non-price break | 3 | 34.93 | -12.08 | 52.37 | -18.62 | 0.00 | 0 | prevents false hard-4C on exception group |


## 20. Score-Return Alignment Matrix

| case_id | symbol | stage_before | score_before | stage_after | score_after | alignment |
| --- | --- | --- | --- | --- | --- | --- |
| C14-R3L97-01-006110 | 006110 | Stage4B-watch_or_late_4C_proxy | 74 | Stage4C | 66 | hard_4c_aligned_low_mfe_high_mae |
| C14-R3L97-02-005420 | 005420 | Stage4B-watch_or_late_4C_proxy | 74 | Stage4C | 66 | hard_4c_aligned_low_mfe_high_mae |
| C14-R3L97-03-336370 | 336370 | Stage4B-watch_or_late_4C_proxy | 74 | Stage4C | 66 | hard_4c_aligned_low_mfe_high_mae |
| C14-R3L97-04-096770 | 096770 | Stage4B-watch_or_late_4C_proxy | 71 | Stage4C | 64 | hard_4c_aligned_low_mfe_high_mae |
| C14-R3L97-05-417200 | 417200 | Stage4C_if_macro_slowdown_overrouted | 72 | Stage4B-watch_not_full_4C | 77 | hard_4c_would_be_false_positive_recovery_mfe_present |
| C14-R3L97-06-078600 | 078600 | Stage4C_if_macro_slowdown_overrouted | 72 | Stage4B-watch_not_full_4C | 77 | hard_4c_would_be_false_positive_recovery_mfe_present |
| C14-R3L97-07-011790 | 011790 | Stage4C_if_macro_slowdown_overrouted | 72 | Stage4B-watch_not_full_4C | 74 | hard_4c_would_be_false_positive_recovery_mfe_present |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER | 4 | 3 | 3 | 4 | 6 | 1 | 7 | 7 | 3 | True | True | C14 index 11 -> local-session adjusted 30; need 0 more to 30 / 20 more to 50 |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 1
reused_case_ids: C14-R3L97-07-011790
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 7
tested_existing_calibrated_axes: hard_4c_thesis_break_routes_to_4c, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: hard_4c_false_positive_when_recovery_mfe_band_exists, hard_4c_correct_when_low_mfe_high_mae_material_margin_break, source_proxy_only_blocks_promotion_until_url_repair
new_axis_proposed: C14_hard_4c_requires_utilization_calloff_margin_break_plus_absent_recovery_mfe_band_before_Stage4C
existing_axis_strengthened: hard_4c_confirmation, local_4b_watch_guard, full_4b_requires_non_price_evidence
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_when_only_macro_ev_slowdown_or_price_weakness_is_present
existing_axis_kept: price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Stock-Web tradable raw OHLC rows for the selected entry dates.
- 30/90/180 trading-day MFE and MAE path calculations.
- C14 round/sector/canonical consistency.
- No-repeat local symbol/trigger-family screen.

Non-validation scope:

- This MD does not change production scoring.
- This MD does not open or patch `stock_agent/src/e2r`.
- Evidence URLs are not considered verified; all evidence-source rows are `source_proxy_only` and `promotion_blocked_until_url_repair=true`.
- This MD is not a current stock recommendation or live watchlist.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_recovery_mfe_exception_filter,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Require confirmed utilization/call-off/margin break AND absent recovery-MFE band before hard Stage4C.","Hard 4C rows avg MFE90 4.55 / MAE90 -45.57; exception rows avg MFE90 34.93 / MAE90 -12.08.","C14-R3L97-01-006110-Stage4C-2024-10-31|C14-R3L97-02-005420-Stage4C-2024-04-30|C14-R3L97-03-336370-Stage4C-2024-07-31|C14-R3L97-04-096770-Stage4C-2025-01-31|C14-R3L97-05-417200-Stage4B-2025-03-31|C14-R3L97-06-078600-Stage4B-2024-04-30|C14-R3L97-07-011790-Stage4B-2025-03-31",7,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual; URL repair required before promotion"
```

## 25. Machine-Readable Rows

```jsonl
{"calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "manifest_max_date": "2026-02-20", "manifest_path": "atlas/manifest.json", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "raw_row_count": 15214118, "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "row_type": "price_source_validation", "schema_path": "atlas/schema.json", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "symbol_count": 5414, "tradable_row_count": 14354401, "universe_path": "atlas/universe/all_symbols.csv", "validation_status": "usable_for_historical_calibration"}
{"best_trigger": "Stage4C", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-01-006110", "case_type": "4C_success", "company_name": "삼아알미늄", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "97", "notes": "battery aluminum foil path; hard 4C works when EV demand reset and margin/utilization pressure leave no recovery band", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R3", "row_type": "case", "score_price_alignment": "hard_4c_aligned_low_mfe_high_mae", "symbol": "006110"}
{"best_trigger": "Stage4C", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-02-005420", "case_type": "4C_success", "company_name": "코스모화학", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "97", "notes": "precursor/material route; MFE stayed tiny while MAE expanded across 90D/180D", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R3", "row_type": "case", "score_price_alignment": "hard_4c_aligned_low_mfe_high_mae", "symbol": "005420"}
{"best_trigger": "Stage4C", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-03-336370", "case_type": "4C_success", "company_name": "솔루스첨단소재", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "97", "notes": "post-January corporate-action window is clean; July demand-reset trigger had almost no recovery MFE", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R3", "row_type": "case", "score_price_alignment": "hard_4c_aligned_low_mfe_high_mae", "symbol": "336370"}
{"best_trigger": "Stage4C", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-04-096770", "case_type": "4C_success", "company_name": "SK이노베이션", "current_profile_verdict": "current_profile_correct_but_requires_post_corporate_action_entry", "fine_archetype_id": "C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "97", "notes": "entry after the 2024-11-20 stock-web corporate-action candidate avoids contaminated forward window", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R3", "row_type": "case", "score_price_alignment": "hard_4c_aligned_low_mfe_high_mae", "symbol": "096770"}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-05-417200", "case_type": "false_hard_4c_exception", "company_name": "LS머트리얼즈", "current_profile_verdict": "current_profile_false_positive_if_hard_4c_without_recovery_band", "fine_archetype_id": "C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "97", "notes": "not a hard 4C: recovery MFE appears before non-price thesis break confirmation", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R3", "row_type": "case", "score_price_alignment": "hard_4c_would_be_false_positive_recovery_mfe_present", "symbol": "417200"}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-06-078600", "case_type": "false_hard_4c_exception", "company_name": "대주전자재료", "current_profile_verdict": "current_profile_false_positive_if_hard_4c_without_recovery_band", "fine_archetype_id": "C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "97", "notes": "hard-4C route would have killed a large 30D/90D MFE; keep as 4B watch unless margin/call-off break confirms", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R3", "row_type": "case", "score_price_alignment": "hard_4c_would_be_false_positive_recovery_mfe_present", "symbol": "078600"}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-07-011790", "case_type": "false_hard_4c_exception", "company_name": "SKC", "current_profile_verdict": "current_profile_false_positive_if_hard_4c_without_recovery_band", "fine_archetype_id": "C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "97", "notes": "same symbol as a prior local C14 file, but a new 2025 recovery-band trigger family; independent_evidence_weight is partial", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": "reused_symbol_from_loop96_but_new_2025_recovery_band_trigger_family_not_same_entry_group", "round": "R3", "row_type": "case", "score_price_alignment": "hard_4c_would_be_false_positive_recovery_mfe_present", "symbol": "011790"}
{"MAE_180D_pct": -65.59, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "MAE_30D_pct": -31.27, "MAE_90D_pct": -46.96, "MFE_180D_pct": 1.18, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 1.18, "MFE_90D_pct": 1.18, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-01-006110", "case_role": "hard_4c_success", "company_name": "삼아알미늄", "corporate_action_candidate_dates": ["2000-10-16", "2000-11-14", "2007-05-04", "2011-04-26", "2023-02-09"], "corporate_action_window_status": "clean_180D_window_after_profile_corporate_action_date_check", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C14_DEEP_2024_2025_EV_DEMAND_HARD_4C_VS_RECOVERY_MFE_EXCEPTION_BY_MATERIAL_CELL_MODULE_ROUTE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -65.99, "entry_date": "2024-10-31", "entry_price": 51000, "evidence_available_at_that_date": "source_proxy_only: historical EV demand slowdown / utilization / margin-reset or recovery-band evidence mapped to quarter-end/public-market date; URL repair pending", "evidence_family": "aluminum_foil_ev_battery_material_margin_reset", "evidence_source": "source_proxy_only_url_repair_pending", "evidence_url_pending": true, "fine_archetype_id": "C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER", "forward_window_trading_days": 180, "four_b_evidence_type": ["margin_or_backlog_slowdown", "positioning_overheat", "price_only_local_peak"], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable_hard_4c_path", "four_c_protection_label": "hard_4c_success", "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "97", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery", "notes": "battery aluminum foil path; hard 4C works when EV demand reset and margin/utilization pressure leave no recovery band", "peak_date": "2024-11-04", "peak_price": 51600, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv; atlas/ohlcv_tradable_by_symbol_year/006/006110/2025.csv", "primary_archetype": "ev_demand_slowdown_4b_4c", "profile_path": "atlas/symbol_profiles/006/006110.json", "promotion_blocked_until_url_repair": true, "reuse_reason": null, "round": "R3", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|006110|Stage4C|2024-10-31|late_2024_battery_foil_demand_margin_break", "sector": "battery_ev_green_mobility", "source_proxy_only": true, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken", "utilization_or_margin_break_proxy_required"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "006110", "trigger_date": "2024-10-31", "trigger_family": "late_2024_battery_foil_demand_margin_break", "trigger_id": "C14-R3L97-01-006110-Stage4C-2024-10-31", "trigger_outcome_label": "battery_foil_hard_4c_low_mfe_high_mae", "trigger_type": "Stage4C"}
{"MAE_180D_pct": -54.28, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "MAE_30D_pct": -13.84, "MAE_90D_pct": -48.68, "MFE_180D_pct": 3.11, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 3.11, "MFE_90D_pct": 3.11, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-02-005420", "case_role": "hard_4c_success", "company_name": "코스모화학", "corporate_action_candidate_dates": ["1998-12-21", "2000-04-11", "2000-08-14", "2001-09-28", "2003-06-18", "2004-05-06", "2019-12-24"], "corporate_action_window_status": "clean_180D_window_after_profile_corporate_action_date_check", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C14_DEEP_2024_2025_EV_DEMAND_HARD_4C_VS_RECOVERY_MFE_EXCEPTION_BY_MATERIAL_CELL_MODULE_ROUTE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -55.66, "entry_date": "2024-04-30", "entry_price": 32150, "evidence_available_at_that_date": "source_proxy_only: historical EV demand slowdown / utilization / margin-reset or recovery-band evidence mapped to quarter-end/public-market date; URL repair pending", "evidence_family": "battery_precursor_material_downcycle", "evidence_source": "source_proxy_only_url_repair_pending", "evidence_url_pending": true, "fine_archetype_id": "C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER", "forward_window_trading_days": 180, "four_b_evidence_type": ["margin_or_backlog_slowdown", "positioning_overheat", "price_only_local_peak"], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable_hard_4c_path", "four_c_protection_label": "hard_4c_success", "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "97", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery", "notes": "precursor/material route; MFE stayed tiny while MAE expanded across 90D/180D", "peak_date": "2024-06-11", "peak_price": 33150, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005420/2024.csv; atlas/ohlcv_tradable_by_symbol_year/005/005420/2025.csv", "primary_archetype": "ev_demand_slowdown_4b_4c", "profile_path": "atlas/symbol_profiles/005/005420.json", "promotion_blocked_until_url_repair": true, "reuse_reason": null, "round": "R3", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|005420|Stage4C|2024-04-30|spring_2024_precursor_material_margin_break", "sector": "battery_ev_green_mobility", "source_proxy_only": true, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken", "utilization_or_margin_break_proxy_required"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "005420", "trigger_date": "2024-04-30", "trigger_family": "spring_2024_precursor_material_margin_break", "trigger_id": "C14-R3L97-02-005420-Stage4C-2024-04-30", "trigger_outcome_label": "precursor_material_hard_4c_after_small_mfe", "trigger_type": "Stage4C"}
{"MAE_180D_pct": -55.59, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "MAE_30D_pct": -26.32, "MAE_90D_pct": -50.0, "MFE_180D_pct": 3.95, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 3.95, "MFE_90D_pct": 3.95, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-03-336370", "case_role": "hard_4c_success", "company_name": "솔루스첨단소재", "corporate_action_candidate_dates": ["2024-01-08", "2024-01-30"], "corporate_action_window_status": "clean_180D_window_after_profile_corporate_action_date_check", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C14_DEEP_2024_2025_EV_DEMAND_HARD_4C_VS_RECOVERY_MFE_EXCEPTION_BY_MATERIAL_CELL_MODULE_ROUTE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -57.28, "entry_date": "2024-07-31", "entry_price": 15200, "evidence_available_at_that_date": "source_proxy_only: historical EV demand slowdown / utilization / margin-reset or recovery-band evidence mapped to quarter-end/public-market date; URL repair pending", "evidence_family": "copper_foil_ev_demand_margin_pressure", "evidence_source": "source_proxy_only_url_repair_pending", "evidence_url_pending": true, "fine_archetype_id": "C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER", "forward_window_trading_days": 180, "four_b_evidence_type": ["margin_or_backlog_slowdown", "positioning_overheat", "price_only_local_peak"], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable_hard_4c_path", "four_c_protection_label": "hard_4c_success", "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "97", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery", "notes": "post-January corporate-action window is clean; July demand-reset trigger had almost no recovery MFE", "peak_date": "2024-08-01", "peak_price": 15800, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv; atlas/ohlcv_tradable_by_symbol_year/336/336370/2025.csv", "primary_archetype": "ev_demand_slowdown_4b_4c", "profile_path": "atlas/symbol_profiles/336/336370.json", "promotion_blocked_until_url_repair": true, "reuse_reason": null, "round": "R3", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|336370|Stage4C|2024-07-31|mid_2024_copper_foil_demand_reset", "sector": "battery_ev_green_mobility", "source_proxy_only": true, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken", "utilization_or_margin_break_proxy_required"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "336370", "trigger_date": "2024-07-31", "trigger_family": "mid_2024_copper_foil_demand_reset", "trigger_id": "C14-R3L97-03-336370-Stage4C-2024-07-31", "trigger_outcome_label": "copper_foil_hard_4c_with_near_zero_upside", "trigger_type": "Stage4C"}
{"MAE_180D_pct": -36.63, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "MAE_30D_pct": -5.88, "MAE_90D_pct": -36.63, "MFE_180D_pct": 9.96, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 9.96, "MFE_90D_pct": 9.96, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-04-096770", "case_role": "hard_4c_success", "company_name": "SK이노베이션", "corporate_action_candidate_dates": ["2024-11-20"], "corporate_action_window_status": "clean_180D_window_after_profile_corporate_action_date_check", "current_profile_verdict": "current_profile_correct_but_requires_post_corporate_action_entry", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C14_DEEP_2024_2025_EV_DEMAND_HARD_4C_VS_RECOVERY_MFE_EXCEPTION_BY_MATERIAL_CELL_MODULE_ROUTE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -42.37, "entry_date": "2025-01-31", "entry_price": 127500, "evidence_available_at_that_date": "source_proxy_only: historical EV demand slowdown / utilization / margin-reset or recovery-band evidence mapped to quarter-end/public-market date; URL repair pending", "evidence_family": "cellmaker_loss_demand_reset_and_balance_sheet_absorption", "evidence_source": "source_proxy_only_url_repair_pending", "evidence_url_pending": true, "fine_archetype_id": "C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER", "forward_window_trading_days": 180, "four_b_evidence_type": ["margin_or_backlog_slowdown", "positioning_overheat", "price_only_local_peak"], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable_hard_4c_path", "four_c_protection_label": "hard_4c_success", "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "97", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery", "notes": "entry after the 2024-11-20 stock-web corporate-action candidate avoids contaminated forward window", "peak_date": "2025-03-13", "peak_price": 140200, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv; atlas/ohlcv_tradable_by_symbol_year/096/096770/2025.csv", "primary_archetype": "ev_demand_slowdown_4b_4c", "profile_path": "atlas/symbol_profiles/096/096770.json", "promotion_blocked_until_url_repair": true, "reuse_reason": null, "round": "R3", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|096770|Stage4C|2025-01-31|post_merger_battery_cell_loss_and_ev_demand_reset", "sector": "battery_ev_green_mobility", "source_proxy_only": true, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken", "utilization_or_margin_break_proxy_required"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "096770", "trigger_date": "2025-01-31", "trigger_family": "post_merger_battery_cell_loss_and_ev_demand_reset", "trigger_id": "C14-R3L97-04-096770-Stage4C-2025-01-31", "trigger_outcome_label": "cellmaker_parent_hard_4c_with_small_mfe_then_drawdown", "trigger_type": "Stage4C"}
{"MAE_180D_pct": -14.94, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "MAE_30D_pct": -14.94, "MAE_90D_pct": -14.94, "MFE_180D_pct": 48.5, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 9.59, "MFE_90D_pct": 15.32, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-05-417200", "case_role": "4B_watch_recovery_exception", "company_name": "LS머트리얼즈", "corporate_action_candidate_dates": [], "corporate_action_window_status": "clean_180D_window_after_profile_corporate_action_date_check", "current_profile_verdict": "current_profile_false_positive_if_hard_4c_without_recovery_band", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C14_DEEP_2024_2025_EV_DEMAND_HARD_4C_VS_RECOVERY_MFE_EXCEPTION_BY_MATERIAL_CELL_MODULE_ROUTE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -28.61, "entry_date": "2025-03-31", "entry_price": 10640, "evidence_available_at_that_date": "source_proxy_only: historical EV demand slowdown / utilization / margin-reset or recovery-band evidence mapped to quarter-end/public-market date; URL repair pending", "evidence_family": "green_mobility_power_module_recovery_band", "evidence_source": "source_proxy_only_url_repair_pending", "evidence_url_pending": true, "fine_archetype_id": "C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER", "forward_window_trading_days": 180, "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat", "macro_ev_slowdown_pressure", "recovery_mfe_exception_filter"], "four_b_full_window_peak_proximity": 0.0, "four_b_local_peak_proximity": 0.0, "four_b_timing_verdict": "price_only_local_4B_watch_not_full_4C", "four_c_protection_label": "false_break", "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "97", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery", "notes": "not a hard 4C: recovery MFE appears before non-price thesis break confirmation", "peak_date": "2025-11-04", "peak_price": 15800, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/417/417200/2024.csv; atlas/ohlcv_tradable_by_symbol_year/417/417200/2025.csv; atlas/ohlcv_tradable_by_symbol_year/417/417200/2026.csv", "primary_archetype": "ev_demand_slowdown_4b_4c", "profile_path": "atlas/symbol_profiles/417/417200.json", "promotion_blocked_until_url_repair": true, "reuse_reason": null, "round": "R3", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|417200|Stage4B|2025-03-31|2025_power_module_capacitor_recovery_mfe_exception", "sector": "battery_ev_green_mobility", "source_proxy_only": true, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "macro_ev_slowdown_pressure", "recovery_mfe_exception_filter"], "stage4c_evidence_fields": ["hard_4c_blocked_until_utilization_calloff_margin_break_confirmed"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "417200", "trigger_date": "2025-03-31", "trigger_family": "2025_power_module_capacitor_recovery_mfe_exception", "trigger_id": "C14-R3L97-05-417200-Stage4B-2025-03-31", "trigger_outcome_label": "power_module_name_recovery_mfe_before_any_hard_break", "trigger_type": "Stage4B"}
{"MAE_180D_pct": -24.39, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "MAE_30D_pct": -2.88, "MAE_90D_pct": -4.79, "MFE_180D_pct": 74.01, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 74.01, "MFE_90D_pct": 74.01, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-06-078600", "case_role": "4B_watch_recovery_exception", "company_name": "대주전자재료", "corporate_action_candidate_dates": [], "corporate_action_window_status": "clean_180D_window_after_profile_corporate_action_date_check", "current_profile_verdict": "current_profile_false_positive_if_hard_4c_without_recovery_band", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C14_DEEP_2024_2025_EV_DEMAND_HARD_4C_VS_RECOVERY_MFE_EXCEPTION_BY_MATERIAL_CELL_MODULE_ROUTE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -56.55, "entry_date": "2024-04-30", "entry_price": 93900, "evidence_available_at_that_date": "source_proxy_only: historical EV demand slowdown / utilization / margin-reset or recovery-band evidence mapped to quarter-end/public-market date; URL repair pending", "evidence_family": "silicon_anode_capacity_customer_optionality", "evidence_source": "source_proxy_only_url_repair_pending", "evidence_url_pending": true, "fine_archetype_id": "C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER", "forward_window_trading_days": 180, "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat", "macro_ev_slowdown_pressure", "recovery_mfe_exception_filter"], "four_b_full_window_peak_proximity": 0.0, "four_b_local_peak_proximity": 0.0, "four_b_timing_verdict": "price_only_local_4B_watch_not_full_4C", "four_c_protection_label": "false_break", "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "97", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery", "notes": "hard-4C route would have killed a large 30D/90D MFE; keep as 4B watch unless margin/call-off break confirms", "peak_date": "2024-06-12", "peak_price": 163400, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv; atlas/ohlcv_tradable_by_symbol_year/078/078600/2025.csv", "primary_archetype": "ev_demand_slowdown_4b_4c", "profile_path": "atlas/symbol_profiles/078/078600.json", "promotion_blocked_until_url_repair": true, "reuse_reason": null, "round": "R3", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|078600|Stage4B|2024-04-30|spring_2024_silicon_anode_recovery_band_exception", "sector": "battery_ev_green_mobility", "source_proxy_only": true, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "macro_ev_slowdown_pressure", "recovery_mfe_exception_filter"], "stage4c_evidence_fields": ["hard_4c_blocked_until_utilization_calloff_margin_break_confirmed"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "078600", "trigger_date": "2024-04-30", "trigger_family": "spring_2024_silicon_anode_recovery_band_exception", "trigger_id": "C14-R3L97-06-078600-Stage4B-2024-04-30", "trigger_outcome_label": "silicon_anode_large_recovery_mfe_despite_later_fade", "trigger_type": "Stage4B"}
{"MAE_180D_pct": -16.52, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "MAE_30D_pct": -16.23, "MAE_90D_pct": -16.52, "MFE_180D_pct": 34.6, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 5.44, "MFE_90D_pct": 15.45, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-07-011790", "case_role": "4B_watch_reused_symbol_new_trigger_family", "company_name": "SKC", "corporate_action_candidate_dates": ["1998-01-03", "2001-12-21"], "corporate_action_window_status": "clean_180D_window_after_profile_corporate_action_date_check", "current_profile_verdict": "current_profile_false_positive_if_hard_4c_without_recovery_band", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C14_DEEP_2024_2025_EV_DEMAND_HARD_4C_VS_RECOVERY_MFE_EXCEPTION_BY_MATERIAL_CELL_MODULE_ROUTE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -26.5, "entry_date": "2025-03-31", "entry_price": 102900, "evidence_available_at_that_date": "source_proxy_only: historical EV demand slowdown / utilization / margin-reset or recovery-band evidence mapped to quarter-end/public-market date; URL repair pending", "evidence_family": "copper_foil_parent_mix_recovery_exception", "evidence_source": "source_proxy_only_url_repair_pending", "evidence_url_pending": true, "fine_archetype_id": "C14_BATTERY_MATERIAL_CELL_AND_POWER_MODULE_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER", "forward_window_trading_days": 180, "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat", "macro_ev_slowdown_pressure", "recovery_mfe_exception_filter"], "four_b_full_window_peak_proximity": 0.0, "four_b_local_peak_proximity": 0.0, "four_b_timing_verdict": "price_only_local_4B_watch_not_full_4C", "four_c_protection_label": "false_break", "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "97", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + 4B_non_price_requirement_stress_test + 4C_thesis_break_timing_test + canonical_archetype_specific_rule_discovery", "notes": "same symbol as a prior local C14 file, but a new 2025 recovery-band trigger family; independent_evidence_weight is partial", "peak_date": "2025-11-04", "peak_price": 138500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv; atlas/ohlcv_tradable_by_symbol_year/011/011790/2025.csv", "primary_archetype": "ev_demand_slowdown_4b_4c", "profile_path": "atlas/symbol_profiles/011/011790.json", "promotion_blocked_until_url_repair": true, "reuse_reason": "reused_symbol_from_loop96_but_new_2025_recovery_band_trigger_family_not_same_entry_group", "round": "R3", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|011790|Stage4B|2025-03-31|2025_copper_foil_recovery_band_after_prior_2024_reset", "sector": "battery_ev_green_mobility", "source_proxy_only": true, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "macro_ev_slowdown_pressure", "recovery_mfe_exception_filter"], "stage4c_evidence_fields": ["hard_4c_blocked_until_utilization_calloff_margin_break_confirmed"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "011790", "trigger_date": "2025-03-31", "trigger_family": "2025_copper_foil_recovery_band_after_prior_2024_reset", "trigger_id": "C14-R3L97-07-011790-Stage4B-2025-03-31", "trigger_outcome_label": "reused_skc_symbol_new_2025_recovery_exception", "trigger_type": "Stage4B"}
{"MAE_90D_pct": -46.96, "MFE_90D_pct": 1.18, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-01-006110", "changed_components": ["hard_4c_confirmation", "recovery_mfe_absence_gate", "utilization_calloff_margin_break_gate"], "component_delta_explanation": "C14 shadow gate separates confirmed utilization/call-off/margin break with absent recovery MFE from macro EV-slowdown labels that still show recovery-band MFE.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 20, "contract_score": 25, "customer_quality_score": 18, "dilution_cb_risk_score": 2, "execution_risk_score": 25, "legal_or_contract_risk_score": 5, "margin_bridge_score": 18, "policy_or_regulatory_score": 6, "relative_strength_score": 8, "revision_score": 13, "valuation_repricing_score": 4}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 20, "contract_score": 25, "customer_quality_score": 18, "dilution_cb_risk_score": 2, "execution_risk_score": 22, "legal_or_contract_risk_score": 5, "margin_bridge_score": 18, "policy_or_regulatory_score": 6, "relative_strength_score": 8, "revision_score": 15, "valuation_repricing_score": 4}, "row_type": "score_simulation", "score_return_alignment_label": "hard_4c_aligned_low_mfe_high_mae", "stage_label_after": "Stage4C", "stage_label_before": "Stage4B-watch_or_late_4C_proxy", "symbol": "006110", "trigger_id": "C14-R3L97-01-006110-Stage4C-2024-10-31", "weighted_score_after": 66, "weighted_score_before": 74}
{"MAE_90D_pct": -48.68, "MFE_90D_pct": 3.11, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-02-005420", "changed_components": ["hard_4c_confirmation", "recovery_mfe_absence_gate", "utilization_calloff_margin_break_gate"], "component_delta_explanation": "C14 shadow gate separates confirmed utilization/call-off/margin break with absent recovery MFE from macro EV-slowdown labels that still show recovery-band MFE.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 20, "contract_score": 25, "customer_quality_score": 18, "dilution_cb_risk_score": 2, "execution_risk_score": 25, "legal_or_contract_risk_score": 5, "margin_bridge_score": 18, "policy_or_regulatory_score": 6, "relative_strength_score": 8, "revision_score": 13, "valuation_repricing_score": 4}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 20, "contract_score": 25, "customer_quality_score": 18, "dilution_cb_risk_score": 2, "execution_risk_score": 22, "legal_or_contract_risk_score": 5, "margin_bridge_score": 18, "policy_or_regulatory_score": 6, "relative_strength_score": 8, "revision_score": 15, "valuation_repricing_score": 4}, "row_type": "score_simulation", "score_return_alignment_label": "hard_4c_aligned_low_mfe_high_mae", "stage_label_after": "Stage4C", "stage_label_before": "Stage4B-watch_or_late_4C_proxy", "symbol": "005420", "trigger_id": "C14-R3L97-02-005420-Stage4C-2024-04-30", "weighted_score_after": 66, "weighted_score_before": 74}
{"MAE_90D_pct": -50.0, "MFE_90D_pct": 3.95, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-03-336370", "changed_components": ["hard_4c_confirmation", "recovery_mfe_absence_gate", "utilization_calloff_margin_break_gate"], "component_delta_explanation": "C14 shadow gate separates confirmed utilization/call-off/margin break with absent recovery MFE from macro EV-slowdown labels that still show recovery-band MFE.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 20, "contract_score": 25, "customer_quality_score": 18, "dilution_cb_risk_score": 2, "execution_risk_score": 25, "legal_or_contract_risk_score": 5, "margin_bridge_score": 18, "policy_or_regulatory_score": 6, "relative_strength_score": 8, "revision_score": 13, "valuation_repricing_score": 4}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 20, "contract_score": 25, "customer_quality_score": 18, "dilution_cb_risk_score": 2, "execution_risk_score": 22, "legal_or_contract_risk_score": 5, "margin_bridge_score": 18, "policy_or_regulatory_score": 6, "relative_strength_score": 8, "revision_score": 15, "valuation_repricing_score": 4}, "row_type": "score_simulation", "score_return_alignment_label": "hard_4c_aligned_low_mfe_high_mae", "stage_label_after": "Stage4C", "stage_label_before": "Stage4B-watch_or_late_4C_proxy", "symbol": "336370", "trigger_id": "C14-R3L97-03-336370-Stage4C-2024-07-31", "weighted_score_after": 66, "weighted_score_before": 74}
{"MAE_90D_pct": -36.63, "MFE_90D_pct": 9.96, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-04-096770", "changed_components": ["hard_4c_confirmation", "recovery_mfe_absence_gate", "utilization_calloff_margin_break_gate"], "component_delta_explanation": "C14 shadow gate separates confirmed utilization/call-off/margin break with absent recovery MFE from macro EV-slowdown labels that still show recovery-band MFE.", "current_profile_verdict": "current_profile_correct_but_requires_post_corporate_action_entry", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 20, "contract_score": 25, "customer_quality_score": 18, "dilution_cb_risk_score": 2, "execution_risk_score": 25, "legal_or_contract_risk_score": 5, "margin_bridge_score": 18, "policy_or_regulatory_score": 6, "relative_strength_score": 8, "revision_score": 13, "valuation_repricing_score": 4}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 20, "contract_score": 25, "customer_quality_score": 18, "dilution_cb_risk_score": 2, "execution_risk_score": 22, "legal_or_contract_risk_score": 5, "margin_bridge_score": 18, "policy_or_regulatory_score": 6, "relative_strength_score": 8, "revision_score": 15, "valuation_repricing_score": 4}, "row_type": "score_simulation", "score_return_alignment_label": "hard_4c_aligned_low_mfe_high_mae", "stage_label_after": "Stage4C", "stage_label_before": "Stage4B-watch_or_late_4C_proxy", "symbol": "096770", "trigger_id": "C14-R3L97-04-096770-Stage4C-2025-01-31", "weighted_score_after": 64, "weighted_score_before": 71}
{"MAE_90D_pct": -14.94, "MFE_90D_pct": 15.32, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-05-417200", "changed_components": ["hard_4c_confirmation_weakened_by_recovery_band_exception", "local_4b_watch_guard_strengthened"], "component_delta_explanation": "C14 shadow gate separates confirmed utilization/call-off/margin break with absent recovery MFE from macro EV-slowdown labels that still show recovery-band MFE.", "current_profile_verdict": "current_profile_false_positive_if_hard_4c_without_recovery_band", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 18, "contract_score": 16, "customer_quality_score": 14, "dilution_cb_risk_score": 2, "execution_risk_score": 17, "legal_or_contract_risk_score": 4, "margin_bridge_score": 10, "policy_or_regulatory_score": 5, "relative_strength_score": 20, "revision_score": 11, "valuation_repricing_score": 12}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 18, "contract_score": 16, "customer_quality_score": 14, "dilution_cb_risk_score": 2, "execution_risk_score": 14, "legal_or_contract_risk_score": 4, "margin_bridge_score": 10, "policy_or_regulatory_score": 5, "relative_strength_score": 20, "revision_score": 10, "valuation_repricing_score": 12}, "row_type": "score_simulation", "score_return_alignment_label": "hard_4c_would_be_false_positive_recovery_mfe_present", "stage_label_after": "Stage4B-watch_not_full_4C", "stage_label_before": "Stage4C_if_macro_slowdown_overrouted", "symbol": "417200", "trigger_id": "C14-R3L97-05-417200-Stage4B-2025-03-31", "weighted_score_after": 77, "weighted_score_before": 72}
{"MAE_90D_pct": -4.79, "MFE_90D_pct": 74.01, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-06-078600", "changed_components": ["hard_4c_confirmation_weakened_by_recovery_band_exception", "local_4b_watch_guard_strengthened"], "component_delta_explanation": "C14 shadow gate separates confirmed utilization/call-off/margin break with absent recovery MFE from macro EV-slowdown labels that still show recovery-band MFE.", "current_profile_verdict": "current_profile_false_positive_if_hard_4c_without_recovery_band", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 18, "contract_score": 16, "customer_quality_score": 14, "dilution_cb_risk_score": 2, "execution_risk_score": 17, "legal_or_contract_risk_score": 4, "margin_bridge_score": 10, "policy_or_regulatory_score": 5, "relative_strength_score": 20, "revision_score": 11, "valuation_repricing_score": 12}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 18, "contract_score": 16, "customer_quality_score": 14, "dilution_cb_risk_score": 2, "execution_risk_score": 14, "legal_or_contract_risk_score": 4, "margin_bridge_score": 10, "policy_or_regulatory_score": 5, "relative_strength_score": 20, "revision_score": 10, "valuation_repricing_score": 12}, "row_type": "score_simulation", "score_return_alignment_label": "hard_4c_would_be_false_positive_recovery_mfe_present", "stage_label_after": "Stage4B-watch_not_full_4C", "stage_label_before": "Stage4C_if_macro_slowdown_overrouted", "symbol": "078600", "trigger_id": "C14-R3L97-06-078600-Stage4B-2024-04-30", "weighted_score_after": 77, "weighted_score_before": 72}
{"MAE_90D_pct": -16.52, "MFE_90D_pct": 15.45, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14-R3L97-07-011790", "changed_components": ["hard_4c_confirmation_weakened_by_recovery_band_exception", "local_4b_watch_guard_strengthened"], "component_delta_explanation": "C14 shadow gate separates confirmed utilization/call-off/margin break with absent recovery MFE from macro EV-slowdown labels that still show recovery-band MFE.", "current_profile_verdict": "current_profile_false_positive_if_hard_4c_without_recovery_band", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 18, "contract_score": 16, "customer_quality_score": 14, "dilution_cb_risk_score": 2, "execution_risk_score": 17, "legal_or_contract_risk_score": 4, "margin_bridge_score": 10, "policy_or_regulatory_score": 5, "relative_strength_score": 20, "revision_score": 11, "valuation_repricing_score": 12}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 18, "contract_score": 16, "customer_quality_score": 14, "dilution_cb_risk_score": 2, "execution_risk_score": 14, "legal_or_contract_risk_score": 4, "margin_bridge_score": 10, "policy_or_regulatory_score": 5, "relative_strength_score": 20, "revision_score": 10, "valuation_repricing_score": 12}, "row_type": "score_simulation", "score_return_alignment_label": "hard_4c_would_be_false_positive_recovery_mfe_present", "stage_label_after": "Stage4B-watch_not_full_4C", "stage_label_before": "Stage4C_if_macro_slowdown_overrouted", "symbol": "011790", "trigger_id": "C14-R3L97-07-011790-Stage4B-2025-03-31", "weighted_score_after": 74, "weighted_score_before": 72}
{"canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "do_not_propose_new_weight_delta": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "97", "loop_contribution_label": "canonical_archetype_rule_candidate", "new_independent_case_count": 6, "new_symbol_count": 6, "new_trigger_family_count": 7, "residual_error_types_found": ["hard_4c_false_positive_when_recovery_mfe_band_exists", "hard_4c_correct_when_low_mfe_high_mae_material_margin_break", "source_proxy_only_blocks_promotion_until_url_repair"], "reused_case_count": 1, "round": "R3", "row_type": "residual_contribution", "tested_existing_calibrated_axes": ["hard_4c_thesis_break_routes_to_4c", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"]}
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 7
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied `e2r_2_1_stock_web_calibrated` profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

### Rules
- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as full new independent evidence unless `independent_evidence_weight > 0`.
- Do not treat `schema_rematerialization_only` or `duplicate_low_value_loop` as new evidence.
- Do not apply global deltas unless multiple `large_sector_id` values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- Price-only rows cannot promote Stage2/Stage3.
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
completed_round = R3
completed_loop = 97
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY, C11_BATTERY_ORDERBOOK_RERATING, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C01_ORDER_BACKLOG_MARGIN_BRIDGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.
- No-repeat and coverage source: `docs/core/V12_Research_No_Repeat_Index.md`.
- Price manifest: `Songdaiki/stock-web/atlas/manifest.json`.
- Schema: `Songdaiki/stock-web/atlas/schema.json`.
- Profiles checked: `006110`, `005420`, `078600`, `096770`, `336370`, `417200`, `011790`.
