# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R3
scheduled_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = BATTERY_MATERIAL_ORDER_REVISION_BRIDGE_VS_EQUIPMENT_AND_CNT_THEME_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R3_loop_89_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
```

This loop continues loop 89 after R2. It adds 3 C11 battery-orderbook rerating cases: one battery-material order/revision positive, one battery-equipment false Stage2, and one CNT/conductive-additive 4B event-cap counterexample.

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
scheduled_round = R3
scheduled_loop = 89
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
round_sector_consistency = pass
computed_next_round = R4
computed_next_loop = 89
```

R3 permits L3 battery/EV/green mobility research. Previous R3 loop-88 used C14, so this loop moves to C11 and targets the residual split between real order/revision bridge and battery-material/equipment theme premium.

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
```

Selected rows avoid those repeated combinations:

```text
078600 / Stage2-Actionable / 2024-02-21
382840 / Stage2-Actionable / 2024-01-04
418550 / Stage4B / 2024-03-26
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
| 078600 | atlas/symbol_profiles/078/078600.json | no corporate-action candidate |
| 382840 | atlas/symbol_profiles/382/382840.json | selected 2024 window clean; CA candidates are 2022-07-12 and 2022-07-29 |
| 418550 | atlas/symbol_profiles/418/418550.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R3L89_C11_DAEJOO_2024_SILICON_ANODE_ORDER_REVISION_POSITIVE | 078600 | 2024-02-21 | yes | 180 | yes | yes | true |
| R3L89_C11_ONEJOON_2024_BATTERY_EQUIPMENT_FALSE_STAGE2 | 382840 | 2024-01-04 | yes | 180 | yes | yes | true |
| R3L89_C11_JEO_2024_CNT_CONDUCTIVE_ADDITIVE_EVENT_CAP_4B | 418550 | 2024-03-26 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C11_BATTERY_ORDERBOOK_RERATING | BATTERY_MATERIAL_ORDER_REVISION_BRIDGE | Positive Stage2 requires customer/order/reorder/revision/margin bridge. |
| C11_BATTERY_ORDERBOOK_RERATING | BATTERY_EQUIPMENT_FALSE_STAGE2 | Battery-equipment/orderbook headline without bridge can become weak-MFE/high-MAE false Stage2. |
| C11_BATTERY_ORDERBOOK_RERATING | CNT_MATERIAL_EVENT_CAP_4B | CNT/conductive-additive theme premium should route to 4B unless reorder/margin bridge is verified. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R3L89_C11_DAEJOO_2024_SILICON_ANODE_ORDER_REVISION_POSITIVE | 078600 | 대주전자재료 | positive | Silicon-anode/material order-revision bridge produced large MFE with shallow early MAE. |
| R3L89_C11_ONEJOON_2024_BATTERY_EQUIPMENT_FALSE_STAGE2 | 382840 | 원준 | counterexample | Battery-equipment theme spike failed and drew down persistently. |
| R3L89_C11_JEO_2024_CNT_CONDUCTIVE_ADDITIVE_EVENT_CAP_4B | 418550 | 제이오 | counterexample / 4B | CNT/conductive-additive premium capped and later drew down. |

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
| Daejoo material order/revision | historical public/report proxy | true | true | shadow-only positive |
| Onejoon equipment false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Jeo CNT material event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 078600 | atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv | atlas/symbol_profiles/078/078600.json |
| 382840 | atlas/ohlcv_tradable_by_symbol_year/382/382840/2024.csv | atlas/symbol_profiles/382/382840.json |
| 418550 | atlas/ohlcv_tradable_by_symbol_year/418/418550/2024.csv | atlas/symbol_profiles/418/418550.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R3L89_C11_DAEJOO_2024_STAGE2_ACTIONABLE_ORDER_REVISION_BRIDGE | 078600 | Stage2-Actionable | 2024-02-21 | 76000 | positive | battery-material order/revision bridge worked |
| R3L89_C11_ONEJOON_2024_STAGE2_FALSE_POSITIVE_EQUIPMENT_ORDERBOOK_THEME | 382840 | Stage2-Actionable | 2024-01-04 | 18910 | counterexample | battery-equipment false Stage2 |
| R3L89_C11_JEO_2024_STAGE4B_CNT_CONDUCTIVE_ADDITIVE_CAP | 418550 | Stage4B | 2024-03-26 | 28050 | counterexample/4B | CNT material event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R3L89_C11_DAEJOO_2024_STAGE2_ACTIONABLE_ORDER_REVISION_BRIDGE | 76000 | 35.79 | -3.03 | 115.00 | -3.03 | 115.00 | -3.03 | 2024-06-12 | 163400 | -28.76 |
| R3L89_C11_ONEJOON_2024_STAGE2_FALSE_POSITIVE_EQUIPMENT_ORDERBOOK_THEME | 18910 | 12.64 | -14.75 | 12.64 | -24.22 | 12.64 | -54.52 | 2024-01-04 | 21300 | -59.62 |
| R3L89_C11_JEO_2024_STAGE4B_CNT_CONDUCTIVE_ADDITIVE_CAP | 28050 | 15.51 | -17.29 | 15.51 | -31.55 | 15.51 | -46.03 | 2024-03-26 | 32400 | -48.61 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C11 Stage2 needs customer/order/reorder/revision/margin bridge |
| local_4b_watch_guard | strengthen: battery material/equipment theme premium should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 078600 | good_stage2 | Battery-material order/revision bridge produced very high MFE90. |
| 382840 | bad_stage2 | Battery-equipment orderbook/theme label had weak MFE and deep MAE. |
| 418550 | good_4B | CNT material premium capped and then drew down. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 382840 equipment theme false Stage2 | 1.00 | 1.00 | battery_equipment_theme_spike_was_false_stage2_event_cap |
| 418550 CNT material cap | 1.00 | 1.00 | good_full_window_4B_timing_CNT_conductive_additive_event_cap |
| 078600 material order/revision | n/a | n/a | positive Stage2, but later material valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 382840 / 418550
```

No hard 4C candidate is proposed. R3 loop 89 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 battery orderbook rerating cases, Stage2 requires verified customer, order, reorder, revision, capacity, or margin bridge. Battery material, CNT, equipment, or orderbook label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
rule = C11 should split customer/order/revision positives from battery-equipment false Stage2 and CNT/material event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 47.72 | -19.60 | 0.67 | mixed; C11 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 47.72 | -19.60 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L3 order/revision bridge required | 2 | 63.82 | -13.63 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C11 bridge vs event-cap split | 2 | 63.82 | -13.63 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing battery themes as positive | 1 | 115.00 | -3.03 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 078600 order/revision bridge | 66 | Stage2-Watch | 75 | Stage2-Actionable | 115.00 | -3.03 | battery_material_order_revision_positive |
| 382840 equipment false Stage2 | 66 | Stage2-Actionable | 53 | Stage1/Watch | 12.64 | -24.22 | battery_equipment_theme_false_stage2 |
| 418550 CNT cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 15.51 | -31.55 | CNT_material_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_ORDER_REVISION_BRIDGE_VS_EQUIPMENT_AND_CNT_THEME_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C11 battery-material order/revision positive, battery-equipment false Stage2, and CNT/conductive-additive event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: battery_material_order_revision_positive, battery_equipment_theme_false_stage2, CNT_material_event_cap_4B
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
- C11 battery orderbook bridge vs material/equipment event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,configured,C11_requires_customer_order_revision_margin_bridge,0,"C11 Stage2 should require verified customer/order/reorder/revision/margin bridge, not battery-material or battery-equipment label alone","Daejoo positive worked; Onejoon and Jeo theme/event rows failed positive-stage promotion","R3L89_C11_DAEJOO_2024_STAGE2_ACTIONABLE_ORDER_REVISION_BRIDGE|R3L89_C11_ONEJOON_2024_STAGE2_FALSE_POSITIVE_EQUIPMENT_ORDERBOOK_THEME|R3L89_C11_JEO_2024_STAGE4B_CNT_CONDUCTIVE_ADDITIVE_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,configured,cap_battery_material_and_equipment_theme_premium_as_4B_watch,0,"Battery equipment/CNT/material premiums can peak before durable order/revision bridge appears and then draw down heavily","Onejoon and Jeo showed weak/asymmetric MFE90 with high MAE90 after theme spikes","R3L89_C11_ONEJOON_2024_STAGE2_FALSE_POSITIVE_EQUIPMENT_ORDERBOOK_THEME|R3L89_C11_JEO_2024_STAGE4B_CNT_CONDUCTIVE_ADDITIVE_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R3L89_C11_DAEJOO_2024_SILICON_ANODE_ORDER_REVISION_POSITIVE", "symbol": "078600", "company_name": "대주전자재료", "round": "R3", "loop": "89", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_ORDER_REVISION_BRIDGE_VS_EQUIPMENT_AND_CNT_THEME_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R3L89_C11_DAEJOO_2024_STAGE2_ACTIONABLE_ORDER_REVISION_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Silicon-anode / battery-material order-revision bridge produced high 90D/180D MFE with shallow early MAE; C11 works when orderbook can convert into margin/revision.", "current_profile_verdict": "current_profile_kept_but_C11_positive_requires_order_revision_margin_bridge_not_battery_material_label_only", "price_source": "Songdaiki/stock-web", "notes": "Source-proxy only; exact as-of customer/order/revision evidence URL remains pending, so no production weight delta."}
{"row_type": "case", "case_id": "R3L89_C11_ONEJOON_2024_BATTERY_EQUIPMENT_FALSE_STAGE2", "symbol": "382840", "company_name": "원준", "round": "R3", "loop": "89", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_ORDER_REVISION_BRIDGE_VS_EQUIPMENT_AND_CNT_THEME_EVENT_CAP", "case_type": "failed_rerating_high_mae", "positive_or_counterexample": "counterexample", "best_trigger": "R3L89_C11_ONEJOON_2024_STAGE2_FALSE_POSITIVE_EQUIPMENT_ORDERBOOK_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Battery-equipment/orderbook theme spike had only modest MFE and deep 90D/180D drawdown; Stage2 should require visible order conversion and margin/revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_equipment_orderbook_theme_counts_without_order_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Clean modern window; source-proxy only."}
{"row_type": "case", "case_id": "R3L89_C11_JEO_2024_CNT_CONDUCTIVE_ADDITIVE_EVENT_CAP_4B", "symbol": "418550", "company_name": "제이오", "round": "R3", "loop": "89", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_ORDER_REVISION_BRIDGE_VS_EQUIPMENT_AND_CNT_THEME_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R3L89_C11_JEO_2024_STAGE4B_CNT_CONDUCTIVE_ADDITIVE_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "CNT/conductive-additive theme premium capped quickly after the March spike, then drew down; material theme premium should route to 4B unless reorder/margin bridge is verified.", "current_profile_verdict": "current_profile_4B_too_late_if_CNT_material_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R3L89_C11_DAEJOO_2024_STAGE2_ACTIONABLE_ORDER_REVISION_BRIDGE", "case_id": "R3L89_C11_DAEJOO_2024_SILICON_ANODE_ORDER_REVISION_POSITIVE", "symbol": "078600", "company_name": "대주전자재료", "round": "R3", "loop": "89", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_ORDER_REVISION_BRIDGE_VS_EQUIPMENT_AND_CNT_THEME_EVENT_CAP", "sector": "battery_material_silicon_anode", "primary_archetype": "battery_material_order_revision_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-21", "entry_date": "2024-02-21", "entry_price": 76000.0, "evidence_available_at_that_date": "silicon-anode / battery-material customer order and revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["customer_orderbook_proxy", "material_reorder_visibility", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["high_MFE30", "very_high_MFE90", "low_MAE90"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_material_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv", "profile_path": "atlas/symbol_profiles/078/078600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 35.79, "MFE_90D_pct": 115.0, "MFE_180D_pct": 115.0, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.03, "MAE_90D_pct": -3.03, "MAE_180D_pct": -3.03, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-12", "peak_price": 163400.0, "drawdown_after_peak_pct": -28.76, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_material_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_battery_material_order_revision_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L89_C11_078600_2024-02-21_76000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L89_C11_ONEJOON_2024_STAGE2_FALSE_POSITIVE_EQUIPMENT_ORDERBOOK_THEME", "case_id": "R3L89_C11_ONEJOON_2024_BATTERY_EQUIPMENT_FALSE_STAGE2", "symbol": "382840", "company_name": "원준", "round": "R3", "loop": "89", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_ORDER_REVISION_BRIDGE_VS_EQUIPMENT_AND_CNT_THEME_EVENT_CAP", "sector": "battery_equipment_furnace_process", "primary_archetype": "battery_equipment_orderbook_theme_false_stage2", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-04", "entry_date": "2024-01-04", "entry_price": 18910.0, "evidence_available_at_that_date": "battery-equipment / process furnace orderbook theme proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["battery_equipment_theme", "orderbook_headline_proxy", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "deep_MAE90", "order_margin_revision_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/382/382840/2024.csv", "profile_path": "atlas/symbol_profiles/382/382840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.64, "MFE_90D_pct": 12.64, "MFE_180D_pct": 12.64, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -14.75, "MAE_90D_pct": -24.22, "MAE_180D_pct": -54.52, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-04", "peak_price": 21300.0, "drawdown_after_peak_pct": -59.62, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "battery_equipment_theme_spike_was_false_stage2_event_cap", "four_b_evidence_type": ["price_only", "positioning_overheat", "order_margin_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_battery_equipment_orderbook_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_if_equipment_orderbook_theme_counts_without_order_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L89_C11_382840_2024-01-04_18910", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L89_C11_JEO_2024_STAGE4B_CNT_CONDUCTIVE_ADDITIVE_CAP", "case_id": "R3L89_C11_JEO_2024_CNT_CONDUCTIVE_ADDITIVE_EVENT_CAP_4B", "symbol": "418550", "company_name": "제이오", "round": "R3", "loop": "89", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_ORDER_REVISION_BRIDGE_VS_EQUIPMENT_AND_CNT_THEME_EVENT_CAP", "sector": "battery_material_CNT_conductive_additive", "primary_archetype": "CNT_conductive_additive_material_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-26", "entry_date": "2024-03-26", "entry_price": 28050.0, "evidence_available_at_that_date": "CNT / conductive additive battery-material theme premium after March spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["CNT_material_theme", "conductive_additive_growth_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/418/418550/2024.csv", "profile_path": "atlas/symbol_profiles/418/418550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.51, "MFE_90D_pct": 15.51, "MFE_180D_pct": 15.51, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -17.29, "MAE_90D_pct": -31.55, "MAE_180D_pct": -46.03, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-26", "peak_price": 32400.0, "drawdown_after_peak_pct": -48.61, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_CNT_conductive_additive_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_CNT_material_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L89_C11_418550_2024-03-26_28050", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L89_C11_DAEJOO_2024_SILICON_ANODE_ORDER_REVISION_POSITIVE", "trigger_id": "R3L89_C11_DAEJOO_2024_STAGE2_ACTIONABLE_ORDER_REVISION_BRIDGE", "symbol": "078600", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 60, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "battery_material_order_revision_positive", "MFE_90D_pct": 115.0, "MAE_90D_pct": -3.03, "score_return_alignment_label": "battery_material_order_revision_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L89_C11_ONEJOON_2024_BATTERY_EQUIPMENT_FALSE_STAGE2", "trigger_id": "R3L89_C11_ONEJOON_2024_STAGE2_FALSE_POSITIVE_EQUIPMENT_ORDERBOOK_THEME", "symbol": "382840", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 20, "policy_or_regulatory_score": 5, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "battery_equipment_theme_false_stage2", "MFE_90D_pct": 12.64, "MAE_90D_pct": -24.22, "score_return_alignment_label": "battery_equipment_theme_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_equipment_orderbook_theme_counts_without_order_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L89_C11_JEO_2024_CNT_CONDUCTIVE_ADDITIVE_EVENT_CAP_4B", "trigger_id": "R3L89_C11_JEO_2024_STAGE4B_CNT_CONDUCTIVE_ADDITIVE_CAP", "symbol": "418550", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 20, "policy_or_regulatory_score": 5, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "CNT_material_event_cap_4B_guard", "MFE_90D_pct": 15.51, "MAE_90D_pct": -31.55, "score_return_alignment_label": "CNT_material_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_CNT_material_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": "89", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_ORDER_REVISION_BRIDGE_VS_EQUIPMENT_AND_CNT_THEME_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["battery_material_order_revision_positive", "battery_equipment_theme_false_stage2", "CNT_material_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_round = R3
completed_loop = 89
next_round = R4
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
