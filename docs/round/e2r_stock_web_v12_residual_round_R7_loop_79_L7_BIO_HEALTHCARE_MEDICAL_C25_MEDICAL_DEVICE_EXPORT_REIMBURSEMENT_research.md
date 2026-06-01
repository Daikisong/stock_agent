# E2R Stock-Web v12 Residual Research — R7 Loop 79 / L7 / C25

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R7",
  "scheduled_loop": 79,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 79,
  "computed_next_round": "R8",
  "computed_next_loop": 79,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "fine_archetype_id": "AESTHETIC_DEVICE_CGM_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "medical_device_export_reimbursement_guardrail",
    "aesthetic_device_CGM_export_reimbursement_bridge",
    "device_theme_reimbursement_revenue_margin_fade_boundary",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "share_count_and_status_validation_queue_creation"
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

Previous completed state in this interactive run: R6 / loop 79.

Therefore:

```text
scheduled_round = R7
scheduled_loop = 79
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
computed_next_round = R8
computed_next_loop = 79
```

R7 was routed to C25 because loop 78 used C24 and C25 still has under-covered device/export/reimbursement residual space.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C25 concentration in:

```text
338220, 214150, 145720, 228670, 328130
```

This run uses three different symbols:

```text
336570 / 원텍 / aesthetic device export and distributor-reorder lifecycle
287410 / 제이시스메디칼 / aesthetic device export / strategic-event commercialization bridge
099190 / 아이센스 / CGM reimbursement/export theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
287410 and 099190 show share-count changes inside the selected window and require coding-agent validation.
287410 also has inactive_or_delisted_like status inference / last-date caveat and requires status validation before runtime promotion.
```

## Research thesis

C25 is not “의료기기 수출 기대감이 있다.”

The mechanism must pass through:

```text
medical device export / reimbursement / approval attention
→ adoption or installed-base expansion
→ distributor reorder or prescription/usage conversion
→ recurring revenue / consumables / service
→ margin bridge
→ durable rerating
```

의료기기 테마는 장비 출고 사진이 아니다.  
C25가 보려는 것은 장비가 병원에 깔리고, 계속 쓰이고, 소모품과 서비스 매출로 반복되며, 마진으로 돌아오는지다.

---

## Case 1 — Lifecycle positive: 336570 / 원텍

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is export channel, distributor reorder, installed-base utilization, recurring revenue and margin bridge evidence.

```text
evidence_family = AESTHETIC_ENERGY_BASED_DEVICE_EXPORT_DISTRIBUTOR_REORDER_REVENUE_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 7,830
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/336/336570/2024.csv`:

```text
2024-02-01,7830,7970,7650,7870
2024-02-16,8900,9400,8860,9210
2024-04-03,8550,9200,8530,8900
2024-04-19,11160,11850,11000,11570
2024-04-22,11580,12000,10690,10860
2024-05-29,8030,8030,7350,7540
2024-08-26,5670,5730,5560,5650
```

### Backtest

```text
MFE_30D  = +20.05%
MAE_30D  = -2.94%
MFE_90D  = +53.26%
MAE_90D  = -6.13%
MFE_180D = +53.26%
MAE_180D = -28.99%
peak_180 = 12,000 on 2024-04-22
trough_180 = 5,560 on 2024-08-26
peak_to_later_drawdown = -53.67%
```

### Interpretation

This is a C25 lifecycle positive.  
The MFE was large, but the post-peak drawdown means export/reorder/margin evidence must refresh.

Correct treatment:

```text
verified export / distributor reorder / installed-base / margin bridge → Stage2 possible
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Positive with status caveat: 287410 / 제이시스메디칼

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
status_validation_required = true
source_repair_required = true
```

The source-repair task is device export/commercialization, distributor channel, installed base, strategic transaction context, revenue and margin bridge evidence.

```text
evidence_family = AESTHETIC_DEVICE_EXPORT_DISTRIBUTION_STRATEGIC_TRANSACTION_REVENUE_MARGIN_BRIDGE
case_role = positive_with_status_validation_and_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 8,550
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/287/287410/2024.csv`:

```text
2024-02-01,8550,8630,8300,8380
2024-03-07,7480,7650,7420,7520
2024-04-19,12410,12650,11450,12020
2024-05-21,11770,12930,11440,12360
2024-06-10,12810,12840,12640,12760
2024-08-16,12940,13800,12910,12920
2024-08-21,12980,13010,12740,12750
```

### Backtest

```text
MFE_30D  = +4.91%
MAE_30D  = -13.22%
MFE_90D  = +51.23%
MAE_90D  = -13.22%
MFE_180D = +61.40%
MAE_180D = -13.22%
peak_180 = 13,800 on 2024-08-16
trough_180 = 7,420 on 2024-03-07
peak_to_later_drawdown = -7.68%
```

### Interpretation

This is a C25 positive but it is not a clean ordinary trading row.  
The price path is stabilized by a strategic/status event, so coding-agent ingestion must validate status and share-count treatment.

Correct treatment:

```text
verified export / installed-base / strategic commercial bridge → Stage2 possible
status and share-count validation first
bridge stale or status contaminated → do not ingest blindly
```

---

## Case 3 — Counterexample / local 4B: 099190 / 아이센스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

This row tests CGM reimbursement/export beta without enough adoption, recurring revenue and margin bridge.

```text
evidence_family = CGM_REIMBURSEMENT_EXPORT_THEME_WITH_WEAK_ADOPTION_REVENUE_MARGIN_BRIDGE
case_role = counterexample_CGM_reimbursement_export_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 24,400
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv`:

```text
2024-02-01,24400,24500,23200,23750
2024-02-02,24000,25550,24000,25200
2024-02-07,21650,21900,20550,21000
2024-03-27,20700,20950,19620,19760
2024-04-11,19300,19650,18880,19320
2024-08-05,17480,17520,15500,15990
2024-09-09,14820,15290,14520,15050
```

### Backtest

```text
MFE_30D  = +4.71%
MAE_30D  = -15.78%
MFE_90D  = +4.71%
MAE_90D  = -22.62%
MFE_180D = +4.71%
MAE_180D = -40.49%
peak_180 = 25,550 on 2024-02-02
trough_180 = 14,520 on 2024-09-09
peak_to_later_drawdown = -43.17%
```

### Interpretation

This is a C25 false-positive boundary.  
CGM reimbursement/export theme beta did not validate durable adoption or recurring revenue rerating.

Correct treatment:

```text
CGM reimbursement/export beta
→ no verified adoption / recurring revenue / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
share_count_validation_guard = strengthen
status_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C25_device_export_weight = true
do_not_treat_all_device_export_or_reimbursement_MFE_as_Green = true
do_not_ingest_status_caveat_rows_without_validation = true
do_not_convert_device_drawdown_to_hard_4C_without_non_price_reimbursement_export_adoption_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
AESTHETIC_DEVICE_CGM_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_THEME_FADE
```

This fine archetype covers:

```text
1. aesthetic device export / distributor reorder bridge → Stage2 possible after source repair
2. device export / strategic event bridge → Stage2 possible only after status validation
3. CGM reimbursement/export beta without adoption/revenue bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R7L79-C25-336570-WONTECH-AESTHETIC-DEVICE-EXPORT-MARGIN-LIFECYCLE", "symbol": "336570", "company_name": "원텍", "round": "R7", "loop": "79", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_CGM_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_THEME_FADE", "case_type": "medical_device_export_reimbursement", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-AestheticDeviceExportMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C25 should allow medical-aesthetic device positives when export demand, distributor reorder, installed-base utilization, consumables/service revenue and margin bridge are visible. Wontech produced large MFE, then a high post-peak drawdown, so it needs lifecycle 4B if export/reorder/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export/reimbursement/adoption/installed-base/revenue/margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R7L79-C25-287410-JEISYS-MEDICAL-AESTHETIC-DEVICE-STRATEGIC-EVENT", "symbol": "287410", "company_name": "제이시스메디칼", "round": "R7", "loop": "79", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_CGM_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_THEME_FADE", "case_type": "medical_device_export_reimbursement", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-AestheticDeviceExportStrategicEventBridgeWithStatusCaveat", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C25 should protect aesthetic-device export/commercialization positives when export channel, installed-base, consumables, distributor reorder, revenue and margin bridge are visible. Jeisys Medical produced strong MFE and later a stabilized strategic-event price path, but status/delisting-like caveat requires validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export/reimbursement/adoption/installed-base/revenue/margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R7L79-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-THEME-FADE", "symbol": "099190", "company_name": "아이센스", "round": "R7", "loop": "79", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_CGM_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_THEME_FADE", "case_type": "medical_device_export_reimbursement", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / CGMReimbursementExportThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C25 should not treat CGM reimbursement/export theme beta as durable Stage2 unless reimbursement coverage, prescription/adoption, distributor revenue, recurring consumables and margin bridge are visible. i-SENS produced only small early MFE and then a deep MAE path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export/reimbursement/adoption/installed-base/revenue/margin evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R7L79-C25-336570-WONTECH-AESTHETIC-DEVICE-EXPORT-MARGIN-LIFECYCLE", "case_id": "R7L79-C25-336570-WONTECH-AESTHETIC-DEVICE-EXPORT-MARGIN-LIFECYCLE", "symbol": "336570", "company_name": "원텍", "round": "R7", "loop": "79", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_CGM_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail", "trigger_type": "Stage2-Actionable-AestheticDeviceExportMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7830.0, "evidence_available_at_that_date": "AESTHETIC_ENERGY_BASED_DEVICE_EXPORT_DISTRIBUTOR_REORDER_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:WONTECH_2024_AESTHETIC_DEVICE_EXPORT_DISTRIBUTOR_REORDER_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["medical_device_export_or_reimbursement_candidate", "adoption_or_installed_base_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "distributor_reorder_or_recurring_revenue_candidate"], "stage4b_evidence_fields": ["medical_device_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336570/2024.csv", "profile_path": "atlas/symbol_profiles/336/336570.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.05, "MFE_90D_pct": 53.26, "MFE_180D_pct": 53.26, "MAE_30D_pct": -2.94, "MAE_90D_pct": -6.13, "MAE_180D_pct": -28.99, "peak_date": "2024-04-22", "peak_price": 12000.0, "drawdown_after_peak_pct": -53.67, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_device_peak_if_export_reimbursement_adoption_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reimbursement_failure_export_channel_loss_adoption_collapse_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C25 should allow medical-aesthetic device positives when export demand, distributor reorder, installed-base utilization, consumables/service revenue and margin bridge are visible. Wontech produced large MFE, then a high post-peak drawdown, so it needs lifecycle 4B if export/reorder/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_status_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C25_MED_DEVICE_336570_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L79-C25-287410-JEISYS-MEDICAL-AESTHETIC-DEVICE-STRATEGIC-EVENT", "case_id": "R7L79-C25-287410-JEISYS-MEDICAL-AESTHETIC-DEVICE-STRATEGIC-EVENT", "symbol": "287410", "company_name": "제이시스메디칼", "round": "R7", "loop": "79", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_CGM_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail", "trigger_type": "Stage2-Actionable-AestheticDeviceExportStrategicEventBridgeWithStatusCaveat", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 8550.0, "evidence_available_at_that_date": "AESTHETIC_DEVICE_EXPORT_DISTRIBUTION_STRATEGIC_TRANSACTION_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:JEISYS_MEDICAL_2024_AESTHETIC_DEVICE_EXPORT_STRATEGIC_TRANSACTION_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["medical_device_export_or_reimbursement_candidate", "adoption_or_installed_base_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "distributor_reorder_or_recurring_revenue_candidate"], "stage4b_evidence_fields": ["medical_device_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/287/287410/2024.csv", "profile_path": "atlas/symbol_profiles/287/287410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.91, "MFE_90D_pct": 51.23, "MFE_180D_pct": 61.4, "MAE_30D_pct": -13.22, "MAE_90D_pct": -13.22, "MAE_180D_pct": -13.22, "peak_date": "2024-08-16", "peak_price": 13800.0, "drawdown_after_peak_pct": -7.68, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_device_peak_if_export_reimbursement_adoption_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reimbursement_failure_export_channel_loss_adoption_collapse_margin_or_financing_break", "trigger_outcome_label": "positive_with_status_validation_and_later_4b_watch", "current_profile_verdict": "C25 should protect aesthetic-device export/commercialization positives when export channel, installed-base, consumables, distributor reorder, revenue and margin bridge are visible. Jeisys Medical produced strong MFE and later a stabilized strategic-event price path, but status/delisting-like caveat requires validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_status_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C25_MED_DEVICE_287410_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R7L79-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-THEME-FADE", "case_id": "R7L79-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-THEME-FADE", "symbol": "099190", "company_name": "아이센스", "round": "R7", "loop": "79", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_CGM_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail", "trigger_type": "Stage2-FalsePositive / CGMReimbursementExportThemeFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 24400.0, "evidence_available_at_that_date": "CGM_REIMBURSEMENT_EXPORT_THEME_WITH_WEAK_ADOPTION_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ISENS_2024_CGM_REIMBURSEMENT_EXPORT_ADOPTION_RECURRING_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["medical_device_export_or_reimbursement_candidate", "adoption_or_installed_base_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "distributor_reorder_or_recurring_revenue_candidate"], "stage4b_evidence_fields": ["medical_device_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv", "profile_path": "atlas/symbol_profiles/099/099190.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.71, "MFE_90D_pct": 4.71, "MFE_180D_pct": 4.71, "MAE_30D_pct": -15.78, "MAE_90D_pct": -22.62, "MAE_180D_pct": -40.49, "peak_date": "2024-02-02", "peak_price": 25550.0, "drawdown_after_peak_pct": -43.17, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_device_peak_if_export_reimbursement_adoption_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reimbursement_failure_export_channel_loss_adoption_collapse_margin_or_financing_break", "trigger_outcome_label": "counterexample_CGM_reimbursement_export_local4b", "current_profile_verdict": "C25 should not treat CGM reimbursement/export theme beta as durable Stage2 unless reimbursement coverage, prescription/adoption, distributor revenue, recurring consumables and margin bridge are visible. i-SENS produced only small early MFE and then a deep MAE path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_status_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C25_MED_DEVICE_099190_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L79-C25-336570-WONTECH-AESTHETIC-DEVICE-EXPORT-MARGIN-LIFECYCLE", "trigger_id": "TRG_R7L79-C25-336570-WONTECH-AESTHETIC-DEVICE-EXPORT-MARGIN-LIFECYCLE", "symbol": "336570", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"export_reimbursement_score": 14, "adoption_installed_base_score": 13, "distributor_reorder_score": 13, "recurring_revenue_score": 12, "margin_bridge_score": 13, "relative_strength_score": 13, "execution_risk_score": 9, "sharecount_or_status_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"export_reimbursement_score": 16, "adoption_installed_base_score": 15, "distributor_reorder_score": 15, "recurring_revenue_score": 14, "margin_bridge_score": 15, "relative_strength_score": 12, "execution_risk_score": 10, "sharecount_or_status_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["export_reimbursement_score", "adoption_installed_base_score", "distributor_reorder_score", "recurring_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified export/reimbursement, adoption/installed-base, distributor reorder, recurring revenue and margin bridge; cap device theme beta when bridge fails to refresh.", "MFE_90D_pct": 53.26, "MAE_90D_pct": -6.13, "score_return_alignment_label": "medical_device_export_positive_with_lifecycle_4b", "current_profile_verdict": "C25 should allow medical-aesthetic device positives when export demand, distributor reorder, installed-base utilization, consumables/service revenue and margin bridge are visible. Wontech produced large MFE, then a high post-peak drawdown, so it needs lifecycle 4B if export/reorder/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L79-C25-287410-JEISYS-MEDICAL-AESTHETIC-DEVICE-STRATEGIC-EVENT", "trigger_id": "TRG_R7L79-C25-287410-JEISYS-MEDICAL-AESTHETIC-DEVICE-STRATEGIC-EVENT", "symbol": "287410", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"export_reimbursement_score": 14, "adoption_installed_base_score": 13, "distributor_reorder_score": 13, "recurring_revenue_score": 12, "margin_bridge_score": 13, "relative_strength_score": 13, "execution_risk_score": 9, "sharecount_or_status_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"export_reimbursement_score": 16, "adoption_installed_base_score": 15, "distributor_reorder_score": 15, "recurring_revenue_score": 14, "margin_bridge_score": 15, "relative_strength_score": 12, "execution_risk_score": 10, "sharecount_or_status_validation_risk": 12, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["export_reimbursement_score", "adoption_installed_base_score", "distributor_reorder_score", "recurring_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified export/reimbursement, adoption/installed-base, distributor reorder, recurring revenue and margin bridge; cap device theme beta when bridge fails to refresh.", "MFE_90D_pct": 51.23, "MAE_90D_pct": -13.22, "score_return_alignment_label": "medical_device_export_positive_with_lifecycle_4b", "current_profile_verdict": "C25 should protect aesthetic-device export/commercialization positives when export channel, installed-base, consumables, distributor reorder, revenue and margin bridge are visible. Jeisys Medical produced strong MFE and later a stabilized strategic-event price path, but status/delisting-like caveat requires validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L79-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-THEME-FADE", "trigger_id": "TRG_R7L79-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-THEME-FADE", "symbol": "099190", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"export_reimbursement_score": 5, "adoption_installed_base_score": 3, "distributor_reorder_score": 2, "recurring_revenue_score": 2, "margin_bridge_score": 2, "relative_strength_score": 3, "execution_risk_score": 22, "sharecount_or_status_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_before": 45, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"export_reimbursement_score": 3, "adoption_installed_base_score": 1, "distributor_reorder_score": 1, "recurring_revenue_score": 1, "margin_bridge_score": 1, "relative_strength_score": 2, "execution_risk_score": 24, "sharecount_or_status_validation_risk": 12, "source_confidence_score": 2}, "weighted_score_after": 33, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["export_reimbursement_score", "adoption_installed_base_score", "distributor_reorder_score", "recurring_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified export/reimbursement, adoption/installed-base, distributor reorder, recurring revenue and margin bridge; cap device theme beta when bridge fails to refresh.", "MFE_90D_pct": 4.71, "MAE_90D_pct": -22.62, "score_return_alignment_label": "false_positive_medical_device_bridge_gap", "current_profile_verdict": "C25 should not treat CGM reimbursement/export theme beta as durable Stage2 unless reimbursement coverage, prescription/adoption, distributor revenue, recurring consumables and margin bridge are visible. i-SENS produced only small early MFE and then a deep MAE path."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R7", "loop": 79, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_CGM_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "status_validation_required_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C25 medical-device symbols outside top-covered 338220/214150/145720/228670/328130 set, +3 aesthetic-device/strategic-device/CGM-reimbursement trigger families, +2 device export positives, +1 CGM reimbursement theme local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_sharecount_and_status_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R7", "loop": 79, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "axis": "aesthetic_device_CGM_export_reimbursement_bridge_vs_device_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C25 should split verified medical-device export/reimbursement/adoption rerating from generic device theme beta. Stage2 requires reimbursement or export channel evidence, installed-base or adoption, distributor reorder, recurring revenue and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count/status flags require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["336570", "287410", "099190"], "share_count_validation_required": ["287410", "099190"], "status_validation_required": ["287410"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": 79, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "share_count_validation_guard", "status_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C25 needs export/reimbursement/adoption/installed-base/revenue/margin proof. Wontech and Jeisys Medical show device export/commercialization MFE candidates after source repair; i-SENS shows CGM reimbursement/export theme beta fading into local 4B when adoption, recurring revenue and margin bridge are absent or stale."}
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
336570:
  name = 원텍 from 2022-06-30, 대신밸런스제8호스팩 before that
  corporate_action_candidate_dates = 2022-06-30
  selected window = 2024-02-01~D+180
  contamination = false

287410:
  name = 제이시스메디칼 from 2021-03-31, 유안타제3호스팩 before that
  corporate_action_candidate_dates = 2020-12-24, 2021-03-31
  selected window = 2024-02-01~D+180
  contamination = false by profile
  market segment includes KOSDAQ GLOBAL during 2024
  status_inferred = inactive_or_delisted_like
  share_count_change_inside_window = true → coding-agent validation required
  status_validation_required = true

099190:
  name = 아이센스
  corporate_action_candidate_dates = 2015-10-02, 2023-03-14, 2023-04-10
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C25 rows are source_proxy_only / evidence_url_pending.
287410 and 099190 require share-count validation.
287410 additionally requires status / inactive-or-delisted-like validation.
This MD is useful for stock-web path calibration and C25 rule-shape discovery,
but coding-agent promotion requires non-proxy device export/reimbursement/adoption/installed-base/revenue/margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R7/C25 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and some rows need share-count/status validation.

Candidate axis:
aesthetic_device_CGM_export_reimbursement_bridge_vs_device_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 336570, 287410 and 099190.
4. Validate 287410 status / inactive-or-delisted-like treatment and share-count changes.
5. Validate 099190 share-count changes inside the selected window.
6. Keep generic C25 medical-device export/reimbursement weight unchanged until source repair is complete.
7. Consider Stage2 only when:
   - export or reimbursement event is explicit,
   - adoption / installed-base evidence is visible,
   - distributor reorder or prescription/usage conversion exists,
   - recurring revenue or consumables/service bridge exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
8. Consider local 4B-watch when:
   - the trigger is device export/reimbursement theme beta only,
   - adoption/revenue/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
9. Do not convert local 4B-watch into full 4B/4C without non-price reimbursement failure, export channel loss, adoption collapse, financing or margin break.
10. Emit before/after diagnostics and reject if verified device export/reimbursement positives or status-caveat rows are overblocked.
```

---

## Final round state

```text
completed_round = R7
completed_loop = 79
next_round = R8
next_loop = 79
round_schedule_status = valid
round_sector_consistency = pass
```

