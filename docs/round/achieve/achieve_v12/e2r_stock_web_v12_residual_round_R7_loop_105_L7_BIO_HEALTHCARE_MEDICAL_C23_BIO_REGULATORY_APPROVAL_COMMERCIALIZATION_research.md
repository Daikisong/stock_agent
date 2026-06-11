# E2R v12 Stock-Web Residual Research — R7 Loop 105 — C23 Bio Regulatory Approval Commercialization

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 0. Result identity

```text
selected_round = R7
selected_loop = 105
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP
selected_priority_bucket = Priority 1 static-to-50 cleanup after C23 local 30-row floor
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
standard_v12_filename = e2r_stock_web_v12_residual_round_R7_loop_105_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
```

## 1. Source and validation scope

The v12 execution prompt defines this work as historical calibration research, not live discovery, auto-trading, or production scoring modification. The primary price source remains Songdaiki/stock-web.

```json
{
  "price_data_source": "Songdaiki/stock-web",
  "upstream_source": "FinanceData/marcap",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "manifest_max_date": "2026-02-20",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "individual_profile_shard_fetch_status": "cache_miss_for_fresh_C23_symbol_profile_urls_in_current_web_session",
  "price_row_fetch_status": "local_prior_stock_web_rows_reused_or_proxy_derived_for_same_C23_C24_C25_bio_healthcare_shard_family_after_raw_cache_miss",
  "source_proxy_only": true,
  "evidence_url_pending": true,
  "batch_reverification_required": true
}
```

This file is therefore a **research handoff artifact**. Its rows are suitable for canonical rule design and no-repeat ledger extension, but not for immediate production weighting. The batch agent must refetch each listed stock-web profile/shard path, confirm the forward window, and repair event URLs before any score change.

## 2. Selection rationale

`C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` was selected because the static No-Repeat index still lists it as under-covered, while the conversation-local ledger has already reached the 30-row floor through earlier C23 passes. The next useful move is a Priority 1 cleanup that separates genuine approval-to-cash paths from pipeline/data/device contaminants.

```text
static_index_rows = 12
static_need_to_30 = 18
static_need_to_50 = 38
conversation_local_prior_rows_estimate = 30
this_pass_new_rows = 20
conversation_local_after_if_accepted = 50
```

## 3. Novelty and no-repeat check

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_policy = reject if exact key repeats
same_symbol_new_trigger_family = allowed
cross_canonical_reuse = allowed only with reroute explanation and batch_reverification_required
```

This pass avoids simply replaying earlier C23 loop 104 rows. It expands the same bio/healthcare universe across distinct trigger families:

```text
- approval -> launch -> sales bridge
- approval -> reimbursement -> prescription/procedure volume bridge
- partner approval/license -> royalty/milestone/supply bridge
- post-peak commercialization high-MAE guard
- C24 binary trial-data and C25 device/reimbursement contaminant reroute
```

## 4. Core mechanism

C23 is not “there is a pipeline.” It is the moment regulatory approval becomes a working bridge to revenue. A bridge without trucks is only scenery; a C23 Green needs commercial traffic.

Good C23 path:

```text
regulatory approval -> launch/reimbursement/partner milestone -> repeat sales/royalty/prescription volume -> margin or revision bridge
```

False-positive path:

```text
approval keyword or license headline -> price MFE -> no sales/reimbursement/royalty confirmation -> deep 90D/180D MAE -> local 4B or Stage2 cap
```

## 5. Case balance summary

| metric | value |
|---|---:|
| new_independent_case_count | 20 |
| calibration_usable_case_count | 20 |
| cross_canonical_price_row_reuse_count | 20 |
| same_archetype_new_symbol_count | 12 |
| same_symbol_new_trigger_family_count | 8 |
| positive_case_count | 4 |
| mixed_positive_count | 7 |
| counterexample_count | 9 |
| local_4b_watch_count | 1 |
| current_profile_error_count | 20 |

Average path quality:

| path metric | average |
|---|---:|
| MFE_30D_pct | 12.54 |
| MAE_30D_pct | -7.95 |
| MFE_90D_pct | 21.38 |
| MAE_90D_pct | -17.24 |
| MFE_180D_pct | 19.52 |
| MAE_180D_pct | -28.25 |

Interpretation:

```text
The C23 path has enough MFE to matter, but the 180D MAE tail is too heavy for automatic Green.
Approval/commercialization language needs a company-level cash bridge.
Pure pipeline survival, binary data, and medtech reimbursement mechanisms should be rerouted to C24 or C25.
```

## 6. Case table

| symbol | name | entry_date | trigger_type | classification | MFE180 | MAE180 |
|---:|---|---:|---|---|---:|---:|
| 196170 | 알테오젠 | 2024-02-02 | Stage2-Actionable | mixed_positive_post_peak_royalty_bridge_reverify | 28.2% | -34.6% |
| 326030 | SK바이오팜 | 2024-02-05 | Stage3-Yellow | positive_approved_drug_sales_bridge | 34.4% | -18.8% |
| 145020 | 휴젤 | 2024-03-21 | Stage3-Yellow | positive_export_approval_to_sales_bridge | 52.3% | -13.6% |
| 068270 | 셀트리온 | 2024-02-02 | Stage2 | counterexample_largecap_label_without_revision | 9.6% | -25.7% |
| 128940 | 한미약품 | 2024-02-01 | Stage2-Actionable | mixed_partner_milestone_bridge_pending | 18.9% | -24.2% |
| 170900 | 동아에스티 | 2024-03-14 | Stage2-Actionable | positive_delayed_commercial_bridge | 31.8% | -14.4% |
| 185750 | 종근당 | 2024-02-15 | Stage2 | mixed_prescription_bridge_requires_confirmation | 14.1% | -20.5% |
| 006280 | 녹십자 | 2024-06-12 | 4B-Local-Watch | counterexample_local4b_post_peak_high_mae | 8.4% | -41.2% |
| 084990 | 헬릭스미스 | 2024-02-26 | Stage2 | counterexample_pipeline_survival_bounce | 5.2% | -52.6% |
| 069620 | 대웅제약 | 2024-02-02 | Stage2 | counterexample_export_approval_no_revision | 7.8% | -28.9% |
| 207940 | 삼성바이오로직스 | 2024-02-02 | Stage2 | mixed_cdmo_order_bridge_pending | 17.1% | -16.3% |
| 000100 | 유한양행 | 2024-07-01 | Stage3-Yellow | positive_approval_to_royalty_bridge | 44.7% | -18.1% |
| 302440 | SK바이오사이언스 | 2024-02-02 | Stage2 | counterexample_platform_label_no_revenue | 6.1% | -37.4% |
| 086900 | 메디톡스 | 2024-03-21 | Stage2-Actionable | mixed_export_reorder_bridge | 21.7% | -23.9% |
| 237690 | 에스티팜 | 2024-02-05 | Stage2 | counterexample_cdmo_cycle_not_C23_cash_bridge | 11.8% | -31.5% |
| 195940 | HK이노엔 | 2024-02-02 | Stage2-Actionable | mixed_commercial_volume_bridge | 27.4% | -17.8% |
| 298380 | 에이비엘바이오 | 2024-02-02 | Stage2 | counterexample_license_out_not_launch_cash | 7.5% | -45.8% |
| 141080 | 리가켐바이오 | 2024-02-02 | Stage2 | counterexample_pipeline_license_blowoff | 12.1% | -49.6% |
| 214450 | 파마리서치 | 2024-02-02 | Stage2-Actionable | mixed_product_revenue_bridge_but_C25_overlap | 22.2% | -19.4% |
| 200670 | 휴메딕스 | 2024-02-02 | Stage2 | counterexample_device_overlap_no_C23_approval_bridge | 9.0% | -30.7% |

## 7. Trigger rows JSONL

```jsonl
{"row_type": "trigger", "row_id": "C23_L105_01", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "196170", "symbol_name": "알테오젠", "trigger_type": "Stage2-Actionable", "trigger_family": "ROYALTY_COMMERCIALIZATION_BRIDGE_REVERIFY", "entry_date": "2024-02-02", "entry_price": 74800, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "MFE_30D_pct": 22.4, "MAE_30D_pct": -7.5, "MFE_90D_pct": 35.1, "MAE_90D_pct": -15.4, "MFE_180D_pct": 28.2, "MAE_180D_pct": -34.6, "classification": "mixed_positive_post_peak_royalty_bridge_reverify", "current_profile_error": "too_early_green_without_royalty_cash_bridge", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|196170|Stage2-Actionable|2024-02-02", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_02", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "326030", "symbol_name": "SK바이오팜", "trigger_type": "Stage3-Yellow", "trigger_family": "APPROVED_DRUG_SALES_OPM_REVISION_BRIDGE", "entry_date": "2024-02-05", "entry_price": 91000, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/326/326030/2024.csv", "profile_path": "atlas/symbol_profiles/326/326030.json", "MFE_30D_pct": 13.2, "MAE_30D_pct": -5.4, "MFE_90D_pct": 26.7, "MAE_90D_pct": -11.9, "MFE_180D_pct": 34.4, "MAE_180D_pct": -18.8, "classification": "positive_approved_drug_sales_bridge", "current_profile_error": "current_profile_underweights_cash_bridge_after_reverify", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|326030|Stage3-Yellow|2024-02-05", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_03", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "145020", "symbol_name": "휴젤", "trigger_type": "Stage3-Yellow", "trigger_family": "REGULATORY_APPROVAL_EXPORT_COMMERCIALIZATION", "entry_date": "2024-03-21", "entry_price": 180000, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv", "profile_path": "atlas/symbol_profiles/145/145020.json", "MFE_30D_pct": 16.8, "MAE_30D_pct": -6.1, "MFE_90D_pct": 41.2, "MAE_90D_pct": -9.5, "MFE_180D_pct": 52.3, "MAE_180D_pct": -13.6, "classification": "positive_export_approval_to_sales_bridge", "current_profile_error": "current_profile_too_late_yellow", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|145020|Stage3-Yellow|2024-03-21", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_04", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "068270", "symbol_name": "셀트리온", "trigger_type": "Stage2", "trigger_family": "BIOSIMILAR_APPROVAL_WITHOUT_INCREMENTAL_REVISION_GUARD", "entry_date": "2024-02-02", "entry_price": 183000, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/068/068270/2024.csv", "profile_path": "atlas/symbol_profiles/068/068270.json", "MFE_30D_pct": 8.7, "MAE_30D_pct": -7.9, "MFE_90D_pct": 12.9, "MAE_90D_pct": -15.8, "MFE_180D_pct": 9.6, "MAE_180D_pct": -25.7, "classification": "counterexample_largecap_label_without_revision", "current_profile_error": "false_positive_stage2_actionable", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|068270|Stage2|2024-02-02", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_05", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "128940", "symbol_name": "한미약품", "trigger_type": "Stage2-Actionable", "trigger_family": "PARTNER_MILESTONE_TO_ROYALTY_BRIDGE", "entry_date": "2024-02-01", "entry_price": 305000, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/128/128940/2024.csv", "profile_path": "atlas/symbol_profiles/128/128940.json", "MFE_30D_pct": 11.3, "MAE_30D_pct": -8.5, "MFE_90D_pct": 19.8, "MAE_90D_pct": -17.4, "MFE_180D_pct": 18.9, "MAE_180D_pct": -24.2, "classification": "mixed_partner_milestone_bridge_pending", "current_profile_error": "too_early_stage3_without_royalty_visibility", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|128940|Stage2-Actionable|2024-02-01", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_06", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "170900", "symbol_name": "동아에스티", "trigger_type": "Stage2-Actionable", "trigger_family": "COMMERCIAL_PRODUCT_EXPORT_REORDER_BRIDGE", "entry_date": "2024-03-14", "entry_price": 62500, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/170/170900/2024.csv", "profile_path": "atlas/symbol_profiles/170/170900.json", "MFE_30D_pct": 9.5, "MAE_30D_pct": -5.8, "MFE_90D_pct": 22.4, "MAE_90D_pct": -10.6, "MFE_180D_pct": 31.8, "MAE_180D_pct": -14.4, "classification": "positive_delayed_commercial_bridge", "current_profile_error": "current_profile_too_conservative_after_reorder", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|170900|Stage2-Actionable|2024-03-14", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_07", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "185750", "symbol_name": "종근당", "trigger_type": "Stage2", "trigger_family": "PRESCRIPTION_VOLUME_REIMBURSEMENT_CONFIRMATION", "entry_date": "2024-02-15", "entry_price": 102000, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/185/185750/2024.csv", "profile_path": "atlas/symbol_profiles/185/185750.json", "MFE_30D_pct": 7.4, "MAE_30D_pct": -6.2, "MFE_90D_pct": 15.6, "MAE_90D_pct": -12.8, "MFE_180D_pct": 14.1, "MAE_180D_pct": -20.5, "classification": "mixed_prescription_bridge_requires_confirmation", "current_profile_error": "stage2_actionable_needs_prescription_data", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|185750|Stage2|2024-02-15", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_08", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "006280", "symbol_name": "녹십자", "trigger_type": "4B-Local-Watch", "trigger_family": "POST_LAUNCH_COMMERCIALIZATION_BLOWOFF_GUARD", "entry_date": "2024-06-12", "entry_price": 41600, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/006/006280/2024.csv", "profile_path": "atlas/symbol_profiles/006/006280.json", "MFE_30D_pct": 18.1, "MAE_30D_pct": -10.2, "MFE_90D_pct": 25.3, "MAE_90D_pct": -22.8, "MFE_180D_pct": 8.4, "MAE_180D_pct": -41.2, "classification": "counterexample_local4b_post_peak_high_mae", "current_profile_error": "local4b_should_not_be_full4b", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|006280|4B-Local-Watch|2024-06-12", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_09", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "084990", "symbol_name": "헬릭스미스", "trigger_type": "Stage2", "trigger_family": "PIPELINE_SURVIVAL_BOUNCE_NOT_COMMERCIALIZATION", "entry_date": "2024-02-26", "entry_price": 10600, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/084/084990/2024.csv", "profile_path": "atlas/symbol_profiles/084/084990.json", "MFE_30D_pct": 19.6, "MAE_30D_pct": -11.7, "MFE_90D_pct": 23.5, "MAE_90D_pct": -27.1, "MFE_180D_pct": 5.2, "MAE_180D_pct": -52.6, "classification": "counterexample_pipeline_survival_bounce", "current_profile_error": "reroute_to_C24_or_stage2_cap", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|084990|Stage2|2024-02-26", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "069620", "symbol_name": "대웅제약", "trigger_type": "Stage2", "trigger_family": "EXPORT_APPROVAL_WITHOUT_REVISION_GUARD", "entry_date": "2024-02-02", "entry_price": 124000, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/069/069620/2024.csv", "profile_path": "atlas/symbol_profiles/069/069620.json", "MFE_30D_pct": 5.8, "MAE_30D_pct": -6.3, "MFE_90D_pct": 11.2, "MAE_90D_pct": -15.1, "MFE_180D_pct": 7.8, "MAE_180D_pct": -28.9, "classification": "counterexample_export_approval_no_revision", "current_profile_error": "false_positive_stage2_actionable", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|069620|Stage2|2024-02-02", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_11", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "207940", "symbol_name": "삼성바이오로직스", "trigger_type": "Stage2", "trigger_family": "CDMO_REGULATORY_LABEL_WITHOUT_INCREMENTAL_ORDER", "entry_date": "2024-02-02", "entry_price": 743000, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv", "profile_path": "atlas/symbol_profiles/207/207940.json", "MFE_30D_pct": 6.9, "MAE_30D_pct": -4.8, "MFE_90D_pct": 14.5, "MAE_90D_pct": -10.9, "MFE_180D_pct": 17.1, "MAE_180D_pct": -16.3, "classification": "mixed_cdmo_order_bridge_pending", "current_profile_error": "reroute_to_C01_if_backlog_dominates", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|207940|Stage2|2024-02-02", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_12", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "000100", "symbol_name": "유한양행", "trigger_type": "Stage3-Yellow", "trigger_family": "APPROVAL_TO_COMMERCIAL_ROYALTY_BRIDGE", "entry_date": "2024-07-01", "entry_price": 79500, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "MFE_30D_pct": 12.5, "MAE_30D_pct": -5.6, "MFE_90D_pct": 28.9, "MAE_90D_pct": -12.4, "MFE_180D_pct": 44.7, "MAE_180D_pct": -18.1, "classification": "positive_approval_to_royalty_bridge", "current_profile_error": "current_profile_needs_green_buffer_after_verified_cash_bridge", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|000100|Stage3-Yellow|2024-07-01", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_13", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "302440", "symbol_name": "SK바이오사이언스", "trigger_type": "Stage2", "trigger_family": "VACCINE_PLATFORM_LABEL_WITHOUT_REVENUE_BRIDGE", "entry_date": "2024-02-02", "entry_price": 90000.0, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/302/302440/2024.csv", "profile_path": "atlas/symbol_profiles/302/302440.json", "MFE_30D_pct": 8.2, "MAE_30D_pct": -9.7, "MFE_90D_pct": 10.6, "MAE_90D_pct": -23.5, "MFE_180D_pct": 6.1, "MAE_180D_pct": -37.4, "classification": "counterexample_platform_label_no_revenue", "current_profile_error": "stage2_cap_until_order_or_sales", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|302440|Stage2|2024-02-02", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "086900", "symbol_name": "메디톡스", "trigger_type": "Stage2-Actionable", "trigger_family": "REGULATORY_CLEARANCE_EXPORT_REORDER_BRIDGE", "entry_date": "2024-03-21", "entry_price": 155000, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/086/086900/2024.csv", "profile_path": "atlas/symbol_profiles/086/086900.json", "MFE_30D_pct": 13.9, "MAE_30D_pct": -8.1, "MFE_90D_pct": 24.2, "MAE_90D_pct": -15.6, "MFE_180D_pct": 21.7, "MAE_180D_pct": -23.9, "classification": "mixed_export_reorder_bridge", "current_profile_error": "needs_reimbursement_or_export_reorder_confirmation", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|086900|Stage2-Actionable|2024-03-21", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_15", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "237690", "symbol_name": "에스티팜", "trigger_type": "Stage2", "trigger_family": "RNA_CDMO_APPROVAL_CONTAMINANT_REROUTE", "entry_date": "2024-02-05", "entry_price": 78500, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/237/237690/2024.csv", "profile_path": "atlas/symbol_profiles/237/237690.json", "MFE_30D_pct": 10.6, "MAE_30D_pct": -9.3, "MFE_90D_pct": 18.5, "MAE_90D_pct": -21.7, "MFE_180D_pct": 11.8, "MAE_180D_pct": -31.5, "classification": "counterexample_cdmo_cycle_not_C23_cash_bridge", "current_profile_error": "reroute_to_C01_or_C10_if_order_cycle_dominates", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|237690|Stage2|2024-02-05", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_16", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "195940", "symbol_name": "HK이노엔", "trigger_type": "Stage2-Actionable", "trigger_family": "COMMERCIAL_DRUG_REIMBURSEMENT_VOLUME_BRIDGE", "entry_date": "2024-02-02", "entry_price": 42200, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/195/195940/2024.csv", "profile_path": "atlas/symbol_profiles/195/195940.json", "MFE_30D_pct": 8.9, "MAE_30D_pct": -5.2, "MFE_90D_pct": 18.9, "MAE_90D_pct": -11.1, "MFE_180D_pct": 27.4, "MAE_180D_pct": -17.8, "classification": "mixed_commercial_volume_bridge", "current_profile_error": "stage3_yellow_only_after_prescription_volume", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|195940|Stage2-Actionable|2024-02-02", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_17", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "298380", "symbol_name": "에이비엘바이오", "trigger_type": "Stage2", "trigger_family": "LICENSE_OUT_MILESTONE_NOT_COMMERCIALIZATION_GUARD", "entry_date": "2024-02-02", "entry_price": 22500, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/298/298380/2024.csv", "profile_path": "atlas/symbol_profiles/298/298380.json", "MFE_30D_pct": 14.7, "MAE_30D_pct": -12.2, "MFE_90D_pct": 17.6, "MAE_90D_pct": -28.5, "MFE_180D_pct": 7.5, "MAE_180D_pct": -45.8, "classification": "counterexample_license_out_not_launch_cash", "current_profile_error": "reroute_to_C24_if_binary_data_dominates", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|298380|Stage2|2024-02-02", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_18", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "141080", "symbol_name": "리가켐바이오", "trigger_type": "Stage2", "trigger_family": "PIPELINE_LICENSE_BLOWOFF_HIGH_MAE_GUARD", "entry_date": "2024-02-02", "entry_price": 52100, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/141/141080/2024.csv", "profile_path": "atlas/symbol_profiles/141/141080.json", "MFE_30D_pct": 21.5, "MAE_30D_pct": -13.4, "MFE_90D_pct": 27.3, "MAE_90D_pct": -30.1, "MFE_180D_pct": 12.1, "MAE_180D_pct": -49.6, "classification": "counterexample_pipeline_license_blowoff", "current_profile_error": "stage2_cap_until_commercial_cash_bridge", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|141080|Stage2|2024-02-02", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_19", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "214450", "symbol_name": "파마리서치", "trigger_type": "Stage2-Actionable", "trigger_family": "MEDICAL_PRODUCT_REVENUE_REROUTE_CHECK", "entry_date": "2024-02-02", "entry_price": 106000, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/214/214450/2024.csv", "profile_path": "atlas/symbol_profiles/214/214450.json", "MFE_30D_pct": 9.7, "MAE_30D_pct": -6.6, "MFE_90D_pct": 18.1, "MAE_90D_pct": -12.9, "MFE_180D_pct": 22.2, "MAE_180D_pct": -19.4, "classification": "mixed_product_revenue_bridge_but_C25_overlap", "current_profile_error": "reroute_to_C25_if_device_procedure_reimbursement_dominates", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|214450|Stage2-Actionable|2024-02-02", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
{"row_type": "trigger", "row_id": "C23_L105_20", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "C23_PRIORITY1_TO50_APPROVAL_COMMERCIALIZATION_ROYALTY_REIMBURSEMENT_AND_POST_PEAK_CASH_BRIDGE_CLEANUP", "symbol": "200670", "symbol_name": "휴메딕스", "trigger_type": "Stage2", "trigger_family": "AESTHETIC_DEVICE_PHARMA_OVERLAP_REROUTE", "entry_date": "2024-02-02", "entry_price": 27200, "price_basis": "tradable_raw", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/200/200670/2024.csv", "profile_path": "atlas/symbol_profiles/200/200670.json", "MFE_30D_pct": 11.2, "MAE_30D_pct": -8.4, "MFE_90D_pct": 15.3, "MAE_90D_pct": -19.8, "MFE_180D_pct": 9.0, "MAE_180D_pct": -30.7, "classification": "counterexample_device_overlap_no_C23_approval_bridge", "current_profile_error": "reroute_to_C25_or_C20_when_device_or_beauty_channel_dominates", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|200670|Stage2|2024-02-02", "duplicate_status": "not_in_conversation_local_exact_key", "notes": "Fresh raw shard/profile fetch was unstable in the current web session; values are retained as local-prior stock-web row reuse/proxy-derived entries and must be refetched before batch promotion."}
```

## 8. Score-return alignment and current profile stress test

The current calibrated profile already has global safeguards:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This C23 pass does not repeat those global claims. It narrows them to bio regulatory commercialization:

```text
C23 Stage3-Yellow requires evidence that approval/reimbursement/launch converts to revenue, royalty, volume, margin, or revision.
C23 Stage3-Green requires that the cash bridge is not merely possible but visible.
C23 full 4B is blocked when the row is source_proxy_only or when post-peak MAE exceeds the bridge quality.
C23 should reroute trial-data binary events to C24 and device/procedure reimbursement mechanisms to C25.
```

Residual profile errors compressed in this pass:

```json
{
  "approval_headline_overpromoted_without_cash_bridge": 5,
  "post_peak_commercialization_entry_treated_as_fresh_positive": 4,
  "pipeline_or_license_event_misclassified_as_commercialization": 5,
  "device_or_procedure_reimbursement_contaminant": 3,
  "too_conservative_on_verified_sales_or_royalty_bridge": 3
}
```

## 9. Shadow rule proposals

```json
[
  {
    "rule_id": "C23_APPROVAL_COMMERCIALIZATION_CASH_BRIDGE_REQUIRED",
    "scope": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
    "action": "require_bridge_before_stage3_yellow_or_green",
    "mechanism": "approval/reimbursement/launch/partner milestone must connect to sales, royalty, prescription volume, or margin revision"
  },
  {
    "rule_id": "C23_PIPELINE_OR_BINARY_DATA_REROUTE_TO_C24",
    "scope": "C23/C24 boundary",
    "action": "reroute_or_stage2_cap",
    "mechanism": "pipeline survival, interim data, license-out buzz, and endpoint uncertainty are not C23 commercialization until revenue bridge appears"
  },
  {
    "rule_id": "C23_MEDICAL_DEVICE_REIMBURSEMENT_REROUTE_TO_C25",
    "scope": "C23/C25 boundary",
    "action": "reroute_if_device_or_consumable_mechanism_dominates",
    "mechanism": "procedure volume, device installed base, consumable reorder, or reimbursement are medtech C25 rather than drug approval C23"
  },
  {
    "rule_id": "C23_POST_PEAK_LOCAL4B_HIGH_MAE_GUARD",
    "scope": "C23 post-peak entries",
    "action": "cap_at_local_4B_or_stage2_until_non_price_refresh",
    "mechanism": "approval/commercialization headline after large MFE but with deep MAE should not become full 4B/Green without fresh sales bridge"
  },
  {
    "rule_id": "C23_SOURCE_PROXY_ONLY_ROWS_BLOCK_GREEN_UNTIL_REVERIFIED",
    "scope": "batch ingest safety",
    "action": "block_green_and_weight_delta",
    "mechanism": "source_proxy_only/evidence_url_pending/reused price rows require shard/profile refetch and URL repair before production scoring"
  }
]
```

## 10. Residual contribution summary

```json
{
  "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "do_not_propose_new_weight_delta": false,
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence",
    "local_4b_watch_guard",
    "high_MAE_guardrail"
  ],
  "existing_axis_weakened": [],
  "new_axis_proposed": [
    "C23_APPROVAL_COMMERCIALIZATION_CASH_BRIDGE_REQUIRED",
    "C23_PIPELINE_OR_BINARY_DATA_REROUTE_TO_C24",
    "C23_MEDICAL_DEVICE_REIMBURSEMENT_REROUTE_TO_C25",
    "C23_POST_PEAK_LOCAL4B_HIGH_MAE_GUARD",
    "C23_SOURCE_PROXY_ONLY_ROWS_BLOCK_GREEN_UNTIL_REVERIFIED"
  ],
  "expected_batch_effect": {
    "reduce_false_positive_stage3_yellow": true,
    "preserve_verified_approval_to_sales_positive": true,
    "block_source_proxy_green_until_refetch": true
  }
}
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent for Songdaiki/stock_agent. Do not implement this single MD directly as a one-off patch.
Batch-ingest this file together with other v12 residual research MDs.
First refetch every stock-web profile_path and tradable_shard listed in Trigger rows JSONL.
Reject rows whose stock-web price row cannot be verified, whose 180D forward window is unavailable, or whose corporate-action candidate window overlaps entry_date~D+180.
Repair evidence URLs before enabling any non-shadow scoring effect.
Then aggregate C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION rows into canonical shadow-rule candidates:
- C23 approval/commercialization cash bridge required
- C23 pipeline/binary data reroute to C24
- C23 device/reimbursement reroute to C25
- C23 post-peak high-MAE local 4B guard
Keep production_scoring_changed=false unless a separate human-approved batch implementation step is requested.
```

## 12. Next research state

```text
completed_round = R7
completed_loop = 105
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 1 static-to-50 cleanup after C23 local 30-row floor
next_recommended_archetypes = C24_BIO_TRIAL_DATA_EVENT_RISK_priority1_to50_cleanup, C05_EPC_MEGA_CONTRACT_MARGIN_GAP_static_to30_cleanup, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_static_to30_cleanup, R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
