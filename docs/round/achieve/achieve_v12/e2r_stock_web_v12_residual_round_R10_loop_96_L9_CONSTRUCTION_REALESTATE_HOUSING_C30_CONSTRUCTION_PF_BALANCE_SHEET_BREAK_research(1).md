# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R10
scheduled_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_LOCAL_BUILDER_PF_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R10_loop_96_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

This file is the corrected final output for this execution. The scheduler state after R9 loop 96 is R10 / loop 96. R10 is the L9 construction / real-estate / housing round, and this run fills C30 construction PF balance-sheet break behavior rather than repeating the immediately preceding R10 loop 95 C30 symbols or top-covered PF/building names.

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
scheduled_loop = 96
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
round_sector_consistency = pass
computed_next_round = R11
computed_next_loop = 96
```

C30 is a PF/cashflow repair archetype. A construction or housing-recovery label is only a crane silhouette; the building stands only when order quality, funding repair, cash conversion, balance-sheet safety, margin and revision hold together.

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
previous R10 loop-95 symbols avoided: 053690, 054930, 034300
previous R9 loop-96 C29 symbols avoided: 204320, 118990, 317120
```

Selected rows avoid hard duplicates and top repeated C30 symbols:

```text
010960 / Stage2-Actionable / 2024-01-31
017000 / Stage2-Actionable / 2024-01-02
091590 / Stage4B / 2024-01-02
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
| 010960 | atlas/symbol_profiles/010/010960.json | selected 2024 window clean after old 2008/2010 CA candidates |
| 017000 | atlas/symbol_profiles/017/017000.json | selected 2024 window clean after old CA candidates |
| 091590 | atlas/symbol_profiles/091/091590.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R10L96_C30_SAMHODEV_2024_CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE_POSITIVE | 010960 | 2024-01-31 | yes | 180 | yes | yes | true |
| R10L96_C30_SHINWONDEV_2024_SMALL_BUILDER_PF_FALSE_STAGE2 | 017000 | 2024-01-02 | yes | 180 | yes | yes | true |
| R10L96_C30_NAMHWA_2024_LOCAL_BUILDER_PF_EVENT_CAP_4B | 091590 | 2024-01-02 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE | Positive Stage2 requires order quality, fee/subcontract visibility, cashflow safety, balance-sheet discipline, margin and revision bridge. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | SMALL_BUILDER_PF_FALSE_STAGE2 | Small-builder PF recovery watch without cashflow/funding bridge can become false Stage2. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | LOCAL_BUILDER_PF_EVENT_CAP_4B | Local-builder PF event premium should route to 4B when cashflow, funding and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R10L96_C30_SAMHODEV_2024_CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE_POSITIVE | 010960 | 삼호개발 | positive | Civil-engineering order/cashflow bridge produced moderate MFE with shallow MAE. |
| R10L96_C30_SHINWONDEV_2024_SMALL_BUILDER_PF_FALSE_STAGE2 | 017000 | 신원종합개발 | counterexample | Small-builder PF recovery watch had brief premium and persistent drawdown. |
| R10L96_C30_NAMHWA_2024_LOCAL_BUILDER_PF_EVENT_CAP_4B | 091590 | 남화토건 | counterexample / 4B | Local-builder PF event premium capped on first-trading-day spike and de-rated deeply. |

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
| Samho Development civil-engineering order/cashflow bridge | historical public/report proxy | true | true | shadow-only positive |
| Shinwon Development small-builder PF false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Namhwa Construction local-builder PF event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 010960 | atlas/ohlcv_tradable_by_symbol_year/010/010960/2024.csv | atlas/symbol_profiles/010/010960.json |
| 017000 | atlas/ohlcv_tradable_by_symbol_year/017/017000/2024.csv | atlas/symbol_profiles/017/017000.json |
| 091590 | atlas/ohlcv_tradable_by_symbol_year/091/091590/2024.csv | atlas/symbol_profiles/091/091590.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R10L96_C30_SAMHODEV_2024_STAGE2_ACTIONABLE_CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE | 010960 | Stage2-Actionable | 2024-01-31 | 3260 | positive | civil-engineering order/cashflow bridge worked |
| R10L96_C30_SHINWONDEV_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_RECOVERY_WATCH | 017000 | Stage2-Actionable | 2024-01-02 | 3595 | counterexample | small-builder PF false Stage2 |
| R10L96_C30_NAMHWA_2024_STAGE4B_LOCAL_BUILDER_PF_EVENT_CAP | 091590 | Stage4B | 2024-01-02 | 7140 | counterexample/4B | local-builder PF event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R10L96_C30_SAMHODEV_2024_STAGE2_ACTIONABLE_CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE | 3260 | 8.28 | -1.99 | 9.36 | -1.99 | 11.96 | -5.21 | 2024-07-30 | 3650 | -15.34 |
| R10L96_C30_SHINWONDEV_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_RECOVERY_WATCH | 3595 | 1.81 | -20.31 | 1.81 | -23.23 | 1.81 | -39.64 | 2024-01-04 | 3660 | -40.71 |
| R10L96_C30_NAMHWA_2024_STAGE4B_LOCAL_BUILDER_PF_EVENT_CAP | 7140 | 1.68 | -18.91 | 1.68 | -32.98 | 1.68 | -42.44 | 2024-01-02 | 7260 | -43.39 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C30 Stage2 needs order quality / cashflow / funding / balance-sheet / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing small-builder and local-builder PF premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE construction/PF rows cannot promote without durable cashflow bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether construction/PF narrative becomes order/cashflow repair.

| symbol | stage quality | explanation |
|---|---|---|
| 010960 | good_stage2_with_later_watch | Order/cashflow bridge produced moderate MFE and shallow MAE. |
| 017000 | bad_stage2 | Small-builder PF watch lacked cashflow/funding bridge and later suffered high MAE. |
| 091590 | good_4B | Local-builder PF premium capped immediately and then drew down deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 017000 small-builder PF false Stage2 | 0.98 | 0.98 | false Stage2 due missing cashflow/funding/order/margin bridge |
| 091590 local-builder PF cap | 0.98 | 0.98 | good full-window 4B timing after first-trading-day local-builder PF event premium |
| 010960 civil-engineering bridge | n/a | n/a | positive Stage2, but later civil-engineering valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 017000 / 091590
```

No hard 4C candidate is introduced in this R10 loop 96 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L9 construction/PF balance-sheet cases, Stage2 requires verified order quality, fee/subcontract visibility, PF cashflow repair, funding capacity, balance-sheet safety, margin, or revision bridge. Small-builder, local-builder, construction-recovery, housing, civil-engineering or PF label alone remains watch/4B/4C.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rule = C30 should split true order/cashflow/funding positives from small-builder PF false Stage2 and local-builder event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 4.28 | -19.40 | 0.67 | mixed; C30 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 4.28 | -19.40 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L9 order/cashflow/funding bridge required | 2 | 5.59 | -12.61 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C30 bridge vs event-cap split | 2 | 5.59 | -12.61 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing construction/PF themes as positive | 1 | 9.36 | -1.99 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 010960 civil-engineering bridge | 64 | Stage2-Watch | 72 | Stage2-Actionable | 9.36 | -1.99 | civil_engineering_order_cashflow_positive |
| 017000 small-builder PF false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 1.81 | -23.23 | small_builder_PF_false_stage2 |
| 091590 local-builder PF cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 1.68 | -32.98 | local_builder_PF_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_LOCAL_BUILDER_PF_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C30 Samho Development civil-engineering order/cashflow positive, Shinwon Development small-builder PF false Stage2, and Namhwa Construction local-builder PF event-cap 4B while avoiding top repeated C30 and previous R10/R9 loop symbols."}
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
residual_error_types_found: civil_engineering_order_cashflow_positive, small_builder_PF_false_stage2, local_builder_PF_event_cap_4B
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
shadow_weight,stage2_required_bridge,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,C30_requires_order_quality_cashflow_funding_balance_sheet_margin_revision_bridge,0,"C30 Stage2 should require order quality, fee/subcontract visibility, PF cashflow repair, funding capacity, balance-sheet safety, margin, or revision bridge, not construction/PF recovery label alone","Samho Development positive worked; Shinwon Development and Namhwa Construction event/watch rows failed positive-stage promotion","R10L96_C30_SAMHODEV_2024_STAGE2_ACTIONABLE_CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE|R10L96_C30_SHINWONDEV_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_RECOVERY_WATCH|R10L96_C30_NAMHWA_2024_STAGE4B_LOCAL_BUILDER_PF_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,cap_bridge_missing_small_builder_PF_event_premiums_as_4B_watch,0,"Small-builder and local-builder PF event premiums can peak before funding, cashflow and margin bridge is proven","Shinwon Development had brief MFE then persistent drawdown; Namhwa Construction showed 4B event-cap behavior from the first trading-day spike","R10L96_C30_SHINWONDEV_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_RECOVERY_WATCH|R10L96_C30_NAMHWA_2024_STAGE4B_LOCAL_BUILDER_PF_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,block_positive_stage_when_construction_PF_theme_has_high_or_persistent_MAE_without_cashflow_bridge,0,"High or persistent MAE after bridge-missing C30 entries should block Stage2/Stage3 promotion unless order, cashflow, funding and margin evidence survives","Shinwon Development MAE180=-39.64 and Namhwa Construction MAE90=-32.98","R10L96_C30_SHINWONDEV_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_RECOVERY_WATCH|R10L96_C30_NAMHWA_2024_STAGE4B_LOCAL_BUILDER_PF_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R10L96_C30_SAMHODEV_2024_CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE_POSITIVE", "symbol": "010960", "company_name": "삼호개발", "round": "R10", "loop": "96", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_LOCAL_BUILDER_PF_EVENT_CAP", "case_type": "moderate_structural_success_with_later_civil_engineering_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R10L96_C30_SAMHODEV_2024_STAGE2_ACTIONABLE_CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Civil-engineering / subcontract order quality and cashflow-safety bridge produced a moderate 90D/180D MFE path with shallow early MAE. C30 can work when construction/PF narrative maps into order quality, fee or subcontract backlog, cash conversion, balance-sheet safety, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C30_positive_requires_order_quality_cashflow_fee_visibility_margin_revision_bridge_not_construction_theme_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2008/2010 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R10L96_C30_SHINWONDEV_2024_SMALL_BUILDER_PF_FALSE_STAGE2", "symbol": "017000", "company_name": "신원종합개발", "round": "R10", "loop": "96", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_LOCAL_BUILDER_PF_EVENT_CAP", "case_type": "failed_rerating_small_builder_PF_recovery_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R10L96_C30_SHINWONDEV_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_RECOVERY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Small-builder PF recovery watch had only a brief early premium and then a persistent drawdown. C30 Stage2 should not be awarded without verified PF cashflow repair, funding capacity, order backlog quality, balance-sheet safety, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_small_builder_PF_recovery_watch_counts_without_cashflow_funding_order_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R10L96_C30_NAMHWA_2024_LOCAL_BUILDER_PF_EVENT_CAP_4B", "symbol": "091590", "company_name": "남화토건", "round": "R10", "loop": "96", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_LOCAL_BUILDER_PF_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R10L96_C30_NAMHWA_2024_STAGE4B_LOCAL_BUILDER_PF_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Local-builder / construction-PF event premium capped on the first trading-day spike and then de-rated deeply. C30 should route bridge-missing builder/PF event premiums to 4B unless order quality, funding repair, cash conversion, balance-sheet safety, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_local_builder_PF_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R10L96_C30_SAMHODEV_2024_STAGE2_ACTIONABLE_CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE", "case_id": "R10L96_C30_SAMHODEV_2024_CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE_POSITIVE", "symbol": "010960", "company_name": "삼호개발", "round": "R10", "loop": "96", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_LOCAL_BUILDER_PF_EVENT_CAP", "sector": "civil_engineering_subcontract_order_cashflow_balance_sheet", "primary_archetype": "order_quality_cashflow_fee_visibility_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-31", "entry_date": "2024-01-31", "entry_price": 3260.0, "evidence_available_at_that_date": "civil-engineering order/subcontract quality, cashflow safety, balance-sheet discipline and margin/revision bridge proxy after January washout; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["order_quality_proxy", "subcontract_backlog_visibility_proxy", "cashflow_safety_proxy", "balance_sheet_safety_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["moderate_MFE30", "moderate_MFE90", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_civil_engineering_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010960/2024.csv", "profile_path": "atlas/symbol_profiles/010/010960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.28, "MFE_90D_pct": 9.36, "MFE_180D_pct": 11.96, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.99, "MAE_90D_pct": -1.99, "MAE_180D_pct": -5.21, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-30", "peak_price": 3650.0, "drawdown_after_peak_pct": -15.34, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_civil_engineering_valuation_4B_watch_needed", "four_b_evidence_type": ["order_cashflow_bridge", "balance_sheet_safety", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_civil_engineering_order_cashflow_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2008_2010_CA", "same_entry_group_id": "R10L96_C30_010960_2024-01-31_3260", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L96_C30_SHINWONDEV_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_RECOVERY_WATCH", "case_id": "R10L96_C30_SHINWONDEV_2024_SMALL_BUILDER_PF_FALSE_STAGE2", "symbol": "017000", "company_name": "신원종합개발", "round": "R10", "loop": "96", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_LOCAL_BUILDER_PF_EVENT_CAP", "sector": "small_builder_PF_recovery_cashflow_watch", "primary_archetype": "small_builder_PF_watch_without_cashflow_funding_order_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "entry_date": "2024-01-02", "entry_price": 3595.0, "evidence_available_at_that_date": "small-builder PF recovery / housing recovery watch without confirmed funding repair, order backlog quality, cash conversion, balance-sheet safety or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["small_builder_PF_recovery_watch", "housing_recovery_sympathy", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["brief_MFE_then_persistent_MAE", "cashflow_funding_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/017/017000/2024.csv", "profile_path": "atlas/symbol_profiles/017/017000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.81, "MFE_90D_pct": 1.81, "MFE_180D_pct": 1.81, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -20.31, "MAE_90D_pct": -23.23, "MAE_180D_pct": -39.64, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-04", "peak_price": 3660.0, "drawdown_after_peak_pct": -40.71, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "small_builder_PF_recovery_watch_was_false_stage2_due_missing_cashflow_funding_order_margin_bridge", "four_b_evidence_type": ["small_builder_PF_premium", "bridge_missing", "persistent_drawdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_small_builder_PF_recovery_watch_without_cashflow_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_small_builder_PF_recovery_watch_counts_without_cashflow_funding_order_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA_candidates", "same_entry_group_id": "R10L96_C30_017000_2024-01-02_3595", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L96_C30_NAMHWA_2024_STAGE4B_LOCAL_BUILDER_PF_EVENT_CAP", "case_id": "R10L96_C30_NAMHWA_2024_LOCAL_BUILDER_PF_EVENT_CAP_4B", "symbol": "091590", "company_name": "남화토건", "round": "R10", "loop": "96", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_LOCAL_BUILDER_PF_EVENT_CAP", "sector": "local_builder_PF_housing_recovery_event_premium", "primary_archetype": "local_builder_PF_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-02", "entry_date": "2024-01-02", "entry_price": 7140.0, "evidence_available_at_that_date": "local builder / construction PF event premium after first-trading-day spike without visible order quality, funding repair, cash conversion or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["local_builder_PF_event", "construction_recovery_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "cashflow_funding_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/091/091590/2024.csv", "profile_path": "atlas/symbol_profiles/091/091590.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.68, "MFE_90D_pct": 1.68, "MFE_180D_pct": 1.68, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -18.91, "MAE_90D_pct": -32.98, "MAE_180D_pct": -42.44, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-02", "peak_price": 7260.0, "drawdown_after_peak_pct": -43.39, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing_local_builder_PF_event_cap", "four_b_evidence_type": ["local_builder_PF_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_local_builder_PF_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_local_builder_PF_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R10L96_C30_091590_2024-01-02_7140", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L96_C30_SAMHODEV_2024_CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE_POSITIVE", "trigger_id": "R10L96_C30_SAMHODEV_2024_STAGE2_ACTIONABLE_CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE", "symbol": "010960", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 55, "customer_quality_score": 35, "policy_or_regulatory_score": 20, "valuation_repricing_score": 50, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 64, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 40, "backlog_visibility_score": 50, "margin_bridge_score": 50, "revision_score": 45, "relative_strength_score": 55, "customer_quality_score": 45, "policy_or_regulatory_score": 20, "valuation_repricing_score": 40, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "civil_engineering_order_cashflow_positive", "MFE_90D_pct": 9.36, "MAE_90D_pct": -1.99, "score_return_alignment_label": "civil_engineering_order_cashflow_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L96_C30_SHINWONDEV_2024_SMALL_BUILDER_PF_FALSE_STAGE2", "trigger_id": "R10L96_C30_SHINWONDEV_2024_STAGE2_FALSE_POSITIVE_SMALL_BUILDER_PF_RECOVERY_WATCH", "symbol": "017000", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 65, "customer_quality_score": 20, "policy_or_regulatory_score": 30, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "small_builder_PF_false_stage2", "MFE_90D_pct": 1.81, "MAE_90D_pct": -23.23, "score_return_alignment_label": "small_builder_PF_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_small_builder_PF_recovery_watch_counts_without_cashflow_funding_order_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L96_C30_NAMHWA_2024_LOCAL_BUILDER_PF_EVENT_CAP_4B", "trigger_id": "R10L96_C30_NAMHWA_2024_STAGE4B_LOCAL_BUILDER_PF_EVENT_CAP", "symbol": "091590", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 30, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "local_builder_PF_event_cap_4B_guard", "MFE_90D_pct": 1.68, "MAE_90D_pct": -32.98, "score_return_alignment_label": "local_builder_PF_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_local_builder_PF_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": "96", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CIVIL_ENGINEERING_ORDER_CASHFLOW_BRIDGE_VS_SMALL_BUILDER_PF_FALSE_STAGE2_AND_LOCAL_BUILDER_PF_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["civil_engineering_order_cashflow_positive", "small_builder_PF_false_stage2", "local_builder_PF_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C30 rows need explicit order quality, fee/subcontract visibility, PF cashflow repair, funding capacity, balance-sheet safety, margin or revision bridge before positive promotion.
- In C30, bridge-missing construction/PF event-premium rows with low MFE/high MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C30 construction/PF rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R10
completed_loop = 96
next_round = R11
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
