# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 101
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION_BRIDGE_VS_RESOURCE_TRADING_FALSE_STAGE2_AND_STRATEGIC_METAL_EVENT_CAP
loop_objective = priority1_to_50_fill_second_pass | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | strategic_resource_offtake_supply_execution_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R4_loop_101_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. C03 second-pass was the immediately preceding final artifact. After C03, C16 remains one of the thinnest Priority 1 buckets below the 50-row practical calibration zone. Since R4 loop98/99/100 were used locally for C17/C16/C15, this file uses R4 loop101 to avoid local round-loop collision.

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
scheduled_loop = 101
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C16 is a strategic resource policy/supply execution archetype. Policy is the map on the table; the signal is whether offtake, supply execution, volume, inventory/pass-through, margin and revision actually move on the road.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY = 30 rows in GitHub index / Priority 1
local C16 first pass added: 229640 / 047050 / 128660
top covered C16 symbols avoided: 006260, 009520, 011810, 025820, 036460, 000670
recent local Priority 0/1 artifacts accounted for: C08, C09, C01, C07, C06, C10, C14, C11, C02, C13, C19, C27, C12, C24, C28, C17, C23, C03, C16, C04, C05, C15, C18, C20, C25, C26, C22, C21, C03_second_pass
```

Selected rows avoid hard duplicates and add new C16 trigger families:

```text
024840 / Stage2-Actionable / 2024-04-12
001120 / Stage2-Actionable / 2024-05-21
012800 / Stage4B / 2024-05-21
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
| 024840 | atlas/symbol_profiles/024/024840.json | selected 2024 window clean after old 1997/1998/1999/2000/2001/2008/2009/2010/2011/2017 CA candidates |
| 001120 | atlas/symbol_profiles/001/001120.json | selected 2024 window clean after old 1996/1999/2006 CA candidates |
| 012800 | atlas/symbol_profiles/012/012800.json | selected 2024 window clean after old 1998/2008 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R4L101_C16_KBIMETAL_2024_COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION_POSITIVE | 024840 | 2024-04-12 | yes | 180 | yes | yes | true |
| R4L101_C16_LXINTL_2024_RESOURCE_TRADING_POLICY_FALSE_STAGE2 | 001120 | 2024-05-21 | yes | 180 | yes | yes | true |
| R4L101_C16_DAECHANG_2024_COPPER_STRATEGIC_METAL_EVENT_CAP_4B | 012800 | 2024-05-21 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION_BRIDGE | Positive Stage2 requires offtake, supply execution, customer quality, volume, inventory/pass-through, margin and revision bridge. |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | RESOURCE_TRADING_FALSE_STAGE2 | Resource trading/policy watch without offtake and volume/margin bridge can become false Stage2. |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | COPPER_STRATEGIC_METAL_EVENT_CAP_4B | Copper/strategic-metal event premium should route to 4B when offtake/supply/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R4L101_C16_KBIMETAL_2024_COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION_POSITIVE | 024840 | KBI메탈 | positive | Copper/cable supply-chain execution bridge produced extreme MFE with manageable early MAE. |
| R4L101_C16_LXINTL_2024_RESOURCE_TRADING_POLICY_FALSE_STAGE2 | 001120 | LX인터내셔널 | counterexample | Resource trading/policy watch had low forward MFE and meaningful MAE without offtake/margin bridge. |
| R4L101_C16_DAECHANG_2024_COPPER_STRATEGIC_METAL_EVENT_CAP_4B | 012800 | 대창 | counterexample / 4B | Copper/strategic-metal event premium capped after the May spike and then de-rated sharply. |

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
| KBI Metal copper/cable supply execution bridge | historical public/report proxy | true | true | shadow-only positive |
| LX International resource trading false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Daechang copper strategic-metal event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 024840 | atlas/ohlcv_tradable_by_symbol_year/024/024840/2024.csv | atlas/symbol_profiles/024/024840.json |
| 001120 | atlas/ohlcv_tradable_by_symbol_year/001/001120/2024.csv | atlas/symbol_profiles/001/001120.json |
| 012800 | atlas/ohlcv_tradable_by_symbol_year/012/012800/2024.csv | atlas/symbol_profiles/012/012800.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R4L101_C16_KBIMETAL_2024_STAGE2_ACTIONABLE_COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION | 024840 | Stage2-Actionable | 2024-04-12 | 1641 | positive | supply-chain execution bridge worked |
| R4L101_C16_LXINTL_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING_POLICY_WATCH | 001120 | Stage2-Actionable | 2024-05-21 | 34450 | counterexample | resource-trading policy false Stage2 |
| R4L101_C16_DAECHANG_2024_STAGE4B_COPPER_STRATEGIC_METAL_EVENT_CAP | 012800 | Stage4B | 2024-05-21 | 2175 | counterexample/4B | copper strategic-metal event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R4L101_C16_KBIMETAL_2024_STAGE2_ACTIONABLE_COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION | 1641 | 189.15 | -7.07 | 189.15 | -7.07 | 189.15 | -7.07 | 2024-05-21 | 4745 | -49.53 |
| R4L101_C16_LXINTL_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING_POLICY_WATCH | 34450 | 4.35 | -18.58 | 4.35 | -18.58 | 4.35 | -18.58 | 2024-05-21 | 35950 | -21.97 |
| R4L101_C16_DAECHANG_2024_STAGE4B_COPPER_STRATEGIC_METAL_EVENT_CAP | 2175 | 6.67 | -37.93 | 6.67 | -37.93 | 6.67 | -37.93 | 2024-05-21 | 2320 | -41.81 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C16 Stage2 needs offtake / supply execution / customer quality / volume / inventory-pass-through / margin / revision bridge |
| strategic_resource_offtake_supply_execution_guardrail | strengthen: strategic-resource/copper policy label alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing resource trading and copper strategic-metal premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C16 rows cannot promote without durable supply/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether strategic-resource narrative becomes offtake, supply execution, volume and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 024840 | good_stage2_with_later_watch | Copper/cable supply execution bridge produced extreme MFE, but later strategic-metal valuation watch remains necessary. |
| 001120 | bad_stage2 | Resource trading watch lacked offtake-volume-margin bridge and produced low MFE with meaningful MAE. |
| 012800 | good_4B | Copper/strategic-metal event premium peaked after the May spike and later de-rated. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 001120 resource trading false Stage2 | 0.96 | 0.96 | false Stage2 due missing offtake / volume / inventory / margin bridge |
| 012800 copper strategic-metal cap | 0.94 | 0.94 | good full-window 4B timing after copper strategic-metal event premium |
| 024840 copper cable supply bridge | n/a | n/a | positive Stage2, but later strategic-resource valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = offtake_or_margin_break_watch_only for 001120 / 012800
```

No hard 4C candidate is introduced in this C16 second-pass file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L4 strategic-resource policy supply cases, Stage2 requires verified offtake, supply execution, customer quality, volume conversion, inventory/pass-through, margin and revision bridge. Strategic-resource policy, copper, critical mineral, energy resource, trading beta or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
rule = C16 should split true offtake/supply-execution/margin positives from resource-trading false Stage2 and copper strategic-metal event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 66.72 | -21.19 | 0.67 | mixed; C16 second-pass supply-execution bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 66.72 | -21.19 | 0.67 | weaker C16 bridge split |
| P1 sector_specific_candidate_profile | L4 offtake/supply/margin bridge required | 2 | 96.75 | -12.82 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C16 bridge vs event-cap split | 2 | 96.75 | -12.82 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing strategic-resource themes as positive | 1 | 189.15 | -7.07 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 024840 supply execution bridge | 66 | Stage2-Watch | 82 | Stage2-Actionable | 189.15 | -7.07 | strategic_resource_supply_execution_positive_second_pass |
| 001120 resource trading false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 4.35 | -18.58 | resource_trading_false_stage2 |
| 012800 copper event cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 6.67 | -37.93 | copper_strategic_metal_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION_BRIDGE_VS_RESOURCE_TRADING_FALSE_STAGE2_AND_STRATEGIC_METAL_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "After C03 second-pass local supplementation, C16 remains one of the thinnest below-50 Priority 1 buckets. This second-pass run adds KBI Metal, LX International and Daechang while avoiding top-covered C16 symbols 006260, 009520, 011810, 025820, 036460, 000670 and prior local C16 additions 229640, 047050, 128660."}
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
residual_error_types_found: strategic_resource_supply_execution_positive_second_pass, resource_trading_false_stage2, copper_strategic_metal_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, strategic_resource_offtake_supply_execution_guardrail, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: priority1_second_pass_canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C16 strategic-resource policy supply second-pass bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,C16_requires_offtake_supply_execution_customer_volume_inventory_margin_revision_bridge,0,"C16 Stage2 should require offtake visibility, supply execution, customer quality, volume conversion, inventory/pass-through, margin and revision bridge, not strategic-resource/copper policy label alone","KBI Metal positive worked; LX International and Daechang event/watch rows failed positive-stage promotion","R4L101_C16_KBIMETAL_2024_STAGE2_ACTIONABLE_COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION|R4L101_C16_LXINTL_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING_POLICY_WATCH|R4L101_C16_DAECHANG_2024_STAGE4B_COPPER_STRATEGIC_METAL_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,cap_bridge_missing_resource_trading_and_copper_strategic_metal_event_premiums_as_4B_watch,0,"Resource-trading and strategic-metal premiums can peak before offtake, volume, inventory and margin bridge is proven","LX International had low MFE and meaningful MAE after May resource-supply spike; Daechang showed 4B event-cap behavior after May copper/strategic-metal premium","R4L101_C16_LXINTL_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING_POLICY_WATCH|R4L101_C16_DAECHANG_2024_STAGE4B_COPPER_STRATEGIC_METAL_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,block_positive_stage_when_strategic_resource_theme_has_high_or_persistent_MAE_without_supply_margin_bridge,0,"High or persistent MAE after bridge-missing C16 entries should block Stage2/Stage3 promotion unless offtake, supply execution and margin evidence survives","LX International MAE90=-18.58 and Daechang MAE90=-37.93","R4L101_C16_LXINTL_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING_POLICY_WATCH|R4L101_C16_DAECHANG_2024_STAGE4B_COPPER_STRATEGIC_METAL_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L101_C16_KBIMETAL_2024_COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION_POSITIVE", "symbol": "024840", "company_name": "KBI메탈", "round": "R4", "loop": "101", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION_BRIDGE_VS_RESOURCE_TRADING_FALSE_STAGE2_AND_STRATEGIC_METAL_EVENT_CAP", "case_type": "structural_success_with_later_strategic_metal_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R4L101_C16_KBIMETAL_2024_STAGE2_ACTIONABLE_COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Copper/cable strategic-resource supply execution bridge produced extreme 30D/90D MFE after the April copper-supply rerating base. C16 works only when strategic-resource policy is tied to offtake, supply execution, customer demand, volume, inventory/pass-through, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C16_positive_requires_offtake_supply_execution_customer_volume_margin_revision_bridge_not_copper_policy_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1997/1998/1999/2000/2001/2008/2009/2010/2011/2017 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R4L101_C16_LXINTL_2024_RESOURCE_TRADING_POLICY_FALSE_STAGE2", "symbol": "001120", "company_name": "LX인터내셔널", "round": "R4", "loop": "101", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION_BRIDGE_VS_RESOURCE_TRADING_FALSE_STAGE2_AND_STRATEGIC_METAL_EVENT_CAP", "case_type": "failed_rerating_resource_trading_policy_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R4L101_C16_LXINTL_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING_POLICY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Resource trading / strategic supply watch after the May spike had low forward MFE and then meaningful MAE. C16 Stage2 should not be awarded without offtake visibility, volume conversion, inventory/working-capital control, spread/pass-through, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_resource_trading_policy_watch_counts_without_offtake_volume_inventory_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1996/1999/2006 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R4L101_C16_DAECHANG_2024_COPPER_STRATEGIC_METAL_EVENT_CAP_4B", "symbol": "012800", "company_name": "대창", "round": "R4", "loop": "101", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION_BRIDGE_VS_RESOURCE_TRADING_FALSE_STAGE2_AND_STRATEGIC_METAL_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L101_C16_DAECHANG_2024_STAGE4B_COPPER_STRATEGIC_METAL_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Copper/strategic-metal event premium capped after the May spike and then de-rated sharply. C16 should route bridge-missing strategic-metal premiums to 4B unless offtake, supply contract, volume, inventory, pass-through, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_copper_strategic_metal_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1998/2008 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L101_C16_KBIMETAL_2024_STAGE2_ACTIONABLE_COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION", "case_id": "R4L101_C16_KBIMETAL_2024_COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION_POSITIVE", "symbol": "024840", "company_name": "KBI메탈", "round": "R4", "loop": "101", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION_BRIDGE_VS_RESOURCE_TRADING_FALSE_STAGE2_AND_STRATEGIC_METAL_EVENT_CAP", "sector": "copper_cable_strategic_resource_supply_execution", "primary_archetype": "offtake_supply_execution_customer_volume_margin_revision_bridge", "loop_objective": "priority1_to_50_fill_second_pass | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | strategic_resource_offtake_supply_execution_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-12", "entry_date": "2024-04-12", "entry_price": 1641.0, "evidence_available_at_that_date": "copper/cable strategic-resource supply-chain execution, customer demand, volume/pass-through and margin/revision bridge proxy after April copper breakout; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["offtake_proxy", "supply_execution_proxy", "customer_demand_proxy", "volume_conversion_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["extreme_MFE30", "extreme_MFE90", "manageable_initial_MAE"], "stage4b_evidence_fields": ["later_strategic_metal_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024840/2024.csv", "profile_path": "atlas/symbol_profiles/024/024840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 189.15, "MFE_90D_pct": 189.15, "MFE_180D_pct": 189.15, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -7.07, "MAE_90D_pct": -7.07, "MAE_180D_pct": -7.07, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-21", "peak_price": 4745.0, "drawdown_after_peak_pct": -49.53, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_strategic_metal_valuation_4B_watch_needed", "four_b_evidence_type": ["strategic_resource_supply_execution_bridge", "offtake_volume_margin", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_strategic_resource_supply_execution_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1997_1998_1999_2000_2001_2008_2009_2010_2011_2017_CA", "same_entry_group_id": "R4L101_C16_024840_2024-04-12_1641", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L101_C16_LXINTL_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING_POLICY_WATCH", "case_id": "R4L101_C16_LXINTL_2024_RESOURCE_TRADING_POLICY_FALSE_STAGE2", "symbol": "001120", "company_name": "LX인터내셔널", "round": "R4", "loop": "101", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION_BRIDGE_VS_RESOURCE_TRADING_FALSE_STAGE2_AND_STRATEGIC_METAL_EVENT_CAP", "sector": "resource_trading_strategic_supply_policy_watch", "primary_archetype": "resource_trading_watch_without_offtake_volume_inventory_margin_bridge", "loop_objective": "priority1_to_50_fill_second_pass | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | strategic_resource_offtake_supply_execution_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-21", "entry_date": "2024-05-21", "entry_price": 34450.0, "evidence_available_at_that_date": "resource trading / strategic-supply policy watch after May spike without confirmed offtake conversion, volume, inventory/working-capital control, spread/pass-through, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["resource_trading_watch", "strategic_supply_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "meaningful_MAE90", "offtake_volume_margin_bridge_missing"], "stage4c_evidence_fields": ["offtake_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001120/2024.csv", "profile_path": "atlas/symbol_profiles/001/001120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.35, "MFE_90D_pct": 4.35, "MFE_180D_pct": 4.35, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -18.58, "MAE_90D_pct": -18.58, "MAE_180D_pct": -18.58, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-21", "peak_price": 35950.0, "drawdown_after_peak_pct": -21.97, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "resource_trading_policy_watch_was_false_stage2_due_missing_offtake_volume_inventory_margin_revision_bridge", "four_b_evidence_type": ["resource_trading_supply_premium", "bridge_missing", "low_MFE_meaningful_MAE"], "four_c_protection_label": "offtake_or_margin_break_watch_only", "trigger_outcome_label": "bad_stage2_resource_trading_policy_watch_without_offtake_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_resource_trading_policy_watch_counts_without_offtake_volume_inventory_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1996_1999_2006_CA", "same_entry_group_id": "R4L101_C16_001120_2024-05-21_34450", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L101_C16_DAECHANG_2024_STAGE4B_COPPER_STRATEGIC_METAL_EVENT_CAP", "case_id": "R4L101_C16_DAECHANG_2024_COPPER_STRATEGIC_METAL_EVENT_CAP_4B", "symbol": "012800", "company_name": "대창", "round": "R4", "loop": "101", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION_BRIDGE_VS_RESOURCE_TRADING_FALSE_STAGE2_AND_STRATEGIC_METAL_EVENT_CAP", "sector": "copper_strategic_metal_event_premium", "primary_archetype": "copper_strategic_metal_event_cap_4B", "loop_objective": "priority1_to_50_fill_second_pass | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | strategic_resource_offtake_supply_execution_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-05-21", "entry_date": "2024-05-21", "entry_price": 2175.0, "evidence_available_at_that_date": "copper / strategic-metal event premium without confirmed offtake, supply contract, volume, inventory normalization, ASP/pass-through, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["copper_event", "strategic_metal_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "low_MFE90", "deep_MAE90", "offtake_margin_bridge_recheck"], "stage4c_evidence_fields": ["offtake_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012800/2024.csv", "profile_path": "atlas/symbol_profiles/012/012800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.67, "MFE_90D_pct": 6.67, "MFE_180D_pct": 6.67, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -37.93, "MAE_90D_pct": -37.93, "MAE_180D_pct": -37.93, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-21", "peak_price": 2320.0, "drawdown_after_peak_pct": -41.81, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing_copper_strategic_metal_event_cap_due_missing_offtake_supply_margin_bridge", "four_b_evidence_type": ["copper_strategic_metal_event_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "offtake_or_margin_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_copper_strategic_metal_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_copper_strategic_metal_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1998_2008_CA", "same_entry_group_id": "R4L101_C16_012800_2024-05-21_2175", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R4L101_C16_KBIMETAL_2024_COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION_POSITIVE", "trigger_id": "R4L101_C16_KBIMETAL_2024_STAGE2_ACTIONABLE_COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION", "symbol": "024840", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 40, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 65, "revision_score": 60, "relative_strength_score": 90, "customer_quality_score": 60, "policy_or_regulatory_score": 45, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "copper_cable_supply_execution_positive", "MFE_90D_pct": 189.15, "MAE_90D_pct": -7.07, "score_return_alignment_label": "strategic_resource_supply_execution_positive_second_pass", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R4L101_C16_LXINTL_2024_RESOURCE_TRADING_POLICY_FALSE_STAGE2", "trigger_id": "R4L101_C16_LXINTL_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING_POLICY_WATCH", "symbol": "001120", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 35, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "resource_trading_policy_false_stage2", "MFE_90D_pct": 4.35, "MAE_90D_pct": -18.58, "score_return_alignment_label": "resource_trading_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_resource_trading_policy_watch_counts_without_offtake_volume_inventory_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R4L101_C16_DAECHANG_2024_COPPER_STRATEGIC_METAL_EVENT_CAP_4B", "trigger_id": "R4L101_C16_DAECHANG_2024_STAGE4B_COPPER_STRATEGIC_METAL_EVENT_CAP", "symbol": "012800", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 25, "policy_or_regulatory_score": 40, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "copper_strategic_metal_event_cap_4B_guard", "MFE_90D_pct": 6.67, "MAE_90D_pct": -37.93, "score_return_alignment_label": "copper_strategic_metal_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_copper_strategic_metal_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "101", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_CABLE_OFFTAKE_SUPPLY_EXECUTION_BRIDGE_VS_RESOURCE_TRADING_FALSE_STAGE2_AND_STRATEGIC_METAL_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "strategic_resource_offtake_supply_execution_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["strategic_resource_supply_execution_positive_second_pass", "resource_trading_false_stage2", "copper_strategic_metal_event_cap_4B"], "loop_contribution_label": "priority1_second_pass_canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_loop = 101
completed_canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
coverage_scheduler_status = coverage_index_first
next_selection_rule = continue second-pass Priority 1 fill; after C16 local second pass, re-evaluate C04/C05/C15/C18/C20/C25/C26/C22/C21/C03 with local supplements
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
