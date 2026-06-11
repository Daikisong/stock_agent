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
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE_VS_RAREEARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | strategic_resource_policy_supply_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R4_loop_98_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
```

This file is the corrected final output for this execution. The scheduler state after R3 loop 98 is R4 / loop 98. R4 is the L4 materials/spread/resource round, and this run fills C16 strategic-resource policy/supply behavior rather than repeating the immediately preceding R4 loop 97 C17 chemical-spread file, R4 loop 96 C15 material-spread file, or R4 loop 95 C16 symbol set.

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
strategic_resource_policy_supply_guardrail = existing_axis_strengthened
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
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
round_sector_consistency = pass
computed_next_round = R5
computed_next_loop = 98
```

C16 is a strategic-resource policy/supply archetype. The policy headline is the mine gate; the useful signal appears only when actual resource exposure, offtake/customer order, shipment volume, pass-through economics, utilization, margin and revision move through it.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY = 36 rows / 23 symbols / good-bad Stage2 14-9 / 4B-4C 2-0
top covered symbols include 047400(6), 005490(3), 012320(3), 001570(2), 081150(2), 101670(2)
previous R4 loop-95 C16 symbols avoided: 103140, 075970, 011810
previous R4 loop-96 C15 symbols avoided: 058430, 032560, 008350
previous R4 loop-97 C17 symbols avoided: 001340, 010060, 006890
previous R3 loop-98 C13 symbols avoided: 036830, 066970, 011500
previous R2 loop-98 C09 symbols avoided: 110990, 405100, 389020
```

Selected rows avoid hard duplicates and top repeated C16 symbols:

```text
336370 / Stage2-Actionable / 2024-02-20
000910 / Stage2-Actionable / 2024-01-12
024890 / Stage4B / 2024-03-12
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
| 336370 | atlas/symbol_profiles/336/336370.json | selected entry after 2024-01-08 and 2024-01-30 CA candidates; 180D forward window clean |
| 000910 | atlas/symbol_profiles/000/000910.json | selected 2024 window clean after old 1997/2008 CA candidates |
| 024890 | atlas/symbol_profiles/024/024890.json | selected 2024 window clean after old 1997/2000/2008 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R4L98_C16_SOLUS_2024_COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE_POSITIVE | 336370 | 2024-02-20 | yes | 180 | yes | post-CA clean | true |
| R4L98_C16_UNION_2024_RAREEARTH_POLICY_SUPPLY_FALSE_STAGE2 | 000910 | 2024-01-12 | yes | 180 | yes | yes | true |
| R4L98_C16_DAEWONCHEM_2024_LITHIUM_MATERIAL_EVENT_CAP_4B | 024890 | 2024-03-12 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE | Positive Stage2 requires customer order, delivery slot, pass-through economics, utilization, margin and revision bridge. |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | RAREEARTH_POLICY_FALSE_STAGE2 | Rare-earth policy watch without actual resource exposure/order/volume/pass-through bridge can become false Stage2. |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | LITHIUM_MATERIAL_EVENT_CAP_4B | Lithium/material supply premium should route to 4B when resource access, offtake and scale-up margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R4L98_C16_SOLUS_2024_COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE_POSITIVE | 336370 | 솔루스첨단소재 | positive | Copper-foil critical-material bridge produced strong MFE with controlled early MAE, but later valuation watch remains necessary. |
| R4L98_C16_UNION_2024_RAREEARTH_POLICY_SUPPLY_FALSE_STAGE2 | 000910 | 유니온 | counterexample | Rare-earth policy watch had near-zero MFE and persistent MAE without resource/order/pass-through bridge. |
| R4L98_C16_DAEWONCHEM_2024_LITHIUM_MATERIAL_EVENT_CAP_4B | 024890 | 대원화성 | counterexample / 4B | Lithium/material event premium capped in the March spike and later drew down deeply. |

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
| Solus Advanced Materials copper-foil critical-material bridge | historical public/report proxy | true | true | shadow-only positive |
| Union rare-earth policy false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Daewon Chemical lithium/material event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 336370 | atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv | atlas/symbol_profiles/336/336370.json |
| 000910 | atlas/ohlcv_tradable_by_symbol_year/000/000910/2024.csv | atlas/symbol_profiles/000/000910.json |
| 024890 | atlas/ohlcv_tradable_by_symbol_year/024/024890/2024.csv | atlas/symbol_profiles/024/024890.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R4L98_C16_SOLUS_2024_STAGE2_ACTIONABLE_COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE | 336370 | Stage2-Actionable | 2024-02-20 | 12890 | positive | copper-foil critical-material supply bridge worked |
| R4L98_C16_UNION_2024_STAGE2_FALSE_POSITIVE_RAREEARTH_POLICY_SUPPLY_WATCH | 000910 | Stage2-Actionable | 2024-01-12 | 6360 | counterexample | rare-earth policy false Stage2 |
| R4L98_C16_DAEWONCHEM_2024_STAGE4B_LITHIUM_MATERIAL_SUPPLY_EVENT_CAP | 024890 | Stage4B | 2024-03-12 | 1841 | counterexample/4B | lithium/material event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R4L98_C16_SOLUS_2024_STAGE2_ACTIONABLE_COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE | 12890 | 51.98 | -8.46 | 82.31 | -8.46 | 82.31 | -8.46 | 2024-07-01 | 23500 | -49.28 |
| R4L98_C16_UNION_2024_STAGE2_FALSE_POSITIVE_RAREEARTH_POLICY_SUPPLY_WATCH | 6360 | 1.89 | -14.78 | 1.89 | -19.81 | 1.89 | -22.56 | 2024-01-15 | 6480 | -24.00 |
| R4L98_C16_DAEWONCHEM_2024_STAGE4B_LITHIUM_MATERIAL_SUPPLY_EVENT_CAP | 1841 | 20.04 | -5.98 | 20.04 | -21.13 | 20.04 | -39.16 | 2024-03-12 | 2210 | -49.32 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C16 Stage2 needs resource exposure / offtake-order / shipment volume / pass-through / utilization / margin / revision bridge |
| strategic_resource_policy_supply_guardrail | strengthen: policy/resource labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing rare-earth and lithium event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE strategic-resource rows cannot promote without durable supply/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether strategic-resource narrative becomes resource exposure, offtake, pass-through and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 336370 | good_stage2_with_later_watch | Critical-material supply bridge produced strong MFE with controlled early MAE, but later drawdown requires 4B valuation watch. |
| 000910 | bad_stage2 | Rare-earth policy watch lacked resource/order/pass-through bridge and produced near-zero MFE. |
| 024890 | good_4B | Lithium/material event premium capped at the March spike and later drew down deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 000910 rare-earth policy false Stage2 | 0.98 | 0.98 | false Stage2 due missing resource exposure / order / pass-through / margin bridge |
| 024890 lithium/material cap | 0.83 | 0.83 | good full-window 4B timing after lithium/material supply event premium |
| 336370 copper-foil supply bridge | n/a | n/a | positive Stage2, but later critical-material valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 000910 / 024890
```

No hard 4C candidate is introduced in this R4 loop 98 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L4 strategic-resource policy/supply cases, Stage2 requires verified resource exposure, offtake or customer order, shipment volume, price/pass-through economics, inventory discipline, utilization, margin, or revision bridge. Strategic-resource, rare-earth, lithium, copper-foil, critical materials, policy, supply-chain or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
rule = C16 should split true resource-exposure/order/pass-through/margin positives from rare-earth policy false Stage2 and lithium/material event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 34.75 | -16.47 | 0.67 | mixed; C16 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 34.75 | -16.47 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L4 resource exposure/order/pass-through bridge required | 2 | 42.10 | -14.14 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C16 bridge vs event-cap split | 2 | 42.10 | -14.14 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing resource-policy themes as positive | 1 | 82.31 | -8.46 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 336370 critical-material bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 82.31 | -8.46 | critical_material_supply_bridge_positive |
| 000910 rare-earth policy false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 1.89 | -19.81 | rareearth_policy_supply_false_stage2 |
| 024890 lithium material cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 20.04 | -21.13 | lithium_material_supply_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE_VS_RAREEARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds R4 loop98 C16: Solus Advanced Materials copper-foil critical-material supply positive, Union rare-earth policy false Stage2, and Daewon Chemical lithium/material event-cap 4B while avoiding top repeated C16 and previous R4/R3 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, strategic_resource_policy_supply_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: critical_material_supply_bridge_positive, rareearth_policy_supply_false_stage2, lithium_material_supply_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, strategic_resource_policy_supply_guardrail, high_MAE_guardrail
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
- C16 strategic-resource policy/supply bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,C16_requires_resource_exposure_order_volume_pass_through_utilization_margin_revision_bridge,0,"C16 Stage2 should require resource exposure, offtake/customer order, shipment volume, pass-through economics, utilization, margin, or revision bridge, not strategic-resource/policy/supply label alone","Solus positive worked; Union and Daewon Chemical event/watch rows failed positive-stage promotion","R4L98_C16_SOLUS_2024_STAGE2_ACTIONABLE_COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE|R4L98_C16_UNION_2024_STAGE2_FALSE_POSITIVE_RAREEARTH_POLICY_SUPPLY_WATCH|R4L98_C16_DAEWONCHEM_2024_STAGE4B_LITHIUM_MATERIAL_SUPPLY_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,cap_bridge_missing_rareearth_and_lithium_resource_event_premiums_as_4B_watch,0,"Rare-earth, lithium and strategic-resource premiums can peak before resource access, offtake, volume, pass-through and margin bridge is proven","Union had near-zero MFE after rare-earth policy watch; Daewon Chemical showed 4B event-cap behavior after March lithium/material supply spike","R4L98_C16_UNION_2024_STAGE2_FALSE_POSITIVE_RAREEARTH_POLICY_SUPPLY_WATCH|R4L98_C16_DAEWONCHEM_2024_STAGE4B_LITHIUM_MATERIAL_SUPPLY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,block_positive_stage_when_resource_policy_theme_has_high_or_persistent_MAE_without_supply_bridge,0,"High or persistent MAE after bridge-missing C16 entries should block Stage2/Stage3 promotion unless resource exposure, order, pass-through and margin evidence survives","Union MAE180=-22.56 and Daewon Chemical MAE180=-39.16","R4L98_C16_UNION_2024_STAGE2_FALSE_POSITIVE_RAREEARTH_POLICY_SUPPLY_WATCH|R4L98_C16_DAEWONCHEM_2024_STAGE4B_LITHIUM_MATERIAL_SUPPLY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L98_C16_SOLUS_2024_COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE_POSITIVE", "symbol": "336370", "company_name": "솔루스첨단소재", "round": "R4", "loop": "98", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE_VS_RAREEARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP", "case_type": "structural_success_with_later_critical_material_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R4L98_C16_SOLUS_2024_STAGE2_ACTIONABLE_COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Copper-foil / critical-material supply bridge produced strong 30D/90D/180D MFE from the post-CA February base with controlled early MAE, then later de-rated sharply from the July peak. C16 works when strategic-resource narrative maps into customer order, delivery slot, copper/pass-through economics, utilization, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C16_positive_requires_customer_order_delivery_pass_through_utilization_margin_revision_bridge_not_resource_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 entry after 2024-01-08 and 2024-01-30 CA candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R4L98_C16_UNION_2024_RAREEARTH_POLICY_SUPPLY_FALSE_STAGE2", "symbol": "000910", "company_name": "유니온", "round": "R4", "loop": "98", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE_VS_RAREEARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP", "case_type": "failed_rerating_rareearth_policy_supply_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R4L98_C16_UNION_2024_STAGE2_FALSE_POSITIVE_RAREEARTH_POLICY_SUPPLY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Rare-earth / strategic-resource policy watch after the January spike had almost no durable MFE and then persistent MAE. C16 Stage2 should not be awarded without confirmed resource exposure, customer order, shipment volume, price/pass-through, inventory discipline, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_rareearth_policy_watch_counts_without_resource_exposure_order_volume_pass_through_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1997/2008 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R4L98_C16_DAEWONCHEM_2024_LITHIUM_MATERIAL_EVENT_CAP_4B", "symbol": "024890", "company_name": "대원화성", "round": "R4", "loop": "98", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE_VS_RAREEARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L98_C16_DAEWONCHEM_2024_STAGE4B_LITHIUM_MATERIAL_SUPPLY_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Lithium/material supply event premium capped at the March spike and later bled into severe drawdown. C16 should route bridge-missing lithium/resource event premiums to 4B unless resource access, offtake/customer order, delivery, pass-through, scale-up, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_lithium_material_supply_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1997/2000/2008 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L98_C16_SOLUS_2024_STAGE2_ACTIONABLE_COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE", "case_id": "R4L98_C16_SOLUS_2024_COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE_POSITIVE", "symbol": "336370", "company_name": "솔루스첨단소재", "round": "R4", "loop": "98", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE_VS_RAREEARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP", "sector": "copper_foil_critical_material_supply_pass_through_utilization", "primary_archetype": "customer_order_delivery_pass_through_utilization_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | strategic_resource_policy_supply_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-20", "entry_date": "2024-02-20", "entry_price": 12890.0, "evidence_available_at_that_date": "copper-foil / critical-material supply recovery, customer order/delivery slot, pass-through economics, utilization and margin/revision bridge proxy after post-CA February base; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["customer_order_proxy", "delivery_slot_proxy", "copper_pass_through_proxy", "utilization_recovery_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "very_strong_MFE90", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_critical_material_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv", "profile_path": "atlas/symbol_profiles/336/336370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 51.98, "MFE_90D_pct": 82.31, "MFE_180D_pct": 82.31, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -8.46, "MAE_90D_pct": -8.46, "MAE_180D_pct": -8.46, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-01", "peak_price": 23500.0, "drawdown_after_peak_pct": -49.28, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_critical_material_valuation_4B_watch_needed", "four_b_evidence_type": ["critical_material_supply_bridge", "customer_order_delivery", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_copperfoil_critical_material_supply_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "post_2024-01-30_CA_boundary_clean_180D_window", "same_entry_group_id": "R4L98_C16_336370_2024-02-20_12890", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L98_C16_UNION_2024_STAGE2_FALSE_POSITIVE_RAREEARTH_POLICY_SUPPLY_WATCH", "case_id": "R4L98_C16_UNION_2024_RAREEARTH_POLICY_SUPPLY_FALSE_STAGE2", "symbol": "000910", "company_name": "유니온", "round": "R4", "loop": "98", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE_VS_RAREEARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP", "sector": "rareearth_strategic_resource_policy_supply_watch", "primary_archetype": "rareearth_policy_watch_without_resource_exposure_order_volume_pass_through_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | strategic_resource_policy_supply_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-12", "entry_date": "2024-01-12", "entry_price": 6360.0, "evidence_available_at_that_date": "rare-earth / strategic-resource policy event watch without confirmed resource exposure, customer order, shipment volume, price pass-through, inventory or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["rareearth_policy_watch", "strategic_resource_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["near_zero_MFE90", "persistent_MAE180", "resource_exposure_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000910/2024.csv", "profile_path": "atlas/symbol_profiles/000/000910.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.89, "MFE_90D_pct": 1.89, "MFE_180D_pct": 1.89, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -14.78, "MAE_90D_pct": -19.81, "MAE_180D_pct": -22.56, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-15", "peak_price": 6480.0, "drawdown_after_peak_pct": -24.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "rareearth_policy_watch_was_false_stage2_due_missing_resource_exposure_order_volume_pass_through_margin_bridge", "four_b_evidence_type": ["rareearth_policy_premium", "bridge_missing", "near_zero_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_rareearth_policy_supply_watch_without_resource_exposure_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_rareearth_policy_watch_counts_without_resource_exposure_order_volume_pass_through_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1997_2008_CA", "same_entry_group_id": "R4L98_C16_000910_2024-01-12_6360", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L98_C16_DAEWONCHEM_2024_STAGE4B_LITHIUM_MATERIAL_SUPPLY_EVENT_CAP", "case_id": "R4L98_C16_DAEWONCHEM_2024_LITHIUM_MATERIAL_EVENT_CAP_4B", "symbol": "024890", "company_name": "대원화성", "round": "R4", "loop": "98", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE_VS_RAREEARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP", "sector": "lithium_material_resource_supply_event_premium", "primary_archetype": "lithium_material_supply_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | strategic_resource_policy_supply_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-12", "entry_date": "2024-03-12", "entry_price": 1841.0, "evidence_available_at_that_date": "lithium/material supply event premium without confirmed resource access, offtake/customer order, delivery, pass-through, scale-up or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["lithium_material_event", "strategic_resource_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "high_MAE90", "deep_MAE180", "offtake_scaleup_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024890/2024.csv", "profile_path": "atlas/symbol_profiles/024/024890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.04, "MFE_90D_pct": 20.04, "MFE_180D_pct": 20.04, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -5.98, "MAE_90D_pct": -21.13, "MAE_180D_pct": -39.16, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-12", "peak_price": 2210.0, "drawdown_after_peak_pct": -49.32, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.83, "four_b_full_window_peak_proximity": 0.83, "four_b_timing_verdict": "good_full_window_4B_timing_lithium_material_supply_event_cap_due_missing_offtake_scaleup_margin_bridge", "four_b_evidence_type": ["lithium_material_supply_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_lithium_material_supply_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_lithium_material_supply_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1997_2000_2008_CA", "same_entry_group_id": "R4L98_C16_024890_2024-03-12_1841", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L98_C16_SOLUS_2024_COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE_POSITIVE", "trigger_id": "R4L98_C16_SOLUS_2024_STAGE2_ACTIONABLE_COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE", "symbol": "336370", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 60, "customer_quality_score": 45, "policy_or_regulatory_score": 35, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 60, "policy_or_regulatory_score": 35, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "copperfoil_critical_material_supply_positive", "MFE_90D_pct": 82.31, "MAE_90D_pct": -8.46, "score_return_alignment_label": "critical_material_supply_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L98_C16_UNION_2024_RAREEARTH_POLICY_SUPPLY_FALSE_STAGE2", "trigger_id": "R4L98_C16_UNION_2024_STAGE2_FALSE_POSITIVE_RAREEARTH_POLICY_SUPPLY_WATCH", "symbol": "000910", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 65, "customer_quality_score": 20, "policy_or_regulatory_score": 65, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "rareearth_policy_supply_false_stage2", "MFE_90D_pct": 1.89, "MAE_90D_pct": -19.81, "score_return_alignment_label": "rareearth_policy_supply_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_rareearth_policy_watch_counts_without_resource_exposure_order_volume_pass_through_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L98_C16_DAEWONCHEM_2024_LITHIUM_MATERIAL_EVENT_CAP_4B", "trigger_id": "R4L98_C16_DAEWONCHEM_2024_STAGE4B_LITHIUM_MATERIAL_SUPPLY_EVENT_CAP", "symbol": "024890", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "lithium_material_supply_event_cap_4B_guard", "MFE_90D_pct": 20.04, "MAE_90D_pct": -21.13, "score_return_alignment_label": "lithium_material_supply_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_lithium_material_supply_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "98", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPERFOIL_CRITICAL_MATERIAL_SUPPLY_BRIDGE_VS_RAREEARTH_POLICY_FALSE_STAGE2_AND_LITHIUM_MATERIAL_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "strategic_resource_policy_supply_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["critical_material_supply_bridge_positive", "rareearth_policy_supply_false_stage2", "lithium_material_supply_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C16 rows need explicit resource exposure, offtake/customer order, shipment volume, price/pass-through economics, inventory discipline, utilization, margin or revision bridge before positive promotion.
- In C16, bridge-missing strategic-resource/policy event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C16 strategic-resource policy/supply rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R4
completed_loop = 98
next_round = R5
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
