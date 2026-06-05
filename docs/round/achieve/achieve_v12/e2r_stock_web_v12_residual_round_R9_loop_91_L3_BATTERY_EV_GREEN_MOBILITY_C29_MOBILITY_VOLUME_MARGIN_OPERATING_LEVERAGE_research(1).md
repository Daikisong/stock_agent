# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R9
scheduled_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = AUTO_INTERIOR_MODULE_VOLUME_MARGIN_BRIDGE_VS_LIGHTWEIGHT_PLASTIC_FALSE_STAGE2_AND_EXHAUST_PARTS_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R9_loop_91_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

This file is the corrected final output for this execution. The scheduler state after R8 loop 91 is R9 / loop 91. R9 allows the L3 mobility route or the L9 construction route; this run uses the L3 mobility route and returns to C29 with fresh non-top-covered symbols.

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
scheduled_round = R9
scheduled_loop = 91
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
round_sector_consistency = pass
computed_next_round = R10
computed_next_loop = 91
```

R9 loop 90 already used C29 with KoreaFT / DIC / INFAC. This loop avoids those symbols and uses a different fine split around auto interior-module volume/margin, lightweight EV plastic parts, and exhaust/mobility parts event-cap behavior.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE = 60 rows / 27 symbols / good-bad Stage2 26-13 / 4B-4C 6-0
top covered symbols include 011210(7), 000270(5), 005380(5), 005850(5), 010690(5), 018880(3)
previous R9 loop-88 C29 symbols avoided: 161390, 003620, 204320
previous R9 loop-90 C29 symbols avoided: 123410, 092200, 023810
previous R8 loop-91 C28 symbols avoided: 170790, 136540, 356890
```

Selected rows avoid hard duplicates and top repeated C29 symbols:

```text
200880 / Stage2-Actionable / 2024-01-24
038110 / Stage2-Actionable / 2024-02-02
033530 / Stage4B / 2024-02-14
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
| 200880 | atlas/symbol_profiles/200/200880.json | no corporate-action candidate |
| 038110 | atlas/symbol_profiles/038/038110.json | selected 2024 window clean after 2023-11-28 CA |
| 033530 | atlas/symbol_profiles/033/033530.json | selected 2024 window clean after old 1999 CA |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R9L91_C29_SEOYONEHWA_2024_AUTO_INTERIOR_MODULE_VOLUME_MARGIN_POSITIVE | 200880 | 2024-01-24 | yes | 180 | yes | yes | true |
| R9L91_C29_ECOPLASTIC_2024_LIGHTWEIGHT_EV_PARTS_FALSE_STAGE2 | 038110 | 2024-02-02 | yes | 180 | yes | yes | true |
| R9L91_C29_SJGSEJONG_2024_EXHAUST_MOBILITY_PARTS_EVENT_CAP_4B | 033530 | 2024-02-14 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_INTERIOR_MODULE_VOLUME_MARGIN_BRIDGE | Positive Stage2 requires customer volume, OEM/customer mix, utilization, operating leverage, margin, and revision bridge. |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | LIGHTWEIGHT_PLASTIC_FALSE_STAGE2 | Lightweight EV parts label without volume/margin bridge can become high-MAE false Stage2. |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | EXHAUST_MOBILITY_PARTS_EVENT_CAP_4B | Exhaust/mobility-parts event premium should route to 4B when volume/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R9L91_C29_SEOYONEHWA_2024_AUTO_INTERIOR_MODULE_VOLUME_MARGIN_POSITIVE | 200880 | 서연이화 | positive | Auto interior-module volume/margin bridge produced very high early MFE with shallow 90D MAE. |
| R9L91_C29_ECOPLASTIC_2024_LIGHTWEIGHT_EV_PARTS_FALSE_STAGE2 | 038110 | 에코플라스틱 | counterexample | Lightweight EV parts theme produced limited MFE and severe 180D MAE. |
| R9L91_C29_SJGSEJONG_2024_EXHAUST_MOBILITY_PARTS_EVENT_CAP_4B | 033530 | SJG세종 | counterexample / 4B | Exhaust/mobility-parts event premium capped and then drew down deeply. |

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
| Seoyon E-Hwa auto interior volume/margin | historical public/report proxy | true | true | shadow-only positive |
| EcoPlastic lightweight EV parts false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| SJG Sejong exhaust/mobility parts event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 200880 | atlas/ohlcv_tradable_by_symbol_year/200/200880/2024.csv | atlas/symbol_profiles/200/200880.json |
| 038110 | atlas/ohlcv_tradable_by_symbol_year/038/038110/2024.csv | atlas/symbol_profiles/038/038110.json |
| 033530 | atlas/ohlcv_tradable_by_symbol_year/033/033530/2024.csv | atlas/symbol_profiles/033/033530.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R9L91_C29_SEOYONEHWA_2024_STAGE2_ACTIONABLE_AUTO_INTERIOR_VOLUME_MARGIN | 200880 | Stage2-Actionable | 2024-01-24 | 16580 | positive | auto interior-module volume/margin bridge worked |
| R9L91_C29_ECOPLASTIC_2024_STAGE2_FALSE_POSITIVE_LIGHTWEIGHT_EV_PARTS | 038110 | Stage2-Actionable | 2024-02-02 | 5510 | counterexample | lightweight EV parts false Stage2 |
| R9L91_C29_SJGSEJONG_2024_STAGE4B_EXHAUST_MOBILITY_PARTS_EVENT_CAP | 033530 | Stage4B | 2024-02-14 | 6380 | counterexample/4B | exhaust mobility-parts event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R9L91_C29_SEOYONEHWA_2024_STAGE2_ACTIONABLE_AUTO_INTERIOR_VOLUME_MARGIN | 16580 | 50.78 | -1.45 | 50.78 | -1.45 | 50.78 | -23.94 | 2024-02-07 | 25000 | -49.56 |
| R9L91_C29_ECOPLASTIC_2024_STAGE2_FALSE_POSITIVE_LIGHTWEIGHT_EV_PARTS | 5510 | 4.36 | -14.70 | 4.36 | -25.77 | 4.36 | -50.45 | 2024-02-06 | 5750 | -52.52 |
| R9L91_C29_SJGSEJONG_2024_STAGE4B_EXHAUST_MOBILITY_PARTS_EVENT_CAP | 6380 | 7.21 | -11.44 | 7.21 | -35.74 | 7.21 | -35.97 | 2024-03-06 | 6840 | -40.28 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C29 Stage2 needs customer volume / OEM mix / utilization / margin / revision bridge |
| local_4b_watch_guard | strengthen: lightweight/exhaust/EV-parts theme premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: high-MAE auto-parts theme rows cannot promote without durable volume/margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is mobility volume/margin bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 200880 | good_stage2_with_later_watch | Customer-volume/margin bridge produced high early MFE, but later cycle watch remains necessary. |
| 038110 | bad_stage2 | Lightweight EV-parts theme lacked durable volume/margin bridge and drew down severely. |
| 033530 | good_4B | Mobility-parts premium capped after the event spike. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 038110 lightweight EV parts false Stage2 | 0.96 | 0.96 | false Stage2 due missing volume/margin bridge |
| 033530 exhaust mobility parts cap | 0.93 | 0.93 | good full-window 4B timing |
| 200880 auto interior bridge | n/a | n/a | positive Stage2, but later auto-parts cycle 4B watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 038110 / 033530
```

No hard 4C candidate is proposed. R9 loop 91 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 mobility volume/margin operating-leverage cases, Stage2 requires verified customer volume, OEM/customer mix, utilization, operating leverage, gross-margin recovery, or revision bridge. Auto parts, lightweight EV, exhaust, mobility module, or theme label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
rule = C29 should split true volume/margin operating-leverage positives from lightweight EV-parts false Stage2 and exhaust/mobility event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 20.78 | -20.99 | 0.67 | mixed; C29 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 20.78 | -20.99 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L3 mobility volume/margin bridge required | 2 | 27.57 | -13.61 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C29 bridge vs event-cap split | 2 | 27.57 | -13.61 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing mobility themes as positive | 1 | 50.78 | -1.45 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 200880 auto interior bridge | 66 | Stage2-Watch | 75 | Stage2-Actionable | 50.78 | -1.45 | auto_interior_volume_margin_positive |
| 038110 lightweight false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 4.36 | -25.77 | lightweight_EV_parts_false_stage2 |
| 033530 exhaust cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 7.21 | -35.74 | exhaust_mobility_parts_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_INTERIOR_MODULE_VOLUME_MARGIN_BRIDGE_VS_LIGHTWEIGHT_PLASTIC_FALSE_STAGE2_AND_EXHAUST_PARTS_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C29 auto interior-module volume/margin positive, lightweight EV plastic false Stage2, and exhaust/mobility parts event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: auto_interior_volume_margin_positive, lightweight_EV_parts_false_stage2, exhaust_mobility_parts_event_cap_4B
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
- C29 mobility volume/margin bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,C29_requires_volume_customer_mix_utilization_margin_revision_bridge,0,"C29 Stage2 should require customer volume, OEM/customer mix, utilization, operating leverage, margin, or revision bridge, not auto-parts/EV/lightweight label alone","Seoyon E-Hwa positive worked; EcoPlastic and SJG Sejong theme/event rows failed positive-stage promotion","R9L91_C29_SEOYONEHWA_2024_STAGE2_ACTIONABLE_AUTO_INTERIOR_VOLUME_MARGIN|R9L91_C29_ECOPLASTIC_2024_STAGE2_FALSE_POSITIVE_LIGHTWEIGHT_EV_PARTS|R9L91_C29_SJGSEJONG_2024_STAGE4B_EXHAUST_MOBILITY_PARTS_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,cap_lightweight_exhaust_and_EV_parts_theme_premiums_as_4B_watch,0,"Mobility-parts theme premiums can peak before confirmed volume/margin bridge appears","EcoPlastic had limited MFE and high MAE; SJG Sejong showed event-cap behavior after February/March spike","R9L91_C29_ECOPLASTIC_2024_STAGE2_FALSE_POSITIVE_LIGHTWEIGHT_EV_PARTS|R9L91_C29_SJGSEJONG_2024_STAGE4B_EXHAUST_MOBILITY_PARTS_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,block_positive_stage_when_auto_parts_theme_has_high_MAE_without_volume_margin_bridge,0,"High MAE after a mobility-parts theme entry should block Stage2/Stage3 promotion unless customer volume and margin evidence survives","EcoPlastic MAE180=-50.45 and SJG Sejong MAE90=-35.74","R9L91_C29_ECOPLASTIC_2024_STAGE2_FALSE_POSITIVE_LIGHTWEIGHT_EV_PARTS|R9L91_C29_SJGSEJONG_2024_STAGE4B_EXHAUST_MOBILITY_PARTS_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R9L91_C29_SEOYONEHWA_2024_AUTO_INTERIOR_MODULE_VOLUME_MARGIN_POSITIVE", "symbol": "200880", "company_name": "서연이화", "round": "R9", "loop": "91", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_INTERIOR_MODULE_VOLUME_MARGIN_BRIDGE_VS_LIGHTWEIGHT_PLASTIC_FALSE_STAGE2_AND_EXHAUST_PARTS_EVENT_CAP", "case_type": "structural_success_with_later_cycle_watch", "positive_or_counterexample": "positive", "best_trigger": "R9L91_C29_SEOYONEHWA_2024_STAGE2_ACTIONABLE_AUTO_INTERIOR_VOLUME_MARGIN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Auto interior-module / global OEM volume-margin operating-leverage bridge produced very high early MFE with shallow 90D MAE. C29 works when mobility volume and customer mix convert into utilization, operating leverage, margin, and revision bridge, but later 4B cycle watch is still needed.", "current_profile_verdict": "current_profile_kept_but_C29_positive_requires_volume_customer_mix_margin_revision_bridge_not_auto_parts_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile; source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R9L91_C29_ECOPLASTIC_2024_LIGHTWEIGHT_EV_PARTS_FALSE_STAGE2", "symbol": "038110", "company_name": "에코플라스틱", "round": "R9", "loop": "91", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_INTERIOR_MODULE_VOLUME_MARGIN_BRIDGE_VS_LIGHTWEIGHT_PLASTIC_FALSE_STAGE2_AND_EXHAUST_PARTS_EVENT_CAP", "case_type": "failed_rerating_high_mae_theme", "positive_or_counterexample": "counterexample", "best_trigger": "R9L91_C29_ECOPLASTIC_2024_STAGE2_FALSE_POSITIVE_LIGHTWEIGHT_EV_PARTS", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Lightweight plastic / EV parts theme spike produced very limited MFE and severe 180D MAE. C29 Stage2 should not be awarded unless customer volume, utilization, operating leverage, and margin/revision bridge are visible.", "current_profile_verdict": "current_profile_false_positive_if_lightweight_EV_parts_theme_counts_without_volume_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after 2023-11-28 CA candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R9L91_C29_SJGSEJONG_2024_EXHAUST_MOBILITY_PARTS_EVENT_CAP_4B", "symbol": "033530", "company_name": "SJG세종", "round": "R9", "loop": "91", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_INTERIOR_MODULE_VOLUME_MARGIN_BRIDGE_VS_LIGHTWEIGHT_PLASTIC_FALSE_STAGE2_AND_EXHAUST_PARTS_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R9L91_C29_SJGSEJONG_2024_STAGE4B_EXHAUST_MOBILITY_PARTS_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Exhaust / mobility parts event premium capped after the February/March spike and then suffered deep drawdown. C29 should route bridge-missing auto-parts event premiums to 4B unless volume and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_exhaust_mobility_parts_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1999 CA candidate. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R9L91_C29_SEOYONEHWA_2024_STAGE2_ACTIONABLE_AUTO_INTERIOR_VOLUME_MARGIN", "case_id": "R9L91_C29_SEOYONEHWA_2024_AUTO_INTERIOR_MODULE_VOLUME_MARGIN_POSITIVE", "symbol": "200880", "company_name": "서연이화", "round": "R9", "loop": "91", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_INTERIOR_MODULE_VOLUME_MARGIN_BRIDGE_VS_LIGHTWEIGHT_PLASTIC_FALSE_STAGE2_AND_EXHAUST_PARTS_EVENT_CAP", "sector": "auto_interior_module_global_OEM_volume_margin", "primary_archetype": "auto_interior_module_customer_mix_operating_leverage_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 16580.0, "evidence_available_at_that_date": "auto interior module / global OEM customer volume, utilization, operating leverage and margin-revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["customer_volume_proxy", "OEM_mix_quality", "operating_leverage_proxy", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "shallow_MAE90"], "stage4b_evidence_fields": ["later_auto_parts_cycle_watch", "valuation_repricing_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/200/200880/2024.csv", "profile_path": "atlas/symbol_profiles/200/200880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 50.78, "MFE_90D_pct": 50.78, "MFE_180D_pct": 50.78, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.45, "MAE_90D_pct": -1.45, "MAE_180D_pct": -23.94, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-07", "peak_price": 25000.0, "drawdown_after_peak_pct": -49.56, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_auto_parts_cycle_4B_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "mobility_margin_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_auto_interior_volume_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R9L91_C29_200880_2024-01-24_16580", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L91_C29_ECOPLASTIC_2024_STAGE2_FALSE_POSITIVE_LIGHTWEIGHT_EV_PARTS", "case_id": "R9L91_C29_ECOPLASTIC_2024_LIGHTWEIGHT_EV_PARTS_FALSE_STAGE2", "symbol": "038110", "company_name": "에코플라스틱", "round": "R9", "loop": "91", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_INTERIOR_MODULE_VOLUME_MARGIN_BRIDGE_VS_LIGHTWEIGHT_PLASTIC_FALSE_STAGE2_AND_EXHAUST_PARTS_EVENT_CAP", "sector": "lightweight_EV_plastic_parts_theme", "primary_archetype": "lightweight_EV_parts_theme_without_volume_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-02", "entry_date": "2024-02-02", "entry_price": 5510.0, "evidence_available_at_that_date": "lightweight plastic / EV parts and mobility theme spike proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["lightweight_EV_parts_theme", "relative_strength_spike", "customer_volume_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "deep_MAE180", "volume_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/038/038110/2024.csv", "profile_path": "atlas/symbol_profiles/038/038110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.36, "MFE_90D_pct": 4.36, "MFE_180D_pct": 4.36, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -14.7, "MAE_90D_pct": -25.77, "MAE_180D_pct": -50.45, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-06", "peak_price": 5750.0, "drawdown_after_peak_pct": -52.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "lightweight_EV_parts_theme_spike_was_false_stage2_due_missing_volume_margin_bridge", "four_b_evidence_type": ["mobility_theme_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_lightweight_EV_parts_without_volume_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_lightweight_EV_parts_theme_counts_without_volume_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2023-11-28_CA", "same_entry_group_id": "R9L91_C29_038110_2024-02-02_5510", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L91_C29_SJGSEJONG_2024_STAGE4B_EXHAUST_MOBILITY_PARTS_EVENT_CAP", "case_id": "R9L91_C29_SJGSEJONG_2024_EXHAUST_MOBILITY_PARTS_EVENT_CAP_4B", "symbol": "033530", "company_name": "SJG세종", "round": "R9", "loop": "91", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_INTERIOR_MODULE_VOLUME_MARGIN_BRIDGE_VS_LIGHTWEIGHT_PLASTIC_FALSE_STAGE2_AND_EXHAUST_PARTS_EVENT_CAP", "sector": "exhaust_mobility_parts_event_premium", "primary_archetype": "exhaust_mobility_parts_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-14", "entry_date": "2024-02-14", "entry_price": 6380.0, "evidence_available_at_that_date": "exhaust / mobility parts event premium and customer-volume watch after February spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["exhaust_mobility_parts_theme", "relative_strength_spike", "customer_volume_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "volume_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/033/033530/2024.csv", "profile_path": "atlas/symbol_profiles/033/033530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.21, "MFE_90D_pct": 7.21, "MFE_180D_pct": 7.21, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -11.44, "MAE_90D_pct": -35.74, "MAE_180D_pct": -35.97, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-06", "peak_price": 6840.0, "drawdown_after_peak_pct": -40.28, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "good_full_window_4B_timing_exhaust_mobility_parts_event_cap", "four_b_evidence_type": ["mobility_parts_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_exhaust_mobility_parts_premium", "current_profile_verdict": "current_profile_4B_too_late_if_exhaust_mobility_parts_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_1999_CA", "same_entry_group_id": "R9L91_C29_033530_2024-02-14_6380", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L91_C29_SEOYONEHWA_2024_AUTO_INTERIOR_MODULE_VOLUME_MARGIN_POSITIVE", "trigger_id": "R9L91_C29_SEOYONEHWA_2024_STAGE2_ACTIONABLE_AUTO_INTERIOR_VOLUME_MARGIN", "symbol": "200880", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "auto_interior_volume_margin_positive", "MFE_90D_pct": 50.78, "MAE_90D_pct": -1.45, "score_return_alignment_label": "auto_interior_volume_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L91_C29_ECOPLASTIC_2024_LIGHTWEIGHT_EV_PARTS_FALSE_STAGE2", "trigger_id": "R9L91_C29_ECOPLASTIC_2024_STAGE2_FALSE_POSITIVE_LIGHTWEIGHT_EV_PARTS", "symbol": "038110", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "lightweight_EV_parts_false_stage2", "MFE_90D_pct": 4.36, "MAE_90D_pct": -25.77, "score_return_alignment_label": "lightweight_EV_parts_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_lightweight_EV_parts_theme_counts_without_volume_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L91_C29_SJGSEJONG_2024_EXHAUST_MOBILITY_PARTS_EVENT_CAP_4B", "trigger_id": "R9L91_C29_SJGSEJONG_2024_STAGE4B_EXHAUST_MOBILITY_PARTS_EVENT_CAP", "symbol": "033530", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "exhaust_mobility_parts_event_cap_4B_guard", "MFE_90D_pct": 7.21, "MAE_90D_pct": -35.74, "score_return_alignment_label": "exhaust_mobility_parts_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_exhaust_mobility_parts_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": "91", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_INTERIOR_MODULE_VOLUME_MARGIN_BRIDGE_VS_LIGHTWEIGHT_PLASTIC_FALSE_STAGE2_AND_EXHAUST_PARTS_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["auto_interior_volume_margin_positive", "lightweight_EV_parts_false_stage2", "exhaust_mobility_parts_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
10. Add tests that bridge-missing C29 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R9
completed_loop = 91
next_round = R10
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
