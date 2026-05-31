# E2R V12 No-Repeat Standalone Residual Research
## R7 / L7 / C25 — Medical device export·reimbursement / aesthetic-CGM-wearable pump 4B·4C guard

metadata:
```text
selected_round: R7
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_CGM_WEARABLE_PUMP_EXPORT_REIMBURSEMENT_4B_4C_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_4C_gap_fill|device_export_reimbursement_to_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_aesthetic_cgm_wearable_pump_4b_2023_2024_research.md
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

This run avoids those top-covered C25 symbols and adds 335890, 099190, and 294090.  
Each row uses a new `C25 + symbol + trigger_type + entry_date` hard key:
```text
C25 + 335890 + Stage2-Actionable + 2024-03-13
C25 + 099190 + Stage3-Yellow + 2023-07-19
C25 + 294090 + 4C-watch + 2023-10-10
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
335890 비올: selected 2024 forward window clean; corporate-action candidate is 2020-11-26, outside selected trigger window.
099190 아이센스: selected post-2023-04-10 forward window clean; corporate-action candidates 2023-03-14 and 2023-04-10 are before selected trigger window.
294090 이오플로우: selected post-2022 forward window; corporate-action candidates are 2022 dates and outside selected trigger window; event halt/trading-gap caveat retained.
```

## 3. Research thesis

C25 should separate medical-device export/reimbursement evidence that converts into repeat revenue from device optionality that is already capitalized:

```text
device export / reimbursement / launch / M&A optionality
→ distributor sell-through or prescription adoption
→ channel reorder or repeat sensor/consumable usage
→ regulatory/reimbursement gate durability
→ ASP/mix and margin revision
→ Stage2/Green or local 4B/4C-watch
```

A device approval or reimbursement headline opens the hospital door. Stage2 can buy it when physicians, distributors and patients keep pulling product through the door. Green should require reorder, repeat usage and margin revision, not just a louder headline.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C25_335890_VIOL_20240313_AESTHETIC_DEVICE_EXPORT_STAGE2 | 335890 | positive_aesthetic_device_export_stage2_success_with_later_4b_refresh | 2024-03-13 | 8480 | 12030 on 2024-04-01 | 6630 on 2024-12-09 | 41.86% | 41.86% | 41.86% | -21.82% | -44.89% |
| C25_099190_ISENS_20230719_CGM_REIMBURSEMENT_FALSE_GREEN | 099190 | CGM_reimbursement_launch_false_green_counterexample | 2023-07-19 | 33800 | 39700 on 2023-09-08 | 17910 on 2024-04-19 | 17.01% | 17.46% | 17.46% | -47.01% | -54.89% |
| C25_294090_EOFLOW_20231010_WEARABLE_PUMP_LEGAL_4C_WATCH | 294090 | wearable_insulin_pump_legal_transaction_break_4c_watch_counterexample | 2023-10-10 | 21700 | 22900 on 2023-10-10 | 3335 on 2024-02-01 | 5.53% | 5.53% | 5.53% | -84.63% | -85.44% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 335890 is the positive anchor. Aesthetic-device export and reorder evidence produced strong MFE before the premium later needed 4B refresh discipline.
- Stage2 is allowed only when device export or reimbursement salience maps to channel sell-through, adoption, reorder, ASP/mix and margin/revision visibility.

### Stage3 / Green
- C25 Green should require distributor reorder or prescription conversion, repeat usage/consumable pull-through, reimbursement durability and margin/revision confirmation.
- 099190 is the false-Green/Yellow guard: CGM launch/reimbursement excitement was real, but the price spike did not carry enough adoption-to-margin evidence to survive the forward path.

### 4B
- 099190 fills a reimbursement/launch price-premium pocket: good local MFE, but much larger forward drawdown when adoption and margin bridge lagged.
- 335890 also shows that valid Stage2 can become local 4B after the export-device rerating capitalizes the reorder story.

### 4C
- 294090 is classified as 4C-watch because legal/transaction/commercialization risk dominated the device optionality. The trading halt/gap is a calibration caveat, but the thesis break is still useful as a non-positive guard.
- Hard 4C should require durable legal injunction, transaction failure, regulatory block, liquidity break or commercialization failure. Absent that, use 4C-watch with event-gap caveat.

## 6. Raw component score breakdown

```json
{
  "C25_099190_ISENS_20230719_CGM_REIMBURSEMENT_FALSE_GREEN": {
    "ASP_mix_consumable_bridge": 3,
    "export_channel_visibility": 5,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "regulatory_or_reimbursement_gate": 8,
    "reorder_sellthrough_quality": 3,
    "total": 29,
    "valuation_rerating_runway": 1
  },
  "C25_294090_EOFLOW_20231010_WEARABLE_PUMP_LEGAL_4C_WATCH": {
    "ASP_mix_consumable_bridge": 1,
    "export_channel_visibility": 2,
    "information_confidence": 4,
    "legal_or_transaction_break_risk": 12,
    "margin_revision_bridge": 1,
    "market_mispricing": 2,
    "regulatory_or_reimbursement_gate": 3,
    "reorder_sellthrough_quality": 1,
    "total": 26,
    "valuation_rerating_runway": 0
  },
  "C25_335890_VIOL_20240313_AESTHETIC_DEVICE_EXPORT_STAGE2": {
    "ASP_mix_consumable_bridge": 7,
    "export_channel_visibility": 10,
    "information_confidence": 4,
    "margin_revision_bridge": 8,
    "market_mispricing": 9,
    "regulatory_or_reimbursement_gate": 5,
    "reorder_sellthrough_quality": 8,
    "total": 58,
    "valuation_rerating_runway": 7
  }
}
```

## 7. Current calibrated profile stress test

Suggested C25 guard:
```text
if medical_device_export_reimbursement and sellthrough_reorder_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if reimbursement_launch_price_premium and no adoption_reorder_consumable_margin_revision_bridge:
    block_stage3_green = true
    route_to_stage3_yellow_or_local_4B = true

if legal_transaction_break or commercialization_delay dominates:
    route_to_4C_watch = true
    add_event_halt_gap_caveat = true
```

Residual errors:
```text
current_profile_error_count = 2
- 099190 / 2023-07-19: CGM reimbursement/launch price confirmation can be over-promoted if price heat substitutes for adoption, reorder and margin proof.
- 294090 / 2023-10-10: wearable-pump optionality can become a hard event-risk trap when legal/transaction/commercialization break dominates.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -21.82, "MAE_30D_pct": -13.92, "MAE_90D_pct": -13.92, "MFE_180D_pct": 41.86, "MFE_30D_pct": 41.86, "MFE_90D_pct": 41.86, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_335890_VIOL_20240313_AESTHETIC_DEVICE_EXPORT_STAGE2", "case_role": "positive_aesthetic_device_export_stage2_success_with_later_4b_refresh", "company_name": "비올", "corporate_action_window_status": "selected 2024 forward window clean; corporate-action candidate is 2020-11-26 and outside selected trigger window; later latest-date/inactive inference does not contaminate selected window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when aesthetic-device export demand, distributor reorder cadence and margin leverage were visible before the rerating was fully capitalized. Green still requires export channel sell-through, recurring consumable or procedure-linked demand, distributor inventory quality, ASP/mix and margin/revision confirmation; after the April/May 2024 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.89, "entry_date": "2024-03-13", "entry_price": 8480, "evidence_family": "medical_aesthetic_device_export_channel_reorder_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "AESTHETIC_CGM_WEARABLE_PUMP_EXPORT_REIMBURSEMENT_4B_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2024-12-09", "low_price_180d": 6630, "peak_date": "2024-04-01", "peak_price": 12030, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/335/335890.json", "raw_component_score_breakdown": {"ASP_mix_consumable_bridge": 7, "export_channel_visibility": 10, "information_confidence": 4, "margin_revision_bridge": 8, "market_mispricing": 9, "regulatory_or_reimbursement_gate": 5, "reorder_sellthrough_quality": 8, "total": 58, "valuation_rerating_runway": 7}, "reuse_reason": null, "same_entry_group_id": "C25_335890_VIOL_20240313_AESTHETIC_DEVICE_EXPORT_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_device_export_channel_or_reimbursement_gate", "sellthrough_or_prescription_adoption_required", "ASP_mix_consumable_margin_revision_route"], "stage3_evidence_fields": ["channel_reorder_or_prescription_conversion_required", "regulatory_reimbursement_and_repeat_usage_required", "ASP_mix_margin_revision_bridge_required"], "stage4b_evidence_fields": ["medical_device_price_premium", "reimbursement_or_export_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["legal_transaction_or_reimbursement_break", "commercialization_delay_or_adoption_gap", "margin_revision_bridge_failure"], "symbol": "335890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/335/335890/2024.csv", "trigger_date": "2024-03-13", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -47.01, "MAE_30D_pct": -17.75, "MAE_90D_pct": -33.73, "MFE_180D_pct": 17.46, "MFE_30D_pct": 17.01, "MFE_90D_pct": 17.46, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_099190_ISENS_20230719_CGM_REIMBURSEMENT_FALSE_GREEN", "case_role": "CGM_reimbursement_launch_false_green_counterexample", "company_name": "아이센스", "corporate_action_window_status": "selected post-2023-04-10 forward window clean; 2023-03-14 and 2023-04-10 corporate-action candidates are before selected trigger window", "current_profile_error": true, "current_profile_verdict": "CGM launch/reimbursement price confirmation should remain Yellow or local 4B when price strength is not followed by adoption cadence, prescription/reimbursement conversion, channel reorder, sensor-utilization repeat demand and margin/revision evidence. The 2023 spike had good local MFE but a much larger forward MAE once adoption-to-margin proof lagged.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -54.89, "entry_date": "2023-07-19", "entry_price": 33800, "evidence_family": "CGM_launch_reimbursement_price_confirmation_without_adoption_reorder_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "AESTHETIC_CGM_WEARABLE_PUMP_EXPORT_REIMBURSEMENT_4B_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2024-04-19", "low_price_180d": 17910, "peak_date": "2023-09-08", "peak_price": 39700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/099/099190.json", "raw_component_score_breakdown": {"ASP_mix_consumable_bridge": 3, "export_channel_visibility": 5, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "regulatory_or_reimbursement_gate": 8, "reorder_sellthrough_quality": 3, "total": 29, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C25_099190_ISENS_20230719_CGM_REIMBURSEMENT_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_device_export_channel_or_reimbursement_gate", "sellthrough_or_prescription_adoption_required", "ASP_mix_consumable_margin_revision_route"], "stage3_evidence_fields": ["channel_reorder_or_prescription_conversion_required", "regulatory_reimbursement_and_repeat_usage_required", "ASP_mix_margin_revision_bridge_required"], "stage4b_evidence_fields": ["medical_device_price_premium", "reimbursement_or_export_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["legal_transaction_or_reimbursement_break", "commercialization_delay_or_adoption_gap", "margin_revision_bridge_failure"], "symbol": "099190", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/099/099190/2023.csv", "trigger_date": "2023-07-19", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -84.63, "MAE_30D_pct": -29.95, "MAE_90D_pct": -81.71, "MFE_180D_pct": 5.53, "MFE_30D_pct": 5.53, "MFE_90D_pct": 5.53, "calibration_caveat": "event_halt_gap_and_legal_transaction_break_caveat", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": false, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_294090_EOFLOW_20231010_WEARABLE_PUMP_LEGAL_4C_WATCH", "case_role": "wearable_insulin_pump_legal_transaction_break_4c_watch_counterexample", "company_name": "이오플로우", "corporate_action_window_status": "selected post-2022 corporate-action forward window; 2022 corporate-action candidates are outside selected trigger window; trading halt/gap around late-2023 is retained as event-risk caveat", "current_profile_error": true, "current_profile_verdict": "Wearable insulin-pump commercialization or M&A optionality should route to 4C-watch when legal injunction, transaction uncertainty, commercialization delay and financing/liquidity risk dominate. Price-only rebound or M&A memory should not substitute for regulatory clarity, shipment adoption, reimbursement conversion and margin/revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -85.44, "entry_date": "2023-10-10", "entry_price": 21700, "evidence_family": "wearable_insulin_pump_MA_legal_injunction_commercialization_break_without_revenue_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "AESTHETIC_CGM_WEARABLE_PUMP_EXPORT_REIMBURSEMENT_4B_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "low_date_180d": "2024-02-01", "low_price_180d": 3335, "peak_date": "2023-10-10", "peak_price": 22900, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/294/294090.json", "raw_component_score_breakdown": {"ASP_mix_consumable_bridge": 1, "export_channel_visibility": 2, "information_confidence": 4, "legal_or_transaction_break_risk": 12, "margin_revision_bridge": 1, "market_mispricing": 2, "regulatory_or_reimbursement_gate": 3, "reorder_sellthrough_quality": 1, "total": 26, "valuation_rerating_runway": 0}, "reuse_reason": null, "same_entry_group_id": "C25_294090_EOFLOW_20231010_WEARABLE_PUMP_LEGAL_4C_WATCH", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R7", "source_proxy_only": false, "stage2_evidence_fields": ["medical_device_export_channel_or_reimbursement_gate", "sellthrough_or_prescription_adoption_required", "ASP_mix_consumable_margin_revision_route"], "stage3_evidence_fields": ["channel_reorder_or_prescription_conversion_required", "regulatory_reimbursement_and_repeat_usage_required", "ASP_mix_margin_revision_bridge_required"], "stage4b_evidence_fields": ["medical_device_price_premium", "reimbursement_or_export_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["legal_transaction_or_reimbursement_break", "commercialization_delay_or_adoption_gap", "margin_revision_bridge_failure"], "symbol": "294090", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/294/294090/2023.csv", "trigger_date": "2023-10-10", "trigger_type": "4C-watch", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 2,
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "caveated_case_count": 1,
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "AESTHETIC_CGM_WEARABLE_PUMP_EXPORT_REIMBURSEMENT_4B_4C_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "loop_contribution_label": "medical_device_export_reimbursement_aesthetic_cgm_wearable_pump_new_symbols_4b_4c_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R7",
  "shadow_rule_candidate": "C25 rows should allow Stage2 when export/reimbursement evidence maps to sell-through, prescription adoption, channel reorder, repeat consumable usage and margin-revision bridge; price spikes around reimbursement/M&A/device optionality should route to Yellow/local 4B or 4C-watch when adoption, legal clarity or margin proof is missing.",
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
3. Treat 294090 as caveated for aggregate full-window calibration because legal/trading-halt gap needs separate event-risk handling.
4. Add C25-specific medical-device export / reimbursement / adoption / reorder / consumable / margin-revision / 4B-4C guard only as a shadow candidate until more rows exist.

Candidate rule:
- C25_STAGE2_ALLOWED_ON_SELLTHROUGH_REORDER_MARGIN_REVISION_BRIDGE
- C25_GREEN_REQUIRES_ADOPTION_REPEAT_USAGE_ASP_MIX_REVISION
- C25_REIMBURSEMENT_LAUNCH_PRICE_PREMIUM_LOCAL_4B
- C25_LEGAL_TRANSACTION_BREAK_ROUTES_TO_4C_WATCH_WITH_EVENT_GAP_CAVEAT

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.

