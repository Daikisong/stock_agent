# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R10
scheduled_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = CONSTRUCTION_MANAGEMENT_ORDER_CASHFLOW_BRIDGE_VS_ENGINEERING_PF_NORMALIZATION_FALSE_STAGE2_AND_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R10_loop_95_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

This file is the corrected final output for this execution. The scheduler state after R9 loop 95 is R10 / loop 95. R10 is the L9 construction / real-estate / housing round, and this run fills C30 construction PF balance-sheet break behavior rather than repeating the immediately preceding R10 loop 94 C30 major-builder PF bridge file.

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
scheduled_round = R10
scheduled_loop = 95
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
round_sector_consistency = pass
computed_next_round = R11
computed_next_loop = 95
```

C30 is a balance-sheet repair archetype. A PF-normalization headline is only scaffolding; the building stands only when order quality, fee/backlog visibility, funding capacity, cash conversion, balance-sheet safety, margin and revision are visible.

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
previous R10 loop-94 symbols avoided: 047040, 013700, 002290
previous R9 loop-95 C14 symbols avoided: 361610, 393890, 025900
```

Selected rows avoid hard duplicates and top repeated C30 symbols:

```text
053690 / Stage2-Actionable / 2024-04-16
054930 / Stage2-Actionable / 2024-02-13
034300 / Stage4B / 2024-05-29
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
| 053690 | atlas/symbol_profiles/053/053690.json | no corporate-action candidate |
| 054930 | atlas/symbol_profiles/054/054930.json | selected 2024 window clean after old 2002/2003 CA candidates |
| 034300 | atlas/symbol_profiles/034/034300.json | post-2024-02-06 CA-candidate boundary clean window with later inactive-like caveat |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R10L95_C30_HANMIGLOBAL_2024_CM_ORDER_CASHFLOW_BRIDGE_POSITIVE | 053690 | 2024-04-16 | yes | 180 | yes | yes | true |
| R10L95_C30_YOOSHIN_2024_ENGINEERING_PF_NORMALIZATION_FALSE_STAGE2 | 054930 | 2024-02-13 | yes | 180 | yes | yes | true |
| R10L95_C30_SHINSEGAEEC_2024_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP_4B | 034300 | 2024-05-29 | yes | 180 | yes | caveated-clean | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | CONSTRUCTION_MANAGEMENT_ORDER_CASHFLOW_BRIDGE | Positive Stage2 requires order quality, fee/backlog visibility, cashflow safety, margin and revision bridge. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | ENGINEERING_PF_FALSE_STAGE2 | Engineering/PF-normalization watch without order/fee/cashflow bridge can become false Stage2. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP_4B | Post-CA PF rescue / restructuring premium should route to 4B when cashflow, ownership and funding bridge are unclear. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R10L95_C30_HANMIGLOBAL_2024_CM_ORDER_CASHFLOW_BRIDGE_POSITIVE | 053690 | 한미글로벌 | positive | Construction management order/cashflow bridge produced clean MFE with shallow initial MAE. |
| R10L95_C30_YOOSHIN_2024_ENGINEERING_PF_NORMALIZATION_FALSE_STAGE2 | 054930 | 유신 | counterexample | Engineering/PF-normalization rebound had low MFE and no durable order/fee bridge. |
| R10L95_C30_SHINSEGAEEC_2024_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP_4B | 034300 | 신세계건설 | counterexample / 4B | Post-CA PF rescue event premium required 4B treatment because it was not a clean balance-sheet repair. |

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
| HanmiGlobal CM order/cashflow bridge | historical public/report proxy | true | true | shadow-only positive |
| Yooshin engineering PF-normalization false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Shinsegae E&C post-CA PF rescue event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 053690 | atlas/ohlcv_tradable_by_symbol_year/053/053690/2024.csv | atlas/symbol_profiles/053/053690.json |
| 054930 | atlas/ohlcv_tradable_by_symbol_year/054/054930/2024.csv | atlas/symbol_profiles/054/054930.json |
| 034300 | atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv | atlas/symbol_profiles/034/034300.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R10L95_C30_HANMIGLOBAL_2024_STAGE2_ACTIONABLE_CM_ORDER_CASHFLOW_BRIDGE | 053690 | Stage2-Actionable | 2024-04-16 | 14540 | positive | construction management order/cashflow bridge worked |
| R10L95_C30_YOOSHIN_2024_STAGE2_FALSE_POSITIVE_ENGINEERING_PF_NORMALIZATION_WATCH | 054930 | Stage2-Actionable | 2024-02-13 | 31450 | counterexample | engineering PF-normalization false Stage2 |
| R10L95_C30_SHINSEGAEEC_2024_STAGE4B_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP | 034300 | Stage4B | 2024-05-29 | 14700 | counterexample/4B | post-CA retail-builder PF rescue event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R10L95_C30_HANMIGLOBAL_2024_STAGE2_ACTIONABLE_CM_ORDER_CASHFLOW_BRIDGE | 14540 | 13.34 | -0.41 | 33.63 | -0.41 | 33.63 | -0.41 | 2024-05-28 | 19430 | -15.18 |
| R10L95_C30_YOOSHIN_2024_STAGE2_FALSE_POSITIVE_ENGINEERING_PF_NORMALIZATION_WATCH | 31450 | 2.38 | -8.90 | 7.00 | -18.60 | 7.00 | -18.60 | 2024-06-07 | 33650 | -20.21 |
| R10L95_C30_SHINSEGAEEC_2024_STAGE4B_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP | 14700 | 26.87 | -20.48 | 31.16 | -24.15 | 31.16 | -24.15 | 2024-07-15 | 19280 | -42.17 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C30 Stage2 needs order quality / fee visibility / cashflow / funding / margin / revision bridge |
| local_4b_watch_guard | strengthen: PF rescue or post-CA builder event premiums should route to 4B when cashflow bridge is unclear |
| high_MAE_guardrail | strengthen: meaningful MAE or later inactive-like risk blocks positive-stage promotion |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether construction/PF narrative becomes order/cashflow repair.

| symbol | stage quality | explanation |
|---|---|---|
| 053690 | good_stage2_with_later_watch | Order/fee/cashflow bridge produced clean MFE and tiny MAE. |
| 054930 | bad_stage2 | Engineering/PF rebound lacked order/fee bridge and did not compound. |
| 034300 | good_4B | PF rescue premium was event-driven and caveated by post-CA / later inactive-like risk. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 054930 engineering false Stage2 | 0.93 | 0.93 | false Stage2 due missing order/fee/cashflow bridge |
| 034300 retail-builder rescue cap | 0.76 | 0.76 | acceptable 4B because post-CA PF rescue mechanics, not clean balance-sheet repair, dominated |
| 053690 CM order/cashflow bridge | n/a | n/a | positive Stage2, but later construction-management valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 054930 / 034300
```

No hard 4C candidate is introduced in this R10 loop 95 file. The Shinsegae E&C row is kept as 4B rather than 4C because the post-CA/restructuring path had event mechanics but did not yet represent a fully confirmed thesis break at the selected entry date.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L9 construction/PF balance-sheet cases, Stage2 requires verified order quality, fee/backlog visibility, PF cashflow repair, funding capacity, balance-sheet safety, margin, or revision bridge. PF normalization, rescue financing, retail-builder rebound, engineering policy, construction-management theme or post-CA event premium alone remains watch/4B/4C.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rule = C30 should split true order/cashflow/funding positives from engineering PF-normalization false Stage2 and post-CA builder rescue event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 23.93 | -14.39 | 0.67 | mixed; C30 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 23.93 | -14.39 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L9 order/cashflow/funding bridge required | 2 | 20.32 | -9.51 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C30 bridge vs event-cap split | 2 | 20.32 | -9.51 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing construction/PF themes as positive | 1 | 33.63 | -0.41 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 053690 CM order/cashflow bridge | 64 | Stage2-Watch | 74 | Stage2-Actionable | 33.63 | -0.41 | construction_management_order_cashflow_positive |
| 054930 engineering PF false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 7.00 | -18.60 | engineering_PF_normalization_false_stage2 |
| 034300 retail-builder rescue cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 31.16 | -24.15 | retail_builder_PF_rescue_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CONSTRUCTION_MANAGEMENT_ORDER_CASHFLOW_BRIDGE_VS_ENGINEERING_PF_NORMALIZATION_FALSE_STAGE2_AND_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C30 HanmiGlobal construction-management order/cashflow positive, Yooshin engineering PF-normalization false Stage2, and Shinsegae E&C post-CA retail-builder PF rescue event-cap 4B split while avoiding top repeated C30 and previous R10/R9 loop symbols."}
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
residual_error_types_found: construction_management_order_cashflow_positive, engineering_PF_normalization_false_stage2, retail_builder_post_CA_PF_rescue_event_cap_4B
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
shadow_weight,stage2_required_bridge,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,C30_requires_order_quality_fee_visibility_cashflow_funding_margin_revision_bridge,0,"C30 Stage2 should require order quality, fee/backlog visibility, PF cashflow repair, funding capacity, balance-sheet safety, margin, or revision bridge, not construction/PF normalization label alone","HanmiGlobal positive worked; Yooshin and Shinsegae E&C event/watch rows failed positive-stage promotion","R10L95_C30_HANMIGLOBAL_2024_STAGE2_ACTIONABLE_CM_ORDER_CASHFLOW_BRIDGE|R10L95_C30_YOOSHIN_2024_STAGE2_FALSE_POSITIVE_ENGINEERING_PF_NORMALIZATION_WATCH|R10L95_C30_SHINSEGAEEC_2024_STAGE4B_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,cap_bridge_missing_PF_rescue_and_small_engineering_event_premiums_as_4B_watch,0,"PF rescue, post-CA builder restructuring and engineering-policy rebounds can peak before cashflow, ownership and margin bridge is proven","Yooshin had low MFE after PF-normalization watch; Shinsegae E&C showed a post-CA PF-rescue event-cap pattern with later inactive-like risk","R10L95_C30_YOOSHIN_2024_STAGE2_FALSE_POSITIVE_ENGINEERING_PF_NORMALIZATION_WATCH|R10L95_C30_SHINSEGAEEC_2024_STAGE4B_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,block_positive_stage_when_construction_PF_theme_has_MAE_or_listing_risk_without_cashflow_bridge,0,"High or meaningful MAE, ownership uncertainty or later inactive-like risk after bridge-missing C30 entries should block Stage2/Stage3 promotion unless cashflow and funding evidence survives","Yooshin MAE90=-18.60 and Shinsegae E&C MAE90=-24.15 with later inactive-like caveat","R10L95_C30_YOOSHIN_2024_STAGE2_FALSE_POSITIVE_ENGINEERING_PF_NORMALIZATION_WATCH|R10L95_C30_SHINSEGAEEC_2024_STAGE4B_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R10L95_C30_HANMIGLOBAL_2024_CM_ORDER_CASHFLOW_BRIDGE_POSITIVE", "symbol": "053690", "company_name": "한미글로벌", "round": "R10", "loop": "95", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CONSTRUCTION_MANAGEMENT_ORDER_CASHFLOW_BRIDGE_VS_ENGINEERING_PF_NORMALIZATION_FALSE_STAGE2_AND_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP", "case_type": "moderate_structural_success_with_later_construction_management_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R10L95_C30_HANMIGLOBAL_2024_STAGE2_ACTIONABLE_CM_ORDER_CASHFLOW_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Construction management / overseas project order and cashflow bridge produced a clean MFE path from the April washout with shallow initial MAE. C30 can work when construction/PF narrative maps into order quality, fee visibility, cash conversion, balance-sheet safety, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C30_positive_requires_order_quality_cashflow_fee_visibility_margin_revision_bridge_not_construction_theme_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R10L95_C30_YOOSHIN_2024_ENGINEERING_PF_NORMALIZATION_FALSE_STAGE2", "symbol": "054930", "company_name": "유신", "round": "R10", "loop": "95", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CONSTRUCTION_MANAGEMENT_ORDER_CASHFLOW_BRIDGE_VS_ENGINEERING_PF_NORMALIZATION_FALSE_STAGE2_AND_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP", "case_type": "failed_rerating_engineering_PF_normalization_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R10L95_C30_YOOSHIN_2024_STAGE2_FALSE_POSITIVE_ENGINEERING_PF_NORMALIZATION_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Engineering / construction policy rebound watch did not produce a durable Stage2 profile. It needed order conversion, fee backlog, execution margin and cashflow bridge; without those, the rebound became false Stage2.", "current_profile_verdict": "current_profile_false_positive_if_engineering_PF_normalization_watch_counts_without_order_fee_cashflow_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2002/2003 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R10L95_C30_SHINSEGAEEC_2024_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP_4B", "symbol": "034300", "company_name": "신세계건설", "round": "R10", "loop": "95", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CONSTRUCTION_MANAGEMENT_ORDER_CASHFLOW_BRIDGE_VS_ENGINEERING_PF_NORMALIZATION_FALSE_STAGE2_AND_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP", "case_type": "event_cap_4b_counterexample_with_post_CA_boundary", "positive_or_counterexample": "counterexample", "best_trigger": "R10L95_C30_SHINSEGAEEC_2024_STAGE4B_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Retail-builder / PF rescue and post-corporate-action event premium needed 4B treatment. The price spike produced MFE, but the bridge was not a normal order/cashflow rerating; PF funding, ownership path, rescue mechanics and later delisting-like behavior made it unsuitable as a positive Stage2 proof.", "current_profile_verdict": "current_profile_4B_too_late_if_retail_builder_PF_rescue_event_premium_is_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Profile flags a 2024-02-06 corporate-action candidate. Entry is after that boundary, so the post-boundary 180D window is used with caveat. Later inactive-like status is treated as risk context, not as a live signal."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R10L95_C30_HANMIGLOBAL_2024_STAGE2_ACTIONABLE_CM_ORDER_CASHFLOW_BRIDGE", "case_id": "R10L95_C30_HANMIGLOBAL_2024_CM_ORDER_CASHFLOW_BRIDGE_POSITIVE", "symbol": "053690", "company_name": "한미글로벌", "round": "R10", "loop": "95", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CONSTRUCTION_MANAGEMENT_ORDER_CASHFLOW_BRIDGE_VS_ENGINEERING_PF_NORMALIZATION_FALSE_STAGE2_AND_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP", "sector": "construction_management_order_fee_cashflow", "primary_archetype": "order_quality_fee_visibility_cashflow_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-16", "entry_date": "2024-04-16", "entry_price": 14540.0, "evidence_available_at_that_date": "construction management / overseas project fee visibility, order conversion, cashflow safety and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["order_quality_proxy", "fee_backlog_visibility_proxy", "cashflow_safety_proxy", "execution_margin_bridge_proxy", "revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "strong_MFE90", "controlled_MAE90"], "stage4b_evidence_fields": ["later_construction_management_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053690/2024.csv", "profile_path": "atlas/symbol_profiles/053/053690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.34, "MFE_90D_pct": 33.63, "MFE_180D_pct": 33.63, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -0.41, "MAE_90D_pct": -0.41, "MAE_180D_pct": -0.41, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-28", "peak_price": 19430.0, "drawdown_after_peak_pct": -15.18, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_construction_management_valuation_4B_watch_needed", "four_b_evidence_type": ["order_fee_bridge", "cashflow_visibility", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_construction_management_order_cashflow_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R10L95_C30_053690_2024-04-16_14540", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L95_C30_YOOSHIN_2024_STAGE2_FALSE_POSITIVE_ENGINEERING_PF_NORMALIZATION_WATCH", "case_id": "R10L95_C30_YOOSHIN_2024_ENGINEERING_PF_NORMALIZATION_FALSE_STAGE2", "symbol": "054930", "company_name": "유신", "round": "R10", "loop": "95", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CONSTRUCTION_MANAGEMENT_ORDER_CASHFLOW_BRIDGE_VS_ENGINEERING_PF_NORMALIZATION_FALSE_STAGE2_AND_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP", "sector": "engineering_consulting_PF_normalization_watch", "primary_archetype": "engineering_PF_rebound_without_order_fee_cashflow_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "entry_date": "2024-02-13", "entry_price": 31450.0, "evidence_available_at_that_date": "engineering / construction policy rebound watch without confirmed order conversion, fee backlog, cashflow or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["engineering_policy_rebound_watch", "construction_PF_normalization_theme", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "MAE90_after_watch", "order_fee_cashflow_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/054/054930/2024.csv", "profile_path": "atlas/symbol_profiles/054/054930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.38, "MFE_90D_pct": 7.0, "MFE_180D_pct": 7.0, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -8.9, "MAE_90D_pct": -18.6, "MAE_180D_pct": -18.6, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-07", "peak_price": 33650.0, "drawdown_after_peak_pct": -20.21, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "engineering_PF_normalization_watch_was_false_stage2_due_missing_order_fee_cashflow_margin_bridge", "four_b_evidence_type": ["construction_policy_rebound", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_engineering_PF_normalization_without_order_cashflow_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_engineering_PF_normalization_watch_counts_without_order_fee_cashflow_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2002_2003_CA", "same_entry_group_id": "R10L95_C30_054930_2024-02-13_31450", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L95_C30_SHINSEGAEEC_2024_STAGE4B_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP", "case_id": "R10L95_C30_SHINSEGAEEC_2024_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP_4B", "symbol": "034300", "company_name": "신세계건설", "round": "R10", "loop": "95", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CONSTRUCTION_MANAGEMENT_ORDER_CASHFLOW_BRIDGE_VS_ENGINEERING_PF_NORMALIZATION_FALSE_STAGE2_AND_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP", "sector": "retail_builder_PF_rescue_post_CA_event_premium", "primary_archetype": "retail_builder_post_CA_rescue_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-05-29", "entry_date": "2024-05-29", "entry_price": 14700.0, "evidence_available_at_that_date": "retail-builder PF rescue / post-corporate-action event premium after May spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["retail_builder_PF_rescue_event", "post_CA_restructuring_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "MAE_recheck", "funding_ownership_cashflow_bridge_recheck"], "stage4c_evidence_fields": ["inactive_like_later_status_watch", "ownership_event_risk_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv", "profile_path": "atlas/symbol_profiles/034/034300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 26.87, "MFE_90D_pct": 31.16, "MFE_180D_pct": 31.16, "MFE_1Y_pct": "not_calculated_due_later_inactive_like_window", "MFE_2Y_pct": "not_calculated_due_later_inactive_like_window", "MAE_30D_pct": -20.48, "MAE_90D_pct": -24.15, "MAE_180D_pct": -24.15, "MAE_1Y_pct": "not_calculated_due_later_inactive_like_window", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-15", "peak_price": 19280.0, "drawdown_after_peak_pct": -42.17, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.76, "four_b_full_window_peak_proximity": 0.76, "four_b_timing_verdict": "acceptable_4B_timing_post_CA_PF_rescue_event_cap_because_non_price_bridge_and_later_listing_risk_dominate", "four_b_evidence_type": ["PF_rescue_event_premium", "post_CA_boundary", "ownership_cashflow_bridge_unclear"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_retail_builder_PF_rescue_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_retail_builder_PF_rescue_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "post_2024-02-06_CA_candidate_boundary_clean_window_with_later_inactive_like_caveat", "same_entry_group_id": "R10L95_C30_034300_2024-05-29_14700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L95_C30_HANMIGLOBAL_2024_CM_ORDER_CASHFLOW_BRIDGE_POSITIVE", "trigger_id": "R10L95_C30_HANMIGLOBAL_2024_STAGE2_ACTIONABLE_CM_ORDER_CASHFLOW_BRIDGE", "symbol": "053690", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 55, "customer_quality_score": 35, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 64, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 40, "backlog_visibility_score": 55, "margin_bridge_score": 50, "revision_score": 50, "relative_strength_score": 65, "customer_quality_score": 45, "policy_or_regulatory_score": 20, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "construction_management_order_cashflow_positive", "MFE_90D_pct": 33.63, "MAE_90D_pct": -0.41, "score_return_alignment_label": "construction_management_order_cashflow_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L95_C30_YOOSHIN_2024_ENGINEERING_PF_NORMALIZATION_FALSE_STAGE2", "trigger_id": "R10L95_C30_YOOSHIN_2024_STAGE2_FALSE_POSITIVE_ENGINEERING_PF_NORMALIZATION_WATCH", "symbol": "054930", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 25, "policy_or_regulatory_score": 35, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "engineering_PF_normalization_false_stage2", "MFE_90D_pct": 7.0, "MAE_90D_pct": -18.6, "score_return_alignment_label": "engineering_PF_normalization_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_engineering_PF_normalization_watch_counts_without_order_fee_cashflow_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L95_C30_SHINSEGAEEC_2024_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP_4B", "trigger_id": "R10L95_C30_SHINSEGAEEC_2024_STAGE4B_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP", "symbol": "034300", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 35, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 30, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 70, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "retail_builder_post_CA_PF_rescue_event_cap_4B_guard", "MFE_90D_pct": 31.16, "MAE_90D_pct": -24.15, "score_return_alignment_label": "retail_builder_PF_rescue_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_retail_builder_PF_rescue_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": "95", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CONSTRUCTION_MANAGEMENT_ORDER_CASHFLOW_BRIDGE_VS_ENGINEERING_PF_NORMALIZATION_FALSE_STAGE2_AND_RETAIL_BUILDER_POST_CA_RESCUE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["construction_management_order_cashflow_positive", "engineering_PF_normalization_false_stage2", "retail_builder_post_CA_PF_rescue_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C30 rows need explicit order quality, fee/backlog visibility, PF cashflow repair, funding capacity, balance-sheet safety, margin or revision bridge before positive promotion.
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
10. Add tests that bridge-missing C30 rows cannot promote positive stages and post-CA PF-rescue premiums remain 4B/watch unless cashflow bridge is proven.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R10
completed_loop = 95
next_round = R11
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
