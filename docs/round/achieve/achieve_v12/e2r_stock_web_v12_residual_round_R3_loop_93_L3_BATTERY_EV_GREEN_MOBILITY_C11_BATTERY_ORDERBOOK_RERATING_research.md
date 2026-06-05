# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R3
scheduled_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = ELECTROLYTE_ADDITIVE_CUSTOMER_ORDERBOOK_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_POUCH_FILM_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R3_loop_93_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
```

This file is the corrected final output for this execution. The scheduler state after R2 loop 93 is R3 / loop 93. It fills C11 battery orderbook rerating behavior after the prior R3 loop 92 used C13, loop 91 used C14, and loop 90 used C12.

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
scheduled_round = R3
scheduled_loop = 93
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
round_sector_consistency = pass
computed_next_round = R4
computed_next_loop = 93
```

R3 permits L3 battery / EV / green mobility research. This loop avoids the previous R3 C12/C13/C14 symbol sets and returns to C11 with a fresh orderbook rerating split.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C11_BATTERY_ORDERBOOK_RERATING = 21 rows / 14 symbols / good-bad Stage2 8-4 / 4B-4C 1-0
top covered symbols include 137400(4), 299030(3), 003670(2), 302430(2), 001570(1), 005070(1)
previous R3 loop-88 C14 symbols avoided: 361610, 051910, 011790
previous R3 loop-90 C12 symbols avoided: 002710, 290670, 396300
previous R3 loop-91 C14 symbols avoided: 066970, 089980, 336370
previous R3 loop-92 C13 symbols avoided: 006400, 373220, 393890
previous R2 loop-93 C10 symbols avoided: 003160, 036540, 031980
```

Selected rows avoid hard duplicates and top repeated C11 symbols:

```text
317330 / Stage2-Actionable / 2024-02-14
382840 / Stage2-Actionable / 2024-02-21
008730 / Stage4B / 2024-02-16
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
| 317330 | atlas/symbol_profiles/317/317330.json | no corporate-action candidate |
| 382840 | atlas/symbol_profiles/382/382840.json | selected 2024 window clean after old 2022 CA candidates |
| 008730 | atlas/symbol_profiles/008/008730.json | selected 2024 window clean after old 1999 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R3L93_C11_DUKSAN_2024_ELECTROLYTE_ADDITIVE_CUSTOMER_ORDERBOOK_POSITIVE | 317330 | 2024-02-14 | yes | 180 | yes | yes | true |
| R3L93_C11_WONJUN_2024_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_STAGE2 | 382840 | 2024-02-21 | yes | 180 | yes | yes | true |
| R3L93_C11_YULCHONCHEM_2024_POUCH_FILM_ORDERBOOK_EVENT_CAP_4B | 008730 | 2024-02-16 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C11_BATTERY_ORDERBOOK_RERATING | ELECTROLYTE_ADDITIVE_CUSTOMER_ORDERBOOK_BRIDGE | Positive Stage2 requires customer qualification, orderbook visibility, capacity ramp, call-off durability, margin and revision bridge. |
| C11_BATTERY_ORDERBOOK_RERATING | BATTERY_EQUIPMENT_FALSE_STAGE2 | Battery equipment orderbook label without customer delivery/margin bridge can become false Stage2. |
| C11_BATTERY_ORDERBOOK_RERATING | POUCH_FILM_EVENT_CAP_4B | Battery-material orderbook premium should route to 4B when customer call-off and margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R3L93_C11_DUKSAN_2024_ELECTROLYTE_ADDITIVE_CUSTOMER_ORDERBOOK_POSITIVE | 317330 | 덕산테코피아 | positive | Electrolyte/additive customer-orderbook bridge produced very high MFE with controlled initial MAE. |
| R3L93_C11_WONJUN_2024_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_STAGE2 | 382840 | 원준 | counterexample | Battery-equipment orderbook watch had low MFE and deep later MAE. |
| R3L93_C11_YULCHONCHEM_2024_POUCH_FILM_ORDERBOOK_EVENT_CAP_4B | 008730 | 율촌화학 | counterexample / 4B | Pouch-film orderbook event premium capped at February spike and then de-rated severely. |

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
| Duksan Techopia electrolyte/additive orderbook bridge | historical public/report proxy | true | true | shadow-only positive |
| Wonjun battery-equipment false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Yulchon Chemical pouch-film orderbook event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 317330 | atlas/ohlcv_tradable_by_symbol_year/317/317330/2024.csv | atlas/symbol_profiles/317/317330.json |
| 382840 | atlas/ohlcv_tradable_by_symbol_year/382/382840/2024.csv | atlas/symbol_profiles/382/382840.json |
| 008730 | atlas/ohlcv_tradable_by_symbol_year/008/008730/2024.csv | atlas/symbol_profiles/008/008730.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R3L93_C11_DUKSAN_2024_STAGE2_ACTIONABLE_ELECTROLYTE_ADDITIVE_ORDERBOOK_BRIDGE | 317330 | Stage2-Actionable | 2024-02-14 | 23850 | positive | electrolyte/additive customer-orderbook bridge worked |
| R3L93_C11_WONJUN_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH | 382840 | Stage2-Actionable | 2024-02-21 | 19110 | counterexample | battery equipment orderbook false Stage2 |
| R3L93_C11_YULCHONCHEM_2024_STAGE4B_POUCH_FILM_ORDERBOOK_EVENT_CAP | 008730 | Stage4B | 2024-02-16 | 45250 | counterexample/4B | pouch-film orderbook event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R3L93_C11_DUKSAN_2024_STAGE2_ACTIONABLE_ELECTROLYTE_ADDITIVE_ORDERBOOK_BRIDGE | 23850 | 96.65 | -10.06 | 183.02 | -10.06 | 183.02 | -10.06 | 2024-06-24 | 67500 | -52.52 |
| R3L93_C11_WONJUN_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH | 19110 | 8.06 | -12.87 | 8.06 | -28.00 | 8.06 | -55.00 | 2024-03-12 | 20650 | -58.35 |
| R3L93_C11_YULCHONCHEM_2024_STAGE4B_POUCH_FILM_ORDERBOOK_EVENT_CAP | 45250 | 8.51 | -22.76 | 8.51 | -32.71 | 8.51 | -55.36 | 2024-02-23 | 49100 | -58.86 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C11 Stage2 needs customer qualification / orderbook / capacity / call-off / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing battery orderbook premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE battery-orderbook rows cannot promote without durable customer/margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is customer-orderbook bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 317330 | good_stage2_with_later_watch | Customer/orderbook/capacity bridge produced very high MFE, but later valuation drawdown requires 4B watch. |
| 382840 | bad_stage2 | Equipment orderbook watch lacked delivery/margin bridge and collapsed after low forward MFE. |
| 008730 | good_4B | Pouch-film orderbook premium capped near the February spike and then de-rated. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 382840 battery equipment false Stage2 | 0.93 | 0.93 | false Stage2 due missing customer delivery/margin bridge |
| 008730 pouch-film cap | 0.92 | 0.92 | good full-window 4B timing after severe MAE confirmation |
| 317330 electrolyte/additive bridge | n/a | n/a | positive Stage2, but later battery-material valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 382840 / 008730
```

No hard 4C candidate is proposed. R3 loop 93 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 battery orderbook rerating cases, Stage2 requires verified customer qualification, firm/orderbook visibility, call-off durability, capacity ramp, margin, or revision bridge. Battery material, equipment, pouch film, electrolyte, additive, orderbook, or customer-rumor label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
rule = C11 should split true customer-orderbook/capacity/margin positives from equipment orderbook false Stage2 and pouch-film event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 66.53 | -23.59 | 0.67 | mixed; C11 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 66.53 | -23.59 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L3 customer/orderbook/margin bridge required | 2 | 95.54 | -19.03 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C11 bridge vs event-cap split | 2 | 95.54 | -19.03 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing battery orderbook themes as positive | 1 | 183.02 | -10.06 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 317330 customer-orderbook bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 183.02 | -10.06 | electrolyte_additive_orderbook_positive |
| 382840 equipment orderbook false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 8.06 | -28.00 | battery_equipment_orderbook_false_stage2 |
| 008730 pouch-film cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 8.51 | -32.71 | pouch_film_orderbook_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "ELECTROLYTE_ADDITIVE_CUSTOMER_ORDERBOOK_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_POUCH_FILM_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C11 electrolyte/additive customer orderbook positive, battery-equipment orderbook false Stage2, and pouch-film orderbook event-cap 4B split while avoiding top repeated C11 symbols."}
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
residual_error_types_found: electrolyte_additive_orderbook_positive, battery_equipment_orderbook_false_stage2, pouch_film_orderbook_event_cap_4B
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
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,configured,C11_requires_customer_orderbook_capacity_calloff_margin_revision_bridge,0,"C11 Stage2 should require customer qualification, orderbook visibility, capacity ramp, call-off durability, margin, or revision bridge, not battery/orderbook/material label alone","Duksan Techopia positive worked; Wonjun and Yulchon Chemical event/watch rows failed positive-stage promotion","R3L93_C11_DUKSAN_2024_STAGE2_ACTIONABLE_ELECTROLYTE_ADDITIVE_ORDERBOOK_BRIDGE|R3L93_C11_WONJUN_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH|R3L93_C11_YULCHONCHEM_2024_STAGE4B_POUCH_FILM_ORDERBOOK_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,configured,cap_bridge_missing_battery_orderbook_event_premiums_as_4B_watch,0,"Battery material/equipment orderbook premiums can peak before customer call-off and margin bridge is proven","Wonjun had low forward MFE and deep later MAE; Yulchon Chemical showed 4B event-cap behavior after February spike","R3L93_C11_WONJUN_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH|R3L93_C11_YULCHONCHEM_2024_STAGE4B_POUCH_FILM_ORDERBOOK_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,configured,block_positive_stage_when_orderbook_theme_has_high_MAE_without_customer_margin_bridge,0,"High MAE after bridge-missing battery orderbook entries should block Stage2/Stage3 promotion unless customer, call-off, capacity and margin evidence survives","Wonjun MAE180=-55.00 and Yulchon Chemical MAE180=-55.36","R3L93_C11_WONJUN_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH|R3L93_C11_YULCHONCHEM_2024_STAGE4B_POUCH_FILM_ORDERBOOK_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R3L93_C11_DUKSAN_2024_ELECTROLYTE_ADDITIVE_CUSTOMER_ORDERBOOK_POSITIVE", "symbol": "317330", "company_name": "덕산테코피아", "round": "R3", "loop": "93", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "ELECTROLYTE_ADDITIVE_CUSTOMER_ORDERBOOK_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_POUCH_FILM_EVENT_CAP", "case_type": "structural_success_with_later_battery_material_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R3L93_C11_DUKSAN_2024_STAGE2_ACTIONABLE_ELECTROLYTE_ADDITIVE_ORDERBOOK_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Electrolyte/additive and battery-material customer/orderbook rerating bridge produced very high 30D/90D/180D MFE with controlled initial MAE. C11 works when the battery material story maps into customer qualification, orderbook visibility, capacity ramp, margin and revision bridge, but later valuation/cycle watch remains necessary.", "current_profile_verdict": "current_profile_kept_but_C11_positive_requires_customer_orderbook_capacity_margin_revision_bridge_not_battery_material_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R3L93_C11_WONJUN_2024_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_STAGE2", "symbol": "382840", "company_name": "원준", "round": "R3", "loop": "93", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "ELECTROLYTE_ADDITIVE_CUSTOMER_ORDERBOOK_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_POUCH_FILM_EVENT_CAP", "case_type": "failed_rerating_equipment_orderbook_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R3L93_C11_WONJUN_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Battery heat-treatment/equipment orderbook recovery watch had low forward MFE and then large 90D/180D MAE. C11 Stage2 should not be awarded without verified customer order, equipment delivery schedule, utilization, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_battery_equipment_orderbook_watch_counts_without_customer_delivery_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2022 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R3L93_C11_YULCHONCHEM_2024_POUCH_FILM_ORDERBOOK_EVENT_CAP_4B", "symbol": "008730", "company_name": "율촌화학", "round": "R3", "loop": "93", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "ELECTROLYTE_ADDITIVE_CUSTOMER_ORDERBOOK_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_POUCH_FILM_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R3L93_C11_YULCHONCHEM_2024_STAGE4B_POUCH_FILM_ORDERBOOK_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Battery pouch-film / orderbook event premium capped around the February spike and then suffered severe 90D/180D MAE. C11 should route bridge-missing battery-material orderbook premiums to 4B unless customer call-off, contract duration, capacity ramp, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_pouch_film_orderbook_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1999 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R3L93_C11_DUKSAN_2024_STAGE2_ACTIONABLE_ELECTROLYTE_ADDITIVE_ORDERBOOK_BRIDGE", "case_id": "R3L93_C11_DUKSAN_2024_ELECTROLYTE_ADDITIVE_CUSTOMER_ORDERBOOK_POSITIVE", "symbol": "317330", "company_name": "덕산테코피아", "round": "R3", "loop": "93", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "ELECTROLYTE_ADDITIVE_CUSTOMER_ORDERBOOK_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_POUCH_FILM_EVENT_CAP", "sector": "electrolyte_additive_battery_material_customer_orderbook", "primary_archetype": "customer_qualification_orderbook_capacity_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-14", "entry_date": "2024-02-14", "entry_price": 23850.0, "evidence_available_at_that_date": "battery electrolyte/additive customer qualification, orderbook visibility, capacity ramp, margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["customer_qualification_proxy", "orderbook_visibility_proxy", "capacity_ramp_proxy", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "very_high_MFE180", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_battery_material_valuation_watch", "post_peak_drawdown_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/317/317330/2024.csv", "profile_path": "atlas/symbol_profiles/317/317330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 96.65, "MFE_90D_pct": 183.02, "MFE_180D_pct": 183.02, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -10.06, "MAE_90D_pct": -10.06, "MAE_180D_pct": -10.06, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-24", "peak_price": 67500.0, "drawdown_after_peak_pct": -52.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_battery_material_valuation_4B_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "battery_material_orderbook_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_electrolyte_additive_orderbook_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R3L93_C11_317330_2024-02-14_23850", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L93_C11_WONJUN_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH", "case_id": "R3L93_C11_WONJUN_2024_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_STAGE2", "symbol": "382840", "company_name": "원준", "round": "R3", "loop": "93", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "ELECTROLYTE_ADDITIVE_CUSTOMER_ORDERBOOK_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_POUCH_FILM_EVENT_CAP", "sector": "battery_equipment_orderbook_recovery_watch", "primary_archetype": "battery_equipment_orderbook_watch_without_customer_delivery_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-21", "entry_date": "2024-02-21", "entry_price": 19110.0, "evidence_available_at_that_date": "battery heat-treatment/equipment orderbook recovery watch and customer equipment order expectation proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["battery_equipment_orderbook_watch", "customer_order_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "deep_MAE180", "customer_delivery_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/382/382840/2024.csv", "profile_path": "atlas/symbol_profiles/382/382840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.06, "MFE_90D_pct": 8.06, "MFE_180D_pct": 8.06, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -12.87, "MAE_90D_pct": -28.0, "MAE_180D_pct": -55.0, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-12", "peak_price": 20650.0, "drawdown_after_peak_pct": -58.35, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "battery_equipment_orderbook_watch_was_false_stage2_due_missing_customer_delivery_margin_bridge", "four_b_evidence_type": ["battery_equipment_orderbook_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_battery_equipment_orderbook_without_customer_delivery_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_battery_equipment_orderbook_watch_counts_without_customer_delivery_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2022_CA", "same_entry_group_id": "R3L93_C11_382840_2024-02-21_19110", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L93_C11_YULCHONCHEM_2024_STAGE4B_POUCH_FILM_ORDERBOOK_EVENT_CAP", "case_id": "R3L93_C11_YULCHONCHEM_2024_POUCH_FILM_ORDERBOOK_EVENT_CAP_4B", "symbol": "008730", "company_name": "율촌화학", "round": "R3", "loop": "93", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "ELECTROLYTE_ADDITIVE_CUSTOMER_ORDERBOOK_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_POUCH_FILM_EVENT_CAP", "sector": "battery_pouch_film_orderbook_event_premium", "primary_archetype": "pouch_film_orderbook_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-16", "entry_date": "2024-02-16", "entry_price": 45250.0, "evidence_available_at_that_date": "battery pouch-film / orderbook event premium after February spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["pouch_film_orderbook_event", "customer_calloff_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "customer_calloff_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008730/2024.csv", "profile_path": "atlas/symbol_profiles/008/008730.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.51, "MFE_90D_pct": 8.51, "MFE_180D_pct": 8.51, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -22.76, "MAE_90D_pct": -32.71, "MAE_180D_pct": -55.36, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-23", "peak_price": 49100.0, "drawdown_after_peak_pct": -58.86, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_full_window_4B_timing_pouch_film_orderbook_event_cap", "four_b_evidence_type": ["battery_material_orderbook_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_pouch_film_orderbook_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_pouch_film_orderbook_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1999_CA", "same_entry_group_id": "R3L93_C11_008730_2024-02-16_45250", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L93_C11_DUKSAN_2024_ELECTROLYTE_ADDITIVE_CUSTOMER_ORDERBOOK_POSITIVE", "trigger_id": "R3L93_C11_DUKSAN_2024_STAGE2_ACTIONABLE_ELECTROLYTE_ADDITIVE_ORDERBOOK_BRIDGE", "symbol": "317330", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 40, "backlog_visibility_score": 65, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 55, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "electrolyte_additive_orderbook_positive", "MFE_90D_pct": 183.02, "MAE_90D_pct": -10.06, "score_return_alignment_label": "electrolyte_additive_orderbook_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L93_C11_WONJUN_2024_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_STAGE2", "trigger_id": "R3L93_C11_WONJUN_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH", "symbol": "382840", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "battery_equipment_orderbook_false_stage2", "MFE_90D_pct": 8.06, "MAE_90D_pct": -28.0, "score_return_alignment_label": "battery_equipment_orderbook_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_battery_equipment_orderbook_watch_counts_without_customer_delivery_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L93_C11_YULCHONCHEM_2024_POUCH_FILM_ORDERBOOK_EVENT_CAP_4B", "trigger_id": "R3L93_C11_YULCHONCHEM_2024_STAGE4B_POUCH_FILM_ORDERBOOK_EVENT_CAP", "symbol": "008730", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "pouch_film_orderbook_event_cap_4B_guard", "MFE_90D_pct": 8.51, "MAE_90D_pct": -32.71, "score_return_alignment_label": "pouch_film_orderbook_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_pouch_film_orderbook_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": "93", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "ELECTROLYTE_ADDITIVE_CUSTOMER_ORDERBOOK_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_POUCH_FILM_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["electrolyte_additive_orderbook_positive", "battery_equipment_orderbook_false_stage2", "pouch_film_orderbook_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
10. Add tests that bridge-missing C11 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R3
completed_loop = 93
next_round = R4
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
