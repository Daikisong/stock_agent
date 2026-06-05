# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R7
scheduled_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = AESTHETIC_MEDICAL_DEVICE_EXPORT_REORDER_VS_DENTAL_AND_DEVICE_THEME_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R7_loop_88_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
```

This loop continues loop 88 after R6. It adds 3 C25 medical-device cases: one aesthetic export/reorder positive, one dental-device false Stage2, and one aesthetic-device 4B event-cap counterexample.

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
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R7
scheduled_loop = 88
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
round_sector_consistency = pass
computed_next_round = R8
computed_next_loop = 88
```

R7 permits L7 bio/healthcare/medical research. C25 has meaningful but not saturated coverage, and this loop avoids the high-repeat C25 symbols by focusing on a clean medical-device export/reimbursement split.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT = 33 rows / 16 symbols / good-bad Stage2 13-6 / 4B-4C 3-2
top covered symbols include 336570(6), 100120(3), 060280(2), 099190(2), 145720(2), 214150(2)
```

Selected rows avoid those repeated combinations:

```text
214450 / Stage2-Actionable / 2024-03-25
228670 / Stage2-Actionable / 2024-01-08
335890 / Stage4B / 2024-04-01
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
| 228670 | atlas/symbol_profiles/228/228670.json | selected 2024 window clean; CA candidates are 2021-06-03 and 2021-06-23 |
| 335890 | atlas/symbol_profiles/335/335890.json | selected 2024 window clean after 2020-11-26 SPAC/merger CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R7L88_C25_PHARMARESEARCH_2024_AESTHETIC_EXPORT_REORDER_POSITIVE | 214450 | 2024-03-25 | yes | 180 | yes | yes | true |
| R7L88_C25_RAY_2024_DENTAL_DEVICE_FALSE_STAGE2 | 228670 | 2024-01-08 | yes | 180 | yes | yes | true |
| R7L88_C25_VIOL_2024_AESTHETIC_DEVICE_EVENT_CAP_4B | 335890 | 2024-04-01 | yes | 180 | yes | yes-after-2020-CA | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | AESTHETIC_EXPORT_REORDER_MARGIN_BRIDGE | Positive Stage2 requires export reorder, channel quality, installed-base/repeat demand, and margin/revision bridge. |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | DENTAL_DEVICE_FALSE_STAGE2 | Dental-device rebound without order/reimbursement/margin bridge can be weak-MFE, high-MAE false Stage2. |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | AESTHETIC_DEVICE_EVENT_CAP | Aesthetic-device theme premium should route to 4B unless export/reorder bridge is verified. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R7L88_C25_PHARMARESEARCH_2024_AESTHETIC_EXPORT_REORDER_POSITIVE | 214450 | 파마리서치 | positive | Aesthetic export/channel bridge produced high 90D/180D MFE with modest MAE. |
| R7L88_C25_RAY_2024_DENTAL_DEVICE_FALSE_STAGE2 | 228670 | 레이 | counterexample | Dental-device rebound failed; weak MFE and deep MAE. |
| R7L88_C25_VIOL_2024_AESTHETIC_DEVICE_EVENT_CAP_4B | 335890 | 비올 | counterexample / 4B | Aesthetic-device premium capped quickly and drew down. |

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
| PharmaResearch export/reorder bridge | historical public/report proxy | true | true | shadow-only positive |
| Ray dental-device false Stage2 | historical public/report proxy | true | true | false-Stage2 guardrail |
| Viol aesthetic device event cap | historical public/report proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 214450 | atlas/ohlcv_tradable_by_symbol_year/214/214450/2024.csv | atlas/symbol_profiles/214/214450.json |
| 228670 | atlas/ohlcv_tradable_by_symbol_year/228/228670/2024.csv | atlas/symbol_profiles/228/228670.json |
| 335890 | atlas/ohlcv_tradable_by_symbol_year/335/335890/2024.csv | atlas/symbol_profiles/335/335890.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R7L88_C25_PHARMARESEARCH_2024_STAGE2_ACTIONABLE_AESTHETIC_EXPORT_REORDER | 214450 | Stage2-Actionable | 2024-03-25 | 98700 | positive | export/reorder bridge worked |
| R7L88_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_REBOUND | 228670 | Stage2-Actionable | 2024-01-08 | 24750 | counterexample | dental export rebound false Stage2 |
| R7L88_C25_VIOL_2024_STAGE4B_AESTHETIC_DEVICE_EVENT_CAP | 335890 | Stage4B | 2024-04-01 | 11730 | counterexample/4B | aesthetic device event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L88_C25_PHARMARESEARCH_2024_STAGE2_ACTIONABLE_AESTHETIC_EXPORT_REORDER | 98700 | 48.83 | -8.00 | 59.47 | -8.00 | 135.06 | -8.00 | 2024-10-16 | 232000 | -12.93 |
| R7L88_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_REBOUND | 24750 | 1.41 | -35.35 | 1.41 | -46.55 | 1.41 | -69.29 | 2024-01-09 | 25100 | -69.72 |
| R7L88_C25_VIOL_2024_STAGE4B_AESTHETIC_DEVICE_EVENT_CAP | 11730 | 2.56 | -19.78 | 2.56 | -36.15 | 2.56 | -36.15 | 2024-04-01 | 12030 | -37.74 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C25 Stage2 needs export reorder / reimbursement or margin bridge |
| local_4b_watch_guard | strengthen: device theme premium should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 214450 | good_stage2 | Export/reorder and margin bridge proxy aligned with strong upside. |
| 228670 | bad_stage2 | Dental-device rebound lacked order/reimbursement/margin bridge. |
| 335890 | good_4B | Aesthetic-device premium was capped without verified bridge. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 335890 aesthetic device event cap | 1.00 | 1.00 | good_full_window_4B_timing_aesthetic_device_event_cap |
| 228670 dental rebound false Stage2 | 0.01 | 0.01 | weak_MFE_high_MAE_false_stage2_dental_device_export_rebound |
| 214450 export reorder bridge | n/a | n/a | positive Stage2; later valuation watch only |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 228670 / 335890
```

No hard 4C candidate is proposed. C25 residual here is Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L7 medical-device cases, Stage2 requires verified export reorder, installed-base/channel quality, reimbursement or margin/revision bridge. Device label or aesthetic/dental theme momentum alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
rule = C25 should split export/reorder/margin-bridge positives from dental/aesthetic device rebound or theme-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 21.15 | -30.23 | 0.67 | mixed; C25 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 21.15 | -30.23 | 0.67 | weaker bridge/theme guard |
| P1 sector_specific_candidate_profile | L7 device export bridge required | 2 | 30.44 | -27.28 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C25 bridge vs event-cap split | 2 | 30.44 | -27.28 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject dental/aesthetic theme caps as positive | 1 | 59.47 | -8.00 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 214450 export/reorder | 66 | Stage2-Watch | 74 | Stage2-Actionable | 59.47 | -8.00 | aesthetic_device_export_reorder_positive |
| 228670 dental false Stage2 | 66 | Stage2-Actionable | 52 | Stage1/Watch | 1.41 | -46.55 | dental_device_export_rebound_false_stage2 |
| 335890 aesthetic cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 2.56 | -36.15 | aesthetic_device_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_MEDICAL_DEVICE_EXPORT_REORDER_VS_DENTAL_AND_DEVICE_THEME_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C25 aesthetic export/reorder positive, dental-device false Stage2, and aesthetic-device event-cap 4B split using non-top-covered symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: aesthetic_device_export_reorder_positive, dental_export_rebound_false_stage2, aesthetic_device_theme_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard
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
- C25 medical-device export/reimbursement bridge vs dental/aesthetic event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,configured,C25_requires_export_reorder_margin_or_reimbursement_bridge,0,"C25 Stage2 should require verified export reorder, installed-base/channel quality, reimbursement or margin/revision bridge, not medical-device label alone","PharmaResearch positive worked; Ray and Viol event/rebound rows failed positive-stage promotion","R7L88_C25_PHARMARESEARCH_2024_STAGE2_ACTIONABLE_AESTHETIC_EXPORT_REORDER|R7L88_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_REBOUND|R7L88_C25_VIOL_2024_STAGE4B_AESTHETIC_DEVICE_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,configured,cap_device_theme_premium_as_4B_watch,0,"Aesthetic/dental device premiums can peak before verified export reorder or reimbursement/margin evidence appears","Ray and Viol showed low MFE90 and high MAE90 after rebound/theme spikes","R7L88_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_REBOUND|R7L88_C25_VIOL_2024_STAGE4B_AESTHETIC_DEVICE_EVENT_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R7L88_C25_PHARMARESEARCH_2024_AESTHETIC_EXPORT_REORDER_POSITIVE", "symbol": "214450", "company_name": "파마리서치", "round": "R7", "loop": "88", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_MEDICAL_DEVICE_EXPORT_REORDER_VS_DENTAL_AND_DEVICE_THEME_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R7L88_C25_PHARMARESEARCH_2024_STAGE2_ACTIONABLE_AESTHETIC_EXPORT_REORDER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Aesthetic/medical-device export and reimbursement-like channel bridge produced high 90D/180D MFE with modest entry MAE.", "current_profile_verdict": "current_profile_kept_but_C25_positive_requires_export_reorder_margin_bridge_not_medical_device_label_only", "price_source": "Songdaiki/stock-web", "notes": "Source-proxy only; exact as-of export/reorder evidence URL remains pending, so no production weight delta."}
{"row_type": "case", "case_id": "R7L88_C25_RAY_2024_DENTAL_DEVICE_FALSE_STAGE2", "symbol": "228670", "company_name": "레이", "round": "R7", "loop": "88", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_MEDICAL_DEVICE_EXPORT_REORDER_VS_DENTAL_AND_DEVICE_THEME_EVENT_CAP", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R7L88_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_REBOUND", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Dental-device export/rebound setup failed: weak MFE, deep MAE, and persistent downtrend indicate Stage2 bridge was missing.", "current_profile_verdict": "current_profile_false_positive_if_dental_device_export_rebound_counts_without_order_reimbursement_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "New C25 symbol; source-proxy only."}
{"row_type": "case", "case_id": "R7L88_C25_VIOL_2024_AESTHETIC_DEVICE_EVENT_CAP_4B", "symbol": "335890", "company_name": "비올", "round": "R7", "loop": "88", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_MEDICAL_DEVICE_EXPORT_REORDER_VS_DENTAL_AND_DEVICE_THEME_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R7L88_C25_VIOL_2024_STAGE4B_AESTHETIC_DEVICE_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Aesthetic-device theme premium capped quickly; low forward MFE and high MAE support 4B/watch rather than structural Green.", "current_profile_verdict": "current_profile_4B_too_late_if_aesthetic_device_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "C25 aesthetic device event-cap counterexample; source-proxy only. Symbol later shows inactive_or_delisted_like status in stock-web profile, but selected 2024 180D window is tradable and clean after 2020 SPAC/merger CA candidate."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R7L88_C25_PHARMARESEARCH_2024_STAGE2_ACTIONABLE_AESTHETIC_EXPORT_REORDER", "case_id": "R7L88_C25_PHARMARESEARCH_2024_AESTHETIC_EXPORT_REORDER_POSITIVE", "symbol": "214450", "company_name": "파마리서치", "round": "R7", "loop": "88", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_MEDICAL_DEVICE_EXPORT_REORDER_VS_DENTAL_AND_DEVICE_THEME_EVENT_CAP", "sector": "aesthetic_medical_device_export", "primary_archetype": "aesthetic_device_export_reorder_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-25", "entry_date": "2024-03-25", "entry_price": 98700.0, "evidence_available_at_that_date": "aesthetic/medical-device export reorder, channel expansion, margin bridge proxy; exact as-of report URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["export_reorder_proxy", "channel_expansion", "margin_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["high_MFE90", "high_MFE180", "low_MAE_to_export_rerating_path"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_180D_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214450/2024.csv", "profile_path": "atlas/symbol_profiles/214/214450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 48.83, "MFE_90D_pct": 59.47, "MFE_180D_pct": 135.06, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -8.0, "MAE_90D_pct": -8.0, "MAE_180D_pct": -8.0, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-16", "peak_price": 232000.0, "drawdown_after_peak_pct": -12.93, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_aesthetic_export_reorder_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L88_C25_214450_2024-03-25_98700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L88_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_REBOUND", "case_id": "R7L88_C25_RAY_2024_DENTAL_DEVICE_FALSE_STAGE2", "symbol": "228670", "company_name": "레이", "round": "R7", "loop": "88", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_MEDICAL_DEVICE_EXPORT_REORDER_VS_DENTAL_AND_DEVICE_THEME_EVENT_CAP", "sector": "dental_device_export", "primary_archetype": "dental_device_export_rebound_false_stage2", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-08", "entry_date": "2024-01-08", "entry_price": 24750.0, "evidence_available_at_that_date": "dental-device export rebound / China-normalization proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["dental_device_export_rebound", "relative_strength_watch", "reimbursement_or_distribution_proxy"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE", "deep_MAE", "order_reimbursement_bridge_missing"], "stage4c_evidence_fields": ["demand_or_channel_break_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/228/228670/2024.csv", "profile_path": "atlas/symbol_profiles/228/228670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.41, "MFE_90D_pct": 1.41, "MFE_180D_pct": 1.41, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -35.35, "MAE_90D_pct": -46.55, "MAE_180D_pct": -69.29, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-09", "peak_price": 25100.0, "drawdown_after_peak_pct": -69.72, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.01, "four_b_full_window_peak_proximity": 0.01, "four_b_timing_verdict": "weak_MFE_high_MAE_false_stage2_dental_device_export_rebound", "four_b_evidence_type": ["margin_or_backlog_slowdown", "price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_dental_export_rebound_false_positive", "current_profile_verdict": "current_profile_false_positive_if_dental_device_export_rebound_counts_without_order_reimbursement_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L88_C25_228670_2024-01-08_24750", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L88_C25_VIOL_2024_STAGE4B_AESTHETIC_DEVICE_EVENT_CAP", "case_id": "R7L88_C25_VIOL_2024_AESTHETIC_DEVICE_EVENT_CAP_4B", "symbol": "335890", "company_name": "비올", "round": "R7", "loop": "88", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_MEDICAL_DEVICE_EXPORT_REORDER_VS_DENTAL_AND_DEVICE_THEME_EVENT_CAP", "sector": "aesthetic_medical_device_theme", "primary_archetype": "aesthetic_device_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-01", "entry_date": "2024-04-01", "entry_price": 11730.0, "evidence_available_at_that_date": "aesthetic-device premium and export-growth theme spike proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["aesthetic_device_theme", "export_growth_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/335/335890/2024.csv", "profile_path": "atlas/symbol_profiles/335/335890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.56, "MFE_90D_pct": 2.56, "MFE_180D_pct": 2.56, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -19.78, "MAE_90D_pct": -36.15, "MAE_180D_pct": -36.15, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-01", "peak_price": 12030.0, "drawdown_after_peak_pct": -37.74, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_aesthetic_device_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_aesthetic_device_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2020_SPAC_CA", "same_entry_group_id": "R7L88_C25_335890_2024-04-01_11730", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L88_C25_PHARMARESEARCH_2024_AESTHETIC_EXPORT_REORDER_POSITIVE", "trigger_id": "R7L88_C25_PHARMARESEARCH_2024_STAGE2_ACTIONABLE_AESTHETIC_EXPORT_REORDER", "symbol": "214450", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 15, "valuation_repricing_score": 55, "execution_risk_score": 40, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 55, "policy_or_regulatory_score": 20, "valuation_repricing_score": 50, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "aesthetic_device_export_reorder_positive", "MFE_90D_pct": 59.47, "MAE_90D_pct": -8.0, "score_return_alignment_label": "aesthetic_device_export_reorder_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L88_C25_RAY_2024_DENTAL_DEVICE_FALSE_STAGE2", "trigger_id": "R7L88_C25_RAY_2024_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_REBOUND", "symbol": "228670", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 15, "valuation_repricing_score": 55, "execution_risk_score": 40, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "dental_device_export_rebound_false_stage2", "MFE_90D_pct": 1.41, "MAE_90D_pct": -46.55, "score_return_alignment_label": "dental_device_export_rebound_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_dental_device_export_rebound_counts_without_order_reimbursement_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L88_C25_VIOL_2024_AESTHETIC_DEVICE_EVENT_CAP_4B", "trigger_id": "R7L88_C25_VIOL_2024_STAGE4B_AESTHETIC_DEVICE_EVENT_CAP", "symbol": "335890", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 15, "valuation_repricing_score": 55, "execution_risk_score": 40, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "aesthetic_device_event_cap_4B_guard", "MFE_90D_pct": 2.56, "MAE_90D_pct": -36.15, "score_return_alignment_label": "aesthetic_device_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_aesthetic_device_theme_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": "88", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_MEDICAL_DEVICE_EXPORT_REORDER_VS_DENTAL_AND_DEVICE_THEME_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["aesthetic_device_export_reorder_positive", "dental_export_rebound_false_stage2", "aesthetic_device_theme_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
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
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R7
completed_loop = 88
next_round = R8
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
