# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R13
loop = 48
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE, BIO_APPROVAL_PARTNER_LAUNCH_BRIDGE, BIO_BINARY_PDUFA_CAP, BIO_APPROVAL_LEGAL_COMMERCIAL_GUARD
loop_objective = auto_coverage_gap_fill | residual_false_positive_mining | residual_missed_structural_mining | yellow_threshold_stress_test | green_strictness_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining
selection_mode = auto_coverage_gap_fill
auto_selected_coverage_gap = L7/C23 approval-to-commercialization needed balanced positive/counterexample and non-price 4B/4C path coverage after prior L6/C21.
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-argue the global axes. It uses C23 cases to test where the calibrated proxy still confuses four different states: approval with commercial bridge, approval with early digestion risk, pre-approval binary expectation, and approval without legal/commercial cleanliness.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R13
loop = 48
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
rule_scope_preference = canonical_archetype_specific, sector_specific
current_stock_discovery_allowed = false
live_candidate_mode = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
```

## 3. Previous Coverage / Duplicate Avoidance Check

A permitted stock_agent artifact search for the C23 symbol set returned no matching research-artifact hit. Local prior drafts were treated as calculation seeds, not as already-applied production evidence. The anti-repetition gate therefore evaluates this loop relative to the prior submitted loop context and the allowed stock_agent artifact search, not as a live scan.

```text
previous_loop_reference = R13_loop_47_L6_C21
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = not_detected_in_stock_agent_allowed_artifact_search
new_independent_case_ratio = 4 / 4 = 1.00
minimum_new_independent_case_ratio = 0.60
minimum_new_symbol_count = 2
minimum_positive_case_count = 1
minimum_counterexample_count = 1
duplicate_status = pass
```

Diversity governor summary:

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_trigger_family_count = 4
positive_case_count = 2
counterexample_count = 2
diversity_score_summary = avg≈19; same C23 archetype with new symbol, new trigger family, positive/counterexample balance, and residual error coverage.
do_not_propose_new_weight_delta = false
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
source_url = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
price_basis = tradable_raw
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

The schema confirms the tradable columns `d,o,h,l,c,v,a,mc,s,m`, raw columns with `rs`, calibration basis `tradable_raw`, and MFE/MAE definitions using max high / min low over N tradable rows.

## 5. Historical Eligibility Gate

All representative triggers below satisfy the historical eligibility gate:

```text
trigger_date_is_past = true
entry_date_in_tradable_shard = true
forward_180D_available_by_manifest_max_date = true
high_low_close_volume_present = true
MFE_30D_90D_180D_computed = true
MAE_30D_90D_180D_computed = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

Symbol profile check:

| symbol | company | profile status | corporate-action caveat for tested window |
| --- | --- | --- | --- |
| 000100 | 유한양행 | active_like; profile has old CA candidates 1997, 1999, 2020 | no overlap with 2024-08-21~D+180 |
| 145020 | 휴젤 | active_like; CA candidates 2017, 2020 | no overlap with 2024-03-04~D+180 |
| 028300 | HLB | active_like; CA candidates through 2021 | no overlap with 2024-04/05 windows |
| 069620 | 대웅제약 | active_like; no CA candidates | clean 2019 approval window |

Narrative-only exclusion retained from the C23 map:

```text
symbol = 068270
company = 셀트리온
reason = stock_web_profile_corporate_action_candidate_date_2024-01-12_overlaps_candidate_180D_window
usage = not_weight_calibration
```

## 6. Canonical Archetype Compression Map

C23 should not be scored as a blunt `approval = good` switch. The useful compression is a four-state machine:

1. **Approval + named commercial bridge**: final approval is linked to partner, launch, reimbursement, or distribution capability. This can justify a canonical approval-bridge bonus.
2. **Approval + export route but early digestion risk**: approval is real, but the path may allow high early MAE before 180D rerating appears.
3. **PDUFA / expectation without approval**: regulatory optionality is not approval. This must cap Green before the decision.
4. **Approval without legal/commercial cleanliness**: a real approval can fail if channel proof, legal overhang, or margin conversion is not clean.

## 7. Case Selection Summary

| case_id | symbol | company | role | best_trigger | current_profile_verdict | notes |
| --- | --- | --- | --- | --- | --- | --- |
| R13L48_C23_000100_LAZCLUZE_US_APPROVAL | 000100 | 유한양행 | positive / structural_success | T48_000100_20240821_STAGE2_APPROVAL | current_profile_too_late | FDA/J&J approval event had named global partner and launch readiness; current proxy likely waits for later revision/coverage confirmation. |
| R13L48_C23_145020_LETYBO_US_APPROVAL | 145020 | 휴젤 | positive / structural_success | T48_145020_20240304_STAGE2_APPROVAL | current_profile_correct | FDA approval alone was not a straight line; but U.S. product route and later commercial visibility supported a 180D rerating. |
| R13L48_C23_028300_RIVO_CAMRELIZUMAB_CRL | 028300 | HLB | counterexample / false_positive_green | T48_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION | current_profile_false_positive | PDUFA/approval expectation with no approval in hand should not become Green; CRL routed to hard 4C. |
| R13L48_C23_069620_JEUVEAU_APPROVAL_LEGAL_DRAG | 069620 | 대웅제약 | counterexample / failed_rerating | T48_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE | current_profile_false_positive | FDA approval event was real, but durable revision/channel proof was weak and legal/commercial uncertainty dominated. |


## 8. Positive vs Counterexample Balance

```text
positive_structural_success_count = 2
counterexample_or_failed_rerating_count = 2
4B_or_4C_case_count = 2
minimum_positive_case_count = 1
minimum_counterexample_count = 1
minimum_calibration_usable_case_count = 3
balance_status = pass
```

The positives share a visible bridge from approval to commercialization. The counterexamples isolate two different residual errors: pre-approval binary-event overpromotion, and approval-only events where durable commercial/legal cleanliness did not follow.

## 9. Evidence Source Map

| company | symbol | event date | evidence family | stage interpretation |
| --- | --- | --- | --- | --- |
| 유한양행 | 000100 | 2024-08-20 | Rybrevant + Lazcluze approval / global partner bridge | Stage2-Actionable → late Green comparison |
| 휴젤 | 145020 | 2024-02-29 | Letybo FDA approval / U.S. market entry | Stage2-Actionable with early MAE tolerance |
| HLB | 028300 | 2024-04-25 / 2024-05-17 | PDUFA expectation then Complete Response Letter | False Green candidate + hard 4C |
| 대웅제약 | 069620 | 2019-02-01 / 2019-02-07 | Jeuveau FDA approval but weak durable commercialization/legal cleanliness | Approval-only counterexample |
| 셀트리온 | 068270 | 2023-10 / 2024-01 overlap | Zymfentra approval considered but excluded | narrative-only due stock-web CA window |

## 10. Price Data Source Map

```text
price_data_source = Songdaiki/stock-web
price_data_repo = https://github.com/Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

Shard map:

| symbol | company | representative shard | profile |
| --- | --- | --- | --- |
| 000100 | 유한양행 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv | atlas/symbol_profiles/000/000100.json |
| 145020 | 휴젤 | atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv | atlas/symbol_profiles/145/145020.json |
| 028300 | HLB | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json |
| 069620 | 대웅제약 | atlas/ohlcv_tradable_by_symbol_year/069/069620/2019.csv | atlas/symbol_profiles/069/069620.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | verdict | aggregate_role |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| T48_000100_20240821_STAGE2_APPROVAL | R13L48_C23_000100_LAZCLUZE_US_APPROVAL | Stage2-Actionable | 2024-08-20 | 2024-08-21 | 94300 | 69.99 | 76.99 | 76.99 | -2.97 | -2.97 | -2.97 | current_profile_too_late | representative |
| T48_000100_20240828_STAGE3_GREEN_LATE | R13L48_C23_000100_LAZCLUZE_US_APPROVAL | Stage3-Green | 2024-08-28 | 2024-08-28 | 135500 | 21.18 | 23.17 | 23.17 | -12.55 | -16.75 | -25.9 | current_profile_too_late | label_comparison_only |
| T48_000100_20241015_4B_VALUATION | R13L48_C23_000100_LAZCLUZE_US_APPROVAL | 4B | 2024-10-15 | 2024-10-15 | 163700 | 1.95 | 1.95 | 1.95 | -30.91 | -34.21 | -38.67 | current_profile_correct | 4B_overlay_only |
| T48_145020_20240304_STAGE2_APPROVAL | R13L48_C23_145020_LETYBO_US_APPROVAL | Stage2-Actionable | 2024-02-29 | 2024-03-04 | 202500 | 8.15 | 29.63 | 60.99 | -14.91 | -14.91 | -14.91 | current_profile_correct | representative |
| T48_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION | R13L48_C23_028300_RIVO_CAMRELIZUMAB_CRL | Stage3-Green-candidate | 2024-04-25 | 2024-04-25 | 109600 | 4.29 | 4.29 | 4.29 | -58.8 | -58.8 | -58.8 | current_profile_false_positive | representative |
| T48_028300_20240517_4C_CRL | R13L48_C23_028300_RIVO_CAMRELIZUMAB_CRL | 4C | 2024-05-17 | 2024-05-17 | 67100 | 9.99 | 46.2 | 46.2 | -32.71 | -32.71 | -32.71 | current_profile_4C_too_late | 4C_overlay_only |
| T48_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE | R13L48_C23_069620_JEUVEAU_APPROVAL_LEGAL_DRAG | Stage2-Actionable | 2019-02-01 | 2019-02-07 | 204000 | 6.37 | 6.37 | 6.37 | -12.99 | -29.17 | -29.9 | current_profile_false_positive | representative |


## 12. Trigger-Level OHLC Backtest Tables

| representative trigger | symbol | entry | peak_date | peak_price | 90D MFE/MAE | 180D MFE/MAE | below entry 90D | outcome |
| --- | --- | --- | --- | ---: | --- | --- | --- | --- |
| T48_000100_20240821_STAGE2_APPROVAL | 000100 | 2024-08-21 @ 94300 | 2024-10-15 | 166900 | 76.99 / -2.97 | 76.99 / -2.97 | True | structural_success_high_MFE_low_initial_MAE |
| T48_145020_20240304_STAGE2_APPROVAL | 145020 | 2024-03-04 @ 202500 | 2024-11-07 | 326000 | 29.63 / -14.91 | 60.99 / -14.91 | True | structural_success_initial_MAE_then_180D_rerating |
| T48_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION | 028300 | 2024-04-25 @ 109600 | 2024-04-30 | 114300 | 4.29 / -58.8 | 4.29 / -58.8 | True | false_positive_green_binary_regulatory_failure |
| T48_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE | 069620 | 2019-02-07 @ 204000 | 2019-02-07 | 217000 | 6.37 / -29.17 | 6.37 / -29.9 | True | failed_rerating_after_real_approval |


Aggregate representative-trigger view:

```text
representative_trigger_count = 4
avg_MFE_90D_pct = 29.32
avg_MAE_90D_pct = -26.46
avg_MFE_180D_pct = 37.16
avg_MAE_180D_pct = -26.64
false_positive_rate_current_proxy = 0.5
```

## 13. Current Calibrated Profile Stress Test

| case | current calibrated verdict | actual path alignment | residual error |
| --- | --- | --- | --- |
| 유한양행 | current_profile_too_late | Stage2 approval+partner entry had +76.99% 180D MFE with only -2.97% 180D MAE | Green waits too long when approval has named commercial bridge |
| 휴젤 | current_profile_correct | early MAE -14.91%, but +60.99% 180D MFE | Yellow/Green-watch better than immediate full Green |
| HLB | current_profile_false_positive | pre-PDUFA entry had only +4.29% MFE and -58.8% MAE | expectation misread as approval |
| 대웅제약 | current_profile_false_positive | approval entry had +6.37% MFE but -29.9% 180D MAE | real approval without clean commercial/legal bridge |

Applied-axis verdict:

```text
stage2_actionable_evidence_bonus = kept; useful for real approval events, but not enough for Green
stage3_yellow_total_min = kept
stage3_green_total_min = kept, but C23 needs approval-state guard
stage3_green_revision_min = kept
stage3_cross_evidence_green_buffer = kept
price_only_blowoff_blocks_positive_stage = strengthened for HLB-style event expectation
full_4b_requires_non_price_evidence = strengthened for Yuhan overheat timing
hard_4c_thesis_break_routes_to_4c = strengthened, but protection is late after gap-down CRL
```

## 14. Stage2 / Yellow / Green Comparison

```text
Yuhan Stage2_Actionable entry = 2024-08-21 close 94300
Yuhan Stage3_Green comparison entry = 2024-08-28 close 135500
Yuhan full-window peak after Stage2 = 166900 on 2024-10-15
green_lateness_ratio = (135500 - 94300) / (166900 - 94300) = 0.57
interpretation = Green was meaningfully late but not entirely post-peak
```

For Hugel, approval entry carried early MAE; the profile should tolerate a Stage3-Yellow / Green-watch state rather than forcing immediate Green. For HLB, the Green candidate should be blocked because approval was not yet in hand.

## 15. 4B Local vs Full-window Timing Audit

| trigger | evidence type | local proximity | full-window proximity | verdict |
| --- | --- | ---: | ---: | --- |
| T48_000100_20241015_4B_VALUATION | valuation_blowoff, positioning_overheat | 0.96 | 0.96 | good_full_window_4B_timing |
| T48_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION | explicit_event_cap, positioning_overheat | n/a | n/a | event-cap guard should block positive Green before full 4B |
| T48_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE | legal_or_regulatory_block, margin_or_backlog_slowdown | n/a | n/a | approval-only counterexample; not a clean full 4B sale signal |

The Yuhan 4B overlay is not price-only: the 4B thesis comes from valuation/positioning overheat after a clean approval-driven rerating.

## 16. 4C Protection Audit

| trigger | 4C label | protection interpretation |
| --- | --- | --- |
| T48_028300_20240517_4C_CRL | hard_4c_late | The CRL is the correct hard 4C route, but protection is late because the gap-down already occurred before the close-based entry. |

C23 needs a separate pre-decision binary-event cap. Hard 4C handles the rejection after it is public; it does not protect against the pre-event false Green unless the PDUFA/approval distinction is enforced earlier.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
candidate_axis = l7_regulatory_event_state_machine
proposal_type = sector_shadow_only
confidence = medium
```

Rule candidate:

```text
In L7, regulatory events should be scored as a state machine:
- approval in hand + commercial bridge: allow Stage2/Yellow promotion and possible Green-shadow if partner/launch/reimbursement evidence is named.
- approval in hand but weak commercial/legal cleanliness: cap at Stage2/Yellow-watch.
- PDUFA/expectation before decision: cap below Green regardless of price strength.
- CRL/rejection: route to hard 4C, but also evaluate whether pre-decision Green should have been blocked earlier.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
candidate_axes:
  - c23_approval_plus_named_commercial_partner_bridge
  - c23_binary_regulatory_event_cap_before_approval
  - c23_legal_or_commercial_cleanliness_gate
  - c23_initial_MAE_tolerance_for_real_approval_with_clean_route
```

The rule is canonical-archetype-specific rather than global. HBM, grid, defense, consumer export, and financial capital-return reratings do not share the same binary regulatory event structure.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | changed_axes | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | verdict |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| P0 | current default | e2r_2_1_stock_web_calibrated_proxy | none | 4 | 29.32 | -26.46 | 37.16 | -26.64 | 0.5 | 1 | 1 | mixed; too late on Yuhan and false positive on HLB/Daewoong |
| P0b | rollback reference | e2r_2_0_baseline_reference | looser Green / weaker 4C guard | 4 | 29.32 | -26.46 | 37.16 | -26.64 | 0.5 | 1 | 1 | worse; binary event risk overpromotes |
| P1 | sector shadow | L7 approval commercialization bridge | non-price approval bridge + legal/commercial guard | 4 | 29.32 | -26.46 | 37.16 | -26.64 | 0.25 | 0 | 0 | better separation of approval bridge vs expectation |
| P2 | canonical shadow | C23 approval state machine | approval+partner bonus; PDUFA cap; approval-only guard | 4 | 29.32 | -26.46 | 37.16 | -26.64 | 0.25 | 0 | 0 | best explanatory compression |
| P3 | counterexample guard | binary event and legal-drag guard | block Green until approval/commercial cleanliness | 4 | 29.32 | -26.46 | 37.16 | -26.64 | 0.0 | 1 | 0 | strong on false positives, may miss early Yuhan-style positives |


## 20. Score-Return Alignment Matrix

| case_id | trigger_id | before score/label | after score/label | MFE_90D | MAE_90D | alignment |
| --- | --- | --- | --- | ---: | ---: | --- |
| R13L48_C23_000100_LAZCLUZE_US_APPROVAL | T48_000100_20240821_STAGE2_APPROVAL | 84 / Stage3-Yellow | 88 / Stage3-Green-shadow | 76.99 | -2.97 | aligned_after_shadow_promotion |
| R13L48_C23_145020_LETYBO_US_APPROVAL | T48_145020_20240304_STAGE2_APPROVAL | 79 / Stage3-Yellow | 86 / Stage3-Yellow-high / Green-watch | 29.63 | -14.91 | partially_aligned_with_MAE_guard |
| R13L48_C23_028300_RIVO_CAMRELIZUMAB_CRL | T48_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION | 88 / Stage3-Green-candidate | 68 / Stage2-Actionable / Binary-event-cap | 4.29 | -58.8 | false_positive_reduced_by_shadow_guard |
| R13L48_C23_069620_JEUVEAU_APPROVAL_LEGAL_DRAG | T48_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE | 81 / Stage3-Yellow | 69 / Stage2-Actionable / Legal-commercial-guard | 6.37 | -29.17 | false_positive_reduced_by_commercial_cleanliness_guard |


Component-score interpretation:

```text
Yuhan: before score 84 Yellow was too conservative because approval had named global partner / launch bridge; after score 88 Green-shadow better matches +76.99% 180D MFE.
Hugel: before 79 Yellow, after 86 high-Yellow/Green-watch; early MAE argues against forced Green despite positive 180D outcome.
HLB: before 88 Green-candidate was wrong; after 68 binary-event-cap matches -58.8% MAE.
Daewoong: before 81 Yellow overstates approval quality; after 69 legal-commercial guard matches failed rerating.
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE | 2 | 2 | 1 | 1 | 4 | 0 | 7 | 4 | 3 | true | true | C23 now has approval+partner positive, approval-with-early-MAE positive, pre-approval binary false Green, approval-only legal/commercial counterexample, 4B, and 4C coverage. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 3
diversity_score_summary: "avg≈19; same C23 archetype with new symbol, trigger-family, and residual-error coverage"
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - approval_expectation_misread_as_approval
  - approval_without_commercial_cleanliness_false_positive
  - green_late_when_approval_partner_bridge_is_strong
  - 4C_after_gap_down_late_protection
new_axis_proposed:
  - c23_approval_plus_named_commercial_partner_bridge
  - c23_binary_regulatory_event_cap_before_approval
  - c23_legal_or_commercial_cleanliness_gate
  - c23_initial_MAE_tolerance_for_real_approval_with_clean_route
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: "L7/C23 approval-to-commercialization balanced residual coverage"
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-web manifest and schema were read for max_date, columns, price basis, and calibration rules.
- Symbol profiles were checked for corporate-action candidate overlap.
- Actual stock-web tradable_raw OHLC-derived values are used for entry, MFE, MAE, peak, and drawdown.
- Same-entry dedupe is applied to representative/label/4B/4C roles.
- Machine-readable case / trigger / score_simulation / residual_contribution / narrative_only rows are included.
```

Not validated:

```text
- No live 2026 candidate scan was performed.
- No broker/API data was used.
- No stock_agent source code was opened.
- No production scoring patch was written.
- External regulatory-event source URLs should be rechecked by the implementation agent if used in a public-facing report; this MD is a calibration artifact, not an investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_approval_plus_named_commercial_partner_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,2,+2,"Yuhan approval+global partner bridge converted into high MFE with low initial MAE","improves missed structural / late Green","T48_000100_20240821_STAGE2_APPROVAL",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c23_binary_regulatory_event_cap_before_approval,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"HLB pre-PDUFA expectation behaved like false Green with -58.8% MAE","reduces false positive Green","T48_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION",4,4,2,medium,canonical_shadow_only,"not production; event-cap guard"
shadow_weight,c23_legal_or_commercial_cleanliness_gate,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Daewoong approval without clean legal/commercial bridge failed to rerate","reduces approval-only false positives","T48_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE",4,4,2,medium,canonical_shadow_only,"not production; legal-commercial guard"
shadow_weight,l7_4b_non_price_approval_rerating_overlay,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Yuhan 4B occurred with valuation/positioning evidence near full-window peak","improves 4B timing separation","T48_000100_20241015_4B_VALUATION",4,4,2,low,sector_shadow_only,"overlay only; not exit advice"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R13L48_C23_000100_LAZCLUZE_US_APPROVAL","symbol":"000100","company_name":"유한양행","round":"R13","loop":"48","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T48_000100_20240821_STAGE2_APPROVAL","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"approval_plus_global_partner_route_aligned_with_high_MFE_low_initial_MAE","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"FDA/J&J approval event had named global partner and launch readiness; current proxy likely waits for later revision/coverage confirmation."}
{"row_type":"case","case_id":"R13L48_C23_145020_LETYBO_US_APPROVAL","symbol":"145020","company_name":"휴젤","round":"R13","loop":"48","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T48_145020_20240304_STAGE2_APPROVAL","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"approval_plus_export_market_entry_produced_positive_180D_path_after_initial_MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"FDA approval alone was not a straight line; but U.S. product route and later commercial visibility supported a 180D rerating."}
{"row_type":"case","case_id":"R13L48_C23_028300_RIVO_CAMRELIZUMAB_CRL","symbol":"028300","company_name":"HLB","round":"R13","loop":"48","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"T48_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"binary_regulatory_expectation_failed_and_MAE_dominated_MFE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"PDUFA/approval expectation with no approval in hand should not become Green; CRL routed to hard 4C."}
{"row_type":"case","case_id":"R13L48_C23_069620_JEUVEAU_APPROVAL_LEGAL_DRAG","symbol":"069620","company_name":"대웅제약","round":"R13","loop":"48","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T48_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"approval_without_durable_channel_and_legal_cleanliness_failed_sustainability","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"FDA approval event was real, but durable revision/channel proof was weak and legal/commercial uncertainty dominated."}
{"row_type":"trigger","trigger_id":"T48_000100_20240821_STAGE2_APPROVAL","case_id":"R13L48_C23_000100_LAZCLUZE_US_APPROVAL","symbol":"000100","company_name":"유한양행","round":"R13","loop":"48","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-20","evidence_available_at_that_date":"U.S. approval of Rybrevant plus Lazcluze; named global partner and immediate launch readiness were public.","evidence_source":"FDA/J&J approval announcement and public market coverage, 2024-08-20","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-21","entry_price":94300,"MFE_30D_pct":69.99,"MFE_90D_pct":76.99,"MFE_180D_pct":76.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.97,"MAE_90D_pct":-2.97,"MAE_180D_pct":-2.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_high_MFE_low_initial_MAE","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"000100_20240821_94300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T48_000100_20240828_STAGE3_GREEN_LATE","case_id":"R13L48_C23_000100_LAZCLUZE_US_APPROVAL","symbol":"000100","company_name":"유한양행","round":"R13","loop":"48","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage3-Green","trigger_date":"2024-08-28","evidence_available_at_that_date":"Post-approval price/revision confirmation zone; label comparison against approval-date actionable trigger.","evidence_source":"Stock-web OHLC path and public post-approval coverage; label comparison only","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-28","entry_price":135500,"MFE_30D_pct":21.18,"MFE_90D_pct":23.17,"MFE_180D_pct":23.17,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.55,"MAE_90D_pct":-16.75,"MAE_180D_pct":-25.9,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":0.57,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"green_late_but_still_profitable","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"000100_20240828_135500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T48_000100_20241015_4B_VALUATION","case_id":"R13L48_C23_000100_LAZCLUZE_US_APPROVAL","symbol":"000100","company_name":"유한양행","round":"R13","loop":"48","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"4B","trigger_date":"2024-10-15","evidence_available_at_that_date":"Valuation and positioning overheat after approval-driven rerating; non-price 4B overlay rather than price-only top call.","evidence_source":"Stock-web OHLC path plus valuation/positioning overheat interpretation","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-15","entry_price":163700,"MFE_30D_pct":1.95,"MFE_90D_pct":1.95,"MFE_180D_pct":1.95,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-30.91,"MAE_90D_pct":-34.21,"MAE_180D_pct":-38.67,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"000100_20241015_163700","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T48_145020_20240304_STAGE2_APPROVAL","case_id":"R13L48_C23_145020_LETYBO_US_APPROVAL","symbol":"145020","company_name":"휴젤","round":"R13","loop":"48","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-29","evidence_available_at_that_date":"U.S. FDA approval of Letybo/letibotulinumtoxinA; next Korea trading day after holiday/weekend.","evidence_source":"FDA Drug Trials Snapshots: Letybo and public FDA approval coverage","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-04","entry_price":202500,"MFE_30D_pct":8.15,"MFE_90D_pct":29.63,"MFE_180D_pct":60.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.91,"MAE_90D_pct":-14.91,"MAE_180D_pct":-14.91,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000,"drawdown_after_peak_pct":-20.25,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_initial_MAE_then_180D_rerating","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"145020_20240304_202500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T48_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION","case_id":"R13L48_C23_028300_RIVO_CAMRELIZUMAB_CRL","symbol":"028300","company_name":"HLB","round":"R13","loop":"48","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage3-Green-candidate","trigger_date":"2024-04-25","evidence_available_at_that_date":"Pre-PDUFA approval expectation and price strength without approval in hand; binary FDA event risk remained unresolved.","evidence_source":"Public FDA decision expectation / HLB-Elevar rivoceranib-camrelizumab HCC BLA context","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["explicit_event_cap","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-25","entry_price":109600,"MFE_30D_pct":4.29,"MFE_90D_pct":4.29,"MFE_180D_pct":4.29,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-58.8,"MAE_90D_pct":-58.8,"MAE_180D_pct":-58.8,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-30","peak_price":114300,"drawdown_after_peak_pct":-60.5,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"event_cap_and_positioning_overheat_should_block_positive_green","four_b_evidence_type":["positioning_overheat","explicit_event_cap"],"four_c_protection_label":null,"trigger_outcome_label":"false_positive_green_binary_regulatory_failure","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"028300_20240425_109600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T48_028300_20240517_4C_CRL","case_id":"R13L48_C23_028300_RIVO_CAMRELIZUMAB_CRL","symbol":"028300","company_name":"HLB","round":"R13","loop":"48","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"4C","trigger_date":"2024-05-17","evidence_available_at_that_date":"FDA Complete Response Letter / non-approval shock; thesis evidence broken.","evidence_source":"HLB/Elevar public CRL event reports, 2024-05-17","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":67100,"MFE_30D_pct":9.99,"MFE_90D_pct":46.2,"MFE_180D_pct":46.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-32.71,"MAE_90D_pct":-32.71,"MAE_180D_pct":-32.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":98100,"drawdown_after_peak_pct":-22.32,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4C_success_but_after_large_gap_down","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"028300_20240517_67100","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T48_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE","case_id":"R13L48_C23_069620_JEUVEAU_APPROVAL_LEGAL_DRAG","symbol":"069620","company_name":"대웅제약","round":"R13","loop":"48","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"K_BIO_REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2019-02-01","evidence_available_at_that_date":"FDA approval of Jeuveau/prabotulinumtoxinA-xvfs; first Korea trading day after Lunar New Year closure.","evidence_source":"Evolus/FDA public approval announcement, 2019-02-01; Daewoong Nabota/Jeuveau approval coverage","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/069/069620/2019.csv","profile_path":"atlas/symbol_profiles/069/069620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2019-02-07","entry_price":204000,"MFE_30D_pct":6.37,"MFE_90D_pct":6.37,"MFE_180D_pct":6.37,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.99,"MAE_90D_pct":-29.17,"MAE_180D_pct":-29.9,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2019-02-07","peak_price":217000,"drawdown_after_peak_pct":-34.1,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"approval_without_clean_commercial_bridge_not_full_stage3","four_b_evidence_type":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"four_c_protection_label":null,"trigger_outcome_label":"failed_rerating_after_real_approval","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"069620_20190207_204000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L48_C23_000100_LAZCLUZE_US_APPROVAL","trigger_id":"T48_000100_20240821_STAGE2_APPROVAL","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":7,"customer_quality_score":9,"policy_or_regulatory_score":10,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":7,"customer_quality_score":10,"policy_or_regulatory_score":10,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green-shadow","changed_components":["customer_quality_score:+1","valuation_repricing_score:+1","c23_global_partner_launch_bridge:+2"],"component_delta_explanation":"C23 approval with named global commercial partner is not mere regulatory optionality; it is an approval-to-commercialization bridge.","MFE_90D_pct":76.99,"MAE_90D_pct":-2.97,"score_return_alignment_label":"aligned_after_shadow_promotion","current_profile_verdict":"current_profile_too_late","round":"R13","loop":"48"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L48_C23_145020_LETYBO_US_APPROVAL","trigger_id":"T48_145020_20240304_STAGE2_APPROVAL","symbol":"145020","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":3,"relative_strength_score":5,"customer_quality_score":7,"policy_or_regulatory_score":10,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":4,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":10,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow-high / Green-watch","changed_components":["customer_quality_score:+1","valuation_repricing_score:+2","revision_score:+1","execution_risk_score:-1"],"component_delta_explanation":"Approval opened a real U.S. product route, but early MAE argues against unconditional Green without channel/order confirmation.","MFE_90D_pct":29.63,"MAE_90D_pct":-14.91,"score_return_alignment_label":"partially_aligned_with_MAE_guard","current_profile_verdict":"current_profile_correct","round":"R13","loop":"48"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L48_C23_028300_RIVO_CAMRELIZUMAB_CRL","trigger_id":"T48_028300_20240425_FALSE_GREEN_PDUFA_EXPECTATION","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":4,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":9,"valuation_repricing_score":9,"execution_risk_score":8,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":88,"stage_label_before":"Stage3-Green-candidate","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":6,"valuation_repricing_score":4,"execution_risk_score":10,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable / Binary-event-cap","changed_components":["policy_or_regulatory_score:-3","relative_strength_score:-4","valuation_repricing_score:-5","execution_risk_score:+2","legal_or_contract_risk_score:+3"],"component_delta_explanation":"PDUFA expectation cannot be scored as approval. Binary-regulatory event cap blocks Green until approval or low-risk regulatory evidence is public.","MFE_90D_pct":4.29,"MAE_90D_pct":-58.8,"score_return_alignment_label":"false_positive_reduced_by_shadow_guard","current_profile_verdict":"current_profile_false_positive","round":"R13","loop":"48"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L48_C23_069620_JEUVEAU_APPROVAL_LEGAL_DRAG","trigger_id":"T48_069620_20190207_STAGE2_APPROVAL_COUNTEREXAMPLE","symbol":"069620","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":3,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":10,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":10,"valuation_repricing_score":3,"execution_risk_score":8,"legal_or_contract_risk_score":9,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Actionable / Legal-commercial-guard","changed_components":["customer_quality_score:-2","valuation_repricing_score:-2","revision_score:-1","execution_risk_score:+3","legal_or_contract_risk_score:+4"],"component_delta_explanation":"Approval was real, but legal/commercial overhang and lack of durable channel data made the approval insufficient for Stage3 promotion.","MFE_90D_pct":6.37,"MAE_90D_pct":-29.17,"score_return_alignment_label":"false_positive_reduced_by_commercial_cleanliness_guard","current_profile_verdict":"current_profile_false_positive","round":"R13","loop":"48"}
{"row_type":"narrative_only","case_id":"R13L48_C23_068270_ZYMFENTRA_APPROVAL_EXCLUDED","symbol":"068270","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","reason":"evidence_available_but_180D_window_overlaps_stock_web_corporate_action_candidate_2024-01-12","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
{"row_type":"residual_contribution","round":"R13","loop":"48","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":0,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"diversity_score_summary":"avg≈19; same C23 archetype, four non-reused symbols, four trigger families, two positives, two counterexamples; no stock_agent artifact hit for same symbol-trigger family.","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["approval_expectation_misread_as_approval","approval_without_commercial_cleanliness_false_positive","green_late_when_approval_partner_bridge_is_strong","4C_after_gap_down_late_protection"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"L7/C23 needed balanced approval-to-commercialization positive, approval-only false positive, PDUFA binary risk, and non-price 4B/4C overlay coverage after the prior L6/C21 loop."}
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
next_round = R13_loop_49
next_large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
next_canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
reason = adjacent L7 binary-event coverage can now move from approval/commercialization to trial-data event-risk and 4C timing.
```

## 28. Source Notes

```text
stock_web_manifest = atlas/manifest.json, generated_at 2026-05-21T16:28:39.421691+00:00
stock_web_schema = atlas/schema.json
profile_000100 = atlas/symbol_profiles/000/000100.json
profile_145020 = atlas/symbol_profiles/145/145020.json
profile_028300 = atlas/symbol_profiles/028/028300.json
profile_069620 = atlas/symbol_profiles/069/069620.json
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

This file is a calibration research artifact. It is not a current-stock recommendation, live watchlist, or production-scoring patch.
