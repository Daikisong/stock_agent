# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
selected_round: R2
selected_loop: 110
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 2 quality_repair_exact_50_after_local_priority0_priority1_fill
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: C08_TEST_SOCKET_TEST_SERVICE_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE
deep_sub_archetype_id: C08_DEEP_TESTER_HANDLER_TEST_SERVICE_SUBSTRATE_INSPECTION_QUALITY_BRIDGE_VS_EVENT_PREMIUM_FADE
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - residual_false_positive_mining
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_specific_rule_discovery
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 7 new independent cases, 4 counterexamples, and 7 residual errors for L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

## 1. Selection Rationale

The static No-Repeat Index already lists C08 at the 50-row threshold, while all Priority 0 and Priority 1 archetypes have been locally pushed toward or above the 50-row band in this session. Therefore this loop moves from pure shortage filling into **quality repair**: C08 still needs cleaner positive/counterexample balance, more direct tester/test-service/inspection routes, and a sharper distinction between customer-quality conversion and mere semiconductor test label premium.

```text
published_index_status = C08 rows 50, Priority 2 quality 보강
local_session_status = C02/C09/C14/C10/C06/C07/C11/C01/C28/C12/C05/C23/C27 already filled or locally lifted
selected_scope = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
selected_reason = exact-50 quality repair + L2 positive/counterexample balance + C08 bridge/4B refinement
```

Existing visible C08 loops include standard v12 loop 100, 103, 104 and 109. This loop avoids visible C08 loop 103/104/109 symbol groups: `058470`, `098120`, `080580`, `232140`, `253590`, `131290`, `252990`, `425420`, `424980`. It also avoids the rejected C08 candidates previously called out in loop109: `092870`, `097800`, `067310`.

## 2. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Manifest basis: `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`.

## 3. Historical Eligibility Gate

| symbol | company | entry row exists | >=180 forward trading days | 180D share-count proxy | calibration usable |
|---|---|---:|---:|---|---:|
| 003160 | 디아이 | true | true | clean_180D_window | true |
| 086390 | 유니테스트 | true | true | clean_180D_window | true |
| 110990 | 디아이티 | true | true | clean_180D_window | true |
| 420770 | 기가비스 | true | true | clean_180D_window | true |
| 089790 | 제이티 | true | true | clean_180D_window | true |
| 119830 | 아이텍 | true | true | clean_180D_window | true |
| 131970 | 두산테스나 | true | true | clean_180D_window | true |


Profile JSON paths are recorded per row. Because the local runtime cannot persist the JSON profile files directly, the 180D corporate-action gate is cross-checked from the tradable shard's `s` share-count stability over the same forward window. All selected rows show one unique share-count value across entry~D+180.

## 4. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| TESTER_TEST_SERVICE_CUSTOMER_QUALITY_REPEAT_DEMAND | C08 | tester/test-service label supports Stage2A only when repeat demand or customer-quality bridge is visible |
| SUBSTRATE_INSPECTION_QUALITY_EVENT_PREMIUM | C08 | inspection/substrate quality event premium needs customer qualification, repeat inspection demand, revenue, margin or FCF bridge |
| TEST_SOCKET_HANDLER_LABEL_WITHOUT_CONVERSION | C08 | handler/socket/test label without conversion bridge is a false-positive/4B-watch path |

## 5. Case Selection Summary

| case_id | symbol | company | role | polarity | why_selected |
| --- | --- | --- | --- | --- | --- |
| C08_003160_2024_03_06_MEMORY_TESTER_EVENT_RERATING_4B_WATCH | 003160 | 디아이 | memory_tester_event_rerating_4B_watch | positive | new C08 symbol/family; direct tester, test-service, inspection or substrate-quality route |
| C08_086390_2024_03_06_MEMORY_TESTER_CUSTOMER_REPEAT_DEMAND_RECOVERY | 086390 | 유니테스트 | memory_tester_customer_repeat_demand_recovery | positive | new C08 symbol/family; direct tester, test-service, inspection or substrate-quality route |
| C08_110990_2024_03_06_INSPECTION_EQUIPMENT_EVENT_PREMIUM_4B_DRAWDOWN | 110990 | 디아이티 | inspection_equipment_event_premium_4B_drawdown | positive | new C08 symbol/family; direct tester, test-service, inspection or substrate-quality route |
| C08_420770_2024_03_06_SUBSTRATE_INSPECTION_QUALITY_EVENT_FADE | 420770 | 기가비스 | substrate_inspection_quality_event_fade | counterexample | new C08 symbol/family; direct tester, test-service, inspection or substrate-quality route |
| C08_089790_2024_03_06_TEST_HANDLER_CUSTOMER_QUALITY_BRIDGE_ABSENT | 089790 | 제이티 | test_handler_customer_quality_bridge_absent | counterexample | new C08 symbol/family; direct tester, test-service, inspection or substrate-quality route |
| C08_119830_2024_03_06_SEMICONDUCTOR_TEST_SERVICE_LABEL_WITHOUT_MARGIN_BRIDGE | 119830 | 아이텍 | semiconductor_test_service_label_without_margin_bridge | counterexample | new C08 symbol/family; direct tester, test-service, inspection or substrate-quality route |
| C08_131970_2024_03_06_TEST_SERVICE_CUSTOMER_QUALITY_MID_MFE_HIGH_MAE | 131970 | 두산테스나 | test_service_customer_quality_mid_mfe_high_mae | counterexample | new C08 symbol/family; direct tester, test-service, inspection or substrate-quality route |

## 6. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 3 |
| counterexample_count | 4 |
| stage4b_case_count | 7 |
| stage4c_case_count | 1 |
| calibration_usable_case_count | 7 |
| calibration_usable_trigger_count | 7 |
| new_independent_case_count | 7 |
| reused_case_count | 0 |

Minimum conditions pass: positive >=1, counterexample >=1, calibration usable >=3, new independent ratio 100%.

## 7. Evidence Source Map

| symbol | company | source status | non-price evidence status | URL repair need |
|---|---|---|---|---|
| 003160 | 디아이 | source_proxy_only | direct/partial customer-quality bridge; memory_tester_route, customer_quality_proxy, relative_strength, order_revenue_bridge_partial | required before promotion |
| 086390 | 유니테스트 | source_proxy_only | direct/partial customer-quality bridge; memory_tester_route, repeat_demand_proxy, margin_bridge_partial, relative_strength | required before promotion |
| 110990 | 디아이티 | source_proxy_only | direct/partial customer-quality bridge; inspection_equipment_route, AOI_quality_proxy, relative_strength, valuation_event | required before promotion |
| 420770 | 기가비스 | source_proxy_only | bridge absent or not yet converted; substrate_inspection_route, quality_event_premium, repeat_demand_bridge_absent | required before promotion |
| 089790 | 제이티 | source_proxy_only | bridge absent or not yet converted; test_handler_route, relative_strength_event, customer_quality_bridge_absent | required before promotion |
| 119830 | 아이텍 | source_proxy_only | bridge absent or not yet converted; semiconductor_test_service_route, test_outsourcing_label, margin_bridge_absent | required before promotion |
| 131970 | 두산테스나 | source_proxy_only | bridge absent or not yet converted; test_service_route, customer_quality_label, revenue_bridge_delayed | required before promotion |


No trigger row uses price-only evidence to promote Stage3. Price path is used only for historical calibration and stress testing.

## 8. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 003160 | atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv | atlas/symbol_profiles/003/003160.json |
| 086390 | atlas/ohlcv_tradable_by_symbol_year/086/086390/2024.csv | atlas/symbol_profiles/086/086390.json |
| 110990 | atlas/ohlcv_tradable_by_symbol_year/110/110990/2024.csv | atlas/symbol_profiles/110/110990.json |
| 420770 | atlas/ohlcv_tradable_by_symbol_year/420/420770/2024.csv | atlas/symbol_profiles/420/420770.json |
| 089790 | atlas/ohlcv_tradable_by_symbol_year/089/089790/2024.csv | atlas/symbol_profiles/089/089790.json |
| 119830 | atlas/ohlcv_tradable_by_symbol_year/119/119830/2024.csv | atlas/symbol_profiles/119/119830.json |
| 131970 | atlas/ohlcv_tradable_by_symbol_year/131/131970/2024.csv | atlas/symbol_profiles/131/131970.json |


## 9. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence_summary |
| --- | --- | --- | --- | --- | --- |
| C08_003160_2024_03_06_STAGE2_ACTIONABLE_MEMORY_TESTER_EVENT_RERATING_4B_WATCH | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 12070 | memory_tester_route;customer_quality_proxy;relative_strength;order_revenue_bridge_partial |
| C08_086390_2024_03_06_STAGE2_ACTIONABLE_MEMORY_TESTER_CUSTOMER_REPEAT_DEMAND_RECOVERY | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 14050 | memory_tester_route;repeat_demand_proxy;margin_bridge_partial;relative_strength |
| C08_110990_2024_03_06_STAGE2_ACTIONABLE_INSPECTION_EQUIPMENT_EVENT_PREMIUM_4B_DRAWDOWN | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 22600 | inspection_equipment_route;AOI_quality_proxy;relative_strength;valuation_event |
| C08_420770_2024_03_06_STAGE2_SUBSTRATE_INSPECTION_QUALITY_EVENT_FADE | Stage2 | 2024-03-06 | 2024-03-06 | 62800 | substrate_inspection_route;quality_event_premium;repeat_demand_bridge_absent |
| C08_089790_2024_03_06_STAGE2_TEST_HANDLER_CUSTOMER_QUALITY_BRIDGE_ABSENT | Stage2 | 2024-03-06 | 2024-03-06 | 10180 | test_handler_route;relative_strength_event;customer_quality_bridge_absent |
| C08_119830_2024_03_06_STAGE2_SEMICONDUCTOR_TEST_SERVICE_LABEL_WITHOUT_MARGIN_BRIDGE | Stage2 | 2024-03-06 | 2024-03-06 | 7400 | semiconductor_test_service_route;test_outsourcing_label;margin_bridge_absent |
| C08_131970_2024_03_06_STAGE2_TEST_SERVICE_CUSTOMER_QUALITY_MID_MFE_HIGH_MAE | Stage2 | 2024-03-06 | 2024-03-06 | 44350 | test_service_route;customer_quality_label;revenue_bridge_delayed |

## 10. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 003160 | 2024-03-06 | 12070 | 110.02 | -23.45 | 155.18 | -23.45 | 155.18 | -23.45 | 2024-06-27 | 30800 | -64.58 |
| 086390 | 2024-03-06 | 14050 | 31.32 | -2.63 | 38.79 | -7.19 | 38.79 | -40.57 | 2024-05-23 | 19500 | -57.18 |
| 110990 | 2024-03-06 | 22600 | 36.95 | -25.88 | 43.14 | -25.88 | 43.14 | -57.08 | 2024-04-26 | 32350 | -70.02 |
| 420770 | 2024-03-06 | 62800 | 31.37 | -3.66 | 31.37 | -23.96 | 31.37 | -62.02 | 2024-04-09 | 82500 | -71.09 |
| 089790 | 2024-03-06 | 10180 | 11.59 | -10.12 | 11.59 | -30.84 | 11.59 | -66.11 | 2024-04-12 | 11360 | -69.63 |
| 119830 | 2024-03-06 | 7400 | 15.14 | -0.81 | 18.24 | -7.43 | 18.24 | -38.78 | 2024-04-19 | 8750 | -48.23 |
| 131970 | 2024-03-06 | 44350 | 20.18 | -5.52 | 20.18 | -19.17 | 20.18 | -48.48 | 2024-04-05 | 53300 | -57.13 |

## 11. Current Calibrated Profile Stress Test

| case | current_profile_likely_judgment | actual_price_path_verdict | stress_result |
| --- | --- | --- | --- |
| 003160 | Stage2/Stage2A possible if C08 label over-credited | MFE90 155.18 / MAE90 -23.45 | current_profile_4B_too_late |
| 086390 | Stage2/Stage2A possible if C08 label over-credited | MFE90 38.79 / MAE90 -7.19 | current_profile_4B_too_late |
| 110990 | Stage2/Stage2A possible if C08 label over-credited | MFE90 43.14 / MAE90 -25.88 | current_profile_4B_too_late |
| 420770 | Stage2/Stage2A possible if C08 label over-credited | MFE90 31.37 / MAE90 -23.96 | current_profile_false_positive |
| 089790 | Stage2/Stage2A possible if C08 label over-credited | MFE90 11.59 / MAE90 -30.84 | current_profile_false_positive |
| 119830 | Stage2/Stage2A possible if C08 label over-credited | MFE90 18.24 / MAE90 -7.43 | current_profile_false_positive |
| 131970 | Stage2/Stage2A possible if C08 label over-credited | MFE90 20.18 / MAE90 -19.17 | current_profile_false_positive |

## 12. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C08 interpretation:

- Stage2-Actionable can work when tester/test-service/inspection exposure is tied to customer qualification, repeat demand, revenue bridge or margin bridge.
- Stage3-Yellow/Green should not be unlocked by a tester, socket, handler, probe-card, OSAT-test or inspection label alone.
- Strong event MFE followed by large drawdown should be routed to local 4B-watch unless the repeat-demand/margin bridge is explicit.

## 13. 4B Local vs Full-window Timing Audit

| symbol | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 003160 | 1.0 | 1.0 | event rerating / customer-quality bridge check | 4B audit required |
| 086390 | 1.0 | 1.0 | event rerating / customer-quality bridge check | 4B audit required |
| 110990 | 1.0 | 1.0 | event rerating / customer-quality bridge check | 4B audit required |
| 420770 | 1.0 | 1.0 | event rerating / customer-quality bridge check | 4B audit required |
| 089790 | 1.0 | 1.0 | event rerating / customer-quality bridge check | 4B audit required |
| 119830 | 1.0 | 1.0 | event rerating / customer-quality bridge check | 4B audit required |
| 131970 | 1.0 | 1.0 | event rerating / customer-quality bridge check | 4B audit required |


## 14. 4C Protection Audit

| symbol | four_c_protection_label | interpretation |
|---|---|---|
| 003160 | thesis_break_watch_only | not hard 4C; local 4B/Stage2 watch is enough |
| 086390 | thesis_break_watch_only | not hard 4C; local 4B/Stage2 watch is enough |
| 110990 | thesis_break_watch_only | not hard 4C; local 4B/Stage2 watch is enough |
| 420770 | hard_4c_late | bridge absence should have capped Stage2 earlier |
| 089790 | hard_4c_late | bridge absence should have capped Stage2 earlier |
| 119830 | thesis_break_watch_only | not hard 4C; local 4B/Stage2 watch is enough |
| 131970 | thesis_break_watch_only | not hard 4C; local 4B/Stage2 watch is enough |


## 15. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, test/socket/probe/inspection exposure can support Stage2A only when customer qualification, repeat test demand, revenue conversion, margin bridge, or FCF conversion is visible. Event-like test label premiums without that bridge should stay Stage1/Stage2-watch and should not become Yellow/Green.

## 16. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
confidence = medium
```

Candidate C08 rule:

```text
C08_customer_quality_repeat_demand_bridge_required =
  tester_or_test_service_or_socket_or_probe_or_inspection_route
  AND (customer_qualification OR repeat_demand OR repeat_consumable_route OR revenue_bridge OR margin_bridge OR confirmed_revision OR fcf_conversion)

if C08_label_premium AND bridge_absent:
  cap_stage = Stage1/Stage2-watch
  do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 30 and drawdown_after_peak < -35:
  add C08_event_peak_4B_audit = true

if MFE_90D < 20 and MAE_90D < -20:
  classify_as C08_test_label_false_positive_guardrail
```

## 17. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 7 | 45.5 | -19.7 | 45.5 | -48.07 | 4 | useful but C08 bridge too loose |
| P1 canonical_archetype_candidate_profile | C08 guard | 3 promoted + 4 guard | 79.04 | -18.84 | 79.04 | -40.37 | 0 | better after bridge and 4B audit |


## 18. Score-Return Alignment Matrix

| symbol | score-return alignment | current_profile_verdict |
|---|---|---|
| 003160 | positive but 4B audit needed | current_profile_4B_too_late |
| 086390 | positive but 4B audit needed | current_profile_4B_too_late |
| 110990 | positive but 4B audit needed | current_profile_4B_too_late |
| 420770 | label/event premium over-credited without repeat-demand/margin bridge | current_profile_false_positive |
| 089790 | label/event premium over-credited without repeat-demand/margin bridge | current_profile_false_positive |
| 119830 | label/event premium over-credited without repeat-demand/margin bridge | current_profile_false_positive |
| 131970 | label/event premium over-credited without repeat-demand/margin bridge | current_profile_false_positive |


## 19. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage impact |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | mixed C08 fine ids | 3 | 4 | 7 | 1 | 7 | 0 | 7 | 7 | 7 | true | true | static 50 -> local quality +7; C08 enters post-50 quality repair band |

## 20. Residual Contribution Summary

```yaml
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
same_archetype_new_symbol_count: 7
same_archetype_new_trigger_family_count: 7
new_trigger_family_count: 7
positive_case_count: 3
counterexample_count: 4
stage4b_case_count: 7
stage4c_case_count: 1
source_proxy_only_count: 7
evidence_url_pending_count: 7
current_profile_error_count: 7
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_4B_too_late
  - current_profile_false_positive
  - C08_repeat_demand_bridge_absent
new_axis_proposed: C08_customer_quality_repeat_demand_bridge_required|C08_event_peak_4B_audit
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
promotion_blocked_until_url_repair: true
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 21. Validation Scope / Non-Validation Scope

Validation scope:

- Uses stock-web tradable OHLC rows.
- Uses manifest max_date 2026-02-20.
- Uses entry date 2024-03-06 and 180 trading-day forward windows inside stock-web.
- Uses C08 as post-50 quality repair target after local Priority 0/1 fill.
- Avoids visible C08 loop 103/104/109 symbol/date groups.
- Uses tradable shard share-count stability as a corporate-action proxy check for the selected 180D windows.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; all evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 22. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_customer_quality_repeat_demand_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"C08 tester/socket/test-service/inspection labels need customer qualification, repeat demand, revenue/margin bridge, or FCF conversion before Yellow/Green","blocks weak label/event false positives while preserving direct tester/service positives as Stage2A with 4B audit","C08_003160_2024_03_06_STAGE2_ACTIONABLE_MEMORY_TESTER_EVENT_RERATING_4B_WATCH|C08_086390_2024_03_06_STAGE2_ACTIONABLE_MEMORY_TESTER_CUSTOMER_REPEAT_DEMAND_RECOVERY|C08_110990_2024_03_06_STAGE2_ACTIONABLE_INSPECTION_EQUIPMENT_EVENT_PREMIUM_4B_DRAWDOWN|C08_420770_2024_03_06_STAGE2_SUBSTRATE_INSPECTION_QUALITY_EVENT_FADE|C08_089790_2024_03_06_STAGE2_TEST_HANDLER_CUSTOMER_QUALITY_BRIDGE_ABSENT|C08_119830_2024_03_06_STAGE2_SEMICONDUCTOR_TEST_SERVICE_LABEL_WITHOUT_MARGIN_BRIDGE|C08_131970_2024_03_06_STAGE2_TEST_SERVICE_CUSTOMER_QUALITY_MID_MFE_HIGH_MAE",7,7,4,medium,canonical_shadow_only,"not production; verified URL repair required before promotion"
shadow_weight,C08_event_peak_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"Several C08 paths show high MFE followed by severe drawdown; event peaks should become local 4B-watch unless repeat-demand bridge is verified","adds local 4B watch after large C08 MFE without converting price-only peaks into Green","C08_003160_2024_03_06_STAGE2_ACTIONABLE_MEMORY_TESTER_EVENT_RERATING_4B_WATCH|C08_086390_2024_03_06_STAGE2_ACTIONABLE_MEMORY_TESTER_CUSTOMER_REPEAT_DEMAND_RECOVERY|C08_110990_2024_03_06_STAGE2_ACTIONABLE_INSPECTION_EQUIPMENT_EVENT_PREMIUM_4B_DRAWDOWN|C08_420770_2024_03_06_STAGE2_SUBSTRATE_INSPECTION_QUALITY_EVENT_FADE|C08_089790_2024_03_06_STAGE2_TEST_HANDLER_CUSTOMER_QUALITY_BRIDGE_ABSENT|C08_119830_2024_03_06_STAGE2_SEMICONDUCTOR_TEST_SERVICE_LABEL_WITHOUT_MARGIN_BRIDGE|C08_131970_2024_03_06_STAGE2_TEST_SERVICE_CUSTOMER_QUALITY_MID_MFE_HIGH_MAE",7,7,4,medium,canonical_shadow_only,"4B overlay/risk calibration only"
```

## 23. Machine-Readable Rows

### 23.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 23.2 case rows

```jsonl
{"row_type":"case","case_id":"C08_003160_2024_03_06_MEMORY_TESTER_EVENT_RERATING_4B_WATCH","symbol":"003160","company_name":"디아이","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_TEST_SERVICE_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE","case_type":"memory_tester_event_rerating_4B_watch","positive_or_counterexample":"positive","best_trigger":"C08_003160_2024_03_06_STAGE2_ACTIONABLE_MEMORY_TESTER_EVENT_RERATING_4B_WATCH","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"C08 bridge worked but 4B audit needed","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol versus visible C08 loops 100/103/104/109; tradable shard share-count proxy clean for 180D window"}
{"row_type":"case","case_id":"C08_086390_2024_03_06_MEMORY_TESTER_CUSTOMER_REPEAT_DEMAND_RECOVERY","symbol":"086390","company_name":"유니테스트","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_TEST_SERVICE_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE","case_type":"memory_tester_customer_repeat_demand_recovery","positive_or_counterexample":"positive","best_trigger":"C08_086390_2024_03_06_STAGE2_ACTIONABLE_MEMORY_TESTER_CUSTOMER_REPEAT_DEMAND_RECOVERY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"C08 bridge worked but 4B audit needed","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol versus visible C08 loops 100/103/104/109; tradable shard share-count proxy clean for 180D window"}
{"row_type":"case","case_id":"C08_110990_2024_03_06_INSPECTION_EQUIPMENT_EVENT_PREMIUM_4B_DRAWDOWN","symbol":"110990","company_name":"디아이티","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_TEST_SERVICE_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE","case_type":"inspection_equipment_event_premium_4B_drawdown","positive_or_counterexample":"positive","best_trigger":"C08_110990_2024_03_06_STAGE2_ACTIONABLE_INSPECTION_EQUIPMENT_EVENT_PREMIUM_4B_DRAWDOWN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"C08 bridge worked but 4B audit needed","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol versus visible C08 loops 100/103/104/109; tradable shard share-count proxy clean for 180D window"}
{"row_type":"case","case_id":"C08_420770_2024_03_06_SUBSTRATE_INSPECTION_QUALITY_EVENT_FADE","symbol":"420770","company_name":"기가비스","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_TEST_SERVICE_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE","case_type":"substrate_inspection_quality_event_fade","positive_or_counterexample":"counterexample","best_trigger":"C08_420770_2024_03_06_STAGE2_SUBSTRATE_INSPECTION_QUALITY_EVENT_FADE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"C08 label/event premium did not convert into repeat-demand/margin bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol versus visible C08 loops 100/103/104/109; tradable shard share-count proxy clean for 180D window"}
{"row_type":"case","case_id":"C08_089790_2024_03_06_TEST_HANDLER_CUSTOMER_QUALITY_BRIDGE_ABSENT","symbol":"089790","company_name":"제이티","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_TEST_SERVICE_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE","case_type":"test_handler_customer_quality_bridge_absent","positive_or_counterexample":"counterexample","best_trigger":"C08_089790_2024_03_06_STAGE2_TEST_HANDLER_CUSTOMER_QUALITY_BRIDGE_ABSENT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"C08 label/event premium did not convert into repeat-demand/margin bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol versus visible C08 loops 100/103/104/109; tradable shard share-count proxy clean for 180D window"}
{"row_type":"case","case_id":"C08_119830_2024_03_06_SEMICONDUCTOR_TEST_SERVICE_LABEL_WITHOUT_MARGIN_BRIDGE","symbol":"119830","company_name":"아이텍","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_TEST_SERVICE_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE","case_type":"semiconductor_test_service_label_without_margin_bridge","positive_or_counterexample":"counterexample","best_trigger":"C08_119830_2024_03_06_STAGE2_SEMICONDUCTOR_TEST_SERVICE_LABEL_WITHOUT_MARGIN_BRIDGE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"C08 label/event premium did not convert into repeat-demand/margin bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol versus visible C08 loops 100/103/104/109; tradable shard share-count proxy clean for 180D window"}
{"row_type":"case","case_id":"C08_131970_2024_03_06_TEST_SERVICE_CUSTOMER_QUALITY_MID_MFE_HIGH_MAE","symbol":"131970","company_name":"두산테스나","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_TEST_SERVICE_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE","case_type":"test_service_customer_quality_mid_mfe_high_mae","positive_or_counterexample":"counterexample","best_trigger":"C08_131970_2024_03_06_STAGE2_TEST_SERVICE_CUSTOMER_QUALITY_MID_MFE_HIGH_MAE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"C08 label/event premium did not convert into repeat-demand/margin bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C08 symbol versus visible C08 loops 100/103/104/109; tradable shard share-count proxy clean for 180D window"}
```

### 23.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"C08_003160_2024_03_06_STAGE2_ACTIONABLE_MEMORY_TESTER_EVENT_RERATING_4B_WATCH","case_id":"C08_003160_2024_03_06_MEMORY_TESTER_EVENT_RERATING_4B_WATCH","symbol":"003160","company_name":"디아이","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_TEST_SERVICE_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|quality_repair_after_50_row_band","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":12070.0,"evidence_available_at_that_date":"source_proxy_only: memory_tester_route, customer_quality_proxy, relative_strength, order_revenue_bridge_partial; verified URL repair pending; not price-only promotion evidence","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_tester_route","customer_quality_proxy","relative_strength","order_revenue_bridge_partial"],"stage3_evidence_fields":["repeat_demand_bridge_partial","margin_revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["event_crowding","peak_proximity","post_peak_drawdown"],"stage4c_evidence_fields":["not_hard_4c"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv","profile_path":"atlas/symbol_profiles/003/003160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":110.02,"MFE_90D_pct":155.18,"MFE_180D_pct":155.18,"MAE_30D_pct":-23.45,"MAE_90D_pct":-23.45,"MAE_180D_pct":-23.45,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-27","peak_price":30800.0,"drawdown_after_peak_pct":-64.58,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"C08 4B audit required after event rerating","four_b_evidence_type":["valuation_rerating","event_crowding","bridge_quality_check"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_mfe_with_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_003160_2024-03-06_12070","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C08_086390_2024_03_06_STAGE2_ACTIONABLE_MEMORY_TESTER_CUSTOMER_REPEAT_DEMAND_RECOVERY","case_id":"C08_086390_2024_03_06_MEMORY_TESTER_CUSTOMER_REPEAT_DEMAND_RECOVERY","symbol":"086390","company_name":"유니테스트","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_TEST_SERVICE_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|quality_repair_after_50_row_band","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":14050.0,"evidence_available_at_that_date":"source_proxy_only: memory_tester_route, repeat_demand_proxy, margin_bridge_partial, relative_strength; verified URL repair pending; not price-only promotion evidence","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_tester_route","repeat_demand_proxy","margin_bridge_partial","relative_strength"],"stage3_evidence_fields":["repeat_demand_bridge_partial","margin_revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["event_crowding","peak_proximity","post_peak_drawdown"],"stage4c_evidence_fields":["not_hard_4c"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086390/2024.csv","profile_path":"atlas/symbol_profiles/086/086390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.32,"MFE_90D_pct":38.79,"MFE_180D_pct":38.79,"MAE_30D_pct":-2.63,"MAE_90D_pct":-7.19,"MAE_180D_pct":-40.57,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-23","peak_price":19500.0,"drawdown_after_peak_pct":-57.18,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"C08 4B audit required after event rerating","four_b_evidence_type":["valuation_rerating","event_crowding","bridge_quality_check"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_mfe_with_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_086390_2024-03-06_14050","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C08_110990_2024_03_06_STAGE2_ACTIONABLE_INSPECTION_EQUIPMENT_EVENT_PREMIUM_4B_DRAWDOWN","case_id":"C08_110990_2024_03_06_INSPECTION_EQUIPMENT_EVENT_PREMIUM_4B_DRAWDOWN","symbol":"110990","company_name":"디아이티","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_TEST_SERVICE_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|quality_repair_after_50_row_band","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":22600.0,"evidence_available_at_that_date":"source_proxy_only: inspection_equipment_route, AOI_quality_proxy, relative_strength, valuation_event; verified URL repair pending; not price-only promotion evidence","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["inspection_equipment_route","AOI_quality_proxy","relative_strength","valuation_event"],"stage3_evidence_fields":["repeat_demand_bridge_partial","margin_revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["event_crowding","peak_proximity","post_peak_drawdown"],"stage4c_evidence_fields":["not_hard_4c"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/110/110990/2024.csv","profile_path":"atlas/symbol_profiles/110/110990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.95,"MFE_90D_pct":43.14,"MFE_180D_pct":43.14,"MAE_30D_pct":-25.88,"MAE_90D_pct":-25.88,"MAE_180D_pct":-57.08,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-26","peak_price":32350.0,"drawdown_after_peak_pct":-70.02,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"C08 4B audit required after event rerating","four_b_evidence_type":["valuation_rerating","event_crowding","bridge_quality_check"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_mfe_with_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_110990_2024-03-06_22600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C08_420770_2024_03_06_STAGE2_SUBSTRATE_INSPECTION_QUALITY_EVENT_FADE","case_id":"C08_420770_2024_03_06_SUBSTRATE_INSPECTION_QUALITY_EVENT_FADE","symbol":"420770","company_name":"기가비스","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_TEST_SERVICE_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|quality_repair_after_50_row_band","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":62800.0,"evidence_available_at_that_date":"source_proxy_only: substrate_inspection_route, quality_event_premium, repeat_demand_bridge_absent; verified URL repair pending; not price-only promotion evidence","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["substrate_inspection_route","quality_event_premium","repeat_demand_bridge_absent"],"stage3_evidence_fields":["none_confirmed","margin_revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["event_crowding","peak_proximity","post_peak_drawdown"],"stage4c_evidence_fields":["customer_quality_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/420/420770/2024.csv","profile_path":"atlas/symbol_profiles/420/420770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.37,"MFE_90D_pct":31.37,"MFE_180D_pct":31.37,"MAE_30D_pct":-3.66,"MAE_90D_pct":-23.96,"MAE_180D_pct":-62.02,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-09","peak_price":82500.0,"drawdown_after_peak_pct":-71.09,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"C08 4B audit required after event rerating","four_b_evidence_type":["valuation_rerating","event_crowding","bridge_quality_check"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_customer_quality_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_420770_2024-03-06_62800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C08_089790_2024_03_06_STAGE2_TEST_HANDLER_CUSTOMER_QUALITY_BRIDGE_ABSENT","case_id":"C08_089790_2024_03_06_TEST_HANDLER_CUSTOMER_QUALITY_BRIDGE_ABSENT","symbol":"089790","company_name":"제이티","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_TEST_SERVICE_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|quality_repair_after_50_row_band","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":10180.0,"evidence_available_at_that_date":"source_proxy_only: test_handler_route, relative_strength_event, customer_quality_bridge_absent; verified URL repair pending; not price-only promotion evidence","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["test_handler_route","relative_strength_event","customer_quality_bridge_absent"],"stage3_evidence_fields":["none_confirmed","margin_revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["event_crowding","peak_proximity","post_peak_drawdown"],"stage4c_evidence_fields":["customer_quality_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089790/2024.csv","profile_path":"atlas/symbol_profiles/089/089790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.59,"MFE_90D_pct":11.59,"MFE_180D_pct":11.59,"MAE_30D_pct":-10.12,"MAE_90D_pct":-30.84,"MAE_180D_pct":-66.11,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-12","peak_price":11360.0,"drawdown_after_peak_pct":-69.63,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"C08 4B audit required after event rerating","four_b_evidence_type":["valuation_rerating","event_crowding","bridge_quality_check"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_customer_quality_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_089790_2024-03-06_10180","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C08_119830_2024_03_06_STAGE2_SEMICONDUCTOR_TEST_SERVICE_LABEL_WITHOUT_MARGIN_BRIDGE","case_id":"C08_119830_2024_03_06_SEMICONDUCTOR_TEST_SERVICE_LABEL_WITHOUT_MARGIN_BRIDGE","symbol":"119830","company_name":"아이텍","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_TEST_SERVICE_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|quality_repair_after_50_row_band","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":7400.0,"evidence_available_at_that_date":"source_proxy_only: semiconductor_test_service_route, test_outsourcing_label, margin_bridge_absent; verified URL repair pending; not price-only promotion evidence","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["semiconductor_test_service_route","test_outsourcing_label","margin_bridge_absent"],"stage3_evidence_fields":["none_confirmed","margin_revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["event_crowding","peak_proximity","post_peak_drawdown"],"stage4c_evidence_fields":["customer_quality_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/119/119830/2024.csv","profile_path":"atlas/symbol_profiles/119/119830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.14,"MFE_90D_pct":18.24,"MFE_180D_pct":18.24,"MAE_30D_pct":-0.81,"MAE_90D_pct":-7.43,"MAE_180D_pct":-38.78,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-19","peak_price":8750.0,"drawdown_after_peak_pct":-48.23,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"C08 4B audit required after event rerating","four_b_evidence_type":["valuation_rerating","event_crowding","bridge_quality_check"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_customer_quality_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_119830_2024-03-06_7400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C08_131970_2024_03_06_STAGE2_TEST_SERVICE_CUSTOMER_QUALITY_MID_MFE_HIGH_MAE","case_id":"C08_131970_2024_03_06_TEST_SERVICE_CUSTOMER_QUALITY_MID_MFE_HIGH_MAE","symbol":"131970","company_name":"두산테스나","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TEST_SOCKET_TEST_SERVICE_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|quality_repair_after_50_row_band","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":44350.0,"evidence_available_at_that_date":"source_proxy_only: test_service_route, customer_quality_label, revenue_bridge_delayed; verified URL repair pending; not price-only promotion evidence","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["test_service_route","customer_quality_label","revenue_bridge_delayed"],"stage3_evidence_fields":["none_confirmed","margin_revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["event_crowding","peak_proximity","post_peak_drawdown"],"stage4c_evidence_fields":["customer_quality_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131970/2024.csv","profile_path":"atlas/symbol_profiles/131/131970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.18,"MFE_90D_pct":20.18,"MFE_180D_pct":20.18,"MAE_30D_pct":-5.52,"MAE_90D_pct":-19.17,"MAE_180D_pct":-48.48,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-05","peak_price":53300.0,"drawdown_after_peak_pct":-57.13,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"C08 4B audit required after event rerating","four_b_evidence_type":["valuation_rerating","event_crowding","bridge_quality_check"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_customer_quality_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_131970_2024-03-06_44350","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 23.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_003160_2024_03_06_MEMORY_TESTER_EVENT_RERATING_4B_WATCH","trigger_id":"C08_003160_2024_03_06_STAGE2_ACTIONABLE_MEMORY_TESTER_EVENT_RERATING_4B_WATCH","symbol":"003160","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow risk","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable with C08 4B audit","changed_components":["margin_bridge_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 promotion requires customer qualification, repeat demand, revenue/margin bridge, and 4B audit after event crowding.","MFE_90D_pct":155.18,"MAE_90D_pct":-23.45,"score_return_alignment_label":"aligned_but_4B_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_086390_2024_03_06_MEMORY_TESTER_CUSTOMER_REPEAT_DEMAND_RECOVERY","trigger_id":"C08_086390_2024_03_06_STAGE2_ACTIONABLE_MEMORY_TESTER_CUSTOMER_REPEAT_DEMAND_RECOVERY","symbol":"086390","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow risk","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable with C08 4B audit","changed_components":["margin_bridge_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 promotion requires customer qualification, repeat demand, revenue/margin bridge, and 4B audit after event crowding.","MFE_90D_pct":38.79,"MAE_90D_pct":-7.19,"score_return_alignment_label":"aligned_but_4B_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_110990_2024_03_06_INSPECTION_EQUIPMENT_EVENT_PREMIUM_4B_DRAWDOWN","trigger_id":"C08_110990_2024_03_06_STAGE2_ACTIONABLE_INSPECTION_EQUIPMENT_EVENT_PREMIUM_4B_DRAWDOWN","symbol":"110990","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow risk","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable with C08 4B audit","changed_components":["margin_bridge_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 promotion requires customer qualification, repeat demand, revenue/margin bridge, and 4B audit after event crowding.","MFE_90D_pct":43.14,"MAE_90D_pct":-25.88,"score_return_alignment_label":"aligned_but_4B_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_420770_2024_03_06_SUBSTRATE_INSPECTION_QUALITY_EVENT_FADE","trigger_id":"C08_420770_2024_03_06_STAGE2_SUBSTRATE_INSPECTION_QUALITY_EVENT_FADE","symbol":"420770","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":8,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/Stage2-watch, not C08 Yellow","changed_components":["margin_bridge_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 promotion requires customer qualification, repeat demand, revenue/margin bridge, and 4B audit after event crowding.","MFE_90D_pct":31.37,"MAE_90D_pct":-23.96,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_089790_2024_03_06_TEST_HANDLER_CUSTOMER_QUALITY_BRIDGE_ABSENT","trigger_id":"C08_089790_2024_03_06_STAGE2_TEST_HANDLER_CUSTOMER_QUALITY_BRIDGE_ABSENT","symbol":"089790","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/Stage2-watch, not C08 Yellow","changed_components":["margin_bridge_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 promotion requires customer qualification, repeat demand, revenue/margin bridge, and 4B audit after event crowding.","MFE_90D_pct":11.59,"MAE_90D_pct":-30.84,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_119830_2024_03_06_SEMICONDUCTOR_TEST_SERVICE_LABEL_WITHOUT_MARGIN_BRIDGE","trigger_id":"C08_119830_2024_03_06_STAGE2_SEMICONDUCTOR_TEST_SERVICE_LABEL_WITHOUT_MARGIN_BRIDGE","symbol":"119830","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/Stage2-watch, not C08 Yellow","changed_components":["margin_bridge_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 promotion requires customer qualification, repeat demand, revenue/margin bridge, and 4B audit after event crowding.","MFE_90D_pct":18.24,"MAE_90D_pct":-7.43,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_131970_2024_03_06_TEST_SERVICE_CUSTOMER_QUALITY_MID_MFE_HIGH_MAE","trigger_id":"C08_131970_2024_03_06_STAGE2_TEST_SERVICE_CUSTOMER_QUALITY_MID_MFE_HIGH_MAE","symbol":"131970","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":8,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage1/Stage2-watch, not C08 Yellow","changed_components":["margin_bridge_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 promotion requires customer qualification, repeat demand, revenue/margin bridge, and 4B audit after event crowding.","MFE_90D_pct":20.18,"MAE_90D_pct":-19.17,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 23.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"same_archetype_new_symbol_count":7,"same_archetype_new_trigger_family_count":7,"new_trigger_family_count":7,"positive_case_count":3,"counterexample_count":4,"current_profile_error_count":7,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive","C08_repeat_demand_bridge_absent"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 24. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row.

Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{symbol}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{symbol}.json.

### Rules

1. Use only calibration_usable=true rows for quantitative calibration.
2. Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
3. Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
4. Do not apply global deltas unless multiple large_sector_id values support the same direction.
5. Prefer sector_specific or canonical_archetype_specific shadow profiles.
6. Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
7. 4B rows are overlay/risk calibration only.
8. 4C rows are thesis-break/protection calibration only.
9. Price-only rows cannot promote Stage2/Stage3.
10. If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
11. Production scoring must not change unless the user explicitly asks for another promotion batch.

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

## 25. Next Round State

```text
completed_round = R2
completed_loop = 110
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 2 quality_repair_exact_50_after_local_priority0_priority1_fill
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C19_BRAND_RETAIL_INVENTORY_MARGIN, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C22_INSURANCE_RATE_CYCLE_RESERVE, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

The next run should re-read the latest No-Repeat Index and avoid repeating these C08 symbol/trigger/date combinations.

## 26. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/086/086390/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/110/110990/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/420/420770/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/089/089790/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/119/119830/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/131/131970/2024.csv
- Symbol profiles referenced:
  - atlas/symbol_profiles/003/003160.json
  - atlas/symbol_profiles/086/086390.json
  - atlas/symbol_profiles/110/110990.json
  - atlas/symbol_profiles/420/420770.json
  - atlas/symbol_profiles/089/089790.json
  - atlas/symbol_profiles/119/119830.json
  - atlas/symbol_profiles/131/131970.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
