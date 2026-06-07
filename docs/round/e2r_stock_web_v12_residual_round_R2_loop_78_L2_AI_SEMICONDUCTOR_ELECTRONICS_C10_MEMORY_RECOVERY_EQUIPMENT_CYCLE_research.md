# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_78_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
selected_round: R2
selected_loop: 78
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_4B_WATCH
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

This loop adds 3 independent cases, 2 counterexamples, and 2 residual error types for R2/L2/C10.

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

C10 is the bridge between memory-cycle beta and actual equipment order conversion. A stock can move on DRAM/NAND recovery, but C10 should not promote Stage3 unless order intake, revenue conversion, revision, or margin bridge follows.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C10 current rows | 21 |
| C10 need to 30 | 9 |
| C10 need to 50 | 29 |
| C10 조사 포인트 | 메모리 회복 beta와 실제 장비 order 전환 구분 |

This session locally generated C08/C09/C01/C07/C06 loops before this file, so C10 is selected as the next under-covered Priority 0 archetype.

Selected symbols:

| symbol | company | status |
|---|---|---|
| 319660 | 피에스케이 | new C10 symbol versus local prior loops |
| 240810 | 원익IPS | new C10 symbol versus local prior loops |
| 095610 | 테스 | new C10 symbol versus local prior loops |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 319660 / 2024-02-29 | true | true | clean_180D_window | true |
| 240810 / 2024-03-29 | true | true | clean_180D_window | true |
| 095610 / 2024-04-15 | true | true | clean_180D_window | true |

Corporate-action notes:

- 피에스케이 has corporate-action candidates in 2022 only; selected 2024 window is clean.
- 원익IPS has zero corporate-action candidates.
- 테스 has corporate-action candidates in 2011 and 2016 only; selected 2024 window is clean.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_4B_WATCH | C10 | early equipment recovery/order conversion route; 4B audit after rerating |
| MEMORY_EQUIPMENT_RECOVERY_LATE_BETA_ORDER_BRIDGE_WEAK | C10 | late memory equipment beta without order/revision bridge |
| MEMORY_EQUIPMENT_SPIKE_ORDER_REVISION_LAG_FALSE_POSITIVE | C10 | late equipment spike with revision lag and high MAE |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C10_PSK_319660_2024_02_29_MEMORY_RECOVERY_EQUIPMENT_ORDER_RERATING | 319660 | 피에스케이 | 4B_overlay_success | positive | early equipment recovery/order route had >50% MFE but later 4B drawdown |
| C10_WONIKIPS_240810_2024_03_29_MEMORY_EQUIP_RECOVERY_LATE_BETA | 240810 | 원익IPS | failed_rerating | counterexample | late price extension had only 8% MFE and -35% 180D MAE |
| C10_TES_095610_2024_04_15_MEMORY_EQUIPMENT_SPIKE_REVISION_LAG | 095610 | 테스 | failed_rerating | counterexample | late spike had only 15% MFE and -45% 180D MAE |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 1 |
| counterexample_count | 2 |
| 4B_case_count | 1 |
| 4C_case_count | 2 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |

Minimum conditions pass:

```text
positive_case_count >= 1
counterexample_count >= 1
calibration_usable_case_count >= 3
new_independent_case_ratio = 1.00
```

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 319660 | source_proxy_only | memory equipment recovery/order conversion route; partial bridge | required before promotion |
| 240810 | source_proxy_only | memory equipment beta but durable order/revision bridge weak | required; useful as counterexample |
| 095610 | source_proxy_only | memory equipment spike but order/revision conversion lagged | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 319660 | atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv | atlas/symbol_profiles/319/319660.json |
| 240810 | atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv | atlas/symbol_profiles/240/240810.json |
| 095610 | atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv | atlas/symbol_profiles/095/095610.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| PSK_319660_2024_02_29_STAGE2A_MEMORY_RECOVERY_EQUIP_ORDER | Stage2-Actionable | 2024-02-29 | 2024-02-29 | 25400 | memory recovery equipment order conversion route |
| WONIKIPS_240810_2024_03_29_STAGE2_FALSE_POSITIVE_MEMORY_EQUIP_BETA | Stage2 | 2024-03-29 | 2024-03-29 | 41500 | late memory-equipment beta without durable order bridge |
| TES_095610_2024_04_15_STAGE2_FALSE_POSITIVE_MEMORY_EQUIP_SPIKE | Stage2 | 2024-04-15 | 2024-04-15 | 28650 | late equipment spike with revision/order lag |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 319660 | 2024-02-29 | 25400 | 24.41 | -11.02 | 53.54 | -11.02 | 53.94 | -21.30 | 2024-07-11 | 39100 | -48.87 |
| 240810 | 2024-03-29 | 41500 | 8.07 | -15.30 | 8.07 | -19.28 | 8.07 | -35.06 | 2024-04-08 | 44850 | -39.91 |
| 095610 | 2024-04-15 | 28650 | 14.83 | -21.29 | 14.83 | -27.57 | 14.83 | -44.68 | 2024-04-17 | 32900 | -51.82 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 319660 | Stage2A/Yellow possible; 4B after rerating | high MFE then deep post-peak drawdown | current_profile_4B_too_late |
| 240810 | Stage2 risk if late cycle beta is over-credited | low MFE and high MAE | current_profile_false_positive |
| 095610 | Stage2 risk if late price spike is over-credited | low MFE and severe MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C10 interpretation:

- Stage2A can work when equipment order conversion appears early in the memory recovery.
- Yellow/Green require confirmed order conversion, margin bridge, and revision.
- Late memory-equipment beta after price extension should be capped as Stage1/Stage2-watch unless bridge evidence arrives.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 319660 | 1.00 | 1.00 | valuation / positioning | good full-window 4B audit after order-route rerating |
| 240810 | 1.00 | 1.00 | price_only / order bridge weak | late price extension not Stage3 |
| 095610 | 1.00 | 1.00 | price_only / revision lag | late spike not Stage3 |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 319660 | thesis_break_watch_only | not hard 4C, but 4B cap needed |
| 240810 | hard_4c_late | weak order/revision bridge should have capped Stage2 |
| 095610 | hard_4c_late | late spike without bridge should have capped Stage2 |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = low_to_medium
```

Candidate:

> In L2 memory equipment names, cycle recovery beta should not be treated as Stage3 unless actual order conversion, margin bridge, or revision appears. Early order-route evidence can support Stage2A, but late price-extension entries should be capped at Stage1/Stage2-watch and routed to C10 false-positive or 4B audit.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
confidence = low_to_medium
```

Candidate C10 rule:

```text
C10_order_conversion_bridge_required =
  memory_equipment_recovery
  AND (order_conversion OR confirmed_revision OR margin_bridge)

if cycle_recovery_beta and order_conversion_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if late_price_extension and MFE_90D < 20 and MAE_180D < -30:
    classify_as C10_false_positive_guardrail

if MFE_90D > 50 and drawdown_after_peak < -40:
    add C10_peak_proximity_4B_audit = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 25.48 | -19.29 | 25.61 | -33.68 | 2 | useful but C10 order bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 25.48 | -19.29 | 25.61 | -33.68 | 2 | over-credits cycle beta |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 53.54 | -11.02 | 53.94 | -21.3 | 0 | better after bridge gate |
| P2 canonical_archetype_candidate_profile | C10 | 1 promoted + 2 guard | 53.54 | -11.02 | 53.94 | -21.3 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C10 guard | 1 promoted + 2 guard | 53.54 | -11.02 | 53.94 | -21.3 | 0 | adds late-cycle beta guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 319660 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 240810 | Stage2 false positive if late beta is over-credited | current_profile_false_positive |
| 095610 | Stage2 false positive if late spike is over-credited | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | mixed C10 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | 21 -> projected 24 rows; still need 6 to reach 30 |

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
new_axis_proposed: C10_order_conversion_bridge_required|C10_late_cycle_beta_guard|C10_peak_proximity_4B_audit
existing_axis_strengthened:
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
- Uses three symbols not used in the local C08/C09/C01/C07/C06 loops.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_order_conversion_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"240810 and 095610 show memory equipment beta can fail without order/revision bridge","blocks two false positives while preserving 319660 Stage2A","PSK_319660_2024_02_29_STAGE2A_MEMORY_RECOVERY_EQUIP_ORDER|WONIKIPS_240810_2024_03_29_STAGE2_FALSE_POSITIVE_MEMORY_EQUIP_BETA|TES_095610_2024_04_15_STAGE2_FALSE_POSITIVE_MEMORY_EQUIP_SPIKE",3,3,2,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C10_late_cycle_beta_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"late price-extension entries had low MFE and high MAE","caps late memory-equipment beta at Stage1/Stage2-watch","WONIKIPS_240810_2024_03_29_STAGE2_FALSE_POSITIVE_MEMORY_EQUIP_BETA|TES_095610_2024_04_15_STAGE2_FALSE_POSITIVE_MEMORY_EQUIP_SPIKE",2,2,2,low_to_medium,canonical_shadow_only,"false-positive guardrail"
shadow_weight,C10_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"319660 high-MFE equipment recovery still required 4B audit after valuation extension","adds 4B audit after large C10 MFE without turning price-only peaks into full 4B","PSK_319660_2024_02_29_STAGE2A_MEMORY_RECOVERY_EQUIP_ORDER",1,1,0,low_to_medium,canonical_shadow_only,"4B overlay/risk calibration only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C10_PSK_319660_2024_02_29_MEMORY_RECOVERY_EQUIPMENT_ORDER_RERATING","symbol":"319660","company_name":"피에스케이","round":"R2","loop":"78","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"PSK_319660_2024_02_29_STAGE2A_MEMORY_RECOVERY_EQUIP_ORDER","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"early memory-recovery equipment/order route captured >50% MFE, but post-peak drawdown requires 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C10 symbol versus local prior loops; evidence is source_proxy_only and requires URL repair"}
{"row_type":"case","case_id":"C10_WONIKIPS_240810_2024_03_29_MEMORY_EQUIP_RECOVERY_LATE_BETA","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"78","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_EQUIPMENT_RECOVERY_LATE_BETA_ORDER_BRIDGE_WEAK","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"WONIKIPS_240810_2024_03_29_STAGE2_FALSE_POSITIVE_MEMORY_EQUIP_BETA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"late memory-equipment beta had only single-digit MFE before -35% 180D MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"counterexample for memory recovery beta without durable order/revision bridge"}
{"row_type":"case","case_id":"C10_TES_095610_2024_04_15_MEMORY_EQUIPMENT_SPIKE_REVISION_LAG","symbol":"095610","company_name":"테스","round":"R2","loop":"78","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_EQUIPMENT_SPIKE_ORDER_REVISION_LAG_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TES_095610_2024_04_15_STAGE2_FALSE_POSITIVE_MEMORY_EQUIP_SPIKE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"late memory-equipment spike showed limited MFE and then severe 180D drawdown as order/revision bridge lagged","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"counterexample for late equipment-cycle entry after price extension"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"PSK_319660_2024_02_29_STAGE2A_MEMORY_RECOVERY_EQUIP_ORDER","case_id":"C10_PSK_319660_2024_02_29_MEMORY_RECOVERY_EQUIPMENT_ORDER_RERATING","symbol":"319660","company_name":"피에스케이","round":"R2","loop":"78","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_4B_WATCH","sector":"AI/semiconductor/electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":25400.0,"evidence_available_at_that_date":"source_proxy_only: memory equipment recovery route, order conversion expectation, relative strength, and sector cycle recovery beta; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_equipment_recovery_route","order_conversion_route","relative_strength","cycle_recovery_beta"],"stage3_evidence_fields":["order_conversion_partial","revision_bridge_pending","margin_bridge_pending"],"stage4b_evidence_fields":["valuation_rerating","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv","profile_path":"atlas/symbol_profiles/319/319660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.41,"MFE_90D_pct":53.54,"MFE_180D_pct":53.94,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-11.02,"MAE_90D_pct":-11.02,"MAE_180D_pct":-21.3,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":39100.0,"drawdown_after_peak_pct":-48.87,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_audit_after_memory_equipment_order_rerating","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_319660_2024_02_29_25400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"WONIKIPS_240810_2024_03_29_STAGE2_FALSE_POSITIVE_MEMORY_EQUIP_BETA","case_id":"C10_WONIKIPS_240810_2024_03_29_MEMORY_EQUIP_RECOVERY_LATE_BETA","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"78","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_EQUIPMENT_RECOVERY_LATE_BETA_ORDER_BRIDGE_WEAK","sector":"AI/semiconductor/electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-29","entry_date":"2024-03-29","entry_price":41500.0,"evidence_available_at_that_date":"source_proxy_only: memory equipment recovery beta and price spike were visible, but durable order/revision bridge was not yet confirmed","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_equipment_beta","relative_strength","cycle_recovery_narrative"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["late_price_extension","order_bridge_weak","valuation_blowoff"],"stage4c_evidence_fields":["order_revision_bridge_absent","cycle_beta_reversal"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv","profile_path":"atlas/symbol_profiles/240/240810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.07,"MFE_90D_pct":8.07,"MFE_180D_pct":8.07,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-15.3,"MAE_90D_pct":-19.28,"MAE_180D_pct":-35.06,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-08","peak_price":44850.0,"drawdown_after_peak_pct":-39.91,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_price_extension_not_stage3_without_order_revision_bridge","four_b_evidence_type":["price_only","valuation_blowoff","order_bridge_weak"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_order_bridge_weak","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_240810_2024_03_29_41500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TES_095610_2024_04_15_STAGE2_FALSE_POSITIVE_MEMORY_EQUIP_SPIKE","case_id":"C10_TES_095610_2024_04_15_MEMORY_EQUIPMENT_SPIKE_REVISION_LAG","symbol":"095610","company_name":"테스","round":"R2","loop":"78","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_EQUIPMENT_SPIKE_ORDER_REVISION_LAG_FALSE_POSITIVE","sector":"AI/semiconductor/electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-04-15","entry_date":"2024-04-15","entry_price":28650.0,"evidence_available_at_that_date":"source_proxy_only: memory equipment spike and cycle recovery beta, but order/revision conversion was late and unconfirmed","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_equipment_spike","cycle_recovery_beta","relative_strength_late"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["late_price_extension","order_revision_lag","valuation_blowoff"],"stage4c_evidence_fields":["order_revision_bridge_absent","cycle_beta_reversal"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv","profile_path":"atlas/symbol_profiles/095/095610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.83,"MFE_90D_pct":14.83,"MFE_180D_pct":14.83,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-21.29,"MAE_90D_pct":-27.57,"MAE_180D_pct":-44.68,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-17","peak_price":32900.0,"drawdown_after_peak_pct":-51.82,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_equipment_spike_not_stage3_without_order_revision_bridge","four_b_evidence_type":["price_only","valuation_blowoff","order_revision_lag"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_revision_lag","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_095610_2024_04_15_28650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_PSK_319660_2024_02_29_MEMORY_RECOVERY_EQUIPMENT_ORDER_RERATING","trigger_id":"PSK_319660_2024_02_29_STAGE2A_MEMORY_RECOVERY_EQUIP_ORDER","symbol":"319660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable / Yellow-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable with mandatory 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Early equipment recovery/order route worked, but valuation extension needed a 4B audit after >50% MFE.","MFE_90D_pct":53.54,"MAE_90D_pct":-11.02,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_WONIKIPS_240810_2024_03_29_MEMORY_EQUIP_RECOVERY_LATE_BETA","trigger_id":"WONIKIPS_240810_2024_03_29_STAGE2_FALSE_POSITIVE_MEMORY_EQUIP_BETA","symbol":"240810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":7,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":51,"stage_label_after":"Stage1/4B-watch, not Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Late memory-equipment beta without order/revision bridge produced poor MFE/MAE alignment.","MFE_90D_pct":8.07,"MAE_90D_pct":-19.28,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_TES_095610_2024_04_15_MEMORY_EQUIPMENT_SPIKE_REVISION_LAG","trigger_id":"TES_095610_2024_04_15_STAGE2_FALSE_POSITIVE_MEMORY_EQUIP_SPIKE","symbol":"095610","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":7,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":51,"stage_label_after":"Stage1/4B-watch, not Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Late equipment spike after price extension lacked order/revision bridge and turned into high MAE.","MFE_90D_pct":14.83,"MAE_90D_pct":-27.57,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"78","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 78
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN
```

If this loop is accepted, C10 moves from 21 to a projected 24 rows. It remains below 30-row minimum stability, but the next run should re-read the latest No-Repeat Index before selecting another C10 case.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/319/319660.json
  - atlas/symbol_profiles/240/240810.json
  - atlas/symbol_profiles/095/095610.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
