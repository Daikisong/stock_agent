# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R7
scheduled_loop: 72
completed_round: R7
completed_loop: 72
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: FDA_APPROVAL_COMMERCIALIZATION_ROYALTY_ROUTE__VS__CRL_THESIS_BREAK
output_file: e2r_stock_web_v12_residual_round_R7_loop_72_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
stock_web_price_atlas_access_required: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION.

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`. The existing global axes are treated as already applied, not re-proposed globally:

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

R7/C23 is a useful stress surface because the price path often moves before final approval, but a single CRL can invert the thesis in one trading session. In this archetype, the score engine should behave like a lock with two keys: the first key is a regulatory event, but the second key must be commercialization/partner/royalty visibility. RS alone is not enough.

## 2. Round / Large Sector / Canonical Archetype Scope

```yaml
scheduled_round: R7
scheduled_loop: 72
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
round_sector_gate: pass
next_round: R8
next_loop: 72
```

R7 maps to `L7_BIO_HEALTHCARE_MEDICAL`; C23 covers regulatory approval to commercialization. This file therefore does not touch platform, finance, construction, current/live candidates, stock_agent code, or production scoring.

## 3. Previous Coverage / Duplicate Avoidance Check

Schedule was continued from the immediately preceding local R6/Loop 72 output. No `src/e2r` path was opened. Duplicate avoidance used the v12 hard key discipline: `canonical_archetype_id + symbol + trigger_type + entry_date`. The selected symbols and trigger families are new for this R7/Loop 72 run:

- `000100` approval/commercialization bridge via priority-review route.
- `039200` royalty/licensing route with approval-day lateness stress.
- `028300` unresolved PDUFA expectation false positive and CRL hard-4C overlay.
- `140410` narrative-only CRL example blocked by stock-web corporate-action contamination.

The loop is not schema rematerialization because it adds new symbols, a new approval/royalty bridge split, and a CRL guard counterexample for C23.

## 4. Stock-Web OHLC Input / Price Source Validation

```yaml
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_path: atlas/manifest.json
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
manifest_max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

The stock-web schema uses `d,o,h,l,c,v,a,mc,s,m` for tradable shards and adds `rs` for raw row status. This loop uses only tradable shards for MFE/MAE; raw rows are not used for calibration weights. Corporate-action contaminated windows are blocked by default.

## 5. Historical Eligibility Gate

| symbol | company | profile_path | forward_180D_available | corporate_action_window_status | calibration status |
|---|---|---|---|---|---|
| 000100 | 유한양행 | atlas/symbol_profiles/000/000100.json | true | clean_2024_180D_window | usable |
| 039200 | 오스코텍 | atlas/symbol_profiles/039/039200.json | true | clean_2024_180D_window | usable |
| 028300 | HLB | atlas/symbol_profiles/028/028300.json | true | clean_2024_180D_window | usable |
| 140410 | 메지온 | atlas/symbol_profiles/140/140410.json | true | corporate_action_contaminated_180D_window | narrative_only |

메지온 is intentionally retained as narrative-only because the profile marks 2022-04-05 and 2022-04-25 as corporate-action candidate dates. Those overlap the post-CRL forward window, so the case is not allowed to vote on weight calibration.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression rule |
|---|---|---|
| FDA_PRIORITY_REVIEW_TO_APPROVAL_DIRECT_COMMERCIALIZATION | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Positive bridge if partner/sponsor quality and commercialization route exist before formal approval. |
| FDA_APPROVAL_ROYALTY_ROUTE | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Positive bridge if royalty path is contractually meaningful, but approval-day Green can be late. |
| UNRESOLVED_PDUFA_EXPECTATION_PRICE_RUN | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Do not promote to Green without approval or durable commercial conversion evidence. |
| CRL_REGULATORY_REJECTION_THESIS_BREAK | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Hard 4C thesis break; prior MFE cannot defend the score. |

## 7. Case Selection Summary

| case_id | symbol | company | role | calibration_usable | new_independent | evidence family | reason selected |
|---|---|---|---|---|---|---|---|
| R7L72_C23_000100_YUHAN_LAZCLUZE_PRIORITY_REVIEW_TO_APPROVAL | 000100 | 유한양행 | positive | true | true | approval/commercialization | Priority-review/partnered FDA route provided a non-price regulatory-commercialization bridge before the later formal approval. |
| R7L72_C23_039200_OSKOTEC_LAZERTINIB_ROYALTY_ROUTE | 039200 | 오스코텍 | positive | true | true | approval/commercialization | The royalty/licensing route was already visible at Stage2; a formal approval-day Green label arrived after a large part of the move. |
| R7L72_C23_028300_HLB_RIVOCERANIB_CRL_FALSE_POSITIVE | 028300 | HLB | counterexample | true | true | CRL/regulatory rejection | Pre-PDUFA momentum was real, but the event was not an approval/commercialization bridge; CRL converted the path to 4C. |
| R7L72_C23_140410_MEZZION_CRL_CONTAMINATED_WINDOW | 140410 | 메지온 | counterexample | false | true | CRL narrative blocked | CRL-like thesis break is useful narratively, but 2022-04-05 and 2022-04-25 corporate-action candidates block the forward calibration window. |


## 8. Positive vs Counterexample Balance

- Positive structural successes: 2 usable cases (`000100`, `039200`).
- Counterexamples / failed rerating: 1 usable hard counterexample (`028300`) plus 1 narrative-only blocked counterexample (`140410`).
- 4C case: `028300` CRL.
- 4B overlay: HLB and Osko show why price-only local peaks are not full 4B without non-price risk evidence.

The balance is sufficient for a C23 canonical shadow rule candidate, but not sufficient for global promotion. The rule remains sector/canonical-specific only.

## 9. Evidence Source Map

| evidence family | accepted for Stage2/3? | examples in this loop | guardrail |
|---|---|---|---|
| Partner-backed priority review | yes | 유한양행 | Needs partner/sponsor and commercialization route. |
| Royalty route through approved partner asset | yes, but Green lateness-aware | 오스코텍 | Approval-day close can be after intraday peak; do not chase fresh Green without post-approval economics. |
| PDUFA expectation / decision-risk momentum | capped | HLB | Not enough for Green without approval/commercial conversion. |
| CRL / regulatory rejection | hard 4C | HLB, 메지온 narrative | Breaks thesis regardless of prior price strength. |

## 10. Price Data Source Map

| symbol | representative shard | profile | entry row used |
|---|---|---|---|
| 000100 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv | atlas/symbol_profiles/000/000100.json | 2024-02-21 close 65,800 |
| 039200 | atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv | atlas/symbol_profiles/039/039200.json | 2024-02-21 close 21,850 |
| 028300 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json | 2024-02-21 close 80,700; 2024-05-17 4C close 67,100 |
| 140410 | no calibration row | atlas/symbol_profiles/140/140410.json | blocked narrative-only |

## 11. Case-by-Case Trigger Grid

| trigger_id | company | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | outcome | current_profile_verdict | aggregate_role |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| R7L72_C23_000100_T1_STAGE2_PRIORITY_REVIEW | 유한양행 | Stage2-Actionable | 2024-02-20 | 2024-02-21 | 65,800 | 26.75 | 28.27 | 153.65 | -2.58 | -2.58 | -2.58 | structural_success | current_profile_correct | representative |
| R7L72_C23_000100_T2_STAGE3_APPROVAL_GREEN | 유한양행 | Stage3-Green | 2024-08-20 | 2024-08-21 | 94,300 | 69.99 | 76.99 | 76.99 | -2.97 | -2.97 | -2.97 | late_but_still_positive_green | current_profile_correct | label_comparison_only |
| R7L72_C23_039200_T1_STAGE2_ROYALTY_ROUTE | 오스코텍 | Stage2-Actionable | 2024-02-20 | 2024-02-21 | 21,850 | 37.3 | 91.3 | 109.84 | -2.97 | -2.97 | -2.97 | structural_success_high_MFE | current_profile_too_late | representative |
| R7L72_C23_039200_T2_STAGE3_APPROVAL_GREEN | 오스코텍 | Stage3-Green | 2024-08-20 | 2024-08-21 | 36,900 | 24.25 | 24.25 | 24.25 | -9.76 | -26.56 | -26.56 | approval_green_late_sell_the_news_risk | current_profile_too_late | label_comparison_only |
| R7L72_C23_028300_T1_STAGE2_PDUFA_EXPECTATION | HLB | Stage2-Actionable | 2024-02-20 | 2024-02-21 | 80,700 | 59.85 | 59.85 | 59.85 | -9.17 | -44.05 | -44.05 | false_positive_green_then_4C | current_profile_false_positive | representative |
| R7L72_C23_028300_T2_4C_CRL | HLB | Stage4C | 2024-05-17 | 2024-05-17 | 67,100 | 10.0 | 46.2 | 46.2 | -32.71 | -32.71 | -32.71 | hard_4c_success_but_after_peak_damage | current_profile_4C_too_late | 4C_overlay_only |


## 12. Trigger-Level OHLC Backtest Tables

### Representative aggregate triggers

| case | entry | entry_price | peak | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | interpretation |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| 유한양행 priority-review bridge | 2024-02-21 | 65,800 | 2024-10-15 / 166,900 | 26.75 | 28.27 | 153.65 | -2.58 | -2.58 | -2.58 | Stage2 bridge aligned with large upside and low early adverse excursion. |
| 오스코텍 royalty route | 2024-02-21 | 21,850 | 2024-08-21 / 45,850 | 37.30 | 91.30 | 109.84 | -2.97 | -2.97 | -2.97 | Royalty/commercialization bridge captured most of the move before formal Green. |
| HLB PDUFA expectation | 2024-02-21 | 80,700 | 2024-03-26 / 129,000 | 59.85 | 59.85 | 59.85 | -9.17 | -44.05 | -44.05 | Large MFE was not enough; CRL turned the route into false positive / 4C. |

### 4C overlay trigger

| case | 4C entry | entry_price | MFE_30D_after_4C | MAE_30D_after_4C | MFE_90D_after_4C | MAE_90D_after_4C | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| HLB CRL | 2024-05-17 | 67,100 | 10.00 | -32.71 | 46.20 | -32.71 | hard 4C was directionally correct but late relative to the prior March peak. |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely label | actual path | verdict | residual |
|---|---|---|---|---|
| 유한양행 | Stage2-Actionable before approval, Green after approval | 180D MFE 153.65%, MAE -2.58% | current_profile_correct | none |
| 오스코텍 | May wait for formal approval/Green | Stage2 MFE 109.84%; approval-day close after intraday peak | current_profile_too_late | royalty route Green-lateness |
| HLB | May over-score unresolved PDUFA if RS dominates | 90D MAE -44.05% after CRL | current_profile_false_positive / current_profile_4C_too_late | PDUFA expectation cap needed |
| 메지온 | data insufficient for weighted calibration | corporate-action contaminated window | current_profile_data_insufficient | narrative only |

## 14. Stage2 / Yellow / Green Comparison

- 유한양행: Stage2 entry at 65,800 captured a much better risk/reward than formal approval Green at 94,300. Green lateness ratio = `(94,300 - 65,800) / (166,900 - 65,800) = 0.282`, which is acceptable but confirms that Stage2 had the cleaner entry.
- 오스코텍: Stage2 entry at 21,850 versus approval-day close at 36,900 yields Green lateness ratio = `(36,900 - 21,850) / (45,850 - 21,850) = 0.627`. Green captured confirmation but missed most of the upside and carried sell-the-news risk.
- HLB: no confirmed Green should have existed. A Green-like label from RS plus decision expectation would be a false positive.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak | full-window peak | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence type | verdict |
|---|---:|---:|---:|---:|---|---|
| 오스코텍 approval-day spike | 45,850 | 45,850 | 1.00 | 1.00 | price_only | Price-only local peak is not a full 4B; needs non-price risk evidence. |
| HLB pre-CRL March peak | 129,000 | 129,000 | 1.00 | 1.00 | price_only, positioning_overheat | Full 4B should remain overlay/watch unless regulatory-risk evidence appears; CRL later routes to 4C. |

This strengthens the already-applied `full_4b_requires_non_price_evidence` axis inside C23. Price-only peaks mark fragility, not necessarily a thesis-break sell signal.

## 16. 4C Protection Audit

HLB demonstrates the difference between overheat and thesis break. The March peak was a price/positioning event; the May CRL was thesis evidence broken. 4C after the CRL still suffered additional MAE, but it correctly blocked any positive-stage continuation. Approximate post-4C protection label:

```text
four_c_protection_label = hard_4c_late_but_thesis_break_success
four_c_protection_score = directional_only
reason = CRL came after peak damage, but still prevented treating the rebound as fresh positive evidence.
```

## 17. Sector-Specific Rule Candidate

```yaml
sector_specific_rule_candidate: true
rule_scope: sector_specific
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
axis: L7_regulatory_event_status_resolution_gate
proposal: |
  In L7, regulatory events require status resolution. Positive promotion needs either formal approval, priority review with credible sponsor/partner and commercialization route, or royalty/revenue visibility. PDUFA expectation plus relative strength is capped below Green until approval/commercial conversion. CRL/regulatory rejection routes to hard 4C.
```

## 18. Canonical-Archetype Rule Candidate

```yaml
canonical_archetype_rule_candidate: true
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
new_axis_proposed:
  - C23_partner_backed_regulatory_commercialization_bridge
  - C23_unresolved_PDUFA_expectation_cap
  - C23_CRL_hard_4C_override
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | late_green_count | score_return_alignment_verdict |
|---|---:|---|---:|---|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | Existing profile catches Stage2 bonus but can over-trust unresolved PDUFA expectation. | 3 | 000100_T1 / 039200_T1 / 028300_T1 | 59.81 | -16.53 | 33.3% | 1 | mixed |
| P0b_e2r_2_0_baseline_reference | rollback | Old baseline waits too long for formal Green and misses early regulatory bridge. | 3 | mostly later approval labels | 44.36 | -24.53 | 33.3% | 2 | too_late |
| P1_sector_specific_candidate_profile | sector | L7 regulatory events need sponsor/partner/commercialization bridge, not RS alone. | 3 | 000100_T1 / 039200_T1 / 028300_capped | 59.81 | -16.53 | 0.0% | 1 | improved_guard |
| P2_canonical_archetype_candidate_profile | C23 | C23 separates approval/royalty route from unresolved decision-risk. | 3 | 000100_T1 / 039200_T1 / 028300_4C_watch | 59.81 | -16.53 | 0.0% | 1 | best_shadow_fit |
| P3_counterexample_guard_profile | C23 guard | CRL and no-approval status override prior price strength. | 3 | 000100_T1 / 039200_T1 / HLB_4C | 55.87 | -13.87 | 0.0% | 1 | protects_false_positive |


## 20. Score-Return Alignment Matrix

| trigger | before score / label | after score / label | return alignment | explanation |
|---|---|---|---|---|
| 유한양행 Stage2 | 76 / Stage2-Actionable | 83 / Stage2-Actionable-C23-bridge | aligned | Partner-backed approval route earned early score without waiting for final approval. |
| 오스코텍 Stage2 | 76 / Stage2-Actionable | 83 / Stage2-Actionable-C23-bridge | aligned | Royalty route compressed into C23 despite not being direct product sales. |
| HLB PDUFA expectation | 78 / Stage2-Actionable | 63 / Stage2-capped-no-approval | improved guard | RS and PDUFA expectation produced MFE, but unresolved decision risk created false positive. |
| HLB CRL 4C | 25 / Stage4C | 14 / Stage4C-hard | aligned with thesis break | CRL should override earlier score and route to hard 4C. |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | FDA_APPROVAL_COMMERCIALIZATION_ROYALTY_ROUTE__VS__CRL_THESIS_BREAK | 2 | 2 | 1 | 1 | 4 | 0 | 6 | 3 | 2 | true | true | C23 now has partner-backed positive route plus CRL/PDUFA false-positive guard; still needs more post-2025 commercial ramp holdouts. |


## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 2
calibration_usable_case_count: 3
calibration_usable_trigger_count: 6
representative_trigger_count: 3
current_profile_error_count: 2
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - approval_green_lateness_in_royalty_route
  - PDUFA_expectation_false_positive
  - CRL_4C_too_late_after_peak_damage
new_axis_proposed:
  - C23_partner_backed_regulatory_commercialization_bridge
  - C23_unresolved_PDUFA_expectation_cap
  - C23_CRL_hard_4C_override
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable OHLC rows for 000100, 039200, 028300.
- Profile-level corporate-action caveat check for 000100, 039200, 028300, 140410.
- 30D / 90D / 180D MFE and MAE for usable representative triggers.
- Stage2 vs Stage3 Green lateness for 유한양행 and 오스코텍.
- 4C overlay timing for HLB CRL.
```

Non-validation scope:

```text
- No current/live candidate discovery.
- No stock_agent source code inspection.
- No production scoring change.
- No 1Y/2Y calibration vote from this MD.
- No brokerage/API/trading execution.
- No global rule promotion.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C23_partner_backed_regulatory_commercialization_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Partner-backed FDA priority-review/approval route with royalty or direct commercialization should preserve Stage2-Actionable even before formal approval when non-price evidence exists.","Improves Yuhan/Osko Stage2 alignment without waiting for late approval Green.","R7L72_C23_000100_T1_STAGE2_PRIORITY_REVIEW|R7L72_C23_039200_T1_STAGE2_ROYALTY_ROUTE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C23_unresolved_PDUFA_expectation_cap,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"PDUFA expectation without approval/commercial conversion should be capped below Green even with strong RS.","Blocks HLB-style false positive Green while retaining 4C thesis-break routing.","R7L72_C23_028300_T1_STAGE2_PDUFA_EXPECTATION",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C23_CRL_hard_4C_override,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"CRL/regulatory rejection immediately breaks approval-commercialization thesis; route to hard 4C regardless of prior MFE.","Improves drawdown protection after regulatory rejection; recognizes that 4C can still be late if detected only after a large gap.","R7L72_C23_028300_T2_4C_CRL",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R7L72_C23_000100_YUHAN_LAZCLUZE_PRIORITY_REVIEW_TO_APPROVAL", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "72", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_COMMERCIALIZATION_ROYALTY_ROUTE__VS__CRL_THESIS_BREAK", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R7L72_C23_000100_T1_STAGE2_PRIORITY_REVIEW", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Priority-review/partnered FDA route provided a non-price regulatory-commercialization bridge before the later formal approval."}
{"row_type": "case", "case_id": "R7L72_C23_039200_OSKOTEC_LAZERTINIB_ROYALTY_ROUTE", "symbol": "039200", "company_name": "오스코텍", "round": "R7", "loop": "72", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_COMMERCIALIZATION_ROYALTY_ROUTE__VS__CRL_THESIS_BREAK", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R7L72_C23_039200_T1_STAGE2_ROYALTY_ROUTE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "The royalty/licensing route was already visible at Stage2; a formal approval-day Green label arrived after a large part of the move."}
{"row_type": "case", "case_id": "R7L72_C23_028300_HLB_RIVOCERANIB_CRL_FALSE_POSITIVE", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "72", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_COMMERCIALIZATION_ROYALTY_ROUTE__VS__CRL_THESIS_BREAK", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R7L72_C23_028300_T1_STAGE2_PDUFA_EXPECTATION", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Pre-PDUFA momentum was real, but the event was not an approval/commercialization bridge; CRL converted the path to 4C."}
{"row_type": "case", "case_id": "R7L72_C23_140410_MEZZION_CRL_CONTAMINATED_WINDOW", "symbol": "140410", "company_name": "메지온", "round": "R7", "loop": "72", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_COMMERCIALIZATION_ROYALTY_ROUTE__VS__CRL_THESIS_BREAK", "case_type": "narrative_only", "positive_or_counterexample": "counterexample", "best_trigger": "R7L72_C23_140410_N1_CRL_NARRATIVE_BLOCKED", "calibration_usable": false, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "score_price_alignment": "narrative_only_blocked", "current_profile_verdict": "current_profile_data_insufficient", "price_source": "Songdaiki/stock-web", "notes": "CRL-like thesis break is useful narratively, but 2022-04-05 and 2022-04-25 corporate-action candidates block the forward calibration window."}
{"row_type": "trigger", "trigger_id": "R7L72_C23_000100_T1_STAGE2_PRIORITY_REVIEW", "case_id": "R7L72_C23_000100_YUHAN_LAZCLUZE_PRIORITY_REVIEW_TO_APPROVAL", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "72", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_COMMERCIALIZATION_ROYALTY_ROUTE__VS__CRL_THESIS_BREAK", "sector": "bio_healthcare_medical", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-20", "entry_date": "2024-02-21", "entry_price": 65800, "evidence_available_at_that_date": "FDA priority-review / partner commercial route for lazertinib combination; Korean disclosure/news timing treated as next-trading-day close.", "evidence_source": "Public regulatory/partner disclosure and Korean market reports; stock-web row: atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 26.75, "MFE_90D_pct": 28.27, "MFE_180D_pct": 153.65, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.58, "MAE_90D_pct": -2.58, "MAE_180D_pct": -2.58, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-15", "peak_price": 166900, "drawdown_after_peak_pct": -17.13, "green_lateness_ratio": "0.282_vs_later_approval_green", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L72_C23_000100_2024-02-21_65800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L72_C23_000100_T2_STAGE3_APPROVAL_GREEN", "case_id": "R7L72_C23_000100_YUHAN_LAZCLUZE_PRIORITY_REVIEW_TO_APPROVAL", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "72", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_COMMERCIALIZATION_ROYALTY_ROUTE__VS__CRL_THESIS_BREAK", "sector": "bio_healthcare_medical", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test", "trigger_type": "Stage3-Green", "trigger_date": "2024-08-20", "entry_date": "2024-08-21", "entry_price": 94300, "evidence_available_at_that_date": "Formal FDA approval of Lazcluze/Rybrevant route; approval-day Korean close used as label-comparison entry.", "evidence_source": "Public FDA/J&J/Yuhan approval references; stock-web row: atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 69.99, "MFE_90D_pct": 76.99, "MFE_180D_pct": 76.99, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.97, "MAE_90D_pct": -2.97, "MAE_180D_pct": -2.97, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-15", "peak_price": 166900, "drawdown_after_peak_pct": -17.13, "green_lateness_ratio": 0.282, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_but_still_positive_green", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L72_C23_000100_2024-08-21_94300", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same_case_stage3_label_comparison", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R7L72_C23_039200_T1_STAGE2_ROYALTY_ROUTE", "case_id": "R7L72_C23_039200_OSKOTEC_LAZERTINIB_ROYALTY_ROUTE", "symbol": "039200", "company_name": "오스코텍", "round": "R7", "loop": "72", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_COMMERCIALIZATION_ROYALTY_ROUTE__VS__CRL_THESIS_BREAK", "sector": "bio_healthcare_medical", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-20", "entry_date": "2024-02-21", "entry_price": 21850, "evidence_available_at_that_date": "Lazertinib/Janssen path created a royalty-commercialization option before final approval; next-trading-day close used.", "evidence_source": "Public partner/regulatory route and Korean reports; stock-web row: atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv", "profile_path": "atlas/symbol_profiles/039/039200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 37.3, "MFE_90D_pct": 91.3, "MFE_180D_pct": 109.84, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.97, "MAE_90D_pct": -2.97, "MAE_180D_pct": -2.97, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-21", "peak_price": 45850, "drawdown_after_peak_pct": -40.89, "green_lateness_ratio": "0.627_vs_later_approval_green", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_MFE", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L72_C23_039200_2024-02-21_21850", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L72_C23_039200_T2_STAGE3_APPROVAL_GREEN", "case_id": "R7L72_C23_039200_OSKOTEC_LAZERTINIB_ROYALTY_ROUTE", "symbol": "039200", "company_name": "오스코텍", "round": "R7", "loop": "72", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_COMMERCIALIZATION_ROYALTY_ROUTE__VS__CRL_THESIS_BREAK", "sector": "bio_healthcare_medical", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test", "trigger_type": "Stage3-Green", "trigger_date": "2024-08-20", "entry_date": "2024-08-21", "entry_price": 36900, "evidence_available_at_that_date": "Formal approval confirms the royalty route, but the approval-day intraday high printed before the close; use as late-green stress test.", "evidence_source": "Public approval references; stock-web row: atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv", "profile_path": "atlas/symbol_profiles/039/039200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 24.25, "MFE_90D_pct": 24.25, "MFE_180D_pct": 24.25, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.76, "MAE_90D_pct": -26.56, "MAE_180D_pct": -26.56, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-21", "peak_price": 45850, "drawdown_after_peak_pct": -40.89, "green_lateness_ratio": 0.627, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_not_full_4B", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "approval_green_late_sell_the_news_risk", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L72_C23_039200_2024-08-21_36900", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same_case_stage3_label_comparison", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R7L72_C23_028300_T1_STAGE2_PDUFA_EXPECTATION", "case_id": "R7L72_C23_028300_HLB_RIVOCERANIB_CRL_FALSE_POSITIVE", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "72", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_COMMERCIALIZATION_ROYALTY_ROUTE__VS__CRL_THESIS_BREAK", "sector": "bio_healthcare_medical", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-20", "entry_date": "2024-02-21", "entry_price": 80700, "evidence_available_at_that_date": "PDUFA/FDA-decision expectation plus strong relative strength, but no final approval or commercial conversion yet.", "evidence_source": "Public PDUFA/approval-expectation news; stock-web row: atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 59.85, "MFE_90D_pct": 59.85, "MFE_180D_pct": 59.85, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.17, "MAE_90D_pct": -44.05, "MAE_180D_pct": -44.05, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-26", "peak_price": 129000, "drawdown_after_peak_pct": -65.0, "green_lateness_ratio": "not_applicable_no_confirmed_approval_green", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_requires_non_price_overlay", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only_until_CRL", "trigger_outcome_label": "false_positive_green_then_4C", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L72_C23_028300_2024-02-21_80700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L72_C23_028300_T2_4C_CRL", "case_id": "R7L72_C23_028300_HLB_RIVOCERANIB_CRL_FALSE_POSITIVE", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "72", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_COMMERCIALIZATION_ROYALTY_ROUTE__VS__CRL_THESIS_BREAK", "sector": "bio_healthcare_medical", "primary_archetype": "bio_regulatory_approval_commercialization", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test", "trigger_type": "Stage4C", "trigger_date": "2024-05-17", "entry_date": "2024-05-17", "entry_price": 67100, "evidence_available_at_that_date": "Complete Response Letter / FDA non-approval event broke the approval-commercialization thesis.", "evidence_source": "Public CRL/non-approval disclosure and news; stock-web row: atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["positioning_overheat"], "stage4c_evidence_fields": ["regulatory_rejection", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.0, "MFE_90D_pct": 46.2, "MFE_180D_pct": 46.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -32.71, "MAE_90D_pct": -32.71, "MAE_180D_pct": -32.71, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 98100, "drawdown_after_peak_pct": -35.1, "green_lateness_ratio": "not_applicable_4C", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_late_but_thesis_break_success", "trigger_outcome_label": "hard_4c_success_but_after_peak_damage", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L72_C23_028300_2024-05-17_67100", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_case_4C_timing_overlay", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L72_C23_000100_YUHAN_LAZCLUZE_PRIORITY_REVIEW_TO_APPROVAL", "trigger_id": "R7L72_C23_000100_T1_STAGE2_PRIORITY_REVIEW", "symbol": "000100", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 12, "customer_quality_score": 17, "policy_or_regulatory_score": 24, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 12, "customer_quality_score": 20, "policy_or_regulatory_score": 28, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 83, "stage_label_after": "Stage2-Actionable-C23-bridge", "changed_components": ["customer_quality_score", "policy_or_regulatory_score"], "component_delta_explanation": "C23 shadow profile separates partner-backed approval/commercialization bridge from unresolved PDUFA expectation and hard CRL thesis break.", "MFE_90D_pct": 28.27, "MAE_90D_pct": -2.58, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L72_C23_000100_YUHAN_LAZCLUZE_PRIORITY_REVIEW_TO_APPROVAL", "trigger_id": "R7L72_C23_000100_T2_STAGE3_APPROVAL_GREEN", "symbol": "000100", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 14, "relative_strength_score": 0, "customer_quality_score": 18, "policy_or_regulatory_score": 28, "valuation_repricing_score": 12, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 14, "relative_strength_score": 0, "customer_quality_score": 18, "policy_or_regulatory_score": 28, "valuation_repricing_score": 7, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Green-lateness_checked", "changed_components": ["valuation_repricing_score"], "component_delta_explanation": "C23 shadow profile separates partner-backed approval/commercialization bridge from unresolved PDUFA expectation and hard CRL thesis break.", "MFE_90D_pct": 76.99, "MAE_90D_pct": -2.97, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L72_C23_039200_OSKOTEC_LAZERTINIB_ROYALTY_ROUTE", "trigger_id": "R7L72_C23_039200_T1_STAGE2_ROYALTY_ROUTE", "symbol": "039200", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 12, "customer_quality_score": 17, "policy_or_regulatory_score": 24, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 12, "customer_quality_score": 20, "policy_or_regulatory_score": 28, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 83, "stage_label_after": "Stage2-Actionable-C23-bridge", "changed_components": ["customer_quality_score", "policy_or_regulatory_score"], "component_delta_explanation": "C23 shadow profile separates partner-backed approval/commercialization bridge from unresolved PDUFA expectation and hard CRL thesis break.", "MFE_90D_pct": 91.3, "MAE_90D_pct": -2.97, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L72_C23_039200_OSKOTEC_LAZERTINIB_ROYALTY_ROUTE", "trigger_id": "R7L72_C23_039200_T2_STAGE3_APPROVAL_GREEN", "symbol": "039200", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 14, "relative_strength_score": 0, "customer_quality_score": 18, "policy_or_regulatory_score": 28, "valuation_repricing_score": 12, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 14, "relative_strength_score": 0, "customer_quality_score": 18, "policy_or_regulatory_score": 28, "valuation_repricing_score": 7, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 77, "stage_label_after": "Stage3-Green-lateness_checked", "changed_components": ["valuation_repricing_score"], "component_delta_explanation": "C23 shadow profile separates partner-backed approval/commercialization bridge from unresolved PDUFA expectation and hard CRL thesis break.", "MFE_90D_pct": 24.25, "MAE_90D_pct": -26.56, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L72_C23_028300_HLB_RIVOCERANIB_CRL_FALSE_POSITIVE", "trigger_id": "R7L72_C23_028300_T1_STAGE2_PDUFA_EXPECTATION", "symbol": "028300", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 20, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": -4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 20, "valuation_repricing_score": 10, "execution_risk_score": -15, "legal_or_contract_risk_score": -12, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 63, "stage_label_after": "Stage2-capped-no-approval", "changed_components": ["execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C23 shadow profile separates partner-backed approval/commercialization bridge from unresolved PDUFA expectation and hard CRL thesis break.", "MFE_90D_pct": 59.85, "MAE_90D_pct": -44.05, "score_return_alignment_label": "false_positive_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L72_C23_028300_HLB_RIVOCERANIB_CRL_FALSE_POSITIVE", "trigger_id": "R7L72_C23_028300_T2_4C_CRL", "symbol": "028300", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": -35, "valuation_repricing_score": 0, "execution_risk_score": -18, "legal_or_contract_risk_score": -28, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -4}, "weighted_score_before": 25, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": -35, "valuation_repricing_score": 0, "execution_risk_score": -24, "legal_or_contract_risk_score": -36, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -4}, "weighted_score_after": 14, "stage_label_after": "Stage4C-hard", "changed_components": ["execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C23 shadow profile separates partner-backed approval/commercialization bridge from unresolved PDUFA expectation and hard CRL thesis break.", "MFE_90D_pct": 46.2, "MAE_90D_pct": -32.71, "score_return_alignment_label": "false_positive_guard_needed", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "residual_contribution", "round": "R7", "loop": "72", "scheduled_round": "R7", "scheduled_loop": 72, "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["approval_green_lateness_in_royalty_route", "PDUFA_expectation_false_positive", "CRL_4C_too_late_after_peak_damage"], "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 2, "diversity_score_summary": "new_symbols=4; new_trigger_family=4; counterexamples=2; residual_errors=2; wrong_round_penalty=0", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
{"row_type": "narrative_only", "case_id": "R7L72_C23_140410_MEZZION_CRL_CONTAMINATED_WINDOW", "symbol": "140410", "company_name": "메지온", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "reason": "CRL/regulatory thesis break is relevant but 2022-04-05 and 2022-04-25 corporate-action candidate dates contaminate the 180D forward window.", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
completed_loop = 72
next_round = R8
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web manifest: `atlas/manifest.json`, max_date `2026-02-20`, basis `tradable_raw`, adjustment `raw_unadjusted_marcap`.
- Stock-web schema: `atlas/schema.json`, tradable columns `d,o,h,l,c,v,a,mc,s,m`.
- Profiles checked: `000/000100.json`, `039/039200.json`, `028/028300.json`, `140/140410.json`.
- Tradable shards checked: `000/000100/2024.csv`, `039/039200/2024.csv`, `028/028300/2024.csv`.
- Event evidence is used only as historical trigger context; no live recommendation language is intended.

