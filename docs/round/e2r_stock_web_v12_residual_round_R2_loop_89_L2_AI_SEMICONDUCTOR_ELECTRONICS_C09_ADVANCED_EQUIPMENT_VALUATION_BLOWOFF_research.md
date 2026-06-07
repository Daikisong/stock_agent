# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata
```text
round = R2
loop = 89
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id = ADVANCED_TEST_SOCKET_PROBE_CARD_EQUIPMENT_VALUATION_BLOWOFF_VS_CUSTOMER_QUALITY_BRIDGE
loop_objective = coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## 1. Current Calibrated Profile Assumption
Current proxy is `e2r_2_1_stock_web_calibrated`; this loop does not re-prove the global Stage2 bonus or loosen Green. It tests C09-specific residual error: advanced test/socket/probe-card equipment price spikes can look like Stage2-Actionable even when customer qualification, repeat demand, or margin bridge is still missing.

## 2. Round / Large Sector / Canonical Archetype Scope
- selected_round: `R2`
- large_sector_id: `L2_AI_SEMICONDUCTOR_ELECTRONICS`
- canonical_archetype_id: `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`
- scope rule: C09 belongs to R2/L2; round-sector consistency passes.

## 3. Previous Coverage / Duplicate Avoidance Check
- Static No-Repeat Index shows C09 at 15 rows, below the 30-row minimum stability band.
- Top-covered C09 symbols include 039030, 084370, 140860, 240810, 036810, 036930; this loop uses 131290, 095340, 425420, avoiding those top-covered pairs.
- Hard duplicate key checked at design level: no repeated `C09 + symbol + trigger_type + entry_date` combination from the visible No-Repeat summary.
- Conversation-local note: the immediately prior run filled C08; this run advances to the next Priority 0 archetype instead of repeating C08.

## 4. Stock-Web OHLC Input / Price Source Validation
| field | value |
|---|---|
| source | Songdaiki/stock-web |
| source_basis | FinanceData/marcap |
| manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| validation_status | usable_for_historical_calibration |

## 5. Historical Eligibility Gate
| symbol | profile_path | entry_date | forward_180D | corporate_action_window_status | calibration_usable |
|---|---|---|---:|---|---|
| 131290 | `atlas/symbol_profiles/131/131290.json` | 2024-02-13 | 180 | clean_180D_window | true |
| 095340 | `atlas/symbol_profiles/095/095340.json` | 2024-03-08 | 180 | clean_180D_window; profile has 2023-10-20 corporate-action candidate outside forward window | true |
| 425420 | `atlas/symbol_profiles/425/425420.json` | 2024-07-04 | 180 | clean_180D_window; no corporate-action candidates in profile | true |

## 6. Canonical Archetype Compression Map
| fine/deep sub-archetype | canonical compression | scoring treatment |
|---|---|---|
| probe-card/test-interface customer qualification bridge | C09 | allow Stage2-Actionable only with customer/repeat-demand/margin bridge |
| socket/test-equipment price-only beta blowoff | C09 | block positive promotion; route to local 4B watch |
| local 4B price-only spike with no non-price bridge | C09 | guardrail row, not full 4B sell/production rule |

## 7. Case Selection Summary
| case_id | symbol | company | role | trigger | entry | MFE90 | MAE90 | verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| C09_TSE_131290_2024_02_13_STAGE2A_PROBE_CARD_BRIDGE | 131290 | 티에스이 | positive | Stage2-Actionable | 57000 | 54.04 | -13.07 | current_profile_correct |
| C09_ISC_095340_2024_03_08_STAGE2_FALSE_POSITIVE_BLOWOFF | 095340 | ISC | counterexample | Stage2 | 95000 | 13.68 | -42.95 | current_profile_false_positive |
| C09_TFE_425420_2024_07_04_LOCAL_4B_PRICE_ONLY_BLOWOFF | 425420 | 티에프이 | counterexample | Stage4B | 31200 | 4.81 | -63.49 | current_profile_4B_too_late |

## 8. Positive vs Counterexample Balance
- positive_case_count: 1
- counterexample_count: 2
- 4B_case_count: 1
- calibration_usable_case_count: 3

## 9. Evidence Source Map
| case | evidence_family | evidence timing | limitation |
|---|---|---|---|
| C09_TSE_131290_2024_02_13_STAGE2A_PROBE_CARD_BRIDGE | probe_card_customer_quality_margin_bridge | available-at-trigger proxy | source_proxy_only / URL repair needed |
| C09_ISC_095340_2024_03_08_STAGE2_FALSE_POSITIVE_BLOWOFF | socket_beta_price_only_valuation_blowoff | available-at-trigger proxy | source_proxy_only / URL repair needed |
| C09_TFE_425420_2024_07_04_LOCAL_4B_PRICE_ONLY_BLOWOFF | test_interface_price_only_local_4b_blowoff | available-at-trigger proxy | source_proxy_only / URL repair needed |

## 10. Price Data Source Map
| symbol | shard | selected row basis |
|---:|---|---|
| 131290 | `atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv` | entry close / forward high-low path from tradable_raw row |
| 095340 | `atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv` | entry close / forward high-low path from tradable_raw row |
| 425420 | `atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv` | entry close / forward high-low path from tradable_raw row |

## 11. Case-by-Case Trigger Grid
| trigger_id | trigger_type | stage2 fields | stage3 fields | stage4B fields | outcome |
|---|---|---|---|---|---|
| TR_C09_TSE_2024_02_13_STAGE2A | Stage2-Actionable | customer_or_order_quality;relative_strength;early_revision_signal;capacity_or_volume_route | margin_bridge;repeat_order_or_conversion | valuation_blowoff_watch_after_peak | good_stage2_high_mfe_then_needs_valuation_4b |
| TR_C09_ISC_2024_03_08_STAGE2_FALSE_POSITIVE | Stage2 | relative_strength | none | valuation_blowoff;positioning_overheat;price_only_local_peak | false_positive_high_mae_after_valuation_blowoff |
| TR_C09_TFE_2024_07_04_STAGE4B_LOCAL | Stage4B | relative_strength | none | price_only_local_peak;valuation_blowoff;positioning_overheat | good_local_4b_watch_prevented_positive_stage |

## 12. Trigger-Level OHLC Backtest Tables
| trigger_id | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| TR_C09_TSE_2024_02_13_STAGE2A | 2024-02-13 | 57000 | 10.88 | -13.07 | 54.04 | -13.07 | 54.04 | -33.25 | 2024-05-03 | 87800 | -56.66 |
| TR_C09_ISC_2024_03_08_STAGE2_FALSE_POSITIVE | 2024-03-08 | 95000 | 13.68 | -12.63 | 13.68 | -42.95 | 13.68 | -56.74 | 2024-03-28 | 108000 | -61.94 |
| TR_C09_TFE_2024_07_04_STAGE4B_LOCAL | 2024-07-04 | 31200 | 4.81 | -47.05 | 4.81 | -63.49 | 4.81 | -63.49 | 2024-07-04 | 32700 | -65.17 |

## 13. Current Calibrated Profile Stress Test
- Current profile is directionally correct for the TSE positive bridge case, because customer/test-interface quality evidence was present and early MFE was strong.
- Current profile remains vulnerable to C09 false positives when relative strength and valuation repricing arrive before repeat customer qualification or margin/revenue conversion.
- Existing price-only blowoff block is kept. This loop strengthens it only as a C09 local 4B watch and does not propose a global production delta.

## 14. Stage2 / Yellow / Green Comparison
- Stage2-Actionable works only when customer quality + repeat demand + margin bridge are all at least partially visible.
- Stage3-Yellow/Green should remain strict; none of the three cases justifies lowering Green thresholds.
- Green lateness ratio is not applicable because this is a C09 blowoff/guardrail loop, not a confirmed Green promotion loop.

## 15. 4B Local vs Full-window Timing Audit
| case | local 4B proximity | full-window 4B proximity | verdict |
|---|---:|---:|---|
| C09_TSE_131290_2024_02_13_STAGE2A_PROBE_CARD_BRIDGE | 0.72 | 0.72 | non-price bridge present; 4B watch after upside capture |
| C09_ISC_095340_2024_03_08_STAGE2_FALSE_POSITIVE_BLOWOFF | 0.82 | 0.82 | price-only valuation blowoff; should be blocked from positive Stage2 |
| C09_TFE_425420_2024_07_04_LOCAL_4B_PRICE_ONLY_BLOWOFF | 1.00 | 1.00 | good local 4B watch; full 4B still requires non-price evidence |

## 16. 4C Protection Audit
- No hard 4C contract/qualification failure is confirmed from the available source proxy. TFE/ISC are treated as 4B/watch and false-positive guardrail cases rather than hard 4C thesis-break rows.

## 17. Sector-Specific Rule Candidate
sector_specific_rule_candidate = true. Within L2, advanced equipment/test-interface price momentum should not become Stage2-Actionable unless at least one non-price bridge exists: customer qualification, repeat order, margin bridge, or revision support.

## 18. Canonical-Archetype Rule Candidate
canonical_archetype_rule_candidate = true. For C09, if `valuation_repricing_score` and `relative_strength_score` are high but `customer_quality_score` and `margin_bridge_score` are missing, route to Stage4B-watch / Stage2-blocked, not Stage2-Actionable.

## 19. Before / After Backtest Comparison
| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive count | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 24.18 | -39.84 | 2 | catches some price-only risk but still too generous to equipment beta |
| P1 sector_specific_candidate_profile | 3 | 24.18 | -39.84 | 1 | requires L2 customer/order bridge |
| P2 canonical_archetype_candidate_profile | 3 | 24.18 | -39.84 | 0-1 | best fit; keeps TSE, blocks ISC/TFE positive promotion |
| P3 counterexample_guard_profile | 2 | 9.25 | -53.22 | 0 | routes price-only blowoff to watch-only |

## 20. Score-Return Alignment Matrix
| case | before score/stage | after score/stage | alignment |
|---|---|---|---|
| C09_TSE_131290_2024_02_13_STAGE2A_PROBE_CARD_BRIDGE | 69 / Stage2 | 76 / Stage2-Actionable | improved_alignment_positive_with_4b_watch |
| C09_ISC_095340_2024_03_08_STAGE2_FALSE_POSITIVE_BLOWOFF | 72 / Stage2-Actionable | 61 / Stage2-blocked | improved_alignment_blocks_false_positive |
| C09_TFE_425420_2024_07_04_LOCAL_4B_PRICE_ONLY_BLOWOFF | 72 / Stage2-Actionable | 61 / Stage4B-watch | improved_alignment_blocks_false_positive |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | ADVANCED_TEST_SOCKET_PROBE_CARD_EQUIPMENT_VALUATION_BLOWOFF_VS_CUSTOMER_QUALITY_BRIDGE | 1 | 2 | 1 | 0 | 3 | 0 | 3 | 3 | 2 | true | true | C09 static 15 rows; still below 30 after local addition |

## 22. Residual Contribution Summary
```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | stage2_actionable_evidence_bonus
residual_error_types_found: price_only_equipment_beta_false_positive | valuation_blowoff_high_MAE | customer_bridge_missing
new_axis_proposed: c09_customer_quality_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C09 local watch
existing_axis_weakened: null
existing_axis_kept: price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.

## 23. Validation Scope / Non-Validation Scope
- Validation scope: historical price path from stock-web tradable_raw shards, C09 canonical compression, Stage2/4B guardrail direction.
- Non-validation scope: live candidate search, broker/API action, production scoring change, current investment recommendation.
- Evidence URL repair remains pending; rows are source-proxy only and should not be over-promoted without later URL validation.

## 24. Shadow Weight Calibration
| axis | scope | baseline | tested | confidence | proposal_type |
|---|---|---|---|---|---|
| c09_customer_quality_bridge_required_for_stage2_actionable | canonical_archetype_specific | not_required | required_if_valuation_repricing_score_high | medium | canonical_shadow_only |
| full_4b_requires_non_price_evidence | canonical_archetype_specific | True | strengthen_local_4b_watch_when_price_only_blowoff_and_no_customer_bridge | medium | canonical_shadow_only |

## 25. Machine-Readable Rows
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C09_TSE_131290_2024_02_13_STAGE2A_PROBE_CARD_BRIDGE","symbol":"131290","company_name":"티에스이","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_TEST_SOCKET_PROBE_CARD_EQUIPMENT_VALUATION_BLOWOFF_VS_CUSTOMER_QUALITY_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_stage2_high_mfe_then_needs_valuation_4b","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Entry row close 57,000 on 2024-02-13; peak high 87,800 around 2024-05-03; later 180D drawdown shows C09 4B overlay still matters."}
{"row_type":"case","case_id":"C09_ISC_095340_2024_03_08_STAGE2_FALSE_POSITIVE_BLOWOFF","symbol":"095340","company_name":"ISC","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_TEST_SOCKET_PROBE_CARD_EQUIPMENT_VALUATION_BLOWOFF_VS_CUSTOMER_QUALITY_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2 false-positive / valuation blowoff","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_high_mae_after_valuation_blowoff","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Entry close 95,000 after blowoff; high 108,000 then deep 180D drawdown. The row stresses price-only positive-stage blocking."}
{"row_type":"case","case_id":"C09_TFE_425420_2024_07_04_LOCAL_4B_PRICE_ONLY_BLOWOFF","symbol":"425420","company_name":"티에프이","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_TEST_SOCKET_PROBE_CARD_EQUIPMENT_VALUATION_BLOWOFF_VS_CUSTOMER_QUALITY_BRIDGE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B local price-only watch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_local_4b_watch_prevented_positive_stage","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Entry close 31,200 at local price-only spike; 30D MAE already -47.05%, validating local 4B watch."}
{"row_type":"trigger","trigger_id":"TR_C09_TSE_2024_02_13_STAGE2A","case_id":"C09_TSE_131290_2024_02_13_STAGE2A_PROBE_CARD_BRIDGE","symbol":"131290","company_name":"티에스이","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_TEST_SOCKET_PROBE_CARD_EQUIPMENT_VALUATION_BLOWOFF_VS_CUSTOMER_QUALITY_BRIDGE","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":57000,"evidence_available_at_that_date":"probe-card/test-interface customer qualification and HBM/AI memory test demand proxy; non-price bridge present but not yet full Green","evidence_source":"source_proxy_only__historical_public_event_proxy","evidence_family":"probe_card_customer_quality_margin_bridge","stage2_evidence_fields":["customer_or_order_quality","relative_strength","early_revision_signal","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","repeat_order_or_conversion"],"stage4b_evidence_fields":["valuation_blowoff_watch_after_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.88,"MFE_90D_pct":54.04,"MFE_180D_pct":54.04,"MAE_30D_pct":-13.07,"MAE_90D_pct":-13.07,"MAE_180D_pct":-33.25,"peak_date":"2024-05-03","peak_price":87800,"drawdown_after_peak_pct":-56.66,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.72,"four_b_full_window_peak_proximity":0.72,"trigger_outcome_label":"good_stage2_high_mfe_then_needs_valuation_4b","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"131290_2024-02-13_57000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"positive"}
{"row_type":"trigger","trigger_id":"TR_C09_ISC_2024_03_08_STAGE2_FALSE_POSITIVE","case_id":"C09_ISC_095340_2024_03_08_STAGE2_FALSE_POSITIVE_BLOWOFF","symbol":"095340","company_name":"ISC","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_TEST_SOCKET_PROBE_CARD_EQUIPMENT_VALUATION_BLOWOFF_VS_CUSTOMER_QUALITY_BRIDGE","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":95000,"evidence_available_at_that_date":"socket/HBM beta price surge with insufficient fresh customer-quality or order/revenue bridge at entry; price action outran evidence","evidence_source":"source_proxy_only__historical_public_event_proxy","evidence_family":"socket_beta_price_only_valuation_blowoff","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.68,"MFE_90D_pct":13.68,"MFE_180D_pct":13.68,"MAE_30D_pct":-12.63,"MAE_90D_pct":-42.95,"MAE_180D_pct":-56.74,"peak_date":"2024-03-28","peak_price":108000,"drawdown_after_peak_pct":-61.94,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.82,"trigger_outcome_label":"false_positive_high_mae_after_valuation_blowoff","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile has 2023-10-20 corporate-action candidate outside forward window","same_entry_group_id":"095340_2024-03-08_95000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"counterexample"}
{"row_type":"trigger","trigger_id":"TR_C09_TFE_2024_07_04_STAGE4B_LOCAL","case_id":"C09_TFE_425420_2024_07_04_LOCAL_4B_PRICE_ONLY_BLOWOFF","symbol":"425420","company_name":"티에프이","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_TEST_SOCKET_PROBE_CARD_EQUIPMENT_VALUATION_BLOWOFF_VS_CUSTOMER_QUALITY_BRIDGE","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-07-04","entry_date":"2024-07-04","entry_price":31200,"evidence_available_at_that_date":"test-interface/equipment beta spike without repeat customer qualification or margin bridge; local 4B watch, not full Green/positive","evidence_source":"source_proxy_only__historical_public_event_proxy","evidence_family":"test_interface_price_only_local_4b_blowoff","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv","profile_path":"atlas/symbol_profiles/425/425420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.81,"MFE_90D_pct":4.81,"MFE_180D_pct":4.81,"MAE_30D_pct":-47.05,"MAE_90D_pct":-63.49,"MAE_180D_pct":-63.49,"peak_date":"2024-07-04","peak_price":32700,"drawdown_after_peak_pct":-65.17,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"trigger_outcome_label":"good_local_4b_watch_prevented_positive_stage","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; no corporate-action candidates in profile","same_entry_group_id":"425420_2024-07-04_31200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"counterexample"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_TSE_131290_2024_02_13_STAGE2A_PROBE_CARD_BRIDGE","trigger_id":"TR_C09_TSE_2024_02_13_STAGE2A","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":69,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":5,"revision_score":3,"relative_strength_score":5,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 shadow profile requires customer qualification/repeat-demand bridge for Stage2-Actionable and routes price-only equipment beta to 4B watch.","MFE_90D_pct":54.04,"MAE_90D_pct":-13.07,"score_return_alignment_label":"improved_alignment_positive_with_4b_watch","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_ISC_095340_2024_03_08_STAGE2_FALSE_POSITIVE_BLOWOFF","trigger_id":"TR_C09_ISC_2024_03_08_STAGE2_FALSE_POSITIVE","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":8,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-blocked","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 shadow profile requires customer qualification/repeat-demand bridge for Stage2-Actionable and routes price-only equipment beta to 4B watch.","MFE_90D_pct":13.68,"MAE_90D_pct":-42.95,"score_return_alignment_label":"improved_alignment_blocks_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_TFE_425420_2024_07_04_LOCAL_4B_PRICE_ONLY_BLOWOFF","trigger_id":"TR_C09_TFE_2024_07_04_STAGE4B_LOCAL","symbol":"425420","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":8,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage4B-watch","changed_components":["customer_quality_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 shadow profile requires customer qualification/repeat-demand bridge for Stage2-Actionable and routes price-only equipment beta to 4B watch.","MFE_90D_pct":4.81,"MAE_90D_pct":-63.49,"score_return_alignment_label":"improved_alignment_blocks_false_positive","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"shadow_weight","axis":"c09_customer_quality_bridge_required_for_stage2_actionable","scope":"canonical_archetype_specific","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","baseline_value":"not_required","tested_value":"required_if_valuation_repricing_score_high","delta":"+guard","reason":"C09 price-only equipment beta created severe MAE in ISC/TFE while TSE worked only with customer/qualification bridge.","backtest_effect":"reduces false positive Stage2-Actionable; preserves one bridge-positive case","trigger_ids":"TR_C09_TSE_2024_02_13_STAGE2A|TR_C09_ISC_2024_03_08_STAGE2_FALSE_POSITIVE|TR_C09_TFE_2024_07_04_STAGE4B_LOCAL","calibration_usable_count":3,"new_independent_case_count":3,"counterexample_count":2,"confidence":"medium","proposal_type":"canonical_shadow_only","notes":"not production; post-calibrated residual"}
{"row_type":"shadow_weight","axis":"full_4b_requires_non_price_evidence","scope":"canonical_archetype_specific","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","baseline_value":true,"tested_value":"strengthen_local_4b_watch_when_price_only_blowoff_and_no_customer_bridge","delta":"strengthen_watch","reason":"TFE and ISC show local blowoff needs watch routing even when full 4B is not confirmed by non-price evidence.","backtest_effect":"earlier watch without treating price-only as full 4B sell signal","trigger_ids":"TR_C09_ISC_2024_03_08_STAGE2_FALSE_POSITIVE|TR_C09_TFE_2024_07_04_STAGE4B_LOCAL","calibration_usable_count":2,"new_independent_case_count":2,"counterexample_count":2,"confidence":"medium","proposal_type":"canonical_shadow_only","notes":"existing axis strengthened only inside C09"}
{"row_type":"residual_contribution","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage2_actionable_evidence_bonus"],"residual_error_types_found":["price_only_equipment_beta_false_positive","valuation_blowoff_high_MAE","customer_bridge_missing"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"coverage_matrix","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_TEST_SOCKET_PROBE_CARD_EQUIPMENT_VALUATION_BLOWOFF_VS_CUSTOMER_QUALITY_BRIDGE","positive_case_count":1,"counterexample_count":2,"4B_case_count":1,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":true,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C09 static rows 15 -> +3 local rows; still under 30 target after external ingest"}
{"row_type":"narrative_only","case_id":"C09_NOTE_SOURCE_PROXY","symbol":"MULTI","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","reason":"evidence_url_pending_source_proxy_only; price path verified from stock-web, but event/source URLs should be repaired in a later URL-validation batch","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 89
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C06_HBM_MEMORY_CUSTOMER_CAPACITY
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes
- Prompt basis: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-repeat basis: docs/core/V12_Research_No_Repeat_Index.md
- Manifest checked: Songdaiki/stock-web atlas/manifest.json, max_date 2026-02-20, tradable_raw, raw_unadjusted_marcap.
- Price rows checked: 131290/2024, 131290/2025, 095340/2024, 095340/2025, 425420/2024, 425420/2025.
- Source proxy caveat: event/evidence names are historical public-event proxies; future URL repair can strengthen or reject these rows.
