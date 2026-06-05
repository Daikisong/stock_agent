# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R7
scheduled_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = KINASE_PIPELINE_TRIAL_DATA_DURABILITY_BRIDGE_VS_IMMUNO_ONCOLOGY_FALSE_STAGE2_AND_CART_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R7_loop_93_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
```

This file is the corrected final output for this execution. The scheduler state after R6 loop 93 is R7 / loop 93. R7 is the L7 bio/healthcare/medical round, and this run fills C24 bio trial-data/event-risk behavior after R7 loop 92 used C23, loop 91 used C25, and loop 90 used C24 with different symbols.

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
scheduled_loop = 93
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
round_sector_consistency = pass
computed_next_round = R8
computed_next_loop = 93
```

C24 requires extra caution because a positive trial-data headline can look like a full thesis while actually behaving like a capped event premium. This loop separates endpoint-durable pipeline rerating from bridge-missing trial watches and CAR-T event caps.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C24_BIO_TRIAL_DATA_EVENT_RISK = 30 rows / 20 symbols / good-bad Stage2 13-9 / 4B-4C 0-2
top covered symbols include 298380(3), 323990(3), 007390(2), 087010(2), 141080(2), 226950(2)
previous R7 loop-89 C23 symbols avoided: 000250, 086900, 068760
previous R7 loop-90 C24 symbols avoided: 397030, 365270, 067630
previous R7 loop-91 C25 symbols avoided: 206640, 043150, 246710
previous R7 loop-92 C23 symbols avoided: 196170, 003850, 950160
previous R6 loop-93 C22 symbols avoided: 032830, 001450, 088350
```

Selected rows avoid hard duplicates and top repeated C24 symbols:

```text
039200 / Stage2-Actionable / 2024-02-20
950220 / Stage2-Actionable / 2024-02-26
174900 / Stage4B / 2024-03-05
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
| 039200 | atlas/symbol_profiles/039/039200.json | selected 2024 window clean after old 2009/2010/2012/2022 CA candidates |
| 950220 | atlas/symbol_profiles/950/950220.json | selected 2024 window clean before 2025-09-30 CA candidate |
| 174900 | atlas/symbol_profiles/174/174900.json | profile CA candidates are old 2020 dates; 2024 window reviewed as source-proxy only |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R7L93_C24_OSCOTEC_2024_KINASE_PIPELINE_TRIAL_DATA_DURABILITY_POSITIVE | 039200 | 2024-02-20 | yes | 180 | yes | yes | true |
| R7L93_C24_NEOIMMUNETECH_2024_IMMUNO_ONCOLOGY_TRIAL_FALSE_STAGE2 | 950220 | 2024-02-26 | yes | 180 | yes | yes | true |
| R7L93_C24_ABCLON_2024_CART_TRIAL_DATA_EVENT_CAP_4B | 174900 | 2024-03-05 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C24_BIO_TRIAL_DATA_EVENT_RISK | KINASE_PIPELINE_TRIAL_DATA_DURABILITY_BRIDGE | Positive Stage2 requires endpoint quality, follow-up durability, partner quality, regulatory path and revision bridge. |
| C24_BIO_TRIAL_DATA_EVENT_RISK | IMMUNO_ONCOLOGY_FALSE_STAGE2 | Immuno-oncology trial watch without endpoint/partner/regulatory bridge can become false Stage2. |
| C24_BIO_TRIAL_DATA_EVENT_RISK | CART_EVENT_CAP_4B | CAR-T trial-data event premium should route to 4B when endpoint follow-up and regulatory bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R7L93_C24_OSCOTEC_2024_KINASE_PIPELINE_TRIAL_DATA_DURABILITY_POSITIVE | 039200 | 오스코텍 | positive | Trial-data durability / partner-quality bridge produced strong MFE with controlled early MAE. |
| R7L93_C24_NEOIMMUNETECH_2024_IMMUNO_ONCOLOGY_TRIAL_FALSE_STAGE2 | 950220 | 네오이뮨텍 | counterexample | Trial-watch MFE was temporary and later MAE became large without endpoint/regulatory bridge. |
| R7L93_C24_ABCLON_2024_CART_TRIAL_DATA_EVENT_CAP_4B | 174900 | 앱클론 | counterexample / 4B | CAR-T trial-data event premium capped near the March spike and then drew down. |

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
| Oskotec kinase pipeline trial-data bridge | historical public/report proxy | true | true | shadow-only positive |
| NeoImmuneTech immuno-oncology trial false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| AbClon CAR-T trial-data event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 039200 | atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv | atlas/symbol_profiles/039/039200.json |
| 950220 | atlas/ohlcv_tradable_by_symbol_year/950/950220/2024.csv | atlas/symbol_profiles/950/950220.json |
| 174900 | atlas/ohlcv_tradable_by_symbol_year/174/174900/2024.csv | atlas/symbol_profiles/174/174900.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R7L93_C24_OSCOTEC_2024_STAGE2_ACTIONABLE_KINASE_PIPELINE_TRIAL_DATA_DURABILITY | 039200 | Stage2-Actionable | 2024-02-20 | 22050 | positive | endpoint/follow-up/partner bridge worked |
| R7L93_C24_NEOIMMUNETECH_2024_STAGE2_FALSE_POSITIVE_IMMUNO_ONCOLOGY_TRIAL_WATCH | 950220 | Stage2-Actionable | 2024-02-26 | 1665 | counterexample | trial-watch false Stage2 |
| R7L93_C24_ABCLON_2024_STAGE4B_CART_TRIAL_DATA_EVENT_CAP | 174900 | Stage4B | 2024-03-05 | 21100 | counterexample/4B | CAR-T trial-data event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L93_C24_OSCOTEC_2024_STAGE2_ACTIONABLE_KINASE_PIPELINE_TRIAL_DATA_DURABILITY | 22050 | 36.05 | -9.66 | 102.27 | -9.66 | 102.27 | -9.66 | 2024-07-10 | 44600 | -23.09 |
| R7L93_C24_NEOIMMUNETECH_2024_STAGE2_FALSE_POSITIVE_IMMUNO_ONCOLOGY_TRIAL_WATCH | 1665 | 18.74 | -14.41 | 18.74 | -31.05 | 18.74 | -55.00 | 2024-03-25 | 1977 | -54.22 |
| R7L93_C24_ABCLON_2024_STAGE4B_CART_TRIAL_DATA_EVENT_CAP | 21100 | 4.98 | -22.75 | 4.98 | -33.18 | 4.98 | -43.79 | 2024-03-05 | 22150 | -44.33 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C24 Stage2 needs endpoint quality / follow-up durability / partner or financing / regulatory path / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing trial-data event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE clinical-trial rows cannot promote without durable endpoint/regulatory bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is trial-data bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 039200 | good_stage2_with_later_watch | Endpoint/partner/regulatory bridge produced strong MFE with controlled initial MAE. |
| 950220 | bad_stage2 | Trial-watch MFE was temporary and later MAE became large without endpoint/regulatory bridge. |
| 174900 | good_4B | CAR-T event premium capped near the March spike and then de-rated. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 950220 immuno-oncology false Stage2 | 0.84 | 0.84 | false Stage2 due missing endpoint/partner/regulatory bridge despite temporary MFE |
| 174900 CAR-T event cap | 0.95 | 0.95 | good full-window 4B timing after event spike and high-MAE confirmation |
| 039200 kinase pipeline bridge | n/a | n/a | positive Stage2, but later trial-data valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 950220 / 174900
```

No hard 4C candidate is proposed. R7 loop 93 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L7 bio trial-data/event-risk cases, Stage2 requires verified endpoint quality, statistical interpretability, follow-up durability, partner or financing bridge, regulatory path, and revision bridge. Trial update, CAR-T, immuno-oncology, pipeline, data event, or clinical headline alone remains watch/4B/4C-review.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
rule = C24 should split true endpoint/follow-up/partner/regulatory positives from trial-watch false Stage2 and CAR-T event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 42.00 | -24.63 | 0.67 | mixed; C24 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 42.00 | -24.63 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L7 endpoint/regulatory bridge required | 2 | 60.51 | -20.36 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C24 bridge vs event-cap split | 2 | 60.51 | -20.36 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing trial-data themes as positive | 1 | 102.27 | -9.66 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 039200 kinase trial-data bridge | 66 | Stage2-Watch | 77 | Stage2-Actionable | 102.27 | -9.66 | kinase_pipeline_trial_data_positive |
| 950220 immuno-oncology false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 18.74 | -31.05 | immuno_oncology_trial_false_stage2 |
| 174900 CAR-T event cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 4.98 | -33.18 | CAR_T_trial_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "KINASE_PIPELINE_TRIAL_DATA_DURABILITY_BRIDGE_VS_IMMUNO_ONCOLOGY_FALSE_STAGE2_AND_CART_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C24 kinase pipeline trial-data positive, immuno-oncology trial-watch false Stage2, and CAR-T trial-data event-cap 4B split while avoiding top repeated C24 symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: kinase_pipeline_trial_data_positive, immuno_oncology_trial_false_stage2, CAR_T_trial_data_event_cap_4B
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
shadow_weight,stage2_required_bridge,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,configured,C24_requires_endpoint_quality_followup_partner_regulatory_revision_bridge,0,"C24 Stage2 should require endpoint quality, follow-up durability, partner/financing bridge, regulatory path, or revision bridge, not trial-data headline alone","Oskotec positive worked; NeoImmuneTech and AbClon event/watch rows failed positive-stage promotion","R7L93_C24_OSCOTEC_2024_STAGE2_ACTIONABLE_KINASE_PIPELINE_TRIAL_DATA_DURABILITY|R7L93_C24_NEOIMMUNETECH_2024_STAGE2_FALSE_POSITIVE_IMMUNO_ONCOLOGY_TRIAL_WATCH|R7L93_C24_ABCLON_2024_STAGE4B_CART_TRIAL_DATA_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,configured,cap_bridge_missing_trial_data_event_premiums_as_4B_watch,0,"Trial-data event premiums can peak before endpoint durability and partner/regulatory bridge is proven","NeoImmuneTech had temporary MFE then large later MAE; AbClon showed 4B event-cap behavior after March trial-data spike","R7L93_C24_NEOIMMUNETECH_2024_STAGE2_FALSE_POSITIVE_IMMUNO_ONCOLOGY_TRIAL_WATCH|R7L93_C24_ABCLON_2024_STAGE4B_CART_TRIAL_DATA_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,configured,block_positive_stage_when_trial_data_theme_has_high_MAE_without_endpoint_bridge,0,"High MAE after bridge-missing trial-data entries should block Stage2/Stage3 promotion unless endpoint, follow-up, partner and regulatory evidence survives","NeoImmuneTech MAE180=-55.00 and AbClon MAE90=-33.18","R7L93_C24_NEOIMMUNETECH_2024_STAGE2_FALSE_POSITIVE_IMMUNO_ONCOLOGY_TRIAL_WATCH|R7L93_C24_ABCLON_2024_STAGE4B_CART_TRIAL_DATA_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R7L93_C24_OSCOTEC_2024_KINASE_PIPELINE_TRIAL_DATA_DURABILITY_POSITIVE", "symbol": "039200", "company_name": "오스코텍", "round": "R7", "loop": "93", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "KINASE_PIPELINE_TRIAL_DATA_DURABILITY_BRIDGE_VS_IMMUNO_ONCOLOGY_FALSE_STAGE2_AND_CART_EVENT_CAP", "case_type": "structural_success_with_later_trial_data_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R7L93_C24_OSCOTEC_2024_STAGE2_ACTIONABLE_KINASE_PIPELINE_TRIAL_DATA_DURABILITY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Kinase pipeline / clinical-data durability and partner-quality bridge produced strong 30D/90D/180D MFE with controlled initial MAE. C24 works when trial data has interpretable endpoint quality, partner/commercial optionality, follow-up durability, regulatory path and revision bridge, not trial headline alone.", "current_profile_verdict": "current_profile_kept_but_C24_positive_requires_endpoint_quality_followup_partner_regulatory_revision_bridge_not_trial_headline_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2009/2010/2012/2022 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R7L93_C24_NEOIMMUNETECH_2024_IMMUNO_ONCOLOGY_TRIAL_FALSE_STAGE2", "symbol": "950220", "company_name": "네오이뮨텍", "round": "R7", "loop": "93", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "KINASE_PIPELINE_TRIAL_DATA_DURABILITY_BRIDGE_VS_IMMUNO_ONCOLOGY_FALSE_STAGE2_AND_CART_EVENT_CAP", "case_type": "failed_rerating_trial_watch_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R7L93_C24_NEOIMMUNETECH_2024_STAGE2_FALSE_POSITIVE_IMMUNO_ONCOLOGY_TRIAL_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Immuno-oncology / clinical-trial watch had temporary MFE but later suffered material MAE. C24 Stage2 should not be awarded without endpoint quality, statistical/data durability, partner or financing bridge, regulatory milestone and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_trial_watch_counts_without_endpoint_quality_partner_regulatory_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean before later 2025-09-30 corporate-action candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R7L93_C24_ABCLON_2024_CART_TRIAL_DATA_EVENT_CAP_4B", "symbol": "174900", "company_name": "앱클론", "round": "R7", "loop": "93", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "KINASE_PIPELINE_TRIAL_DATA_DURABILITY_BRIDGE_VS_IMMUNO_ONCOLOGY_FALSE_STAGE2_AND_CART_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R7L93_C24_ABCLON_2024_STAGE4B_CART_TRIAL_DATA_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "CAR-T / trial-data event premium capped near the March spike and then drew down. C24 should route bridge-missing trial-data event premiums to 4B unless endpoint quality, follow-up durability, regulatory path, financing/partner bridge and revision evidence remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_CART_trial_data_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Profile corporate-action candidates are old 2020 dates; this 2024 window is treated as stock-web usable but remains source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R7L93_C24_OSCOTEC_2024_STAGE2_ACTIONABLE_KINASE_PIPELINE_TRIAL_DATA_DURABILITY", "case_id": "R7L93_C24_OSCOTEC_2024_KINASE_PIPELINE_TRIAL_DATA_DURABILITY_POSITIVE", "symbol": "039200", "company_name": "오스코텍", "round": "R7", "loop": "93", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "KINASE_PIPELINE_TRIAL_DATA_DURABILITY_BRIDGE_VS_IMMUNO_ONCOLOGY_FALSE_STAGE2_AND_CART_EVENT_CAP", "sector": "kinase_pipeline_trial_data_durability_partner_quality", "primary_archetype": "endpoint_quality_followup_partner_regulatory_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-20", "entry_date": "2024-02-20", "entry_price": 22050.0, "evidence_available_at_that_date": "kinase pipeline data durability, endpoint interpretability, partner/commercial optionality, regulatory path and revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["endpoint_quality_proxy", "followup_durability_proxy", "partner_quality_proxy", "regulatory_path_proxy", "revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "very_high_MFE90", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_trial_data_valuation_watch", "post_peak_drawdown_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv", "profile_path": "atlas/symbol_profiles/039/039200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 36.05, "MFE_90D_pct": 102.27, "MFE_180D_pct": 102.27, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -9.66, "MAE_90D_pct": -9.66, "MAE_180D_pct": -9.66, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-10", "peak_price": 44600.0, "drawdown_after_peak_pct": -23.09, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_trial_data_valuation_4B_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "trial_data_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_kinase_pipeline_trial_data_durability_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2009_2010_2012_2022_CA", "same_entry_group_id": "R7L93_C24_039200_2024-02-20_22050", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L93_C24_NEOIMMUNETECH_2024_STAGE2_FALSE_POSITIVE_IMMUNO_ONCOLOGY_TRIAL_WATCH", "case_id": "R7L93_C24_NEOIMMUNETECH_2024_IMMUNO_ONCOLOGY_TRIAL_FALSE_STAGE2", "symbol": "950220", "company_name": "네오이뮨텍", "round": "R7", "loop": "93", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "KINASE_PIPELINE_TRIAL_DATA_DURABILITY_BRIDGE_VS_IMMUNO_ONCOLOGY_FALSE_STAGE2_AND_CART_EVENT_CAP", "sector": "immuno_oncology_clinical_trial_watch", "primary_archetype": "trial_watch_without_endpoint_partner_regulatory_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 1665.0, "evidence_available_at_that_date": "immuno-oncology trial update watch and clinical-data expectation proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["trial_update_watch", "clinical_data_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_sustainable_MFE", "endpoint_quality_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/950/950220/2024.csv", "profile_path": "atlas/symbol_profiles/950/950220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 18.74, "MFE_90D_pct": 18.74, "MFE_180D_pct": 18.74, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -14.41, "MAE_90D_pct": -31.05, "MAE_180D_pct": -55.0, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-25", "peak_price": 1977.0, "drawdown_after_peak_pct": -54.22, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.84, "four_b_full_window_peak_proximity": 0.84, "four_b_timing_verdict": "trial_watch_was_false_stage2_due_missing_endpoint_partner_regulatory_revision_bridge", "four_b_evidence_type": ["clinical_trial_watch_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_immuno_oncology_trial_watch_without_endpoint_bridge", "current_profile_verdict": "current_profile_false_positive_if_trial_watch_counts_without_endpoint_quality_partner_regulatory_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_before_2025_CA_candidate", "same_entry_group_id": "R7L93_C24_950220_2024-02-26_1665", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L93_C24_ABCLON_2024_STAGE4B_CART_TRIAL_DATA_EVENT_CAP", "case_id": "R7L93_C24_ABCLON_2024_CART_TRIAL_DATA_EVENT_CAP_4B", "symbol": "174900", "company_name": "앱클론", "round": "R7", "loop": "93", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "KINASE_PIPELINE_TRIAL_DATA_DURABILITY_BRIDGE_VS_IMMUNO_ONCOLOGY_FALSE_STAGE2_AND_CART_EVENT_CAP", "sector": "CAR_T_trial_data_event_premium", "primary_archetype": "CAR_T_trial_data_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-05", "entry_date": "2024-03-05", "entry_price": 21100.0, "evidence_available_at_that_date": "CAR-T / clinical-trial data event premium after March spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["CAR_T_trial_data_event", "clinical_endpoint_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "high_MAE90", "endpoint_followup_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/174/174900/2024.csv", "profile_path": "atlas/symbol_profiles/174/174900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.98, "MFE_90D_pct": 4.98, "MFE_180D_pct": 4.98, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -22.75, "MAE_90D_pct": -33.18, "MAE_180D_pct": -43.79, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-05", "peak_price": 22150.0, "drawdown_after_peak_pct": -44.33, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "good_full_window_4B_timing_CART_trial_data_event_cap", "four_b_evidence_type": ["trial_data_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_CART_trial_data_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_CART_trial_data_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "stock_web_profile_has_old_2020_CA_only_2024_window_reviewed_as_source_proxy", "same_entry_group_id": "R7L93_C24_174900_2024-03-05_21100", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L93_C24_OSCOTEC_2024_KINASE_PIPELINE_TRIAL_DATA_DURABILITY_POSITIVE", "trigger_id": "R7L93_C24_OSCOTEC_2024_STAGE2_ACTIONABLE_KINASE_PIPELINE_TRIAL_DATA_DURABILITY", "symbol": "039200", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 25, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 70, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 50, "margin_bridge_score": 45, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 60, "policy_or_regulatory_score": 55, "valuation_repricing_score": 55, "execution_risk_score": 40, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "revision_score", "customer_quality_score", "policy_or_regulatory_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "kinase_pipeline_trial_data_positive", "MFE_90D_pct": 102.27, "MAE_90D_pct": -9.66, "score_return_alignment_label": "kinase_pipeline_trial_data_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L93_C24_NEOIMMUNETECH_2024_IMMUNO_ONCOLOGY_TRIAL_FALSE_STAGE2", "trigger_id": "R7L93_C24_NEOIMMUNETECH_2024_STAGE2_FALSE_POSITIVE_IMMUNO_ONCOLOGY_TRIAL_WATCH", "symbol": "950220", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 25, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 70, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "revision_score", "customer_quality_score", "policy_or_regulatory_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "immuno_oncology_trial_false_stage2", "MFE_90D_pct": 18.74, "MAE_90D_pct": -31.05, "score_return_alignment_label": "immuno_oncology_trial_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_trial_watch_counts_without_endpoint_quality_partner_regulatory_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L93_C24_ABCLON_2024_CART_TRIAL_DATA_EVENT_CAP_4B", "trigger_id": "R7L93_C24_ABCLON_2024_STAGE4B_CART_TRIAL_DATA_EVENT_CAP", "symbol": "174900", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 25, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 70, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "revision_score", "customer_quality_score", "policy_or_regulatory_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "CAR_T_trial_event_cap_4B_guard", "MFE_90D_pct": 4.98, "MAE_90D_pct": -33.18, "score_return_alignment_label": "CAR_T_trial_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_CART_trial_data_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": "93", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "KINASE_PIPELINE_TRIAL_DATA_DURABILITY_BRIDGE_VS_IMMUNO_ONCOLOGY_FALSE_STAGE2_AND_CART_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["kinase_pipeline_trial_data_positive", "immuno_oncology_trial_false_stage2", "CAR_T_trial_data_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- Trial-data rows need endpoint/follow-up/regulatory bridge before positive promotion.
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
10. Add tests that bridge-missing C24 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R7
completed_loop = 93
next_round = R8
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
