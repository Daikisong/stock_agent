# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R3
scheduled_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_THERMAL_MANAGEMENT_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
```

This file is the corrected final output for this execution. The scheduler state after R2 loop 96 is R3 / loop 96. R3 is the L3 battery/EV/green-mobility round, and this run fills C11 battery orderbook rerating rather than repeating the immediately preceding R3 loop 95 C13 JV/utilization file or R9 loop 95 C14 demand-slowdown file.

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
scheduled_round = R3
scheduled_loop = 96
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
round_sector_consistency = pass
computed_next_round = R4
computed_next_loop = 96
```

C11 is an orderbook-to-margin bridge archetype. Battery-label heat is the spark; the engine runs only when customer orderbook, call-off durability, delivery cadence, utilization, ASP/mix, margin and revision are visible.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C11_BATTERY_ORDERBOOK_RERATING = 21 rows / 14 symbols / good-bad Stage2 8-4 / 4B-4C 1-0
top covered symbols include 137400(4), 299030(3), 003670(2), 302430(2), 001570(1), 005070(1)
previous R3 loop-93 C11 symbols avoided: 317330, 382840, 008730
previous R3 loop-94 C12 symbols avoided: 036830, 418550, 078600
previous R3 loop-95 C13 symbols avoided: 014820, 093370, 450080
previous R9 loop-95 C14 symbols avoided: 361610, 393890, 025900
previous R2 loop-96 C08 symbols avoided: 424980, 098120, 080580
```

Selected rows avoid hard duplicates and top repeated C11 symbols:

```text
006110 / Stage2-Actionable / 2024-02-06
079810 / Stage2-Actionable / 2024-02-21
417010 / Stage4B / 2024-03-26
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
| 006110 | atlas/symbol_profiles/006/006110.json | selected 2024 window clean after old CA candidates |
| 079810 | atlas/symbol_profiles/079/079810.json | selected 2024 window clean after old 2023 CA candidate |
| 417010 | atlas/symbol_profiles/417/417010.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R3L96_C11_SAMAALUMINUM_2024_BATTERY_FOIL_ORDERBOOK_MARGIN_POSITIVE | 006110 | 2024-02-06 | yes | 180 | yes | yes | true |
| R3L96_C11_DENT_2024_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_STAGE2 | 079810 | 2024-02-21 | yes | 180 | yes | yes | true |
| R3L96_C11_NANOTIM_2024_THERMAL_MANAGEMENT_BATTERY_ORDER_EVENT_CAP_4B | 417010 | 2024-03-26 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C11_BATTERY_ORDERBOOK_RERATING | BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE | Positive Stage2 requires customer orderbook, call-off durability, delivery cadence, utilization, ASP/mix, margin and revision bridge. |
| C11_BATTERY_ORDERBOOK_RERATING | BATTERY_EQUIPMENT_FALSE_STAGE2 | Battery-equipment orderbook watch without call-off/delivery/margin bridge can become false Stage2. |
| C11_BATTERY_ORDERBOOK_RERATING | THERMAL_MANAGEMENT_EVENT_CAP_4B | Thermal-management battery-parts event premium should route to 4B when customer orderbook and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R3L96_C11_SAMAALUMINUM_2024_BATTERY_FOIL_ORDERBOOK_MARGIN_POSITIVE | 006110 | 삼아알미늄 | positive | Battery-foil orderbook and margin bridge produced strong MFE after the February washout. |
| R3L96_C11_DENT_2024_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_STAGE2 | 079810 | 디이엔티 | counterexample | Equipment orderbook watch had tiny MFE and high MAE without call-off/margin bridge. |
| R3L96_C11_NANOTIM_2024_THERMAL_MANAGEMENT_BATTERY_ORDER_EVENT_CAP_4B | 417010 | 나노팀 | counterexample / 4B | Thermal-management battery-parts event premium capped after the March spike and de-rated. |

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
| SamA Aluminum battery foil orderbook bridge | historical public/report proxy | true | true | shadow-only positive |
| DENT battery equipment false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Nanotim thermal-management event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 006110 | atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv | atlas/symbol_profiles/006/006110.json |
| 079810 | atlas/ohlcv_tradable_by_symbol_year/079/079810/2024.csv | atlas/symbol_profiles/079/079810.json |
| 417010 | atlas/ohlcv_tradable_by_symbol_year/417/417010/2024.csv | atlas/symbol_profiles/417/417010.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R3L96_C11_SAMAALUMINUM_2024_STAGE2_ACTIONABLE_BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE | 006110 | Stage2-Actionable | 2024-02-06 | 82100 | positive | battery-foil orderbook/margin bridge worked |
| R3L96_C11_DENT_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH | 079810 | Stage2-Actionable | 2024-02-21 | 17000 | counterexample | battery equipment orderbook false Stage2 |
| R3L96_C11_NANOTIM_2024_STAGE4B_THERMAL_MANAGEMENT_BATTERY_ORDER_EVENT_CAP | 417010 | Stage4B | 2024-03-26 | 14790 | counterexample/4B | thermal-management battery event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R3L96_C11_SAMAALUMINUM_2024_STAGE2_ACTIONABLE_BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE | 82100 | 41.78 | -2.31 | 41.78 | -16.20 | 41.78 | -24.48 | 2024-02-21 | 116400 | -42.27 |
| R3L96_C11_DENT_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH | 17000 | 2.47 | -19.47 | 2.47 | -31.88 | 2.47 | -55.41 | 2024-02-22 | 17420 | -56.03 |
| R3L96_C11_NANOTIM_2024_STAGE4B_THERMAL_MANAGEMENT_BATTERY_ORDER_EVENT_CAP | 14790 | 2.23 | -14.81 | 2.23 | -28.87 | 2.23 | -35.77 | 2024-03-27 | 15120 | -36.57 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C11 Stage2 needs customer orderbook / call-off durability / delivery cadence / utilization / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing battery equipment and parts premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE battery-orderbook rows cannot promote without durable customer/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether battery orderbook narrative becomes customer, call-off and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 006110 | good_stage2_with_later_watch | Battery-foil orderbook bridge produced strong MFE, but later drawdown requires valuation/call-off watch. |
| 079810 | bad_stage2 | Equipment orderbook watch lacked call-off/margin evidence and produced tiny MFE. |
| 417010 | good_4B | Thermal-management event premium capped after the March spike and then suffered high MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 079810 battery equipment false Stage2 | 0.98 | 0.98 | false Stage2 due missing customer call-off / delivery / margin bridge |
| 417010 thermal-management cap | 0.98 | 0.98 | good full-window 4B timing after March battery-parts event premium |
| 006110 battery-foil bridge | n/a | n/a | positive Stage2, but later battery-foil valuation and call-off watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 079810 / 417010
```

No hard 4C candidate is introduced in this R3 loop 96 file. The counterexamples are bridge-missing / event-cap rows, not hard thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 battery orderbook-rerating cases, Stage2 requires verified customer orderbook quality, call-off durability, delivery cadence, utilization, ASP/mix, margin, or revision bridge. Battery material, foil, equipment, thermal-management, EV parts or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
rule = C11 should split true orderbook/delivery/margin positives from battery-equipment orderbook false Stage2 and battery-parts event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 15.49 | -25.65 | 0.67 | mixed; C11 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 15.49 | -25.65 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L3 orderbook/call-off/margin bridge required | 2 | 22.13 | -24.04 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C11 bridge vs event-cap split | 2 | 22.13 | -24.04 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing battery orderbook themes as positive | 1 | 41.78 | -16.20 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 006110 battery-foil bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 41.78 | -16.20 | battery_foil_orderbook_margin_positive |
| 079810 battery-equipment false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 2.47 | -31.88 | battery_equipment_orderbook_false_stage2 |
| 417010 thermal-management cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 2.23 | -28.87 | thermal_management_order_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_THERMAL_MANAGEMENT_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C11 SamA Aluminum battery-foil orderbook/margin positive, DENT battery-equipment orderbook false Stage2, and Nanotim thermal-management order event-cap 4B while avoiding top repeated C11 and previous R3/R9/R2 loop symbols."}
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
residual_error_types_found: battery_foil_orderbook_margin_positive, battery_equipment_orderbook_false_stage2, thermal_management_order_event_cap_4B
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
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,configured,C11_requires_customer_orderbook_delivery_utilization_ASP_mix_margin_revision_bridge,0,"C11 Stage2 should require customer orderbook quality, delivery cadence, call-off durability, utilization, ASP/mix, margin, or revision bridge, not battery-equipment or battery-parts label alone","SamA Aluminum positive worked; DENT and Nanotim event/watch rows failed positive-stage promotion","R3L96_C11_SAMAALUMINUM_2024_STAGE2_ACTIONABLE_BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE|R3L96_C11_DENT_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH|R3L96_C11_NANOTIM_2024_STAGE4B_THERMAL_MANAGEMENT_BATTERY_ORDER_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,configured,cap_bridge_missing_battery_equipment_and_parts_event_premiums_as_4B_watch,0,"Battery-equipment and thermal-management parts premiums can peak before call-off, delivery and margin bridge is proven","DENT had tiny MFE after orderbook watch; Nanotim showed 4B event-cap behavior after the March battery-parts spike","R3L96_C11_DENT_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH|R3L96_C11_NANOTIM_2024_STAGE4B_THERMAL_MANAGEMENT_BATTERY_ORDER_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,configured,block_positive_stage_when_battery_orderbook_theme_has_high_or_persistent_MAE_without_margin_bridge,0,"High or persistent MAE after bridge-missing C11 entries should block Stage2/Stage3 promotion unless customer-orderbook and margin evidence survives","DENT MAE90=-31.88 and Nanotim MAE90=-28.87","R3L96_C11_DENT_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH|R3L96_C11_NANOTIM_2024_STAGE4B_THERMAL_MANAGEMENT_BATTERY_ORDER_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R3L96_C11_SAMAALUMINUM_2024_BATTERY_FOIL_ORDERBOOK_MARGIN_POSITIVE", "symbol": "006110", "company_name": "삼아알미늄", "round": "R3", "loop": "96", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_THERMAL_MANAGEMENT_EVENT_CAP", "case_type": "structural_success_with_later_battery_foil_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R3L96_C11_SAMAALUMINUM_2024_STAGE2_ACTIONABLE_BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Battery foil orderbook / customer demand / margin-mix bridge produced strong 30D/90D MFE after the February washout, but later drawdown still requires valuation and call-off watch. C11 works only when orderbook rerating maps into customer-quality, delivery, utilization, ASP/mix, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C11_positive_requires_customer_orderbook_delivery_utilization_margin_revision_bridge_not_battery_material_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old corporate-action candidates; source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R3L96_C11_DENT_2024_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_STAGE2", "symbol": "079810", "company_name": "디이엔티", "round": "R3", "loop": "96", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_THERMAL_MANAGEMENT_EVENT_CAP", "case_type": "failed_rerating_battery_equipment_orderbook_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R3L96_C11_DENT_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Battery-equipment orderbook watch produced only a brief MFE and then high MAE. C11 Stage2 should not be awarded without confirmed equipment order quality, customer call-off durability, delivery cadence, utilization, ASP/mix, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_battery_equipment_orderbook_watch_counts_without_customer_calloff_delivery_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2023 corporate-action candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R3L96_C11_NANOTIM_2024_THERMAL_MANAGEMENT_BATTERY_ORDER_EVENT_CAP_4B", "symbol": "417010", "company_name": "나노팀", "round": "R3", "loop": "96", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_THERMAL_MANAGEMENT_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R3L96_C11_NANOTIM_2024_STAGE4B_THERMAL_MANAGEMENT_BATTERY_ORDER_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Thermal-management / battery order event premium capped shortly after the March spike and then deteriorated. C11 should route bridge-missing thermal-management/battery-parts event premiums to 4B unless customer orderbook, delivery slot, utilization, ASP/mix, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_thermal_management_battery_order_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R3L96_C11_SAMAALUMINUM_2024_STAGE2_ACTIONABLE_BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE", "case_id": "R3L96_C11_SAMAALUMINUM_2024_BATTERY_FOIL_ORDERBOOK_MARGIN_POSITIVE", "symbol": "006110", "company_name": "삼아알미늄", "round": "R3", "loop": "96", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_THERMAL_MANAGEMENT_EVENT_CAP", "sector": "battery_foil_orderbook_customer_margin", "primary_archetype": "customer_orderbook_delivery_utilization_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-06", "entry_date": "2024-02-06", "entry_price": 82100.0, "evidence_available_at_that_date": "battery foil customer-orderbook / delivery cadence / utilization and margin-mix recovery proxy after January-February washout; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["battery_foil_orderbook_proxy", "customer_quality_proxy", "delivery_cadence_proxy", "utilization_recovery_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "positive_MFE180"], "stage4b_evidence_fields": ["later_battery_foil_valuation_watch", "EV_calloff_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv", "profile_path": "atlas/symbol_profiles/006/006110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 41.78, "MFE_90D_pct": 41.78, "MFE_180D_pct": 41.78, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -2.31, "MAE_90D_pct": -16.2, "MAE_180D_pct": -24.48, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-21", "peak_price": 116400.0, "drawdown_after_peak_pct": -42.27, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_battery_foil_valuation_and_calloff_4B_watch_needed", "four_b_evidence_type": ["battery_foil_orderbook_bridge", "customer_quality", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_battery_foil_orderbook_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA_candidates", "same_entry_group_id": "R3L96_C11_006110_2024-02-06_82100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L96_C11_DENT_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH", "case_id": "R3L96_C11_DENT_2024_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_STAGE2", "symbol": "079810", "company_name": "디이엔티", "round": "R3", "loop": "96", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_THERMAL_MANAGEMENT_EVENT_CAP", "sector": "battery_equipment_orderbook_customer_calloff_watch", "primary_archetype": "battery_equipment_watch_without_calloff_delivery_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-21", "entry_date": "2024-02-21", "entry_price": 17000.0, "evidence_available_at_that_date": "battery-equipment orderbook/capacity watch without confirmed customer call-off durability, delivery cadence, utilization or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["battery_equipment_orderbook_watch", "relative_strength_spike", "EV_capex_recovery_theme"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "deep_MAE90", "customer_calloff_delivery_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/079/079810/2024.csv", "profile_path": "atlas/symbol_profiles/079/079810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.47, "MFE_90D_pct": 2.47, "MFE_180D_pct": 2.47, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -19.47, "MAE_90D_pct": -31.88, "MAE_180D_pct": -55.41, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-22", "peak_price": 17420.0, "drawdown_after_peak_pct": -56.03, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "battery_equipment_orderbook_watch_was_false_stage2_due_missing_customer_calloff_delivery_margin_bridge", "four_b_evidence_type": ["battery_equipment_capex_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_battery_equipment_orderbook_watch_without_calloff_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_battery_equipment_orderbook_watch_counts_without_customer_calloff_delivery_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2023_CA", "same_entry_group_id": "R3L96_C11_079810_2024-02-21_17000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L96_C11_NANOTIM_2024_STAGE4B_THERMAL_MANAGEMENT_BATTERY_ORDER_EVENT_CAP", "case_id": "R3L96_C11_NANOTIM_2024_THERMAL_MANAGEMENT_BATTERY_ORDER_EVENT_CAP_4B", "symbol": "417010", "company_name": "나노팀", "round": "R3", "loop": "96", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_THERMAL_MANAGEMENT_EVENT_CAP", "sector": "battery_thermal_management_order_event_premium", "primary_archetype": "thermal_management_battery_order_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-26", "entry_date": "2024-03-26", "entry_price": 14790.0, "evidence_available_at_that_date": "battery thermal-management / EV parts order event premium after March battery-parts spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["thermal_management_order_event", "battery_parts_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "orderbook_delivery_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/417/417010/2024.csv", "profile_path": "atlas/symbol_profiles/417/417010.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.23, "MFE_90D_pct": 2.23, "MFE_180D_pct": 2.23, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -14.81, "MAE_90D_pct": -28.87, "MAE_180D_pct": -35.77, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-27", "peak_price": 15120.0, "drawdown_after_peak_pct": -36.57, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing_thermal_management_battery_order_event_cap", "four_b_evidence_type": ["battery_parts_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_thermal_management_battery_order_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_thermal_management_battery_order_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R3L96_C11_417010_2024-03-26_14790", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L96_C11_SAMAALUMINUM_2024_BATTERY_FOIL_ORDERBOOK_MARGIN_POSITIVE", "trigger_id": "R3L96_C11_SAMAALUMINUM_2024_STAGE2_ACTIONABLE_BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE", "symbol": "006110", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 60, "customer_quality_score": 40, "policy_or_regulatory_score": 15, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 60, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 65, "customer_quality_score": 55, "policy_or_regulatory_score": 15, "valuation_repricing_score": 45, "execution_risk_score": 40, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "battery_foil_orderbook_margin_positive", "MFE_90D_pct": 41.78, "MAE_90D_pct": -16.2, "score_return_alignment_label": "battery_foil_orderbook_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L96_C11_DENT_2024_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_STAGE2", "trigger_id": "R3L96_C11_DENT_2024_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_WATCH", "symbol": "079810", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 15, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "battery_equipment_orderbook_false_stage2", "MFE_90D_pct": 2.47, "MAE_90D_pct": -31.88, "score_return_alignment_label": "battery_equipment_orderbook_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_battery_equipment_orderbook_watch_counts_without_customer_calloff_delivery_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L96_C11_NANOTIM_2024_THERMAL_MANAGEMENT_BATTERY_ORDER_EVENT_CAP_4B", "trigger_id": "R3L96_C11_NANOTIM_2024_STAGE4B_THERMAL_MANAGEMENT_BATTERY_ORDER_EVENT_CAP", "symbol": "417010", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 15, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "thermal_management_battery_order_event_cap_4B_guard", "MFE_90D_pct": 2.23, "MAE_90D_pct": -28.87, "score_return_alignment_label": "thermal_management_battery_order_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_thermal_management_battery_order_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": "96", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_FOIL_ORDERBOOK_MARGIN_BRIDGE_VS_BATTERY_EQUIPMENT_FALSE_STAGE2_AND_THERMAL_MANAGEMENT_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["battery_foil_orderbook_margin_positive", "battery_equipment_orderbook_false_stage2", "thermal_management_order_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C11 rows need explicit customer orderbook quality, call-off durability, delivery cadence, utilization, ASP/mix, margin or revision bridge before positive promotion.
- In C11, event-premium rows with low MFE/high MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C11 battery orderbook rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R3
completed_loop = 96
next_round = R4
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
