# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R10
scheduled_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_PF_SURVIVOR_RESIDUAL
output_file = e2r_stock_web_v12_residual_round_R10_loop_13_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
```

This loop adds **6** new independent cases, **3** counterexamples, and **6** current-profile stress observations for `R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK`.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The point of this file is not to re-prove the global calibration. The residual question is narrower: when small-cap construction names move on policy/PF-liquidity headlines, does the current profile separate a tradable Stage2 theme-watch from a true C30 balance-sheet/margin repair signal?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R10
scheduled_loop = 13
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_PF_SURVIVOR_RESIDUAL
loop_objective = coverage_gap_fill | counterexample_mining | residual_false_positive_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
```

`R10` maps directly to `L9_CONSTRUCTION_REALESTATE_HOUSING`, so the round-sector consistency gate passes. `C30` is used because the common failure mode is not ordinary order backlog; it is the gap between policy/PF-liquidity optimism and actual balance-sheet, receivable, cash-collection, and margin evidence.

## 3. Previous Coverage / Duplicate Avoidance Check

Existing local v12 R10 outputs before this file already covered the heavier builder set:

```text
loop 10: HDC현대산업개발, 현대건설, DL이앤씨, GS건설, 태영건설 narrative-only
loop 11: 대우건설, 계룡건설, 코오롱글로벌, 금호건설, 동부건설, 신세계건설 narrative-only
loop 12: KCC건설, HL D&I, 서희건설, 한신공영, HS화성, 삼부토건 narrative/blocked
```

This loop therefore avoids those symbols and adds six under-covered smaller construction/theme names: `010780`, `013360`, `001260`, `002410`, `002780`, `025950`. The macro trigger family overlaps the March 2024 PF/policy support window, but the case contribution is new because the symbol set, liquidity profile, MAE behavior, and theme-blowoff path are new.

```text
new_independent_case_count = 6
reused_case_count = 0
new_symbol_count = 6
same_archetype_new_symbol_count = 6
same_archetype_new_trigger_family_count = 3
new_trigger_family_count = 3
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
price_atlas_repo = https://github.com/Songdaiki/stock-web
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_min_date = 1995-05-02
manifest_max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The price basis is raw/unadjusted marcap OHLC. Corporate-action contaminated windows are blocked by default. The cases in this file use 2024 entry windows, and the listed symbol-profile corporate-action candidates do not overlap each entry-date to D+180 window.

## 5. Historical Eligibility Gate

All representative trigger rows are historical. All entry dates exist in the tradable shards. Each representative trigger has at least 180 trading days available under manifest max date `2026-02-20`. No representative 180D window is blocked by a corporate-action candidate.

| symbol | company | profile_path | price_shard_path | entry_date | 180D usable | corporate_action_window_status |
| --- | --- | --- | --- | --- | --- | --- |
| 010780 | 아이에스동서 | atlas/symbol_profiles/010/010780.json | atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv | 2024-03-27 | true | clean_180D_window |
| 013360 | 일성건설 | atlas/symbol_profiles/013/013360.json | atlas/ohlcv_tradable_by_symbol_year/013/013360/2024.csv | 2024-03-27 | true | clean_180D_window |
| 001260 | 남광토건 | atlas/symbol_profiles/001/001260.json | atlas/ohlcv_tradable_by_symbol_year/001/001260/2024.csv | 2024-03-27 | true | clean_180D_window |
| 002410 | 범양건영 | atlas/symbol_profiles/002/002410.json | atlas/ohlcv_tradable_by_symbol_year/002/002410/2024.csv | 2024-03-27 | true | clean_180D_window |
| 002780 | 진흥기업 | atlas/symbol_profiles/002/002780.json | atlas/ohlcv_tradable_by_symbol_year/002/002780/2024.csv | 2024-03-27 | true | clean_180D_window |
| 025950 | 동신건설 | atlas/symbol_profiles/025/025950.json | atlas/ohlcv_tradable_by_symbol_year/025/025950/2024.csv | 2024-03-27 | true | clean_180D_window |


## 6. Canonical Archetype Compression Map

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  ├─ large-builder PF/quality break path      -> covered in earlier R10 loops
  ├─ mid-builder receivable/cash risk path    -> covered in earlier R10 loops
  └─ small-cap policy/theme residual path     -> this loop
```

The compression lesson is that small-cap construction names need two separate tracks. The first is `Stage2-Theme-Watch`: policy, PF-liquidity, election, or local-contract beta can create MFE. The second is `Stage3-Yellow/Green`: this requires non-price proof of cash collection, PF exposure repair, margin bridge, and contract-quality visibility. The two tracks must not be collapsed into one score.

## 7. Case Selection Summary

| case_id | symbol | company | case_type | positive_or_counterexample | novelty_reason |
| --- | --- | --- | --- | --- | --- |
| R10L13_C30_010780_POLICY_SUPPORT_NO_PF_CONVERSION | 010780 | 아이에스동서 | failed_rerating | counterexample | new C30 small-cap construction symbol; no reused entry row |
| R10L13_C30_013360_SMALLCAP_POLICY_BLOWOFF | 013360 | 일성건설 | 4B_overlay_success | positive | new C30 small-cap construction symbol; no reused entry row |
| R10L13_C30_001260_POLICY_THEME_HIGH_MFE | 001260 | 남광토건 | 4B_overlay_success | positive | new C30 small-cap construction symbol; no reused entry row |
| R10L13_C30_002410_POLICY_THEME_THIN_FLOAT | 002410 | 범양건영 | high_mae_success | positive | new C30 small-cap construction symbol; no reused entry row |
| R10L13_C30_002780_NO_CONVERSION_DRIFT_DOWN | 002780 | 진흥기업 | failed_rerating | counterexample | new C30 small-cap construction symbol; no reused entry row |
| R10L13_C30_025950_EARLY_BLOWOFF_FAIL | 025950 | 동신건설 | false_positive_green | counterexample | new C30 small-cap construction symbol; no reused entry row |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 3
calibration_usable_case_count = 6
```

The positive cases here are not Green promotion cases. They are positive only for **theme-watch and 4B overlay calibration**: they prove that C30 small-cap construction beta can generate MFE, but the same evidence set is not enough to label a structural Stage3-Green. The counterexamples show the other half of the machine: when the same policy evidence is not joined by margin/cash/PF repair, price either drifts down or produces unacceptable MAE.

## 9. Evidence Source Map

```text
common_policy_event_window = 2024-03-27 PF / construction liquidity-support policy window
case_specific_non_price_green_evidence = not confirmed at trigger date
stage2_theme_watch_evidence = policy optionality + relative strength
stage3_green_evidence = absent at trigger date
4B_evidence = price-only blowoff / positioning overheat / failed conversion
4C_evidence = thesis-break watch where price drift or MAE overwhelms MFE
```

No later outcome is used to move the trigger date backward. The March 2024 trigger is kept as a Stage2/Theme-Watch test; later November-December 2024 spikes are treated as outcome/4B timing evidence, not as retroactive Stage3 evidence.

## 10. Price Data Source Map

| symbol | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 010780 | 29250 | 4.1% | -16.41% | 4.1% | -30.43% | 4.1% | -40.24% | 2024-03-29 | 30450 |
| 013360 | 1267 | 24.94% | -7.5% | 46.8% | -7.5% | 334.1% | -8.05% | 2024-12-11 | 5500 |
| 001260 | 6380 | 3.92% | -8.31% | 34.01% | -11.29% | 64.58% | -11.29% | 2024-11-13 | 10500 |
| 002410 | 1611 | 10.18% | -16.2% | 10.18% | -25.64% | 160.4% | -38.86% | 2024-12-13 | 4195 |
| 002780 | 1004 | 0.5% | -7.77% | 0.5% | -13.35% | 0.5% | -20.62% | 2024-03-28 | 1009 |
| 025950 | 29000 | 5.17% | -35.9% | 5.17% | -39.55% | 5.17% | -39.55% | 2024-04-02 | 30500 |


## 11. Case-by-Case Trigger Grid

| case_id | symbol | company | role | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | current_profile |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R10L13_C30_010780_POLICY_SUPPORT_NO_PF_CONVERSION | 010780 | 아이에스동서 | failed_rerating | 2024-03-27 / 29250 | 4.1% | -16.41% | 4.1% | -30.43% | 4.1% | -40.24% | 2024-03-29 / 30450 | current_profile_false_positive |
| R10L13_C30_013360_SMALLCAP_POLICY_BLOWOFF | 013360 | 일성건설 | price_moved_without_evidence | 2024-03-27 / 1267 | 24.94% | -7.5% | 46.8% | -7.5% | 334.1% | -8.05% | 2024-12-11 / 5500 | current_profile_4B_too_late |
| R10L13_C30_001260_POLICY_THEME_HIGH_MFE | 001260 | 남광토건 | high_mae_success | 2024-03-27 / 6380 | 3.92% | -8.31% | 34.01% | -11.29% | 64.58% | -11.29% | 2024-11-13 / 10500 | current_profile_4B_too_late |
| R10L13_C30_002410_POLICY_THEME_THIN_FLOAT | 002410 | 범양건영 | high_mae_success | 2024-03-27 / 1611 | 10.18% | -16.2% | 10.18% | -25.64% | 160.4% | -38.86% | 2024-12-13 / 4195 | current_profile_4B_too_late |
| R10L13_C30_002780_NO_CONVERSION_DRIFT_DOWN | 002780 | 진흥기업 | false_positive_green | 2024-03-27 / 1004 | 0.5% | -7.77% | 0.5% | -13.35% | 0.5% | -20.62% | 2024-03-28 / 1009 | current_profile_false_positive |
| R10L13_C30_025950_EARLY_BLOWOFF_FAIL | 025950 | 동신건설 | false_positive_green | 2024-03-27 / 29000 | 5.17% | -35.9% | 5.17% | -39.55% | 5.17% | -39.55% | 2024-04-02 / 30500 | current_profile_false_positive |


## 12. Trigger-Level OHLC Backtest Tables

The representative aggregate includes only `calibration_usable=true`, `dedupe_for_aggregate=true`, `aggregate_group_role=representative`, and `do_not_count_as_new_case=false` rows.

```text
representative_trigger_count = 6
avg_MFE_30D_pct = 8.13
avg_MAE_30D_pct = -15.35
avg_MFE_90D_pct = 16.79
avg_MAE_90D_pct = -21.29
avg_MFE_180D_pct = 94.81
avg_MAE_180D_pct = -26.44
```

Interpretation: the average 180D MFE is inflated by political/theme blowoffs in `013360`, `001260`, and `002410`, but average MAE is also structurally high. This is exactly the profile of a theme-watch/overlay domain, not a clean Green promotion domain.

## 13. Current Calibrated Profile Stress Test

1. `current_profile_false_positive` appears when the profile gives too much credit to macro policy optionality without PF/cash repair evidence: `010780`, `002780`, `025950`.
2. `current_profile_4B_too_late` appears when price-only blowoff becomes obvious only after most of the theme move has already happened: `013360`, `001260`, `002410`.
3. The existing `price_only_blowoff_blocks_positive_stage` axis is kept and strengthened for C30.
4. The existing `full_4b_requires_non_price_evidence` axis is kept; however, for small-cap C30, a separate `theme-watch 4B overlay` should exist before full 4B.

| symbol | before_score/stage | after_score/stage | MFE90 | MAE90 | alignment |
| --- | --- | --- | --- | --- | --- |
| 010780 | 72 / Stage2-Actionable | 61 / Stage2-Watch | 4.1% | -30.43% | policy_support_did_not_convert_to_margin_or_balance_sheet_repair |
| 013360 | 70 / Stage2-Actionable | 58 / Stage2-Theme-Watch | 46.8% | -7.5% | huge_price_move_without_confirmed_pf_or_margin_evidence |
| 001260 | 69 / Stage2-Actionable | 59 / Stage2-Theme-Watch | 34.01% | -11.29% | theme_beta_captured_but_green_promotion_not_supported |
| 002410 | 68 / Stage2-Actionable | 57 / Stage2-Theme-Watch | 10.18% | -25.64% | thin_float_policy_theme_created_return_but_large_mae_and_blowoff |
| 002780 | 67 / Stage2-Actionable | 50 / Stage1/2-Watch | 0.5% | -13.35% | policy_optionality_failed_without_contract_or_margin_evidence |
| 025950 | 71 / Stage2-Actionable | 49 / Stage1/2-Watch | 5.17% | -39.55% | early_spike_failed_and_high_mae_confirmed_no_green |


## 14. Stage2 / Yellow / Green Comparison

```text
Stage2-Actionable = policy/PF-liquidity support + relative strength
Stage3-Yellow = requires visible PF exposure containment, cash collection, backlog quality, or margin bridge
Stage3-Green = requires confirmed revision + financial visibility + low red-team risk
```

No case in this loop has a clean Stage3-Green trigger on the 2024-03-27 evidence date. Therefore `green_lateness_ratio = not_applicable`. The important lesson is not “Green is late”; the lesson is “small-cap policy/theme Stage2 must not be confused with Green.”

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B_local_peak_proximity | 4B_full_window_peak_proximity | four_b_timing_verdict | four_b_evidence_type |
| --- | --- | --- | --- | --- |
| 010780 | 1.0 | 1.0 | good_local_but_not_full_positive_stage | valuation_blowoff|margin_or_backlog_slowdown |
| 013360 | 1.0 | 1.0 | price_only_blowoff_requires_overlay_not_green | price_only|positioning_overheat |
| 001260 | 0.86 | 1.0 | late_full_window_4B_after_theme_blowoff | price_only|positioning_overheat |
| 002410 | 0.69 | 1.0 | full_window_4B_late_after_theme_blowoff | price_only|positioning_overheat |
| 002780 | 1.0 | 1.0 | negative_alignment_no_full_4B_needed | margin_or_backlog_slowdown |
| 025950 | 1.0 | 1.0 | price_only_local_4B_should_block_positive_stage | price_only|positioning_overheat |


The 4B signal here behaves like a pressure gauge, not an exit button. In C30 small caps, price can make several local peaks before the final theme blowoff. Treating the first local peak as a full 4B would be too early for `013360`, `001260`, and `002410`; treating the final blowoff as structural Green would be too late and unsafe.

## 16. 4C Protection Audit

`002780` and `025950` are the clearest thesis-break watch examples: MFE is small while MAE is large. `010780` also fails to convert policy support into a price path. These cases argue for an earlier watch downgrade when the name breaks below entry without non-price repair evidence.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success = not claimed
hard_4c_late = not claimed
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = L9_C30_POLICY_THEME_STAGE2_WATCH_GUARD
rule_candidate = true
```

For L9 construction/housing, policy or PF-liquidity support should create at most `Stage2-Theme-Watch` unless at least two non-price supports are present:

```text
required_non_price_supports:
- PF exposure repair or project-level financing de-risking
- cash collection / receivable normalization
- margin bridge or cost-to-complete visibility
- contract-quality/backlog conversion evidence
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rule_candidate = true
```

Proposed C30 compression:

```text
if policy_or_regulatory_score is high
and margin_bridge_score is not supported
and backlog_visibility_score is not supported
and cash/PF repair evidence is absent:
    max_positive_stage = Stage2-Theme-Watch
    do_not_promote_to_Stage3_Green = true
```

For small-cap C30 blowoffs:

```text
if price_only_local_peak == true
and non_price_4B_evidence == absent:
    treat_as_4B_overlay_watch
    do_not_treat_as_full_4B
    do_not_count_as_positive_green_evidence
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | FP_rate | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 6 | 16.79% | -21.29% | 94.81% | -26.44% | 0.5 | mixed; theme-MFE high but Green evidence absent |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 6 | 16.79% | -21.29% | 94.81% | -26.44% | 0.67 | worse: policy-only promotion too easy |
| P1_L9_sector_specific_candidate_profile | sector_specific | 6 | 16.79% | -21.29% | 94.81% | -26.44% | 0.17 | better: keeps theme-watch and prevents Green false positives |
| P2_C30_canonical_archetype_candidate_profile | canonical_archetype_specific | 6 | 16.79% | -21.29% | 94.81% | -26.44% | 0.17 | best explanatory compression for this loop |
| P3_counterexample_guard_profile | guard_profile | 6 | 16.79% | -21.29% | 94.81% | -26.44% | 0.0 | safe but may undercapture very thin-float theme MFE |


## 20. Score-Return Alignment Matrix

| symbol | before_score/stage | after_score/stage | MFE90 | MAE90 | alignment |
| --- | --- | --- | --- | --- | --- |
| 010780 | 72 / Stage2-Actionable | 61 / Stage2-Watch | 4.1% | -30.43% | policy_support_did_not_convert_to_margin_or_balance_sheet_repair |
| 013360 | 70 / Stage2-Actionable | 58 / Stage2-Theme-Watch | 46.8% | -7.5% | huge_price_move_without_confirmed_pf_or_margin_evidence |
| 001260 | 69 / Stage2-Actionable | 59 / Stage2-Theme-Watch | 34.01% | -11.29% | theme_beta_captured_but_green_promotion_not_supported |
| 002410 | 68 / Stage2-Actionable | 57 / Stage2-Theme-Watch | 10.18% | -25.64% | thin_float_policy_theme_created_return_but_large_mae_and_blowoff |
| 002780 | 67 / Stage2-Actionable | 50 / Stage1/2-Watch | 0.5% | -13.35% | policy_optionality_failed_without_contract_or_margin_evidence |
| 025950 | 71 / Stage2-Actionable | 49 / Stage1/2-Watch | 5.17% | -39.55% | early_spike_failed_and_high_mae_confirmed_no_green |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_PF_SURVIVOR_RESIDUAL | 3 | 3 | 6 | 2 | 6 | 0 | 6 | 6 | 6 | true | true | large-cap/mid-cap C30 was covered in prior loops; this loop adds under-covered small-cap policy/theme residuals |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: policy_theme_false_positive, 4B_too_late_after_price_only_blowoff, high_MAE_success_not_green
new_axis_proposed: C30_policy_theme_without_pf_repair_haircut, C30_require_cash_collection_margin_bridge_for_green
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest and price basis
- symbol profile availability
- tradable 2024 shard entry rows
- 30D / 90D / 180D MFE and MAE estimates from stock-web rows
- corporate-action candidate non-overlap for 2024 entry windows
- current calibrated profile stress test at research-proxy level
```

Not validated:

```text
- live 2026 candidate scan
- production stock_agent scoring code
- brokerage or auto-trading use
- current investability
- exact sell/exit recommendation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C30_policy_theme_without_pf_repair_haircut,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,-1,-1,Policy or small-cap construction theme beta alone created high false-positive/4B-late risk.,Reduced false-positive promotion in 010780/002780/025950 while retaining theme-watch rows for 013360/001260/002410.,"R10L13_C30_010780_T_STAGE2_20240327|R10L13_C30_013360_T_STAGE2_20240327|R10L13_C30_001260_T_STAGE2_20240327|R10L13_C30_002410_T_STAGE2_20240327|R10L13_C30_002780_T_STAGE2_20240327|R10L13_C30_025950_T_STAGE2_20240327",6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C30_require_cash_collection_margin_bridge_for_green,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,false,true,guard,"Green cannot rely on policy support or price spike without PF exposure repair, margin bridge, and cash collection evidence.",Blocks price-only blowoff from becoming positive Stage3.,"R10L13_C30_010780_T_STAGE2_20240327|R10L13_C30_013360_T_STAGE2_20240327|R10L13_C30_001260_T_STAGE2_20240327|R10L13_C30_002410_T_STAGE2_20240327|R10L13_C30_002780_T_STAGE2_20240327|R10L13_C30_025950_T_STAGE2_20240327",6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R10L13_C30_010780_POLICY_SUPPORT_NO_PF_CONVERSION","symbol":"010780","company_name":"아이에스동서","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_PF_SURVIVOR_RESIDUAL","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R10L13_C30_010780_T_STAGE2_20240327","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"policy_support_did_not_convert_to_margin_or_balance_sheet_repair","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Policy-liquidity support and sector rebound were visible, but no case-date evidence showed PF exposure repair, cash collection conversion, or margin bridge."}
{"row_type":"case","case_id":"R10L13_C30_013360_SMALLCAP_POLICY_BLOWOFF","symbol":"013360","company_name":"일성건설","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_PF_SURVIVOR_RESIDUAL","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R10L13_C30_013360_T_STAGE2_20240327","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"huge_price_move_without_confirmed_pf_or_margin_evidence","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Small-cap construction policy/theme beta produced large MFE, but the available case-date evidence was not a Green-quality PF repair or margin bridge."}
{"row_type":"case","case_id":"R10L13_C30_001260_POLICY_THEME_HIGH_MFE","symbol":"001260","company_name":"남광토건","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_PF_SURVIVOR_RESIDUAL","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R10L13_C30_001260_T_STAGE2_20240327","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"theme_beta_captured_but_green_promotion_not_supported","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Policy and small-construction beta gave a tradable run, but the move was not supported by case-date confirmed PF balance-sheet repair evidence."}
{"row_type":"case","case_id":"R10L13_C30_002410_POLICY_THEME_THIN_FLOAT","symbol":"002410","company_name":"범양건영","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_PF_SURVIVOR_RESIDUAL","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R10L13_C30_002410_T_STAGE2_20240327","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"thin_float_policy_theme_created_return_but_large_mae_and_blowoff","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Thin-float construction theme later produced strong MFE, but without non-price Green evidence the useful calibration is a 4B/positioning overlay, not a positive score promotion."}
{"row_type":"case","case_id":"R10L13_C30_002780_NO_CONVERSION_DRIFT_DOWN","symbol":"002780","company_name":"진흥기업","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_PF_SURVIVOR_RESIDUAL","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R10L13_C30_002780_T_STAGE2_20240327","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"policy_optionality_failed_without_contract_or_margin_evidence","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Sector policy support existed, but the name had no observed case-date margin bridge, backlog conversion, or contract-quality confirmation; price drifted lower."}
{"row_type":"case","case_id":"R10L13_C30_025950_EARLY_BLOWOFF_FAIL","symbol":"025950","company_name":"동신건설","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_PF_SURVIVOR_RESIDUAL","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R10L13_C30_025950_T_STAGE2_20240327","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"early_spike_failed_and_high_mae_confirmed_no_green","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The 2024 policy support date arrived after an already-hot small-cap move; there was no case-date PF repair or margin bridge, and MAE overwhelmed the modest MFE."}
{"row_type":"trigger","trigger_id":"R10L13_C30_010780_T_STAGE2_20240327","case_id":"R10L13_C30_010780_POLICY_SUPPORT_NO_PF_CONVERSION","symbol":"010780","company_name":"아이에스동서","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_PF_SURVIVOR_RESIDUAL","sector":"construction_realestate_housing","primary_archetype":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-27","evidence_available_at_that_date":"Policy-liquidity support and sector rebound were visible, but no case-date evidence showed PF exposure repair, cash collection conversion, or margin bridge.","evidence_source":"public policy/PF-liquidity event + stock-web OHLC atlas; no live candidate research","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv","profile_path":"atlas/symbol_profiles/010/010780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-27","entry_price":29250,"MFE_30D_pct":4.1,"MFE_90D_pct":4.1,"MFE_180D_pct":4.1,"MFE_1Y_pct":4.1,"MFE_2Y_pct":null,"MAE_30D_pct":-16.41,"MAE_90D_pct":-30.43,"MAE_180D_pct":-40.24,"MAE_1Y_pct":-40.24,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-29","peak_price":30450,"drawdown_after_peak_pct":-42.59,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_local_but_not_full_positive_stage","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_support_did_not_convert_to_margin_or_balance_sheet_repair","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L13_C30_010780_POLICY_SUPPORT_NO_PF_CONVERSION::2024-03-27::29250","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L13_C30_013360_T_STAGE2_20240327","case_id":"R10L13_C30_013360_SMALLCAP_POLICY_BLOWOFF","symbol":"013360","company_name":"일성건설","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_PF_SURVIVOR_RESIDUAL","sector":"construction_realestate_housing","primary_archetype":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-27","evidence_available_at_that_date":"Small-cap construction policy/theme beta produced large MFE, but the available case-date evidence was not a Green-quality PF repair or margin bridge.","evidence_source":"public policy/PF-liquidity event + stock-web OHLC atlas; no live candidate research","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/013/013360/2024.csv","profile_path":"atlas/symbol_profiles/013/013360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-27","entry_price":1267,"MFE_30D_pct":24.94,"MFE_90D_pct":46.8,"MFE_180D_pct":334.1,"MFE_1Y_pct":334.1,"MFE_2Y_pct":null,"MAE_30D_pct":-7.5,"MAE_90D_pct":-7.5,"MAE_180D_pct":-8.05,"MAE_1Y_pct":-8.05,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-11","peak_price":5500,"drawdown_after_peak_pct":-43.64,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_blowoff_requires_overlay_not_green","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"false_break_or_theme_watch_only","trigger_outcome_label":"huge_price_move_without_confirmed_pf_or_margin_evidence","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L13_C30_013360_SMALLCAP_POLICY_BLOWOFF::2024-03-27::1267","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L13_C30_001260_T_STAGE2_20240327","case_id":"R10L13_C30_001260_POLICY_THEME_HIGH_MFE","symbol":"001260","company_name":"남광토건","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_PF_SURVIVOR_RESIDUAL","sector":"construction_realestate_housing","primary_archetype":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-27","evidence_available_at_that_date":"Policy and small-construction beta gave a tradable run, but the move was not supported by case-date confirmed PF balance-sheet repair evidence.","evidence_source":"public policy/PF-liquidity event + stock-web OHLC atlas; no live candidate research","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001260/2024.csv","profile_path":"atlas/symbol_profiles/001/001260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-27","entry_price":6380,"MFE_30D_pct":3.92,"MFE_90D_pct":34.01,"MFE_180D_pct":64.58,"MFE_1Y_pct":64.58,"MFE_2Y_pct":null,"MAE_30D_pct":-8.31,"MAE_90D_pct":-11.29,"MAE_180D_pct":-11.29,"MAE_1Y_pct":-11.29,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-13","peak_price":10500,"drawdown_after_peak_pct":-33.05,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_full_window_4B_after_theme_blowoff","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"false_break_or_theme_watch_only","trigger_outcome_label":"theme_beta_captured_but_green_promotion_not_supported","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L13_C30_001260_POLICY_THEME_HIGH_MFE::2024-03-27::6380","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L13_C30_002410_T_STAGE2_20240327","case_id":"R10L13_C30_002410_POLICY_THEME_THIN_FLOAT","symbol":"002410","company_name":"범양건영","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_PF_SURVIVOR_RESIDUAL","sector":"construction_realestate_housing","primary_archetype":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-27","evidence_available_at_that_date":"Thin-float construction theme later produced strong MFE, but without non-price Green evidence the useful calibration is a 4B/positioning overlay, not a positive score promotion.","evidence_source":"public policy/PF-liquidity event + stock-web OHLC atlas; no live candidate research","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002410/2024.csv","profile_path":"atlas/symbol_profiles/002/002410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-27","entry_price":1611,"MFE_30D_pct":10.18,"MFE_90D_pct":10.18,"MFE_180D_pct":160.4,"MFE_1Y_pct":160.4,"MFE_2Y_pct":null,"MAE_30D_pct":-16.2,"MAE_90D_pct":-25.64,"MAE_180D_pct":-38.86,"MAE_1Y_pct":-38.86,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-13","peak_price":4195,"drawdown_after_peak_pct":-41.6,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.69,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"full_window_4B_late_after_theme_blowoff","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"false_break_or_theme_watch_only","trigger_outcome_label":"thin_float_policy_theme_created_return_but_large_mae_and_blowoff","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L13_C30_002410_POLICY_THEME_THIN_FLOAT::2024-03-27::1611","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L13_C30_002780_T_STAGE2_20240327","case_id":"R10L13_C30_002780_NO_CONVERSION_DRIFT_DOWN","symbol":"002780","company_name":"진흥기업","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_PF_SURVIVOR_RESIDUAL","sector":"construction_realestate_housing","primary_archetype":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-27","evidence_available_at_that_date":"Sector policy support existed, but the name had no observed case-date margin bridge, backlog conversion, or contract-quality confirmation; price drifted lower.","evidence_source":"public policy/PF-liquidity event + stock-web OHLC atlas; no live candidate research","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002780/2024.csv","profile_path":"atlas/symbol_profiles/002/002780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-27","entry_price":1004,"MFE_30D_pct":0.5,"MFE_90D_pct":0.5,"MFE_180D_pct":0.5,"MFE_1Y_pct":0.5,"MFE_2Y_pct":null,"MAE_30D_pct":-7.77,"MAE_90D_pct":-13.35,"MAE_180D_pct":-20.62,"MAE_1Y_pct":-20.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-28","peak_price":1009,"drawdown_after_peak_pct":-20.91,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"negative_alignment_no_full_4B_needed","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_optionality_failed_without_contract_or_margin_evidence","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L13_C30_002780_NO_CONVERSION_DRIFT_DOWN::2024-03-27::1004","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L13_C30_025950_T_STAGE2_20240327","case_id":"R10L13_C30_025950_EARLY_BLOWOFF_FAIL","symbol":"025950","company_name":"동신건설","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_PF_SURVIVOR_RESIDUAL","sector":"construction_realestate_housing","primary_archetype":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-27","evidence_available_at_that_date":"The 2024 policy support date arrived after an already-hot small-cap move; there was no case-date PF repair or margin bridge, and MAE overwhelmed the modest MFE.","evidence_source":"public policy/PF-liquidity event + stock-web OHLC atlas; no live candidate research","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/025/025950/2024.csv","profile_path":"atlas/symbol_profiles/025/025950.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-27","entry_price":29000,"MFE_30D_pct":5.17,"MFE_90D_pct":5.17,"MFE_180D_pct":5.17,"MFE_1Y_pct":5.17,"MFE_2Y_pct":null,"MAE_30D_pct":-35.9,"MAE_90D_pct":-39.55,"MAE_180D_pct":-39.55,"MAE_1Y_pct":-39.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-02","peak_price":30500,"drawdown_after_peak_pct":-42.52,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_should_block_positive_stage","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"early_spike_failed_and_high_mae_confirmed_no_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L13_C30_025950_EARLY_BLOWOFF_FAIL::2024-03-27::29000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L13_C30_010780_POLICY_SUPPORT_NO_PF_CONVERSION","trigger_id":"R10L13_C30_010780_T_STAGE2_20240327","symbol":"010780","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":35,"margin_bridge_score":15,"revision_score":10,"relative_strength_score":55,"customer_quality_score":20,"policy_or_regulatory_score":70,"valuation_repricing_score":30,"execution_risk_score":60,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":20,"accounting_trust_risk_score":25},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":30,"margin_bridge_score":10,"revision_score":10,"relative_strength_score":40,"customer_quality_score":20,"policy_or_regulatory_score":55,"valuation_repricing_score":25,"execution_risk_score":70,"legal_or_contract_risk_score":40,"dilution_cb_risk_score":20,"accounting_trust_risk_score":25},"weighted_score_after":61,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","relative_strength_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C30 small-cap construction policy/theme evidence is haircut unless PF exposure repair, cash collection, margin bridge, and contract-quality evidence are present.","MFE_90D_pct":4.1,"MAE_90D_pct":-30.43,"score_return_alignment_label":"policy_support_did_not_convert_to_margin_or_balance_sheet_repair","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L13_C30_013360_SMALLCAP_POLICY_BLOWOFF","trigger_id":"R10L13_C30_013360_T_STAGE2_20240327","symbol":"013360","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":15,"backlog_visibility_score":20,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":80,"customer_quality_score":10,"policy_or_regulatory_score":75,"valuation_repricing_score":45,"execution_risk_score":65,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":20,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":55,"customer_quality_score":10,"policy_or_regulatory_score":55,"valuation_repricing_score":35,"execution_risk_score":75,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_after":58,"stage_label_after":"Stage2-Theme-Watch","changed_components":["policy_or_regulatory_score","relative_strength_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C30 small-cap construction policy/theme evidence is haircut unless PF exposure repair, cash collection, margin bridge, and contract-quality evidence are present.","MFE_90D_pct":46.8,"MAE_90D_pct":-7.5,"score_return_alignment_label":"huge_price_move_without_confirmed_pf_or_margin_evidence","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L13_C30_001260_POLICY_THEME_HIGH_MFE","trigger_id":"R10L13_C30_001260_T_STAGE2_20240327","symbol":"001260","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":15,"backlog_visibility_score":25,"margin_bridge_score":10,"revision_score":5,"relative_strength_score":75,"customer_quality_score":10,"policy_or_regulatory_score":75,"valuation_repricing_score":40,"execution_risk_score":60,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":20,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":55,"customer_quality_score":10,"policy_or_regulatory_score":55,"valuation_repricing_score":30,"execution_risk_score":70,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_after":59,"stage_label_after":"Stage2-Theme-Watch","changed_components":["policy_or_regulatory_score","relative_strength_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C30 small-cap construction policy/theme evidence is haircut unless PF exposure repair, cash collection, margin bridge, and contract-quality evidence are present.","MFE_90D_pct":34.01,"MAE_90D_pct":-11.29,"score_return_alignment_label":"theme_beta_captured_but_green_promotion_not_supported","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L13_C30_002410_POLICY_THEME_THIN_FLOAT","trigger_id":"R10L13_C30_002410_T_STAGE2_20240327","symbol":"002410","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":15,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":85,"customer_quality_score":5,"policy_or_regulatory_score":75,"valuation_repricing_score":45,"execution_risk_score":70,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":15,"accounting_trust_risk_score":25},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":15,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":55,"customer_quality_score":5,"policy_or_regulatory_score":55,"valuation_repricing_score":35,"execution_risk_score":80,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":15,"accounting_trust_risk_score":25},"weighted_score_after":57,"stage_label_after":"Stage2-Theme-Watch","changed_components":["policy_or_regulatory_score","relative_strength_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C30 small-cap construction policy/theme evidence is haircut unless PF exposure repair, cash collection, margin bridge, and contract-quality evidence are present.","MFE_90D_pct":10.18,"MAE_90D_pct":-25.64,"score_return_alignment_label":"thin_float_policy_theme_created_return_but_large_mae_and_blowoff","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L13_C30_002780_NO_CONVERSION_DRIFT_DOWN","trigger_id":"R10L13_C30_002780_T_STAGE2_20240327","symbol":"002780","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":10,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":25,"customer_quality_score":5,"policy_or_regulatory_score":70,"valuation_repricing_score":15,"execution_risk_score":75,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":15,"accounting_trust_risk_score":30},"weighted_score_before":67,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":10,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":15,"customer_quality_score":5,"policy_or_regulatory_score":45,"valuation_repricing_score":10,"execution_risk_score":85,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":15,"accounting_trust_risk_score":30},"weighted_score_after":50,"stage_label_after":"Stage1/2-Watch","changed_components":["policy_or_regulatory_score","relative_strength_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C30 small-cap construction policy/theme evidence is haircut unless PF exposure repair, cash collection, margin bridge, and contract-quality evidence are present.","MFE_90D_pct":0.5,"MAE_90D_pct":-13.35,"score_return_alignment_label":"policy_optionality_failed_without_contract_or_margin_evidence","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L13_C30_025950_EARLY_BLOWOFF_FAIL","trigger_id":"R10L13_C30_025950_T_STAGE2_20240327","symbol":"025950","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":10,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":80,"customer_quality_score":5,"policy_or_regulatory_score":70,"valuation_repricing_score":45,"execution_risk_score":85,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":10,"accounting_trust_risk_score":35},"weighted_score_before":71,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":10,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":35,"customer_quality_score":5,"policy_or_regulatory_score":45,"valuation_repricing_score":25,"execution_risk_score":90,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":10,"accounting_trust_risk_score":35},"weighted_score_after":49,"stage_label_after":"Stage1/2-Watch","changed_components":["policy_or_regulatory_score","relative_strength_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C30 small-cap construction policy/theme evidence is haircut unless PF exposure repair, cash collection, margin bridge, and contract-quality evidence are present.","MFE_90D_pct":5.17,"MAE_90D_pct":-39.55,"score_return_alignment_label":"early_spike_failed_and_high_mae_confirmed_no_green","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R10","loop":"13","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","scheduled_round":"R10","scheduled_loop":"13","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"same_archetype_new_symbol_count":6,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":3,"counterexample_count":3,"current_profile_error_count":6,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["policy_theme_false_positive","4B_too_late_after_price_only_blowoff","high_MAE_success_not_green"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"diversity_score_summary":"6 new symbols inside R10/C30; prior R10 loops covered large/mid builders, this loop adds small-cap construction theme/PF residuals."}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_loop = 13
next_round = R11
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
primary_price_source = Songdaiki/stock-web
manifest = atlas/manifest.json
schema = atlas/schema.json
universe = atlas/universe/all_symbols.csv
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

Key stock-web files read for this loop:

```text
atlas/manifest.json
atlas/symbol_profiles/010/010780.json
atlas/symbol_profiles/013/013360.json
atlas/symbol_profiles/001/001260.json
atlas/symbol_profiles/002/002410.json
atlas/symbol_profiles/002/002780.json
atlas/symbol_profiles/025/025950.json
atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv
atlas/ohlcv_tradable_by_symbol_year/013/013360/2024.csv
atlas/ohlcv_tradable_by_symbol_year/001/001260/2024.csv
atlas/ohlcv_tradable_by_symbol_year/002/002410/2024.csv
atlas/ohlcv_tradable_by_symbol_year/002/002780/2024.csv
atlas/ohlcv_tradable_by_symbol_year/025/025950/2024.csv
```

