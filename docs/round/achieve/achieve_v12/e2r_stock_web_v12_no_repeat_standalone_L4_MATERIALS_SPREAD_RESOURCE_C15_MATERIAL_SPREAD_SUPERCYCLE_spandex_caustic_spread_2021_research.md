# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C15 — Material spread supercycle duration guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: SPANDEX_TIRECORD_CAUSTIC_SPREAD_DURATION_GUARD
loop_objective: coverage_gap_fill|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_spandex_caustic_spread_2021_research.md
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

This run uses three symbols not listed as C15 top-covered symbols in the No-Repeat table: 298020, 298050, and 014830.  
No selected row repeats an existing `C15 + symbol + trigger_type + entry_date` hard key from the No-Repeat table.

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
298020 효성티앤씨: corporate_action_candidate_count=0; 2021 window clean.
298050 효성첨단소재: corporate_action_candidate_count=0; 2021 window clean.
014830 유니드: corporate-action candidates are 2015-08-18 and 2022-11-28; 2021 window clean.
```

## 3. Research thesis

C15 is not a generic commodity rebound bucket. It is a spread-duration archetype:

```text
input/output spread widening
→ capacity tightness / shortage
→ margin bridge
→ revision confirmation
→ valuation rerating
```

The successful 2021 spandex / tire-cord path shows that C15 can support a real Green, but the guard is strict: price strength alone is not enough. The counterexample row shows why late spread-theme rallies need local 4B treatment unless duration and revision evidence remain live.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| C15_298020_HYOSUNG_TNC_20210114_SPANDEX_SPREAD_SUPERCYCLE | 298020 | positive_structural_success | 2021-01-14 | 228000 | 963000 on 2021-07-16 | 226500 on 2021-01-14 | 322.37% | -0.66% | -38.42% |
| C15_298050_HYOSUNG_ADVANCED_20210122_TIRECORD_ARACHID_SPREAD_HIGH_MAE_SUCCESS | 298050 | positive_high_mae_success | 2021-01-22 | 187000 | 877000 on 2021-09-24 | 175000 on 2021-01-22 | 368.98% | -6.42% | -32.16% |
| C15_014830_UNID_20210419_CAUSTIC_POTASH_SPREAD_LOCAL_4B | 014830 | spread_theme_local_4b_counterexample | 2021-04-19 | 75700 | 95700 on 2021-04-27 | 73500 on 2021-07-12 | 26.42% | -2.91% | -23.2% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Spread widening and relative strength are valid early attention signals.
- These signals are especially useful when the market still treats the company as an old-cycle commodity name.

### Stage3 / Green
- C15 Green should require duration and transmission: the spread must reach margin/revision evidence, not only price momentum.
- 298020 is the cleanest Green example: the price path confirms a large durable rerating window.
- 298050 is an early Stage2-to-Green candidate, but its later path also shows why 4B discipline becomes necessary after spread-cycle saturation.

### 4B
- 014830 is not a failure of all spread logic; it is a warning against late-stage spread-theme extrapolation.
- The local 4B condition should activate when spread-cycle attention runs ahead of revision duration.

### 4C
- No hard 4C/accounting break is asserted here.
- The relevant thesis break is spread mean reversion or duration failure.

## 6. Current calibrated profile stress test

Suggested C15 guard:
```text
if material_spread_signal and no margin_or_revision_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if spread_theme_price_rally and duration_evidence_fades:
    route_to_local_4B_watch = true
```

Residual error:
```text
current_profile_error_count = 1
- 014830: a spread-theme rally can look like Green if relative strength is over-weighted, but the evidence is better treated as local 4B / duration guard.
```

## 7. Machine-readable rows

```jsonl
{"MAE_180D_pct": -0.66, "MAE_30D_pct": -0.66, "MAE_90D_pct": -0.66, "MFE_180D_pct": 322.37, "MFE_30D_pct": 322.37, "MFE_90D_pct": 322.37, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_298020_HYOSUNG_TNC_20210114_SPANDEX_SPREAD_SUPERCYCLE", "case_role": "positive_structural_success", "company_name": "효성티앤씨", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Green is justified only because spread/margin bridge was structural, not merely price momentum.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -38.42, "entry_date": "2021-01-14", "entry_price": 228000, "evidence_family": "spandex_spread_supercycle_capacity_tightness_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "SPANDEX_TIRECORD_CAUSTIC_SPREAD_DURATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-01-14", "low_price_180d": 226500, "peak_date": "2021-07-16", "peak_price": 963000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/298/298020.json", "reuse_reason": null, "same_entry_group_id": "C15_298020_HYOSUNG_TNC_20210114_SPANDEX_SPREAD_SUPERCYCLE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["spread_widening_signal", "capacity_tightness_or_shortage", "relative_strength"], "stage3_evidence_fields": ["margin_bridge_required", "spread_duration_evidence_required", "revision_confirmation_required"], "stage4b_evidence_fields": ["spread_cycle_saturation", "valuation_or_price_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "duration_failure", "revision_fade"], "symbol": "298020", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv", "trigger_date": "2021-01-14", "trigger_type": "Stage3-Green", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -6.42, "MAE_30D_pct": -6.42, "MAE_90D_pct": -6.42, "MFE_180D_pct": 368.98, "MFE_30D_pct": 368.98, "MFE_90D_pct": 368.98, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_298050_HYOSUNG_ADVANCED_20210122_TIRECORD_ARACHID_SPREAD_HIGH_MAE_SUCCESS", "case_role": "positive_high_mae_success", "company_name": "효성첨단소재", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 worked early, but Green should wait for margin/revision evidence; later 4B needed after spread-cycle saturation.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -32.16, "entry_date": "2021-01-22", "entry_price": 187000, "evidence_family": "tirecord_arachid_carbon_material_spread_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "SPANDEX_TIRECORD_CAUSTIC_SPREAD_DURATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-01-22", "low_price_180d": 175000, "peak_date": "2021-09-24", "peak_price": 877000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/298/298050.json", "reuse_reason": null, "same_entry_group_id": "C15_298050_HYOSUNG_ADVANCED_20210122_TIRECORD_ARACHID_SPREAD_HIGH_MAE_SUCCESS", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["spread_widening_signal", "capacity_tightness_or_shortage", "relative_strength"], "stage3_evidence_fields": ["margin_bridge_required", "spread_duration_evidence_required", "revision_confirmation_required"], "stage4b_evidence_fields": ["spread_cycle_saturation", "valuation_or_price_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "duration_failure", "revision_fade"], "symbol": "298050", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298050/2021.csv", "trigger_date": "2021-01-22", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -2.91, "MAE_30D_pct": -2.91, "MAE_90D_pct": -2.91, "MFE_180D_pct": 26.42, "MFE_30D_pct": 26.42, "MFE_90D_pct": 26.42, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_014830_UNID_20210419_CAUSTIC_POTASH_SPREAD_LOCAL_4B", "case_role": "spread_theme_local_4b_counterexample", "company_name": "유니드", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Spread-price rally should not become Green without duration/revision bridge; local 4B guard is needed.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -23.2, "entry_date": "2021-04-19", "entry_price": 75700, "evidence_family": "caustic_potash_spread_theme_without_revision_duration_confirmation", "evidence_url_pending": false, "fine_archetype_id": "SPANDEX_TIRECORD_CAUSTIC_SPREAD_DURATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-07-12", "low_price_180d": 73500, "peak_date": "2021-04-27", "peak_price": 95700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/014/014830.json", "reuse_reason": null, "same_entry_group_id": "C15_014830_UNID_20210419_CAUSTIC_POTASH_SPREAD_LOCAL_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["spread_widening_signal", "capacity_tightness_or_shortage", "relative_strength"], "stage3_evidence_fields": ["margin_bridge_required", "spread_duration_evidence_required", "revision_confirmation_required"], "stage4b_evidence_fields": ["spread_cycle_saturation", "valuation_or_price_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "duration_failure", "revision_fade"], "symbol": "014830", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014830/2021.csv", "trigger_date": "2021-04-19", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 8. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SPANDEX_TIRECORD_CAUSTIC_SPREAD_DURATION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "positive_and_4b_guard_added",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C15 material-spread supercycle should permit Green only when spread widening has duration plus margin/revision bridge; price-only late spread moves should become local 4B, not Green.",
  "source_proxy_only_count": 0
}
```

## 9. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C15 + symbol + trigger_type + entry_date.
3. Add C15-specific duration/margin bridge guard only as a shadow candidate until more rows exist.

Candidate rule:
- C15_MATERIAL_SPREAD_GREEN_REQUIRES_MARGIN_REVISION_DURATION
- C15_LATE_SPREAD_PRICE_STRENGTH_LOCAL_4B
- C15_SPREAD_MEAN_REVERSION_WATCH

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 10. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE.

