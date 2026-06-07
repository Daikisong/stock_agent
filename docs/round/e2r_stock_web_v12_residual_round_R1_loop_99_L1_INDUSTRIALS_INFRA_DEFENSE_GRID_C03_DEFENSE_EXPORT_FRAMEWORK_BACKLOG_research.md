# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R1
scheduled_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id = MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_AIRCRAFT_EXPORT_FRAMEWORK_FALSE_STAGE2_AND_AMMUNITION_EVENT_CAP
loop_objective = priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | defense_export_backlog_delivery_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R1_loop_99_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. Priority 0 has been locally supplemented through C23, so the run moves to Priority 1. C03 is the first Priority 1 archetype and still needs 20 rows to reach the 50-row practical calibration zone. Since R1 loop98 was already used locally for C01, this file uses R1 loop99 to avoid local filename/round-loop collision.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_2_rolling_calibrated
previous_baseline_reference = e2r_2_1_stock_web_calibrated
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
defense_export_backlog_delivery_margin_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R1
scheduled_loop = 99
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C03 is a defense export framework / backlog archetype. The export framework is the diplomatic handshake; the usable signal is signed backlog, delivery schedule, customer quality, capacity, margin and revision becoming the signed contract’s heartbeat.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG = 30 rows / Priority 1
top covered C03 symbols avoided: 012450, 064350, 099320, 272210, 010820, 013810
recent local Priority 0 artifacts accounted for: C08, C09, C01, C07, C06, C10, C14, C11, C02, C13, C19, C27, C12, C24, C28, C17, C23
```

Selected rows avoid hard duplicates and add new C03 trigger families:

```text
079550 / Stage2-Actionable / 2024-02-14
047810 / Stage2-Actionable / 2024-01-03
103140 / Stage4B / 2024-05-02
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
| 079550 | atlas/symbol_profiles/079/079550.json | no corporate-action candidate |
| 047810 | atlas/symbol_profiles/047/047810.json | no corporate-action candidate |
| 103140 | atlas/symbol_profiles/103/103140.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R1L99_C03_LIGNEX1_2024_MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_POSITIVE | 079550 | 2024-02-14 | yes | 180 | yes | yes | true |
| R1L99_C03_KAI_2024_AIRCRAFT_EXPORT_FRAMEWORK_LOW_MFE_FALSE_STAGE2 | 047810 | 2024-01-03 | yes | 180 | yes | yes | true |
| R1L99_C03_POONGSAN_2024_AMMUNITION_EXPORT_EVENT_CAP_4B | 103140 | 2024-05-02 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE | Positive Stage2 requires signed export backlog, delivery schedule, customer quality, production capacity, margin and revision bridge. |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | AIRCRAFT_EXPORT_FRAMEWORK_FALSE_STAGE2 | Aircraft export framework watch without final contract and delivery/margin bridge can become false Stage2. |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | AMMUNITION_EXPORT_EVENT_CAP_4B | Ammunition export event premium should route to 4B when signed backlog/delivery/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R1L99_C03_LIGNEX1_2024_MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_POSITIVE | 079550 | LIG넥스원 | positive | Missile/export backlog bridge produced strong MFE through 30D/90D/180D. |
| R1L99_C03_KAI_2024_AIRCRAFT_EXPORT_FRAMEWORK_LOW_MFE_FALSE_STAGE2 | 047810 | 한국항공우주 | counterexample | Aircraft export framework watch had low MFE and meaningful early MAE without final contract/delivery bridge. |
| R1L99_C03_POONGSAN_2024_AMMUNITION_EXPORT_EVENT_CAP_4B | 103140 | 풍산 | counterexample / 4B | Ammunition/export event premium capped after the May spike and then sold down. |

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
| LIG Nex1 missile export backlog/delivery bridge | historical public/report proxy | true | true | shadow-only positive |
| KAI aircraft export framework false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Poongsan ammunition export event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 079550 | atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv | atlas/symbol_profiles/079/079550.json |
| 047810 | atlas/ohlcv_tradable_by_symbol_year/047/047810/2024.csv | atlas/symbol_profiles/047/047810.json |
| 103140 | atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv | atlas/symbol_profiles/103/103140.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R1L99_C03_LIGNEX1_2024_STAGE2_ACTIONABLE_MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE | 079550 | Stage2-Actionable | 2024-02-14 | 127000 | positive | defense export backlog/delivery bridge worked |
| R1L99_C03_KAI_2024_STAGE2_FALSE_POSITIVE_AIRCRAFT_EXPORT_FRAMEWORK_WATCH | 047810 | Stage2-Actionable | 2024-01-03 | 54600 | counterexample | aircraft export framework false Stage2 |
| R1L99_C03_POONGSAN_2024_STAGE4B_AMMUNITION_EXPORT_EVENT_CAP | 103140 | Stage4B | 2024-05-02 | 72700 | counterexample/4B | ammunition export event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1L99_C03_LIGNEX1_2024_STAGE2_ACTIONABLE_MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE | 127000 | 50.63 | -9.13 | 72.83 | -9.13 | 96.06 | -9.13 | 2024-07-17 | 249000 | -32.32 |
| R1L99_C03_KAI_2024_STAGE2_FALSE_POSITIVE_AIRCRAFT_EXPORT_FRAMEWORK_WATCH | 54600 | 3.30 | -12.45 | 3.30 | -12.45 | 8.97 | -12.45 | 2024-05-28 | 59500 | -18.24 |
| R1L99_C03_POONGSAN_2024_STAGE4B_AMMUNITION_EXPORT_EVENT_CAP | 72700 | 6.46 | -15.54 | 6.46 | -23.52 | 6.46 | -23.52 | 2024-05-07 | 77400 | -28.17 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C03 Stage2 needs signed export backlog / delivery schedule / export-customer quality / production capacity / margin / revision bridge |
| defense_export_backlog_delivery_margin_guardrail | strengthen: defense export framework label alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing aircraft export and ammunition premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C03 rows cannot promote without durable delivery/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether defense export narrative becomes signed backlog, delivery and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 079550 | good_stage2_with_later_watch | Export backlog/delivery bridge produced strong MFE, but later valuation watch remains necessary. |
| 047810 | bad_stage2 | Aircraft export framework watch lacked final contract/delivery bridge and produced low MFE. |
| 103140 | good_4B | Ammunition/export event premium peaked near May high and later drew down. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 047810 aircraft export false Stage2 | 0.92 | 0.92 | false Stage2 due missing final contract / delivery / margin bridge |
| 103140 ammunition export event cap | 0.94 | 0.94 | good 4B timing after ammunition/export event premium |
| 079550 missile export backlog bridge | n/a | n/a | positive Stage2, but later defense-export valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 047810 / 103140
```

No hard 4C candidate is introduced in this C03 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 defense export framework cases, Stage2 requires verified signed export backlog, delivery schedule, export-customer quality, production capacity, margin and revision bridge. Defense export framework, aircraft export, ammunition export, geopolitical demand or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
rule = C03 should split true signed backlog/delivery/margin positives from aircraft-framework false Stage2 and ammunition event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 27.53 | -15.03 | 0.67 | mixed; C03 backlog/delivery bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 27.53 | -15.03 | 0.67 | weaker C03 bridge split |
| P1 sector_specific_candidate_profile | L1 signed backlog/delivery/margin bridge required | 2 | 38.07 | -10.79 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C03 bridge vs event-cap split | 2 | 38.07 | -10.79 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing defense export themes as positive | 1 | 72.83 | -9.13 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 079550 missile export bridge | 66 | Stage2-Watch | 81 | Stage2-Actionable | 72.83 | -9.13 | defense_export_backlog_positive |
| 047810 aircraft export false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 3.30 | -12.45 | aircraft_export_framework_false_stage2 |
| 103140 ammunition export cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 6.46 | -23.52 | ammunition_export_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_AIRCRAFT_EXPORT_FRAMEWORK_FALSE_STAGE2_AND_AMMUNITION_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Priority 0 is locally supplemented through C23. C03 is the first Priority 1 archetype and still needs 20 rows to reach 50. This run adds LIG Nex1, KAI, and Poongsan while avoiding top-covered C03 symbols 012450, 064350, 099320, 272210, 010820 and 013810."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, defense_export_backlog_delivery_margin_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: defense_export_backlog_positive, aircraft_export_framework_false_stage2, ammunition_export_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, defense_export_backlog_delivery_margin_guardrail, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: priority1_canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C03 defense export framework backlog bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,configured,C03_requires_signed_backlog_delivery_schedule_customer_quality_capacity_margin_revision_bridge,0,"C03 Stage2 should require signed export backlog, delivery schedule, export-customer quality, production capacity, margin and revision bridge, not defense export framework label alone","LIG Nex1 positive worked; KAI and Poongsan event/watch rows failed positive-stage promotion","R1L99_C03_LIGNEX1_2024_STAGE2_ACTIONABLE_MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE|R1L99_C03_KAI_2024_STAGE2_FALSE_POSITIVE_AIRCRAFT_EXPORT_FRAMEWORK_WATCH|R1L99_C03_POONGSAN_2024_STAGE4B_AMMUNITION_EXPORT_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,configured,cap_bridge_missing_aircraft_export_and_ammunition_event_premiums_as_4B_watch,0,"Aircraft export framework and ammunition export premiums can peak before final contract, delivery cadence and margin bridge is proven","KAI had low MFE and meaningful MAE after early-January aircraft export watch; Poongsan showed 4B event-cap behavior after May ammunition/export premium","R1L99_C03_KAI_2024_STAGE2_FALSE_POSITIVE_AIRCRAFT_EXPORT_FRAMEWORK_WATCH|R1L99_C03_POONGSAN_2024_STAGE4B_AMMUNITION_EXPORT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,configured,block_positive_stage_when_defense_export_theme_has_high_or_persistent_MAE_without_delivery_margin_bridge,0,"High or persistent MAE after bridge-missing C03 entries should block Stage2/Stage3 promotion unless signed backlog, delivery and margin evidence survives","KAI MAE90=-12.45 and Poongsan MAE90=-23.52","R1L99_C03_KAI_2024_STAGE2_FALSE_POSITIVE_AIRCRAFT_EXPORT_FRAMEWORK_WATCH|R1L99_C03_POONGSAN_2024_STAGE4B_AMMUNITION_EXPORT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R1L99_C03_LIGNEX1_2024_MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_POSITIVE", "symbol": "079550", "company_name": "LIG넥스원", "round": "R1", "loop": "99", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_AIRCRAFT_EXPORT_FRAMEWORK_FALSE_STAGE2_AND_AMMUNITION_EVENT_CAP", "case_type": "structural_success_with_later_defense_export_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R1L99_C03_LIGNEX1_2024_STAGE2_ACTIONABLE_MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Missile / precision-guided weapon export framework and delivery-backlog bridge produced strong 30D/90D/180D MFE after the February breakout. C03 works when defense-export framework is tied to signed order backlog, delivery schedule, export-customer quality, production capacity, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C03_positive_requires_signed_backlog_delivery_schedule_customer_quality_capacity_margin_revision_bridge_not_defense_export_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R1L99_C03_KAI_2024_AIRCRAFT_EXPORT_FRAMEWORK_LOW_MFE_FALSE_STAGE2", "symbol": "047810", "company_name": "한국항공우주", "round": "R1", "loop": "99", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_AIRCRAFT_EXPORT_FRAMEWORK_FALSE_STAGE2_AND_AMMUNITION_EVENT_CAP", "case_type": "failed_rerating_aircraft_export_framework_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R1L99_C03_KAI_2024_STAGE2_FALSE_POSITIVE_AIRCRAFT_EXPORT_FRAMEWORK_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Aircraft-export framework watch at the early-January high had low forward MFE and meaningful early MAE. C03 Stage2 should not be awarded without final export contract, delivery slot, advance payment, backlog conversion, program margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_aircraft_export_framework_watch_counts_without_final_contract_delivery_backlog_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R1L99_C03_POONGSAN_2024_AMMUNITION_EXPORT_EVENT_CAP_4B", "symbol": "103140", "company_name": "풍산", "round": "R1", "loop": "99", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_AIRCRAFT_EXPORT_FRAMEWORK_FALSE_STAGE2_AND_AMMUNITION_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R1L99_C03_POONGSAN_2024_STAGE4B_AMMUNITION_EXPORT_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Ammunition/defense export event premium around the May spike capped before a sharp drawdown. C03 should route bridge-missing ammunition/export premiums to 4B unless signed export order, delivery cadence, raw-material pass-through, production capacity, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_ammunition_export_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R1L99_C03_LIGNEX1_2024_STAGE2_ACTIONABLE_MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE", "case_id": "R1L99_C03_LIGNEX1_2024_MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_POSITIVE", "symbol": "079550", "company_name": "LIG넥스원", "round": "R1", "loop": "99", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_AIRCRAFT_EXPORT_FRAMEWORK_FALSE_STAGE2_AND_AMMUNITION_EVENT_CAP", "sector": "missile_precision_weapon_export_backlog_delivery_margin", "primary_archetype": "signed_backlog_delivery_schedule_customer_quality_capacity_margin_revision_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | defense_export_backlog_delivery_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-14", "entry_date": "2024-02-14", "entry_price": 127000.0, "evidence_available_at_that_date": "missile / precision-guided weapon export framework, signed-order backlog, delivery schedule, export-customer quality and margin/revision bridge proxy after February breakout; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["signed_export_backlog_proxy", "delivery_schedule_proxy", "export_customer_quality_proxy", "production_capacity_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "very_strong_MFE90", "very_strong_MFE180"], "stage4b_evidence_fields": ["later_defense_export_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv", "profile_path": "atlas/symbol_profiles/079/079550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 50.63, "MFE_90D_pct": 72.83, "MFE_180D_pct": 96.06, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -9.13, "MAE_90D_pct": -9.13, "MAE_180D_pct": -9.13, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-17", "peak_price": 249000.0, "drawdown_after_peak_pct": -32.32, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_defense_export_valuation_4B_watch_needed", "four_b_evidence_type": ["defense_export_backlog_bridge", "delivery_margin", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_defense_export_backlog_delivery_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R1L99_C03_079550_2024-02-14_127000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L99_C03_KAI_2024_STAGE2_FALSE_POSITIVE_AIRCRAFT_EXPORT_FRAMEWORK_WATCH", "case_id": "R1L99_C03_KAI_2024_AIRCRAFT_EXPORT_FRAMEWORK_LOW_MFE_FALSE_STAGE2", "symbol": "047810", "company_name": "한국항공우주", "round": "R1", "loop": "99", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_AIRCRAFT_EXPORT_FRAMEWORK_FALSE_STAGE2_AND_AMMUNITION_EVENT_CAP", "sector": "aircraft_export_framework_delivery_margin_watch", "primary_archetype": "aircraft_export_watch_without_final_contract_delivery_backlog_margin_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | defense_export_backlog_delivery_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-03", "entry_date": "2024-01-03", "entry_price": 54600.0, "evidence_available_at_that_date": "aircraft export framework / FA-50 or aerospace-defense export watch without confirmed final contract, delivery slot, advance payment, backlog conversion, program margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["aircraft_export_framework_watch", "defense_export_theme", "relative_strength_high"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "meaningful_MAE30", "final_contract_delivery_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047810/2024.csv", "profile_path": "atlas/symbol_profiles/047/047810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.3, "MFE_90D_pct": 3.3, "MFE_180D_pct": 8.97, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -12.45, "MAE_90D_pct": -12.45, "MAE_180D_pct": -12.45, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-28", "peak_price": 59500.0, "drawdown_after_peak_pct": -18.24, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "aircraft_export_framework_watch_was_false_stage2_due_missing_final_contract_delivery_margin_revision_bridge", "four_b_evidence_type": ["aircraft_export_framework_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_aircraft_export_framework_without_delivery_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_aircraft_export_framework_watch_counts_without_final_contract_delivery_backlog_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R1L99_C03_047810_2024-01-03_54600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L99_C03_POONGSAN_2024_STAGE4B_AMMUNITION_EXPORT_EVENT_CAP", "case_id": "R1L99_C03_POONGSAN_2024_AMMUNITION_EXPORT_EVENT_CAP_4B", "symbol": "103140", "company_name": "풍산", "round": "R1", "loop": "99", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_AIRCRAFT_EXPORT_FRAMEWORK_FALSE_STAGE2_AND_AMMUNITION_EVENT_CAP", "sector": "ammunition_export_event_backlog_margin_watch", "primary_archetype": "ammunition_export_event_cap_4B", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | defense_export_backlog_delivery_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-05-02", "entry_date": "2024-05-02", "entry_price": 72700.0, "evidence_available_at_that_date": "ammunition / defense export event premium without confirmed signed export order, delivery cadence, raw-material pass-through, production capacity, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["ammunition_export_event", "defense_export_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "high_MAE90", "delivery_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.46, "MFE_90D_pct": 6.46, "MFE_180D_pct": 6.46, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.54, "MAE_90D_pct": -23.52, "MAE_180D_pct": -23.52, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-07", "peak_price": 77400.0, "drawdown_after_peak_pct": -28.17, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing_ammunition_export_event_cap_due_missing_delivery_margin_bridge", "four_b_evidence_type": ["ammunition_export_event_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_ammunition_export_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_ammunition_export_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R1L99_C03_103140_2024-05-02_72700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R1L99_C03_LIGNEX1_2024_MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R1L99_C03_LIGNEX1_2024_STAGE2_ACTIONABLE_MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE", "symbol": "079550", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 50, "policy_or_regulatory_score": 40, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 65, "backlog_visibility_score": 65, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 80, "customer_quality_score": 65, "policy_or_regulatory_score": 45, "valuation_repricing_score": 45, "execution_risk_score": 30, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 81, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "missile_export_backlog_delivery_margin_positive", "MFE_90D_pct": 72.83, "MAE_90D_pct": -9.13, "score_return_alignment_label": "defense_export_backlog_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R1L99_C03_KAI_2024_AIRCRAFT_EXPORT_FRAMEWORK_LOW_MFE_FALSE_STAGE2", "trigger_id": "R1L99_C03_KAI_2024_STAGE2_FALSE_POSITIVE_AIRCRAFT_EXPORT_FRAMEWORK_WATCH", "symbol": "047810", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 60, "customer_quality_score": 40, "policy_or_regulatory_score": 35, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 15, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "aircraft_export_framework_false_stage2", "MFE_90D_pct": 3.3, "MAE_90D_pct": -12.45, "score_return_alignment_label": "aircraft_export_framework_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_aircraft_export_framework_watch_counts_without_final_contract_delivery_backlog_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R1L99_C03_POONGSAN_2024_AMMUNITION_EXPORT_EVENT_CAP_4B", "trigger_id": "R1L99_C03_POONGSAN_2024_STAGE4B_AMMUNITION_EXPORT_EVENT_CAP", "symbol": "103140", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 25, "policy_or_regulatory_score": 30, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "ammunition_export_event_cap_4B_guard", "MFE_90D_pct": 6.46, "MAE_90D_pct": -23.52, "score_return_alignment_label": "ammunition_export_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_ammunition_export_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": "99", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "MISSILE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_AIRCRAFT_EXPORT_FRAMEWORK_FALSE_STAGE2_AND_AMMUNITION_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "defense_export_backlog_delivery_margin_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["defense_export_backlog_positive", "aircraft_export_framework_false_stage2", "ammunition_export_event_cap_4B"], "loop_contribution_label": "priority1_canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied calibrated profile.

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
- C03 rows need explicit signed export backlog, delivery schedule, export-customer quality, production capacity, margin and revision bridge before positive promotion.
- In C03, bridge-missing defense export event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C03 defense export framework backlog rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R1
completed_loop = 99
completed_canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
coverage_scheduler_status = coverage_index_first
next_selection_rule = re-read V12_Research_No_Repeat_Index.md Priority 1 and local supplements
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
