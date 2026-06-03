# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
- mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
- research_session: post_calibrated_sector_archetype_residual_research
- scheduled_round: R2
- scheduled_loop: 75
- completed_round: R2
- completed_loop: 75
- next_round: R3
- next_loop: 75
- large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
- canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
- fine_archetype_id: MEMORY_RECOVERY_EQUIPMENT_CYCLE_ORDER_QUALITY_VS_PRICE_ONLY_AI_BETA
- output_file: e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
- production_scoring_changed: false
- shadow_weight_only: true
- stock_agent_code_access_allowed: false
- stock_agent_code_patch_allowed: false
- stock_web_price_atlas_access_required: true
- current_stock_discovery_allowed: false

This loop adds 6 new independent cases, 2 counterexamples, and 5 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE.

## 1. Current Calibrated Profile Assumption
Current proxy is `e2r_2_1_stock_web_calibrated`, with Stage2 actionable bonus +2.0, Yellow minimum 75, Green minimum 87, Green revision minimum 55, cross-evidence Green buffer +1.5, price-only blowoff blocking positive stage, full 4B requiring non-price evidence, and hard 4C routing on thesis break.
This MD does not re-prove those global axes. It stress-tests the residual inside R2/C10: memory recovery and AI demand can lift almost every semiconductor ticker, but C10 should promote only those where equipment-cycle evidence acts like a drivetrain, not a painted speedometer.

## 2. Round / Large Sector / Canonical Archetype Scope
| field | value |
|---|---|
| scheduled_round | R2 |
| scheduled_loop | 75 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE |
| fine_archetype_id | MEMORY_RECOVERY_EQUIPMENT_CYCLE_ORDER_QUALITY_VS_PRICE_ONLY_AI_BETA |
| round_schedule_status | valid |
| round_sector_consistency | pass |
| loop_objective | residual_false_positive_mining; residual_missed_structural_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; coverage_gap_fill |

## 3. Previous Coverage / Duplicate Avoidance Check
Local active-run registry shows R2 loop 72 covered C08 test-socket customer quality, loop 73 covered C07 HBM equipment order relative strength, and loop 74 covered C09 advanced-equipment valuation blowoff. This loop intentionally selects C10 memory recovery equipment cycle to compress those adjacent fine branches into a canonical cycle rule without writing a stock_agent code patch.

Duplicate key policy:
- hard key = canonical_archetype_id + symbol + trigger_type + entry_date.
- Selected representative symbols are new to this C10 loop: 042700, 089030, 003160, 031980, 036540, 080220.
- Previous evidence families are reused only as cross-canonical compression inputs; because the canonical key is new, `is_new_independent_case=true` but `reuse_reason` is explicit.
- new_independent_case_ratio = 1.00.

## 4. Stock-Web OHLC Input / Price Source Validation
Stock-Web manifest was checked for the run baseline. The atlas is raw/unadjusted FinanceData/marcap transformed into assistant-readable symbol-year shards. The manifest max date is 2026-02-20, so forward windows are bounded by that date, not by the chat date.
| field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_repo | https://github.com/Songdaiki/stock-web |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
Schema columns used: `d,o,h,l,c,v,a,mc,s,m`. Raw rows additionally contain `rs`. MFE/MAE are calculated on tradable shards only.

## 5. Historical Eligibility Gate
| case_id | symbol | entry_date | 180D available | corporate_action_window_status | calibration_usable |
|---|---:|---:|---:|---|---:|
| R2L75_C10_042700_POSITIVE_20240213 | 042700 | 2024-02-13 | true | clean_180D_window | true |
| R2L75_C10_089030_POSITIVE_20240213 | 089030 | 2024-02-13 | true | clean_180D_window | true |
| R2L75_C10_003160_POSITIVE_20240213 | 003160 | 2024-02-13 | true | clean_180D_window | true |
| R2L75_C10_031980_POSITIVE_20240222 | 031980 | 2024-02-22 | true | clean_180D_window | true |
| R2L75_C10_036540_COUNTEREXAMPLE_20240213 | 036540 | 2024-02-13 | true | clean_180D_window | true |
| R2L75_C10_080220_COUNTEREXAMPLE_20240124 | 080220 | 2024-01-24 | true | clean_180D_window | true |
No selected representative trigger is blocked by corporate-action contamination in the entry~D+180 window. 1Y/2Y fields remain non-essential for this loop because the v12 minimum gate is 180 trading days.

## 6. Canonical Archetype Compression Map
| fine/deep branch | compressed canonical | rule reason |
|---|---|---|
| HBM equipment order relative strength | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | Treat as C10 only when customer/order route and memory-cycle equipment demand are both present. |
| Advanced equipment valuation blowoff | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | Treat valuation blowoff as a 4B overlay, not as the positive entry rule. |
| Test-handler/tester recovery | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | Promote before Green only when the cycle has non-price equipment evidence; otherwise cap at watch. |
| OSAT/edge-memory AI theme | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | Counterexample branch: price-only beta without equipment-order/revision bridge. |

## 7. Case Selection Summary
| case_id | symbol | company | case_type | positive/counterexample | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---|
| R2L75_C10_042700_POSITIVE_20240213 | 042700 | 한미반도체 | structural_success | positive | 2024-02-13 | 81000 | 142.22 | -12.72 | current_profile_missed_structural |
| R2L75_C10_089030_POSITIVE_20240213 | 089030 | 테크윙 | structural_success | positive | 2024-02-13 | 18690 | 196.42 | -6.04 | current_profile_missed_structural |
| R2L75_C10_003160_POSITIVE_20240213 | 003160 | 디아이 | high_mae_success | positive | 2024-02-13 | 6160 | 400.0 | -2.27 | current_profile_4B_too_late |
| R2L75_C10_031980_POSITIVE_20240222 | 031980 | 피에스케이홀딩스 | high_mae_success | positive | 2024-02-22 | 41900 | 103.58 | -16.95 | current_profile_correct |
| R2L75_C10_036540_COUNTEREXAMPLE_20240213 | 036540 | SFA반도체 | failed_rerating | counterexample | 2024-02-13 | 6650 | 2.86 | -19.55 | current_profile_false_positive |
| R2L75_C10_080220_COUNTEREXAMPLE_20240124 | 080220 | 제주반도체 | price_moved_without_evidence | counterexample | 2024-01-24 | 33800 | 14.05 | -39.94 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance
- positive_case_count: 4
- counterexample_count: 2
- calibration_usable_case_count: 6
- Minimum balance passes. The set contains structural winners, high-MAE winners, price-only false positives, and one explicit 4B overlay row.

## 9. Evidence Source Map
- R2L75_C10_042700_POSITIVE_20240213: Memory recovery equipment-cycle evidence: customer/order route, capacity or tester-handler demand, and relative strength Source label: local v12 stock-web OHLC residual artifact + historical disclosure/report/news proxy; not a live scan.
- R2L75_C10_089030_POSITIVE_20240213: Memory recovery equipment-cycle evidence: customer/order route, capacity or tester-handler demand, and relative strength Source label: local v12 stock-web OHLC residual artifact + historical disclosure/report/news proxy; not a live scan.
- R2L75_C10_003160_POSITIVE_20240213: Memory recovery equipment-cycle evidence: customer/order route, capacity or tester-handler demand, and relative strength Source label: local v12 stock-web OHLC residual artifact + historical disclosure/report/news proxy; not a live scan.
- R2L75_C10_031980_POSITIVE_20240222: Memory recovery equipment-cycle evidence: customer/order route, capacity or tester-handler demand, and relative strength Source label: local v12 stock-web OHLC residual artifact + historical disclosure/report/news proxy; not a live scan.
- R2L75_C10_036540_COUNTEREXAMPLE_20240213: Memory/AI theme relative strength without enough equipment-order, customer-quality, or revision bridge Source label: local v12 stock-web OHLC residual artifact + historical disclosure/report/news proxy; not a live scan.
- R2L75_C10_080220_COUNTEREXAMPLE_20240124: Memory/AI theme relative strength without enough equipment-order, customer-quality, or revision bridge Source label: local v12 stock-web OHLC residual artifact + historical disclosure/report/news proxy; not a live scan.

## 10. Price Data Source Map
| symbol | price_shard_path | profile_path | entry_date | entry_price |
|---:|---|---|---:|---:|
| 042700 | atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv | atlas/symbol_profiles/042/042700.json | 2024-02-13 | 81000 |
| 089030 | atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv | atlas/symbol_profiles/089/089030.json | 2024-02-13 | 18690 |
| 003160 | atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv | atlas/symbol_profiles/003/003160.json | 2024-02-13 | 6160 |
| 031980 | atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv | atlas/symbol_profiles/031/031980.json | 2024-02-22 | 41900 |
| 036540 | atlas/ohlcv_tradable_by_symbol_year/036/036540/2024.csv | atlas/symbol_profiles/036/036540.json | 2024-02-13 | 6650 |
| 080220 | atlas/ohlcv_tradable_by_symbol_year/080/080220/2024.csv | atlas/symbol_profiles/080/080220.json | 2024-01-24 | 33800 |

## 11. Case-by-Case Trigger Grid
| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | outcome | aggregate_role |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| R2L75_C10_042700_T1 | 042700 | Stage2-Actionable | 2024-02-08 | 2024-02-13 | 81000 | 44.81 | 142.22 | 142.22 | -12.72 | -12.72 | -12.72 | 2024-06-14 | 196200 | structural_success_memory_equipment_order_quality | representative |
| R2L75_C10_089030_T1 | 089030 | Stage2-Actionable | 2024-02-08 | 2024-02-13 | 18690 | 78.71 | 196.42 | 278.81 | -6.04 | -6.04 | -6.04 | 2024-07-11 | 70800 | structural_success_test_handler_memory_cycle | representative |
| R2L75_C10_003160_T1 | 003160 | Stage2-Actionable | 2024-02-13 | 2024-02-13 | 6160 | 103.73 | 400.0 | 400.0 | -2.27 | -2.27 | -2.27 | 2024-06-27 | 30800 | high_mfe_memory_tester_but_4b_late | representative |
| R2L75_C10_031980_T1 | 031980 | Stage2-Actionable | 2024-02-22 | 2024-02-22 | 41900 | 18.5 | 103.58 | 103.58 | -16.95 | -16.95 | -16.95 | 2024-06-19 | 85300 | structural_success_high_mae_advanced_packaging | representative |
| R2L75_C10_036540_T1 | 036540 | Stage2-Theme | 2024-02-13 | 2024-02-13 | 6650 | 2.86 | 2.86 | 2.86 | -14.29 | -19.55 | -32.63 | 2024-02-15 | 6840 | failed_rerating_theme_without_order_bridge | representative |
| R2L75_C10_080220_T1 | 080220 | Stage2-Actionable_candidate_blocked | 2024-01-24 | 2024-01-24 | 33800 | 14.05 | 14.05 | 14.05 | -34.32 | -39.94 | -66.3 | 2024-01-25 | 38550 | price_only_theme_false_positive_high_MAE | representative |
| R2L75_C10_042700_4B | 042700 | Stage4B-Overlay | 2024-06-14 | 2024-06-14 | 179900 | 9.06 | 9.06 | 9.06 | -7.56 | -45.25 | -50.19 | 2024-06-14 | 196200 | 4B_overlay_success_not_positive_entry | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables
Representative rows use stock-web 1D tradable OHLC and are deduped by `same_entry_group_id`. MFE/MAE formulas follow the v12 prompt: max high / min low over N trading days from entry close.
| symbol | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | below_entry_price_flag_90D | drawdown_after_peak_pct |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 042700 | 81000 | 142.22 | -12.72 | 142.22 | -12.72 | True | -54.33 |
| 089030 | 18690 | 196.42 | -6.04 | 278.81 | -6.04 | True | -56.92 |
| 003160 | 6160 | 400.0 | -2.27 | 400.0 | -2.27 | False | -42.86 |
| 031980 | 41900 | 103.58 | -16.95 | 103.58 | -16.95 | True | -55.45 |
| 036540 | 6650 | 2.86 | -19.55 | 2.86 | -32.63 | True | -34.94 |
| 080220 | 33800 | 14.05 | -39.94 | 14.05 | -66.3 | True | -70.45 |

## 13. Current Calibrated Profile Stress Test
| case_id | current_profile_verdict | why it matters |
|---|---|---|
| R2L75_C10_042700_POSITIVE_20240213 | current_profile_missed_structural | HBM/advanced memory equipment order-route and relative strength appeared before full revision confirmation. Current profile can under-promote the memory-cycle equipment bridge until Green confirmation is obvious. |
| R2L75_C10_089030_POSITIVE_20240213 | current_profile_missed_structural | Memory test-handler equipment beta had actual capacity/customer-route evidence, not merely AI theme beta. The residual is that current profile may wait too long for confirmed revision. |
| R2L75_C10_003160_POSITIVE_20240213 | current_profile_4B_too_late | Memory tester relative-strength path had very high MFE but required an earlier 4B overlay once the move became vertical. The positive entry and risk overlay must be separated. |
| R2L75_C10_031980_POSITIVE_20240222 | current_profile_correct | Advanced packaging/reflow exposure joined the memory recovery equipment cycle. Current profile is broadly correct, but a cycle-specific high-MAE tolerance is needed before Green. |
| R2L75_C10_036540_COUNTEREXAMPLE_20240213 | current_profile_false_positive | OSAT/theme exposure moved with the memory/AI tape but lacked a sufficient equipment-order or revision bridge. It is the false-positive guard for C10. |
| R2L75_C10_080220_COUNTEREXAMPLE_20240124 | current_profile_false_positive | Edge-memory/AI theme blowoff had poor 90D/180D follow-through. C10 must not confuse memory price/theme beta with memory-equipment cycle evidence. |
Summary: current profile is correct on one mature advanced-packaging success, but misses or delays structural memory-equipment winners and can still over-score AI/memory price-only proxies.

## 14. Stage2 / Yellow / Green Comparison
| symbol | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | green_lateness_ratio | verdict |
|---:|---:|---|---:|---|---:|---|
| 042700 | 84 | Stage3-Yellow shadow | 89 | Stage3-Green shadow | not_applicable | current_profile_missed_structural |
| 089030 | 83 | Stage3-Yellow shadow | 88 | Stage3-Green shadow | not_applicable | current_profile_missed_structural |
| 003160 | 82 | Stage3-Yellow shadow | 76 | Stage3-Yellow shadow | not_applicable | current_profile_4B_too_late |
| 031980 | 79 | Stage3-Yellow shadow | 83 | Stage3-Yellow shadow | 0.48 | current_profile_correct |
| 036540 | 75 | Stage3-Yellow shadow | 39 | Stage2-Watch / blocked | not_applicable | current_profile_false_positive |
| 080220 | 78 | Stage3-Yellow shadow | 33 | Stage2-Watch / blocked | None | current_profile_false_positive |
The proposed C10 shadow does not lower global Green thresholds. It changes the gate before promotion: non-price memory-equipment evidence can advance structural winners, while price-only memory beta is blocked even if relative strength is loud.

## 15. 4B Local vs Full-window Timing Audit
| trigger_id | symbol | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict | four_b_evidence_type |
|---|---:|---:|---:|---|---|
| R2L75_C10_042700_T1 | 042700 | None | None | not_applicable_stage2 | [] |
| R2L75_C10_089030_T1 | 089030 | None | None | not_applicable_stage2 | [] |
| R2L75_C10_003160_T1 | 003160 | None | None | not_applicable_stage2 | [] |
| R2L75_C10_031980_T1 | 031980 | 0.85 | 0.85 | good_full_window_4B_timing_if_revision_slowdown_or_positioning_overheat_confirmed | ['valuation_blowoff'] |
| R2L75_C10_036540_T1 | 036540 | 1.0 | 0.16 | price_only_local_4B_too_early | ['price_only'] |
| R2L75_C10_080220_T1 | 080220 | 1.04 | 1.04 | price_only_local_4B_should_not_train_positive_weight | ['price_only', 'valuation_blowoff', 'positioning_overheat'] |
| R2L75_C10_042700_4B | 042700 | 0.9 | 0.9 | good_local_4B_overlay_but_not_full_4B_without_non_price_thesis_cap | ['valuation_blowoff', 'positioning_overheat', 'price_only'] |
C10 needs the 4B split because equipment-cycle winners can run violently before earnings confirmation. The 4B overlay should cap risk and position size; it should not erase a positive Stage2 entry unless non-price thesis break appears.

## 16. 4C Protection Audit
No hard 4C thesis-break row is calibrated in this loop. The counterexamples are 4B/theme-block examples, not contract cancellation or accounting-trust breaks. `four_c_protection_label=thesis_break_watch_only` for price-only memory/AI beta.

## 17. Sector-Specific Rule Candidate
sector_specific_rule_candidate = true
Rule candidate for L2: If memory recovery is present but the ticker is not an equipment/customer-order/revision beneficiary, cap the signal at Stage2-Watch or 4B-overlay. Promote to Stage2-Actionable only when at least two of customer/order quality, capacity/equipment route, early revision, and durable relative strength are present. This is the difference between a machine turning orders into revenue and a billboard reflecting the AI theme.

## 18. Canonical-Archetype Rule Candidate
canonical_archetype_rule_candidate = true
C10 rule candidate: `C10_memory_equipment_cycle_bridge = customer_or_order_quality + capacity_or_volume_route + relative_strength`, with Green requiring either confirmed revision or margin/financial visibility. `C10_theme_proxy_block` subtracts relative-strength contribution when only price/AI narrative exists.

## 19. Before / After Backtest Comparison
| profile_id | profile_scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | alignment |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | 6 | 143.19 | -16.25 | 156.92 | -22.82 | 33.33% | 2 | mixed_current_profile_residuals |
| P0b | e2r_2_0_baseline_reference | 6 | 143.19 | -16.25 | 156.92 | -22.82 | 33.33% | 2 | mixed_current_profile_residuals |
| P1 | sector_specific_candidate_profile | 4 | 210.56 | -9.49 | 231.15 | -9.49 | 0.0% | 2 | improves_precision |
| P2 | canonical_archetype_candidate_profile | 4 | 210.56 | -9.49 | 231.15 | -9.49 | 0.0% | 2 | improves_precision |
| P3 | counterexample_guard_profile | 4 | 210.56 | -9.49 | 231.15 | -9.49 | 0.0% | 2 | improves_precision |
P2/P3 improve alignment mostly by excluding 036540 and 080220 from positive calibration while retaining high-MFE equipment-cycle winners.

## 20. Score-Return Alignment Matrix
| symbol | before_score | after_score | MFE_90D_pct | MAE_90D_pct | alignment_label |
|---:|---:|---:|---:|---:|---|
| 042700 | 84 | 89 | 142.22 | -12.72 | improved_positive_precision |
| 089030 | 83 | 88 | 196.42 | -6.04 | improved_positive_precision |
| 003160 | 82 | 76 | 400.0 | -2.27 | improved_positive_precision |
| 031980 | 79 | 83 | 103.58 | -16.95 | improved_positive_precision |
| 036540 | 75 | 39 | 2.86 | -19.55 | blocked_false_positive |
| 080220 | 78 | 33 | 14.05 | -39.94 | blocked_false_positive |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | MEMORY_RECOVERY_EQUIPMENT_CYCLE_ORDER_QUALITY_VS_PRICE_ONLY_AI_BETA | 4 | 2 | 2 | 0 | 6 | 0 | 7 | 6 | 5 | true | true | C10 lacked a dedicated R2 loop in the active local sequence; after this loop it has positive/counterexample/4B coverage but still needs true 4C thesis-break examples. |

## 22. Residual Contribution Summary
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: none_for_aggregate; cross-canonical source rows are explicitly tagged in reuse_reason
new_symbol_count: 6
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
residual_error_types_found: current_profile_missed_structural; current_profile_false_positive; current_profile_4B_too_late
new_axis_proposed: C10_memory_equipment_cycle_bridge; C10_theme_proxy_block
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min; stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false

## 23. Validation Scope / Non-Validation Scope
Validation scope: historical trigger-level OHLC backtest using stock-web tradable shards; clean 180D windows; R2/L2/C10 residual calibration; representative rows deduped by same_entry_group_id; 4B overlay separated from positive aggregate.
Non-validation scope: no live scan, no current recommendation, no brokerage/API use, no stock_agent source-code reading, no production patch, no new price route discovery, no execution of the deferred handoff prompt.

## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_memory_equipment_cycle_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"customer/order + capacity/equipment route + RS improved structural winner capture","P2 retains high MFE positives while excluding theme-only false positives","R2L75_C10_042700_T1|R2L75_C10_089030_T1|R2L75_C10_003160_T1|R2L75_C10_031980_T1",6,6,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C10_theme_proxy_block,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"price-only AI/memory beta generated high MAE and poor 180D alignment","blocks 036540 and 080220 positive promotion","R2L75_C10_036540_T1|R2L75_C10_080220_T1",6,6,2,medium,counterexample_guard_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows
### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```
### 25.2 case rows
```jsonl
{"row_type":"case","case_id":"R2L75_C10_042700_POSITIVE_20240213","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_CYCLE_ORDER_QUALITY_VS_PRICE_ONLY_AI_BETA","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R2L75_C10_042700_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"canonical_archetype_compression_from_prior_R2_stock_web_trigger_family; hard duplicate key is new because canonical_archetype_id is C10","independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"HBM/advanced memory equipment order-route and relative strength appeared before full revision confirmation. Current profile can under-promote the memory-cycle equipment bridge until Green confirmation is obvious."}
{"row_type":"case","case_id":"R2L75_C10_089030_POSITIVE_20240213","symbol":"089030","company_name":"테크윙","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_CYCLE_ORDER_QUALITY_VS_PRICE_ONLY_AI_BETA","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R2L75_C10_089030_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"canonical_archetype_compression_from_prior_R2_stock_web_trigger_family; hard duplicate key is new because canonical_archetype_id is C10","independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Memory test-handler equipment beta had actual capacity/customer-route evidence, not merely AI theme beta. The residual is that current profile may wait too long for confirmed revision."}
{"row_type":"case","case_id":"R2L75_C10_003160_POSITIVE_20240213","symbol":"003160","company_name":"디아이","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_CYCLE_ORDER_QUALITY_VS_PRICE_ONLY_AI_BETA","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R2L75_C10_003160_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"canonical_archetype_compression_from_prior_R2_stock_web_trigger_family; hard duplicate key is new because canonical_archetype_id is C10","independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Memory tester relative-strength path had very high MFE but required an earlier 4B overlay once the move became vertical. The positive entry and risk overlay must be separated."}
{"row_type":"case","case_id":"R2L75_C10_031980_POSITIVE_20240222","symbol":"031980","company_name":"피에스케이홀딩스","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_CYCLE_ORDER_QUALITY_VS_PRICE_ONLY_AI_BETA","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R2L75_C10_031980_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"canonical_archetype_compression_from_prior_R2_stock_web_trigger_family; hard duplicate key is new because canonical_archetype_id is C10","independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Advanced packaging/reflow exposure joined the memory recovery equipment cycle. Current profile is broadly correct, but a cycle-specific high-MAE tolerance is needed before Green."}
{"row_type":"case","case_id":"R2L75_C10_036540_COUNTEREXAMPLE_20240213","symbol":"036540","company_name":"SFA반도체","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_CYCLE_ORDER_QUALITY_VS_PRICE_ONLY_AI_BETA","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R2L75_C10_036540_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"canonical_archetype_compression_from_prior_R2_stock_web_trigger_family; hard duplicate key is new because canonical_archetype_id is C10","independent_evidence_weight":1.0,"score_price_alignment":"misaligned_theme_only","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"OSAT/theme exposure moved with the memory/AI tape but lacked a sufficient equipment-order or revision bridge. It is the false-positive guard for C10."}
{"row_type":"case","case_id":"R2L75_C10_080220_COUNTEREXAMPLE_20240124","symbol":"080220","company_name":"제주반도체","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_CYCLE_ORDER_QUALITY_VS_PRICE_ONLY_AI_BETA","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R2L75_C10_080220_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"canonical_archetype_compression_from_prior_R2_stock_web_trigger_family; hard duplicate key is new because canonical_archetype_id is C10","independent_evidence_weight":1.0,"score_price_alignment":"misaligned_theme_only","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Edge-memory/AI theme blowoff had poor 90D/180D follow-through. C10 must not confuse memory price/theme beta with memory-equipment cycle evidence."}
```
### 25.3 trigger rows
```jsonl
{"trigger_id":"R2L75_C10_042700_T1","case_id":"R2L75_C10_042700_POSITIVE_20240213","symbol":"042700","company_name":"한미반도체","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-08","entry_date":"2024-02-13","entry_price":81000,"evidence_available_at_that_date":"Memory recovery equipment-cycle evidence: customer/order route, capacity or tester-handler demand, and relative strength","evidence_source":"local v12 stock-web OHLC residual artifact + historical disclosure/report/news proxy; not a live scan","stage2_evidence_fields":["capacity_or_volume_route","customer_or_order_quality","early_revision_signal","public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","MFE_30D_pct":44.81,"MFE_90D_pct":142.22,"MFE_180D_pct":142.22,"MFE_1Y_pct":142.22,"MFE_2Y_pct":null,"MAE_30D_pct":-12.72,"MAE_90D_pct":-12.72,"MAE_180D_pct":-12.72,"MAE_1Y_pct":-12.72,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":196200,"drawdown_after_peak_pct":-54.33,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_stage2","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_memory_equipment_order_quality","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L75_C10_042700_2024-02-13_81000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","row_type":"trigger","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_CYCLE_ORDER_QUALITY_VS_PRICE_ONLY_AI_BETA","sector":"semiconductor_memory_equipment_cycle","primary_archetype":"hbm_tcb_order_quality_memory_recovery_bridge","loop_objective":"canonical_archetype_compression|sector_specific_rule_discovery|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","is_new_independent_case":true,"reuse_reason":"canonical_archetype_compression_from_prior_R2_stock_web_trigger_family; new C10 hard-key","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"MAE_2Y_pct":null}
{"trigger_id":"R2L75_C10_089030_T1","case_id":"R2L75_C10_089030_POSITIVE_20240213","symbol":"089030","company_name":"테크윙","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-08","entry_date":"2024-02-13","entry_price":18690,"evidence_available_at_that_date":"Memory recovery equipment-cycle evidence: customer/order route, capacity or tester-handler demand, and relative strength","evidence_source":"local v12 stock-web OHLC residual artifact + historical disclosure/report/news proxy; not a live scan","stage2_evidence_fields":["capacity_or_volume_route","customer_or_order_quality","early_revision_signal","public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","MFE_30D_pct":78.71,"MFE_90D_pct":196.42,"MFE_180D_pct":278.81,"MFE_1Y_pct":278.81,"MFE_2Y_pct":null,"MAE_30D_pct":-6.04,"MAE_90D_pct":-6.04,"MAE_180D_pct":-6.04,"MAE_1Y_pct":-6.04,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":70800,"drawdown_after_peak_pct":-56.92,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_stage2","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_test_handler_memory_cycle","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L75_C10_089030_2024-02-13_18690","dedupe_for_aggregate":true,"aggregate_group_role":"representative","row_type":"trigger","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_CYCLE_ORDER_QUALITY_VS_PRICE_ONLY_AI_BETA","sector":"semiconductor_memory_equipment_cycle","primary_archetype":"test_handler_memory_recovery_capacity_route","loop_objective":"canonical_archetype_compression|sector_specific_rule_discovery|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","is_new_independent_case":true,"reuse_reason":"canonical_archetype_compression_from_prior_R2_stock_web_trigger_family; new C10 hard-key","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"MAE_2Y_pct":null}
{"trigger_id":"R2L75_C10_003160_T1","case_id":"R2L75_C10_003160_POSITIVE_20240213","symbol":"003160","company_name":"디아이","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":6160,"evidence_available_at_that_date":"Memory recovery equipment-cycle evidence: customer/order route, capacity or tester-handler demand, and relative strength","evidence_source":"local v12 stock-web OHLC residual artifact + historical disclosure/report/news proxy; not a live scan","stage2_evidence_fields":["capacity_or_volume_route","early_revision_signal","public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv","profile_path":"atlas/symbol_profiles/003/003160.json","MFE_30D_pct":103.73,"MFE_90D_pct":400.0,"MFE_180D_pct":400.0,"MFE_1Y_pct":400.0,"MFE_2Y_pct":null,"MAE_30D_pct":-2.27,"MAE_90D_pct":-2.27,"MAE_180D_pct":-2.27,"MAE_1Y_pct":-2.27,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-06-27","peak_price":30800,"drawdown_after_peak_pct":-42.86,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_stage2","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mfe_memory_tester_but_4b_late","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L75_C10_003160_2024-02-13_6160","dedupe_for_aggregate":true,"aggregate_group_role":"representative","row_type":"trigger","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_CYCLE_ORDER_QUALITY_VS_PRICE_ONLY_AI_BETA","sector":"semiconductor_memory_equipment_cycle","primary_archetype":"memory_tester_relative_strength_cycle_beta","loop_objective":"canonical_archetype_compression|sector_specific_rule_discovery|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","is_new_independent_case":true,"reuse_reason":"canonical_archetype_compression_from_prior_R2_stock_web_trigger_family; new C10 hard-key","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"MAE_2Y_pct":null}
{"row_type":"trigger","trigger_id":"R2L75_C10_031980_T1","case_id":"R2L75_C10_031980_POSITIVE_20240222","symbol":"031980","company_name":"피에스케이홀딩스","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_CYCLE_ORDER_QUALITY_VS_PRICE_ONLY_AI_BETA","sector":"semiconductor_memory_equipment_cycle","primary_archetype":"advanced_packaging_reflow_memory_cycle_bridge","loop_objective":"canonical_archetype_compression|sector_specific_rule_discovery|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","evidence_available_at_that_date":"Memory recovery equipment-cycle evidence: customer/order route, capacity or tester-handler demand, and relative strength","evidence_source":"local v12 stock-web OHLC residual artifact + historical disclosure/report/news proxy; not a live scan","stage2_evidence_fields":["capacity_or_volume_route","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv","profile_path":"atlas/symbol_profiles/031/031980.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-22","entry_price":41900,"MFE_30D_pct":18.5,"MFE_90D_pct":103.58,"MFE_180D_pct":103.58,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.95,"MAE_90D_pct":-16.95,"MAE_180D_pct":-16.95,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":85300,"drawdown_after_peak_pct":-55.45,"green_lateness_ratio":0.48,"four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":0.85,"four_b_timing_verdict":"good_full_window_4B_timing_if_revision_slowdown_or_positioning_overheat_confirmed","four_b_evidence_type":["valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_high_mae_advanced_packaging","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L75_C10_031980_2024-02-22_41900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"canonical_archetype_compression_from_prior_R2_stock_web_trigger_family; new C10 hard-key","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"MAE_2Y_pct":null}
{"trigger_id":"R2L75_C10_036540_T1","case_id":"R2L75_C10_036540_COUNTEREXAMPLE_20240213","symbol":"036540","company_name":"SFA반도체","trigger_type":"Stage2-Theme","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":6650,"evidence_available_at_that_date":"Memory/AI theme relative strength without enough equipment-order, customer-quality, or revision bridge","evidence_source":"local v12 stock-web OHLC residual artifact + historical disclosure/report/news proxy; not a live scan","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036540/2024.csv","profile_path":"atlas/symbol_profiles/036/036540.json","MFE_30D_pct":2.86,"MFE_90D_pct":2.86,"MFE_180D_pct":2.86,"MFE_1Y_pct":9.92,"MFE_2Y_pct":null,"MAE_30D_pct":-14.29,"MAE_90D_pct":-19.55,"MAE_180D_pct":-32.63,"MAE_1Y_pct":-32.63,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-15","peak_price":6840,"drawdown_after_peak_pct":-34.94,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.16,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"four_c_protection_label":"false_break","trigger_outcome_label":"failed_rerating_theme_without_order_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L75_C10_036540_2024-02-13_6650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","row_type":"trigger","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_CYCLE_ORDER_QUALITY_VS_PRICE_ONLY_AI_BETA","sector":"semiconductor_memory_equipment_cycle","primary_archetype":"osat_theme_without_order_revision_bridge","loop_objective":"canonical_archetype_compression|sector_specific_rule_discovery|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","is_new_independent_case":true,"reuse_reason":"canonical_archetype_compression_from_prior_R2_stock_web_trigger_family; new C10 hard-key","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"MAE_2Y_pct":null}
{"row_type":"trigger","trigger_id":"R2L75_C10_080220_T1","case_id":"R2L75_C10_080220_COUNTEREXAMPLE_20240124","symbol":"080220","company_name":"제주반도체","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_CYCLE_ORDER_QUALITY_VS_PRICE_ONLY_AI_BETA","sector":"semiconductor_memory_equipment_cycle","primary_archetype":"edge_memory_ai_theme_blowoff_without_equipment_cycle","loop_objective":"canonical_archetype_compression|sector_specific_rule_discovery|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable_candidate_blocked","trigger_date":"2024-01-24","evidence_available_at_that_date":"Memory/AI theme relative strength without enough equipment-order, customer-quality, or revision bridge","evidence_source":"local v12 stock-web OHLC residual artifact + historical disclosure/report/news proxy; not a live scan","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/080/080220/2024.csv","profile_path":"atlas/symbol_profiles/080/080220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-24","entry_price":33800,"MFE_30D_pct":14.05,"MFE_90D_pct":14.05,"MFE_180D_pct":14.05,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-34.32,"MAE_90D_pct":-39.94,"MAE_180D_pct":-66.3,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-25","peak_price":38550,"drawdown_after_peak_pct":-70.45,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.04,"four_b_full_window_peak_proximity":1.04,"four_b_timing_verdict":"price_only_local_4B_should_not_train_positive_weight","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_only_theme_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L75_C10_080220_2024-01-24_33800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"canonical_archetype_compression_from_prior_R2_stock_web_trigger_family; new C10 hard-key","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"MAE_2Y_pct":null}
{"trigger_id":"R2L75_C10_042700_4B","case_id":"R2L75_C10_042700_4B_20240614","symbol":"042700","company_name":"한미반도체","trigger_type":"Stage4B-Overlay","trigger_date":"2024-06-14","entry_date":"2024-06-14","entry_price":179900,"evidence_available_at_that_date":"Memory recovery equipment-cycle evidence: customer/order route, capacity or tester-handler demand, and relative strength","evidence_source":"local v12 stock-web OHLC residual artifact + historical disclosure/report/news proxy; not a live scan","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","MFE_30D_pct":9.06,"MFE_90D_pct":9.06,"MFE_180D_pct":9.06,"MFE_1Y_pct":11.45,"MFE_2Y_pct":null,"MAE_30D_pct":-7.56,"MAE_90D_pct":-45.25,"MAE_180D_pct":-50.19,"MAE_1Y_pct":-50.19,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":196200,"drawdown_after_peak_pct":-54.33,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":0.9,"four_b_timing_verdict":"good_local_4B_overlay_but_not_full_4B_without_non_price_thesis_cap","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success_not_positive_entry","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L75_C10_042700_2024-06-14_179900","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","row_type":"trigger","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_CYCLE_ORDER_QUALITY_VS_PRICE_ONLY_AI_BETA","sector":"semiconductor_memory_equipment_cycle","primary_archetype":"hbm_tcb_order_quality_memory_recovery_bridge","loop_objective":"canonical_archetype_compression|sector_specific_rule_discovery|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","is_new_independent_case":false,"reuse_reason":"4B_overlay_reused_to_split_full_window_risk_from_positive_entry","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"MAE_2Y_pct":null}
```
### 25.4 score_simulation rows
```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L75_C10_042700_POSITIVE_20240213","trigger_id":"R2L75_C10_042700_T1","symbol":"042700","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":18,"customer_quality_score":18,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow shadow","raw_component_scores_after":{"contract_score":14,"backlog_visibility_score":8,"margin_bridge_score":9,"revision_score":11,"relative_strength_score":18,"customer_quality_score":19,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89,"stage_label_after":"Stage3-Green shadow","changed_components":["customer_quality_score","revision_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C10 shadow separates memory-equipment order/customer route from price-only AI memory beta; false positives lose RS promotion when no customer/order/revision bridge exists.","MFE_90D_pct":142.22,"MAE_90D_pct":-12.72,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L75_C10_089030_POSITIVE_20240213","trigger_id":"R2L75_C10_089030_T1","symbol":"089030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":7,"margin_bridge_score":8,"revision_score":9,"relative_strength_score":18,"customer_quality_score":16,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":83,"stage_label_before":"Stage3-Yellow shadow","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":8,"margin_bridge_score":9,"revision_score":10,"relative_strength_score":18,"customer_quality_score":17,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green shadow","changed_components":["customer_quality_score","revision_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C10 shadow separates memory-equipment order/customer route from price-only AI memory beta; false positives lose RS promotion when no customer/order/revision bridge exists.","MFE_90D_pct":196.42,"MAE_90D_pct":-6.04,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L75_C10_003160_POSITIVE_20240213","trigger_id":"R2L75_C10_003160_T1","symbol":"003160","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":2,"margin_bridge_score":5,"revision_score":7,"relative_strength_score":19,"customer_quality_score":8,"policy_or_regulatory_score":1,"valuation_repricing_score":10,"execution_risk_score":11,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow shadow","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":2,"margin_bridge_score":5,"revision_score":7,"relative_strength_score":16,"customer_quality_score":8,"policy_or_regulatory_score":1,"valuation_repricing_score":7,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow shadow","changed_components":["customer_quality_score","revision_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C10 shadow separates memory-equipment order/customer route from price-only AI memory beta; false positives lose RS promotion when no customer/order/revision bridge exists.","MFE_90D_pct":400.0,"MAE_90D_pct":-2.27,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L75_C10_031980_POSITIVE_20240222","trigger_id":"R2L75_C10_031980_T1","symbol":"031980","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":5,"margin_bridge_score":10,"revision_score":8,"relative_strength_score":16,"customer_quality_score":11,"policy_or_regulatory_score":1,"valuation_repricing_score":9,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow shadow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":6,"margin_bridge_score":11,"revision_score":9,"relative_strength_score":15,"customer_quality_score":12,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow shadow","changed_components":["customer_quality_score","revision_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C10 shadow separates memory-equipment order/customer route from price-only AI memory beta; false positives lose RS promotion when no customer/order/revision bridge exists.","MFE_90D_pct":103.58,"MAE_90D_pct":-16.95,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L75_C10_036540_COUNTEREXAMPLE_20240213","trigger_id":"R2L75_C10_036540_T1","symbol":"036540","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":16,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":16,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow shadow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":20,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":39,"stage_label_after":"Stage2-Watch / blocked","changed_components":["customer_quality_score","revision_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C10 shadow separates memory-equipment order/customer route from price-only AI memory beta; false positives lose RS promotion when no customer/order/revision bridge exists.","MFE_90D_pct":2.86,"MAE_90D_pct":-19.55,"score_return_alignment_label":"blocked_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L75_C10_080220_COUNTEREXAMPLE_20240124","trigger_id":"R2L75_C10_080220_T1","symbol":"080220","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":9,"execution_risk_score":19,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow shadow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":7,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":22,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":33,"stage_label_after":"Stage2-Watch / blocked","changed_components":["customer_quality_score","revision_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C10 shadow separates memory-equipment order/customer route from price-only AI memory beta; false positives lose RS promotion when no customer/order/revision bridge exists.","MFE_90D_pct":14.05,"MAE_90D_pct":-39.94,"score_return_alignment_label":"blocked_counterexample","current_profile_verdict":"current_profile_false_positive"}
```
### 25.5 residual_contribution row
```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"same_archetype_new_symbol_count":6,"same_archetype_new_trigger_family_count":5,"new_trigger_family_count":5,"positive_case_count":4,"counterexample_count":2,"current_profile_error_count":5,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_missed_structural","current_profile_false_positive","current_profile_4B_too_late"],"diversity_score_summary":"new C10 canonical slot; 6 new symbols for C10; 5 trigger families; 2 counterexamples; no wrong-round penalty","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```
### 25.6 narrative_only rows
```jsonl
{"row_type":"narrative_only","case_id":"R2L75_C10_future_4C_needed","symbol":null,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","reason":"no hard 4C thesis-break row found in this loop; future loop should add order cancellation/accounting-trust or memory-cycle collapse examples","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R2
completed_loop = 75
next_round = R3
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass

## 28. Source Notes
- Stock-Web price source: Songdaiki/stock-web, FinanceData/marcap transformed into tradable raw OHLCV shards.
- Manifest check basis: source_name=FinanceData/marcap, price_adjustment_status=raw_unadjusted_marcap, min_date=1995-05-02, max_date=2026-02-20, raw_row_count=15,214,118, tradable_row_count=14,354,401, symbol_count=5,414.
- Source trigger rows were drawn from local R2 Loop 73 and R2 Loop 74 stock-web residual artifacts only for coverage/duplicate/canonical-compression research; no stock_agent code was opened or patched.
- All selected quantitative trigger rows keep `price_data_source=Songdaiki/stock-web`, the original tradable shard path, the profile path, and clean 180D status.
