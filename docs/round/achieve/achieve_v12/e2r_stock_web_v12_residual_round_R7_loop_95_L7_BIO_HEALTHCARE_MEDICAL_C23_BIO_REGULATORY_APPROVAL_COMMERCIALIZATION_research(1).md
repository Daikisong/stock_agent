# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R7
scheduled_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE_VS_CELL_THERAPY_COMMERCIALIZATION_FALSE_STAGE2_AND_NOX_INHIBITOR_REGULATORY_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R7_loop_95_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
```

This file is the corrected final output for this execution. The scheduler state after R6 loop 95 is R7 / loop 95. R7 is the L7 bio/healthcare/medical round, and this run fills C23 bio regulatory approval/commercialization rather than repeating the immediately preceding R7 loop 94 C25 medical-device file.

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
scheduled_loop = 95
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
round_sector_consistency = pass
computed_next_round = R8
computed_next_loop = 95
```

C23 is a regulatory-to-commercialization bridge archetype. An approval, trial, or commercialization label is only the hospital door; the revenue patient arrives only through partner/channel visibility, launch economics, reimbursement, milestone/supply-contract quality, margin and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION = 26 rows / 14 symbols / good-bad Stage2 8-5 / 4B-4C 0-2
top covered symbols include UNKNOWN_SYMBOL(6), 028300(4), 000100(2), 039200(2), 195940(2), 003850(1)
previous R7 loop-90 C24 symbols avoided: 397030, 365270, 067630
previous R7 loop-91 C25 symbols avoided: 206640, 043150, 246710
previous R7 loop-92 C23 symbols avoided: 196170, 003850, 950160
previous R7 loop-93 C24 symbols avoided: 039200, 950220, 174900
previous R7 loop-94 C25 symbols avoided: 214450, 228670, 214680
previous R6 loop-95 C22 symbols avoided: 138040, 244920, 211050
```

Selected rows avoid hard duplicates and top repeated C23 symbols:

```text
000250 / Stage2-Actionable / 2024-03-25
085660 / Stage2-Actionable / 2024-03-07
293780 / Stage4B / 2024-07-11
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
| 000250 | atlas/symbol_profiles/000/000250.json | selected 2024 window clean after old 2002 CA candidate |
| 085660 | atlas/symbol_profiles/085/085660.json | selected 2024 window clean before 2025-06-25 CA candidate |
| 293780 | atlas/symbol_profiles/293/293780.json | selected 2024 window clean after old 2021 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R7L95_C23_SCD_2024_BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE_POSITIVE | 000250 | 2024-03-25 | yes | 180 | yes | yes | true |
| R7L95_C23_CHABIO_2024_CELL_THERAPY_COMMERCIALIZATION_FALSE_STAGE2 | 085660 | 2024-03-07 | yes | 180 | yes | yes | true |
| R7L95_C23_APTABIO_2024_NOX_INHIBITOR_REGULATORY_EVENT_CAP_4B | 293780 | 2024-07-11 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE | Positive Stage2 requires partner/channel, regulatory path, launch economics, milestone/supply contract, margin and revision bridge. |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | CELL_THERAPY_COMMERCIALIZATION_FALSE_STAGE2 | Commercialization watch without partner/revenue/margin bridge can become false Stage2. |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | NOX_INHIBITOR_REGULATORY_EVENT_CAP_4B | Regulatory-development event premium should route to 4B when partner/funding/endpoint bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R7L95_C23_SCD_2024_BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE_POSITIVE | 000250 | 삼천당제약 | positive | Biosimilar commercialization/partner bridge produced very high MFE despite later valuation drawdown. |
| R7L95_C23_CHABIO_2024_CELL_THERAPY_COMMERCIALIZATION_FALSE_STAGE2 | 085660 | 차바이오텍 | counterexample | Cell-therapy commercialization watch had limited MFE and no durable partner/revenue bridge. |
| R7L95_C23_APTABIO_2024_NOX_INHIBITOR_REGULATORY_EVENT_CAP_4B | 293780 | 압타바이오 | counterexample / 4B | Regulatory-development event premium capped near the July spike and then suffered deep MAE. |

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
| Samchundang biosimilar commercialization bridge | historical public/report proxy | true | true | shadow-only positive |
| Cha Biotech cell-therapy commercialization false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| AptaBio NOX inhibitor regulatory event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 000250 | atlas/ohlcv_tradable_by_symbol_year/000/000250/2024.csv | atlas/symbol_profiles/000/000250.json |
| 085660 | atlas/ohlcv_tradable_by_symbol_year/085/085660/2024.csv | atlas/symbol_profiles/085/085660.json |
| 293780 | atlas/ohlcv_tradable_by_symbol_year/293/293780/2024.csv | atlas/symbol_profiles/293/293780.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R7L95_C23_SCD_2024_STAGE2_ACTIONABLE_BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE | 000250 | Stage2-Actionable | 2024-03-25 | 111100 | positive | biosimilar commercialization partner bridge worked |
| R7L95_C23_CHABIO_2024_STAGE2_FALSE_POSITIVE_CELL_THERAPY_COMMERCIALIZATION_WATCH | 085660 | Stage2-Actionable | 2024-03-07 | 19060 | counterexample | cell-therapy commercialization false Stage2 |
| R7L95_C23_APTABIO_2024_STAGE4B_NOX_INHIBITOR_REGULATORY_EVENT_CAP | 293780 | Stage4B | 2024-07-11 | 14600 | counterexample/4B | NOX inhibitor regulatory event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L95_C23_SCD_2024_STAGE2_ACTIONABLE_BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE | 111100 | 36.09 | -12.69 | 107.02 | -12.69 | 107.02 | -12.69 | 2024-07-10 | 230000 | -44.17 |
| R7L95_C23_CHABIO_2024_STAGE2_FALSE_POSITIVE_CELL_THERAPY_COMMERCIALIZATION_WATCH | 19060 | 10.18 | -14.06 | 10.18 | -20.46 | 12.28 | -20.46 | 2024-03-27 | 21000 | -27.81 |
| R7L95_C23_APTABIO_2024_STAGE4B_NOX_INHIBITOR_REGULATORY_EVENT_CAP | 14600 | 6.10 | -41.78 | 6.10 | -48.56 | 6.10 | -48.56 | 2024-07-11 | 15490 | -48.56 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C23 Stage2 needs partner/channel / regulatory / launch revenue / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing bio regulatory event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE regulatory event rows cannot promote without durable partner/funding/margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether approval/commercialization becomes partner, launch and margin.

| symbol | stage quality | explanation |
|---|---|---|
| 000250 | good_stage2_with_later_watch | Biosimilar commercialization/partner bridge produced very high MFE but later valuation watch remains necessary. |
| 085660 | bad_stage2 | Cell-therapy commercialization watch lacked partner/revenue/margin bridge and produced limited MFE. |
| 293780 | good_4B | Regulatory-development event premium capped near the July spike and later suffered deep MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 085660 cell-therapy false Stage2 | 0.91 | 0.91 | false Stage2 due missing regulatory/partner/revenue bridge |
| 293780 NOX inhibitor cap | 0.94 | 0.94 | good full-window 4B timing after July regulatory event premium |
| 000250 biosimilar bridge | n/a | n/a | positive Stage2, but later biosimilar valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 085660 / 293780
```

No hard 4C candidate is proposed. R7 loop 95 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L7 bio regulatory approval/commercialization cases, Stage2 requires verified regulatory path, partner/channel visibility, launch revenue, reimbursement or milestone/supply economics, margin, or revision bridge. Approval, commercialization, clinical, cell therapy, biosimilar, inhibitor or regulatory-event label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
rule = C23 should split true partner/channel/launch-economics positives from commercialization false Stage2 and regulatory event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 41.10 | -27.24 | 0.67 | mixed; C23 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 41.10 | -27.24 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L7 partner/regulatory/launch bridge required | 2 | 58.60 | -16.58 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C23 bridge vs event-cap split | 2 | 58.60 | -16.58 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing bio regulatory themes as positive | 1 | 107.02 | -12.69 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 000250 biosimilar partner bridge | 66 | Stage2-Watch | 79 | Stage2-Actionable | 107.02 | -12.69 | biosimilar_global_commercialization_positive |
| 085660 cell therapy false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 10.18 | -20.46 | cell_therapy_commercialization_false_stage2 |
| 293780 NOX inhibitor cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 6.10 | -48.56 | NOX_inhibitor_regulatory_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE_VS_CELL_THERAPY_COMMERCIALIZATION_FALSE_STAGE2_AND_NOX_INHIBITOR_REGULATORY_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C23 Samchundang biosimilar commercialization positive, Cha Biotech cell-therapy commercialization false Stage2, and AptaBio NOX-inhibitor regulatory event-cap 4B split while avoiding top repeated C23 symbols and previous R7/R6 loop symbols."}
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
residual_error_types_found: biosimilar_global_commercialization_positive, cell_therapy_commercialization_false_stage2, NOX_inhibitor_regulatory_event_cap_4B
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
- C23 bio regulatory approval/commercialization bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,configured,C23_requires_partner_channel_regulatory_launch_margin_revision_bridge,0,"C23 Stage2 should require regulatory path, partner/channel visibility, launch revenue, reimbursement, milestone or supply contract quality, margin, or revision bridge, not approval/commercialization label alone","Samchundang positive worked; Cha Biotech and AptaBio event/watch rows failed positive-stage promotion","R7L95_C23_SCD_2024_STAGE2_ACTIONABLE_BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE|R7L95_C23_CHABIO_2024_STAGE2_FALSE_POSITIVE_CELL_THERAPY_COMMERCIALIZATION_WATCH|R7L95_C23_APTABIO_2024_STAGE4B_NOX_INHIBITOR_REGULATORY_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,configured,cap_bridge_missing_regulatory_and_bio_commercialization_event_premiums_as_4B_watch,0,"Regulatory/commercialization event premiums can peak before partner, launch and margin bridge is proven","Cha Biotech had limited MFE after commercialization watch; AptaBio showed 4B event-cap behavior after July bio event spike","R7L95_C23_CHABIO_2024_STAGE2_FALSE_POSITIVE_CELL_THERAPY_COMMERCIALIZATION_WATCH|R7L95_C23_APTABIO_2024_STAGE4B_NOX_INHIBITOR_REGULATORY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,configured,block_positive_stage_when_bio_regulatory_theme_has_high_or_persistent_MAE_without_partner_margin_bridge,0,"High or persistent MAE after bridge-missing C23 entries should block Stage2/Stage3 promotion unless partner, regulatory, launch and margin evidence survives","Cha Biotech MAE180=-20.46 and AptaBio MAE90=-48.56","R7L95_C23_CHABIO_2024_STAGE2_FALSE_POSITIVE_CELL_THERAPY_COMMERCIALIZATION_WATCH|R7L95_C23_APTABIO_2024_STAGE4B_NOX_INHIBITOR_REGULATORY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R7L95_C23_SCD_2024_BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE_POSITIVE", "symbol": "000250", "company_name": "삼천당제약", "round": "R7", "loop": "95", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE_VS_CELL_THERAPY_COMMERCIALIZATION_FALSE_STAGE2_AND_NOX_INHIBITOR_REGULATORY_EVENT_CAP", "case_type": "structural_success_with_later_biosimilar_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R7L95_C23_SCD_2024_STAGE2_ACTIONABLE_BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Biosimilar/regulatory commercialization partner bridge produced strong 30D/90D/180D MFE despite a post-spike valuation drawdown. C23 works when approval/commercialization narrative maps into partner/channel visibility, regulatory path, launch economics, milestone or supply contract quality, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C23_positive_requires_partner_channel_regulatory_launch_margin_revision_bridge_not_approval_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2002 corporate-action candidate. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R7L95_C23_CHABIO_2024_CELL_THERAPY_COMMERCIALIZATION_FALSE_STAGE2", "symbol": "085660", "company_name": "차바이오텍", "round": "R7", "loop": "95", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE_VS_CELL_THERAPY_COMMERCIALIZATION_FALSE_STAGE2_AND_NOX_INHIBITOR_REGULATORY_EVENT_CAP", "case_type": "failed_rerating_cell_therapy_commercialization_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R7L95_C23_CHABIO_2024_STAGE2_FALSE_POSITIVE_CELL_THERAPY_COMMERCIALIZATION_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Cell-therapy / healthcare commercialization watch produced only limited MFE and then a slow drawdown. C23 Stage2 should not be awarded without confirmed regulatory milestone, partner/customer channel, launch revenue, reimbursement or margin/revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_cell_therapy_commercialization_watch_counts_without_regulatory_partner_revenue_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean before 2025-06-25 corporate-action candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R7L95_C23_APTABIO_2024_NOX_INHIBITOR_REGULATORY_EVENT_CAP_4B", "symbol": "293780", "company_name": "압타바이오", "round": "R7", "loop": "95", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE_VS_CELL_THERAPY_COMMERCIALIZATION_FALSE_STAGE2_AND_NOX_INHIBITOR_REGULATORY_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R7L95_C23_APTABIO_2024_STAGE4B_NOX_INHIBITOR_REGULATORY_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "NOX inhibitor / regulatory or clinical-development event premium capped around the July spike and then suffered deep 30D/90D/180D MAE. C23 should route bridge-missing regulatory event premiums to 4B unless partner, regulatory endpoint, funding runway, launch economics, milestone quality and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_NOX_inhibitor_regulatory_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2021 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R7L95_C23_SCD_2024_STAGE2_ACTIONABLE_BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE", "case_id": "R7L95_C23_SCD_2024_BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE_POSITIVE", "symbol": "000250", "company_name": "삼천당제약", "round": "R7", "loop": "95", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE_VS_CELL_THERAPY_COMMERCIALIZATION_FALSE_STAGE2_AND_NOX_INHIBITOR_REGULATORY_EVENT_CAP", "sector": "biosimilar_global_commercialization_partner_channel", "primary_archetype": "partner_channel_regulatory_launch_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-25", "entry_date": "2024-03-25", "entry_price": 111100.0, "evidence_available_at_that_date": "biosimilar global commercialization partner/channel, regulatory path, supply or milestone economics and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["partner_channel_visibility_proxy", "regulatory_path_proxy", "commercial_launch_economics_proxy", "milestone_supply_contract_quality_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "very_high_MFE90", "very_high_MFE180", "controlled_MAE90"], "stage4b_evidence_fields": ["later_biosimilar_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000250/2024.csv", "profile_path": "atlas/symbol_profiles/000/000250.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 36.09, "MFE_90D_pct": 107.02, "MFE_180D_pct": 107.02, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -12.69, "MAE_90D_pct": -12.69, "MAE_180D_pct": -12.69, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-10", "peak_price": 230000.0, "drawdown_after_peak_pct": -44.17, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_biosimilar_valuation_4B_watch_needed", "four_b_evidence_type": ["regulatory_commercialization_bridge", "partner_channel_visibility", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_biosimilar_global_commercialization_partner_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2002_CA", "same_entry_group_id": "R7L95_C23_000250_2024-03-25_111100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L95_C23_CHABIO_2024_STAGE2_FALSE_POSITIVE_CELL_THERAPY_COMMERCIALIZATION_WATCH", "case_id": "R7L95_C23_CHABIO_2024_CELL_THERAPY_COMMERCIALIZATION_FALSE_STAGE2", "symbol": "085660", "company_name": "차바이오텍", "round": "R7", "loop": "95", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE_VS_CELL_THERAPY_COMMERCIALIZATION_FALSE_STAGE2_AND_NOX_INHIBITOR_REGULATORY_EVENT_CAP", "sector": "cell_therapy_healthcare_commercialization_watch", "primary_archetype": "cell_therapy_commercialization_watch_without_regulatory_partner_revenue_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-07", "entry_date": "2024-03-07", "entry_price": 19060.0, "evidence_available_at_that_date": "cell-therapy / healthcare commercialization watch without confirmed regulatory endpoint, partner channel, launch revenue, reimbursement or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["cell_therapy_commercialization_watch", "healthcare_platform_recovery", "relative_strength_rebound"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "revenue_margin_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/085/085660/2024.csv", "profile_path": "atlas/symbol_profiles/085/085660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.18, "MFE_90D_pct": 10.18, "MFE_180D_pct": 12.28, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -14.06, "MAE_90D_pct": -20.46, "MAE_180D_pct": -20.46, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-27", "peak_price": 21000.0, "drawdown_after_peak_pct": -27.81, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.91, "four_b_full_window_peak_proximity": 0.91, "four_b_timing_verdict": "cell_therapy_commercialization_watch_was_false_stage2_due_missing_regulatory_partner_revenue_margin_bridge", "four_b_evidence_type": ["bio_commercialization_watch", "bridge_missing", "limited_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_cell_therapy_commercialization_watch_without_partner_revenue_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_cell_therapy_commercialization_watch_counts_without_regulatory_partner_revenue_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_before_2025-06-25_CA_candidate", "same_entry_group_id": "R7L95_C23_085660_2024-03-07_19060", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R7L95_C23_APTABIO_2024_STAGE4B_NOX_INHIBITOR_REGULATORY_EVENT_CAP", "case_id": "R7L95_C23_APTABIO_2024_NOX_INHIBITOR_REGULATORY_EVENT_CAP_4B", "symbol": "293780", "company_name": "압타바이오", "round": "R7", "loop": "95", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE_VS_CELL_THERAPY_COMMERCIALIZATION_FALSE_STAGE2_AND_NOX_INHIBITOR_REGULATORY_EVENT_CAP", "sector": "NOX_inhibitor_regulatory_development_event_premium", "primary_archetype": "NOX_inhibitor_regulatory_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-07-11", "entry_date": "2024-07-11", "entry_price": 14600.0, "evidence_available_at_that_date": "NOX inhibitor / regulatory-development event premium after July bio event spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["NOX_inhibitor_regulatory_event", "bio_event_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "partner_regulatory_funding_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/293/293780/2024.csv", "profile_path": "atlas/symbol_profiles/293/293780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.1, "MFE_90D_pct": 6.1, "MFE_180D_pct": 6.1, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -41.78, "MAE_90D_pct": -48.56, "MAE_180D_pct": -48.56, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 15490.0, "drawdown_after_peak_pct": -48.56, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing_NOX_inhibitor_regulatory_event_cap", "four_b_evidence_type": ["bio_regulatory_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_NOX_inhibitor_regulatory_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_NOX_inhibitor_regulatory_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2021_CA", "same_entry_group_id": "R7L95_C23_293780_2024-07-11_14600", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L95_C23_SCD_2024_BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE_POSITIVE", "trigger_id": "R7L95_C23_SCD_2024_STAGE2_ACTIONABLE_BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE", "symbol": "000250", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 80, "customer_quality_score": 60, "policy_or_regulatory_score": 70, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "biosimilar_global_commercialization_partner_bridge_positive", "MFE_90D_pct": 107.02, "MAE_90D_pct": -12.69, "score_return_alignment_label": "biosimilar_global_commercialization_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L95_C23_CHABIO_2024_CELL_THERAPY_COMMERCIALIZATION_FALSE_STAGE2", "trigger_id": "R7L95_C23_CHABIO_2024_STAGE2_FALSE_POSITIVE_CELL_THERAPY_COMMERCIALIZATION_WATCH", "symbol": "085660", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 50, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "cell_therapy_commercialization_false_stage2", "MFE_90D_pct": 10.18, "MAE_90D_pct": -20.46, "score_return_alignment_label": "cell_therapy_commercialization_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_cell_therapy_commercialization_watch_counts_without_regulatory_partner_revenue_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L95_C23_APTABIO_2024_NOX_INHIBITOR_REGULATORY_EVENT_CAP_4B", "trigger_id": "R7L95_C23_APTABIO_2024_STAGE4B_NOX_INHIBITOR_REGULATORY_EVENT_CAP", "symbol": "293780", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 65, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "NOX_inhibitor_regulatory_event_cap_4B_guard", "MFE_90D_pct": 6.1, "MAE_90D_pct": -48.56, "score_return_alignment_label": "NOX_inhibitor_regulatory_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_NOX_inhibitor_regulatory_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": "95", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIOSIMILAR_GLOBAL_COMMERCIALIZATION_PARTNER_BRIDGE_VS_CELL_THERAPY_COMMERCIALIZATION_FALSE_STAGE2_AND_NOX_INHIBITOR_REGULATORY_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["biosimilar_global_commercialization_positive", "cell_therapy_commercialization_false_stage2", "NOX_inhibitor_regulatory_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C23 rows need explicit regulatory path, partner/channel visibility, launch revenue, reimbursement or milestone/supply economics, margin or revision bridge before positive promotion.
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
10. Add tests that bridge-missing C23 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R7
completed_loop = 95
next_round = R8
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
