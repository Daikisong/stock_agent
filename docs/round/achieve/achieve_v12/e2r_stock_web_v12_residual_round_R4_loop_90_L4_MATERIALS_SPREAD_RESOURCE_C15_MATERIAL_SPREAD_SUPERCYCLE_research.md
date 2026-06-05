# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = COPPER_NONFERROUS_SPREAD_MARGIN_BRIDGE_VS_ALUMINUM_THEME_AND_FOIL_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R4_loop_90_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
```

This loop continues loop 90 after R3. It adds 3 C15 material spread/supercycle cases: one copper/non-ferrous spread positive, one aluminum theme false Stage2, and one aluminum-foil 4B event-cap counterexample.

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
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R4
scheduled_loop = 90
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
round_sector_consistency = pass
computed_next_round = R5
computed_next_loop = 90
```

R4 permits L4 materials/spread/resource research. Previous R4 loop 88 used C17 and R4 loop 89 used C16, so this loop fills C15 and tests whether material supercycle price moves are supported by spread, repricing, inventory, volume, margin, or revision conversion.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C15_MATERIAL_SPREAD_SUPERCYCLE = 28 rows / 11 symbols / good-bad Stage2 13-0 / 4B-4C 3-0
top covered symbols include 103140(6), 012800(5), 025820(5), 004560(3), 021050(3), 001780(1)
previous R4 loop-88 C17 symbols avoided: 120110, 069260, 161000
previous R4 loop-89 C16 symbols avoided: 009520, 011810, 037370
```

Selected rows avoid those repeated combinations:

```text
024840 / Stage2-Actionable / 2024-04-05
018470 / Stage2-Actionable / 2024-04-18
006110 / Stage4B / 2024-06-11
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
| 024840 | atlas/symbol_profiles/024/024840.json | selected 2024 window clean; old CA candidates only |
| 018470 | atlas/symbol_profiles/018/018470.json | selected 2024 window clean; CA candidates are 2012 or earlier |
| 006110 | atlas/symbol_profiles/006/006110.json | selected 2024 window clean after 2023-02-09 CA |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R4L90_C15_KBIMETAL_2024_COPPER_SPREAD_MARGIN_BRIDGE_POSITIVE | 024840 | 2024-04-05 | yes | 180 | yes | yes | true |
| R4L90_C15_CHOILALUMINUM_2024_ALUMINUM_THEME_FALSE_STAGE2 | 018470 | 2024-04-18 | yes | 180 | yes | yes | true |
| R4L90_C15_SAMAALUMINUM_2024_ALUMINUM_FOIL_EVENT_CAP_4B | 006110 | 2024-06-11 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C15_MATERIAL_SPREAD_SUPERCYCLE | COPPER_NONFERROUS_SPREAD_MARGIN_BRIDGE | Positive Stage2 requires spread, repricing, inventory, volume, margin, or revision bridge. |
| C15_MATERIAL_SPREAD_SUPERCYCLE | ALUMINUM_THEME_FALSE_STAGE2 | Aluminum/non-ferrous theme without spread-margin bridge can become false Stage2. |
| C15_MATERIAL_SPREAD_SUPERCYCLE | ALUMINUM_FOIL_EVENT_CAP_4B | Aluminum foil / battery-material premium should route to 4B when event premium is capped. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R4L90_C15_KBIMETAL_2024_COPPER_SPREAD_MARGIN_BRIDGE_POSITIVE | 024840 | KBI메탈 | positive | Copper/non-ferrous spread bridge produced very high MFE with shallow early MAE. |
| R4L90_C15_CHOILALUMINUM_2024_ALUMINUM_THEME_FALSE_STAGE2 | 018470 | 조일알미늄 | counterexample | Aluminum theme premium had limited MFE and no durable margin bridge. |
| R4L90_C15_SAMAALUMINUM_2024_ALUMINUM_FOIL_EVENT_CAP_4B | 006110 | 삼아알미늄 | counterexample / 4B | Aluminum foil premium capped at June peak and then de-rated deeply. |

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
| KBI Metal copper/non-ferrous bridge | historical public/news proxy | true | true | shadow-only positive |
| Choil Aluminum aluminum false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Sama Aluminum aluminum foil cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 024840 | atlas/ohlcv_tradable_by_symbol_year/024/024840/2024.csv | atlas/symbol_profiles/024/024840.json |
| 018470 | atlas/ohlcv_tradable_by_symbol_year/018/018470/2024.csv | atlas/symbol_profiles/018/018470.json |
| 006110 | atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv | atlas/symbol_profiles/006/006110.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R4L90_C15_KBIMETAL_2024_STAGE2_ACTIONABLE_COPPER_SPREAD_MARGIN_BRIDGE | 024840 | Stage2-Actionable | 2024-04-05 | 1535 | positive | copper/non-ferrous spread margin bridge worked |
| R4L90_C15_CHOILALUMINUM_2024_STAGE2_FALSE_POSITIVE_ALUMINUM_THEME | 018470 | Stage2-Actionable | 2024-04-18 | 2510 | counterexample | aluminum theme false Stage2 |
| R4L90_C15_SAMAALUMINUM_2024_STAGE4B_ALUMINUM_FOIL_EVENT_CAP | 006110 | Stage4B | 2024-06-11 | 96300 | counterexample/4B | aluminum foil event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R4L90_C15_KBIMETAL_2024_STAGE2_ACTIONABLE_COPPER_SPREAD_MARGIN_BRIDGE | 1535 | 209.12 | -3.00 | 209.12 | -3.00 | 209.12 | -3.00 | 2024-05-21 | 4745 | -54.16 |
| R4L90_C15_CHOILALUMINUM_2024_STAGE2_FALSE_POSITIVE_ALUMINUM_THEME | 2510 | 9.96 | -13.35 | 9.96 | -20.32 | 9.96 | -20.32 | 2024-04-18 | 2760 | -27.54 |
| R4L90_C15_SAMAALUMINUM_2024_STAGE4B_ALUMINUM_FOIL_EVENT_CAP | 96300 | 0.62 | -23.57 | 0.62 | -58.88 | 0.62 | -58.88 | 2024-06-11 | 96900 | -59.13 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C15 Stage2 needs spread/margin/inventory/repricing bridge |
| local_4b_watch_guard | strengthen: aluminum/foil theme premiums should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is material-spread bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 024840 | good_stage2 | Copper/non-ferrous spread bridge produced explosive MFE. |
| 018470 | bad_stage2 | Aluminum theme lacked durable margin/repricing bridge. |
| 006110 | good_4B | Aluminum foil premium capped around the June spike. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 018470 aluminum false Stage2 | 1.00 | 1.00 | aluminum theme spike was false Stage2 event cap |
| 006110 aluminum foil cap | 1.00 | 1.00 | good full-window 4B timing |
| 024840 copper spread bridge | n/a | n/a | positive Stage2, but later commodity-spread valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 018470 / 006110
```

No hard 4C candidate is proposed. R4 loop 90 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L4 material-spread cases, Stage2 requires verified spread, inventory/repricing, volume, cost pass-through, margin, or revision bridge. Copper/aluminum/material-supercycle label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
rule = C15 should split real spread/margin positives from material-theme false Stage2 and aluminum/foil event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 73.23 | -27.40 | 0.67 | mixed; C15 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 73.23 | -27.40 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L4 spread/margin bridge required | 2 | 109.54 | -11.66 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C15 bridge vs event-cap split | 2 | 109.54 | -11.66 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing material themes as positive | 1 | 209.12 | -3.00 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 024840 copper spread bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 209.12 | -3.00 | copper_spread_margin_bridge_positive |
| 018470 aluminum false Stage2 | 66 | Stage2-Actionable | 53 | Stage1/Watch | 9.96 | -20.32 | aluminum_theme_false_stage2 |
| 006110 aluminum foil cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 0.62 | -58.88 | aluminum_foil_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_SPREAD_MARGIN_BRIDGE_VS_ALUMINUM_THEME_AND_FOIL_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C15 copper/non-ferrous spread positive, aluminum theme false Stage2, and aluminum-foil material event-cap 4B split using non-top-covered symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: copper_spread_margin_bridge_positive, aluminum_theme_false_stage2, aluminum_foil_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard
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
- C15 material spread/supercycle bridge vs material-theme event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,configured,C15_requires_spread_margin_inventory_or_pricing_bridge,0,"C15 Stage2 should require commodity spread, inventory/repricing, volume, margin, or revision bridge, not material supercycle or metal label alone","KBI Metal positive worked; Choil Aluminum and Sama Aluminum theme/event rows failed positive-stage promotion","R4L90_C15_KBIMETAL_2024_STAGE2_ACTIONABLE_COPPER_SPREAD_MARGIN_BRIDGE|R4L90_C15_CHOILALUMINUM_2024_STAGE2_FALSE_POSITIVE_ALUMINUM_THEME|R4L90_C15_SAMAALUMINUM_2024_STAGE4B_ALUMINUM_FOIL_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,configured,cap_aluminum_and_material_theme_premiums_as_4B_watch,0,"Aluminum/foil/material theme premiums can peak before verified spread/margin bridge appears","Choil Aluminum showed limited MFE; Sama Aluminum showed full-window event-cap behavior with severe MAE","R4L90_C15_CHOILALUMINUM_2024_STAGE2_FALSE_POSITIVE_ALUMINUM_THEME|R4L90_C15_SAMAALUMINUM_2024_STAGE4B_ALUMINUM_FOIL_EVENT_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L90_C15_KBIMETAL_2024_COPPER_SPREAD_MARGIN_BRIDGE_POSITIVE", "symbol": "024840", "company_name": "KBI메탈", "round": "R4", "loop": "90", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_SPREAD_MARGIN_BRIDGE_VS_ALUMINUM_THEME_AND_FOIL_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R4L90_C15_KBIMETAL_2024_STAGE2_ACTIONABLE_COPPER_SPREAD_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Copper/non-ferrous spread and margin bridge produced a very large 30D/90D MFE with shallow initial MAE; C15 works when spread, inventory/repricing, volume, and margin bridge are visible.", "current_profile_verdict": "current_profile_kept_but_C15_positive_requires_spread_margin_inventory_or_pricing_bridge_not_commodity_label_only", "price_source": "Songdaiki/stock-web", "notes": "Modern 2024 window is clean relative to old corporate-action candidates; source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R4L90_C15_CHOILALUMINUM_2024_ALUMINUM_THEME_FALSE_STAGE2", "symbol": "018470", "company_name": "조일알미늄", "round": "R4", "loop": "90", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_SPREAD_MARGIN_BRIDGE_VS_ALUMINUM_THEME_AND_FOIL_EVENT_CAP", "case_type": "failed_rerating_theme_spike", "positive_or_counterexample": "counterexample", "best_trigger": "R4L90_C15_CHOILALUMINUM_2024_STAGE2_FALSE_POSITIVE_ALUMINUM_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Aluminum spread/theme spike showed limited forward MFE and material MAE; C15 Stage2 should not be awarded without a verified pricing/margin/inventory bridge.", "current_profile_verdict": "current_profile_false_positive_if_aluminum_theme_counts_without_spread_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; CA candidates are 2012 or earlier. Source-proxy only."}
{"row_type": "case", "case_id": "R4L90_C15_SAMAALUMINUM_2024_ALUMINUM_FOIL_EVENT_CAP_4B", "symbol": "006110", "company_name": "삼아알미늄", "round": "R4", "loop": "90", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_SPREAD_MARGIN_BRIDGE_VS_ALUMINUM_THEME_AND_FOIL_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L90_C15_SAMAALUMINUM_2024_STAGE4B_ALUMINUM_FOIL_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Aluminum foil / battery-material premium capped around the June spike and then de-rated deeply; material theme premium should route to 4B unless spread/margin/reorder bridge remains expanding.", "current_profile_verdict": "current_profile_4B_too_late_if_aluminum_foil_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after 2023-02-09 CA candidate. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L90_C15_KBIMETAL_2024_STAGE2_ACTIONABLE_COPPER_SPREAD_MARGIN_BRIDGE", "case_id": "R4L90_C15_KBIMETAL_2024_COPPER_SPREAD_MARGIN_BRIDGE_POSITIVE", "symbol": "024840", "company_name": "KBI메탈", "round": "R4", "loop": "90", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_SPREAD_MARGIN_BRIDGE_VS_ALUMINUM_THEME_AND_FOIL_EVENT_CAP", "sector": "copper_nonferrous_spread_margin", "primary_archetype": "copper_nonferrous_spread_margin_inventory_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-05", "entry_date": "2024-04-05", "entry_price": 1535.0, "evidence_available_at_that_date": "copper/non-ferrous spread, repricing, inventory and margin bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["copper_spread_supercycle_proxy", "inventory_repricing_bridge", "volume_margin_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "controlled_entry_MAE"], "stage4b_evidence_fields": ["valuation_watch_after_material_spread_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024840/2024.csv", "profile_path": "atlas/symbol_profiles/024/024840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 209.12, "MFE_90D_pct": 209.12, "MFE_180D_pct": 209.12, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.0, "MAE_90D_pct": -3.0, "MAE_180D_pct": -3.0, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-21", "peak_price": 4745.0, "drawdown_after_peak_pct": -54.16, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_material_spread_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "commodity_spread_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_copper_spread_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L90_C15_024840_2024-04-05_1535", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L90_C15_CHOILALUMINUM_2024_STAGE2_FALSE_POSITIVE_ALUMINUM_THEME", "case_id": "R4L90_C15_CHOILALUMINUM_2024_ALUMINUM_THEME_FALSE_STAGE2", "symbol": "018470", "company_name": "조일알미늄", "round": "R4", "loop": "90", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_SPREAD_MARGIN_BRIDGE_VS_ALUMINUM_THEME_AND_FOIL_EVENT_CAP", "sector": "aluminum_spread_theme", "primary_archetype": "aluminum_theme_without_spread_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-18", "entry_date": "2024-04-18", "entry_price": 2510.0, "evidence_available_at_that_date": "aluminum spread/theme spike and non-ferrous materials premium proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["aluminum_theme_spike", "nonferrous_spread_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "margin_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018470/2024.csv", "profile_path": "atlas/symbol_profiles/018/018470.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.96, "MFE_90D_pct": 9.96, "MFE_180D_pct": 9.96, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -13.35, "MAE_90D_pct": -20.32, "MAE_180D_pct": -20.32, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-18", "peak_price": 2760.0, "drawdown_after_peak_pct": -27.54, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "aluminum_theme_spike_was_false_stage2_event_cap", "four_b_evidence_type": ["commodity_spread_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_aluminum_theme_without_spread_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_aluminum_theme_counts_without_spread_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L90_C15_018470_2024-04-18_2510", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L90_C15_SAMAALUMINUM_2024_STAGE4B_ALUMINUM_FOIL_EVENT_CAP", "case_id": "R4L90_C15_SAMAALUMINUM_2024_ALUMINUM_FOIL_EVENT_CAP_4B", "symbol": "006110", "company_name": "삼아알미늄", "round": "R4", "loop": "90", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_SPREAD_MARGIN_BRIDGE_VS_ALUMINUM_THEME_AND_FOIL_EVENT_CAP", "sector": "aluminum_foil_battery_material_spread", "primary_archetype": "aluminum_foil_material_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-06-11", "entry_date": "2024-06-11", "entry_price": 96300.0, "evidence_available_at_that_date": "aluminum foil / battery-material and non-ferrous spread premium after June spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["aluminum_foil_theme", "battery_material_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv", "profile_path": "atlas/symbol_profiles/006/006110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.62, "MFE_90D_pct": 0.62, "MFE_180D_pct": 0.62, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -23.57, "MAE_90D_pct": -58.88, "MAE_180D_pct": -58.88, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-11", "peak_price": 96900.0, "drawdown_after_peak_pct": -59.13, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_aluminum_foil_material_event_cap", "four_b_evidence_type": ["commodity_spread_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_aluminum_foil_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2023-02-09_CA", "same_entry_group_id": "R4L90_C15_006110_2024-06-11_96300", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L90_C15_KBIMETAL_2024_COPPER_SPREAD_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R4L90_C15_KBIMETAL_2024_STAGE2_ACTIONABLE_COPPER_SPREAD_MARGIN_BRIDGE", "symbol": "024840", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 45, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "backlog_visibility_score"], "component_delta_explanation": "copper_spread_margin_bridge_positive", "MFE_90D_pct": 209.12, "MAE_90D_pct": -3.0, "score_return_alignment_label": "copper_spread_margin_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L90_C15_CHOILALUMINUM_2024_ALUMINUM_THEME_FALSE_STAGE2", "trigger_id": "R4L90_C15_CHOILALUMINUM_2024_STAGE2_FALSE_POSITIVE_ALUMINUM_THEME", "symbol": "018470", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "backlog_visibility_score"], "component_delta_explanation": "aluminum_theme_false_stage2", "MFE_90D_pct": 9.96, "MAE_90D_pct": -20.32, "score_return_alignment_label": "aluminum_theme_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_aluminum_theme_counts_without_spread_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L90_C15_SAMAALUMINUM_2024_ALUMINUM_FOIL_EVENT_CAP_4B", "trigger_id": "R4L90_C15_SAMAALUMINUM_2024_STAGE4B_ALUMINUM_FOIL_EVENT_CAP", "symbol": "006110", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "backlog_visibility_score"], "component_delta_explanation": "aluminum_foil_event_cap_4B_guard", "MFE_90D_pct": 0.62, "MAE_90D_pct": -58.88, "score_return_alignment_label": "aluminum_foil_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_aluminum_foil_theme_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "90", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_SPREAD_MARGIN_BRIDGE_VS_ALUMINUM_THEME_AND_FOIL_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["copper_spread_margin_bridge_positive", "aluminum_theme_false_stage2", "aluminum_foil_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
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
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R4
completed_loop = 90
next_round = R5
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
