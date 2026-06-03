# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| field | value |
|---|---|
| research_session | post_calibrated_sector_archetype_residual_research |
| mode | historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12 |
| output_file | `e2r_stock_web_v12_residual_round_R7_loop_14_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md` |
| scheduled_round | R7 |
| scheduled_loop | 14 |
| completed_round | R7 |
| completed_loop | 14 |
| next_round | R8 |
| next_loop | 14 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION |
| fine_archetype_id | BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_CRL_REDTEAM |
| stock_agent_code_access_allowed | false |
| stock_agent_code_patch_allowed | false |
| stock_agent_live_scan_allowed | false |
| production_scoring_changed | false |
| shadow_weight_only | true |
| price_source | Songdaiki/stock-web |
| stock_web_manifest_max_date | 2026-02-20 |
| loop_objective | coverage_gap_fill; residual_false_positive_mining; counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test |
| loop_contribution_label | canonical_archetype_rule_candidate |
| do_not_propose_new_weight_delta | false |

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for `R7/L7_BIO_HEALTHCARE_MEDICAL/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION`.

## 1. Current Calibrated Profile Assumption

The current profile proxy is `e2r_2_1_stock_web_calibrated`. It already includes:

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

This round does **not** re-argue the global Stage2 bonus or the global 4B/4C guards. It stress-tests them inside C23 and proposes only a C23-specific shadow ledger adjustment.

## 2. Round / Large Sector / Canonical Archetype Scope

| dimension | selected |
|---|---|
| round | R7 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION |
| allowed C23 evidence | hard approval, approvability evidence, commercialization/royalty conversion, durable customer confirmation |
| explicit red-team | pre-approval expectation / PDUFA event-cap cannot clear Green by itself |

## 3. Previous Coverage / Duplicate Avoidance Check

The allowed registry shows older parsed R7 healthcare rounds up to loop 8, but no v12 residual file with this exact filename pattern was found in the accessible registry. The immediately preceding generated handoff state in this conversation completed `R6 / loop 14` and pointed to `R7 / loop 14`.

Duplicate-avoidance result:

```text
same_symbol_same_trigger_date_research = false
same_symbol_same_entry_group_reuse = false
new_symbol_count = 3 calibration-usable + 1 narrative-only blocked
new_trigger_family_count = 4
new_independent_case_ratio = 1.00 among calibration-usable cases
```

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest fields used for this run:

| field | value |
|---|---|
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
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Profile validation summary:

| symbol | company | profile_path | profile first-last | available years used | corporate-action window status |
|---|---:|---|---|---|---|
| 196170 | 알테오젠 | atlas/symbol_profiles/196/196170.json | 2014-12-12 ~ 2026-02-20 | 2024 | clean_180D_window; historical CA candidates before 2024 |
| 000100 | 유한양행 | atlas/symbol_profiles/000/000100.json | 1995-05-02 ~ 2026-02-20 | 2024 | clean_180D_window; historical CA candidates before 2024 |
| 028300 | HLB | atlas/symbol_profiles/028/028300.json | 1996-09-02 ~ 2026-02-20 | 2024 | clean_180D_window; historical CA candidates before 2024 |
| 141080 | 리가켐바이오 | atlas/symbol_profiles/141/141080.json | 2013-05-10 ~ 2026-02-20 | 2023-2024 | blocked: 2024-04-23 corporate-action candidate inside 180D window |

## 5. Historical Eligibility Gate

| case | entry date in tradable shard | 180D forward available | OHLC complete | CA contaminated 180D | calibration_usable |
|---|---:|---:|---:|---:|---:|
| 알테오젠 196170 | yes | yes | yes | no | true |
| 유한양행 000100 | yes | yes | yes | no | true |
| HLB 028300 | yes | yes | yes | no | true |
| 리가켐바이오 141080 | yes | yes | yes | yes | false |

## 6. Canonical Archetype Compression Map

```text
ALT-B4 / SC platform licensing conversion
  -> C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  -> evidence: durable customer + commercialization/royalty route

Yuhan Lazcluze FDA approval
  -> C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  -> evidence: hard FDA approval + first-line treatment label

HLB FDA CRL / non-approval
  -> C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION red-team
  -> evidence: regulatory rejection + thesis evidence broken

LCB ADC platform licensing
  -> C23 narrative-only this loop
  -> blocked: corporate_action_contaminated_180D_window
```

The compression lesson is that C23 should not treat all “approval-related anticipation” as the same animal. A hard approval is a bridge; pre-approval expectation is a cliff edge.

## 7. Case Selection Summary

| case_id                         |   symbol | company_name   | role                 | positive_or_counterexample   | calibration_usable   | current_profile_verdict           | notes                                                                                                                                                                                      |
|:--------------------------------|---------:|:---------------|:---------------------|:-----------------------------|:---------------------|:----------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R7L14-C23-ALT-196170-20240223   |   196170 | 알테오젠       | structural_success   | positive                     | True                 | current_profile_too_late          | SC formulation/enzyme platform licensing turned into a clearer commercialization/royalty route; early trigger carried strong customer quality but Green confirmation would have been late. |
| R7L14-C23-YUHAN-000100-20240821 |   000100 | 유한양행       | structural_success   | positive                     | True                 | current_profile_correct           | FDA approval supplied clean non-price regulatory confirmation and immediate commercialization option.                                                                                      |
| R7L14-C23-HLB-028300-20240516   |   028300 | HLB            | false_positive_green | counterexample               | True                 | current_profile_false_positive    | High expectation ahead of FDA decision was not enough; CRL routed directly to 4C thesis break.                                                                                             |
| R7L14-C23-LCB-141080-20231227   |   141080 | 리가켐바이오   | narrative_only       | positive                     | False                | current_profile_data_insufficient | Useful narrative case for ADC platform licensing, but stock-web profile flags 2024-04-23 corporate-action candidate within 180D window, so it is not used for quantitative calibration.    |

## 8. Positive vs Counterexample Balance

| label | count | cases |
|---|---:|---|
| positive_structural_success | 2 | 알테오젠, 유한양행 |
| counterexample_or_failed_rerating | 1 | HLB |
| 4B_overlay_case | 2 | 알테오젠 peak row, 유한양행 peak row |
| 4C_case | 1 | HLB CRL |
| narrative_only | 1 | 리가켐바이오 blocked by CA window |

The minimum R7 requirement is met: `positive_case_count >= 1`, `counterexample_count >= 1`, and `calibration_usable_case_count >= 3`.

## 9. Evidence Source Map

| case | trigger date | evidence family | source class | evidence separation |
|---|---:|---|---|---|
| 알테오젠 | 2024-02-22 / 2024-02-23 | platform-license conversion / durable customer | company disclosure, public press, stock-web OHLC | Stage2/3 evidence is non-price; 4B peak row is price-only overlay |
| 유한양행 | 2024-08-20 / 2024-08-21 | FDA approval / first-line NSCLC label | FDA approval notification, stock-web OHLC | hard regulatory evidence supports Stage3-Green |
| HLB | 2024-05-16 / 2024-05-17 | pre-approval expectation then CRL | public company communication, regulatory event, stock-web OHLC | pre-event Green is blocked; CRL routes to 4C |
| 리가켐바이오 | 2023-12-26 / 2023-12-27 | ADC platform license | public disclosure, stock-web profile | narrative only because CA candidate blocks 180D window |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry rows checked |
|---|---|---|---|
| 196170 | atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv | atlas/symbol_profiles/196/196170.json | 2024-02-23 close 131200; 2024-11-11 peak high 455500 |
| 000100 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv | atlas/symbol_profiles/000/000100.json | 2024-08-21 close 94300; 2024-10-15 peak high 166900 |
| 028300 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json | 2024-05-16 close 95800; 2024-05-17 close 67100; 2024-05-21 low 45150 |
| 141080 | atlas/ohlcv_tradable_by_symbol_year/141/141080/2023.csv and 2024.csv | atlas/symbol_profiles/141/141080.json | 2023-12-27 close 61100; 2024-04-23 CA candidate blocks 180D |

## 11. Case-by-Case Trigger Grid

| trigger_id   |   symbol | company_name   | trigger_type           | trigger_date   | entry_date   |   entry_price |   MFE_30D_pct |   MFE_90D_pct |   MFE_180D_pct |   MAE_30D_pct |   MAE_90D_pct |   MAE_180D_pct | trigger_outcome_label             | current_profile_verdict        | dedupe_for_aggregate   |
|:-------------|---------:|:---------------|:-----------------------|:---------------|:-------------|--------------:|--------------:|--------------:|---------------:|--------------:|--------------:|---------------:|:----------------------------------|:-------------------------------|:-----------------------|
| R7L14-T001   |   196170 | 알테오젠       | Stage2-Actionable      | 2024-02-22     | 2024-02-23   |        131200 |         71.88 |        127.52 |         247.18 |         -9.3  |         -9.3  |          -9.3  | structural_success                | current_profile_too_late       | True                   |
| R7L14-T002   |   196170 | 알테오젠       | Stage3-Green           | 2024-03-13     | 2024-03-13   |        201000 |         12.19 |         48.51 |         126.62 |        -22.29 |        -22.29 |         -22.29 | late_green_but_still_positive     | current_profile_too_late       | False                  |
| R7L14-T003   |   196170 | 알테오젠       | Stage4B-Overlay        | 2024-11-11     | 2024-11-11   |        445500 |          2.24 |          2.24 |           2.24 |        -37.37 |        -38.75 |         -38.75 | 4B_overlay_success_but_price_only | current_profile_correct        | False                  |
| R7L14-T004   |   000100 | 유한양행       | Stage3-Green           | 2024-08-20     | 2024-08-21   |         94300 |         69.99 |         76.99 |          76.99 |         -2.97 |         -2.97 |          -2.97 | structural_success                | current_profile_correct        | True                   |
| R7L14-T005   |   000100 | 유한양행       | Stage4B-Overlay        | 2024-10-15     | 2024-10-15   |        163700 |          1.96 |          1.96 |           1.96 |        -25.41 |        -33.41 |         -33.41 | 4B_overlay_success_but_price_only | current_profile_correct        | False                  |
| R7L14-T006   |   028300 | HLB            | Stage3-Green-candidate | 2024-05-16     | 2024-05-16   |         95800 |        -22.96 |          2.4  |           2.4  |        -52.87 |        -52.87 |         -52.87 | false_positive_green              | current_profile_false_positive | True                   |
| R7L14-T007   |   028300 | HLB            | Stage4C                | 2024-05-17     | 2024-05-17   |         67100 |          9.99 |         46.2  |          46.2  |        -32.71 |        -32.71 |         -32.71 | 4C_success                        | current_profile_4C_too_late    | False                  |

## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate rows:

| case | entry | entry_price | peak_date | peak_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 알테오젠 | 2024-02-23 | 131200 | 2024-11-11 | 455500 | 71.88 | -9.30 | 127.52 | -9.30 | 247.18 | -9.30 | early non-price platform-license trigger was valuable |
| 유한양행 | 2024-08-21 | 94300 | 2024-10-15 | 166900 | 69.99 | -2.97 | 76.99 | -2.97 | 76.99 | -2.97 | hard approval trigger aligned with return |
| HLB | 2024-05-16 | 95800 | 2024-07-08 | 98100 | -22.96 | -52.87 | 2.40 | -52.87 | 2.40 | -52.87 | pre-approval expectation was false positive |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely action | actual MFE/MAE | residual verdict |
|---|---|---|---|
| 알테오젠 | likely Yellow first, Green only after confirmation | +127.52% MFE_90D with -9.30% MAE | current_profile_too_late |
| 유한양행 | Green allowed after hard FDA approval | +76.99% MFE_90D with -2.97% MAE | current_profile_correct |
| HLB | could over-promote if expectation and RS dominate | +2.40% MFE_90D with -52.87% MAE | current_profile_false_positive |
| 리가켐바이오 | data insufficient for calibration | CA-blocked window | current_profile_data_insufficient |

Answers to required stress-test questions:

```text
1. current profile handles hard approval well: Yuhan = correct.
2. current profile can be too late for platform-license conversion when durable customer + royalty route are already public: Alteogen = too_late.
3. current profile can still be too permissive if pre-approval expectation is scored like approval evidence: HLB = false_positive.
4. Stage2 bonus is not globally changed; C23 needs an event-quality gate.
5. Yellow 75 is not weakened.
6. Green 87 / revision 55 is kept, but C23 component composition should reward hard approval / durable customer route and penalize event-cap uncertainty.
7. price-only 4B guard is kept.
8. full 4B non-price requirement is kept.
9. hard 4C routing is strengthened for CRL/regulatory rejection.
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 / actionable entry | Green entry | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| 알테오젠 | 131200 | 201000 | 455500 | 0.215 | Green not catastrophic, but C23 platform-license route had enough non-price evidence earlier |
| 유한양행 | 94300 | 94300 | 166900 | 0.000 | hard FDA approval is clean Green |
| HLB | 95800 candidate | should be blocked | 98100 | N/A | pre-approval expectation should not become Green |

## 15. 4B Local vs Full-window Timing Audit

| case | 4B trigger | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---:|---|---|
| 알테오젠 | 2024-11-11 | 1.00 | 1.00 | price_only; valuation_blowoff; positioning_overheat | Useful overlay, but not full 4B without non-price deterioration |
| 유한양행 | 2024-10-15 | 1.00 | 1.00 | price_only; valuation_blowoff; positioning_overheat | Useful overlay, but not thesis break |
| HLB | event-cap before CRL | N/A | N/A | explicit_event_cap; positioning_overheat | Event-cap risk should block Green even before 4C |

## 16. 4C Protection Audit

HLB is the 4C test. The pre-CRL candidate entry at 95800 suffered `MAE_90D = -52.87%`. The hard 4C row on 2024-05-17 still had rebound risk, but the regulatory rejection label correctly ended the prior approval thesis. This supports `hard_4c_thesis_break_routes_to_4c` and adds a C23-specific `CRL/regulatory rejection` guard.

```text
four_c_protection_label = hard_4c_success_after_crl
four_c_protection_score = qualitative_success
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

R7 as a whole is too broad. Medical device reimbursement, trial-data event risk, and drug approval commercialization behave differently. The signal is not L7-wide.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
```

Proposed C23 shadow rule:

```text
If C23 evidence includes hard regulatory approval OR durable customer/platform-license conversion with visible commercialization/royalty route:
    allow small C23-specific promotion to Stage3 quality, subject to non-price evidence.

If C23 evidence is only pre-approval anticipation, PDUFA proximity, rumor, or relative strength:
    block Stage3-Green even when total score or RS is high.

If CRL/regulatory rejection appears:
    route to hard 4C thesis break immediately.
```

## 19. Before / After Backtest Comparison

| profile_id                               |   eligible_trigger_count | selected_entry_trigger_per_case                   |   avg_MFE_90D_pct |   avg_MAE_90D_pct | false_positive_rate   |   missed_structural_count |   late_green_count | score_return_alignment_verdict                                                |
|:-----------------------------------------|-------------------------:|:--------------------------------------------------|------------------:|------------------:|:----------------------|--------------------------:|-------------------:|:------------------------------------------------------------------------------|
| P0 e2r_2_1_stock_web_calibrated_proxy    |                        3 | ALT T001; Yuhan T004; HLB T006                    |             68.97 |            -21.71 | 1/3                   |                         1 |                  1 | mixed: good hard approval, late platform-license, false positive pre-approval |
| P0b e2r_2_0_baseline_reference           |                        3 | more price/RS sensitive                           |             68.97 |            -21.71 | 1/3+                  |                         1 |                  1 | weaker distinction between hard approval and expectation                      |
| P1 sector_specific_candidate_profile     |                        3 | same reps; no sector-wide delta                   |             68.97 |            -21.71 | 1/3                   |                         1 |                  1 | sector-wide rule too broad; C23 scope preferred                               |
| P2 canonical_archetype_candidate_profile |                        3 | ALT/Yuhan promoted; HLB event-cap blocked         |            102.25 |             -6.14 | 0/3 after guard       |                         0 |                  0 | best fit for C23 residual                                                     |
| P3 counterexample_guard_profile          |                        3 | HLB blocked unless hard approval evidence appears |            102.25 |             -6.14 | 0/3                   |                         0 |                  1 | good guard but too conservative on platform licensing unless combined with P2 |

## 20. Score-Return Alignment Matrix

| case | weighted before | stage before | weighted after | stage after | return alignment |
|---|---:|---|---:|---|---|
| 알테오젠 | 84 | Stage3-Yellow | 89 | Stage3-Green | after better captures platform-license conversion |
| 유한양행 | 88 | Stage3-Green | 91 | Stage3-Green | both valid; after records C23 hard approval quality |
| HLB | 87 | Stage3-Green-candidate | 70 | Stage2-Watch / event-cap blocked | after avoids false positive |
| 리가켐바이오 | N/A | narrative_only | N/A | narrative_only | blocked by CA window |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_CRL_REDTEAM | 2 | 1 | 2 | 1 | 3 | 0 | 7 | 3 | 2 | false | true | C23 now has hard approval, platform-license conversion, and CRL counterexample coverage; still needs more non-oncology and device/diagnostic approval cases. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3 calibration-usable, 1 narrative-only
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_too_late for platform-license conversion
  - current_profile_false_positive for pre-approval expectation
  - price-only 4B overlay should not become thesis break
new_axis_proposed:
  - C23_hard_approval_or_customer_quality_route_bonus
  - C23_pre_approval_expectation_event_cap_guard
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- actual stock-web tradable OHLC rows for entry, peak, MFE/MAE anchors
- manifest max_date = 2026-02-20
- profile corporate-action caveats
- 180D calibration usability for 196170, 000100, 028300
- C23 positive vs counterexample balance
```

Not validated:

```text
- production scoring code
- live candidate scan
- current investment recommendation
- brokerage/API integration
- global profile patch
- L7-wide sector rule
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C23_hard_approval_or_customer_quality_route_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Hard FDA approval or platform-license conversion with durable customer quality should receive a small C23-specific promotion, not a global Stage2 bonus.","Improves separation of ALTEOGEN/Yuhan positives from HLB pre-approval expectation.","R7L14-T001|R7L14-T004",3,2,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C23_pre_approval_expectation_event_cap_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Pre-PDUFA / pending-approval anticipation cannot clear Green without hard approval, approvability evidence, or high-quality regulatory confirmation.","Blocks HLB-like false positive while keeping Yuhan hard approval valid.","R7L14-T006|R7L14-T007",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C23_price_only_4B_overlay_not_full_exit,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,0,"Price-only blowoff after bio approval/licensing runs should stay 4B overlay unless non-price deterioration appears.","Keeps ALTEOGEN/Yuhan peak rows as overlay-only; avoids converting price peak into thesis break.","R7L14-T003|R7L14-T005",2,2,0,low,canonical_shadow_only,"stress test of existing applied axis"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R7L14-C23-ALT-196170-20240223", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_CRL_REDTEAM", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R7L14-T001", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "SC formulation/enzyme platform licensing turned into a clearer commercialization/royalty route; early trigger carried strong customer quality but Green confirmation would have been late."}
{"row_type": "case", "case_id": "R7L14-C23-YUHAN-000100-20240821", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_CRL_REDTEAM", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R7L14-T004", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "FDA approval supplied clean non-price regulatory confirmation and immediate commercialization option."}
{"row_type": "case", "case_id": "R7L14-C23-HLB-028300-20240516", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_CRL_REDTEAM", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R7L14-T006", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "High expectation ahead of FDA decision was not enough; CRL routed directly to 4C thesis break."}
{"row_type": "case", "case_id": "R7L14-C23-LCB-141080-20231227", "symbol": "141080", "company_name": "리가켐바이오", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_CRL_REDTEAM", "case_type": "narrative_only", "positive_or_counterexample": "positive", "best_trigger": "R7L14-N001", "calibration_usable": false, "is_new_independent_case": true, "reuse_reason": "corporate_action_contaminated_180D_window", "independent_evidence_weight": 0.0, "score_price_alignment": "not_weight_calibration", "current_profile_verdict": "current_profile_data_insufficient", "price_source": "Songdaiki/stock-web", "notes": "Useful narrative case for ADC platform licensing, but stock-web profile flags 2024-04-23 corporate-action candidate within 180D window, so it is not used for quantitative calibration."}
{"row_type": "trigger", "trigger_id": "R7L14-T001", "case_id": "R7L14-C23-ALT-196170-20240223", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_CRL_REDTEAM", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "entry_date": "2024-02-23", "entry_price": 131200, "evidence_available_at_that_date": "ALT-B4 / SC formulation licensing economics became materially clearer via MSD-linked contract-amendment style public event; entry uses next tradable close after event digestion.", "evidence_source": "company disclosure / public press coverage / stock-web OHLC", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["durable_customer_confirmation", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 71.88, "MFE_90D_pct": 127.52, "MFE_180D_pct": 247.18, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.3, "MAE_90D_pct": -9.3, "MAE_180D_pct": -9.3, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-11", "peak_price": 455500, "drawdown_after_peak_pct": -38.75, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L14-G001", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L14-T002", "case_id": "R7L14-C23-ALT-196170-20240223", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_CRL_REDTEAM", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY", "loop_objective": "green_strictness_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2024-03-13", "entry_date": "2024-03-13", "entry_price": 201000, "evidence_available_at_that_date": "Post-event price/evidence confirmation after platform route became accepted; used only for lateness comparison, not aggregate entry.", "evidence_source": "stock-web OHLC + public follow-through evidence", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality"], "stage3_evidence_fields": ["durable_customer_confirmation", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.19, "MFE_90D_pct": 48.51, "MFE_180D_pct": 126.62, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -22.29, "MAE_90D_pct": -22.29, "MAE_180D_pct": -22.29, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-11", "peak_price": 455500, "drawdown_after_peak_pct": -38.75, "green_lateness_ratio": 0.215, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "late_green_but_still_positive", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L14-G001-LABEL", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R7L14-T003", "case_id": "R7L14-C23-ALT-196170-20240223", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_CRL_REDTEAM", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-11-11", "entry_date": "2024-11-11", "entry_price": 445500, "evidence_available_at_that_date": "Observed blowoff/positioning peak after long run; no separate non-price thesis deterioration identified in this loop.", "evidence_source": "stock-web OHLC only", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.24, "MFE_90D_pct": 2.24, "MFE_180D_pct": 2.24, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -37.37, "MAE_90D_pct": -38.75, "MAE_180D_pct": -38.75, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-11", "peak_price": 455500, "drawdown_after_peak_pct": -38.75, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_peak_do_not_treat_as_full_4B_without_non_price_evidence", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": null, "trigger_outcome_label": "4B_overlay_success_but_price_only", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L14-G001-4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R7L14-T004", "case_id": "R7L14-C23-YUHAN-000100-20240821", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_CRL_REDTEAM", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY", "loop_objective": "coverage_gap_fill|holdout_validation|canonical_archetype_compression", "trigger_type": "Stage3-Green", "trigger_date": "2024-08-20", "entry_date": "2024-08-21", "entry_price": 94300, "evidence_available_at_that_date": "FDA approval of lazertinib in combination with amivantamab for first-line EGFR-mutated NSCLC; entry uses next Korean tradable close after U.S. approval publication.", "evidence_source": "FDA approved-drug notification + stock-web OHLC", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources", "financial_visibility", "durable_customer_confirmation", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 69.99, "MFE_90D_pct": 76.99, "MFE_180D_pct": 76.99, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.97, "MAE_90D_pct": -2.97, "MAE_180D_pct": -2.97, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-10-15", "peak_price": 166900, "drawdown_after_peak_pct": -34.69, "green_lateness_ratio": 0.0, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L14-G002", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L14-T005", "case_id": "R7L14-C23-YUHAN-000100-20240821", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_CRL_REDTEAM", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-10-15", "entry_date": "2024-10-15", "entry_price": 163700, "evidence_available_at_that_date": "Peak/positioning heat after approval run; no independent clinical/regulatory thesis break at peak.", "evidence_source": "stock-web OHLC only", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.96, "MFE_90D_pct": 1.96, "MFE_180D_pct": 1.96, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -25.41, "MAE_90D_pct": -33.41, "MAE_180D_pct": -33.41, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-15", "peak_price": 166900, "drawdown_after_peak_pct": -34.69, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_peak_do_not_treat_as_full_4B_without_non_price_evidence", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": null, "trigger_outcome_label": "4B_overlay_success_but_price_only", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L14-G002-4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R7L14-T006", "case_id": "R7L14-C23-HLB-028300-20240516", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_CRL_REDTEAM", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "BIO_APPROVAL_EVENT_RISK", "loop_objective": "residual_false_positive_mining|counterexample_mining|4C_thesis_break_timing_test", "trigger_type": "Stage3-Green-candidate", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 95800, "evidence_available_at_that_date": "Pre-PDUFA approval expectation and high public attention existed, but hard approval evidence was not yet available.", "evidence_source": "public expectation / company communication / stock-web OHLC", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["explicit_event_cap", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": -22.96, "MFE_90D_pct": 2.4, "MFE_180D_pct": 2.4, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -52.87, "MAE_90D_pct": -52.87, "MAE_180D_pct": -52.87, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 98100, "drawdown_after_peak_pct": -53.98, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "event_cap_should_block_green_without_hard_approval", "four_b_evidence_type": ["positioning_overheat", "explicit_event_cap"], "four_c_protection_label": "hard_4c_success_after_crl", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L14-G003", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L14-T007", "case_id": "R7L14-C23-HLB-028300-20240516", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_CRL_REDTEAM", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "BIO_APPROVAL_EVENT_RISK", "loop_objective": "4C_thesis_break_timing_test", "trigger_type": "Stage4C", "trigger_date": "2024-05-17", "entry_date": "2024-05-17", "entry_price": 67100, "evidence_available_at_that_date": "FDA Complete Response Letter / non-approval event broke the immediate approval thesis.", "evidence_source": "company/public CRL communication + stock-web OHLC", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap"], "stage4c_evidence_fields": ["regulatory_rejection", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.99, "MFE_90D_pct": 46.2, "MFE_180D_pct": 46.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -32.71, "MAE_90D_pct": -32.71, "MAE_180D_pct": -32.71, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 98100, "drawdown_after_peak_pct": -53.98, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": ["explicit_event_cap"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L14-G003-4C", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L14-C23-ALT-196170-20240223", "trigger_id": "R7L14-T001", "symbol": "196170", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 13, "customer_quality_score": 18, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 18, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 12, "relative_strength_score": 13, "customer_quality_score": 20, "policy_or_regulatory_score": 8, "valuation_repricing_score": 11, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green", "changed_components": ["contract_score", "customer_quality_score", "revision_score"], "component_delta_explanation": "C23 needs a platform-license conversion bonus when customer quality and commercial/royalty route are both visible; not a generic Stage2 bonus repeat.", "MFE_90D_pct": 127.52, "MAE_90D_pct": -9.3, "score_return_alignment_label": "current_profile_too_late_but_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L14-C23-YUHAN-000100-20240821", "trigger_id": "R7L14-T004", "symbol": "000100", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 11, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 14, "relative_strength_score": 15, "customer_quality_score": 18, "policy_or_regulatory_score": 20, "valuation_repricing_score": 8, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 15, "customer_quality_score": 18, "policy_or_regulatory_score": 22, "valuation_repricing_score": 8, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 91, "stage_label_after": "Stage3-Green", "changed_components": ["policy_or_regulatory_score", "revision_score"], "component_delta_explanation": "Hard FDA approval is a high-quality non-price trigger; current profile already works, but C23 ledger should distinguish hard approval from pre-approval expectation.", "MFE_90D_pct": 76.99, "MAE_90D_pct": -2.97, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L14-C23-HLB-028300-20240516", "trigger_id": "R7L14-T006", "symbol": "028300", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 18, "customer_quality_score": 8, "policy_or_regulatory_score": 15, "valuation_repricing_score": 15, "execution_risk_score": -6, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 87, "stage_label_before": "Stage3-Green-candidate", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 18, "customer_quality_score": 8, "policy_or_regulatory_score": 10, "valuation_repricing_score": 10, "execution_risk_score": -12, "legal_or_contract_risk_score": -10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 70, "stage_label_after": "Stage2-Watch / Event-cap blocked", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Pre-approval expectation with event-cap risk must not clear C23 Green unless hard approval or approvability evidence exists.", "MFE_90D_pct": 2.4, "MAE_90D_pct": -52.87, "score_return_alignment_label": "current_profile_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R7", "loop": "14", "scheduled_round": "R7", "scheduled_loop": 14, "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 1, "current_profile_error_count": 2, "tested_existing_calibrated_axes": ["stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["approval_expectation_false_positive", "green_too_late_for_platform_license_conversion", "price_only_4B_must_remain_overlay"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
{"row_type": "narrative_only", "case_id": "R7L14-C23-LCB-141080-20231227", "symbol": "141080", "company_name": "리가켐바이오", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_CRL_REDTEAM", "reason": "ADC platform licensing evidence exists, but profile flags corporate_action_candidate_date=2024-04-23 inside the entry~D+180 window; not used for weight calibration.", "price_source": "Songdaiki/stock-web", "usage": "coverage_context_only_not_weight_calibration", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/141/141080/2023.csv|atlas/ohlcv_tradable_by_symbol_year/141/141080/2024.csv", "profile_path": "atlas/symbol_profiles/141/141080.json"}
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
completed_loop = 14
next_round = R8
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json`.
- Stock-Web schema: `atlas/schema.json`.
- Stock-Web universe: `atlas/universe/all_symbols.csv`.
- Price rows used:
  - `atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/141/141080/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/141/141080/2024.csv`
- Profiles used:
  - `atlas/symbol_profiles/196/196170.json`
  - `atlas/symbol_profiles/000/000100.json`
  - `atlas/symbol_profiles/028/028300.json`
  - `atlas/symbol_profiles/141/141080.json`
- External evidence anchors:
  - FDA approved lazertinib with amivantamab-vmjw on 2024-08-19; content current as of 2024-08-20.
  - Public ALTEOGEN/MSD-linked platform-license amendment coverage around 2024-02-22.
  - Public HLB CRL / FDA non-approval communication around 2024-05-17.
  - LCB/Legochem ADC platform license context is narrative only in this loop due stock-web corporate-action caveat.


