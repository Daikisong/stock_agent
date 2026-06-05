# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R7
scheduled_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE_VS_CLINICAL_EVENT_FALSE_STAGE2_AND_GENE_THERAPY_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_watch | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R7_loop_96_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
```

This file is the corrected final output for this execution. The scheduler state after R6 loop 96 is R7 / loop 96. R7 is the L7 bio/healthcare/medical round, and this run fills C24 bio trial-data event risk rather than repeating the immediately preceding R7 loop 95 C23 commercialization file or R7 loop 94 C25 medical-device file.

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
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R7
scheduled_loop = 96
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
round_sector_consistency = pass
computed_next_round = R8
computed_next_loop = 96
```

C24 is a trial-data bridge and event-risk archetype. A clinical-data headline is the lab door opening; the investable bridge is endpoint quality, mechanism credibility, cohort durability, partner/funding path, regulatory visibility, commercial path and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C24_BIO_TRIAL_DATA_EVENT_RISK = 30 rows / 20 symbols / good-bad Stage2 13-9 / 4B-4C 0-2 / reuse 10-10
top covered symbols include 298380(3), 323990(3), 007390(2), 087010(2), 141080(2), 226950(2)
previous R7 loop-90 C24 symbols avoided: 397030, 365270, 067630
previous R7 loop-91 C25 symbols avoided: 206640, 043150, 246710
previous R7 loop-92 C23 symbols avoided: 196170, 003850, 950160
previous R7 loop-93 C24 symbols avoided: 039200, 950220, 174900
previous R7 loop-94 C25 symbols avoided: 214450, 228670, 214680
previous R7 loop-95 C23 symbols avoided: 000250, 085660, 293780
previous R6 loop-96 C21 symbols avoided: 029780, 007330, 377300
```

Selected rows avoid hard duplicates and top repeated C24 symbols:

```text
310210 / Stage2-Actionable / 2024-02-06
203400 / Stage2-Actionable / 2024-06-10
084990 / Stage4B / 2024-02-06
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
| 310210 | atlas/symbol_profiles/310/310210.json | no corporate-action candidate |
| 203400 | atlas/symbol_profiles/203/203400.json | selected 2024 window clean after old 2015 CA and before 2025 CA candidates |
| 084990 | atlas/symbol_profiles/084/084990.json | selected 2024 window clean after old 2019/2020/2021 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R7L96_C24_VORONOI_2024_TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE_POSITIVE | 310210 | 2024-02-06 | yes | 180 | yes | yes | true |
| R7L96_C24_ABION_2024_CLINICAL_DATA_EVENT_FALSE_STAGE2 | 203400 | 2024-06-10 | yes | 180 | yes | yes | true |
| R7L96_C24_HELIXMITH_2024_GENE_THERAPY_EVENT_CAP_4B | 084990 | 2024-02-06 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C24_BIO_TRIAL_DATA_EVENT_RISK | TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE | Positive Stage2 requires endpoint quality, mechanism credibility, partner optionality, funding runway, regulatory path and revision bridge. |
| C24_BIO_TRIAL_DATA_EVENT_RISK | CLINICAL_DATA_FALSE_STAGE2 | Clinical-data event watch without endpoint/partner/funding bridge can become false Stage2. |
| C24_BIO_TRIAL_DATA_EVENT_RISK | GENE_THERAPY_EVENT_CAP_4B | Gene-therapy trial-data event premium should route to 4B when endpoint/funding/partner bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R7L96_C24_VORONOI_2024_TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE_POSITIVE | 310210 | 보로노이 | positive | Targeted-oncology pipeline-data bridge produced strong 30D/90D and very strong 180D MFE. |
| R7L96_C24_ABION_2024_CLINICAL_DATA_EVENT_FALSE_STAGE2 | 203400 | 에이비온 | counterexample | Clinical-data spike had low forward MFE and deep MAE without endpoint/partner/funding bridge. |
| R7L96_C24_HELIXMITH_2024_GENE_THERAPY_EVENT_CAP_4B | 084990 | 헬릭스미스 | counterexample / 4B | Gene-therapy trial event premium capped on the February spike and then drew down deeply. |

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
| Voronoi targeted-oncology pipeline data bridge | historical public/report proxy | true | true | shadow-only positive |
| Abion clinical-data event false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Helixmith gene-therapy trial event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 310210 | atlas/ohlcv_tradable_by_symbol_year/310/310210/2024.csv | atlas/symbol_profiles/310/310210.json |
| 203400 | atlas/ohlcv_tradable_by_symbol_year/203/203400/2024.csv | atlas/symbol_profiles/203/203400.json |
| 084990 | atlas/ohlcv_tradable_by_symbol_year/084/084990/2024.csv | atlas/symbol_profiles/084/084990.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R7L96_C24_VORONOI_2024_STAGE2_ACTIONABLE_TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE | 310210 | Stage2-Actionable | 2024-02-06 | 35050 | positive | targeted-oncology pipeline-data bridge worked |
| R7L96_C24_ABION_2024_STAGE2_FALSE_POSITIVE_CLINICAL_DATA_EVENT_WATCH | 203400 | Stage2-Actionable | 2024-06-10 | 12390 | counterexample | clinical-data event false Stage2 |
| R7L96_C24_HELIXMITH_2024_STAGE4B_GENE_THERAPY_TRIAL_EVENT_CAP | 084990 | Stage4B | 2024-02-06 | 5850 | counterexample/4B | gene-therapy trial event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L96_C24_VORONOI_2024_STAGE2_ACTIONABLE_TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE | 35050 | 38.94 | -10.13 | 47.22 | -19.12 | 239.23 | -19.12 | 2024-10-21 | 118900 | -16.40 |
| R7L96_C24_ABION_2024_STAGE2_FALSE_POSITIVE_CLINICAL_DATA_EVENT_WATCH | 12390 | 4.92 | -28.41 | 4.92 | -35.43 | 4.92 | -39.06 | 2024-06-10 | 13000 | -39.06 |
| R7L96_C24_HELIXMITH_2024_STAGE4B_GENE_THERAPY_TRIAL_EVENT_CAP | 5850 | 27.18 | -28.63 | 27.18 | -43.59 | 27.18 | -43.59 | 2024-02-06 | 7440 | -55.65 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C24 Stage2 needs endpoint quality / mechanism / partner / funding / regulatory / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing clinical and gene-therapy event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE bio trial event rows cannot promote without durable endpoint/partner bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether trial-data excitement becomes endpoint, partner, funding and regulatory bridge.

| symbol | stage quality | explanation |
|---|---|---|
| 310210 | good_stage2_with_later_watch | Pipeline-data bridge produced strong MFE, but later valuation watch remains necessary. |
| 203400 | bad_stage2 | Clinical-data event watch lacked endpoint/partner/funding bridge and produced low MFE with high MAE. |
| 084990 | good_4B | Gene-therapy trial premium capped on the February spike and later suffered deep drawdown. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 203400 clinical-data false Stage2 | 0.95 | 0.95 | false Stage2 due missing endpoint/partner/funding bridge |
| 084990 gene-therapy event cap | 0.79 | 0.79 | acceptable 4B because non-price bridge was missing and later MAE was deep |
| 310210 oncology pipeline bridge | n/a | n/a | positive Stage2, but later pipeline valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 203400 / 084990
```

No hard 4C candidate is introduced in this R7 loop 96 file. The counterexamples are bridge-missing / event-cap rows, not hard thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L7 bio trial-data event-risk cases, Stage2 requires verified endpoint quality, mechanism credibility, cohort durability, partner/funding path, regulatory visibility, commercial path, or revision bridge. Trial data, clinical event, oncology, gene therapy, pipeline, conference, publication or relative-strength label alone remains watch/4B/4C.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
rule = C24 should split true endpoint/partner/funding/regulatory positives from clinical-data false Stage2 and gene-therapy event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 26.44 | -32.71 | 0.67 | mixed; C24 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 26.44 | -32.71 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L7 endpoint/partner/funding bridge required | 2 | 26.07 | -27.28 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C24 bridge vs event-cap split | 2 | 26.07 | -27.28 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing clinical-data themes as positive | 1 | 47.22 | -19.12 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 310210 oncology pipeline bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 47.22 | -19.12 | targeted_oncology_pipeline_data_positive |
| 203400 clinical-data false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 4.92 | -35.43 | clinical_data_event_false_stage2 |
| 084990 gene-therapy cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 27.18 | -43.59 | gene_therapy_trial_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE_VS_CLINICAL_EVENT_FALSE_STAGE2_AND_GENE_THERAPY_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C24 Voronoi targeted-oncology pipeline-data positive, Abion clinical-data event false Stage2, and Helixmith gene-therapy trial-event cap 4B while avoiding top repeated C24 and previous R7/R6 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: targeted_oncology_pipeline_data_positive, clinical_data_event_false_stage2, gene_therapy_trial_event_cap_4B
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
- C24 bio trial-data event risk bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,configured,C24_requires_endpoint_quality_partner_optionality_funding_regulatory_revision_bridge,0,"C24 Stage2 should require endpoint quality, mechanism credibility, cohort durability, partner/funding path, regulatory visibility, commercial path, or revision bridge, not clinical-data/trial-event label alone","Voronoi positive worked; Abion and Helixmith event/watch rows failed positive-stage promotion","R7L96_C24_VORONOI_2024_STAGE2_ACTIONABLE_TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE|R7L96_C24_ABION_2024_STAGE2_FALSE_POSITIVE_CLINICAL_DATA_EVENT_WATCH|R7L96_C24_HELIXMITH_2024_STAGE4B_GENE_THERAPY_TRIAL_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,configured,cap_bridge_missing_clinical_trial_and_gene_therapy_event_premiums_as_4B_watch,0,"Clinical-data and gene-therapy event premiums can peak before endpoint, partner, funding and regulatory bridge is proven","Abion had low MFE after a clinical-data spike; Helixmith showed 4B event-cap behavior after the February gene-therapy spike","R7L96_C24_ABION_2024_STAGE2_FALSE_POSITIVE_CLINICAL_DATA_EVENT_WATCH|R7L96_C24_HELIXMITH_2024_STAGE4B_GENE_THERAPY_TRIAL_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,configured,block_positive_stage_when_bio_trial_event_has_high_or_persistent_MAE_without_endpoint_partner_bridge,0,"High or persistent MAE after bridge-missing C24 entries should block Stage2/Stage3 promotion unless endpoint, partner, funding and regulatory evidence survives","Abion MAE90=-35.43 and Helixmith MAE90=-43.59","R7L96_C24_ABION_2024_STAGE2_FALSE_POSITIVE_CLINICAL_DATA_EVENT_WATCH|R7L96_C24_HELIXMITH_2024_STAGE4B_GENE_THERAPY_TRIAL_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R7L96_C24_VORONOI_2024_TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE_POSITIVE", "symbol": "310210", "company_name": "보로노이", "round": "R7", "loop": "96", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE_VS_CLINICAL_EVENT_FALSE_STAGE2_AND_GENE_THERAPY_EVENT_CAP", "case_type": "structural_success_with_later_bio_pipeline_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R7L96_C24_VORONOI_2024_STAGE2_ACTIONABLE_TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Targeted-oncology pipeline / clinical-data / partner optionality bridge produced strong 30D/90D/180D MFE after February washout. C24 can work when trial-data narrative maps into mechanism credibility, endpoint quality, partner optionality, funding runway, regulatory path and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C24_positive_requires_endpoint_quality_partner_optionality_funding_regulatory_revision_bridge_not_trial_event_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R7L96_C24_ABION_2024_CLINICAL_DATA_EVENT_FALSE_STAGE2", "symbol": "203400", "company_name": "에이비온", "round": "R7", "loop": "96", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE_VS_CLINICAL_EVENT_FALSE_STAGE2_AND_GENE_THERAPY_EVENT_CAP", "case_type": "failed_rerating_clinical_data_event_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R7L96_C24_ABION_2024_STAGE2_FALSE_POSITIVE_CLINICAL_DATA_EVENT_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Clinical-data / oncology pipeline event watch after the June spike produced very low forward MFE and then deep drawdown. C24 Stage2 should not be awarded without endpoint quality, cohort durability, partner/funding path, regulatory visibility, commercial bridge and revision evidence.", "current_profile_verdict": "current_profile_false_positive_if_clinical_data_event_watch_counts_without_endpoint_partner_funding_regulatory_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; old 2015 CA and 2025 CA candidates do not overlap the 180D review window."}
{"row_type": "case", "case_id": "R7L96_C24_HELIXMITH_2024_GENE_THERAPY_EVENT_CAP_4B", "symbol": "084990", "company_name": "헬릭스미스", "round": "R7", "loop": "96", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE_VS_CLINICAL_EVENT_FALSE_STAGE2_AND_GENE_THERAPY_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R7L96_C24_HELIXMITH_2024_STAGE4B_GENE_THERAPY_TRIAL_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Gene-therapy / trial-data event premium capped on the February spike and then suffered deep 30D/90D/180D MAE. C24 should route bridge-missing clinical event premiums to 4B unless endpoint, funding, partner, regulatory and commercial bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_gene_therapy_trial_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2019/2020/2021 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R7L96_C24_VORONOI_2024_STAGE2_ACTIONABLE_TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE", "case_id": "R7L96_C24_VORONOI_2024_TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE_POSITIVE", "symbol": "310210", "company_name": "보로노이", "round": "R7", "loop": "96", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE_VS_CLINICAL_EVENT_FALSE_STAGE2_AND_GENE_THERAPY_EVENT_CAP", "sector": "targeted_oncology_pipeline_data_partner_optionality", "primary_archetype": "endpoint_quality_partner_optionality_funding_regulatory_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_watch | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-06", "entry_date": "2024-02-06", "entry_price": 35050.0, "evidence_available_at_that_date": "targeted-oncology pipeline and clinical-data credibility with partner optionality, funding runway, regulatory path and revision bridge proxy after February washout; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["endpoint_quality_proxy", "mechanism_credibility_proxy", "partner_optionality_proxy", "funding_runway_proxy", "regulatory_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "very_strong_MFE180"], "stage4b_evidence_fields": ["later_pipeline_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/310/310210/2024.csv", "profile_path": "atlas/symbol_profiles/310/310210.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 38.94, "MFE_90D_pct": 47.22, "MFE_180D_pct": 239.23, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -10.13, "MAE_90D_pct": -19.12, "MAE_180D_pct": -19.12, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-21", "peak_price": 118900.0, "drawdown_after_peak_pct": -16.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_pipeline_valuation_4B_watch_needed", "four_b_evidence_type": ["pipeline_data_bridge", "partner_optionality", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_targeted_oncology_pipeline_data_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R7L96_C24_310210_2024-02-06_35050", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L96_C24_ABION_2024_STAGE2_FALSE_POSITIVE_CLINICAL_DATA_EVENT_WATCH", "case_id": "R7L96_C24_ABION_2024_CLINICAL_DATA_EVENT_FALSE_STAGE2", "symbol": "203400", "company_name": "에이비온", "round": "R7", "loop": "96", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE_VS_CLINICAL_EVENT_FALSE_STAGE2_AND_GENE_THERAPY_EVENT_CAP", "sector": "oncology_clinical_data_event_watch", "primary_archetype": "clinical_data_event_watch_without_endpoint_partner_funding_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_watch | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-10", "entry_date": "2024-06-10", "entry_price": 12390.0, "evidence_available_at_that_date": "clinical-data / oncology pipeline event premium without confirmed endpoint quality, durable cohort, partner path, funding runway or regulatory/commercial bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["clinical_data_event", "oncology_pipeline_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "deep_MAE90", "endpoint_partner_funding_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/203/203400/2024.csv", "profile_path": "atlas/symbol_profiles/203/203400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.92, "MFE_90D_pct": 4.92, "MFE_180D_pct": 4.92, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -28.41, "MAE_90D_pct": -35.43, "MAE_180D_pct": -39.06, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-10", "peak_price": 13000.0, "drawdown_after_peak_pct": -39.06, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "clinical_data_event_watch_was_false_stage2_due_missing_endpoint_partner_funding_revision_bridge", "four_b_evidence_type": ["clinical_data_event_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_clinical_data_event_watch_without_endpoint_partner_bridge", "current_profile_verdict": "current_profile_false_positive_if_clinical_data_event_watch_counts_without_endpoint_partner_funding_regulatory_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2015_CA_and_before_2025_CA_candidates", "same_entry_group_id": "R7L96_C24_203400_2024-06-10_12390", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L96_C24_HELIXMITH_2024_STAGE4B_GENE_THERAPY_TRIAL_EVENT_CAP", "case_id": "R7L96_C24_HELIXMITH_2024_GENE_THERAPY_EVENT_CAP_4B", "symbol": "084990", "company_name": "헬릭스미스", "round": "R7", "loop": "96", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE_VS_CLINICAL_EVENT_FALSE_STAGE2_AND_GENE_THERAPY_EVENT_CAP", "sector": "gene_therapy_trial_data_event_premium", "primary_archetype": "gene_therapy_trial_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_watch | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-06", "entry_date": "2024-02-06", "entry_price": 5850.0, "evidence_available_at_that_date": "gene-therapy / clinical-trial data event premium after February bio event spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["gene_therapy_event", "clinical_trial_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "endpoint_funding_partner_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/084/084990/2024.csv", "profile_path": "atlas/symbol_profiles/084/084990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 27.18, "MFE_90D_pct": 27.18, "MFE_180D_pct": 27.18, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -28.63, "MAE_90D_pct": -43.59, "MAE_180D_pct": -43.59, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-06", "peak_price": 7440.0, "drawdown_after_peak_pct": -55.65, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.79, "four_b_full_window_peak_proximity": 0.79, "four_b_timing_verdict": "acceptable_4B_timing_gene_therapy_event_cap_because_non_price_bridge_missing_and_subsequent_MAE_deep", "four_b_evidence_type": ["gene_therapy_trial_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_gene_therapy_trial_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_gene_therapy_trial_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2019_2020_2021_CA", "same_entry_group_id": "R7L96_C24_084990_2024-02-06_5850", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L96_C24_VORONOI_2024_TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE_POSITIVE", "trigger_id": "R7L96_C24_VORONOI_2024_STAGE2_ACTIONABLE_TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE", "symbol": "310210", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 15, "revision_score": 25, "relative_strength_score": 60, "customer_quality_score": 30, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 45, "margin_bridge_score": 25, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 50, "policy_or_regulatory_score": 70, "valuation_repricing_score": 50, "execution_risk_score": 40, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "targeted_oncology_pipeline_data_positive", "MFE_90D_pct": 47.22, "MAE_90D_pct": -19.12, "score_return_alignment_label": "targeted_oncology_pipeline_data_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L96_C24_ABION_2024_CLINICAL_DATA_EVENT_FALSE_STAGE2", "trigger_id": "R7L96_C24_ABION_2024_STAGE2_FALSE_POSITIVE_CLINICAL_DATA_EVENT_WATCH", "symbol": "203400", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 20, "margin_bridge_score": 10, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "clinical_data_event_false_stage2", "MFE_90D_pct": 4.92, "MAE_90D_pct": -35.43, "score_return_alignment_label": "clinical_data_event_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_clinical_data_event_watch_counts_without_endpoint_partner_funding_regulatory_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L96_C24_HELIXMITH_2024_GENE_THERAPY_EVENT_CAP_4B", "trigger_id": "R7L96_C24_HELIXMITH_2024_STAGE4B_GENE_THERAPY_TRIAL_EVENT_CAP", "symbol": "084990", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 65, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "gene_therapy_trial_event_cap_4B_guard", "MFE_90D_pct": 27.18, "MAE_90D_pct": -43.59, "score_return_alignment_label": "gene_therapy_trial_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_gene_therapy_trial_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": "96", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "TARGETED_ONCOLOGY_PIPELINE_DATA_BRIDGE_VS_CLINICAL_EVENT_FALSE_STAGE2_AND_GENE_THERAPY_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_thesis_break_routes_to_4c", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["targeted_oncology_pipeline_data_positive", "clinical_data_event_false_stage2", "gene_therapy_trial_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C24 rows need explicit endpoint quality, mechanism credibility, cohort durability, partner/funding path, regulatory visibility, commercial path or revision bridge before positive promotion.
- In C24, bridge-missing clinical-data event-premium rows with low MFE/high MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C24 bio trial-data rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R7
completed_loop = 96
next_round = R8
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
