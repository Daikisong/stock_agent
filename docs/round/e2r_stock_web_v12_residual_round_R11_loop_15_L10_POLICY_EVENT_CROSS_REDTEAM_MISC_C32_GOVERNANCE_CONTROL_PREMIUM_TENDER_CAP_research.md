# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R11_loop_15_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md

scheduled_round = R11
scheduled_loop = 15
completed_round = R11
completed_loop = 15
next_round = R12
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass

large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_AND_POLICY_RESCUE_GUARD

live_candidate_mode = false
current_stock_discovery_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 3 new independent cases, 1 counterexamples, and 2 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.

## 1. Current Calibrated Profile Assumption

The current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied axes are treated as active:

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

This research does not re-prove those global axes. It stress-tests whether C32 governance/event cases need a more specific shadow rule: a cash tender or explicit control-price anchor can justify Stage2-Actionable, but tender cap, offer deadline, squeeze dynamics, legal contest, and state-rescue dilution must decide whether the event is 4B, 4C, or no-promote.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R11 |
| scheduled_loop | 15 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP |
| round_sector_consistency | pass |
| loop_objective | coverage_gap_fill; counterexample_mining; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression |

R11 is used here as event/policy/governance round. C32 is selected because the common mechanism is not ordinary sector EPS rerating. It is a control-right price discovery mechanism: the stock behaves like a courtroom auction board. Cash offers, tender prices, financing terms, injunctions, acceptance deadlines, and squeeze mechanics become the rails of the price path.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifacts were consulted only for coverage and applied-axis awareness. `calibrated_profile_report.md` shows production default scoring already changed and lists the applied axes, including Stage2 bonus, stricter Green gates, full 4B non-price requirement, hard 4C routing, and price-only blowoff blocking positive stage. No `src/e2r` code was opened or inferred.

Search for `e2r_stock_web_v12_residual_round_R11_loop` in `Songdaiki/stock_agent` returned no current v12 file result in the accessible code-search index. The prior local handoff state from the immediately preceding generated MD set `next_round=R11`, `next_loop=15`; this MD follows that state.

Duplicate guard outcome:

| candidate | duplicate risk | action |
|---|---:|---|
| 에스엠 041510 / 2023 control battle | low | new symbol/trigger family in v12 C32 scope |
| 고려아연 010130 / 2024 hostile tender-buyback squeeze | low | new symbol/trigger family in v12 C32 scope |
| 한진칼 180640 / 2020 state-backed Asiana rescue-merger | low | new counterexample and policy-rescue guard |
| 아시아나항공 020560 / 2020 target event | rejected | corporate-action candidate on 2021-01-15 overlaps the forward 180D window, so not used for quantitative calibration |

## 4. Stock-Web OHLC Input / Price Source Validation

- Stock-Web manifest read: `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, `tradable_row_count=14,354,401`, `symbol_count=5,414`, `markets=KONEX/KOSDAQ/KOSDAQ GLOBAL/KOSPI`.
- Schema read: tradable columns are `d,o,h,l,c,v,a,mc,s,m`; calibration requires positive OHLCV, entry row exists, at least 180 forward tradable days, and no 180D corporate-action contamination.
- Profiles checked: `041510`, `010130`, `180640`.
  - `041510` has no corporate-action candidate in the 2023 control-battle window.
  - `010130` has `corporate_action_candidate_count=0`.
  - `180640` has one corporate-action candidate in 2014 only, outside the 2020/2021 event window.


`manifest.max_date=2026-02-20` is used as the forward-window boundary. No price after that date is fabricated.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D available | corporate action window | calibration_usable | reason |
|---|---:|---:|---:|---|---:|---|
| R11L15_C32_SM_041510 | 041510 | 2023-02-10 | yes | clean_180D_window | true | active-like profile, no 2023 corporate-action candidate |
| R11L15_C32_KZ_010130 | 010130 | 2024-09-13 | yes | clean_180D_window | true | corporate_action_candidate_count=0 |
| R11L15_C32_HK_180640 | 180640 | 2020-11-16 | yes | clean_180D_window | true | only corporate-action candidate is 2014-11-20 |
| narrative rejected candidate | 020560 | 2020-11-16 | yes | contaminated | false | 2021-01-15 corporate-action candidate overlaps 180D window |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| K_CONTENT_CONTROL_PREMIUM_TENDER_CAP | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Same mechanism: cash tender price creates event anchor; offer cap creates 4B |
| HOSTILE_TENDER_BUYBACK_COUNTERBID_CONTROL_PREMIUM | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Same mechanism: hostile/friendly counter-offers create control-squeeze path |
| STATE_BACKED_RESCUE_MERGER_CONTROL_PREMIUM_DILUTION_GUARD | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Same event domain, but serves as counterexample: policy rescue can be minority-shareholder dilution |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | one-line result |
|---|---:|---|---|---|---|
| R11L15_C32_SM_041510 | 041510 | 에스엠 | structural_success + 4B overlay | cash tender / tender cap | Stage2 worked; Kakao 150k tender cap was a good full-window 4B |
| R11L15_C32_KZ_010130 | 010130 | 고려아연 | high-MFE success + 4B too early | hostile tender / counter-buyback | Stage2 worked dramatically; first 4B cap was too early for full squeeze |
| R11L15_C32_HK_180640 | 180640 | 한진칼 | false positive | policy rescue / dilution overhang | policy-backed merger headline failed as durable rerating |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 5
new_independent_case_count = 3
reused_case_count = 0
```

The balance is acceptable for canonical shadow-rule proposal, but not for global promotion. It is a C32-specific rule candidate only.

## 9. Evidence Source Map

| case | historical evidence source | event interpretation |
|---|---|---|
| 에스엠 | AP reported HYBE's 14.8% stake purchase and planned 120,000 KRW tender route, and later Kakao's 150,000 KRW tender for 35% | cash control contest; positive entry anchor and later tender cap |
| 고려아연 | Reuters reported MBK/Young Poong 660,000 KRW tender offer; Reuters later reported court clearing Korea Zinc buyback/tender hurdle and price near 890,000 KRW tender offer | hostile tender/counter-tender squeeze; first event cap not enough for full 4B |
| 한진칼 | Reuters/Wikipedia summary of state-backed Korean Air/Asiana merger and KDB funding to Hanjin Group | policy rescue headline; dilution/regulatory burden prevented durable minority rerating |

## 10. Price Data Source Map

| symbol | profile_path | shard_path(s) used | profile caveat |
|---:|---|---|---|
| 041510 | atlas/symbol_profiles/041/041510.json | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | corporate action candidates exist only in 2002/2005, outside event window |
| 010130 | atlas/symbol_profiles/010/010130.json | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv; 2025.csv | corporate_action_candidate_count=0 |
| 180640 | atlas/symbol_profiles/180/180640.json | atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv; 2021.csv | 2014 candidate only, outside event window |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | evidence split | current_profile_verdict | aggregate_role |
|---|---|---:|---|---:|---:|---:|---|---|---|
| R11L15_C32_SM_041510_T1_HYBE_STAKE_TENDER_STAGE2 | SM | 041510 | Stage2-Actionable | 2023-02-10 | 2023-02-10 | 114,700 | Stage2: stake+tender anchor; Stage3: no EPS Green | current_profile_correct | representative |
| R11L15_C32_SM_041510_T2_KAKAO_TENDER_CAP_4B | SM | 041510 | Stage4B | 2023-03-07 | 2023-03-07 | 149,700 | 4B: explicit 150k tender cap | current_profile_correct | 4B_overlay_only |
| R11L15_C32_KZ_010130_T1_MBK_YP_TENDER_STAGE2 | KZ | 010130 | Stage2-Actionable | 2024-09-13 | 2024-09-13 | 666,000 | Stage2: hostile tender anchor | current_profile_correct | representative |
| R11L15_C32_KZ_010130_T2_COURT_BUYBACK_4B_TOO_EARLY | KZ | 010130 | Stage4B | 2024-10-21 | 2024-10-21 | 877,000 | 4B: tender/buyback legal cap, but squeeze unresolved | current_profile_4B_too_early | 4B_overlay_only |
| R11L15_C32_HK_180640_T1_KDB_ASIANA_POLICY_STAGE2_FALSE_POSITIVE | HK | 180640 | Stage2-Actionable | 2020-11-16 | 2020-11-16 | 82,200 | Stage2 headline; 4B/4C dilution/regulatory overhang | current_profile_false_positive | representative |

## 12. Trigger-Level OHLC Backtest Tables

### Representative entry triggers

| trigger_id | entry | price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | below_entry_90D |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SM Stage2 | 2023-02-10 | 114,700 | 40.54% | 40.54% | 40.54% | -21.10% | -21.10% | -21.10% | 2023-03-08 | 161,200 | true |
| KZ Stage2 | 2024-09-13 | 666,000 | 131.68% | 261.41% | 261.41% | -1.65% | -1.65% | -3.45% | 2024-12-06 | 2,407,000 | false |
| Hanjin KAL Stage2 | 2020-11-16 | 82,200 | 16.18% | 16.18% | 16.18% | -27.74% | -31.75% | -39.84% | 2020-11-16 | 95,500 | true |

### 4B overlay triggers

| trigger_id | entry | price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | 4B verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SM Kakao tender cap | 2023-03-07 | 149,700 | 7.68% | 7.68% | 7.68% | -39.55% | -39.55% | -42.35% | good_full_window_4B_timing |
| KZ court/buyback cap | 2024-10-21 | 877,000 | 74.91% | 174.46% | 174.46% | -15.74% | -15.74% | -26.68% | price_only_or_first_tender_cap_4B_too_early_for_full_window |

## 13. Current Calibrated Profile Stress Test

| case | how P0 likely classifies | actual alignment | verdict |
|---|---|---|---|
| SM | Stage2-Actionable on control-premium evidence; not Green because no earnings revision | Correct entry; needs explicit 4B cap later | current_profile_correct |
| Korea Zinc | Stage2-Actionable; first non-price 4B allowed around court/tender cap | Entry correct, but first non-price cap misses later squeeze | current_profile_4B_too_early |
| Hanjin KAL | Stage2-Actionable from policy-backed control/rescue headline | Large MAE, no durable rerating | current_profile_false_positive |

Stress answers:

1. Stage2 bonus was useful for SM and Korea Zinc, too permissive for Hanjin KAL.
2. Yellow threshold 75 is acceptable for tender/control evidence, but should not survive policy-rescue dilution.
3. Green 87/revision 55 should remain strict; none of these should be promoted to full fundamental Green without revision evidence.
4. Price-only blowoff guard remains correct.
5. Full 4B non-price requirement remains correct, but C32 needs a second distinction: local tender cap vs unresolved control squeeze.
6. Hard 4C routing remains correct, especially for policy rescue where the minority-shareholder thesis is broken by dilution/regulatory financing.

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used as an entry in this loop. The point is not that Green is late; it is that C32 often has no legitimate Green because the evidence is event-price-control, not earnings-revision durability.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | Stage2 price | 4B price | local peak | full peak | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| SM Kakao 150k tender cap | 114,700 | 149,700 | 161,200 | 161,200 | 0.75 | 0.75 | good full-window 4B |
| Korea Zinc court/buyback cap | 666,000 | 877,000 | 889,000 | 2,407,000 | 0.95 | 0.12 | too early for full-window 4B |

This split is the main residual contribution. C32 needs a separate `control_squeeze_unresolved` state: a valid non-price event cap can be a good local risk overlay while still being too early as a full exit signal.

## 16. 4C Protection Audit

| case | 4C label | protection logic |
|---|---|---|
| SM | hard_4c_success_if_tender_cap_breaks_after_acceptance_end | Once tender acceptance and ownership result is known, price below cap is no longer just volatility; it is the end of the control-premium path |
| Korea Zinc | hard_4c_late_if_only_after_squeeze_collapse | Waiting for post-squeeze collapse is protective but late; 4B watch-only should appear before hard 4C |
| Hanjin KAL | thesis_break_watch_only | Policy rescue and capital injection should cap Stage2 promotion before a full 4C crash is required |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = R11/L10 cross-event sample is not a conventional operating sector.
```

The rule should not be tied to content, materials, or airlines. It belongs to C32 canonical event mechanics.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

Proposed shadow rules:

1. **C32 explicit cash tender / control price anchor bonus**  
   Add a small positive shadow bonus when an actual cash offer, tender price, or control stake transaction gives a verifiable price anchor.

2. **C32 tender cap / offer deadline 4B overlay**  
   If the stock trades at or near the tender price and the acceptance/deadline mechanics cap upside, treat it as 4B overlay even if price momentum remains strong.

3. **C32 unresolved control squeeze watch-only state**  
   If legal battle, counter-buyback, or free-float squeeze can continue, do not convert first tender-cap proximity into full-window 4B; split local and full proximity.

4. **C32 policy rescue dilution-overhang no-Green guard**  
   State-backed rescue, financing, or merger consolidation cannot become Green unless the minority-shareholder upside route is explicit and dilution/regulatory burden is controlled.

## 19. Before / After Backtest Comparison

| profile_id | scope | changed axes | eligible representatives | avg MFE_90D | avg MAE_90D | avg MFE_180D | avg MAE_180D | false positive rate | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | none | 3 | 106.04% | -18.17% | 106.04% | -21.46% | 33.3% | captures entries but lets policy-rescue false positive through |
| P0b e2r_2_0_baseline_reference | rollback | weaker Stage2 bonus / looser Green | 3 | 106.04% | -18.17% | 106.04% | -21.46% | 33.3% | worse label clarity; may confuse event price action with Green |
| P1 sector_specific_candidate_profile | L10 | no sector delta | 3 | 106.04% | -18.17% | 106.04% | -21.46% | 33.3% | no sector rule proposed |
| P2 canonical_archetype_candidate_profile | C32 | tender anchor bonus + tender cap overlay + dilution guard | 3 | 106.04% | -18.17% | 106.04% | -21.46% | 0% after label correction | best explanatory fit |
| P3 counterexample_guard_profile | C32 guard | excludes policy-rescue dilution no-upside trigger | 2 | 150.98% | -11.38% | 150.98% | -12.28% | 0% | cleaner but could over-filter real state-backed value transfers |

## 20. Score-Return Alignment Matrix

| case | before_score | before_label | after_score | after_label | return alignment |
|---|---:|---|---:|---|---|
| SM Stage2 | 78 | Stage2-Actionable | 80 | Stage2-Actionable | aligned |
| SM 4B | 82 | Stage3-Yellow | 69 | Stage4B-Overlay | improved |
| Korea Zinc Stage2 | 79 | Stage2-Actionable | 80 | Stage2-Actionable | aligned |
| Korea Zinc 4B | 85 | Stage3-Yellow/4B-watch | 72 | Stage4B-watch-only | improved: avoids full exit too early |
| Hanjin KAL | 77 | Stage2-Actionable | 61 | Stage2-Watch/No-Promote | improved: filters false positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | mixed C32 governance event | 2 | 1 | 2 | 1 | 3 | 0 | 5 | 3 | 2 | false | true | More holdout cases needed: squeeze ending, failed tender, delisting/tender narrative-only |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 4

tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
- policy_rescue_false_positive
- first_tender_cap_4B_too_early_when_control_squeeze_continues
- tender_cap_should_be_overlay_not_positive_green

new_axis_proposed:
- C32_explicit_cash_tender_or_control_price_anchor_bonus
- C32_tender_cap_or_offer_deadline_4B_overlay
- C32_policy_rescue_dilution_overhang_no_green_guard

existing_axis_strengthened:
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

existing_axis_weakened: null
existing_axis_kept:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- stage3_green_revision_min
- price_only_blowoff_blocks_positive_stage

sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- actual Stock-Web tradable OHLC rows for all quantitative triggers.
- entry_date and entry_price from `c` column.
- MFE/MAE from high/low windows.
- corporate-action window status from symbol profiles.
- current calibrated profile stress test as research proxy.

Not validated:

- production `stock_agent` code.
- live candidates.
- broker/API workflows.
- exact production scoring implementation.
- investment recommendation.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_explicit_cash_tender_or_control_price_anchor_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,1,"cash tender/offer price gives real event anchor, unlike vague governance rumor",improves positive hit recognition for SM/Korea Zinc entry triggers,R11L15_C32_SM_041510_T1_HYBE_STAKE_TENDER_STAGE2|R11L15_C32_KZ_010130_T1_MBK_YP_TENDER_STAGE2,3,3,1,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C32_tender_cap_or_offer_deadline_4B_overlay,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,1,near-tender-price close plus offer deadline caps upside even while theme is hot,marks SM tender cap as good 4B and Korea Zinc first cap as watch-only,R11L15_C32_SM_041510_T2_KAKAO_TENDER_CAP_4B|R11L15_C32_KZ_010130_T2_COURT_BUYBACK_4B_TOO_EARLY,2,2,0,medium,canonical_shadow_only,split local vs full-window proximity before full 4B
shadow_weight,C32_policy_rescue_dilution_overhang_no_green_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,1,state-backed rescue/merger financing can be value destructive for holding-company minority holders,filters Hanjin KAL false positive,R11L15_C32_HK_180640_T1_KDB_ASIANA_POLICY_STAGE2_FALSE_POSITIVE,3,3,1,medium,canonical_shadow_only,do not promote to Green without minority-upside route and clean capital structure
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R11L15_C32_SM_041510", "symbol": "041510", "company_name": "에스엠", "round": "R11", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "K_CONTENT_CONTROL_PREMIUM_TENDER_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R11L15_C32_SM_041510_T1_HYBE_STAKE_TENDER_STAGE2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2 control-premium evidence worked, but later tender cap was needed to stop treating control battle as durable fundamental rerating.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Positive event route, but 4B cap was decisive."}
{"row_type": "case", "case_id": "R11L15_C32_KZ_010130", "symbol": "010130", "company_name": "고려아연", "round": "R11", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_BUYBACK_COUNTERBID_CONTROL_PREMIUM", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R11L15_C32_KZ_010130_T1_MBK_YP_TENDER_STAGE2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Initial tender evidence captured enormous MFE; first non-price 4B was locally sensible but full-window too early because control squeeze continued.", "current_profile_verdict": "current_profile_4B_too_early", "price_source": "Songdaiki/stock-web", "notes": "Positive but high-volatility control-squeeze residual."}
{"row_type": "case", "case_id": "R11L15_C32_HK_180640", "symbol": "180640", "company_name": "한진칼", "round": "R11", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "STATE_BACKED_RESCUE_MERGER_CONTROL_PREMIUM_DILUTION_GUARD", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R11L15_C32_HK_180640_T1_KDB_ASIANA_POLICY_STAGE2_FALSE_POSITIVE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Policy-backed control headline produced only brief MFE and large MAE; dilution/financing overhang should cap positive score.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Counterexample for policy rescue headline without minority-shareholder upside."}
{"row_type": "trigger", "trigger_id": "R11L15_C32_SM_041510_T1_HYBE_STAKE_TENDER_STAGE2", "case_id": "R11L15_C32_SM_041510", "symbol": "041510", "company_name": "에스엠", "round": "R11", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "K_CONTENT_CONTROL_PREMIUM_TENDER_CAP", "sector": "platform_content_event", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-10", "entry_date": "2023-02-10", "entry_price": 114700, "evidence_available_at_that_date": "HYBE/Lee Soo-man stake purchase and 120,000 KRW tender offer route created explicit control-premium price anchor before the later Kakao overbid.", "evidence_source": "AP: HYBE acquired 14.8% stake and planned to purchase additional shares at 120,000 KRW; Kakao later countered at 150,000 KRW.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 40.54, "MFE_90D_pct": 40.54, "MFE_180D_pct": 40.54, "MFE_1Y_pct": 40.54, "MFE_2Y_pct": null, "MAE_30D_pct": -21.1, "MAE_90D_pct": -21.1, "MAE_180D_pct": -21.1, "MAE_1Y_pct": -28.07, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -46.46, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_entry_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_with_later_tender_cap_pullback", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L15_C32_SM_041510_2023-02-10_114700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R11L15_C32_SM_041510_T2_KAKAO_TENDER_CAP_4B", "case_id": "R11L15_C32_SM_041510", "symbol": "041510", "company_name": "에스엠", "round": "R11", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "K_CONTENT_CONTROL_PREMIUM_TENDER_CAP", "sector": "platform_content_event", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "4B_non_price_requirement_stress_test|counterexample_mining", "trigger_type": "Stage4B", "trigger_date": "2023-03-07", "entry_date": "2023-03-07", "entry_price": 149700, "evidence_available_at_that_date": "Kakao launched a 150,000 KRW/share tender offer for up to 35%; stock closed almost exactly at tender price, creating explicit event cap.", "evidence_source": "AP: Kakao tender offer at 150,000 KRW/share and SM shares jumped to 149,700 KRW on the announcement.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["explicit_event_cap", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.68, "MFE_90D_pct": 7.68, "MFE_180D_pct": 7.68, "MFE_1Y_pct": 7.68, "MFE_2Y_pct": null, "MAE_30D_pct": -39.55, "MAE_90D_pct": -39.55, "MAE_180D_pct": -42.35, "MAE_1Y_pct": -44.89, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -46.46, "green_lateness_ratio": "not_applicable:4B_overlay", "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.75, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["explicit_event_cap", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_success_if_tender_cap_breaks_after_acceptance_end", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L15_C32_SM_041510_2023-03-07_149700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_4B_cap", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R11L15_C32_KZ_010130_T1_MBK_YP_TENDER_STAGE2", "case_id": "R11L15_C32_KZ_010130", "symbol": "010130", "company_name": "고려아연", "round": "R11", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_BUYBACK_COUNTERBID_CONTROL_PREMIUM", "sector": "materials_governance_event", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-13", "entry_date": "2024-09-13", "entry_price": 666000, "evidence_available_at_that_date": "MBK Partners and Young Poong launched tender offer at 660,000 KRW/share for 6.98%~14.61%; stock moved to the tender anchor immediately.", "evidence_source": "Reuters: MBK/Young Poong tender offer at 660,000 KRW/share; Korea Zinc denounced it as hostile.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 131.68, "MFE_90D_pct": 261.41, "MFE_180D_pct": 261.41, "MFE_1Y_pct": 261.41, "MFE_2Y_pct": null, "MAE_30D_pct": -1.65, "MAE_90D_pct": -1.65, "MAE_180D_pct": -3.45, "MAE_1Y_pct": -3.45, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_entry_trigger", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_with_extreme_control_squeeze", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L15_C32_KZ_010130_2024-09-13_666000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R11L15_C32_KZ_010130_T2_COURT_BUYBACK_4B_TOO_EARLY", "case_id": "R11L15_C32_KZ_010130", "symbol": "010130", "company_name": "고려아연", "round": "R11", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOSTILE_TENDER_BUYBACK_COUNTERBID_CONTROL_PREMIUM", "sector": "materials_governance_event", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "4B_non_price_requirement_stress_test|residual_false_positive_mining", "trigger_type": "Stage4B", "trigger_date": "2024-10-21", "entry_date": "2024-10-21", "entry_price": 877000, "evidence_available_at_that_date": "Court rejected Young Poong request to block Korea Zinc buyback/tender countermeasure; price approached 890,000 KRW tender offer area but control squeeze was not finished.", "evidence_source": "Reuters: court cleared hurdle for Korea Zinc buyback offer; stock closed 877,000 KRW near 890,000 KRW tender offer price.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["explicit_event_cap", "legal_or_regulatory_block", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 74.91, "MFE_90D_pct": 174.46, "MFE_180D_pct": 174.46, "MFE_1Y_pct": 174.46, "MFE_2Y_pct": null, "MAE_30D_pct": -15.74, "MAE_90D_pct": -15.74, "MAE_180D_pct": -26.68, "MAE_1Y_pct": -26.68, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": "not_applicable:4B_overlay", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.12, "four_b_timing_verdict": "price_only_or_first_tender_cap_4B_too_early_for_full_window", "four_b_evidence_type": ["explicit_event_cap", "legal_or_regulatory_block", "positioning_overheat"], "four_c_protection_label": "hard_4c_late_if_only_after_squeeze_collapse", "trigger_outcome_label": "4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L15_C32_KZ_010130_2024-10-21_877000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_4B_timing_residual", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R11L15_C32_HK_180640_T1_KDB_ASIANA_POLICY_STAGE2_FALSE_POSITIVE", "case_id": "R11L15_C32_HK_180640", "symbol": "180640", "company_name": "한진칼", "round": "R11", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "STATE_BACKED_RESCUE_MERGER_CONTROL_PREMIUM_DILUTION_GUARD", "sector": "airline_policy_restructuring_event", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "counterexample_mining|residual_false_positive_mining|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-11-16", "entry_date": "2020-11-16", "entry_price": 82200, "evidence_available_at_that_date": "South Korean state-backed Asiana/Korean Air consolidation and KDB financing created control-premium and policy rescue headline, but minority-shareholder upside was diluted by financing/regulatory burden.", "evidence_source": "Reuters/Wikipedia summary: government-backed Korean Air-Asiana merger initiated Nov 16 2020; Korea Development Bank agreed to invest/fund Hanjin Group.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["dilution_or_cb", "capital_raise_or_overhang", "legal_or_regulatory_block"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv", "profile_path": "atlas/symbol_profiles/180/180640.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.18, "MFE_90D_pct": 16.18, "MFE_180D_pct": 16.18, "MFE_1Y_pct": 16.18, "MFE_2Y_pct": null, "MAE_30D_pct": -27.74, "MAE_90D_pct": -31.75, "MAE_180D_pct": -39.84, "MAE_1Y_pct": -39.84, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-11-16", "peak_price": 95500, "drawdown_after_peak_pct": -48.22, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "policy_rescue_headline_not_full_4B_without_dilution_guard", "four_b_evidence_type": ["dilution_or_cb", "capital_raise_or_overhang", "legal_or_regulatory_block"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_green_or_stage2_promotion", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L15_C32_HK_180640_2020-11-16_82200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L15_C32_SM_041510", "trigger_id": "R11L15_C32_SM_041510_T1_HYBE_STAKE_TENDER_STAGE2", "symbol": "041510", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 8, "policy_or_regulatory_score": 8, "valuation_repricing_score": 18, "execution_risk_score": 0, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 8, "policy_or_regulatory_score": 8, "valuation_repricing_score": 18, "execution_risk_score": -1, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable", "changed_components": ["valuation_repricing_score", "legal_or_contract_risk_score", "dilution_cb_risk_score", "execution_risk_score"], "component_delta_explanation": "C32 shadow adds explicit tender-cap recognition and penalizes policy-rescue/dilution/legal-overhang evidence that cannot translate into durable minority-shareholder upside.", "MFE_90D_pct": 40.54, "MAE_90D_pct": -21.1, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L15_C32_SM_041510", "trigger_id": "R11L15_C32_SM_041510_T2_KAKAO_TENDER_CAP_4B", "symbol": "041510", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 22, "execution_risk_score": 0, "legal_or_contract_risk_score": -4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 22, "execution_risk_score": -8, "legal_or_contract_risk_score": -10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 69, "stage_label_after": "Stage4B-Overlay", "changed_components": ["valuation_repricing_score", "legal_or_contract_risk_score", "dilution_cb_risk_score", "execution_risk_score"], "component_delta_explanation": "C32 shadow adds explicit tender-cap recognition and penalizes policy-rescue/dilution/legal-overhang evidence that cannot translate into durable minority-shareholder upside.", "MFE_90D_pct": 7.68, "MAE_90D_pct": -39.55, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L15_C32_KZ_010130", "trigger_id": "R11L15_C32_KZ_010130_T1_MBK_YP_TENDER_STAGE2", "symbol": "010130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 20, "execution_risk_score": 0, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 20, "execution_risk_score": 0, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable", "changed_components": ["valuation_repricing_score", "legal_or_contract_risk_score", "dilution_cb_risk_score", "execution_risk_score"], "component_delta_explanation": "C32 shadow adds explicit tender-cap recognition and penalizes policy-rescue/dilution/legal-overhang evidence that cannot translate into durable minority-shareholder upside.", "MFE_90D_pct": 261.41, "MAE_90D_pct": -1.65, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L15_C32_KZ_010130", "trigger_id": "R11L15_C32_KZ_010130_T2_COURT_BUYBACK_4B_TOO_EARLY", "symbol": "010130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 24, "execution_risk_score": 0, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 85, "stage_label_before": "Stage3-Yellow/4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 24, "execution_risk_score": -8, "legal_or_contract_risk_score": -10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72, "stage_label_after": "Stage4B-watch-only", "changed_components": ["valuation_repricing_score", "legal_or_contract_risk_score", "dilution_cb_risk_score", "execution_risk_score"], "component_delta_explanation": "C32 shadow adds explicit tender-cap recognition and penalizes policy-rescue/dilution/legal-overhang evidence that cannot translate into durable minority-shareholder upside.", "MFE_90D_pct": 174.46, "MAE_90D_pct": -15.74, "score_return_alignment_label": "residual_misalignment", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L15_C32_HK_180640", "trigger_id": "R11L15_C32_HK_180640_T1_KDB_ASIANA_POLICY_STAGE2_FALSE_POSITIVE", "symbol": "180640", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 20, "valuation_repricing_score": 14, "execution_risk_score": 0, "legal_or_contract_risk_score": -4, "dilution_cb_risk_score": -4, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 20, "valuation_repricing_score": 8, "execution_risk_score": -8, "legal_or_contract_risk_score": -10, "dilution_cb_risk_score": -12, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "Stage2-Watch/No-Promote", "changed_components": ["valuation_repricing_score", "legal_or_contract_risk_score", "dilution_cb_risk_score", "execution_risk_score"], "component_delta_explanation": "C32 shadow adds explicit tender-cap recognition and penalizes policy-rescue/dilution/legal-overhang evidence that cannot translate into durable minority-shareholder upside.", "MFE_90D_pct": 16.18, "MAE_90D_pct": -31.75, "score_return_alignment_label": "residual_misalignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R11", "loop": "15", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "scheduled_round": "R11", "scheduled_loop": "15", "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 1, "current_profile_error_count": 2, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["policy_rescue_false_positive", "4B_too_early_when_control_squeeze_continues", "tender_cap_needs_separate_overlay"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R11
completed_loop = 15
next_round = R12
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

### Stock-Web

- Songdaiki/stock-web `atlas/manifest.json`: `max_date=2026-02-20`, `price_adjustment_status=raw_unadjusted_marcap`, `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`.
- Songdaiki/stock-web `atlas/schema.json`: MFE/MAE formulas and calibration-usable rules.
- Symbol profiles:
  - `atlas/symbol_profiles/041/041510.json`
  - `atlas/symbol_profiles/010/010130.json`
  - `atlas/symbol_profiles/180/180640.json`
  - rejected diagnostic only: `atlas/symbol_profiles/020/020560.json`
- OHLC shards:
  - `atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/180/180640/2021.csv`

### Historical evidence

- AP, 2023-02-22: HYBE completed purchase of 14.8% SM stake and planned tender route.
- AP, 2023-03-07: Kakao tender offer for up to 35% of SM at 150,000 KRW/share; SM close at 149,700 KRW.
- Reuters, 2024-09-13: MBK/Young Poong tender offer for Korea Zinc at 660,000 KRW/share.
- Reuters, 2024-10-21: Korea Zinc shares near 890,000 KRW tender/buyback offer area after court rejected block request.
- Reuters/Wikipedia summary, 2020/2024: Korean Air-Asiana state-backed consolidation, KDB financing, and eventual completion after regulatory approvals.


