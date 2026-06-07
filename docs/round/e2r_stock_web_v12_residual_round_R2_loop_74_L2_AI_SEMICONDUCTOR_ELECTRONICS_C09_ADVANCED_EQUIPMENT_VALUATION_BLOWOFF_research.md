# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_74_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
selected_round: R2
selected_loop: 74
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_PROCESS_EQUIPMENT_PRICE_EXTENSION_4B_WATCH
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

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual error types for R2/L2/C09.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop only stress-tests them inside C09:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS
C09 -> C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

C09 is interpreted as semiconductor/advanced equipment cases where the price can move ahead of order intake, revenue conversion, margin bridge, or revision. The central question is not “did the equipment stock move?” but “did the move have enough non-price bridge to avoid becoming 4B or a false Stage2?”

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C09 current rows | 15 |
| C09 current symbols | 11 |
| C09 good/bad Stage2 | 6 / 3 |
| C09 4B/4C | 1 / 2 |
| C09 URL pending/proxy | 15 / 9 |
| top covered symbols | 039030, 084370, 140860, 240810, 036810, 036930 |

This session locally generated C08 loops 72-73, so this run moves to the next official Priority 0 archetype, C09, to reduce local repetition.

Selected symbols avoid the C09 top-covered symbols:

| symbol | company | status |
|---|---|---|
| 281820 | 케이씨텍 | new symbol versus top covered C09 list |
| 089970 | 브이엠 | new symbol versus top covered C09 list |
| 083310 | 엘오티베큠 | new symbol versus top covered C09 list |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web atlas validation:

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream | FinanceData/marcap |
| manifest | atlas/manifest.json |
| schema | atlas/schema.json |
| manifest max_date | 2026-02-20 |
| calibration shard root | atlas/ohlcv_tradable_by_symbol_year |
| raw shard root | atlas/ohlcv_raw_by_symbol_year |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 281820 / 2024-02-27 | true | true | clean_180D_window | true |
| 089970 / 2024-06-11 | true | true | clean_180D_window | true |
| 083310 / 2024-02-22 | true | true | clean_180D_window | true |

Corporate-action notes:

- 281820 profile has zero corporate-action candidates.
- 089970 profile has zero corporate-action candidates.
- 083310 profile has corporate-action candidates only in 2007; selected 2024 windows are clean.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| ADVANCED_PROCESS_EQUIPMENT_PRICE_EXTENSION_4B_WATCH | C09 | process-equipment rerating can work, but valuation needs a 4B audit |
| ADVANCED_EQUIPMENT_RENAME_EVENT_PRICE_BLOWOFF_WITHOUT_ORDER_BRIDGE | C09 | advanced-equipment/event beta without order bridge is a false-positive path |
| VACUUM_EQUIPMENT_PRICE_SPIKE_ORDER_BRIDGE_MISSING | C09 | equipment price spike without order/revision bridge is C09 guardrail evidence |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C09_KCTECH_281820_2024_02_27_ADV_EQUIP_RERATING_4B | 281820 | 케이씨텍 | 4B_overlay_success | positive | high MFE confirms equipment rerating, but later drawdown shows valuation audit needed |
| C09_VM_089970_2024_06_11_ADV_EQUIP_BLOWOFF_FALSE_POSITIVE | 089970 | 브이엠 | failed_rerating | counterexample | event/advanced-equipment spike had weak order bridge and large MAE |
| C09_LOTVAC_083310_2024_02_22_VACUUM_EQUIP_PRICE_SPIKE | 083310 | 엘오티베큠 | failed_rerating | counterexample | vacuum-equipment spike had low MFE and high drawdown |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 1 |
| counterexample_count | 2 |
| 4B_case_count | 3 |
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
| 281820 | source_proxy_only | advanced-equipment route and sector equipment beta; order/revision bridge partial | required before promotion |
| 089970 | source_proxy_only | advanced-equipment/event beta; order/revision bridge absent | required; counterexample useful |
| 083310 | source_proxy_only | vacuum-equipment route; order/revision bridge absent | required; counterexample useful |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 281820 | atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv | atlas/symbol_profiles/281/281820.json |
| 089970 | atlas/ohlcv_tradable_by_symbol_year/089/089970/2024.csv | atlas/symbol_profiles/089/089970.json |
| 083310 | atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv | atlas/symbol_profiles/083/083310.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| KCTECH_281820_2024_02_27_STAGE2A_ADV_EQUIP_RERATING | Stage2-Actionable | 2024-02-27 | 2024-02-27 | 39200 | advanced-equipment rerating; bridge partial |
| VM_089970_2024_06_11_STAGE2_FALSE_POSITIVE_ADV_EQUIP_BLOWOFF | Stage2 | 2024-06-11 | 2024-06-11 | 17730 | advanced-equipment/event beta without order bridge |
| LOTVAC_083310_2024_02_22_STAGE2_FALSE_POSITIVE_VACUUM_EQUIP_SPIKE | Stage2 | 2024-02-22 | 2024-02-22 | 23350 | vacuum-equipment spike without durable bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 281820 | 2024-02-27 | 39200 | 38.01 | -8.16 | 50.51 | -17.47 | 50.51 | -24.87 | 2024-07-11 | 59000 | -50.08 |
| 089970 | 2024-06-11 | 17730 | 18.16 | -35.87 | 18.16 | -49.69 | 18.16 | -54.71 | 2024-06-13 | 20950 | -61.67 |
| 083310 | 2024-02-22 | 23350 | 4.71 | -10.06 | 4.71 | -35.25 | 4.71 | -46.04 | 2024-02-23 | 24450 | -48.47 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 281820 | Stage2A/Yellow possible; 4B after price extension | 50% MFE then -50% post-peak drawdown | current_profile_4B_too_late |
| 089970 | Stage2 risk if advanced-equipment/event beta over-credited | 18% MFE then -55% 180D MAE | current_profile_false_positive |
| 083310 | Stage2 risk if vacuum-equipment spike over-credited | 5% MFE then -46% 180D MAE | current_profile_false_positive |

Required axis audit:

1. Stage2 bonus is useful for 281820 but too generous for 089970 and 083310 without order/revision bridge.
2. Yellow threshold 75 should not be relaxed for C09.
3. Green threshold 87 / revision 55 should remain strict.
4. Price-only blowoff guard is correct but needs stronger C09 “order bridge required” language.
5. Full 4B non-price requirement remains correct; price-only local peaks should be logged as 4B audit, not full 4B.
6. Hard 4C routing should be earlier for C09 when order/revision bridge fails and MAE expands.

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C09 interpretation:

- Stage2A can be allowed for advanced equipment rerating when an order/revision bridge is at least partial.
- Yellow requires order intake, backlog/revenue conversion, margin bridge, or confirmed revision.
- Green requires strong order/revision bridge plus low 4B risk.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 281820 | 1.00 | 1.00 | valuation / positioning | good full-window 4B timing needed |
| 089970 | 1.00 | 1.00 | price_only / valuation | price-only local 4B too early without order bridge |
| 083310 | 1.00 | 1.00 | price_only / valuation | price-only spike is not Stage3 and not full 4B |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 281820 | thesis_break_watch_only | not hard 4C, but 4B cap was needed |
| 089970 | hard_4c_late | bridge absence should have blocked Stage2 earlier |
| 083310 | hard_4c_late | low MFE/high MAE should have remained Stage1/4B-watch |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = low_to_medium
```

Candidate:

> In L2 advanced semiconductor equipment names, relative strength and equipment beta can open Stage2A only when an order/revision bridge exists. If the price spike is driven mainly by valuation/positioning without order intake, backlog conversion, margin bridge, or revision, cap at Stage1/Stage2-watch and route to C09 4B/false-positive audit.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
confidence = low_to_medium
```

Candidate C09 rule:

```text
C09_order_revision_bridge_required =
  order_intake_growth
  OR backlog/revenue_conversion
  OR margin_bridge
  OR confirmed_revision

if advanced_equipment_price_spike and no order_revision_bridge:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_30D is small and MAE_90D < -30:
    classify_as C09_false_positive_guardrail

if MFE_90D > 40 and drawdown_after_peak < -45:
    add C09_peak_proximity_4B_audit = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 24.46 | -34.14 | 24.46 | -41.87 | 2 | bridge too loose for C09 |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 24.46 | -34.14 | 24.46 | -41.87 | 2 | over-credits price and relative strength |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 50.51 | -17.47 | 50.51 | -24.87 | 0 | better after bridge gate |
| P2 canonical_archetype_candidate_profile | C09 | 1 promoted + 2 guard | 50.51 | -17.47 | 50.51 | -24.87 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C09 guard | 1 promoted + 2 guard | 50.51 | -17.47 | 50.51 | -24.87 | 0 | adds hard bridge gate |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 281820 | Stage2A aligned; 4B watch late | current_profile_4B_too_late |
| 089970 | Stage2 false-positive if bridge not enforced | current_profile_false_positive |
| 083310 | Stage2 false-positive if spike over-credited | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | mixed C09 fine ids | 1 | 2 | 3 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | 15 -> projected 18 rows; still need 12 to reach 30 |

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
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - stage2_actionable_evidence_bonus
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_false_positive
  - current_profile_4B_too_late
new_axis_proposed: C09_order_revision_bridge_required|C09_peak_proximity_4B_audit
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
- Uses C09 Priority 0 coverage gap.
- Uses three symbols not listed among C09 top-covered symbols.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C09_order_revision_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"089970 and 083310 show equipment/valuation spikes can fail without order/revision bridge","blocks two false positives while preserving 281820 Stage2A","KCTECH_281820_2024_02_27_STAGE2A_ADV_EQUIP_RERATING|VM_089970_2024_06_11_STAGE2_FALSE_POSITIVE_ADV_EQUIP_BLOWOFF|LOTVAC_083310_2024_02_22_STAGE2_FALSE_POSITIVE_VACUUM_EQUIP_SPIKE",3,3,2,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C09_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"281820 shows successful equipment rerating can still become a 4B drawdown case","adds 4B audit after rapid C09 MFE and valuation extension","KCTECH_281820_2024_02_27_STAGE2A_ADV_EQUIP_RERATING",1,1,0,low_to_medium,canonical_shadow_only,"4B overlay/risk calibration only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C09_KCTECH_281820_2024_02_27_ADV_EQUIP_RERATING_4B","symbol":"281820","company_name":"케이씨텍","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_PROCESS_EQUIPMENT_PRICE_EXTENSION_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"KCTECH_281820_2024_02_27_STAGE2A_ADV_EQUIP_RERATING","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2A caught the equipment rerating; C09 needed 4B audit before the July peak-to-September drawdown","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"source_proxy_only; URL repair required before promotion"}
{"row_type":"case","case_id":"C09_VM_089970_2024_06_11_ADV_EQUIP_BLOWOFF_FALSE_POSITIVE","symbol":"089970","company_name":"브이엠","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_RENAME_EVENT_PRICE_BLOWOFF_WITHOUT_ORDER_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"VM_089970_2024_06_11_STAGE2_FALSE_POSITIVE_ADV_EQUIP_BLOWOFF","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"18% MFE was quickly overwhelmed by 30D/90D/180D drawdown, consistent with order-bridge failure","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"source_proxy_only; useful C09 counterexample"}
{"row_type":"case","case_id":"C09_LOTVAC_083310_2024_02_22_VACUUM_EQUIP_PRICE_SPIKE","symbol":"083310","company_name":"엘오티베큠","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"VACUUM_EQUIPMENT_PRICE_SPIKE_ORDER_BRIDGE_MISSING","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"LOTVAC_083310_2024_02_22_STAGE2_FALSE_POSITIVE_VACUUM_EQUIP_SPIKE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"local price spike had weak follow-through and deep 180D drawdown","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"source_proxy_only; C09 false-positive guardrail"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"KCTECH_281820_2024_02_27_STAGE2A_ADV_EQUIP_RERATING","case_id":"C09_KCTECH_281820_2024_02_27_ADV_EQUIP_RERATING_4B","symbol":"281820","company_name":"케이씨텍","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_PROCESS_EQUIPMENT_PRICE_EXTENSION_4B_WATCH","sector":"AI/semiconductor/electronics","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-27","entry_date":"2024-02-27","entry_price":39200.0,"evidence_available_at_that_date":"source_proxy_only: advanced process/semiconductor equipment rerating and AI equipment beta visible; order/revision bridge still partial","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["advanced_equipment_route","relative_strength","sector_ai_equipment_beta"],"stage3_evidence_fields":["order_conversion_partial","margin_bridge_pending","confirmed_revision_pending"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv","profile_path":"atlas/symbol_profiles/281/281820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":38.01,"MFE_90D_pct":50.51,"MFE_180D_pct":50.51,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-8.16,"MAE_90D_pct":-17.47,"MAE_180D_pct":-24.87,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":59000.0,"drawdown_after_peak_pct":-50.08,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_needed_before_price_normalization","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_with_4b_drawdown","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_281820_2024_02_27_39200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"VM_089970_2024_06_11_STAGE2_FALSE_POSITIVE_ADV_EQUIP_BLOWOFF","case_id":"C09_VM_089970_2024_06_11_ADV_EQUIP_BLOWOFF_FALSE_POSITIVE","symbol":"089970","company_name":"브이엠","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_RENAME_EVENT_PRICE_BLOWOFF_WITHOUT_ORDER_BRIDGE","sector":"AI/semiconductor/electronics","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-06-11","entry_date":"2024-06-11","entry_price":17730.0,"evidence_available_at_that_date":"source_proxy_only: advanced equipment/name-change/sector beta price spike, but order intake and revision bridge missing","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["advanced_equipment_route","relative_strength","event_or_rename_beta"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["order_bridge_absent","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089970/2024.csv","profile_path":"atlas/symbol_profiles/089/089970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.16,"MFE_90D_pct":18.16,"MFE_180D_pct":18.16,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-35.87,"MAE_90D_pct":-49.69,"MAE_180D_pct":-54.71,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":20950.0,"drawdown_after_peak_pct":-61.67,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early_without_order_bridge","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_high_mae_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_089970_2024_06_11_17730","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"LOTVAC_083310_2024_02_22_STAGE2_FALSE_POSITIVE_VACUUM_EQUIP_SPIKE","case_id":"C09_LOTVAC_083310_2024_02_22_VACUUM_EQUIP_PRICE_SPIKE","symbol":"083310","company_name":"엘오티베큠","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"VACUUM_EQUIPMENT_PRICE_SPIKE_ORDER_BRIDGE_MISSING","sector":"AI/semiconductor/electronics","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":23350.0,"evidence_available_at_that_date":"source_proxy_only: vacuum equipment price spike and sector equipment beta; no confirmed new order/revision bridge","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["vacuum_equipment_route","relative_strength","sector_equipment_beta"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":["order_bridge_absent","margin_or_backlog_slowdown"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv","profile_path":"atlas/symbol_profiles/083/083310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.71,"MFE_90D_pct":4.71,"MFE_180D_pct":4.71,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-10.06,"MAE_90D_pct":-35.25,"MAE_180D_pct":-46.04,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-23","peak_price":24450.0,"drawdown_after_peak_pct":-48.47,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_spike_not_full_4B_and_not_stage3","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_083310_2024_02_22_23350","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_KCTECH_281820_2024_02_27_ADV_EQUIP_RERATING_4B","trigger_id":"KCTECH_281820_2024_02_27_STAGE2A_ADV_EQUIP_RERATING","symbol":"281820","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":9,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":9,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Actionable with mandatory 4B audit","changed_components":["valuation_repricing_score","execution_risk_score","revision_score"],"component_delta_explanation":"Equipment rerating was real enough for Stage2A, but C09 valuation score must decay after rapid MFE without confirmed order/revision bridge.","MFE_90D_pct":50.51,"MAE_90D_pct":-17.47,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_VM_089970_2024_06_11_ADV_EQUIP_BLOWOFF_FALSE_POSITIVE","trigger_id":"VM_089970_2024_06_11_STAGE2_FALSE_POSITIVE_ADV_EQUIP_BLOWOFF","symbol":"089970","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":52,"stage_label_after":"Stage1/4B-watch, not Stage2","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Advanced-equipment label and price gap were insufficient without order intake/revision bridge; drawdown shows Stage2 was too early.","MFE_90D_pct":18.16,"MAE_90D_pct":-49.69,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_LOTVAC_083310_2024_02_22_VACUUM_EQUIP_PRICE_SPIKE","trigger_id":"LOTVAC_083310_2024_02_22_STAGE2_FALSE_POSITIVE_VACUUM_EQUIP_SPIKE","symbol":"083310","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":7,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":53,"stage_label_after":"Stage1/4B-watch, not Stage2","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","revision_score"],"component_delta_explanation":"Vacuum equipment spike had no durable order/revision bridge; MFE was too small and MAE too large for Stage2 promotion.","MFE_90D_pct":4.71,"MAE_90D_pct":-35.25,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"74","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage2_actionable_evidence_bonus","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_false_positive","current_profile_4B_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 74
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

If this loop is accepted, C09 moves from 15 to a projected 18 rows. It remains below 30-row minimum stability, so C09 can still be selected again if the latest No-Repeat Index has not changed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/089/089970/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/281/281820.json
  - atlas/symbol_profiles/089/089970.json
  - atlas/symbol_profiles/083/083310.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
