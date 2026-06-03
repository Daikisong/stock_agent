# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
```text
round = R13
loop = 57
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selection_mode = auto_coverage_gap_fill
output_file = e2r_stock_web_v12_residual_round_R13_loop_57_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
current_stock_discovery_allowed = false
stock_web_price_atlas_access_required = true
```
This file is historical calibration research only. It is not a live candidate scan, not an investment recommendation, and not a repository patch. The loop was auto-selected because local v12 output coverage already included recent L3/C14 and L1/C02 artifacts, while C04 nuclear-policy / project / legal-delay coverage was missing in the local MD snapshot.
## 1. Current Calibrated Profile Assumption
```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```
## 2. Round / Large Sector / Canonical Archetype Scope
| field | value |
|---|---|
| round | R13 |
| loop | 57 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY |
| fine_archetype_id | CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_DELAY |
| loop_objective | auto_coverage_gap_fill; sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test |
| selected evidence window | 2024-07-17 Czech preferred-bidder decision through 2025-04 legal/forward-window stress |

## 3. Previous Coverage / Duplicate Avoidance Check
- Local v12 artifacts in `/mnt/data` already contained many L5/L6/L7/L8 loops and the immediately preceding L3/C14 battery-demand-slowdown MD.
- L1/C02 power-grid/data-center CAPEX also appeared in local output history, so this loop deliberately moved to C04 rather than re-materializing C02.
- Duplicate key blocked: same `symbol + trigger_date + entry_date + evidence family`. None of the representative C04 rows below reused an existing local C04 row.
- Auto-selected coverage gap: `C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY` had no prior local v12 MD in the observed artifact snapshot.

## 4. Stock-Web OHLC Input / Price Source Validation
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
| markets | ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI'] |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Stock-Web manifest confirms `max_date = 2026-02-20`, `price_adjustment_status = raw_unadjusted_marcap`, and calibration-safe tradable shards under `atlas/ohlcv_tradable_by_symbol_year`. The manifest also states that zero-volume / invalid OHLC rows are excluded from calibration shards and corporate-action-contaminated windows are blocked by default. fileciteturn943file0

## 5. Historical Eligibility Gate
| case_id | symbol | entry_date | forward_180D_available | corporate_action_window_status | calibration_usable | note |
|---|---:|---|---:|---|---:|---|
| C04_DOOSAN_202407_CZECH_PREFERRED_BIDDER_HIGH_MAE_DELAYED_SUCCESS | 034020 | 2024-07-18 | true | clean_180D_window; historical profile candidate dates do not overlap 2024/2025 window | true | 180D window is inside stock-web max_date 2026-02-20 |
| C04_KEPCO_EC_202407_CZECH_PREFERRED_BIDDER_FAILED_RERATING | 052690 | 2024-07-18 | true | clean_180D_window_no_profile_candidate_dates | true | 180D window is inside stock-web max_date 2026-02-20 |
| C04_KEPCO_KPS_202407_CZECH_SERVICE_EXPOSURE_SMOOTHER_SUCCESS | 051600 | 2024-07-18 | true | clean_180D_window_no_profile_candidate_dates | true | 180D window is inside stock-web max_date 2026-02-20 |

- Doosan Enerbility profile has historical corporate-action candidates, but the listed candidate dates end before the 2024/2025 calibration window used here, so the selected 180D window is treated as clean for this loop. fileciteturn969file0
- KEPCO E&C and KEPCO KPS profiles show no corporate-action candidate dates, making the 2024-07-18 to 180D windows usable for calibration. fileciteturn971file0 fileciteturn972file0

## 6. Canonical Archetype Compression Map
| fine_archetype_id | canonical_archetype_id | compression rationale |
|---|---|---|
| CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_DELAY | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | Preferred-bidder event creates policy optionality, but final project economics depend on contract signing, appeals, financing, localization, and schedule. |
| NUCLEAR_VALUE_CHAIN_SERVICE_EXPOSURE | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | Service/maintenance exposure should remain in C04, but has different MAE profile from pure EPC/design optionality. |
| NUCLEAR_EPC_DESIGN_EVENT_BETA | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | Design/EPC-linked symbols can spike on event beta while lacking conversion evidence. |

## 7. Case Selection Summary
| case_id | symbol | company | role | positive_or_counterexample | current_profile_verdict |
|---|---:|---|---|---|---|
| C04_DOOSAN_202407_CZECH_PREFERRED_BIDDER_HIGH_MAE_DELAYED_SUCCESS | 034020 | 두산에너빌리티 | high_mae_success | positive | current_profile_too_early |
| C04_KEPCO_EC_202407_CZECH_PREFERRED_BIDDER_FAILED_RERATING | 052690 | 한전기술 | failed_rerating | counterexample | current_profile_false_positive |
| C04_KEPCO_KPS_202407_CZECH_SERVICE_EXPOSURE_SMOOTHER_SUCCESS | 051600 | 한전KPS | structural_success | positive | current_profile_correct |

## 8. Positive vs Counterexample Balance
```text
positive_case_count = 2
counterexample_count = 1
4B_or_4C_overlay_trigger_count = 2
minimum_calibration_usable_case_count = 3
positive_case_missing = false
counterexample_search_incomplete = false
```
The set intentionally pairs two positive or partially positive paths with one failed-rerating counterexample. This prevents the C04 rule from becoming a simple “nuclear event bullish” rule.

## 9. Evidence Source Map
| event_date | evidence family | source note | stage usage |
|---|---|---|---|
| 2024-07-17 | Czech government selected KHNP as preferred bidder for Dukovany nuclear units; Korean nuclear value-chain equities reacted. | Reuters coverage of Czech preferred-bidder decision and Korean nuclear share reaction. | Stage2-Actionable / policy optionality |
| 2024-10-30 | Czech anti-monopoly office temporarily prohibited contract signing during EDF / Westinghouse appeals. | Reuters legal-delay coverage. | 4B / 4C-watch, not hard 4C by itself |
| 2025-05-06 and 2025-06-04 | Court block and later signing-clearance sequence. | AP legal block and later signing coverage. | Narrative-only validation of “procedural delay vs thesis break” distinction |

## 10. Price Data Source Map
| symbol | company | tradable_shard | profile_path | key fetched rows |
|---:|---|---|---|---|
| 034020 | 두산에너빌리티 | atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv; 2025.csv | atlas/symbol_profiles/034/034020.json | 2024-07-18, 2024-10-31, 2025-02-19, 2025-04 window. fileciteturn962file0 fileciteturn963file0 |
| 052690 | 한전기술 | atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv; 2025.csv | atlas/symbol_profiles/052/052690.json | 2024-07-18 spike, 2025-04 low. fileciteturn965file0 fileciteturn966file0 |
| 051600 | 한전KPS | atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv; 2025.csv | atlas/symbol_profiles/051/051600.json | 2024-07-18 entry, 2024-12-03 4B-watch, 2025-04 window. fileciteturn967file0 fileciteturn968file0 |

## 11. Case-by-Case Trigger Grid
| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | evidence fields | aggregate_role | current_profile_verdict |
|---|---:|---|---|---|---:|---|---|---|
| C04_DOOSAN_20240718_STAGE2_ACTIONABLE | 034020 | Stage2-Actionable | 2024-07-17 | 2024-07-18 | 21000 | public_event_or_disclosure,policy_or_regulatory_optionality,backlog_or_delivery_visibility,multiple_public_sources | representative | current_profile_too_early |
| C04_DOOSAN_20241031_PROCEDURAL_LEGAL_DELAY_WATCH | 034020 | 4C-watch / legal-delay overlay | 2024-10-30 | 2024-10-31 | 20050 | legal_or_regulatory_block,explicit_event_cap | 4C_overlay_only | current_profile_4C_too_early_if_hard_routed |
| C04_KEPCO_EC_20240718_STAGE2_ACTIONABLE | 052690 | Stage2-Actionable | 2024-07-17 | 2024-07-18 | 82000 | public_event_or_disclosure,policy_or_regulatory_optionality,price_only_local_peak,positioning_overheat | representative | current_profile_false_positive |
| C04_KEPCO_KPS_20240718_STAGE2_ACTIONABLE | 051600 | Stage2-Actionable | 2024-07-17 | 2024-07-18 | 38900 | public_event_or_disclosure,policy_or_regulatory_optionality,backlog_or_delivery_visibility,financial_visibility | representative | current_profile_correct |
| C04_KEPCO_KPS_20241203_4B_VALUATION_WATCH | 051600 | 4B-watch | 2024-12-03 | 2024-12-03 | 48600 | valuation_blowoff,positioning_overheat | 4B_overlay_only | current_profile_correct |

## 12. Trigger-Level OHLC Backtest Tables
| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| C04_DOOSAN_20240718_STAGE2_ACTIONABLE | 21000 | 19.05 | -27.86 | 19.05 | -27.86 | 47.14 | -27.86 | 2025-02-19 | 30900 | -35.4 |
| C04_DOOSAN_20241031_PROCEDURAL_LEGAL_DELAY_WATCH | 20050 | 12.22 | -3.49 | 54.11 | -14.21 | 54.11 | -14.21 | 2025-02-19 | 30900 | -35.4 |
| C04_KEPCO_EC_20240718_STAGE2_ACTIONABLE | 82000 | 19.63 | -24.88 | 19.63 | -24.88 | 19.63 | -39.27 | 2024-07-18 | 98100 | -49.24 |
| C04_KEPCO_KPS_20240718_STAGE2_ACTIONABLE | 38900 | 21.98 | -7.84 | 24.04 | -7.84 | 26.22 | -2.31 | 2024-12-03 | 49100 | -22.61 |
| C04_KEPCO_KPS_20241203_4B_VALUATION_WATCH | 48600 | -1.03 | -14.3 | -1.03 | -21.4 | -1.03 | -21.4 | 2024-12-03 | 49100 | -22.61 |

Representative row aggregate: avg_MFE_90D_pct = 20.91, avg_MAE_90D_pct = -20.19, avg_MFE_180D_pct = 30.99, avg_MAE_180D_pct = -23.15. The average hides the important residual: KPS had low MAE while KEPCO E&C had severe 180D drawdown.

## 13. Current Calibrated Profile Stress Test
| case | current profile likely label | actual alignment | verdict |
|---|---|---|---|
| 두산에너빌리티 | Stage2-Actionable may be too aggressively promoted toward Yellow because policy event + RS were visible. | 180D MFE eventually strong, but initial -27.86% MAE says premature Green/Yellow would be hard to hold. | current_profile_too_early |
| 한전기술 | Preferred-bidder spike could cross event/repricing threshold even without confirmed contract economics. | +19.63% MFE but -39.27% 180D MAE; peak was entry day. | current_profile_false_positive |
| 한전KPS | Stage2-Actionable / Yellow watch is reasonable because service exposure had lower MAE. | +26.22% 180D MFE and only -2.31% 180D MAE from July entry. | current_profile_correct |
| 2024-10 legal delay | If hard 4C fired on temporary appeal alone, it would be too early. | Doosan rallied to 2025-02 peak after the temporary prohibition. | current_profile_4C_too_early_if_hard_routed |

## 14. Stage2 / Yellow / Green Comparison
- Stage2-Actionable is justified for all three July 2024 nuclear-policy rows because the public event was real and immediate.
- Stage3-Yellow should be capped or delayed for C04 preferred-bidder-only exposure unless contract probability, financing/legal clearance, and earnings bridge are independently visible.
- Stage3-Green should not be assigned from the preferred-bidder event alone. No trigger here had enough confirmed revision and low legal/contract risk at the July date.
- Green lateness ratio is not applicable because no confirmed Stage3-Green trigger was accepted in this loop.

## 15. 4B Local vs Full-window Timing Audit
| trigger_id | four_b_evidence_type | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---|---:|---:|---|
| C04_KEPCO_EC_20240718_STAGE2_ACTIONABLE | price_only; positioning_overheat; legal_or_regulatory_block | 1.00 | 1.00 | event spike was both local and full-window peak; 4B watch was justified, but not because price alone promotes any positive stage |
| C04_KEPCO_KPS_20241203_4B_VALUATION_WATCH | valuation_blowoff; positioning_overheat | 0.95 | 0.95 | good 4B-watch timing; subsequent 90D/180D forward return was weak |
| C04_DOOSAN_20241031_PROCEDURAL_LEGAL_DELAY_WATCH | legal_or_regulatory_block | not_applicable | not_applicable | legal-delay overlay should be watch/risk, not hard 4C unless the appeal blocks signing or cancels thesis |

## 16. 4C Protection Audit
The 2024-10-30 temporary Czech anti-monopoly appeal is a useful C04 residual: treating every procedural appeal as hard 4C would have exited Doosan before its 2025-02 high. The correct distinction is between `procedural appeal / signing delay watch` and `hard legal block / contract cancellation / final thesis break`. The 2025 court block and later signing-clearance sequence is retained as narrative-only evidence that C04 needs a two-step legal delay model.

```text
four_c_protection_label_2024_10 = false_break_watch_only
recommended_4C_route = hard_4c only after final injunction, contract cancellation, or explicit signing failure; otherwise 4B/legal-watch
```

## 17. Sector-Specific Rule Candidate
```text
rule_scope = sector_specific
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
axis = c04_policy_win_requires_contract_probability_and_legal_delay_discount
proposal_type = sector_shadow_only
production_scoring_changed = false
```
Rule candidate: in L1 nuclear-policy/project rows, a preferred-bidder decision creates Stage2 optionality but should not receive full Stage3/Green treatment unless contract probability, legal clearance, financing path, project margin bridge, and backlog conversion evidence are present. The mechanism is simple: policy opens the door, but legal/contract execution decides whether the door stays open.

## 18. Canonical-Archetype Rule Candidate
```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
axis_1 = c04_preferred_bidder_only_stage3_cap
axis_2 = c04_procedural_appeal_watch_not_hard4c
```
C04 should split evidence into three clocks: event clock, contract/legal clock, and earnings/backlog clock. Event clock alone is fast and tradable but fragile; contract/legal clock determines whether the event deserves Yellow/Green; earnings/backlog clock determines whether rerating survives beyond the first spike.

## 19. Before / After Backtest Comparison
| profile_id | scope | eligible_representative_count | selected_entries | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | score_return_alignment_verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global proxy | 3 | all Stage2 event rows | 20.91 | -20.19 | 30.99 | -23.15 | 0.33 | captures event beta but over-promotes KEPCO E&C risk |
| P0b_e2r_2_0_baseline_reference | old baseline | 3 | more price/event weighted | 20.91 | -20.19 | 30.99 | -23.15 | 0.33 | weaker legal-delay handling |
| P1_sector_specific_candidate_profile | L1 sector | 3 | C04 event rows with legal discount | 20.91 | -20.19 | 30.99 | -23.15 | 0.33 | same entries, better stage labels |
| P2_canonical_archetype_candidate_profile | C04 | 2 promoted, 1 watch | Doosan + KPS promoted; KEPCO E&C watch-only | 21.55 | -17.85 | 36.68 | -15.09 | 0.00 | improves score-return alignment by preventing design/EPC event-beta overpromotion |
| P3_counterexample_guard_profile | C04 guard | 1 promoted, 2 watch/4B | KPS preferred as lower-MAE representative | 24.04 | -7.84 | 26.22 | -2.31 | 0.00 | too strict for Doosan delayed success, but useful as red-team guard |

## 20. Score-Return Alignment Matrix
| symbol | before label | after label | score-return alignment | reason |
|---:|---|---|---|---|
| 034020 | Stage3-Yellow borderline | Stage2-Actionable / legal-clearance watch | improved | avoids premature high-MAE promotion while preserving delayed 180D upside |
| 052690 | Stage3-Yellow borderline | Stage2-watch / no Green | improved | event spike did not convert; peak occurred on entry day and 180D MAE was -39.27% |
| 051600 | Stage2-Actionable | Stage3-Yellow service-exposure exception | improved | lower MAE and smoother path justify a positive exception within C04 |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_DELAY | 2 | 1 | 2 | 1 watch-only | 3 | 0 | 5 | 3 | 2 | true | true | C04 now has initial positive/counterexample/legal-delay seed; needs additional non-Czech nuclear cases later |

## 22. Residual Contribution Summary
```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [preferred_bidder_event_false_positive, high_mae_delayed_success, procedural_legal_delay_false_4c]
new_axis_proposed: [c04_policy_win_requires_contract_probability_and_legal_delay_discount, c04_procedural_appeal_watch_not_hard4c]
existing_axis_strengthened: [full_4b_requires_non_price_evidence]
existing_axis_weakened: [hard_4c_thesis_break_routes_to_4c for procedural appeals without final injunction or contract failure]
existing_axis_kept: [price_only_blowoff_blocks_positive_stage, stage3_green_revision_min]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: avg=23.7; no repeated same-symbol/same-trigger representative rows; three new C04 symbols
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C04 zero local v12 MD coverage before this loop in /mnt/data snapshot
```

## 23. Validation Scope / Non-Validation Scope
Validated: historical event-timed OHLC behavior for three Korean C04 nuclear value-chain symbols, using stock-web tradable_raw rows and profile caveats. Not validated: live investment candidates, current 2026 stage labels, brokerage execution, stock_agent code behavior, production scoring, or global calibration changes.

## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c04_preferred_bidder_only_stage3_cap,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,0,1,+1,"Preferred-bidder event alone overpromotes pure design/EPC beta; require contract/legal/earnings bridge before Yellow/Green","Blocks KEPCO E&C false positive while keeping KPS service exception",C04_KEPCO_EC_20240718_STAGE2_ACTIONABLE|C04_DOOSAN_20240718_STAGE2_ACTIONABLE|C04_KEPCO_KPS_20240718_STAGE2_ACTIONABLE,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c04_procedural_appeal_watch_not_hard4c,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,0,1,+1,"Temporary appeal/procurement review should be 4B/legal-watch, not hard 4C unless final injunction/cancellation occurs","Avoids false hard-4C on 2024-10 procedural delay before later rally",C04_DOOSAN_20241031_PROCEDURAL_LEGAL_DELAY_WATCH,1,1,0,low,canonical_shadow_only,"not production; needs more legal-delay cases"
```

## 25. Machine-Readable Rows
### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "C04_DOOSAN_202407_CZECH_PREFERRED_BIDDER_HIGH_MAE_DELAYED_SUCCESS", "symbol": "034020", "company_name": "두산에너빌리티", "round": "R13", "loop": "57", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_DELAY", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "C04_DOOSAN_20240718_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Preferred-bidder event created immediate upside but also -27.86% 30D/90D MAE; 180D MFE recovered to +47.14%. The useful rule is not “ignore the event”, but “do not Green it without contract/legal/earnings bridge.”", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "Preferred-bidder event created immediate upside but also -27.86% 30D/90D MAE; 180D MFE recovered to +47.14%. The useful rule is not “ignore the event”, but “do not Green it without contract/legal/earnings bridge.”"}
{"row_type": "case", "case_id": "C04_KEPCO_EC_202407_CZECH_PREFERRED_BIDDER_FAILED_RERATING", "symbol": "052690", "company_name": "한전기술", "round": "R13", "loop": "57", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_DELAY", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "C04_KEPCO_EC_20240718_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Pure design/engineering exposure reacted strongly on the Czech preferred-bidder event, but the row failed to convert into durable rerating within 180D: MFE stayed +19.63% while MAE widened to -39.27%.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Pure design/engineering exposure reacted strongly on the Czech preferred-bidder event, but the row failed to convert into durable rerating within 180D: MFE stayed +19.63% while MAE widened to -39.27%."}
{"row_type": "case", "case_id": "C04_KEPCO_KPS_202407_CZECH_SERVICE_EXPOSURE_SMOOTHER_SUCCESS", "symbol": "051600", "company_name": "한전KPS", "round": "R13", "loop": "57", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_DELAY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C04_KEPCO_KPS_20240718_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Service/maintenance exposure had a smaller but cleaner path: +21.98% 30D MFE, only -7.84% 30D/90D MAE, and +26.22% 180D MFE.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Service/maintenance exposure had a smaller but cleaner path: +21.98% 30D MFE, only -7.84% 30D/90D MAE, and +26.22% 180D MFE."}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "C04_DOOSAN_20240718_STAGE2_ACTIONABLE", "case_id": "C04_DOOSAN_202407_CZECH_PREFERRED_BIDDER_HIGH_MAE_DELAYED_SUCCESS", "symbol": "034020", "company_name": "두산에너빌리티", "round": "R13", "loop": "57", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_DELAY", "sector": "industrials_infra_defense_grid", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "auto_coverage_gap_fill;sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;4B_non_price_requirement_stress_test;4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "Czech government selected KHNP as preferred bidder; direct Korean nuclear value-chain reaction.", "evidence_source": "Reuters 2024-07-17/18 Czech preferred-bidder coverage; Stock-Web rows for 2024-07-18 and 2025-02-19.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv", "profile_path": "atlas/symbol_profiles/034/034020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 21000, "MFE_30D_pct": 19.05, "MFE_90D_pct": 19.05, "MFE_180D_pct": 47.14, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -27.86, "MAE_90D_pct": -27.86, "MAE_180D_pct": -27.86, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-19", "peak_price": 30900, "drawdown_after_peak_pct": -35.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "delayed_180d_success_high_mae", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_candidate_dates_not_overlapping_2024_07_18_to_2025_04_11", "same_entry_group_id": "C04_DOOSAN_20240718_CLOSE_21000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C04_DOOSAN_20241031_PROCEDURAL_LEGAL_DELAY_WATCH", "case_id": "C04_DOOSAN_202407_CZECH_PREFERRED_BIDDER_HIGH_MAE_DELAYED_SUCCESS", "symbol": "034020", "company_name": "두산에너빌리티", "round": "R13", "loop": "57", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_DELAY", "sector": "industrials_infra_defense_grid", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "auto_coverage_gap_fill;sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;4B_non_price_requirement_stress_test;4C_thesis_break_timing_test", "trigger_type": "4C-watch / legal-delay overlay", "trigger_date": "2024-10-30", "evidence_available_at_that_date": "Czech anti-monopoly office temporarily prohibited signing while EDF/Westinghouse appeals proceeded, but this later did not become an immediate thesis break.", "evidence_source": "Reuters 2024-10-30 legal-delay coverage; Doosan Stock-Web 2024-10-31 through 2025-04 window.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["legal_or_regulatory_block", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv", "profile_path": "atlas/symbol_profiles/034/034020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-10-31", "entry_price": 20050, "MFE_30D_pct": 12.22, "MFE_90D_pct": 54.11, "MFE_180D_pct": 54.11, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.49, "MAE_90D_pct": -14.21, "MAE_180D_pct": -14.21, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-19", "peak_price": 30900, "drawdown_after_peak_pct": -35.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "procedural_appeal_not_hard_4c", "four_b_evidence_type": ["legal_or_regulatory_block"], "four_c_protection_label": "false_break_watch_only", "trigger_outcome_label": "legal_delay_watch_but_not_thesis_break", "current_profile_verdict": "current_profile_4C_too_early_if_hard_routed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_candidate_dates_not_overlapping_2024_10_31_to_2025_07_approx", "same_entry_group_id": "C04_DOOSAN_20241031_CLOSE_20050", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C04_KEPCO_EC_20240718_STAGE2_ACTIONABLE", "case_id": "C04_KEPCO_EC_202407_CZECH_PREFERRED_BIDDER_FAILED_RERATING", "symbol": "052690", "company_name": "한전기술", "round": "R13", "loop": "57", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_DELAY", "sector": "industrials_infra_defense_grid", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "auto_coverage_gap_fill;sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;4B_non_price_requirement_stress_test;4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "Preferred-bidder event attached to engineering/design exposure, but no enough confirmed revision or backlog conversion appeared by trigger date.", "evidence_source": "Reuters 2024-07-17/18 Czech preferred-bidder coverage; KEPCO E&C Stock-Web rows.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv", "profile_path": "atlas/symbol_profiles/052/052690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 82000, "MFE_30D_pct": 19.63, "MFE_90D_pct": 19.63, "MFE_180D_pct": 19.63, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -24.88, "MAE_90D_pct": -24.88, "MAE_180D_pct": -39.27, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-18", "peak_price": 98100, "drawdown_after_peak_pct": -49.24, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "event_spike_was_local_and_full_window_peak", "four_b_evidence_type": ["price_only", "positioning_overheat", "legal_or_regulatory_block"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_after_preferred_bidder_spike", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_profile_candidate_dates", "same_entry_group_id": "C04_KEPCO_EC_20240718_CLOSE_82000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C04_KEPCO_KPS_20240718_STAGE2_ACTIONABLE", "case_id": "C04_KEPCO_KPS_202407_CZECH_SERVICE_EXPOSURE_SMOOTHER_SUCCESS", "symbol": "051600", "company_name": "한전KPS", "round": "R13", "loop": "57", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_DELAY", "sector": "industrials_infra_defense_grid", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "auto_coverage_gap_fill;sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;4B_non_price_requirement_stress_test;4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "Service/maintenance exposure to nuclear lifecycle; less one-off EPC design optionality and lower MAE after the Czech event.", "evidence_source": "Reuters 2024-07-17/18 Czech preferred-bidder coverage; KEPCO KPS Stock-Web rows.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv", "profile_path": "atlas/symbol_profiles/051/051600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 38900, "MFE_30D_pct": 21.98, "MFE_90D_pct": 24.04, "MFE_180D_pct": 26.22, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.84, "MAE_90D_pct": -7.84, "MAE_180D_pct": -2.31, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-03", "peak_price": 49100, "drawdown_after_peak_pct": -22.61, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "smoother_service_exposure_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_profile_candidate_dates", "same_entry_group_id": "C04_KEPCO_KPS_20240718_CLOSE_38900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C04_KEPCO_KPS_20241203_4B_VALUATION_WATCH", "case_id": "C04_KEPCO_KPS_202407_CZECH_SERVICE_EXPOSURE_SMOOTHER_SUCCESS", "symbol": "051600", "company_name": "한전KPS", "round": "R13", "loop": "57", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_LEGAL_DELAY", "sector": "industrials_infra_defense_grid", "primary_archetype": "nuclear_policy_project_legal_delay", "loop_objective": "auto_coverage_gap_fill;sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;4B_non_price_requirement_stress_test;4C_thesis_break_timing_test", "trigger_type": "4B-watch", "trigger_date": "2024-12-03", "evidence_available_at_that_date": "After the smoother KPS move, late-2024 extended valuation/positioning had weak forward return and larger drawdown than the July entry.", "evidence_source": "KEPCO KPS Stock-Web 2024-12-03 and 2025-04 window.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv", "profile_path": "atlas/symbol_profiles/051/051600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-12-03", "entry_price": 48600, "MFE_30D_pct": -1.03, "MFE_90D_pct": -1.03, "MFE_180D_pct": -1.03, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -14.3, "MAE_90D_pct": -21.4, "MAE_180D_pct": -21.4, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-03", "peak_price": 49100, "drawdown_after_peak_pct": -22.61, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "good_full_window_4B_watch_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_not_required", "trigger_outcome_label": "late_cycle_4b_watch_reduced_forward_return", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_profile_candidate_dates", "same_entry_group_id": "C04_KEPCO_KPS_20241203_CLOSE_48600", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C04_DOOSAN_202407_CZECH_PREFERRED_BIDDER_HIGH_MAE_DELAYED_SUCCESS", "trigger_id": "C04_DOOSAN_20240718_STAGE2_ACTIONABLE", "symbol": "034020", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 10, "margin_bridge_score": "unknown_or_not_supported", "revision_score": 5, "relative_strength_score": 12, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 20, "valuation_repricing_score": "unknown_or_not_supported", "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": -4, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow borderline", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 8, "margin_bridge_score": "unknown_or_not_supported", "revision_score": 5, "relative_strength_score": 10, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 18, "valuation_repricing_score": "unknown_or_not_supported", "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": -8, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 71, "stage_label_after": "Stage2-Actionable / C04 legal-clearance watch", "changed_components": ["contract_score", "legal_or_contract_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "Preferred-bidder is not a signed contract; legal/appeal path is discounted until final contract/legal clearance.", "MFE_90D_pct": 19.05, "MAE_90D_pct": -27.86, "score_return_alignment_label": "after_profile_better_handles_high_mae", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C04_KEPCO_EC_202407_CZECH_PREFERRED_BIDDER_FAILED_RERATING", "trigger_id": "C04_KEPCO_EC_20240718_STAGE2_ACTIONABLE", "symbol": "052690", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 2, "relative_strength_score": 12, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 22, "valuation_repricing_score": 16, "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow borderline", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 17, "valuation_repricing_score": 8, "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": -10, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 61, "stage_label_after": "Stage2-watch / no Green", "changed_components": ["valuation_repricing_score", "contract_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Engineering/design exposure had event beta but lacked backlog conversion and suffered the worst 180D MAE.", "MFE_90D_pct": 19.63, "MAE_90D_pct": -24.88, "score_return_alignment_label": "after_profile_blocks_false_positive_green", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C04_KEPCO_KPS_202407_CZECH_SERVICE_EXPOSURE_SMOOTHER_SUCCESS", "trigger_id": "C04_KEPCO_KPS_20240718_STAGE2_ACTIONABLE", "symbol": "051600", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": 12, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 10, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 17, "valuation_repricing_score": "unknown_or_not_supported", "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": 13, "margin_bridge_score": 7, "revision_score": 8, "relative_strength_score": 10, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 17, "valuation_repricing_score": "unknown_or_not_supported", "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 76, "stage_label_after": "Stage3-Yellow / service-exposure exception", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score"], "component_delta_explanation": "Lifecycle service/maintenance exposure had lower MAE and smoother 180D behavior, so C04 should not penalize all nuclear value-chain names equally.", "MFE_90D_pct": 24.04, "MAE_90D_pct": -7.84, "score_return_alignment_label": "after_profile_keeps_positive", "current_profile_verdict": "current_profile_correct"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c04_preferred_bidder_only_stage3_cap,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,0,1,+1,"Preferred bidder alone is not signed contract/revision evidence","Blocks false-positive Green/Yellow in pure design/EPC beta while keeping service-exposure exception",C04_KEPCO_EC_20240718_STAGE2_ACTIONABLE|C04_DOOSAN_20240718_STAGE2_ACTIONABLE|C04_KEPCO_KPS_20240718_STAGE2_ACTIONABLE,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c04_procedural_appeal_watch_not_hard4c,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,0,1,+1,"Procedural appeal is legal-watch until final injunction/cancellation","Avoids false hard-4C on temporary appeal before later rally",C04_DOOSAN_20241031_PROCEDURAL_LEGAL_DELAY_WATCH,1,1,0,low,canonical_shadow_only,"not production; needs more legal-delay cases"
```

### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": "57", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["preferred_bidder_event_false_positive", "high_mae_delayed_success", "procedural_legal_delay_false_4c"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "diversity_score_summary": "avg=23.7; three new C04 symbols; no same-symbol/same-trigger representative reuse", "auto_selected_coverage_gap": "C04 zero local v12 MD coverage before this loop in /mnt/data snapshot"}
```

### 25.7 narrative_only row
```jsonl
{"row_type": "narrative_only", "case_id": "C04_202505_CZECH_COURT_BLOCK_AND_202506_SIGNING_CLEARANCE", "symbol": "034020|052690|051600", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "reason": "2025 court block and later signing clearance used only to distinguish procedural/legal watch from hard 4C thesis break; not used for new weight calibration in this loop", "price_source": "Songdaiki/stock-web", "usage": "narrative_only_not_weight_calibration"}
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
Next recommended residual loop remains R13, preferably another missing canonical archetype rather than another C04 repetition. Candidates: C01/C05/C06/C08/C10/C11/C12/C13 if still absent in the coding-agent registry.

## 28. Source Notes
- Stock-Web manifest and row profile validation are based on GitHub-fetched `atlas/manifest.json`, symbol profile JSONs, and OHLC tradable shards. fileciteturn943file0 fileciteturn969file0 fileciteturn971file0 fileciteturn972file0
- Doosan Enerbility OHLC rows used for July 2024, October 2024, and 2025 forward windows come from stock-web tradable shards. fileciteturn962file0 fileciteturn963file0 fileciteturn964file0
- KEPCO E&C and KEPCO KPS OHLC rows used for July 2024 through April 2025 forward-window calculations come from stock-web tradable shards. fileciteturn965file0 fileciteturn966file0 fileciteturn967file0 fileciteturn968file0
- Historical event evidence is from Reuters/AP reporting on the Czech KHNP preferred-bidder selection, later appeal/procurement-delay route, court block, and eventual signing clearance; this MD uses those sources only for historical evidence timing and not for current candidate discovery.
