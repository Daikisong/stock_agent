# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE_VS_PETROCHEM_SPREAD_FALSE_STAGE2_AND_OIL_PRODUCT_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R4_loop_94_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
```

This file is the corrected final output for this execution. The scheduler state after R3 loop 94 is R4 / loop 94. R4 is the L4 materials/spread/resource round, and this run fills C17 chemical/commodity margin-spread behavior rather than repeating the immediately preceding R4 loop 93 C15 material-spread file.

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
scheduled_loop = 94
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
round_sector_consistency = pass
computed_next_round = R5
computed_next_loop = 94
```

C17 is a margin-spread archetype. A commodity label is only the smell of smoke; the fire is ASP pass-through, input-cost relief, product mix, utilization, volume and margin revision. This loop separates that bridge from petrochemical false Stage2 and oil-product event caps.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD = 21 rows / 15 symbols / good-bad Stage2 8-3 / 4B-4C 4-0
top covered symbols include 004000(3), 006650(2), 011780(2), 014680(2), 298020(2), 001390(1)
previous R4 loop-90 C15 symbols avoided: 024840, 018470, 006110
previous R4 loop-91 C17 symbols avoided: 010060, 007690, 298000
previous R4 loop-92 C16 symbols avoided: 006260, 012800, 025820
previous R4 loop-93 C15 symbols avoided: 003030, 016380, 024060
previous R3 loop-94 C12 symbols avoided: 036830, 418550, 078600
```

Selected rows avoid hard duplicates and top repeated C17 symbols:

```text
002380 / Stage2-Actionable / 2024-01-24
011170 / Stage2-Actionable / 2024-02-01
004090 / Stage4B / 2024-04-09
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
| 002380 | atlas/symbol_profiles/002/002380.json | selected 2024 window clean after old CA candidates |
| 011170 | atlas/symbol_profiles/011/011170.json | no relevant 2024 CA contamination |
| 004090 | atlas/symbol_profiles/004/004090.json | selected 2024 window clean after old 2021 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R4L94_C17_KCC_2024_SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE_POSITIVE | 002380 | 2024-01-24 | yes | 180 | yes | yes | true |
| R4L94_C17_LOTTECHEM_2024_PETROCHEM_SPREAD_FALSE_STAGE2 | 011170 | 2024-02-01 | yes | 180 | yes | yes | true |
| R4L94_C17_KOREAPETROLEUM_2024_OIL_PRODUCT_SPREAD_EVENT_CAP_4B | 004090 | 2024-04-09 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE | Positive Stage2 requires ASP pass-through, input-cost relief, product/customer mix, margin and revision bridge. |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | PETROCHEM_SPREAD_FALSE_STAGE2 | Petrochemical spread label without utilization and margin bridge can become false Stage2. |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | OIL_PRODUCT_EVENT_CAP_4B | Oil-product/asphalt spread event premium should route to 4B when inventory and margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R4L94_C17_KCC_2024_SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE_POSITIVE | 002380 | KCC | positive | Silicone/paint/material mix and margin bridge produced strong MFE with minimal entry MAE. |
| R4L94_C17_LOTTECHEM_2024_PETROCHEM_SPREAD_FALSE_STAGE2 | 011170 | 롯데케미칼 | counterexample | Petrochemical spread watch had near-zero MFE and persistent MAE without utilization/margin bridge. |
| R4L94_C17_KOREAPETROLEUM_2024_OIL_PRODUCT_SPREAD_EVENT_CAP_4B | 004090 | 한국석유 | counterexample / 4B | Oil-product/asphalt event premium capped around the April spike and then de-rated. |

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
| KCC silicone/paint material margin bridge | historical public/report proxy | true | true | shadow-only positive |
| Lotte Chemical petrochem spread false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Korea Petroleum oil-product spread event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 002380 | atlas/ohlcv_tradable_by_symbol_year/002/002380/2024.csv | atlas/symbol_profiles/002/002380.json |
| 011170 | atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv | atlas/symbol_profiles/011/011170.json |
| 004090 | atlas/ohlcv_tradable_by_symbol_year/004/004090/2024.csv | atlas/symbol_profiles/004/004090.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R4L94_C17_KCC_2024_STAGE2_ACTIONABLE_SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE | 002380 | Stage2-Actionable | 2024-01-24 | 215500 | positive | silicone/paint material margin bridge worked |
| R4L94_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_PETROCHEM_SPREAD_WATCH | 011170 | Stage2-Actionable | 2024-02-01 | 140100 | counterexample | petrochemical spread false Stage2 |
| R4L94_C17_KOREAPETROLEUM_2024_STAGE4B_OIL_PRODUCT_SPREAD_EVENT_CAP | 004090 | Stage4B | 2024-04-09 | 15300 | counterexample/4B | oil-product spread event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R4L94_C17_KCC_2024_STAGE2_ACTIONABLE_SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE | 215500 | 35.96 | -0.23 | 51.97 | -0.23 | 60.09 | -0.23 | 2024-07-17 | 345000 | -18.84 |
| R4L94_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_PETROCHEM_SPREAD_WATCH | 140100 | 0.50 | -16.63 | 0.50 | -24.34 | 0.50 | -32.55 | 2024-02-01 | 140800 | -32.55 |
| R4L94_C17_KOREAPETROLEUM_2024_STAGE4B_OIL_PRODUCT_SPREAD_EVENT_CAP | 15300 | 7.45 | -12.81 | 7.45 | -28.30 | 7.45 | -32.10 | 2024-04-09 | 16440 | -34.10 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C17 Stage2 needs ASP pass-through / input-cost relief / utilization / mix / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing chemical/oil-product event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE chemical-spread rows cannot promote without durable margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is spread-to-margin bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 002380 | good_stage2_with_later_watch | Material mix and margin bridge produced strong MFE and minimal entry MAE. |
| 011170 | bad_stage2 | Petrochemical spread watch had almost no MFE and persistent drawdown. |
| 004090 | good_4B | Oil-product/asphalt premium capped around the April event spike and then de-rated. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 011170 petrochem false Stage2 | 1.00 | 1.00 | false Stage2 due missing utilization/margin bridge |
| 004090 oil-product cap | 0.93 | 0.93 | good full-window 4B timing after April event spike |
| 002380 material margin bridge | n/a | n/a | positive Stage2, but later material-margin valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 011170 / 004090
```

No hard 4C candidate is proposed. R4 loop 94 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L4 chemical/commodity margin-spread cases, Stage2 requires verified ASP pass-through, input-cost relief, product/customer mix, utilization, volume, margin or revision bridge. Chemical, petrochemical, oil-product, asphalt, naphtha, spread or commodity rebound label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
rule = C17 should split true spread-to-margin positives from petrochemical spread false Stage2 and oil-product event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 19.97 | -17.62 | 0.67 | mixed; C17 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 19.97 | -17.62 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L4 ASP/utilization/margin bridge required | 2 | 26.24 | -12.29 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C17 bridge vs event-cap split | 2 | 26.24 | -12.29 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing chemical spread themes as positive | 1 | 51.97 | -0.23 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 002380 material margin bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 51.97 | -0.23 | silicone_paint_material_margin_positive |
| 011170 petrochem false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 0.50 | -24.34 | petrochem_spread_false_stage2 |
| 004090 oil-product cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 7.45 | -28.30 | oil_product_spread_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE_VS_PETROCHEM_SPREAD_FALSE_STAGE2_AND_OIL_PRODUCT_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C17 KCC silicone/paint margin positive, Lotte Chemical petrochemical-spread false Stage2, and Korea Petroleum oil-product event-cap 4B split while avoiding top repeated C17 symbols."}
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
residual_error_types_found: silicone_paint_material_margin_positive, petrochem_spread_false_stage2, oil_product_spread_event_cap_4B
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
- C17 chemical commodity margin-spread bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,configured,C17_requires_ASP_pass_through_input_cost_product_mix_utilization_margin_revision_bridge,0,"C17 Stage2 should require ASP pass-through, input-cost relief, product/customer mix, utilization, margin, or revision bridge, not chemical/commodity spread label alone","KCC positive worked; Lotte Chemical and Korea Petroleum event/watch rows failed positive-stage promotion","R4L94_C17_KCC_2024_STAGE2_ACTIONABLE_SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE|R4L94_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_PETROCHEM_SPREAD_WATCH|R4L94_C17_KOREAPETROLEUM_2024_STAGE4B_OIL_PRODUCT_SPREAD_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,configured,cap_bridge_missing_chemical_and_oil_product_event_premiums_as_4B_watch,0,"Chemical/oil-product event premiums can peak before spread, inventory and margin bridge is proven","Lotte Chemical had near-zero forward MFE; Korea Petroleum showed 4B event-cap behavior after April oil-product spike","R4L94_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_PETROCHEM_SPREAD_WATCH|R4L94_C17_KOREAPETROLEUM_2024_STAGE4B_OIL_PRODUCT_SPREAD_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,configured,block_positive_stage_when_chemical_spread_theme_has_high_MAE_without_margin_bridge,0,"High or persistent MAE after bridge-missing chemical spread entries should block Stage2/Stage3 promotion unless spread, volume, utilization and margin evidence survives","Lotte Chemical MAE180=-32.55 and Korea Petroleum MAE90=-28.30","R4L94_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_PETROCHEM_SPREAD_WATCH|R4L94_C17_KOREAPETROLEUM_2024_STAGE4B_OIL_PRODUCT_SPREAD_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L94_C17_KCC_2024_SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE_POSITIVE", "symbol": "002380", "company_name": "KCC", "round": "R4", "loop": "94", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE_VS_PETROCHEM_SPREAD_FALSE_STAGE2_AND_OIL_PRODUCT_EVENT_CAP", "case_type": "structural_success_with_later_material_margin_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R4L94_C17_KCC_2024_STAGE2_ACTIONABLE_SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Silicone/paint/material mix and margin bridge produced strong 30D/90D/180D MFE with almost no entry MAE. C17 works when commodity spread narrative maps into ASP pass-through, input-cost relief, product mix, customer demand, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C17_positive_requires_ASP_product_mix_input_cost_margin_revision_bridge_not_chemical_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R4L94_C17_LOTTECHEM_2024_PETROCHEM_SPREAD_FALSE_STAGE2", "symbol": "011170", "company_name": "롯데케미칼", "round": "R4", "loop": "94", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE_VS_PETROCHEM_SPREAD_FALSE_STAGE2_AND_OIL_PRODUCT_EVENT_CAP", "case_type": "failed_rerating_petrochem_spread_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R4L94_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_PETROCHEM_SPREAD_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Petrochemical spread recovery watch had near-zero forward MFE and then persistent MAE. C17 Stage2 should not be awarded without naphtha/product spread durability, utilization recovery, inventory drawdown, customer demand, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_petrochem_spread_watch_counts_without_utilization_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean with no relevant 2024 corporate-action contamination. Source-proxy only."}
{"row_type": "case", "case_id": "R4L94_C17_KOREAPETROLEUM_2024_OIL_PRODUCT_SPREAD_EVENT_CAP_4B", "symbol": "004090", "company_name": "한국석유", "round": "R4", "loop": "94", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE_VS_PETROCHEM_SPREAD_FALSE_STAGE2_AND_OIL_PRODUCT_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L94_C17_KOREAPETROLEUM_2024_STAGE4B_OIL_PRODUCT_SPREAD_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Oil-product / asphalt / resource spread event premium capped around the April spike and then de-rated. C17 should route bridge-missing chemical/oil-product event premiums to 4B unless inventory spread, ASP pass-through, volume, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_oil_product_spread_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2021 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L94_C17_KCC_2024_STAGE2_ACTIONABLE_SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE", "case_id": "R4L94_C17_KCC_2024_SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE_POSITIVE", "symbol": "002380", "company_name": "KCC", "round": "R4", "loop": "94", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE_VS_PETROCHEM_SPREAD_FALSE_STAGE2_AND_OIL_PRODUCT_EVENT_CAP", "sector": "silicone_paint_material_product_mix_margin", "primary_archetype": "ASP_product_mix_input_cost_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 215500.0, "evidence_available_at_that_date": "silicone/paint/material product-mix improvement, input-cost relief, ASP pass-through and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["ASP_pass_through_proxy", "input_cost_relief_proxy", "product_mix_bridge", "customer_demand_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "strong_MFE180", "shallow_MAE90"], "stage4b_evidence_fields": ["later_material_margin_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002380/2024.csv", "profile_path": "atlas/symbol_profiles/002/002380.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 35.96, "MFE_90D_pct": 51.97, "MFE_180D_pct": 60.09, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -0.23, "MAE_90D_pct": -0.23, "MAE_180D_pct": -0.23, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-17", "peak_price": 345000.0, "drawdown_after_peak_pct": -18.84, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_material_margin_valuation_4B_watch_needed", "four_b_evidence_type": ["material_margin_bridge", "product_mix_repricing", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_silicone_paint_material_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA_candidates", "same_entry_group_id": "R4L94_C17_002380_2024-01-24_215500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L94_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_PETROCHEM_SPREAD_WATCH", "case_id": "R4L94_C17_LOTTECHEM_2024_PETROCHEM_SPREAD_FALSE_STAGE2", "symbol": "011170", "company_name": "롯데케미칼", "round": "R4", "loop": "94", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE_VS_PETROCHEM_SPREAD_FALSE_STAGE2_AND_OIL_PRODUCT_EVENT_CAP", "sector": "petrochemical_spread_recovery_watch", "primary_archetype": "petrochem_spread_watch_without_utilization_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 140100.0, "evidence_available_at_that_date": "petrochemical spread recovery watch, naphtha cost relief expectation and commodity-cycle rebound proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["petrochem_spread_recovery_watch", "naphtha_cost_relief_expectation", "commodity_cycle_rebound", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["near_zero_MFE90", "utilization_margin_revision_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv", "profile_path": "atlas/symbol_profiles/011/011170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.5, "MFE_90D_pct": 0.5, "MFE_180D_pct": 0.5, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -16.63, "MAE_90D_pct": -24.34, "MAE_180D_pct": -32.55, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-01", "peak_price": 140800.0, "drawdown_after_peak_pct": -32.55, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "petrochem_spread_watch_was_false_stage2_due_missing_utilization_margin_revision_bridge", "four_b_evidence_type": ["petrochem_spread_watch_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_petrochem_spread_watch_without_utilization_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_petrochem_spread_watch_counts_without_utilization_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_2024_CA_contamination", "same_entry_group_id": "R4L94_C17_011170_2024-02-01_140100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L94_C17_KOREAPETROLEUM_2024_STAGE4B_OIL_PRODUCT_SPREAD_EVENT_CAP", "case_id": "R4L94_C17_KOREAPETROLEUM_2024_OIL_PRODUCT_SPREAD_EVENT_CAP_4B", "symbol": "004090", "company_name": "한국석유", "round": "R4", "loop": "94", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE_VS_PETROCHEM_SPREAD_FALSE_STAGE2_AND_OIL_PRODUCT_EVENT_CAP", "sector": "oil_product_asphalt_spread_event_premium", "primary_archetype": "oil_product_spread_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-09", "entry_date": "2024-04-09", "entry_price": 15300.0, "evidence_available_at_that_date": "oil-product/asphalt spread event premium and resource-price spike after April event; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["oil_product_spread_event", "asphalt_inventory_margin_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "post_event_drawdown", "inventory_spread_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004090/2024.csv", "profile_path": "atlas/symbol_profiles/004/004090.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.45, "MFE_90D_pct": 7.45, "MFE_180D_pct": 7.45, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -12.81, "MAE_90D_pct": -28.3, "MAE_180D_pct": -32.1, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-09", "peak_price": 16440.0, "drawdown_after_peak_pct": -34.1, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "good_full_window_4B_timing_oil_product_spread_event_cap", "four_b_evidence_type": ["oil_product_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_oil_product_spread_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_oil_product_spread_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2021_CA", "same_entry_group_id": "R4L94_C17_004090_2024-04-09_15300", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L94_C17_KCC_2024_SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R4L94_C17_KCC_2024_STAGE2_ACTIONABLE_SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE", "symbol": "002380", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 45, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "silicone_paint_material_margin_positive", "MFE_90D_pct": 51.97, "MAE_90D_pct": -0.23, "score_return_alignment_label": "silicone_paint_material_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L94_C17_LOTTECHEM_2024_PETROCHEM_SPREAD_FALSE_STAGE2", "trigger_id": "R4L94_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_PETROCHEM_SPREAD_WATCH", "symbol": "011170", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "petrochem_spread_false_stage2", "MFE_90D_pct": 0.5, "MAE_90D_pct": -24.34, "score_return_alignment_label": "petrochem_spread_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_petrochem_spread_watch_counts_without_utilization_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L94_C17_KOREAPETROLEUM_2024_OIL_PRODUCT_SPREAD_EVENT_CAP_4B", "trigger_id": "R4L94_C17_KOREAPETROLEUM_2024_STAGE4B_OIL_PRODUCT_SPREAD_EVENT_CAP", "symbol": "004090", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "oil_product_spread_event_cap_4B_guard", "MFE_90D_pct": 7.45, "MAE_90D_pct": -28.3, "score_return_alignment_label": "oil_product_spread_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_oil_product_spread_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "94", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SILICONE_PAINT_MATERIAL_MARGIN_BRIDGE_VS_PETROCHEM_SPREAD_FALSE_STAGE2_AND_OIL_PRODUCT_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["silicone_paint_material_margin_positive", "petrochem_spread_false_stage2", "oil_product_spread_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C17 rows need explicit ASP pass-through, input-cost relief, utilization, product mix, volume, margin or revision bridge before positive promotion.
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
10. Add tests that bridge-missing C17 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R4
completed_loop = 94
next_round = R5
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
