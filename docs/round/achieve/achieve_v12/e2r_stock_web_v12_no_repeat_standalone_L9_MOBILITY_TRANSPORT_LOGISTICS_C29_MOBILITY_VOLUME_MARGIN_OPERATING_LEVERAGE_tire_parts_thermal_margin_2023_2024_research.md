# E2R V12 No-Repeat Standalone Residual Research
## R9 / L9 / C29 — Mobility volume / margin operating-leverage guard

metadata:
```text
selected_round: R9
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L9_MOBILITY_TRANSPORT_LOGISTICS
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: TIRE_PARTS_THERMAL_VOLUME_MARGIN_REVISION_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L9_MOBILITY_TRANSPORT_LOGISTICS_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_tire_parts_thermal_margin_2023_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE current coverage:
rows=36, symbols=15, date range=2020-08-14~2024-09-09, good/bad S2=10/7, 4B/4C=4/2
top covered symbols: 000270(10), 204320(6), 011210(5), 005380(4), 003490(1)
```

This run avoids those top-covered C29 symbols and adds 161390, 012330, and 018880.  
Each row uses a new `C29 + symbol + trigger_type + entry_date` hard key.

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
161390 한국타이어앤테크놀로지: corporate_action_candidate_count=0.
012330 현대모비스: 2024 forward window clean; corporate-action candidates are old, outside the test window.
018880 한온시스템: 2023/2024 forward window clean; corporate-action candidates are old or in 2025/2026, outside the test window.
```

## 3. Research thesis

C29 should not be a generic "mobility up" bucket. It should test whether volume becomes operating leverage:

```text
mobility volume / replacement demand / parts mix attention
→ channel quality and customer mix
→ raw-material cost or cost-pass-through duration
→ margin bridge
→ revision confirmation
→ rerating
```

The guard is margin duration. A car can leave the factory and still not carry profit if mix, parts cost, labor, logistics or debt eat the spread. C29 should pay for the torque at the wheel, not just the engine rev.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C29_161390_HANKOOKTIRE_20230412_TIRE_VOLUME_MARGIN_STAGE2_SUCCESS | 161390 | positive_volume_margin_stage2_success | 2023-04-12 | 34700 | 48400 on 2023-12-05 | 33700 on 2023-04-12 | 7.78% | 21.76% | 39.48% | -2.88% | -11.26% |
| C29_012330_MOBIS_20240315_AUTO_PARTS_MARGIN_LATE_FALSE_GREEN | 012330 | parts_margin_late_false_green_counterexample | 2024-03-15 | 269000 | 270000 on 2024-03-18 | 200500 on 2024-08-05 | 0.37% | 0.37% | 0.37% | -25.46% | -25.74% |
| C29_018880_HANON_20230810_THERMAL_MGMT_VOLUME_MARGIN_FALSE_GREEN | 018880 | thermal_management_margin_counterexample | 2023-08-10 | 9690 | 10170 on 2023-08-11 | 5560 on 2024-03-20 | 4.95% | 4.95% | 4.95% | -42.62% | -45.33% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Mobility volume, tire replacement demand, and raw-material cost relief can be valid Stage2 routes.
- 161390 is the positive anchor: tire demand and cost relief translated into a low-MAE rerating path with margin/revision leverage.

### Stage3 / Green
- C29 Green should require volume quality, mix, cost-pass-through or raw-material-duration evidence, and margin/revision confirmation.
- 012330 and 018880 show why parts/thermal-management labels should not be promoted if the operating-leverage bridge is thin.

### 4B
- 012330 is the late price-confirmation guard. The March 2024 parts-margin rerating had already priced a large part of the story, and the following drawdown argues against fresh Green.
- 018880 also shows that one thermal-management rally can be a weak bridge if margin, debt and customer mix fail to confirm.

### 4C
- No hard accounting break is asserted.
- The C29 break mode is operating-leverage failure: the volume story exists, but mix, cost, debt or margin revision does not carry the valuation.

## 6. Raw component score breakdown

```json
{
  "C29_012330_MOBIS_20240315_AUTO_PARTS_MARGIN_LATE_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 3,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 33,
    "valuation_rerating_runway": 3,
    "visibility_quality": 7
  },
  "C29_018880_HANON_20230810_THERMAL_MGMT_VOLUME_MARGIN_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 25,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C29_161390_HANKOOKTIRE_20230412_TIRE_VOLUME_MARGIN_STAGE2_SUCCESS": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 3,
    "eps_fcf_explosion": 11,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 58,
    "valuation_rerating_runway": 9,
    "visibility_quality": 12
  }
}
```

## 7. Current calibrated profile stress test

Suggested C29 guard:
```text
if mobility_volume_margin_attention and no mix_cost_margin_revision_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if late_parts_or_thermal_price_confirmation and no incremental_margin_duration:
    route_to_local_4B_watch = true

if post_peak_drawdown and margin_or_debt_revision_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 012330 / 2024-03-15: auto-parts margin recovery can be over-promoted if the model does not require revision-duration and mix evidence after a price run.
- 018880 / 2023-08-10: thermal-management EV optionality can look like operating leverage, but the later path argues for Yellow/counterexample when margin and debt bridge fail.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -2.88, "MAE_30D_pct": -2.88, "MAE_90D_pct": -2.88, "MFE_180D_pct": 39.48, "MFE_30D_pct": 7.78, "MFE_90D_pct": 21.76, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_161390_HANKOOKTIRE_20230412_TIRE_VOLUME_MARGIN_STAGE2_SUCCESS", "case_role": "positive_volume_margin_stage2_success", "company_name": "한국타이어앤테크놀로지", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when tire volume/replacement demand and raw-material cost relief could translate into margin and revision leverage; Green still requires channel mix and margin-duration confirmation.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -11.26, "entry_date": "2023-04-12", "entry_price": 34700, "evidence_family": "tire_replacement_oem_volume_raw_material_cost_margin_operating_leverage", "evidence_url_pending": false, "fine_archetype_id": "TIRE_PARTS_THERMAL_VOLUME_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_MOBILITY_TRANSPORT_LOGISTICS", "low_date_180d": "2023-04-12", "low_price_180d": 33700, "peak_date": "2023-12-05", "peak_price": 48400, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/161/161390.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 3, "eps_fcf_explosion": 11, "information_confidence": 4, "market_mispricing": 10, "total": 58, "valuation_rerating_runway": 9, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C29_161390_HANKOOKTIRE_20230412_TIRE_VOLUME_MARGIN_STAGE2_SUCCESS", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["mobility_volume_or_replacement_demand_attention", "margin_or_raw_material_cost_relief_claim", "operating_leverage_or_mix_improvement_signal"], "stage3_evidence_fields": ["volume_quality_and_channel_mix_required", "cost_pass_through_or_raw_material_duration_required", "margin_and_revision_bridge_required"], "stage4b_evidence_fields": ["mobility_margin_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["volume_or_mix_fade", "cost_pass_through_failure", "debt_margin_or_revision_break"], "symbol": "161390", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/161/161390/2023.csv", "trigger_date": "2023-04-12", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -25.46, "MAE_30D_pct": -11.34, "MAE_90D_pct": -18.4, "MFE_180D_pct": 0.37, "MFE_30D_pct": 0.37, "MFE_90D_pct": 0.37, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_012330_MOBIS_20240315_AUTO_PARTS_MARGIN_LATE_FALSE_GREEN", "case_role": "parts_margin_late_false_green_counterexample", "company_name": "현대모비스", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Auto-parts margin recovery should not become fresh Green after the price run unless module/AS mix, cost pass-through, inventory quality and revision duration remain visible.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -25.74, "entry_date": "2024-03-15", "entry_price": 269000, "evidence_family": "auto_parts_margin_recovery_price_confirmation_without_revision_duration", "evidence_url_pending": false, "fine_archetype_id": "TIRE_PARTS_THERMAL_VOLUME_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_MOBILITY_TRANSPORT_LOGISTICS", "low_date_180d": "2024-08-05", "low_price_180d": 200500, "peak_date": "2024-03-18", "peak_price": 270000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/012/012330.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 3, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 5, "total": 33, "valuation_rerating_runway": 3, "visibility_quality": 7}, "reuse_reason": null, "same_entry_group_id": "C29_012330_MOBIS_20240315_AUTO_PARTS_MARGIN_LATE_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["mobility_volume_or_replacement_demand_attention", "margin_or_raw_material_cost_relief_claim", "operating_leverage_or_mix_improvement_signal"], "stage3_evidence_fields": ["volume_quality_and_channel_mix_required", "cost_pass_through_or_raw_material_duration_required", "margin_and_revision_bridge_required"], "stage4b_evidence_fields": ["mobility_margin_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["volume_or_mix_fade", "cost_pass_through_failure", "debt_margin_or_revision_break"], "symbol": "012330", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv", "trigger_date": "2024-03-15", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -42.62, "MAE_30D_pct": -8.05, "MAE_90D_pct": -30.34, "MFE_180D_pct": 4.95, "MFE_30D_pct": 4.95, "MFE_90D_pct": 4.95, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_018880_HANON_20230810_THERMAL_MGMT_VOLUME_MARGIN_FALSE_GREEN", "case_role": "thermal_management_margin_counterexample", "company_name": "한온시스템", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "EV thermal-management volume optionality should stay Yellow when margin, debt, capex, customer mix and revision bridge fail to close.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.33, "entry_date": "2023-08-10", "entry_price": 9690, "evidence_family": "ev_thermal_management_volume_story_without_margin_debt_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "TIRE_PARTS_THERMAL_VOLUME_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_MOBILITY_TRANSPORT_LOGISTICS", "low_date_180d": "2024-03-20", "low_price_180d": 5560, "peak_date": "2023-08-11", "peak_price": 10170, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/018/018880.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 5, "total": 25, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C29_018880_HANON_20230810_THERMAL_MGMT_VOLUME_MARGIN_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["mobility_volume_or_replacement_demand_attention", "margin_or_raw_material_cost_relief_claim", "operating_leverage_or_mix_improvement_signal"], "stage3_evidence_fields": ["volume_quality_and_channel_mix_required", "cost_pass_through_or_raw_material_duration_required", "margin_and_revision_bridge_required"], "stage4b_evidence_fields": ["mobility_margin_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["volume_or_mix_fade", "cost_pass_through_failure", "debt_margin_or_revision_break"], "symbol": "018880", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018880/2023.csv", "trigger_date": "2023-08-10", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "TIRE_PARTS_THERMAL_VOLUME_MARGIN_REVISION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L9_MOBILITY_TRANSPORT_LOGISTICS",
  "loop_contribution_label": "mobility_volume_margin_tire_parts_thermal_counterexamples_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R9",
  "shadow_rule_candidate": "C29 mobility rows should allow Stage2 on early volume/margin operating-leverage evidence, but Stage3 Green requires volume quality, mix, cost-pass-through duration, raw-material relief, margin and revision bridge; late parts or thermal-management price confirmation without margin duration should route to Yellow/local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C29 + symbol + trigger_type + entry_date.
3. Add C29-specific mobility volume/mix/cost-pass-through/margin-duration guard only as a shadow candidate until more rows exist.

Candidate rule:
- C29_GREEN_REQUIRES_VOLUME_MIX_COST_MARGIN_REVISION
- C29_TIRE_RAW_MATERIAL_COST_RELIEF_STAGE2_ALLOWED
- C29_LATE_PARTS_MARGIN_PRICE_CONFIRMATION_LOCAL_4B
- C29_THERMAL_MANAGEMENT_WITHOUT_MARGIN_DEBT_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R9/L9_MOBILITY_TRANSPORT_LOGISTICS/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

