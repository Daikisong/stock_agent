# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
selected_round: R2
selected_loop: 73
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: PROBE_CARD_CERAMIC_STF_CUSTOMER_QUALITY_REPEAT_DEMAND
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

This loop adds 3 new independent cases, 1 counterexample, and 2 residual error types for R2/L2/C08.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

This loop does not re-propose global rules. It stress-tests already-applied axes inside C08:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS
C08 -> C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
```

C08 is compressed as:

```text
test socket / probe card / reliability-test customer-quality route
  -> customer qualification or repeat consumable demand
  -> revenue conversion
  -> margin durability
```

The selected fine/deep sub-archetypes are all mapped to C08:

| fine_archetype_id | canonical mapping |
|---|---|
| PROBE_CARD_CERAMIC_STF_CUSTOMER_QUALITY_REPEAT_DEMAND | C08 |
| MEMS_PROBE_CARD_SMALL_CAP_QUALIFICATION_BRIDGE_ABSENT | C08 |
| RELIABILITY_TEST_SERVICE_CUSTOMER_QUALITY_4B_WATCH | C08 |

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot:

| item | value |
|---|---:|
| C08 current rows | 14 |
| C08 current symbols | 11 |
| C08 good/bad Stage2 | 4 / 4 |
| C08 4B/4C | 2 / 2 |
| C08 URL pending/proxy | 14 / 9 |
| top covered symbols | 098120, 080580, 058470, 067310, 092870, 097800 |

This loop intentionally avoids the previous local loop symbols `095340`, `131290`, and `425420`, and also avoids the top-covered C08 list where possible. The selected symbols are:

| symbol | company | status |
|---|---|---|
| 252990 | 샘씨엔에스 | new C08 symbol versus index top list and previous local loop |
| 424980 | 마이크로투나노 | new C08 symbol versus index top list and previous local loop |
| 405100 | 큐알티 | new C08 symbol versus index top list and previous local loop |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the No-Repeat summary.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream | FinanceData/marcap |
| manifest | atlas/manifest.json |
| schema | atlas/schema.json |
| manifest max_date | 2026-02-20 |
| calibration shard root | atlas/ohlcv_tradable_by_symbol_year |
| raw shard root | atlas/ohlcv_raw_by_symbol_year |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate action window | calibration usable |
|---|---:|---:|---|---:|
| 252990 / 2024-01-23 | true | true | clean_180D_window | true |
| 424980 / 2024-04-02 | true | true | clean_180D_window | true |
| 405100 / 2024-01-18 | true | true | clean_180D_window | true |

Corporate-action notes:

- 샘씨엔에스 profile shows zero corporate-action candidates.
- 마이크로투나노 profile shows zero corporate-action candidates.
- 큐알티 profile shows corporate-action candidates only in 2022-12 and 2023-01; selected 2024 windows do not overlap.

## 6. Canonical Archetype Compression Map

| case | fine/deep path | compressed canonical |
|---|---|---|
| 샘씨엔에스 | probe-card ceramic STF / consumable route | C08 |
| 마이크로투나노 | MEMS probe-card beta without qualification bridge | C08 counterexample |
| 큐알티 | semiconductor reliability-test service and customer-quality validation | C08 |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C08_SEMCNS_252990_2024_01_23_CERAMIC_STF_PROBE_CARD_RERATING | 252990 | 샘씨엔에스 | structural_success | positive | moderate MFE, clean window, new C08 probe-card consumable path |
| C08_M2N_424980_2024_04_02_MEMS_PROBE_CARD_FALSE_POSITIVE | 424980 | 마이크로투나노 | failed_rerating | counterexample | price spike faded into large MAE without customer/revision bridge |
| C08_QRT_405100_2024_01_18_RELIABILITY_TEST_CUSTOMER_QUALITY_4B | 405100 | 큐알티 | high_mae_success | positive | large MFE but severe post-peak drawdown; 4B timing stress |

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
| 252990 | source_proxy_only | probe-card ceramic STF / consumable route | required before promotion |
| 424980 | source_proxy_only | MEMS probe-card exposure but qualification bridge absent | required; counterexample can still inform guardrail |
| 405100 | source_proxy_only | reliability-test service customer-quality route | required before promotion |

No row uses price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 252990 | atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv | atlas/symbol_profiles/252/252990.json |
| 424980 | atlas/ohlcv_tradable_by_symbol_year/424/424980/2024.csv | atlas/symbol_profiles/424/424980.json |
| 405100 | atlas/ohlcv_tradable_by_symbol_year/405/405100/2024.csv | atlas/symbol_profiles/405/405100.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| SEMCNS_252990_2024_01_23_STAGE2A_PROBE_CARD_CERAMIC_STF | Stage2-Actionable | 2024-01-23 | 2024-01-23 | 6860 | probe-card ceramic STF / consumable route |
| M2N_424980_2024_04_02_STAGE2_FALSE_POSITIVE_MEMS_PROBE_CARD | Stage2 | 2024-04-02 | 2024-04-02 | 13780 | MEMS/probe-card exposure without qualification bridge |
| QRT_405100_2024_01_18_STAGE2A_RELIABILITY_TEST_CUSTOMER_QUALITY | Stage2-Actionable | 2024-01-18 | 2024-01-18 | 22650 | reliability-test service / customer-quality route |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 252990 | 2024-01-23 | 6860 | 28.86 | -2.33 | 35.28 | -7.00 | 35.28 | -30.76 | 2024-04-18 | 9280 | -48.81 |
| 424980 | 2024-04-02 | 13780 | 11.76 | -12.19 | 11.76 | -52.90 | 11.76 | -65.57 | 2024-04-02 | 15400 | -69.19 |
| 405100 | 2024-01-18 | 22650 | 86.09 | -19.82 | 92.05 | -19.82 | 92.05 | -47.37 | 2024-03-05 | 43500 | -72.60 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 252990 | Stage2A acceptable; Green waits for bridge | moderate MFE with controlled 90D MAE but later drawdown | current_profile_correct |
| 424980 | Stage2 risk if MEMS/probe-card exposure over-credited | local spike then severe MAE | current_profile_false_positive |
| 405100 | Stage2A/Yellow possible but needs 4B audit | huge MFE then severe post-peak drawdown | current_profile_4B_too_late |

Required axis audit:

1. `stage2_actionable_evidence_bonus` is useful for 252990 and 405100, but too loose for 424980 without customer-quality bridge.
2. `stage3_yellow_total_min = 75` should remain strict in C08 when margin/revision bridge is missing.
3. `stage3_green_total_min = 87` and `revision_min = 55` should remain strict.
4. `price_only_blowoff_blocks_positive_stage` is correct and should be reinforced by C08 bridge logic.
5. `full_4b_requires_non_price_evidence` is correct, but C08 still needs a peak-proximity 4B audit row even when non-price 4B evidence is not yet available.
6. `hard_4c_thesis_break_routes_to_4c` is useful, but bridge absence should cap Stage2 before a large MAE path develops.

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C08 conclusion:

- Stage2A can fire on customer-quality / probe-card / test-service route.
- Yellow requires stronger margin, repeat order, or revision bridge.
- Green requires confirmed customer qualification, repeat revenue conversion, margin durability, and low 4B risk.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 252990 | 1.00 | 1.00 | valuation / positioning | moderate success but bridge needed before Green |
| 424980 | 1.00 | 1.00 | price_only / valuation | price-only local 4B too early; better as false-positive guard |
| 405100 | 1.00 | 1.00 | price_only / valuation / positioning | full-window price timing was useful, but non-price 4B evidence missing |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 252990 | thesis_break_watch_only | no hard 4C, but later drawdown argues against Green |
| 424980 | hard_4c_late | bridge absence should have blocked Stage2 earlier |
| 405100 | thesis_break_watch_only | not a thesis-break case, but 4B watch was late |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = low_to_medium
```

Candidate:

> In L2 semiconductor test/probe/socket names, a test-demand route may support Stage2A, but Stage3-Yellow/Green should require a customer-quality bridge: qualification, repeat consumable demand, named customer route, margin bridge, or confirmed revision. Small-cap MEMS/probe-card beta without that bridge should be capped at Stage1/Stage2-watch and counted as false-positive risk if MFE is local and MAE expands.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
confidence = low_to_medium
```

Candidate C08 rule:

```text
C08_customer_quality_bridge_required =
  customer_qualification
  OR repeat_socket/probe_card_consumable_demand
  OR named_customer_test_route
  OR margin/revision bridge

if probe/socket/test exposure is present but customer_quality_bridge is absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 35 and drawdown_after_peak < -45:
    add C08_peak_proximity_4B_audit = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 46.36 | -26.57 | 46.36 | -47.9 | 1 | useful but bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 46.36 | -26.57 | 46.36 | -47.9 | 1 | too sensitive to price/relative strength |
| P1 sector_specific_candidate_profile | L2 | 2 promoted + 1 guard | 63.66 | -13.41 | 63.66 | -39.06 | 0 | better if 424980 is blocked |
| P2 canonical_archetype_candidate_profile | C08 | 2 promoted + 1 guard | 63.66 | -13.41 | 63.66 | -39.06 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C08 guard | 2 promoted + 1 guard | 63.66 | -13.41 | 63.66 | -39.06 | 0 | adds hard bridge gate |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 252990 | Stage2A aligned; Green still blocked | current_profile_correct |
| 424980 | Stage2 false-positive if bridge not enforced | current_profile_false_positive |
| 405100 | Stage2A aligned; 4B watch late | current_profile_4B_too_late |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | mixed C08 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 2 | true | true | 14 -> projected 17 rows; still need 13 to reach 30 |

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
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - stage2_actionable_evidence_bonus
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_false_positive
  - current_profile_4B_too_late
new_axis_proposed: C08_customer_quality_bridge_required|C08_peak_proximity_4B_audit
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
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
- Uses C08 Priority 0 coverage gap.
- Uses three new symbols relative to No-Repeat top-covered list and previous local loop.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_customer_quality_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"424980 shows MEMS/probe-card exposure without qualification/revision bridge can become false-positive","blocks 424980 while preserving 252990/405100 Stage2A","SEMCNS_252990_2024_01_23_STAGE2A_PROBE_CARD_CERAMIC_STF|M2N_424980_2024_04_02_STAGE2_FALSE_POSITIVE_MEMS_PROBE_CARD|QRT_405100_2024_01_18_STAGE2A_RELIABILITY_TEST_CUSTOMER_QUALITY",3,3,1,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C08_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"405100 and 252990 show useful Stage2A can still suffer deep post-peak drawdown","adds 4B audit after large C08 MFE without converting price-only peaks into full 4B","SEMCNS_252990_2024_01_23_STAGE2A_PROBE_CARD_CERAMIC_STF|QRT_405100_2024_01_18_STAGE2A_RELIABILITY_TEST_CUSTOMER_QUALITY",2,2,0,low_to_medium,canonical_shadow_only,"4B overlay/risk calibration only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C08_SEMCNS_252990_2024_01_23_CERAMIC_STF_PROBE_CARD_RERATING","symbol":"252990","company_name":"샘씨엔에스","round":"R2","loop":"73","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"PROBE_CARD_CERAMIC_STF_CUSTOMER_QUALITY_REPEAT_DEMAND","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"SEMCNS_252990_2024_01_23_STAGE2A_PROBE_CARD_CERAMIC_STF","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2A captured moderate 35% MFE, but later -31% MAE requires C08 margin/revision bridge before Green","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"new C08 symbol; source_proxy_only evidence, URL repair required before any promotion"}
{"row_type":"case","case_id":"C08_M2N_424980_2024_04_02_MEMS_PROBE_CARD_FALSE_POSITIVE","symbol":"424980","company_name":"마이크로투나노","round":"R2","loop":"73","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"MEMS_PROBE_CARD_SMALL_CAP_QUALIFICATION_BRIDGE_ABSENT","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"M2N_424980_2024_04_02_STAGE2_FALSE_POSITIVE_MEMS_PROBE_CARD","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Local probe-card spike failed; 180D MAE around -66% when customer/revision bridge was absent","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C08 symbol; counterexample for MEMS/probe-card beta without repeat customer conversion"}
{"row_type":"case","case_id":"C08_QRT_405100_2024_01_18_RELIABILITY_TEST_CUSTOMER_QUALITY_4B","symbol":"405100","company_name":"큐알티","round":"R2","loop":"73","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"RELIABILITY_TEST_SERVICE_CUSTOMER_QUALITY_4B_WATCH","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"QRT_405100_2024_01_18_STAGE2A_RELIABILITY_TEST_CUSTOMER_QUALITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Very high early MFE but severe post-peak drawdown; C08 needs peak-proximity 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C08 symbol; useful as positive plus 4B timing stress case"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"SEMCNS_252990_2024_01_23_STAGE2A_PROBE_CARD_CERAMIC_STF","case_id":"C08_SEMCNS_252990_2024_01_23_CERAMIC_STF_PROBE_CARD_RERATING","symbol":"252990","company_name":"샘씨엔에스","round":"R2","loop":"73","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"PROBE_CARD_CERAMIC_STF_CUSTOMER_QUALITY_REPEAT_DEMAND","sector":"AI/semiconductor/electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-23","entry_date":"2024-01-23","entry_price":6860.0,"evidence_available_at_that_date":"source_proxy_only: probe-card ceramic STF / test consumable route and C08 customer-quality narrative; URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["probe_card_route","ceramic_stf_consumable_route","customer_quality_route","relative_strength"],"stage3_evidence_fields":["repeat_demand_partial","margin_bridge_pending","revision_confirmation_pending"],"stage4b_evidence_fields":["valuation_extension","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv","profile_path":"atlas/symbol_profiles/252/252990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.86,"MFE_90D_pct":35.28,"MFE_180D_pct":35.28,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-2.33,"MAE_90D_pct":-7.0,"MAE_180D_pct":-30.76,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-18","peak_price":9280.0,"drawdown_after_peak_pct":-48.81,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"moderate_success_but_needs_margin_revision_bridge_before_green","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_moderate_mfe_with_drawdown","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_252990_2024_01_23_6860","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"M2N_424980_2024_04_02_STAGE2_FALSE_POSITIVE_MEMS_PROBE_CARD","case_id":"C08_M2N_424980_2024_04_02_MEMS_PROBE_CARD_FALSE_POSITIVE","symbol":"424980","company_name":"마이크로투나노","round":"R2","loop":"73","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"MEMS_PROBE_CARD_SMALL_CAP_QUALIFICATION_BRIDGE_ABSENT","sector":"AI/semiconductor/electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-04-02","entry_date":"2024-04-02","entry_price":13780.0,"evidence_available_at_that_date":"source_proxy_only: MEMS/probe-card small-cap route visible, but named qualification, repeat shipment, and revision bridge absent","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["mems_probe_card_exposure","relative_strength","small_cap_theme_beta"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":["thesis_evidence_broken","qualification_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/424/424980/2024.csv","profile_path":"atlas/symbol_profiles/424/424980.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.76,"MFE_90D_pct":11.76,"MFE_180D_pct":11.76,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-12.19,"MAE_90D_pct":-52.9,"MAE_180D_pct":-65.57,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-02","peak_price":15400.0,"drawdown_after_peak_pct":-69.19,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early_without_customer_bridge","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_high_mae_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_424980_2024_04_02_13780","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"QRT_405100_2024_01_18_STAGE2A_RELIABILITY_TEST_CUSTOMER_QUALITY","case_id":"C08_QRT_405100_2024_01_18_RELIABILITY_TEST_CUSTOMER_QUALITY_4B","symbol":"405100","company_name":"큐알티","round":"R2","loop":"73","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"RELIABILITY_TEST_SERVICE_CUSTOMER_QUALITY_4B_WATCH","sector":"AI/semiconductor/electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-18","entry_date":"2024-01-18","entry_price":22650.0,"evidence_available_at_that_date":"source_proxy_only: semiconductor reliability/test service customer-quality route plus HBM/test demand beta; URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["reliability_test_service_route","customer_quality_route","relative_strength","test_demand_beta"],"stage3_evidence_fields":["margin_bridge_pending","repeat_order_or_conversion_pending","revision_confirmation_pending"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/405/405100/2024.csv","profile_path":"atlas/symbol_profiles/405/405100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":86.09,"MFE_90D_pct":92.05,"MFE_180D_pct":92.05,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-19.82,"MAE_90D_pct":-19.82,"MAE_180D_pct":-47.37,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-05","peak_price":43500.0,"drawdown_after_peak_pct":-72.6,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_price_timing_but_non_price_evidence_missing","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_with_high_mae","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_405100_2024_01_18_22650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_SEMCNS_252990_2024_01_23_CERAMIC_STF_PROBE_CARD_RERATING","trigger_id":"SEMCNS_252990_2024_01_23_STAGE2A_PROBE_CARD_CERAMIC_STF","symbol":"252990","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable, Green blocked until margin/revision bridge","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Moderate MFE supports early C08 Stage2A, but Green needs margin/revision bridge and drawdown guard.","MFE_90D_pct":35.28,"MAE_90D_pct":-7.0,"score_return_alignment_label":"stage2_good_green_block_needed","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_M2N_424980_2024_04_02_MEMS_PROBE_CARD_FALSE_POSITIVE","trigger_id":"M2N_424980_2024_04_02_STAGE2_FALSE_POSITIVE_MEMS_PROBE_CARD","symbol":"424980","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":7,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":52,"stage_label_after":"Stage1/4B-watch, not Stage2","changed_components":["customer_quality_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"MEMS/probe-card exposure without named qualification or repeat shipment should not receive C08 Stage2 bridge credit.","MFE_90D_pct":11.76,"MAE_90D_pct":-52.9,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_QRT_405100_2024_01_18_RELIABILITY_TEST_CUSTOMER_QUALITY_4B","trigger_id":"QRT_405100_2024_01_18_STAGE2A_RELIABILITY_TEST_CUSTOMER_QUALITY","symbol":"405100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow risk / 4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable with 4B audit","changed_components":["valuation_repricing_score","execution_risk_score","revision_score"],"component_delta_explanation":"Huge MFE proves early signal value, but the post-peak drawdown requires immediate C08 peak-proximity 4B audit rather than Green promotion.","MFE_90D_pct":92.05,"MAE_90D_pct":-19.82,"score_return_alignment_label":"positive_but_4b_too_late","current_profile_verdict":"current_profile_4B_too_late"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"73","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage2_actionable_evidence_bonus","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_false_positive","current_profile_4B_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 73
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

If this loop is accepted, C08 moves from 14 to a projected 17 rows. Because the No-Repeat ledger has not yet incorporated this local output, the next repository-level automation should still re-read the latest index before selecting the next canonical.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/424/424980/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/405/405100/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/252/252990.json
  - atlas/symbol_profiles/424/424980.json
  - atlas/symbol_profiles/405/405100.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
