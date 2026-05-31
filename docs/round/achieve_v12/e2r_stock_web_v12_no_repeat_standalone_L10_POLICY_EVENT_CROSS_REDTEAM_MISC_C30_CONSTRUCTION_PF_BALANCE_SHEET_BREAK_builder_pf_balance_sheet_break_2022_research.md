# E2R V12 No-Repeat Standalone Residual Research
## R13 / L10 / C30 — Construction PF / balance-sheet break guard

metadata:
```text
selected_round: R13
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: BUILDER_PF_REFINANCING_HOUSING_BALANCE_SHEET_4C_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|4B_4C_guard_validation|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_builder_pf_balance_sheet_break_2022_research.md
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

This run avoids those top-covered C30 symbols and adds 047040, 005960, and 013360.  
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
047040 대우건설: 2022 forward window clean; corporate-action candidates are 2001/2003/2011 and outside the selected test window.
005960 동부건설: 2022 forward window clean; corporate-action candidates are historical and outside the selected test window.
013360 일성건설: 2022 forward window clean; latest corporate-action candidate is 2017-05-18, outside the selected test window.
```

## 3. Research thesis

C30 should not be treated as a normal cyclical value bucket. It is a balance-sheet break detector:

```text
housing-cycle slowdown / PF spread pressure
→ refinancing access weakens
→ unsold inventory and collection quality worsen
→ margin and working-capital bridge breaks
→ revisions fail
→ 4C
```

A builder can look cheap the same way a bridge looks short from far away. The danger is not the distance; it is the load-bearing structure underneath. C30 should ask whether the PF bridge can carry the balance sheet before allowing any Stage2/Green rerating.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C30_047040_DAEWOO_20220112_HOUSING_PF_BALANCE_SHEET_4C | 047040 | protective_4c_success_large_builder_balance_sheet_break | 2022-01-12 | 6100 | 7510 on 2022-03-14 | 4000 on 2022-10-13 | 4.92% | 23.11% | 23.11% | -34.43% | -46.74% |
| C30_005960_DONGBU_20220112_MIDSIZE_BUILDER_PF_LIQUIDITY_4C | 005960 | midsize_builder_pfrisk_false_stage2_counterexample | 2022-01-12 | 14600 | 15150 on 2022-03-16 | 6740 on 2022-10-26 | 1.37% | 3.77% | 3.77% | -53.84% | -55.51% |
| C30_013360_ILSUNG_20220112_SMALL_BUILDER_PF_BALANCE_SHEET_4C | 013360 | small_builder_pf_liquidity_counterexample | 2022-01-12 | 5370 | 6360 on 2022-03-25 | 2065 on 2022-10-13 | 4.84% | 18.44% | 18.44% | -61.55% | -67.53% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD should be counted as Stage2/Green positive research.
- Builder backlog, low PBR, or short price rebounds are insufficient when PF refinancing, housing demand, inventory, collection quality and margin evidence are deteriorating.
- Stage2 should reopen only after refinancing access, working-capital pressure, and gross-margin revision bridge improve together.

### 4B
- Temporary price bounces inside 2022 should be treated as local 4B-style relief unless non-price balance-sheet evidence improves.
- For C30, a bounce is often a solvent-looking shadow. It can move the tape, but it does not repair refinancing access or inventory absorption.

### 4C
- 047040 is the protective 4C anchor: the large-builder path still produced a deep post-peak drawdown once the housing/PF balance-sheet bridge deteriorated.
- 005960 and 013360 are current-profile residual errors. They show why mid/small builders need a harsher PF/liquidity cap: the fall was not just sector beta, but balance-sheet duration meeting a tightening funding market.

## 6. Raw component score breakdown

```json
{
  "C30_005960_DONGBU_20220112_MIDSIZE_BUILDER_PF_LIQUIDITY_4C": {
    "bottleneck_pricing_power": 3,
    "capital_allocation": 1,
    "eps_fcf_explosion": 2,
    "information_confidence": 4,
    "market_mispricing": 4,
    "total": 19,
    "valuation_rerating_runway": 1,
    "visibility_quality": 4
  },
  "C30_013360_ILSUNG_20220112_SMALL_BUILDER_PF_BALANCE_SHEET_4C": {
    "bottleneck_pricing_power": 3,
    "capital_allocation": 1,
    "eps_fcf_explosion": 2,
    "information_confidence": 4,
    "market_mispricing": 4,
    "total": 18,
    "valuation_rerating_runway": 1,
    "visibility_quality": 3
  },
  "C30_047040_DAEWOO_20220112_HOUSING_PF_BALANCE_SHEET_4C": {
    "bottleneck_pricing_power": 3,
    "capital_allocation": 1,
    "eps_fcf_explosion": 3,
    "information_confidence": 4,
    "market_mispricing": 4,
    "total": 21,
    "valuation_rerating_runway": 1,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C30 guard:
```text
if builder_low_pbr_or_backlog_attention and PF_refinancing_spread_housing_inventory_bridge_fails:
    block_stage2_green = true
    route_to_4C_hard = true

if construction_price_bounce and no refinancing_access_margin_revision_recovery:
    route_to_local_4B_watch = true
    require_non_price_recovery_evidence = true

if mid_small_builder and liquidity_or_collection_quality_deteriorates:
    apply_harsher_balance_sheet_cap = true
```

Residual errors:
```text
current_profile_error_count = 2
- 005960 / 2022-01-12: mid-size builder valuation/backlog can be over-promoted if PF refinancing and liquidity bridge are not explicitly weighted.
- 013360 / 2022-01-12: small builder price bounces can look like recovery, but the forward path argues for hard 4C unless balance-sheet and margin evidence repair.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -34.43, "MAE_30D_pct": -12.95, "MAE_90D_pct": -12.95, "MFE_180D_pct": 23.11, "MFE_30D_pct": 4.92, "MFE_90D_pct": 23.11, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_047040_DAEWOO_20220112_HOUSING_PF_BALANCE_SHEET_4C", "case_role": "protective_4c_success_large_builder_balance_sheet_break", "company_name": "대우건설", "corporate_action_window_status": "clean_2022_forward_window; corporate-action candidates are old and outside selected test window", "current_profile_error": false, "current_profile_verdict": "The protective C30 route was useful when housing-cycle slowdown, PF refinancing cost, unsold inventory and balance-sheet duration risk began to dominate. This should block fresh Stage2/Green even if headline order backlog or low PBR looks attractive.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.74, "entry_date": "2022-01-12", "entry_price": 6100, "evidence_family": "housing_cycle_slowdown_pf_refinancing_cost_unsold_inventory_balance_sheet_break", "evidence_url_pending": false, "fine_archetype_id": "BUILDER_PF_REFINANCING_HOUSING_BALANCE_SHEET_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2022-10-13", "low_price_180d": 4000, "peak_date": "2022-03-14", "peak_price": 7510, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/047/047040.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 3, "capital_allocation": 1, "eps_fcf_explosion": 3, "information_confidence": 4, "market_mispricing": 4, "total": 21, "valuation_rerating_runway": 1, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C30_047040_DAEWOO_20220112_HOUSING_PF_BALANCE_SHEET_4C", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R13", "source_proxy_only": false, "stage2_evidence_fields": ["only_allowed_after_balance_sheet_risk_clears", "fresh_refinancing_access_required", "housing_demand_and_margin_recovery_required"], "stage3_evidence_fields": ["PF_refinancing_spread_stabilization_required", "unsold_inventory_and_collection_quality_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["cheap_builder_or_order_backlog_price_bounce", "valuation_trap_or_positioning_bounce", "post_peak_drawdown"], "stage4c_evidence_fields": ["PF_refinancing_or_liquidity_break", "housing_demand_and_unsold_inventory_pressure", "balance_sheet_margin_revision_failure"], "symbol": "047040", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2022.csv", "trigger_date": "2022-01-12", "trigger_type": "Stage4C-Hard", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -53.84, "MAE_30D_pct": -15.07, "MAE_90D_pct": -16.44, "MFE_180D_pct": 3.77, "MFE_30D_pct": 1.37, "MFE_90D_pct": 3.77, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_005960_DONGBU_20220112_MIDSIZE_BUILDER_PF_LIQUIDITY_4C", "case_role": "midsize_builder_pfrisk_false_stage2_counterexample", "company_name": "동부건설", "corporate_action_window_status": "clean_2022_forward_window; corporate-action candidates are old and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Mid-size builder backlog or cheap valuation should not become Stage2/Green when PF refinancing, funding spread, housing demand and margin revision evidence are deteriorating. The row argues for hard C30 4C routing.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -55.51, "entry_date": "2022-01-12", "entry_price": 14600, "evidence_family": "midsize_builder_pf_refinancing_liquidity_and_margin_break", "evidence_url_pending": false, "fine_archetype_id": "BUILDER_PF_REFINANCING_HOUSING_BALANCE_SHEET_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2022-10-26", "low_price_180d": 6740, "peak_date": "2022-03-16", "peak_price": 15150, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005960.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 3, "capital_allocation": 1, "eps_fcf_explosion": 2, "information_confidence": 4, "market_mispricing": 4, "total": 19, "valuation_rerating_runway": 1, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C30_005960_DONGBU_20220112_MIDSIZE_BUILDER_PF_LIQUIDITY_4C", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R13", "source_proxy_only": false, "stage2_evidence_fields": ["only_allowed_after_balance_sheet_risk_clears", "fresh_refinancing_access_required", "housing_demand_and_margin_recovery_required"], "stage3_evidence_fields": ["PF_refinancing_spread_stabilization_required", "unsold_inventory_and_collection_quality_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["cheap_builder_or_order_backlog_price_bounce", "valuation_trap_or_positioning_bounce", "post_peak_drawdown"], "stage4c_evidence_fields": ["PF_refinancing_or_liquidity_break", "housing_demand_and_unsold_inventory_pressure", "balance_sheet_margin_revision_failure"], "symbol": "005960", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005960/2022.csv", "trigger_date": "2022-01-12", "trigger_type": "Stage4C-Hard", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -61.55, "MAE_30D_pct": -38.92, "MAE_90D_pct": -47.49, "MFE_180D_pct": 18.44, "MFE_30D_pct": 4.84, "MFE_90D_pct": 18.44, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_013360_ILSUNG_20220112_SMALL_BUILDER_PF_BALANCE_SHEET_4C", "case_role": "small_builder_pf_liquidity_counterexample", "company_name": "일성건설", "corporate_action_window_status": "clean_2022_forward_window; corporate-action candidates are old and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Small builder PF/liquidity exposure should be routed to 4C when housing demand, financing access, margin visibility and balance-sheet duration fail. Price bounces inside the drawdown should not be treated as evidence recovery.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.53, "entry_date": "2022-01-12", "entry_price": 5370, "evidence_family": "small_builder_pf_liquidity_housing_demand_balance_sheet_break", "evidence_url_pending": false, "fine_archetype_id": "BUILDER_PF_REFINANCING_HOUSING_BALANCE_SHEET_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2022-10-13", "low_price_180d": 2065, "peak_date": "2022-03-25", "peak_price": 6360, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/013/013360.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 3, "capital_allocation": 1, "eps_fcf_explosion": 2, "information_confidence": 4, "market_mispricing": 4, "total": 18, "valuation_rerating_runway": 1, "visibility_quality": 3}, "reuse_reason": null, "same_entry_group_id": "C30_013360_ILSUNG_20220112_SMALL_BUILDER_PF_BALANCE_SHEET_4C", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R13", "source_proxy_only": false, "stage2_evidence_fields": ["only_allowed_after_balance_sheet_risk_clears", "fresh_refinancing_access_required", "housing_demand_and_margin_recovery_required"], "stage3_evidence_fields": ["PF_refinancing_spread_stabilization_required", "unsold_inventory_and_collection_quality_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["cheap_builder_or_order_backlog_price_bounce", "valuation_trap_or_positioning_bounce", "post_peak_drawdown"], "stage4c_evidence_fields": ["PF_refinancing_or_liquidity_break", "housing_demand_and_unsold_inventory_pressure", "balance_sheet_margin_revision_failure"], "symbol": "013360", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/013/013360/2022.csv", "trigger_date": "2022-01-12", "trigger_type": "Stage4C-Hard", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "BUILDER_PF_REFINANCING_HOUSING_BALANCE_SHEET_4C_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "loop_contribution_label": "construction_pf_balance_sheet_new_symbols_4c_guard_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R13",
  "shadow_rule_candidate": "C30 construction/PF rows should hard-route to 4C when PF refinancing spread, housing demand, unsold inventory, collection quality, balance-sheet duration, margin and revision bridges deteriorate; builder order backlog, low PBR, or short price bounces should not become Stage2/Green unless refinancing access and margin recovery are visible.",
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
3. Add C30-specific construction PF / balance-sheet / refinancing / housing-inventory guard only as a shadow candidate until more rows exist.

Candidate rule:
- C30_BLOCK_STAGE2_GREEN_WHEN_PF_REFINANCING_AND_INVENTORY_BRIDGE_FAILS
- C30_BUILDER_BOUNCE_REQUIRES_NON_PRICE_BALANCE_SHEET_REPAIR
- C30_MID_SMALL_BUILDER_HARSHER_LIQUIDITY_CAP
- C30_HARD_4C_ON_REFINANCING_COLLECTION_MARGIN_REVISION_BREAK

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R13/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

