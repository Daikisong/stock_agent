# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R7
scheduled_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE_VS_FDA_CRL_HARD_4C_AND_ONCOLYTIC_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | trial_data_event_risk_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R7_loop_98_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. C12 was the immediately preceding final artifact, so this run skips it. After local C08/C09/C01/C07/C06/C10/C14/C11/C02/C13/C19/C27/C12 supplementation, C24 is the next unsupplemented Priority 0 archetype. Top-covered C24 symbols are avoided.

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
trial_data_event_risk_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R7
scheduled_loop = 98
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C24 is a clinical-trial / data-event risk archetype. A biotech event is the lightning; the usable signal is whether trial-data quality, endpoint clarity, partner validation, regulatory path, financing runway and revision survive after the flash.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C24_BIO_TRIAL_DATA_EVENT_RISK = 27 rows / Priority 0
top covered C24 symbols avoided: 196170, 950220, 039200, 206650, 235980, 365270
recent local C08/C09/C01/C07/C06/C10/C14/C11/C02/C13/C19/C27/C12 artifacts accounted for but not duplicated
```

Selected rows avoid hard duplicates and add new C24 trigger families:

```text
310210 / Stage2-Actionable / 2024-05-16
028300 / Stage4C / 2024-05-16
215600 / Stage4B / 2024-08-19
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
| 028300 | atlas/symbol_profiles/028/028300.json | selected 2024 window clean after old 2021 CA candidates |
| 215600 | atlas/symbol_profiles/215/215600.json | selected entry after 2024-07-09 CA candidate; post-CA 180D window |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R7L98_C24_VORONOI_2024_ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE_POSITIVE | 310210 | 2024-05-16 | yes | 180 | yes | yes | true |
| R7L98_C24_HLB_2024_FDA_CRL_HARD_4C_TRIAL_EVENT_PROTECTION | 028300 | 2024-05-16 | yes | 180 | yes | yes | true |
| R7L98_C24_SILLAJEN_2024_ONCOLYTIC_VIRUS_TRIAL_EVENT_CAP_4B | 215600 | 2024-08-19 | yes | 180 | yes | post-CA clean | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C24_BIO_TRIAL_DATA_EVENT_RISK | ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE | Positive Stage2 requires trial-data quality, endpoint clarity, partner validation, financing runway and revision bridge. |
| C24_BIO_TRIAL_DATA_EVENT_RISK | FDA_CRL_HARD_4C | Late-stage clinical/regulatory break must route to 4C protection. |
| C24_BIO_TRIAL_DATA_EVENT_RISK | ONCOLYTIC_VIRUS_EVENT_CAP_4B | Oncology trial event premium should route to 4B when data/runway/partner bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R7L98_C24_VORONOI_2024_ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE_POSITIVE | 310210 | 보로노이 | positive | Trial-data/partnering bridge produced very strong MFE with shallow early MAE. |
| R7L98_C24_HLB_2024_FDA_CRL_HARD_4C_TRIAL_EVENT_PROTECTION | 028300 | HLB | counterexample / 4C | Clinical/regulatory event risk produced a cliff-like hard 4C break. |
| R7L98_C24_SILLAJEN_2024_ONCOLYTIC_VIRUS_TRIAL_EVENT_CAP_4B | 215600 | 신라젠 | counterexample / 4B | Oncolytic-virus event premium had low MFE and later drawdown after post-CA reset. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| Voronoi oncology trial-data / partnering bridge | historical public/report proxy | true | true | shadow-only positive |
| HLB FDA/clinical-regulatory hard 4C break | historical public/news proxy | true | true | 4C protection |
| SillaJen oncolytic-virus trial event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 310210 | atlas/ohlcv_tradable_by_symbol_year/310/310210/2024.csv | atlas/symbol_profiles/310/310210.json |
| 028300 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json |
| 215600 | atlas/ohlcv_tradable_by_symbol_year/215/215600/2024.csv | atlas/symbol_profiles/215/215600.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R7L98_C24_VORONOI_2024_STAGE2_ACTIONABLE_ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE | 310210 | Stage2-Actionable | 2024-05-16 | 33250 | positive | trial-data / partnering bridge worked |
| R7L98_C24_HLB_2024_STAGE4C_FDA_CRL_TRIAL_REGULATORY_EVENT_PROTECTION | 028300 | Stage4C | 2024-05-16 | 95800 | counterexample/4C | hard 4C regulatory-event break |
| R7L98_C24_SILLAJEN_2024_STAGE4B_ONCOLYTIC_VIRUS_TRIAL_EVENT_CAP | 215600 | Stage4B | 2024-08-19 | 3275 | counterexample/4B | oncolytic-virus event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L98_C24_VORONOI_2024_STAGE2_ACTIONABLE_ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE | 33250 | 55.19 | -1.95 | 194.74 | -1.95 | 257.59 | -1.95 | 2024-10-21 | 118900 | n/a |
| R7L98_C24_HLB_2024_STAGE4C_FDA_CRL_TRIAL_REGULATORY_EVENT_PROTECTION | 95800 | 11.59 | -52.87 | 11.59 | -52.87 | 11.59 | -52.87 | 2024-05-16 | 106900 | -57.76 |
| R7L98_C24_SILLAJEN_2024_STAGE4B_ONCOLYTIC_VIRUS_TRIAL_EVENT_CAP | 3275 | 4.89 | -20.00 | 4.89 | -20.00 | 4.89 | -20.00 | 2024-08-19 | 3435 | -23.73 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C24 Stage2 needs trial data quality / endpoint clarity / partner validation / financing runway / regulatory path / revision bridge |
| trial_data_event_risk_guardrail | strengthen: biotech event label alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing trial-event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C24 rows cannot promote without durable data/runway bridge |
| hard_4c_thesis_break_routes_to_4c | strengthen: clinical/regulatory breaks must route to 4C protection |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B / 4C Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether a biotech event becomes durable data/partner/runway evidence or collapses into 4B/4C protection.

| symbol | stage quality | explanation |
|---|---|---|
| 310210 | good_stage2_with_later_watch | Trial-data/partnering bridge produced very strong MFE with shallow MAE, but later valuation watch remains necessary. |
| 028300 | good_4C_protection | Regulatory-event break required hard 4C treatment, not positive-stage promotion. |
| 215600 | good_4B | Trial-event premium lacked durable endpoint/runway bridge and later bled lower. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 028300 FDA/CRL hard 4C | 0.90 | 0.90 | hard 4C protection before regulatory event break was required |
| 215600 oncolytic-virus event cap | 0.95 | 0.95 | good 4B timing after post-CA oncology trial-event premium |
| 310210 oncology data bridge | n/a | n/a | positive Stage2, but later biotech valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 1
four_c_protection_label = hard_4C_protection_success for 028300
```

C24 should preserve hard 4C routing. A late-stage clinical/regulatory break is not a failed “long setup” only; it is proof that the protection valve is needed.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L7 bio trial-data event-risk cases, Stage2 requires verified trial-data quality, endpoint clarity, partner validation, financing runway, regulatory path and revision bridge. Biotech event, oncology pipeline, FDA catalyst, trial rumor, platform biology or relative-strength label alone remains watch/4B/4C.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
rule = C24 should split true trial-data/partner/runway positives from clinical-regulatory hard 4C breaks and event-cap 4B rows. 4B/4C rows are risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false-positive/protection rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 70.41 | -24.94 | 0.67 | mixed; C24 bridge/protection split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 70.41 | -24.94 | 0.67 | weaker C24 risk split |
| P1 sector_specific_candidate_profile | L7 data/partner/runway bridge required | 2 | 99.82 | -10.98 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C24 bridge vs 4B/4C split | 3 | 70.41 | -24.94 | 1.00 | best explanatory fit |
| P3 relaxed-event profile | bio event label can promote positive stage | 3 | 70.41 | -24.94 | 0.00 | rejected |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 310210 oncology data bridge | 66 | Stage2-Watch | 79 | Stage2-Actionable | 194.74 | -1.95 | bio_trial_data_partnering_positive |
| 028300 FDA/CRL protection | 66 | Stage2-Actionable-like event watch | 46 | Stage4C-protection | 11.59 | -52.87 | hard_4C_regulatory_event_protection |
| 215600 oncolytic event cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 4.89 | -20.00 | oncolytic_trial_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE_VS_FDA_CRL_HARD_4C_AND_ONCOLYTIC_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 1, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C24 is the next unsupplemented Priority 0 archetype after local C08/C09/C01/C07/C06/C10/C14/C11/C02/C13/C19/C27/C12 supplementation. This run adds Voronoi, HLB, and SillaJen while avoiding top-covered C24 symbols 196170, 950220, 039200, 206650, 235980 and 365270."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, trial_data_event_risk_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: bio_trial_data_partnering_positive, hard_4C_regulatory_event_protection, oncolytic_trial_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, trial_data_event_risk_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
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
- C24 bio trial-data event-risk bridge vs 4B/4C split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,configured,C24_requires_trial_data_quality_partner_validation_runway_revision_bridge,0,"C24 Stage2 should require trial-data quality, endpoint clarity, partner validation, financing runway, regulatory path, and revision bridge, not bio event label alone","Voronoi positive worked; HLB and SillaJen event/watch rows failed positive-stage promotion or required 4C protection","R7L98_C24_VORONOI_2024_STAGE2_ACTIONABLE_ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE|R7L98_C24_HLB_2024_STAGE4C_FDA_CRL_TRIAL_REGULATORY_EVENT_PROTECTION|R7L98_C24_SILLAJEN_2024_STAGE4B_ONCOLYTIC_VIRUS_TRIAL_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,hard_4c_thesis_break_routes_to_4c,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,configured,route_confirmed_trial_regulatory_breaks_to_4C_protection,0,"Late-stage clinical/regulatory breaks must route to hard 4C rather than remain as Stage2/Stage3 event-watch evidence","HLB showed cliff-like 4C behavior after regulatory break","R7L98_C24_HLB_2024_STAGE4C_FDA_CRL_TRIAL_REGULATORY_EVENT_PROTECTION",1,1,1,medium,guardrail_shadow_only,"4C protection axis; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,configured,block_positive_stage_when_bio_trial_event_has_high_or_persistent_MAE_without_data_runway_bridge,0,"High or persistent MAE after bridge-missing C24 entries should block Stage2/Stage3 promotion unless trial data, runway and regulatory evidence survive","HLB MAE90=-52.87 and SillaJen MAE90=-20.00","R7L98_C24_HLB_2024_STAGE4C_FDA_CRL_TRIAL_REGULATORY_EVENT_PROTECTION|R7L98_C24_SILLAJEN_2024_STAGE4B_ONCOLYTIC_VIRUS_TRIAL_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R7L98_C24_VORONOI_2024_ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE_POSITIVE", "symbol": "310210", "company_name": "보로노이", "round": "R7", "loop": "98", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE_VS_FDA_CRL_HARD_4C_AND_ONCOLYTIC_EVENT_CAP", "case_type": "structural_success_with_later_trial_data_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R7L98_C24_VORONOI_2024_STAGE2_ACTIONABLE_ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Targeted-oncology / trial-data / partnering bridge produced very strong 30D/90D/180D MFE with shallow early MAE. C24 works when biology/data risk is tied to trial readout quality, partner validation, differentiated target, financing runway, valuation discipline and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C24_positive_requires_trial_data_quality_partner_validation_runway_margin_revision_bridge_not_bio_event_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R7L98_C24_HLB_2024_FDA_CRL_HARD_4C_TRIAL_EVENT_PROTECTION", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "98", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE_VS_FDA_CRL_HARD_4C_AND_ONCOLYTIC_EVENT_CAP", "case_type": "hard_4C_protection_success_trial_regulatory_event_break", "positive_or_counterexample": "counterexample", "best_trigger": "R7L98_C24_HLB_2024_STAGE4C_FDA_CRL_TRIAL_REGULATORY_EVENT_PROTECTION", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "FDA/clinical-regulatory event risk had a cliff-like 4C break. A pre-event rebound should not be promoted unless approval path, manufacturing/inspection, label risk, financing runway and commercialization bridge survive. C24 hard 4C protection is the useful signal.", "current_profile_verdict": "current_profile_kept_but_hard_4C_should_block_positive_stage_when_trial_regulatory_event_breaks", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2021 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R7L98_C24_SILLAJEN_2024_ONCOLYTIC_VIRUS_TRIAL_EVENT_CAP_4B", "symbol": "215600", "company_name": "신라젠", "round": "R7", "loop": "98", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE_VS_FDA_CRL_HARD_4C_AND_ONCOLYTIC_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R7L98_C24_SILLAJEN_2024_STAGE4B_ONCOLYTIC_VIRUS_TRIAL_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Oncolytic-virus / trial-event premium after the post-CA reset had weak MFE and then bled down. C24 should route bridge-missing biotech event premiums to 4B unless trial-data quality, endpoint visibility, funding runway, partner validation and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_oncology_trial_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Entry selected after 2024-07-09 corporate-action candidate boundary. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R7L98_C24_VORONOI_2024_STAGE2_ACTIONABLE_ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE", "case_id": "R7L98_C24_VORONOI_2024_ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE_POSITIVE", "symbol": "310210", "company_name": "보로노이", "round": "R7", "loop": "98", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE_VS_FDA_CRL_HARD_4C_AND_ONCOLYTIC_EVENT_CAP", "sector": "oncology_target_trial_data_partnering_runway", "primary_archetype": "trial_data_quality_partner_validation_financing_runway_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | trial_data_event_risk_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 33250.0, "evidence_available_at_that_date": "targeted-oncology / trial-data quality / partner validation and financing-runway bridge proxy after May recovery base; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["trial_data_quality_proxy", "target_differentiation_proxy", "partner_validation_proxy", "financing_runway_proxy", "revision_bridge_proxy"], "stage3_evidence_fields": ["very_strong_MFE30", "very_strong_MFE90", "shallow_initial_MAE"], "stage4b_evidence_fields": ["later_trial_data_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/310/310210/2024.csv", "profile_path": "atlas/symbol_profiles/310/310210.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 55.19, "MFE_90D_pct": 194.74, "MFE_180D_pct": 257.59, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.95, "MAE_90D_pct": -1.95, "MAE_180D_pct": -1.95, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-21", "peak_price": 118900.0, "drawdown_after_peak_pct": "not_calculated", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_bio_trial_data_valuation_4B_watch_needed", "four_b_evidence_type": ["trial_data_quality_bridge", "partner_validation", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_oncology_trial_data_partnering_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R7L98_C24_310210_2024-05-16_33250", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L98_C24_HLB_2024_STAGE4C_FDA_CRL_TRIAL_REGULATORY_EVENT_PROTECTION", "case_id": "R7L98_C24_HLB_2024_FDA_CRL_HARD_4C_TRIAL_EVENT_PROTECTION", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "98", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE_VS_FDA_CRL_HARD_4C_AND_ONCOLYTIC_EVENT_CAP", "sector": "oncology_drug_regulatory_trial_event_CRL", "primary_archetype": "FDA_CRL_trial_regulatory_event_break_protection", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | trial_data_event_risk_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4C", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 95800.0, "evidence_available_at_that_date": "oncology drug FDA/clinical-regulatory event risk before complete-response/regulatory break; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["approval_event_watch", "late_stage_trial_event", "relative_strength_before_event"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "commercialization_bridge_recheck"], "stage4c_evidence_fields": ["regulatory_path_break", "event_gap_down", "positive_stage_blocked"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.59, "MFE_90D_pct": 11.59, "MFE_180D_pct": 11.59, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -52.87, "MAE_90D_pct": -52.87, "MAE_180D_pct": -52.87, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-16", "peak_price": 106900.0, "drawdown_after_peak_pct": -57.76, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "hard_4C_protection_before_regulatory_event_break_was_required", "four_b_evidence_type": ["FDA_CRL_risk", "trial_regulatory_event_break", "price_gap_down"], "four_c_protection_label": "hard_4C_protection_success", "trigger_outcome_label": "protective_success_hard_4C_bio_regulatory_event_break", "current_profile_verdict": "current_profile_kept_but_hard_4C_should_block_positive_stage", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2021_CA", "same_entry_group_id": "R7L98_C24_028300_2024-05-16_95800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_hard_4C", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L98_C24_SILLAJEN_2024_STAGE4B_ONCOLYTIC_VIRUS_TRIAL_EVENT_CAP", "case_id": "R7L98_C24_SILLAJEN_2024_ONCOLYTIC_VIRUS_TRIAL_EVENT_CAP_4B", "symbol": "215600", "company_name": "신라젠", "round": "R7", "loop": "98", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE_VS_FDA_CRL_HARD_4C_AND_ONCOLYTIC_EVENT_CAP", "sector": "oncolytic_virus_trial_data_event_premium", "primary_archetype": "oncolytic_virus_trial_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | trial_data_event_risk_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-08-19", "entry_date": "2024-08-19", "entry_price": 3275.0, "evidence_available_at_that_date": "oncolytic-virus / oncology trial-event premium after post-CA reset without confirmed endpoint quality, partner validation, runway or commercialization bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["oncolytic_virus_event", "trial_data_watch", "post_CA_relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "low_MFE30", "persistent_MAE90", "trial_data_endpoint_runway_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/215/215600/2024.csv", "profile_path": "atlas/symbol_profiles/215/215600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.89, "MFE_90D_pct": 4.89, "MFE_180D_pct": 4.89, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -20.0, "MAE_90D_pct": -20.0, "MAE_180D_pct": -20.0, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-19", "peak_price": 3435.0, "drawdown_after_peak_pct": -23.73, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "good_full_window_4B_timing_oncolytic_virus_event_cap_due_missing_trial_data_endpoint_runway_bridge", "four_b_evidence_type": ["oncolytic_virus_event_premium", "post_CA_reset", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_oncology_trial_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_oncology_trial_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "post_2024-07-09_CA_boundary_clean_180D_window", "same_entry_group_id": "R7L98_C24_215600_2024-08-19_3275", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R7L98_C24_VORONOI_2024_ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE_POSITIVE", "trigger_id": "R7L98_C24_VORONOI_2024_STAGE2_ACTIONABLE_ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE", "symbol": "310210", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 20, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 45, "policy_or_regulatory_score": 15, "valuation_repricing_score": 60, "execution_risk_score": 70, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 55, "margin_bridge_score": 35, "revision_score": 60, "relative_strength_score": 85, "customer_quality_score": 60, "policy_or_regulatory_score": 20, "valuation_repricing_score": 45, "execution_risk_score": 45, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "oncology_target_trial_data_partnering_positive", "MFE_90D_pct": 194.74, "MAE_90D_pct": -1.95, "score_return_alignment_label": "bio_trial_data_partnering_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R7L98_C24_HLB_2024_FDA_CRL_HARD_4C_TRIAL_EVENT_PROTECTION", "trigger_id": "R7L98_C24_HLB_2024_STAGE4C_FDA_CRL_TRIAL_REGULATORY_EVENT_PROTECTION", "symbol": "028300", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 55, "valuation_repricing_score": 65, "execution_risk_score": 75, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable-like event watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 100, "legal_or_contract_risk_score": 85, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_after": 46, "stage_label_after": "Stage4C-protection", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "FDA_CRL_trial_regulatory_event_hard_4C", "MFE_90D_pct": 11.59, "MAE_90D_pct": -52.87, "score_return_alignment_label": "hard_4C_regulatory_event_protection", "current_profile_verdict": "current_profile_kept_but_hard_4C_should_block_positive_stage"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R7L98_C24_SILLAJEN_2024_ONCOLYTIC_VIRUS_TRIAL_EVENT_CAP_4B", "trigger_id": "R7L98_C24_SILLAJEN_2024_STAGE4B_ONCOLYTIC_VIRUS_TRIAL_EVENT_CAP", "symbol": "215600", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 65, "customer_quality_score": 25, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 75, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 70, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "oncolytic_virus_trial_event_cap_4B_guard", "MFE_90D_pct": 4.89, "MAE_90D_pct": -20.0, "score_return_alignment_label": "oncolytic_trial_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_oncology_trial_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": "98", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ONCOLOGY_TARGET_TRIAL_DATA_PARTNERING_BRIDGE_VS_FDA_CRL_HARD_4C_AND_ONCOLYTIC_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 1, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "trial_data_event_risk_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["bio_trial_data_partnering_positive", "hard_4C_regulatory_event_protection", "oncolytic_trial_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C24 hard 4C rows are protection calibration only, not long-positive evidence.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C24 rows need explicit trial-data quality, endpoint clarity, partner validation, financing runway, regulatory path and revision bridge before positive promotion.
- In C24, bridge-missing biotech event rows with low MFE or high/persistent MAE should route to 4B/4C, not Stage3.
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
9. Report new independent cases, counterexamples, 4B/4C rows, and residual error types.
10. Add tests that bridge-missing C24 bio trial-data event-risk rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R7
completed_loop = 98
completed_canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
coverage_scheduler_status = coverage_index_first
next_selection_rule = re-read V12_Research_No_Repeat_Index.md Priority 0 and local supplements
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
