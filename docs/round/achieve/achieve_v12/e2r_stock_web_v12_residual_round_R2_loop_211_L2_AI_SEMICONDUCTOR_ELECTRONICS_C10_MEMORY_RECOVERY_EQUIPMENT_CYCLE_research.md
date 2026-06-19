# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 211
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 / balance-quality reinforcement + Priority 0 direct URL and MFE/MAE repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: C10_MEMORY_CAPEX_EQUIPMENT_ORDER_CONVERSION_AND_FALSE_RECOVERY_GUARD
loop_objective: counterexample_mining; residual_false_positive_mining; residual_missed_structural_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
filename: e2r_stock_web_v12_residual_round_R2_loop_211_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
```

One-line contribution: this loop adds 6 new independent cases, 7 calibration-usable trigger rows, 3 positives, 3 counterexamples, and a C10-specific order-conversion freshness ladder.

## 1. Current Calibrated Profile Assumption

Current proxy is `e2r_2_1_stock_web_calibrated_proxy`. This MD does not reopen global v12 rules such as `stage2_actionable_evidence_bonus`, stricter Yellow/Green thresholds, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, or `hard_4c_thesis_break_routes_to_4c`. The test is local: whether C10 memory-equipment recovery needs a ladder from broad cycle repair to supplier-specific order conversion and margin confirmation.

## 2. Round / Sector / Archetype Scope

C10 maps to `R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS`. This is not HBM relative-strength research, not a live semiconductor screen, and not a current investment recommendation. It is historical trigger-level calibration using Stock-Web OHLC rows.

## 3. Previous Coverage / Duplicate Avoidance Check

The no-repeat index shows all C01~C32 archetypes are already above 80 rows, so this run targets quality reinforcement rather than row-count filling. C10 is listed under Priority 1 for early recovery-cycle false positives and order-conversion confirmation. The run avoids the immediately repeated C15/C05/C01/C13 sequence from the current session and uses the hard duplicate key `canonical_archetype_id + symbol + trigger_type + entry_date`.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest values used:

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date / max_date | 1995-05-02 / 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |

Downloaded and calculated tradable shards:

| symbol | years used | profile path | 180D CA status |
|---:|---|---|---|
| 092870 | 2023, 2024 | atlas/symbol_profiles/092/092870.json | clean_180D_window; 1Y blocked by later 2024-07-31 CA candidate |
| 084370 | 2023, 2024 | atlas/symbol_profiles/084/084370.json | clean_180D_window |
| 281820 | 2024, 2025 | atlas/symbol_profiles/281/281820.json | clean_180D_window |
| 095610 | 2021, 2022 | atlas/symbol_profiles/095/095610.json | clean_180D_window |
| 319660 | 2024, 2025 | atlas/symbol_profiles/319/319660.json | clean_180D_window |
| 036930 | 2023, 2024 | atlas/symbol_profiles/036/036930.json | clean_180D_window |

## 5. Historical Eligibility Gate

All representative rows are historical, have an entry row in the Stock-Web tradable shard, have at least 180 forward trading days available before the manifest max date, and include complete canonical `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, and `MAE_180D_pct` fields. No representative row is blocked by a 180D corporate-action window.

## 6. Canonical Archetype Compression Map

| fine evidence family | compressed C10 interpretation | expected score behavior |
|---|---|---|
| DDR5 / memory tester generation change | real conversion route, but high-MAE sizing risk | allow Stage2-Actionable; require MAE guard |
| DRAM process/fine-node equipment route | clean customer/process conversion | allow Stage2-Actionable or Yellow |
| mixed delay + material/CMP route | missed structural risk if overly conservative | keep Yellow possible, not hard block |
| result-only quarter after cycle narrative | late Green trap | cap below Green without fresh order conversion |
| IR/business-status near local peak | local 4B risk | overlay, not promotion evidence |
| 3Q result comment without conversion | false positive Green risk | require freshness decay and 4B watch |

## 7. Case Selection Summary

| case | symbol | type | pos/counter | trigger | entry | MFE30/90/180 | MAE30/90/180 | peak | verdict |
|---|---:|---|---|---|---|---:|---:|---|---|
| C10-R2-L211-01 | 092870 엑시콘 | high_mae_success | positive | Stage2-Actionable | 2023-08-28 @ 14890 | 10.81/57.15/137.74 | -15.04/-27.47/-27.47 | 2024-04-02 35400 | current_profile_correct |
| C10-R2-L211-02 | 084370 유진테크 | structural_success | positive | Stage2-Actionable | 2023-08-16 @ 32550 | 36.56/46.7/80.34 | -5.38/-5.38/-5.38 | 2024-05-07 58700 | current_profile_correct |
| C10-R2-L211-03 | 281820 케이씨텍 | missed_structural | positive | Stage3-Yellow | 2024-12-02 @ 27400 | 34.12/51.09/51.09 | -8.21/-17.15/-17.15 | 2025-02-18 41400 | current_profile_missed_structural |
| C10-R2-L211-04 | 095610 테스 | failed_rerating | counterexample | Stage3-Green | 2021-08-17 @ 28450 | 5.8/5.8/5.8 | -11.42/-14.76/-16.52 | 2021-09-23 30100 | current_profile_false_positive |
| C10-R2-L211-05 | 319660 피에스케이 | failed_rerating | counterexample | Stage2-Actionable | 2024-05-31 @ 31750 | 23.15/23.15/23.15 | -3.94/-35.43/-51.02 | 2024-07-11 39100 | current_profile_false_positive |
| C10-R2-L211-06 | 036930 주성엔지니어링 | false_positive_green | counterexample | Stage3-Yellow | 2023-11-21 @ 34400 | 8.43/18.46/20.49 | -9.45/-21.8/-35.61 | 2024-04-08 41450 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

| bucket | cases | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | interpretation |
|---|---:|---:|---:|---:|---:|---|
| positive structural / missed structural | 3 | 51.65 | -16.67 | 89.72 | -16.67 | conversion route works, but sizing and mixed-signal guards still matter |
| counterexample / failed rerating | 3 | 15.8 | -24.0 | 16.48 | -34.38 | result-only or local-peak narratives produce poor score-return alignment |
| all representatives | 6 | 33.73 | -20.33 | 53.1 | -25.53 | C10 needs a ladder, not blanket memory-recovery promotion |

## 9. Evidence Source Map

| case | symbol | evidence source | outcome |
|---|---:|---|---|
| C10-R2-L211-01 | 092870 | IRGO 092870 IR Room; KIRS 2023-08 Exicon report | memory_tester_generation_change_positive_but_high_mae |
| C10-R2-L211-02 | 084370 | IRGO 084370 IR page; iM Securities 2023-08 report | dram_process_equipment_recovery_structural_success |
| C10-R2-L211-03 | 281820 | IRGO 281820 IR page; public broker report dated 2024-11-29 | mixed_delay_report_missed_dram_cmp_repricing |
| C10-R2-L211-04 | 095610 | IRGO 095610 2021-08 2Q21 result presentation; public 1Q21 result review | late_supercycle_result_false_positive |
| C10-R2-L211-05 | 319660 | IRGO 319660 IR page | business_status_peak_followed_by_execution_drawdown |
| C10-R2-L211-06 | 036930 | IRGO 036930 IR page | result_comment_local_rally_high_mae_failure |

## 10. Price Data Source Map

All entry prices are the `c` column of the next tradable Stock-Web row after the evidence date, because evidence publication time is not consistently intraday-verifiable. MFE is the maximum forward high against entry close, and MAE is the minimum forward low against entry close over 30/90/180 trading-day windows.

## 11. Trigger-Level OHLC Backtest Tables

The representative grid in Section 7 is the aggregate basis. The overlay row below is not counted as a new independent case but is kept for the local/full 4B timing split.

| overlay | symbol | trigger | entry | MFE30/90/180 | MAE30/90/180 | local/full 4B proximity | verdict |
|---|---:|---|---|---:|---:|---:|---|
| C10-R2-L211-05-T02 | 319660 피에스케이 | 2024-08-19 | 2024-08-20 @ 28950 | 6.39/6.39/6.39 | -29.19/-46.29/-46.29 | -0.38 / -0.38 | late_after_local_peak_not_protective |

## 12. Current Profile Stress Test

The current profile handles clear conversion positives well, but C10 still has four residual error modes:

1. `result_only_memory_green_false_positive`: already-realized results are mistaken for fresh order conversion.
2. `mixed_delay_missed_structural`: delay language suppresses a genuine material/process turn.
3. `4B_overlay_too_late_after_local_peak`: the 4B label is directionally right but arrives after the useful protection window.
4. `high_mae_success_sizing_problem`: winners can still carry -17% to -27% MAE before the thesis matures.

## 13. Local 4B vs Full-Window 4B Split

The PSK overlay is deliberately marked `dedupe_for_aggregate=false`. It tests the prompt's split between local 4B and full-window 4B: after the local peak has already passed, a 4B row may diagnose risk but should not receive the same credit as an early protective 4B trigger.

## 14. Stage2 / Yellow / Green / 4B / 4C Interpretation

| stage | C10 interpretation from this run |
|---|---|
| Stage2 | broad memory bottom or public recovery signal can open the watch bridge |
| Stage2-Actionable | customer/process/order route appears before the price path is exhausted |
| Stage3-Yellow | multiple public sources plus conversion evidence, but not enough margin/FCF confirmation |
| Stage3-Green | requires order conversion freshness plus margin/revision durability |
| Stage4B | full/local peak risk overlay; price-only cannot promote but can warn |
| Stage4C | no hard 4C in this loop; thesis break needs repeated order/margin collapse or structural customer loss |

## 15. Raw Component Score Breakdown Summary

The shadow simulation does not change production scoring. It proposes reallocating C10 evidence from broad memory-cycle headlines toward order conversion and margin freshness.

| component | current risk | shadow handling |
|---|---|---|
| memory-cycle headline | over-promotes late result rows | cap if supplier conversion is absent |
| order/customer conversion | underweighted in structural winners | promote Stage2-Actionable / Yellow |
| margin/revision confirmation | needed for Green | require freshness, not stale record result |
| price-only/positioning | can be useful as watch | never promotes; only 4B overlay |

## 16. Sector-Specific Rule Candidate

`L2_AI_SEMICONDUCTOR_ELECTRONICS` rule candidate:

> L2 memory-equipment recovery should split memory price/capex sentiment, utilization, customer/process conversion, booked equipment order visibility, and margin confirmation. Stage2 can start at conversion evidence; Stage3-Green waits for order conversion or durable customer confirmation.

## 17. Canonical Archetype Rule Candidate

`C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` rule candidate:

> C10 needs a memory order-conversion freshness ladder: memory upcycle headline = watch; utilization/process route = Stage2 possible; customer/order/tool conversion = Stage2-Actionable/Yellow; booked order/repeat plus margin = Green; result-only after local rally = cap below Green; business-status after peak = 4B/decay overlay.

## 18. Before / After Rule Impact

| case | before risk | after shadow behavior |
|---|---|---|
| Exicon | high MFE but high MAE may be over-sized | keep positive, add MAE/sizing guard |
| Eugene Tech | clean conversion success | preserve Stage2-Actionable / Yellow |
| KC Tech | mixed delay may be missed | allow Yellow if material/process route is visible |
| TES | record result may be over-promoted | cap stale result-only Green |
| PSK | business-status near peak may be late | require 4B timing proximity audit |
| Jusung | result comment may look like Green | require fresh order/backlog/margin bridge |

## 19. Score-Return Alignment Matrix

| alignment feature | positive rows | counterexample rows | scoring implication |
|---|---|---|---|
| customer/process/order route | strong in Exicon/Eugene/KC Tech | weak in TES/PSK/Jusung | reward only when concrete route exists |
| result-only confirmation | secondary | dominant in TES/Jusung | cap Green if freshness is stale |
| high MAE despite high MFE | Exicon/KC Tech | PSK/Jusung | add sizing/watch guard rather than block all positives |
| 4B timing | not needed | PSK late overlay | mark late 4B separately from good peak protection |

## 20. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C10_MEMORY_CAPEX_EQUIPMENT_ORDER_CONVERSION_AND_FALSE_RECOVERY_GUARD | 3 | 3 | 1 | 0 | 6 | 0 | 7 | 6 | 4 | C10 now has complete 30/90/180 MFE-MAE rows for false recovery, missed structural, high-MAE success, and late 4B overlay |

## 21. Residual Contribution Summary

```yaml
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
same_archetype_new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - result_only_memory_green_false_positive
  - mixed_delay_missed_structural
  - 4B_overlay_too_late_after_local_peak
  - high_mae_success_sizing_problem
new_axis_proposed: c10_memory_order_conversion_freshness_ladder
existing_axis_strengthened: stage3_green_revision_min_by_order_conversion; full_4b_requires_non_price_evidence_with_timing_proximity
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus; price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: L2 memory-equipment recovery needs customer/process/order conversion before Green promotion.
canonical_archetype_rule_candidate: C10 should split memory upcycle sentiment, utilization, order conversion, margin confirmation, and result-only decay.
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 22. Validation Scope / Non-Validation Scope

Validated: actual Stock-Web tradable OHLC rows, entry close, 30D/90D/180D MFE/MAE, 180D forward window availability, symbol/profile path existence, representative/overlay dedupe status, and direct/public evidence URL map.

Not validated: live candidate status, current 2026 investment attractiveness, broker target prices, production scoring code, or any `stock_agent` source implementation. No current recommendation is made.

## 23. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c10_order_conversion_freshness_gate,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Require customer/order/fine-node conversion evidence before Green","counterexamples avg MAE180 -34.38 while positives avg MFE180 89.72","C10-R2-L211-01-T01|C10-R2-L211-02-T01|C10-R2-L211-03-T01|C10-R2-L211-04-T01|C10-R2-L211-05-T01|C10-R2-L211-06-T01",7,6,3,medium,canonical_shadow_only,"not production; v12 residual candidate"
shadow_weight,c10_result_only_green_cap,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Cap late result-only memory equipment Green below Yellow/Watch unless order conversion remains fresh","TES/Jusung false positives show result comment without conversion creates high MAE","C10-R2-L211-04-T01|C10-R2-L211-06-T01",2,2,2,medium,guardrail_shadow_only,"strengthens existing stage3_green_revision_min without changing global threshold"
shadow_weight,c10_4b_after_local_peak_late_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"If 4B overlay appears only after price has fallen below Stage2 entry, mark as late protection not good timing","PSK overlay proximity -0.38 and MAE180 -46.29 from 4B entry","C10-R2-L211-05-T02",1,0,1,low,4b_timing_shadow_only,"timing audit row, not representative aggregate"
```

## 24. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C10-R2-L211-01","symbol":"092870","company_name":"엑시콘","round":"R2","loop":"211","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_CAPEX_EQUIPMENT_ORDER_CONVERSION_AND_FALSE_RECOVERY_GUARD","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"MFE180은 매우 강했지만 90D MAE가 -27%라 C10에서는 order-conversion 확인 전 포지션 사이징/MAE guard가 필요하다."}
{"row_type":"trigger","trigger_id":"C10-R2-L211-01-T01","case_id":"C10-R2-L211-01","symbol":"092870","company_name":"엑시콘","round":"R2","loop":"211","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_CAPEX_EQUIPMENT_ORDER_CONVERSION_AND_FALSE_RECOVERY_GUARD","sector":"semiconductor_memory_equipment_and_consumables","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"counterexample_mining; residual_false_positive_mining; residual_missed_structural_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-25","evidence_available_at_that_date":"2023-08 IR/리서치에서 메모리 테스터·DDR5·신제품 개발/사업현황이 확인되었고, 단순 업황 바닥이 아니라 tester generation change가 붙은 회복 신호였다.","evidence_source":"IRGO 092870 IR Room; KIRS 2023-08 Exicon report","evidence_url":"https://m.irgo.co.kr/IR-ROOM/092870/-IR-ROOM | https://w4.kirs.or.kr/download/research/230816_Exicon_.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/092/092870/2023.csv","profile_path":"atlas/symbol_profiles/092/092870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-28","entry_price":14890.0,"MFE_30D_pct":10.81,"MFE_90D_pct":57.15,"MFE_180D_pct":137.74,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.04,"MAE_90D_pct":-27.47,"MAE_180D_pct":-27.47,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-02","peak_price":35400.0,"drawdown_after_peak_pct":-48.64,"window_end_180D":"2024-05-24","green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_not_full_4B","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"memory_tester_generation_change_positive_but_high_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; 1Y window blocked by 2024-07-31 corporate-action candidate","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_092870_2023-08-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_plus_c10_shadow_gate","case_id":"C10-R2-L211-01","trigger_id":"C10-R2-L211-01-T01","symbol":"092870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"memory_cycle_score":22,"order_conversion_score":14,"margin_revision_score":12,"relative_strength_score":14,"execution_risk_score":10,"valuation_risk_score":8},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"memory_cycle_score":22,"order_conversion_score":24,"margin_revision_score":14,"relative_strength_score":14,"execution_risk_score":8,"valuation_risk_score":8},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable/Stage3-Yellow kept","changed_components":["c10_memory_order_conversion_freshness_ladder","result_only_green_cap","high_mae_watch_guard"],"component_delta_explanation":"C10 shadow separates order/customer conversion from result-only memory cycle narrative; high-MAE counterexamples are capped below Green unless conversion freshness exists.","MFE_90D_pct":57.15,"MAE_90D_pct":-27.47,"score_return_alignment_label":"improved_alignment_after_c10_order_conversion_gate","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C10-R2-L211-02","symbol":"084370","company_name":"유진테크","round":"R2","loop":"211","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_CAPEX_EQUIPMENT_ORDER_CONVERSION_AND_FALSE_RECOVERY_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C10에서 단순 memory-price bottom이 아니라 customer/process route가 붙으면 early Stage2가 작동할 수 있음을 보여준다."}
{"row_type":"trigger","trigger_id":"C10-R2-L211-02-T01","case_id":"C10-R2-L211-02","symbol":"084370","company_name":"유진테크","round":"R2","loop":"211","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_CAPEX_EQUIPMENT_ORDER_CONVERSION_AND_FALSE_RECOVERY_GUARD","sector":"semiconductor_memory_equipment_and_consumables","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"counterexample_mining; residual_false_positive_mining; residual_missed_structural_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-14","evidence_available_at_that_date":"2023-08 IR 일정과 리서치에서 2024년 장비 포트폴리오 회복, 반도체 장비 매출 발생 경로가 제시됐다. 이후 MFE180 +80.34%, MAE180 -5.38%로 가장 깨끗한 structural success다.","evidence_source":"IRGO 084370 IR page; iM Securities 2023-08 report","evidence_url":"https://m.irgo.co.kr/IR-COMP/084370/%EC%9C%A0%EC%A7%84%ED%85%8C%ED%81%AC-IR-PAGE | https://www.imfnsec.com/upload/R_E08/2023/08/%5B04155206%5D_084370.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","backlog_or_delivery_visibility"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084370/2023.csv","profile_path":"atlas/symbol_profiles/084/084370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-16","entry_price":32550.0,"MFE_30D_pct":36.56,"MFE_90D_pct":46.7,"MFE_180D_pct":80.34,"MFE_1Y_pct":84.33,"MFE_2Y_pct":null,"MAE_30D_pct":-5.38,"MAE_90D_pct":-5.38,"MAE_180D_pct":-5.38,"MAE_1Y_pct":-5.38,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-07","peak_price":58700.0,"drawdown_after_peak_pct":-16.18,"window_end_180D":"2024-05-13","green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_not_full_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"dram_process_equipment_recovery_structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_084370_2023-08-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_plus_c10_shadow_gate","case_id":"C10-R2-L211-02","trigger_id":"C10-R2-L211-02-T01","symbol":"084370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"memory_cycle_score":22,"order_conversion_score":14,"margin_revision_score":12,"relative_strength_score":14,"execution_risk_score":10,"valuation_risk_score":8},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"memory_cycle_score":22,"order_conversion_score":24,"margin_revision_score":14,"relative_strength_score":14,"execution_risk_score":8,"valuation_risk_score":8},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable/Stage3-Yellow kept","changed_components":["c10_memory_order_conversion_freshness_ladder","result_only_green_cap","high_mae_watch_guard"],"component_delta_explanation":"C10 shadow separates order/customer conversion from result-only memory cycle narrative; high-MAE counterexamples are capped below Green unless conversion freshness exists.","MFE_90D_pct":46.7,"MAE_90D_pct":-5.38,"score_return_alignment_label":"improved_alignment_after_c10_order_conversion_gate","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C10-R2-L211-03","symbol":"281820","company_name":"케이씨텍","round":"R2","loop":"211","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_CAPEX_EQUIPMENT_ORDER_CONVERSION_AND_FALSE_RECOVERY_GUARD","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"C10 rule이 너무 보수적이면 지연 문구가 포함된 mixed report에서도 실제 DRAM CMP/material turn을 놓친다."}
{"row_type":"trigger","trigger_id":"C10-R2-L211-03-T01","case_id":"C10-R2-L211-03","symbol":"281820","company_name":"케이씨텍","round":"R2","loop":"211","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_CAPEX_EQUIPMENT_ORDER_CONVERSION_AND_FALSE_RECOVERY_GUARD","sector":"semiconductor_memory_equipment_and_consumables","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"counterexample_mining; residual_false_positive_mining; residual_missed_structural_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2024-11-29","evidence_available_at_that_date":"2024-11 리서치/IR에서 소재는 견조하고 장비는 지연되는 혼합 신호가 동시에 보였다. 지연 문구만 보면 보수적이지만 DRAM CMP/material turn이 실제 180D MFE +51.09%로 이어졌다.","evidence_source":"IRGO 281820 IR page; public broker report dated 2024-11-29","evidence_url":"https://m.irgo.co.kr/IR-COMP/281820/%EC%BC%80%EC%9D%B4%EC%94%A8%ED%85%8D-IR-PAGE","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources","mixed_delay_but_conversion_route"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv","profile_path":"atlas/symbol_profiles/281/281820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-12-02","entry_price":27400.0,"MFE_30D_pct":34.12,"MFE_90D_pct":51.09,"MFE_180D_pct":51.09,"MFE_1Y_pct":68.43,"MFE_2Y_pct":null,"MAE_30D_pct":-8.21,"MAE_90D_pct":-17.15,"MAE_180D_pct":-17.15,"MAE_1Y_pct":-17.15,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-18","peak_price":41400.0,"drawdown_after_peak_pct":-45.17,"window_end_180D":"2025-08-28","green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_not_full_4B","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"mixed_delay_report_missed_dram_cmp_repricing","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_281820_2024-12-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_plus_c10_shadow_gate","case_id":"C10-R2-L211-03","trigger_id":"C10-R2-L211-03-T01","symbol":"281820","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"memory_cycle_score":22,"order_conversion_score":14,"margin_revision_score":12,"relative_strength_score":14,"execution_risk_score":10,"valuation_risk_score":8},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"memory_cycle_score":22,"order_conversion_score":24,"margin_revision_score":14,"relative_strength_score":14,"execution_risk_score":8,"valuation_risk_score":8},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable/Stage3-Yellow kept","changed_components":["c10_memory_order_conversion_freshness_ladder","result_only_green_cap","high_mae_watch_guard"],"component_delta_explanation":"C10 shadow separates order/customer conversion from result-only memory cycle narrative; high-MAE counterexamples are capped below Green unless conversion freshness exists.","MFE_90D_pct":51.09,"MAE_90D_pct":-17.15,"score_return_alignment_label":"improved_alignment_after_c10_order_conversion_gate","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"case","case_id":"C10-R2-L211-04","symbol":"095610","company_name":"테스","round":"R2","loop":"211","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_CAPEX_EQUIPMENT_ORDER_CONVERSION_AND_FALSE_RECOVERY_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage3-Green","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_high_mae_failure","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"이미 실적으로 확인된 후 Green 처리하면 cycle peak 뒤 결과만 산다. C10에서는 result-confirmed Green보다 order conversion freshness가 우선이다."}
{"row_type":"trigger","trigger_id":"C10-R2-L211-04-T01","case_id":"C10-R2-L211-04","symbol":"095610","company_name":"테스","round":"R2","loop":"211","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_CAPEX_EQUIPMENT_ORDER_CONVERSION_AND_FALSE_RECOVERY_GUARD","sector":"semiconductor_memory_equipment_and_consumables","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"counterexample_mining; residual_false_positive_mining; residual_missed_structural_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test","trigger_type":"Stage3-Green","trigger_date":"2021-08-13","evidence_available_at_that_date":"1Q21/2Q21 실적과 supercycle 수요가 이미 결과로 확인된 뒤의 Green은 늦었다. 실적 숫자는 강했지만 forward return은 MFE180 +5.80%, MAE180 -16.52%에 그쳤다.","evidence_source":"IRGO 095610 2021-08 2Q21 result presentation; public 1Q21 result review","evidence_url":"https://m.irgo.co.kr/IR-COMP/095610/%ED%85%8C%EC%8A%A4-IR-PAGE","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["result_only_late_cycle","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095610/2021.csv","profile_path":"atlas/symbol_profiles/095/095610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-08-17","entry_price":28450.0,"MFE_30D_pct":5.8,"MFE_90D_pct":5.8,"MFE_180D_pct":5.8,"MFE_1Y_pct":5.8,"MFE_2Y_pct":null,"MAE_30D_pct":-11.42,"MAE_90D_pct":-14.76,"MAE_180D_pct":-16.52,"MAE_1Y_pct":-34.97,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-23","peak_price":30100.0,"drawdown_after_peak_pct":-21.1,"window_end_180D":"2022-05-11","green_lateness_ratio":"late_result_green_trap","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_not_full_4B","four_b_evidence_type":["result_only_late_cycle","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_supercycle_result_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_095610_2021-08-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_plus_c10_shadow_gate","case_id":"C10-R2-L211-04","trigger_id":"C10-R2-L211-04-T01","symbol":"095610","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"memory_cycle_score":22,"order_conversion_score":14,"margin_revision_score":12,"relative_strength_score":14,"execution_risk_score":10,"valuation_risk_score":8},"weighted_score_before":86,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"memory_cycle_score":17,"order_conversion_score":12,"margin_revision_score":8,"relative_strength_score":14,"execution_risk_score":14,"valuation_risk_score":12},"weighted_score_after":78,"stage_label_after":"capped_below_Green_or_watch","changed_components":["c10_memory_order_conversion_freshness_ladder","result_only_green_cap","high_mae_watch_guard"],"component_delta_explanation":"C10 shadow separates order/customer conversion from result-only memory cycle narrative; high-MAE counterexamples are capped below Green unless conversion freshness exists.","MFE_90D_pct":5.8,"MAE_90D_pct":-14.76,"score_return_alignment_label":"improved_alignment_after_c10_order_conversion_gate","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C10-R2-L211-05","symbol":"319660","company_name":"피에스케이","round":"R2","loop":"211","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_CAPEX_EQUIPMENT_ORDER_CONVERSION_AND_FALSE_RECOVERY_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_high_mae_failure","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"초기 MFE가 +23%라 단기 성공처럼 보이지만 cycle unwind가 더 컸다. 4B overlay가 늦으면 손실 방어가 실패한다."}
{"row_type":"trigger","trigger_id":"C10-R2-L211-05-T01","case_id":"C10-R2-L211-05","symbol":"319660","company_name":"피에스케이","round":"R2","loop":"211","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_CAPEX_EQUIPMENT_ORDER_CONVERSION_AND_FALSE_RECOVERY_GUARD","sector":"semiconductor_memory_equipment_and_consumables","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"counterexample_mining; residual_false_positive_mining; residual_missed_structural_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-30","evidence_available_at_that_date":"2024-05 코스닥 글로벌 세그먼트/사업현황성 IR은 회복 기대를 만들었지만 90D 이후 MAE가 -35%를 넘고 180D MAE가 -51%까지 악화됐다.","evidence_source":"IRGO 319660 IR page","evidence_url":"https://m.irgo.co.kr/IR-COMP/319660/%ED%94%BC%EC%97%90%EC%8A%A4%EC%BC%80%EC%9D%B4-IR-PAGE","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv","profile_path":"atlas/symbol_profiles/319/319660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-31","entry_price":31750.0,"MFE_30D_pct":23.15,"MFE_90D_pct":23.15,"MFE_180D_pct":23.15,"MFE_1Y_pct":23.15,"MFE_2Y_pct":null,"MAE_30D_pct":-3.94,"MAE_90D_pct":-35.43,"MAE_180D_pct":-51.02,"MAE_1Y_pct":-51.02,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":39100.0,"drawdown_after_peak_pct":-60.23,"window_end_180D":"2025-02-27","green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_not_full_4B","four_b_evidence_type":["positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"business_status_peak_followed_by_execution_drawdown","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_319660_2024-05-31","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_plus_c10_shadow_gate","case_id":"C10-R2-L211-05","trigger_id":"C10-R2-L211-05-T01","symbol":"319660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"memory_cycle_score":22,"order_conversion_score":14,"margin_revision_score":12,"relative_strength_score":14,"execution_risk_score":10,"valuation_risk_score":8},"weighted_score_before":86,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"memory_cycle_score":17,"order_conversion_score":12,"margin_revision_score":8,"relative_strength_score":14,"execution_risk_score":14,"valuation_risk_score":12},"weighted_score_after":78,"stage_label_after":"capped_below_Green_or_watch","changed_components":["c10_memory_order_conversion_freshness_ladder","result_only_green_cap","high_mae_watch_guard"],"component_delta_explanation":"C10 shadow separates order/customer conversion from result-only memory cycle narrative; high-MAE counterexamples are capped below Green unless conversion freshness exists.","MFE_90D_pct":23.15,"MAE_90D_pct":-35.43,"score_return_alignment_label":"improved_alignment_after_c10_order_conversion_gate","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C10-R2-L211-06","symbol":"036930","company_name":"주성엔지니어링","round":"R2","loop":"211","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_CAPEX_EQUIPMENT_ORDER_CONVERSION_AND_FALSE_RECOVERY_GUARD","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_high_mae_failure","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"MFE180 +20%는 있었지만 MAE180 -35%와 peak 이후 -46% drawdown 때문에 C10 Green은 order/backlog conversion freshness 없이는 제한해야 한다."}
{"row_type":"trigger","trigger_id":"C10-R2-L211-06-T01","case_id":"C10-R2-L211-06","symbol":"036930","company_name":"주성엔지니어링","round":"R2","loop":"211","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_CAPEX_EQUIPMENT_ORDER_CONVERSION_AND_FALSE_RECOVERY_GUARD","sector":"semiconductor_memory_equipment_and_consumables","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"counterexample_mining; residual_false_positive_mining; residual_missed_structural_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2023-11-20","evidence_available_at_that_date":"2023-11 3Q23 실적 코멘트는 result/improvement narrative를 제공했지만 이후 180D MAE가 -35.61%로 열려 단순 실적 코멘트 Green은 위험했다.","evidence_source":"IRGO 036930 IR page","evidence_url":"https://m.irgo.co.kr/IR-COMP/036930/%EC%A3%BC%EC%84%B1%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81-IR-PAGE","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036930/2023.csv","profile_path":"atlas/symbol_profiles/036/036930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-11-21","entry_price":34400.0,"MFE_30D_pct":8.43,"MFE_90D_pct":18.46,"MFE_180D_pct":20.49,"MFE_1Y_pct":20.49,"MFE_2Y_pct":null,"MAE_30D_pct":-9.45,"MAE_90D_pct":-21.8,"MAE_180D_pct":-35.61,"MAE_1Y_pct":-35.9,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-08","peak_price":41450.0,"drawdown_after_peak_pct":-46.56,"window_end_180D":"2024-08-13","green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_not_full_4B","four_b_evidence_type":["price_only_local_peak","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"result_comment_local_rally_high_mae_failure","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_036930_2023-11-21","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_plus_c10_shadow_gate","case_id":"C10-R2-L211-06","trigger_id":"C10-R2-L211-06-T01","symbol":"036930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"memory_cycle_score":22,"order_conversion_score":14,"margin_revision_score":12,"relative_strength_score":14,"execution_risk_score":10,"valuation_risk_score":8},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"memory_cycle_score":17,"order_conversion_score":12,"margin_revision_score":8,"relative_strength_score":14,"execution_risk_score":14,"valuation_risk_score":12},"weighted_score_after":78,"stage_label_after":"capped_below_Green_or_watch","changed_components":["c10_memory_order_conversion_freshness_ladder","result_only_green_cap","high_mae_watch_guard"],"component_delta_explanation":"C10 shadow separates order/customer conversion from result-only memory cycle narrative; high-MAE counterexamples are capped below Green unless conversion freshness exists.","MFE_90D_pct":18.46,"MAE_90D_pct":-21.8,"score_return_alignment_label":"improved_alignment_after_c10_order_conversion_gate","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"trigger","trigger_id":"C10-R2-L211-05-T02","case_id":"C10-R2-L211-05","symbol":"319660","company_name":"피에스케이","round":"R2","loop":"211","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_CAPEX_EQUIPMENT_ORDER_CONVERSION_AND_FALSE_RECOVERY_GUARD","sector":"semiconductor_memory_equipment_and_consumables","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-08-19","evidence_available_at_that_date":"2024-08 사업현황성 IR 이후, local peak가 이미 통과된 상태에서 margin/order slowdown risk를 4B overlay로 검증했다.","evidence_source":"IRGO 319660 IR page","evidence_url":"https://m.irgo.co.kr/IR-COMP/319660/%ED%94%BC%EC%97%90%EC%8A%A4%EC%BC%80%EC%9D%B4-IR-PAGE","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv","profile_path":"atlas/symbol_profiles/319/319660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-20","entry_price":28950.0,"MFE_30D_pct":6.39,"MFE_90D_pct":6.39,"MFE_180D_pct":6.39,"MFE_1Y_pct":6.39,"MFE_2Y_pct":null,"MAE_30D_pct":-29.19,"MAE_90D_pct":-46.29,"MAE_180D_pct":-46.29,"MAE_1Y_pct":-46.29,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-20","peak_price":30800.0,"drawdown_after_peak_pct":-49.51,"window_end_180D":"2025-05-19","green_lateness_ratio":"not_applicable:4B_overlay","four_b_local_peak_proximity":-0.38,"four_b_full_window_peak_proximity":-0.38,"four_b_timing_verdict":"late_after_local_peak_not_protective","four_b_evidence_type":["positioning_overheat","margin_or_backlog_slowdown","price_only_local_peak"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"stage4b_overlay_too_late_after_local_peak","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_319660_2024-08-20","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_same_case_stage4b_overlay_new_timing_path","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"aggregate_metric","round":"R2","loop":"211","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","representative_trigger_count":6,"calibration_usable_trigger_count":7,"positive_case_count":3,"counterexample_count":3,"avg_MFE_90D_pct":33.73,"avg_MAE_90D_pct":-20.33,"avg_MFE_180D_pct":53.1,"avg_MAE_180D_pct":-25.53,"positive_avg_MFE_180D_pct":89.72,"counterexample_avg_MAE_180D_pct":-34.38,"alignment_note":"C10 winners show order/customer/fine-node conversion; losers show result-only or local-peak cycle narrative with MAE expansion."}
{"row_type":"residual_contribution","round":"R2","loop":"211","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":2,"same_archetype_new_symbol_count":2,"same_archetype_new_trigger_family_count":6,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["result_only_memory_green_false_positive","mixed_delay_missed_structural","4B_overlay_too_late_after_local_peak","high_mae_success_sizing_problem"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 25. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Rules
1. Use only `calibration_usable=true` rows for quantitative calibration.
2. Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
3. Deduplicate `same_entry_group_id` and representative rows.
4. Treat 4B rows as overlay/risk calibration only.
5. Do not change production scoring unless the user explicitly requests a later promotion batch.
6. Preserve global calibrated profile unless multiple independent MDs support a global change.
7. For this MD, add only a shadow candidate: `c10_memory_order_conversion_freshness_ladder`.

### Expected repository tasks
- Parse `case`, `trigger`, `score_simulation`, `aggregate_metric`, and `residual_contribution` rows.
- Validate Stock-Web price source fields.
- Validate `large_sector_id` and `canonical_archetype_id` mapping.
- Report accepted/rejected rows, new sector/archetype coverage, and strengthened/kept axes.
- Do not output current stock recommendations.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 211
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 / balance-quality reinforcement + Priority 0 direct URL and MFE/MAE repair
next_recommended_archetypes = C05/C01/C13/C15 only for direct URL or MFE/MAE repair; R13 only for duplicate compression or cross-archetype high-MAE taxonomy; C10 should re-enter only with new direct order-conversion source rows.
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-repeat index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- Evidence source URLs are stored per trigger row in the JSONL machine-readable block.
