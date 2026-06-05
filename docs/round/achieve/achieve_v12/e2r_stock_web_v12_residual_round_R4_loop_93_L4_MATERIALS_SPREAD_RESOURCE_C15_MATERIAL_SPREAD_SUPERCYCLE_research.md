# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = STEEL_PIPE_EXPORT_SPREAD_MARGIN_BRIDGE_VS_STEEL_COIL_FALSE_STAGE2_AND_OIL_RESOURCE_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R4_loop_93_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
```

This file is the corrected final output for this execution. The scheduler state after R3 loop 93 is R4 / loop 93. R4 is the L4 materials/spread/resource round, and this run fills C15 material spread supercycle with a new positive-vs-counterexample split.

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
scheduled_round = R4
scheduled_loop = 93
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
round_sector_consistency = pass
computed_next_round = R5
computed_next_loop = 93
```

C15 currently has many positive Stage2 rows but few explicit bridge-missing false Stage2 examples. This loop adds one steel-pipe spread positive, one steel-coil false Stage2, and one oil/resource event-cap 4B row.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C15_MATERIAL_SPREAD_SUPERCYCLE = 28 rows / 11 symbols / good-bad Stage2 13-0 / 4B-4C 3-0
top covered symbols include 103140(6), 012800(5), 025820(5), 004560(3), 021050(3), 001780(1)
previous R4 loop-89 C16 symbols avoided: 009520, 011810, 037370
previous R4 loop-90 C15 symbols avoided: 024840, 018470, 006110
previous R4 loop-91 C17 symbols avoided: 010060, 007690, 298000
previous R4 loop-92 C16 symbols avoided: 006260, 012800, 025820
previous R3 loop-93 C11 symbols avoided: 317330, 382840, 008730
```

Selected rows avoid hard duplicates and top repeated C15 symbols:

```text
003030 / Stage2-Actionable / 2024-01-24
016380 / Stage2-Actionable / 2024-02-05
024060 / Stage4B / 2024-06-04
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
| 003030 | atlas/symbol_profiles/003/003030.json | selected 2024 window clean after old 2001/2018/2019 CA candidates |
| 016380 | atlas/symbol_profiles/016/016380.json | selected 2024 window clean after old 1999~2019 CA candidates |
| 024060 | atlas/symbol_profiles/024/024060.json | selected 2024 window clean after old 1997~2008 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R4L93_C15_SEAHSTEELHOLDINGS_2024_STEEL_PIPE_EXPORT_SPREAD_MARGIN_POSITIVE | 003030 | 2024-01-24 | yes | 180 | yes | yes | true |
| R4L93_C15_KGSTEEL_2024_STEEL_COIL_SPREAD_FALSE_STAGE2 | 016380 | 2024-02-05 | yes | 180 | yes | yes | true |
| R4L93_C15_HEUNGGOO_2024_OIL_RESOURCE_SPREAD_EVENT_CAP_4B | 024060 | 2024-06-04 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C15_MATERIAL_SPREAD_SUPERCYCLE | STEEL_PIPE_EXPORT_SPREAD_MARGIN_BRIDGE | Positive Stage2 requires export spread, raw-material cost spread, product/customer mix, margin and revision bridge. |
| C15_MATERIAL_SPREAD_SUPERCYCLE | STEEL_COIL_FALSE_STAGE2 | Steel/material spread label without ASP and margin bridge can become false Stage2. |
| C15_MATERIAL_SPREAD_SUPERCYCLE | OIL_RESOURCE_EVENT_CAP_4B | Oil/resource event premium should route to 4B when inventory spread and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R4L93_C15_SEAHSTEELHOLDINGS_2024_STEEL_PIPE_EXPORT_SPREAD_MARGIN_POSITIVE | 003030 | 세아제강지주 | positive | Steel-pipe export spread / product-mix bridge produced positive MFE with shallow early MAE. |
| R4L93_C15_KGSTEEL_2024_STEEL_COIL_SPREAD_FALSE_STAGE2 | 016380 | KG스틸 | counterexample | Steel-coil spread watch had near-zero MFE and later material drawdown. |
| R4L93_C15_HEUNGGOO_2024_OIL_RESOURCE_SPREAD_EVENT_CAP_4B | 024060 | 흥구석유 | counterexample / 4B | Oil/resource event premium capped at the June spike and then de-rated. |

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
| SeAH Steel Holdings steel-pipe export spread | historical public/report proxy | true | true | shadow-only positive |
| KG Steel steel-coil spread false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Heunggoo Oil resource event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 003030 | atlas/ohlcv_tradable_by_symbol_year/003/003030/2024.csv | atlas/symbol_profiles/003/003030.json |
| 016380 | atlas/ohlcv_tradable_by_symbol_year/016/016380/2024.csv | atlas/symbol_profiles/016/016380.json |
| 024060 | atlas/ohlcv_tradable_by_symbol_year/024/024060/2024.csv | atlas/symbol_profiles/024/024060.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R4L93_C15_SEAHSTEELHOLDINGS_2024_STAGE2_ACTIONABLE_STEEL_PIPE_EXPORT_SPREAD_MARGIN | 003030 | Stage2-Actionable | 2024-01-24 | 197600 | positive | steel-pipe export spread / margin bridge worked |
| R4L93_C15_KGSTEEL_2024_STAGE2_FALSE_POSITIVE_STEEL_COIL_SPREAD_WATCH | 016380 | Stage2-Actionable | 2024-02-05 | 7970 | counterexample | steel spread false Stage2 |
| R4L93_C15_HEUNGGOO_2024_STAGE4B_OIL_RESOURCE_SPREAD_EVENT_CAP | 024060 | Stage4B | 2024-06-04 | 19240 | counterexample/4B | oil/resource spread event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R4L93_C15_SEAHSTEELHOLDINGS_2024_STAGE2_ACTIONABLE_STEEL_PIPE_EXPORT_SPREAD_MARGIN | 197600 | 19.69 | -1.27 | 21.71 | -1.27 | 21.71 | -8.15 | 2024-03-27 | 240500 | -24.53 |
| R4L93_C15_KGSTEEL_2024_STAGE2_FALSE_POSITIVE_STEEL_COIL_SPREAD_WATCH | 7970 | 1.51 | -12.17 | 1.51 | -19.20 | 1.51 | -33.50 | 2024-02-05 | 8090 | -34.49 |
| R4L93_C15_HEUNGGOO_2024_STAGE4B_OIL_RESOURCE_SPREAD_EVENT_CAP | 19240 | 8.89 | -28.79 | 8.89 | -28.85 | 8.89 | -28.85 | 2024-06-04 | 20950 | -34.65 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C15 Stage2 needs spread / product mix / volume / margin / revision bridge |
| local_4b_watch_guard | strengthen: commodity/resource event premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: high-MAE spread-theme rows cannot promote without durable margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is spread/margin bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 003030 | good_stage2_with_later_watch | Steel-pipe export spread bridge produced positive MFE and shallow early MAE. |
| 016380 | bad_stage2 | Steel spread watch had almost no MFE and later persistent MAE. |
| 024060 | good_4B | Oil/resource event premium capped at the June spike and de-rated. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 016380 steel spread false Stage2 | 0.99 | 0.99 | false Stage2 due missing ASP/volume/margin bridge |
| 024060 oil/resource cap | 0.92 | 0.92 | good full-window 4B timing after event spike |
| 003030 steel-pipe spread bridge | n/a | n/a | positive Stage2, but later material-spread valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 016380 / 024060
```

No hard 4C candidate is proposed. R4 loop 93 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L4 material spread/supercycle cases, Stage2 requires verified raw-material cost spread, ASP pass-through, product/customer mix, volume, margin, or revision bridge. Steel, pipe, coil, copper, oil, resource, commodity, or supercycle label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
rule = C15 should split true spread/margin positives from steel-coil false Stage2 and oil/resource event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 10.70 | -16.44 | 0.67 | mixed; C15 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 10.70 | -16.44 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L4 spread/margin bridge required | 2 | 11.61 | -10.24 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C15 bridge vs event-cap split | 2 | 11.61 | -10.24 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing commodity spread themes as positive | 1 | 21.71 | -1.27 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 003030 steel-pipe spread bridge | 66 | Stage2-Watch | 74 | Stage2-Actionable | 21.71 | -1.27 | steel_pipe_export_spread_margin_positive |
| 016380 steel spread false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 1.51 | -19.20 | steel_coil_spread_false_stage2 |
| 024060 oil/resource cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 8.89 | -28.85 | oil_resource_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_PIPE_EXPORT_SPREAD_MARGIN_BRIDGE_VS_STEEL_COIL_FALSE_STAGE2_AND_OIL_RESOURCE_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C15 steel-pipe spread margin positive, steel-coil spread false Stage2, and oil/resource event-cap 4B split while avoiding top repeated C15 symbols."}
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
residual_error_types_found: steel_pipe_export_spread_margin_positive, steel_coil_spread_false_stage2, oil_resource_event_cap_4B
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
- C15 material-spread bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,configured,C15_requires_spread_product_mix_volume_margin_revision_bridge,0,"C15 Stage2 should require export price spread, raw-material cost spread, product/customer mix, volume, margin, or revision bridge, not commodity/material label alone","SeAH Steel Holdings positive worked; KG Steel and Heunggoo Oil theme/event rows failed positive-stage promotion","R4L93_C15_SEAHSTEELHOLDINGS_2024_STAGE2_ACTIONABLE_STEEL_PIPE_EXPORT_SPREAD_MARGIN|R4L93_C15_KGSTEEL_2024_STAGE2_FALSE_POSITIVE_STEEL_COIL_SPREAD_WATCH|R4L93_C15_HEUNGGOO_2024_STAGE4B_OIL_RESOURCE_SPREAD_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,configured,cap_bridge_missing_commodity_spread_event_premiums_as_4B_watch,0,"Commodity/resource event premiums can peak before actual spread and margin bridge is proven","KG Steel had near-zero forward MFE; Heunggoo Oil showed 4B event-cap behavior after June oil/resource spike","R4L93_C15_KGSTEEL_2024_STAGE2_FALSE_POSITIVE_STEEL_COIL_SPREAD_WATCH|R4L93_C15_HEUNGGOO_2024_STAGE4B_OIL_RESOURCE_SPREAD_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,configured,block_positive_stage_when_spread_theme_has_high_MAE_without_margin_bridge,0,"High MAE after bridge-missing material spread entries should block Stage2/Stage3 promotion unless spread, volume and margin evidence survives","KG Steel MAE180=-33.50 and Heunggoo Oil MAE90=-28.85","R4L93_C15_KGSTEEL_2024_STAGE2_FALSE_POSITIVE_STEEL_COIL_SPREAD_WATCH|R4L93_C15_HEUNGGOO_2024_STAGE4B_OIL_RESOURCE_SPREAD_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L93_C15_SEAHSTEELHOLDINGS_2024_STEEL_PIPE_EXPORT_SPREAD_MARGIN_POSITIVE", "symbol": "003030", "company_name": "세아제강지주", "round": "R4", "loop": "93", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_PIPE_EXPORT_SPREAD_MARGIN_BRIDGE_VS_STEEL_COIL_FALSE_STAGE2_AND_OIL_RESOURCE_EVENT_CAP", "case_type": "structural_success_with_later_spread_cycle_watch", "positive_or_counterexample": "positive", "best_trigger": "R4L93_C15_SEAHSTEELHOLDINGS_2024_STAGE2_ACTIONABLE_STEEL_PIPE_EXPORT_SPREAD_MARGIN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Steel-pipe export spread / product-mix margin bridge produced positive 30D/90D MFE with shallow early MAE. C15 works when material-spread narrative maps into export price, raw-material spread, product mix, order/backlog quality, and margin/revision bridge.", "current_profile_verdict": "current_profile_kept_but_C15_positive_requires_spread_product_mix_margin_revision_bridge_not_steel_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2001/2018/2019 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R4L93_C15_KGSTEEL_2024_STEEL_COIL_SPREAD_FALSE_STAGE2", "symbol": "016380", "company_name": "KG스틸", "round": "R4", "loop": "93", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_PIPE_EXPORT_SPREAD_MARGIN_BRIDGE_VS_STEEL_COIL_FALSE_STAGE2_AND_OIL_RESOURCE_EVENT_CAP", "case_type": "failed_rerating_steel_spread_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R4L93_C15_KGSTEEL_2024_STAGE2_FALSE_POSITIVE_STEEL_COIL_SPREAD_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Steel-coil / material spread recovery watch produced almost no forward MFE and then persistent 90D/180D MAE. C15 Stage2 should not be awarded without ASP pass-through, raw-material spread durability, volume/customer mix, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_steel_spread_theme_counts_without_ASP_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1999~2019 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R4L93_C15_HEUNGGOO_2024_OIL_RESOURCE_SPREAD_EVENT_CAP_4B", "symbol": "024060", "company_name": "흥구석유", "round": "R4", "loop": "93", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_PIPE_EXPORT_SPREAD_MARGIN_BRIDGE_VS_STEEL_COIL_FALSE_STAGE2_AND_OIL_RESOURCE_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L93_C15_HEUNGGOO_2024_STAGE4B_OIL_RESOURCE_SPREAD_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Oil/resource spread event premium capped at the June spike and then suffered high MAE. C15 should route bridge-missing oil/resource event premiums to 4B unless inventory spread, refining/distribution margin, volume and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_oil_resource_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1997~2008 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L93_C15_SEAHSTEELHOLDINGS_2024_STAGE2_ACTIONABLE_STEEL_PIPE_EXPORT_SPREAD_MARGIN", "case_id": "R4L93_C15_SEAHSTEELHOLDINGS_2024_STEEL_PIPE_EXPORT_SPREAD_MARGIN_POSITIVE", "symbol": "003030", "company_name": "세아제강지주", "round": "R4", "loop": "93", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_PIPE_EXPORT_SPREAD_MARGIN_BRIDGE_VS_STEEL_COIL_FALSE_STAGE2_AND_OIL_RESOURCE_EVENT_CAP", "sector": "steel_pipe_export_spread_product_mix_margin", "primary_archetype": "steel_pipe_export_spread_product_mix_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 197600.0, "evidence_available_at_that_date": "steel-pipe export spread, product mix, energy pipe demand, raw-material spread, order quality and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["export_price_spread_proxy", "raw_material_cost_spread_proxy", "product_mix_bridge", "order_backlog_quality_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "positive_MFE90", "shallow_MAE90"], "stage4b_evidence_fields": ["later_steel_spread_cycle_watch", "post_peak_drawdown_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003030/2024.csv", "profile_path": "atlas/symbol_profiles/003/003030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 19.69, "MFE_90D_pct": 21.71, "MFE_180D_pct": 21.71, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.27, "MAE_90D_pct": -1.27, "MAE_180D_pct": -8.15, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-27", "peak_price": 240500.0, "drawdown_after_peak_pct": -24.53, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_steel_spread_cycle_4B_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "steel_spread_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_steel_pipe_export_spread_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2001_2018_2019_CA", "same_entry_group_id": "R4L93_C15_003030_2024-01-24_197600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L93_C15_KGSTEEL_2024_STAGE2_FALSE_POSITIVE_STEEL_COIL_SPREAD_WATCH", "case_id": "R4L93_C15_KGSTEEL_2024_STEEL_COIL_SPREAD_FALSE_STAGE2", "symbol": "016380", "company_name": "KG스틸", "round": "R4", "loop": "93", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_PIPE_EXPORT_SPREAD_MARGIN_BRIDGE_VS_STEEL_COIL_FALSE_STAGE2_AND_OIL_RESOURCE_EVENT_CAP", "sector": "steel_coil_material_spread_recovery_watch", "primary_archetype": "steel_spread_watch_without_ASP_volume_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-05", "entry_date": "2024-02-05", "entry_price": 7970.0, "evidence_available_at_that_date": "steel coil / material spread recovery watch and raw-material cost relief expectation proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["steel_spread_recovery_watch", "raw_material_cost_relief_expectation", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["near_zero_MFE90", "ASP_volume_margin_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/016/016380/2024.csv", "profile_path": "atlas/symbol_profiles/016/016380.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.51, "MFE_90D_pct": 1.51, "MFE_180D_pct": 1.51, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -12.17, "MAE_90D_pct": -19.2, "MAE_180D_pct": -33.5, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-05", "peak_price": 8090.0, "drawdown_after_peak_pct": -34.49, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.99, "four_b_full_window_peak_proximity": 0.99, "four_b_timing_verdict": "steel_spread_watch_was_false_stage2_due_missing_ASP_volume_margin_bridge", "four_b_evidence_type": ["steel_spread_recovery_premium", "positioning_overheat_watch", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_steel_spread_watch_without_ASP_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_steel_spread_theme_counts_without_ASP_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1999_2019_CA", "same_entry_group_id": "R4L93_C15_016380_2024-02-05_7970", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L93_C15_HEUNGGOO_2024_STAGE4B_OIL_RESOURCE_SPREAD_EVENT_CAP", "case_id": "R4L93_C15_HEUNGGOO_2024_OIL_RESOURCE_SPREAD_EVENT_CAP_4B", "symbol": "024060", "company_name": "흥구석유", "round": "R4", "loop": "93", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_PIPE_EXPORT_SPREAD_MARGIN_BRIDGE_VS_STEEL_COIL_FALSE_STAGE2_AND_OIL_RESOURCE_EVENT_CAP", "sector": "oil_resource_distribution_spread_event_premium", "primary_archetype": "oil_resource_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-06-04", "entry_date": "2024-06-04", "entry_price": 19240.0, "evidence_available_at_that_date": "oil/resource spread event premium and geopolitical oil-price spike after June event; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["oil_resource_event_premium", "geopolitical_oil_price_spike", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "inventory_spread_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024060/2024.csv", "profile_path": "atlas/symbol_profiles/024/024060.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.89, "MFE_90D_pct": 8.89, "MFE_180D_pct": 8.89, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -28.79, "MAE_90D_pct": -28.85, "MAE_180D_pct": -28.85, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-04", "peak_price": 20950.0, "drawdown_after_peak_pct": -34.65, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_full_window_4B_timing_oil_resource_spread_event_cap", "four_b_evidence_type": ["oil_resource_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_oil_resource_spread_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_oil_resource_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1997_2008_CA", "same_entry_group_id": "R4L93_C15_024060_2024-06-04_19240", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L93_C15_SEAHSTEELHOLDINGS_2024_STEEL_PIPE_EXPORT_SPREAD_MARGIN_POSITIVE", "trigger_id": "R4L93_C15_SEAHSTEELHOLDINGS_2024_STAGE2_ACTIONABLE_STEEL_PIPE_EXPORT_SPREAD_MARGIN", "symbol": "003030", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 50, "margin_bridge_score": 55, "revision_score": 50, "relative_strength_score": 60, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "steel_pipe_export_spread_margin_positive", "MFE_90D_pct": 21.71, "MAE_90D_pct": -1.27, "score_return_alignment_label": "steel_pipe_export_spread_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L93_C15_KGSTEEL_2024_STEEL_COIL_SPREAD_FALSE_STAGE2", "trigger_id": "R4L93_C15_KGSTEEL_2024_STAGE2_FALSE_POSITIVE_STEEL_COIL_SPREAD_WATCH", "symbol": "016380", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "steel_coil_spread_false_stage2", "MFE_90D_pct": 1.51, "MAE_90D_pct": -19.2, "score_return_alignment_label": "steel_coil_spread_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_steel_spread_theme_counts_without_ASP_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L93_C15_HEUNGGOO_2024_OIL_RESOURCE_SPREAD_EVENT_CAP_4B", "trigger_id": "R4L93_C15_HEUNGGOO_2024_STAGE4B_OIL_RESOURCE_SPREAD_EVENT_CAP", "symbol": "024060", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "oil_resource_event_cap_4B_guard", "MFE_90D_pct": 8.89, "MAE_90D_pct": -28.85, "score_return_alignment_label": "oil_resource_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_oil_resource_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "93", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_PIPE_EXPORT_SPREAD_MARGIN_BRIDGE_VS_STEEL_COIL_FALSE_STAGE2_AND_OIL_RESOURCE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["steel_pipe_export_spread_margin_positive", "steel_coil_spread_false_stage2", "oil_resource_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
10. Add tests that bridge-missing C15 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R4
completed_loop = 93
next_round = R5
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
