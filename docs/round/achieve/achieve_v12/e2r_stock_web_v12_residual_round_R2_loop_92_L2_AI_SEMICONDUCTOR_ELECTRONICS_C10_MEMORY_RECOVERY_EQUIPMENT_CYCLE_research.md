# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 92
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_GENERIC_WAFER_CAPEX_BETA_FADE
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This MD does not re-propose the already applied global Stage2 bonus or Green lateness axis. It tests the residual C10 problem: **generic memory recovery beta can look like an equipment-cycle signal, but only order/customer/revision conversion separates durable equipment recovery from a beta fade.**

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R2 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE |
| fine_archetype_id | MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_GENERIC_WAFER_CAPEX_BETA_FADE |
| expected round-sector pair | R2 → L2 |
| round_sector_consistency | pass |

C10 is not the HBM customer-capacity archetype (C06), and not the HBM equipment relative-strength archetype (C07). This loop compresses cases where the first observable signal is **memory-cycle recovery / wafer-capex recovery / test-equipment cycle recovery**, and asks whether the signal is confirmed by order, customer, revision, and margin conversion.

## 3. Previous Coverage / Duplicate Avoidance Check

The no-repeat ledger marks C10 as Priority 0 with 21 rows and a 9-row shortage to the 30-row minimum. Its current top-covered C10 symbols include 036930 and 074600, so this loop avoids those and adds three symbol/trigger-family expansions.

| selected symbol | company | previous C10 top-covered? | use in this loop | novelty reason |
|---|---|---:|---|---|
| 089030 | 테크윙 | no | positive | memory test-handler recovery with strong order/revenue conversion proxy |
| 319660 | 피에스케이 | no | positive/high-MAE success | wafer equipment recovery with later fade; separates early Stage2 from full Green |
| 240810 | 원익IPS | no | counterexample | generic memory-capex beta spike without durable order/margin bridge |

Hard duplicate avoided:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
C10 + 089030 + Stage2-Actionable + 2024-02-08 = new
C10 + 319660 + Stage2-Actionable + 2024-02-29 = new
C10 + 240810 + Stage2-Actionable + 2024-02-29 = new
C10 + 240810 + Stage4B-Watch + 2024-04-08 = new overlay
```

## 4. Stock-Web OHLC Input / Price Source Validation

| item | value |
|---|---|
| source | Songdaiki/stock-web |
| source basis | FinanceData/marcap transformed into symbol-year CSV shards |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| manifest_max_date | 2026-02-20 |
| validation_status | usable_for_historical_calibration |

Symbol profile checks:

| symbol | profile_path | first_date | last_date | status_inferred | corporate action caveat |
|---|---|---:|---:|---|---|
| 089030 | atlas/symbol_profiles/089/089030.json | 2011-11-10 | 2026-02-20 | active_like | corporate-action windows blocked by default |
| 319660 | atlas/symbol_profiles/319/319660.json | 2019-05-10 | 2026-02-20 | active_like | corporate-action windows blocked by default |
| 240810 | atlas/symbol_profiles/240/240810.json | 2016-05-02 | 2026-02-20 | active_like | clean recent window; no corporate-action candidates in profile |

## 5. Historical Eligibility Gate

| case_id | trigger_date | entry_date | entry in shard | forward 180 trading days | clean 180D window | calibration_usable |
|---|---:|---:|---|---|---|---|
| C10_089030_20240208 | 2024-02-08 | 2024-02-08 | yes | yes | yes | true |
| C10_319660_20240229 | 2024-02-29 | 2024-02-29 | yes | yes | yes | true |
| C10_240810_20240229 | 2024-02-29 | 2024-02-29 | yes | yes | yes | true |

## 6. Canonical Archetype Compression Map

| symbol | surface theme | compressed C10 interpretation | not this archetype |
|---|---|---|---|
| 089030 | HBM/test-handler momentum | memory recovery equipment cycle with repeatable equipment demand conversion | not pure C07 because this row tests cycle conversion, not just relative strength |
| 319660 | wafer equipment/etch-clean recovery | memory capex cycle recovery with later drawdown risk | not C09 because valuation blowoff is secondary; order-cycle confirmation is primary |
| 240810 | wafer equipment capex beta | generic memory recovery beta without enough order/margin durability | not C07 because no specific HBM-equipment relative-strength bridge is used |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | positive_or_counterexample | best_trigger | short thesis |
|---|---|---|---|---|---|---|
| C10_089030_20240208 | 089030 | 테크윙 | structural_success | positive | Stage2-Actionable | Memory test-handler recovery signal converted into a large, low-MAE equipment-cycle move. |
| C10_319660_20240229 | 319660 | 피에스케이 | high_mae_success | positive | Stage2-Actionable | Early wafer-equipment recovery was useful but later cycle fade means Green should wait for revision/order confirmation. |
| C10_240810_20240229 | 240810 | 원익IPS | failed_rerating | counterexample | Stage2-Actionable | Generic memory-capex beta gave a tradable local rally, then failed as a durable C10 rerating without margin/order bridge. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
minimum_positive_case_count = 1
minimum_counterexample_count = 1
positive_counterexample_balance_status = pass
```

## 9. Evidence Source Map

Evidence is proxy-scored at trigger date. This is not live candidate research and does not assert the current investment attractiveness of any symbol.

| evidence field | 089030 | 319660 | 240810 |
|---|---|---|---|
| public_event_or_disclosure | memory/HBM test-equipment cycle proxy | wafer equipment cycle proxy | generic memory capex beta |
| customer_or_order_quality | high | medium | low-to-medium |
| backlog_or_delivery_visibility | medium | medium | weak at trigger |
| early_revision_signal | medium | medium | weak |
| margin_bridge | medium | medium | weak |
| price-only risk | low at entry | medium after local peak | high after local peak |
| evidence_source_quality | source_proxy_only | source_proxy_only | source_proxy_only |

## 10. Price Data Source Map

| symbol | entry shard | profile path | entry row observed in stock-web | later path observed |
|---|---|---|---|---|
| 089030 | atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv | atlas/symbol_profiles/089/089030.json | 2024-02-08 close 17,400 | peak high near 70,800 around 2024-07-11 |
| 319660 | atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv | atlas/symbol_profiles/319/319660.json | 2024-02-29 close 25,400 | peak high near 40,300 around 2024-07-04, later large drawdown |
| 240810 | atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv | atlas/symbol_profiles/240/240810.json | 2024-02-29 close 32,800 | local high 44,850, then 2024-11 drawdown toward 22,200 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | evidence_available_at_that_date | trigger_family |
|---|---|---|---:|---:|---:|---|---|
| C10_089030_S2A_20240208 | 089030 | Stage2-Actionable | 2024-02-08 | 2024-02-08 | 17400 | test-handler/memory recovery proxy + relative strength | memory_test_handler_recovery |
| C10_319660_S2A_20240229 | 319660 | Stage2-Actionable | 2024-02-29 | 2024-02-29 | 25400 | wafer equipment recovery proxy + volume expansion | wafer_equipment_recovery |
| C10_240810_S2A_20240229 | 240810 | Stage2-Actionable | 2024-02-29 | 2024-02-29 | 32800 | memory capex beta + local equipment rally | generic_wafer_capex_beta |
| C10_240810_4B_20240408 | 240810 | Stage4B-Watch | 2024-04-08 | 2024-04-08 | 41650 | local blowoff after beta rally; non-price evidence insufficient | price_only_local_4B_watch |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger metrics

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C10_089030_S2A_20240208 | 17400 | 31.6 | 0.0 | 208.6 | 0.0 | 306.9 | 0.0 | 2024-07-11 | 70800 | -51.7 | strong_success_low_MAE |
| C10_319660_S2A_20240229 | 25400 | 21.3 | -0.4 | 58.7 | -0.4 | 58.7 | -19.7 | 2024-07-04 | 40300 | -49.4 | high_MAE_success |
| C10_240810_S2A_20240229 | 32800 | 32.3 | -2.3 | 36.7 | -2.3 | 36.7 | -32.3 | 2024-04-08 | 44850 | -50.5 | failed_durable_rerating |

### 12.2 Overlay trigger metrics

| trigger_id | entry_price | local_peak | full_window_peak | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---:|---:|---:|---|
| C10_240810_4B_20240408 | 41650 | 44850 | 44850 | 0.93 | 0.93 | useful_local_4B_watch_but_not_full_4B_without_non_price_evidence |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely action | actual path | current_profile_verdict | residual error |
|---|---|---|---|---|
| C10_089030_20240208 | Stage2-Actionable/Yellow allowed | very high MFE and low MAE | current_profile_correct | none |
| C10_319660_20240229 | Stage2-Actionable allowed; Green should wait | good MFE but later large drawdown | current_profile_too_early | Stage2 was useful, Green would require stricter revision/order confirmation |
| C10_240810_20240229 | Stage2-Actionable may be allowed if beta over-weighted | local MFE but poor 180D durability | current_profile_false_positive | generic memory beta should not become durable C10 positive without order/margin bridge |

Answers to required stress-test questions:

```text
1. current calibrated profile 판단: 089030 correct, 319660 partially too early, 240810 false-positive risk.
2. actual MFE/MAE alignment: positive for 089030; mixed for 319660; poor durable alignment for 240810.
3. Stage2 bonus: useful only when order/customer/revision bridge exists; over-generous for generic wafer-capex beta.
4. Yellow 75: acceptable; should require C10 bridge components, not just price/sector beta.
5. Green 87/revision 55: keep strict; do not loosen for C10.
6. price-only blowoff guard: appropriate.
7. full 4B non-price requirement: appropriate; 240810 remains 4B-watch, not full 4B, without non-price confirmation.
8. hard 4C routing: no hard 4C in this loop; drawdown is beta fade rather than thesis-break evidence.
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2-Actionable timing | Yellow timing | Green timing | green_lateness_ratio | conclusion |
|---|---|---|---|---:|---|
| C10_089030_20240208 | timely | timely if order/revenue bridge scored | no confirmed Green row used | not_applicable | Stage2 is enough for early calibration; Green requires later revision confirmation |
| C10_319660_20240229 | useful but volatile | should be cautious | should not be automatic | not_applicable | classify as high-MAE success, not clean Green |
| C10_240810_20240229 | too permissive if driven by beta only | should remain watch-only | no Green | not_applicable | needs order/margin bridge before positive promotion |

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| 240810 | price_only | 0.93 | 0.93 | local watch is valid, but price-only 4B cannot define full 4B |
| 319660 | price_only / cycle fade | not primary row | not primary row | decline after peak supports keeping non-price requirement |
| 089030 | none at Stage2 | n/a | n/a | no 4B calibration proposed |

## 16. 4C Protection Audit

```text
four_c_protection_score = not_computed
reason = no hard thesis-break 4C row in this loop
label = thesis_break_watch_only
```

The 240810 case is a beta-fade counterexample, not a hard 4C thesis break. It should strengthen Stage2 bridge and 4B-watch guards, not hard-route to 4C.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
candidate_axis = l2_memory_recovery_equipment_requires_order_or_revision_bridge
```

Rule candidate:

> In L2 semiconductor equipment, memory-recovery beta alone may unlock Stage1/Watch, but Stage2-Actionable requires at least one non-price bridge among customer/order quality, shipment/capex conversion, early revision, or margin bridge.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
new_axis_proposed = c10_order_revision_bridge_required_for_stage2_actionable_shadow_only
```

C10-specific shadow rule:

```text
if canonical_archetype_id == C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:
    Stage2-Actionable positive calibration requires:
        memory_recovery_signal == true
        AND at least one of:
            order_intake_quality_score >= medium
            customer_quality_score >= medium
            revision_score >= medium
            margin_bridge_score >= medium
    otherwise:
        treat as watch-only or beta-counterexample
```

## 19. Before / After Backtest Comparison

| profile_id | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 101.3 | -0.9 | 33.3% | 0 | good upside capture but one beta false positive |
| P0b e2r_2_0_baseline_reference | 3 | 101.3 | -0.9 | 66.7% | 1 | too sensitive to theme beta |
| P1 sector_specific_candidate_profile | 3 | 133.7 | -0.2 | 0.0% | 0 | improves beta filtering |
| P2 canonical_archetype_candidate_profile | 3 | 133.7 | -0.2 | 0.0% | 0 | best alignment for C10 |
| P3 counterexample_guard_profile | 3 | 101.3 | -0.9 | 0.0% | 1 | safer but may delay 319660-style high-MAE success |

## 20. Score-Return Alignment Matrix

| case_id | raw score before | weighted score before | stage before | proposed score after | stage after | alignment |
|---|---:|---:|---|---:|---|---|
| C10_089030_20240208 | 73 | 75 | Stage2-Actionable | 79 | Stage2-Actionable / Yellow-watch | aligned |
| C10_319660_20240229 | 70 | 72 | Stage2-Actionable | 74 | Stage2-Actionable but Green-blocked | improved |
| C10_240810_20240229 | 68 | 70 | Stage2-Actionable | 63 | Watch-only | improved |

Component explanation:

```text
089030: strong relative_strength_score + customer_quality/order_intake proxy support Stage2.
319660: equipment cycle proxy supports Stage2, but revision/margin bridge not enough for Green.
240810: valuation_repricing and relative_strength exist, but customer_quality/order_intake/margin bridge are weak; beta-only Stage2 should be blocked.
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_GENERIC_WAFER_CAPEX_BETA_FADE | 2 | 1 | 1 | 0 | 3 | 0 | 4 | 3 | 2 | true | true | C10 21→24 synthetic coverage; still below 30 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - beta_false_positive
  - green_should_wait_for_revision_bridge
  - price_only_local_4b_watch_not_full_4b
new_axis_proposed: c10_order_revision_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C10 memory equipment beta rallies
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- stock-web 1D OHLC path for selected historical dates
- entry_date / entry_price checks
- 30D/90D/180D MFE/MAE proxy calculations
- C10-specific positive/counterexample balance
- current calibrated profile stress test
```

Non-validation scope:

```text
- no live candidate scan
- no production scoring change
- no brokerage/trading action
- no stock_agent source-code patch
- no claim that source_proxy evidence is sufficient for promotion without later URL verification
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c10_order_revision_bridge_required_for_stage2_actionable,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Blocks beta-only memory equipment Stage2 while preserving order/revision-backed equipment recovery","240810 false positive blocked; 089030/319660 retained as Stage2","C10_089030_S2A_20240208|C10_319660_S2A_20240229|C10_240810_S2A_20240229",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c10_green_requires_revision_or_margin_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Prevents high-MAE equipment-cycle successes from being promoted to Green too early","319660 remains useful Stage2 but Green-blocked until revision/margin bridge","C10_319660_S2A_20240229",1,1,0,low,canonical_shadow_only,"Green threshold not loosened"
shadow_weight,c10_price_only_local_4b_watch_only,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Keeps local price blowoff as watch overlay, not full 4B without non-price evidence","240810 4B overlay classified as watch-only","C10_240810_4B_20240408",1,1,1,medium,canonical_shadow_only,"supports existing full_4b_requires_non_price_evidence"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C10_089030_20240208","symbol":"089030","company_name":"테크윙","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_GENERIC_WAFER_CAPEX_BETA_FADE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Memory test-handler recovery converted into high MFE and low MAE path."}
{"row_type":"case","case_id":"C10_319660_20240229","symbol":"319660","company_name":"피에스케이","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_GENERIC_WAFER_CAPEX_BETA_FADE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"partially_aligned_high_mae","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Stage2 useful, but Green should wait for revision/order bridge due to later drawdown."}
{"row_type":"case","case_id":"C10_240810_20240229","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_GENERIC_WAFER_CAPEX_BETA_FADE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"local_mfe_but_failed_durable_rerating","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Generic memory capex beta rallied but lacked durable order/revision/margin bridge."}
{"row_type":"trigger","trigger_id":"C10_089030_S2A_20240208","case_id":"C10_089030_20240208","symbol":"089030","company_name":"테크윙","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_GENERIC_WAFER_CAPEX_BETA_FADE","loop_objective":"coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-08","entry_date":"2024-02-08","entry_price":17400,"evidence_available_at_that_date":"memory/HBM test-equipment recovery proxy and relative strength","evidence_source":"source_proxy_only","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.6,"MFE_90D_pct":208.6,"MFE_180D_pct":306.9,"MAE_30D_pct":0.0,"MAE_90D_pct":0.0,"MAE_180D_pct":0.0,"peak_date":"2024-07-11","peak_price":70800,"drawdown_after_peak_pct":-51.7,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"strong_success_low_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_089030_20240208_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C10_319660_S2A_20240229","case_id":"C10_319660_20240229","symbol":"319660","company_name":"피에스케이","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_GENERIC_WAFER_CAPEX_BETA_FADE","loop_objective":"coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":25400,"evidence_available_at_that_date":"wafer equipment recovery proxy and volume expansion","evidence_source":"source_proxy_only","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv","profile_path":"atlas/symbol_profiles/319/319660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.3,"MFE_90D_pct":58.7,"MFE_180D_pct":58.7,"MAE_30D_pct":-0.4,"MAE_90D_pct":-0.4,"MAE_180D_pct":-19.7,"peak_date":"2024-07-04","peak_price":40300,"drawdown_after_peak_pct":-49.4,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"high_MAE_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_319660_20240229_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C10_240810_S2A_20240229","case_id":"C10_240810_20240229","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_GENERIC_WAFER_CAPEX_BETA_FADE","loop_objective":"counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":32800,"evidence_available_at_that_date":"generic memory capex beta and local equipment rally","evidence_source":"source_proxy_only","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv","profile_path":"atlas/symbol_profiles/240/240810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":32.3,"MFE_90D_pct":36.7,"MFE_180D_pct":36.7,"MAE_30D_pct":-2.3,"MAE_90D_pct":-2.3,"MAE_180D_pct":-32.3,"peak_date":"2024-04-08","peak_price":44850,"drawdown_after_peak_pct":-50.5,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"failed_durable_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_240810_20240229_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C10_240810_4B_20240408","case_id":"C10_240810_20240229","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_GENERIC_WAFER_CAPEX_BETA_FADE","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Watch","trigger_date":"2024-04-08","entry_date":"2024-04-08","entry_price":41650,"evidence_available_at_that_date":"local price blowoff after beta rally; non-price evidence insufficient","evidence_source":"source_proxy_only","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv","profile_path":"atlas/symbol_profiles/240/240810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.7,"MFE_90D_pct":7.7,"MFE_180D_pct":7.7,"MAE_30D_pct":-19.6,"MAE_90D_pct":-19.6,"MAE_180D_pct":-46.7,"peak_date":"2024-04-08","peak_price":44850,"drawdown_after_peak_pct":-50.5,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.93,"trigger_outcome_label":"price_only_local_4B_watch","current_profile_verdict":"current_profile_4B_watch_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_240810_20240408_4b","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_089030_20240208","trigger_id":"C10_089030_S2A_20240208","symbol":"089030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":35,"margin_bridge_score":45,"revision_score":50,"relative_strength_score":80,"customer_quality_score":65,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":30,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":40,"margin_bridge_score":50,"revision_score":55,"relative_strength_score":80,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":25,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":79,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","revision_score","margin_bridge_score"],"component_delta_explanation":"Customer/order and revision bridge preserved; Stage2 retained.","MFE_90D_pct":208.6,"MAE_90D_pct":0.0,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"canonical_archetype_candidate_profile","case_id":"C10_240810_20240229","trigger_id":"C10_240810_S2A_20240229","symbol":"240810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":15,"margin_bridge_score":20,"revision_score":20,"relative_strength_score":75,"customer_quality_score":25,"policy_or_regulatory_score":0,"valuation_repricing_score":60,"execution_risk_score":45,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":15,"margin_bridge_score":20,"revision_score":20,"relative_strength_score":55,"customer_quality_score":20,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":55,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":63,"stage_label_after":"Watch-only","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Beta-only signal loses Stage2 when order/revision/margin bridge is absent.","MFE_90D_pct":36.7,"MAE_90D_pct":-2.3,"score_return_alignment_label":"improved_counterexample_filter","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["beta_false_positive","green_should_wait_for_revision_bridge","price_only_local_4b_watch_not_full_4b"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
next_recommended_archetypes:
  - C14_EV_DEMAND_SLOWDOWN_4B_4C
  - C11_BATTERY_ORDERBOOK_RERATING
  - C02_POWER_GRID_DATACENTER_CAPEX
reason:
  C10 has received this loop, but remains below 30 rows; however the next Priority 0 queue should also continue C14/C11/C02 unless the next runner chooses additional C10 symbol diversity.
```

## 28. Source Notes

```text
stock-web manifest: atlas/manifest.json
089030 profile: atlas/symbol_profiles/089/089030.json
089030 price shard: atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv
319660 profile: atlas/symbol_profiles/319/319660.json
319660 price shard: atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv
240810 profile: atlas/symbol_profiles/240/240810.json
240810 price shard: atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv
no-repeat index: docs/core/V12_Research_No_Repeat_Index.md
```
