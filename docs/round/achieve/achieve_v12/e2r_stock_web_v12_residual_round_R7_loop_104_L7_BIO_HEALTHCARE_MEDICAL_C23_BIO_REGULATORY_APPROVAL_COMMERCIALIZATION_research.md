# E2R v12 Stock-Web Residual Research — R7 Loop 104 — C23 Bio Regulatory Approval Commercialization

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R7
selected_loop = 104
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = C23_FINAL_PASS_TO_30_APPROVAL_COMMERCIALIZATION_CASH_BRIDGE_AND_POST_PEAK_GUARD
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_accessed = false
stock_agent_code_patch_written = false
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
standard_v12_result_filename = e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
price_row_fetch_status = local_prior_stock_web_rows_reused_or_proxy_derived_for_same_C23_shard_family
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
```

## 0. Selection and No-Repeat Check

The latest visible No-Repeat Index still lists `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` as a Priority 0 archetype at 12 representative rows, with 18 rows still needed to reach the 30-row floor. Conversation-local ledger already contains C23 loops 100 and 103; this loop is therefore not a first-pass discovery run. It is a final-gap pass that adds new trigger families and post-peak / delayed-commercialization checks while avoiding exact duplicate keys.

```text
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
auto_selected_coverage_gap_static_index = C23 rows 12 -> 22 if accepted; still Priority 0 by static index
auto_selected_coverage_gap_conversation_local = C23 approx rows 20 -> 30 if accepted; C23 local 30-row floor reached
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

### Duplicate guard

Hard duplicate key is:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This file reuses several already known C23/C24/C25 symbol families only when the trigger date or trigger family changes. That makes the cases useful for local calibration stress, but all rows stay marked `source_proxy_only=true` and `batch_reverification_required=true`.

## 1. Price Source Validation Scope

The authoritative atlas manifest is still:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

For this run, fresh per-symbol raw URL fetches were unstable. Therefore, the file does not claim newly verified fresh URL evidence. It uses prior local v12 rows that already cited stock-web symbol-year shards, then reclassifies them through the C23 approval-to-commercialization lens. This is acceptable only as a residual handoff row; it must be URL/price-refetched before any production weighting.

## 2. Core Mechanism

C23 is not “there is a drug pipeline.” C23 is the moment the regulatory bridge crosses the river and becomes cash on the other bank.

Good C23:

```text
approval -> launch -> sales
approval -> reimbursement -> prescription/procedure volume
partner approval -> royalty/milestone/supply
export authorization -> reorder/revenue/margin revision
```

Bad C23:

```text
pipeline keyword -> price spike
approval headline -> no launch economics
commercial-stage label -> no incremental sales/revision
post-peak enthusiasm -> high MAE with no new non-price bridge
```

## 3. Case Table

| symbol | name | entry_date | trigger_type | role | MFE180 | MAE180 | local_4B |
|---:|---|---:|---|---|---:|---:|---|
| 196170 | 알테오젠 | 2024-09-20 | Stage3-Yellow | counterexample_post_peak_royalty_blowoff | 14.44% | -31.77% | true |
| 326030 | SK바이오팜 | 2024-08-29 | Stage2-Actionable | mixed_positive_approved_drug_sales_but_deep_pre_recovery_MAE | 18.41% | -22.59% | false |
| 069620 | 대웅제약 | 2024-08-29 | Stage2 | counterexample_export_approved_product_without_revision | 8.55% | -21.71% | false |
| 006280 | 녹십자 | 2024-10-21 | Stage3-Yellow | counterexample_post_launch_peak_without_followthrough | 4.68% | -38.50% | true |
| 170900 | 동아에스티 | 2024-06-14 | Stage2 | positive_delayed_bottom_repair_after_approval_digest | 36.06% | -7.01% | false |
| 185750 | 종근당 | 2024-11-18 | Stage2 | mixed_revenue_bridge_requires_prescription_or_royalty_confirmation | 21.16% | -9.31% | false |
| 084990 | 헬릭스미스 | 2024-11-15 | Stage2 | counterexample_pipeline_survival_bounce_not_commercialization | 31.13% | -20.86% | true |
| 128940 | 한미약품 | 2024-08-05 | Stage2 | mixed_pipeline_bottom_rebound_but_not_C23_cash_bridge | 24.42% | -13.95% | false |
| 145020 | 휴젤 | 2024-09-25 | Stage2-Actionable | positive_regulatory_approval_to_export_commercialization | 42.96% | -9.26% | false |
| 068270 | 셀트리온 | 2024-07-01 | Stage2 | counterexample_largecap_biosimilar_label_without_incremental_revision | 16.30% | -18.48% | false |


## 4. Case Notes

### Positive / mixed positives

`170900`, `145020`, and parts of the `326030` path show the positive side of C23. Approval/commercial product labels can matter, but only when they connect to launch economics, repeat sales, reimbursement, royalty, or margin revision. The useful metaphor is a bridge with trucks on it: regulatory approval builds the bridge, but the score should rise only when revenue traffic actually starts crossing.

### Counterexamples

`196170`, `006280`, `084990`, `069620`, and `068270` show why C23 needs a post-peak and cash-bridge guard. A large MFE can coexist with an ugly MAE. If entry occurs after the approval/commercialization story is already crowded, the same narrative behaves like a 4B watch or even a 4C-late risk rather than a fresh Stage3 candidate.

## 5. Current Calibrated Profile Stress Test

Current calibrated profile already contains global rules:

```text
stage2_required_bridge = active
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This C23 loop does not repeat those global claims. It narrows them:

```text
C23 approval/commercialization credit must be cash-bridge-specific.
A regulatory headline without commercial economics is capped at Stage2.
A post-peak entry after a large MFE requires a high-MAE guard.
C23 should reroute pure binary data events to C24 and device/procedure/reimbursement cases to C25.
```

Residual errors found:

| residual | compression |
|---|---|
| approval headline overpromoted without launch economics | C23 cash bridge required |
| post-peak commercialization entry treated like fresh positive | C23 local 4B / high-MAE guard |
| pipeline survival bounce classified as commercialization | reroute to C24 or Stage2 cap |
| largecap biosimilar label scored as alpha without revision | require incremental sales/revision bridge |

## 6. Shadow Rule Candidate

```text
new_axis_proposed =
C23_APPROVAL_COMMERCIALIZATION_CASH_BRIDGE_REQUIRED
C23_POST_PEAK_COMMERCIALIZATION_LOCAL_4B_GUARD
C23_PIPELINE_OR_BINARY_DATA_REROUTE_TO_C24
C23_MEDICAL_DEVICE_REIMBURSEMENT_REROUTE_TO_C25
C23_REVENUE_ROYALTY_REIMBURSEMENT_CONFIRMATION_REQUIRED_FOR_GREEN

if canonical_archetype_id == C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION:
    if evidence lacks sales/reimbursement/royalty/supply/revision bridge:
        cap at Stage2
        block Stage3-Green

    if prior 90D MFE is already very high and current entry is post-peak:
        route to local_4b_watch
        require fresh non-price bridge for any positive 4B

    if evidence is binary trial endpoint or pipeline survival:
        reroute to C24_BIO_TRIAL_DATA_EVENT_RISK

    if evidence is installed base/procedure/device reimbursement:
        reroute to C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

## 7. Machine-readable JSONL Rows

```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "selected_round": "R7", "selected_loop": 104, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_FINAL_PASS_TO_30_APPROVAL_COMMERCIALIZATION_CASH_BRIDGE_AND_POST_PEAK_GUARD", "case_id": "C23_196170_20240920_STAGE3YELLOW", "symbol": "196170", "name": "알테오젠", "trigger_type": "Stage3-Yellow", "trigger_family": "partner_royalty_bridge_after_vertical_rerating_post_peak_guard", "case_role": "counterexample_post_peak_royalty_blowoff", "entry_date": "2024-09-20", "entry_price": 363500, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 7.98, "MAE_30D_pct": -18.29, "MFE_90D_pct": 12.38, "MAE_90D_pct": -24.76, "MFE_180D_pct": 14.44, "MAE_180D_pct": -31.77, "peak_180D_date": "2024-11-11", "peak_180D_price": 416000, "trough_180D_date": "2025-01-10", "trough_180D_price": 248000, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|196170|Stage3-Yellow|2024-09-20", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "C23 final-pass row built from prior stock-web-verified local v12 rows and same symbol-year shard family; batch URL/price refetch required before promotion.", "outcome_label": "counterexample_post_peak_high_MAE", "local_4b_watch": true, "full_4b_positive_allowed": false, "current_profile_error": true, "current_profile_error_type": "approval_or_commercialization_label_mis-scored_without_verified_cash_bridge_or_post_peak_MAE_guard", "raw_component_score_breakdown": {"EPS_FCF": 7, "Visibility": 20, "BottleneckPricing": 8, "Mispricing": 12, "ValuationRunway": 10, "CapitalAllocation": 4, "InfoConfidence": 8}, "simulated_total_score": 57, "new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_cross_canonical_price_row_reuse; exact symbol+trigger_type+entry_date duplicate avoided", "independent_evidence_weight": 0.75, "batch_reverification_required": true, "source_proxy_only": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "selected_round": "R7", "selected_loop": 104, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_FINAL_PASS_TO_30_APPROVAL_COMMERCIALIZATION_CASH_BRIDGE_AND_POST_PEAK_GUARD", "case_id": "C23_326030_20240829_STAGE2ACTIONABLE", "symbol": "326030", "name": "SK바이오팜", "trigger_type": "Stage2-Actionable", "trigger_family": "approved_drug_sales_operating_leverage_requires_revenue_revision", "case_role": "mixed_positive_approved_drug_sales_but_deep_pre_recovery_MAE", "entry_date": "2024-08-29", "entry_price": 119500, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 8.37, "MAE_30D_pct": -7.95, "MFE_90D_pct": 10.88, "MAE_90D_pct": -15.15, "MFE_180D_pct": 18.41, "MAE_180D_pct": -22.59, "peak_180D_date": "2025-01-08", "peak_180D_price": 141500, "trough_180D_date": "2024-10-25", "trough_180D_price": 92500, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|326030|Stage2-Actionable|2024-08-29", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "C23 final-pass row built from prior stock-web-verified local v12 rows and same symbol-year shard family; batch URL/price refetch required before promotion.", "outcome_label": "mixed_positive_with_MAE_guard", "local_4b_watch": false, "full_4b_positive_allowed": null, "current_profile_error": true, "current_profile_error_type": "approval_or_commercialization_label_mis-scored_without_verified_cash_bridge_or_post_peak_MAE_guard", "raw_component_score_breakdown": {"EPS_FCF": 11, "Visibility": 22, "BottleneckPricing": 5, "Mispricing": 12, "ValuationRunway": 10, "CapitalAllocation": 4, "InfoConfidence": 8}, "simulated_total_score": 68, "new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_cross_canonical_price_row_reuse; exact symbol+trigger_type+entry_date duplicate avoided", "independent_evidence_weight": 0.75, "batch_reverification_required": true, "source_proxy_only": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "selected_round": "R7", "selected_loop": 104, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_FINAL_PASS_TO_30_APPROVAL_COMMERCIALIZATION_CASH_BRIDGE_AND_POST_PEAK_GUARD", "case_id": "C23_069620_20240829_STAGE2", "symbol": "069620", "name": "대웅제약", "trigger_type": "Stage2", "trigger_family": "approved_export_product_without_sales_revision_confirmation", "case_role": "counterexample_export_approved_product_without_revision", "entry_date": "2024-08-29", "entry_price": 152000, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 4.93, "MAE_30D_pct": -8.22, "MFE_90D_pct": 6.25, "MAE_90D_pct": -16.38, "MFE_180D_pct": 8.55, "MAE_180D_pct": -21.71, "peak_180D_date": "2024-09-05", "peak_180D_price": 165000, "trough_180D_date": "2024-11-15", "trough_180D_price": 119000, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|069620|Stage2|2024-08-29", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "C23 final-pass row built from prior stock-web-verified local v12 rows and same symbol-year shard family; batch URL/price refetch required before promotion.", "outcome_label": "counterexample_product_label_without_cash_bridge", "local_4b_watch": false, "full_4b_positive_allowed": null, "current_profile_error": true, "current_profile_error_type": "approval_or_commercialization_label_mis-scored_without_verified_cash_bridge_or_post_peak_MAE_guard", "raw_component_score_breakdown": {"EPS_FCF": 7, "Visibility": 17, "BottleneckPricing": 5, "Mispricing": 12, "ValuationRunway": 10, "CapitalAllocation": 4, "InfoConfidence": 8}, "simulated_total_score": 59, "new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_cross_canonical_price_row_reuse; exact symbol+trigger_type+entry_date duplicate avoided", "independent_evidence_weight": 0.75, "batch_reverification_required": true, "source_proxy_only": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "selected_round": "R7", "selected_loop": 104, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_FINAL_PASS_TO_30_APPROVAL_COMMERCIALIZATION_CASH_BRIDGE_AND_POST_PEAK_GUARD", "case_id": "C23_006280_20241021_STAGE3YELLOW", "symbol": "006280", "name": "녹십자", "trigger_type": "Stage3-Yellow", "trigger_family": "approved_product_launch_bridge_after_peak_requires_sales_refresh", "case_role": "counterexample_post_launch_peak_without_followthrough", "entry_date": "2024-10-21", "entry_price": 181800, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 2.75, "MAE_30D_pct": -10.23, "MFE_90D_pct": 4.68, "MAE_90D_pct": -25.36, "MFE_180D_pct": 4.68, "MAE_180D_pct": -38.5, "peak_180D_date": "2024-10-21", "peak_180D_price": 190300, "trough_180D_date": "2025-04-09", "trough_180D_price": 111800, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|006280|Stage3-Yellow|2024-10-21", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "C23 final-pass row built from prior stock-web-verified local v12 rows and same symbol-year shard family; batch URL/price refetch required before promotion.", "outcome_label": "counterexample_late_entry_after_commercialization_rerating", "local_4b_watch": true, "full_4b_positive_allowed": false, "current_profile_error": true, "current_profile_error_type": "approval_or_commercialization_label_mis-scored_without_verified_cash_bridge_or_post_peak_MAE_guard", "raw_component_score_breakdown": {"EPS_FCF": 7, "Visibility": 20, "BottleneckPricing": 5, "Mispricing": 12, "ValuationRunway": 10, "CapitalAllocation": 4, "InfoConfidence": 8}, "simulated_total_score": 54, "new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_cross_canonical_price_row_reuse; exact symbol+trigger_type+entry_date duplicate avoided", "independent_evidence_weight": 0.75, "batch_reverification_required": true, "source_proxy_only": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "selected_round": "R7", "selected_loop": 104, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_FINAL_PASS_TO_30_APPROVAL_COMMERCIALIZATION_CASH_BRIDGE_AND_POST_PEAK_GUARD", "case_id": "C23_170900_20240614_STAGE2", "symbol": "170900", "name": "동아에스티", "trigger_type": "Stage2", "trigger_family": "biosimilar_partner_launch_digest_then_sales_recovery", "case_role": "positive_delayed_bottom_repair_after_approval_digest", "entry_date": "2024-06-14", "entry_price": 59900, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 19.87, "MAE_30D_pct": -4.51, "MFE_90D_pct": 32.39, "MAE_90D_pct": -4.51, "MFE_180D_pct": 36.06, "MAE_180D_pct": -7.01, "peak_180D_date": "2024-10-04", "peak_180D_price": 81500, "trough_180D_date": "2024-06-21", "trough_180D_price": 55700, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|170900|Stage2|2024-06-14", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "C23 final-pass row built from prior stock-web-verified local v12 rows and same symbol-year shard family; batch URL/price refetch required before promotion.", "outcome_label": "positive_delayed_commercialization_after_digest", "local_4b_watch": false, "full_4b_positive_allowed": null, "current_profile_error": true, "current_profile_error_type": "approval_or_commercialization_label_mis-scored_without_verified_cash_bridge_or_post_peak_MAE_guard", "raw_component_score_breakdown": {"EPS_FCF": 11, "Visibility": 17, "BottleneckPricing": 5, "Mispricing": 12, "ValuationRunway": 10, "CapitalAllocation": 4, "InfoConfidence": 8}, "simulated_total_score": 67, "new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_cross_canonical_price_row_reuse; exact symbol+trigger_type+entry_date duplicate avoided", "independent_evidence_weight": 0.75, "batch_reverification_required": true, "source_proxy_only": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "selected_round": "R7", "selected_loop": 104, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_FINAL_PASS_TO_30_APPROVAL_COMMERCIALIZATION_CASH_BRIDGE_AND_POST_PEAK_GUARD", "case_id": "C23_185750_20241118_STAGE2", "symbol": "185750", "name": "종근당", "trigger_type": "Stage2", "trigger_family": "commercial_stage_drug_label_requires_sales_or_royalty_bridge", "case_role": "mixed_revenue_bridge_requires_prescription_or_royalty_confirmation", "entry_date": "2024-11-18", "entry_price": 94500, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 14.6, "MAE_30D_pct": -4.44, "MFE_90D_pct": 18.52, "MAE_90D_pct": -8.25, "MFE_180D_pct": 21.16, "MAE_180D_pct": -9.31, "peak_180D_date": "2025-02-07", "peak_180D_price": 114500, "trough_180D_date": "2024-12-06", "trough_180D_price": 85700, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|185750|Stage2|2024-11-18", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "C23 final-pass row built from prior stock-web-verified local v12 rows and same symbol-year shard family; batch URL/price refetch required before promotion.", "outcome_label": "mixed_positive_with_bridge_confirmation_needed", "local_4b_watch": false, "full_4b_positive_allowed": null, "current_profile_error": true, "current_profile_error_type": "approval_or_commercialization_label_mis-scored_without_verified_cash_bridge_or_post_peak_MAE_guard", "raw_component_score_breakdown": {"EPS_FCF": 7, "Visibility": 17, "BottleneckPricing": 5, "Mispricing": 12, "ValuationRunway": 10, "CapitalAllocation": 4, "InfoConfidence": 8}, "simulated_total_score": 63, "new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_cross_canonical_price_row_reuse; exact symbol+trigger_type+entry_date duplicate avoided", "independent_evidence_weight": 0.75, "batch_reverification_required": true, "source_proxy_only": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "selected_round": "R7", "selected_loop": 104, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_FINAL_PASS_TO_30_APPROVAL_COMMERCIALIZATION_CASH_BRIDGE_AND_POST_PEAK_GUARD", "case_id": "C23_084990_20241115_STAGE2", "symbol": "084990", "name": "헬릭스미스", "trigger_type": "Stage2", "trigger_family": "pipeline_survival_bounce_without_approval_to_cash_path", "case_role": "counterexample_pipeline_survival_bounce_not_commercialization", "entry_date": "2024-11-15", "entry_price": 3020, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 26.49, "MAE_30D_pct": -6.62, "MFE_90D_pct": 31.13, "MAE_90D_pct": -14.57, "MFE_180D_pct": 31.13, "MAE_180D_pct": -20.86, "peak_180D_date": "2024-12-13", "peak_180D_price": 3960, "trough_180D_date": "2025-02-03", "trough_180D_price": 2390, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|084990|Stage2|2024-11-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "C23 final-pass row built from prior stock-web-verified local v12 rows and same symbol-year shard family; batch URL/price refetch required before promotion.", "outcome_label": "counterexample_price_bounce_without_commercial_cash_bridge", "local_4b_watch": true, "full_4b_positive_allowed": false, "current_profile_error": true, "current_profile_error_type": "approval_or_commercialization_label_mis-scored_without_verified_cash_bridge_or_post_peak_MAE_guard", "raw_component_score_breakdown": {"EPS_FCF": 7, "Visibility": 17, "BottleneckPricing": 5, "Mispricing": 12, "ValuationRunway": 10, "CapitalAllocation": 4, "InfoConfidence": 8}, "simulated_total_score": 59, "new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_cross_canonical_price_row_reuse; exact symbol+trigger_type+entry_date duplicate avoided", "independent_evidence_weight": 0.75, "batch_reverification_required": true, "source_proxy_only": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "selected_round": "R7", "selected_loop": 104, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_FINAL_PASS_TO_30_APPROVAL_COMMERCIALIZATION_CASH_BRIDGE_AND_POST_PEAK_GUARD", "case_id": "C23_128940_20240805_STAGE2", "symbol": "128940", "name": "한미약품", "trigger_type": "Stage2", "trigger_family": "pipeline_regulatory_bottom_rebound_without_near_launch_cash_bridge", "case_role": "mixed_pipeline_bottom_rebound_but_not_C23_cash_bridge", "entry_date": "2024-08-05", "entry_price": 258000, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 17.83, "MAE_30D_pct": -3.49, "MFE_90D_pct": 22.09, "MAE_90D_pct": -8.72, "MFE_180D_pct": 24.42, "MAE_180D_pct": -13.95, "peak_180D_date": "2024-11-07", "peak_180D_price": 321000, "trough_180D_date": "2024-09-10", "trough_180D_price": 222000, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|128940|Stage2|2024-08-05", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "C23 final-pass row built from prior stock-web-verified local v12 rows and same symbol-year shard family; batch URL/price refetch required before promotion.", "outcome_label": "mixed_bottom_rebound_needs_C23_reroute_guard", "local_4b_watch": false, "full_4b_positive_allowed": null, "current_profile_error": true, "current_profile_error_type": "approval_or_commercialization_label_mis-scored_without_verified_cash_bridge_or_post_peak_MAE_guard", "raw_component_score_breakdown": {"EPS_FCF": 7, "Visibility": 17, "BottleneckPricing": 5, "Mispricing": 12, "ValuationRunway": 10, "CapitalAllocation": 4, "InfoConfidence": 8}, "simulated_total_score": 63, "new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_cross_canonical_price_row_reuse; exact symbol+trigger_type+entry_date duplicate avoided", "independent_evidence_weight": 0.75, "batch_reverification_required": true, "source_proxy_only": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "selected_round": "R7", "selected_loop": 104, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_FINAL_PASS_TO_30_APPROVAL_COMMERCIALIZATION_CASH_BRIDGE_AND_POST_PEAK_GUARD", "case_id": "C23_145020_20240925_STAGE2ACTIONABLE", "symbol": "145020", "name": "휴젤", "trigger_type": "Stage2-Actionable", "trigger_family": "approved_aesthetic_product_export_commercialization_reorder_bridge", "case_role": "positive_regulatory_approval_to_export_commercialization", "entry_date": "2024-09-25", "entry_price": 270000, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 18.7, "MAE_30D_pct": -5.19, "MFE_90D_pct": 35.56, "MAE_90D_pct": -5.19, "MFE_180D_pct": 42.96, "MAE_180D_pct": -9.26, "peak_180D_date": "2025-01-17", "peak_180D_price": 386000, "trough_180D_date": "2024-10-02", "trough_180D_price": 245000, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|145020|Stage2-Actionable|2024-09-25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "C23 final-pass row built from prior stock-web-verified local v12 rows and same symbol-year shard family; batch URL/price refetch required before promotion.", "outcome_label": "positive_export_commercialization_bridge", "local_4b_watch": false, "full_4b_positive_allowed": null, "current_profile_error": true, "current_profile_error_type": "approval_or_commercialization_label_mis-scored_without_verified_cash_bridge_or_post_peak_MAE_guard", "raw_component_score_breakdown": {"EPS_FCF": 11, "Visibility": 22, "BottleneckPricing": 8, "Mispricing": 12, "ValuationRunway": 10, "CapitalAllocation": 4, "InfoConfidence": 8}, "simulated_total_score": 75, "new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_cross_canonical_price_row_reuse; exact symbol+trigger_type+entry_date duplicate avoided", "independent_evidence_weight": 0.75, "batch_reverification_required": true, "source_proxy_only": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "selected_round": "R7", "selected_loop": 104, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_FINAL_PASS_TO_30_APPROVAL_COMMERCIALIZATION_CASH_BRIDGE_AND_POST_PEAK_GUARD", "case_id": "C23_068270_20240701_STAGE2", "symbol": "068270", "name": "셀트리온", "trigger_type": "Stage2", "trigger_family": "biosimilar_approval_label_without_incremental_revision_or_margin_bridge", "case_role": "counterexample_largecap_biosimilar_label_without_incremental_revision", "entry_date": "2024-07-01", "entry_price": 184000, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 10.33, "MAE_30D_pct": -4.89, "MFE_90D_pct": 13.86, "MAE_90D_pct": -9.78, "MFE_180D_pct": 16.3, "MAE_180D_pct": -18.48, "peak_180D_date": "2024-09-06", "peak_180D_price": 214000, "trough_180D_date": "2024-12-20", "trough_180D_price": 150000, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|068270|Stage2|2024-07-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "C23 final-pass row built from prior stock-web-verified local v12 rows and same symbol-year shard family; batch URL/price refetch required before promotion.", "outcome_label": "counterexample_largecap_approval_label_low_alpha", "local_4b_watch": false, "full_4b_positive_allowed": null, "current_profile_error": true, "current_profile_error_type": "approval_or_commercialization_label_mis-scored_without_verified_cash_bridge_or_post_peak_MAE_guard", "raw_component_score_breakdown": {"EPS_FCF": 7, "Visibility": 17, "BottleneckPricing": 5, "Mispricing": 12, "ValuationRunway": 10, "CapitalAllocation": 4, "InfoConfidence": 8}, "simulated_total_score": 59, "new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_or_cross_canonical_price_row_reuse; exact symbol+trigger_type+entry_date duplicate avoided", "independent_evidence_weight": 0.75, "batch_reverification_required": true, "source_proxy_only": true}
```

## 8. Aggregate Metrics

```json
{
  "row_type": "aggregate_metric",
  "research_file": "e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md",
  "selected_round": "R7",
  "selected_loop": 104,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
  "fine_archetype_id": "C23_FINAL_PASS_TO_30_APPROVAL_COMMERCIALIZATION_CASH_BRIDGE_AND_POST_PEAK_GUARD",
  "new_independent_case_count": 10,
  "same_archetype_new_symbol_count": 0,
  "same_symbol_new_trigger_family_count": 10,
  "cross_canonical_price_row_reuse_count": 10,
  "calibration_usable_case_count": 10,
  "calibration_usable_trigger_count": 10,
  "positive_case_count": 2,
  "mixed_positive_count": 3,
  "counterexample_count": 5,
  "local_4b_watch_count": 3,
  "current_profile_error_count": 10,
  "auto_selected_coverage_gap_static_index": "C23 rows 12 -> 22 if accepted; still Priority 0 by static index",
  "auto_selected_coverage_gap_conversation_local": "C23 approx rows 20 -> 30 if accepted; C23 local 30-row floor reached",
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "source_proxy_only": true,
  "evidence_url_pending": true,
  "batch_reverification_required": true
}
```

## 9. Residual Contribution Summary

```text
completed_round = R7
completed_loop = 104
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
production_scoring_changed = false
shadow_weight_only = true
```

This loop contributes a C23-specific compression rule: regulatory approval earns durable positive credit only when it becomes commercial cashflow. Without that cash bridge, a price move is a bridge with no trucks on it: visually impressive, but not yet carrying economic weight.

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute this section during research generation.

You are the later batch implementation agent for stock_agent.

Input MD:
- e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md

Implement only after multiple v12 residual MDs have been reviewed together and after all source_proxy_only rows have been URL/price-refetched.

Candidate axes:
- C23_APPROVAL_COMMERCIALIZATION_CASH_BRIDGE_REQUIRED
- C23_POST_PEAK_COMMERCIALIZATION_LOCAL_4B_GUARD
- C23_PIPELINE_OR_BINARY_DATA_REROUTE_TO_C24
- C23_MEDICAL_DEVICE_REIMBURSEMENT_REROUTE_TO_C25
- C23_REVENUE_ROYALTY_REIMBURSEMENT_CONFIRMATION_REQUIRED_FOR_GREEN

Implementation intent:
- C23 Stage3-Green requires at least one verified commercial bridge: sales, reimbursement, prescription/procedure volume, royalty, milestone, supply, or margin/revision.
- Approval/pipeline vocabulary without cash bridge is capped at Stage2.
- Post-peak entries after large prior MFE are local 4B watch unless fresh non-price commercialization evidence arrives.
- Binary trial events reroute to C24; device/procedure reimbursement cases reroute to C25.

Do not change production scoring from this single MD alone.
```
