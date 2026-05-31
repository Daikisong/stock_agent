# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C29 — Mobility volume-margin operating leverage / auto-parts late-cycle 4B guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_PARTS_VOLUME_MARGIN_LATE_CYCLE_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|late_cycle_operating_leverage_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_auto_parts_volume_margin_latecycle_2023_research.md
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

This run avoids those top-covered C29 symbols and adds 015750, 010690, and 005850.  
Each row uses a new `C29 + symbol + trigger_type + entry_date` hard key.

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
015750 성우하이텍: selected 2023 forward window clean; historical corporate-action candidates outside selected test window.
010690 화신: selected 2023 forward window clean; historical corporate-action candidates outside selected test window.
005850 에스엘: selected 2023 forward window clean; historical corporate-action candidates outside selected test window.
```

## 3. Research thesis

C29 should separate fresh auto-parts operating leverage from late-cycle volume/margin premium:

```text
mobility / auto-parts volume growth
→ OEM platform mix and utilization
→ FX and raw-material cost bridge
→ operating leverage and margin revision
→ rerating or local 4B cap
```

Auto-parts leverage is a gearbox. Stage2 can buy the first torque transfer from volume into margin, but Green should not keep paying the same torque once the gear is already fully engaged and revisions no longer accelerate.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C29_015750_SUNGWOO_20230216_AUTO_PARTS_VOLUME_MARGIN_STAGE2 | 015750 | positive_auto_parts_volume_margin_operating_leverage_stage2_success_with_later_4b_refresh | 2023-02-16 | 6230 | 16370 on 2023-07-12 | 5500 on 2023-02-16 | 27.45% | 80.26% | 162.76% | -11.72% | -52.11% |
| C29_010690_HWASHIN_20230706_AUTO_PARTS_VOLUME_MARGIN_PREMIUM_4B | 010690 | auto_parts_volume_margin_price_premium_counterexample | 2023-07-06 | 21000 | 22700 on 2023-07-06 | 9940 on 2023-10-26 | 8.1% | 8.1% | 8.1% | -52.67% | -56.21% |
| C29_005850_SL_20230717_AUTO_LIGHTING_MARGIN_FALSE_GREEN | 005850 | auto_lighting_operating_leverage_false_green_counterexample | 2023-07-17 | 38750 | 42400 on 2023-07-17 | 28500 on 2023-10-20 | 9.42% | 9.42% | 9.42% | -26.45% | -32.78% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 015750 is the positive anchor. The February 2023 route captured a large auto-parts volume/margin rerating before the July premium became a 4B refresh problem.
- Stage2 is allowed only when non-price evidence connects volume to OEM platform mix, utilization, FX/raw-material bridge and revision visibility.

### Stage3 / Green
- C29 Green should require platform volume, customer/OEM mix, utilization, operating leverage, FX/raw-material bridge and margin/revision confirmation.
- 005850 is the false-Green guard. Auto lighting and volume/margin leverage were real, but the July 2023 price confirmation did not supply enough incremental revision evidence after the price had already capitalized the operating leverage.

### 4B
- 010690 fills the auto-parts late-cycle price-premium pocket. The July 2023 trigger had small residual upside and a much larger forward drawdown.
- 005850 shows the same problem in a higher-quality lighting supplier: a real operating leverage story can become local 4B when the market has already paid for it.
- 015750 also demonstrates the transition from valid Stage2 to later local 4B once the rerating is capitalized.

### 4C
- No hard customer loss, plant shutdown or accounting break is asserted.
- The C29 break mode is evidence exhaustion: volume/margin leverage can remain real, but incremental platform volume, cost bridge and revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C29_005850_SL_20230717_AUTO_LIGHTING_MARGIN_FALSE_GREEN": {
    "fx_raw_material_bridge": 4,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "oem_platform_mix_quality": 5,
    "total": 30,
    "utilization_operating_leverage": 4,
    "valuation_rerating_runway": 1,
    "volume_growth_visibility": 6
  },
  "C29_010690_HWASHIN_20230706_AUTO_PARTS_VOLUME_MARGIN_PREMIUM_4B": {
    "fx_raw_material_bridge": 4,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "oem_platform_mix_quality": 5,
    "total": 30,
    "utilization_operating_leverage": 4,
    "valuation_rerating_runway": 1,
    "volume_growth_visibility": 6
  },
  "C29_015750_SUNGWOO_20230216_AUTO_PARTS_VOLUME_MARGIN_STAGE2": {
    "fx_raw_material_bridge": 7,
    "information_confidence": 4,
    "margin_revision_bridge": 8,
    "market_mispricing": 10,
    "oem_platform_mix_quality": 8,
    "total": 64,
    "utilization_operating_leverage": 9,
    "valuation_rerating_runway": 8,
    "volume_growth_visibility": 10
  }
}
```

## 7. Current calibrated profile stress test

Suggested C29 guard:
```text
if auto_parts_volume_growth and platform_mix_utilization_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if auto_parts_operating_leverage_price_premium and no incremental_platform_volume_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and volume_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 010690 / 2023-07-06: auto-parts volume/margin premium can be over-promoted if the model treats price heat as fresh platform-volume and margin-revision proof.
- 005850 / 2023-07-17: auto-lighting operating leverage can look like Yellow-to-Green, but fails without renewed customer mix, utilization and revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -11.72, "MAE_30D_pct": -11.72, "MAE_90D_pct": -11.72, "MFE_180D_pct": 162.76, "MFE_30D_pct": 27.45, "MFE_90D_pct": 80.26, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_015750_SUNGWOO_20230216_AUTO_PARTS_VOLUME_MARGIN_STAGE2", "case_role": "positive_auto_parts_volume_margin_operating_leverage_stage2_success_with_later_4b_refresh", "company_name": "성우하이텍", "corporate_action_window_status": "clean_2023_forward_window; historical corporate-action candidates outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when auto-parts volume, OEM mix and operating leverage appeared before the rerating was fully capitalized. Green still requires orderbook volume, platform mix, FX/raw-material bridge, utilization and margin/revision confirmation; after the July 2023 premium the same evidence required local 4B refresh discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -52.11, "entry_date": "2023-02-16", "entry_price": 6230, "evidence_family": "auto_parts_volume_margin_operating_leverage_export_oem_mix_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "AUTO_PARTS_VOLUME_MARGIN_LATE_CYCLE_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-02-16", "low_price_180d": 5500, "peak_date": "2023-07-12", "peak_price": 16370, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/015/015750.json", "raw_component_score_breakdown": {"fx_raw_material_bridge": 7, "information_confidence": 4, "margin_revision_bridge": 8, "market_mispricing": 10, "oem_platform_mix_quality": 8, "total": 64, "utilization_operating_leverage": 9, "valuation_rerating_runway": 8, "volume_growth_visibility": 10}, "reuse_reason": null, "same_entry_group_id": "C29_015750_SUNGWOO_20230216_AUTO_PARTS_VOLUME_MARGIN_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["mobility_volume_or_order_growth_visibility", "oem_platform_mix_and_utilization", "fx_raw_material_margin_revision_route"], "stage3_evidence_fields": ["platform_volume_and_customer_mix_required", "utilization_and_operating_leverage_required", "fx_raw_material_margin_revision_bridge_required"], "stage4b_evidence_fields": ["auto_parts_volume_margin_price_premium", "operating_leverage_story_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["volume_or_platform_mix_disappointment", "raw_material_fx_margin_bridge_failure", "revision_momentum_break"], "symbol": "015750", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/015/015750/2023.csv", "trigger_date": "2023-02-16", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -52.67, "MAE_30D_pct": -8.52, "MAE_90D_pct": -43.33, "MFE_180D_pct": 8.1, "MFE_30D_pct": 8.1, "MFE_90D_pct": 8.1, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_010690_HWASHIN_20230706_AUTO_PARTS_VOLUME_MARGIN_PREMIUM_4B", "case_role": "auto_parts_volume_margin_price_premium_counterexample", "company_name": "화신", "corporate_action_window_status": "clean_2023_forward_window; historical corporate-action candidates outside selected test window", "current_profile_error": true, "current_profile_verdict": "Auto-parts volume/margin premium should route to local 4B or counterexample when the stock has already capitalized operating leverage and incremental platform volume, utilization, FX/raw-material bridge and margin/revision evidence do not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -56.21, "entry_date": "2023-07-06", "entry_price": 21000, "evidence_family": "auto_parts_volume_margin_price_premium_without_incremental_platform_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "AUTO_PARTS_VOLUME_MARGIN_LATE_CYCLE_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-26", "low_price_180d": 9940, "peak_date": "2023-07-06", "peak_price": 22700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/010/010690.json", "raw_component_score_breakdown": {"fx_raw_material_bridge": 4, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "oem_platform_mix_quality": 5, "total": 30, "utilization_operating_leverage": 4, "valuation_rerating_runway": 1, "volume_growth_visibility": 6}, "reuse_reason": null, "same_entry_group_id": "C29_010690_HWASHIN_20230706_AUTO_PARTS_VOLUME_MARGIN_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["mobility_volume_or_order_growth_visibility", "oem_platform_mix_and_utilization", "fx_raw_material_margin_revision_route"], "stage3_evidence_fields": ["platform_volume_and_customer_mix_required", "utilization_and_operating_leverage_required", "fx_raw_material_margin_revision_bridge_required"], "stage4b_evidence_fields": ["auto_parts_volume_margin_price_premium", "operating_leverage_story_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["volume_or_platform_mix_disappointment", "raw_material_fx_margin_bridge_failure", "revision_momentum_break"], "symbol": "010690", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010690/2023.csv", "trigger_date": "2023-07-06", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -26.45, "MAE_30D_pct": -4.52, "MAE_90D_pct": -22.06, "MFE_180D_pct": 9.42, "MFE_30D_pct": 9.42, "MFE_90D_pct": 9.42, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_005850_SL_20230717_AUTO_LIGHTING_MARGIN_FALSE_GREEN", "case_role": "auto_lighting_operating_leverage_false_green_counterexample", "company_name": "에스엘", "corporate_action_window_status": "clean_2023_forward_window; historical corporate-action candidates outside selected test window", "current_profile_error": true, "current_profile_verdict": "Auto-lighting operating-leverage price confirmation should stay Yellow when price strength is not followed by fresh platform volume, customer mix, utilization, FX/raw-material and margin/revision evidence. The July 2023 peak had small residual upside and larger forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -32.78, "entry_date": "2023-07-17", "entry_price": 38750, "evidence_family": "auto_lighting_margin_price_confirmation_without_incremental_volume_platform_revision", "evidence_url_pending": false, "fine_archetype_id": "AUTO_PARTS_VOLUME_MARGIN_LATE_CYCLE_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-20", "low_price_180d": 28500, "peak_date": "2023-07-17", "peak_price": 42400, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005850.json", "raw_component_score_breakdown": {"fx_raw_material_bridge": 4, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "oem_platform_mix_quality": 5, "total": 30, "utilization_operating_leverage": 4, "valuation_rerating_runway": 1, "volume_growth_visibility": 6}, "reuse_reason": null, "same_entry_group_id": "C29_005850_SL_20230717_AUTO_LIGHTING_MARGIN_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["mobility_volume_or_order_growth_visibility", "oem_platform_mix_and_utilization", "fx_raw_material_margin_revision_route"], "stage3_evidence_fields": ["platform_volume_and_customer_mix_required", "utilization_and_operating_leverage_required", "fx_raw_material_margin_revision_bridge_required"], "stage4b_evidence_fields": ["auto_parts_volume_margin_price_premium", "operating_leverage_story_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["volume_or_platform_mix_disappointment", "raw_material_fx_margin_bridge_failure", "revision_momentum_break"], "symbol": "005850", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005850/2023.csv", "trigger_date": "2023-07-17", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "AUTO_PARTS_VOLUME_MARGIN_LATE_CYCLE_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "mobility_auto_parts_volume_margin_late_cycle_4b_guard_new_symbols",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C29 mobility volume/margin rows should allow Stage2 when volume growth is backed by OEM platform mix, utilization, FX/raw-material bridge and margin/revision evidence, but should route to local 4B/Yellow when operating-leverage premium is already capitalized and incremental platform volume or margin revisions have not refreshed.",
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
3. Add C29-specific auto-parts volume / platform mix / utilization / FX-raw material / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C29_STAGE2_ALLOWED_ON_PLATFORM_VOLUME_UTILIZATION_MARGIN_REVISION_BRIDGE
- C29_GREEN_REQUIRES_OEM_MIX_FX_RAW_MATERIAL_OPERATING_LEVERAGE_REVISION
- C29_AUTO_PARTS_OPERATING_LEVERAGE_PRICE_PREMIUM_LOCAL_4B
- C29_VOLUME_MARGIN_PRICE_CONFIRMATION_WITHOUT_INCREMENTAL_REVISION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

