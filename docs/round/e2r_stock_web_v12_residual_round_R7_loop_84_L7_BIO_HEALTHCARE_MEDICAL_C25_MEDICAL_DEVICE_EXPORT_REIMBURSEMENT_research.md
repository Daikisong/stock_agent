# E2R Stock-Web v12 Residual Research — R7 Loop 84 / L7 / C25

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R7",
  "scheduled_loop": 84,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 84,
  "computed_next_round": "R8",
  "computed_next_loop": 84,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "fine_archetype_id": "AESTHETIC_OPHTHALMIC_XRAY_DEVICE_EXPORT_REORDER_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "medical_device_export_reimbursement_guardrail",
    "device_export_reorder_install_base_margin_bridge_test",
    "local_4B_timing_after_device_MFE",
    "source_proxy_runtime_promotion_blocker",
    "high_MAE_guardrail",
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
scheduled_loop = 84
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
computed_next_round = R8
computed_next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

R7 is the bio / healthcare / medical round. This run selects C25 because loop83 already tested C24 trial-data event risk. C25 is the device-specific bridge:

```text
medical-device export / reimbursement / regulatory clearance headline
→ install-base utilization
→ distributor sell-through and reorder cadence
→ reimbursement or hospital purchasing visibility
→ gross-margin conversion
→ durable rerating or local 4B / false-positive fade
```

A device can be shipped once and still not become a compounding business. C25 only becomes durable when the box on the hospital floor turns into repeated utilization, reordered consumables or follow-on device demand, and margin conversion.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C25 top-covered symbols include `338220`, `214150`, `099190`, `145720`, `228670`, and `043150`. This run avoids that top-covered set and uses:

```text
336570 / 원텍
065510 / 휴비츠
263690 / 디알젬
```

All three are treated as new independent C25 medical-device export / reimbursement / reorder cases for this loop. No hard duplicate is intentionally reused.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Per-symbol profile status:

| symbol | company | profile path | corporate-action caveat |
|---|---|---|---|
| 336570 | 원텍 | `atlas/symbol_profiles/336/336570.json` | old 2022 SPAC/CA candidate; selected 2024 forward window clean |
| 065510 | 휴비츠 | `atlas/symbol_profiles/065/065510.json` | old 2004 CA candidates; selected 2024 forward window clean |
| 263690 | 디알젬 | `atlas/symbol_profiles/263/263690.json` | no profile-level CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R7L84-C25-01 | 336570 | 2024-03-11 | 7,880 | 180D | clean | true |
| R7L84-C25-02 | 065510 | 2024-02-05 | 18,220 | 180D | clean | true |
| R7L84-C25-03 | 263690 | 2024-01-15 | 10,990 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | AESTHETIC_DEVICE_EXPORT_INSTALLBASE_REORDER | keep Stage2 only with export order, install-base utilization, consumables/reorder and margin bridge; add local 4B after MFE |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | OPHTHALMIC_DEVICE_EXPORT_THEME_FADE | reject or demote when distributor/reimbursement/reorder evidence is missing |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | XRAY_DEVICE_EXPORT_REORDER_FADE | reject low-MFE export-order buzz without fresh backlog and reimbursement bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R7L84-C25-01 | 336570 | 원텍 | Stage2-Actionable | 2024-03-11 | 7,880 | 42.13 | -29.44 | current_profile_partially_correct_local_4B_watch_needed |
| R7L84-C25-02 | 065510 | 휴비츠 | Stage2-FalsePositive | 2024-02-05 | 18,220 | 20.2 | -53.35 | current_profile_false_positive_high_MAE |
| R7L84-C25-03 | 263690 | 디알젬 | Stage2-FalsePositive | 2024-01-15 | 10,990 | 2.91 | -24.75 | current_profile_false_positive_low_MFE |

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

This MD therefore creates a source-repair queue and a C25 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: export order, regulatory/reimbursement clearance, distributor sell-through, install-base utilization, reorder cadence, consumables pull-through, gross-margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 336570 | `atlas/ohlcv_tradable_by_symbol_year/336/336570/2024.csv` | `atlas/symbol_profiles/336/336570.json` |
| 065510 | `atlas/ohlcv_tradable_by_symbol_year/065/065510/2024.csv` | `atlas/symbol_profiles/065/065510.json` |
| 263690 | `atlas/ohlcv_tradable_by_symbol_year/263/263690/2024.csv` | `atlas/symbol_profiles/263/263690.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 336570 / 원텍

C25 device-export positive with local 4B watch. The entry path produced strong MFE, but the later drawdown shows why the device model must not wait for full-window 4B. It needs install-base utilization, distributor reorder and margin repair before clean Green.

### Case 2 — 065510 / 휴비츠

C25 ophthalmic-device false positive. The initial MFE was tradable, but the MAE widened fast. This is a device-theme heat case unless distributor sell-through, reimbursement and margin conversion are repaired.

### Case 3 — 263690 / 디알젬

C25 X-ray export/reorder fade. The entry-date upside was weak and the forward path bled lower. Export-order buzz did not become durable rerating in the absence of fresh order backlog and reimbursement/channel evidence.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 336570 | 7,880 | 42.13 | -0.76 | 42.13 | -15.61 | 42.13 | -29.44 | 2024-04-03 / 11,200 | -50.36 |
| 065510 | 18,220 | 20.20 | -22.78 | 20.20 | -32.60 | 20.20 | -53.35 | 2024-02-05 / 21,900 | -61.19 |
| 263690 | 10,990 | 2.91 | -6.73 | 2.91 | -13.56 | 2.91 | -24.75 | 2024-01-16 / 11,310 | -36.60 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R7L84-C25-01 | Stage2-Actionable if export/reorder/margin bridge exists | strong MFE, later drawdown | partially correct; local 4B watch needed |
| R7L84-C25-02 | risk of treating ophthalmic-device export theme as Stage2 | short MFE / high MAE | false positive |
| R7L84-C25-03 | risk of treating X-ray export-order buzz as Stage2 | low MFE / persistent MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C25, the residual is not Green lateness. The residual is whether device export MFE becomes clean Stage2/Green before install-base, reorder, reimbursement and gross-margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R7L84-C25-01 | 0.82 | 0.72 | local 4B watch after device export MFE if reorder/margin bridge stalls |
| R7L84-C25-02 | 0.30 | 0.25 | device-theme MFE rejected without export/reorder/reimbursement bridge |
| R7L84-C25-03 | 0.30 | 0.25 | export-order buzz rejected without backlog/reimbursement bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_reimbursement_or_order_break
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L7 medical-device rows need install-base utilization, distributor sell-through/reorder, reimbursement/regulatory and margin bridge before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
candidate_axis = C25_device_export_installbase_reorder_reimbursement_margin_bridge_required
effect = keep device positives with local 4B/high-MAE watch; demote device-export theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 21.75 | -20.59 | may over-credit medical-device export/order MFE | needs C25 bridge repair |
| P1 canonical shadow bridge profile | 3 | 42.13 on kept positive | -15.61 on kept positive | demotes 065510/263690 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R7L84-C25-01 | 78 | Stage2-Actionable | 76 | Stage2-Actionable + local 4B/high-MAE watch | partially aligned |
| R7L84-C25-02 | 58 | Stage2-Watch/FalsePositive | 46 | Rejected-Stage2 / RiskWatch | improved |
| R7L84-C25-03 | 58 | Stage2-Watch/FalsePositive | 46 | Rejected-Stage2 / RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | AESTHETIC_OPHTHALMIC_XRAY_DEVICE_EXPORT_REORDER_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE | 1 | 2 | 3-watch | 0 | 3 | 0 | 3 | 2 | no | yes | source repair needed |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
residual_error_types_found:
  - medical_device_theme_false_positive_high_MAE
  - export_installbase_reorder_reimbursement_margin_bridge_required
  - local_4B_late_after_device_MFE
  - source_proxy_runtime_promotion_risk
  - high_MAE_positive_Green_blocker
new_axis_proposed: false
existing_axis_strengthened:
  - C25_device_export_installbase_reorder_reimbursement_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C25_device_export_installbase_reorder_reimbursement_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.

## 23. Validation Scope / Non-Validation Scope

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
- export order or distributor sell-through source
- install-base utilization / consumables pull-through
- reimbursement or regulatory clearance detail
- gross-margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C25_device_export_installbase_reorder_reimbursement_margin_bridge_required,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Require medical-device export traction to convert into install-base utilization, distributor sell-through/reorder, reimbursement/regulatory bridge and margin conversion before clean Stage2/Green","keeps 336570 with local 4B watch; demotes 065510/263690","R7L84-C25-01-S2A-20240311|R7L84-C25-02-S2FP-20240205|R7L84-C25-03-S2FP-20240115",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R7L84-C25-01", "symbol": "336570", "company_name": "원텍", "round": "R7", "loop": 84, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_OPHTHALMIC_XRAY_DEVICE_EXPORT_REORDER_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "case_type": "aesthetic_device_export_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R7L84-C25-01-S2A-20240311", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "device_export_MFE_positive_but_local_4B_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C25 can keep Stage2 only when device export traction converts into install-base utilization, consumables/reorder, reimbursement or distributor quality, and margin bridge."}
{"row_type": "trigger", "trigger_id": "R7L84-C25-01-S2A-20240311", "case_id": "R7L84-C25-01", "symbol": "336570", "company_name": "원텍", "round": "R7", "loop": 84, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_OPHTHALMIC_XRAY_DEVICE_EXPORT_REORDER_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail|local_4B_timing_after_device_MFE|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-11", "evidence_available_at_that_date": "aesthetic medical-device export and install-base reorder proxy; primary reimbursement/export evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["device_export_proxy", "install_base_or_distributor_proxy", "reorder_visibility_proxy"], "stage3_evidence_fields": ["confirmed_export_order", "distributor_sellthrough", "install_base_utilization", "reimbursement_or_regulatory_clearance", "gross_margin_conversion"], "stage4b_evidence_fields": ["device_MFE_without_reorder_bridge", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_reimbursement_or_customer_order_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336570/2024.csv", "profile_path": "atlas/symbol_profiles/336/336570.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-11", "entry_price": 7880, "MFE_30D_pct": 42.13, "MFE_90D_pct": 42.13, "MFE_180D_pct": 42.13, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -0.76, "MAE_90D_pct": -15.61, "MAE_180D_pct": -29.44, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-03", "peak_price": 11200, "drawdown_after_peak_pct": -50.36, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_watch_after_device_export_MFE_if_reorder_margin_bridge_stalls", "four_b_evidence_type": ["device_MFE_without_reorder_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_reimbursement_or_order_break", "trigger_outcome_label": "device_export_MFE_positive_but_local_4B_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2022_SPAC_CA_candidate", "same_entry_group_id": "R7L84-C25-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L84-C25-01", "trigger_id": "R7L84-C25-01-S2A-20240311", "symbol": "336570", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"device_export_score": 55, "install_base_score": 45, "reorder_visibility_score": 40, "reimbursement_score": 35, "distributor_quality_score": 40, "gross_margin_bridge_score": 40, "revision_score": 45, "relative_strength_score": 65, "valuation_blowoff_risk_score": 65, "execution_risk_score": 45, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"device_export_score": 55, "install_base_score": 45, "reorder_visibility_score": 40, "reimbursement_score": 35, "distributor_quality_score": 40, "gross_margin_bridge_score": 40, "revision_score": 45, "relative_strength_score": 65, "valuation_blowoff_risk_score": 75, "execution_risk_score": 45, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable + local 4B/high-MAE watch", "changed_components": ["reorder_visibility_score", "reimbursement_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C25 requires device export traction to convert into install-base utilization, distributor sell-through/reorder, reimbursement/regulatory clearance and gross-margin conversion; device-theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 42.13, "MAE_90D_pct": -15.61, "score_return_alignment_label": "device_export_MFE_positive_but_local_4B_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R7L84-C25-02", "symbol": "065510", "company_name": "휴비츠", "round": "R7", "loop": 84, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_OPHTHALMIC_XRAY_DEVICE_EXPORT_REORDER_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "case_type": "ophthalmic_device_export_theme_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R7L84-C25-02-S2FP-20240205", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "short_MFE_high_MAE_device_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Ophthalmic device export narrative should stay RiskWatch unless distributor sell-through, repeat orders and margin conversion are explicit."}
{"row_type": "trigger", "trigger_id": "R7L84-C25-02-S2FP-20240205", "case_id": "R7L84-C25-02", "symbol": "065510", "company_name": "휴비츠", "round": "R7", "loop": 84, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_OPHTHALMIC_XRAY_DEVICE_EXPORT_REORDER_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail|local_4B_timing_after_device_MFE|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-05", "evidence_available_at_that_date": "ophthalmic equipment export/order theme proxy without distributor reorder, reimbursement or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["device_export_proxy", "install_base_or_distributor_proxy", "reorder_visibility_proxy"], "stage3_evidence_fields": ["confirmed_export_order", "distributor_sellthrough", "install_base_utilization", "reimbursement_or_regulatory_clearance", "gross_margin_conversion"], "stage4b_evidence_fields": ["device_MFE_without_reorder_bridge", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_reimbursement_or_customer_order_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/065/065510/2024.csv", "profile_path": "atlas/symbol_profiles/065/065510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-05", "entry_price": 18220, "MFE_30D_pct": 20.2, "MFE_90D_pct": 20.2, "MFE_180D_pct": 20.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -22.78, "MAE_90D_pct": -32.6, "MAE_180D_pct": -53.35, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-05", "peak_price": 21900, "drawdown_after_peak_pct": -61.19, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.3, "four_b_full_window_peak_proximity": 0.25, "four_b_timing_verdict": "device_theme_MFE_rejected_without_export_reorder_reimbursement_margin_bridge", "four_b_evidence_type": ["device_MFE_without_reorder_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_reimbursement_or_order_break", "trigger_outcome_label": "short_MFE_high_MAE_device_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2004_CA_candidates", "same_entry_group_id": "R7L84-C25-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L84-C25-02", "trigger_id": "R7L84-C25-02-S2FP-20240205", "symbol": "065510", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"device_export_score": 30, "install_base_score": 15, "reorder_visibility_score": 5, "reimbursement_score": 5, "distributor_quality_score": 15, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 70, "execution_risk_score": 75, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"device_export_score": 30, "install_base_score": 15, "reorder_visibility_score": 0, "reimbursement_score": 0, "distributor_quality_score": 15, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 70, "execution_risk_score": 85, "source_quality_score": 5, "4B_watch_score": 80}, "weighted_score_after": 46, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["reorder_visibility_score", "reimbursement_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C25 requires device export traction to convert into install-base utilization, distributor sell-through/reorder, reimbursement/regulatory clearance and gross-margin conversion; device-theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 20.2, "MAE_90D_pct": -32.6, "score_return_alignment_label": "short_MFE_high_MAE_device_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "case", "case_id": "R7L84-C25-03", "symbol": "263690", "company_name": "디알젬", "round": "R7", "loop": 84, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_OPHTHALMIC_XRAY_DEVICE_EXPORT_REORDER_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "case_type": "xray_device_export_reorder_fade_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R7L84-C25-03-S2FP-20240115", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_persistent_MAE_device_export_fade", "current_profile_verdict": "current_profile_false_positive_low_MFE", "price_source": "Songdaiki/stock-web", "notes": "Device export/order buzz should be rejected unless backlog, reimbursement/channel quality and margin conversion are visible at entry."}
{"row_type": "trigger", "trigger_id": "R7L84-C25-03-S2FP-20240115", "case_id": "R7L84-C25-03", "symbol": "263690", "company_name": "디알젬", "round": "R7", "loop": 84, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_OPHTHALMIC_XRAY_DEVICE_EXPORT_REORDER_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|medical_device_export_reimbursement_guardrail|local_4B_timing_after_device_MFE|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-01-15", "evidence_available_at_that_date": "X-ray device export and distributor reorder proxy without fresh order backlog, reimbursement or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["device_export_proxy", "install_base_or_distributor_proxy", "reorder_visibility_proxy"], "stage3_evidence_fields": ["confirmed_export_order", "distributor_sellthrough", "install_base_utilization", "reimbursement_or_regulatory_clearance", "gross_margin_conversion"], "stage4b_evidence_fields": ["device_MFE_without_reorder_bridge", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_reimbursement_or_customer_order_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263690/2024.csv", "profile_path": "atlas/symbol_profiles/263/263690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-15", "entry_price": 10990, "MFE_30D_pct": 2.91, "MFE_90D_pct": 2.91, "MFE_180D_pct": 2.91, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.73, "MAE_90D_pct": -13.56, "MAE_180D_pct": -24.75, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-16", "peak_price": 11310, "drawdown_after_peak_pct": -36.6, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.3, "four_b_full_window_peak_proximity": 0.25, "four_b_timing_verdict": "device_export_theme_rejected_without_order_backlog_reimbursement_margin_bridge", "four_b_evidence_type": ["device_MFE_without_reorder_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_reimbursement_or_order_break", "trigger_outcome_label": "low_MFE_persistent_MAE_device_export_fade", "current_profile_verdict": "current_profile_false_positive_low_MFE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_profile_CA_candidate", "same_entry_group_id": "R7L84-C25-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L84-C25-03", "trigger_id": "R7L84-C25-03-S2FP-20240115", "symbol": "263690", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"device_export_score": 30, "install_base_score": 15, "reorder_visibility_score": 5, "reimbursement_score": 5, "distributor_quality_score": 15, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 70, "execution_risk_score": 75, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"device_export_score": 30, "install_base_score": 15, "reorder_visibility_score": 0, "reimbursement_score": 0, "distributor_quality_score": 15, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 35, "valuation_blowoff_risk_score": 70, "execution_risk_score": 85, "source_quality_score": 5, "4B_watch_score": 80}, "weighted_score_after": 46, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["reorder_visibility_score", "reimbursement_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C25 requires device export traction to convert into install-base utilization, distributor sell-through/reorder, reimbursement/regulatory clearance and gross-margin conversion; device-theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 2.91, "MAE_90D_pct": -13.56, "score_return_alignment_label": "low_MFE_persistent_MAE_device_export_fade", "current_profile_verdict": "current_profile_false_positive_low_MFE"}
{"row_type": "shadow_weight", "axis": "C25_device_export_installbase_reorder_reimbursement_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Medical-device rerating requires export order traction, install-base utilization, distributor sell-through/reorder, reimbursement/regulatory bridge and gross-margin conversion; device-theme MFE without bridge fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 336570 with local 4B watch; demotes 065510/263690 device-theme false positives", "trigger_ids": "R7L84-C25-01-S2A-20240311|R7L84-C25-02-S2FP-20240205|R7L84-C25-03-S2FP-20240115", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R7", "loop": 84, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail"], "residual_error_types_found": ["medical_device_theme_false_positive_high_MAE", "export_installbase_reorder_reimbursement_margin_bridge_required", "local_4B_late_after_device_MFE", "source_proxy_runtime_promotion_risk", "high_MAE_positive_Green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat source_proxy_only or evidence_url_pending rows as runtime promotion-ready.
- Keep production scoring unchanged unless a later batch validates primary evidence and aggregate thresholds.
- For C25, test a canonical-archetype guard requiring device export traction, install-base utilization, distributor sell-through/reorder, reimbursement/regulatory bridge and gross-margin conversion before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R7
completed_loop = 84
next_round = R8
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
