# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_103_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
selected_round: R2
selected_loop: 103
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: TEST_SOCKET_CUSTOMER_QUALIFICATION_REPEAT_DEMAND_MARGIN_4B_WATCH
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

This loop adds 3 new independent C08 rows and moves C08 from static 14 rows to projected 17 rows. It remains the thinnest Priority 0 archetype after this run.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C08:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS
C08 -> C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
```

C08 is the semi test/socket customer quality archetype. The test socket is a razor-and-blade business only when qualification, repeat consumable replacement, margin, revision, and FCF conversion are visible. A socket/HBM label alone is not the bridge.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C08 static rows | 14 |
| C08 need to 30 | 16 |
| C08 need to 50 | 36 |
| C08 investigation point | 고객 qualification, 소모품 반복수요, socket/test margin, 납품 전환 반례 |
| local previous C08 rows in this session | 0 |
| this loop projected rows | 17 |

Selected symbols:

| symbol | company | status |
|---|---|---|
| 058470 | 리노공업 | new local C08 symbol |
| 098120 | 마이크로컨텍솔 | new local C08 symbol |
| 080580 | 오킨스전자 | new local C08 symbol |

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
| 058470 / 2024-03-06 | true | true | clean_180D_window | true |
| 098120 / 2024-03-06 | true | true | clean_180D_window | true |
| 080580 / 2024-03-06 | true | true | clean_180D_window | true |

Corporate-action notes:

- 리노공업 has corporate-action candidates in 2013 and 2025 only; selected 2024 window is clean.
- 마이크로컨텍솔 has corporate-action candidates in 2011 only.
- 오킨스전자는 corporate-action candidates in 2021 only.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| TEST_SOCKET_CUSTOMER_QUALIFICATION_REPEAT_DEMAND_MARGIN_4B_WATCH | C08 | qualification/repeat-demand/margin route can support Stage2A, but valuation 4B audit is needed |
| TEST_SOCKET_THEME_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_BRIDGE | C08 | socket theme premium without repeat demand is false-positive risk |
| SOCKET_SMALLCAP_EVENT_SPIKE_WITHOUT_CUSTOMER_QUALIFICATION_BRIDGE | C08 | small-cap event spike without customer qualification bridge is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C08_LEENO_058470_2024_03_06_TEST_SOCKET_CUSTOMER_QUALITY_RERATING_4B | 058470 | 리노공업 | 4B_overlay_success | positive | customer-quality socket route produced 49% MFE, then full-window 4B drawdown |
| C08_MICROCONTACT_098120_2024_03_06_SOCKET_THEME_PREMIUM_FALSE_POSITIVE | 098120 | 마이크로컨텍솔 | failed_rerating | counterexample | socket theme had only 4% MFE and severe MAE |
| C08_OKINS_080580_2024_03_06_SOCKET_THEME_SPIKE_FALSE_POSITIVE | 080580 | 오킨스전자 | failed_rerating | counterexample | event spike had near-zero MFE and severe MAE |

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

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 058470 | source_proxy_only | customer qualification / repeat consumable / high-margin socket route | required before promotion |
| 098120 | source_proxy_only | socket/test theme premium but repeat-demand bridge absent | required; useful as counterexample |
| 080580 | source_proxy_only | small-cap socket event spike but customer qualification bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 058470 | atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv | atlas/symbol_profiles/058/058470.json |
| 098120 | atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv | atlas/symbol_profiles/098/098120.json |
| 080580 | atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv | atlas/symbol_profiles/080/080580.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| LEENO_058470_2024_03_06_STAGE2A_SOCKET_CUSTOMER_QUALITY | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 207000 | test socket customer qualification / repeat demand |
| MICROCONTACT_098120_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_THEME | Stage2 | 2024-03-06 | 2024-03-06 | 11230 | socket theme premium without repeat-demand bridge |
| OKINS_080580_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_EVENT_SPIKE | Stage2 | 2024-03-06 | 2024-03-06 | 11990 | small-cap socket event spike without qualification bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 058470 | 2024-03-06 | 207000 | 36.47 | -3.38 | 49.28 | -3.38 | 49.28 | -30.77 | 2024-05-07 | 309000 | -53.62 |
| 098120 | 2024-03-06 | 11230 | 4.19 | -21.10 | 4.19 | -30.54 | 4.19 | -55.79 | 2024-03-08 | 11700 | -57.56 |
| 080580 | 2024-03-06 | 11990 | 2.42 | -35.36 | 2.42 | -42.29 | 2.42 | -59.42 | 2024-03-08 | 12280 | -60.38 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 058470 | Stage2A/Yellow possible; 4B after customer-quality rerating | high MFE, low 90D MAE, later drawdown | current_profile_4B_too_late |
| 098120 | Stage2 risk if socket theme is over-credited | low MFE and severe MAE | current_profile_false_positive |
| 080580 | Stage2 risk if socket event spike is over-credited | near-zero MFE and severe MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C08 interpretation:

- Stage2A can work when test/socket exposure is tied to customer qualification, repeat consumable demand, high margin, and FCF.
- Yellow/Green require qualification conversion, margin bridge, revision, and repeat-demand proof.
- Socket/HBM theme premium without those bridges should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 058470 | 0.67 | 1.00 | customer-quality rerating / valuation | full-window 4B audit required |
| 098120 | 1.00 | 1.00 | theme premium / weak follow-through | not Stage3 without qualification bridge |
| 080580 | 1.00 | 1.00 | event spike / weak follow-through | not Stage3 without qualification bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 058470 | thesis_break_watch_only | not hard 4C, but 4B cap needed after rerating |
| 098120 | hard_4c_late | repeat-demand/margin bridge absence should have capped Stage2 earlier |
| 080580 | hard_4c_late | customer qualification bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, test/socket exposure can support Stage2A only when customer qualification, repeat consumable demand, margin bridge, revision, or FCF conversion is visible. Socket/HBM theme premium or small-cap event spikes without that bridge should not become Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
confidence = medium
```

Candidate C08 rule:

```text
C08_socket_customer_quality_bridge_required =
  test_socket_or_test_interface_route
  AND (customer_qualification OR repeat_consumable_demand OR margin_bridge OR confirmed_revision OR fcf_conversion)

if socket_theme_premium and customer_quality_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 25 and drawdown_after_peak < -35:
    add C08_peak_proximity_4B_audit = true

if MFE_90D < 10 and MAE_90D < -25:
    classify_as C08_socket_theme_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 18.63 | -25.4 | 18.63 | -48.66 | 2 | useful but C08 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 18.63 | -25.4 | 18.63 | -48.66 | 2 | over-credits socket theme premiums |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 49.28 | -3.38 | 49.28 | -30.77 | 0 | better after customer-quality bridge gate |
| P2 canonical_archetype_candidate_profile | C08 | 1 promoted + 2 guard | 49.28 | -3.38 | 49.28 | -30.77 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C08 guard | 1 promoted + 2 guard | 49.28 | -3.38 | 49.28 | -30.77 | 0 | adds socket-theme false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 058470 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 098120 | Stage2 false positive if customer-quality bridge not enforced | current_profile_false_positive |
| 080580 | Stage2 false positive if event spike not gated | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | mixed C08 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 14 -> projected 17; still need 13 to reach 30 |

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
new_axis_proposed: C08_socket_customer_quality_bridge_required|C08_peak_proximity_4B_audit|C08_socket_theme_false_positive_guardrail
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
- Uses C08 Priority 0 coverage gap.
- Uses three local-new C08 symbol/trigger/date combinations.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_socket_customer_quality_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"098120/080580 show socket theme premiums can fail without customer qualification/repeat-demand bridge while 058470 works only as Stage2A with 4B audit","blocks two false positives while preserving 058470 Stage2A","LEENO_058470_2024_03_06_STAGE2A_SOCKET_CUSTOMER_QUALITY|MICROCONTACT_098120_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_THEME|OKINS_080580_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_EVENT_SPIKE",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C08_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"058470 customer-quality socket rerating needed full-window 4B audit after high MFE and drawdown","adds 4B audit after large C08 MFE without converting price-only peaks into Green","LEENO_058470_2024_03_06_STAGE2A_SOCKET_CUSTOMER_QUALITY",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C08_socket_theme_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"098120/080580 had low MFE and severe MAE after socket theme/event premium","requires qualification/repeat demand/margin/FCF bridge before Stage2/Yellow promotion","MICROCONTACT_098120_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_THEME|OKINS_080580_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_EVENT_SPIKE",2,2,2,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C08_LEENO_058470_2024_03_06_TEST_SOCKET_CUSTOMER_QUALITY_RERATING_4B","symbol":"058470","company_name":"리노공업","round":"R2","loop":"103","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALIFICATION_REPEAT_DEMAND_MARGIN_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"LEENO_058470_2024_03_06_STAGE2A_SOCKET_CUSTOMER_QUALITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"test socket/customer qualification and repeat-demand margin route captured 49% MFE, but later peak-to-drawdown required C08 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C08_MICROCONTACT_098120_2024_03_06_SOCKET_THEME_PREMIUM_FALSE_POSITIVE","symbol":"098120","company_name":"마이크로컨텍솔","round":"R2","loop":"103","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_THEME_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"MICROCONTACT_098120_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_THEME","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"socket/test theme premium produced only ~4% MFE and then large MAE without qualification, repeat demand, or margin bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"counterexample for C08 theme beta without customer-quality conversion"}
{"row_type":"case","case_id":"C08_OKINS_080580_2024_03_06_SOCKET_THEME_SPIKE_FALSE_POSITIVE","symbol":"080580","company_name":"오킨스전자","round":"R2","loop":"103","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SOCKET_SMALLCAP_EVENT_SPIKE_WITHOUT_CUSTOMER_QUALIFICATION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"OKINS_080580_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_EVENT_SPIKE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"small-cap socket event spike had almost no MFE and then severe MAE because customer qualification and repeat-consumable bridge did not appear","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"counterexample for event-driven socket premium without repeat-demand evidence"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"LEENO_058470_2024_03_06_STAGE2A_SOCKET_CUSTOMER_QUALITY","case_id":"C08_LEENO_058470_2024_03_06_TEST_SOCKET_CUSTOMER_QUALITY_RERATING_4B","symbol":"058470","company_name":"리노공업","round":"R2","loop":"103","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALIFICATION_REPEAT_DEMAND_MARGIN_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":207000.0,"evidence_available_at_that_date":"source_proxy_only: test socket customer qualification, repeat consumable demand, high-margin socket route, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["customer_qualification_route","test_socket_repeat_demand","high_margin_consumable_route","relative_strength"],"stage3_evidence_fields":["qualification_bridge_partial","repeat_demand_bridge_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv","profile_path":"atlas/symbol_profiles/058/058470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.47,"MFE_90D_pct":49.28,"MFE_180D_pct":49.28,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-3.38,"MAE_90D_pct":-3.38,"MAE_180D_pct":-30.77,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-07","peak_price":309000.0,"drawdown_after_peak_pct":-53.62,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.67,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"customer_quality_socket_rerating_worked_but_full_window_peak_requires_C08_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_058470_2024_03_06_207000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"MICROCONTACT_098120_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_THEME","case_id":"C08_MICROCONTACT_098120_2024_03_06_SOCKET_THEME_PREMIUM_FALSE_POSITIVE","symbol":"098120","company_name":"마이크로컨텍솔","round":"R2","loop":"103","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_THEME_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":11230.0,"evidence_available_at_that_date":"source_proxy_only: socket/test theme premium and short relative-strength spike visible, but customer qualification, repeat consumable demand, margin and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["socket_theme_premium","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","theme_beta","bridge_absent"],"stage4c_evidence_fields":["customer_qualification_absent","repeat_demand_absent","margin_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv","profile_path":"atlas/symbol_profiles/098/098120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.19,"MFE_90D_pct":4.19,"MFE_180D_pct":4.19,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-21.1,"MAE_90D_pct":-30.54,"MAE_180D_pct":-55.79,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-08","peak_price":11700.0,"drawdown_after_peak_pct":-57.56,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"socket_theme_premium_not_stage3_without_qualification_repeat_demand_margin_bridge","four_b_evidence_type":["theme_beta","weak_follow_through"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_customer_quality_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_098120_2024_03_06_11230","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"OKINS_080580_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_EVENT_SPIKE","case_id":"C08_OKINS_080580_2024_03_06_SOCKET_THEME_SPIKE_FALSE_POSITIVE","symbol":"080580","company_name":"오킨스전자","round":"R2","loop":"103","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SOCKET_SMALLCAP_EVENT_SPIKE_WITHOUT_CUSTOMER_QUALIFICATION_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":11990.0,"evidence_available_at_that_date":"source_proxy_only: socket small-cap event premium and HBM/test theme visible, but customer qualification, repeat consumable demand, margin and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["socket_event_premium","hbm_test_theme","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_spike","weak_follow_through","bridge_absent"],"stage4c_evidence_fields":["customer_qualification_absent","repeat_consumable_absent","margin_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv","profile_path":"atlas/symbol_profiles/080/080580.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.42,"MFE_90D_pct":2.42,"MFE_180D_pct":2.42,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-35.36,"MAE_90D_pct":-42.29,"MAE_180D_pct":-59.42,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-08","peak_price":12280.0,"drawdown_after_peak_pct":-60.38,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"smallcap_socket_event_spike_not_stage3_without_customer_qualification_repeat_demand_bridge","four_b_evidence_type":["event_spike","weak_follow_through"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_customer_quality_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_080580_2024_03_06_11990","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_LEENO_058470_2024_03_06_TEST_SOCKET_CUSTOMER_QUALITY_RERATING_4B","trigger_id":"LEENO_058470_2024_03_06_STAGE2A_SOCKET_CUSTOMER_QUALITY","symbol":"058470","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":71,"stage_label_after":"Stage2-Actionable with C08 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Customer-quality socket route worked, but Yellow/Green requires repeated qualification, margin, revision, and FCF conversion plus valuation 4B audit.","MFE_90D_pct":49.28,"MAE_90D_pct":-3.38,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_MICROCONTACT_098120_2024_03_06_SOCKET_THEME_PREMIUM_FALSE_POSITIVE","trigger_id":"MICROCONTACT_098120_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_THEME","symbol":"098120","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C08 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Socket theme premium without customer qualification and repeat-demand bridge produced low MFE and high MAE.","MFE_90D_pct":4.19,"MAE_90D_pct":-30.54,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_OKINS_080580_2024_03_06_SOCKET_THEME_SPIKE_FALSE_POSITIVE","trigger_id":"OKINS_080580_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_EVENT_SPIKE","symbol":"080580","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":6,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C08 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Small-cap socket event premium without qualification/repeat-consumable bridge produced near-zero MFE and severe MAE.","MFE_90D_pct":2.42,"MAE_90D_pct":-42.29,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"103","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 103
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C15_MATERIAL_SPREAD_SUPERCYCLE
```

If this loop is accepted, C08 moves to projected 17 rows and still needs 13 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C08 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/058/058470.json
  - atlas/symbol_profiles/098/098120.json
  - atlas/symbol_profiles/080/080580.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
