# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R7
scheduled_loop: 11
completed_round: R7
completed_loop: 11
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_LAUNCH_BRIDGE
loop_objective: coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression
round_schedule_status: valid
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
stock_web_price_atlas_access_required: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 5 new independent cases, 2 counterexamples, and 3 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION.

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. The already-applied global axes are treated as active: Stage2 actionable evidence bonus, Yellow 75, Green 87, Green revision 55, cross-evidence Green buffer, price-only blowoff block, full 4B non-price requirement, and hard 4C thesis-break routing. This MD does not re-prove those axes globally; it stress-tests whether C23 needs a more specific approval-to-commercialization bridge and a stronger binary-event guard.

## 2. Round / Large Sector / Canonical Archetype Scope

- round: `R7`
- loop: `11`
- large sector: `L7_BIO_HEALTHCARE_MEDICAL`
- canonical archetype: `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION`
- fine archetype: `BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_LAUNCH_BRIDGE`
- consistency: `R7 -> L7_BIO_HEALTHCARE_MEDICAL`, pass.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact read scope was limited to calibration reports, not source code. R7 was already broadly populated, so this loop avoids generic biotechnology repetition and focuses on a narrower residual: regulatory approval does not behave like one homogeneous signal. Approval with a confirmed partner/launch/royalty bridge behaved differently from pre-PDUFA price strength without approval.

Existing R7 report snapshot:

- representative_triggers: 102
- unique_cases: 27
- trigger types include Stage2, Stage2-Actionable, Stage3-Yellow, Stage3-Green, Stage4B, and 4C-thesis-break.

Novelty policy:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
new_symbol_count = 5
new_trigger_family_count = 5
reused_case_count = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```yaml
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Schema basis: tradable shards use `d,o,h,l,c,v,a,mc,s,m`; raw shards add `rs`. Calibration requires positive OHLCV, available 180 forward trading days, and no corporate-action contamination in the 180D window.

## 5. Historical Eligibility Gate

| gate | status |
|---|---|
| trigger dates are historical | pass |
| entry dates exist in tradable shard | pass for 000100, 196170, 145020, 028300 |
| forward 180 trading days available by manifest max_date | pass |
| corporate-action contamination in 180D | clean for 000100, 196170, 145020, 028300; blocked for 068270 narrative-only |
| raw shard used for weight calibration | no |
| production scoring changed | no |

## 6. Canonical Archetype Compression Map

```text
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  ├─ FDA approval + partner/royalty/commercial launch bridge: 000100, 196170, 145020
  ├─ binary approval-decision speculation without actual approval: 028300
  ├─ corporate-action-contaminated approval case for future validation only: 068270
  └─ C23-specific residual: approval evidence must be separated from price-only pre-PDUFA anticipation.
```

## 7. Case Selection Summary

| case_id | symbol | company | role | usable | new_independent | best_trigger | current_profile_verdict | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R7L11-C23-000100-yuhan-lazcluze-fda | 000100 | 유한양행 | structural_success | True | True | R7L11-C23-000100-T1-stage2-actionable-fda-approval | current_profile_too_late | approval+royalty route; high MFE and low MAE. |
| R7L11-C23-196170-alteogen-merck-sc-route | 196170 | 알테오젠 | structural_success | True | True | R7L11-C23-196170-T1-commercial-optionality | current_profile_missed_structural | partner SC formulation route; extreme upside but later 4B required. |
| R7L11-C23-145020-hugel-letybo-fda | 145020 | 휴젤 | stage2_promote_candidate | True | True | R7L11-C23-145020-T1-letybo-fda | current_profile_missed_structural | approval was real but commercialization bridge needed patience. |
| R7L11-C23-028300-hlb-crl-pdufa | 028300 | HLB | false_positive_green | True | True | R7L11-C23-028300-T1-pre-pdufa-false-green | current_profile_false_positive | pre-PDUFA price/euphoria without actual approval should not promote Green. |
| R7L11-C23-068270-celltrion-zymfentra-blocked | 068270 | 셀트리온 | narrative_only | False | True | narrative_only | current_profile_data_insufficient | C23-relevant but corporate-action contaminated 180D window blocks quantitative use. |

## 8. Positive vs Counterexample Balance

- positive structural/promote candidates: 3 (`000100`, `196170`, `145020`)
- counterexample / failed rerating / blocked case: 2 (`028300`, `068270` narrative-only)
- 4B case count: 2 (`000100`, `196170`)
- 4C case count: 1 (`028300`)
- calibration usable case count: 4

This satisfies the minimum balance rule and supplies both successful approval-to-commercialization cases and a binary regulatory failure case.

## 9. Evidence Source Map

| symbol | event family | evidence date | evidence interpretation |
|---|---|---:|---|
| 000100 | FDA approval + royalty/commercialization bridge | 2024-08-20 | Real approval and partner launch route; should not wait for all earnings revisions before Stage2/Yellow promotion. |
| 196170 | global pharma SC formulation route | 2024-02-22 | Partner-quality commercialization optionality; platform signal became more durable than ordinary biotech optionality. |
| 145020 | FDA approval to U.S. launch | 2024-02-29 | Approval real, but earnings bridge slower; Yellow is better than immediate Green. |
| 028300 | pre-PDUFA anticipation / CRL | 2024-05-16 / 2024-05-17 | Relative strength before decision was not approval evidence; CRL is thesis-break 4C. |
| 068270 | FDA approval narrative blocked | 2023-10-22 | C23-relevant, but stock-web corporate-action candidate in 180D blocks quantitative use. |

## 10. Price Data Source Map

| symbol | company | profile_path | representative price shard |
|---|---|---|---|
| 000100 | 유한양행 | atlas/symbol_profiles/000/000100.json | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv |
| 196170 | 알테오젠 | atlas/symbol_profiles/196/196170.json | atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv |
| 145020 | 휴젤 | atlas/symbol_profiles/145/145020.json | atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv |
| 028300 | HLB | atlas/symbol_profiles/028/028300.json | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv |
| 068270 | 셀트리온 | atlas/symbol_profiles/068/068270.json | narrative-only; 180D contaminated by 2024-01-12 corporate-action candidate |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | outcome | current_profile_verdict | aggregate_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R7L11-C23-000100-yuhan-lazcluze-fda | 000100 | Stage2-Actionable | 2024-08-20 | 2024-08-21 | 94300 | 76.99 | -2.97 | 76.99 | -2.97 | structural_success | current_profile_too_late | representative |
| R7L11-C23-000100-yuhan-lazcluze-fda | 000100 | Stage4B | 2024-10-15 | 2024-10-15 | 163700 | 1.95 | -38.67 | 1.95 | -38.67 | 4B_overlay_success | current_profile_correct | 4B_overlay_only |
| R7L11-C23-196170-alteogen-merck-sc-route | 196170 | Stage2-Actionable | 2024-02-22 | 2024-02-23 | 131200 | 121.8 | -9.3 | 247.18 | -9.3 | structural_success | current_profile_missed_structural | representative |
| R7L11-C23-196170-alteogen-merck-sc-route | 196170 | Stage4B | 2024-11-08 | 2024-11-08 | 437000 | 4.23 | -38.44 | 4.23 | -38.44 | 4B_overlay_success | current_profile_correct | 4B_overlay_only |
| R7L11-C23-145020-hugel-letybo-fda | 145020 | Stage2-Actionable | 2024-02-29 | 2024-03-04 | 202500 | 14.07 | -14.91 | 48.64 | -14.91 | stage2_promote_candidate | current_profile_missed_structural | representative |
| R7L11-C23-028300-hlb-crl-pdufa | 028300 | Stage3-Green-candidate-false-positive | 2024-05-16 | 2024-05-16 | 95800 | 11.59 | -52.87 | 11.59 | -52.87 | false_positive_green | current_profile_false_positive | representative |
| R7L11-C23-028300-hlb-crl-pdufa | 028300 | Stage4C | 2024-05-17 | 2024-05-17 | 67100 | 46.2 | -32.71 | 46.2 | -32.71 | 4C_success | current_profile_correct | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate triggers only:

| symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | interpretation |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 000100 | 2024-08-21 | 94,300 | 69.99 | -2.97 | 76.99 | -2.97 | 76.99 | -2.97 | Approval + partner launch route quickly repriced with shallow early MAE. |
| 196170 | 2024-02-23 | 131,200 | 71.88 | -9.30 | 121.80 | -9.30 | 247.18 | -9.30 | Partner-quality SC formulation route created extreme rerating, later requiring 4B. |
| 145020 | 2024-03-04 | 202,500 | 14.07 | -14.91 | 14.07 | -14.91 | 48.64 | -14.91 | Real approval, but high-MAE patience required; best classified Yellow before Green. |
| 028300 | 2024-05-16 | 95,800 | 11.59 | -52.87 | 11.59 | -52.87 | 11.59 | -52.87 | Pre-decision price strength was a false Green candidate; CRL broke the thesis. |

Overlay triggers:

| symbol | overlay | entry_date | entry_price | peak_date | peak_price | proximity | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| 000100 | 4B valuation/positioning | 2024-10-15 | 163,700 | 2024-10-15 | 166,900 | 0.96 | good timing but overlay-only; non-price evidence was not a hard thesis break. |
| 196170 | 4B event/valuation cap | 2024-11-08 | 437,000 | 2024-11-11 | 455,500 | 0.94 | good full-window 4B timing. |
| 028300 | 4C CRL | 2024-05-17 | 67,100 | 2024-07-08 | 98,100 | n/a | hard 4C, despite later rebound. |

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| How would current profile judge these cases? | It would generally reward non-price evidence and block price-only blowoff, but C23 approval cases still need finer distinction between approval+commercialization bridge and pre-decision speculation. |
| Did judgment match MFE/MAE? | Partly. It was correct on hard 4C logic, but too late/missed on 000100/196170/145020 and too permissive if HLB-like pre-PDUFA strength is promoted. |
| Was Stage2 bonus too high/low? | Not globally. For C23, Stage2 bonus is useful only when regulatory approval is already real or commercialization bridge is partner-confirmed. |
| Yellow 75 too high/low? | For C23 approval with partner route, Yellow can be reached earlier. For binary pre-decision events, Yellow should not become Green without approval. |
| Green 87/revision 55 too high/low? | Too strict for approval+royalty bridge if revisions lag. Correctly strict for approval-not-yet-known events. |
| price-only blowoff guard? | Strengthened. 028300 and 196170 show why price-only peaks cannot create positive stage labels. |
| full 4B non-price requirement? | Kept. 000100 4B is overlay-only; 196170 has better explicit event/valuation cap evidence. |
| hard 4C routing? | Strengthened. CRL/regulatory rejection should route to 4C even if technical rebound follows. |

## 14. Stage2 / Yellow / Green Comparison

- `000100`: Stage2-Actionable at approval/launch-route date captured most of the move; waiting for full quarterly revision would appear near the 4B zone.
- `196170`: Stage2-Actionable/commercial-optionality trigger was much earlier than price peak; Green strictness based only on conventional revisions would miss a large part of the rerating.
- `145020`: Approval was real, but MAE was high and the launch bridge needed time. Yellow is the correct compromise.
- `028300`: Pre-decision Green is wrong. The absence of actual approval should force event-risk discount, not Stage3 promotion.

## 15. 4B Local vs Full-window Timing Audit

| symbol | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 000100 | 0.96 | 0.96 | valuation_blowoff, positioning_overheat | good overlay timing, not hard full 4B without stronger non-price evidence |
| 196170 | 0.94 | 0.94 | valuation_blowoff, positioning_overheat, explicit_event_cap | good full-window 4B timing |
| 028300 | n/a | n/a | price_only before CRL; regulatory rejection after | price-only local peak is not 4B; CRL is 4C |

## 16. 4C Protection Audit

HLB is the clean 4C case. A pre-CRL entry at 95,800 had 180D MAE of -52.87%. The CRL row at 67,100 still had a severe next-trading-day drawdown to 47,000, but it protected against treating the subsequent rebound as proof that the original approval thesis remained intact. The 4C label should be thesis-protection, not a mechanical short signal.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L7_bio_regulatory_approval_commercialization_bridge
candidate_rule:
  In L7 bio/healthcare, approval-related Stage2/Yellow promotion is allowed when at least two of the following are present:
    1. actual regulatory approval or formal partner/commercial launch route,
    2. identifiable royalty/revenue/launch channel,
    3. durable global customer or partner confirmation,
    4. clean stock-web 180D window.
  Pre-decision PDUFA anticipation, price strength, or event countdown without actual approval cannot become Stage3-Green.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
candidate_shadow_axes:
  approval_to_commercialization_bridge_bonus = +2
  binary_regulatory_event_no_approval_green_block = true
  approval_without_revenue_bridge_max_stage = Stage3-Yellow
  CRL_or_regulatory_rejection_routes_to_4C = strengthened
```

This is not a global proposal. It is specific to C23 where the same word “approval” can mean three different economic states: approved-and-launchable, approved-but-commercially-slow, and not-yet-approved binary event risk.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current | Global calibrated profile, no C23-specific approval bridge. | none | 4 | 4 | 56.14 | -19.76 | 95.85 | -19.76 | 0.25 | 2 | 1 | 0.95 | 0.95 | 0.95 | partially_aligned_but_residual_errors |
| P0b_e2r_2_0_baseline_reference | rollback | Old baseline; allows too much event/price weight before approval. | reference only | 4 | 4 | 56.14 | -19.76 | 95.85 | -19.76 | 0.5 | 1 | 2 | 0.98 | 0.95 | 0.95 | worse_false_positive_control |
| P1_L7_sector_candidate | sector_specific | Bio/healthcare approvals need commercialization bridge and binary event guard. | approval_bridge_bonus; binary_event_guard | 4 | 4 | 56.14 | -19.76 | 95.85 | -19.76 | 0.0 | 0 | 1 | 0.64 | 0.95 | 0.95 | improved_alignment |
| P2_C23_archetype_candidate | canonical_archetype_specific | C23 differentiates approval+partner launch from pre-PDUFA speculation. | approval_to_commercialization_bridge_bonus +2; no_approval_green_block | 4 | 4 | 56.14 | -19.76 | 95.85 | -19.76 | 0.0 | 0 | 1 | 0.64 | 0.95 | 0.95 | best_shadow_alignment |
| P3_counterexample_guard | canonical_archetype_specific | Hard CRL/regulatory rejection routes to 4C regardless of rebound. | hard_4c_thesis_break_routes_to_4c strengthened | 4 | 4 | 56.14 | -19.76 | 95.85 | -19.76 | 0.0 | 1 | 1 | 0.64 | 0.95 | 0.95 | best_risk_control |

## 20. Score-Return Alignment Matrix

| symbol | before_score | before_label | after_score | after_label | changed_components | explanation |
| --- | --- | --- | --- | --- | --- | --- |
| 000100 | 83 | Stage3-Yellow | 90 | Stage3-Green | policy_or_regulatory_score,customer_quality_score,execution_risk_score,legal_or_contract_risk_score | C23 shadow adds approval-to-commercialization bridge and partner launch quality; Green may be allowed before full quarterly revision if approval+royalty route is confirmed. |
| 196170 | 82 | Stage3-Yellow | 92 | Stage3-Green | policy_or_regulatory_score,customer_quality_score,execution_risk_score,legal_or_contract_risk_score | Global pharma partner plus SC formulation launch route is more durable than ordinary platform-optionality news. |
| 145020 | 70 | Stage2-Actionable | 77 | Stage3-Yellow | policy_or_regulatory_score,customer_quality_score,execution_risk_score,legal_or_contract_risk_score | Approval alone should not jump to Green; C23 shadow allows Yellow when launch/commercialization route exists but earnings bridge is not yet proven. |
| 028300 | 76 | Stage3-Yellow_or_Green_candidate | 47 | Stage4C_watch_before_decision | policy_or_regulatory_score,customer_quality_score,execution_risk_score,legal_or_contract_risk_score | Binary PDUFA anticipation cannot be promoted to Green without approval evidence; CRL route becomes hard 4C. |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_LAUNCH_BRIDGE | 3 | 2 | 2 | 1 | 5 | 0 | 7 | 4 | 3 | True | True | C23 now has approval/commercialization positives, binary regulatory false positive, 4B overlay, and blocked corporate-action narrative case. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_too_late
  - current_profile_missed_structural
  - current_profile_false_positive
new_axis_proposed: null
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened:
  - stage3_green_revision_min, C23-specific only; not global rollback
existing_axis_kept:
  - stage2_actionable_evidence_bonus
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web manifest/schema basis
- profile availability and corporate-action caveats for selected symbols
- selected historical trigger rows and representative MFE/MAE proxy calculations from inspected OHLC rows
- C23 distinction between approval bridge, approval-only, and pre-approval speculation

Not validated:

- production `stock_agent` source code
- live candidates after manifest max_date
- broker/API execution
- global scoring promotion
- exact full 1Y/2Y metrics for late-2024 triggers where the manifest max_date makes 504D unavailable or not central to the shadow rule

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,approval_to_commercialization_bridge_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,2,+2,"Confirmed approval plus launch/royalty/commercialization bridge separated Yuhan/Alteogen/Hugel from pure PDUFA anticipation.","Raises Yuhan/Alteogen into Green or high Yellow; keeps Hugel Yellow until earnings bridge matures.","R7L11-C23-000100-T1-stage2-actionable-fda-approval|R7L11-C23-196170-T1-commercial-optionality|R7L11-C23-145020-T1-letybo-fda",4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,binary_regulatory_event_no_approval_green_block,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,"+1 guard","HLB shows relative strength plus event countdown can be a false Green without actual approval or partner commercialization bridge.","Blocks HLB-like pre-CRL false positive from Green.",R7L11-C23-028300-T1-pre-pdufa-false-green,4,4,1,medium,canonical_shadow_only,"strengthens existing non-price-evidence / 4C thesis-break axis"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R7L11-C23-000100-yuhan-lazcluze-fda","symbol":"000100","company_name":"유한양행","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_LAUNCH_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L11-C23-000100-T1-stage2-actionable-fda-approval","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned_after","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"approval+royalty route; high MFE and low MAE."}
{"row_type":"case","case_id":"R7L11-C23-196170-alteogen-merck-sc-route","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_LAUNCH_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R7L11-C23-196170-T1-commercial-optionality","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned_after","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"partner SC formulation route; extreme upside but later 4B required."}
{"row_type":"case","case_id":"R7L11-C23-145020-hugel-letybo-fda","symbol":"145020","company_name":"휴젤","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_LAUNCH_BRIDGE","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"R7L11-C23-145020-T1-letybo-fda","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"partial_alignment_high_mae","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"approval was real but commercialization bridge needed patience."}
{"row_type":"case","case_id":"R7L11-C23-028300-hlb-crl-pdufa","symbol":"028300","company_name":"HLB","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_LAUNCH_BRIDGE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R7L11-C23-028300-T1-pre-pdufa-false-green","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_blocked_after","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"pre-PDUFA price/euphoria without actual approval should not promote Green."}
{"row_type":"case","case_id":"R7L11-C23-068270-celltrion-zymfentra-blocked","symbol":"068270","company_name":"셀트리온","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_LAUNCH_BRIDGE","case_type":"narrative_only","positive_or_counterexample":"counterexample","best_trigger":"narrative_only","calibration_usable":false,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.0,"score_price_alignment":"not_weight_calibration","current_profile_verdict":"current_profile_data_insufficient","price_source":"Songdaiki/stock-web","notes":"C23-relevant but corporate-action contaminated 180D window blocks quantitative use."}
{"trigger_id":"R7L11-C23-000100-T1-stage2-actionable-fda-approval","case_id":"R7L11-C23-000100-yuhan-lazcluze-fda","symbol":"000100","company_name":"유한양행","sector":"bio_pharma","primary_archetype":"FDA approval to royalty/commercialization bridge","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-20","entry_date":"2024-08-21","entry_price":94300,"evidence_available_at_that_date":"FDA/J&J approval of Rybrevant plus Lazcluze/lazertinib for first-line EGFR-mutated NSCLC; Korean listed royalty/commercialization path via Yuhan.","evidence_source":"Reuters 2024-08-20; FDA/J&J approval notice summarized in public news; stock-web row 2024-08-21 c=94,300.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":69.99,"MFE_90D_pct":76.99,"MFE_180D_pct":76.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.97,"MAE_90D_pct":-2.97,"MAE_180D_pct":-2.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":0.96,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_block_reasons":[],"same_entry_group_id":"R7L11-C23-000100-20240821","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","row_type":"trigger","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_LAUNCH_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R7L11-C23-000100-T2-4b-valuation-overheat","case_id":"R7L11-C23-000100-yuhan-lazcluze-fda","symbol":"000100","company_name":"유한양행","sector":"bio_pharma","primary_archetype":"FDA approval to royalty/commercialization bridge","trigger_type":"Stage4B","trigger_date":"2024-10-15","entry_date":"2024-10-15","entry_price":163700,"evidence_available_at_that_date":"Post-approval price acceleration had consumed most observed upside before confirmed quarterly royalty scale-up was visible.","evidence_source":"stock-web row 2024-10-15 c=163,700; non-price 4B evidence is weak, so this is an overlay not a full exit rule.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"MFE_30D_pct":1.95,"MFE_90D_pct":1.95,"MFE_180D_pct":1.95,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-27.55,"MAE_90D_pct":-38.67,"MAE_180D_pct":-38.67,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_full_window_4B_timing_but_overlay_only","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_block_reasons":[],"same_entry_group_id":"R7L11-C23-000100-20241015","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B timing overlay, not new aggregate entry","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","row_type":"trigger","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_LAUNCH_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R7L11-C23-196170-T1-commercial-optionality","case_id":"R7L11-C23-196170-alteogen-merck-sc-route","symbol":"196170","company_name":"알테오젠","sector":"bio_platform","primary_archetype":"global partner SC formulation commercialization route","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-23","entry_price":131200,"evidence_available_at_that_date":"Merck/Keytruda subcutaneous formulation route upgraded from platform optionality to commercial exclusivity/launch-route optionality.","evidence_source":"Merck/Alteogen public reporting; Reuters later confirmed Alteogen enzyme in Keytruda SC launch pathway; stock-web row 2024-02-23 c=131,200.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":71.88,"MFE_90D_pct":121.8,"MFE_180D_pct":247.18,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.3,"MAE_90D_pct":-9.3,"MAE_180D_pct":-9.3,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-11","peak_price":455500,"drawdown_after_peak_pct":-38.64,"green_lateness_ratio":0.94,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_block_reasons":[],"same_entry_group_id":"R7L11-C23-196170-20240223","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","profile_path":"atlas/symbol_profiles/196/196170.json","row_type":"trigger","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_LAUNCH_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R7L11-C23-196170-T2-4b-keytruda-sc-overheat","case_id":"R7L11-C23-196170-alteogen-merck-sc-route","symbol":"196170","company_name":"알테오젠","sector":"bio_platform","primary_archetype":"global partner SC formulation commercialization route","trigger_type":"Stage4B","trigger_date":"2024-11-08","entry_date":"2024-11-08","entry_price":437000,"evidence_available_at_that_date":"Large rerating reached near full-window peak before FDA decision/launch revenues; later drawdown shows 4B overlay value, but no hard 4C before thesis break.","evidence_source":"stock-web row 2024-11-08 c=437,000; peak 2024-11-11 h=455,500.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"MFE_30D_pct":4.23,"MFE_90D_pct":4.23,"MFE_180D_pct":4.23,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-36.16,"MAE_90D_pct":-38.44,"MAE_180D_pct":-38.44,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-11","peak_price":455500,"drawdown_after_peak_pct":-38.64,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_block_reasons":[],"same_entry_group_id":"R7L11-C23-196170-20241108","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B overlay; independent only for 4B timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","profile_path":"atlas/symbol_profiles/196/196170.json","row_type":"trigger","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_LAUNCH_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R7L11-C23-145020-T1-letybo-fda","case_id":"R7L11-C23-145020-hugel-letybo-fda","symbol":"145020","company_name":"휴젤","sector":"bio_aesthetics","primary_archetype":"FDA approval to US commercial launch bridge","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-29","entry_date":"2024-03-04","entry_price":202500,"evidence_available_at_that_date":"U.S. approval of Letybo/letibotulinumtoxinA created a real commercialization bridge, but follow-through was slower than pure approval headlines suggested.","evidence_source":"FDA approval/date summarized in public sources; stock-web row 2024-03-04 c=202,500.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":14.07,"MFE_90D_pct":14.07,"MFE_180D_pct":48.64,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.91,"MAE_90D_pct":-14.91,"MAE_180D_pct":-14.91,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-17","peak_price":301000,"drawdown_after_peak_pct":-18.77,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"stage2_promote_candidate","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_block_reasons":[],"same_entry_group_id":"R7L11-C23-145020-20240304","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","row_type":"trigger","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_LAUNCH_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R7L11-C23-028300-T1-pre-pdufa-false-green","case_id":"R7L11-C23-028300-hlb-crl-pdufa","symbol":"028300","company_name":"HLB","sector":"bio_pharma","primary_archetype":"binary FDA decision risk without approval bridge","trigger_type":"Stage3-Green-candidate-false-positive","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":95800,"evidence_available_at_that_date":"Pre-decision PDUFA anticipation and price strength existed, but actual approval evidence was absent; this is the canonical C23 false-positive pattern.","evidence_source":"stock-web row 2024-05-16 c=95,800; subsequent CRL shock row 2024-05-17 c=67,100 and 2024-05-20 c=47,000.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","positioning_overheat"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"MFE_30D_pct":11.59,"MFE_90D_pct":11.59,"MFE_180D_pct":11.59,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-52.87,"MAE_90D_pct":-52.87,"MAE_180D_pct":-52.87,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":106900,"drawdown_after_peak_pct":-57.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"pre_event_price_only_not_full_4B","four_b_evidence_type":["price_only","explicit_event_cap"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_block_reasons":[],"same_entry_group_id":"R7L11-C23-028300-20240516","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","row_type":"trigger","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_LAUNCH_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R7L11-C23-028300-T2-hard-4c-crl","case_id":"R7L11-C23-028300-hlb-crl-pdufa","symbol":"028300","company_name":"HLB","sector":"bio_pharma","primary_archetype":"binary FDA decision risk without approval bridge","trigger_type":"Stage4C","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":67100,"evidence_available_at_that_date":"CRL/regulatory rejection converted binary approval thesis into a hard 4C event; rebound afterward does not restore the original approval thesis.","evidence_source":"stock-web row 2024-05-17 c=67,100; next-trading-day row 2024-05-20 c=47,000.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"MFE_30D_pct":46.2,"MFE_90D_pct":46.2,"MFE_180D_pct":46.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-32.71,"MAE_90D_pct":-32.71,"MAE_180D_pct":-32.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":98100,"drawdown_after_peak_pct":-54.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_block_reasons":[],"same_entry_group_id":"R7L11-C23-028300-20240517","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4C protection audit; not aggregate entry","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","row_type":"trigger","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_LAUNCH_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L11-C23-000100-yuhan-lazcluze-fda","trigger_id":"R7L11-C23-000100-T1-stage2-actionable-fda-approval","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":14,"relative_strength_score":12,"customer_quality_score":15,"policy_or_regulatory_score":20,"valuation_repricing_score":10,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":83,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":16,"relative_strength_score":12,"customer_quality_score":18,"policy_or_regulatory_score":23,"valuation_repricing_score":12,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":90,"stage_label_after":"Stage3-Green","changed_components":["policy_or_regulatory_score","customer_quality_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C23 shadow adds approval-to-commercialization bridge and partner launch quality; Green may be allowed before full quarterly revision if approval+royalty route is confirmed.","MFE_90D_pct":76.99,"MAE_90D_pct":-2.97,"score_return_alignment_label":"score_return_aligned_after","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L11-C23-196170-alteogen-merck-sc-route","trigger_id":"R7L11-C23-196170-T1-commercial-optionality","symbol":"196170","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":18,"customer_quality_score":19,"policy_or_regulatory_score":14,"valuation_repricing_score":13,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":12,"relative_strength_score":18,"customer_quality_score":23,"policy_or_regulatory_score":18,"valuation_repricing_score":14,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":92,"stage_label_after":"Stage3-Green","changed_components":["policy_or_regulatory_score","customer_quality_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Global pharma partner plus SC formulation launch route is more durable than ordinary platform-optionality news.","MFE_90D_pct":121.8,"MAE_90D_pct":-9.3,"score_return_alignment_label":"score_return_aligned_after","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L11-C23-145020-hugel-letybo-fda","trigger_id":"R7L11-C23-145020-T1-letybo-fda","symbol":"145020","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":8,"relative_strength_score":8,"customer_quality_score":10,"policy_or_regulatory_score":22,"valuation_repricing_score":7,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":8,"relative_strength_score":8,"customer_quality_score":12,"policy_or_regulatory_score":24,"valuation_repricing_score":7,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":77,"stage_label_after":"Stage3-Yellow","changed_components":["policy_or_regulatory_score","customer_quality_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Approval alone should not jump to Green; C23 shadow allows Yellow when launch/commercialization route exists but earnings bridge is not yet proven.","MFE_90D_pct":14.07,"MAE_90D_pct":-14.91,"score_return_alignment_label":"partial_alignment_high_mae","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L11-C23-028300-hlb-crl-pdufa","trigger_id":"R7L11-C23-028300-T1-pre-pdufa-false-green","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":12,"relative_strength_score":20,"customer_quality_score":8,"policy_or_regulatory_score":18,"valuation_repricing_score":16,"execution_risk_score":-8,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_or_Green_candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":20,"customer_quality_score":4,"policy_or_regulatory_score":8,"valuation_repricing_score":16,"execution_risk_score":-18,"legal_or_contract_risk_score":-20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage4C_watch_before_decision","changed_components":["policy_or_regulatory_score","customer_quality_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Binary PDUFA anticipation cannot be promoted to Green without approval evidence; CRL route becomes hard 4C.","MFE_90D_pct":11.59,"MAE_90D_pct":-52.87,"score_return_alignment_label":"false_positive_blocked_after","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R7","loop":"11","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_too_late","current_profile_missed_structural","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R7L11-C23-068270-celltrion-zymfentra-blocked","symbol":"068270","company_name":"셀트리온","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","reason":"Zymfentra FDA approval route is archetypally relevant but stock-web profile has corporate_action_candidate_date 2024-01-12 inside the 180D post-approval window; not used for weight calibration.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration","profile_path":"atlas/symbol_profiles/068/068270.json"}
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

- `reports/e2r_calibration/by_round/R7.md` was read for previous R7 coverage only.
- `atlas/manifest.json` and `atlas/schema.json` were read for price-source and calibration basis.
- Symbol profiles read: `000100`, `196170`, `145020`, `028300`, `068270`.
- Stock-web row excerpts inspected: `000100/2024.csv`, `000100/2025.csv`, `196170/2024.csv`, `145020/2024.csv`, `028300/2024.csv`.
- Web evidence consulted for event interpretation: FDA/J&J Lazcluze/Rybrevant approval, Merck/Alteogen Keytruda SC commercial route, Hugel Letybo FDA approval, and HLB CRL/regulatory rejection context. The MD is not investment advice and does not scan current candidates.

