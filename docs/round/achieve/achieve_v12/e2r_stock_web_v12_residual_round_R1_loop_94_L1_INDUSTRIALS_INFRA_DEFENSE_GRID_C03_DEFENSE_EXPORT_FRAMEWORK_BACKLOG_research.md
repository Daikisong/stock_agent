# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R1
scheduled_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id = NAVAL_ENGINE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_SPACE_DEFENSE_COMPONENT_FALSE_STAGE2_AND_FORGING_MUNITION_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R1_loop_94_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
```

This file is the corrected final output for this execution. The scheduler state after R13 loop 93 is R1 / loop 94. R1 is the L1 industrials/infra/defense/grid round, and this run fills C03 defense export framework/backlog rather than repeating the immediately preceding R1 loop 93 C05 EPC file.

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
scheduled_loop = 94
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
round_sector_consistency = pass
computed_next_round = R2
computed_next_loop = 94
```

C03 currently has good Stage2 coverage but no explicit 4B/4C row in the no-repeat snapshot. This loop therefore prioritizes a positive export/backlog bridge plus a bridge-missing false Stage2 and a 4B event-cap row.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG = 21 rows / 12 symbols / good-bad Stage2 11-3 / 4B-4C 0-0
top covered symbols include 079550(4), 047810(3), 065450(3), 005870(2), 103140(2), 003570(1)
previous R1 loop-91 C02 symbols avoided: C02 family from prior loop
previous R1 loop-92 C01 symbols avoided: C01 family from prior loop
previous R1 loop-93 C05 symbols avoided: 100840, 094820, 010960
previous R11 loop-91 C03 symbols avoided: 012450, 214430, 013810
previous R13 loop-93 review-only rows do_not_count_as_new_case
```

Selected rows avoid hard duplicates and top repeated C03 symbols:

```text
077970 / Stage2-Actionable / 2024-01-24
361390 / Stage2-Actionable / 2024-01-24
024740 / Stage4B / 2024-01-17
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
| 077970 | atlas/symbol_profiles/077/077970.json | selected 2024 180D window clean before 2025-04-21 CA candidate |
| 361390 | atlas/symbol_profiles/361/361390.json | selected 2024 window clean after old 2021 CA candidates |
| 024740 | atlas/symbol_profiles/024/024740.json | selected 2024 window clean after old 2002~2018 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R1L94_C03_STXENGINE_2024_NAVAL_ENGINE_EXPORT_FRAMEWORK_BACKLOG_POSITIVE | 077970 | 2024-01-24 | yes | 180 | yes | yes | true |
| R1L94_C03_XENOCO_2024_SPACE_DEFENSE_COMPONENT_HEADLINE_FALSE_STAGE2 | 361390 | 2024-01-24 | yes | 180 | yes | yes | true |
| R1L94_C03_HANILFORGING_2024_MUNITION_FORGING_DEFENSE_EVENT_CAP_4B | 024740 | 2024-01-17 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | NAVAL_ENGINE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE | Positive Stage2 requires export framework, platform subsystem order visibility, customer quality, delivery cadence, margin and revision bridge. |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | SPACE_DEFENSE_COMPONENT_FALSE_STAGE2 | Space/defense component headline without prime/export/order bridge can become false Stage2. |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | FORGING_MUNITION_EVENT_CAP_4B | Munition/forging defense event premium should route to 4B when order/capacity/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R1L94_C03_STXENGINE_2024_NAVAL_ENGINE_EXPORT_FRAMEWORK_BACKLOG_POSITIVE | 077970 | STX엔진 | positive | Naval/defense engine export/backlog bridge produced strong 90D/180D MFE with shallow MAE. |
| R1L94_C03_XENOCO_2024_SPACE_DEFENSE_COMPONENT_HEADLINE_FALSE_STAGE2 | 361390 | 제노코 | counterexample | Space/defense component headline had almost no MFE and severe later MAE. |
| R1L94_C03_HANILFORGING_2024_MUNITION_FORGING_DEFENSE_EVENT_CAP_4B | 024740 | 한일단조 | counterexample / 4B | Munition/forging defense event premium capped on the January spike. |

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
| STX Engine naval engine export/backlog bridge | historical public/report proxy | true | true | shadow-only positive |
| Xenoco space-defense component false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Hanil Forging munition/forging event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 077970 | atlas/ohlcv_tradable_by_symbol_year/077/077970/2024.csv | atlas/symbol_profiles/077/077970.json |
| 361390 | atlas/ohlcv_tradable_by_symbol_year/361/361390/2024.csv | atlas/symbol_profiles/361/361390.json |
| 024740 | atlas/ohlcv_tradable_by_symbol_year/024/024740/2024.csv | atlas/symbol_profiles/024/024740.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R1L94_C03_STXENGINE_2024_STAGE2_ACTIONABLE_NAVAL_ENGINE_EXPORT_BACKLOG_BRIDGE | 077970 | Stage2-Actionable | 2024-01-24 | 11620 | positive | naval engine export/backlog bridge worked |
| R1L94_C03_XENOCO_2024_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_COMPONENT_HEADLINE | 361390 | Stage2-Actionable | 2024-01-24 | 17940 | counterexample | space-defense component headline false Stage2 |
| R1L94_C03_HANILFORGING_2024_STAGE4B_MUNITION_FORGING_DEFENSE_EVENT_CAP | 024740 | Stage4B | 2024-01-17 | 2755 | counterexample/4B | munition/forging event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1L94_C03_STXENGINE_2024_STAGE2_ACTIONABLE_NAVAL_ENGINE_EXPORT_BACKLOG_BRIDGE | 11620 | 12.74 | -1.38 | 35.37 | -1.38 | 60.59 | -1.38 | 2024-06-25 | 18660 | -16.45 |
| R1L94_C03_XENOCO_2024_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_COMPONENT_HEADLINE | 17940 | 1.34 | -14.72 | 1.34 | -14.72 | 1.34 | -37.07 | 2024-01-24 | 18180 | -37.90 |
| R1L94_C03_HANILFORGING_2024_STAGE4B_MUNITION_FORGING_DEFENSE_EVENT_CAP | 2755 | 7.08 | -15.43 | 7.08 | -19.78 | 7.08 | -23.23 | 2024-01-17 | 2950 | -28.31 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C03 Stage2 needs export framework / order backlog / platform-prime linkage / delivery / customer / margin bridge |
| local_4b_watch_guard | strengthen: defense parts/munition event premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: high or persistent MAE rows cannot promote without durable export-backlog bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is defense export/backlog bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 077970 | good_stage2_with_later_watch | Export/backlog bridge produced strong MFE with shallow early MAE, but later valuation watch remains necessary. |
| 361390 | bad_stage2 | Space-defense component headline lacked order/export bridge and then de-rated. |
| 024740 | good_4B | Munition/forging defense event premium capped at the January spike and bled down. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 361390 space-defense false Stage2 | 0.99 | 0.99 | false Stage2 due missing export/order/margin bridge |
| 024740 munition/forging cap | 0.93 | 0.93 | good full-window 4B timing after January defense spike |
| 077970 naval engine bridge | n/a | n/a | positive Stage2, but later defense-export valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 361390 / 024740
```

No hard 4C candidate is proposed. R1 loop 94 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 defense export framework/backlog cases, Stage2 requires verified export framework, order/backlog, prime/platform linkage, delivery cadence, customer quality, margin, or revision bridge. Defense, space, satellite, munition, forging, engine, or geopolitical headline alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
rule = C03 should split true export/backlog/delivery positives from space-defense headline false Stage2 and munition/forging event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 14.60 | -11.96 | 0.67 | mixed; C03 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 14.60 | -11.96 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L1 export/backlog/margin bridge required | 2 | 18.36 | -8.05 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C03 bridge vs event-cap split | 2 | 18.36 | -8.05 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing defense headlines as positive | 1 | 35.37 | -1.38 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 077970 naval engine backlog bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 35.37 | -1.38 | naval_engine_export_backlog_positive |
| 361390 space-defense false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 1.34 | -14.72 | space_defense_component_headline_false_stage2 |
| 024740 munition/forging cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 7.08 | -19.78 | munition_forging_defense_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "NAVAL_ENGINE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_SPACE_DEFENSE_COMPONENT_FALSE_STAGE2_AND_FORGING_MUNITION_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C03 naval/defense engine export-backlog positive, space-defense component headline false Stage2, and munition/forging event-cap 4B split while avoiding top repeated C03 symbols."}
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
residual_error_types_found: naval_engine_export_backlog_positive, space_defense_component_headline_false_stage2, munition_forging_defense_event_cap_4B
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
- C03 defense export framework/backlog bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,configured,C03_requires_export_framework_order_backlog_delivery_customer_margin_revision_bridge,0,"C03 Stage2 should require export framework, confirmed order/backlog, prime/platform linkage, delivery cadence, customer quality, margin, or revision bridge, not defense/space/munition label alone","STX Engine positive worked; Xenoco and Hanil Forging event/headline rows failed positive-stage promotion","R1L94_C03_STXENGINE_2024_STAGE2_ACTIONABLE_NAVAL_ENGINE_EXPORT_BACKLOG_BRIDGE|R1L94_C03_XENOCO_2024_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_COMPONENT_HEADLINE|R1L94_C03_HANILFORGING_2024_STAGE4B_MUNITION_FORGING_DEFENSE_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,configured,cap_bridge_missing_defense_component_and_munition_event_premiums_as_4B_watch,0,"Defense parts/space/munition event premiums can peak before export framework and margin bridge is proven","Xenoco had near-zero MFE and deep MAE180; Hanil Forging showed 4B event-cap behavior after January defense spike","R1L94_C03_XENOCO_2024_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_COMPONENT_HEADLINE|R1L94_C03_HANILFORGING_2024_STAGE4B_MUNITION_FORGING_DEFENSE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,configured,block_positive_stage_when_defense_headline_has_high_or_persistent_MAE_without_export_backlog_bridge,0,"High or persistent MAE after bridge-missing defense entries should block Stage2/Stage3 promotion unless export, order, backlog, customer and margin evidence survives","Xenoco MAE180=-37.07 and Hanil Forging MAE180=-23.23","R1L94_C03_XENOCO_2024_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_COMPONENT_HEADLINE|R1L94_C03_HANILFORGING_2024_STAGE4B_MUNITION_FORGING_DEFENSE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R1L94_C03_STXENGINE_2024_NAVAL_ENGINE_EXPORT_FRAMEWORK_BACKLOG_POSITIVE", "symbol": "077970", "company_name": "STX엔진", "round": "R1", "loop": "94", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "NAVAL_ENGINE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_SPACE_DEFENSE_COMPONENT_FALSE_STAGE2_AND_FORGING_MUNITION_EVENT_CAP", "case_type": "structural_success_with_later_defense_export_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R1L94_C03_STXENGINE_2024_STAGE2_ACTIONABLE_NAVAL_ENGINE_EXPORT_BACKLOG_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Naval/defense engine export framework and backlog bridge produced strong 30D/90D/180D MFE with shallow entry MAE. C03 works when defense export narrative maps into executable platform program, engine/subsystem order visibility, customer quality, delivery cadence and margin/revision bridge.", "current_profile_verdict": "current_profile_kept_but_C03_positive_requires_export_framework_order_backlog_delivery_margin_bridge_not_defense_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean before 2025-04-21 corporate-action candidate. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R1L94_C03_XENOCO_2024_SPACE_DEFENSE_COMPONENT_HEADLINE_FALSE_STAGE2", "symbol": "361390", "company_name": "제노코", "round": "R1", "loop": "94", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "NAVAL_ENGINE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_SPACE_DEFENSE_COMPONENT_FALSE_STAGE2_AND_FORGING_MUNITION_EVENT_CAP", "case_type": "failed_rerating_space_defense_component_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R1L94_C03_XENOCO_2024_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_COMPONENT_HEADLINE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Space/defense component headline watch had near-zero forward MFE and later severe 180D MAE. C03 Stage2 should not be awarded without export framework, prime-contractor linkage, order/backlog, production delivery and margin/revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_space_defense_component_headline_counts_without_export_order_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2021 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R1L94_C03_HANILFORGING_2024_MUNITION_FORGING_DEFENSE_EVENT_CAP_4B", "symbol": "024740", "company_name": "한일단조", "round": "R1", "loop": "94", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "NAVAL_ENGINE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_SPACE_DEFENSE_COMPONENT_FALSE_STAGE2_AND_FORGING_MUNITION_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R1L94_C03_HANILFORGING_2024_STAGE4B_MUNITION_FORGING_DEFENSE_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Munition/forging defense event premium capped on the January spike and then bled down through the 180D window. C03 should route bridge-missing defense parts/event premiums to 4B unless confirmed export framework, purchase order, capacity utilization, customer quality and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_munition_forging_defense_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2002~2018 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R1L94_C03_STXENGINE_2024_STAGE2_ACTIONABLE_NAVAL_ENGINE_EXPORT_BACKLOG_BRIDGE", "case_id": "R1L94_C03_STXENGINE_2024_NAVAL_ENGINE_EXPORT_FRAMEWORK_BACKLOG_POSITIVE", "symbol": "077970", "company_name": "STX엔진", "round": "R1", "loop": "94", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "NAVAL_ENGINE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_SPACE_DEFENSE_COMPONENT_FALSE_STAGE2_AND_FORGING_MUNITION_EVENT_CAP", "sector": "naval_defense_engine_export_framework_backlog", "primary_archetype": "defense_platform_subsystem_export_backlog_delivery_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 11620.0, "evidence_available_at_that_date": "naval/defense engine export-framework watch, platform subsystem order visibility, customer quality, delivery cadence and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["export_framework_proxy", "platform_subsystem_order_visibility", "customer_quality_proxy", "delivery_cadence_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "strong_MFE90", "very_high_MFE180", "shallow_MAE90"], "stage4b_evidence_fields": ["later_defense_export_valuation_watch", "post_peak_program_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/077/077970/2024.csv", "profile_path": "atlas/symbol_profiles/077/077970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.74, "MFE_90D_pct": 35.37, "MFE_180D_pct": 60.59, "MFE_1Y_pct": "contaminated_or_unavailable_due_2025-04-21_CA_candidate", "MFE_2Y_pct": "contaminated_or_unavailable_due_2025-04-21_CA_candidate", "MAE_30D_pct": -1.38, "MAE_90D_pct": -1.38, "MAE_180D_pct": -1.38, "MAE_1Y_pct": "contaminated_or_unavailable_due_2025-04-21_CA_candidate", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-25", "peak_price": 18660.0, "drawdown_after_peak_pct": -16.45, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_defense_export_valuation_4B_watch_needed", "four_b_evidence_type": ["export_framework", "backlog_delivery_bridge", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_naval_engine_export_backlog_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_before_2025-04-21_CA_candidate", "same_entry_group_id": "R1L94_C03_077970_2024-01-24_11620", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L94_C03_XENOCO_2024_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_COMPONENT_HEADLINE", "case_id": "R1L94_C03_XENOCO_2024_SPACE_DEFENSE_COMPONENT_HEADLINE_FALSE_STAGE2", "symbol": "361390", "company_name": "제노코", "round": "R1", "loop": "94", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "NAVAL_ENGINE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_SPACE_DEFENSE_COMPONENT_FALSE_STAGE2_AND_FORGING_MUNITION_EVENT_CAP", "sector": "space_defense_component_headline_watch", "primary_archetype": "space_defense_component_watch_without_export_order_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 17940.0, "evidence_available_at_that_date": "space/defense component headline and satellite-defense expectation proxy without confirmed export framework or order/backlog bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["space_defense_component_headline", "satellite_defense_expectation", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["near_zero_MFE90", "deep_MAE180", "export_order_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361390/2024.csv", "profile_path": "atlas/symbol_profiles/361/361390.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.34, "MFE_90D_pct": 1.34, "MFE_180D_pct": 1.34, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -14.72, "MAE_90D_pct": -14.72, "MAE_180D_pct": -37.07, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-24", "peak_price": 18180.0, "drawdown_after_peak_pct": -37.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.99, "four_b_full_window_peak_proximity": 0.99, "four_b_timing_verdict": "space_defense_component_headline_was_false_stage2_due_missing_export_order_margin_bridge", "four_b_evidence_type": ["space_defense_headline_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_space_defense_component_headline_without_export_order_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_space_defense_component_headline_counts_without_export_order_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2021_CA", "same_entry_group_id": "R1L94_C03_361390_2024-01-24_17940", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L94_C03_HANILFORGING_2024_STAGE4B_MUNITION_FORGING_DEFENSE_EVENT_CAP", "case_id": "R1L94_C03_HANILFORGING_2024_MUNITION_FORGING_DEFENSE_EVENT_CAP_4B", "symbol": "024740", "company_name": "한일단조", "round": "R1", "loop": "94", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "NAVAL_ENGINE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_SPACE_DEFENSE_COMPONENT_FALSE_STAGE2_AND_FORGING_MUNITION_EVENT_CAP", "sector": "munition_forging_defense_event_premium", "primary_archetype": "munition_forging_defense_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-17", "entry_date": "2024-01-17", "entry_price": 2755.0, "evidence_available_at_that_date": "munition/forging defense event premium after January defense-theme spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["munition_forging_defense_event", "defense_export_theme_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE180", "export_order_capacity_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024740/2024.csv", "profile_path": "atlas/symbol_profiles/024/024740.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.08, "MFE_90D_pct": 7.08, "MFE_180D_pct": 7.08, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.43, "MAE_90D_pct": -19.78, "MAE_180D_pct": -23.23, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-17", "peak_price": 2950.0, "drawdown_after_peak_pct": -28.31, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "good_full_window_4B_timing_munition_forging_defense_event_cap", "four_b_evidence_type": ["munition_defense_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_munition_forging_defense_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_munition_forging_defense_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2002_2018_CA", "same_entry_group_id": "R1L94_C03_024740_2024-01-17_2755", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L94_C03_STXENGINE_2024_NAVAL_ENGINE_EXPORT_FRAMEWORK_BACKLOG_POSITIVE", "trigger_id": "R1L94_C03_STXENGINE_2024_STAGE2_ACTIONABLE_NAVAL_ENGINE_EXPORT_BACKLOG_BRIDGE", "symbol": "077970", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 50, "backlog_visibility_score": 60, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 55, "policy_or_regulatory_score": 55, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "naval_engine_export_backlog_positive", "MFE_90D_pct": 35.37, "MAE_90D_pct": -1.38, "score_return_alignment_label": "naval_engine_export_backlog_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L94_C03_XENOCO_2024_SPACE_DEFENSE_COMPONENT_HEADLINE_FALSE_STAGE2", "trigger_id": "R1L94_C03_XENOCO_2024_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_COMPONENT_HEADLINE", "symbol": "361390", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "space_defense_component_headline_false_stage2", "MFE_90D_pct": 1.34, "MAE_90D_pct": -14.72, "score_return_alignment_label": "space_defense_component_headline_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_space_defense_component_headline_counts_without_export_order_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L94_C03_HANILFORGING_2024_MUNITION_FORGING_DEFENSE_EVENT_CAP_4B", "trigger_id": "R1L94_C03_HANILFORGING_2024_STAGE4B_MUNITION_FORGING_DEFENSE_EVENT_CAP", "symbol": "024740", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "munition_forging_defense_event_cap_4B_guard", "MFE_90D_pct": 7.08, "MAE_90D_pct": -19.78, "score_return_alignment_label": "munition_forging_defense_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_munition_forging_defense_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": "94", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "NAVAL_ENGINE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_SPACE_DEFENSE_COMPONENT_FALSE_STAGE2_AND_FORGING_MUNITION_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["naval_engine_export_backlog_positive", "space_defense_component_headline_false_stage2", "munition_forging_defense_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C03 rows need explicit export framework, order/backlog, platform-prime linkage, delivery, customer quality or margin bridge before positive promotion.
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
10. Add tests that bridge-missing C03 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R1
completed_loop = 94
next_round = R2
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
