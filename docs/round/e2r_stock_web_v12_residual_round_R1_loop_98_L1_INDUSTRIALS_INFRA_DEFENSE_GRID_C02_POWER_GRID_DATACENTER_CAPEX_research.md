# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R1
scheduled_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE_VS_POWER_SUPPLY_CAPEX_FALSE_STAGE2_AND_CABLE_COPPER_GRID_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | grid_capex_delivery_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R1_loop_98_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
```

This file is the corrected final output for this execution. The scheduler state after R13 loop 97 is R1 / loop 98. R1 is the L1 industrials / infrastructure / defense / grid round, and this run fills C02 power-grid / datacenter capex behavior rather than repeating the immediately preceding R1 loop 97 C05 EPC margin-gap file or R1 loop 96 C01 order-backlog file.

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
grid_capex_delivery_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R1
scheduled_loop = 98
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
round_sector_consistency = pass
computed_next_round = R2
computed_next_loop = 98
```

C02 is a grid/datacenter capex delivery archetype. The grid-capex headline is the substation map; the usable signal is order backlog, customer quality, delivery slot, capacity utilization, pass-through economics, margin and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C02_POWER_GRID_DATACENTER_CAPEX = 22 rows / 12 symbols / good-bad Stage2 11-4 / 4B-4C 2-0
top covered symbols include 000500(3), 006340(3), 033100(3), 001440(2), 017040(2), 189860(2)
previous R1 loop-95 C02 symbols avoided: 267260, 237750, 017510
previous R1 loop-96 C01 symbols avoided: 082740, 064820, 101170
previous R1 loop-97 C05 symbols avoided: 100840, 028050, 045100
previous R11 loop-97 C03 symbols avoided: 077970, 361390, 024740
previous R13 loop-97 review-only rows do_not_count_as_new_case
```

Selected rows avoid hard duplicates and top repeated C02 symbols:

```text
010120 / Stage2-Actionable / 2024-02-06
037030 / Stage2-Actionable / 2024-02-19
024840 / Stage4B / 2024-05-21
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
| 010120 | atlas/symbol_profiles/010/010120.json | selected 2024 window clean after old 1995/1999/2003 CA candidates |
| 037030 | atlas/symbol_profiles/037/037030.json | selected 2024 window clean after old 2000/2001/2005/2018 CA candidates |
| 024840 | atlas/symbol_profiles/024/024840.json | selected 2024~2025 window clean after old 1997~2017 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R1L98_C02_LSELECTRIC_2024_GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_POSITIVE | 010120 | 2024-02-06 | yes | 180 | yes | yes | true |
| R1L98_C02_POWERNET_2024_POWER_SUPPLY_DATACENTER_CAPEX_FALSE_STAGE2 | 037030 | 2024-02-19 | yes | 180 | yes | yes | true |
| R1L98_C02_KBIMETAL_2024_CABLE_COPPER_GRID_EVENT_CAP_4B | 024840 | 2024-05-21 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C02_POWER_GRID_DATACENTER_CAPEX | GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE | Positive Stage2 requires order backlog, delivery slot, datacenter or utility customer quality, capacity utilization, margin and revision bridge. |
| C02_POWER_GRID_DATACENTER_CAPEX | POWER_SUPPLY_CAPEX_FALSE_STAGE2 | Power-supply / datacenter-capex sympathy without customer order and delivery/margin bridge can become false Stage2. |
| C02_POWER_GRID_DATACENTER_CAPEX | CABLE_COPPER_GRID_EVENT_CAP_4B | Cable/copper/grid event premium should route to 4B when customer order, delivery, pass-through and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R1L98_C02_LSELECTRIC_2024_GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_POSITIVE | 010120 | LS ELECTRIC | positive | Grid automation / datacenter capex delivery bridge produced very strong MFE with shallow MAE. |
| R1L98_C02_POWERNET_2024_POWER_SUPPLY_DATACENTER_CAPEX_FALSE_STAGE2 | 037030 | 파워넷 | counterexample | Power-supply capex watch had low MFE and then persistent MAE. |
| R1L98_C02_KBIMETAL_2024_CABLE_COPPER_GRID_EVENT_CAP_4B | 024840 | KBI메탈 | counterexample / 4B | Cable/copper/grid event premium capped at the May spike and then de-rated deeply. |

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
| LS ELECTRIC grid/datacenter capex delivery bridge | historical public/report proxy | true | true | shadow-only positive |
| Powernet power-supply capex false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| KBI Metal cable/copper grid event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 010120 | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv | atlas/symbol_profiles/010/010120.json |
| 037030 | atlas/ohlcv_tradable_by_symbol_year/037/037030/2024.csv | atlas/symbol_profiles/037/037030.json |
| 024840 | atlas/ohlcv_tradable_by_symbol_year/024/024840/2024.csv and 2025.csv | atlas/symbol_profiles/024/024840.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R1L98_C02_LSELECTRIC_2024_STAGE2_ACTIONABLE_GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE | 010120 | Stage2-Actionable | 2024-02-06 | 65500 | positive | grid/datacenter capex delivery bridge worked |
| R1L98_C02_POWERNET_2024_STAGE2_FALSE_POSITIVE_POWER_SUPPLY_DATACENTER_CAPEX_WATCH | 037030 | Stage2-Actionable | 2024-02-19 | 3125 | counterexample | power-supply capex false Stage2 |
| R1L98_C02_KBIMETAL_2024_STAGE4B_CABLE_COPPER_GRID_EVENT_CAP | 024840 | Stage4B | 2024-05-21 | 4040 | counterexample/4B | cable/copper grid event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1L98_C02_LSELECTRIC_2024_STAGE2_ACTIONABLE_GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE | 65500 | 46.26 | -3.51 | 272.52 | -3.51 | 272.52 | -3.51 | 2024-05-29 | 244000 | -48.28 |
| R1L98_C02_POWERNET_2024_STAGE2_FALSE_POSITIVE_POWER_SUPPLY_DATACENTER_CAPEX_WATCH | 3125 | 8.00 | -9.28 | 8.00 | -20.32 | 8.00 | -34.24 | 2024-02-19 | 3375 | -39.11 |
| R1L98_C02_KBIMETAL_2024_STAGE4B_CABLE_COPPER_GRID_EVENT_CAP | 4040 | 17.45 | -33.66 | 17.45 | -40.72 | 17.45 | -52.87 | 2024-05-21 | 4745 | -59.87 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C02 Stage2 needs order backlog / delivery slot / customer / capacity / margin / revision bridge |
| grid_capex_delivery_guardrail | strengthen: grid/datacenter labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing power-supply and cable/copper grid premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE grid-capex rows cannot promote without durable delivery/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether grid/datacenter capex narrative becomes order, delivery and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 010120 | good_stage2_with_later_watch | Order/delivery bridge produced very strong MFE, but later valuation watch remains necessary. |
| 037030 | bad_stage2 | Power-supply capex watch lacked customer-order and delivery/margin bridge, producing low MFE and persistent MAE. |
| 024840 | good_4B | Cable/copper grid premium capped at the May event spike and later drew down deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 037030 power-supply false Stage2 | 0.93 | 0.93 | false Stage2 due missing customer order / delivery / margin bridge |
| 024840 cable/copper grid cap | 0.85 | 0.85 | good full-window 4B timing after May cable/copper grid event premium |
| 010120 grid/datacenter delivery bridge | n/a | n/a | positive Stage2, but later grid-capex valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 037030 / 024840
```

No hard 4C candidate is introduced in this R1 loop 98 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 power-grid/datacenter capex cases, Stage2 requires verified order backlog, customer quality, delivery-slot visibility, capacity utilization, pass-through economics, margin, or revision bridge. Grid, datacenter, power supply, cable/copper, transformer, switchgear, AI power or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
rule = C02 should split true order/backlog/delivery/margin positives from power-supply false Stage2 and cable/copper grid event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 99.32 | -21.52 | 0.67 | mixed; C02 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 99.32 | -21.52 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L1 order/delivery/margin bridge required | 2 | 140.26 | -11.92 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C02 bridge vs event-cap split | 2 | 140.26 | -11.92 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing grid-capex themes as positive | 1 | 272.52 | -3.51 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 010120 grid/datacenter bridge | 66 | Stage2-Watch | 80 | Stage2-Actionable | 272.52 | -3.51 | grid_datacenter_capex_delivery_positive |
| 037030 power-supply false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 8.00 | -20.32 | power_supply_capex_false_stage2 |
| 024840 cable/copper cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 17.45 | -40.72 | cable_copper_grid_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE_VS_POWER_SUPPLY_CAPEX_FALSE_STAGE2_AND_CABLE_COPPER_GRID_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Starts loop98 with C02: LS ELECTRIC grid/datacenter capex delivery positive, Powernet power-supply capex false Stage2, and KBI Metal cable/copper grid event-cap 4B while avoiding top repeated C02 symbols and recent R1/R11/R13 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, grid_capex_delivery_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: grid_datacenter_capex_delivery_positive, power_supply_capex_false_stage2, cable_copper_grid_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, grid_capex_delivery_guardrail, high_MAE_guardrail
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
- C02 power-grid/datacenter capex bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,configured,C02_requires_order_backlog_delivery_customer_capacity_margin_revision_bridge,0,"C02 Stage2 should require grid/datacenter customer order, backlog conversion, delivery-slot visibility, capacity utilization, pass-through, margin, or revision bridge, not power-grid/datacenter capex label alone","LS ELECTRIC positive worked; Powernet and KBI Metal event/watch rows failed positive-stage promotion","R1L98_C02_LSELECTRIC_2024_STAGE2_ACTIONABLE_GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE|R1L98_C02_POWERNET_2024_STAGE2_FALSE_POSITIVE_POWER_SUPPLY_DATACENTER_CAPEX_WATCH|R1L98_C02_KBIMETAL_2024_STAGE4B_CABLE_COPPER_GRID_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,configured,cap_bridge_missing_power_supply_and_cable_copper_grid_event_premiums_as_4B_watch,0,"Power-supply, cable/copper and grid equipment premiums can peak before customer order, delivery, pass-through and margin bridge is proven","Powernet had low MFE and persistent MAE; KBI Metal showed 4B event-cap behavior after the May cable/copper grid spike","R1L98_C02_POWERNET_2024_STAGE2_FALSE_POSITIVE_POWER_SUPPLY_DATACENTER_CAPEX_WATCH|R1L98_C02_KBIMETAL_2024_STAGE4B_CABLE_COPPER_GRID_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,configured,block_positive_stage_when_grid_capex_theme_has_high_or_persistent_MAE_without_delivery_bridge,0,"High or persistent MAE after bridge-missing C02 entries should block Stage2/Stage3 promotion unless order, delivery, capacity and margin evidence survives","Powernet MAE180=-34.24 and KBI Metal MAE90=-40.72","R1L98_C02_POWERNET_2024_STAGE2_FALSE_POSITIVE_POWER_SUPPLY_DATACENTER_CAPEX_WATCH|R1L98_C02_KBIMETAL_2024_STAGE4B_CABLE_COPPER_GRID_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R1L98_C02_LSELECTRIC_2024_GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_POSITIVE", "symbol": "010120", "company_name": "LS ELECTRIC", "round": "R1", "loop": "98", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE_VS_POWER_SUPPLY_CAPEX_FALSE_STAGE2_AND_CABLE_COPPER_GRID_EVENT_CAP", "case_type": "structural_success_with_later_grid_capex_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R1L98_C02_LSELECTRIC_2024_STAGE2_ACTIONABLE_GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Grid automation / datacenter capex / power-equipment delivery bridge produced very strong 30D/90D/180D MFE with shallow early MAE. C02 works when grid-capex narrative maps into order backlog, delivery slot, customer quality, capacity utilization, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C02_positive_requires_order_backlog_delivery_customer_capacity_margin_revision_bridge_not_grid_capex_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1995/1999/2003 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R1L98_C02_POWERNET_2024_POWER_SUPPLY_DATACENTER_CAPEX_FALSE_STAGE2", "symbol": "037030", "company_name": "파워넷", "round": "R1", "loop": "98", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE_VS_POWER_SUPPLY_CAPEX_FALSE_STAGE2_AND_CABLE_COPPER_GRID_EVENT_CAP", "case_type": "failed_rerating_power_supply_capex_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R1L98_C02_POWERNET_2024_STAGE2_FALSE_POSITIVE_POWER_SUPPLY_DATACENTER_CAPEX_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Power-supply / datacenter capex sympathy watch had only low MFE and then a persistent 90D/180D drawdown. C02 Stage2 should not be awarded without confirmed customer order, delivery visibility, capacity utilization, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_power_supply_capex_watch_counts_without_customer_order_delivery_capacity_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2000/2001/2005/2018 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R1L98_C02_KBIMETAL_2024_CABLE_COPPER_GRID_EVENT_CAP_4B", "symbol": "024840", "company_name": "KBI메탈", "round": "R1", "loop": "98", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE_VS_POWER_SUPPLY_CAPEX_FALSE_STAGE2_AND_CABLE_COPPER_GRID_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R1L98_C02_KBIMETAL_2024_STAGE4B_CABLE_COPPER_GRID_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Cable/copper/grid event premium capped at the May spike and then de-rated deeply. C02 should route bridge-missing cable/copper grid premiums to 4B unless utility/datacenter customer order, delivery slot, copper pass-through, utilization, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_cable_copper_grid_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024~2025 forward window clean after old 1997~2017 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R1L98_C02_LSELECTRIC_2024_STAGE2_ACTIONABLE_GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE", "case_id": "R1L98_C02_LSELECTRIC_2024_GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_POSITIVE", "symbol": "010120", "company_name": "LS ELECTRIC", "round": "R1", "loop": "98", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE_VS_POWER_SUPPLY_CAPEX_FALSE_STAGE2_AND_CABLE_COPPER_GRID_EVENT_CAP", "sector": "grid_automation_datacenter_capex_power_equipment_delivery", "primary_archetype": "order_backlog_delivery_customer_capacity_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | grid_capex_delivery_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-06", "entry_date": "2024-02-06", "entry_price": 65500.0, "evidence_available_at_that_date": "grid automation / datacenter capex power-equipment demand, order backlog, delivery-slot visibility, customer quality and margin/revision bridge proxy after February washout; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["order_backlog_proxy", "delivery_slot_visibility_proxy", "datacenter_capex_customer_proxy", "capacity_utilization_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "very_strong_MFE90", "very_strong_MFE180", "shallow_MAE90"], "stage4b_evidence_fields": ["later_grid_capex_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv", "profile_path": "atlas/symbol_profiles/010/010120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 46.26, "MFE_90D_pct": 272.52, "MFE_180D_pct": 272.52, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.51, "MAE_90D_pct": -3.51, "MAE_180D_pct": -3.51, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-29", "peak_price": 244000.0, "drawdown_after_peak_pct": -48.28, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_grid_capex_valuation_4B_watch_needed", "four_b_evidence_type": ["grid_capex_order_delivery_bridge", "datacenter_customer_visibility", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_grid_automation_datacenter_capex_delivery_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1995_1999_2003_CA", "same_entry_group_id": "R1L98_C02_010120_2024-02-06_65500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L98_C02_POWERNET_2024_STAGE2_FALSE_POSITIVE_POWER_SUPPLY_DATACENTER_CAPEX_WATCH", "case_id": "R1L98_C02_POWERNET_2024_POWER_SUPPLY_DATACENTER_CAPEX_FALSE_STAGE2", "symbol": "037030", "company_name": "파워넷", "round": "R1", "loop": "98", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE_VS_POWER_SUPPLY_CAPEX_FALSE_STAGE2_AND_CABLE_COPPER_GRID_EVENT_CAP", "sector": "power_supply_datacenter_capex_sympathy_watch", "primary_archetype": "power_supply_capex_watch_without_customer_order_delivery_capacity_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | grid_capex_delivery_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-19", "entry_date": "2024-02-19", "entry_price": 3125.0, "evidence_available_at_that_date": "power-supply / datacenter capex sympathy watch without confirmed grid/datacenter customer order, delivery visibility, capacity utilization, pass-through or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["power_supply_capex_watch", "datacenter_power_sympathy", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "persistent_MAE90", "customer_order_delivery_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/037/037030/2024.csv", "profile_path": "atlas/symbol_profiles/037/037030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.0, "MFE_90D_pct": 8.0, "MFE_180D_pct": 8.0, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -9.28, "MAE_90D_pct": -20.32, "MAE_180D_pct": -34.24, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-19", "peak_price": 3375.0, "drawdown_after_peak_pct": -39.11, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "power_supply_capex_watch_was_false_stage2_due_missing_customer_order_delivery_capacity_margin_bridge", "four_b_evidence_type": ["power_supply_datacenter_capex_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_power_supply_datacenter_capex_watch_without_order_delivery_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_power_supply_capex_watch_counts_without_customer_order_delivery_capacity_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2000_2001_2005_2018_CA", "same_entry_group_id": "R1L98_C02_037030_2024-02-19_3125", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L98_C02_KBIMETAL_2024_STAGE4B_CABLE_COPPER_GRID_EVENT_CAP", "case_id": "R1L98_C02_KBIMETAL_2024_CABLE_COPPER_GRID_EVENT_CAP_4B", "symbol": "024840", "company_name": "KBI메탈", "round": "R1", "loop": "98", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE_VS_POWER_SUPPLY_CAPEX_FALSE_STAGE2_AND_CABLE_COPPER_GRID_EVENT_CAP", "sector": "cable_copper_grid_datacenter_event_premium", "primary_archetype": "cable_copper_grid_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | grid_capex_delivery_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-05-21", "entry_date": "2024-05-21", "entry_price": 4040.0, "evidence_available_at_that_date": "cable/copper/grid and datacenter-power event premium without confirmed utility/datacenter customer order, delivery slot, copper pass-through, capacity utilization or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["cable_copper_grid_event", "datacenter_power_copper_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "customer_order_delivery_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024840/2024.csv; atlas/ohlcv_tradable_by_symbol_year/024/024840/2025.csv", "profile_path": "atlas/symbol_profiles/024/024840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 17.45, "MFE_90D_pct": 17.45, "MFE_180D_pct": 17.45, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -33.66, "MAE_90D_pct": -40.72, "MAE_180D_pct": -52.87, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-21", "peak_price": 4745.0, "drawdown_after_peak_pct": -59.87, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.85, "four_b_full_window_peak_proximity": 0.85, "four_b_timing_verdict": "good_full_window_4B_timing_cable_copper_grid_event_cap", "four_b_evidence_type": ["cable_copper_grid_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_cable_copper_grid_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_cable_copper_grid_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1997_2017_CA_candidates", "same_entry_group_id": "R1L98_C02_024840_2024-05-21_4040", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L98_C02_LSELECTRIC_2024_GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_POSITIVE", "trigger_id": "R1L98_C02_LSELECTRIC_2024_STAGE2_ACTIONABLE_GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE", "symbol": "010120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 60, "customer_quality_score": 50, "policy_or_regulatory_score": 25, "valuation_repricing_score": 55, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 60, "backlog_visibility_score": 65, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 80, "customer_quality_score": 65, "policy_or_regulatory_score": 25, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "grid_automation_datacenter_capex_delivery_positive", "MFE_90D_pct": 272.52, "MAE_90D_pct": -3.51, "score_return_alignment_label": "grid_datacenter_capex_delivery_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L98_C02_POWERNET_2024_POWER_SUPPLY_DATACENTER_CAPEX_FALSE_STAGE2", "trigger_id": "R1L98_C02_POWERNET_2024_STAGE2_FALSE_POSITIVE_POWER_SUPPLY_DATACENTER_CAPEX_WATCH", "symbol": "037030", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 60, "customer_quality_score": 25, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "power_supply_datacenter_capex_false_stage2", "MFE_90D_pct": 8.0, "MAE_90D_pct": -20.32, "score_return_alignment_label": "power_supply_capex_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_power_supply_capex_watch_counts_without_customer_order_delivery_capacity_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L98_C02_KBIMETAL_2024_CABLE_COPPER_GRID_EVENT_CAP_4B", "trigger_id": "R1L98_C02_KBIMETAL_2024_STAGE4B_CABLE_COPPER_GRID_EVENT_CAP", "symbol": "024840", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "cable_copper_grid_event_cap_4B_guard", "MFE_90D_pct": 17.45, "MAE_90D_pct": -40.72, "score_return_alignment_label": "cable_copper_grid_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_cable_copper_grid_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": "98", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_AUTOMATION_DATACENTER_CAPEX_DELIVERY_BRIDGE_VS_POWER_SUPPLY_CAPEX_FALSE_STAGE2_AND_CABLE_COPPER_GRID_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "grid_capex_delivery_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["grid_datacenter_capex_delivery_positive", "power_supply_capex_false_stage2", "cable_copper_grid_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C02 rows need explicit order backlog, customer quality, delivery-slot visibility, capacity utilization, pass-through economics, margin or revision bridge before positive promotion.
- In C02, bridge-missing power-grid/datacenter event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C02 power-grid/datacenter capex rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R1
completed_loop = 98
next_round = R2
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
