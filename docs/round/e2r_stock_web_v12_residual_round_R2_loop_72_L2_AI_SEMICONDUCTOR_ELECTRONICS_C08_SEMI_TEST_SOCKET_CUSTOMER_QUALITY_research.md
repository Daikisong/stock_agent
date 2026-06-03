# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
scheduled_round: R2
scheduled_loop: 72
completed_round: R2
completed_loop: 72
computed_next_round: R3
computed_next_loop: 72
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: HBM_TEST_SOCKET_PROBE_CUSTOMER_QUALITY_REPEAT_CONSUMABLE_SPLIT
loop_objective:
  - residual_false_positive_mining
  - 4B_non_price_requirement_stress_test
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - coverage_gap_fill
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

## 1. Current Calibrated Profile Assumption

The current profile proxy is `e2r_2_1_stock_web_calibrated`. The already-applied global axes are treated as existing guardrails, not as new proposals: `stage2_actionable_evidence_bonus=+2.0`, `stage3_yellow_total_min=75`, `stage3_green_total_min=87`, `stage3_green_revision_min=55`, `stage3_cross_evidence_green_buffer=+1.5`, `price_only_blowoff_blocks_positive_stage=true`, `full_4b_requires_non_price_evidence=true`, and `hard_4c_thesis_break_routes_to_4c=true`.

The research question is narrower: inside C08, does the score need to distinguish durable test-socket/customer-quality bridges from AI/HBM theme extension where the price route moves first but the customer/repeat-consumable evidence remains thin?

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R2 |
| scheduled_loop | 72 |
| allowed large sector | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| selected canonical | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY |
| fine archetype | HBM_TEST_SOCKET_PROBE_CUSTOMER_QUALITY_REPEAT_CONSUMABLE_SPLIT |
| scope verdict | valid R2/L2 pair |

R2 allows L2 only. C08 is a valid semiconductor/electronics canonical archetype, centered on test sockets, probe/interface boards, customer qualification, repeat consumable demand, and quality lock-in.

## 3. Previous Coverage / Duplicate Avoidance Check

No stock-agent source code was opened. The previous loop state was inferred from the immediately preceding generated research sequence: R13 loop 71 completed, then R1 loop 72 completed. Therefore the next scheduled state is R2 loop 72. The selected case set avoids the just-used R1 power-grid/datacenter names and uses R2/C08 test-socket/probe symbols.

Hard duplicate key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected symbols are treated as new independent C08 samples for this loop:

| symbol | company_name | reuse_reason | independent_evidence_weight |
|---|---:|---|---:|
| 058470 | 리노공업 | null | 1.0 |
| 095340 | ISC | null | 1.0 |
| 131290 | 티에스이 | null | 1.0 |
| 098120 | 마이크로컨텍솔 | null | 1.0 |

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest was checked for this run.

```json
{
  "source": "Songdaiki/stock-web",
  "upstream_source": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Raw/unadjusted OHLC is used. Corporate-action candidate windows are blocked where they overlap the 180D window. For this loop, the selected 2024 trigger windows are outside each symbol's listed corporate-action candidate dates.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D forward window | corporate-action 180D status | calibration_usable |
|---|---:|---:|---|---|---|
| R2L72_C08_058470 | 058470 | 2024-03-12 | available before manifest max_date | clean_180D_window | true |
| R2L72_C08_095340 | 095340 | 2024-03-11 | available before manifest max_date | clean_180D_window | true |
| R2L72_C08_131290 | 131290 | 2024-02-13 | available before manifest max_date | clean_180D_window | true |
| R2L72_C08_098120 | 098120 | 2024-04-03 | available before manifest max_date | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep branch | Compression rule |
|---|---|---|
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | premium test socket customer quality | Promote only when customer qualification, repeat consumable demand, margin/revision support, and non-price RS align. |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | HBM/AI test socket theme extension | Treat price strength as Stage2 watch unless non-price customer or margin bridge is present. |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | probe/interface board catch-up | Allow Yellow if order/earnings visibility is present; avoid Green when spike is customer-proxy only. |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | small-cap socket price-only blowoff | 4B watch only; do not promote Stage3 from price action alone. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_type | entry_date | entry_price | reason selected |
|---|---:|---|---|---|---:|---:|---|
| R2L72_C08_058470 | 058470 | 리노공업 | structural_success | Stage2-Actionable | 2024-03-12 | 241500 | durable socket/customer-quality proxy produced strong MFE with manageable early MAE |
| R2L72_C08_095340 | 095340 | ISC | false_positive_green | Stage2-Actionable | 2024-03-11 | 93700 | AI/HBM socket excitement produced early spike but failed 90D/180D alignment |
| R2L72_C08_131290 | 131290 | 티에스이 | high_mae_success | Stage2-Actionable | 2024-02-13 | 57000 | probe/interface-board rerating worked, but later MAE argues for 4B watch once customer bridge saturates |
| R2L72_C08_098120 | 098120 | 마이크로컨텍솔 | failed_rerating | Stage2-Actionable | 2024-04-03 | 9440 | small-cap socket proxy had theme bounce but weak follow-through and deep drawdown |

## 8. Positive vs Counterexample Balance

| Bucket | Count | Cases |
|---|---:|---|
| positive structural success | 2 | 058470, 131290 |
| counterexample / failed rerating | 2 | 095340, 098120 |
| 4B / local overheat audit | 2 | 095340, 131290 |
| current profile residual errors | 2 | 095340 false-positive risk, 098120 price-only promotion risk |

Minimum conditions passed: positive_case_count >= 1, counterexample_count >= 1, calibration_usable_case_count >= 3, new_independent_case_ratio >= 0.60.

## 9. Evidence Source Map

Evidence descriptions are historical research proxies. They are deliberately written as trigger-date-available evidence categories rather than live recommendations.

| case_id | trigger_date | evidence_available_at_that_date | evidence_source | Stage2 evidence | Stage3 evidence | 4B / 4C evidence |
|---|---:|---|---|---|---|---|
| R2L72_C08_058470 | 2024-03-11 | AI/HPC test socket demand, premium customer quality, strong relative strength | historical disclosure/report/news proxy | customer_or_order_quality; relative_strength; early_revision_signal | confirmed_revision; margin_bridge; financial_visibility; durable_customer_confirmation | valuation_blowoff watch only after May peak |
| R2L72_C08_095340 | 2024-03-08 | HBM/socket theme acceleration with price gap but less durable bridge at trigger | historical report/news proxy | relative_strength; early_revision_signal | limited confirmed_revision; customer bridge not yet durable | price_only_local_peak; valuation_blowoff; revision_slowdown |
| R2L72_C08_131290 | 2024-02-13 | probe/interface board recovery and test-equipment cycle rebound | historical report/news proxy | public_event_or_disclosure; customer_or_order_quality; relative_strength | confirmed_revision; margin_bridge partial | 4B local overheat after Apr 26-May 03 |
| R2L72_C08_098120 | 2024-04-02 | small-cap socket proxy and AI theme spillover | historical news/proxy | relative_strength only; weak customer quality | not enough for Green | price_only_local_peak; thesis watch |

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path | profile corporate action note |
|---:|---|---|---|
| 058470 | atlas/symbol_profiles/058/058470.json | atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv | candidate dates: 2013-06-13, 2013-07-08, 2025-04-25; selected 2024 180D window clean |
| 095340 | atlas/symbol_profiles/095/095340.json | atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv | candidate dates: 2014-12-26, 2023-10-20; selected 2024 180D window clean |
| 131290 | atlas/symbol_profiles/131/131290.json | atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv | candidate dates: 2011-04-05, 2011-04-28; selected 2024 180D window clean |
| 098120 | atlas/symbol_profiles/098/098120.json | atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv | candidate dates: 2011-04-19, 2011-05-17; selected 2024 180D window clean |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | representative? | current_profile_verdict |
|---|---|---|---:|---:|---:|---|---|
| R2L72_C08_058470_T1 | R2L72_C08_058470 | Stage2-Actionable | 2024-03-11 | 2024-03-12 | 241500 | true | current_profile_correct |
| R2L72_C08_095340_T1 | R2L72_C08_095340 | Stage2-Actionable | 2024-03-08 | 2024-03-11 | 93700 | true | current_profile_false_positive |
| R2L72_C08_095340_T2 | R2L72_C08_095340 | 4B-watch | 2024-03-28 | 2024-03-28 | 99400 | false | current_profile_4B_too_late |
| R2L72_C08_131290_T1 | R2L72_C08_131290 | Stage2-Actionable | 2024-02-13 | 2024-02-13 | 57000 | true | current_profile_correct |
| R2L72_C08_131290_T2 | R2L72_C08_131290 | 4B-watch | 2024-04-26 | 2024-04-26 | 79000 | false | current_profile_4B_too_late |
| R2L72_C08_098120_T1 | R2L72_C08_098120 | Stage2-Actionable | 2024-04-02 | 2024-04-03 | 9440 | true | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R2L72_C08_058470_T1 | 2024-03-12 | 241500 | 16.98 | -5.38 | 27.95 | -11.18 | 27.95 | -24.20 | 2024-05-07 | 309000 | -38.30 |
| R2L72_C08_095340_T1 | 2024-03-11 | 93700 | 15.26 | -9.07 | 15.26 | -42.37 | 15.26 | -48.24 | 2024-03-28 | 108000 | -53.70 |
| R2L72_C08_095340_T2 | 2024-03-28 | 99400 | 8.65 | -22.13 | 8.65 | -45.67 | 8.65 | -51.61 | 2024-03-28 | 108000 | -53.70 |
| R2L72_C08_131290_T1 | 2024-02-13 | 57000 | 15.09 | -8.42 | 50.53 | -8.42 | 50.53 | -20.88 | 2024-04-30 | 85800 | -46.27 |
| R2L72_C08_131290_T2 | 2024-04-26 | 79000 | 11.14 | -14.81 | 11.14 | -41.65 | 11.14 | -43.16 | 2024-05-03 | 87800 | -47.49 |
| R2L72_C08_098120_T1 | 2024-04-03 | 9440 | 17.90 | -5.61 | 17.90 | -19.49 | 17.90 | -24.79 | 2024-04-29 | 11130 | -31.72 |

Note: 1Y/2Y fields are not used for weight calibration in this MD. 180D is the required clean window.

## 13. Current Calibrated Profile Stress Test

| case_id | P0 expected behavior | Actual path | Verdict |
|---|---|---|---|
| R2L72_C08_058470 | Stage2-Actionable allowed; Green only after revision/margin confirmation | good 90D MFE with manageable early MAE | current_profile_correct |
| R2L72_C08_095340 | could over-promote if AI/HBM price RS is treated as customer-quality evidence | quick MFE then deep 90D/180D drawdown | current_profile_false_positive |
| R2L72_C08_131290 | Stage2/Yellow allowed; Green should wait for margin bridge | good MFE but later sharp drawdown | current_profile_correct, but needs 4B watch |
| R2L72_C08_098120 | price-only RS should be blocked from Stage3 | theme bounce then failed continuation | current_profile_false_positive if RS is over-weighted |

Answers to required stress questions:

1. Current calibrated profile is directionally correct on durable customer-quality names but can still be too generous when C08 price RS is mistaken for customer qualification.
2. Actual MFE/MAE supports promotion for 058470 and 131290, but not for 095340/098120 without extra bridge evidence.
3. Stage2 bonus is not globally wrong; it needs a C08 customer-quality bridge.
4. Yellow threshold 75 is acceptable if price-only relative strength is capped.
5. Green threshold 87/revision 55 is acceptable; no easing is proposed.
6. Price-only blowoff guard is strengthened.
7. Full 4B non-price requirement is preserved, but C08 price-only local blowoff should still become 4B-watch.
8. Hard 4C routing is not the main residual; this is mostly Stage2/4B overlay calibration.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 actionable entry | Hypothetical Yellow | Hypothetical Green | green_lateness_ratio | Interpretation |
|---|---:|---:|---:|---:|---|
| 058470 | 241500 | 255500 | 274500 | 0.49 | Green somewhat late but acceptable because evidence quality was high |
| 095340 | 93700 | 97800 | not_supported | not_applicable | no confirmed durable Green trigger |
| 131290 | 57000 | 62600 | 79000 | 0.76 | Green would capture late upside and risk near-local peak |
| 098120 | 9440 | not_supported | not_supported | not_applicable | price-only bounce only |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local peak | full window peak | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---:|---:|---|
| R2L72_C08_095340_T2 | price_only; valuation_blowoff; revision_slowdown | 108000 | 108000 | 0.97 | 0.97 | good_watch_timing_but_not_full_4B_without_non_price |
| R2L72_C08_131290_T2 | price_only; positioning_overheat | 87800 | 87800 | 0.73 | 0.73 | good_local_4B_watch_timing |
| R2L72_C08_098120_T1 | price_only | 11130 | 11130 | 0.00 | 0.00 | stage2_price_only_proxy_not_4B_full |

4B conclusion: for C08, local price blowoff should not become full 4B without non-price evidence, but it should cap Stage3 promotion and force a watch overlay.

## 16. 4C Protection Audit

No hard 4C thesis-break trigger is promoted in this loop. The drawdowns in 095340 and 098120 are treated as failed rerating / price-only false-positive paths rather than confirmed contract/cancel/qualification-failure 4C. `four_c_protection_label = thesis_break_watch_only` for the counterexamples.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = C08_customer_quality_bridge_required_before_stage3_promotion
proposal_type = sector_shadow_only
```

Rule candidate: in L2/C08, price RS plus AI/HBM narrative should not be enough for Stage3. Stage2-Actionable can be allowed only when at least one non-price bridge exists: customer qualification, repeat consumable demand, margin bridge, or confirmed revision. Otherwise the row remains Stage2-watch/4B-watch and cannot become Green.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = C08_socket_probe_quality_bridge_and_price_only_cap
```

Compression proposal:

- Premium customer-quality socket names: allow Stage2-Actionable and Yellow with customer/revision/margin bridge.
- Probe/interface-board catch-up: allow Yellow but force 4B-watch if MFE is front-loaded and margin bridge is not yet confirmed.
- Small-cap socket proxy: price-only RS cannot promote Stage3.

## 19. Before / After Backtest Comparison

| profile_id | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | 4 | 27.91 | -20.37 | 0.50 | 0 | 1 | mixed; false positives in price-only C08 proxies |
| P0b_e2r_2_0_baseline_reference | 4 | 27.91 | -20.37 | 0.50 | 1 | 1 | stricter but misses 058470 early |
| P1_sector_specific_candidate_profile | 4 | 39.24 | -9.80 | 0.25 | 0 | 1 | better: keeps durable C08, demotes weak proxy |
| P2_canonical_archetype_candidate_profile | 4 | 39.24 | -9.80 | 0.25 | 0 | 1 | best canonical compression for C08 |
| P3_counterexample_guard_profile | 4 | 39.24 | -9.80 | 0.00 for Green | 0 | 1 | strongest Stage3 safety, but may under-label early Yellow |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R2L72_C08_058470 | 78 | Stage3-Yellow | 81 | Stage3-Yellow | 27.95 | -11.18 | aligned |
| R2L72_C08_095340 | 76 | Stage3-Yellow | 68 | Stage2-watch | 15.26 | -42.37 | improved by demotion |
| R2L72_C08_131290 | 75 | Stage3-Yellow | 75 | Stage3-Yellow + 4B-watch | 50.53 | -8.42 | aligned but needs risk cap |
| R2L72_C08_098120 | 66 | Stage2-Actionable | 59 | Stage1/Stage2-watch | 17.90 | -19.49 | improved by demotion |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | HBM_TEST_SOCKET_PROBE_CUSTOMER_QUALITY_REPEAT_CONSUMABLE_SPLIT | 2 | 2 | 2 | 0 | 4 | 0 | 6 | 4 | 2 | true | true | still needs more non-price 4B evidence and overseas customer qualification cases |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - C08 price-only RS falsely treated as customer-quality evidence
  - C08 local 4B watch too late when theme spike precedes margin bridge
new_axis_proposed:
  - C08_socket_probe_customer_quality_bridge_required_before_stage3_promotion
  - C08_price_only_socket_proxy_demote_to_stage2_watch_or_4B_watch
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Uses `Songdaiki/stock-web` tradable_raw OHLCV rows.
- Uses clean 180D windows.
- Uses representative trigger rows for aggregate metrics.
- Uses shadow-only research proxy score components.

Non-validation scope:

- Does not change production scoring.
- Does not open `stock_agent/src/e2r`.
- Does not perform live candidate discovery.
- Does not use broker/API/trading logic.
- Does not claim exact production score equivalence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_customer_quality_bridge_required_before_stage3_promotion,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"C08 price-only RS caused false-positive risk in ISC and Microcontact Solution","false positive demotion while preserving 058470/TSE positives","R2L72_C08_058470_T1|R2L72_C08_095340_T1|R2L72_C08_131290_T1|R2L72_C08_098120_T1",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C08_price_only_socket_proxy_4B_watch_cap,sector_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"local price spikes in C08 should cap Stage3 before durable evidence appears","improves 4B timing for theme blowoff names","R2L72_C08_095340_T2|R2L72_C08_131290_T2",2,2,1,low,sector_shadow_only,"4B overlay only; not sell signal"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R2L72_C08_058470","symbol":"058470","company_name":"리노공업","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_TEST_SOCKET_PROBE_CUSTOMER_QUALITY_REPEAT_CONSUMABLE_SPLIT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R2L72_C08_058470_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"premium test socket customer-quality bridge"}
{"row_type":"case","case_id":"R2L72_C08_095340","symbol":"095340","company_name":"ISC","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_TEST_SOCKET_PROBE_CUSTOMER_QUALITY_REPEAT_CONSUMABLE_SPLIT","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R2L72_C08_095340_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_without_customer_bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"price/AI socket theme ran ahead of durable bridge"}
{"row_type":"case","case_id":"R2L72_C08_131290","symbol":"131290","company_name":"티에스이","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_TEST_SOCKET_PROBE_CUSTOMER_QUALITY_REPEAT_CONSUMABLE_SPLIT","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R2L72_C08_131290_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_with_4B_watch","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"probe/interface-board recovery worked but required local overheat watch"}
{"row_type":"case","case_id":"R2L72_C08_098120","symbol":"098120","company_name":"마이크로컨텍솔","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_TEST_SOCKET_PROBE_CUSTOMER_QUALITY_REPEAT_CONSUMABLE_SPLIT","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R2L72_C08_098120_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"weak_followthrough","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"small-cap socket proxy lacked durable bridge"}
{"row_type":"trigger","trigger_id":"R2L72_C08_058470_T1","case_id":"R2L72_C08_058470","symbol":"058470","company_name":"리노공업","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_TEST_SOCKET_PROBE_CUSTOMER_QUALITY_REPEAT_CONSUMABLE_SPLIT","sector":"semiconductor_test_socket","primary_archetype":"customer_quality_repeat_consumable","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-11","entry_date":"2024-03-12","entry_price":241500,"evidence_available_at_that_date":"AI/HPC test socket demand plus premium customer-quality bridge","evidence_source":"historical disclosure/report/news proxy","stage2_evidence_fields":["customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv","profile_path":"atlas/symbol_profiles/058/058470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.98,"MFE_90D_pct":27.95,"MFE_180D_pct":27.95,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.38,"MAE_90D_pct":-11.18,"MAE_180D_pct":-24.2,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-07","peak_price":309000,"drawdown_after_peak_pct":-38.3,"green_lateness_ratio":0.49,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L72_C08_058470_2024-03-12_241500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L72_C08_095340_T1","case_id":"R2L72_C08_095340","symbol":"095340","company_name":"ISC","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_TEST_SOCKET_PROBE_CUSTOMER_QUALITY_REPEAT_CONSUMABLE_SPLIT","sector":"semiconductor_test_socket","primary_archetype":"theme_extension_without_bridge","loop_objective":"residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-08","entry_date":"2024-03-11","entry_price":93700,"evidence_available_at_that_date":"AI/HBM socket theme spike without enough durable customer bridge","evidence_source":"historical report/news proxy","stage2_evidence_fields":["relative_strength","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.26,"MFE_90D_pct":15.26,"MFE_180D_pct":15.26,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.07,"MAE_90D_pct":-42.37,"MAE_180D_pct":-48.24,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-28","peak_price":108000,"drawdown_after_peak_pct":-53.7,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_blowoff_not_full_4B","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L72_C08_095340_2024-03-11_93700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L72_C08_095340_T2","case_id":"R2L72_C08_095340","symbol":"095340","company_name":"ISC","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_TEST_SOCKET_PROBE_CUSTOMER_QUALITY_REPEAT_CONSUMABLE_SPLIT","sector":"semiconductor_test_socket","primary_archetype":"theme_extension_without_bridge","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B-watch","trigger_date":"2024-03-28","entry_date":"2024-03-28","entry_price":99400,"evidence_available_at_that_date":"local peak and valuation blowoff but insufficient non-price 4B evidence","evidence_source":"stock-web price path plus historical proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.65,"MFE_90D_pct":8.65,"MFE_180D_pct":8.65,"MAE_30D_pct":-22.13,"MAE_90D_pct":-45.67,"MAE_180D_pct":-51.61,"peak_date":"2024-03-28","peak_price":108000,"drawdown_after_peak_pct":-53.7,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":0.97,"four_b_timing_verdict":"good_watch_timing_but_not_full_4B_without_non_price","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_too_early_if_full","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L72_C08_095340_2024-03-28_99400","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L72_C08_131290_T1","case_id":"R2L72_C08_131290","symbol":"131290","company_name":"티에스이","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_TEST_SOCKET_PROBE_CUSTOMER_QUALITY_REPEAT_CONSUMABLE_SPLIT","sector":"semiconductor_probe_interface","primary_archetype":"probe_board_cycle_recovery","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":57000,"evidence_available_at_that_date":"probe/interface-board recovery and test cycle rebound","evidence_source":"historical report/news proxy","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.09,"MFE_90D_pct":50.53,"MFE_180D_pct":50.53,"MAE_30D_pct":-8.42,"MAE_90D_pct":-8.42,"MAE_180D_pct":-20.88,"peak_date":"2024-04-30","peak_price":85800,"drawdown_after_peak_pct":-46.27,"green_lateness_ratio":0.76,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L72_C08_131290_2024-02-13_57000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L72_C08_131290_T2","case_id":"R2L72_C08_131290","symbol":"131290","company_name":"티에스이","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_TEST_SOCKET_PROBE_CUSTOMER_QUALITY_REPEAT_CONSUMABLE_SPLIT","trigger_type":"4B-watch","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":79000,"evidence_available_at_that_date":"local overheat after probe-board rerating","evidence_source":"stock-web price path plus historical proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.14,"MFE_90D_pct":11.14,"MFE_180D_pct":11.14,"MAE_30D_pct":-14.81,"MAE_90D_pct":-41.65,"MAE_180D_pct":-43.16,"peak_date":"2024-05-03","peak_price":87800,"drawdown_after_peak_pct":-47.49,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.73,"four_b_full_window_peak_proximity":0.73,"four_b_timing_verdict":"good_local_4B_watch_timing","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L72_C08_131290_2024-04-26_79000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L72_C08_098120_T1","case_id":"R2L72_C08_098120","symbol":"098120","company_name":"마이크로컨텍솔","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_TEST_SOCKET_PROBE_CUSTOMER_QUALITY_REPEAT_CONSUMABLE_SPLIT","sector":"semiconductor_socket_smallcap_proxy","primary_archetype":"price_only_proxy","loop_objective":"residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-02","entry_date":"2024-04-03","entry_price":9440,"evidence_available_at_that_date":"small-cap socket proxy and AI theme spillover","evidence_source":"historical news/proxy","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv","profile_path":"atlas/symbol_profiles/098/098120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.9,"MFE_90D_pct":17.9,"MFE_180D_pct":17.9,"MAE_30D_pct":-5.61,"MAE_90D_pct":-19.49,"MAE_180D_pct":-24.79,"peak_date":"2024-04-29","peak_price":11130,"drawdown_after_peak_pct":-31.72,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"price_only_proxy_not_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L72_C08_098120_2024-04-03_9440","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L72_C08_058470","trigger_id":"R2L72_C08_058470_T1","symbol":"058470","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":15,"revision_score":16,"relative_strength_score":15,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":16,"revision_score":16,"relative_strength_score":14,"customer_quality_score":19,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score"],"component_delta_explanation":"durable customer-quality evidence improves C08 confidence","MFE_90D_pct":27.95,"MAE_90D_pct":-11.18,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L72_C08_095340","trigger_id":"R2L72_C08_095340_T1","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":8,"revision_score":12,"relative_strength_score":20,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":14,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":6,"revision_score":9,"relative_strength_score":14,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-watch","changed_components":["customer_quality_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"price RS is capped when customer-quality bridge is weak","MFE_90D_pct":15.26,"MAE_90D_pct":-42.37,"score_return_alignment_label":"improved_by_demotion","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L72_C08_131290","trigger_id":"R2L72_C08_131290_T1","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":11,"revision_score":14,"relative_strength_score":17,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":11,"revision_score":14,"relative_strength_score":15,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":75,"stage_label_after":"Stage3-Yellow+4B-watch","changed_components":["relative_strength_score","execution_risk_score"],"component_delta_explanation":"valid recovery but local overheat watch caps Green promotion","MFE_90D_pct":50.53,"MAE_90D_pct":-8.42,"score_return_alignment_label":"aligned_with_risk_cap","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L72_C08_098120","trigger_id":"R2L72_C08_098120_T1","symbol":"098120","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":16,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":10,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":59,"stage_label_after":"Stage1/Stage2-watch","changed_components":["relative_strength_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"small-cap price proxy lacks durable customer bridge","MFE_90D_pct":17.9,"MAE_90D_pct":-19.49,"score_return_alignment_label":"improved_by_demotion","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["price_only_RS_as_customer_quality_false_positive","late_local_4B_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 72
next_round = R3
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- `atlas/manifest.json` confirmed stock-web max_date `2026-02-20`, price basis `tradable_raw`, and adjustment status `raw_unadjusted_marcap`.
- `atlas/symbol_profiles/058/058470.json`, `095/095340.json`, `131/131290.json`, and `098/098120.json` were checked for available years, profile status, and corporate-action candidate dates.
- `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/2024.csv` rows were used for entry/peak/drawdown calculations.
- This MD is historical calibration research only and does not recommend trading any security.

