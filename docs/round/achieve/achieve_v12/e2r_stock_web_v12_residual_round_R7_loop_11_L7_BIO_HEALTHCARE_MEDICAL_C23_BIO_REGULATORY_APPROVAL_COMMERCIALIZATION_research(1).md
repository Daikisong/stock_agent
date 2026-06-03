# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "scheduled_round": "R7",
  "scheduled_loop": 11,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 11,
  "computed_next_round": "R8",
  "computed_next_loop": 11,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
  "fine_archetype_id": "FDA_APPROVAL_COMMERCIALIZATION_DIRECT_ECONOMICS_VS_BINARY_REGULATORY_REJECTION_AND_CO_DEVELOPER_HIGH_MAE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "residual_false_positive_mining",
    "residual_missed_structural_mining",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "4B_non_price_requirement_stress_test",
    "4C_thesis_break_timing_test",
    "green_strictness_stress_test"
  ],
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "new_symbol_count": 3,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 3,
  "new_trigger_family_count": 3,
  "calibration_usable_case_count": 3,
  "calibration_usable_trigger_count": 5,
  "positive_case_count": 1,
  "counterexample_count": 2,
  "current_profile_error_count": 4,
  "diversity_score_summary": "estimated +52; wrong_round_penalty=0; repeated_same_symbol_penalty=0 for representative rows; repeated_same_trigger_family_penalty accepted because Yuhan/Oscotec deliberately test direct-owner vs co-developer economics",
  "do_not_propose_new_weight_delta": false,
  "loop_contribution_label": "canonical_archetype_rule_candidate"
}
```

This loop adds 3 new independent cases, 2 counterexamples, and 4 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION.

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

This research does not patch `stock_agent`, does not inspect `src/e2r`, and does not alter production scoring. It writes shadow-only C23 residual rules.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R7
scheduled_loop = 11
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = FDA_APPROVAL_COMMERCIALIZATION_DIRECT_ECONOMICS_VS_BINARY_REGULATORY_REJECTION_AND_CO_DEVELOPER_HIGH_MAE
round_schedule_status = valid
round_sector_consistency = pass
```

The prior generated state was R6 / Loop 11, so the next scheduled round is R7 / Loop 11. R7 is constrained to L7_BIO_HEALTHCARE_MEDICAL and the selected canonical archetype is C23.

## 3. Previous Coverage / Duplicate Avoidance Check

This loop does not reuse the R6 financial cases or the R5 consumer cases. It also avoids the obvious but contaminated Celltrion/Zymfentra quantitative path because the stock-web profile flags a corporate-action candidate inside the relevant post-approval window.

```text
same_canonical_archetype_research = allowed
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_independent_case_ratio = 1.00
wrong_round_penalty = 0
schema_rematerialization_penalty = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_basis = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Profile checks:

| symbol | company | profile_path | corporate-action candidates relevant to selected window | selected window status |
|---:|---|---|---|---|
| 000100 | 유한양행 | atlas/symbol_profiles/000/000100.json | none inside 2024-08-20~D+180 | clean |
| 039200 | 오스코텍 | atlas/symbol_profiles/039/039200.json | none inside 2024-08-20~D+180 | clean |
| 028300 | HLB | atlas/symbol_profiles/028/028300.json | none inside 2024-05-16~D+180 | clean |
| 068270 | 셀트리온 | atlas/symbol_profiles/068/068270.json | 2024-01-12 overlaps Zymfentra post-approval window | narrative-only / blocked |

## 5. Historical Eligibility Gate

```text
trigger_date is historical = true
entry_date exists in stock-web tradable shard = true
forward 180D trading window available = true
required OHLC fields available = true
corporate_action_contaminated_180D_window = false for representative rows
calibration_usable = true for 000100 / 039200 / 028300 representative rows
```

2Y fields are present but `null` because the stock-web manifest max_date of 2026-02-20 does not provide full 504-trading-day windows for 2024 triggers.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| DIRECT_OWNER_PARTNER_CONFIRMED_FDA_APPROVAL_COMMERCIALIZATION | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Final approval plus direct economics and partner commercialization path can justify positive-stage promotion. |
| CO_DEVELOPER_APPROVAL_ECONOMICS_HIGH_MAE | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Same approval event can be a high-MAE counterexample when economics are indirect or already priced. |
| PDUFA_BINARY_REGULATORY_REJECTION_FALSE_GREEN | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Pre-PDUFA optimism is not final approval; unresolved regulatory/CMC risk should cap Green. |
| CRL_HARD_4C_ROUTE | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | A CRL/regulatory rejection is thesis-break evidence and routes to hard 4C. |

## 7. Case Selection Summary

| case_id | symbol | company | role | why selected |
|---|---:|---|---|---|
| R7L11_C23_000100_YUHAN_LAZCLUZE_APPROVAL_COMMERCIALIZATION_20240820 | 000100 | 유한양행 | positive / structural success | Clean direct approval-to-commercialization rerating case. |
| R7L11_C23_039200_OSCOTEC_CO_DEVELOPER_HIGH_MAE_APPROVAL_20240820 | 039200 | 오스코텍 | counterexample / high-MAE approval-linked case | Same approval event, but weaker economic ownership and high MAE. |
| R7L11_C23_028300_HLB_PRE_PDUFA_FALSE_GREEN_AND_CRL_20240516 | 028300 | HLB | counterexample / false Green + hard 4C | Pre-approval expectation collapsed after CRL/regulatory rejection. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
calibration_usable_case_count = 3
4B_case_count = 1
4C_case_count = 1
```

The C23 mechanism behaves like a hospital door with two locks. Clinical data opens the first lock; final regulatory approval and commercial economics open the second. Yuhan cleared both, so the price reacted like the corridor was open. Oscotec had a key to the same corridor but not the same room. HLB stood at the door before the second lock opened, and the CRL showed that the door had never actually opened.

## 9. Evidence Source Map

| symbol | evidence family | source status | use |
|---:|---|---|---|
| 000100 | FDA approval of Rybrevant/Lazcluze combination; direct originator/economics/commercialization path | FDA/J&J/Reuters public approval family; issuer economics need enrichment before production | quantitative positive |
| 039200 | same program approval linked to co-developer/royalty economics | public approval family; economics clarity/royalty ownership should be enriched before production | quantitative counterexample |
| 028300 | pre-PDUFA approval expectation followed by CRL/regulatory rejection | public CRL/regulatory-rejection family; issuer filing URL should be enriched before production | quantitative counterexample / 4C |
| 068270 | Zymfentra FDA approval | relevant but stock-web corporate-action overlap blocks quantitative calibration | narrative-only |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry_date | forward window |
|---:|---|---|---|---|
| 000100 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv | atlas/symbol_profiles/000/000100.json | 2024-08-20 | usable |
| 000100 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv | atlas/symbol_profiles/000/000100.json | 2024-08-29 | usable 4B overlay |
| 039200 | atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv | atlas/symbol_profiles/039/039200.json | 2024-08-20 | usable |
| 028300 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json | 2024-05-16 | usable |
| 028300 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json | 2024-05-17 | usable 4C overlay |

## 11. Case-by-Case Trigger Grid

| case | symbol | trigger | entry | entry_price | MFE_30 | MFE_90 | MFE_180 | MAE_30 | MAE_90 | MAE_180 | verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 유한양행 Lazcluze approval direct economics | 000100 | Stage3-Green | 2024-08-20 | 94,000 | +70.53% | +77.55% | +77.55% | -2.66% | -2.66% | -26.28% | direct approval commercialization success |
| 오스코텍 co-developer approval high MAE | 039200 | Stage2-Actionable | 2024-08-20 | 41,450 | +10.62% | +10.62% | +10.62% | -21.11% | -47.89% | -47.89% | co-developer economics counterexample |
| HLB pre-PDUFA false Green | 028300 | Stage3-Green-False | 2024-05-16 | 95,800 | +11.59% | +11.59% | +11.59% | -52.87% | -52.87% | -52.87% | unresolved binary regulatory risk |
| 유한양행 price-only local 4B overlay | 000100 | 4B price-only local peak | 2024-08-29 | 137,100 | +21.74% | +21.74% | +21.74% | -13.57% | -20.50% | -49.45% | local 4B too early |
| HLB CRL hard 4C overlay | 028300 | 4C-Hard | 2024-05-17 | 67,100 | +9.99% | +46.20% | +46.20% | -32.71% | -32.71% | -32.71% | partial hard-4C protection |


## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate rows only:

| metric | 000100 유한양행 | 039200 오스코텍 | 028300 HLB pre-PDUFA |
|---|---:|---:|---:|
| entry_price | 94,000 | 41,450 | 95,800 |
| MFE_30D_pct | +70.53 | +10.62 | +11.59 |
| MFE_90D_pct | +77.55 | +10.62 | +11.59 |
| MFE_180D_pct | +77.55 | +10.62 | +11.59 |
| MAE_30D_pct | -2.66 | -21.11 | -52.87 |
| MAE_90D_pct | -2.66 | -47.89 | -52.87 |
| MAE_180D_pct | -26.28 | -47.89 | -52.87 |

Aggregate interpretation:

```text
positive_direct_approval_MFE90_pct = +77.55
positive_direct_approval_MAE90_pct = -2.66
counterexample_avg_MFE90_pct = +11.11
counterexample_avg_MAE90_pct = -50.38
```

## 13. Current Calibrated Profile Stress Test

| case | likely current profile behavior | actual OHLC alignment | verdict |
|---|---|---|---|
| 유한양행 final FDA approval | might wait for later revision or generic commercial confirmation | +77.55% MFE90 / -2.66% MAE90 | current_profile_too_late |
| 오스코텍 co-developer linkage | may over-credit same approval event without economics attenuation | +10.62% MFE90 / -47.89% MAE90 | current_profile_false_positive |
| HLB pre-PDUFA expectation | may over-credit trial/regulatory expectation as Green before final FDA decision | +11.59% MFE90 / -52.87% MAE90 | current_profile_false_positive |
| HLB CRL 4C | hard regulatory rejection should route immediately to 4C | 4C after first CRL reaction still MAE90 -32.71 | current_profile_4C_too_late |
| 유한양행 local price blowoff | price-only local overheat before full observed approval-cycle peak | local proximity 0.84 / full proximity 0.59 | current_profile_4B_too_early |

Axis verdict:

```text
stage2_actionable_evidence_bonus = existing_axis_strengthened for final approval with direct economics
stage3_yellow_total_min = existing_axis_kept
stage3_green_total_min = existing_axis_weakened only for C23 final approval + direct commercialization economics
stage3_green_revision_min = existing_axis_weakened only when final approval/partner/commercialization proof is strong
stage3_cross_evidence_green_buffer = existing_axis_strengthened
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_strengthened
```

## 14. Stage2 / Yellow / Green Comparison

```text
Stage2 / Watch:
  clinical data or approval expectation without final regulatory decision

Stage2-Actionable:
  final approval path visible, but economics are indirect or commercialization ownership is unclear

Stage3-Yellow:
  final regulatory decision likely or positive, but launch/economics/revision bridge still incomplete

Stage3-Green:
  final regulatory approval + direct company economics + partner/customer commercialization route + low unresolved CMC/inspection risk

False Green guard:
  pre-PDUFA expectation, single-arm regulatory optimism, unresolved CMC/inspection risk, or indirect co-developer economics

4B overlay:
  price-only local blowoff is insufficient; full 4B needs event cap, valuation blowoff plus non-price deterioration, or commercialization/royalty/revision evidence weakening

4C:
  CRL, regulatory rejection, qualification failure, or explicit thesis evidence break
```

Green lateness:

| case | early actionable entry | later Green/proxy | full observed peak | green_lateness_ratio | read |
|---|---:|---:|---:|---:|---|
| 000100 유한양행 | 94,000 | 94,000 approval Green | 166,900 | 0.00 | final approval should be immediate C23 Green when economics are direct |
| 039200 오스코텍 | 41,450 | not promoted after guard | 45,850 | not_applicable | co-developer economics/overhang guard prevents false promotion |
| 028300 HLB | 95,800 | should not have been Green | 106,900 pre-event high | not_applicable | unresolved PDUFA/CMC risk caps Green |

## 15. 4B Local vs Full-window Timing Audit

| trigger | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---:|---|
| R7L11_T01B_YUHAN_20240829_PRICE_ONLY_LOCAL_4B_TOO_EARLY | 0.84 | 0.59 | price_only_local_4B_too_early |
| R7L11_T03_HLB_20240516_FALSE_GREEN_PRE_PDUFA_UNRESOLVED_REGULATORY_RISK | 1.00 | 1.00 | event_cap_4B_required_before_binary_regulatory_decision |

The Yuhan row says “do not turn every post-approval spike into a full 4B.” The HLB row says the opposite risk can also exist: when a binary regulatory event has not resolved, Green should be capped by an event-risk overlay before the decision.

## 16. 4C Protection Audit

| trigger | prior stage drawdown proxy | 4C entry MAE90 | protection label |
|---|---:|---:|---|
| HLB CRL 4C | -57.76% from pre-event peak to post-CRL low | -32.71% after 4C entry | partial_hard_4c_success |

The HLB CRL row is not a clean profit-capture row. It is a damage-control row. It shows why hard 4C should not wait for price confirmation after a regulatory rejection: the road is already broken.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
candidate_axis = final_regulatory_approval_direct_economics_vs_unresolved_binary_event_risk
```

Candidate rule:

```text
In L7 bio/healthcare, final approval with direct commercialization economics can promote faster than ordinary revision evidence, but pre-PDUFA optimism, unresolved CMC/inspection risk, and indirect co-developer economics should cap Green or block promotion.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
new_axis_proposed:
  - c23_final_approval_direct_commercial_economics_boost
  - c23_co_developer_economics_attenuation_guard
  - c23_unresolved_binary_pdufa_cmc_green_cap
  - c23_crl_hard_4c_immediate_route
```

## 19. Before / After Backtest Comparison

| profile | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | current representative | +33.25 | -34.47 | +33.25 | -42.35 | 0.67 | 1 | 1 | 0.00 | 0.92 | 0.80 | mixed; misses direct-approval positive and over-promotes binary/co-developer risk |
| P0b e2r_2_0_baseline_reference | 3 | baseline representative | +33.25 | -34.47 | +33.25 | -42.35 | 0.67 | 1 | 1 | 0.00 | 0.92 | 0.80 | worse; trial/regulatory expectation is too easily Green |
| P1 sector_specific_candidate_profile | 3 | final approval + direct economics only | +77.55 positive / +11.11 blocked | -2.66 positive / -50.38 blocked | +77.55 positive / +11.11 blocked | -26.28 positive / -50.38 blocked | 0.00 | 0 | 0 | 0.00 | 0.92 | 0.80 | better positive/counterexample separation |
| P2 canonical_archetype_candidate_profile | 3 | C23 final-approval boost + PDUFA/co-developer guard | +77.55 positive / +11.11 blocked | -2.66 positive / -50.38 blocked | +77.55 positive / +11.11 blocked | -26.28 positive / -50.38 blocked | 0.00 | 0 | 0 | 0.00 | 0.92 | 0.80 | best explanatory fit |
| P3 counterexample_guard_profile | 3 | guard only | +33.25 | -34.47 | +33.25 | -42.35 | 0.00 false-stage | 1 | 1 | 0.00 | 0.92 | 0.80 | safer, but under-promotes direct final approval |

## 20. Score-Return Alignment Matrix

| case | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE90/MAE90 | alignment |
|---|---:|---|---:|---|---|---|
| 000100 | 84.0 | Stage3-Yellow_high | 91.0 | Stage3-Green | +77.55 / -2.66 | direct final approval captured |
| 039200 | 76.0 | Stage2-Actionable_high_mae | 61.0 | Stage2-Watch_or_blocked | +10.62 / -47.89 | co-developer high-MAE guard works |
| 028300 | 88.0 | Stage3-Green_false | 38.0 | 4C-Hard | +11.59 / -52.87 | false Green rejected; CRL hard-4C route required |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | FDA_APPROVAL_COMMERCIALIZATION_DIRECT_ECONOMICS_VS_BINARY_REGULATORY_REJECTION_AND_CO_DEVELOPER_HIGH_MAE | 1 | 2 | 1 | 1 | 3 | 0 | 5 | 3 | 4 | true | true | C23 now has direct approval positive, co-developer economics high-MAE guard, unresolved PDUFA/CMC false-Green guard, and CRL hard-4C route. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 3
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
  - direct_approval_commercialization_missed_structural
  - co_developer_approval_high_mae_false_positive
  - pre_pdufa_false_green
  - crl_hard_4c_too_late
  - price_only_local_4b_too_early_after_approval
new_axis_proposed:
  - c23_final_approval_direct_commercial_economics_boost
  - c23_co_developer_economics_attenuation_guard
  - c23_unresolved_binary_pdufa_cmc_green_cap
  - c23_crl_hard_4c_immediate_route
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened:
  - stage3_green_total_min, only under C23 final approval + direct commercialization economics exception
  - stage3_green_revision_min, only when final approval/partner/commercialization proof is independently strong
existing_axis_kept:
  - stage3_yellow_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and raw/unadjusted price basis
- profile availability and corporate-action caveats for 000100, 039200, 028300
- representative entry prices from stock-web tradable shards
- 30D/90D/180D MFE/MAE calculations from stock-web OHLC rows
- clean 180D corporate-action windows for selected quantitative rows
- R7/L7/C23 schedule consistency
```

Not validated:

```text
- production stock_agent source code
- live watchlist or current candidates
- brokerage execution
- exact issuer-specific regulatory filing URLs for production promotion
- post-2026-02-20 price path
- full 2Y windows for 2024 trigger dates
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_final_approval_direct_commercial_economics_boost,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,+1,+1,"Final regulatory approval plus direct commercialization economics separated Yuhan from generic clinical-data watch","Yuhan MFE90 +77.55 / MAE90 -2.66","R7L11_T01_YUHAN_20240820_STAGE3_GREEN_FDA_APPROVAL_DIRECT_ECONOMICS",3,3,2,medium,canonical_shadow_only,"not production; issuer-specific economics URLs need enrichment"
shadow_weight,c23_co_developer_economics_attenuation_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,+1,+1,"Co-developer/royalty proxy should not inherit full direct-owner approval boost when economics clarity is weak","Oscotec MFE90 +10.62 / MAE90 -47.89","R7L11_T02_OSCOTEC_20240820_STAGE2_APPROVAL_CO_DEVELOPER_HIGH_MAE",3,3,2,medium,guardrail_shadow_only,"blocks approval-linked but high-MAE co-developer false positives"
shadow_weight,c23_unresolved_binary_pdufa_cmc_green_cap,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,+1,+1,"Before final FDA decision, unresolved PDUFA/CMC/inspection risk should cap Green and add 4B event-cap overlay","HLB pre-CRL MAE90 -52.87","R7L11_T03_HLB_20240516_FALSE_GREEN_PRE_PDUFA_UNRESOLVED_REGULATORY_RISK",3,3,2,high,canonical_shadow_only,"strengthens price-only blowoff and 4C routing; not production"
shadow_weight,c23_crl_hard_4c_immediate_route,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,+1,+1,"CRL/regulatory rejection is thesis-break evidence and should route to 4C without waiting for price confirmation","HLB 4C row: entry after CRL still MAE90 -32.71 but avoids pre-CRL -52.87 representative drawdown","R7L11_T03B_HLB_20240517_HARD_4C_CRL_REGULATORY_REJECTION",3,3,2,medium,4c_shadow_only,"4C protection row, not positive-stage row"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","min_date":"1995-05-02","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KONEX","KOSDAQ","KOSDAQ GLOBAL","KOSPI"],"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R7L11_C23_000100_YUHAN_LAZCLUZE_APPROVAL_COMMERCIALIZATION_20240820","symbol":"000100","company_name":"유한양행","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"DIRECT_OWNER_PARTNER_CONFIRMED_FDA_APPROVAL_COMMERCIALIZATION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L11_T01_YUHAN_20240820_STAGE3_GREEN_FDA_APPROVAL_DIRECT_ECONOMICS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"FDA approval plus partner commercialization path produced a large early MFE, but later drawdown shows 4B overlay must still be separated from approval-stage promotion.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Positive C23 direct-economics case: approval signal was stronger than generic clinical-data watch."}
{"row_type":"case","case_id":"R7L11_C23_039200_OSCOTEC_CO_DEVELOPER_HIGH_MAE_APPROVAL_20240820","symbol":"039200","company_name":"오스코텍","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CO_DEVELOPER_APPROVAL_ECONOMICS_HIGH_MAE","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"R7L11_T02_OSCOTEC_20240820_STAGE2_APPROVAL_CO_DEVELOPER_HIGH_MAE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Same approval event did not translate into durable rerating for a co-developer/royalty-economics proxy; high MAE argues against treating all linked beneficiaries equally.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample C23 case: approval event needs economic ownership/royalty clarity and liquidity/overhang checks."}
{"row_type":"case","case_id":"R7L11_C23_028300_HLB_PRE_PDUFA_FALSE_GREEN_AND_CRL_20240516","symbol":"028300","company_name":"HLB","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"PDUFA_BINARY_REGULATORY_REJECTION_FALSE_GREEN","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R7L11_T03_HLB_20240516_FALSE_GREEN_PRE_PDUFA_UNRESOLVED_REGULATORY_RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Pre-approval expectation without resolved CMC/inspection/regulatory evidence had catastrophic MAE after CRL; C23 needs an unresolved-binary-event guard.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample C23 case: likely approval narrative collapsed under hard 4C regulatory rejection."}
{"row_type":"trigger","trigger_id":"R7L11_T01_YUHAN_20240820_STAGE3_GREEN_FDA_APPROVAL_DIRECT_ECONOMICS","case_id":"R7L11_C23_000100_YUHAN_LAZCLUZE_APPROVAL_COMMERCIALIZATION_20240820","symbol":"000100","company_name":"유한양행","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"DIRECT_OWNER_PARTNER_CONFIRMED_FDA_APPROVAL_COMMERCIALIZATION","sector":"바이오·헬스케어·의료기기","primary_archetype":"BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","loop_objective":["coverage_gap_fill","counterexample_mining","residual_false_positive_mining","residual_missed_structural_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","green_strictness_stress_test"],"trigger_type":"Stage3-Green","trigger_date":"2024-08-20","evidence_available_at_that_date":"US FDA approval of the Rybrevant/Lazcluze combination created direct approval-to-commercialization evidence for the Korean originator/economics holder.","evidence_source":"FDA/J&J/Reuters approval and CRL event family; issuer-specific filing URLs should be enriched before production promotion; stock-web used only for OHLC","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility","durable_customer_confirmation","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-20","entry_price":94000,"MFE_30D_pct":70.53,"MFE_90D_pct":77.55,"MFE_180D_pct":77.55,"MFE_1Y_pct":77.55,"MFE_2Y_pct":null,"MAE_30D_pct":-2.66,"MAE_90D_pct":-2.66,"MAE_180D_pct":-26.28,"MAE_1Y_pct":-26.28,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-58.48,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L11_000100_20240820_94000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L11_T01B_YUHAN_20240829_PRICE_ONLY_LOCAL_4B_TOO_EARLY","case_id":"R7L11_C23_000100_YUHAN_LAZCLUZE_APPROVAL_COMMERCIALIZATION_20240820","symbol":"000100","company_name":"유한양행","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"DIRECT_OWNER_PARTNER_CONFIRMED_FDA_APPROVAL_COMMERCIALIZATION","sector":"바이오·헬스케어·의료기기","primary_archetype":"BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","loop_objective":["coverage_gap_fill","counterexample_mining","residual_false_positive_mining","residual_missed_structural_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","green_strictness_stress_test"],"trigger_type":"4B-PriceOnlyLocalPeak","trigger_date":"2024-08-29","evidence_available_at_that_date":"The first post-approval price blowoff looked locally stretched, but the full observed approval cycle later peaked higher in October; price-only local 4B would have been too early.","evidence_source":"FDA/J&J/Reuters approval and CRL event family; issuer-specific filing URLs should be enriched before production promotion; stock-web used only for OHLC","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-29","entry_price":137100,"MFE_30D_pct":21.74,"MFE_90D_pct":21.74,"MFE_180D_pct":21.74,"MFE_1Y_pct":21.74,"MFE_2Y_pct":null,"MAE_30D_pct":-13.57,"MAE_90D_pct":-20.5,"MAE_180D_pct":-49.45,"MAE_1Y_pct":-49.45,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-58.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.84,"four_b_full_window_peak_proximity":0.59,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_too_early","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L11_000100_20240829_137100","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same Yuhan case, separate 4B timing overlay; not representative for aggregate entry","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R7L11_T02_OSCOTEC_20240820_STAGE2_APPROVAL_CO_DEVELOPER_HIGH_MAE","case_id":"R7L11_C23_039200_OSCOTEC_CO_DEVELOPER_HIGH_MAE_APPROVAL_20240820","symbol":"039200","company_name":"오스코텍","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CO_DEVELOPER_APPROVAL_ECONOMICS_HIGH_MAE","sector":"바이오·헬스케어·의료기기","primary_archetype":"BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","loop_objective":["coverage_gap_fill","counterexample_mining","residual_false_positive_mining","residual_missed_structural_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","green_strictness_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-08-20","evidence_available_at_that_date":"Same program approval was linked to a co-developer/royalty economics story, but ownership/economics clarity and overhang were weaker than direct-owner commercialization.","evidence_source":"FDA/J&J/Reuters approval and CRL event family; issuer-specific filing URLs should be enriched before production promotion; stock-web used only for OHLC","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv","profile_path":"atlas/symbol_profiles/039/039200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-20","entry_price":41450,"MFE_30D_pct":10.62,"MFE_90D_pct":10.62,"MFE_180D_pct":10.62,"MFE_1Y_pct":10.62,"MFE_2Y_pct":null,"MAE_30D_pct":-21.11,"MAE_90D_pct":-47.89,"MAE_180D_pct":-47.89,"MAE_1Y_pct":-47.89,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-21","peak_price":45850,"drawdown_after_peak_pct":-52.89,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L11_039200_20240820_41450","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L11_T03_HLB_20240516_FALSE_GREEN_PRE_PDUFA_UNRESOLVED_REGULATORY_RISK","case_id":"R7L11_C23_028300_HLB_PRE_PDUFA_FALSE_GREEN_AND_CRL_20240516","symbol":"028300","company_name":"HLB","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"PDUFA_BINARY_REGULATORY_REJECTION_FALSE_GREEN","sector":"바이오·헬스케어·의료기기","primary_archetype":"BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","loop_objective":["coverage_gap_fill","counterexample_mining","residual_false_positive_mining","residual_missed_structural_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","green_strictness_stress_test"],"trigger_type":"Stage3-Green-False","trigger_date":"2024-05-16","evidence_available_at_that_date":"Pre-PDUFA approval expectation was not equivalent to final regulatory approval; unresolved binary FDA/CMC/inspection risk remained.","evidence_source":"FDA/J&J/Reuters approval and CRL event family; issuer-specific filing URLs should be enriched before production promotion; stock-web used only for OHLC","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","explicit_event_cap","legal_or_regulatory_block","positioning_overheat"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-16","entry_price":95800,"MFE_30D_pct":11.59,"MFE_90D_pct":11.59,"MFE_180D_pct":11.59,"MFE_1Y_pct":11.59,"MFE_2Y_pct":null,"MAE_30D_pct":-52.87,"MAE_90D_pct":-52.87,"MAE_180D_pct":-52.87,"MAE_1Y_pct":-52.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":106900,"drawdown_after_peak_pct":-57.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"event_cap_4B_required_before_binary_regulatory_decision","four_b_evidence_type":["valuation_blowoff","legal_or_regulatory_block","positioning_overheat","control_premium_or_event_premium"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L11_028300_20240516_95800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L11_T03B_HLB_20240517_HARD_4C_CRL_REGULATORY_REJECTION","case_id":"R7L11_C23_028300_HLB_PRE_PDUFA_FALSE_GREEN_AND_CRL_20240516","symbol":"028300","company_name":"HLB","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"PDUFA_BINARY_REGULATORY_REJECTION_FALSE_GREEN","sector":"바이오·헬스케어·의료기기","primary_archetype":"BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","loop_objective":["coverage_gap_fill","counterexample_mining","residual_false_positive_mining","residual_missed_structural_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","green_strictness_stress_test"],"trigger_type":"4C-Hard","trigger_date":"2024-05-17","evidence_available_at_that_date":"FDA Complete Response Letter / regulatory rejection event converted unresolved approval risk into hard thesis break.","evidence_source":"FDA/J&J/Reuters approval and CRL event family; issuer-specific filing URLs should be enriched before production promotion; stock-web used only for OHLC","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","explicit_event_cap"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":67100,"MFE_30D_pct":9.99,"MFE_90D_pct":46.2,"MFE_180D_pct":46.2,"MFE_1Y_pct":46.2,"MFE_2Y_pct":null,"MAE_30D_pct":-32.71,"MAE_90D_pct":-32.71,"MAE_180D_pct":-32.71,"MAE_1Y_pct":-32.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-23","peak_price":98100,"drawdown_after_peak_pct":-53.98,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"partial_hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L11_028300_20240517_67100","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same HLB case, separate hard-4C protection timing; not representative for aggregate entry","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L11_C23_000100_YUHAN_LAZCLUZE_APPROVAL_COMMERCIALIZATION_20240820","trigger_id":"R7L11_T01_YUHAN_20240820_STAGE3_GREEN_FDA_APPROVAL_DIRECT_ECONOMICS","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":52,"relative_strength_score":76,"customer_quality_score":0,"policy_or_regulatory_score":78,"valuation_repricing_score":72,"execution_risk_score":42,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"regulatory_approval_score":82,"commercialization_score":68,"partner_quality_score":86,"royalty_or_profit_share_visibility_score":64,"clinical_data_quality_score":78,"pdufa_binary_event_risk_score":32,"cmc_or_inspection_risk_score":28,"co_developer_economics_clarity_score":70,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":84.0,"stage_label_before":"Stage3-Yellow_high","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":60,"relative_strength_score":82,"customer_quality_score":0,"policy_or_regulatory_score":88,"valuation_repricing_score":78,"execution_risk_score":38,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"regulatory_approval_score":96,"commercialization_score":88,"partner_quality_score":92,"royalty_or_profit_share_visibility_score":82,"clinical_data_quality_score":86,"pdufa_binary_event_risk_score":18,"cmc_or_inspection_risk_score":18,"co_developer_economics_clarity_score":86,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":91.0,"stage_label_after":"Stage3-Green","changed_components":["regulatory_approval_score","commercialization_score","partner_quality_score","royalty_or_profit_share_visibility_score"],"component_delta_explanation":"Final approval plus partner commercialization path deserves C23-specific Green promotion even before ordinary quarterly revision fully appears.","MFE_90D_pct":77.55,"MAE_90D_pct":-2.66,"score_return_alignment_label":"direct approval-to-commercialization captured","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L11_C23_039200_OSCOTEC_CO_DEVELOPER_HIGH_MAE_APPROVAL_20240820","trigger_id":"R7L11_T02_OSCOTEC_20240820_STAGE2_APPROVAL_CO_DEVELOPER_HIGH_MAE","symbol":"039200","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":42,"relative_strength_score":60,"customer_quality_score":0,"policy_or_regulatory_score":72,"valuation_repricing_score":68,"execution_risk_score":58,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"regulatory_approval_score":84,"commercialization_score":50,"partner_quality_score":80,"royalty_or_profit_share_visibility_score":44,"clinical_data_quality_score":76,"pdufa_binary_event_risk_score":28,"cmc_or_inspection_risk_score":24,"co_developer_economics_clarity_score":40,"positioning_overheat_score":70,"thesis_break_score":0},"weighted_score_before":76.0,"stage_label_before":"Stage2-Actionable_high_mae","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":36,"relative_strength_score":42,"customer_quality_score":0,"policy_or_regulatory_score":72,"valuation_repricing_score":48,"execution_risk_score":72,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"regulatory_approval_score":78,"commercialization_score":38,"partner_quality_score":74,"royalty_or_profit_share_visibility_score":28,"clinical_data_quality_score":72,"pdufa_binary_event_risk_score":24,"cmc_or_inspection_risk_score":22,"co_developer_economics_clarity_score":22,"positioning_overheat_score":84,"thesis_break_score":0},"weighted_score_after":61.0,"stage_label_after":"Stage2-Watch_or_blocked","changed_components":["co_developer_economics_clarity_score","royalty_or_profit_share_visibility_score","execution_risk_score","positioning_overheat_score"],"component_delta_explanation":"Co-developer approval linkage without direct commercialization economics should not inherit the direct-owner C23 boost.","MFE_90D_pct":10.62,"MAE_90D_pct":-47.89,"score_return_alignment_label":"high-MAE counterexample blocked","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L11_C23_028300_HLB_PRE_PDUFA_FALSE_GREEN_AND_CRL_20240516","trigger_id":"R7L11_T03_HLB_20240516_FALSE_GREEN_PRE_PDUFA_UNRESOLVED_REGULATORY_RISK","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":48,"relative_strength_score":88,"customer_quality_score":0,"policy_or_regulatory_score":74,"valuation_repricing_score":86,"execution_risk_score":68,"legal_or_contract_risk_score":52,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"regulatory_approval_score":62,"commercialization_score":54,"partner_quality_score":64,"royalty_or_profit_share_visibility_score":52,"clinical_data_quality_score":70,"pdufa_binary_event_risk_score":78,"cmc_or_inspection_risk_score":72,"co_developer_economics_clarity_score":0,"positioning_overheat_score":88,"thesis_break_score":0},"weighted_score_before":88.0,"stage_label_before":"Stage3-Green_false","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":22,"relative_strength_score":24,"customer_quality_score":0,"policy_or_regulatory_score":42,"valuation_repricing_score":18,"execution_risk_score":92,"legal_or_contract_risk_score":94,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"regulatory_approval_score":8,"commercialization_score":4,"partner_quality_score":32,"royalty_or_profit_share_visibility_score":12,"clinical_data_quality_score":46,"pdufa_binary_event_risk_score":96,"cmc_or_inspection_risk_score":96,"co_developer_economics_clarity_score":0,"positioning_overheat_score":88,"thesis_break_score":96},"weighted_score_after":38.0,"stage_label_after":"4C-Hard","changed_components":["pdufa_binary_event_risk_score","cmc_or_inspection_risk_score","regulatory_approval_score","thesis_break_score"],"component_delta_explanation":"Unresolved binary PDUFA/CMC risk should cap Green and route CRL to hard 4C immediately.","MFE_90D_pct":11.59,"MAE_90D_pct":-52.87,"score_return_alignment_label":"false Green rejected / 4C required","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["direct_approval_commercialization_missed_structural","co_developer_approval_high_mae_false_positive","pre_pdufa_false_green","crl_hard_4c_too_late","price_only_local_4b_too_early_after_approval"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R7L11_C23_068270_CELLTRION_ZYMFENTRA_NARRATIVE_ONLY_CORPORATE_ACTION_BLOCK","symbol":"068270","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","reason":"Zymfentra FDA approval is relevant to C23, but the selected post-approval window overlaps a stock-web corporate-action candidate date in 2024-01-12; excluded from quantitative calibration.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 11
next_round = R8
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web manifest confirmed source_name=FinanceData/marcap, price_adjustment_status=raw_unadjusted_marcap, max_date=2026-02-20, tradable_row_count=14,354,401, and calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year.
- 000100 profile confirmed active-like KOSPI profile, available through 2026-02-20, corporate-action candidate dates only in 1997/1999/2020 for this selected 2024-2025 window.
- 039200 profile confirmed active-like KOSDAQ profile, available through 2026-02-20, corporate-action candidate dates not overlapping the selected 2024-2025 window.
- 028300 profile confirmed active-like KOSDAQ profile, available through 2026-02-20, corporate-action candidate dates not overlapping the selected 2024-2025 window.
- 068270 Celltrion was considered for C23 Zymfentra approval, but excluded from quantitative rows because stock-web profile flags a 2024-01-12 corporate-action candidate overlapping the post-approval window.
- Evidence-source enrichment note: Yuhan/J&J Lazcluze approval is supported by FDA/J&J/Reuters public coverage; HLB CRL is treated as the public May 2024 CRL/regulatory rejection event but should receive issuer/filing URL enrichment before any production promotion.

