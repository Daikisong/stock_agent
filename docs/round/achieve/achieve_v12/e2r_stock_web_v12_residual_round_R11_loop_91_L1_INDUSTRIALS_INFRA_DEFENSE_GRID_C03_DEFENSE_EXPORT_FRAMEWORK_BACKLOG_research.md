# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R11
scheduled_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id = AEROSPACE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_IR_SENSOR_FALSE_STAGE2_AND_DEFENSE_THEME_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R11_loop_91_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
```

This file is the corrected final output for this execution. The scheduler state after R10 loop 91 is R11 / loop 91. R11 permits the L10 policy/event route or the L1 policy-defense/infra route; this run uses the L1 defense-export route and returns to C03 with a fresh non-top-covered symbol set.

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
scheduled_round = R11
scheduled_loop = 91
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
round_sector_consistency = pass
computed_next_round = R12
computed_next_loop = 91
```

R11 loop 90 used C05 EPC and loop 89 used C03 with other symbols. This loop returns to C03 but avoids the prior R11 C03 symbol set and top repeated C03 names.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG = 21 rows / 12 symbols / good-bad Stage2 11-3 / 4B-4C 0-0
top covered symbols include 079550(4), 047810(3), 065450(3), 005870(2), 103140(2), 003570(1)
previous R11 loop-88 C31 symbols avoided: 036460, 053290, 057030
previous R11 loop-89 C03 symbols avoided: 064350, 010820, 099320
previous R11 loop-90 C05 symbols avoided: 047040, 028050, 052690
previous R10 loop-91 C30 symbols avoided: 003070, 001260, 021320
```

Selected rows avoid hard duplicates and top repeated C03 symbols:

```text
012450 / Stage2-Actionable / 2024-02-14
214430 / Stage2-Actionable / 2024-03-25
013810 / Stage4B / 2024-01-18
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
| 012450 | atlas/symbol_profiles/012/012450.json | selected 2024 window clean after old CA candidates |
| 214430 | atlas/symbol_profiles/214/214430.json | selected 2024 window clean after 2017 CA candidates |
| 013810 | atlas/symbol_profiles/013/013810.json | selected 2024 window clean after old CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R11L91_C03_HANWHA_AERO_2024_AEROSPACE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POSITIVE | 012450 | 2024-02-14 | yes | 180 | yes | yes | true |
| R11L91_C03_I3SYSTEM_2024_IR_SENSOR_DEFENSE_FALSE_STAGE2 | 214430 | 2024-03-25 | yes | 180 | yes | yes | true |
| R11L91_C03_SPEC0_2024_DEFENSE_THEME_EVENT_CAP_4B | 013810 | 2024-01-18 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | AEROSPACE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE | Positive Stage2 requires export framework, firm order, backlog, capacity, customer quality, and margin/revision bridge. |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | IR_SENSOR_DEFENSE_FALSE_STAGE2 | Sensor/defense-electronics theme without export/backlog bridge can become high-MAE false Stage2. |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | DEFENSE_THEME_EVENT_CAP_4B | Geopolitical/defense theme premium should route to 4B when firm export/backlog bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R11L91_C03_HANWHA_AERO_2024_AEROSPACE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POSITIVE | 012450 | 한화에어로스페이스 | positive | Defense export framework/backlog bridge produced very high MFE with controlled early MAE. |
| R11L91_C03_I3SYSTEM_2024_IR_SENSOR_DEFENSE_FALSE_STAGE2 | 214430 | 아이쓰리시스템 | counterexample | IR sensor defense theme had limited MFE and severe later MAE after spike entry. |
| R11L91_C03_SPEC0_2024_DEFENSE_THEME_EVENT_CAP_4B | 013810 | 스페코 | counterexample / 4B | Defense/geopolitical theme premium capped at the January spike and then de-rated. |

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
| Hanwha Aerospace export/backlog bridge | historical public/report proxy | true | true | shadow-only positive |
| I3system IR-sensor false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Speco defense-theme event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 012450 | atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv | atlas/symbol_profiles/012/012450.json |
| 214430 | atlas/ohlcv_tradable_by_symbol_year/214/214430/2024.csv | atlas/symbol_profiles/214/214430.json |
| 013810 | atlas/ohlcv_tradable_by_symbol_year/013/013810/2024.csv | atlas/symbol_profiles/013/013810.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R11L91_C03_HANWHA_AERO_2024_STAGE2_ACTIONABLE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 012450 | Stage2-Actionable | 2024-02-14 | 146300 | positive | export framework/backlog bridge worked |
| R11L91_C03_I3SYSTEM_2024_STAGE2_FALSE_POSITIVE_IR_SENSOR_DEFENSE_THEME | 214430 | Stage2-Actionable | 2024-03-25 | 46750 | counterexample | IR sensor defense false Stage2 |
| R11L91_C03_SPEC0_2024_STAGE4B_DEFENSE_THEME_EVENT_CAP | 013810 | Stage4B | 2024-01-18 | 5090 | counterexample/4B | defense theme event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R11L91_C03_HANWHA_AERO_2024_STAGE2_ACTIONABLE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 146300 | 53.79 | -8.34 | 74.98 | -8.34 | 190.50 | -8.34 | 2024-11-12 | 425000 | -29.06 |
| R11L91_C03_I3SYSTEM_2024_STAGE2_FALSE_POSITIVE_IR_SENSOR_DEFENSE_THEME | 46750 | 9.52 | -20.21 | 9.52 | -24.81 | 9.52 | -47.38 | 2024-03-29 | 51200 | -51.95 |
| R11L91_C03_SPEC0_2024_STAGE4B_DEFENSE_THEME_EVENT_CAP | 5090 | 16.90 | -27.21 | 16.90 | -28.39 | 16.90 | -41.95 | 2024-01-18 | 5950 | -50.34 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C03 Stage2 needs export framework / firm order / backlog / capacity / margin bridge |
| local_4b_watch_guard | strengthen: defense theme and sensor-event premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: high-MAE defense-theme rows cannot promote without durable backlog bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is export-framework/backlog bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 012450 | good_stage2 | Export framework/backlog/capacity bridge produced very high MFE. |
| 214430 | bad_stage2 | Sensor-defense theme lacked backlog bridge and drew down severely after limited MFE. |
| 013810 | good_4B | Defense/geopolitical theme premium capped at the event spike. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 214430 IR-sensor false Stage2 | 0.91 | 0.91 | false Stage2 due missing export framework/backlog bridge |
| 013810 defense-theme cap | 1.00 | 1.00 | good full-window 4B timing |
| 012450 export/backlog bridge | n/a | n/a | positive Stage2, but later defense-export valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 214430 / 013810
```

No hard 4C candidate is proposed. R11 loop 91 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 defense-export cases, Stage2 requires verified export framework, firm order, backlog visibility, production capacity, customer quality, margin, or revision bridge. Defense, geopolitical, sensor, aerospace, or military theme label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
rule = C03 should split real export-framework/backlog positives from defense-electronics false Stage2 and geopolitical-theme event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 33.80 | -20.51 | 0.67 | mixed; C03 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 33.80 | -20.51 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L1 defense export framework/backlog bridge required | 2 | 42.25 | -16.58 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C03 bridge vs event-cap split | 2 | 42.25 | -16.58 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing defense themes as positive | 1 | 74.98 | -8.34 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 012450 defense export bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 74.98 | -8.34 | defense_export_framework_backlog_positive |
| 214430 IR sensor false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 9.52 | -24.81 | IR_sensor_defense_false_stage2 |
| 013810 defense theme cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 16.90 | -28.39 | defense_theme_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "AEROSPACE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_IR_SENSOR_FALSE_STAGE2_AND_DEFENSE_THEME_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C03 aerospace/defense export-framework backlog positive, IR-sensor defense false Stage2, and defense-theme event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: defense_export_framework_backlog_positive, IR_sensor_defense_false_stage2, defense_theme_event_cap_4B
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
- C03 defense export-framework/backlog bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,configured,C03_requires_export_framework_backlog_capacity_margin_revision_bridge,0,"C03 Stage2 should require export framework, firm order, backlog visibility, production capacity, customer quality, margin, or revision bridge, not defense/geopolitical label alone","Hanwha Aerospace positive worked; I3system and Speco theme/event rows failed positive-stage promotion","R11L91_C03_HANWHA_AERO_2024_STAGE2_ACTIONABLE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|R11L91_C03_I3SYSTEM_2024_STAGE2_FALSE_POSITIVE_IR_SENSOR_DEFENSE_THEME|R11L91_C03_SPEC0_2024_STAGE4B_DEFENSE_THEME_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,configured,cap_bridge_missing_defense_theme_and_sensor_premiums_as_4B_watch,0,"Defense theme and sensor/electronics premiums can peak before firm export framework/backlog evidence appears","I3system had deep 180D MAE after late-March spike; Speco showed full-window event-cap behavior after January spike","R11L91_C03_I3SYSTEM_2024_STAGE2_FALSE_POSITIVE_IR_SENSOR_DEFENSE_THEME|R11L91_C03_SPEC0_2024_STAGE4B_DEFENSE_THEME_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,configured,block_positive_stage_when_defense_theme_has_high_MAE_without_backlog_bridge,0,"High MAE after a defense/geopolitical theme entry should block Stage2/Stage3 promotion unless export framework and backlog evidence survives","I3system MAE180=-47.38 and Speco MAE180=-41.95","R11L91_C03_I3SYSTEM_2024_STAGE2_FALSE_POSITIVE_IR_SENSOR_DEFENSE_THEME|R11L91_C03_SPEC0_2024_STAGE4B_DEFENSE_THEME_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R11L91_C03_HANWHA_AERO_2024_AEROSPACE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POSITIVE", "symbol": "012450", "company_name": "한화에어로스페이스", "round": "R11", "loop": "91", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "AEROSPACE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_IR_SENSOR_FALSE_STAGE2_AND_DEFENSE_THEME_EVENT_CAP", "case_type": "structural_success_with_later_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R11L91_C03_HANWHA_AERO_2024_STAGE2_ACTIONABLE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Aerospace/defense export framework and backlog bridge produced very high 30D/90D/180D MFE with controlled initial MAE. C03 works when defense export narrative maps into framework contracts, backlog visibility, production capacity, customer quality, and margin/revision bridge.", "current_profile_verdict": "current_profile_kept_but_C03_positive_requires_export_framework_backlog_capacity_margin_bridge_not_defense_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R11L91_C03_I3SYSTEM_2024_IR_SENSOR_DEFENSE_FALSE_STAGE2", "symbol": "214430", "company_name": "아이쓰리시스템", "round": "R11", "loop": "91", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "AEROSPACE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_IR_SENSOR_FALSE_STAGE2_AND_DEFENSE_THEME_EVENT_CAP", "case_type": "failed_rerating_high_mae_after_sensor_theme", "positive_or_counterexample": "counterexample", "best_trigger": "R11L91_C03_I3SYSTEM_2024_STAGE2_FALSE_POSITIVE_IR_SENSOR_DEFENSE_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "IR sensor / defense-electronics theme spike had limited MFE after the late-March entry and then severe 180D MAE. C03 Stage2 should not be awarded without export framework, firm order, program backlog, production capacity, and margin/revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_IR_sensor_defense_theme_counts_without_export_framework_backlog_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2017 CA candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R11L91_C03_SPEC0_2024_DEFENSE_THEME_EVENT_CAP_4B", "symbol": "013810", "company_name": "스페코", "round": "R11", "loop": "91", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "AEROSPACE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_IR_SENSOR_FALSE_STAGE2_AND_DEFENSE_THEME_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R11L91_C03_SPEC0_2024_STAGE4B_DEFENSE_THEME_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Defense/geopolitical theme premium capped at the January spike and then suffered deep drawdown. C03 should route bridge-missing defense theme premiums to 4B unless export framework, firm order, backlog, capacity, and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_defense_theme_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old CA candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R11L91_C03_HANWHA_AERO_2024_STAGE2_ACTIONABLE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "R11L91_C03_HANWHA_AERO_2024_AEROSPACE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POSITIVE", "symbol": "012450", "company_name": "한화에어로스페이스", "round": "R11", "loop": "91", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "AEROSPACE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_IR_SENSOR_FALSE_STAGE2_AND_DEFENSE_THEME_EVENT_CAP", "sector": "aerospace_defense_export_framework_backlog", "primary_archetype": "defense_export_framework_backlog_capacity_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-14", "entry_date": "2024-02-14", "entry_price": 146300.0, "evidence_available_at_that_date": "aerospace/defense export framework, order backlog, capacity expansion, customer quality and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["export_framework_proxy", "firm_order_backlog_proxy", "production_capacity_proxy", "customer_quality_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "very_high_MFE180", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_defense_export_valuation_watch", "positioning_overheat_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv", "profile_path": "atlas/symbol_profiles/012/012450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 53.79, "MFE_90D_pct": 74.98, "MFE_180D_pct": 190.5, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -8.34, "MAE_90D_pct": -8.34, "MAE_180D_pct": -8.34, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-12", "peak_price": 425000.0, "drawdown_after_peak_pct": -29.06, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_defense_export_valuation_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "defense_export_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_defense_export_framework_backlog_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA", "same_entry_group_id": "R11L91_C03_012450_2024-02-14_146300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R11L91_C03_I3SYSTEM_2024_STAGE2_FALSE_POSITIVE_IR_SENSOR_DEFENSE_THEME", "case_id": "R11L91_C03_I3SYSTEM_2024_IR_SENSOR_DEFENSE_FALSE_STAGE2", "symbol": "214430", "company_name": "아이쓰리시스템", "round": "R11", "loop": "91", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "AEROSPACE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_IR_SENSOR_FALSE_STAGE2_AND_DEFENSE_THEME_EVENT_CAP", "sector": "IR_sensor_defense_electronics_theme", "primary_archetype": "IR_sensor_theme_without_export_framework_backlog_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-25", "entry_date": "2024-03-25", "entry_price": 46750.0, "evidence_available_at_that_date": "IR sensor / defense electronics theme and export/order expectation proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["IR_sensor_defense_theme", "export_order_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "deep_MAE180", "export_framework_backlog_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214430/2024.csv", "profile_path": "atlas/symbol_profiles/214/214430.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.52, "MFE_90D_pct": 9.52, "MFE_180D_pct": 9.52, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -20.21, "MAE_90D_pct": -24.81, "MAE_180D_pct": -47.38, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-29", "peak_price": 51200.0, "drawdown_after_peak_pct": -51.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.91, "four_b_full_window_peak_proximity": 0.91, "four_b_timing_verdict": "IR_sensor_defense_theme_spike_was_false_stage2_due_missing_export_framework_backlog_bridge", "four_b_evidence_type": ["defense_electronics_theme", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_IR_sensor_defense_theme_without_export_framework_backlog_bridge", "current_profile_verdict": "current_profile_false_positive_if_IR_sensor_defense_theme_counts_without_export_framework_backlog_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2017_CA", "same_entry_group_id": "R11L91_C03_214430_2024-03-25_46750", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R11L91_C03_SPEC0_2024_STAGE4B_DEFENSE_THEME_EVENT_CAP", "case_id": "R11L91_C03_SPEC0_2024_DEFENSE_THEME_EVENT_CAP_4B", "symbol": "013810", "company_name": "스페코", "round": "R11", "loop": "91", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "AEROSPACE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_IR_SENSOR_FALSE_STAGE2_AND_DEFENSE_THEME_EVENT_CAP", "sector": "defense_geopolitical_theme_event", "primary_archetype": "defense_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-18", "entry_date": "2024-01-18", "entry_price": 5090.0, "evidence_available_at_that_date": "defense/geopolitical theme premium after January spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["defense_theme_event_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "export_framework_backlog_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/013/013810/2024.csv", "profile_path": "atlas/symbol_profiles/013/013810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.9, "MFE_90D_pct": 16.9, "MFE_180D_pct": 16.9, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -27.21, "MAE_90D_pct": -28.39, "MAE_180D_pct": -41.95, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-18", "peak_price": 5950.0, "drawdown_after_peak_pct": -50.34, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_defense_theme_event_cap", "four_b_evidence_type": ["defense_theme_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_defense_theme_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_defense_theme_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA", "same_entry_group_id": "R11L91_C03_013810_2024-01-18_5090", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L91_C03_HANWHA_AERO_2024_AEROSPACE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_POSITIVE", "trigger_id": "R11L91_C03_HANWHA_AERO_2024_STAGE2_ACTIONABLE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "symbol": "012450", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 65, "backlog_visibility_score": 70, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 60, "policy_or_regulatory_score": 55, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "defense_export_framework_backlog_positive", "MFE_90D_pct": 74.98, "MAE_90D_pct": -8.34, "score_return_alignment_label": "defense_export_framework_backlog_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L91_C03_I3SYSTEM_2024_IR_SENSOR_DEFENSE_FALSE_STAGE2", "trigger_id": "R11L91_C03_I3SYSTEM_2024_STAGE2_FALSE_POSITIVE_IR_SENSOR_DEFENSE_THEME", "symbol": "214430", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "IR_sensor_defense_false_stage2", "MFE_90D_pct": 9.52, "MAE_90D_pct": -24.81, "score_return_alignment_label": "IR_sensor_defense_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_IR_sensor_defense_theme_counts_without_export_framework_backlog_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L91_C03_SPEC0_2024_DEFENSE_THEME_EVENT_CAP_4B", "trigger_id": "R11L91_C03_SPEC0_2024_STAGE4B_DEFENSE_THEME_EVENT_CAP", "symbol": "013810", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "defense_theme_event_cap_4B_guard", "MFE_90D_pct": 16.9, "MAE_90D_pct": -28.39, "score_return_alignment_label": "defense_theme_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_defense_theme_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": "91", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "AEROSPACE_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_IR_SENSOR_FALSE_STAGE2_AND_DEFENSE_THEME_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["defense_export_framework_backlog_positive", "IR_sensor_defense_false_stage2", "defense_theme_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_round = R11
completed_loop = 91
next_round = R12
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
