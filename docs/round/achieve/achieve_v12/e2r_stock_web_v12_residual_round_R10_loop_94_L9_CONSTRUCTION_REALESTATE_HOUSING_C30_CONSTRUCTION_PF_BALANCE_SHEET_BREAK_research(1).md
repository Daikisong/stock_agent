# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R10
scheduled_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_BUILDER_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R10_loop_94_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

This file is the corrected final output for this execution. The scheduler state after R9 loop 94 is R10 / loop 94. R10 is the L9 construction/PF round, and this run fills C30 construction/PF balance-sheet behavior while avoiding top repeated C30 symbols and the prior R10 loop 88~93 symbols.

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
scheduled_loop = 94
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
round_sector_consistency = pass
computed_next_round = R11
computed_next_loop = 94
```

C30 is a balance-sheet bridge archetype. A PF headline is only a crack in the wall; the repair is cashflow visibility, funding capacity, order quality, project mix, margin and revision.

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
previous R10 loop-93 symbols avoided: 012630, 001840, 025950
previous R9 loop-94 C29 symbols avoided: 015750, 009900, 123410
```

Selected rows avoid hard duplicates and top repeated C30 symbols:

```text
047040 / Stage2-Actionable / 2024-01-24
013700 / Stage2-Actionable / 2024-01-24
002290 / Stage4B / 2024-01-24
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
| 047040 | atlas/symbol_profiles/047/047040.json | selected 2024 window clean after old 2001/2003/2011 CA candidates |
| 013700 | atlas/symbol_profiles/013/013700.json | selected 180D window before 2024-10-18 CA candidate boundary |
| 002290 | atlas/symbol_profiles/002/002290.json | selected 2024 window clean after old CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R10L94_C30_DAEWOOE_C_2024_MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE_POSITIVE | 047040 | 2024-01-24 | yes | 180 | yes | yes | true |
| R10L94_C30_CAMUSENC_2024_SMALL_BUILDER_PF_NORMALIZATION_FALSE_STAGE2 | 013700 | 2024-01-24 | yes | 180 | yes | caveated-clean | true |
| R10L94_C30_SAMIL_2024_REGIONAL_BUILDER_POLICY_EVENT_CAP_4B | 002290 | 2024-01-24 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE | Positive Stage2 requires order quality, PF cashflow repair, funding capacity, project mix, margin and revision bridge. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | SMALL_BUILDER_FALSE_STAGE2 | Small-builder PF normalization without cashflow/order/funding bridge can become false Stage2. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | REGIONAL_BUILDER_EVENT_CAP_4B | Regional-builder policy/PF event premium should route to 4B when cashflow and funding bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R10L94_C30_DAEWOOE_C_2024_MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE_POSITIVE | 047040 | 대우건설 | positive | Major-builder order/funding bridge produced positive 180D MFE with controlled MAE. |
| R10L94_C30_CAMUSENC_2024_SMALL_BUILDER_PF_NORMALIZATION_FALSE_STAGE2 | 013700 | 까뮤이앤씨 | counterexample | Small-builder PF normalization watch had low MFE and no durable bridge. |
| R10L94_C30_SAMIL_2024_REGIONAL_BUILDER_POLICY_EVENT_CAP_4B | 002290 | 삼일기업공사 | counterexample / 4B | Regional-builder event premium capped near the late-January spike and then de-rated. |

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
| Daewoo E&C major-builder order/funding bridge | historical public/report proxy | true | true | shadow-only positive |
| Camus E&C small-builder PF false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Samil regional-builder event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 047040 | atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv | atlas/symbol_profiles/047/047040.json |
| 013700 | atlas/ohlcv_tradable_by_symbol_year/013/013700/2024.csv | atlas/symbol_profiles/013/013700.json |
| 002290 | atlas/ohlcv_tradable_by_symbol_year/002/002290/2024.csv | atlas/symbol_profiles/002/002290.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R10L94_C30_DAEWOOE_C_2024_STAGE2_ACTIONABLE_MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE | 047040 | Stage2-Actionable | 2024-01-24 | 3910 | positive | major-builder order/funding bridge worked |
| R10L94_C30_CAMUSENC_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_NORMALIZATION_WATCH | 013700 | Stage2-Actionable | 2024-01-24 | 1580 | counterexample | small-builder PF normalization false Stage2 |
| R10L94_C30_SAMIL_2024_STAGE4B_REGIONAL_BUILDER_POLICY_EVENT_CAP | 002290 | Stage4B | 2024-01-24 | 3955 | counterexample/4B | regional-builder policy event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R10L94_C30_DAEWOOE_C_2024_STAGE2_ACTIONABLE_MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE | 3910 | 6.91 | -2.81 | 6.91 | -8.44 | 26.98 | -8.44 | 2024-07-18 | 4965 | -17.02 |
| R10L94_C30_CAMUSENC_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_NORMALIZATION_WATCH | 1580 | 3.29 | -6.90 | 10.76 | -6.96 | 10.76 | -16.90 | 2024-04-12 | 1750 | -25.00 |
| R10L94_C30_SAMIL_2024_STAGE4B_REGIONAL_BUILDER_POLICY_EVENT_CAP | 3955 | 5.69 | -14.03 | 5.69 | -14.29 | 5.69 | -20.35 | 2024-01-25 | 4180 | -22.50 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C30 Stage2 needs order quality / PF cashflow / funding / balance / margin / revision bridge |
| local_4b_watch_guard | strengthen: regional and small-builder event premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: later-MAE construction/PF rows cannot promote without durable balance-repair evidence |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is PF/balance bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 047040 | good_stage2_with_later_watch | Order/funding bridge produced positive 180D MFE with controlled MAE. |
| 013700 | bad_stage2 | Small-builder PF watch had low MFE and no durable cashflow/funding bridge. |
| 002290 | good_4B | Regional-builder event premium capped near the January spike and later drew down. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 013700 small-builder false Stage2 | 0.90 | 0.90 | false Stage2 due missing cashflow/order/funding bridge |
| 002290 regional-builder cap | 0.95 | 0.95 | acceptable full-window 4B timing after late-January event premium |
| 047040 major-builder bridge | n/a | n/a | positive Stage2, but later construction/PF valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 013700 / 002290
```

No hard 4C candidate is proposed. R10 loop 94 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L9 construction/PF balance-sheet cases, Stage2 requires verified PF cashflow repair, funding capacity, order quality, project mix, asset/balance-sheet visibility, margin, or revision bridge. Small-builder, regional policy, PF normalization, housing beta, construction rebound or builder label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rule = C30 should split true PF/balance/order/funding positives from small-builder false Stage2 and regional-policy event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 7.79 | -9.90 | 0.67 | mixed; C30 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 7.79 | -9.90 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L9 PF/order/funding bridge required | 2 | 8.84 | -7.70 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C30 bridge vs event-cap split | 2 | 8.84 | -7.70 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing construction/PF themes as positive | 1 | 6.91 | -8.44 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 047040 major-builder bridge | 65 | Stage2-Watch | 73 | Stage2-Actionable | 6.91 | -8.44 | major_builder_order_backlog_funding_positive |
| 013700 small-builder false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 10.76 | -6.96 | small_builder_PF_normalization_false_stage2 |
| 002290 regional-builder cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 5.69 | -14.29 | regional_builder_policy_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_BUILDER_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C30 Daewoo E&C major-builder order/funding positive, Camus E&C small-builder PF false Stage2, and Samil regional-builder policy event-cap 4B split while avoiding top repeated C30 symbols and previous R10/R9 loop94 symbols."}
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
residual_error_types_found: major_builder_order_backlog_funding_positive, small_builder_PF_normalization_false_stage2, regional_builder_policy_event_cap_4B
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
shadow_weight,stage2_required_bridge,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,C30_requires_order_quality_cashflow_funding_balance_margin_revision_bridge,0,"C30 Stage2 should require PF cashflow repair, funding capacity, order quality, project mix, balance-sheet visibility, margin, or revision bridge, not construction/PF/policy beta label alone","Daewoo E&C positive worked; Camus E&C and Samil Enterprise event/watch rows failed positive-stage promotion","R10L94_C30_DAEWOOE_C_2024_STAGE2_ACTIONABLE_MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE|R10L94_C30_CAMUSENC_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_NORMALIZATION_WATCH|R10L94_C30_SAMIL_2024_STAGE4B_REGIONAL_BUILDER_POLICY_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,cap_bridge_missing_small_builder_and_regional_policy_event_premiums_as_4B_watch,0,"Small-builder and regional-policy construction premiums can peak before cashflow, order quality and funding bridge is proven","Camus had low MFE after PF normalization watch; Samil showed event-cap behavior after late-January builder spike","R10L94_C30_CAMUSENC_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_NORMALIZATION_WATCH|R10L94_C30_SAMIL_2024_STAGE4B_REGIONAL_BUILDER_POLICY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,block_positive_stage_when_construction_PF_watch_has_high_or_later_MAE_without_balance_bridge,0,"Later or persistent MAE after bridge-missing construction/PF entries should block Stage2/Stage3 promotion unless PF cashflow and balance evidence survives","Camus MAE180=-16.90 and Samil MAE180=-20.35","R10L94_C30_CAMUSENC_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_NORMALIZATION_WATCH|R10L94_C30_SAMIL_2024_STAGE4B_REGIONAL_BUILDER_POLICY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R10L94_C30_DAEWOOE_C_2024_MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE_POSITIVE", "symbol": "047040", "company_name": "대우건설", "round": "R10", "loop": "94", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_BUILDER_EVENT_CAP", "case_type": "structural_success_with_later_construction_PF_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R10L94_C30_DAEWOOE_C_2024_STAGE2_ACTIONABLE_MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Major-builder order backlog / overseas project / funding-capacity bridge produced positive 180D MFE with controlled drawdown. C30 works when construction/PF narrative maps into order quality, funding capacity, cashflow repair, balance-sheet visibility, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C30_positive_requires_order_quality_funding_cashflow_margin_revision_bridge_not_construction_beta_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2001/2003/2011 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R10L94_C30_CAMUSENC_2024_SMALL_BUILDER_PF_NORMALIZATION_FALSE_STAGE2", "symbol": "013700", "company_name": "까뮤이앤씨", "round": "R10", "loop": "94", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_BUILDER_EVENT_CAP", "case_type": "failed_rerating_small_builder_PF_normalization_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R10L94_C30_CAMUSENC_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_NORMALIZATION_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Small-builder PF normalization watch had only low forward MFE and later drawdown. C30 Stage2 should not be awarded without verified PF cashflow repair, contract/order quality, funding capacity, execution margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_small_builder_PF_normalization_watch_counts_without_cashflow_order_funding_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window treated as clean before 2024-10-18 corporate-action candidate boundary; source-proxy only."}
{"row_type": "case", "case_id": "R10L94_C30_SAMIL_2024_REGIONAL_BUILDER_POLICY_EVENT_CAP_4B", "symbol": "002290", "company_name": "삼일기업공사", "round": "R10", "loop": "94", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_BUILDER_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R10L94_C30_SAMIL_2024_STAGE4B_REGIONAL_BUILDER_POLICY_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Regional builder / small construction policy-beta event premium capped in late January and then de-rated. C30 should route bridge-missing regional-builder PF/policy premiums to 4B unless backlog, funding, cashflow, execution margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_regional_builder_policy_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R10L94_C30_DAEWOOE_C_2024_STAGE2_ACTIONABLE_MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE", "case_id": "R10L94_C30_DAEWOOE_C_2024_MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE_POSITIVE", "symbol": "047040", "company_name": "대우건설", "round": "R10", "loop": "94", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_BUILDER_EVENT_CAP", "sector": "major_builder_order_backlog_funding_capacity", "primary_archetype": "order_quality_funding_cashflow_balance_repair_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 3910.0, "evidence_available_at_that_date": "major-builder order backlog, overseas project mix, PF/funding capacity, cashflow repair and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["order_quality_proxy", "funding_capacity_proxy", "PF_cashflow_repair_proxy", "project_mix_margin_bridge_proxy", "revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "positive_MFE90", "positive_MFE180", "controlled_MAE90"], "stage4b_evidence_fields": ["later_construction_PF_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv", "profile_path": "atlas/symbol_profiles/047/047040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.91, "MFE_90D_pct": 6.91, "MFE_180D_pct": 26.98, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -2.81, "MAE_90D_pct": -8.44, "MAE_180D_pct": -8.44, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-18", "peak_price": 4965.0, "drawdown_after_peak_pct": -17.02, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_construction_PF_valuation_4B_watch_needed", "four_b_evidence_type": ["order_backlog_bridge", "funding_capacity", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_major_builder_order_backlog_funding_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2001_2003_2011_CA", "same_entry_group_id": "R10L94_C30_047040_2024-01-24_3910", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L94_C30_CAMUSENC_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_NORMALIZATION_WATCH", "case_id": "R10L94_C30_CAMUSENC_2024_SMALL_BUILDER_PF_NORMALIZATION_FALSE_STAGE2", "symbol": "013700", "company_name": "까뮤이앤씨", "round": "R10", "loop": "94", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_BUILDER_EVENT_CAP", "sector": "small_builder_PF_normalization_watch", "primary_archetype": "small_builder_PF_watch_without_cashflow_order_funding_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 1580.0, "evidence_available_at_that_date": "small-builder PF normalization and construction policy-beta watch without verified PF cashflow, order quality, funding or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["small_builder_PF_watch", "construction_policy_beta", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/013/013700/2024.csv", "profile_path": "atlas/symbol_profiles/013/013700.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.29, "MFE_90D_pct": 10.76, "MFE_180D_pct": 10.76, "MFE_1Y_pct": "not_calculated_due_2024-10-18_CA_candidate_boundary", "MFE_2Y_pct": "not_calculated_due_2024-10-18_CA_candidate_boundary", "MAE_30D_pct": -6.9, "MAE_90D_pct": -6.96, "MAE_180D_pct": -16.9, "MAE_1Y_pct": "not_calculated_due_2024-10-18_CA_candidate_boundary", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-12", "peak_price": 1750.0, "drawdown_after_peak_pct": -25.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "small_builder_PF_normalization_watch_was_false_stage2_due_missing_cashflow_order_funding_margin_bridge", "four_b_evidence_type": ["small_builder_PF_beta", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_small_builder_PF_normalization_without_cashflow_order_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_small_builder_PF_normalization_watch_counts_without_cashflow_order_funding_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_before_2024-10-18_CA_candidate_boundary", "same_entry_group_id": "R10L94_C30_013700_2024-01-24_1580", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L94_C30_SAMIL_2024_STAGE4B_REGIONAL_BUILDER_POLICY_EVENT_CAP", "case_id": "R10L94_C30_SAMIL_2024_REGIONAL_BUILDER_POLICY_EVENT_CAP_4B", "symbol": "002290", "company_name": "삼일기업공사", "round": "R10", "loop": "94", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_BUILDER_EVENT_CAP", "sector": "regional_builder_policy_event_premium", "primary_archetype": "regional_builder_PF_policy_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 3955.0, "evidence_available_at_that_date": "regional-builder / policy-linked construction event premium after late-January construction beta spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["regional_builder_policy_event", "construction_beta_rebound", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "MAE_recheck", "PF_order_funding_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002290/2024.csv", "profile_path": "atlas/symbol_profiles/002/002290.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.69, "MFE_90D_pct": 5.69, "MFE_180D_pct": 5.69, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -14.03, "MAE_90D_pct": -14.29, "MAE_180D_pct": -20.35, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-25", "peak_price": 4180.0, "drawdown_after_peak_pct": -22.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "acceptable_full_window_4B_timing_regional_builder_policy_event_cap", "four_b_evidence_type": ["regional_builder_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_regional_builder_policy_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_regional_builder_policy_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA_candidates", "same_entry_group_id": "R10L94_C30_002290_2024-01-24_3955", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L94_C30_DAEWOOE_C_2024_MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE_POSITIVE", "trigger_id": "R10L94_C30_DAEWOOE_C_2024_STAGE2_ACTIONABLE_MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE", "symbol": "047040", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 25, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 65, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 55, "margin_bridge_score": 50, "revision_score": 45, "relative_strength_score": 55, "customer_quality_score": 35, "policy_or_regulatory_score": 20, "valuation_repricing_score": 45, "execution_risk_score": 40, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "major_builder_order_backlog_funding_positive", "MFE_90D_pct": 6.91, "MAE_90D_pct": -8.44, "score_return_alignment_label": "major_builder_order_backlog_funding_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L94_C30_CAMUSENC_2024_SMALL_BUILDER_PF_NORMALIZATION_FALSE_STAGE2", "trigger_id": "R10L94_C30_CAMUSENC_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_NORMALIZATION_WATCH", "symbol": "013700", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 25, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "small_builder_PF_normalization_false_stage2", "MFE_90D_pct": 10.76, "MAE_90D_pct": -6.96, "score_return_alignment_label": "small_builder_PF_normalization_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_small_builder_PF_normalization_watch_counts_without_cashflow_order_funding_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L94_C30_SAMIL_2024_REGIONAL_BUILDER_POLICY_EVENT_CAP_4B", "trigger_id": "R10L94_C30_SAMIL_2024_STAGE4B_REGIONAL_BUILDER_POLICY_EVENT_CAP", "symbol": "002290", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 25, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "regional_builder_policy_event_cap_4B_guard", "MFE_90D_pct": 5.69, "MAE_90D_pct": -14.29, "score_return_alignment_label": "regional_builder_policy_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_regional_builder_policy_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": "94", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MAJOR_BUILDER_ORDER_BACKLOG_FUNDING_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_REGIONAL_BUILDER_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["major_builder_order_backlog_funding_positive", "small_builder_PF_normalization_false_stage2", "regional_builder_policy_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C30 rows need explicit PF cashflow, funding capacity, order quality, project mix, balance-sheet visibility, margin or revision bridge before positive promotion.
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
completed_loop = 94
next_round = R11
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
