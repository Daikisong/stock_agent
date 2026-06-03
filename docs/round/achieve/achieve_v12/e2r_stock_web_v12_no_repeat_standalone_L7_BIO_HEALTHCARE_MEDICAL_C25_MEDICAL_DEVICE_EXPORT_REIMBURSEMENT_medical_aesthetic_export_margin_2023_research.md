# E2R V12 No-Repeat Standalone Residual Research
## R7 / L7 / C25 — Medical device export/reimbursement margin guard

metadata:
```text
selected_round: R7
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: MEDICAL_AESTHETIC_EXPORT_DISTRIBUTION_MARGIN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_medical_aesthetic_export_margin_2023_research.md
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

This run avoids those top-covered C25 symbols and adds 214450, 335890, and 336570.  
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
214450 파마리서치: corporate_action_candidate_count=0.
335890 비올: selected 2023 forward window clean; corporate-action candidate is 2020-11-26 and outside selected test window.
336570 원텍: selected 2023/2024 forward window clean; corporate-action candidate is 2022-06-30 and outside selected test window.
```

## 3. Research thesis

C25 should not treat every medical-device export headline as a durable reimbursement or margin rerating. It should test whether export demand becomes repeat distributor sell-through, approved markets and recurring procedure/device economics:

```text
medical device export / aesthetic device demand
→ regulatory approval or reimbursement reach
→ distributor sell-through and channel inventory quality
→ device + consumable repeat revenue and ASP/mix
→ gross margin and revision bridge
→ rerating or local 4B cap
```

A device shipment is the first pulse. Green should require the heartbeat: repeat procedures, clean distributor inventory, consumable reorder and a margin revision that keeps showing up.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C25_214450_PHARMARESEARCH_20230403_AESTHETIC_DEVICE_EXPORT_MARGIN_STAGE2 | 214450 | positive_medical_aesthetic_export_margin_stage2_success_with_later_4b_refresh | 2023-04-03 | 75100 | 158200 on 2023-08-11 | 70900 on 2023-04-03 | 64.85% | 110.65% | 110.65% | -5.59% | -27.12% |
| C25_335890_VIOL_20230405_RF_MICRONEEDLE_EXPORT_STAGE2 | 335890 | positive_rf_microneedle_export_margin_stage2_success_with_later_4b_refresh | 2023-04-05 | 5390 | 8920 on 2023-08-08 | 4715 on 2023-04-13 | 23.93% | 65.49% | 65.49% | -12.52% | -30.83% |
| C25_336570_WONTECH_20230831_AESTHETIC_EXPORT_PRICE_PREMIUM_4B | 336570 | aesthetic_device_export_price_premium_counterexample | 2023-08-31 | 14890 | 15110 on 2023-08-31 | 7600 on 2024-02-08 | 1.48% | 1.48% | 1.48% | -48.96% | -49.7% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Medical aesthetic export can be a valid Stage2 route when export acceleration is backed by distributor sell-through, approved-market expansion, recurring consumable economics and margin/revision evidence.
- 214450 is the larger-cap positive anchor. The April 2023 route produced strong 30D and 90D MFE as export/distribution and margin revision evidence were capitalized.
- 335890 is the smaller-device positive anchor. The April 2023 RF-microneedle route produced large forward MFE before the August premium required 4B discipline.

### Stage3 / Green
- C25 Green should require repeat distributor sell-through, channel inventory quality, regulatory/reimbursement reach, recurring consumable revenue, ASP/mix, gross margin and revision confirmation.
- A device export shipment alone is not enough. The model should ask whether the distributor is clearing inventory and whether procedure volume creates repeat consumable revenue.

### 4B
- 336570 fills the aesthetic-device price-premium 4B pocket. The August 2023 trigger had little further upside from the trigger-day high and then drew down sharply as incremental sell-through and margin evidence did not refresh quickly enough.
- 214450 and 335890 also show the same transition: valid Stage2 export/margin evidence can later become a fully capitalized premium requiring local 4B discipline.

### 4C
- No hard regulatory rejection, product recall or accounting break is asserted.
- The C25 break mode is distribution-to-margin exhaustion: export demand remains plausible, but sell-through, channel inventory, recurring consumables, approval/reimbursement reach, gross margin and revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C25_214450_PHARMARESEARCH_20230403_AESTHETIC_DEVICE_EXPORT_MARGIN_STAGE2": {
    "distribution_sellthrough_quality": 9,
    "export_revenue_acceleration": 11,
    "gross_margin_revision_bridge": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "regulatory_reimbursement_quality": 7,
    "total": 59,
    "valuation_rerating_runway": 8
  },
  "C25_335890_VIOL_20230405_RF_MICRONEEDLE_EXPORT_STAGE2": {
    "distribution_sellthrough_quality": 8,
    "export_revenue_acceleration": 10,
    "gross_margin_revision_bridge": 9,
    "information_confidence": 4,
    "market_mispricing": 10,
    "regulatory_reimbursement_quality": 7,
    "total": 56,
    "valuation_rerating_runway": 8
  },
  "C25_336570_WONTECH_20230831_AESTHETIC_EXPORT_PRICE_PREMIUM_4B": {
    "distribution_sellthrough_quality": 4,
    "export_revenue_acceleration": 5,
    "gross_margin_revision_bridge": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "regulatory_reimbursement_quality": 5,
    "total": 26,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C25 guard:
```text
if medical_device_export_attention and distributor_sellthrough_consumable_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if medical_device_export_price_premium and no incremental_sellthrough_regulatory_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and distribution_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual error:
```text
current_profile_error_count = 1
- 336570 / 2023-08-31: aesthetic-device export premium can be over-promoted if the model treats price strength as proof of incremental sell-through, consumable repeat revenue and margin revision.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -5.59, "MAE_30D_pct": -5.59, "MAE_90D_pct": -5.59, "MFE_180D_pct": 110.65, "MFE_30D_pct": 64.85, "MFE_90D_pct": 110.65, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_214450_PHARMARESEARCH_20230403_AESTHETIC_DEVICE_EXPORT_MARGIN_STAGE2", "case_role": "positive_medical_aesthetic_export_margin_stage2_success_with_later_4b_refresh", "company_name": "파마리서치", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2023_forward_window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when medical-aesthetic export/distribution strength and margin revision visibility appeared before the rerating was fully capitalized. Green still requires repeat export sell-through, distributor inventory quality, regulatory/approval reach, ASP/mix, procedure reimbursement optionality and revision bridge; after the August 2023 premium, the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -27.12, "entry_date": "2023-04-03", "entry_price": 75100, "evidence_family": "medical_aesthetic_export_distribution_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "MEDICAL_AESTHETIC_EXPORT_DISTRIBUTION_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2023-04-03", "low_price_180d": 70900, "peak_date": "2023-08-11", "peak_price": 158200, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/214/214450.json", "raw_component_score_breakdown": {"distribution_sellthrough_quality": 9, "export_revenue_acceleration": 11, "gross_margin_revision_bridge": 10, "information_confidence": 4, "market_mispricing": 10, "regulatory_reimbursement_quality": 7, "total": 59, "valuation_rerating_runway": 8}, "reuse_reason": null, "same_entry_group_id": "C25_214450_PHARMARESEARCH_20230403_AESTHETIC_DEVICE_EXPORT_MARGIN_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_device_export_or_distribution_acceleration", "regulatory_approval_or_reimbursement_reach_signal", "gross_margin_or_revision_route"], "stage3_evidence_fields": ["repeat_distributor_sellthrough_required", "regulatory_reimbursement_and_geographic_expansion_required", "consumable_repeat_revenue_ASP_mix_margin_revision_required"], "stage4b_evidence_fields": ["medical_device_export_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["distributor_inventory_or_sellthrough_disappointment", "regulatory_or_reimbursement_delay", "gross_margin_revision_bridge_failure"], "symbol": "214450", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214450/2023.csv", "trigger_date": "2023-04-03", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -12.52, "MAE_30D_pct": -12.52, "MAE_90D_pct": -12.52, "MFE_180D_pct": 65.49, "MFE_30D_pct": 23.93, "MFE_90D_pct": 65.49, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_335890_VIOL_20230405_RF_MICRONEEDLE_EXPORT_STAGE2", "case_role": "positive_rf_microneedle_export_margin_stage2_success_with_later_4b_refresh", "company_name": "비올", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidate is 2020-11-26 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when RF microneedle export demand, distributor reorder visibility and high-margin device/consumable mix created a clear revision route. Green still requires distributor sell-through, recurring consumable revenue, regulatory approvals, channel inventory, gross margin and revision confirmation; after the August 2023 premium, the same evidence required 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -30.83, "entry_date": "2023-04-05", "entry_price": 5390, "evidence_family": "rf_microneedle_device_export_distributor_reorder_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "MEDICAL_AESTHETIC_EXPORT_DISTRIBUTION_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2023-04-13", "low_price_180d": 4715, "peak_date": "2023-08-08", "peak_price": 8920, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/335/335890.json", "raw_component_score_breakdown": {"distribution_sellthrough_quality": 8, "export_revenue_acceleration": 10, "gross_margin_revision_bridge": 9, "information_confidence": 4, "market_mispricing": 10, "regulatory_reimbursement_quality": 7, "total": 56, "valuation_rerating_runway": 8}, "reuse_reason": null, "same_entry_group_id": "C25_335890_VIOL_20230405_RF_MICRONEEDLE_EXPORT_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_device_export_or_distribution_acceleration", "regulatory_approval_or_reimbursement_reach_signal", "gross_margin_or_revision_route"], "stage3_evidence_fields": ["repeat_distributor_sellthrough_required", "regulatory_reimbursement_and_geographic_expansion_required", "consumable_repeat_revenue_ASP_mix_margin_revision_required"], "stage4b_evidence_fields": ["medical_device_export_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["distributor_inventory_or_sellthrough_disappointment", "regulatory_or_reimbursement_delay", "gross_margin_revision_bridge_failure"], "symbol": "335890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/335/335890/2023.csv", "trigger_date": "2023-04-05", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -48.96, "MAE_30D_pct": -31.16, "MAE_90D_pct": -47.68, "MFE_180D_pct": 1.48, "MFE_30D_pct": 1.48, "MFE_90D_pct": 1.48, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_336570_WONTECH_20230831_AESTHETIC_EXPORT_PRICE_PREMIUM_4B", "case_role": "aesthetic_device_export_price_premium_counterexample", "company_name": "원텍", "corporate_action_window_status": "clean_2023_2024_forward_window; corporate-action candidate is 2022-06-30 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Aesthetic-device export price premium should route to local 4B or counterexample when the stock has already capitalized export growth and incremental distributor sell-through, consumable repeat revenue, regulatory expansion, ASP/mix, gross margin and revision evidence do not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -49.7, "entry_date": "2023-08-31", "entry_price": 14890, "evidence_family": "aesthetic_device_export_price_premium_without_incremental_distributor_sellthrough_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "MEDICAL_AESTHETIC_EXPORT_DISTRIBUTION_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2024-02-08", "low_price_180d": 7600, "peak_date": "2023-08-31", "peak_price": 15110, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/336/336570.json", "raw_component_score_breakdown": {"distribution_sellthrough_quality": 4, "export_revenue_acceleration": 5, "gross_margin_revision_bridge": 4, "information_confidence": 3, "market_mispricing": 4, "regulatory_reimbursement_quality": 5, "total": 26, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C25_336570_WONTECH_20230831_AESTHETIC_EXPORT_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_device_export_or_distribution_acceleration", "regulatory_approval_or_reimbursement_reach_signal", "gross_margin_or_revision_route"], "stage3_evidence_fields": ["repeat_distributor_sellthrough_required", "regulatory_reimbursement_and_geographic_expansion_required", "consumable_repeat_revenue_ASP_mix_margin_revision_required"], "stage4b_evidence_fields": ["medical_device_export_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["distributor_inventory_or_sellthrough_disappointment", "regulatory_or_reimbursement_delay", "gross_margin_revision_bridge_failure"], "symbol": "336570", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336570/2023.csv", "trigger_date": "2023-08-31", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "MEDICAL_AESTHETIC_EXPORT_DISTRIBUTION_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "loop_contribution_label": "medical_device_export_reimbursement_aesthetic_export_margin_new_symbols_and_4b_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R7",
  "shadow_rule_candidate": "C25 medical-device export/reimbursement rows should allow Stage2 when export acceleration is backed by distributor sell-through, regulatory/reimbursement reach, recurring consumable revenue, ASP/mix and gross-margin revision bridge, but Stage3 Green requires repeat sell-through and margin revision; medical aesthetic export price premium without incremental non-price proof should route to local 4B or counterexample.",
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
3. Add C25-specific medical-device export / reimbursement-reach / distributor sell-through / consumable-margin / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C25_STAGE2_ALLOWED_ON_EXPORT_SELLTHROUGH_CONSUMABLE_MARGIN_REVISION_BRIDGE
- C25_GREEN_REQUIRES_REGULATORY_REIMBURSEMENT_SELLTHROUGH_ASP_MIX_MARGIN_REVISION
- C25_MEDICAL_DEVICE_EXPORT_PRICE_PREMIUM_LOCAL_4B
- C25_EXPORT_WITHOUT_DISTRIBUTOR_SELLTHROUGH_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R7/L7_BIO_HEALTHCARE_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.

