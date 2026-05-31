# E2R V12 No-Repeat Standalone Residual Research
## R10 / L9 / C30 — Construction PF balance-sheet break / workout-vs-overhang divergence guard

metadata:
```text
selected_round: R10
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_WORKOUT_OVERHANG_BUILDER_DIVERGENCE_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4C_hard_break_guard|false_4C_sector_overhang_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_pf_workout_overhang_builder_divergence_2023_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK current coverage:
rows=28, symbols=6, date range=2022-01-12~2024-08-27, good/bad S2=5/0, 4B/4C=0/4
top covered symbols: 006360(6), 294870(5), 375500(4), UNKNOWN_SYMBOL(3), 000720(2)
```

This run avoids those top-covered C30 symbols and adds 009410, 010780, and 047040.  
Each row uses a new `C30 + symbol + trigger_type + entry_date` hard key.

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
symbol_count: 5414
active_like_symbol_count: 2868
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
009410 태영건설: selected 2023-12-28~2024-03-13 window is pre-2024-10-31 corporate-action candidate; full post-resumption forward window is blocked.
010780 아이에스동서: selected 2023/2024 forward window clean; historical corporate-action candidates are outside selected test window.
047040 대우건설: selected 2023/2024 forward window clean; corporate-action candidates are 2001-07-13, 2003-11-18, 2011-01-18 and outside selected test window.
```

## 3. Research thesis

C30 should separate **company-specific PF break** from **sector PF overhang**:

```text
construction / real-estate PF stress
→ company-specific PF maturity stack and refinancing need
→ creditor workout, covenant breach or refinancing failure
→ unsold inventory / project cash recovery / asset-sale visibility
→ gross margin and revision bridge
→ hard 4C or Yellow/4B-watch
```

PF stress is smoke. Hard 4C should require the fire inside the company: a creditor process, broken refinancing, project cash drain, or margin revision collapse. Sector smoke alone should not burn every builder.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD | calibration |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C30_009410_TAEYOUNG_20231228_PF_WORKOUT_HARD_4C_PARTIAL_WINDOW | 009410 | positive_pf_workout_hard_4c_with_partial_pre_corporate_action_window | 2023-12-28 | 2315 | 4110 on 2024-01-11 | 2180 on 2024-01-25 | 77.54% | 77.54% | 77.54% | -5.83% | -46.96% | partial |
| C30_010780_ISDONGSEO_20231026_PF_OVERHANG_FALSE_4C | 010780 | pf_overhang_false_4c_resilient_balance_sheet_counterexample | 2023-10-26 | 26500 | 31200 on 2024-03-22 | 23250 on 2024-01-18 | 10.0% | 11.32% | 17.74% | -12.26% | -21.31% | True |
| C30_047040_DAEWOOE&C_20231228_PF_SECTOR_CONTAGION_FALSE_4C | 047040 | large_builder_pf_sector_contagion_false_4c_counterexample | 2023-12-28 | 4145 | 4965 on 2024-07-18 | 3580 on 2024-04-17 | 4.7% | 4.7% | 19.78% | -13.63% | -18.33% | True |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a clean Stage2/Green positive.
- C30 Green should require a clearly repaired PF maturity stack, refinancing terms, creditor confidence, unsold inventory cash recovery, asset-sale visibility and margin/revision confirmation.
- 010780 and 047040 are false-4C counterexamples: sector PF fear existed, but company-specific hard break evidence was not visible enough to justify automatic hard-4C routing.

### 4B
- PF relief bounces should be treated as 4B-watch unless there is fresh non-price proof that refinancing risk, unsold inventory and margin revisions have improved.
- 009410 had a large relief bounce after the hard event, but that bounce was not Stage2 because the balance-sheet process itself remained the core evidence.
- 047040 shows why broad PF contagion should not be treated as a hard break when a large builder lacks company-specific creditor/workout evidence.

### 4C
- 009410 is the hard-break anchor, with partial calibration only because the later 2024-10-31 corporate-action candidate blocks the full forward window.
- Hard 4C should be triggered by creditor/workout/refinancing failure evidence, not by sector beta alone.
- The residual model error is asymmetric: too loose creates false Green on broken balance sheets, but too broad creates false 4C on resilient builders.

## 6. Raw component score breakdown

```json
{
  "C30_009410_TAEYOUNG_20231228_PF_WORKOUT_HARD_4C_PARTIAL_WINDOW": {
    "asset_sale_cash_recovery_visibility": 2,
    "company_specific_refinancing_failure": 12,
    "creditor_workout_or_covenant_break": 11,
    "information_confidence": 4,
    "margin_revision_bridge": 1,
    "market_mispricing": 3,
    "pf_liquidity_stress": 12,
    "total": 45,
    "valuation_rerating_runway": 0
  },
  "C30_010780_ISDONGSEO_20231026_PF_OVERHANG_FALSE_4C": {
    "asset_sale_cash_recovery_visibility": 5,
    "company_specific_refinancing_failure": 2,
    "creditor_workout_or_covenant_break": 1,
    "information_confidence": 3,
    "margin_revision_bridge": 4,
    "market_mispricing": 5,
    "pf_liquidity_stress": 6,
    "total": 29,
    "valuation_rerating_runway": 3
  },
  "C30_047040_DAEWOOE&C_20231228_PF_SECTOR_CONTAGION_FALSE_4C": {
    "asset_sale_cash_recovery_visibility": 6,
    "company_specific_refinancing_failure": 1,
    "creditor_workout_or_covenant_break": 0,
    "information_confidence": 3,
    "margin_revision_bridge": 4,
    "market_mispricing": 6,
    "pf_liquidity_stress": 5,
    "total": 29,
    "valuation_rerating_runway": 4
  }
}
```

## 7. Current calibrated profile stress test

Suggested C30 guard:
```text
if pf_sector_overhang and no company_specific_refinancing_failure:
    block_hard_4c = true
    route_to_stage3_yellow_or_4b_watch = true

if creditor_workout_or_covenant_break and refinancing_failure_visible:
    route_to_hard_4c = true
    block_stage2_green_positive = true

if relief_bounce_after_pf_break and no creditor_terms_cash_recovery_margin_revision_bridge:
    keep_as_4b_relief_bounce_not_stage2 = true
```

Residual errors:
```text
current_profile_error_count = 2
- 010780 / 2023-10-26: broad PF overhang can be over-routed to hard 4C if the model does not require company-specific refinancing failure.
- 047040 / 2023-12-28: large-builder sector contagion can be over-penalized when there is no direct creditor/workout/covenant evidence.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -5.83, "MAE_30D_pct": -5.83, "MAE_90D_pct": -5.83, "MFE_180D_pct": 77.54, "MFE_30D_pct": 77.54, "MFE_90D_pct": 77.54, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": "partial", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_009410_TAEYOUNG_20231228_PF_WORKOUT_HARD_4C_PARTIAL_WINDOW", "case_role": "positive_pf_workout_hard_4c_with_partial_pre_corporate_action_window", "company_name": "태영건설", "corporate_action_window_status": "partial_pre_2024_10_31_window; corporate-action candidates are 2007-05-03, 2020-09-22, 2024-10-31; 2023-12-28~2024-03-13 rows are used and full 180D post-resumption window is blocked", "current_profile_error": false, "current_profile_verdict": "Hard 4C routing is correct when PF liquidity stress moves from sector overhang into company-level workout / creditor process. The violent post-trigger bounce does not convert it into Stage2 because financing finality, project cash recovery, creditor terms, dilution and margin/revision evidence are structurally impaired. Aggregate use should be partial because a later 2024-10-31 corporate-action candidate blocks full forward-window calibration.", "dedupe_for_aggregate": false, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.96, "entry_date": "2023-12-28", "entry_price": 2315, "evidence_family": "pf_workout_liquidity_covenant_balance_sheet_break_partial_window", "evidence_url_pending": false, "fine_archetype_id": "PF_WORKOUT_OVERHANG_BUILDER_DIVERGENCE_GUARD", "forward_window_trading_days": 52, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "low_date_180d": "2024-01-25", "low_price_180d": 2180, "peak_date": "2024-01-11", "peak_price": 4110, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/009/009410.json", "raw_component_score_breakdown": {"asset_sale_cash_recovery_visibility": 2, "company_specific_refinancing_failure": 12, "creditor_workout_or_covenant_break": 11, "information_confidence": 4, "margin_revision_bridge": 1, "market_mispricing": 3, "pf_liquidity_stress": 12, "total": 45, "valuation_rerating_runway": 0}, "reuse_reason": null, "same_entry_group_id": "C30_009410_TAEYOUNG_20231228_PF_WORKOUT_HARD_4C_PARTIAL_WINDOW", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R10", "source_proxy_only": false, "stage2_evidence_fields": ["construction_pf_liquidity_or_refinancing_attention", "company_specific_project_cashflow_and_debt_maturity_required", "asset_sale_creditor_terms_margin_revision_route"], "stage3_evidence_fields": ["company_specific_pf_maturity_stack_required", "refinancing_creditor_terms_required", "unsold_inventory_cash_recovery_margin_revision_required"], "stage4b_evidence_fields": ["sector_pf_contagion_price_premium_or_relief_bounce", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["workout_or_creditor_process", "refinancing_failure_or_covenant_break", "project_cash_drain_and_margin_revision_break"], "symbol": "009410", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv", "trigger_date": "2023-12-28", "trigger_type": "4C-hard-thesis-break", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -12.26, "MAE_30D_pct": -5.66, "MAE_90D_pct": -12.26, "MFE_180D_pct": 17.74, "MFE_30D_pct": 10.0, "MFE_90D_pct": 11.32, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_010780_ISDONGSEO_20231026_PF_OVERHANG_FALSE_4C", "case_role": "pf_overhang_false_4c_resilient_balance_sheet_counterexample", "company_name": "아이에스동서", "corporate_action_window_status": "clean_2023_2024_forward_window; selected rows avoid historical corporate-action candidates", "current_profile_error": true, "current_profile_verdict": "Sector PF overhang should not automatically route to hard 4C. Without company-specific refinancing failure, creditor workout, covenant breach, unsold-inventory cash drain or margin/revision collapse, this should remain Yellow/overhang rather than hard break.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -21.31, "entry_date": "2023-10-26", "entry_price": 26500, "evidence_family": "construction_pf_sector_overhang_without_company_specific_liquidity_break", "evidence_url_pending": false, "fine_archetype_id": "PF_WORKOUT_OVERHANG_BUILDER_DIVERGENCE_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "low_date_180d": "2024-01-18", "low_price_180d": 23250, "peak_date": "2024-03-22", "peak_price": 31200, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/010/010780.json", "raw_component_score_breakdown": {"asset_sale_cash_recovery_visibility": 5, "company_specific_refinancing_failure": 2, "creditor_workout_or_covenant_break": 1, "information_confidence": 3, "margin_revision_bridge": 4, "market_mispricing": 5, "pf_liquidity_stress": 6, "total": 29, "valuation_rerating_runway": 3}, "reuse_reason": null, "same_entry_group_id": "C30_010780_ISDONGSEO_20231026_PF_OVERHANG_FALSE_4C", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R10", "source_proxy_only": false, "stage2_evidence_fields": ["construction_pf_liquidity_or_refinancing_attention", "company_specific_project_cashflow_and_debt_maturity_required", "asset_sale_creditor_terms_margin_revision_route"], "stage3_evidence_fields": ["company_specific_pf_maturity_stack_required", "refinancing_creditor_terms_required", "unsold_inventory_cash_recovery_margin_revision_required"], "stage4b_evidence_fields": ["sector_pf_contagion_price_premium_or_relief_bounce", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["workout_or_creditor_process", "refinancing_failure_or_covenant_break", "project_cash_drain_and_margin_revision_break"], "symbol": "010780", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010780/2023.csv", "trigger_date": "2023-10-26", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -13.63, "MAE_30D_pct": -6.63, "MAE_90D_pct": -13.03, "MFE_180D_pct": 19.78, "MFE_30D_pct": 4.7, "MFE_90D_pct": 4.7, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_047040_DAEWOOE&C_20231228_PF_SECTOR_CONTAGION_FALSE_4C", "case_role": "large_builder_pf_sector_contagion_false_4c_counterexample", "company_name": "대우건설", "corporate_action_window_status": "clean_2023_2024_forward_window; corporate-action candidates are 2001-07-13, 2003-11-18, 2011-01-18 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Large-builder PF contagion should not be treated as hard 4C when direct balance-sheet break, creditor workout, refinancing failure, covenant breach and project-level cash drain are absent. The row belongs in Yellow/4B-watch until company-specific liquidity evidence appears.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -18.33, "entry_date": "2023-12-28", "entry_price": 4145, "evidence_family": "large_builder_pf_sector_contagion_without_direct_balance_sheet_break", "evidence_url_pending": false, "fine_archetype_id": "PF_WORKOUT_OVERHANG_BUILDER_DIVERGENCE_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "low_date_180d": "2024-04-17", "low_price_180d": 3580, "peak_date": "2024-07-18", "peak_price": 4965, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/047/047040.json", "raw_component_score_breakdown": {"asset_sale_cash_recovery_visibility": 6, "company_specific_refinancing_failure": 1, "creditor_workout_or_covenant_break": 0, "information_confidence": 3, "margin_revision_bridge": 4, "market_mispricing": 6, "pf_liquidity_stress": 5, "total": 29, "valuation_rerating_runway": 4}, "reuse_reason": null, "same_entry_group_id": "C30_047040_DAEWOOE&C_20231228_PF_SECTOR_CONTAGION_FALSE_4C", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R10", "source_proxy_only": false, "stage2_evidence_fields": ["construction_pf_liquidity_or_refinancing_attention", "company_specific_project_cashflow_and_debt_maturity_required", "asset_sale_creditor_terms_margin_revision_route"], "stage3_evidence_fields": ["company_specific_pf_maturity_stack_required", "refinancing_creditor_terms_required", "unsold_inventory_cash_recovery_margin_revision_required"], "stage4b_evidence_fields": ["sector_pf_contagion_price_premium_or_relief_bounce", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["workout_or_creditor_process", "refinancing_failure_or_covenant_break", "project_cash_drain_and_margin_revision_break"], "symbol": "047040", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2023.csv", "trigger_date": "2023-12-28", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 2,
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "PF_WORKOUT_OVERHANG_BUILDER_DIVERGENCE_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "loop_contribution_label": "construction_pf_balance_sheet_break_workout_vs_sector_overhang_divergence",
  "new_independent_case_count": 3,
  "partial_calibration_case_count": 1,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R10",
  "shadow_rule_candidate": "C30 PF rows should route to hard 4C only when sector PF overhang becomes company-specific refinancing failure, creditor workout/covenant break, unsold-inventory cash drain or margin/revision break; broad PF contagion without company-specific liquidity failure should remain Yellow/4B-watch rather than hard 4C.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C30 + symbol + trigger_type + entry_date.
3. Treat 009410 as partial-calibration only because the full forward window crosses a later corporate-action candidate.
4. Add C30-specific PF workout / refinancing / creditor-process / sector-overhang false-4C guard only as a shadow candidate until more rows exist.

Candidate rule:
- C30_HARD_4C_REQUIRES_COMPANY_SPECIFIC_REFINANCING_FAILURE_OR_CREDITOR_PROCESS
- C30_SECTOR_PF_OVERHANG_WITHOUT_COMPANY_BREAK_STAYS_YELLOW_OR_4B
- C30_PF_RELIEF_BOUNCE_WITHOUT_CASH_RECOVERY_REVISION_IS_NOT_STAGE2
- C30_BLOCK_GREEN_ON_WORKOUT_COVENANT_PROJECT_CASH_BREAK

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

