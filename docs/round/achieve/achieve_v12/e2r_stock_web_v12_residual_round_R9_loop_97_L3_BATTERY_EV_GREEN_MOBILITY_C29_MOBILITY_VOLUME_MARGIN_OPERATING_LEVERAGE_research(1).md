# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R9
scheduled_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE_VS_EV_REDUCER_EXPORT_FALSE_STAGE2_AND_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | mobility_volume_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R9_loop_97_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

This file is the corrected final output for this execution. The scheduler state after R8 loop 97 is R9 / loop 97. R9 allows the L3 mobility route or the L9 construction route. This run uses the L3 mobility route and fills C29 mobility volume/margin operating-leverage rather than repeating the immediately preceding R9 loop 96 C29 symbols or R9 loop 95 C14 demand-slowdown guardrail file.

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
mobility_volume_margin_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R9
scheduled_loop = 97
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
round_sector_consistency = pass
computed_next_round = R10
computed_next_loop = 97
```

C29 is a mobility-volume-to-margin archetype. A mobility or autonomous-driving label is the dashboard light; the signal becomes useful only when OEM volume, model mix, utilization, ASP/mix, margin and revision are actually wired into the case.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE = 60 rows / 27 symbols / good-bad Stage2 26-13 / 4B-4C 6-0
top covered symbols include 011210(7), 000270(5), 005380(5), 005850(5), 010690(5), 018880(3)
previous R9 loop-94 C29 symbols avoided: 015750, 009900, 123410
previous R9 loop-95 C14 symbols avoided: 361610, 393890, 025900
previous R9 loop-96 C29 symbols avoided: 204320, 118990, 317120
previous R8 loop-97 C28 symbols avoided: 047560, 263860, 356680
previous R3 loop-97 C12 symbols avoided: 011790, 243840, 419050
```

Selected rows avoid hard duplicates and top repeated C29 symbols:

```text
064960 / Stage2-Actionable / 2024-02-06
092200 / Stage2-Actionable / 2024-04-22
370090 / Stage4B / 2024-04-30
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
| 064960 | atlas/symbol_profiles/064/064960.json | 30D/90D/180D clean before 2025-01-24 and 2025-02-26 CA candidates |
| 092200 | atlas/symbol_profiles/092/092200.json | selected 2024 window clean after old 2008/2019 CA candidates |
| 370090 | atlas/symbol_profiles/370/370090.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R9L97_C29_SNTMOTIVE_2024_EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE_POSITIVE | 064960 | 2024-02-06 | yes | 180 | yes | yes | true |
| R9L97_C29_DIC_2024_EV_REDUCER_EXPORT_VOLUME_FALSE_STAGE2 | 092200 | 2024-04-22 | yes | 180 | yes | yes | true |
| R9L97_C29_FUTURENURI_2024_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP_4B | 370090 | 2024-04-30 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE | Positive Stage2 requires OEM volume, powertrain mix, utilization, customer quality, margin and revision bridge. |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | EV_REDUCER_EXPORT_FALSE_STAGE2 | EV reducer/export watch without OEM call-off and margin bridge can become false Stage2. |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTONOMOUS_CAMERA_MODULE_EVENT_CAP_4B | Autonomous camera/sensing-module premium should route to 4B when design-win, utilization and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R9L97_C29_SNTMOTIVE_2024_EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE_POSITIVE | 064960 | SNT모티브 | positive | EV/powertrain auto-parts bridge produced positive MFE with controlled MAE. |
| R9L97_C29_DIC_2024_EV_REDUCER_EXPORT_VOLUME_FALSE_STAGE2 | 092200 | 디아이씨 | counterexample | EV reducer/export watch had high MAE after a shallow follow-through. |
| R9L97_C29_FUTURENURI_2024_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP_4B | 370090 | 퓨런티어 | counterexample / 4B | Autonomous camera-module event premium capped around the April spike and later de-rated. |

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
| SNT Motive EV/powertrain margin bridge | historical public/report proxy | true | true | shadow-only positive |
| DIC EV reducer/export false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Furonteer autonomous camera-module cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 064960 | atlas/ohlcv_tradable_by_symbol_year/064/064960/2024.csv | atlas/symbol_profiles/064/064960.json |
| 092200 | atlas/ohlcv_tradable_by_symbol_year/092/092200/2024.csv | atlas/symbol_profiles/092/092200.json |
| 370090 | atlas/ohlcv_tradable_by_symbol_year/370/370090/2024.csv | atlas/symbol_profiles/370/370090.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R9L97_C29_SNTMOTIVE_2024_STAGE2_ACTIONABLE_EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE | 064960 | Stage2-Actionable | 2024-02-06 | 44250 | positive | EV/powertrain auto-parts margin bridge worked |
| R9L97_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_EXPORT_VOLUME_WATCH | 092200 | Stage2-Actionable | 2024-04-22 | 6180 | counterexample | EV reducer/export false Stage2 |
| R9L97_C29_FUTURENURI_2024_STAGE4B_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP | 370090 | Stage4B | 2024-04-30 | 26100 | counterexample/4B | autonomous camera-module event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R9L97_C29_SNTMOTIVE_2024_STAGE2_ACTIONABLE_EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE | 44250 | 5.88 | -2.49 | 12.43 | -2.49 | 13.67 | -4.86 | 2024-06-28 | 50300 | -13.52 |
| R9L97_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_EXPORT_VOLUME_WATCH | 6180 | 1.94 | -18.61 | 11.97 | -25.89 | 11.97 | -25.89 | 2024-06-26 | 6920 | -33.81 |
| R9L97_C29_FUTURENURI_2024_STAGE4B_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP | 26100 | 6.51 | -18.20 | 6.51 | -27.28 | 6.51 | -35.00 | 2024-04-30 | 27800 | -31.65 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C29 Stage2 needs OEM volume / model mix / utilization / ASP-mix / margin / revision bridge |
| mobility_volume_margin_guardrail | strengthen: mobility labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing EV reducer and autonomous camera-module premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE mobility rows cannot promote without durable volume/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether mobility narrative becomes OEM volume and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 064960 | good_stage2_with_later_watch | EV/powertrain mix and margin bridge produced positive MFE with controlled MAE. |
| 092200 | bad_stage2 | EV reducer/export watch lacked confirmed OEM call-off and suffered high MAE. |
| 370090 | good_4B | Autonomous camera-module premium capped around the April high and then drew down. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 092200 EV reducer/export false Stage2 | 0.89 | 0.89 | false Stage2 due missing OEM call-off / mix / utilization / margin bridge |
| 370090 autonomous camera-module cap | 0.94 | 0.94 | good full-window 4B timing after autonomous camera-module event premium |
| 064960 EV/powertrain bridge | n/a | n/a | positive Stage2, but later mobility valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 092200 / 370090
```

No hard 4C candidate is introduced in this R9 loop 97 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 mobility volume/margin operating-leverage cases, Stage2 requires verified OEM production volume, model/order mix, design-win or call-off durability, utilization, ASP/mix, margin, or revision bridge. Mobility, EV, reducer, powertrain, ADAS, autonomous driving, camera module, smart-car or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
rule = C29 should split true OEM-volume/mix/margin positives from EV reducer export false Stage2 and autonomous camera-module event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 10.30 | -18.55 | 0.67 | mixed; C29 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 10.30 | -18.55 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L3 OEM-volume/margin bridge required | 2 | 12.20 | -14.19 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C29 bridge vs event-cap split | 2 | 12.20 | -14.19 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing mobility themes as positive | 1 | 12.43 | -2.49 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 064960 EV/powertrain bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 12.43 | -2.49 | EV_powertrain_margin_positive |
| 092200 reducer/export false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 11.97 | -25.89 | EV_reducer_export_false_stage2 |
| 370090 camera-module cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 6.51 | -27.28 | autonomous_camera_module_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE_VS_EV_REDUCER_EXPORT_FALSE_STAGE2_AND_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C29 SNT Motive EV/powertrain auto-parts margin positive, DIC EV reducer/export volume false Stage2, and Furonteer autonomous camera-module event-cap 4B while avoiding top repeated C29 and previous R9/R8 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, mobility_volume_margin_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: EV_powertrain_margin_positive, EV_reducer_export_false_stage2, autonomous_camera_module_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, mobility_volume_margin_guardrail, high_MAE_guardrail
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
- C29 mobility volume/margin operating-leverage bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,C29_requires_OEM_volume_model_mix_utilization_margin_revision_bridge,0,"C29 Stage2 should require OEM production volume, model/order mix, powertrain or component utilization, ASP/mix, margin, or revision bridge, not mobility/EV/ADAS/autonomous-driving label alone","SNT Motive positive worked; DIC and Furonteer event/watch rows failed positive-stage promotion","R9L97_C29_SNTMOTIVE_2024_STAGE2_ACTIONABLE_EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE|R9L97_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_EXPORT_VOLUME_WATCH|R9L97_C29_FUTURENURI_2024_STAGE4B_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,cap_bridge_missing_EV_reducer_and_autonomous_camera_event_premiums_as_4B_watch,0,"EV reducer/export and autonomous camera/sensing premiums can peak before OEM call-off, design-win, utilization and margin bridge is proven","DIC had high MAE after EV reducer export watch; Furonteer showed 4B event-cap behavior after the April camera-module spike","R9L97_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_EXPORT_VOLUME_WATCH|R9L97_C29_FUTURENURI_2024_STAGE4B_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,block_positive_stage_when_mobility_theme_has_high_or_persistent_MAE_without_volume_margin_bridge,0,"High or persistent MAE after bridge-missing C29 entries should block Stage2/Stage3 promotion unless OEM volume, mix and margin evidence survives","DIC MAE90=-25.89 and Furonteer MAE90=-27.28","R9L97_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_EXPORT_VOLUME_WATCH|R9L97_C29_FUTURENURI_2024_STAGE4B_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R9L97_C29_SNTMOTIVE_2024_EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE_POSITIVE", "symbol": "064960", "company_name": "SNT모티브", "round": "R9", "loop": "97", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE_VS_EV_REDUCER_EXPORT_FALSE_STAGE2_AND_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP", "case_type": "moderate_structural_success_with_later_mobility_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R9L97_C29_SNTMOTIVE_2024_STAGE2_ACTIONABLE_EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "EV/powertrain auto-parts volume and margin bridge produced a clean 30D/90D/180D MFE path with controlled MAE. C29 works when mobility-volume narrative maps into OEM model volume, powertrain mix, utilization, customer quality, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C29_positive_requires_OEM_volume_powertrain_mix_utilization_margin_revision_bridge_not_mobility_label_only", "price_source": "Songdaiki/stock-web", "notes": "Profile has 2025-01-24 and 2025-02-26 CA candidates, but selected 2024-02-06 entry keeps 30D/90D/180D calibration window before those CA candidates."}
{"row_type": "case", "case_id": "R9L97_C29_DIC_2024_EV_REDUCER_EXPORT_VOLUME_FALSE_STAGE2", "symbol": "092200", "company_name": "디아이씨", "round": "R9", "loop": "97", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE_VS_EV_REDUCER_EXPORT_FALSE_STAGE2_AND_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP", "case_type": "failed_rerating_EV_reducer_export_volume_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R9L97_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_EXPORT_VOLUME_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "EV reducer / drivetrain export-volume watch after the April spike had only shallow follow-through and then high MAE. C29 Stage2 should not be awarded without confirmed OEM production call-off, model mix, utilization, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_EV_reducer_export_watch_counts_without_OEM_calloff_mix_utilization_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2008 and 2019 CA candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R9L97_C29_FUTURENURI_2024_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP_4B", "symbol": "370090", "company_name": "퓨런티어", "round": "R9", "loop": "97", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE_VS_EV_REDUCER_EXPORT_FALSE_STAGE2_AND_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R9L97_C29_FUTURENURI_2024_STAGE4B_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Autonomous-driving camera / sensing-module event premium capped around the April spike and then de-rated through the following window. C29 should route bridge-missing autonomous camera-module premiums to 4B unless OEM design-win, model-volume cadence, ASP/mix, utilization, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_autonomous_camera_module_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R9L97_C29_SNTMOTIVE_2024_STAGE2_ACTIONABLE_EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE", "case_id": "R9L97_C29_SNTMOTIVE_2024_EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE_POSITIVE", "symbol": "064960", "company_name": "SNT모티브", "round": "R9", "loop": "97", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE_VS_EV_REDUCER_EXPORT_FALSE_STAGE2_AND_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP", "sector": "EV_powertrain_auto_parts_OEM_volume_margin", "primary_archetype": "OEM_volume_powertrain_mix_utilization_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | mobility_volume_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-06", "entry_date": "2024-02-06", "entry_price": 44250.0, "evidence_available_at_that_date": "EV/powertrain auto-parts OEM volume, product mix, utilization, customer quality and margin/revision bridge proxy after February retest; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["OEM_volume_proxy", "powertrain_mix_proxy", "utilization_proxy", "customer_quality_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "positive_MFE90", "positive_MFE180", "controlled_MAE90"], "stage4b_evidence_fields": ["later_mobility_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064960/2024.csv", "profile_path": "atlas/symbol_profiles/064/064960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.88, "MFE_90D_pct": 12.43, "MFE_180D_pct": 13.67, "MFE_1Y_pct": "contaminated_or_unavailable_due_2025_CA_candidate", "MFE_2Y_pct": "contaminated_or_unavailable_due_2025_CA_candidate", "MAE_30D_pct": -2.49, "MAE_90D_pct": -2.49, "MAE_180D_pct": -4.86, "MAE_1Y_pct": "contaminated_or_unavailable_due_2025_CA_candidate", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-28", "peak_price": 50300.0, "drawdown_after_peak_pct": -13.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_mobility_valuation_4B_watch_needed", "four_b_evidence_type": ["OEM_volume_bridge", "powertrain_mix_margin", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_EV_powertrain_auto_parts_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_before_2025_CA_candidates", "same_entry_group_id": "R9L97_C29_064960_2024-02-06_44250", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L97_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_EXPORT_VOLUME_WATCH", "case_id": "R9L97_C29_DIC_2024_EV_REDUCER_EXPORT_VOLUME_FALSE_STAGE2", "symbol": "092200", "company_name": "디아이씨", "round": "R9", "loop": "97", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE_VS_EV_REDUCER_EXPORT_FALSE_STAGE2_AND_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP", "sector": "EV_reducer_drivetrain_export_volume_watch", "primary_archetype": "EV_reducer_export_watch_without_OEM_calloff_mix_utilization_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | mobility_volume_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-22", "entry_date": "2024-04-22", "entry_price": 6180.0, "evidence_available_at_that_date": "EV reducer / drivetrain export-volume event watch without confirmed OEM production call-off, model mix, utilization or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["EV_reducer_export_watch", "drivetrain_volume_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_quality_MFE", "high_MAE90", "OEM_calloff_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/092/092200/2024.csv", "profile_path": "atlas/symbol_profiles/092/092200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.94, "MFE_90D_pct": 11.97, "MFE_180D_pct": 11.97, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -18.61, "MAE_90D_pct": -25.89, "MAE_180D_pct": -25.89, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 6920.0, "drawdown_after_peak_pct": -33.81, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.89, "four_b_full_window_peak_proximity": 0.89, "four_b_timing_verdict": "EV_reducer_export_watch_was_false_stage2_due_missing_OEM_calloff_mix_utilization_margin_bridge", "four_b_evidence_type": ["EV_reducer_export_event_premium", "bridge_missing", "high_MAE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_EV_reducer_export_volume_watch_without_OEM_calloff_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_EV_reducer_export_watch_counts_without_OEM_calloff_mix_utilization_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2008_2019_CA", "same_entry_group_id": "R9L97_C29_092200_2024-04-22_6180", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L97_C29_FUTURENURI_2024_STAGE4B_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP", "case_id": "R9L97_C29_FUTURENURI_2024_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP_4B", "symbol": "370090", "company_name": "퓨런티어", "round": "R9", "loop": "97", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE_VS_EV_REDUCER_EXPORT_FALSE_STAGE2_AND_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP", "sector": "autonomous_driving_camera_sensing_module_event_premium", "primary_archetype": "autonomous_camera_module_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | mobility_volume_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-30", "entry_date": "2024-04-30", "entry_price": 26100.0, "evidence_available_at_that_date": "autonomous-driving camera/sensing module event premium without confirmed OEM design-win, production volume cadence, ASP/mix, utilization or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["autonomous_camera_module_event", "ADAS_sensing_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "high_MAE90", "OEM_design_win_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/370/370090/2024.csv", "profile_path": "atlas/symbol_profiles/370/370090.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.51, "MFE_90D_pct": 6.51, "MFE_180D_pct": 6.51, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -18.2, "MAE_90D_pct": -27.28, "MAE_180D_pct": -35.0, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-30", "peak_price": 27800.0, "drawdown_after_peak_pct": -31.65, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing_autonomous_camera_module_event_cap", "four_b_evidence_type": ["autonomous_camera_module_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_autonomous_camera_module_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_autonomous_camera_module_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R9L97_C29_370090_2024-04-30_26100", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L97_C29_SNTMOTIVE_2024_EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R9L97_C29_SNTMOTIVE_2024_STAGE2_ACTIONABLE_EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE", "symbol": "064960", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 55, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 50, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 65, "customer_quality_score": 60, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 30, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "EV_powertrain_auto_parts_margin_positive", "MFE_90D_pct": 12.43, "MAE_90D_pct": -2.49, "score_return_alignment_label": "EV_powertrain_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L97_C29_DIC_2024_EV_REDUCER_EXPORT_VOLUME_FALSE_STAGE2", "trigger_id": "R9L97_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_EXPORT_VOLUME_WATCH", "symbol": "092200", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "EV_reducer_export_false_stage2", "MFE_90D_pct": 11.97, "MAE_90D_pct": -25.89, "score_return_alignment_label": "EV_reducer_export_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_EV_reducer_export_watch_counts_without_OEM_calloff_mix_utilization_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L97_C29_FUTURENURI_2024_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP_4B", "trigger_id": "R9L97_C29_FUTURENURI_2024_STAGE4B_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP", "symbol": "370090", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "autonomous_camera_module_event_cap_4B_guard", "MFE_90D_pct": 6.51, "MAE_90D_pct": -27.28, "score_return_alignment_label": "autonomous_camera_module_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_autonomous_camera_module_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": "97", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE_VS_EV_REDUCER_EXPORT_FALSE_STAGE2_AND_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "mobility_volume_margin_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["EV_powertrain_margin_positive", "EV_reducer_export_false_stage2", "autonomous_camera_module_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C29 rows need explicit OEM production volume, model/order mix, design-win or call-off durability, utilization, ASP/mix, margin, or revision bridge before positive promotion.
- In C29, bridge-missing mobility event-premium rows with low-quality MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C29 mobility volume/margin rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R9
completed_loop = 97
next_round = R10
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
