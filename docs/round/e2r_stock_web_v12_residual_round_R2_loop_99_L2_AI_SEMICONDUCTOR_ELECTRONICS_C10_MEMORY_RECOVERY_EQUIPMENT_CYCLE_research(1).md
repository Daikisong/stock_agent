# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_99_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
selected_round: R2
selected_loop: 99
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_DEPOSITION_EQUIPMENT_RECOVERY_ORDER_MARGIN_4B_WATCH
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 3 new independent C10 rows and moves C10 from static 21 rows to projected 24 rows. It remains below the 30-row stability threshold.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C10:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS
C10 -> C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

C10 is the memory recovery / equipment cycle archetype. The route is not simply “memory is recovering”; the usable bridge is order conversion, utilization, ASP/mix, margin, revision, and FCF.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| static C10 rows | 21 |
| static C10 symbols | 18 |
| static C10 good/bad Stage2 | 6 / 6 |
| static C10 4B/4C | 3 / 3 |
| static C10 URL pending/proxy | 18 / 12 |
| static top covered symbols | 036930, 074600, 003160, 031980, 036540, 039030 |
| this loop projected rows | 24 |

Selected symbols avoid the static C10 top-covered symbols.

| symbol | company | status |
|---|---|---|
| 095610 | 테스 | new C10 symbol versus static top-covered list |
| 166090 | 하나머티리얼즈 | new C10 symbol versus static top-covered list |
| 083310 | 엘오티베큠 | new C10 symbol versus static top-covered list |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated C10 memory.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 095610 / 2024-03-06 | true | true | clean_180D_window | true |
| 166090 / 2024-03-22 | true | true | clean_180D_window | true |
| 083310 / 2024-02-22 | true | true | clean_180D_window | true |

Corporate-action notes:

- 테스 has corporate-action candidates only in 2011 and 2016.
- 하나머티리얼즈 has corporate-action candidates only in 2018.
- 엘오티베큠 has corporate-action candidates only in 2007.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| MEMORY_DEPOSITION_EQUIPMENT_RECOVERY_ORDER_MARGIN_4B_WATCH | C10 | deposition equipment recovery can open Stage2A, but order/margin conversion must follow |
| MEMORY_PROCESS_PARTS_UTILIZATION_RECOVERY_4B_WATCH | C10 | process-parts utilization recovery can rerate, but late cycle drawdown requires 4B audit |
| VACUUM_EQUIPMENT_MEMORY_RECOVERY_PREMIUM_MARGIN_BRIDGE_FAIL | C10 | equipment-cycle premium without realized order/margin bridge is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C10_TES_095610_2024_03_06_MEMORY_EQUIPMENT_RECOVERY_RERATING_4B | 095610 | 테스 | 4B_overlay_success | positive | deposition/memory equipment recovery produced 58% MFE, then cycle drawdown |
| C10_HANAMATERIALS_166090_2024_03_22_MEMORY_PROCESS_PARTS_CYCLE_RERATING | 166090 | 하나머티리얼즈 | 4B_overlay_success | positive | process-parts recovery produced 32% MFE, then late drawdown |
| C10_LOTVACUUM_083310_2024_02_22_MEMORY_EQUIPMENT_RECOVERY_FALSE_POSITIVE | 083310 | 엘오티베큠 | failed_rerating | counterexample | vacuum equipment premium had only 4.7% MFE and deep MAE |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 095610 | source_proxy_only | memory equipment/deposition order-cycle route | required before promotion |
| 166090 | source_proxy_only | memory process-parts utilization route | required before promotion |
| 083310 | source_proxy_only | vacuum equipment recovery premium but order/margin bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 095610 | atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv | atlas/symbol_profiles/095/095610.json |
| 166090 | atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv | atlas/symbol_profiles/166/166090.json |
| 083310 | atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv | atlas/symbol_profiles/083/083310.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| TES_095610_2024_03_06_STAGE2A_MEMORY_EQUIPMENT_RECOVERY | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 20800 | memory capex recovery / deposition equipment order route |
| HANAMATERIALS_166090_2024_03_22_STAGE2A_MEMORY_PROCESS_PARTS_RECOVERY | Stage2-Actionable | 2024-03-22 | 2024-03-22 | 52200 | memory process-parts utilization recovery |
| LOTVACUUM_083310_2024_02_22_STAGE2_FALSE_POSITIVE_MEMORY_EQUIPMENT_RECOVERY | Stage2 | 2024-02-22 | 2024-02-22 | 23350 | vacuum equipment recovery premium without order/margin bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 095610 | 2024-03-06 | 20800 | 21.15 | -8.85 | 58.17 | -8.85 | 58.17 | -23.08 | 2024-04-17 | 32900 | -51.37 |
| 166090 | 2024-03-22 | 52200 | 17.82 | -2.87 | 32.76 | -8.05 | 32.76 | -45.88 | 2024-07-02 | 69300 | -59.24 |
| 083310 | 2024-02-22 | 23350 | 4.71 | -8.35 | 4.71 | -35.25 | 4.71 | -46.04 | 2024-02-23 | 24450 | -48.47 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 095610 | Stage2A/Yellow possible; 4B after equipment recovery rerating | high MFE then cycle drawdown | current_profile_4B_too_late |
| 166090 | Stage2A possible; 4B after parts/utilization recovery | useful MFE then late drawdown | current_profile_4B_too_late |
| 083310 | Stage2 risk if memory equipment premium is over-credited | low MFE and high MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C10 interpretation:

- Stage2A can work when memory recovery is tied to order conversion, utilization, or margin route.
- Yellow/Green require realized equipment order, OPM, revision, and FCF.
- Recovery theme premium without those bridges should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 095610 | 1.00 | 1.00 | valuation / cycle peak | good 4B audit after equipment recovery rerating |
| 166090 | 1.00 | 1.00 | utilization/cycle peak | 4B audit needed after parts recovery rerating |
| 083310 | 1.00 | 1.00 | event premium / weak follow-through | not Stage3 without order/margin bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 095610 | thesis_break_watch_only | not hard 4C, but 4B cap needed after cycle peak |
| 166090 | thesis_break_watch_only | not hard 4C, but late memory-cycle drawdown needs audit |
| 083310 | hard_4c_late | order/margin/revision bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, memory recovery can support Stage2A only when tied to order conversion, utilization, margin bridge, revision, or FCF. Equipment-cycle or vacuum-equipment premiums without that bridge should not become Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
confidence = medium
```

Candidate C10 rule:

```text
C10_memory_cycle_conversion_bridge_required =
  memory_recovery_or_equipment_cycle_route
  AND (order_conversion OR utilization_bridge OR margin_bridge OR confirmed_revision OR fcf_conversion)

if recovery_premium and conversion_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 25 and drawdown_after_peak < -35:
    add C10_peak_proximity_4B_audit = true

if MFE_90D < 10 and MAE_90D < -25:
    classify_as C10_memory_equipment_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 31.88 | -17.38 | 31.88 | -38.33 | 1 | useful but C10 conversion bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 31.88 | -17.38 | 31.88 | -38.33 | 1 | over-credits recovery theme premiums |
| P1 sector_specific_candidate_profile | L2 | 2 promoted + 1 guard | 45.47 | -8.45 | 45.47 | -34.48 | 0 | better after order/margin bridge gate |
| P2 canonical_archetype_candidate_profile | C10 | 2 promoted + 1 guard | 45.47 | -8.45 | 45.47 | -34.48 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C10 guard | 2 promoted + 1 guard | 45.47 | -8.45 | 45.47 | -34.48 | 0 | adds equipment-cycle false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 095610 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 166090 | Stage2A aligned; late 4B audit needed | current_profile_4B_too_late |
| 083310 | Stage2 false positive if order/margin bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | mixed C10 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | static 21 -> projected 24; still need 6 to reach 30 |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_4B_too_late
  - current_profile_false_positive
new_axis_proposed: C10_memory_cycle_conversion_bridge_required|C10_peak_proximity_4B_audit|C10_memory_equipment_false_positive_guardrail
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Uses stock-web tradable OHLC rows.
- Uses manifest max_date 2026-02-20.
- Uses clean 180D windows.
- Uses C10 Priority 0 coverage gap.
- Avoids static C10 top-covered symbols.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_memory_cycle_conversion_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"083310 shows memory equipment recovery premium can fail without order/margin bridge while 095610/166090 work only as Stage2A with 4B audit","blocks 083310 false positive while preserving 095610/166090 Stage2A","TES_095610_2024_03_06_STAGE2A_MEMORY_EQUIPMENT_RECOVERY|HANAMATERIALS_166090_2024_03_22_STAGE2A_MEMORY_PROCESS_PARTS_RECOVERY|LOTVACUUM_083310_2024_02_22_STAGE2_FALSE_POSITIVE_MEMORY_EQUIPMENT_RECOVERY",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C10_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"095610/166090 memory recovery reratings needed 4B audit after MFE and cycle drawdown","adds 4B audit after large C10 MFE without converting price-only cycle peaks into Green","TES_095610_2024_03_06_STAGE2A_MEMORY_EQUIPMENT_RECOVERY|HANAMATERIALS_166090_2024_03_22_STAGE2A_MEMORY_PROCESS_PARTS_RECOVERY",2,2,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C10_memory_equipment_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"083310 had low MFE and high MAE after memory equipment recovery premium","requires realized order/utilization/margin/revision bridge before Stage2/Yellow promotion","LOTVACUUM_083310_2024_02_22_STAGE2_FALSE_POSITIVE_MEMORY_EQUIPMENT_RECOVERY",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C10_TES_095610_2024_03_06_MEMORY_EQUIPMENT_RECOVERY_RERATING_4B","symbol":"095610","company_name":"테스","round":"R2","loop":"99","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_DEPOSITION_EQUIPMENT_RECOVERY_ORDER_MARGIN_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"TES_095610_2024_03_06_STAGE2A_MEMORY_EQUIPMENT_RECOVERY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"memory equipment recovery / deposition order cycle captured 58% MFE, but later cycle drawdown required C10 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C10 symbol versus static top-covered list; clean 2024 corporate-action window"}
{"row_type":"case","case_id":"C10_HANAMATERIALS_166090_2024_03_22_MEMORY_PROCESS_PARTS_CYCLE_RERATING","symbol":"166090","company_name":"하나머티리얼즈","round":"R2","loop":"99","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_PROCESS_PARTS_UTILIZATION_RECOVERY_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"HANAMATERIALS_166090_2024_03_22_STAGE2A_MEMORY_PROCESS_PARTS_RECOVERY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"memory process-parts utilization recovery captured 32% MFE, but later memory-cycle drawdown demanded 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C10 symbol; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C10_LOTVACUUM_083310_2024_02_22_MEMORY_EQUIPMENT_RECOVERY_FALSE_POSITIVE","symbol":"083310","company_name":"엘오티베큠","round":"R2","loop":"99","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"VACUUM_EQUIPMENT_MEMORY_RECOVERY_PREMIUM_MARGIN_BRIDGE_FAIL","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"LOTVACUUM_083310_2024_02_22_STAGE2_FALSE_POSITIVE_MEMORY_EQUIPMENT_RECOVERY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"vacuum equipment memory-recovery premium had only 4.7% MFE before severe 90D/180D MAE without order/margin bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C10 symbol; counterexample for equipment-cycle beta without realized order/revision/margin conversion"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TES_095610_2024_03_06_STAGE2A_MEMORY_EQUIPMENT_RECOVERY","case_id":"C10_TES_095610_2024_03_06_MEMORY_EQUIPMENT_RECOVERY_RERATING_4B","symbol":"095610","company_name":"테스","round":"R2","loop":"99","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_DEPOSITION_EQUIPMENT_RECOVERY_ORDER_MARGIN_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":20800.0,"evidence_available_at_that_date":"source_proxy_only: memory capex recovery, deposition equipment order-cycle route, customer order visibility, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_capex_recovery","deposition_equipment_order_route","relative_strength","customer_order_visibility"],"stage3_evidence_fields":["order_conversion_partial","margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv","profile_path":"atlas/symbol_profiles/095/095610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.15,"MFE_90D_pct":58.17,"MFE_180D_pct":58.17,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-8.85,"MAE_90D_pct":-8.85,"MAE_180D_pct":-23.08,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-17","peak_price":32900.0,"drawdown_after_peak_pct":-51.37,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_stage2a_but_memory_equipment_cycle_peak_requires_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_095610_2024_03_06_20800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HANAMATERIALS_166090_2024_03_22_STAGE2A_MEMORY_PROCESS_PARTS_RECOVERY","case_id":"C10_HANAMATERIALS_166090_2024_03_22_MEMORY_PROCESS_PARTS_CYCLE_RERATING","symbol":"166090","company_name":"하나머티리얼즈","round":"R2","loop":"99","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_PROCESS_PARTS_UTILIZATION_RECOVERY_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-22","entry_date":"2024-03-22","entry_price":52200.0,"evidence_available_at_that_date":"source_proxy_only: memory utilization recovery, process-parts replacement cycle, customer utilization ramp, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_utilization_recovery","process_parts_cycle","customer_utilization_ramp","relative_strength"],"stage3_evidence_fields":["utilization_bridge_partial","margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv","profile_path":"atlas/symbol_profiles/166/166090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.82,"MFE_90D_pct":32.76,"MFE_180D_pct":32.76,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-2.87,"MAE_90D_pct":-8.05,"MAE_180D_pct":-45.88,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-02","peak_price":69300.0,"drawdown_after_peak_pct":-59.24,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"memory_parts_recovery_worked_but_cycle_peak_and_late_mae_require_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_mfe_with_late_4b_drawdown","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_166090_2024_03_22_52200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"LOTVACUUM_083310_2024_02_22_STAGE2_FALSE_POSITIVE_MEMORY_EQUIPMENT_RECOVERY","case_id":"C10_LOTVACUUM_083310_2024_02_22_MEMORY_EQUIPMENT_RECOVERY_FALSE_POSITIVE","symbol":"083310","company_name":"엘오티베큠","round":"R2","loop":"99","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"VACUUM_EQUIPMENT_MEMORY_RECOVERY_PREMIUM_MARGIN_BRIDGE_FAIL","sector":"AI / semiconductor / electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":23350.0,"evidence_available_at_that_date":"source_proxy_only: vacuum equipment memory-recovery premium and relative-strength spike visible, but realized order, utilization, margin, and revision bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_equipment_recovery_premium","vacuum_equipment_theme","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_spike","weak_follow_through","order_margin_bridge_absent"],"stage4c_evidence_fields":["order_conversion_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv","profile_path":"atlas/symbol_profiles/083/083310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.71,"MFE_90D_pct":4.71,"MFE_180D_pct":4.71,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-8.35,"MAE_90D_pct":-35.25,"MAE_180D_pct":-46.04,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-23","peak_price":24450.0,"drawdown_after_peak_pct":-48.47,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"memory_equipment_recovery_spike_not_stage3_without_order_margin_revision_bridge","four_b_evidence_type":["event_spike","weak_follow_through"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_order_margin_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_083310_2024_02_22_23350","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_TES_095610_2024_03_06_MEMORY_EQUIPMENT_RECOVERY_RERATING_4B","trigger_id":"TES_095610_2024_03_06_STAGE2A_MEMORY_EQUIPMENT_RECOVERY","symbol":"095610","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable / Yellow-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage2-Actionable with C10 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Memory equipment recovery worked, but Green requires realized order, margin, revision, and FCF conversion.","MFE_90D_pct":58.17,"MAE_90D_pct":-8.85,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_HANAMATERIALS_166090_2024_03_22_MEMORY_PROCESS_PARTS_CYCLE_RERATING","trigger_id":"HANAMATERIALS_166090_2024_03_22_STAGE2A_MEMORY_PROCESS_PARTS_RECOVERY","symbol":"166090","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable / cycle-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":65,"stage_label_after":"Stage2-watch with memory-cycle 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Process-parts recovery produced MFE, but late drawdown says margin/revision bridge must gate Yellow/Green.","MFE_90D_pct":32.76,"MAE_90D_pct":-8.05,"score_return_alignment_label":"positive_but_late_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_LOTVACUUM_083310_2024_02_22_MEMORY_EQUIPMENT_RECOVERY_FALSE_POSITIVE","trigger_id":"LOTVACUUM_083310_2024_02_22_STAGE2_FALSE_POSITIVE_MEMORY_EQUIPMENT_RECOVERY","symbol":"083310","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":7,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":48,"stage_label_after":"Stage1/4C-watch, not C10 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Equipment recovery spike without realized order/margin/revision bridge produced low MFE and high MAE.","MFE_90D_pct":4.71,"MAE_90D_pct":-35.25,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"99","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 99
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

If this loop is accepted, C10 moves to projected 24 rows and still needs 6 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C10 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/095/095610.json
  - atlas/symbol_profiles/166/166090.json
  - atlas/symbol_profiles/083/083310.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
