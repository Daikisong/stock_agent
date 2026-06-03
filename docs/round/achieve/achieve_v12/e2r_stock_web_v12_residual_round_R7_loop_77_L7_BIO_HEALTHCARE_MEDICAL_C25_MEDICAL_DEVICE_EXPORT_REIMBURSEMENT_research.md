# E2R Stock-Web v12 Residual Research — R7 Loop 77 / L7 / C25

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R7",
  "scheduled_loop": 77,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 77,
  "computed_next_round": "R8",
  "computed_next_loop": 77,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "fine_archetype_id": "AESTHETIC_CGM_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "medical_device_export_reimbursement_guardrail",
    "aesthetic_CGM_dental_bridge_vs_device_theme_beta",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "share_count_validation_queue_creation"
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

Previous completed state in this interactive run: R6 / loop 77.

Therefore:

```text
scheduled_round = R7
scheduled_loop = 77
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
computed_next_round = R8
computed_next_loop = 77
```

R7 was routed to C25 because loop 76 used C24.  
This file tests medical-device export/reimbursement/adoption bridges rather than clinical trial-data events or pharma approval-commercialization.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C25 is concentrated in:

```text
338220, 214150, 145720, 228670, 328130
```

This run uses three different symbols:

```text
214450 / 파마리서치 / aesthetic medical-device export-margin bridge
099190 / 아이센스 / CGM reimbursement/export beta fade
043150 / 바텍 / dental imaging export beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
214450 and 099190 show share-count changes inside the selected window and require coding-agent validation before runtime promotion.
```

## Research thesis

C25 is not “의료기기주가 올랐다.”

The mechanism must pass through:

```text
medical device / diagnostic / aesthetic product
→ approval, reimbursement, export or channel reorder
→ adoption, sell-through or installed-base utilization
→ pricing and margin bridge
→ durable rerating
```

의료기기 스토리는 병원 문 앞에서 끝나지 않는다.  
C25는 제품이 실제로 처방·시술·소모품 재주문·해외 채널 마진으로 이어지는지를 본다.

---

## Case 1 — Positive with lifecycle 4B: 214450 / 파마리서치

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is aesthetic device/product export channel reorder, approval/registration, pricing and margin bridge evidence.

```text
evidence_family = AESTHETIC_REJURAN_MEDICAL_DEVICE_EXPORT_CHANNEL_REORDER_PRICING_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-03-29
entry_date = 2024-04-01
entry_price = 99,700
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/214/214450/2024.csv`:

```text
2024-04-01,99700,110900,98600,108000
2024-05-16,143100,149600,133500,137300
2024-06-24,149300,157000,147000,153600
2024-08-16,184600,189500,184100,188100
2024-10-22,227000,238000,225000,230500
2024-11-01,221500,222000,211500,213000
```

### Backtest

```text
MFE_30D  = +49.95%
MAE_30D  = -1.10%
MFE_90D  = +57.87%
MAE_90D  = -1.10%
MFE_180D = +138.72%
MAE_180D = -1.10%
peak_180 = 238,000 on 2024-10-22
trough_180 = 98,600 on 2024-04-01
peak_to_later_drawdown = -11.13%
```

### Interpretation

This is the C25 positive-shaped row.  
The price path validates a device/export/margin rerating candidate, but runtime promotion still needs source repair and share-count validation.

Correct treatment:

```text
verified export/channel reorder/pricing/margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 099190 / 아이센스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

This row tests CGM/reimbursement/export beta without enough adoption, sell-through and margin bridge.

```text
evidence_family = CGM_REIMBURSEMENT_EXPORT_THEME_WITH_WEAK_ADOPTION_SELLTHROUGH_MARGIN_BRIDGE
case_role = counterexample_CGM_reimbursement_beta_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 24,400
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv`:

```text
2024-02-01,24400,24500,23200,23750
2024-02-02,24000,25550,24000,25200
2024-03-20,20950,21050,20000,20550
2024-08-05,17480,17520,15500,15990
2024-09-09,14820,15290,14520,15050
2024-10-17,19200,20750,19000,20500
```

### Backtest

```text
MFE_30D  = +4.71%
MAE_30D  = -18.03%
MFE_90D  = +4.71%
MAE_90D  = -22.62%
MFE_180D = +4.71%
MAE_180D = -40.49%
peak_180 = 25,550 on 2024-02-02
trough_180 = 14,520 on 2024-09-09
peak_to_later_drawdown = -43.17%
```

### Interpretation

This is a C25 false-positive row.  
Reimbursement/export beta did not become durable adoption and margin rerating.

Correct treatment:

```text
CGM / reimbursement theme beta
→ no adoption / sell-through / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 043150 / 바텍

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests dental imaging export-device beta without enough export reorder, installed-base utilization and margin bridge.

```text
evidence_family = DENTAL_IMAGING_EXPORT_THEME_WITH_WEAK_REORDER_UTILIZATION_MARGIN_BRIDGE
case_role = counterexample_dental_device_export_beta_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 32,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/043/043150/2024.csv`:

```text
2024-02-01,32500,32500,31550,31900
2024-02-27,30450,30700,29800,29950
2024-04-01,30750,31650,30450,31300
2024-08-05,25000,25150,23050,23250
2024-09-04,23350,23350,22700,22700
2024-10-31,22900,23000,22600,22750
```

### Backtest

```text
MFE_30D  = +0.00%
MAE_30D  = -7.85%
MFE_90D  = +0.00%
MAE_90D  = -8.62%
MFE_180D = +0.00%
MAE_180D = -30.46%
peak_180 = 32,500 on 2024-02-01
trough_180 = 22,600 on 2024-10-31
peak_to_later_drawdown = -30.46%
```

### Interpretation

This is a no-durable-Green boundary.  
The path failed to show meaningful MFE and drifted lower.

Correct treatment:

```text
dental imaging/export-device beta
→ no export reorder / installed-base / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
full_4b_requires_non_price_evidence = keep
share_count_validation_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C25_medical_device_theme_weight = true
do_not_treat_all_medical_device_MFE_as_Green = true
do_not_convert_medical_device_drawdown_to_hard_4C_without_non_price_approval_reimbursement_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
AESTHETIC_CGM_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE
```

This fine archetype covers:

```text
1. aesthetic medical-device export/channel/margin bridge → Stage2 possible after source repair
2. CGM reimbursement/export beta without adoption/margin bridge → false Stage2 / local 4B
3. dental imaging export beta without reorder/utilization bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R7L77-C25-214450-PHARMARESEARCH-AESTHETIC-MEDDEVICE-EXPORT-MARGIN", "symbol": "214450", "company_name": "파마리서치", "round": "R7", "loop": "77", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_CGM_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "case_type": "medical_device_export_reimbursement", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-AestheticMedicalDeviceExportMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C25 should allow aesthetic/regenerative medical-device positives when export channel reorder, approval/registration visibility, pricing and margin bridge are visible. PharmaResearch produced very large MFE with almost no entry-basis MAE, but later price pinning and post-peak drawdown require lifecycle local 4B if export/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export channel reorder, reimbursement/adoption, distributor inventory, installed-base utilization, pricing and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R7L77-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-BETA-FADE", "symbol": "099190", "company_name": "아이센스", "round": "R7", "loop": "77", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_CGM_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "case_type": "medical_device_export_reimbursement", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / CGMReimbursementExportBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C25 should not treat CGM/reimbursement or diabetes-device theme beta as durable Stage2 unless adoption, reimbursement coverage, distributor sell-through, export reorder and margin bridge are visible. i-SENS had only a small early MFE and then a high-MAE drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export channel reorder, reimbursement/adoption, distributor inventory, installed-base utilization, pricing and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R7L77-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-BETA-FADE", "symbol": "043150", "company_name": "바텍", "round": "R7", "loop": "77", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_CGM_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "case_type": "medical_device_export_reimbursement", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / DentalImagingExportBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C25 should not treat dental imaging/export-device beta as durable Stage2 unless export channel reorder, installed-base utilization, distributor inventory and margin bridge are visible. Vatech failed to generate meaningful MFE and then drifted lower, so it is a no-durable-Green/local-4B boundary.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export channel reorder, reimbursement/adoption, distributor inventory, installed-base utilization, pricing and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R7L77-C25-214450-PHARMARESEARCH-AESTHETIC-MEDDEVICE-EXPORT-MARGIN", "case_id": "R7L77-C25-214450-PHARMARESEARCH-AESTHETIC-MEDDEVICE-EXPORT-MARGIN", "symbol": "214450", "company_name": "파마리서치", "round": "R7", "loop": "77", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_CGM_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail", "trigger_type": "Stage2-Actionable-AestheticMedicalDeviceExportMarginBridgeWithLifecycle4B", "trigger_date": "2024-03-29", "entry_date": "2024-04-01", "entry_price": 99700.0, "evidence_available_at_that_date": "AESTHETIC_REJURAN_MEDICAL_DEVICE_EXPORT_CHANNEL_REORDER_PRICING_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:PHARMARESEARCH_2024_AESTHETIC_REJURAN_EXPORT_CHANNEL_REORDER_PRICING_MARGIN_BRIDGE", "stage2_evidence_fields": ["medical_device_export_or_reimbursement_candidate", "adoption_sellthrough_or_channel_reorder_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "distributor_inventory_installed_base_or_pricing_candidate"], "stage4b_evidence_fields": ["device_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214450/2024.csv", "profile_path": "atlas/symbol_profiles/214/214450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 49.95, "MFE_90D_pct": 57.87, "MFE_180D_pct": 138.72, "MAE_30D_pct": -1.1, "MAE_90D_pct": -1.1, "MAE_180D_pct": -1.1, "peak_date": "2024-10-22", "peak_price": 238000.0, "drawdown_after_peak_pct": -11.13, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_medical_device_peak_if_export_reimbursement_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_approval_failure_reimbursement_loss_distributor_issue_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C25 should allow aesthetic/regenerative medical-device positives when export channel reorder, approval/registration visibility, pricing and margin bridge are visible. PharmaResearch produced very large MFE with almost no entry-basis MAE, but later price pinning and post-peak drawdown require lifecycle local 4B if export/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C25_DEVICE_EXPORT_214450_2024-04-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L77-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-BETA-FADE", "case_id": "R7L77-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-BETA-FADE", "symbol": "099190", "company_name": "아이센스", "round": "R7", "loop": "77", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_CGM_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail", "trigger_type": "Stage2-FalsePositive / CGMReimbursementExportBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 24400.0, "evidence_available_at_that_date": "CGM_REIMBURSEMENT_EXPORT_THEME_WITH_WEAK_ADOPTION_SELLTHROUGH_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ISENS_2024_CGM_REIMBURSEMENT_EXPORT_ADOPTION_SELLTHROUGH_MARGIN_BRIDGE", "stage2_evidence_fields": ["medical_device_export_or_reimbursement_candidate", "adoption_sellthrough_or_channel_reorder_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "distributor_inventory_installed_base_or_pricing_candidate"], "stage4b_evidence_fields": ["device_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv", "profile_path": "atlas/symbol_profiles/099/099190.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.71, "MFE_90D_pct": 4.71, "MFE_180D_pct": 4.71, "MAE_30D_pct": -18.03, "MAE_90D_pct": -22.62, "MAE_180D_pct": -40.49, "peak_date": "2024-02-02", "peak_price": 25550.0, "drawdown_after_peak_pct": -43.17, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_medical_device_peak_if_export_reimbursement_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_approval_failure_reimbursement_loss_distributor_issue_margin_or_financing_break", "trigger_outcome_label": "counterexample_CGM_reimbursement_beta_local4b", "current_profile_verdict": "C25 should not treat CGM/reimbursement or diabetes-device theme beta as durable Stage2 unless adoption, reimbursement coverage, distributor sell-through, export reorder and margin bridge are visible. i-SENS had only a small early MFE and then a high-MAE drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C25_DEVICE_EXPORT_099190_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L77-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-BETA-FADE", "case_id": "R7L77-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-BETA-FADE", "symbol": "043150", "company_name": "바텍", "round": "R7", "loop": "77", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_CGM_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail", "trigger_type": "Stage2-FalsePositive / DentalImagingExportBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 32500.0, "evidence_available_at_that_date": "DENTAL_IMAGING_EXPORT_THEME_WITH_WEAK_REORDER_UTILIZATION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:VATECH_2024_DENTAL_IMAGING_EXPORT_REORDER_DISTRIBUTOR_UTILIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["medical_device_export_or_reimbursement_candidate", "adoption_sellthrough_or_channel_reorder_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "distributor_inventory_installed_base_or_pricing_candidate"], "stage4b_evidence_fields": ["device_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/043/043150/2024.csv", "profile_path": "atlas/symbol_profiles/043/043150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "MFE_180D_pct": 0.0, "MAE_30D_pct": -7.85, "MAE_90D_pct": -8.62, "MAE_180D_pct": -30.46, "peak_date": "2024-02-01", "peak_price": 32500.0, "drawdown_after_peak_pct": -30.46, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_medical_device_peak_if_export_reimbursement_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_approval_failure_reimbursement_loss_distributor_issue_margin_or_financing_break", "trigger_outcome_label": "counterexample_dental_device_export_beta_local4b", "current_profile_verdict": "C25 should not treat dental imaging/export-device beta as durable Stage2 unless export channel reorder, installed-base utilization, distributor inventory and margin bridge are visible. Vatech failed to generate meaningful MFE and then drifted lower, so it is a no-durable-Green/local-4B boundary.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C25_DEVICE_EXPORT_043150_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L77-C25-214450-PHARMARESEARCH-AESTHETIC-MEDDEVICE-EXPORT-MARGIN", "trigger_id": "TRG_R7L77-C25-214450-PHARMARESEARCH-AESTHETIC-MEDDEVICE-EXPORT-MARGIN", "symbol": "214450", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"device_export_score": 14, "reimbursement_adoption_score": 12, "channel_reorder_score": 14, "distributor_inventory_score": 12, "pricing_margin_score": 14, "relative_strength_score": 16, "execution_risk_score": 8, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"device_export_score": 16, "reimbursement_adoption_score": 14, "channel_reorder_score": 16, "distributor_inventory_score": 14, "pricing_margin_score": 16, "relative_strength_score": 15, "execution_risk_score": 9, "dilution_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["device_export_score", "reimbursement_adoption_score", "channel_reorder_score", "pricing_margin_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified export/channel reorder, reimbursement/adoption, distributor inventory, installed-base utilization, pricing and margin bridge; cap medical-device theme beta when evidence fails to refresh.", "MFE_90D_pct": 57.87, "MAE_90D_pct": -1.1, "score_return_alignment_label": "medical_device_export_positive_with_lifecycle_4b", "current_profile_verdict": "C25 should allow aesthetic/regenerative medical-device positives when export channel reorder, approval/registration visibility, pricing and margin bridge are visible. PharmaResearch produced very large MFE with almost no entry-basis MAE, but later price pinning and post-peak drawdown require lifecycle local 4B if export/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L77-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-BETA-FADE", "trigger_id": "TRG_R7L77-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-BETA-FADE", "symbol": "099190", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"device_export_score": 5, "reimbursement_adoption_score": 3, "channel_reorder_score": 3, "distributor_inventory_score": 2, "pricing_margin_score": 2, "relative_strength_score": 3, "execution_risk_score": 20, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 47, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"device_export_score": 3, "reimbursement_adoption_score": 1, "channel_reorder_score": 2, "distributor_inventory_score": 1, "pricing_margin_score": 1, "relative_strength_score": 2, "execution_risk_score": 22, "dilution_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 35, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["device_export_score", "reimbursement_adoption_score", "channel_reorder_score", "pricing_margin_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified export/channel reorder, reimbursement/adoption, distributor inventory, installed-base utilization, pricing and margin bridge; cap medical-device theme beta when evidence fails to refresh.", "MFE_90D_pct": 4.71, "MAE_90D_pct": -22.62, "score_return_alignment_label": "false_positive_device_theme_bridge_gap", "current_profile_verdict": "C25 should not treat CGM/reimbursement or diabetes-device theme beta as durable Stage2 unless adoption, reimbursement coverage, distributor sell-through, export reorder and margin bridge are visible. i-SENS had only a small early MFE and then a high-MAE drawdown path."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L77-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-BETA-FADE", "trigger_id": "TRG_R7L77-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-BETA-FADE", "symbol": "043150", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"device_export_score": 5, "reimbursement_adoption_score": 3, "channel_reorder_score": 3, "distributor_inventory_score": 2, "pricing_margin_score": 2, "relative_strength_score": 3, "execution_risk_score": 20, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 47, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"device_export_score": 3, "reimbursement_adoption_score": 1, "channel_reorder_score": 2, "distributor_inventory_score": 1, "pricing_margin_score": 1, "relative_strength_score": 2, "execution_risk_score": 22, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 35, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["device_export_score", "reimbursement_adoption_score", "channel_reorder_score", "pricing_margin_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified export/channel reorder, reimbursement/adoption, distributor inventory, installed-base utilization, pricing and margin bridge; cap medical-device theme beta when evidence fails to refresh.", "MFE_90D_pct": 0.0, "MAE_90D_pct": -8.62, "score_return_alignment_label": "false_positive_device_theme_bridge_gap", "current_profile_verdict": "C25 should not treat dental imaging/export-device beta as durable Stage2 unless export channel reorder, installed-base utilization, distributor inventory and margin bridge are visible. Vatech failed to generate meaningful MFE and then drifted lower, so it is a no-durable-Green/local-4B boundary."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R7", "loop": 77, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_CGM_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "current_profile_error_count": 2, "diversity_score_summary": "+3 C25 medical-device symbols outside top-covered 338220/214150/145720/228670/328130 set, +3 aesthetic/CGM/dental-imaging trigger families, +1 export-margin positive, +2 device theme local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R7", "loop": 77, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "axis": "aesthetic_CGM_dental_device_export_reimbursement_margin_bridge_vs_device_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C25 should split verified medical-device export/reimbursement margin bridges from generic device theme beta. Stage2 requires export channel reorder, reimbursement/adoption, distributor sell-through or installed-base utilization, pricing and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["214450", "099190", "043150"], "share_count_validation_required": ["214450", "099190"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": 77, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C25 needs export/reimbursement/adoption/margin proof. PharmaResearch shows an aesthetic medical-device export-margin positive after source repair; i-SENS and Vatech show CGM/dental device theme beta failing to become durable Stage2 when adoption, distributor sell-through and margin bridge are absent."}
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
214450:
  name = 파마리서치 from 2021-04-13, 파마리서치프로덕트 before that
  corporate_action_candidate_dates = none
  selected window = 2024-04-01~D+180
  contamination = false
  share_count_change_inside_window = true → coding-agent validation required

099190:
  corporate_action_candidate_dates = 2015-10-02, 2023-03-14, 2023-04-10
  selected window = 2024-02-01~D+180
  contamination = false
  share_count_change_inside_window = true → coding-agent validation required

043150:
  corporate_action_candidate_dates = 2010-09-02
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C25 rows are source_proxy_only / evidence_url_pending.
214450 and 099190 also require share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C25 rule-shape discovery,
but coding-agent promotion requires non-proxy export channel reorder, reimbursement/adoption, distributor inventory, installed-base utilization, pricing and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R7/C25 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and two rows need share-count validation.

Candidate axis:
aesthetic_CGM_dental_device_export_reimbursement_margin_bridge_vs_device_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 214450, 099190 and 043150.
4. Validate 214450 and 099190 share-count changes inside the selected window.
5. Keep generic C25 medical-device/export weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - medical device / diagnostic / aesthetic product exposure is explicit,
   - approval, reimbursement, export channel reorder or adoption evidence is visible,
   - distributor sell-through or installed-base utilization bridge exists,
   - pricing and margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is medical-device theme beta only,
   - approval/reimbursement/adoption/channel/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -30~35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price approval failure, reimbursement loss, distributor/channel issue, installed-base slowdown, margin collapse, financing or regulatory evidence.
9. Emit before/after diagnostics and reject if verified low-MAE export/margin positives are overblocked.
```

---

## Final round state

```text
completed_round = R7
completed_loop = 77
next_round = R8
next_loop = 77
round_schedule_status = valid
round_sector_consistency = pass
```

