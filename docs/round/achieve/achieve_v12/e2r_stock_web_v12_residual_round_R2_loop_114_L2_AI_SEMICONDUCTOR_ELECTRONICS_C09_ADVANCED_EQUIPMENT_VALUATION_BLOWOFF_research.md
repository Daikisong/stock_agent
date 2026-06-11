# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_114_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
selected_round: R2
selected_loop: 114
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_PACKAGING_LASER_EQUIPMENT_EVENT_BLOWOFF_4B_WATCH
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

This is the corrected valid run after an accidental loop113 re-materialization attempt. Loop113 already existed; this loop is loop114 and uses new C09 symbol/trigger/date combinations only.

This loop adds 3 new independent C09 rows and moves C09 from static 15 rows to local projected 27 after loops 110/111/112/113, then to projected 30 after this loop. The 30-row stability threshold is reached.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C09:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS
C09 -> C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

C09 is the advanced-equipment valuation blowoff archetype. The spark is “advanced equipment optionality”; the fuse that determines whether it becomes durable value is order conversion, margin, revision, and FCF.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C09 static rows | 15 |
| C09 static symbols | 11 |
| C09 good/bad Stage2 | 6 / 3 |
| C09 4B/4C | 1 / 2 |
| C09 URL pending/proxy | 15 / 9 |
| static top covered symbols | 039030(2), 084370(2), 140860(2), 240810(2), 036810(1), 036930(1) |
| local C09 loop110 projected rows | 18 |
| local C09 loop111 projected rows | 21 |
| local C09 loop112 projected rows | 24 |
| local C09 loop113 projected rows | 27 |
| this loop projected rows | 30 |

Selected symbols avoid static C09 top-covered symbols and local C09 loop110/111/112/113 symbols: `031980`, `348210`, `101490`, `161580`, `089970`, `064290`, `083500`, `322310`, `089790`, `086390`, `036200`, `160980`.

| symbol | company | status |
|---|---|---|
| 089890 | 코세스 | new local C09 symbol; old corporate-action caveat outside selected 2024 window |
| 187870 | 디바이스 / 디바이스이엔지 | new local C09 symbol |
| 281820 | 케이씨텍 | new local C09 symbol |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated C09 memory.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 089890 / 2024-01-24 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.95 |
| 187870 / 2024-03-06 | true | true | clean_180D_window | true |
| 281820 / 2024-03-06 | true | true | clean_180D_window | true |

Corporate-action notes:

- 코세스 has old corporate-action candidates in 2011/2018 only; selected 2024 window is clean.
- 디바이스이엔지 has zero corporate-action candidates. Name changed to 디바이스 after the 2024 trigger window.
- 케이씨텍 has zero corporate-action candidates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| ADVANCED_PACKAGING_LASER_EQUIPMENT_EVENT_BLOWOFF_4B_WATCH | C09 | packaging/laser equipment event can rerate sharply, but requires 4B audit |
| ADVANCED_CLEANING_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_ORDER_MARGIN_REVISION_BRIDGE | C09 | cleaning/process equipment premium without conversion bridge is false-positive risk |
| ADVANCED_CMP_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_SUSTAINED_MARGIN_REVISION_BRIDGE | C09 | CMP/process equipment premium with high MAE needs conversion proof before Stage3 |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C09_KOSES_089890_2024_01_24_ADVANCED_PACKAGING_LASER_EQUIPMENT_BLOWOFF_4B | 089890 | 코세스 | 4B_overlay_success | positive | advanced packaging/laser equipment blowoff produced 40% MFE and then collapsed |
| C09_DEVICEENG_187870_2024_03_06_ADVANCED_CLEANING_EQUIPMENT_PREMIUM_FAIL | 187870 | 디바이스이엔지 | failed_rerating | counterexample | premium had only modest MFE and no conversion bridge |
| C09_KCTECH_281820_2024_03_06_CMP_PROCESS_EQUIPMENT_PREMIUM_FAIL | 281820 | 케이씨텍 | failed_rerating | counterexample | CMP/process-equipment premium had high MAE and missing margin/revision bridge |

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
| reduced_weight_caveat_count | 1 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 089890 | source_proxy_only | advanced packaging / laser equipment event premium | required before promotion |
| 187870 | source_proxy_only | advanced cleaning/process equipment premium but bridge absent | required; useful as counterexample |
| 281820 | source_proxy_only | CMP/process equipment premium but sustained bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 089890 | atlas/ohlcv_tradable_by_symbol_year/089/089890/2024.csv | atlas/symbol_profiles/089/089890.json |
| 187870 | atlas/ohlcv_tradable_by_symbol_year/187/187870/2024.csv | atlas/symbol_profiles/187/187870.json |
| 281820 | atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv | atlas/symbol_profiles/281/281820.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| KOSES_089890_2024_01_24_STAGE2A_ADVANCED_PACKAGING_LASER_EQUIPMENT | Stage2-Actionable | 2024-01-24 | 2024-01-24 | 15660 | advanced packaging / laser equipment event blowoff |
| DEVICEENG_187870_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_CLEANING_EQUIPMENT | Stage2 | 2024-03-06 | 2024-03-06 | 14950 | advanced cleaning/process equipment premium without bridge |
| KCTECH_281820_2024_03_06_STAGE2_FALSE_POSITIVE_CMP_PROCESS_EQUIPMENT | Stage2 | 2024-03-06 | 2024-03-06 | 47600 | CMP/process equipment premium without sustained bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 089890 | 2024-01-24 | 15660 | 40.17 | -16.41 | 40.17 | -16.41 | 40.17 | -45.66 | 2024-01-31 | 21950 | -61.23 |
| 187870 | 2024-03-06 | 14950 | 14.65 | -0.94 | 17.53 | -2.34 | 17.53 | -21.67 | 2024-06-18 | 17570 | -35.40 |
| 281820 | 2024-03-06 | 47600 | 13.66 | -24.37 | 23.95 | -32.04 | 23.95 | -38.13 | 2024-07-11 | 59000 | -50.08 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 089890 | Stage2A/Yellow possible; 4B after event blowoff | high MFE but deep post-peak drawdown | current_profile_4B_too_late |
| 187870 | Stage2 risk if advanced cleaning premium is over-credited | modest MFE and no conversion bridge | current_profile_false_positive |
| 281820 | Stage2 risk if CMP/process equipment premium is over-credited | mid-MFE but high MAE and bridge absent | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C09 interpretation:

- Stage2A can work when advanced equipment exposure is tied to actual order conversion and margin/revision bridge.
- Yellow/Green require order, customer, margin, revision, and FCF confirmation.
- Advanced-equipment label and valuation premium alone should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 089890 | 1.00 | 1.00 | event blowoff / valuation crowding | 4B audit required after blowoff |
| 187870 | 0.85 | 1.00 | premium with weak follow-through | not Stage3 without order/margin bridge |
| 281820 | 0.81 | 1.00 | CMP/process-equipment premium with high MAE | not Stage3 without sustained conversion bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 089890 | thesis_break_watch_only | not hard 4C, but 4B cap needed after blowoff |
| 187870 | hard_4c_late | order/margin/revision bridge absence should have capped Stage2 earlier |
| 281820 | hard_4c_late | sustained margin/revision bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, advanced equipment exposure can support Stage2A only when order conversion, customer confirmation, margin bridge, revision, or FCF is visible. Event-crowded equipment labeling without that bridge should not become Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
confidence = medium
```

Candidate C09 rule:

```text
C09_advanced_equipment_conversion_bridge_required =
  advanced_equipment_or_advanced_materials_route
  AND (order_conversion OR customer_confirmation OR margin_bridge OR confirmed_revision OR fcf_conversion)

if valuation_premium and conversion_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 25 and drawdown_after_peak < -30:
    add C09_peak_proximity_4B_audit = true

if MFE_90D < 25 and MAE_90D < -20:
    classify_as C09_advanced_equipment_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 27.22 | -16.93 | 27.22 | -35.15 | 2 | useful but C09 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 27.22 | -16.93 | 27.22 | -35.15 | 2 | over-credits advanced-equipment premiums |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 40.17 | -16.41 | 40.17 | -45.66 | 0 | better after conversion bridge gate |
| P2 canonical_archetype_candidate_profile | C09 | 1 promoted + 2 guard | 40.17 | -16.41 | 40.17 | -45.66 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C09 guard | 1 promoted + 2 guard | 40.17 | -16.41 | 40.17 | -45.66 | 0 | adds advanced-equipment false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 089890 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 187870 | Stage2 false positive if conversion bridge not enforced | current_profile_false_positive |
| 281820 | Stage2 false positive if sustained bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | mixed C09 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 15 -> local 27 -> projected 30; reaches minimum stability threshold |

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
new_axis_proposed: C09_advanced_equipment_conversion_bridge_required|C09_peak_proximity_4B_audit|C09_advanced_equipment_false_positive_guardrail
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
- Uses C09 Priority 0 coverage gap.
- Avoids static C09 top-covered symbols and local loop110/111/112/113 C09 symbols.
- Keeps 089890 with slightly reduced weight because old corporate-action candidates exist outside the selected 2024 window.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count the accidental loop113 re-materialization as a valid new run.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C09_advanced_equipment_conversion_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"187870/281820 show equipment premiums can fail without order/margin/revision bridge while 089890 works only as Stage2A with 4B audit","blocks two false positives while preserving 089890 Stage2A","KOSES_089890_2024_01_24_STAGE2A_ADVANCED_PACKAGING_LASER_EQUIPMENT|DEVICEENG_187870_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_CLEANING_EQUIPMENT|KCTECH_281820_2024_03_06_STAGE2_FALSE_POSITIVE_CMP_PROCESS_EQUIPMENT",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C09_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"089890 advanced packaging/laser equipment blowoff needed 4B audit after MFE and drawdown","adds 4B audit after C09 MFE without converting price-only peaks into Green","KOSES_089890_2024_01_24_STAGE2A_ADVANCED_PACKAGING_LASER_EQUIPMENT",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C09_advanced_equipment_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"187870/281820 had modest-to-mid MFE with bridge-absent drawdown or high MAE after equipment premiums","requires order/customer/margin/revision/FCF bridge before Stage2/Yellow promotion","DEVICEENG_187870_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_CLEANING_EQUIPMENT|KCTECH_281820_2024_03_06_STAGE2_FALSE_POSITIVE_CMP_PROCESS_EQUIPMENT",2,2,2,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C09_KOSES_089890_2024_01_24_ADVANCED_PACKAGING_LASER_EQUIPMENT_BLOWOFF_4B","symbol":"089890","company_name":"코세스","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_PACKAGING_LASER_EQUIPMENT_EVENT_BLOWOFF_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"KOSES_089890_2024_01_24_STAGE2A_ADVANCED_PACKAGING_LASER_EQUIPMENT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only in 2011/2018; selected 2024 window is clean","independent_evidence_weight":0.95,"score_price_alignment":"advanced packaging / laser equipment event rerating captured 40% MFE, but the post-peak collapse required C09 4B valuation audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C09 symbol versus loops 110/111/112/113; selected 2024-01-24 event window"}
{"row_type":"case","case_id":"C09_DEVICEENG_187870_2024_03_06_ADVANCED_CLEANING_EQUIPMENT_PREMIUM_FAIL","symbol":"187870","company_name":"디바이스","alias_at_trigger":"디바이스이엔지","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_CLEANING_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_ORDER_MARGIN_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"DEVICEENG_187870_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_CLEANING_EQUIPMENT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"advanced cleaning/process-equipment premium produced only a modest MFE and then a long post-peak drawdown without order/margin/revision bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C09 symbol; zero corporate-action candidates in profile; 2025 name changed to 디바이스"}
{"row_type":"case","case_id":"C09_KCTECH_281820_2024_03_06_CMP_PROCESS_EQUIPMENT_PREMIUM_FAIL","symbol":"281820","company_name":"케이씨텍","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_CMP_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_SUSTAINED_MARGIN_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"KCTECH_281820_2024_03_06_STAGE2_FALSE_POSITIVE_CMP_PROCESS_EQUIPMENT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"CMP/process-equipment premium had a tradable MFE but also severe early and full-window MAE, so C09 promotion needed confirmed margin/revision/FCF bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C09 symbol; zero corporate-action candidates in profile"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"KOSES_089890_2024_01_24_STAGE2A_ADVANCED_PACKAGING_LASER_EQUIPMENT","case_id":"C09_KOSES_089890_2024_01_24_ADVANCED_PACKAGING_LASER_EQUIPMENT_BLOWOFF_4B","symbol":"089890","company_name":"코세스","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_PACKAGING_LASER_EQUIPMENT_EVENT_BLOWOFF_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":15660.0,"evidence_available_at_that_date":"source_proxy_only: advanced packaging / laser equipment event premium, semiconductor equipment order-cycle expectation, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["advanced_packaging_laser_equipment","event_repricing","relative_strength","order_cycle_expectation"],"stage3_evidence_fields":["order_conversion_partial","margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_blowoff","event_crowding","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089890/2024.csv","profile_path":"atlas/symbol_profiles/089/089890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":40.17,"MFE_90D_pct":40.17,"MFE_180D_pct":40.17,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-16.41,"MAE_90D_pct":-16.41,"MAE_180D_pct":-45.66,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-31","peak_price":21950.0,"drawdown_after_peak_pct":-61.23,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"advanced_packaging_laser_equipment_blowoff_worked_but_requires_C09_4B_audit","four_b_evidence_type":["valuation_blowoff","event_crowding"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C09_089890_2024_01_24_15660","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only in 2011/2018; selected 2024 window is clean","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"DEVICEENG_187870_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_CLEANING_EQUIPMENT","case_id":"C09_DEVICEENG_187870_2024_03_06_ADVANCED_CLEANING_EQUIPMENT_PREMIUM_FAIL","symbol":"187870","company_name":"디바이스","alias_at_trigger":"디바이스이엔지","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_CLEANING_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_ORDER_MARGIN_REVISION_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":14950.0,"evidence_available_at_that_date":"source_proxy_only: advanced cleaning/process equipment premium visible, but order conversion, margin, revision, and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["advanced_cleaning_process_equipment_premium","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","valuation_premium","bridge_absent"],"stage4c_evidence_fields":["order_conversion_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/187/187870/2024.csv","profile_path":"atlas/symbol_profiles/187/187870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.65,"MFE_90D_pct":17.53,"MFE_180D_pct":17.53,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-0.94,"MAE_90D_pct":-2.34,"MAE_180D_pct":-21.67,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":17570.0,"drawdown_after_peak_pct":-35.4,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"advanced_cleaning_equipment_premium_not_C09_stage3_without_order_margin_revision_bridge","four_b_evidence_type":["valuation_premium","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_modest_mfe_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_187870_2024_03_06_14950","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"KCTECH_281820_2024_03_06_STAGE2_FALSE_POSITIVE_CMP_PROCESS_EQUIPMENT","case_id":"C09_KCTECH_281820_2024_03_06_CMP_PROCESS_EQUIPMENT_PREMIUM_FAIL","symbol":"281820","company_name":"케이씨텍","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_CMP_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_SUSTAINED_MARGIN_REVISION_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":47600.0,"evidence_available_at_that_date":"source_proxy_only: CMP/process equipment premium visible, but sustained order conversion, margin, revision, and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["cmp_process_equipment_premium","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["volatility_after_premium","valuation_premium","bridge_absent"],"stage4c_evidence_fields":["sustained_order_conversion_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv","profile_path":"atlas/symbol_profiles/281/281820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.66,"MFE_90D_pct":23.95,"MFE_180D_pct":23.95,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-24.37,"MAE_90D_pct":-32.04,"MAE_180D_pct":-38.13,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":59000.0,"drawdown_after_peak_pct":-50.08,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.81,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"cmp_process_equipment_premium_not_C09_stage3_without_sustained_margin_revision_bridge","four_b_evidence_type":["valuation_premium","bridge_absent","high_mae"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mid_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_281820_2024_03_06_47600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_KOSES_089890_2024_01_24_ADVANCED_PACKAGING_LASER_EQUIPMENT_BLOWOFF_4B","trigger_id":"KOSES_089890_2024_01_24_STAGE2A_ADVANCED_PACKAGING_LASER_EQUIPMENT","symbol":"089890","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":10,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow / 4B-blowoff risk","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":10,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable with mandatory C09 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Advanced packaging equipment blowoff worked, but event crowding cannot become Green without order/margin/revision/FCF bridge.","MFE_90D_pct":40.17,"MAE_90D_pct":-16.41,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_DEVICEENG_187870_2024_03_06_ADVANCED_CLEANING_EQUIPMENT_PREMIUM_FAIL","trigger_id":"DEVICEENG_187870_2024_03_06_STAGE2_FALSE_POSITIVE_ADVANCED_CLEANING_EQUIPMENT","symbol":"187870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":59,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":46,"stage_label_after":"Stage1/4C-watch, not C09 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Cleaning/process-equipment premium without order/margin/revision bridge produced only modest MFE and a long drawdown.","MFE_90D_pct":17.53,"MAE_90D_pct":-2.34,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_KCTECH_281820_2024_03_06_CMP_PROCESS_EQUIPMENT_PREMIUM_FAIL","trigger_id":"KCTECH_281820_2024_03_06_STAGE2_FALSE_POSITIVE_CMP_PROCESS_EQUIPMENT","symbol":"281820","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2 false-positive / 4B-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":50,"stage_label_after":"Stage1/4C-watch, not C09 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"CMP/process equipment premium had tradable upside, but high MAE and missing conversion bridge block Stage3.","MFE_90D_pct":23.95,"MAE_90D_pct":-32.04,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 114
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C15_MATERIAL_SPREAD_SUPERCYCLE, C02_POWER_GRID_DATACENTER_CAPEX, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_ONLY_IF_UNCOVERED_FINE_ARCHETYPE
```

If this loop is accepted together with loops 110, 111, 112, and 113, C09 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C09 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/089/089890/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/187/187870/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/089/089890.json
  - atlas/symbol_profiles/187/187870.json
  - atlas/symbol_profiles/281/281820.json
- Rejected local duplicate C09 symbols:
  - 031980, 348210, 101490
  - 161580, 089970, 064290
  - 083500, 322310, 089790
  - 086390, 036200, 160980
- Avoided static C09 top-covered symbols:
  - 039030, 084370, 140860, 240810, 036810, 036930
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
