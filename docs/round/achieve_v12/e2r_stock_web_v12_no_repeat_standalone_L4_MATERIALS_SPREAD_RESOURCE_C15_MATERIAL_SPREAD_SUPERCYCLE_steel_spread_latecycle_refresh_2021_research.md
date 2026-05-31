# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C15 — Material spread supercycle / steel late-cycle refresh 4B guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: STEEL_SPREAD_LATECYCLE_REFRESH_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_date_trigger_family|counterexample_mining|positive_counterexample_balance|4B_gap_fill|latecycle_steel_spread_to_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_steel_spread_latecycle_refresh_2021_research.md
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

This run avoids those top-covered C15 symbols and uses new symbol/date/trigger-family combinations:
```text
C15 + 001430 + Stage2-Actionable + 2021-04-16
C15 + 005490 + 4B-local-price-only + 2021-05-10
C15 + 004020 + Stage3-Yellow + 2021-06-24
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
001430 세아베스틸/세아베스틸지주: selected 2021 forward window clean; later 2022 name change does not affect selected trigger window.
005490 POSCO/POSCO홀딩스: selected post-2008 forward window clean; historical corporate-action candidates outside selected trigger window.
004020 현대제철: selected 2021 forward window clean; historical corporate-action candidates outside selected trigger window.
```

## 3. Research thesis

C15 should split real material-spread supercycle discovery from late-cycle steel spread optionality already paid in price:

```text
steel / special-steel material spread and reopening restocking
→ realized spread duration
→ shipment volume and export/reopening demand
→ ASP/input-cost pass-through
→ inventory and working-capital quality
→ gross margin and revision bridge
→ Stage2/Green or local 4B cap
```

A steel spread is a furnace draft. Stage2 can buy the first heat when ASP and margin revisions are still rising. Green should not keep feeding the furnace after the market has already priced the heat and the next spread-to-margin proof has stopped arriving.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C15_001430_SEAHBESTEEL_20210416_SPECIAL_STEEL_SPREAD_STAGE2 | 001430 | positive_special_steel_spread_stage2_success_with_later_4b_refresh | 2021-04-16 | 20650 | 36450 on 2021-05-11 | 21050 on 2021-11-01 | 76.51% | 76.51% | 76.51% | 1.94% | -42.25% |
| C15_005490_POSCO_20210510_STEEL_SPREAD_PREMIUM_4B | 005490 | steel_spread_price_premium_counterexample | 2021-05-10 | 407000 | 413500 on 2021-05-10 | 282500 on 2021-11-05 | 1.6% | 1.6% | 1.6% | -30.59% | -31.68% |
| C15_004020_HYUNDAISTEEL_20210624_STEEL_SPREAD_FALSE_GREEN | 004020 | late_steel_spread_confirmation_false_green_counterexample | 2021-06-24 | 55100 | 56100 on 2021-06-25 | 43250 on 2021-10-06 | 1.81% | 1.81% | 1.81% | -21.51% | -22.91% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 001430 is the positive anchor. The April 2021 special-steel spread/reopening route produced strong MFE before the May 2021 premium required 4B refresh discipline.
- Stage2 is allowed only when material-spread salience maps to realized spread duration, shipment/reopening volume, ASP/input-cost pass-through, inventory quality and margin/revision visibility.

### Stage3 / Green
- C15 Green should require realized spread duration, volume shipment or restocking persistence, feedstock/input-cost pass-through, inventory quality and margin/revision confirmation.
- 004020 is the false-Green/Yellow guard: late steel spread confirmation was visible, but the June 2021 price had almost no residual upside and much larger forward MAE when new spread-to-margin evidence did not refresh.

### 4B
- 005490 fills the steel spread supercycle price-premium 4B pocket. The May 2021 trigger had tiny residual upside and a large drawdown.
- 004020 shows the same failure in steel-sector beta form: spread optionality can remain directionally real while the listed-company earnings bridge is too stale for Green.
- 001430 also demonstrates that valid Stage2 evidence can become local 4B after the rerating capitalizes the spread pipeline.

### 4C
- No hard plant disruption, customer loss, inventory write-down or accounting break is asserted.
- The C15 break mode is spread-to-margin exhaustion: the steel spread story may remain directionally real, but incremental spread duration, volume, cost bridge and revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C15_001430_SEAHBESTEEL_20210416_SPECIAL_STEEL_SPREAD_STAGE2": {
    "ASP_input_cost_bridge": 8,
    "information_confidence": 4,
    "inventory_working_capital_quality": 6,
    "margin_revision_bridge": 7,
    "market_mispricing": 9,
    "material_spread_visibility": 9,
    "realized_spread_duration": 8,
    "total": 67,
    "valuation_rerating_runway": 8,
    "volume_restocking_export_bridge": 8
  },
  "C15_004020_HYUNDAISTEEL_20210624_STEEL_SPREAD_FALSE_GREEN": {
    "ASP_input_cost_bridge": 3,
    "information_confidence": 3,
    "inventory_working_capital_quality": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "material_spread_visibility": 7,
    "realized_spread_duration": 4,
    "total": 30,
    "valuation_rerating_runway": 1,
    "volume_restocking_export_bridge": 3
  },
  "C15_005490_POSCO_20210510_STEEL_SPREAD_PREMIUM_4B": {
    "ASP_input_cost_bridge": 4,
    "information_confidence": 3,
    "inventory_working_capital_quality": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "material_spread_visibility": 8,
    "realized_spread_duration": 4,
    "total": 34,
    "valuation_rerating_runway": 1,
    "volume_restocking_export_bridge": 4
  }
}
```

## 7. Current calibrated profile stress test

Suggested C15 guard:
```text
if material_spread_supercycle and realized_spread_volume_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if latecycle_steel_spread_price_premium and no incremental_spread_duration_volume_inputcost_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and spread_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 005490 / 2021-05-10: steel spread premium can be over-promoted if price strength substitutes for renewed volume/spread duration and margin proof.
- 004020 / 2021-06-24: late steel spread confirmation can look like Yellow-to-Green, but fails without refreshed shipment, input-cost and revision evidence.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": 1.94, "MAE_30D_pct": -4.12, "MAE_90D_pct": -4.12, "MFE_180D_pct": 76.51, "MFE_30D_pct": 76.51, "MFE_90D_pct": 76.51, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_001430_SEAHBESTEEL_20210416_SPECIAL_STEEL_SPREAD_STAGE2", "case_role": "positive_special_steel_spread_stage2_success_with_later_4b_refresh", "company_name": "세아베스틸지주", "corporate_action_window_status": "selected 2021 forward window clean; later 2022 name change does not affect selected trigger window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when special-steel spread/reopening evidence, restocking demand, ASP hikes and margin-revision optionality were visible before the rerating was fully capitalized. Green still requires realized spread duration, shipment volume, inventory discipline, ASP/input-cost bridge, margin revisions and valuation runway; after the May 2021 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -42.25, "entry_date": "2021-04-16", "entry_price": 20650, "evidence_family": "special_steel_spread_reopening_restocking_ASP_inputcost_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "STEEL_SPREAD_LATECYCLE_REFRESH_4B_GUARD", "forward_window_trading_days": 180, "historical_name": "세아베스틸", "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-11-01", "low_price_180d": 21050, "peak_date": "2021-05-11", "peak_price": 36450, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/001/001430.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 8, "information_confidence": 4, "inventory_working_capital_quality": 6, "margin_revision_bridge": 7, "market_mispricing": 9, "material_spread_visibility": 9, "realized_spread_duration": 8, "total": 67, "valuation_rerating_runway": 8, "volume_restocking_export_bridge": 8}, "reuse_reason": null, "same_entry_group_id": "C15_001430_SEAHBESTEEL_20210416_SPECIAL_STEEL_SPREAD_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["material_spread_supercycle_visibility", "realized_spread_duration_and_volume_bridge", "ASP_input_cost_inventory_margin_revision_route"], "stage3_evidence_fields": ["spread_duration_required", "shipment_volume_and_restocking_persistence_required", "input_cost_inventory_margin_revision_bridge_required"], "stage4b_evidence_fields": ["steel_spread_latecycle_price_premium", "spread_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion_or_restocking_gap", "input_cost_inventory_quality_break", "margin_revision_bridge_failure"], "symbol": "001430", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001430/2021.csv", "trigger_date": "2021-04-16", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -30.59, "MAE_30D_pct": -17.94, "MAE_90D_pct": -24.82, "MFE_180D_pct": 1.6, "MFE_30D_pct": 1.6, "MFE_90D_pct": 1.6, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_005490_POSCO_20210510_STEEL_SPREAD_PREMIUM_4B", "case_role": "steel_spread_price_premium_counterexample", "company_name": "POSCO홀딩스", "corporate_action_window_status": "selected post-2008 forward window clean; historical corporate-action candidates outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Steel spread supercycle premium should route to local 4B/counterexample when the market has already capitalized reopening restocking, ASP hikes and margin recovery while incremental spread duration, shipment volume, input-cost pass-through and margin/revision evidence do not keep expanding. The May 2021 trigger had tiny residual upside and a large forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -31.68, "entry_date": "2021-05-10", "entry_price": 407000, "evidence_family": "steel_spread_supercycle_price_premium_without_incremental_spread_duration_volume_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "STEEL_SPREAD_LATECYCLE_REFRESH_4B_GUARD", "forward_window_trading_days": 180, "historical_name": "POSCO", "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-11-05", "low_price_180d": 282500, "peak_date": "2021-05-10", "peak_price": 413500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005490.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 4, "information_confidence": 3, "inventory_working_capital_quality": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "material_spread_visibility": 8, "realized_spread_duration": 4, "total": 34, "valuation_rerating_runway": 1, "volume_restocking_export_bridge": 4}, "reuse_reason": null, "same_entry_group_id": "C15_005490_POSCO_20210510_STEEL_SPREAD_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["material_spread_supercycle_visibility", "realized_spread_duration_and_volume_bridge", "ASP_input_cost_inventory_margin_revision_route"], "stage3_evidence_fields": ["spread_duration_required", "shipment_volume_and_restocking_persistence_required", "input_cost_inventory_margin_revision_bridge_required"], "stage4b_evidence_fields": ["steel_spread_latecycle_price_premium", "spread_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion_or_restocking_gap", "input_cost_inventory_quality_break", "margin_revision_bridge_failure"], "symbol": "005490", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2021.csv", "trigger_date": "2021-05-10", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -21.51, "MAE_30D_pct": -8.17, "MAE_90D_pct": -21.51, "MFE_180D_pct": 1.81, "MFE_30D_pct": 1.81, "MFE_90D_pct": 1.81, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_004020_HYUNDAISTEEL_20210624_STEEL_SPREAD_FALSE_GREEN", "case_role": "late_steel_spread_confirmation_false_green_counterexample", "company_name": "현대제철", "corporate_action_window_status": "selected 2021 forward window clean; historical corporate-action candidates outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Late steel spread/reopening confirmation should stay Yellow or local 4B when the price has already paid for the cycle and fresh shipment volume, ASP/input-cost, inventory quality and margin-revision evidence do not refresh. The June 2021 trigger had almost no residual upside and much larger forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -22.91, "entry_date": "2021-06-24", "entry_price": 55100, "evidence_family": "steel_spread_reopening_price_confirmation_without_incremental_volume_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "STEEL_SPREAD_LATECYCLE_REFRESH_4B_GUARD", "forward_window_trading_days": 180, "historical_name": "현대제철", "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-10-06", "low_price_180d": 43250, "peak_date": "2021-06-25", "peak_price": 56100, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/004/004020.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 3, "information_confidence": 3, "inventory_working_capital_quality": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "material_spread_visibility": 7, "realized_spread_duration": 4, "total": 30, "valuation_rerating_runway": 1, "volume_restocking_export_bridge": 3}, "reuse_reason": null, "same_entry_group_id": "C15_004020_HYUNDAISTEEL_20210624_STEEL_SPREAD_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["material_spread_supercycle_visibility", "realized_spread_duration_and_volume_bridge", "ASP_input_cost_inventory_margin_revision_route"], "stage3_evidence_fields": ["spread_duration_required", "shipment_volume_and_restocking_persistence_required", "input_cost_inventory_margin_revision_bridge_required"], "stage4b_evidence_fields": ["steel_spread_latecycle_price_premium", "spread_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion_or_restocking_gap", "input_cost_inventory_quality_break", "margin_revision_bridge_failure"], "symbol": "004020", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004020/2021.csv", "trigger_date": "2021-06-24", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "STEEL_SPREAD_LATECYCLE_REFRESH_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "material_spread_supercycle_steel_latecycle_new_dates_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C15 steel/material-spread rows should allow Stage2 when realized spread duration is backed by shipment/reopening volume, ASP-input-cost pass-through, inventory quality and margin-revision bridge, but route late-cycle steel spread premiums to Yellow/local 4B when incremental spread-to-margin evidence has not refreshed.",
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
3. Add C15-specific material spread / realized spread duration / volume-shipment / ASP-input-cost / inventory / margin-revision / late-cycle local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C15_STAGE2_ALLOWED_ON_REALIZED_SPREAD_VOLUME_MARGIN_REVISION_BRIDGE
- C15_GREEN_REQUIRES_SPREAD_DURATION_VOLUME_INPUT_COST_INVENTORY_REVISION
- C15_LATECYCLE_STEEL_SPREAD_PRICE_PREMIUM_LOCAL_4B
- C15_SPREAD_OPTIONALITY_WITHOUT_VOLUME_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE.

