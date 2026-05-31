# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R7
scheduled_loop: 12
completed_round: R7
completed_loop: 12
next_round: R8
next_loop: 12
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: CLINICAL_READOUT_INTERPRETATION_TO_PARTNER_BRIDGE_OR_THESIS_BREAK
output_file: e2r_stock_web_v12_residual_round_R7_loop_12_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
stock_web_price_atlas_access_required: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 3 new independent cases, 2 counterexamples, and 4 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C24_BIO_TRIAL_DATA_EVENT_RISK.

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`.

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This MD does not re-prove those global axes. It tests a C24-specific residual: clinical trial data is not a single type of evidence. The same “data event” can be a high-MAE success, a delayed partner/royalty bridge, or a hard thesis break. The scoring layer therefore needs a clinical-readout grammar, not a simple event-date boost.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R7 |
| scheduled_loop | 12 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK |
| fine_archetype_id | CLINICAL_READOUT_INTERPRETATION_TO_PARTNER_BRIDGE_OR_THESIS_BREAK |
| loop_objective | coverage_gap_fill; counterexample_mining; residual_false_positive_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression |

R7 maps directly to `L7_BIO_HEALTHCARE_MEDICAL`; round-sector consistency passes. C24 was selected because local R7 v12 coverage already had C25 medical-device and C23 approval/commercialization files, while the clinical-data/readout risk layer remained under-covered.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 state shows R6 loop12 was completed immediately before this run, so the next valid state is R7 loop12. Existing R7 loop10 covered C25 and loop11 covered C23. This MD avoids those by selecting C24 and by using new clinical-data trigger families.

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided for new independent cases
new_independent_case_count = 3
reused_case_count = 1
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 4
new_trigger_family_count = 4
minimum_new_independent_case_ratio = 3 / 4 = 0.75
```

The reused HLB row is explicitly label-comparison only. It is not counted as new independent evidence because the same symbol/date was already used in R7 loop11 under C23.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX|KOSDAQ|KOSDAQ GLOBAL|KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The stock-web manifest max date is `2026-02-20`, so all forward-window checks stop there. The price basis is `tradable_raw`; rows are raw/unadjusted OHLC, not split-adjusted prices. Corporate-action candidate windows are blocked for calibration.

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | 180D forward window | corporate-action status | calibration_usable |
|---|---:|---|---|---|---|
| R7L12-C24-000100-YUHAN-MARIPOSA-READOUT-HIGHMAE-SUCCESS | 000100 | atlas/symbol_profiles/000/000100.json | available | 2020-04-08 outside window | true |
| R7L12-C24-039200-OSCOTEC-MARIPOSA-READOUT-RERATING | 039200 | atlas/symbol_profiles/039/039200.json | available | 2022-11-30 outside window | true |
| R7L12-C24-019170-SHINPOONG-PYRAMAX-DATA-FAILURE | 019170 | atlas/symbol_profiles/019/019170.json | available | historical candidates outside window | true |
| R7L12-C24-028300-HLB-BINARY-READOUT-REGULATORY-REUSE | 028300 | atlas/symbol_profiles/028/028300.json | available | historical candidates outside window | true but reused label-comparison only |
| R7L12-C24-084990-HELIXMITH-VM202-DPN-BLOCKED | 084990 | atlas/symbol_profiles/084/084990.json | available | 2020-05-15 overlaps post-readout 180D window | narrative_only |

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype compression:
  MARIPOSA_READOUT_HIGH_MAE_SUCCESS -> C24
  CLINICAL_READOUT_ROYALTY_PARTNER_BRIDGE -> C24
  COVID_TREATMENT_BINARY_ENDPOINT_FAILURE -> C24
  PRE_EVENT_PRICE_ONLY_BINARY_SPECULATION -> C24 guardrail only
```

C24 should not be split by disease area. The reusable axis is the evidence bridge: endpoint quality, data interpretability, partner/commercial bridge, and thesis-break severity.

## 7. Case Selection Summary

| case_id | symbol | company | case_type | role | new_independent_case | current_profile_verdict |
|---|---:|---|---|---|---|---|
| R7L12-C24-000100-YUHAN-MARIPOSA-READOUT-HIGHMAE-SUCCESS | 000100 | 유한양행 | high_mae_success | positive | True | current_profile_too_early |
| R7L12-C24-039200-OSCOTEC-MARIPOSA-READOUT-RERATING | 039200 | 오스코텍 | high_mae_success | positive | True | current_profile_missed_structural |
| R7L12-C24-019170-SHINPOONG-PYRAMAX-DATA-FAILURE | 019170 | 신풍제약 | false_positive_green | counterexample | True | current_profile_false_positive |
| R7L12-C24-028300-HLB-BINARY-READOUT-REGULATORY-REUSE | 028300 | HLB | false_positive_green | counterexample | False | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
calibration_usable_case_count = 4
representative_trigger_count = 3
new_independent_case_count = 3
reused_case_count = 1
4B_case_count = 2
4C_case_count = 2
```

The positive side is not clean low-MAE momentum: Yuhan and Oscotec both initially suffered drawdown after the readout. The difference is that their clinical data later acquired a partner/approval/royalty bridge. The counterexample side shows the other path: if endpoint confirmation is absent or broken, relative strength becomes a trapdoor.

## 9. Evidence Source Map

| symbol | trigger family | evidence_date | stage2 evidence | stage3 evidence | 4B / 4C evidence |
|---:|---|---|---|---|---|
| 000100 | MARIPOSA data readout | 2023-10-23 | public_event_or_disclosure; customer_or_order_quality; early_revision_signal | multiple_public_sources; durable_customer_confirmation | none at entry |
| 039200 | MARIPOSA data / royalty read-through | 2023-10-23 | public_event_or_disclosure; customer_or_order_quality; early_revision_signal | financial_visibility after bridge | 4B overlay after vertical rerating |
| 019170 | pre-readout COVID treatment speculation | 2021-06-25 | public_event_or_disclosure; relative_strength | none | positioning_overheat; thesis_evidence_broken |
| 028300 | reused binary event comparison | 2024-05-16 | public_event_or_disclosure; relative_strength | none | explicit_event_cap; regulatory_rejection; thesis_evidence_broken |

## 10. Price Data Source Map

| symbol | company | price_shard_path used | profile_path | manifest max date |
|---:|---|---|---|---|
| 000100 | 유한양행 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2023.csv; 2024.csv | atlas/symbol_profiles/000/000100.json | 2026-02-20 |
| 039200 | 오스코텍 | atlas/ohlcv_tradable_by_symbol_year/039/039200/2023.csv; 2024.csv | atlas/symbol_profiles/039/039200.json | 2026-02-20 |
| 019170 | 신풍제약 | atlas/ohlcv_tradable_by_symbol_year/019/019170/2021.csv; 2022.csv | atlas/symbol_profiles/019/019170.json | 2026-02-20 |
| 028300 | HLB | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json | 2026-02-20 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | current_profile_verdict | aggregate? |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| R7L12-C24-000100-T1-MARIPOSA-STAGE2A-20231023 | 000100 | Stage2-Actionable | 2023-10-23 | 2023-10-23 | 62000 | 3.55 | 15.48 | 59.03 | -11.45 | -11.45 | -11.45 | 2024-07-15 | 98600 | current_profile_too_early | True |
| R7L12-C24-039200-T1-MARIPOSA-STAGE2A-20231023 | 039200 | Stage2-Actionable | 2023-10-23 | 2023-10-23 | 21850 | 2.06 | 13.04 | 104.12 | -16.25 | -17.62 | -17.62 | 2024-07-15 | 44600 | current_profile_missed_structural | True |
| R7L12-C24-039200-T2-4B-TRIAL-DATA-RERATING-20240716 | 039200 | Stage4B | 2024-07-16 | 2024-07-16 | 43400 | 3.46 | 3.46 | 25.12 | -10.02 | -24.08 | -24.08 | 2026-02-20 | 54300 | current_profile_4B_too_late | False |
| R7L12-C24-019170-T1-PRE-READOUT-FALSE-STAGE2-20210625 | 019170 | Stage2-FalsePositive | 2021-06-25 | 2021-06-25 | 91300 | 11.17 | 11.17 | 11.17 | -32.86 | -46.28 | -74.97 | 2021-07-05 | 101500 | current_profile_false_positive | True |
| R7L12-C24-019170-T2-HARD-4C-DATA-FAILURE-20210706 | 019170 | Stage4C | 2021-07-06 | 2021-07-06 | 67000 | 16.87 | 17.91 | 17.91 | -8.51 | -26.79 | -65.9 | 2021-08-30 | 79000 | current_profile_4C_too_late | False |
| R7L12-C24-028300-T1-PRE-EVENT-FALSE-GREEN-20240516 | 028300 | Stage3-Green-candidate-false-positive | 2024-05-16 | 2024-05-16 | 95800 | 11.59 | 11.59 | 11.59 | -52.87 | -52.87 | -52.87 | 2024-05-16 | 106900 | current_profile_false_positive | False |

## 12. Trigger-Level OHLC Backtest Tables

### Representative aggregate rows

| trigger_id | entry | max high basis | min low basis | interpretation |
|---|---:|---|---|---|
| R7L12-C24-000100-T1-MARIPOSA-STAGE2A-20231023 | 62,000 | 64,200 / 71,600 / 98,600 | 54,900 / 54,900 / 54,900 | positive but early high-MAE; data alone is not clean Green |
| R7L12-C24-039200-T1-MARIPOSA-STAGE2A-20231023 | 21,850 | 22,300 / 24,700 / 44,600 | 18,300 / 18,000 / 18,000 | delayed structural success; requires bridge and 4B later |
| R7L12-C24-019170-T1-PRE-READOUT-FALSE-STAGE2-20210625 | 91,300 | 101,500 / 101,500 / 101,500 | 61,300 / 49,050 / 22,850 | binary event false positive; endpoint unknown should cap stage |

### Overlay-only rows

| trigger_id | role | why not aggregate |
|---|---|---|
| R7L12-C24-039200-T2-4B-TRIAL-DATA-RERATING-20240716 | 4B overlay | same Oscotec case; tests overheat after >100% rerating |
| R7L12-C24-019170-T2-HARD-4C-DATA-FAILURE-20210706 | 4C overlay | same Shinpoong case; tests thesis-break routing |
| R7L12-C24-028300-T1-PRE-EVENT-FALSE-GREEN-20240516 | label comparison only | reused from R7 loop11 C23; not new independent evidence |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely behavior | actual MFE/MAE alignment | verdict |
|---|---|---|---|
| Yuhan MARIPOSA | may promote too early if data headline and partner quality are scored before post-readout MAE | MFE_180 +59.03%, but MAE_30 -11.45% | current_profile_too_early |
| Oscotec MARIPOSA | may miss structural bridge if early drawdown suppresses score | MFE_180 +104.12%, MAE_90 -17.62% | current_profile_missed_structural |
| Shinpoong pre-readout | may overpromote relative strength / COVID optionality | MFE_90 +11.17%, MAE_180 -74.97% | current_profile_false_positive |
| HLB reused binary event | may overpromote price strength before actual decision evidence | MFE_90 +11.59%, MAE_90 -52.87% | current_profile_false_positive |

Answers to required stress-test questions:

```text
1. current calibrated profile can separate some 4C breaks, but pre-readout Green/Yellows remain risky.
2. actual MFE/MAE says positive readouts can still carry high early MAE; false readouts produce catastrophic MAE.
3. Stage2 bonus is useful only after clinical endpoint evidence exists or after bridge evidence appears.
4. Yellow 75 is acceptable if endpoint quality is present; too loose if price momentum is the main input.
5. Green 87 / revision 55 is too early for Yuhan-like noisy readout, too late for Oscotec after bridge confirmation.
6. price-only blowoff guard remains appropriate.
7. full 4B non-price requirement is strengthened: Oscotec 4B needs valuation/positioning evidence, not only local peak.
8. hard 4C routing should be earlier in endpoint failure cases.
```

## 14. Stage2 / Yellow / Green Comparison

For C24, Green lateness cannot be calculated the same way as ordinary EPS-revision cases because the Green event is often an approval/commercialization bridge that belongs to C23. Therefore:

```text
Yuhan green_lateness_ratio = not_applicable:no_C24_Green_before_C23_approval_bridge
Oscotec green_lateness_ratio = not_applicable:no_C24_Green_before_partner_bridge
Shinpoong green_lateness_ratio = not_applicable:false_positive_before_data
```

Interpretation: C24 should generally allow Stage2/Actionable when a clinical event is real, but it should withhold clean Green unless endpoint quality plus interpretation bridge is explicit.

## 15. 4B Local vs Full-window Timing Audit

| case | stage2 entry | 4B entry | local peak | full-window peak | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| Oscotec | 21,850 | 43,400 | 44,900 | 44,900 inside 180D | 0.935 | 0.935 | good local/full 4B if valuation/positioning evidence confirms |
| Shinpoong | 91,300 | price peak 101,500 | 101,500 | 101,500 | 1.000 | 1.000 | price-only 4B is too late; endpoint guard should have capped pre-readout stage |
| HLB reused | 95,800 | 95,800 | 106,900 | 106,900 | n/a | n/a | pre-event price-only overheat is not full 4B; it is a binary-event guard |

## 16. 4C Protection Audit

| case | 4C date | 4C entry | max drawdown after prior stage | 4C label |
|---|---|---:|---:|---|
| Shinpoong | 2021-07-06 | 67,000 | -74.97% from pre-readout entry to 180D low | hard_4c_success_after_thesis_break |
| HLB reused | 2024-05-17 | 67,100 | -57.76% from pre-event peak | hard_4c_success |
| Helixmith narrative-only | 2019/2020 VM202 path | blocked | corporate-action contaminated 180D window | narrative_only_not_weight_calibration |

The C24 rule is simple: failed endpoint or regulatory/data thesis break routes to 4C even if the prior price trend was strong.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = R7 has heterogeneous bio/healthcare subsegments; this file supports a canonical C24 rule, not a broad R7 sector rule.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
```

Candidate C24 shadow rules:

```text
C24_endpoint_quality_gate:
  clinical endpoint must be explicit before Stage3 promotion.

C24_interpretation_bridge:
  data readout with high initial MAE remains Stage2/Yellow until partner, label, royalty, or approval bridge appears.

C24_binary_event_green_block:
  pre-readout / pre-decision price strength cannot become Green without actual data/approval evidence.

C24_failed_endpoint_4C_route:
  weak/failed endpoint routes to 4C even if prior relative strength was strong.

C24_post_success_4B_overlay:
  after >100% rerating, valuation/positioning evidence can create 4B overlay without invalidating the original Stage2 thesis.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global_current | 4 | 13.82 | -31.56 | 40.47 | -41.98 | 0.5 | 1 | 1 | mixed_alignment |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 13.82 | -31.56 | 40.47 | -41.98 | 0.75 | 1 | 1 | overpromotes_binary_events |
| P1_R7_sector_clinical_readout_guard | sector_specific | 4 | 10.9 | -21.78 | 61.03 | -35.65 | 0.25 | 0 | 1 | improved_alignment |
| P2_C24_trial_data_event_profile | canonical_archetype_specific | 4 | 10.9 | -21.78 | 61.03 | -35.65 | 0.0 | 0 | 1 | best_alignment |
| P3_C24_counterexample_guard_profile | canonical_archetype_specific | 4 | 8.3 | -17.62 | 54.01 | -29.44 | 0.0 | 1 | 1 | strict_but_may_delay_real_successes |

## 20. Score-Return Alignment Matrix

| case | P0 label | P2 C24 label | actual path | alignment |
|---|---|---|---|---|
| Yuhan | Stage2/Yellow too fast | Stage2-Actionable watch | initial -11.45% MAE then +59.03% 180D MFE | improved by high-MAE guard |
| Oscotec | Stage2-watch / missed structural | Stage3-Yellow after bridge | +104.12% MFE_180 after early -17.62% MAE | improved by bridge recognition |
| Shinpoong | Stage3 candidate on momentum | Stage4C watch before readout | -74.97% MAE_180 | false positive blocked |
| HLB reused | Green candidate risk | C24 binary guard comparison | -52.87% MAE_90 | not new evidence but consistent guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | CLINICAL_READOUT_INTERPRETATION_TO_PARTNER_BRIDGE_OR_THESIS_BREAK | 2 | 2 | 2 | 2 | 3 | 1 | 6 | 3 | 4 | false | true | reduced: C24 now has positive, counterexample, 4B, 4C rows |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 1
reused_case_ids: R7L12-C24-028300-HLB-BINARY-READOUT-REGULATORY-REUSE
new_symbol_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: current_profile_too_early, current_profile_missed_structural, current_profile_false_positive, current_profile_4C_too_late
new_axis_proposed: C24_endpoint_quality_gate, C24_interpretation_bridge, C24_binary_event_green_block, C24_failed_endpoint_4C_route, C24_post_success_4B_overlay
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema fields
- symbol profile availability and corporate-action candidate dates
- 1D OHLC entry rows and forward high/low windows from tradable_raw shards
- Stage2/Stage3/4B/4C evidence separation
- same_entry_group_id dedupe and reused-case non-counting
```

Not validated:

```text
- no live stock scan
- no current recommendation
- no stock_agent source-code inspection
- no production scoring change
- no broker/API automation
- no adjusted-price reconstruction
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C24_trial_data_requires_endpoint_plus_interpretation_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,"+1 guard","Trial readout headline alone had high MAE in Yuhan/Oscotec before partner/approval interpretation matured.","Blocks premature Green and keeps Stage2/Yellow until endpoint + bridge evidence coexist.","R7L12-C24-000100-T1-MARIPOSA-STAGE2A-20231023|R7L12-C24-039200-T1-MARIPOSA-STAGE2A-20231023",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C24_binary_event_unknown_endpoint_green_block,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,"+1 guard","Shinpoong and reused HLB show price strength before binary data/regulatory event can become false Green.","Reduces false-positive rate by requiring readout/approval evidence before Stage3 promotion.","R7L12-C24-019170-T1-PRE-READOUT-FALSE-STAGE2-20210625|R7L12-C24-028300-T1-PRE-EVENT-FALSE-GREEN-20240516",3,3,2,medium,canonical_shadow_only,"HLB reused only as label-comparison evidence"
shadow_weight,C24_failed_endpoint_routes_to_hard_4C,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,"+1 guard","Failed/weak endpoint should route to 4C even if prior relative strength was strong.","Improves drawdown protection after Shinpoong-like readout failure.",R7L12-C24-019170-T2-HARD-4C-DATA-FAILURE-20210706,3,3,1,medium,canonical_shadow_only,"strengthens hard_4c_thesis_break_routes_to_4c inside C24"
shadow_weight,C24_4B_after_clinical_rerating_vertical,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,"+1 overlay","Oscotec shows >100% post-readout rerating can require a 4B overlay once valuation/positioning outrun data confirmation.","Separates positive Stage2/Yellow from later 4B risk overlay.",R7L12-C24-039200-T2-4B-TRIAL-DATA-RERATING-20240716,3,3,1,low,canonical_shadow_only,"4B overlay only; not a positive promotion rule"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R7L12-C24-000100-YUHAN-MARIPOSA-READOUT-HIGHMAE-SUCCESS","symbol":"000100","company_name":"유한양행","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R7L12-C24-000100-T1-MARIPOSA-STAGE2A-20231023","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"delayed_positive_alignment_after_initial_data_selloff","current_profile_verdict":"current_profile_too_early","notes":"MARIPOSA readout was ultimately valuable, but the immediate post-data path had deep MAE before the partner/approval bridge became clear; C24 should not promote data alone to clean Green.","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_READOUT_INTERPRETATION_TO_PARTNER_BRIDGE_OR_THESIS_BREAK","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R7L12-C24-039200-OSCOTEC-MARIPOSA-READOUT-RERATING","symbol":"039200","company_name":"오스코텍","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R7L12-C24-039200-T1-MARIPOSA-STAGE2A-20231023","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment_with_large_lag_and_4b_overlay","current_profile_verdict":"current_profile_missed_structural","notes":"Same readout family as Yuhan but with more convex later rerating; the difference is not data headline alone but licensing/royalty read-through and later confirmation.","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_READOUT_INTERPRETATION_TO_PARTNER_BRIDGE_OR_THESIS_BREAK","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R7L12-C24-019170-SHINPOONG-PYRAMAX-DATA-FAILURE","symbol":"019170","company_name":"신풍제약","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R7L12-C24-019170-T1-PRE-READOUT-FALSE-STAGE2-20210625","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_blocked_after","current_profile_verdict":"current_profile_false_positive","notes":"Pre-readout COVID treatment enthusiasm produced a tradable spike, but the failed/weak endpoint path turned into a long drawdown; binary clinical event risk must cap Stage2/Green before readout.","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_READOUT_INTERPRETATION_TO_PARTNER_BRIDGE_OR_THESIS_BREAK","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R7L12-C24-028300-HLB-BINARY-READOUT-REGULATORY-REUSE","symbol":"028300","company_name":"HLB","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R7L12-C24-028300-T1-PRE-EVENT-FALSE-GREEN-20240516","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"Reuses R7 loop11 HLB CRL row as C24 label-comparison only; same symbol/trigger is not counted as new independent evidence.","independent_evidence_weight":0.25,"score_price_alignment":"false_positive_blocked_after","current_profile_verdict":"current_profile_false_positive","notes":"Included only to show that a binary clinical/regulatory event countdown should be guarded in C24 as well; not counted as a new case.","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_READOUT_INTERPRETATION_TO_PARTNER_BRIDGE_OR_THESIS_BREAK","price_source":"Songdaiki/stock-web"}
{"row_type":"trigger","trigger_id":"R7L12-C24-000100-T1-MARIPOSA-STAGE2A-20231023","case_id":"R7L12-C24-000100-YUHAN-MARIPOSA-READOUT-HIGHMAE-SUCCESS","symbol":"000100","company_name":"유한양행","sector":"bio_pharma","primary_archetype":"clinical readout with partner/approval bridge after initial interpretation shock","loop_objective":"coverage_gap_fill|green_strictness_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-10-23","entry_date":"2023-10-23","entry_price":62000,"evidence_available_at_that_date":"MARIPOSA/lazertinib-amivantamab clinical data readout was public around ESMO 2023; early market interpretation was noisy because efficacy, toxicity, and commercialization read-through were not yet cleanly digested.","evidence_source":"public MARIPOSA readout / subsequent FDA approval context; stock-web 000100 rows 2023-10-23 onward","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":3.55,"MFE_90D_pct":15.48,"MFE_180D_pct":59.03,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.45,"MAE_90D_pct":-11.45,"MAE_180D_pct":-11.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-15","peak_price":98600,"drawdown_after_peak_pct":-4.16,"green_lateness_ratio":"not_applicable:no_C24_Green_before_C23_approval_bridge","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L12-C24-000100-20231023-62000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2023.csv; atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_READOUT_INTERPRETATION_TO_PARTNER_BRIDGE_OR_THESIS_BREAK","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"row_type":"trigger","trigger_id":"R7L12-C24-039200-T1-MARIPOSA-STAGE2A-20231023","case_id":"R7L12-C24-039200-OSCOTEC-MARIPOSA-READOUT-RERATING","symbol":"039200","company_name":"오스코텍","sector":"bio_pharma","primary_archetype":"clinical data readout royalty/partner read-through","loop_objective":"coverage_gap_fill|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-10-23","entry_date":"2023-10-23","entry_price":21850,"evidence_available_at_that_date":"MARIPOSA data readout exposed the royalty/partner read-through but also immediate interpretation risk; subsequent rerating required confirmation rather than headline-only scoring.","evidence_source":"public MARIPOSA readout / stock-web 039200 rows 2023-10-23 onward","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["durable_customer_confirmation","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":2.06,"MFE_90D_pct":13.04,"MFE_180D_pct":104.12,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.25,"MAE_90D_pct":-17.62,"MAE_180D_pct":-17.62,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-15","peak_price":44600,"drawdown_after_peak_pct":-7.17,"green_lateness_ratio":"not_applicable:no_C24_Green_before_partner_bridge","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"delayed_structural_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L12-C24-039200-20231023-21850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039200/2023.csv; atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv","profile_path":"atlas/symbol_profiles/039/039200.json","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_READOUT_INTERPRETATION_TO_PARTNER_BRIDGE_OR_THESIS_BREAK","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"row_type":"trigger","trigger_id":"R7L12-C24-039200-T2-4B-TRIAL-DATA-RERATING-20240716","case_id":"R7L12-C24-039200-OSCOTEC-MARIPOSA-READOUT-RERATING","symbol":"039200","company_name":"오스코텍","sector":"bio_pharma","primary_archetype":"clinical data rerating 4B overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-07-16","entry_date":"2024-07-16","entry_price":43400,"evidence_available_at_that_date":"After a >100% move from C24 readout entry, valuation/positioning risk became the relevant overlay; this row is 4B-only and is not a new positive signal.","evidence_source":"stock-web 039200 2024-07-16 c=43,400 and 2024-07-16 high=44,900","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"MFE_30D_pct":3.46,"MFE_90D_pct":3.46,"MFE_180D_pct":25.12,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.02,"MAE_90D_pct":-24.08,"MAE_180D_pct":-24.08,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2026-02-20","peak_price":54300,"drawdown_after_peak_pct":null,"green_lateness_ratio":"not_applicable:4B_overlay","four_b_local_peak_proximity":0.935,"four_b_full_window_peak_proximity":0.935,"four_b_timing_verdict":"good_local_4B_but_requires_non_price_overheat_confirmation","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L12-C24-039200-20240716-43400","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same Oscotec case used for 4B overlay timing; not aggregate entry","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv; atlas/ohlcv_tradable_by_symbol_year/039/039200/2025.csv; atlas/ohlcv_tradable_by_symbol_year/039/039200/2026.csv","profile_path":"atlas/symbol_profiles/039/039200.json","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_READOUT_INTERPRETATION_TO_PARTNER_BRIDGE_OR_THESIS_BREAK","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"row_type":"trigger","trigger_id":"R7L12-C24-019170-T1-PRE-READOUT-FALSE-STAGE2-20210625","case_id":"R7L12-C24-019170-SHINPOONG-PYRAMAX-DATA-FAILURE","symbol":"019170","company_name":"신풍제약","sector":"pharma_covid_treatment","primary_archetype":"binary clinical readout speculation without endpoint confirmation","loop_objective":"counterexample_mining|residual_false_positive_mining|4C_thesis_break_timing_test","trigger_type":"Stage2-FalsePositive","trigger_date":"2021-06-25","entry_date":"2021-06-25","entry_price":91300,"evidence_available_at_that_date":"Pre-readout price strength and COVID treatment narrative existed, but confirmed clinical endpoint evidence was absent; this should be capped before data.","evidence_source":"stock-web 019170 2021-06-25 c=91,300; weak/failed endpoint event reflected by 2021-07-06 shock row","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken"],"MFE_30D_pct":11.17,"MFE_90D_pct":11.17,"MFE_180D_pct":11.17,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-32.86,"MAE_90D_pct":-46.28,"MAE_180D_pct":-74.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-05","peak_price":101500,"drawdown_after_peak_pct":-77.49,"green_lateness_ratio":"not_applicable:false_positive_before_data","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_late_without_readout_guard","four_b_evidence_type":["price_only","positioning_overheat","explicit_event_cap"],"four_c_protection_label":"hard_4c_late_if_waiting_for_price_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L12-C24-019170-20210625-91300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/019/019170/2021.csv; atlas/ohlcv_tradable_by_symbol_year/019/019170/2022.csv","profile_path":"atlas/symbol_profiles/019/019170.json","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_READOUT_INTERPRETATION_TO_PARTNER_BRIDGE_OR_THESIS_BREAK","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"row_type":"trigger","trigger_id":"R7L12-C24-019170-T2-HARD-4C-DATA-FAILURE-20210706","case_id":"R7L12-C24-019170-SHINPOONG-PYRAMAX-DATA-FAILURE","symbol":"019170","company_name":"신풍제약","sector":"pharma_covid_treatment","primary_archetype":"failed endpoint 4C protection","loop_objective":"4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2021-07-06","entry_date":"2021-07-06","entry_price":67000,"evidence_available_at_that_date":"Weak/failed clinical endpoint broke the pre-readout thesis; from here the correct action is thesis-break routing, not averaging down on previous relative strength.","evidence_source":"stock-web 019170 2021-07-06 c=67,000 after 2021-07-05 event spike","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken","safety_or_trial_failure"],"MFE_30D_pct":16.87,"MFE_90D_pct":17.91,"MFE_180D_pct":17.91,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.51,"MAE_90D_pct":-26.79,"MAE_180D_pct":-65.9,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-08-30","peak_price":79000,"drawdown_after_peak_pct":-71.08,"green_lateness_ratio":"not_applicable:4C_overlay","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success_after_thesis_break","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L12-C24-019170-20210706-67000","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same Shinpoong case 4C protection audit; not aggregate entry","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/019/019170/2021.csv; atlas/ohlcv_tradable_by_symbol_year/019/019170/2022.csv","profile_path":"atlas/symbol_profiles/019/019170.json","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_READOUT_INTERPRETATION_TO_PARTNER_BRIDGE_OR_THESIS_BREAK","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"row_type":"trigger","trigger_id":"R7L12-C24-028300-T1-PRE-EVENT-FALSE-GREEN-20240516","case_id":"R7L12-C24-028300-HLB-BINARY-READOUT-REGULATORY-REUSE","symbol":"028300","company_name":"HLB","sector":"bio_pharma","primary_archetype":"binary clinical/regulatory event countdown without approval evidence","loop_objective":"counterexample_mining|4C_thesis_break_timing_test|holdout_validation","trigger_type":"Stage3-Green-candidate-false-positive","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":95800,"evidence_available_at_that_date":"Pre-event anticipation and price strength existed, but endpoint/regulatory confirmation was absent; this row was already used in C23 and is included here only as a C24 guardrail comparison.","evidence_source":"local R7 loop11 stock-web computed row; stock-web 028300 2024-05-16 c=95,800 and 2024-05-17 c=67,100","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","positioning_overheat"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"MFE_30D_pct":11.59,"MFE_90D_pct":11.59,"MFE_180D_pct":11.59,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-52.87,"MAE_90D_pct":-52.87,"MAE_180D_pct":-52.87,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":106900,"drawdown_after_peak_pct":-57.76,"green_lateness_ratio":"not_applicable:reused_false_positive","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"pre_event_price_only_not_full_4B","four_b_evidence_type":["price_only","explicit_event_cap"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L12-C24-028300-20240516-95800","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"reused_symbol_and_trigger_from_R7_loop11_C23; not counted as new case","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_READOUT_INTERPRETATION_TO_PARTNER_BRIDGE_OR_THESIS_BREAK","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L12-C24-000100-YUHAN-MARIPOSA-READOUT-HIGHMAE-SUCCESS","trigger_id":"R7L12-C24-000100-T1-MARIPOSA-STAGE2A-20231023","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":8,"relative_strength_score":4,"customer_quality_score":12,"policy_or_regulatory_score":6,"valuation_repricing_score":4,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_endpoint_score":12,"trial_data_quality_score":12,"partner_bridge_score":8,"binary_event_risk_score":-10,"commercialization_bridge_score":4,"thesis_break_score":0,"positioning_overheat_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":7,"relative_strength_score":4,"customer_quality_score":12,"policy_or_regulatory_score":6,"valuation_repricing_score":4,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_endpoint_score":12,"trial_data_quality_score":13,"partner_bridge_score":8,"binary_event_risk_score":-14,"commercialization_bridge_score":5,"thesis_break_score":0,"positioning_overheat_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Actionable_watch","changed_components":["binary_event_risk_score","execution_risk_score"],"component_delta_explanation":"C24 shadow keeps Stage2 but blocks premature Green because immediate high-MAE data interpretation risk was visible.","MFE_90D_pct":15.48,"MAE_90D_pct":-11.45,"score_return_alignment_label":"partial_alignment_after_high_MAE_guard","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L12-C24-039200-OSCOTEC-MARIPOSA-READOUT-RERATING","trigger_id":"R7L12-C24-039200-T1-MARIPOSA-STAGE2A-20231023","symbol":"039200","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":6,"relative_strength_score":3,"customer_quality_score":10,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_endpoint_score":11,"trial_data_quality_score":12,"partner_bridge_score":7,"binary_event_risk_score":-10,"commercialization_bridge_score":3,"thesis_break_score":0,"positioning_overheat_score":0},"weighted_score_before":68,"stage_label_before":"Stage2-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":8,"relative_strength_score":8,"customer_quality_score":12,"policy_or_regulatory_score":7,"valuation_repricing_score":8,"execution_risk_score":-9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_endpoint_score":13,"trial_data_quality_score":14,"partner_bridge_score":12,"binary_event_risk_score":-10,"commercialization_bridge_score":6,"thesis_break_score":0,"positioning_overheat_score":0},"weighted_score_after":79,"stage_label_after":"Stage3-Yellow_after_bridge","changed_components":["partner_bridge_score","trial_data_quality_score","relative_strength_score"],"component_delta_explanation":"The data headline alone was noisy, but later partner/royalty read-through justified Yellow; this is missed structural if C24 ignores confirmation bridge.","MFE_90D_pct":13.04,"MAE_90D_pct":-17.62,"score_return_alignment_label":"positive_alignment_after_confirmation_bridge","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L12-C24-019170-SHINPOONG-PYRAMAX-DATA-FAILURE","trigger_id":"R7L12-C24-019170-T1-PRE-READOUT-FALSE-STAGE2-20210625","symbol":"019170","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":4,"relative_strength_score":18,"customer_quality_score":2,"policy_or_regulatory_score":4,"valuation_repricing_score":10,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_endpoint_score":0,"trial_data_quality_score":0,"partner_bridge_score":0,"binary_event_risk_score":-6,"commercialization_bridge_score":0,"thesis_break_score":0,"positioning_overheat_score":16},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_or_Green_candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_endpoint_score":0,"trial_data_quality_score":0,"partner_bridge_score":0,"binary_event_risk_score":-25,"commercialization_bridge_score":0,"thesis_break_score":-22,"positioning_overheat_score":16},"weighted_score_after":41,"stage_label_after":"Stage4C_watch_before_data","changed_components":["binary_event_risk_score","clinical_endpoint_score","thesis_break_score"],"component_delta_explanation":"C24 guard blocks price-only/relative-strength pre-readout promotion because endpoint evidence is unknown.","MFE_90D_pct":11.17,"MAE_90D_pct":-46.28,"score_return_alignment_label":"false_positive_blocked_after","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L12-C24-028300-HLB-BINARY-READOUT-REGULATORY-REUSE","trigger_id":"R7L12-C24-028300-T1-PRE-EVENT-FALSE-GREEN-20240516","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":12,"relative_strength_score":20,"customer_quality_score":8,"policy_or_regulatory_score":18,"valuation_repricing_score":16,"execution_risk_score":-8,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_endpoint_score":0,"trial_data_quality_score":0,"partner_bridge_score":0,"binary_event_risk_score":-6,"commercialization_bridge_score":0,"thesis_break_score":0,"positioning_overheat_score":18},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_or_Green_candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":20,"customer_quality_score":4,"policy_or_regulatory_score":8,"valuation_repricing_score":16,"execution_risk_score":-18,"legal_or_contract_risk_score":-20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_endpoint_score":0,"trial_data_quality_score":0,"partner_bridge_score":0,"binary_event_risk_score":-24,"commercialization_bridge_score":0,"thesis_break_score":-20,"positioning_overheat_score":18},"weighted_score_after":47,"stage_label_after":"Stage4C_watch_before_decision","changed_components":["binary_event_risk_score","legal_or_contract_risk_score","thesis_break_score"],"component_delta_explanation":"Reused HLB row shows the same binary-event guard applies to C24, but it is not new independent evidence.","MFE_90D_pct":11.59,"MAE_90D_pct":-52.87,"score_return_alignment_label":"false_positive_blocked_after","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","new_independent_case_count":3,"reused_case_count":1,"new_symbol_count":3,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_too_early","current_profile_missed_structural","current_profile_false_positive","current_profile_4C_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R7L12-C24-084990-HELIXMITH-VM202-DPN-BLOCKED","symbol":"084990","company_name":"헬릭스미스","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","reason":"VM202/DPN failure is archetypally relevant C24 4C evidence, but symbol profile has corporate_action_candidate_date 2020-05-15 inside the post-2019 readout 180D window; not used for weight calibration.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration","profile_path":"atlas/symbol_profiles/084/084990.json"}
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
completed_loop = 12
next_round = R8
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web manifest and schema were consulted for `manifest_max_date = 2026-02-20`, tradable/raw row counts, and tradable shard column semantics.
- Symbol profiles consulted: `000100`, `039200`, `019170`, `028300`, `084990`.
- Stock-web row excerpts inspected: `000100/2023.csv`, `000100/2024.csv`, `039200/2023.csv`, `039200/2024.csv`, `019170/2021.csv`, `019170/2022.csv`, and the local R7 loop11 HLB row for reused label-comparison metrics.
- Web evidence consulted for event interpretation: MARIPOSA/lazertinib-amivantamab trial and FDA approval context, plus publicly reported Helixmith/Engensis DPN trial-failure context. The HLB row is a reused guardrail row from local R7 loop11 and is not new independent evidence.
- This MD is historical calibration research only and contains no investment recommendation.

