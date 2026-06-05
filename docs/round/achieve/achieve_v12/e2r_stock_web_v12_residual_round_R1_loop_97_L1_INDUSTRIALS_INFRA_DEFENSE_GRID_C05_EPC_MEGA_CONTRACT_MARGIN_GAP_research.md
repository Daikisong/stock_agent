# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R1
scheduled_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE_VS_GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2_AND_SEMICON_FACILITY_EPC_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R1_loop_97_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
```

This file is the corrected final output for this execution. The scheduler state after R13 loop 96 is R1 / loop 97. R1 is the L1 industrials / infrastructure / defense / grid round, and this run fills under-covered C05 EPC mega-contract margin-gap behavior rather than repeating the immediately preceding R1 loop 96 C01 order-backlog/margin file or R11 loop 96 C04 nuclear-policy file.

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
scheduled_round = R1
scheduled_loop = 97
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
round_sector_consistency = pass
computed_next_round = R2
computed_next_loop = 97
```

C05 is an EPC contract-quality-to-margin archetype. The contract headline is the steel frame; the usable signal is cost-to-complete, delivery schedule, change-order economics, customer/payment quality, margin and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP = 10 rows / 9 symbols / good-bad Stage2 3-4 / 4B-4C 0-0
top covered symbols include 053690(2), 002150(1), 011560(1), 023350(1), 023960(1), 054930(1)
previous R1 loop-96 C01 symbols avoided: 082740, 064820, 101170
previous R1 loop-95 C02 symbols avoided: 267260, 237750, 017510
previous R11 loop-96 C04 symbols avoided: 052690, 105840, 019990
previous R13 loop-96 review-only rows do_not_count_as_new_case
```

Selected rows avoid hard duplicates and top repeated C05 symbols:

```text
100840 / Stage2-Actionable / 2024-06-03
028050 / Stage2-Actionable / 2024-04-03
045100 / Stage4B / 2024-04-16
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
| 100840 | atlas/symbol_profiles/100/100840.json | entry after 2024-04-16 / 2024-05-17 CA-candidate boundary; post-boundary window used |
| 028050 | atlas/symbol_profiles/028/028050.json | selected 2024 window clean after old 2016 CA candidate |
| 045100 | atlas/symbol_profiles/045/045100.json | selected 2024 window clean after old CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R1L97_C05_SNTENERGY_2024_HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_POSITIVE | 100840 | 2024-06-03 | yes | 180 | yes | post-CA clean | true |
| R1L97_C05_SAMSUNGEA_2024_GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2 | 028050 | 2024-04-03 | yes | 180 | yes | yes | true |
| R1L97_C05_HANYANGENG_2024_SEMICON_FACILITY_EPC_EVENT_CAP_4B | 045100 | 2024-04-16 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE | Positive Stage2 requires order quality, delivery visibility, cost-to-complete control, customer/payment quality, margin and revision bridge. |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2 | Global EPC/mega-contract watch without cost-to-complete and margin bridge can become false Stage2. |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | SEMICON_FACILITY_EPC_EVENT_CAP_4B | Facility EPC/services event premium should route to 4B when execution schedule and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R1L97_C05_SNTENERGY_2024_HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_POSITIVE | 100840 | SNT에너지 | positive | Post-CA heat-exchanger/plant EPC order and margin bridge produced strong forward MFE. |
| R1L97_C05_SAMSUNGEA_2024_GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2 | 028050 | 삼성E&A | counterexample | Global EPC order watch had limited MFE and later margin-gap drawdown. |
| R1L97_C05_HANYANGENG_2024_SEMICON_FACILITY_EPC_EVENT_CAP_4B | 045100 | 한양이엔지 | counterexample / 4B | Semiconductor facility EPC event premium capped around the April spike and failed to compound. |

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
| SNT Energy heat-exchanger / plant EPC order bridge | historical public/report proxy | true | true | shadow-only positive |
| Samsung E&A global EPC margin-gap false Stage2 | historical public/news/report proxy | true | true | false-Stage2 guardrail |
| Hanyang ENG semicon facility EPC event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 100840 | atlas/ohlcv_tradable_by_symbol_year/100/100840/2024.csv and 2025.csv | atlas/symbol_profiles/100/100840.json |
| 028050 | atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv | atlas/symbol_profiles/028/028050.json |
| 045100 | atlas/ohlcv_tradable_by_symbol_year/045/045100/2024.csv | atlas/symbol_profiles/045/045100.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R1L97_C05_SNTENERGY_2024_STAGE2_ACTIONABLE_HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE | 100840 | Stage2-Actionable | 2024-06-03 | 10050 | positive | post-CA EPC order/margin bridge worked |
| R1L97_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_GLOBAL_EPC_MARGIN_GAP_WATCH | 028050 | Stage2-Actionable | 2024-04-03 | 25300 | counterexample | global EPC margin-gap false Stage2 |
| R1L97_C05_HANYANGENG_2024_STAGE4B_SEMICON_FACILITY_EPC_EVENT_CAP | 045100 | Stage4B | 2024-04-16 | 20900 | counterexample/4B | semicon facility EPC event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1L97_C05_SNTENERGY_2024_STAGE2_ACTIONABLE_HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE | 10050 | 60.20 | -4.28 | 60.20 | -4.28 | 232.34 | -4.28 | 2025-02-25 | 33400 | -13.47 |
| R1L97_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_GLOBAL_EPC_MARGIN_GAP_WATCH | 25300 | 6.72 | -1.19 | 6.72 | -14.62 | 6.72 | -18.18 | 2024-04-30 | 27000 | -19.63 |
| R1L97_C05_HANYANGENG_2024_STAGE4B_SEMICON_FACILITY_EPC_EVENT_CAP | 20900 | 7.18 | -9.38 | 7.18 | -13.92 | 7.18 | -13.92 | 2024-04-17 | 22400 | -19.69 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C05 Stage2 needs contract quality / delivery / cost-to-complete / change-order / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing EPC/facility event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: persistent MAE after EPC margin-gap watches blocks promotion without cost/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether EPC/order narrative becomes execution-cost and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 100840 | good_stage2_with_later_watch | Post-CA order/margin bridge produced strong MFE; later valuation watch remains necessary. |
| 028050 | bad_stage2 | Global EPC watch lacked cost-to-complete and revision bridge; MFE stayed limited. |
| 045100 | good_4B | Facility EPC spike capped quickly and did not compound. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 028050 global EPC false Stage2 | 0.94 | 0.94 | false Stage2 due missing cost-to-complete / change-order / margin bridge |
| 045100 semicon facility EPC cap | 0.93 | 0.93 | acceptable 4B timing because order/execution/margin bridge was missing |
| 100840 plant EPC order bridge | n/a | n/a | positive Stage2, but later EPC valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 028050 / 045100
```

No hard 4C candidate is introduced in this R1 loop 97 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 EPC mega-contract margin-gap cases, Stage2 requires verified contract quality, customer/payment quality, delivery-slot visibility, cost-to-complete discipline, change-order economics, margin, or revision bridge. EPC, mega-contract, order, facility, semiconductor-infra, plant or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
rule = C05 should split true order/delivery/cost-to-complete/margin positives from global EPC margin-gap false Stage2 and facility EPC event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 24.70 | -10.94 | 0.67 | mixed; C05 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 24.70 | -10.94 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L1 execution-cost/margin bridge required | 2 | 33.46 | -9.45 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C05 bridge vs event-cap split | 2 | 33.46 | -9.45 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing EPC themes as positive | 1 | 60.20 | -4.28 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 100840 plant EPC bridge | 66 | Stage2-Watch | 79 | Stage2-Actionable | 60.20 | -4.28 | heat_exchanger_plant_EPC_order_margin_positive |
| 028050 global EPC false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 6.72 | -14.62 | global_EPC_margin_gap_false_stage2 |
| 045100 semicon facility cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 7.18 | -13.92 | semicon_facility_EPC_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE_VS_GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2_AND_SEMICON_FACILITY_EPC_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Starts loop97 with under-covered C05: SNT Energy post-CA heat-exchanger/plant EPC order-margin positive, Samsung E&A global EPC margin-gap false Stage2, and Hanyang ENG semicon facility EPC event-cap 4B while avoiding top repeated C05 and recent R1/R11/R13 loop symbols."}
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
residual_error_types_found: heat_exchanger_plant_EPC_order_margin_positive, global_EPC_margin_gap_false_stage2, semicon_facility_EPC_event_cap_4B
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
- C05 EPC mega-contract margin-gap bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,configured,C05_requires_contract_quality_delivery_cost_to_complete_change_order_margin_revision_bridge,0,"C05 Stage2 should require contract quality, customer/payment quality, delivery-slot visibility, cost-to-complete discipline, change-order economics, margin, or revision bridge, not EPC/order/mega-contract label alone","SNT Energy positive worked; Samsung E&A and Hanyang ENG event/watch rows failed positive-stage promotion","R1L97_C05_SNTENERGY_2024_STAGE2_ACTIONABLE_HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE|R1L97_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_GLOBAL_EPC_MARGIN_GAP_WATCH|R1L97_C05_HANYANGENG_2024_STAGE4B_SEMICON_FACILITY_EPC_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,configured,cap_bridge_missing_global_EPC_and_facility_event_premiums_as_4B_watch,0,"Global EPC and facility-services event premiums can peak before cost-to-complete, delivery and margin bridge is proven","Samsung E&A had limited MFE after global EPC watch; Hanyang ENG showed 4B event-cap behavior after the April facility EPC spike","R1L97_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_GLOBAL_EPC_MARGIN_GAP_WATCH|R1L97_C05_HANYANGENG_2024_STAGE4B_SEMICON_FACILITY_EPC_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,configured,block_positive_stage_when_EPC_theme_has_high_or_persistent_MAE_without_margin_bridge,0,"Meaningful or persistent MAE after bridge-missing C05 entries should block Stage2/Stage3 promotion unless order, execution, cost and margin evidence survives","Samsung E&A MAE180=-18.18 and Hanyang ENG MAE90=-13.92","R1L97_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_GLOBAL_EPC_MARGIN_GAP_WATCH|R1L97_C05_HANYANGENG_2024_STAGE4B_SEMICON_FACILITY_EPC_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R1L97_C05_SNTENERGY_2024_HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_POSITIVE", "symbol": "100840", "company_name": "SNT에너지", "round": "R1", "loop": "97", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE_VS_GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2_AND_SEMICON_FACILITY_EPC_EVENT_CAP", "case_type": "structural_success_with_post_CA_entry_and_later_EPC_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R1L97_C05_SNTENERGY_2024_STAGE2_ACTIONABLE_HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Post-CA heat-exchanger / plant EPC order backlog and margin bridge produced strong 30D/90D and very strong 180D MFE with limited early MAE. C05 works only when EPC order narrative maps into customer/order quality, delivery slot visibility, cost-to-complete discipline, margin mix and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C05_positive_requires_order_quality_delivery_cost_margin_revision_bridge_not_EPC_order_label_only", "price_source": "Songdaiki/stock-web", "notes": "Profile flags 2024-04-16 and 2024-05-17 corporate-action candidates; selected entry is 2024-06-03, after the post-CA boundary. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R1L97_C05_SAMSUNGEA_2024_GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2", "symbol": "028050", "company_name": "삼성E&A", "round": "R1", "loop": "97", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE_VS_GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2_AND_SEMICON_FACILITY_EPC_EVENT_CAP", "case_type": "failed_rerating_global_EPC_margin_gap_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R1L97_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_GLOBAL_EPC_MARGIN_GAP_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Global EPC / mega-contract watch produced only limited forward MFE and then drifted into margin-gap drawdown. C05 Stage2 should not be awarded without confirmed contract quality, cost-to-complete visibility, change-order economics, customer/payment quality, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_global_EPC_contract_watch_counts_without_cost_to_complete_change_order_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2016 corporate-action candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R1L97_C05_HANYANGENG_2024_SEMICON_FACILITY_EPC_EVENT_CAP_4B", "symbol": "045100", "company_name": "한양이엔지", "round": "R1", "loop": "97", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE_VS_GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2_AND_SEMICON_FACILITY_EPC_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R1L97_C05_HANYANGENG_2024_STAGE4B_SEMICON_FACILITY_EPC_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Semiconductor facility / EPC service event premium capped around the April spike and then failed to compound. C05 should route bridge-missing facility EPC event premiums to 4B unless customer order backlog, execution schedule, cost-to-complete, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_semicon_facility_EPC_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R1L97_C05_SNTENERGY_2024_STAGE2_ACTIONABLE_HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE", "case_id": "R1L97_C05_SNTENERGY_2024_HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_POSITIVE", "symbol": "100840", "company_name": "SNT에너지", "round": "R1", "loop": "97", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE_VS_GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2_AND_SEMICON_FACILITY_EPC_EVENT_CAP", "sector": "heat_exchanger_plant_EPC_order_backlog_margin", "primary_archetype": "order_quality_delivery_cost_to_complete_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-03", "entry_date": "2024-06-03", "entry_price": 10050.0, "evidence_available_at_that_date": "post-CA plant/EPC heat-exchanger order backlog, delivery-slot visibility, cost-to-complete discipline, margin mix and revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["order_backlog_proxy", "customer_quality_proxy", "delivery_slot_visibility_proxy", "cost_to_complete_discipline_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "very_strong_MFE180", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_EPC_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100840/2024.csv; atlas/ohlcv_tradable_by_symbol_year/100/100840/2025.csv", "profile_path": "atlas/symbol_profiles/100/100840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 60.2, "MFE_90D_pct": 60.2, "MFE_180D_pct": 232.34, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -4.28, "MAE_90D_pct": -4.28, "MAE_180D_pct": -4.28, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-25", "peak_price": 33400.0, "drawdown_after_peak_pct": -13.47, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_EPC_valuation_4B_watch_needed", "four_b_evidence_type": ["post_CA_order_margin_bridge", "customer_delivery_visibility", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_heat_exchanger_plant_EPC_order_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "post_2024-05-17_CA_candidate_boundary_clean_window", "same_entry_group_id": "R1L97_C05_100840_2024-06-03_10050", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L97_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_GLOBAL_EPC_MARGIN_GAP_WATCH", "case_id": "R1L97_C05_SAMSUNGEA_2024_GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2", "symbol": "028050", "company_name": "삼성E&A", "round": "R1", "loop": "97", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE_VS_GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2_AND_SEMICON_FACILITY_EPC_EVENT_CAP", "sector": "global_EPC_mega_contract_margin_gap_watch", "primary_archetype": "global_EPC_watch_without_cost_to_complete_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-03", "entry_date": "2024-04-03", "entry_price": 25300.0, "evidence_available_at_that_date": "global EPC / mega-contract order watch without confirmed cost-to-complete visibility, change-order economics, customer/payment quality or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["global_EPC_order_watch", "mega_contract_theme", "relative_strength_rebound"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "margin_gap_recheck", "cost_to_complete_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv", "profile_path": "atlas/symbol_profiles/028/028050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.72, "MFE_90D_pct": 6.72, "MFE_180D_pct": 6.72, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.19, "MAE_90D_pct": -14.62, "MAE_180D_pct": -18.18, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-30", "peak_price": 27000.0, "drawdown_after_peak_pct": -19.63, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "global_EPC_contract_watch_was_false_stage2_due_missing_cost_to_complete_margin_revision_bridge", "four_b_evidence_type": ["global_EPC_order_premium", "bridge_missing", "limited_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_global_EPC_margin_gap_watch_without_cost_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_global_EPC_contract_watch_counts_without_cost_to_complete_change_order_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2016_CA", "same_entry_group_id": "R1L97_C05_028050_2024-04-03_25300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L97_C05_HANYANGENG_2024_STAGE4B_SEMICON_FACILITY_EPC_EVENT_CAP", "case_id": "R1L97_C05_HANYANGENG_2024_SEMICON_FACILITY_EPC_EVENT_CAP_4B", "symbol": "045100", "company_name": "한양이엔지", "round": "R1", "loop": "97", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE_VS_GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2_AND_SEMICON_FACILITY_EPC_EVENT_CAP", "sector": "semiconductor_facility_EPC_services_event_premium", "primary_archetype": "semicon_facility_EPC_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-16", "entry_date": "2024-04-16", "entry_price": 20900.0, "evidence_available_at_that_date": "semiconductor facility EPC/services event premium after April facility-infra spike without confirmed customer order backlog, execution schedule or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["semicon_facility_EPC_event", "facility_infra_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "limited_MFE90", "execution_schedule_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/045/045100/2024.csv", "profile_path": "atlas/symbol_profiles/045/045100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.18, "MFE_90D_pct": 7.18, "MFE_180D_pct": 7.18, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -9.38, "MAE_90D_pct": -13.92, "MAE_180D_pct": -13.92, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-17", "peak_price": 22400.0, "drawdown_after_peak_pct": -19.69, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "acceptable_4B_timing_semicon_facility_EPC_event_cap_due_missing_order_execution_margin_bridge", "four_b_evidence_type": ["semicon_facility_EPC_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_semicon_facility_EPC_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_semicon_facility_EPC_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA_candidates", "same_entry_group_id": "R1L97_C05_045100_2024-04-16_20900", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L97_C05_SNTENERGY_2024_HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_POSITIVE", "trigger_id": "R1L97_C05_SNTENERGY_2024_STAGE2_ACTIONABLE_HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE", "symbol": "100840", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 60, "customer_quality_score": 45, "policy_or_regulatory_score": 15, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 60, "backlog_visibility_score": 65, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 70, "customer_quality_score": 60, "policy_or_regulatory_score": 15, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "heat_exchanger_plant_EPC_order_margin_positive", "MFE_90D_pct": 60.2, "MAE_90D_pct": -4.28, "score_return_alignment_label": "heat_exchanger_plant_EPC_order_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L97_C05_SAMSUNGEA_2024_GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2", "trigger_id": "R1L97_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_GLOBAL_EPC_MARGIN_GAP_WATCH", "symbol": "028050", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 45, "policy_or_regulatory_score": 15, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 25, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "global_EPC_margin_gap_false_stage2", "MFE_90D_pct": 6.72, "MAE_90D_pct": -14.62, "score_return_alignment_label": "global_EPC_margin_gap_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_global_EPC_contract_watch_counts_without_cost_to_complete_change_order_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L97_C05_HANYANGENG_2024_SEMICON_FACILITY_EPC_EVENT_CAP_4B", "trigger_id": "R1L97_C05_HANYANGENG_2024_STAGE4B_SEMICON_FACILITY_EPC_EVENT_CAP", "symbol": "045100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "semicon_facility_EPC_event_cap_4B_guard", "MFE_90D_pct": 7.18, "MAE_90D_pct": -13.92, "score_return_alignment_label": "semicon_facility_EPC_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_semicon_facility_EPC_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": "97", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE_VS_GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2_AND_SEMICON_FACILITY_EPC_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["heat_exchanger_plant_EPC_order_margin_positive", "global_EPC_margin_gap_false_stage2", "semicon_facility_EPC_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C05 rows need explicit contract quality, customer/payment quality, delivery-slot visibility, cost-to-complete discipline, change-order economics, margin or revision bridge before positive promotion.
- In C05, bridge-missing EPC/facility event-premium rows with limited MFE or persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C05 EPC mega-contract rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R1
completed_loop = 97
next_round = R2
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
