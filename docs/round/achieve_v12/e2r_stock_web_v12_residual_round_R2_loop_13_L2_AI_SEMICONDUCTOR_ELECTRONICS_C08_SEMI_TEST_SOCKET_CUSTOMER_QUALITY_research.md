# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R2_loop_13_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
scheduled_round: R2
scheduled_loop: 13
completed_round: R2
completed_loop: 13
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: SEMI_TEST_SOCKET_CUSTOMER_QUALITY_HBM_AI_DEVICE_SOCKET_ROUTE
loop_objective:
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - yellow_threshold_stress_test
  - green_strictness_stress_test
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - counterexample_mining
  - coverage_gap_fill
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
production_scoring_changed: false
shadow_weight_only: true
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
round_schedule_status: valid
round_sector_consistency: pass
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

## 1. Current Calibrated Profile Assumption

The current proxy profile is treated as `e2r_2_1_stock_web_calibrated_proxy`, not the old E2R 2.0 baseline. The active global axes are assumed to be:

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

This file does not re-prove the global Stage2 bonus or Green lateness rule. It stress-tests a narrower R2/C08 residual: in AI-semiconductor test/socket names, **customer-quality language without confirmed design-in conversion or earnings bridge can still receive too much early credit**, while **high-quality socket names can remain structurally valid despite high post-peak MAE**.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R2 |
| scheduled_loop | 13 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY |
| fine_archetype_id | SEMI_TEST_SOCKET_CUSTOMER_QUALITY_HBM_AI_DEVICE_SOCKET_ROUTE |
| primary_archetype | semiconductor test socket / probe / package inspection customer-quality route |
| round-sector consistency | pass |

R2 maps to `L2_AI_SEMICONDUCTOR_ELECTRONICS`, so the round-sector pair is valid. The chosen canonical archetype is not C06/C07 HBM memory/equipment itself. It is adjacent to that cycle, but the focus is the socket/probe/inspection evidence quality layer.

## 3. Previous Coverage / Duplicate Avoidance Check

The accessible registry showed earlier R2 historical calibration files under `docs/round/e2r_stock_web_historical_calibration_round_R2_loop_8...9_ai_semiconductor_electronic_components_research.md`, but no existing v12 residual file matching `e2r_stock_web_v12_residual_round_R2_loop_13...`. `data/e2r/calibration/trigger_rows_representative.jsonl` was empty at the checked revision, so duplicate row-level symbol/trigger matching could not be performed from that artifact.

Selection therefore avoids simply rerunning the representative HBM memory pair and uses four C08-specific names:

| case_id | symbol | company | novelty rationale |
|---|---:|---|---|
| R2L13_C08_058470_STAGE2 | 058470 | 리노공업 | same sector, test socket quality route; not a memory maker trigger |
| R2L13_C08_095340_FP | 095340 | ISC | socket narrative false-positive stress test |
| R2L13_C08_131290_STAGE2 | 131290 | 티에스이 | probe/test interface route with high-MAE continuation risk |
| R2L13_C08_064290_FP | 064290 | 인텍플러스 | package inspection / test-adjacent false-positive stress test |

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest fields checked for this run:

| manifest field | value |
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
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Tradable shard schema used:

```text
d,o,h,l,c,v,a,mc,s,m
```

The backtest rows below use the `c` column as entry price, the maximum `h` for MFE, and the minimum `l` for MAE. All quantitative rows are based on `tradable_raw`, not adjusted prices.

## 5. Historical Eligibility Gate

| symbol | profile_path | profile last_date | corp action dates relevant to 180D window | 180D eligibility |
|---:|---|---:|---|---|
| 058470 | atlas/symbol_profiles/058/058470.json | 2026-02-20 | 2025-04-25 is outside 2024-02-16~D+180 | usable |
| 095340 | atlas/symbol_profiles/095/095340.json | 2026-02-20 | 2023-10-20 before trigger window | usable |
| 131290 | atlas/symbol_profiles/131/131290.json | 2026-02-20 | only 2011 historical candidates | usable |
| 064290 | atlas/symbol_profiles/064/064290.json | 2026-02-20 | none | usable |

All representative trigger rows have at least 180 forward trading days available inside stock-web manifest max date 2026-02-20. The 2Y column is marked `null` for rows where the full 504D window is not required for this v12 calibration slice or where a later corporate-action candidate would contaminate the longer window.

## 6. Canonical Archetype Compression Map

| fine signal | canonical mapping | compression note |
|---|---|---|
| AI device socket design-in | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Requires customer-quality + conversion or repeat order, not price alone. |
| Probe card / test interface recovery | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Needs visible memory/logic customer demand plus earnings bridge. |
| Package inspection AI narrative | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Negative control: customer-quality language without revenue conversion should be capped. |
| Price-only HBM socket local peak | C08 risk overlay only | Cannot become full Stage3/4B without non-price evidence. |

## 7. Case Selection Summary

| case_id | role | symbol | entry_date | entry_price | 180D outcome summary |
|---|---|---:|---:|---:|---|
| R2L13_C08_058470_STAGE2 | structural_success / high_mae_success | 058470 | 2024-02-16 | 209500 | MFE_90 +47.49%, MAE_180 -21.72%; quality route worked but with large post-peak drawdown. |
| R2L13_C08_095340_FP | false_positive_green | 095340 | 2024-03-08 | 95000 | MFE capped near +13.68%, MAE_180 -56.74%; price/customer narrative was not enough. |
| R2L13_C08_131290_STAGE2 | stage2_promote_candidate / 4B_overlay_success | 131290 | 2024-02-16 | 53500 | MFE_90 +64.11%, then drawdown; entry worked, later price-only peak required overlay. |
| R2L13_C08_064290_FP | failed_rerating | 064290 | 2024-03-04 | 40200 | MFE_90 only +1.74%, MAE_90 -30.35%; revision/customer quality failed to confirm. |

## 8. Positive vs Counterexample Balance

| type | count | cases |
|---|---:|---|
| positive_case_count | 2 | 058470, 131290 |
| counterexample_count | 2 | 095340, 064290 |
| 4B_case_count | 2 | 058470, 131290 |
| 4C_case_count | 0 | none; this loop is a Stage2/Green/4B timing residual, not hard-thesis-break 4C |
| calibration_usable_case_count | 4 | all representative rows usable |

The balance is enough to propose a canonical-archetype-specific shadow rule candidate, not a global production change.

## 9. Evidence Source Map

| case_id | trigger_date | evidence family available at trigger date | source label |
|---|---:|---|---|
| R2L13_C08_058470_STAGE2 | 2024-02-15 | AI/custom semiconductor test socket quality route, relative strength already present, early demand optionality | public earnings/IR/newsflow family + stock-web row confirmation |
| R2L13_C08_095340_FP | 2024-03-08 | AI/HBM socket narrative and sharp price momentum, but no confirmed revision bridge yet | public newsflow family + stock-web row confirmation |
| R2L13_C08_131290_STAGE2 | 2024-02-15 | test interface/probe recovery and semiconductor cycle option, followed by stronger price confirmation | public earnings/IR/newsflow family + stock-web row confirmation |
| R2L13_C08_064290_FP | 2024-03-04 | inspection equipment recovery narrative, but customer conversion/earnings support weak | public newsflow family + stock-web row confirmation |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | entry row checked |
|---:|---|---|---|---|
| 058470 | 리노공업 | atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv | atlas/symbol_profiles/058/058470.json | 2024-02-16 c=209500 |
| 095340 | ISC | atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv | atlas/symbol_profiles/095/095340.json | 2024-03-08 c=95000 |
| 131290 | 티에스이 | atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv | atlas/symbol_profiles/131/131290.json | 2024-02-16 c=53500 |
| 064290 | 인텍플러스 | atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv | atlas/symbol_profiles/064/064290.json | 2024-03-04 c=40200 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | 4B evidence | current profile verdict |
|---|---|---|---:|---:|---:|---|---|---|---|
| R2L13_C08_058470_T1 | R2L13_C08_058470_STAGE2 | Stage2-Actionable | 2024-02-15 | 2024-02-16 | 209500 | customer_or_order_quality; relative_strength; early_revision_signal | none yet | none | current_profile_correct |
| R2L13_C08_058470_T2 | R2L13_C08_058470_STAGE2 | Stage3-Yellow | 2024-03-11 | 2024-03-11 | 242500 | customer_or_order_quality; relative_strength | multiple_public_sources; financial_visibility | none | current_profile_correct |
| R2L13_C08_095340_T1 | R2L13_C08_095340_FP | Stage2-Actionable | 2024-03-08 | 2024-03-08 | 95000 | relative_strength; public_event_or_disclosure | none | price_only_local_peak | current_profile_false_positive |
| R2L13_C08_095340_T2 | R2L13_C08_095340_FP | Stage3-Yellow-candidate | 2024-03-28 | 2024-03-28 | 99400 | relative_strength | not_confirmed_revision | price_only_local_peak | current_profile_false_positive |
| R2L13_C08_131290_T1 | R2L13_C08_131290_STAGE2 | Stage2-Actionable | 2024-02-15 | 2024-02-16 | 53500 | public_event_or_disclosure; relative_strength; capacity_or_volume_route | none yet | none | current_profile_correct |
| R2L13_C08_131290_T2 | R2L13_C08_131290_STAGE2 | 4B-overlay | 2024-04-30 | 2024-04-30 | 83200 | none | none | price_only_local_peak; positioning_overheat | current_profile_4B_too_early |
| R2L13_C08_064290_T1 | R2L13_C08_064290_FP | Stage2-Actionable | 2024-03-04 | 2024-03-04 | 40200 | public_event_or_disclosure; relative_strength | none | none | current_profile_false_positive |
| R2L13_C08_064290_T2 | R2L13_C08_064290_FP | 4C-watch | 2024-04-22 | 2024-04-22 | 29900 | none | none | none | current_profile_4C_too_late |

## 12. Trigger-Level OHLC Backtest Tables

Representative trigger rows are deduplicated for aggregate metrics. Label-comparison and 4B/4C overlay rows are retained but not aggregated.

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MFE_1Y_pct | MFE_2Y_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | MAE_1Y_pct | below_entry_90D | peak_date | peak_price | drawdown_after_peak_pct | calibration_usable |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---|---:|---:|---:|---|
| R2L13_C08_058470_T1 | 058470 | 2024-02-16 | 209500 | 31.74 | 47.49 | 47.49 | 47.49 | null | -6.59 | -6.59 | -21.72 | null | true | 2024-05-07 | 309000 | -46.93 | true |
| R2L13_C08_095340_T1 | 095340 | 2024-03-08 | 95000 | 13.68 | 13.68 | 13.68 | null | null | -12.63 | -47.47 | -56.74 | null | true | 2024-03-28 | 108000 | -61.94 | true |
| R2L13_C08_131290_T1 | 131290 | 2024-02-16 | 53500 | 22.62 | 64.11 | 64.11 | null | null | -2.43 | -2.43 | -28.88 | null | true | 2024-05-03 | 87800 | -56.66 | true |
| R2L13_C08_064290_T1 | 064290 | 2024-03-04 | 40200 | 1.74 | 1.74 | 1.74 | null | null | -26.62 | -30.35 | -30.35 | null | true | 2024-03-07 | 40900 | -31.54 | true |

Calculation notes:

```text
058470: entry 209500, max high 309000, min low 164000, MFE=(309000/209500-1)*100, MAE=(164000/209500-1)*100.
095340: entry 95000, max high 108000, min low 41100, MFE=(108000/95000-1)*100, MAE=(41100/95000-1)*100.
131290: entry 53500, max high 87800, min low 38050, MFE=(87800/53500-1)*100, MAE=(38050/53500-1)*100.
064290: entry 40200, max high 40900, min low 28000, MFE=(40900/40200-1)*100, MAE=(28000/40200-1)*100.
```

## 13. Current Calibrated Profile Stress Test

| case_id | current calibrated profile behavior | actual OHLC alignment | verdict |
|---|---|---|---|
| R2L13_C08_058470_STAGE2 | Stage2-Actionable accepted; Green waits for more evidence | Good MFE with manageable early MAE, but high later drawdown | current_profile_correct |
| R2L13_C08_095340_FP | May over-credit price + customer-quality narrative as Yellow | Actual MFE small, MAE very large | current_profile_false_positive |
| R2L13_C08_131290_STAGE2 | Stage2 accepted; 4B price-only treated as overlay | Entry useful; price-only 4B should not become full thesis exit without non-price evidence | current_profile_correct |
| R2L13_C08_064290_FP | May accept rebound as actionable if relative strength is overweighted | Very low MFE, large MAE | current_profile_false_positive |

Stress-test answers:

1. The current calibrated profile is directionally right when customer-quality evidence has durable design-in / conversion hints.
2. It remains too permissive when C08 evidence is only price strength plus broad AI/HBM narrative.
3. Stage2 bonus is appropriate for 058470 and 131290, too generous for 095340 and 064290.
4. Yellow threshold 75 is still vulnerable if relative strength and customer-quality terms are counted without conversion evidence.
5. Green threshold 87 / revision 55 should remain strict; this loop strengthens that axis for C08.
6. Price-only blowoff guard is appropriate and should be strengthened for C08.
7. Full 4B non-price requirement is appropriate; price-only local peaks caught local risk but did not always mark the full cycle top.
8. Hard 4C routing is not the primary axis here, but 064290 suggests earlier thesis-break watch labels help.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | later Yellow/Green proxy | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| R2L13_C08_058470_STAGE2 | 209500 | 242500 | 0.3317 | Yellow is somewhat late but still before much of the move. |
| R2L13_C08_095340_FP | 95000 | 99400 | 0.3385 | Yellow-like confirmation arrived near a local peak and did not protect MAE. |
| R2L13_C08_131290_STAGE2 | 53500 | 83200 | 0.8659 | Late confirmation/overlay near local peak; Stage2 captured most upside. |
| R2L13_C08_064290_FP | 40200 | not_applicable | not_applicable | No confirmed Green trigger; early rebound should have stayed watch-only. |

For C08, Green lateness is not the main residual. The sharper residual is that **unconfirmed socket/customer-quality narratives can be false-positive Yellow candidates even before Green**.

## 15. 4B Local vs Full-window Timing Audit

| case_id | Stage2 price | 4B candidate price | local peak | full window peak | local proximity | full-window proximity | 4B evidence type | timing verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| R2L13_C08_058470_STAGE2 | 209500 | 298000 | 309000 | 309000 | 0.8894 | 0.8894 | price_only; positioning_overheat | price_only_overlay_useful_not_full_4B |
| R2L13_C08_131290_STAGE2 | 53500 | 83200 | 87800 | 87800 | 0.8659 | 0.8659 | price_only; positioning_overheat | price_only_overlay_useful_not_full_4B |
| R2L13_C08_095340_FP | 95000 | 99400 | 108000 | 108000 | 0.3385 | 0.3385 | price_only | weak_4B_not_enough_for_full_timing |
| R2L13_C08_064290_FP | 40200 | 29900 | 40900 | 40900 | negative_after_break | negative_after_break | thesis_break_watch_only | 4C_watch_more_relevant_than_4B |

## 16. 4C Protection Audit

No hard 4C thesis-break case was fully calibrated in this loop. However, 064290 shows a watch-only 4C pattern: after the early rebound failed to extend and the stock returned below the trigger base, C08 names with weak conversion evidence should move to `thesis_break_watch_only` before a hard 4C route.

| case_id | 4C label | protection note |
|---|---|---|
| R2L13_C08_064290_FP | thesis_break_watch_only | useful to prevent false Stage2 from becoming repeated Yellow attempts |
| R2L13_C08_095340_FP | thesis_break_watch_only | socket narrative without earnings bridge should not remain active after -40%+ MAE |

## 17. Sector-Specific Rule Candidate

No broad L2 sector rule is proposed. The cases are concentrated in C08, not the whole semiconductor/electronics sector. C06 memory, C07 HBM equipment, and C09 valuation blowoff may need different rules.

```text
sector_specific_rule_candidate = false
reason = C08-specific residual; insufficient breadth across R2 canonical archetypes
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
rule_candidate = C08_customer_quality_requires_conversion_or_revision_bridge
```

Candidate rule:

```text
For C08, customer_quality_score can support Stage2 only when at least one of the following exists:
1. design-in / qualification / repeat order / conversion evidence,
2. earnings or margin bridge evidence from the same customer route,
3. cross-evidence with relative strength plus non-price disclosure/newsflow.

If evidence is only price strength + AI/HBM socket narrative:
- cap Stage2-Actionable score contribution,
- block Stage3-Yellow promotion,
- treat local peak as price-only 4B overlay, not full 4B.
```

Expected effect:

- Keeps 058470/131290 as usable Stage2 or Stage2-Actionable entries.
- Blocks 095340/064290 from false Yellow/Green promotion.
- Preserves the already applied global rule that price-only blowoff cannot create positive stage labels.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | 4 | 31.76 | -21.51 | 31.76 | -34.42 | 0.50 | 0 | 1 | mixed_alignment |
| P0b_e2r_2_0_baseline_reference | rollback | 4 | 31.76 | -21.51 | 31.76 | -34.42 | 0.75 | 0 | 0 | weaker_guardrails |
| P1_sector_specific_candidate_profile | L2 shadow | 4 | 31.76 | -21.51 | 31.76 | -34.42 | 0.50 | 0 | 1 | no_sector_delta_needed |
| P2_canonical_archetype_candidate_profile | C08 shadow | 4 | 55.80 | -4.51 | 55.80 | -25.30 | 0.00 | 0 | 1 | improved_alignment |
| P3_counterexample_guard_profile | C08 guard | 4 | 55.80 | -4.51 | 55.80 | -25.30 | 0.00 | 1 | 1 | conservative_but_safer |

`P2` selects 058470 and 131290 as representative C08 entries while blocking 095340/064290 from positive aggregation. It does not claim that these two counterexamples had no tradable bounce; it says their evidence quality was insufficient for positive-stage promotion.

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R2L13_C08_058470_T1 | 76 | Stage3-Yellow | 78 | Stage3-Yellow | 47.49 | -6.59 | aligned_positive |
| R2L13_C08_095340_T1 | 77 | Stage3-Yellow | 69 | Stage2-Watch | 13.68 | -47.47 | fixed_false_positive |
| R2L13_C08_131290_T1 | 74 | Stage2-Actionable | 76 | Stage3-Yellow | 64.11 | -2.43 | improved_positive |
| R2L13_C08_064290_T1 | 75 | Stage3-Yellow | 66 | Stage2-Watch | 1.74 | -30.35 | fixed_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | SEMI_TEST_SOCKET_CUSTOMER_QUALITY_HBM_AI_DEVICE_SOCKET_ROUTE | 2 | 2 | 2 | 0 | 4 | 0 | 8 | 4 | 3 | false | true | Needs more hard 4C examples and non-Korean global analog holdout. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - C08_customer_quality_without_conversion_false_positive
  - C08_price_only_local_peak_not_full_4B
  - C08_high_MAE_after_valid_stage2
new_axis_proposed:
  - C08_customer_quality_requires_conversion_or_revision_bridge
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Scheduled R2 / loop 13 state.
- R2 maps to L2_AI_SEMICONDUCTOR_ELECTRONICS.
- Actual stock-web tradable OHLC rows used for entry, peak, MFE and MAE calculations.
- 180D windows are usable for the representative rows.
- Same-entry dedupe applied: one representative row per case for aggregate metrics.
- Positive/counterexample balance achieved.
```

Not validated:

```text
- This file does not inspect stock_agent source code.
- This file does not patch production scoring.
- This file does not create current/live watchlists.
- This file does not claim an investment recommendation.
- Evidence source labels are historical public-event families; this run calibrates the price/evidence logic, not the source ingestion layer.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_customer_quality_requires_conversion_or_revision_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"Blocks C08 price/customer-quality narrative from Yellow unless conversion or revision evidence exists","False-positive rate falls from 0.50 to 0.00 in this sample","R2L13_C08_095340_T1|R2L13_C08_064290_T1",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C08_price_only_local_peak_overlay_only,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"Local peaks in socket/probe names were useful risk overlays but not full 4B without non-price evidence","Protects against premature full 4B and false Green promotion","R2L13_C08_058470_T2|R2L13_C08_131290_T2",4,4,2,medium,canonical_shadow_only,"strengthens existing price-only guard"
shadow_weight,C08_high_MAE_success_exception,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"Valid C08 Stage2 entries may suffer high post-peak MAE; do not retroactively reject Stage2 if early MFE alignment was strong","Keeps 058470 and 131290 as positive examples while separating 4B overlay","R2L13_C08_058470_T1|R2L13_C08_131290_T1",4,4,2,low,canonical_shadow_only,"guarded exception; needs more cases"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R2L13_C08_058470_STAGE2","symbol":"058470","company_name":"리노공업","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALITY_HBM_AI_DEVICE_SOCKET_ROUTE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R2L13_C08_058470_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive_high_mae","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Valid C08 quality route, but later price-only peak needs overlay handling."}
{"row_type":"case","case_id":"R2L13_C08_095340_FP","symbol":"095340","company_name":"ISC","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALITY_HBM_AI_DEVICE_SOCKET_ROUTE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R2L13_C08_095340_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Narrative/price strength lacked confirmed revision bridge."}
{"row_type":"case","case_id":"R2L13_C08_131290_STAGE2","symbol":"131290","company_name":"티에스이","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALITY_HBM_AI_DEVICE_SOCKET_ROUTE","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"R2L13_C08_131290_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive_with_4B_overlay","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Stage2 worked; late peak requires risk overlay."}
{"row_type":"case","case_id":"R2L13_C08_064290_FP","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALITY_HBM_AI_DEVICE_SOCKET_ROUTE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R2L13_C08_064290_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"failed_rerating_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Inspection/test-adjacent rebound had insufficient conversion evidence."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R2L13_C08_058470_T1","case_id":"R2L13_C08_058470_STAGE2","symbol":"058470","company_name":"리노공업","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALITY_HBM_AI_DEVICE_SOCKET_ROUTE","sector":"AI·반도체·전자부품","primary_archetype":"test socket customer quality","loop_objective":"canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-15","entry_date":"2024-02-16","entry_price":209500,"evidence_available_at_that_date":"AI/custom semiconductor test-socket quality and early relative strength, before full confirmed revision","evidence_source":"public_event_family_plus_stock_web_ohlc","stage2_evidence_fields":["customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv","profile_path":"atlas/symbol_profiles/058/058470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.74,"MFE_90D_pct":47.49,"MFE_180D_pct":47.49,"MFE_1Y_pct":47.49,"MFE_2Y_pct":null,"MAE_30D_pct":-6.59,"MAE_90D_pct":-6.59,"MAE_180D_pct":-21.72,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-07","peak_price":309000,"drawdown_after_peak_pct":-46.93,"green_lateness_ratio":0.3317,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_high_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L13_C08_058470_2024-02-16_209500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L13_C08_058470_T2","case_id":"R2L13_C08_058470_STAGE2","symbol":"058470","company_name":"리노공업","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALITY_HBM_AI_DEVICE_SOCKET_ROUTE","sector":"AI·반도체·전자부품","primary_archetype":"test socket customer quality","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B-overlay","trigger_date":"2024-05-07","entry_date":"2024-05-07","entry_price":298000,"evidence_available_at_that_date":"local price blowoff after strong C08 move; non-price 4B evidence not confirmed","evidence_source":"stock_web_ohlc_price_overlay","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv","profile_path":"atlas/symbol_profiles/058/058470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.69,"MFE_90D_pct":3.69,"MFE_180D_pct":3.69,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.54,"MAE_90D_pct":-44.97,"MAE_180D_pct":-44.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-07","peak_price":309000,"drawdown_after_peak_pct":-46.93,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.8894,"four_b_full_window_peak_proximity":0.8894,"four_b_timing_verdict":"price_only_overlay_useful_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L13_C08_058470_2024-05-07_298000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L13_C08_095340_T1","case_id":"R2L13_C08_095340_FP","symbol":"095340","company_name":"ISC","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALITY_HBM_AI_DEVICE_SOCKET_ROUTE","sector":"AI·반도체·전자부품","primary_archetype":"test socket customer quality","loop_objective":"counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":95000,"evidence_available_at_that_date":"AI/HBM socket narrative and relative strength without confirmed revision bridge","evidence_source":"public_event_family_plus_stock_web_ohlc","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.68,"MFE_90D_pct":13.68,"MFE_180D_pct":13.68,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.63,"MAE_90D_pct":-47.47,"MAE_180D_pct":-56.74,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-28","peak_price":108000,"drawdown_after_peak_pct":-61.94,"green_lateness_ratio":0.3385,"four_b_local_peak_proximity":0.3385,"four_b_full_window_peak_proximity":0.3385,"four_b_timing_verdict":"weak_price_only_peak_then_failed_rerating","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L13_C08_095340_2024-03-08_95000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L13_C08_131290_T1","case_id":"R2L13_C08_131290_STAGE2","symbol":"131290","company_name":"티에스이","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALITY_HBM_AI_DEVICE_SOCKET_ROUTE","sector":"AI·반도체·전자부품","primary_archetype":"test socket customer quality","loop_objective":"stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-15","entry_date":"2024-02-16","entry_price":53500,"evidence_available_at_that_date":"probe/test-interface recovery and semiconductor cycle optionality","evidence_source":"public_event_family_plus_stock_web_ohlc","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.62,"MFE_90D_pct":64.11,"MFE_180D_pct":64.11,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.43,"MAE_90D_pct":-2.43,"MAE_180D_pct":-28.88,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-03","peak_price":87800,"drawdown_after_peak_pct":-56.66,"green_lateness_ratio":0.8659,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"stage2_promote_candidate","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L13_C08_131290_2024-02-16_53500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L13_C08_064290_T1","case_id":"R2L13_C08_064290_FP","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALITY_HBM_AI_DEVICE_SOCKET_ROUTE","sector":"AI·반도체·전자부품","primary_archetype":"package inspection / test-adjacent quality route","loop_objective":"counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":40200,"evidence_available_at_that_date":"inspection/test-adjacent rebound and semiconductor cycle narrative without conversion evidence","evidence_source":"public_event_family_plus_stock_web_ohlc","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv","profile_path":"atlas/symbol_profiles/064/064290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.74,"MFE_90D_pct":1.74,"MFE_180D_pct":1.74,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-26.62,"MAE_90D_pct":-30.35,"MAE_180D_pct":-30.35,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":40900,"drawdown_after_peak_pct":-31.54,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L13_C08_064290_2024-03-04_40200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L13_C08_058470_STAGE2","trigger_id":"R2L13_C08_058470_T1","symbol":"058470","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":14,"relative_strength_score":17,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":0,"commercialization_score":10},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":14,"relative_strength_score":17,"customer_quality_score":20,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":0,"commercialization_score":12},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","commercialization_score"],"component_delta_explanation":"C08 quality route has enough conversion-like support to keep Yellow.","MFE_90D_pct":47.49,"MAE_90D_pct":-6.59,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L13_C08_095340_FP","trigger_id":"R2L13_C08_095340_T1","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":6,"relative_strength_score":20,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":13,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":8},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":4,"relative_strength_score":17,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":4},"weighted_score_after":69,"stage_label_after":"Stage2-Watch","changed_components":["customer_quality_score","revision_score","valuation_repricing_score","execution_risk_score","commercialization_score"],"component_delta_explanation":"Customer-quality narrative without conversion/revision bridge is capped.","MFE_90D_pct":13.68,"MAE_90D_pct":-47.47,"score_return_alignment_label":"fixed_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L13_C08_131290_STAGE2","trigger_id":"R2L13_C08_131290_T1","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":10,"relative_strength_score":16,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":8},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":10,"relative_strength_score":17,"customer_quality_score":17,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":9},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["relative_strength_score","customer_quality_score","capacity_or_shipment_score"],"component_delta_explanation":"Stage2 entry had enough test-interface route support, but late 4B overlay is needed.","MFE_90D_pct":64.11,"MAE_90D_pct":-2.43,"score_return_alignment_label":"aligned_positive_with_late_overlay","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L13_C08_064290_FP","trigger_id":"R2L13_C08_064290_T1","symbol":"064290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":17,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":5},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":3,"relative_strength_score":10,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":2},"weighted_score_after":66,"stage_label_after":"Stage2-Watch","changed_components":["relative_strength_score","customer_quality_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Inspection/test-adjacent rebound without conversion support is capped.","MFE_90D_pct":1.74,"MAE_90D_pct":-30.35,"score_return_alignment_label":"fixed_false_positive","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_customer_quality_requires_conversion_or_revision_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"Blocks C08 price/customer-quality narrative from Yellow unless conversion or revision evidence exists","False-positive rate falls from 0.50 to 0.00 in this sample","R2L13_C08_095340_T1|R2L13_C08_064290_T1",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C08_price_only_local_peak_overlay_only,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"Local peaks are risk overlays but not full 4B without non-price evidence","Separates 4B overlay from full thesis exit","R2L13_C08_058470_T2|R2L13_C08_131290_T2",4,4,2,medium,canonical_shadow_only,"strengthens existing price-only guard"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"13","scheduled_round":"R2","scheduled_loop":"13","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["C08_customer_quality_without_conversion_false_positive","C08_price_only_local_peak_not_full_4B","C08_high_MAE_after_valid_stage2"],"diversity_score_summary":"new_symbol +12, counterexample_gap +8, new_trigger_family +16, residual_error +15, wrong_round_penalty 0; estimated +51","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R2L13_C08_GLOBAL_AI_SOCKET_NOTE","symbol":null,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","reason":"Global AI test-socket customer route is narratively relevant but not a stock-web Korean OHLC calibration row in this loop.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R2
completed_loop = 13
next_round = R3
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Price-source files checked:

```text
Songdaiki/stock-web: atlas/manifest.json
Songdaiki/stock-web: atlas/schema.json
Songdaiki/stock-web: atlas/symbol_profiles/058/058470.json
Songdaiki/stock-web: atlas/symbol_profiles/095/095340.json
Songdaiki/stock-web: atlas/symbol_profiles/131/131290.json
Songdaiki/stock-web: atlas/symbol_profiles/064/064290.json
Songdaiki/stock-web: atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv
Songdaiki/stock-web: atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv
Songdaiki/stock-web: atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv
Songdaiki/stock-web: atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv
Songdaiki/stock_agent allowed artifact: data/e2r/calibration/md_registry.jsonl
Songdaiki/stock_agent allowed artifact: data/e2r/calibration/trigger_rows_representative.jsonl
```

The file intentionally avoids stock_agent source-code inspection and avoids production scoring changes. All proposed changes are shadow-only.
