# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = COPPER_STRATEGIC_RESOURCE_SUPPLY_CHAIN_BRIDGE_VS_COPPER_THEME_FALSE_STAGE2_AND_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R4_loop_92_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
```

This file is the corrected final output for this execution. The scheduler state after R3 loop 92 is R4 / loop 92. It fills C16 strategic-resource policy/supply behavior after the prior R4 loop 91 used C17, loop 90 used C15, and loop 89 used C16 with different symbols.

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
scheduled_loop = 92
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
round_sector_consistency = pass
computed_next_round = R5
computed_next_loop = 92
```

R4 permits L4 materials / spread / resource research. This loop avoids the previous R4 C17/C15/C16 symbol sets and uses a fresh copper strategic-resource split.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY = 36 rows / 23 symbols / good-bad Stage2 14-9 / 4B-4C 2-0
top covered symbols include 047400(6), 005490(3), 012320(3), 001570(2), 081150(2), 101670(2)
previous R4 loop-89 C16 symbols avoided: 009520, 011810, 037370
previous R4 loop-90 C15 symbols avoided: 024840, 018470, 006110
previous R4 loop-91 C17 symbols avoided: 010060, 007690, 298000
previous R3 loop-92 C13 symbols avoided: 006400, 373220, 393890
```

Selected rows avoid hard duplicates and top repeated C16 symbols:

```text
006260 / Stage2-Actionable / 2024-01-24
012800 / Stage2-Actionable / 2024-02-15
025820 / Stage4B / 2024-04-05
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
| 006260 | atlas/symbol_profiles/006/006260.json | no relevant 2024 corporate-action caveat |
| 012800 | atlas/symbol_profiles/012/012800.json | selected 2024 window clean after old 1998/2008 CA candidates |
| 025820 | atlas/symbol_profiles/025/025820.json | selected 2024 window clean after old 1996/2007 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R4L92_C16_LS_2024_COPPER_STRATEGIC_RESOURCE_SUPPLY_CHAIN_POSITIVE | 006260 | 2024-01-24 | yes | 180 | yes | yes | true |
| R4L92_C16_DAECHANG_2024_COPPER_THEME_FALSE_STAGE2 | 012800 | 2024-02-15 | yes | 180 | yes | yes | true |
| R4L92_C16_EGU_2024_COPPER_RESOURCE_EVENT_CAP_4B | 025820 | 2024-04-05 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | COPPER_STRATEGIC_RESOURCE_SUPPLY_CHAIN_BRIDGE | Positive Stage2 requires supply-chain earnings, inventory-cost spread, ASP pass-through, margin and revision bridge. |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | COPPER_THEME_FALSE_STAGE2 | Copper/resource label without supply-chain/margin bridge can become false Stage2. |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | COPPER_RESOURCE_EVENT_CAP_4B | Copper event premium should route to 4B when margin bridge is missing or capped. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R4L92_C16_LS_2024_COPPER_STRATEGIC_RESOURCE_SUPPLY_CHAIN_POSITIVE | 006260 | LS | positive | Copper/electrification supply-chain bridge produced very high MFE with shallow MAE. |
| R4L92_C16_DAECHANG_2024_COPPER_THEME_FALSE_STAGE2 | 012800 | 대창 | counterexample | Copper theme spike had limited follow-through and large 180D MAE. |
| R4L92_C16_EGU_2024_COPPER_RESOURCE_EVENT_CAP_4B | 025820 | 이구산업 | counterexample / 4B | Copper/resource event premium capped near the April spike and then drew down. |

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
| LS copper supply-chain bridge | historical public/report proxy | true | true | shadow-only positive |
| DaeChang copper-theme false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Egu Industry copper event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 006260 | atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv | atlas/symbol_profiles/006/006260.json |
| 012800 | atlas/ohlcv_tradable_by_symbol_year/012/012800/2024.csv | atlas/symbol_profiles/012/012800.json |
| 025820 | atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv | atlas/symbol_profiles/025/025820.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R4L92_C16_LS_2024_STAGE2_ACTIONABLE_COPPER_RESOURCE_SUPPLY_CHAIN | 006260 | Stage2-Actionable | 2024-01-24 | 80000 | positive | copper supply-chain bridge worked |
| R4L92_C16_DAECHANG_2024_STAGE2_FALSE_POSITIVE_COPPER_THEME | 012800 | Stage2-Actionable | 2024-02-15 | 1676 | counterexample | copper-theme false Stage2 |
| R4L92_C16_EGU_2024_STAGE4B_COPPER_RESOURCE_EVENT_CAP | 025820 | Stage4B | 2024-04-05 | 5700 | counterexample/4B | copper-resource event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R4L92_C16_LS_2024_STAGE2_ACTIONABLE_COPPER_RESOURCE_SUPPLY_CHAIN | 80000 | 35.25 | -1.75 | 143.50 | -1.75 | 143.50 | -1.75 | 2024-05-21 | 194800 | -33.21 |
| R4L92_C16_DAECHANG_2024_STAGE2_FALSE_POSITIVE_COPPER_THEME | 1676 | 9.67 | -20.05 | 9.67 | -20.05 | 9.67 | -34.37 | 2024-02-15 | 1838 | -40.15 |
| R4L92_C16_EGU_2024_STAGE4B_COPPER_RESOURCE_EVENT_CAP | 5700 | 4.04 | -22.02 | 4.04 | -33.77 | 4.04 | -35.96 | 2024-04-09 | 5930 | -38.28 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C16 Stage2 needs supply-chain earnings / inventory-cost spread / ASP pass-through / margin / revision bridge |
| local_4b_watch_guard | strengthen: copper/resource event premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: high-MAE resource-theme rows cannot promote without durable supply/margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is supply-chain/margin bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 006260 | good_stage2_with_later_watch | Supply-chain bridge produced very high MFE and shallow drawdown. |
| 012800 | bad_stage2 | Copper theme spike lacked durable margin/revision evidence. |
| 025820 | good_4B | Copper event premium capped and then de-rated. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 012800 copper theme false Stage2 | 0.91 | 0.91 | false Stage2 due missing supply/margin bridge |
| 025820 copper resource cap | 0.96 | 0.96 | good full-window 4B timing |
| 006260 copper supply-chain bridge | n/a | n/a | positive Stage2, but later copper valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 012800 / 025820
```

No hard 4C candidate is proposed. R4 loop 92 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L4 strategic resource / supply-chain cases, Stage2 requires verified supply-chain earnings, inventory-cost spread, ASP pass-through, customer demand, margin, or revision bridge. Copper, resource, commodity, strategic supply, or policy label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
rule = C16 should split true supply-chain earnings/margin positives from copper/resource theme false Stage2 and event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 52.40 | -18.52 | 0.67 | mixed; C16 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 52.40 | -18.52 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L4 supply/margin bridge required | 2 | 76.59 | -10.90 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C16 bridge vs event-cap split | 2 | 76.59 | -10.90 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing resource themes as positive | 1 | 143.50 | -1.75 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 006260 copper supply-chain bridge | 66 | Stage2-Watch | 77 | Stage2-Actionable | 143.50 | -1.75 | copper_resource_supply_chain_positive |
| 012800 copper theme false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 9.67 | -20.05 | copper_theme_false_stage2 |
| 025820 copper event cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 4.04 | -33.77 | copper_resource_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_STRATEGIC_RESOURCE_SUPPLY_CHAIN_BRIDGE_VS_COPPER_THEME_FALSE_STAGE2_AND_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C16 copper strategic-resource supply-chain positive, copper-theme false Stage2, and copper-resource event-cap 4B split while avoiding top repeated C16 symbols."}
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
residual_error_types_found: copper_resource_supply_chain_positive, copper_theme_false_stage2, copper_resource_event_cap_4B
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
- C16 strategic-resource supply-chain bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,C16_requires_supply_chain_inventory_ASP_margin_revision_bridge,0,"C16 Stage2 should require supply-chain earnings, inventory-cost spread, ASP pass-through, customer demand, margin, or revision bridge, not copper/resource/policy label alone","LS positive worked; DaeChang and Egu Industry theme/event rows failed positive-stage promotion","R4L92_C16_LS_2024_STAGE2_ACTIONABLE_COPPER_RESOURCE_SUPPLY_CHAIN|R4L92_C16_DAECHANG_2024_STAGE2_FALSE_POSITIVE_COPPER_THEME|R4L92_C16_EGU_2024_STAGE4B_COPPER_RESOURCE_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,cap_bridge_missing_copper_resource_event_premiums_as_4B_watch,0,"Copper/resource event premiums can peak before supply-chain earnings and margin bridge is proven","DaeChang capped at the February spike and Egu Industry showed 4B event-cap behavior near the April copper spike","R4L92_C16_DAECHANG_2024_STAGE2_FALSE_POSITIVE_COPPER_THEME|R4L92_C16_EGU_2024_STAGE4B_COPPER_RESOURCE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,block_positive_stage_when_resource_theme_has_high_MAE_without_margin_bridge,0,"High MAE after a bridge-missing copper/resource theme entry should block Stage2/Stage3 promotion unless supply-chain, inventory-cost spread and margin evidence survives","DaeChang MAE180=-34.37 and Egu Industry MAE90=-33.77","R4L92_C16_DAECHANG_2024_STAGE2_FALSE_POSITIVE_COPPER_THEME|R4L92_C16_EGU_2024_STAGE4B_COPPER_RESOURCE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L92_C16_LS_2024_COPPER_STRATEGIC_RESOURCE_SUPPLY_CHAIN_POSITIVE", "symbol": "006260", "company_name": "LS", "round": "R4", "loop": "92", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_STRATEGIC_RESOURCE_SUPPLY_CHAIN_BRIDGE_VS_COPPER_THEME_FALSE_STAGE2_AND_EVENT_CAP", "case_type": "structural_success_with_later_commodity_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R4L92_C16_LS_2024_STAGE2_ACTIONABLE_COPPER_RESOURCE_SUPPLY_CHAIN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Copper/electrification strategic-resource supply-chain bridge produced very high 30D/90D/180D MFE with shallow entry MAE. C16 works when resource/supply-chain narrative maps into copper exposure, grid/electrification demand, subsidiary earnings, margin/revision bridge, and later valuation watch.", "current_profile_verdict": "current_profile_kept_but_C16_positive_requires_supply_chain_earnings_margin_revision_bridge_not_resource_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat in selected 2024 window. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R4L92_C16_DAECHANG_2024_COPPER_THEME_FALSE_STAGE2", "symbol": "012800", "company_name": "대창", "round": "R4", "loop": "92", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_STRATEGIC_RESOURCE_SUPPLY_CHAIN_BRIDGE_VS_COPPER_THEME_FALSE_STAGE2_AND_EVENT_CAP", "case_type": "failed_rerating_copper_theme_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R4L92_C16_DAECHANG_2024_STAGE2_FALSE_POSITIVE_COPPER_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Copper/raw-material theme spike produced limited forward MFE and then large 180D MAE. C16 Stage2 should not be awarded without supply contract, inventory-cost spread, ASP pass-through, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_copper_theme_counts_without_supply_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1998/2008 CA candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R4L92_C16_EGU_2024_COPPER_RESOURCE_EVENT_CAP_4B", "symbol": "025820", "company_name": "이구산업", "round": "R4", "loop": "92", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_STRATEGIC_RESOURCE_SUPPLY_CHAIN_BRIDGE_VS_COPPER_THEME_FALSE_STAGE2_AND_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L92_C16_EGU_2024_STAGE4B_COPPER_RESOURCE_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Copper/resource event premium capped around the April spike and then failed to hold a durable spread/margin rerating. C16 should route bridge-missing copper/resource event premiums to 4B unless supply-chain earnings, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_copper_resource_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1996/2007 CA candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L92_C16_LS_2024_STAGE2_ACTIONABLE_COPPER_RESOURCE_SUPPLY_CHAIN", "case_id": "R4L92_C16_LS_2024_COPPER_STRATEGIC_RESOURCE_SUPPLY_CHAIN_POSITIVE", "symbol": "006260", "company_name": "LS", "round": "R4", "loop": "92", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_STRATEGIC_RESOURCE_SUPPLY_CHAIN_BRIDGE_VS_COPPER_THEME_FALSE_STAGE2_AND_EVENT_CAP", "sector": "copper_electrification_resource_supply_chain", "primary_archetype": "copper_supply_chain_grid_electrification_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 80000.0, "evidence_available_at_that_date": "copper/electrification strategic-resource supply-chain, subsidiary earnings, margin and revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["copper_supply_chain_proxy", "grid_electrification_demand_proxy", "subsidiary_earnings_bridge", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "shallow_MAE90"], "stage4b_evidence_fields": ["later_copper_valuation_watch", "positioning_overheat_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv", "profile_path": "atlas/symbol_profiles/006/006260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 35.25, "MFE_90D_pct": 143.5, "MFE_180D_pct": 143.5, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.75, "MAE_90D_pct": -1.75, "MAE_180D_pct": -1.75, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-21", "peak_price": 194800.0, "drawdown_after_peak_pct": -33.21, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_copper_resource_valuation_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "copper_resource_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_copper_resource_supply_chain_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L92_C16_006260_2024-01-24_80000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L92_C16_DAECHANG_2024_STAGE2_FALSE_POSITIVE_COPPER_THEME", "case_id": "R4L92_C16_DAECHANG_2024_COPPER_THEME_FALSE_STAGE2", "symbol": "012800", "company_name": "대창", "round": "R4", "loop": "92", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_STRATEGIC_RESOURCE_SUPPLY_CHAIN_BRIDGE_VS_COPPER_THEME_FALSE_STAGE2_AND_EVENT_CAP", "sector": "copper_raw_material_theme", "primary_archetype": "copper_theme_without_supply_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-15", "entry_date": "2024-02-15", "entry_price": 1676.0, "evidence_available_at_that_date": "copper/raw-material theme spike and strategic resource supply narrative proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["copper_theme_spike", "strategic_resource_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "supply_margin_revision_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012800/2024.csv", "profile_path": "atlas/symbol_profiles/012/012800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.67, "MFE_90D_pct": 9.67, "MFE_180D_pct": 9.67, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -20.05, "MAE_90D_pct": -20.05, "MAE_180D_pct": -34.37, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-15", "peak_price": 1838.0, "drawdown_after_peak_pct": -40.15, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.91, "four_b_full_window_peak_proximity": 0.91, "four_b_timing_verdict": "copper_theme_spike_was_false_stage2_due_missing_supply_margin_revision_bridge", "four_b_evidence_type": ["copper_theme_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_copper_theme_without_supply_margin_revision_bridge", "current_profile_verdict": "current_profile_false_positive_if_copper_theme_counts_without_supply_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1998_2008_CA", "same_entry_group_id": "R4L92_C16_012800_2024-02-15_1676", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L92_C16_EGU_2024_STAGE4B_COPPER_RESOURCE_EVENT_CAP", "case_id": "R4L92_C16_EGU_2024_COPPER_RESOURCE_EVENT_CAP_4B", "symbol": "025820", "company_name": "이구산업", "round": "R4", "loop": "92", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_STRATEGIC_RESOURCE_SUPPLY_CHAIN_BRIDGE_VS_COPPER_THEME_FALSE_STAGE2_AND_EVENT_CAP", "sector": "copper_resource_event_premium", "primary_archetype": "copper_resource_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-05", "entry_date": "2024-04-05", "entry_price": 5700.0, "evidence_available_at_that_date": "copper/resource event premium after April spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["copper_resource_theme", "strategic_supply_chain_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "supply_margin_bridge_recheck", "post_event_range_failure"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv", "profile_path": "atlas/symbol_profiles/025/025820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.04, "MFE_90D_pct": 4.04, "MFE_180D_pct": 4.04, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -22.02, "MAE_90D_pct": -33.77, "MAE_180D_pct": -35.96, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-09", "peak_price": 5930.0, "drawdown_after_peak_pct": -38.28, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing_copper_resource_event_cap", "four_b_evidence_type": ["copper_resource_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_copper_resource_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_copper_resource_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1996_2007_CA", "same_entry_group_id": "R4L92_C16_025820_2024-04-05_5700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L92_C16_LS_2024_COPPER_STRATEGIC_RESOURCE_SUPPLY_CHAIN_POSITIVE", "trigger_id": "R4L92_C16_LS_2024_STAGE2_ACTIONABLE_COPPER_RESOURCE_SUPPLY_CHAIN", "symbol": "006260", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 40, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 50, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 45, "policy_or_regulatory_score": 45, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "copper_resource_supply_chain_positive", "MFE_90D_pct": 143.5, "MAE_90D_pct": -1.75, "score_return_alignment_label": "copper_resource_supply_chain_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L92_C16_DAECHANG_2024_COPPER_THEME_FALSE_STAGE2", "trigger_id": "R4L92_C16_DAECHANG_2024_STAGE2_FALSE_POSITIVE_COPPER_THEME", "symbol": "012800", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 40, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "copper_theme_false_stage2", "MFE_90D_pct": 9.67, "MAE_90D_pct": -20.05, "score_return_alignment_label": "copper_theme_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_copper_theme_counts_without_supply_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L92_C16_EGU_2024_COPPER_RESOURCE_EVENT_CAP_4B", "trigger_id": "R4L92_C16_EGU_2024_STAGE4B_COPPER_RESOURCE_EVENT_CAP", "symbol": "025820", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 40, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "copper_resource_event_cap_4B_guard", "MFE_90D_pct": 4.04, "MAE_90D_pct": -33.77, "score_return_alignment_label": "copper_resource_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_copper_resource_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "92", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_STRATEGIC_RESOURCE_SUPPLY_CHAIN_BRIDGE_VS_COPPER_THEME_FALSE_STAGE2_AND_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["copper_resource_supply_chain_positive", "copper_theme_false_stage2", "copper_resource_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_loop = 92
next_round = R5
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
