# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_ENERGY_TRADING_RESOURCE_FALSE_STAGE2_AND_ALUMINUM_EVENT_CAP
loop_objective = priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | strategic_resource_offtake_supply_execution_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R4_loop_99_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. C03 was the immediately preceding Priority 1 artifact, so this run moves to the next Priority 1 gap. C16 still needs 20 rows to reach the 50-row practical calibration zone. Because R4 loop98 was used locally for C17, this file uses R4 loop99 to avoid local round-loop collision.

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
strategic_resource_offtake_supply_execution_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R4
scheduled_loop = 99
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C16 is a strategic resource policy / supply execution archetype. Policy is the map; the investable signal is whether offtake, supply execution, export/customer demand, volume, inventory/pass-through, margin and revision actually move along the road.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY = 30 rows / Priority 1
top covered C16 symbols avoided: 006260, 009520, 011810, 025820, 036460, 000670
recent local Priority 0/1 artifacts accounted for: C08, C09, C01, C07, C06, C10, C14, C11, C02, C13, C19, C27, C12, C24, C28, C17, C23, C03
```

Selected rows avoid hard duplicates and add new C16 trigger families:

```text
229640 / Stage2-Actionable / 2024-04-22
047050 / Stage2-Actionable / 2024-06-14
128660 / Stage4B / 2024-05-03
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
| 229640 | atlas/symbol_profiles/229/229640.json | no corporate-action candidate |
| 047050 | atlas/symbol_profiles/047/047050.json | selected 2024 window clean after old 2001/2003/2023 CA candidates |
| 128660 | atlas/symbol_profiles/128/128660.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R4L99_C16_LSECOENERGY_2024_CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION_POSITIVE | 229640 | 2024-04-22 | yes | 180 | yes | yes | true |
| R4L99_C16_POSCOINTL_2024_ENERGY_TRADING_RESOURCE_FALSE_STAGE2 | 047050 | 2024-06-14 | yes | 180 | yes | yes | true |
| R4L99_C16_PJMETAL_2024_ALUMINUM_STRATEGIC_METAL_EVENT_CAP_4B | 128660 | 2024-05-03 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION_BRIDGE | Positive Stage2 requires offtake, supply execution, customer quality, volume, margin and revision bridge. |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | ENERGY_TRADING_RESOURCE_FALSE_STAGE2 | Energy/resource trading watch without offtake and volume/margin bridge can become false Stage2. |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | ALUMINUM_EVENT_CAP_4B | Aluminum/strategic-metal premium should route to 4B when offtake/supply/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R4L99_C16_LSECOENERGY_2024_CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION_POSITIVE | 229640 | LS에코에너지 | positive | Critical-mineral/cable supply-chain execution bridge produced very strong MFE with shallow initial MAE. |
| R4L99_C16_POSCOINTL_2024_ENERGY_TRADING_RESOURCE_FALSE_STAGE2 | 047050 | 포스코인터내셔널 | counterexample | Energy/resource trading watch had low MFE and high MAE without offtake/volume/margin bridge. |
| R4L99_C16_PJMETAL_2024_ALUMINUM_STRATEGIC_METAL_EVENT_CAP_4B | 128660 | 피제이메탈 | counterexample / 4B | Aluminum strategic-metal event premium capped after the May spike and later de-rated. |

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
| LS Eco Energy critical-mineral/cable supply-chain execution bridge | historical public/report proxy | true | true | shadow-only positive |
| POSCO International energy/resource trading false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| PJ Metal aluminum strategic-metal event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 229640 | atlas/ohlcv_tradable_by_symbol_year/229/229640/2024.csv | atlas/symbol_profiles/229/229640.json |
| 047050 | atlas/ohlcv_tradable_by_symbol_year/047/047050/2024.csv | atlas/symbol_profiles/047/047050.json |
| 128660 | atlas/ohlcv_tradable_by_symbol_year/128/128660/2024.csv | atlas/symbol_profiles/128/128660.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R4L99_C16_LSECOENERGY_2024_STAGE2_ACTIONABLE_CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION | 229640 | Stage2-Actionable | 2024-04-22 | 19600 | positive | supply-chain execution bridge worked |
| R4L99_C16_POSCOINTL_2024_STAGE2_FALSE_POSITIVE_ENERGY_TRADING_RESOURCE_WATCH | 047050 | Stage2-Actionable | 2024-06-14 | 68300 | counterexample | energy/resource false Stage2 |
| R4L99_C16_PJMETAL_2024_STAGE4B_ALUMINUM_STRATEGIC_METAL_EVENT_CAP | 128660 | Stage4B | 2024-05-03 | 4870 | counterexample/4B | aluminum strategic-metal event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R4L99_C16_LSECOENERGY_2024_STAGE2_ACTIONABLE_CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION | 19600 | 128.06 | -3.83 | 128.06 | -3.83 | 128.06 | -3.83 | 2024-05-22 | 44700 | -51.23 |
| R4L99_C16_POSCOINTL_2024_STAGE2_FALSE_POSITIVE_ENERGY_TRADING_RESOURCE_WATCH | 68300 | 6.59 | -8.64 | 6.59 | -23.43 | 6.59 | -23.43 | 2024-06-14 | 72800 | -28.16 |
| R4L99_C16_PJMETAL_2024_STAGE4B_ALUMINUM_STRATEGIC_METAL_EVENT_CAP | 4870 | 10.68 | -15.91 | 10.68 | -28.54 | 10.68 | -34.09 | 2024-05-21 | 5390 | -40.45 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C16 Stage2 needs offtake / supply execution / customer quality / volume / inventory-pass-through / margin / revision bridge |
| strategic_resource_offtake_supply_execution_guardrail | strengthen: strategic-resource policy label alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing energy/resource and metal-event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C16 rows cannot promote without durable supply/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether policy/supply narrative becomes offtake, execution, volume and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 229640 | good_stage2_with_later_watch | Supply-chain execution bridge produced very strong MFE and shallow early MAE, but later valuation watch remains necessary. |
| 047050 | bad_stage2 | Energy/resource trading watch lacked offtake-volume-margin bridge and produced low MFE with meaningful MAE. |
| 128660 | good_4B | Aluminum/strategic-metal event premium peaked after the May spike and later de-rated. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 047050 energy/resource false Stage2 | 0.94 | 0.94 | false Stage2 due missing offtake / volume / inventory / margin bridge |
| 128660 aluminum strategic-metal cap | 0.90 | 0.90 | good full-window 4B timing after aluminum strategic-metal event premium |
| 229640 critical-mineral supply bridge | n/a | n/a | positive Stage2, but later strategic-resource valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 047050 / 128660
```

No hard 4C candidate is introduced in this C16 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L4 strategic-resource policy supply cases, Stage2 requires verified offtake, supply execution, customer quality, volume conversion, inventory/pass-through, margin and revision bridge. Strategic-resource policy, critical mineral, energy resource, aluminum, copper, rare-earth or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
rule = C16 should split true offtake/supply-execution/margin positives from energy-resource false Stage2 and strategic-metal event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 48.44 | -18.60 | 0.67 | mixed; C16 supply-execution bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 48.44 | -18.60 | 0.67 | weaker C16 bridge split |
| P1 sector_specific_candidate_profile | L4 offtake/supply/margin bridge required | 2 | 67.33 | -13.63 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C16 bridge vs event-cap split | 2 | 67.33 | -13.63 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing strategic-resource themes as positive | 1 | 128.06 | -3.83 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 229640 supply-chain execution bridge | 66 | Stage2-Watch | 81 | Stage2-Actionable | 128.06 | -3.83 | strategic_resource_supply_execution_positive |
| 047050 energy/resource false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 6.59 | -23.43 | energy_resource_false_stage2 |
| 128660 aluminum event cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 10.68 | -28.54 | aluminum_strategic_metal_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_ENERGY_TRADING_RESOURCE_FALSE_STAGE2_AND_ALUMINUM_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C16 is the next Priority 1 archetype after C03 and still needs 20 rows to reach 50 in the No-Repeat index. This run adds LS Eco Energy, POSCO International, and PJ Metal while avoiding top-covered C16 symbols 006260, 009520, 011810, 025820, 036460, and 000670."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, strategic_resource_offtake_supply_execution_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: strategic_resource_supply_execution_positive, energy_resource_false_stage2, aluminum_strategic_metal_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, strategic_resource_offtake_supply_execution_guardrail, high_MAE_guardrail
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
- C16 strategic-resource policy supply bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,C16_requires_offtake_supply_execution_customer_volume_margin_revision_bridge,0,"C16 Stage2 should require offtake visibility, supply execution, customer quality, volume conversion, inventory/pass-through, margin and revision bridge, not strategic-resource policy label alone","LS Eco Energy positive worked; POSCO International and PJ Metal event/watch rows failed positive-stage promotion","R4L99_C16_LSECOENERGY_2024_STAGE2_ACTIONABLE_CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION|R4L99_C16_POSCOINTL_2024_STAGE2_FALSE_POSITIVE_ENERGY_TRADING_RESOURCE_WATCH|R4L99_C16_PJMETAL_2024_STAGE4B_ALUMINUM_STRATEGIC_METAL_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,cap_bridge_missing_energy_resource_and_metal_event_premiums_as_4B_watch,0,"Energy/resource trading and strategic-metal premiums can peak before offtake, volume, inventory and margin bridge is proven","POSCO International had low MFE and high MAE after June resource-supply spike; PJ Metal showed 4B event-cap behavior after May aluminum/strategic-metal premium","R4L99_C16_POSCOINTL_2024_STAGE2_FALSE_POSITIVE_ENERGY_TRADING_RESOURCE_WATCH|R4L99_C16_PJMETAL_2024_STAGE4B_ALUMINUM_STRATEGIC_METAL_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,block_positive_stage_when_strategic_resource_theme_has_high_or_persistent_MAE_without_supply_margin_bridge,0,"High or persistent MAE after bridge-missing C16 entries should block Stage2/Stage3 promotion unless offtake, supply execution and margin evidence survives","POSCO International MAE90=-23.43 and PJ Metal MAE90=-28.54","R4L99_C16_POSCOINTL_2024_STAGE2_FALSE_POSITIVE_ENERGY_TRADING_RESOURCE_WATCH|R4L99_C16_PJMETAL_2024_STAGE4B_ALUMINUM_STRATEGIC_METAL_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L99_C16_LSECOENERGY_2024_CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION_POSITIVE", "symbol": "229640", "company_name": "LS에코에너지", "round": "R4", "loop": "99", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_ENERGY_TRADING_RESOURCE_FALSE_STAGE2_AND_ALUMINUM_EVENT_CAP", "case_type": "structural_success_with_later_strategic_resource_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R4L99_C16_LSECOENERGY_2024_STAGE2_ACTIONABLE_CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Critical-mineral / cable supply-chain execution bridge produced very strong 30D/90D/180D MFE with shallow early MAE after the April supply-chain rerating base. C16 works when strategic-resource policy is tied to offtake, production/export execution, customer quality, volume, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C16_positive_requires_offtake_supply_execution_customer_volume_margin_revision_bridge_not_resource_policy_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R4L99_C16_POSCOINTL_2024_ENERGY_TRADING_RESOURCE_FALSE_STAGE2", "symbol": "047050", "company_name": "포스코인터내셔널", "round": "R4", "loop": "99", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_ENERGY_TRADING_RESOURCE_FALSE_STAGE2_AND_ALUMINUM_EVENT_CAP", "case_type": "failed_rerating_energy_resource_trading_supply_execution_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R4L99_C16_POSCOINTL_2024_STAGE2_FALSE_POSITIVE_ENERGY_TRADING_RESOURCE_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Energy/resource trading and strategic supply watch after the June spike had low forward MFE and meaningful MAE. C16 Stage2 should not be awarded without offtake visibility, volume conversion, inventory/working-capital control, spread/pass-through, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_energy_resource_watch_counts_without_offtake_volume_inventory_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2001/2003/2023 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R4L99_C16_PJMETAL_2024_ALUMINUM_STRATEGIC_METAL_EVENT_CAP_4B", "symbol": "128660", "company_name": "피제이메탈", "round": "R4", "loop": "99", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_ENERGY_TRADING_RESOURCE_FALSE_STAGE2_AND_ALUMINUM_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L99_C16_PJMETAL_2024_STAGE4B_ALUMINUM_STRATEGIC_METAL_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Aluminum / strategic metal event premium capped after the May spike and then de-rated. C16 should route bridge-missing metal-policy premiums to 4B unless offtake, supply contract, volume, inventory, pass-through, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_aluminum_strategic_metal_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L99_C16_LSECOENERGY_2024_STAGE2_ACTIONABLE_CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION", "case_id": "R4L99_C16_LSECOENERGY_2024_CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION_POSITIVE", "symbol": "229640", "company_name": "LS에코에너지", "round": "R4", "loop": "99", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_ENERGY_TRADING_RESOURCE_FALSE_STAGE2_AND_ALUMINUM_EVENT_CAP", "sector": "critical_mineral_cable_supply_chain_execution", "primary_archetype": "offtake_supply_execution_customer_volume_margin_revision_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | strategic_resource_offtake_supply_execution_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-22", "entry_date": "2024-04-22", "entry_price": 19600.0, "evidence_available_at_that_date": "critical-mineral / power-cable supply-chain execution, export/customer demand, volume and margin/revision bridge proxy after April rerating base; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["offtake_proxy", "supply_execution_proxy", "export_customer_quality_proxy", "volume_conversion_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["very_strong_MFE30", "very_strong_MFE90", "shallow_initial_MAE"], "stage4b_evidence_fields": ["later_strategic_resource_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/229/229640/2024.csv", "profile_path": "atlas/symbol_profiles/229/229640.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 128.06, "MFE_90D_pct": 128.06, "MFE_180D_pct": 128.06, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.83, "MAE_90D_pct": -3.83, "MAE_180D_pct": -3.83, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-22", "peak_price": 44700.0, "drawdown_after_peak_pct": -51.23, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_strategic_resource_valuation_4B_watch_needed", "four_b_evidence_type": ["strategic_resource_supply_execution_bridge", "offtake_volume_margin", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_strategic_resource_supply_execution_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R4L99_C16_229640_2024-04-22_19600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L99_C16_POSCOINTL_2024_STAGE2_FALSE_POSITIVE_ENERGY_TRADING_RESOURCE_WATCH", "case_id": "R4L99_C16_POSCOINTL_2024_ENERGY_TRADING_RESOURCE_FALSE_STAGE2", "symbol": "047050", "company_name": "포스코인터내셔널", "round": "R4", "loop": "99", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_ENERGY_TRADING_RESOURCE_FALSE_STAGE2_AND_ALUMINUM_EVENT_CAP", "sector": "energy_resource_trading_strategic_supply_watch", "primary_archetype": "energy_resource_watch_without_offtake_volume_inventory_margin_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | strategic_resource_offtake_supply_execution_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-14", "entry_date": "2024-06-14", "entry_price": 68300.0, "evidence_available_at_that_date": "energy/resource trading and strategic supply watch after June spike without confirmed offtake conversion, volume, inventory/working-capital control, spread/pass-through, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["energy_resource_watch", "strategic_supply_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "high_MAE90", "offtake_volume_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047050/2024.csv", "profile_path": "atlas/symbol_profiles/047/047050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.59, "MFE_90D_pct": 6.59, "MFE_180D_pct": 6.59, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -8.64, "MAE_90D_pct": -23.43, "MAE_180D_pct": -23.43, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 72800.0, "drawdown_after_peak_pct": -28.16, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "energy_resource_trading_watch_was_false_stage2_due_missing_offtake_volume_inventory_margin_revision_bridge", "four_b_evidence_type": ["energy_resource_supply_premium", "bridge_missing", "low_MFE_high_MAE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_energy_resource_trading_watch_without_offtake_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_energy_resource_watch_counts_without_offtake_volume_inventory_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2001_2003_2023_CA", "same_entry_group_id": "R4L99_C16_047050_2024-06-14_68300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L99_C16_PJMETAL_2024_STAGE4B_ALUMINUM_STRATEGIC_METAL_EVENT_CAP", "case_id": "R4L99_C16_PJMETAL_2024_ALUMINUM_STRATEGIC_METAL_EVENT_CAP_4B", "symbol": "128660", "company_name": "피제이메탈", "round": "R4", "loop": "99", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_ENERGY_TRADING_RESOURCE_FALSE_STAGE2_AND_ALUMINUM_EVENT_CAP", "sector": "aluminum_strategic_metal_event_premium", "primary_archetype": "aluminum_strategic_metal_event_cap_4B", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | strategic_resource_offtake_supply_execution_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-05-03", "entry_date": "2024-05-03", "entry_price": 4870.0, "evidence_available_at_that_date": "aluminum / strategic metal event premium without confirmed offtake, supply contract, volume, inventory normalization, ASP/pass-through, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["aluminum_event", "strategic_metal_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "high_MAE90", "offtake_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/128/128660/2024.csv", "profile_path": "atlas/symbol_profiles/128/128660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.68, "MFE_90D_pct": 10.68, "MFE_180D_pct": 10.68, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.91, "MAE_90D_pct": -28.54, "MAE_180D_pct": -34.09, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-21", "peak_price": 5390.0, "drawdown_after_peak_pct": -40.45, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "good_full_window_4B_timing_aluminum_strategic_metal_event_cap_due_missing_offtake_supply_margin_bridge", "four_b_evidence_type": ["aluminum_strategic_metal_event_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_aluminum_strategic_metal_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_aluminum_strategic_metal_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R4L99_C16_128660_2024-05-03_4870", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R4L99_C16_LSECOENERGY_2024_CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION_POSITIVE", "trigger_id": "R4L99_C16_LSECOENERGY_2024_STAGE2_ACTIONABLE_CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION", "symbol": "229640", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 85, "customer_quality_score": 65, "policy_or_regulatory_score": 50, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 81, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "critical_mineral_supply_chain_execution_positive", "MFE_90D_pct": 128.06, "MAE_90D_pct": -3.83, "score_return_alignment_label": "strategic_resource_supply_execution_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R4L99_C16_POSCOINTL_2024_ENERGY_TRADING_RESOURCE_FALSE_STAGE2", "trigger_id": "R4L99_C16_POSCOINTL_2024_STAGE2_FALSE_POSITIVE_ENERGY_TRADING_RESOURCE_WATCH", "symbol": "047050", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 35, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "energy_resource_trading_false_stage2", "MFE_90D_pct": 6.59, "MAE_90D_pct": -23.43, "score_return_alignment_label": "energy_resource_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_energy_resource_watch_counts_without_offtake_volume_inventory_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R4L99_C16_PJMETAL_2024_ALUMINUM_STRATEGIC_METAL_EVENT_CAP_4B", "trigger_id": "R4L99_C16_PJMETAL_2024_STAGE4B_ALUMINUM_STRATEGIC_METAL_EVENT_CAP", "symbol": "128660", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 25, "policy_or_regulatory_score": 40, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "aluminum_strategic_metal_event_cap_4B_guard", "MFE_90D_pct": 10.68, "MAE_90D_pct": -28.54, "score_return_alignment_label": "aluminum_strategic_metal_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_aluminum_strategic_metal_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "99", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CRITICAL_MINERAL_CABLE_SUPPLY_CHAIN_EXECUTION_BRIDGE_VS_ENERGY_TRADING_RESOURCE_FALSE_STAGE2_AND_ALUMINUM_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "strategic_resource_offtake_supply_execution_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["strategic_resource_supply_execution_positive", "energy_resource_false_stage2", "aluminum_strategic_metal_event_cap_4B"], "loop_contribution_label": "priority1_canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C16 rows need explicit offtake visibility, supply execution, customer quality, volume conversion, inventory/pass-through, margin and revision bridge before positive promotion.
- In C16, bridge-missing strategic-resource event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C16 strategic-resource policy supply rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R4
completed_loop = 99
completed_canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
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
