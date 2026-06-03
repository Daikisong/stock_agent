# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C15 — Material spread supercycle / steel late-cycle 4B refresh guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: STEEL_SPREAD_LATE_CYCLE_4B_REFRESH_GUARD
loop_objective: coverage_gap_fill|new_trigger_family|counterexample_mining|positive_counterexample_balance|4B_refresh_after_stage2_success|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_steel_spread_4b_refresh_2021_research.md
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

This run uses a new late-cycle 4B refresh trigger family for 004020, 005490 and 001230.  
The hard keys are new:
```text
C15 + 004020 + 4B-local-price-only + 2021-05-11
C15 + 005490 + 4B-local-price-only + 2021-05-11
C15 + 001230 + Stage3-Yellow + 2021-09-08
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
004020 현대제철: selected 2021 forward window clean; latest corporate-action candidate is 2014-01-24 and outside selected test window.
005490 POSCO홀딩스: corporate_action_candidate_count=0.
001230 동국제강/동국홀딩스: selected 2021 forward window clean; 2023-06-16 and 2023-11-13 corporate-action candidates are after selected 180D window.
```

## 3. Research thesis

C15 should split fresh spread-cycle entry from late-cycle spread premium:

```text
material spread supercycle attention
→ realized spread duration
→ shipment volume and utilization
→ raw-material/input-cost pass-through
→ downstream demand and working-capital quality
→ gross margin and revision bridge
→ rerating or local 4B cap
```

A spread is a tide. Stage2 can ride the incoming tide, but after the harbor is already full, Green needs a new tide table: fresh volume, input-cost proof, and revision evidence.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C15_004020_HYUNDAISTEEL_20210511_STEEL_SPREAD_PREMIUM_4B_REFRESH | 004020 | protective_steel_spread_price_premium_4b_success | 2021-05-11 | 61900 | 63000 on 2021-05-11 | 37100 on 2021-11-30 | 1.78% | 1.78% | 1.78% | -40.06% | -41.11% |
| C15_005490_POSCO_20210511_INTEGRATED_STEEL_SPREAD_PREMIUM_4B | 005490 | integrated_steel_spread_price_premium_counterexample | 2021-05-11 | 409500 | 412000 on 2021-05-11 | 260000 on 2021-11-30 | 0.61% | 0.61% | 0.61% | -36.51% | -36.89% |
| C15_001230_DONGKUKSTEEL_20210908_STEEL_SPREAD_FALSE_GREEN | 001230 | steel_spread_late_cycle_false_green_counterexample | 2021-09-08 | 22250 | 22550 on 2021-09-08 | 14050 on 2021-11-30 | 1.35% | 1.35% | 1.35% | -36.85% | -37.69% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as clean Stage2/Green positive.
- C15 Green should require realized spread duration, downstream demand, shipment volume, utilization, raw-material cost bridge and margin/revision confirmation.
- 001230 is the false-Green guard: late-cycle price confirmation did not supply fresh spread-duration, volume or margin revision evidence.

### 4B
- 004020 is the protective 4B anchor. The spread cycle was real, but the May 2021 premium had already paid for it and the later drawdown confirmed the need for fresh evidence.
- 005490 shows the same integrated-steel 4B pattern: peak proximity was tight and the later 180D drawdown was much larger than the residual upside.
- 001230 adds the late-cycle Stage3-Yellow version: price confirmation alone failed as evidence exhaustion turned into mean reversion.

### 4C
- No hard plant shutdown, covenant issue, or accounting break is asserted.
- The C15 break mode is spread mean-reversion/evidence exhaustion: spread strength may remain real, but incremental volume, input-cost and margin revision evidence no longer supports the price already paid.

## 6. Raw component score breakdown

```json
{
  "C15_001230_DONGKUKSTEEL_20210908_STEEL_SPREAD_FALSE_GREEN": {
    "downstream_demand_quality": 3,
    "information_confidence": 3,
    "input_cost_pass_through": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "spread_duration_quality": 4,
    "total": 24,
    "valuation_rerating_runway": 1,
    "volume_utilization": 4
  },
  "C15_004020_HYUNDAISTEEL_20210511_STEEL_SPREAD_PREMIUM_4B_REFRESH": {
    "downstream_demand_quality": 4,
    "information_confidence": 3,
    "input_cost_pass_through": 4,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "spread_duration_quality": 6,
    "total": 30,
    "valuation_rerating_runway": 1,
    "volume_utilization": 5
  },
  "C15_005490_POSCO_20210511_INTEGRATED_STEEL_SPREAD_PREMIUM_4B": {
    "downstream_demand_quality": 4,
    "information_confidence": 3,
    "input_cost_pass_through": 4,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "spread_duration_quality": 5,
    "total": 29,
    "valuation_rerating_runway": 1,
    "volume_utilization": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C15 guard:
```text
if material_spread_supercycle and realized_spread_volume_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if late_cycle_steel_spread_price_premium and no incremental_spread_duration_volume_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and spread_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 005490 / 2021-05-11: integrated steel spread premium can be over-promoted if the model treats peak-cycle price strength as fresh spread and revision proof.
- 001230 / 2021-09-08: late-cycle spread confirmation can look like Yellow-to-Green, but fails without renewed volume and margin bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -40.06, "MAE_30D_pct": -16.96, "MAE_90D_pct": -26.9, "MFE_180D_pct": 1.78, "MFE_30D_pct": 1.78, "MFE_90D_pct": 1.78, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_004020_HYUNDAISTEEL_20210511_STEEL_SPREAD_PREMIUM_4B_REFRESH", "case_role": "protective_steel_spread_price_premium_4b_success", "company_name": "현대제철", "corporate_action_window_status": "clean_2021_forward_window; corporate-action candidates are 1997-01-03, 1997-10-16, 1999-03-25, 1999-07-14, 2000-04-12, 2014-01-24, all outside selected test window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful after the steel spread rerating had already been paid. The spread cycle was real, but after the May 2021 high the model needed fresh shipment-volume, input-cost pass-through, downstream demand and margin/revision evidence before permitting Green.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.11, "entry_date": "2021-05-11", "entry_price": 61900, "evidence_family": "steel_plate_rebar_spread_price_premium_without_incremental_spread_volume_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "STEEL_SPREAD_LATE_CYCLE_4B_REFRESH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-11-30", "low_price_180d": 37100, "peak_date": "2021-05-11", "peak_price": 63000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/004/004020.json", "raw_component_score_breakdown": {"downstream_demand_quality": 4, "information_confidence": 3, "input_cost_pass_through": 4, "margin_revision_bridge": 3, "market_mispricing": 4, "spread_duration_quality": 6, "total": 30, "valuation_rerating_runway": 1, "volume_utilization": 5}, "reuse_reason": null, "same_entry_group_id": "C15_004020_HYUNDAISTEEL_20210511_STEEL_SPREAD_PREMIUM_4B_REFRESH", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["realized_material_spread_attention", "shipment_volume_and_utilization_visibility", "input_cost_pass_through_margin_revision_route"], "stage3_evidence_fields": ["spread_duration_and_downstream_demand_required", "shipment_volume_utilization_required", "raw_material_input_cost_and_margin_revision_bridge_required"], "stage4b_evidence_fields": ["steel_spread_price_premium", "late_cycle_spread_supercycle_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "shipment_volume_or_downstream_demand_disappointment", "margin_revision_bridge_failure"], "symbol": "004020", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004020/2021.csv", "trigger_date": "2021-05-11", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -36.51, "MAE_30D_pct": -18.68, "MAE_90D_pct": -25.27, "MFE_180D_pct": 0.61, "MFE_30D_pct": 0.61, "MFE_90D_pct": 0.61, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_005490_POSCO_20210511_INTEGRATED_STEEL_SPREAD_PREMIUM_4B", "case_role": "integrated_steel_spread_price_premium_counterexample", "company_name": "POSCO홀딩스", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2021_forward_window", "current_profile_error": true, "current_profile_verdict": "Integrated steel spread premium should route to local 4B or counterexample when the stock has already capitalized the supercycle and incremental spread duration, volume, input-cost bridge and margin revisions do not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -36.89, "entry_date": "2021-05-11", "entry_price": 409500, "evidence_family": "integrated_steel_spread_price_premium_without_incremental_spread_volume_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "STEEL_SPREAD_LATE_CYCLE_4B_REFRESH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-11-30", "low_price_180d": 260000, "peak_date": "2021-05-11", "peak_price": 412000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005490.json", "raw_component_score_breakdown": {"downstream_demand_quality": 4, "information_confidence": 3, "input_cost_pass_through": 4, "margin_revision_bridge": 3, "market_mispricing": 4, "spread_duration_quality": 5, "total": 29, "valuation_rerating_runway": 1, "volume_utilization": 5}, "reuse_reason": null, "same_entry_group_id": "C15_005490_POSCO_20210511_INTEGRATED_STEEL_SPREAD_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["realized_material_spread_attention", "shipment_volume_and_utilization_visibility", "input_cost_pass_through_margin_revision_route"], "stage3_evidence_fields": ["spread_duration_and_downstream_demand_required", "shipment_volume_utilization_required", "raw_material_input_cost_and_margin_revision_bridge_required"], "stage4b_evidence_fields": ["steel_spread_price_premium", "late_cycle_spread_supercycle_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "shipment_volume_or_downstream_demand_disappointment", "margin_revision_bridge_failure"], "symbol": "005490", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2021.csv", "trigger_date": "2021-05-11", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -36.85, "MAE_30D_pct": -24.27, "MAE_90D_pct": -36.85, "MFE_180D_pct": 1.35, "MFE_30D_pct": 1.35, "MFE_90D_pct": 1.35, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_001230_DONGKUKSTEEL_20210908_STEEL_SPREAD_FALSE_GREEN", "case_role": "steel_spread_late_cycle_false_green_counterexample", "company_name": "동국제강", "corporate_action_window_status": "clean_2021_forward_window; corporate-action candidates are 1999-01-27, 1999-07-13, 1999-09-21, 2014-07-15 and later 2023-06-16/2023-11-13, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Late-cycle steel spread confirmation should stay Yellow when price confirmation is not followed by fresh spread duration, shipment volume, input-cost pass-through and margin/revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -37.69, "entry_date": "2021-09-08", "entry_price": 22250, "evidence_family": "late_cycle_steel_spread_price_confirmation_without_incremental_volume_inputcost_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "STEEL_SPREAD_LATE_CYCLE_4B_REFRESH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-11-30", "low_price_180d": 14050, "peak_date": "2021-09-08", "peak_price": 22550, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/001/001230.json", "raw_component_score_breakdown": {"downstream_demand_quality": 3, "information_confidence": 3, "input_cost_pass_through": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "spread_duration_quality": 4, "total": 24, "valuation_rerating_runway": 1, "volume_utilization": 4}, "reuse_reason": null, "same_entry_group_id": "C15_001230_DONGKUKSTEEL_20210908_STEEL_SPREAD_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["realized_material_spread_attention", "shipment_volume_and_utilization_visibility", "input_cost_pass_through_margin_revision_route"], "stage3_evidence_fields": ["spread_duration_and_downstream_demand_required", "shipment_volume_utilization_required", "raw_material_input_cost_and_margin_revision_bridge_required"], "stage4b_evidence_fields": ["steel_spread_price_premium", "late_cycle_spread_supercycle_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "shipment_volume_or_downstream_demand_disappointment", "margin_revision_bridge_failure"], "symbol": "001230", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001230/2021.csv", "trigger_date": "2021-09-08", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "STEEL_SPREAD_LATE_CYCLE_4B_REFRESH_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "material_spread_supercycle_steel_late_cycle_4b_refresh_counterexamples",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C15 material-spread rows should allow Stage2 on realized spread duration plus shipment volume and margin revision evidence, but after the first rerating, steel spread price premium should route to local 4B unless incremental spread duration, volume, input-cost pass-through and revision evidence refresh.",
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
3. Add C15-specific material spread / steel late-cycle / volume / input-cost / margin-revision / local-4B refresh guard only as a shadow candidate until more rows exist.

Candidate rule:
- C15_STAGE2_ALLOWED_ON_REALIZED_SPREAD_VOLUME_MARGIN_REVISION_BRIDGE
- C15_GREEN_REQUIRES_SPREAD_DURATION_VOLUME_INPUT_COST_DEMAND_REVISION
- C15_LATE_CYCLE_STEEL_SPREAD_PRICE_PREMIUM_LOCAL_4B
- C15_SPREAD_PRICE_CONFIRMATION_WITHOUT_INCREMENTAL_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE.

