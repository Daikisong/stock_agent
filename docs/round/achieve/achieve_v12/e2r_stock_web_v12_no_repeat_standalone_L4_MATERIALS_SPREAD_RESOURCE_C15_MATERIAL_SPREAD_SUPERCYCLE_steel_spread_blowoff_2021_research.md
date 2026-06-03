# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C15 — Material spread supercycle duration / 4B guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: STEEL_SPREAD_SUPERCYCLE_DURATION_4B_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_steel_spread_blowoff_2021_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C15_MATERIAL_SPREAD_SUPERCYCLE current coverage:
rows=10, symbols=7, date range=2020-08-10~2024-05-21, good/bad S2=4/0, 4B/4C=0/0
top covered symbols: 006260(2), 011170(2), 103140(2), 006650(1), 011780(1)
```

This run avoids those top-covered C15 symbols and adds 005490, 004020, and 001230.  
Each row uses a new `C15 + symbol + trigger_type + entry_date` hard key.

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
005490 POSCO: corporate_action_candidate_count=0.
004020 현대제철: 2021 forward window clean; corporate-action candidates are old, outside the test window.
001230 동국제강: 2021 forward window clean; corporate-action candidates are old or 2023, outside the test window.
```

## 3. Research thesis

C15 is not a generic “materials up” bucket. It should test whether the spread cycle has enough duration to become EPS bodyweight:

```text
material / steel spread expansion
→ inventory and cost-lag operating leverage
→ pass-through or pricing power
→ margin and revision bridge
→ rerating
```

The core guard is timing. In the early part of a spread cycle, the furnace is being fed by cheap inventory and rising ASP. In the late part, the same furnace can become a mirror: it reflects the past spread, but no longer tells you whether the next quarter’s margin will survive.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C15_005490_POSCO_20210305_STEEL_SPREAD_SUPERCYCLE_STAGE2_SUCCESS | 005490 | positive_spread_supercycle_stage2_success | 2021-03-05 | 314500 | 413500 on 2021-05-10 | 276500 on 2021-11-08 | 11.13% | 31.48% | 31.48% | -12.08% | -33.13% |
| C15_004020_HYUNDAISTEEL_20210511_STEEL_SPREAD_LATE_FALSE_GREEN | 004020 | late_steel_spread_false_green_counterexample | 2021-05-11 | 61900 | 63000 on 2021-05-11 | 39550 on 2021-11-11 | 1.78% | 1.78% | 1.78% | -36.11% | -37.22% |
| C15_001230_DONGKUKSTEEL_20210427_REBAR_STEEL_SPREAD_BLOWOFF_4B | 001230 | steel_spread_blowoff_counterexample | 2021-04-27 | 25300 | 27850 on 2021-04-29 | 15550 on 2021-11-08 | 10.08% | 10.08% | 10.08% | -38.54% | -44.17% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Material spread expansion and integrated steel operating leverage are valid early routing signals.
- 005490 is the positive anchor: early 2021 spread strength produced a tradable Stage2 route before the later spread-cycle peak.

### Stage3 / Green
- C15 Green should require spread duration, margin/revision confirmation, pass-through ability, and inventory quality.
- The model should not treat the steel spread label as enough by itself. A spread is a moving gate, not a fixed asset.

### 4B
- 004020 and 001230 show why late-cycle price confirmation needs 4B discipline.
- 001230 is the sharper blowoff row: the price premium arrived quickly, but the later path shows that the spread story had already been over-capitalized.

### 4C
- No hard accounting break is asserted.
- The failure mode is spread mean reversion and margin-duration failure: the price had paid for a supercycle, but the non-price bridge did not keep expanding.

## 6. Raw component score breakdown

```json
{
  "C15_001230_DONGKUKSTEEL_20210427_REBAR_STEEL_SPREAD_BLOWOFF_4B": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 2,
    "eps_fcf_explosion": 7,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 32,
    "valuation_rerating_runway": 2,
    "visibility_quality": 6
  },
  "C15_004020_HYUNDAISTEEL_20210511_STEEL_SPREAD_LATE_FALSE_GREEN": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 2,
    "eps_fcf_explosion": 7,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 35,
    "valuation_rerating_runway": 3,
    "visibility_quality": 7
  },
  "C15_005490_POSCO_20210305_STEEL_SPREAD_SUPERCYCLE_STAGE2_SUCCESS": {
    "bottleneck_pricing_power": 10,
    "capital_allocation": 3,
    "eps_fcf_explosion": 11,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 59,
    "valuation_rerating_runway": 9,
    "visibility_quality": 11
  }
}
```

## 7. Current calibrated profile stress test

Suggested C15 guard:
```text
if material_spread_expansion and early_cycle_revision_bridge_visible:
    allow_stage2_actionable = true

if spread_cycle_price_run and no incremental_spread_duration_or_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and spread_or_inventory_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 004020 / 2021-05-11: late steel-spread price confirmation can be over-promoted if spread duration and revision evidence are not required.
- 001230 / 2021-04-27: rebar/plate steel premium can become a local blowoff if the model treats price strength as fresh spread evidence.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -12.08, "MAE_30D_pct": -9.06, "MAE_90D_pct": -9.06, "MFE_180D_pct": 31.48, "MFE_30D_pct": 11.13, "MFE_90D_pct": 31.48, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_005490_POSCO_20210305_STEEL_SPREAD_SUPERCYCLE_STAGE2_SUCCESS", "case_role": "positive_spread_supercycle_stage2_success", "company_name": "POSCO", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when steel spread expansion and integrated producer leverage were visible; Green still requires spread duration, margin/revision bridge and inventory/cost pass-through evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -33.13, "entry_date": "2021-03-05", "entry_price": 314500, "evidence_family": "integrated_steel_spread_supercycle_margin_revision_route", "evidence_url_pending": false, "fine_archetype_id": "STEEL_SPREAD_SUPERCYCLE_DURATION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-11-08", "low_price_180d": 276500, "peak_date": "2021-05-10", "peak_price": 413500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005490.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 10, "capital_allocation": 3, "eps_fcf_explosion": 11, "information_confidence": 4, "market_mispricing": 11, "total": 59, "valuation_rerating_runway": 9, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C15_005490_POSCO_20210305_STEEL_SPREAD_SUPERCYCLE_STAGE2_SUCCESS", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["steel_or_material_spread_expansion", "inventory_or_cost_lag_operating_leverage", "relative_strength_after_spread_inflection"], "stage3_evidence_fields": ["spread_duration_confirmation_required", "margin_or_revision_bridge_required", "cost_pass_through_and_inventory_quality_required"], "stage4b_evidence_fields": ["spread_supercycle_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "raw_material_cost_or_inventory_loss", "margin_or_revision_duration_failure"], "symbol": "005490", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2021.csv", "trigger_date": "2021-03-05", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -36.11, "MAE_30D_pct": -17.45, "MAE_90D_pct": -26.9, "MFE_180D_pct": 1.78, "MFE_30D_pct": 1.78, "MFE_90D_pct": 1.78, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_004020_HYUNDAISTEEL_20210511_STEEL_SPREAD_LATE_FALSE_GREEN", "case_role": "late_steel_spread_false_green_counterexample", "company_name": "현대제철", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Late steel spread strength should stay Yellow/local 4B unless spread duration and revision evidence remain fresh; price confirmation alone was a false-Green risk.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -37.22, "entry_date": "2021-05-11", "entry_price": 61900, "evidence_family": "late_steel_spread_price_confirmation_without_duration_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "STEEL_SPREAD_SUPERCYCLE_DURATION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-11-11", "low_price_180d": 39550, "peak_date": "2021-05-11", "peak_price": 63000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/004/004020.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 2, "eps_fcf_explosion": 7, "information_confidence": 3, "market_mispricing": 5, "total": 35, "valuation_rerating_runway": 3, "visibility_quality": 7}, "reuse_reason": null, "same_entry_group_id": "C15_004020_HYUNDAISTEEL_20210511_STEEL_SPREAD_LATE_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["steel_or_material_spread_expansion", "inventory_or_cost_lag_operating_leverage", "relative_strength_after_spread_inflection"], "stage3_evidence_fields": ["spread_duration_confirmation_required", "margin_or_revision_bridge_required", "cost_pass_through_and_inventory_quality_required"], "stage4b_evidence_fields": ["spread_supercycle_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "raw_material_cost_or_inventory_loss", "margin_or_revision_duration_failure"], "symbol": "004020", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004020/2021.csv", "trigger_date": "2021-05-11", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -38.54, "MAE_30D_pct": -17.59, "MAE_90D_pct": -30.83, "MFE_180D_pct": 10.08, "MFE_30D_pct": 10.08, "MFE_90D_pct": 10.08, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_001230_DONGKUKSTEEL_20210427_REBAR_STEEL_SPREAD_BLOWOFF_4B", "case_role": "steel_spread_blowoff_counterexample", "company_name": "동국제강", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Local 4B was the correct use after the mini steel-spread blowoff; without margin duration and revision bridge, the stock should not be promoted as fresh Green.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.17, "entry_date": "2021-04-27", "entry_price": 25300, "evidence_family": "rebar_plate_steel_spread_price_premium_without_sustainable_margin_duration", "evidence_url_pending": false, "fine_archetype_id": "STEEL_SPREAD_SUPERCYCLE_DURATION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-11-08", "low_price_180d": 15550, "peak_date": "2021-04-29", "peak_price": 27850, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/001/001230.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 2, "eps_fcf_explosion": 7, "information_confidence": 3, "market_mispricing": 4, "total": 32, "valuation_rerating_runway": 2, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C15_001230_DONGKUKSTEEL_20210427_REBAR_STEEL_SPREAD_BLOWOFF_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["steel_or_material_spread_expansion", "inventory_or_cost_lag_operating_leverage", "relative_strength_after_spread_inflection"], "stage3_evidence_fields": ["spread_duration_confirmation_required", "margin_or_revision_bridge_required", "cost_pass_through_and_inventory_quality_required"], "stage4b_evidence_fields": ["spread_supercycle_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "raw_material_cost_or_inventory_loss", "margin_or_revision_duration_failure"], "symbol": "001230", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001230/2021.csv", "trigger_date": "2021-04-27", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "STEEL_SPREAD_SUPERCYCLE_DURATION_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "steel_spread_supercycle_4b_counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C15 material/steel spread supercycle rows should allow Stage2 on early spread expansion, but Stage3 Green requires spread duration, margin/revision bridge, cost pass-through and inventory quality; late spread-cycle price premium should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C15 + symbol + trigger_type + entry_date.
3. Add C15-specific spread-duration / inventory-quality / revision-bridge guard only as a shadow candidate until more rows exist.

Candidate rule:
- C15_GREEN_REQUIRES_SPREAD_DURATION_MARGIN_REVISION
- C15_EARLY_SPREAD_EXPANSION_STAGE2_ALLOWED
- C15_LATE_STEEL_SPREAD_PRICE_PREMIUM_LOCAL_4B
- C15_SPREAD_MEAN_REVERSION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE.

