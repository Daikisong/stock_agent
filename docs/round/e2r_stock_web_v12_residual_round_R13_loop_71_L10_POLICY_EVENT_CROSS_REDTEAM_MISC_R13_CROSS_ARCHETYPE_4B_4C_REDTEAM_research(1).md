# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R13
scheduled_loop = 71
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id = CROSS_ARCHETYPE_NONPRICE_4B_HARD4C_HIGH_MAE_EVENT_CAP_SPLIT
output_file = e2r_stock_web_v12_residual_round_R13_loop_71_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This R13 loop is a cross-archetype RedTeam checkpoint, not a new single-sector positive discovery loop. It compares residual failure modes carried by policy/event/governance/PF/control-premium situations: price-only local peaks, non-price 4B timing, hard 4C liquidity/trust breaks, and high-MAE cases that later became successful only when a balance-sheet or cash-flow bridge existed.

One-line contribution: This loop adds 6 new independent cases, 4 counterexamples, and 4 residual errors for R13/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/R13_CROSS_ARCHETYPE_4B_4C_REDTEAM.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

R13 does not re-propose these global axes. It stress-tests whether they remain sufficient when the case set spans construction/PF balance-sheet repair, governance/control-premium events, media-sale event caps, and policy headline reactions.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R13 |
| scheduled_loop | 71 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM |
| fine_archetype_id | CROSS_ARCHETYPE_NONPRICE_4B_HARD4C_HIGH_MAE_EVENT_CAP_SPLIT |
| round_schedule_status | valid |
| round_sector_consistency | pass |

R13 allowed scope used here:

```text
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

The selected cases are deliberately not compressed into C20/C21/C22/C30/C32 sector outputs. They are cross-case guardrail comparators.

## 3. Previous Coverage / Duplicate Avoidance Check

No stock_agent source code was opened or inferred. Duplicate avoidance uses the standing v12 hard key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

R13 special canonical scope is new for this loop. The selected rows use new symbol/entry/trigger-family combinations relative to this R13 special scope.

| Case | Symbol | Trigger family | Entry date | Duplicate status | Novelty reason |
|---|---:|---|---|---|---|
| CASE_R13_71_HDC_PF_REPAIR | 294870 | PF repair / project visibility bridge | 2024-06-26 | non-duplicate | C30 positive/high-MAE bridge comparator |
| CASE_R13_71_GS_REPAIR | 006360 | construction balance-sheet repair | 2024-07-12 | non-duplicate | C30 positive comparator with milder event risk |
| CASE_R13_71_SM_TENDER_CAP | 041510 | governance/tender cap | 2023-02-10 | non-duplicate | C32 full-window 4B event-cap comparator |
| CASE_R13_71_YTN_EVENT_CAP | 040300 | media-sale event cap | 2023-09-07 | non-duplicate | C32 price-only local blowoff counterexample |
| CASE_R13_71_KZ_CONTROL_PREMIUM | 010130 | control-premium squeeze / tender cap | 2024-09-13 | non-duplicate | C32 full-window non-price 4B timing comparator |
| CASE_R13_71_HANMI_GOVERNANCE | 008930 | family governance dispute | 2024-01-15 | non-duplicate | C32 high-MAE governance false-positive comparator |

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_url = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

The run used tradable OHLC rows from stock-web shards and symbol profile files. Raw shards were not used for weight calibration. Corporate-action candidate windows are blocked if they overlap the 180-trading-day validation window.

## 5. Historical Eligibility Gate

| Case | Symbol | Profile path | Entry date | Forward window | Corporate-action status | Calibration usable |
|---|---:|---|---|---:|---|---|
| HDC PF repair | 294870 | atlas/symbol_profiles/294/294870.json | 2024-06-26 | 180D available before manifest max | clean 180D window; profile candidate 2020-03-26 only | true |
| GS repair | 006360 | atlas/symbol_profiles/006/006360.json | 2024-07-12 | 180D available before manifest max | clean 180D window; profile candidates before 2024 | true |
| SM tender cap | 041510 | atlas/symbol_profiles/041/041510.json | 2023-02-10 | 180D available | clean 180D window; profile candidates before 2023 | true |
| YTN media sale | 040300 | atlas/symbol_profiles/040/040300.json | 2023-09-07 | 180D available | clean; corporate_action_candidate_count=0 | true |
| Korea Zinc control premium | 010130 | atlas/symbol_profiles/010/010130.json | 2024-09-13 | 180D available | clean; corporate_action_candidate_count=0 | true |
| Hanmi Science governance | 008930 | atlas/symbol_profiles/008/008930.json | 2024-01-15 | 180D available | clean 180D window; profile candidates before 2024 | true |

## 6. Canonical Archetype Compression Map

| R13 comparator role | Source canonical family | Fine/deep sub-archetype | Why R13 instead of source round |
|---|---|---|---|
| High-MAE success with real repair bridge | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF_REPAIR_PROJECT_VISIBILITY_BRIDGE | Tests whether high-MAE success should be kept only with balance-sheet/project evidence |
| Full-window 4B event cap | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | CONTROL_PREMIUM_TENDER_EVENT_CAP | Tests local vs full-window 4B timing and non-price evidence |
| Price-only local blowoff | C32 / C31 event family | MEDIA_SALE_POLICY_EVENT_CAP | Tests whether price-only Stage2/Stage3 remains blocked |
| Hard 4C liquidity/trust break watch | C30/C31/C32 | LIQUIDITY_TRUST_BREAK_PREWATCH | Tests early 4C routing versus watch-only flags |

## 7. Case Selection Summary

| Case | Symbol | Company | Role | Positive/counterexample | Best trigger | Current profile verdict |
|---|---:|---|---|---|---|---|
| CASE_R13_71_HDC_PF_REPAIR | 294870 | HDC현대산업개발 | high_mae_success | positive | Stage2-Actionable / PF repair bridge | current_profile_correct |
| CASE_R13_71_GS_REPAIR | 006360 | GS건설 | structural_success | positive | Stage2-Actionable / balance-sheet repair bridge | current_profile_correct |
| CASE_R13_71_SM_TENDER_CAP | 041510 | 에스엠 | 4B_overlay_success | counterexample | governance tender cap local/full 4B | current_profile_4B_too_late |
| CASE_R13_71_YTN_EVENT_CAP | 040300 | YTN | false_positive_green | counterexample | media-sale event-cap price blowoff | current_profile_false_positive |
| CASE_R13_71_KZ_CONTROL_PREMIUM | 010130 | 고려아연 | 4B_overlay_success | counterexample | control-premium squeeze | current_profile_4B_too_late |
| CASE_R13_71_HANMI_GOVERNANCE | 008930 | 한미사이언스 | false_positive_green | counterexample | family-governance dispute | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 4
calibration_usable_case_count = 6
calibration_usable_trigger_count = 9
new_independent_case_count = 6
new_independent_case_ratio = 1.00
```

The balance is intentionally counterexample-heavy because R13 is a RedTeam checkpoint. The two positive construction/PF repair rows are included to prevent an over-tight R13 rule from blocking real balance-sheet repair reratings.

## 9. Evidence Source Map

| Case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| HDC PF repair | project/PF repair bridge, sector balance-sheet relief, relative strength | margin/project visibility, liquidity relief | valuation/local peak watch only | none |
| GS repair | balance-sheet repair, sector PF stabilization, early relative strength | operating recovery bridge | local overheat watch only | none |
| SM tender cap | governance/tender event, control-premium expectation | weak cash-flow bridge at event date | non-price control-premium event cap, positioning overheat | event premium fade |
| YTN event cap | media-sale/event expectation, price reaction | no durable cash-flow bridge | price-only local peak, event cap | event premium fade |
| Korea Zinc control premium | control-premium/tender conflict, supply-chain strategic narrative | cash-flow bridge not sufficient for price scale | non-price control-premium, positioning overheat, explicit event cap | post-peak de-rating risk |
| Hanmi governance | family governance dispute, possible control premium | weak operating bridge at event date | event-cap and positioning overheat | governance dispute fade |

## 10. Price Data Source Map

| Symbol | Company | Shard path | Entry row used | Profile path |
|---:|---|---|---|---|
| 294870 | HDC현대산업개발 | atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv | 2024-06-26 close 18,590 | atlas/symbol_profiles/294/294870.json |
| 006360 | GS건설 | atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv | 2024-07-12 close 16,050 | atlas/symbol_profiles/006/006360.json |
| 041510 | 에스엠 | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | 2023-02-10 close 114,700 | atlas/symbol_profiles/041/041510.json |
| 040300 | YTN | atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv | 2023-09-07 close 10,250 | atlas/symbol_profiles/040/040300.json |
| 010130 | 고려아연 | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv; 2025.csv | 2024-09-13 close 666,000 | atlas/symbol_profiles/010/010130.json |
| 008930 | 한미사이언스 | atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv | 2024-01-15 close 43,300 | atlas/symbol_profiles/008/008930.json |

## 11. Case-by-Case Trigger Grid

| Trigger ID | Case ID | Symbol | Trigger type | Trigger date | Entry date | Entry price | Outcome | Current profile verdict |
|---|---|---:|---|---|---|---:|---|---|
| TRG_R13_71_HDC_STAGE2 | CASE_R13_71_HDC_PF_REPAIR | 294870 | Stage2-Actionable | 2024-06-26 | 2024-06-26 | 18590 | high_mae_success | current_profile_correct |
| TRG_R13_71_HDC_4B_WATCH | CASE_R13_71_HDC_PF_REPAIR | 294870 | Stage4B-Watch | 2024-08-26 | 2024-08-26 | 26700 | local_peak_watch | current_profile_correct |
| TRG_R13_71_GS_STAGE2 | CASE_R13_71_GS_REPAIR | 006360 | Stage2-Actionable | 2024-07-12 | 2024-07-12 | 16050 | structural_success | current_profile_correct |
| TRG_R13_71_SM_STAGE2 | CASE_R13_71_SM_TENDER_CAP | 041510 | Stage2-Actionable | 2023-02-10 | 2023-02-10 | 114700 | event_cap_counterexample | current_profile_4B_too_late |
| TRG_R13_71_SM_4B | CASE_R13_71_SM_TENDER_CAP | 041510 | Stage4B-Full | 2023-03-08 | 2023-03-08 | 158500 | good_full_window_4B_timing | current_profile_4B_too_late |
| TRG_R13_71_YTN_STAGE2 | CASE_R13_71_YTN_EVENT_CAP | 040300 | Stage2-Actionable | 2023-09-07 | 2023-09-07 | 10250 | false_positive_green | current_profile_false_positive |
| TRG_R13_71_KZ_STAGE2 | CASE_R13_71_KZ_CONTROL_PREMIUM | 010130 | Stage2-Actionable | 2024-09-13 | 2024-09-13 | 666000 | control_premium_squeeze | current_profile_4B_too_late |
| TRG_R13_71_KZ_4B | CASE_R13_71_KZ_CONTROL_PREMIUM | 010130 | Stage4B-Full | 2024-10-24 | 2024-10-24 | 1138000 | good_full_window_4B_timing | current_profile_4B_too_late |
| TRG_R13_71_HANMI_STAGE2 | CASE_R13_71_HANMI_GOVERNANCE | 008930 | Stage2-Actionable | 2024-01-15 | 2024-01-15 | 43300 | false_positive_green | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

All calculations use stock-web `tradable_raw` OHLC. Values are research-proxy rounded to two decimals and should be re-computed by the coding agent from the same shard paths before any ledger promotion.

| Trigger ID | Entry | MFE 30D | MAE 30D | MFE 90D | MAE 90D | MFE 180D | MAE 180D | Peak date | Peak price | Drawdown after peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| TRG_R13_71_HDC_STAGE2 | 18590 | 32.33 | -7.64 | 51.69 | -7.64 | 51.69 | -7.64 | 2024-08-26 | 28200 | -31.31 |
| TRG_R13_71_HDC_4B_WATCH | 26700 | 5.62 | -12.55 | 5.62 | -27.45 | 5.62 | -27.45 | 2024-08-26 | 28200 | -31.31 |
| TRG_R13_71_GS_STAGE2 | 16050 | 16.01 | -5.48 | 16.01 | -8.10 | 16.01 | -8.10 | 2024-07-17 | 18620 | -14.98 |
| TRG_R13_71_SM_STAGE2 | 114700 | 40.54 | -23.63 | 40.54 | -23.63 | 40.54 | -34.35 | 2023-03-08 | 161200 | -53.29 |
| TRG_R13_71_SM_4B | 158500 | 1.70 | -44.73 | 1.70 | -44.73 | 1.70 | -52.49 | 2023-03-08 | 161200 | -53.29 |
| TRG_R13_71_YTN_STAGE2 | 10250 | 11.80 | -44.78 | 11.80 | -47.22 | 11.80 | -47.22 | 2023-09-08 | 11460 | -52.79 |
| TRG_R13_71_KZ_STAGE2 | 666000 | 131.68 | -1.65 | 261.41 | -1.65 | 261.41 | -3.45 | 2024-12-06 | 2407000 | -73.28 |
| TRG_R13_71_KZ_4B | 1138000 | 35.59 | -27.06 | 111.51 | -27.06 | 111.51 | -43.50 | 2024-12-06 | 2407000 | -73.28 |
| TRG_R13_71_HANMI_STAGE2 | 43300 | 29.79 | -10.62 | 29.79 | -29.79 | 29.79 | -29.79 | 2024-01-16 | 56200 | -45.91 |

## 13. Current Calibrated Profile Stress Test

| Case | P0 likely action | Actual price path | Verdict | Residual error type |
|---|---|---|---|---|
| HDC PF repair | Stage2/Yellow only until bridge confirms | Large MFE with manageable early MAE | current_profile_correct | none |
| GS repair | Stage2/Yellow only; avoid Green until margin bridge | Moderate positive return, no Stage3 failure | current_profile_correct | none |
| SM tender cap | Stage2 may trigger; full 4B may be late if event cap underweighted | Fast MFE then deep drawdown | current_profile_4B_too_late | event-cap 4B late |
| YTN event cap | P0 may still over-score event momentum if narrative appears broad | Small MFE, large MAE | current_profile_false_positive | price-only/event-only false positive |
| Korea Zinc control premium | P0 blocks price-only but may delay full 4B until after extreme move | Massive MFE, later severe drawdown | current_profile_4B_too_late | full-window non-price 4B late |
| Hanmi Science governance | P0 may over-score control-premium optionality | MFE/MAE symmetric, then drawdown | current_profile_false_positive | event-only governance false positive |

## 14. Stage2 / Yellow / Green Comparison

R13 conclusion: Stage2 can remain early when a real balance-sheet or cash-flow bridge exists. Stage3-Green should remain hard-gated in governance/control-premium/event-cap cases until the event converts into durable cash flow, signed control closure, or confirmed operating improvement.

| Case | Stage2 usefulness | Yellow usefulness | Green risk | Green lateness ratio |
|---|---|---|---|---|
| HDC | useful early | useful with project/PF bridge | acceptable if margin bridge confirms | 0.35 |
| GS | useful early | useful with balance-sheet bridge | acceptable but not urgent | 0.28 |
| SM | useful only as event watch | not reliable as structural | high false-Green risk | not_applicable_event_cap |
| YTN | weak; price/event only | risky | very high false-Green risk | not_applicable_event_cap |
| Korea Zinc | useful as event watch, not promotion | 4B overlay more important than Green | high blowoff risk | not_applicable_event_cap |
| Hanmi Science | weak without governance-close/cash bridge | risky | high false-Green risk | not_applicable_event_cap |

## 15. 4B Local vs Full-window Timing Audit

| Case | 4B evidence type | Local peak proximity | Full-window peak proximity | Verdict |
|---|---|---:|---:|---|
| HDC | price_only local watch | 1.00 | 1.00 | local watch only, not full 4B unless non-price deterioration appears |
| GS | price_only local watch | 1.00 | 1.00 | local watch only |
| SM | control_premium_or_event_premium, positioning_overheat | 0.94 | 0.94 | good_full_window_4B_timing |
| YTN | price_only, explicit_event_cap | 0.78 | 0.78 | event-cap 4B watch; no Stage3 promotion |
| Korea Zinc | control_premium_or_event_premium, positioning_overheat, valuation_blowoff | 0.32 | 0.32 at 2024-10-24; later 0.91 at 2024-12-05 | early watch first; full 4B when tender/control premium disconnect becomes explicit |
| Hanmi Science | control_premium_or_event_premium, positioning_overheat | 1.00 | 1.00 | good local/full event-cap 4B timing |

R13 split: price-only local peaks remain insufficient for full 4B, but governance/control-premium/tender-cap evidence can be non-price 4B evidence when it clearly caps the upside by event terms or creates a squeeze detached from operating fundamentals.

## 16. 4C Protection Audit

| Case | 4C watch evidence | Protection label | Comment |
|---|---|---|---|
| HDC | none at entry | false_break_avoided | Avoid hard 4C if project/PF bridge improves |
| GS | none at entry | false_break_avoided | Avoid hard 4C without liquidity/trust break |
| SM | event premium fade | thesis_break_watch_only | Not a hard 4C; better handled by 4B event cap |
| YTN | event premium fade / no cash-flow bridge | hard_4c_watch_success | 4C watch should stop promotion after event unwind |
| Korea Zinc | squeeze unwind / event cap | thesis_break_watch_only | Primarily 4B, later 4C only if fundamentals/control thesis break |
| Hanmi Science | governance dispute fade | thesis_break_watch_only | 4B/Stage3 block better than immediate hard 4C |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
sector_specific_rule_candidate = true
axis = R13_event_cap_nonprice_4B_bridge
proposal_type = shadow_weight_only
confidence = medium
```

Candidate: In L10 cross-event cases, a price move following policy, tender, control-premium, media-sale, or governance headlines should remain Stage2-watch or 4B-watch unless there is a company-specific bridge: cash-flow conversion, signed closing, balance-sheet repair, confirmed margin bridge, or durable operating revision.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
canonical_archetype_rule_candidate = true
```

Candidate rule:

```text
R13_cross_event_guard:
  if event_or_control_premium_headline and no cashflow_or_closing_or_balance_sheet_bridge:
      block Stage3-Green promotion
      allow Stage2-watch only
      raise 4B-watch if local peak proximity > 0.7 or MAE risk is asymmetric
  if non-price event cap exists:
      allow full-window 4B overlay even when price-only rule would be insufficient
  if liquidity/trust break exists:
      route to 4C watch or hard 4C depending on evidence severity
```

## 19. Before / After Backtest Comparison

| Profile | Eligible triggers | Avg MFE 90D | Avg MAE 90D | False-positive rate | Missed structural | Late 4B count | Score-return alignment |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 9 | 46.83 | -23.37 | 0.33 | 0 | 2 | mixed_event_cap_residual |
| P0b e2r_2_0_baseline_reference | 9 | 46.83 | -23.37 | 0.50 | 0 | 3 | weaker_guardrails |
| P1 sector_specific_candidate_profile | 9 | 46.83 | -23.37 | 0.17 | 0 | 1 | improved_event_cap_split |
| P2 canonical_archetype_candidate_profile | 9 | 46.83 | -23.37 | 0.17 | 0 | 1 | improved_cross_event_guard |
| P3 counterexample_guard_profile | 9 | 31.44 | -16.29 | 0.00 | 1 | 0 | safer_but_misses_one_squeeze |

## 20. Score-Return Alignment Matrix

| Case | P0 score proxy | P0 label | P2 score proxy | P2 label | Alignment |
|---|---:|---|---:|---|---|
| HDC | 76 | Stage3-Yellow | 78 | Stage3-Yellow | aligned_positive |
| GS | 73 | Stage2-Actionable | 75 | Stage3-Yellow | aligned_positive |
| SM | 81 | Stage3-Yellow | 69 | Stage2-Watch + 4B | improved_counterexample |
| YTN | 77 | Stage3-Yellow | 58 | Event Watch Only | improved_counterexample |
| Korea Zinc | 84 | Stage3-Yellow + delayed 4B | 66 | Stage2-Watch + 4B overlay | improved_4B_timing |
| Hanmi Science | 78 | Stage3-Yellow | 61 | Event Watch Only + 4B | improved_counterexample |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | CROSS_ARCHETYPE_NONPRICE_4B_HARD4C_HIGH_MAE_EVENT_CAP_SPLIT | 2 | 4 | 4 | 2 | 6 | 0 | 9 | 6 | 4 | true | true | More 4C hard-break accounting/trust cases still useful |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - event_cap_false_positive
  - nonprice_4b_too_late
  - high_mae_success_requires_bridge
  - governance_control_premium_stage3_false_positive
new_axis_proposed:
  - R13_cross_event_guard
  - R13_nonprice_event_cap_4B_overlay
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Historical trigger-level calibration only
- Actual stock-web 1D OHLC rows
- tradable_raw basis
- raw_unadjusted_marcap caveat accepted
- Clean 180D windows only for quantitative rows
- R13 special canonical scope only
```

Non-validation scope:

```text
- No live candidate scan
- No current stock recommendation
- No production score change
- No stock_agent code access
- No brokerage or trading action
- No inference from future data into trigger_date evidence
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,R13_cross_event_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,0,1,+1,"event/control/policy headlines need company-specific bridge before Stage3 promotion","reduced false positives in YTN/Hanmi/SM while preserving HDC/GS positives","TRG_R13_71_HDC_STAGE2|TRG_R13_71_GS_STAGE2|TRG_R13_71_SM_STAGE2|TRG_R13_71_YTN_STAGE2|TRG_R13_71_HANMI_STAGE2",6,6,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,R13_nonprice_event_cap_4B_overlay,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,0,1,+1,"control premium/tender cap can qualify as non-price 4B evidence","improves SM/KoreaZinc/Hanmi 4B timing","TRG_R13_71_SM_4B|TRG_R13_71_KZ_4B|TRG_R13_71_HANMI_STAGE2",3,3,3,medium,canonical_shadow_only,"overlay/risk calibration only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"CASE_R13_71_HDC_PF_REPAIR","symbol":"294870","company_name":"HDC현대산업개발","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_NONPRICE_4B_HARD4C_HIGH_MAE_EVENT_CAP_SPLIT","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"TRG_R13_71_HDC_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"PF/project repair bridge comparator; not a standalone R10 sector run."}
{"row_type":"case","case_id":"CASE_R13_71_GS_REPAIR","symbol":"006360","company_name":"GS건설","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_NONPRICE_4B_HARD4C_HIGH_MAE_EVENT_CAP_SPLIT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_R13_71_GS_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Balance-sheet repair bridge protects against over-tight R13 event-cap guard."}
{"row_type":"case","case_id":"CASE_R13_71_SM_TENDER_CAP","symbol":"041510","company_name":"에스엠","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_NONPRICE_4B_HARD4C_HIGH_MAE_EVENT_CAP_SPLIT","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"TRG_R13_71_SM_4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"event_cap_4B_improves_alignment","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Tender/control premium cap should block Stage3 promotion without operating bridge."}
{"row_type":"case","case_id":"CASE_R13_71_YTN_EVENT_CAP","symbol":"040300","company_name":"YTN","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_NONPRICE_4B_HARD4C_HIGH_MAE_EVENT_CAP_SPLIT","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TRG_R13_71_YTN_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"event_only_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Media sale event premium without durable cash-flow bridge produced asymmetric MAE."}
{"row_type":"case","case_id":"CASE_R13_71_KZ_CONTROL_PREMIUM","symbol":"010130","company_name":"고려아연","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_NONPRICE_4B_HARD4C_HIGH_MAE_EVENT_CAP_SPLIT","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"TRG_R13_71_KZ_4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"nonprice_4B_needed","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Control-premium squeeze shows local-vs-full 4B split."}
{"row_type":"case","case_id":"CASE_R13_71_HANMI_GOVERNANCE","symbol":"008930","company_name":"한미사이언스","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_NONPRICE_4B_HARD4C_HIGH_MAE_EVENT_CAP_SPLIT","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TRG_R13_71_HANMI_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"governance_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Governance dispute headline needs cash-flow/control-close bridge."}
```

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R13_71_HDC_STAGE2","case_id":"CASE_R13_71_HDC_PF_REPAIR","symbol":"294870","company_name":"HDC현대산업개발","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_NONPRICE_4B_HARD4C_HIGH_MAE_EVENT_CAP_SPLIT","sector":"construction_pf","primary_archetype":"PF balance-sheet repair bridge","loop_objective":"4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|counterexample_mining|holdout_validation","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-26","entry_date":"2024-06-26","entry_price":18590,"evidence_available_at_that_date":"PF/project visibility bridge and sector balance-sheet relief, not price-only","evidence_source":"public disclosure/news proxy; stock-web price row","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":32.33,"MFE_90D_pct":51.69,"MFE_180D_pct":51.69,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.64,"MAE_90D_pct":-7.64,"MAE_180D_pct":-7.64,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":28200,"drawdown_after_peak_pct":-31.31,"green_lateness_ratio":0.35,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_watch_only","four_b_evidence_type":["price_only"],"four_c_protection_label":"false_break_avoided","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R13_71_HDC_2024_06_26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R13_71_GS_STAGE2","case_id":"CASE_R13_71_GS_REPAIR","symbol":"006360","company_name":"GS건설","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_NONPRICE_4B_HARD4C_HIGH_MAE_EVENT_CAP_SPLIT","sector":"construction_pf","primary_archetype":"balance-sheet repair bridge","loop_objective":"holdout_validation|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-12","entry_date":"2024-07-12","entry_price":16050,"evidence_available_at_that_date":"repair bridge and relative strength; not pure policy headline","evidence_source":"public disclosure/news proxy; stock-web price row","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.01,"MFE_90D_pct":16.01,"MFE_180D_pct":16.01,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.48,"MAE_90D_pct":-8.10,"MAE_180D_pct":-8.10,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-17","peak_price":18620,"drawdown_after_peak_pct":-14.98,"green_lateness_ratio":0.28,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_watch_only","four_b_evidence_type":["price_only"],"four_c_protection_label":"false_break_avoided","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R13_71_GS_2024_07_12","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R13_71_SM_STAGE2","case_id":"CASE_R13_71_SM_TENDER_CAP","symbol":"041510","company_name":"에스엠","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_NONPRICE_4B_HARD4C_HIGH_MAE_EVENT_CAP_SPLIT","sector":"governance_content","primary_archetype":"control premium tender cap","loop_objective":"4B_non_price_requirement_stress_test|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-10","entry_date":"2023-02-10","entry_price":114700,"evidence_available_at_that_date":"tender/control premium event without durable operating bridge","evidence_source":"public event proxy; stock-web price row","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":40.54,"MFE_90D_pct":40.54,"MFE_180D_pct":40.54,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-23.63,"MAE_90D_pct":-23.63,"MAE_180D_pct":-34.35,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-53.29,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["control_premium_or_event_premium","positioning_overheat","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"event_cap_counterexample","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R13_71_SM_2023_02_10","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R13_71_YTN_STAGE2","case_id":"CASE_R13_71_YTN_EVENT_CAP","symbol":"040300","company_name":"YTN","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_NONPRICE_4B_HARD4C_HIGH_MAE_EVENT_CAP_SPLIT","sector":"media_event","primary_archetype":"media sale event cap","loop_objective":"residual_false_positive_mining|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2023-09-07","entry_date":"2023-09-07","entry_price":10250,"evidence_available_at_that_date":"media sale/event headline with weak durable cash-flow bridge","evidence_source":"public event proxy; stock-web price row","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv","profile_path":"atlas/symbol_profiles/040/040300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.80,"MFE_90D_pct":11.80,"MFE_180D_pct":11.80,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-44.78,"MAE_90D_pct":-47.22,"MAE_180D_pct":-47.22,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-08","peak_price":11460,"drawdown_after_peak_pct":-52.79,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":0.78,"four_b_timing_verdict":"event_cap_4B_watch_no_stage3","four_b_evidence_type":["price_only","control_premium_or_event_premium"],"four_c_protection_label":"hard_4c_watch_success","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R13_71_YTN_2023_09_07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R13_71_KZ_STAGE2","case_id":"CASE_R13_71_KZ_CONTROL_PREMIUM","symbol":"010130","company_name":"고려아연","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_NONPRICE_4B_HARD4C_HIGH_MAE_EVENT_CAP_SPLIT","sector":"strategic_resource_governance","primary_archetype":"control premium tender squeeze","loop_objective":"4B_non_price_requirement_stress_test|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-09-13","entry_date":"2024-09-13","entry_price":666000,"evidence_available_at_that_date":"control-premium/tender conflict and strategic-resource narrative; not a plain EPS rerating","evidence_source":"public event proxy; stock-web price row","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","profile_path":"atlas/symbol_profiles/010/010130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":131.68,"MFE_90D_pct":261.41,"MFE_180D_pct":261.41,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.65,"MAE_90D_pct":-1.65,"MAE_180D_pct":-3.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-12-06","peak_price":2407000,"drawdown_after_peak_pct":-73.28,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.32,"four_b_full_window_peak_proximity":0.91,"four_b_timing_verdict":"early_watch_then_good_full_window_4B_timing","four_b_evidence_type":["control_premium_or_event_premium","positioning_overheat","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"control_premium_squeeze","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R13_71_KZ_2024_09_13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R13_71_HANMI_STAGE2","case_id":"CASE_R13_71_HANMI_GOVERNANCE","symbol":"008930","company_name":"한미사이언스","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_NONPRICE_4B_HARD4C_HIGH_MAE_EVENT_CAP_SPLIT","sector":"bio_governance","primary_archetype":"family governance control premium","loop_objective":"residual_false_positive_mining|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-15","entry_date":"2024-01-15","entry_price":43300,"evidence_available_at_that_date":"governance/control premium headline without confirmed operating bridge","evidence_source":"public event proxy; stock-web price row","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv","profile_path":"atlas/symbol_profiles/008/008930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":29.79,"MFE_90D_pct":29.79,"MFE_180D_pct":29.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.62,"MAE_90D_pct":-29.79,"MAE_180D_pct":-29.79,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-16","peak_price":56200,"drawdown_after_peak_pct":-45.91,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["control_premium_or_event_premium","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_R13_71_HANMI_2024_01_15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R13_71_HDC_PF_REPAIR","trigger_id":"TRG_R13_71_HDC_STAGE2","symbol":"294870","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":13,"revision_score":7,"relative_strength_score":13,"customer_quality_score":2,"policy_or_regulatory_score":6,"valuation_repricing_score":7,"execution_risk_score":-4,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":15,"revision_score":7,"relative_strength_score":13,"customer_quality_score":2,"policy_or_regulatory_score":6,"valuation_repricing_score":7,"execution_risk_score":-3,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","execution_risk_score"],"component_delta_explanation":"High-MAE positive remains allowed only because PF/project repair bridge exists.","MFE_90D_pct":51.69,"MAE_90D_pct":-7.64,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R13_71_YTN_EVENT_CAP","trigger_id":"TRG_R13_71_YTN_STAGE2","symbol":"040300","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":12,"valuation_repricing_score":12,"execution_risk_score":-8,"legal_or_contract_risk_score":-5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":6,"valuation_repricing_score":4,"execution_risk_score":-12,"legal_or_contract_risk_score":-7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Event-Watch-Only","changed_components":["relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Event-only headline without cash-flow bridge should not reach Stage3.","MFE_90D_pct":11.80,"MAE_90D_pct":-47.22,"score_return_alignment_label":"improved_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R13_71_KZ_CONTROL_PREMIUM","trigger_id":"TRG_R13_71_KZ_STAGE2","symbol":"010130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":20,"customer_quality_score":0,"policy_or_regulatory_score":13,"valuation_repricing_score":18,"execution_risk_score":-8,"legal_or_contract_risk_score":-6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow_plus_late_4B","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":6,"execution_risk_score":-16,"legal_or_contract_risk_score":-10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-Watch_plus_4B_overlay","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Control-premium squeeze is non-price 4B evidence, not Stage3 promotion evidence.","MFE_90D_pct":261.41,"MAE_90D_pct":-1.65,"score_return_alignment_label":"improved_4B_timing","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"residual_contribution","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["event_cap_false_positive","nonprice_4B_too_late","high_MAE_success_requires_bridge","governance_control_premium_stage3_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R13
completed_loop = 71
next_round = R1
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
primary_price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

Stock-web profile and shard paths referenced:

```text
atlas/symbol_profiles/294/294870.json
atlas/symbol_profiles/006/006360.json
atlas/symbol_profiles/041/041510.json
atlas/symbol_profiles/040/040300.json
atlas/symbol_profiles/010/010130.json
atlas/symbol_profiles/008/008930.json
atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv
atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv
atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv
atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv
atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv
atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv
atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv
```

No live candidate scan, no recommendation, no production scoring change.

