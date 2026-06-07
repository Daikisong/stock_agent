# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R1_loop_108_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
selected_round: R1
selected_loop: 108
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: GRID_TRANSFORMER_BACKLOG_EXPORT_MARGIN_BRIDGE_4B_WATCH
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

This loop adds 3 new independent C01 rows and moves C01 from static 16 rows to local projected 28 after loops 102/105/106/107, then to projected 31 after this loop. The minimum 30-row stability threshold is reached.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C01:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R1 -> L1_INDUSTRIALS_INFRA_DEFENSE_GRID
C01 -> C01_ORDER_BACKLOG_MARGIN_BRIDGE
```

C01 is the industrial order-backlog margin bridge archetype. Backlog is the pipeline. The calibration question is whether price, delivery mix, utilization, margin, revision, working capital, and FCF actually flow through the pipe.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C01 static rows | 16 |
| C01 need to 30 before local loops | 14 |
| C01 investigation point | 수주잔고와 margin bridge가 같이 있는 성공/실패 분리 |
| local C01 loop102 projected rows | 19 |
| local C01 loop105 projected rows | 22 |
| local C01 loop106 projected rows | 25 |
| local C01 loop107 projected rows | 28 |
| this loop projected rows | 31 |

Selected symbols avoid local C01 loop102 symbols `009540`, `010620`, `097230`, loop105 symbols `329180`, `042660`, `047040`, loop106 symbols `064350`, `079550`, `000720`, and loop107 symbols `267260`, `103590`, `375500`.

| symbol | company | status |
|---|---|---|
| 298040 | 효성중공업 | new local C01 symbol |
| 010120 | LS ELECTRIC | new local C01 symbol |
| 006360 | GS건설 | new local C01 symbol |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated memory.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 298040 / 2024-03-06 | true | true | clean_180D_window | true |
| 010120 / 2024-03-06 | true | true | clean_180D_window | true |
| 006360 / 2024-03-06 | true | true | clean_180D_window | true |

Corporate-action notes:

- 효성중공업 has zero corporate-action candidates.
- LS ELECTRIC has corporate-action candidates before 2004 only.
- GS건설 has corporate-action candidates before 2015 only.
- HD현대일렉트릭, 일진전기, DL이앤씨 were rejected as local duplicates from loop107.
- 한화에어로스페이스 remained rejected because the 2024 row stream showed forward-window share-count/trading-gap contamination risk.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| GRID_TRANSFORMER_BACKLOG_EXPORT_MARGIN_BRIDGE_4B_WATCH | C01 | grid transformer backlog + export/margin route can support Stage2A, but peak audit is required |
| GRID_AUTOMATION_BACKLOG_EXPORT_MARGIN_ASP_BRIDGE_4B_WATCH | C01 | electrical/grid automation backlog can work, but full-window 4B audit is mandatory |
| CONSTRUCTION_BACKLOG_HEADLINE_WITHOUT_MARGIN_WORKING_CAPITAL_FCF_BRIDGE | C01 | construction backlog headline without working-capital/FCF conversion is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C01_HYOSUNGHEAVY_298040_2024_03_06_GRID_TRANSFORMER_BACKLOG_MARGIN_RERATING | 298040 | 효성중공업 | 4B_overlay_success | positive | transformer backlog/margin route produced 100%+ MFE and later full-window peak |
| C01_LSELECTRIC_010120_2024_03_06_GRID_AUTOMATION_BACKLOG_MARGIN_RERATING | 010120 | LS ELECTRIC | 4B_overlay_success | positive | grid automation/equipment backlog route produced 200%+ MFE and cycle drawdown |
| C01_GSENC_006360_2024_03_06_CONSTRUCTION_BACKLOG_HEADLINE_MARGIN_FCF_FAIL | 006360 | GS건설 | failed_rerating | counterexample | construction backlog headline had weak 30D/90D MFE and no margin/FCF bridge |

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
| 298040 | source_proxy_only | grid transformer/export backlog and margin bridge route | required before promotion |
| 010120 | source_proxy_only | grid automation/electrical equipment backlog and ASP/margin bridge route | required before promotion |
| 006360 | source_proxy_only | construction backlog headline but margin/working-capital/FCF bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 298040 | atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv | atlas/symbol_profiles/298/298040.json |
| 010120 | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv | atlas/symbol_profiles/010/010120.json |
| 006360 | atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv | atlas/symbol_profiles/006/006360.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| HYOSUNGHEAVY_298040_2024_03_06_STAGE2A_GRID_BACKLOG_MARGIN | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 232000 | grid transformer backlog / export / margin bridge |
| LSELECTRIC_010120_2024_03_06_STAGE2A_GRID_AUTOMATION_BACKLOG_MARGIN | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 79100 | grid automation/equipment backlog / ASP margin |
| GSENC_006360_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG | Stage2 | 2024-03-06 | 2024-03-06 | 15310 | construction backlog headline without margin/FCF bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 298040 | 2024-03-06 | 232000 | 53.88 | -4.53 | 102.16 | -4.53 | 123.28 | -4.53 | 2024-11-12 | 518000 | -26.25 |
| 010120 | 2024-03-06 | 79100 | 103.67 | -3.41 | 247.03 | -3.41 | 247.03 | -3.41 | 2024-07-24 | 274500 | -54.03 |
| 006360 | 2024-03-06 | 15310 | 8.10 | -8.03 | 9.21 | -8.30 | 42.06 | -8.30 | 2024-08-27 | 21750 | -19.31 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 298040 | Stage2A/Yellow/Green-risk; 4B after transformer rerating | 100%+ MFE and later full-window peak watch | current_profile_4B_too_late |
| 010120 | Stage2A/Yellow/Green-risk; 4B after grid automation rerating | 200%+ MFE and deep post-peak drawdown | current_profile_4B_too_late |
| 006360 | Stage2 risk if construction backlog headline is over-credited | weak early MFE and no margin/FCF bridge | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C01 interpretation:

- Stage2A can work when backlog is tied to export order, ASP, delivery mix, margin bridge, revision, and FCF.
- Yellow/Green require realized margin and cash conversion.
- Backlog headline alone should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 298040 | 0.45 | 1.00 | grid transformer rerating / valuation | full-window 4B audit required |
| 010120 | 0.29 | 1.00 | grid automation rerating / cycle peak | full-window 4B audit required |
| 006360 | 0.70 | 1.00 | construction backlog headline / late event spike | not Stage3 without margin/FCF bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 298040 | thesis_break_watch_only | not hard 4C, but 4B cap needed after rerating |
| 010120 | thesis_break_watch_only | not hard 4C, but cycle/valuation cap needed |
| 006360 | hard_4c_late | margin/working-capital/FCF bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
confidence = medium
```

Candidate:

> In L1 industrial backlog names, backlog should promote Stage2A only when delivery mix, ASP, export order quality, margin bridge, revision, working-capital discipline, or FCF conversion is visible. Construction backlog/headline without conversion should be capped at Stage1/Stage2-watch.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C01_ORDER_BACKLOG_MARGIN_BRIDGE
confidence = medium
```

Candidate C01 rule:

```text
C01_backlog_margin_bridge_required =
  order_backlog_or_contract_route
  AND (delivery_mix_bridge OR asp_bridge OR margin_bridge OR confirmed_revision OR working_capital_quality OR fcf_conversion)

if backlog_headline and margin_fcf_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 30 and full_window_peak_proximity == 1.0:
    add C01_peak_proximity_4B_audit = true

if MFE_90D < 10 and margin_fcf_bridge_absent:
    classify_as C01_backlog_headline_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 119.47 | -5.41 | 137.46 | -5.41 | 1 | useful but C01 bridge still loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 119.47 | -5.41 | 137.46 | -5.41 | 1 | over-credits backlog headlines |
| P1 sector_specific_candidate_profile | L1 | 2 promoted + 1 guard | 174.59 | -3.97 | 185.16 | -3.97 | 0 | better after margin/FCF bridge gate |
| P2 canonical_archetype_candidate_profile | C01 | 2 promoted + 1 guard | 174.59 | -3.97 | 185.16 | -3.97 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C01 guard | 2 promoted + 1 guard | 174.59 | -3.97 | 185.16 | -3.97 | 0 | adds backlog headline false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 298040 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 010120 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 006360 | Stage2 false positive if margin/FCF bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C01_ORDER_BACKLOG_MARGIN_BRIDGE | mixed C01 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | static 16 -> local 28 -> projected 31; reaches minimum stability threshold |

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
new_axis_proposed: C01_backlog_margin_bridge_required|C01_peak_proximity_4B_audit|C01_backlog_headline_false_positive_guardrail
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
- Uses C01 Priority 0 coverage gap.
- Avoids local loop102, loop105, loop106, and loop107 C01 symbol/trigger/date combinations.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count the accidental pre-write duplicate loop107 draft in this session as a valid new run.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C01_backlog_margin_bridge_required,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"006360 shows construction backlog headline can fail without margin/working-capital/FCF bridge while 298040/010120 work only as Stage2A with 4B audit","blocks 006360 false positive while preserving 298040/010120 Stage2A","HYOSUNGHEAVY_298040_2024_03_06_STAGE2A_GRID_BACKLOG_MARGIN|LSELECTRIC_010120_2024_03_06_STAGE2A_GRID_AUTOMATION_BACKLOG_MARGIN|GSENC_006360_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C01_peak_proximity_4B_audit,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"298040/010120 backlog-margin reratings needed full-window 4B audit after large MFE","adds 4B audit after large C01 MFE without converting price-only cycle peaks into Green","HYOSUNGHEAVY_298040_2024_03_06_STAGE2A_GRID_BACKLOG_MARGIN|LSELECTRIC_010120_2024_03_06_STAGE2A_GRID_AUTOMATION_BACKLOG_MARGIN",2,2,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C01_backlog_headline_false_positive_guardrail,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"006360 had weak 30D/90D MFE and bridge-absent path after construction backlog headline","requires delivery mix/margin/revision/FCF bridge before Stage2/Yellow promotion","GSENC_006360_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C01_HYOSUNGHEAVY_298040_2024_03_06_GRID_TRANSFORMER_BACKLOG_MARGIN_RERATING","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"108","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"GRID_TRANSFORMER_BACKLOG_EXPORT_MARGIN_BRIDGE_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"HYOSUNGHEAVY_298040_2024_03_06_STAGE2A_GRID_BACKLOG_MARGIN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"grid transformer/export backlog and margin bridge route captured 100%+ MFE, but later full-window peak required C01 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C01 symbol versus loops 102/105/106/107; zero corporate-action candidates in profile"}
{"row_type":"case","case_id":"C01_LSELECTRIC_010120_2024_03_06_GRID_AUTOMATION_BACKLOG_MARGIN_RERATING","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"108","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"GRID_AUTOMATION_BACKLOG_EXPORT_MARGIN_ASP_BRIDGE_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"LSELECTRIC_010120_2024_03_06_STAGE2A_GRID_AUTOMATION_BACKLOG_MARGIN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"grid automation/electrical equipment backlog and ASP/margin route captured 200%+ MFE, but valuation-cycle drawdown required C01 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C01 symbol; old corporate-action candidates are before 2004 and outside the selected 2024 window"}
{"row_type":"case","case_id":"C01_GSENC_006360_2024_03_06_CONSTRUCTION_BACKLOG_HEADLINE_MARGIN_FCF_FAIL","symbol":"006360","company_name":"GS건설","round":"R1","loop":"108","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"CONSTRUCTION_BACKLOG_HEADLINE_WITHOUT_MARGIN_WORKING_CAPITAL_FCF_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"GSENC_006360_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"construction backlog/headline had weak 30D/90D MFE and bridge-absent path before a later event spike, so C01 promotion needed margin/working-capital/FCF proof","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C01 symbol; old corporate-action candidates only before 2015"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"HYOSUNGHEAVY_298040_2024_03_06_STAGE2A_GRID_BACKLOG_MARGIN","case_id":"C01_HYOSUNGHEAVY_298040_2024_03_06_GRID_TRANSFORMER_BACKLOG_MARGIN_RERATING","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"108","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"GRID_TRANSFORMER_BACKLOG_EXPORT_MARGIN_BRIDGE_4B_WATCH","sector":"industrials / grid equipment / order backlog / margin bridge","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":232000.0,"evidence_available_at_that_date":"source_proxy_only: transformer export backlog, grid capex demand, ASP/mix and margin bridge route, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["grid_transformer_backlog","export_order_route","asp_mix_bridge","margin_bridge_partial","relative_strength"],"stage3_evidence_fields":["margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv","profile_path":"atlas/symbol_profiles/298/298040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":53.88,"MFE_90D_pct":102.16,"MFE_180D_pct":123.28,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.53,"MAE_90D_pct":-4.53,"MAE_180D_pct":-4.53,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-12","peak_price":518000.0,"drawdown_after_peak_pct":-26.25,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.45,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"grid_transformer_backlog_margin_route_worked_but_full_window_peak_requires_C01_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_298040_2024_03_06_232000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"LSELECTRIC_010120_2024_03_06_STAGE2A_GRID_AUTOMATION_BACKLOG_MARGIN","case_id":"C01_LSELECTRIC_010120_2024_03_06_GRID_AUTOMATION_BACKLOG_MARGIN_RERATING","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"108","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"GRID_AUTOMATION_BACKLOG_EXPORT_MARGIN_ASP_BRIDGE_4B_WATCH","sector":"industrials / grid automation / order backlog / margin bridge","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":79100.0,"evidence_available_at_that_date":"source_proxy_only: grid automation backlog, export/electrical equipment demand, ASP/mix bridge, margin route, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["grid_automation_backlog","electrical_equipment_order_route","export_order_route","asp_mix_bridge","relative_strength"],"stage3_evidence_fields":["margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":103.67,"MFE_90D_pct":247.03,"MFE_180D_pct":247.03,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-3.41,"MAE_90D_pct":-3.41,"MAE_180D_pct":-3.41,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-24","peak_price":274500.0,"drawdown_after_peak_pct":-54.03,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.29,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"grid_automation_backlog_margin_route_worked_but_cycle_drawdown_requires_C01_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_010120_2024_03_06_79100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"GSENC_006360_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG","case_id":"C01_GSENC_006360_2024_03_06_CONSTRUCTION_BACKLOG_HEADLINE_MARGIN_FCF_FAIL","symbol":"006360","company_name":"GS건설","round":"R1","loop":"108","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"CONSTRUCTION_BACKLOG_HEADLINE_WITHOUT_MARGIN_WORKING_CAPITAL_FCF_BRIDGE","sector":"industrials / construction / order backlog / margin bridge","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":15310.0,"evidence_available_at_that_date":"source_proxy_only: construction backlog/headline and valuation support visible, but margin, working-capital, and FCF conversion bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["construction_backlog_headline","valuation_support_narrative","recovery_theme"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_early_follow_through","late_event_spike","bridge_absent"],"stage4c_evidence_fields":["margin_bridge_absent","working_capital_bridge_absent","fcf_conversion_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.1,"MFE_90D_pct":9.21,"MFE_180D_pct":42.06,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-8.03,"MAE_90D_pct":-8.3,"MAE_180D_pct":-8.3,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-27","peak_price":21750.0,"drawdown_after_peak_pct":-19.31,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.7,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"construction_backlog_headline_had_weak_30D_90D_follow_through_and_not_stage3_without_margin_working_capital_fcf_bridge","four_b_evidence_type":["weak_early_follow_through","late_event_spike","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_weak_early_mfe_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_006360_2024_03_06_15310","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_HYOSUNGHEAVY_298040_2024_03_06_GRID_TRANSFORMER_BACKLOG_MARGIN_RERATING","trigger_id":"HYOSUNGHEAVY_298040_2024_03_06_STAGE2A_GRID_BACKLOG_MARGIN","symbol":"298040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":6,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow/Green-risk with 4B-watch","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":6,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":73,"stage_label_after":"Stage2-Actionable with C01 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Grid transformer backlog/margin route worked, but Green requires realized revision/FCF and full-window 4B audit.","MFE_90D_pct":102.16,"MAE_90D_pct":-4.53,"score_return_alignment_label":"positive_extreme_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_LSELECTRIC_010120_2024_03_06_GRID_AUTOMATION_BACKLOG_MARGIN_RERATING","trigger_id":"LSELECTRIC_010120_2024_03_06_STAGE2A_GRID_AUTOMATION_BACKLOG_MARGIN","symbol":"010120","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":6,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":9,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow/Green-risk with 4B-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":6,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":9,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable with grid automation 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Grid automation/electrical backlog route worked, but Stage3/Green still requires confirmed margin/revision/cash conversion and cycle audit.","MFE_90D_pct":247.03,"MAE_90D_pct":-3.41,"score_return_alignment_label":"positive_extreme_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_GSENC_006360_2024_03_06_CONSTRUCTION_BACKLOG_HEADLINE_MARGIN_FCF_FAIL","trigger_id":"GSENC_006360_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG","symbol":"006360","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C01 Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Construction backlog headline without margin, working-capital, and FCF bridge should not receive C01 promotion; late event spike is not enough.","MFE_90D_pct":9.21,"MAE_90D_pct":-8.3,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"108","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R1
completed_loop = 108
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C15_MATERIAL_SPREAD_SUPERCYCLE, C01_ORDER_BACKLOG_MARGIN_BRIDGE_ONLY_IF_UNCOVERED_FINE_ARCHETYPE
```

If this loop is accepted together with local loops 102, 105, 106, and 107, C01 reaches and exceeds the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C01 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/298/298040.json
  - atlas/symbol_profiles/010/010120.json
  - atlas/symbol_profiles/006/006360.json
- Rejected local duplicates:
  - 267260, 103590, 375500
  - 064350, 079550, 000720
  - 329180, 042660, 047040
  - 009540, 010620, 097230
- Rejected due to candidate forward-window contamination risk:
  - 012450
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
