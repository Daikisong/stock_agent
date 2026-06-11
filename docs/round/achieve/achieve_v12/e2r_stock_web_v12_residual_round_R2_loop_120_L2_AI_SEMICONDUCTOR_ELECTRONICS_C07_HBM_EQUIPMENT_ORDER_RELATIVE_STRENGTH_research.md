# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_120_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
selected_round: R2
selected_loop: 120
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_LASER_ANNEAL_EQUIPMENT_RS_ORDER_REVISION_4B_WATCH
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

This is the valid loop120 run after a discarded duplicate loop119 materialization path. C07 remains the selected gap because C08 and C09 crossed the local 30-row threshold, while C07 is still under-covered.

This loop adds 3 new independent C07 rows and moves C07 from static 18 rows to local projected 24 after loops 118/119, then to projected 27 after this loop. It still needs 3 rows to reach the 30-row stability threshold.

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

C07 is the HBM equipment order/relative-strength archetype. Relative strength is the market pointing at the machine; order conversion, revision, margin, and FCF prove whether the machine is actually earning.

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
| this loop projected rows | 27 |

Selected symbols avoid local C07 loop118 symbols `042700`, `110990`, `412350` and loop119 symbols `122640`, `403870`, `053610`.

| symbol | company | status |
|---|---|---|
| 039030 | 이오테크닉스 | new local C07 symbol; C09 boundary, reduced weight |
| 084370 | 유진테크 | new local C07 symbol; C09 boundary, reduced weight |
| 240810 | 원익IPS | new local C07 symbol; C09 boundary, clean profile, reduced weight |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated C07 memory. The accidental duplicate loop119 materialization path is not counted as new evidence.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 039030 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.85 |
| 084370 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.85 |
| 240810 / 2024-03-06 | true | true | clean_180D_window | true, reduced weight 0.90 |

Corporate-action notes:

- 이오테크닉스 has an old 2003 corporate-action candidate only; selected 2024 window is clean.
- 유진테크 has old corporate-action candidates before 2013 only; selected 2024 window is clean.
- 원익IPS has zero corporate-action candidates.
- All three are C09 boundary names, so C07 independent evidence weights are reduced even though the 2024 price windows are usable.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| HBM_LASER_ANNEAL_EQUIPMENT_RS_ORDER_REVISION_4B_WATCH | C07 | laser/anneal RS can work if tied to order/revision; 4B audit required |
| HBM_PROCESS_EQUIPMENT_RS_ORDER_REVISION_4B_WATCH | C07 | process equipment RS can work if order/revision conversion arrives |
| MEMORY_CAPEX_EQUIPMENT_RS_WITHOUT_HBM_ORDER_REVISION_BRIDGE | C07 | memory-capex RS without HBM order/revision bridge is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C07_EOTECHNICS_039030_2024_03_06_HBM_LASER_ANNEAL_EQUIPMENT_RS_RERATING_4B | 039030 | 이오테크닉스 | 4B_overlay_success | positive | HBM/laser equipment RS produced 36% MFE and then full-window drawdown |
| C07_EUGENETECH_084370_2024_03_06_HBM_PROCESS_EQUIPMENT_RS_RERATING_4B | 084370 | 유진테크 | 4B_overlay_success | positive | HBM/process equipment RS produced 65% MFE and later 4B drawdown |
| C07_WONIKIPS_240810_2024_03_06_MEMORY_CAPEX_EQUIPMENT_RS_FALSE_POSITIVE | 240810 | 원익IPS | failed_rerating | counterexample | memory-capex equipment RS produced tradable MFE but severe full-window MAE without bridge |

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
| reduced_weight_caveat_count | 3 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 039030 | source_proxy_only | HBM/laser anneal equipment RS and order-cycle expectation | required before promotion |
| 084370 | source_proxy_only | HBM/process equipment RS and order-cycle expectation | required before promotion |
| 240810 | source_proxy_only | memory-capex equipment RS but HBM order/revision bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 039030 | atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv | atlas/symbol_profiles/039/039030.json |
| 084370 | atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv | atlas/symbol_profiles/084/084370.json |
| 240810 | atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv | atlas/symbol_profiles/240/240810.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| EOTECHNICS_039030_2024_03_06_STAGE2A_HBM_LASER_ANNEAL_RS | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 206000 | HBM/laser anneal equipment RS with order-cycle expectation |
| EUGENETECH_084370_2024_03_06_STAGE2A_HBM_PROCESS_EQUIPMENT_RS | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 36250 | HBM/process equipment RS with order-cycle expectation |
| WONIKIPS_240810_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_CAPEX_RS | Stage2 | 2024-03-06 | 2024-03-06 | 35100 | memory-capex equipment RS without HBM order/revision bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 039030 | 2024-03-06 | 206000 | 36.41 | -16.70 | 36.41 | -17.28 | 36.41 | -42.96 | 2024-04-12 | 281000 | -58.19 |
| 084370 | 2024-03-06 | 36250 | 51.45 | -5.24 | 65.52 | -5.24 | 65.52 | -9.79 | 2024-05-28 | 60000 | -45.50 |
| 240810 | 2024-03-06 | 35100 | 27.78 | -6.55 | 27.78 | -6.55 | 27.78 | -36.75 | 2024-04-08 | 44850 | -50.50 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 039030 | Stage2A possible; 4B after laser/anneal RS rerating | useful MFE but deep full-window drawdown | current_profile_4B_too_late |
| 084370 | Stage2A possible; 4B after process-equipment RS rerating | high MFE and later drawdown | current_profile_4B_too_late |
| 240810 | Stage2 risk if memory-capex RS is over-credited | MFE but full-window MAE too large without bridge | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C07 interpretation:

- Stage2A can work when relative strength is tied to HBM equipment order conversion, customer capex, margin, revision, and FCF.
- Yellow/Green require non-price order/revision evidence.
- Memory-capex equipment RS without HBM order/revision bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 039030 | 1.00 | 1.00 | laser/anneal equipment RS / valuation rerating | 4B audit required |
| 084370 | 0.60 | 1.00 | process-equipment RS / cycle peak | full-window 4B audit required |
| 240810 | 0.78 | 1.00 | memory-capex RS / bridge absent | not Stage3 without HBM order/revision bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 039030 | thesis_break_watch_only | not hard 4C, but 4B audit needed after rerating |
| 084370 | thesis_break_watch_only | not hard 4C, but valuation/cycle cap needed |
| 240810 | hard_4c_late | HBM order/revision bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, HBM-equipment relative strength can support Stage2A only when order conversion, customer capex, margin bridge, revision, or FCF is visible. Memory-capex equipment RS without HBM-specific order/revision bridge should not become Yellow/Green.

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

if memory_capex_equipment_RS and hbm_order_revision_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 25 and drawdown_after_peak < -35:
    add C07_peak_proximity_4B_audit = true

if MFE_90D > 20 and MAE_180D < -30 and bridge_absent:
    classify_as C07_memory_capex_RS_false_positive_guardrail

if cross_canonical_C09_boundary:
    reduce_independent_evidence_weight = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 43.24 | -9.69 | 43.24 | -29.83 | 1 | useful but C07 bridge still loose |
| P0b calibrated rollback | rollback | 3 | 43.24 | -9.69 | 43.24 | -29.83 | 1 | over-credits equipment RS boundary cases |
| P1 sector_specific_candidate_profile | L2 | 2 promoted + 1 guard | 50.96 | -11.26 | 50.96 | -26.38 | 0 | better after order/revision bridge gate |
| P2 canonical_archetype_candidate_profile | C07 | 2 promoted + 1 guard | 50.96 | -11.26 | 50.96 | -26.38 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C07 guard | 2 promoted + 1 guard | 50.96 | -11.26 | 50.96 | -26.38 | 0 | adds memory-capex RS false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 039030 | Stage2A aligned; 4B audit needed | current_profile_4B_too_late |
| 084370 | Stage2A aligned; 4B audit needed | current_profile_4B_too_late |
| 240810 | Stage2 false positive if HBM order/revision bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | mixed C07 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | static 18 -> local 24 -> projected 27; still need 3 to reach 30 |

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
new_axis_proposed: C07_hbm_equipment_order_revision_bridge_required|C07_peak_proximity_4B_audit|C07_memory_capex_RS_false_positive_guardrail|cross_canonical_C09_boundary_weight_reduction
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
- Avoids local C07 loop118 and loop119 symbols.
- Keeps 039030/084370/240810 with reduced weights due to C07-C09 boundary overlap.
- Corrects the discarded duplicate loop119 materialization path by making this the valid loop120 C07 artifact.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count any repeated loop119 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C07_hbm_equipment_order_revision_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"240810 shows memory-capex equipment RS can fail without HBM order/revision bridge while 039030/084370 work only as Stage2A with 4B audit","blocks 240810 false positive while preserving 039030/084370 Stage2A","EOTECHNICS_039030_2024_03_06_STAGE2A_HBM_LASER_ANNEAL_RS|EUGENETECH_084370_2024_03_06_STAGE2A_HBM_PROCESS_EQUIPMENT_RS|WONIKIPS_240810_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_CAPEX_RS",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C07_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"039030/084370 HBM equipment RS reratings needed 4B audit after MFE and drawdown","adds 4B audit after C07 MFE without converting price-only peaks into Green","EOTECHNICS_039030_2024_03_06_STAGE2A_HBM_LASER_ANNEAL_RS|EUGENETECH_084370_2024_03_06_STAGE2A_HBM_PROCESS_EQUIPMENT_RS",2,2,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C07_memory_capex_RS_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"240810 had tradable MFE but severe full-window MAE after memory-capex equipment RS without HBM order/revision bridge","requires confirmed order/customer capex/margin/revision/FCF bridge before Stage2/Yellow promotion","WONIKIPS_240810_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_CAPEX_RS",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
shadow_weight,cross_canonical_C09_boundary_weight_reduction,archetype_specific_quality_flag,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"039030/084370/240810 are C07-C09 boundary names; rows are useful but should not overcount C07 independent evidence","keeps rows usable but lowers independent evidence weight","EOTECHNICS_039030_2024_03_06_STAGE2A_HBM_LASER_ANNEAL_RS|EUGENETECH_084370_2024_03_06_STAGE2A_HBM_PROCESS_EQUIPMENT_RS|WONIKIPS_240810_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_CAPEX_RS",3,3,1,medium,quality_shadow_only,"validation-quality guard"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C07_EOTECHNICS_039030_2024_03_06_HBM_LASER_ANNEAL_EQUIPMENT_RS_RERATING_4B","symbol":"039030","company_name":"이오테크닉스","round":"R2","loop":"120","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_LASER_ANNEAL_EQUIPMENT_RS_ORDER_REVISION_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"EOTECHNICS_039030_2024_03_06_STAGE2A_HBM_LASER_ANNEAL_RS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"static C09 top-covered crossover but C07 order/RS family differs; old corporate-action candidate only in 2003","independent_evidence_weight":0.85,"score_price_alignment":"laser/anneal HBM-equipment RS route captured 36%+ MFE, but later full-window drawdown required C07 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C07 symbol versus loops 118/119; reduced weight due to C09 boundary"}
{"row_type":"case","case_id":"C07_EUGENETECH_084370_2024_03_06_HBM_PROCESS_EQUIPMENT_RS_RERATING_4B","symbol":"084370","company_name":"유진테크","round":"R2","loop":"120","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_PROCESS_EQUIPMENT_RS_ORDER_REVISION_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"EUGENETECH_084370_2024_03_06_STAGE2A_HBM_PROCESS_EQUIPMENT_RS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"static C09 top-covered crossover but C07 HBM process-equipment RS family differs; old corporate-action candidates only before 2013","independent_evidence_weight":0.85,"score_price_alignment":"HBM/process-equipment RS route captured 65% MFE, then post-peak drawdown required C07 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C07 symbol; market label changes are not treated as corporate-action contamination"}
{"row_type":"case","case_id":"C07_WONIKIPS_240810_2024_03_06_MEMORY_CAPEX_EQUIPMENT_RS_FALSE_POSITIVE","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"120","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"MEMORY_CAPEX_EQUIPMENT_RS_WITHOUT_HBM_ORDER_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"WONIKIPS_240810_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_CAPEX_RS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"static C09 top-covered crossover; clean profile with zero corporate-action candidates","independent_evidence_weight":0.9,"score_price_alignment":"memory-capex/equipment RS premium produced a tradable MFE but then severe full-window MAE without confirmed HBM order/revision bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C07 symbol; useful C07-C09 boundary counterexample"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"EOTECHNICS_039030_2024_03_06_STAGE2A_HBM_LASER_ANNEAL_RS","case_id":"C07_EOTECHNICS_039030_2024_03_06_HBM_LASER_ANNEAL_EQUIPMENT_RS_RERATING_4B","symbol":"039030","company_name":"이오테크닉스","round":"R2","loop":"120","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_LASER_ANNEAL_EQUIPMENT_RS_ORDER_REVISION_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_equipment_order_relative_strength","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":206000.0,"evidence_available_at_that_date":"source_proxy_only: HBM/laser anneal equipment relative strength, advanced packaging route, order-cycle expectation, and revision expectation visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_laser_anneal_equipment_rs","advanced_packaging_route","relative_strength","order_cycle_expectation"],"stage3_evidence_fields":["order_conversion_partial","revision_bridge_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv","profile_path":"atlas/symbol_profiles/039/039030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.41,"MFE_90D_pct":36.41,"MFE_180D_pct":36.41,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-16.7,"MAE_90D_pct":-17.28,"MAE_180D_pct":-42.96,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-12","peak_price":281000.0,"drawdown_after_peak_pct":-58.19,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"hbm_laser_anneal_rs_worked_but_full_window_peak_requires_C07_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_mfe_4b_watch_reduced_weight","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["cross_canonical_C09_boundary_reduced_weight"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C07_039030_2024_03_06_206000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"static C09 top-covered crossover but C07 order/RS family differs","independent_evidence_weight":0.85,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"EUGENETECH_084370_2024_03_06_STAGE2A_HBM_PROCESS_EQUIPMENT_RS","case_id":"C07_EUGENETECH_084370_2024_03_06_HBM_PROCESS_EQUIPMENT_RS_RERATING_4B","symbol":"084370","company_name":"유진테크","round":"R2","loop":"120","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_PROCESS_EQUIPMENT_RS_ORDER_REVISION_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_equipment_order_relative_strength","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":36250.0,"evidence_available_at_that_date":"source_proxy_only: HBM/process equipment relative strength, advanced memory capex route, order-cycle expectation, and revision expectation visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_process_equipment_rs","advanced_memory_capex_route","relative_strength","order_cycle_expectation"],"stage3_evidence_fields":["order_conversion_partial","revision_bridge_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv","profile_path":"atlas/symbol_profiles/084/084370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":51.45,"MFE_90D_pct":65.52,"MFE_180D_pct":65.52,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-5.24,"MAE_90D_pct":-5.24,"MAE_180D_pct":-9.79,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-28","peak_price":60000.0,"drawdown_after_peak_pct":-45.5,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.6,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"hbm_process_equipment_rs_worked_but_full_window_peak_requires_C07_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch_reduced_weight","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["cross_canonical_C09_boundary_reduced_weight"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C07_084370_2024_03_06_36250","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"static C09 top-covered crossover but C07 order/RS family differs","independent_evidence_weight":0.85,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"WONIKIPS_240810_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_CAPEX_RS","case_id":"C07_WONIKIPS_240810_2024_03_06_MEMORY_CAPEX_EQUIPMENT_RS_FALSE_POSITIVE","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"120","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"MEMORY_CAPEX_EQUIPMENT_RS_WITHOUT_HBM_ORDER_REVISION_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_equipment_order_relative_strength","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":35100.0,"evidence_available_at_that_date":"source_proxy_only: memory-capex equipment RS and advanced fab equipment premium visible, but confirmed HBM order/revision/margin and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_capex_equipment_rs","advanced_fab_equipment_premium","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","bridge_absent","full_window_drawdown"],"stage4c_evidence_fields":["hbm_order_absent","revision_bridge_absent","margin_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv","profile_path":"atlas/symbol_profiles/240/240810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.78,"MFE_90D_pct":27.78,"MFE_180D_pct":27.78,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-6.55,"MAE_90D_pct":-6.55,"MAE_180D_pct":-36.75,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-08","peak_price":44850.0,"drawdown_after_peak_pct":-50.5,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"memory_capex_equipment_rs_not_C07_stage3_without_hbm_order_revision_bridge","four_b_evidence_type":["event_premium","bridge_absent","full_window_drawdown"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mfe_but_high_full_window_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["cross_canonical_C09_boundary_reduced_weight"],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C07_240810_2024_03_06_35100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"static C09 top-covered crossover; clean profile with zero corporate-action candidates","independent_evidence_weight":0.9,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C07_EOTECHNICS_039030_2024_03_06_HBM_LASER_ANNEAL_EQUIPMENT_RS_RERATING_4B","trigger_id":"EOTECHNICS_039030_2024_03_06_STAGE2A_HBM_LASER_ANNEAL_RS","symbol":"039030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage2-watch with C07 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Laser/anneal equipment RS produced MFE, but C07 Stage3 requires confirmed HBM order/revision/margin bridge.","MFE_90D_pct":36.41,"MAE_90D_pct":-17.28,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C07_EUGENETECH_084370_2024_03_06_HBM_PROCESS_EQUIPMENT_RS_RERATING_4B","trigger_id":"EUGENETECH_084370_2024_03_06_STAGE2A_HBM_PROCESS_EQUIPMENT_RS","symbol":"084370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":9,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":9,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-watch with C07 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Process-equipment RS produced high MFE, but full-window drawdown says Green still needs order/revision/margin/FCF conversion.","MFE_90D_pct":65.52,"MAE_90D_pct":-5.24,"score_return_alignment_label":"positive_high_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C07_WONIKIPS_240810_2024_03_06_MEMORY_CAPEX_EQUIPMENT_RS_FALSE_POSITIVE","trigger_id":"WONIKIPS_240810_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_CAPEX_RS","symbol":"240810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage2 false-positive / memory-capex RS risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Stage1/4C-watch, not C07 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Memory-capex equipment RS without HBM order/revision bridge produced tradable MFE but severe full-window MAE.","MFE_90D_pct":27.78,"MAE_90D_pct":-6.55,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"120","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 120
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C02_POWER_GRID_DATACENTER_CAPEX, C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING
```

If this loop is accepted together with local C07 loops 118 and 119, C07 moves to projected 27 rows and still needs 3 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C07 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/039/039030.json
  - atlas/symbol_profiles/084/084370.json
  - atlas/symbol_profiles/240/240810.json
- Rejected local duplicate C07 symbols:
  - 042700, 110990, 412350
  - 122640, 403870, 053610
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
