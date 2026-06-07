# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R1_loop_107_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
selected_round: R1
selected_loop: 107
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

This loop adds 3 new independent C01 rows and moves C01 from static 16 rows to local projected 25 after loops 102/105/106, then to projected 28 after this loop. It still needs 2 rows to reach the 30-row minimum stability threshold.

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
| C01 need to 30 | 14 |
| C01 need to 50 | 34 |
| C01 investigation point | 수주잔고와 margin bridge가 같이 있는 성공/실패 분리 |
| local C01 loop102 projected rows | 19 |
| local C01 loop105 projected rows | 22 |
| local C01 loop106 projected rows | 25 |
| this loop projected rows | 28 |

Selected symbols avoid local C01 loop102 symbols `009540`, `010620`, `097230`, loop105 symbols `329180`, `042660`, `047040`, and loop106 symbols `064350`, `079550`, `000720`.

| symbol | company | status |
|---|---|---|
| 267260 | HD현대일렉트릭 | new local C01 symbol |
| 103590 | 일진전기 | new local C01 symbol; post-2024-02-13 candidate window |
| 375500 | DL이앤씨 | new local C01 symbol |

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
| 267260 / 2024-03-06 | true | true | clean_180D_window | true |
| 103590 / 2024-03-06 | true | true | clean_180D_window_after_2024_02_13_candidate | true |
| 375500 / 2024-03-06 | true | true | clean_180D_window | true |

Corporate-action notes:

- HD현대일렉트릭 has corporate-action candidates before 2020 only.
- 일진전기 has a 2024-02-13 corporate-action candidate, but the selected entry is 2024-03-06 and the forward window is post-candidate.
- DL이앤씨 has corporate-action candidates in 2022 only.
- 현대로템/LIG넥스원/현대건설 were rejected in this loop as local duplicates from loop106.
- 한화에어로스페이스 was again rejected because the 2024 row stream has forward-window share-count/trading-gap contamination risk.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| GRID_TRANSFORMER_BACKLOG_EXPORT_MARGIN_BRIDGE_4B_WATCH | C01 | grid transformer backlog + export/margin route can support Stage2A, but peak audit is required |
| GRID_CABLE_TRANSFORMER_BACKLOG_MARGIN_EXPORT_4B_WATCH | C01 | grid cable/transformer backlog can work, but post-rerating 4B audit is mandatory |
| CONSTRUCTION_BACKLOG_HEADLINE_WITHOUT_MARGIN_WORKING_CAPITAL_FCF_BRIDGE | C01 | construction backlog headline without working-capital/FCF conversion is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C01_HDHYUNDAIELECTRIC_267260_2024_03_06_GRID_TRANSFORMER_BACKLOG_MARGIN_RERATING | 267260 | HD현대일렉트릭 | 4B_overlay_success | positive | grid transformer backlog/margin route produced 200%+ 180D MFE |
| C01_ILJINELECTRIC_103590_2024_03_06_GRID_CABLE_BACKLOG_MARGIN_RERATING | 103590 | 일진전기 | 4B_overlay_success | positive | grid cable/transformer backlog route produced 130%+ MFE and then cycle drawdown |
| C01_DLEANDC_375500_2024_03_06_CONSTRUCTION_BACKLOG_MARGIN_FCF_FAIL | 375500 | DL이앤씨 | failed_rerating | counterexample | construction backlog headline produced only single-digit MFE and persistent MAE |

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
| 267260 | source_proxy_only | grid transformer/export backlog and margin bridge route | required before promotion |
| 103590 | source_proxy_only | grid cable/transformer backlog and margin bridge route | required before promotion |
| 375500 | source_proxy_only | construction backlog headline but margin/working-capital/FCF bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 267260 | atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv | atlas/symbol_profiles/267/267260.json |
| 103590 | atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv | atlas/symbol_profiles/103/103590.json |
| 375500 | atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv | atlas/symbol_profiles/375/375500.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| HDHYUNDAIELECTRIC_267260_2024_03_06_STAGE2A_GRID_BACKLOG_MARGIN | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 136000 | grid transformer backlog / export / margin bridge |
| ILJINELECTRIC_103590_2024_03_06_STAGE2A_GRID_CABLE_BACKLOG_MARGIN | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 12930 | grid cable/transformer backlog / export / margin bridge |
| DLEANDC_375500_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG | Stage2 | 2024-03-06 | 2024-03-06 | 35300 | construction backlog headline without margin/FCF bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 267260 | 2024-03-06 | 136000 | 95.22 | -7.35 | 166.91 | -7.35 | 204.04 | -7.35 | 2024-11-12 | 413500 | -19.23 |
| 103590 | 2024-03-06 | 12930 | 89.48 | -7.12 | 133.57 | -7.12 | 133.57 | -7.12 | 2024-07-15 | 30200 | -45.03 |
| 375500 | 2024-03-06 | 35300 | 7.08 | -4.39 | 7.08 | -10.34 | 7.08 | -18.98 | 2024-04-04 | 37800 | -24.34 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 267260 | Stage2A/Yellow/Green-risk; 4B after grid transformer rerating | extreme MFE and later full-window peak watch | current_profile_4B_too_late |
| 103590 | Stage2A/Yellow possible; 4B after grid cable rerating | extreme MFE and later cycle drawdown | current_profile_4B_too_late |
| 375500 | Stage2 risk if construction backlog headline is over-credited | single-digit MFE and persistent MAE | current_profile_false_positive |

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
| 267260 | 0.33 | 1.00 | grid transformer rerating / valuation | full-window 4B audit required |
| 103590 | 0.43 | 1.00 | grid cable rerating / cycle peak | full-window 4B audit required |
| 375500 | 1.00 | 1.00 | construction backlog headline / weak bridge | not Stage3 without margin/FCF bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 267260 | thesis_break_watch_only | not hard 4C, but 4B cap needed after rerating |
| 103590 | thesis_break_watch_only | not hard 4C, but cycle/valuation cap needed |
| 375500 | hard_4c_late | margin/working-capital/FCF bridge absence should have capped Stage2 earlier |

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
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 102.52 | -8.27 | 114.9 | -11.15 | 1 | useful but C01 bridge still loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 102.52 | -8.27 | 114.9 | -11.15 | 1 | over-credits backlog headlines |
| P1 sector_specific_candidate_profile | L1 | 2 promoted + 1 guard | 150.24 | -7.23 | 168.81 | -7.23 | 0 | better after margin/FCF bridge gate |
| P2 canonical_archetype_candidate_profile | C01 | 2 promoted + 1 guard | 150.24 | -7.23 | 168.81 | -7.23 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C01 guard | 2 promoted + 1 guard | 150.24 | -7.23 | 168.81 | -7.23 | 0 | adds backlog headline false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 267260 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 103590 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 375500 | Stage2 false positive if margin/FCF bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C01_ORDER_BACKLOG_MARGIN_BRIDGE | mixed C01 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | static 16 -> local 25 -> projected 28; still need 2 to reach 30 |

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
- Avoids local loop102, loop105, and loop106 C01 symbol/trigger/date combinations.
- Uses a post-corporate-action-candidate entry for 103590.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C01_backlog_margin_bridge_required,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"375500 shows construction backlog headline can fail without margin/working-capital/FCF bridge while 267260/103590 work only as Stage2A with 4B audit","blocks 375500 false positive while preserving 267260/103590 Stage2A","HDHYUNDAIELECTRIC_267260_2024_03_06_STAGE2A_GRID_BACKLOG_MARGIN|ILJINELECTRIC_103590_2024_03_06_STAGE2A_GRID_CABLE_BACKLOG_MARGIN|DLEANDC_375500_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C01_peak_proximity_4B_audit,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"267260/103590 backlog-margin reratings needed full-window 4B audit after large MFE","adds 4B audit after large C01 MFE without converting price-only cycle peaks into Green","HDHYUNDAIELECTRIC_267260_2024_03_06_STAGE2A_GRID_BACKLOG_MARGIN|ILJINELECTRIC_103590_2024_03_06_STAGE2A_GRID_CABLE_BACKLOG_MARGIN",2,2,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C01_backlog_headline_false_positive_guardrail,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"375500 had single-digit MFE and persistent MAE after construction backlog headline","requires delivery mix/margin/revision/FCF bridge before Stage2/Yellow promotion","DLEANDC_375500_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C01_HDHYUNDAIELECTRIC_267260_2024_03_06_GRID_TRANSFORMER_BACKLOG_MARGIN_RERATING","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"107","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"GRID_TRANSFORMER_BACKLOG_EXPORT_MARGIN_BRIDGE_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"HDHYUNDAIELECTRIC_267260_2024_03_06_STAGE2A_GRID_BACKLOG_MARGIN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"grid transformer/export backlog and margin bridge route captured triple-digit MFE, but later full-window peak required C01 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C01 symbol versus loops 102/105/106; old corporate-action candidates only before 2020"}
{"row_type":"case","case_id":"C01_ILJINELECTRIC_103590_2024_03_06_GRID_CABLE_BACKLOG_MARGIN_RERATING","symbol":"103590","company_name":"일진전기","round":"R1","loop":"107","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"GRID_CABLE_TRANSFORMER_BACKLOG_MARGIN_EXPORT_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"ILJINELECTRIC_103590_2024_03_06_STAGE2A_GRID_CABLE_BACKLOG_MARGIN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"2024-02-13 corporate-action candidate is before selected entry; forward window treated as clean","independent_evidence_weight":0.95,"score_price_alignment":"grid cable/transformer backlog route captured large 30D/90D MFE, then later cycle drawdown required C01 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C01 symbol; selected after 2024-02-13 share-count discontinuity"}
{"row_type":"case","case_id":"C01_DLEANDC_375500_2024_03_06_CONSTRUCTION_BACKLOG_MARGIN_FCF_FAIL","symbol":"375500","company_name":"DL이앤씨","round":"R1","loop":"107","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"CONSTRUCTION_BACKLOG_HEADLINE_WITHOUT_MARGIN_WORKING_CAPITAL_FCF_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"DLEANDC_375500_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"construction backlog/headline produced only single-digit MFE and then persistent MAE because margin, working-capital, and FCF bridge did not convert","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C01 symbol; old corporate-action candidates only in 2022"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"HDHYUNDAIELECTRIC_267260_2024_03_06_STAGE2A_GRID_BACKLOG_MARGIN","case_id":"C01_HDHYUNDAIELECTRIC_267260_2024_03_06_GRID_TRANSFORMER_BACKLOG_MARGIN_RERATING","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"107","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"GRID_TRANSFORMER_BACKLOG_EXPORT_MARGIN_BRIDGE_4B_WATCH","sector":"industrials / grid equipment / order backlog / margin bridge","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":136000.0,"evidence_available_at_that_date":"source_proxy_only: transformer export backlog, grid capex demand, ASP/mix and margin bridge route, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["grid_transformer_backlog","export_order_route","asp_mix_bridge","margin_bridge_partial","relative_strength"],"stage3_evidence_fields":["margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv","profile_path":"atlas/symbol_profiles/267/267260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":95.22,"MFE_90D_pct":166.91,"MFE_180D_pct":204.04,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-7.35,"MAE_90D_pct":-7.35,"MAE_180D_pct":-7.35,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-12","peak_price":413500.0,"drawdown_after_peak_pct":-19.23,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.33,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"grid_transformer_backlog_margin_route_worked_but_full_window_peak_requires_C01_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_267260_2024_03_06_136000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"ILJINELECTRIC_103590_2024_03_06_STAGE2A_GRID_CABLE_BACKLOG_MARGIN","case_id":"C01_ILJINELECTRIC_103590_2024_03_06_GRID_CABLE_BACKLOG_MARGIN_RERATING","symbol":"103590","company_name":"일진전기","round":"R1","loop":"107","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"GRID_CABLE_TRANSFORMER_BACKLOG_MARGIN_EXPORT_4B_WATCH","sector":"industrials / grid equipment / order backlog / margin bridge","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":12930.0,"evidence_available_at_that_date":"source_proxy_only: grid cable/transformer backlog, export order route, margin bridge, and relative strength visible after 2024-02 share-count discontinuity; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["grid_cable_backlog","transformer_order_route","export_order_route","margin_bridge_partial","relative_strength"],"stage3_evidence_fields":["margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv","profile_path":"atlas/symbol_profiles/103/103590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":89.48,"MFE_90D_pct":133.57,"MFE_180D_pct":133.57,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-7.12,"MAE_90D_pct":-7.12,"MAE_180D_pct":-7.12,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-15","peak_price":30200.0,"drawdown_after_peak_pct":-45.03,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.43,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"grid_cable_backlog_margin_route_worked_but_cycle_drawdown_requires_C01_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_after_2024_02_13_candidate","same_entry_group_id":"C01_103590_2024_03_06_12930","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"2024-02-13 corporate-action candidate is before selected entry; C01 row uses post-candidate window only","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"DLEANDC_375500_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG","case_id":"C01_DLEANDC_375500_2024_03_06_CONSTRUCTION_BACKLOG_MARGIN_FCF_FAIL","symbol":"375500","company_name":"DL이앤씨","round":"R1","loop":"107","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"CONSTRUCTION_BACKLOG_HEADLINE_WITHOUT_MARGIN_WORKING_CAPITAL_FCF_BRIDGE","sector":"industrials / construction / order backlog / margin bridge","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":35300.0,"evidence_available_at_that_date":"source_proxy_only: construction backlog/headline and valuation support visible, but margin, working-capital, and FCF conversion bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["construction_backlog_headline","valuation_support_narrative","recovery_theme"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","margin_bridge_absent"],"stage4c_evidence_fields":["margin_bridge_absent","working_capital_bridge_absent","fcf_conversion_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv","profile_path":"atlas/symbol_profiles/375/375500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.08,"MFE_90D_pct":7.08,"MFE_180D_pct":7.08,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.39,"MAE_90D_pct":-10.34,"MAE_180D_pct":-18.98,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-04","peak_price":37800.0,"drawdown_after_peak_pct":-24.34,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"construction_backlog_headline_not_stage3_without_margin_working_capital_fcf_bridge","four_b_evidence_type":["weak_follow_through","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_single_digit_mfe_persistent_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_375500_2024_03_06_35300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_HDHYUNDAIELECTRIC_267260_2024_03_06_GRID_TRANSFORMER_BACKLOG_MARGIN_RERATING","trigger_id":"HDHYUNDAIELECTRIC_267260_2024_03_06_STAGE2A_GRID_BACKLOG_MARGIN","symbol":"267260","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":7,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow/Green-risk with 4B-watch","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":7,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable with C01 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Grid backlog/margin route worked, but Green requires realized margin/revision/FCF and full-window 4B audit.","MFE_90D_pct":166.91,"MAE_90D_pct":-7.35,"score_return_alignment_label":"positive_extreme_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_ILJINELECTRIC_103590_2024_03_06_GRID_CABLE_BACKLOG_MARGIN_RERATING","trigger_id":"ILJINELECTRIC_103590_2024_03_06_STAGE2A_GRID_CABLE_BACKLOG_MARGIN","symbol":"103590","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":9,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":9,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":71,"stage_label_after":"Stage2-Actionable with grid/backlog 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Grid cable/backlog route worked, but Stage3/Green still requires confirmed margin/revision/cash conversion.","MFE_90D_pct":133.57,"MAE_90D_pct":-7.12,"score_return_alignment_label":"positive_extreme_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_DLEANDC_375500_2024_03_06_CONSTRUCTION_BACKLOG_MARGIN_FCF_FAIL","trigger_id":"DLEANDC_375500_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG","symbol":"375500","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C01 Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Construction backlog headline without margin, working-capital, and FCF bridge should not receive C01 promotion.","MFE_90D_pct":7.08,"MAE_90D_pct":-10.34,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"107","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 107
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C01_ORDER_BACKLOG_MARGIN_BRIDGE, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C15_MATERIAL_SPREAD_SUPERCYCLE
```

If this loop is accepted together with local loops 102, 105, and 106, C01 moves to projected 28 rows and still needs 2 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C01 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/267/267260.json
  - atlas/symbol_profiles/103/103590.json
  - atlas/symbol_profiles/375/375500.json
- Rejected local duplicates:
  - 064350, 079550, 000720
- Rejected due to candidate forward-window contamination risk:
  - 012450
- Considered but not selected:
  - 006360
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
