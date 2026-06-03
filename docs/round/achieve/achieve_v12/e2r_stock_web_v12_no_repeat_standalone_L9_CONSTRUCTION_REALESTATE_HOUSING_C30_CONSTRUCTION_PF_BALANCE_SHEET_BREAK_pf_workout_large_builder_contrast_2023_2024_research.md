# E2R V12 No-Repeat Standalone Residual Research
## R10 / L9 / C30 — Construction PF balance-sheet break guard

metadata:
```text
selected_round: R10
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_WORKOUT_LARGE_BUILDER_CONTRAST_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|4C_structural_break|false_break_counterexample|balance_sheet_gate_refinement
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_pf_workout_large_builder_contrast_2023_2024_research.md
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

This run avoids those top-covered C30 symbols and adds 009410, 005960, and 047040.  
Each row uses a new `C30 + symbol + trigger_type + entry_date` hard key.

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
009410 태영건설: selected 2023-12-28 event window is structurally useful but post-restructuring comparability is blocked by a 2024-10-31 corporate-action candidate.
005960 동부건설: selected 2024 forward window is clean; corporate-action candidates are historical and outside selected test window.
047040 대우건설: selected 2024 forward window is clean; corporate-action candidates are historical and outside selected test window.
```

## 3. Research thesis

C30 should distinguish a real PF balance-sheet break from broad construction-sector fear:

```text
construction PF stress
→ direct PF exposure and guarantee load
→ debt maturity wall / refinancing bridge
→ asset-sale or parent/support quality
→ cash-flow, orderbook margin and covenant room
→ 4C break or false-break relief path
```

PF stress is not one storm cloud over every builder. It is a water leak through specific balance-sheet joints: guarantee exposure, near-term maturity, refinancing access, asset-sale liquidity, and cash-flow margin. The same rain can flood one basement and leave another only damp.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C30_009410_TAEYOUNG_20231228_PF_WORKOUT_STRUCTURAL_4C | 009410 | positive_pf_workout_structural_4c_success_with_trading_halt_caveat | 2023-12-28 | 2315 | 4110 on 2024-01-11 | 1935 on 2023-12-28 | 77.54% | 77.54% | 77.54% | -16.41% | -46.96% |
| C30_005960_DONGBU_20240117_PF_SYMPATHY_FALSE_GREEN_YELLOW | 005960 | pf_sympathy_false_green_counterexample | 2024-01-17 | 5340 | 5500 on 2024-02-19 | 4175 on 2024-09-09 | 3.0% | 3.0% | 3.0% | -21.82% | -24.09% |
| C30_047040_DAEWOO_20240117_LARGE_BUILDER_PF_FALSE_BREAK_COUNTEREXAMPLE | 047040 | large_builder_pf_false_break_counterexample | 2024-01-17 | 4010 | 4965 on 2024-07-18 | 3545 on 2024-08-05 | 4.24% | 4.24% | 23.82% | -11.6% | -28.6% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD should be treated as a clean Stage2/Green positive.
- C30 Green should require direct PF exposure analysis, maturity/refinancing bridge, cash-flow durability, orderbook margin and support-asset quality.
- 005960 stays Yellow: there was sector stress and later MAE, but not enough hard 4C proof from price alone.
- 047040 is a false-break counterexample: a large builder should not be mechanically routed to 4C solely because the sector is under PF stress.

### 4B
- 009410 had a speculative bounce after the workout shock; the bounce did not erase the 4C thesis break.
- 005960 belongs in 4B/Yellow watch unless refinancing and cash-flow bridge evidence improves.
- 047040 demonstrates the inverse guard: do not over-block large builders with stronger orderbook/liquidity evidence.

### 4C
- 009410 is the structural 4C anchor. The key signal is workout/liquidity-bridge failure, not the event-day price path.
- 009410 is marked limited because post-restructuring rows are not comparable after the 2024-10-31 corporate-action candidate.
- The C30 failure mode is balance-sheet conversion: PF exposure and debt maturity stop being a sector headline and become a funding-path break.

## 6. Raw component score breakdown

```json
{
  "C30_005960_DONGBU_20240117_PF_SYMPATHY_FALSE_GREEN_YELLOW": {
    "asset_sale_support_quality": 3,
    "balance_sheet_stress": 9,
    "information_confidence": 3,
    "market_mispricing": 4,
    "pf_liquidity_bridge_break": 8,
    "refinancing_visibility": 4,
    "total": 32,
    "valuation_rerating_runway": 1
  },
  "C30_009410_TAEYOUNG_20231228_PF_WORKOUT_STRUCTURAL_4C": {
    "asset_sale_support_quality": 3,
    "balance_sheet_stress": 12,
    "information_confidence": 4,
    "market_mispricing": 2,
    "pf_liquidity_bridge_break": 13,
    "refinancing_visibility": 3,
    "total": 37,
    "valuation_rerating_runway": 0
  },
  "C30_047040_DAEWOO_20240117_LARGE_BUILDER_PF_FALSE_BREAK_COUNTEREXAMPLE": {
    "asset_sale_support_quality": 5,
    "balance_sheet_stress": 5,
    "information_confidence": 3,
    "market_mispricing": 7,
    "pf_liquidity_bridge_break": 4,
    "refinancing_visibility": 7,
    "total": 35,
    "valuation_rerating_runway": 4
  }
}
```

## 7. Current calibrated profile stress test

Suggested C30 guard:
```text
if pf_workout_or_liquidity_bridge_failure:
    route_to_4c_structural_break = true
    block_stage2_green = true

if construction_pf_sympathy and no direct_refinancing_cashflow_margin_bridge:
    keep_stage3_yellow_or_4b_watch = true

if large_builder_has_distinguishable_liquidity_orderbook_margin_bridge:
    do_not_auto_route_to_4c = true
```

Residual errors:
```text
current_profile_error_count = 2
- 005960 / 2024-01-17: sector PF sympathy can be over-promoted if price stabilization substitutes for refinancing, cash-flow and orderbook-margin proof.
- 047040 / 2024-01-17: broad PF fear can be over-penalized if the model lacks a large-builder/direct-exposure contrast gate.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -16.41, "MAE_30D_pct": -16.41, "MAE_90D_pct": -16.41, "MFE_180D_pct": 77.54, "MFE_30D_pct": 77.54, "MFE_90D_pct": 77.54, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": "limited_pre_restructuring_event_window", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_009410_TAEYOUNG_20231228_PF_WORKOUT_STRUCTURAL_4C", "case_role": "positive_pf_workout_structural_4c_success_with_trading_halt_caveat", "company_name": "태영건설", "corporate_action_window_status": "limited_pre_restructuring_window; profile has corporate-action candidates 2007-05-03, 2020-09-22, 2024-10-31; 2024-10-31 restructuring/share-count break blocks post-restructuring comparability", "current_profile_error": false, "current_profile_verdict": "A PF workout/liquidity-bridge failure should route to structural 4C even when event-day volatility later creates a speculative bounce. This case is a thesis-break guard, not a long-entry Stage2/Green row.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.96, "entry_date": "2023-12-28", "entry_price": 2315, "evidence_family": "construction_pf_workout_liquidity_bridge_failure_structural_break", "evidence_url_pending": false, "fine_archetype_id": "PF_WORKOUT_LARGE_BUILDER_CONTRAST_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "low_date_180d": "2023-12-28", "low_price_180d": 1935, "peak_date": "2024-01-11", "peak_price": 4110, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/009/009410.json", "raw_component_score_breakdown": {"asset_sale_support_quality": 3, "balance_sheet_stress": 12, "information_confidence": 4, "market_mispricing": 2, "pf_liquidity_bridge_break": 13, "refinancing_visibility": 3, "total": 37, "valuation_rerating_runway": 0}, "reuse_reason": null, "same_entry_group_id": "C30_009410_TAEYOUNG_20231228_PF_WORKOUT_STRUCTURAL_4C", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R10", "source_proxy_only": false, "stage2_evidence_fields": ["construction_pf_balance_sheet_stress_attention", "refinancing_or_liquidity_bridge_visibility", "orderbook_margin_cashflow_recovery_signal"], "stage3_evidence_fields": ["direct_pf_exposure_required", "debt_maturity_refinancing_bridge_required", "cashflow_orderbook_margin_bridge_required"], "stage4b_evidence_fields": ["pf_stress_price_premium_or_relief_rally", "asset_sale_support_or_workout_speculation", "post_peak_drawdown"], "stage4c_evidence_fields": ["workout_liquidity_bridge_failure", "refinancing_or_maturity_wall_failure", "balance_sheet_break_and_trading_halt_caveat"], "symbol": "009410", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv", "trigger_date": "2023-12-28", "trigger_type": "4C-structural-break", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -21.82, "MAE_30D_pct": -2.62, "MAE_90D_pct": -11.05, "MFE_180D_pct": 3.0, "MFE_30D_pct": 3.0, "MFE_90D_pct": 3.0, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_005960_DONGBU_20240117_PF_SYMPATHY_FALSE_GREEN_YELLOW", "case_role": "pf_sympathy_false_green_counterexample", "company_name": "동부건설", "corporate_action_window_status": "clean_2024_forward_window; profile corporate-action candidates are historical and latest 2016-11-04, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Medium/small construction PF sympathy should stay Yellow or 4B watch unless refinancing, PF guarantee exposure, cash flow, orderbook margin and debt maturity evidence improve. Price stabilization alone was not a Green bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -24.09, "entry_date": "2024-01-17", "entry_price": 5340, "evidence_family": "construction_pf_sympathy_liquidity_risk_without_refinancing_margin_orderbook_recovery", "evidence_url_pending": false, "fine_archetype_id": "PF_WORKOUT_LARGE_BUILDER_CONTRAST_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "low_date_180d": "2024-09-09", "low_price_180d": 4175, "peak_date": "2024-02-19", "peak_price": 5500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005960.json", "raw_component_score_breakdown": {"asset_sale_support_quality": 3, "balance_sheet_stress": 9, "information_confidence": 3, "market_mispricing": 4, "pf_liquidity_bridge_break": 8, "refinancing_visibility": 4, "total": 32, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C30_005960_DONGBU_20240117_PF_SYMPATHY_FALSE_GREEN_YELLOW", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R10", "source_proxy_only": false, "stage2_evidence_fields": ["construction_pf_balance_sheet_stress_attention", "refinancing_or_liquidity_bridge_visibility", "orderbook_margin_cashflow_recovery_signal"], "stage3_evidence_fields": ["direct_pf_exposure_required", "debt_maturity_refinancing_bridge_required", "cashflow_orderbook_margin_bridge_required"], "stage4b_evidence_fields": ["pf_stress_price_premium_or_relief_rally", "asset_sale_support_or_workout_speculation", "post_peak_drawdown"], "stage4c_evidence_fields": ["workout_liquidity_bridge_failure", "refinancing_or_maturity_wall_failure", "balance_sheet_break_and_trading_halt_caveat"], "symbol": "005960", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv", "trigger_date": "2024-01-17", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -11.6, "MAE_30D_pct": -3.62, "MAE_90D_pct": -9.6, "MFE_180D_pct": 23.82, "MFE_30D_pct": 4.24, "MFE_90D_pct": 4.24, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_047040_DAEWOO_20240117_LARGE_BUILDER_PF_FALSE_BREAK_COUNTEREXAMPLE", "case_role": "large_builder_pf_false_break_counterexample", "company_name": "대우건설", "corporate_action_window_status": "clean_2024_forward_window; profile corporate-action candidates are 2001-07-13, 2003-11-18, 2011-01-18 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Large-builder PF industry stress should not auto-route to 4C when direct PF exposure, liquidity bridge, overseas/orderbook margin and refinancing evidence remain distinguishable from the distressed peer group.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -28.6, "entry_date": "2024-01-17", "entry_price": 4010, "evidence_family": "large_builder_pf_industry_stress_without_balance_sheet_break_orderbook_margin_failure", "evidence_url_pending": false, "fine_archetype_id": "PF_WORKOUT_LARGE_BUILDER_CONTRAST_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "low_date_180d": "2024-08-05", "low_price_180d": 3545, "peak_date": "2024-07-18", "peak_price": 4965, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/047/047040.json", "raw_component_score_breakdown": {"asset_sale_support_quality": 5, "balance_sheet_stress": 5, "information_confidence": 3, "market_mispricing": 7, "pf_liquidity_bridge_break": 4, "refinancing_visibility": 7, "total": 35, "valuation_rerating_runway": 4}, "reuse_reason": null, "same_entry_group_id": "C30_047040_DAEWOO_20240117_LARGE_BUILDER_PF_FALSE_BREAK_COUNTEREXAMPLE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R10", "source_proxy_only": false, "stage2_evidence_fields": ["construction_pf_balance_sheet_stress_attention", "refinancing_or_liquidity_bridge_visibility", "orderbook_margin_cashflow_recovery_signal"], "stage3_evidence_fields": ["direct_pf_exposure_required", "debt_maturity_refinancing_bridge_required", "cashflow_orderbook_margin_bridge_required"], "stage4b_evidence_fields": ["pf_stress_price_premium_or_relief_rally", "asset_sale_support_or_workout_speculation", "post_peak_drawdown"], "stage4c_evidence_fields": ["workout_liquidity_bridge_failure", "refinancing_or_maturity_wall_failure", "balance_sheet_break_and_trading_halt_caveat"], "symbol": "047040", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv", "trigger_date": "2024-01-17", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 2,
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "PF_WORKOUT_LARGE_BUILDER_CONTRAST_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "limited_event_window_case_count": 1,
  "loop_contribution_label": "construction_pf_balance_sheet_break_pf_workout_large_builder_contrast",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R10",
  "shadow_rule_candidate": "C30 construction PF rows should route actual workout/liquidity-bridge failure to 4C, but should not over-generalize industry PF stress to all builders; Green/Yellow distinction requires direct PF exposure, debt maturity, refinancing bridge, cash flow, orderbook margin and support-asset quality.",
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
3. Keep 009410 as a limited structural 4C event-window row because post-restructuring price comparability is blocked.
4. Add C30-specific construction PF / refinancing / direct exposure / false-break large-builder guard only as a shadow candidate until more rows exist.

Candidate rule:
- C30_ROUTE_WORKOUT_LIQUIDITY_BRIDGE_FAILURE_TO_4C
- C30_GREEN_REQUIRES_DIRECT_PF_EXPOSURE_REFINANCING_CASHFLOW_ORDERBOOK_MARGIN_BRIDGE
- C30_PF_SYMPATHY_WITHOUT_REFINANCING_BRIDGE_STAYS_YELLOW_4B
- C30_LARGE_BUILDER_DIRECT_EXPOSURE_CONTRAST_PREVENTS_AUTO_4C

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

