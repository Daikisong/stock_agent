# E2R V12 No-Repeat Standalone Residual Research
## R7 / L7 / C25 — Medical device export / reimbursement adoption guard

metadata:
```text
selected_round: R7
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: ROBOT_CGM_IMAGING_EXPORT_REIMBURSEMENT_ADOPTION_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_robot_cgm_imaging_export_2022_2024_research.md
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

This run avoids those top-covered C25 symbols and adds 060280, 099190, and 100120.  
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
060280 큐렉소: 2023 forward window clean; corporate-action candidates are old, outside the selected test window.
099190 아이센스: 2024 forward window clean; 2023 corporate-action candidates are outside the selected 2024 entry window.
100120 뷰웍스: 2022 forward window clean; corporate-action candidate is 2011-08-08, outside the test window.
```

## 3. Research thesis

C25 is not a generic healthcare momentum bucket. It should test whether device attention becomes adopted, reimbursed revenue:

```text
medical device export / reimbursement / install-base attention
→ installation or adoption conversion
→ utilization and repeat consumable or service revenue
→ reimbursement cadence or order durability
→ gross margin and revision bridge
→ rerating
```

The machine can be installed before the business is installed. C25 should pay for utilization and reimbursement, not just a device sitting in the hospital corridor.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C25_060280_CUREXO_20230316_MEDICAL_ROBOT_EXPORT_STAGE2_SUCCESS | 060280 | positive_medical_robot_export_stage2_success_with_later_4b | 2023-03-16 | 11000 | 25750 on 2023-08-24 | 10890 on 2023-04-10 | 50.82% | 106.82% | 134.09% | -1.0% | -49.59% |
| C25_099190_ISENS_20240110_CGM_REIMBURSEMENT_PRICE_PREMIUM_FALSE_GREEN | 099190 | cgm_reimbursement_false_green_counterexample | 2024-01-10 | 29500 | 30400 on 2024-01-12 | 14520 on 2024-09-09 | 3.05% | 3.05% | 3.05% | -50.78% | -52.24% |
| C25_100120_VIEWORKS_20220511_MEDICAL_IMAGING_EXPORT_MARGIN_FALSE_GREEN | 100120 | medical_imaging_export_margin_false_green_counterexample | 2022-05-11 | 39100 | 44300 on 2022-08-12 | 29650 on 2022-12-21 | 4.35% | 13.3% | 13.3% | -24.17% | -33.07% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Medical-device export, installation, reimbursement and device-monetization attention can be valid Stage2 routes.
- 060280 is the positive anchor: robot/device export and install-base optionality created a strong MFE, but later drawdown shows why Stage2 success must mature into 4B discipline if utilization/revision evidence stops expanding.

### Stage3 / Green
- C25 Green should require adoption or installation conversion, utilization, reimbursement cadence, gross margin and revision confirmation.
- 099190 and 100120 show why reimbursement/export language should not be promoted if adoption, utilization, order durability and margin bridge are not visible.

### 4B
- 060280 after the August 2023 peak required local 4B discipline despite a valid earlier Stage2.
- 099190 and 100120 show softer price-premium failure: the market paid for device optionality before the income statement had enough utilization and revision bodyweight.

### 4C
- No hard accounting or approval break is asserted.
- The C25 break mode is adoption-to-revenue failure: the device story remains plausible, but utilization, reimbursement cadence, export order durability, consumable/service revenue or margin bridge does not support the valuation.

## 6. Raw component score breakdown

```json
{
  "C25_060280_CUREXO_20230316_MEDICAL_ROBOT_EXPORT_STAGE2_SUCCESS": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 56,
    "valuation_rerating_runway": 9,
    "visibility_quality": 11
  },
  "C25_099190_ISENS_20240110_CGM_REIMBURSEMENT_PRICE_PREMIUM_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 30,
    "valuation_rerating_runway": 3,
    "visibility_quality": 6
  },
  "C25_100120_VIEWORKS_20220511_MEDICAL_IMAGING_EXPORT_MARGIN_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 3,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 31,
    "valuation_rerating_runway": 3,
    "visibility_quality": 6
  }
}
```

## 7. Current calibrated profile stress test

Suggested C25 guard:
```text
if medical_device_export_or_reimbursement_attention and install_base_or_order_visibility:
    allow_stage2_actionable = true

if device_price_premium and no adoption_utilization_reimbursement_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and utilization_or_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 099190 / 2024-01-10: CGM/reimbursement optionality can be over-promoted if adoption ramp, utilization and reimbursement cadence are not required.
- 100120 / 2022-05-11: medical-imaging export strength can look like Green, but the later path argues for Yellow/counterexample when order durability and margin revisions fade.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -1.0, "MAE_30D_pct": -1.0, "MAE_90D_pct": -1.0, "MFE_180D_pct": 134.09, "MFE_30D_pct": 50.82, "MFE_90D_pct": 106.82, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_060280_CUREXO_20230316_MEDICAL_ROBOT_EXPORT_STAGE2_SUCCESS", "case_role": "positive_medical_robot_export_stage2_success_with_later_4b", "company_name": "큐렉소", "corporate_action_window_status": "clean_forward_window; old corporate-action candidates outside selected test window where present", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when medical-robot export/install-base attention created a credible device monetization route, but Green still requires installation conversion, utilization, service revenue, reimbursement and revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -49.59, "entry_date": "2023-03-16", "entry_price": 11000, "evidence_family": "medical_robot_export_install_base_reimbursement_optionality_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "ROBOT_CGM_IMAGING_EXPORT_REIMBURSEMENT_ADOPTION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2023-04-10", "low_price_180d": 10890, "peak_date": "2023-08-24", "peak_price": 25750, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/060/060280.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 11, "total": 56, "valuation_rerating_runway": 9, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C25_060280_CUREXO_20230316_MEDICAL_ROBOT_EXPORT_STAGE2_SUCCESS", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_device_export_or_reimbursement_attention", "install_base_or_order_visibility_claim", "relative_strength_after_device_monetization_signal"], "stage3_evidence_fields": ["adoption_or_installation_conversion_required", "utilization_reimbursement_cadence_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["device_export_reimbursement_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["adoption_or_utilization_shortfall", "reimbursement_or_export_order_delay", "margin_revision_bridge_failure"], "symbol": "060280", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/060/060280/2023.csv", "trigger_date": "2023-03-16", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -50.78, "MAE_30D_pct": -30.34, "MAE_90D_pct": -36.0, "MFE_180D_pct": 3.05, "MFE_30D_pct": 3.05, "MFE_90D_pct": 3.05, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_099190_ISENS_20240110_CGM_REIMBURSEMENT_PRICE_PREMIUM_FALSE_GREEN", "case_role": "cgm_reimbursement_false_green_counterexample", "company_name": "아이센스", "corporate_action_window_status": "clean_forward_window; old corporate-action candidates outside selected test window where present", "current_profile_error": true, "current_profile_verdict": "CGM/reimbursement attention should stay Yellow when adoption ramp, sensor utilization, reimbursement cadence, gross margin and revision evidence are not confirmed.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -52.24, "entry_date": "2024-01-10", "entry_price": 29500, "evidence_family": "cgm_reimbursement_optional_claim_without_adoption_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "ROBOT_CGM_IMAGING_EXPORT_REIMBURSEMENT_ADOPTION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2024-09-09", "low_price_180d": 14520, "peak_date": "2024-01-12", "peak_price": 30400, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/099/099190.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 30, "valuation_rerating_runway": 3, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C25_099190_ISENS_20240110_CGM_REIMBURSEMENT_PRICE_PREMIUM_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_device_export_or_reimbursement_attention", "install_base_or_order_visibility_claim", "relative_strength_after_device_monetization_signal"], "stage3_evidence_fields": ["adoption_or_installation_conversion_required", "utilization_reimbursement_cadence_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["device_export_reimbursement_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["adoption_or_utilization_shortfall", "reimbursement_or_export_order_delay", "margin_revision_bridge_failure"], "symbol": "099190", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv", "trigger_date": "2024-01-10", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -24.17, "MAE_30D_pct": -10.36, "MAE_90D_pct": -14.45, "MFE_180D_pct": 13.3, "MFE_30D_pct": 4.35, "MFE_90D_pct": 13.3, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_100120_VIEWORKS_20220511_MEDICAL_IMAGING_EXPORT_MARGIN_FALSE_GREEN", "case_role": "medical_imaging_export_margin_false_green_counterexample", "company_name": "뷰웍스", "corporate_action_window_status": "clean_forward_window; old corporate-action candidates outside selected test window where present", "current_profile_error": true, "current_profile_verdict": "Medical-imaging export strength should not become Green unless order visibility, ASP/mix, gross margin and revision durability continue after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -33.07, "entry_date": "2022-05-11", "entry_price": 39100, "evidence_family": "medical_imaging_export_device_price_strength_without_order_margin_revision_duration", "evidence_url_pending": false, "fine_archetype_id": "ROBOT_CGM_IMAGING_EXPORT_REIMBURSEMENT_ADOPTION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2022-12-21", "low_price_180d": 29650, "peak_date": "2022-08-12", "peak_price": 44300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/100/100120.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 3, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 31, "valuation_rerating_runway": 3, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C25_100120_VIEWORKS_20220511_MEDICAL_IMAGING_EXPORT_MARGIN_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_device_export_or_reimbursement_attention", "install_base_or_order_visibility_claim", "relative_strength_after_device_monetization_signal"], "stage3_evidence_fields": ["adoption_or_installation_conversion_required", "utilization_reimbursement_cadence_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["device_export_reimbursement_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["adoption_or_utilization_shortfall", "reimbursement_or_export_order_delay", "margin_revision_bridge_failure"], "symbol": "100120", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100120/2022.csv", "trigger_date": "2022-05-11", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "ROBOT_CGM_IMAGING_EXPORT_REIMBURSEMENT_ADOPTION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "loop_contribution_label": "medical_device_robot_cgm_imaging_export_reimbursement_guard_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R7",
  "shadow_rule_candidate": "C25 medical-device export/reimbursement rows should allow Stage2 on early device monetization/export/install-base attention, but Stage3 Green requires adoption or installation conversion, utilization, reimbursement cadence, gross margin and revision bridge; device price premium without utilization proof should route to local 4B or counterexample.",
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
3. Add C25-specific adoption/utilization/reimbursement/margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C25_STAGE2_ALLOWED_ON_DEVICE_EXPORT_INSTALL_BASE_ATTENTION
- C25_GREEN_REQUIRES_ADOPTION_UTILIZATION_REIMBURSEMENT_MARGIN_REVISION
- C25_DEVICE_PRICE_PREMIUM_LOCAL_4B
- C25_DEVICE_STORY_WITHOUT_UTILIZATION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.

