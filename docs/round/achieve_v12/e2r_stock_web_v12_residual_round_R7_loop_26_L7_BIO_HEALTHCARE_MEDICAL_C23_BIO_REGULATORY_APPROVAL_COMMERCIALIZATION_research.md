# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R7
loop = 26
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
output_file = e2r_stock_web_v12_residual_round_R7_loop_26_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
```

This is not live candidate discovery and not an investment recommendation. It is a historical trigger-level residual calibration note. It intentionally does not inspect `src/e2r` or propose a production patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference

stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The question in this loop is narrower: in C23, when a drug, biologic, or aesthetic therapy crosses from regulatory event to commercialization route, does the current profile wait too long for revision evidence? Conversely, when the event is only approval expectation or a non-core CRL, should the existing hard-4C guard be applied or softened?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R7
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id set =
  - BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY
  - AESTHETIC_BIO_US_APPROVAL_COMMERCIAL_LAUNCH
  - NON_CORE_DELIVERY_FORMAT_CRL_4B_NOT_4C
  - CORE_APPROVAL_FAILURE_HARD_4C
loop_objective =
  - coverage_gap_fill
  - counterexample_mining
  - sector_specific_rule_discovery
  - green_strictness_stress_test
  - 4B_non_price_requirement_stress_test
```

## 3. Previous Coverage / Duplicate Avoidance Check

A repository search over allowed research artifact terms did not surface prior C23 rows for `000100`, `145020`, or `028300` under this exact canonical archetype. The loop therefore treats all four cases as new independent C23 samples. The `000100` approval and `000100` non-core CRL rows share a symbol but not the same trigger family, evidence family, entry date, or outcome role.

```text
auto_selected_coverage_gap = R7/C23 approval-to-commercialization coverage needed positive + counterexample balance.
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 4
new_trigger_family_count = 4
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields used in this loop:

| field | value |
|---|---:|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Source validation: `atlas/manifest.json` reports `max_date = 2026-02-20`, `price_adjustment_status = raw_unadjusted_marcap`, and `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`. The manifest also states that raw/unadjusted OHLC is used, zero-volume/zero-OHLC rows are excluded from calibration shards, and corporate-action-contaminated windows are blocked by default. See source rows: fileciteturn561file0

Symbol profile checks:

| symbol | company | profile_path | 180D corporate-action status |
|---|---|---|---|
| 000100 | 유한양행 | atlas/symbol_profiles/000/000100.json | clean for 2024-08-20 and 2024-12-17 windows; profile CA dates are 1997-01-03, 1999-08-26, 2020-04-08. fileciteturn563file0turn564file0 |
| 145020 | 휴젤 | atlas/symbol_profiles/145/145020.json | clean for 2024-03-04 and 2024-11-06 windows; profile CA dates are 2017-07-31, 2020-07-08, 2020-07-31. fileciteturn566file0 |
| 028300 | HLB | atlas/symbol_profiles/028/028300.json | clean for 2024-03-26 and 2024-05-17 windows; profile CA dates end at 2021-04-01. fileciteturn567file0turn568file0 |

## 5. Historical Eligibility Gate

| gate | status |
|---|---|
| trigger dates are historical | pass |
| entry dates exist in stock-web tradable shards | pass |
| at least 180 trading days available after representative entries | pass |
| high/low/close/volume present | pass |
| corporate-action-contaminated 180D window | none detected from profile CA dates |
| 1Y/2Y quantitative use | non-core in this loop; 30/90/180D are the calibrated windows |

## 6. Canonical Archetype Compression Map

```text
BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY -> C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
AESTHETIC_BIO_US_APPROVAL_COMMERCIAL_LAUNCH -> C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
NON_CORE_DELIVERY_FORMAT_CRL_4B_NOT_4C -> C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
CORE_APPROVAL_FAILURE_HARD_4C -> C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

The key compression is not “FDA approval good / FDA CRL bad.” The useful C23 distinction is:

```text
positive C23 = approval + credible launch/royalty/commercial channel route
watch/4B C23 = non-core formulation, manufacturing, or delivery-format delay that does not break the already-approved core product
4C C23 = core approval route fails, product thesis breaks, or final regulatory evidence contradicts the investment thesis
```

## 7. Case Selection Summary

| case_id | symbol | fine_archetype_id | role | case_type | current_profile_verdict | independent_weight |
|---|---|---|---|---|---|---:|
| R7L26-C23-000100-LAZERTINIB-US-APPROVAL | 000100 유한양행 | BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY | positive | structural_success | current_profile_too_late | 1.0 |
| R7L26-C23-145020-LETYBO-US-APPROVAL | 145020 휴젤 | AESTHETIC_BIO_US_APPROVAL_COMMERCIAL_LAUNCH | positive | structural_success | current_profile_too_late | 1.0 |
| R7L26-C23-000100-RYBREVANT-SC-CRL | 000100 유한양행 | NON_CORE_DELIVERY_FORMAT_CRL_4B_NOT_4C | counterexample | 4B_overlay_success | current_profile_correct | 0.5 |
| R7L26-C23-028300-CORE-APPROVAL-FAILURE | 028300 HLB | CORE_APPROVAL_FAILURE_HARD_4C | counterexample | false_positive_green | current_profile_correct | 1.0 |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 4
representative_trigger_count = 4
```

The case mix is deliberately balanced. 유한양행 and 휴젤 test the positive approval-to-commercialization bridge. The Rybrevant subcutaneous CRL tests a non-core delay that should remain 4B/watch rather than hard 4C. HLB tests a hard approval-failure route that should block price-only Green and route to 4C when the core regulatory thesis breaks.

## 9. Evidence Source Map

| evidence family | source used | interpretation |
|---|---|---|
| Lazertinib + Rybrevant approval | Reuters reported FDA approval of J&J's chemotherapy-free Rybrevant + lazertinib combination and noted imminent launch / commercial expectations. citeturn521049news1 | C23 positive; commercialization/royalty route became explicit. |
| Letybo US approval / launch | Allure and NY Post described Letybo as FDA-approved and entering US dermatologist availability; Allure identifies Hugel as manufacturer. citeturn582758news0turn582758news1 | C23 positive but high-MAE; approval needs launch/channel conversion. |
| Rybrevant subcutaneous CRL | Reuters reported FDA declined the injectable/subcutaneous version because of manufacturing inspection observations and that it was unrelated to efficacy/safety/formulation, with no extra clinical studies requested. citeturn521049news0 | Non-core delay: 4B/watch, not hard 4C. |
| HLB core approval failure | Public CRL event is used as known non-price thesis-break context, but this run did not retrieve a high-quality web source for the CRL text. Stock-web price rows verify the price path; source quality is flagged as `source_quality_limited_for_event_text`. | Hard 4C path; do not promote approval-expectation price-only Green. |

## 10. Price Data Source Map

| symbol | shard(s) used | key stock-web rows |
|---|---|---|
| 000100 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv; 2025.csv | 2024-08-20 close 94,000; peak high 166,900 on 2024-10-15; 2025 forward lows used for 180D drawdown. fileciteturn569file0turn570file0 |
| 145020 | atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv | 2024-03-04 close 202,500; 2024-11-07 high 326,000; post-peak low 237,000. fileciteturn573file0turn574file0 |
| 028300 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv; 2025.csv | 2024-03-26 close 120,800; 2024-05-17 close 67,100; 2024-05-21 low 45,150; rebound high 98,100. fileciteturn577file0turn575file0turn576file0 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | current_profile_verdict | role |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| R7L26-T001 | 000100 유한양행 | Stage2-Actionable | 2024-08-20 | 2024-08-20 | 94000 | 70.53 | 77.55 | 77.55 | -2.66 | -2.66 | -2.66 | current_profile_too_late | representative |
| R7L26-T002 | 000100 유한양행 | Stage3-Green | 2024-09-20 | 2024-09-20 | 145400 | 14.79 | 14.79 | 14.79 | -7.5 | -25.03 | -30.95 | current_profile_too_late | label_comparison_only |
| R7L26-T003 | 145020 휴젤 | Stage2-Actionable | 2024-03-04 | 2024-03-04 | 202500 | 8.15 | 29.63 | 60.99 | -14.91 | -14.91 | -14.91 | current_profile_too_late | representative |
| R7L26-T004 | 145020 휴젤 | Stage4B | 2024-11-06 | 2024-11-06 | 321000 | 1.56 | 1.56 | 1.56 | -26.17 | -26.17 | -26.17 | current_profile_correct | 4B_overlay_only |
| R7L26-T005 | 000100 유한양행 | Stage4B | 2024-12-16 | 2024-12-17 | 112800 | 23.67 | 24.73 | 24.73 | -3.37 | -10.99 | -10.99 | current_profile_correct | representative |
| R7L26-T006 | 028300 HLB | Stage3-Green-candidate-blocked | 2024-03-26 | 2024-03-26 | 120800 | 6.79 | 6.79 | 6.79 | -29.55 | -62.62 | -62.62 | current_profile_correct | representative |
| R7L26-T007 | 028300 HLB | Stage4C | 2024-05-17 | 2024-05-17 | 67100 | 9.99 | 46.2 | 46.2 | -32.71 | -32.71 | -32.71 | current_profile_correct | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger interpretation

| trigger_id | outcome | mechanism |
|---|---|---|
| R7L26-T001 | structural_success | Approval acted like a bridge being laid across a river before the traffic count was visible. The market priced the crossing once the bridge existed, not after every toll receipt was counted. |
| R7L26-T003 | high_mae_success | Approval was necessary but not sufficient. The initial path pulled back -14.91% before the later commercial route carried the stock to +60.99% MFE. |
| R7L26-T005 | 4B_overlay_not_4C | A CRL attached to a delivery format/manufacturing inspection is a bent road sign, not a collapsed bridge. It should slow the thesis, not kill it. |
| R7L26-T006 | false_positive_green_if_unblocked | A price tower built on approval expectation without approval evidence broke sharply. This supports the existing price-only blowoff guard. |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely decision | actual 180D path | verdict |
|---|---|---|---|
| 유한양행 approval | Stage2/Yellow until revision proof | +77.55% MFE180, -2.66% MAE180 | current_profile_too_late |
| 휴젤 approval | Stage2/Yellow until launch proof | +60.99% MFE180, -14.91% MAE180 | current_profile_too_late, but high-MAE |
| 유한양행 subcutaneous CRL | 4B/watch if non-core details are parsed | +24.73% MFE180, -10.99% MAE180 | current_profile_correct if not routed to hard 4C |
| HLB approval expectation | block Green / hard 4C on core failure | +6.79% MFE180, -62.62% MAE180 | current_profile_correct |

Answers to the eight stress-test questions:

```text
1. Current profile catches price-only HLB as blocked, but is late for C23 positive approval-to-commercialization cases.
2. Yuhan and Hugel show that waiting for fully confirmed EPS revision can miss much of the move.
3. Stage2 bonus is directionally right but too generic for C23; approval + credible commercialization deserves a canonical buffer.
4. Yellow threshold 75 is acceptable if C23 bonus is small and evidence-gated.
5. Green 87 / revision 55 is too strict for royalty/launch cases where the regulator has already unlocked the commercial route.
6. Price-only blowoff guard remains appropriate and is strengthened by HLB.
7. Full 4B non-price requirement remains appropriate; Rybrevant SC CRL shows non-core regulatory delay can be a 4B overlay.
8. Hard 4C routing is correct only for core thesis break. Non-core manufacturing/delivery-format CRL should not automatically route to hard 4C.
```

## 14. Stage2 / Yellow / Green Comparison

The clearest lateness audit is 유한양행:

```text
Stage2-Actionable entry = 2024-08-20 close 94,000
Stage3-Green comparison entry = 2024-09-20 close 145,400
full observed peak after Stage2 = 166,900
green_lateness_ratio = (145,400 - 94,000) / (166,900 - 94,000) = 0.705
```

A 0.705 ratio means Green arrived after roughly 70% of the Stage2-to-peak upside had already been consumed. This is not a global argument that Green is always late; it is a C23-specific argument that approved drug / partner launch / royalty routes can be economically real before clean analyst revision thresholds are visible.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---:|---|
| R7L26-T004 | 0.98 | 0.98 | good_full_window_4B_timing |
| R7L26-T005 | 0.22 | 0.33 | non_core_crl_watch_not_full_4C |
| R7L26-T006 | 1.00 | 1.00 | price_only_local_4B_blocks_positive_stage |

The Hugel 4B row is the cleanest full-window 4B. Entry at 321,000 had only +1.56% forward MFE but -26.17% MAE, making it a better risk overlay than a new positive trigger.

## 16. 4C Protection Audit

| case | 4C label | note |
|---|---|---|
| 유한양행 Rybrevant SC CRL | false_break_or_watch_only | CRL did not concern the approved IV product’s efficacy/safety and did not request new clinical studies. Treat as 4B/watch. |
| HLB core approval failure | hard_4c_success | Core approval expectation failed; prior price-only Green candidate had -62.62% MAE90. |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = only one large_sector_id tested in this MD
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

Proposed C23 shadow rules:

```text
1. c23_approval_to_commercialization_bonus:
   Add a small canonical C23 buffer only when regulatory approval is paired with partner launch, royalty route, reimbursement/commercial availability, or channel conversion evidence.

2. c23_non_core_crl_not_4c_guard:
   A CRL tied to manufacturing inspection, delivery format, or administration route is 4B/watch unless it breaks the already-approved core product thesis.

3. c23_core_approval_absence_guard:
   Price strength + regulatory expectation cannot become Stage3-Green without final approval or equivalent regulatory evidence.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | selected cases | avg MFE90 | avg MAE90 | false_positive_rate | score-return alignment |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 4 | 34.68 | -22.80 | 0.25 if HLB were not blocked | mixed: too late for positives, correct for HLB |
| P0b e2r_2_0_baseline_reference | rollback | 4 | lower quality | worse | higher | would over-credit price/expectation |
| P1 sector_specific_candidate_profile | L7 | 4 | 34.68 | -22.80 | unchanged | not enough sector breadth |
| P2 canonical_archetype_candidate_profile | C23 | 4 | 34.68 | -22.80 | lower after C23 guard | best fit |
| P3 counterexample_guard_profile | C23 guard | 2 counterexamples | n/a | n/a | lower | best for CRL/expectation distinction |

## 20. Score-Return Alignment Matrix

| trigger_id | symbol | before | after | changed_components | alignment |
|---|---|---|---|---|---|
| R7L26-T001 | 000100 | 82.0 / Stage3-Yellow | 88.5 / Stage3-Green | c23_partner_commercialization_bonus, approval_to_royalty_visibility_bonus | aligned |
| R7L26-T003 | 145020 | 74.0 / Stage2-Actionable | 79.5 / Stage3-Yellow | aesthetic_us_launch_visibility_buffer | aligned |
| R7L26-T005 | 000100 | 62.0 / 4B-Watch | 64.0 / 4B-Watch | non_core_crl_not_hard_4c_guard | watch_only_aligned |
| R7L26-T006 | 028300 | 86.0 / Blocked-Green | 58.0 / 4C-Watch | core_approval_absence_guard, hard_4c_thesis_break | aligned |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | multiple | 2 | 2 | 2 | 1 | 4 | 0 | 7 | 4 | 2 | false | true | still needs more non-US approvals and reimbursement-launch cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - C23_approval_success_missed_when_revision_lags
  - C23_non_core_CRL_should_not_route_to_hard_4C
new_axis_proposed:
  - c23_approval_to_commercialization_bonus
  - c23_non_core_crl_not_4c_guard
  - c23_core_approval_absence_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c, but only for core thesis breaks
existing_axis_weakened:
  - stage3_green_revision_min as C23-specific exception only
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R7/C23 positive/counterexample balance and CRL distinction gap
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Historical OHLC backtest using Songdaiki/stock-web tradable_raw rows.
- 30D / 90D / 180D MFE and MAE.
- Corporate-action window blocking via symbol profile CA candidate dates.
- Trigger-level C23 residual rule proposal.
```

Non-validation scope:

```text
- No live candidate scan.
- No 2026 recommendation.
- No production scoring change.
- No stock_agent src/e2r inspection.
- 1Y/2Y fields are present as null in JSONL because this loop uses 180D as the calibration window.
- HLB event text source quality is limited in this run; HLB row is retained because OHLC is clean and the event is used as hard-4C context, but a later source-enrichment pass should attach the exact primary event document.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_approval_to_commercialization_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,+1,+1,"Approval with partner launch/royalty or US commercial channel visibility can promote Stage2/Yellow before full consensus revision.","Improved capture of 77.55% and 60.99% 180D MFE cases without allowing price-only HLB.",R7L26-T001|R7L26-T003,4,4,2,medium,canonical_shadow_only,"not production; use only with non-price approval evidence"
shadow_weight,c23_non_core_crl_not_4c_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,+1,+1,"Delivery-format/manufacturing CRL that leaves approved IV/formulation intact is 4B/watch, not hard 4C.","Avoids overreacting to R7L26-T005 where 90D MFE remained +24.73%.",R7L26-T005,4,4,2,medium,canonical_shadow_only,"qualifies hard_4c axis"
shadow_weight,c23_core_approval_absence_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,+1,+1,"If final approval evidence is absent, price/expectation strength cannot become Green.","Blocks R7L26-T006 false Green with -62.62% 90D MAE.",R7L26-T006|R7L26-T007,4,4,2,high,canonical_shadow_only,"strengthens price-only blowoff guard"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R7L26-C23-000100-LAZERTINIB-US-APPROVAL","symbol":"000100","company_name":"유한양행","round":"R7","loop":"26","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L26-T001","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"approval + durable partner commercialization evidence led price before consensus Green could safely arrive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"C23 positive: US approval opened royalty/commercialization route; Green confirmation was too late relative to the upside already captured by Stage2-Actionable."}
{"row_type":"case","case_id":"R7L26-C23-145020-LETYBO-US-APPROVAL","symbol":"145020","company_name":"휴젤","round":"R7","loop":"26","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"AESTHETIC_BIO_US_APPROVAL_COMMERCIAL_LAUNCH","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L26-T003","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"initial FDA approval move had high MAE but commercial launch/US availability route later validated a longer C23 window","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"C23 positive but high-MAE: approval alone was not enough for immediate Green; commercialization channel visibility mattered."}
{"row_type":"case","case_id":"R7L26-C23-000100-RYBREVANT-SC-CRL","symbol":"000100","company_name":"유한양행","round":"R7","loop":"26","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"NON_CORE_DELIVERY_FORMAT_CRL_4B_NOT_4C","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"R7L26-T005","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_non_core_formulation_crl","independent_evidence_weight":0.5,"score_price_alignment":"non-core delivery-format CRL did not behave like thesis-break; 4B overlay was better than hard 4C","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Same company as approval case but a distinct trigger family: subcutaneous formulation CRL tied to manufacturing inspection, not core IV approval, efficacy, or safety."}
{"row_type":"case","case_id":"R7L26-C23-028300-CORE-APPROVAL-FAILURE","symbol":"028300","company_name":"HLB","round":"R7","loop":"26","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CORE_APPROVAL_FAILURE_HARD_4C","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R7L26-T006","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"approval-expectation price ramp without final regulatory evidence produced severe MAE and immediate thesis break","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C23 counterexample: approval expectation without an approval document should not become positive Green; hard 4C was appropriate once the core approval route broke."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","case_id":"R7L26-C23-000100-LAZERTINIB-US-APPROVAL","symbol":"000100","company_name":"유한양행","round":"R7","loop":"26","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"R7L26-T001","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-20","entry_date":"2024-08-20","entry_price":94000,"evidence_available_at_that_date":"US FDA approval of lazertinib + amivantamab for EGFR-mutated NSCLC made the royalty/commercialization route explicit.","evidence_source":"Reuters Aug 20 2024; FDA/partner approval report; stock-web 000100 2024 shard.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","MFE_30D_pct":70.53,"MFE_90D_pct":77.55,"MFE_180D_pct":77.55,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.66,"MAE_90D_pct":-2.66,"MAE_180D_pct":-2.66,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":"not_applicable_for_stage2_representative","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L26-G001","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","case_id":"R7L26-C23-000100-LAZERTINIB-US-APPROVAL","symbol":"000100","company_name":"유한양행","round":"R7","loop":"26","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"R7L26-T002","trigger_type":"Stage3-Green","trigger_date":"2024-09-20","entry_date":"2024-09-20","entry_price":145400,"evidence_available_at_that_date":"By this point, approval news, partner launch logic, and price-relative-strength had already become consensus-like.","evidence_source":"stock-web 000100 2024 shard; Reuters approval report.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","MFE_30D_pct":14.79,"MFE_90D_pct":14.79,"MFE_180D_pct":14.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.5,"MAE_90D_pct":-25.03,"MAE_180D_pct":-30.95,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":0.705,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_low_incremental_upside","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L26-G002","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"same_case_label_comparison_green_lateness","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","case_id":"R7L26-C23-145020-LETYBO-US-APPROVAL","symbol":"145020","company_name":"휴젤","round":"R7","loop":"26","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"AESTHETIC_BIO_US_APPROVAL_COMMERCIAL_LAUNCH","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"R7L26-T003","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":202500,"evidence_available_at_that_date":"Letybo FDA approval had become tradable in Korea; later US availability confirmed the commercialization route.","evidence_source":"Allure 2025 confirmation of Letybo FDA-approved US availability; stock-web 145020 2024 shard.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","MFE_30D_pct":8.15,"MFE_90D_pct":29.63,"MFE_180D_pct":60.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.91,"MAE_90D_pct":-14.91,"MAE_180D_pct":-14.91,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000,"drawdown_after_peak_pct":-27.3,"green_lateness_ratio":"not_applicable_no_clean_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L26-G003","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","case_id":"R7L26-C23-145020-LETYBO-US-APPROVAL","symbol":"145020","company_name":"휴젤","round":"R7","loop":"26","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"AESTHETIC_BIO_US_APPROVAL_COMMERCIAL_LAUNCH","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"R7L26-T004","trigger_type":"Stage4B","trigger_date":"2024-11-06","entry_date":"2024-11-06","entry_price":321000,"evidence_available_at_that_date":"After a long post-approval run, the row behaved like a valuation/positioning overlay: tiny extra MFE and large forward MAE.","evidence_source":"stock-web 145020 2024 shard.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","MFE_30D_pct":1.56,"MFE_90D_pct":1.56,"MFE_180D_pct":1.56,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-26.17,"MAE_90D_pct":-26.17,"MAE_180D_pct":-26.17,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000,"drawdown_after_peak_pct":-27.3,"green_lateness_ratio":"not_applicable_4B_overlay","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L26-G004","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_4B_overlay_timing","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","case_id":"R7L26-C23-000100-RYBREVANT-SC-CRL","symbol":"000100","company_name":"유한양행","round":"R7","loop":"26","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"NON_CORE_DELIVERY_FORMAT_CRL_4B_NOT_4C","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"R7L26-T005","trigger_type":"Stage4B","trigger_date":"2024-12-16","entry_date":"2024-12-17","entry_price":112800,"evidence_available_at_that_date":"FDA declined the subcutaneous Rybrevant form due to manufacturing inspection observations; the approved IV formulation was not impacted and no additional clinical studies were requested.","evidence_source":"Reuters Dec 16 2024; stock-web 000100 2024/2025 shards.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["legal_or_regulatory_block","contract_delay"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv|atlas/ohlcv_tradable_by_symbol_year/000/000100/2025.csv","profile_path":"atlas/symbol_profiles/000/000100.json","MFE_30D_pct":23.67,"MFE_90D_pct":24.73,"MFE_180D_pct":24.73,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.37,"MAE_90D_pct":-10.99,"MAE_180D_pct":-10.99,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-07","peak_price":140700,"drawdown_after_peak_pct":-28.64,"green_lateness_ratio":"not_applicable_4B_overlay","four_b_local_peak_proximity":0.22,"four_b_full_window_peak_proximity":0.33,"four_b_timing_verdict":"non_core_crl_watch_not_full_4C","four_b_evidence_type":["legal_or_regulatory_block","contract_delay"],"four_c_protection_label":"false_break_or_watch_only","trigger_outcome_label":"4B_overlay_not_4C","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L26-G005","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_non_core_formulation_crl","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","case_id":"R7L26-C23-028300-CORE-APPROVAL-FAILURE","symbol":"028300","company_name":"HLB","round":"R7","loop":"26","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CORE_APPROVAL_FAILURE_HARD_4C","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"R7L26-T006","trigger_type":"Stage3-Green-candidate-blocked","trigger_date":"2024-03-26","entry_date":"2024-03-26","entry_price":120800,"evidence_available_at_that_date":"Price and public expectation had run ahead of an FDA decision, but final regulatory approval evidence was not yet available.","evidence_source":"stock-web 028300 2024 shard; public CRL event used as known non-price thesis-break context, source quality flagged below.","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["unknown_or_not_supported"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","MFE_30D_pct":6.79,"MFE_90D_pct":6.79,"MFE_180D_pct":6.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-29.55,"MAE_90D_pct":-62.62,"MAE_180D_pct":-62.62,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-26","peak_price":129000,"drawdown_after_peak_pct":-65.0,"green_lateness_ratio":"not_applicable_blocked_green_candidate","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_blocks_positive_stage","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"pre_4C_watch","trigger_outcome_label":"false_positive_green_if_unblocked","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L26-G006","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","case_id":"R7L26-C23-028300-CORE-APPROVAL-FAILURE","symbol":"028300","company_name":"HLB","round":"R7","loop":"26","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CORE_APPROVAL_FAILURE_HARD_4C","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"R7L26-T007","trigger_type":"Stage4C","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":67100,"evidence_available_at_that_date":"Core approval route broke; the stock-web row shows the immediate limit-down style response and subsequent high volatility.","evidence_source":"stock-web 028300 2024 shard; public CRL event used as known non-price thesis-break context, source quality flagged below.","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","MFE_30D_pct":9.99,"MFE_90D_pct":46.2,"MFE_180D_pct":46.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-32.71,"MAE_90D_pct":-32.71,"MAE_180D_pct":-32.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":98100,"drawdown_after_peak_pct":-38.84,"green_lateness_ratio":"not_applicable_4C","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"hard_4C_not_4B","four_b_evidence_type":["legal_or_regulatory_block"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L26-G007","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_4C_overlay_timing","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L26-C23-000100-LAZERTINIB-US-APPROVAL","trigger_id":"R7L26-T001","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":10,"margin_bridge_score":35,"revision_score":45,"relative_strength_score":80,"customer_quality_score":90,"policy_or_regulatory_score":95,"valuation_repricing_score":75,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":10,"margin_bridge_score":35,"revision_score":45,"relative_strength_score":80,"customer_quality_score":90,"policy_or_regulatory_score":95,"valuation_repricing_score":75,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88.5,"stage_label_after":"Stage3-Green","changed_components":["c23_partner_commercialization_bonus","approval_to_royalty_visibility_bonus"],"component_delta_explanation":"C23 approval + credible partner launch/royalty route deserves small canonical bonus before full EPS revision lands.","MFE_90D_pct":77.55,"MAE_90D_pct":-2.66,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L26-C23-145020-LETYBO-US-APPROVAL","trigger_id":"R7L26-T003","symbol":"145020","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":10,"margin_bridge_score":30,"revision_score":35,"relative_strength_score":55,"customer_quality_score":65,"policy_or_regulatory_score":90,"valuation_repricing_score":60,"execution_risk_score":45,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":10,"margin_bridge_score":30,"revision_score":35,"relative_strength_score":55,"customer_quality_score":65,"policy_or_regulatory_score":90,"valuation_repricing_score":60,"execution_risk_score":45,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":79.5,"stage_label_after":"Stage3-Yellow","changed_components":["aesthetic_us_launch_visibility_buffer"],"component_delta_explanation":"FDA approval alone remains high-MAE; add only a Yellow buffer until channel/launch conversion appears.","MFE_90D_pct":29.63,"MAE_90D_pct":-14.91,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L26-C23-000100-RYBREVANT-SC-CRL","trigger_id":"R7L26-T005","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":45,"customer_quality_score":85,"policy_or_regulatory_score":35,"valuation_repricing_score":55,"execution_risk_score":55,"legal_or_contract_risk_score":65,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62.0,"stage_label_before":"4B-Watch","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":45,"customer_quality_score":85,"policy_or_regulatory_score":35,"valuation_repricing_score":55,"execution_risk_score":55,"legal_or_contract_risk_score":65,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64.0,"stage_label_after":"4B-Watch","changed_components":["non_core_crl_not_hard_4c_guard"],"component_delta_explanation":"A manufacturing/inspection CRL for a delivery format is not the same as a core efficacy/safety rejection.","MFE_90D_pct":24.73,"MAE_90D_pct":-10.99,"score_return_alignment_label":"watch_only_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L26-C23-028300-CORE-APPROVAL-FAILURE","trigger_id":"R7L26-T006","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":20,"relative_strength_score":95,"customer_quality_score":35,"policy_or_regulatory_score":45,"valuation_repricing_score":90,"execution_risk_score":90,"legal_or_contract_risk_score":80,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":86.0,"stage_label_before":"Blocked-Green","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":20,"relative_strength_score":95,"customer_quality_score":35,"policy_or_regulatory_score":45,"valuation_repricing_score":90,"execution_risk_score":90,"legal_or_contract_risk_score":80,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":58.0,"stage_label_after":"4C-Watch","changed_components":["core_approval_absence_guard","hard_4c_thesis_break"],"component_delta_explanation":"Price/expectation alone would have been dangerous; absent final approval evidence and a later core CRL support hard 4C routing.","MFE_90D_pct":6.79,"MAE_90D_pct":-62.62,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_approval_to_commercialization_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,+1,+1,"Approval with partner launch/royalty or US commercial channel visibility can promote Stage2/Yellow before full consensus revision.","Improved capture of 77.55% and 60.99% 180D MFE cases without allowing price-only HLB.",R7L26-T001|R7L26-T003,4,4,2,medium,canonical_shadow_only,"not production; use only with non-price approval evidence"
shadow_weight,c23_non_core_crl_not_4c_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,+1,+1,"Delivery-format/manufacturing CRL that leaves approved IV/formulation intact is 4B/watch, not hard 4C.","Avoids overreacting to R7L26-T005 where 90D MFE remained +24.73%.",R7L26-T005,4,4,2,medium,canonical_shadow_only,"qualifies hard_4c axis"
shadow_weight,c23_core_approval_absence_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,+1,+1,"If final approval evidence is absent, price/expectation strength cannot become Green.","Blocks R7L26-T006 false Green with -62.62% 90D MAE.",R7L26-T006|R7L26-T007,4,4,2,high,canonical_shadow_only,"strengthens price-only blowoff guard"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"26","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":0,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["C23_approval_success_missed_when_revision_lags","C23_non_core_CRL_should_not_route_to_hard_4C"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R7L26-C23-068270-ZYMFENTRA-US-APPROVAL","symbol":"068270","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","reason":"Celltrion Zymfentra approval path was considered but excluded from quantitative calibration because the 2023-10-22 approval window overlaps a 2024-01-12 corporate-action candidate in the stock-web profile.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
- For this MD specifically, parse C23 CRLs into `core_thesis_break` versus `non_core_delivery_or_manufacturing_delay`.

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
11. Add a C23-specific test that non-core delivery/manufacturing CRL does not automatically route to hard 4C.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
next_round = R7 / C24_BIO_TRIAL_DATA_EVENT_RISK
reason = after C23 approval-commercialization, the adjacent gap is trial-data event risk and failed/ambiguous data interpretation.
```

## 28. Source Notes

- Stock-web manifest and price rows are the quantitative source of truth for OHLC metrics. fileciteturn561file0
- 000100, 145020, and 028300 profile and shard citations are embedded in sections 4 and 10.
- Web evidence is used only to timestamp and classify event families, not to compute prices. Reuters supports the Lazertinib/Rybrevant approval and Rybrevant subcutaneous CRL event classifications. citeturn521049news1turn521049news0
- Letybo launch/approval context is supported by consumer/medical-aesthetic coverage that identifies Letybo as FDA-approved and manufactured by Hugel. citeturn582758news0turn582758news1
- HLB CRL text source quality is flagged as limited; a later source-enrichment pass should attach a primary disclosure or partner release before promotion.
