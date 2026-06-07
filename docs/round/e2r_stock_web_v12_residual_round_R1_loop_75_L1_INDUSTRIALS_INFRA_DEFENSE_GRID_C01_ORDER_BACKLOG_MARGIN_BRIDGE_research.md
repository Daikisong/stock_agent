# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R1_loop_75_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
selected_round: R1
selected_loop: 75
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_ORDER_BACKLOG_MARGIN_BRIDGE_4B_WATCH
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

This loop adds 3 new independent cases, 1 counterexample, and 2 residual error types for R1/L1/C01.

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

C01 asks whether an industrial order/backlog signal becomes margin, EPS, and FCF conversion. The failure mode is a headline or cyclical order bounce that never gets a margin bridge.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C01 current rows | 16 |
| C01 current symbols | 12 |
| C01 good/bad Stage2 | 7 / 3 |
| C01 4B/4C | 2 / 2 |
| C01 URL pending/proxy | 16 / 9 |
| top covered symbols | 082740, 267270, 010660, 044450, 054540, 064820 |

Selected symbols avoid the C01 top-covered symbols:

| symbol | company | status |
|---|---|---|
| 010620 | HD현대미포 | new C01 symbol versus top-covered C01 list |
| 329180 | HD현대중공업 | new C01 symbol versus top-covered C01 list |
| 042670 | HD현대인프라코어 | new C01 symbol versus top-covered C01 list |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 010620 / 2024-04-18 | true | true | clean_180D_window | true |
| 329180 / 2024-04-18 | true | true | clean_180D_window | true |
| 042670 / 2024-02-02 | true | true | clean_180D_window | true |

Corporate-action notes:

- 010620 has corporate-action candidates only in 1999, 2004, and 2018; selected 2024 window is clean.
- 329180 has zero corporate-action candidates.
- 042670 has corporate-action candidates only in 2013 and 2021; selected 2024 window is clean.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| SHIPBUILDING_ORDER_BACKLOG_MARGIN_BRIDGE_4B_WATCH | C01 | shipbuilding backlog and margin-turn route; 4B audit after rerating |
| LARGE_SHIPBUILDING_BACKLOG_MARGIN_REVISION_BRIDGE | C01 | large shipbuilding order book, delivery visibility, and margin bridge |
| CONSTRUCTION_EQUIPMENT_ORDER_CYCLE_MARGIN_BRIDGE_ABSENT | C01 | equipment order/cycle bounce without durable margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C01_HDMIPO_010620_2024_04_18_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE | 010620 | HD현대미포 | 4B_overlay_success | positive | backlog/margin bridge captured high MFE; 4B audit needed |
| C01_HHI_329180_2024_04_18_SHIPBUILDING_BACKLOG_MARGIN_RERATING | 329180 | HD현대중공업 | high_mae_success | positive | strong backlog rerating with later peak drawdown |
| C01_HDI_042670_2024_02_02_EQUIPMENT_ORDER_CYCLE_FALSE_POSITIVE | 042670 | HD현대인프라코어 | failed_rerating | counterexample | order/cycle bounce without margin bridge produced low MFE and drawdown |

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
| 010620 | source_proxy_only | backlog/margin-turn route and relative strength | required before promotion |
| 329180 | source_proxy_only | shipbuilding backlog, delivery visibility, margin bridge | required before promotion |
| 042670 | source_proxy_only | order/cycle rebound but margin bridge absent | required; useful as counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 010620 | atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv | atlas/symbol_profiles/010/010620.json |
| 329180 | atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv | atlas/symbol_profiles/329/329180.json |
| 042670 | atlas/ohlcv_tradable_by_symbol_year/042/042670/2024.csv | atlas/symbol_profiles/042/042670.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| HDMIPO_010620_2024_04_18_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE | Stage2-Actionable | 2024-04-18 | 2024-04-18 | 64900 | backlog/margin-turn route |
| HHI_329180_2024_04_18_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE | Stage2-Actionable | 2024-04-18 | 2024-04-18 | 120300 | large backlog/margin rerating |
| HDI_042670_2024_02_02_STAGE2_FALSE_POSITIVE_ORDER_CYCLE_MARGIN_BRIDGE | Stage2 | 2024-02-02 | 2024-02-02 | 8400 | order/cycle rebound without margin bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 010620 | 2024-04-18 | 64900 | 22.34 | -8.17 | 89.21 | -8.17 | 89.21 | -8.17 | 2024-07-31 | 122800 | -24.51 |
| 329180 | 2024-04-18 | 120300 | 21.36 | -6.48 | 84.95 | -6.48 | 84.95 | -6.48 | 2024-08-09 | 222500 | -23.64 |
| 042670 | 2024-02-02 | 8400 | 5.95 | -12.98 | 5.95 | -12.98 | 9.05 | -25.36 | 2024-07-23 | 9160 | -31.55 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 010620 | Stage2A/Yellow possible; 4B after rerating | high MFE then valuation drawdown | current_profile_4B_too_late |
| 329180 | Stage2A/Yellow possible; 4B after rerating | high MFE then post-peak drawdown | current_profile_4B_too_late |
| 042670 | Stage2 risk if cycle/order bounce over-credited | low MFE and high MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C01 interpretation:

- Stage2A can work when backlog plus margin bridge appears.
- Yellow/Green require margin evidence, revision, and cash conversion.
- Order/cycle bounce without margin bridge should not be upgraded.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 010620 | 1.00 | 1.00 | valuation / positioning | good 4B audit after backlog rerating |
| 329180 | 1.00 | 1.00 | valuation / positioning | good 4B audit after large backlog rerating |
| 042670 | 1.00 | 1.00 | price_only / cycle risk | local peak without margin bridge is not full 4B |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 010620 | thesis_break_watch_only | not hard 4C, but 4B cap needed |
| 329180 | thesis_break_watch_only | not hard 4C, but valuation cap needed |
| 042670 | hard_4c_late | margin bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
confidence = low_to_medium
```

Candidate:

> In L1 industrial order/backlog names, Stage2A can be supported by backlog plus delivery visibility. However, Stage3-Yellow/Green requires margin bridge, revision, and cash conversion. If an order/cycle rally lacks margin bridge, cap it at Stage1/Stage2-watch and treat later price peaks as C01 false-positive or 4B audit rows.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C01_ORDER_BACKLOG_MARGIN_BRIDGE
confidence = low_to_medium
```

Candidate C01 rule:

```text
C01_margin_bridge_required =
  backlog_visibility
  AND (margin_bridge OR confirmed_revision OR fcf_conversion)

if order_backlog_or_cycle_signal and margin_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 50 and drawdown_after_peak < -20:
    add C01_peak_proximity_4B_audit = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 60.04 | -9.21 | 61.07 | -13.34 | 1 | useful but margin bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 60.04 | -9.21 | 61.07 | -13.34 | 1 | over-credits order/cycle beta |
| P1 sector_specific_candidate_profile | L1 | 2 promoted + 1 guard | 87.08 | -7.33 | 87.08 | -7.33 | 0 | better after bridge gate |
| P2 canonical_archetype_candidate_profile | C01 | 2 promoted + 1 guard | 87.08 | -7.33 | 87.08 | -7.33 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C01 guard | 2 promoted + 1 guard | 87.08 | -7.33 | 87.08 | -7.33 | 0 | adds margin bridge gate |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 010620 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 329180 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 042670 | Stage2 false positive if margin bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C01_ORDER_BACKLOG_MARGIN_BRIDGE | mixed C01 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | 16 -> projected 19 rows; still need 11 to reach 30 |

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
new_axis_proposed: C01_margin_bridge_required|C01_peak_proximity_4B_audit
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
- Uses C01 Priority 0 coverage gap.
- Uses three symbols not listed among C01 top-covered symbols.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C01_margin_bridge_required,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"042670 shows order/cycle rebound can fail without margin bridge","blocks 042670 false positive while preserving 010620/329180 Stage2A","HDMIPO_010620_2024_04_18_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE|HHI_329180_2024_04_18_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE|HDI_042670_2024_02_02_STAGE2_FALSE_POSITIVE_ORDER_CYCLE_MARGIN_BRIDGE",3,3,1,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C01_peak_proximity_4B_audit,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"010620/329180 high-MFE backlog reratings still needed 4B audit after valuation extension","adds 4B audit after large C01 MFE without turning price-only peaks into full 4B","HDMIPO_010620_2024_04_18_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE|HHI_329180_2024_04_18_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE",2,2,0,low_to_medium,canonical_shadow_only,"4B overlay/risk calibration only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C01_HDMIPO_010620_2024_04_18_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE","symbol":"010620","company_name":"HD현대미포","round":"R1","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ORDER_BACKLOG_MARGIN_BRIDGE_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"HDMIPO_010620_2024_04_18_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2A captured backlog/margin rerating; later peak-to-drawdown needs 4B audit rather than unbounded Green","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C01 symbol versus top-covered C01 list; evidence is source_proxy_only and needs URL repair"}
{"row_type":"case","case_id":"C01_HHI_329180_2024_04_18_SHIPBUILDING_BACKLOG_MARGIN_RERATING","symbol":"329180","company_name":"HD현대중공업","round":"R1","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"LARGE_SHIPBUILDING_BACKLOG_MARGIN_REVISION_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"HHI_329180_2024_04_18_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Large 90D/180D MFE confirms backlog/margin bridge, but post-peak drawdown requires valuation/4B watch","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C01 symbol; source_proxy_only evidence"}
{"row_type":"case","case_id":"C01_HDI_042670_2024_02_02_EQUIPMENT_ORDER_CYCLE_FALSE_POSITIVE","symbol":"042670","company_name":"HD현대인프라코어","round":"R1","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"CONSTRUCTION_EQUIPMENT_ORDER_CYCLE_MARGIN_BRIDGE_ABSENT","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"HDI_042670_2024_02_02_STAGE2_FALSE_POSITIVE_ORDER_CYCLE_MARGIN_BRIDGE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Industrial/order-cycle rally had low MFE and later drawdown; margin bridge was insufficient","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C01 symbol; counterexample for order/cycle headline without margin bridge"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"HDMIPO_010620_2024_04_18_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE","case_id":"C01_HDMIPO_010620_2024_04_18_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE","symbol":"010620","company_name":"HD현대미포","round":"R1","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ORDER_BACKLOG_MARGIN_BRIDGE_4B_WATCH","sector":"industrial orders / shipbuilding backlog","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-18","entry_date":"2024-04-18","entry_price":64900.0,"evidence_available_at_that_date":"source_proxy_only: shipbuilding backlog/margin-turn narrative, relative strength, and early margin bridge route; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["order_backlog_route","margin_turn_route","relative_strength","delivery_visibility"],"stage3_evidence_fields":["margin_bridge_partial","revision_confirmation_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv","profile_path":"atlas/symbol_profiles/010/010620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.34,"MFE_90D_pct":89.21,"MFE_180D_pct":89.21,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-8.17,"MAE_90D_pct":-8.17,"MAE_180D_pct":-8.17,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":122800.0,"drawdown_after_peak_pct":-24.51,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_audit_after_backlog_margin_rerating","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_010620_2024_04_18_64900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HHI_329180_2024_04_18_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE","case_id":"C01_HHI_329180_2024_04_18_SHIPBUILDING_BACKLOG_MARGIN_RERATING","symbol":"329180","company_name":"HD현대중공업","round":"R1","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"LARGE_SHIPBUILDING_BACKLOG_MARGIN_REVISION_BRIDGE","sector":"industrial orders / shipbuilding backlog","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-18","entry_date":"2024-04-18","entry_price":120300.0,"evidence_available_at_that_date":"source_proxy_only: large shipbuilding backlog, delivery/mix improvement, and margin bridge route; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["order_backlog_route","delivery_visibility","margin_turn_route","relative_strength"],"stage3_evidence_fields":["revision_bridge_partial","margin_bridge_partial","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv","profile_path":"atlas/symbol_profiles/329/329180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.36,"MFE_90D_pct":84.95,"MFE_180D_pct":84.95,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-6.48,"MAE_90D_pct":-6.48,"MAE_180D_pct":-6.48,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-09","peak_price":222500.0,"drawdown_after_peak_pct":-23.64,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_audit_after_large_backlog_rerating","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_329180_2024_04_18_120300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HDI_042670_2024_02_02_STAGE2_FALSE_POSITIVE_ORDER_CYCLE_MARGIN_BRIDGE","case_id":"C01_HDI_042670_2024_02_02_EQUIPMENT_ORDER_CYCLE_FALSE_POSITIVE","symbol":"042670","company_name":"HD현대인프라코어","round":"R1","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"CONSTRUCTION_EQUIPMENT_ORDER_CYCLE_MARGIN_BRIDGE_ABSENT","sector":"industrial orders / machinery cycle","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":8400.0,"evidence_available_at_that_date":"source_proxy_only: construction-equipment order/cycle rebound and relative-strength signal, but margin bridge and order durability not confirmed","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["order_cycle_rebound","relative_strength","industrial_demand_beta"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["price_only_local_peak","cycle_reversal_risk"],"stage4c_evidence_fields":["margin_bridge_absent","order_cycle_reversal"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042670/2024.csv","profile_path":"atlas/symbol_profiles/042/042670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.95,"MFE_90D_pct":5.95,"MFE_180D_pct":9.05,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-12.98,"MAE_90D_pct":-12.98,"MAE_180D_pct":-25.36,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-23","peak_price":9160.0,"drawdown_after_peak_pct":-31.55,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_peak_without_margin_bridge_not_full_4B","four_b_evidence_type":["price_only","cycle_reversal_risk"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_margin_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_042670_2024_02_02_8400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_HDMIPO_010620_2024_04_18_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE","trigger_id":"HDMIPO_010620_2024_04_18_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE","symbol":"010620","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":8,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":8,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable with mandatory 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Backlog/margin bridge worked, but rapid rerating requires C01 4B peak-proximity audit.","MFE_90D_pct":89.21,"MAE_90D_pct":-8.17,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_HHI_329180_2024_04_18_SHIPBUILDING_BACKLOG_MARGIN_RERATING","trigger_id":"HHI_329180_2024_04_18_STAGE2A_SHIPBUILDING_BACKLOG_MARGIN_BRIDGE","symbol":"329180","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":8,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":8,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable with mandatory 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Large backlog rerating captured high MFE; valuation room should decay into 4B audit after peak extension.","MFE_90D_pct":84.95,"MAE_90D_pct":-6.48,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_HDI_042670_2024_02_02_EQUIPMENT_ORDER_CYCLE_FALSE_POSITIVE","trigger_id":"HDI_042670_2024_02_02_STAGE2_FALSE_POSITIVE_ORDER_CYCLE_MARGIN_BRIDGE","symbol":"042670","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":7,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":52,"stage_label_after":"Stage1/4B-watch, not Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Order-cycle/relative-strength signal without margin bridge produced too little MFE and too much drawdown.","MFE_90D_pct":5.95,"MAE_90D_pct":-12.98,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 75
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C14_EV_DEMAND_SLOWDOWN_4B_4C
```

If this loop is accepted, C01 moves from 16 to a projected 19 rows. It remains below 30-row minimum stability, but the next run should re-read the latest No-Repeat Index before selecting another C01 case.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/042/042670/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/010/010620.json
  - atlas/symbol_profiles/329/329180.json
  - atlas/symbol_profiles/042/042670.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
