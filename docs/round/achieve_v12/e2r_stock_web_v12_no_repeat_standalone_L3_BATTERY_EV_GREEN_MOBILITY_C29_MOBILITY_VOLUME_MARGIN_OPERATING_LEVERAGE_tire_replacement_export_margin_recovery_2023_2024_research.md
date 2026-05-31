# E2R V12 No-Repeat Standalone Residual Research
## R9 / L3 / C29 — Mobility volume margin operating leverage / tire replacement-export margin recovery 4B guard

metadata:
```text
selected_round: R9
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: TIRE_REPLACEMENT_EXPORT_MARGIN_RECOVERY_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|tire_volume_mix_inputcost_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_tire_replacement_export_margin_recovery_2023_2024_research.md
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

This run avoids those top-covered C29 symbols and adds 161390, 073240, and 002350.  
Each row uses a new `C29 + symbol + trigger_type + entry_date` hard key:
```text
C29 + 161390 + Stage2-Actionable + 2023-10-27
C29 + 073240 + 4B-local-price-only + 2024-05-02
C29 + 002350 + Stage3-Yellow + 2024-04-11
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
161390 한국타이어앤테크놀로지: corporate_action_candidate_count=0; clean 2023/2024 forward window.
073240 금호타이어: selected post-2018 forward window clean; corporate-action candidates are historical/latest 2018-07-20, outside selected trigger window.
002350 넥센타이어: selected post-2008 forward window clean; corporate-action candidates are historical/latest 2008-03-21, outside selected trigger window.
```

## 3. Research thesis

C29 should distinguish tire/mobility margin operating leverage from late tire-margin beta already paid in price:

```text
mobility volume / tire replacement-export demand
→ shipment volume and premium mix
→ raw-material and freight pass-through
→ inventory and working-capital quality
→ operating leverage and margin revision
→ Stage2/Green or local 4B cap
```

A tire margin cycle is a wheel gaining traction. Stage2 can buy when the wheel starts gripping—volume, mix and cost bridge all turn together. Green should not keep pressing the accelerator after the market has already paid for the grip and the next margin revision has stopped arriving.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C29_161390_HANKOOKTIRE_20231027_TIRE_REPLACEMENT_EXPORT_MARGIN_STAGE2 | 161390 | positive_tire_replacement_export_margin_stage2_success_with_later_4b_refresh | 2023-10-27 | 37200 | 63300 on 2024-04-16 | 36650 on 2023-10-30 | 30.11% | 60.22% | 70.16% | -1.48% | -33.41% |
| C29_073240_KUMHOTIRE_20240502_TIRE_MARGIN_BETA_PRICE_PREMIUM_4B | 073240 | tire_margin_beta_price_premium_counterexample | 2024-05-02 | 7830 | 8360 on 2024-05-07 | 5410 on 2024-07-18 | 6.77% | 6.77% | 6.77% | -30.91% | -35.29% |
| C29_002350_NEXENTIRE_20240411_TIRE_REPLACEMENT_FALSE_GREEN | 002350 | tire_replacement_margin_false_green_counterexample | 2024-04-11 | 9500 | 9600 on 2024-05-02 | 6060 on 2024-07-09 | 1.05% | 1.05% | 1.05% | -36.21% | -36.88% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 161390 is the positive anchor. The October 2023 tire export/replacement margin route produced strong 30D/90D/180D MFE before the April 2024 premium required 4B refresh discipline.
- Stage2 is allowed only when tire volume/mix salience maps to shipment, export/replacement demand, input-cost/freight bridge and margin/revision visibility.

### Stage3 / Green
- C29 Green should require shipment volume and mix persistence, raw-material/freight pass-through, operating leverage, inventory quality and margin/revision confirmation.
- 002350 is the false-Green/Yellow guard: tire margin confirmation was visible, but the April 2024 price had almost no residual upside and much larger forward MAE when new volume-to-margin evidence did not refresh.

### 4B
- 073240 fills the tire margin beta price-premium 4B pocket. The May 2024 trigger had small residual upside and a much larger drawdown.
- 161390 also demonstrates that valid Stage2 can become local 4B after the rerating capitalizes the tire margin pipeline.
- The core 4B rule is that tire-sector beta and replacement/export narrative should not substitute for fresh shipment, mix, input-cost and margin revision evidence.

### 4C
- No hard customer loss, plant disruption, accounting break or structural demand collapse is asserted.
- The C29 break mode is volume-to-margin exhaustion: the tire margin story may remain directionally real, but incremental volume, mix, cost bridge and revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C29_002350_NEXENTIRE_20240411_TIRE_REPLACEMENT_FALSE_GREEN": {
    "export_mix_or_replacement_demand": 4,
    "information_confidence": 3,
    "input_cost_freight_bridge": 4,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "mobility_volume_visibility": 5,
    "operating_leverage_quality": 3,
    "total": 26,
    "valuation_rerating_runway": 1
  },
  "C29_073240_KUMHOTIRE_20240502_TIRE_MARGIN_BETA_PRICE_PREMIUM_4B": {
    "export_mix_or_replacement_demand": 5,
    "information_confidence": 3,
    "input_cost_freight_bridge": 4,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "mobility_volume_visibility": 6,
    "operating_leverage_quality": 4,
    "total": 30,
    "valuation_rerating_runway": 1
  },
  "C29_161390_HANKOOKTIRE_20231027_TIRE_REPLACEMENT_EXPORT_MARGIN_STAGE2": {
    "export_mix_or_replacement_demand": 9,
    "information_confidence": 4,
    "input_cost_freight_bridge": 8,
    "margin_revision_bridge": 8,
    "market_mispricing": 8,
    "mobility_volume_visibility": 8,
    "operating_leverage_quality": 8,
    "total": 60,
    "valuation_rerating_runway": 7
  }
}
```

## 7. Current calibrated profile stress test

Suggested C29 guard:
```text
if tire_volume_margin and shipment_mix_cost_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if tire_margin_price_premium and no incremental_volume_mix_inputcost_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and volume_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 073240 / 2024-05-02: tire margin beta can be over-promoted if price strength substitutes for fresh volume/mix and margin proof.
- 002350 / 2024-04-11: tire replacement/export confirmation can look like Yellow-to-Green, but fails without renewed shipment, cost bridge and revision evidence.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -1.48, "MAE_30D_pct": -1.48, "MAE_90D_pct": -1.48, "MFE_180D_pct": 70.16, "MFE_30D_pct": 30.11, "MFE_90D_pct": 60.22, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_161390_HANKOOKTIRE_20231027_TIRE_REPLACEMENT_EXPORT_MARGIN_STAGE2", "case_role": "positive_tire_replacement_export_margin_stage2_success_with_later_4b_refresh", "company_name": "한국타이어앤테크놀로지", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2023/2024 forward window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when tire replacement/export demand, premium mix, freight/input-cost normalization and operating-leverage evidence were visible before the rerating was fully capitalized. Green still requires volume shipment, ASP/mix persistence, raw-material/freight pass-through, inventory quality and margin/revision confirmation; after the April 2024 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -33.41, "entry_date": "2023-10-27", "entry_price": 37200, "evidence_family": "tire_replacement_export_mix_input_cost_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "TIRE_REPLACEMENT_EXPORT_MARGIN_RECOVERY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-30", "low_price_180d": 36650, "peak_date": "2024-04-16", "peak_price": 63300, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/161/161390.json", "raw_component_score_breakdown": {"export_mix_or_replacement_demand": 9, "information_confidence": 4, "input_cost_freight_bridge": 8, "margin_revision_bridge": 8, "market_mispricing": 8, "mobility_volume_visibility": 8, "operating_leverage_quality": 8, "total": 60, "valuation_rerating_runway": 7}, "reuse_reason": null, "same_entry_group_id": "C29_161390_HANKOOKTIRE_20231027_TIRE_REPLACEMENT_EXPORT_MARGIN_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["mobility_or_tire_volume_visibility", "export_replacement_mix_quality", "input_cost_freight_margin_revision_route"], "stage3_evidence_fields": ["shipment_volume_and_mix_persistence_required", "raw_material_freight_pass_through_required", "operating_leverage_margin_revision_bridge_required"], "stage4b_evidence_fields": ["tire_margin_recovery_price_premium", "volume_mix_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["volume_or_mix_disappointment", "input_cost_freight_margin_bridge_failure", "revision_momentum_break"], "symbol": "161390", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/161/161390/2023.csv", "trigger_date": "2023-10-27", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -30.91, "MAE_30D_pct": -12.64, "MAE_90D_pct": -30.91, "MFE_180D_pct": 6.77, "MFE_30D_pct": 6.77, "MFE_90D_pct": 6.77, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_073240_KUMHOTIRE_20240502_TIRE_MARGIN_BETA_PRICE_PREMIUM_4B", "case_role": "tire_margin_beta_price_premium_counterexample", "company_name": "금호타이어", "corporate_action_window_status": "clean post-2018 corporate-action forward window; corporate-action candidates are historical/latest 2018-07-20 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Tire margin beta price premium should route to local 4B/counterexample when the market has already capitalized export/replacement demand and incremental volume shipment, ASP/mix, raw-material/freight bridge and margin/revision evidence do not refresh. The May 2024 trigger had small residual upside and much larger local drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -35.29, "entry_date": "2024-05-02", "entry_price": 7830, "evidence_family": "tire_margin_export_beta_price_premium_without_incremental_volume_mix_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "TIRE_REPLACEMENT_EXPORT_MARGIN_RECOVERY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-07-18", "low_price_180d": 5410, "peak_date": "2024-05-07", "peak_price": 8360, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/073/073240.json", "raw_component_score_breakdown": {"export_mix_or_replacement_demand": 5, "information_confidence": 3, "input_cost_freight_bridge": 4, "margin_revision_bridge": 3, "market_mispricing": 4, "mobility_volume_visibility": 6, "operating_leverage_quality": 4, "total": 30, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C29_073240_KUMHOTIRE_20240502_TIRE_MARGIN_BETA_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["mobility_or_tire_volume_visibility", "export_replacement_mix_quality", "input_cost_freight_margin_revision_route"], "stage3_evidence_fields": ["shipment_volume_and_mix_persistence_required", "raw_material_freight_pass_through_required", "operating_leverage_margin_revision_bridge_required"], "stage4b_evidence_fields": ["tire_margin_recovery_price_premium", "volume_mix_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["volume_or_mix_disappointment", "input_cost_freight_margin_bridge_failure", "revision_momentum_break"], "symbol": "073240", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv", "trigger_date": "2024-05-02", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -36.21, "MAE_30D_pct": -12.0, "MAE_90D_pct": -36.21, "MFE_180D_pct": 1.05, "MFE_30D_pct": 1.05, "MFE_90D_pct": 1.05, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_002350_NEXENTIRE_20240411_TIRE_REPLACEMENT_FALSE_GREEN", "case_role": "tire_replacement_margin_false_green_counterexample", "company_name": "넥센타이어", "corporate_action_window_status": "clean post-2008 corporate-action forward window; corporate-action candidates are historical/latest 2008-03-21 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Tire replacement/export margin confirmation should stay Yellow or local 4B when price strength is not followed by fresh shipment volume, customer/mix proof, freight/raw-material bridge, inventory quality and margin/revision evidence. The April 2024 trigger had almost no residual upside and a much larger forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -36.88, "entry_date": "2024-04-11", "entry_price": 9500, "evidence_family": "tire_replacement_margin_price_confirmation_without_incremental_volume_mix_revision", "evidence_url_pending": false, "fine_archetype_id": "TIRE_REPLACEMENT_EXPORT_MARGIN_RECOVERY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-07-09", "low_price_180d": 6060, "peak_date": "2024-05-02", "peak_price": 9600, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/002/002350.json", "raw_component_score_breakdown": {"export_mix_or_replacement_demand": 4, "information_confidence": 3, "input_cost_freight_bridge": 4, "margin_revision_bridge": 2, "market_mispricing": 4, "mobility_volume_visibility": 5, "operating_leverage_quality": 3, "total": 26, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C29_002350_NEXENTIRE_20240411_TIRE_REPLACEMENT_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["mobility_or_tire_volume_visibility", "export_replacement_mix_quality", "input_cost_freight_margin_revision_route"], "stage3_evidence_fields": ["shipment_volume_and_mix_persistence_required", "raw_material_freight_pass_through_required", "operating_leverage_margin_revision_bridge_required"], "stage4b_evidence_fields": ["tire_margin_recovery_price_premium", "volume_mix_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["volume_or_mix_disappointment", "input_cost_freight_margin_bridge_failure", "revision_momentum_break"], "symbol": "002350", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002350/2024.csv", "trigger_date": "2024-04-11", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "TIRE_REPLACEMENT_EXPORT_MARGIN_RECOVERY_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "mobility_volume_margin_tire_replacement_export_margin_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R9",
  "shadow_rule_candidate": "C29 tire/mobility margin rows should allow Stage2 when export/replacement volume, mix, input-cost/freight bridge and margin-revision evidence are still expanding, but should route late tire-margin beta premiums to Yellow/local 4B when incremental volume-to-margin evidence has not refreshed.",
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
3. Add C29-specific tire volume/mix / replacement-export demand / raw-material-freight bridge / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C29_STAGE2_ALLOWED_ON_VOLUME_MIX_INPUTCOST_MARGIN_REVISION_BRIDGE
- C29_GREEN_REQUIRES_SHIPMENT_MIX_COST_PASS_THROUGH_AND_REVISION
- C29_TIRE_MARGIN_PRICE_PREMIUM_LOCAL_4B
- C29_PRICE_CONFIRMATION_WITHOUT_VOLUME_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

