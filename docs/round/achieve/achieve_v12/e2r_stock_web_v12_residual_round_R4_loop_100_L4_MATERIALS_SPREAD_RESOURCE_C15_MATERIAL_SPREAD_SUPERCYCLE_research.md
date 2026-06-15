# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 100
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = COPPER_SPREAD_VOLUME_MARGIN_BRIDGE_VS_LITHIUM_STEEL_SUPERCYCLE_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP
loop_objective = priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | material_spread_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R4_loop_100_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. A C05 duplicate artifact was generated during this run but is not the final artifact because C05 was already finalized immediately before. Priority 1 already added C03, C16, C04 and C05, so C15 is the next unsupplemented Priority 1 gap below the 50-row practical calibration zone. Because R4 loop98/99 were used locally for C17/C16, this file uses R4 loop100 to avoid local round-loop collision.

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
material_spread_margin_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R4
scheduled_loop = 100
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C15 is a material-spread supercycle archetype. The supercycle headline is the tide chart; the investable signal is whether realized spread, volume, inventory turn, pass-through, FCF/margin and revision actually lift the company’s boat.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C15_MATERIAL_SPREAD_SUPERCYCLE = 33 rows / Priority 1
recent local Priority 0/1 artifacts accounted for: C08, C09, C01, C07, C06, C10, C14, C11, C02, C13, C19, C27, C12, C24, C28, C17, C23, C03, C16, C04, C05
C05 duplicate generated during this run discarded from final output
```

Selected rows avoid hard duplicates and add new C15 trigger families:

```text
103140 / Stage2-Actionable / 2024-02-22
005490 / Stage2-Actionable / 2024-01-02
009520 / Stage4B / 2024-01-03
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
| 103140 | atlas/symbol_profiles/103/103140.json | no corporate-action candidate |
| 005490 | atlas/symbol_profiles/005/005490.json | no corporate-action candidate |
| 009520 | atlas/symbol_profiles/009/009520.json | selected 2024 window clean after old 1999/2011/2012 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R4L100_C15_POONGSAN_2024_COPPER_SPREAD_VOLUME_MARGIN_BRIDGE_POSITIVE | 103140 | 2024-02-22 | yes | 180 | yes | yes | true |
| R4L100_C15_POSCOHOLDINGS_2024_LITHIUM_STEEL_SUPERCYCLE_FALSE_STAGE2 | 005490 | 2024-01-02 | yes | 180 | yes | yes | true |
| R4L100_C15_POSCOMTECH_2024_LITHIUM_MATERIAL_EVENT_CAP_4B | 009520 | 2024-01-03 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C15_MATERIAL_SPREAD_SUPERCYCLE | COPPER_SPREAD_VOLUME_MARGIN_BRIDGE | Positive Stage2 requires realized spread, volume, inventory, pass-through, FCF/margin and revision bridge. |
| C15_MATERIAL_SPREAD_SUPERCYCLE | LITHIUM_STEEL_FALSE_STAGE2 | Lithium/steel supercycle watch without realized spread and margin bridge can become false Stage2. |
| C15_MATERIAL_SPREAD_SUPERCYCLE | LITHIUM_MATERIAL_EVENT_CAP_4B | Lithium/material event premium should route to 4B when spread-margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R4L100_C15_POONGSAN_2024_COPPER_SPREAD_VOLUME_MARGIN_BRIDGE_POSITIVE | 103140 | 풍산 | positive | Copper/material spread-volume bridge produced strong MFE with shallow early MAE. |
| R4L100_C15_POSCOHOLDINGS_2024_LITHIUM_STEEL_SUPERCYCLE_FALSE_STAGE2 | 005490 | POSCO홀딩스 | counterexample | Lithium/steel supercycle watch had tiny MFE and persistent MAE without realized spread/margin bridge. |
| R4L100_C15_POSCOMTECH_2024_LITHIUM_MATERIAL_EVENT_CAP_4B | 009520 | 포스코엠텍 | counterexample / 4B | Lithium/material event premium capped after the early-January spike and then de-rated. |

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
| Poongsan copper/material spread bridge | historical public/report proxy | true | true | shadow-only positive |
| POSCO Holdings lithium/steel supercycle false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| POSCO M-Tech lithium/material event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 103140 | atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv | atlas/symbol_profiles/103/103140.json |
| 005490 | atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv | atlas/symbol_profiles/005/005490.json |
| 009520 | atlas/ohlcv_tradable_by_symbol_year/009/009520/2024.csv | atlas/symbol_profiles/009/009520.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R4L100_C15_POONGSAN_2024_STAGE2_ACTIONABLE_COPPER_SPREAD_VOLUME_MARGIN_BRIDGE | 103140 | Stage2-Actionable | 2024-02-22 | 42200 | positive | copper spread-volume margin bridge worked |
| R4L100_C15_POSCOHOLDINGS_2024_STAGE2_FALSE_POSITIVE_LITHIUM_STEEL_SUPERCYCLE_WATCH | 005490 | Stage2-Actionable | 2024-01-02 | 488000 | counterexample | lithium/steel supercycle false Stage2 |
| R4L100_C15_POSCOMTECH_2024_STAGE4B_LITHIUM_MATERIAL_EVENT_CAP | 009520 | Stage4B | 2024-01-03 | 29950 | counterexample/4B | lithium/material event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R4L100_C15_POONGSAN_2024_STAGE2_ACTIONABLE_COPPER_SPREAD_VOLUME_MARGIN_BRIDGE | 42200 | 27.49 | -1.66 | 83.41 | -1.66 | 83.41 | -1.66 | 2024-05-07 | 77400 | -28.17 |
| R4L100_C15_POSCOHOLDINGS_2024_STAGE2_FALSE_POSITIVE_LITHIUM_STEEL_SUPERCYCLE_WATCH | 488000 | 1.64 | -20.70 | 1.64 | -22.03 | 1.64 | -36.68 | 2024-01-02 | 496000 | -37.70 |
| R4L100_C15_POSCOMTECH_2024_STAGE4B_LITHIUM_MATERIAL_EVENT_CAP | 29950 | 11.19 | -20.20 | 11.19 | -33.26 | 11.19 | -38.90 | 2024-01-03 | 33300 | -39.97 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C15 Stage2 needs realized spread / volume / inventory / pass-through / FCF-margin / revision bridge |
| material_spread_margin_guardrail | strengthen: material supercycle label alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing lithium/steel/material premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C15 rows cannot promote without durable realized margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether material-spread narrative becomes realized spread, volume, inventory and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 103140 | good_stage2_with_later_watch | Copper-spread volume/margin bridge produced strong MFE with shallow MAE, but later spread valuation watch remains necessary. |
| 005490 | bad_stage2 | Lithium/steel supercycle watch lacked realized spread/margin bridge and produced tiny MFE with persistent MAE. |
| 009520 | good_4B | Lithium/material event premium peaked immediately and later de-rated sharply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 005490 lithium/steel false Stage2 | 0.98 | 0.98 | false Stage2 due missing realized spread / volume / inventory / margin bridge |
| 009520 lithium material event cap | 0.90 | 0.90 | good full-window 4B timing after lithium/material supercycle premium |
| 103140 copper spread bridge | n/a | n/a | positive Stage2, but later material-spread valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 005490 / 009520
```

No hard 4C candidate is introduced in this C15 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L4 material spread supercycle cases, Stage2 requires verified realized product spread, volume recovery, inventory turn, ASP/cost pass-through, FCF/margin and revision bridge. Supercycle, lithium, steel, copper, nonferrous, raw-material or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
rule = C15 should split true realized-spread/volume/margin positives from lithium/steel false Stage2 and material event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 32.08 | -18.98 | 0.67 | mixed; C15 realized-spread bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 32.08 | -18.98 | 0.67 | weaker C15 bridge split |
| P1 sector_specific_candidate_profile | L4 realized-spread/margin bridge required | 2 | 42.53 | -11.85 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C15 bridge vs event-cap split | 2 | 42.53 | -11.85 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing material-supercycle themes as positive | 1 | 83.41 | -1.66 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 103140 copper spread bridge | 66 | Stage2-Watch | 79 | Stage2-Actionable | 83.41 | -1.66 | material_spread_supercycle_positive |
| 005490 lithium/steel false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 1.64 | -22.03 | lithium_steel_false_stage2 |
| 009520 lithium material cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 11.19 | -33.26 | lithium_material_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_SPREAD_VOLUME_MARGIN_BRIDGE_VS_LITHIUM_STEEL_SUPERCYCLE_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C15 is the next unsupplemented Priority 1 archetype after C03/C16/C04/C05 and still remains below the practical 50-row calibration zone. This run adds Poongsan, POSCO Holdings, and POSCO M-Tech while avoiding the immediately preceding C05 artifact and top repeated C15 families."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, material_spread_margin_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: material_spread_supercycle_positive, lithium_steel_false_stage2, lithium_material_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, material_spread_margin_guardrail, high_MAE_guardrail
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
- C15 material-spread supercycle bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,configured,C15_requires_realized_spread_volume_inventory_pass_through_margin_revision_bridge,0,"C15 Stage2 should require realized product spread, volume recovery, inventory turn, ASP/cost pass-through, FCF/margin and revision bridge, not material supercycle label alone","Poongsan positive worked; POSCO Holdings and POSCO M-Tech event/watch rows failed positive-stage promotion","R4L100_C15_POONGSAN_2024_STAGE2_ACTIONABLE_COPPER_SPREAD_VOLUME_MARGIN_BRIDGE|R4L100_C15_POSCOHOLDINGS_2024_STAGE2_FALSE_POSITIVE_LITHIUM_STEEL_SUPERCYCLE_WATCH|R4L100_C15_POSCOMTECH_2024_STAGE4B_LITHIUM_MATERIAL_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,configured,cap_bridge_missing_lithium_steel_and_material_event_premiums_as_4B_watch,0,"Lithium/steel/material supercycle premiums can peak before realized spread, volume, inventory and margin bridge is proven","POSCO Holdings had tiny MFE and persistent MAE after January high; POSCO M-Tech showed 4B event-cap behavior after early-January lithium/material premium","R4L100_C15_POSCOHOLDINGS_2024_STAGE2_FALSE_POSITIVE_LITHIUM_STEEL_SUPERCYCLE_WATCH|R4L100_C15_POSCOMTECH_2024_STAGE4B_LITHIUM_MATERIAL_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,configured,block_positive_stage_when_material_supercycle_theme_has_high_or_persistent_MAE_without_realized_margin_bridge,0,"High or persistent MAE after bridge-missing C15 entries should block Stage2/Stage3 promotion unless realized spread, inventory and margin evidence survives","POSCO Holdings MAE180=-36.68 and POSCO M-Tech MAE90=-33.26","R4L100_C15_POSCOHOLDINGS_2024_STAGE2_FALSE_POSITIVE_LITHIUM_STEEL_SUPERCYCLE_WATCH|R4L100_C15_POSCOMTECH_2024_STAGE4B_LITHIUM_MATERIAL_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L100_C15_POONGSAN_2024_COPPER_SPREAD_VOLUME_MARGIN_BRIDGE_POSITIVE", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": "100", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_SPREAD_VOLUME_MARGIN_BRIDGE_VS_LITHIUM_STEEL_SUPERCYCLE_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP", "case_type": "structural_success_with_later_copper_spread_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R4L100_C15_POONGSAN_2024_STAGE2_ACTIONABLE_COPPER_SPREAD_VOLUME_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Copper / nonferrous material-spread supercycle bridge produced strong 30D/90D MFE after the February copper-spread breakout with shallow early MAE. C15 works when spread-supercycle narrative is tied to realized product spread, volume, inventory, pass-through, FCF/margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C15_positive_requires_realized_spread_volume_inventory_pass_through_margin_revision_bridge_not_material_supercycle_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Same symbol appeared in another canonical artifact, but hard duplicate key differs because canonical_archetype_id and entry_date differ. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R4L100_C15_POSCOHOLDINGS_2024_LITHIUM_STEEL_SUPERCYCLE_FALSE_STAGE2", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": "100", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_SPREAD_VOLUME_MARGIN_BRIDGE_VS_LITHIUM_STEEL_SUPERCYCLE_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP", "case_type": "failed_rerating_lithium_steel_material_spread_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R4L100_C15_POSCOHOLDINGS_2024_STAGE2_FALSE_POSITIVE_LITHIUM_STEEL_SUPERCYCLE_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Lithium/steel material supercycle watch at the January high had only tiny MFE and then persistent drawdown. C15 Stage2 should not be awarded without realized ASP/spread, volume recovery, inventory normalization, cost pass-through, FCF/margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_lithium_steel_supercycle_watch_counts_without_realized_spread_volume_inventory_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R4L100_C15_POSCOMTECH_2024_LITHIUM_MATERIAL_EVENT_CAP_4B", "symbol": "009520", "company_name": "포스코엠텍", "round": "R4", "loop": "100", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_SPREAD_VOLUME_MARGIN_BRIDGE_VS_LITHIUM_STEEL_SUPERCYCLE_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L100_C15_POSCOMTECH_2024_STAGE4B_LITHIUM_MATERIAL_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Lithium/material event premium capped immediately after the early-January spike and then de-rated sharply. C15 should route bridge-missing material supercycle premiums to 4B unless realized spread, volume, inventory turn, ASP/cost pass-through, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_lithium_material_supercycle_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1999/2011/2012 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L100_C15_POONGSAN_2024_STAGE2_ACTIONABLE_COPPER_SPREAD_VOLUME_MARGIN_BRIDGE", "case_id": "R4L100_C15_POONGSAN_2024_COPPER_SPREAD_VOLUME_MARGIN_BRIDGE_POSITIVE", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": "100", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_SPREAD_VOLUME_MARGIN_BRIDGE_VS_LITHIUM_STEEL_SUPERCYCLE_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP", "sector": "copper_nonferrous_spread_volume_margin", "primary_archetype": "realized_spread_volume_inventory_pass_through_margin_revision_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | material_spread_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "entry_date": "2024-02-22", "entry_price": 42200.0, "evidence_available_at_that_date": "copper / nonferrous material spread, volume recovery, inventory discipline, ASP/cost pass-through and margin/revision bridge proxy after February breakout; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["realized_spread_proxy", "volume_recovery_proxy", "inventory_discipline_proxy", "cost_pass_through_proxy", "FCF_margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "very_strong_MFE90", "shallow_initial_MAE"], "stage4b_evidence_fields": ["later_copper_spread_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 27.49, "MFE_90D_pct": 83.41, "MFE_180D_pct": 83.41, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.66, "MAE_90D_pct": -1.66, "MAE_180D_pct": -1.66, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-07", "peak_price": 77400.0, "drawdown_after_peak_pct": -28.17, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_material_spread_valuation_4B_watch_needed", "four_b_evidence_type": ["material_spread_margin_bridge", "volume_inventory_FCF", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_copper_spread_volume_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R4L100_C15_103140_2024-02-22_42200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L100_C15_POSCOHOLDINGS_2024_STAGE2_FALSE_POSITIVE_LITHIUM_STEEL_SUPERCYCLE_WATCH", "case_id": "R4L100_C15_POSCOHOLDINGS_2024_LITHIUM_STEEL_SUPERCYCLE_FALSE_STAGE2", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": "100", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_SPREAD_VOLUME_MARGIN_BRIDGE_VS_LITHIUM_STEEL_SUPERCYCLE_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP", "sector": "lithium_steel_material_supercycle_watch", "primary_archetype": "lithium_steel_supercycle_watch_without_realized_spread_volume_inventory_margin_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | material_spread_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "entry_date": "2024-01-02", "entry_price": 488000.0, "evidence_available_at_that_date": "lithium/steel material supercycle watch without confirmed realized spread, volume recovery, inventory turn, cost pass-through, FCF or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["lithium_steel_supercycle_watch", "material_spread_beta", "relative_strength_old_premium"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["tiny_MFE90", "persistent_MAE90", "realized_spread_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv", "profile_path": "atlas/symbol_profiles/005/005490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.64, "MFE_90D_pct": 1.64, "MFE_180D_pct": 1.64, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -20.7, "MAE_90D_pct": -22.03, "MAE_180D_pct": -36.68, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-02", "peak_price": 496000.0, "drawdown_after_peak_pct": -37.7, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "lithium_steel_supercycle_watch_was_false_stage2_due_missing_realized_spread_volume_inventory_margin_revision_bridge", "four_b_evidence_type": ["material_supercycle_premium", "bridge_missing", "tiny_MFE_high_MAE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_lithium_steel_supercycle_without_realized_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_lithium_steel_supercycle_watch_counts_without_realized_spread_volume_inventory_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R4L100_C15_005490_2024-01-02_488000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L100_C15_POSCOMTECH_2024_STAGE4B_LITHIUM_MATERIAL_EVENT_CAP", "case_id": "R4L100_C15_POSCOMTECH_2024_LITHIUM_MATERIAL_EVENT_CAP_4B", "symbol": "009520", "company_name": "포스코엠텍", "round": "R4", "loop": "100", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_SPREAD_VOLUME_MARGIN_BRIDGE_VS_LITHIUM_STEEL_SUPERCYCLE_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP", "sector": "lithium_material_supercycle_event_premium", "primary_archetype": "lithium_material_event_cap_4B", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | material_spread_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-03", "entry_date": "2024-01-03", "entry_price": 29950.0, "evidence_available_at_that_date": "lithium/material supercycle event premium without confirmed realized spread, volume, inventory, ASP/cost pass-through, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["lithium_material_event", "material_supercycle_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "spread_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009520/2024.csv", "profile_path": "atlas/symbol_profiles/009/009520.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.19, "MFE_90D_pct": 11.19, "MFE_180D_pct": 11.19, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -20.2, "MAE_90D_pct": -33.26, "MAE_180D_pct": -38.9, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-03", "peak_price": 33300.0, "drawdown_after_peak_pct": -39.97, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "good_full_window_4B_timing_lithium_material_event_cap_due_missing_realized_spread_margin_bridge", "four_b_evidence_type": ["lithium_material_event_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_lithium_material_supercycle_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_lithium_material_supercycle_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1999_2011_2012_CA", "same_entry_group_id": "R4L100_C15_009520_2024-01-03_29950", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R4L100_C15_POONGSAN_2024_COPPER_SPREAD_VOLUME_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R4L100_C15_POONGSAN_2024_STAGE2_ACTIONABLE_COPPER_SPREAD_VOLUME_MARGIN_BRIDGE", "symbol": "103140", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 45, "margin_bridge_score": 65, "revision_score": 60, "relative_strength_score": 85, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "copper_spread_volume_margin_positive", "MFE_90D_pct": 83.41, "MAE_90D_pct": -1.66, "score_return_alignment_label": "material_spread_supercycle_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R4L100_C15_POSCOHOLDINGS_2024_LITHIUM_STEEL_SUPERCYCLE_FALSE_STAGE2", "trigger_id": "R4L100_C15_POSCOHOLDINGS_2024_STAGE2_FALSE_POSITIVE_LITHIUM_STEEL_SUPERCYCLE_WATCH", "symbol": "005490", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 60, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "lithium_steel_supercycle_false_stage2", "MFE_90D_pct": 1.64, "MAE_90D_pct": -22.03, "score_return_alignment_label": "lithium_steel_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_lithium_steel_supercycle_watch_counts_without_realized_spread_volume_inventory_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R4L100_C15_POSCOMTECH_2024_LITHIUM_MATERIAL_EVENT_CAP_4B", "trigger_id": "R4L100_C15_POSCOMTECH_2024_STAGE4B_LITHIUM_MATERIAL_EVENT_CAP", "symbol": "009520", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "lithium_material_event_cap_4B_guard", "MFE_90D_pct": 11.19, "MAE_90D_pct": -33.26, "score_return_alignment_label": "lithium_material_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_lithium_material_supercycle_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "100", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_SPREAD_VOLUME_MARGIN_BRIDGE_VS_LITHIUM_STEEL_SUPERCYCLE_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "material_spread_margin_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["material_spread_supercycle_positive", "lithium_steel_false_stage2", "lithium_material_event_cap_4B"], "loop_contribution_label": "priority1_canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C15 rows need explicit realized product spread, volume recovery, inventory turn, ASP/cost pass-through, FCF/margin and revision bridge before positive promotion.
- In C15, bridge-missing material supercycle event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C15 material-spread supercycle rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R4
completed_loop = 100
completed_canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
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
