# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = COATED_STEEL_SPREAD_MARGIN_BRIDGE_VS_STAINLESS_NICKEL_FALSE_STAGE2_AND_ALUMINUM_POLICY_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R4_loop_96_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
```

This file is the corrected final output for this execution. The scheduler state after R3 loop 96 is R4 / loop 96. R4 is the L4 materials/spread/resource round, and this run fills C15 material spread supercycle rather than repeating the immediately preceding R4 loop 95 C16 strategic-resource file or R4 loop 94 C17 chemical spread file.

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
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R4
scheduled_loop = 96
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
round_sector_consistency = pass
computed_next_round = R5
computed_next_loop = 96
```

C15 is a product-spread-to-margin bridge archetype. A commodity or material-cycle label is only the refinery smoke; the evidence is realized spread, inventory discipline, shipment mix, ASP pass-through, margin and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C15_MATERIAL_SPREAD_SUPERCYCLE = 28 rows / 11 symbols / good-bad Stage2 13-0 / 4B-4C 3-0
top covered symbols include 103140(6), 012800(5), 025820(5), 004560(3), 021050(3), 001780(1)
previous R4 loop-90 C15 symbols avoided: 024840, 018470, 006110
previous R4 loop-93 C15 symbols avoided: 003030, 016380, 024060
previous R4 loop-94 C17 symbols avoided: 002380, 011170, 004090
previous R4 loop-95 C16 symbols avoided: 103140, 075970, 011810
previous R3 loop-96 C11 symbols avoided: 006110, 079810, 417010
```

Selected rows avoid hard duplicates and top repeated C15 symbols:

```text
058430 / Stage2-Actionable / 2024-01-22
032560 / Stage2-Actionable / 2024-01-31
008350 / Stage4B / 2024-01-02
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
| 058430 | atlas/symbol_profiles/058/058430.json | selected 2024 window clean after old name-history / CA candidates |
| 032560 | atlas/symbol_profiles/032/032560.json | selected 2024 window clean after old CA / market-history candidates |
| 008350 | atlas/symbol_profiles/008/008350.json | selected 2024 window clean after old CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R4L96_C15_POSCOSTEELION_2024_COATED_STEEL_SPREAD_MARGIN_POSITIVE | 058430 | 2024-01-22 | yes | 180 | yes | yes | true |
| R4L96_C15_HWANGGEUMST_2024_STAINLESS_NICKEL_SPREAD_FALSE_STAGE2 | 032560 | 2024-01-31 | yes | 180 | yes | yes | true |
| R4L96_C15_NAMSEONALUMINUM_2024_ALUMINUM_POLICY_SPREAD_EVENT_CAP_4B | 008350 | 2024-01-02 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C15_MATERIAL_SPREAD_SUPERCYCLE | COATED_STEEL_SPREAD_MARGIN_BRIDGE | Positive Stage2 requires realized product spread, shipment/export mix, inventory discipline, margin and revision bridge. |
| C15_MATERIAL_SPREAD_SUPERCYCLE | STAINLESS_NICKEL_FALSE_STAGE2 | Stainless/nickel spread watch without inventory and margin bridge can become false Stage2. |
| C15_MATERIAL_SPREAD_SUPERCYCLE | ALUMINUM_POLICY_EVENT_CAP_4B | Aluminum/material policy event premium should route to 4B when shipment and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R4L96_C15_POSCOSTEELION_2024_COATED_STEEL_SPREAD_MARGIN_POSITIVE | 058430 | 포스코스틸리온 | positive | Coated-steel spread/margin bridge produced moderate MFE with controlled early MAE. |
| R4L96_C15_HWANGGEUMST_2024_STAINLESS_NICKEL_SPREAD_FALSE_STAGE2 | 032560 | 황금에스티 | counterexample | Stainless/nickel spread spike did not prove shipment or margin bridge. |
| R4L96_C15_NAMSEONALUMINUM_2024_ALUMINUM_POLICY_SPREAD_EVENT_CAP_4B | 008350 | 남선알미늄 | counterexample / 4B | Aluminum/policy spread premium capped immediately and then de-rated. |

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
| POSCO Steeleon coated-steel spread/margin bridge | historical public/report proxy | true | true | shadow-only positive |
| Hwanggeum ST stainless/nickel false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Namseon Aluminum aluminum-policy event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 058430 | atlas/ohlcv_tradable_by_symbol_year/058/058430/2024.csv | atlas/symbol_profiles/058/058430.json |
| 032560 | atlas/ohlcv_tradable_by_symbol_year/032/032560/2024.csv | atlas/symbol_profiles/032/032560.json |
| 008350 | atlas/ohlcv_tradable_by_symbol_year/008/008350/2024.csv | atlas/symbol_profiles/008/008350.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R4L96_C15_POSCOSTEELION_2024_STAGE2_ACTIONABLE_COATED_STEEL_SPREAD_MARGIN_BRIDGE | 058430 | Stage2-Actionable | 2024-01-22 | 47350 | positive | coated-steel spread/margin bridge worked |
| R4L96_C15_HWANGGEUMST_2024_STAGE2_FALSE_POSITIVE_STAINLESS_NICKEL_SPREAD_WATCH | 032560 | Stage2-Actionable | 2024-01-31 | 7330 | counterexample | stainless/nickel spread false Stage2 |
| R4L96_C15_NAMSEONALUMINUM_2024_STAGE4B_ALUMINUM_POLICY_SPREAD_EVENT_CAP | 008350 | Stage4B | 2024-01-02 | 2515 | counterexample/4B | aluminum policy/material-spread event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R4L96_C15_POSCOSTEELION_2024_STAGE2_ACTIONABLE_COATED_STEEL_SPREAD_MARGIN_BRIDGE | 47350 | 12.57 | -0.53 | 12.57 | -12.78 | 12.57 | -15.10 | 2024-02-16 | 53300 | -21.76 |
| R4L96_C15_HWANGGEUMST_2024_STAGE2_FALSE_POSITIVE_STAINLESS_NICKEL_SPREAD_WATCH | 7330 | 2.32 | -5.19 | 2.32 | -10.50 | 2.32 | -13.78 | 2024-01-31 | 7500 | -14.67 |
| R4L96_C15_NAMSEONALUMINUM_2024_STAGE4B_ALUMINUM_POLICY_SPREAD_EVENT_CAP | 2515 | 4.57 | -18.49 | 4.57 | -28.15 | 4.57 | -28.15 | 2024-01-02 | 2630 | -31.29 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C15 Stage2 needs realized spread / inventory / shipment mix / pass-through / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing metal spread/policy premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE aluminum/material event rows cannot promote without durable margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether metal-spread narrative becomes realized margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 058430 | good_stage2_with_later_watch | Product-spread/margin bridge produced moderate MFE with controlled early MAE. |
| 032560 | bad_stage2 | Stainless/nickel spread watch lacked shipment/inventory/margin bridge and produced tiny MFE. |
| 008350 | good_4B | Aluminum-policy premium capped immediately and then suffered high MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 032560 stainless/nickel false Stage2 | 0.98 | 0.98 | false Stage2 due missing shipment / inventory / margin bridge |
| 008350 aluminum policy cap | 0.96 | 0.96 | good full-window 4B timing after first-trading-day aluminum/material-spread event premium |
| 058430 coated-steel bridge | n/a | n/a | positive Stage2, but later material-spread valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 032560 / 008350
```

No hard 4C candidate is introduced in this R4 loop 96 file. The counterexamples are bridge-missing / event-cap rows, not hard thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L4 material-spread supercycle cases, Stage2 requires verified realized product spread, inventory discipline, shipment mix, ASP/pass-through, margin, or revision bridge. Metal cycle, aluminum, stainless, nickel, copper, steel, commodity, policy or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
rule = C15 should split true product-spread/inventory/margin positives from metal-spread false Stage2 and aluminum-policy event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 6.49 | -17.14 | 0.67 | mixed; C15 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 6.49 | -17.14 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L4 realized spread/margin bridge required | 2 | 7.45 | -11.64 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C15 bridge vs event-cap split | 2 | 7.45 | -11.64 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing metal spread themes as positive | 1 | 12.57 | -12.78 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 058430 coated-steel spread bridge | 64 | Stage2-Watch | 73 | Stage2-Actionable | 12.57 | -12.78 | coated_steel_spread_margin_positive |
| 032560 stainless/nickel false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 2.32 | -10.50 | stainless_nickel_false_stage2 |
| 008350 aluminum policy cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 4.57 | -28.15 | aluminum_policy_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COATED_STEEL_SPREAD_MARGIN_BRIDGE_VS_STAINLESS_NICKEL_FALSE_STAGE2_AND_ALUMINUM_POLICY_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C15 POSCO Steeleon coated-steel spread/margin positive, Hwanggeum ST stainless/nickel spread false Stage2, and Namseon Aluminum aluminum-policy event-cap 4B while avoiding top repeated C15 and previous R4/R3 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: coated_steel_spread_margin_positive, stainless_nickel_false_stage2, aluminum_policy_event_cap_4B
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
shadow_weight,stage2_required_bridge,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,configured,C15_requires_realized_product_spread_inventory_shipment_margin_revision_bridge,0,"C15 Stage2 should require realized product spread, inventory discipline, shipment mix, ASP pass-through, margin, or revision bridge, not material-cycle or commodity-spread label alone","POSCO Steeleon positive worked; Hwanggeum ST and Namseon Aluminum event/watch rows failed positive-stage promotion","R4L96_C15_POSCOSTEELION_2024_STAGE2_ACTIONABLE_COATED_STEEL_SPREAD_MARGIN_BRIDGE|R4L96_C15_HWANGGEUMST_2024_STAGE2_FALSE_POSITIVE_STAINLESS_NICKEL_SPREAD_WATCH|R4L96_C15_NAMSEONALUMINUM_2024_STAGE4B_ALUMINUM_POLICY_SPREAD_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,configured,cap_bridge_missing_metal_spread_policy_event_premiums_as_4B_watch,0,"Aluminum, stainless and metal-spread policy premiums can peak before shipment, inventory and margin bridge is proven","Hwanggeum ST had very low MFE after spread watch; Namseon Aluminum showed 4B event-cap behavior after the January aluminum-policy spike","R4L96_C15_HWANGGEUMST_2024_STAGE2_FALSE_POSITIVE_STAINLESS_NICKEL_SPREAD_WATCH|R4L96_C15_NAMSEONALUMINUM_2024_STAGE4B_ALUMINUM_POLICY_SPREAD_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,configured,block_positive_stage_when_material_spread_theme_has_high_or_persistent_MAE_without_margin_bridge,0,"High or persistent MAE after bridge-missing C15 entries should block Stage2/Stage3 promotion unless product spread, shipment and margin evidence survives","Hwanggeum ST MAE180=-13.78 and Namseon Aluminum MAE90=-28.15","R4L96_C15_HWANGGEUMST_2024_STAGE2_FALSE_POSITIVE_STAINLESS_NICKEL_SPREAD_WATCH|R4L96_C15_NAMSEONALUMINUM_2024_STAGE4B_ALUMINUM_POLICY_SPREAD_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L96_C15_POSCOSTEELION_2024_COATED_STEEL_SPREAD_MARGIN_POSITIVE", "symbol": "058430", "company_name": "포스코스틸리온", "round": "R4", "loop": "96", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COATED_STEEL_SPREAD_MARGIN_BRIDGE_VS_STAINLESS_NICKEL_FALSE_STAGE2_AND_ALUMINUM_POLICY_EVENT_CAP", "case_type": "moderate_structural_success_with_later_steel_spread_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R4L96_C15_POSCOSTEELION_2024_STAGE2_ACTIONABLE_COATED_STEEL_SPREAD_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Coated-steel product spread, export/channel mix and margin-bridge setup produced a moderate forward MFE from the January washout with controlled early MAE. C15 works only when a material-spread narrative maps into realized product spread, inventory discipline, shipment mix, pass-through, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C15_positive_requires_product_spread_inventory_shipment_margin_revision_bridge_not_material_cycle_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old name-history/corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R4L96_C15_HWANGGEUMST_2024_STAINLESS_NICKEL_SPREAD_FALSE_STAGE2", "symbol": "032560", "company_name": "황금에스티", "round": "R4", "loop": "96", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COATED_STEEL_SPREAD_MARGIN_BRIDGE_VS_STAINLESS_NICKEL_FALSE_STAGE2_AND_ALUMINUM_POLICY_EVENT_CAP", "case_type": "failed_rerating_stainless_nickel_spread_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R4L96_C15_HWANGGEUMST_2024_STAGE2_FALSE_POSITIVE_STAINLESS_NICKEL_SPREAD_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stainless/nickel spread watch produced only a short premium around the January spike and did not prove shipment, inventory, ASP pass-through or margin revision. C15 Stage2 should not be awarded without product-spread realization and margin bridge.", "current_profile_verdict": "current_profile_false_positive_if_stainless_nickel_spread_watch_counts_without_shipment_inventory_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old corporate-action / KOSDAQ-to-KOSPI history. Source-proxy only."}
{"row_type": "case", "case_id": "R4L96_C15_NAMSEONALUMINUM_2024_ALUMINUM_POLICY_SPREAD_EVENT_CAP_4B", "symbol": "008350", "company_name": "남선알미늄", "round": "R4", "loop": "96", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COATED_STEEL_SPREAD_MARGIN_BRIDGE_VS_STAINLESS_NICKEL_FALSE_STAGE2_AND_ALUMINUM_POLICY_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L96_C15_NAMSEONALUMINUM_2024_STAGE4B_ALUMINUM_POLICY_SPREAD_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Aluminum/policy/material-spread event premium capped at the first trading-day spike and then de-rated through 30D/90D/180D. C15 should route bridge-missing aluminum spread/policy premiums to 4B unless shipment mix, pass-through, inventory and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_aluminum_policy_spread_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L96_C15_POSCOSTEELION_2024_STAGE2_ACTIONABLE_COATED_STEEL_SPREAD_MARGIN_BRIDGE", "case_id": "R4L96_C15_POSCOSTEELION_2024_COATED_STEEL_SPREAD_MARGIN_POSITIVE", "symbol": "058430", "company_name": "포스코스틸리온", "round": "R4", "loop": "96", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COATED_STEEL_SPREAD_MARGIN_BRIDGE_VS_STAINLESS_NICKEL_FALSE_STAGE2_AND_ALUMINUM_POLICY_EVENT_CAP", "sector": "coated_steel_product_spread_export_mix_margin", "primary_archetype": "product_spread_inventory_shipment_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-22", "entry_date": "2024-01-22", "entry_price": 47350.0, "evidence_available_at_that_date": "coated-steel product spread, export/channel mix, inventory discipline and margin/revision bridge proxy after January washout; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["coated_steel_spread_proxy", "export_mix_proxy", "inventory_discipline_proxy", "shipment_margin_bridge_proxy", "revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "positive_MFE90", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_steel_spread_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/058/058430/2024.csv", "profile_path": "atlas/symbol_profiles/058/058430.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.57, "MFE_90D_pct": 12.57, "MFE_180D_pct": 12.57, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -0.53, "MAE_90D_pct": -12.78, "MAE_180D_pct": -15.1, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-16", "peak_price": 53300.0, "drawdown_after_peak_pct": -21.76, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_steel_spread_valuation_4B_watch_needed", "four_b_evidence_type": ["product_spread_bridge", "export_margin_mix", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_coated_steel_spread_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_name_history_CA_candidates", "same_entry_group_id": "R4L96_C15_058430_2024-01-22_47350", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L96_C15_HWANGGEUMST_2024_STAGE2_FALSE_POSITIVE_STAINLESS_NICKEL_SPREAD_WATCH", "case_id": "R4L96_C15_HWANGGEUMST_2024_STAINLESS_NICKEL_SPREAD_FALSE_STAGE2", "symbol": "032560", "company_name": "황금에스티", "round": "R4", "loop": "96", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COATED_STEEL_SPREAD_MARGIN_BRIDGE_VS_STAINLESS_NICKEL_FALSE_STAGE2_AND_ALUMINUM_POLICY_EVENT_CAP", "sector": "stainless_nickel_material_spread_watch", "primary_archetype": "stainless_nickel_watch_without_shipment_inventory_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-31", "entry_date": "2024-01-31", "entry_price": 7330.0, "evidence_available_at_that_date": "stainless/nickel spread watch without confirmed shipment mix, inventory turn, ASP pass-through or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["stainless_nickel_spread_watch", "material_spread_sympathy", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "shipment_inventory_margin_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032560/2024.csv", "profile_path": "atlas/symbol_profiles/032/032560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.32, "MFE_90D_pct": 2.32, "MFE_180D_pct": 2.32, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -5.19, "MAE_90D_pct": -10.5, "MAE_180D_pct": -13.78, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-31", "peak_price": 7500.0, "drawdown_after_peak_pct": -14.67, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "stainless_nickel_spread_watch_was_false_stage2_due_missing_shipment_inventory_margin_bridge", "four_b_evidence_type": ["stainless_nickel_spread_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_stainless_nickel_spread_watch_without_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_stainless_nickel_spread_watch_counts_without_shipment_inventory_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA_market_history_candidates", "same_entry_group_id": "R4L96_C15_032560_2024-01-31_7330", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L96_C15_NAMSEONALUMINUM_2024_STAGE4B_ALUMINUM_POLICY_SPREAD_EVENT_CAP", "case_id": "R4L96_C15_NAMSEONALUMINUM_2024_ALUMINUM_POLICY_SPREAD_EVENT_CAP_4B", "symbol": "008350", "company_name": "남선알미늄", "round": "R4", "loop": "96", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COATED_STEEL_SPREAD_MARGIN_BRIDGE_VS_STAINLESS_NICKEL_FALSE_STAGE2_AND_ALUMINUM_POLICY_EVENT_CAP", "sector": "aluminum_policy_material_spread_event_premium", "primary_archetype": "aluminum_policy_spread_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-02", "entry_date": "2024-01-02", "entry_price": 2515.0, "evidence_available_at_that_date": "aluminum/material-spread policy event premium after first-trading-day spike without visible shipment mix, inventory or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["aluminum_policy_event", "material_spread_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "shipment_inventory_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008350/2024.csv", "profile_path": "atlas/symbol_profiles/008/008350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.57, "MFE_90D_pct": 4.57, "MFE_180D_pct": 4.57, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -18.49, "MAE_90D_pct": -28.15, "MAE_180D_pct": -28.15, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-02", "peak_price": 2630.0, "drawdown_after_peak_pct": -31.29, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing_aluminum_policy_spread_event_cap", "four_b_evidence_type": ["aluminum_policy_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_aluminum_policy_material_spread_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_aluminum_policy_spread_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA_candidates", "same_entry_group_id": "R4L96_C15_008350_2024-01-02_2515", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L96_C15_POSCOSTEELION_2024_COATED_STEEL_SPREAD_MARGIN_POSITIVE", "trigger_id": "R4L96_C15_POSCOSTEELION_2024_STAGE2_ACTIONABLE_COATED_STEEL_SPREAD_MARGIN_BRIDGE", "symbol": "058430", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 55, "customer_quality_score": 35, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 64, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 45, "margin_bridge_score": 55, "revision_score": 50, "relative_strength_score": 55, "customer_quality_score": 45, "policy_or_regulatory_score": 20, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "coated_steel_spread_margin_positive", "MFE_90D_pct": 12.57, "MAE_90D_pct": -12.78, "score_return_alignment_label": "coated_steel_spread_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L96_C15_HWANGGEUMST_2024_STAINLESS_NICKEL_SPREAD_FALSE_STAGE2", "trigger_id": "R4L96_C15_HWANGGEUMST_2024_STAGE2_FALSE_POSITIVE_STAINLESS_NICKEL_SPREAD_WATCH", "symbol": "032560", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 25, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 75, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "stainless_nickel_false_stage2", "MFE_90D_pct": 2.32, "MAE_90D_pct": -10.5, "score_return_alignment_label": "stainless_nickel_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_stainless_nickel_spread_watch_counts_without_shipment_inventory_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L96_C15_NAMSEONALUMINUM_2024_ALUMINUM_POLICY_SPREAD_EVENT_CAP_4B", "trigger_id": "R4L96_C15_NAMSEONALUMINUM_2024_STAGE4B_ALUMINUM_POLICY_SPREAD_EVENT_CAP", "symbol": "008350", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 15, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 35, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "aluminum_policy_event_cap_4B_guard", "MFE_90D_pct": 4.57, "MAE_90D_pct": -28.15, "score_return_alignment_label": "aluminum_policy_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_aluminum_policy_spread_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "96", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COATED_STEEL_SPREAD_MARGIN_BRIDGE_VS_STAINLESS_NICKEL_FALSE_STAGE2_AND_ALUMINUM_POLICY_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["coated_steel_spread_margin_positive", "stainless_nickel_false_stage2", "aluminum_policy_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C15 rows need explicit realized product spread, inventory discipline, shipment mix, ASP/pass-through, margin or revision bridge before positive promotion.
- In C15, policy/event-premium rows with low MFE/high MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C15 material-spread rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R4
completed_loop = 96
next_round = R5
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
