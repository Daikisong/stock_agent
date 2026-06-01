# E2R Stock-Web v12 Residual Research — R7 Loop 82 / L7 / C25

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R7",
  "scheduled_loop": 82,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 82,
  "computed_next_round": "R8",
  "computed_next_loop": 82,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "fine_archetype_id": "DIAGNOSTIC_DENTAL_OPHTHALMIC_DEVICE_EXPORT_CHANNEL_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "medical_device_export_reimbursement_guardrail",
    "diagnostic_dental_ophthalmic_device_export_channel_margin_bridge",
    "device_theme_fade_boundary",
    "share_count_validation_queue_creation",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## Execution compliance note

This file is a standalone historical calibration / sector-archetype residual research Markdown artifact.  
It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

The execution used `Songdaiki/stock-web` as the sole price atlas:

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R6 / loop 82.

Therefore:

```text
scheduled_round = R7
scheduled_loop = 82
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
computed_next_round = R8
computed_next_loop = 82
```

R7 was routed to C25 because loop 81 R7 used C23 and loop 80 R7 used C24.  
This file tests medical-device export/reimbursement/distributor-channel bridges rather than regulatory approval or trial-data event risk.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C25 concentration in:

```text
338220, 214150, 145720, 099190, 228670, 335890
```

This run uses three different medical-device symbols:

```text
041830 / 인바디 / diagnostic body-composition device export-channel candidate
043150 / 바텍 / dental imaging device export/reimbursement fade
065510 / 휴비츠 / ophthalmic/optical device export theme fade with share-count validation
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
065510 shows share-count changes inside the selected 2024 shard and requires coding-agent validation before runtime promotion.
```

## Research thesis

C25 is not “의료기기주가 올랐다.”

The mechanism must pass through:

```text
medical device / export / reimbursement headline
→ distributor or hospital/clinic channel order
→ reimbursement or clinic capex cycle
→ reorder and revenue conversion
→ margin bridge
→ durable rerating
```

의료기기는 제품 사진이 아니라 병원·대리점·상환체계가 반복해서 당겨주는 주문서다.  
C25가 보려는 것은 장비 테마가 실제 수출 채널, 재주문, 매출, 마진으로 연결되는지다.

---

## Case 1 — Bounded diagnostic-device candidate: 041830 / 인바디

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is diagnostic-device export channel, hospital/fitness/clinic reorder, reimbursement or distributor channel quality, revenue conversion and margin bridge evidence.

```text
evidence_family = BODY_COMPOSITION_DIAGNOSTIC_DEVICE_EXPORT_CHANNEL_REIMBURSEMENT_REORDER_REVENUE_MARGIN_BRIDGE
case_role = positive_bounded_diagnostic_device_export_channel_candidate_no_forced4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 24,850
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/041/041830/2024.csv`:

```text
2024-02-01,24850,25650,24750,25400
2024-02-19,27250,28450,27000,28000
2024-03-26,29250,30200,28850,30050
2024-04-01,30650,31650,30450,31300
2024-08-05,22800,22800,21600,21750
2024-08-30,25050,26200,25000,25750
2024-09-12,23150,23600,22750,22950
2024-10-31,24500,24700,24100,24400
```

### Backtest

```text
MFE_30D  = +14.49%
MAE_30D  = -0.80%
MFE_90D  = +27.36%
MAE_90D  = -0.80%
MFE_180D = +27.36%
MAE_180D = -13.08%
peak_180 = 31,650 on 2024-04-01
trough_180 = 21,600 on 2024-08-05
peak_to_later_drawdown = -31.75%
```

### Interpretation

This is a bounded C25 diagnostic-device export candidate, not an explosive Green.  
The MAE stayed below the local-4B high-MAE threshold, so it should not be forced into 4B without non-price deterioration.

Correct treatment:

```text
verified diagnostic-device export channel / distributor reorder / reimbursement or clinic demand / margin bridge → Stage2-Yellow possible
bounded MAE + weak bridge → RiskWatch
no forced 4B without non-price channel or margin deterioration
```

---

## Case 2 — Counterexample / local 4B: 043150 / 바텍

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests dental-imaging device export/reimbursement beta without enough distributor-order, clinic-demand, revenue and margin bridge.

```text
evidence_family = DENTAL_IMAGING_DEVICE_EXPORT_CHANNEL_REIMBURSEMENT_THEME_WITH_WEAK_ORDER_REVENUE_MARGIN_BRIDGE
case_role = counterexample_dental_imaging_export_channel_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 32,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/043/043150/2024.csv`:

```text
2024-02-01,32500,32500,31550,31900
2024-02-06,30800,31000,30100,30300
2024-02-27,30450,30700,29800,29950
2024-04-01,30750,31650,30450,31300
2024-08-05,25000,25150,23050,23250
2024-09-04,23350,23350,22700,22700
2024-10-29,23550,25900,23000,23150
2024-10-31,22900,23000,22600,22750
```

### Backtest

```text
MFE_30D  = +0.00%
MAE_30D  = -8.31%
MFE_90D  = +0.00%
MAE_90D  = -8.62%
MFE_180D = +0.00%
MAE_180D = -30.46%
peak_180 = 32,500 on 2024-02-01
trough_180 = 22,600 on 2024-10-31
peak_to_later_drawdown = -30.46%
```

### Interpretation

This is a C25 false-positive / local-4B boundary.  
There was no meaningful forward MFE after entry and the path widened into high-MAE territory.

Correct treatment:

```text
dental imaging device export/reimbursement theme beta
→ no verified distributor order / clinic demand / revenue / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 065510 / 휴비츠

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
source_repair_required = true
```

This row tests ophthalmic/optical device export beta without enough channel-order and margin bridge.

```text
evidence_family = OPHTHALMIC_OPTICAL_DEVICE_EXPORT_CHANNEL_THEME_WITH_WEAK_ORDER_REVENUE_MARGIN_BRIDGE
case_role = counterexample_ophthalmic_device_export_theme_local4b_with_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 18,180
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/065/065510/2024.csv`:

```text
2024-02-01,18180,18380,17770,18000
2024-02-05,19190,21900,18080,18220
2024-02-27,17620,17700,15530,15530
2024-04-08,12990,12990,12550,12560
2024-08-05,10010,10100,8500,8860
2024-09-06,9810,9930,9530,9600
2024-10-25,8940,8940,8690,8770
2024-10-31,8710,9040,8600,9030
```

### Backtest

```text
MFE_30D  = +20.46%
MAE_30D  = -19.31%
MFE_90D  = +20.46%
MAE_90D  = -32.45%
MFE_180D = +20.46%
MAE_180D = -53.25%
peak_180 = 21,900 on 2024-02-05
trough_180 = 8,500 on 2024-08-05
peak_to_later_drawdown = -61.19%
```

### Interpretation

This is a C25 ophthalmic-device export theme-fade row.  
The early spike did not convert into durable order/revenue/margin economics, and the later MAE was severe.

Correct treatment:

```text
ophthalmic/optical device export theme beta
→ no verified distributor order / reimbursement or clinic capex / revenue / margin bridge
→ local 4B-watch
→ share-count validation before runtime ingestion
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
medical_device_export_reimbursement_bridge_required = strengthen
device_order_distributor_revenue_margin_guard = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
bounded_MAE_no_forced_4B_guard = strengthen
share_count_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C25_medical_device_theme_weight = true
do_not_treat_all_device_MFE_as_Green = true
do_not_ingest_sharecount_changed_device_rows_without_validation = true
do_not_convert_medical_device_drawdown_to_hard_4C_without_non_price_reimbursement_channel_order_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
DIAGNOSTIC_DENTAL_OPHTHALMIC_DEVICE_EXPORT_CHANNEL_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE
```

This fine archetype covers:

```text
1. diagnostic-device export channel with bounded MAE → Stage2-Yellow possible after source repair
2. dental-imaging device export/reimbursement theme fade → false Stage2 / local 4B
3. ophthalmic/optical device export theme fade with share-count validation → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R7L82-C25-041830-INBODY-DIAGNOSTIC-DEVICE-EXPORT-BOUNDED", "symbol": "041830", "company_name": "인바디", "round": "R7", "loop": "82", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DIAGNOSTIC_DENTAL_OPHTHALMIC_DEVICE_EXPORT_CHANNEL_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "case_type": "medical_device_export_reimbursement", "positive_or_counterexample": "positive", "best_trigger": "RiskWatch-PositiveDiagnosticDeviceExportChannelMarginNoForced4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C25 should allow bounded diagnostic-device export positives only when export channel, hospital/fitness/clinic reorder, reimbursement or distributor channel quality, revenue conversion and margin bridge are visible. InBody had moderate MFE with bounded MAE, so it should be RiskWatch/Stage2-Yellow after source repair, not forced 4B.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy distributor/export channel, device order, reimbursement or clinic capex cycle, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R7L82-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-FADE", "symbol": "043150", "company_name": "바텍", "round": "R7", "loop": "82", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DIAGNOSTIC_DENTAL_OPHTHALMIC_DEVICE_EXPORT_CHANNEL_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "case_type": "medical_device_export_reimbursement", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / DentalImagingDeviceExportReimbursementFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C25 should not treat dental-imaging device export/reimbursement theme beta as durable Stage2 unless distributor channel order, dental clinic demand, reimbursement or capex cycle, revenue conversion and margin bridge are visible. Vatech had almost no forward MFE and a persistent MAE path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy distributor/export channel, device order, reimbursement or clinic capex cycle, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R7L82-C25-065510-HUVITZ-OPHTHALMIC-DEVICE-SHARECOUNT-FADE", "symbol": "065510", "company_name": "휴비츠", "round": "R7", "loop": "82", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DIAGNOSTIC_DENTAL_OPHTHALMIC_DEVICE_EXPORT_CHANNEL_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "case_type": "medical_device_export_reimbursement", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / OphthalmicDeviceExportThemeFadeWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C25 should not treat ophthalmic/optical device export theme beta as durable Stage2 unless customer order, distributor channel, reimbursement/capex cycle, revenue conversion and margin bridge are visible. Huvitz had an early spike, a severe high-MAE fade, and 2024 shard share-count changes that require validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy distributor/export channel, device order, reimbursement or clinic capex cycle, revenue conversion and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R7L82-C25-041830-INBODY-DIAGNOSTIC-DEVICE-EXPORT-BOUNDED", "case_id": "R7L82-C25-041830-INBODY-DIAGNOSTIC-DEVICE-EXPORT-BOUNDED", "symbol": "041830", "company_name": "인바디", "round": "R7", "loop": "82", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DIAGNOSTIC_DENTAL_OPHTHALMIC_DEVICE_EXPORT_CHANNEL_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail", "trigger_type": "RiskWatch-PositiveDiagnosticDeviceExportChannelMarginNoForced4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 24850.0, "evidence_available_at_that_date": "BODY_COMPOSITION_DIAGNOSTIC_DEVICE_EXPORT_CHANNEL_REIMBURSEMENT_REORDER_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:INBODY_2024_DIAGNOSTIC_DEVICE_EXPORT_CHANNEL_REORDER_REIMBURSEMENT_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["device_export_channel_candidate", "reimbursement_or_clinic_capex_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "distributor_reorder_or_customer_quality_candidate"], "stage4b_evidence_fields": ["medical_device_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041830/2024.csv", "profile_path": "atlas/symbol_profiles/041/041830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.49, "MFE_90D_pct": 27.36, "MFE_180D_pct": 27.36, "MAE_30D_pct": -0.8, "MAE_90D_pct": -0.8, "MAE_180D_pct": -13.08, "peak_date": "2024-04-01", "peak_price": 31650.0, "drawdown_after_peak_pct": -31.75, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_medical_device_peak_if_export_reimbursement_reorder_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reimbursement_cut_channel_collapse_order_loss_margin_or_regulatory_break", "trigger_outcome_label": "positive_bounded_diagnostic_device_export_channel_candidate_no_forced4b", "current_profile_verdict": "C25 should allow bounded diagnostic-device export positives only when export channel, hospital/fitness/clinic reorder, reimbursement or distributor channel quality, revenue conversion and margin bridge are visible. InBody had moderate MFE with bounded MAE, so it should be RiskWatch/Stage2-Yellow after source repair, not forced 4B.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C25_MEDICAL_DEVICE_041830_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L82-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-FADE", "case_id": "R7L82-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-FADE", "symbol": "043150", "company_name": "바텍", "round": "R7", "loop": "82", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DIAGNOSTIC_DENTAL_OPHTHALMIC_DEVICE_EXPORT_CHANNEL_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail", "trigger_type": "Stage2-FalsePositive / DentalImagingDeviceExportReimbursementFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 32500.0, "evidence_available_at_that_date": "DENTAL_IMAGING_DEVICE_EXPORT_CHANNEL_REIMBURSEMENT_THEME_WITH_WEAK_ORDER_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:VATECH_2024_DENTAL_IMAGING_EXPORT_CHANNEL_DISTRIBUTOR_ORDER_REIMBURSEMENT_MARGIN_BRIDGE", "stage2_evidence_fields": ["device_export_channel_candidate", "reimbursement_or_clinic_capex_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "distributor_reorder_or_customer_quality_candidate"], "stage4b_evidence_fields": ["medical_device_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/043/043150/2024.csv", "profile_path": "atlas/symbol_profiles/043/043150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "MFE_180D_pct": 0.0, "MAE_30D_pct": -8.31, "MAE_90D_pct": -8.62, "MAE_180D_pct": -30.46, "peak_date": "2024-02-01", "peak_price": 32500.0, "drawdown_after_peak_pct": -30.46, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_medical_device_peak_if_export_reimbursement_reorder_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reimbursement_cut_channel_collapse_order_loss_margin_or_regulatory_break", "trigger_outcome_label": "counterexample_dental_imaging_export_channel_local4b", "current_profile_verdict": "C25 should not treat dental-imaging device export/reimbursement theme beta as durable Stage2 unless distributor channel order, dental clinic demand, reimbursement or capex cycle, revenue conversion and margin bridge are visible. Vatech had almost no forward MFE and a persistent MAE path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C25_MEDICAL_DEVICE_043150_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L82-C25-065510-HUVITZ-OPHTHALMIC-DEVICE-SHARECOUNT-FADE", "case_id": "R7L82-C25-065510-HUVITZ-OPHTHALMIC-DEVICE-SHARECOUNT-FADE", "symbol": "065510", "company_name": "휴비츠", "round": "R7", "loop": "82", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DIAGNOSTIC_DENTAL_OPHTHALMIC_DEVICE_EXPORT_CHANNEL_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail", "trigger_type": "Stage2-FalsePositive / OphthalmicDeviceExportThemeFadeWithSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 18180.0, "evidence_available_at_that_date": "OPHTHALMIC_OPTICAL_DEVICE_EXPORT_CHANNEL_THEME_WITH_WEAK_ORDER_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HUVITZ_2024_OPHTHALMIC_OPTICAL_DEVICE_EXPORT_CHANNEL_ORDER_REIMBURSEMENT_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["device_export_channel_candidate", "reimbursement_or_clinic_capex_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "distributor_reorder_or_customer_quality_candidate"], "stage4b_evidence_fields": ["medical_device_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/065/065510/2024.csv", "profile_path": "atlas/symbol_profiles/065/065510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.46, "MFE_90D_pct": 20.46, "MFE_180D_pct": 20.46, "MAE_30D_pct": -19.31, "MAE_90D_pct": -32.45, "MAE_180D_pct": -53.25, "peak_date": "2024-02-05", "peak_price": 21900.0, "drawdown_after_peak_pct": -61.19, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_medical_device_peak_if_export_reimbursement_reorder_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reimbursement_cut_channel_collapse_order_loss_margin_or_regulatory_break", "trigger_outcome_label": "counterexample_ophthalmic_device_export_theme_local4b_with_sharecount_validation", "current_profile_verdict": "C25 should not treat ophthalmic/optical device export theme beta as durable Stage2 unless customer order, distributor channel, reimbursement/capex cycle, revenue conversion and margin bridge are visible. Huvitz had an early spike, a severe high-MAE fade, and 2024 shard share-count changes that require validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C25_MEDICAL_DEVICE_065510_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L82-C25-041830-INBODY-DIAGNOSTIC-DEVICE-EXPORT-BOUNDED", "trigger_id": "TRG_R7L82-C25-041830-INBODY-DIAGNOSTIC-DEVICE-EXPORT-BOUNDED", "symbol": "041830", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"export_channel_score": 13, "reimbursement_or_clinic_capex_score": 12, "distributor_reorder_score": 12, "revenue_conversion_score": 12, "margin_bridge_score": 12, "relative_strength_score": 7, "sharecount_validation_risk": 0, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_before": 68, "stage_label_before": "RiskWatch / Stage2-Yellow candidate after source repair", "raw_component_scores_after": {"export_channel_score": 15, "reimbursement_or_clinic_capex_score": 14, "distributor_reorder_score": 14, "revenue_conversion_score": 14, "margin_bridge_score": 14, "relative_strength_score": 6, "sharecount_validation_risk": 0, "execution_risk_score": 12, "source_confidence_score": 2}, "weighted_score_after": 74, "stage_label_after": "Stage2-Yellow only after source repair / no forced 4B", "changed_components": ["export_channel_score", "reimbursement_or_clinic_capex_score", "distributor_reorder_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified device export channel, reimbursement or clinic capex cycle, distributor reorder, revenue conversion and margin bridge; cap device theme beta when bridge fails to refresh.", "MFE_90D_pct": 27.36, "MAE_90D_pct": -0.8, "score_return_alignment_label": "medical_device_export_bounded_candidate", "current_profile_verdict": "C25 should allow bounded diagnostic-device export positives only when export channel, hospital/fitness/clinic reorder, reimbursement or distributor channel quality, revenue conversion and margin bridge are visible. InBody had moderate MFE with bounded MAE, so it should be RiskWatch/Stage2-Yellow after source repair, not forced 4B."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L82-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-FADE", "trigger_id": "TRG_R7L82-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-FADE", "symbol": "043150", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"export_channel_score": 4, "reimbursement_or_clinic_capex_score": 3, "distributor_reorder_score": 2, "revenue_conversion_score": 2, "margin_bridge_score": 1, "relative_strength_score": 2, "sharecount_validation_risk": 0, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"export_channel_score": 2, "reimbursement_or_clinic_capex_score": 1, "distributor_reorder_score": 1, "revenue_conversion_score": 1, "margin_bridge_score": 1, "relative_strength_score": 2, "sharecount_validation_risk": 0, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["export_channel_score", "reimbursement_or_clinic_capex_score", "distributor_reorder_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified device export channel, reimbursement or clinic capex cycle, distributor reorder, revenue conversion and margin bridge; cap device theme beta when bridge fails to refresh.", "MFE_90D_pct": 0.0, "MAE_90D_pct": -8.62, "score_return_alignment_label": "false_positive_medical_device_bridge_gap", "current_profile_verdict": "C25 should not treat dental-imaging device export/reimbursement theme beta as durable Stage2 unless distributor channel order, dental clinic demand, reimbursement or capex cycle, revenue conversion and margin bridge are visible. Vatech had almost no forward MFE and a persistent MAE path."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L82-C25-065510-HUVITZ-OPHTHALMIC-DEVICE-SHARECOUNT-FADE", "trigger_id": "TRG_R7L82-C25-065510-HUVITZ-OPHTHALMIC-DEVICE-SHARECOUNT-FADE", "symbol": "065510", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"export_channel_score": 4, "reimbursement_or_clinic_capex_score": 3, "distributor_reorder_score": 2, "revenue_conversion_score": 2, "margin_bridge_score": 1, "relative_strength_score": 7, "sharecount_validation_risk": 10, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"export_channel_score": 2, "reimbursement_or_clinic_capex_score": 1, "distributor_reorder_score": 1, "revenue_conversion_score": 1, "margin_bridge_score": 1, "relative_strength_score": 2, "sharecount_validation_risk": 12, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["export_channel_score", "reimbursement_or_clinic_capex_score", "distributor_reorder_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified device export channel, reimbursement or clinic capex cycle, distributor reorder, revenue conversion and margin bridge; cap device theme beta when bridge fails to refresh.", "MFE_90D_pct": 20.46, "MAE_90D_pct": -32.45, "score_return_alignment_label": "false_positive_medical_device_bridge_gap", "current_profile_verdict": "C25 should not treat ophthalmic/optical device export theme beta as durable Stage2 unless customer order, distributor channel, reimbursement/capex cycle, revenue conversion and margin bridge are visible. Huvitz had an early spike, a severe high-MAE fade, and 2024 shard share-count changes that require validation."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R7", "loop": 82, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DIAGNOSTIC_DENTAL_OPHTHALMIC_DEVICE_EXPORT_CHANNEL_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C25 medical-device symbols outside top-covered 338220/214150/145720/099190/228670/335890 set, +3 diagnostic/dental/ophthalmic device trigger families, +1 bounded diagnostic-device candidate, +2 device export/reimbursement theme local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R7", "loop": 82, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "axis": "diagnostic_dental_ophthalmic_device_export_channel_reimbursement_margin_bridge_vs_device_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C25 should split verified medical-device export/reimbursement/distributor-channel margin rerating from generic medical-device theme beta. Stage2 requires export channel, distributor reorder, reimbursement or clinic capex cycle, revenue conversion and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count flags require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["041830", "043150", "065510"], "share_count_validation_required": ["065510"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": 82, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "existing_axis_strengthened": ["stage2_required_bridge", "medical_device_export_reimbursement_bridge_required", "device_order_distributor_revenue_margin_guard", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "bounded_MAE_no_forced_4B_guard", "share_count_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C25 needs medical-device MFE to map into export channel, distributor reorder, reimbursement or clinic capex cycle, revenue conversion and margin proof. InBody is a bounded diagnostic-device candidate after source repair; Vatech and Huvitz show dental/ophthalmic device theme beta fading into local 4B when order/revenue bridge is absent or stale."}
```

---

## Validation scope

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
forward_window_basis = stock_web_manifest_max_date
all_selected_entry_dates_present_in_tradable_shards = true
all_selected_180D_windows_available = true
production_scoring_changed = false
shadow_weight_only = true
```

Profile checks:

```text
041830:
  name = 인바디 from 2014-09-19, 바이오스페이스 / 바이오스페이 before that
  corporate_action_candidate_dates = 2010-04-23, 2010-05-18
  selected window = 2024-02-01~D+180
  contamination = false

043150:
  name = 바텍
  corporate_action_candidate_dates = 2010-09-02
  selected window = 2024-02-01~D+180
  contamination = false

065510:
  name = 휴비츠
  corporate_action_candidate_dates = 2004-04-22, 2004-05-21
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C25 rows are source_proxy_only / evidence_url_pending.
065510 requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C25 medical-device export/reimbursement rule-shape discovery,
but coding-agent promotion requires non-proxy distributor/export channel, device order, reimbursement or clinic capex cycle, revenue conversion and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R7/C25 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 065510 needs share-count validation.

Candidate axis:
diagnostic_dental_ophthalmic_device_export_channel_reimbursement_margin_bridge_vs_device_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 041830, 043150 and 065510.
4. Validate 065510 share-count changes inside the selected window.
5. Keep generic C25 medical-device export/reimbursement weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - export channel or distributor order is explicit,
   - reimbursement or clinic capex cycle is visible,
   - reorder or customer quality is visible,
   - revenue conversion and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is medical-device theme beta only,
   - export/reimbursement/order/revenue/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not force local 4B when bounded medical-device rows have controlled MAE and no confirmed non-price bridge break.
9. Do not convert local 4B-watch into full 4B/4C without non-price reimbursement cut, channel collapse, order loss, regulatory issue, financing or margin break.
10. Emit before/after diagnostics and reject if verified medical-device export positives or bounded diagnostic rows are overblocked.
```

---

## Final round state

```text
completed_round = R7
completed_loop = 82
next_round = R8
next_loop = 82
round_schedule_status = valid
round_sector_consistency = pass
```

