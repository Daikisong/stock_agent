# E2R V12 No-Repeat Standalone Residual Research
## R7 / L7 / C25 — Aesthetic medical-device export sell-through 4B refresh guard

metadata:
```text
selected_round: R7
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DEVICE_EXPORT_SELLTHROUGH_4B_REFRESH_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|new_trigger_family|counterexample_mining|positive_counterexample_balance|4B_refresh_after_stage2_success|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_aesthetic_sellthrough_4b_refresh_2023_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT prior coverage is already non-trivial, so this loop avoids the previous hard keys and adds one new symbol plus two new trigger-date/stage-transition rows.
Hard keys used here are new:
- C25 + 287410 + Stage2-Actionable + 2023-01-26
- C25 + 335890 + 4B-local-price-only + 2023-08-08
- C25 + 336570 + Stage3-Yellow + 2024-03-25
```

This run does not reuse the prior C25 214450/2023-04-03, 335890/2023-04-05, or 336570/2023-08-31 hard keys.

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
287410 제이시스메디칼: selected 2023 forward window clean; corporate-action candidates are 2020-12-24 and 2021-03-31, outside selected test window.
335890 비올: selected 2023/2024 forward window clean; corporate-action candidate is 2020-11-26, outside selected test window.
336570 원텍: selected 2024 forward window clean; corporate-action candidate is 2022-06-30, outside selected test window.
```

## 3. Research thesis

C25 should distinguish a fresh medical-device export acceleration from a fully priced aesthetic-device premium:

```text
aesthetic medical-device export demand
→ distributor sell-through and channel inventory quality
→ regulatory/geographic expansion
→ installed-base conversion and consumable/procedure repeat economics
→ ASP/mix, gross margin and revision bridge
→ rerating or local 4B cap
```

A device shipment is the first pulse. Green should require the heartbeat: repeat distributor sell-through, procedure volume, consumable/repeat revenue and margin revision.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C25_287410_JSYS_20230126_AESTHETIC_DEVICE_EXPORT_STAGE2 | 287410 | positive_aesthetic_device_export_sellthrough_stage2_success | 2023-01-26 | 9540 | 14500 on 2023-08-24 | 7980 on 2023-05-15 | 4.61% | 26.52% | 51.99% | -16.35% | -20.0% |
| C25_335890_VIOL_20230808_RF_MICRONEEDLE_EXPORT_PREMIUM_4B | 335890 | rf_microneedle_export_premium_4b_refresh_counterexample | 2023-08-08 | 8660 | 10000 on 2024-01-09 | 6170 on 2023-09-12 | 3.0% | 3.0% | 15.47% | -28.75% | -29.5% |
| C25_336570_WONTECH_20240325_AESTHETIC_DEVICE_EXPORT_FALSE_GREEN | 336570 | aesthetic_device_export_false_green_counterexample | 2024-03-25 | 10350 | 12030 on 2024-04-01 | 5560 on 2024-08-26 | 16.23% | 16.23% | 16.23% | -46.28% | -53.78% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 287410 is the new-symbol positive anchor. The January 2023 route produced a meaningful 180D MFE as aesthetic-device demand began to price export/distribution and margin leverage.
- Stage2 is allowed only when non-price evidence shows distributor sell-through, installed-base expansion and gross-margin revision visibility before the price fully capitalizes the story.

### Stage3 / Green
- C25 Green should require repeat distributor sell-through, clean channel inventory, regulatory/geographic expansion, installed-base conversion, recurring consumable or procedure economics, ASP/mix and revision confirmation.
- 336570 is the false-Green guard: March 2024 price confirmation did not prevent a large forward drawdown once incremental sell-through and margin evidence failed to keep expanding.

### 4B
- 335890 is a rerating-refresh row. Earlier Stage2 evidence can be valid, but a later August premium should be capped unless fresh distributor sell-through, consumable economics and margin revisions arrive.
- 336570 is the stronger local 4B/Yellow counterexample. The premium showed high MFE in the first week, but the 180D low and post-peak drawdown demonstrate why price strength cannot substitute for non-price export and margin proof.

### 4C
- No hard regulatory rejection, product recall or accounting break is asserted.
- The C25 break mode is distribution-to-margin exhaustion: export demand may remain plausible, but distributor inventory, repeat procedures, installed-base monetization and gross-margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C25_287410_JSYS_20230126_AESTHETIC_DEVICE_EXPORT_STAGE2": {
    "distribution_sellthrough_quality": 8,
    "export_revenue_acceleration": 10,
    "gross_margin_revision_bridge": 8,
    "information_confidence": 4,
    "market_mispricing": 9,
    "regulatory_reimbursement_quality": 7,
    "total": 53,
    "valuation_rerating_runway": 7
  },
  "C25_335890_VIOL_20230808_RF_MICRONEEDLE_EXPORT_PREMIUM_4B": {
    "distribution_sellthrough_quality": 4,
    "export_revenue_acceleration": 6,
    "gross_margin_revision_bridge": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "regulatory_reimbursement_quality": 5,
    "total": 27,
    "valuation_rerating_runway": 1
  },
  "C25_336570_WONTECH_20240325_AESTHETIC_DEVICE_EXPORT_FALSE_GREEN": {
    "distribution_sellthrough_quality": 4,
    "export_revenue_acceleration": 5,
    "gross_margin_revision_bridge": 4,
    "information_confidence": 3,
    "market_mispricing": 5,
    "regulatory_reimbursement_quality": 5,
    "total": 27,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C25 guard:
```text
if aesthetic_device_export_attention and distributor_sellthrough_installed_base_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if aesthetic_device_export_price_premium and no incremental_sellthrough_consumable_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and distribution_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 335890 / 2023-08-08: a valid earlier RF-microneedle Stage2 can become a 4B refresh problem once price has capitalized distributor growth.
- 336570 / 2024-03-25: aesthetic-device export price confirmation can be over-promoted if the model treats price momentum as sell-through and margin proof.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -16.35, "MAE_30D_pct": -9.43, "MAE_90D_pct": -16.35, "MFE_180D_pct": 51.99, "MFE_30D_pct": 4.61, "MFE_90D_pct": 26.52, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_287410_JSYS_20230126_AESTHETIC_DEVICE_EXPORT_STAGE2", "case_role": "positive_aesthetic_device_export_sellthrough_stage2_success", "company_name": "제이시스메디칼", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidates are 2020-12-24 and 2021-03-31, outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when aesthetic-device export/channel demand and margin-revision visibility appeared before the full rerating. Green still requires repeat distributor sell-through, regulatory/geographic expansion, installed-base conversion, consumable or repeat procedure economics, ASP/mix and revision confirmation.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -20.0, "entry_date": "2023-01-26", "entry_price": 9540, "evidence_family": "aesthetic_device_export_distributor_sellthrough_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_SELLTHROUGH_4B_REFRESH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2023-05-15", "low_price_180d": 7980, "peak_date": "2023-08-24", "peak_price": 14500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/287/287410.json", "raw_component_score_breakdown": {"distribution_sellthrough_quality": 8, "export_revenue_acceleration": 10, "gross_margin_revision_bridge": 8, "information_confidence": 4, "market_mispricing": 9, "regulatory_reimbursement_quality": 7, "total": 53, "valuation_rerating_runway": 7}, "reuse_reason": null, "same_entry_group_id": "C25_287410_JSYS_20230126_AESTHETIC_DEVICE_EXPORT_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_aesthetic_device_export_acceleration", "distributor_sellthrough_or_installed_base_visibility", "gross_margin_or_revision_route"], "stage3_evidence_fields": ["repeat_distributor_sellthrough_required", "regulatory_geographic_expansion_required", "installed_base_consumable_or_procedure_margin_revision_required"], "stage4b_evidence_fields": ["medical_aesthetic_export_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["distributor_inventory_or_sellthrough_gap", "regulatory_geographic_expansion_delay", "gross_margin_revision_bridge_failure"], "symbol": "287410", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/287/287410/2023.csv", "trigger_date": "2023-01-26", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -28.75, "MAE_30D_pct": -28.75, "MAE_90D_pct": -28.75, "MFE_180D_pct": 15.47, "MFE_30D_pct": 3.0, "MFE_90D_pct": 3.0, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_335890_VIOL_20230808_RF_MICRONEEDLE_EXPORT_PREMIUM_4B", "case_role": "rf_microneedle_export_premium_4b_refresh_counterexample", "company_name": "비올", "corporate_action_window_status": "clean_2023_2024_forward_window; corporate-action candidate is 2020-11-26, outside selected test window", "current_profile_error": true, "current_profile_verdict": "RF microneedle export premium should route to local 4B or counterexample after the first rerating unless fresh distributor sell-through, installed-base expansion, recurring consumables, regulatory reach, ASP/mix and margin/revision evidence keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -29.5, "entry_date": "2023-08-08", "entry_price": 8660, "evidence_family": "rf_microneedle_export_price_premium_without_incremental_sellthrough_consumable_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_SELLTHROUGH_4B_REFRESH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2023-09-12", "low_price_180d": 6170, "peak_date": "2024-01-09", "peak_price": 10000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/335/335890.json", "raw_component_score_breakdown": {"distribution_sellthrough_quality": 4, "export_revenue_acceleration": 6, "gross_margin_revision_bridge": 4, "information_confidence": 3, "market_mispricing": 4, "regulatory_reimbursement_quality": 5, "total": 27, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C25_335890_VIOL_20230808_RF_MICRONEEDLE_EXPORT_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_aesthetic_device_export_acceleration", "distributor_sellthrough_or_installed_base_visibility", "gross_margin_or_revision_route"], "stage3_evidence_fields": ["repeat_distributor_sellthrough_required", "regulatory_geographic_expansion_required", "installed_base_consumable_or_procedure_margin_revision_required"], "stage4b_evidence_fields": ["medical_aesthetic_export_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["distributor_inventory_or_sellthrough_gap", "regulatory_geographic_expansion_delay", "gross_margin_revision_bridge_failure"], "symbol": "335890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/335/335890/2023.csv", "trigger_date": "2023-08-08", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -46.28, "MAE_30D_pct": -12.37, "MAE_90D_pct": -23.29, "MFE_180D_pct": 16.23, "MFE_30D_pct": 16.23, "MFE_90D_pct": 16.23, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_336570_WONTECH_20240325_AESTHETIC_DEVICE_EXPORT_FALSE_GREEN", "case_role": "aesthetic_device_export_false_green_counterexample", "company_name": "원텍", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidate is 2022-06-30, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Aesthetic-device export recovery should remain Yellow when price confirmation is not followed by distributor sell-through, recurring consumable/procedure economics, regulatory/geographic expansion, ASP/mix, gross margin and revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -53.78, "entry_date": "2024-03-25", "entry_price": 10350, "evidence_family": "aesthetic_device_export_price_confirmation_without_distributor_sellthrough_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_SELLTHROUGH_4B_REFRESH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2024-08-26", "low_price_180d": 5560, "peak_date": "2024-04-01", "peak_price": 12030, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/336/336570.json", "raw_component_score_breakdown": {"distribution_sellthrough_quality": 4, "export_revenue_acceleration": 5, "gross_margin_revision_bridge": 4, "information_confidence": 3, "market_mispricing": 5, "regulatory_reimbursement_quality": 5, "total": 27, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C25_336570_WONTECH_20240325_AESTHETIC_DEVICE_EXPORT_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_aesthetic_device_export_acceleration", "distributor_sellthrough_or_installed_base_visibility", "gross_margin_or_revision_route"], "stage3_evidence_fields": ["repeat_distributor_sellthrough_required", "regulatory_geographic_expansion_required", "installed_base_consumable_or_procedure_margin_revision_required"], "stage4b_evidence_fields": ["medical_aesthetic_export_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["distributor_inventory_or_sellthrough_gap", "regulatory_geographic_expansion_delay", "gross_margin_revision_bridge_failure"], "symbol": "336570", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336570/2024.csv", "trigger_date": "2024-03-25", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_SELLTHROUGH_4B_REFRESH_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "loop_contribution_label": "medical_aesthetic_export_sellthrough_4b_refresh_new_date_symbol_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R7",
  "shadow_rule_candidate": "C25 aesthetic-device export rows should allow Stage2 only when export acceleration is backed by distributor sell-through, regulatory/geographic expansion, installed-base/consumable economics and gross-margin revision bridge; after rerating, price premium without incremental sell-through should route to local 4B or counterexample.",
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
3. Add C25-specific aesthetic-device export / distributor sell-through / installed-base / consumable-margin / local-4B refresh guard only as a shadow candidate until more rows exist.

Candidate rule:
- C25_STAGE2_ALLOWED_ON_EXPORT_SELLTHROUGH_INSTALLED_BASE_MARGIN_BRIDGE
- C25_GREEN_REQUIRES_REPEAT_SELLTHROUGH_REGULATORY_EXPANSION_CONSUMABLE_MARGIN_REVISION
- C25_AESTHETIC_DEVICE_PRICE_PREMIUM_LOCAL_4B_REFRESH
- C25_PRICE_CONFIRMATION_WITHOUT_DISTRIBUTOR_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.

