# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R7
scheduled_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE_VS_DENTAL_DEVICE_EXPORT_FALSE_STAGE2_AND_DIAGNOSTIC_IMAGING_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R7_loop_94_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
```

This file is the corrected final output for this execution. The scheduler state after R6 loop 94 is R7 / loop 94. R7 is the L7 bio/healthcare/medical round, and this run fills C25 medical-device export/reimbursement behavior rather than repeating the immediately preceding R7 loop 93 C24 trial-data file.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R7
scheduled_loop = 94
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
round_sector_consistency = pass
computed_next_round = R8
computed_next_loop = 94
```

C25 is a commercial bridge archetype. A device/export headline is only a clinic sign at the entrance. The working mechanism is repeat consumable demand, overseas channel throughput, reimbursement/distributor sell-through, ASP/mix, margin and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT = 33 rows / 16 symbols / good-bad Stage2 13-6 / 4B-4C 3-2
top covered symbols include 336570(6), 100120(3), 060280(2), 099190(2), 145720(2), 214150(2)
previous R7 loop-90 C24 symbols avoided: 397030, 365270, 067630
previous R7 loop-91 C25 symbols avoided: 206640, 043150, 246710
previous R7 loop-92 C23 symbols avoided: 196170, 003850, 950160
previous R7 loop-93 C24 symbols avoided: 039200, 950220, 174900
previous R6 loop-94 C21 symbols avoided: 055550, 006800, 041190
```

Selected rows avoid hard duplicates and top repeated C25 symbols:

```text
214450 / Stage2-Actionable / 2024-02-23
228670 / Stage2-Actionable / 2024-01-24
214680 / Stage4B / 2024-01-09
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest | atlas/manifest.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |

| symbol | profile path | CA window status |
|---|---|---|
| 214450 | atlas/symbol_profiles/214/214450.json | no corporate-action candidate |
| 228670 | atlas/symbol_profiles/228/228670.json | selected 2024 window clean after old 2021 CA candidates |
| 214680 | atlas/symbol_profiles/214/214680.json | selected 2024 window clean after old 2016 CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R7L94_C25_PHARMARESEARCH_2024_MEDICAL_AESTHETIC_EXPORT_MARGIN_POSITIVE | 214450 | 2024-02-23 | yes | 180 | yes | yes | true |
| R7L94_C25_RAY_2024_DENTAL_DEVICE_EXPORT_RECOVERY_FALSE_STAGE2 | 228670 | 2024-01-24 | yes | 180 | yes | yes | true |
| R7L94_C25_DRTECH_2024_DIAGNOSTIC_IMAGING_DEVICE_EVENT_CAP_4B | 214680 | 2024-01-09 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE | Positive Stage2 requires export-channel expansion, repeat consumable demand, ASP/mix, margin and revision bridge. |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | DENTAL_DEVICE_FALSE_STAGE2 | Dental-device export recovery watch without channel/margin bridge can become false Stage2. |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | DIAGNOSTIC_IMAGING_EVENT_CAP_4B | Diagnostic-imaging device export event premium should route to 4B when order/reimbursement/channel bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R7L94_C25_PHARMARESEARCH_2024_MEDICAL_AESTHETIC_EXPORT_MARGIN_POSITIVE | 214450 | 파마리서치 | positive | Export/channel and repeat-consumable margin bridge produced strong MFE with controlled early MAE. |
| R7L94_C25_RAY_2024_DENTAL_DEVICE_EXPORT_RECOVERY_FALSE_STAGE2 | 228670 | 레이 | counterexample | Dental export recovery watch had nearly no MFE and deep MAE without channel/margin bridge. |
| R7L94_C25_DRTECH_2024_DIAGNOSTIC_IMAGING_DEVICE_EVENT_CAP_4B | 214680 | 디알텍 | counterexample / 4B | Diagnostic-imaging device event premium capped at the January spike and then de-rated. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| PharmaResearch medical-aesthetic export margin bridge | historical public/report proxy | true | true | shadow-only positive |
| Ray dental-device export false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| DRTECH diagnostic-imaging event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 214450 | atlas/ohlcv_tradable_by_symbol_year/214/214450/2024.csv | atlas/symbol_profiles/214/214450.json |
| 228670 | atlas/ohlcv_tradable_by_symbol_year/228/228670/2024.csv | atlas/symbol_profiles/228/228670.json |
| 214680 | atlas/ohlcv_tradable_by_symbol_year/214/214680/2024.csv | atlas/symbol_profiles/214/214680.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R7L94_C25_PHARMARESEARCH_2024_STAGE2_ACTIONABLE_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE | 214450 | Stage2-Actionable | 2024-02-23 | 94700 | positive | medical-aesthetic export/margin bridge worked |
| R7L94_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE_EXPORT_RECOVERY | 228670 | Stage2-Actionable | 2024-01-24 | 21900 | counterexample | dental-device export recovery false Stage2 |
| R7L94_C25_DRTECH_2024_STAGE4B_DIAGNOSTIC_IMAGING_DEVICE_EVENT_CAP | 214680 | Stage4B | 2024-01-09 | 4890 | counterexample/4B | diagnostic-imaging device event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L94_C25_PHARMARESEARCH_2024_STAGE2_ACTIONABLE_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE | 94700 | 25.66 | -8.34 | 66.21 | -8.34 | 145.00 | -8.34 | 2024-10-16 | 232000 | -7.11 |
| R7L94_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE_EXPORT_RECOVERY | 21900 | 1.14 | -27.85 | 1.14 | -49.45 | 1.14 | -49.45 | 2024-01-24 | 22150 | -50.07 |
| R7L94_C25_DRTECH_2024_STAGE4B_DIAGNOSTIC_IMAGING_DEVICE_EVENT_CAP | 4890 | 4.09 | -22.99 | 4.09 | -39.67 | 4.09 | -39.67 | 2024-01-09 | 5090 | -42.53 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C25 Stage2 needs export-channel / repeat-consumable / order / reimbursement / margin bridge |
| local_4b_watch_guard | strengthen: bridge-missing medical-device event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE medical-device export rows cannot promote without durable channel/margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is export/reimbursement/channel bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 214450 | good_stage2_with_later_watch | Export-channel and margin bridge produced strong 90D and very high 180D MFE. |
| 228670 | bad_stage2 | Dental-device export recovery label lacked channel/margin bridge and then de-rated sharply. |
| 214680 | good_4B | Diagnostic-imaging event premium capped at the January spike and later suffered deep MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 228670 dental export false Stage2 | 0.99 | 0.99 | false Stage2 due missing export-channel/margin bridge |
| 214680 diagnostic-imaging cap | 0.96 | 0.96 | good full-window 4B timing after January device event spike |
| 214450 medical aesthetic bridge | n/a | n/a | positive Stage2, but later healthcare valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 228670 / 214680
```

No hard 4C candidate is proposed. R7 loop 94 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L7 medical-device/export/reimbursement cases, Stage2 requires verified export channel expansion, repeat consumable/order durability, reimbursement or distributor sell-through, ASP/mix, margin, or revision bridge. Medical device, dental, diagnostic, export, reimbursement, imaging or aesthetic label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
rule = C25 should split true export-channel/repeat-consumable/margin positives from dental export recovery false Stage2 and diagnostic-device event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 23.81 | -32.49 | 0.67 | mixed; C25 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 23.81 | -32.49 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L7 export/channel/margin bridge required | 2 | 33.68 | -28.90 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C25 bridge vs event-cap split | 2 | 33.68 | -28.90 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing medical-device export themes as positive | 1 | 66.21 | -8.34 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 214450 medical-aesthetic export bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 66.21 | -8.34 | medical_aesthetic_export_margin_positive |
| 228670 dental export false | 66 | Stage2-Actionable | 51 | Stage1/Watch | 1.14 | -49.45 | dental_device_export_recovery_false_stage2 |
| 214680 diagnostic-imaging cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 4.09 | -39.67 | diagnostic_imaging_device_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE_VS_DENTAL_DEVICE_EXPORT_FALSE_STAGE2_AND_DIAGNOSTIC_IMAGING_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C25 PharmaResearch medical-aesthetic export/margin positive, Ray dental-device export false Stage2, and DRTECH diagnostic-imaging device event-cap 4B split while avoiding top repeated C25 symbols and previous R7 loop93 C24 symbols."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: medical_aesthetic_export_margin_positive, dental_device_export_recovery_false_stage2, diagnostic_imaging_device_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C25 medical-device export/reimbursement bridge vs false Stage2 / event-cap split
```

Non-validation scope:

```text
- Exact as-of evidence URLs remain pending for all selected cases.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,configured,C25_requires_export_channel_repeat_consumable_order_margin_revision_bridge,0,"C25 Stage2 should require export channel expansion, repeat consumable/order durability, reimbursement or distributor sell-through, ASP/mix, margin, or revision bridge, not medical-device/export label alone","PharmaResearch positive worked; Ray and DRTECH event/watch rows failed positive-stage promotion","R7L94_C25_PHARMARESEARCH_2024_STAGE2_ACTIONABLE_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE|R7L94_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE_EXPORT_RECOVERY|R7L94_C25_DRTECH_2024_STAGE4B_DIAGNOSTIC_IMAGING_DEVICE_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,configured,cap_bridge_missing_medical_device_export_event_premiums_as_4B_watch,0,"Medical-device/export event premiums can peak before order, channel, reimbursement and margin bridge is proven","Ray had near-zero forward MFE and deep MAE; DRTECH showed event-cap behavior after January imaging-device spike","R7L94_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE_EXPORT_RECOVERY|R7L94_C25_DRTECH_2024_STAGE4B_DIAGNOSTIC_IMAGING_DEVICE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,configured,block_positive_stage_when_medical_device_theme_has_high_MAE_without_export_margin_bridge,0,"High or persistent MAE after bridge-missing medical-device export entries should block Stage2/Stage3 promotion unless channel, order, reimbursement and margin evidence survives","Ray MAE90=-49.45 and DRTECH MAE90=-39.67","R7L94_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE_EXPORT_RECOVERY|R7L94_C25_DRTECH_2024_STAGE4B_DIAGNOSTIC_IMAGING_DEVICE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R7L94_C25_PHARMARESEARCH_2024_MEDICAL_AESTHETIC_EXPORT_MARGIN_POSITIVE", "symbol": "214450", "company_name": "파마리서치", "round": "R7", "loop": "94", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE_VS_DENTAL_DEVICE_EXPORT_FALSE_STAGE2_AND_DIAGNOSTIC_IMAGING_EVENT_CAP", "case_type": "structural_success_with_later_medical_aesthetic_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R7L94_C25_PHARMARESEARCH_2024_STAGE2_ACTIONABLE_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Medical aesthetic / regenerative product export and margin bridge produced strong 30D/90D and very high 180D MFE with controlled early MAE. C25 works when medical-device/healthcare export narrative maps into overseas channel expansion, repeat consumable demand, ASP/mix, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C25_positive_requires_export_channel_repeat_consumable_margin_revision_bridge_not_medical_device_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R7L94_C25_RAY_2024_DENTAL_DEVICE_EXPORT_RECOVERY_FALSE_STAGE2", "symbol": "228670", "company_name": "레이", "round": "R7", "loop": "94", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE_VS_DENTAL_DEVICE_EXPORT_FALSE_STAGE2_AND_DIAGNOSTIC_IMAGING_EVENT_CAP", "case_type": "failed_rerating_export_recovery_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R7L94_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE_EXPORT_RECOVERY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Dental-device export recovery watch had almost no forward MFE and then severe 90D/180D MAE. C25 Stage2 should not be awarded without visible export order recovery, distributor/channel sell-through, receivable/inventory normalization, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_dental_device_export_recovery_counts_without_channel_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2021 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R7L94_C25_DRTECH_2024_DIAGNOSTIC_IMAGING_DEVICE_EVENT_CAP_4B", "symbol": "214680", "company_name": "디알텍", "round": "R7", "loop": "94", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE_VS_DENTAL_DEVICE_EXPORT_FALSE_STAGE2_AND_DIAGNOSTIC_IMAGING_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R7L94_C25_DRTECH_2024_STAGE4B_DIAGNOSTIC_IMAGING_DEVICE_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Diagnostic-imaging device / export event premium capped on the January spike and then suffered deep MAE before later noise rebounds. C25 should route bridge-missing diagnostic-device event premiums to 4B unless confirmed order, reimbursement/export channel, delivery cadence, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_diagnostic_imaging_device_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2016 corporate-action candidate. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R7L94_C25_PHARMARESEARCH_2024_STAGE2_ACTIONABLE_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE", "case_id": "R7L94_C25_PHARMARESEARCH_2024_MEDICAL_AESTHETIC_EXPORT_MARGIN_POSITIVE", "symbol": "214450", "company_name": "파마리서치", "round": "R7", "loop": "94", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE_VS_DENTAL_DEVICE_EXPORT_FALSE_STAGE2_AND_DIAGNOSTIC_IMAGING_EVENT_CAP", "sector": "medical_aesthetic_export_repeat_consumable_margin", "primary_archetype": "export_channel_repeat_consumable_ASP_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-23", "entry_date": "2024-02-23", "entry_price": 94700.0, "evidence_available_at_that_date": "medical aesthetic / regenerative product export channel, repeat consumable demand, ASP/mix and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["export_channel_expansion_proxy", "repeat_consumable_demand_proxy", "ASP_mix_bridge_proxy", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "very_high_MFE180", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_medical_aesthetic_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214450/2024.csv", "profile_path": "atlas/symbol_profiles/214/214450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 25.66, "MFE_90D_pct": 66.21, "MFE_180D_pct": 145.0, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -8.34, "MAE_90D_pct": -8.34, "MAE_180D_pct": -8.34, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-16", "peak_price": 232000.0, "drawdown_after_peak_pct": -7.11, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_medical_aesthetic_valuation_4B_watch_needed", "four_b_evidence_type": ["export_channel_bridge", "repeat_consumable_margin", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_medical_aesthetic_export_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R7L94_C25_214450_2024-02-23_94700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L94_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE_EXPORT_RECOVERY", "case_id": "R7L94_C25_RAY_2024_DENTAL_DEVICE_EXPORT_RECOVERY_FALSE_STAGE2", "symbol": "228670", "company_name": "레이", "round": "R7", "loop": "94", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE_VS_DENTAL_DEVICE_EXPORT_FALSE_STAGE2_AND_DIAGNOSTIC_IMAGING_EVENT_CAP", "sector": "dental_device_export_recovery_watch", "primary_archetype": "dental_device_export_recovery_without_channel_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 21900.0, "evidence_available_at_that_date": "dental-device export recovery watch without confirmed distributor sell-through, receivable/inventory normalization or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["dental_device_export_recovery_watch", "channel_restocking_expectation", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["near_zero_MFE30", "deep_MAE90", "channel_margin_revision_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/228/228670/2024.csv", "profile_path": "atlas/symbol_profiles/228/228670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.14, "MFE_90D_pct": 1.14, "MFE_180D_pct": 1.14, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -27.85, "MAE_90D_pct": -49.45, "MAE_180D_pct": -49.45, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-24", "peak_price": 22150.0, "drawdown_after_peak_pct": -50.07, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.99, "four_b_full_window_peak_proximity": 0.99, "four_b_timing_verdict": "dental_device_export_recovery_watch_was_false_stage2_due_missing_channel_margin_revision_bridge", "four_b_evidence_type": ["medical_device_export_recovery_watch", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_dental_device_export_recovery_without_channel_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_dental_device_export_recovery_counts_without_channel_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2021_CA", "same_entry_group_id": "R7L94_C25_228670_2024-01-24_21900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L94_C25_DRTECH_2024_STAGE4B_DIAGNOSTIC_IMAGING_DEVICE_EVENT_CAP", "case_id": "R7L94_C25_DRTECH_2024_DIAGNOSTIC_IMAGING_DEVICE_EVENT_CAP_4B", "symbol": "214680", "company_name": "디알텍", "round": "R7", "loop": "94", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE_VS_DENTAL_DEVICE_EXPORT_FALSE_STAGE2_AND_DIAGNOSTIC_IMAGING_EVENT_CAP", "sector": "diagnostic_imaging_device_export_event_premium", "primary_archetype": "diagnostic_imaging_device_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-09", "entry_date": "2024-01-09", "entry_price": 4890.0, "evidence_available_at_that_date": "diagnostic-imaging device / medical export event premium after January spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["diagnostic_imaging_device_event", "medical_device_export_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "order_reimbursement_export_channel_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214680/2024.csv", "profile_path": "atlas/symbol_profiles/214/214680.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.09, "MFE_90D_pct": 4.09, "MFE_180D_pct": 4.09, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -22.99, "MAE_90D_pct": -39.67, "MAE_180D_pct": -39.67, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-09", "peak_price": 5090.0, "drawdown_after_peak_pct": -42.53, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing_diagnostic_imaging_device_event_cap", "four_b_evidence_type": ["medical_device_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_diagnostic_imaging_device_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_diagnostic_imaging_device_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2016_CA", "same_entry_group_id": "R7L94_C25_214680_2024-01-09_4890", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L94_C25_PHARMARESEARCH_2024_MEDICAL_AESTHETIC_EXPORT_MARGIN_POSITIVE", "trigger_id": "R7L94_C25_PHARMARESEARCH_2024_STAGE2_ACTIONABLE_MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE", "symbol": "214450", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 40, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 55, "policy_or_regulatory_score": 25, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "medical_aesthetic_export_margin_positive", "MFE_90D_pct": 66.21, "MAE_90D_pct": -8.34, "score_return_alignment_label": "medical_aesthetic_export_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L94_C25_RAY_2024_DENTAL_DEVICE_EXPORT_RECOVERY_FALSE_STAGE2", "trigger_id": "R7L94_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_DEVICE_EXPORT_RECOVERY", "symbol": "228670", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 51, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "dental_device_export_recovery_false_stage2", "MFE_90D_pct": 1.14, "MAE_90D_pct": -49.45, "score_return_alignment_label": "dental_device_export_recovery_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_dental_device_export_recovery_counts_without_channel_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L94_C25_DRTECH_2024_DIAGNOSTIC_IMAGING_DEVICE_EVENT_CAP_4B", "trigger_id": "R7L94_C25_DRTECH_2024_STAGE4B_DIAGNOSTIC_IMAGING_DEVICE_EVENT_CAP", "symbol": "214680", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "diagnostic_imaging_device_event_cap_4B_guard", "MFE_90D_pct": 4.09, "MAE_90D_pct": -39.67, "score_return_alignment_label": "diagnostic_imaging_device_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_diagnostic_imaging_device_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": "94", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AESTHETIC_EXPORT_MARGIN_BRIDGE_VS_DENTAL_DEVICE_EXPORT_FALSE_STAGE2_AND_DIAGNOSTIC_IMAGING_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["medical_aesthetic_export_margin_positive", "dental_device_export_recovery_false_stage2", "diagnostic_imaging_device_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C25 rows need explicit export channel, repeat consumable/order durability, reimbursement/distributor sell-through, ASP/mix, margin or revision bridge before positive promotion.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that bridge-missing C25 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R7
completed_loop = 94
next_round = R8
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
