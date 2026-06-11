# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_117_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
selected_round: R2
selected_loop: 117
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: TEST_SERVICE_REPEAT_DEMAND_EVENT_RERATING_4B_WATCH
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

This is the corrected valid run after an accidental loop116 re-materialization attempt. Loop116 already existed; this loop is loop117 and uses new C08 symbol/trigger/date combinations only.

This loop adds 3 new independent C08 rows and moves C08 from static 14 rows to local projected 29 after loops 103/104/109/115/116, then to projected 32 after this loop. The 30-row stability threshold is reached.

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

C08 is the semi test/socket customer-quality archetype. In this loop the bridge is explicitly widened from socket-only to test-service, test PCB, and semiconductor test-service routes. The common mechanism remains customer qualification, repeat test demand, margin, revision, and FCF. Without that bridge, a test label is only a flare.

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
| local C08 loop116 projected rows | 29 |
| this loop projected rows | 32 |

Selected symbols avoid static C08 top-covered symbols and local C08 loop103/104/109/115/116 symbols: `058470`, `098120`, `080580`, `232140`, `253590`, `131290`, `252990`, `425420`, `424980`, `089030`, `330860`, `061970`, `095340`, `036540`, `033170`.

| symbol | company | status |
|---|---|---|
| 200470 | 에이팩트 | new local C08 symbol; 2024 row stream clean, old corporate-action caveat only |
| 219130 | 타이거일렉 | new local C08 symbol; zero corporate-action candidates |
| 131970 | 두산테스나 | new local C08 symbol; old corporate-action caveat and market-label switch only |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated C08 memory. The accidental re-materialized loop116 file is explicitly not counted as new evidence.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 200470 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.95 |
| 219130 / 2024-03-06 | true | true | clean_180D_window | true |
| 131970 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.95 |

Corporate-action notes:

- 에이팩트 has old corporate-action candidates in 2022 only; selected 2024 window is clean.
- 타이거일렉 has zero corporate-action candidates.
- 두산테스나 has old corporate-action candidates in 2020 only. The 2024 KOSDAQ GLOBAL market-label switch is not treated as a corporate-action break.
- 큐알티(405100) was considered but rejected because the 2024 row stream shows share-count drift inside the candidate forward window.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| TEST_SERVICE_REPEAT_DEMAND_EVENT_RERATING_4B_WATCH | C08 | test-service event can rerate, but repeat-demand/margin/FCF bridge and 4B audit are required |
| TEST_PCB_SOCKET_EVENT_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_BRIDGE | C08 | test PCB/socket premium without repeat-demand bridge is false-positive risk |
| SEMICONDUCTOR_TEST_SERVICE_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_REVISION_BRIDGE | C08 | test-service premium needs repeat-demand, margin, revision and FCF before Stage2/Yellow |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C08_AFACT_200470_2024_03_06_TEST_SERVICE_EVENT_RERATING_4B | 200470 | 에이팩트 | 4B_overlay_success | positive | test-service event rerating produced 45.61% MFE then full-window drawdown |
| C08_TIGERELEC_219130_2024_03_06_TEST_PCB_SOCKET_EVENT_PREMIUM_FAIL | 219130 | 타이거일렉 | failed_rerating | counterexample | test PCB/socket premium had tradable MFE but high MAE and severe drawdown |
| C08_DOOSANTESNA_131970_2024_03_06_TEST_SERVICE_PREMIUM_FAIL | 131970 | 두산테스나 | failed_rerating | counterexample | test-service premium had limited MFE and persistent MAE |

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
| 200470 | source_proxy_only | test-service event rerating / memory test-cycle / repeat service demand route | required before promotion |
| 219130 | source_proxy_only | test PCB/socket premium but repeat-demand/margin bridge absent | required; useful as counterexample |
| 131970 | source_proxy_only | test-service premium but repeat-demand/margin/revision bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 200470 | atlas/ohlcv_tradable_by_symbol_year/200/200470/2024.csv | atlas/symbol_profiles/200/200470.json |
| 219130 | atlas/ohlcv_tradable_by_symbol_year/219/219130/2024.csv | atlas/symbol_profiles/219/219130.json |
| 131970 | atlas/ohlcv_tradable_by_symbol_year/131/131970/2024.csv | atlas/symbol_profiles/131/131970.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| AFACT_200470_2024_03_06_STAGE2A_TEST_SERVICE_RERATING | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 4725 | test-service event rerating / repeat test service |
| TIGERELEC_219130_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_PCB_SOCKET | Stage2 | 2024-03-06 | 2024-03-06 | 34000 | test PCB/socket premium without repeat-demand bridge |
| DOOSANTESNA_131970_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_SERVICE | Stage2 | 2024-03-06 | 2024-03-06 | 44350 | test-service premium without repeat-demand/margin/revision bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 200470 | 2024-03-06 | 4725 | 45.61 | -1.38 | 45.61 | -1.38 | 45.61 | -41.27 | 2024-03-29 | 6880 | -59.74 |
| 219130 | 2024-03-06 | 34000 | 26.18 | -22.06 | 33.24 | -21.62 | 33.24 | -56.00 | 2024-05-14 | 45300 | -66.98 |
| 131970 | 2024-03-06 | 44350 | 20.18 | -5.52 | 20.18 | -19.17 | 20.18 | -37.66 | 2024-04-05 | 53300 | -48.12 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 200470 | Stage2A possible; 4B after test-service rerating | high MFE but later drawdown | current_profile_4B_too_late |
| 219130 | Stage2 risk if test PCB/socket premium is over-credited | MFE with high MAE and bridge-absent drawdown | current_profile_false_positive |
| 131970 | Stage2 risk if test-service premium is over-credited | limited MFE and persistent MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C08 interpretation:

- Stage2A can work when test/socket/test-service exposure is tied to customer qualification and repeat-demand conversion.
- Yellow/Green require repeat demand, margin, revision, and FCF proof.
- Test PCB or test-service premium without those bridges should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 200470 | 0.69 | 1.00 | test-service event rerating / valuation | full-window 4B audit required |
| 219130 | 0.75 | 1.00 | test PCB/socket event premium / bridge absent | not Stage3 without repeat-demand bridge |
| 131970 | 0.83 | 1.00 | test-service premium / bridge absent | not Stage3 without margin/revision bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 200470 | thesis_break_watch_only | not hard 4C, but 4B cap needed after rerating |
| 219130 | hard_4c_late | repeat-demand/margin bridge absence should have capped Stage2 earlier |
| 131970 | hard_4c_late | repeat-demand/margin/revision bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, test/socket/test-service exposure can support Stage2A only when customer qualification, repeat test demand, margin bridge, revision, or FCF conversion is visible. Test PCB or test-service premiums without that bridge should not become Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
confidence = medium
```

Candidate C08 rule:

```text
C08_socket_customer_quality_bridge_required =
  test_socket_or_test_pcb_or_test_service_route
  AND (customer_qualification OR repeat_demand OR repeat_consumable_route OR margin_bridge OR confirmed_revision OR fcf_conversion)

if test_pcb_or_test_service_premium and customer_quality_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 35 and drawdown_after_peak < -35:
    add C08_peak_proximity_4B_audit = true

if MFE_90D > 15 and MAE_90D < -15 and bridge_absent:
    classify_as C08_test_service_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 33.01 | -14.06 | 33.01 | -44.98 | 2 | useful but C08 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 33.01 | -14.06 | 33.01 | -44.98 | 2 | over-credits test PCB/service premiums |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 45.61 | -1.38 | 45.61 | -41.27 | 0 | better after customer-quality bridge gate |
| P2 canonical_archetype_candidate_profile | C08 | 1 promoted + 2 guard | 45.61 | -1.38 | 45.61 | -41.27 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C08 guard | 1 promoted + 2 guard | 45.61 | -1.38 | 45.61 | -41.27 | 0 | adds test-service/PCB false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 200470 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 219130 | Stage2 false positive if repeat-demand/margin bridge not enforced | current_profile_false_positive |
| 131970 | Stage2 false positive if repeat-demand/margin/revision bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | mixed C08 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 14 -> local 29 -> projected 32; reaches minimum stability threshold |

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
new_axis_proposed: C08_socket_customer_quality_bridge_required|C08_peak_proximity_4B_audit|C08_test_service_pcb_false_positive_guardrail
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
- Avoids static C08 top-covered symbols and local loop103/104/109/115/116 C08 symbols.
- Keeps 200470 and 131970 with reduced weights because corporate-action candidates are outside selected forward windows or because the 2024 market-label switch is not price-adjustment contamination.
- Rejects 405100 due to 2024 share-count drift inside the candidate forward window.
- Corrects the accidental duplicate loop116 materialization attempt by making this the valid loop117 C08 artifact.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count any repeated loop116 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_socket_customer_quality_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"219130/131970 show test PCB or test-service premiums can fail without repeat-demand/margin bridge while 200470 works only as Stage2A with 4B audit","blocks two false positives while preserving 200470 Stage2A","AFACT_200470_2024_03_06_STAGE2A_TEST_SERVICE_RERATING|TIGERELEC_219130_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_PCB_SOCKET|DOOSANTESNA_131970_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_SERVICE",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C08_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"200470 test-service event rerating needed full-window 4B audit after high MFE and drawdown","adds 4B audit after C08 MFE without converting price-only peaks into Green","AFACT_200470_2024_03_06_STAGE2A_TEST_SERVICE_RERATING",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C08_test_service_pcb_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"219130/131970 had limited-to-mid MFE with high MAE or bridge-absent drawdown after test-service/test-PCB premiums","requires qualification/repeat demand/margin/FCF bridge before Stage2/Yellow promotion","TIGERELEC_219130_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_PCB_SOCKET|DOOSANTESNA_131970_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_SERVICE",2,2,2,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C08_AFACT_200470_2024_03_06_TEST_SERVICE_EVENT_RERATING_4B","symbol":"200470","company_name":"에이팩트","round":"R2","loop":"117","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SERVICE_REPEAT_DEMAND_EVENT_RERATING_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"AFACT_200470_2024_03_06_STAGE2A_TEST_SERVICE_RERATING","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only in 2022; selected 2024 window is clean","independent_evidence_weight":0.95,"score_price_alignment":"semiconductor test-service rerating captured 45.61% MFE, but later full-window drawdown required C08 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol versus loops 103/104/109/115/116; QRT was rejected due to 2024 share-count drift in the selected window"}
{"row_type":"case","case_id":"C08_TIGERELEC_219130_2024_03_06_TEST_PCB_SOCKET_EVENT_PREMIUM_FAIL","symbol":"219130","company_name":"타이거일렉","round":"R2","loop":"117","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_PCB_SOCKET_EVENT_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TIGERELEC_219130_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_PCB_SOCKET","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"test PCB/socket premium produced a tradable MFE but high early MAE and severe full-window drawdown without repeat-demand and margin bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol; zero corporate-action candidates in profile"}
{"row_type":"case","case_id":"C08_DOOSANTESNA_131970_2024_03_06_TEST_SERVICE_PREMIUM_FAIL","symbol":"131970","company_name":"두산테스나","round":"R2","loop":"117","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMICONDUCTOR_TEST_SERVICE_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"DOOSANTESNA_131970_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_SERVICE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates in 2020 and 2024 market-board label switch only; selected price window is usable","independent_evidence_weight":0.95,"score_price_alignment":"test-service premium produced ~20% MFE but later persistent MAE without repeat-demand, margin, revision and FCF bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol; KOSDAQ GLOBAL market label switch is not treated as corporate action"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"AFACT_200470_2024_03_06_STAGE2A_TEST_SERVICE_RERATING","case_id":"C08_AFACT_200470_2024_03_06_TEST_SERVICE_EVENT_RERATING_4B","symbol":"200470","company_name":"에이팩트","round":"R2","loop":"117","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SERVICE_REPEAT_DEMAND_EVENT_RERATING_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":4725.0,"evidence_available_at_that_date":"source_proxy_only: semiconductor test-service event rerating, memory/test-cycle expectation, repeat service demand route, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["test_service_event_rerating","memory_test_cycle_expectation","repeat_test_service_demand","relative_strength"],"stage3_evidence_fields":["customer_repeat_demand_partial","margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","event_crowding","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/200/200470/2024.csv","profile_path":"atlas/symbol_profiles/200/200470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":45.61,"MFE_90D_pct":45.61,"MFE_180D_pct":45.61,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-1.38,"MAE_90D_pct":-1.38,"MAE_180D_pct":-41.27,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-29","peak_price":6880.0,"drawdown_after_peak_pct":-59.74,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.69,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"test_service_rerating_worked_but_full_window_drawdown_requires_C08_4B_audit","four_b_evidence_type":["valuation_rerating","event_crowding"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C08_200470_2024_03_06_4725","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only in 2022; selected 2024 window is clean","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TIGERELEC_219130_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_PCB_SOCKET","case_id":"C08_TIGERELEC_219130_2024_03_06_TEST_PCB_SOCKET_EVENT_PREMIUM_FAIL","symbol":"219130","company_name":"타이거일렉","round":"R2","loop":"117","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_PCB_SOCKET_EVENT_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":34000.0,"evidence_available_at_that_date":"source_proxy_only: test PCB/socket premium and HBM/test board narrative visible, but repeat-demand, margin bridge, revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["test_pcb_socket_premium","hbm_test_board_narrative","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","weak_follow_through","bridge_absent"],"stage4c_evidence_fields":["repeat_demand_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/219/219130/2024.csv","profile_path":"atlas/symbol_profiles/219/219130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.18,"MFE_90D_pct":33.24,"MFE_180D_pct":33.24,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-22.06,"MAE_90D_pct":-21.62,"MAE_180D_pct":-56.0,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-14","peak_price":45300.0,"drawdown_after_peak_pct":-66.98,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.75,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"test_pcb_socket_event_premium_not_C08_stage3_without_repeat_demand_margin_bridge","four_b_evidence_type":["event_premium","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mid_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_219130_2024_03_06_34000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"DOOSANTESNA_131970_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_SERVICE","case_id":"C08_DOOSANTESNA_131970_2024_03_06_TEST_SERVICE_PREMIUM_FAIL","symbol":"131970","company_name":"두산테스나","round":"R2","loop":"117","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMICONDUCTOR_TEST_SERVICE_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_REVISION_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":44350.0,"evidence_available_at_that_date":"source_proxy_only: semiconductor test-service customer-quality premium visible, but repeat-demand, margin, revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["test_service_premium","customer_quality_narrative","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["valuation_premium","weak_follow_through","bridge_absent"],"stage4c_evidence_fields":["repeat_demand_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131970/2024.csv","profile_path":"atlas/symbol_profiles/131/131970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.18,"MFE_90D_pct":20.18,"MFE_180D_pct":20.18,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-5.52,"MAE_90D_pct":-19.17,"MAE_180D_pct":-37.66,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-05","peak_price":53300.0,"drawdown_after_peak_pct":-48.12,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.83,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"test_service_premium_not_C08_stage3_without_repeat_demand_margin_revision_bridge","four_b_evidence_type":["valuation_premium","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_limited_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["market_label_switch_not_corporate_action"],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C08_131970_2024_03_06_44350","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates in 2020 and 2024 market label switch only","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_AFACT_200470_2024_03_06_TEST_SERVICE_EVENT_RERATING_4B","trigger_id":"AFACT_200470_2024_03_06_STAGE2A_TEST_SERVICE_RERATING","symbol":"200470","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":65,"stage_label_after":"Stage2-watch with C08 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Test-service event rerating worked, but Green requires repeat-demand/margin/revision/FCF proof and later drawdown audit.","MFE_90D_pct":45.61,"MAE_90D_pct":-1.38,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_TIGERELEC_219130_2024_03_06_TEST_PCB_SOCKET_EVENT_PREMIUM_FAIL","trigger_id":"TIGERELEC_219130_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_PCB_SOCKET","symbol":"219130","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage2 false-positive / test PCB risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C08 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Test PCB/socket premium without repeat-demand and margin bridge produced MFE but with high MAE and drawdown.","MFE_90D_pct":33.24,"MAE_90D_pct":-21.62,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_DOOSANTESNA_131970_2024_03_06_TEST_SERVICE_PREMIUM_FAIL","trigger_id":"DOOSANTESNA_131970_2024_03_06_STAGE2_FALSE_POSITIVE_TEST_SERVICE","symbol":"131970","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2 false-positive / test-service risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C08 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Test-service premium without repeat-demand/margin/revision bridge produced limited MFE and later persistent MAE.","MFE_90D_pct":20.18,"MAE_90D_pct":-19.17,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"117","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 117
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C02_POWER_GRID_DATACENTER_CAPEX, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C15_MATERIAL_SPREAD_SUPERCYCLE, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_ONLY_IF_UNCOVERED_FINE_ARCHETYPE
```

If this loop is accepted together with local C08 loops 103, 104, 109, 115, and 116, C08 reaches and exceeds the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C08 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/200/200470/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/219/219130/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/131/131970/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/200/200470.json
  - atlas/symbol_profiles/219/219130.json
  - atlas/symbol_profiles/131/131970.json
- Considered but rejected:
  - atlas/symbol_profiles/405/405100.json
- Rejected local duplicate C08 symbols:
  - 058470, 098120, 080580
  - 232140, 253590, 131290
  - 252990, 425420, 424980
  - 089030, 330860, 061970
  - 095340, 036540, 033170
- Rejected static top-covered C08 symbols or contamination-risk names:
  - 067310, 092870, 097800
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
