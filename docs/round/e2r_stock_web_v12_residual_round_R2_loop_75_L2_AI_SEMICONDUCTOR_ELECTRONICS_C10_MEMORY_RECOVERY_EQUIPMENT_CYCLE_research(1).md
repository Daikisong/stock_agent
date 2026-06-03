# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R2
scheduled_loop: 75
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R3
computed_next_loop: 75
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: C10_ORDER_UTILIZATION_MARGIN_CASHFLOW_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

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

## 2. Round / Large Sector / Canonical Archetype Scope

R2 maps to `L2_AI_SEMICONDUCTOR_ELECTRONICS`. The previous R2 loop used C08 socket/probe-card customer quality, so this run rotates to the under-covered C10 memory-recovery equipment-cycle branch. The aim is to separate real recovery-through-utilization and margin evidence from equipment-theme MFE that later decays into high MAE.

| layer | id | definition |
|---|---|---|
| round | R2 | AI / semiconductor / electronics |
| large_sector | L2_AI_SEMICONDUCTOR_ELECTRONICS | semiconductor, AI, HBM, equipment, memory cycle |
| canonical | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | memory recovery, equipment/parts cycle, utilization and margin |
| fine | C10_ORDER_UTILIZATION_MARGIN_CASHFLOW_BRIDGE_GUARD | memory/equipment signal must become order, utilization and margin bridge |
| deep | SEMICONDUCTOR_PARTS_CLEANING_REFURB_MEMORY_RECOVERY_TO_UTILIZATION_MARGIN | parts-cleaning/refurb positive |
| deep | VACUUM_PUMP_SEMI_EQUIPMENT_OPTIONALITY_WITHOUT_CUSTOMER_ORDER_UTILIZATION_MARGIN_CONVERSION | vacuum equipment false positive |
| deep | ETCH_EQUIPMENT_MEMORY_RECOVERY_OPTIONALITY_WITHOUT_REPEAT_ORDER_MARGIN_CASHFLOW_CONVERSION | etch equipment MFE/high-MAE watch |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C10 top-covered symbols are `036930`, `240810`, `084370`, `095610`, `테스`, and `000660`. This run avoids that cluster and also avoids the prior R2/C08/C09/C10 representative sets where possible.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C10 | 114810 | new independent | not top-covered C10 symbol; parts-cleaning/refurb utilization-margin bridge |
| C10 | 083310 | new independent | not top-covered C10 symbol; vacuum equipment theme without durable order/margin bridge |
| C10 | 089970 | new independent | not top-covered C10 symbol; etch equipment MFE without durable repeat-order bridge |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web assumptions:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable columns = d,o,h,l,c,v,a,mc,s,m
```

## 5. Historical Eligibility Gate

```text
entry row exists = true
forward 180 trading days available = true
MFE/MAE 30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Corporate-action caveat:

```text
114810 has corporate-action candidate dates ending 2021, outside the selected 2024 representative window.
083310 has corporate-action candidate dates ending 2007, outside the selected 2024 representative window.
089970 has no corporate-action candidate dates.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 114810 | 한솔아이원스 | Stage2-Actionable | 2024-02-20 | 10820 | parts-cleaning/refurb memory recovery bridge worked, but Green blocked |
| failed_memory_equipment_theme_high_MAE_counterexample | 083310 | 엘오티베큠 | Stage2-Actionable | 2024-02-22 | 23350 | vacuum equipment theme lacked durable customer-order/margin bridge |
| etch_equipment_MFE_then_high_MAE_counterexample | 089970 | 브이엠 | Stage2-Actionable | 2024-02-29 | 14060 | etch-equipment MFE lacked durable repeat-order/margin bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 3
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 114810 | 한솔아이원스 | Stage2-Actionable | 2024-02-20 | 10820 | 41.96 | 41.96 | 41.96 | -2.03 | -2.03 | -23.66 | 2024-04-02 | 15360 | -46.22 |
| 083310 | 엘오티베큠 | Stage2-Actionable | 2024-02-22 | 23350 | 4.71 | 4.71 | 4.71 | -12.85 | -35.97 | -64.63 | 2024-02-23 | 24450 | -66.22 |
| 089970 | 브이엠 | Stage2-Actionable | 2024-02-29 | 14060 | 20.91 | 25.82 | 25.82 | -16.86 | -21.41 | -40.97 | 2024-07-01 | 17690 | -53.08 |

## 9. Case-by-Case Notes

### 9.1 114810 / 한솔아이원스 — parts-cleaning/refurb memory-recovery bridge

The entry row is 2024-02-20 at 10,820. The path reached 15,360, with early MAE staying contained before the later cycle drawdown. This is a valid C10 positive only as a guarded Yellow: parts cleaning/refurb and memory recovery have to translate into utilization, margin, and earnings visibility. The later high-MAE path blocks Green.

### 9.2 083310 / 엘오티베큠 — vacuum-equipment theme false positive

The entry row is 2024-02-22 at 23,350. The local high was 24,450, but the later path fell sharply. This is the C10 false-positive branch: equipment-cycle language and memory-recovery beta cannot substitute for confirmed customer orders, utilization and margin conversion.

### 9.3 089970 / 브이엠 — etch-equipment MFE without durable bridge

The entry row is 2024-02-29 at 14,060. MFE existed, eventually reaching 17,690, but the later low reached 8,300. This row is useful because it shows that even real MFE should remain 4B/high-MAE watch if repeat orders, utilization, margin and cashflow are not durable.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C10 treats memory/equipment MFE as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C10 needs order/utilization/margin/cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 083310 and 089970. |
| Full 4B non-price requirement appropriate? | Yes. 114810 has better non-price bridge evidence; the others do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
114810:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after utilization / margin / earnings bridge
  Stage3-Green = reject because late high-MAE and cycle drawdown remain active

083310:
  Stage2-Actionable = too generous if based only on vacuum-equipment / memory-recovery theme
  Stage3-Yellow = reject without customer-order, utilization, margin and cashflow bridge
  Stage3-Green = reject

089970:
  Stage2-Actionable = acceptable only as equipment-cycle watch
  Stage3-Yellow = reject without repeat-order, margin, utilization and cashflow durability
  Stage3-Green = reject despite MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 114810 | 1.00 | 1.00 | memory-parts recovery positive but full-window 4B/high-MAE watch |
| 083310 | 1.00 | 1.00 | vacuum-equipment theme local 4B watch, not positive stage |
| 089970 | 0.77 | 1.00 | MFE exists but no durable order/margin bridge; keep 4B/high-MAE watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c10_requires_order_utilization_margin_cashflow_bridge

rule:
  For C10 memory-recovery equipment-cycle rows, do not promote memory,
  semiconductor equipment, vacuum pump, etch equipment, parts cleaning/refurb,
  or equipment-cycle Stage2 signals into Stage3-Yellow/Green unless at least one
  non-price bridge is visible:
  customer order, repeat order, backlog-to-revenue conversion, utilization recovery,
  margin conversion, working-capital/cashflow conversion, or earnings revision.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 24.16 | -19.8 | 66.7% | too generous to equipment-cycle MFE |
| P0b e2r_2_0_baseline_reference | 3 | 24.16 | -19.8 | 33.3% | safer but may miss 114810 |
| P1 sector_specific_candidate_profile | 3 | 24.16 | -19.8 | 66.7% | no broad L2 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 41.96 | -2.03 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 15.27 | -28.69 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 114810 | current_profile_correct_but_no_green | utilization/margin bridge aligned with MFE but high-MAE blocks Green |
| 083310 | current_profile_false_positive | vacuum-equipment theme produced shallow MFE and high MAE |
| 089970 | current_profile_false_positive_if_green | etch-equipment MFE lacked durable order/margin bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C10_ORDER_UTILIZATION_MARGIN_CASHFLOW_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R2/C10 non-top-covered memory equipment-cycle residual reduced |

## 17. Residual Contribution Summary

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
- local_4b_watch_guard
- high_MAE_guardrail
residual_error_types_found:
- equipment theme without order/margin bridge
- memory parts recovery winner needs 4B watch
- equipment-cycle MFE then high MAE
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_watch_guard
existing_axis_weakened: null
existing_axis_kept:
- stage3_green_total_min
- stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
```

## 18. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- MFE/MAE/peak/drawdown
- R2 direct L2 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/report URLs
- exact customer/order announcement URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c10_requires_order_utilization_margin_cashflow_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"C10 memory-recovery equipment-cycle rows should not promote toward Stage3-Yellow/Green unless memory/equipment signal converts into customer order, backlog-to-revenue, utilization, margin, repeat-order, or cashflow bridge","114810 survives only as guarded positive after utilization/margin bridge; 083310 and 089970 are demoted because equipment-recovery MFE lacked durable customer-order and margin bridge","TRG_R2L75_C10_114810_20240220_PARTS_CLEANING_MEMORY_RECOVERY_MARGIN_BRIDGE|TRG_R2L75_C10_083310_20240222_VACUUM_EQUIPMENT_THEME_NO_ORDER_MARGIN_BRIDGE|TRG_R2L75_C10_089970_20240229_ETCH_EQUIPMENT_MEMORY_RECOVERY_MFE_NO_DURABLE_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c10_equipment_cycle_4b_high_mae_watch_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,1,1,0,"Memory-equipment cycle winners and theme false starts can peak before utilization and margin durability are confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 114810 guarded positive while preventing 083310/089970 equipment-cycle false positives","TRG_R2L75_C10_114810_20240220_PARTS_CLEANING_MEMORY_RECOVERY_MARGIN_BRIDGE|TRG_R2L75_C10_083310_20240222_VACUUM_EQUIPMENT_THEME_NO_ORDER_MARGIN_BRIDGE|TRG_R2L75_C10_089970_20240229_ETCH_EQUIPMENT_MEMORY_RECOVERY_MFE_NO_DURABLE_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R2L75_C10_114810_20240220_PARTS_CLEANING_MEMORY_RECOVERY_MARGIN_BRIDGE","symbol":"114810","company_name":"한솔아이원스","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_PARTS_CLEANING_MEMORY_RECOVERY_MARGIN_BRIDGE","deep_sub_archetype_id":"SEMICONDUCTOR_PARTS_CLEANING_REFURB_MEMORY_RECOVERY_TO_UTILIZATION_MARGIN","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C10 memory recovery equipment-cycle rows require customer order, backlog-to-revenue, utilization, margin, repeat-order or cashflow bridge; memory/equipment theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R2L75_C10_083310_20240222_VACUUM_EQUIPMENT_THEME_NO_ORDER_MARGIN_BRIDGE","symbol":"083310","company_name":"엘오티베큠","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_VACUUM_EQUIPMENT_THEME_WITHOUT_ORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"VACUUM_PUMP_SEMI_EQUIPMENT_OPTIONALITY_WITHOUT_CUSTOMER_ORDER_UTILIZATION_MARGIN_CONVERSION","case_type":"failed_memory_equipment_theme_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C10 memory recovery equipment-cycle rows require customer order, backlog-to-revenue, utilization, margin, repeat-order or cashflow bridge; memory/equipment theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R2L75_C10_089970_20240229_ETCH_EQUIPMENT_MEMORY_RECOVERY_MFE_NO_DURABLE_BRIDGE","symbol":"089970","company_name":"브이엠","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_ETCH_EQUIPMENT_MEMORY_RECOVERY_THEME_WITHOUT_DURABLE_ORDER_BRIDGE","deep_sub_archetype_id":"ETCH_EQUIPMENT_MEMORY_RECOVERY_OPTIONALITY_WITHOUT_REPEAT_ORDER_MARGIN_CASHFLOW_CONVERSION","case_type":"etch_equipment_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C10 memory recovery equipment-cycle rows require customer order, backlog-to-revenue, utilization, margin, repeat-order or cashflow bridge; memory/equipment theme MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R2L75_C10_114810_20240220_PARTS_CLEANING_MEMORY_RECOVERY_MARGIN_BRIDGE","case_id":"R2L75_C10_114810_20240220_PARTS_CLEANING_MEMORY_RECOVERY_MARGIN_BRIDGE","symbol":"114810","company_name":"한솔아이원스","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_PARTS_CLEANING_MEMORY_RECOVERY_MARGIN_BRIDGE","deep_sub_archetype_id":"SEMICONDUCTOR_PARTS_CLEANING_REFURB_MEMORY_RECOVERY_TO_UTILIZATION_MARGIN","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-20","entry_date":"2024-02-20","entry_price":10820,"evidence_available_at_that_date":"source_proxy_semiconductor_parts_cleaning_refurb_memory_recovery_utilization_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_semiconductor_parts_cleaning_refurb_memory_recovery_utilization_margin_bridge; evidence_url_pending","bridge_summary":"memory recovery and parts-cleaning/refurb demand converted into utilization and margin visibility, but later cycle drawdown required 4B/high-MAE watch","stage2_evidence_fields":["memory_recovery_cycle","parts_cleaning_refurb_demand","relative_strength","utilization_margin_proxy"],"stage3_evidence_fields":["utilization_to_margin_visibility","customer_recovery_proxy","earnings_revision_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","semi_parts_cycle_crowding_after_recovery"],"stage4c_evidence_fields":["late_high_MAE_watch_after_peak"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/114/114810/2024.csv","profile_path":"atlas/symbol_profiles/114/114810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":41.96,"MFE_90D_pct":41.96,"MFE_180D_pct":41.96,"MFE_1Y_pct":41.96,"MFE_2Y_pct":41.96,"MAE_30D_pct":-2.03,"MAE_90D_pct":-2.03,"MAE_180D_pct":-23.66,"MAE_1Y_pct":-23.66,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-02","peak_price":15360,"drawdown_after_peak_pct":-46.22,"green_lateness_ratio":"0.38","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"memory_parts_recovery_positive_but_full_window_4B_high_MAE_watch","four_b_evidence_type":"non_price_memory_recovery_utilization_margin_bridge","four_c_protection_label":"late_high_MAE_watch_after_peak","trigger_outcome_label":"structural_success_then_4B_high_MAE_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L75_C10_114810_20240220_PARTS_CLEANING_MEMORY_RECOVERY_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R2L75_C10_083310_20240222_VACUUM_EQUIPMENT_THEME_NO_ORDER_MARGIN_BRIDGE","case_id":"R2L75_C10_083310_20240222_VACUUM_EQUIPMENT_THEME_NO_ORDER_MARGIN_BRIDGE","symbol":"083310","company_name":"엘오티베큠","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_VACUUM_EQUIPMENT_THEME_WITHOUT_ORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"VACUUM_PUMP_SEMI_EQUIPMENT_OPTIONALITY_WITHOUT_CUSTOMER_ORDER_UTILIZATION_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":23350,"evidence_available_at_that_date":"source_proxy_vacuum_pump_memory_equipment_theme_without_customer_order_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_vacuum_pump_memory_equipment_theme_without_customer_order_margin_bridge; evidence_url_pending","bridge_summary":"vacuum equipment / semi recovery theme failed to convert into visible customer order, utilization, margin, or backlog-to-revenue bridge; high MAE dominated the path","stage2_evidence_fields":["vacuum_equipment_theme","memory_recovery_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_theme_local_peak","customer_order_bridge_absent","utilization_margin_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_order_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv","profile_path":"atlas/symbol_profiles/083/083310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.71,"MFE_90D_pct":4.71,"MFE_180D_pct":4.71,"MFE_1Y_pct":4.71,"MFE_2Y_pct":4.71,"MAE_30D_pct":-12.85,"MAE_90D_pct":-35.97,"MAE_180D_pct":-64.63,"MAE_1Y_pct":-64.63,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-23","peak_price":24450,"drawdown_after_peak_pct":-66.22,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"vacuum_equipment_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"equipment_theme_without_durable_order_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L75_C10_083310_20240222_VACUUM_EQUIPMENT_THEME_NO_ORDER_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R2L75_C10_089970_20240229_ETCH_EQUIPMENT_MEMORY_RECOVERY_MFE_NO_DURABLE_BRIDGE","case_id":"R2L75_C10_089970_20240229_ETCH_EQUIPMENT_MEMORY_RECOVERY_MFE_NO_DURABLE_BRIDGE","symbol":"089970","company_name":"브이엠","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_ETCH_EQUIPMENT_MEMORY_RECOVERY_THEME_WITHOUT_DURABLE_ORDER_BRIDGE","deep_sub_archetype_id":"ETCH_EQUIPMENT_MEMORY_RECOVERY_OPTIONALITY_WITHOUT_REPEAT_ORDER_MARGIN_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":14060,"evidence_available_at_that_date":"source_proxy_etch_equipment_memory_recovery_theme_without_repeat_order_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_etch_equipment_memory_recovery_theme_without_repeat_order_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"etch equipment and memory-recovery optionality produced MFE, but durable repeat order, utilization, margin, and cashflow bridge did not hold through the cycle","stage2_evidence_fields":["etch_equipment_theme","memory_recovery_beta","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["MFE_peak_watch","repeat_order_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_durable_order_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089970/2024.csv","profile_path":"atlas/symbol_profiles/089/089970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.91,"MFE_90D_pct":25.82,"MFE_180D_pct":25.82,"MFE_1Y_pct":25.82,"MFE_2Y_pct":25.82,"MAE_30D_pct":-16.86,"MAE_90D_pct":-21.41,"MAE_180D_pct":-40.97,"MAE_1Y_pct":-40.97,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-01","peak_price":17690,"drawdown_after_peak_pct":-53.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"MFE_exists_but_no_durable_order_margin_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"equipment_theme_without_durable_order_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L75_C10_089970_20240229_ETCH_EQUIPMENT_MEMORY_RECOVERY_MFE_NO_DURABLE_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L75_C10_114810_20240220_PARTS_CLEANING_MEMORY_RECOVERY_MARGIN_BRIDGE","trigger_id":"TRG_R2L75_C10_114810_20240220_PARTS_CLEANING_MEMORY_RECOVERY_MARGIN_BRIDGE","symbol":"114810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"memory_recovery_score":12,"customer_order_score":10,"utilization_margin_score":11,"cashflow_bridge_score":9,"relative_strength_score":11,"theme_risk_penalty":6},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"memory_recovery_score":14,"customer_order_score":13,"utilization_margin_score":14,"cashflow_bridge_score":11,"relative_strength_score":8,"theme_risk_penalty":9},"weighted_score_after":79,"stage_label_after":"Stage3-Yellow","changed_components":["memory_recovery_score","customer_order_score","utilization_margin_score","cashflow_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C10 row is promoted only because memory recovery converts into parts-cleaning utilization, margin and earnings bridge; late high-MAE blocks Green.","MFE_90D_pct":41.96,"MAE_90D_pct":-2.03,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L75_C10_083310_20240222_VACUUM_EQUIPMENT_THEME_NO_ORDER_MARGIN_BRIDGE","trigger_id":"TRG_R2L75_C10_083310_20240222_VACUUM_EQUIPMENT_THEME_NO_ORDER_MARGIN_BRIDGE","symbol":"083310","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"memory_recovery_score":10,"customer_order_score":1,"utilization_margin_score":1,"cashflow_bridge_score":0,"relative_strength_score":10,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"memory_recovery_score":4,"customer_order_score":0,"utilization_margin_score":0,"cashflow_bridge_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["memory_recovery_score","customer_order_score","utilization_margin_score","cashflow_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C10 guard demotes equipment-cycle theme rows when customer order, utilization, margin, repeat-order and cashflow bridge are absent.","MFE_90D_pct":4.71,"MAE_90D_pct":-35.97,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L75_C10_089970_20240229_ETCH_EQUIPMENT_MEMORY_RECOVERY_MFE_NO_DURABLE_BRIDGE","trigger_id":"TRG_R2L75_C10_089970_20240229_ETCH_EQUIPMENT_MEMORY_RECOVERY_MFE_NO_DURABLE_BRIDGE","symbol":"089970","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"memory_recovery_score":10,"customer_order_score":1,"utilization_margin_score":1,"cashflow_bridge_score":0,"relative_strength_score":10,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"memory_recovery_score":4,"customer_order_score":0,"utilization_margin_score":0,"cashflow_bridge_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["memory_recovery_score","customer_order_score","utilization_margin_score","cashflow_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C10 guard demotes equipment-cycle theme rows when customer order, utilization, margin, repeat-order and cashflow bridge are absent.","MFE_90D_pct":25.82,"MAE_90D_pct":-21.41,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c10_requires_order_utilization_margin_cashflow_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"C10 memory-recovery equipment-cycle rows should not promote toward Stage3-Yellow/Green unless memory/equipment signal converts into customer order, backlog-to-revenue, utilization, margin, repeat-order, or cashflow bridge","114810 survives only as guarded positive after utilization/margin bridge; 083310 and 089970 are demoted because equipment-recovery MFE lacked durable customer-order and margin bridge","TRG_R2L75_C10_114810_20240220_PARTS_CLEANING_MEMORY_RECOVERY_MARGIN_BRIDGE|TRG_R2L75_C10_083310_20240222_VACUUM_EQUIPMENT_THEME_NO_ORDER_MARGIN_BRIDGE|TRG_R2L75_C10_089970_20240229_ETCH_EQUIPMENT_MEMORY_RECOVERY_MFE_NO_DURABLE_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c10_equipment_cycle_4b_high_mae_watch_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,1,1,0,"Memory-equipment cycle winners and theme false starts can peak before utilization and margin durability are confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 114810 guarded positive while preventing 083310/089970 equipment-cycle false positives","TRG_R2L75_C10_114810_20240220_PARTS_CLEANING_MEMORY_RECOVERY_MARGIN_BRIDGE|TRG_R2L75_C10_083310_20240222_VACUUM_EQUIPMENT_THEME_NO_ORDER_MARGIN_BRIDGE|TRG_R2L75_C10_089970_20240229_ETCH_EQUIPMENT_MEMORY_RECOVERY_MFE_NO_DURABLE_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"75","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["equipment_theme_without_order_margin_bridge","memory_parts_recovery_winner_needs_4B_watch","equipment_cycle_MFE_then_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R2-specific handling

- R2 maps to `L2_AI_SEMICONDUCTOR_ELECTRONICS`.
- This MD uses `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE`.
- Validate `round_schedule_status=valid` and `round_sector_consistency=pass` before accepting rows.

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
- price-only/equipment-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R2 direct L2 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C10 memory-recovery equipment rows cannot promote without customer order, repeat order, backlog-to-revenue conversion, utilization recovery, margin conversion, working-capital/cashflow conversion, or earnings revision.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R2
completed_loop = 75
next_round = R3
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

## 23. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

Stock-web:
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/114/114810.json
atlas/symbol_profiles/083/083310.json
atlas/symbol_profiles/089/089970.json
atlas/ohlcv_tradable_by_symbol_year/114/114810/2024.csv
atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv
atlas/ohlcv_tradable_by_symbol_year/089/089970/2024.csv
```

This loop continues loop 75 with R2 and adds 3 new independent C10 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R2/L2.
