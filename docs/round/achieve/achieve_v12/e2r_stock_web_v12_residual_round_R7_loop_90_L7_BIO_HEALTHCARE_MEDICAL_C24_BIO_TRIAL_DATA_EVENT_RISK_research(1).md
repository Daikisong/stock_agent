# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R7
scheduled_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = BIO_TRIAL_DATA_LICENSING_BRIDGE_VS_TRIAL_FAILURE_AND_REGULATORY_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R7_loop_90_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
```

This loop continues loop 90 after R6. It adds 3 C24 bio trial-data event-risk cases: one trial-data/licensing bridge positive, one trial-data false Stage2, and one binary regulatory/trial 4B event-cap counterexample.

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
scheduled_loop = 90
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
round_sector_consistency = pass
computed_next_round = R8
computed_next_loop = 90
```

R7 permits L7 bio/healthcare/medical research. Previous R7 loop 88 used C25 and R7 loop 89 used C23, so this loop fills C24 and tests whether clinical/trial events are backed by durable endpoint, partner/licensing, milestone, financing, or approval-to-commercialization bridges.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C24_BIO_TRIAL_DATA_EVENT_RISK = 30 rows / 20 symbols / good-bad Stage2 13-9 / 4B-4C 0-2
top covered symbols include 298380(3), 323990(3), 007390(2), 087010(2), 141080(2), 226950(2)
previous R7 loop-88 C25 symbols avoided: 214450, 228670, 335890
previous R7 loop-89 C23 symbols avoided: 000250, 086900, 068760
```

Selected rows avoid those repeated combinations and top repeated C24 symbols:

```text
397030 / Stage2-Actionable / 2024-03-06
365270 / Stage2-Actionable / 2024-03-20
067630 / Stage4B / 2024-03-25
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
| 397030 | atlas/symbol_profiles/397/397030.json | selected 2024 window clean after 2023-10/11 CA candidates |
| 365270 | atlas/symbol_profiles/365/365270.json | selected 2024 window clean; 2025 CA candidate outside window |
| 067630 | atlas/symbol_profiles/067/067630.json | selected 2024 window clean after 2021 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R7L90_C24_APRILBIO_2024_TRIAL_DATA_LICENSING_BRIDGE_POSITIVE | 397030 | 2024-03-06 | yes | 180 | yes | yes | true |
| R7L90_C24_CURACLE_2024_TRIAL_DATA_FAILURE_FALSE_STAGE2 | 365270 | 2024-03-20 | yes | 180 | yes | yes | true |
| R7L90_C24_HLBBIO_2024_REGULATORY_TRIAL_EVENT_CAP_4B | 067630 | 2024-03-25 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C24_BIO_TRIAL_DATA_EVENT_RISK | TRIAL_DATA_LICENSING_BRIDGE | Positive Stage2 requires endpoint/data quality plus partner, licensing, milestone, or runway bridge. |
| C24_BIO_TRIAL_DATA_EVENT_RISK | TRIAL_DATA_EVENT_FALSE_STAGE2 | Trial-data event without endpoint/partner/runway bridge can become severe-MAE false Stage2. |
| C24_BIO_TRIAL_DATA_EVENT_RISK | REGULATORY_TRIAL_EVENT_CAP_4B | Binary regulatory/trial premium should route to 4B when event risk is asymmetric. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R7L90_C24_APRILBIO_2024_TRIAL_DATA_LICENSING_BRIDGE_POSITIVE | 397030 | 에이프릴바이오 | positive | Trial-data / licensing bridge produced strong 30D/90D/180D MFE with controlled MAE. |
| R7L90_C24_CURACLE_2024_TRIAL_DATA_FAILURE_FALSE_STAGE2 | 365270 | 큐라클 | counterexample | Trial-data event spike had limited MFE and severe 90D/180D MAE. |
| R7L90_C24_HLBBIO_2024_REGULATORY_TRIAL_EVENT_CAP_4B | 067630 | HLB생명과학 | counterexample / 4B | Binary regulatory/trial premium capped near the March spike and drew down deeply. |

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
| AprilBio trial-data/licensing bridge | historical public/report proxy | true | true | shadow-only positive |
| Curacle trial-data event false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| HLB Life Science regulatory/trial cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 397030 | atlas/ohlcv_tradable_by_symbol_year/397/397030/2024.csv | atlas/symbol_profiles/397/397030.json |
| 365270 | atlas/ohlcv_tradable_by_symbol_year/365/365270/2024.csv | atlas/symbol_profiles/365/365270.json |
| 067630 | atlas/ohlcv_tradable_by_symbol_year/067/067630/2024.csv | atlas/symbol_profiles/067/067630.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R7L90_C24_APRILBIO_2024_STAGE2_ACTIONABLE_TRIAL_DATA_LICENSING_BRIDGE | 397030 | Stage2-Actionable | 2024-03-06 | 14260 | positive | trial-data/licensing bridge worked |
| R7L90_C24_CURACLE_2024_STAGE2_FALSE_POSITIVE_TRIAL_DATA_EVENT | 365270 | Stage2-Actionable | 2024-03-20 | 18630 | counterexample | trial-data false Stage2 |
| R7L90_C24_HLBBIO_2024_STAGE4B_REGULATORY_TRIAL_EVENT_CAP | 067630 | Stage4B | 2024-03-25 | 24300 | counterexample/4B | regulatory/trial event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L90_C24_APRILBIO_2024_STAGE2_ACTIONABLE_TRIAL_DATA_LICENSING_BRIDGE | 14260 | 34.29 | -4.14 | 56.73 | -5.47 | 81.63 | -5.47 | 2024-10-15 | 25900 | -41.58 |
| R7L90_C24_CURACLE_2024_STAGE2_FALSE_POSITIVE_TRIAL_DATA_EVENT | 18630 | 14.60 | -22.17 | 14.60 | -69.94 | 14.60 | -73.70 | 2024-04-08 | 21350 | -77.05 |
| R7L90_C24_HLBBIO_2024_STAGE4B_REGULATORY_TRIAL_EVENT_CAP | 24300 | 2.88 | -34.98 | 2.88 | -66.34 | 2.88 | -66.46 | 2024-03-26 | 25000 | -67.40 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C24 Stage2 needs endpoint/data quality plus partner/licensing/milestone/runway bridge |
| local_4b_watch_guard | strengthen: binary trial/regulatory premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: MAE90 below -50% blocks positive promotion without durable bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is data-event bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 397030 | good_stage2 | Data/licensing bridge produced strong MFE with controlled MAE. |
| 365270 | bad_stage2 | Trial-data event lacked durable endpoint/partner/runway bridge and drew down severely. |
| 067630 | good_4B | Binary regulatory/trial event premium capped before severe MAE. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 365270 trial-data false Stage2 | 0.87 | 0.87 | trial-data event spike was false Stage2 due endpoint/partner/runway risk |
| 067630 regulatory/trial cap | 1.00 | 1.00 | good full-window 4B timing |
| 397030 data/licensing bridge | n/a | n/a | positive Stage2, but later bio-event valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 365270 / 067630
```

No hard 4C candidate is proposed. R7 loop 90 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L7 bio trial-data event cases, Stage2 requires endpoint/data quality, partner/licensing economics, milestone/revenue bridge, financing runway, regulatory path, or commercialization bridge. Bio event, trial data, regulatory approval, or phase headline alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
rule = C24 should split data/licensing positives from trial-data false Stage2 and binary regulatory/trial event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 24.74 | -47.25 | 0.67 | mixed; C24 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 24.74 | -47.25 | 0.67 | weaker trial-event guard |
| P1 sector_specific_candidate_profile | L7 endpoint/partner bridge required | 2 | 35.67 | -37.71 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C24 bridge vs event-cap split | 2 | 35.67 | -37.71 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing trial events as positive | 1 | 56.73 | -5.47 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 397030 data/licensing bridge | 66 | Stage2-Watch | 75 | Stage2-Actionable | 56.73 | -5.47 | trial_data_licensing_bridge_positive |
| 365270 trial-data false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 14.60 | -69.94 | trial_data_event_false_stage2 |
| 067630 regulatory/trial cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 2.88 | -66.34 | regulatory_trial_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_LICENSING_BRIDGE_VS_TRIAL_FAILURE_AND_REGULATORY_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C24 trial-data/licensing positive, trial-data false Stage2, and binary regulatory/trial event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: trial_data_licensing_bridge_positive, trial_data_event_false_stage2, regulatory_trial_event_cap_4B
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
- C24 bio trial-data event-risk bridge vs event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,configured,C24_requires_data_quality_partner_milestone_or_runway_bridge,0,"C24 Stage2 should require data quality, endpoint durability, partner/licensing economics, milestone/revenue bridge, financing runway, or regulatory path, not bio event label alone","AprilBio positive worked; Curacle and HLB Life Science event rows failed positive-stage promotion","R7L90_C24_APRILBIO_2024_STAGE2_ACTIONABLE_TRIAL_DATA_LICENSING_BRIDGE|R7L90_C24_CURACLE_2024_STAGE2_FALSE_POSITIVE_TRIAL_DATA_EVENT|R7L90_C24_HLBBIO_2024_STAGE4B_REGULATORY_TRIAL_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,configured,cap_binary_trial_and_regulatory_event_premiums_as_4B_watch,0,"Binary trial/regulatory premiums can peak before endpoint/partner/commercialization bridge is proven and can create severe MAE","Curacle and HLB Life Science showed deep 90D/180D MAE after trial/regulatory event premium","R7L90_C24_CURACLE_2024_STAGE2_FALSE_POSITIVE_TRIAL_DATA_EVENT|R7L90_C24_HLBBIO_2024_STAGE4B_REGULATORY_TRIAL_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,configured,block_positive_stage_when_trial_event_MAE_is_severe_without_partner_runway_bridge,0,"Bio trial event rows with MAE90 below -50% should not promote to Stage2/Stage3 without durable endpoint, partner, financing, or approval-to-commercialization bridge","Curacle MAE90=-69.94 and HLB Life Science MAE90=-66.34","R7L90_C24_CURACLE_2024_STAGE2_FALSE_POSITIVE_TRIAL_DATA_EVENT|R7L90_C24_HLBBIO_2024_STAGE4B_REGULATORY_TRIAL_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"review for canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R7L90_C24_APRILBIO_2024_TRIAL_DATA_LICENSING_BRIDGE_POSITIVE", "symbol": "397030", "company_name": "에이프릴바이오", "round": "R7", "loop": "90", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_LICENSING_BRIDGE_VS_TRIAL_FAILURE_AND_REGULATORY_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R7L90_C24_APRILBIO_2024_STAGE2_ACTIONABLE_TRIAL_DATA_LICENSING_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Trial-data / platform licensing bridge produced strong 30D/90D/180D MFE with controlled MAE; C24 works when data quality, partner/licensing optionality, milestone economics, and financing runway are visible.", "current_profile_verdict": "current_profile_kept_but_C24_positive_requires_data_quality_partner_or_milestone_bridge_not_bio_event_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after 2023 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R7L90_C24_CURACLE_2024_TRIAL_DATA_FAILURE_FALSE_STAGE2", "symbol": "365270", "company_name": "큐라클", "round": "R7", "loop": "90", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_LICENSING_BRIDGE_VS_TRIAL_FAILURE_AND_REGULATORY_EVENT_CAP", "case_type": "failed_rerating_trial_data_risk", "positive_or_counterexample": "counterexample", "best_trigger": "R7L90_C24_CURACLE_2024_STAGE2_FALSE_POSITIVE_TRIAL_DATA_EVENT", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Trial-data event spike had limited forward MFE and then severe 90D/180D MAE; C24 Stage2 should not be awarded without verified endpoint quality, partner economics, and financing runway bridge.", "current_profile_verdict": "current_profile_false_positive_if_trial_data_event_counts_without_endpoint_partner_runway_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; 2025 CA candidate outside forward window. Source-proxy only."}
{"row_type": "case", "case_id": "R7L90_C24_HLBBIO_2024_REGULATORY_TRIAL_EVENT_CAP_4B", "symbol": "067630", "company_name": "HLB생명과학", "round": "R7", "loop": "90", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_LICENSING_BRIDGE_VS_TRIAL_FAILURE_AND_REGULATORY_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R7L90_C24_HLBBIO_2024_STAGE4B_REGULATORY_TRIAL_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Regulatory/trial approval premium capped around the late-March spike and then suffered severe drawdown; binary regulatory/trial event premium should route to 4B/watch unless approval-to-commercialization bridge survives.", "current_profile_verdict": "current_profile_4B_too_late_if_regulatory_trial_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Old CA candidates are outside selected 2024 window. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R7L90_C24_APRILBIO_2024_STAGE2_ACTIONABLE_TRIAL_DATA_LICENSING_BRIDGE", "case_id": "R7L90_C24_APRILBIO_2024_TRIAL_DATA_LICENSING_BRIDGE_POSITIVE", "symbol": "397030", "company_name": "에이프릴바이오", "round": "R7", "loop": "90", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_LICENSING_BRIDGE_VS_TRIAL_FAILURE_AND_REGULATORY_EVENT_CAP", "sector": "bio_trial_data_platform_licensing", "primary_archetype": "trial_data_partner_milestone_financing_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-06", "entry_date": "2024-03-06", "entry_price": 14260.0, "evidence_available_at_that_date": "trial data / platform licensing, partner optionality, milestone economics, and financing runway proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["trial_data_quality_proxy", "partner_or_licensing_optionality", "milestone_economics_proxy", "financing_runway_watch", "relative_strength_reversal"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "strong_MFE180", "controlled_MAE90"], "stage4b_evidence_fields": ["valuation_watch_after_bio_event_rerating"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/397/397030/2024.csv", "profile_path": "atlas/symbol_profiles/397/397030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 34.29, "MFE_90D_pct": 56.73, "MFE_180D_pct": 81.63, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -4.14, "MAE_90D_pct": -5.47, "MAE_180D_pct": -5.47, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-15", "peak_price": 25900.0, "drawdown_after_peak_pct": -41.58, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_bio_event_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "bio_event_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_trial_data_licensing_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2023_CA", "same_entry_group_id": "R7L90_C24_397030_2024-03-06_14260", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L90_C24_CURACLE_2024_STAGE2_FALSE_POSITIVE_TRIAL_DATA_EVENT", "case_id": "R7L90_C24_CURACLE_2024_TRIAL_DATA_FAILURE_FALSE_STAGE2", "symbol": "365270", "company_name": "큐라클", "round": "R7", "loop": "90", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_LICENSING_BRIDGE_VS_TRIAL_FAILURE_AND_REGULATORY_EVENT_CAP", "sector": "trial_data_event_endpoint_risk", "primary_archetype": "trial_data_event_without_endpoint_partner_runway_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-20", "entry_date": "2024-03-20", "entry_price": 18630.0, "evidence_available_at_that_date": "trial-data event / endpoint and partner expectation proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["trial_data_event", "endpoint_quality_watch", "partner_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "deep_MAE90", "endpoint_partner_runway_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/365/365270/2024.csv", "profile_path": "atlas/symbol_profiles/365/365270.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.6, "MFE_90D_pct": 14.6, "MFE_180D_pct": 14.6, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -22.17, "MAE_90D_pct": -69.94, "MAE_180D_pct": -73.7, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-08", "peak_price": 21350.0, "drawdown_after_peak_pct": -77.05, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.87, "four_b_full_window_peak_proximity": 0.87, "four_b_timing_verdict": "trial_data_event_spike_was_false_stage2_due_endpoint_partner_runway_risk", "four_b_evidence_type": ["bio_event_premium", "positioning_overheat", "endpoint_partner_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_trial_data_event_without_endpoint_partner_bridge", "current_profile_verdict": "current_profile_false_positive_if_trial_data_event_counts_without_endpoint_partner_runway_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L90_C24_365270_2024-03-20_18630", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L90_C24_HLBBIO_2024_STAGE4B_REGULATORY_TRIAL_EVENT_CAP", "case_id": "R7L90_C24_HLBBIO_2024_REGULATORY_TRIAL_EVENT_CAP_4B", "symbol": "067630", "company_name": "HLB생명과학", "round": "R7", "loop": "90", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_LICENSING_BRIDGE_VS_TRIAL_FAILURE_AND_REGULATORY_EVENT_CAP", "sector": "regulatory_trial_event_premium", "primary_archetype": "binary_regulatory_trial_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-25", "entry_date": "2024-03-25", "entry_price": 24300.0, "evidence_available_at_that_date": "binary regulatory/trial approval event premium after March spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["regulatory_trial_event_premium", "approval_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067630/2024.csv", "profile_path": "atlas/symbol_profiles/067/067630.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.88, "MFE_90D_pct": 2.88, "MFE_180D_pct": 2.88, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -34.98, "MAE_90D_pct": -66.34, "MAE_180D_pct": -66.46, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-26", "peak_price": 25000.0, "drawdown_after_peak_pct": -67.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_binary_regulatory_trial_event_cap", "four_b_evidence_type": ["regulatory_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_regulatory_trial_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2021_CA", "same_entry_group_id": "R7L90_C24_067630_2024-03-25_24300", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L90_C24_APRILBIO_2024_TRIAL_DATA_LICENSING_BRIDGE_POSITIVE", "trigger_id": "R7L90_C24_APRILBIO_2024_STAGE2_ACTIONABLE_TRIAL_DATA_LICENSING_BRIDGE", "symbol": "397030", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 60, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 40, "margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 65, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score", "legal_or_contract_risk_score", "dilution_cb_risk_score"], "component_delta_explanation": "trial_data_licensing_bridge_positive", "MFE_90D_pct": 56.73, "MAE_90D_pct": -5.47, "score_return_alignment_label": "trial_data_licensing_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L90_C24_CURACLE_2024_TRIAL_DATA_FAILURE_FALSE_STAGE2", "trigger_id": "R7L90_C24_CURACLE_2024_STAGE2_FALSE_POSITIVE_TRIAL_DATA_EVENT", "symbol": "365270", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 60, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 35, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 35, "accounting_trust_risk_score": 0}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score", "legal_or_contract_risk_score", "dilution_cb_risk_score"], "component_delta_explanation": "trial_data_event_false_stage2", "MFE_90D_pct": 14.6, "MAE_90D_pct": -69.94, "score_return_alignment_label": "trial_data_event_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_trial_data_event_counts_without_endpoint_partner_runway_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L90_C24_HLBBIO_2024_REGULATORY_TRIAL_EVENT_CAP_4B", "trigger_id": "R7L90_C24_HLBBIO_2024_STAGE4B_REGULATORY_TRIAL_EVENT_CAP", "symbol": "067630", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 60, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 35, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 35, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score", "legal_or_contract_risk_score", "dilution_cb_risk_score"], "component_delta_explanation": "regulatory_trial_event_cap_4B_guard", "MFE_90D_pct": 2.88, "MAE_90D_pct": -66.34, "score_return_alignment_label": "regulatory_trial_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_regulatory_trial_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": "90", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_LICENSING_BRIDGE_VS_TRIAL_FAILURE_AND_REGULATORY_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["trial_data_licensing_bridge_positive", "trial_data_event_false_stage2", "regulatory_trial_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 90
next_round = R8
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
