# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R11
scheduled_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id = DEFENSE_SPACE_SYSTEM_EXPORT_BACKLOG_BRIDGE_VS_SMALLSAT_POLICY_FALSE_STAGE2_AND_SATELLITE_GROUND_STATION_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R11_loop_95_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
```

This file is the corrected final output for this execution. The scheduler state after R10 loop 95 is R11 / loop 95. R11 allows the L10 policy/event route or the L1 policy/defense-linked route. This run uses the L1 defense-linked route and fills C03 defense export framework/backlog rather than repeating the immediately preceding R11 loop 94 C31 policy/subsidy file.

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
scheduled_round = R11
scheduled_loop = 95
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
round_sector_consistency = pass
computed_next_round = R12
computed_next_loop = 95
```

C03 is a defense-export framework and funded-program backlog archetype. A defense or space-policy headline is the uniform; the evidence is customer/order visibility, funded program, delivery cadence, export framework, system integration, margin and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG = 21 rows / 12 symbols / good-bad Stage2 11-3 / 4B-4C 0-0
top covered symbols include 079550(4), 047810(3), 065450(3), 005870(2), 103140(2), 003570(1)
previous R11 loop-89 C03 symbols avoided: 064350, 010820, 099320
previous R11 loop-91 C03 symbols avoided: 012450, 214430, 013810
previous R11 loop-94 C31 symbols avoided: 034020, 126880, 119850
previous R10 loop-95 C30 symbols avoided: 053690, 054930, 034300
previous R8 loop-95 C26 symbols avoided: 214320, 236810, 417860
```

Selected rows avoid hard duplicates and top repeated C03 symbols:

```text
272210 / Stage2-Actionable / 2024-04-23
211270 / Stage2-Actionable / 2024-01-03
451760 / Stage4B / 2024-01-11
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
| 272210 | atlas/symbol_profiles/272/272210.json | selected 2024 window clean after old 2021 CA candidate |
| 211270 | atlas/symbol_profiles/211/211270.json | no corporate-action candidate |
| 451760 | atlas/symbol_profiles/451/451760.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R11L95_C03_HANWHASYSTEMS_2024_DEFENSE_SPACE_EXPORT_BACKLOG_BRIDGE_POSITIVE | 272210 | 2024-04-23 | yes | 180 | yes | yes | true |
| R11L95_C03_APSAT_2024_SMALLSAT_POLICY_FALSE_STAGE2 | 211270 | 2024-01-03 | yes | 180 | yes | yes | true |
| R11L95_C03_CONTEC_2024_SATELLITE_GROUND_STATION_EVENT_CAP_4B | 451760 | 2024-01-11 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | DEFENSE_SPACE_SYSTEM_EXPORT_BACKLOG_BRIDGE | Positive Stage2 requires export framework, funded program/order backlog, customer quality, delivery cadence, margin and revision bridge. |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | SMALLSAT_POLICY_FALSE_STAGE2 | Small-satellite / space-policy watch without funded order and margin bridge can become false Stage2. |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | SATELLITE_GROUND_STATION_EVENT_CAP_4B | New-space / ground-station event premium should route to 4B when recurring contract and backlog bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R11L95_C03_HANWHASYSTEMS_2024_DEFENSE_SPACE_EXPORT_BACKLOG_BRIDGE_POSITIVE | 272210 | 한화시스템 | positive | Defense/space system backlog bridge produced clean MFE with controlled MAE. |
| R11L95_C03_APSAT_2024_SMALLSAT_POLICY_FALSE_STAGE2 | 211270 | AP위성 | counterexample | Small-satellite policy spike had temporary MFE but no durable export/backlog bridge. |
| R11L95_C03_CONTEC_2024_SATELLITE_GROUND_STATION_EVENT_CAP_4B | 451760 | 컨텍 | counterexample / 4B | Satellite ground-station event premium capped near the January spike and then de-rated. |

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
| Hanwha Systems defense/space export-backlog bridge | historical public/report proxy | true | true | shadow-only positive |
| AP Satellite smallsat policy false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Contec satellite ground-station event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 272210 | atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv | atlas/symbol_profiles/272/272210.json |
| 211270 | atlas/ohlcv_tradable_by_symbol_year/211/211270/2024.csv | atlas/symbol_profiles/211/211270.json |
| 451760 | atlas/ohlcv_tradable_by_symbol_year/451/451760/2024.csv | atlas/symbol_profiles/451/451760.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R11L95_C03_HANWHASYSTEMS_2024_STAGE2_ACTIONABLE_DEFENSE_SPACE_EXPORT_BACKLOG_BRIDGE | 272210 | Stage2-Actionable | 2024-04-23 | 17920 | positive | defense/space export-backlog bridge worked |
| R11L95_C03_APSAT_2024_STAGE2_FALSE_POSITIVE_SMALLSAT_POLICY_EXPORT_WATCH | 211270 | Stage2-Actionable | 2024-01-03 | 17860 | counterexample | smallsat policy false Stage2 |
| R11L95_C03_CONTEC_2024_STAGE4B_SATELLITE_GROUND_STATION_EVENT_CAP | 451760 | Stage4B | 2024-01-11 | 22750 | counterexample/4B | satellite ground-station event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R11L95_C03_HANWHASYSTEMS_2024_STAGE2_ACTIONABLE_DEFENSE_SPACE_EXPORT_BACKLOG_BRIDGE | 17920 | 14.96 | -6.25 | 25.28 | -6.25 | 25.28 | -6.25 | 2024-06-18 | 22450 | -18.49 |
| R11L95_C03_APSAT_2024_STAGE2_FALSE_POSITIVE_SMALLSAT_POLICY_EXPORT_WATCH | 17860 | 13.10 | -21.22 | 13.10 | -21.22 | 13.10 | -21.22 | 2024-01-04 | 20200 | -30.35 |
| R11L95_C03_CONTEC_2024_STAGE4B_SATELLITE_GROUND_STATION_EVENT_CAP | 22750 | 11.43 | -37.45 | 11.43 | -37.45 | 11.43 | -37.45 | 2024-01-11 | 25350 | -43.87 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C03 Stage2 needs export framework / funded program / order backlog / delivery / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing new-space / smallsat event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE space-policy rows cannot promote without durable order/backlog bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether defense/space-policy excitement becomes funded program and delivery.

| symbol | stage quality | explanation |
|---|---|---|
| 272210 | good_stage2_with_later_watch | Export/backlog and delivery bridge produced positive MFE with controlled MAE. |
| 211270 | bad_stage2 | Small-satellite policy premium lacked funded order and margin bridge. |
| 451760 | good_4B | Ground-station event premium capped at the January spike and then drew down deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 211270 smallsat false Stage2 | 0.88 | 0.88 | false Stage2 due missing export framework / funded order / margin bridge |
| 451760 satellite ground-station cap | 0.90 | 0.90 | good 4B timing after January new-space event premium |
| 272210 defense/space backlog bridge | n/a | n/a | positive Stage2, but later defense/space valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 211270 / 451760
```

No hard 4C candidate is introduced in this R11 loop 95 file. The counterexamples are event-cap / bridge-missing rows, not hard thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 defense/export/space-policy cases, Stage2 requires verified export framework, funded program/order backlog, customer visibility, delivery cadence, system-integration margin, or revision bridge. Defense, space, satellite, new-space, policy, export, radar or ground-station label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
rule = C03 should split true export-framework/funded-program/order-backlog positives from smallsat policy false Stage2 and satellite ground-station event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 16.60 | -21.64 | 0.67 | mixed; C03 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 16.60 | -21.64 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L1 export/backlog/margin bridge required | 2 | 19.19 | -13.74 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C03 bridge vs event-cap split | 2 | 19.19 | -13.74 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing defense/space policy themes as positive | 1 | 25.28 | -6.25 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 272210 defense/space bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 25.28 | -6.25 | defense_space_export_backlog_positive |
| 211270 smallsat false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 13.10 | -21.22 | smallsat_policy_false_stage2 |
| 451760 ground-station cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 11.43 | -37.45 | satellite_ground_station_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SPACE_SYSTEM_EXPORT_BACKLOG_BRIDGE_VS_SMALLSAT_POLICY_FALSE_STAGE2_AND_SATELLITE_GROUND_STATION_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C03 Hanwha Systems defense/space export-backlog positive, AP Satellite smallsat policy false Stage2, and Contec satellite ground-station event-cap 4B split while avoiding top repeated C03 symbols and previous R11/R8/R10 loop symbols."}
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
residual_error_types_found: defense_space_export_backlog_positive, smallsat_policy_false_stage2, satellite_ground_station_event_cap_4B
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
- C03 defense export/framework backlog bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,configured,C03_requires_export_framework_order_backlog_customer_delivery_margin_revision_bridge,0,"C03 Stage2 should require defense export framework, funded program/order backlog, customer visibility, delivery cadence, system-integration margin, or revision bridge, not defense/space policy label alone","Hanwha Systems positive worked; AP Satellite and Contec event/watch rows failed positive-stage promotion","R11L95_C03_HANWHASYSTEMS_2024_STAGE2_ACTIONABLE_DEFENSE_SPACE_EXPORT_BACKLOG_BRIDGE|R11L95_C03_APSAT_2024_STAGE2_FALSE_POSITIVE_SMALLSAT_POLICY_EXPORT_WATCH|R11L95_C03_CONTEC_2024_STAGE4B_SATELLITE_GROUND_STATION_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,configured,cap_bridge_missing_space_policy_and_ground_station_event_premiums_as_4B_watch,0,"Space-policy, smallsat and satellite ground-station event premiums can peak before export framework, funded program and margin bridge is proven","AP Satellite had temporary MFE then drawdown; Contec showed 4B event-cap behavior after January new-space spike","R11L95_C03_APSAT_2024_STAGE2_FALSE_POSITIVE_SMALLSAT_POLICY_EXPORT_WATCH|R11L95_C03_CONTEC_2024_STAGE4B_SATELLITE_GROUND_STATION_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,configured,block_positive_stage_when_defense_space_event_has_high_or_persistent_MAE_without_backlog_bridge,0,"High or persistent MAE after bridge-missing defense/space policy entries should block Stage2/Stage3 promotion unless customer/order backlog, delivery and margin evidence survives","AP Satellite MAE90=-21.22 and Contec MAE90=-37.45","R11L95_C03_APSAT_2024_STAGE2_FALSE_POSITIVE_SMALLSAT_POLICY_EXPORT_WATCH|R11L95_C03_CONTEC_2024_STAGE4B_SATELLITE_GROUND_STATION_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R11L95_C03_HANWHASYSTEMS_2024_DEFENSE_SPACE_EXPORT_BACKLOG_BRIDGE_POSITIVE", "symbol": "272210", "company_name": "한화시스템", "round": "R11", "loop": "95", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SPACE_SYSTEM_EXPORT_BACKLOG_BRIDGE_VS_SMALLSAT_POLICY_FALSE_STAGE2_AND_SATELLITE_GROUND_STATION_EVENT_CAP", "case_type": "structural_success_with_later_defense_space_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R11L95_C03_HANWHASYSTEMS_2024_STAGE2_ACTIONABLE_DEFENSE_SPACE_EXPORT_BACKLOG_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Defense/space system export framework, order backlog and system-integration bridge produced a clean 90D/180D MFE path with controlled MAE. C03 works when defense-policy narrative maps into export framework, customer/order visibility, program backlog, delivery cadence, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C03_positive_requires_export_framework_order_backlog_delivery_margin_revision_bridge_not_defense_policy_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2021 corporate-action candidate. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R11L95_C03_APSAT_2024_SMALLSAT_POLICY_FALSE_STAGE2", "symbol": "211270", "company_name": "AP위성", "round": "R11", "loop": "95", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SPACE_SYSTEM_EXPORT_BACKLOG_BRIDGE_VS_SMALLSAT_POLICY_FALSE_STAGE2_AND_SATELLITE_GROUND_STATION_EVENT_CAP", "case_type": "failed_rerating_smallsat_policy_export_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R11L95_C03_APSAT_2024_STAGE2_FALSE_POSITIVE_SMALLSAT_POLICY_EXPORT_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Small-satellite / space-policy watch had an early event premium but failed to prove durable export framework, funded program backlog, delivery cadence or margin revision. C03 Stage2 should not be awarded without confirmed defense/space customer order visibility, funded program, delivery and margin bridge.", "current_profile_verdict": "current_profile_false_positive_if_smallsat_policy_watch_counts_without_customer_order_backlog_delivery_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R11L95_C03_CONTEC_2024_SATELLITE_GROUND_STATION_EVENT_CAP_4B", "symbol": "451760", "company_name": "컨텍", "round": "R11", "loop": "95", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SPACE_SYSTEM_EXPORT_BACKLOG_BRIDGE_VS_SMALLSAT_POLICY_FALSE_STAGE2_AND_SATELLITE_GROUND_STATION_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R11L95_C03_CONTEC_2024_STAGE4B_SATELLITE_GROUND_STATION_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Satellite ground-station / new-space event premium capped around the January spike and then suffered deep 30D/90D/180D MAE. C03 should route bridge-missing space-policy or ground-station event premiums to 4B unless funded defense/space program, export customer, recurring service contract, delivery and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_satellite_ground_station_space_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R11L95_C03_HANWHASYSTEMS_2024_STAGE2_ACTIONABLE_DEFENSE_SPACE_EXPORT_BACKLOG_BRIDGE", "case_id": "R11L95_C03_HANWHASYSTEMS_2024_DEFENSE_SPACE_EXPORT_BACKLOG_BRIDGE_POSITIVE", "symbol": "272210", "company_name": "한화시스템", "round": "R11", "loop": "95", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SPACE_SYSTEM_EXPORT_BACKLOG_BRIDGE_VS_SMALLSAT_POLICY_FALSE_STAGE2_AND_SATELLITE_GROUND_STATION_EVENT_CAP", "sector": "defense_space_system_export_framework_backlog", "primary_archetype": "export_framework_order_backlog_delivery_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-23", "entry_date": "2024-04-23", "entry_price": 17920.0, "evidence_available_at_that_date": "defense/space system export framework, funded program/order backlog, customer visibility, system-integration delivery cadence and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["export_framework_proxy", "funded_program_backlog_proxy", "customer_quality_proxy", "delivery_cadence_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "positive_MFE90", "controlled_MAE90"], "stage4b_evidence_fields": ["later_defense_space_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv", "profile_path": "atlas/symbol_profiles/272/272210.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.96, "MFE_90D_pct": 25.28, "MFE_180D_pct": 25.28, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.25, "MAE_90D_pct": -6.25, "MAE_180D_pct": -6.25, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-18", "peak_price": 22450.0, "drawdown_after_peak_pct": -18.49, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_defense_space_valuation_4B_watch_needed", "four_b_evidence_type": ["export_framework_bridge", "funded_program_backlog", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_defense_space_export_backlog_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2021_CA", "same_entry_group_id": "R11L95_C03_272210_2024-04-23_17920", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R11L95_C03_APSAT_2024_STAGE2_FALSE_POSITIVE_SMALLSAT_POLICY_EXPORT_WATCH", "case_id": "R11L95_C03_APSAT_2024_SMALLSAT_POLICY_FALSE_STAGE2", "symbol": "211270", "company_name": "AP위성", "round": "R11", "loop": "95", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SPACE_SYSTEM_EXPORT_BACKLOG_BRIDGE_VS_SMALLSAT_POLICY_FALSE_STAGE2_AND_SATELLITE_GROUND_STATION_EVENT_CAP", "sector": "small_satellite_space_policy_export_watch", "primary_archetype": "smallsat_policy_watch_without_customer_order_backlog_delivery_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-03", "entry_date": "2024-01-03", "entry_price": 17860.0, "evidence_available_at_that_date": "small-satellite / space-defense policy watch without confirmed export framework, funded program backlog, recurring service order or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["smallsat_policy_watch", "space_defense_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["temporary_MFE_then_MAE", "customer_order_backlog_margin_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/211/211270/2024.csv", "profile_path": "atlas/symbol_profiles/211/211270.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.1, "MFE_90D_pct": 13.1, "MFE_180D_pct": 13.1, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -21.22, "MAE_90D_pct": -21.22, "MAE_180D_pct": -21.22, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-04", "peak_price": 20200.0, "drawdown_after_peak_pct": -30.35, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "smallsat_policy_watch_was_false_stage2_due_missing_customer_order_backlog_delivery_margin_bridge", "four_b_evidence_type": ["space_policy_event_premium", "bridge_missing", "temporary_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_smallsat_policy_watch_without_export_backlog_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_smallsat_policy_watch_counts_without_customer_order_backlog_delivery_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R11L95_C03_211270_2024-01-03_17860", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R11L95_C03_CONTEC_2024_STAGE4B_SATELLITE_GROUND_STATION_EVENT_CAP", "case_id": "R11L95_C03_CONTEC_2024_SATELLITE_GROUND_STATION_EVENT_CAP_4B", "symbol": "451760", "company_name": "컨텍", "round": "R11", "loop": "95", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SPACE_SYSTEM_EXPORT_BACKLOG_BRIDGE_VS_SMALLSAT_POLICY_FALSE_STAGE2_AND_SATELLITE_GROUND_STATION_EVENT_CAP", "sector": "satellite_ground_station_newspace_event_premium", "primary_archetype": "satellite_ground_station_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-11", "entry_date": "2024-01-11", "entry_price": 22750.0, "evidence_available_at_that_date": "satellite ground-station / new-space event premium after January space-policy spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["satellite_ground_station_event", "newspace_policy_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "funded_program_contract_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/451/451760/2024.csv", "profile_path": "atlas/symbol_profiles/451/451760.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.43, "MFE_90D_pct": 11.43, "MFE_180D_pct": 11.43, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -37.45, "MAE_90D_pct": -37.45, "MAE_180D_pct": -37.45, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-11", "peak_price": 25350.0, "drawdown_after_peak_pct": -43.87, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "good_full_window_4B_timing_satellite_ground_station_event_cap", "four_b_evidence_type": ["newspace_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_satellite_ground_station_newspace_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_satellite_ground_station_space_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R11L95_C03_451760_2024-01-11_22750", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L95_C03_HANWHASYSTEMS_2024_DEFENSE_SPACE_EXPORT_BACKLOG_BRIDGE_POSITIVE", "trigger_id": "R11L95_C03_HANWHASYSTEMS_2024_STAGE2_ACTIONABLE_DEFENSE_SPACE_EXPORT_BACKLOG_BRIDGE", "symbol": "272210", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 60, "customer_quality_score": 45, "policy_or_regulatory_score": 55, "valuation_repricing_score": 55, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 50, "revision_score": 50, "relative_strength_score": 65, "customer_quality_score": 60, "policy_or_regulatory_score": 65, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "defense_space_export_backlog_positive", "MFE_90D_pct": 25.28, "MAE_90D_pct": -6.25, "score_return_alignment_label": "defense_space_export_backlog_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L95_C03_APSAT_2024_SMALLSAT_POLICY_FALSE_STAGE2", "trigger_id": "R11L95_C03_APSAT_2024_STAGE2_FALSE_POSITIVE_SMALLSAT_POLICY_EXPORT_WATCH", "symbol": "211270", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "smallsat_policy_false_stage2", "MFE_90D_pct": 13.1, "MAE_90D_pct": -21.22, "score_return_alignment_label": "smallsat_policy_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_smallsat_policy_watch_counts_without_customer_order_backlog_delivery_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L95_C03_CONTEC_2024_SATELLITE_GROUND_STATION_EVENT_CAP_4B", "trigger_id": "R11L95_C03_CONTEC_2024_STAGE4B_SATELLITE_GROUND_STATION_EVENT_CAP", "symbol": "451760", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "satellite_ground_station_event_cap_4B_guard", "MFE_90D_pct": 11.43, "MAE_90D_pct": -37.45, "score_return_alignment_label": "satellite_ground_station_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_satellite_ground_station_space_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": "95", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SPACE_SYSTEM_EXPORT_BACKLOG_BRIDGE_VS_SMALLSAT_POLICY_FALSE_STAGE2_AND_SATELLITE_GROUND_STATION_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["defense_space_export_backlog_positive", "smallsat_policy_false_stage2", "satellite_ground_station_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C03 rows need explicit defense export framework, funded program/order backlog, customer visibility, delivery cadence, system-integration margin or revision bridge before positive promotion.
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
10. Add tests that bridge-missing C03 defense/space policy rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R11
completed_loop = 95
next_round = R12
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
