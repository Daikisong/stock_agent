# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R1
scheduled_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id = SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_VS_LNG_EQUIPMENT_FALSE_STAGE2_AND_SHIP_BLOCK_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R1_loop_92_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
```

This file starts loop 92 after the completed R13 loop 91 cross-archetype review. R1 is the L1 industrials/infrastructure/defense/grid round, so this run fills C01 order-backlog / margin-bridge behavior with a ship-engine positive, an LNG equipment false Stage2, and a ship-block equipment 4B event-cap row.

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
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R1
scheduled_loop = 92
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
round_sector_consistency = pass
computed_next_round = R2
computed_next_loop = 92
```

R1 loop 91 used C02; R11 loop 91 used C03; R10 loop 91 used C30. This loop returns to under-covered C01 and avoids top repeated C01 symbols.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C01_ORDER_BACKLOG_MARGIN_BRIDGE = 25 rows / 14 symbols / good-bad Stage2 16-4 / 4B-4C 1-0
top covered symbols include 042660(5), 071970(3), 100090(3), 329180(3), 010140(2), 009540(1)
previous R1 loop-91 C02 symbols avoided: 298040, 119850, 010120
previous R11 loop-91 C03 symbols avoided: 012450, 214430, 013810
previous R13 loop-91 review rows are do_not_count_as_new_case=true
```

Selected rows avoid hard duplicates and top repeated C01 symbols:

```text
082740 / Stage2-Actionable / 2024-03-20
096350 / Stage2-Actionable / 2024-02-23
075580 / Stage4B / 2024-07-17
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
| 082740 | atlas/symbol_profiles/082/082740.json | entry after 2024 name/share transition; old 2018/2021/2022 CA candidates outside selected window |
| 096350 | atlas/symbol_profiles/096/096350.json | selected 2024 window clean after old 2019-or-earlier CA; 2025 CA outside forward window |
| 075580 | atlas/symbol_profiles/075/075580.json | selected 2024 window clean after 2020 CA |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R1L92_C01_HANWHAENGINE_2024_SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_POSITIVE | 082740 | 2024-03-20 | yes | 180 | yes | yes | true |
| R1L92_C01_DAECHANGSOL_2024_LNG_EQUIPMENT_THEME_FALSE_STAGE2 | 096350 | 2024-02-23 | yes | 180 | yes | yes | true |
| R1L92_C01_SEJINHEAVY_2024_SHIP_BLOCK_EVENT_CAP_4B | 075580 | 2024-07-17 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE | Positive Stage2 requires firm order backlog, delivery capacity, customer quality, margin, and revision bridge. |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | LNG_EQUIPMENT_FALSE_STAGE2 | LNG/ship-equipment label without backlog/margin bridge can become false Stage2. |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | SHIP_BLOCK_EVENT_CAP_4B | Ship block/equipment premium should route to 4B when backlog/margin evidence is capped or missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R1L92_C01_HANWHAENGINE_2024_SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_POSITIVE | 082740 | 한화엔진 | positive | Ship-engine order backlog/margin bridge produced strong MFE with controlled initial MAE. |
| R1L92_C01_DAECHANGSOL_2024_LNG_EQUIPMENT_THEME_FALSE_STAGE2 | 096350 | 대창솔루션 | counterexample | LNG equipment theme spike peaked same day and lacked durable backlog/margin bridge. |
| R1L92_C01_SEJINHEAVY_2024_SHIP_BLOCK_EVENT_CAP_4B | 075580 | 세진중공업 | counterexample / 4B | Ship-block/equipment premium capped around the July spike and then drew down deeply. |

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
| Hanwha Engine ship-engine order/backlog bridge | historical public/report proxy | true | true | shadow-only positive |
| Daechang Solution LNG equipment false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Sejin Heavy ship-block equipment cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 082740 | atlas/ohlcv_tradable_by_symbol_year/082/082740/2024.csv | atlas/symbol_profiles/082/082740.json |
| 096350 | atlas/ohlcv_tradable_by_symbol_year/096/096350/2024.csv | atlas/symbol_profiles/096/096350.json |
| 075580 | atlas/ohlcv_tradable_by_symbol_year/075/075580/2024.csv | atlas/symbol_profiles/075/075580.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R1L92_C01_HANWHAENGINE_2024_STAGE2_ACTIONABLE_SHIP_ENGINE_ORDER_BACKLOG_MARGIN | 082740 | Stage2-Actionable | 2024-03-20 | 9950 | positive | ship-engine order/backlog margin bridge worked |
| R1L92_C01_DAECHANGSOL_2024_STAGE2_FALSE_POSITIVE_LNG_EQUIPMENT_THEME | 096350 | Stage2-Actionable | 2024-02-23 | 464 | counterexample | LNG equipment false Stage2 |
| R1L92_C01_SEJINHEAVY_2024_STAGE4B_SHIP_BLOCK_BACKLOG_EVENT_CAP | 075580 | Stage4B | 2024-07-17 | 9850 | counterexample/4B | ship-block equipment event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1L92_C01_HANWHAENGINE_2024_STAGE2_ACTIONABLE_SHIP_ENGINE_ORDER_BACKLOG_MARGIN | 9950 | 39.60 | -6.83 | 72.46 | -6.83 | 84.32 | -6.83 | 2024-11-25 | 18340 | -23.45 |
| R1L92_C01_DAECHANGSOL_2024_STAGE2_FALSE_POSITIVE_LNG_EQUIPMENT_THEME | 464 | 16.38 | -3.02 | 16.38 | -14.87 | 16.38 | -19.83 | 2024-02-23 | 540 | -31.11 |
| R1L92_C01_SEJINHEAVY_2024_STAGE4B_SHIP_BLOCK_BACKLOG_EVENT_CAP | 9850 | 10.86 | -32.28 | 10.86 | -32.28 | 10.86 | -32.28 | 2024-07-17 | 10920 | -38.92 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C01 Stage2 needs firm order/backlog/delivery/margin/revision bridge |
| local_4b_watch_guard | strengthen: shipbuilding/LNG equipment premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: high-MAE equipment-theme rows cannot promote without backlog/margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is order-backlog margin bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 082740 | good_stage2 | Order/backlog/margin bridge produced high MFE with controlled initial MAE. |
| 096350 | bad_stage2 | Theme spike peaked on entry and lacked durable backlog/margin evidence. |
| 075580 | good_4B | Ship-block/equipment premium capped and drew down severely. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 096350 LNG equipment false Stage2 | 1.00 | 1.00 | false Stage2 due missing order/backlog margin bridge |
| 075580 ship-block cap | 1.00 | 1.00 | good full-window 4B timing |
| 082740 ship-engine bridge | n/a | n/a | positive Stage2, but later backlog valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 096350 / 075580
```

No hard 4C candidate is proposed. R1 loop 92 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 order-backlog/margin cases, Stage2 requires verified firm order, backlog visibility, delivery/capacity, customer quality, margin, or revision bridge. Shipbuilding, LNG equipment, ship engine, ship block, or industrial equipment label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
rule = C01 should split true order-backlog/margin positives from LNG-equipment false Stage2 and ship-block/equipment event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 33.23 | -17.99 | 0.67 | mixed; C01 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 33.23 | -17.99 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L1 order/backlog margin bridge required | 2 | 44.42 | -10.85 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C01 bridge vs event-cap split | 2 | 44.42 | -10.85 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing equipment themes as positive | 1 | 72.46 | -6.83 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 082740 ship-engine backlog bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 72.46 | -6.83 | ship_engine_order_backlog_margin_positive |
| 096350 LNG equipment false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 16.38 | -14.87 | LNG_equipment_false_stage2 |
| 075580 ship-block cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 10.86 | -32.28 | ship_block_equipment_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_VS_LNG_EQUIPMENT_FALSE_STAGE2_AND_SHIP_BLOCK_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C01 ship-engine order/backlog margin positive, LNG equipment false Stage2, and ship-block equipment event-cap 4B split using non-top-covered symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: ship_engine_order_backlog_margin_positive, LNG_equipment_false_stage2, ship_block_equipment_event_cap_4B
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
- C01 order-backlog/margin bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,configured,C01_requires_firm_order_backlog_delivery_margin_revision_bridge,0,"C01 Stage2 should require firm order, order backlog, delivery capacity, customer quality, margin, or revision bridge, not shipbuilding/LNG/equipment label alone","Hanwha Engine positive worked; Daechang Solution and Sejin Heavy theme/event rows failed positive-stage promotion","R1L92_C01_HANWHAENGINE_2024_STAGE2_ACTIONABLE_SHIP_ENGINE_ORDER_BACKLOG_MARGIN|R1L92_C01_DAECHANGSOL_2024_STAGE2_FALSE_POSITIVE_LNG_EQUIPMENT_THEME|R1L92_C01_SEJINHEAVY_2024_STAGE4B_SHIP_BLOCK_BACKLOG_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,configured,cap_bridge_missing_shipbuilding_equipment_event_premiums_as_4B_watch,0,"Shipbuilding/LNG equipment premiums can peak before confirmed backlog and margin bridge appears","Daechang Solution peaked same day and lacked follow-through; Sejin Heavy had severe MAE after July event spike","R1L92_C01_DAECHANGSOL_2024_STAGE2_FALSE_POSITIVE_LNG_EQUIPMENT_THEME|R1L92_C01_SEJINHEAVY_2024_STAGE4B_SHIP_BLOCK_BACKLOG_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,configured,block_positive_stage_when_equipment_theme_has_high_MAE_without_backlog_margin_bridge,0,"High MAE after a bridge-missing order/backlog theme entry should block Stage2/Stage3 promotion unless backlog and margin evidence survives","Sejin Heavy MAE90=-32.28; Daechang Solution had capped MFE and persistent 180D MAE","R1L92_C01_DAECHANGSOL_2024_STAGE2_FALSE_POSITIVE_LNG_EQUIPMENT_THEME|R1L92_C01_SEJINHEAVY_2024_STAGE4B_SHIP_BLOCK_BACKLOG_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R1L92_C01_HANWHAENGINE_2024_SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_POSITIVE", "symbol": "082740", "company_name": "한화엔진", "round": "R1", "loop": "92", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_VS_LNG_EQUIPMENT_FALSE_STAGE2_AND_SHIP_BLOCK_EVENT_CAP", "case_type": "structural_success_with_later_backlog_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R1L92_C01_HANWHAENGINE_2024_STAGE2_ACTIONABLE_SHIP_ENGINE_ORDER_BACKLOG_MARGIN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Ship-engine order backlog / shipbuilding cycle / margin-revision bridge produced high 30D/90D/180D MFE with controlled initial MAE. C01 works when order backlog converts into delivery capacity, margin expansion, customer quality, and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C01_positive_requires_order_backlog_delivery_margin_revision_bridge_not_shipbuilding_label_only", "price_source": "Songdaiki/stock-web", "notes": "Entry selected after the March 2024 name/share-count transition window visible in shard; profile CA candidates are older. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R1L92_C01_DAECHANGSOL_2024_LNG_EQUIPMENT_THEME_FALSE_STAGE2", "symbol": "096350", "company_name": "대창솔루션", "round": "R1", "loop": "92", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_VS_LNG_EQUIPMENT_FALSE_STAGE2_AND_SHIP_BLOCK_EVENT_CAP", "case_type": "failed_rerating_equipment_theme_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R1L92_C01_DAECHANGSOL_2024_STAGE2_FALSE_POSITIVE_LNG_EQUIPMENT_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "LNG / shipbuilding equipment theme spike had same-day MFE but no durable follow-through and then persistent 180D MAE. C01 Stage2 should not be awarded without firm order, delivery backlog, margin, and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_LNG_ship_equipment_theme_counts_without_order_backlog_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2019-or-earlier CA candidates; 2025 CA candidate outside forward window. Source-proxy only."}
{"row_type": "case", "case_id": "R1L92_C01_SEJINHEAVY_2024_SHIP_BLOCK_EVENT_CAP_4B", "symbol": "075580", "company_name": "세진중공업", "round": "R1", "loop": "92", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_VS_LNG_EQUIPMENT_FALSE_STAGE2_AND_SHIP_BLOCK_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R1L92_C01_SEJINHEAVY_2024_STAGE4B_SHIP_BLOCK_BACKLOG_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Ship block / shipbuilding equipment premium capped around the July spike and then suffered severe local/full-window MAE. C01 should route bridge-missing equipment event premiums to 4B unless firm order backlog, margin, and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_ship_block_equipment_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2020 CA candidate. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R1L92_C01_HANWHAENGINE_2024_STAGE2_ACTIONABLE_SHIP_ENGINE_ORDER_BACKLOG_MARGIN", "case_id": "R1L92_C01_HANWHAENGINE_2024_SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_POSITIVE", "symbol": "082740", "company_name": "한화엔진", "round": "R1", "loop": "92", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_VS_LNG_EQUIPMENT_FALSE_STAGE2_AND_SHIP_BLOCK_EVENT_CAP", "sector": "ship_engine_order_backlog_margin", "primary_archetype": "ship_engine_delivery_backlog_capacity_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-20", "entry_date": "2024-03-20", "entry_price": 9950.0, "evidence_available_at_that_date": "ship-engine order backlog, shipbuilding delivery cycle, capacity, customer quality, and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["order_backlog_visibility_proxy", "delivery_capacity_proxy", "shipbuilding_cycle_customer_quality", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["high_MFE30", "very_high_MFE90", "very_high_MFE180", "controlled_MAE90"], "stage4b_evidence_fields": ["later_backlog_valuation_watch", "positioning_overheat_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/082/082740/2024.csv", "profile_path": "atlas/symbol_profiles/082/082740.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 39.6, "MFE_90D_pct": 72.46, "MFE_180D_pct": 84.32, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.83, "MAE_90D_pct": -6.83, "MAE_180D_pct": -6.83, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-25", "peak_price": 18340.0, "drawdown_after_peak_pct": -23.45, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_ship_engine_backlog_valuation_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "order_backlog_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_ship_engine_order_backlog_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_entry_after_2024_name_share_transition_and_after_old_CA", "same_entry_group_id": "R1L92_C01_082740_2024-03-20_9950", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L92_C01_DAECHANGSOL_2024_STAGE2_FALSE_POSITIVE_LNG_EQUIPMENT_THEME", "case_id": "R1L92_C01_DAECHANGSOL_2024_LNG_EQUIPMENT_THEME_FALSE_STAGE2", "symbol": "096350", "company_name": "대창솔루션", "round": "R1", "loop": "92", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_VS_LNG_EQUIPMENT_FALSE_STAGE2_AND_SHIP_BLOCK_EVENT_CAP", "sector": "LNG_shipbuilding_equipment_theme", "primary_archetype": "LNG_equipment_theme_without_order_backlog_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-23", "entry_date": "2024-02-23", "entry_price": 464.0, "evidence_available_at_that_date": "LNG / shipbuilding equipment theme spike and order expectation proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["LNG_equipment_theme", "shipbuilding_order_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["same_day_peak", "followthrough_missing", "order_backlog_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096350/2024.csv", "profile_path": "atlas/symbol_profiles/096/096350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.38, "MFE_90D_pct": 16.38, "MFE_180D_pct": 16.38, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.02, "MAE_90D_pct": -14.87, "MAE_180D_pct": -19.83, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-23", "peak_price": 540.0, "drawdown_after_peak_pct": -31.11, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "LNG_equipment_theme_spike_was_false_stage2_due_missing_order_backlog_margin_bridge", "four_b_evidence_type": ["shipbuilding_equipment_theme", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_LNG_equipment_theme_without_order_backlog_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_LNG_ship_equipment_theme_counts_without_order_backlog_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2019_CA_and_before_2025_CA", "same_entry_group_id": "R1L92_C01_096350_2024-02-23_464", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L92_C01_SEJINHEAVY_2024_STAGE4B_SHIP_BLOCK_BACKLOG_EVENT_CAP", "case_id": "R1L92_C01_SEJINHEAVY_2024_SHIP_BLOCK_EVENT_CAP_4B", "symbol": "075580", "company_name": "세진중공업", "round": "R1", "loop": "92", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_VS_LNG_EQUIPMENT_FALSE_STAGE2_AND_SHIP_BLOCK_EVENT_CAP", "sector": "ship_block_equipment_backlog_event", "primary_archetype": "ship_block_equipment_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-07-17", "entry_date": "2024-07-17", "entry_price": 9850.0, "evidence_available_at_that_date": "ship block / shipbuilding equipment backlog premium after July spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["ship_block_equipment_theme", "order_backlog_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "order_backlog_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/075/075580/2024.csv", "profile_path": "atlas/symbol_profiles/075/075580.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.86, "MFE_90D_pct": 10.86, "MFE_180D_pct": 10.86, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -32.28, "MAE_90D_pct": -32.28, "MAE_180D_pct": -32.28, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-17", "peak_price": 10920.0, "drawdown_after_peak_pct": -38.92, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_ship_block_equipment_event_cap", "four_b_evidence_type": ["shipbuilding_equipment_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_ship_block_equipment_premium", "current_profile_verdict": "current_profile_4B_too_late_if_ship_block_equipment_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2020_CA", "same_entry_group_id": "R1L92_C01_075580_2024-07-17_9850", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L92_C01_HANWHAENGINE_2024_SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R1L92_C01_HANWHAENGINE_2024_STAGE2_ACTIONABLE_SHIP_ENGINE_ORDER_BACKLOG_MARGIN", "symbol": "082740", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 60, "backlog_visibility_score": 65, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 50, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "ship_engine_order_backlog_margin_positive", "MFE_90D_pct": 72.46, "MAE_90D_pct": -6.83, "score_return_alignment_label": "ship_engine_order_backlog_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L92_C01_DAECHANGSOL_2024_LNG_EQUIPMENT_THEME_FALSE_STAGE2", "trigger_id": "R1L92_C01_DAECHANGSOL_2024_STAGE2_FALSE_POSITIVE_LNG_EQUIPMENT_THEME", "symbol": "096350", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "LNG_equipment_false_stage2", "MFE_90D_pct": 16.38, "MAE_90D_pct": -14.87, "score_return_alignment_label": "LNG_equipment_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_LNG_ship_equipment_theme_counts_without_order_backlog_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L92_C01_SEJINHEAVY_2024_SHIP_BLOCK_EVENT_CAP_4B", "trigger_id": "R1L92_C01_SEJINHEAVY_2024_STAGE4B_SHIP_BLOCK_BACKLOG_EVENT_CAP", "symbol": "075580", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "ship_block_equipment_event_cap_4B_guard", "MFE_90D_pct": 10.86, "MAE_90D_pct": -32.28, "score_return_alignment_label": "ship_block_equipment_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_ship_block_equipment_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": "92", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_VS_LNG_EQUIPMENT_FALSE_STAGE2_AND_SHIP_BLOCK_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["ship_engine_order_backlog_margin_positive", "LNG_equipment_false_stage2", "ship_block_equipment_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
10. Add tests that bridge-missing C01 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R1
completed_loop = 92
next_round = R2
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
