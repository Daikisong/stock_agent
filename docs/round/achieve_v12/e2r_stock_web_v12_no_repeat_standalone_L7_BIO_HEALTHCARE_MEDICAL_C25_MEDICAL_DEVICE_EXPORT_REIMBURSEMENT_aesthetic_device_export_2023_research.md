# E2R V12 No-Repeat Standalone Residual Research
## R7 / L7 / C25 — Aesthetic medical-device export / reimbursement guard

metadata:
```text
selected_round: R7
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DEVICE_EXPORT_CONSUMABLE_REORDER_REIMBURSEMENT_GUARD
loop_objective: coverage_gap_fill|positive_counterexample_balance|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_aesthetic_device_export_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT current coverage:
rows=54, symbols=10, date range=2022-05-16~2024-02-20, good/bad S2=23/7, 4B/4C=4/2
top covered symbols: 338220(15), 214150(12), 145720(7), 228670(6), 328130(4)
```

This run avoids those top-covered C25 symbols and adds 335890, 336570, and 287410.  
Each row uses a new `C25 + symbol + trigger_type + entry_date` hard key.

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
335890 비올: 2023 forward window clean; corporate-action candidate is 2020-11-26.
336570 원텍: 2023 forward window clean; corporate-action candidate is 2022-06-30.
287410 제이시스메디칼: 2023 forward window clean; corporate-action candidates are 2020-12-24 and 2021-03-31.
```

## 3. Research thesis

C25 should not be a generic medical-device momentum bucket. It should test whether device sales become repeatable, reimbursable, or consumable-linked:

```text
device export / aesthetic device attention
→ overseas channel or installed base expansion
→ consumable, reorder, reimbursement, or treatment-volume visibility
→ margin and revision bridge
→ rerating
```

The positive rows show that export and device-operating leverage can create real rerating windows. The counterexample shows the guard: a late price run in the same theme should not become fresh Green unless incremental export/reorder/reimbursement evidence arrives.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C25_335890_VIOL_20230113_AESTHETIC_RF_EXPORT_CONSUMABLE_RERATING | 335890 | positive_structural_success | 2023-01-13 | 3590 | 7400 on 2023-10-18 | 3430 on 2023-01-13 | 49.58% | 57.94% | 106.13% | -4.46% | -17.97% |
| C25_336570_WONTECH_20230329_AESTHETIC_LASER_EXPORT_OPERATING_LEVERAGE | 336570 | positive_high_mfe_success_but_4b_needed | 2023-03-29 | 6340 | 15110 on 2023-08-31 | 6160 on 2023-04-11 | 8.99% | 86.59% | 138.33% | -2.84% | -44.47% |
| C25_287410_JEISYS_20230824_AESTHETIC_DEVICE_LATE_FALSE_GREEN | 287410 | late_false_green_counterexample | 2023-08-24 | 13680 | 14500 on 2023-08-24 | 9950 on 2023-10-20 | 5.99% | 5.99% | 5.99% | -27.27% | -31.38% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Medical-device export attention and relative strength are valid early research routes.
- 336570 shows a useful early Stage2 route before the market fully capitalized the aesthetic-device operating-leverage story.

### Stage3 / Green
- C25 Green should require export reorder, consumable/reimbursement visibility, and margin/revision evidence.
- 335890 is the cleanest positive anchor because the price path shows a durable rerating window after early export/device traction.

### 4B
- 336570 later required 4B discipline after the large MFE. The same evidence that made Stage2 useful can become stale once valuation catches the story.
- 287410 is the late false-Green guard: post-run relative strength without incremental evidence should not be promoted.

### 4C
- No hard regulatory or accounting break is asserted.
- The relevant thesis break is softer: channel inventory, export reorder fade, reimbursement/consumable bridge gap, or revision fade.

## 6. Raw component score breakdown

```json
{
  "C25_287410_JEISYS_20230824_AESTHETIC_DEVICE_LATE_FALSE_GREEN": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 2,
    "eps_fcf_explosion": 7,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 36,
    "valuation_rerating_runway": 4,
    "visibility_quality": 7
  },
  "C25_335890_VIOL_20230113_AESTHETIC_RF_EXPORT_CONSUMABLE_RERATING": {
    "bottleneck_pricing_power": 13,
    "capital_allocation": 2,
    "eps_fcf_explosion": 15,
    "information_confidence": 4,
    "market_mispricing": 12,
    "total": 70,
    "valuation_rerating_runway": 10,
    "visibility_quality": 14
  },
  "C25_336570_WONTECH_20230329_AESTHETIC_LASER_EXPORT_OPERATING_LEVERAGE": {
    "bottleneck_pricing_power": 11,
    "capital_allocation": 2,
    "eps_fcf_explosion": 13,
    "information_confidence": 4,
    "market_mispricing": 12,
    "total": 64,
    "valuation_rerating_runway": 10,
    "visibility_quality": 12
  }
}
```

## 7. Current calibrated profile stress test

Suggested C25 guard:
```text
if medical_device_export_attention and no reorder_or_consumable_or_reimbursement_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if late_aesthetic_device_price_run and no incremental_revision_evidence:
    route_to_local_4B_watch = true

if post_peak_drawdown and channel_or_reorder_visibility_fades:
    route_to_counterexample_or_4C_watch = true
```

Residual error:
```text
current_profile_error_count = 1
- 287410 / 2023-08-24: late aesthetic-device relative strength could be over-promoted if C25 treats price confirmation as export/reimbursement quality.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -4.46, "MAE_30D_pct": -4.46, "MAE_90D_pct": -4.46, "MFE_180D_pct": 106.13, "MFE_30D_pct": 49.58, "MFE_90D_pct": 57.94, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_335890_VIOL_20230113_AESTHETIC_RF_EXPORT_CONSUMABLE_RERATING", "case_role": "positive_structural_success", "company_name": "비올", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Green can be justified only when device export traction closes into consumable/reorder visibility and margin/revision bridge; not merely K-medical-device theme heat.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -17.97, "entry_date": "2023-01-13", "entry_price": 3590, "evidence_family": "aesthetic_rf_device_export_consumable_reorder_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_CONSUMABLE_REORDER_REIMBURSEMENT_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2023-01-13", "low_price_180d": 3430, "peak_date": "2023-10-18", "peak_price": 7400, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/335/335890.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 13, "capital_allocation": 2, "eps_fcf_explosion": 15, "information_confidence": 4, "market_mispricing": 12, "total": 70, "valuation_rerating_runway": 10, "visibility_quality": 14}, "reuse_reason": null, "same_entry_group_id": "C25_335890_VIOL_20230113_AESTHETIC_RF_EXPORT_CONSUMABLE_RERATING", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_device_export_attention", "aesthetic_device_or_consumable_route", "relative_strength"], "stage3_evidence_fields": ["export_reorder_confirmation_required", "consumable_or_reimbursement_visibility_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["late_device_theme_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["export_order_fade_or_channel_inventory", "reimbursement_or_consumable_bridge_gap", "revision_or_margin_break"], "symbol": "335890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/335/335890/2023.csv", "trigger_date": "2023-01-13", "trigger_type": "Stage3-Green", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -2.84, "MAE_30D_pct": -2.84, "MAE_90D_pct": -2.84, "MFE_180D_pct": 138.33, "MFE_30D_pct": 8.99, "MFE_90D_pct": 86.59, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_336570_WONTECH_20230329_AESTHETIC_LASER_EXPORT_OPERATING_LEVERAGE", "case_role": "positive_high_mfe_success_but_4b_needed", "company_name": "원텍", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful early, but after the large MFE the profile should shift toward 4B watch unless export/reorder and revision evidence keep improving.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.47, "entry_date": "2023-03-29", "entry_price": 6340, "evidence_family": "aesthetic_laser_device_export_operating_leverage_reorder_route", "evidence_url_pending": false, "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_CONSUMABLE_REORDER_REIMBURSEMENT_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2023-04-11", "low_price_180d": 6160, "peak_date": "2023-08-31", "peak_price": 15110, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/336/336570.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 11, "capital_allocation": 2, "eps_fcf_explosion": 13, "information_confidence": 4, "market_mispricing": 12, "total": 64, "valuation_rerating_runway": 10, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C25_336570_WONTECH_20230329_AESTHETIC_LASER_EXPORT_OPERATING_LEVERAGE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_device_export_attention", "aesthetic_device_or_consumable_route", "relative_strength"], "stage3_evidence_fields": ["export_reorder_confirmation_required", "consumable_or_reimbursement_visibility_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["late_device_theme_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["export_order_fade_or_channel_inventory", "reimbursement_or_consumable_bridge_gap", "revision_or_margin_break"], "symbol": "336570", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336570/2023.csv", "trigger_date": "2023-03-29", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -27.27, "MAE_30D_pct": -18.06, "MAE_90D_pct": -27.27, "MFE_180D_pct": 5.99, "MFE_30D_pct": 5.99, "MFE_90D_pct": 5.99, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_287410_JEISYS_20230824_AESTHETIC_DEVICE_LATE_FALSE_GREEN", "case_role": "late_false_green_counterexample", "company_name": "제이시스메디칼", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Late relative strength in aesthetic-device names should not become fresh Green without incremental export/reimbursement/revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -31.38, "entry_date": "2023-08-24", "entry_price": 13680, "evidence_family": "aesthetic_device_export_theme_late_entry_without_incremental_reimbursement_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_CONSUMABLE_REORDER_REIMBURSEMENT_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2023-10-20", "low_price_180d": 9950, "peak_date": "2023-08-24", "peak_price": 14500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/287/287410.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 2, "eps_fcf_explosion": 7, "information_confidence": 3, "market_mispricing": 5, "total": 36, "valuation_rerating_runway": 4, "visibility_quality": 7}, "reuse_reason": null, "same_entry_group_id": "C25_287410_JEISYS_20230824_AESTHETIC_DEVICE_LATE_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_device_export_attention", "aesthetic_device_or_consumable_route", "relative_strength"], "stage3_evidence_fields": ["export_reorder_confirmation_required", "consumable_or_reimbursement_visibility_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["late_device_theme_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["export_order_fade_or_channel_inventory", "reimbursement_or_consumable_bridge_gap", "revision_or_margin_break"], "symbol": "287410", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/287/287410/2023.csv", "trigger_date": "2023-08-24", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_CONSUMABLE_REORDER_REIMBURSEMENT_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "loop_contribution_label": "medical_device_export_new_symbol_and_late_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R7",
  "shadow_rule_candidate": "C25 medical-device/aesthetic-device export rerating should permit Stage2/Green only when export reorder, consumable or reimbursement visibility, and margin/revision bridge close; late theme strength without incremental evidence should cap at Yellow or local 4B.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C25 + symbol + trigger_type + entry_date.
3. Add C25-specific export/reorder/consumable/reimbursement bridge logic only as a shadow candidate until more rows exist.

Candidate rule:
- C25_DEVICE_GREEN_REQUIRES_EXPORT_REORDER_CONSUMABLE_REIMBURSEMENT_BRIDGE
- C25_AESTHETIC_DEVICE_RELATIVE_STRENGTH_STAGE2_CAP
- C25_LATE_DEVICE_THEME_LOCAL_4B

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R7/L7_BIO_HEALTHCARE_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.

