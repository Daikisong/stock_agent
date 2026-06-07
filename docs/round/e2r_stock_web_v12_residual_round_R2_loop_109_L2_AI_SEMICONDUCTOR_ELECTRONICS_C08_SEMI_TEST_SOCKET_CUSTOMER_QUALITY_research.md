# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_109_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
selected_round: R2
selected_loop: 109
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: PROBE_CARD_CERAMIC_SUBSTRATE_CUSTOMER_QUALITY_REPEAT_DEMAND_4B_WATCH
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

This loop adds 3 new independent C08 rows and moves C08 from static 14 rows to local projected 20 after loops 103/104, then to projected 23 after this loop.

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

C08 is the semi test/socket customer-quality archetype. The bridge is not “probe card / socket / tester label.” It is customer qualification, repeat consumable or repeat tester demand, margin, revision, and FCF. The label opens the door; the repeat-demand bridge decides whether anyone actually walks through it.

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
| this loop projected rows | 23 |

Selected symbols avoid local C08 loop103 symbols `058470`, `098120`, `080580` and loop104 symbols `232140`, `253590`, `131290`. Static top-covered candidates `092870` and `097800` were rejected due to 2024 forward-window corporate-action contamination risk.

| symbol | company | status |
|---|---|---|
| 252990 | 샘씨엔에스 | new local C08 symbol |
| 425420 | 티에프이 | new local C08 symbol |
| 424980 | 마이크로투나노 | new local C08 symbol |

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
| 252990 / 2024-03-06 | true | true | clean_180D_window | true |
| 425420 / 2024-03-06 | true | true | clean_180D_window | true |
| 424980 / 2024-03-06 | true | true | clean_180D_window | true |

Corporate-action notes:

- 샘씨엔에스 has zero corporate-action candidates.
- 티에프이 has zero corporate-action candidates.
- 마이크로투나노 has zero corporate-action candidates.
- 하나마이크론(067310) was considered but rejected as a static top-covered C08 symbol and because 2024 row stream has share-count changes later in the forward window.
- 윈팩(097800) was rejected due to a 2024-05-31 corporate-action candidate.
- 엑시콘(092870) was rejected due to a 2024-07-31 corporate-action candidate.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| PROBE_CARD_CERAMIC_SUBSTRATE_CUSTOMER_QUALITY_REPEAT_DEMAND_4B_WATCH | C08 | probe-card customer-quality route can support Stage2A, but event crowding needs 4B audit |
| TEST_SOCKET_PROBE_CARD_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_BRIDGE | C08 | socket/probe-card premium without repeat demand is false-positive risk |
| PROBE_CARD_EVENT_PREMIUM_WITHOUT_CUSTOMER_QUALIFICATION_BRIDGE | C08 | probe-card event premium needs qualification and repeat-demand bridge before Stage2/Yellow |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C08_SEMCNS_252990_2024_03_06_PROBE_CARD_CUSTOMER_QUALITY_RERATING_4B | 252990 | 샘씨엔에스 | 4B_overlay_success | positive | customer-quality route produced 100%+ MFE but then large drawdown |
| C08_TFE_425420_2024_03_06_TEST_SOCKET_PROBE_EVENT_PREMIUM_FAIL | 425420 | 티에프이 | failed_rerating | counterexample | socket/probe premium had only mid-teens MFE and severe MAE |
| C08_MICRO2NANO_424980_2024_03_06_PROBE_CARD_EVENT_PREMIUM_FAIL | 424980 | 마이크로투나노 | failed_rerating | counterexample | probe-card event premium had sub-20% MFE and severe MAE |

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
| 252990 | source_proxy_only | probe-card ceramic substrate / customer-quality / repeat test demand | required before promotion |
| 425420 | source_proxy_only | socket/probe-card event premium but repeat-demand bridge absent | required; useful as counterexample |
| 424980 | source_proxy_only | probe-card event premium but customer qualification bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 252990 | atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv | atlas/symbol_profiles/252/252990.json |
| 425420 | atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv | atlas/symbol_profiles/425/425420.json |
| 424980 | atlas/ohlcv_tradable_by_symbol_year/424/424980/2024.csv | atlas/symbol_profiles/424/424980.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| SEMCNS_252990_2024_03_06_STAGE2A_PROBE_CARD_CUSTOMER_QUALITY | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 7140 | probe-card customer qualification / ceramic substrate / repeat demand |
| TFE_425420_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_PROBE_PREMIUM | Stage2 | 2024-03-06 | 2024-03-06 | 38000 | socket/probe-card premium without repeat-demand bridge |
| MICRO2NANO_424980_2024_03_06_STAGE2_FALSE_POSITIVE_PROBE_CARD_EVENT | Stage2 | 2024-03-06 | 2024-03-06 | 13030 | probe-card event premium without customer-qualification bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 252990 | 2024-03-06 | 7140 | 115.69 | -10.64 | 115.69 | -19.05 | 115.69 | -33.47 | 2024-04-02 | 15400 | -69.16 |
| 425420 | 2024-03-06 | 38000 | 15.39 | -14.08 | 15.39 | -31.84 | 15.39 | -61.24 | 2024-03-21 | 43850 | -66.41 |
| 424980 | 2024-03-06 | 13030 | 18.19 | -9.75 | 18.19 | -21.72 | 18.19 | -57.48 | 2024-04-02 | 15400 | -64.03 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 252990 | Stage2A/Yellow possible; 4B after probe-card rerating | extreme MFE but large post-peak drawdown | current_profile_4B_too_late |
| 425420 | Stage2 risk if socket/probe-card premium is over-credited | mid-teens MFE and severe MAE | current_profile_false_positive |
| 424980 | Stage2 risk if probe-card event premium is over-credited | sub-20% MFE and severe MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C08 interpretation:

- Stage2A can work when tester/socket/probe-card exposure is tied to qualification and repeat-demand conversion.
- Yellow/Green require repeat-demand, margin, revision, and FCF proof.
- Probe-card/socket event premium without conversion bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 252990 | 1.00 | 1.00 | probe-card rerating / event crowding | 4B audit required after extreme MFE |
| 425420 | 1.00 | 1.00 | socket/probe-card premium / bridge absent | not Stage3 without repeat-demand bridge |
| 424980 | 1.00 | 1.00 | probe-card event premium / bridge absent | not Stage3 without qualification bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 252990 | thesis_break_watch_only | not hard 4C, but 4B cap needed after rerating |
| 425420 | hard_4c_late | repeat-demand/margin bridge absence should have capped Stage2 earlier |
| 424980 | hard_4c_late | customer qualification/repeat-demand bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, tester/socket/probe-card exposure can support Stage2A only when customer qualification, repeat-demand conversion, margin bridge, revision, or FCF is visible. Event-like probe-card/socket premiums without that bridge should not become Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
confidence = medium
```

Candidate C08 rule:

```text
C08_socket_customer_quality_bridge_required =
  test_socket_or_tester_or_probe_card_route
  AND (customer_qualification OR repeat_demand OR repeat_consumable_route OR margin_bridge OR confirmed_revision OR fcf_conversion)

if tester_or_socket_or_probe_card_event_premium and customer_quality_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 40 and drawdown_after_peak < -35:
    add C08_peak_proximity_4B_audit = true

if MFE_90D < 20 and MAE_90D < -20:
    classify_as C08_tester_probe_event_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 49.76 | -24.2 | 49.76 | -50.73 | 2 | useful but C08 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 49.76 | -24.2 | 49.76 | -50.73 | 2 | over-credits event premiums |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 115.69 | -19.05 | 115.69 | -33.47 | 0 | better after customer-quality bridge gate |
| P2 canonical_archetype_candidate_profile | C08 | 1 promoted + 2 guard | 115.69 | -19.05 | 115.69 | -33.47 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C08 guard | 1 promoted + 2 guard | 115.69 | -19.05 | 115.69 | -33.47 | 0 | adds probe/socket-event false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 252990 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 425420 | Stage2 false positive if repeat-demand bridge not enforced | current_profile_false_positive |
| 424980 | Stage2 false positive if customer-quality bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | mixed C08 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 14 -> local 20 -> projected 23; still need 7 to reach 30 |

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
new_axis_proposed: C08_socket_customer_quality_bridge_required|C08_peak_proximity_4B_audit|C08_tester_probe_event_false_positive_guardrail
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
- Avoids local loop103 and loop104 C08 symbol/trigger/date combinations.
- Rejects 092870 and 097800 due to 2024 forward-window corporate-action contamination risk.
- Rejects 067310 due to static top-covered status and later 2024 share-count changes.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_socket_customer_quality_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"425420/424980 show socket/probe-card premiums can fail without customer qualification/repeat-demand bridge while 252990 works only as Stage2A with 4B audit","blocks two false positives while preserving 252990 Stage2A","SEMCNS_252990_2024_03_06_STAGE2A_PROBE_CARD_CUSTOMER_QUALITY|TFE_425420_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_PROBE_PREMIUM|MICRO2NANO_424980_2024_03_06_STAGE2_FALSE_POSITIVE_PROBE_CARD_EVENT",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C08_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"252990 probe-card customer-quality rerating needed 4B audit after extreme MFE and drawdown","adds 4B audit after large C08 MFE without converting price-only peaks into Green","SEMCNS_252990_2024_03_06_STAGE2A_PROBE_CARD_CUSTOMER_QUALITY",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C08_tester_probe_event_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"425420/424980 had limited MFE and severe MAE after socket/probe-card event premium","requires qualification/repeat demand/margin/FCF bridge before Stage2/Yellow promotion","TFE_425420_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_PROBE_PREMIUM|MICRO2NANO_424980_2024_03_06_STAGE2_FALSE_POSITIVE_PROBE_CARD_EVENT",2,2,2,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C08_SEMCNS_252990_2024_03_06_PROBE_CARD_CUSTOMER_QUALITY_RERATING_4B","symbol":"252990","company_name":"샘씨엔에스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"PROBE_CARD_CERAMIC_SUBSTRATE_CUSTOMER_QUALITY_REPEAT_DEMAND_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"SEMCNS_252990_2024_03_06_STAGE2A_PROBE_CARD_CUSTOMER_QUALITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"probe-card ceramic substrate/customer-quality route captured 100%+ MFE, but later peak-to-drawdown required C08 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol versus loops 103/104; zero corporate-action candidates in profile"}
{"row_type":"case","case_id":"C08_TFE_425420_2024_03_06_TEST_SOCKET_PROBE_EVENT_PREMIUM_FAIL","symbol":"425420","company_name":"티에프이","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_PROBE_CARD_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TFE_425420_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_PROBE_PREMIUM","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"test socket/probe-card premium had only mid-teens MFE and then severe 90D/180D MAE without repeat-demand or margin bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol; zero corporate-action candidates in profile"}
{"row_type":"case","case_id":"C08_MICRO2NANO_424980_2024_03_06_PROBE_CARD_EVENT_PREMIUM_FAIL","symbol":"424980","company_name":"마이크로투나노","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"PROBE_CARD_EVENT_PREMIUM_WITHOUT_CUSTOMER_QUALIFICATION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"MICRO2NANO_424980_2024_03_06_STAGE2_FALSE_POSITIVE_PROBE_CARD_EVENT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"probe-card event premium produced sub-20% MFE and then severe MAE without customer qualification/repeat-demand bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol; zero corporate-action candidates in profile"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"SEMCNS_252990_2024_03_06_STAGE2A_PROBE_CARD_CUSTOMER_QUALITY","case_id":"C08_SEMCNS_252990_2024_03_06_PROBE_CARD_CUSTOMER_QUALITY_RERATING_4B","symbol":"252990","company_name":"샘씨엔에스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"PROBE_CARD_CERAMIC_SUBSTRATE_CUSTOMER_QUALITY_REPEAT_DEMAND_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":7140.0,"evidence_available_at_that_date":"source_proxy_only: probe-card ceramic substrate customer qualification, repeat test consumable demand, HBM/test cycle route, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["probe_card_customer_qualification","ceramic_substrate_route","repeat_test_consumable_demand","relative_strength"],"stage3_evidence_fields":["customer_quality_bridge_partial","repeat_demand_bridge_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","event_crowding","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv","profile_path":"atlas/symbol_profiles/252/252990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":115.69,"MFE_90D_pct":115.69,"MFE_180D_pct":115.69,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-10.64,"MAE_90D_pct":-19.05,"MAE_180D_pct":-33.47,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-02","peak_price":15400.0,"drawdown_after_peak_pct":-69.16,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"probe_card_customer_quality_rerating_worked_but_full_window_drawdown_requires_C08_4B_audit","four_b_evidence_type":["valuation_rerating","event_crowding"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_252990_2024_03_06_7140","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TFE_425420_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_PROBE_PREMIUM","case_id":"C08_TFE_425420_2024_03_06_TEST_SOCKET_PROBE_EVENT_PREMIUM_FAIL","symbol":"425420","company_name":"티에프이","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_PROBE_CARD_PREMIUM_WITHOUT_REPEAT_DEMAND_MARGIN_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":38000.0,"evidence_available_at_that_date":"source_proxy_only: test socket/probe-card premium and event strength visible, but customer qualification, repeat consumable demand, margin and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["socket_probe_theme_premium","relative_strength_event"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","bridge_absent","weak_follow_through"],"stage4c_evidence_fields":["customer_qualification_absent","repeat_demand_absent","margin_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv","profile_path":"atlas/symbol_profiles/425/425420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.39,"MFE_90D_pct":15.39,"MFE_180D_pct":15.39,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-14.08,"MAE_90D_pct":-31.84,"MAE_180D_pct":-61.24,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-21","peak_price":43850.0,"drawdown_after_peak_pct":-66.41,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"socket_probe_premium_not_stage3_without_repeat_demand_margin_bridge","four_b_evidence_type":["event_premium","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mid_mfe_high_mae_customer_quality_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_425420_2024_03_06_38000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"MICRO2NANO_424980_2024_03_06_STAGE2_FALSE_POSITIVE_PROBE_CARD_EVENT","case_id":"C08_MICRO2NANO_424980_2024_03_06_PROBE_CARD_EVENT_PREMIUM_FAIL","symbol":"424980","company_name":"마이크로투나노","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"PROBE_CARD_EVENT_PREMIUM_WITHOUT_CUSTOMER_QUALIFICATION_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":13030.0,"evidence_available_at_that_date":"source_proxy_only: probe-card event premium and short relative strength visible, but customer qualification, repeat-demand, margin/revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["probe_card_event_premium","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","bridge_absent","weak_follow_through"],"stage4c_evidence_fields":["customer_qualification_absent","repeat_demand_absent","margin_revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/424/424980/2024.csv","profile_path":"atlas/symbol_profiles/424/424980.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.19,"MFE_90D_pct":18.19,"MFE_180D_pct":18.19,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-9.75,"MAE_90D_pct":-21.72,"MAE_180D_pct":-57.48,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-02","peak_price":15400.0,"drawdown_after_peak_pct":-64.03,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"probe_card_event_premium_not_stage3_without_customer_qualification_repeat_demand_bridge","four_b_evidence_type":["event_premium","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mid_mfe_high_mae_customer_quality_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_424980_2024_03_06_13030","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_SEMCNS_252990_2024_03_06_PROBE_CARD_CUSTOMER_QUALITY_RERATING_4B","trigger_id":"SEMCNS_252990_2024_03_06_STAGE2A_PROBE_CARD_CUSTOMER_QUALITY","symbol":"252990","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Actionable with C08 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Probe-card customer-quality route worked, but Yellow/Green needs repeat qualification, margin, revision, and FCF conversion plus valuation 4B audit.","MFE_90D_pct":115.69,"MAE_90D_pct":-19.05,"score_return_alignment_label":"positive_extreme_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_TFE_425420_2024_03_06_TEST_SOCKET_PROBE_EVENT_PREMIUM_FAIL","trigger_id":"TFE_425420_2024_03_06_STAGE2_FALSE_POSITIVE_SOCKET_PROBE_PREMIUM","symbol":"425420","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":6,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C08 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Socket/probe-card premium without repeat-demand and margin bridge produced limited upside and severe drawdown.","MFE_90D_pct":15.39,"MAE_90D_pct":-31.84,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_MICRO2NANO_424980_2024_03_06_PROBE_CARD_EVENT_PREMIUM_FAIL","trigger_id":"MICRO2NANO_424980_2024_03_06_STAGE2_FALSE_POSITIVE_PROBE_CARD_EVENT","symbol":"424980","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/4C-watch, not C08 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Probe-card event premium without customer qualification/repeat demand should not receive C08 promotion.","MFE_90D_pct":18.19,"MAE_90D_pct":-21.72,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 109
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C15_MATERIAL_SPREAD_SUPERCYCLE, C02_POWER_GRID_DATACENTER_CAPEX
```

If this loop is accepted together with local loops 103 and 104, C08 moves to projected 23 rows and still needs 7 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C08 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/424/424980/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/252/252990.json
  - atlas/symbol_profiles/425/425420.json
  - atlas/symbol_profiles/424/424980.json
- Rejected local duplicates:
  - 058470, 098120, 080580
  - 232140, 253590, 131290
- Rejected due to candidate forward-window contamination risk:
  - 092870, 097800
- Rejected due to static top-covered + 2024 share-count changes:
  - 067310
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
