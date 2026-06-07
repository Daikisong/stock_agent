# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R1_loop_106_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
selected_round: R1
selected_loop: 106
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: DEFENSE_RAIL_BACKLOG_EXPORT_MARGIN_BRIDGE_4B_WATCH
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

This loop adds 3 new independent C01 rows and moves C01 from static 16 rows to local projected 22 after loops 102/105, then to projected 25 after this loop. It still needs 5 rows to reach the 30-row minimum stability threshold.

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

C01 is the industrial order-backlog margin bridge archetype. Backlog is the reservoir; the stock only re-rates sustainably when the water reaches the turbine: delivery, ASP, margin, revision, working capital, and FCF.

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
| this loop projected rows | 25 |

Selected symbols avoid local C01 loop102 symbols `009540`, `010620`, `097230` and loop105 symbols `329180`, `042660`, `047040`.

| symbol | company | status |
|---|---|---|
| 064350 | 현대로템 | new local C01 symbol |
| 079550 | LIG넥스원 | new local C01 symbol |
| 000720 | 현대건설 | new local C01 symbol |

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
| 064350 / 2024-03-06 | true | true | clean_180D_window | true |
| 079550 / 2024-03-06 | true | true | clean_180D_window | true |
| 000720 / 2024-03-06 | true | true | clean_180D_window | true |

Corporate-action notes:

- 현대로템 has a corporate-action candidate in 2020 only.
- LIG넥스원 has zero corporate-action candidates.
- 현대건설 has corporate-action candidates before 2005 only.
- 한화에어로스페이스(012450) was considered but rejected because the 2024 row stream showed a share-count discontinuity/trading-gap pattern inside the candidate forward window.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| DEFENSE_RAIL_BACKLOG_EXPORT_MARGIN_BRIDGE_4B_WATCH | C01 | defense/rail backlog can support Stage2A if delivery and margin bridge are visible |
| DEFENSE_EXPORT_BACKLOG_MARGIN_REVISION_BRIDGE_4B_WATCH | C01 | defense export backlog can work, but full-window peak requires 4B audit |
| CONSTRUCTION_BACKLOG_HEADLINE_WITHOUT_MARGIN_WORKING_CAPITAL_FCF_BRIDGE | C01 | construction backlog headline without margin/FCF bridge is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C01_HYUNDAIROTEM_064350_2024_03_06_DEFENSE_RAIL_BACKLOG_MARGIN_RERATING | 064350 | 현대로템 | 4B_overlay_success | positive | backlog/export bridge produced triple-digit 180D MFE, then full-window peak audit |
| C01_LIGNEX1_079550_2024_03_06_DEFENSE_BACKLOG_EXPORT_MARGIN_RERATING | 079550 | LIG넥스원 | 4B_overlay_success | positive | defense backlog bridge produced high 90D/180D MFE, then 4B audit |
| C01_HYUNDAIEANDC_000720_2024_03_06_CONSTRUCTION_BACKLOG_MARGIN_FCF_FAIL | 000720 | 현대건설 | failed_rerating | counterexample | construction backlog headline had only 3% MFE and double-digit 180D MAE |

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
| 064350 | source_proxy_only | defense/rail backlog, export delivery, margin bridge route | required before promotion |
| 079550 | source_proxy_only | defense export backlog and margin/revision bridge route | required before promotion |
| 000720 | source_proxy_only | construction backlog headline but margin/working-capital/FCF bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 064350 | atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv | atlas/symbol_profiles/064/064350.json |
| 079550 | atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv | atlas/symbol_profiles/079/079550.json |
| 000720 | atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv | atlas/symbol_profiles/000/000720.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| HYUNDAIROTEM_064350_2024_03_06_STAGE2A_DEFENSE_RAIL_BACKLOG_MARGIN | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 31950 | defense/rail backlog, export delivery, margin bridge |
| LIGNEX1_079550_2024_03_06_STAGE2A_DEFENSE_BACKLOG_MARGIN | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 168500 | defense export backlog and margin/revision bridge |
| HYUNDAIEANDC_000720_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG | Stage2 | 2024-03-06 | 2024-03-06 | 33750 | construction backlog headline without margin/FCF bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 064350 | 2024-03-06 | 31950 | 35.99 | -6.42 | 40.53 | -6.42 | 117.53 | -6.42 | 2024-11-20 | 69500 | -26.04 |
| 079550 | 2024-03-06 | 168500 | 13.53 | -7.95 | 35.31 | -11.04 | 61.13 | -11.04 | 2024-11-08 | 271500 | -26.52 |
| 000720 | 2024-03-06 | 33750 | 3.11 | -4.59 | 3.41 | -6.07 | 3.41 | -13.93 | 2024-07-17 | 34900 | -16.62 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 064350 | Stage2A/Yellow possible; 4B after defense/rail rerating | extreme 180D MFE and later peak watch | current_profile_4B_too_late |
| 079550 | Stage2A/Yellow possible; 4B after defense backlog rerating | high MFE and later peak watch | current_profile_4B_too_late |
| 000720 | Stage2 risk if construction backlog headline is over-credited | low MFE and moderate 180D MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C01 interpretation:

- Stage2A can work when backlog is tied to delivery mix, ASP, margin bridge, revision, and FCF.
- Yellow/Green require realized margin and cash conversion.
- Backlog headline alone should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 064350 | 0.46 | 1.00 | defense/rail rerating / valuation | full-window 4B audit required |
| 079550 | 0.62 | 1.00 | defense export rerating / cycle peak | full-window 4B audit required |
| 000720 | 0.97 | 1.00 | construction backlog headline / weak bridge | not Stage3 without margin/FCF bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 064350 | thesis_break_watch_only | not hard 4C, but 4B cap needed after rerating |
| 079550 | thesis_break_watch_only | not hard 4C, but cycle/valuation cap needed |
| 000720 | hard_4c_late | margin/working-capital/FCF bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
confidence = medium
```

Candidate:

> In L1 industrial backlog names, backlog should promote Stage2A only when delivery mix, ASP, margin bridge, revision, working-capital discipline, or FCF conversion is visible. Construction backlog/headline without conversion should be capped at Stage1/Stage2-watch.

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

if MFE_90D < 5 and margin_fcf_bridge_absent:
    classify_as C01_backlog_headline_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 26.42 | -7.84 | 60.69 | -10.46 | 1 | useful but C01 bridge still loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 26.42 | -7.84 | 60.69 | -10.46 | 1 | over-credits backlog headlines |
| P1 sector_specific_candidate_profile | L1 | 2 promoted + 1 guard | 37.92 | -8.73 | 89.33 | -8.73 | 0 | better after margin/FCF bridge gate |
| P2 canonical_archetype_candidate_profile | C01 | 2 promoted + 1 guard | 37.92 | -8.73 | 89.33 | -8.73 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C01 guard | 2 promoted + 1 guard | 37.92 | -8.73 | 89.33 | -8.73 | 0 | adds backlog headline false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 064350 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 079550 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 000720 | Stage2 false positive if margin/FCF bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C01_ORDER_BACKLOG_MARGIN_BRIDGE | mixed C01 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | static 16 -> local 22 -> projected 25; still need 5 to reach 30 |

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
- Avoids local loop102 and loop105 C01 symbol/trigger/date combinations.
- Rejects 012450 due to 2024 share-count/trading-gap contamination risk inside the forward window.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C01_backlog_margin_bridge_required,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"000720 shows construction backlog headline can fail without margin/working-capital/FCF bridge while 064350/079550 work only as Stage2A with 4B audit","blocks 000720 false positive while preserving 064350/079550 Stage2A","HYUNDAIROTEM_064350_2024_03_06_STAGE2A_DEFENSE_RAIL_BACKLOG_MARGIN|LIGNEX1_079550_2024_03_06_STAGE2A_DEFENSE_BACKLOG_MARGIN|HYUNDAIEANDC_000720_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C01_peak_proximity_4B_audit,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"064350/079550 backlog-margin reratings needed full-window 4B audit after large MFE","adds 4B audit after large C01 MFE without converting price-only cycle peaks into Green","HYUNDAIROTEM_064350_2024_03_06_STAGE2A_DEFENSE_RAIL_BACKLOG_MARGIN|LIGNEX1_079550_2024_03_06_STAGE2A_DEFENSE_BACKLOG_MARGIN",2,2,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C01_backlog_headline_false_positive_guardrail,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"000720 had low MFE and moderate MAE after construction backlog headline","requires delivery mix/margin/revision/FCF bridge before Stage2/Yellow promotion","HYUNDAIEANDC_000720_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C01_HYUNDAIROTEM_064350_2024_03_06_DEFENSE_RAIL_BACKLOG_MARGIN_RERATING","symbol":"064350","company_name":"현대로템","round":"R1","loop":"106","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"DEFENSE_RAIL_BACKLOG_EXPORT_MARGIN_BRIDGE_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"HYUNDAIROTEM_064350_2024_03_06_STAGE2A_DEFENSE_RAIL_BACKLOG_MARGIN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"defense/rail backlog and export-margin bridge route captured triple-digit 180D MFE, but full-window peak required C01 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C01 symbol versus loops 102/105; old 2020 corporate-action candidate only"}
{"row_type":"case","case_id":"C01_LIGNEX1_079550_2024_03_06_DEFENSE_BACKLOG_EXPORT_MARGIN_RERATING","symbol":"079550","company_name":"LIG넥스원","round":"R1","loop":"106","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"DEFENSE_EXPORT_BACKLOG_MARGIN_REVISION_BRIDGE_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"LIGNEX1_079550_2024_03_06_STAGE2A_DEFENSE_BACKLOG_MARGIN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"defense export/backlog and margin-revision bridge route captured 35% 90D and 61% 180D MFE, but late full-window peak required 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C01 symbol; zero corporate-action candidates in profile"}
{"row_type":"case","case_id":"C01_HYUNDAIEANDC_000720_2024_03_06_CONSTRUCTION_BACKLOG_MARGIN_FCF_FAIL","symbol":"000720","company_name":"현대건설","round":"R1","loop":"106","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"CONSTRUCTION_BACKLOG_HEADLINE_WITHOUT_MARGIN_WORKING_CAPITAL_FCF_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"HYUNDAIEANDC_000720_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"construction backlog/headline path had only 3% MFE and later double-digit MAE because margin, working-capital, and FCF bridge did not convert","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C01 symbol; old corporate-action candidates only before 2005"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"HYUNDAIROTEM_064350_2024_03_06_STAGE2A_DEFENSE_RAIL_BACKLOG_MARGIN","case_id":"C01_HYUNDAIROTEM_064350_2024_03_06_DEFENSE_RAIL_BACKLOG_MARGIN_RERATING","symbol":"064350","company_name":"현대로템","round":"R1","loop":"106","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"DEFENSE_RAIL_BACKLOG_EXPORT_MARGIN_BRIDGE_4B_WATCH","sector":"industrials / order backlog / margin bridge","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":31950.0,"evidence_available_at_that_date":"source_proxy_only: defense/rail backlog, export delivery bridge, margin route, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["order_backlog_route","defense_export_route","rail_delivery_route","margin_bridge_partial","relative_strength"],"stage3_evidence_fields":["margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv","profile_path":"atlas/symbol_profiles/064/064350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":35.99,"MFE_90D_pct":40.53,"MFE_180D_pct":117.53,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-6.42,"MAE_90D_pct":-6.42,"MAE_180D_pct":-6.42,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-20","peak_price":69500.0,"drawdown_after_peak_pct":-26.04,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.46,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"defense_rail_backlog_margin_route_worked_but_full_window_peak_requires_C01_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_064350_2024_03_06_31950","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"LIGNEX1_079550_2024_03_06_STAGE2A_DEFENSE_BACKLOG_MARGIN","case_id":"C01_LIGNEX1_079550_2024_03_06_DEFENSE_BACKLOG_EXPORT_MARGIN_RERATING","symbol":"079550","company_name":"LIG넥스원","round":"R1","loop":"106","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"DEFENSE_EXPORT_BACKLOG_MARGIN_REVISION_BRIDGE_4B_WATCH","sector":"industrials / order backlog / margin bridge","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":168500.0,"evidence_available_at_that_date":"source_proxy_only: defense export backlog, missile/electronics delivery route, margin-revision bridge, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["defense_export_backlog","customer_delivery_route","margin_revision_bridge_partial","relative_strength"],"stage3_evidence_fields":["margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv","profile_path":"atlas/symbol_profiles/079/079550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.53,"MFE_90D_pct":35.31,"MFE_180D_pct":61.13,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-7.95,"MAE_90D_pct":-11.04,"MAE_180D_pct":-11.04,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-08","peak_price":271500.0,"drawdown_after_peak_pct":-26.52,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.62,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"defense_export_backlog_margin_route_worked_but_full_window_peak_requires_C01_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_079550_2024_03_06_168500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HYUNDAIEANDC_000720_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG","case_id":"C01_HYUNDAIEANDC_000720_2024_03_06_CONSTRUCTION_BACKLOG_MARGIN_FCF_FAIL","symbol":"000720","company_name":"현대건설","round":"R1","loop":"106","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"CONSTRUCTION_BACKLOG_HEADLINE_WITHOUT_MARGIN_WORKING_CAPITAL_FCF_BRIDGE","sector":"industrials / order backlog / margin bridge","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":33750.0,"evidence_available_at_that_date":"source_proxy_only: construction backlog and recovery headline visible, but margin, working-capital, and FCF conversion bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["construction_backlog_headline","recovery_theme","valuation_support_narrative"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","margin_bridge_absent"],"stage4c_evidence_fields":["margin_bridge_absent","working_capital_bridge_absent","fcf_conversion_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.11,"MFE_90D_pct":3.41,"MFE_180D_pct":3.41,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.59,"MAE_90D_pct":-6.07,"MAE_180D_pct":-13.93,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-17","peak_price":34900.0,"drawdown_after_peak_pct":-16.62,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"construction_backlog_headline_not_stage3_without_margin_working_capital_fcf_bridge","four_b_evidence_type":["weak_follow_through","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_moderate_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_000720_2024_03_06_33750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_HYUNDAIROTEM_064350_2024_03_06_DEFENSE_RAIL_BACKLOG_MARGIN_RERATING","trigger_id":"HYUNDAIROTEM_064350_2024_03_06_STAGE2A_DEFENSE_RAIL_BACKLOG_MARGIN","symbol":"064350","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":6,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":6,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":71,"stage_label_after":"Stage2-Actionable with C01 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Defense/rail backlog route worked, but Green requires realized margin/revision/FCF and full-window 4B audit.","MFE_90D_pct":40.53,"MAE_90D_pct":-6.42,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_LIGNEX1_079550_2024_03_06_DEFENSE_BACKLOG_EXPORT_MARGIN_RERATING","trigger_id":"LIGNEX1_079550_2024_03_06_STAGE2A_DEFENSE_BACKLOG_MARGIN","symbol":"079550","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable with backlog/margin 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Defense export backlog route worked, but Stage3/Green requires confirmed margin/revision/cash conversion.","MFE_90D_pct":35.31,"MAE_90D_pct":-11.04,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_HYUNDAIEANDC_000720_2024_03_06_CONSTRUCTION_BACKLOG_MARGIN_FCF_FAIL","trigger_id":"HYUNDAIEANDC_000720_2024_03_06_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BACKLOG","symbol":"000720","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C01 Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Construction backlog headline without margin, working-capital, and FCF bridge should not receive C01 promotion.","MFE_90D_pct":3.41,"MAE_90D_pct":-6.07,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"106","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 106
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C01_ORDER_BACKLOG_MARGIN_BRIDGE, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C15_MATERIAL_SPREAD_SUPERCYCLE
```

If this loop is accepted together with local loops 102 and 105, C01 moves to projected 25 rows and still needs 5 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C01 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/064/064350.json
  - atlas/symbol_profiles/079/079550.json
  - atlas/symbol_profiles/000/000720.json
- Rejected due to candidate forward-window contamination risk:
  - atlas/symbol_profiles/012/012450.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
