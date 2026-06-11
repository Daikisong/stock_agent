# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R3
scheduled_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE_VS_CELLMAKER_ORDERBOOK_FALSE_STAGE2_AND_CNT_MATERIAL_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | battery_orderbook_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R3_loop_98_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. After local C08/C09/C01/C07/C06/C10/C14 supplementation, C11 is the next unsupplemented Priority 0 archetype. Prior C11 symbols 006110 / 079810 / 417010 and the immediately preceding C14 symbols are avoided.

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
battery_orderbook_margin_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R3
scheduled_loop = 98
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C11 is an orderbook-to-margin conversion archetype. Order backlog is only the warehouse ledger; the signal becomes investable only when delivery, customer quality, working capital, FCF, margin and revision unlock the cash drawer.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C11_BATTERY_ORDERBOOK_RERATING = 23 rows / Priority 0
previous C11 symbols avoided: 006110, 079810, 417010
recent local C08/C09/C01/C07/C06/C10/C14 artifacts accounted for but not duplicated
```

Selected rows avoid hard duplicates and add new C11 trigger families:

```text
137400 / Stage2-Actionable / 2024-02-21
006400 / Stage2-Actionable / 2024-03-25
121600 / Stage4B / 2024-02-22
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
| 137400 | atlas/symbol_profiles/137/137400.json | selected 2024 window clean after old 2012/2019 CA candidates |
| 006400 | atlas/symbol_profiles/006/006400.json | selected 2024 window clean after old 1996/1998/2014 CA candidates |
| 121600 | atlas/symbol_profiles/121/121600.json | selected 2024 window clean after old 2015 CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R3L98_C11_PNT_2024_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE_POSITIVE | 137400 | 2024-02-21 | yes | 180 | yes | yes | true |
| R3L98_C11_SAMSUNGSDI_2024_CELLMAKER_ORDERBOOK_FALSE_STAGE2 | 006400 | 2024-03-25 | yes | 180 | yes | yes | true |
| R3L98_C11_NANOCHEM_2024_CNT_MATERIAL_ORDERBOOK_EVENT_CAP_4B | 121600 | 2024-02-22 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C11_BATTERY_ORDERBOOK_RERATING | BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE | Positive Stage2 requires orderbook conversion, delivery schedule, customer quality, FCF/margin and revision bridge. |
| C11_BATTERY_ORDERBOOK_RERATING | CELLMAKER_ORDERBOOK_FALSE_STAGE2 | Cell-maker orderbook/rebound watch without call-off/utilization/margin bridge can become false Stage2. |
| C11_BATTERY_ORDERBOOK_RERATING | CNT_MATERIAL_EVENT_CAP_4B | CNT/material orderbook premium should route to 4B when offtake, repeat delivery and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R3L98_C11_PNT_2024_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE_POSITIVE | 137400 | 피엔티 | positive | Battery equipment orderbook/margin bridge produced very strong 90D/180D MFE despite later valuation watch. |
| R3L98_C11_SAMSUNGSDI_2024_CELLMAKER_ORDERBOOK_FALSE_STAGE2 | 006400 | 삼성SDI | counterexample | Cell-maker orderbook recovery watch had tiny MFE and then large MAE without call-off/margin bridge. |
| R3L98_C11_NANOCHEM_2024_CNT_MATERIAL_ORDERBOOK_EVENT_CAP_4B | 121600 | 나노신소재 | counterexample / 4B | CNT/material event premium capped at the February spike and then de-rated. |

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
| PNT battery equipment orderbook/margin bridge | historical public/report proxy | true | true | shadow-only positive |
| Samsung SDI cell-maker orderbook false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Nano Chem CNT/material orderbook event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 137400 | atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv | atlas/symbol_profiles/137/137400.json |
| 006400 | atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv | atlas/symbol_profiles/006/006400.json |
| 121600 | atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv | atlas/symbol_profiles/121/121600.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R3L98_C11_PNT_2024_STAGE2_ACTIONABLE_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE | 137400 | Stage2-Actionable | 2024-02-21 | 43500 | positive | orderbook-to-margin bridge worked |
| R3L98_C11_SAMSUNGSDI_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_ORDERBOOK_CALLOFF_WATCH | 006400 | Stage2-Actionable | 2024-03-25 | 486000 | counterexample | cell-maker orderbook false Stage2 |
| R3L98_C11_NANOCHEM_2024_STAGE4B_CNT_MATERIAL_ORDERBOOK_EVENT_CAP | 121600 | Stage4B | 2024-02-22 | 138000 | counterexample/4B | CNT/material orderbook event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R3L98_C11_PNT_2024_STAGE2_ACTIONABLE_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE | 43500 | 10.80 | -8.74 | 105.75 | -16.55 | 105.75 | -16.55 | 2024-06-19 | 89500 | -39.33 |
| R3L98_C11_SAMSUNGSDI_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_ORDERBOOK_CALLOFF_WATCH | 486000 | 1.75 | -16.26 | 1.75 | -27.78 | 1.75 | -27.88 | 2024-03-25 | 494500 | -29.12 |
| R3L98_C11_NANOCHEM_2024_STAGE4B_CNT_MATERIAL_ORDERBOOK_EVENT_CAP | 138000 | 14.35 | -11.96 | 14.35 | -15.94 | 14.35 | -42.03 | 2024-02-22 | 157800 | -51.78 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C11 Stage2 needs orderbook conversion / delivery / customer quality / FCF / margin / revision bridge |
| battery_orderbook_margin_guardrail | strengthen: battery orderbook label alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing cell-maker and material orderbook premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C11 rows cannot promote without durable margin/FCF bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether battery orderbook narrative becomes delivery, FCF, margin and revision evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 137400 | good_stage2_with_later_watch | Orderbook/margin bridge produced very strong MFE, but later valuation watch remains necessary. |
| 006400 | bad_stage2 | Cell-maker orderbook rebound lacked call-off/utilization/margin bridge and produced tiny MFE. |
| 121600 | good_4B | CNT/material orderbook event premium peaked immediately and later de-rated deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 006400 cell-maker false Stage2 | 0.98 | 0.98 | false Stage2 due missing call-off / utilization / margin bridge |
| 121600 CNT material cap | 0.87 | 0.87 | good full-window 4B timing after CNT/material orderbook premium |
| 137400 battery equipment bridge | n/a | n/a | positive Stage2, but later battery-equipment valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 006400 / 121600
```

No hard 4C candidate is introduced in this C11 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 battery orderbook rerating cases, Stage2 requires verified orderbook conversion, delivery schedule, customer quality, working-capital/FCF, margin, and revision bridge. Battery orderbook, cell-maker recovery, CNT/material orderbook, equipment backlog or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
rule = C11 should split true orderbook-delivery-margin positives from cell-maker orderbook false Stage2 and material orderbook event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 40.62 | -20.09 | 0.67 | mixed; C11 bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 40.62 | -20.09 | 0.67 | weaker C11 bridge split |
| P1 sector_specific_candidate_profile | L3 orderbook-delivery-margin bridge required | 2 | 53.75 | -16.25 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C11 bridge vs event-cap split | 2 | 53.75 | -16.25 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing battery orderbook themes as positive | 1 | 105.75 | -16.55 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 137400 battery orderbook bridge | 66 | Stage2-Watch | 79 | Stage2-Actionable | 105.75 | -16.55 | battery_orderbook_margin_positive |
| 006400 cell-maker false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 1.75 | -27.78 | cellmaker_orderbook_false_stage2 |
| 121600 CNT material cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 14.35 | -15.94 | CNT_material_orderbook_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE_VS_CELLMAKER_ORDERBOOK_FALSE_STAGE2_AND_CNT_MATERIAL_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C11 is the next unsupplemented Priority 0 archetype after local C08/C09/C01/C07/C06/C10/C14 supplementation. This run adds PNT, Samsung SDI, and Nano Chem rows while avoiding prior C11 symbols 006110, 079810, 417010 and recent C14 symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, battery_orderbook_margin_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: battery_orderbook_margin_positive, cellmaker_orderbook_false_stage2, CNT_material_orderbook_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, battery_orderbook_margin_guardrail, high_MAE_guardrail
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
- C11 battery orderbook rerating bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,configured,C11_requires_orderbook_delivery_customer_margin_FCF_revision_bridge,0,"C11 Stage2 should require orderbook conversion, delivery schedule, customer quality, working-capital/FCF, margin, and revision bridge, not battery orderbook label alone","PNT positive worked; Samsung SDI and Nano Chem event/watch rows failed positive-stage promotion","R3L98_C11_PNT_2024_STAGE2_ACTIONABLE_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE|R3L98_C11_SAMSUNGSDI_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_ORDERBOOK_CALLOFF_WATCH|R3L98_C11_NANOCHEM_2024_STAGE4B_CNT_MATERIAL_ORDERBOOK_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,configured,cap_bridge_missing_cellmaker_and_material_orderbook_event_premiums_as_4B_watch,0,"Cell-maker and material-orderbook premiums can peak before call-off, delivery, inventory turn, ASP/mix and margin bridge is proven","Samsung SDI had tiny MFE and high MAE after March rebound; Nano Chem showed 4B event-cap behavior after February CNT/material spike","R3L98_C11_SAMSUNGSDI_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_ORDERBOOK_CALLOFF_WATCH|R3L98_C11_NANOCHEM_2024_STAGE4B_CNT_MATERIAL_ORDERBOOK_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,configured,block_positive_stage_when_battery_orderbook_theme_has_high_or_persistent_MAE_without_margin_FCF_bridge,0,"High or persistent MAE after bridge-missing C11 entries should block Stage2/Stage3 promotion unless orderbook conversion, delivery and margin evidence survives","Samsung SDI MAE90=-27.78 and Nano Chem MAE180=-42.03","R3L98_C11_SAMSUNGSDI_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_ORDERBOOK_CALLOFF_WATCH|R3L98_C11_NANOCHEM_2024_STAGE4B_CNT_MATERIAL_ORDERBOOK_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R3L98_C11_PNT_2024_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE_POSITIVE", "symbol": "137400", "company_name": "피엔티", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE_VS_CELLMAKER_ORDERBOOK_FALSE_STAGE2_AND_CNT_MATERIAL_EVENT_CAP", "case_type": "structural_success_with_later_battery_equipment_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R3L98_C11_PNT_2024_STAGE2_ACTIONABLE_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Battery equipment orderbook / delivery / margin bridge produced very strong 90D/180D MFE after the February equipment-recovery base. C11 works when orderbook is connected to delivery schedule, customer quality, working-capital control, margin conversion and revision, not merely battery equipment beta.", "current_profile_verdict": "current_profile_kept_but_C11_positive_requires_orderbook_delivery_customer_margin_FCF_revision_bridge_not_orderbook_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2012/2019 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R3L98_C11_SAMSUNGSDI_2024_CELLMAKER_ORDERBOOK_FALSE_STAGE2", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE_VS_CELLMAKER_ORDERBOOK_FALSE_STAGE2_AND_CNT_MATERIAL_EVENT_CAP", "case_type": "failed_rerating_cellmaker_orderbook_calloff_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R3L98_C11_SAMSUNGSDI_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_ORDERBOOK_CALLOFF_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Cell-maker orderbook / battery recovery watch after the March rebound had tiny forward MFE and then large MAE. C11 Stage2 should not be awarded without customer call-off, utilization, ASP/mix, inventory normalization, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_cellmaker_orderbook_watch_counts_without_calloff_utilization_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1996/1998/2014 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R3L98_C11_NANOCHEM_2024_CNT_MATERIAL_ORDERBOOK_EVENT_CAP_4B", "symbol": "121600", "company_name": "나노신소재", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE_VS_CELLMAKER_ORDERBOOK_FALSE_STAGE2_AND_CNT_MATERIAL_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R3L98_C11_NANOCHEM_2024_STAGE4B_CNT_MATERIAL_ORDERBOOK_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "CNT / conductive additive / battery-material orderbook event premium capped during the February spike and then de-rated. C11 should route bridge-missing material orderbook premiums to 4B unless customer offtake, repeat delivery, inventory turn, ASP/mix, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_CNT_material_orderbook_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2015 corporate-action candidate. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R3L98_C11_PNT_2024_STAGE2_ACTIONABLE_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE", "case_id": "R3L98_C11_PNT_2024_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE_POSITIVE", "symbol": "137400", "company_name": "피엔티", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE_VS_CELLMAKER_ORDERBOOK_FALSE_STAGE2_AND_CNT_MATERIAL_EVENT_CAP", "sector": "battery_equipment_orderbook_delivery_margin_FCF", "primary_archetype": "orderbook_delivery_customer_margin_FCF_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | battery_orderbook_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-21", "entry_date": "2024-02-21", "entry_price": 43500.0, "evidence_available_at_that_date": "battery equipment orderbook, delivery schedule, customer quality, working-capital control and margin/revision bridge proxy after February equipment-recovery base; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["orderbook_proxy", "delivery_schedule_proxy", "customer_quality_proxy", "working_capital_FCF_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "very_strong_MFE90", "very_strong_MFE180"], "stage4b_evidence_fields": ["later_battery_equipment_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv", "profile_path": "atlas/symbol_profiles/137/137400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.8, "MFE_90D_pct": 105.75, "MFE_180D_pct": 105.75, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -8.74, "MAE_90D_pct": -16.55, "MAE_180D_pct": -16.55, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 89500.0, "drawdown_after_peak_pct": -39.33, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_battery_equipment_valuation_4B_watch_needed", "four_b_evidence_type": ["battery_equipment_orderbook_bridge", "delivery_margin_FCF", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_battery_equipment_orderbook_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2012_2019_CA", "same_entry_group_id": "R3L98_C11_137400_2024-02-21_43500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L98_C11_SAMSUNGSDI_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_ORDERBOOK_CALLOFF_WATCH", "case_id": "R3L98_C11_SAMSUNGSDI_2024_CELLMAKER_ORDERBOOK_FALSE_STAGE2", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE_VS_CELLMAKER_ORDERBOOK_FALSE_STAGE2_AND_CNT_MATERIAL_EVENT_CAP", "sector": "cellmaker_orderbook_calloff_utilization_watch", "primary_archetype": "cellmaker_orderbook_watch_without_calloff_utilization_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | battery_orderbook_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-25", "entry_date": "2024-03-25", "entry_price": 486000.0, "evidence_available_at_that_date": "cell-maker orderbook / EV recovery watch without confirmed customer call-off, utilization, ASP/mix, inventory normalization or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["cellmaker_orderbook_watch", "EV_recovery_theme", "relative_strength_rebound"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["tiny_MFE90", "high_MAE90", "calloff_utilization_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv", "profile_path": "atlas/symbol_profiles/006/006400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.75, "MFE_90D_pct": 1.75, "MFE_180D_pct": 1.75, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -16.26, "MAE_90D_pct": -27.78, "MAE_180D_pct": -27.88, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-25", "peak_price": 494500.0, "drawdown_after_peak_pct": -29.12, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "cellmaker_orderbook_watch_was_false_stage2_due_missing_calloff_utilization_margin_revision_bridge", "four_b_evidence_type": ["cellmaker_orderbook_rebound", "bridge_missing", "tiny_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_cellmaker_orderbook_watch_without_calloff_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_cellmaker_orderbook_watch_counts_without_calloff_utilization_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1996_1998_2014_CA", "same_entry_group_id": "R3L98_C11_006400_2024-03-25_486000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L98_C11_NANOCHEM_2024_STAGE4B_CNT_MATERIAL_ORDERBOOK_EVENT_CAP", "case_id": "R3L98_C11_NANOCHEM_2024_CNT_MATERIAL_ORDERBOOK_EVENT_CAP_4B", "symbol": "121600", "company_name": "나노신소재", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE_VS_CELLMAKER_ORDERBOOK_FALSE_STAGE2_AND_CNT_MATERIAL_EVENT_CAP", "sector": "CNT_conductive_additive_battery_material_orderbook_event_premium", "primary_archetype": "CNT_material_orderbook_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | battery_orderbook_margin_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-22", "entry_date": "2024-02-22", "entry_price": 138000.0, "evidence_available_at_that_date": "CNT/conductive-additive battery-material orderbook event premium without confirmed offtake, repeat delivery, inventory turn, ASP/mix, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["CNT_material_event", "battery_orderbook_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_post_peak_drawdown", "offtake_inventory_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv", "profile_path": "atlas/symbol_profiles/121/121600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.35, "MFE_90D_pct": 14.35, "MFE_180D_pct": 14.35, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -11.96, "MAE_90D_pct": -15.94, "MAE_180D_pct": -42.03, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-22", "peak_price": 157800.0, "drawdown_after_peak_pct": -51.78, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.87, "four_b_full_window_peak_proximity": 0.87, "four_b_timing_verdict": "good_full_window_4B_timing_CNT_material_orderbook_event_cap_due_missing_offtake_inventory_margin_bridge", "four_b_evidence_type": ["CNT_material_event_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_CNT_material_orderbook_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_CNT_material_orderbook_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2015_CA", "same_entry_group_id": "R3L98_C11_121600_2024-02-22_138000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R3L98_C11_PNT_2024_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R3L98_C11_PNT_2024_STAGE2_ACTIONABLE_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE", "symbol": "137400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 45, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 65, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 80, "customer_quality_score": 60, "policy_or_regulatory_score": 25, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "battery_equipment_orderbook_margin_positive", "MFE_90D_pct": 105.75, "MAE_90D_pct": -16.55, "score_return_alignment_label": "battery_orderbook_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R3L98_C11_SAMSUNGSDI_2024_CELLMAKER_ORDERBOOK_FALSE_STAGE2", "trigger_id": "R3L98_C11_SAMSUNGSDI_2024_STAGE2_FALSE_POSITIVE_CELLMAKER_ORDERBOOK_CALLOFF_WATCH", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "cellmaker_orderbook_false_stage2", "MFE_90D_pct": 1.75, "MAE_90D_pct": -27.78, "score_return_alignment_label": "cellmaker_orderbook_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_cellmaker_orderbook_watch_counts_without_calloff_utilization_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R3L98_C11_NANOCHEM_2024_CNT_MATERIAL_ORDERBOOK_EVENT_CAP_4B", "trigger_id": "R3L98_C11_NANOCHEM_2024_STAGE4B_CNT_MATERIAL_ORDERBOOK_EVENT_CAP", "symbol": "121600", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 25, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "CNT_material_orderbook_event_cap_4B_guard", "MFE_90D_pct": 14.35, "MAE_90D_pct": -15.94, "score_return_alignment_label": "CNT_material_orderbook_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_CNT_material_orderbook_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE_VS_CELLMAKER_ORDERBOOK_FALSE_STAGE2_AND_CNT_MATERIAL_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "battery_orderbook_margin_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["battery_orderbook_margin_positive", "cellmaker_orderbook_false_stage2", "CNT_material_orderbook_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C11 rows need explicit orderbook conversion, delivery schedule, customer quality, working-capital/FCF, margin and revision bridge before positive promotion.
- In C11, bridge-missing battery orderbook event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C11 battery orderbook rerating rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R3
completed_loop = 98
completed_canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
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
