# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R2
scheduled_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_TEST_SOCKET_CHANNEL_FALSE_STAGE2_AND_MEMORY_SOCKET_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R2_loop_96_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
```

This file is the corrected final output for this execution. The scheduler state after R1 loop 96 is R2 / loop 96. R2 is the L2 AI/semiconductor/electronics round, and this run fills C08 semiconductor test/socket customer-quality behavior rather than repeating the immediately preceding R2 loop 95 C10 memory-recovery equipment cycle file or R2 loop 94 C07 HBM-equipment file.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R2
scheduled_loop = 96
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
round_sector_consistency = pass
computed_next_round = R3
computed_next_loop = 96
```

C08 is a customer-quality and test-chain bridge archetype. A test socket, probe card, or memory-recovery label is the test jig; the signal becomes investable only when customer quality, order visibility, reorder durability, ASP/mix, utilization, margin and revision are visible.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY = 21 rows / 11 symbols / good-bad Stage2 9-5 / 4B-4C 2-0
top covered symbols include UNKNOWN_SYMBOL(6), 089030(2), 095340(2), 131290(2), 252990(2), 058470(1)
previous R2 loop-94 C07 symbols avoided: 089030, 253590, 425420
previous R2 loop-95 C10 symbols avoided: 232140, 330860, 200470
previous R1 loop-96 C01 symbols avoided: 082740, 064820, 101170
previous R13 loop-95 review-only rows do_not_count_as_new_case
```

Selected rows avoid hard duplicates and top repeated C08 symbols:

```text
424980 / Stage2-Actionable / 2024-04-02
098120 / Stage2-Actionable / 2024-04-24
080580 / Stage4B / 2024-01-23
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest | atlas/manifest.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |

| symbol | profile path | CA window status |
|---|---|---|
| 424980 | atlas/symbol_profiles/424/424980.json | no corporate-action candidate |
| 098120 | atlas/symbol_profiles/098/098120.json | selected 2024 window clean after old 2011 CA candidates |
| 080580 | atlas/symbol_profiles/080/080580.json | selected 2024 window clean after old 2021 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R2L96_C08_MICRO2NANO_2024_MEMS_PROBE_CARD_CUSTOMER_QUALITY_POSITIVE | 424980 | 2024-04-02 | yes | 180 | yes | yes | true |
| R2L96_C08_MICONSO_2024_TEST_SOCKET_CHANNEL_FALSE_STAGE2 | 098120 | 2024-04-24 | yes | 180 | yes | yes | true |
| R2L96_C08_OKINS_2024_MEMORY_SOCKET_EVENT_CAP_4B | 080580 | 2024-01-23 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE | Positive Stage2 requires customer quality, order visibility, ASP/mix, utilization, margin and revision bridge. |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | TEST_SOCKET_CHANNEL_FALSE_STAGE2 | Test-socket channel watch without customer/order and margin bridge can become false Stage2. |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | MEMORY_SOCKET_EVENT_CAP_4B | Memory-socket event premium should route to 4B when order/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R2L96_C08_MICRO2NANO_2024_MEMS_PROBE_CARD_CUSTOMER_QUALITY_POSITIVE | 424980 | 마이크로투나노 | positive | MEMS probe-card/test-chain bridge produced extreme MFE, while later drawdown requires valuation watch. |
| R2L96_C08_MICONSO_2024_TEST_SOCKET_CHANNEL_FALSE_STAGE2 | 098120 | 마이크로컨텍솔 | counterexample | Test-socket channel rebound had limited MFE without customer/order/margin bridge. |
| R2L96_C08_OKINS_2024_MEMORY_SOCKET_EVENT_CAP_4B | 080580 | 오킨스전자 | counterexample / 4B | Memory-socket event premium capped near the January spike and then suffered deep MAE. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| Micro2Nano MEMS probe-card customer-quality bridge | historical public/report proxy | true | true | shadow-only positive |
| Microcontactsol test-socket channel false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Okins memory-socket event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 424980 | atlas/ohlcv_tradable_by_symbol_year/424/424980/2024.csv | atlas/symbol_profiles/424/424980.json |
| 098120 | atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv | atlas/symbol_profiles/098/098120.json |
| 080580 | atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv | atlas/symbol_profiles/080/080580.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R2L96_C08_MICRO2NANO_2024_STAGE2_ACTIONABLE_MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE | 424980 | Stage2-Actionable | 2024-04-02 | 13780 | positive | MEMS probe-card customer-quality bridge worked, but later 4B watch required |
| R2L96_C08_MICONSO_2024_STAGE2_FALSE_POSITIVE_TEST_SOCKET_CHANNEL_WATCH | 098120 | Stage2-Actionable | 2024-04-24 | 9950 | counterexample | test-socket channel false Stage2 |
| R2L96_C08_OKINS_2024_STAGE4B_MEMORY_SOCKET_EVENT_CAP | 080580 | Stage4B | 2024-01-23 | 13770 | counterexample/4B | memory-socket event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R2L96_C08_MICRO2NANO_2024_STAGE2_ACTIONABLE_MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE | 13780 | 72.35 | -12.77 | 72.35 | -31.06 | 72.35 | -31.06 | 2024-05-03 | 23750 | -60.00 |
| R2L96_C08_MICONSO_2024_STAGE2_FALSE_POSITIVE_TEST_SOCKET_CHANNEL_WATCH | 9950 | 11.86 | -11.16 | 11.86 | -23.62 | 11.86 | -23.62 | 2024-04-29 | 11130 | -31.72 |
| R2L96_C08_OKINS_2024_STAGE4B_MEMORY_SOCKET_EVENT_CAP | 13770 | 8.28 | -27.74 | 8.28 | -52.14 | 8.28 | -52.14 | 2024-01-23 | 14910 | -55.80 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C08 Stage2 needs customer-quality / order visibility / ASP mix / utilization / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing socket/probe-card event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE socket event rows cannot promote without durable customer/order bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether a test-socket/probe-card label becomes customer quality, order visibility and margin.

| symbol | stage quality | explanation |
|---|---|---|
| 424980 | good_stage2_with_later_watch | Customer-quality/probe-card bridge produced extreme MFE, but later drawdown makes 4B valuation watch mandatory. |
| 098120 | bad_stage2 | Test-socket channel watch lacked order/margin bridge and produced limited MFE. |
| 080580 | good_4B | Memory-socket premium capped on the January spike and later suffered deep MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 098120 test-socket false Stage2 | 0.89 | 0.89 | false Stage2 due missing customer/order/ASP/margin bridge |
| 080580 memory-socket cap | 0.92 | 0.92 | good 4B timing after January socket event premium |
| 424980 probe-card bridge | n/a | n/a | positive Stage2, but later probe-card valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 098120 / 080580
```

No hard 4C candidate is introduced in this R2 loop 96 file. The counterexamples are bridge-missing / event-cap rows, not hard thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L2 semi test-socket/probe-card customer-quality cases, Stage2 requires verified customer quality, order visibility, reorder durability, ASP/mix, utilization, margin, or revision bridge. Test socket, probe card, memory recovery, HBM, AI semiconductor or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
rule = C08 should split true customer-quality/order/margin positives from test-socket channel false Stage2 and memory-socket event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 30.83 | -35.61 | 0.67 | mixed; C08 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 30.83 | -35.61 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L2 customer-quality/order/margin bridge required | 2 | 42.11 | -27.34 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C08 bridge vs event-cap split | 2 | 42.11 | -27.34 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing socket themes as positive | 1 | 72.35 | -31.06 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 424980 probe-card bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 72.35 | -31.06 | MEMS_probe_card_customer_quality_positive_with_later_4B_watch |
| 098120 test-socket false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 11.86 | -23.62 | test_socket_channel_false_stage2 |
| 080580 memory-socket cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 8.28 | -52.14 | memory_socket_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_TEST_SOCKET_CHANNEL_FALSE_STAGE2_AND_MEMORY_SOCKET_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C08 Micro2Nano MEMS probe-card customer-quality positive, Microcontactsol test-socket channel false Stage2, and Okins memory-socket event-cap 4B while avoiding top repeated C08 and previous R2/R1 loop symbols."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: MEMS_probe_card_customer_quality_positive, test_socket_channel_false_stage2, memory_socket_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C08 semi test-socket/probe-card customer-quality bridge vs false Stage2 / event-cap split
```

Non-validation scope:

```text
- Exact as-of evidence URLs remain pending for all selected cases.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,configured,C08_requires_customer_quality_order_visibility_ASP_mix_utilization_margin_revision_bridge,0,"C08 Stage2 should require customer quality, order visibility, reorder durability, ASP/mix, utilization, margin, or revision bridge, not test socket/probe-card/memory recovery label alone","Micro2Nano positive worked; Microcontactsol and Okins event/watch rows failed positive-stage promotion","R2L96_C08_MICRO2NANO_2024_STAGE2_ACTIONABLE_MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE|R2L96_C08_MICONSO_2024_STAGE2_FALSE_POSITIVE_TEST_SOCKET_CHANNEL_WATCH|R2L96_C08_OKINS_2024_STAGE4B_MEMORY_SOCKET_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,configured,cap_bridge_missing_test_socket_probe_card_event_premiums_as_4B_watch,0,"Probe-card and test-socket premiums can peak before customer/order/margin bridge is proven","Microcontactsol had limited MFE after socket-channel watch; Okins showed 4B event-cap behavior after the January memory-socket spike","R2L96_C08_MICONSO_2024_STAGE2_FALSE_POSITIVE_TEST_SOCKET_CHANNEL_WATCH|R2L96_C08_OKINS_2024_STAGE4B_MEMORY_SOCKET_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,configured,block_positive_stage_when_socket_theme_has_high_or_persistent_MAE_without_customer_margin_bridge,0,"High or persistent MAE after bridge-missing C08 entries should block Stage2/Stage3 promotion unless customer quality, order and margin evidence survives","Microcontactsol MAE180=-23.62 and Okins MAE90=-52.14","R2L96_C08_MICONSO_2024_STAGE2_FALSE_POSITIVE_TEST_SOCKET_CHANNEL_WATCH|R2L96_C08_OKINS_2024_STAGE4B_MEMORY_SOCKET_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R2L96_C08_MICRO2NANO_2024_MEMS_PROBE_CARD_CUSTOMER_QUALITY_POSITIVE", "symbol": "424980", "company_name": "마이크로투나노", "round": "R2", "loop": "96", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_TEST_SOCKET_CHANNEL_FALSE_STAGE2_AND_MEMORY_SOCKET_EVENT_CAP", "case_type": "structural_success_with_later_probe_card_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R2L96_C08_MICRO2NANO_2024_STAGE2_ACTIONABLE_MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "MEMS probe-card / test-socket customer-quality bridge produced extreme 30D/90D MFE. The later drawdown confirms that C08 can promote only when customer quality, order visibility, ASP/mix, capacity utilization, margin and revision bridge are visible, and must still carry a later 4B valuation watch.", "current_profile_verdict": "current_profile_kept_but_C08_positive_requires_customer_quality_order_visibility_ASP_mix_margin_revision_bridge_not_test_socket_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R2L96_C08_MICONSO_2024_TEST_SOCKET_CHANNEL_FALSE_STAGE2", "symbol": "098120", "company_name": "마이크로컨텍솔", "round": "R2", "loop": "96", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_TEST_SOCKET_CHANNEL_FALSE_STAGE2_AND_MEMORY_SOCKET_EVENT_CAP", "case_type": "failed_rerating_test_socket_channel_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R2L96_C08_MICONSO_2024_STAGE2_FALSE_POSITIVE_TEST_SOCKET_CHANNEL_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Test-socket / memory-channel recovery watch had only limited MFE and then meaningful drawdown. C08 Stage2 should not be awarded without confirmed customer order quality, reorder durability, ASP/mix, utilization, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_test_socket_channel_watch_counts_without_customer_order_ASP_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2011 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R2L96_C08_OKINS_2024_MEMORY_SOCKET_EVENT_CAP_4B", "symbol": "080580", "company_name": "오킨스전자", "round": "R2", "loop": "96", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_TEST_SOCKET_CHANNEL_FALSE_STAGE2_AND_MEMORY_SOCKET_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R2L96_C08_OKINS_2024_STAGE4B_MEMORY_SOCKET_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Memory-socket / test-socket event premium capped near the January spike and then suffered deep 30D/90D/180D MAE. C08 should route bridge-missing socket event premiums to 4B unless customer-quality, order, ASP/mix, utilization, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_memory_socket_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2021 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R2L96_C08_MICRO2NANO_2024_STAGE2_ACTIONABLE_MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE", "case_id": "R2L96_C08_MICRO2NANO_2024_MEMS_PROBE_CARD_CUSTOMER_QUALITY_POSITIVE", "symbol": "424980", "company_name": "마이크로투나노", "round": "R2", "loop": "96", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_TEST_SOCKET_CHANNEL_FALSE_STAGE2_AND_MEMORY_SOCKET_EVENT_CAP", "sector": "MEMS_probe_card_test_socket_customer_quality", "primary_archetype": "customer_quality_order_visibility_ASP_mix_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-02", "entry_date": "2024-04-02", "entry_price": 13780.0, "evidence_available_at_that_date": "MEMS probe-card / test-socket customer-quality and AI/HBM test-supply chain watch with customer order, ASP/mix and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["probe_card_customer_quality_proxy", "test_socket_order_visibility_proxy", "ASP_mix_bridge_proxy", "capacity_utilization_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["extreme_MFE30", "extreme_MFE90", "positive_180D_MFE"], "stage4b_evidence_fields": ["later_probe_card_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/424/424980/2024.csv", "profile_path": "atlas/symbol_profiles/424/424980.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 72.35, "MFE_90D_pct": 72.35, "MFE_180D_pct": 72.35, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -12.77, "MAE_90D_pct": -31.06, "MAE_180D_pct": -31.06, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-03", "peak_price": 23750.0, "drawdown_after_peak_pct": -60.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_probe_card_valuation_4B_watch_needed", "four_b_evidence_type": ["customer_quality_bridge", "probe_card_order_visibility", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_MEMS_probe_card_customer_quality_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R2L96_C08_424980_2024-04-02_13780", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L96_C08_MICONSO_2024_STAGE2_FALSE_POSITIVE_TEST_SOCKET_CHANNEL_WATCH", "case_id": "R2L96_C08_MICONSO_2024_TEST_SOCKET_CHANNEL_FALSE_STAGE2", "symbol": "098120", "company_name": "마이크로컨텍솔", "round": "R2", "loop": "96", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_TEST_SOCKET_CHANNEL_FALSE_STAGE2_AND_MEMORY_SOCKET_EVENT_CAP", "sector": "test_socket_memory_channel_recovery_watch", "primary_archetype": "test_socket_channel_watch_without_order_quality_ASP_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-24", "entry_date": "2024-04-24", "entry_price": 9950.0, "evidence_available_at_that_date": "test-socket / memory-channel recovery watch without confirmed customer order quality, reorder durability, ASP/mix or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["test_socket_channel_watch", "memory_recovery_sympathy", "relative_strength_rebound"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "channel_order_margin_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv", "profile_path": "atlas/symbol_profiles/098/098120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.86, "MFE_90D_pct": 11.86, "MFE_180D_pct": 11.86, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -11.16, "MAE_90D_pct": -23.62, "MAE_180D_pct": -23.62, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-29", "peak_price": 11130.0, "drawdown_after_peak_pct": -31.72, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.89, "four_b_full_window_peak_proximity": 0.89, "four_b_timing_verdict": "test_socket_channel_watch_was_false_stage2_due_missing_customer_order_ASP_margin_revision_bridge", "four_b_evidence_type": ["test_socket_rebound", "bridge_missing", "limited_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_test_socket_channel_watch_without_customer_order_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_test_socket_channel_watch_counts_without_customer_order_ASP_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2011_CA", "same_entry_group_id": "R2L96_C08_098120_2024-04-24_9950", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L96_C08_OKINS_2024_STAGE4B_MEMORY_SOCKET_EVENT_CAP", "case_id": "R2L96_C08_OKINS_2024_MEMORY_SOCKET_EVENT_CAP_4B", "symbol": "080580", "company_name": "오킨스전자", "round": "R2", "loop": "96", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_TEST_SOCKET_CHANNEL_FALSE_STAGE2_AND_MEMORY_SOCKET_EVENT_CAP", "sector": "memory_socket_test_socket_event_premium", "primary_archetype": "memory_socket_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-23", "entry_date": "2024-01-23", "entry_price": 13770.0, "evidence_available_at_that_date": "memory-socket / test-socket event premium after January semiconductor socket spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["memory_socket_event", "test_socket_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "customer_order_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv", "profile_path": "atlas/symbol_profiles/080/080580.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.28, "MFE_90D_pct": 8.28, "MFE_180D_pct": 8.28, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -27.74, "MAE_90D_pct": -52.14, "MAE_180D_pct": -52.14, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-23", "peak_price": 14910.0, "drawdown_after_peak_pct": -55.8, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_full_window_4B_timing_memory_socket_event_cap", "four_b_evidence_type": ["memory_socket_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_memory_socket_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_memory_socket_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2021_CA", "same_entry_group_id": "R2L96_C08_080580_2024-01-23_13770", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L96_C08_MICRO2NANO_2024_MEMS_PROBE_CARD_CUSTOMER_QUALITY_POSITIVE", "trigger_id": "R2L96_C08_MICRO2NANO_2024_STAGE2_ACTIONABLE_MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE", "symbol": "424980", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 60, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 80, "customer_quality_score": 65, "policy_or_regulatory_score": 5, "valuation_repricing_score": 45, "execution_risk_score": 40, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "MEMS_probe_card_customer_quality_positive", "MFE_90D_pct": 72.35, "MAE_90D_pct": -31.06, "score_return_alignment_label": "MEMS_probe_card_customer_quality_positive_with_later_4B_watch", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L96_C08_MICONSO_2024_TEST_SOCKET_CHANNEL_FALSE_STAGE2", "trigger_id": "R2L96_C08_MICONSO_2024_STAGE2_FALSE_POSITIVE_TEST_SOCKET_CHANNEL_WATCH", "symbol": "098120", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "test_socket_channel_false_stage2", "MFE_90D_pct": 11.86, "MAE_90D_pct": -23.62, "score_return_alignment_label": "test_socket_channel_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_test_socket_channel_watch_counts_without_customer_order_ASP_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L96_C08_OKINS_2024_MEMORY_SOCKET_EVENT_CAP_4B", "trigger_id": "R2L96_C08_OKINS_2024_STAGE4B_MEMORY_SOCKET_EVENT_CAP", "symbol": "080580", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "memory_socket_event_cap_4B_guard", "MFE_90D_pct": 8.28, "MAE_90D_pct": -52.14, "score_return_alignment_label": "memory_socket_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_memory_socket_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": "96", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "MEMS_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_TEST_SOCKET_CHANNEL_FALSE_STAGE2_AND_MEMORY_SOCKET_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["MEMS_probe_card_customer_quality_positive", "test_socket_channel_false_stage2", "memory_socket_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C08 rows need explicit customer quality, order visibility, reorder durability, ASP/mix, utilization, margin or revision bridge before positive promotion.
- In C08, extreme MFE with later high drawdown still requires post-peak 4B/valuation watch.
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
10. Add tests that bridge-missing C08 test-socket/probe-card rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 96
next_round = R3
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
