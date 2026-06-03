# E2R V12 No-Repeat Standalone Residual Research
## R10 / L9 / C30 — Construction PF balance-sheet break / workout-support 4B·4C guard

metadata:
```text
selected_round: R10
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: CONSTRUCTION_PF_LIQUIDITY_WORKOUT_SUPPORT_4B_4C_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_4C_gap_fill|pf_balance_sheet_repair_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_construction_pf_liquidity_workout_2023_2024_research.md
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

This run avoids those top-covered C30 symbols and adds 009410, 034300, and 047040.  
Each row uses a new `C30 + symbol + trigger_type + entry_date` hard key:
```text
C30 + 009410 + 4C-watch + 2023-12-28
C30 + 034300 + Stage3-Yellow + 2024-02-15
C30 + 047040 + 4B-local-price-only + 2024-07-18
```

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
009410 태영건설: distress window is before 2024-10-31 corporate-action candidate; post-halt/post-candidate path is excluded from aggregate calibration.
034300 신세계건설: selected post-2024-02-06 forward window clean; corporate-action candidate is before trigger window.
047040 대우건설: selected 2024 forward window clean; corporate-action candidates are historical and outside selected trigger window.
```

## 3. Research thesis

C30 should distinguish balance-sheet repair from balance-sheet stress traded as a rebound:

```text
PF exposure / contingent guarantee / unsold inventory
→ debt maturity and refinancing path
→ sponsor support quality or workout terms
→ orderbook-to-cash conversion and working-capital drain
→ gross margin and revision bridge
→ Yellow / 4B / 4C-watch routing
```

A PF book is a building with hidden basement water. A headline pump can move the water for a day, but Green needs the foundation repaired: exposure down, maturities extended, cash collected and margins revised.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C30_009410_TAEYOUNG_20231228_PF_WORKOUT_4C_WATCH | 009410 | pf_workout_balance_sheet_break_4c_watch_with_restructuring_squeeze_caveat | 2023-12-28 | 2315 | 4110 on 2024-01-11 | 2180 on 2024-01-25 | 77.54% | 77.54% | 77.54% | -5.83% | -46.96% |
| C30_034300_SHINSEGAEEC_20240215_PF_SUPPORT_FALSE_GREEN | 034300 | pf_support_recap_false_green_counterexample | 2024-02-15 | 12040 | 14600 on 2024-06-28 | 10100 on 2024-04-15 | 6.15% | 21.26% | 21.26% | -16.11% | -23.63% |
| C30_047040_DAEWOOEC_20240718_CONSTRUCTION_POLICY_BETA_4B | 047040 | construction_policy_beta_price_premium_counterexample | 2024-07-18 | 4250 | 4965 on 2024-07-18 | 3545 on 2024-08-05 | 16.82% | 16.82% | 16.82% | -16.59% | -28.6% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a clean Stage2/Green positive.
- C30 Green should require PF exposure reduction, refinancing or maturity extension, sponsor support quality, unsold inventory/cash collection improvement and margin/revision confirmation.
- 034300 is the false-Green/Yellow guard: support helped stabilize the equity, but the balance-sheet-to-margin bridge was not enough to justify Green.
- 047040 is the sector-beta guard: construction policy/rate beta is not the same as PF balance-sheet repair.

### 4B
- 047040 fills the construction policy-beta 4B pocket. The trigger had immediate upside but also a sharp local drawdown when PF-risk repair evidence did not follow.
- 034300 shows that sponsor support and capital measures need to be separated from true cash conversion and margin repair.

### 4C
- 009410 is classified as 4C-watch with a restructuring-squeeze caveat. The workout thesis was a real balance-sheet break, but distressed names can rally sharply after restructuring headlines; therefore the row should block positive Stage2/Green rather than be treated as a clean short-term short signal.
- Hard 4C should require durable break evidence such as workout/covenant breach, refinancing failure, creditor control, capital impairment, default or material contract/cash-flow break.

## 6. Raw component score breakdown

```json
{
  "C30_009410_TAEYOUNG_20231228_PF_WORKOUT_4C_WATCH": {
    "PF_exposure_visibility": 10,
    "covenant_or_workout_risk": 11,
    "information_confidence": 4,
    "liquidity_refinancing_stress": 11,
    "margin_revision_bridge": 1,
    "market_mispricing": 3,
    "orderbook_cash_conversion": 2,
    "sponsor_support_quality": 4,
    "total": 46,
    "valuation_rerating_runway": 0
  },
  "C30_034300_SHINSEGAEEC_20240215_PF_SUPPORT_FALSE_GREEN": {
    "PF_exposure_visibility": 8,
    "covenant_or_workout_risk": 6,
    "information_confidence": 3,
    "liquidity_refinancing_stress": 8,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "orderbook_cash_conversion": 3,
    "sponsor_support_quality": 7,
    "total": 42,
    "valuation_rerating_runway": 1
  },
  "C30_047040_DAEWOOEC_20240718_CONSTRUCTION_POLICY_BETA_4B": {
    "PF_exposure_visibility": 5,
    "covenant_or_workout_risk": 4,
    "information_confidence": 3,
    "liquidity_refinancing_stress": 5,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "orderbook_cash_conversion": 3,
    "sponsor_support_quality": 3,
    "total": 30,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C30 guard:
```text
if construction_price_rebound and no PF_exposure_refinancing_cash_margin_repair:
    block_stage2_green_positive = true
    route_to_stage3_yellow_or_local_4B = true

if workout_or_covenant_break and refinancing_gap_visible:
    route_to_4C_watch_or_hard_4C = true
    add_restructuring_squeeze_caveat = true

if sponsor_support and no cash_conversion_margin_revision_bridge:
    keep_yellow_or_4B_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 034300 / 2024-02-15: sponsor support can be over-promoted if price confirmation substitutes for PF exposure reduction and cash-margin repair.
- 047040 / 2024-07-18: construction policy beta can look like recovery, but fails without company-level PF and margin evidence.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -5.83, "MAE_30D_pct": -5.83, "MAE_90D_pct": -5.83, "MFE_180D_pct": 77.54, "MFE_30D_pct": 77.54, "MFE_90D_pct": 77.54, "calibration_caveat": "restructuring_squeeze_and_post_halt_corporate_action_excluded", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": false, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_009410_TAEYOUNG_20231228_PF_WORKOUT_4C_WATCH", "case_role": "pf_workout_balance_sheet_break_4c_watch_with_restructuring_squeeze_caveat", "company_name": "태영건설", "corporate_action_window_status": "pre-2024-10-31 forward path used; profile has corporate-action candidate 2024-10-31 after the selected distress window, so post-relisting window is excluded from calibration aggregate", "current_profile_error": false, "current_profile_verdict": "PF workout and liquidity stress should route to 4C-watch or hard 4C when short-term refinancing, bond repayment, PF guarantee exposure and sponsor support uncertainty dominate. This row also carries a restructuring-squeeze caveat: distress names can rally after workout news, so the 4C label is a thesis-risk block rather than a clean short-term downside signal.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.96, "entry_date": "2023-12-28", "entry_price": 2315, "evidence_family": "construction_pf_workout_balance_sheet_break_with_restructuring_liquidity_gap", "evidence_url_pending": false, "fine_archetype_id": "CONSTRUCTION_PF_LIQUIDITY_WORKOUT_SUPPORT_4B_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "low_date_180d": "2024-01-25", "low_price_180d": 2180, "peak_date": "2024-01-11", "peak_price": 4110, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/009/009410.json", "raw_component_score_breakdown": {"PF_exposure_visibility": 10, "covenant_or_workout_risk": 11, "information_confidence": 4, "liquidity_refinancing_stress": 11, "margin_revision_bridge": 1, "market_mispricing": 3, "orderbook_cash_conversion": 2, "sponsor_support_quality": 4, "total": 46, "valuation_rerating_runway": 0}, "reuse_reason": null, "same_entry_group_id": "C30_009410_TAEYOUNG_20231228_PF_WORKOUT_4C_WATCH", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R10", "source_proxy_only": false, "stage2_evidence_fields": ["construction_PF_exposure_and_liquidity_visibility", "debt_maturity_refinancing_or_sponsor_support_quality", "cash_conversion_unsold_inventory_margin_revision_route"], "stage3_evidence_fields": ["PF_exposure_reduction_required", "maturity_extension_or_refinancing_confirmation_required", "cash_conversion_margin_revision_bridge_required"], "stage4b_evidence_fields": ["PF_support_or_policy_beta_price_premium", "balance_sheet_repair_not_proven", "post_peak_drawdown"], "stage4c_evidence_fields": ["workout_or_covenant_break", "refinancing_failure_or_support_gap", "cash_conversion_margin_revision_bridge_failure"], "symbol": "009410", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv", "trigger_date": "2023-12-28", "trigger_type": "4C-watch", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -16.11, "MAE_30D_pct": -13.54, "MAE_90D_pct": -16.11, "MFE_180D_pct": 21.26, "MFE_30D_pct": 6.15, "MFE_90D_pct": 21.26, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_034300_SHINSEGAEEC_20240215_PF_SUPPORT_FALSE_GREEN", "case_role": "pf_support_recap_false_green_counterexample", "company_name": "신세계건설", "corporate_action_window_status": "selected post-2024-02-06 forward window clean; corporate-action candidate is before trigger window", "current_profile_error": true, "current_profile_verdict": "Parent/sponsor support can stabilize a PF-stressed construction equity, but it should stay Yellow unless leverage, PF guarantee exposure, cash conversion, debt maturity, unsold inventory and margin/revision evidence improve. Price confirmation after support should not substitute for balance-sheet repair.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -23.63, "entry_date": "2024-02-15", "entry_price": 12040, "evidence_family": "construction_pf_support_recap_price_confirmation_without_cash_conversion_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "CONSTRUCTION_PF_LIQUIDITY_WORKOUT_SUPPORT_4B_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "low_date_180d": "2024-04-15", "low_price_180d": 10100, "peak_date": "2024-06-28", "peak_price": 14600, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/034/034300.json", "raw_component_score_breakdown": {"PF_exposure_visibility": 8, "covenant_or_workout_risk": 6, "information_confidence": 3, "liquidity_refinancing_stress": 8, "margin_revision_bridge": 2, "market_mispricing": 4, "orderbook_cash_conversion": 3, "sponsor_support_quality": 7, "total": 42, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C30_034300_SHINSEGAEEC_20240215_PF_SUPPORT_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R10", "source_proxy_only": false, "stage2_evidence_fields": ["construction_PF_exposure_and_liquidity_visibility", "debt_maturity_refinancing_or_sponsor_support_quality", "cash_conversion_unsold_inventory_margin_revision_route"], "stage3_evidence_fields": ["PF_exposure_reduction_required", "maturity_extension_or_refinancing_confirmation_required", "cash_conversion_margin_revision_bridge_required"], "stage4b_evidence_fields": ["PF_support_or_policy_beta_price_premium", "balance_sheet_repair_not_proven", "post_peak_drawdown"], "stage4c_evidence_fields": ["workout_or_covenant_break", "refinancing_failure_or_support_gap", "cash_conversion_margin_revision_bridge_failure"], "symbol": "034300", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv", "trigger_date": "2024-02-15", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -16.59, "MAE_30D_pct": -16.59, "MAE_90D_pct": -16.59, "MFE_180D_pct": 16.82, "MFE_30D_pct": 16.82, "MFE_90D_pct": 16.82, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_047040_DAEWOOEC_20240718_CONSTRUCTION_POLICY_BETA_4B", "case_role": "construction_policy_beta_price_premium_counterexample", "company_name": "대우건설", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are historical and outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Construction-policy or rate-cut beta should route to local 4B/counterexample when it is not backed by PF balance-sheet repair, unsold inventory reduction, debt maturity extension, orderbook cash conversion and margin/revision evidence. A sector beta rally is not the same as PF-risk repair.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -28.6, "entry_date": "2024-07-18", "entry_price": 4250, "evidence_family": "construction_policy_beta_price_premium_without_pf_balance_sheet_cash_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "CONSTRUCTION_PF_LIQUIDITY_WORKOUT_SUPPORT_4B_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "low_date_180d": "2024-08-05", "low_price_180d": 3545, "peak_date": "2024-07-18", "peak_price": 4965, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/047/047040.json", "raw_component_score_breakdown": {"PF_exposure_visibility": 5, "covenant_or_workout_risk": 4, "information_confidence": 3, "liquidity_refinancing_stress": 5, "margin_revision_bridge": 2, "market_mispricing": 4, "orderbook_cash_conversion": 3, "sponsor_support_quality": 3, "total": 30, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C30_047040_DAEWOOEC_20240718_CONSTRUCTION_POLICY_BETA_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R10", "source_proxy_only": false, "stage2_evidence_fields": ["construction_PF_exposure_and_liquidity_visibility", "debt_maturity_refinancing_or_sponsor_support_quality", "cash_conversion_unsold_inventory_margin_revision_route"], "stage3_evidence_fields": ["PF_exposure_reduction_required", "maturity_extension_or_refinancing_confirmation_required", "cash_conversion_margin_revision_bridge_required"], "stage4b_evidence_fields": ["PF_support_or_policy_beta_price_premium", "balance_sheet_repair_not_proven", "post_peak_drawdown"], "stage4c_evidence_fields": ["workout_or_covenant_break", "refinancing_failure_or_support_gap", "cash_conversion_margin_revision_bridge_failure"], "symbol": "047040", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv", "trigger_date": "2024-07-18", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 2,
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "caveated_case_count": 1,
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "CONSTRUCTION_PF_LIQUIDITY_WORKOUT_SUPPORT_4B_4C_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "loop_contribution_label": "construction_pf_balance_sheet_break_workout_support_policy_beta_new_symbols",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R10",
  "shadow_rule_candidate": "C30 rows should block Stage2/Green when PF balance-sheet repair is not visible: price rebound, sponsor support or policy beta must be tied to PF exposure reduction, refinancing/maturity extension, unsold inventory reduction, cash conversion and margin/revision bridge; hard 4C/workout rows should also mark restructuring-squeeze caveat rather than treating 4C as a clean short-term downside predictor.",
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
3. Treat 009410 as caveated for aggregate full-window calibration because distress/restructuring squeeze and post-2024-10-31 corporate-action window require separate handling.
4. Add C30-specific PF exposure / refinancing / sponsor-support / cash-conversion / margin-revision / 4B-4C guard only as a shadow candidate until more rows exist.

Candidate rule:
- C30_BLOCK_GREEN_WITHOUT_PF_REFINANCING_CASH_MARGIN_REPAIR
- C30_SPONSOR_SUPPORT_WITHOUT_CASH_CONVERSION_STAYS_YELLOW_4B
- C30_WORKOUT_COVENANT_BREAK_ROUTES_TO_4C_WATCH_WITH_RESTRUCTURING_SQUEEZE_CAVEAT
- C30_POLICY_BETA_WITHOUT_BALANCE_SHEET_REPAIR_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

