# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_115_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
selected_round: R2
selected_loop: 115
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: MEMORY_TEST_HANDLER_CUSTOMER_QUALIFICATION_REPEAT_TEST_DEMAND_4B_WATCH
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

This is the corrected valid run after the attempted C09 re-materialization path was discarded. C09 already reached the 30-row stability threshold at local loop114, so this loop returns to the thinner C08 gap.

This loop adds 3 new independent C08 rows and moves C08 from static 14 rows to local projected 23 after loops 103/104/109, then to projected 26 after this loop.

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

C08 is the semi test/socket customer-quality archetype. In this loop the socket-only framing is widened to adjacent test-handler, test-service, and OSAT test-package routes. The common mechanism is still the same: customer qualification and repeat test demand must become margin and FCF, or the premium is just a sparkler.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C08 static rows | 14 |
| C08 static symbols | 11 |
| C08 good/bad Stage2 | 4 / 4 |
| C08 4B/4C | 2 / 2 |
| C08 URL pending/proxy | 14 / 9 |
| static top covered symbols | 098120(3), 080580(2), 058470(1), 067310(1), 092870(1), 097800(1) |
| local C08 loop103 projected rows | 17 |
| local C08 loop104 projected rows | 20 |
| local C08 loop109 projected rows | 23 |
| this loop projected rows | 26 |

Selected symbols avoid static C08 top-covered symbols and local C08 loop103/104/109 symbols: `058470`, `098120`, `080580`, `232140`, `253590`, `131290`, `252990`, `425420`, `424980`.

| symbol | company | status |
|---|---|---|
| 089030 | 테크윙 | new local C08 symbol; old corporate-action caveat outside selected 2024 window |
| 330860 | 네패스아크 | new local C08 symbol |
| 061970 | LB세미콘 | new local C08 symbol; 2025 corporate-action candidate outside selected 2024 window |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated C08 memory.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 089030 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.95 |
| 330860 / 2024-03-06 | true | true | clean_180D_window | true |
| 061970 / 2024-03-06 | true | true | clean_180D_window_before_2025_02_21_candidate | true, reduced weight 0.95 |

Corporate-action notes:

- 테크윙 has old corporate-action candidates in 2011/2022 only; selected 2024 window is clean.
- 네패스아크 has zero corporate-action candidates.
- LB세미콘 has a 2025-02-21 corporate-action candidate, outside the selected 2024 forward window.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| MEMORY_TEST_HANDLER_CUSTOMER_QUALIFICATION_REPEAT_TEST_DEMAND_4B_WATCH | C08 | memory test-handler qualification/repeat-demand route can support Stage2A, but 4B audit is mandatory |
| SEMICONDUCTOR_TEST_SERVICE_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_BRIDGE | C08 | test-service premium without sustained repeat-demand/margin bridge is false-positive risk |
| OSAT_TEST_PACKAGE_PREMIUM_WITHOUT_CUSTOMER_QUALIFICATION_MARGIN_BRIDGE | C08 | OSAT/test-package premium needs customer qualification and margin bridge before Stage2/Yellow |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C08_TECHWING_089030_2024_03_06_MEMORY_TEST_HANDLER_CUSTOMER_QUALITY_RERATING_4B | 089030 | 테크윙 | 4B_overlay_success | positive | memory test-handler customer-quality route produced 200%+ MFE, then deep post-peak drawdown |
| C08_NEPESARK_330860_2024_03_06_TEST_SERVICE_CUSTOMER_QUALITY_FAIL | 330860 | 네패스아크 | failed_rerating | counterexample | test-service premium had a short spike but severe full-window MAE |
| C08_LBSEMI_061970_2024_03_06_OSAT_TEST_PACKAGE_PREMIUM_FAIL | 061970 | LB세미콘 | failed_rerating | counterexample | OSAT/test-package premium produced short MFE but deep 180D MAE |

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
| reduced_weight_caveat_count | 2 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 089030 | source_proxy_only | memory test-handler customer qualification / HBM test-cycle / repeat utilization | required before promotion |
| 330860 | source_proxy_only | test-service customer-quality narrative but repeat-demand/margin bridge absent | required; useful as counterexample |
| 061970 | source_proxy_only | OSAT/test-package customer narrative but qualification/margin bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 089030 | atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv | atlas/symbol_profiles/089/089030.json |
| 330860 | atlas/ohlcv_tradable_by_symbol_year/330/330860/2024.csv | atlas/symbol_profiles/330/330860.json |
| 061970 | atlas/ohlcv_tradable_by_symbol_year/061/061970/2024.csv | atlas/symbol_profiles/061/061970.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| TECHWING_089030_2024_03_06_STAGE2A_MEMORY_TEST_HANDLER_CUSTOMER_QUALITY | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 23500 | memory test-handler qualification / repeat test demand |
| NEPESARK_330860_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_SERVICE_PREMIUM | Stage2 | 2024-03-06 | 2024-03-06 | 35850 | test-service premium without repeat-demand/margin bridge |
| LBSEMI_061970_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_TEST_PACKAGE | Stage2 | 2024-03-06 | 2024-03-06 | 7110 | OSAT/test-package premium without qualification/margin bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 089030 | 2024-03-06 | 23500 | 61.06 | -9.36 | 201.28 | -9.36 | 201.28 | -9.36 | 2024-07-11 | 70800 | -56.36 |
| 330860 | 2024-03-06 | 35850 | 29.43 | -16.46 | 29.43 | -40.86 | 29.43 | -61.00 | 2024-03-12 | 46400 | -69.87 |
| 061970 | 2024-03-06 | 7110 | 32.35 | -1.41 | 32.35 | -12.80 | 32.35 | -45.43 | 2024-03-25 | 9410 | -58.77 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 089030 | Stage2A/Yellow possible; 4B after test-handler rerating | extreme MFE and later cycle drawdown | current_profile_4B_too_late |
| 330860 | Stage2 risk if test-service premium is over-credited | short spike and severe full-window MAE | current_profile_false_positive |
| 061970 | Stage2 risk if OSAT/test-package premium is over-credited | short MFE and deep 180D MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C08 interpretation:

- Stage2A can work when test/socket/test-handler exposure is tied to customer qualification and repeat-demand conversion.
- Yellow/Green require repeat demand, margin, revision, and FCF proof.
- Test-service or OSAT/test-package premium without conversion bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 089030 | 0.33 | 1.00 | test-handler customer-quality rerating / valuation | full-window 4B audit required |
| 330860 | 1.00 | 1.00 | test-service premium / weak follow-through | not Stage3 without repeat-demand bridge |
| 061970 | 1.00 | 1.00 | OSAT/test-package event premium / bridge absent | not Stage3 without qualification/margin bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 089030 | thesis_break_watch_only | not hard 4C, but 4B cap needed after rerating |
| 330860 | hard_4c_late | repeat-demand/margin bridge absence should have capped Stage2 earlier |
| 061970 | hard_4c_late | qualification/margin/FCF bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, test/socket/test-handler exposure can support Stage2A only when customer qualification, repeat test demand, margin bridge, revision, or FCF conversion is visible. Test-service or OSAT/test-package premiums without that bridge should not become Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
confidence = medium
```

Candidate C08 rule:

```text
C08_socket_customer_quality_bridge_required =
  test_socket_or_tester_or_test_handler_or_test_service_route
  AND (customer_qualification OR repeat_demand OR repeat_consumable_route OR margin_bridge OR confirmed_revision OR fcf_conversion)

if test_service_or_osat_package_premium and customer_quality_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 40 and drawdown_after_peak < -35:
    add C08_peak_proximity_4B_audit = true

if MFE_90D > 20 and MAE_90D < -10 and bridge_absent:
    classify_as C08_test_service_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 87.69 | -21.01 | 87.69 | -38.6 | 2 | useful but C08 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 87.69 | -21.01 | 87.69 | -38.6 | 2 | over-credits test-service/OSAT premiums |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 201.28 | -9.36 | 201.28 | -9.36 | 0 | better after customer-quality bridge gate |
| P2 canonical_archetype_candidate_profile | C08 | 1 promoted + 2 guard | 201.28 | -9.36 | 201.28 | -9.36 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C08 guard | 1 promoted + 2 guard | 201.28 | -9.36 | 201.28 | -9.36 | 0 | adds test-service/OSAT false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 089030 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 330860 | Stage2 false positive if repeat-demand bridge not enforced | current_profile_false_positive |
| 061970 | Stage2 false positive if customer-quality bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | mixed C08 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 14 -> local 23 -> projected 26; still need 4 to reach 30 |

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
new_axis_proposed: C08_socket_customer_quality_bridge_required|C08_peak_proximity_4B_audit|C08_test_service_osat_false_positive_guardrail
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
- Uses C08 Priority 0 coverage gap.
- Avoids static C08 top-covered symbols and local loop103/104/109 C08 symbols.
- Keeps 089030 and 061970 with reduced weights because corporate-action candidates exist outside the selected forward windows.
- Corrects the immediately preceding accidental C09 re-materialization attempt by making this the valid loop115 C08 artifact.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count any repeated C09 loop114 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_socket_customer_quality_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"330860/061970 show test-service or OSAT premiums can fail without customer qualification/repeat-demand bridge while 089030 works only as Stage2A with 4B audit","blocks two false positives while preserving 089030 Stage2A","TECHWING_089030_2024_03_06_STAGE2A_MEMORY_TEST_HANDLER_CUSTOMER_QUALITY|NEPESARK_330860_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_SERVICE_PREMIUM|LBSEMI_061970_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_TEST_PACKAGE",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C08_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"089030 memory test-handler customer-quality rerating needed full-window 4B audit after extreme MFE and drawdown","adds 4B audit after large C08 MFE without converting price-only peaks into Green","TECHWING_089030_2024_03_06_STAGE2A_MEMORY_TEST_HANDLER_CUSTOMER_QUALITY",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C08_test_service_osat_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"330860/061970 had short MFE but high MAE after test-service or OSAT/test-package premiums","requires qualification/repeat demand/margin/FCF bridge before Stage2/Yellow promotion","NEPESARK_330860_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_SERVICE_PREMIUM|LBSEMI_061970_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_TEST_PACKAGE",2,2,2,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C08_TECHWING_089030_2024_03_06_MEMORY_TEST_HANDLER_CUSTOMER_QUALITY_RERATING_4B","symbol":"089030","company_name":"테크윙","round":"R2","loop":"115","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"MEMORY_TEST_HANDLER_CUSTOMER_QUALIFICATION_REPEAT_TEST_DEMAND_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"TECHWING_089030_2024_03_06_STAGE2A_MEMORY_TEST_HANDLER_CUSTOMER_QUALITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before 2023; selected 2024 window is clean","independent_evidence_weight":0.95,"score_price_alignment":"memory test-handler/customer-quality rerating captured 200%+ MFE, but later full-window drawdown required C08 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol versus loops 103/104/109; C08 customer qualification and repeat-test demand bridge"}
{"row_type":"case","case_id":"C08_NEPESARK_330860_2024_03_06_TEST_SERVICE_CUSTOMER_QUALITY_FAIL","symbol":"330860","company_name":"네패스아크","round":"R2","loop":"115","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMICONDUCTOR_TEST_SERVICE_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"NEPESARK_330860_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_SERVICE_PREMIUM","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"test-service/customer-quality premium produced a short MFE but later severe MAE without sustained repeat-demand and margin bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol; zero corporate-action candidates in profile"}
{"row_type":"case","case_id":"C08_LBSEMI_061970_2024_03_06_OSAT_TEST_PACKAGE_PREMIUM_FAIL","symbol":"061970","company_name":"LB세미콘","round":"R2","loop":"115","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"OSAT_TEST_PACKAGE_PREMIUM_WITHOUT_CUSTOMER_QUALIFICATION_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"LBSEMI_061970_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_TEST_PACKAGE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"2025-02-21 corporate-action candidate is outside selected 2024 forward window","independent_evidence_weight":0.95,"score_price_alignment":"OSAT/test-package premium produced a short MFE but later deep MAE without customer qualification, repeat-demand, or margin bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol; 2025 corporate-action candidate outside historical window"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TECHWING_089030_2024_03_06_STAGE2A_MEMORY_TEST_HANDLER_CUSTOMER_QUALITY","case_id":"C08_TECHWING_089030_2024_03_06_MEMORY_TEST_HANDLER_CUSTOMER_QUALITY_RERATING_4B","symbol":"089030","company_name":"테크윙","round":"R2","loop":"115","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"MEMORY_TEST_HANDLER_CUSTOMER_QUALIFICATION_REPEAT_TEST_DEMAND_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":23500.0,"evidence_available_at_that_date":"source_proxy_only: memory test-handler customer qualification, HBM/test cycle expectation, repeat handler utilization route, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_test_handler_customer_qualification","hbm_test_cycle_expectation","repeat_handler_utilization","relative_strength"],"stage3_evidence_fields":["customer_qualification_bridge_partial","repeat_demand_bridge_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":61.06,"MFE_90D_pct":201.28,"MFE_180D_pct":201.28,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-9.36,"MAE_90D_pct":-9.36,"MAE_180D_pct":-9.36,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":70800.0,"drawdown_after_peak_pct":-56.36,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.33,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"memory_test_handler_customer_quality_rerating_worked_but_full_window_peak_requires_C08_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C08_089030_2024_03_06_23500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before 2023; selected 2024 window is clean","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"NEPESARK_330860_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_SERVICE_PREMIUM","case_id":"C08_NEPESARK_330860_2024_03_06_TEST_SERVICE_CUSTOMER_QUALITY_FAIL","symbol":"330860","company_name":"네패스아크","round":"R2","loop":"115","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMICONDUCTOR_TEST_SERVICE_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":35850.0,"evidence_available_at_that_date":"source_proxy_only: semiconductor test-service premium and customer-quality narrative visible, but sustained repeat demand, margin bridge, revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["test_service_premium","customer_quality_narrative","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","weak_follow_through","bridge_absent"],"stage4c_evidence_fields":["repeat_demand_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/330/330860/2024.csv","profile_path":"atlas/symbol_profiles/330/330860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":29.43,"MFE_90D_pct":29.43,"MFE_180D_pct":29.43,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-16.46,"MAE_90D_pct":-40.86,"MAE_180D_pct":-61.0,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-12","peak_price":46400.0,"drawdown_after_peak_pct":-69.87,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"test_service_premium_not_C08_stage3_without_repeat_demand_margin_revision_bridge","four_b_evidence_type":["event_premium","weak_follow_through"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mid_mfe_high_mae_customer_quality_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_330860_2024_03_06_35850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"LBSEMI_061970_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_TEST_PACKAGE","case_id":"C08_LBSEMI_061970_2024_03_06_OSAT_TEST_PACKAGE_PREMIUM_FAIL","symbol":"061970","company_name":"LB세미콘","round":"R2","loop":"115","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"OSAT_TEST_PACKAGE_PREMIUM_WITHOUT_CUSTOMER_QUALIFICATION_MARGIN_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":7110.0,"evidence_available_at_that_date":"source_proxy_only: OSAT/test-package customer-quality premium visible, but customer qualification, repeat-demand, margin and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["osat_test_package_premium","customer_quality_narrative","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","weak_follow_through","bridge_absent"],"stage4c_evidence_fields":["customer_qualification_absent","repeat_demand_absent","margin_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/061/061970/2024.csv","profile_path":"atlas/symbol_profiles/061/061970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":32.35,"MFE_90D_pct":32.35,"MFE_180D_pct":32.35,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-1.41,"MAE_90D_pct":-12.8,"MAE_180D_pct":-45.43,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":9410.0,"drawdown_after_peak_pct":-58.77,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"osat_test_package_premium_not_C08_stage3_without_customer_qualification_repeat_demand_margin_bridge","four_b_evidence_type":["event_premium","weak_follow_through"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_short_mfe_high_180d_mae_customer_quality_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_before_2025_02_21_candidate","same_entry_group_id":"C08_061970_2024_03_06_7110","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"2025-02-21 corporate-action candidate is outside selected 2024 forward window","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_TECHWING_089030_2024_03_06_MEMORY_TEST_HANDLER_CUSTOMER_QUALITY_RERATING_4B","trigger_id":"TECHWING_089030_2024_03_06_STAGE2A_MEMORY_TEST_HANDLER_CUSTOMER_QUALITY","symbol":"089030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":10,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":10,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable with C08 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Memory test-handler customer-quality route worked, but Yellow/Green requires repeat-demand, margin, revision, and FCF proof plus full-window 4B audit.","MFE_90D_pct":201.28,"MAE_90D_pct":-9.36,"score_return_alignment_label":"positive_extreme_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_NEPESARK_330860_2024_03_06_TEST_SERVICE_CUSTOMER_QUALITY_FAIL","trigger_id":"NEPESARK_330860_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_SERVICE_PREMIUM","symbol":"330860","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":6,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2 false-positive / C08 service-premium risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Stage1/4C-watch, not C08 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Test-service premium without repeat-demand and margin bridge had a short spike but severe full-window drawdown.","MFE_90D_pct":29.43,"MAE_90D_pct":-40.86,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_LBSEMI_061970_2024_03_06_OSAT_TEST_PACKAGE_PREMIUM_FAIL","trigger_id":"LBSEMI_061970_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_TEST_PACKAGE","symbol":"061970","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2 false-positive / OSAT test-package risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C08 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"OSAT/test-package premium without qualification/repeat-demand bridge produced a short MFE but deep 180D MAE.","MFE_90D_pct":32.35,"MAE_90D_pct":-12.8,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"115","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 115
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C02_POWER_GRID_DATACENTER_CAPEX, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C15_MATERIAL_SPREAD_SUPERCYCLE
```

If this loop is accepted together with local C08 loops 103, 104, and 109, C08 moves to projected 26 rows and still needs 4 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C08 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/330/330860/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/061/061970/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/089/089030.json
  - atlas/symbol_profiles/330/330860.json
  - atlas/symbol_profiles/061/061970.json
- Rejected local duplicate C08 symbols:
  - 058470, 098120, 080580
  - 232140, 253590, 131290
  - 252990, 425420, 424980
- Rejected static top-covered C08 symbols or contamination-risk names:
  - 067310, 092870, 097800
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
