# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE_VS_RARE_EARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_NICKEL_TRADING_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R4_loop_95_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
```

This file is the corrected final output for this execution. The scheduler state after R3 loop 95 is R4 / loop 95. R4 is the L4 materials/spread/resource round, and this run fills C16 strategic resource policy/supply rather than repeating the immediately preceding R4 loop 94 C17 chemical margin-spread file.

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
scheduled_round = R4
scheduled_loop = 95
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
round_sector_consistency = pass
computed_next_round = R5
computed_next_loop = 95
```

C16 is a strategic-resource bridge archetype. A rare-earth or lithium headline is only a mining map; the ore becomes investable evidence only when supply, offtake, customer quality, inventory spread, shipment volume, margin and revision are visible.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY = 36 rows / 23 symbols / good-bad Stage2 14-9 / 4B-4C 2-0
top covered symbols include 047400(6), 005490(3), 012320(3), 001570(2), 081150(2), 101670(2)
previous R4 loop-90 C15 symbols avoided: 024840, 018470, 006110
previous R4 loop-91 C17 symbols avoided: 010060, 007690, 298000
previous R4 loop-92 C16 symbols avoided: 006260, 012800, 025820
previous R4 loop-93 C15 symbols avoided: 003030, 016380, 024060
previous R4 loop-94 C17 symbols avoided: 002380, 011170, 004090
previous R3 loop-95 C13 symbols avoided: 014820, 093370, 450080
```

Selected rows avoid hard duplicates and top repeated C16 symbols:

```text
103140 / Stage2-Actionable / 2024-03-07
075970 / Stage2-Actionable / 2024-01-23
011810 / Stage4B / 2024-02-16
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
| 075970 | atlas/symbol_profiles/075/075970.json | selected 2024 window clean after old 2006/2008 CA candidates |
| 011810 | atlas/symbol_profiles/011/011810.json | selected 2024 window clean after old CA/name-history candidates; later inactive-like caveat after 2025 |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R4L95_C16_POONGSAN_2024_COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_POSITIVE | 103140 | 2024-03-07 | yes | 180 | yes | yes | true |
| R4L95_C16_DONGKUKRNS_2024_RARE_EARTH_POLICY_FALSE_STAGE2 | 075970 | 2024-01-23 | yes | 180 | yes | yes | true |
| R4L95_C16_STX_2024_LITHIUM_NICKEL_TRADING_RESOURCE_EVENT_CAP_4B | 011810 | 2024-02-16 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE | Positive Stage2 requires resource price spread, supply/order visibility, customer quality, inventory/volume and margin/revision bridge. |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | RARE_EARTH_POLICY_FALSE_STAGE2 | Rare-earth/resource policy watch without offtake or margin bridge can become false Stage2. |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | LITHIUM_NICKEL_TRADING_EVENT_CAP_4B | Lithium/nickel trading event premium should route to 4B when offtake/shipment/financing bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R4L95_C16_POONGSAN_2024_COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_POSITIVE | 103140 | 풍산 | positive | Copper/nonferrous and defense-material margin bridge produced strong MFE with shallow early MAE. |
| R4L95_C16_DONGKUKRNS_2024_RARE_EARTH_POLICY_FALSE_STAGE2 | 075970 | 동국알앤에스 | counterexample | Rare-earth policy watch had temporary MFE but no durable supply/order/margin bridge. |
| R4L95_C16_STX_2024_LITHIUM_NICKEL_TRADING_RESOURCE_EVENT_CAP_4B | 011810 | STX | counterexample / 4B | Lithium/nickel trading premium capped on the February spike and then de-rated sharply. |

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
| Poongsan copper/defense material supply-margin bridge | historical public/report proxy | true | true | shadow-only positive |
| Dongkuk R&S rare-earth policy false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| STX lithium/nickel resource-trading event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 103140 | atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv | atlas/symbol_profiles/103/103140.json |
| 075970 | atlas/ohlcv_tradable_by_symbol_year/075/075970/2024.csv | atlas/symbol_profiles/075/075970.json |
| 011810 | atlas/ohlcv_tradable_by_symbol_year/011/011810/2024.csv | atlas/symbol_profiles/011/011810.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R4L95_C16_POONGSAN_2024_STAGE2_ACTIONABLE_COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE | 103140 | Stage2-Actionable | 2024-03-07 | 46100 | positive | copper/defense material supply-margin bridge worked |
| R4L95_C16_DONGKUKRNS_2024_STAGE2_FALSE_POSITIVE_RARE_EARTH_POLICY_SUPPLY_WATCH | 075970 | Stage2-Actionable | 2024-01-23 | 3605 | counterexample | rare-earth policy false Stage2 |
| R4L95_C16_STX_2024_STAGE4B_LITHIUM_NICKEL_TRADING_RESOURCE_EVENT_CAP | 011810 | Stage4B | 2024-02-16 | 10950 | counterexample/4B | lithium/nickel trading resource event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R4L95_C16_POONGSAN_2024_STAGE2_ACTIONABLE_COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE | 46100 | 46.42 | -3.90 | 71.15 | -3.90 | 71.15 | -3.90 | 2024-05-14 | 78900 | -27.25 |
| R4L95_C16_DONGKUKRNS_2024_STAGE2_FALSE_POSITIVE_RARE_EARTH_POLICY_SUPPLY_WATCH | 3605 | 13.18 | -6.80 | 13.18 | -13.04 | 13.18 | -22.33 | 2024-01-23 | 4080 | -31.62 |
| R4L95_C16_STX_2024_STAGE4B_LITHIUM_NICKEL_TRADING_RESOURCE_EVENT_CAP | 10950 | 8.68 | -23.29 | 8.68 | -34.52 | 8.68 | -39.73 | 2024-02-16 | 11900 | -44.54 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C16 Stage2 needs resource price spread / supply-order / customer / inventory-volume / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing resource policy or trading event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE strategic-resource rows cannot promote without durable supply/margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether strategic-resource narrative becomes supply/order/margin.

| symbol | stage quality | explanation |
|---|---|---|
| 103140 | good_stage2_with_later_watch | Copper and defense-material bridge produced strong MFE with shallow MAE. |
| 075970 | bad_stage2 | Rare-earth policy watch lacked order/margin bridge and became a one-day event premium. |
| 011810 | good_4B | Lithium/nickel trading premium capped on the February spike and then drew down deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 075970 rare-earth false Stage2 | 0.88 | 0.88 | false Stage2 due missing supply/order/margin bridge |
| 011810 lithium/nickel trading cap | 0.92 | 0.92 | good full-window 4B timing after February resource-trading spike |
| 103140 copper material bridge | n/a | n/a | positive Stage2, but later copper/material valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 075970 / 011810
```

No hard 4C candidate is proposed. R4 loop 95 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L4 strategic-resource policy/supply cases, Stage2 requires verified resource price pass-through, supply/offtake/order visibility, customer quality, inventory spread, shipment volume, margin, or revision bridge. Rare-earth, lithium, nickel, copper, strategic resource, policy, trading or supply-chain label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
rule = C16 should split true resource-price/supply/order/margin positives from rare-earth policy false Stage2 and lithium/nickel event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 31.00 | -17.15 | 0.67 | mixed; C16 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 31.00 | -17.15 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L4 supply/order/margin bridge required | 2 | 42.17 | -8.47 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C16 bridge vs event-cap split | 2 | 42.17 | -8.47 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing strategic-resource themes as positive | 1 | 71.15 | -3.90 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 103140 copper/material bridge | 66 | Stage2-Watch | 77 | Stage2-Actionable | 71.15 | -3.90 | copper_defense_material_supply_margin_positive |
| 075970 rare-earth false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 13.18 | -13.04 | rare_earth_policy_supply_false_stage2 |
| 011810 lithium/nickel cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 8.68 | -34.52 | lithium_nickel_resource_trading_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE_VS_RARE_EARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_NICKEL_TRADING_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C16 Poongsan copper/defense material supply-margin positive, Dongkuk R&S rare-earth policy false Stage2, and STX lithium/nickel resource-trading event-cap 4B split while avoiding top repeated C16 and previous R4/R3 loop symbols."}
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
residual_error_types_found: copper_defense_material_supply_margin_positive, rare_earth_policy_supply_false_stage2, lithium_nickel_resource_trading_event_cap_4B
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
- C16 strategic resource policy/supply bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,C16_requires_resource_price_supply_order_customer_margin_revision_bridge,0,"C16 Stage2 should require resource price pass-through, supply/offtake/order visibility, customer quality, inventory spread, shipment volume, margin, or revision bridge, not strategic-resource/policy/rare-earth label alone","Poongsan positive worked; Dongkuk R&S and STX event/watch rows failed positive-stage promotion","R4L95_C16_POONGSAN_2024_STAGE2_ACTIONABLE_COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE|R4L95_C16_DONGKUKRNS_2024_STAGE2_FALSE_POSITIVE_RARE_EARTH_POLICY_SUPPLY_WATCH|R4L95_C16_STX_2024_STAGE4B_LITHIUM_NICKEL_TRADING_RESOURCE_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,cap_bridge_missing_resource_policy_and_trading_event_premiums_as_4B_watch,0,"Strategic-resource, rare-earth, lithium/nickel and trading event premiums can peak before offtake, shipment and margin bridge is proven","Dongkuk R&S had temporary rare-earth policy MFE then drawdown; STX showed 4B event-cap behavior after February resource spike","R4L95_C16_DONGKUKRNS_2024_STAGE2_FALSE_POSITIVE_RARE_EARTH_POLICY_SUPPLY_WATCH|R4L95_C16_STX_2024_STAGE4B_LITHIUM_NICKEL_TRADING_RESOURCE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,block_positive_stage_when_resource_policy_theme_has_high_or_persistent_MAE_without_supply_margin_bridge,0,"High or persistent MAE after bridge-missing strategic-resource entries should block Stage2/Stage3 promotion unless supply, offtake, customer and margin evidence survives","Dongkuk R&S MAE180=-22.33 and STX MAE90=-34.52","R4L95_C16_DONGKUKRNS_2024_STAGE2_FALSE_POSITIVE_RARE_EARTH_POLICY_SUPPLY_WATCH|R4L95_C16_STX_2024_STAGE4B_LITHIUM_NICKEL_TRADING_RESOURCE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L95_C16_POONGSAN_2024_COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_POSITIVE", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": "95", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE_VS_RARE_EARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_NICKEL_TRADING_EVENT_CAP", "case_type": "structural_success_with_later_copper_material_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R4L95_C16_POONGSAN_2024_STAGE2_ACTIONABLE_COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Copper/nonferrous material price, defense-material demand and supply-margin bridge produced strong 30D/90D/180D MFE with shallow early MAE. C16 works when strategic resource narrative maps into realized commodity price spread, customer/order quality, volume, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C16_positive_requires_resource_price_supply_order_margin_revision_bridge_not_resource_policy_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R4L95_C16_DONGKUKRNS_2024_RARE_EARTH_POLICY_FALSE_STAGE2", "symbol": "075970", "company_name": "동국알앤에스", "round": "R4", "loop": "95", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE_VS_RARE_EARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_NICKEL_TRADING_EVENT_CAP", "case_type": "failed_rerating_rare_earth_policy_supply_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R4L95_C16_DONGKUKRNS_2024_STAGE2_FALSE_POSITIVE_RARE_EARTH_POLICY_SUPPLY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Rare-earth / refractory material policy-supply watch had only temporary MFE and then drifted down without order, ASP, inventory or margin bridge. C16 Stage2 should not be awarded without confirmed strategic-resource supply contract, customer visibility, price pass-through, inventory spread, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_rare_earth_policy_watch_counts_without_supply_order_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2006/2008 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R4L95_C16_STX_2024_LITHIUM_NICKEL_TRADING_RESOURCE_EVENT_CAP_4B", "symbol": "011810", "company_name": "STX", "round": "R4", "loop": "95", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE_VS_RARE_EARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_NICKEL_TRADING_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L95_C16_STX_2024_STAGE4B_LITHIUM_NICKEL_TRADING_RESOURCE_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Lithium/nickel/resource-trading event premium capped on the February spike and then suffered deep MAE. C16 should route bridge-missing resource-trading event premiums to 4B unless confirmed offtake, shipment volume, trading margin, financing and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_lithium_nickel_resource_trading_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old corporate-action/name-history candidates; issuer later inactive-like after 2025 but 2024 180D window remains usable. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L95_C16_POONGSAN_2024_STAGE2_ACTIONABLE_COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE", "case_id": "R4L95_C16_POONGSAN_2024_COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_POSITIVE", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": "95", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE_VS_RARE_EARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_NICKEL_TRADING_EVENT_CAP", "sector": "copper_nonferrous_defense_material_supply_margin", "primary_archetype": "resource_price_supply_order_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-07", "entry_date": "2024-03-07", "entry_price": 46100.0, "evidence_available_at_that_date": "copper/nonferrous price spread, defense-material customer demand, inventory and supply margin bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["resource_price_spread_proxy", "defense_material_order_proxy", "inventory_spread_proxy", "customer_quality_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "strong_MFE180", "shallow_MAE90"], "stage4b_evidence_fields": ["later_copper_material_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 46.42, "MFE_90D_pct": 71.15, "MFE_180D_pct": 71.15, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.9, "MAE_90D_pct": -3.9, "MAE_180D_pct": -3.9, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-14", "peak_price": 78900.0, "drawdown_after_peak_pct": -27.25, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_copper_material_valuation_4B_watch_needed", "four_b_evidence_type": ["resource_price_spread", "defense_material_order_bridge", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_copper_defense_material_supply_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R4L95_C16_103140_2024-03-07_46100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L95_C16_DONGKUKRNS_2024_STAGE2_FALSE_POSITIVE_RARE_EARTH_POLICY_SUPPLY_WATCH", "case_id": "R4L95_C16_DONGKUKRNS_2024_RARE_EARTH_POLICY_FALSE_STAGE2", "symbol": "075970", "company_name": "동국알앤에스", "round": "R4", "loop": "95", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE_VS_RARE_EARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_NICKEL_TRADING_EVENT_CAP", "sector": "rare_earth_refractory_policy_supply_watch", "primary_archetype": "rare_earth_policy_watch_without_supply_order_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-23", "entry_date": "2024-01-23", "entry_price": 3605.0, "evidence_available_at_that_date": "rare-earth/refractory material policy-supply watch without confirmed supply contract, customer order, price pass-through or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["rare_earth_policy_watch", "strategic_resource_supply_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["temporary_MFE", "order_margin_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/075/075970/2024.csv", "profile_path": "atlas/symbol_profiles/075/075970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.18, "MFE_90D_pct": 13.18, "MFE_180D_pct": 13.18, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.8, "MAE_90D_pct": -13.04, "MAE_180D_pct": -22.33, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-23", "peak_price": 4080.0, "drawdown_after_peak_pct": -31.62, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "rare_earth_policy_supply_watch_was_false_stage2_due_missing_supply_order_margin_bridge", "four_b_evidence_type": ["rare_earth_policy_theme", "bridge_missing", "low_sustainable_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_rare_earth_policy_supply_watch_without_order_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_rare_earth_policy_watch_counts_without_supply_order_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2006_2008_CA", "same_entry_group_id": "R4L95_C16_075970_2024-01-23_3605", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L95_C16_STX_2024_STAGE4B_LITHIUM_NICKEL_TRADING_RESOURCE_EVENT_CAP", "case_id": "R4L95_C16_STX_2024_LITHIUM_NICKEL_TRADING_RESOURCE_EVENT_CAP_4B", "symbol": "011810", "company_name": "STX", "round": "R4", "loop": "95", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE_VS_RARE_EARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_NICKEL_TRADING_EVENT_CAP", "sector": "lithium_nickel_resource_trading_event_premium", "primary_archetype": "lithium_nickel_resource_trading_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-16", "entry_date": "2024-02-16", "entry_price": 10950.0, "evidence_available_at_that_date": "lithium/nickel/resource trading event premium after February strategic-resource spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["lithium_nickel_trading_event", "strategic_resource_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "offtake_shipping_margin_financing_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011810/2024.csv", "profile_path": "atlas/symbol_profiles/011/011810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.68, "MFE_90D_pct": 8.68, "MFE_180D_pct": 8.68, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -23.29, "MAE_90D_pct": -34.52, "MAE_180D_pct": -39.73, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-16", "peak_price": 11900.0, "drawdown_after_peak_pct": -44.54, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_full_window_4B_timing_lithium_nickel_resource_trading_event_cap", "four_b_evidence_type": ["strategic_resource_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_lithium_nickel_resource_trading_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_lithium_nickel_resource_trading_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA_name_history_candidates", "same_entry_group_id": "R4L95_C16_011810_2024-02-16_10950", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L95_C16_POONGSAN_2024_COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_POSITIVE", "trigger_id": "R4L95_C16_POONGSAN_2024_STAGE2_ACTIONABLE_COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE", "symbol": "103140", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 50, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 55, "policy_or_regulatory_score": 45, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "copper_defense_material_supply_margin_positive", "MFE_90D_pct": 71.15, "MAE_90D_pct": -3.9, "score_return_alignment_label": "copper_defense_material_supply_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L95_C16_DONGKUKRNS_2024_RARE_EARTH_POLICY_FALSE_STAGE2", "trigger_id": "R4L95_C16_DONGKUKRNS_2024_STAGE2_FALSE_POSITIVE_RARE_EARTH_POLICY_SUPPLY_WATCH", "symbol": "075970", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 50, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "rare_earth_policy_supply_false_stage2", "MFE_90D_pct": 13.18, "MAE_90D_pct": -13.04, "score_return_alignment_label": "rare_earth_policy_supply_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_rare_earth_policy_watch_counts_without_supply_order_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L95_C16_STX_2024_LITHIUM_NICKEL_TRADING_RESOURCE_EVENT_CAP_4B", "trigger_id": "R4L95_C16_STX_2024_STAGE4B_LITHIUM_NICKEL_TRADING_RESOURCE_EVENT_CAP", "symbol": "011810", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 50, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "lithium_nickel_resource_trading_event_cap_4B_guard", "MFE_90D_pct": 8.68, "MAE_90D_pct": -34.52, "score_return_alignment_label": "lithium_nickel_resource_trading_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_lithium_nickel_resource_trading_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "95", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_DEFENSE_MATERIAL_SUPPLY_MARGIN_BRIDGE_VS_RARE_EARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_NICKEL_TRADING_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["copper_defense_material_supply_margin_positive", "rare_earth_policy_supply_false_stage2", "lithium_nickel_resource_trading_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C16 rows need explicit resource price pass-through, supply/offtake/order visibility, customer quality, inventory spread, shipment volume, margin or revision bridge before positive promotion.
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
10. Add tests that bridge-missing C16 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R4
completed_loop = 95
next_round = R5
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
