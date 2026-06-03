# E2R Stock-Web v12 Residual Research — R7 Loop 87 / L7 / C25

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R7",
  "scheduled_loop": 87,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 87,
  "computed_next_round": "R8",
  "computed_next_loop": 87,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "fine_archetype_id": "BODY_COMPOSITION_XRAY_DETECTOR_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_INSTALL_BASE_CONSUMABLE_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "medical_device_export_reimbursement_guardrail",
    "device_export_to_install_base_consumable_margin_bridge_test",
    "aesthetic_device_theme_MFE_vs_reorder_utilization_margin_bridge_test",
    "local_4B_timing_after_medical_device_MFE",
    "hard_4C_non_price_export_reimbursement_or_margin_break_protection",
    "source_proxy_runtime_promotion_blocker",
    "high_MAE_guardrail",
    "corporate_action_window_caveat_review",
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

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

This file is a standalone historical calibration / sector-archetype residual research artifact. It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R7
scheduled_loop = 87
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
computed_next_round = R8
computed_next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

R7 is the bio / healthcare / medical round. This run selects C25 because loop87 has reached R7 after R6/C21, while loop86 R7 used C24 and loop85 R7 used C23. The selected C25 route avoids top-covered medical AI / dental / reimbursement names and tests body-composition, aesthetic and imaging-device export/reimbursement bridges.

The tested mechanism:

```text
medical device / export / reimbursement headline
→ export order quality and channel reorder
→ installed base
→ consumable or service attachment
→ reimbursement / regulatory channel
→ gross / OP margin conversion
→ durable rerating or device-theme fade
```

C25 is the installed-base meter. A device sale is a spark; recurring use, reimbursement and margin are the current.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C25 top-covered symbols include `338220`, `214150`, `099190`, `145720`, `228670`, and `043150`. This run avoids that top-covered set and uses:

```text
041830 / 인바디
336570 / 원텍
100120 / 뷰웍스
```

All three are treated as new independent C25 medical-device export/reimbursement cases for this loop. No hard duplicate is intentionally reused.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
```

Per-symbol profile status:

| symbol | company | profile path | corporate-action caveat |
|---|---|---|---|
| 041830 | 인바디 | `atlas/symbol_profiles/041/041830.json` | old CA candidates through 2010; selected 2024 forward window clean |
| 336570 | 원텍 | `atlas/symbol_profiles/336/336570.json` | old 2022 SPAC/name-change CA candidate; selected 2024 forward window clean |
| 100120 | 뷰웍스 | `atlas/symbol_profiles/100/100120.json` | old 2011 CA candidate; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R7L87-C25-01 | 041830 | 2024-02-13 | 25,650 | 180D | clean | true |
| R7L87-C25-02 | 336570 | 2024-02-13 | 8,190 | 180D | clean | true |
| R7L87-C25-03 | 100120 | 2024-02-13 | 28,000 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | BODY_COMPOSITION_EXPORT_INSTALL_BASE | keep Stage2 with export order, installed base, reimbursement/channel and margin bridge |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | AESTHETIC_DEVICE_EXPORT_THEME_BLOWOFF | reject or local-4B-watch MFE without reorder, consumable attachment and margin bridge |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | XRAY_DETECTOR_EXPORT_LOW_MFE_FADE | reject low-MFE medical-imaging export rebound without backlog/reimbursement/margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R7L87-C25-01 | 041830 | 인바디 | Stage2-Actionable | 2024-02-13 | 25,650 | 20.47 | -15.79 | current_profile_partially_correct_local_4B_export_margin_watch_needed |
| R7L87-C25-02 | 336570 | 원텍 | Stage2-FalsePositive | 2024-02-13 | 8,190 | 36.75 | -32.11 | current_profile_false_positive_high_MAE_aesthetic_device_theme |
| R7L87-C25-03 | 100120 | 뷰웍스 | Stage2-FalsePositive | 2024-02-13 | 28,000 | 10.36 | -18.21 | current_profile_false_positive_low_MFE_export_device_theme |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_or_4C_case_count = 3
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD creates a source-repair queue and a C25 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: export order, installed base, reimbursement channel, consumable/service attachment, reorder cadence, regulatory channel, gross/OP margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 041830 | `atlas/ohlcv_tradable_by_symbol_year/041/041830/2024.csv` | `atlas/symbol_profiles/041/041830.json` |
| 336570 | `atlas/ohlcv_tradable_by_symbol_year/336/336570/2024.csv` | `atlas/symbol_profiles/336/336570.json` |
| 100120 | `atlas/ohlcv_tradable_by_symbol_year/100/100120/2024.csv` | `atlas/symbol_profiles/100/100120.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 041830 / 인바디

C25 body-composition device export/install-base positive with local 4B watch. The February entry produced MFE into late March, but later drew down into August. It is kept as Stage2-Actionable, but needs export order quality, installed base, reimbursement/channel and margin evidence before clean Green.

### Case 2 — 336570 / 원텍

C25 aesthetic medical-device export theme high-MAE counterexample. The February entry produced meaningful MFE into April, but then fell deeply by August. Device theme MFE without reorder/consumable/margin bridge should not validate clean Stage2.

### Case 3 — 100120 / 뷰웍스

C25 X-ray detector / medical-imaging export low-MFE false positive. The March MFE was modest and later MAE widened. Imaging-device export language should remain RiskWatch unless order backlog, reimbursement channel and margin conversion are explicit.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 041830 | 25,650 | 20.47 | -3.90 | 20.47 | -3.90 | 20.47 | -15.79 | 2024-03-29 / 30,900 | -30.10 |
| 336570 | 8,190 | 20.76 | -3.66 | 36.75 | -3.66 | 36.75 | -32.11 | 2024-04-03 / 11,200 | -50.36 |
| 100120 | 28,000 | 10.36 | -2.14 | 10.36 | -2.86 | 10.36 | -18.21 | 2024-03-29 / 30,900 | -25.89 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R7L87-C25-01 | Stage2-Actionable if export/install-base bridge exists | moderate MFE, later drawdown | partially correct; local 4B/export-reimbursement watch needed |
| R7L87-C25-02 | risk of treating aesthetic device MFE as clean Stage2 | MFE then high MAE | false positive / high-MAE guardrail |
| R7L87-C25-03 | risk of treating imaging export rebound as Stage2 | low MFE / later MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C25, the residual is whether medical-device export/reimbursement MFE becomes clean Stage2/Green before installed base, reimbursement, reorder/consumable and margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R7L87-C25-01 | 0.72 | 0.62 | local 4B watch after body-composition device MFE if export/install-base/margin bridge stalls |
| R7L87-C25-02 | 0.35 | 0.30 | aesthetic device MFE rejected or local-4B-watched without reorder/consumable/margin bridge |
| R7L87-C25-03 | 0.35 | 0.30 | medical imaging export theme rejected without backlog/reimbursement/margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_export_order_reimbursement_or_margin_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C25 hard 4C requires confirmed export order loss, reimbursement failure, regulatory channel break, installed-base utilization deterioration, consumable attachment failure or margin thesis break.

## 17. Sector / Canonical Rule Candidate

```text
rule_scope = no_new_global_rule
canonical_archetype_rule_candidate = C25_medical_device_export_reimbursement_installed_base_consumable_margin_bridge_required
confidence = low
production_scoring_changed = false
shadow_weight_only = true
```

## 18. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 22.53 | -3.47 | may over-credit medical-device export theme MFE without reimbursement/installed-base bridge | needs C25 export/reimbursement margin repair |
| P1 canonical shadow bridge profile | 3 | keeps 041830 with watch | demotes 336570/100120 | better alignment, source repair required |

## 19. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | canonical rule |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L7_BIO_HEALTHCARE_MEDICAL | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | BODY_COMPOSITION_XRAY_DETECTOR_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_INSTALL_BASE_CONSUMABLE_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE | 1 | 2 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | yes |

## 20. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
new_symbol_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
residual_error_types_found:
  - medical_device_theme_false_positive_high_MAE
  - export_reimbursement_installed_base_consumable_margin_bridge_required
  - aesthetic_device_MFE_then_high_MAE_false_positive
  - medical_imaging_low_MFE_false_positive
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_non_price_export_reimbursement_or_margin_break
new_axis_proposed: false
existing_axis_strengthened:
  - C25_medical_device_export_reimbursement_installed_base_consumable_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
do_not_propose_new_weight_delta: true
```

## 21. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- Stock-Web profile path exists for selected symbols
- Stock-Web tradable shard path exists for selected symbols
- entry_date / entry_price are taken from tradable_raw close
- MFE / MAE / peak / post-peak drawdown are computed from observed OHLC windows
- corporate-action windows are checked at profile level
- scheduled_round / scheduled_loop / large_sector consistency
```

Not validated in this MD:

```text
- primary evidence URL
- exact publication time
- export order or backlog evidence
- reimbursement / regulatory channel
- installed-base utilization and consumable attachment
- gross/OP margin conversion
- production scoring implementation
```

## 22. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C25_medical_device_export_reimbursement_installed_base_consumable_margin_bridge_required,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Require export order quality, installed base, reimbursement channel, consumable/service attachment, channel reorder and gross/OP margin conversion before clean Stage2/Green","keeps 041830 with local 4B/export-reimbursement watch; demotes 336570/100120","R7L87-C25-01-S2A-20240213|R7L87-C25-02-S2FP-20240213|R7L87-C25-03-S2FP-20240213",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 23. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R7L87-C25-01", "symbol": "041830", "company_name": "인바디", "round": "R7", "loop": 87, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "BODY_COMPOSITION_XRAY_DETECTOR_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_INSTALL_BASE_CONSUMABLE_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "case_type": "body_composition_device_export_install_base_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R7L87-C25-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "moderate_device_export_MFE_but_install_base_reimbursement_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_export_margin_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C25 body-composition device positives need export order quality, installed base, consumable/service attachment, reimbursement channel and gross/OP margin bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R7L87-C25-01-S2A-20240213", "case_id": "R7L87-C25-01", "symbol": "041830", "company_name": "인바디", "round": "R7", "loop": 87, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "BODY_COMPOSITION_XRAY_DETECTOR_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_INSTALL_BASE_CONSUMABLE_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail|installed_base_consumable_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "body composition medical device / export channel / install-base and consumable-service margin proxy; primary export order, reimbursement and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["medical_device_export_proxy", "installed_base_proxy", "reimbursement_or_margin_proxy"], "stage3_evidence_fields": ["confirmed_export_order", "installed_base", "reimbursement_channel", "consumable_service_attachment", "channel_reorder", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["medical_device_MFE_without_export_reimbursement_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_export_order_loss_reimbursement_failure_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041830/2024.csv", "profile_path": "atlas/symbol_profiles/041/041830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 25650, "MFE_30D_pct": 20.47, "MAE_30D_pct": -3.9, "MFE_90D_pct": 20.47, "MAE_90D_pct": -3.9, "MFE_180D_pct": 20.47, "MAE_180D_pct": -15.79, "peak_date": "2024-03-29", "peak_price": 30900, "drawdown_after_peak_pct": -30.1, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.72, "four_b_full_window_peak_proximity": 0.62, "four_b_timing_verdict": "local_4B_watch_after_body_composition_device_MFE_if_export_install_base_reimbursement_margin_bridge_stalls", "four_b_evidence_type": ["medical_device_MFE_without_export_reimbursement_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_export_order_reimbursement_or_margin_break", "trigger_outcome_label": "moderate_device_export_MFE_but_install_base_reimbursement_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_export_margin_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2010_CA_candidates", "same_entry_group_id": "R7L87-C25-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L87-C25-01", "trigger_id": "R7L87-C25-01-S2A-20240213", "symbol": "041830", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"export_order_visibility_score": 50, "installed_base_score": 45, "reimbursement_channel_score": 35, "consumable_service_attachment_score": 35, "channel_reorder_score": 40, "gross_margin_bridge_score": 40, "regulatory_quality_score": 40, "relative_strength_score": 55, "valuation_blowoff_risk_score": 55, "execution_risk_score": 45, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"export_order_visibility_score": 50, "installed_base_score": 45, "reimbursement_channel_score": 35, "consumable_service_attachment_score": 35, "channel_reorder_score": 40, "gross_margin_bridge_score": 40, "regulatory_quality_score": 40, "relative_strength_score": 55, "valuation_blowoff_risk_score": 65, "execution_risk_score": 45, "source_quality_score": 10, "4B_watch_score": 80, "4C_watch_score": 25}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + local 4B/export-reimbursement margin watch", "changed_components": ["export_order_visibility_score", "installed_base_score", "reimbursement_channel_score", "consumable_service_attachment_score", "channel_reorder_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C25 requires medical-device export/reimbursement MFE to convert into export order quality, installed base, reimbursement channel, consumable/service attachment, reorder cadence and gross/OP margin bridge before clean Stage2/Green.", "MFE_90D_pct": 20.47, "MAE_90D_pct": -3.9, "score_return_alignment_label": "moderate_device_export_MFE_but_install_base_reimbursement_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_export_margin_watch_needed"}
{"row_type": "case", "case_id": "R7L87-C25-02", "symbol": "336570", "company_name": "원텍", "round": "R7", "loop": 87, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "BODY_COMPOSITION_XRAY_DETECTOR_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_INSTALL_BASE_CONSUMABLE_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "case_type": "aesthetic_medical_device_export_theme_MFE_then_high_MAE_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R7L87-C25-02-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aesthetic_device_MFE_then_deep_MAE_export_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_aesthetic_device_theme", "price_source": "Songdaiki/stock-web", "notes": "Aesthetic-device export MFE should not validate C25 unless reorder cadence, installed-base utilization, consumable attachment and margin conversion are explicit at entry."}
{"row_type": "trigger", "trigger_id": "R7L87-C25-02-S2FP-20240213", "case_id": "R7L87-C25-02", "symbol": "336570", "company_name": "원텍", "round": "R7", "loop": 87, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "BODY_COMPOSITION_XRAY_DETECTOR_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_INSTALL_BASE_CONSUMABLE_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail|installed_base_consumable_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "aesthetic medical device / export and installed-base expansion proxy without confirmed reorder, consumable, reimbursement or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["medical_device_export_proxy", "installed_base_proxy", "reimbursement_or_margin_proxy"], "stage3_evidence_fields": ["confirmed_export_order", "installed_base", "reimbursement_channel", "consumable_service_attachment", "channel_reorder", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["medical_device_MFE_without_export_reimbursement_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_export_order_loss_reimbursement_failure_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336570/2024.csv", "profile_path": "atlas/symbol_profiles/336/336570.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 8190, "MFE_30D_pct": 20.76, "MAE_30D_pct": -3.66, "MFE_90D_pct": 36.75, "MAE_90D_pct": -3.66, "MFE_180D_pct": 36.75, "MAE_180D_pct": -32.11, "peak_date": "2024-04-03", "peak_price": 11200, "drawdown_after_peak_pct": -50.36, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "aesthetic_device_MFE_rejected_or_local_4B_watch_without_export_reorder_consumable_margin_bridge", "four_b_evidence_type": ["medical_device_MFE_without_export_reimbursement_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_export_order_reimbursement_or_margin_break", "trigger_outcome_label": "aesthetic_device_MFE_then_deep_MAE_export_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_aesthetic_device_theme", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_2022_SPAC_CA_candidate", "same_entry_group_id": "R7L87-C25-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L87-C25-02", "trigger_id": "R7L87-C25-02-S2FP-20240213", "symbol": "336570", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"export_order_visibility_score": 25, "installed_base_score": 20, "reimbursement_channel_score": 5, "consumable_service_attachment_score": 5, "channel_reorder_score": 10, "gross_margin_bridge_score": 5, "regulatory_quality_score": 25, "relative_strength_score": 35, "valuation_blowoff_risk_score": 75, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"export_order_visibility_score": 25, "installed_base_score": 20, "reimbursement_channel_score": 0, "consumable_service_attachment_score": 0, "channel_reorder_score": 0, "gross_margin_bridge_score": 0, "regulatory_quality_score": 25, "relative_strength_score": 35, "valuation_blowoff_risk_score": 75, "execution_risk_score": 92, "source_quality_score": 5, "4B_watch_score": 92, "4C_watch_score": 65}, "weighted_score_after": 42, "stage_label_after": "Rejected-Stage2 / Medical-device export theme RiskWatch", "changed_components": ["export_order_visibility_score", "installed_base_score", "reimbursement_channel_score", "consumable_service_attachment_score", "channel_reorder_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C25 requires medical-device export/reimbursement MFE to convert into export order quality, installed base, reimbursement channel, consumable/service attachment, reorder cadence and gross/OP margin bridge before clean Stage2/Green.", "MFE_90D_pct": 36.75, "MAE_90D_pct": -3.66, "score_return_alignment_label": "aesthetic_device_MFE_then_deep_MAE_export_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_aesthetic_device_theme"}
{"row_type": "case", "case_id": "R7L87-C25-03", "symbol": "100120", "company_name": "뷰웍스", "round": "R7", "loop": 87, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "BODY_COMPOSITION_XRAY_DETECTOR_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_INSTALL_BASE_CONSUMABLE_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "case_type": "Xray_detector_medical_imaging_export_low_MFE_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R7L87-C25-03-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_high_MAE_medical_imaging_export_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_export_device_theme", "price_source": "Songdaiki/stock-web", "notes": "Medical-imaging export/replacement-cycle language should remain RiskWatch unless backlog, export order quality, reimbursement channel and margin bridge are source-repaired."}
{"row_type": "trigger", "trigger_id": "R7L87-C25-03-S2FP-20240213", "case_id": "R7L87-C25-03", "symbol": "100120", "company_name": "뷰웍스", "round": "R7", "loop": 87, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "BODY_COMPOSITION_XRAY_DETECTOR_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_INSTALL_BASE_CONSUMABLE_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail|installed_base_consumable_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "X-ray detector / medical imaging export and device replacement-cycle proxy without confirmed order backlog, reimbursement or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["medical_device_export_proxy", "installed_base_proxy", "reimbursement_or_margin_proxy"], "stage3_evidence_fields": ["confirmed_export_order", "installed_base", "reimbursement_channel", "consumable_service_attachment", "channel_reorder", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["medical_device_MFE_without_export_reimbursement_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_export_order_loss_reimbursement_failure_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100120/2024.csv", "profile_path": "atlas/symbol_profiles/100/100120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 28000, "MFE_30D_pct": 10.36, "MAE_30D_pct": -2.14, "MFE_90D_pct": 10.36, "MAE_90D_pct": -2.86, "MFE_180D_pct": 10.36, "MAE_180D_pct": -18.21, "peak_date": "2024-03-29", "peak_price": 30900, "drawdown_after_peak_pct": -25.89, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "medical_imaging_export_theme_rejected_without_order_backlog_reimbursement_margin_bridge", "four_b_evidence_type": ["medical_device_MFE_without_export_reimbursement_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_export_order_reimbursement_or_margin_break", "trigger_outcome_label": "low_MFE_high_MAE_medical_imaging_export_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_export_device_theme", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2011_CA_candidate", "same_entry_group_id": "R7L87-C25-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L87-C25-03", "trigger_id": "R7L87-C25-03-S2FP-20240213", "symbol": "100120", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"export_order_visibility_score": 25, "installed_base_score": 20, "reimbursement_channel_score": 5, "consumable_service_attachment_score": 5, "channel_reorder_score": 10, "gross_margin_bridge_score": 5, "regulatory_quality_score": 25, "relative_strength_score": 35, "valuation_blowoff_risk_score": 75, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"export_order_visibility_score": 25, "installed_base_score": 20, "reimbursement_channel_score": 0, "consumable_service_attachment_score": 0, "channel_reorder_score": 0, "gross_margin_bridge_score": 0, "regulatory_quality_score": 25, "relative_strength_score": 35, "valuation_blowoff_risk_score": 75, "execution_risk_score": 92, "source_quality_score": 5, "4B_watch_score": 92, "4C_watch_score": 65}, "weighted_score_after": 42, "stage_label_after": "Rejected-Stage2 / Medical-device export theme RiskWatch", "changed_components": ["export_order_visibility_score", "installed_base_score", "reimbursement_channel_score", "consumable_service_attachment_score", "channel_reorder_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C25 requires medical-device export/reimbursement MFE to convert into export order quality, installed base, reimbursement channel, consumable/service attachment, reorder cadence and gross/OP margin bridge before clean Stage2/Green.", "MFE_90D_pct": 10.36, "MAE_90D_pct": -2.86, "score_return_alignment_label": "low_MFE_high_MAE_medical_imaging_export_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_export_device_theme"}
{"row_type": "shadow_weight", "axis": "C25_medical_device_export_reimbursement_installed_base_consumable_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Medical-device export/reimbursement rerating requires export order quality, installed base, reimbursement channel, consumable/service attachment, channel reorder and gross/OP margin conversion; device-theme MFE without bridge fades into high MAE or low-MFE false positive.", "backtest_effect": "keeps 041830 with local 4B/export-reimbursement watch; demotes 336570/100120 device-theme false positives", "trigger_ids": "R7L87-C25-01-S2A-20240213|R7L87-C25-02-S2FP-20240213|R7L87-C25-03-S2FP-20240213", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R7", "loop": 87, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["medical_device_theme_false_positive_high_MAE", "export_reimbursement_installed_base_consumable_margin_bridge_required", "aesthetic_device_MFE_then_high_MAE_false_positive", "medical_imaging_low_MFE_false_positive", "source_proxy_runtime_promotion_risk", "hard_4C_requires_non_price_export_reimbursement_or_margin_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
```

## 24. Deferred Coding Agent Handoff Prompt

Use only `calibration_usable=true` rows. Do not treat `source_proxy_only/evidence_url_pending` rows as runtime promotion-ready. For C25, test a canonical guard requiring export order quality, installed base, reimbursement channel, consumable/service attachment, channel reorder and gross/OP margin conversion before clean Stage2/Green.

## 25. Next Round State

```text
completed_round = R7
completed_loop = 87
next_round = R8
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

## 26. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
