# E2R Stock-Web v12 Residual Research — R7 Loop 75 / L7 / C25

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R7",
  "scheduled_loop": 75,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 75,
  "computed_next_round": "R8",
  "computed_next_loop": 75,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "fine_archetype_id": "IVD_CGM_XRAY_EXPORT_REIMBURSEMENT_CHANNEL_BRIDGE_VS_DEVICE_THEME_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "medical_device_export_reimbursement_guardrail",
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

Previous completed state in this interactive run: R6 / loop 75.

Therefore:

```text
scheduled_round = R7
scheduled_loop = 75
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
computed_next_round = R8
computed_next_loop = 75
```

R7 was routed to C25 because loop 74 used C24 and C25 is thinner than C23.  
This file tests medical device export/reimbursement/channel bridges outside the top-covered AI diagnosis, aesthetic-device and implant set.

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
206640 / 바디텍메드 / IVD export-channel reagent margin bridge
099190 / 아이센스 / CGM reimbursement/adoption beta fade
214680 / 디알텍 / X-ray detector export/OEM beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
099190 and 214680 show share-count changes inside the selected window and require coding-agent validation before runtime promotion.
```

## Research thesis

C25 is not “medical-device stock went up.”

The mechanism must be:

```text
device / diagnosis / reimbursement attention
→ export or OEM channel
→ installed base / prescription refill / reagent pull-through
→ utilization and margin conversion
→ durable rerating
```

A device sale is the razor.  
The installed base, refill, reagent and reimbursement cadence are the blades.

---

## Case 1 — Positive with lifecycle 4B: 206640 / 바디텍메드

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is IVD export channel reorder, installed base, reagent pull-through, utilization and margin bridge evidence.

```text
evidence_family = IVD_DIAGNOSTIC_DEVICE_EXPORT_CHANNEL_REORDER_INSTRUMENT_REAGENT_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-03-19
entry_date = 2024-03-20
entry_price = 14,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/206/206640/2024.csv`:

```text
2024-03-20,14000,16000,14000,15600
2024-07-24,18500,19570,18340,19300
2024-08-19,19700,21050,19560,20550
2024-10-22,13680,13800,13350,13660
2024-10-24,15600,16600,15310,16000
```

### Backtest

```text
MFE_30D  = +14.29%
MAE_30D  = -4.29%
MFE_90D  = +50.36%
MAE_90D  = -4.29%
MFE_180D = +50.36%
MAE_180D = -4.64%
peak_180 = 21,050 on 2024-08-19
trough_180 = 13,350 on 2024-10-22
peak_to_later_drawdown = -36.58%
```

### Interpretation

This is the useful C25 positive row.  
The entry-basis risk was controlled and MFE expanded over months.

But C25 should still require source repair:

```text
export/OEM channel
installed base
reagent pull-through
utilization
margin bridge
```

The post-peak drawdown means lifecycle local 4B should activate if export/reagent evidence fades.

---

## Case 2 — Counterexample / local 4B: 099190 / 아이센스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

This row tests CGM reimbursement/adoption beta without durable prescription refill, reimbursement coverage, utilization and margin bridge.

```text
evidence_family = CGM_REIMBURSEMENT_LAUNCH_ADOPTION_BETA_WITH_WEAK_UTILIZATION_MARGIN_BRIDGE
case_role = counterexample_reimbursement_beta_local4b
trigger_date = 2024-01-10
entry_date = 2024-01-11
entry_price = 29,950
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv`:

```text
2024-01-11,29950,30200,29150,30050
2024-01-12,30350,30400,28800,28800
2024-02-07,21650,21900,20550,21000
2024-08-05,17480,17520,15500,15990
2024-09-06,15340,15520,15020,15090
2024-10-18,20500,21000,19910,20450
```

### Backtest

```text
MFE_30D  = +1.50%
MAE_30D  = -31.39%
MFE_90D  = +1.50%
MAE_90D  = -35.26%
MFE_180D = +1.50%
MAE_180D = -49.85%
peak_180 = 30,400 on 2024-01-12
trough_180 = 15,020 on 2024-09-06
peak_to_later_drawdown = -50.59%
```

### Interpretation

This is a reimbursement/adoption false positive.  
CGM or reimbursement attention can create a headline bid, but it does not become C25 Stage2 unless adoption and refill economics are visible.

Correct treatment:

```text
launch/reimbursement beta
→ no utilization/refill/margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 214680 / 디알텍

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

This row tests X-ray detector export/OEM order beta without enough named order and margin refresh.

```text
evidence_family = XRAY_DETECTOR_EXPORT_OEM_ORDER_REIMBURSEMENT_BETA_WITH_WEAK_MARGIN_REFRESH
case_role = counterexample_device_export_local4b
trigger_date = 2024-03-28
entry_date = 2024-03-29
entry_price = 3,345
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/214/214680/2024.csv`:

```text
2024-03-29,3345,3830,3260,3475
2024-07-30,3830,4090,3795,3870
2024-08-05,3490,3490,2840,2975
2024-09-06,2930,2955,2760,2765
2024-10-07,3080,3460,3020,3275
```

### Backtest

```text
MFE_30D  = +14.50%
MAE_30D  = -11.81%
MFE_90D  = +22.27%
MAE_90D  = -12.26%
MFE_180D = +22.27%
MAE_180D = -17.49%
peak_180 = 4,090 on 2024-07-30
trough_180 = 2,760 on 2024-09-06
peak_to_later_drawdown = -32.52%
```

### Interpretation

This is a device-export beta row.  
It was tradable, but not durable enough to be Green without export/OEM order and margin bridge.

It is not hard 4C. It is local 4B-watch unless non-price order, reimbursement or margin evidence confirms a real break.

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
share_count_validation_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C25_medical_device_weight = true
do_not_treat_all_reimbursement_or_device_export_MFE_as_Green = true
do_not_convert_device_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
IVD_CGM_XRAY_EXPORT_REIMBURSEMENT_CHANNEL_BRIDGE_VS_DEVICE_THEME_BETA_FADE
```

This fine archetype covers:

```text
1. IVD export/channel installed-base and reagent bridge → Stage2 possible after source repair
2. CGM reimbursement/adoption beta without refill/utilization bridge → false Stage2 / local 4B
3. X-ray detector export/OEM beta without order/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R7L75-C25-206640-BODITECH-IVD-EXPORT-CHANNEL-MARGIN-BRIDGE", "symbol": "206640", "company_name": "바디텍메드", "round": "R7", "loop": "75", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "IVD_CGM_XRAY_EXPORT_REIMBURSEMENT_CHANNEL_BRIDGE_VS_DEVICE_THEME_BETA_FADE", "case_type": "medical_device_export_reimbursement", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-IVDExportChannelMarginBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C25 should allow Stage2 when IVD device export/channel reorder converts into installed base, reagent pull-through, utilization and margin bridge. Boditech Med produced high MFE with controlled entry-basis MAE, but later drawdown requires lifecycle local 4B if export/reagent bridge fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export/OEM channel, reimbursement, installed base, refill/reagent pull-through, utilization and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R7L75-C25-099190-ISENS-CGM-REIMBURSEMENT-ADOPTION-BETA-FADE", "symbol": "099190", "company_name": "아이센스", "round": "R7", "loop": "75", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "IVD_CGM_XRAY_EXPORT_REIMBURSEMENT_CHANNEL_BRIDGE_VS_DEVICE_THEME_BETA_FADE", "case_type": "medical_device_export_reimbursement", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / CGMReimbursementAdoptionBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C25 should not treat CGM/reimbursement or launch attention as durable Stage2 unless adoption, prescription refill, reimbursement coverage, utilization and margin evidence refreshes. i-SENS had only small initial MFE and then severe MAE/drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export/OEM channel, reimbursement, installed base, refill/reagent pull-through, utilization and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R7L75-C25-214680-DRTECH-XRAY-DETECTOR-EXPORT-ORDER-BETA-FADE", "symbol": "214680", "company_name": "디알텍", "round": "R7", "loop": "75", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "IVD_CGM_XRAY_EXPORT_REIMBURSEMENT_CHANNEL_BRIDGE_VS_DEVICE_THEME_BETA_FADE", "case_type": "medical_device_export_reimbursement", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / XrayDetectorExportOrderBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C25 should not treat X-ray detector/export/OEM order beta as durable Stage2 unless named export orders, OEM channel expansion, reimbursement or margin bridge is visible. DRTech had tradable MFE but later drawdown opened enough to require local 4B-watch.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export/OEM channel, reimbursement, installed base, refill/reagent pull-through, utilization and margin evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R7L75-C25-206640-BODITECH-IVD-EXPORT-CHANNEL-MARGIN-BRIDGE", "case_id": "R7L75-C25-206640-BODITECH-IVD-EXPORT-CHANNEL-MARGIN-BRIDGE", "symbol": "206640", "company_name": "바디텍메드", "round": "R7", "loop": "75", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "IVD_CGM_XRAY_EXPORT_REIMBURSEMENT_CHANNEL_BRIDGE_VS_DEVICE_THEME_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail", "trigger_type": "Stage2-Actionable-IVDExportChannelMarginBridge", "trigger_date": "2024-03-19", "entry_date": "2024-03-20", "entry_price": 14000.0, "evidence_available_at_that_date": "IVD_DIAGNOSTIC_DEVICE_EXPORT_CHANNEL_REORDER_INSTRUMENT_REAGENT_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:BODITECH_MED_2024_IVD_DIAGNOSTIC_DEVICE_EXPORT_CHANNEL_INSTALLED_BASE_REAGENT_MARGIN_BRIDGE", "stage2_evidence_fields": ["medical_device_export_candidate", "reimbursement_or_oem_channel_candidate", "installed_base_or_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "utilization_reagent_refill_or_order_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown", "reimbursement_or_adoption_beta_risk"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/206/206640/2024.csv", "profile_path": "atlas/symbol_profiles/206/206640.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.29, "MFE_90D_pct": 50.36, "MFE_180D_pct": 50.36, "MAE_30D_pct": -4.29, "MAE_90D_pct": -4.29, "MAE_180D_pct": -4.64, "peak_date": "2024-08-19", "peak_price": 21050.0, "drawdown_after_peak_pct": -36.58, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_device_export_or_reimbursement_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_reimbursement_adoption_utilization_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C25 should allow Stage2 when IVD device export/channel reorder converts into installed base, reagent pull-through, utilization and margin bridge. Boditech Med produced high MFE with controlled entry-basis MAE, but later drawdown requires lifecycle local 4B if export/reagent bridge fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C25_MED_DEVICE_206640_2024-03-20", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L75-C25-099190-ISENS-CGM-REIMBURSEMENT-ADOPTION-BETA-FADE", "case_id": "R7L75-C25-099190-ISENS-CGM-REIMBURSEMENT-ADOPTION-BETA-FADE", "symbol": "099190", "company_name": "아이센스", "round": "R7", "loop": "75", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "IVD_CGM_XRAY_EXPORT_REIMBURSEMENT_CHANNEL_BRIDGE_VS_DEVICE_THEME_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail", "trigger_type": "Stage2-FalsePositive / CGMReimbursementAdoptionBetaFade", "trigger_date": "2024-01-10", "entry_date": "2024-01-11", "entry_price": 29950.0, "evidence_available_at_that_date": "CGM_REIMBURSEMENT_LAUNCH_ADOPTION_BETA_WITH_WEAK_UTILIZATION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ISENS_2024_CGM_REIMBURSEMENT_LAUNCH_ADOPTION_PRESCRIPTION_REFILL_MARGIN_BRIDGE", "stage2_evidence_fields": ["medical_device_export_candidate", "reimbursement_or_oem_channel_candidate", "installed_base_or_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "utilization_reagent_refill_or_order_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown", "reimbursement_or_adoption_beta_risk"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv", "profile_path": "atlas/symbol_profiles/099/099190.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.5, "MFE_90D_pct": 1.5, "MFE_180D_pct": 1.5, "MAE_30D_pct": -31.39, "MAE_90D_pct": -35.26, "MAE_180D_pct": -49.85, "peak_date": "2024-01-12", "peak_price": 30400.0, "drawdown_after_peak_pct": -50.59, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_device_export_or_reimbursement_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_reimbursement_adoption_utilization_or_margin_break", "trigger_outcome_label": "counterexample_reimbursement_beta_local4b", "current_profile_verdict": "C25 should not treat CGM/reimbursement or launch attention as durable Stage2 unless adoption, prescription refill, reimbursement coverage, utilization and margin evidence refreshes. i-SENS had only small initial MFE and then severe MAE/drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C25_MED_DEVICE_099190_2024-01-11", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L75-C25-214680-DRTECH-XRAY-DETECTOR-EXPORT-ORDER-BETA-FADE", "case_id": "R7L75-C25-214680-DRTECH-XRAY-DETECTOR-EXPORT-ORDER-BETA-FADE", "symbol": "214680", "company_name": "디알텍", "round": "R7", "loop": "75", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "IVD_CGM_XRAY_EXPORT_REIMBURSEMENT_CHANNEL_BRIDGE_VS_DEVICE_THEME_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail", "trigger_type": "Stage2-FalsePositive / XrayDetectorExportOrderBetaFade", "trigger_date": "2024-03-28", "entry_date": "2024-03-29", "entry_price": 3345.0, "evidence_available_at_that_date": "XRAY_DETECTOR_EXPORT_OEM_ORDER_REIMBURSEMENT_BETA_WITH_WEAK_MARGIN_REFRESH", "evidence_source": "source_proxy_manual_verification_required:DRTECH_2024_XRAY_DETECTOR_EXPORT_OEM_ORDER_CHANNEL_MARGIN_BRIDGE", "stage2_evidence_fields": ["medical_device_export_candidate", "reimbursement_or_oem_channel_candidate", "installed_base_or_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "utilization_reagent_refill_or_order_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown", "reimbursement_or_adoption_beta_risk"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214680/2024.csv", "profile_path": "atlas/symbol_profiles/214/214680.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.5, "MFE_90D_pct": 22.27, "MFE_180D_pct": 22.27, "MAE_30D_pct": -11.81, "MAE_90D_pct": -12.26, "MAE_180D_pct": -17.49, "peak_date": "2024-07-30", "peak_price": 4090.0, "drawdown_after_peak_pct": -32.52, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_device_export_or_reimbursement_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_reimbursement_adoption_utilization_or_margin_break", "trigger_outcome_label": "counterexample_device_export_local4b", "current_profile_verdict": "C25 should not treat X-ray detector/export/OEM order beta as durable Stage2 unless named export orders, OEM channel expansion, reimbursement or margin bridge is visible. DRTech had tradable MFE but later drawdown opened enough to require local 4B-watch.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C25_MED_DEVICE_214680_2024-03-29", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L75-C25-206640-BODITECH-IVD-EXPORT-CHANNEL-MARGIN-BRIDGE", "trigger_id": "TRG_R7L75-C25-206640-BODITECH-IVD-EXPORT-CHANNEL-MARGIN-BRIDGE", "symbol": "206640", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"export_channel_score": 14, "reimbursement_access_score": 5, "installed_base_or_oem_score": 13, "utilization_refill_reagent_score": 13, "margin_bridge_score": 12, "relative_strength_score": 14, "execution_risk_score": 6, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"export_channel_score": 16, "reimbursement_access_score": 4, "installed_base_or_oem_score": 15, "utilization_refill_reagent_score": 15, "margin_bridge_score": 14, "relative_strength_score": 13, "execution_risk_score": 7, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow candidate after source repair + lifecycle 4B", "changed_components": ["export_channel_score", "installed_base_or_oem_score", "utilization_refill_reagent_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified device export/OEM, reimbursement, installed-base, refill/reagent pull-through and margin bridge; cap device-theme beta when adoption/utilization evidence fails to refresh.", "MFE_90D_pct": 50.36, "MAE_90D_pct": -4.29, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C25 should allow Stage2 when IVD device export/channel reorder converts into installed base, reagent pull-through, utilization and margin bridge. Boditech Med produced high MFE with controlled entry-basis MAE, but later drawdown requires lifecycle local 4B if export/reagent bridge fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L75-C25-099190-ISENS-CGM-REIMBURSEMENT-ADOPTION-BETA-FADE", "trigger_id": "TRG_R7L75-C25-099190-ISENS-CGM-REIMBURSEMENT-ADOPTION-BETA-FADE", "symbol": "099190", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"export_channel_score": 6, "reimbursement_access_score": 11, "installed_base_or_oem_score": 5, "utilization_refill_reagent_score": 3, "margin_bridge_score": 2, "relative_strength_score": 6, "execution_risk_score": 17, "dilution_or_sharecount_validation_risk": 6, "source_confidence_score": 2}, "weighted_score_before": 51, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"export_channel_score": 4, "reimbursement_access_score": 9, "installed_base_or_oem_score": 3, "utilization_refill_reagent_score": 2, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 20, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_after": 39, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["export_channel_score", "installed_base_or_oem_score", "utilization_refill_reagent_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified device export/OEM, reimbursement, installed-base, refill/reagent pull-through and margin bridge; cap device-theme beta when adoption/utilization evidence fails to refresh.", "MFE_90D_pct": 1.5, "MAE_90D_pct": -35.26, "score_return_alignment_label": "false_positive_device_export_reimbursement_bridge_gap", "current_profile_verdict": "C25 should not treat CGM/reimbursement or launch attention as durable Stage2 unless adoption, prescription refill, reimbursement coverage, utilization and margin evidence refreshes. i-SENS had only small initial MFE and then severe MAE/drawdown."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L75-C25-214680-DRTECH-XRAY-DETECTOR-EXPORT-ORDER-BETA-FADE", "trigger_id": "TRG_R7L75-C25-214680-DRTECH-XRAY-DETECTOR-EXPORT-ORDER-BETA-FADE", "symbol": "214680", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"export_channel_score": 6, "reimbursement_access_score": 5, "installed_base_or_oem_score": 5, "utilization_refill_reagent_score": 3, "margin_bridge_score": 2, "relative_strength_score": 6, "execution_risk_score": 17, "dilution_or_sharecount_validation_risk": 6, "source_confidence_score": 2}, "weighted_score_before": 51, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"export_channel_score": 4, "reimbursement_access_score": 4, "installed_base_or_oem_score": 3, "utilization_refill_reagent_score": 2, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 20, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_after": 39, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["export_channel_score", "installed_base_or_oem_score", "utilization_refill_reagent_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified device export/OEM, reimbursement, installed-base, refill/reagent pull-through and margin bridge; cap device-theme beta when adoption/utilization evidence fails to refresh.", "MFE_90D_pct": 22.27, "MAE_90D_pct": -12.26, "score_return_alignment_label": "false_positive_device_export_reimbursement_bridge_gap", "current_profile_verdict": "C25 should not treat X-ray detector/export/OEM order beta as durable Stage2 unless named export orders, OEM channel expansion, reimbursement or margin bridge is visible. DRTech had tradable MFE but later drawdown opened enough to require local 4B-watch."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R7", "loop": 75, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "IVD_CGM_XRAY_EXPORT_REIMBURSEMENT_CHANNEL_BRIDGE_VS_DEVICE_THEME_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C25 medical-device symbols outside top-covered AI/imaging/implant set, +3 IVD/CGM/X-ray trigger families, +1 export-channel positive, +2 reimbursement/device beta fade local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R7", "loop": 75, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "axis": "ivd_cgm_xray_export_reimbursement_channel_bridge_vs_device_theme_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C25 should split verified medical-device export/reimbursement channel bridges from device-theme beta. Stage2 requires OEM/channel expansion, reimbursement access, installed base, prescription/refill/reagent pull-through, utilization or margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["206640", "099190", "214680"], "share_count_validation_required": ["099190", "214680"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": 75, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C25 needs export/reimbursement utilization proof. Boditech Med shows an IVD export/channel positive after source repair; i-SENS and DRTech show CGM/X-ray device-theme beta fading into local 4B when adoption, reimbursement, OEM or margin bridge is absent."}
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
206640:
  corporate_action_candidate_dates = 2015-09-11, 2016-02-12
  selected window = 2024-03-20~D+180
  contamination = false

099190:
  corporate_action_candidate_dates = 2015-10-02, 2023-03-14, 2023-04-10
  selected window = 2024-01-11~D+180
  contamination = false
  share_count_change_inside_window = true → coding-agent validation required

214680:
  corporate_action_candidate_dates = 2016-12-05
  selected window = 2024-03-29~D+180
  contamination = false
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C25 rows are source_proxy_only / evidence_url_pending.
099190 and 214680 also require share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C25 rule-shape discovery,
but coding-agent promotion requires non-proxy export/OEM channel, reimbursement, installed base, refill/reagent pull-through, utilization and margin evidence.
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
ivd_cgm_xray_export_reimbursement_channel_bridge_vs_device_theme_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 206640, 099190 and 214680.
4. Validate 099190 and 214680 share-count changes inside the selected window.
5. Keep generic C25 medical-device weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - export/OEM channel expansion or reimbursement access is explicit,
   - installed base or prescription/refill/reagent pull-through is visible,
   - utilization and margin bridge exists,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is medical-device/reimbursement/export beta only,
   - order/adoption/utilization or margin evidence is weak/stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -30~35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price order loss, reimbursement failure, adoption miss, utilization collapse, financing or margin break.
9. Emit before/after diagnostics and reject if verified IVD installed-base/reagent positives are overblocked.
```

---

## Final round state

```text
completed_round = R7
completed_loop = 75
next_round = R8
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

