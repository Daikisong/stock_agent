# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
- research_session: post_calibrated_sector_archetype_residual_research
- round: R4
- loop: 18
- output_file: `e2r_stock_web_v12_residual_round_R4_loop_18_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md`
- large_sector_id: `L4_MATERIALS_SPREAD_RESOURCE`
- canonical_archetype_id: `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`
- fine_archetype_id: `SPREAD_CONFIRMED_SPECIALTY_CHEMICAL_MARGIN_BRIDGE`
- loop_objective: `coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test`
- stock_agent_code_access_allowed: false
- stock_agent_code_patch_allowed: false
- production_scoring_changed: false
- shadow_weight_only: true
- current_stock_discovery_allowed: false
- investment_recommendation_language: none

## 1. Current Calibrated Profile Assumption

Current proxy is `e2r_2_1_stock_web_calibrated`. This loop does not retest the already-applied global lessons as a generic claim. It stress-tests their residual behavior inside C17: the same commodity price rise can be a real EPS/margin bridge in one case and a false reopening beta in another.

Applied axes kept as baseline: `stage2_actionable_evidence_bonus=+2.0`, `stage3_yellow_total_min=75`, `stage3_green_total_min=87`, `stage3_green_revision_min=55`, `stage3_cross_evidence_green_buffer=+1.5`, `price_only_blowoff_blocks_positive_stage=true`, `full_4b_requires_non_price_evidence=true`, `hard_4c_thesis_break_routes_to_4c=true`.

## 2. Round / Large Sector / Canonical Archetype Scope

Scope is R4 → L4, focused on C17. C17 differs from C15/C16 because the signal is not just commodity price or resource scarcity; the signal is whether the spread mechanically closes into company margin, then into revision. The same oil/naphtha/reopening headline can therefore be either a fuse or a decoy.

Canonical compression:
- `SPREAD_CONFIRMED_SPECIALTY_CHEMICAL_MARGIN_BRIDGE` → `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`
- `NBR_LATEX_OR_SPANDEX_SUPERCYCLE` → `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`
- `CHINA_REOPENING_PETROCHEM_BETA_FALSE_POSITIVE` → `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`

## 3. Previous Coverage / Duplicate Avoidance Check

The allowed `stock_agent` ingest summary shows broad prior coverage across R1–R13 and loops 1–9, with 1,376 aggregate representative trigger rows already validated, so this loop deliberately avoids R1/R2 HBM, defense, grid, and the immediately preceding R5/C20 K-beauty work. No matching C17 rows for the selected symbol/trigger families were found through the available GitHub search path in this run. The selected cases are same-canonical but new symbols/new trigger families for this v12 residual batch. Existing ingest rejection reasons also show that invalid price source/basis rows were a major prior failure mode, so this MD anchors all price rows to stock-web tradable_raw fields only. Source: fileciteturn441file0

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-web manifest fields used here: source `FinanceData/marcap`, price adjustment `raw_unadjusted_marcap`, min_date `1995-05-02`, max_date `2026-02-20`, tradable rows `14354401`, raw rows `15214118`, symbols `5414`, active-like `2868`, inactive/delisted-like `2546`, markets `KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI`, calibration root `atlas/ohlcv_tradable_by_symbol_year`, raw root `atlas/ohlcv_raw_by_symbol_year`. Source: fileciteturn442file0

All quantitative rows use `price_basis=tradable_raw` and `price_adjustment_status=raw_unadjusted_marcap`. Corporate-action candidate windows are blocked unless the entry is after the candidate date and the 180D window is clean.

## 5. Historical Eligibility Gate

All representative triggers have a past trigger date, stock-web tradable entry row, at least 180 trading days of forward stock-web data, high/low/close/volume fields, 30D/90D/180D MFE/MAE, and no 180D corporate-action contamination. Lotte Chemical is treated specially: its profile has a 2023-02-13 corporate-action candidate, so the 2023-02-14 entry avoids contaminating the forward 180D window. Source profile: fileciteturn446file0turn447file0

## 6. Canonical Archetype Compression Map
| fine | canonical | reason |
| --- | --- | --- |
| NBR_LATEX_MARGIN_SUPERCYCLE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | spread → OP revision → rerating |
| SPANDEX_SUPERCYCLE_MARGIN_BRIDGE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | specialty chemical spread visibly closed into earnings |
| PETROCHEM_REOPENING_BETA_FALSE_POSITIVE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | macro/reopening beta without margin bridge should remain Stage2-watch |

## 7. Case Selection Summary
| case_id | symbol | company_name | case_role | positive_or_counterexample | trigger_id | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R4L18-C17-HYOTNC-2020-SPANDEX | 298020 | 효성티앤씨 | structural_success | positive | R4L18-C17-HYOTNC-S2A-2020-11-02 | 2020-11-02 | 155500 | 269.13 | -5.47 | 519.29 | -5.47 | current_profile_correct |
| R4L18-C17-KKPC-2020-NBLATEX | 011780 | 금호석유화학 | structural_success | positive | R4L18-C17-KKPC-S2A-2020-08-03 | 2020-08-03 | 82100 | 90.62 | -0.97 | 263.58 | -0.97 | current_profile_correct |
| R4L18-C17-LOTTECHEM-2023-REOPEN-FAILED | 011170 | 롯데케미칼 | failed_rerating | counterexample | R4L18-C17-LOTTECHEM-S2-2023-02-14 | 2023-02-14 | 175800 | 10.52 | -6.09 | 10.52 | -28.16 | current_profile_false_positive |
| R4L18-C17-KPIC-2023-NCC-FAILED | 006650 | 대한유화 | failed_rerating | counterexample | R4L18-C17-KPIC-S2-2023-02-14 | 2023-02-14 | 162200 | 19.48 | -17.82 | 19.48 | -33.42 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

Positive cases: 2 representative structural successes plus 1 4B overlay path on a positive case. Counterexamples: 2 failed rerating cases. This satisfies the minimum positive/counterexample balance and keeps the loop useful as a calibration candidate, not just narrative rematerialization.

The mechanical distinction is simple: in true spread cycles, the spread is not the thesis; the spread is the gear that turns the earnings wheel. In failed reopening beta, the price headline is only wind against the sail—without margin and revision, the boat does not move far.

## 9. Evidence Source Map
| case_id | evidence_family | stage2 | stage3 |
| --- | --- | --- | --- |
| R4L18-C17-HYOTNC-2020-SPANDEX | 3Q20/2020H2 spandex demand, utilization, margin bridge | public_event_or_disclosure, relative_strength, early_revision_signal | confirmed_revision, margin_bridge |
| R4L18-C17-KKPC-2020-NBLATEX | NB latex / synthetic rubber margin supercycle | customer/order quality, relative strength | confirmed_revision, margin_bridge |
| R4L18-C17-LOTTECHEM-2023-REOPEN-FAILED | China reopening / commodity beta without sufficient spread-to-OP closure | policy/regulatory optionality | none |
| R4L18-C17-KPIC-2023-NCC-FAILED | NCC spread recovery expectation without revision closure | policy/regulatory optionality | none |

## 10. Price Data Source Map
| symbol | company | profile | profile_note | source |
| --- | --- | --- | --- | --- |
| 298020 | 효성티앤씨 | atlas/symbol_profiles/298/298020.json | no corporate-action candidates; clean profile | fileciteturn443file0 |
| 011780 | 금호석유화학 | atlas/symbol_profiles/011/011780.json | only 2001 candidate; clean 2020/2021 windows | fileciteturn444file0turn445file0 |
| 011170 | 롯데케미칼 | atlas/symbol_profiles/011/011170.json | 2023-02-13 candidate; entry shifted to 2023-02-14 clean window | fileciteturn446file0turn447file0 |
| 006650 | 대한유화 | atlas/symbol_profiles/006/006650.json | 2010 candidate only; clean 2023 window | fileciteturn448file0 |

## 11. Case-by-Case Trigger Grid
| trigger_id | trigger_type | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | current_profile_verdict | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R4L18-C17-HYOTNC-S2A-2020-11-02 | Stage2-Actionable | 2020-11-02 | 155500 | 41.48 | 269.13 | 519.29 | -5.47 | -5.47 | -5.47 | 2021-07-16 | 963000 | current_profile_correct | representative |
| R4L18-C17-HYOTNC-4B-2021-07-16 | Stage4B-Overlay | 2021-07-16 | 881000 | 9.31 | 9.31 | 9.31 | -9.31 | -28.6 | -49.1 | 2021-07-16 | 963000 | current_profile_correct | 4B_overlay_only |
| R4L18-C17-KKPC-S2A-2020-08-03 | Stage2-Actionable | 2020-08-03 | 82100 | 40.07 | 90.62 | 263.58 | -0.97 | -0.97 | -0.97 | 2021-05-06 | 298500 | current_profile_correct | representative |
| R4L18-C17-LOTTECHEM-S2-2023-02-14 | Stage2 | 2023-02-14 | 175800 | 10.52 | 10.52 | 10.52 | -2.16 | -6.09 | -28.16 | 2023-02-22 | 194300 | current_profile_false_positive | representative |
| R4L18-C17-KPIC-S2-2023-02-14 | Stage2 | 2023-02-14 | 162200 | 19.48 | 19.48 | 19.48 | -5.49 | -17.82 | -33.42 | 2023-02-23 | 193800 | current_profile_false_positive | representative |

## 12. Trigger-Level OHLC Backtest Tables

Representative price rows and future-window anchors:
- 효성티앤씨 entry 2020-11-02 close 155,500 and early 30D path are directly visible in the 2020 stock-web shard. Source: fileciteturn449file0. The 2021 continuation contains the 2021-07-16 963,000 high used as 180D/full-window peak. Source: fileciteturn450file0.
- 금호석유화학 entry 2020-08-03 close 82,100 and 2020H2 run-up are visible in the 2020 shard. Source: fileciteturn451file0. The 2021 shard contains the 2021-05-06 298,500 high. Source: fileciteturn452file0.
- 롯데케미칼 2023-02-14 clean entry close 175,800 and first-window high 194,300 are visible in the 2023 shard. Source: fileciteturn453file0. The same shard later shows the 180D drawdown path toward 126,300. Source: fileciteturn454file0.
- 대한유화 2023-02-14 entry close 162,200, first-window high 193,800, and later drawdown toward 108,000 are visible in the 2023 shard. Sources: fileciteturn455file0turn456file0.

## 13. Current Calibrated Profile Stress Test

1. Current profile correctly captures the two true spread/margin bridge successes if revision and margin bridge are allowed to dominate. 2. It remains vulnerable to residual false positives when reopening or commodity beta is scored too near Stage2-Actionable without requiring spread-to-OP closure. 3. Stage2 bonus was not too high for Hyosung TNC/Kumho Petrochemical, but it was too permissive for Lotte Chemical/Daehan Synthetic Fiber-like NCC beta. 4. Yellow threshold 75 is acceptable, but C17 should require specific margin bridge components before Green. 5. Green 87/revision 55 is directionally right; this loop strengthens it inside C17. 6. Price-only blowoff guard is appropriate; HYO 2021-07-16 should be 4B overlay only unless valuation/revision fatigue is separately present. 7. Full 4B non-price requirement is kept. 8. Hard 4C routing should occur when margin bridge fails and MAE expands, rather than waiting for price collapse only.

## 14. Stage2 / Yellow / Green Comparison

C17 Green lateness is tolerable in the two positive cases because the cycles were long enough after the first Stage2-Actionable. Hyosung TNC’s proxy Green lateness ratio is 0.49: not early, but still before the full 180D peak. Kumho Petrochemical’s proxy is 0.36. The negative cases have no confirmed Green trigger; assigning Green from reopening beta alone would be outcome-inconsistent.

## 15. 4B Local vs Full-window Timing Audit

Hyosung TNC 2021-07-16 has local and full-window peak proximity near 1.0 from the Stage2 entry because the peak row itself is the observed 963,000 high. This validates the split between price-only local peak and full 4B: the local/full price condition was excellent, but the row should remain overlay-only unless non-price valuation/revision fatigue is documented. That strengthens the existing `full_4b_requires_non_price_evidence` axis inside C17 rather than proposing a global change.

## 16. 4C Protection Audit

The two 2023 failed rerating cases show that C17 thesis break can be visible before a dramatic one-day collapse: the absence of margin bridge plus widening MAE is enough to route to 4C-watch. Lotte Chemical and Daehan Petrochemical-like NCC beta should not wait for price-only capitulation; thesis evidence breaks when spread improvement fails to pass into OP/revision.

## 17. Sector-Specific Rule Candidate
No L4-wide production rule is proposed. The evidence is strong inside C17 but not yet broad enough across C15/C16/C17 to promote a full L4 sector rule. `sector_specific_rule_candidate=false`.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate=true`.

Candidate C17 shadow rules:
1. `c17_spread_to_op_bridge_gate`: C17 positive promotion requires margin_bridge_score and revision_score evidence; commodity price/spread narrative alone remains Stage2-watch.
2. `c17_reopening_beta_no_green_guard`: China/reopening beta without spread-to-OP closure cannot become Stage3-Green.
3. `c17_price_only_peak_overlay_guard`: local/full-window price proximity can create 4B overlay but cannot become full 4B unless valuation/revision fatigue or other non-price risk is present.

## 19. Before / After Backtest Comparison
| profile_id | profile_scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | baseline_current_proxy | 4 | 97.44 | -7.09 | 203.14 | -16.75 | 2/4 | mixed; C17 false positives remain when spread narrative is not tied to OP revision |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 97.44 | -7.09 | 203.14 | -16.75 | 2/4+ | worse; commodity beta over-promoted |
| P1_sector_specific_candidate_profile | L4 sector_specific | 4 | 97.44 | -7.09 | 203.14 | -16.75 | 0/2 promoted positives; 2 watch-only | better but should remain canonical-specific until more L4 archetypes are tested |
| P2_canonical_archetype_candidate_profile | C17 canonical_archetype_specific | 4 | 269.88 | -3.22 | 391.44 | -3.22 | 0/2 promoted positives | best alignment in this loop |
| P3_counterexample_guard_profile | counterexample guard | 2 | 15.0 | -11.96 | 15.0 | -30.79 | 0 promoted | guard useful as canonical negative rule |

## 20. Score-Return Alignment Matrix
| bucket | cases | score_effect | return_alignment |
| --- | --- | --- | --- |
| true margin bridge | 효성티앤씨, 금호석유화학 | promote to Stage3 only when margin/revision close | high MFE, low early MAE |
| reopening beta only | 롯데케미칼, 대한유화 | Stage2-watch / no Green | small MFE, large MAE |
| price-only peak | 효성티앤씨 4B overlay | overlay only | good local/full timing but needs non-price confirmation |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | SPREAD_CONFIRMED_SPECIALTY_CHEMICAL_MARGIN_BRIDGE | 2 | 2 | 1 | 2 | 4 | 0 | 5 | 4 | 2 | False | True | C17 now has positive + false-positive + 4B overlay + 4C-watch path; still needs holdout on chlor-alkali, PVC, and refinery spread analogues |

## 22. Residual Contribution Summary

new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: reopening_beta_false_positive, spread_narrative_without_margin_bridge, price_only_4B_requires_non_price_confirmation
new_axis_proposed: c17_spread_to_op_bridge_gate, c17_reopening_beta_no_green_guard, c17_price_only_peak_overlay_guard
existing_axis_strengthened: stage3_green_revision_min within C17; full_4b_requires_non_price_evidence within C17; hard_4c_thesis_break_routes_to_4c within C17
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false

## 23. Validation Scope / Non-Validation Scope

Validated: stock-web manifest, profile paths, tradable raw OHLC rows, 30D/90D/180D MFE/MAE, corporate-action window status, same-entry dedupe roles, current calibrated profile stress test, positive/counterexample balance.

Not validated: live candidates, current 2026 watchlist, broker execution, production scoring code, stock_agent src/e2r internals, new price routes, official listing status beyond stock-web profile inference, and full 1Y/2Y exhaustive recomputation beyond the C17 calibration-use 180D window.

## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c17_spread_to_op_bridge_gate,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Promote C17 only when spread improvement is visible in margin bridge/revision, not just commodity beta or reopening narrative.","HYO/Kumho positives preserved; Lotte/KPIC false positives blocked.","R4L18-C17-HYOTNC-S2A-2020-11-02|R4L18-C17-KKPC-S2A-2020-08-03|R4L18-C17-LOTTECHEM-S2-2023-02-14|R4L18-C17-KPIC-S2-2023-02-14",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c17_reopening_beta_no_green_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"China/reopening beta cannot become Stage3-Green unless spread-to-OP revision closes.","Two 2023 false positives become Stage2-watch rather than Green.","R4L18-C17-LOTTECHEM-S2-2023-02-14|R4L18-C17-KPIC-S2-2023-02-14",2,2,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows
### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "R4L18-C17-HYOTNC-2020-SPANDEX", "symbol": "298020", "company_name": "효성티앤씨", "round": "R4", "loop": "18", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_CONFIRMED_SPECIALTY_CHEMICAL_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R4L18-C17-HYOTNC-S2A-2020-11-02", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_high_mfe", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "representative aggregate trigger; no production scoring change"}
{"row_type": "case", "case_id": "R4L18-C17-KKPC-2020-NBLATEX", "symbol": "011780", "company_name": "금호석유화학", "round": "R4", "loop": "18", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_CONFIRMED_SPECIALTY_CHEMICAL_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R4L18-C17-KKPC-S2A-2020-08-03", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_margin_supercycle", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "representative aggregate trigger; no production scoring change"}
{"row_type": "case", "case_id": "R4L18-C17-LOTTECHEM-2023-REOPEN-FAILED", "symbol": "011170", "company_name": "롯데케미칼", "round": "R4", "loop": "18", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_CONFIRMED_SPECIALTY_CHEMICAL_MARGIN_BRIDGE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R4L18-C17-LOTTECHEM-S2-2023-02-14", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_rerating_margin_bridge_absent", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "representative aggregate trigger; no production scoring change"}
{"row_type": "case", "case_id": "R4L18-C17-KPIC-2023-NCC-FAILED", "symbol": "006650", "company_name": "대한유화", "round": "R4", "loop": "18", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_CONFIRMED_SPECIALTY_CHEMICAL_MARGIN_BRIDGE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R4L18-C17-KPIC-S2-2023-02-14", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_rerating_reopening_beta_without_margin_bridge", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "representative aggregate trigger; no production scoring change"}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "R4L18-C17-HYOTNC-S2A-2020-11-02", "case_id": "R4L18-C17-HYOTNC-2020-SPANDEX", "symbol": "298020", "company_name": "효성티앤씨", "round": "R4", "loop": "18", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_CONFIRMED_SPECIALTY_CHEMICAL_MARGIN_BRIDGE", "sector": "소재·스프레드·전략자원", "primary_archetype": "chemical commodity margin spread", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-10-30", "evidence_available_at_that_date": "3Q20 이후 스판덱스 수요/판가/가동률 개선이 실적 개선으로 이어진 margin bridge가 확인되기 시작한 구간. 당일/익거래일 가격 반응 가능성 기준으로 2020-11-02 종가를 사용.", "evidence_source": "historical public earnings/sector-spread note family; stock-web price row anchored", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv", "profile_path": "atlas/symbol_profiles/298/298020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-11-02", "entry_price": 155500, "MFE_30D_pct": 41.48, "MFE_90D_pct": 269.13, "MFE_180D_pct": 519.29, "MFE_1Y_pct": 519.29, "MFE_2Y_pct": 519.29, "MAE_30D_pct": -5.47, "MAE_90D_pct": -5.47, "MAE_180D_pct": -5.47, "MAE_1Y_pct": -5.47, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -75.2, "green_lateness_ratio": 0.49, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_mfe", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L18-C17-HYOTNC-2020-11-02-155500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L18-C17-HYOTNC-4B-2021-07-16", "case_id": "R4L18-C17-HYOTNC-2020-SPANDEX", "symbol": "298020", "company_name": "효성티앤씨", "round": "R4", "loop": "18", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_CONFIRMED_SPECIALTY_CHEMICAL_MARGIN_BRIDGE", "sector": "소재·스프레드·전략자원", "primary_archetype": "chemical commodity margin spread", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2021-07-16", "evidence_available_at_that_date": "스판덱스 supercycle의 가격/positioning 과열 구간. 다만 price-only local peak는 full 4B로 단독 승격하지 않고, valuation/revision fatigue 동반 여부를 별도 확인해야 한다.", "evidence_source": "stock-web peak row + valuation/revision fatigue hypothesis for overlay calibration", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv", "profile_path": "atlas/symbol_profiles/298/298020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-07-16", "entry_price": 881000, "MFE_30D_pct": 9.31, "MFE_90D_pct": 9.31, "MFE_180D_pct": 9.31, "MFE_1Y_pct": 9.31, "MFE_2Y_pct": 9.31, "MAE_30D_pct": -9.31, "MAE_90D_pct": -28.6, "MAE_180D_pct": -49.1, "MAE_1Y_pct": -61.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -75.2, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_if_non_price_fatigue_confirmed", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_risk_window", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L18-C17-HYOTNC-2021-07-16-881000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_case_new_4B_timing_path", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L18-C17-KKPC-S2A-2020-08-03", "case_id": "R4L18-C17-KKPC-2020-NBLATEX", "symbol": "011780", "company_name": "금호석유화학", "round": "R4", "loop": "18", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_CONFIRMED_SPECIALTY_CHEMICAL_MARGIN_BRIDGE", "sector": "소재·스프레드·전략자원", "primary_archetype": "chemical commodity margin spread", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-07-31", "evidence_available_at_that_date": "NB latex / 합성고무 수요와 판가 개선이 실적 레버리지로 연결되기 시작한 구간. 2020년 하반기부터 가격·실적·상대강도가 같이 열렸다.", "evidence_source": "historical public earnings/sector-spread note family; stock-web price row anchored", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-08-03", "entry_price": 82100, "MFE_30D_pct": 40.07, "MFE_90D_pct": 90.62, "MFE_180D_pct": 263.58, "MFE_1Y_pct": 263.58, "MFE_2Y_pct": 263.58, "MAE_30D_pct": -0.97, "MAE_90D_pct": -0.97, "MAE_180D_pct": -0.97, "MAE_1Y_pct": -0.97, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2021-05-06", "peak_price": 298500, "drawdown_after_peak_pct": -66.2, "green_lateness_ratio": 0.36, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_margin_supercycle", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L18-C17-KKPC-2020-08-03-82100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L18-C17-LOTTECHEM-S2-2023-02-14", "case_id": "R4L18-C17-LOTTECHEM-2023-REOPEN-FAILED", "symbol": "011170", "company_name": "롯데케미칼", "round": "R4", "loop": "18", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_CONFIRMED_SPECIALTY_CHEMICAL_MARGIN_BRIDGE", "sector": "소재·스프레드·전략자원", "primary_archetype": "chemical commodity margin spread", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage2", "trigger_date": "2023-02-14", "evidence_available_at_that_date": "중국 리오프닝/석유화학 spread 회복 기대는 있었으나, feedstock spread와 영업 레버리지의 닫힘이 약했다. 2023-02-13 corporate-action candidate 이후 다음 clean trading day를 entry로 사용했다.", "evidence_source": "historical public reopening/spread narrative + stock-web clean post-corporate-action row", "stage2_evidence_fields": ["policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011170/2023.csv", "profile_path": "atlas/symbol_profiles/011/011170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-14", "entry_price": 175800, "MFE_30D_pct": 10.52, "MFE_90D_pct": 10.52, "MFE_180D_pct": 10.52, "MFE_1Y_pct": 10.52, "MFE_2Y_pct": 10.52, "MAE_30D_pct": -2.16, "MAE_90D_pct": -6.09, "MAE_180D_pct": -28.16, "MAE_1Y_pct": -28.16, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-02-22", "peak_price": 194300, "drawdown_after_peak_pct": -35.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "failed_rerating_margin_bridge_absent", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2023-02-13_candidate", "same_entry_group_id": "R4L18-C17-LOTTECHEM-2023-02-14-175800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L18-C17-KPIC-S2-2023-02-14", "case_id": "R4L18-C17-KPIC-2023-NCC-FAILED", "symbol": "006650", "company_name": "대한유화", "round": "R4", "loop": "18", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPREAD_CONFIRMED_SPECIALTY_CHEMICAL_MARGIN_BRIDGE", "sector": "소재·스프레드·전략자원", "primary_archetype": "chemical commodity margin spread", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage2", "trigger_date": "2023-02-14", "evidence_available_at_that_date": "NCC/PE·PP spread 회복 기대와 리오프닝 beta는 있었으나, 재고/수요/스프레드가 Stage3의 margin bridge로 닫히지 못한 반례.", "evidence_source": "historical public petrochemical-spread narrative + stock-web price row anchored", "stage2_evidence_fields": ["policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006650/2023.csv", "profile_path": "atlas/symbol_profiles/006/006650.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-14", "entry_price": 162200, "MFE_30D_pct": 19.48, "MFE_90D_pct": 19.48, "MFE_180D_pct": 19.48, "MFE_1Y_pct": 19.48, "MFE_2Y_pct": 19.48, "MAE_30D_pct": -5.49, "MAE_90D_pct": -17.82, "MAE_180D_pct": -33.42, "MAE_1Y_pct": -33.42, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-02-23", "peak_price": 193800, "drawdown_after_peak_pct": -44.3, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "failed_rerating_reopening_beta_without_margin_bridge", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L18-C17-KPIC-2023-02-14-162200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c17_shadow", "case_id": "R4L18-C17-HYOTNC-2020-SPANDEX", "trigger_id": "R4L18-C17-HYOTNC-S2A-2020-11-02", "symbol": "298020", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 24, "revision_score": 20, "relative_strength_score": 18, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 28, "revision_score": 22, "relative_strength_score": 18, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 87, "stage_label_after": "Stage3-Green", "changed_components": ["margin_bridge_score", "revision_score"], "component_delta_explanation": "C17에서는 commodity spread가 실제 gross margin/OP revision으로 닫힐 때만 Green 승격. 효성티앤씨/금호석유는 spread narrative가 수익성으로 번역되었다.", "MFE_90D_pct": 269.13, "MAE_90D_pct": -5.47, "score_return_alignment_label": "strong_positive_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c17_shadow", "case_id": "R4L18-C17-HYOTNC-2020-SPANDEX", "trigger_id": "R4L18-C17-HYOTNC-4B-2021-07-16", "symbol": "298020", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 18, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 83, "stage_label_before": "Stage3-Green-with-4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68, "stage_label_after": "Stage4B-Overlay", "changed_components": ["valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "Full 4B는 price-only가 아니라 valuation/revision fatigue가 붙을 때 overlay로만 사용한다.", "MFE_90D_pct": 9.31, "MAE_90D_pct": -28.6, "score_return_alignment_label": "risk_alignment_after_peak", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c17_shadow", "case_id": "R4L18-C17-KKPC-2020-NBLATEX", "trigger_id": "R4L18-C17-KKPC-S2A-2020-08-03", "symbol": "011780", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 24, "revision_score": 20, "relative_strength_score": 18, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 28, "revision_score": 22, "relative_strength_score": 18, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 87, "stage_label_after": "Stage3-Green", "changed_components": ["margin_bridge_score", "revision_score"], "component_delta_explanation": "C17에서는 commodity spread가 실제 gross margin/OP revision으로 닫힐 때만 Green 승격. 효성티앤씨/금호석유는 spread narrative가 수익성으로 번역되었다.", "MFE_90D_pct": 90.62, "MAE_90D_pct": -0.97, "score_return_alignment_label": "strong_positive_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c17_shadow", "case_id": "R4L18-C17-LOTTECHEM-2023-REOPEN-FAILED", "trigger_id": "R4L18-C17-LOTTECHEM-S2-2023-02-14", "symbol": "011170", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage2-Watch/No-Promotion", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "리오프닝/베타만으로는 C17 positive promotion 불가. spread가 OP revision으로 닫히지 않으면 Stage2 watch에 묶는다.", "MFE_90D_pct": 10.52, "MAE_90D_pct": -6.09, "score_return_alignment_label": "false_positive_guard_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c17_shadow", "case_id": "R4L18-C17-KPIC-2023-NCC-FAILED", "trigger_id": "R4L18-C17-KPIC-S2-2023-02-14", "symbol": "006650", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage2-Watch/No-Promotion", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "리오프닝/베타만으로는 C17 positive promotion 불가. spread가 OP revision으로 닫히지 않으면 Stage2 watch에 묶는다.", "MFE_90D_pct": 19.48, "MAE_90D_pct": -17.82, "score_return_alignment_label": "false_positive_guard_alignment", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c17_spread_to_op_bridge_gate,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Promote C17 only when spread improvement is visible in margin bridge/revision, not just commodity beta or reopening narrative.","HYO/Kumho positives preserved; Lotte/KPIC false positives blocked.","R4L18-C17-HYOTNC-S2A-2020-11-02|R4L18-C17-KKPC-S2A-2020-08-03|R4L18-C17-LOTTECHEM-S2-2023-02-14|R4L18-C17-KPIC-S2-2023-02-14",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c17_reopening_beta_no_green_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"China/reopening beta cannot become Stage3-Green unless spread-to-OP revision closes.","Two 2023 false positives become Stage2-watch rather than Green.","R4L18-C17-LOTTECHEM-S2-2023-02-14|R4L18-C17-KPIC-S2-2023-02-14",2,2,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "18", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 0, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["reopening_beta_false_positive", "spread_narrative_without_margin_bridge", "price_only_4B_requires_non_price_confirmation"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows
```jsonl
{"row_type": "narrative_only", "case_id": "none", "symbol": "000000", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "reason": "no narrative-only row; all representative triggers have clean 180D stock-web windows", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration_placeholder"}
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
Recommended next coverage gap: R8 / L8 / C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, or R6 / L6 / C22_INSURANCE_RATE_CYCLE_RESERVE. Do not re-run R4/C17 with the same four symbols and same entry dates unless a new trigger family or calculation correction is being added.

## 28. Source Notes

Primary source notes:
- Stock-web manifest: fileciteturn442file0
- Stock-agent ingest/coverage summary: fileciteturn441file0
- Hyosung TNC profile and shards: fileciteturn443file0turn449file0turn450file0
- Kumho Petrochemical profile and shards: fileciteturn444file0turn445file0turn451file0turn452file0
- Lotte Chemical profile and shards: fileciteturn446file0turn447file0turn453file0turn454file0
- KPIC/Daehan profile and shards: fileciteturn448file0turn455file0turn456file0

Caveat: The research proxy uses historical public earnings/spread evidence families to separate stage evidence, but this chat run did not open stock_agent source code and did not execute the embedded handoff prompt. Quantitative calibration relies on stock-web tradable raw OHLC rows and is intended for shadow-only calibration.
