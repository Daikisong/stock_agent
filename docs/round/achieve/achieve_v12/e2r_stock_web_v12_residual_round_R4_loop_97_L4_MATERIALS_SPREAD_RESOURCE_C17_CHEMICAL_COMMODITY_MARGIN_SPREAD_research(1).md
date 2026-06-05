# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE_VS_POLYSILICON_SPREAD_FALSE_STAGE2_AND_INDUSTRIAL_GAS_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | commodity_spread_bridge_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R4_loop_97_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
```

This file is the corrected final output for this execution. The scheduler state after R3 loop 97 is R4 / loop 97. R4 is the L4 materials/spread/resource round, and this run fills C17 chemical commodity margin spread rather than repeating the immediately preceding R4 loop 96 C15 material-spread file, R4 loop 95 C16 strategic-resource file, or R3 loop 97 C12 battery-calloff file.

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
commodity_spread_bridge_guard = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R4
scheduled_loop = 97
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
round_sector_consistency = pass
computed_next_round = R5
computed_next_loop = 97
```

C17 is a realized chemical-spread-to-margin archetype. A commodity spread label is only the price board; the signal becomes usable when inventory discipline, cost curve, pass-through, capacity/customer quality, margin and revision show up together.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD = 21 rows / 15 symbols / good-bad Stage2 8-3 / 4B-4C 4-0
top covered symbols include 004000(3), 006650(2), 011780(2), 014680(2), 298020(2), 001390(1)
previous R4 loop-94 C17 symbols avoided: 002380, 011170, 004090
previous R4 loop-95 C16 symbols avoided: 103140, 075970, 011810
previous R4 loop-96 C15 symbols avoided: 058430, 032560, 008350
previous R3 loop-97 C12 symbols avoided: 011790, 243840, 419050
previous R2 loop-97 C06 symbols avoided: 031980, 036540, 080220
```

Selected rows avoid hard duplicates and top repeated C17 symbols:

```text
001340 / Stage2-Actionable / 2024-05-22
010060 / Stage2-Actionable / 2024-02-06
006890 / Stage4B / 2024-05-24
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
| 001340 | atlas/symbol_profiles/001/001340.json | selected 2024/2025 window clean after old 2008/2012/2015 CA candidates |
| 010060 | atlas/symbol_profiles/010/010060.json | selected 2024 window clean after old CA and after 2023 name-continuity zone |
| 006890 | atlas/symbol_profiles/006/006890.json | selected 2024 window clean after old CA and market-history candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R4L97_C17_PKC_2024_CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE_POSITIVE | 001340 | 2024-05-22 | yes | 180 | yes | yes | true |
| R4L97_C17_OCIHOLDINGS_2024_POLYSILICON_SPREAD_FALSE_STAGE2 | 010060 | 2024-02-06 | yes | 180 | yes | yes | true |
| R4L97_C17_TAEKYUNGCHEM_2024_INDUSTRIAL_GAS_DRYICE_EVENT_CAP_4B | 006890 | 2024-05-24 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE | Positive Stage2 requires realized spread, capacity/customer bridge, inventory discipline, margin and revision bridge. |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | POLYSILICON_SPREAD_FALSE_STAGE2 | Polysilicon/solar chemical spread watch without realized spread and cost-curve bridge can become false Stage2. |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | INDUSTRIAL_GAS_DRYICE_EVENT_CAP_4B | Industrial-gas/dry-ice event premium should route to 4B when volume/contract/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R4L97_C17_PKC_2024_CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE_POSITIVE | 001340 | 백광산업 | positive | Reopening-window chemical spread/margin bridge produced very strong MFE, while later drawdown requires valuation watch. |
| R4L97_C17_OCIHOLDINGS_2024_POLYSILICON_SPREAD_FALSE_STAGE2 | 010060 | OCI홀딩스 | counterexample | Polysilicon/solar chemical spread watch had tiny MFE and then persistent MAE. |
| R4L97_C17_TAEKYUNGCHEM_2024_INDUSTRIAL_GAS_DRYICE_EVENT_CAP_4B | 006890 | 태경케미컬 | counterexample / 4B | Industrial-gas/dry-ice spread event premium capped modestly and then de-rated. |

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
| PKC/Baekkwang chlor-alkali / semiconductor chemical spread bridge | historical public/news-report proxy | true | true | shadow-only positive |
| OCI Holdings polysilicon spread false Stage2 | historical public/news-report proxy | true | true | false-Stage2 guardrail |
| Taekyung Chemical industrial-gas/dry-ice spread cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 001340 | atlas/ohlcv_tradable_by_symbol_year/001/001340/2024.csv and 2025.csv | atlas/symbol_profiles/001/001340.json |
| 010060 | atlas/ohlcv_tradable_by_symbol_year/010/010060/2024.csv | atlas/symbol_profiles/010/010060.json |
| 006890 | atlas/ohlcv_tradable_by_symbol_year/006/006890/2024.csv | atlas/symbol_profiles/006/006890.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R4L97_C17_PKC_2024_STAGE2_ACTIONABLE_CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE | 001340 | Stage2-Actionable | 2024-05-22 | 7970 | positive | realized chemical spread / semicon-chemical margin bridge worked |
| R4L97_C17_OCIHOLDINGS_2024_STAGE2_FALSE_POSITIVE_POLYSILICON_SPREAD_WATCH | 010060 | Stage2-Actionable | 2024-02-06 | 110200 | counterexample | polysilicon spread false Stage2 |
| R4L97_C17_TAEKYUNGCHEM_2024_STAGE4B_INDUSTRIAL_GAS_DRYICE_SPREAD_EVENT_CAP | 006890 | Stage4B | 2024-05-24 | 14330 | counterexample/4B | industrial-gas/dry-ice spread event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R4L97_C17_PKC_2024_STAGE2_ACTIONABLE_CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE | 7970 | 131.37 | -10.04 | 131.37 | -10.04 | 131.37 | -17.82 | 2024-06-12 | 18440 | -64.48 |
| R4L97_C17_OCIHOLDINGS_2024_STAGE2_FALSE_POSITIVE_POLYSILICON_SPREAD_WATCH | 110200 | 2.54 | -16.42 | 2.54 | -21.87 | 2.54 | -41.74 | 2024-02-07 | 113000 | -43.19 |
| R4L97_C17_TAEKYUNGCHEM_2024_STAGE4B_INDUSTRIAL_GAS_DRYICE_SPREAD_EVENT_CAP | 14330 | 8.09 | -3.70 | 8.09 | -33.08 | 8.09 | -33.08 | 2024-06-11 | 15490 | -38.09 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C17 Stage2 needs realized spread / inventory / capacity-customer / pass-through / margin / revision bridge |
| commodity_spread_bridge_guard | strengthen: spread labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing chemical commodity event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE chemical spread rows cannot promote without durable realized margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether chemical/commodity-spread narrative becomes realized spread and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 001340 | good_stage2_with_later_watch | Realized chemical spread and semicon-chemical customer bridge produced very strong MFE but later post-peak drawdown demands 4B valuation watch. |
| 010060 | bad_stage2 | Polysilicon spread watch lacked realized spread, inventory and margin bridge; price path had tiny MFE and deep MAE. |
| 006890 | good_4B | Industrial-gas spread event premium made only a modest local high and then de-rated. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 010060 polysilicon false Stage2 | 0.98 | 0.98 | false Stage2 due missing realized spread / inventory / cost curve / margin bridge |
| 006890 industrial-gas cap | 0.93 | 0.93 | acceptable 4B timing because volume/contract/margin bridge was missing |
| 001340 chlor-alkali bridge | n/a | n/a | positive Stage2, but later spread-normalization and valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 010060 / 006890
```

No hard 4C candidate is introduced in this R4 loop 97 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L4 chemical commodity margin-spread cases, Stage2 requires verified realized product spread, inventory discipline, capacity/customer bridge, cost curve or pass-through, margin, or revision bridge. Chemical, polysilicon, industrial gas, dry ice, commodity spread, reopening or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
rule = C17 should split true realized-spread/customer/margin positives from polysilicon false Stage2 and industrial-gas event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 47.33 | -21.66 | 0.67 | mixed; C17 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 47.33 | -21.66 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L4 realized-spread/margin bridge required | 2 | 66.95 | -15.96 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C17 bridge vs event-cap split | 2 | 66.95 | -15.96 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing chemical-spread themes as positive | 1 | 131.37 | -10.04 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 001340 chemical spread bridge | 66 | Stage2-Watch | 79 | Stage2-Actionable | 131.37 | -10.04 | chloralkali_semicon_chemical_margin_positive |
| 010060 polysilicon false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 2.54 | -21.87 | polysilicon_spread_false_stage2 |
| 006890 industrial-gas cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 8.09 | -33.08 | industrial_gas_dryice_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE_VS_POLYSILICON_SPREAD_FALSE_STAGE2_AND_INDUSTRIAL_GAS_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C17 PKC/Baekkwang chlor-alkali chemical margin positive, OCI Holdings polysilicon spread false Stage2, and Taekyung Chemical industrial-gas spread event-cap 4B while avoiding top repeated C17 and previous R4/R3 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, commodity_spread_bridge_guard, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: chloralkali_semicon_chemical_margin_positive, polysilicon_spread_false_stage2, industrial_gas_dryice_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, commodity_spread_bridge_guard, high_MAE_guardrail
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
- C17 chemical commodity margin spread bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,configured,C17_requires_realized_spread_inventory_capacity_customer_margin_revision_bridge,0,"C17 Stage2 should require realized product spread, inventory discipline, capacity/customer bridge, cost curve/pass-through, margin, or revision bridge, not chemical/commodity/spread label alone","PKC/Baekkwang positive worked; OCI Holdings and Taekyung Chemical event/watch rows failed positive-stage promotion","R4L97_C17_PKC_2024_STAGE2_ACTIONABLE_CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE|R4L97_C17_OCIHOLDINGS_2024_STAGE2_FALSE_POSITIVE_POLYSILICON_SPREAD_WATCH|R4L97_C17_TAEKYUNGCHEM_2024_STAGE4B_INDUSTRIAL_GAS_DRYICE_SPREAD_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,configured,cap_bridge_missing_polysilicon_and_industrial_gas_event_premiums_as_4B_watch,0,"Chemical spread and industrial-gas event premiums can peak before realized spread, volume, inventory and margin bridge is proven","OCI Holdings had low MFE and persistent MAE; Taekyung Chemical showed event-cap behavior after the May/June industrial-gas spike","R4L97_C17_OCIHOLDINGS_2024_STAGE2_FALSE_POSITIVE_POLYSILICON_SPREAD_WATCH|R4L97_C17_TAEKYUNGCHEM_2024_STAGE4B_INDUSTRIAL_GAS_DRYICE_SPREAD_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,configured,block_positive_stage_when_chemical_spread_theme_has_high_or_persistent_MAE_without_margin_bridge,0,"High or persistent MAE after bridge-missing C17 entries should block Stage2/Stage3 promotion unless realized spread, inventory and margin evidence survives","OCI Holdings MAE180=-41.74 and Taekyung Chemical MAE90=-33.08","R4L97_C17_OCIHOLDINGS_2024_STAGE2_FALSE_POSITIVE_POLYSILICON_SPREAD_WATCH|R4L97_C17_TAEKYUNGCHEM_2024_STAGE4B_INDUSTRIAL_GAS_DRYICE_SPREAD_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L97_C17_PKC_2024_CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE_POSITIVE", "symbol": "001340", "company_name": "백광산업", "round": "R4", "loop": "97", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE_VS_POLYSILICON_SPREAD_FALSE_STAGE2_AND_INDUSTRIAL_GAS_EVENT_CAP", "case_type": "structural_success_with_later_chemical_spread_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R4L97_C17_PKC_2024_STAGE2_ACTIONABLE_CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Chlor-alkali / semiconductor-grade chemical spread and capacity/margin bridge produced very strong MFE after the May reopening window, but later post-peak drawdown means C17 positives still need valuation and spread-normalization watch.", "current_profile_verdict": "current_profile_kept_but_C17_positive_requires_realized_spread_capacity_customer_margin_revision_bridge_not_chemical_theme_only", "price_source": "Songdaiki/stock-web", "notes": "2024 tradable window starts on 2024-04-22. Profile shows old 2008/2012/2015 CA candidates only. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R4L97_C17_OCIHOLDINGS_2024_POLYSILICON_SPREAD_FALSE_STAGE2", "symbol": "010060", "company_name": "OCI홀딩스", "round": "R4", "loop": "97", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE_VS_POLYSILICON_SPREAD_FALSE_STAGE2_AND_INDUSTRIAL_GAS_EVENT_CAP", "case_type": "failed_rerating_polysilicon_solar_chemical_spread_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R4L97_C17_OCIHOLDINGS_2024_STAGE2_FALSE_POSITIVE_POLYSILICON_SPREAD_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Polysilicon / solar chemical spread watch had a brief February premium but then sold off into persistent MAE as realized spread, inventory, customer demand, cost curve and revision bridge were not confirmed.", "current_profile_verdict": "current_profile_false_positive_if_polysilicon_spread_watch_counts_without_realized_spread_inventory_cost_curve_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old CA candidates and after 2023 name-continuity change. Source-proxy only."}
{"row_type": "case", "case_id": "R4L97_C17_TAEKYUNGCHEM_2024_INDUSTRIAL_GAS_DRYICE_EVENT_CAP_4B", "symbol": "006890", "company_name": "태경케미컬", "round": "R4", "loop": "97", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE_VS_POLYSILICON_SPREAD_FALSE_STAGE2_AND_INDUSTRIAL_GAS_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L97_C17_TAEKYUNGCHEM_2024_STAGE4B_INDUSTRIAL_GAS_DRYICE_SPREAD_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Industrial gas / dry-ice spread event premium made a modest local high and then de-rated as no durable realized spread, volume, contract or margin-revision bridge was proven.", "current_profile_verdict": "current_profile_4B_too_late_if_industrial_gas_spread_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1996/1998/2002/2003 corporate-action and market-history candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L97_C17_PKC_2024_STAGE2_ACTIONABLE_CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE", "case_id": "R4L97_C17_PKC_2024_CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE_POSITIVE", "symbol": "001340", "company_name": "백광산업", "round": "R4", "loop": "97", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE_VS_POLYSILICON_SPREAD_FALSE_STAGE2_AND_INDUSTRIAL_GAS_EVENT_CAP", "sector": "chloralkali_semiconductor_chemical_spread_capacity_margin", "primary_archetype": "realized_spread_capacity_customer_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | commodity_spread_bridge_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-22", "entry_date": "2024-05-22", "entry_price": 7970.0, "evidence_available_at_that_date": "chlor-alkali / semiconductor chemical spread and customer/capacity margin bridge proxy after 2024 reopening window; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_report_proxy", "stage2_evidence_fields": ["realized_spread_proxy", "capacity_reopening_proxy", "semicon_chemical_customer_proxy", "inventory_discipline_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["very_strong_MFE30", "very_strong_MFE90", "positive_MFE180"], "stage4b_evidence_fields": ["later_chemical_spread_valuation_watch", "spread_normalization_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001340/2024.csv; atlas/ohlcv_tradable_by_symbol_year/001/001340/2025.csv", "profile_path": "atlas/symbol_profiles/001/001340.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 131.37, "MFE_90D_pct": 131.37, "MFE_180D_pct": 131.37, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -10.04, "MAE_90D_pct": -10.04, "MAE_180D_pct": -17.82, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-12", "peak_price": 18440.0, "drawdown_after_peak_pct": -64.48, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_chemical_spread_valuation_4B_watch_needed", "four_b_evidence_type": ["chemical_spread_bridge", "semicon_chemical_customer", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_chloralkali_semicon_chemical_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2008_2012_2015_CA", "same_entry_group_id": "R4L97_C17_001340_2024-05-22_7970", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L97_C17_OCIHOLDINGS_2024_STAGE2_FALSE_POSITIVE_POLYSILICON_SPREAD_WATCH", "case_id": "R4L97_C17_OCIHOLDINGS_2024_POLYSILICON_SPREAD_FALSE_STAGE2", "symbol": "010060", "company_name": "OCI홀딩스", "round": "R4", "loop": "97", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE_VS_POLYSILICON_SPREAD_FALSE_STAGE2_AND_INDUSTRIAL_GAS_EVENT_CAP", "sector": "polysilicon_solar_chemical_spread_inventory_cost_curve_watch", "primary_archetype": "polysilicon_spread_watch_without_realized_spread_inventory_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | commodity_spread_bridge_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-06", "entry_date": "2024-02-06", "entry_price": 110200.0, "evidence_available_at_that_date": "polysilicon / solar chemical spread watch without confirmed realized spread, inventory discipline, cost curve, demand or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_report_proxy", "stage2_evidence_fields": ["polysilicon_spread_watch", "solar_chemical_cycle_sympathy", "relative_strength_rebound"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "persistent_MAE90", "spread_inventory_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010060/2024.csv", "profile_path": "atlas/symbol_profiles/010/010060.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.54, "MFE_90D_pct": 2.54, "MFE_180D_pct": 2.54, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -16.42, "MAE_90D_pct": -21.87, "MAE_180D_pct": -41.74, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-07", "peak_price": 113000.0, "drawdown_after_peak_pct": -43.19, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "polysilicon_spread_watch_was_false_stage2_due_missing_realized_spread_inventory_margin_revision_bridge", "four_b_evidence_type": ["polysilicon_spread_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_polysilicon_spread_watch_without_inventory_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_polysilicon_spread_watch_counts_without_realized_spread_inventory_cost_curve_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA_and_after_2023_name_continuity_zone", "same_entry_group_id": "R4L97_C17_010060_2024-02-06_110200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L97_C17_TAEKYUNGCHEM_2024_STAGE4B_INDUSTRIAL_GAS_DRYICE_SPREAD_EVENT_CAP", "case_id": "R4L97_C17_TAEKYUNGCHEM_2024_INDUSTRIAL_GAS_DRYICE_EVENT_CAP_4B", "symbol": "006890", "company_name": "태경케미컬", "round": "R4", "loop": "97", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE_VS_POLYSILICON_SPREAD_FALSE_STAGE2_AND_INDUSTRIAL_GAS_EVENT_CAP", "sector": "industrial_gas_dryice_commodity_spread_event_premium", "primary_archetype": "industrial_gas_dryice_spread_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | commodity_spread_bridge_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-05-24", "entry_date": "2024-05-24", "entry_price": 14330.0, "evidence_available_at_that_date": "industrial gas / dry-ice commodity spread event premium without confirmed realized spread, contract volume, customer pass-through or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["industrial_gas_event", "dryice_spread_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "persistent_MAE90", "volume_contract_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006890/2024.csv", "profile_path": "atlas/symbol_profiles/006/006890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.09, "MFE_90D_pct": 8.09, "MFE_180D_pct": 8.09, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.7, "MAE_90D_pct": -33.08, "MAE_180D_pct": -33.08, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-11", "peak_price": 15490.0, "drawdown_after_peak_pct": -38.09, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "acceptable_4B_timing_industrial_gas_dryice_spread_event_cap_due_missing_volume_contract_margin_bridge", "four_b_evidence_type": ["industrial_gas_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_industrial_gas_dryice_spread_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_industrial_gas_spread_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA_and_market_history_candidates", "same_entry_group_id": "R4L97_C17_006890_2024-05-24_14330", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L97_C17_PKC_2024_CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R4L97_C17_PKC_2024_STAGE2_ACTIONABLE_CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE", "symbol": "001340", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 30, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 15, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 30, "backlog_visibility_score": 55, "margin_bridge_score": 65, "revision_score": 60, "relative_strength_score": 80, "customer_quality_score": 55, "policy_or_regulatory_score": 15, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "chloralkali_semicon_chemical_margin_positive", "MFE_90D_pct": 131.37, "MAE_90D_pct": -10.04, "score_return_alignment_label": "chloralkali_semicon_chemical_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L97_C17_OCIHOLDINGS_2024_POLYSILICON_SPREAD_FALSE_STAGE2", "trigger_id": "R4L97_C17_OCIHOLDINGS_2024_STAGE2_FALSE_POSITIVE_POLYSILICON_SPREAD_WATCH", "symbol": "010060", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 30, "policy_or_regulatory_score": 15, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "polysilicon_spread_false_stage2", "MFE_90D_pct": 2.54, "MAE_90D_pct": -21.87, "score_return_alignment_label": "polysilicon_spread_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_polysilicon_spread_watch_counts_without_realized_spread_inventory_cost_curve_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L97_C17_TAEKYUNGCHEM_2024_INDUSTRIAL_GAS_DRYICE_EVENT_CAP_4B", "trigger_id": "R4L97_C17_TAEKYUNGCHEM_2024_STAGE4B_INDUSTRIAL_GAS_DRYICE_SPREAD_EVENT_CAP", "symbol": "006890", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "industrial_gas_dryice_event_cap_4B_guard", "MFE_90D_pct": 8.09, "MAE_90D_pct": -33.08, "score_return_alignment_label": "industrial_gas_dryice_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_industrial_gas_spread_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "97", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE_VS_POLYSILICON_SPREAD_FALSE_STAGE2_AND_INDUSTRIAL_GAS_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "commodity_spread_bridge_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["chloralkali_semicon_chemical_margin_positive", "polysilicon_spread_false_stage2", "industrial_gas_dryice_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C17 rows need explicit realized product spread, inventory discipline, capacity/customer bridge, cost curve/pass-through, margin or revision bridge before positive promotion.
- In C17, bridge-missing chemical-spread event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C17 chemical commodity spread rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R4
completed_loop = 97
next_round = R5
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
