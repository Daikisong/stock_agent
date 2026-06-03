# E2R V12 No-Repeat Standalone Residual Research
## R7 / L7 / C25 — Medical device export / reimbursement guard

metadata:
```text
selected_round: R7
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L7_HEALTHCARE_BIO_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DIAGNOSTIC_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L7_HEALTHCARE_BIO_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_aesthetic_diagnostic_export_reimbursement_2023_2024_research.md
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

This run avoids those top-covered C25 symbols and adds 336570, 099190, and 100120.  
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
336570 원텍: 2023 forward window clean; corporate-action candidate is 2022-06-30 and outside selected test window.
099190 아이센스: 2024 forward window clean; corporate-action candidates are 2015-10-02, 2023-03-14 and 2023-04-10, outside selected test window.
100120 뷰웍스: 2023 forward window clean; corporate-action candidate is 2011-08-08 and outside selected test window.
```

## 3. Research thesis

C25 should not treat every export or reimbursement headline as durable medical-device EPS. It should test whether the product reaches recurring adoption, channel pull and margin:

```text
medical device export / reimbursement attention
→ export sell-through or payer/hospital adoption
→ channel inventory and reorder cadence
→ customer mix, consumables or service economics
→ gross margin and revision bridge
→ rerating
```

A device shipment is the first heartbeat. Green should pay for a pulse: repeat orders, reimbursement adoption, channel discipline and margin that keeps beating through revisions.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C25_336570_WONTECH_20230329_AESTHETIC_DEVICE_EXPORT_STAGE2 | 336570 | positive_aesthetic_device_export_stage2_success_with_later_4b | 2023-03-29 | 6340 | 12330 on 2023-09-19 | 6100 on 2023-04-25 | 28.86% | 86.59% | 94.48% | -3.79% | -31.95% |
| C25_099190_ISENS_20240111_CGM_REIMBURSEMENT_FALSE_GREEN | 099190 | diagnostic_cgm_reimbursement_false_green_counterexample | 2024-01-11 | 30050 | 30400 on 2024-01-12 | 17620 on 2024-05-31 | 1.16% | 1.16% | 1.16% | -41.36% | -42.04% |
| C25_100120_VIEWORKS_20230620_IMAGING_EXPORT_MARGIN_4B | 100120 | medical_imaging_export_margin_price_premium_counterexample | 2023-06-20 | 36900 | 37300 on 2023-06-21 | 26050 on 2023-12-07 | 1.08% | 1.08% | 1.08% | -29.4% | -30.16% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Medical-device export can be a valid Stage2 route when export sell-through, distributor/channel reorder and margin leverage appear before the valuation has fully capitalized the growth.
- 336570 is the positive anchor. The March 2023 aesthetic-device export route produced a large MFE with controlled early MAE, then later required 4B discipline after the export-growth story became widely priced.

### Stage3 / Green
- C25 Green should require repeat export sell-through, reimbursement or payer/hospital adoption, channel inventory quality, customer mix, gross margin and revision confirmation.
- 099190 is the false-Green guard. CGM/reimbursement attention had a plausible theme, but the forward path shows that adoption pace, payer conversion, sensor margin and revisions had not carried the valuation.
- 100120 is the medical-imaging/export version of the same failure: order and hospital capex visibility did not refresh fast enough after a local premium.

### 4B
- 100120 fills a local 4B pocket. The medical-imaging export margin story had little forward upside from the June 2023 premium and then rolled over as order and margin evidence faded.
- 336570 also moved from valid Stage2 into 4B watch once the stock paid upfront for export-channel growth.

### 4C
- No hard regulatory rejection or reimbursement cancellation is asserted.
- The C25 break mode is adoption/reorder disappointment: the product remains real, but reimbursement conversion, channel inventory, export reorder, customer mix, gross margin and revisions do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C25_099190_ISENS_20240111_CGM_REIMBURSEMENT_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 27,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C25_100120_VIEWORKS_20230620_IMAGING_EXPORT_MARGIN_4B": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 25,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C25_336570_WONTECH_20230329_AESTHETIC_DEVICE_EXPORT_STAGE2": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 53,
    "valuation_rerating_runway": 8,
    "visibility_quality": 11
  }
}
```

## 7. Current calibrated profile stress test

Suggested C25 guard:
```text
if medical_device_export_attention and sellthrough_reorder_margin_bridge_visible:
    allow_stage2_actionable = true

if reimbursement_or_device_price_premium and no payer_adoption_channel_inventory_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and adoption_or_reorder_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 099190 / 2024-01-11: CGM/reimbursement can be over-promoted if the model treats reimbursement attention as adoption, sensor margin and revision proof.
- 100120 / 2023-06-20: medical imaging/export price premium can become price-only when order, customer mix, hospital capex and margin evidence do not refresh.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -3.79, "MAE_30D_pct": -3.79, "MAE_90D_pct": -3.79, "MFE_180D_pct": 94.48, "MFE_30D_pct": 28.86, "MFE_90D_pct": 86.59, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_336570_WONTECH_20230329_AESTHETIC_DEVICE_EXPORT_STAGE2", "case_role": "positive_aesthetic_device_export_stage2_success_with_later_4b", "company_name": "원텍", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidate is 2022-06-30 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when aesthetic medical-device export growth, distributor/channel reorder and margin leverage appeared before the rerating was fully capitalized. Green still requires country-by-country export sell-through, reorder cadence, consumables/service mix, reimbursement or channel economics, margin and revision bridge; after the September 2023 premium the same evidence needed local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -31.95, "entry_date": "2023-03-29", "entry_price": 6340, "evidence_family": "aesthetic_energy_device_export_channel_reorder_margin_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "AESTHETIC_DIAGNOSTIC_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_HEALTHCARE_BIO_MEDICAL", "low_date_180d": "2023-04-25", "low_price_180d": 6100, "peak_date": "2023-09-19", "peak_price": 12330, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/336/336570.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 10, "total": 53, "valuation_rerating_runway": 8, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C25_336570_WONTECH_20230329_AESTHETIC_DEVICE_EXPORT_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_device_export_or_reimbursement_attention", "channel_reorder_or_hospital_payer_adoption_signal", "gross_margin_or_revision_bridge_visibility"], "stage3_evidence_fields": ["repeat_export_sellthrough_or_reimbursement_adoption_required", "channel_inventory_or_hospital_capex_cycle_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["medical_device_export_reimbursement_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["adoption_or_reimbursement_conversion_gap", "channel_inventory_or_export_order_disappointment", "gross_margin_revision_bridge_failure"], "symbol": "336570", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336570/2023.csv", "trigger_date": "2023-03-29", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -41.36, "MAE_30D_pct": -31.61, "MAE_90D_pct": -41.36, "MFE_180D_pct": 1.16, "MFE_30D_pct": 1.16, "MFE_90D_pct": 1.16, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_099190_ISENS_20240111_CGM_REIMBURSEMENT_FALSE_GREEN", "case_role": "diagnostic_cgm_reimbursement_false_green_counterexample", "company_name": "아이센스", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 2015-10-02, 2023-03-14 and 2023-04-10, outside selected test window", "current_profile_error": true, "current_profile_verdict": "CGM/diagnostic reimbursement or launch attention should stay Yellow when adoption speed, payer/reimbursement conversion, channel inventory, sensor gross margin and revision evidence do not keep improving after the price run. Price confirmation alone was a false-Green risk.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -42.04, "entry_date": "2024-01-11", "entry_price": 30050, "evidence_family": "cgm_diagnostic_reimbursement_price_premium_without_adoption_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "AESTHETIC_DIAGNOSTIC_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_HEALTHCARE_BIO_MEDICAL", "low_date_180d": "2024-05-31", "low_price_180d": 17620, "peak_date": "2024-01-12", "peak_price": 30400, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/099/099190.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 5, "total": 27, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C25_099190_ISENS_20240111_CGM_REIMBURSEMENT_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_device_export_or_reimbursement_attention", "channel_reorder_or_hospital_payer_adoption_signal", "gross_margin_or_revision_bridge_visibility"], "stage3_evidence_fields": ["repeat_export_sellthrough_or_reimbursement_adoption_required", "channel_inventory_or_hospital_capex_cycle_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["medical_device_export_reimbursement_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["adoption_or_reimbursement_conversion_gap", "channel_inventory_or_export_order_disappointment", "gross_margin_revision_bridge_failure"], "symbol": "099190", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv", "trigger_date": "2024-01-11", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -29.4, "MAE_30D_pct": -10.16, "MAE_90D_pct": -17.89, "MFE_180D_pct": 1.08, "MFE_30D_pct": 1.08, "MFE_90D_pct": 1.08, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_100120_VIEWORKS_20230620_IMAGING_EXPORT_MARGIN_4B", "case_role": "medical_imaging_export_margin_price_premium_counterexample", "company_name": "뷰웍스", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidate is 2011-08-08 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Medical imaging/export price premium should route to local 4B or counterexample unless order backlog, export shipment quality, customer mix, reimbursement or hospital capex cycle, gross margin and revision evidence remain visible after the stock has already priced recovery.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -30.16, "entry_date": "2023-06-20", "entry_price": 36900, "evidence_family": "medical_imaging_detector_export_price_premium_without_order_reimbursement_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "AESTHETIC_DIAGNOSTIC_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_HEALTHCARE_BIO_MEDICAL", "low_date_180d": "2023-12-07", "low_price_180d": 26050, "peak_date": "2023-06-21", "peak_price": 37300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/100/100120.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 4, "total": 25, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C25_100120_VIEWORKS_20230620_IMAGING_EXPORT_MARGIN_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_device_export_or_reimbursement_attention", "channel_reorder_or_hospital_payer_adoption_signal", "gross_margin_or_revision_bridge_visibility"], "stage3_evidence_fields": ["repeat_export_sellthrough_or_reimbursement_adoption_required", "channel_inventory_or_hospital_capex_cycle_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["medical_device_export_reimbursement_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["adoption_or_reimbursement_conversion_gap", "channel_inventory_or_export_order_disappointment", "gross_margin_revision_bridge_failure"], "symbol": "100120", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100120/2023.csv", "trigger_date": "2023-06-20", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "AESTHETIC_DIAGNOSTIC_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L7_HEALTHCARE_BIO_MEDICAL",
  "loop_contribution_label": "medical_device_export_reimbursement_new_symbols_aesthetic_diagnostic_imaging_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R7",
  "shadow_rule_candidate": "C25 medical-device export/reimbursement rows should allow Stage2 when export sell-through, channel reorder or reimbursement adoption visibly connects to gross-margin and revision leverage, but Stage3 Green requires repeat export sell-through, payer/hospital adoption, channel inventory, customer mix, gross margin and revision bridge; medical-device price premium without adoption or margin proof should route to local 4B or counterexample.",
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
3. Add C25-specific medical-device export / reimbursement adoption / channel inventory / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C25_STAGE2_ALLOWED_ON_EXPORT_SELLTHROUGH_REORDER_MARGIN_BRIDGE
- C25_GREEN_REQUIRES_REIMBURSEMENT_ADOPTION_CHANNEL_INVENTORY_CUSTOMER_MIX_MARGIN_REVISION
- C25_MEDICAL_DEVICE_PRICE_PREMIUM_LOCAL_4B
- C25_REIMBURSEMENT_OR_EXPORT_WITHOUT_ADOPTION_MARGIN_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R7/L7_HEALTHCARE_BIO_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.

