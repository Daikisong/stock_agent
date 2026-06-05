# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R10
scheduled_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = HOLDCO_HOUSING_BALANCE_REPAIR_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_POLICY_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R10_loop_93_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

This file is the corrected final output for this execution. The scheduler state after R9 loop 93 is R10 / loop 93. R10 is the L9 construction/PF round, so this run stays inside C30 and avoids prior R10 loop 88~92 symbol sets.

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
scheduled_round = R10
scheduled_loop = 93
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
round_sector_consistency = pass
computed_next_round = R11
computed_next_loop = 93
```

C30 already has many construction/PF rows. This loop adds a fresh holdco/housing balance-repair positive, a small-builder PF false Stage2, and a regional-policy builder event-cap 4B row.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK = 81 rows / 31 symbols / good-bad Stage2 16-29 / 4B-4C 3-4
top covered symbols include 002990(6), 294870(6), 375500(6), 004960(5), 013580(5), 006360(4)
previous R10 loop-88 symbols avoided: 035890, 028100, 009410
previous R10 loop-89 symbols avoided: 010780, 005960, 001470
previous R10 loop-90 symbols avoided: 000720, 002460, 013360
previous R10 loop-91 symbols avoided: 003070, 001260, 021320
previous R10 loop-92 symbols avoided: 014790, 002780, 002410
previous R9 loop-93 C14 symbols avoided: 096770, 222080, 086520
```

Selected rows avoid hard duplicates and top repeated C30 symbols:

```text
012630 / Stage2-Actionable / 2024-01-24
001840 / Stage2-Actionable / 2024-01-24
025950 / Stage4B / 2024-03-25
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
| 012630 | atlas/symbol_profiles/012/012630.json | selected 2024 window clean after old 2018 CA candidates |
| 001840 | atlas/symbol_profiles/001/001840.json | selected 2024 window clean after old 1997~2014 CA candidates |
| 025950 | atlas/symbol_profiles/025/025950.json | selected 2024 window clean after old 1997/2003/2004 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R10L93_C30_HDC_2024_HOLDCO_HOUSING_BALANCE_REPAIR_POSITIVE | 012630 | 2024-01-24 | yes | 180 | yes | yes | true |
| R10L93_C30_EWHACONST_2024_SMALL_BUILDER_PF_FALSE_STAGE2 | 001840 | 2024-01-24 | yes | 180 | yes | yes | true |
| R10L93_C30_DONGSHIN_2024_REGIONAL_POLICY_BUILDER_EVENT_CAP_4B | 025950 | 2024-03-25 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | HOLDCO_HOUSING_BALANCE_REPAIR_BRIDGE | Positive Stage2 requires asset-value visibility, PF/balance repair, order quality, funding capacity, margin and revision bridge. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | SMALL_BUILDER_FALSE_STAGE2 | Small-builder/PF watch without cashflow and order-quality bridge can become false Stage2. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | REGIONAL_POLICY_EVENT_CAP_4B | Regional-policy construction premium should route to 4B when funding/PF/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R10L93_C30_HDC_2024_HOLDCO_HOUSING_BALANCE_REPAIR_POSITIVE | 012630 | HDC | positive | Housing/PF balance-repair and asset-value bridge produced high MFE with minimal MAE. |
| R10L93_C30_EWHACONST_2024_SMALL_BUILDER_PF_FALSE_STAGE2 | 001840 | 이화공영 | counterexample | Small-builder PF watch had low MFE and persistent MAE without balance bridge. |
| R10L93_C30_DONGSHIN_2024_REGIONAL_POLICY_BUILDER_EVENT_CAP_4B | 025950 | 동신건설 | counterexample / 4B | Regional-policy builder premium capped around the March spike and then de-rated sharply. |

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
| HDC holdco/housing balance repair | historical public/report proxy | true | true | shadow-only positive |
| Ewhagong small-builder PF false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Dongshin regional-policy builder cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 012630 | atlas/ohlcv_tradable_by_symbol_year/012/012630/2024.csv | atlas/symbol_profiles/012/012630.json |
| 001840 | atlas/ohlcv_tradable_by_symbol_year/001/001840/2024.csv | atlas/symbol_profiles/001/001840.json |
| 025950 | atlas/ohlcv_tradable_by_symbol_year/025/025950/2024.csv | atlas/symbol_profiles/025/025950.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R10L93_C30_HDC_2024_STAGE2_ACTIONABLE_HOLDCO_HOUSING_BALANCE_REPAIR | 012630 | Stage2-Actionable | 2024-01-24 | 6480 | positive | holdco/housing balance-repair bridge worked |
| R10L93_C30_EWHACONST_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_WATCH | 001840 | Stage2-Actionable | 2024-01-24 | 3125 | counterexample | small-builder PF watch false Stage2 |
| R10L93_C30_DONGSHIN_2024_STAGE4B_REGIONAL_POLICY_BUILDER_EVENT_CAP | 025950 | Stage4B | 2024-03-25 | 30850 | counterexample/4B | regional-policy builder event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R10L93_C30_HDC_2024_STAGE2_ACTIONABLE_HOLDCO_HOUSING_BALANCE_REPAIR | 6480 | 36.11 | -0.15 | 37.19 | -0.15 | 40.28 | -0.15 | 2024-07-17 | 9090 | -13.64 |
| R10L93_C30_EWHACONST_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_WATCH | 3125 | 4.16 | -4.32 | 4.16 | -20.80 | 4.16 | -27.52 | 2024-02-08 | 3255 | -30.41 |
| R10L93_C30_DONGSHIN_2024_STAGE4B_REGIONAL_POLICY_BUILDER_EVENT_CAP | 30850 | 3.24 | -39.74 | 3.24 | -39.74 | 3.24 | -39.74 | 2024-03-25 | 31850 | -41.63 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C30 Stage2 needs PF cashflow / funding / order-quality / balance repair / margin bridge |
| local_4b_watch_guard | strengthen: regional and small-builder event premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: high-MAE construction/PF rows cannot promote without durable balance-repair evidence |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is PF/balance bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 012630 | good_stage2_with_later_watch | Balance-repair and asset-value bridge produced high MFE with almost no entry MAE. |
| 001840 | bad_stage2 | Small-builder PF watch lacked cashflow/order bridge and later de-rated. |
| 025950 | good_4B | Regional-policy builder premium capped near the March spike and immediately suffered high MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 001840 small-builder false Stage2 | 0.96 | 0.96 | false Stage2 due missing cashflow/order-quality bridge |
| 025950 regional-policy builder cap | 0.97 | 0.97 | good full-window 4B timing after March event spike |
| 012630 holdco/housing bridge | n/a | n/a | positive Stage2, but later housing/PF valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 001840 / 025950
```

No hard 4C candidate is proposed. R10 loop 93 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L9 construction/PF balance-sheet cases, Stage2 requires verified PF cashflow repair, funding capacity, order quality, asset-value visibility, balance-sheet repair, margin, or revision bridge. Small-builder, regional policy, PF normalization, housing beta, or construction rebound label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rule = C30 should split true PF/balance-repair positives from small-builder false Stage2 and regional-policy event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 14.86 | -20.23 | 0.67 | mixed; C30 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 14.86 | -20.23 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L9 PF/balance bridge required | 2 | 20.68 | -10.48 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C30 bridge vs event-cap split | 2 | 20.68 | -10.48 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing construction/PF themes as positive | 1 | 37.19 | -0.15 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 012630 holdco balance bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 37.19 | -0.15 | holdco_housing_balance_repair_positive |
| 001840 small-builder false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 4.16 | -20.80 | small_builder_PF_false_stage2 |
| 025950 regional-policy cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 3.24 | -39.74 | regional_policy_builder_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOLDCO_HOUSING_BALANCE_REPAIR_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_POLICY_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C30 HDC holdco housing/PF balance-repair positive, Ewhagong small-builder PF false Stage2, and Dongshin regional-policy builder event-cap 4B split while avoiding top repeated C30 symbols."}
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
residual_error_types_found: holdco_housing_balance_repair_positive, small_builder_PF_false_stage2, regional_policy_builder_event_cap_4B
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
- C30 construction/PF balance-sheet bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,C30_requires_balance_repair_cashflow_order_quality_funding_margin_bridge,0,"C30 Stage2 should require PF cashflow repair, funding capacity, order quality, asset-value visibility, balance-sheet repair, margin, or revision bridge, not construction/PF/policy beta label alone","HDC positive worked; Ewhagong and Dongshin event/watch rows failed positive-stage promotion","R10L93_C30_HDC_2024_STAGE2_ACTIONABLE_HOLDCO_HOUSING_BALANCE_REPAIR|R10L93_C30_EWHACONST_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_WATCH|R10L93_C30_DONGSHIN_2024_STAGE4B_REGIONAL_POLICY_BUILDER_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,cap_bridge_missing_small_builder_and_regional_policy_event_premiums_as_4B_watch,0,"Small-builder and regional-policy construction premiums can peak before cashflow, order quality and funding bridge is proven","Ewhagong had low forward MFE and later MAE; Dongshin showed clean 4B event-cap behavior after March spike","R10L93_C30_EWHACONST_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_WATCH|R10L93_C30_DONGSHIN_2024_STAGE4B_REGIONAL_POLICY_BUILDER_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,block_positive_stage_when_construction_PF_watch_has_high_MAE_without_balance_bridge,0,"High or persistent MAE after bridge-missing construction/PF entries should block Stage2/Stage3 promotion unless PF cashflow and balance evidence survives","Ewhagong MAE180=-27.52 and Dongshin MAE90=-39.74","R10L93_C30_EWHACONST_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_WATCH|R10L93_C30_DONGSHIN_2024_STAGE4B_REGIONAL_POLICY_BUILDER_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R10L93_C30_HDC_2024_HOLDCO_HOUSING_BALANCE_REPAIR_POSITIVE", "symbol": "012630", "company_name": "HDC", "round": "R10", "loop": "93", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOLDCO_HOUSING_BALANCE_REPAIR_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_POLICY_EVENT_CAP", "case_type": "structural_success_with_later_housing_PF_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R10L93_C30_HDC_2024_STAGE2_ACTIONABLE_HOLDCO_HOUSING_BALANCE_REPAIR", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Holding-company / housing PF balance-repair bridge produced high 30D/90D/180D MFE with almost no entry MAE. C30 works when the construction/PF narrative maps into balance repair, asset-value discount narrowing, order quality, funding capacity and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C30_positive_requires_balance_repair_asset_value_order_quality_funding_bridge_not_housing_beta_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2018 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R10L93_C30_EWHACONST_2024_SMALL_BUILDER_PF_FALSE_STAGE2", "symbol": "001840", "company_name": "이화공영", "round": "R10", "loop": "93", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOLDCO_HOUSING_BALANCE_REPAIR_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_POLICY_EVENT_CAP", "case_type": "failed_rerating_small_builder_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R10L93_C30_EWHACONST_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Small-builder / PF normalization watch had low forward MFE and then persistent 90D/180D MAE. C30 Stage2 should not be awarded without verified PF cashflow repair, order quality, funding capacity, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_small_builder_PF_watch_counts_without_cashflow_order_quality_balance_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1997~2014 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R10L93_C30_DONGSHIN_2024_REGIONAL_POLICY_BUILDER_EVENT_CAP_4B", "symbol": "025950", "company_name": "동신건설", "round": "R10", "loop": "93", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOLDCO_HOUSING_BALANCE_REPAIR_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_POLICY_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R10L93_C30_DONGSHIN_2024_STAGE4B_REGIONAL_POLICY_BUILDER_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Regional builder / policy-linked construction event premium capped around the March spike and then suffered severe MAE. C30 should route bridge-missing regional construction/PF event premiums to 4B unless backlog, PF cashflow, funding, execution and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_regional_builder_policy_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1997/2003/2004 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R10L93_C30_HDC_2024_STAGE2_ACTIONABLE_HOLDCO_HOUSING_BALANCE_REPAIR", "case_id": "R10L93_C30_HDC_2024_HOLDCO_HOUSING_BALANCE_REPAIR_POSITIVE", "symbol": "012630", "company_name": "HDC", "round": "R10", "loop": "93", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOLDCO_HOUSING_BALANCE_REPAIR_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_POLICY_EVENT_CAP", "sector": "housing_holdco_PF_balance_repair_asset_value", "primary_archetype": "holdco_housing_asset_value_funding_balance_repair_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 6480.0, "evidence_available_at_that_date": "housing/PF discount narrowing, holdco asset-value visibility, funding capacity, balance repair and revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["balance_repair_proxy", "asset_value_discount_narrowing_proxy", "funding_capacity_bridge", "housing_order_quality_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["high_MFE30", "high_MFE90", "high_MFE180", "shallow_MAE90"], "stage4b_evidence_fields": ["later_housing_PF_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012630/2024.csv", "profile_path": "atlas/symbol_profiles/012/012630.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 36.11, "MFE_90D_pct": 37.19, "MFE_180D_pct": 40.28, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -0.15, "MAE_90D_pct": -0.15, "MAE_180D_pct": -0.15, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-17", "peak_price": 9090.0, "drawdown_after_peak_pct": -13.64, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_housing_PF_valuation_watch_needed", "four_b_evidence_type": ["valuation_repricing", "asset_value_discount_narrowing", "PF_balance_repair_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_holdco_housing_balance_repair_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2018_CA", "same_entry_group_id": "R10L93_C30_012630_2024-01-24_6480", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L93_C30_EWHACONST_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_WATCH", "case_id": "R10L93_C30_EWHACONST_2024_SMALL_BUILDER_PF_FALSE_STAGE2", "symbol": "001840", "company_name": "이화공영", "round": "R10", "loop": "93", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOLDCO_HOUSING_BALANCE_REPAIR_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_POLICY_EVENT_CAP", "sector": "small_builder_PF_normalization_watch", "primary_archetype": "small_builder_PF_watch_without_cashflow_order_quality_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 3125.0, "evidence_available_at_that_date": "small-builder / regional construction PF normalization watch and policy-beta expectation proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["small_builder_PF_watch", "regional_construction_beta", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "high_MAE180", "PF_cashflow_order_quality_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001840/2024.csv", "profile_path": "atlas/symbol_profiles/001/001840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.16, "MFE_90D_pct": 4.16, "MFE_180D_pct": 4.16, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -4.32, "MAE_90D_pct": -20.8, "MAE_180D_pct": -27.52, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-08", "peak_price": 3255.0, "drawdown_after_peak_pct": -30.41, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "small_builder_PF_watch_was_false_stage2_due_missing_cashflow_order_quality_balance_bridge", "four_b_evidence_type": ["small_builder_PF_beta", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_small_builder_PF_watch_without_balance_bridge", "current_profile_verdict": "current_profile_false_positive_if_small_builder_PF_watch_counts_without_cashflow_order_quality_balance_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1997_2014_CA", "same_entry_group_id": "R10L93_C30_001840_2024-01-24_3125", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L93_C30_DONGSHIN_2024_STAGE4B_REGIONAL_POLICY_BUILDER_EVENT_CAP", "case_id": "R10L93_C30_DONGSHIN_2024_REGIONAL_POLICY_BUILDER_EVENT_CAP_4B", "symbol": "025950", "company_name": "동신건설", "round": "R10", "loop": "93", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOLDCO_HOUSING_BALANCE_REPAIR_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_POLICY_EVENT_CAP", "sector": "regional_policy_builder_event_premium", "primary_archetype": "regional_policy_builder_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-25", "entry_date": "2024-03-25", "entry_price": 30850.0, "evidence_available_at_that_date": "regional builder / policy-linked construction event premium after March spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["regional_builder_policy_event", "construction_beta_rebound", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "PF_cashflow_execution_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/025/025950/2024.csv", "profile_path": "atlas/symbol_profiles/025/025950.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.24, "MFE_90D_pct": 3.24, "MFE_180D_pct": 3.24, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -39.74, "MAE_90D_pct": -39.74, "MAE_180D_pct": -39.74, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-25", "peak_price": 31850.0, "drawdown_after_peak_pct": -41.63, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "good_full_window_4B_timing_regional_policy_builder_event_cap", "four_b_evidence_type": ["regional_policy_builder_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_regional_policy_builder_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_regional_builder_policy_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1997_2003_2004_CA", "same_entry_group_id": "R10L93_C30_025950_2024-03-25_30850", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L93_C30_HDC_2024_HOLDCO_HOUSING_BALANCE_REPAIR_POSITIVE", "trigger_id": "R10L93_C30_HDC_2024_STAGE2_ACTIONABLE_HOLDCO_HOUSING_BALANCE_REPAIR", "symbol": "012630", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 55, "margin_bridge_score": 50, "revision_score": 50, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 25, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "holdco_housing_balance_repair_positive", "MFE_90D_pct": 37.19, "MAE_90D_pct": -0.15, "score_return_alignment_label": "holdco_housing_balance_repair_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L93_C30_EWHACONST_2024_SMALL_BUILDER_PF_FALSE_STAGE2", "trigger_id": "R10L93_C30_EWHACONST_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_WATCH", "symbol": "001840", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "small_builder_PF_false_stage2", "MFE_90D_pct": 4.16, "MAE_90D_pct": -20.8, "score_return_alignment_label": "small_builder_PF_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_small_builder_PF_watch_counts_without_cashflow_order_quality_balance_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L93_C30_DONGSHIN_2024_REGIONAL_POLICY_BUILDER_EVENT_CAP_4B", "trigger_id": "R10L93_C30_DONGSHIN_2024_STAGE4B_REGIONAL_POLICY_BUILDER_EVENT_CAP", "symbol": "025950", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "regional_policy_builder_event_cap_4B_guard", "MFE_90D_pct": 3.24, "MAE_90D_pct": -39.74, "score_return_alignment_label": "regional_policy_builder_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_regional_builder_policy_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": "93", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOLDCO_HOUSING_BALANCE_REPAIR_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_POLICY_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["holdco_housing_balance_repair_positive", "small_builder_PF_false_stage2", "regional_policy_builder_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
10. Add tests that bridge-missing C30 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R10
completed_loop = 93
next_round = R11
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
