# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R13
loop = 12
loop_name = cross_archetype_holdout_3
output_file = e2r_stock_web_v12_residual_round_R13_loop_12_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
live_candidate_mode = false
current_stock_discovery_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This standalone Markdown file is a historical calibration holdout file, not a live candidate report. It uses `Songdaiki/stock-web` OHLC rows as the price atlas and tests whether the post-calibrated global E2R profile still needs a C07-specific gate for HBM equipment/order-led rerating.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference

existing applied axes tested:
- stage2_actionable_evidence_bonus = +2.0
- stage3_yellow_total_min = 75.0
- stage3_green_total_min = 87.0
- stage3_green_revision_min = 55.0
- stage3_cross_evidence_green_buffer = +1.5
- price_only_blowoff_blocks_positive_stage = true
- full_4b_requires_non_price_evidence = true
- hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-propose the global calibration. It asks a narrower question: in HBM equipment, does relative strength represent real order conversion, or is it just a mirror reflecting AI-theme heat? The residual answer is that **customer-named order/backlog or revision bridge** is the hinge.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R13
loop = 12
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id = HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_HOLDOUT
loop_objective =
  - holdout_validation
  - residual_false_positive_mining
  - residual_missed_structural_mining
  - 4B_non_price_requirement_stress_test
  - counterexample_mining
  - coverage_gap_fill
```

### Research question

Can the existing calibrated profile separate true HBM equipment order rerating from adjacent semiconductor quality/AI narrative rerating? The holdout result is mixed: Stage2-Actionable works well for true equipment order routes, but Green remains too blunt unless C07 requires an explicit order/backlog/revision bridge.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts were used only for coverage and duplicate avoidance.

```text
ingest_summary_observed:
- discovered_md_count = 398
- discovered_result_md_count = 107
- raw_trigger_rows = 4951
- validated_trigger_rows = 1940
- aggregate_representative_trigger_rows = 1376
- rounds_covered = R1~R13
- loops_covered = 1~9

applied_global_axes_observed:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- stage3_green_revision_min
- stage3_cross_evidence_green_buffer
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

duplicate_avoidance:
- 4 of 5 calibration-usable cases are new independent holdout cases for this MD.
- 1 case is reused as a holdout anchor and does not count as a new independent case.
- new_independent_case_ratio = 0.80
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Stock-web manifest fields inspected:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | entry window | forward 180D available | 180D corporate-action overlap | calibration_usable |
|---|---:|---|---|---:|---:|---:|
| R13L12_C07_HANMI_042700 | 042700 | atlas/symbol_profiles/042/042700.json | 2024-02-08 onward | true | false | true |
| R13L12_C07_TECHWING_089030 | 089030 | atlas/symbol_profiles/089/089030.json | 2024-01-19 onward | true | false | true |
| R13L12_C07_EOTECH_039030 | 039030 | atlas/symbol_profiles/039/039030.json | 2024-01-19 onward | true | false | true |
| R13L12_C07_ISC_095340 | 095340 | atlas/symbol_profiles/095/095340.json | 2024-03-08 onward | true | false | true |
| R13L12_C07_LEENO_058470 | 058470 | atlas/symbol_profiles/058/058470.json | 2024-03-11 onward | true | false | true |

## 6. Canonical Archetype Compression Map

```text
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id = HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_HOLDOUT

compressed fine signals:
- HBM_TCBONDER_ORDER_ROUTE -> C07
- HBM_INSPECTION_PROBER_ORDER_ROUTE -> C07
- ADVANCED_PACKAGING_LASER_OPTIONALITY -> C07 boundary / Yellow only unless order bridge exists
- TEST_SOCKET_CUSTOMER_QUALITY_ONLY -> C08/C07 boundary, not C07 Green by itself
```

The archetype should not reward every “AI semiconductor” label equally. In C07, relative strength is like smoke: sometimes it comes from a furnace of real orders, sometimes from fog machines around a theme. The scoring gate must inspect the fuel.

## 7. Case Selection Summary

| case_id | symbol | company | role | new? | best trigger | current profile verdict |
|---|---:|---|---|---:|---|---|
| R13L12_C07_HANMI_042700 | 042700 | 한미반도체 | structural_success | reused holdout | Stage2-Actionable | current_profile_too_late |
| R13L12_C07_TECHWING_089030 | 089030 | 테크윙 | structural_success | true | Stage2-Actionable | current_profile_missed_structural |
| R13L12_C07_EOTECH_039030 | 039030 | 이오테크닉스 | high_mae_success / Yellow | true | Stage3-Yellow | current_profile_correct |
| R13L12_C07_ISC_095340 | 095340 | ISC | false_positive_green | true | counterexample | current_profile_false_positive |
| R13L12_C07_LEENO_058470 | 058470 | 리노공업 | failed_rerating / Yellow-only | true | counterexample | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 2
4B_case_count = 3
4C_case_count = 2
minimum_calibration_usable_case_count = 3
calibration_usable_case_count = 5
```

Positive cases had a concrete equipment/order route or at least a strong shipment/revision bridge. Counterexamples had premium quality or AI-adjacent narrative, but lacked a fresh HBM order/backlog bridge.

## 9. Evidence Source Map

| evidence family | Stage2 use | Stage3 use | 4B/4C use | C07 interpretation |
|---|---|---|---|---|
| Relative strength | useful early filter | insufficient alone | can become overheat flag | never enough for Green |
| Named HBM equipment/order route | high value | unlocks Green when paired with revision | watch for saturation | central positive evidence |
| Customer quality | useful | insufficient unless order converts | weak protection | boundary evidence |
| Revision / margin bridge | Stage2 enhancer | Green gate | slowdown triggers 4B | required for durable rerating |
| Price-only spike | no positive promotion | no Green | overlay only | strengthens existing price-only guard |

## 10. Price Data Source Map

| symbol | shard(s) used | profile | corporate-action caveat |
|---:|---|---|---|
| 042700 | atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv | atlas/symbol_profiles/042/042700.json | prior corporate-action dates outside 2024 180D window |
| 089030 | atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv | atlas/symbol_profiles/089/089030.json | prior 2022 dates outside selected window |
| 039030 | atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv | atlas/symbol_profiles/039/039030.json | no 2024 overlap |
| 095340 | atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv | atlas/symbol_profiles/095/095340.json | 2023 corporate-action candidate outside selected 2024 window |
| 058470 | atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv | atlas/symbol_profiles/058/058470.json | 2025 corporate-action candidate outside selected 180D window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | role | current verdict | aggregate role |
|---|---:|---|---|---|---:|---|---|---|
| R13L12_T001_042700_STAGE2 | 042700 | Stage2-Actionable | 2024-02-08 | 2024-02-08 | 78500 | structural_success | current_profile_too_late | representative |
| R13L12_T002_042700_GREEN_LATE | 042700 | Stage3-Green | 2024-03-28 | 2024-03-28 | 134000 | label comparison | current_profile_too_late | label_comparison_only |
| R13L12_T003_042700_4B | 042700 | 4B-watch | 2024-06-13 | 2024-06-13 | 189000 | 4B overlay | current_profile_correct | 4B_overlay_only |
| R13L12_T004_089030_STAGE2 | 089030 | Stage2-Actionable | 2024-01-19 | 2024-01-19 | 14600 | structural_success | current_profile_missed_structural | representative |
| R13L12_T005_089030_GREEN_LATE | 089030 | Stage3-Yellow/Green | 2024-03-27 | 2024-03-27 | 35200 | label comparison | current_profile_too_late | label_comparison_only |
| R13L12_T006_039030_YELLOW | 039030 | Stage3-Yellow | 2024-01-19 | 2024-01-19 | 183900 | Yellow positive | current_profile_correct | representative |
| R13L12_T007_095340_COUNTER | 095340 | False-Green counterexample | 2024-03-08 | 2024-03-08 | 95000 | counterexample | current_profile_false_positive | representative |
| R13L12_T008_058470_COUNTER | 058470 | Stage2/Yellow counterexample | 2024-03-11 | 2024-03-11 | 242500 | counterexample | current_profile_false_positive | representative |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R13L12_T001_042700_STAGE2 | 78500 | 37.3 | -9.9 | 95.2 | -9.9 | 150.0 | -9.9 | 2024-06-14 | 196200 | -39.8 |
| R13L12_T002_042700_GREEN_LATE | 134000 | 14.3 | -6.6 | 46.4 | -9.1 | 46.4 | -20.3 | 2024-06-14 | 196200 | -39.8 |
| R13L12_T003_042700_4B | 189000 | 3.8 | -23.8 | 3.8 | -39.8 | 3.8 | -39.8 | 2024-06-14 | 196200 | -39.8 |
| R13L12_T004_089030_STAGE2 | 14600 | 56.8 | -11.7 | 209.6 | -11.7 | 384.9 | -11.7 | 2024-07-11 | 70800 | -31.5 |
| R13L12_T005_089030_GREEN_LATE | 35200 | 11.1 | -11.6 | 82.7 | -11.6 | 101.1 | -11.6 | 2024-07-11 | 70800 | -31.5 |
| R13L12_T006_039030_YELLOW | 183900 | 16.6 | -11.1 | 52.8 | -11.1 | 52.8 | -14.0 | 2024-04-12 | 281000 | -43.7 |
| R13L12_T007_095340_COUNTER | 95000 | 13.7 | -9.3 | 13.7 | -29.6 | 13.7 | -48.4 | 2024-03-28 | 108000 | -54.6 |
| R13L12_T008_058470_COUNTER | 242500 | 16.5 | -0.8 | 27.4 | -17.0 | 27.4 | -20.3 | 2024-05-07 | 309000 | -37.4 |

## 13. Current Calibrated Profile Stress Test

| case_id | expected current-profile behavior | actual price-path alignment | verdict |
|---|---|---|---|
| R13L12_C07_HANMI_042700 | Stage2/Yellow early, Green after revision | early Stage2 captured much more upside than Green | current_profile_too_late |
| R13L12_C07_TECHWING_089030 | may wait for explicit revision confirmation | early Stage2 had extremely strong forward MFE | current_profile_missed_structural |
| R13L12_C07_EOTECH_039030 | Yellow not Green | moderate MFE with high drawdown risk | current_profile_correct |
| R13L12_C07_ISC_095340 | possible false Yellow/Green risk from quality + relative strength | low MFE and large MAE | current_profile_false_positive |
| R13L12_C07_LEENO_058470 | possible overpromotion from quality + relative strength | moderate MFE but large drawdown and no order bridge | current_profile_false_positive |

Stress-test answers:

```text
1. Current profile is broadly directionally correct but too late for real HBM equipment order winners.
2. MFE/MAE confirms Stage2-Actionable was economically meaningful in Hanmi/Techwing.
3. Stage2 bonus is not too high for true C07 order routes; it is too generous for quality-only adjacent names.
4. Yellow threshold 75 is appropriate for EO Technics-like boundary names.
5. Green threshold 87 and revision 55 are appropriate, but C07 should add order/backlog bridge before Green.
6. price-only blowoff guard is appropriate and should be strengthened in C07.
7. full 4B non-price requirement is appropriate; C07 full 4B should require valuation/positioning plus delivery/revision slowdown.
8. hard 4C routing is kept; no immediate global 4C change proposed.
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green/Yellow entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| Hanmi | 78500 | 134000 | 0.472 | Green captured confirmation but gave up almost half of Stage2-to-peak distance |
| Techwing | 14600 | 35200 | 0.366 | Green/Yellow was late but still had upside; Stage2 mattered most |
| EO Technics | n/a | 183900 | not_applicable | Yellow boundary; no confirmed C07 Green |
| ISC | n/a | 95000 | not_applicable | should not be Green |
| Leeno | n/a | 242500 | not_applicable | should remain quality watch / Yellow boundary |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---|---|
| R13L12_T003_042700_4B | 0.94 | 0.94 | valuation_blowoff / positioning_overheat | good_full_window_4B_timing |
| R13L12_T007_095340_COUNTER | 0.75 | 0.75 | price_only / valuation_blowoff | price_only_local_4B_too_early_without_order_slowdown |
| R13L12_T008_058470_COUNTER | 0.72 | 0.72 | price_only / valuation_blowoff | price_only_local_4B_too_early_without_revision_slowdown |

C07 4B should not fire just because a chart is near a local peak. Full 4B needs heat plus a crack in the machine: delivery delay, revision slowdown, margin disappointment, or customer/order weakness.

## 16. 4C Protection Audit

| case_id | 4C label | protection interpretation |
|---|---|---|
| R13L12_C07_HANMI_042700 | thesis_break_watch_only | no hard 4C; overheat was 4B overlay, not thesis break |
| R13L12_C07_TECHWING_089030 | thesis_break_watch_only | no hard 4C in selected window |
| R13L12_C07_EOTECH_039030 | thesis_break_watch_only | drawdown after optionality spike should be monitored, not hard 4C |
| R13L12_C07_ISC_095340 | false_break / thesis_break_watch_only | lack of order conversion is a guardrail, not automatic 4C without explicit negative evidence |
| R13L12_C07_LEENO_058470 | thesis_break_watch_only | premium quality did not break; it simply did not qualify for C07 Green |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
candidate_axis = hbm_equipment_order_bridge_over_quality_only
proposal_type = sector_shadow_only
confidence = medium
```

For L2, relative strength should be promoted differently depending on whether the company sells into a **constrained HBM equipment lane** or merely sits in the broad semiconductor quality halo.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
new_axis_proposed:
- c07_customer_named_order_or_backlog_bridge_required
- c07_relative_strength_without_order_cap
- c07_full_4b_requires_delivery_or_revision_slowdown
```

C07 Green should require at least two of the following before promotion:

```text
- named or strongly inferable HBM equipment/customer route
- backlog/order/shipment bridge
- confirmed revision or margin bridge
- relative strength before full consensus recognition
```

Quality-only names may still be Stage2 or Stage3-Yellow, but they should not borrow the full C07 Green multiple unless order conversion appears.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global current | 5 | 79.7 | -15.9 | 125.8 | -20.8 | 0.40 | 1 | 2 | useful but blunt for C07 |
| P0b e2r_2_0_baseline_reference | old baseline | 5 | 58.1 | -17.6 | 89.0 | -24.0 | 0.50 | 2 | 2 | worse early capture and more false positives |
| P1 sector_specific_candidate_profile | L2 sector shadow | 5 | 82.4 | -14.8 | 128.3 | -19.5 | 0.30 | 1 | 1 | improves by capping quality-only names |
| P2 canonical_archetype_candidate_profile | C07 shadow | 5 | 91.7 | -13.4 | 144.1 | -17.8 | 0.20 | 0 | 1 | best explanatory alignment |
| P3 counterexample_guard_profile | C07 guard | 5 | 73.5 | -12.9 | 107.0 | -16.2 | 0.10 | 1 | 1 | safer but may under-promote Techwing-like early cases |

## 20. Score-Return Alignment Matrix

| case_id | weighted_before | stage_before | weighted_after | stage_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R13L12_C07_HANMI_042700 | 82.0 | Stage3-Yellow/Stage2-Actionable | 87.5 | Stage3-Green candidate after gate | 95.2 | -9.9 | strong_positive_alignment |
| R13L12_C07_TECHWING_089030 | 74.0 | Stage2-Actionable | 80.5 | Stage3-Yellow / early C07 candidate | 209.6 | -11.7 | very_strong_positive_alignment |
| R13L12_C07_EOTECH_039030 | 76.0 | Stage3-Yellow | 77.5 | Stage3-Yellow kept | 52.8 | -11.1 | moderate_positive_alignment |
| R13L12_C07_ISC_095340 | 73.0 | Stage2/false Yellow risk | 61.0 | Stage1 / no promotion | 13.7 | -29.6 | counterexample_alignment |
| R13L12_C07_LEENO_058470 | 74.0 | Stage2/Yellow watch | 68.0 | Stage2 watch / no Green | 27.4 | -17.0 | weak_to_moderate_alignment |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_HOLDOUT | 3 | 2 | 3 | 2 | 4 | 1 | 8 | 5 | 4 | true | true | reduced; next gap is cross-sector promotion review rather than more C07 schema rows |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 1
reused_case_ids: [R13L12_C07_HANMI_042700]
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - current_profile_missed_structural
  - current_profile_too_late
  - current_profile_false_positive
  - price_only_local_4B_too_early
new_axis_proposed:
  - c07_customer_named_order_or_backlog_bridge_required
  - c07_relative_strength_without_order_cap
  - c07_full_4b_requires_delivery_or_revision_slowdown
existing_axis_strengthened:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: holdout_validation_passed
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema source fields
- symbol profile availability and corporate-action window status
- selected trigger entry dates and entry prices from stock-web tradable shards
- 30D/90D/180D MFE/MAE proxy calculations
- C07-specific residual error classification
```

Not validated:

```text
- no live/current candidate scan
- no broker/API usage
- no stock_agent code access or patching
- no production score mutation
- no investment recommendation
- no post-2026-02-20 price fabrication
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c07_customer_named_order_or_backlog_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"Positive cases had HBM equipment/order route or relative-strength plus customer route; counterexamples had quality/narrative without explicit order/backlog conversion.","Reduced false_positive_green while preserving Hanmi/Techwing early promotion.",R13L12_T001_042700_STAGE2|R13L12_T004_089030_STAGE2|R13L12_T007_095340_COUNTER|R13L12_T008_058470_COUNTER,5,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c07_relative_strength_without_order_cap,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"Relative strength alone confused ISC/Leeno with true HBM equipment winners; require non-price order/revision bridge for Green.","Blocks price/quality-only false positives and keeps them at Stage2/Yellow watch.",R13L12_T006_039030_YELLOW|R13L12_T007_095340_COUNTER|R13L12_T008_058470_COUNTER,3,3,2,medium,guard_shadow_only,"not production; strengthens price_only_blowoff_blocks_positive_stage"
shadow_weight,c07_full_4b_requires_delivery_or_revision_slowdown,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"Full 4B is best when valuation/positioning overheat coincides with delivery/revision slowdown; price-only local peaks are overlay-only.","Improves 4B timing on Hanmi while avoiding premature full exit labels on ISC/Leeno.",R13L12_T003_042700_4B|R13L12_T007_095340_COUNTER|R13L12_T008_058470_COUNTER,3,2,2,low,overlay_shadow_only,"not production; reinforces full_4b_requires_non_price_evidence"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "round": "R13", "loop": "12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_HOLDOUT", "price_source": "Songdaiki/stock-web", "case_id": "R13L12_C07_HANMI_042700", "symbol": "042700", "company_name": "한미반도체", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R13L12_T001_042700_STAGE2", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "holdout_validation_from_prior_R2_HBM_equipment_axis", "independent_evidence_weight": 0.5, "score_price_alignment": "named/visible HBM equipment order route plus relative strength aligned with large MFE, but Green confirmation was materially later than Stage2", "current_profile_verdict": "current_profile_too_late", "notes": "Reused as holdout anchor; does not count as new independent evidence."}
{"row_type": "case", "round": "R13", "loop": "12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_HOLDOUT", "price_source": "Songdaiki/stock-web", "case_id": "R13L12_C07_TECHWING_089030", "symbol": "089030", "company_name": "테크윙", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R13L12_T004_089030_STAGE2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "relative strength plus HBM inspection/prober order route captured a large forward MFE before full confirmation", "current_profile_verdict": "current_profile_missed_structural", "notes": "New independent holdout: shows early Stage2-Actionable needs customer/order quality uplift before revision print."}
{"row_type": "case", "round": "R13", "loop": "12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_HOLDOUT", "price_source": "Songdaiki/stock-web", "case_id": "R13L12_C07_EOTECH_039030", "symbol": "039030", "company_name": "이오테크닉스", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R13L12_T006_039030_YELLOW", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "laser/advanced packaging narrative produced usable MFE but required Yellow rather than full Green due order specificity gap", "current_profile_verdict": "current_profile_correct", "notes": "New boundary positive: supports Yellow, not automatic C07 Green."}
{"row_type": "case", "round": "R13", "loop": "12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_HOLDOUT", "price_source": "Songdaiki/stock-web", "case_id": "R13L12_C07_ISC_095340", "symbol": "095340", "company_name": "ISC", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R13L12_T007_095340_COUNTER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "socket/customer-quality narrative without fresh order/revision bridge had small MFE and severe MAE", "current_profile_verdict": "current_profile_false_positive", "notes": "New counterexample: customer quality alone should not unlock C07 Green."}
{"row_type": "case", "round": "R13", "loop": "12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_HOLDOUT", "price_source": "Songdaiki/stock-web", "case_id": "R13L12_C07_LEENO_058470", "symbol": "058470", "company_name": "리노공업", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R13L12_T008_058470_COUNTER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "premium test-socket quality had moderate MFE but high MAE and no explicit HBM equipment/backlog bridge", "current_profile_verdict": "current_profile_false_positive", "notes": "New counterexample: durable quality should be Stage2/Yellow watch unless order conversion is visible."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R13L12_T001_042700_STAGE2", "case_id": "R13L12_C07_HANMI_042700", "symbol": "042700", "company_name": "한미반도체", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-08", "entry_date": "2024-02-08", "entry_price": 78500, "evidence_available_at_that_date": "HBM TC-bonder/order route and relative strength proxy visible by trigger date; no later-outcome relabeling", "evidence_source": "historical public disclosure/report narrative proxy; stock-web OHLC row validation", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv", "profile_path": "atlas/symbol_profiles/042/042700.json", "MFE_30D_pct": 37.3, "MFE_90D_pct": 95.2, "MFE_180D_pct": 150.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.9, "MAE_90D_pct": -9.9, "MAE_180D_pct": -9.9, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 196200, "drawdown_after_peak_pct": -39.8, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "same_entry_group_id": "R13L12_C07_HANMI_042700_2024-02-08_78500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": false, "reuse_reason": "holdout_validation_from_prior_R2_HBM_equipment_axis", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true, "round": "R13", "loop": "12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_HOLDOUT", "sector": "Cross-archetype RedTeam holdout / AI semiconductor equipment", "primary_archetype": "hbm_equipment_order_relative_strength_vs_customer_quality_only", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window"}
{"row_type": "trigger", "trigger_id": "R13L12_T002_042700_GREEN_LATE", "case_id": "R13L12_C07_HANMI_042700", "symbol": "042700", "company_name": "한미반도체", "trigger_type": "Stage3-Green", "trigger_date": "2024-03-28", "entry_date": "2024-03-28", "entry_price": 134000, "evidence_available_at_that_date": "stronger confirmation/revision proxy visible after the move had already repriced materially", "evidence_source": "historical public disclosure/report narrative proxy; stock-web OHLC row validation", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv", "profile_path": "atlas/symbol_profiles/042/042700.json", "MFE_30D_pct": 14.3, "MFE_90D_pct": 46.4, "MFE_180D_pct": 46.4, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.6, "MAE_90D_pct": -9.1, "MAE_180D_pct": -20.3, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 196200, "drawdown_after_peak_pct": -39.8, "green_lateness_ratio": 0.472, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_success_but_not_early_entry", "current_profile_verdict": "current_profile_too_late", "same_entry_group_id": "R13L12_C07_HANMI_042700_2024-03-28_134000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "holdout_validation_from_prior_R2_HBM_equipment_axis", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true, "round": "R13", "loop": "12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_HOLDOUT", "sector": "Cross-archetype RedTeam holdout / AI semiconductor equipment", "primary_archetype": "hbm_equipment_order_relative_strength_vs_customer_quality_only", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window"}
{"row_type": "trigger", "trigger_id": "R13L12_T003_042700_4B", "case_id": "R13L12_C07_HANMI_042700", "symbol": "042700", "company_name": "한미반도체", "trigger_type": "4B-watch", "trigger_date": "2024-06-13", "entry_date": "2024-06-13", "entry_price": 189000, "evidence_available_at_that_date": "valuation/positioning overheat plus vertical HBM equipment repricing; used as overlay only", "evidence_source": "historical public market/valuation narrative proxy; stock-web OHLC row validation", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv", "profile_path": "atlas/symbol_profiles/042/042700.json", "MFE_30D_pct": 3.8, "MFE_90D_pct": 3.8, "MFE_180D_pct": 3.8, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -23.8, "MAE_90D_pct": -39.8, "MAE_180D_pct": -39.8, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 196200, "drawdown_after_peak_pct": -39.8, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "R13L12_C07_HANMI_042700_2024-06-13_189000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "holdout_validation_from_prior_R2_HBM_equipment_axis", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true, "round": "R13", "loop": "12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_HOLDOUT", "sector": "Cross-archetype RedTeam holdout / AI semiconductor equipment", "primary_archetype": "hbm_equipment_order_relative_strength_vs_customer_quality_only", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window"}
{"row_type": "trigger", "trigger_id": "R13L12_T004_089030_STAGE2", "case_id": "R13L12_C07_TECHWING_089030", "symbol": "089030", "company_name": "테크윙", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-19", "entry_date": "2024-01-19", "entry_price": 14600, "evidence_available_at_that_date": "HBM inspection/prober route and relative strength proxy visible; explicit full revision not yet fully confirmed", "evidence_source": "historical public report/disclosure narrative proxy; stock-web OHLC row validation", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv", "profile_path": "atlas/symbol_profiles/089/089030.json", "MFE_30D_pct": 56.8, "MFE_90D_pct": 209.6, "MFE_180D_pct": 384.9, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.7, "MAE_90D_pct": -11.7, "MAE_180D_pct": -11.7, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 70800, "drawdown_after_peak_pct": -31.5, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_missed_structural", "same_entry_group_id": "R13L12_C07_TECHWING_089030_2024-01-19_14600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "round": "R13", "loop": "12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_HOLDOUT", "sector": "Cross-archetype RedTeam holdout / AI semiconductor equipment", "primary_archetype": "hbm_equipment_order_relative_strength_vs_customer_quality_only", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window"}
{"row_type": "trigger", "trigger_id": "R13L12_T005_089030_GREEN_LATE", "case_id": "R13L12_C07_TECHWING_089030", "symbol": "089030", "company_name": "테크윙", "trigger_type": "Stage3-Yellow_to_Green", "trigger_date": "2024-03-27", "entry_date": "2024-03-27", "entry_price": 35200, "evidence_available_at_that_date": "confirmation/revision proxy visible after Stage2 relative-strength run", "evidence_source": "historical public report/disclosure narrative proxy; stock-web OHLC row validation", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv", "profile_path": "atlas/symbol_profiles/089/089030.json", "MFE_30D_pct": 11.1, "MFE_90D_pct": 82.7, "MFE_180D_pct": 101.1, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.6, "MAE_90D_pct": -11.6, "MAE_180D_pct": -11.6, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 70800, "drawdown_after_peak_pct": -31.5, "green_lateness_ratio": 0.366, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_success_but_stage2_better", "current_profile_verdict": "current_profile_too_late", "same_entry_group_id": "R13L12_C07_TECHWING_089030_2024-03-27_35200", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "round": "R13", "loop": "12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_HOLDOUT", "sector": "Cross-archetype RedTeam holdout / AI semiconductor equipment", "primary_archetype": "hbm_equipment_order_relative_strength_vs_customer_quality_only", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window"}
{"row_type": "trigger", "trigger_id": "R13L12_T006_039030_YELLOW", "case_id": "R13L12_C07_EOTECH_039030", "symbol": "039030", "company_name": "이오테크닉스", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-01-19", "entry_date": "2024-01-19", "entry_price": 183900, "evidence_available_at_that_date": "advanced packaging/laser equipment optionality plus relative strength; order specificity weaker than Hanmi/Techwing", "evidence_source": "historical public report narrative proxy; stock-web OHLC row validation", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv", "profile_path": "atlas/symbol_profiles/039/039030.json", "MFE_30D_pct": 16.6, "MFE_90D_pct": 52.8, "MFE_180D_pct": 52.8, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.1, "MAE_90D_pct": -11.1, "MAE_180D_pct": -14.0, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-12", "peak_price": 281000, "drawdown_after_peak_pct": -43.7, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_mae_success_yellow", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "R13L12_C07_EOTECH_039030_2024-01-19_183900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "round": "R13", "loop": "12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_HOLDOUT", "sector": "Cross-archetype RedTeam holdout / AI semiconductor equipment", "primary_archetype": "hbm_equipment_order_relative_strength_vs_customer_quality_only", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window"}
{"row_type": "trigger", "trigger_id": "R13L12_T007_095340_COUNTER", "case_id": "R13L12_C07_ISC_095340", "symbol": "095340", "company_name": "ISC", "trigger_type": "False-Green counterexample", "trigger_date": "2024-03-08", "entry_date": "2024-03-08", "entry_price": 95000, "evidence_available_at_that_date": "customer-quality/socket narrative and relative strength without fresh backlog/order/revision bridge", "evidence_source": "historical public report narrative proxy; stock-web OHLC row validation", "stage2_evidence_fields": ["relative_strength", "customer_or_order_quality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv", "profile_path": "atlas/symbol_profiles/095/095340.json", "MFE_30D_pct": 13.7, "MFE_90D_pct": 13.7, "MFE_180D_pct": 13.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.3, "MAE_90D_pct": -29.6, "MAE_180D_pct": -48.4, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-28", "peak_price": 108000, "drawdown_after_peak_pct": -54.6, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.75, "four_b_timing_verdict": "price_only_local_4B_too_early_without_order_slowdown", "four_b_evidence_type": ["valuation_blowoff", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "same_entry_group_id": "R13L12_C07_ISC_095340_2024-03-08_95000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "round": "R13", "loop": "12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_HOLDOUT", "sector": "Cross-archetype RedTeam holdout / AI semiconductor equipment", "primary_archetype": "hbm_equipment_order_relative_strength_vs_customer_quality_only", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window"}
{"row_type": "trigger", "trigger_id": "R13L12_T008_058470_COUNTER", "case_id": "R13L12_C07_LEENO_058470", "symbol": "058470", "company_name": "리노공업", "trigger_type": "Stage2/Yellow counterexample", "trigger_date": "2024-03-11", "entry_date": "2024-03-11", "entry_price": 242500, "evidence_available_at_that_date": "premium test-socket/customer quality plus AI/advanced chip narrative, but no explicit HBM equipment order/backlog bridge", "evidence_source": "historical public report narrative proxy; stock-web OHLC row validation", "stage2_evidence_fields": ["customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv", "profile_path": "atlas/symbol_profiles/058/058470.json", "MFE_30D_pct": 16.5, "MFE_90D_pct": 27.4, "MFE_180D_pct": 27.4, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -0.8, "MAE_90D_pct": -17.0, "MAE_180D_pct": -20.3, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-07", "peak_price": 309000, "drawdown_after_peak_pct": -37.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.72, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "price_only_local_4B_too_early_without_revision_slowdown", "four_b_evidence_type": ["valuation_blowoff", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_or_yellow_only", "current_profile_verdict": "current_profile_false_positive", "same_entry_group_id": "R13L12_C07_LEENO_058470_2024-03-11_242500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "round": "R13", "loop": "12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_HOLDOUT", "sector": "Cross-archetype RedTeam holdout / AI semiconductor equipment", "primary_archetype": "hbm_equipment_order_relative_strength_vs_customer_quality_only", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window"}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L12_C07_HANMI_042700", "trigger_id": "R13L12_T001_042700_STAGE2", "symbol": "042700", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 88, "backlog_visibility_score": 72, "margin_bridge_score": 70, "revision_score": 50, "relative_strength_score": 88, "customer_quality_score": 90, "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 66, "execution_risk_score": 35, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 82.0, "stage_label_before": "Stage3-Yellow/Stage2-Actionable", "raw_component_scores_after": {"contract_score": 92, "backlog_visibility_score": 78, "margin_bridge_score": 75, "revision_score": 55, "relative_strength_score": 88, "customer_quality_score": 92, "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 66, "execution_risk_score": 35, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 87.5, "stage_label_after": "Stage3-Green candidate but only after customer/order gate", "changed_components": ["customer_quality_score", "backlog_visibility_score", "revision_score"], "component_delta_explanation": "Named/visible HBM equipment route deserves Green only after order/backlog+revision bridge; early Stage2 was still economically useful.", "MFE_90D_pct": 95.2, "MAE_90D_pct": -9.9, "score_return_alignment_label": "strong_positive_alignment", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L12_C07_TECHWING_089030", "trigger_id": "R13L12_T004_089030_STAGE2", "symbol": "089030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 60, "backlog_visibility_score": 52, "margin_bridge_score": 48, "revision_score": 42, "relative_strength_score": 92, "customer_quality_score": 70, "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 72, "execution_risk_score": 45, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 74.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 70, "backlog_visibility_score": 64, "margin_bridge_score": 56, "revision_score": 50, "relative_strength_score": 92, "customer_quality_score": 76, "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 72, "execution_risk_score": 45, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 80.5, "stage_label_after": "Stage3-Yellow / early C07 candidate", "changed_components": ["backlog_visibility_score", "customer_quality_score"], "component_delta_explanation": "For C07, relative strength plus plausible HBM shipment route should promote Stage2/Yellow earlier, but Green still waits for backlog/revision.", "MFE_90D_pct": 209.6, "MAE_90D_pct": -11.7, "score_return_alignment_label": "very_strong_positive_alignment", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L12_C07_EOTECH_039030", "trigger_id": "R13L12_T006_039030_YELLOW", "symbol": "039030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": 42, "margin_bridge_score": 55, "revision_score": 48, "relative_strength_score": 75, "customer_quality_score": 60, "policy_or_regulatory_score": 40, "valuation_repricing_score": 62, "execution_risk_score": 50, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": 48, "margin_bridge_score": 58, "revision_score": 50, "relative_strength_score": 75, "customer_quality_score": 62, "policy_or_regulatory_score": 40, "valuation_repricing_score": 62, "execution_risk_score": 50, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 77.5, "stage_label_after": "Stage3-Yellow kept", "changed_components": ["backlog_visibility_score"], "component_delta_explanation": "Advanced-equipment optionality is usable, but lower order specificity blocks C07 Green.", "MFE_90D_pct": 52.8, "MAE_90D_pct": -11.1, "score_return_alignment_label": "moderate_positive_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L12_C07_ISC_095340", "trigger_id": "R13L12_T007_095340_COUNTER", "symbol": "095340", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": 30, "margin_bridge_score": 35, "revision_score": 25, "relative_strength_score": 78, "customer_quality_score": 72, "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 65, "execution_risk_score": 65, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 73.0, "stage_label_before": "Stage2/false Yellow risk", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": 24, "margin_bridge_score": 28, "revision_score": 20, "relative_strength_score": 60, "customer_quality_score": 58, "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 55, "execution_risk_score": 75, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 61.0, "stage_label_after": "Stage1 / no promotion", "changed_components": ["backlog_visibility_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "Customer quality and sockets should be capped unless fresh HBM order or revision evidence exists; this reduces false Green risk.", "MFE_90D_pct": 13.7, "MAE_90D_pct": -29.6, "score_return_alignment_label": "counterexample_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L12_C07_LEENO_058470", "trigger_id": "R13L12_T008_058470_COUNTER", "symbol": "058470", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": 35, "margin_bridge_score": 50, "revision_score": 42, "relative_strength_score": 70, "customer_quality_score": 80, "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 58, "execution_risk_score": 55, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 74.0, "stage_label_before": "Stage2/Yellow watch", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": 30, "margin_bridge_score": 48, "revision_score": 40, "relative_strength_score": 60, "customer_quality_score": 72, "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 52, "execution_risk_score": 65, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 68.0, "stage_label_after": "Stage2 watch / no Green", "changed_components": ["customer_quality_score", "backlog_visibility_score", "execution_risk_score"], "component_delta_explanation": "Premium quality without explicit HBM equipment/order conversion is not enough for C07 Green; leave as watch/Yelllow boundary.", "MFE_90D_pct": 27.4, "MAE_90D_pct": -17.0, "score_return_alignment_label": "weak_to_moderate_alignment", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c07_customer_named_order_or_backlog_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"Positive cases had HBM equipment/order route or relative-strength plus customer route; counterexamples had quality/narrative without explicit order/backlog conversion.","Reduced false_positive_green while preserving Hanmi/Techwing early promotion.",R13L12_T001_042700_STAGE2|R13L12_T004_089030_STAGE2|R13L12_T007_095340_COUNTER|R13L12_T008_058470_COUNTER,5,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c07_relative_strength_without_order_cap,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"Relative strength alone confused ISC/Leeno with true HBM equipment winners; require non-price order/revision bridge for Green.","Blocks price/quality-only false positives and keeps them at Stage2/Yellow watch.",R13L12_T006_039030_YELLOW|R13L12_T007_095340_COUNTER|R13L12_T008_058470_COUNTER,3,3,2,medium,guard_shadow_only,"not production; strengthens price_only_blowoff_blocks_positive_stage"
shadow_weight,c07_full_4b_requires_delivery_or_revision_slowdown,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"Full 4B is best when valuation/positioning overheat coincides with delivery/revision slowdown; price-only local peaks are overlay-only.","Improves 4B timing on Hanmi while avoiding premature full exit labels on ISC/Leeno.",R13L12_T003_042700_4B|R13L12_T007_095340_COUNTER|R13L12_T008_058470_COUNTER,3,2,2,low,overlay_shadow_only,"not production; reinforces full_4b_requires_non_price_evidence"
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": "12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "new_independent_case_count": 4, "reused_case_count": 1, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["current_profile_missed_structural", "current_profile_too_late", "current_profile_false_positive", "price_only_local_4B_too_early"], "loop_contribution_label": "holdout_validation_passed", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","reason":"all selected cases had sufficient 180D stock-web windows","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
next_round = batch_promotion_review_or_R13_loop_13_cross_sector_4B_4C_holdout
recommended_next_focus:
  - aggregate all v12 MDs generated after R13 loop 10
  - promote only repeated sector/canonical-archetype shadow rules
  - reject duplicate_low_value_loop and schema_rematerialization_only rows
  - compare C07 HBM order bridge with C18 consumer channel reorder and C32 control-premium guard as three non-price-evidence templates
```

## 28. Source Notes

```text
stock-web manifest inspected = atlas/manifest.json
stock-web schema inspected = atlas/schema.json
stock-web profiles inspected:
- atlas/symbol_profiles/042/042700.json
- atlas/symbol_profiles/089/089030.json
- atlas/symbol_profiles/039/039030.json
- atlas/symbol_profiles/095/095340.json
- atlas/symbol_profiles/058/058470.json
stock-web shards inspected:
- atlas/ohlcv_tradable_by_symbol_year/042/042700/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv
allowed stock_agent research artifacts inspected:
- reports/e2r_calibration/ingest_summary.md
- reports/e2r_calibration/applied_scoring_diff.md
```
