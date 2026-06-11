# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_121_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
selected_round: R2
selected_loop: 121
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_MEMORY_DEPOSITION_EQUIPMENT_RS_ORDER_REVISION_4B_WATCH
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

This is the corrected valid run after a discarded duplicate loop120 materialization path. C07 was still 3 rows short after loop120, so this loop completes the 30-row stability threshold.

This loop adds 3 new independent C07 rows and moves C07 from static 18 rows to local projected 27 after loops 118/119/120, then to projected 30 after this loop.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_2_rolling_calibrated_proxy`; rollback reference is `calibrated`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C07:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS
C07 -> C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
```

C07 is the HBM equipment order/relative-strength archetype. Relative strength is useful only when it is tied to HBM order conversion, customer capex, margin, revision, and FCF. Otherwise it is a loud signal with no engine behind it.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C07 static rows | 18 |
| C07 need to 30 | 12 |
| C07 need to 50 | 32 |
| C07 investigation point | HBM 장비 상대강도와 실제 order/revision 연결 여부 |
| local C07 loop118 projected rows | 21 |
| local C07 loop119 projected rows | 24 |
| local C07 loop120 projected rows | 27 |
| this loop projected rows | 30 |

Selected symbols avoid local C07 loop118 symbols `042700`, `110990`, `412350`, loop119 symbols `122640`, `403870`, `053610`, and loop120 symbols `039030`, `084370`, `240810`.

| symbol | company | status |
|---|---|---|
| 095610 | 테스 | new local C07 symbol; old corporate-action caveat outside 2024 |
| 036930 | 주성엔지니어링 | new local C07 symbol; C09 boundary, reduced weight |
| 079370 | 제우스 | new local C07 symbol; selected after Jan/Feb 2024 corporate-action candidates |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated C07 memory. The accidental duplicate loop120 materialization path is not counted as new evidence.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 095610 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.95 |
| 036930 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.90 |
| 079370 / 2024-03-06 | true | true | clean_forward_window_after_2024_02_08_candidate | true, reduced weight 0.85 |

Corporate-action notes:

- 테스 has old corporate-action candidates in 2011/2016 only; selected 2024 window is clean.
- 주성엔지니어링 has an old 2000 corporate-action candidate only; selected 2024 window is clean.
- 제우스 has January/February 2024 corporate-action candidates, but the selected entry is after the 2024-02-08 candidate, so the forward window is treated as usable with reduced weight.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| HBM_MEMORY_DEPOSITION_EQUIPMENT_RS_ORDER_REVISION_4B_WATCH | C07 | memory/deposition equipment RS can support Stage2A if order/revision bridge exists; 4B audit required |
| MEMORY_PROCESS_EQUIPMENT_RS_WITHOUT_HBM_ORDER_REVISION_BRIDGE | C07 | memory/process equipment RS without HBM order/revision bridge is false-positive risk |
| WAFER_PROCESS_AUTOMATION_RS_WITHOUT_HBM_ORDER_REVISION_BRIDGE | C07 | wafer/process automation RS without HBM order/revision bridge is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C07_TES_095610_2024_03_06_HBM_DEPOSITION_EQUIPMENT_RS_RERATING_4B | 095610 | 테스 | 4B_overlay_success | positive | HBM/memory deposition RS produced 58% MFE, then 4B drawdown |
| C07_JUSUNG_036930_2024_03_06_MEMORY_PROCESS_EQUIPMENT_RS_FALSE_POSITIVE | 036930 | 주성엔지니어링 | failed_rerating | counterexample | process-equipment RS had low MFE and severe 180D MAE |
| C07_ZEUS_079370_2024_03_06_WAFER_PROCESS_AUTOMATION_RS_FAIL | 079370 | 제우스 | failed_rerating | counterexample | wafer/process automation RS had short MFE and deep MAE |

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
| reduced_weight_caveat_count | 3 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 095610 | source_proxy_only | HBM/memory deposition equipment RS and order-cycle expectation | required before promotion |
| 036930 | source_proxy_only | process equipment RS but HBM order/revision bridge absent | required; useful as counterexample |
| 079370 | source_proxy_only | wafer/process automation RS but HBM order/revision bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 095610 | atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv | atlas/symbol_profiles/095/095610.json |
| 036930 | atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv | atlas/symbol_profiles/036/036930.json |
| 079370 | atlas/ohlcv_tradable_by_symbol_year/079/079370/2024.csv | atlas/symbol_profiles/079/079370.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| TES_095610_2024_03_06_STAGE2A_HBM_DEPOSITION_EQUIPMENT_RS | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 20800 | HBM/memory deposition RS with order-cycle expectation |
| JUSUNG_036930_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_PROCESS_RS | Stage2 | 2024-03-06 | 2024-03-06 | 37350 | memory/process equipment RS without HBM order bridge |
| ZEUS_079370_2024_03_06_STAGE2_FALSE_POSITIVE_WAFER_PROCESS_AUTOMATION_RS | Stage2 | 2024-03-06 | 2024-03-06 | 20400 | wafer/process automation RS without HBM order bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 095610 | 2024-03-06 | 20800 | 58.17 | -9.38 | 58.17 | -9.38 | 58.17 | -32.31 | 2024-04-17 | 32900 | -57.20 |
| 036930 | 2024-03-06 | 37350 | 10.98 | -10.44 | 10.98 | -15.66 | 10.98 | -40.96 | 2024-04-08 | 41450 | -46.80 |
| 079370 | 2024-03-06 | 20400 | 7.60 | -18.38 | 7.60 | -30.49 | 7.60 | -46.52 | 2024-03-07 | 21950 | -50.30 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 095610 | Stage2A possible; 4B after deposition-equipment RS rerating | high MFE, later drawdown | current_profile_4B_too_late |
| 036930 | Stage2 risk if process-equipment RS is over-credited | low MFE and high 180D MAE | current_profile_false_positive |
| 079370 | Stage2 risk if wafer/process automation RS is over-credited | single-digit MFE and deep MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C07 interpretation:

- Stage2A can work when relative strength is tied to HBM equipment order conversion, customer capex, margin, revision, and FCF.
- Yellow/Green require non-price order/revision evidence.
- Process-equipment or wafer automation RS without HBM order/revision bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 095610 | 0.63 | 1.00 | deposition-equipment RS / valuation rerating | full-window 4B audit required |
| 036930 | 0.90 | 1.00 | memory/process equipment RS / weak follow-through | not Stage3 without HBM order/revision bridge |
| 079370 | 0.93 | 1.00 | wafer/process automation RS / bridge absent | not Stage3 without HBM order/revision bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 095610 | thesis_break_watch_only | not hard 4C, but 4B audit needed after rerating |
| 036930 | hard_4c_late | HBM order/revision bridge absence should have capped Stage2 earlier |
| 079370 | hard_4c_late | HBM order/revision bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, HBM-equipment relative strength can support Stage2A only when order conversion, customer capex, margin bridge, revision, or FCF is visible. Generic process-equipment or wafer-automation RS without that bridge should not become Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
confidence = medium
```

Candidate C07 rule:

```text
C07_hbm_equipment_order_revision_bridge_required =
  hbm_equipment_relative_strength_route
  AND (confirmed_order OR customer_capex_conversion OR backlog_visibility OR margin_bridge OR confirmed_revision OR fcf_conversion)

if generic_process_or_wafer_automation_RS and hbm_order_revision_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 25 and drawdown_after_peak < -35:
    add C07_peak_proximity_4B_audit = true

if MFE_90D < 15 and MAE_90D < -15 and bridge_absent:
    classify_as C07_generic_equipment_RS_false_positive_guardrail

if post_corporate_action_candidate_entry:
    reduce_independent_evidence_weight = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 25.58 | -18.51 | 25.58 | -39.93 | 2 | useful but C07 bridge still loose |
| P0b calibrated rollback | rollback | 3 | 25.58 | -18.51 | 25.58 | -39.93 | 2 | over-credits generic equipment RS |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 58.17 | -9.38 | 58.17 | -32.31 | 0 | better after order/revision bridge gate |
| P2 canonical_archetype_candidate_profile | C07 | 1 promoted + 2 guard | 58.17 | -9.38 | 58.17 | -32.31 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C07 guard | 1 promoted + 2 guard | 58.17 | -9.38 | 58.17 | -32.31 | 0 | adds generic equipment RS false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 095610 | Stage2A aligned; 4B audit needed | current_profile_4B_too_late |
| 036930 | Stage2 false positive if HBM order/revision bridge not enforced | current_profile_false_positive |
| 079370 | Stage2 false positive if HBM order/revision bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | mixed C07 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 18 -> local 27 -> projected 30; reaches minimum stability threshold |

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
new_axis_proposed: C07_hbm_equipment_order_revision_bridge_required|C07_peak_proximity_4B_audit|C07_generic_equipment_RS_false_positive_guardrail|post_corporate_action_entry_weight_reduction
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
- Uses C07 Priority 0 coverage gap.
- Avoids local C07 loop118, loop119, and loop120 symbols.
- Keeps 095610 and 036930 with reduced weights due to old corporate-action caveats outside the selected window or C09 boundary overlap.
- Keeps 079370 with reduced weight because the selected entry is after January/February 2024 corporate-action candidates.
- Corrects the discarded duplicate loop120 materialization path by making this the valid loop121 C07 artifact.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count any repeated loop120 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C07_hbm_equipment_order_revision_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"036930/079370 show process-equipment or wafer-automation RS can fail without HBM order/revision bridge while 095610 works only as Stage2A with 4B audit","blocks two false positives while preserving 095610 Stage2A","TES_095610_2024_03_06_STAGE2A_HBM_DEPOSITION_EQUIPMENT_RS|JUSUNG_036930_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_PROCESS_RS|ZEUS_079370_2024_03_06_STAGE2_FALSE_POSITIVE_WAFER_PROCESS_AUTOMATION_RS",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C07_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"095610 HBM/memory deposition RS needed 4B audit after high MFE and drawdown","adds 4B audit after C07 MFE without converting price-only peaks into Green","TES_095610_2024_03_06_STAGE2A_HBM_DEPOSITION_EQUIPMENT_RS",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C07_generic_equipment_RS_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"036930/079370 had low MFE and high MAE after generic equipment RS premiums","requires confirmed HBM order/customer capex/margin/revision/FCF bridge before Stage2/Yellow promotion","JUSUNG_036930_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_PROCESS_RS|ZEUS_079370_2024_03_06_STAGE2_FALSE_POSITIVE_WAFER_PROCESS_AUTOMATION_RS",2,2,2,medium,canonical_shadow_only,"false-positive guardrail"
shadow_weight,post_corporate_action_entry_weight_reduction,archetype_specific_quality_flag,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"079370 entry is after Jan/Feb 2024 corporate-action candidates, so the forward window is usable but should not overcount independent evidence","keeps row usable but lowers independent evidence weight","ZEUS_079370_2024_03_06_STAGE2_FALSE_POSITIVE_WAFER_PROCESS_AUTOMATION_RS",1,1,1,medium,quality_shadow_only,"validation-quality guard"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C07_TES_095610_2024_03_06_HBM_DEPOSITION_EQUIPMENT_RS_RERATING_4B","symbol":"095610","company_name":"테스","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_MEMORY_DEPOSITION_EQUIPMENT_RS_ORDER_REVISION_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"TES_095610_2024_03_06_STAGE2A_HBM_DEPOSITION_EQUIPMENT_RS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before selected 2024 window","independent_evidence_weight":0.95,"score_price_alignment":"HBM/memory deposition equipment relative-strength route captured 58% MFE, but the later full-window drawdown required C07 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C07 symbol versus loops 118/119/120; old corporate-action caveat outside selected window"}
{"row_type":"case","case_id":"C07_JUSUNG_036930_2024_03_06_MEMORY_PROCESS_EQUIPMENT_RS_FALSE_POSITIVE","symbol":"036930","company_name":"주성엔지니어링","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"MEMORY_PROCESS_EQUIPMENT_RS_WITHOUT_HBM_ORDER_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"JUSUNG_036930_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_PROCESS_RS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"static C09 top-covered crossover but C07 order/RS family differs; old corporate-action candidate only in 2000","independent_evidence_weight":0.9,"score_price_alignment":"memory/process equipment RS premium produced only low-teens MFE and then severe 180D MAE without confirmed HBM order/revision bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C07 symbol; useful C07-C09 boundary false-positive guard"}
{"row_type":"case","case_id":"C07_ZEUS_079370_2024_03_06_WAFER_PROCESS_AUTOMATION_RS_FAIL","symbol":"079370","company_name":"제우스","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"WAFER_PROCESS_AUTOMATION_RS_WITHOUT_HBM_ORDER_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"ZEUS_079370_2024_03_06_STAGE2_FALSE_POSITIVE_WAFER_PROCESS_AUTOMATION_RS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"2024 corporate-action candidates are before selected entry; forward window treated as clean but independent weight reduced","independent_evidence_weight":0.85,"score_price_alignment":"wafer/process automation RS premium produced only a short single-digit MFE and then deep MAE without HBM order/revision bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C07 symbol; selected after Jan/Feb 2024 corporate-action candidates"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TES_095610_2024_03_06_STAGE2A_HBM_DEPOSITION_EQUIPMENT_RS","case_id":"C07_TES_095610_2024_03_06_HBM_DEPOSITION_EQUIPMENT_RS_RERATING_4B","symbol":"095610","company_name":"테스","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_MEMORY_DEPOSITION_EQUIPMENT_RS_ORDER_REVISION_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_equipment_order_relative_strength","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":20800.0,"evidence_available_at_that_date":"source_proxy_only: HBM/memory deposition equipment relative strength, memory capex route, order-cycle expectation, and revision expectation visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_memory_deposition_equipment_rs","memory_capex_route","relative_strength","order_cycle_expectation"],"stage3_evidence_fields":["order_conversion_partial","revision_bridge_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv","profile_path":"atlas/symbol_profiles/095/095610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":58.17,"MFE_90D_pct":58.17,"MFE_180D_pct":58.17,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-9.38,"MAE_90D_pct":-9.38,"MAE_180D_pct":-32.31,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-17","peak_price":32900.0,"drawdown_after_peak_pct":-57.2,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.63,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"hbm_memory_deposition_rs_worked_but_full_window_peak_requires_C07_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C07_095610_2024_03_06_20800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected 2024 window only","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"JUSUNG_036930_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_PROCESS_RS","case_id":"C07_JUSUNG_036930_2024_03_06_MEMORY_PROCESS_EQUIPMENT_RS_FALSE_POSITIVE","symbol":"036930","company_name":"주성엔지니어링","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"MEMORY_PROCESS_EQUIPMENT_RS_WITHOUT_HBM_ORDER_REVISION_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_equipment_order_relative_strength","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":37350.0,"evidence_available_at_that_date":"source_proxy_only: memory/process equipment RS and advanced fab equipment premium visible, but confirmed HBM order/revision, margin and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_process_equipment_rs","advanced_fab_equipment_premium","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","bridge_absent","full_window_drawdown"],"stage4c_evidence_fields":["hbm_order_absent","revision_bridge_absent","margin_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv","profile_path":"atlas/symbol_profiles/036/036930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.98,"MFE_90D_pct":10.98,"MFE_180D_pct":10.98,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-10.44,"MAE_90D_pct":-15.66,"MAE_180D_pct":-40.96,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-08","peak_price":41450.0,"drawdown_after_peak_pct":-46.8,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"memory_process_equipment_rs_not_C07_stage3_without_hbm_order_revision_bridge","four_b_evidence_type":["weak_follow_through","bridge_absent","full_window_drawdown"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["cross_canonical_C09_boundary_reduced_weight"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C07_036930_2024_03_06_37350","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"static C09 top-covered crossover but C07 evidence family differs","independent_evidence_weight":0.9,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"ZEUS_079370_2024_03_06_STAGE2_FALSE_POSITIVE_WAFER_PROCESS_AUTOMATION_RS","case_id":"C07_ZEUS_079370_2024_03_06_WAFER_PROCESS_AUTOMATION_RS_FAIL","symbol":"079370","company_name":"제우스","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"WAFER_PROCESS_AUTOMATION_RS_WITHOUT_HBM_ORDER_REVISION_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_equipment_order_relative_strength","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":20400.0,"evidence_available_at_that_date":"source_proxy_only: wafer/process automation relative strength visible after Jan/Feb corporate-action candidates, but confirmed HBM order/revision and margin bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["wafer_process_automation_rs","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","bridge_absent","full_window_drawdown"],"stage4c_evidence_fields":["hbm_order_absent","revision_bridge_absent","margin_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/079/079370/2024.csv","profile_path":"atlas/symbol_profiles/079/079370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.6,"MFE_90D_pct":7.6,"MFE_180D_pct":7.6,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-18.38,"MAE_90D_pct":-30.49,"MAE_180D_pct":-46.52,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":21950.0,"drawdown_after_peak_pct":-50.3,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"wafer_process_automation_rs_not_C07_stage3_without_hbm_order_revision_bridge","four_b_evidence_type":["weak_follow_through","bridge_absent","full_window_drawdown"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["post_2024_02_08_corporate_action_window_reduced_weight"],"corporate_action_window_status":"clean_forward_window_after_2024_02_08_candidate","same_entry_group_id":"C07_079370_2024_03_06_20400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"2024 corporate-action candidates are before selected entry; forward window treated as clean","independent_evidence_weight":0.85,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C07_TES_095610_2024_03_06_HBM_DEPOSITION_EQUIPMENT_RS_RERATING_4B","trigger_id":"TES_095610_2024_03_06_STAGE2A_HBM_DEPOSITION_EQUIPMENT_RS","symbol":"095610","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage2-watch with C07 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"HBM/memory deposition RS produced high MFE, but C07 Stage3 needs confirmed order/revision/margin/FCF conversion.","MFE_90D_pct":58.17,"MAE_90D_pct":-9.38,"score_return_alignment_label":"positive_high_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C07_JUSUNG_036930_2024_03_06_MEMORY_PROCESS_EQUIPMENT_RS_FALSE_POSITIVE","trigger_id":"JUSUNG_036930_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_PROCESS_RS","symbol":"036930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2 false-positive / memory-process RS risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C07 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Memory/process equipment RS without HBM order/revision bridge produced low MFE and high MAE.","MFE_90D_pct":10.98,"MAE_90D_pct":-15.66,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C07_ZEUS_079370_2024_03_06_WAFER_PROCESS_AUTOMATION_RS_FAIL","trigger_id":"ZEUS_079370_2024_03_06_STAGE2_FALSE_POSITIVE_WAFER_PROCESS_AUTOMATION_RS","symbol":"079370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":59,"stage_label_before":"Stage2 false-positive / wafer-process RS risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_after":45,"stage_label_after":"Stage1/4C-watch, not C07 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Wafer/process automation RS after pre-window corporate-action candidates lacked HBM order/revision bridge and collapsed.","MFE_90D_pct":7.6,"MAE_90D_pct":-30.49,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"121","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 121
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY, C02_POWER_GRID_DATACENTER_CAPEX, C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_ONLY_IF_UNCOVERED_FINE_ARCHETYPE
```

If this loop is accepted together with local C07 loops 118, 119, and 120, C07 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C07 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/079/079370/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/095/095610.json
  - atlas/symbol_profiles/036/036930.json
  - atlas/symbol_profiles/079/079370.json
- Rejected local duplicate C07 symbols:
  - 042700, 110990, 412350
  - 122640, 403870, 053610
  - 039030, 084370, 240810
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
