# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R7
scheduled_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_IMAGING_EXPORT_FALSE_STAGE2_AND_BIOPRINTING_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R7_loop_91_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
```

This file is the corrected final output for this execution. The prior tool call recreated an R6/C22 file, but the scheduler state after R6 loop 91 is R7 / loop 91. This round uses C25 medical device / export / reimbursement behavior and avoids R7 loop 88, 89, and 90 symbol sets.

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
scheduled_loop = 91
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
round_sector_consistency = pass
computed_next_round = R8
computed_next_loop = 91
```

R7 permits L7 bio / healthcare / medical research. Previous R7 loop 90 used C24, loop 89 used C23, and loop 88 used C25 with different symbols. This loop returns to C25 with fresh non-top-covered symbols.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT = 33 rows / 16 symbols / good-bad Stage2 13-6 / 4B-4C 3-2
top covered symbols include 336570(6), 100120(3), 060280(2), 099190(2), 145720(2), 214150(2)
previous R7 loop-88 C25 symbols avoided: 214450, 228670, 335890
previous R7 loop-89 C23 symbols avoided: 000250, 086900, 068760
previous R7 loop-90 C24 symbols avoided: 397030, 365270, 067630
previous R6 loop-91 C22 symbols avoided: 085620, 000540, 000400
```

Selected rows avoid hard duplicates and top repeated C25 symbols:

```text
206640 / Stage2-Actionable / 2024-03-20
043150 / Stage2-Actionable / 2024-04-01
246710 / Stage4B / 2024-03-11
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
| 206640 | atlas/symbol_profiles/206/206640.json | selected 2024 window clean after 2015/2016 CA candidates |
| 043150 | atlas/symbol_profiles/043/043150.json | selected 2024 window clean after 2010-09-02 CA |
| 246710 | atlas/symbol_profiles/246/246710.json | selected 2024 window clean after 2022 CA candidates; 2025 CA outside window |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R7L91_C25_BODITECH_2024_DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT_POSITIVE | 206640 | 2024-03-20 | yes | 180 | yes | yes | true |
| R7L91_C25_VATECH_2024_DENTAL_IMAGING_EXPORT_FALSE_STAGE2 | 043150 | 2024-04-01 | yes | 180 | yes | yes | true |
| R7L91_C25_TNRBIOFAB_2024_BIOPRINTING_REGENERATIVE_DEVICE_EVENT_CAP_4B | 246710 | 2024-03-11 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE | Positive Stage2 requires export order, reimbursement, installed-base/consumable, and margin/revision bridge. |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | DENTAL_IMAGING_EXPORT_FALSE_STAGE2 | Dental imaging/export recovery label without confirmed bridge can become low-MFE false Stage2. |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | BIOPRINTING_REGENERATIVE_DEVICE_EVENT_CAP_4B | Regenerative-device theme premium should route to 4B when export/reimbursement bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R7L91_C25_BODITECH_2024_DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT_POSITIVE | 206640 | 바디텍메드 | positive | Diagnostic-device export/reimbursement bridge produced positive 90D/180D MFE with controlled MAE. |
| R7L91_C25_VATECH_2024_DENTAL_IMAGING_EXPORT_FALSE_STAGE2 | 043150 | 바텍 | counterexample | Dental imaging export recovery watch had near-zero forward MFE and persistent MAE. |
| R7L91_C25_TNRBIOFAB_2024_BIOPRINTING_REGENERATIVE_DEVICE_EVENT_CAP_4B | 246710 | 티앤알바이오팹 | counterexample / 4B | Bioprinting/regenerative-device premium capped near the March spike and de-rated. |

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
| Boditech diagnostic export/reimbursement bridge | historical public/report proxy | true | true | shadow-only positive |
| Vatech dental imaging export false Stage2 | historical public/report proxy | true | true | false-Stage2 guardrail |
| T&R Biofab regenerative device event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 206640 | atlas/ohlcv_tradable_by_symbol_year/206/206640/2024.csv | atlas/symbol_profiles/206/206640.json |
| 043150 | atlas/ohlcv_tradable_by_symbol_year/043/043150/2024.csv | atlas/symbol_profiles/043/043150.json |
| 246710 | atlas/ohlcv_tradable_by_symbol_year/246/246710/2024.csv | atlas/symbol_profiles/246/246710.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R7L91_C25_BODITECH_2024_STAGE2_ACTIONABLE_DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT | 206640 | Stage2-Actionable | 2024-03-20 | 15600 | positive | diagnostic device export/reimbursement bridge worked |
| R7L91_C25_VATECH_2024_STAGE2_FALSE_POSITIVE_DENTAL_IMAGING_EXPORT_RECOVERY | 043150 | Stage2-Actionable | 2024-04-01 | 31300 | counterexample | dental imaging export false Stage2 |
| R7L91_C25_TNRBIOFAB_2024_STAGE4B_BIOPRINTING_REGENERATIVE_DEVICE_CAP | 246710 | Stage4B | 2024-03-11 | 9290 | counterexample/4B | bioprinting regenerative device event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L91_C25_BODITECH_2024_STAGE2_ACTIONABLE_DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT | 15600 | 2.56 | -12.56 | 25.45 | -12.56 | 34.94 | -12.56 | 2024-08-19 | 21050 | -36.58 |
| R7L91_C25_VATECH_2024_STAGE2_FALSE_POSITIVE_DENTAL_IMAGING_EXPORT_RECOVERY | 31300 | 1.12 | -5.11 | 1.12 | -19.17 | 1.12 | -27.48 | 2024-04-01 | 31650 | -28.44 |
| R7L91_C25_TNRBIOFAB_2024_STAGE4B_BIOPRINTING_REGENERATIVE_DEVICE_CAP | 9290 | 6.46 | -29.60 | 6.46 | -34.02 | 6.46 | -37.78 | 2024-03-11 | 9890 | -44.08 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C25 Stage2 needs export/reimbursement/installed-base/consumable/margin bridge |
| local_4b_watch_guard | strengthen: medical-device and regenerative-device premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: high-MAE device-theme rows cannot promote without durable export/reimbursement bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is export/reimbursement bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 206640 | good_stage2 | Diagnostic-device export/reimbursement bridge produced positive 90D/180D MFE. |
| 043150 | bad_stage2 | Dental imaging export recovery watch lacked follow-through. |
| 246710 | good_4B | Regenerative-device theme premium capped around the event spike. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 043150 dental imaging false Stage2 | 0.99 | 0.99 | recovery watch was false Stage2 due missing export/reimbursement bridge |
| 246710 regenerative device cap | 1.00 | 1.00 | good full-window 4B timing |
| 206640 diagnostic bridge | n/a | n/a | positive Stage2, but later medical-device valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 043150 / 246710
```

No hard 4C candidate is proposed. R7 loop 91 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L7 medical-device export/reimbursement cases, Stage2 requires verified export order, reimbursement, installed base, consumable pull-through, clinical adoption, margin, or revision bridge. Device, dental, diagnostic, regenerative, bioprinting, or reimbursement label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
rule = C25 should split real export/reimbursement positives from dental-imaging false Stage2 and regenerative-device event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 11.01 | -21.92 | 0.67 | mixed; C25 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 11.01 | -21.92 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L7 export/reimbursement bridge required | 2 | 13.29 | -15.87 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C25 bridge vs event-cap split | 2 | 13.29 | -15.87 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing device themes as positive | 1 | 25.45 | -12.56 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 206640 diagnostic bridge | 66 | Stage2-Watch | 74 | Stage2-Actionable | 25.45 | -12.56 | diagnostic_device_export_reimbursement_positive |
| 043150 dental export false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 1.12 | -19.17 | dental_imaging_export_false_stage2 |
| 246710 regenerative cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 6.46 | -34.02 | bioprinting_regenerative_device_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_IMAGING_EXPORT_FALSE_STAGE2_AND_BIOPRINTING_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C25 diagnostic device export/reimbursement positive, dental imaging export false Stage2, and bioprinting/regenerative device event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: diagnostic_device_export_reimbursement_positive, dental_imaging_export_false_stage2, bioprinting_regenerative_device_event_cap_4B
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
- C25 medical-device export/reimbursement bridge vs event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,configured,C25_requires_export_reimbursement_installedbase_consumable_margin_bridge,0,"C25 Stage2 should require export order, reimbursement, installed base, consumable, clinical adoption, margin, or revision bridge, not medical-device/export label alone","Boditech positive worked; Vatech and T&R Biofab event/theme rows failed positive-stage promotion","R7L91_C25_BODITECH_2024_STAGE2_ACTIONABLE_DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT|R7L91_C25_VATECH_2024_STAGE2_FALSE_POSITIVE_DENTAL_IMAGING_EXPORT_RECOVERY|R7L91_C25_TNRBIOFAB_2024_STAGE4B_BIOPRINTING_REGENERATIVE_DEVICE_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,configured,cap_bridge_missing_device_and_regenerative_theme_premiums_as_4B_watch,0,"Medical-device, regenerative, and dental export premiums can peak before export/reimbursement bridge is proven","Vatech had near-zero forward MFE; T&R Biofab showed full-window event-cap behavior after March spike","R7L91_C25_VATECH_2024_STAGE2_FALSE_POSITIVE_DENTAL_IMAGING_EXPORT_RECOVERY|R7L91_C25_TNRBIOFAB_2024_STAGE4B_BIOPRINTING_REGENERATIVE_DEVICE_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,configured,block_positive_stage_when_medical_device_theme_has_high_MAE_without_export_reimbursement_bridge,0,"High MAE after a device/export/regenerative event should block positive Stage2/Stage3 promotion unless reimbursement and order evidence survives","T&R Biofab MAE90=-34.02; Vatech MAE180=-27.48","R7L91_C25_VATECH_2024_STAGE2_FALSE_POSITIVE_DENTAL_IMAGING_EXPORT_RECOVERY|R7L91_C25_TNRBIOFAB_2024_STAGE4B_BIOPRINTING_REGENERATIVE_DEVICE_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R7L91_C25_BODITECH_2024_DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT_POSITIVE", "symbol": "206640", "company_name": "바디텍메드", "round": "R7", "loop": "91", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_IMAGING_EXPORT_FALSE_STAGE2_AND_BIOPRINTING_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R7L91_C25_BODITECH_2024_STAGE2_ACTIONABLE_DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Diagnostic device export/reimbursement and margin-revision bridge produced a controlled drawdown then strong 90D/180D MFE. C25 works when export order, installed-base/consumable, reimbursement, and margin bridge are visible.", "current_profile_verdict": "current_profile_kept_but_C25_positive_requires_export_reimbursement_consumable_margin_bridge_not_medical_device_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after 2015/2016 SPAC/CA candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R7L91_C25_VATECH_2024_DENTAL_IMAGING_EXPORT_FALSE_STAGE2", "symbol": "043150", "company_name": "바텍", "round": "R7", "loop": "91", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_IMAGING_EXPORT_FALSE_STAGE2_AND_BIOPRINTING_EVENT_CAP", "case_type": "failed_rerating_export_recovery", "positive_or_counterexample": "counterexample", "best_trigger": "R7L91_C25_VATECH_2024_STAGE2_FALSE_POSITIVE_DENTAL_IMAGING_EXPORT_RECOVERY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Dental imaging / export recovery watch had near-zero forward MFE and then persistent MAE. C25 Stage2 should not be awarded without export order, reimbursement, installed-base utilization, consumable, or margin/revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_dental_imaging_export_recovery_counts_without_order_reimbursement_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2010 CA candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R7L91_C25_TNRBIOFAB_2024_BIOPRINTING_REGENERATIVE_DEVICE_EVENT_CAP_4B", "symbol": "246710", "company_name": "티앤알바이오팹", "round": "R7", "loop": "91", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_IMAGING_EXPORT_FALSE_STAGE2_AND_BIOPRINTING_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R7L91_C25_TNRBIOFAB_2024_STAGE4B_BIOPRINTING_REGENERATIVE_DEVICE_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Bioprinting/regenerative medical-device theme premium capped around the March spike and then de-rated. C25 should route bridge-missing device/regenerative event premiums to 4B unless export order, reimbursement, clinical adoption, and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_bioprinting_regenerative_device_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after 2022 CA candidates; 2025 CA candidates outside window. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R7L91_C25_BODITECH_2024_STAGE2_ACTIONABLE_DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "R7L91_C25_BODITECH_2024_DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT_POSITIVE", "symbol": "206640", "company_name": "바디텍메드", "round": "R7", "loop": "91", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_IMAGING_EXPORT_FALSE_STAGE2_AND_BIOPRINTING_EVENT_CAP", "sector": "diagnostic_device_export_reimbursement", "primary_archetype": "diagnostic_device_export_installed_base_reimbursement_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-20", "entry_date": "2024-03-20", "entry_price": 15600.0, "evidence_available_at_that_date": "diagnostic device export demand, reimbursement / installed-base consumable and margin-revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["diagnostic_device_export_proxy", "reimbursement_bridge_proxy", "installed_base_consumable_proxy", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["positive_MFE90", "positive_MFE180", "controlled_MAE90"], "stage4b_evidence_fields": ["valuation_watch_after_medical_device_export_recovery"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/206/206640/2024.csv", "profile_path": "atlas/symbol_profiles/206/206640.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.56, "MFE_90D_pct": 25.45, "MFE_180D_pct": 34.94, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -12.56, "MAE_90D_pct": -12.56, "MAE_180D_pct": -12.56, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-19", "peak_price": 21050.0, "drawdown_after_peak_pct": -36.58, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_medical_device_export_valuation_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "medical_device_export_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_diagnostic_device_export_reimbursement_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2016_CA", "same_entry_group_id": "R7L91_C25_206640_2024-03-20_15600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L91_C25_VATECH_2024_STAGE2_FALSE_POSITIVE_DENTAL_IMAGING_EXPORT_RECOVERY", "case_id": "R7L91_C25_VATECH_2024_DENTAL_IMAGING_EXPORT_FALSE_STAGE2", "symbol": "043150", "company_name": "바텍", "round": "R7", "loop": "91", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_IMAGING_EXPORT_FALSE_STAGE2_AND_BIOPRINTING_EVENT_CAP", "sector": "dental_imaging_export_recovery", "primary_archetype": "dental_imaging_export_recovery_without_reimbursement_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-01", "entry_date": "2024-04-01", "entry_price": 31300.0, "evidence_available_at_that_date": "dental imaging / export recovery watch and reimbursement/margin bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["dental_imaging_export_recovery_watch", "relative_strength_watch", "reimbursement_margin_bridge_unverified"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["near_zero_MFE90", "export_reimbursement_margin_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/043/043150/2024.csv", "profile_path": "atlas/symbol_profiles/043/043150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.12, "MFE_90D_pct": 1.12, "MFE_180D_pct": 1.12, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -5.11, "MAE_90D_pct": -19.17, "MAE_180D_pct": -27.48, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-01", "peak_price": 31650.0, "drawdown_after_peak_pct": -28.44, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.99, "four_b_full_window_peak_proximity": 0.99, "four_b_timing_verdict": "dental_imaging_export_recovery_watch_was_false_stage2_due_missing_bridge", "four_b_evidence_type": ["medical_device_export_watch", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_dental_imaging_export_recovery_without_bridge", "current_profile_verdict": "current_profile_false_positive_if_dental_imaging_export_recovery_counts_without_order_reimbursement_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2010_CA", "same_entry_group_id": "R7L91_C25_043150_2024-04-01_31300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L91_C25_TNRBIOFAB_2024_STAGE4B_BIOPRINTING_REGENERATIVE_DEVICE_CAP", "case_id": "R7L91_C25_TNRBIOFAB_2024_BIOPRINTING_REGENERATIVE_DEVICE_EVENT_CAP_4B", "symbol": "246710", "company_name": "티앤알바이오팹", "round": "R7", "loop": "91", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_IMAGING_EXPORT_FALSE_STAGE2_AND_BIOPRINTING_EVENT_CAP", "sector": "bioprinting_regenerative_medical_device_event", "primary_archetype": "bioprinting_regenerative_device_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-11", "entry_date": "2024-03-11", "entry_price": 9290.0, "evidence_available_at_that_date": "bioprinting / regenerative medical-device theme premium after March spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["bioprinting_device_theme", "regenerative_medical_device_event", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_forward_followthrough", "export_reimbursement_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/246/246710/2024.csv", "profile_path": "atlas/symbol_profiles/246/246710.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.46, "MFE_90D_pct": 6.46, "MFE_180D_pct": 6.46, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -29.6, "MAE_90D_pct": -34.02, "MAE_180D_pct": -37.78, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-11", "peak_price": 9890.0, "drawdown_after_peak_pct": -44.08, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_bioprinting_regenerative_device_event_cap", "four_b_evidence_type": ["medical_device_theme_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_bioprinting_regenerative_device_theme", "current_profile_verdict": "current_profile_4B_too_late_if_bioprinting_regenerative_device_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2022_CA", "same_entry_group_id": "R7L91_C25_246710_2024-03-11_9290", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L91_C25_BODITECH_2024_DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT_POSITIVE", "trigger_id": "R7L91_C25_BODITECH_2024_STAGE2_ACTIONABLE_DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "206640", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 65, "customer_quality_score": 30, "policy_or_regulatory_score": 30, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 50, "backlog_visibility_score": 45, "margin_bridge_score": 55, "revision_score": 50, "relative_strength_score": 60, "customer_quality_score": 45, "policy_or_regulatory_score": 40, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "diagnostic_device_export_reimbursement_positive", "MFE_90D_pct": 25.45, "MAE_90D_pct": -12.56, "score_return_alignment_label": "diagnostic_device_export_reimbursement_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L91_C25_VATECH_2024_DENTAL_IMAGING_EXPORT_FALSE_STAGE2", "trigger_id": "R7L91_C25_VATECH_2024_STAGE2_FALSE_POSITIVE_DENTAL_IMAGING_EXPORT_RECOVERY", "symbol": "043150", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 65, "customer_quality_score": 30, "policy_or_regulatory_score": 30, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "dental_imaging_export_false_stage2", "MFE_90D_pct": 1.12, "MAE_90D_pct": -19.17, "score_return_alignment_label": "dental_imaging_export_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_dental_imaging_export_recovery_counts_without_order_reimbursement_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L91_C25_TNRBIOFAB_2024_BIOPRINTING_REGENERATIVE_DEVICE_EVENT_CAP_4B", "trigger_id": "R7L91_C25_TNRBIOFAB_2024_STAGE4B_BIOPRINTING_REGENERATIVE_DEVICE_CAP", "symbol": "246710", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 65, "customer_quality_score": 30, "policy_or_regulatory_score": 30, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "bioprinting_regenerative_device_event_cap_4B_guard", "MFE_90D_pct": 6.46, "MAE_90D_pct": -34.02, "score_return_alignment_label": "bioprinting_regenerative_device_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_bioprinting_regenerative_device_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": "91", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "DIAGNOSTIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_IMAGING_EXPORT_FALSE_STAGE2_AND_BIOPRINTING_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["diagnostic_device_export_reimbursement_positive", "dental_imaging_export_false_stage2", "bioprinting_regenerative_device_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_loop = 91
next_round = R8
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
