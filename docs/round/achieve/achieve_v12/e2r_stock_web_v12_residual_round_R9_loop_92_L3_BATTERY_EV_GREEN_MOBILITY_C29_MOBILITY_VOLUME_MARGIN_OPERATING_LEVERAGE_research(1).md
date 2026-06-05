# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R9
scheduled_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = TIRE_OE_REPLACEMENT_VOLUME_MARGIN_BRIDGE_VS_EV_VALVE_FALSE_STAGE2_AND_INTERIOR_MODULE_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R9_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

This file is the corrected final output for this execution. The scheduler state after R8 loop 92 is R9 / loop 92. R9 allows the L3 mobility route or the L9 construction route; this run uses the L3 mobility route and returns to C29 with a fresh tire / EV-valve / interior-module split.

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
scheduled_loop = 92
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
round_sector_consistency = pass
computed_next_round = R10
computed_next_loop = 92
```

R9 loop 91 already used C29 with auto interior / lightweight EV parts / exhaust parts. This loop avoids that symbol set and uses a different C29 split around tire volume-margin and smaller auto-parts theme/event failure modes.

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
previous R9 loop-91 C29 symbols avoided: 200880, 038110, 033530
previous R8 loop-92 C26 symbols avoided: 042000, 089600, 123570
```

Selected rows avoid hard duplicates and top repeated C29 symbols:

```text
073240 / Stage2-Actionable / 2024-01-24
011320 / Stage2-Actionable / 2024-02-06
024900 / Stage4B / 2024-02-05
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
| 073240 | atlas/symbol_profiles/073/073240.json | selected 2024 window clean after old 2010/2018 CA candidates |
| 011320 | atlas/symbol_profiles/011/011320.json | selected 2024 window clean after old 1998~2003 CA candidates |
| 024900 | atlas/symbol_profiles/024/024900.json | selected 2024 window clean after old 1997~2014 CA candidates; 2025 name-change outside window |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R9L92_C29_KUMHOTIRE_2024_TIRE_VOLUME_MARGIN_BRIDGE_POSITIVE | 073240 | 2024-01-24 | yes | 180 | yes | yes | true |
| R9L92_C29_UNICK_2024_EV_VALVE_MOBILITY_THEME_FALSE_STAGE2 | 011320 | 2024-02-06 | yes | 180 | yes | yes | true |
| R9L92_C29_DUCKYANG_2024_INTERIOR_MODULE_MOBILITY_EVENT_CAP_4B | 024900 | 2024-02-05 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | TIRE_OE_REPLACEMENT_VOLUME_MARGIN_BRIDGE | Positive Stage2 requires tire OE/replacement volume, pricing, utilization, operating leverage, margin and revision bridge. |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | EV_VALVE_FALSE_STAGE2 | EV valve / hydrogen-mobility label without customer-volume and margin bridge can become false Stage2. |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | INTERIOR_MODULE_EVENT_CAP_4B | Interior-module mobility event premium should route to 4B when volume/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R9L92_C29_KUMHOTIRE_2024_TIRE_VOLUME_MARGIN_BRIDGE_POSITIVE | 073240 | 금호타이어 | positive | Tire volume/pricing/margin bridge produced strong MFE with shallow initial MAE. |
| R9L92_C29_UNICK_2024_EV_VALVE_MOBILITY_THEME_FALSE_STAGE2 | 011320 | 유니크 | counterexample | EV valve/mobility theme watch had low forward MFE without customer-volume/margin bridge. |
| R9L92_C29_DUCKYANG_2024_INTERIOR_MODULE_MOBILITY_EVENT_CAP_4B | 024900 | 덕양산업 | counterexample / 4B | Interior-module event premium capped around the February spike and later drew down severely. |

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
| Kumho Tire volume/margin bridge | historical public/report proxy | true | true | shadow-only positive |
| Unick EV-valve false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Duckyang interior-module event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 073240 | atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv | atlas/symbol_profiles/073/073240.json |
| 011320 | atlas/ohlcv_tradable_by_symbol_year/011/011320/2024.csv | atlas/symbol_profiles/011/011320.json |
| 024900 | atlas/ohlcv_tradable_by_symbol_year/024/024900/2024.csv | atlas/symbol_profiles/024/024900.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R9L92_C29_KUMHOTIRE_2024_STAGE2_ACTIONABLE_TIRE_VOLUME_MARGIN_BRIDGE | 073240 | Stage2-Actionable | 2024-01-24 | 5140 | positive | tire volume/pricing/margin bridge worked |
| R9L92_C29_UNICK_2024_STAGE2_FALSE_POSITIVE_EV_VALVE_MOBILITY_THEME | 011320 | Stage2-Actionable | 2024-02-06 | 5000 | counterexample | EV valve mobility false Stage2 |
| R9L92_C29_DUCKYANG_2024_STAGE4B_INTERIOR_MODULE_MOBILITY_EVENT_CAP | 024900 | Stage4B | 2024-02-05 | 5410 | counterexample/4B | interior-module mobility event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R9L92_C29_KUMHOTIRE_2024_STAGE2_ACTIONABLE_TIRE_VOLUME_MARGIN_BRIDGE | 5140 | 33.85 | -1.75 | 62.65 | -1.75 | 62.65 | -19.65 | 2024-05-07 | 8360 | -51.20 |
| R9L92_C29_UNICK_2024_STAGE2_FALSE_POSITIVE_EV_VALVE_MOBILITY_THEME | 5000 | 5.00 | -5.90 | 5.00 | -11.70 | 5.00 | -11.70 | 2024-02-06 | 5250 | -16.76 |
| R9L92_C29_DUCKYANG_2024_STAGE4B_INTERIOR_MODULE_MOBILITY_EVENT_CAP | 5410 | 13.68 | -16.91 | 13.68 | -19.41 | 13.68 | -44.73 | 2024-02-05 | 6150 | -51.38 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C29 Stage2 needs customer volume / product mix / utilization / pricing / margin / revision bridge |
| local_4b_watch_guard | strengthen: auto-parts event premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: high or later-cycle MAE rows cannot promote without durable volume/margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is mobility volume/margin bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 073240 | good_stage2_with_later_watch | Tire volume/pricing/margin bridge produced strong MFE, but later cycle/valuation watch remains necessary. |
| 011320 | bad_stage2 | EV-valve theme lacked durable customer-volume/margin bridge. |
| 024900 | good_4B | Interior-module event premium capped after the February spike and later suffered severe MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 011320 EV-valve false Stage2 | 0.95 | 0.95 | false Stage2 due missing volume/margin bridge |
| 024900 interior-module cap | 0.88 | 0.88 | good full-window 4B timing despite non-perfect peak proximity because later MAE confirmed cap |
| 073240 tire volume/margin bridge | n/a | n/a | positive Stage2, but later tire-cycle valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 011320 / 024900
```

No hard 4C candidate is proposed. R9 loop 92 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 mobility volume/margin operating-leverage cases, Stage2 requires verified customer volume, product/customer mix, utilization, pricing, operating leverage, gross-margin recovery, or revision bridge. Tire, EV valve, hydrogen mobility, interior module, auto-parts, or mobility label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
rule = C29 should split true volume/pricing/margin operating-leverage positives from EV-valve false Stage2 and interior-module event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 27.11 | -10.95 | 0.67 | mixed; C29 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 27.11 | -10.95 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L3 volume/pricing/margin bridge required | 2 | 33.83 | -6.73 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C29 bridge vs event-cap split | 2 | 33.83 | -6.73 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing mobility themes as positive | 1 | 62.65 | -1.75 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 073240 tire margin bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 62.65 | -1.75 | tire_volume_margin_positive |
| 011320 EV-valve false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 5.00 | -11.70 | EV_valve_mobility_false_stage2 |
| 024900 interior-module cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 13.68 | -19.41 | interior_module_mobility_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_OE_REPLACEMENT_VOLUME_MARGIN_BRIDGE_VS_EV_VALVE_FALSE_STAGE2_AND_INTERIOR_MODULE_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C29 tire volume/margin positive, EV valve mobility-theme false Stage2, and interior-module mobility event-cap 4B split while avoiding top repeated C29 symbols."}
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
residual_error_types_found: tire_volume_margin_positive, EV_valve_mobility_false_stage2, interior_module_mobility_event_cap_4B
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
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,C29_requires_volume_pricing_utilization_margin_revision_bridge,0,"C29 Stage2 should require customer volume, product/customer mix, utilization, pricing or operating-leverage margin bridge, not mobility/EV/auto-parts label alone","Kumho Tire positive worked; Unick and Duckyang event/theme rows failed positive-stage promotion","R9L92_C29_KUMHOTIRE_2024_STAGE2_ACTIONABLE_TIRE_VOLUME_MARGIN_BRIDGE|R9L92_C29_UNICK_2024_STAGE2_FALSE_POSITIVE_EV_VALVE_MOBILITY_THEME|R9L92_C29_DUCKYANG_2024_STAGE4B_INTERIOR_MODULE_MOBILITY_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,cap_bridge_missing_auto_parts_theme_and_event_premiums_as_4B_watch,0,"EV valve/interior-module mobility event premiums can peak before customer-volume and margin bridge is proven","Unick had small forward MFE; Duckyang showed event-cap behavior after the February spike with severe later MAE","R9L92_C29_UNICK_2024_STAGE2_FALSE_POSITIVE_EV_VALVE_MOBILITY_THEME|R9L92_C29_DUCKYANG_2024_STAGE4B_INTERIOR_MODULE_MOBILITY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,block_positive_stage_when_mobility_theme_has_high_or_later_MAE_without_volume_margin_bridge,0,"High or later-cycle MAE after bridge-missing mobility entries should block Stage2/Stage3 promotion unless volume and margin evidence survives","Duckyang MAE180=-44.73 and Kumho Tire positive still needed later valuation watch after peak drawdown","R9L92_C29_UNICK_2024_STAGE2_FALSE_POSITIVE_EV_VALVE_MOBILITY_THEME|R9L92_C29_DUCKYANG_2024_STAGE4B_INTERIOR_MODULE_MOBILITY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R9L92_C29_KUMHOTIRE_2024_TIRE_VOLUME_MARGIN_BRIDGE_POSITIVE", "symbol": "073240", "company_name": "금호타이어", "round": "R9", "loop": "92", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_OE_REPLACEMENT_VOLUME_MARGIN_BRIDGE_VS_EV_VALVE_FALSE_STAGE2_AND_INTERIOR_MODULE_EVENT_CAP", "case_type": "structural_success_with_later_cycle_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R9L92_C29_KUMHOTIRE_2024_STAGE2_ACTIONABLE_TIRE_VOLUME_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Tire OE/replacement volume, pricing and operating-leverage margin bridge produced strong 30D/90D/180D MFE with very shallow initial MAE. C29 works when mobility volume and product/customer mix convert into utilization, pricing, margin and revision bridge, but later cycle/valuation watch remains necessary.", "current_profile_verdict": "current_profile_kept_but_C29_positive_requires_volume_pricing_margin_revision_bridge_not_mobility_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2010/2018 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R9L92_C29_UNICK_2024_EV_VALVE_MOBILITY_THEME_FALSE_STAGE2", "symbol": "011320", "company_name": "유니크", "round": "R9", "loop": "92", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_OE_REPLACEMENT_VOLUME_MARGIN_BRIDGE_VS_EV_VALVE_FALSE_STAGE2_AND_INTERIOR_MODULE_EVENT_CAP", "case_type": "failed_rerating_EV_valve_theme_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R9L92_C29_UNICK_2024_STAGE2_FALSE_POSITIVE_EV_VALVE_MOBILITY_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "EV valve / hydrogen-mobility parts theme watch had only small forward MFE and then persistent drawdown. C29 Stage2 should not be awarded without customer volume, SOP/order visibility, utilization, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_EV_valve_mobility_theme_counts_without_volume_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1998~2003 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R9L92_C29_DUCKYANG_2024_INTERIOR_MODULE_MOBILITY_EVENT_CAP_4B", "symbol": "024900", "company_name": "덕양산업", "round": "R9", "loop": "92", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_OE_REPLACEMENT_VOLUME_MARGIN_BRIDGE_VS_EV_VALVE_FALSE_STAGE2_AND_INTERIOR_MODULE_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R9L92_C29_DUCKYANG_2024_STAGE4B_INTERIOR_MODULE_MOBILITY_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Interior-module / mobility-parts event premium capped around the February spike and then suffered severe 180D MAE. C29 should route bridge-missing auto-parts event premiums to 4B unless volume, customer mix, utilization and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_interior_module_mobility_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1997~2014 corporate-action candidates and before the 2025 name-change period. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R9L92_C29_KUMHOTIRE_2024_STAGE2_ACTIONABLE_TIRE_VOLUME_MARGIN_BRIDGE", "case_id": "R9L92_C29_KUMHOTIRE_2024_TIRE_VOLUME_MARGIN_BRIDGE_POSITIVE", "symbol": "073240", "company_name": "금호타이어", "round": "R9", "loop": "92", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_OE_REPLACEMENT_VOLUME_MARGIN_BRIDGE_VS_EV_VALVE_FALSE_STAGE2_AND_INTERIOR_MODULE_EVENT_CAP", "sector": "tire_OE_replacement_volume_pricing_margin", "primary_archetype": "tire_volume_pricing_utilization_operating_leverage_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 5140.0, "evidence_available_at_that_date": "tire OE/replacement volume, pricing, utilization, operating leverage and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["tire_volume_proxy", "OE_replacement_mix_proxy", "pricing_margin_bridge_proxy", "utilization_operating_leverage_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["strong_MFE30", "very_high_MFE90", "shallow_MAE90"], "stage4b_evidence_fields": ["later_tire_cycle_valuation_watch", "post_peak_drawdown_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv", "profile_path": "atlas/symbol_profiles/073/073240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 33.85, "MFE_90D_pct": 62.65, "MFE_180D_pct": 62.65, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.75, "MAE_90D_pct": -1.75, "MAE_180D_pct": -19.65, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-07", "peak_price": 8360.0, "drawdown_after_peak_pct": -51.2, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_tire_cycle_valuation_4B_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "mobility_margin_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_tire_volume_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2010_2018_CA", "same_entry_group_id": "R9L92_C29_073240_2024-01-24_5140", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L92_C29_UNICK_2024_STAGE2_FALSE_POSITIVE_EV_VALVE_MOBILITY_THEME", "case_id": "R9L92_C29_UNICK_2024_EV_VALVE_MOBILITY_THEME_FALSE_STAGE2", "symbol": "011320", "company_name": "유니크", "round": "R9", "loop": "92", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_OE_REPLACEMENT_VOLUME_MARGIN_BRIDGE_VS_EV_VALVE_FALSE_STAGE2_AND_INTERIOR_MODULE_EVENT_CAP", "sector": "EV_valve_hydrogen_mobility_parts_theme", "primary_archetype": "EV_valve_theme_without_volume_utilization_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-06", "entry_date": "2024-02-06", "entry_price": 5000.0, "evidence_available_at_that_date": "EV valve / hydrogen-mobility parts theme and customer order expectation proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["EV_valve_mobility_theme", "customer_order_expectation", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_forward_MFE", "volume_utilization_margin_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011320/2024.csv", "profile_path": "atlas/symbol_profiles/011/011320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.0, "MFE_90D_pct": 5.0, "MFE_180D_pct": 5.0, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -5.9, "MAE_90D_pct": -11.7, "MAE_180D_pct": -11.7, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-06", "peak_price": 5250.0, "drawdown_after_peak_pct": -16.76, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "EV_valve_mobility_theme_watch_was_false_stage2_due_missing_volume_margin_bridge", "four_b_evidence_type": ["mobility_theme_premium", "positioning_overheat_watch", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_EV_valve_mobility_theme_without_volume_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_EV_valve_mobility_theme_counts_without_volume_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1998_2003_CA", "same_entry_group_id": "R9L92_C29_011320_2024-02-06_5000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L92_C29_DUCKYANG_2024_STAGE4B_INTERIOR_MODULE_MOBILITY_EVENT_CAP", "case_id": "R9L92_C29_DUCKYANG_2024_INTERIOR_MODULE_MOBILITY_EVENT_CAP_4B", "symbol": "024900", "company_name": "덕양산업", "round": "R9", "loop": "92", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_OE_REPLACEMENT_VOLUME_MARGIN_BRIDGE_VS_EV_VALVE_FALSE_STAGE2_AND_INTERIOR_MODULE_EVENT_CAP", "sector": "interior_module_mobility_parts_event_premium", "primary_archetype": "interior_module_mobility_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-05", "entry_date": "2024-02-05", "entry_price": 5410.0, "evidence_available_at_that_date": "interior-module / auto-parts event premium after early-February mobility spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["interior_module_mobility_event", "customer_volume_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE180", "volume_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024900/2024.csv", "profile_path": "atlas/symbol_profiles/024/024900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.68, "MFE_90D_pct": 13.68, "MFE_180D_pct": 13.68, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -16.91, "MAE_90D_pct": -19.41, "MAE_180D_pct": -44.73, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-05", "peak_price": 6150.0, "drawdown_after_peak_pct": -51.38, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "good_full_window_4B_timing_interior_module_mobility_event_cap", "four_b_evidence_type": ["mobility_parts_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_interior_module_mobility_parts_premium", "current_profile_verdict": "current_profile_4B_too_late_if_interior_module_mobility_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1997_2014_CA_before_2025_name_change", "same_entry_group_id": "R9L92_C29_024900_2024-02-05_5410", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L92_C29_KUMHOTIRE_2024_TIRE_VOLUME_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R9L92_C29_KUMHOTIRE_2024_STAGE2_ACTIONABLE_TIRE_VOLUME_MARGIN_BRIDGE", "symbol": "073240", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "tire_volume_margin_positive", "MFE_90D_pct": 62.65, "MAE_90D_pct": -1.75, "score_return_alignment_label": "tire_volume_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L92_C29_UNICK_2024_EV_VALVE_MOBILITY_THEME_FALSE_STAGE2", "trigger_id": "R9L92_C29_UNICK_2024_STAGE2_FALSE_POSITIVE_EV_VALVE_MOBILITY_THEME", "symbol": "011320", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "EV_valve_mobility_false_stage2", "MFE_90D_pct": 5.0, "MAE_90D_pct": -11.7, "score_return_alignment_label": "EV_valve_mobility_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_EV_valve_mobility_theme_counts_without_volume_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L92_C29_DUCKYANG_2024_INTERIOR_MODULE_MOBILITY_EVENT_CAP_4B", "trigger_id": "R9L92_C29_DUCKYANG_2024_STAGE4B_INTERIOR_MODULE_MOBILITY_EVENT_CAP", "symbol": "024900", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "interior_module_mobility_event_cap_4B_guard", "MFE_90D_pct": 13.68, "MAE_90D_pct": -19.41, "score_return_alignment_label": "interior_module_mobility_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_interior_module_mobility_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": "92", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_OE_REPLACEMENT_VOLUME_MARGIN_BRIDGE_VS_EV_VALVE_FALSE_STAGE2_AND_INTERIOR_MODULE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["tire_volume_margin_positive", "EV_valve_mobility_false_stage2", "interior_module_mobility_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_loop = 92
next_round = R10
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
