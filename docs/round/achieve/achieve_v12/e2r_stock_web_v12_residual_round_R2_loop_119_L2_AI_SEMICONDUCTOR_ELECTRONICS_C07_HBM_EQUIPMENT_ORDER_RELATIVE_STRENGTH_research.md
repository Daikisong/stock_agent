# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_119_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
selected_round: R2
selected_loop: 119
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_ANNEAL_PROCESS_EQUIPMENT_ORDER_RS_4B_WATCH
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

This loop adds 3 new independent C07 rows and moves C07 from static 18 rows to local projected 21 after loop118, then to projected 24 after this loop. It still needs 6 rows to reach the 30-row stability threshold.

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

C07 is the HBM equipment order/relative-strength archetype. Relative strength is a thermometer, not the heat source. The heat source is confirmed order conversion, customer capex, margin, revision, and FCF.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C07 static rows | 18 |
| C07 need to 30 | 12 |
| C07 need to 50 | 32 |
| C07 investigation point | HBM 장비 상대강도와 실제 order/revision 연결 여부 |
| local C07 loop118 projected rows | 21 |
| this loop projected rows | 24 |

Selected symbols avoid local C07 loop118 symbols `042700`, `110990`, and `412350`.

| symbol | company | status |
|---|---|---|
| 122640 | 예스티 | new local C07 symbol; reduced weight due to 2024 share-count drift watch |
| 403870 | HPSP | new local C07 symbol; reduced weight due to market-label/share-count drift watch |
| 053610 | 프로텍 | new local C07 symbol |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated C07 memory.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 122640 / 2024-03-06 | true | true | profile_clean_but_2024_share_count_drift_watch | true, reduced weight 0.80 |
| 403870 / 2024-03-06 | true | true | profile_clean_after_2023_but_2024_label_switch_share_count_drift_watch | true, reduced weight 0.80 |
| 053610 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.95 |

Corporate-action notes:

- 예스티 has old profile corporate-action candidates, but 2024 share-count drift is visible in the row stream, so the row is retained with reduced independent evidence weight.
- HPSP has old 2023 corporate-action candidates and a 2024 market-label switch/share-count drift watch, so it is retained as a reduced-weight false-positive guard case.
- 프로텍 has old 2005/2006 corporate-action candidates only; selected 2024 window is treated as clean.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| HBM_ANNEAL_PROCESS_EQUIPMENT_ORDER_RS_4B_WATCH | C07 | HBM/process equipment RS can support Stage2A, but needs order/revision bridge and 4B audit |
| PROCESS_EQUIPMENT_RELATIVE_STRENGTH_WITHOUT_HBM_ORDER_REVISION_BRIDGE | C07 | process equipment RS without HBM order/revision bridge is false-positive risk |
| ADVANCED_PACKAGING_EQUIPMENT_RS_WITHOUT_HBM_ORDER_REVISION_BRIDGE | C07 | advanced packaging equipment RS without confirmed HBM order/revision bridge is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C07_YEST_122640_2024_03_06_HBM_ANNEAL_EQUIPMENT_ORDER_RS_RERATING_4B | 122640 | 예스티 | 4B_overlay_success | positive | HBM/process equipment RS produced 28.33% MFE and then drawdown |
| C07_HPSP_403870_2024_03_06_PROCESS_EQUIPMENT_RS_FALSE_POSITIVE | 403870 | HPSP | failed_rerating | counterexample | process equipment RS had almost no MFE and severe MAE without HBM order/revision |
| C07_PROTEC_053610_2024_03_06_ADVANCED_PACKAGING_EQUIPMENT_RS_FAIL | 053610 | 프로텍 | failed_rerating | counterexample | advanced packaging RS had only 7% MFE and deep drawdown |

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
| 122640 | source_proxy_only | HBM/process equipment RS and order-cycle expectation | required before promotion |
| 403870 | source_proxy_only | process equipment RS but HBM order/revision bridge absent | required; useful as counterexample |
| 053610 | source_proxy_only | advanced packaging RS but HBM order/revision bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 122640 | atlas/ohlcv_tradable_by_symbol_year/122/122640/2024.csv | atlas/symbol_profiles/122/122640.json |
| 403870 | atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv | atlas/symbol_profiles/403/403870.json |
| 053610 | atlas/ohlcv_tradable_by_symbol_year/053/053610/2024.csv | atlas/symbol_profiles/053/053610.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| YEST_122640_2024_03_06_STAGE2A_HBM_ANNEAL_EQUIPMENT_RS | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 23300 | HBM/process-equipment RS with order-cycle expectation |
| HPSP_403870_2024_03_06_STAGE2_FALSE_POSITIVE_PROCESS_EQUIPMENT_RS | Stage2 | 2024-03-06 | 2024-03-06 | 58000 | process-equipment RS without HBM order/revision bridge |
| PROTEC_053610_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_PACKAGING_RS | Stage2 | 2024-03-06 | 2024-03-06 | 52600 | advanced-packaging RS without HBM order/revision bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 122640 | 2024-03-06 | 23300 | 28.33 | -20.99 | 28.33 | -26.35 | 28.33 | -38.54 | 2024-03-27 | 29900 | -52.11 |
| 403870 | 2024-03-06 | 58000 | 2.24 | -30.52 | 2.24 | -37.59 | 2.24 | -59.14 | 2024-03-07 | 59300 | -60.03 |
| 053610 | 2024-03-06 | 52600 | 7.03 | -23.00 | 7.03 | -41.92 | 7.03 | -56.46 | 2024-03-12 | 56300 | -59.15 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 122640 | Stage2A possible; 4B/share-count audit after HBM-process equipment RS | useful MFE but drawdown and dilution caveat | current_profile_4B_too_late |
| 403870 | Stage2 risk if process-equipment RS is over-credited | low MFE and severe MAE | current_profile_false_positive |
| 053610 | Stage2 risk if advanced packaging RS is over-credited | low MFE and high MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C07 interpretation:

- Stage2A can work when relative strength is tied to HBM equipment order conversion, customer capex, margin, revision, and FCF.
- Yellow/Green require non-price order/revision evidence.
- Process-equipment or advanced-packaging RS without HBM order/revision bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 122640 | 1.00 | 1.00 | HBM/process equipment RS / share-count drift watch | 4B audit required |
| 403870 | 1.00 | 1.00 | process equipment RS / weak follow-through | not Stage3 without HBM order/revision bridge |
| 053610 | 1.00 | 1.00 | advanced packaging RS / bridge absent | not Stage3 without HBM order/revision bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 122640 | thesis_break_watch_only | not hard 4C, but 4B and share-count audit needed |
| 403870 | hard_4c_late | HBM order/revision bridge absence should have capped Stage2 earlier |
| 053610 | hard_4c_late | HBM order/revision bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, HBM-equipment relative strength can support Stage2A only when order conversion, customer capex, margin bridge, revision, or FCF is visible. Process-equipment or advanced-packaging RS without that bridge should not become Yellow/Green.

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

if process_equipment_RS and hbm_order_revision_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 25 and drawdown_after_peak < -35:
    add C07_peak_proximity_4B_audit = true

if MFE_90D < 10 and MAE_90D < -25 and bridge_absent:
    classify_as C07_equipment_RS_false_positive_guardrail

if share_count_drift_watch:
    reduce_independent_evidence_weight = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 12.53 | -35.29 | 12.53 | -51.38 | 2 | useful but C07 bridge too loose |
| P0b calibrated rollback | rollback | 3 | 12.53 | -35.29 | 12.53 | -51.38 | 2 | over-credits process-equipment RS |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 28.33 | -26.35 | 28.33 | -38.54 | 0 | better after order/revision bridge gate |
| P2 canonical_archetype_candidate_profile | C07 | 1 promoted + 2 guard | 28.33 | -26.35 | 28.33 | -38.54 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C07 guard | 1 promoted + 2 guard | 28.33 | -26.35 | 28.33 | -38.54 | 0 | adds process/packaging RS false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 122640 | Stage2A aligned; 4B/share-count audit needed | current_profile_4B_too_late |
| 403870 | Stage2 false positive if order/revision bridge not enforced | current_profile_false_positive |
| 053610 | Stage2 false positive if HBM order bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | mixed C07 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 18 -> local 21 -> projected 24; still need 6 to reach 30 |

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
new_axis_proposed: C07_hbm_equipment_order_revision_bridge_required|C07_peak_proximity_4B_audit|C07_equipment_RS_false_positive_guardrail|share_count_drift_independent_weight_reduction
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
- Avoids local C07 loop118 symbols.
- Keeps 122640 and 403870 with reduced weights due to 2024 share-count drift/market-label watch.
- Keeps 053610 as clean-window false-positive guard.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count any repeated loop118 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C07_hbm_equipment_order_revision_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"403870/053610 show process-equipment or advanced-packaging RS can fail without HBM order/revision bridge while 122640 works only as Stage2A with 4B/share-count audit","blocks two false positives while preserving 122640 Stage2A","YEST_122640_2024_03_06_STAGE2A_HBM_ANNEAL_EQUIPMENT_RS|HPSP_403870_2024_03_06_STAGE2_FALSE_POSITIVE_PROCESS_EQUIPMENT_RS|PROTEC_053610_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_PACKAGING_RS",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C07_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"122640 HBM/process equipment RS needed full-window 4B audit after MFE and drawdown","adds 4B audit after C07 MFE without converting price-only peaks into Green","YEST_122640_2024_03_06_STAGE2A_HBM_ANNEAL_EQUIPMENT_RS",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C07_equipment_RS_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"403870/053610 had low MFE and high MAE after equipment RS premiums","requires confirmed order/customer capex/margin/revision/FCF bridge before Stage2/Yellow promotion","HPSP_403870_2024_03_06_STAGE2_FALSE_POSITIVE_PROCESS_EQUIPMENT_RS|PROTEC_053610_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_PACKAGING_RS",2,2,2,medium,canonical_shadow_only,"false-positive guardrail"
shadow_weight,share_count_drift_independent_weight_reduction,archetype_specific_quality_flag,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"122640/403870 have 2024 share-count or market-label drift during the validation window","keeps rows usable but lowers independent evidence weight","YEST_122640_2024_03_06_STAGE2A_HBM_ANNEAL_EQUIPMENT_RS|HPSP_403870_2024_03_06_STAGE2_FALSE_POSITIVE_PROCESS_EQUIPMENT_RS",2,2,1,medium,quality_shadow_only,"not a scoring alpha; validation-quality guard"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C07_YEST_122640_2024_03_06_HBM_ANNEAL_EQUIPMENT_ORDER_RS_RERATING_4B","symbol":"122640","company_name":"예스티","round":"R2","loop":"119","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_ANNEAL_PROCESS_EQUIPMENT_ORDER_RS_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"YEST_122640_2024_03_06_STAGE2A_HBM_ANNEAL_EQUIPMENT_RS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"profile corporate-action candidates are old, but 2024 share-count drift is flagged; independent weight reduced","independent_evidence_weight":0.8,"score_price_alignment":"HBM/process equipment relative-strength route captured 28% MFE, but post-peak drawdown required C07 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C07 symbol versus loop118; share-count drift watch"}
{"row_type":"case","case_id":"C07_HPSP_403870_2024_03_06_PROCESS_EQUIPMENT_RS_FALSE_POSITIVE","symbol":"403870","company_name":"HPSP","round":"R2","loop":"119","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"PROCESS_EQUIPMENT_RELATIVE_STRENGTH_WITHOUT_HBM_ORDER_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"HPSP_403870_2024_03_06_STAGE2_FALSE_POSITIVE_PROCESS_EQUIPMENT_RS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"market label switch and share-count drift watch; C07 false-positive use only","independent_evidence_weight":0.8,"score_price_alignment":"process-equipment relative strength without HBM order/revision bridge produced almost no MFE and then high MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C07 symbol; market label switch to KOSDAQ GLOBAL and share-count drift watch"}
{"row_type":"case","case_id":"C07_PROTEC_053610_2024_03_06_ADVANCED_PACKAGING_EQUIPMENT_RS_FAIL","symbol":"053610","company_name":"프로텍","round":"R2","loop":"119","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"ADVANCED_PACKAGING_EQUIPMENT_RS_WITHOUT_HBM_ORDER_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"PROTEC_053610_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_PACKAGING_RS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before selected 2024 window","independent_evidence_weight":0.95,"score_price_alignment":"advanced packaging/equipment relative-strength premium produced only 7% MFE and then deep MAE without order/revision bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C07 symbol; old corporate-action candidates outside selected window"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"YEST_122640_2024_03_06_STAGE2A_HBM_ANNEAL_EQUIPMENT_RS","case_id":"C07_YEST_122640_2024_03_06_HBM_ANNEAL_EQUIPMENT_ORDER_RS_RERATING_4B","symbol":"122640","company_name":"예스티","round":"R2","loop":"119","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_ANNEAL_PROCESS_EQUIPMENT_ORDER_RS_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_equipment_order_relative_strength","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":23300.0,"evidence_available_at_that_date":"source_proxy_only: HBM/process equipment relative strength, anneal/equipment route, order-cycle expectation, and event strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_process_equipment_route","anneal_equipment_route","relative_strength","order_cycle_expectation"],"stage3_evidence_fields":["order_conversion_partial","margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","share_count_drift_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/122/122640/2024.csv","profile_path":"atlas/symbol_profiles/122/122640.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.33,"MFE_90D_pct":28.33,"MFE_180D_pct":28.33,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-20.99,"MAE_90D_pct":-26.35,"MAE_180D_pct":-38.54,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-27","peak_price":29900.0,"drawdown_after_peak_pct":-52.11,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"hbm_process_equipment_rs_worked_as_stage2a_but_requires_C07_4B_audit_and_share_count_drift_watch","four_b_evidence_type":["valuation_rerating","share_count_drift_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_mfe_4b_watch_reduced_weight","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["share_count_drift_watch_reduced_weight"],"corporate_action_window_status":"profile_clean_but_2024_share_count_drift_watch","same_entry_group_id":"C07_122640_2024_03_06_23300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"profile corporate-action candidates are old, but 2024 share-count drift is flagged","independent_evidence_weight":0.8,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HPSP_403870_2024_03_06_STAGE2_FALSE_POSITIVE_PROCESS_EQUIPMENT_RS","case_id":"C07_HPSP_403870_2024_03_06_PROCESS_EQUIPMENT_RS_FALSE_POSITIVE","symbol":"403870","company_name":"HPSP","round":"R2","loop":"119","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"PROCESS_EQUIPMENT_RELATIVE_STRENGTH_WITHOUT_HBM_ORDER_REVISION_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_equipment_order_relative_strength","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":58000.0,"evidence_available_at_that_date":"source_proxy_only: process-equipment relative strength and advanced fab equipment premium visible, but confirmed HBM order, revision, margin and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["process_equipment_relative_strength","advanced_fab_equipment_premium"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","market_label_switch","share_count_drift_watch","bridge_absent"],"stage4c_evidence_fields":["hbm_order_absent","revision_bridge_absent","margin_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv","profile_path":"atlas/symbol_profiles/403/403870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.24,"MFE_90D_pct":2.24,"MFE_180D_pct":2.24,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-30.52,"MAE_90D_pct":-37.59,"MAE_180D_pct":-59.14,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":59300.0,"drawdown_after_peak_pct":-60.03,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"process_equipment_rs_not_C07_stage3_without_hbm_order_revision_bridge","four_b_evidence_type":["weak_follow_through","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_bridge_absent_reduced_weight","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["market_label_switch_and_share_count_drift_watch_reduced_weight"],"corporate_action_window_status":"profile_clean_after_2023_but_2024_label_switch_share_count_drift_watch","same_entry_group_id":"C07_403870_2024_03_06_58000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"market label switch and share-count drift watch; false-positive guard use only","independent_evidence_weight":0.8,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"PROTEC_053610_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_PACKAGING_RS","case_id":"C07_PROTEC_053610_2024_03_06_ADVANCED_PACKAGING_EQUIPMENT_RS_FAIL","symbol":"053610","company_name":"프로텍","round":"R2","loop":"119","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"ADVANCED_PACKAGING_EQUIPMENT_RS_WITHOUT_HBM_ORDER_REVISION_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_equipment_order_relative_strength","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":52600.0,"evidence_available_at_that_date":"source_proxy_only: advanced packaging equipment relative-strength premium visible, but confirmed HBM order, revision, margin and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["advanced_packaging_equipment_rs","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","bridge_absent"],"stage4c_evidence_fields":["hbm_order_absent","revision_bridge_absent","margin_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053610/2024.csv","profile_path":"atlas/symbol_profiles/053/053610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.03,"MFE_90D_pct":7.03,"MFE_180D_pct":7.03,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-23.0,"MAE_90D_pct":-41.92,"MAE_180D_pct":-56.46,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-12","peak_price":56300.0,"drawdown_after_peak_pct":-59.15,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"advanced_packaging_rs_not_C07_stage3_without_hbm_order_revision_bridge","four_b_evidence_type":["weak_follow_through","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C07_053610_2024_03_06_52600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected 2024 window only","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C07_YEST_122640_2024_03_06_HBM_ANNEAL_EQUIPMENT_ORDER_RS_RERATING_4B","trigger_id":"YEST_122640_2024_03_06_STAGE2A_HBM_ANNEAL_EQUIPMENT_RS","symbol":"122640","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_after":65,"stage_label_after":"Stage2-watch with C07 4B/share-count audit","changed_components":["valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"HBM/process equipment RS produced MFE, but share-count drift and post-peak drawdown prevent Yellow/Green without order/revision/margin proof.","MFE_90D_pct":28.33,"MAE_90D_pct":-26.35,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C07_HPSP_403870_2024_03_06_PROCESS_EQUIPMENT_RS_FALSE_POSITIVE","trigger_id":"HPSP_403870_2024_03_06_STAGE2_FALSE_POSITIVE_PROCESS_EQUIPMENT_RS","symbol":"403870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2 false-positive / process-equipment RS risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_after":46,"stage_label_after":"Stage1/4C-watch, not C07 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Process-equipment RS without HBM order/revision bridge produced near-zero MFE and high MAE.","MFE_90D_pct":2.24,"MAE_90D_pct":-37.59,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C07_PROTEC_053610_2024_03_06_ADVANCED_PACKAGING_EQUIPMENT_RS_FAIL","trigger_id":"PROTEC_053610_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_PACKAGING_RS","symbol":"053610","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2 false-positive / advanced-packaging RS risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C07 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Advanced-packaging equipment RS without HBM order/revision bridge produced low MFE and severe MAE.","MFE_90D_pct":7.03,"MAE_90D_pct":-41.92,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"119","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 119
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C02_POWER_GRID_DATACENTER_CAPEX, C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING
```

If this loop is accepted together with local C07 loop118, C07 moves to projected 24 rows and still needs 6 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C07 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/122/122640/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/053/053610/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/122/122640.json
  - atlas/symbol_profiles/403/403870.json
  - atlas/symbol_profiles/053/053610.json
- Rejected local duplicate C07 symbols:
  - 042700, 110990, 412350
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
