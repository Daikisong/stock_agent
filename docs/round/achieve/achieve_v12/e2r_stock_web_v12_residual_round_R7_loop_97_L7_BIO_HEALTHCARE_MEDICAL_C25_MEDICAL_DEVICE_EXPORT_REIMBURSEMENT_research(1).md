# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R7
scheduled_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE_VS_OPHTHALMIC_DEVICE_FALSE_STAGE2_AND_WEARABLE_INSULIN_DEVICE_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | reimbursement_export_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R7_loop_97_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
```

This file is the corrected final output for this execution. The scheduler state after R6 loop 97 is R7 / loop 97. R7 is the L7 bio/healthcare/medical round, and this run fills C25 medical-device export/reimbursement rather than repeating the immediately preceding R7 loop 96 C24 trial-data file, R7 loop 95 C23 commercialization file, or R6 loop 97 C22 insurance-reserve file.

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
reimbursement_export_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R7
scheduled_loop = 97
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
round_sector_consistency = pass
computed_next_round = R8
computed_next_loop = 97
```

C25 is a medical-device export/reimbursement bridge archetype. A device-export label is the showroom display; the signal becomes usable only when installed base, consumables, distributor sell-through, regulatory/reimbursement path, product mix, margin and revision are visible.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT = 33 rows / 16 symbols / good-bad Stage2 13-6 / 4B-4C 3-2
top covered symbols include 336570(6), 100120(3), 060280(2), 099190(2), 145720(2), 214150(2)
previous R7 loop-91 C25 symbols avoided: 206640, 043150, 246710
previous R7 loop-94 C25 symbols avoided: 214450, 228670, 214680
previous R7 loop-95 C23 symbols avoided: 000250, 085660, 293780
previous R7 loop-96 C24 symbols avoided: 310210, 203400, 084990
previous R6 loop-97 C22 symbols avoided: 032830, 088350, 000400
```

Selected rows avoid hard duplicates and top repeated C25 symbols:

```text
335890 / Stage2-Actionable / 2024-04-25
065510 / Stage2-Actionable / 2024-02-05
294090 / Stage4B / 2024-03-05
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
| 335890 | atlas/symbol_profiles/335/335890.json | selected 2024 window clean after old 2020 SPAC/CA candidate |
| 065510 | atlas/symbol_profiles/065/065510.json | no 2024 corporate-action candidate |
| 294090 | atlas/symbol_profiles/294/294090.json | selected 2024 window clean after old 2022 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R7L97_C25_VIOL_2024_AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_POSITIVE | 335890 | 2024-04-25 | yes | 180 | yes | yes | true |
| R7L97_C25_HUVITZ_2024_OPHTHALMIC_DEVICE_EXPORT_FALSE_STAGE2 | 065510 | 2024-02-05 | yes | 180 | yes | yes | true |
| R7L97_C25_EOFLOW_2024_WEARABLE_INSULIN_DEVICE_EVENT_CAP_4B | 294090 | 2024-03-05 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE | Positive Stage2 requires installed base, consumable/reorder economics, distributor quality, regulatory channel, margin and revision bridge. |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | OPHTHALMIC_DEVICE_EXPORT_FALSE_STAGE2 | Ophthalmic/diagnostic device export watch without sell-through and reimbursement/regulatory bridge can become false Stage2. |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | WEARABLE_INSULIN_DEVICE_EVENT_CAP_4B | Wearable medical-device event premium should route to 4B when regulatory, reimbursement and manufacturing bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R7L97_C25_VIOL_2024_AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_POSITIVE | 335890 | 비올 | positive | Aesthetic device export/consumable margin bridge produced positive MFE with acceptable MAE after April retest. |
| R7L97_C25_HUVITZ_2024_OPHTHALMIC_DEVICE_EXPORT_FALSE_STAGE2 | 065510 | 휴비츠 | counterexample | Ophthalmic-device export watch had a brief spike and then severe MAE. |
| R7L97_C25_EOFLOW_2024_WEARABLE_INSULIN_DEVICE_EVENT_CAP_4B | 294090 | 이오플로우 | counterexample / 4B | Wearable insulin-device regulatory/litigation premium capped almost immediately and then de-rated. |

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
| VIOL aesthetic-device export/consumable bridge | historical public/report proxy | true | true | shadow-only positive |
| Huvitz ophthalmic-device export false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| EOFlow wearable-insulin device event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 335890 | atlas/ohlcv_tradable_by_symbol_year/335/335890/2024.csv | atlas/symbol_profiles/335/335890.json |
| 065510 | atlas/ohlcv_tradable_by_symbol_year/065/065510/2024.csv | atlas/symbol_profiles/065/065510.json |
| 294090 | atlas/ohlcv_tradable_by_symbol_year/294/294090/2024.csv | atlas/symbol_profiles/294/294090.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R7L97_C25_VIOL_2024_STAGE2_ACTIONABLE_AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE | 335890 | Stage2-Actionable | 2024-04-25 | 9660 | positive | aesthetic-device export/consumable margin bridge worked |
| R7L97_C25_HUVITZ_2024_STAGE2_FALSE_POSITIVE_OPHTHALMIC_DEVICE_EXPORT_WATCH | 065510 | Stage2-Actionable | 2024-02-05 | 18220 | counterexample | ophthalmic-device export false Stage2 |
| R7L97_C25_EOFLOW_2024_STAGE4B_WEARABLE_INSULIN_DEVICE_EVENT_CAP | 294090 | Stage4B | 2024-03-05 | 6380 | counterexample/4B | wearable insulin-device event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L97_C25_VIOL_2024_STAGE2_ACTIONABLE_AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE | 9660 | 21.84 | -1.04 | 23.08 | -12.01 | 23.08 | -12.01 | 2024-07-08 | 11890 | -28.51 |
| R7L97_C25_HUVITZ_2024_STAGE2_FALSE_POSITIVE_OPHTHALMIC_DEVICE_EXPORT_WATCH | 18220 | 20.20 | -24.26 | 20.20 | -32.60 | 20.20 | -49.12 | 2024-02-05 | 21900 | -58.40 |
| R7L97_C25_EOFLOW_2024_STAGE4B_WEARABLE_INSULIN_DEVICE_EVENT_CAP | 6380 | 1.72 | -43.42 | 1.72 | -43.42 | 1.72 | -57.99 | 2024-03-05 | 6490 | -59.78 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C25 Stage2 needs installed base / consumables / distributor sell-through / regulatory-reimbursement / margin / revision bridge |
| reimbursement_export_guardrail | strengthen: device-export labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing device event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE device rows cannot promote without durable export/reimbursement bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether device/export narrative becomes installed-base, consumable and reimbursement evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 335890 | good_stage2_with_later_watch | Device-export/consumable margin bridge produced positive MFE and acceptable MAE. |
| 065510 | bad_stage2 | Ophthalmic-device export watch lacked distributor/reimbursement/margin bridge and suffered high MAE. |
| 294090 | good_4B | Wearable insulin-device event premium capped almost immediately and later drew down deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 065510 ophthalmic-device false Stage2 | 0.83 | 0.83 | false Stage2 due missing distributor sell-through / reimbursement / margin bridge |
| 294090 wearable insulin-device cap | 0.98 | 0.98 | good full-window 4B timing after regulatory/litigation relief premium |
| 335890 aesthetic-device bridge | n/a | n/a | positive Stage2, but later medical-device valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 065510 / 294090
```

No hard 4C candidate is introduced in this R7 loop 97 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L7 medical-device export/reimbursement cases, Stage2 requires verified installed base, consumable/reorder economics, distributor sell-through, regulatory clearance or reimbursement channel, manufacturing scale, product mix, margin, or revision bridge. Medical-device, export, reimbursement, diagnostic, wearable, aesthetic-device or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
rule = C25 should split true installed-base/consumable/regulatory/margin positives from device-export false Stage2 and wearable-device event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 14.99 | -29.34 | 0.67 | mixed; C25 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 14.99 | -29.34 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L7 installed-base/reimbursement/margin bridge required | 2 | 21.64 | -22.31 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C25 bridge vs event-cap split | 2 | 21.64 | -22.31 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing medical-device themes as positive | 1 | 23.08 | -12.01 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 335890 aesthetic-device bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 23.08 | -12.01 | aesthetic_device_export_consumable_margin_positive |
| 065510 ophthalmic-device false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 20.20 | -32.60 | ophthalmic_device_export_false_stage2 |
| 294090 wearable-device cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 1.72 | -43.42 | wearable_insulin_device_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE_VS_OPHTHALMIC_DEVICE_FALSE_STAGE2_AND_WEARABLE_INSULIN_DEVICE_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C25 VIOL aesthetic-device export/consumable positive, Huvitz ophthalmic-device export false Stage2, and EOFlow wearable-insulin device event-cap 4B while avoiding top repeated C25 and previous R7/R6 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, reimbursement_export_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: aesthetic_device_export_consumable_margin_positive, ophthalmic_device_export_false_stage2, wearable_insulin_device_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, reimbursement_export_guardrail, high_MAE_guardrail
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
shadow_weight,stage2_required_bridge,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,configured,C25_requires_installed_base_consumable_distributor_regulatory_reimbursement_margin_revision_bridge,0,"C25 Stage2 should require installed base, consumable/reorder economics, distributor sell-through, regulatory clearance or reimbursement channel, product mix, margin, or revision bridge, not medical-device/export label alone","VIOL positive worked; Huvitz and EOFlow event/watch rows failed positive-stage promotion","R7L97_C25_VIOL_2024_STAGE2_ACTIONABLE_AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE|R7L97_C25_HUVITZ_2024_STAGE2_FALSE_POSITIVE_OPHTHALMIC_DEVICE_EXPORT_WATCH|R7L97_C25_EOFLOW_2024_STAGE4B_WEARABLE_INSULIN_DEVICE_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,configured,cap_bridge_missing_ophthalmic_and_wearable_device_event_premiums_as_4B_watch,0,"Medical-device export and wearable-device event premiums can peak before sell-through, regulatory, reimbursement and margin bridge is proven","Huvitz had high MAE after a brief export-device spike; EOFlow showed clean 4B event-cap behavior after regulatory/litigation relief premium","R7L97_C25_HUVITZ_2024_STAGE2_FALSE_POSITIVE_OPHTHALMIC_DEVICE_EXPORT_WATCH|R7L97_C25_EOFLOW_2024_STAGE4B_WEARABLE_INSULIN_DEVICE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,configured,block_positive_stage_when_medical_device_theme_has_high_or_persistent_MAE_without_export_reimbursement_bridge,0,"High or persistent MAE after bridge-missing C25 entries should block Stage2/Stage3 promotion unless installed base, distributor, regulatory/reimbursement and margin evidence survives","Huvitz MAE90=-32.60 and EOFlow MAE90=-43.42","R7L97_C25_HUVITZ_2024_STAGE2_FALSE_POSITIVE_OPHTHALMIC_DEVICE_EXPORT_WATCH|R7L97_C25_EOFLOW_2024_STAGE4B_WEARABLE_INSULIN_DEVICE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R7L97_C25_VIOL_2024_AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_POSITIVE", "symbol": "335890", "company_name": "비올", "round": "R7", "loop": "97", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE_VS_OPHTHALMIC_DEVICE_FALSE_STAGE2_AND_WEARABLE_INSULIN_DEVICE_EVENT_CAP", "case_type": "structural_success_with_later_aesthetic_device_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R7L97_C25_VIOL_2024_STAGE2_ACTIONABLE_AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Aesthetic medical-device export / consumable margin bridge produced positive 30D/90D MFE with acceptable MAE after the April retest. C25 works when device-export narrative maps into installed-base expansion, consumable/reorder economics, distributor quality, regulatory clearance or reimbursement channel, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C25_positive_requires_installed_base_consumable_distributor_regulatory_margin_revision_bridge_not_device_export_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2020 SPAC/CA candidate. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R7L97_C25_HUVITZ_2024_OPHTHALMIC_DEVICE_EXPORT_FALSE_STAGE2", "symbol": "065510", "company_name": "휴비츠", "round": "R7", "loop": "97", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE_VS_OPHTHALMIC_DEVICE_FALSE_STAGE2_AND_WEARABLE_INSULIN_DEVICE_EVENT_CAP", "case_type": "failed_rerating_ophthalmic_device_export_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R7L97_C25_HUVITZ_2024_STAGE2_FALSE_POSITIVE_OPHTHALMIC_DEVICE_EXPORT_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Ophthalmic-device export / diagnostic-equipment watch showed a brief spike but then suffered persistent MAE. C25 Stage2 should not be awarded without confirmed overseas order cadence, distributor sell-through, regulatory/reimbursement bridge, product mix, margin and revision evidence.", "current_profile_verdict": "current_profile_false_positive_if_ophthalmic_device_export_watch_counts_without_distributor_sellthrough_regulatory_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No 2024 corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R7L97_C25_EOFLOW_2024_WEARABLE_INSULIN_DEVICE_EVENT_CAP_4B", "symbol": "294090", "company_name": "이오플로우", "round": "R7", "loop": "97", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE_VS_OPHTHALMIC_DEVICE_FALSE_STAGE2_AND_WEARABLE_INSULIN_DEVICE_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R7L97_C25_EOFLOW_2024_STAGE4B_WEARABLE_INSULIN_DEVICE_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Wearable insulin-device / regulatory-litigation relief event premium capped almost immediately and then de-rated. C25 should route bridge-missing medical-device event premiums to 4B unless regulatory path, injunction/litigation clarity, customer adoption, reimbursement, manufacturing scale and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_wearable_insulin_device_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2022 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R7L97_C25_VIOL_2024_STAGE2_ACTIONABLE_AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE", "case_id": "R7L97_C25_VIOL_2024_AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_POSITIVE", "symbol": "335890", "company_name": "비올", "round": "R7", "loop": "97", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE_VS_OPHTHALMIC_DEVICE_FALSE_STAGE2_AND_WEARABLE_INSULIN_DEVICE_EVENT_CAP", "sector": "aesthetic_device_export_consumable_margin", "primary_archetype": "installed_base_consumable_distributor_regulatory_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | reimbursement_export_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-25", "entry_date": "2024-04-25", "entry_price": 9660.0, "evidence_available_at_that_date": "aesthetic medical-device export, installed-base expansion, consumable/reorder margin, distributor quality and regulatory/channel bridge proxy after April retest; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["installed_base_proxy", "consumable_reorder_proxy", "export_distributor_quality_proxy", "regulatory_channel_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "positive_MFE90", "acceptable_MAE90"], "stage4b_evidence_fields": ["later_aesthetic_device_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/335/335890/2024.csv", "profile_path": "atlas/symbol_profiles/335/335890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 21.84, "MFE_90D_pct": 23.08, "MFE_180D_pct": 23.08, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.04, "MAE_90D_pct": -12.01, "MAE_180D_pct": -12.01, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 11890.0, "drawdown_after_peak_pct": -28.51, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_aesthetic_device_valuation_4B_watch_needed", "four_b_evidence_type": ["device_export_consumable_margin_bridge", "installed_base", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_aesthetic_device_export_consumable_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2020_SPAC_CA", "same_entry_group_id": "R7L97_C25_335890_2024-04-25_9660", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L97_C25_HUVITZ_2024_STAGE2_FALSE_POSITIVE_OPHTHALMIC_DEVICE_EXPORT_WATCH", "case_id": "R7L97_C25_HUVITZ_2024_OPHTHALMIC_DEVICE_EXPORT_FALSE_STAGE2", "symbol": "065510", "company_name": "휴비츠", "round": "R7", "loop": "97", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE_VS_OPHTHALMIC_DEVICE_FALSE_STAGE2_AND_WEARABLE_INSULIN_DEVICE_EVENT_CAP", "sector": "ophthalmic_device_export_diagnostic_equipment_watch", "primary_archetype": "ophthalmic_device_watch_without_distributor_sellthrough_regulatory_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | reimbursement_export_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-05", "entry_date": "2024-02-05", "entry_price": 18220.0, "evidence_available_at_that_date": "ophthalmic diagnostic-device export watch without confirmed distributor sell-through, reimbursement/regulatory channel, product mix or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["ophthalmic_device_export_watch", "diagnostic_equipment_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["brief_MFE_then_high_MAE", "sellthrough_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/065/065510/2024.csv", "profile_path": "atlas/symbol_profiles/065/065510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.2, "MFE_90D_pct": 20.2, "MFE_180D_pct": 20.2, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -24.26, "MAE_90D_pct": -32.6, "MAE_180D_pct": -49.12, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-05", "peak_price": 21900.0, "drawdown_after_peak_pct": -58.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.83, "four_b_full_window_peak_proximity": 0.83, "four_b_timing_verdict": "ophthalmic_device_export_watch_was_false_stage2_due_missing_distributor_sellthrough_regulatory_margin_bridge", "four_b_evidence_type": ["medical_device_export_premium", "bridge_missing", "high_MAE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_ophthalmic_device_export_watch_without_sellthrough_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_ophthalmic_device_export_watch_counts_without_distributor_sellthrough_regulatory_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R7L97_C25_065510_2024-02-05_18220", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L97_C25_EOFLOW_2024_STAGE4B_WEARABLE_INSULIN_DEVICE_EVENT_CAP", "case_id": "R7L97_C25_EOFLOW_2024_WEARABLE_INSULIN_DEVICE_EVENT_CAP_4B", "symbol": "294090", "company_name": "이오플로우", "round": "R7", "loop": "97", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE_VS_OPHTHALMIC_DEVICE_FALSE_STAGE2_AND_WEARABLE_INSULIN_DEVICE_EVENT_CAP", "sector": "wearable_insulin_device_regulatory_litigation_event_premium", "primary_archetype": "wearable_insulin_device_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | reimbursement_export_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-05", "entry_date": "2024-03-05", "entry_price": 6380.0, "evidence_available_at_that_date": "wearable insulin-device / regulatory-litigation relief event premium without confirmed injunction/litigation clarity, customer adoption, reimbursement or manufacturing scale bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["wearable_insulin_device_event", "regulatory_litigation_relief_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "low_MFE90", "deep_MAE90", "regulatory_reimbursement_scale_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/294/294090/2024.csv", "profile_path": "atlas/symbol_profiles/294/294090.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.72, "MFE_90D_pct": 1.72, "MFE_180D_pct": 1.72, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -43.42, "MAE_90D_pct": -43.42, "MAE_180D_pct": -57.99, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-05", "peak_price": 6490.0, "drawdown_after_peak_pct": -59.78, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing_wearable_insulin_device_event_cap", "four_b_evidence_type": ["wearable_insulin_device_event_premium", "regulatory_litigation_uncertainty", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_wearable_insulin_device_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_wearable_insulin_device_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2022_CA", "same_entry_group_id": "R7L97_C25_294090_2024-03-05_6380", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L97_C25_VIOL_2024_AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_POSITIVE", "trigger_id": "R7L97_C25_VIOL_2024_STAGE2_ACTIONABLE_AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE", "symbol": "335890", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 60, "customer_quality_score": 45, "policy_or_regulatory_score": 30, "valuation_repricing_score": 55, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 40, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 65, "customer_quality_score": 60, "policy_or_regulatory_score": 35, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "aesthetic_device_export_consumable_margin_positive", "MFE_90D_pct": 23.08, "MAE_90D_pct": -12.01, "score_return_alignment_label": "aesthetic_device_export_consumable_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L97_C25_HUVITZ_2024_OPHTHALMIC_DEVICE_EXPORT_FALSE_STAGE2", "trigger_id": "R7L97_C25_HUVITZ_2024_STAGE2_FALSE_POSITIVE_OPHTHALMIC_DEVICE_EXPORT_WATCH", "symbol": "065510", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 30, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "ophthalmic_device_export_false_stage2", "MFE_90D_pct": 20.2, "MAE_90D_pct": -32.6, "score_return_alignment_label": "ophthalmic_device_export_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_ophthalmic_device_export_watch_counts_without_distributor_sellthrough_regulatory_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L97_C25_EOFLOW_2024_WEARABLE_INSULIN_DEVICE_EVENT_CAP_4B", "trigger_id": "R7L97_C25_EOFLOW_2024_STAGE4B_WEARABLE_INSULIN_DEVICE_EVENT_CAP", "symbol": "294090", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 40, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 95, "legal_or_contract_risk_score": 70, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "wearable_insulin_device_event_cap_4B_guard", "MFE_90D_pct": 1.72, "MAE_90D_pct": -43.42, "score_return_alignment_label": "wearable_insulin_device_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_wearable_insulin_device_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": "97", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE_VS_OPHTHALMIC_DEVICE_FALSE_STAGE2_AND_WEARABLE_INSULIN_DEVICE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "reimbursement_export_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["aesthetic_device_export_consumable_margin_positive", "ophthalmic_device_export_false_stage2", "wearable_insulin_device_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C25 rows need explicit installed base, consumable/reorder economics, distributor sell-through, regulatory clearance or reimbursement channel, manufacturing scale, product mix, margin or revision bridge before positive promotion.
- In C25, bridge-missing medical-device event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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

## 27. Next Round State

```text
completed_round = R7
completed_loop = 97
next_round = R8
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
