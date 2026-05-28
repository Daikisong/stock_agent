# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| field | value |
|---|---|
| research_session | post_calibrated_sector_archetype_residual_research |
| mode | historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12 |
| output_file | e2r_stock_web_v12_residual_round_R2_loop_16_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md |
| scheduled_round | R2 |
| scheduled_loop | 16 |
| completed_round | R2 |
| completed_loop | 16 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE |
| fine_archetype_id | MEMORY_RECOVERY_SECOND_WAVE_EQUIPMENT_PARTS_UTILIZATION_LAG |
| production_scoring_changed | false |
| shadow_weight_only | true |
| handoff_prompt_embedded | true |
| handoff_prompt_executed_now | false |

This loop adds 4 new independent cases, 1 counterexamples, and 3 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

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

This MD does not re-prove the global axes. It tests whether C10 memory-recovery equipment/parts suppliers need a more precise order-conversion and utilization-followthrough guard.

## 2. Round / Large Sector / Canonical Archetype Scope

| item | value |
|---|---|
| scheduled_round | R2 |
| scheduled_loop | 16 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE |
| round_sector_consistency | pass |
| selected reason | R2 local loops 10-15 covered C06/C07/C08/C09/C10, but C10 was still concentrated in memory majors and first-wave equipment. This loop adds new C10 symbols in equipment/parts/utilization lag. |
| loop_objective | coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test |

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 inventory shows R2 loop 11 already tested C10 with `000660`, `005930`, `036930`, `095610`, and `240810`. This loop avoids those symbols and uses four new C10 names: `319660`, `166090`, `084370`, `074600`.

| duplicate check | result |
|---|---|
| repeated canonical | allowed; C10 is the target archetype |
| repeated symbol + trigger_date + entry_date | none against local C10 loop 11 |
| minimum_new_symbol_count | pass: 4 |
| minimum_counterexample_count | pass: 1 |
| minimum_positive_case_count | pass: 3 |
| new_independent_case_ratio | 4/4 = 1.00 |
| same_archetype_new_trigger_family_count | 2: second-wave order-conversion and late price-only parts blowoff |

## 4. Stock-Web OHLC Input / Price Source Validation

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

Tradable shard columns are `d,o,h,l,c,v,a,mc,s,m`. MFE/MAE are computed from maximum high and minimum low from entry date through the relevant forward trading-day window. The rows below use stock-web tradable rows only.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D available by manifest max_date | corporate action 180D window | calibration_usable |
|---|---:|---:|---:|---|---|
| R2L16_C10_319660_PSK_SECOND_WAVE_CONVERSION | 319660 | 2024-01-19 | yes | clean_180D_window; profile CA candidates are 2022-09-21 and 2022-10-20 only | true |
| R2L16_C10_166090_HANA_PARTS_UTILIZATION | 166090 | 2024-01-19 | yes | clean_180D_window; profile CA candidates are 2018-06-14 and 2018-07-10 only | true |
| R2L16_C10_084370_EUGENE_ALD_HIGH_MAE | 084370 | 2024-01-19 | yes | clean_180D_window; profile CA candidates are 2007-05-17, 2010-01-22, 2012-06-07 only | true |
| R2L16_C10_074600_WONIKQNC_LATE_PRICE_ONLY | 074600 | 2024-06-07 | yes | clean_180D_window; profile CA candidates are 2004-06-25, 2004-07-21, 2017-04-28, 2017-05-24 only | true |

## 6. Canonical Archetype Compression Map

C10 is not simply “memory recovery = buy every semiconductor name.” It has three bridges:

```text
memory price / utilization bottoming
→ equipment order conversion or parts utilization follow-through
→ margin/revision confirmation
```

| fine pattern | canonical mapping | scoring implication |
|---|---|---|
| second-wave equipment order conversion | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | keep Stage2/Yellow; promote only with customer/order/revision confirmation |
| parts utilization lag | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | allow early signal but require utilization follow-through |
| late price-only parts blowoff | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | block positive promotion; route to 4B watch |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_date | entry_date | entry_price | outcome |
|---|---:|---|---|---:|---:|---:|---|
| R2L16_C10_319660_PSK_SECOND_WAVE_CONVERSION | 319660 | 피에스케이 | structural_success | 2024-01-19 | 2024-01-19 | 21,200 | structural_success |
| R2L16_C10_166090_HANA_PARTS_UTILIZATION | 166090 | 하나머티리얼즈 | high_mae_success | 2024-01-19 | 2024-01-19 | 53,000 | high_mae_success |
| R2L16_C10_084370_EUGENE_ALD_HIGH_MAE | 084370 | 유진테크 | high_mae_success | 2024-01-19 | 2024-01-19 | 43,650 | high_mae_success |
| R2L16_C10_074600_WONIKQNC_LATE_PRICE_ONLY | 074600 | 원익QnC | false_positive_green | 2024-06-07 | 2024-06-07 | 40,950 | false_positive_green |

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive structural / order-conversion success | 1 | 319660 |
| high-MAE success | 2 | 166090, 084370 |
| late price-only false positive | 1 | 074600 |
| 4B/4C overlay evidence | 4 | all cases have valuation, overheat, or thesis-watch labels |

## 9. Evidence Source Map

| evidence family | evidence date | source note |
|---|---:|---|
| memory recovery second wave | 2024-01-19 | Historical public research/news proxy; the price rows are verified in stock-web. |
| equipment order conversion | 2024-01~2024-07 | PSK and Eugene Tech show different MFE/MAE paths despite similar memory recovery narrative. |
| parts utilization lag | 2024-01~2024-07 | Hana Materials and Wonik QnC show why parts suppliers need utilization follow-through rather than headline-only Green. |
| late price-only blowoff | 2024-06-07 | Wonik QnC reached its observed peak on the trigger date, then suffered large MAE without fresh order/margin bridge. |

## 10. Price Data Source Map

| symbol | company | tradable shard(s) used | profile |
|---:|---|---|---|
| 319660 | 피에스케이 | `atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv` | `atlas/symbol_profiles/319/319660.json` |
| 166090 | 하나머티리얼즈 | `atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv` | `atlas/symbol_profiles/166/166090.json` |
| 084370 | 유진테크 | `atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv` | `atlas/symbol_profiles/084/084370.json` |
| 074600 | 원익QnC | `atlas/ohlcv_tradable_by_symbol_year/074/074600/2024.csv` | `atlas/symbol_profiles/074/074600.json` |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence | current verdict |
|---|---|---|---|---|---|---|---|
| TRG_R2L16_C10_319660_PSK_STAGE2A_20240119 | R2L16_C10_319660_PSK_SECOND_WAVE_CONVERSION | Stage2-Actionable | relative_strength, capacity_or_volume_route, early_revision_signal, customer_or_order_quality | repeat_order_or_conversion, margin_bridge, financial_visibility | valuation_blowoff, positioning_overheat | none | current_profile_correct |
| TRG_R2L16_C10_166090_HANA_STAGE2A_20240119 | R2L16_C10_166090_HANA_PARTS_UTILIZATION | Stage2-Actionable | capacity_or_volume_route, relative_strength, early_revision_signal | margin_bridge, financial_visibility | positioning_overheat, margin_or_backlog_slowdown | none | current_profile_too_early |
| TRG_R2L16_C10_084370_EUGENE_STAGE2A_20240119 | R2L16_C10_084370_EUGENE_ALD_HIGH_MAE | Stage2-Actionable | relative_strength, capacity_or_volume_route, customer_or_order_quality | repeat_order_or_conversion, margin_bridge | valuation_blowoff, positioning_overheat | none | current_profile_too_early |
| TRG_R2L16_C10_074600_WONIKQNC_PRICEONLY_20240607 | R2L16_C10_074600_WONIKQNC_LATE_PRICE_ONLY | Stage2-Watch | relative_strength | none | price_only_local_peak, positioning_overheat, margin_or_backlog_slowdown | thesis_evidence_broken | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 319660 | 2024-01-19 | 21,200 | 26.18 | -7.88 | 55.42 | -7.88 | 84.43 | -7.88 | 2024-07-11 | 39,100 | -29.41 |
| 166090 | 2024-01-19 | 53,000 | 2.64 | -15.85 | 15.09 | -15.85 | 30.75 | -15.85 | 2024-07-02 | 69,300 | -33.69 |
| 084370 | 2024-01-19 | 43,650 | 7.67 | -26.23 | 37.46 | -26.23 | 37.46 | -26.23 | 2024-05-28 | 60,000 | -47.33 |
| 074600 | 2024-06-07 | 40,950 | 0.12 | -13.68 | 0.12 | -31.99 | 0.12 | -31.99 | 2024-06-07 | 41,000 | -32.07 |

Raw row anchors:

```text
319660: 2024-01-19 c=21200; 2024-02-01 l=19530; 2024-07-11 h=39100; 2024-08-02 l=27600.
166090: 2024-01-19 c=53000; 2024-02-05 l=44600; 2024-04-04 h=61000; 2024-07-02 h=69300; 2024-07-30 l=45950.
084370: 2024-01-19 c=43650; 2024-02-05 l=32200; 2024-05-28 h=60000; 2024-12-02 l=31600.
074600: 2024-06-07 c=40950; 2024-06-07 h=41000; 2024-06-25 l=35350; 2024-08-02 l=27850.
```

## 13. Current Calibrated Profile Stress Test

| case | expected current-profile action | actual MFE/MAE alignment | verdict |
|---|---|---|---|
| 319660 피에스케이 | Stage3-Yellow | 55.42% / -7.88% | current_profile_correct |
| 166090 하나머티리얼즈 | Stage3-Yellow | 15.09% / -15.85% | current_profile_too_early |
| 084370 유진테크 | Stage3-Yellow/weak-Green-risk | 37.46% / -26.23% | current_profile_too_early |
| 074600 원익QnC | Stage3-Yellow/price-momentum-risk | 0.12% / -31.99% | current_profile_false_positive |

Required answers:

```text
1. Current calibrated profile would likely classify 319660 as valid Yellow, 166090/084370 as Yellow or weak-Green candidates, and 074600 as a possible momentum-driven Yellow if relative strength is overweighted.
2. 319660 aligns well; 166090 and 084370 align only if high-MAE risk is tolerated; 074600 is a false positive.
3. Stage2 actionable bonus is useful for early order-conversion/parts follow-through, but too permissive for late price-only parts blowoff.
4. Yellow threshold 75 is acceptable if C10-specific order-conversion guard is present.
5. Green 87 / revision 55 should remain strict; 166090 and 084370 should not Green before utilization/revision confirmation.
6. Price-only blowoff guard is strongly appropriate for 074600.
7. Full 4B non-price requirement remains correct; 074600 is price-only local/full peak, so it should not train positive Stage2/3 weights.
8. Hard 4C routing is not triggered at entry, but thesis-break watch should activate when utilization/margin follow-through fails.
```

## 14. Stage2 / Yellow / Green Comparison

C10 stage ladder after this loop:

```text
Stage2-Actionable: memory recovery headline + relative strength + early equipment/parts route
Stage3-Yellow: Stage2 + order conversion, utilization follow-through, or margin bridge
Stage3-Green: Yellow + confirmed revision/customer/order conversion + low overheat
4B overlay: late price-only spike, valuation/positioning overheat, revision slowdown
4C: explicit utilization/margin thesis break or order collapse
```

Green lateness ratio is `not_applicable` for the representative rows because the loop is a C10 second-wave entry/guard test rather than a late-Green timing optimization. For the 074600 price-only row, a Green label would be a false positive because the trigger occurred at the full-window peak.

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence | local peak proximity | full-window peak proximity | verdict |
|---:|---|---:|---:|---|
| 319660 | valuation/positioning watch only | n/a | n/a | not a 4B entry; keep as positive Stage2/Yellow |
| 166090 | positioning/margin-slowdown watch | n/a | n/a | high-MAE positive; do not Green until utilization confirms |
| 084370 | valuation/positioning watch | n/a | n/a | high-MAE positive; 4B only after non-price slowdown |
| 074600 | price-only local/full peak | 1.00 | 1.00 | price_only_local_4B_too_early_but_not_positive |

## 16. 4C Protection Audit

| symbol | 4C evidence type | label | interpretation |
|---:|---|---|---|
| 319660 | none at entry | thesis_break_watch_only | keep as positive C10 equipment conversion row |
| 166090 | utilization lag watch | thesis_break_watch_only | high-MAE success; needs follow-through gate |
| 084370 | order/revision delay watch | thesis_break_watch_only | high-MAE success; Green requires confirmation |
| 074600 | price-only thesis failure | hard_4c_late_watch | no positive weight; use as C10 parts blowoff guard |

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`

Candidate rule:

```text
In L2/C10, memory recovery headline can open Stage2-Actionable.
For equipment and parts suppliers, Stage3-Yellow requires order conversion or utilization follow-through.
Stage3-Green requires revision/margin confirmation.
Late price-only parts spikes without fresh order/revision evidence are blocked from positive promotion and routed to 4B-watch.
```

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`

Proposed C10 shadow axes:

```text
c10_equipment_order_conversion_bonus = +1
c10_parts_utilization_followthrough_score = +1
c10_high_mae_success_guard = true
c10_late_price_only_blowoff_guard = true
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected cases | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 4 | all | 27.02 | -20.49 | 38.19 | -20.49 | 0.25 | 0 | mixed; 074600 false positive remains |
| P0b e2r_2_0_baseline_reference | rollback | 4 | all, looser Green risk | 27.02 | -20.49 | 38.19 | -20.49 | 0.25 | 0 | too permissive for price-only late spikes |
| P1 sector_specific_candidate_profile | sector shadow | 3 | 319660,166090,084370 | 35.99 | -16.65 | 50.88 | -16.65 | 0.00 | 0 | better explanatory balance |
| P2 canonical_archetype_candidate_profile | C10 shadow | 3 | positive rows only; 074600 blocked | 35.99 | -16.65 | 50.88 | -16.65 | 0.00 | 0 | best candidate profile |
| P3 counterexample_guard_profile | guard | 1 | 319660 only | 55.42 | -7.88 | 84.43 | -7.88 | 0.00 | 2 | safest but may miss high-MAE positives |

## 20. Score-Return Alignment Matrix

| trigger_id | before_score | before_label | after_score | after_label | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| TRG_R2L16_C10_319660_PSK_STAGE2A_20240119 | 81 | Stage3-Yellow | 86 | Stage3-Yellow-high-confidence | 55.42% | -7.88% | strong_positive_alignment |
| TRG_R2L16_C10_166090_HANA_STAGE2A_20240119 | 78 | Stage3-Yellow | 78 | Stage2-Actionable / wait-for-utilization-confirmation | 15.09% | -15.85% | positive_but_high_MAE_success |
| TRG_R2L16_C10_084370_EUGENE_STAGE2A_20240119 | 80 | Stage3-Yellow/weak-Green-risk | 76 | Stage2-Actionable-high-MAE-guard | 37.46% | -26.23% | positive_but_high_MAE_success |
| TRG_R2L16_C10_074600_WONIKQNC_PRICEONLY_20240607 | 76 | Stage3-Yellow/price-momentum-risk | 54 | Stage2-Watch / no-positive-promotion | 0.12% | -31.99% | price_only_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | MEMORY_RECOVERY_SECOND_WAVE_EQUIPMENT_PARTS_UTILIZATION_LAG | 3 | 1 | 1 | 1 | 4 | 0 | 4 | 4 | 3 | true | true | C10 now has memory-major, equipment, and parts/utilization-lag coverage; needs future holdout only |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 2
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: current_profile_too_early, current_profile_false_positive, high_mae_success
new_axis_proposed: c10_equipment_order_conversion_bonus, c10_parts_utilization_followthrough_score, c10_high_mae_success_guard, c10_late_price_only_blowoff_guard
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, stage3_green_revision_min
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_cross_evidence_green_buffer, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema basis
- four symbol profiles for corporate-action and forward-window checks
- 2024 tradable OHLC anchor rows for entry, peak, low, and drawdown
- 30D/90D/180D MFE/MAE from actual stock-web OHLC rows
- current calibrated profile stress test as research proxy only
```

Not validated:

```text
- live 2026 candidate scan
- brokerage or auto-trading
- production scoring code
- stock_agent src/e2r implementation details
- new price route discovery outside Songdaiki/stock-web
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_equipment_order_conversion_bonus,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Order-conversion/parts-utilization evidence separates PSK/Hana/Eugene positives from generic memory recovery headline.","keeps positive cases as Stage2/Yellow without forcing Green",TRG_R2L16_C10_319660_PSK_STAGE2A_20240119|TRG_R2L16_C10_166090_HANA_STAGE2A_20240119|TRG_R2L16_C10_084370_EUGENE_STAGE2A_20240119,4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C10_late_price_only_blowoff_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1 guard,"Late parts/utilization price spike without fresh order or margin bridge produced near-zero MFE and high MAE.","blocks WonikQnC 2024-06-07 from positive promotion",TRG_R2L16_C10_074600_WONIKQNC_PRICEONLY_20240607,4,4,1,medium,canonical_shadow_only,"strengthens price-only blowoff guard inside C10 only"
shadow_weight,C10_parts_utilization_followthrough_score,sector_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Parts suppliers rerate after utilization evidence rather than immediately at memory-price bottom.","reduces premature Green and keeps high-MAE successes as Stage2/Yellow",TRG_R2L16_C10_166090_HANA_STAGE2A_20240119|TRG_R2L16_C10_074600_WONIKQNC_PRICEONLY_20240607,4,4,1,low_to_medium,sector_shadow_only,"not global; R2/C10 only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R2L16_C10_319660_PSK_SECOND_WAVE_CONVERSION", "symbol": "319660", "company_name": "피에스케이", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_SECOND_WAVE_EQUIPMENT_PARTS_UTILIZATION_LAG", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_R2L16_C10_319660_PSK_STAGE2A_20240119", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "strong_positive_alignment", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "2024년 초 메모리 업황 회복 기대가 단순 감산/가격 바닥을 넘어 전공정 장비 주문 전환 기대로 확산된 구간. 피에스케이는 1월 말 이후 완만한 상승 뒤 2~7월까지 추가 rerating이 확인된다."}
{"row_type": "case", "case_id": "R2L16_C10_166090_HANA_PARTS_UTILIZATION", "symbol": "166090", "company_name": "하나머티리얼즈", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_SECOND_WAVE_EQUIPMENT_PARTS_UTILIZATION_LAG", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_R2L16_C10_166090_HANA_STAGE2A_20240119", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_but_high_MAE_success", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "소모성 부품/실리콘 부품은 메모리 가격 반등보다 utilization 회복이 늦게 붙는 구조다. 1월 Stage2는 빠른 Green이 아니라 parts-utilization follow-through를 기다리는 Yellow 후보로 보는 것이 맞았다."}
{"row_type": "case", "case_id": "R2L16_C10_084370_EUGENE_ALD_HIGH_MAE", "symbol": "084370", "company_name": "유진테크", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_SECOND_WAVE_EQUIPMENT_PARTS_UTILIZATION_LAG", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_R2L16_C10_084370_EUGENE_STAGE2A_20240119", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_but_high_MAE_success", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "증착/ALD 장비 기대는 메모리 회복 second wave에서 먼저 움직였지만 2월 초 큰 MAE를 동반했다. 결과적으로 90D/180D MFE는 양호했으나, C10 Green은 주문 전환 확인 전까지 유보해야 한다."}
{"row_type": "case", "case_id": "R2L16_C10_074600_WONIKQNC_LATE_PRICE_ONLY", "symbol": "074600", "company_name": "원익QnC", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_SECOND_WAVE_EQUIPMENT_PARTS_UTILIZATION_LAG", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_R2L16_C10_074600_WONIKQNC_PRICEONLY_20240607", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "price_only_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "석영/부품 utilization 회복 narrative가 이미 가격에 반영된 뒤 2024-06-07 단발 급등으로 들어간 케이스다. 주문 전환·마진 bridge 없이 가격만 따라가면 90D/180D MFE는 거의 없고 MAE가 커졌다."}
{"row_type": "trigger", "trigger_id": "TRG_R2L16_C10_319660_PSK_STAGE2A_20240119", "case_id": "R2L16_C10_319660_PSK_SECOND_WAVE_CONVERSION", "symbol": "319660", "company_name": "피에스케이", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_SECOND_WAVE_EQUIPMENT_PARTS_UTILIZATION_LAG", "sector": "AI/semiconductor/electronics", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-19", "evidence_available_at_that_date": "2024년 초 메모리 업황 회복 기대가 단순 감산/가격 바닥을 넘어 전공정 장비 주문 전환 기대로 확산된 구간. 피에스케이는 1월 말 이후 완만한 상승 뒤 2~7월까지 추가 rerating이 확인된다.", "evidence_source": "historical public disclosure/news/research proxy; OHLC verified in Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route", "early_revision_signal", "customer_or_order_quality"], "stage3_evidence_fields": ["repeat_order_or_conversion", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv", "profile_path": "atlas/symbol_profiles/319/319660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-19", "entry_price": 21200, "MFE_30D_pct": 26.18, "MFE_90D_pct": 55.42, "MFE_180D_pct": 84.43, "MFE_1Y_pct": 84.43, "MFE_2Y_pct": null, "MAE_30D_pct": -7.88, "MAE_90D_pct": -7.88, "MAE_180D_pct": -7.88, "MAE_1Y_pct": -29.95, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 39100, "drawdown_after_peak_pct": -29.41, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile CA candidates are 2022-09-21 and 2022-10-20 only", "same_entry_group_id": "R2L16_C10_319660_PSK_SECOND_WAVE_CONVERSION|2024-01-19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R2L16_C10_166090_HANA_STAGE2A_20240119", "case_id": "R2L16_C10_166090_HANA_PARTS_UTILIZATION", "symbol": "166090", "company_name": "하나머티리얼즈", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_SECOND_WAVE_EQUIPMENT_PARTS_UTILIZATION_LAG", "sector": "AI/semiconductor/electronics", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-19", "evidence_available_at_that_date": "소모성 부품/실리콘 부품은 메모리 가격 반등보다 utilization 회복이 늦게 붙는 구조다. 1월 Stage2는 빠른 Green이 아니라 parts-utilization follow-through를 기다리는 Yellow 후보로 보는 것이 맞았다.", "evidence_source": "historical public disclosure/news/research proxy; OHLC verified in Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["capacity_or_volume_route", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility"], "stage4b_evidence_fields": ["positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv", "profile_path": "atlas/symbol_profiles/166/166090.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-19", "entry_price": 53000, "MFE_30D_pct": 2.64, "MFE_90D_pct": 15.09, "MFE_180D_pct": 30.75, "MFE_1Y_pct": 30.75, "MFE_2Y_pct": null, "MAE_30D_pct": -15.85, "MAE_90D_pct": -15.85, "MAE_180D_pct": -15.85, "MAE_1Y_pct": -33.69, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-02", "peak_price": 69300, "drawdown_after_peak_pct": -33.69, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": ["positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile CA candidates are 2018-06-14 and 2018-07-10 only", "same_entry_group_id": "R2L16_C10_166090_HANA_PARTS_UTILIZATION|2024-01-19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R2L16_C10_084370_EUGENE_STAGE2A_20240119", "case_id": "R2L16_C10_084370_EUGENE_ALD_HIGH_MAE", "symbol": "084370", "company_name": "유진테크", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_SECOND_WAVE_EQUIPMENT_PARTS_UTILIZATION_LAG", "sector": "AI/semiconductor/electronics", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-19", "evidence_available_at_that_date": "증착/ALD 장비 기대는 메모리 회복 second wave에서 먼저 움직였지만 2월 초 큰 MAE를 동반했다. 결과적으로 90D/180D MFE는 양호했으나, C10 Green은 주문 전환 확인 전까지 유보해야 한다.", "evidence_source": "historical public disclosure/news/research proxy; OHLC verified in Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route", "customer_or_order_quality"], "stage3_evidence_fields": ["repeat_order_or_conversion", "margin_bridge"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv", "profile_path": "atlas/symbol_profiles/084/084370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-19", "entry_price": 43650, "MFE_30D_pct": 7.67, "MFE_90D_pct": 37.46, "MFE_180D_pct": 37.46, "MFE_1Y_pct": 37.46, "MFE_2Y_pct": null, "MAE_30D_pct": -26.23, "MAE_90D_pct": -26.23, "MAE_180D_pct": -26.23, "MAE_1Y_pct": -27.61, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-28", "peak_price": 60000, "drawdown_after_peak_pct": -47.33, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile CA candidates are 2007-05-17, 2010-01-22, 2012-06-07 only", "same_entry_group_id": "R2L16_C10_084370_EUGENE_ALD_HIGH_MAE|2024-01-19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R2L16_C10_074600_WONIKQNC_PRICEONLY_20240607", "case_id": "R2L16_C10_074600_WONIKQNC_LATE_PRICE_ONLY", "symbol": "074600", "company_name": "원익QnC", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_SECOND_WAVE_EQUIPMENT_PARTS_UTILIZATION_LAG", "sector": "AI/semiconductor/electronics", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Watch", "trigger_date": "2024-06-07", "evidence_available_at_that_date": "석영/부품 utilization 회복 narrative가 이미 가격에 반영된 뒤 2024-06-07 단발 급등으로 들어간 케이스다. 주문 전환·마진 bridge 없이 가격만 따라가면 90D/180D MFE는 거의 없고 MAE가 커졌다.", "evidence_source": "historical public disclosure/news/research proxy; OHLC verified in Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/074/074600/2024.csv", "profile_path": "atlas/symbol_profiles/074/074600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-07", "entry_price": 40950, "MFE_30D_pct": 0.12, "MFE_90D_pct": 0.12, "MFE_180D_pct": 0.12, "MFE_1Y_pct": 0.12, "MFE_2Y_pct": null, "MAE_30D_pct": -13.68, "MAE_90D_pct": -31.99, "MAE_180D_pct": -31.99, "MAE_1Y_pct": -31.99, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-07", "peak_price": 41000, "drawdown_after_peak_pct": -32.07, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early_but_not_positive", "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_late_watch", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile CA candidates are 2004-06-25, 2004-07-21, 2017-04-28, 2017-05-24 only", "same_entry_group_id": "R2L16_C10_074600_WONIKQNC_LATE_PRICE_ONLY|2024-06-07", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow", "case_id": "R2L16_C10_319660_PSK_SECOND_WAVE_CONVERSION", "trigger_id": "TRG_R2L16_C10_319660_PSK_STAGE2A_20240119", "symbol": "319660", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 7, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 6, "asp_or_spread_score": 5, "parts_utilization_score": 4}, "weighted_score_before": 81, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 7, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 6, "asp_or_spread_score": 5, "parts_utilization_score": 4, "capex_order_conversion_guard": 2, "late_price_only_blowoff_guard": 0, "parts_utilization_followthrough_score": 1}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow-high-confidence", "changed_components": ["capex_order_conversion_guard", "late_price_only_blowoff_guard", "parts_utilization_followthrough_score"], "component_delta_explanation": "C10 shadow separates memory-recovery headline from equipment/parts utilization follow-through. Early entries can remain Stage2/Yellow, but late price-only spikes are blocked from positive promotion.", "MFE_90D_pct": 55.42, "MAE_90D_pct": -7.88, "score_return_alignment_label": "strong_positive_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow", "case_id": "R2L16_C10_166090_HANA_PARTS_UTILIZATION", "trigger_id": "TRG_R2L16_C10_166090_HANA_STAGE2A_20240119", "symbol": "166090", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 5, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 5, "asp_or_spread_score": 4, "parts_utilization_score": 5}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 5, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 5, "asp_or_spread_score": 4, "parts_utilization_score": 5, "capex_order_conversion_guard": 1, "late_price_only_blowoff_guard": 0, "parts_utilization_followthrough_score": 2}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable / wait-for-utilization-confirmation", "changed_components": ["capex_order_conversion_guard", "late_price_only_blowoff_guard", "parts_utilization_followthrough_score"], "component_delta_explanation": "C10 shadow separates memory-recovery headline from equipment/parts utilization follow-through. Early entries can remain Stage2/Yellow, but late price-only spikes are blocked from positive promotion.", "MFE_90D_pct": 15.09, "MAE_90D_pct": -15.85, "score_return_alignment_label": "positive_but_high_MAE_success", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow", "case_id": "R2L16_C10_084370_EUGENE_ALD_HIGH_MAE", "trigger_id": "TRG_R2L16_C10_084370_EUGENE_STAGE2A_20240119", "symbol": "084370", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 6, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 5, "asp_or_spread_score": 4, "parts_utilization_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow/weak-Green-risk", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 6, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 5, "asp_or_spread_score": 4, "parts_utilization_score": 2, "capex_order_conversion_guard": 1, "late_price_only_blowoff_guard": 0, "parts_utilization_followthrough_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable-high-MAE-guard", "changed_components": ["capex_order_conversion_guard", "late_price_only_blowoff_guard", "parts_utilization_followthrough_score"], "component_delta_explanation": "C10 shadow separates memory-recovery headline from equipment/parts utilization follow-through. Early entries can remain Stage2/Yellow, but late price-only spikes are blocked from positive promotion.", "MFE_90D_pct": 37.46, "MAE_90D_pct": -26.23, "score_return_alignment_label": "positive_but_high_MAE_success", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C10_shadow", "case_id": "R2L16_C10_074600_WONIKQNC_LATE_PRICE_ONLY", "trigger_id": "TRG_R2L16_C10_074600_WONIKQNC_PRICEONLY_20240607", "symbol": "074600", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 3, "asp_or_spread_score": 3, "parts_utilization_score": 3}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow/price-momentum-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 3, "asp_or_spread_score": 3, "parts_utilization_score": 3, "capex_order_conversion_guard": -3, "late_price_only_blowoff_guard": -4, "parts_utilization_followthrough_score": -2}, "weighted_score_after": 54, "stage_label_after": "Stage2-Watch / no-positive-promotion", "changed_components": ["capex_order_conversion_guard", "late_price_only_blowoff_guard", "parts_utilization_followthrough_score"], "component_delta_explanation": "C10 shadow separates memory-recovery headline from equipment/parts utilization follow-through. Early entries can remain Stage2/Yellow, but late price-only spikes are blocked from positive promotion.", "MFE_90D_pct": 0.12, "MAE_90D_pct": -31.99, "score_return_alignment_label": "price_only_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 2, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["current_profile_too_early", "current_profile_false_positive", "high_mae_success"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_equipment_order_conversion_bonus,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Order-conversion/parts-utilization evidence separates PSK/Hana/Eugene positives from generic memory recovery headline.","keeps positive cases as Stage2/Yellow without forcing Green",TRG_R2L16_C10_319660_PSK_STAGE2A_20240119|TRG_R2L16_C10_166090_HANA_STAGE2A_20240119|TRG_R2L16_C10_084370_EUGENE_STAGE2A_20240119,4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C10_late_price_only_blowoff_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1 guard,"Late parts/utilization price spike without fresh order or margin bridge produced near-zero MFE and high MAE.","blocks WonikQnC 2024-06-07 from positive promotion",TRG_R2L16_C10_074600_WONIKQNC_PRICEONLY_20240607,4,4,1,medium,canonical_shadow_only,"strengthens price-only blowoff guard inside C10 only"
shadow_weight,C10_parts_utilization_followthrough_score,sector_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Parts suppliers rerate after utilization evidence rather than immediately at memory-price bottom.","reduces premature Green and keeps high-MAE successes as Stage2/Yellow",TRG_R2L16_C10_166090_HANA_STAGE2A_20240119|TRG_R2L16_C10_074600_WONIKQNC_PRICEONLY_20240607,4,4,1,low_to_medium,sector_shadow_only,"not global; R2/C10 only"
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
completed_round = R2
completed_loop = 16
next_round = R3
next_loop = 16
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock_agent_code_accessed: false
stock_agent_patch_written: false
stock_agent_live_scan: false
stock_web_price_atlas_accessed: true
stock_web_manifest_max_date: 2026-02-20
stock_web_profile_files:
- atlas/symbol_profiles/319/319660.json
- atlas/symbol_profiles/166/166090.json
- atlas/symbol_profiles/084/084370.json
- atlas/symbol_profiles/074/074600.json
stock_web_tradable_shards:
- atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/074/074600/2024.csv
round_schedule_status: valid
round_sector_consistency: pass
```

