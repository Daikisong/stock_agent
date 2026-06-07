# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_125_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
selected_round: R2
selected_loop: 125
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_PARTS_CONSUMABLE_RECOVERY_ORDER_CYCLE_4B_WATCH
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

This is the corrected valid run after a C06 duplicate materialization path was discarded. C06 reached the local 30-row stability threshold at loop124, so this loop moves to the next Priority 0 gap: C10.

This loop adds 3 new independent C10 rows and moves C10 from static 21 rows to projected 24 rows. It still needs 6 rows to reach the 30-row stability threshold.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_2_rolling_calibrated_proxy`; rollback reference is `calibrated`.

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

C10 is the memory recovery equipment-cycle archetype. The key distinction is between a broad memory-cycle beta and a real order/consumable/margin bridge. The former is a tide; the latter is a pier that can actually hold weight.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C10 static rows | 21 |
| C10 static symbols | 18 |
| C10 good/bad Stage2 | 6 / 6 |
| C10 4B/4C | 3 / 3 |
| C10 URL pending/proxy | 18 / 12 |
| C10 top covered symbols | 036930(3), 074600(2), 003160(1), 031980(1), 036540(1), 039030(1) |
| local previous C10 rows in this session | 0 |
| this loop projected rows | 24 |

Selected symbols avoid static C10 top-covered symbols and local C06/C07/C08/C09 stabilization rows where possible.

| symbol | company | status |
|---|---|---|
| 166090 | 하나머티리얼즈 | new local C10 symbol |
| 064760 | 티씨케이 | new local C10 symbol |
| 014680 | 한솔케미칼 | new local C10 symbol; material/equipment-cycle boundary, reduced weight |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known local hard duplicate.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 166090 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.95 |
| 064760 / 2024-03-06 | true | true | clean_180D_window | true |
| 014680 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.90 |

Corporate-action notes:

- 하나머티리얼즈 has old corporate-action candidates in 2018 only; selected 2024 window is clean.
- 티씨케이 has zero corporate-action candidates.
- 한솔케미칼 has old corporate-action candidates before 2000 only; selected 2024 window is clean.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| MEMORY_PARTS_CONSUMABLE_RECOVERY_ORDER_CYCLE_4B_WATCH | C10 | memory parts/consumable recovery can support Stage2A, but cycle 4B audit is mandatory |
| SIC_RING_CONSUMABLE_MEMORY_RECOVERY_ORDER_CYCLE_4B_WATCH | C10 | SiC ring/consumable cycle can work if utilization/order conversion arrives |
| MEMORY_CHEMICAL_MATERIAL_RECOVERY_BETA_WITHOUT_ORDER_MARGIN_BRIDGE | C10 | memory chemical/material beta without order/margin/revision bridge is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C10_HANAMATERIALS_166090_2024_03_06_MEMORY_PARTS_CONSUMABLE_RECOVERY_4B | 166090 | 하나머티리얼즈 | 4B_overlay_success | positive | memory parts recovery produced 43.18% MFE but later deep drawdown |
| C10_TCK_064760_2024_03_06_SIC_RING_MEMORY_CONSUMABLE_RECOVERY_4B | 064760 | 티씨케이 | 4B_overlay_success | positive | SiC ring consumable cycle produced 55.50% MFE and then cycle drawdown |
| C10_HANSOLCHEM_014680_2024_03_06_MEMORY_CHEMICAL_BETA_FAIL | 014680 | 한솔케미칼 | failed_rerating | counterexample | memory chemical beta had low MFE and deep 180D MAE without bridge |

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
| reduced_weight_caveat_count | 2 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 166090 | source_proxy_only | parts/consumable order-cycle recovery / utilization recovery | required before promotion |
| 064760 | source_proxy_only | SiC ring/etch consumable recovery / margin bridge partial | required before promotion |
| 014680 | source_proxy_only | chemical/material memory beta but order/margin/revision bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 166090 | atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv | atlas/symbol_profiles/166/166090.json |
| 064760 | atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv | atlas/symbol_profiles/064/064760.json |
| 014680 | atlas/ohlcv_tradable_by_symbol_year/014/014680/2024.csv | atlas/symbol_profiles/014/014680.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| HANAMATERIALS_166090_2024_03_06_STAGE2A_MEMORY_PARTS_RECOVERY | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 48400 | memory parts/consumable order-cycle recovery |
| TCK_064760_2024_03_06_STAGE2A_MEMORY_CONSUMABLE_RECOVERY | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 96400 | SiC ring / etch consumable recovery |
| HANSOLCHEM_014680_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_CHEMICAL_BETA | Stage2 | 2024-03-06 | 2024-03-06 | 190700 | memory chemical/material beta without order/margin bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 166090 | 2024-03-06 | 48400 | 27.07 | -5.79 | 43.18 | -5.79 | 43.18 | -53.31 | 2024-07-02 | 69300 | -67.39 |
| 064760 | 2024-03-06 | 96400 | 44.29 | -3.11 | 55.50 | -3.11 | 55.50 | -29.57 | 2024-06-14 | 149900 | -54.70 |
| 014680 | 2024-03-06 | 190700 | 12.22 | -4.82 | 12.22 | -9.23 | 12.22 | -48.19 | 2024-03-21 | 214000 | -53.83 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 166090 | Stage2A possible; 4B after memory parts recovery | high MFE but later deep drawdown | current_profile_4B_too_late |
| 064760 | Stage2A possible; 4B after SiC ring recovery | high MFE but cycle peak drawdown | current_profile_4B_too_late |
| 014680 | Stage2 risk if material beta is over-credited | low MFE and high 180D MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C10 interpretation:

- Stage2A can work when recovery beta is tied to parts/consumable order conversion, utilization, margin, revision, and FCF.
- Yellow/Green require non-price order or margin evidence.
- Broad memory chemical/material beta without the order/margin bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 166090 | 0.70 | 1.00 | parts/consumable cycle rerating | full-window C10 4B audit required |
| 064760 | 0.64 | 1.00 | SiC ring consumable cycle rerating | full-window C10 4B audit required |
| 014680 | 0.89 | 1.00 | chemical/material beta / bridge absent | not Stage3 without order/margin/revision bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 166090 | thesis_break_watch_only | not hard 4C, but cycle 4B cap needed after rerating |
| 064760 | thesis_break_watch_only | not hard 4C, but memory-consumable cycle cap needed |
| 014680 | hard_4c_late | order/margin/revision bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, memory recovery should promote Stage2A only when parts/consumable/equipment order conversion, utilization, margin bridge, revision or FCF is visible. Generic chemical/material memory beta without that bridge should not become Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
confidence = medium
```

Candidate C10 rule:

```text
C10_memory_recovery_order_margin_bridge_required =
  memory_recovery_equipment_or_consumable_route
  AND (order_conversion OR utilization_recovery OR consumable_repeat_demand OR margin_bridge OR confirmed_revision OR fcf_conversion)

if memory_material_beta and order_margin_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 35 and drawdown_after_peak < -35:
    add C10_memory_cycle_4B_audit = true

if MFE_90D < 15 and MAE_180D < -35 and bridge_absent:
    classify_as C10_memory_beta_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 36.97 | -6.04 | 36.97 | -43.69 | 1 | useful but C10 bridge still loose |
| P0b calibrated rollback | rollback | 3 | 36.97 | -6.04 | 36.97 | -43.69 | 1 | over-credits memory beta |
| P1 sector_specific_candidate_profile | L2 | 2 promoted + 1 guard | 49.34 | -4.45 | 49.34 | -41.44 | 0 | better after order/margin bridge gate |
| P2 canonical_archetype_candidate_profile | C10 | 2 promoted + 1 guard | 49.34 | -4.45 | 49.34 | -41.44 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C10 guard | 2 promoted + 1 guard | 49.34 | -4.45 | 49.34 | -41.44 | 0 | adds memory beta false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 166090 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 064760 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 014680 | Stage2 false positive if order/margin bridge not enforced | current_profile_false_positive |

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
new_axis_proposed: C10_memory_recovery_order_margin_bridge_required|C10_memory_cycle_4B_audit|C10_memory_beta_false_positive_guardrail
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
- Uses C10 Priority 0 coverage gap.
- Avoids C10 static top-covered symbols where possible.
- Avoids local C06/C07/C08/C09 threshold-completion loops.
- Keeps 166090 and 014680 with reduced weights due to old profile caveats or material/equipment-cycle boundary.
- Discards the accidental duplicate C06 loop124 materialization path.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count repeated loop124 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_memory_recovery_order_margin_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"014680 shows memory material beta can fail without order/margin/revision bridge while 166090/064760 work only as Stage2A with 4B audit","blocks 014680 false positive while preserving 166090/064760 Stage2A","HANAMATERIALS_166090_2024_03_06_STAGE2A_MEMORY_PARTS_RECOVERY|TCK_064760_2024_03_06_STAGE2A_MEMORY_CONSUMABLE_RECOVERY|HANSOLCHEM_014680_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_CHEMICAL_BETA",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C10_memory_cycle_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"166090/064760 memory recovery-cycle reratings needed full-window 4B audit after high MFE and drawdown","adds 4B audit after C10 memory-cycle MFE without converting price-only peaks into Green","HANAMATERIALS_166090_2024_03_06_STAGE2A_MEMORY_PARTS_RECOVERY|TCK_064760_2024_03_06_STAGE2A_MEMORY_CONSUMABLE_RECOVERY",2,2,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C10_memory_beta_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"014680 had low MFE and high 180D MAE after memory chemical beta without order/margin bridge","requires confirmed order/utilization/margin/revision/FCF bridge before Stage2/Yellow promotion","HANSOLCHEM_014680_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_CHEMICAL_BETA",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C10_HANAMATERIALS_166090_2024_03_06_MEMORY_PARTS_CONSUMABLE_RECOVERY_4B","symbol":"166090","company_name":"하나머티리얼즈","round":"R2","loop":"125","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_PARTS_CONSUMABLE_RECOVERY_ORDER_CYCLE_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"HANAMATERIALS_166090_2024_03_06_STAGE2A_MEMORY_PARTS_RECOVERY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before selected 2024 window; 2024 market label is stable KOSDAQ GLOBAL","independent_evidence_weight":0.95,"score_price_alignment":"memory parts/consumable recovery route captured 43% MFE, but full-window collapse required C10 4B cycle audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C10 symbol; avoids static top-covered C10 names"}
{"row_type":"case","case_id":"C10_TCK_064760_2024_03_06_SIC_RING_MEMORY_CONSUMABLE_RECOVERY_4B","symbol":"064760","company_name":"티씨케이","round":"R2","loop":"125","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SIC_RING_CONSUMABLE_MEMORY_RECOVERY_ORDER_CYCLE_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"TCK_064760_2024_03_06_STAGE2A_MEMORY_CONSUMABLE_RECOVERY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"SiC ring / memory consumable recovery route captured 55% MFE, but post-peak drawdown required C10 4B cycle audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"clean profile with zero corporate-action candidates; strong C10 4B positive"}
{"row_type":"case","case_id":"C10_HANSOLCHEM_014680_2024_03_06_MEMORY_CHEMICAL_BETA_FAIL","symbol":"014680","company_name":"한솔케미칼","round":"R2","loop":"125","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CHEMICAL_MATERIAL_RECOVERY_BETA_WITHOUT_ORDER_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"HANSOLCHEM_014680_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_CHEMICAL_BETA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before selected 2024 window; material/equipment-cycle boundary, independent weight reduced","independent_evidence_weight":0.9,"score_price_alignment":"memory chemical/material recovery beta produced only low-teens MFE and later deep MAE without equipment order, margin, revision or FCF bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C10 symbol; boundary case with materials but useful recovery-beta failure guard"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"HANAMATERIALS_166090_2024_03_06_STAGE2A_MEMORY_PARTS_RECOVERY","case_id":"C10_HANAMATERIALS_166090_2024_03_06_MEMORY_PARTS_CONSUMABLE_RECOVERY_4B","symbol":"166090","company_name":"하나머티리얼즈","round":"R2","loop":"125","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_PARTS_CONSUMABLE_RECOVERY_ORDER_CYCLE_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":48400.0,"evidence_available_at_that_date":"source_proxy_only: memory recovery, parts/consumable order-cycle expectation, utilization recovery and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_recovery_cycle","parts_consumable_order_cycle","utilization_recovery","relative_strength"],"stage3_evidence_fields":["order_conversion_partial","margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["cycle_peak_watch","valuation_rerating","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv","profile_path":"atlas/symbol_profiles/166/166090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.07,"MFE_90D_pct":43.18,"MFE_180D_pct":43.18,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-5.79,"MAE_90D_pct":-5.79,"MAE_180D_pct":-53.31,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-02","peak_price":69300.0,"drawdown_after_peak_pct":-67.39,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.7,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"memory_parts_recovery_worked_as_stage2a_but_full_window_drawdown_requires_C10_4B_cycle_audit","four_b_evidence_type":["valuation_rerating","memory_cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C10_166090_2024_03_06_48400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected 2024 window only","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TCK_064760_2024_03_06_STAGE2A_MEMORY_CONSUMABLE_RECOVERY","case_id":"C10_TCK_064760_2024_03_06_SIC_RING_MEMORY_CONSUMABLE_RECOVERY_4B","symbol":"064760","company_name":"티씨케이","round":"R2","loop":"125","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SIC_RING_CONSUMABLE_MEMORY_RECOVERY_ORDER_CYCLE_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":96400.0,"evidence_available_at_that_date":"source_proxy_only: memory recovery, SiC ring/consumable cycle, etch utilization recovery and order-cycle expectation visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["sic_ring_consumable_cycle","memory_recovery_cycle","etch_utilization_recovery","relative_strength"],"stage3_evidence_fields":["order_conversion_partial","margin_bridge_partial","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["cycle_peak_watch","valuation_rerating","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv","profile_path":"atlas/symbol_profiles/064/064760.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":44.29,"MFE_90D_pct":55.5,"MFE_180D_pct":55.5,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-3.11,"MAE_90D_pct":-3.11,"MAE_180D_pct":-29.57,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":149900.0,"drawdown_after_peak_pct":-54.7,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.64,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"sic_ring_memory_consumable_recovery_worked_but_full_window_peak_requires_C10_4B_cycle_audit","four_b_evidence_type":["valuation_rerating","memory_cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_064760_2024_03_06_96400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HANSOLCHEM_014680_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_CHEMICAL_BETA","case_id":"C10_HANSOLCHEM_014680_2024_03_06_MEMORY_CHEMICAL_BETA_FAIL","symbol":"014680","company_name":"한솔케미칼","round":"R2","loop":"125","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CHEMICAL_MATERIAL_RECOVERY_BETA_WITHOUT_ORDER_MARGIN_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":190700.0,"evidence_available_at_that_date":"source_proxy_only: memory chemical/material recovery beta and relative strength visible, but equipment order conversion, margin bridge, revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_chemical_material_beta","memory_recovery_narrative","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","bridge_absent","full_window_drawdown"],"stage4c_evidence_fields":["equipment_order_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014680/2024.csv","profile_path":"atlas/symbol_profiles/014/014680.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.22,"MFE_90D_pct":12.22,"MFE_180D_pct":12.22,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.82,"MAE_90D_pct":-9.23,"MAE_180D_pct":-48.19,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-21","peak_price":214000.0,"drawdown_after_peak_pct":-53.83,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.89,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"memory_chemical_beta_not_C10_stage3_without_equipment_order_margin_revision_bridge","four_b_evidence_type":["weak_follow_through","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["material_equipment_cycle_boundary_reduced_weight"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C10_014680_2024_03_06_190700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected 2024 window; C10-material boundary","independent_evidence_weight":0.9,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C10_HANAMATERIALS_166090_2024_03_06_MEMORY_PARTS_CONSUMABLE_RECOVERY_4B","trigger_id":"HANAMATERIALS_166090_2024_03_06_STAGE2A_MEMORY_PARTS_RECOVERY","symbol":"166090","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage2-watch with C10 4B cycle audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Memory parts recovery worked, but Green needs real consumable order, margin, revision and FCF conversion.","MFE_90D_pct":43.18,"MAE_90D_pct":-5.79,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C10_TCK_064760_2024_03_06_SIC_RING_MEMORY_CONSUMABLE_RECOVERY_4B","trigger_id":"TCK_064760_2024_03_06_STAGE2A_MEMORY_CONSUMABLE_RECOVERY","symbol":"064760","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage2-watch with C10 4B cycle audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"SiC ring consumable cycle produced high MFE, but full-window drawdown still needs cycle 4B audit before Green.","MFE_90D_pct":55.5,"MAE_90D_pct":-3.11,"score_return_alignment_label":"positive_high_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C10_HANSOLCHEM_014680_2024_03_06_MEMORY_CHEMICAL_BETA_FAIL","trigger_id":"HANSOLCHEM_014680_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_CHEMICAL_BETA","symbol":"014680","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":59,"stage_label_before":"Stage2 false-positive / memory material beta risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":46,"stage_label_after":"Stage1/4C-watch, not C10 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Material recovery beta without equipment order/margin/revision bridge produced low MFE and deep 180D MAE.","MFE_90D_pct":12.22,"MAE_90D_pct":-9.23,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"125","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_2 rolling calibrated profile.

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
completed_loop = 125
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```

If this loop is accepted, C10 moves to projected 24 rows and still needs 6 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C10 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/014/014680/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/166/166090.json
  - atlas/symbol_profiles/064/064760.json
  - atlas/symbol_profiles/014/014680.json
- Avoided static C10 top-covered symbols:
  - 036930, 074600, 003160, 031980, 036540, 039030
- Discarded duplicate attempt:
  - e2r_stock_web_v12_residual_round_R2_loop_124_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
