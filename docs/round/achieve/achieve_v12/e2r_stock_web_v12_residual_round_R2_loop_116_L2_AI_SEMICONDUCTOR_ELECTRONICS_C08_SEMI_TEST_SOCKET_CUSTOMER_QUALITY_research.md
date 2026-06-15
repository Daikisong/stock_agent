# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_116_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
selected_round: R2
selected_loop: 116
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: TEST_SOCKET_CUSTOMER_QUALIFICATION_HIGH_MARGIN_REPEAT_DEMAND_4B_WATCH
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

This is the corrected valid run after a duplicate loop115 materialization attempt. Loop115 already existed; this loop is loop116 and uses new C08 symbol/trigger/date combinations only.

This loop adds 3 new independent C08 rows and moves C08 from static 14 rows to local projected 26 after loops 103/104/109/115, then to projected 29 after this loop. It still needs 1 row to reach the 30-row stability threshold.

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

C08 is the semi test/socket customer-quality archetype. The repeat-demand bridge is the core. A socket, package, or OSAT label can start the spark; customer qualification, replacement demand, margin, revision, and FCF decide whether the signal is durable.

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
| local C08 loop115 projected rows | 26 |
| this loop projected rows | 29 |

Selected symbols avoid static C08 top-covered symbols and local C08 loop103/104/109/115 symbols: `058470`, `098120`, `080580`, `232140`, `253590`, `131290`, `252990`, `425420`, `424980`, `089030`, `330860`, `061970`.

| symbol | company | status |
|---|---|---|
| 095340 | ISC | new local C08 symbol; prime socket route, reduced weight due to old pre-window corporate-action caveat |
| 036540 | SFA반도체 | new local C08 symbol; C10 crossover, reduced weight |
| 033170 | 시그네틱스 | new local C08 symbol |

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
| 095340 / 2024-03-06 | true | true | clean_180D_window_after_2023_10_20_candidate | true, reduced weight 0.95 |
| 036540 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.85 |
| 033170 / 2024-03-06 | true | true | clean_180D_window | true |

Corporate-action notes:

- ISC has corporate-action candidates before the selected 2024 window.
- SFA반도체 has old corporate-action candidates before 2016 only.
- 시그네틱스 has zero corporate-action candidates.
- 타이거일렉(219130) was considered but not selected because this loop already had enough C08 rows after selecting one cleaner prime socket positive and two clearer package/OSAT counterexamples.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| TEST_SOCKET_CUSTOMER_QUALIFICATION_HIGH_MARGIN_REPEAT_DEMAND_4B_WATCH | C08 | socket qualification/repeat-demand route can support Stage2A, but 4B audit is mandatory |
| OSAT_PACKAGE_TEST_PREMIUM_WITHOUT_CUSTOMER_QUALIFICATION_MARGIN_BRIDGE | C08 | OSAT/package premium without qualification and margin bridge is false-positive risk |
| OSAT_PACKAGE_EVENT_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_BRIDGE | C08 | event-like OSAT premium needs repeat-demand bridge before Stage2/Yellow |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C08_ISC_095340_2024_03_06_TEST_SOCKET_CUSTOMER_QUALITY_RERATING_4B | 095340 | ISC | 4B_overlay_success | positive | test socket/customer-quality route produced 36.7% MFE, then full-window 4B drawdown |
| C08_SFASEMICON_036540_2024_03_06_OSAT_PACKAGE_PREMIUM_FAIL | 036540 | SFA반도체 | failed_rerating | counterexample | OSAT/package-test premium produced only 5.9% MFE and high MAE |
| C08_SIGNETICS_033170_2024_03_06_OSAT_PACKAGE_EVENT_PREMIUM_FAIL | 033170 | 시그네틱스 | failed_rerating | counterexample | OSAT/package event premium had short MFE and severe later drawdown |

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
| 095340 | source_proxy_only | test socket customer qualification / repeat consumable / high-margin route | required before promotion |
| 036540 | source_proxy_only | OSAT/package-test premium but qualification/repeat-demand bridge absent | required; useful as counterexample |
| 033170 | source_proxy_only | OSAT/package event premium but repeat-demand/margin bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 095340 | atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv | atlas/symbol_profiles/095/095340.json |
| 036540 | atlas/ohlcv_tradable_by_symbol_year/036/036540/2024.csv | atlas/symbol_profiles/036/036540.json |
| 033170 | atlas/ohlcv_tradable_by_symbol_year/033/033170/2024.csv | atlas/symbol_profiles/033/033170.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| ISC_095340_2024_03_06_STAGE2A_TEST_SOCKET_CUSTOMER_QUALITY | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 79000 | test socket customer qualification / repeat demand |
| SFASEMICON_036540_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_PACKAGE_TEST | Stage2 | 2024-03-06 | 2024-03-06 | 6070 | OSAT/package-test premium without qualification bridge |
| SIGNETICS_033170_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_PACKAGE_EVENT | Stage2 | 2024-03-06 | 2024-03-06 | 1931 | OSAT/package event premium without repeat-demand bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 095340 | 2024-03-06 | 79000 | 36.71 | -5.82 | 36.71 | -29.11 | 36.71 | -47.97 | 2024-03-28 | 108000 | -61.94 |
| 036540 | 2024-03-06 | 6070 | 5.93 | -6.10 | 5.93 | -17.46 | 5.93 | -45.55 | 2024-04-02 | 6430 | -48.60 |
| 033170 | 2024-03-06 | 1931 | 20.92 | -10.98 | 20.92 | -35.01 | 20.92 | -58.47 | 2024-03-13 | 2335 | -65.65 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 095340 | Stage2A/Yellow possible; 4B after socket rerating | useful MFE but major full-window drawdown | current_profile_4B_too_late |
| 036540 | Stage2 risk if package-test premium is over-credited | low MFE and high MAE | current_profile_false_positive |
| 033170 | Stage2 risk if OSAT event premium is over-credited | short MFE and severe drawdown | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C08 interpretation:

- Stage2A can work when test/socket exposure is tied to customer qualification and repeat-demand conversion.
- Yellow/Green require repeat demand, margin, revision, and FCF proof.
- OSAT/package premium without those bridges should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 095340 | 0.73 | 1.00 | socket customer-quality rerating / valuation | full-window 4B audit required |
| 036540 | 1.00 | 1.00 | package-test premium / bridge absent | not Stage3 without qualification bridge |
| 033170 | 1.00 | 1.00 | OSAT event premium / bridge absent | not Stage3 without repeat-demand bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 095340 | thesis_break_watch_only | not hard 4C, but 4B cap needed after rerating |
| 036540 | hard_4c_late | qualification/repeat-demand/margin bridge absence should have capped Stage2 earlier |
| 033170 | hard_4c_late | repeat-demand/margin bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, test/socket/OSAT-package exposure can support Stage2A only when customer qualification, repeat test demand, margin bridge, revision, or FCF conversion is visible. OSAT/package premiums without that bridge should not become Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
confidence = medium
```

Candidate C08 rule:

```text
C08_socket_customer_quality_bridge_required =
  test_socket_or_tester_or_test_handler_or_osat_package_route
  AND (customer_qualification OR repeat_demand OR repeat_consumable_route OR margin_bridge OR confirmed_revision OR fcf_conversion)

if osat_package_premium and customer_quality_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 30 and drawdown_after_peak < -35:
    add C08_peak_proximity_4B_audit = true

if MFE_90D < 25 and MAE_90D < -15 and bridge_absent:
    classify_as C08_osat_package_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 21.19 | -27.19 | 21.19 | -50.66 | 2 | useful but C08 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 21.19 | -27.19 | 21.19 | -50.66 | 2 | over-credits OSAT/package premiums |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 36.71 | -29.11 | 36.71 | -47.97 | 0 | better after customer-quality bridge gate |
| P2 canonical_archetype_candidate_profile | C08 | 1 promoted + 2 guard | 36.71 | -29.11 | 36.71 | -47.97 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C08 guard | 1 promoted + 2 guard | 36.71 | -29.11 | 36.71 | -47.97 | 0 | adds OSAT/package false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 095340 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 036540 | Stage2 false positive if qualification/repeat-demand bridge not enforced | current_profile_false_positive |
| 033170 | Stage2 false positive if repeat-demand/margin bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | mixed C08 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 14 -> local 26 -> projected 29; still need 1 to reach 30 |

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
new_axis_proposed: C08_socket_customer_quality_bridge_required|C08_peak_proximity_4B_audit|C08_osat_package_false_positive_guardrail
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
- Avoids static C08 top-covered symbols and local loop103/104/109/115 C08 symbols.
- Keeps 095340 and 036540 with reduced weights because corporate-action candidates exist outside selected forward windows or because of cross-canonical C10 overlap.
- Corrects the accidental duplicate loop115 materialization attempt by making this the valid loop116 C08 artifact.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count any repeated loop115 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_socket_customer_quality_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"036540/033170 show OSAT package premiums can fail without qualification/repeat-demand bridge while 095340 works only as Stage2A with 4B audit","blocks two false positives while preserving 095340 Stage2A","ISC_095340_2024_03_06_STAGE2A_TEST_SOCKET_CUSTOMER_QUALITY|SFASEMICON_036540_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_PACKAGE_TEST|SIGNETICS_033170_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_PACKAGE_EVENT",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C08_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"095340 socket customer-quality rerating needed full-window 4B audit after MFE and drawdown","adds 4B audit after C08 MFE without converting price-only peaks into Green","ISC_095340_2024_03_06_STAGE2A_TEST_SOCKET_CUSTOMER_QUALITY",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C08_osat_package_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"036540/033170 had low-to-mid MFE and severe MAE after OSAT/package premiums","requires qualification/repeat demand/margin/FCF bridge before Stage2/Yellow promotion","SFASEMICON_036540_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_PACKAGE_TEST|SIGNETICS_033170_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_PACKAGE_EVENT",2,2,2,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C08_ISC_095340_2024_03_06_TEST_SOCKET_CUSTOMER_QUALITY_RERATING_4B","symbol":"095340","company_name":"ISC","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALIFICATION_HIGH_MARGIN_REPEAT_DEMAND_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"ISC_095340_2024_03_06_STAGE2A_TEST_SOCKET_CUSTOMER_QUALITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"corporate-action candidates before selected 2024 window; 2024 window treated as clean but independent weight reduced","independent_evidence_weight":0.95,"score_price_alignment":"test-socket/customer qualification and repeat-demand route captured 36.7% MFE, but post-peak drawdown required C08 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol versus loops 103/104/109/115; prime socket route"}
{"row_type":"case","case_id":"C08_SFASEMICON_036540_2024_03_06_OSAT_PACKAGE_PREMIUM_FAIL","symbol":"036540","company_name":"SFA반도체","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"OSAT_PACKAGE_TEST_PREMIUM_WITHOUT_CUSTOMER_QUALIFICATION_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"SFASEMICON_036540_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_PACKAGE_TEST","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"C10 static top-covered symbol but C08 evidence family differs; old corporate-action candidates before 2016 only","independent_evidence_weight":0.85,"score_price_alignment":"OSAT/package-test premium produced only 5.9% MFE and then deep MAE without customer qualification, repeat-demand, or margin bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"cross-canonical C10 boundary case; reduced independent weight"}
{"row_type":"case","case_id":"C08_SIGNETICS_033170_2024_03_06_OSAT_PACKAGE_EVENT_PREMIUM_FAIL","symbol":"033170","company_name":"시그네틱스","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"OSAT_PACKAGE_EVENT_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"SIGNETICS_033170_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_PACKAGE_EVENT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"OSAT/package event premium produced a short 20.9% MFE but then severe MAE without repeat-demand or margin bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol; zero corporate-action candidates in profile"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"ISC_095340_2024_03_06_STAGE2A_TEST_SOCKET_CUSTOMER_QUALITY","case_id":"C08_ISC_095340_2024_03_06_TEST_SOCKET_CUSTOMER_QUALITY_RERATING_4B","symbol":"095340","company_name":"ISC","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALIFICATION_HIGH_MARGIN_REPEAT_DEMAND_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":79000.0,"evidence_available_at_that_date":"source_proxy_only: test-socket customer qualification, repeat consumable demand, high-margin socket route, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["test_socket_customer_qualification","repeat_consumable_demand","high_margin_socket_route","relative_strength"],"stage3_evidence_fields":["customer_qualification_bridge_partial","repeat_demand_bridge_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.71,"MFE_90D_pct":36.71,"MFE_180D_pct":36.71,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-5.82,"MAE_90D_pct":-29.11,"MAE_180D_pct":-47.97,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-28","peak_price":108000.0,"drawdown_after_peak_pct":-61.94,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.73,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"test_socket_customer_quality_rerating_worked_but_full_window_drawdown_requires_C08_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_after_2023_10_20_candidate","same_entry_group_id":"C08_095340_2024_03_06_79000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"corporate-action candidates before selected 2024 window; C08 prime socket route","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"SFASEMICON_036540_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_PACKAGE_TEST","case_id":"C08_SFASEMICON_036540_2024_03_06_OSAT_PACKAGE_PREMIUM_FAIL","symbol":"036540","company_name":"SFA반도체","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"OSAT_PACKAGE_TEST_PREMIUM_WITHOUT_CUSTOMER_QUALIFICATION_MARGIN_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":6070.0,"evidence_available_at_that_date":"source_proxy_only: OSAT/package-test premium and memory recovery narrative visible, but customer qualification, repeat-demand, margin and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["osat_package_test_premium","memory_recovery_narrative","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","bridge_absent"],"stage4c_evidence_fields":["customer_qualification_absent","repeat_demand_absent","margin_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036540/2024.csv","profile_path":"atlas/symbol_profiles/036/036540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.93,"MFE_90D_pct":5.93,"MFE_180D_pct":5.93,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-6.1,"MAE_90D_pct":-17.46,"MAE_180D_pct":-45.55,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-02","peak_price":6430.0,"drawdown_after_peak_pct":-48.6,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"osat_package_premium_not_C08_stage3_without_customer_qualification_repeat_demand_bridge","four_b_evidence_type":["weak_follow_through","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_customer_quality_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["cross_canonical_C10_boundary_reduced_weight"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C08_036540_2024_03_06_6070","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"C10 static top-covered symbol but C08 evidence family differs","independent_evidence_weight":0.85,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"SIGNETICS_033170_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_PACKAGE_EVENT","case_id":"C08_SIGNETICS_033170_2024_03_06_OSAT_PACKAGE_EVENT_PREMIUM_FAIL","symbol":"033170","company_name":"시그네틱스","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"OSAT_PACKAGE_EVENT_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":1931.0,"evidence_available_at_that_date":"source_proxy_only: OSAT/package event premium and semiconductor recovery narrative visible, but repeat-demand, margin and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["osat_package_event_premium","semiconductor_recovery_narrative","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_spike","bridge_absent","weak_follow_through"],"stage4c_evidence_fields":["repeat_demand_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/033/033170/2024.csv","profile_path":"atlas/symbol_profiles/033/033170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.92,"MFE_90D_pct":20.92,"MFE_180D_pct":20.92,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-10.98,"MAE_90D_pct":-35.01,"MAE_180D_pct":-58.47,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":2335.0,"drawdown_after_peak_pct":-65.65,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"osat_package_event_premium_not_C08_stage3_without_repeat_demand_margin_bridge","four_b_evidence_type":["event_spike","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mid_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_033170_2024_03_06_1931","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_ISC_095340_2024_03_06_TEST_SOCKET_CUSTOMER_QUALITY_RERATING_4B","trigger_id":"ISC_095340_2024_03_06_STAGE2A_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":71,"stage_label_after":"Stage2-Actionable with C08 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Test-socket customer-quality route worked, but Green needs repeat-demand/margin/revision/FCF proof plus drawdown audit.","MFE_90D_pct":36.71,"MAE_90D_pct":-29.11,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_SFASEMICON_036540_2024_03_06_OSAT_PACKAGE_PREMIUM_FAIL","trigger_id":"SFASEMICON_036540_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_PACKAGE_TEST","symbol":"036540","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":59,"stage_label_before":"Stage2 false-positive / OSAT package risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":45,"stage_label_after":"Stage1/4C-watch, not C08 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"OSAT/package premium without qualification or repeat-demand bridge produced almost no upside and high 180D MAE.","MFE_90D_pct":5.93,"MAE_90D_pct":-17.46,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_SIGNETICS_033170_2024_03_06_OSAT_PACKAGE_EVENT_PREMIUM_FAIL","trigger_id":"SIGNETICS_033170_2024_03_06_STAGE2_FALSE_POSITIVE_OSAT_PACKAGE_EVENT","symbol":"033170","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2 false-positive / OSAT event risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C08 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"OSAT/package event premium without repeat-demand bridge produced short MFE and severe MAE.","MFE_90D_pct":20.92,"MAE_90D_pct":-35.01,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 116
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C02_POWER_GRID_DATACENTER_CAPEX, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C15_MATERIAL_SPREAD_SUPERCYCLE
```

If this loop is accepted together with local C08 loops 103, 104, 109, and 115, C08 moves to projected 29 rows and still needs 1 more row to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C08 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/036/036540/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/033/033170/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/095/095340.json
  - atlas/symbol_profiles/036/036540.json
  - atlas/symbol_profiles/033/033170.json
- Considered but not selected:
  - atlas/symbol_profiles/219/219130.json
- Rejected local duplicate C08 symbols:
  - 058470, 098120, 080580
  - 232140, 253590, 131290
  - 252990, 425420, 424980
  - 089030, 330860, 061970
- Rejected static top-covered C08 symbols or contamination-risk names:
  - 067310, 092870, 097800
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
