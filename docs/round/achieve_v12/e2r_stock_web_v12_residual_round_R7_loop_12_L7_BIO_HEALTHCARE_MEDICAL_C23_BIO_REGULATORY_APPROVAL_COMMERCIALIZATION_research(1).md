# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R7_loop_12_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
scheduled_round = R7
scheduled_loop = 12
completed_round = R7
completed_loop = 12
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = APPROVAL_TO_COMMERCIALIZATION_WITH_CRL_GUARD
loop_objective = coverage_gap_fill | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4C_thesis_break_timing_test | 4B_non_price_requirement_stress_test
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds **3** new independent cases, **1** counterexample, and **3** residual errors for **R7 / L7_BIO_HEALTHCARE_MEDICAL / C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION**.

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

This MD does **not** restate that Stage2 is generally earlier than Green. The residual question is narrower: in C23, when does a regulatory approval path become investable structural evidence, and when is it merely pre-decision event beta that should be capped?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R7
scheduled_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

R7 is constrained to **L7_BIO_HEALTHCARE_MEDICAL**, so no R13 cross-archetype jump is used. The selected canonical archetype is C23 rather than C24 because the central distinction is **final approval + commercialization route** versus **approval expectation that fails at the regulatory decision point**.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifact usage was limited to registry and coverage review. Existing registry material shows prior R7 historical calibration files, but this v12 loop is treated as a new residual run with a new canonical compression map and new symbol set.

```text
previous_r7_material_observed = historical_calibration_round_R7_loop_1_to_8_generic_bio_healthcare_medtech
v12_same_filename_observed = false
same_symbol_same_trigger_reuse = false
new_symbol_count = 3
new_trigger_family_count = 4
minimum_new_independent_case_ratio = 1.00
```

Duplicate avoidance is passed because the three representative cases use new symbol + trigger-family combinations inside the scheduled R7 sector:
- 유한양행: FDA approval plus partner commercialization.
- 휴젤: FDA approval in aesthetic toxin with later commercialization/positioning 4B.
- HLB: pre-decision approval expectation followed by CRL/regulatory thesis break.

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest fields used:

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
markets = ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The atlas is raw/unadjusted OHLC from FinanceData/marcap. All quantitative rows use tradable shards, not raw shards.

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | profile last_date | corporate_action_window_status | forward_180D_available | calibration_usable |
|---|---|---|---|---|---|---|
| R7L12_C23_YUHAN_LAZCLUZE_APPROVAL | 000100 | atlas/symbol_profiles/000/000100.json | 2026-02-20 | clean_180D_window; profile has old corporate-action candidates outside window | true | true |
| R7L12_C23_HUGEL_LETYBO_APPROVAL | 145020 | atlas/symbol_profiles/145/145020.json | 2026-02-20 | clean_180D_window; profile has 2017/2020 candidates outside window | true | true |
| R7L12_C23_HLB_APPROVAL_EXPECTATION_CRL | 028300 | atlas/symbol_profiles/028/028300.json | 2026-02-20 | clean_180D_window; profile candidates end 2021, outside 2024 window | true | true |

No representative trigger is blocked for insufficient forward window or corporate-action contamination.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION

fine_archetype compression:
- EGFR_LAZERTINIB_US_FDA_APPROVAL_PARTNER_COMMERCIALIZATION -> C23
- BOTULINUM_TOXIN_US_APPROVAL_AESTHETIC_COMMERCIALIZATION -> C23
- FDA_DECISION_RISK_APPROVAL_EXPECTATION_CRL -> C23 counterexample / guard
```

Mechanism: C23 should not treat all regulatory events equally. The decisive fork is whether the evidence is **final external approval with a monetization path** or merely **pre-decision event probability**. The former is a bridge; the latter is a drawbridge that may open or collapse.

## 7. Case Selection Summary

| case_id | symbol | company | case_type | polarity | best_trigger | calibration_usable | is_new_independent_case | independent_evidence_weight |
|---|---|---|---|---|---|---|---|---:|
| R7L12_C23_YUHAN_LAZCLUZE_APPROVAL | 000100 | 유한양행 | structural_success | positive | R7L12_C23_YUHAN_STAGE2_APPROVAL_2024-08-20 | true | true | 1.0 |
| R7L12_C23_HUGEL_LETYBO_APPROVAL | 145020 | 휴젤 | structural_success | positive | R7L12_C23_HUGEL_STAGE2_APPROVAL_2024-03-04 | true | true | 1.0 |
| R7L12_C23_HLB_APPROVAL_EXPECTATION_CRL | 028300 | HLB | false_positive_green | counterexample | R7L12_C23_HLB_PRE_CRL_EXPECTATION_2024-05-14 | true | true | 1.0 |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 3
```

The balance is sufficient for a **canonical-archetype-specific** shadow rule but not for a global rule. The counterexample is essential: without HLB, the loop would only say “approval events can work,” which is too blunt for biotech.

## 9. Evidence Source Map

| case_id | trigger family | evidence timing | evidence source note |
|---|---|---|---|
| Yuhan | final FDA approval + partner commercialization | FDA approval date 2024-08-19; Korean entry 2024-08-20 close | FDA approved lazertinib with amivantamab for first-line EGFR-mutated NSCLC; FDA page lists efficacy and PFS data. |
| Hugel | final FDA approval + aesthetic commercialization | FDA approval date 2024-02-29; Korean next tradable entry 2024-03-04 close | FDA Drug Trials Snapshot lists LETYBO, Hugel, Inc., approval date 2024-02-29, and BLESS trial basis. |
| HLB | pre-decision expectation + hard CRL thesis break | representative pre-event trigger 2024-05-14; hard 4C trigger 2024-05-17 | CRL/regulatory rejection path; stock-web captures immediate gap-down and high MAE. |

## 10. Price Data Source Map

| symbol | shard(s) used | profile | entry basis |
|---|---|---|---|
| 000100 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv; 2025.csv | atlas/symbol_profiles/000/000100.json | 2024-08-20 close = 94,000 |
| 145020 | atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv | atlas/symbol_profiles/145/145020.json | 2024-03-04 close = 202,500 |
| 028300 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv; 2025.csv | atlas/symbol_profiles/028/028300.json | 2024-05-14 close = 94,600; 4C row 2024-05-17 close = 67,100 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol/company | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | current_profile_verdict | aggregate_role |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| R7L12_C23_YUHAN_STAGE2_APPROVAL_2024-08-20 | 000100 유한양행 | Stage2-Actionable | 2024-08-20 | 2024-08-20 | 94,000 | 70.53 | 77.55 | 77.55 | -2.66 | -2.66 | -2.66 | 2024-10-15 | 166,900 | current_profile_too_late | representative |
| R7L12_C23_YUHAN_STAGE3_GREEN_2024-09-24 | 000100 유한양행 | Stage3-Green | 2024-09-24 | 2024-09-24 | 157,000 | 6.31 | 6.31 | 6.31 | -12.55 | -30.57 | -36.05 | 2024-10-15 | 166,900 | current_profile_too_late | label_comparison_only |
| R7L12_C23_HUGEL_STAGE2_APPROVAL_2024-03-04 | 145020 휴젤 | Stage2-Actionable | 2024-02-29 | 2024-03-04 | 202,500 | 8.15 | 29.63 | 60.99 | -14.91 | -14.91 | -14.91 | 2024-11-07 | 326,000 | current_profile_missed_structural | representative |
| R7L12_C23_HUGEL_4B_POSITIONING_2024-11-06 | 145020 휴젤 | Stage4B | 2024-11-06 | 2024-11-06 | 321,000 | 1.56 | 1.56 | 1.56 | -26.17 | -26.17 | -26.17 | 2024-11-07 | 326,000 | current_profile_4B_too_late | 4B_overlay_only |
| R7L12_C23_HLB_PRE_CRL_EXPECTATION_2024-05-14 | 028300 HLB | Stage3-Yellow | 2024-05-14 | 2024-05-14 | 94,600 | 13.0 | 13.0 | 13.0 | -52.27 | -52.27 | -52.27 | 2024-05-16 | 106,900 | current_profile_false_positive | representative |
| R7L12_C23_HLB_4C_CRL_2024-05-17 | 028300 HLB | Stage4C | 2024-05-17 | 2024-05-17 | 67,100 | 9.99 | 46.2 | 46.2 | -32.71 | -32.71 | -32.71 | 2024-09-23 | 97,600 | current_profile_4C_too_late | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### Representative aggregate rows

| representative trigger | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | interpretation |
|---|---:|---:|---:|---:|---|
| Yuhan FDA approval | 94,000 | +70.53 / -2.66 | +77.55 / -2.66 | +77.55 / -2.66 | official approval + commercialization owner produced asymmetric upside with low early adverse excursion |
| Hugel LETYBO approval | 202,500 | +8.15 / -14.91 | +29.63 / -14.91 | +60.99 / -14.91 | approval worked, but early drawdown shows commercial launch/reorder confirmation still mattered |
| HLB pre-CRL approval expectation | 94,600 | +13.00 / -52.27 | +13.00 / -52.27 | +13.00 / -52.27 | pre-decision event beta was not enough; CRL transformed the case into hard 4C |

### Same-entry dedupe

```text
dedupe_for_aggregate = true only for representative rows.
label_comparison_only, 4B_overlay_only, and 4C_overlay_only rows are excluded from aggregate metrics.
```

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgement | actual outcome | verdict |
|---|---|---|---|
| Yuhan | Stage3 might wait for cross-source confirmation and revision visibility after approval | Stage2 approval date captured most upside; later Green caught only late part | current_profile_too_late |
| Hugel | approval-only evidence may remain Yellow until commercial/reorder visibility appears | structural positive emerged over 180D, despite initial MAE | current_profile_missed_structural |
| HLB | strong relative strength + regulatory optionality could be promoted too far before decision | CRL caused deep MAE and thesis break | current_profile_false_positive |

Answers to mandatory stress-test questions:

```text
stage2_actionable_evidence_bonus = useful for Yuhan/Hugel when final approval exists; too risky for HLB-style unapproved event beta.
yellow_threshold_75 = acceptable, but should be capped for pre-decision C23 setups without final approval.
green_threshold_87_revision_55 = too late for Yuhan if final approval plus partner commercialization is already public.
price_only_blowoff_guard = kept; HLB and Hugel show price alone cannot define positive evidence.
full_4B_non_price_requirement = strengthened; Hugel 4B needs valuation/positioning overlay.
hard_4C_routing = strengthened; CRL/regulatory rejection should route to 4C even when later rebound happens.
```

## 14. Stage2 / Yellow / Green Comparison

Yuhan is the clearest lateness audit.

```text
Stage2_Actionable_entry_price = 94,000
Stage3_Green_entry_price = 157,000
observed_peak_price_after_Stage2 = 166,900

green_lateness_ratio =
(157,000 - 94,000) / (166,900 - 94,000)
= 0.864
```

Interpretation: a generic Green threshold waits until most of the upside has already been consumed. For C23, the problem is not “make Green loose.” The better rule is narrower: **final external approval plus a named commercialization path deserves a C23-specific promotion bonus**, while pre-decision event beta remains capped.

## 15. 4B Local vs Full-window Timing Audit

| 4B trigger | Stage2 entry | 4B entry | local/full peak | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---|
| Hugel 2024-11-06 | 202,500 | 321,000 | 326,000 | 0.96 | 0.96 | good_full_window_4B_timing |

Hugel shows a clean 4B overlay: the thesis was not broken, but the price path had moved from regulatory approval to post-approval positioning/valuation.

HLB is not a 4B case. It is a hard 4C case because the regulatory thesis evidence broke.

## 16. 4C Protection Audit

HLB 4C trigger:

```text
pre_event_representative_entry = 94,600
pre_event_min_low_after_peak = 45,150
pre_event_MAE = -52.27%

4C_entry = 67,100
MAE_after_4C_90D = -32.71%

four_c_protection_score ≈ 1 - 32.71 / 52.27 = 0.374
four_c_protection_label = hard_4c_success
```

The protection score is not perfect because the gap occurred before the system could exit at the pre-event price. Still, routing to 4C is correct: a CRL is not valuation cooling; it is thesis evidence broken.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
candidate_axis = L7_regulatory_finality_before_positive_promotion
```

Rule candidate:
- In L7, regulatory event beta must be split into:
  - **final approval / label / reimbursement / commercialization owner confirmed**, and
  - **pre-decision optionality / PDUFA / NDA acceptance / trial expectation**.
- Only the first bucket can receive positive Stage2/Stage3 promotion.
- The second bucket may score as watch/yellow optionality, but must carry a CRL/approval-failure guard.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

Proposed C23 shadow axes:
1. `C23_final_regulatory_approval_commercialization_bonus = +3`
2. `C23_pre_decision_event_beta_cap = cap_at_Stage2_Watch_or_low_Yellow`
3. `C23_4C_regulatory_rejection_route = hard_4C`
4. `C23_post_approval_positioning_4B_overlay = enabled`

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | applies broad post-calibrated thresholds but does not yet isolate approval-finality vs pre-decision event beta | 3 | Yuhan/Hugel/HLB representative | 40.06 | -23.28 | 40.06 | -23.28 | 33.3% | 1 | 1 | 0.864 | n/a | n/a | mixed: positives work, HLB false positive remains |
| P0b e2r_2_0_baseline_reference | rollback reference | looser historical profile over-promotes pre-decision bio event beta | 3 | all representative | 40.06 | -23.28 | 40.06 | -23.28 | 33.3%+ | 0 | 0 | n/a | n/a | n/a | worse guard quality |
| P1 sector_specific_candidate_profile | L7 sector | requires externally verified approval or reimbursement/commercialization path before positive Stage3 promotion | 3 | HLB capped, Yuhan/Hugel selected | 53.59 | -8.79 | 69.27 | -8.79 | 0.0% | 0 | 1 | 0.864 | 0.96 | 0.96 | improved |
| P2 canonical_archetype_candidate_profile | C23 | adds C23_final_regulatory_approval_commercialization_bonus and pre-decision event-beta cap | 3 | Yuhan/Hugel selected; HLB watch/4C | 53.59 | -8.79 | 69.27 | -8.79 | 0.0% | 0 | 1 | 0.864 | 0.96 | 0.96 | best explanatory fit |
| P3 counterexample_guard_profile | C23 guard | if no final approval, cap Stage3 despite relative strength; if CRL, route hard 4C | 1 counterexample + 2 positives | HLB rejected from positive aggregate | 53.59 | -8.79 | 69.27 | -8.79 | 0.0% | 0 | 1 | 0.864 | n/a | n/a | strongest false-positive control |


## 20. Score-Return Alignment Matrix

| case | before profile score/stage | after shadow score/stage | MFE_180D | MAE_180D | score-return alignment |
|---|---:|---:|---:|---:|---|
| Yuhan | 83 / Yellow | 90 / Green | +77.55 | -2.66 | after improves; final approval was stronger than generic Green waited for |
| Hugel | 78 / Yellow | 88 / Green | +60.99 | -14.91 | after improves, but still requires MAE tolerance because launch conversion lag exists |
| HLB | 82 / Yellow | 61 / Watch | +13.00 | -52.27 | after improves by preventing pre-decision false positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | EGFR_LAZERTINIB_US_FDA_APPROVAL_PARTNER_COMMERCIALIZATION | 1 | 0 | 0 | 0 | 1 | 0 | 2 | 1 | 1 | true | true | Yuhan adds drug-level approval-commercialization positive |
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | BOTULINUM_TOXIN_US_APPROVAL_AESTHETIC_COMMERCIALIZATION | 1 | 0 | 1 | 0 | 1 | 0 | 2 | 1 | 1 | true | true | Hugel adds med-aesthetic approval plus 4B overlay |
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | FDA_DECISION_RISK_APPROVAL_EXPECTATION_CRL | 0 | 1 | 0 | 1 | 1 | 0 | 2 | 1 | 1 | true | true | HLB fills counterexample and hard 4C route |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 4
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 4

tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- stage3_green_revision_min
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
- current_profile_too_late
- current_profile_missed_structural
- current_profile_false_positive
- current_profile_4C_too_late

new_axis_proposed:
- C23_final_regulatory_approval_commercialization_bonus
- C23_pre_decision_event_beta_cap
- C23_4C_regulatory_rejection_route
- C23_post_approval_positioning_4B_overlay

existing_axis_strengthened:
- stage2_actionable_evidence_bonus, but only when final regulatory approval exists
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

existing_axis_weakened: null
existing_axis_kept:
- price_only_blowoff_blocks_positive_stage
- stage3_yellow_total_min
- stage3_green_total_min

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- stock-web tradable OHLC rows for 000100, 145020, 028300.
- entry date and entry price separation.
- 30D / 90D / 180D MFE and MAE.
- representative trigger dedupe.
- C23 positive/counterexample balance.
- 4B local/full-window split for Hugel.
- 4C thesis-break routing for HLB.

Not validated:
- current/live candidate discovery.
- production scoring implementation.
- brokerage execution.
- exact future 1Y/2Y calibration beyond the 180D research window.
- formal analyst consensus revision values.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C23_final_regulatory_approval_commercialization_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,+3,+3,"Official approval plus identifiable commercialization owner/partner separates Yuhan/Hugel positives from HLB pre-decision risk","keeps positive avg MFE_180D high while not promoting unapproved event beta","R7L12_C23_YUHAN_STAGE2_APPROVAL_2024-08-20|R7L12_C23_HUGEL_STAGE2_APPROVAL_2024-03-04",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C23_pre_decision_event_beta_cap,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,none,cap_at_Stage2_Watch,-8,"NDA/PDUFA expectation without final approval can show high relative strength but carries CRL gap risk","blocks HLB-style false positive green before approval","R7L12_C23_HLB_PRE_CRL_EXPECTATION_2024-05-14",3,3,1,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,C23_4C_regulatory_rejection_route,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,false,true,+1,"CRL/regulatory rejection is thesis evidence broken, not just 4B valuation cooling","routes HLB 2024-05-17 to 4C even if later rebound occurs","R7L12_C23_HLB_4C_CRL_2024-05-17",3,3,1,medium,4C_shadow_only,"not production; post-calibrated residual"
shadow_weight,C23_post_approval_positioning_4B_overlay,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,none,enabled,+1,"After verified approval and rerating, 4B should require valuation/positioning overlay rather than price-only peak","captures Hugel full-window peak proximity near 0.96","R7L12_C23_HUGEL_4B_POSITIONING_2024-11-06",3,3,1,low,4B_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R7L12_C23_YUHAN_LAZCLUZE_APPROVAL","symbol":"000100","company_name":"유한양행","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"EGFR_LAZERTINIB_US_FDA_APPROVAL_PARTNER_COMMERCIALIZATION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L12_C23_YUHAN_STAGE2_APPROVAL_2024-08-20","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive aligned","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"FDA approval of lazertinib with amivantamab converted prior clinical optionality into externally verified commercialization evidence."}
{"row_type":"case","case_id":"R7L12_C23_HUGEL_LETYBO_APPROVAL","symbol":"145020","company_name":"휴젤","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BOTULINUM_TOXIN_US_APPROVAL_AESTHETIC_COMMERCIALIZATION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L12_C23_HUGEL_STAGE2_APPROVAL_2024-03-04","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive aligned","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"FDA approval of LETYBO created an approval-to-commercialization path, but the full upside was captured only after later launch/positioning follow-through."}
{"row_type":"case","case_id":"R7L12_C23_HLB_APPROVAL_EXPECTATION_CRL","symbol":"028300","company_name":"HLB","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"FDA_DECISION_RISK_APPROVAL_EXPECTATION_CRL","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R7L12_C23_HLB_PRE_CRL_EXPECTATION_2024-05-14","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample: high MAE after approval expectation","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Pre-decision approval expectation generated high event beta, but the CRL/gap-down path shows that C23 positive promotion must require final approval or robust de-risked regulatory evidence."}
{"row_type":"trigger","trigger_id":"R7L12_C23_YUHAN_STAGE2_APPROVAL_2024-08-20","case_id":"R7L12_C23_YUHAN_LAZCLUZE_APPROVAL","symbol":"000100","company_name":"유한양행","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"EGFR_LAZERTINIB_US_FDA_APPROVAL_PARTNER_COMMERCIALIZATION","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-20","evidence_available_at_that_date":"FDA approval of lazertinib with amivantamab for first-line EGFR-mutated NSCLC; partner commercialization route is external and drug-level.","evidence_source":"FDA approved lazertinib with amivantamab on 2024-08-19; FDA content current as of 2024-08-20.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-20","entry_price":94000,"MFE_30D_pct":70.53,"MFE_90D_pct":77.55,"MFE_180D_pct":77.55,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.66,"MAE_90D_pct":-2.66,"MAE_180D_pct":-2.66,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":"0.864 when later Stage3-Green is 2024-09-24 close 157000 vs Stage2 94000 and peak 166900","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"approval_to_commercialization_structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L12_000100_2024-08-20_94000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L12_C23_YUHAN_STAGE3_GREEN_2024-09-24","case_id":"R7L12_C23_YUHAN_LAZCLUZE_APPROVAL","symbol":"000100","company_name":"유한양행","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"EGFR_LAZERTINIB_US_FDA_APPROVAL_PARTNER_COMMERCIALIZATION","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test","trigger_type":"Stage3-Green","trigger_date":"2024-09-24","evidence_available_at_that_date":"post-approval market confirmation and cross-source rerating after initial commercialization approval.","evidence_source":"Stock-Web price row only for label-comparison timing; evidence is later market-confirmation proxy, not used to backdate Stage2.","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-09-24","entry_price":157000,"MFE_30D_pct":6.31,"MFE_90D_pct":6.31,"MFE_180D_pct":6.31,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.55,"MAE_90D_pct":-30.57,"MAE_180D_pct":-36.05,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":0.864,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"green_late_after_approval_event","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L12_000100_2024-09-24_157000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R7L12_C23_HUGEL_STAGE2_APPROVAL_2024-03-04","case_id":"R7L12_C23_HUGEL_LETYBO_APPROVAL","symbol":"145020","company_name":"휴젤","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BOTULINUM_TOXIN_US_APPROVAL_AESTHETIC_COMMERCIALIZATION","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-29","evidence_available_at_that_date":"FDA Drug Trials Snapshot lists LETYBO, Hugel, Inc., approval date February 29, 2024; first Korean tradable date used as entry.","evidence_source":"FDA Drug Trials Snapshots: LETYBO, approval date 2024-02-29.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-04","entry_price":202500,"MFE_30D_pct":8.15,"MFE_90D_pct":29.63,"MFE_180D_pct":60.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.91,"MAE_90D_pct":-14.91,"MAE_180D_pct":-14.91,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000,"drawdown_after_peak_pct":-27.3,"green_lateness_ratio":"not_applicable; no single confirmed Stage3-Green trigger used as representative","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"approval_to_commercialization_structural_success_with_high_initial_MAE","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L12_145020_2024-03-04_202500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L12_C23_HUGEL_4B_POSITIONING_2024-11-06","case_id":"R7L12_C23_HUGEL_LETYBO_APPROVAL","symbol":"145020","company_name":"휴젤","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BOTULINUM_TOXIN_US_APPROVAL_AESTHETIC_COMMERCIALIZATION","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test","trigger_type":"Stage4B","trigger_date":"2024-11-06","evidence_available_at_that_date":"post-approval rerating reached full-window peak zone; evidence type is positioning/valuation overlay rather than thesis break.","evidence_source":"Stock-Web OHLC; non-price interpretation is post-approval launch/valuation overlay.","stage2_evidence_fields":[],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-11-06","entry_price":321000,"MFE_30D_pct":1.56,"MFE_90D_pct":1.56,"MFE_180D_pct":1.56,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-26.17,"MAE_90D_pct":-26.17,"MAE_180D_pct":-26.17,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000,"drawdown_after_peak_pct":-27.3,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L12_145020_2024-11-06_321000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R7L12_C23_HLB_PRE_CRL_EXPECTATION_2024-05-14","case_id":"R7L12_C23_HLB_APPROVAL_EXPECTATION_CRL","symbol":"028300","company_name":"HLB","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"FDA_DECISION_RISK_APPROVAL_EXPECTATION_CRL","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-14","evidence_available_at_that_date":"pre-decision approval expectation and event beta before final FDA decision; no final approval existed at this trigger date.","evidence_source":"Public event-risk setup; 4C source is subsequent CRL/rejection path. Representative row uses stock-web price before the event break.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-14","entry_price":94600,"MFE_30D_pct":13.0,"MFE_90D_pct":13.0,"MFE_180D_pct":13.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-52.27,"MAE_90D_pct":-52.27,"MAE_180D_pct":-52.27,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":106900,"drawdown_after_peak_pct":-57.76,"green_lateness_ratio":"not_applicable; no confirmed Stage3-Green because the thesis broke before approval","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"pre_event_positioning_overheat_not_full_4B","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"approval_expectation_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L12_028300_2024-05-14_94600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L12_C23_HLB_4C_CRL_2024-05-17","case_id":"R7L12_C23_HLB_APPROVAL_EXPECTATION_CRL","symbol":"028300","company_name":"HLB","round":"R7","loop":"12","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"FDA_DECISION_RISK_APPROVAL_EXPECTATION_CRL","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2024-05-17","evidence_available_at_that_date":"FDA CRL / approval failure event path; thesis evidence broken rather than mere valuation cooling.","evidence_source":"Public CRL event path; stock-web shows immediate limit-down style gap on 2024-05-17 and follow-through low.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","positioning_overheat"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":67100,"MFE_30D_pct":9.99,"MFE_90D_pct":46.2,"MFE_180D_pct":46.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-32.71,"MAE_90D_pct":-32.71,"MAE_180D_pct":-32.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-23","peak_price":97600,"drawdown_after_peak_pct":-53.74,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_hard_4C","four_b_evidence_type":["explicit_event_cap"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_thesis_break_with_rebound_risk","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L12_028300_2024-05-17_67100","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L12_C23_YUHAN_LAZCLUZE_APPROVAL","trigger_id":"R7L12_C23_YUHAN_STAGE2_APPROVAL_2024-08-20","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":18,"relative_strength_score":11,"customer_quality_score":16,"policy_or_regulatory_score":19,"valuation_repricing_score":8,"execution_risk_score":-3,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":14},"weighted_score_before":83.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":19,"relative_strength_score":11,"customer_quality_score":18,"policy_or_regulatory_score":22,"valuation_repricing_score":9,"execution_risk_score":-3,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":17},"weighted_score_after":90.0,"stage_label_after":"Stage3-Green","changed_components":["policy_or_regulatory_score","commercialization_score","legal_or_contract_risk_score","execution_risk_score"],"component_delta_explanation":"C23 shadow rule separates final approval/commercialization evidence from pre-decision event beta; counterexample guard penalizes unapproved CRL-risk setups.","MFE_90D_pct":77.55,"MAE_90D_pct":-2.66,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"proposed_sector_or_archetype_shadow_profile","case_id":"R7L12_C23_YUHAN_LAZCLUZE_APPROVAL","trigger_id":"R7L12_C23_YUHAN_STAGE3_GREEN_2024-09-24","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":18,"relative_strength_score":11,"customer_quality_score":16,"policy_or_regulatory_score":19,"valuation_repricing_score":8,"execution_risk_score":-3,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":14},"weighted_score_before":83.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":19,"relative_strength_score":11,"customer_quality_score":18,"policy_or_regulatory_score":22,"valuation_repricing_score":9,"execution_risk_score":-3,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":17},"weighted_score_after":90.0,"stage_label_after":"Stage3-Green","changed_components":["policy_or_regulatory_score","commercialization_score","legal_or_contract_risk_score","execution_risk_score"],"component_delta_explanation":"C23 shadow rule separates final approval/commercialization evidence from pre-decision event beta; counterexample guard penalizes unapproved CRL-risk setups.","MFE_90D_pct":6.31,"MAE_90D_pct":-30.57,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L12_C23_HUGEL_LETYBO_APPROVAL","trigger_id":"R7L12_C23_HUGEL_STAGE2_APPROVAL_2024-03-04","symbol":"145020","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":8,"customer_quality_score":13,"policy_or_regulatory_score":21,"valuation_repricing_score":7,"execution_risk_score":-4,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":13},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":13,"relative_strength_score":8,"customer_quality_score":15,"policy_or_regulatory_score":22,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":17},"weighted_score_after":88.0,"stage_label_after":"Stage3-Green","changed_components":["policy_or_regulatory_score","commercialization_score","legal_or_contract_risk_score","execution_risk_score"],"component_delta_explanation":"C23 shadow rule separates final approval/commercialization evidence from pre-decision event beta; counterexample guard penalizes unapproved CRL-risk setups.","MFE_90D_pct":29.63,"MAE_90D_pct":-14.91,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"proposed_sector_or_archetype_shadow_profile","case_id":"R7L12_C23_HUGEL_LETYBO_APPROVAL","trigger_id":"R7L12_C23_HUGEL_4B_POSITIONING_2024-11-06","symbol":"145020","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":8,"customer_quality_score":13,"policy_or_regulatory_score":21,"valuation_repricing_score":7,"execution_risk_score":-4,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":13},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":13,"relative_strength_score":8,"customer_quality_score":15,"policy_or_regulatory_score":22,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":17},"weighted_score_after":88.0,"stage_label_after":"Stage3-Green","changed_components":["policy_or_regulatory_score","commercialization_score","legal_or_contract_risk_score","execution_risk_score"],"component_delta_explanation":"C23 shadow rule separates final approval/commercialization evidence from pre-decision event beta; counterexample guard penalizes unapproved CRL-risk setups.","MFE_90D_pct":1.56,"MAE_90D_pct":-26.17,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L12_C23_HLB_APPROVAL_EXPECTATION_CRL","trigger_id":"R7L12_C23_HLB_PRE_CRL_EXPECTATION_2024-05-14","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":11,"relative_strength_score":19,"customer_quality_score":7,"policy_or_regulatory_score":17,"valuation_repricing_score":14,"execution_risk_score":-11,"legal_or_contract_risk_score":-8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":0},"weighted_score_before":82.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":6,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":7,"valuation_repricing_score":5,"execution_risk_score":-18,"legal_or_contract_risk_score":-22,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":0},"weighted_score_after":61.0,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","commercialization_score","legal_or_contract_risk_score","execution_risk_score"],"component_delta_explanation":"C23 shadow rule separates final approval/commercialization evidence from pre-decision event beta; counterexample guard penalizes unapproved CRL-risk setups.","MFE_90D_pct":13.0,"MAE_90D_pct":-52.27,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"proposed_sector_or_archetype_shadow_profile","case_id":"R7L12_C23_HLB_APPROVAL_EXPECTATION_CRL","trigger_id":"R7L12_C23_HLB_4C_CRL_2024-05-17","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":11,"relative_strength_score":19,"customer_quality_score":7,"policy_or_regulatory_score":17,"valuation_repricing_score":14,"execution_risk_score":-11,"legal_or_contract_risk_score":-8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":0},"weighted_score_before":82.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":6,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":7,"valuation_repricing_score":5,"execution_risk_score":-18,"legal_or_contract_risk_score":-22,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":0},"weighted_score_after":61.0,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","commercialization_score","legal_or_contract_risk_score","execution_risk_score"],"component_delta_explanation":"C23 shadow rule separates final approval/commercialization evidence from pre-decision event beta; counterexample guard penalizes unapproved CRL-risk setups.","MFE_90D_pct":46.2,"MAE_90D_pct":-32.71,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"residual_contribution","round":"R7","loop":"12","scheduled_round":"R7","scheduled_loop":"12","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_too_late","current_profile_missed_structural","current_profile_false_positive","current_profile_4C_too_late"],"diversity_score_summary":"estimated +55; new symbols=3, new trigger families=4, counterexample=1, residual errors=3, wrong_round_penalty=0","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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

- Price atlas: Songdaiki/stock-web, `atlas/manifest.json`, `atlas/ohlcv_tradable_by_symbol_year`, raw/unadjusted FinanceData/marcap basis.
- FDA lazertinib approval source: `https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-lazertinib-amivantamab-vmjw-non-small-lung-cancer`
- FDA LETYBO snapshot source: `https://www.fda.gov/drugs/drug-trials-snapshots/drug-trials-snapshots-letybo`
- HLB CRL row is treated as a public regulatory thesis-break event; quantitative calibration is based on stock-web OHLC only, with no live recommendation inference.
