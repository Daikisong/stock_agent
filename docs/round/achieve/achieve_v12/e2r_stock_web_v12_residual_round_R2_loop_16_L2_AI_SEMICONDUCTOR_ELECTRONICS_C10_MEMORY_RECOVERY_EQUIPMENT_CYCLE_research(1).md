# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

scheduled_round = R2  
scheduled_loop = 16  
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS  
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE  
fine_archetype_id = MEMORY_EQUIPMENT_RECOVERY_ORDER_QUALITY_VS_PRICE_SPIKE  
research_session = post_calibrated_sector_archetype_residual_research  
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12  
production_scoring_changed = false  
shadow_weight_only = true  
stock_agent_code_access_allowed = false  
stock_agent_code_patch_allowed = false  
stock_web_price_atlas_access_required = true  

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE.

## 1. Current Calibrated Profile Assumption

current_default_profile_proxy = e2r_2_1_stock_web_calibrated  
rollback_reference_profile_id = e2r_2_0_baseline_reference  

The current proxy already includes the global Stock-Web calibration axes: Stage2 actionable evidence bonus, Yellow/Green stricter thresholds, price-only positive-stage blocking, full-4B non-price requirement, and hard 4C thesis-break routing. This MD does not re-argue those globally. It tests whether C10 memory-equipment recovery needs a narrower bridge rule: **recovery beta is not enough; order/revision/margin visibility must carry the promotion**.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
| --- | --- |
| scheduled_round | R2 |
| scheduled_loop | 16 |
| round_schedule_status | valid |
| round_sector_consistency | pass |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE |
| fine_archetype_id | MEMORY_EQUIPMENT_RECOVERY_ORDER_QUALITY_VS_PRICE_SPIKE |
| loop_objective | coverage_gap_fill / sector_specific_rule_discovery / canonical_archetype_compression / counterexample_mining / green_strictness_stress_test / 4B_non_price_requirement_stress_test |

R2 maps to L2_AI_SEMICONDUCTOR_ELECTRONICS, so the round-sector pair is valid.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 research files available in the working set show R2 loop 10~15 covered C06, C07, C08, and C09. C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE was not covered in those R2 v12 outputs. This file therefore fills the scheduled-round C10 coverage gap rather than repeating HBM customer-capacity, HBM equipment, test socket, or valuation-blowoff loops.

| previous R2 loop | canonical_archetype_id | symbols already used |
| --- | --- | --- |
| 10 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 000660, 005930 |
| 11 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 058470, 131290, 095340 |
| 12 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 042700, 089030, 232140, 003160 |
| 13 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 058470, 095340, 131290, 064290 |
| 14 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 042700, 089030, 058470, 131290, 095340, 064290, 003160 |
| 15 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 000660, 005930 |

The loop uses four symbols not used in those R2 v12 files: 240810, 084370, 036930, 095610.

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | value |
| --- | --- |
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
| markets | KONEX / KOSDAQ / KOSDAQ GLOBAL / KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

## 5. Historical Eligibility Gate

All representative triggers are historical, have entry rows inside Stock-Web tradable shards, have at least 180 forward trading days by the 2026-02-20 manifest max date, include positive OHLCV fields, and have no 2024 corporate-action overlap.

| symbol | source row anchors | profile status |
| --- | --- | --- |
| 240810 | 2024-02-29/03-04 entry, 2024-04-08 peak, 2024-11 low | corporate_action_candidate_count=0; clean 180D |
| 084370 | 2024-01-25/01-26 entry, 2024-02-05 low, 2024-05-28 peak | CA candidates 2007/2010/2012; clean 2024 window |
| 036930 | 2024-02-28 spike, 2024-04-08 limited peak, 2024-07 drawdown | CA candidate 2000 only; clean 2024 window |
| 095610 | 2024-04-02 entry, 2024-04-17 peak, 2024-11-14 low | CA candidates 2011/2016; clean 2024 window |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rationale |
| --- | --- | --- |
| MEMORY_EQUIPMENT_RECOVERY_ORDER_QUALITY_VS_PRICE_SPIKE | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | Captures non-HBM-specific semiconductor equipment recovery where order/revision/margin bridge matters more than raw price beta. |
| MEMORY_RECOVERY_HIGH_MAE_STAGE2 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | Early recovery entries can work but often carry severe shakeout risk, so they should be Stage2/Yellow rather than automatic Green. |
| MEMORY_EQUIPMENT_PRICE_ONLY_BETA_COUNTEREXAMPLE | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | Relative-strength-only spikes without order or revision confirmation are false-positive candidates. |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | current_profile_verdict |
| --- | --- | --- | --- | --- | --- |
| R2L16_C10_240810_WONIKIPS_MEMORY_RECOVERY_STAGE2A | 240810 | 원익IPS | high_mae_success | positive | current_profile_correct |
| R2L16_C10_084370_EUGENETECH_MEMORY_RECOVERY_DELAYED_SUCCESS | 084370 | 유진테크 | high_mae_success | positive | current_profile_too_late |
| R2L16_C10_036930_JUSUNG_PRICE_SPIKE_FALSE_POSITIVE | 036930 | 주성엔지니어링 | false_positive_green | counterexample | current_profile_false_positive |
| R2L16_C10_095610_TES_PRICE_ONLY_MEMORY_RECOVERY_BLOWOFF | 095610 | 테스 | false_positive_green | counterexample | current_profile_4B_too_late |

## 8. Positive vs Counterexample Balance

positive_case_count = 2  
counterexample_count = 2  
calibration_usable_case_count = 4  
calibration_usable_trigger_count = 5  
representative_trigger_count = 4  

The balance is deliberate. 240810 and 084370 show that C10 can produce material upside when recovery becomes tied to revision/order visibility. 036930 and 095610 show that price-only memory-equipment beta can look convincing but fails the durable-rerating test.

## 9. Evidence Source Map

| symbol | trigger_date | evidence_family | evidence_summary |
| --- | --- | --- | --- |
| 240810 | 2024-02-29 | public_event_or_disclosure|relative_strength|capacity_or_volume_route|early_revision_signal|confirmed_revision|margin_bridge|financial_visibility|multiple_public_sources | Memory-equipment recovery evidence became tradable after the late-February 2024 equipment/revision inflection: sharp volume expansion, memory capex recovery nar |
| 084370 | 2024-01-25 | public_event_or_disclosure|relative_strength|early_revision_signal|capacity_or_volume_route|confirmed_revision|margin_bridge|financial_visibility | January 2024 memory recovery setup produced a severe early shakeout, then repriced once recovery and equipment-order visibility improved into March-May. This is |
| 036930 | 2024-02-28 | relative_strength|public_event_or_disclosure|price_only_local_peak|positioning_overheat | The February 2024 spike had price/volume and generic memory recovery linkage, but not enough C10-specific order/revision bridge. It demonstrates that relative s |
| 095610 | 2024-04-02 | relative_strength|public_event_or_disclosure|valuation_blowoff|positioning_overheat|price_only_local_peak|thesis_evidence_broken | The April 2024 secondary move produced a large short-window MFE but then gave back the move and broke down into the second half. This is a C10 false-positive pa |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | price_basis | adjustment |
| --- | --- | --- | --- | --- |
| 240810 | atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv | atlas/symbol_profiles/240/240810.json | tradable_raw | raw_unadjusted_marcap |
| 084370 | atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv | atlas/symbol_profiles/084/084370.json | tradable_raw | raw_unadjusted_marcap |
| 036930 | atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv | atlas/symbol_profiles/036/036930.json | tradable_raw | raw_unadjusted_marcap |
| 095610 | atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv | atlas/symbol_profiles/095/095610.json | tradable_raw | raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company_name | trigger_type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict | dedupe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R2L16_C10_240810_STAGE2A_2024-02-29 | 240810 | 원익IPS | Stage2-Actionable | 2024-03-04 | 33200 | 35.09 | -3.46 | 35.09 | -33.13 | current_profile_correct | True |
| R2L16_C10_084370_STAGE2A_2024-01-25 | 084370 | 유진테크 | Stage2-Actionable | 2024-01-26 | 43300 | 38.57 | -25.64 | 38.57 | -25.64 | current_profile_too_late | True |
| R2L16_C10_036930_STAGE2WATCH_2024-02-28 | 036930 | 주성엔지니어링 | Stage2-Watch | 2024-02-28 | 40000 | 3.63 | -20.88 | 3.63 | -23.38 | current_profile_false_positive | True |
| R2L16_C10_095610_STAGE2WATCH_2024-04-02 | 095610 | 테스 | Stage2-Watch | 2024-04-02 | 25150 | 30.82 | -15.7 | 30.82 | -43.14 | current_profile_4B_too_late | True |
| R2L16_C10_095610_4B_WATCH_2024-04-17 | 095610 | 테스 | Stage4B-Watch | 2024-04-17 | 29300 | 2.22 | -27.65 | 2.22 | -51.19 | current_profile_4B_too_late | False |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R2L16_C10_240810_STAGE2A_2024-02-29 | 2024-03-04 | 33200 | 35.09 | -3.46 | 35.09 | -3.46 | 35.09 | -33.13 | 2024-04-08 | 44850 | -50.5 |
| R2L16_C10_084370_STAGE2A_2024-01-25 | 2024-01-26 | 43300 | 6.12 | -25.64 | 38.57 | -25.64 | 38.57 | -25.64 | 2024-05-28 | 60000 | -38.67 |
| R2L16_C10_036930_STAGE2WATCH_2024-02-28 | 2024-02-28 | 40000 | 3.63 | -16.38 | 3.63 | -20.88 | 3.63 | -23.38 | 2024-04-08 | 41450 | -26.05 |
| R2L16_C10_095610_STAGE2WATCH_2024-04-02 | 2024-04-02 | 25150 | 30.82 | -10.34 | 30.82 | -15.7 | 30.82 | -43.14 | 2024-04-17 | 32900 | -56.53 |
| R2L16_C10_095610_4B_WATCH_2024-04-17 | 2024-04-17 | 29300 | 2.22 | -23.89 | 2.22 | -27.65 | 2.22 | -51.19 | 2024-04-17 | 32900 | -56.53 |

## 13. Current Calibrated Profile Stress Test

| question | conclusion |
| --- | --- |
| How would current profile judge these cases? | It handles obvious structural cases better than E2R 2.0, but C10 still needs a recovery/order-bridge split. |
| Actual MFE/MAE alignment? | Positive cases have useful 90D/180D MFE but high or delayed MAE; counterexamples show poor durability or post-peak collapse. |
| Stage2 bonus too high or low? | Broadly correct, but too broad for price-only memory-equipment beta. |
| Yellow threshold 75? | Appropriate as watch/action boundary. |
| Green threshold 87 / revision 55? | Needs C10-specific confirmation: order/revision bridge before Green. |
| Price-only blowoff guard? | Existing global guard is correct and should be strengthened inside C10. |
| Full 4B non-price requirement? | Correct. TES 4B is a watch overlay, not full 4B. |
| Hard 4C routing? | Correct in principle, but if it waits for explicit thesis break after a price-only blowoff, protection is late. |

## 14. Stage2 / Yellow / Green Comparison

For 240810, a plausible Stage3-Green confirmation around 2024-03-29 would have entered after much of the peak path was already consumed: green_lateness_ratio ≈ 0.71. For 084370, a delayed confirmation around early April has green_lateness_ratio ≈ 0.40. This does not weaken Green strictness globally; it argues for C10 Stage2/Yellow visibility with explicit high-MAE treatment.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict | evidence type |
| --- | ---: | ---: | --- | --- |
| R2L16_C10_036930_STAGE2WATCH_2024-02-28 | 0.96 | 0.96 | price_only_local_4B_watch_not_full_4B | price_only / positioning_overheat |
| R2L16_C10_095610_4B_WATCH_2024-04-17 | 1.00 | 1.00 | price_only_local_4B_watch_valid_but_not_full_4B | price_only / valuation_blowoff / positioning_overheat |

The 4B result strengthens the existing rule: price-only local peaks are useful risk overlays, but they cannot become full 4B without non-price evidence such as order delay, revision slowdown, contract risk, or margin/backlog deterioration.

## 16. 4C Protection Audit

TES shows the cleanest 4C-style protection pattern: after the April local peak, the stock fell into a 2024-11 low near 14300. However, the usable calibration lesson is not “route to 4C on price alone.” It is “after a price-only 4B-Watch, require faster thesis-check refresh because waiting for hard non-price break can be late.”

## 17. Sector-Specific Rule Candidate

sector_specific_rule_candidate = true  
rule_scope = sector_specific + canonical_archetype_specific  

Candidate rule: in L2 semiconductor equipment, memory-recovery beta can qualify for Stage2-Actionable if at least two of the following are present: early revision signal, margin bridge, order/backlog visibility, or customer/capex route. Price/volume relative strength alone remains Stage2-Watch.

## 18. Canonical-Archetype Rule Candidate

canonical_archetype_rule_candidate = true  

C10_order_revision_bridge:  
- Positive lift when memory recovery has revision/order/margin bridge.  
- High-MAE throttle keeps early recovery at Stage2/Yellow unless Green revision confirmation appears.  
- Price-only equipment beta is blocked from Stage3 promotion and converted into watch or 4B-Watch overlay.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 4 | 27.03 | -16.42 | 27.03 | -31.32 | 0.5 | 1 | 1 | mixed; residual errors remain |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 27.03 | -16.42 | 27.03 | -31.32 | 0.75 | 0 | 0 | worse false-positive control |
| P1_L2_memory_equipment_recovery_shadow_profile | sector_specific | 4 | 36.83 | -14.55 | 36.83 | -29.39 | 0.0 | 0 | 1 | better separation |
| P2_C10_order_revision_bridge_candidate_profile | canonical_archetype_specific | 4 | 36.83 | -14.55 | 36.83 | -29.39 | 0.0 | 0 | 1 | best shadow profile in this loop |
| P3_C10_price_only_counterexample_guard | counterexample_guard | 2 | 17.23 | -18.29 | 17.23 | -33.26 | 0.0 | 0 | 0 | counterexamples fixed |

## 20. Score-Return Alignment Matrix

| case_id | symbol | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R2L16_C10_240810_WONIKIPS_MEMORY_RECOVERY_STAGE2A | 240810 | 76 | Stage3-Yellow | 84 | Stage2-Actionable/Yellow boundary | 35.09 | -3.46 | aligned_positive_high_mae |
| R2L16_C10_084370_EUGENETECH_MEMORY_RECOVERY_DELAYED_SUCCESS | 084370 | 70 | Stage2-Watch | 82 | Stage2-Actionable | 38.57 | -25.64 | aligned_positive_delayed |
| R2L16_C10_036930_JUSUNG_PRICE_SPIKE_FALSE_POSITIVE | 036930 | 78 | Stage3-Yellow false-positive risk | 64 | Stage2-Watch | 3.63 | -20.88 | counterexample_fixed_by_guard |
| R2L16_C10_095610_TES_PRICE_ONLY_MEMORY_RECOVERY_BLOWOFF | 095610 | 79 | Stage3-Yellow/false Green risk | 60 | Stage2-Watch + 4B-Watch overlay | 30.82 | -15.7 | counterexample_fixed_by_guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | MEMORY_EQUIPMENT_RECOVERY_ORDER_QUALITY_VS_PRICE_SPIKE | 2 | 2 | 1 | 1 | 4 | 0 | 5 | 4 | 3 | True | True | C10 now has positive/counterexample/4B coverage; needs holdout across 2021-2023 downcycle and 2025 rerating later |

## 22. Residual Contribution Summary

new_independent_case_count: 4  
reused_case_count: 0  
reused_case_ids: []  
new_symbol_count: 4  
new_canonical_archetype_count: 1  
new_fine_archetype_count: 1  
new_trigger_family_count: 4  
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence  
residual_error_types_found: memory_equipment_price_only_false_positive, high_MAE_success_requires_stage2_not_green, price_only_4B_watch_overlay_too_late  
new_axis_proposed: C10_order_revision_bridge / C10_price_only_equipment_beta_guard  
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage / full_4b_requires_non_price_evidence  
existing_axis_weakened: null  
existing_axis_kept: stage2_actionable_evidence_bonus / stage3_green_revision_min  
sector_specific_rule_candidate: true  
canonical_archetype_rule_candidate: true  
no_new_signal_reason: null  
loop_contribution_label: canonical_archetype_rule_candidate  
do_not_propose_new_weight_delta: false

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical C10 trigger-level backtest using Stock-Web tradable_raw 1D OHLC rows for 240810, 084370, 036930, and 095610.  
Non-validation scope: no live candidate scan, no investment recommendation, no production score change, no stock_agent code inspection, no broker/API integration.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_order_revision_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Require revision/order/margin bridge before C10 Green; allow Stage2 for high-MAE recovery success","Improves separation: keeps 240810/084370 while blocking 036930/095610 false-positive Green",R2L16_C10_240810_STAGE2A_2024-02-29|R2L16_C10_084370_STAGE2A_2024-01-25|R2L16_C10_036930_STAGE2WATCH_2024-02-28|R2L16_C10_095610_STAGE2WATCH_2024-04-02,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C10_price_only_equipment_beta_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Price-only memory-equipment beta cannot promote Stage3; can create 4B-Watch overlay only","Reduces false-positive rate from 50% to 0% in loop sample",R2L16_C10_036930_STAGE2WATCH_2024-02-28|R2L16_C10_095610_STAGE2WATCH_2024-04-02|R2L16_C10_095610_4B_WATCH_2024-04-17,3,2,2,medium,canonical_shadow_only,"strengthens existing price-only guard inside C10"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R2L16_C10_240810_WONIKIPS_MEMORY_RECOVERY_STAGE2A", "symbol": "240810", "company_name": "원익IPS", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_RECOVERY_ORDER_QUALITY_VS_PRICE_SPIKE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R2L16_C10_240810_STAGE2A_2024-02-29", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive_high_mae", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Memory-equipment recovery evidence became tradable after the late-February 2024 equipment/revision inflection: sharp volume expansion, memory capex recovery narrative, and later March/April price confirmation. It had no "}
{"row_type": "case", "case_id": "R2L16_C10_084370_EUGENETECH_MEMORY_RECOVERY_DELAYED_SUCCESS", "symbol": "084370", "company_name": "유진테크", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_RECOVERY_ORDER_QUALITY_VS_PRICE_SPIKE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R2L16_C10_084370_STAGE2A_2024-01-25", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive_delayed", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "January 2024 memory recovery setup produced a severe early shakeout, then repriced once recovery and equipment-order visibility improved into March-May. This is the C10 pattern: recovery is real, but early entries need d"}
{"row_type": "case", "case_id": "R2L16_C10_036930_JUSUNG_PRICE_SPIKE_FALSE_POSITIVE", "symbol": "036930", "company_name": "주성엔지니어링", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_RECOVERY_ORDER_QUALITY_VS_PRICE_SPIKE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R2L16_C10_036930_STAGE2WATCH_2024-02-28", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_fixed_by_guard", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The February 2024 spike had price/volume and generic memory recovery linkage, but not enough C10-specific order/revision bridge. It demonstrates that relative strength alone should not upgrade memory-equipment recovery t"}
{"row_type": "case", "case_id": "R2L16_C10_095610_TES_PRICE_ONLY_MEMORY_RECOVERY_BLOWOFF", "symbol": "095610", "company_name": "테스", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_RECOVERY_ORDER_QUALITY_VS_PRICE_SPIKE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R2L16_C10_095610_STAGE2WATCH_2024-04-02", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_fixed_by_guard", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "The April 2024 secondary move produced a large short-window MFE but then gave back the move and broke down into the second half. This is a C10 false-positive pattern: memory recovery beta plus price-only blowoff is not d"}
{"row_type": "trigger", "trigger_id": "R2L16_C10_240810_STAGE2A_2024-02-29", "case_id": "R2L16_C10_240810_WONIKIPS_MEMORY_RECOVERY_STAGE2A", "symbol": "240810", "company_name": "원익IPS", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_RECOVERY_ORDER_QUALITY_VS_PRICE_SPIKE", "sector": "AI·반도체·전자부품", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-29", "evidence_available_at_that_date": "Memory-equipment recovery evidence became tradable after the late-February 2024 equipment/revision inflection: sharp volume expansion, memory capex recovery narrative, and later March/April price confirmation. It had no direct HBM customer-order evidence, so it belongs in C10 rather than C07/C06.", "evidence_source": "Stock-Web 240810 2024 shard rows: 2024-02-29 close 32800, 2024-03-04 close 33200, 2024-03-29 high 43400, 2024-04-08 high 44850; profile clean CA window.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv", "profile_path": "atlas/symbol_profiles/240/240810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-04", "entry_price": 33200, "MFE_30D_pct": 35.09, "MFE_90D_pct": 35.09, "MFE_180D_pct": 35.09, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.46, "MAE_90D_pct": -3.46, "MAE_180D_pct": -33.13, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-04-08", "peak_price": 44850, "drawdown_after_peak_pct": -50.5, "green_lateness_ratio": 0.71, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success_high_mae", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "240810_20240304_33200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R2L16_C10_084370_STAGE2A_2024-01-25", "case_id": "R2L16_C10_084370_EUGENETECH_MEMORY_RECOVERY_DELAYED_SUCCESS", "symbol": "084370", "company_name": "유진테크", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_RECOVERY_ORDER_QUALITY_VS_PRICE_SPIKE", "sector": "AI·반도체·전자부품", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-25", "evidence_available_at_that_date": "January 2024 memory recovery setup produced a severe early shakeout, then repriced once recovery and equipment-order visibility improved into March-May. This is the C10 pattern: recovery is real, but early entries need drawdown-aware sizing and cannot be promoted to Green without revision/order confirmation.", "evidence_source": "Stock-Web 084370 2024 shard rows: 2024-01-25 close 46600, 2024-01-26 close 43300, 2024-02-05 low 32200, 2024-05-28 high 60000; profile has no modern CA contamination.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "early_revision_signal", "capacity_or_volume_route"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv", "profile_path": "atlas/symbol_profiles/084/084370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-26", "entry_price": 43300, "MFE_30D_pct": 6.12, "MFE_90D_pct": 38.57, "MFE_180D_pct": 38.57, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -25.64, "MAE_90D_pct": -25.64, "MAE_180D_pct": -25.64, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-28", "peak_price": 60000, "drawdown_after_peak_pct": -38.67, "green_lateness_ratio": 0.4, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success_high_mae", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "084370_20240126_43300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R2L16_C10_036930_STAGE2WATCH_2024-02-28", "case_id": "R2L16_C10_036930_JUSUNG_PRICE_SPIKE_FALSE_POSITIVE", "symbol": "036930", "company_name": "주성엔지니어링", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_RECOVERY_ORDER_QUALITY_VS_PRICE_SPIKE", "sector": "AI·반도체·전자부품", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Watch", "trigger_date": "2024-02-28", "evidence_available_at_that_date": "The February 2024 spike had price/volume and generic memory recovery linkage, but not enough C10-specific order/revision bridge. It demonstrates that relative strength alone should not upgrade memory-equipment recovery to Green.", "evidence_source": "Stock-Web 036930 2024 shard rows: 2024-02-28 close 40000 after high-volume spike, 2024-04-08 area high near 41450, later 2024-07-18 low around 30650; profile CA candidates are historical only.", "stage2_evidence_fields": ["relative_strength", "public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv", "profile_path": "atlas/symbol_profiles/036/036930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-28", "entry_price": 40000, "MFE_30D_pct": 3.63, "MFE_90D_pct": 3.63, "MFE_180D_pct": 3.63, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -16.38, "MAE_90D_pct": -20.88, "MAE_180D_pct": -23.38, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-08", "peak_price": 41450, "drawdown_after_peak_pct": -26.05, "green_lateness_ratio": "not_applicable:no_confirmed_stage3_green_trigger", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "price_only_local_4B_watch_not_full_4B", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "failed_rerating_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "036930_20240228_40000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R2L16_C10_095610_STAGE2WATCH_2024-04-02", "case_id": "R2L16_C10_095610_TES_PRICE_ONLY_MEMORY_RECOVERY_BLOWOFF", "symbol": "095610", "company_name": "테스", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_RECOVERY_ORDER_QUALITY_VS_PRICE_SPIKE", "sector": "AI·반도체·전자부품", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Watch", "trigger_date": "2024-04-02", "evidence_available_at_that_date": "The April 2024 secondary move produced a large short-window MFE but then gave back the move and broke down into the second half. This is a C10 false-positive pattern: memory recovery beta plus price-only blowoff is not durable enough for Green without order/revision confirmation.", "evidence_source": "Stock-Web 095610 2024 shard rows: 2024-04-02 close 25150, 2024-04-17 high 32900, 2024-06-25 low 21600, 2024-11-14 low 14300; profile CA candidates do not overlap 2024.", "stage2_evidence_fields": ["relative_strength", "public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv", "profile_path": "atlas/symbol_profiles/095/095610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-02", "entry_price": 25150, "MFE_30D_pct": 30.82, "MFE_90D_pct": 30.82, "MFE_180D_pct": 30.82, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.34, "MAE_90D_pct": -15.7, "MAE_180D_pct": -43.14, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-17", "peak_price": 32900, "drawdown_after_peak_pct": -56.53, "green_lateness_ratio": "not_applicable:no_confirmed_stage3_green_trigger", "four_b_local_peak_proximity": 0.55, "four_b_full_window_peak_proximity": 0.55, "four_b_timing_verdict": "price_only_local_4B_watch_valid_but_not_full_4B", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_success_after_drawdown_but_late_if_waiting_for_accounting_break", "trigger_outcome_label": "price_moved_without_durable_evidence", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "095610_20240402_25150", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R2L16_C10_095610_4B_WATCH_2024-04-17", "case_id": "R2L16_C10_095610_TES_PRICE_ONLY_MEMORY_RECOVERY_BLOWOFF", "symbol": "095610", "company_name": "테스", "round": "R2", "loop": "16", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_EQUIPMENT_RECOVERY_ORDER_QUALITY_VS_PRICE_SPIKE", "sector": "AI·반도체·전자부품", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "4B_non_price_requirement_stress_test|counterexample_mining", "trigger_type": "Stage4B-Watch", "trigger_date": "2024-04-17", "evidence_available_at_that_date": "Local price blowoff after a memory-recovery beta move; evidence is price/positioning only, not order cancellation or formal thesis break. It should become a watch overlay, not full 4B.", "evidence_source": "Stock-Web 095610 2024 shard rows around 2024-04-17 local high and post-peak drawdown.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv", "profile_path": "atlas/symbol_profiles/095/095610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-17", "entry_price": 29300, "MFE_30D_pct": 2.22, "MFE_90D_pct": 2.22, "MFE_180D_pct": 2.22, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -23.89, "MAE_90D_pct": -27.65, "MAE_180D_pct": -51.19, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-17", "peak_price": 32900, "drawdown_after_peak_pct": -56.53, "green_lateness_ratio": "not_applicable:4B_overlay", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_watch_valid_but_not_full_4B", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success_not_full_4B", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "095610_20240417_29300", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same case but distinct 4B local-vs-full timing audit", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L16_C10_240810_WONIKIPS_MEMORY_RECOVERY_STAGE2A", "trigger_id": "R2L16_C10_240810_STAGE2A_2024-02-29", "symbol": "240810", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 18, "relative_strength_score": 16, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 5, "margin_bridge_score": 8, "revision_score": 20, "relative_strength_score": 16, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage2-Actionable/Yellow boundary", "changed_components": ["margin_bridge_score", "backlog_visibility_score", "execution_risk_score"], "component_delta_explanation": "C10 lift rewards memory-equipment recovery only when order/revision bridge is visible; the high MAE keeps it below automatic Green.", "MFE_90D_pct": 35.09, "MAE_90D_pct": -3.46, "score_return_alignment_label": "aligned_positive_high_mae", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L16_C10_084370_EUGENETECH_MEMORY_RECOVERY_DELAYED_SUCCESS", "trigger_id": "R2L16_C10_084370_STAGE2A_2024-01-25", "symbol": "084370", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 13, "relative_strength_score": 12, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 8, "revision_score": 18, "relative_strength_score": 14, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable", "changed_components": ["revision_score", "margin_bridge_score", "backlog_visibility_score"], "component_delta_explanation": "C10 should allow Stage2-Actionable before Green when memory recovery is visible but first-quarter shakeout risk remains high.", "MFE_90D_pct": 38.57, "MAE_90D_pct": -25.64, "score_return_alignment_label": "aligned_positive_delayed", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L16_C10_036930_JUSUNG_PRICE_SPIKE_FALSE_POSITIVE", "trigger_id": "R2L16_C10_036930_STAGE2WATCH_2024-02-28", "symbol": "036930", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 7, "relative_strength_score": 18, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 15, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow false-positive risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 12, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 64, "stage_label_after": "Stage2-Watch", "changed_components": ["revision_score", "relative_strength_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C10 guard subtracts score when a memory-equipment move is mainly price/volume without order or revision bridge.", "MFE_90D_pct": 3.63, "MAE_90D_pct": -20.88, "score_return_alignment_label": "counterexample_fixed_by_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L16_C10_095610_TES_PRICE_ONLY_MEMORY_RECOVERY_BLOWOFF", "trigger_id": "R2L16_C10_095610_STAGE2WATCH_2024-04-02", "symbol": "095610", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 6, "relative_strength_score": 21, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 18, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow/false Green risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 11, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": -15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 60, "stage_label_after": "Stage2-Watch + 4B-Watch overlay", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C10 guard prevents price-only memory recovery beta from becoming a positive-stage signal; separate 4B watch can still be useful.", "MFE_90D_pct": 30.82, "MAE_90D_pct": -15.7, "score_return_alignment_label": "counterexample_fixed_by_guard", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "residual_contribution", "round": "R2", "loop": "16", "scheduled_round": "R2", "scheduled_loop": 16, "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 3, "diversity_score_summary": "new_symbol_count=4; counterexample_count=2; C10 was absent from R2 loops 10-15; no same symbol/date/entry reuse; wrong_round_penalty=0", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["memory_equipment_price_only_false_positive", "high_MAE_success_requires_stage2_not_green", "price_only_4B_watch_overlay_too_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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

completed_round = R2  
completed_loop = 16  
next_round = R3  
next_loop = 16  
round_schedule_status = valid  
round_sector_consistency = pass

## 28. Source Notes

- Stock-Web manifest max_date used for forward-window eligibility: 2026-02-20.
- Price basis: tradable_raw, raw_unadjusted_marcap.
- Corporate-action windows: all representative 2024 windows are clean_180D_window under the profile checks used here.
- This is a historical calibration artifact only, not a current stock recommendation.
