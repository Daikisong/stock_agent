# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R7
scheduled_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = AESTHETIC_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_EXPORT_FALSE_STAGE2_AND_ENERGY_BASED_DEVICE_EVENT_CAP
loop_objective = priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | medical_device_export_reimbursement_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R7_loop_99_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. A C20 duplicate artifact was generated during this run but is not the final artifact because C20 was already finalized immediately before. Priority 1 already added C03, C16, C04, C05, C15, C18 and C20, so C25 is the next unsupplemented Priority 1 gap below the 50-row practical calibration zone. Since R7 loop98 was used locally for C23/C24, this file uses R7 loop99 to avoid local round-loop collision.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_2_rolling_calibrated
previous_baseline_reference = e2r_2_1_stock_web_calibrated
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
medical_device_export_reimbursement_margin_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R7
scheduled_loop = 99
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C25 is a medical-device export / reimbursement archetype. A device approval or export headline is the clinic signboard; the usable signal is installed base, consumable recurrence, distributor reorder, reimbursement/country approval, ASP/mix, OPM and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT = 33 rows / Priority 1
top covered C25 symbols avoided: 228670, 214450, 335890, 065510, 043150, 041830
recent local Priority 0/1 artifacts accounted for: C08, C09, C01, C07, C06, C10, C14, C11, C02, C13, C19, C27, C12, C24, C28, C17, C23, C03, C16, C04, C05, C15, C18, C20
C20 duplicate generated during this run discarded from final output
```

Selected rows avoid hard duplicates and add new C25 trigger families:

```text
214150 / Stage2-Actionable / 2024-02-14
145720 / Stage2-Actionable / 2024-02-29
336570 / Stage4B / 2024-04-03
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
| 214150 | atlas/symbol_profiles/214/214150.json | selected 2024 window clean after old 2017 CA candidate |
| 145720 | atlas/symbol_profiles/145/145720.json | no corporate-action candidate |
| 336570 | atlas/symbol_profiles/336/336570.json | selected 2024 window clean after old 2022 CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R7L99_C25_CLASSYS_2024_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_POSITIVE | 214150 | 2024-02-14 | yes | 180 | yes | yes | true |
| R7L99_C25_DENTIUM_2024_DENTAL_EXPORT_REIMBURSEMENT_FALSE_STAGE2 | 145720 | 2024-02-29 | yes | 180 | yes | yes | true |
| R7L99_C25_WONTECH_2024_ENERGY_BASED_MEDICAL_DEVICE_EVENT_CAP_4B | 336570 | 2024-04-03 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE | Positive Stage2 requires installed base, consumable recurrence, distributor reorder, country approval/reimbursement clarity, OPM and revision bridge. |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | DENTAL_EXPORT_REIMBURSEMENT_FALSE_STAGE2 | Dental export watch without sell-through, distributor reorder and reimbursement/OPM bridge can become false Stage2. |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | ENERGY_BASED_MEDICAL_DEVICE_EVENT_CAP_4B | Energy-based aesthetic-device event premium should route to 4B when installed-base/consumable/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R7L99_C25_CLASSYS_2024_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_POSITIVE | 214150 | 클래시스 | positive | Aesthetic-device export/installed-base bridge produced strong 30D and very strong 90D/180D MFE. |
| R7L99_C25_DENTIUM_2024_DENTAL_EXPORT_REIMBURSEMENT_FALSE_STAGE2 | 145720 | 덴티움 | counterexample | Dental export/reimbursement watch had tiny forward MFE and persistent MAE without reorder/OPM bridge. |
| R7L99_C25_WONTECH_2024_ENERGY_BASED_MEDICAL_DEVICE_EVENT_CAP_4B | 336570 | 원텍 | counterexample / 4B | Energy-based device event premium capped after the April spike and then de-rated sharply. |

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
| Classys aesthetic medical-device export/reimbursement margin bridge | historical public/report proxy | true | true | shadow-only positive |
| Dentium dental export/reimbursement false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Wontech energy-based medical-device event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 214150 | atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv | atlas/symbol_profiles/214/214150.json |
| 145720 | atlas/ohlcv_tradable_by_symbol_year/145/145720/2024.csv | atlas/symbol_profiles/145/145720.json |
| 336570 | atlas/ohlcv_tradable_by_symbol_year/336/336570/2024.csv | atlas/symbol_profiles/336/336570.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R7L99_C25_CLASSYS_2024_STAGE2_ACTIONABLE_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE | 214150 | Stage2-Actionable | 2024-02-14 | 30000 | positive | medical-device installed-base/export margin bridge worked |
| R7L99_C25_DENTIUM_2024_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_REIMBURSEMENT_WATCH | 145720 | Stage2-Actionable | 2024-02-29 | 144200 | counterexample | dental export/reimbursement false Stage2 |
| R7L99_C25_WONTECH_2024_STAGE4B_ENERGY_BASED_MEDICAL_DEVICE_EVENT_CAP | 336570 | Stage4B | 2024-04-03 | 10850 | counterexample/4B | energy-based medical-device event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L99_C25_CLASSYS_2024_STAGE2_ACTIONABLE_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE | 30000 | 26.33 | -6.50 | 89.67 | -6.50 | 109.67 | -6.50 | 2024-10-21 | 62900 | n/a |
| R7L99_C25_DENTIUM_2024_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_REIMBURSEMENT_WATCH | 144200 | 2.98 | -13.11 | 2.98 | -25.80 | 2.98 | -31.14 | 2024-03-06 | 148500 | -33.13 |
| R7L99_C25_WONTECH_2024_STAGE4B_ENERGY_BASED_MEDICAL_DEVICE_EVENT_CAP | 10850 | 10.60 | -11.71 | 10.60 | -37.24 | 10.60 | -40.92 | 2024-04-22 | 12000 | -46.58 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C25 Stage2 needs installed base / consumables / export-country approval / distributor reorder / OPM / revision bridge |
| medical_device_export_reimbursement_margin_guardrail | strengthen: medical-device export/reimbursement label alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing dental and energy-based-device premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C25 rows cannot promote without durable installed-base/reimbursement/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether device-export narrative becomes installed-base, consumable, reimbursement/channel and OPM evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 214150 | good_stage2_with_later_watch | Installed-base/export margin bridge produced large MFE with shallow early MAE, but later valuation watch remains necessary. |
| 145720 | bad_stage2 | Dental export/reimbursement watch lacked sell-through/reorder/OPM bridge and produced tiny MFE with persistent MAE. |
| 336570 | good_4B | Energy-based medical-device premium peaked in April and later drew down without durable bridge. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 145720 dental export false Stage2 | 0.97 | 0.97 | false Stage2 due missing sell-through / distributor reorder / reimbursement / OPM bridge |
| 336570 energy-based device event cap | 0.90 | 0.90 | good full-window 4B timing after medical-device event premium |
| 214150 aesthetic device bridge | n/a | n/a | positive Stage2, but later medical-device valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = reimbursement_or_channel_break_watch_only for 145720
four_c_protection_label = channel_or_margin_break_watch_only for 336570
```

No hard 4C candidate is introduced in this C25 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L7 medical-device export/reimbursement cases, Stage2 requires verified installed base, consumable recurrence, country approval/reimbursement clarity, distributor reorder, ASP/mix, OPM and revision bridge. Device export, dental implant, aesthetic device, reimbursement, overseas approval or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
rule = C25 should split true installed-base/consumable/reimbursement-margin positives from dental export false Stage2 and device-event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 34.42 | -23.18 | 0.67 | mixed; C25 reimbursement/margin bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 34.42 | -23.18 | 0.67 | weaker C25 bridge split |
| P1 sector_specific_candidate_profile | L7 installed-base/reimbursement/OPM bridge required | 2 | 46.33 | -16.15 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C25 bridge vs event-cap split | 2 | 46.33 | -16.15 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing medical-device themes as positive | 1 | 89.67 | -6.50 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 214150 aesthetic device bridge | 66 | Stage2-Watch | 82 | Stage2-Actionable | 89.67 | -6.50 | medical_device_export_reimbursement_positive |
| 145720 dental export false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 2.98 | -25.80 | dental_export_false_stage2 |
| 336570 energy-based device cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 10.60 | -37.24 | medical_device_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_EXPORT_FALSE_STAGE2_AND_ENERGY_BASED_DEVICE_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C25 is the next unsupplemented Priority 1 archetype after C03/C16/C04/C05/C15/C18/C20 and remains below the practical 50-row calibration zone. This run adds Classys, Dentium and Wontech while avoiding top-covered C25 symbols 228670, 214450, 335890, 065510, 043150 and 041830."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, medical_device_export_reimbursement_margin_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: medical_device_export_reimbursement_positive, dental_export_false_stage2, medical_device_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, medical_device_export_reimbursement_margin_guardrail, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: priority1_canonical_archetype_rule_candidate
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
shadow_weight,stage2_required_bridge,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,configured,C25_requires_installed_base_consumable_export_approval_reimbursement_margin_revision_bridge,0,"C25 Stage2 should require installed base, consumable recurrence, export/country approval, reimbursement or channel clarity, distributor reorder, OPM and revision bridge, not medical-device export label alone","Classys positive worked; Dentium and Wontech event/watch rows failed positive-stage promotion","R7L99_C25_CLASSYS_2024_STAGE2_ACTIONABLE_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE|R7L99_C25_DENTIUM_2024_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_REIMBURSEMENT_WATCH|R7L99_C25_WONTECH_2024_STAGE4B_ENERGY_BASED_MEDICAL_DEVICE_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,configured,cap_bridge_missing_dental_and_energy_based_device_event_premiums_as_4B_watch,0,"Dental export and energy-based aesthetic device premiums can peak before sell-through, distributor reorder, reimbursement/approval and OPM bridge is proven","Dentium had tiny MFE and persistent MAE after late-February spike; Wontech showed 4B event-cap behavior after April device premium","R7L99_C25_DENTIUM_2024_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_REIMBURSEMENT_WATCH|R7L99_C25_WONTECH_2024_STAGE4B_ENERGY_BASED_MEDICAL_DEVICE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,configured,block_positive_stage_when_medical_device_export_theme_has_high_or_persistent_MAE_without_reimbursement_margin_bridge,0,"High or persistent MAE after bridge-missing C25 entries should block Stage2/Stage3 promotion unless installed-base, consumables, distributor reorder and OPM evidence survives","Dentium MAE90=-25.80 and Wontech MAE90=-37.24","R7L99_C25_DENTIUM_2024_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_REIMBURSEMENT_WATCH|R7L99_C25_WONTECH_2024_STAGE4B_ENERGY_BASED_MEDICAL_DEVICE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R7L99_C25_CLASSYS_2024_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_POSITIVE", "symbol": "214150", "company_name": "클래시스", "round": "R7", "loop": "99", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_EXPORT_FALSE_STAGE2_AND_ENERGY_BASED_DEVICE_EVENT_CAP", "case_type": "structural_success_with_later_aesthetic_device_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R7L99_C25_CLASSYS_2024_STAGE2_ACTIONABLE_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Aesthetic medical-device export / installed-base / consumable and reimbursement-adjacent margin bridge produced strong 30D and very strong 90D/180D MFE with shallow early MAE. C25 works when device-export momentum is tied to installed base, recurring consumables, country approvals, distributor quality, ASP/mix, OPM and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C25_positive_requires_installed_base_consumable_export_approval_reimbursement_margin_revision_bridge_not_device_export_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2017 corporate-action candidate. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R7L99_C25_DENTIUM_2024_DENTAL_EXPORT_REIMBURSEMENT_FALSE_STAGE2", "symbol": "145720", "company_name": "덴티움", "round": "R7", "loop": "99", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_EXPORT_FALSE_STAGE2_AND_ENERGY_BASED_DEVICE_EVENT_CAP", "case_type": "failed_rerating_dental_export_reimbursement_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R7L99_C25_DENTIUM_2024_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_REIMBURSEMENT_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Dental-device export/reimbursement watch after the late-February spike had tiny forward MFE and then persistent MAE. C25 Stage2 should not be awarded without export sell-through, distributor reorder, country reimbursement/approval clarity, implant volume, ASP/mix, OPM and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_dental_export_watch_counts_without_sellthrough_reorder_reimbursement_OPM_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R7L99_C25_WONTECH_2024_ENERGY_BASED_MEDICAL_DEVICE_EVENT_CAP_4B", "symbol": "336570", "company_name": "원텍", "round": "R7", "loop": "99", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_EXPORT_FALSE_STAGE2_AND_ENERGY_BASED_DEVICE_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R7L99_C25_WONTECH_2024_STAGE4B_ENERGY_BASED_MEDICAL_DEVICE_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Energy-based aesthetic device event premium capped around the April spike and then de-rated sharply. C25 should route bridge-missing medical-device export premiums to 4B unless installed-base growth, recurring consumables, overseas approvals, distributor reorder, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_energy_based_device_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2022 SPAC/name-change corporate-action candidate. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R7L99_C25_CLASSYS_2024_STAGE2_ACTIONABLE_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE", "case_id": "R7L99_C25_CLASSYS_2024_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_POSITIVE", "symbol": "214150", "company_name": "클래시스", "round": "R7", "loop": "99", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_EXPORT_FALSE_STAGE2_AND_ENERGY_BASED_DEVICE_EVENT_CAP", "sector": "aesthetic_medical_device_export_installed_base_consumable_margin", "primary_archetype": "installed_base_consumable_export_approval_reimbursement_margin_revision_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | medical_device_export_reimbursement_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-14", "entry_date": "2024-02-14", "entry_price": 30000.0, "evidence_available_at_that_date": "aesthetic medical-device export, installed-base expansion, consumable recurrence, overseas approval/distributor and margin/revision bridge proxy after February base; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["installed_base_proxy", "consumable_recurrence_proxy", "export_approval_proxy", "distributor_quality_proxy", "OPM_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "very_strong_MFE90", "very_strong_MFE180", "shallow_initial_MAE"], "stage4b_evidence_fields": ["later_aesthetic_device_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv", "profile_path": "atlas/symbol_profiles/214/214150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 26.33, "MFE_90D_pct": 89.67, "MFE_180D_pct": 109.67, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.5, "MAE_90D_pct": -6.5, "MAE_180D_pct": -6.5, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-21", "peak_price": 62900.0, "drawdown_after_peak_pct": "not_calculated", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_aesthetic_device_valuation_4B_watch_needed", "four_b_evidence_type": ["medical_device_export_margin_bridge", "installed_base_consumable", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_medical_device_export_reimbursement_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2017_CA", "same_entry_group_id": "R7L99_C25_214150_2024-02-14_30000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L99_C25_DENTIUM_2024_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_REIMBURSEMENT_WATCH", "case_id": "R7L99_C25_DENTIUM_2024_DENTAL_EXPORT_REIMBURSEMENT_FALSE_STAGE2", "symbol": "145720", "company_name": "덴티움", "round": "R7", "loop": "99", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_EXPORT_FALSE_STAGE2_AND_ENERGY_BASED_DEVICE_EVENT_CAP", "sector": "dental_implant_export_reimbursement_channel_watch", "primary_archetype": "dental_export_watch_without_sellthrough_reorder_reimbursement_OPM_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | medical_device_export_reimbursement_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-29", "entry_date": "2024-02-29", "entry_price": 144200.0, "evidence_available_at_that_date": "dental implant export/reimbursement recovery watch after late-February spike without confirmed sell-through, distributor reorder, reimbursement/approval clarity, implant volume, ASP/mix, OPM or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["dental_export_watch", "reimbursement_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["tiny_MFE90", "persistent_MAE90", "sellthrough_reorder_OPM_bridge_missing"], "stage4c_evidence_fields": ["reimbursement_or_channel_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/145/145720/2024.csv", "profile_path": "atlas/symbol_profiles/145/145720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.98, "MFE_90D_pct": 2.98, "MFE_180D_pct": 2.98, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -13.11, "MAE_90D_pct": -25.8, "MAE_180D_pct": -31.14, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-06", "peak_price": 148500.0, "drawdown_after_peak_pct": -33.13, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "dental_export_reimbursement_watch_was_false_stage2_due_missing_sellthrough_reorder_reimbursement_OPM_revision_bridge", "four_b_evidence_type": ["dental_export_premium", "bridge_missing", "tiny_MFE_high_MAE"], "four_c_protection_label": "reimbursement_or_channel_break_watch_only", "trigger_outcome_label": "bad_stage2_dental_export_reimbursement_watch_without_reorder_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_dental_export_watch_counts_without_sellthrough_reorder_reimbursement_OPM_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R7L99_C25_145720_2024-02-29_144200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L99_C25_WONTECH_2024_STAGE4B_ENERGY_BASED_MEDICAL_DEVICE_EVENT_CAP", "case_id": "R7L99_C25_WONTECH_2024_ENERGY_BASED_MEDICAL_DEVICE_EVENT_CAP_4B", "symbol": "336570", "company_name": "원텍", "round": "R7", "loop": "99", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_EXPORT_FALSE_STAGE2_AND_ENERGY_BASED_DEVICE_EVENT_CAP", "sector": "energy_based_aesthetic_medical_device_event_premium", "primary_archetype": "energy_based_medical_device_event_cap_4B", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | medical_device_export_reimbursement_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-03", "entry_date": "2024-04-03", "entry_price": 10850.0, "evidence_available_at_that_date": "energy-based aesthetic medical-device event premium without confirmed installed-base growth, recurring consumables, overseas approvals, distributor reorder, OPM or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["energy_based_device_event", "aesthetic_medical_device_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "installed_base_consumable_margin_bridge_recheck"], "stage4c_evidence_fields": ["channel_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336570/2024.csv", "profile_path": "atlas/symbol_profiles/336/336570.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.6, "MFE_90D_pct": 10.6, "MFE_180D_pct": 10.6, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -11.71, "MAE_90D_pct": -37.24, "MAE_180D_pct": -40.92, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-22", "peak_price": 12000.0, "drawdown_after_peak_pct": -46.58, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "good_full_window_4B_timing_energy_based_medical_device_event_cap_due_missing_installed_base_consumable_margin_bridge", "four_b_evidence_type": ["energy_based_medical_device_event_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "channel_or_margin_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_energy_based_medical_device_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_energy_based_medical_device_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2022_CA", "same_entry_group_id": "R7L99_C25_336570_2024-04-03_10850", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R7L99_C25_CLASSYS_2024_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R7L99_C25_CLASSYS_2024_STAGE2_ACTIONABLE_AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE", "symbol": "214150", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 45, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 65, "revision_score": 65, "relative_strength_score": 85, "customer_quality_score": 65, "policy_or_regulatory_score": 35, "valuation_repricing_score": 45, "execution_risk_score": 30, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "aesthetic_medical_device_export_reimbursement_margin_positive", "MFE_90D_pct": 89.67, "MAE_90D_pct": -6.5, "score_return_alignment_label": "medical_device_export_reimbursement_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R7L99_C25_DENTIUM_2024_DENTAL_EXPORT_REIMBURSEMENT_FALSE_STAGE2", "trigger_id": "R7L99_C25_DENTIUM_2024_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_REIMBURSEMENT_WATCH", "symbol": "145720", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 25, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 15, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "dental_export_reimbursement_false_stage2", "MFE_90D_pct": 2.98, "MAE_90D_pct": -25.8, "score_return_alignment_label": "dental_export_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_dental_export_watch_counts_without_sellthrough_reorder_reimbursement_OPM_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R7L99_C25_WONTECH_2024_ENERGY_BASED_MEDICAL_DEVICE_EVENT_CAP_4B", "trigger_id": "R7L99_C25_WONTECH_2024_STAGE4B_ENERGY_BASED_MEDICAL_DEVICE_EVENT_CAP", "symbol": "336570", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "energy_based_medical_device_event_cap_4B_guard", "MFE_90D_pct": 10.6, "MAE_90D_pct": -37.24, "score_return_alignment_label": "medical_device_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_energy_based_medical_device_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": "99", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DENTAL_EXPORT_FALSE_STAGE2_AND_ENERGY_BASED_DEVICE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "medical_device_export_reimbursement_margin_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["medical_device_export_reimbursement_positive", "dental_export_false_stage2", "medical_device_event_cap_4B"], "loop_contribution_label": "priority1_canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied calibrated profile.

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
- C25 rows need explicit installed base, consumable recurrence, country approval/reimbursement clarity, distributor reorder, ASP/mix, OPM and revision bridge before positive promotion.
- In C25, bridge-missing medical-device export/reimbursement rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C25 medical-device export/reimbursement rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R7
completed_loop = 99
completed_canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
coverage_scheduler_status = coverage_index_first
next_selection_rule = re-read V12_Research_No_Repeat_Index.md Priority 1 and local supplements
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
