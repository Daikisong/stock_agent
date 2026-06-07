# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = SYNTHETIC_RUBBER_PETROCHEM_SPREAD_MARGIN_BRIDGE_VS_BASE_CHEMICAL_RECOVERY_FALSE_STAGE2_AND_BATTERY_CHEMICAL_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | chemical_spread_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R4_loop_98_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. After local C08/C09/C01/C07/C06/C10/C14/C11/C02/C13/C19/C27/C12/C24/C28 supplementation, C17 is the next unsupplemented Priority 0 archetype. Prior C17 symbols 001340 / 010060 / 006890 are avoided.

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
chemical_spread_margin_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R4
scheduled_loop = 98
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C17 is a chemical commodity spread archetype. The commodity quote is the weather report; the usable signal is whether product spread, volume, inventory, pass-through, FCF/margin and revision actually reach the company’s income statement.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD = 29 rows / Priority 0
previous C17 symbols avoided: 001340, 010060, 006890
recent local C08/C09/C01/C07/C06/C10/C14/C11/C02/C13/C19/C27/C12/C24/C28 artifacts accounted for but not duplicated
```

Selected rows avoid hard duplicates and add new C17 trigger families:

```text
011780 / Stage2-Actionable / 2024-01-24
011170 / Stage2-Actionable / 2024-01-25
161000 / Stage4B / 2024-01-02
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
| 011780 | atlas/symbol_profiles/011/011780.json | selected 2024 window clean after old 2001 CA candidate |
| 011170 | atlas/symbol_profiles/011/011170.json | selected 2024 window clean after old 2023 CA candidate |
| 161000 | atlas/symbol_profiles/161/161000.json | selected 2024 window clean after old 2016/2021 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R4L98_C17_KUMHOPETRO_2024_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE_POSITIVE | 011780 | 2024-01-24 | yes | 180 | yes | yes | true |
| R4L98_C17_LOTTECHEM_2024_BASE_CHEMICAL_RECOVERY_FALSE_STAGE2 | 011170 | 2024-01-25 | yes | 180 | yes | yes | true |
| R4L98_C17_AEKYUNGCHEM_2024_BATTERY_CHEMICAL_EVENT_CAP_4B | 161000 | 2024-01-02 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | SYNTHETIC_RUBBER_PETROCHEM_SPREAD_MARGIN_BRIDGE | Positive Stage2 requires realized product spread, volume recovery, inventory turn, cost pass-through, FCF/margin and revision bridge. |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | BASE_CHEMICAL_RECOVERY_FALSE_STAGE2 | Base-chemical rebound without realized spread and margin bridge can become false Stage2. |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | BATTERY_CHEMICAL_EVENT_CAP_4B | Battery/specialty chemical event premium should route to 4B when spread-margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R4L98_C17_KUMHOPETRO_2024_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE_POSITIVE | 011780 | 금호석유화학 | positive | Product-spread and margin bridge produced strong MFE with shallow early MAE. |
| R4L98_C17_LOTTECHEM_2024_BASE_CHEMICAL_RECOVERY_FALSE_STAGE2 | 011170 | 롯데케미칼 | counterexample | Base-chemical recovery watch had tiny MFE and severe MAE without realized spread/margin bridge. |
| R4L98_C17_AEKYUNGCHEM_2024_BATTERY_CHEMICAL_EVENT_CAP_4B | 161000 | 애경케미칼 | counterexample / 4B | Chemical/battery-theme premium capped near the early-January high and later de-rated deeply. |

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
| Kumho Petrochemical synthetic-rubber spread/margin bridge | historical public/report proxy | true | true | shadow-only positive |
| Lotte Chemical base-chemical recovery false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Aekyung Chemical battery/specialty-chemical event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 011780 | atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv | atlas/symbol_profiles/011/011780.json |
| 011170 | atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv | atlas/symbol_profiles/011/011170.json |
| 161000 | atlas/ohlcv_tradable_by_symbol_year/161/161000/2024.csv | atlas/symbol_profiles/161/161000.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R4L98_C17_KUMHOPETRO_2024_STAGE2_ACTIONABLE_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE | 011780 | Stage2-Actionable | 2024-01-24 | 112500 | positive | product-spread margin bridge worked |
| R4L98_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_BASE_CHEMICAL_SPREAD_RECOVERY_WATCH | 011170 | Stage2-Actionable | 2024-01-25 | 136900 | counterexample | base-chemical spread false Stage2 |
| R4L98_C17_AEKYUNGCHEM_2024_STAGE4B_BATTERY_CHEMICAL_SPREAD_EVENT_CAP | 161000 | Stage4B | 2024-01-02 | 16740 | counterexample/4B | battery/specialty chemical event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R4L98_C17_KUMHOPETRO_2024_STAGE2_ACTIONABLE_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE | 112500 | 45.69 | -2.13 | 45.69 | -2.13 | 48.44 | -2.13 | 2024-07-15 | 167000 | -27.72 |
| R4L98_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_BASE_CHEMICAL_SPREAD_RECOVERY_WATCH | 136900 | 2.85 | -12.93 | 2.85 | -29.80 | 2.85 | -42.00 | 2024-02-01 | 140800 | -43.61 |
| R4L98_C17_AEKYUNGCHEM_2024_STAGE4B_BATTERY_CHEMICAL_SPREAD_EVENT_CAP | 16740 | 2.21 | -28.32 | 2.21 | -31.36 | 2.21 | -46.83 | 2024-01-03 | 17110 | -47.98 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C17 Stage2 needs realized product spread / volume / inventory / pass-through / FCF-margin / revision bridge |
| chemical_spread_margin_guardrail | strengthen: commodity spread label alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing base-chemical and battery-chemical premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C17 rows cannot promote without durable realized margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether chemical spread narrative becomes realized product spread and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 011780 | good_stage2_with_later_watch | Product spread and margin bridge produced strong MFE with shallow MAE, but later spread/valuation watch remains necessary. |
| 011170 | bad_stage2 | Base-chemical recovery watch lacked realized spread/margin bridge and suffered severe MAE. |
| 161000 | good_4B | Battery/specialty-chemical event premium peaked immediately and later de-rated deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 011170 base chemical false Stage2 | 0.97 | 0.97 | false Stage2 due missing realized spread / volume / inventory / margin bridge |
| 161000 battery chemical event cap | 0.98 | 0.98 | good full-window 4B timing after battery/specialty-chemical event premium |
| 011780 synthetic-rubber spread bridge | n/a | n/a | positive Stage2, but later chemical-spread valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 011170 / 161000
```

No hard 4C candidate is introduced in this C17 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L4 chemical commodity margin-spread cases, Stage2 requires verified realized product spread, volume recovery, inventory turn, cost pass-through, FCF/margin and revision bridge. Commodity spread, naphtha spread, base chemical rebound, battery chemical, specialty chemical or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
rule = C17 should split true realized product-spread/margin positives from base-chemical false Stage2 and battery/specialty-chemical event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 16.92 | -21.10 | 0.67 | mixed; C17 realized-spread bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 16.92 | -21.10 | 0.67 | weaker C17 bridge split |
| P1 sector_specific_candidate_profile | L4 realized-spread/margin bridge required | 2 | 24.27 | -15.97 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C17 bridge vs event-cap split | 2 | 24.27 | -15.97 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing chemical-spread themes as positive | 1 | 45.69 | -2.13 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 011780 product-spread bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 45.69 | -2.13 | chemical_spread_margin_positive |
| 011170 base chemical false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 2.85 | -29.80 | base_chemical_false_stage2 |
| 161000 battery chemical cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 2.21 | -31.36 | battery_chemical_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SYNTHETIC_RUBBER_PETROCHEM_SPREAD_MARGIN_BRIDGE_VS_BASE_CHEMICAL_RECOVERY_FALSE_STAGE2_AND_BATTERY_CHEMICAL_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C17 is the next unsupplemented Priority 0 archetype after local C08/C09/C01/C07/C06/C10/C14/C11/C02/C13/C19/C27/C12/C24/C28 supplementation. This run adds Kumho Petrochemical, Lotte Chemical, and Aekyung Chemical while avoiding prior C17 symbols 001340, 010060 and 006890."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, chemical_spread_margin_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: chemical_spread_margin_positive, base_chemical_false_stage2, battery_chemical_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, chemical_spread_margin_guardrail, high_MAE_guardrail
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
shadow_weight,stage2_required_bridge,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,configured,C17_requires_realized_product_spread_volume_inventory_FCF_margin_revision_bridge,0,"C17 Stage2 should require realized product spread, volume recovery, inventory turn, cost pass-through, FCF/margin and revision bridge, not chemical commodity spread label alone","Kumho Petrochemical positive worked; Lotte Chemical and Aekyung Chemical event/watch rows failed positive-stage promotion","R4L98_C17_KUMHOPETRO_2024_STAGE2_ACTIONABLE_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE|R4L98_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_BASE_CHEMICAL_SPREAD_RECOVERY_WATCH|R4L98_C17_AEKYUNGCHEM_2024_STAGE4B_BATTERY_CHEMICAL_SPREAD_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,configured,cap_bridge_missing_base_chemical_and_battery_chemical_event_premiums_as_4B_watch,0,"Base chemical and battery-chemical premiums can peak before realized spread, volume, inventory and margin bridge is proven","Lotte Chemical had tiny MFE and severe MAE after late-January recovery; Aekyung Chemical showed 4B event-cap behavior after early-January chemical/battery spread premium","R4L98_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_BASE_CHEMICAL_SPREAD_RECOVERY_WATCH|R4L98_C17_AEKYUNGCHEM_2024_STAGE4B_BATTERY_CHEMICAL_SPREAD_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,configured,block_positive_stage_when_chemical_spread_theme_has_high_or_persistent_MAE_without_realized_margin_bridge,0,"High or persistent MAE after bridge-missing C17 entries should block Stage2/Stage3 promotion unless product spread, inventory turn and margin evidence survives","Lotte Chemical MAE180=-42.00 and Aekyung Chemical MAE180=-46.83","R4L98_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_BASE_CHEMICAL_SPREAD_RECOVERY_WATCH|R4L98_C17_AEKYUNGCHEM_2024_STAGE4B_BATTERY_CHEMICAL_SPREAD_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L98_C17_KUMHOPETRO_2024_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE_POSITIVE", "symbol": "011780", "company_name": "금호석유화학", "round": "R4", "loop": "98", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SYNTHETIC_RUBBER_PETROCHEM_SPREAD_MARGIN_BRIDGE_VS_BASE_CHEMICAL_RECOVERY_FALSE_STAGE2_AND_BATTERY_CHEMICAL_EVENT_CAP", "case_type": "structural_success_with_later_chemical_spread_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R4L98_C17_KUMHOPETRO_2024_STAGE2_ACTIONABLE_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Synthetic-rubber / petrochemical spread and margin bridge produced strong 30D/90D/180D MFE with shallow early MAE after the January trough. C17 works when commodity spread is tied to actual product spread, volume, inventory discipline, cost pass-through, FCF/margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C17_positive_requires_product_spread_volume_inventory_FCF_margin_revision_bridge_not_commodity_spread_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2001 corporate-action candidate. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R4L98_C17_LOTTECHEM_2024_BASE_CHEMICAL_RECOVERY_FALSE_STAGE2", "symbol": "011170", "company_name": "롯데케미칼", "round": "R4", "loop": "98", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SYNTHETIC_RUBBER_PETROCHEM_SPREAD_MARGIN_BRIDGE_VS_BASE_CHEMICAL_RECOVERY_FALSE_STAGE2_AND_BATTERY_CHEMICAL_EVENT_CAP", "case_type": "failed_rerating_base_chemical_spread_recovery_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R4L98_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_BASE_CHEMICAL_SPREAD_RECOVERY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Base-chemical / naphtha-spread recovery watch after the late-January rebound had tiny MFE and then severe MAE. C17 Stage2 should not be awarded without realized product spread, volume recovery, inventory turn, cost pass-through, FCF/margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_base_chemical_recovery_watch_counts_without_realized_spread_volume_inventory_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2023 corporate-action candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R4L98_C17_AEKYUNGCHEM_2024_BATTERY_CHEMICAL_EVENT_CAP_4B", "symbol": "161000", "company_name": "애경케미칼", "round": "R4", "loop": "98", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SYNTHETIC_RUBBER_PETROCHEM_SPREAD_MARGIN_BRIDGE_VS_BASE_CHEMICAL_RECOVERY_FALSE_STAGE2_AND_BATTERY_CHEMICAL_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L98_C17_AEKYUNGCHEM_2024_STAGE4B_BATTERY_CHEMICAL_SPREAD_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Battery-chemical / specialty-chemical event premium capped near the early-January high and then de-rated deeply. C17 should route bridge-missing chemical theme premiums to 4B unless product spread, volume, inventory, ASP/cost pass-through, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_battery_chemical_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2016/2021 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L98_C17_KUMHOPETRO_2024_STAGE2_ACTIONABLE_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE", "case_id": "R4L98_C17_KUMHOPETRO_2024_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE_POSITIVE", "symbol": "011780", "company_name": "금호석유화학", "round": "R4", "loop": "98", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SYNTHETIC_RUBBER_PETROCHEM_SPREAD_MARGIN_BRIDGE_VS_BASE_CHEMICAL_RECOVERY_FALSE_STAGE2_AND_BATTERY_CHEMICAL_EVENT_CAP", "sector": "synthetic_rubber_petrochemical_product_spread_margin", "primary_archetype": "product_spread_volume_inventory_FCF_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | chemical_spread_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 112500.0, "evidence_available_at_that_date": "synthetic-rubber / petrochemical product spread, inventory discipline, cost pass-through and margin/FCF revision bridge proxy after January trough; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["product_spread_proxy", "volume_recovery_proxy", "inventory_discipline_proxy", "cost_pass_through_proxy", "FCF_margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "strong_MFE180", "shallow_initial_MAE"], "stage4b_evidence_fields": ["later_chemical_spread_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 45.69, "MFE_90D_pct": 45.69, "MFE_180D_pct": 48.44, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -2.13, "MAE_90D_pct": -2.13, "MAE_180D_pct": -2.13, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-15", "peak_price": 167000.0, "drawdown_after_peak_pct": -27.72, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_chemical_spread_valuation_4B_watch_needed", "four_b_evidence_type": ["product_spread_margin_bridge", "inventory_FCF", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_synthetic_rubber_spread_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2001_CA", "same_entry_group_id": "R4L98_C17_011780_2024-01-24_112500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L98_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_BASE_CHEMICAL_SPREAD_RECOVERY_WATCH", "case_id": "R4L98_C17_LOTTECHEM_2024_BASE_CHEMICAL_RECOVERY_FALSE_STAGE2", "symbol": "011170", "company_name": "롯데케미칼", "round": "R4", "loop": "98", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SYNTHETIC_RUBBER_PETROCHEM_SPREAD_MARGIN_BRIDGE_VS_BASE_CHEMICAL_RECOVERY_FALSE_STAGE2_AND_BATTERY_CHEMICAL_EVENT_CAP", "sector": "base_chemical_naphtha_spread_recovery_watch", "primary_archetype": "base_chemical_recovery_watch_without_realized_spread_volume_inventory_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | chemical_spread_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-25", "entry_date": "2024-01-25", "entry_price": 136900.0, "evidence_available_at_that_date": "base chemical / naphtha-spread recovery watch after late-January rebound without confirmed realized spread, volume recovery, inventory turn, cost pass-through, FCF or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["base_chemical_recovery_watch", "commodity_spread_beta", "relative_strength_rebound"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["tiny_MFE90", "high_MAE90", "realized_spread_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv", "profile_path": "atlas/symbol_profiles/011/011170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.85, "MFE_90D_pct": 2.85, "MFE_180D_pct": 2.85, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -12.93, "MAE_90D_pct": -29.8, "MAE_180D_pct": -42.0, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-01", "peak_price": 140800.0, "drawdown_after_peak_pct": -43.61, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "base_chemical_recovery_watch_was_false_stage2_due_missing_realized_spread_volume_inventory_margin_revision_bridge", "four_b_evidence_type": ["base_chemical_spread_beta", "bridge_missing", "tiny_MFE_high_MAE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_base_chemical_spread_recovery_without_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_base_chemical_recovery_watch_counts_without_realized_spread_volume_inventory_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2023_CA", "same_entry_group_id": "R4L98_C17_011170_2024-01-25_136900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L98_C17_AEKYUNGCHEM_2024_STAGE4B_BATTERY_CHEMICAL_SPREAD_EVENT_CAP", "case_id": "R4L98_C17_AEKYUNGCHEM_2024_BATTERY_CHEMICAL_EVENT_CAP_4B", "symbol": "161000", "company_name": "애경케미칼", "round": "R4", "loop": "98", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SYNTHETIC_RUBBER_PETROCHEM_SPREAD_MARGIN_BRIDGE_VS_BASE_CHEMICAL_RECOVERY_FALSE_STAGE2_AND_BATTERY_CHEMICAL_EVENT_CAP", "sector": "battery_chemical_specialty_chemical_event_premium", "primary_archetype": "battery_chemical_spread_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | chemical_spread_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-02", "entry_date": "2024-01-02", "entry_price": 16740.0, "evidence_available_at_that_date": "battery-chemical / specialty-chemical spread event premium without confirmed product spread, volume, inventory normalization, ASP/cost pass-through, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["battery_chemical_event", "specialty_chemical_spread_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE180", "spread_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/161/161000/2024.csv", "profile_path": "atlas/symbol_profiles/161/161000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.21, "MFE_90D_pct": 2.21, "MFE_180D_pct": 2.21, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -28.32, "MAE_90D_pct": -31.36, "MAE_180D_pct": -46.83, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-03", "peak_price": 17110.0, "drawdown_after_peak_pct": -47.98, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing_battery_chemical_event_cap_due_missing_product_spread_margin_bridge", "four_b_evidence_type": ["battery_chemical_event_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_battery_chemical_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_battery_chemical_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2016_2021_CA", "same_entry_group_id": "R4L98_C17_161000_2024-01-02_16740", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R4L98_C17_KUMHOPETRO_2024_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R4L98_C17_KUMHOPETRO_2024_STAGE2_ACTIONABLE_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE", "symbol": "011780", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 55, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 45, "margin_bridge_score": 65, "revision_score": 60, "relative_strength_score": 75, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "synthetic_rubber_product_spread_margin_positive", "MFE_90D_pct": 45.69, "MAE_90D_pct": -2.13, "score_return_alignment_label": "chemical_spread_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R4L98_C17_LOTTECHEM_2024_BASE_CHEMICAL_RECOVERY_FALSE_STAGE2", "trigger_id": "R4L98_C17_LOTTECHEM_2024_STAGE2_FALSE_POSITIVE_BASE_CHEMICAL_SPREAD_RECOVERY_WATCH", "symbol": "011170", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 60, "customer_quality_score": 25, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "base_chemical_spread_false_stage2", "MFE_90D_pct": 2.85, "MAE_90D_pct": -29.8, "score_return_alignment_label": "base_chemical_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_base_chemical_recovery_watch_counts_without_realized_spread_volume_inventory_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R4L98_C17_AEKYUNGCHEM_2024_BATTERY_CHEMICAL_EVENT_CAP_4B", "trigger_id": "R4L98_C17_AEKYUNGCHEM_2024_STAGE4B_BATTERY_CHEMICAL_SPREAD_EVENT_CAP", "symbol": "161000", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "battery_chemical_event_cap_4B_guard", "MFE_90D_pct": 2.21, "MAE_90D_pct": -31.36, "score_return_alignment_label": "battery_chemical_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_battery_chemical_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "98", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SYNTHETIC_RUBBER_PETROCHEM_SPREAD_MARGIN_BRIDGE_VS_BASE_CHEMICAL_RECOVERY_FALSE_STAGE2_AND_BATTERY_CHEMICAL_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "chemical_spread_margin_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["chemical_spread_margin_positive", "base_chemical_false_stage2", "battery_chemical_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C17 rows need explicit realized product spread, volume recovery, inventory turn, cost pass-through, FCF/margin and revision bridge before positive promotion.
- In C17, bridge-missing chemical commodity spread event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C17 chemical commodity margin-spread rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R4
completed_loop = 98
completed_canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
coverage_scheduler_status = coverage_index_first
next_selection_rule = re-read V12_Research_No_Repeat_Index.md Priority 0 and local supplements
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
