# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R10
scheduled_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = MID_BUILDER_PF_ORDER_BALANCE_REPAIR_BRIDGE_VS_REGIONAL_BUILDER_FALSE_STAGE2_AND_SMALL_BUILDER_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R10_loop_92_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

This file is the corrected final output for this execution. The scheduler state after R9 loop 92 is R10 / loop 92. R10 is the L9 construction/PF round, so this run uses C30 and avoids the R10 loop 88/89/90/91 symbol sets.

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
scheduled_loop = 92
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
round_sector_consistency = pass
computed_next_round = R11
computed_next_loop = 92
```

R10 loop 91 used 003070 / 001260 / 021320. This loop avoids those symbols and also avoids the top repeated C30 names.

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
previous R9 loop-92 C29 symbols avoided: 073240, 011320, 024900
```

Selected rows avoid hard duplicates and top repeated C30 symbols:

```text
014790 / Stage2-Actionable / 2024-06-03
002780 / Stage2-Actionable / 2024-02-26
002410 / Stage4B / 2024-01-02
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
| 014790 | atlas/symbol_profiles/014/014790.json | selected 2024 window clean after old 1996~2012 CA candidates |
| 002780 | atlas/symbol_profiles/002/002780.json | selected 2024 window clean after old 1998~2015 CA candidates |
| 002410 | atlas/symbol_profiles/002/002410.json | selected 2024 window clean after old 1996~2017 CA candidates; early entry has available 180D window |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R10L92_C30_HLDNI_2024_MID_BUILDER_PF_ORDER_BALANCE_REPAIR_POSITIVE | 014790 | 2024-06-03 | yes | 180 | yes | yes | true |
| R10L92_C30_CHINHUNG_2024_REGIONAL_BUILDER_PF_FALSE_STAGE2 | 002780 | 2024-02-26 | yes | 180 | yes | yes | true |
| R10L92_C30_BUMYANG_2024_SMALL_BUILDER_PF_EVENT_CAP_4B | 002410 | 2024-01-02 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | MID_BUILDER_PF_ORDER_BALANCE_REPAIR_BRIDGE | Positive Stage2 requires PF cashflow repair, funding capacity, order quality, balance-sheet repair, margin and revision bridge. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | REGIONAL_BUILDER_FALSE_STAGE2 | Regional builder/PF recovery label without cashflow and order-quality bridge can become false Stage2. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | SMALL_BUILDER_EVENT_CAP_4B | Small-builder PF event premium should route to 4B when balance repair evidence is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R10L92_C30_HLDNI_2024_MID_BUILDER_PF_ORDER_BALANCE_REPAIR_POSITIVE | 014790 | HL D&I | positive | PF/order balance-repair bridge produced strong MFE with very shallow initial MAE. |
| R10L92_C30_CHINHUNG_2024_REGIONAL_BUILDER_PF_FALSE_STAGE2 | 002780 | 진흥기업 | counterexample | Regional builder/PF watch had only event-like MFE and then large 180D MAE. |
| R10L92_C30_BUMYANG_2024_SMALL_BUILDER_PF_EVENT_CAP_4B | 002410 | 범양건영 | counterexample / 4B | Small-builder PF premium capped at the January spike and then de-rated severely. |

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
| HL D&I PF/order balance repair | historical public/report proxy | true | true | shadow-only positive |
| Chinhung regional-builder PF false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Bumyung small-builder PF event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 014790 | atlas/ohlcv_tradable_by_symbol_year/014/014790/2024.csv | atlas/symbol_profiles/014/014790.json |
| 002780 | atlas/ohlcv_tradable_by_symbol_year/002/002780/2024.csv | atlas/symbol_profiles/002/002780.json |
| 002410 | atlas/ohlcv_tradable_by_symbol_year/002/002410/2024.csv | atlas/symbol_profiles/002/002410.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R10L92_C30_HLDNI_2024_STAGE2_ACTIONABLE_MID_BUILDER_PF_ORDER_BALANCE_REPAIR | 014790 | Stage2-Actionable | 2024-06-03 | 2025 | positive | mid-builder PF/order balance-repair bridge worked |
| R10L92_C30_CHINHUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_BUILDER_PF_WATCH | 002780 | Stage2-Actionable | 2024-02-26 | 1063 | counterexample | regional-builder PF watch false Stage2 |
| R10L92_C30_BUMYANG_2024_STAGE4B_SMALL_BUILDER_PF_EVENT_CAP | 002410 | Stage4B | 2024-01-02 | 2220 | counterexample/4B | small-builder PF event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R10L92_C30_HLDNI_2024_STAGE2_ACTIONABLE_MID_BUILDER_PF_ORDER_BALANCE_REPAIR | 2025 | 31.36 | -0.74 | 42.22 | -0.74 | 42.22 | -0.74 | 2024-08-23 | 2880 | -28.13 |
| R10L92_C30_CHINHUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_BUILDER_PF_WATCH | 1063 | 8.09 | -10.72 | 8.09 | -14.68 | 8.09 | -32.27 | 2024-02-26 | 1149 | -37.34 |
| R10L92_C30_BUMYANG_2024_STAGE4B_SMALL_BUILDER_PF_EVENT_CAP | 2220 | 5.63 | -23.87 | 5.63 | -38.42 | 5.63 | -49.82 | 2024-01-02 | 2345 | -57.36 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C30 Stage2 needs PF cashflow / funding capacity / order-quality / balance repair / margin bridge |
| local_4b_watch_guard | strengthen: regional and small-builder PF event premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: high-MAE construction/PF rows cannot promote without durable balance repair bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is PF cashflow/order/balance bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 014790 | good_stage2_with_later_watch | PF/order balance-repair bridge produced strong MFE and shallow entry MAE. |
| 002780 | bad_stage2 | Regional builder/PF watch had event-like MFE and later drawdown. |
| 002410 | good_4B | Small-builder PF event premium capped and then de-rated severely. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 002780 regional-builder false Stage2 | 0.93 | 0.93 | false Stage2 due missing PF cashflow/order-quality bridge |
| 002410 small-builder PF cap | 1.00 | 1.00 | good full-window 4B timing |
| 014790 PF/order bridge | n/a | n/a | positive Stage2, but later construction/PF valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 002780 / 002410
```

No hard 4C candidate is proposed. R10 loop 92 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L9 construction/PF cases, Stage2 requires verified PF cashflow repair, funding capacity, order quality, balance-sheet repair, margin, or revision bridge. Regional builder, small builder, PF normalization, housing recovery, or construction beta label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rule = C30 should split true PF cashflow/order-quality/balance-repair positives from regional-builder false Stage2 and small-builder PF event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 18.65 | -17.95 | 0.67 | mixed; C30 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 18.65 | -17.95 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L9 PF/order balance bridge required | 2 | 25.16 | -7.71 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C30 bridge vs event-cap split | 2 | 25.16 | -7.71 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing construction/PF themes as positive | 1 | 42.22 | -0.74 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 014790 PF/order balance bridge | 66 | Stage2-Watch | 75 | Stage2-Actionable | 42.22 | -0.74 | mid_builder_PF_order_balance_repair_positive |
| 002780 regional-builder false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 8.09 | -14.68 | regional_builder_PF_false_stage2 |
| 002410 small-builder PF cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 5.63 | -38.42 | small_builder_PF_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDER_BALANCE_REPAIR_BRIDGE_VS_REGIONAL_BUILDER_FALSE_STAGE2_AND_SMALL_BUILDER_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C30 mid-builder PF/order balance-repair positive, regional-builder PF false Stage2, and small-builder PF event-cap 4B split while avoiding top repeated C30 symbols."}
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
residual_error_types_found: mid_builder_PF_order_balance_repair_positive, regional_builder_PF_false_stage2, small_builder_PF_event_cap_4B
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
shadow_weight,stage2_required_bridge,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,C30_requires_PF_cashflow_order_quality_balance_repair_margin_bridge,0,"C30 Stage2 should require PF cashflow repair, funding capacity, order quality, balance-sheet repair, margin, or revision bridge, not construction/PF beta label alone","HL D&I positive worked; Chinhung Enterprise and Bumyung Construction event/watch rows failed positive-stage promotion","R10L92_C30_HLDNI_2024_STAGE2_ACTIONABLE_MID_BUILDER_PF_ORDER_BALANCE_REPAIR|R10L92_C30_CHINHUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_BUILDER_PF_WATCH|R10L92_C30_BUMYANG_2024_STAGE4B_SMALL_BUILDER_PF_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,cap_bridge_missing_regional_builder_and_PF_event_premiums_as_4B_watch,0,"Regional/small-builder PF event premiums can peak before cashflow and balance repair is proven","Chinhung had event-like MFE then large MAE; Bumyung showed clean 4B event-cap behavior after January spike","R10L92_C30_CHINHUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_BUILDER_PF_WATCH|R10L92_C30_BUMYANG_2024_STAGE4B_SMALL_BUILDER_PF_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,block_positive_stage_when_construction_PF_watch_has_high_MAE_without_balance_bridge,0,"High or persistent MAE after bridge-missing construction/PF entries should block Stage2/Stage3 promotion unless PF cashflow and balance evidence survives","Chinhung MAE180=-32.27 and Bumyung MAE90=-38.42","R10L92_C30_CHINHUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_BUILDER_PF_WATCH|R10L92_C30_BUMYANG_2024_STAGE4B_SMALL_BUILDER_PF_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R10L92_C30_HLDNI_2024_MID_BUILDER_PF_ORDER_BALANCE_REPAIR_POSITIVE", "symbol": "014790", "company_name": "HL D&I", "round": "R10", "loop": "92", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDER_BALANCE_REPAIR_BRIDGE_VS_REGIONAL_BUILDER_FALSE_STAGE2_AND_SMALL_BUILDER_EVENT_CAP", "case_type": "structural_success_with_later_PF_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R10L92_C30_HLDNI_2024_STAGE2_ACTIONABLE_MID_BUILDER_PF_ORDER_BALANCE_REPAIR", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Mid-builder PF/order backlog and balance-sheet repair bridge produced strong 30D/90D MFE with very shallow entry MAE. C30 works when construction recovery maps into PF cashflow repair, order quality, funding capacity, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C30_positive_requires_PF_cashflow_order_quality_balance_repair_bridge_not_construction_beta_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1996~2012 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R10L92_C30_CHINHUNG_2024_REGIONAL_BUILDER_PF_FALSE_STAGE2", "symbol": "002780", "company_name": "진흥기업", "round": "R10", "loop": "92", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDER_BALANCE_REPAIR_BRIDGE_VS_REGIONAL_BUILDER_FALSE_STAGE2_AND_SMALL_BUILDER_EVENT_CAP", "case_type": "failed_rerating_regional_builder_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R10L92_C30_CHINHUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_BUILDER_PF_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Regional builder / PF-normalization watch had only event-like MFE and then large 180D MAE. C30 Stage2 should not be awarded without verified PF cashflow repair, debt-maturity relief, order quality, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_regional_builder_PF_watch_counts_without_cashflow_order_quality_balance_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1998~2015 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R10L92_C30_BUMYANG_2024_SMALL_BUILDER_PF_EVENT_CAP_4B", "symbol": "002410", "company_name": "범양건영", "round": "R10", "loop": "92", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDER_BALANCE_REPAIR_BRIDGE_VS_REGIONAL_BUILDER_FALSE_STAGE2_AND_SMALL_BUILDER_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R10L92_C30_BUMYANG_2024_STAGE4B_SMALL_BUILDER_PF_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Small-builder / PF event premium capped at the January spike and then suffered severe 90D/180D drawdown. C30 should route bridge-missing construction/PF event premiums to 4B unless PF cashflow, order backlog, balance-sheet repair and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_small_builder_PF_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1996~2017 corporate-action candidates; last tradable date is 2025-03-20 but 180D forward window is available for this early-2024 entry."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R10L92_C30_HLDNI_2024_STAGE2_ACTIONABLE_MID_BUILDER_PF_ORDER_BALANCE_REPAIR", "case_id": "R10L92_C30_HLDNI_2024_MID_BUILDER_PF_ORDER_BALANCE_REPAIR_POSITIVE", "symbol": "014790", "company_name": "HL D&I", "round": "R10", "loop": "92", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDER_BALANCE_REPAIR_BRIDGE_VS_REGIONAL_BUILDER_FALSE_STAGE2_AND_SMALL_BUILDER_EVENT_CAP", "sector": "mid_builder_PF_order_balance_repair", "primary_archetype": "PF_cashflow_order_quality_balance_repair_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-03", "entry_date": "2024-06-03", "entry_price": 2025.0, "evidence_available_at_that_date": "mid-builder PF cashflow repair, order backlog quality, funding/balance-sheet repair, housing recovery and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["PF_cashflow_repair_proxy", "order_quality_backlog_proxy", "funding_capacity_bridge", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "shallow_MAE90"], "stage4b_evidence_fields": ["later_construction_PF_valuation_watch", "post_peak_drawdown_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014790/2024.csv", "profile_path": "atlas/symbol_profiles/014/014790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 31.36, "MFE_90D_pct": 42.22, "MFE_180D_pct": 42.22, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -0.74, "MAE_90D_pct": -0.74, "MAE_180D_pct": -0.74, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-23", "peak_price": 2880.0, "drawdown_after_peak_pct": -28.13, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_construction_PF_valuation_4B_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "PF_repair_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_mid_builder_PF_order_balance_repair_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1996_2012_CA", "same_entry_group_id": "R10L92_C30_014790_2024-06-03_2025", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L92_C30_CHINHUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_BUILDER_PF_WATCH", "case_id": "R10L92_C30_CHINHUNG_2024_REGIONAL_BUILDER_PF_FALSE_STAGE2", "symbol": "002780", "company_name": "진흥기업", "round": "R10", "loop": "92", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDER_BALANCE_REPAIR_BRIDGE_VS_REGIONAL_BUILDER_FALSE_STAGE2_AND_SMALL_BUILDER_EVENT_CAP", "sector": "regional_builder_PF_normalization_watch", "primary_archetype": "regional_builder_PF_watch_without_cashflow_order_quality_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 1063.0, "evidence_available_at_that_date": "regional builder / PF normalization watch and small-construction sector beta proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["regional_builder_PF_watch", "construction_beta_rebound", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "cashflow_order_quality_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002780/2024.csv", "profile_path": "atlas/symbol_profiles/002/002780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.09, "MFE_90D_pct": 8.09, "MFE_180D_pct": 8.09, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -10.72, "MAE_90D_pct": -14.68, "MAE_180D_pct": -32.27, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-26", "peak_price": 1149.0, "drawdown_after_peak_pct": -37.34, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "regional_builder_PF_watch_was_false_stage2_due_missing_cashflow_order_quality_balance_bridge", "four_b_evidence_type": ["regional_construction_beta", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_regional_builder_PF_watch_without_balance_bridge", "current_profile_verdict": "current_profile_false_positive_if_regional_builder_PF_watch_counts_without_cashflow_order_quality_balance_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1998_2015_CA", "same_entry_group_id": "R10L92_C30_002780_2024-02-26_1063", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L92_C30_BUMYANG_2024_STAGE4B_SMALL_BUILDER_PF_EVENT_CAP", "case_id": "R10L92_C30_BUMYANG_2024_SMALL_BUILDER_PF_EVENT_CAP_4B", "symbol": "002410", "company_name": "범양건영", "round": "R10", "loop": "92", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDER_BALANCE_REPAIR_BRIDGE_VS_REGIONAL_BUILDER_FALSE_STAGE2_AND_SMALL_BUILDER_EVENT_CAP", "sector": "small_builder_PF_event_premium", "primary_archetype": "small_builder_PF_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-02", "entry_date": "2024-01-02", "entry_price": 2220.0, "evidence_available_at_that_date": "small-builder / construction PF event premium and sector recovery watch after early-January spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["small_builder_PF_event_premium", "construction_recovery_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "PF_cashflow_balance_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002410/2024.csv", "profile_path": "atlas/symbol_profiles/002/002410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.63, "MFE_90D_pct": 5.63, "MFE_180D_pct": 5.63, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -23.87, "MAE_90D_pct": -38.42, "MAE_180D_pct": -49.82, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-02", "peak_price": 2345.0, "drawdown_after_peak_pct": -57.36, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_small_builder_PF_event_cap", "four_b_evidence_type": ["small_builder_PF_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_small_builder_PF_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_small_builder_PF_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1996_2017_CA", "same_entry_group_id": "R10L92_C30_002410_2024-01-02_2220", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L92_C30_HLDNI_2024_MID_BUILDER_PF_ORDER_BALANCE_REPAIR_POSITIVE", "trigger_id": "R10L92_C30_HLDNI_2024_STAGE2_ACTIONABLE_MID_BUILDER_PF_ORDER_BALANCE_REPAIR", "symbol": "014790", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 30, "backlog_visibility_score": 55, "margin_bridge_score": 50, "revision_score": 45, "relative_strength_score": 65, "customer_quality_score": 30, "policy_or_regulatory_score": 15, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 75, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "mid_builder_PF_order_balance_repair_positive", "MFE_90D_pct": 42.22, "MAE_90D_pct": -0.74, "score_return_alignment_label": "mid_builder_PF_order_balance_repair_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L92_C30_CHINHUNG_2024_REGIONAL_BUILDER_PF_FALSE_STAGE2", "trigger_id": "R10L92_C30_CHINHUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_BUILDER_PF_WATCH", "symbol": "002780", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "regional_builder_PF_false_stage2", "MFE_90D_pct": 8.09, "MAE_90D_pct": -14.68, "score_return_alignment_label": "regional_builder_PF_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_regional_builder_PF_watch_counts_without_cashflow_order_quality_balance_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L92_C30_BUMYANG_2024_SMALL_BUILDER_PF_EVENT_CAP_4B", "trigger_id": "R10L92_C30_BUMYANG_2024_STAGE4B_SMALL_BUILDER_PF_EVENT_CAP", "symbol": "002410", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "small_builder_PF_event_cap_4B_guard", "MFE_90D_pct": 5.63, "MAE_90D_pct": -38.42, "score_return_alignment_label": "small_builder_PF_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_small_builder_PF_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": "92", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDER_BALANCE_REPAIR_BRIDGE_VS_REGIONAL_BUILDER_FALSE_STAGE2_AND_SMALL_BUILDER_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["mid_builder_PF_order_balance_repair_positive", "regional_builder_PF_false_stage2", "small_builder_PF_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_loop = 92
next_round = R11
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
