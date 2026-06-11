# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R1_loop_102_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
selected_round: R1
selected_loop: 102
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_BACKLOG_MARGIN_DELIVERY_MIX_RERATING_4B_WATCH
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

This loop adds 3 new independent C01 rows and moves C01 from static 16 rows to projected 19 rows. It remains below the 30-row stability threshold.

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

C01 is the general industrial order-backlog margin bridge archetype. The backlog is the warehouse receipt; the calibration question is whether delivery mix, ASP, OPM, working capital, revision, and FCF actually turn that receipt into cash.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C01 static rows | 16 |
| C01 need to 30 | 14 |
| C01 need to 50 | 34 |
| C01 investigation point | 수주잔고와 margin bridge가 같이 있는 성공/실패 분리 |
| local previous C01 rows in this session | 0 |
| this loop projected rows | 19 |

The compact No-Repeat Index snapshot does not expose top-covered C01 symbols. This loop therefore prioritizes new local symbols, clean 2024 windows, and non-overlapping trigger keys.

Selected symbols:

| symbol | company | status |
|---|---|---|
| 009540 | HD한국조선해양 | new local C01 symbol |
| 010620 | HD현대미포 | new local C01 symbol |
| 097230 | HJ중공업 | new local C01 symbol |

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
| 009540 / 2024-03-06 | true | true | clean_180D_window | true |
| 010620 / 2024-03-06 | true | true | clean_180D_window | true |
| 097230 / 2024-03-06 | true | true | clean_180D_window | true |

Corporate-action notes:

- HD한국조선해양 has corporate-action candidates before 2019 only.
- HD현대미포 has corporate-action candidates before 2019 only. It has later inactive-like status in the profile, but the selected 2024 calibration window is usable.
- HJ중공업 has corporate-action candidates before 2020 only.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| SHIPBUILDING_BACKLOG_MARGIN_DELIVERY_MIX_RERATING_4B_WATCH | C01 | backlog + delivery mix + margin bridge can support Stage2A, but peak audit is required |
| MID_SIZE_SHIP_BACKLOG_TURNAROUND_MARGIN_BRIDGE_4B_WATCH | C01 | turnaround backlog path can work when margin/working-capital bridge is visible |
| SHIPBUILDING_CONSTRUCTION_BACKLOG_HEADLINE_WITHOUT_MARGIN_FCF_BRIDGE | C01 | backlog headline without margin/FCF conversion is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C01_KSOE_009540_2024_03_06_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE_RERATING | 009540 | HD한국조선해양 | 4B_overlay_success | positive | backlog/margin route produced large MFE with low early MAE |
| C01_HDMIPO_010620_2024_03_06_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_RERATING | 010620 | HD현대미포 | 4B_overlay_success | positive | turnaround backlog route produced extreme MFE and low MAE |
| C01_HJSHIP_097230_2024_03_06_BACKLOG_HEADLINE_MARGIN_BRIDGE_FAIL | 097230 | HJ중공업 | failed_rerating | counterexample | backlog headline lacked margin/FCF conversion and later produced high MAE |

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
| 009540 | source_proxy_only | backlog/delivery mix/margin bridge route | required before promotion |
| 010620 | source_proxy_only | backlog turnaround/margin bridge route | required before promotion |
| 097230 | source_proxy_only | backlog headline but margin/FCF bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 009540 | atlas/ohlcv_tradable_by_symbol_year/009/009540/2024.csv | atlas/symbol_profiles/009/009540.json |
| 010620 | atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv | atlas/symbol_profiles/010/010620.json |
| 097230 | atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv | atlas/symbol_profiles/097/097230.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| KSOE_009540_2024_03_06_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 112400 | shipbuilding backlog / delivery mix / margin bridge |
| HDMIPO_010620_2024_03_06_STAGE2A_BACKLOG_TURNAROUND_MARGIN | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 61300 | mid-size ship backlog / margin turnaround |
| HJSHIP_097230_2024_03_06_STAGE2_FALSE_POSITIVE_BACKLOG_HEADLINE | Stage2 | 2024-03-06 | 2024-03-06 | 3405 | backlog headline without delivery mix / margin / FCF bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 009540 | 2024-03-06 | 112400 | 14.77 | -2.76 | 63.70 | -2.76 | 89.50 | -2.76 | 2024-08-01 | 213000 | -23.76 |
| 010620 | 2024-03-06 | 61300 | 17.46 | -4.08 | 70.64 | -4.08 | 100.33 | -4.08 | 2024-07-31 | 122800 | -25.49 |
| 097230 | 2024-03-06 | 3405 | 9.25 | -15.57 | 11.16 | -15.57 | 11.16 | -35.39 | 2024-06-19 | 3785 | -41.88 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 009540 | Stage2A/Yellow possible; 4B after rerating | high MFE and low MAE, later peak watch | current_profile_4B_too_late |
| 010620 | Stage2A/Yellow possible; 4B after turnaround rerating | extreme MFE and low MAE, later peak watch | current_profile_4B_too_late |
| 097230 | Stage2 risk if backlog headline is over-credited | low MFE and high 180D MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C01 interpretation:

- Stage2A can work when backlog is tied to delivery mix, ASP, margin bridge, revision, and FCF.
- Yellow/Green require realized margin and conversion evidence.
- Backlog headline alone should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 009540 | 0.53 | 1.00 | valuation / shipbuilding cycle peak | full-window 4B audit required |
| 010620 | 0.50 | 1.00 | turnaround rerating / cycle peak | full-window 4B audit required |
| 097230 | 0.90 | 1.00 | weak follow-through / margin bridge absent | not Stage3 without margin/FCF bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 009540 | thesis_break_watch_only | not hard 4C, but 4B cap needed after rerating |
| 010620 | thesis_break_watch_only | not hard 4C, but cycle/valuation cap needed |
| 097230 | hard_4c_late | margin/FCF bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
confidence = medium
```

Candidate:

> In L1 industrial backlog names, backlog should promote Stage2A only when delivery mix, ASP, margin bridge, revision, working-capital discipline, or FCF conversion is visible. Backlog/headline without conversion should be capped at Stage1/Stage2-watch.

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

if MFE_90D > 50 and full_window_peak_proximity == 1.0:
    add C01_peak_proximity_4B_audit = true

if MFE_90D < 15 and MAE_180D < -30:
    classify_as C01_backlog_headline_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 48.5 | -7.47 | 67.0 | -14.08 | 1 | useful but C01 bridge still loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 48.5 | -7.47 | 67.0 | -14.08 | 1 | over-credits backlog headlines |
| P1 sector_specific_candidate_profile | L1 | 2 promoted + 1 guard | 67.17 | -3.42 | 94.91 | -3.42 | 0 | better after margin/FCF bridge gate |
| P2 canonical_archetype_candidate_profile | C01 | 2 promoted + 1 guard | 67.17 | -3.42 | 94.91 | -3.42 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C01 guard | 2 promoted + 1 guard | 67.17 | -3.42 | 94.91 | -3.42 | 0 | adds backlog headline false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 009540 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 010620 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 097230 | Stage2 false positive if margin/FCF bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C01_ORDER_BACKLOG_MARGIN_BRIDGE | mixed C01 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | static 16 -> projected 19; still need 11 to reach 30 |

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
- Uses three local-new C01 symbol/trigger/date combinations.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C01_backlog_margin_bridge_required,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"097230 shows backlog headline can fail without margin/FCF bridge while 009540/010620 work only as Stage2A with 4B audit","blocks 097230 false positive while preserving 009540/010620 Stage2A","KSOE_009540_2024_03_06_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN|HDMIPO_010620_2024_03_06_STAGE2A_BACKLOG_TURNAROUND_MARGIN|HJSHIP_097230_2024_03_06_STAGE2_FALSE_POSITIVE_BACKLOG_HEADLINE",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C01_peak_proximity_4B_audit,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"009540/010620 backlog-margin reratings needed full-window 4B audit after large MFE","adds 4B audit after large C01 MFE without converting price-only cycle peaks into Green","KSOE_009540_2024_03_06_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN|HDMIPO_010620_2024_03_06_STAGE2A_BACKLOG_TURNAROUND_MARGIN",2,2,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C01_backlog_headline_false_positive_guardrail,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"097230 had low MFE and high 180D MAE after backlog headline","requires delivery mix/margin/revision/FCF bridge before Stage2/Yellow promotion","HJSHIP_097230_2024_03_06_STAGE2_FALSE_POSITIVE_BACKLOG_HEADLINE",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C01_KSOE_009540_2024_03_06_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE_RERATING","symbol":"009540","company_name":"HD한국조선해양","round":"R1","loop":"102","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_MARGIN_DELIVERY_MIX_RERATING_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"KSOE_009540_2024_03_06_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"shipbuilding backlog, delivery mix, and margin bridge route captured large 90D/180D MFE, but later peak proximity required C01 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C01 symbol in current local memory; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C01_HDMIPO_010620_2024_03_06_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_RERATING","symbol":"010620","company_name":"HD현대미포","round":"R1","loop":"102","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"MID_SIZE_SHIP_BACKLOG_TURNAROUND_MARGIN_BRIDGE_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"HDMIPO_010620_2024_03_06_STAGE2A_BACKLOG_TURNAROUND_MARGIN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mid-size ship backlog and margin-turnaround route captured high MFE with small early MAE, then required 4B cycle audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"2024 window is clean despite old corporate-action candidates and later inactive-like status after 2025 corporate history"}
{"row_type":"case","case_id":"C01_HJSHIP_097230_2024_03_06_BACKLOG_HEADLINE_MARGIN_BRIDGE_FAIL","symbol":"097230","company_name":"HJ중공업","round":"R1","loop":"102","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_CONSTRUCTION_BACKLOG_HEADLINE_WITHOUT_MARGIN_FCF_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"HJSHIP_097230_2024_03_06_STAGE2_FALSE_POSITIVE_BACKLOG_HEADLINE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"backlog/headline route produced only low MFE and then deep 180D MAE because margin, delivery mix, and FCF bridge did not convert","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"counterexample for order/backlog headline without realized margin bridge"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"KSOE_009540_2024_03_06_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN","case_id":"C01_KSOE_009540_2024_03_06_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE_RERATING","symbol":"009540","company_name":"HD한국조선해양","round":"R1","loop":"102","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_MARGIN_DELIVERY_MIX_RERATING_4B_WATCH","sector":"industrials / order backlog / margin bridge","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":112400.0,"evidence_available_at_that_date":"source_proxy_only: shipbuilding backlog, high-value vessel delivery mix, margin-turnaround route, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["order_backlog_route","delivery_mix_route","margin_bridge_partial","relative_strength"],"stage3_evidence_fields":["margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009540/2024.csv","profile_path":"atlas/symbol_profiles/009/009540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.77,"MFE_90D_pct":63.7,"MFE_180D_pct":89.5,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-2.76,"MAE_90D_pct":-2.76,"MAE_180D_pct":-2.76,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-01","peak_price":213000.0,"drawdown_after_peak_pct":-23.76,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.53,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"backlog_margin_rerating_worked_but_later_cycle_peak_requires_C01_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_low_mae_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_009540_2024_03_06_112400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HDMIPO_010620_2024_03_06_STAGE2A_BACKLOG_TURNAROUND_MARGIN","case_id":"C01_HDMIPO_010620_2024_03_06_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_RERATING","symbol":"010620","company_name":"HD현대미포","round":"R1","loop":"102","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"MID_SIZE_SHIP_BACKLOG_TURNAROUND_MARGIN_BRIDGE_4B_WATCH","sector":"industrials / order backlog / margin bridge","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":61300.0,"evidence_available_at_that_date":"source_proxy_only: mid-size ship backlog, turnaround margin bridge, delivery-mix improvement, and orderbook rerating route visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["order_backlog_route","turnaround_margin_route","delivery_mix_route","relative_strength"],"stage3_evidence_fields":["margin_bridge_pending","revision_bridge_pending","working_capital_check_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv","profile_path":"atlas/symbol_profiles/010/010620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.46,"MFE_90D_pct":70.64,"MFE_180D_pct":100.33,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.08,"MAE_90D_pct":-4.08,"MAE_180D_pct":-4.08,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":122800.0,"drawdown_after_peak_pct":-25.49,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.5,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"turnaround_backlog_rerating_worked_but_full_window_peak_requires_C01_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_low_mae_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_010620_2024_03_06_61300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HJSHIP_097230_2024_03_06_STAGE2_FALSE_POSITIVE_BACKLOG_HEADLINE","case_id":"C01_HJSHIP_097230_2024_03_06_BACKLOG_HEADLINE_MARGIN_BRIDGE_FAIL","symbol":"097230","company_name":"HJ중공업","round":"R1","loop":"102","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_CONSTRUCTION_BACKLOG_HEADLINE_WITHOUT_MARGIN_FCF_BRIDGE","sector":"industrials / order backlog / margin bridge","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":3405.0,"evidence_available_at_that_date":"source_proxy_only: backlog/headline and shipbuilding-construction recovery route visible, but delivery mix, margin bridge, and FCF conversion absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["backlog_headline","recovery_theme","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","margin_bridge_absent"],"stage4c_evidence_fields":["delivery_mix_absent","margin_bridge_absent","fcf_conversion_absent","working_capital_risk"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv","profile_path":"atlas/symbol_profiles/097/097230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.25,"MFE_90D_pct":11.16,"MFE_180D_pct":11.16,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-15.57,"MAE_90D_pct":-15.57,"MAE_180D_pct":-35.39,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":3785.0,"drawdown_after_peak_pct":-41.88,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"backlog_headline_not_stage3_without_margin_fcf_bridge","four_b_evidence_type":["weak_follow_through","margin_bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_margin_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_097230_2024_03_06_3405","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_KSOE_009540_2024_03_06_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE_RERATING","trigger_id":"KSOE_009540_2024_03_06_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN","symbol":"009540","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":6,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":6,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":71,"stage_label_after":"Stage2-Actionable with C01 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Backlog/margin route worked, but Green requires realized margin/revision/FCF conversion and later peak audit.","MFE_90D_pct":63.7,"MAE_90D_pct":-2.76,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_HDMIPO_010620_2024_03_06_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_RERATING","trigger_id":"HDMIPO_010620_2024_03_06_STAGE2A_BACKLOG_TURNAROUND_MARGIN","symbol":"010620","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable with backlog-turnaround 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Turnaround backlog route produced strong MFE, but Stage3/Green requires confirmed margin/revision/working-capital conversion.","MFE_90D_pct":70.64,"MAE_90D_pct":-4.08,"score_return_alignment_label":"positive_extreme_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_HJSHIP_097230_2024_03_06_BACKLOG_HEADLINE_MARGIN_BRIDGE_FAIL","trigger_id":"HJSHIP_097230_2024_03_06_STAGE2_FALSE_POSITIVE_BACKLOG_HEADLINE","symbol":"097230","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C01 Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Backlog headline without margin, delivery-mix, and FCF bridge produced weak upside and high MAE.","MFE_90D_pct":11.16,"MAE_90D_pct":-15.57,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"102","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 102
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C15_MATERIAL_SPREAD_SUPERCYCLE
```

If this loop is accepted, C01 moves to projected 19 rows and still needs 11 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C01 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/009/009540/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/009/009540.json
  - atlas/symbol_profiles/010/010620.json
  - atlas/symbol_profiles/097/097230.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
